# P-A-2017-65448-6ed1d510

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For ofﬁce use only For ofﬁce use only

<!-- b000003 | title | pages [1] -->
65448

<!-- b000004 | prose | pages [1] -->
T1 F1

<!-- b000005 | prose | pages [1] -->
T2 F2

<!-- b000006 | prose | pages [1] -->
Problem Chosen T3 F3

<!-- b000007 | title | pages [1] -->
A

<!-- b000008 | prose | pages [1] -->
T4 F4

<!-- b000009 | heading | pages [1] -->
2017 Mathematical Contest in Modeling (MCM) Summary Sheet

<!-- b000010 | front_matter | pages [1] -->
(Attach a copy of this page to each copy of your solution paper.)

<!-- b000011 | heading | pages [1] -->
Abstract

<!-- b000012 | prose | pages [1] -->
The Kariba Dam on the Zambezi River is confronted with foundation errosion and control limitation cur- rently, so a strategy to maintain water management on the Zambezi River is of great value for the whole Zambezi basin. Based on the detailed data provided by World Bank, we conduct the assessment of three op- tions (repairing the dam, rebuilding the dam or replacing the dam with several smaller dams along the river) and provide a reasonable and detailed model to construct a new dam system with some emergency strategies.

<!-- b000013 | prose | pages [1] -->
To begin with, a brief assessment report with potential costs and beneﬁts is offered according to abundant references and reliable data. The evaluation of repairing the Kariba Dam is completed refering to the Kariba Dam Rehabilitation Project in the charge of World Bank, while the assessment of rebuilding the dam is realized following the actual capital investment expenditure of the Stage 1 of the Kariba Project. And the assessment of replacing the dam is carefully estimated according to the model to construct the new dam system.

<!-- b000014 | prose | pages [1] -->
Then, we concentrate on the establishment of the model for new dam system.

<!-- b000015 | prose | pages [1] -->
Firstly, a Hydrodynamic Model (HM) of the Zambezi River is established in order to estimate the ﬂowing and depth situation of the river. The model is constructed based on ﬂow conservation and energy conservation, which separately producing continuity equation and energy conservation equation, taking the normal water cycles and on-way resistance into account. Moreover, we obtain the numerical solution of the Hydrodynamic Model with Mathematica, and get the approximate current velocity curve and river depth curve along the river.

<!-- b000016 | prose | pages [1] -->
Secondly, the site selection and number conﬁrmation of the new dams is realized according to the ﬂowing and depth situation estimated by HM, geological data and hydrological data. The indexes for evaluation are determined after consulting professional literatures, and Grey Relation Grade Analysis is utilized in the selection among candidate sites so that all the indexes can be considered comprehensively and objectively.

<!-- b000017 | prose | pages [1] -->
Thirdly, a Difference Model (DM) of the Zambezi River with a dam system is established to provide suf- ﬁcient details for the conﬁrmation of dam construction and modulating strategies. We separate the river into several segments by the dams. A difference approximation of HM is applied to describe each segment of the river. A hydraulic emprical formula is utilized to determine the discharges of the dam. In this way, the re- currence formulas can be obtained to easily determine the runoff and river depth along the river with given environmental and initial conditions.

<!-- b000018 | prose | pages [1] -->
Fourthly, the type of each dam is conﬁrmed with corrected DM, with the overall water management capa- bilities, protection and water management options for Lake Kariba evaluated and special topograph consid- ered. Considering the loss of energy in collision, tributaries and the runoff variation with rainfall at headstram and tributaries, DM is corrected to adapt to the reality. With the results calculated by corrected DM, the type of each dam is conﬁrmed balancing the safety and costs. Each type of dam has three gears of discharges, which increases the water management options.

<!-- b000019 | prose | pages [1] -->
Finally, the strategies to handle such emergency water ﬂow situations as ﬂooding and drought are designed with the new dam system established above. When solving a known catastrophe, the exhaustive method is utilized to rule out the best strategies which realized by the gear variation of the dam. It is validated that the new dam system can handle most extreme conditions and the method we adopted to establish the strategy is of low sensibility considering reasonable errors.

<!-- b000020 | furniture | pages [2] -->
Team # 65448

<!-- b000021 | furniture | pages [2] -->
Page 1 of 25

<!-- b000022 | contents | pages [2] -->
A Multi-Dam System Design for Zambezi River

<!-- b000023 | contents | pages [2] -->
January 24, 2017

<!-- b000024 | heading | pages [2] -->
Contents

<!-- b000025 | contents | pages [2] -->
1 Assessment Report of Three Options

<!-- b000026 | contents | pages [2] -->
1

<!-- b000027 | contents | pages [2] -->
1.1

<!-- b000028 | contents | pages [2] -->
Repairing the Existing Kariba Dam . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000029 | contents | pages [2] -->
1

<!-- b000030 | contents | pages [2] -->
1.1.1

<!-- b000031 | contents | pages [2] -->
Institutional Project Support (estimated cost US$69.6 million) . . . . . . . . . .

<!-- b000032 | contents | pages [2] -->
1

<!-- b000033 | contents | pages [2] -->
1.1.2

<!-- b000034 | contents | pages [2] -->
Plunge Pool Reshaping (estimated cost US$100.0 million) . . . . . . . . . . . . .

<!-- b000035 | contents | pages [2] -->
1

<!-- b000036 | contents | pages [2] -->
1.1.3

<!-- b000037 | contents | pages [2] -->
Spillway Refurbishment (estimated cost US$124.6 million) . . . . . . . . . . . .

<!-- b000038 | contents | pages [2] -->
1

<!-- b000039 | contents | pages [2] -->
1.1.4

<!-- b000040 | contents | pages [2] -->
Beneﬁts

<!-- b000041 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000042 | contents | pages [2] -->
1

<!-- b000043 | contents | pages [2] -->
1.2

<!-- b000044 | contents | pages [2] -->
Rebuilding the Existing Kariba Dam . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000045 | contents | pages [2] -->
1

<!-- b000046 | contents | pages [2] -->
1.3

<!-- b000047 | contents | pages [2] -->
Removing the Kariba Dam & Replacing It with A Series of Ten to Twenty Smaller Dams

<!-- b000048 | contents | pages [2] -->
Along the Zambezi River . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000049 | contents | pages [2] -->
2

<!-- b000050 | contents | pages [2] -->
2 Introduction

<!-- b000051 | contents | pages [2] -->
2

<!-- b000052 | contents | pages [2] -->
2.1

<!-- b000053 | contents | pages [2] -->
Restatement of the problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000054 | contents | pages [2] -->
2

<!-- b000055 | contents | pages [2] -->
2.2

<!-- b000056 | contents | pages [2] -->
Our Approach . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000057 | contents | pages [2] -->
3

<!-- b000058 | contents | pages [2] -->
3 General Assumption

<!-- b000059 | contents | pages [2] -->
4

<!-- b000060 | contents | pages [2] -->
4 Notations

<!-- b000061 | contents | pages [2] -->
4

<!-- b000062 | contents | pages [2] -->
5 The Model

<!-- b000063 | contents | pages [2] -->
5

<!-- b000064 | contents | pages [2] -->
5.1

<!-- b000065 | contents | pages [2] -->
Hydrodynamic Model of the Zambezi River . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000066 | contents | pages [2] -->
5

<!-- b000067 | contents | pages [2] -->
5.1.1

<!-- b000068 | contents | pages [2] -->
Continuity Equation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000069 | contents | pages [2] -->
5

<!-- b000070 | contents | pages [2] -->
5.1.2

<!-- b000071 | contents | pages [2] -->
Energy Conservation Equation . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000072 | contents | pages [2] -->
6

<!-- b000073 | contents | pages [2] -->
5.1.3

<!-- b000074 | contents | pages [2] -->
Boundary Condition and Initial Condition

<!-- b000075 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . .

<!-- b000076 | contents | pages [2] -->
6

<!-- b000077 | contents | pages [2] -->
5.1.4

<!-- b000078 | contents | pages [2] -->
Calculation of the Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000079 | contents | pages [2] -->
7

<!-- b000080 | contents | pages [2] -->
5.2

<!-- b000081 | contents | pages [2] -->
Selection System of the Dam Site . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000082 | contents | pages [2] -->
8

<!-- b000083 | contents | pages [2] -->
5.2.1

<!-- b000084 | contents | pages [2] -->
Evaluation indexes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000085 | contents | pages [2] -->
9

<!-- b000086 | contents | pages [2] -->
5.2.2

<!-- b000087 | contents | pages [2] -->
Candidate Site . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000088 | contents | pages [2] -->
9

<!-- b000089 | contents | pages [2] -->
5.2.3

<!-- b000090 | contents | pages [2] -->
Grey Relation Grade Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000091 | contents | pages [2] -->
10

<!-- b000092 | contents | pages [2] -->
5.3

<!-- b000093 | contents | pages [2] -->
Difference Model of the Dam System . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000094 | contents | pages [2] -->
11

<!-- b000095 | contents | pages [2] -->
5.3.1

<!-- b000096 | contents | pages [2] -->
Equations in the River (Without the Dam) . . . . . . . . . . . . . . . . . . . . . .

<!-- b000097 | contents | pages [2] -->
12

<!-- b000098 | contents | pages [2] -->
5.3.2

<!-- b000099 | contents | pages [2] -->
Equations in the Dam Region . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000100 | contents | pages [2] -->
13

<!-- b000101 | contents | pages [2] -->
5.3.3

<!-- b000102 | contents | pages [2] -->
Recurrence Formulas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000103 | contents | pages [2] -->
13

<!-- b000104 | contents | pages [2] -->
5.4

<!-- b000105 | contents | pages [2] -->
Dam Construction & Manipulating System . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000106 | contents | pages [2] -->
14

<!-- b000107 | contents | pages [2] -->
5.4.1

<!-- b000108 | contents | pages [2] -->
Conﬁrm the Parameters of Different Dam Types . . . . . . . . . . . . . . . . . .

<!-- b000109 | contents | pages [2] -->
14

<!-- b000110 | contents | pages [2] -->
5.4.2

<!-- b000111 | contents | pages [2] -->
Conﬁrm the Type Selection of Each Dam

<!-- b000112 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . .

<!-- b000113 | contents | pages [2] -->
14

<!-- b000114 | contents | pages [2] -->
5.4.3

<!-- b000115 | contents | pages [2] -->
Evaluate the Protection & Water Management Options for Lake Kariba . . . . .

<!-- b000116 | contents | pages [2] -->
17

<!-- b000117 | contents | pages [2] -->
5.4.4

<!-- b000118 | contents | pages [2] -->
Strategies to Handle Emergency Water Flow Situations . . . . . . . . . . . . . .

<!-- b000119 | contents | pages [2] -->
17

<!-- b000120 | contents | pages [2] -->
6 Testing the model

<!-- b000121 | contents | pages [2] -->
19

<!-- b000122 | contents | pages [2] -->
6.1

<!-- b000123 | contents | pages [2] -->
Error analysis

<!-- b000124 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000125 | contents | pages [2] -->
19

<!-- b000126 | contents | pages [2] -->
6.2

<!-- b000127 | contents | pages [2] -->
Sensitivity Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000128 | contents | pages [2] -->
20

<!-- b000129 | contents | pages [2] -->
Sensitivity Analysis for Hi . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000130 | contents | pages [2] -->
6.2.1

<!-- b000131 | contents | pages [2] -->
20

<!-- b000132 | contents | pages [2] -->
Sensitivity Analysis for hi . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000133 | contents | pages [2] -->
6.2.2

<!-- b000134 | contents | pages [2] -->
20

<!-- b000135 | contents | pages [3] -->
Sensitivity Analysis for Qi . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000136 | contents | pages [3] -->
6.2.3

<!-- b000137 | contents | pages [3] -->
21

<!-- b000138 | contents | pages [3] -->
6.3

<!-- b000139 | contents | pages [3] -->
Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000140 | contents | pages [3] -->
21

<!-- b000141 | contents | pages [3] -->
6.3.1

<!-- b000142 | contents | pages [3] -->
Strengths and weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000143 | contents | pages [3] -->
21

<!-- b000144 | contents | pages [3] -->
6.3.2

<!-- b000145 | contents | pages [3] -->
Future Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000146 | contents | pages [3] -->
22

<!-- b000147 | heading | pages [3] -->
Appendices

<!-- b000148 | prose | pages [3] -->
23

<!-- b000149 | prose | pages [3] -->
0

<!-- b000150 | furniture | pages [4] -->
Team # 65448

<!-- b000151 | furniture | pages [4] -->
Page 1 of 25

<!-- b000152 | heading | pages [4] -->
1 Assessment Report of Three Options

<!-- b000153 | heading | pages [4] -->
1.1 Repairing the Existing Kariba Dam

<!-- b000154 | prose | pages [4] -->
1 At present, the foundation of the Kariba Dam is gradually undermined by scouring and erosion of water, so that operations are limited to only three of the six, non-adjacent gates. The Kariba Dam is also suffering frequent maintenance operations and potential limitations on the operational control of the reservoir. Therefore, plunge pool reshaping and spillway refurbishment are necessities. What is more, institutional project support are also signiﬁcant to ensure the project running smoothly.

<!-- b000155 | heading | pages [4] -->
1.1.1 Institutional Project Support (estimated cost US$69.6 million)

<!-- b000156 | prose | pages [4] -->
1 Institutional project support mainly provides overall management, supervision, professional consultant, comprehensive assessment and risk evaluation for the project.

<!-- b000157 | heading | pages [4] -->
1.1.2 Plunge Pool Reshaping (estimated cost US$100.0 million)

<!-- b000158 | prose | pages [4] -->
1 Financing in the component is primarily utilized for goods, works and consultants services, which is constituted with four parts: a. Plunge Pool Reshaping Civil Works Contract: The measures are required to reshape the plunge pool through excavation of the downstream face and north and south bank sides of the pool; b. Additional Engineering Studies; c. Monitoring Services Contract; d. Visibility & Communications.

<!-- b000159 | heading | pages [4] -->
1.1.3 Spillway Refurbishment (estimated cost US$124.6 million)

<!-- b000160 | prose | pages [4] -->
1 Financing in the component is mainly used for goods, works and non-consulting services as- sociated with the refurbishment of the spillway, which is composed of two parts: a. Spillway Re- furbishment Contract: The works will be conducted at one gate at a time, in a sequenced manner starting with the gates that today show the largest need for rehabilitation; b. Additional Engineering Studies.

<!-- b000161 | heading | pages [4] -->
1.1.4 Beneﬁts

<!-- b000162 | prose | pages [4] -->
1 Besides the elimination of potential danger and operational limitation which is mentioned above, the repairing of the dam also reinforce the integrated infrastructure platform within the Zambezi River basin. The beneﬁts through avoided disaster and continued power production are substantial, considering the estimated 3 million people living in the potential impact area and the economic value in excess of US$8 billion.

<!-- b000163 | heading | pages [4] -->
1.2 Rebuilding the Existing Kariba Dam

<!-- b000164 | prose | pages [4] -->
2 After 50 years of operation serving the southern African region, the geological conditions under the Kariba dam have been changed with the scouring and erosion of the water, so that the initial design of the dam is not appropriate for the new conditions. In this way, rebuilding the dam is a reasonable alternative to replace and even reinforce the function of the old one, and Lake Kariba is also utilized as a reservior. The ﬁnancing of the project will be primarily utilized for civil engineering works and electrical and mechanical works.

<!-- b000165 | prose | pages [4] -->
• Civil Engineering Works (estimated cost US$729.1 million): The component will include the costs of access roads, township, dam wall, south bank power station and engineering fees.

<!-- b000166 | prose | pages [4] -->
• Electrical and Mechanical Works (estimated cost US$380.6 million): The component will in- clude the costs of generation plant and equipment, transmission system and engineering fees.

<!-- b000167 | furniture | pages [5] -->
Team # 65448

<!-- b000168 | furniture | pages [5] -->
Page 2 of 25

<!-- b000169 | prose | pages [5] -->
The rebuilt dam can be designed to suit the new geological conditions and eliminate the over- whelming erosion confronted in the previous design. The beneﬁts through avoided frequent main- tenance of the dam and improved manipulating capability are substantial, given the lifespan and signiﬁcance of the dam for the approximately 3 million local residents.

<!-- b000170 | prose | pages [5] -->
1.3 Removing the Kariba Dam & Replacing It with A Series of Ten to Twenty Smaller Dams Along the Zambezi River

<!-- b000171 | prose | pages [5] -->
During the construction of the Kariba Dam, the dam suffered from three huge ﬂoodings exceeding the design ﬂood. And the dam became broken quickly in ﬁfty years, which was quite shorter than the designed lifespan.1 All these facts ﬁgure out that more dams should be constructed on the Zambezi River in order to prevent the unexpected ﬂoodings. In this way, replacing the Kariba Dam with a series of ten to twenty smaller dams is an alternative which are more likely to balance the costs and safety.

<!-- b000172 | prose | pages [5] -->
As a series of so many dams is quite rare in the world, the costs can only be estimated approx- imately by the number and size of the dams. Financing of the project is mainly utilized for dam construction and relevant institutional project support.

<!-- b000173 | prose | pages [5] -->
• Dam Construction (estimated cost US$860 million): The costs of the dam construction are as- sumed to increase exponentially with the dam size increasing. Therefore, the costs of different dam types (which are introduced in the following model) are listed in Table 1. According to the following model, eight III dams and two IV dams are constructed, which cost US$860 million.

<!-- b000174 | prose | pages [5] -->
• Institutional Project Support (estimated cost US$69.6 million).

<!-- b000175 | prose | pages [5] -->
The area of Reservior/m2 Warning water levelHmi/m Types of dam Costs/million US$

<!-- b000176 | prose | pages [5] -->
1 × 108 I 60 10

<!-- b000177 | prose | pages [5] -->
1 × 107 II 50 1

<!-- b000178 | prose | pages [5] -->
1 × 106 III 40 0.8

<!-- b000179 | prose | pages [5] -->
1 × 105 IV 30 0.6

<!-- b000180 | caption | pages [5] -->
Table 1: Costs of different dam types

<!-- b000181 | prose | pages [5] -->
The construction of the dam system can balance between the safety and costs and have excellent functions to prevent unexpected ﬂoodings, whose beneﬁts through avoided catastrophe is substan- tial, considering the powerful water management capabilities and more abundant hydropower.

<!-- b000182 | heading | pages [5] -->
2 Introduction

<!-- b000183 | heading | pages [5] -->
2.1 Restatement of the problem

<!-- b000184 | prose | pages [5] -->
Kariba Dam, constructed in 1955-59, with a storage capacity of 180km3, is one of the largest dams in Africa. Now it is in dire need of maintenance. The Zambezi River Authority (ZRA) faces three available options to address this situation:

<!-- b000185 | prose | pages [5] -->
• (Option 1) Repairing the existing Kariba Dam;

<!-- b000186 | prose | pages [5] -->
• (Option 2) Rebuilding the existing Kariba Dam;

<!-- b000187 | prose | pages [5] -->
• (Option 3) Removing the Kariba Dam and replacing it with a series of ten to twenty smaller dams along the Zambezi River.

<!-- b000188 | furniture | pages [6] -->
Team # 65448

<!-- b000189 | furniture | pages [6] -->
Page 3 of 25

<!-- b000190 | prose | pages [6] -->
On the one hand, we need to brieﬂy assess all the three options above and provide an overview of potential costs and beneﬁts associated with each option.

<!-- b000191 | prose | pages [6] -->
On the other hand, the problem needs us to conduct a detailed analysis on option 3. We need to give a recommendation on how to design a new system of dam. The new system must meet following requirements:

<!-- b000192 | prose | pages [6] -->
• Having the same overall water management capabilities as the existing Kariba Dam, In our report, we use the total live storage of reservoirs in front of dams which marks the ability of a dam system to dynamically regulate the water ﬂows within the basin to describe the overall water management capabilities.

<!-- b000193 | prose | pages [6] -->
• Providing the same or greater levels of protection and water management options for Lake Kariba. For Lake Kariba, the more stable the inﬂow is with the variation of seasons, the better conditions like ﬁshing conditions Lake Kariba can provide for local people. So our new dam system is expected to make the inﬂow of Lake Kariba more stable than the original Kariba Dam.

<!-- b000194 | prose | pages [6] -->
• Properly addressing known or predicted normal water cycles.

<!-- b000195 | prose | pages [6] -->
• Having the ability to handle emergency water ﬂow situations including ﬂooding and prolonged low water conditions. Extreme conditions derive from abnormal rainfall. When rainfall of some region increases sharply, our dam system is expected to be adjusted to make sure that no region is ﬂooded as possible and when some regions experience prolonged drought our system should be adjusted to provide more runoff for that region as possible.

<!-- b000196 | prose | pages [6] -->
In our main report, we are required to provide:

<!-- b000197 | prose | pages [6] -->
• The number and placement of the new dams along the Zambezi River.

<!-- b000198 | prose | pages [6] -->
• A guidance to the ZRA managers that explains and justiﬁes the actions that should be taken to properly handle emergency water ﬂow situations.

<!-- b000199 | prose | pages [6] -->
• Information about the location and last time for a speciﬁc extreme condition in our guidance.

<!-- b000200 | heading | pages [6] -->
2.2 Our Approach

<!-- b000201 | prose | pages [6] -->
Based on the detailed data provided by World Bank, we conduct the assessment of three options, and provide a reasonable and detailed model to construct a new dam system with some emergency strategies.

<!-- b000202 | prose | pages [6] -->
To begin with, we offer a brief assessment report with potential costs and beneﬁts according to abundant references and reliable data. We complete the evaluation of repairing the Kariba Dam refering to the Kariba Dam Rehabilitation Project in the charge of World Bank, while we realize the assessment of rebuilding the dam following the actual capital investment expenditure of the Stage 1 of the Kariba Project. And the assessment of replacing the dam is carefully estimated according to the model to construct the new dam system.

<!-- b000203 | prose | pages [6] -->
Then, we concentrate on the establishment of the model for new dam system.

<!-- b000204 | prose | pages [6] -->
Firstly, we establish a Hydrodynamic Model (HM) of the Zambezi River in order to estimate the ﬂowing and depth situation of the river. The model is constructed based on ﬂow conservation and energy conservation, which separately producing continuity equation and energy conservation equation, taking the normal water cycles and on-way resistance into account. Moreover, we obtain the numerical solution of the Hydrodynamic Model with Mathematica, and get the approximate current velocity curve and river depth curve along the river.

<!-- b000205 | prose | pages [6] -->
Secondly, we realize the site selection and number conﬁrmation of the new dams according to the ﬂowing and depth situation estimated by HM, geological data and hydrological data. We determine the evaluation indexes after consulting professional literatures, and Grey Relation Grade Analysis is utilized in the selection among candidate sites so that all the indexes can be considered comprehen- sively and objectively.

<!-- b000206 | furniture | pages [7] -->
Team # 65448

<!-- b000207 | furniture | pages [7] -->
Page 4 of 25

<!-- b000208 | prose | pages [7] -->
Thirdly, we establish a Difference Model (DM) of the Zambezi River with a dam system to provide sufﬁcient details for the conﬁrmation of dam construction and modulating strategies. We separate the river into several segments by the dams. A difference approximation of HM is applied to describe each segment of the river. We utilize a hydraulic emprical formula to determine the discharges of the dam. In this way, the recurrence formulas can be obtained to easily determine the runoff and river depth along the river with given environmental and initial conditions.

<!-- b000209 | prose | pages [7] -->
Fourthly, the type of each dam is conﬁrmed with corrected DM, with the overall water manage- ment capabilities, protection and water management options for Lake Kariba evaluated and special topograph considered. Considering the loss of energy in collision, tributaries and the runoff varia- tion with rainfall at headstram and tributaries, we correct DM to adapt to the reality. With the results calculated by corrected DM, we conﬁrm the type of each dam balancing the safety and costs. Each type of dam has three gears of discharges, which increases the water management options.

<!-- b000210 | prose | pages [7] -->
Finally, the strategies to handle such emergency water ﬂow situations as ﬂooding and drought are designed with the new dam system established above. When solving a known catastrophe, we utilize the exhaustive method to rule out the best strategies which realized by the gear variation of the dam. It is validated that the new dam system can handle most extreme conditions and the method we adopted to establish the strategy is of low sensibility considering reasonable errors.

<!-- b000211 | heading | pages [7] -->
3 General Assumption

<!-- b000212 | prose | pages [7] -->
• All dams are double curvature concrete arch dams and each dam is built with a hydropower station and a reservoir, in consistence with the original Kariba Dam.

<!-- b000213 | prose | pages [7] -->
• The costs of the dams have positive correlation with the size of the dams.

<!-- b000214 | prose | pages [7] -->
• The water is forced by on-way resistance, which is proportial to current velocity and the coefﬁ- cient is a constant.

<!-- b000215 | prose | pages [7] -->
• The evaporation exists anytime and is approximately a constant.

<!-- b000216 | heading | pages [7] -->
4 Notations

<!-- b000217 | heading | pages [7] -->
Notations

<!-- b000218 | prose | pages [7] -->
Deﬁnitions

<!-- b000219 | prose | pages [7] -->
x The distance away from the headstream

<!-- b000220 | prose | pages [7] -->
L The width of the river

<!-- b000221 | prose | pages [7] -->
h The river depth

<!-- b000222 | prose | pages [7] -->
v Current velocity

<!-- b000223 | prose | pages [7] -->
ρ The density of the water

<!-- b000224 | prose | pages [7] -->
q Rainfall

<!-- b000225 | prose | pages [7] -->
δ Evaporation

<!-- b000226 | prose | pages [7] -->
k on-way resistance coefﬁcient

<!-- b000227 | prose | pages [7] -->
Q Runoff

<!-- b000228 | prose | pages [7] -->
H The depth of the reservoir attached to dam

<!-- b000229 | prose | pages [7] -->
θ The gate opening of the dam

<!-- b000230 | prose | pages [7] -->
b The width of the gate hole

<!-- b000231 | prose | pages [7] -->
A The outﬂow coefﬁcient of the dam

<!-- b000232 | furniture | pages [8] -->
Team # 65448

<!-- b000233 | furniture | pages [8] -->
Page 5 of 25

<!-- b000234 | heading | pages [8] -->
5 The Model

<!-- b000235 | heading | pages [8] -->
5.1 Hydrodynamic Model of the Zambezi River

<!-- b000236 | prose | pages [8] -->
In this section, we establish a hydrodynamic model of the current velocity and river depth which vary with the space and time, which is based on ﬂow conservation and energy conservation. When the current velocity and river depth at the headstream is given, the whole Zamberi River can be depicted with the current velocity and river depth anywhere and anytime.

<!-- b000237 | heading | pages [8] -->
5.1.1 Continuity Equation

<!-- b000238 | prose | pages [8] -->
Considering a short segment of the river from x to x + ∆x (x and x + ∆x are all the distances away from the headstream), the ﬂow conservation is given by

<!-- b000239 | prose | pages [8] -->
Qin + qrain −qevaporation −Qout = ρ∆V (1)

<!-- b000240 | prose | pages [8] -->
where

<!-- b000241 | prose | pages [8] -->
• Qin is the quantity of water ﬂowing into the segment,

<!-- b000242 | prose | pages [8] -->
• qrain is the rainfall quantity of the segment,

<!-- b000243 | prose | pages [8] -->
• qevaporation is the evaporation quantity of the segment,

<!-- b000244 | prose | pages [8] -->
• Qout is the quantity of water ﬂowing out of the segment,

<!-- b000245 | prose | pages [8] -->
• ρ is the density of water,

<!-- b000246 | prose | pages [8] -->
• V is the volume of water in this segment.

<!-- b000247 | prose | pages [8] -->
Qin, qrain, qevaporation, Qout and ∆V in the time period of ∆t can be written as

<!-- b000248 | prose | pages [8] -->
Qin = ρL(x)h(x, t)v(x, t)∆t (2)

<!-- b000249 | prose | pages [8] -->
qrain = ρq(x)L(x)∆x∆t (3)

<!-- b000250 | prose | pages [8] -->
qevaporation = ρδ(x)L(x)∆x∆t (4)

<!-- b000251 | prose | pages [8] -->
Qout = ρL(x + ∆x)h(x + ∆x, t)v(x + ∆x, t)∆t (5)

<!-- b000252 | prose | pages [8] -->
∆V = L(x)∆x[h(x, t + ∆t) −h(x, t)] (6)

<!-- b000253 | prose | pages [8] -->
The ﬂow conservation equation turns into

<!-- b000254 | prose | pages [8] -->
ρ[q(x) −δ(x)]L(x)∆x∆t + ρ[L(x)h(x, t)v(x, t) −L(x + ∆x)h(x + ∆x, t)v(x + ∆x, t)]∆t (7) = ρL(x)∆x[h(x, t + ∆t) −h(x, t)]

<!-- b000255 | prose | pages [8] -->
After simpliﬁcation, the equation is given by

<!-- b000256 | prose | pages [8] -->
−∂[L(x)h(x, t)v(x, t)] + [q(x) −δ(x)]L(x) = L(x)∂h(x, t) (8) ∂x ∂t

<!-- b000257 | prose | pages [8] -->
which is the continuity equation of the river.

<!-- b000258 | furniture | pages [9] -->
Team # 65448

<!-- b000259 | furniture | pages [9] -->
Page 6 of 25

<!-- b000260 | heading | pages [9] -->
5.1.2 Energy Conservation Equation

<!-- b000261 | prose | pages [9] -->
Also considering a short segment of the river from x to x + ∆x (x and x + ∆x are all the dis- tances away from the headstream), and neglecting the variation of the pressure with x, the energy conservation is written as

<!-- b000262 | prose | pages [9] -->
Wgravity + Wresistance = ∆Twater + ∆Train + ∆Tevaporation (9)

<!-- b000263 | prose | pages [9] -->
where

<!-- b000264 | prose | pages [9] -->
• Wgravity is the work done by the gravity of water,

<!-- b000265 | prose | pages [9] -->
• Wresistance is the work done by the on-way resistance,

<!-- b000266 | prose | pages [9] -->
• ∆Twater is the change of kinetic energy of the water in the segment,

<!-- b000267 | prose | pages [9] -->
• ∆Train is the change of kinetic energy of rain in the segment,

<!-- b000268 | prose | pages [9] -->
• ∆Tevaporation is the change of kinetic energy of water evaporated from the segment. Wgravity and ∆Twater in the time period of ∆t is given by Wgravity = −ρgL(x)h(x, t)v(x, t)∆t∆y (10) ∆Twater = 1 2ρL(x)h(x, t)v(x, t)∆(v2)∆t (11) = 1 2ρL(x)h(x, t)v2(x, t)∆t(∂v ∂t ∆t + ∂v ∂x∆x) Assuming that the on-way resistance per volume is proportional to the current velocity, which is

<!-- b000269 | prose | pages [9] -->
Fr = kv(x, t) (12)

<!-- b000270 | prose | pages [9] -->
Wresistance is expressed as Wresistance = −kL(x)h(x, t)v(x, t)∆x∆t (13) Supposing that the initial velocity of rain in the river is approximately zero, ∆Train is given by ∆Train = 1 2ρq(x)v2(x, t)∆x∆t (14)

<!-- b000271 | prose | pages [9] -->
Neglecting the velocity of vapour evaporated from the river, ∆Tevaporation is given by ∆Tevaporation = −1 2ρδ(x)v2(x, t)∆x∆t (15)

<!-- b000272 | prose | pages [9] -->
Thus, the energy conservation equation after simpliﬁcation is −gh(x, t)y′(x) −kh(x, t) = h(x, t)v(x, t)∂v ∂x + h(x, t)∂v ∂t + 1 2[q(x) −δ(x)]v(x, t) (16)

<!-- b000273 | heading | pages [9] -->
5.1.3 Boundary Condition and Initial Condition

<!-- b000274 | prose | pages [9] -->
In order to solve the above two equations, the boundary condition and initial condition of the river should be given. Boundary conditions refer to the current velocity and river depth at the head- stream, which can be measured in reality. Initial condition refer to the current velocity and river depth anywhere along the river when t = 0, which can also be provided by hydrological stations.

<!-- b000275 | prose | pages [9] -->
In our model, the current velocity and river depth at the headstream are assumed to be constant, which is  v(0, t) = v0  (17) h(0, t) = h0  The initial depth is also supposed to be consistent along the river, while the inital current velocity is set to have the distribution of free falling movement, which can be written as

<!-- b000276 | prose | pages [9] -->
 p v2 0 + 2g[y(0) −y(x)] v(x, 0) =  (18) h(x, 0) = h0 

<!-- b000277 | furniture | pages [10] -->
Team # 65448

<!-- b000278 | furniture | pages [10] -->
Page 7 of 25

<!-- b000279 | heading | pages [10] -->
5.1.4 Calculation of the Model

<!-- b000280 | prose | pages [10] -->
The hydrodynamic equations of the river are all partial different equations and approximately impossible to get the analytical solution, so we should obtain all the values of the known parameters in the equations so that we can get the numerical solution of the equations.

<!-- b000281 | prose | pages [10] -->
We observe the Zambezi River in Google Earth and acquire the altitude variations along the river, which gives y(x) with interpolation. The curve of y(x) (altitude variation) is shown in Figure 1.

<!-- b000282 | caption | pages [10] -->
Figure 1: Altitude variation

<!-- b000283 | prose | pages [10] -->
The width of the Zambezi River is almost constant along the river, which means L(x) = L.

<!-- b000284 | prose | pages [10] -->
The runoff, rainfall and evaporation along the river are obtained from the data provided by World Bank,3 which determines v0, h0, q(x), δ(x).In order to simplify the calculation, δ(x) is taken as a con- stant δ, which is the annual average evaporation. The rainfall data is provided by some hydrological stations, so the data is discrete, which is shown in Figure 1. In order to acquire the rough data of rain- fall anywhere along the river, we try to ﬁt the data points of rainfall and obtain the analysis formula, which is shown in Figure 2-6.

<!-- b000285 | caption | pages [10] -->
Figure 2: Spring rainfall

<!-- b000286 | caption | pages [10] -->
Figure 3: Summer rainfall

<!-- b000287 | furniture | pages [11] -->
Team # 65448

<!-- b000288 | furniture | pages [11] -->
Page 8 of 25

<!-- b000289 | caption | pages [11] -->
Figure 4: Fall rainfall

<!-- b000290 | caption | pages [11] -->
Figure 5: Winter rainfall

<!-- b000291 | caption | pages [11] -->
Figure 6: The annual rainfall along the river and the ﬁtting curve

<!-- b000292 | prose | pages [11] -->
Considering the data all above and some scientiﬁc constants (such as g and k), all the known parameters can be given:

<!-- b000293 | prose | pages [11] -->
• g = 9.8m/s, k = 1.0 × 10−6kg · m−3 · s−1

<!-- b000294 | prose | pages [11] -->
• v0 = 10m/s, h0 = 20m, L = 1km, δ = 3.2 × 10−9m/s

<!-- b000295 | prose | pages [11] -->
After a few approximation and estimation, the trend of the current velocity and depth along the river from the initial time to the ending time can be obtained, which is shown in Figure 7-8. According to the results, the trend of the current velocity and depth will approach a stable state as the time goes.

<!-- b000296 | caption | pages [11] -->
Figure 8: River Depth

<!-- b000297 | caption | pages [11] -->
Figure 7: Current Velocity

<!-- b000298 | heading | pages [11] -->
5.2 Selection System of the Dam Site

<!-- b000299 | prose | pages [11, 12] -->
The site selection of the dams is signiﬁcant in dam construction, which directly decides the func- tion and lifespan of the dams. As many parameters of river have been obtained in previous calcu- lation, we can evaluate the location from many aspects, so that a scientiﬁc and objective selection system of the dam site can be established based on Grey Relation Grade Analysis.4

<!-- b000300 | furniture | pages [12] -->
Team # 65448

<!-- b000301 | furniture | pages [12] -->
Page 9 of 25

<!-- b000303 | heading | pages [12] -->
5.2.1 Evaluation indexes

<!-- b000304 | prose | pages [12] -->
In order to smooth the channel and acquire the maximum hydropower resources, the dams should be established in the regions with steep terrain gap, large river depth and much rainfall, where the huge quantity of water and rapid current may make the channel so turbulent as to threaten the safety of transportation and residents nearby, yet ensuring the abundant hydropower resources at the same time. The situation is similar when the current acceleration is enormous.5 In addition to this, some special topographies are appropriate for dam construction. Lakes can be utilized as a natural reservior for the dam, pocket-like lowlands can contribute to water management and valleys can eliminate the construction amount.5 What is more, the smaller width the channel has, the lower the construction cost is.5 In this way, the following indexes are considered for the site selection:

<!-- b000305 | prose | pages [12] -->
• Terrain gap: y′(x), the derivative of y(x);

<!-- b000306 | prose | pages [12] -->
• River depth h(x) in stable state;

<!-- b000307 | prose | pages [12] -->
• Rainfall q(x);

<!-- b000308 | prose | pages [12] -->
• Current acceleration ∂v(x,t) ∂t

<!-- b000309 | prose | pages [12] -->
• Lakes;

<!-- b000310 | prose | pages [12] -->
• Pocket-like lowlands;

<!-- b000311 | prose | pages [12] -->
• Valleys;

<!-- b000312 | prose | pages [12] -->
• River width L(x) (which can be obtained from the map).

<!-- b000313 | prose | pages [12] -->
The topographic indexes are evaluated by checking whether the suitable topography exists. If the appropriate topography exists, the relevant index is 1; if not, zero.

<!-- b000314 | heading | pages [12] -->
5.2.2 Candidate Site

<!-- b000315 | prose | pages [12] -->
Several candidate sites should be determined to optimize the site selection. According to the relief map, rainfall, river depth calculated by the hydrodynamic model, considering the distances between adjacent dams, 26 advantageous sites are selected as candidate sites, which is shown in Figure 9.

<!-- b000316 | caption | pages [12] -->
Figure 9: Candidate sites

<!-- b000317 | furniture | pages [13] -->
Team # 65448

<!-- b000318 | furniture | pages [13] -->
Page 10 of 25

<!-- b000319 | heading | pages [13] -->
5.2.3 Grey Relation Grade Analysis

<!-- b000320 | prose | pages [13] -->
Because of the complex interaction between these parameters, we ﬁnally choose Grey Relation Grade Analysis to conﬁrm the selection system.

<!-- b000321 | prose | pages [13] -->
Firstly, index weight should be obtained. The concrete steps are:

<!-- b000322 | prose | pages [13] -->
Step 1: Determine the reference data series as an ideal comparison standard. In our system, the largest value of each metric (river width is taken minus) constitutes the reference sequence.

<!-- b000323 | prose | pages [13] -->
X0 = (x0(1), x0(2), · · · , x0(m)) (19)

<!-- b000324 | prose | pages [13] -->
Step 2: Calculate the absolute difference value of each parameter sequence and the reference se- quence of the corresponding elements,as ∆i(j) = |xi(j) −x0(j)|. In the formula, i represents the number of candidate sites; j is the number of metrics; x0(j) means the reference data in the metric.

<!-- b000325 | prose | pages [13] -->
1⩽i⩽m{∆i(j)} and b = max 1⩽i⩽m{∆i(j)}. Step 3: Conﬁrm a = min 1⩽i⩽n min 1⩽i⩽n max Step 4: Calculate the correlation coefﬁcient as:

<!-- b000326 | prose | pages [13] -->
a + bλ fi(j) = (20) ∆i(j) + bλ

<!-- b000327 | prose | pages [13] -->
where resolution coefﬁcient λ ∈(0, 1), commonly using 0.5. Step 5: Calculate the correlation degree.

<!-- b000328 | prose | pages [13] -->
n rj = 1 X fi(j) (21) n i=1

<!-- b000329 | prose | pages [13] -->
Step 6: Calculate the weight of each measure standard.

<!-- b000330 | prose | pages [13] -->
rj r′ j = (22) r1 + r2 + · · · + rm

<!-- b000331 | prose | pages [13] -->
Step 7: Build the evaluation model.

<!-- b000332 | prose | pages [13] -->
Zi = r′ 1xi(1) + r′ 2xi(2) + · · · + r′ mxi(m) (23)

<!-- b000333 | prose | pages [13] -->
Based on the data we got above, we can solve the model and obtain the following results (Figure 10).

<!-- b000334 | caption | pages [13] -->
Figure 10: Results of Grey Relation Grade Analysis

<!-- b000335 | prose | pages [13] -->
As shown in Figure 11-12, the following 11 sites are selected to constructed dams, considering the costs and the distances clustering between adjacent dams.

<!-- b000336 | furniture | pages [14] -->
Team # 65448

<!-- b000337 | furniture | pages [14] -->
Page 11 of 25

<!-- b000338 | caption | pages [14] -->
Figure 11: Dam sites in terrain map

<!-- b000339 | caption | pages [14] -->
Figure 12: Dam sites in altitude map

<!-- b000340 | heading | pages [14] -->
5.3 Difference Model of the Dam System

<!-- b000341 | prose | pages [14] -->
When the dam system is considered in the Zambezi River, the Hydrodynamic Model with partial differential equations is too complex to describe the inﬂuences of the dam system, making it impos- sible to obtain the changes of the river in a bearable time. Therefore, the simpliﬁcation of the model should be introduced, which is difference model of the dam system, providing recurrence formulas to calculate the runoff of the river with dam system.

<!-- b000342 | prose | pages [14] -->
The dams are numbered from 1 to 11, and the time is seperated into j time periods of T. For the ith dam in the jth time period,

<!-- b000343 | prose | pages [14] -->
• Q(i+1)j is the river ﬂux ﬂowing out of the dam. Specially, Q1j represents the ﬂux at the head- stream;

<!-- b000344 | prose | pages [14] -->
• Q′ ij is the river ﬂux ﬂowing into the dam;

<!-- b000345 | furniture | pages [15] -->
Team # 65448

<!-- b000346 | furniture | pages [15] -->
Page 12 of 25

<!-- b000347 | prose | pages [15] -->
• qij is the rainfall ﬂux density in the dam region and the region between the dam and previous one;

<!-- b000348 | prose | pages [15] -->
• δij is the evaporation ﬂux density in the dam region and the region between the dam and previous one;

<!-- b000349 | prose | pages [15] -->
• ∆yi is the altitude changes between the dam and previous one;

<!-- b000350 | prose | pages [15] -->
• li is the distance between the dam and the previous one;

<!-- b000351 | prose | pages [15] -->
• hij is the river depth in the region between the dam and the previous one;

<!-- b000352 | prose | pages [15] -->
• Hij is the water depth of the reservior attached to the dam;

<!-- b000353 | prose | pages [15] -->
• Si is the area of the reservior attached to the dam;

<!-- b000354 | prose | pages [15] -->
• H0i is the dead water level of the reservior attached to the dam (dead water level is the mini- mum water level which the reservoir is allowed to drawdown).

<!-- b000355 | caption | pages [15] -->
Figure 13: Diagram describing the situation of the river with dam system

<!-- b000356 | heading | pages [15] -->
5.3.1 Equations in the River (Without the Dam)

<!-- b000357 | prose | pages [15] -->
As is written in the Hydrodynamic Model, the continuity equation (based on the ﬂow conserva- tion) can be written as ij = liL∆hi (qij −δij)liL + Qij −Q′ (24) ∆t hi(j+1)−hij In the time period of T, ∆hi ∆t = . T Neglecting the variation of v in time period of T, the energy conservation equation is given by

<!-- b000358 | prose | pages [15] -->
ρLhijvTg∆yi −ρkhijLvTli = 1 2ρ(qij −δij)LliTv2 + 1 2ρLhijvT∆(v2) (25)

<!-- b000359 | prose | pages [15] -->
where v and ∆(v2) can be expressed by Qij and Q′ ij.

<!-- b000360 | prose | pages [15] -->
Qij + Q′ ij v = (26) 2hijL

<!-- b000361 | prose | pages [15] -->
2 −Q2 Q′ ij ij ∆(v2) = (27) h2 ijL2

<!-- b000362 | prose | pages [15] -->
After simpliﬁcation, the equations in the river without the dam are

<!-- b000363 | prose | pages [15] -->
 hi(j+1)−hij (qij −δij)liL + Qij −Q′ ij = liL  T    (28)  2 −Q2  ij + 1 ijL2li = Q′ 2(qij −δij)L(Qij + Q′ 2h2 ijL2g∆yi −2kh2  ij)li  ij

<!-- b000364 | furniture | pages [16] -->
Team # 65448

<!-- b000365 | furniture | pages [16] -->
Page 13 of 25

<!-- b000366 | heading | pages [16] -->
5.3.2 Equations in the Dam Region

<!-- b000367 | prose | pages [16] -->
As is written in the Hydrodynamic Model, the continuity equation (based on the ﬂow conserva- tion) can be written as ∆Hi (qij −δij)Si + Q′ ij −Q(i+1)j = Si (29) ∆t Hi(j+1)−Hij In the time period of T, ∆Hi ∆t = . T According to Hydraulics textbook, Q(i+1)j has the following relation with Hij:6 3 Q(i+1)j = Ai(Hij −H0i) (30) 2

<!-- b000368 | prose | pages [16] -->
where the Ai is the outﬂow coefﬁcient determined by the width bi of the gate hole and the relative gate opening θ of the dam. According to the emprical formula, Ai can be given by Ai = 2.7674θbi (31)

<!-- b000369 | heading | pages [16] -->
5.3.3 Recurrence Formulas

<!-- b000370 | prose | pages [16] -->
Concluding the equations above, the recurrence formulas of the river with dam systems can be obtained.

<!-- b000371 | prose | pages [16] -->
q −1 1 i −4( 1  4 g2L2l2 2 gLQijli−Q2 ij+2kh2 ijL2li−2h2 ijL2g∆yi) 2 gLli+ Q′ ij =   2          3  Q(i+1)j = Ai(Hij −H0i)  2     (32)  (qij−δij)liL+Qij−Q′   ij hi(j+1) = T + hij   liL         3  (qij−δij)Si+Q′ ij−Ai(Hij−H0i)  2  Hi(j+1) = T + Hij  Si In this way, when the known parameters are conﬁrmed, the river with dam system can be de- picted with Qij, Q′ ij, hij, Hij. All the known parameters are listed below.

<!-- b000372 | prose | pages [16] -->
• Q1j: the river ﬂux at the headstream;

<!-- b000373 | prose | pages [16] -->
• Q(i+1)0: the initial river ﬂux ﬂowing out of the dam;

<!-- b000374 | prose | pages [16] -->
• hi0: the initial river depth in the region between the dam and the previous one;

<!-- b000375 | prose | pages [16] -->
• Hi0: the initial water depth of the reservior attached to the dam;

<!-- b000376 | prose | pages [16] -->
• qij: the rainfall along the river;

<!-- b000377 | prose | pages [16] -->
• δij: the evaporation along the river;

<!-- b000378 | prose | pages [16] -->
• ∆yi is the altitude changes between the dam and previous one;

<!-- b000379 | prose | pages [16] -->
• li is the distance between the dam and the previous one;

<!-- b000380 | prose | pages [16] -->
• Si: the area of the reservior attached to the dam;

<!-- b000381 | prose | pages [16] -->
• Ai: the outﬂow coefﬁcient of the dam;

<!-- b000382 | prose | pages [16] -->
• H0i: the dead water level of the reservior attached to the dam;

<!-- b000383 | prose | pages [16] -->
• L: the width of the river;

<!-- b000384 | prose | pages [16] -->
• g: the acceleration of gravity;

<!-- b000385 | prose | pages [16] -->
• k: the on-way resistance coefﬁcient;

<!-- b000386 | prose | pages [16] -->
• T: the time scale.

<!-- b000387 | furniture | pages [17] -->
Team # 65448

<!-- b000388 | furniture | pages [17] -->
Page 14 of 25

<!-- b000389 | heading | pages [17] -->
5.4 Dam Construction & Manipulating System

<!-- b000390 | prose | pages [17] -->
As the number and placement of the new dams have been conﬁrmed, the size of dams and manip- ulating strategy should be assigned so that the dam systems can have good performance and handle emergency water ﬂow situations. The concrete steps to design the size of dams and manipulating strategy are listed below:

<!-- b000391 | prose | pages [17] -->
Step 1: Conﬁrm the parameters of different dam types. Step 2: Conﬁrm the type selection of each dam. Step 3: Evaluate the protection and water management options for Lake Kariba. Step 4: Strategies to handle emergency water ﬂow situations.

<!-- b000392 | heading | pages [17] -->
5.4.1 Conﬁrm the Parameters of Different Dam Types

<!-- b000393 | prose | pages [17] -->
According to the standard of Water Conservancy Engineering, the dams can be categoried into several types according to the capacity of the reservior attached.7 As shown in Table 2, four ap- propriate types of dam are selected considering the reality of the Zambezi River and the relevant parameters have been conﬁrmed.

<!-- b000394 | prose | pages [17] -->
The area of Reservior/m2 A Warning water levelHmi/m Types of dam

<!-- b000395 | prose | pages [17] -->
1 × 108 33θ I 60

<!-- b000396 | prose | pages [17] -->
1 × 107 27θ II 50

<!-- b000397 | prose | pages [17] -->
1 × 106 16θ III 40

<!-- b000398 | prose | pages [17] -->
1 × 105 11θ IV 30

<!-- b000399 | caption | pages [17] -->
Table 2: Parameters of different dam types

<!-- b000400 | prose | pages [17] -->
Where θ is the relative gate opening of the dam. In order to simplify the manipulation of the dam, it is assumed that there are three gears of the gate opening, which means θ can be taken as 0.25, 0.5, 1.0. In normal situation, θ is taken as 0.5.

<!-- b000401 | caption | pages [17] -->
Figure 14: Diagram of the dam

<!-- b000402 | heading | pages [17] -->
5.4.2 Conﬁrm the Type Selection of Each Dam

<!-- b000403 | prose | pages [17, 18] -->
The new dams should be established to protect the river’s basin from the ﬂoods and drought, so it seems that the dam with largest reservior is the best choice. However, the cost of one large dam is equal to that of many small dams. Therefore, we should take a reasonable balance between safety and costs, which can be completed with the Difference Model of the Dam System. When each dam size has been conﬁrmed, Hij, hij, Qij, Q′ ij can be determined, which means a certain series of dam size will correspond to a certain river situation.

<!-- b000404 | furniture | pages [18] -->
Team # 65448

<!-- b000405 | furniture | pages [18] -->
Page 15 of 25

<!-- b000407 | prose | pages [18] -->
However, the main tributaries are neglected in the Difference Model of the Dam System, which play an important role in the river system. Therefore, we correct the model by detecting the main tributaries and adding them into the model. According to the terrain map of the basin, which is shown in Figure 15, the main tributaries distribute at the region between the dam A and B, B and C, F and G, H and I, J and K. Their runoff are marked as q′ 2j, q′ 3j, q′ 7j, q′ 9j, q′ 11j. The runoff will be added into the ﬂux ﬂowing into the relevant dam. For example, the ﬂux ﬂowing into the 2nd dam will be Q′ 2j + q′ 2j.

<!-- b000408 | caption | pages [18] -->
Figure 15: Tributaries

<!-- b000409 | prose | pages [18] -->
In addition to this, the loss of mechanical energy when the ﬂow collides with the banks and bottom of the river, so a loss coefﬁcient β should be included in the energy conservation equation, which is

<!-- b000410 | prose | pages [18] -->
q −1 1 i −4(1 4g2L2l2 2gLQijli −Q2 ij + 2kh2 ijL2li −2h2 ijL2gβ∆yi) 2gLli + Q′ ij = (33) 2 Before calculating the best type selection with the Difference Model of the Dam System, all the known parameters should be conﬁrmed. It is assumed that the rainfall and evaporation in a certain region is constant in the time period we have concerned, which means qij = qi, δij = δi. The dead water level of each dam is supposed to be constant, which means H0j = H0. Apparently, the rainfall will inﬂuence the runoff at the headstream and tributaries, so it is reasonable to suppose that

<!-- b000411 | prose | pages [18] -->
 Q1j = Q1 + α(q1 −δ1)      q′ 2j = q′ 2 + α(q2 −δ2)       q′ 3j = q′ 3 + α(q3 −δ3)   (34) q′ 7j = q′ 7 + α(q7 −δ7)      q′ 9j = q′  9 + α(q9 −δ9)      q′ 11j = q′  11 + α(q11 −δ11) 

<!-- b000412 | prose | pages [18] -->
where Q1, q′ 2, q′ 3, q′ 7, q′ 9, q′ 11 are separately the runoff at the headstream and each tributary, α is the constant coefﬁcient.

<!-- b000413 | prose | pages [18] -->
∆yi and li can be easily determined by the geographical data mentioned above, which is included in the Appendix. Q1, hi0, Hi0, qi and δi can be decided by the above hydrologcial data,3 where it is assumed that hi0 = h0, Hi0 = H0, δi = δ0, qi is supposed to obey the distribution concluded from the rainfall data.Li is presented in the appendices. Other known parameters are listed below:

<!-- b000414 | furniture | pages [19] -->
Team # 65448

<!-- b000415 | furniture | pages [19] -->
Page 16 of 25

<!-- b000416 | prose | pages [19] -->
• Q1 = 500m3/s, h0 = 20m, H0 = 20m, T = 60s

<!-- b000417 | prose | pages [19] -->
• q′ 2 = 150m3/s, q′ 3 = 100m3/s, q′ 7 = 50m3/s, q′ 9 = 120m3/s, q′ 11 = 80m3/s

<!-- b000418 | prose | pages [19] -->
• g = 9.8m/s2, k = 1 × 10−6kg · m3 · s−1, α = 3 × 109, β = 10−3

<!-- b000419 | prose | pages [19] -->
With all the known parameters conﬁrmed, we can calculate the best type selection with the cor- rected Difference Model of the Dam System. It is obvious that the smallest dam is cheapest, so we choose IV type for each dam at ﬁrst except the 11th one and the 7th one. At the site of the 11th dam, the Cahora Bassa Dam8 has been constructed, which is a I-type dam, so the 11 th dam is selected as I type. The 7th dam is located at the previous Kariba Dam, but the new geological condition after errosion is not suitable for a I-type dam, so II type is selected considering the huge capacity of Lake Kariba. Then we calculate the situation of the river (with 90000 iterations, which means 3 months for the model). According to the calculation, the situation of the river will approach a stable state with time goes. If Hij at the stable state is higher than the warning water level at one dam, the dam type will be upgraded for one grade. The procedure will be repeated until all Hij at the stable state are lower than the corresponding warning water level. However, another restriction should be satisﬁed by the ﬁnal type selection:

<!-- b000420 | prose | pages [19] -->
• P11 i=1 SiHmi ⩾VLake, which means the total capacity of the reserviors attached to new dams should be larger than the capacity of previous Lake Kariba (VLake). The total capacity represents the overall water management capabilities of the dam system. The restriction means the new dam system has the same and even higher overall water management capabilities than the Kariba Dam.

<!-- b000421 | prose | pages [19] -->
The detailed procedure is shown in the Figure 16.

<!-- b000422 | caption | pages [19] -->
Figure 16: Diagram of the Type Selection of Each Dam

<!-- b000423 | prose | pages [19] -->
The selection result is presented in Table 3.

<!-- b000424 | furniture | pages [20] -->
Team # 65448

<!-- b000425 | furniture | pages [20] -->
Page 17 of 25

<!-- b000426 | prose | pages [20] -->
Dam A B C D E F G H I J K

<!-- b000427 | prose | pages [20] -->
Types of Dam III III III III III III III IV I IV III

<!-- b000428 | caption | pages [20] -->
Table 3: Types of each dam

<!-- b000429 | heading | pages [20] -->
5.4.3 Evaluate the Protection & Water Management Options for Lake Kariba

<!-- b000430 | prose | pages [20] -->
The protection for Lake Kariba can be evaluated with the water level ﬂuctuation of Lake Kariba between rainy season and dry season. The smaller the ﬂuctuation is, the better protection is offered for the lake. The water level in rainy season and dry season can be easily calculated with the corrected Difference Model of the Dam System. hi0 and Hi0 are set as the stable value with normal rainfall and qi has been determined by the corresponding rainfall data of rainy season and dry season. The calculation result is taken as the ﬁnal result after 90000 iterations, because it is observed that for large reservoirs like Kariba, the instantaneous and daily peak ﬂows are not important, as these can be stored in the reservoir.

<!-- b000431 | prose | pages [20] -->
As shown in Fig , we can ﬁnd that the ﬂuctuation decreases with the new dam system, proving that the new dam system provides the better production for Lake Kariba.

<!-- b000432 | prose | pages [20] -->
In addition to this, the discharge of the dam is provided with 3 gears, so that elaborate water management can be realized with the new dam system. Therefore, the new dam system has more water management options.

<!-- b000433 | heading | pages [20] -->
5.4.4 Strategies to Handle Emergency Water Flow Situations

<!-- b000434 | prose | pages [20] -->
The emergency water ﬂow situations include the ﬂooding and drought, which are both common in the Zambezi River’s basin, so different strategies should be designed to handle the two emergency water ﬂow situations.

<!-- b000435 | prose | pages [20] -->
Flooding The ﬂooding caused by extreme large rainfall is assumed to occur at the region between the 2nd dam and the 4th one for three months, which is typical for the river’s basin according to the data provided by World Bank.3 qi in the ﬂooding region is set as the rainfall of approximately 24mm per twelve hours, which can be categoried as heavy rain. The runoff distribution without modulating along the river is shown in Figure 17. The exhaustive method is utilized to test all combinations of Ai (which means the changes of the dam gear) for the combination which obtains the minimum variance of all Hi −Hi0. The minimum variance of all Hi −Hi0 means that the reserviors attached to dams have minimum ﬂuctuation during the ﬂooding, which will protect the residents from danger and economic loss. The concrete procedure is shown in Figure 18.

<!-- b000436 | caption | pages [20] -->
Figure 17: Runoff distribution without regulating

<!-- b000437 | furniture | pages [21] -->
Team # 65448

<!-- b000438 | furniture | pages [21] -->
Page 18 of 25

<!-- b000439 | caption | pages [21] -->
Figure 18: Diagram of the strategy selection for ﬂooding

<!-- b000440 | prose | pages [21] -->
The best combination of the dam gears is presented in Table 4.

<!-- b000441 | prose | pages [21] -->
Dam 1 2 3 4 5 6 7 8 9 10 11

<!-- b000442 | prose | pages [21] -->
A 4 8 16 16 16 16 16.5 5.5 16.5 8 8

<!-- b000443 | caption | pages [21] -->
Table 4: Best combination of Ai

<!-- b000444 | prose | pages [21] -->
The regulated reservior depth is shown in the Figure 19, compared with the unregulated reservior depth.

<!-- b000445 | caption | pages [21] -->
Figure 19: Regulated reservior depth comparing with the unregulated reservior depth

<!-- b000446 | prose | pages [21] -->
Drought The drought caused by extreme small rainfall is assumed to occur along the whole river for three months. δi in the drought region is set as the rainfall of approximately 1100mm per year, which can be categoried as heavy rain. The runoff distribution without modulating along the river is shown in

<!-- b000447 | caption | pages [21] -->
Figure 20. The exhaustive method is utilized to test all combinations of Ai (which means the changes

<!-- b000448 | prose | pages [21] -->
of the dam gear) for the combination which obtains the maximum increased runoff. The increased runoff is more signicant in drought, which will protect the residents from danger and economic loss. The concrete procedure is shown in Figure 21.

<!-- b000449 | furniture | pages [22] -->
Team # 65448

<!-- b000450 | furniture | pages [22] -->
Page 19 of 25

<!-- b000451 | caption | pages [22] -->
Figure 20: Runoff distribution without regulating

<!-- b000452 | caption | pages [22] -->
Figure 21: Diagram of the strategy selection for drought

<!-- b000453 | prose | pages [22] -->
The best combination of the dam gears is that each dam is set as the maximum Ai. The regulated runoff is shown in the Figure 22, compared with the unregulated runoff.

<!-- b000454 | caption | pages [22] -->
Figure 22: Regulated reservior depth comparing with the unregulated reservior depth

<!-- b000455 | heading | pages [22] -->
6 Testing the model

<!-- b000456 | heading | pages [22] -->
6.1 Error analysis

<!-- b000457 | prose | pages [22] -->
In this part, we will analyze relevant factors that might cause error in our model.

<!-- b000458 | furniture | pages [23] -->
Team # 65448

<!-- b000459 | furniture | pages [23] -->
Page 20 of 25

<!-- b000460 | prose | pages [23] -->
• The mechanical energy loss of water: In fact, the mechanical energy loss water in each segment is very complex, which is relevant to the topographic feature in the segment. However, we have neglected the complexity.

<!-- b000461 | prose | pages [23] -->
• ResistenceïijŽIn fact, the on-way resistance coefﬁcient k in each segment is closely related with the curve of the channel in the segment, which is neglected by us.

<!-- b000462 | prose | pages [23] -->
• Evaporation along the river and the runoff of tributaries and headstream: Accurate data is not available so that we roughly estimate it.

<!-- b000463 | heading | pages [23] -->
6.2 Sensitivity Analysis

<!-- b000464 | prose | pages [23] -->
In our model, some inputs are not precise enough for the lack of actual data about Zambezi basin and some parameters are difﬁcult to obtain directly. Those inputs or parameters may inﬂuence the result of our calculation, so we implement a sensitive analysis to test the robustness of our model.

<!-- b000465 | prose | pages [23] -->
In fact, we cannot obtain the real value of the inputs Q1, Hi0, hi0 and parameter α with the data we have. Sensitivity Analysis is primarily conducted on these inputs and parameters.

<!-- b000466 | heading | pages [23] -->
6.2.1 Sensitivity Analysis for Hi

<!-- b000467 | prose | pages [23] -->
-5% -3% -1% 0% 1% 3% 5%

<!-- b000468 | prose | pages [23] -->
hi0 2.9281% 2.9767% 3.0253% 0% 3.0738% 3.1223% 3.1706%

<!-- b000469 | prose | pages [23] -->
Hi0 7.5529% 3.7451% 1.8459% 0% 4.2614% 7.6778% 11.4852%

<!-- b000470 | prose | pages [23] -->
Q00 3.0475% 3.0483% 3.0492% 0% 3.0500% 3.0508% 3.0517%

<!-- b000471 | prose | pages [23] -->
α 2.9252% 2.9749% 3.0247% 0% 3.0745% 3.1242% 3.1739%

<!-- b000472 | caption | pages [23] -->
Table 5: Sensitivity Analysis for Hi

<!-- b000473 | prose | pages [23] -->
All the percentage presented on the table represents the maximum ﬂuctuation among Hi. There- fore, Hi is not sensitive to the value of Q1, Hi0, hi0 and α.

<!-- b000474 | heading | pages [23] -->
6.2.2 Sensitivity Analysis for hi

<!-- b000475 | prose | pages [23] -->
-5% -3% -1% 0% 1% 3% 5%

<!-- b000476 | prose | pages [23] -->
hi0 5.0000% 3.0000% 1.0000% 0% 1.0000% 3.0000% 5.0000%

<!-- b000477 | prose | pages [23] -->
Hi0 0.2140% 0.1309% 0.0445% 0% 0.0453% 0.1382% 0.2341%

<!-- b000478 | prose | pages [23] -->
Q00 0.0432% 0.0259% 0.0086% 0% 0.0086% 0.0259% 0.0432%

<!-- b000479 | prose | pages [23] -->
α 0.0169% 0.0102% 0.0034% 0% 0.0034% 0.0102% 0.0170%

<!-- b000480 | caption | pages [23] -->
Table 6: Sensitivity Analysis for hi

<!-- b000481 | prose | pages [23] -->
All the percentage presented on the table represents the maximum ﬂuctuation among hi. There- fore, hi is not sensitive to the value of Q1, Hi0, hi0 and α.

<!-- b000482 | furniture | pages [24] -->
Team # 65448

<!-- b000483 | furniture | pages [24] -->
Page 21 of 25

<!-- b000484 | heading | pages [24] -->
6.2.3 Sensitivity Analysis for Qi

<!-- b000485 | prose | pages [24] -->
-5% -3% -1% 0% 1% 3% 5%

<!-- b000486 | prose | pages [24] -->
hi0 0.5677% 0.4539% 0.3403% 0% 0.2267% 0.1133% 0.0000%

<!-- b000487 | prose | pages [24] -->
Hi0 26.3961% 16.2663% 5.7108% 0% 5.2538% 16.6129% 28.3529%

<!-- b000488 | prose | pages [24] -->
Q00 5.0000% 3.0000% 1.0000% 0% 1.0000% 3.0000% 5.0000%

<!-- b000489 | prose | pages [24] -->
α 5.5439% 3.3332% 1.1134% 0% 1.1156% 3.3538% 5.6011%

<!-- b000490 | caption | pages [24] -->
Table 7: Sensitivity Analysis for Qi

<!-- b000491 | prose | pages [24] -->
All the percentage presented on the table represents the maximum ﬂuctuation among Qi. It can be seen that Qi is sensitive to Hi0, namely the faint error of the initial depth of the reservior attached to the dam may lead to the great changes of Qi, so the initial value of Hi0 should be taken as the stable value calculated in normal condition to control the potential error of Qi

<!-- b000492 | heading | pages [24] -->
6.3 Conclusion

<!-- b000493 | heading | pages [24] -->
6.3.1 Strengths and weaknesses

<!-- b000494 | heading | pages [24] -->
Strengths:

<!-- b000495 | prose | pages [24] -->
• We have got the sufﬁcient topographic data of the river and build hydrodynamic model model to calculate the velocity and depth distribution of the river. So we have a detailed and compre- hensive description of the Zambezi River.

<!-- b000496 | prose | pages [24] -->
• We consult many professional literatures to determine the evaluation indexes of site selection of dams. And we use grey relation analysis and k-means clustering combined with these multiple indexes to pick out optimal sites from candidates. So our selection is reasonable.

<!-- b000497 | prose | pages [24] -->
• We use difference model to simplify the calculation of the river and considered the inﬂuence both tributaries and evaporation. As long as we have enough data to set precise inputs we can predict the dynamical process of the river. It is of great importance and convenience for us to do further discussion about dams.

<!-- b000498 | prose | pages [24] -->
• After consulting relevant literature, we have relative knowledge of dams including types, rel- evant parameters, function and building cost in practical situation. Based on this we set four types of dams to be selected for each site and ﬁnally conﬁrm them by balancing safety and costs. Through this our dam system owns more water management options.

<!-- b000499 | heading | pages [24] -->
Weaknesses:

<!-- b000500 | prose | pages [24] -->
• On the one hand, insufﬁcient data of the runoff of Zambezi River’s tributaries and headstream and the evaporation of its basin trigger the indeterminacy of the inputs of our equation. On the other hand, some parameters in our equation like the coefﬁcient of on-way resistance is hard to get directly. So actually the solution of our equation may be not fully consistent with actual data numerically.

<!-- b000501 | prose | pages [24] -->
• We do not have enough consideration of geological conditions of Zambezi basin when con- ﬁrming the sites of dams and the analysis for social and ecological impact of the project is also insufﬁcient.

<!-- b000502 | furniture | pages [25] -->
Team # 65448

<!-- b000503 | furniture | pages [25] -->
Page 22 of 25

<!-- b000504 | heading | pages [25] -->
6.3.2 Future Work

<!-- b000505 | prose | pages [25] -->
Since we still have some weaknesses in our current work, future efforts are needed to better work out this problem.

<!-- b000506 | prose | pages [25] -->
Firstly, more sufﬁcient data of runoff of Zambezi Riverâ ˘A ´Zs tributaries and headstream and the evaporation of its basin will be needed in order to do more accurate calculation of the river.

<!-- b000507 | prose | pages [25] -->
Secondly, more geological knowledge will be needed and more civilian and ecological factors will be considered in order to make more scientiﬁc and reasonable site selection of dams.

<!-- b000508 | prose | pages [25] -->
Thirdly, more rainfall and evaporation data of Zambezi basin are needed to better predict the extreme conditions and provide more detailed and comprehensive guidance for the new dam system.

<!-- b000509 | prose | pages [25] -->
Finally, we will try to generalize our model and approach in this problem to more multi-dam systems after more polishment.

<!-- b000510 | heading | pages [25] -->
References

<!-- b000511 | references | pages [25] -->
[1] World Bank: International Development Association Project Appraisal Document on A Pro-

<!-- b000512 | references | pages [25] -->
posed Credit in the Amount of SDR 5.6 Million and A Proposed Swedish Grant in the Amount

<!-- b000513 | references | pages [25] -->
of US$25 Million to the Republic of Zambia for A Kariba Dam Rehabilitation Project, 2014.11.

<!-- b000514 | references | pages [25] -->
[2] World Bank: Kariba Dam, Zambia and Zimbabwe, 2000.11.

<!-- b000515 | references | pages [25] -->
[3] World Bank: The Zambezi River Basin: A Multi-Sector Investment Opportunities Analysis

<!-- b000516 | references | pages [25] -->
[4] Zhang YaGuan, Xue ShiMing, Kuang ChongYi, Chen Gong: Relation grade analysis of grey

<!-- b000517 | references | pages [25] -->
theory and comprehensive evaluation of introduced forage of winter-free farmland in the north

<!-- b000518 | references | pages [25] -->
of Yunnan subtropics. ISSN 1004-5759

<!-- b000519 | references | pages [25] -->
[5] Wang Liwen: The function and site selection of reservior dams

<!-- b000520 | references | pages [25] -->
[6] Zhou Zhihao: Water Resources and Hydropower Planning, China High Education Press.

<!-- b000521 | references | pages [25] -->
[7] E.M. Welson: Engineering Hydrology, Palgrave Macmillan, 1990.

<!-- b000522 | references | pages [25] -->
[8] Wikipedia: Cahora Bassa Dam.

<!-- b000523 | furniture | pages [26] -->
Team # 65448

<!-- b000524 | furniture | pages [26] -->
Page 23 of 25

<!-- b000525 | heading | pages [26] -->
Appendices

<!-- b000526 | prose | pages [26] -->
District Oct Nov Dec Jan Feb Mar Apr May Jun Jul Aug Sep Year

<!-- b000527 | prose | pages [26] -->
1 20 71 164 243 180 173 71 45 37 28 27 15 1074

<!-- b000528 | prose | pages [26] -->
2 12 78 174 197 180 108 26 7 5 3 3 3 796

<!-- b000529 | prose | pages [26] -->
4 17 84 172 179 159 90 18 3 1 0 0 1 724

<!-- b000530 | prose | pages [26] -->
6 18 68 156 164 139 76 24 5 1 0 0 2 653

<!-- b000531 | prose | pages [26] -->
9 26 90 191 195 187 113 28 2 1 0 0 2 835

<!-- b000532 | prose | pages [26] -->
13 46 178 259 254 216 195 50 3 1 0 1 6 1209

<!-- b000533 | caption | pages [26] -->
Table 8: Rainfalls along the River

<!-- b000534 | caption | pages [26] -->
Figure 23: Distrcts in Table 8

<!-- b000535 | prose | pages [26] -->
District 1 2 4 6 9 13

<!-- b000536 | prose | pages [26, 27, 28] -->
Mean Distance From the Headstream 417 786 557 1029 1888 2261 Potential Distance from Lat/Long Locations the Headstream 13◦8′S 23◦2′E 1 120 13◦9′S 23◦3′E 2 150 16◦1′S 23◦6′E 3 420 17◦0′S 25◦9′E 4 738 17◦8′S 26◦1′E 5 806 17◦8′S 26◦5′E 6 818 17◦7′S 26◦6′E 7 820 17◦5′S 26◦7′E 8 825 17◦4′S 26◦9′E 9 828 17◦6′S 26◦5′E 10 860 18◦0′S 26◦4′E 11 880 18◦2′S 26◦6′E 12 882 18◦3′S 26◦6′E 13 885 18◦3′S 26◦6′E 14 886 17◦6′S 27◦2′E 15 940 17◦3′S 27◦5′E 16 946 16◦7′S 28◦9′E 17 1208 16◦8′S 28◦1′E 18 1215 16◦1′S 28◦0′E 19 1217 15◦8′S 30◦6′E 20 1408 15◦8′S 30◦3′E 21 1420 15◦4′S 32◦9′E 22 1683 15◦5′S 32◦5′E 23 1695 15◦0′S 33◦3′E 24 1715 15◦2′S 33◦5′E 25 1720 16◦2′S 34◦4′E 26 1885 Locations Terrain gap River Flow Acceleration Rainfall Depth Valley Lake Pocket-like lowlands Width of river

<!-- b000537 | caption | pages [26] -->
Table 9: Locations of Distance in 8

<!-- b000538 | furniture | pages [27] -->
Team # 65448

<!-- b000539 | furniture | pages [27] -->
Page 24 of 25

<!-- b000541 | caption | pages [27] -->
Table 10: Potiential locations for New Dam system

<!-- b000542 | furniture | pages [28] -->
Team # 65448

<!-- b000543 | furniture | pages [28] -->
Page 25 of 25

<!-- b000545 | prose | pages [28] -->
1 -0.758387 0.068707535 0.494863 27.9938 0 0 0 0.228625733

<!-- b000546 | prose | pages [28] -->
2 -0.188707 0.008492897 0.482928 28.1081 0 0 0 0.269829219

<!-- b000547 | prose | pages [28] -->
3 -0.131455 0.005840917 0.390808 36.9643 0 0 0 0.255940496

<!-- b000548 | prose | pages [28] -->
4 -0.371262 0.020843327 0.317614 34.1216 0 0 0 0.89091976

<!-- b000549 | prose | pages [28] -->
5 -5.36119 0.2854 0.306918 27.3157 1 0 0 0.105767626

<!-- b000550 | prose | pages [28] -->
6 -6.34961 0.310580549 0.305212 25.2888 1 0 0 0.231204181

<!-- b000551 | prose | pages [28] -->
7 -7.41301 0.353306423 0.304933 24.5147 1 0 0 0.153765839

<!-- b000552 | prose | pages [28] -->
8 -11.478 0.446515611 0.304242 22.6366 1 0 0 0.089243799

<!-- b000553 | prose | pages [28] -->
9 -9.88432 0.4206 0.303832 21.0487 1 0 1 0.247277304

<!-- b000554 | prose | pages [28] -->
10 0.47558 0.028870209 0.299668 21.4808 1 0 0 0.108070299

<!-- b000555 | prose | pages [28] -->
11 -7.05964 0.251578098 0.297263 19.8484 1 0 0 0.160722158

<!-- b000556 | prose | pages [28] -->
12 -6.57593 0.2306 0.29703 19.5294 0 0 1 0.207333801

<!-- b000557 | prose | pages [28] -->
13 -11.3948 0.400920723 0.296685 18.8262 0 0 1 0.209334368

<!-- b000558 | prose | pages [28] -->
14 -5.43244 0.178947925 0.294446 18.6609 0 0 1 0.137633864

<!-- b000559 | prose | pages [28] -->
15 -0.47327 0.00114481 0.290952 18.5564 0 0 1 0.359885441

<!-- b000560 | prose | pages [28] -->
16 -3.90212 0.1113 0.290395 18.4459 0 1 0 2.133441296

<!-- b000561 | prose | pages [28] -->
17 -2.5892 0.075096648 0.279359 20.4907 0 1 1 0.425886964

<!-- b000562 | prose | pages [28] -->
18 -3.36631 0.099757025 0.279419 20.1174 0 0 0 0.553183045

<!-- b000563 | prose | pages [28] -->
19 -3.4093 0.1 0.27944 20.0102 0 0 0 0.392962291

<!-- b000564 | prose | pages [28] -->
20 -1.23203 0.03221616 0.288379 22.0094 0 0 1 0.193799965

<!-- b000565 | prose | pages [28] -->
21 -3.68041 0.108738542 0.2894 21.7235 0 0 0 0.502505624

<!-- b000566 | prose | pages [28] -->
22 -1.40594 0.038844327 0.325444 25.1723 1 1 1 0.140411027

<!-- b000567 | prose | pages [28] -->
23 -3.64917 0.1039 0.327711 24.7095 1 0 0 0.178182111

<!-- b000568 | prose | pages [28] -->
24 -3.88742 0.108105599 0.331611 23.4029 0 0 1 0.126866802

<!-- b000569 | prose | pages [28] -->
25 -4.08962 0.1137 0.33261 23.0711 0 0 0 0.106678572

<!-- b000570 | prose | pages [28] -->
26 -1.69058 0.032759026 0.370861 23.4115 0 0 1 0.715017666

<!-- b000571 | caption | pages [28] -->
Table 11: Metric for determine the Dams’ Locations

<!-- b000572 | prose | pages [28] -->
Distance from Lat/Long Locations the Headstream 13◦8′S 23◦2′E A 120 16◦1′S 23◦6′E B 420 17◦0′S 25◦9′E C 738 17◦8′S 26◦1′E D 806 17◦5′S 26◦7′E E 825 18◦3′S 26◦6′E F 885 16◦7′S 28◦9′E G 1208 15◦8′S 30◦6′E H 1408 15◦4′S 32◦9′E I 1683 15◦0′S 33◦3′E J 1715 16◦2′S 34◦4′E K 1885

<!-- b000573 | caption | pages [28] -->
Table 12: Locations of Dams in the New Dam System
