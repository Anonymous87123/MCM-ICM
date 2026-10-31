# P-D-2023-2304962-b6a95eaf

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Problem Chosen D 2023 MCM/ICM Summary Sheet Team Control Number 2304962

<!-- b000002 | title | pages [1] -->
Connecting the Dots: Unpacking the Network Systems of SDGs

<!-- b000003 | heading | pages [1] -->
Summary

<!-- b000004 | prose | pages [1] -->
The Sustainable Development Goals are not just a call to action, but a vision of hope for a better world where all people can thrive, nature can flourish, and societies can prosper in harmony with one another. To achieve sustainable development, it is critical to study relationship between SDGs and select the most effective priority goals.

<!-- b000005 | prose | pages [1] -->
For problem one, A multi-layer network approach was employed to establish a model for analyzing the interrelationships and impacts of SDGs, which improved upon the UN’s goal-target-indicator model by obtaining separate networks for each SDG. The final model was derived by computing the Pearson correlation coefficient matrix and network connections. The network models for 10 regions were visualized, revealing that in the WLD region, SDG8 had a positive impact on other SDGs, particularly on SDG4, while SDG17 had a negative impact on 14 SDGs.

<!-- b000006 | prose | pages [1] -->
For problem two, we proposed a network-based evaluation algorithm for problem two, which considers feedback mechanisms and time impact to identify achievable goals and assess project effectiveness. Scores for each SDG were visualized for 10 regions, recommending SDG4 in five regions, including WLD and ARB. Achievable goals within 10 years were identified for 9 regions achieving SDG1 and 2 regions achieving SDG17.

<!-- b000007 | prose | pages [1] -->
For problem three, we proposed a revised plan to analyze the impact of network model changes when implementing a specific SDG, identifying new feasible goals with smaller impact on other SDGs. Using WLD as an example, we modified the network model to account for the one-way impact of achieved SDGs on other SDGs, visualizing and analyzing the results. We used an evaluation algorithm to determine the optimal priority target, finding that when implementing SDG4 in WLD, the optimal priority shifted to SDG8. We also recommend incorporating technology and digitalization as new development goals, given their positive impact on SDG2, SDG3, SDG7.

<!-- b000008 | prose | pages [1] -->
For problem four, we modified the model to respond to crises/opportunities by introducing a perturbation matrix to represent event impact and exploring its effect on optimal development goals. In the case of WLD/local wars, the optimal goal shifted from SDG1 to SDG17. Analyzing SDG9 under 7 events, we determined that natural disasters had the greatest impact on the UN’s work.

<!-- b000009 | prose | pages [1] -->
For problem five, our hierarchical network modeling approach can be promoted to analyze goal connections and select priority development goals in other fields. It can refine business goals into targets, indicators, and data in companies. We used business goals as an example, established a network model, and determined the optimal priority development goals. Our method is not limited to the SDG field but can also help other organizations and individuals achieve their goals.

<!-- b000010 | prose | pages [1] -->
We have concluded that our model has strong robustness, high stability, and good interpretability. This provides scientific guidance and support for achieving the SDGs.

<!-- b000011 | keywords | pages [1] -->
Keywords: SDG, Multiple Complex Networks, Pearson correlation coefficient, system dynamics

<!-- b000012 | heading | pages [2] -->
Contents

<!-- b000013 | contents | pages [2] -->
1 Introduction

<!-- b000014 | contents | pages [2] -->
2

<!-- b000015 | contents | pages [2] -->
1.1

<!-- b000016 | contents | pages [2] -->
Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000017 | contents | pages [2] -->
2

<!-- b000018 | contents | pages [2] -->
1.2

<!-- b000019 | contents | pages [2] -->
Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000020 | contents | pages [2] -->
2

<!-- b000021 | contents | pages [2] -->
1.3

<!-- b000022 | contents | pages [2] -->
Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000023 | contents | pages [2] -->
2

<!-- b000024 | contents | pages [2] -->
1.4

<!-- b000025 | contents | pages [2] -->
Our Works . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000026 | contents | pages [2] -->
3

<!-- b000027 | contents | pages [2] -->
2 Model Preparation

<!-- b000028 | contents | pages [2] -->
4

<!-- b000029 | contents | pages [2] -->
2.1

<!-- b000030 | contents | pages [2] -->
Assumptions and Justification

<!-- b000031 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000032 | contents | pages [2] -->
4

<!-- b000033 | contents | pages [2] -->
2.2

<!-- b000034 | contents | pages [2] -->
Notations

<!-- b000035 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000036 | contents | pages [2] -->
5

<!-- b000037 | contents | pages [2] -->
2.3

<!-- b000038 | contents | pages [2] -->
Data Preparation

<!-- b000039 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000040 | contents | pages [2] -->
5

<!-- b000041 | contents | pages [2] -->
3 Sub-model I: Establishment of Relationship Networks

<!-- b000042 | contents | pages [2] -->
6

<!-- b000043 | contents | pages [2] -->
3.1

<!-- b000044 | contents | pages [2] -->
Multiple Complex Model for Interactions among SDGs . . . . . . . . . . . . . . .

<!-- b000045 | contents | pages [2] -->
6

<!-- b000046 | contents | pages [2] -->
3.1.1

<!-- b000047 | contents | pages [2] -->
Introducing Multiple Complex Networks

<!-- b000048 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . .

<!-- b000049 | contents | pages [2] -->
6

<!-- b000050 | contents | pages [2] -->
3.1.2

<!-- b000051 | contents | pages [2] -->
Analyzing Relationships among SDGs using Multilayer Complex Networks

<!-- b000052 | contents | pages [2] -->
6

<!-- b000053 | contents | pages [2] -->
3.2

<!-- b000054 | contents | pages [2] -->
Result Analysis and Presentation . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000055 | contents | pages [2] -->
9

<!-- b000056 | contents | pages [2] -->
3.2.1

<!-- b000057 | contents | pages [2] -->
Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000058 | contents | pages [2] -->
9

<!-- b000059 | contents | pages [2] -->
3.2.2

<!-- b000060 | contents | pages [2] -->
In Different Regions

<!-- b000061 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000062 | contents | pages [2] -->
10

<!-- b000063 | contents | pages [2] -->
4 Sub-model II: Choice of Priorities Based on Relationship Network

<!-- b000064 | contents | pages [2] -->
10

<!-- b000065 | contents | pages [2] -->
4.1

<!-- b000066 | contents | pages [2] -->
Evaluation Method for Priorities Effectiveness . . . . . . . . . . . . . . . . . . . .

<!-- b000067 | contents | pages [2] -->
10

<!-- b000068 | contents | pages [2] -->
4.2

<!-- b000069 | contents | pages [2] -->
Priority Development Decision-making

<!-- b000070 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . .

<!-- b000071 | contents | pages [2] -->
12

<!-- b000072 | contents | pages [2] -->
4.3

<!-- b000073 | contents | pages [2] -->
Priority Decision-making in other Regions . . . . . . . . . . . . . . . . . . . . . .

<!-- b000074 | contents | pages [2] -->
13

<!-- b000075 | contents | pages [2] -->
4.4

<!-- b000076 | contents | pages [2] -->
Reasonably Achievable SDG for the next Decade

<!-- b000077 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . .

<!-- b000078 | contents | pages [2] -->
14

<!-- b000079 | contents | pages [2] -->
5 Sub-model III: The Impact of the Realization of a Particular SDG

<!-- b000080 | contents | pages [2] -->
15

<!-- b000081 | contents | pages [2] -->
5.1

<!-- b000082 | contents | pages [2] -->
Impact on Network Structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000083 | contents | pages [2] -->
15

<!-- b000084 | contents | pages [2] -->
5.2

<!-- b000085 | contents | pages [2] -->
Impact on Priority Selection

<!-- b000086 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000087 | contents | pages [2] -->
16

<!-- b000088 | contents | pages [2] -->
5.3

<!-- b000089 | contents | pages [2] -->
Other Goals that could be Considered

<!-- b000090 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000091 | contents | pages [2] -->
17

<!-- b000092 | contents | pages [2] -->
6 Sub-model IV: Impact of International Events or Crises

<!-- b000093 | contents | pages [2] -->
18

<!-- b000094 | contents | pages [2] -->
6.1

<!-- b000095 | contents | pages [2] -->
Impact on Network Model and Priority Selection

<!-- b000096 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . .

<!-- b000097 | contents | pages [2] -->
18

<!-- b000098 | contents | pages [2] -->
6.2

<!-- b000099 | contents | pages [2] -->
Numerical Simulation and Results Analysis . . . . . . . . . . . . . . . . . . . . .

<!-- b000100 | contents | pages [2] -->
19

<!-- b000101 | contents | pages [2] -->
6.3

<!-- b000102 | contents | pages [2] -->
Impact on UN Sustainable Development Business . . . . . . . . . . . . . . . . . .

<!-- b000103 | contents | pages [2] -->
20

<!-- b000104 | contents | pages [2] -->
7 Promoting Model:Setting Target Priorities for other Organizations

<!-- b000105 | contents | pages [2] -->
21

<!-- b000106 | contents | pages [2] -->
8 Robustness Testing and Analysis of Pros and Cons

<!-- b000107 | contents | pages [2] -->
22

<!-- b000108 | contents | pages [2] -->
8.1

<!-- b000109 | contents | pages [2] -->
Robustness Testing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000110 | contents | pages [2] -->
22

<!-- b000111 | contents | pages [2] -->
8.2

<!-- b000112 | contents | pages [2] -->
Pros . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000113 | contents | pages [2] -->
23

<!-- b000114 | contents | pages [2] -->
8.3

<!-- b000115 | contents | pages [2] -->
Cons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000116 | contents | pages [2] -->
23

<!-- b000117 | contents | pages [2] -->
Reference

<!-- b000118 | contents | pages [2] -->
24

<!-- b000119 | furniture | pages [3] -->
Team # 2304962

<!-- b000120 | furniture | pages [3] -->
Page 2 of 24

<!-- b000121 | heading | pages [3] -->
1 Introduction

<!-- b000122 | heading | pages [3] -->
1.1 Background

<!-- b000123 | prose | pages [3] -->
To promote sustainable development for all humanity, the establishment of the Sustainable Development Goals (SDGs) embodies humanity’s hope for the future. The interrelatedness, mutual support or opposition between these goals affects the implementation of all of them.

<!-- b000124 | prose | pages [3] -->
In addition, international events such as technological advances, global pandemics, war, and refugee crises also have a significant impact on the implementation of SDGs. Therefore, interdisci- plinary and comprehensive research methods are needed to understand and address these complex relationships and impacts.

<!-- b000125 | heading | pages [3] -->
1.2 Overview

<!-- b000126 | prose | pages [3] -->
The sustainable development goals (SDGs) are tightly interconnected and constitute an indi- visible whole, making it crucial to study their interrelationships. There has been extensive research conducted by various sectors of society on the relationships between SDGs. In 2015, the United Nations proposed 169 specific targets to elaborate the 17 goals. And the International Council for Science has used network models to study the interconnections between goals. Other scholars have conducted research from different perspectives, such as linkage pathways, degree of interaction, sustainable development goal models and execution methods. They have achieved many results.

<!-- b000127 | prose | pages [3] -->
However, current research has certain limitations because it is limited to expert knowledge and does not fully utilize economic data. Moreover, there is still a lack of quantitative research on how to use the relationships between SDGs to prioritize goals.

<!-- b000128 | heading | pages [3] -->
1.3 Restatement of the Problem

<!-- b000129 | prose | pages [3] -->
Our main challenge is to develop a network model that describes the relationships between the seventeen Sustainable Development Goals (SDGs), and to use this model to support decision- making and assess potential impacts. Specifically, our objectives are as follows:

<!-- b000130 | prose | pages [3] -->
• To construct a network structure that describes the relationships between the seventeen SDGs.

<!-- b000131 | prose | pages [3] -->
• Using the network structure to evaluate the effectiveness of a single SDG in promoting busi- ness development, and determining the priority issues and achievable goals within the next ten years.

<!-- b000132 | prose | pages [3] -->
• To explore the impact of achieving a specific SDG on the network structure, as well as how achieving that SDG would influence priority setting decisions, and to discuss other SDGs that could be incorporated into the United Nations agenda.

<!-- b000133 | prose | pages [3] -->
• To discuss the impact of international events such as technological advances and global pan- demics on the network structure and priority setting decisions, and to examine the implica- tions of such disruptions for sustainable development.

<!-- b000134 | prose | pages [3] -->
• To promote the method of constructing network structures to other companies and organiza- tions to help them determine the priority of their goals.

<!-- b000135 | furniture | pages [4] -->
Team # 2304962

<!-- b000136 | furniture | pages [4] -->
Page 3 of 24

<!-- b000137 | heading | pages [4] -->
1.4 Our Works

<!-- b000138 | prose | pages [4] -->
According to the requirements of the task, our work mainly includes the following aspects:

<!-- b000139 | prose | pages [4] -->
• Data collection and preprocessing: We collected 169 targets and 241 indicators data from UN experts, as well as time-series data of 500 sustainable development indicators from 1967 to 2018, covering ten research regions.

<!-- b000140 | prose | pages [4] -->
• Model establishment: Based on the correlation between data and the 4-layer network struc- ture from goals to data, we constructed the SDG relationship network model. Using the relationship network model G, we proposed an evaluation method to assess the effectiveness of prioritizing the implementation of a particular SDG.

<!-- b000141 | prose | pages [4] -->
• Model application: Based on the established network model, we visualized the network graph of ten research regions. Using the evaluation method, we also visualized the effective- ness of prioritized strategies for ten regions. Analyzing the visualization results, we drew conclusions.

<!-- b000142 | prose | pages [4] -->
Based on the network model, we established a model to describe the impact of different timeframes on the degree of SDG implementation. We established a model for the SDGs that can be reasonably achieved in different regions within ten years.

<!-- b000143 | prose | pages [4] -->
• Model adjustment for implementing a specific SDG: Based on the network model, we modified the weight and adjusted the network model, considering the impact on selecting priority items. We also proposed some new goals that could be included in the UN’s con- siderations, such as technological development and digitalization, and analyzed the reasons from the perspective of other SDG impacts.

<!-- b000144 | prose | pages [4] -->
• Model adjustment during international crises or opportunities: Based on the network model and evaluation method, we derived a new relationship network G’, introduced the anti-interference index c, and proposed a relationship formula between the disturbance Δx and G’ and the original network G. We modified the network model, considering the impact on selecting priority items, and analyzed the impact on the UN’s mission before and after the crisis.

<!-- b000145 | prose | pages [4] -->
• Promotion of model analysis methods: We promoted the analysis method of the relationship network to other fields, such as analyzing the relationship between a company’s strategic goals, to help leaders prioritize development items.

<!-- b000146 | prose | pages [4] -->
We conducted robustness and stability analysis, considering the disturbance of different research regions and events on the model. We concluded that the model has strong stability and robustness. In addition, we also analyzed the advantages and disadvantages of the model.

<!-- b000147 | furniture | pages [5] -->
Team # 2304962

<!-- b000148 | furniture | pages [5] -->
Page 4 of 24

<!-- b000149 | caption | pages [5] -->
Figure 1: Our work

<!-- b000150 | heading | pages [5] -->
2 Model Preparation

<!-- b000151 | heading | pages [5] -->
2.1 Assumptions and Justification

<!-- b000152 | prose | pages [5] -->
To simplify the problem and make it convenient for us to simulate real-life conditions, we make the following basic assumptions, each of which is properly justified.

<!-- b000153 | prose | pages [5] -->
• Consider the cascading effects between SDGs, such as reducing poverty and hunger may promote health and education, but at the same time may have negative impacts on climate change and the environment, thus affecting aspects such as species diversity.

<!-- b000154 | prose | pages [5] -->
• Consider the differences in the network of SDGs relationships between countries in dif- ferent regions and development levels.

<!-- b000155 | prose | pages [5] -->
• Assume that the effects between SDGs are stable, i.e., the relationship network does not change over time.

<!-- b000156 | prose | pages [5] -->
• Assume that the obtained data are real and reliable, and ignore the small noise in the data.

<!-- b000157 | prose | pages [5] -->
• Assume that there is only a linear relationship between the data of different indica- tors,although non-linear relationships are widely present, it is difficult to estimate. There- fore, we choose variables with a sufficiently large correlation coefficient, meaning that we greatly reduce the possible influence on the results.

<!-- b000158 | prose | pages [5] -->
• Assume that the influence between two targets is the same, i.e., the adjacency matrix is an undirected power map.

<!-- b000159 | furniture | pages [6] -->
Team # 2304962

<!-- b000160 | furniture | pages [6] -->
Page 5 of 24

<!-- b000161 | heading | pages [6] -->
2.2 Notations

<!-- b000162 | prose | pages [6] -->
Variable Name M eanings Examples Nodes, e.g. Ng denotes the set of Goal nodes Ng, Nt, Ni, Nd. N A Adjacency matrix Agg, Att, Aii, Add, etc.

<!-- b000163 | prose | pages [6] -->
Relationship Network Model G = Agg. G x The degree of realization of SDGs , as a 1*17 matrix x0, x1, etc.

<!-- b000164 | prose | pages [6] -->
∆x Perturbations arising , for 1*17 matrix ∆x.

<!-- b000165 | prose | pages [6] -->
c Anti-interference coefficient, related c

<!-- b000166 | heading | pages [6] -->
2.3 Data Preparation

<!-- b000167 | prose | pages [6] -->
In the data preparation stage, we conducted the identification of indicators and collection areas, multi-layer data collection, and World Bank data processing, and finally obtained the following data.

<!-- b000168 | prose | pages [6] -->
• data on 169 targets and 241 indicators derived from UN expert studies.

<!-- b000169 | prose | pages [6] -->
• time series data from 1967 to 2018 for 10 regions, 500 indicators about sustainable develop- ment.

<!-- b000170 | prose | pages [6] -->
For indicator identification, we used the Goal-Target-Indicator structure derived from the UN study to collect Targets and Indicator data. Second, we selected 10 study regions. These are the World (WLD), members of the Organization for Economic Cooperation and Development (OECD) (OED), the Arab World (ARB), Central Europe and the Baltics (CEB), East Asia & Pacific (EAS), East Asia & Central Asia (ECS), the European Union (EUU), Latin America & the Caribbean (LCN), the Middle East & North Africa (MEA) North Africa (MEA), and North America (NAC).

<!-- b000171 | caption | pages [6] -->
Figure 2: Regional Data preparation

<!-- b000172 | prose | pages [6] -->
For data collection and processing, we collected time-series data for 263 countries and regions from websites such as World Bank. The final data were obtained after processes such as process- ing missing values, eliminating useless data, sorting by region, and classifying the data in G-T-I structure.

<!-- b000173 | furniture | pages [7] -->
Team # 2304962

<!-- b000174 | furniture | pages [7] -->
Page 6 of 24

<!-- b000175 | heading | pages [7] -->
3 Sub-model I: Establishment of Relationship Networks

<!-- b000176 | heading | pages [7] -->
3.1 Multiple Complex Model for Interactions among SDGs

<!-- b000177 | heading | pages [7] -->
3.1.1 Introducing Multiple Complex Networks

<!-- b000178 | prose | pages [7] -->
Multilayer Complex Networks(MCNs) refer to complex network models composed of multiple layers or networks, which can interact or depend on each other. Unlike traditional network models, multilayer complex networks allow different types of nodes and connections to intersect across different layers, and allow nodes to have overlapping relationships across different layers.

<!-- b000179 | prose | pages [7] -->
Multilayer complex networks have wide applications in describing and analyzing complex real- world systems, such as social networks, biological networks, and transportation networks. They can provide a more comprehensive perspective to describe the structure and function of the system, and can better capture the multiple relationships between nodes.

<!-- b000180 | prose | pages [7] -->
Analytical methods of multilayer complex networks include graph-theoretical methods, com- plex network models and methods, as well as machine learning methods, among others. By an- alyzing multilayer complex networks, we can better understand the evolution and behavior of the system, and provide new insights and methods for solving practical problems.

<!-- b000181 | prose | pages [7] -->
In summary, the study of multilayer complex networks has great potential for understanding complex systems and addressing real-world problems. The development of analytical methods and models for multilayer complex networks can provide a new perspective and approach for the study of complex systems.

<!-- b000182 | heading | pages [7] -->
3.1.2 Analyzing Relationships among SDGs using Multilayer Complex Networks

<!-- b000183 | prose | pages [7] -->
The interrelationships among SDGs are highly complex, as each goal can potentially affect the implementation of other goals. Moreover, there are many indicators that can be used to repre- sent the degree of goal attainment, and simply linking goals to data indicators may overlook their intricate relationships. Therefore, we turn to a data-driven approach, namely MCNs, to analyze the relationships among data indicators, which can indirectly construct the interrelationships among SDGs. This approach can help us better understand the mutual impacts among SDGs and provide new ideas and methods for solving practical problems.

<!-- b000184 | prose | pages [7] -->
• G −T −I framework determined by UN experts:

<!-- b000185 | prose | pages [7, 8] -->
The United Nations has identified 169 specific indicators to assess whether the 17 sustainable development goals (SDGs) have been achieved. For instance, SDG7 is evaluated using seven indi- cators, including increasing the proportion of renewable energy and improving energy efficiency. UN experts have established links between Targets and used Indicators to quantify them. For ex- ample, Target 1.1 under SDG1 (no poverty) is ”to eradicate extreme poverty and hunger globally,” while Target 1.2 is ”to ensure that everyone has access to adequate social protection and healthcare.” Indicator 1.1.1 under Target 1.1 is ”Proportion of population below the international poverty line, by sex, age, employment status and geographical location (urban/rural).” Based on the G −T −I system established by UN experts and known data, we can establish a direct relationship between World Bank Data and Indicators. This allows us to present the changes between goals and data more systematically. By connecting 241 Indicators with 500 Data indicators, we ultimately obtained 17 isolated G −T −I −D networks. Using SDG9 as an example, the network structure is shown in

<!-- b000186 | furniture | pages [8] -->
Team # 2304962

<!-- b000187 | furniture | pages [8] -->
Page 7 of 24

<!-- b000189 | caption | pages [8] -->
Figure 3.

<!-- b000190 | caption | pages [8] -->
Figure 3: G −T −I −D network

<!-- b000191 | prose | pages [8] -->
• Describing the Mechanism of Interconnection in the G-T-I-D Network:

<!-- b000192 | prose | pages [8] -->
As shown in Figure 4, two G−T −I−D networks are connected through the correlation of D. N represents the node matrix, with Ng, Nt, Ni, Nd representing the goals, targets, indicators, and data nodes, respectively. A represents the adjacency matrix, with Agg[17×17], Att[169×169], Aii[241× 241], Add[500 × 500] representing the adjacency matrices between goals, targets, indicators, and data, respectively. Agt[17 × 169], Ati[169 × 241], and Aid[241 × 500] represent the adjacency matrices between goals and targets, targets and indicators, and indicators and data, respectively. The adjacency matrices of these four initial ones matrices are given by a single G −T −I −D structure.

<!-- b000193 | prose | pages [8] -->
The linking of the Datas is based on the Pearson correlation coefficient values. (the datas were connected when the r exceeded 0.9 with p < 0.1 significance level.)

<!-- b000194 | furniture | pages [9] -->
Team # 2304962

<!-- b000195 | furniture | pages [9] -->
Page 8 of 24

<!-- b000196 | caption | pages [9] -->
Figure 4: two G −T −I −D network

<!-- b000197 | prose | pages [9] -->
• Calculation of G −G Adjacency Matrix:

<!-- b000198 | prose | pages [9] -->
First, calculate the correlation between data: We calculated the correlation coefficients between World Bank data indicators to obtain the Add matrix.

<!-- b000199 | prose | pages [9] -->
Then, the I −I adjacency matrix Aiiwas obtained as Aii = Aid · Add · Adi, and the T −T adjacency matrix was obtained as Att = Ati · Aid · Add · Adi · Ait. Finally, the G −G adjacency matrix was obtained as Agg = Agt ·Ati ·Aid ·Add ·Adi ·Ait ·Atg. The process is illustrated in Figure 5.

<!-- b000200 | caption | pages [9] -->
Figure 5: calculation of Agg

<!-- b000201 | furniture | pages [10] -->
Team # 2304962

<!-- b000202 | furniture | pages [10] -->
Page 9 of 24

<!-- b000203 | heading | pages [10] -->
3.2 Result Analysis and Presentation

<!-- b000204 | heading | pages [10] -->
3.2.1 Result

<!-- b000205 | prose | pages [10] -->
The elements of the G −G adjacency matrix Agg represent the weights that denote the in- terconnections among the 17 SDGs. By distinguishing only between 0 and non-zero elements, we can obtain an undirected and unweighted graph of the SDGs, which represents the existence of influence between two SDGs. If we consider the weight values, the greater the absolute value, the higher the degree of influence between two SDGs, with the sign indicating mutual support or counterbalance between the two SDGs. We use orange-red and light-blue colors to represent the mutually supportive and antagonistic relationships between SDGs, respectively, and the brightness of the connecting line color indicates the degree of influence between SDGs. We visualize the SDG impact network as shown in Figure 6 after optimizing its structure.

<!-- b000206 | caption | pages [10] -->
Figure 6: Weighted graph of SDGs interconnection (using WLD as an example)

<!-- b000207 | prose | pages [10] -->
In the WLD region, SDG8, SDG10, and SDG4 have a positive impact on 14 SDGs, indicating that these three goals have been well implemented and executed in the region. SDG8 focuses on economic growth and employment, SDG10 focuses on reducing inequality, and SDG4 focuses on quality education. These three goals have a common feature in that they make important contribu- tions to economic and social development and occupy a significant position in the development of the WLD region. Therefore, the positive impact of these three goals on other SDGs is not surprising.

<!-- b000208 | prose | pages [10] -->
In contrast, SDG17 has a negative impact on 16 SDGs, indicating that there are some problems with the implementation of SDG17 in the WLD region. SDG17 focuses on global partnerships, including development assistance, trade, and technology transfer, but in the WLD region, the de- velopment of these aspects faces some challenges

<!-- b000209 | furniture | pages [11] -->
Team # 2304962

<!-- b000210 | furniture | pages [11] -->
Page 10 of 24

<!-- b000211 | heading | pages [11] -->
3.2.2 In Different Regions

<!-- b000212 | prose | pages [11] -->
Considering that the connections and influences between SDGs in different regions may vary, we used data from different regions to verify the generated network structure. The SDG networks of eight regions are shown in Figure 7.

<!-- b000213 | caption | pages [11] -->
Figure 7: Weighted graph of SDGs interconnection (using WLD as an example)

<!-- b000214 | prose | pages [11] -->
In the CEB region, SDG4 has a negative impact on six other goals, including SDG3, and only a positive impact on SDG8. On the other hand, in the EAS region, SDG4 has a positive impact on all 16 SDGs. In the OED region, most of the SDGs have negative impacts on each other, while in the MEA region, most of the SDGs have positive impacts on each other. The reasons for these differences may be related to various factors, such as economic, social, cultural, and political dif- ferences.

<!-- b000215 | prose | pages [11] -->
In the CEB region, a lack of educational and health resources may be the reason for the negative impact of SDG4 on other goals. For instance, a shortage of education and health resources could lead to higher levels of disease and poverty, thereby having a negative impact on SDG3.

<!-- b000216 | prose | pages [11] -->
On the other hand, in the EAS region, success in education and health may be the reason for the positive impact of SDG4 on other goals. For example, good levels of education and health may help to improve employment rates, promote economic growth, and thus have a positive impact on SDG8.

<!-- b000217 | heading | pages [11] -->
4 Sub-model II: Choice of Priorities Based on Relationship Net-

<!-- b000218 | prose | pages [11] -->
work

<!-- b000219 | heading | pages [11] -->
4.1 Evaluation Method for Priorities Effectiveness

<!-- b000220 | prose | pages [11] -->
• Quantifying the Implementation of SDGs by Adopting Standards:

<!-- b000221 | prose | pages [11, 12] -->
If we use some numbers to represent the current level of implementation of these 17 SDGs, we can standardize these numbers so that their range is limited to values between 0 and 1. If we repre- sent the level of implementation of these 17 SDGs with x1 to x17, then the range of values is from 0 to 1. Then, we can use these numerical values as a 17-dimensional vector x = [x1, x2, . . . , x17], which can represent the level of implementation of 17 SDGs in a certain region.

<!-- b000222 | furniture | pages [12] -->
Team # 2304962

<!-- b000223 | furniture | pages [12] -->
Page 11 of 24

<!-- b000225 | prose | pages [12] -->
• Consider the Effects of Prioritizing the Development of a Specific SDG:

<!-- b000226 | prose | pages [12] -->
If we want to measure the impact of changes in implementation levels, we can use a coefficient matrix to calculate the changes in the implementation vector x0. Specifically, assuming the coeffi- cient matrix is A, which is the adjacency matrix Agg of the relationship network among SDGs, the implementation vector x0 can be calculated after one iteration as follows:

<!-- b000227 | prose | pages [12] -->
x1 = Ax0

<!-- b000228 | prose | pages [12] -->
Here, x1 represents the new value of the implementation vector x0 after one iteration. This new value reflects the impact of changes in implementation levels on other indicators. If an element in x1 becomes closer to 1, it indicates an improvement in the implementation level of the corresponding indicator, and vice versa.

<!-- b000229 | prose | pages [12] -->
It should be noted that the values of the coefficient matrix A should be between 0 and 1. If a coefficient is greater than 1, it can be viewed as 1, and if it is less than 0, it can be viewed as 0. This ensures that each element of the calculated implementation vector x1 is between 0 and 1.

<!-- b000230 | prose | pages [12] -->
• Consider the Cascading Effects:

<!-- b000231 | prose | pages [12] -->
However, the relationships between these goals are not always straightforward and can be com- plex. For example, investing heavily in education may have a short-term impact on economic de- velopment, but in the long run, education can accelerate the development of the economy and technology. Therefore, when considering the cascading effects of prioritizing a particular SDG, it is important to take into account both short-term and long-term effects and the potential feedback loops between different goals. This requires a more nuanced analysis and modeling approach to capture the complex interdependencies between the SDGs.

<!-- b000232 | prose | pages [12] -->
xn = Anx0, xn = A · (nx0) not

<!-- b000233 | prose | pages [12] -->
Therefore, we need to revise the original model. Here, we should not only consider the impact of SDG 1 on SDG 2, but also the impact of SDG 1 on SDG 3, and then the impact of SDG 3 on SDG 2.Figure 8 shows the chain efforts of such iteration. This indicates that within a certain period of iteration, which is several years, we should always expect that the significant development of one SDG will have not only a direct impact but also indirect impacts on other SDGs.

<!-- b000234 | prose | pages [12] -->
In addition, we cannot simply assume that the development of a certain SDG will not have an impact on itself. For example, without other limiting conditions, the vigorous development of the economy (SDG 8) itself will have a positive impact on economic development, which is called a ”positive feedback mechanism”.

<!-- b000235 | furniture | pages [13] -->
Team # 2304962

<!-- b000236 | furniture | pages [13] -->
Page 12 of 24

<!-- b000237 | caption | pages [13] -->
Figure 8: chain efforts

<!-- b000238 | prose | pages [13] -->
• New Modified Model:

<!-- b000239 | prose | pages [13] -->
n = An can Based on the above, using the nth power of the influence coefficient matrix Agg approximately reflect the impact of a sudden change in one indicator on other indicators. This impact can represent the effect of a strong SDG development on the progress of other goals in the short term or over several years.

<!-- b000240 | prose | pages [13] -->
Therefore, if n is taken to be infinity or sufficiently large, it can represent the long-term changes of other goals when one goal is significantly developed. The arithmetic sum of the vectors of

<!-- b000241 | prose | pages [13] -->
n|| = ||An||1 y = ||Agg

<!-- b000242 | prose | pages [13] -->
can then represent the score obtained from the significant development of that goal. By further comparing the scores obtained from the significant development of each goal, we can identify the priority development goals and the possible achievement of other goals.

<!-- b000243 | heading | pages [13] -->
4.2 Priority Development Decision-making

<!-- b000244 | prose | pages [13] -->
Using WLD as an example, we applied our evaluation model and calculated the network relation- ships for WLD. To represent the prioritization of SDG1, we some initial values and evaluated the impact on the other 16 SDGs. By quantifying the impact on each SDG and summing them, we obtained an effectiveness value for the development of SDG1. The same process was repeated for each SDG. The effectiveness values for the development of the 17 SDGs in WLD were obtained and presented in a table, as shown in Figure 9. Further analysis of the results will be provided.

<!-- b000245 | furniture | pages [14] -->
Team # 2304962

<!-- b000246 | furniture | pages [14] -->
Page 13 of 24

<!-- b000247 | caption | pages [14] -->
Figure 9: Effectiveness of prioritizing the development of 17 SDGs(taking WLD as an example)

<!-- b000248 | heading | pages [14] -->
4.3 Priority Decision-making in other Regions

<!-- b000249 | prose | pages [14] -->
Applying the model to the network relationship models of the other eight regions, we obtained effectiveness values for the development of the 17 SDGs, which are presented in a table as shown in the Figure 10.

<!-- b000250 | caption | pages [14] -->
Figure 10: Effectiveness of prioritizing the development of 17 SDGs in other regions

<!-- b000251 | prose | pages [14] -->
It can be observed that the priority development needs vary across different regions. For in- stance, in the MEA region, there is a higher demand for the development of SDG 1 and 2, while the demand for SDG 13-15 is relatively lower. On the other hand, in the NAC region, there is a higher demand for the development of SDG 13-15, and a lower demand for SDG 1-2. The difference in development needs between these two regions does not imply that they do not need to develop in those aspects. Sometimes, it may be due to the fact that they have already achieved a relatively high level of development, resulting in lower effectiveness in further development. At other times, it may be because they need to prioritize the development of other SDGs.

<!-- b000252 | furniture | pages [15] -->
Team # 2304962

<!-- b000253 | furniture | pages [15] -->
Page 14 of 24

<!-- b000254 | prose | pages [15] -->
Moreover, by plotting these development needs as line graphs and placing them at one Figure 11. The varying priority levels for developing different SDGs across different regions can be clearly visualized.

<!-- b000255 | caption | pages [15] -->
Figure 11: Line graph of effectiveness of prioritizing the development

<!-- b000256 | prose | pages [15] -->
We validated the priority assessment for different regions and found that it is generally consistent with reality, indicating that our model has good robustness.

<!-- b000257 | heading | pages [15] -->
4.4 Reasonably Achievable SDG for the next Decade

<!-- b000258 | prose | pages [15] -->
In our previous model, we analyzed and quantified the numerical representation of SDG im- plementation. We set the year n = 10 to calculate the development progress of the 17 SDGs ten years later and selected coefficients to evaluate the development progress based on the current ac- tual development level. According to the evaluation results, the SDGs that these ten regions can achieve in the next ten years are presented in the Figure 12.

<!-- b000259 | prose | pages [15] -->
Within ten years, SDG1 can be achieved in nine regions, SDG4 in eight regions, while only one region can achieve SDG13, SDG14, SDG16, and SDG17.

<!-- b000260 | prose | pages [15] -->
SDG1, which aims to eradicate poverty, is one of the most fundamental and prerequisite goals for achieving other Sustainable Development Goals. Its implementation typically requires govern- ment policy support and commitment, as well as broad efforts in social and economic development. Therefore, the fact that 9 regions can achieve SDG1 within 10 years may indicate that these regions have relatively developed economic and social infrastructure, government commitment to invest in poverty reduction plans, and good international support.

<!-- b000261 | prose | pages [15] -->
In contrast, SDG13, SDG14, and SDG16 require more global cooperation and policy action to achieve. As climate change and marine protection issues often involve global environmental and economic impacts, progress requires coordinated international action. The achievement of SDG16 also requires the establishment of effective political and judicial systems, which may face some difficulties in certain regions.

<!-- b000262 | furniture | pages [16] -->
Team # 2304962

<!-- b000263 | furniture | pages [16] -->
Page 15 of 24

<!-- b000264 | caption | pages [16] -->
Figure 12: Reasonably achievable SDGs for the next decade in 10 regions

<!-- b000265 | heading | pages [16] -->
5 Sub-model III: The Impact of the Realization of a Particular

<!-- b000266 | prose | pages [16] -->
SDG

<!-- b000267 | heading | pages [16] -->
5.1 Impact on Network Structure

<!-- b000268 | prose | pages [16] -->
The attainment of a specific SDG can have a significant impact on the realization of other SDGs, as the SDGs are interdependent. It is possible that implementing a particular SDG will result in transforming some of the pre-existing bidirectional impacts in the network to unidirectional impacts. While completed SDGs will continue to have positive or negative effects on the incomplete SDGs, the incomplete SDGs will no longer affect the completed SDGs. Accordingly, the G −G adjacency matrix Agg can be modified to incorporate these changes by converting the bidirectional impacts to unidirectional ones, leading to a new network of interrelationships between SDGs.

<!-- b000269 | prose | pages [16] -->
We also have focused on the area of WLD and used SDGs as a case study to analyze the ef- fects of implementing this SDG on the network of interrelationships. To compare the network of interrelationships before and after the implementation of SDGs, we have generated Figure 13. Our analysis reveals that after achieving SDG4, the highest priority item is to achieve SDG8, followed by SDG17. Therefore, considering the connections with SDG4, the number of connections between SDG8 and SDG17 increases, meaning that more SDGs are influenced by their development.

<!-- b000270 | furniture | pages [17] -->
Team # 2304962

<!-- b000271 | furniture | pages [17] -->
Page 16 of 24

<!-- b000272 | caption | pages [17] -->
Figure 13: Comparison of the relational network before and after SDG4 implementation

<!-- b000273 | heading | pages [17] -->
5.2 Impact on Priority Selection

<!-- b000274 | prose | pages [17] -->
The completion of a specific SDG can affect the prioritization of development targets by al- tering the network structure.

<!-- b000275 | prose | pages [17] -->
To evaluate the effectiveness by our model, we have abstracted the element of Agg(i, j) as the impact of SDGi to SDGj. By summing and normalizing each row of the matrix Agg, we have derived the comprehensive impact score of SDGi to all 17 SDGs (in 10 regions) to aid in selecting the optimal development target that balances multiple goals.

<!-- b000276 | prose | pages [17] -->
After implementing a specific SDG, the network of interrelationships, Agg, undergoes a trans- formation to A′ gg. However, the same approach for evaluating effectiveness can be applied to A′ gg in order to prioritize development targets.

<!-- b000277 | prose | pages [17] -->
Taking the area of WLD as a case study, we examined the impact of implementing SDGs on the prioritization of development targets. We applied our assessment method to calculate the com- prehensive scores for developing all 17 SDGs, both before Agg and after A′ gg implementation. The results of the comparison between the prioritization of development targets before and after the implementation of SDGs are shown in Figure 14.

<!-- b000278 | prose | pages [17] -->
Our analysis reveals that during the process of focusing on achieving SDG4 (Quality Education), we observed a phenomenon of decreased priority in SDG7 (Affordable and Clean Energy) and SDG14 (Life Below Water). This is because there is a high degree of overlap between SDG4 and SDG7/SDG14, and due to the widespread promotion of education, more people have become aware of the importance of SDG7 and SDG14. As a result, the priority for further development of these two SDGs has decreased.

<!-- b000279 | furniture | pages [18] -->
Team # 2304962

<!-- b000280 | furniture | pages [18] -->
Page 17 of 24

<!-- b000281 | caption | pages [18] -->
Figure 14: Comparison of priority selection scores before and after SDGs implementation

<!-- b000282 | heading | pages [18] -->
5.3 Other Goals that could be Considered

<!-- b000283 | prose | pages [18] -->
While the SDGs are a broad, inclusive framework, it still has some shortcomings and chal- lenges. If some of the goals have been achieved, we believe there are others that can be taken into account including Technology Innovation and Digitalization and regional variability elimination. We will analyze the reasons for this in terms of the impact of these goals on other SDGs.

<!-- b000284 | prose | pages [18] -->
• Technological Innovation and Digital Technologies:

<!-- b000285 | prose | pages [18] -->
In the context of sustainable development goals, social, economic, and environmental sustain- ability has received widespread attention, but there has been relatively less focus on technological innovation and digitization, which is a shortcoming. Technological innovation and digital tech- nologies have important impacts on the achievement of multiple SDG targets.

<!-- b000286 | prose | pages [18] -->
For example, in SDG 2 (Zero Hunger), the development of agricultural technology and digital technology can improve agricultural productivity, increase food supply, and enhance food safety. In SDG 3 (Good Health and Well-being), digital technology can support the development and inno- vation of healthcare services, such as telemedicine and electronic health records. In SDG 4 (Quality Education), digital technology can improve education content and teaching methods, such as on- line learning and virtual reality technology. In SDG 7 (Affordable and Clean Energy), innovative technology can improve the production efficiency of renewable energy and reduce energy consump- tion, such as solar, wind, and geothermal energy. In SDG 11 (Sustainable Cities and Communities), digital technology can promote sustainable development of cities and communities, such as smart transportation, smart city management, and smart buildings.

<!-- b000287 | prose | pages [18] -->
In summary, technological innovation and digital technology play a promoting role in achieving multiple SDG targets, providing important support for sustainable development.

<!-- b000288 | furniture | pages [19] -->
Team # 2304962

<!-- b000289 | furniture | pages [19] -->
Page 18 of 24

<!-- b000290 | prose | pages [19] -->
• Regional Equality:

<!-- b000291 | prose | pages [19] -->
Although sustainable development goals are a global framework, the needs and challenges of different regions and countries are different. Ignoring the impact of regional differences is harm- ful. Therefore, regional equality (eliminating regional differences) has a significant impact on the implementation of multiple SDG targets, particularly on the following targets:

<!-- b000292 | prose | pages [19] -->
SDG 1 (No Poverty), SDG 2 (Zero Hunger), SDG 3 (Good Health and Well-being), SDG 4 (Quality Education), SDG 9 (Industry, Innovation and Infrastructure), and SDG 10 (Reduced In- equality). Eliminating regional differences can reduce the gap between rich and poor areas, improve the living standards of people in poverty-stricken areas, enhance agricultural production and food supply in rural areas, promote the equitable distribution of healthcare resources, reduce the gap between urban and rural education levels, and balance economic development and infrastructure in different regions, thus promoting social equity and common prosperity.

<!-- b000293 | prose | pages [19] -->
In conclusion, eliminating regional differences is of great significance for the implementation of SDGs, as it can improve the comprehensiveness and coordination of SDG goals and promote the process of sustainable development.

<!-- b000294 | heading | pages [19] -->
6 Sub-model IV: Impact of International Events or Crises

<!-- b000295 | heading | pages [19] -->
6.1 Impact on Network Model and Priority Selection

<!-- b000296 | prose | pages [19] -->
First, we modeled the expressions of the SDGs relationship networks before and after the occurrence of opportunities or crises. We used x0 to represent the initial level of implementation of the 17 SDGs, x2(1·17) to represent the level of implementation of the 17 SDGs after the occurrence of opportunities or crises, and x1(1 · 17) to represent the level of SDG implementation after being affected but without opportunities or crises. We used ∆x(1 · 17) to represent the disturbance to the development of the 17 SDGs brought by opportunities or crises. We used G and G2 to represent the SDGs relationship networks before and after the occurrence of opportunities or crises.

<!-- b000297 | prose | pages [19] -->
If there is no opportunity or crisis, the initial state x0 changes to x1 after being influenced by the network. this process can be expressed as 

<!-- b000298 | prose | pages [19] -->
x1 = x0 · G (1)

<!-- b000299 | prose | pages [19] -->
When an opportunity or crisis occurs, the degree of realization x0 in the initial state changes to the degree of realization x2 after the opportunity or crisis. this process can be expressed as 

<!-- b000300 | prose | pages [19] -->
x2 = x0 · G′ (2)

<!-- b000301 | prose | pages [19] -->
Therefore, x1, x2 can be linked by perturbing ∆x, and the relationship between them can be ex- pressed as  x2 = x1 + ∆x (3)

<!-- b000302 | prose | pages [19] -->
Combine the equations1,2,3  x0 · G′ = x0 · G + ∆x (4)

<!-- b000303 | prose | pages [19, 20] -->
Assuming that x0 is invertible, it is further obtained that  G′ = G + x−1 · ∆x (5) 0 Here,we define the inverse of x−1 s.t.   x−1 · x0 = E17·17 0 0 Let G′ = c · ∆x, where Gij represents the resistance of SDGi to the disturbance of SDGj at the development level of x0.

<!-- b000304 | furniture | pages [20] -->
Team # 2304962

<!-- b000305 | furniture | pages [20] -->
Page 19 of 24

<!-- b000307 | prose | pages [20] -->
The SDG network G′ under the occurrence of opportunities or crises can be represented as:

<!-- b000308 | prose | pages [20] -->
G′ = G + ∆G, ∆G = c · ∆x

<!-- b000309 | prose | pages [20] -->
where c is related to x0, representing the resistance of the region to opportunities or risks in the implementation of a certain SDG level.

<!-- b000310 | prose | pages [20] -->
We will continue to use the previously adopted method for evaluating the effectiveness of pri- ority development issues.

<!-- b000311 | heading | pages [20] -->
6.2 Numerical Simulation and Results Analysis

<!-- b000312 | prose | pages [20] -->
We quantified the impact of progress or crisis on the 17 SDGs and expressed it as a 1*17 perturbation matrix. Natural disasters have a significant impact on SDG goal attainment, so we included natural disasters in the events considered.

<!-- b000313 | prose | pages [20] -->
We analyzed the impacts of six events on the implementation of SDGs based on common sense and available data.

<!-- b000314 | prose | pages [20] -->
For example, climate change poses significant threats to ecosystems and human health, includ- ing sea-level rise, temperature increases, and natural disasters, which negatively affect the imple- mentation of SDG13, set to -1. War leads to social instability and damages infrastructure, economy, ecology, and human health, which negatively affect the implementation of SDG1, set to -0.8.

<!-- b000315 | prose | pages [20] -->
Combining the analysis, we finally obtained the disturbance matrix ∆x for SDG implementation under six opportunities or risks, as shown in Table 1.

<!-- b000316 | prose | pages [20] -->
Event Name Perturbation matrix Technological advances [0,0,0.1,0,-0.2,0.6,-0.5,0.8,0,0,0.9,0,0,0,-0.3,0.5,0] Global Epidemics [-0.5,-0.9,-0.8,-0.3,0,0,-0.1,0,0,0,0,0,0,0,0.4,-0.6,-0.7] Climate Change [-0.9,-0.8,-1,-0.6,0,0,-0.8,0,0,0,0,0,0,0,0.7,-0.4,-0.6] Regional Wars [-0.7,-0.8,-0.9,-1,0,0,-0.7,0,0,0,0,0,0,0,0.5,-0.8,-0.5] Refugee Movement [-0.7,-0.5,-0.6,-0.7,0,0,-0.6,0,0,0,0,0,0,0,0.7,-0.9,-0.4] Natural Disasters [-0.3,-0.2,0.3,0,0,-0.2,0.5,0,0,-0.2,0,0,0,0.3,0.3,0,0.3]

<!-- b000317 | caption | pages [20] -->
Table 1: Perturbation matrix of each events

<!-- b000318 | prose | pages [20] -->
Taking ARB and natural disasters as examples, we provided the initial development level x1. We then calculated x2 and G′ using the derived formulas. Based on G′ and the effectiveness assessment method, we presented the development relationship network and the priority development scores of SDGs before and after the impact of natural disasters in ARB, as shown in Figure 15.

<!-- b000319 | furniture | pages [21] -->
Team # 2304962

<!-- b000320 | furniture | pages [21] -->
Page 20 of 24

<!-- b000321 | caption | pages [21] -->
Figure 15: The effectiveness of prioritizing SDG development in regions affected by Region Wars

<!-- b000322 | prose | pages [21] -->
in the ARB

<!-- b000323 | prose | pages [21] -->
The development effectiveness of SDGs varies in different circumstances, and war is one of the most significant factors that can influence the priority setting of SDG development. As revealed in our analysis, the effectiveness of developing SDG3 (good health and well-being) and SDG17 (partnerships for the goals) becomes more crucial during wartime. The former is critical for en- hancing people’s health and survival ability, while the latter can help countries jointly cope with the challenges brought by war. However, due to the potential economic recession and social instabil- ity that may arise during war, the realization of SDG1 (no poverty) and SDG4 (quality education) may become more difficult and uncertain, leading to a relatively lower priority in the development agenda. Therefore, it is essential to carefully consider the impact of war on SDG development and prioritize accordingly, to ensure a comprehensive and coordinated approach towards sustainable development.

<!-- b000324 | heading | pages [21] -->
6.3 Impact on UN Sustainable Development Business

<!-- b000325 | prose | pages [21] -->
By comparing x1, x2, and ∆x, we can evaluate the impact of opportunities and challenges on the United Nations Sustainable Development Plan. For example, in the case of all events in the WLD region, as shown in the Figure 16, From here, we can see that natural disasters have the greatest impact on the prioritization of the 17 SDGs. It has a huge negative effect on all of our SDGs, especially SDG4, where lack of sufficient funds or manpower for education is a major issue, as well as SDG1 and SDG8, as natural disasters can destroy people’s homes, damage their property, and greatly affect the economic development and job security of regions and countries.

<!-- b000326 | furniture | pages [22] -->
Team # 2304962

<!-- b000327 | furniture | pages [22] -->
Page 21 of 24

<!-- b000328 | prose | pages [22] -->
Moreover, in most cases, people tend to lower the priority of SDGs during natural disasters because these events often call for unity and cooperation among individuals and communities in different regions and countries. Therefore, in such situations, the effectiveness of prioritizing the development of SDG17 is relatively low.

<!-- b000329 | caption | pages [22] -->
Figure 16: Priority development level of different SDGs in different events

<!-- b000330 | heading | pages [22] -->
7 Promoting Model:Setting Target Priorities for other Organi-

<!-- b000331 | prose | pages [22] -->
zations

<!-- b000332 | prose | pages [22] -->
• Our method has strong generalizability.In this paper, we refined the goals based on UN expert recommendations, decomposing abstract SDGs into more specific targets, and further breaking down these targets into quantifiable indicators. We then linked the available data with these indicators, constructing a hierarchical network of single targets. Based on the interrelationship of data, we indirectly linked multiple single-goal networks through the net- work structure to obtain complex interdependence relationships among goals and between different levels.

<!-- b000333 | prose | pages [22] -->
• Regarding a company’s strategic objectives, a similar method can be used for analy- sis.Assuming that the company has four strategic objectives, namely market goal, innovation goal, profit goal, and social goal.

<!-- b000334 | prose | pages [22] -->
• A hierarchical network model can be used to analyze these objectives, taking the market goal as an example, which can be broken down into two specific targets: increasing market share and improving product quality.

<!-- b000335 | prose | pages [22] -->
• Among them, increasing market share can be further refined into quantifiable indicators such as increasing sales, expanding sales channels, expanding market coverage, and increasing brand awareness. The increasing sales indicator can be measured using specific data such as total sales, sales volume, and average unit price.

<!-- b000336 | furniture | pages [23] -->
Team # 2304962

<!-- b000337 | furniture | pages [23] -->
Page 22 of 24

<!-- b000338 | prose | pages [23] -->
• The network diagram of a single objective is shown in Figure 17, and similar analysis methods can be used to obtain a multi-layer network of the four macro objectives.

<!-- b000339 | prose | pages [23] -->
Based on the correlation between the data, the relationship network G between macro objec- tives can be obtained, and the best priority development item can be identified through this network.

<!-- b000340 | caption | pages [23] -->
Figure 17: Single-layer network of a certain company

<!-- b000341 | prose | pages [23] -->
The same approach can be applied to analyze goals for any organization or individual, regardless of whether they are commercial, non-profit, or personal. Breaking down abstract goals into specific sub-goals and further refining them into quantifiable metrics can help people better understand their goal, track and evaluate their progress towards them, and identify the crit- ical factors affecting goal achievement. By using a network, relationships between goals can be better understood, and this can aid organizations or individuals in selecting priority items among numerous goals.

<!-- b000342 | heading | pages [23] -->
8 Robustness Testing and Analysis of Pros and Cons

<!-- b000343 | heading | pages [23] -->
8.1 Robustness Testing

<!-- b000344 | prose | pages [23] -->
• In Model I, we conducted a regional test by setting different regions to examine the stability of the model with respect to regions.

<!-- b000345 | prose | pages [23] -->
• In Model II, we set different SDG priority orders to test the stability of the model with respect to SDGs.

<!-- b000346 | furniture | pages [24] -->
Team # 2304962

<!-- b000347 | furniture | pages [24] -->
Page 23 of 24

<!-- b000348 | prose | pages [24] -->
• In Model III, we tested the stability of the model regarding time by setting different time lengths.

<!-- b000349 | prose | pages [24] -->
• In Model IV, we examined the stability of the model under different perturbations by provid- ing various disturbances.

<!-- b000350 | prose | pages [24] -->
Our testing in these four aspects was conducted in a progressive manner, meaning that our model ensures stability across all four dimensions.

<!-- b000351 | heading | pages [24] -->
8.2 Pros

<!-- b000352 | prose | pages [24] -->
• Considers the chain reactions among SDGs, which is more in line with the reality of the situation and provides a more accurate representation of the interconnectedness of the SDGs.

<!-- b000353 | prose | pages [24] -->
• The network is complex, and its structure is hierarchical, making it highly interpretable and easy to understand.

<!-- b000354 | prose | pages [24] -->
• The model has high generalizability and can be extended to other domains or areas.

<!-- b000355 | prose | pages [24] -->
• It is stable and robust, indicating that the model is less likely to be influenced by outliers or unexpected changes.

<!-- b000356 | heading | pages [24] -->
8.3 Cons

<!-- b000357 | prose | pages [24] -->
• The model does not ues nonlinear relationships between the SDGs, which may limit its ability to capture more complex interactions between the goal.

<!-- b000358 | prose | pages [24] -->
• Discarding too many data sets with small linear correlation, which may lead to the loss of valuable information on the interrelationships between SDGs.

<!-- b000359 | furniture | pages [25] -->
Team # 2304962

<!-- b000360 | furniture | pages [25] -->
Page 24 of 24

<!-- b000361 | heading | pages [25] -->
References

<!-- b000362 | references | pages [25] -->
[1] Nasir Ahmad, Sybil Derrible, Shunsuke Managi. A network-based frequency analysis of In-

<!-- b000363 | references | pages [25] -->
clusive Wealth to track sustainable development in world countries. Journal of Environmental

<!-- b000364 | references | pages [25] -->
Management, 2018.

<!-- b000365 | references | pages [25] -->
[2] Cameron Allen, Graciela Metternicht, Thomas Wiedmann. National pathways to the Sustain-

<!-- b000366 | references | pages [25] -->
able Development Goals (SDGs): A comparative review of scenario modelling tools. Envi-

<!-- b000367 | references | pages [25] -->
ronmental Science & Policy, Volume 66, 2016.

<!-- b000368 | references | pages [25] -->
[3] Ana Paula Barbosa-Póvoa, Cátia da Silva, Ana Carvalho. Opportunities and challenges in sus-

<!-- b000369 | references | pages [25] -->
tainable supply chain: An operations research perspective. European Journal of Operational

<!-- b000370 | references | pages [25] -->
Research, Volume 268, Issue 2, 2018.

<!-- b000371 | references | pages [25] -->
[4] Morten Bidstrup, Lone Kørnøv, Maria Rosário Partidário. Cumulative effects in strategic en-

<!-- b000372 | references | pages [25] -->
vironmental assessment: The influence of plan boundaries. Environmental Impact Assess-

<!-- b000373 | references | pages [25] -->
ment Review, Volume 57, 2016.

<!-- b000374 | references | pages [25] -->
[5] Viktor Sebestyén, Miklós Bulla, Ákos Rédey, János Abonyi. Network model-based analysis

<!-- b000375 | references | pages [25] -->
of the goals, targets and indicators of sustainable development for strategic environmental

<!-- b000376 | references | pages [25] -->
assessment. Journal of Environmental Management, Volume 238, 2019.

<!-- b000377 | references | pages [25] -->
[6] Viktor Sebestyén, Miklós Bulla, Ákos Rédey, János Abonyi. Data-driven multilayer complex

<!-- b000378 | references | pages [25] -->
networks of sustainable development goals. Data in Brief, Volume 25, 2019. The World Bank

<!-- b000379 | references | pages [25] -->
[7] Dataset of All Indicators. 2018. https://data.worldbank.org/indicator?tab=all
