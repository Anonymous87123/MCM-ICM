# P-D-2024-2429211-de10f571

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
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
1 Introduction

<!-- b000027 | contents | pages [2] -->
3

<!-- b000028 | contents | pages [2] -->
1.1

<!-- b000029 | contents | pages [2] -->
Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000030 | contents | pages [2] -->
3

<!-- b000031 | contents | pages [2] -->
1.2

<!-- b000032 | contents | pages [2] -->
Restatement Of The Question . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000033 | contents | pages [2] -->
3

<!-- b000034 | contents | pages [2] -->
1.3

<!-- b000035 | contents | pages [2] -->
Overview of Linear Programs . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000036 | contents | pages [2] -->
4

<!-- b000037 | contents | pages [2] -->
1.4

<!-- b000038 | contents | pages [2] -->
Assumptions And Justifications . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000039 | contents | pages [2] -->
5

<!-- b000040 | contents | pages [2] -->
2 Macroschedule Model

<!-- b000041 | contents | pages [2] -->
6

<!-- b000042 | contents | pages [2] -->
2.1

<!-- b000043 | contents | pages [2] -->
Dynamic Network Formulation . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000044 | contents | pages [2] -->
6

<!-- b000045 | contents | pages [2] -->
2.2

<!-- b000046 | contents | pages [2] -->
Ideal Water Determination Algorithm

<!-- b000047 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000048 | contents | pages [2] -->
7

<!-- b000049 | contents | pages [2] -->
微信号：MATHmodels

<!-- b000050 | contents | pages [2] -->
2.3

<!-- b000051 | contents | pages [2] -->
Linear Program Formulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000052 | contents | pages [2] -->
7

<!-- b000053 | contents | pages [2] -->
2.4

<!-- b000054 | contents | pages [2] -->
Methods for Stakeholder Management . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000055 | contents | pages [2] -->
9

<!-- b000056 | contents | pages [2] -->
2.5

<!-- b000057 | contents | pages [2] -->
Data-Based Model Of The Hydrosphere . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000058 | contents | pages [2] -->
10

<!-- b000059 | contents | pages [2] -->
2.6

<!-- b000060 | contents | pages [2] -->
Additional Considerations

<!-- b000061 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000062 | contents | pages [2] -->
12

<!-- b000063 | contents | pages [2] -->
3 Microschedule Model

<!-- b000064 | contents | pages [2] -->
12

<!-- b000065 | contents | pages [2] -->
4 Model Insights

<!-- b000066 | contents | pages [2] -->
13

<!-- b000067 | contents | pages [2] -->
4.1

<!-- b000068 | contents | pages [2] -->
Dynamic Control Of The System . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000069 | contents | pages [2] -->
14

<!-- b000070 | contents | pages [2] -->
4.2

<!-- b000071 | contents | pages [2] -->
Robustness to Severe Climate Events . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000072 | contents | pages [2] -->
15

<!-- b000073 | contents | pages [2] -->
5 Sensitivity Analysis

<!-- b000074 | contents | pages [2] -->
16

<!-- b000075 | contents | pages [2] -->
6 Conclusions

<!-- b000076 | contents | pages [2] -->
17

<!-- b000077 | contents | pages [2] -->
6.1

<!-- b000078 | contents | pages [2] -->
Strengths

<!-- b000079 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000080 | contents | pages [2] -->
18

<!-- b000081 | contents | pages [2] -->
6.2

<!-- b000082 | contents | pages [2] -->
Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000083 | contents | pages [2] -->
18

<!-- b000084 | contents | pages [2] -->
7 Future Exploration

<!-- b000085 | contents | pages [2] -->
19

<!-- b000086 | contents | pages [2] -->
8 Memo To The ĲC

<!-- b000087 | contents | pages [2] -->
20

<!-- b000088 | contents | pages [2] -->
A Notation

<!-- b000089 | contents | pages [2] -->
21

<!-- b000090 | furniture | pages [2] -->
关注数学模型

<!-- b000091 | furniture | pages [2] -->
2

<!-- b000092 | furniture | pages [2] -->
MATHmodels

<!-- b000093 | furniture | pages [2] -->
获取更多资讯

<!-- b000094 | furniture | pages [3] -->
Team # 2429211

<!-- b000095 | furniture | pages [3] -->
Page 3 of 24

<!-- b000096 | heading | pages [3] -->
1 Introduction

<!-- b000097 | heading | pages [3] -->
1.1 Background

<!-- b000098 | prose | pages [3] -->
微信公众号：数学模型 The Great Lakes are one of the most promi- nent features of the North American continent; they not only make up 20 percent of the world’s freshwater, but they also have a tremendous im- pact on the economy, climate, and ecosystems of the United States and Canada. The Great Lakes region is one of the largest economies in the world, supporting 1.5 million people and forming the backbone for other industries which are valued at over 6 trillion dollars [8]. Addi- tionally, they also are the source of life for over 3500 species of plants and animals across a 微信号：MATHmodels wide range of biomes making them indispens- able to the North American ecosystems [18].

<!-- b000099 | caption | pages [3] -->
Figure 1: A cloudless view of all of the Great

<!-- b000100 | prose | pages [3] -->
Due to the invaluable benefit that the Great Lakes taken by a NASA satellite in August 2010 Lakes provide us, it is of the utmost importance [13]. to society that they are flourishing in the best way possible.

<!-- b000101 | prose | pages [3] -->
To ensure that the Great Lakes community is well-serviced, it is necessary to analyze the impacts on the stakeholders dependent on the lakes. The stakeholders identified in the report by the Inter- national Joint Committee (ĲC) are: domestic water supply, commercial navigation, hydropower, environment, recreational boaters, docking companies, and shoreline (riparian) property owners [10].

<!-- b000102 | prose | pages [3] -->
The current methodology of managing the water flow in Lake Ontario is based on Plan 2014. Plan 2014 prioritizes natural flow out of Lake Ontario into the St. Lawrence River while continually checking if a number of critical points have been reached. When a critical point has been reached, the ĲC takes action to control the level of water in the dam [2]. After the initiation of Plan 2014 in 2017, record precipitation hit the area and Lake Ontario experienced severe flooding [7]. This caused millions of dollars of damage and increased the risk for invasive species (like zebra mussels), harmful algae bloom, and sewage blockage [15] [19] [10]. This event brought the effectiveness of the plan under scrutiny. Flooding has proven to be a continual threat to the lives and livelihoods of the stakeholders. Thus, ICM has set out to formulate water level control mechanisms that could prevent such dire events.

<!-- b000103 | heading | pages [3] -->
1.2 Restatement Of The Question

<!-- b000104 | prose | pages [3, 4] -->
To address the concerns of the ĲC, we propose a number of human-centered algorithms that control the water levels of the Great Lakes to best address the residents’ concerns around Lake Ontario and the St. Lawrence River. Our models and algorithms are fit to address the needs of various stakeholders, while ensuring that the water levels within the lakes remain safe. Motivated by the flooding damage from 2017, our model focuses on achieving water levels and currents that benefit the stakeholders subject to hard constraints on the risk of flooding and low-water levels. Our outlook differs significantly from that of Plan 2014 to be more resilient in a highly volatile climate. We propose using a linear program to model the needs of the stakeholders with respect to the water level and modulating it with dynamic control of dams that account for the transportation times of 微信公众号：数学模型 the water. Inspired by the successes of Plan 2014 as a method to solve a complex constrained scheduling problem and equipped with the knowledge of where Plan 2014 falls short, we propose a model that utilizes the Compensating Works dam at the Sault. St. Marie River as well as the Moses-Saunders dam to do the following:

<!-- b000105 | furniture | pages [3] -->
关注数学模型

<!-- b000106 | furniture | pages [3] -->
2

<!-- b000107 | furniture | pages [3] -->
MATHmodels

<!-- b000108 | furniture | pages [3] -->
获取更多资讯

<!-- b000109 | furniture | pages [4] -->
Team # 2429211

<!-- b000110 | furniture | pages [4] -->
Page 4 of 24

<!-- b000112 | heading | pages [4] -->
1. Center the human impacts by modeling the needs of the stakeholders

<!-- b000113 | heading | pages [4] -->
2. Robustness to severe climate events

<!-- b000114 | heading | pages [4] -->
3. Dynamic control of the system

<!-- b000115 | heading | pages [4] -->
1.3 Overview of Linear Programs

<!-- b000116 | prose | pages [4] -->
微信号：MATHmodels Our control algorithms are implemented as linear programs. Linear programming is a widely- used optimization technique in the field of operations research and network science. It has various applications from policymaking to power plant deployment to production logistics to watershed management [11, 20]. Linear programs rapidly found applications across the natural sciences, industry, government, and many other fields, and are a natural way to model many scheduling problems where it is important to understand how to plan a series of actions to maximize an objective (typically profit or some other measure of overall utility) subject to some constraints (e.g. there might only be so much time available to us) [21]. Within the realm of environmental decisions, linear programming has been applied to solve complex questions like green-energy planning [5]. Inspired by the success of linear programs in related fields, our control algorithms employ linear programming to determine how to utilize the dams within the Great Lakes. The advantages to be expected from utilizing linear programming are as follows:

<!-- b000117 | prose | pages [4] -->
• Algorithms for solving linear programs are widely available and extremely fast. Due to the effectiveness of the famous Simplex algorithm and its variants, linear programs can be solved with incredible speed which is advantageous for testing out a variety of weather scenarios.

<!-- b000118 | prose | pages [4] -->
• Linear programs are interpretable. Practitioners need access to a white-box control algo- rithm where it is possible to understand their decision.

<!-- b000119 | prose | pages [4] -->
• Linear programs are not defined with specific parameter values in mind. If practitioners need to revise their predictions for environmental factors, they can easily rerun the model with the adjusted parameters.

<!-- b000120 | prose | pages [4] -->
However, it’s also important to acknowledge the downsides that accompany linear programs:

<!-- b000121 | prose | pages [4] -->
• The objective and constraints must be linear. This limits the ways we can model our system considerably and, as such, it is important to recognize parts of the model that are remnants of the required linearity.

<!-- b000122 | furniture | pages [4] -->
关注数学模型

<!-- b000123 | furniture | pages [4] -->
2

<!-- b000124 | furniture | pages [4] -->
MATHmodels

<!-- b000125 | furniture | pages [4] -->
获取更多资讯

<!-- b000126 | furniture | pages [5] -->
Team # 2429211

<!-- b000127 | furniture | pages [5] -->
Page 5 of 24

<!-- b000128 | prose | pages [5] -->
• When a linear program is impossible to solve, it is difficult to visualize what is going wrong.

<!-- b000129 | prose | pages [5] -->
If our control algorithms determine that there is no valid schedule that meets all constraints, it will be difficult for the practitioner to find a way to determine a valid schedule. 微信公众号：数学模型 By keeping these disadvantages in mind, we designed our control algorithms to be effective even with the drawbacks of linear programming.

<!-- b000130 | heading | pages [5] -->
1.4 Assumptions And Justifications

<!-- b000131 | prose | pages [5] -->
As mentioned in the problem statement, the dynamic network flow problem is wicked. As such, we make use of several assumptions to manage the complexity of our models.

<!-- b000132 | prose | pages [5] -->
↓ i W Hydrology: The lake’s sizes remain con- stant and our system can be simplified 微信号：MATHmodels

<!-- b000133 | caption | pages [5] -->
Figure 2: Since water levels do not vary

<!-- b000134 | prose | pages [5] -->
much relative to total depth, we can approxi- mate the lake surface area as being constant. We can then convert flow to marginal height by dividing by surface area. to five nodes by not factoring in the auxiliaries like lake St. Claire.

<!-- b000135 | prose | pages [5] -->
Justification: Keeping the lake sizes con- stant provides us with a consistent con- version metric, as seen in figure 2 be- tween flow and height for each lake. Based on the correlation data for the flow rates, the other nodes are negligi- ble as compared to the main outflows between the Great Lakes.

<!-- b000136 | prose | pages [5] -->
Systemic: Dams can be fully opened or closed within an hour and they have zero downtime.

<!-- b000137 | prose | pages [5] -->
Additionally, the lag times calculated from correlation data are accurate (Figure 2).

<!-- b000138 | prose | pages [5] -->
Justification: We want to encapsulate granular dam schedules to minimize flooding and drought of the Great Lakes community. Also, we need the lag times to be accurate to simulate the water flowing between the lakes.

<!-- b000139 | prose | pages [5] -->
Scaling: The regressions we found for the flow rates from the lakes are linear (Figure 3) and the time horizon of the data is on the order of a few months.

<!-- b000140 | prose | pages [5] -->
Justification: The regressions are done on the order of the change in height of the lakes, so the flow rates for our purposes should be accurate. Since the time scale of our time lags is on the order of a few months, our time horizon encapsulates the lag time and our model should be used dynamically based on current data.

<!-- b000141 | furniture | pages [5] -->
关注数学模型

<!-- b000142 | furniture | pages [5] -->
2

<!-- b000143 | furniture | pages [5] -->
MATHmodels

<!-- b000144 | furniture | pages [5] -->
获取更多资讯

<!-- b000145 | furniture | pages [6] -->
Team # 2429211

<!-- b000146 | furniture | pages [6] -->
Page 6 of 24

<!-- b000147 | heading | pages [6] -->
2 Macroschedule Model

<!-- b000148 | prose | pages [6] -->
Here, we describe our algorithm for determining the optimal achievable water levels in the great lakes over a large time-period. 微信公众号：数学模型

<!-- b000149 | heading | pages [6] -->
2.1 Dynamic Network Formulation

<!-- b000150 | prose | pages [6] -->
We begin with a high-level overview of the model. The Great Lake water level problem can be studied as a dynamic network flow problem on the network shown in Figure 3. There are two arcs that we have some level of control over. The Sault St. Marie Dam allows us to send a constrained amount of water from Lake Superior to Lakes Huron and Michigan. Water then flows naturally from Lakes Huron and Michigan into Lake Erie and from Lake Erie to Lake Ontario. Through the Moses-Saunders Dam, we can let a constrained amount of water out of Lake Ontario into the St. Lawrence River.

<!-- b000151 | prose | pages [6] -->
The reason why our analysis differs from the well-studied static flow problem is because it takes time for water to flow between each node. For instance, it takes roughly one month for flows in 微信号：MATHmodels Lake Superior to be observed in Lakes Huron and Michigan; it takes roughly three months to be observed in Lake Ontario. Thus, the network flow becomes dynamic–which significantly increases the problem’s modeling and computational difficulty.

<!-- b000152 | prose | pages [6] -->
Superior

<!-- b000153 | prose | pages [6] -->
Erie 𝑐1, 𝑡1 𝑐2 Ontario St. Law

<!-- b000154 | prose | pages [6] -->
H.M

<!-- b000155 | caption | pages [6] -->
Figure 3: Network used in the model. 𝑐𝑖is the capacity of the arc and 𝑡𝑖is the transit time of the

<!-- b000156 | prose | pages [6] -->
arc. All unlabeled arcs correspond to uncontrolled flows of water.

<!-- b000157 | prose | pages [6] -->
More formally, the dynamic flow problem is defined over a network 𝑁= (𝑉, 𝐸, 𝜇, 𝜏,𝑉+,𝑉−). The vertex set is given by 𝑉∪𝑉+ ∪𝑉−where 𝑉+ represent source nodes, 𝑉−represent sink nodes, and 𝑉represent transit nodes. Each edge 𝐸𝑖has a corresponding capacity 𝜇𝑖𝑡and transit time 𝜏𝑖[6]. The goal is to find the min-cost flow over a fixed time horizon 𝑇that satisfies a particular objective.

<!-- b000158 | prose | pages [6] -->
To make this problem tractable, we employ Ford and Fulkerson’s time-expansion method to convert the problem into static flow [14]. We discretize the model over a fixed timestep, and we create copies of each node for each one over the entire time-horizon. We then assign edges based on the transit times between nodes. With this, the problem is now described by a network 𝑁◦= (𝑉, 𝐸, 𝜇,𝑉+,𝑉−). I.e. an augmented network that includes vertex copies but no transit times. This formulation is amenable to static-flow analysis.

<!-- b000159 | furniture | pages [6] -->
关注数学模型

<!-- b000160 | furniture | pages [6] -->
2

<!-- b000161 | furniture | pages [6] -->
MATHmodels

<!-- b000162 | furniture | pages [6] -->
获取更多资讯

<!-- b000163 | furniture | pages [7] -->
Team # 2429211

<!-- b000164 | furniture | pages [7] -->
Page 7 of 24

<!-- b000165 | heading | pages [7] -->
2.2 Ideal Water Determination Algorithm

<!-- b000166 | prose | pages [7] -->
To determine the ideal water levels for each body of water, we developed a utility function for each shareholder that determines their optimal water level based on the historical averages. 微信公众号：数学模型 This optimal water level is determined based on the fluctuations in the water level and what each of the stakeholders listed as their ideal scenario from the ĲC report. While navigation, docks, hydropower, and recreational boaters all prefer a fixed level of water, riparian owners, domestic water supply, and the environment prefer natural oscillations in water level [10]. To account for this discrepancy, we simulated sinusoidal oscillations about the mean height of the lake for their preferred timescales and amplitudes scaled compared to the natural processes:

<!-- b000167 | prose | pages [7] -->
Environment: The environment prefers natural annual water level oscillations to best align with the natural mating seasons of species like wetland birds [12].

<!-- b000168 | prose | pages [7] -->
Domestic Water Supply: To preserve high water quality, the domestic water supply needs to oscillate close to the average to prevent the inflow of sewage and harmful algae blooms 微信号：MATHmodels [15][10].

<!-- b000169 | prose | pages [7] -->
Riparian Owners: The riparian owners prefer lower water levels with smaller amplitude os- cillations, with higher frequency to increase the amount of sand re-deposition and dune replenishment [10].

<!-- b000170 | prose | pages [7] -->
Navigation: Navigation prefers steadily high water levels because lower water levels can increase costs by 30 percent and double emissions in the Great Lakes [16]. Additionally, they want it to not flood because they need ships to get through [10].

<!-- b000171 | prose | pages [7] -->
Hydropower: The dams prefer their flow rates to be constant or near their ideal operating range of around 7, 000𝑚3 𝑠, so they prefer to be above the average water levels, similar to navigation, to maintain that [9].

<!-- b000172 | prose | pages [7] -->
Boaters: Boaters also prefer to be in a similar range of slightly above the average water level to improve the speed they can travel through the water during the day [10].

<!-- b000173 | prose | pages [7] -->
Docks: For the shipping ports in Montreal, they prefer to have constant low water levels so the amount of the ideal amount of water coming downstream from the Moses-Saunders Dam should be minimized during working hours.

<!-- b000174 | prose | pages [7] -->
There are conflicting interests among the stakeholders, and it is impossible to please each stakeholder. To account for this, we introduced a weighting system into our model to allow each stakeholder to be considered with different severity. As a result, our ideal water plots look like

<!-- b000175 | caption | pages [7] -->
figure 4 compared to the historical data

<!-- b000176 | heading | pages [7] -->
2.3 Linear Program Formulation

<!-- b000177 | prose | pages [7, 8] -->
Here we describe the Linear Program (LP) we propose to determine long-term dam schedules for the Great Lakes. We consider two sets that our decision variables and parameters belong to: (1) Bodies of Water and (2) Time. Our decision variables are the amount of water we let flow from the Lake Ontario ideal water level curve Lake Superior ideal water level curve Ideal Ideal 75.1 Historic 183.45 Historic

<!-- b000178 | furniture | pages [7] -->
关注数学模型

<!-- b000179 | furniture | pages [7] -->
2

<!-- b000180 | furniture | pages [7] -->
MATHmodels

<!-- b000181 | furniture | pages [7] -->
获取更多资讯

<!-- b000182 | furniture | pages [8] -->
Team # 2429211

<!-- b000183 | furniture | pages [8] -->
Page 8 of 24

<!-- b000185 | prose | pages [8] -->
微信公众号：数学模型 75.0 183.40 Water level (m) Water level (m) 74.9 183.35

<!-- b000186 | prose | pages [8] -->
183.30 74.8

<!-- b000187 | prose | pages [8] -->
183.25 74.7

<!-- b000188 | prose | pages [8] -->
183.20 74.6

<!-- b000189 | prose | pages [8] -->
0 50 100 150 200 250 300 350 0 50 100 150 200 250 300 350 Day of year Day of year

<!-- b000190 | caption | pages [8] -->
Figure 4: Plot of the ideal water levels (solid orange lines) based on stakeholder needs for Lake

<!-- b000191 | prose | pages [8] -->
Superior and Lake Ontario compared to the historical averages (dotted blue lines) from the dataset.

<!-- b000192 | prose | pages [8] -->
微信号：MATHmodels Superior to the St. Mary River at each time-step and the amount of water we let flow from Lake Ontario to the St. Lawrence River1. The objective of the LP is to minimize the absolute difference between the achieved water level and the “ideal” water level. The LP is constrained by limits on the water level ensuring no flooding occurs and the water level is never critically low. The variables and parameters and described in the first table in Appendix A. The algebraic form of the linear program is shown below:

<!-- b000193 | prose | pages [8] -->
∑︁ ∑︁ ∑︁ 𝜔𝑖|ℎ𝑖,𝑡−ˆℎ𝑖,𝑡| + (1 − 𝜔𝑖) | 𝑓𝑡−ˆ𝑓𝑡| minimize 𝑖∈𝐵,𝑡∈𝑇 𝑖∈𝐵 𝑡∈𝑇 ℎ1,𝑡= ℎ1,𝑡−1 −𝑥𝑡−1 + 𝑟1,𝑡−1 ∀𝑡∈[1,𝑇] subject to 𝑠2𝑥𝑡−𝐿−(𝛼2ℎ2,𝑡−1+𝛽2) ℎ2,𝑡= ℎ2,𝑡−1 + 𝑠1 + 𝑟2,𝑡−1 ∀𝑡∈[1,𝑇] 𝑠2

<!-- b000194 | prose | pages [8] -->
ℎ3,𝑡= ℎ3,𝑡−1 + (𝛼2ℎ2,𝑡−𝐿+𝛽2) −(𝛼3ℎ3,𝑡−1+𝛽3) + 𝑟3,𝑡−1 ∀𝑡∈[1,𝑇] 𝑠3 𝑠3

<!-- b000195 | prose | pages [8] -->
ℎ4,𝑡= ℎ4,𝑡−1 + (𝛼3ℎ3,𝑡−1+𝛽3) −𝑦𝑡−1 + 𝑟4,𝑡−1 ∀𝑡∈[1,𝑇] 𝑠4

<!-- b000196 | prose | pages [8] -->
ℎ𝑖,𝑡≤𝐹𝑖 ∀𝑖∈𝐵, 𝑡∈[1,𝑇] ℎ𝑖,𝑡≥𝐷𝑖 ∀𝑖∈𝐵, 𝑡∈[1,𝑇] 𝑥𝑡≤𝑀1 ∀𝑡∈[1,𝑇] 𝑦𝑡≤𝑀2 ∀𝑡∈[1,𝑇] 𝑓𝑡= 𝑤𝑓𝑡−1 + (1 −𝑤)𝑦𝑡 ∀𝑡∈[1,𝑇]

<!-- b000197 | prose | pages [8] -->
1In Appendix A, more variables are listed, but these are completely determined by equality constraints and are thus not listed as decision variables here.

<!-- b000198 | furniture | pages [8] -->
关注数学模型

<!-- b000199 | furniture | pages [8] -->
2

<!-- b000200 | furniture | pages [8] -->
MATHmodels

<!-- b000201 | furniture | pages [8] -->
获取更多资讯

<!-- b000202 | furniture | pages [9] -->
Team # 2429211

<!-- b000203 | furniture | pages [9] -->
Page 9 of 24

<!-- b000204 | prose | pages [9] -->
All decision variables are nonnegative. The first four constraints capture how the height of water in each lake changes over time by tracking how much water enters the lake and how much leaves. We use the index 𝑥𝑡−𝐿to capture the fact that there is a lag between the changes in Lake Superior and the changes at other lakes. The 5th and 6th constraints allow us to ensure that no 微信公众号：数学模型 flooding or dangerously-low water levels occur. To capture the fact that dams can only let out so much water at a time, we introduce the 7th and 8th constraints to bound the amount of water we can let out of the dams. Lastly, we track the flow in the St. Lawrence River with the 9th constraint.

<!-- b000205 | heading | pages [9] -->
2.4 Methods for Stakeholder Management

<!-- b000206 | prose | pages [9] -->
As ĲC notes, this problem is particularly difficult because of the often-conflicting requests from the various stakeholders around the Lake Ontario and St. Lawrence River regions. Our algorithm provides a method to weight stakeholder interests, however, it relies on the practitioner to assign these weights manually. This has the potential to create divides between groups of stakeholders. Thus, some sort of heuristic should be used to equitably assign these weights on a per-stakeholder basis. 微信号：MATHmodels We propose the following methodology to determine fair weightings between ideal water level curves:

<!-- b000207 | prose | pages [9] -->
• We create an initial set of weights 𝑤0 and set them as parameters in the model.

<!-- b000208 | prose | pages [9] -->
• Then we simulate roughly five months2, and observe the forecasted ideal water levels.

<!-- b000209 | prose | pages [9] -->
• We then proceed with the schedule for two months.

<!-- b000210 | prose | pages [9] -->
We simulate beyond the necessary time horizon to ensure that our model accounts for future impacts of flows in the other lakes. In particular, we designate a three-month buffer since this is the time taken for an effect in Lake Superior to be observed in Lake Ontario.

<!-- b000211 | prose | pages [9] -->
After adopting the given schedule for the two month period, we calculate the net error between the real observed water levels and the ideal curves provided per stakeholder.

<!-- b000212 | prose | pages [9] -->
∑︁ 𝜀𝑖= |ℎ𝑡−ˆℎ𝑡| 𝑡∈[1, 60] 𝑡

<!-- b000213 | prose | pages [9] -->
This gives us per-stakeholder errors {𝜀1, . . . 𝜀𝑛} for 𝑛stakeholders. Note that higher values of 𝜀𝑖correspond to a lower level of stakholder 𝑖’s satisfaction. Keeping this in mind, we can reassign weights for the next time horizon with

<!-- b000214 | prose | pages [9] -->
𝜀𝑖 𝑤1𝑖= 𝑘𝜀𝑘 Í

<!-- b000215 | prose | pages [9] -->
That is, the new stakeholder weights are their normalized net errors from the last time period. This allows stakeholders that had greater deviations to be prioritized during the next time period.

<!-- b000216 | prose | pages [9] -->
2The chosen time horizon is left up to the practitioner, but we recommend choosing one of the same order. I.e. 2-6 months

<!-- b000217 | furniture | pages [9] -->
关注数学模型

<!-- b000218 | furniture | pages [9] -->
2

<!-- b000219 | furniture | pages [9] -->
MATHmodels

<!-- b000220 | furniture | pages [9] -->
获取更多资讯

<!-- b000221 | furniture | pages [10] -->
Team # 2429211

<!-- b000222 | furniture | pages [10] -->
Page 10 of 24

<!-- b000223 | heading | pages [10] -->
2.5 Data-Based Model Of The Hydrosphere

<!-- b000224 | prose | pages [10] -->
Modeling the movement of water in the Great Lakes is difficult and requires a number of assumptions to make the problem tractable. To ground our model in reality we used a data-based 微信公众号：数学模型 approach to determine time lag, flow rates out of lakes, and other sources of water outside of the flow between the lakes.

<!-- b000225 | prose | pages [10] -->
We first needed to approximate the time lags between the lakes for our LP to create dam schedules. For instance, we needed to know that it takes roughly two months for the effect of a flow in Lake Michigan to be observed in Lake Ontario. To identify the latencies, we used time-lagged cross correlation on the provided water level time series to find where the correlation is maximized. For example, the time-lagged cross-correlation between the water levels in Lake Superior and Lake Michigan is given by Figure 5.

<!-- b000226 | prose | pages [10] -->
Time lagged cross-correlation between Lake Erie and Lake Ontario Time lagged cross-correlation between Lake Huron and Lake Erie 0.7 0.90 微信号：MATHmodels 0.6

<!-- b000227 | prose | pages [10] -->
0.85 0.5

<!-- b000228 | prose | pages [10] -->
Correlation Correlation 0.4 0.80 0.3

<!-- b000229 | prose | pages [10] -->
0.75 0.2

<!-- b000230 | prose | pages [10] -->
0.1 0.70 0.0

<!-- b000231 | prose | pages [10] -->
−0.1 0.65 0 −10 −5 5 10 0 −10 −5 5 10 Time lag (months) Time lag (months)

<!-- b000232 | caption | pages [10] -->
Figure 5: Time lagged cross-correlation examples for between Lake Huron and Erie and between

<!-- b000233 | prose | pages [10] -->
Lake Erie and Ontario computed from the dataset given for Problem D in [1].

<!-- b000234 | prose | pages [10] -->
The correlation is maximized at a time lag of 1. Thus, we can interpret that a flow in Lake Superior will take approximately a month to propagate in Lake Michigan. The full matrix of these time-lagged correlations is given by Table 1.

<!-- b000235 | prose | pages [10] -->
Sup. Mich + Huron Erie Ont.

<!-- b000236 | prose | pages [10] -->
Sup. 0 1 3 3 Mich. + Huron -1 0 1 2 Erie -3 -2 0 0 Ont. -3 -2 0 0

<!-- b000237 | caption | pages [10] -->
Table 1: Time lag matrix between the Great Lakes

<!-- b000238 | prose | pages [10] -->
Additionally, we used the datasets to run a linear regression, pictured in figure 6, to obtain the flow rates as a function of the height of the lake, which we will use to model the flow in and out of the lakes. We suspect this to be true because if we approximate flow using Bernoulli’s principle in fluid mechanics, we find that by expanding for small oscillations we will have locally linear results.

<!-- b000239 | furniture | pages [10] -->
关注数学模型

<!-- b000240 | furniture | pages [10] -->
2

<!-- b000241 | furniture | pages [10] -->
MATHmodels

<!-- b000242 | furniture | pages [10] -->
获取更多资讯

<!-- b000243 | furniture | pages [11] -->
Team # 2429211

<!-- b000244 | furniture | pages [11] -->
Page 11 of 24

<!-- b000245 | prose | pages [11] -->
Detroit River ﬂow vs Lake Michigan/Huron height Niagara Riverflow vs Lake Erie height 8000 7500

<!-- b000246 | prose | pages [11] -->
7500 微信公众号：数学模型 7000 3s−1) Detroit River ﬂow (m3s−1) 7000 6500 Niagara river ﬂow ( m 6000 6500

<!-- b000247 | prose | pages [11] -->
5500 6000

<!-- b000248 | prose | pages [11] -->
5000 5500 4500 5000 4000

<!-- b000249 | prose | pages [11] -->
175.50 175.75 176.00 176.25 176.50 176.75 177.00 173.8 177.25 177.50 174.0 174.2 174.4 174.6 174.8 175.0 175.2 Lake Michigan/Huron height (m) Lake Erie height ( m )

<!-- b000250 | caption | pages [11] -->
Figure 6: Flow along the Niagara River and Detroit River as a function of the height (relative to

<!-- b000251 | prose | pages [11] -->
微信号：MATHmodels sea level) of the lakes they flow from. The regression formulae are given by:

<!-- b000252 | prose | pages [11] -->
𝑓Niagara = 2088.917ℎErie −357993.824 with (R2 = 0.928) 𝑓Detroit = 1611.581ℎHuron −278618.674 with (R2 = 0.850)

<!-- b000253 | prose | pages [11] -->
Lastly, we also approximated other aspects of the hydrosphere (precipitation, groundwater, evaporation, and surface runoff) by modeling the inflow of water based on how much it rained because according to the biohydrological database for the Great Lakes makes up 20 percent of the water flowing into the Great Lakes [3]. Using the NOAA data set of rainfall, evaporation, and runoff into the Great Lakes [17], we determined the total inflow that would occur each month based on historical data. We visualize the historical rainfall that occurred during each month in Figure 7.

<!-- b000254 | prose | pages [11] -->
Lake Superior net exogenous ﬂow Lake Ontario net exogenous ﬂow 25p 25p 50p 50p 75p 75p 0.4 0.15 Marginal height (m) Marginal height (m) 0.10 0.3

<!-- b000255 | prose | pages [11] -->
0.05 0.2

<!-- b000256 | prose | pages [11] -->
0.00 0.1

<!-- b000257 | prose | pages [11] -->
−0.05 Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec Month Month

<!-- b000258 | caption | pages [11] -->
Figure 7: 1st (in blue), 2nd (in red), and 3rd (in orange) quartiles of exogenous flow into Lakes

<!-- b000259 | prose | pages [11] -->
Superior and Ontario

<!-- b000260 | furniture | pages [11] -->
关注数学模型

<!-- b000261 | furniture | pages [11] -->
2

<!-- b000262 | furniture | pages [11] -->
MATHmodels

<!-- b000263 | furniture | pages [11] -->
获取更多资讯

<!-- b000264 | furniture | pages [12] -->
Team # 2429211

<!-- b000265 | furniture | pages [12] -->
Page 12 of 24

<!-- b000266 | heading | pages [12] -->
2.6 Additional Considerations

<!-- b000267 | prose | pages [12] -->
Aside from the data-driven parameters we obtained, we considered other parameters to help make our model more realistic: 微信公众号：数学模型 Seasonal Wave Attenuation: To consider the seasonality of the Great Lakes we also add an attenuation factor that reduces the flow between the lakes. We added this factor because a study by Peng Bai showed that ice attenuates the waves in the Great Lakes and thus should reduce their flow from their turbulent effects [4].

<!-- b000268 | prose | pages [12] -->
Fuzzing The Model: Since exogenous inflow is highly random, we added noise to historical inflow data to increase the robustness of our model. This makes the model more robust by removing biases towards certain shores at different water levels and helps us accurately assess the drought and flooding risk factors.

<!-- b000269 | heading | pages [12] -->
3 Microschedule Model

<!-- b000270 | prose | pages [12] -->
微信号：MATHmodels One aspect that our Macroschedule model does not incorporate are the proximal effects of opening the Moses-Saunders Dam. As noted by the problem statement, even small variances in the water level can have drastic implications for stakeholders around Lake Ontario and the St. Lawrence River. As such, it is not enough to know how to release water in a day. It is also important to time outflows when it is generally most beneficial for these stakeholders. We develop a linear program that schedules intra-day outflows to maximize community benefit.

<!-- b000271 | prose | pages [12] -->
Unlike the macroscheduling problem, there is no substantial time lag on flows between nodes in the microscheduling problem. Thus, we can exert more immediate control over the water level and flows in Lake Ontario and the St. Lawrence River. We use a similarly formulated linear program to represent these flows, and the objective of maximizing proximity to ideal water levels and flows. The variables of the problems are defined in the second table of Appendix A

<!-- b000272 | prose | pages [12] -->
And the LP is formulated as follows:

<!-- b000273 | prose | pages [12] -->
∑︁ 𝛼1|ℎ𝑡−ˆℎ𝑡| + 𝛼2| 𝑓𝑡−ˆ𝑓𝑡| minimize 𝑡∈𝑇 ℎ𝑡= ℎ𝑡−1 + 𝐹𝑡−𝑥𝑡 ∀𝑡∈𝑇 subject to 𝑓𝑡= 𝜔𝑓𝑡−1 + 𝑘(1 −𝜔)𝑥𝑡 ∀𝑡∈𝑇 𝑥𝑡≤𝑂 ∀𝑡∈𝑇 ℎ𝑇= ˆ𝐻

<!-- b000274 | prose | pages [12, 13] -->
The first two constraints implement height and flow rate updates in Lake Ontario and the St. Lawrence river respectively. Notice that the second constraint models the river flow rate as a convex combination of inflow from the dam and its prior flow rate. This is influenced by sound physical intuition, but it is difficult to accurately model this parameter based on available data. The third constraint limits total outflow from the dam, and the fourth enforces that a certain amount of water has left Lake Ontario by the end of the day. This ensures that the microscheduler adheres to the daily requirements set forth by the larger schedule. Our proposed synthesis of the macroscheduler and microscheduler is show in Figure 8 Due to lower lag times, the model cansatisfy daily requirements relatively well. This is important because there are likely days when dam usage must be limited to coordinate with monthly schedules. However, the water level can still be modulated to a level where stakeholders can still be largely satisfied. 微信公众号：数学模型 Set Time Horizon

<!-- b000275 | furniture | pages [12] -->
关注数学模型

<!-- b000276 | furniture | pages [12] -->
2

<!-- b000277 | furniture | pages [12] -->
MATHmodels

<!-- b000278 | furniture | pages [12] -->
获取更多资讯

<!-- b000279 | furniture | pages [13] -->
Team # 2429211

<!-- b000280 | furniture | pages [13] -->
Page 13 of 24

<!-- b000282 | prose | pages [13] -->
Macroscheduler Microscheduler

<!-- b000283 | prose | pages [13] -->
Manage Stakeholder Find Ideal Curves Expectations

<!-- b000284 | prose | pages [13] -->
微信号：MATHmodels Fit Micro Fit Macro Approve Parameters Parameters

<!-- b000285 | prose | pages [13] -->
Test & Determine Generate Schedule Generate Schedule Robustness

<!-- b000286 | prose | pages [13] -->
Collect Data Improve Model

<!-- b000287 | caption | pages [13] -->
Figure 8: The pipeline for using our control algorithms.

<!-- b000288 | heading | pages [13] -->
4 Model Insights

<!-- b000289 | prose | pages [13] -->
Here we outline a brief overview of the main insights of our model:

<!-- b000290 | prose | pages [13] -->
• Effectively managing Lake Ontario means effectively Managing Lake Superior. Lake Supe- rior is able to influence Lake Ontario after a significant time delay which makes proactive scheduling at Lake Superior able to create desirable water levels at Lake Ontario.

<!-- b000291 | prose | pages [13] -->
• Our model successfully achieves the desired water levels in most lakes even with varying degrees of rainfall.

<!-- b000292 | prose | pages [13] -->
• After determining optimal water levels through our macro-schedule algorithm, our micro- schedule algorithm is able to determine realistic and effective schedules for scheduling a dam during any particular day.

<!-- b000293 | furniture | pages [13] -->
关注数学模型

<!-- b000294 | furniture | pages [13] -->
2

<!-- b000295 | furniture | pages [13] -->
MATHmodels

<!-- b000296 | furniture | pages [13] -->
获取更多资讯

<!-- b000297 | furniture | pages [14] -->
Team # 2429211

<!-- b000298 | furniture | pages [14] -->
Page 14 of 24

<!-- b000299 | heading | pages [14] -->
4.1 Dynamic Control Of The System

<!-- b000300 | prose | pages [14] -->
Most dams use a heuristic approach for dam scheduling called rule curves. That is, dams are given fixed schedules depending on water level and precipitation thresholds. While our model is 微信公众号：数学模型 amenable to producting rule curves, we believe that the dynamic nature of scheduling makes it superior to this approach.

<!-- b000301 | prose | pages [14] -->
One of the most critical aspects of the model is that it can make decisions by “looking ahead”. That is, given a range of forecasts, the model can schedule flows that are both robust to climate events and still satisfy the needs of stakeholders. This way, action can be taken to mitigate potential crises well before they actually occur.

<!-- b000302 | prose | pages [14] -->
After we “look ahead” we can then use a combination of the macroscheduler and microscheduler model to forecast both the four-month time horizon and then locally on the daily horizon. By modeling both of these time horizons, we gain valuable insights on the importance of factoring in the time lags to forecasting the dam schedules. The efficacy of our model is shown in Figure 9:

<!-- b000303 | prose | pages [14] -->
微信号：MATHmodels Microscheduler ﬂow error rate

<!-- b000304 | prose | pages [14] -->
1.4

<!-- b000305 | prose | pages [14] -->
1.2

<!-- b000306 | prose | pages [14] -->
1.0 Error (%) 0.8

<!-- b000307 | prose | pages [14] -->
0.6

<!-- b000308 | prose | pages [14] -->
0.4

<!-- b000309 | prose | pages [14] -->
0.2

<!-- b000310 | prose | pages [14] -->
0.0 0 5 10 15 20 Hour

<!-- b000311 | caption | pages [14] -->
Figure 9: Plot of the percent error between ideal flow and the flow achieved by the microscheduler

<!-- b000312 | prose | pages [14] -->
after the optimal water levels were determined by the macroscheduling algorithm.

<!-- b000313 | furniture | pages [14] -->
关注数学模型

<!-- b000314 | furniture | pages [14] -->
2

<!-- b000315 | furniture | pages [14] -->
MATHmodels

<!-- b000316 | furniture | pages [14] -->
获取更多资讯

<!-- b000317 | furniture | pages [15] -->
Team # 2429211

<!-- b000318 | furniture | pages [15] -->
Page 15 of 24

<!-- b000319 | heading | pages [15] -->
4.2 Robustness to Severe Climate Events

<!-- b000320 | prose | pages [15] -->
We tested the schedules produced by our control algorithm using past rain/runoff/evap- Quartile 1 微信公众号：数学模型 oration data collected from [17]. We deter- Superior mined the average amount of total rain, runoff, Huron/Michigan 176.5 183.4 and evaporation for each month from 1980 to 176.4 Water Height 176.3 183.2 2020. Due to the fact that our model uses 176.2 a time-step of one day and the data available 183.0 176.1 176.0 form [17] tracks how much rain/runoff/evap- 182.8 175.9 oration occurred each month, we determined 175.8 182.6 175.7 how much it rained per day by running a cu- Ontario Erie bic spline through the historical averages and 174.5 then dividing the value for total rain, runoff, 75.0 174.4 Water Height and evaporation by 30 to account for the fact 74.8 174.3 that the month data was the total over a month 74.6 微信号：MATHmodels 174.2 (roughly 30 days). This allows us to capture the 74.4 174.1 natural patterns of rain, runoff, and evaporation 74.2 174.0 while making the data usable in our model. We 0 50 100 150 200 250 300 350 0 50 100 150 200 250 300 350 Days Days ran a similar procedure to determine the 25th Qaurtile 2 and 75th percentile amount of rain, runoff, and Huron/Michigan Superior evaporation that occurred on each day.

<!-- b000321 | prose | pages [15] -->
176.5 183.4 After obtaining these rain values, we ran our 176.4 Water Height 176.3 183.3 linear program using the historic rain level (ei- 176.2 ther the 25th, 50th or 75th percentile) at body of 183.2 176.1 water 𝑖during time 𝑡for the 𝑟𝑖,𝑡parameter. The 183.1 176.0

<!-- b000322 | prose | pages [15] -->
175.9 time horizon for these experiments was set to a 183.0 175.8 year and the ideal water was determined using 182.9 Erie Ontario the techniques in Section 2.2. The water levels 174.50 achieved by the model are shown in Figures 10 75.1 174.45 75.0 Water Height and 11. 174.40 74.9 174.35 74.8 We observe that the Lake Ontario water lev- 174.30 74.7 els are very consistent across different levels of 174.25 74.6 174.20 74.5 total rain, runoff, and evaporation while Lake 174.15 74.4 Superior’s levels are not. This demonstrates 0 50 100 150 200 250 300 350 0 50 100 150 200 250 300 350 Days that effectively scheduling Lake Superior is cru- Days cial to having desirable water levels at Lake On-

<!-- b000323 | caption | pages [15] -->
Figure 10: Plots of the 1st and 2nd quartiles of the

<!-- b000324 | prose | pages [15] -->
tario. The types of schedules that are required in water levels in each of the Great Lakes drawn from Lake Superior to create desirable water levels at the historic rain data. The water levels achieved Lake Ontario are non-robust to severe changes by the model are shown with dotted blue lines and in total inflow to the Great Lakes, but the water the ideal water levels with solid orange lines. levels in the rest of the Great Lakes are indeed robust to climate events.

<!-- b000325 | furniture | pages [15] -->
关注数学模型

<!-- b000326 | furniture | pages [15] -->
2

<!-- b000327 | furniture | pages [15] -->
MATHmodels

<!-- b000328 | furniture | pages [15] -->
获取更多资讯

<!-- b000329 | furniture | pages [16] -->
Team # 2429211

<!-- b000330 | furniture | pages [16] -->
Page 16 of 24

<!-- b000331 | prose | pages [16] -->
Quartile 3 Superior Huron/Michigan 183.45 176.5 微信公众号：数学模型 183.40 176.4 Water Height 183.35 176.3

<!-- b000332 | prose | pages [16] -->
183.30 176.2

<!-- b000333 | prose | pages [16] -->
183.25 176.1

<!-- b000334 | prose | pages [16] -->
183.20 176.0

<!-- b000335 | prose | pages [16] -->
Ontario Erie

<!-- b000336 | prose | pages [16] -->
174.6 75.1

<!-- b000337 | prose | pages [16] -->
75.0 Water Height 174.5 74.9 微信号：MATHmodels 174.4 74.8

<!-- b000338 | prose | pages [16] -->
74.7 174.3

<!-- b000339 | prose | pages [16] -->
74.6 174.2

<!-- b000340 | prose | pages [16] -->
0 50 100 150 200 250 300 350 0 50 100 150 200 250 300 350 Days Days

<!-- b000341 | caption | pages [16] -->
Figure 11: Plots of achieved water levels using the third quartile rain data (extreme rain). The water

<!-- b000342 | prose | pages [16] -->
levels achieved by the model are shown with dotted blue lines and the ideal water levels are shown with solid orange lines.

<!-- b000343 | heading | pages [16] -->
5 Sensitivity Analysis

<!-- b000344 | prose | pages [16] -->
Since our model is primarily mechanistic, it relies heavily on parameters that represent real-life values such as flow rates, flow decay, and attenuation. As such, it is reasonable to observe how the model’s output changes as we modulate some of these parameters. Specifically, we vary 𝜔–the St. Lawrence river flow decay rate.

<!-- b000345 | prose | pages [16] -->
Moreover, we determine that it is possible to avoid flooding and dangerously low water levels while achieving desirable water levels in all lakes even with varying degrees of total inflow to the lakes. This demonstrates the value of our linear programming approach as a valuable tool to determine dam schedules.

<!-- b000346 | prose | pages [16] -->
The value that was used in the final model was 0.8. This was chosen based off observing flows in the St. Lawrence River and how they change with respect to the height of Lake Ontario. However, since there isn’t data on the status of the dam at these times, this link is admittedly tenuous. Thus, we decided to observe the effects of modulating this parameter on the net flow error in the St. Lawrence River. That is, with different decay rates, we measure how hard is it for our control algorithm to match the desired flow rate in the St. Lawrence River.

<!-- b000347 | furniture | pages [16] -->
关注数学模型

<!-- b000348 | furniture | pages [16] -->
2

<!-- b000349 | furniture | pages [16] -->
MATHmodels

<!-- b000350 | furniture | pages [16] -->
获取更多资讯

<!-- b000351 | furniture | pages [17] -->
Team # 2429211

<!-- b000352 | furniture | pages [17] -->
Page 17 of 24

<!-- b000353 | prose | pages [17] -->
We uniformly vary the parameter 𝜔in the range [0.7, 0.825] and observe the net error rate. We see that:

<!-- b000354 | prose | pages [17] -->
Yearly average ﬂow error based on ω 微信公众号：数学模型 1000

<!-- b000355 | prose | pages [17] -->
980 Net ﬂow error 960

<!-- b000356 | prose | pages [17] -->
940

<!-- b000357 | prose | pages [17] -->
920 0.70 0.72 0.74 0.76 0.78 0.80 0.82 ω 微信号：MATHmodels

<!-- b000358 | caption | pages [17] -->
Figure 12: Flow in the St. Lawrence River is sensitive to 𝜔

<!-- b000359 | prose | pages [17] -->
The error here varies quite significantly. In some sense, this is not surprising. Complex systems such as the Great Lakes are very sensitive to slight physical changes. To maximize the effectiveness of the model, it is therefore important to be able to measure these parameters accurately, and provide them to the model with high-resolution.

<!-- b000360 | prose | pages [17] -->
In conclusion, the model is largely robust to changes in climate forecasting. However, due to its mechanistic nature, it is quite sensitive to parameters describing natural and artificial flow processes.

<!-- b000361 | heading | pages [17] -->
6 Conclusions

<!-- b000362 | prose | pages [17] -->
• Our model demonstrates that to effectively manage Lake Ontario, the ĲC must also effectively manage Lake Superior. Lake Superior has the capacity to send large amounts of water to Lake Ontario. While the time it takes for Lake Ontario to feel the effects of actions taken at Lake Superior, by proactively increasing the water sent from Lake Superior, Lake Ontario can more effectively manage its water levels.

<!-- b000363 | prose | pages [17] -->
• Dam schedules will consistently make tradeoffs betweeen flood/drought security and stake- holder satisfaction. It is important to manage stakeholder expectations and use equitable prioritization methods to ensure overall contentedness.

<!-- b000364 | prose | pages [17] -->
• Testing schedules against different severities of exogenous inflow yield outcomes that are significantly more robust to climate and hydrologic events. Regardless of the scheduling algorithm, plans should always be tested against real historical inflows as well as randomly simulated climate events.

<!-- b000365 | furniture | pages [17] -->
关注数学模型

<!-- b000366 | furniture | pages [17] -->
2

<!-- b000367 | furniture | pages [17] -->
MATHmodels

<!-- b000368 | furniture | pages [17] -->
获取更多资讯

<!-- b000369 | furniture | pages [18] -->
Team # 2429211

<!-- b000370 | furniture | pages [18] -->
Page 18 of 24

<!-- b000371 | heading | pages [18] -->
6.1 Strengths

<!-- b000372 | prose | pages [18] -->
1. Due the speed of solving linear programs, our model can be employed to develop schedules for a large number of potential forecasts and ideal water levels. This allows practitioners to 微信公众号：数学模型 be more prepared for extreme weather events by being able to prep schedules for best-case, worst-case, and average-case weather events. If it becomes evident that the environmental data that the dam control schedule was created from is poor, a new schedule can be quickly substituted in to mitigate damage.

<!-- b000373 | prose | pages [18] -->
2. Our control algorithms can effectively meet stakeholder demands while the water levels re- main close to historical averages. The Great Lakes water system needs to flow naturally while still accounting for the demands of stakeholders, so our model must meet this benchmark.

<!-- b000374 | prose | pages [18] -->
3. Due to the constrained nature of our control algorithms, practitioners will always be aware of the maximum and minimum water levels that are produced by the schedule. Since actions taken at Lake Superior affect Lake Ontario with a severe delay, there is an associated risk 微信号：MATHmodels with increasing or decreasing the flow through the Compensating Works dam. Our control algorithms allow for practitioners to predict the effect of the schedules they implement.

<!-- b000375 | prose | pages [18] -->
4. Our model is extremely flood and drought-resistant. In our analysis using realistic precipita- tion data our model didn’t experience any droughts or floods.

<!-- b000376 | heading | pages [18] -->
6.2 Weaknesses

<!-- b000377 | prose | pages [18] -->
Practitioners need to be aware of the flaws of our model so that unexpected results from our control algorithms can be mitigated. The weaknesses of our model are as follows:

<!-- b000378 | prose | pages [18] -->
• Due to the mechanistic nature of our model, the schedule of the model is noticeably sensitive to changes in parameters related to natural processes. For example, if the rate of flow decay in the St. Lawrence River is poorly measured, the model will produce a schedule that differs slightly, but noticeably, from the true ideal schedule. Practitioners should be aware of this flaw and apply the model several times with varying values for parameters like the decay rate and rain schedule. While the schedule will be sensitive to poor measurements, it will provide valuable insights into how to best manage the dams.

<!-- b000379 | prose | pages [18] -->
• Our model assumes a linear relationship between the height of a body of water and the total outflow which may change over time as the landscape of the Great Lakes changes. To account for this, practitioners should routinely track the relationship between the height of each lake and the observed flows of each lake’s distributaries.

<!-- b000380 | prose | pages [18] -->
• Due to the constraints placed on flooding and dangerously low water levels, our model will occasionally determine that an adequate schedule is possible. If practitioners encounter this issue when using our proposed control algorithms, they must choose the location and extent of flooding that will necessarily occur. We believe that no model can completely avoid flooding, so we believe that our model’s ability to have controlled and predictable flooding is sufficiently safe.

<!-- b000381 | furniture | pages [18] -->
关注数学模型

<!-- b000382 | furniture | pages [18] -->
2

<!-- b000383 | furniture | pages [18] -->
MATHmodels

<!-- b000384 | furniture | pages [18] -->
获取更多资讯

<!-- b000385 | furniture | pages [19] -->
Team # 2429211

<!-- b000386 | furniture | pages [19] -->
Page 19 of 24

<!-- b000387 | heading | pages [19] -->
7 Future Exploration

<!-- b000388 | prose | pages [19] -->
To address some of the weaknesses we identified, we believe that our model could be expanded in the following ways: 微信公众号：数学模型

<!-- b000389 | prose | pages [19] -->
• Pull from more refined data: By pulling from more refined data, our model would have more accurate information hydrological information. As a result, our model could improve the mechanistic nature of our model.

<!-- b000390 | prose | pages [19] -->
• Safety Optimizer: Another extension of our model could be using the results from running many fuzzy trials to determine which dam schedule is optimal against random weather conditions. This would allow practitioners to understand the risk assosiated with the schedules they select.

<!-- b000391 | prose | pages [19] -->
• Create an algorithm to determine which stakeholders to prioritize. The time of year has a large effect on the possibility of pleasing any particular stakeholder. A future direction of 微信号：MATHmodels this work would be to implement the time of year into our weighting of the stakeholders.

<!-- b000392 | furniture | pages [19] -->
关注数学模型

<!-- b000393 | furniture | pages [19] -->
2

<!-- b000394 | furniture | pages [19] -->
MATHmodels

<!-- b000395 | furniture | pages [19] -->
获取更多资讯

<!-- b000396 | furniture | pages [20] -->
Team # 2429211

<!-- b000397 | furniture | pages [20] -->
Page 20 of 24

<!-- b000398 | heading | pages [20] -->
8 Memo To The ĲC

<!-- b000399 | prose | pages [20] -->
Dear ĲC Leadership,

<!-- b000400 | prose | pages [20] -->
微信公众号：数学模型 In light of the successes and failures experienced by Plan 2014 in regards to controlling the Moses-Saunders dam at Lake Ontario, we developed two linear programming-based control algorithms to effectively determine how to jointly manage the Compensating Works Dam at Lake Superior and the Moses-Saunders Dam at Lake Ontario to achieve ideal water levels throughout the Great Lakes. We believe that our algorithms build off of the adaptive control approach that Plan 2014 has successfully implemented while avoiding the limitations of Plan 2014 that have allowed for flooding in recent years.

<!-- b000401 | prose | pages [20] -->
In our model, we employ linear programming and a series of algorithms that forecast the needs of the stakeholders to determine how much we need to open dams at Lake Superior and Ontario. Because we are using a linear program, our model can simulate hundreds of thousands of scenarios within a few minutes, this would allow for the ĲC to have a more holistic approach to assessing the risks of running certain dam schedules for their stakeholders. Our algorithm for determining 微信号：MATHmodels the optimal levels of stakeholders is based on their desires outlined in the ĲC report and draws from historical water levels [10]. Our model also utilizes historical data to simulate natural processes in the hydrosphere in the following ways:

<!-- b000402 | prose | pages [20] -->
• We account for the time it takes water to flow between lakes. We were able to correlate the water level data between different lakes to estimate the time it taken for flows to propagate through the system.

<!-- b000403 | prose | pages [20] -->
• We use a data-driven approach to determine flow rates of naturally flowing sources. More- over, using the data available to us, we found a strong linear relationship between height and the rate and which water flows out.

<!-- b000404 | prose | pages [20] -->
• Our model accounts for various levels of rainfall and other hydrological processes. We utilized a combination of precipitation from NOAA and preexisting models to get randomized, but representative rain data to run our situations [17] [22].

<!-- b000405 | prose | pages [20] -->
To show the resilience of our model we ran it under various extreme climate events and found it was effective in preventing floods and droughts. Specifically, the way our algorithms achieve near-optimal water levels even with severe climate events is by creatively managing Lake Superior. By incorporating the relationship between Lake Superior and Lake Ontario into our model, we are able to achieve schedules that allow Lake Ontario to remain safe and beneficial to the stakeholders.

<!-- b000406 | prose | pages [20] -->
We believe that our model provides the ĲC with valuable insights about how to best manage the Compensating Works and Sault. St. Marie dams. Our model will allow the ĲC to use the most recent sets of data being gathered at the monitoring points along the Great Lakes and adapt an optimal dam schedule based on current conditions and predictive forecasts.

<!-- b000407 | prose | pages [20, 21] -->
Thank you for your consideration, A

<!-- b000408 | furniture | pages [20] -->
Team #2429211

<!-- b000409 | furniture | pages [20] -->
关注数学模型

<!-- b000410 | furniture | pages [20] -->
2

<!-- b000411 | furniture | pages [20] -->
MATHmodels

<!-- b000412 | furniture | pages [20] -->
获取更多资讯

<!-- b000413 | furniture | pages [21] -->
Team # 2429211

<!-- b000414 | furniture | pages [21] -->
Page 21 of 24

<!-- b000416 | heading | pages [21] -->
Notation

<!-- b000417 | prose | pages [21] -->
Name Type Description.

<!-- b000418 | prose | pages [21] -->
微信公众号：数学模型 𝑇 Set Set of time-steps.

<!-- b000419 | prose | pages [21] -->
𝐵 Set Set of Bodies of Water.

<!-- b000420 | prose | pages [21] -->
𝑥𝑡 Height of water let through the Sault St. Marie Dam at time 𝑡. Variable 𝑦𝑡 Height of water let through the Moses-Saunders Dam at time 𝑡. Variable 𝑓𝑡 Flow at River Lawrence at time 𝑡. Variable ℎ𝑖,𝑡 Height of water in body of water 𝑖at time 𝑡. Variable 𝜔𝑖 Weighting term for the objective function. High 𝜔𝑖 Parameter 𝑟𝑖,𝑡 The total height added by environmental factors in body of water 𝑖at time 𝑡. Parameter 微信号：MATHmodels 𝑠𝑖 The surface area of body of water 𝑖. Parameter 𝛼𝑖 Parameter Determined slope from regression.

<!-- b000421 | prose | pages [21] -->
𝛽𝑖 Parameter Determined bias from regression.

<!-- b000422 | prose | pages [21] -->
𝐿 Parameter Lag time between specified bodies of water.

<!-- b000423 | prose | pages [21] -->
𝐹𝑖 Height of water required for a flood at body of water 𝑖. Parameter 𝐷𝑖 Height required for dangerously low water at body of water 𝑖. Parameter 𝑀1 Parameter Maximum height of water releasable from Lake Superior during a time-step.

<!-- b000424 | prose | pages [21] -->
𝑀2 Parameter Maximum height of water releasable from Lake Ontario during a time-step 𝑤 Parameter Influence of the Mosses-Saunders Dam on the flow of the St. Lawrence River

<!-- b000425 | caption | pages [21] -->
Table 2: Description of variables involed in the mathematical program used to determine dam

<!-- b000426 | prose | pages [21, 22] -->
schedules. All heights are in meters, all flows are in cubic meters per second, and all areas are given meters squared, all lag times are given in days Name Type Description.

<!-- b000427 | furniture | pages [21] -->
关注数学模型

<!-- b000428 | furniture | pages [21] -->
2

<!-- b000429 | furniture | pages [21] -->
MATHmodels

<!-- b000430 | furniture | pages [21] -->
获取更多资讯

<!-- b000431 | furniture | pages [22] -->
Team # 2429211

<!-- b000432 | furniture | pages [22] -->
Page 22 of 24

<!-- b000434 | prose | pages [22] -->
𝐵𝑖 Set Bodies of water (Ontario, St. Lawrence) 微信公众号：数学模型 𝑇 Param Time Horizon 𝐹𝑡 Param Hourly inflow into Lake Ontario ˆℎ𝑡 Param Ideal water levels ˆ𝑓𝑡 Param Ideal flow levels 𝑘 Param Flow conversion coefficient 𝑙𝑖 Param Initial water and flow levels 𝛼𝑖 Param Weights for stakeholder importance 𝜔 Param Hourly flow decay coefficient 微信号：MATHmodels 𝑂 Param Dam outflow limit ˆ𝐻 Param Final water height ℎ𝑡 Variable Water level 𝑓𝑡 Variable Flow level 𝑥𝑡 Variable Moses-Saunders Dam outflow

<!-- b000435 | caption | pages [22] -->
Table 3: Microschedule LP formulation. All water levels are heights in meters, all times are in

<!-- b000436 | prose | pages [22] -->
hours, and all flows are in cubic meters per second

<!-- b000437 | furniture | pages [22] -->
关注数学模型

<!-- b000438 | furniture | pages [22] -->
2

<!-- b000439 | furniture | pages [22] -->
MATHmodels

<!-- b000440 | furniture | pages [22] -->
获取更多资讯

<!-- b000441 | furniture | pages [23] -->
Team # 2429211

<!-- b000442 | furniture | pages [23] -->
Page 23 of 24

<!-- b000443 | heading | pages [23] -->
References

<!-- b000444 | references | pages [23] -->
[1] 2024MCM/ICM Problems. https://www.immchallenge.org/mcm/index.html.

<!-- b000445 | references | pages [23] -->
[2] International Joint Commission (2014). Lake Ontario St. Lawrence River Plan 201: Protecting

<!-- b000446 | references | pages [23] -->
微信公众号：数学模型

<!-- b000447 | references | pages [23] -->
against extreme water levels, restoring wetlands and preparing for climate change, 2014.

<!-- b000448 | references | pages [23] -->
[3] US army Corps of Engineers. John glenn great lakes basin program biohydrological informa-

<!-- b000449 | references | pages [23] -->
tion base, 2007.

<!-- b000450 | references | pages [23] -->
[4] Peng Bai, Jia Wang, Philip Chu, Nathan Hawley, Ayumi Fujisaki-Manome, James Kessler,

<!-- b000451 | references | pages [23] -->
Brent M Lofgren, Dmitry Beletsky, Eric J Anderson, and Yaru Li. Modeling the ice-attenuated

<!-- b000452 | references | pages [23] -->
waves in the great lakes. Ocean Dynamics, 70:991–1003, 2020.

<!-- b000453 | references | pages [23] -->
[5] Chiranjib Bhowmik, Sumit Bhowmik, Amitava Ray, and Krishna Murari Pandey. Optimal

<!-- b000454 | references | pages [23] -->
green energy planning for sustainable development: A review. Renewable and Sustainable

<!-- b000455 | references | pages [23] -->
Energy Reviews, 71:796–813, 2017.

<!-- b000456 | references | pages [23] -->
[6] Thomas Bläsius, Adrian Feilhauer, and Jannik Westenfelder.

<!-- b000457 | references | pages [23] -->
Dynamic flows with time-

<!-- b000458 | references | pages [23] -->
dependent capacities, 2023.

<!-- b000459 | references | pages [23] -->
微信号：MATHmodels

<!-- b000460 | references | pages [23] -->
[7] Murray Clamen and Daniel Macfarlane. Plan 2014: The historical evolution of lake ontario–

<!-- b000461 | references | pages [23] -->
Canadian Water Resources Journal/Revue canadienne des

<!-- b000462 | references | pages [23] -->
st. lawrence river regulation.

<!-- b000463 | references | pages [23] -->
ressources hydriques, 43(4):416–431, 2018.

<!-- b000464 | references | pages [23] -->
[8] Great Lakes Commission.

<!-- b000465 | references | pages [23] -->
[9] International Joint Commission. Options for managing lake ontario and st. lawrence river

<!-- b000466 | references | pages [23] -->
water levels and flows (final report), 2006.

<!-- b000467 | references | pages [23] -->
[10] International Joint Commission. Section 5: Impacts on various interests, 2023.

<!-- b000468 | references | pages [23] -->
[11] George B Dantzig. Linear programming. History of mathematical programming, pages

<!-- b000469 | references | pages [23] -->
19–31, 1991.

<!-- b000470 | references | pages [23] -->
[12] Jean-Luc Desgranges, Joel Ingram, Bruno Drolet, Jean Morin, Caroline Savage, and Daniel

<!-- b000471 | references | pages [23] -->
Borcard. Modelling wetland bird response to water level changes in the lake ontario–st.

<!-- b000472 | references | pages [23] -->
lawrence river hydrosystem. Environmental monitoring and assessment, 113:329–365, 2006.

<!-- b000473 | references | pages [23] -->
[13] Google Earth. Great lakes, no clouds, 2010.

<!-- b000474 | references | pages [23] -->
[14] Lester Randolph Ford. Flows in networks. 2015.

<!-- b000475 | references | pages [23] -->
[15] Inga Kanoshina, Urmas Lips, and Juha-Markku Leppänen. The influence of weather con-

<!-- b000476 | references | pages [23] -->
ditions (temperature and wind) on cyanobacterial bloom development in the gulf of finland

<!-- b000477 | references | pages [23] -->
(baltic sea). Harmful Algae, 2(1):29–41, 2003.

<!-- b000478 | references | pages [23] -->
[16] Frank Millerd. The economic impact of climate change on canadian commercial navigation

<!-- b000479 | references | pages [23] -->
on the great lake. Canadian Water Resources Journal, 30(4):269–280, 2005.

<!-- b000480 | references | pages [23] -->
[17] NOAA. Noaa glerl data, 2021.

<!-- b000481 | references | pages [23] -->
[18] National Oceanic and Atmospheric Administration. Great lakes ecoregion - national oceanic

<!-- b000482 | references | pages [23] -->
and atmospheric administration, 2019.

<!-- b000483 | references | pages [23] -->
[19] Frank J Rahel and Julian D Olden. Assessing the effects of climate change on aquatic invasive

<!-- b000484 | references | pages [23] -->
species. Conservation biology, 22(3):521–533, 2008.

<!-- b000485 | furniture | pages [23] -->
关注数学模型

<!-- b000486 | furniture | pages [23] -->
2

<!-- b000487 | furniture | pages [23] -->
MATHmodels

<!-- b000488 | furniture | pages [23] -->
获取更多资讯

<!-- b000489 | furniture | pages [24] -->
Team # 2429211

<!-- b000490 | furniture | pages [24] -->
Page 24 of 24

<!-- b000491 | references | pages [24] -->
[20] Charles S. Revelle, Daniel P. Loucks, and Walter R. Lynn. Linear programming applied to

<!-- b000492 | references | pages [24] -->
water quality management. Water Resources Research, 4(1):1–9, 1968.

<!-- b000493 | references | pages [24] -->
[21] Michael H Veatch. Linear and convex optimization: A Mathematical Approach. John Wiley

<!-- b000494 | references | pages [24] -->
微信公众号：数学模型

<!-- b000495 | references | pages [24] -->
& Sons, 2020.

<!-- b000496 | references | pages [24] -->
[22] Daniel S Wilks and Robert L Wilby. The weather generation game: a review of stochastic

<!-- b000497 | references | pages [24] -->
weather models. Progress in physical geography, 23(3):329–357, 1999.

<!-- b000498 | references | pages [24] -->
微信号：MATHmodels

<!-- b000499 | furniture | pages [24] -->
关注数学模型

<!-- b000500 | furniture | pages [24] -->
2

<!-- b000501 | furniture | pages [24] -->
MATHmodels

<!-- b000502 | furniture | pages [24] -->
获取更多资讯

<!-- b000503 | furniture | pages [25] -->
Team # 2429211

<!-- b000504 | references | pages [25] -->
Page 25

<!-- b000505 | heading | pages [25] -->
Report on Use of AI

<!-- b000506 | ai_disclosure | pages [25] -->
Dear ICM Judges,

<!-- b000507 | ai_disclosure | pages [25] -->
微信公众号：数学模型

<!-- b000508 | ai_disclosure | pages [25] -->
No AI was used in the writing, code, or development of this project.

<!-- b000509 | ai_disclosure | pages [25] -->
We wish you the best.

<!-- b000510 | ai_disclosure | pages [25] -->
微信号：MATHmodels

<!-- b000511 | furniture | pages [25] -->
关注数学模型

<!-- b000512 | furniture | pages [25] -->
2

<!-- b000513 | furniture | pages [25] -->
MATHmodels

<!-- b000514 | furniture | pages [25] -->
获取更多资讯
