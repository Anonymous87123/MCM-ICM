# P-D-2024-2429211-de10f571

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
D

<!-- b000006 | title | pages [1] -->
2429211

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | prose | pages [1] -->
Dynamic Dams Model: A Multigranular, Human-Centered Approach For

<!-- b000009 | title | pages [1] -->
微信公众号：数学模型

<!-- b000010 | prose | pages [1] -->
Modeling Water In The Great Lakes

<!-- b000011 | heading | pages [1] -->
Summary

<!-- b000012 | prose | pages [1] -->
The Great Lakes serve as the heart of North America with their ebbs and flows providing the lifeblood of both the surrounding environment and societies. Because of the lake’s incredible importance, it is in the best interest of the world to protect them. Plan 2014, proposed by the International Joint Committee (ĲC), manages the water in the Great Lakes by building up water behind both the Compensating Works dam at the Sault St. Marie River and Moses-Saunders dam and taking action as needed. To better serve the Great Lakes region, we seek to expand Plan 2014 to regulate water levels optimizing for human needs and the preservation of ecosystems.

<!-- b000013 | title | pages [1] -->
微信号：MATHmodels

<!-- b000014 | prose | pages [1] -->
To determine optimal dam scheduling we modeled the Great Lakes as a dynamic flow network and created two control algorithms that utilize linear programming to solve for optimal dam schedules and water levels. The first control algorithm determines the optimal water level in each lake that is achievable through use of the Compensating Works and Moses-Saunders dams over the course of a multiple-month time horizon. After the optimal water levels have been determined, we employ another control algorithm to plan how to schedule the dams over a daily time horizon to achieve the water levels that equitably benefit stakeholders, but still adhere to the larger schedule. By utilizing these two control algorithms, it is possible to generate dam schedules that meet stakeholder needs while avoiding catastrophic events like flooding or dangerously low water levels.

<!-- b000015 | prose | pages [1] -->
An important aspect of our model is that it is mechanistic. Since we model real flows, it is important to determine accurate parameters to encode natural and artificial processes. However, the Great Lakes are a highly complex system, and they are influenced by several stochastic and highly volatile processes. To account for this complexity, we utilized a data-based approach to best coincide with the data that the ĲC will have access to. By utilizing time lagged cross-correlation, we were able to determine the relationship of flow rates between Great Lakes. We also utilized linear regression to model the relationship between the height of each Great Lake and the rate of flow in its distributaries. This allowed us to include necessary complexities while maintaining accurate and faithful parameters.

<!-- b000016 | prose | pages [1] -->
Our model provides a number of key insights into effective management of the Great Lakes. We observe that using adaptive control algorithms, it is possible to determine schedules that avoid flooding in most cases and allow the ĲC to be prepared when flooding is inevitable and to influence the location and time of the flood. Moreover, we observe that despite the large amount of time it takes for Lake Ontario to experience the effects of changes in Lake Superior, it is crucial to manage Lake Superior with the downstream effects on Lake Ontario in mind. When Lake Ontario faces a challenging climate event, effective scheduling at Lake Superior can mitigate the damage and allow Lake Ontario to maintain optimal water levels.

<!-- b000017 | keywords | pages [1] -->
Keywords: Linear Program; Dynamic Flow Network; Human-Centered; Multigranular Approach.

<!-- b000018 | furniture | pages [1] -->
关注数学模型

<!-- b000019 | furniture | pages [1] -->
2

<!-- b000020 | furniture | pages [1] -->
MATHmodels

<!-- b000021 | furniture | pages [1] -->
获取更多资讯

<!-- b000022 | furniture | pages [2] -->
Team # 2429211

<!-- b000023 | furniture | pages [2] -->
Page 2 of 24

<!-- b000024 | heading | pages [2] -->
Contents

<!-- b000025 | contents | pages [2] -->
微信公众号：数学模型

<!-- b000026 | contents | pages [2] -->
1

<!-- b000027 | heading | pages [2] -->
Introduction

<!-- b000028 | prose | pages [2] -->
3

<!-- b000029 | prose | pages [2] -->
Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 3

<!-- b000030 | prose | pages [2] -->
Restatement Of The Question . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 3

<!-- b000031 | prose | pages [2] -->
Overview of Linear Programs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3 4

<!-- b000032 | prose | pages [2] -->
Assumptions And Justifications . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.4

<!-- b000033 | prose | pages [2] -->
2

<!-- b000034 | heading | pages [2] -->
Macroschedule Model

<!-- b000035 | prose | pages [2] -->
5

<!-- b000036 | prose | pages [2] -->
6

<!-- b000037 | prose | pages [2] -->
Dynamic Network Formulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.1

<!-- b000038 | prose | pages [2] -->
2.2 Ideal Water Determination Algorithm

<!-- b000039 | prose | pages [2] -->
6

<!-- b000040 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000041 | prose | pages [2] -->
7

<!-- b000042 | prose | pages [2] -->
微信号：MATHmodels

<!-- b000043 | prose | pages [2] -->
Linear Program Formulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.3 7

<!-- b000044 | prose | pages [2] -->
Methods for Stakeholder Management . . . . . . . . . . . . . . . . . . . . . . . . 2.4 9

<!-- b000045 | prose | pages [2] -->
Data-Based Model Of The Hydrosphere . . . . . . . . . . . . . . . . . . . . . . . 2.5 10

<!-- b000046 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.6 Additional Considerations

<!-- b000047 | prose | pages [2] -->
3

<!-- b000048 | heading | pages [2] -->
Microschedule Model

<!-- b000049 | prose | pages [2] -->
4

<!-- b000050 | heading | pages [2] -->
Model Insights

<!-- b000051 | prose | pages [2] -->
12

<!-- b000052 | prose | pages [2] -->
12

<!-- b000053 | prose | pages [2] -->
13

<!-- b000054 | prose | pages [2] -->
Dynamic Control Of The System . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 14

<!-- b000055 | prose | pages [2] -->
Robustness to Severe Climate Events . . . . . . . . . . . . . . . . . . . . . . . . . 4.2

<!-- b000056 | prose | pages [2] -->
5

<!-- b000057 | heading | pages [2] -->
Sensitivity Analysis

<!-- b000058 | prose | pages [2] -->
6

<!-- b000059 | heading | pages [2] -->
Conclusions

<!-- b000060 | prose | pages [2] -->
15

<!-- b000061 | prose | pages [2] -->
16

<!-- b000062 | prose | pages [2] -->
17

<!-- b000063 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 Strengths 18

<!-- b000064 | prose | pages [2] -->
Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2

<!-- b000065 | prose | pages [2] -->
7 Future Exploration

<!-- b000066 | prose | pages [2] -->
8

<!-- b000067 | heading | pages [2] -->
Memo To The ĲC

<!-- b000068 | heading | pages [2] -->
A Notation

<!-- b000069 | prose | pages [2] -->
18

<!-- b000070 | prose | pages [2] -->
19

<!-- b000071 | prose | pages [2] -->
20

<!-- b000072 | prose | pages [2] -->
21

<!-- b000073 | furniture | pages [2] -->
关注数学模型

<!-- b000074 | furniture | pages [2] -->
2

<!-- b000075 | furniture | pages [2] -->
MATHmodels

<!-- b000076 | furniture | pages [2] -->
获取更多资讯

<!-- b000077 | furniture | pages [3] -->
Team # 2429211

<!-- b000078 | prose | pages [3] -->
1

<!-- b000079 | heading | pages [3] -->
Introduction

<!-- b000080 | prose | pages [3] -->
1.1

<!-- b000081 | heading | pages [3] -->
Background

<!-- b000082 | furniture | pages [3] -->
Page 3 of 24

<!-- b000083 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000084 | prose | pages [3] -->
The Great Lakes are one of the most promi- nent features of the North American continent; they not only make up 20 percent of the world’s freshwater, but they also have a tremendous im- pact on the economy, climate, and ecosystems of the United States and Canada. The Great Lakes region is one of the largest economies in the world, supporting 1.5 million people and forming the backbone for other industries which are valued at over 6 trillion dollars [8]. Addi- tionally, they also are the source of life for over 3500 species of plants and animals across a

<!-- b000085 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000086 | prose | pages [3] -->
wide range of biomes making them indispens- able to the North American ecosystems [18]. Due to the invaluable benefit that the Great Lakes provide us, it is of the utmost importance to society that they are flourishing in the best way possible.

<!-- b000087 | caption | pages [3] -->
Figure 1: A cloudless view of all of the Great

<!-- b000088 | prose | pages [3] -->
Lakes taken by a NASA satellite in August 2010 [13].

<!-- b000089 | prose | pages [3] -->
To ensure that the Great Lakes community is well-serviced, it is necessary to analyze the impacts on the stakeholders dependent on the lakes. The stakeholders identified in the report by the Inter- national Joint Committee (ĲC) are: domestic water supply, commercial navigation, hydropower, environment, recreational boaters, docking companies, and shoreline (riparian) property owners [10].

<!-- b000090 | prose | pages [3] -->
The current methodology of managing the water flow in Lake Ontario is based on Plan 2014. Plan 2014 prioritizes natural flow out of Lake Ontario into the St. Lawrence River while continually checking if a number of critical points have been reached. When a critical point has been reached, the ĲC takes action to control the level of water in the dam [2]. After the initiation of Plan 2014 in 2017, record precipitation hit the area and Lake Ontario experienced severe flooding [7]. This caused millions of dollars of damage and increased the risk for invasive species (like zebra mussels), harmful algae bloom, and sewage blockage [15] [19] [10]. This event brought the effectiveness of the plan under scrutiny. Flooding has proven to be a continual threat to the lives and livelihoods of the stakeholders. Thus, ICM has set out to formulate water level control mechanisms that could prevent such dire events.

<!-- b000091 | prose | pages [3] -->
1.2 Restatement Of The Question

<!-- b000092 | prose | pages [3] -->
To address the concerns of the ĲC, we propose a number of human-centered algorithms that control the water levels of the Great Lakes to best address the residents’ concerns around Lake Ontario and the St. Lawrence River. Our models and algorithms are fit to address the needs of various stakeholders, while ensuring that the water levels within the lakes remain safe. Motivated by the flooding damage from 2017, our model focuses on achieving water levels and currents that

<!-- b000093 | furniture | pages [3] -->
关注数学模型

<!-- b000094 | furniture | pages [3] -->
2

<!-- b000095 | furniture | pages [3] -->
MATHmodels

<!-- b000096 | furniture | pages [3] -->
获取更多资讯

<!-- b000097 | furniture | pages [4] -->
Team # 2429211

<!-- b000098 | furniture | pages [4] -->
Page 4 of 24

<!-- b000099 | prose | pages [4] -->
benefit the stakeholders subject to hard constraints on the risk of flooding and low-water levels. Our outlook differs significantly from that of Plan 2014 to be more resilient in a highly volatile climate. We propose using a linear program to model the needs of the stakeholders with respect to the water level and modulating it with dynamic control of dams that account for the transportation times of

<!-- b000100 | prose | pages [4] -->
微信公众号：数学模型

<!-- b000101 | prose | pages [4] -->
the water. Inspired by the successes of Plan 2014 as a method to solve a complex constrained scheduling problem and equipped with the knowledge of where Plan 2014 falls short, we propose a model that utilizes the Compensating Works dam at the Sault. St. Marie River as well as the Moses-Saunders dam to do the following:

<!-- b000102 | heading | pages [4] -->
1. Center the human impacts by modeling the needs of the stakeholders

<!-- b000103 | heading | pages [4] -->
2. Robustness to severe climate events

<!-- b000104 | heading | pages [4] -->
3. Dynamic control of the system

<!-- b000105 | prose | pages [4] -->
1.3 Overview of Linear Programs

<!-- b000106 | prose | pages [4] -->
微信号：MATHmodels

<!-- b000107 | prose | pages [4] -->
Our control algorithms are implemented as linear programs. Linear programming is a widely- used optimization technique in the field of operations research and network science. It has various applications from policymaking to power plant deployment to production logistics to watershed management [11, 20]. Linear programs rapidly found applications across the natural sciences, industry, government, and many other fields, and are a natural way to model many scheduling problems where it is important to understand how to plan a series of actions to maximize an objective (typically profit or some other measure of overall utility) subject to some constraints (e.g. there might only be so much time available to us) [21]. Within the realm of environmental decisions, linear programming has been applied to solve complex questions like green-energy planning [5]. Inspired by the success of linear programs in related fields, our control algorithms employ linear programming to determine how to utilize the dams within the Great Lakes. The advantages to be expected from utilizing linear programming are as follows:

<!-- b000108 | prose | pages [4] -->
• Algorithms for solving linear programs are widely available and extremely fast. Due to the effectiveness of the famous Simplex algorithm and its variants, linear programs can be solved with incredible speed which is advantageous for testing out a variety of weather scenarios.

<!-- b000109 | prose | pages [4] -->
• Linear programs are interpretable. Practitioners need access to a white-box control algo- rithm where it is possible to understand their decision.

<!-- b000110 | prose | pages [4] -->
• Linear programs are not defined with specific parameter values in mind. If practitioners need to revise their predictions for environmental factors, they can easily rerun the model with the adjusted parameters.

<!-- b000111 | prose | pages [4] -->
However, it’s also important to acknowledge the downsides that accompany linear programs:

<!-- b000112 | prose | pages [4] -->
• The objective and constraints must be linear. This limits the ways we can model our system considerably and, as such, it is important to recognize parts of the model that are remnants of the required linearity.

<!-- b000113 | furniture | pages [4] -->
关注数学模型

<!-- b000114 | furniture | pages [4] -->
2

<!-- b000115 | furniture | pages [4] -->
MATHmodels

<!-- b000116 | furniture | pages [4] -->
获取更多资讯

<!-- b000117 | furniture | pages [5] -->
Team # 2429211

<!-- b000118 | furniture | pages [5] -->
Page 5 of 24

<!-- b000119 | prose | pages [5] -->
• When a linear program is impossible to solve, it is difficult to visualize what is going wrong. If our control algorithms determine that there is no valid schedule that meets all constraints, it will be difficult for the practitioner to find a way to determine a valid schedule.

<!-- b000120 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000121 | prose | pages [5] -->
By keeping these disadvantages in mind, we designed our control algorithms to be effective even with the drawbacks of linear programming.

<!-- b000122 | prose | pages [5] -->
1.4

<!-- b000123 | heading | pages [5] -->
Assumptions And Justifications

<!-- b000124 | prose | pages [5] -->
As mentioned in the problem statement, the dynamic network flow problem is wicked. As such, we make use of several assumptions to manage the complexity of our models.

<!-- b000125 | prose | pages [5] -->
↓ i W

<!-- b000126 | prose | pages [5] -->
Hydrology: The lake’s sizes remain con-

<!-- b000127 | prose | pages [5] -->
stant and our system can be simplified

<!-- b000128 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000129 | caption | pages [5] -->
Figure 2: Since water levels do not vary

<!-- b000130 | prose | pages [5] -->
much relative to total depth, we can approxi- mate the lake surface area as being constant. We can then convert flow to marginal height by dividing by surface area.

<!-- b000131 | prose | pages [5] -->
to five nodes by not factoring in the auxiliaries like lake St. Claire.

<!-- b000132 | prose | pages [5] -->
Justification: Keeping the lake sizes con-

<!-- b000133 | prose | pages [5] -->
stant provides us with a consistent con- version metric, as seen in figure 2 be- tween flow and height for each lake. Based on the correlation data for the flow rates, the other nodes are negligi- ble as compared to the main outflows between the Great Lakes.

<!-- b000134 | prose | pages [5] -->
Systemic: Dams can be fully opened or closed within an hour and they have zero downtime.

<!-- b000135 | prose | pages [5] -->
Additionally, the lag times calculated from correlation data are accurate (Figure 2).

<!-- b000136 | prose | pages [5] -->
Justification: We want to encapsulate granular dam schedules to minimize flooding and drought of

<!-- b000137 | prose | pages [5] -->
the Great Lakes community. Also, we need the lag times to be accurate to simulate the water flowing between the lakes.

<!-- b000138 | prose | pages [5] -->
Scaling: The regressions we found for the flow rates from the lakes are linear (Figure 3) and the

<!-- b000139 | prose | pages [5] -->
time horizon of the data is on the order of a few months.

<!-- b000140 | prose | pages [5] -->
Justification: The regressions are done on the order of the change in height of the lakes, so the

<!-- b000141 | prose | pages [5] -->
flow rates for our purposes should be accurate. Since the time scale of our time lags is on the order of a few months, our time horizon encapsulates the lag time and our model should be used dynamically based on current data.

<!-- b000142 | furniture | pages [5] -->
关注数学模型

<!-- b000143 | furniture | pages [5] -->
2

<!-- b000144 | furniture | pages [5] -->
MATHmodels

<!-- b000145 | furniture | pages [5] -->
获取更多资讯

<!-- b000146 | furniture | pages [6] -->
Team # 2429211

<!-- b000147 | prose | pages [6] -->
2

<!-- b000148 | heading | pages [6] -->
Macroschedule Model

<!-- b000149 | furniture | pages [6] -->
Page 6 of 24

<!-- b000150 | prose | pages [6] -->
Here, we describe our algorithm for determining the optimal achievable water levels in the great lakes over a large time-period.

<!-- b000151 | prose | pages [6] -->
微信公众号：数学模型

<!-- b000152 | prose | pages [6] -->
2.1 Dynamic Network Formulation

<!-- b000153 | prose | pages [6] -->
We begin with a high-level overview of the model. The Great Lake water level problem can be studied as a dynamic network flow problem on the network shown in Figure 3. There are two arcs that we have some level of control over. The Sault St. Marie Dam allows us to send a constrained amount of water from Lake Superior to Lakes Huron and Michigan. Water then flows naturally from Lakes Huron and Michigan into Lake Erie and from Lake Erie to Lake Ontario. Through the Moses-Saunders Dam, we can let a constrained amount of water out of Lake Ontario into the St. Lawrence River.

<!-- b000154 | prose | pages [6] -->
The reason why our analysis differs from the well-studied static flow problem is because it takes time for water to flow between each node. For instance, it takes roughly one month for flows in

<!-- b000155 | prose | pages [6] -->
微信号：MATHmodels

<!-- b000156 | prose | pages [6] -->
Lake Superior to be observed in Lakes Huron and Michigan; it takes roughly three months to be observed in Lake Ontario. Thus, the network flow becomes dynamic–which significantly increases the problem’s modeling and computational difficulty.

<!-- b000157 | prose | pages [6] -->
Superior

<!-- b000158 | prose | pages [6] -->
𝑐1, 𝑡1

<!-- b000159 | prose | pages [6] -->
H.M

<!-- b000160 | prose | pages [6] -->
Erie Erie

<!-- b000161 | prose | pages [6] -->
𝑐2

<!-- b000162 | prose | pages [6] -->
Ontario St. Law

<!-- b000163 | caption | pages [6] -->
Figure 3: Network used in the model. 𝑐𝑖is the capacity of the arc and 𝑡𝑖is the transit time of the

<!-- b000164 | prose | pages [6] -->
arc. All unlabeled arcs correspond to uncontrolled flows of water.

<!-- b000165 | prose | pages [6] -->
More formally, the dynamic flow problem is defined over a network 𝑁= (𝑉, 𝐸, 𝜇, 𝜏,𝑉+,𝑉−). The vertex set is given by 𝑉∪𝑉+ ∪𝑉−where 𝑉+ represent source nodes, 𝑉−represent sink nodes, and 𝑉represent transit nodes. Each edge 𝐸𝑖has a corresponding capacity 𝜇𝑖𝑡and transit time 𝜏𝑖[6]. The goal is to find the min-cost flow over a fixed time horizon 𝑇that satisfies a particular objective.

<!-- b000166 | prose | pages [6] -->
To make this problem tractable, we employ Ford and Fulkerson’s time-expansion method to convert the problem into static flow [14]. We discretize the model over a fixed timestep, and we create copies of each node for each one over the entire time-horizon. We then assign edges based on the transit times between nodes. With this, the problem is now described by a network 𝑁◦= (𝑉, 𝐸, 𝜇,𝑉+,𝑉−). I.e. an augmented network that includes vertex copies but no transit times. This formulation is amenable to static-flow analysis.

<!-- b000167 | furniture | pages [6] -->
关注数学模型

<!-- b000168 | furniture | pages [6] -->
2

<!-- b000169 | furniture | pages [6] -->
MATHmodels

<!-- b000170 | furniture | pages [6] -->
获取更多资讯

<!-- b000171 | furniture | pages [7] -->
Team # 2429211

<!-- b000172 | furniture | pages [7] -->
Page 7 of 24

<!-- b000173 | heading | pages [7] -->
Ideal Water Determination Algorithm

<!-- b000174 | prose | pages [7] -->
2.2

<!-- b000175 | prose | pages [7] -->
To determine the ideal water levels for each body of water, we developed a utility function for each shareholder that determines their optimal water level based on the historical averages.

<!-- b000176 | prose | pages [7] -->
微信公众号：数学模型

<!-- b000177 | prose | pages [7] -->
This optimal water level is determined based on the fluctuations in the water level and what each of the stakeholders listed as their ideal scenario from the ĲC report. While navigation, docks, hydropower, and recreational boaters all prefer a fixed level of water, riparian owners, domestic water supply, and the environment prefer natural oscillations in water level [10]. To account for this discrepancy, we simulated sinusoidal oscillations about the mean height of the lake for their preferred timescales and amplitudes scaled compared to the natural processes:

<!-- b000178 | prose | pages [7] -->
Environment: The environment prefers natural annual water level oscillations to best align with

<!-- b000179 | prose | pages [7] -->
the natural mating seasons of species like wetland birds [12].

<!-- b000180 | prose | pages [7] -->
Domestic Water Supply: To preserve high water quality, the domestic water supply needs to

<!-- b000181 | prose | pages [7] -->
oscillate close to the average to prevent the inflow of sewage and harmful algae blooms

<!-- b000182 | prose | pages [7] -->
微信号：MATHmodels

<!-- b000183 | prose | pages [7] -->
[15][10].

<!-- b000184 | prose | pages [7] -->
Riparian Owners: The riparian owners prefer lower water levels with smaller amplitude os-

<!-- b000185 | prose | pages [7] -->
cillations, with higher frequency to increase the amount of sand re-deposition and dune replenishment [10].

<!-- b000186 | prose | pages [7] -->
Navigation: Navigation prefers steadily high water levels because lower water levels can increase

<!-- b000187 | prose | pages [7] -->
costs by 30 percent and double emissions in the Great Lakes [16]. Additionally, they want it to not flood because they need ships to get through [10].

<!-- b000188 | prose | pages [7] -->
Hydropower: The dams prefer their flow rates to be constant or near their ideal operating range of

<!-- b000189 | prose | pages [7] -->
around 7, 000𝑚3

<!-- b000190 | prose | pages [7] -->
𝑠, so they prefer to be above the average water levels, similar to navigation, to maintain that [9].

<!-- b000191 | prose | pages [7] -->
Boaters: Boaters also prefer to be in a similar range of slightly above the average water level to

<!-- b000192 | prose | pages [7] -->
improve the speed they can travel through the water during the day [10].

<!-- b000193 | prose | pages [7] -->
Docks: For the shipping ports in Montreal, they prefer to have constant low water levels so the

<!-- b000194 | prose | pages [7] -->
amount of the ideal amount of water coming downstream from the Moses-Saunders Dam should be minimized during working hours.

<!-- b000195 | prose | pages [7] -->
There are conflicting interests among the stakeholders, and it is impossible to please each stakeholder. To account for this, we introduced a weighting system into our model to allow each stakeholder to be considered with different severity. As a result, our ideal water plots look like

<!-- b000196 | caption | pages [7] -->
figure 4 compared to the historical data

<!-- b000197 | prose | pages [7] -->
2.3 Linear Program Formulation

<!-- b000198 | prose | pages [7] -->
Here we describe the Linear Program (LP) we propose to determine long-term dam schedules for the Great Lakes. We consider two sets that our decision variables and parameters belong to: (1) Bodies of Water and (2) Time. Our decision variables are the amount of water we let flow from the

<!-- b000199 | furniture | pages [7] -->
关注数学模型

<!-- b000200 | furniture | pages [7] -->
2

<!-- b000201 | furniture | pages [7] -->
MATHmodels

<!-- b000202 | furniture | pages [7] -->
获取更多资讯

<!-- b000203 | furniture | pages [8] -->
Team # 2429211

<!-- b000204 | prose | pages [8] -->
Lake Superior ideal water level curve

<!-- b000205 | prose | pages [8] -->
Ideal Historic

<!-- b000206 | prose | pages [8] -->
183.45

<!-- b000207 | furniture | pages [8] -->
Page 8 of 24

<!-- b000208 | prose | pages [8] -->
Lake Ontario ideal water level curve

<!-- b000209 | prose | pages [8] -->
Ideal

<!-- b000210 | prose | pages [8] -->
75.1

<!-- b000211 | prose | pages [8] -->
Historic

<!-- b000212 | prose | pages [8] -->
微信公众号：数学模型

<!-- b000213 | prose | pages [8] -->
183.40

<!-- b000214 | prose | pages [8] -->
Water level (m)

<!-- b000215 | prose | pages [8] -->
183.35

<!-- b000216 | prose | pages [8] -->
183.30

<!-- b000217 | prose | pages [8] -->
183.25

<!-- b000218 | prose | pages [8] -->
183.20

<!-- b000219 | prose | pages [8] -->
0 50 100 150 200 250 300 350 Day of year

<!-- b000220 | prose | pages [8] -->
75.0

<!-- b000221 | prose | pages [8] -->
Water level (m)

<!-- b000222 | prose | pages [8] -->
74.9

<!-- b000223 | prose | pages [8] -->
74.8

<!-- b000224 | prose | pages [8] -->
74.7

<!-- b000225 | prose | pages [8] -->
74.6

<!-- b000226 | prose | pages [8] -->
0 50 100 150 200 250 300 350 Day of year

<!-- b000227 | caption | pages [8] -->
Figure 4: Plot of the ideal water levels (solid orange lines) based on stakeholder needs for Lake

<!-- b000228 | prose | pages [8] -->
Superior and Lake Ontario compared to the historical averages (dotted blue lines) from the dataset.

<!-- b000229 | prose | pages [8] -->
微信号：MATHmodels

<!-- b000230 | prose | pages [8] -->
Superior to the St. Mary River at each time-step and the amount of water we let flow from Lake Ontario to the St. Lawrence River1. The objective of the LP is to minimize the absolute difference between the achieved water level and the “ideal” water level. The LP is constrained by limits on the water level ensuring no flooding occurs and the water level is never critically low. The variables and parameters and described in the first table in Appendix A. The algebraic form of the linear program is shown below:

<!-- b000231 | prose | pages [8] -->
∑︁

<!-- b000232 | prose | pages [8] -->
𝜔𝑖|ℎ𝑖,𝑡−ˆℎ𝑖,𝑡| + (1 −

<!-- b000233 | prose | pages [8] -->
minimize

<!-- b000234 | prose | pages [8] -->
𝑖∈𝐵,𝑡∈𝑇

<!-- b000235 | prose | pages [8] -->
ℎ1,𝑡= ℎ1,𝑡−1 −𝑥𝑡−1 + 𝑟1,𝑡−1 subject to

<!-- b000236 | prose | pages [8] -->
∑︁

<!-- b000237 | prose | pages [8] -->
∑︁

<!-- b000238 | prose | pages [8] -->
| 𝑓𝑡−ˆ𝑓𝑡|

<!-- b000239 | prose | pages [8] -->
𝜔𝑖)

<!-- b000240 | prose | pages [8] -->
𝑖∈𝐵

<!-- b000241 | prose | pages [8] -->
𝑡∈𝑇

<!-- b000242 | prose | pages [8] -->
∀𝑡∈[1,𝑇]

<!-- b000243 | prose | pages [8] -->
𝑠2𝑥𝑡−𝐿−(𝛼2ℎ2,𝑡−1+𝛽2)

<!-- b000244 | prose | pages [8] -->
ℎ2,𝑡= ℎ2,𝑡−1 + 𝑠1

<!-- b000245 | prose | pages [8] -->
ℎ3,𝑡= ℎ3,𝑡−1 + (𝛼2ℎ2,𝑡−𝐿+𝛽2)

<!-- b000246 | prose | pages [8] -->
𝑠3

<!-- b000247 | prose | pages [8] -->
ℎ4,𝑡= ℎ4,𝑡−1 + (𝛼3ℎ3,𝑡−1+𝛽3)

<!-- b000248 | prose | pages [8] -->
+ 𝑟2,𝑡−1 ∀𝑡∈[1,𝑇] 𝑠2

<!-- b000249 | prose | pages [8] -->
−(𝛼3ℎ3,𝑡−1+𝛽3)

<!-- b000250 | prose | pages [8] -->
+ 𝑟3,𝑡−1 ∀𝑡∈[1,𝑇] 𝑠3

<!-- b000251 | prose | pages [8] -->
−𝑦𝑡−1 + 𝑟4,𝑡−1 𝑠4

<!-- b000252 | prose | pages [8] -->
ℎ𝑖,𝑡≤𝐹𝑖

<!-- b000253 | prose | pages [8] -->
ℎ𝑖,𝑡≥𝐷𝑖

<!-- b000254 | prose | pages [8] -->
𝑥𝑡≤𝑀1

<!-- b000255 | prose | pages [8] -->
𝑦𝑡≤𝑀2

<!-- b000256 | prose | pages [8] -->
𝑓𝑡= 𝑤𝑓𝑡−1 + (1 −𝑤)𝑦𝑡

<!-- b000257 | prose | pages [8] -->
∀𝑡∈[1,𝑇]

<!-- b000258 | prose | pages [8] -->
∀𝑖∈𝐵, 𝑡∈[1,𝑇]

<!-- b000259 | prose | pages [8] -->
∀𝑖∈𝐵, 𝑡∈[1,𝑇]

<!-- b000260 | prose | pages [8] -->
∀𝑡∈[1,𝑇]

<!-- b000261 | prose | pages [8] -->
∀𝑡∈[1,𝑇]

<!-- b000262 | prose | pages [8] -->
∀𝑡∈[1,𝑇]

<!-- b000263 | prose | pages [8] -->
1In Appendix A, more variables are listed, but these are completely determined by equality constraints and are thus not listed as decision variables here.

<!-- b000264 | furniture | pages [8] -->
关注数学模型

<!-- b000265 | furniture | pages [8] -->
2

<!-- b000266 | furniture | pages [8] -->
MATHmodels

<!-- b000267 | furniture | pages [8] -->
获取更多资讯

<!-- b000268 | furniture | pages [9] -->
Team # 2429211

<!-- b000269 | furniture | pages [9] -->
Page 9 of 24

<!-- b000270 | prose | pages [9] -->
All decision variables are nonnegative. The first four constraints capture how the height of water in each lake changes over time by tracking how much water enters the lake and how much leaves. We use the index 𝑥𝑡−𝐿to capture the fact that there is a lag between the changes in Lake Superior and the changes at other lakes. The 5th and 6th constraints allow us to ensure that no

<!-- b000271 | prose | pages [9] -->
微信公众号：数学模型

<!-- b000272 | prose | pages [9] -->
flooding or dangerously-low water levels occur. To capture the fact that dams can only let out so much water at a time, we introduce the 7th and 8th constraints to bound the amount of water we can let out of the dams. Lastly, we track the flow in the St. Lawrence River with the 9th constraint.

<!-- b000273 | prose | pages [9] -->
Methods for Stakeholder Management 2.4

<!-- b000274 | prose | pages [9] -->
As ĲC notes, this problem is particularly difficult because of the often-conflicting requests from the various stakeholders around the Lake Ontario and St. Lawrence River regions. Our algorithm provides a method to weight stakeholder interests, however, it relies on the practitioner to assign these weights manually. This has the potential to create divides between groups of stakeholders. Thus, some sort of heuristic should be used to equitably assign these weights on a per-stakeholder basis.

<!-- b000275 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000276 | prose | pages [9] -->
We propose the following methodology to determine fair weightings between ideal water level curves:

<!-- b000277 | prose | pages [9] -->
• We create an initial set of weights 𝑤0 and set them as parameters in the model.

<!-- b000278 | prose | pages [9] -->
• Then we simulate roughly five months2, and observe the forecasted ideal water levels.

<!-- b000279 | prose | pages [9] -->
• We then proceed with the schedule for two months.

<!-- b000280 | prose | pages [9] -->
We simulate beyond the necessary time horizon to ensure that our model accounts for future impacts of flows in the other lakes. In particular, we designate a three-month buffer since this is the time taken for an effect in Lake Superior to be observed in Lake Ontario.

<!-- b000281 | prose | pages [9] -->
After adopting the given schedule for the two month period, we calculate the net error between the real observed water levels and the ideal curves provided per stakeholder.

<!-- b000282 | prose | pages [9] -->
∑︁

<!-- b000283 | prose | pages [9] -->
|ℎ𝑡−ˆℎ𝑡|

<!-- b000284 | prose | pages [9] -->
𝜀𝑖=

<!-- b000285 | prose | pages [9] -->
𝑡

<!-- b000286 | prose | pages [9] -->
𝑡∈[1, 60]

<!-- b000287 | prose | pages [9] -->
This gives us per-stakeholder errors {𝜀1, . . . 𝜀𝑛} for 𝑛stakeholders. Note that higher values of 𝜀𝑖correspond to a lower level of stakholder 𝑖’s satisfaction. Keeping this in mind, we can reassign weights for the next time horizon with

<!-- b000288 | prose | pages [9] -->
𝑤1𝑖= 𝜀𝑖

<!-- b000289 | prose | pages [9] -->
𝑘𝜀𝑘

<!-- b000290 | prose | pages [9] -->
Í

<!-- b000291 | prose | pages [9] -->
That is, the new stakeholder weights are their normalized net errors from the last time period. This allows stakeholders that had greater deviations to be prioritized during the next time period.

<!-- b000292 | prose | pages [9] -->
2The chosen time horizon is left up to the practitioner, but we recommend choosing one of the same order. I.e. 2-6 months

<!-- b000293 | furniture | pages [9] -->
关注数学模型

<!-- b000294 | furniture | pages [9] -->
2

<!-- b000295 | furniture | pages [9] -->
MATHmodels

<!-- b000296 | furniture | pages [9] -->
获取更多资讯

<!-- b000297 | furniture | pages [10] -->
Team # 2429211

<!-- b000298 | furniture | pages [10] -->
Page 10 of 24

<!-- b000299 | heading | pages [10] -->
Data-Based Model Of The Hydrosphere

<!-- b000300 | prose | pages [10] -->
2.5

<!-- b000301 | prose | pages [10] -->
Modeling the movement of water in the Great Lakes is difficult and requires a number of assumptions to make the problem tractable. To ground our model in reality we used a data-based

<!-- b000302 | prose | pages [10] -->
微信公众号：数学模型

<!-- b000303 | prose | pages [10] -->
approach to determine time lag, flow rates out of lakes, and other sources of water outside of the flow between the lakes.

<!-- b000304 | prose | pages [10] -->
We first needed to approximate the time lags between the lakes for our LP to create dam schedules. For instance, we needed to know that it takes roughly two months for the effect of a flow in Lake Michigan to be observed in Lake Ontario. To identify the latencies, we used time-lagged cross correlation on the provided water level time series to find where the correlation is maximized. For example, the time-lagged cross-correlation between the water levels in Lake Superior and Lake Michigan is given by Figure 5.

<!-- b000305 | prose | pages [10] -->
Time lagged cross-correlation between Lake Huron and Lake Erie

<!-- b000306 | furniture | pages [10] -->


<!-- b000307 | prose | pages [10] -->
0.90

<!-- b000308 | prose | pages [10] -->
Time lagged cross-correlation between Lake Erie and Lake Ontario

<!-- b000309 | prose | pages [10] -->
0.7

<!-- b000310 | prose | pages [10] -->
微信号：MATHmodels

<!-- b000311 | prose | pages [10] -->
0.85

<!-- b000312 | prose | pages [10] -->
Correlation

<!-- b000313 | prose | pages [10] -->
0.80

<!-- b000314 | prose | pages [10] -->
0.75

<!-- b000315 | prose | pages [10] -->
0.70

<!-- b000316 | prose | pages [10] -->
0.65

<!-- b000317 | prose | pages [10] -->
0 −10 −5 5 10 Time lag (months)

<!-- b000318 | prose | pages [10] -->
0.6

<!-- b000319 | prose | pages [10] -->
0.5

<!-- b000320 | prose | pages [10] -->
Correlation

<!-- b000321 | prose | pages [10] -->
0.4

<!-- b000322 | prose | pages [10] -->
0.3

<!-- b000323 | prose | pages [10] -->
0.2

<!-- b000324 | prose | pages [10] -->
0.1

<!-- b000325 | prose | pages [10] -->
0.0

<!-- b000326 | prose | pages [10] -->
−0.1

<!-- b000327 | prose | pages [10] -->
0 −10 −5 5 10 Time lag (months)

<!-- b000328 | caption | pages [10] -->
Figure 5: Time lagged cross-correlation examples for between Lake Huron and Erie and between

<!-- b000329 | prose | pages [10] -->
Lake Erie and Ontario computed from the dataset given for Problem D in [1].

<!-- b000330 | prose | pages [10] -->
The correlation is maximized at a time lag of 1. Thus, we can interpret that a flow in Lake Superior will take approximately a month to propagate in Lake Michigan. The full matrix of these time-lagged correlations is given by Table 1.

<!-- b000331 | prose | pages [10] -->
Sup. Sup.

<!-- b000332 | prose | pages [10] -->
0 Mich. + Huron -1 Erie -3 Ont.

<!-- b000333 | prose | pages [10] -->
-3 Mich + Huron Erie Ont. 1 3 3 0 1 2 -2 0 0 -2 0 0

<!-- b000334 | caption | pages [10] -->
Table 1: Time lag matrix between the Great Lakes

<!-- b000335 | prose | pages [10] -->
Additionally, we used the datasets to run a linear regression, pictured in figure 6, to obtain the flow rates as a function of the height of the lake, which we will use to model the flow in and out of the lakes. We suspect this to be true because if we approximate flow using Bernoulli’s principle in fluid mechanics, we find that by expanding for small oscillations we will have locally linear results.

<!-- b000336 | furniture | pages [10] -->
关注数学模型

<!-- b000337 | furniture | pages [10] -->
2

<!-- b000338 | furniture | pages [10] -->
MATHmodels

<!-- b000339 | furniture | pages [10] -->
获取更多资讯

<!-- b000340 | furniture | pages [11] -->
Team # 2429211

<!-- b000341 | prose | pages [11] -->
Niagara Riverflow vs Lake Erie height

<!-- b000342 | prose | pages [11] -->
8000

<!-- b000343 | prose | pages [11] -->
7500

<!-- b000344 | furniture | pages [11] -->
Page 11 of 24

<!-- b000345 | prose | pages [11] -->
Detroit River ﬂow vs Lake Michigan/Huron height

<!-- b000346 | prose | pages [11] -->
7500

<!-- b000347 | prose | pages [11] -->
微信公众号：数学模型

<!-- b000348 | prose | pages [11] -->
3s−1)

<!-- b000349 | prose | pages [11] -->
7000

<!-- b000350 | prose | pages [11] -->
Niagara river ﬂow ( m

<!-- b000351 | prose | pages [11] -->
6500

<!-- b000352 | prose | pages [11] -->
6000

<!-- b000353 | prose | pages [11] -->
5500

<!-- b000354 | prose | pages [11] -->
5000

<!-- b000355 | prose | pages [11] -->
173.8 174.0 174.2 174.4 174.6 174.8 175.0 175.2 Lake Erie height ( m )

<!-- b000356 | prose | pages [11] -->
7000

<!-- b000357 | prose | pages [11] -->
Detroit River ﬂow (m3s−1)

<!-- b000358 | prose | pages [11] -->
6500

<!-- b000359 | prose | pages [11] -->
6000

<!-- b000360 | prose | pages [11] -->
5500

<!-- b000361 | prose | pages [11] -->
5000

<!-- b000362 | prose | pages [11] -->
4500

<!-- b000363 | prose | pages [11] -->
4000

<!-- b000364 | prose | pages [11] -->
175.50 175.75 176.00 176.25 176.50 176.75 177.00 177.25 177.50 Lake Michigan/Huron height (m)

<!-- b000365 | caption | pages [11] -->
Figure 6: Flow along the Niagara River and Detroit River as a function of the height (relative to

<!-- b000366 | prose | pages [11] -->
微信号：MATHmodels

<!-- b000367 | prose | pages [11] -->
sea level) of the lakes they flow from. The regression formulae are given by:

<!-- b000368 | prose | pages [11] -->
𝑓Niagara = 2088.917ℎErie −357993.824 with (R2 = 0.928) 𝑓Detroit = 1611.581ℎHuron −278618.674 with (R2 = 0.850)

<!-- b000369 | prose | pages [11] -->
Lastly, we also approximated other aspects of the hydrosphere (precipitation, groundwater, evaporation, and surface runoff) by modeling the inflow of water based on how much it rained because according to the biohydrological database for the Great Lakes makes up 20 percent of the water flowing into the Great Lakes [3]. Using the NOAA data set of rainfall, evaporation, and runoff into the Great Lakes [17], we determined the total inflow that would occur each month based on historical data. We visualize the historical rainfall that occurred during each month in Figure 7.

<!-- b000370 | prose | pages [11] -->
Lake Superior net exogenous ﬂow

<!-- b000371 | prose | pages [11] -->
25p 50p 75p

<!-- b000372 | prose | pages [11] -->
0.15

<!-- b000373 | prose | pages [11] -->
Marginal height (m)

<!-- b000374 | prose | pages [11] -->
0.10

<!-- b000375 | prose | pages [11] -->
0.05

<!-- b000376 | prose | pages [11] -->
0.00

<!-- b000377 | prose | pages [11] -->
−0.05

<!-- b000378 | prose | pages [11] -->
Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec Month

<!-- b000379 | prose | pages [11] -->
Lake Ontario net exogenous ﬂow

<!-- b000380 | prose | pages [11] -->
25p 50p 75p

<!-- b000381 | prose | pages [11] -->
0.4

<!-- b000382 | prose | pages [11] -->
Marginal height (m) Marginal height (m)

<!-- b000383 | prose | pages [11] -->
0.3

<!-- b000384 | prose | pages [11] -->
0.2

<!-- b000385 | prose | pages [11] -->
0.1

<!-- b000386 | prose | pages [11] -->
Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec Month

<!-- b000387 | caption | pages [11] -->
Figure 7: 1st (in blue), 2nd (in red), and 3rd (in orange) quartiles of exogenous flow into Lakes

<!-- b000388 | prose | pages [11] -->
Superior and Ontario

<!-- b000389 | furniture | pages [11] -->
关注数学模型

<!-- b000390 | furniture | pages [11] -->
2

<!-- b000391 | furniture | pages [11] -->
MATHmodels

<!-- b000392 | furniture | pages [11] -->
获取更多资讯

<!-- b000393 | furniture | pages [12] -->
Team # 2429211

<!-- b000394 | prose | pages [12] -->
2.6 Additional Considerations

<!-- b000395 | furniture | pages [12] -->
Page 12 of 24

<!-- b000396 | prose | pages [12] -->
Aside from the data-driven parameters we obtained, we considered other parameters to help make our model more realistic:

<!-- b000397 | prose | pages [12] -->
微信公众号：数学模型

<!-- b000398 | prose | pages [12] -->
Seasonal Wave Attenuation: To consider the seasonality of the Great Lakes we also add an

<!-- b000399 | prose | pages [12] -->
attenuation factor that reduces the flow between the lakes. We added this factor because a study by Peng Bai showed that ice attenuates the waves in the Great Lakes and thus should reduce their flow from their turbulent effects [4].

<!-- b000400 | prose | pages [12] -->
Fuzzing The Model: Since exogenous inflow is highly random, we added noise to historical inflow

<!-- b000401 | prose | pages [12] -->
data to increase the robustness of our model. This makes the model more robust by removing biases towards certain shores at different water levels and helps us accurately assess the drought and flooding risk factors.

<!-- b000402 | prose | pages [12] -->
3

<!-- b000403 | heading | pages [12] -->
Microschedule Model

<!-- b000404 | prose | pages [12] -->
微信号：MATHmodels

<!-- b000405 | prose | pages [12] -->
One aspect that our Macroschedule model does not incorporate are the proximal effects of opening the Moses-Saunders Dam. As noted by the problem statement, even small variances in the water level can have drastic implications for stakeholders around Lake Ontario and the St. Lawrence River. As such, it is not enough to know how to release water in a day. It is also important to time outflows when it is generally most beneficial for these stakeholders. We develop a linear program that schedules intra-day outflows to maximize community benefit.

<!-- b000406 | prose | pages [12] -->
Unlike the macroscheduling problem, there is no substantial time lag on flows between nodes in the microscheduling problem. Thus, we can exert more immediate control over the water level and flows in Lake Ontario and the St. Lawrence River. We use a similarly formulated linear program to represent these flows, and the objective of maximizing proximity to ideal water levels and flows. The variables of the problems are defined in the second table of Appendix A

<!-- b000407 | prose | pages [12] -->
And the LP is formulated as follows:

<!-- b000408 | prose | pages [12] -->
∑︁

<!-- b000409 | prose | pages [12] -->
𝛼1|ℎ𝑡−ˆℎ𝑡| + 𝛼2| 𝑓𝑡−ˆ𝑓𝑡|

<!-- b000410 | prose | pages [12] -->
minimize

<!-- b000411 | prose | pages [12] -->
𝑡∈𝑇

<!-- b000412 | prose | pages [12] -->
ℎ𝑡= ℎ𝑡−1 + 𝐹𝑡−𝑥𝑡 subject to ∀𝑡∈𝑇 𝑓𝑡= 𝜔𝑓𝑡−1 + 𝑘(1 −𝜔)𝑥𝑡 𝑥𝑡≤𝑂 ℎ𝑇= ˆ𝐻 ∀𝑡∈𝑇 ∀𝑡∈𝑇

<!-- b000413 | prose | pages [12] -->
The first two constraints implement height and flow rate updates in Lake Ontario and the St. Lawrence river respectively. Notice that the second constraint models the river flow rate as a convex combination of inflow from the dam and its prior flow rate. This is influenced by sound physical intuition, but it is difficult to accurately model this parameter based on available data. The third constraint limits total outflow from the dam, and the fourth enforces that a certain amount of water has left Lake Ontario by the end of the day. This ensures that the microscheduler adheres to the daily requirements set forth by the larger schedule. Our proposed synthesis of the macroscheduler and microscheduler is show in Figure 8

<!-- b000414 | furniture | pages [12] -->
关注数学模型

<!-- b000415 | furniture | pages [12] -->
2

<!-- b000416 | furniture | pages [12] -->
MATHmodels

<!-- b000417 | furniture | pages [12] -->
获取更多资讯

<!-- b000418 | furniture | pages [13] -->
Team # 2429211

<!-- b000419 | furniture | pages [13] -->
Page 13 of 24

<!-- b000420 | prose | pages [13] -->
Due to lower lag times, the model cansatisfy daily requirements relatively well. This is important because there are likely days when dam usage must be limited to coordinate with monthly schedules. However, the water level can still be modulated to a level where stakeholders can still be largely satisfied.

<!-- b000421 | prose | pages [13] -->
微信公众号：数学模型

<!-- b000422 | prose | pages [13] -->
Set Time Horizon

<!-- b000423 | prose | pages [13] -->
Macroscheduler

<!-- b000424 | prose | pages [13] -->
Manage Stakeholder

<!-- b000425 | prose | pages [13] -->
Expectations

<!-- b000426 | prose | pages [13] -->
Microscheduler

<!-- b000427 | prose | pages [13] -->
Find Ideal Curves

<!-- b000428 | prose | pages [13] -->
微信号：MATHmodels

<!-- b000429 | prose | pages [13] -->
Fit Macro

<!-- b000430 | prose | pages [13] -->
Approve

<!-- b000431 | prose | pages [13] -->
Parameters

<!-- b000432 | prose | pages [13] -->
Test & Determine Generate Schedule

<!-- b000433 | prose | pages [13] -->
Robustness

<!-- b000434 | prose | pages [13] -->
Collect Data

<!-- b000435 | prose | pages [13] -->
Fit Micro Parameters

<!-- b000436 | prose | pages [13] -->
Generate Schedule

<!-- b000437 | prose | pages [13] -->
Improve Model

<!-- b000438 | caption | pages [13] -->
Figure 8: The pipeline for using our control algorithms.

<!-- b000439 | prose | pages [13] -->
4

<!-- b000440 | heading | pages [13] -->
Model Insights

<!-- b000441 | prose | pages [13] -->
Here we outline a brief overview of the main insights of our model:

<!-- b000442 | prose | pages [13] -->
• Effectively managing Lake Ontario means effectively Managing Lake Superior. Lake Supe- rior is able to influence Lake Ontario after a significant time delay which makes proactive scheduling at Lake Superior able to create desirable water levels at Lake Ontario.

<!-- b000443 | prose | pages [13] -->
• Our model successfully achieves the desired water levels in most lakes even with varying degrees of rainfall.

<!-- b000444 | prose | pages [13] -->
• After determining optimal water levels through our macro-schedule algorithm, our micro- schedule algorithm is able to determine realistic and effective schedules for scheduling a dam during any particular day.

<!-- b000445 | furniture | pages [13] -->
关注数学模型

<!-- b000446 | furniture | pages [13] -->
2

<!-- b000447 | furniture | pages [13] -->
MATHmodels

<!-- b000448 | furniture | pages [13] -->
获取更多资讯

<!-- b000449 | furniture | pages [14] -->
Team # 2429211

<!-- b000450 | prose | pages [14] -->
4.1 Dynamic Control Of The System

<!-- b000451 | furniture | pages [14] -->
Page 14 of 24

<!-- b000452 | prose | pages [14] -->
Most dams use a heuristic approach for dam scheduling called rule curves. That is, dams are given fixed schedules depending on water level and precipitation thresholds. While our model is

<!-- b000453 | prose | pages [14] -->
微信公众号：数学模型

<!-- b000454 | prose | pages [14] -->
amenable to producting rule curves, we believe that the dynamic nature of scheduling makes it superior to this approach.

<!-- b000455 | prose | pages [14] -->
One of the most critical aspects of the model is that it can make decisions by “looking ahead”. That is, given a range of forecasts, the model can schedule flows that are both robust to climate events and still satisfy the needs of stakeholders. This way, action can be taken to mitigate potential crises well before they actually occur.

<!-- b000456 | prose | pages [14] -->
After we “look ahead” we can then use a combination of the macroscheduler and microscheduler model to forecast both the four-month time horizon and then locally on the daily horizon. By modeling both of these time horizons, we gain valuable insights on the importance of factoring in the time lags to forecasting the dam schedules. The efficacy of our model is shown in Figure 9:

<!-- b000457 | prose | pages [14] -->
微信号：MATHmodels

<!-- b000458 | prose | pages [14] -->
Microscheduler ﬂow error rate

<!-- b000459 | prose | pages [14] -->
1.4

<!-- b000460 | prose | pages [14] -->
1.2

<!-- b000461 | prose | pages [14] -->
1.0

<!-- b000462 | prose | pages [14] -->
Error (%)

<!-- b000463 | prose | pages [14] -->
0.8

<!-- b000464 | prose | pages [14] -->
0.6

<!-- b000465 | prose | pages [14] -->
0.4

<!-- b000466 | prose | pages [14] -->
0.2

<!-- b000467 | prose | pages [14] -->
0.0

<!-- b000468 | prose | pages [14] -->
0 5 10 15 20 Hour

<!-- b000469 | caption | pages [14] -->
Figure 9: Plot of the percent error between ideal flow and the flow achieved by the microscheduler

<!-- b000470 | prose | pages [14] -->
after the optimal water levels were determined by the macroscheduling algorithm.

<!-- b000471 | furniture | pages [14] -->
关注数学模型

<!-- b000472 | furniture | pages [14] -->
2

<!-- b000473 | furniture | pages [14] -->
MATHmodels

<!-- b000474 | furniture | pages [14] -->
获取更多资讯

<!-- b000475 | furniture | pages [15] -->
Team # 2429211

<!-- b000476 | furniture | pages [15] -->
Page 15 of 24

<!-- b000477 | prose | pages [15] -->
Robustness to Severe Climate Events 4.2

<!-- b000478 | prose | pages [15] -->
We tested the schedules produced by our control algorithm using past rain/runoff/evap-

<!-- b000479 | prose | pages [15] -->
Quartile 1

<!-- b000480 | prose | pages [15] -->
微信公众号：数学模型

<!-- b000481 | prose | pages [15] -->
oration data collected from [17].

<!-- b000482 | prose | pages [15] -->
We deter- mined the average amount of total rain, runoff, and evaporation for each month from 1980 to 2020.

<!-- b000483 | prose | pages [15] -->
Due to the fact that our model uses a time-step of one day and the data available form [17] tracks how much rain/runoff/evap- oration occurred each month, we determined how much it rained per day by running a cu- bic spline through the historical averages and then dividing the value for total rain, runoff, and evaporation by 30 to account for the fact that the month data was the total over a month

<!-- b000484 | prose | pages [15] -->
Superior

<!-- b000485 | prose | pages [15] -->
Huron/Michigan 176.5

<!-- b000486 | prose | pages [15] -->
183.4

<!-- b000487 | prose | pages [15] -->
176.4

<!-- b000488 | prose | pages [15] -->
Water Height

<!-- b000489 | prose | pages [15] -->
176.3

<!-- b000490 | prose | pages [15] -->
183.2

<!-- b000491 | prose | pages [15] -->
176.2

<!-- b000492 | prose | pages [15] -->
183.0

<!-- b000493 | prose | pages [15] -->
176.1

<!-- b000494 | prose | pages [15] -->
176.0

<!-- b000495 | prose | pages [15] -->
182.8

<!-- b000496 | prose | pages [15] -->
175.9

<!-- b000497 | prose | pages [15] -->
175.8

<!-- b000498 | prose | pages [15] -->
182.6

<!-- b000499 | prose | pages [15] -->
175.7

<!-- b000500 | prose | pages [15] -->
Ontario Erie

<!-- b000501 | prose | pages [15] -->
174.5

<!-- b000502 | prose | pages [15] -->
75.0

<!-- b000503 | prose | pages [15] -->
174.4

<!-- b000504 | prose | pages [15] -->
Water Height

<!-- b000505 | prose | pages [15] -->
74.8

<!-- b000506 | prose | pages [15] -->
174.3

<!-- b000507 | prose | pages [15] -->
74.6

<!-- b000508 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000509 | prose | pages [15] -->
(roughly 30 days). This allows us to capture the natural patterns of rain, runoff, and evaporation while making the data usable in our model. We ran a similar procedure to determine the 25th and 75th percentile amount of rain, runoff, and evaporation that occurred on each day.

<!-- b000510 | prose | pages [15] -->
After obtaining these rain values, we ran our linear program using the historic rain level (ei- ther the 25th, 50th or 75th percentile) at body of water 𝑖during time 𝑡for the 𝑟𝑖,𝑡parameter. The time horizon for these experiments was set to a year and the ideal water was determined using the techniques in Section 2.2. The water levels achieved by the model are shown in Figures 10 and 11.

<!-- b000511 | prose | pages [15] -->
We observe that the Lake Ontario water lev- els are very consistent across different levels of total rain, runoff, and evaporation while Lake Superior’s levels are not.

<!-- b000512 | prose | pages [15] -->
This demonstrates that effectively scheduling Lake Superior is cru- cial to having desirable water levels at Lake On- tario. The types of schedules that are required in Lake Superior to create desirable water levels at Lake Ontario are non-robust to severe changes in total inflow to the Great Lakes, but the water levels in the rest of the Great Lakes are indeed robust to climate events.

<!-- b000513 | prose | pages [15] -->
174.2

<!-- b000514 | prose | pages [15] -->
74.4

<!-- b000515 | prose | pages [15] -->
174.1

<!-- b000516 | prose | pages [15] -->
74.2

<!-- b000517 | prose | pages [15] -->
174.0

<!-- b000518 | prose | pages [15] -->
0 50 100 150 200 250 300 350

<!-- b000519 | prose | pages [15] -->
0 50 100 150 200 250 300 350

<!-- b000520 | prose | pages [15] -->
Days

<!-- b000521 | prose | pages [15] -->
Days

<!-- b000522 | prose | pages [15] -->
Qaurtile 2

<!-- b000523 | prose | pages [15] -->
Huron/Michigan

<!-- b000524 | prose | pages [15] -->
Superior

<!-- b000525 | prose | pages [15] -->
176.5

<!-- b000526 | prose | pages [15] -->
183.4

<!-- b000527 | prose | pages [15] -->
176.4

<!-- b000528 | prose | pages [15] -->
Water Height Water Height

<!-- b000529 | prose | pages [15] -->
176.3

<!-- b000530 | prose | pages [15] -->
183.3

<!-- b000531 | prose | pages [15] -->
176.2

<!-- b000532 | prose | pages [15] -->
183.2

<!-- b000533 | prose | pages [15] -->
176.1

<!-- b000534 | prose | pages [15] -->
183.1

<!-- b000535 | prose | pages [15] -->
176.0

<!-- b000536 | prose | pages [15] -->
175.9

<!-- b000537 | prose | pages [15] -->
183.0

<!-- b000538 | prose | pages [15] -->
175.8

<!-- b000539 | prose | pages [15] -->
182.9

<!-- b000540 | prose | pages [15] -->
Erie Ontario

<!-- b000541 | prose | pages [15] -->
174.50

<!-- b000542 | prose | pages [15] -->
75.1

<!-- b000543 | prose | pages [15] -->
174.45

<!-- b000544 | prose | pages [15] -->
75.0

<!-- b000545 | prose | pages [15] -->
Water Height Water Height

<!-- b000546 | prose | pages [15] -->
174.40

<!-- b000547 | prose | pages [15] -->
74.9

<!-- b000548 | prose | pages [15] -->
174.35

<!-- b000549 | prose | pages [15] -->
74.8

<!-- b000550 | prose | pages [15] -->
174.30

<!-- b000551 | prose | pages [15] -->
74.7

<!-- b000552 | prose | pages [15] -->
174.25

<!-- b000553 | prose | pages [15] -->
74.6

<!-- b000554 | prose | pages [15] -->
174.20

<!-- b000555 | prose | pages [15] -->
74.5

<!-- b000556 | prose | pages [15] -->
174.15

<!-- b000557 | prose | pages [15] -->
74.4

<!-- b000558 | prose | pages [15] -->
0 50 100 150 200 250 300 350

<!-- b000559 | prose | pages [15] -->
0 50 100 150 200 250 300 350

<!-- b000560 | prose | pages [15] -->
Days

<!-- b000561 | prose | pages [15] -->
Days

<!-- b000562 | caption | pages [15] -->
Figure 10: Plots of the 1st and 2nd quartiles of the

<!-- b000563 | prose | pages [15] -->
water levels in each of the Great Lakes drawn from the historic rain data. The water levels achieved by the model are shown with dotted blue lines and the ideal water levels with solid orange lines.

<!-- b000564 | furniture | pages [15] -->
关注数学模型

<!-- b000565 | furniture | pages [15] -->
2

<!-- b000566 | furniture | pages [15] -->
MATHmodels

<!-- b000567 | furniture | pages [15] -->
获取更多资讯

<!-- b000568 | furniture | pages [16] -->
Team # 2429211

<!-- b000569 | furniture | pages [16] -->
Page 16 of 24

<!-- b000570 | prose | pages [16] -->
Quartile 3

<!-- b000571 | prose | pages [16] -->
Superior

<!-- b000572 | prose | pages [16] -->
183.45

<!-- b000573 | prose | pages [16] -->
Huron/Michigan 176.5

<!-- b000574 | prose | pages [16] -->
微信公众号：数学模型

<!-- b000575 | prose | pages [16] -->
183.40

<!-- b000576 | prose | pages [16] -->
Water Height

<!-- b000577 | prose | pages [16] -->
183.35

<!-- b000578 | prose | pages [16] -->
183.30

<!-- b000579 | prose | pages [16] -->
183.25

<!-- b000580 | prose | pages [16] -->
183.20

<!-- b000581 | prose | pages [16] -->
Erie

<!-- b000582 | prose | pages [16] -->
174.6

<!-- b000583 | prose | pages [16] -->
Water Height

<!-- b000584 | prose | pages [16] -->
174.5

<!-- b000585 | prose | pages [16] -->
176.4

<!-- b000586 | prose | pages [16] -->
176.3

<!-- b000587 | prose | pages [16] -->
176.2

<!-- b000588 | prose | pages [16] -->
176.1

<!-- b000589 | prose | pages [16] -->
176.0

<!-- b000590 | prose | pages [16] -->
Ontario

<!-- b000591 | prose | pages [16] -->
75.1

<!-- b000592 | prose | pages [16] -->
75.0

<!-- b000593 | prose | pages [16] -->
74.9

<!-- b000594 | prose | pages [16] -->
微信号：MATHmodels

<!-- b000595 | prose | pages [16] -->
174.4

<!-- b000596 | prose | pages [16] -->
174.3

<!-- b000597 | prose | pages [16] -->
174.2

<!-- b000598 | prose | pages [16] -->
0 50 100 150 200 250 300 350 Days

<!-- b000599 | prose | pages [16] -->
74.8

<!-- b000600 | prose | pages [16] -->
74.7

<!-- b000601 | prose | pages [16] -->
74.6

<!-- b000602 | prose | pages [16] -->
0 50 100 150 200 250 300 350

<!-- b000603 | prose | pages [16] -->
Days

<!-- b000604 | caption | pages [16] -->
Figure 11: Plots of achieved water levels using the third quartile rain data (extreme rain). The water

<!-- b000605 | prose | pages [16] -->
levels achieved by the model are shown with dotted blue lines and the ideal water levels are shown with solid orange lines.

<!-- b000606 | prose | pages [16] -->
5

<!-- b000607 | heading | pages [16] -->
Sensitivity Analysis

<!-- b000608 | prose | pages [16] -->
Since our model is primarily mechanistic, it relies heavily on parameters that represent real-life values such as flow rates, flow decay, and attenuation. As such, it is reasonable to observe how the model’s output changes as we modulate some of these parameters. Specifically, we vary 𝜔–the St. Lawrence river flow decay rate.

<!-- b000609 | prose | pages [16] -->
Moreover, we determine that it is possible to avoid flooding and dangerously low water levels while achieving desirable water levels in all lakes even with varying degrees of total inflow to the lakes. This demonstrates the value of our linear programming approach as a valuable tool to determine dam schedules.

<!-- b000610 | prose | pages [16] -->
The value that was used in the final model was 0.8. This was chosen based off observing flows in the St. Lawrence River and how they change with respect to the height of Lake Ontario. However, since there isn’t data on the status of the dam at these times, this link is admittedly tenuous. Thus, we decided to observe the effects of modulating this parameter on the net flow error in the St. Lawrence River. That is, with different decay rates, we measure how hard is it for our control algorithm to match the desired flow rate in the St. Lawrence River.

<!-- b000611 | furniture | pages [16] -->
关注数学模型

<!-- b000612 | furniture | pages [16] -->
2

<!-- b000613 | furniture | pages [16] -->
MATHmodels

<!-- b000614 | furniture | pages [16] -->
获取更多资讯

<!-- b000615 | furniture | pages [17] -->
Team # 2429211

<!-- b000616 | furniture | pages [17] -->
Page 17 of 24

<!-- b000617 | prose | pages [17] -->
We uniformly vary the parameter 𝜔in the range [0.7, 0.825] and observe the net error rate. We see that:

<!-- b000618 | prose | pages [17] -->
Yearly average ﬂow error based on ω

<!-- b000619 | prose | pages [17] -->
微信公众号：数学模型

<!-- b000620 | prose | pages [17] -->
1000

<!-- b000621 | prose | pages [17] -->
980

<!-- b000622 | prose | pages [17] -->
Net ﬂow error

<!-- b000623 | prose | pages [17] -->
960

<!-- b000624 | prose | pages [17] -->
940

<!-- b000625 | prose | pages [17] -->
920

<!-- b000626 | prose | pages [17] -->
0.70 0.72 0.74 0.76 0.78 0.80 0.82 ω

<!-- b000627 | prose | pages [17] -->
微信号：MATHmodels

<!-- b000628 | caption | pages [17] -->
Figure 12: Flow in the St. Lawrence River is sensitive to 𝜔

<!-- b000629 | prose | pages [17] -->
The error here varies quite significantly. In some sense, this is not surprising. Complex systems such as the Great Lakes are very sensitive to slight physical changes. To maximize the effectiveness of the model, it is therefore important to be able to measure these parameters accurately, and provide them to the model with high-resolution.

<!-- b000630 | prose | pages [17] -->
In conclusion, the model is largely robust to changes in climate forecasting. However, due to its mechanistic nature, it is quite sensitive to parameters describing natural and artificial flow processes.

<!-- b000631 | prose | pages [17] -->
6

<!-- b000632 | heading | pages [17] -->
Conclusions

<!-- b000633 | prose | pages [17] -->
• Our model demonstrates that to effectively manage Lake Ontario, the ĲC must also effectively manage Lake Superior. Lake Superior has the capacity to send large amounts of water to Lake Ontario. While the time it takes for Lake Ontario to feel the effects of actions taken at Lake Superior, by proactively increasing the water sent from Lake Superior, Lake Ontario can more effectively manage its water levels.

<!-- b000634 | prose | pages [17] -->
• Dam schedules will consistently make tradeoffs betweeen flood/drought security and stake- holder satisfaction. It is important to manage stakeholder expectations and use equitable prioritization methods to ensure overall contentedness.

<!-- b000635 | prose | pages [17] -->
• Testing schedules against different severities of exogenous inflow yield outcomes that are significantly more robust to climate and hydrologic events. Regardless of the scheduling algorithm, plans should always be tested against real historical inflows as well as randomly simulated climate events.

<!-- b000636 | furniture | pages [17] -->
关注数学模型

<!-- b000637 | furniture | pages [17] -->
2

<!-- b000638 | furniture | pages [17] -->
MATHmodels

<!-- b000639 | furniture | pages [17] -->
获取更多资讯

<!-- b000640 | furniture | pages [18] -->
Team # 2429211

<!-- b000641 | prose | pages [18] -->
6.1

<!-- b000642 | heading | pages [18] -->
Strengths

<!-- b000643 | furniture | pages [18] -->
Page 18 of 24

<!-- b000644 | prose | pages [18] -->
1. Due the speed of solving linear programs, our model can be employed to develop schedules for a large number of potential forecasts and ideal water levels. This allows practitioners to

<!-- b000645 | prose | pages [18] -->
微信公众号：数学模型

<!-- b000646 | prose | pages [18] -->
be more prepared for extreme weather events by being able to prep schedules for best-case, worst-case, and average-case weather events. If it becomes evident that the environmental data that the dam control schedule was created from is poor, a new schedule can be quickly substituted in to mitigate damage.

<!-- b000647 | prose | pages [18] -->
2. Our control algorithms can effectively meet stakeholder demands while the water levels re- main close to historical averages. The Great Lakes water system needs to flow naturally while still accounting for the demands of stakeholders, so our model must meet this benchmark.

<!-- b000648 | prose | pages [18] -->
3. Due to the constrained nature of our control algorithms, practitioners will always be aware of the maximum and minimum water levels that are produced by the schedule. Since actions taken at Lake Superior affect Lake Ontario with a severe delay, there is an associated risk

<!-- b000649 | prose | pages [18] -->
微信号：MATHmodels

<!-- b000650 | prose | pages [18] -->
with increasing or decreasing the flow through the Compensating Works dam. Our control algorithms allow for practitioners to predict the effect of the schedules they implement.

<!-- b000651 | prose | pages [18] -->
4. Our model is extremely flood and drought-resistant. In our analysis using realistic precipita- tion data our model didn’t experience any droughts or floods.

<!-- b000652 | prose | pages [18] -->
6.2

<!-- b000653 | heading | pages [18] -->
Weaknesses

<!-- b000654 | prose | pages [18] -->
Practitioners need to be aware of the flaws of our model so that unexpected results from our control algorithms can be mitigated. The weaknesses of our model are as follows:

<!-- b000655 | prose | pages [18] -->
• Due to the mechanistic nature of our model, the schedule of the model is noticeably sensitive to changes in parameters related to natural processes. For example, if the rate of flow decay in the St. Lawrence River is poorly measured, the model will produce a schedule that differs slightly, but noticeably, from the true ideal schedule. Practitioners should be aware of this flaw and apply the model several times with varying values for parameters like the decay rate and rain schedule. While the schedule will be sensitive to poor measurements, it will provide valuable insights into how to best manage the dams.

<!-- b000656 | prose | pages [18] -->
• Our model assumes a linear relationship between the height of a body of water and the total outflow which may change over time as the landscape of the Great Lakes changes. To account for this, practitioners should routinely track the relationship between the height of each lake and the observed flows of each lake’s distributaries.

<!-- b000657 | prose | pages [18] -->
• Due to the constraints placed on flooding and dangerously low water levels, our model will occasionally determine that an adequate schedule is possible. If practitioners encounter this issue when using our proposed control algorithms, they must choose the location and extent of flooding that will necessarily occur. We believe that no model can completely avoid flooding, so we believe that our model’s ability to have controlled and predictable flooding is sufficiently safe.

<!-- b000658 | furniture | pages [18] -->
关注数学模型

<!-- b000659 | furniture | pages [18] -->
2

<!-- b000660 | furniture | pages [18] -->
MATHmodels

<!-- b000661 | furniture | pages [18] -->
获取更多资讯

<!-- b000662 | furniture | pages [19] -->
Team # 2429211

<!-- b000663 | prose | pages [19] -->
7 Future Exploration

<!-- b000664 | furniture | pages [19] -->
Page 19 of 24

<!-- b000665 | prose | pages [19] -->
To address some of the weaknesses we identified, we believe that our model could be expanded in the following ways:

<!-- b000666 | prose | pages [19] -->
微信公众号：数学模型

<!-- b000667 | prose | pages [19] -->
• Pull from more refined data: By pulling from more refined data, our model would have more accurate information hydrological information. As a result, our model could improve the mechanistic nature of our model.

<!-- b000668 | prose | pages [19] -->
• Safety Optimizer: Another extension of our model could be using the results from running many fuzzy trials to determine which dam schedule is optimal against random weather conditions. This would allow practitioners to understand the risk assosiated with the schedules they select.

<!-- b000669 | prose | pages [19] -->
• Create an algorithm to determine which stakeholders to prioritize. The time of year has a large effect on the possibility of pleasing any particular stakeholder. A future direction of

<!-- b000670 | prose | pages [19] -->
微信号：MATHmodels

<!-- b000671 | prose | pages [19] -->
this work would be to implement the time of year into our weighting of the stakeholders.

<!-- b000672 | furniture | pages [19] -->
关注数学模型

<!-- b000673 | furniture | pages [19] -->
2

<!-- b000674 | furniture | pages [19] -->
MATHmodels

<!-- b000675 | furniture | pages [19] -->
获取更多资讯

<!-- b000676 | furniture | pages [20] -->
Team # 2429211

<!-- b000677 | prose | pages [20] -->
8

<!-- b000678 | heading | pages [20] -->
Memo To The ĲC

<!-- b000679 | prose | pages [20] -->
Dear ĲC Leadership,

<!-- b000680 | furniture | pages [20] -->
Page 20 of 24

<!-- b000681 | prose | pages [20] -->
微信公众号：数学模型

<!-- b000682 | prose | pages [20] -->
In light of the successes and failures experienced by Plan 2014 in regards to controlling the Moses-Saunders dam at Lake Ontario, we developed two linear programming-based control algorithms to effectively determine how to jointly manage the Compensating Works Dam at Lake Superior and the Moses-Saunders Dam at Lake Ontario to achieve ideal water levels throughout the Great Lakes. We believe that our algorithms build off of the adaptive control approach that Plan 2014 has successfully implemented while avoiding the limitations of Plan 2014 that have allowed for flooding in recent years.

<!-- b000683 | prose | pages [20] -->
In our model, we employ linear programming and a series of algorithms that forecast the needs of the stakeholders to determine how much we need to open dams at Lake Superior and Ontario. Because we are using a linear program, our model can simulate hundreds of thousands of scenarios within a few minutes, this would allow for the ĲC to have a more holistic approach to assessing the risks of running certain dam schedules for their stakeholders. Our algorithm for determining

<!-- b000684 | prose | pages [20] -->
微信号：MATHmodels

<!-- b000685 | prose | pages [20] -->
the optimal levels of stakeholders is based on their desires outlined in the ĲC report and draws from historical water levels [10]. Our model also utilizes historical data to simulate natural processes in the hydrosphere in the following ways:

<!-- b000686 | prose | pages [20] -->
• We account for the time it takes water to flow between lakes. We were able to correlate the water level data between different lakes to estimate the time it taken for flows to propagate through the system.

<!-- b000687 | prose | pages [20] -->
• We use a data-driven approach to determine flow rates of naturally flowing sources. More- over, using the data available to us, we found a strong linear relationship between height and the rate and which water flows out.

<!-- b000688 | prose | pages [20] -->
• Our model accounts for various levels of rainfall and other hydrological processes. We utilized a combination of precipitation from NOAA and preexisting models to get randomized, but representative rain data to run our situations [17] [22].

<!-- b000689 | prose | pages [20] -->
To show the resilience of our model we ran it under various extreme climate events and found it was effective in preventing floods and droughts. Specifically, the way our algorithms achieve near-optimal water levels even with severe climate events is by creatively managing Lake Superior. By incorporating the relationship between Lake Superior and Lake Ontario into our model, we are able to achieve schedules that allow Lake Ontario to remain safe and beneficial to the stakeholders.

<!-- b000690 | prose | pages [20] -->
We believe that our model provides the ĲC with valuable insights about how to best manage the Compensating Works and Sault. St. Marie dams. Our model will allow the ĲC to use the most recent sets of data being gathered at the monitoring points along the Great Lakes and adapt an optimal dam schedule based on current conditions and predictive forecasts.

<!-- b000691 | prose | pages [20] -->
Thank you for your consideration,

<!-- b000692 | furniture | pages [20] -->
Team #2429211

<!-- b000693 | furniture | pages [20] -->
关注数学模型

<!-- b000694 | furniture | pages [20] -->
2

<!-- b000695 | furniture | pages [20] -->
MATHmodels

<!-- b000696 | furniture | pages [20] -->
获取更多资讯

<!-- b000697 | furniture | pages [21] -->
Team # 2429211

<!-- b000698 | prose | pages [21] -->
A

<!-- b000699 | heading | pages [21] -->
Notation

<!-- b000700 | prose | pages [21] -->
Name Type

<!-- b000701 | furniture | pages [21] -->
Page 21 of 24

<!-- b000702 | prose | pages [21] -->
Description.

<!-- b000703 | prose | pages [21] -->
微信公众号：数学模型

<!-- b000704 | prose | pages [21] -->
𝑇 Set

<!-- b000705 | prose | pages [21] -->
𝐵 Set

<!-- b000706 | prose | pages [21] -->
Set of time-steps.

<!-- b000707 | prose | pages [21] -->
Set of Bodies of Water.

<!-- b000708 | prose | pages [21] -->
Height of water let through the Sault St. Marie Dam at time 𝑡. 𝑥𝑡 Variable

<!-- b000709 | prose | pages [21] -->
Height of water let through the Moses-Saunders Dam at time 𝑡. 𝑦𝑡 Variable

<!-- b000710 | prose | pages [21] -->
Flow at River Lawrence at time 𝑡. 𝑓𝑡 Variable

<!-- b000711 | prose | pages [21] -->
Height of water in body of water 𝑖at time 𝑡. ℎ𝑖,𝑡 Variable

<!-- b000712 | prose | pages [21] -->
Weighting term for the objective function. High 𝜔𝑖 𝜔𝑖 Parameter

<!-- b000713 | prose | pages [21] -->
The total height added by environmental factors in body of water 𝑖at time 𝑡. 𝑟𝑖,𝑡 Parameter

<!-- b000714 | prose | pages [21] -->
微信号：MATHmodels

<!-- b000715 | prose | pages [21] -->
The surface area of body of water 𝑖. 𝑠𝑖 Parameter

<!-- b000716 | prose | pages [21] -->
𝛼𝑖 Determined slope from regression. Parameter

<!-- b000717 | prose | pages [21] -->
𝛽𝑖 Determined bias from regression. Parameter

<!-- b000718 | prose | pages [21] -->
𝐿 Lag time between specified bodies of water. Parameter

<!-- b000719 | prose | pages [21] -->
Height of water required for a flood at body of water 𝑖. 𝐹𝑖 Parameter

<!-- b000720 | prose | pages [21] -->
Height required for dangerously low water at body of water 𝑖. 𝐷𝑖 Parameter

<!-- b000721 | prose | pages [21] -->
𝑀1 Maximum height of water releasable from Lake Superior during a time-step. Parameter

<!-- b000722 | prose | pages [21] -->
𝑀2 Maximum height of water releasable from Lake Ontario during a time-step Parameter

<!-- b000723 | prose | pages [21] -->
𝑤 Influence of the Mosses-Saunders Dam on the flow of the St. Lawrence River Parameter

<!-- b000724 | caption | pages [21] -->
Table 2: Description of variables involed in the mathematical program used to determine dam

<!-- b000725 | prose | pages [21] -->
schedules. All heights are in meters, all flows are in cubic meters per second, and all areas are given meters squared, all lag times are given in days

<!-- b000726 | furniture | pages [21] -->
关注数学模型

<!-- b000727 | furniture | pages [21] -->
2

<!-- b000728 | furniture | pages [21] -->
MATHmodels

<!-- b000729 | furniture | pages [21] -->
获取更多资讯

<!-- b000730 | furniture | pages [22] -->
Team # 2429211

<!-- b000731 | prose | pages [22] -->
Name Type

<!-- b000732 | prose | pages [22] -->
𝐵𝑖

<!-- b000733 | furniture | pages [22] -->
Page 22 of 24

<!-- b000734 | prose | pages [22] -->
Description.

<!-- b000735 | prose | pages [22] -->
Bodies of water (Ontario, St. Lawrence) Set

<!-- b000736 | prose | pages [22] -->
微信公众号：数学模型

<!-- b000737 | prose | pages [22] -->
𝑇 Param

<!-- b000738 | prose | pages [22] -->
𝐹𝑡

<!-- b000739 | prose | pages [22] -->
Time Horizon

<!-- b000740 | prose | pages [22] -->
Hourly inflow into Lake Ontario Param

<!-- b000741 | prose | pages [22] -->
ˆℎ𝑡 Param

<!-- b000742 | prose | pages [22] -->
ˆ𝑓𝑡 Param

<!-- b000743 | prose | pages [22] -->
𝑘

<!-- b000744 | prose | pages [22] -->
Ideal water levels

<!-- b000745 | prose | pages [22] -->
Ideal flow levels

<!-- b000746 | prose | pages [22] -->
Flow conversion coefficient Param

<!-- b000747 | prose | pages [22] -->
𝑙𝑖 Initial water and flow levels Param

<!-- b000748 | prose | pages [22] -->
𝛼𝑖 Weights for stakeholder importance Param

<!-- b000749 | prose | pages [22] -->
𝜔 Hourly flow decay coefficient Param

<!-- b000750 | prose | pages [22] -->
微信号：MATHmodels

<!-- b000751 | prose | pages [22] -->
𝑂 Param

<!-- b000752 | prose | pages [22] -->
ˆ𝐻 Param

<!-- b000753 | prose | pages [22] -->
ℎ𝑡 Variable

<!-- b000754 | prose | pages [22] -->
𝑓𝑡 Variable

<!-- b000755 | prose | pages [22] -->
𝑥𝑡

<!-- b000756 | prose | pages [22] -->
Dam outflow limit

<!-- b000757 | prose | pages [22] -->
Final water height

<!-- b000758 | prose | pages [22] -->
Water level

<!-- b000759 | prose | pages [22] -->
Flow level

<!-- b000760 | prose | pages [22] -->
Moses-Saunders Dam outflow Variable

<!-- b000761 | caption | pages [22] -->
Table 3: Microschedule LP formulation. All water levels are heights in meters, all times are in

<!-- b000762 | prose | pages [22] -->
hours, and all flows are in cubic meters per second

<!-- b000763 | furniture | pages [22] -->
关注数学模型

<!-- b000764 | furniture | pages [22] -->
2

<!-- b000765 | furniture | pages [22] -->
MATHmodels

<!-- b000766 | furniture | pages [22] -->
获取更多资讯

<!-- b000767 | furniture | pages [23] -->
Team # 2429211

<!-- b000768 | heading | pages [23] -->
References

<!-- b000769 | furniture | pages [23] -->
Page 23 of 24

<!-- b000770 | references | pages [23] -->
[1] 2024MCM/ICM Problems. https://www.immchallenge.org/mcm/index.html.

<!-- b000771 | references | pages [23] -->
[2] International Joint Commission (2014). Lake Ontario St. Lawrence River Plan 201: Protecting

<!-- b000772 | references | pages [23] -->
微信公众号：数学模型

<!-- b000773 | references | pages [23] -->
against extreme water levels, restoring wetlands and preparing for climate change, 2014.

<!-- b000774 | references | pages [23] -->
[3] US army Corps of Engineers. John glenn great lakes basin program biohydrological informa-

<!-- b000775 | references | pages [23] -->
tion base, 2007.

<!-- b000776 | references | pages [23] -->
[4] Peng Bai, Jia Wang, Philip Chu, Nathan Hawley, Ayumi Fujisaki-Manome, James Kessler,

<!-- b000777 | references | pages [23] -->
Brent M Lofgren, Dmitry Beletsky, Eric J Anderson, and Yaru Li. Modeling the ice-attenuated

<!-- b000778 | references | pages [23] -->
waves in the great lakes. Ocean Dynamics, 70:991–1003, 2020.

<!-- b000779 | references | pages [23] -->
[5] Chiranjib Bhowmik, Sumit Bhowmik, Amitava Ray, and Krishna Murari Pandey. Optimal

<!-- b000780 | references | pages [23] -->
green energy planning for sustainable development: A review. Renewable and Sustainable

<!-- b000781 | references | pages [23] -->
Energy Reviews, 71:796–813, 2017.

<!-- b000782 | references | pages [23] -->
[6] Thomas Bläsius, Adrian Feilhauer, and Jannik Westenfelder.

<!-- b000783 | references | pages [23] -->
dependent capacities, 2023.

<!-- b000784 | references | pages [23] -->
Dynamic flows with time-

<!-- b000785 | references | pages [23] -->
微信号：MATHmodels

<!-- b000786 | references | pages [23] -->
[7] Murray Clamen and Daniel Macfarlane. Plan 2014: The historical evolution of lake ontario–

<!-- b000787 | references | pages [23] -->
Canadian Water Resources Journal/Revue canadienne des

<!-- b000788 | references | pages [23] -->
st. lawrence river regulation.

<!-- b000789 | references | pages [23] -->
ressources hydriques, 43(4):416–431, 2018.

<!-- b000790 | references | pages [23] -->
[8] Great Lakes Commission.

<!-- b000791 | references | pages [23] -->
[9] International Joint Commission. Options for managing lake ontario and st. lawrence river

<!-- b000792 | references | pages [23] -->
water levels and flows (final report), 2006.

<!-- b000793 | references | pages [23] -->
[10] International Joint Commission. Section 5: Impacts on various interests, 2023.

<!-- b000794 | references | pages [23] -->
[11] George B Dantzig. Linear programming. History of mathematical programming, pages

<!-- b000795 | references | pages [23] -->
19–31, 1991.

<!-- b000796 | references | pages [23] -->
[12] Jean-Luc Desgranges, Joel Ingram, Bruno Drolet, Jean Morin, Caroline Savage, and Daniel

<!-- b000797 | references | pages [23] -->
Borcard. Modelling wetland bird response to water level changes in the lake ontario–st.

<!-- b000798 | references | pages [23] -->
lawrence river hydrosystem. Environmental monitoring and assessment, 113:329–365, 2006.

<!-- b000799 | references | pages [23] -->
[13] Google Earth. Great lakes, no clouds, 2010.

<!-- b000800 | references | pages [23] -->
[14] Lester Randolph Ford. Flows in networks. 2015.

<!-- b000801 | references | pages [23] -->
[15] Inga Kanoshina, Urmas Lips, and Juha-Markku Leppänen. The influence of weather con-

<!-- b000802 | references | pages [23] -->
ditions (temperature and wind) on cyanobacterial bloom development in the gulf of finland

<!-- b000803 | references | pages [23] -->
(baltic sea). Harmful Algae, 2(1):29–41, 2003.

<!-- b000804 | references | pages [23] -->
[16] Frank Millerd. The economic impact of climate change on canadian commercial navigation

<!-- b000805 | references | pages [23] -->
on the great lake. Canadian Water Resources Journal, 30(4):269–280, 2005.

<!-- b000806 | references | pages [23] -->
[17] NOAA. Noaa glerl data, 2021.

<!-- b000807 | references | pages [23] -->
[18] National Oceanic and Atmospheric Administration. Great lakes ecoregion - national oceanic

<!-- b000808 | references | pages [23] -->
and atmospheric administration, 2019.

<!-- b000809 | references | pages [23] -->
[19] Frank J Rahel and Julian D Olden. Assessing the effects of climate change on aquatic invasive

<!-- b000810 | references | pages [23] -->
species. Conservation biology, 22(3):521–533, 2008.

<!-- b000811 | furniture | pages [23] -->
关注数学模型

<!-- b000812 | furniture | pages [23] -->
2

<!-- b000813 | furniture | pages [23] -->
MATHmodels

<!-- b000814 | furniture | pages [23] -->
获取更多资讯

<!-- b000815 | furniture | pages [24] -->
Team # 2429211

<!-- b000816 | furniture | pages [24] -->
Page 24 of 24

<!-- b000817 | references | pages [24] -->
[20] Charles S. Revelle, Daniel P. Loucks, and Walter R. Lynn. Linear programming applied to

<!-- b000818 | references | pages [24] -->
water quality management. Water Resources Research, 4(1):1–9, 1968.

<!-- b000819 | references | pages [24] -->
[21] Michael H Veatch. Linear and convex optimization: A Mathematical Approach. John Wiley

<!-- b000820 | references | pages [24] -->
微信公众号：数学模型

<!-- b000821 | references | pages [24] -->
& Sons, 2020.

<!-- b000822 | references | pages [24] -->
[22] Daniel S Wilks and Robert L Wilby. The weather generation game: a review of stochastic

<!-- b000823 | references | pages [24] -->
weather models. Progress in physical geography, 23(3):329–357, 1999.

<!-- b000824 | references | pages [24] -->
微信号：MATHmodels

<!-- b000825 | furniture | pages [24] -->
关注数学模型

<!-- b000826 | furniture | pages [24] -->
2

<!-- b000827 | furniture | pages [24] -->
MATHmodels

<!-- b000828 | furniture | pages [24] -->
获取更多资讯

<!-- b000829 | furniture | pages [25] -->
Team # 2429211

<!-- b000830 | references | pages [25] -->
Page 25

<!-- b000831 | heading | pages [25] -->
Report on Use of AI

<!-- b000832 | ai_disclosure | pages [25] -->
Dear ICM Judges,

<!-- b000833 | ai_disclosure | pages [25] -->
微信公众号：数学模型

<!-- b000834 | ai_disclosure | pages [25] -->
No AI was used in the writing, code, or development of this project.

<!-- b000835 | ai_disclosure | pages [25] -->
We wish you the best.

<!-- b000836 | ai_disclosure | pages [25] -->
微信号：MATHmodels

<!-- b000837 | furniture | pages [25] -->
关注数学模型

<!-- b000838 | furniture | pages [25] -->
2

<!-- b000839 | furniture | pages [25] -->
MATHmodels

<!-- b000840 | furniture | pages [25] -->
获取更多资讯
