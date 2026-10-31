# P-D-2022-2224178-5906c8e3

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Problem Chosen D 2022 MCM/ICM Summary Sheet Team Control Number 2224178

<!-- b000002 | title | pages [1] -->
Voice of Logistics: Focus on Data Governance

<!-- b000003 | heading | pages [1] -->
Summary

<!-- b000004 | prose | pages [1] -->
As an essential asset of port, data plays an increasingly important role in the daily operation of port enterprises. Achieving effective integration of data from multiple subjects involved in port logistics (e.g. people, technology and process) is essential to deepen the construction of data and analytics (D&A) systems and improve the production efficiency of port enterprises.

<!-- b000005 | prose | pages [1] -->
For Session 1, aiming to realize a comprehensive assessment and optimization of the maturity of ICM’s D&A system, this paper innovatively proposed to establish a standard D&A system meta-network model for port logistics as the basis for subsequent work. According to the expectations of ICM Corporation for the D&A system, this paper selected people, technology, process and data information as the modeling objects of the meta-network. Specific modeling elements and correlations were identified through government documents, institution reports, and academic publications. Finally, a standard D&A system meta-network model of port logistics with 33 nodes and 199 links was developed.

<!-- b000006 | prose | pages [1] -->
For Session 2, to select comprehensive D&A system maturity assessment indicators, a standard D&A system meta-network analysis (MNA) was conducted in this paper. From the perspective of effective integration of people, technology, process and data information of port logistics system, this paper selected 12 D&A system maturity evaluation indicators such as Process Data Information Needs Congruence and Data Information Based Task Completion. Subsequently, this paper used the indicator data obtained from Monte Carlo stochastic simulation as the input data of PCA to develop a quantitative assessment model for the D&A system maturity. We selected Mediterranean Shipping Company S.A as an application to demonstrate using MNA-PCA for D&A system maturity assessment. According to the analysis results, the score of illustrative enterprise’s D&A system maturity was 85.14, and it was found that the enterprise should strengthen the construction of customs release information and in-port consolidation and distribution information.

<!-- b000007 | prose | pages [1] -->
For Session 3, this paper proposed to simulate the performance of the enterprise port logistics D&A system by developing a stochastic Petri net (SPN) model that is isomorphic to the meta-network. The average delay time of in-port transportation equipment of the illustrative enterprise was simulated using the SPN model and optimized based on the standard D&A system meta-network. According to the simulation results, the average detention time of transportation equipment was reduced from 140.17 minutes to 85.98 minutes, with a 38.7% reduction.

<!-- b000008 | prose | pages [1] -->
For Session 4, based on the model’s effectiveness, we provided ICM companies with recommendations for applying the model developed in this paper. This paper detailed the critical steps needed to apply the model to other industries.

<!-- b000009 | keywords | pages [1] -->
Keywords: Data and analytics (D&A) system; Meta-network; PCA; Stochastic Petri net (SPN); Monte Carlo simulation

<!-- b000010 | heading | pages [2] -->
Contents

<!-- b000011 | contents | pages [2] -->
1 Introduction ...................................................................................................... 3

<!-- b000012 | contents | pages [2] -->
1.1 Problem Background ....................................................................................................... 3

<!-- b000013 | contents | pages [2] -->
1.2 Our Work .......................................................................................................................... 3

<!-- b000014 | contents | pages [2] -->
2 Preparation of the Models ............................................................................... 5

<!-- b000015 | contents | pages [2] -->
2.1 Assumptions ..................................................................................................................... 5

<!-- b000016 | contents | pages [2] -->
2.2 Notations .......................................................................................................................... 5

<!-- b000017 | contents | pages [2] -->
3 Model 1: Port Logistics D&A System Meta-Network Model ...................... 5

<!-- b000018 | contents | pages [2] -->
3.1 Meta-Network Model ....................................................................................................... 5

<!-- b000019 | contents | pages [2] -->
3.2 Identification of Port Logistics Elements ........................................................................ 6

<!-- b000020 | contents | pages [2] -->
3.3 The Establishment of Port Logistics D&A System Meta-Network Model ...................... 7

<!-- b000021 | contents | pages [2] -->
4 Model 2: MNA-PCA Based D&A System Maturity Assessment ................. 8

<!-- b000022 | contents | pages [2] -->
4.1 Maturity Assessment Indicators for D&A System Based on MNA ................................. 9

<!-- b000023 | contents | pages [2] -->
4.2 Principal Component Analysis ....................................................................................... 11

<!-- b000024 | contents | pages [2] -->
4.3 Development of D&A System Maturity Assessment System ........................................ 11

<!-- b000025 | contents | pages [2] -->
4.4 D&A System Maturity Assessment Application Demonstration and Recommendations

<!-- b000026 | contents | pages [2] -->
.............................................................................................................................................. 13

<!-- b000027 | contents | pages [2] -->
5 Model 3: Stochastic Petri Net for the Port Logistics Optimization

<!-- b000028 | contents | pages [2] -->
Isomorphic with D&A System Meta-Network ............................................... 14

<!-- b000029 | contents | pages [2] -->
5.1 Basic Theory of Stochastic Petri Nets (SPN)................................................................. 14

<!-- b000030 | contents | pages [2] -->
5.2 Stochastic Petri Net Modelling for the Port Logistics Optimization ............................. 15

<!-- b000031 | contents | pages [2] -->
5.3 Port Logistics Optimization for the Illustrative Enterprise ............................................ 18

<!-- b000032 | contents | pages [2] -->
6 Sensitivity Analysis ......................................................................................... 20

<!-- b000033 | contents | pages [2] -->
6.1 Sensitivity Analysis of the Standard Port Logistics D&A System Maturity ................. 20

<!-- b000034 | contents | pages [2] -->
6.2 Sensitivity Analysis of the Illustrative Enterprise Port Logistics SPN .......................... 20

<!-- b000035 | contents | pages [2] -->
7 Application Recommendations for ICM Corporation’s D&A System and

<!-- b000036 | contents | pages [2] -->
Model Extensions .............................................................................................. 21

<!-- b000037 | contents | pages [2] -->
7.1 D&A System Application Recommendations ................................................................ 21

<!-- b000038 | contents | pages [2] -->
7.2 Model’s Industry Extensions .......................................................................................... 21

<!-- b000039 | contents | pages [2] -->
8 Model Evaluation ........................................................................................... 22

<!-- b000040 | contents | pages [2] -->
8.1 Strengths ........................................................................................................................ 22

<!-- b000041 | contents | pages [2] -->
8.2 Weaknesses .................................................................................................................... 23

<!-- b000042 | furniture | pages [3] -->
Team # 2224178

<!-- b000043 | furniture | pages [3] -->
Page 3 of 24

<!-- b000044 | heading | pages [3] -->
1 Introduction

<!-- b000045 | heading | pages [3] -->
1.1 Problem Background

<!-- b000046 | prose | pages [3] -->
As an important asset owned by the enterprise, data governance refers to its correctness and timeliness, control of data flow, permissions and management of security. The correct ap- plication of the data and analytics (D&A) system should be based on accurate and reasonable data. Port logistics service is a complex system engineering. The organization of port logistics services involves government regulatory agencies, port enterprises and various types of logis- tics service providers and customers in multiple departments and units. Its business side in- volves port inspection, logistics and transportation, customs clearance and review, and many other aspects. Establishing the data and analytics D&A system can help improve its overall operational efficiency and service quality.

<!-- b000047 | prose | pages [3] -->
The specific requirements of this question are as follows：  Develop a D&A system maturity assessment indicator system and apply it to the il- lustrative enterprise’s D&A system assessment.

<!-- b000048 | prose | pages [3] -->
 Demonstrate how to use the developed model to maximize the value of enterprise data assets.

<!-- b000049 | prose | pages [3] -->
 Apply the model to evaluate and optimize ICM’s D&A system.

<!-- b000050 | prose | pages [3] -->
 Expand the application of the developed model to other companies or industries.

<!-- b000051 | heading | pages [3] -->
1.2 Our Work

<!-- b000052 | prose | pages [3] -->
Since this question did not give any port operation data for ICM Corporation, a quantita- tive model that can effectively integrate multiple types of essential information, the meta-net- work model, was developed as a basis for subsequent maturity assessment and process optimi- zation. According to ICM Corporation’s target requirements for the D&A system, we selected people, technology, process and data information as the modeling elements of the meta-net- work. Through literature analysis, we classified the types of people, technology, process and relevant data information involved in port logistics services and analyzed the correlations be- tween the elements. We integrated port logistics services’ components and associated relation- ships into a network to establish a standard D&A system meta-network model.

<!-- b000053 | prose | pages [3] -->
To comprehensively assess the maturity of the D&A system, we need to analyze the multi- level network indicators to select maturity indicators based on the established D&A system meta-network model. This paper selected 12 indicators such as Data Information Based Process Completion (DIBPC), Data Information Negotiation (DIN), and Process Data Information Needs Congruence (PDINC) as the critical indicators to measure the performance of people, technologies and processes in the D&A system. Due to the lack of data on the operation of the business, this paper used Monte Carlo simulations to capture the changes in the D&A system maturity assessment indicators under different scenarios. Principal component analysis was used to reduce the dimensionality of the indicator data in the Monte Carlo simulation and es- tablish a maturity assessment model based on the D&A system meta-network. We applied the maturity model to Mediterranean Shipping Company S.A as an application demonstration of the model for ICM Corporation.

<!-- b000054 | furniture | pages [4] -->
Team # 2224178

<!-- b000055 | furniture | pages [4] -->
Page 4 of 24

<!-- b000056 | prose | pages [4] -->
For ICM Corporation to maximize the benefit of its data information and reduce the transit time, this paper developed a Stochastic Petri Net (SPN) isomorphic to the D&A system meta- network. The SPN model is established by corresponding the elements of port logistics in the SPN to the elements in the D&A system meta-network and inheriting the correlation relation- ships between the elements in the meta-network. This paper selected the illustrative enterprise for the D&A system maturity assessment as the object of SPN logistics process optimization. This paper used the SPN model to simulate delays in the port logistics system of the illustrative enterprise and optimized the system based on the standard D&A system meta-network.

<!-- b000057 | prose | pages [4] -->
Finally, based on the model’s effectiveness, we recommended the established D&A sys- tem maturity assessment and optimization models to ICM. This paper detailed how the models can be extended to other enterprises or industries. A letter related to the maturity of ICM Cor- poration’s port logistics services D&A system is also provided to ICM Corporation’s customers to increase their confidence in the data practices.

<!-- b000058 | prose | pages [4] -->
Step 1. Develop the Port Logistics D&A System Meta-Networks

<!-- b000059 | prose | pages [4] -->
Develop Meta-matrices Collect data

<!-- b000060 | prose | pages [4] -->
 Government profiles 11 10 0 0 0 … 1 … 10 0 1 … 1 0 0 0 0 0 … … …

<!-- b000061 | prose | pages [4] -->
 Institutions/associations reports Determine nodes and links … … … … … … … … … … … … 0 0 0 1 … 1 … 0 0 1 … 0

<!-- b000062 | prose | pages [4] -->
 Academic publications c 01 11 0 0 1 … 0 …

<!-- b000063 | prose | pages [4] -->
 Nodes: A, T, P, I 1 0 1 0 … … … … … … … … … …

<!-- b000064 | prose | pages [4] -->
 …… 0 1 0 1 … 0 … 0

<!-- b000065 | prose | pages [4] -->
 Links: AT, AP, AI, TP, TI, 11 10 0 0 … 0 1 … guideline actual 1 0 0 0 … … TT, PP, PI and II … … … … … … … … information information 0 0 0 … 1 1 … 0

<!-- b000066 | prose | pages [4] -->
Visualize Meta-Networks

<!-- b000067 | prose | pages [4] -->
AA Network AT Network AP Network TI Network

<!-- b000068 | prose | pages [4] -->
PP Network PI Network AI Network

<!-- b000069 | prose | pages [4] -->
Step 2. Assess the D&A System Maturity Based on MNA-PCA MNA Quantify PCA Analyze

<!-- b000070 | heading | pages [4] -->
System maturity results

<!-- b000071 | prose | pages [4] -->
Meta-network measures

<!-- b000072 | prose | pages [4] -->
 Data information/technology People Technology Omega

<!-- b000073 | prose | pages [4] -->
 Overall task completion

<!-- b000074 | prose | pages [4] -->
 Process technology/data Data Process information needs information

<!-- b000075 | prose | pages [4] -->
 ……

<!-- b000076 | prose | pages [4] -->
Step 3. Optimize Port Logistics Based on Stochastic Petri Net

<!-- b000077 | heading | pages [4] -->
System simulation results

<!-- b000078 | prose | pages [4] -->
P Mapping & Optimization

<!-- b000079 | prose | pages [4] -->
λ3 λ9

<!-- b000080 | prose | pages [4] -->
Feedback & Learning Simulation & Emulation

<!-- b000081 | prose | pages [4] -->
Stochastic Petri Net

<!-- b000082 | caption | pages [4] -->
Fig. 1 Technology roadmap for this paper

<!-- b000083 | furniture | pages [5] -->
Team # 2224178

<!-- b000084 | furniture | pages [5] -->
Page 5 of 24

<!-- b000085 | heading | pages [5] -->
2 Preparation of the Models

<!-- b000086 | heading | pages [5] -->
2.1 Assumptions

<!-- b000087 | prose | pages [5] -->
1. ICM Corporation’s port-related business is not likely to change significantly shortly.

<!-- b000088 | prose | pages [5] -->
2. The maturity of the D&A system is only influenced by the people, technology, process and data information in the introduction to the problem.

<!-- b000089 | prose | pages [5] -->
3. The illustrative enterprise is consistent with the nature of ICM Corporation and is a good representation of the operations of ICM Corporation.

<!-- b000090 | prose | pages [5] -->
4. There is no conflict between the needs of the different departments in the ICM Corpo- ration management team.

<!-- b000091 | heading | pages [5] -->
2.2 Notations

<!-- b000092 | prose | pages [5] -->
The key mathematical notations used in this paper are listed in Table 1.

<!-- b000093 | caption | pages [5] -->
Table 1 Notations used in this paper

<!-- b000094 | prose | pages [5] -->
Symbol Description 𝑓௘ The 𝑒th principal component score 𝛽௘ The weight of the 𝑖th principal component DIBTC Data Information Based Task Completion DIO Data Information Omega PTNC Process Technology Needs Congruence TO Technology Omega 𝑁ഥ The average token of the places The average system delay time 𝑁

<!-- b000095 | heading | pages [5] -->
3 Model 1: Port Logistics D&A System Meta-Network Model

<!-- b000096 | prose | pages [5] -->
The primary purpose of this section is to establish a port logistics D&A system meta- network to realize the integration of data information, people, technology and process and pro- vide a basis for subsequent D&A system maturity assessment and optimization.

<!-- b000097 | heading | pages [5] -->
3.1 Meta-Network Model

<!-- b000098 | prose | pages [5] -->
Carley et al. (2007) proposed the concept of meta-network, which is a multi-level social network that includes multiple organizational elements (Carley et al., 2007). Meta-network has a ‘tree-like’ hierarchical structure and can be seen as mapping multiple homogeneous or heter- ogeneous sub-network. By analyzing the meta-network model as a whole or more sub-networks within the meta-network, critical information about the structural characteristics of the system can be obtained.

<!-- b000099 | prose | pages [5, 6] -->
Pestov (2009) argued that any natural system, such as society or organization, can be rep- resented by a meta-network (Pestov, 2009). Various entities or elements in a system, including people, data information and resources, can be captured as meta-network nodes, as shown in uncertainty. Therefore, the port logistics system is complex, with a hierarchy composed of mul- tiple subjects. Based on the characteristics of ICM Corporation’s port logistics system and the objectives of ICM’s D&A system, we can learn that the meta-network model is well suited to this problem. The main steps in developing a meta-network model are identifying nodes and links.

<!-- b000100 | caption | pages [5] -->
Fig. 2. The port logistics services are characterized by large scale, multiple associations and

<!-- b000101 | furniture | pages [6] -->
Team # 2224178

<!-- b000102 | furniture | pages [6] -->
Page 6 of 24

<!-- b000104 | prose | pages [6] -->
Nodes People Technology Data Inforamtion Process

<!-- b000105 | caption | pages [6] -->
Fig. 2 Basic meta-network concept diagram

<!-- b000106 | heading | pages [6] -->
3.2 Identification of Port Logistics Elements

<!-- b000107 | prose | pages [6] -->
During the port logistics D&A system analysis, there is a non-negligible correlation be- tween many factors such as people, technology, process, and data information. This paper needs to decompose the processes at the system level, analyze the various factors included, and con- sider the correlations.

<!-- b000108 | prose | pages [6] -->
Based on relevant technical specifications, government documents and related literature, this paper identifies a total of 33 critical elements based on the core of the port logistics trans- portation process (Almotairi and Lumsden, 2009). The identification results of port logistics elements are shown in Table 2.

<!-- b000109 | caption | pages [6] -->
Table 2 Identification of port logistics elements

<!-- b000110 | prose | pages [6, 7] -->
Category ID ID Meaning P1 Vessel arrival P2 Vessels waiting for berth allocation P3 Vessel approaching the port P4 Container liner P5 Bill review Process P6 Loading and unloading operations P7 Assembled goods P8 Stockpile storage P9 Intra-port consolidation vehicle transportation P10 Customs supervision and release P11 Registration information ship leaving the post I1 Regulatory release information Data I2 Container liner information Information I3 Loading and unloading machinery information I4 Stockyard information I5 Intra-port information I6 Railroad port station information I7 Vessel information T1 Technology for loading and unloading operations T2 Berth operation technology T3 Container box source organization technology T4 Stacking and mechanical loading and unloading synergistic technology Technology Cooperative technology of collecting and transporting machinery and loading and T5 unloading machinery T6 Cooperative technology of berth operation and loading/unloading operation T7 Modern information technology A1 Customs inspector A2 Port commanders A3 Valets A4 Longshoreman People A5 Freight forwarder A6 Loading and unloading machinery operators A7 Accountant A8 Shipper

<!-- b000111 | furniture | pages [7] -->
Team # 2224178

<!-- b000112 | furniture | pages [7] -->
Page 7 of 24

<!-- b000114 | heading | pages [7] -->
3.3 The Establishment of Port Logistics D&A System Meta-Network Model

<!-- b000115 | prose | pages [7] -->
Based on the identified port logistics elements, four-element types (i.e. Process (P), Data Information (I), People (A) and Technology (T)) are identified as meta-network four-dimen- sional nodes. In order to develop the port logistics D&A system and sort out the correlations between the elements of entities in port logistics, which are transformed into links between nodes, the standard port logistics D&A system meta-network is developed, as shown in Fig. 3. The port logistics D&A system meta-network will be explained in detail below.

<!-- b000116 | prose | pages [7, 8] -->
People Information Process Technology In the port logistics D&A system meta-network model, there are unidirectional or bidirec- tional associations between different nodes, and the following types of association networks are developed according to different associations in this paper, as shown in Table 3. For exam- ple, AP Net refers to the involvement of certain people needed to complete a specific process. TP Net refers to the skills required to complete a specific process. AI Net refers to the data in- formation that someone has. The structural characteristics of a port logistics system can be described by analyzing the entire meta matrix or one or more networks in the matrix. The as- sociated sub-network based on the node relationship matrix is shown in Fig. 4. By analyzing the meta-network, we can obtain practically meaningful multidimensional network indicators, which will be specified in 4.2 Maturity Assessment Indicators for D&A System Based on MNA.

<!-- b000117 | caption | pages [7] -->
Fig. 3 The standard port logistics D&A system meta-network model

<!-- b000118 | furniture | pages [8] -->
Team # 2224178

<!-- b000119 | furniture | pages [8] -->
Page 8 of 24

<!-- b000121 | caption | pages [8] -->
Table 3 Port logistics D&A system meta matrix

<!-- b000122 | prose | pages [8] -->
People Technology Process Data Information People -- AT Net AP Net AI Net Technology -- TT Net TP Net TI Net Process -- -- PP Net PI Net Data Information -- -- -- II Net

<!-- b000123 | prose | pages [8] -->
People People People Technology Information Process

<!-- b000124 | prose | pages [8] -->
AI Net: Who knows which AP Net: Who is assigned to which process AT Net: Who knows which technology data information Information Information Process Process

<!-- b000125 | prose | pages [8] -->
II Net: Interaction between data IP Net: Which data information is required PP Net: Which process is relied on which information for which process process

<!-- b000126 | prose | pages [8] -->
Information Technology Technology Technology Process

<!-- b000127 | prose | pages [8] -->
IT Net: Which technology know which TP Net: Which technology is required for data information which process TT Net: Interaction between technology

<!-- b000128 | caption | pages [8] -->
Fig. 4 Port logistics D&A system meta-network sub-network system diagram

<!-- b000129 | heading | pages [8] -->
4 Model 2: MNA-PCA Based D&A System Maturity Assessment

<!-- b000130 | prose | pages [8] -->
In this section, the meta-network analysis (MNA) was carried out based on ICM’s D&A system targets, and indicators were selected that enable a comprehensive assessment of the D&A system maturity. This paper calculated the indicator dataset through Monte Carlo simu- lation and performed principal component analysis (PCA) to determine the indicator weights.

<!-- b000131 | furniture | pages [9] -->
Team # 2224178

<!-- b000132 | furniture | pages [9] -->
Page 9 of 24

<!-- b000133 | prose | pages [9] -->
Finally, the model was applied to company Mediterranean Shipping Company S.A as an appli- cation demonstration.

<!-- b000134 | heading | pages [9] -->
4.1 Maturity Assessment Indicators for D&A System Based on MNA

<!-- b000135 | prose | pages [9] -->
The target of developing a D&A system is to maximize the use of data assets by enhancing the correlation between people, technology and process to form collaborative management of the whole life cycle. The key to the selection of indicators is to describe the collaborative pro- cess of people, technology and data information during the completion of logistics operations to achieve a comprehensive assessment of the maturity of the D&A system. Therefore, this paper selects a multi-layered network assessment indicator with a core of the process, as shown below. All computed elements in the following are the meta-network 0-1 relationship matrix as represented in Table 3 and are calculated as matrix operations.

<!-- b000136 | prose | pages [9] -->
 Agent Data Information Needs Congruence (ADINC): This indicator represents the amount of data information that is missing for the agent to complete its assigned pro- cess. Let NDI = AP*IP’ = data information needed by agents to do their assigned process. The formula for the ADINC for agent 𝑖 is shown in Equation (1).

<!-- b000137 | prose | pages [9] -->
𝐴𝐷𝐼𝑁𝐶௜= 𝑠𝑢𝑚(𝑁𝐷𝐼(𝑖, : ) .∗~𝐴𝐼(𝑖, : )) (1) 𝑠𝑢𝑚(𝑁𝐷𝐼(𝑖, : ))  Agent Technology Needs Congruence (ATNC): This indicator represents the amount of technology missing for the agent to complete its assigned process. Let NT = AP*TP’ = technology agents need to do their assigned process. The formula is familiar with that of ADINC.

<!-- b000138 | prose | pages [9] -->
 Process Data Information Needs Congruence (PDINC): The number of data infor- mation not supplied to a process, but required to do the process, is expressed as a fraction of the total knowledge required for the task. It is similar to Agent Data Infor- mation Needs Congruence but quantifies only the undersupply of data information to tasks, as shown in Equation (2).

<!-- b000139 | prose | pages [9] -->
𝑃𝐷𝐼𝑁𝐶௜= 𝑠𝑢𝑚(𝐼𝑃′(𝑖, : ) .∗~(𝐴𝑃ᇱ∗𝐴𝐼(𝑖, : )) (2) 𝑠𝑢𝑚(𝐼𝑃′(𝑖, : ))  Process Technology Needs Congruence (PTNC): This is Process Data Information Needs Congruence with the data information-based networks replaced with the cor- responding technology-based networks.

<!-- b000140 | prose | pages [9] -->
 Data Information Actual Workload (DIAW): The data information an agent uses to perform the processes to which it is assigned. DIAW for agent 𝑖 is computed as Equation (3):

<!-- b000141 | prose | pages [9] -->
𝐷𝐼𝐴𝑊௜= [𝐴𝐼∗𝐼𝑃∗𝐴𝑃′](𝑖, 𝑖) (3) 𝑠𝑢𝑚(𝐼𝑃)  Technology Actual Workload (TAW): The technology an agent uses to perform the processes to which it is assigned. The formula can be found in DIAW.

<!-- b000142 | prose | pages [9] -->
 Data Information Based Task Completion (DIBTC): The fraction of the assigned pro- cesses that can be completed by agents based on data information. DIBTC for agent 𝑖 is computed as Equation (4):

<!-- b000143 | furniture | pages [10] -->
Team # 2224178

<!-- b000144 | furniture | pages [10] -->
Page 10 of 24

<!-- b000145 | prose | pages [10] -->
𝐷𝐼𝐵𝑇𝐶௜= |𝑇| −|(𝐼𝑃ᇱ−𝐴𝑃ᇱ∗𝐴𝐼)| (4) |𝑇|  Technology Based Task Completion (TBTC): This is Data Information Based Task Completion with the data information-based networks replaced with the correspond- ing technology-based networks.

<!-- b000146 | prose | pages [10] -->
 Social Technical Congruence (STC): The proportion of the overall needs of a process that are met by the coordination of people working through a process. STC for agent 𝑖 is computed as Equation (5):

<!-- b000147 | prose | pages [10] -->
𝑆𝑇𝐶௜= 𝑠𝑢𝑚[𝐼(( 𝐴𝑃∗𝑃𝑃∗𝐴𝑃ᇱ).∗𝐴𝐴> 0)] (5) 𝑠𝑢𝑚(𝐼(( 𝐴𝑃∗𝑃𝑃∗𝐴𝑃ᇱ) > 0)) where, 𝐼(𝐴> 0) denotes a function that if true returns a value of 1.

<!-- b000148 | prose | pages [10] -->
 Agent Socio Technology-Information Power (ASTIP): A measure of actor power based on access to data information, technology, and process. ASTIP is the Out-De- gree Centrality of the binarized concatenated network: [AT AI AP]  Data Information Omega (DIO): The degree to which agents reuse data information while doing their processes. DIO for agent 𝑖 is computed as Equation (6):

<!-- b000149 | prose | pages [10] -->
𝐷𝐼𝑂௜= 𝑠𝑢𝑚[(( 𝑇ᇱ.∗𝐴𝑇ᇱ∗𝐴𝑇).∗𝐾𝑇ᇱ).∗𝐾𝑇′] (6) 𝑠𝑢𝑚(𝐾𝑇)  Technology Omega (TO): The degree to which agents reuse technology while doing their processes. This is Data Information Omega with the data information-based net- works replaced with the corresponding technology-based networks.

<!-- b000150 | prose | pages [10] -->
The indicators selected above address the concerns of ICM Corporation’s management team, as shown in Table 5. The results of the standard D&A system maturity assessment met- rics are shown in Table 6.

<!-- b000151 | caption | pages [10] -->
Table 5 Indicators and concerns solved table

<!-- b000152 | prose | pages [10] -->
Indicators Solved concerns Agent Data Information Needs Congruence Cataloging of data assets; Process Data Information Needs Congruence Integration of people, technology, processes and data in- Data Information Actual Workload formation; Data Information Based Task Completion Data governance. Data Information Omega Agent Technology Needs Congruence Process Technology Needs Congruence Skills of recruited staff; Technology Actual Workload Staff training; Technology Based Task Completion Technical solution reliability measurement. Technology Omega Agent Socio Technology-Information Power Determination of talent reserve deficiencies;

<!-- b000153 | prose | pages [10] -->
Determination of the number of employees; Social Technical Congruence Selection of talents in demand.

<!-- b000154 | caption | pages [10] -->
Table 6 Calculation of standard D&A system maturity indicators

<!-- b000155 | prose | pages [10, 11] -->
Indicators Value Indicators Value Indicators Value Indicators Value ATNC 0.188 DIBTC 0.636 DIAW 0.522 STC 0.675 TAW 0.287 PTNC 0.364 DIBTC 0.364 ASTIP 0.385 TBTC 0.727 DIO 0.353 PDINC 0.235 TO 0.682

<!-- b000156 | furniture | pages [11] -->
Team # 2224178

<!-- b000157 | furniture | pages [11] -->
Page 11 of 24

<!-- b000159 | heading | pages [11] -->
4.2 Principal Component Analysis

<!-- b000160 | prose | pages [11] -->
Principal Component Analysis (PCA) is a multivariate statistical method (Wold et al., 1987). PCA converts a set of correlated variables into a set of orthogonal, uncorrelated varia- bles using an orthogonal transformation called a principal component. The modeling steps for PCA are shown in following steps.

<!-- b000161 | prose | pages [11] -->
Step 1: Calculate the component score.

<!-- b000162 | prose | pages [11] -->
௡ (7) 𝛿௜= ෍𝛽௘𝑓௘ ௘ୀଵ where 𝑓௘ denotes the 𝑒th principal component score and the weight of the 𝑖th principal component is denoted by 𝛽௘.

<!-- b000163 | prose | pages [11] -->
Step 2: Calculate the information contribution and cumulative contribution of each com- ponent eigenvalue.

<!-- b000164 | prose | pages [11] -->
𝜆௜ ，𝑖= 1,2, … ,9 (8) 𝑏௜= ௜ ∑ 𝜆ఏ ఏୀଵ ௣ ∑ 𝜆௘ ௘ୀଵ (9) 𝛼௘= ଽ ∑ 𝜆ఏ ఏୀଵ where 𝑏௜ is the contribution of each component 𝑋௜ is the information contribution and 𝛼௘ is the cumulative contribution of each component.

<!-- b000165 | prose | pages [11] -->
Step 3: Calculate the overall score.

<!-- b000166 | prose | pages [11] -->
௡ (10) 𝛿௜= ෍𝛽௘𝑏௘ ௘ୀଵ where 𝑏௘ is the information contribution of the 𝑒th principal component, and a compre- hensive evaluation can be made based on the combined score.

<!-- b000167 | heading | pages [11] -->
4.3 Development of D&A System Maturity Assessment System

<!-- b000168 | prose | pages [11] -->
We performed 50 Monte Carlo simulations to randomly remove elements from a standard port logistics D&A system meta-network model. Data from 50 D&A system maturity assess- ment simulations were recorded and used as the input data set for the PCA. Due to space limi- tations, only some of the Monte Carlo simulation data is shown in Table 6.

<!-- b000169 | prose | pages [11, 12] -->
Indicators/Simulation times 1 2 3 4 5 … 48 49 50 ATNC 0.205 0.22 0.205 0.225 0.243 … 0.2 0.225 0.196 TAW 0.273 0.267 0.273 0.258 0.292 … 0.281 0.258 0.289 TBTC 0.727 0.182 0.455 0.727 0.727 … 0.7 0.576 0.8 … … … … … … … … … … ASTIP 0.411 0.343 0.406 0.366 0.377 … 0.385 0.38 0.391 The PCA was performed on the maturity assessment system using MATLAB. According to the calculated results, the cumulative variance contribution of the first six principal compo- nents reached 85%, and their characteristic roots were 𝜆ଵ= 3.84, 𝜆ଶ= 2.30, 𝜆ଷ= 1.65, 𝜆ସ= 1.32, and 𝜆ହ= 1.14. Therefore, the first 5 principal components were selected as indicators in this paper. The PCA calculated fragmentation diagram is shown in Fig. 5.

<!-- b000170 | furniture | pages [12] -->
Team # 2224178

<!-- b000171 | furniture | pages [12] -->
Page 12 of 24

<!-- b000173 | prose | pages [12] -->
4.0 3.84 3.5 Characteristic roots 3.0

<!-- b000174 | prose | pages [12] -->
2.5 2.3 2.0 1.65 1.5 1.321.14 1.0 0.77 0.5 0.410.320.160.060.01 0.0

<!-- b000175 | prose | pages [12] -->
-0.5 0 2 4 6 8 10 12 Principal component ID

<!-- b000176 | caption | pages [12] -->
Fig. 5 PCA fragmentation diagram

<!-- b000177 | prose | pages [12] -->
The results of the linear combination coefficients and weights of the PCA principal com- ponents are shown in Table 7.

<!-- b000178 | caption | pages [12] -->
Table 7 Linear combination coefficients and weighting results

<!-- b000179 | prose | pages [12] -->
Component Component Component Component Component 1 2 3 4 5 Weight Feature Root 3.84 2.301 1.654 1.319 1.141 Variance 32.00% 19.17% 13.78% 10.99% 9.51% Extraction ATNC 0.36 0.24 0.24 0.29 0.27 10.3% TAW 0.17 0.55 0.12 0.20 0.06 8.28% RBTC 0.01 0.30 0.65 0.13 0.19 7.58% DIBTC 0.41 0.30 0.12 0.17 0.12 9.62% PTNC 0.49 0.01 0.07 0.05 0.14 7.66% DIO 0.21 0.48 0.17 0.31 0.06 9.13% … … … … … … … The expression for the overall D&A system maturity score is shown in Equation (11). Its weight distribution tree diagram is shown in Fig. 6.

<!-- b000180 | prose | pages [12] -->
𝐹= 0.1037𝐴𝑇𝑁𝐶+ 0.0962𝐵𝐼𝐷𝑇𝐶+ 0.0920𝑆𝑇𝐶+ 0.0913𝐷𝐼𝑂+ 0.0912𝑇𝑂 (11) + 0.0909𝐷𝐼𝐴𝑊+ 0.8028𝑇𝐴𝑊+ 0.0766𝑃𝑇𝑁𝐶+ 0.0758𝑅𝐵𝑇𝐶 + 0.0709𝐷𝐼𝐵𝑇𝐶+ 0.0701𝑃𝐷𝐼𝑁𝐶+ 0.0583𝐴𝑆𝑇𝐼𝑃

<!-- b000181 | furniture | pages [13] -->
Team # 2224178

<!-- b000182 | furniture | pages [13] -->
Page 13 of 24

<!-- b000183 | caption | pages [13] -->
Fig. 5 D&A system maturity assessment indicator weighting tree diagram

<!-- b000184 | heading | pages [13] -->
4.4 D&A System Maturity Assessment Application Demonstration and Rec-

<!-- b000185 | prose | pages [13] -->
ommendations

<!-- b000186 | prose | pages [13] -->
Mediterranean Shipping Company S.A is a global company engaged in shipping and lo- gistics, established in 1970, with more than 200 routes deployed in more than 150 countries and territories worldwide, and the second-largest shipping capacity in the world. Our search of the relevant literature and the analysis of the company's financial reports revealed that Medi- terranean Shipping Company S.A has specific problems in terms of information technology and the working capacity of the port command staff (S. et al., 2015).

<!-- b000187 | prose | pages [13] -->
The company’s Regulatory Release Information (I1) and Intra-port information (I5) were not updated on time, resulting in prolonged in-port detention of vessels. In addition, the stack- ing and mechanical loading and unloading synergistic technology (T4) and modern information technology (T7) were relatively backward. Port commanders (A2) sometimes failed at vessels waiting for berth allocation (P2) and customs supervision and release (P10) due to missing real- time data information. Due to lack of authority, longshoreman (A4) cannot obtain stockyard information (I4), resulting in failure to arrive on duty in time. We fed back the deficiencies of the illustrative enterprise to the meta-network model of the standard port logistics D&A system. The specific changes of the meta-network are summarized in Table 8.

<!-- b000188 | caption | pages [13] -->
Table 8 Summary of changes to the meta-network structure

<!-- b000189 | prose | pages [13] -->
Missing type Element ID Missing nodes I1, I5, T4, T7 Missing links A2-P2, A2-P10, A4-I4 We input the above changes into the standard port logistics D&A system meta-network and calculated maturity indicators for the D&A system of the illustrative enterprise. The ratio of the maturity score of the illustrative enterprise to the maturity score of the standard system is used as the final score, which is calculated as 0.8514. The results of calculating the maturity indicators for the illustrative enterprise and the standard system are shown in Fig. 6.

<!-- b000190 | caption | pages [13] -->
Fig. 6 Radar chart comparing the standard system with the illustrative enterprise system indi-

<!-- b000191 | prose | pages [13, 14] -->
cators Based on the calculation results, we can see that the illustrative enterprise’s DIBTC, DIO, PTNC and TO indicators are significantly smaller than the standard system. We were able to calculate through the D&A system meta-network model matrix the links that need to be en- hanced by data information for this business, as summarized in Table 9. Based on the result, the enterprise can strengthen these segments in a targeted manner.

<!-- b000192 | furniture | pages [14] -->
Team # 2224178

<!-- b000193 | furniture | pages [14] -->
Page 14 of 24

<!-- b000195 | caption | pages [14] -->
Table 9 Illustrative enterprise D&A system optimization recommendations

<!-- b000196 | prose | pages [14] -->
Links or nodes to be filled or strengthened Element ID A2-P2, A2-P10, A2-I2, A2-I5, A2-I7, A3-P3, Links A4-I4, A7-T7 Nodes I1, I5, T4, T7, A2, A7

<!-- b000197 | heading | pages [14] -->
5 Model 3: Stochastic Petri Net for the Port Logistics Optimiza-

<!-- b000198 | prose | pages [14] -->
tion Isomorphic with D&A System Meta-Network

<!-- b000199 | prose | pages [14] -->
This section describes how to develop a stochastic Petri net model of port logistics using the illustrative enterprise's D&A system meta-network and simulate the average detention time of the illustrative enterprise's port transport equipment. The illustrative enterprise D&A system is then optimized based on the standard D&A system meta-network model.

<!-- b000200 | heading | pages [14] -->
5.1 Basic Theory of Stochastic Petri Nets (SPN)

<!-- b000201 | prose | pages [14] -->
Petri nets are modelling tools that describe models using specific notations and are often used for process modelling (Lee and Mitici, 2020). It features a graphical, digital modelling tool for various systems, especially discrete-event dynamic systems. It provides a powerful tool for describing and studying information processing systems that are parallel, asynchronous and stochastic.

<!-- b000202 | prose | pages [14] -->
With the stochastic Petri net (SPN) model, the system’s performance can be quantified through a series of transformations to obtain the busy probability, the idle probability, the var- iable utilization, etc., of the repository. In this case, the busy probability of the place reflects the utilization of resources and the active status of the tasks in the actual system. The utilization of the transition reflects information such as system throughput and latency.

<!-- b000203 | prose | pages [14] -->
We define a SPN as a seven-tuple, Σ = (𝑃, 𝑇, 𝐹, 𝐾, 𝑊, 𝑀଴, 𝜆).

<!-- b000204 | prose | pages [14] -->
 Place (𝑃 ○) indicates the location and state of the system, and each circle can hold a certain amount of resources.

<!-- b000205 | prose | pages [14] -->
 Transition (𝑇 ▋) refers to the consumption, use and generation of resources in the system.

<!-- b000206 | prose | pages [14] -->
 Token (·) can be moved between two places, the number of which represents the number of resources in the place.

<!-- b000207 | prose | pages [14] -->
 𝐹 is the set of directed arcs.

<!-- b000208 | prose | pages [14] -->
 𝑊 is the weight function of a directed arc, the set of nodal flow relationships.

<!-- b000209 | prose | pages [14] -->
 𝐾 is a function of the capacity of the library.

<!-- b000210 | prose | pages [14] -->
 𝑀଴ is the initial marker.

<!-- b000211 | prose | pages [14, 15] -->
 𝜆 is the set of average implementation rates of the transition. 𝜆௜ is the average im- plementation rate of the transition, and denotes the number of implementations per unit of time.

<!-- b000212 | furniture | pages [15] -->
Team # 2224178

<!-- b000213 | furniture | pages [15] -->
Page 15 of 24

<!-- b000215 | prose | pages [15] -->
Analyzing the performance of a system based on SPN is described in detail as shown in the following steps.

<!-- b000216 | prose | pages [15] -->
Step 1: Develop a process SPN model by associating a realistic delay to all the transitions based on the model already built.

<!-- b000217 | prose | pages [15] -->
Step 2: Develop a reachable tree based on the known SPN model. According to the dis- tribution of tokens (resources) in the model repository and the triggering rules of transitions, a Markov chain is obtained isomorphically.

<!-- b000218 | prose | pages [15] -->
Step 3: Based on Markov chains, the transfer rate matrix for Markov processes are devel- oped, and the steady-state probabilities are obtained by solving the matrix equations.

<!-- b000219 | prose | pages [15] -->
Step 4: Calculate the final performance metrics to determine the final performance esti- mate required for the entire system described by the model.

<!-- b000220 | heading | pages [15] -->
5.2 Stochastic Petri Net Modelling for the Port Logistics Optimization

<!-- b000221 | prose | pages [15] -->
Before modelling, it is necessary to analyze the specific processes that port logistics needs to go through and then map the critical elements of these processes to the process elements in the SPN. The system initializes the location of the resource, which is reflected in the SPN model as the initial identification, and in the case of port logistics transport processes, the re- source can be a container or a transport truck. The state and condition of the resource, the corresponding element in the SPN model, is the library. Place corresponds to people, technol- ogy and data information in the developed standard D&A system meta-network. Transitions represent the state of use or progress, corresponding to the process element in the standard D&A system meta-network. The logical relationships between place and transition in the SPN use the same logical links as the meta-network links. Corresponding the elements of the D&A system meta-network to the essential elements of the SPN is the basis for subsequent work. The workload of Petri net modelling is significantly reduced by developing an SPN that is isomorphic to the D&A system meta-network, improving the efficiency of the study.

<!-- b000222 | prose | pages [15] -->
Based on the detailed analysis and description of the illustrative enterprise’s port logistics D&A system meta-network, the processes are modelled with the basic Petri net modelling methods and principles. The illustrative enterprise’s SPN model of the port logistics D&A sys- tem is shown in Fig. 7. The colors in the diagram remain the same as the colors of the node types in the meta-network. The specific meanings of place and transition in the illustrative enterprise’s SPN are shown in Table 10.

<!-- b000223 | prose | pages [15] -->
P5 T4 P6 T5 P7 T6 P8 T7

<!-- b000224 | prose | pages [15] -->
P1 T1 P2 T2

<!-- b000225 | prose | pages [15] -->
P9 P3 T3 P4

<!-- b000226 | prose | pages [15] -->
P15 T13

<!-- b000227 | prose | pages [15, 16] -->
P14 T12 P13 T11 P12 T10 P11 T9 P10 T8 Place Meaning Transi- Meaning tion P1 Shipper (A8) T1 Ship arriving in port (P1) P2 Vessel information (I7) T2 Vessel waiting for berth allocation (P2) P3 Regulatory release information (I1) T3 Vessel approaching port (P3) P4 Container liner information (I2) T4 Container liner (P4) P5 Accountant (A7) T5 Bill review (P5) P6 Loading and unloading machinery infor- T6 Loading and unloading operations (P6) mation (I3) P7 Stockyard information (I4) T7 Loading and unloading operations (P6) P8 Longshoreman (A4) T8 Stockpile storage (P7) P9 Intra-port information (I5) T9 Intra-port consolidation vehicle transport (P9) P10 Longshoreman (A4) T10 Intra-port consolidation vehicle transport (P9) P11 Regulatory release information (I1) T11 Bill review (P5) P12 Accountant (A7) T12 Customs supervision (P10) P13 Customs inspector (A1) T13 Vessels leaving port (P11) P14 Valets (A3) P15 Consignee First, this paper needs to validate the validity of the already established SPN model of the illustrative enterprise. Based on the already established SPN model of the illustrative enterprise port logistics D&A system, the correlation matrix 𝐴 is calculated as Equation (12).

<!-- b000228 | furniture | pages [16] -->
Team # 2224178

<!-- b000229 | furniture | pages [16] -->
Page 16 of 24

<!-- b000230 | caption | pages [16] -->
Fig. 7 Illustrative enterprise’s port logistics operation process SPN

<!-- b000231 | caption | pages [16] -->
Table 10 Implications of the port logistics SPN place and transition

<!-- b000233 | prose | pages [16] -->
−1 1 0 0 0 0 0 0 0 0 0 0 0 −1 1 0 0 0 0 0 0 0 0 0 ⎛ ⎞ 0 0 −1 1 0 1 0 0 0 0 0 0 ⎜ ⎟ 0 0 0 −1 1 0 0 0 0 0 0 0 ⎜ ⎟ 0 0 0 0 0 −1 1 0 0 0 0 0 ⎜ ⎟ (12) 𝐴= 0 0 0 0 0 0 −1 1 0 0 0 0 ⎜ ⎟ 0 0 0 0 0 0 0 −1 1 0 0 0 ⎜ ⎟ ⎜ ⎟ 0 0 0 0 0 0 0 0 −1 1 0 0 0 0 0 0 0 0 0 0 0 −1 1 0 ⎝ 1⎠ 0 0 0 0 0 0 0 0 0 0 −1 Solve for 𝐴𝑋 = 0 to obtain a set of invariant bits.

<!-- b000234 | prose | pages [16] -->
(13) 𝑋ଵ= (1,1,1,1,0,1,0,0,0,0,1,1)் (14) 𝑋ଶ= (1,1,1,0,1,0,1,1,1,1,1,1)் The following conclusions can be drawn from the correlation matrix 𝐴 and the invariant 𝑋 (Chahrour et al., 2021).

<!-- b000235 | prose | pages [16] -->
(1) All depots in the constructed model have input conditions, i.e., adjacent input variants and alternate depots and variants, indicating a very smooth articulation process of the port op- eration process.

<!-- b000236 | furniture | pages [17] -->
Team # 2224178

<!-- b000237 | furniture | pages [17] -->
Page 17 of 24

<!-- b000238 | prose | pages [17] -->
(2) There are no processes in the constructed model that can never be performed. The model has neither isolated elements (places and transitions) nor connections between places or between transitions, which suggests that every process in the port operation can be executed.

<!-- b000239 | prose | pages [17] -->
The average delay and rate consumed by each transition in the SPN model of the illustra- tive enterprise is shown in Table 11.

<!-- b000240 | caption | pages [17] -->
Table 11 Illustrative enterprise SPN average transition delay and rate

<!-- b000241 | prose | pages [17] -->
Transition Delay Rate 𝜆 Transition Delay Rate 𝜆 𝑇ଵ 20 0.05 𝑇଻ 10 0.1 𝑇ଶ 15 0.00667 𝑇଼ 20 0.05 𝑇ଷ 30 0.0333 𝑇ଽ 10 0.1 𝑇ସ 10 0.1 𝑇ଵ଴ 3 0.333 𝑇ହ 5 0.2 𝑇ଵଵ 1 1 𝑇଺ 3 0.333 The equation for the probabilistic relationship between the states of the system is calcu- lated, as in Equation (15).

<!-- b000242 | prose | pages [17] -->
𝜆ଵ𝑥଴= 𝜆ଵଵ𝑥ଵଷ ⎧ 𝜆ଶ𝑥ଵ= 𝜆ଵ𝑥଴ ⎪ 𝜆ଷ𝑥ଶ= 𝜆ଶ𝑥ଶ ⎪ (𝜆ସ+ 𝜆ହ)𝑥ଷ= 𝜆ଷ𝑥ଶ ⎪ ⎪ (𝜆ସ+ 𝜆଺)𝑥ସ= 𝜆ହ𝑥ଷ ⎪ (𝜆ସ+ 𝜆଻)𝑥ହ= 𝜆଺𝑥ସ ⎪ 𝜆ସ𝑥଺= 𝜆଻𝑥ହ (15) 𝜆ହ𝑥଻= 𝜆ସ𝑥ଷ ⎨ 𝜆଺𝑥଼= 𝜆ସ𝑥ସ+ 𝜆ହ𝑥଻ ⎪ ⎪ 𝜆଻𝑥ଽ= 𝜆ସ𝑥ହ+ 𝜆଺𝑥 ⎪ 𝜆଼𝑥ଵ଴= 𝜆ସ𝑥଺+ 𝜆଻𝑥ଽ ⎪ 𝜆ଽ𝑥ଵଵ= 𝜆଼𝑥ଵ଴ ⎪ 𝜆ଵ଴𝑥ଵଶ= 𝜆ଽ𝑥ଵଶ ⎪ ⎩ 𝑥ଵ+ 𝑥ଶ+ 𝑥ଷ+ 𝑥ସ+ 𝑥ହ+ 𝑥଺+ 𝑥଻+ 𝑥଼+ 𝑥ଽ+ 𝑥ଵ଴+ 𝑥ଵଵ+ 𝑥ଵଶ+ 𝑥ଵଷ= 1 The table of probabilities for each state was obtained by programming in MATLAB as follows.

<!-- b000243 | caption | pages [17] -->
Table 12 Steady state probability values for each marker

<!-- b000244 | prose | pages [17] -->
Steady state markers Probability Steady state markers Probability 𝑃(𝑀଴) 0.1672 𝑃(𝑀଻) 0.0139 𝑃(𝑀ଵ) 0.1254 𝑃(𝑀଼) 0.0122 𝑃(𝑀ଶ) 0.2511 𝑃(𝑀ଽ) 0.0622 𝑃(𝑀ଷ) 0.0279 𝑃(𝑀ଵ଴) 0.1672 𝑃(𝑀ସ) 0.0129 𝑃(𝑀ଵଵ) 0.0836 𝑃(𝑀ହ) 0.0214 𝑃(𝑀ଵଶ) 0.0251 𝑃(𝑀଺) 0.0214 𝑃(𝑀ଵଷ) 0.0084 According to the reachable tree of the reachable SPN model of the process, the token distribution in each representation state can be obtained.

<!-- b000245 | caption | pages [17] -->
Table 13 Identification status and inclusion of place and place busy probability

<!-- b000246 | furniture | pages [18] -->
Team # 2224178

<!-- b000247 | furniture | pages [18] -->
Page 18 of 24

<!-- b000248 | prose | pages [18] -->
Maker Place Busy probability Maker Place Busy probability 𝑀଴ 𝑃ଵ -- 𝑀଻ 𝑃ହ/𝑃଺ 0.0251 𝑀ଵ 𝑃ଶ 0.1672 𝑀଼ 𝑃଺/𝑃଻ 0.0836 𝑀ଶ 𝑃ଷ 0.1254 𝑀ଽ 𝑃଺/𝑃଼ 0.1886 𝑀ଷ 𝑃ସ 0.2511 𝑀ଵ଴ 𝑃଺/𝑃ଽ 0.0836 𝑀ସ 𝑃ସ/𝑃଻ 0.0836 𝑀ଵଵ 𝑃ଵ଴ 0.02511 𝑀ହ 𝑃ସ/𝑃ହ/𝑃଼ 0.0418 𝑀ଵଶ 𝑃ଵଵ 0.0084 𝑀଺ 𝑃ସ/𝑃ଽ 0.255 𝑀ଵଷ 𝑃ଵଶ -- The paper then calculated the system average token number of places, the average marker flow rate into the system and the average system delay time in the illustrative enterprise.

<!-- b000249 | prose | pages [18] -->
𝑁ഥ= 𝜇ଶ (16) തതതത= 𝑃[𝑀(𝑃ଶ) = 1] + ⋯+ 𝑃[𝑀(𝑃ଵ଴) = 1] = 1.1718 തതത+ ⋯+ 𝜇ଵ଴ 𝜆= 𝑅(𝑇ଵ, 𝑃ଶ) = 𝑈(𝑇ଵ) × 𝜆ଵ= 8.36 × 10ିଷ (17) (18) 𝑁= 𝑁ഥ 𝜆= 140.167 According to the calculation results, the average delay of the SPN of the example enter- prise port logistics D&A system reaches 140.167 minutes. In the next section, we will optimize the example enterprise SPN to reduce the delay time of transport vehicles in ports.

<!-- b000250 | heading | pages [18] -->
5.3 Port Logistics Optimization for the Illustrative Enterprise

<!-- b000251 | prose | pages [18] -->
Based on the developed standard D&A system meta-network model, an optimized SPN model was developed. The main changes compared to the unoptimized illustrative enterprise model are:

<!-- b000252 | prose | pages [18] -->
(1) The provision of vessel information to the customs department immediately upon ar- rival of the vessel is shown as T2 ahead of schedule, in parallel with T3.

<!-- b000253 | prose | pages [18] -->
(2) Container unloading is carried out in parallel with ticket checking and is represented in the model as T4 and T5 in parallel.

<!-- b000254 | prose | pages [18] -->
(3) The previous manual checking of box numbers has been replaced by an automatic check using the RFID container tagging system.

<!-- b000255 | prose | pages [18] -->
P2 T2 P4

<!-- b000256 | prose | pages [18] -->
P1 T1 P5 T4

<!-- b000257 | prose | pages [18] -->
P3 T3 P7 T6 P8 T7 P9 T8

<!-- b000258 | prose | pages [18] -->
P6 T5

<!-- b000259 | prose | pages [18] -->
T9 P10

<!-- b000260 | caption | pages [18] -->
Fig. 8 Optimized illustrative enterprise SPN model

<!-- b000261 | caption | pages [18] -->
Table 14 Optimized implications of the port logistics SPN place and transition

<!-- b000262 | prose | pages [18, 19] -->
Place Meaning Transi- Meaning tion P1 Shipper (A8) T1 Ship arriving in port (P1) P2 Vessel information (I7) T2 Vessel waiting for berth allocation (P2) P3 Regulatory release information (I1) T3 Vessel approaching port (P3) P4 Loading and unloading machinery infor- T4 Container liner (P4) mation (I3) P5 Stockyard information (I4) T5 Loading and unloading operations (P6) P6 Longshoreman (A4) T6 Stockpile storage (P7) P7 Intra-port information (I5) T7 Intra-port consolidation vehicle transport (P9) P8 Longshoreman (A4) T8 Customs supervision (P10) P9 Customs inspector (A1) T9 Vessels leaving port (P11) P10 Consignee The system average delay and rate of each transition in the SPN model after structural optimization based on the meta-network is shown in Table 15. Due to the strengthened man- agement and organization of the operation, the working time of the container unloading oper- ation has been shortened, so the delay of the corresponding transition T4 has been reduced from 30-time units to 20-time units.

<!-- b000263 | furniture | pages [19] -->
Team # 2224178

<!-- b000264 | furniture | pages [19] -->
Page 19 of 24

<!-- b000266 | caption | pages [19] -->
Table 15 Optimized illustrative enterprise SPN average transition delay and rate

<!-- b000267 | prose | pages [19] -->
Transition Delay Rate 𝜆 Transition Delay Rate 𝜆 𝑇ଵ 20 0.05 𝑇଺ 10 0.1 𝑇ଶ 10 0.1 𝑇଻ 20 0.05 𝑇ଷ 15 0.0667 𝑇଼ 10 0.1 𝑇ସ 20 0.05 𝑇ଽ 1 1 𝑇ହ 5 0.2 The same as the calculation process before optimizing the example enterprise SPN, the system average token number of the place, the average mark flow rate flowing into the system and the system average delay time were calculated.

<!-- b000268 | prose | pages [19] -->
𝑁ഥ= 𝜇ଶ (19) തതതത= 𝑃[𝑀(𝑃ଶ) = 1] + ⋯+ 𝑃[𝑀(𝑃ଵ଴) = 1] = 1.5829 തതത+ ⋯+ 𝜇ଵ଴ 𝜆= 𝑅(𝑇ଵ, 𝑃ଶ) = 𝑈(𝑇ଵ) × 𝜆ଵ= 1.841 × 10ିଶ (20) (21) 𝑁= 𝑁ഥ 𝜆= 85.980 After we optimized the SPN model of the illustrative enterprise based on the standard e port logistics D&A system meta-network model, the average system delay was reduced by 38.7%, 54.187 minutes.

<!-- b000269 | prose | pages [19] -->
Before optimization Illustrative enterprise system performance After optimization 160 Illustrative enterprise system delay (min) 140.167 140 After 120 optimization 38% 100 85.98 80 Before 60 optimization 62% 40

<!-- b000270 | prose | pages [19] -->
20 Before optimization After optimization 0

<!-- b000271 | furniture | pages [20] -->
Team # 2224178

<!-- b000272 | furniture | pages [20] -->
Page 20 of 24

<!-- b000273 | caption | pages [20] -->
Fig. 9 Illustrative enterprise system performance comparison before and after optimization

<!-- b000274 | heading | pages [20] -->
6 Sensitivity Analysis

<!-- b000275 | heading | pages [20] -->
6.1 Sensitivity Analysis of the Standard Port Logistics D&A System Ma-

<!-- b000276 | prose | pages [20] -->
turity

<!-- b000277 | prose | pages [20] -->
This paper introduces Monte Carlo stochastic simulations to validate the developed MNA- PCA based maturity assessment model for standard port logistics D&A systems. The Monte Carlo simulation contains a total of four scenarios, which are the random removal of one node, two nodes, three nodes and four nodes from the standard DA system meta-network. Fifty sim- ulations were performed for each scenario, and the average of 12 D&A system maturity indi- cators was recorded. The average value of the indicators for each scenario was compared to the indicators for the standard meta-network, and a sensitivity analysis was performed, as shown in Fig. 10. As shown in Fig. 10, the overall change in the indicator for the scenario where four nodes are removed is significant, while the indicator remains relatively flat when one node is removed. Notably, the changes in the sensitivity of the indicators at the four deleted nodes are consistent with the changes in the indicators of the illustrative enterprise selected in this paper, demonstrating the stability and feasibility of the model developed in this paper.

<!-- b000278 | caption | pages [20] -->
Fig. 10 Sensitivity analysis of indicators in different scenarios

<!-- b000279 | heading | pages [20] -->
6.2 Sensitivity Analysis of the Illustrative Enterprise Port Logistics SPN

<!-- b000280 | prose | pages [20] -->
This paper selected the most likely busy states 𝑀ଷ and 𝑀ଽ in Table 13 for sensitivity simulations (Elusakin and Shafiee, 2020). We changed the 𝜆ଷ and 𝜆ଽ corresponding to the two states continuously in units of 0.01 from 0.01 to 1, thus calculating the change in the prob- ability of stranding of the transport equipment, as shown in Fig. 11. We can fit this surface to quantitatively calculate the detention probability of transportation equipment and provide a basis for the decision-making of port enterprises.

<!-- b000281 | furniture | pages [21] -->
Team # 2224178

<!-- b000282 | furniture | pages [21] -->
Page 21 of 24

<!-- b000283 | prose | pages [21] -->
P

<!-- b000284 | prose | pages [21] -->
λ3 λ9

<!-- b000285 | caption | pages [21] -->
Fig. 11 Change surface of transportation equipment detention probability

<!-- b000286 | heading | pages [21] -->
7 Application Recommendations for ICM Corporation’s D&A

<!-- b000287 | heading | pages [21] -->
System and Model Extensions

<!-- b000288 | heading | pages [21] -->
7.1 D&A System Application Recommendations

<!-- b000289 | prose | pages [21] -->
According to the maturity assessment results and the SPN port optimization results of the illustrative enterprise, we can see that the D&A system meta-network model established in this paper has good results.

<!-- b000290 | prose | pages [21] -->
The D&A system maturity assessment model based on MNA-PCA is easy to operate. Ac- cording to the standard D&A system meta-network model, it is only necessary for an ICM company to delete the nodes or links that the company cannot realize. Then, the model will present the ICM company's port logistics system, calculate the ICM company's D&A system maturity score, and detect the problems existing in the system. The SPN model for port logistics is highly accurate and integrative and can simulate the average delay of ICM ports to the great- est extent possible.

<!-- b000291 | prose | pages [21] -->
The D&A system maturity indicators screened by the meta-network analysis method in this paper effectively address the relevant requirements of the ICM departments for D&A sys- tems. In addition, the indicators selected relate to the interaction process between people, tech- nology, processes and data information, which can better inform do not decisions for the ICM management team.

<!-- b000292 | heading | pages [21] -->
7.2 Model’s Industry Extensions

<!-- b000293 | prose | pages [21] -->
The key to the cross-industry extension of the model developed in this paper is to analyze the differences in logistics operations across industries. The people, technology, process and data information involved in logistics processes are different in different industries. The cross- industry extension of the model first requires the construction of meta-network models of lo- gistics D&A systems in different industries. The steps for specific model expansion are shown below in Fig. 12.

<!-- b000294 | furniture | pages [22] -->
Team # 2224178

<!-- b000295 | furniture | pages [22] -->
Page 22 of 24

<!-- b000296 | heading | pages [22] -->
(1) Original data collection

<!-- b000297 | prose | pages [22] -->
(2) Structured Dataset Development

<!-- b000298 | prose | pages [22] -->
(4) Visualized Meta-network Generation (3)  Meta-network Matrix Development

<!-- b000299 | prose | pages [22] -->
A11 A01 A15 … … … FT17 PT06 PT05 A11 A01

<!-- b000300 | prose | pages [22] -->
K01 … Meta-network in disaster prevention stage … … Meta-network in function recovery stage A07 A12 Agent Knowledge A15 K21 RT09 … Resource … … R05 Task A01 Meta-network in disaster resistance stage

<!-- b000301 | caption | pages [22] -->
Fig. 12 Model expansion flow chart

<!-- b000302 | prose | pages [22] -->
Step 1: Gather critical information on the logistics processes of the target industry. Sources of information can be government documents, agency reports or academic publications, etc.

<!-- b000303 | prose | pages [22] -->
Step 2: Determine the nodes and links of the meta-network according to the enterprise's objectives of building the D&A system. The D&A system meta-network model nodes can be people, knowledge, resources, and processes.

<!-- b000304 | prose | pages [22] -->
Step 3: Identify the sub-networks and determine the correlation between sub-network nodes.

<!-- b000305 | prose | pages [22] -->
Step 4: Input critical nodes and correlations into the D&A system meta-network model to visualize the meta-network.

<!-- b000306 | prose | pages [22] -->
Step 5: Finally, a meta-network-based enterprise D&A system maturity assessment and enterprise logistics SPN model simulation is carried out.

<!-- b000307 | prose | pages [22] -->
The model developed in this paper is highly integrative, allowing additions, deletions and simulations to be made to the model at any time, and will reach a wide range of applications in different industries.

<!-- b000308 | heading | pages [22] -->
8 Model Evaluation

<!-- b000309 | heading | pages [22] -->
8.1 Strengths

<!-- b000310 | prose | pages [22, 23] -->
1. This paper innovatively combines a meta-network model with a port logistics D&A system. The meta-network model effectively combines people, skills, processes and data infor- mation in port logistics operations. Solves the difficulties of port logistics companies with mul- tiple associations and subjects when it comes to data governance.

<!-- b000311 | furniture | pages [23] -->
Team # 2224178

<!-- b000312 | furniture | pages [23] -->
Page 23 of 24

<!-- b000314 | prose | pages [23] -->
2. The D&A system maturity assessment system was established through the association of meta-network analysis and principal component analysis. The DA maturity assessment in- dicators, which are systematic and comprehensive, enable the indicators to be given practical meaning from a multi-component perspective.

<!-- b000315 | prose | pages [23] -->
3. An innovative proposal to build stochastic Petri nets isomorphic to meta-networks. This process greatly simplifies the complex process of traditional Petri net modelling. The devel- oped SPN model can quantitatively assess the average delay of a company's port logistics sys- tem.

<!-- b000316 | prose | pages [23] -->
4. The meta-network model applied in this paper is highly extensible and provides new ideas and perspectives for port logistics data information governance.

<!-- b000317 | heading | pages [23] -->
8.2 Weaknesses

<!-- b000318 | prose | pages [23] -->
1. Only one representative enterprise has been selected to demonstrate the model proposed in this paper. Future research could add example systems.

<!-- b000319 | prose | pages [23] -->
2. The meta-network model of the port logistics D&A system established in this paper is based on the literature and relevant policy documents only and can be subject to expert consul- tation in the event of sufficient time.

<!-- b000320 | heading | pages [23] -->
References:

<!-- b000321 | references | pages [23] -->
Almotairi, B. & Lumsden, K. (2009), "Port logistics platform integration in supply chain management", Interna-

<!-- b000322 | references | pages [23] -->
tional Journal of Shipping and Transport Logistics, Vol. 1 No. 2, pp. 194-210.

<!-- b000323 | references | pages [23] -->
Carley, K. M., Diesner, J., Reminga, J. & Tsvetovat, M. (2007), "Toward an interoperable dynamic network anal-

<!-- b000324 | references | pages [23] -->
ysis toolkit", Decision Support Systems, Vol. 43 No. 4, pp. 1324-1347.

<!-- b000325 | references | pages [23] -->
Chahrour, N., Nasr, M., Tacnet, J. & Bérenguer, C. (2021), "Deterioration modeling and maintenance assessment

<!-- b000326 | references | pages [23] -->
using physics-informed stochastic Petri nets: Application to torrent protection structures", Reliability Engi-

<!-- b000327 | references | pages [23] -->
neering & System Safety, Vol. 210107524.

<!-- b000328 | references | pages [23] -->
Elusakin, T. & Shafiee, M. (2020), "Reliability analysis of subsea blowout preventers with condition-based

<!-- b000329 | references | pages [23] -->
maintenance using stochastic Petri nets", Journal of Loss Prevention in the Process Industries, Vol.

<!-- b000330 | references | pages [23] -->
63104026.

<!-- b000331 | references | pages [23] -->
Lee, J. & Mitici, M. (2020), "An integrated assessment of safety and efficiency of aircraft maintenance strategies

<!-- b000332 | references | pages [23] -->
using agent-based modelling and stochastic Petri nets", Reliability Engineering & System Safety, Vol.

<!-- b000333 | references | pages [23] -->
202107052.

<!-- b000334 | references | pages [23] -->
Pestov, I. (2009), "Dynamic network analysis for understanding complex systems and processes", Defence Re-

<!-- b000335 | references | pages [23] -->
search and Development Canada,.

<!-- b000336 | references | pages [23] -->
S., B., A., S. & L., K. (2015), "Main factors to select a cruise homeport in the Mediterranean region: A perspective

<!-- b000337 | references | pages [23] -->
from the cruise industry agents", in 2015 International Conference on Logistics, Informatics and Service

<!-- b000338 | references | pages [23] -->
Sciences (LISS), pp. 1-5.

<!-- b000339 | references | pages [23] -->
Wold, S., Esbensen, K. & Geladi, P. (1987), "Principal component analysis", Chemometrics and Intelligent La-

<!-- b000340 | references | pages [23] -->
boratory Systems, Vol. 2 No. 1, pp. 37-52.

<!-- b000341 | heading | pages [24] -->
ICM Corporation

<!-- b000342 | prose | pages [24] -->
--The Value Creation of Port Logistics Big Data Dear Port Users： I would like to thank you for your trust in choosing ICM Corporation as your partner. ICM Corporation insists on being customer-oriented and adheres to the concept of “people-oriented and win-win cooperation”. Bringing tremendous success to our customers is a constant moti- vation for us at ICM Corporation. ICM Corporation has implemented the new logistics core strategy of “Supply Chain + Big Data + AIOT” and created a data and analytics (D&A) system with independent intellectual property rights. ICM Corporation conducted a four-day D&A system maturity assessment and optimization exercise on 2022.2.18.

<!-- b000343 | prose | pages [24] -->
 Overview of Targets

<!-- b000344 | prose | pages [24] -->
 Maximizing the value of ICM Corporation’s data assets.

<!-- b000345 | prose | pages [24] -->
 Measuring the maturity capability of ICM Corporation’s D&A system through people, technologies and processes.

<!-- b000346 | prose | pages [24] -->
 Optimizing the D&A system architecture to improve system analysis.

<!-- b000347 | heading | pages [24] -->
 Solutions

<!-- b000348 | prose | pages [24] -->
The consulting team develops a standard D&A system meta-network model based on the port logistics industry’s most advanced D&A system architecture. The model effectively real- izes the visual integration of people, relevant technologies, mature processes and data infor- mation. Through meta-network analysis, 12 practically meaningful indicators were selected to construct the D&A system maturity assessment system. Feeding the current status of ICM’s D&A system into a standard D&A system meta-network enables the assessment of the maturity of ICM’s D&A system.

<!-- b000349 | prose | pages [24] -->
Based on ICM’s D&A system, the consultancy team constructed a stochastic Petri network model (SPN) for port logistics. The SPN model enables the simulation of logistic transport detention times based on ICM’s D&A system data. Finally, ICM’s D&A system optimization is implemented based on the standard D&A system meta-network model.

<!-- b000350 | heading | pages [24] -->
 Results Analysis

<!-- b000351 | prose | pages [24] -->
 ICM's D&A system maturity assessment level is Excellent.

<!-- b000352 | prose | pages [24] -->
 The average dwell time of port transport equipment decreased by 38.7%.

<!-- b000353 | prose | pages [24] -->
ICM’s D&A systems consultancy project has shown that the modelling tools provided by the consultancy are a powerful tool for assessing and planning logistics business processes. ICM Corporation will continue to work with this consultancy to continuously improve the data asset application capabilities of the D&A system. ICM Corporation will strive to develop into a preeminent port logistics service provider, offering our customers complete logistics solutions and logistics services. We hope you will keep your faith in ICM’s D&A system and ICM Cor- poration!

<!-- b000354 | prose | pages [24] -->
Yours sincerely, ICM Corporation
