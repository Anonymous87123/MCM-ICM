# P-A-2017-55280-55cec2b6

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For ofﬁce use only

<!-- b000003 | prose | pages [1] -->
For ofﬁce use only

<!-- b000004 | title | pages [1] -->
55280

<!-- b000005 | prose | pages [1] -->
T1

<!-- b000006 | prose | pages [1] -->
F1

<!-- b000007 | prose | pages [1] -->
T2

<!-- b000008 | prose | pages [1] -->
F2

<!-- b000009 | prose | pages [1] -->
T3

<!-- b000010 | prose | pages [1] -->
F3

<!-- b000011 | prose | pages [1] -->
Problem Chosen

<!-- b000012 | title | pages [1] -->
A

<!-- b000013 | prose | pages [1] -->
T4

<!-- b000014 | prose | pages [1] -->
F4

<!-- b000015 | prose | pages [1] -->
2017 MCM/ICM

<!-- b000016 | heading | pages [1] -->
Summary Sheet

<!-- b000017 | title | pages [1] -->
iMoDs: A Treatment to the Kariba Dam

<!-- b000018 | heading | pages [1] -->
Summary

<!-- b000019 | prose | pages [1] -->
Located on the Zambezi River, the Kariba Dam holds back the world’s largest reser- voir. After so many years, despite efforts to slow its structural problems, the Kariba Dam is in great danger.

<!-- b000020 | prose | pages [1] -->
To address this situation, our paper provides a detailed analysis of one option, re- moving the Kariba Dam and replacing it with a series of ten to twenty smaller dams along the river. We propose a model iMoDS(Integrated Model of Dams in Series) to fully analyze different aspects, such as the number, placement, and height of the new dams. In the meantime, we can set the total water management capabilities as same as the existing dam, providing protection and water management options for Lake Kariba.

<!-- b000021 | prose | pages [1] -->
We ﬁrst analyze the water ﬂow using Manning formula which helps us to analyze a single dam. After that, we simulate a dam in real life with 3ds MAX, show the simpliﬁed dam model on it and derive its storage capacity and building cost.

<!-- b000022 | prose | pages [1] -->
iMoDS model consists of three main submodels, Risk Cost Model, Power Supply Ability Model, and Series Safety Model. For explanation, there is a ﬁgure which connects all related parts together.

<!-- b000023 | prose | pages [1] -->
Risk Cost Model aims at every single dam. It implements risk analysis, using accept- able risk ratio, Pf. Thus, it can make a good balance between cost and safety.

<!-- b000024 | prose | pages [1] -->
Power Supply Ability Model also aims at every single dam, the sum of which mea- sures the beneﬁts our dam system can produce.

<!-- b000025 | prose | pages [1] -->
Series Safety Model measures how safe the whole system is, based on an ideal distri- bution of dams along a river.

<!-- b000026 | prose | pages [1] -->
Then we use AHP to analyze these three submodels and propose iMoDS.

<!-- b000027 | prose | pages [1] -->
To get enough data, we surveyed the literature and other sources. Using genetic algorithm to determine the number and placement, we further solve each dam’s height.

<!-- b000028 | prose | pages [1] -->
Another section of our paper discusses strategies for addressing several situations, including the balance between safety and costs, protection for Lake Kariba, guidances for emergency water ﬂow situations and extreme water ﬂows.

<!-- b000029 | prose | pages [1] -->
In the end, we make sensitivity analysis and discuss strengths and weaknesses.

<!-- b000030 | keywords | pages [1] -->
Keywords: dam series; water ﬂow; risk analysis; integrated model; dam control strategy

<!-- b000031 | furniture | pages [2] -->
Team # 55280

<!-- b000032 | furniture | pages [2] -->
Page 1 of 25

<!-- b000033 | prose | pages [2] -->
iMoDs: A Treatment to the Kariba Dam

<!-- b000034 | prose | pages [2] -->
January 23, 2017

<!-- b000035 | heading | pages [2] -->
Contents

<!-- b000036 | contents | pages [2] -->
1

<!-- b000037 | heading | pages [2] -->
Introduction

<!-- b000038 | prose | pages [2] -->
3

<!-- b000039 | prose | pages [2] -->
Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 3

<!-- b000040 | prose | pages [2] -->
Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2

<!-- b000041 | prose | pages [2] -->
2

<!-- b000042 | heading | pages [2] -->
Assumptions

<!-- b000043 | prose | pages [2] -->
3

<!-- b000044 | heading | pages [2] -->
Nomenclature

<!-- b000045 | prose | pages [2] -->
4

<!-- b000046 | heading | pages [2] -->
Statement of our Model

<!-- b000047 | prose | pages [2] -->
3

<!-- b000048 | prose | pages [2] -->
4

<!-- b000049 | prose | pages [2] -->
4

<!-- b000050 | prose | pages [2] -->
4

<!-- b000051 | prose | pages [2] -->
Behavior of Water Flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 5

<!-- b000052 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2 Analysis of A Single Dam 5

<!-- b000053 | prose | pages [2] -->
iMoDS: Integrated Model of Dams in Series . . . . . . . . . . . . . . . . . . 4.3 7

<!-- b000054 | prose | pages [2] -->
Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3.1 7

<!-- b000055 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3.2 Risk Cost Model 8

<!-- b000056 | prose | pages [2] -->
Series Safety Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3.3 9

<!-- b000057 | prose | pages [2] -->
Power Supply Ability Model . . . . . . . . . . . . . . . . . . . . . . 4.3.4 10

<!-- b000058 | prose | pages [2] -->
Integration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3.5 10

<!-- b000059 | prose | pages [2] -->
Ranking Submodels with AHP . . . . . . . . . . . . . . . . . . . . . 4.3.6

<!-- b000060 | prose | pages [2] -->
5 Implementation

<!-- b000061 | prose | pages [2] -->
11

<!-- b000062 | prose | pages [2] -->
12

<!-- b000063 | prose | pages [2] -->
Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 12

<!-- b000064 | prose | pages [2] -->
Number and placement of the new dams 5.2 . . . . . . . . . . . . . . . . . . .

<!-- b000065 | prose | pages [2] -->
13

<!-- b000066 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2.1 Whole Procedures 13

<!-- b000067 | prose | pages [2] -->
Determining the number and placement by genetic algorithm . . . 5.2.2 13

<!-- b000068 | prose | pages [2] -->
Determining the height of each dam . . . . . . . . . . . . . . . . . . 5.2.3

<!-- b000069 | prose | pages [2] -->
6 Strategies

<!-- b000070 | prose | pages [2] -->
15

<!-- b000071 | prose | pages [2] -->
16

<!-- b000072 | prose | pages [2] -->
A Balance Between Safety and Costs . . . . . . . . . . . . . . . . . . . . . . 6.1 16

<!-- b000073 | furniture | pages [3] -->
Team # 55280

<!-- b000074 | furniture | pages [3] -->
Page 2 of 25

<!-- b000075 | prose | pages [3] -->
Protection for Lake Kariba . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2 17

<!-- b000076 | prose | pages [3] -->
Guidance for Emergency Water Flow Situations 6.3 . . . . . . . . . . . . . . .

<!-- b000077 | prose | pages [3] -->
17

<!-- b000078 | prose | pages [3] -->
Guidance for Extreme Water Flows . . . . . . . . . . . . . . . . . . . . . . . 6.4

<!-- b000079 | prose | pages [3] -->
7

<!-- b000080 | heading | pages [3] -->
Model Analysis

<!-- b000081 | prose | pages [3] -->
18

<!-- b000082 | prose | pages [3] -->
19

<!-- b000083 | prose | pages [3] -->
Sensitivity Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.1 19

<!-- b000084 | prose | pages [3] -->
Impact of Planned Working Years N for a Dam . . . . . . . . . . . . 7.1.1 19

<!-- b000085 | prose | pages [3] -->
Impact of Extreme Condition ratio α . . . . . . . . . . . . . . . . . . 7.1.2 19

<!-- b000086 | prose | pages [3] -->
Strengths and Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.2 20

<!-- b000087 | prose | pages [3] -->
Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.2.1 20

<!-- b000088 | prose | pages [3] -->
Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.2.2

<!-- b000089 | prose | pages [3] -->
8

<!-- b000090 | heading | pages [3] -->
Conclusion

<!-- b000091 | prose | pages [3] -->
Brief Assessment Report

<!-- b000092 | prose | pages [3] -->
20

<!-- b000093 | prose | pages [3] -->
20

<!-- b000094 | prose | pages [3] -->
21

<!-- b000095 | prose | pages [3] -->
Option 1: Repairing the existing Kariba Dam . . . . . . . . . . . . . . . . . . . .

<!-- b000096 | prose | pages [3] -->
21

<!-- b000097 | prose | pages [3] -->
Option 2: Rebuilding the existing Kariba Dam . . . . . . . . . . . . . . . . . . .

<!-- b000098 | prose | pages [3] -->
22

<!-- b000099 | prose | pages [3] -->
Option 3: Removing the Kariba Dam and replacing it with a series of ten to

<!-- b000100 | prose | pages [3] -->
twenty smaller dams along the Zambezi River . . . . . . . . . . . . . . . .

<!-- b000101 | heading | pages [3] -->
Appendices

<!-- b000102 | prose | pages [3] -->
22

<!-- b000103 | prose | pages [3] -->
24

<!-- b000104 | heading | pages [3] -->
Appendix A Implemented Genetic Algorithm

<!-- b000105 | heading | pages [3] -->
Appendix B

<!-- b000106 | prose | pages [3] -->
Fitness Function

<!-- b000107 | prose | pages [3] -->
24

<!-- b000108 | prose | pages [3] -->
24

<!-- b000109 | furniture | pages [4] -->
Team # 55280

<!-- b000110 | furniture | pages [4] -->
Page 3 of 25

<!-- b000111 | prose | pages [4] -->
1

<!-- b000112 | heading | pages [4] -->
Introduction

<!-- b000113 | prose | pages [4] -->
1.1 Problem Background

<!-- b000114 | prose | pages [4] -->
Over ﬁfty years ago, a giant was born on the Zambezi river, along the border be- tween Zimbabwe and Zambia. It provides the two countries with a huge amount of hydropower. The world’s largest reservoir is held by it. This giant was named as Kariba Dam.

<!-- b000115 | caption | pages [4] -->
Figure 1: Kariba Dam

<!-- b000116 | prose | pages [4] -->
Kariba Dam is a double curvature concrete arch dam with 128 metres (420 ft) tall and 579 metres (1,900 ft) long. It was designed to have six spillway gates, which have a discharge capacity of 9500m3/s. Total storage, or overall water management capabilities, is up to 180.6km3. [1].

<!-- b000117 | prose | pages [4] -->
Kariba was designed as a single prupose hydropower project, but as it turned out both ﬁshery and tourism bacame important beniﬁts [1]. Since it was built, this dam is more a landmark than an actual dam for tourists. This area provides them with wa- ter sports and sufﬁcient wildlife resources. Not to mention the fact that Kariba water helps develop the industry of agriculture and ﬁshing. Every coin has two sides. Despite these economical beneﬁts, there are other great environmental impacts, like population displacement and resettlement, and drowned vegetation. [2]

<!-- b000118 | prose | pages [4] -->
However, such a great construction is in great danger and dire need of maintenance. Kariba is threatned by severe droughts, which has lowered the reservoir’s volume to twelve percent of the capacity. What makes the situation more complicated is that if we reﬁll the reservoir, then the dam is very likely to collapse. Due to unexpected ﬂoods and climate changes, the dam seems to be greatly dangerous.

<!-- b000119 | prose | pages [4] -->
1.2 Our Work

<!-- b000120 | prose | pages [4] -->
To address this situation, we have three different options: repairing, rebuilding, or removing the existing Kariba Dam and replacing it with a series of ten to twenty smaller

<!-- b000121 | furniture | pages [5] -->
Team # 55280

<!-- b000122 | furniture | pages [5] -->
Page 4 of 25

<!-- b000123 | prose | pages [5] -->
dams along the Zambezi River.

<!-- b000124 | prose | pages [5] -->
In this paper, we focus on the last option and provide a detailed analysis of it. We propose an integrated model of dams in series. This model not only recommends the number and placement of the dams along the Zambezi River, but also make a balacne between safety and costs. Our system have the same overall water management capa- bilities as the existing Kariba Dam while providing greater levels protection and water management options for Lake Kariba.

<!-- b000125 | prose | pages [5] -->
In Section.2, we state several basic assumptions. Section.3 contains the nomenclature used in model statement. Section.4 provides sufﬁcient details about our model. Section.5 carrys out experiment and analysis about our proposed model. Section.6 provides de- tailed strategies dealing with several conditions. At last, we further study our model in Section.7 and make some conclusions in Section.8.

<!-- b000126 | prose | pages [5] -->
2

<!-- b000127 | heading | pages [5] -->
Assumptions

<!-- b000128 | prose | pages [5] -->
Our model makes the following assumptions:

<!-- b000129 | prose | pages [5] -->
1. In the phase of modeling, we don’t consider extreme conditions on the river, like waterfalls, water cutoff seasons. Because these conditions require extremely big data. They are even unnecessary for in real life dams have dynamic strategies to handle them. We will discuss emergency water ﬂow situations in another Section.

<!-- b000130 | prose | pages [5] -->
2. Other existing dams are ignored. They are not as big as Kariba Dam. Few data about other dams on the river are accessible, especially thier effects on runoff of the river and slope of its hydraulic grade line. This assumption is ﬂexible because it only affects the input data of the river, but not our model.

<!-- b000131 | prose | pages [5] -->
3. We simpliﬁes the water ﬂow into an open-channel ﬂow. Open-channel ﬂow has a free surface. Based on this assumption, we are able to estimate the average velocity of the river’s water ﬂow.

<!-- b000132 | prose | pages [5] -->
3

<!-- b000133 | heading | pages [5] -->
Nomenclature

<!-- b000134 | prose | pages [5] -->
In this paper we use the nomenclature in Table.1 to descibe our model. Other symbols that are used only once will be described later.

<!-- b000135 | prose | pages [5] -->
4

<!-- b000136 | heading | pages [5] -->
Statement of our Model

<!-- b000137 | prose | pages [5] -->
In this section, we will discuss all details about our model. This model takes several ﬁelds into consideration, ranging from liquid ﬂow theory to economy. To begin with, we ﬁrst investigate the behavior of water ﬂow. Then we provide our integrated model of dams in series. This model makes a great balance between safety and costs.

<!-- b000138 | furniture | pages [6] -->
Team # 55280

<!-- b000139 | furniture | pages [6] -->
Page 5 of 25

<!-- b000140 | caption | pages [6] -->
Table 1: Nomenclature

<!-- b000141 | prose | pages [6] -->
Symbol i Deﬁnition the ith dam in a series of small dams Distance from the river’s beginning to dam i Xi Series(X) Value of safety evaluation under a series of dams Value of power supply ability at dam i Supply(Xi) Risk Cost of dam i Risk(Xi) Pf Acceptable risk ratio Volumetric ﬂow rate at time t for dam i Q(Xi; t) Slope of the hydraulic grade line at dam i k(Xi) N Planned working years for a dam n Number of small dams M Overall water management L Length of the Zambezi River d The width of the Zambezi River α Extreme Condition ratio The height of a dam i h(Xi)

<!-- b000142 | prose | pages [6] -->
4.1 Behavior of Water Flow

<!-- b000143 | prose | pages [6] -->
In our model, we need to calculate power supply ability of each dam. One of the key variables is the average velocity of water ﬂowing when it reaches a dam. We have assumed the water ﬂow in the Zambezi river to be a channel ﬂow. Thus, we can employ an empirical formula, the Manning formula, to estimate this velocity. [3]

<!-- b000144 | prose | pages [6] -->
v = k

<!-- b000145 | prose | pages [6] -->
nRh2/3S1/2

<!-- b000146 | prose | pages [6] -->
where:

<!-- b000147 | prose | pages [6] -->
• v is the cross-sectional average velocity;

<!-- b000148 | prose | pages [6] -->
• n is the Gauckler-Manning coefﬁcient;

<!-- b000149 | prose | pages [6] -->
• Rh is the hydraulic radius (L; ft, m);

<!-- b000150 | prose | pages [6] -->
(1)

<!-- b000151 | prose | pages [6] -->
• S is the slope of the hydraulic grade line or the linear hydraulic head loss (L/L);

<!-- b000152 | prose | pages [6] -->
• k is a conversion factor between SI and English units.

<!-- b000153 | prose | pages [6] -->
This formula can be obtained by use of dimensional analysis. With this formula, it is easy to ﬁnd that when water ﬂow reaches a dam, its average velocity only depends on the channel slope S and hydraulic radius Rh.

<!-- b000154 | prose | pages [6] -->
4.2 Analysis of A Single Dam

<!-- b000155 | prose | pages [6] -->
Figure.2 is the simulation of a dam in real life. We determine a reservoir’s storage capacity based on this model. In the literature, Cone method [4] is a common method. Its formula is:

<!-- b000156 | prose | pages [6] -->
n ∑

<!-- b000157 | prose | pages [6] -->
1

<!-- b000158 | prose | pages [6] -->
CA(Xi) =

<!-- b000159 | prose | pages [6] -->
√

<!-- b000160 | prose | pages [6] -->
Ai × Ai+1) × △Li

<!-- b000161 | prose | pages [6] -->
3(Ai + Ai+1 +

<!-- b000162 | prose | pages [6] -->
i=0

<!-- b000163 | furniture | pages [7] -->
Team # 55280

<!-- b000164 | furniture | pages [7] -->
Page 6 of 25

<!-- b000165 | caption | pages [7] -->
Figure 2: A Simulation of a dam with 3ds MAX

<!-- b000166 | prose | pages [7] -->
where:

<!-- b000167 | prose | pages [7] -->
• V is the capacity of reservoir;

<!-- b000168 | prose | pages [7] -->
• Ai is the area of ith cross section;

<!-- b000169 | prose | pages [7] -->
• △Li is the gap between ith and i+1th cross section.

<!-- b000170 | prose | pages [7] -->
For simplicity, we further consider that a reservoir has the areas enclosed by contours in Figure.2, which is colored in black. We use the parameter d to denote the width of the river. Thus, we derive the capacity formula:

<!-- b000171 | prose | pages [7] -->
CA(Xi) = 1

<!-- b000172 | prose | pages [7] -->
3(1 2d × h + d × h) × h(Xi) k(Xi)

<!-- b000173 | prose | pages [7] -->
= h(Xi)2

<!-- b000174 | prose | pages [7] -->
3k(Xi)(3 2d)

<!-- b000175 | prose | pages [7] -->
= h(Xi)2d

<!-- b000176 | prose | pages [7] -->
(2) 2k(Xi)

<!-- b000177 | prose | pages [7] -->
The other key measurement is a dam’s building cost.

<!-- b000178 | prose | pages [7] -->
A basic function contains two parts, construction cost and other unavoidable cost. Construction cost is linear to the volume of the dam. To calculate this volume, we need the bottom width. Actually it is linear to the pressure Pa = ρgh [5].

<!-- b000179 | prose | pages [7] -->
Note that here we calculate the volume of the dam, but not the volume of the reser- voir that is calculated by Equation.2.

<!-- b000180 | prose | pages [7] -->
Finally, it is reasonable to simplify other cost to a constant β, because every construc-

<!-- b000181 | furniture | pages [8] -->
Team # 55280

<!-- b000182 | furniture | pages [8] -->
Page 7 of 25

<!-- b000183 | prose | pages [8] -->
tion work has its initial cost. And there is a safety factor for compressive stress σ [5].

<!-- b000184 | prose | pages [8] -->
Cost(Xi) = λρgh(Xi) × d × h(Xi)

<!-- b000185 | prose | pages [8] -->
+ β 2σ

<!-- b000186 | prose | pages [8] -->
= λρgdh(Xi)2

<!-- b000187 | prose | pages [8] -->
2σ

<!-- b000188 | prose | pages [8] -->
where λ a is volume-to-expense coefﬁcient.

<!-- b000189 | prose | pages [8] -->
+ β (3)

<!-- b000190 | heading | pages [8] -->
iMoDS: Integrated Model of Dams in Series

<!-- b000191 | prose | pages [8] -->
4.3

<!-- b000192 | prose | pages [8] -->
After investigating water’s behavior when it reaches a dam and a single dam, we further proposed an integrated model of dams in series. This model consists of three main parts, Risk Cost Model, Power Supply Ability Model, and Series Safety Model. As illustrated in Figure.3, our model works as an integrated machine which evaluate both a single dam and the whole group. Basically, we can regard it as a nonlinear programming method. Three main parts work as three features derived from different ﬁelds. They are also assigned with different weights according to their own contribution to the whole system.

<!-- b000193 | prose | pages [8] -->
4.3.1 Prerequisites

<!-- b000194 | prose | pages [8] -->
1. Q(Xi; t)

<!-- b000195 | prose | pages [8] -->
The value of Q(Xi; t) is volumetric ﬂow rate at time t for dam i. In our modeling phase, for simplication we replace Q(Xi; t) with Q(Xi; t) to denote the annual av- erage volumetric ﬂow rate. In our paper, d remains the same, so volumetric ﬂow rate upstream is greater than the one downstream. Later we will further discuss and provide speciﬁc guidance for extreme water ﬂows ranging from maximum expected discharges to minimum expected discharges.

<!-- b000196 | caption | pages [8] -->
Figure 3: Overview of Integrated Model of Dams in Series

<!-- b000197 | furniture | pages [9] -->
Team # 55280

<!-- b000198 | prose | pages [9] -->
2. k(Xi) = dElevation(x) |x=Xi dx

<!-- b000199 | furniture | pages [9] -->
Page 8 of 25

<!-- b000200 | prose | pages [9] -->
The placement of each dam is described by the distance from the river’s starting point, Xi. We set the slope of the hydraulic grade line at dam i as the value of k(Xi).

<!-- b000201 | prose | pages [9] -->
More details about k(Xi) will be discussed in Section.5.1.

<!-- b000202 | prose | pages [9] -->
4.3.2

<!-- b000203 | heading | pages [9] -->
Risk Cost Model

<!-- b000204 | prose | pages [9] -->
As Figure.3 shows, Risk Loss and Fundamental Investment determine the output of Risk Cost Model. To build a dam, there are two key factors that we should keep in mind: cost and safety. However, before we try to ﬁnd an equilibrium between them, we have to change it into a math problem. Here we combine them based on risk analysis, a widely used theory in economics. Based on this theory, we numerically determine the safety loss and fundamental cost with an acceptable risk ratio. Because acceptable risk ratio measures the extent that a person focus more on safety than merely cost.

<!-- b000205 | prose | pages [9] -->
Cost - Fundamental Investment Cost reveals how feasible a dam project is. Investors always expect to spend less money while maintaining the same water management abil- ity. A ground truth is that investors must spend more money while paying more atten- tion on safety. Thus, Pf is negatively related to the cost. Its exponent is set by experiment. Slightly modify Equation.3, then it is the equation we need here:

<!-- b000206 | prose | pages [9] -->
Fundamental Investment = Cost(Xi)

<!-- b000207 | prose | pages [9] -->
(4)

<!-- b000208 | prose | pages [9] -->
P 1.1

<!-- b000209 | prose | pages [9] -->
f

<!-- b000210 | prose | pages [9] -->
Given Pf, Equation.4 can measure one dam’s fundamental investment.

<!-- b000211 | prose | pages [9] -->
Safety - Risk Loss Safety reveals how environmental-friendly a dam project is. Projects that pay less attention on safety will result in a high possibility of collaspe. We call it Risk Loss. Equation.5 is the evaluation model. [1 −(1 −Pf)N] is the probability distribution that measures the possibility to collapse. So, we deﬁne the loss at dam i as:

<!-- b000212 | prose | pages [9] -->
collapse probability * (1+ indirect damage index)*Volumetric ﬂow rate

<!-- b000213 | prose | pages [9] -->
Risk Loss = [1 −(1 −Pf)N]α(1 + λ)Q(Xi; t) (5)

<!-- b000214 | prose | pages [9] -->
where α is an coefﬁcent that reveals how likely and serious a river is to suffer from extreme conditions.

<!-- b000215 | prose | pages [9] -->
This method contributes to the evolution of risk-based dam safety assessment meth- ods.

<!-- b000216 | prose | pages [9] -->
Risk(Xi) = Risk Loss + Fundamental Investment

<!-- b000217 | prose | pages [9] -->
Figure.4 shows the function of Pf and Risk Value. Curves with different colors de- note different value of α. From top to bottom, each time α is decreased by 0.05.

<!-- b000218 | furniture | pages [10] -->
Team # 55280

<!-- b000219 | furniture | pages [10] -->
Page 9 of 25

<!-- b000220 | caption | pages [10] -->
Figure 4: Given the same Xi, the function of Pf and Risk Value with different α

<!-- b000221 | prose | pages [10] -->
Observation 1 For each curve, it is strictly decreasing on the left while increasing on the right.

<!-- b000222 | prose | pages [10] -->
Risk Value is not a monotonic function because Risk Loss is a monoton- Illustraion ically increasing function of Pf while Fundamental Investment is a monotonically de- creasing function of Pf.

<!-- b000223 | prose | pages [10] -->
Compared with different curves, the larger α is, the higher Risk Cost Observation 2 is, with the extreme point moving left.

<!-- b000224 | prose | pages [10] -->
If the coefﬁcient α is larger, then it reveals that for a same Pf the govern- Illustraion ment has to handle higher potential losses. Thus, to balance the fundamental cost and safety, the government will have a lower Pf. That’s exactly what our function reveals.

<!-- b000225 | prose | pages [10] -->
4.3.3

<!-- b000226 | heading | pages [10] -->
Series Safety Model

<!-- b000227 | prose | pages [10] -->
Our system removes the Kariba Dam and replaces it with a series of ten to twenty smaller dams. In this model, our goal is to assess a series of dams along the river and give a mark. Researches show that if dams are built uniformly on a river, then this dam system can be operated to produce greater beneﬁts than operating a single large dam.

<!-- b000228 | prose | pages [10] -->
To quantify safety based on locations, we consider two factors involved. One is the average distance between two neighbouring dams. The other is the degree of even dis- tribution. Here we bring in and modify Pearson Chi-Square test to represent it. The more even this distribution is, the safer we consider this system is. Thus, we get the following formula.

<!-- b000229 | prose | pages [10] -->
Series(X) = d

<!-- b000230 | prose | pages [10] -->
(6)

<!-- b000231 | prose | pages [10] -->
∑n−1

<!-- b000232 | prose | pages [10] -->
(di−d)2

<!-- b000233 | prose | pages [10] -->
d2

<!-- b000234 | prose | pages [10] -->
i=1

<!-- b000235 | prose | pages [10] -->
e e

<!-- b000236 | prose | pages [10] -->
where d is the average distance between two neighbouring dams.

<!-- b000237 | furniture | pages [11] -->
Team # 55280

<!-- b000238 | furniture | pages [11] -->
Page 10 of 25

<!-- b000239 | prose | pages [11] -->
4.3.4

<!-- b000240 | heading | pages [11] -->
Power Supply Ability Model

<!-- b000241 | prose | pages [11] -->
Kariba was designed as a single-purpose hydropower project. Embarking on any hy- dropower generation project, it is essential to calculate its amount of hydropower. In our model, the last part is to estimate this kind of economic beneﬁts. If we sum up the power supply of each dam, this model can numerically calculate our new system’s hrdropower supply. Based on the hydropower equation [6], intuitively we get Equation.7 which is a function of the hydraulic head and rate of ﬂuid ﬂow.

<!-- b000242 | prose | pages [11] -->
How much work a unit of water can do depends on its weight times the head. And the power available from a dam can be measured by the density of water, acceleration due to gravity, the ﬂow rate, and the height of fall.

<!-- b000243 | prose | pages [11] -->
Supply(Xi) = ηρgh(Xi)Q(Xi; t) (7)

<!-- b000244 | prose | pages [11] -->
where:

<!-- b000245 | prose | pages [11] -->
• η is the dimensionless efﬁciency of the turbine;

<!-- b000246 | prose | pages [11] -->
• ρ is the density of water in kilograms per cubic metre;

<!-- b000247 | prose | pages [11] -->
• g is the acceleration due to gravity.

<!-- b000248 | prose | pages [11] -->
4.3.5 Integration

<!-- b000249 | prose | pages [11] -->
Based on previous illustrations, we are able to integrate all these features together.

<!-- b000250 | prose | pages [11] -->
• Series(X) Positively related to the safety level. The higher Series(X)’s score is, the better our system is.

<!-- b000251 | prose | pages [11] -->
• Risk(Xi) There is an equilibrium between investment and loss which reaches the lower bound of this model. We always want to save money while ensuring safety. So, the lower Risk(Xi)’s score is, the better our system is.

<!-- b000252 | prose | pages [11] -->
• Supply(Xi) Positively related to power supply. The higher Supply(Xi)’s score is, the better our system is.

<!-- b000253 | prose | pages [11] -->
To make all features equal, we need feature scaling, or data nomalization, because these features all have a broad range of values. If we don’t process thier value, the result of our integrated model may be governed by one of them. In our model, we implement rescaling method. This method rescale the range of features to sacle the range in [0, 1]. The general formula is like this:

<!-- b000254 | prose | pages [11] -->
x −min(x) ′ =

<!-- b000255 | prose | pages [11] -->
x

<!-- b000256 | prose | pages [11] -->
max(x) −min(x)

<!-- b000257 | prose | pages [11] -->
where:

<!-- b000258 | prose | pages [11] -->
• x is an original value;

<!-- b000259 | prose | pages [11] -->
′ is the normalized value. • x

<!-- b000260 | furniture | pages [12] -->
Team # 55280

<!-- b000261 | furniture | pages [12] -->
Page 11 of 25

<!-- b000262 | prose | pages [12] -->
′,

<!-- b000263 | prose | pages [12] -->
After resacling, normalized Series(Xi), Risk(Xi), and Supply(Xi) is Series(Xi)

<!-- b000264 | prose | pages [12] -->
′ respectively. As we can see, Risk(Xi) is negatively related.

<!-- b000265 | prose | pages [12] -->
′, and Supply(Xi)

<!-- b000266 | prose | pages [12] -->
Risk(Xi)

<!-- b000267 | prose | pages [12] -->
Thus we modify it to be positively related by a modiﬁed rescaling method.

<!-- b000268 | prose | pages [12] -->
′ = Series(X) × n −1

<!-- b000269 | prose | pages [12] -->
Series(X)

<!-- b000270 | prose | pages [12] -->
L

<!-- b000271 | prose | pages [12] -->
′ = min(Risk(Xi))/Risk(Xi)

<!-- b000272 | prose | pages [12] -->
Risk(Xi)

<!-- b000273 | prose | pages [12] -->
′ = Supply(X) × n −1

<!-- b000274 | prose | pages [12] -->
Supply(X)

<!-- b000275 | prose | pages [12] -->
L

<!-- b000276 | prose | pages [12] -->
In our model, the goal is to minimize the Final Value. Thus, we scale Supply(Xi) and Series(X) into [−1, 0]. Write our model into a nonlinear programming form then we get

<!-- b000277 | heading | pages [12] -->
the Integrated Model of Dams in Series:

<!-- b000278 | prose | pages [12] -->
′ +

<!-- b000279 | prose | pages [12] -->
max Final Value = Series(X)

<!-- b000280 | prose | pages [12] -->
Xi ≤L, ∀Xi ∈[1, n] s.t

<!-- b000281 | prose | pages [12] -->
n ∑

<!-- b000282 | prose | pages [12] -->
CA(Xi) ≥M

<!-- b000283 | prose | pages [12] -->
i=1

<!-- b000284 | prose | pages [12] -->
10 ≤n ≤20, n ∈Z

<!-- b000285 | prose | pages [12] -->
Xi ≥0, ∀Xi ∈[1, n]

<!-- b000286 | prose | pages [12] -->
where:

<!-- b000287 | prose | pages [12] -->
n ∑

<!-- b000288 | prose | pages [12] -->
′ +

<!-- b000289 | prose | pages [12] -->
n

<!-- b000290 | prose | pages [12] -->
n

<!-- b000291 | prose | pages [12] -->
∑

<!-- b000292 | prose | pages [12] -->
∑

<!-- b000293 | prose | pages [12] -->
′ +

<!-- b000294 | prose | pages [12] -->
′

<!-- b000295 | prose | pages [12] -->
Risk(Xi)

<!-- b000296 | prose | pages [12] -->
Supply(Xi)

<!-- b000297 | prose | pages [12] -->
i=1

<!-- b000298 | prose | pages [12] -->
i=1

<!-- b000299 | prose | pages [12] -->
n ∑

<!-- b000300 | prose | pages [12] -->
′ +

<!-- b000301 | prose | pages [12] -->
′

<!-- b000302 | prose | pages [12] -->
Risk(Xi)

<!-- b000303 | prose | pages [12] -->
Final Value = Series(X)

<!-- b000304 | prose | pages [12] -->
i=1

<!-- b000305 | prose | pages [12] -->
× n −1

<!-- b000306 | prose | pages [12] -->
d =

<!-- b000307 | prose | pages [12] -->
∑n−1

<!-- b000308 | prose | pages [12] -->
(di−d)2

<!-- b000309 | prose | pages [12] -->
L

<!-- b000310 | prose | pages [12] -->
d2

<!-- b000311 | prose | pages [12] -->
i=1

<!-- b000312 | prose | pages [12] -->
e

<!-- b000313 | prose | pages [12] -->
Supply(Xi)

<!-- b000314 | prose | pages [12] -->
i=1

<!-- b000315 | prose | pages [12] -->
n ∑

<!-- b000316 | prose | pages [12] -->
min(Risk(Xi))/{Cost(Xi)

<!-- b000317 | prose | pages [12] -->
+

<!-- b000318 | prose | pages [12] -->
+

<!-- b000319 | prose | pages [12] -->
P 1.1

<!-- b000320 | prose | pages [12] -->
f

<!-- b000321 | prose | pages [12] -->
i=1

<!-- b000322 | prose | pages [12] -->
n ∑

<!-- b000323 | prose | pages [12] -->
[1 −(1 −Pf)N]α(1 + λ)Q(Xi; t)} +

<!-- b000324 | prose | pages [12] -->
4.3.6 Ranking Submodels with AHP

<!-- b000325 | prose | pages [12] -->
ρgηLk(Xi)Q(Xi; t)

<!-- b000326 | prose | pages [12] -->
i=1

<!-- b000327 | prose | pages [12] -->
The analytic hierarchy process (AHP) is a structured technique for organizing and analyzing complex decisions, based on mathematics and psychology. Our goal is to rank previous three submodels and assign weights to iMoDS model.

<!-- b000328 | caption | pages [12] -->
Table 2: AHP production

<!-- b000329 | prose | pages [12] -->
Feature Risk Cost Series Safety Weight 0.5403 0.3478 Power Supply Ability 0.1119

<!-- b000330 | prose | pages [12] -->
Table.2 shows the result of AHP. We then assign them to the model derived in Sec-

<!-- b000331 | furniture | pages [13] -->
Team # 55280

<!-- b000332 | prose | pages [13] -->
tion.4.3.5:

<!-- b000333 | furniture | pages [13] -->
Page 12 of 25

<!-- b000334 | prose | pages [13] -->
n

<!-- b000335 | prose | pages [13] -->
n

<!-- b000336 | prose | pages [13] -->
∑

<!-- b000337 | prose | pages [13] -->
∑

<!-- b000338 | prose | pages [13] -->
′ + 0.54

<!-- b000339 | prose | pages [13] -->
max Final Value = 0.35Series(X)

<!-- b000340 | prose | pages [13] -->
Xi ≤L, ∀Xi ∈[1, n] s.t

<!-- b000341 | prose | pages [13] -->
n ∑

<!-- b000342 | prose | pages [13] -->
CA(Xi) ≥M

<!-- b000343 | prose | pages [13] -->
i=1

<!-- b000344 | prose | pages [13] -->
10 ≤n ≤20, n ∈Z

<!-- b000345 | prose | pages [13] -->
Xi ≥0, ∀Xi ∈[1, n]

<!-- b000346 | prose | pages [13] -->
5 Implementation

<!-- b000347 | prose | pages [13] -->
5.1 Data

<!-- b000348 | prose | pages [13] -->
′ + 0.11

<!-- b000349 | prose | pages [13] -->
′

<!-- b000350 | prose | pages [13] -->
Risk(Xi)

<!-- b000351 | prose | pages [13] -->
Supply(Xi)

<!-- b000352 | prose | pages [13] -->
i=1

<!-- b000353 | prose | pages [13] -->
i=1

<!-- b000354 | prose | pages [13] -->
We tried to ﬁnd some existing dataset about dams, but failed. Thus, in this paper we ourselves analyzed many textual data and ﬁgures from reliable sources and experiment with them. Google Earth provide us with the elevation proﬁle of the Zambezi River. We use Matlab to ﬁt a curve which is shown in Figure.5. The set of blue spots is the raw data while the red curve represents the river’s elevation. This curve is ﬁtted as an eighth-power polynomials.

<!-- b000355 | prose | pages [13] -->
f(Xi) relies on these data.

<!-- b000356 | caption | pages [13] -->
Figure 5: The red curve represents the river’s elevation. X-Axis is the distance from the

<!-- b000357 | prose | pages [13] -->
river’s source while Y-Axis is altitude.

<!-- b000358 | prose | pages [13] -->
Thanks for the basin analysis [7], we are able to analyze the river’s ﬂow data. Fig- ure.6(a) and Figure.6(b) show the Zambezi River mean annual river ﬂow.

<!-- b000359 | prose | pages [13] -->
Q(Xi; t) relies on these data.

<!-- b000360 | furniture | pages [14] -->
Team # 55280

<!-- b000361 | furniture | pages [14] -->
Page 13 of 25

<!-- b000362 | prose | pages [14] -->
(a) 2D version. It includes surrounding coun-

<!-- b000363 | prose | pages [14] -->
(b) 3D version. It includes the river’s elevation

<!-- b000364 | prose | pages [14] -->
tries and cities.

<!-- b000365 | prose | pages [14] -->
changes.

<!-- b000366 | caption | pages [14] -->
Figure 6: Zambezi River’s mean annual river ﬂow. The violet, pink, and yellow bands

<!-- b000367 | prose | pages [14] -->
represents the upstream, midstream, and downstream, respectively. Width of each band measures the value of mean annual river ﬂow.

<!-- b000368 | prose | pages [14] -->
5.2 Number and placement of the new dams

<!-- b000369 | prose | pages [14] -->
5.2.1 Whole Procedures

<!-- b000370 | prose | pages [14] -->
1. Set all small dams to have equal height;

<!-- b000371 | prose | pages [14] -->
2. Use heuristic algorithm, like generic algorithm, to run iMoDS model;

<!-- b000372 | prose | pages [14] -->
3. Based on the set {Xi} which is found in Step 2, use Equation.8 to reset each one’s height.

<!-- b000373 | prose | pages [14] -->
4. Test constraint by Equation.9. If it doesn’t meet, tune {Xi} and go to Step 3.

<!-- b000374 | prose | pages [14] -->
5.2.2

<!-- b000375 | heading | pages [14] -->
Determining the number and placement by genetic algorithm

<!-- b000376 | prose | pages [14] -->
The optimization of a dam group is high dimensional, multilevel, and nonlinear. Classical algorithm that solves linear programming problems are impossible to ﬁnd the global optimum. Heuristic algorithm, however, can solve this optimization problem. Genetic algorithm(GA), based on a antural selection process that mimics biological evo- lution, is one of them.

<!-- b000377 | prose | pages [14] -->
In this section, we give an analysis about the number and placement of dams, and also provide a recommendation. However, if the height of each dam is dynamic, it will be a problem of over 20 dimensions. For simpliﬁcation we assume that each small dam is in equal size.

<!-- b000378 | prose | pages [14] -->
Because of the simpliﬁcation, h(Xi) is a constant. The whole evaluation is sensitive to the variables, {Xi}, Pf and n. To ﬁnd the optimal solution, we use genetic algorithm to simulate the evaluation process. Codes are listed in Appendices.

<!-- b000379 | prose | pages [14] -->
Weights of three key features have been provided by AHP. Risk Cost dominates the other two features. To maximum min Risk(Xi)

<!-- b000380 | prose | pages [14] -->
and meet the constraint, total water man- Risk(Xi) agement M, the algorithm will select Pf to an optimal value which has been introduced

<!-- b000381 | furniture | pages [15] -->
Team # 55280

<!-- b000382 | furniture | pages [15] -->
Page 14 of 25

<!-- b000383 | caption | pages [15] -->
Figure 7: Best placement of new dams with different quantity of dams

<!-- b000384 | prose | pages [15] -->
in Figure.4, i.e., locating dams to relatively gentle slopes. Although Power Supply takes a small weight, the value will greatly increase when the dam is on a steep terrain. Fi- nally, Series is more likely to let these dams in a evenly distribution. Considering the interaction between three features, the ﬁnal placement shows like Figure.7.

<!-- b000385 | prose | pages [15] -->
Figure.8 shows that when n = 13 and Pf = 0.0024, the evaluation reaches the peak value, or the optimal value. It is cogent for our model.

<!-- b000386 | prose | pages [15] -->
This result is convincing. If the quantity of dams n increases, then:

<!-- b000387 | prose | pages [15] -->
1. ∑min(Risk(Xi)) decreases. Although the height of each dam is smaller, sum of ini- Risk(Xi) tial cost β increases.

<!-- b000388 | prose | pages [15] -->
2. ∑Supply(Xi) increases and then decreases. With n increasing, the ideal hydropower supply goes higher. But when n goes to large, Series(X) will restrict it to goes

<!-- b000389 | caption | pages [15] -->
Table 3: Accurate placement of dams when n = 13 and Pf = 0.0024

<!-- b000390 | prose | pages [15] -->
Distance Xi/m Order of Dam Elevation/m 288.3 1 1160.2 494.5 2 1136.3 664.4 3 1084.55 810.0 4 5 6 7 1057 843 932 879 790 954 651 1160 8 638 1323 9 520 1552 10 468 1729 11 453 1924 12 257 2098 13 195

<!-- b000391 | furniture | pages [16] -->
Team # 55280

<!-- b000392 | furniture | pages [16] -->
Page 15 of 25

<!-- b000393 | caption | pages [16] -->
Figure 8: Trend of Final Value with n increasing

<!-- b000394 | prose | pages [16] -->
lower.

<!-- b000395 | prose | pages [16] -->
3. Series(X) is not relevant to the quantity of n.

<!-- b000396 | prose | pages [16] -->
Thus, in this decision-making process, there is an equilibrium between ten and twenty. We ﬁnd that it is n = 13 with Pf = 0.0024.

<!-- b000397 | prose | pages [16] -->
Table.3 shows the optimal result of this new dam system. From dam 1 to dam 13, we recommend each dam’s placement. Note that DistanceXi denotes the distance from the river’s source to dam i. Due to the restriction in this nonlinear programming, the overall water management capacities is the same as the existing Kariba Dam.

<!-- b000398 | prose | pages [16] -->
5.2.3 Determining the height of each dam

<!-- b000399 | prose | pages [16] -->
Here we eliminate the assumption that each small dam is in equal size. If we refer to Section.4.2, the height of a dam is really a key factor to the ﬁnal evaluation as it inﬂuences the system’s risk cost and power supply that these dams can totally provide. It is critical to determine the height of each dam so that the system’s ﬁnal value can be optimized. Given Pf, a single dam’s contribution to the whole system(iMoDS model) is a function of one variable, h(Xi). So we can ignore Series(Xi). To optimize the contribution, let the

<!-- b000400 | furniture | pages [17] -->
Team # 55280

<!-- b000401 | furniture | pages [17] -->
Page 16 of 25

<!-- b000402 | caption | pages [17] -->
Figure 9: Placement of 13(optimal quantity) dams along the Zambezi River. Each dam is

<!-- b000403 | prose | pages [17] -->
labelled with its height. The blue areas are each dam’s corresponding reservoirs.

<!-- b000404 | prose | pages [17] -->
differential equation to be zero:

<!-- b000405 | prose | pages [17] -->
Supply(Xi)′ −Risk(Xi)′ = 0

<!-- b000406 | prose | pages [17] -->
ηρgQ(Xi; t) −λ2ρgdh(Xi)

<!-- b000407 | prose | pages [17] -->
= 0

<!-- b000408 | prose | pages [17] -->
2σP 1.1 f f

<!-- b000409 | prose | pages [17] -->
ησP 1.1

<!-- b000410 | prose | pages [17] -->
f Q(Xi; t)

<!-- b000411 | prose | pages [17] -->
h(Xi) =

<!-- b000412 | prose | pages [17] -->
(8) λd

<!-- b000413 | prose | pages [17] -->
We can ﬁnd that with Q(Xi; t) increasing, the best h(Xi) increases. However, there is a constraint to h(Xi).

<!-- b000414 | prose | pages [17] -->
n ∑

<!-- b000415 | prose | pages [17] -->
CA(Xi) =

<!-- b000416 | prose | pages [17] -->
i=1

<!-- b000417 | prose | pages [17] -->
n n ∑

<!-- b000418 | prose | pages [17] -->
h(Xi)2d

<!-- b000419 | prose | pages [17] -->
2k(Xi) ≥M (9)

<!-- b000420 | prose | pages [17] -->
i=1

<!-- b000421 | heading | pages [17] -->
1. If our optimal {Xi} meets the constraint, Equation.9, then it is the ﬁnal result.

<!-- b000422 | heading | pages [17] -->
2. Else, we can slightly modify Xi to meet the constraint.

<!-- b000423 | prose | pages [17] -->
Thus, Final Value of iMoDS model and each dam’s height are both determined by {Xi}.

<!-- b000424 | prose | pages [17] -->
Figure.9 is our ﬁnal result of placement and number.

<!-- b000425 | prose | pages [17] -->
6 Strategies

<!-- b000426 | prose | pages [17] -->
A Balance Between Safety and Costs 6.1

<!-- b000427 | prose | pages [17] -->
Our new multiple dam system is modeled based on three key factors, Risk Cost, Power Supply, and Series Safety. Risk Cost fully considers the balance between safety and costs by acceptable risk ratio Pf. Series Safety further investigates the safety of a dam group. Thus, our system is well-balanced. What’s more, we also take beneﬁts into consideration.

<!-- b000428 | furniture | pages [18] -->
Team # 55280

<!-- b000429 | furniture | pages [18] -->
Page 17 of 25

<!-- b000430 | prose | pages [18] -->
6.2 Protection for Lake Kariba

<!-- b000431 | prose | pages [18] -->
Now we take the ability of protecting Lake Kariba into consideration. In the former section, we degenerate this factor to the total volume of the reservoirs. However, we ﬁnd it is reasonable to evaluate it with the relative distance between a reservoir and the lake. We ﬁnally determined to use a gentle Gaussian curve to give a weight of each dam.

<!-- b000432 | prose | pages [18] -->
n ∑

<!-- b000433 | prose | pages [18] -->
CA(Xi)N (XLake, σ2)

<!-- b000434 | prose | pages [18] -->
Protection =

<!-- b000435 | prose | pages [18] -->
(10)

<!-- b000436 | prose | pages [18] -->
i=1

<!-- b000437 | prose | pages [18] -->
where XLake is the location of Lake Kariba, σ is a ﬁtting factor.

<!-- b000438 | prose | pages [18] -->
To as greatly as possible increase the total Protection to the River, we can build dams near the lake with more capacity,i.e., stronger ability of management of the water.

<!-- b000439 | prose | pages [18] -->
When it is the period of the dry season, the lower dams near Lake Kariba should start to reserve water and higher dams start to discharge water untill this season passes. On the contrary, when it is the wet season, the behavior of dams near the lake are opposite to the former condition.

<!-- b000440 | prose | pages [18] -->
We also need to consider the ecosystem of the lake, so dams near the lake need to be designed carefully to minimize the damage to the environment.

<!-- b000441 | prose | pages [18] -->
6.3 Guidance for Emergency Water Flow Situations

<!-- b000442 | prose | pages [18] -->
Emergency water ﬂow situation(i.e. ﬂooding and prolonged low water conditions) can generate catastrophe. Flood water may wash away any cities downstream and cause considerable loss of life. Extreme low water conditions could destory many ﬁelds of a country. To ensure the safety of our new dam system, we will provide the ZRA managers with speciﬁc guidance.

<!-- b000443 | prose | pages [18] -->
The aim of this guidance is prevent an uncontrolled release of water from reservoirs.

<!-- b000444 | prose | pages [18] -->
For ﬂood control, our objective is to maintain as much control over ﬂows entering the system above a critical ﬂood-prone reach as possible. [8]

<!-- b000445 | prose | pages [18] -->
Method Filling the upper reserviors ﬁrst and emptying the lower reservoirs ﬁrst.

<!-- b000446 | prose | pages [18] -->
An illustration of this method has been studied [9]. Flood storage at the reservoir close to upstream provides greater ﬂood controlability than the lower reservoirs.

<!-- b000447 | prose | pages [18] -->
However, an exception is that if the lower reservoir’s outﬂow capacity is restricted, then it is better to ﬁll the lower reservoir ﬁrst to increase head on the outlet. In this way we can increase the release capacity from the entire sistem to the downstream channel capacity. This exception is prepared for some extremely serious ﬂoods.

<!-- b000448 | prose | pages [18] -->
For prolonged low water conditions, our objective is to maintain the river runoff.

<!-- b000449 | prose | pages [18] -->
Method Emptying the reservoirs from lower ones to higher ones

<!-- b000450 | prose | pages [18] -->
In this kind of periods, the river’s natural runoff is considerably smaller than an- nual water runoff. We must take advantage of the dam system’s capability of dynamic

<!-- b000451 | furniture | pages [19] -->
Team # 55280

<!-- b000452 | furniture | pages [19] -->
Page 18 of 25

<!-- b000453 | prose | pages [19] -->
scheduling. In other owrds, we maintain the river’s minimum runoff by compensative regulation. Empty the reservoirs downstream ﬁrst can avoid people’s water shortage while enabling reservoirs upstream to store water.

<!-- b000454 | prose | pages [19] -->
6.4 Guidance for Extreme Water Flows

<!-- b000455 | prose | pages [19] -->
In our previous analysis, we use Q(Xi; t) to denote the annual water ﬂow. However in real life, Q(Xi; t) should be a function of time t. Along the Zambezi River there is a dry season and a wet season.

<!-- b000456 | prose | pages [19] -->
1. Dry Season

<!-- b000457 | prose | pages [19] -->
It is clear that the dam system need to discharge in dry season. First, we suppose that dry season lasts for time T. At the beginning of the dry season all reservoirs have reached their full capacities. Second, we introduce three parameters,p, k, and m. p denotes the speed of discharging. k denotes the rate of lost water because of evaporation and washing away. m is the amount of remaining water. The problem is then simpliﬁed as an expression of discharging all reserved water during the dry season with some speed.

<!-- b000458 | prose | pages [19] -->
dm

<!-- b000459 | prose | pages [19] -->
dt = −p −km

<!-- b000460 | prose | pages [19] -->
Solve this function, we get:

<!-- b000461 | prose | pages [19] -->
m = ce−kt −p

<!-- b000462 | prose | pages [19] -->
k Let m(0) = M, m(T) = 0

<!-- b000463 | prose | pages [19] -->
Then p = Mke−kT

<!-- b000464 | prose | pages [19] -->
1 −e−kT

<!-- b000465 | prose | pages [19] -->
Now we qualitatively analyze this discharging speed. Because the water in the upper reservoirs is shared by all the terrain along the river. On the contrary, the water of the reservoirs downstream is only used by relatively small terrain. It is reasonable that in the dry season, the reservoirs upstream have a larger speed than those downstream. And the average speed of the whole system is p.

<!-- b000466 | prose | pages [19] -->
2. Wet Season

<!-- b000467 | prose | pages [19] -->
It has a high rainfall in wet season, so we need to charge reservoirs to avoid great increment of the level of riverway and prepare for the next dry season. We can assume that rainfall is uniformly distributed along the whole river. The upper reservoirs must start to store water ﬁrst. Because if a reservoir downstream ﬁrst to start storing water, Q(Xi; t) will be too large and leads to great risk and waste of water.

<!-- b000468 | furniture | pages [20] -->
Team # 55280

<!-- b000469 | furniture | pages [20] -->
Page 19 of 25

<!-- b000470 | prose | pages [20] -->
7

<!-- b000471 | heading | pages [20] -->
Model Analysis

<!-- b000472 | prose | pages [20] -->
7.1

<!-- b000473 | heading | pages [20] -->
Sensitivity Analysis

<!-- b000474 | prose | pages [20] -->
Our iMoDS model contains several parameters. We determine some of the parame- ters through least square ﬁtting, some of them by knowledge in the literature, and other methods. In this section, we would like to produce a sensitibity analysis to show whether our model is sensitive to different values of parameters.

<!-- b000475 | prose | pages [20] -->
We will study the impact of two importnant parameters in our model.

<!-- b000476 | prose | pages [20] -->
Impact of Planned Working Years N for a Dam 7.1.1

<!-- b000477 | caption | pages [20] -->
Figure 10: Given the same Xi, the function of Pf and Risk Value with different N

<!-- b000478 | prose | pages [20] -->
N is set to be 50 and not changed ever since. In the literature, a dam over 50 years old is deﬁned to be dangerous. The Kariba Dam is one of them. We vary this value from

<!-- b000479 | heading | pages [20] -->
50 to 100 by 10. Figure.10 proves that the trends of Risk Loss remains to be the same.

<!-- b000480 | prose | pages [20] -->
Therefore, we come to the conclusion that our model is not sensitive to N.

<!-- b000481 | prose | pages [20] -->
Impact of Extreme Condition ratio α 7.1.2

<!-- b000482 | prose | pages [20] -->
Figure.4 shows the sensitivity analysis of α. To avoid repetition, we don’t illustrate it here again.

<!-- b000483 | furniture | pages [21] -->
Team # 55280

<!-- b000484 | furniture | pages [21] -->
Page 20 of 25

<!-- b000485 | prose | pages [21] -->
7.2

<!-- b000486 | heading | pages [21] -->
Strengths and Weaknesses

<!-- b000487 | prose | pages [21] -->
7.2.1

<!-- b000488 | heading | pages [21] -->
Strengths

<!-- b000489 | prose | pages [21] -->
1. Use accurate data of the Zambezi River. From the very beginning of our analysis, we emphasize on mining useful data. Only with these dependable data, we can conclude that the model we built is appropriate.

<!-- b000490 | prose | pages [21] -->
2. Design a novel and innovative evaluation rules of dam construction. We used methods across disciplines to give an integrated evaluation function of dams. AHP and GA are leveraged in our simulation which can provide reliable results of the model.

<!-- b000491 | prose | pages [21] -->
3. Use fancy visualization to display our model.

<!-- b000492 | prose | pages [21] -->
7.2.2

<!-- b000493 | heading | pages [21] -->
Weaknesses

<!-- b000494 | prose | pages [21] -->
1. Heuristic algorithm has randomness. Because of the high dimensional constraint, we used GA as our simulation algorithm. We cannot always get the optimal results for the sites selection

<!-- b000495 | prose | pages [21] -->
2. Some real water conditions are omitted. We simpliﬁed the river as an open chan- nel. However, the real condition is much more complex. It will also inﬂuence the construction cost and safety evaluation.

<!-- b000496 | prose | pages [21] -->
3. Lacking details of the trade-off function. We paid an emphasis on the balance be- tween cost and safety. Though we have added power supply to our model, it still lacks other beneﬁts of dam construction.

<!-- b000497 | prose | pages [21] -->
8

<!-- b000498 | heading | pages [21] -->
Conclusion

<!-- b000499 | prose | pages [21] -->
Our papaer provides a detailed analysis of removing the Kariba Dam and replacing it with a series of ten to twenty smaller dams along the river. Before introducing the model, we analyze water ﬂow and a single dam. Then our model iMoDS is proposed. It takes safety, cost, and beneﬁts into consideration and makes a balance of them. Three submodels, Risk Cost Model, Power Supply Ability Model, and Series Safety Model, form the integrated model.

<!-- b000500 | prose | pages [21] -->
We use real data to give a recommendation as to the number, placement, and height of the new dams. For this is a high dimensional problem, we implement GA to ﬁnd a global optimum result.

<!-- b000501 | prose | pages [21] -->
Strategies are fully discussed. Balance between safety and costs have been inlcuded in the integrated model. Protection for Lake Kariba uses Gaussian curve to give a weight of each dam. And two guidances include speciﬁc instructions of the dam group when facing these conditions.

<!-- b000502 | furniture | pages [22] -->
Team # 55280

<!-- b000503 | prose | pages [22] -->
Brief Assessment Report

<!-- b000504 | furniture | pages [22] -->
Page 21 of 25

<!-- b000505 | prose | pages [22] -->
The Kariba Dam, which was opened in 1959 and held back the world’s largest reser- voir, has been working for over 50 years and faces the possibility of callapse. Also serv- ing as a major supply of Zambia and nearby contries’ electricity, it is in dire need of maintenance. To deal with this situation, there are three major options available to the Zambezi River Authority (ZRA). For each option, we will access its potential cost ne- murically and provide other aspects of information.

<!-- b000506 | prose | pages [22] -->
In the literature, the rate of failure for dams has been studied. With Bayesian analysis approach, researchers [10] evaluated the dam failure rate uncertainty. They found uni- versal failure rate to be steady and got the value of 3 × 10−4. However, we investigate the whole life cycle of a dam. Its failure rate [11] should be a function of time t, denoted as FR(T)

<!-- b000507 | prose | pages [22] -->
{

<!-- b000508 | prose | pages [22] -->
3 × 10−4

<!-- b000509 | prose | pages [22] -->
FR(T) =

<!-- b000510 | prose | pages [22] -->
1 −e−( t+143.67 100 if 0 ≤T < 50 years (11) )3 if T ≥50 years

<!-- b000511 | caption | pages [22] -->
Figure 11: A Dam’s Failure Rate

<!-- b000512 | prose | pages [22] -->
Figure.11 shows a dam’s failure rate with the change of years.

<!-- b000513 | prose | pages [22] -->
Option 1: Repairing the existing Kariba Dam

<!-- b000514 | prose | pages [22] -->
Once mechanized systems supplant natural ones, they must be managed in perpetu- ity, or else they break down [12]. In the past ﬁfties years, the torrents has been consis- tantly eroding the dam’s structure. The ﬁrst option is to repair this existing giant.

<!-- b000515 | prose | pages [22] -->
Potential Cost One report [13] said that expected cost will be $294 million this time. However, repair can handle current situation but never eliminate the potential danger. Thus, we explore an expectation of future failure rate by modifying Equation.11

<!-- b000516 | prose | pages [22] -->
FRrepair(t) = 1 −e−( t+143.67

<!-- b000517 | prose | pages [22] -->
)3, (12) 100

<!-- b000518 | prose | pages [22] -->
where t = how many years have passed since last repair.

<!-- b000519 | prose | pages [22] -->
Thus, given a speciﬁc year Y and annual cost of repair C, the potential costs will be:

<!-- b000520 | prose | pages [22] -->
∫Y −2017 294 + C ×

<!-- b000521 | prose | pages [22] -->
0 FRrepair(t)dt (13)

<!-- b000522 | furniture | pages [23] -->
Team # 55280

<!-- b000523 | prose | pages [23] -->
Beneﬁts

<!-- b000524 | furniture | pages [23] -->
Page 22 of 25

<!-- b000525 | prose | pages [23] -->
Repair signiﬁcantly saves the construction period.It doesn’t affect hydro power supply which is generated from the reservior.

<!-- b000526 | heading | pages [23] -->
Shortcomings

<!-- b000527 | prose | pages [23] -->
Potential danger to collapse. High repair rate with high cost each time.

<!-- b000528 | prose | pages [23] -->
Option 2: Rebuilding the existing Kariba Dam

<!-- b000529 | prose | pages [23] -->
Potential Cost Rebuilding such a giant dam is extremely expensive.

<!-- b000530 | prose | pages [23] -->
According to Kariba Dam - Case Study [1], the project was built in two stages. The total cost of two stages amounted to $1.8 billion. To know how much it will cost now, we estimate it with The Consumer Price Index(CPI) [14]. CPI for the 1950’s was 27.2 while current CPI is about 241.4. Thus, the total cost of rebuilding is about 241.4/27.2 × $1.8 = $15.975 billion.

<!-- b000531 | prose | pages [23] -->
Also we calculate future cost: given a speciﬁc year Y and annual cost of repair C, the potential costs will be:

<!-- b000532 | prose | pages [23] -->
∫Y −2017 7440 + C ×

<!-- b000533 | prose | pages [23] -->
Beneﬁts

<!-- b000534 | prose | pages [23] -->
FR(t)dt (14) 0 0

<!-- b000535 | prose | pages [23] -->
No severe potential danger any more. No need to repair very often.

<!-- b000536 | heading | pages [23] -->
Shortcomings

<!-- b000537 | prose | pages [23] -->
A long period of time under construction. Lack of a Dam, affecting hydro power supply, and protection for Lake Kariba.

<!-- b000538 | prose | pages [23] -->
Option 3: Removing the Kariba Dam and replacing it with a series of ten to twenty smaller dams along the Zambezi River

<!-- b000539 | prose | pages [23] -->
Potential Costs The construction cost can be described as:

<!-- b000540 | prose | pages [23] -->
Construction cost = k ∗capacity + basic cost

<!-- b000541 | prose | pages [23] -->
Considering that the total capacity of these small dams is equal to the capacity of Kariba Dam, the construction cost of Option 3 is close to n times of basic cost plus the cost of Option 2, where n is the number of these small dams. Here we suppose that the basic cost is 10% of the total construction cost and the cost of removing Kariba Dam is about 15% of the total construction cost, thus, the total construction cost is about $15.975∗ (1 + 10% ∗n + 15%) = $34.363 to $50.321 billion.

<!-- b000542 | prose | pages [23] -->
Let n = 13, the cost of the solution we give in our model is about $39.139 billion.

<!-- b000543 | prose | pages [23] -->
Beneﬁts Strengthen the ability to handle emergency water ﬂow, protect Lake Kariba, and adjust water ﬂow between seasons.

<!-- b000544 | heading | pages [23] -->
Shortcomings

<!-- b000545 | prose | pages [23] -->
It costs most in these 3 options, and it brings in new problems of coor- dinating and control in a dam system.

<!-- b000546 | furniture | pages [24] -->
Team # 55280

<!-- b000547 | heading | pages [24] -->
References

<!-- b000548 | references | pages [24] -->
[1] “Kariba

<!-- b000549 | references | pages [24] -->
dam-case

<!-- b000550 | references | pages [24] -->
study,”

<!-- b000551 | references | pages [24] -->
World

<!-- b000552 | furniture | pages [24] -->
Page 23 of 25

<!-- b000553 | references | pages [24] -->
Commission

<!-- b000554 | references | pages [24] -->
on

<!-- b000555 | references | pages [24] -->
Dams,

<!-- b000556 | references | pages [24] -->
2010.

<!-- b000557 | references | pages [24] -->
[On-

<!-- b000558 | references | pages [24] -->
http://202.120.0.1/cache/1/03/nanjing-school.com/

<!-- b000559 | references | pages [24] -->
line].

<!-- b000560 | references | pages [24] -->
Available:

<!-- b000561 | references | pages [24] -->
897d9a2a02069bb2075b729dd8c33afb/World_Commission_on_Dams_2000_Case_

<!-- b000562 | references | pages [24] -->
Study_Kariba_Dam_Final_Report_November_2000-2etc5lv.pdf

<!-- b000563 | references | pages [24] -->
[2] “Kariba dam,” Wikipedia. [Online]. Available: https://en.wikipedia.org/wiki/

<!-- b000564 | references | pages [24] -->
Kariba_Dam

<!-- b000565 | references | pages [24] -->
[3] “Manning formula,” Wikipedia. [Online]. Available: https://en.wikipedia.org/

<!-- b000566 | references | pages [24] -->
wiki/Manning_formula

<!-- b000567 | references | pages [24] -->
[4] “Determination

<!-- b000568 | references | pages [24] -->
of

<!-- b000569 | references | pages [24] -->
reservoir

<!-- b000570 | references | pages [24] -->
storage

<!-- b000571 | references | pages [24] -->
capacity,”

<!-- b000572 | references | pages [24] -->
Education.

<!-- b000573 | references | pages [24] -->
http://www.slideshare.net/chingtonymbuma/

<!-- b000574 | references | pages [24] -->
[Online].

<!-- b000575 | references | pages [24] -->
Available:

<!-- b000576 | references | pages [24] -->
determination-of-reservoir-storage-capacity

<!-- b000577 | references | pages [24] -->
[5] Z. W.-y. YANG Qiang, WU Hao, “Stress evaluation in ﬁnite element analysis of

<!-- b000578 | references | pages [24] -->
dams,” Engineering Mechanics(In Chinese), vol. 23(1), pp. 69–73, 2006.

<!-- b000579 | references | pages [24] -->
[6] “Hydropower,” Wikipedia. [Online]. Available: https://en.wikipedia.org/wiki/

<!-- b000580 | references | pages [24] -->
Hydropower

<!-- b000581 | references | pages [24] -->
A multi-sector investment opportunities analysis

<!-- b000582 | references | pages [24] -->
[7] “The zambezi river basin :

<!-- b000583 | references | pages [24] -->
- basin development scenarios,” World Bank, 2010. [Online]. Available: https:

<!-- b000584 | references | pages [24] -->
//openknowledge.worldbank.org/handle/10986/2959

<!-- b000585 | references | pages [24] -->
[8] J. G. Jay R. Lund, “Some derived operating rules for reservoirs in series or in par-

<!-- b000586 | references | pages [24] -->
allel,” Journal of Water Resources Planning and Management, vol. 125(3), pp. 143–153,

<!-- b000587 | references | pages [24] -->
1999.

<!-- b000588 | references | pages [24] -->
[9] J.Kelman and J.P.DAMAZIO, “The determination of ﬂood control volumes in a mul-

<!-- b000589 | references | pages [24] -->
tireservoir system,” Journal of Water Resources Planning and Management, vol. 25(3),

<!-- b000590 | references | pages [24] -->
pp. 337–344, 1989.

<!-- b000591 | references | pages [24] -->
[10] J. Vail, F. Ferrante, and J. Mitman, “Generic failure rate evaluation for jocassee

<!-- b000592 | references | pages [24] -->
dam,” UNITED STATES NUCLEAR REGULATORY COMMISSION, 2010. [Online].

<!-- b000593 | references | pages [24] -->
Available: https://www.nrc.gov/docs/ML1303/ML13039A084.pdf

<!-- b000594 | references | pages [24] -->
[11] “Bathtub curve,” Wikipedia. [Online]. Available: https://en.wikipedia.org/wiki/

<!-- b000595 | references | pages [24] -->
Bathtub_curve

<!-- b000596 | references | pages [24] -->
[12] J.

<!-- b000597 | references | pages [24] -->
Leslie,

<!-- b000598 | references | pages [24] -->
“One

<!-- b000599 | references | pages [24] -->
of

<!-- b000600 | references | pages [24] -->
africa’s

<!-- b000601 | references | pages [24] -->
biggest

<!-- b000602 | references | pages [24] -->
dams

<!-- b000603 | references | pages [24] -->
is

<!-- b000604 | references | pages [24] -->
falling

<!-- b000605 | references | pages [24] -->
apart,”

<!-- b000606 | references | pages [24] -->
The

<!-- b000607 | references | pages [24] -->
New

<!-- b000608 | references | pages [24] -->
http://www.newyorker.com/tech/elements/

<!-- b000609 | references | pages [24] -->
Yorker, 2016. [Online]. Available:

<!-- b000610 | references | pages [24] -->
one-of-africas-biggest-dams-is-falling-apart

<!-- b000611 | references | pages [24] -->
[13] “Zambia, zimbabwe to start kariba dam repairs in early 2017,” REUTERS

<!-- b000612 | references | pages [24] -->
AFRICA, 2016. [Online]. Available: http://af.reuters.com/article/zambiaNews/

<!-- b000613 | references | pages [24] -->
idAFL5N17T1OI

<!-- b000614 | references | pages [24] -->
[14] N. G. Mankiw, Principles of macroeconomics.

<!-- b000615 | references | pages [24] -->
Cengage Learning, 2014.

<!-- b000616 | furniture | pages [25] -->
Team # 55280

<!-- b000617 | furniture | pages [25] -->
Page 24 of 25

<!-- b000618 | heading | pages [25] -->
Appendices

<!-- b000619 | heading | pages [25] -->
Appendix A

<!-- b000620 | heading | pages [25] -->
Implemented Genetic Algorithm

<!-- b000621 | prose | pages [25] -->
n=13;% need adjust B_sub1=[zeros(n,1);0.00001]; %B_sub1 means the VLB of the Xi B_sub2=[ones(n,1)*2100;0.1]; %B_sub2 means the VUB of the Xi B=[B_sub1,B_sub2]; % constraint of Xi initPop=initializega(n,B,’fitness’); [x endPop,bPop,trace]=ga(B,’fitness’,[],initPop,[1e-6 1 1],

<!-- b000622 | prose | pages [25] -->
’maxGenTerm’,10000,’normGeomSelect’,... [0.08],[’arithXover’],[2],’nonUnifMutation’,[2 10000 3]); %3000 generations xx=sort(x(1:14)); % sites selection sorts as ascending order x=[xx,x(15)]; % the last one is the evaluation value

<!-- b000623 | heading | pages [25] -->
Appendix B

<!-- b000624 | prose | pages [25] -->
Fitness Function

<!-- b000625 | prose | pages [25] -->
function[sol,eval]=fitness(sol,~) n=13; x=sol(1,1:n+1); xx=sort(x(1:n)); x=[xx,x(n+1)]; p1=0; p2=0; cc=0; N=50; Ca=300; BB=6000; aa1=400; rr=0.8; pp=1005; yy=0.5; l=200; Cmin=2e6; Pm=1e8; % above are the constant parameter setting wei=[0.12,0.54,0.34]; % wei means the weight of three key function for i=1:n

<!-- b000626 | prose | pages [25] -->
k=my(x(i)); Q=my2(x(i)); R=(1-(1-x(n+1))^N)*Q*aa1*(1+rr); C=((Ca/n)*k+BB)*(1/(x(n+1))^1.1); Power=Q*pp*yy*k*l*9.8/1000; p1=p1+Power; p2=p2+C+R; end p1=p1/Pm p2=Cmin/p2

<!-- b000627 | furniture | pages [26] -->
Team # 55280

<!-- b000628 | furniture | pages [26] -->
Page 25 of 25

<!-- b000629 | prose | pages [26] -->
for j=1:n-1

<!-- b000630 | prose | pages [26] -->
cc=cc+((x(n)-x(1))/(n-1)-(x(j+1)-x(j)))^2; end

<!-- b000631 | prose | pages [26] -->
Sa=((x(n)-x(1))/exp(cc/((x(n)-x(1))/(n-1))^2))/2100 eval=p1*wei(1)+Sa*wei(3)+p2*wei(2) end
