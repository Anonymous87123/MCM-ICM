# P-D-2022-2215444-cd948920

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Problem Chosen 2022

<!-- b000002 | furniture | pages [1] -->
Team Control Number

<!-- b000003 | prose | pages [1] -->
MCM/ICM

<!-- b000004 | title | pages [1] -->
D

<!-- b000005 | title | pages [1] -->
2215444

<!-- b000006 | heading | pages [1] -->
Summary Sheet

<!-- b000007 | title | pages [1] -->
How Can We Realize the Full Potential of Our Data?

<!-- b000008 | heading | pages [1] -->
Summary

<!-- b000009 | prose | pages [1] -->
With the development of technology and the explosive growth of data, data is becoming an important strategic asset in today's society, and it is more and more important to establish a suitable system to manage and analyze the data. In this paper, we build a model to analyze the factors affecting the maturity of data analysis systems, revealing how to make better use of data, and for- mulate plans to maximize the potential of data assets.

<!-- b000010 | prose | pages [1] -->
In Task1: First, based on the grounded theory, we comprehensively consider the ICM company requirements as well as the factors of the maturity model literature given in the title, screening out the indicators that affect data analysis to establish a data analysis system capability maturity eval- uation model (DAMM). Then we use the Analytic Hierarchy Process combined with the Entropy Weight Method (AHP-EWM) to perform a combined weighting analysis on the weight values of the relevant indicators. Finally, we introduce the concept of membership function, dividing the system maturity into five levels, and calculating the system maturity index score of 0.8173 points (the highest score is 1), which is in the relatively mature fourth level ( the highest is the fifth level).

<!-- b000011 | prose | pages [1] -->
In Task2: First, we use a linear programming model to quantitatively analyze, and in the case of  limited optimization costs, we transform the problem into maximizing the system maturity index. Then, we use system dynamics to simulate and obtain the index values corresponding to different maturity levels for qualitative analysis, verifying the validity of the model by comparing the difference between the simulation results and the evaluation model of task 1. Finally, we com- bine the two methods, and based on the differences between the fourth and fifth levels of maturity, we give suggestions that ICM companies need to invest in teamwork and technical management.

<!-- b000012 | prose | pages [1] -->
In Task3: In order to formulate an agreement to measure the effectiveness of the system, we divide different index levels from the perspectives of people, technology and process, using the Apriori to analyze the rule association between the three groups of indicators, combined with system dynamics simulation in the way of simulation, we give the relevant agreement of the ICM data analysis system in the connection mechanism between people, technology, process and the three together.

<!-- b000013 | prose | pages [1] -->
In Task4: First, we evaluate the model based on the differences in data analysis systems of seaport companies with different scales, and conduct multiple sets of simulations based on the model proposed in task 2 simulation. Then, we compare the errors between the simulated maturity index and the results obtained by the DAMM model, which are all smaller than 5%, showing the good applicability of the model to seaport companies of different sizes. Finally, combined with the International Standard Plan of "Quality Management System Requirements" (ISO9001), we ana- lyze the reasons for the universality of DAMM, and give three benefits for customers to adopt DAMM for ICM.

<!-- b000014 | keywords | pages [1] -->
Keywords: data analysis; maturity evaluation model; AHP-EWM; system dynamics; Apriori

<!-- b000015 | heading | pages [2] -->
Contents

<!-- b000016 | contents | pages [2] -->
1 Introduction ...................................................................................................... 3

<!-- b000017 | contents | pages [2] -->
1.1 Problem Background ....................................................................................................... 3

<!-- b000018 | contents | pages [2] -->
1.2 Restatement of the Problem ............................................................................................. 3

<!-- b000019 | contents | pages [2] -->
1.3 Literature Review ............................................................................................................. 3

<!-- b000020 | contents | pages [2] -->
1.4 Our Work .......................................................................................................................... 4

<!-- b000021 | contents | pages [2] -->
2 Assumptions and Justifications ....................................................................... 4

<!-- b000022 | contents | pages [2] -->
3 Notations ........................................................................................................... 5

<!-- b000023 | contents | pages [2] -->
4 TASK 1: DAMM Based on AHP-EWM ......................................................... 6

<!-- b000024 | contents | pages [2] -->
4.1 Indicator selection ............................................................................................................ 6

<!-- b000025 | contents | pages [2] -->
4.2 Weight determination ....................................................................................................... 9

<!-- b000026 | contents | pages [2] -->
4.2.1 EWM ...................................................................................................................... 9

<!-- b000027 | contents | pages [2] -->
4.2.2 AHP ...................................................................................................................... 10

<!-- b000028 | contents | pages [2] -->
4.2.3 Combination weight ............................................................................................. 10

<!-- b000029 | contents | pages [2] -->
4.3 The Solution of Task 1 ................................................................................................... 11

<!-- b000030 | contents | pages [2] -->
5 TASK 2: Linear programming and System Dynamics ............................... 12

<!-- b000031 | contents | pages [2] -->
5.1 Model Overview ............................................................................................................ 12

<!-- b000032 | contents | pages [2] -->
5.2 Establishment of Model ................................................................................................. 12

<!-- b000033 | contents | pages [2] -->
5.2.1 Linear programming ............................................................................................. 12

<!-- b000034 | contents | pages [2] -->
5.2.2 System Dynamics ................................................................................................. 13

<!-- b000035 | contents | pages [2] -->
5.3 The Solution of Task 2 ................................................................................................... 14

<!-- b000036 | contents | pages [2] -->
6 TASK 3:System Effectiveness Measure Model Based on Apriori ............. 15

<!-- b000037 | contents | pages [2] -->
6.1 Model Overview ............................................................................................................ 15

<!-- b000038 | contents | pages [2] -->
6.2 Data Processing .............................................................................................................. 15

<!-- b000039 | contents | pages [2] -->
6.3 Establishment of Apriori ................................................................................................ 16

<!-- b000040 | contents | pages [2] -->
6.4 Analysis of The Result ................................................................................................... 17

<!-- b000041 | contents | pages [2] -->
7 TASK 4: Sensitivity Analysis and Model promotion .................................. 18

<!-- b000042 | contents | pages [2] -->
7.1 Sensitivity Analysis ........................................................................................................ 18

<!-- b000043 | contents | pages [2] -->
7.2 Model promotion ........................................................................................................... 19

<!-- b000044 | contents | pages [2] -->
8 Model Evaluation and Further Discussion .................................................. 20

<!-- b000045 | contents | pages [2] -->
8.1 Strengths ........................................................................................................................ 20

<!-- b000046 | contents | pages [2] -->
8.2 Weaknesses .................................................................................................................... 20

<!-- b000047 | contents | pages [2] -->
References .......................................................................................................... 21

<!-- b000048 | heading | pages [3] -->
1 Introduction

<!-- b000049 | heading | pages [3] -->
1.1 Problem Background

<!-- b000050 | prose | pages [3] -->
With the completion of the information revolution in the 1950s, the main body represent- ing advanced productivity has been banned by informatization. Nowadays, data and infor- mation have become strategic materials for enterprises and companies to compete. Only by properly managing and making full use of information can cold data be transformed into visible wealth. Therefore, mature data analysis capabilities have become the top priority to enhance the competitive advantage of enterprises. The complete cognition of the data analysis system can undoubtedly clarify the direction of enterprise optimization and development. As a conse- quence, a reasonable assessment of its own data analysis capabilities has become the key for enterprises to improve themselves and enhance user loyalty.

<!-- b000051 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000052 | prose | pages [3] -->
Considering the background information and restricted conditions identified in the prob- lem statement, we need to solve the following problems:

<!-- b000053 | prose | pages [3] -->
 Provide indicators to measure the maturity of Intercontinental Cargo (ICM) D&A systems (including talent, technology and process).

<!-- b000054 | prose | pages [3] -->
 Establish a model for Intercontinental Cargo Company (ICM) to evaluate the maturity of its own D&A system, and provide the modification method that ICM needs to make to the system to fully realize the potential of data.

<!-- b000055 | prose | pages [3] -->
 Give the protocol that ICM needs to make to measure the effectiveness of the D&A system.

<!-- b000056 | prose | pages [3] -->
 Apply the model to ports of other sizes and different industries, analyze the adapta- bility of the model, point out the superiority of the model indicators, and analyze the possible benefits to ICM companies if ICM customers use the evaluation model.

<!-- b000057 | prose | pages [3] -->
 Write a letter to ICM Collaborative users describing our approach and increasing con- fidence in ICM Collaborative D&A systems.

<!-- b000058 | heading | pages [3] -->
1.3 Literature Review

<!-- b000059 | prose | pages [3] -->
In 1979, Nolan proposed the growth stage model to study the development of enterprise information data system, and it became the prototype of the maturity model. In 1986, Carnegie Mellon University in the United States developed the Capability Maturity Model (CMM) [1] based on the Nolan model. Its main contents are divided into the qualitative analysis of capa- bility maturity and the evaluation index system of capability maturity model. After the capa- bility maturity model is established, many scholars begin to improve the maturity model and apply it in different fields according to the characteristics of different fields. For example, hu- man resources maturity model, customer information quality management maturity model, en- terprise information maturity model.

<!-- b000060 | prose | pages [3, 4] -->
In the research of various scholars, Pekka Berg [2] constructed the R&D quality maturity model, by constructing the dimensions of the quality maturity model, the maturity level and the characteristics of each maturity, and establishing a detailed evaluation method to study the R&D quality of enterprises. process, and test the effect of this model in R&D quality improve- ment through case analysis. Kirazli and Moetz[3] introduced the factors of risk management into the maturity model, formulated a four-level model of enterprises' digital process, and paid attention to the potential risks brought by the implementation of digital technology by enter- prises, but the impact of digital technology on enterprises The advantages are lacking in elab- oration. Dr. J.Kent Crawford [4] proposed the PMS project management maturity. The model establishes a clear project management system and determines the maturity level of project management. By analyzing the status quo of project management, and then on the basis of the model evaluation results, put forward the corresponding improvement measures.

<!-- b000062 | prose | pages [4] -->
Through the analysis and summary of many literatures, it can be seen that many scholars pay extensive attention to the digital management of enterprises, and have done a lot of research on it. In terms of enterprise digitalization, scholars believe that many enterprises are limited by their own resources and capabilities, and need to rely on third-party digital platforms to achieve digital management. Generally speaking, there is still a lack of research on digital maturity models.

<!-- b000063 | heading | pages [4] -->
1.4 Our Work

<!-- b000064 | prose | pages [4] -->
Our work in this problem is mainly shown in the figure 1:

<!-- b000065 | caption | pages [4] -->
Figure 1 Our Work

<!-- b000066 | heading | pages [4] -->
2 Assumptions and Justifications

<!-- b000067 | prose | pages [4, 5] -->
We made the following assumptions to help us build the model. These constructions are the background and basis for our subsequent analysis.

<!-- b000069 | prose | pages [5] -->
 Assumption 1：It is assumed that ICM's data analysis system is comprehensive in terms of people, technology, and processes.

<!-- b000070 | prose | pages [5] -->
Justification: Although the general description given in the title is not necessarily all the indicators concerned by ICM's data analysis system, in order to make the indicator analysis clear and controllable, we assume that other indicators that affect data anal- ysis found later are not considered by the system and belong to the part of maturity that needs to be improved.

<!-- b000071 | prose | pages [5] -->
 Assumption 2：It is assumed that the literature we have checked is relatively com- prehensive and scientific.

<!-- b000072 | prose | pages [5] -->
Justification: In order to make the DAMM model scientific and reasonable, it is as- sumed that the literature we have checked is comprehensive and scientific, which means that our analysis is consistent with objective cognition and facts.

<!-- b000073 | prose | pages [5] -->
 Assumption 3：It is assumed that ICM clients are limited to collective companies, ignoring a small number of self-employed individuals.

<!-- b000074 | prose | pages [5] -->
Justification: In real work, intercontinental freight companies may also trade with a small number of self-employed individuals, but the vast majority of customers are of little value and significance because of individual people, technology and processes.

<!-- b000075 | prose | pages [5] -->
 Assumption 4：Assume that the estimated costs that ICM can use to improve the data analysis system are known.

<!-- b000076 | prose | pages [5] -->
Justification: This is done to analyze how to use the data assets to their fullest po- tential.

<!-- b000077 | heading | pages [5] -->
3 Notations

<!-- b000078 | prose | pages [5] -->
The key mathematical notations used in this paper are listed in Table 1.

<!-- b000079 | caption | pages [5] -->
Table 1: Notations used in this paper

<!-- b000080 | heading | pages [5] -->
Symbol

<!-- b000081 | prose | pages [5] -->
Description 𝑆𝑆 Factors considered score 𝛼𝛼 Initial score for the factor of interest Comprehensive weight 𝑄𝑄𝑖𝑖 𝑈𝑈𝑖𝑖 Sbjective weight 𝐻𝐻𝑖𝑖 Objective weight People's Scores for Different Indicators 𝑃𝑃𝑖𝑖 𝑇𝑇𝑗𝑗 Scores for different indicators of technology 𝑅𝑅𝑞𝑞 Scores for different metrics of the process

<!-- b000082 | heading | pages [6] -->
4 TASK 1: DAMM Based on AHP-EWM

<!-- b000083 | heading | pages [6] -->
4.1 Indicator selection

<!-- b000084 | prose | pages [6] -->
There are many factors that describe the maturity of an enterprise data analysis system, but the systematic index system is definitely not the bigger the better. Based on the analysis method of grounded theory, we can summarize the experience from the original data, and then rise to the system level to help us better build an evaluation system. Therefore, we are in the numerous literature on maturity models (some maturity models are shown in the table 2 below) Extract available indicators, and follow the principles of generalization, completeness and little overlap, and select more representative indicators as the main dimension of enterprise data analysis system maturity measurement。

<!-- b000085 | caption | pages [6] -->
Table 2 Partial maturity model

<!-- b000086 | prose | pages [6] -->
Researchers Indicators Background Tobias Met- IT capability,Teamwork Study on influencing factors of digital tlera[6] Talent management maturity of Swiss hospitals

<!-- b000087 | prose | pages [6] -->
Hongfei Tao [7] Process coverage Process internal management, supply chain process, process record

<!-- b000088 | prose | pages [6] -->
Yongyi Lin [8] Process visualization Process tracking, process diagnosis, process standardization

<!-- b000089 | prose | pages [6] -->
Gang Xie [9] Process Reengineering Process customization, process continuous improvement

<!-- b000090 | prose | pages [6] -->
De Carolis [10] Position Integrated and interoperable, digitally oriented

<!-- b000091 | prose | pages [6] -->
According to the above literature, We develop the data analysis system maturity model (DAMM) based on CMM, which comprehensively reflects the maturity level of the enterprise D&A system and provides strategic guidance for enterprise system diagnosis, transformation and upgrading.

<!-- b000092 | prose | pages [6, 7] -->
By constructing the Data Analysis System Maturity Model (DAMM), we analyze the key performance impacted by the maturity of the enterprise data analysis system from the perspec- tives of people, technology and process, and evaluate the system network from three perspec- tives formed from the grounded theory. The relationship diagram is as shown in figure 2： Analyzing the figure 2, the data analysis system maturity evaluation model we constructed comprehensively answered the confusion of ICM company recruitment managers about people factors. For example, from the perspective of the company's use of people, we consider the people expenditure cost index, which better summarizes ICM's problems in training talents, hiring or contracting; By using educational qualification evaluation indicators, the model can better solve the problem of recruiting talent location, hiring goals, and so on. In addition, based on the grounded theory, in the empirical summary of the references, our model also gives two important indicators of teamwork and talent management that a more complete maturity model should focus on in terms of people.

<!-- b000093 | caption | pages [7] -->
Figure 2 People-Related Metrics

<!-- b000095 | caption | pages [7] -->
Figure 3 Technology-Related Metrics

<!-- b000096 | prose | pages [7] -->
From the figure 3, we can know that DAMM has also completed the evaluation of tech- nology-related key performance at the technical level, and is similar to the analysis at employee level, adding two important indicators such as technological innovation and technological sta- bility, the specific analysis process will not be repeated here.

<!-- b000097 | caption | pages [8] -->
Figure 4 Process-Related Metrics

<!-- b000098 | prose | pages [8] -->
Comprehensive analysis of figures 2 to 4 shows that the evaluation system (DAMM) we constructed has well answered ICM's questions about the relationship between people, tech- nology and process. In addition, based on many literatures on enterprise maturity models, we have added relatively complete measures in all three aspects. Therefore, a more comprehensive and scientific data analysis system maturity evaluation model (DAMM) is constructed.

<!-- b000099 | prose | pages [8] -->
Specifically for ICM, we constructed a hierarchy of ICM's current data analysis maturity evaluation indicators based on ICM's description and analysis of people and technical processes, as shown in the figure 5 below.

<!-- b000100 | caption | pages [8] -->
Figure 5 Maturity evaluation index system

<!-- b000101 | prose | pages [8, 9] -->
Comparing Figures 2 to 5, ICM is lacking in all three levels, so the maturity of the data analysis system is not ideal. According to the specific situation of ICM, combined with a com- plete data analysis system model (DAMM), defining the factors that affect people 𝑃𝑃𝑖𝑖(1 ≤𝑖𝑖≤6): Number of people, Education background, IT capability, Cost, Team work and talent management followed by 𝑃𝑃1~𝑃𝑃6; Defining factors affecting technology 𝑇𝑇𝑗𝑗(1 ≤𝑗𝑗≤6): collection efficiency, response speed, storage capacity, positioning capacity, technological in- novation, and technical stability followed by 𝑇𝑇1~𝑇𝑇6; Define the factors that affect the process 𝑅𝑅𝑞𝑞(1 ≤𝑞𝑞≤5): process coverage, process visualization, process reengineering, process com- plexity, and process stability followed by 𝑅𝑅1~𝑅𝑅5 .

<!-- b000103 | prose | pages [9] -->
We define a maximum score 𝑆𝑆𝑖𝑖 of all metrics is 1, and a score of 0.3 for metrics 𝑀𝑀𝑖𝑖 that affect the maturity of data analytics systems but are not considered by ICM.

<!-- b000104 | prose | pages [9] -->
Since the existing data analysis system is included in the system analysis level, the initial score of the factor that has been concerned can be set to 𝛼𝛼1, and the calculation formula of the factor score considered by ICM is defined as follows:

<!-- b000105 | prose | pages [9] -->
(1) 𝛽𝛽𝑖𝑖 indicates the concerns of the ICM involved in the 𝑖𝑖 indicator, the scores of different indicators can be obtained by calculating separately.

<!-- b000106 | prose | pages [9] -->
Later, we calculate the weight value according to the Analytic Hierarchy Process and the Entropy Weight Method (AHP-EWM).

<!-- b000107 | heading | pages [9] -->
4.2  Weight determination

<!-- b000108 | prose | pages [9] -->
For the construction of data analysis system evaluation model (DAMM), the determina- tion of evaluation index weights plays a crucial role, which directly affects the accuracy of model evaluation. The entropy weight method (EWM) is an objective weighting method, and AHP is a subjective weighting method; we use the combination of the EWM and the AHP to determine the weight of the indicators. This is a comprehensive evaluation method that com- bines subjective and objective and integrates various methods, which can effectively improve the rationality and correctness of evaluation.

<!-- b000109 | heading | pages [9] -->
4.2.1 EWM

<!-- b000110 | prose | pages [9] -->
First, we calculate the weight of the 𝑗𝑗th indicator in the 𝑖𝑖th country

<!-- b000111 | prose | pages [9] -->
(2)

<!-- b000112 | prose | pages [9] -->
According to the concept of self-information and entropy in information theory, the infor- mation entropy 𝐸𝐸𝑗𝑗 of each evaluation indicator can be calculated, and thus

<!-- b000113 | prose | pages [9] -->
(3)

<!-- b000114 | prose | pages [9] -->
Based on the information entropy, we will further calculate the weight of each evaluation indicator we defined before.

<!-- b000115 | prose | pages [9] -->
(4)

<!-- b000116 | heading | pages [10] -->
4.2.2 AHP

<!-- b000117 | prose | pages [10] -->
First, between the same layers, we analyze the importance of indicators by constructing a judgment matrix.

<!-- b000118 | prose | pages [10] -->
(5)

<!-- b000119 | prose | pages [10] -->
in the above formula, 𝑏𝑏𝑖𝑖𝑖𝑖and 𝑏𝑏𝑖𝑖𝑖𝑖 represent different evaluation indicators, 𝑖𝑖= 1,2,3, ⋯𝑛𝑛, 𝑛𝑛 represents the number of indicators at the same level.

<!-- b000120 | prose | pages [10] -->
In order to ensure the accuracy of the judgment matrix, we perform a consistency check on the judgment matrix:

<!-- b000121 | prose | pages [10] -->
(6)

<!-- b000122 | prose | pages [10] -->
(7) In the formula, 𝜆𝜆𝑚𝑚𝑚𝑚𝑚𝑚 represents the largest eigenvalue of the judgment matrix, 𝑛𝑛 repre- sents the number of indicators at the same level. If calculated 𝐶𝐶𝐶𝐶< 0.1, then the judgment matrix can pass the consistency test.

<!-- b000123 | prose | pages [10] -->
Finally, based on the judgment matrix calculation, the subjective weight value 𝑈𝑈𝑖𝑖 solved by the AHP method is obtained.

<!-- b000124 | heading | pages [10] -->
4.2.3 Combination weight

<!-- b000125 | prose | pages [10] -->
The subjective weight 𝑈𝑈𝑖𝑖 and objective weight 𝐻𝐻𝑖𝑖 of each index are obtained by the AHP method and the EWM method.

<!-- b000126 | prose | pages [10] -->
(8) In the formula: 𝑄𝑄𝑖𝑖 is the comprehensive weight; 𝑚𝑚 and 𝑛𝑛 are the weight distribution coefficients.

<!-- b000127 | prose | pages [10] -->
The difference between subjective weight 𝑈𝑈𝑖𝑖 and objective weight 𝐻𝐻𝑖𝑖 should be the same as the difference between 𝑚𝑚 and 𝑛𝑛, At the same time, the sum of 𝑚𝑚 and 𝑛𝑛 is 1. As a result

<!-- b000128 | prose | pages [10] -->
(9)

<!-- b000129 | prose | pages [10] -->
In the formula,

<!-- b000130 | prose | pages [10] -->
Solve the equation to get the values of 𝑚𝑚 and 𝑛𝑛, Bring 𝑈𝑈𝑖𝑖 and 𝐻𝐻𝑖𝑖 into formula (8) then get the comprehensive weight 𝑄𝑄𝑖𝑖.

<!-- b000131 | heading | pages [11] -->
4.3  The Solution of Task 1

<!-- b000132 | prose | pages [11] -->
The subjective and objective weights are combined by the AHP-EWM method, and the weight values occupied by different indicators are finally obtained as shown in the figure 6.

<!-- b000133 | caption | pages [11] -->
Figure 6 Weight values for different indicators

<!-- b000134 | prose | pages [11] -->
Due to the different weights occupied by the different evaluation indicators above, we use the following formula

<!-- b000135 | prose | pages [11] -->
(10) In the formula (10), 𝑀𝑀𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠 represents the data analysis system maturity score, For the above results, based on the idea of Topsis method, We process and analyze the score 𝑀𝑀𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠 and introduce a membership function

<!-- b000136 | prose | pages [11] -->
(11) In the formula, 𝑀𝑀𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠 represents the data analysis system maturity score, represents the theoretical maximum, similarly, 𝑀𝑀𝑚𝑚𝑚𝑚𝑚𝑚  represents the theoretical minimum, based on the above method, the calculated maturity score of ICM's data analysis system is 0.8173. Accord- ing to the analysis in the figure 7, the existing data analysis system is in a relatively mature range, with a relatively high degree of maturity, and there is still room for improvement to a certain extent.

<!-- b000137 | caption | pages [11] -->
Figure 7 Maturity grading chart

<!-- b000138 | heading | pages [12] -->
5 TASK 2: Linear programming and System Dynamics

<!-- b000139 | heading | pages [12] -->
5.1 Model Overview

<!-- b000140 | prose | pages [12] -->
For the second problem, in order to maximize the potential of ICM's D&A system, con- sider adopting the goal planning model, combined with the DAMM model constructed in the first question, to convert the goal to maximize the score of the data analysis system. As shown in the figure 8, after ICM uses our model to evaluate the maturity of its own D&A system, we need to point out the best method to optimize the maturity of the D&A system through the demonstration analysis of the DAMM system, so that ICM can use its data assets maximum potential.

<!-- b000141 | caption | pages [12] -->
Figure 8 TASK 2 Process

<!-- b000142 | heading | pages [12] -->
5.2 Establishment of Model

<!-- b000143 | heading | pages [12] -->
5.2.1 Linear programming

<!-- b000144 | prose | pages [12] -->
The maturity score of the existing data analysis system is 0.8173 points, which belongs to a relatively mature category, but there is still a certain gap from the mature category (higher than 0.9 points). The maturity score of the data analysis system maximizes the score under certain constraints.

<!-- b000145 | prose | pages [12] -->
The maturity index of the data analysis system after being evaluated by the DAMM model： Step 1: Determination of decision variables According to the requirements of the problem, this paper assumes that the cost required to increase different evaluation indicators by 1% is known, and determines the size of the im- provement of different indicators as a decision variable, and optimizes the target by adjusting the size of the improvement of the indicators.

<!-- b000146 | prose | pages [12] -->
Step 2: Analysis of the objective function Analyzing the background of the problem, in order to maximize the potential of the data assets of ICM's data analysis system, this paper determines the objective function as follows:

<!-- b000147 | prose | pages [12] -->
(12)

<!-- b000148 | prose | pages [12, 13] -->
Where represents the maturity score of the optimized D&A system, and represent the upper limit of the index improvement.

<!-- b000150 | prose | pages [13] -->
Step 3: Constraint Analysis Ⅰ Question 2 also satisfies the assumption of task 1, so the optimization model needs to meet the constraints established by the DAMM model. The highest score of the optimized index is still 1 point, thus

<!-- b000151 | prose | pages [13] -->
(13)

<!-- b000152 | prose | pages [13] -->
Ⅱ At the same time, when improving the index parameters, the sum of the cost 𝑏𝑏 for the improvement of the index parameters cannot exceed the cost that the company can

<!-- b000153 | prose | pages [13] -->
bear for the improvement of the D&A system, thus

<!-- b000154 | prose | pages [13] -->
(14) Ⅲ In addition, due to the improvement of the indicators to play the potential of the data analysis system, the existing indicators can only be maintained or improved, in consequence

<!-- b000155 | prose | pages [13] -->
(15)

<!-- b000156 | prose | pages [13] -->
Ⅳ According to the assumption, the literature data we checked is accurate and scientific, and the sum of all indicators remains unchanged, which is (16) 𝜇𝜇 means that the number of all indicators is unchanged.

<!-- b000157 | heading | pages [13] -->
Step 4: Model results

<!-- b000158 | prose | pages [13] -->
According to the above linear programming model, assuming that the cost b and total budget cost Δ required to increase different indicators of ICM company by 1% are known, the optimized maturity index score can be obtained according to the model analysis and

<!-- b000159 | prose | pages [13] -->
calculation. The percentage value determines the optimization method of the D&A system.

<!-- b000160 | heading | pages [13] -->
5.2.2 System Dynamics

<!-- b000161 | prose | pages [13] -->
System dynamics is a very practical and effective method to solve complex system prob- lems [11]. In the past 30 years, system dynamics has been widely used in research fields such as management, psychology, and environmental science [8]. The D&A system evaluation sys- tem covers a very wide range, and the factors affecting the maturity of the system are complex. Using system dynamics theory to systematically study the data analysis system, it can not only conduct comprehensive macro research by integrating all factors, but also conduct micro anal- ysis. Starting from a certain influencing factor, analyze its impact on the exploration of the potential of data assets, which can provide a more scientific and reasonable decision for ICM to improve the maturity of the D&A system.

<!-- b000162 | prose | pages [14] -->
Here is a simple data verification and analysis. According to problem 1, from the perspec- tive of the data analysis system of five different maturity levels in the DAMM model, the sys- tem dynamics model is used to simulate the corresponding index parameter ranges of the five groups of models, and Analysis, the specific steps are as follows Step 1: Convert all the evaluation indicators in the DAMM model into the control varia- bles of the system dynamics, replace the original variables with the products between the con- trol variables and the variables, and analyze and calculate the predicted value;

<!-- b000163 | prose | pages [14] -->
Step 2: By combining different values of different control variables, five data analysis systems with different maturity levels are simulated and set up;

<!-- b000164 | prose | pages [14] -->
Step 3: The parameters of the model control variables are subjected to multiple pre-ex- periments to achieve a high degree of simulation.

<!-- b000165 | heading | pages [14] -->
5.3 The Solution of Task 2

<!-- b000166 | prose | pages [14] -->
Finally, the different parameter combination values are obtained as shown in the following table.

<!-- b000167 | caption | pages [14] -->
Figure 9 Indicators weight values under different maturity levels

<!-- b000168 | prose | pages [14] -->
I1-I8 in the figure 9 represent I1: process visualization, process coverage, process reengi- neering; I2: process stability, process complexity; I3: positioning capability, collection effi- ciency; I4: technical stability, technical innovation; I5: storage Ability, response speed; I6: teamwork, talent management; I7: IT capability, training and employment costs; I8: number of people, education.

<!-- b000169 | prose | pages [14] -->
Analyzing the figure 9, the parameters of the simulated good level are basically the same as the index weight values in task 1. We measure the difference between the model's simulated value and ICM's actual value in terms of mean absolute percent error (MAPE), thus

<!-- b000170 | prose | pages [14] -->
(17)

<!-- b000171 | prose | pages [14] -->
Where 𝐴𝐴𝑡𝑡 represents the index value in problem 1, 𝐹𝐹𝑡𝑡 represents the system dynamics simulation value, 𝑛𝑛 represents the number of simulation values, and 𝑡𝑡 is 8. After calculation, the MAPE value of the good level is 7.6%, lower than 10%, which is high precision Prediction, verifying the validity and stability of the DAMM model. Combined with task 1, according to the simulation of the system dynamics model, the difference between the good level and the excellent level of the different indices is shown in the figure 10:

<!-- b000172 | caption | pages [15] -->
Figure 10 Comparison of the weight value of good grade and excellent grade

<!-- b000173 | prose | pages [15] -->
According to the analysis of the above figure, the biggest difference between ICM's good grade and excellent grade is the level of teamwork and technical management. If the limited capital is invested in the construction of these two aspects, the greatest potential of data assets can be exerted.

<!-- b000174 | heading | pages [15] -->
6 TASK 3:System Effectiveness Measure Model Based on Apriori

<!-- b000175 | heading | pages [15] -->
6.1 Model Overview

<!-- b000176 | prose | pages [15] -->
For problem 3, based on problem 2, we use system dynamics simulation to simulate mul- tiple sets of data for each maturity level, and then set different level standards for people, tech- nology and process. Formulate the standard to measure the effectiveness of the data analysis system, which is mainly solved by the Apriori based on the association relationship.

<!-- b000177 | heading | pages [15] -->
6.2 Data Processing

<!-- b000178 | prose | pages [15] -->
From task 1 and task 2, the system dynamics simulation obtains a series of score values for people, technology, and process, as shown in the table 3:

<!-- b000179 | prose | pages [15] -->
Ⅰ Set up experimental group data and control group data Set the data based on system dynamics simulation as the experimental data for correlation analysis, and the data analyzed in Task 1 as the control group data, which is used to verify the results of the association rules for the experimental group data.

<!-- b000180 | prose | pages [15] -->
Ⅱ Data discretization Different index values correspond to different maturity levels, that is, three influencing factors and one affected factor. Discretize these data. Considering the continuous linear nature of human, technical, and process variables, we use the equal-width discrete method. For the division of maturity level, we follow the level division given by DAMM in Task 1.

<!-- b000181 | caption | pages [16] -->
Table 3 Simulation data discretization results

<!-- b000182 | prose | pages [16] -->
Number Maturity People Technol- Process ogy 1 M1 A1 B1 C1 2 M1 A2 B1 C3 3 M2 A2 B2 C2 4 M2 A1 B3 C4 5 M3 A4 B1 C4 6 M3 A2 B4 C4 7 M4 A4 B3 C3 8 M4 A2 B4 C2 9 M5 A2 B4 C4 10 M5 A4 B3 C4 11 M5 A3 B4 C3 12 M5 A4 B4 C4 Maturity level M1 (0~0.25), M2 (0.25~0.5), M3 (0.5~0.75), M4 (0.75~0.9), M5 (0.9~1); People level A1 (0~0.25), A2 (0.25~0.5), A3 (0.5~0.75),A4 (0.75~1); Technical level B1 (0~0.25)， B2 (0.25~0.5), B3 (0.5~0.75), B4(0.75~1); Process level B1 (0~0.25), B2 (0.25~0.5), B3 (0.5~0.75), C4(0.75~1);

<!-- b000183 | prose | pages [16] -->
Classify and arrange the results of the discretization of the data, the level division and specific values are shown in the figure 11：

<!-- b000184 | caption | pages [16] -->
Figure 11 The respective grades of the three indicators

<!-- b000185 | heading | pages [16] -->
6.3 Establishment of Apriori

<!-- b000186 | prose | pages [16] -->
The specific process of Apriori algorithm analyzing data is shown in the figure 12:

<!-- b000187 | caption | pages [17] -->
Figure 12 Apriori algorithm analysis process

<!-- b000188 | prose | pages [17] -->
The support and confidence are measured by setting thresholds. In this paper, the mini- mum support threshold is set to 20%, and the minimum confidence threshold is 60%. We con- tinuously filter candidate sets, iteratively search layer by layer to obtain more candidate sets, and then realize the generation of connection relation.

<!-- b000189 | heading | pages [17] -->
6.4 Analysis of The Result

<!-- b000190 | prose | pages [17] -->
The final valid association rule data mining table is shown in the table 4:

<!-- b000191 | caption | pages [17] -->
Table 4 Effective Association Rules Mining Table

<!-- b000192 | prose | pages [17] -->
ID Rule Support Confidence

<!-- b000193 | prose | pages [17] -->
1 B4,C4 ⟹ M5 19.05% 57.14% 2 19.05% 57.14% A3,B4 ⟹ M5 3 19.05% 85.17% A4,B4 ⟹ M5 4 B4,C3 ⟹ M5 28.57% 85.17% 5 28.57% 85.17% A4,B3,C4 ⟹ M5 6 28.57% 85.17% A4,B4,C4 ⟹ M5

<!-- b000194 | heading | pages [17] -->
Result analysis:

<!-- b000195 | prose | pages [17, 18] -->
(1) Rules ID2, ID5, ID6 indicate that the fourth-level people level A4 (0.8~1.0) has ex- tremely high support and confidence (28.57%, 85.71%) to the fifth-level maturity M5 (0.9~1.0), and the third-level people level A3 (0.6~0.8) has high support and confidence (19.05%, 57.14%) for the fifth-level maturity, indicating that when the people level reaches the fourth-level, the maturity of ICM's data analysis system can reach a higher level, that is, a higher level of system effectiveness.

<!-- b000197 | prose | pages [18] -->
(2) Rules ID4, ID5, and ID6 indicate that the third-level technical level B3 (0.6~0.8) and the fourth-level technical level B4 (0.8~1.0) have extremely high support for the fifth-level maturity M5 (0.9~1.0). and confidence (28.57%, 85.71%), indicating that the technical require- ments are lower than the people level. When the technical level reaches the third and fourth level, the level of the data analysis system can reach a higher level.

<!-- b000198 | prose | pages [18] -->
(3) Rules ID5 and ID6 indicate that the support of the fourth-level process level C4 (0.8~1.0) to the fifth-level maturity M5 (0.9~1.0) is 28.57%, and the confidence level is 85.71%, indicating that the process level reaches the fourth level. At the high level, its data analysis system is more effective.

<!-- b000199 | prose | pages [18] -->
(4) Comprehensive analysis of all rules, when the people of the data analysis system of ICM company reaches the fourth level, the technology reaches the third or fourth level, and the process reaches the fourth level, the effectiveness of the data analysis system is fine.

<!-- b000200 | heading | pages [18] -->
7 TASK 4: Sensitivity Analysis and Model promotion

<!-- b000201 | prose | pages [18] -->
Analyzing whether our model can be used for larger or smaller seaport companies, which is essentially a test of the DAMM model. For this problem, the analysis is easy to understand. As shown in the figure below, the amount of data contained in larger seaport companies More, the requirements for technical stability and technical response speed are higher; smaller seaport companies have less data volume and fewer people in the data analysis system, so they have higher requirements for the personal ability of people. Therefore, companies of different scales have different emphases in the evaluation of maturity, and the weight values of the indicators obtained based on the AHP-EWM method in task 1 are different.

<!-- b000202 | caption | pages [18] -->
Figure 13 The focus of seaports of different scales

<!-- b000203 | heading | pages [18] -->
7.1 Sensitivity Analysis

<!-- b000204 | prose | pages [18, 19] -->
After adjusting the weight values of people, technology and process, the system dynamics model in question 2 is used to re-simulate, and the error value e between the simulation results and the actual evaluation value of DAMM is analyzed, and the error results change graph are obtained as follows:

<!-- b000206 | caption | pages [19] -->
Figure 14 Error value between simulation result and actual evaluation value

<!-- b000207 | prose | pages [19] -->
Analyze the figure 14 , with the change of the relative size of the seaport, the error between the evaluation results of the DAMM model and the simulation results is small, and both remain below 5%, which shows the good applicability of the model to seaport companies of different sizes.

<!-- b000208 | heading | pages [19] -->
7.2 Model promotion

<!-- b000209 | prose | pages [19] -->
The universality of the DAMM system lies in:

<!-- b000210 | prose | pages [19] -->
A.DAMM is not directly based on the data level analysis generated by the specific cargo movement of the intercontinental freight company, but conducts evaluation and modeling from the perspectives of people, technology and process. Different types of systematic evaluation are inseparable from people and technology. and process three factors, thus ensuring that the model can be directly transferred in the systematic evaluation of different types of companies;

<!-- b000211 | prose | pages [19] -->
B. For freight companies, based on the ISO9001 "Quality Management System Require- ments" international standard plan and grounded theory[12], DAMM is used to evaluate the system based on people, process and technology, which has the characteristics of conformity, Systematic and overall effectiveness.

<!-- b000212 | prose | pages [19] -->
For ICM companies, if their customers also use the DAMM model, there will be the fol- lowing benefits (as shown in figure 5):

<!-- b000213 | prose | pages [19] -->
A. ICM companies can understand the current maturity index of different customers to help them better analyze customers.

<!-- b000214 | prose | pages [19] -->
B. ICM companies can know the current problems of their own services to help them make better decisions.

<!-- b000215 | heading | pages [19] -->
C. ICM companies can analyze the positioning of current customers and facilitate the

<!-- b000216 | prose | pages [19] -->
development of differentiated plans.

<!-- b000217 | caption | pages [20] -->
Figure 15 Advantages of the DAMM Model

<!-- b000218 | heading | pages [20] -->
8 Model Evaluation and Further Discussion

<!-- b000219 | heading | pages [20] -->
8.1 Strengths

<!-- b000220 | prose | pages [20] -->
 We use the AHP-EWM method to build an evaluation model of the maturity of the data analysis system, and use more sufficient indicators to build a complete maturity evaluation model;  When analyzing how to maximize the potential of data assets, we use system dynam- ics simulation to obtain simulation data, and qualitatively give improvement strate- gies; at the same time, combined with linear programming methods, we quantitatively analyze the focus of model improvement. The combination of the two methods en- hances the robustness of the model;  We have done enough visualization of the algorithms and results in this paper for easy understanding;  Our maturity evaluation model DAMM is based on three aspects: people, technology and process, and has good promotion significance and value;  Most of our models are based on innovative ideas or improvements based on the orig- inal theory and the problem of this paper, making our models both theoretical and innovative.

<!-- b000221 | heading | pages [20] -->
8.2 Weaknesses

<!-- b000222 | prose | pages [20] -->
 We could have analyzed the relationship between the three levels of factors in more depth, but due to space limitations, our work can only do this for the time being.  Due to the lack of actual numerical reference, we can only observe the accuracy of the model from the comparison of simulation and evaluation model, but cannot meas- ure the accuracy of the model through the calculation of actual company data.

<!-- b000223 | heading | pages [21] -->
References

<!-- b000224 | references | pages [21] -->
[1] Paulk M. Comparing ISO 9001 and the Capability Maturity Model for Software[J].

<!-- b000225 | references | pages [21] -->
Kluwer Academic Publishers, 1993,2(4): 245-256

<!-- b000226 | references | pages [21] -->
[2] Pekka B M，Mikko L J. Assessment of quality and maturity level of R &D [J]. Production

<!-- b000227 | references | pages [21] -->
Economics,2002,(78):29-35

<!-- b000228 | references | pages [21] -->
[3] Kirazli A T, Moetz O B. (2015). “A methodological approach for evaluatingthe influences

<!-- b000229 | references | pages [21] -->
of Industrie 4.0 on risk management of the goods receiving area in a German automotive

<!-- b000230 | references | pages [21] -->
manufacturer”, in Proceedings of the 22nd Eur OMA Conference. Operations Manage-

<!-- b000231 | references | pages [21] -->
ment for Sustainable Competitiveness.

<!-- b000232 | references | pages [21] -->
[4] Crawford J K. PM Solutions. Project Management Maturity[J].New York:Marcel Dek-

<!-- b000233 | references | pages [21] -->
ker,2002:76-81

<!-- b000234 | references | pages [21] -->
[5] WILTJER HANNEKE, SEERS KATE, TUTTON ELIZABETH. Understanding assess-

<!-- b000235 | references | pages [21] -->
ment on a hospital ward for older people: A qualitative study[J]. Journal of advanced

<!-- b000236 | references | pages [21] -->
nursing,2019(4). DOI:10.1111/jan.13930.

<!-- b000237 | references | pages [21] -->
[6] Tobias Mettlera, Chen, Y. , Wang, H. , Chenjing, Zhang, J. , & Wang, H. , et al. (2011).

<!-- b000238 | references | pages [21] -->
The study on the influencing factors of patients' loyalty to hospitals of grade three,class

<!-- b000239 | references | pages [21] -->
a. Modern Hospital Management.

<!-- b000240 | references | pages [21] -->
[7] Tao Hongfei, Sun Yixin, Wu Guowei, et al. Maturity assessment of power information

<!-- b000241 | references | pages [21] -->
system based on big data and AHP[J]. China Electric Power, 2016(10). DOI:

<!-- b000242 | references | pages [21] -->
10.11930/j.issn.1004-9649.2016.10.114.05.

<!-- b000243 | references | pages [21] -->
[8] Lin Yongyi, Li Minqiang. Research on Maturity Model of Enterprise Business Process

<!-- b000244 | references | pages [21] -->
Management [J]. Modern Management Science, 2008(7). DOI:10.3969/j.issn.1007-

<!-- b000245 | references | pages [21] -->
368X.2008.07.036.

<!-- b000246 | references | pages [21] -->
[9] Xie Gang, Feng Ying, Li Zhiwen. The maturity model of customer information quality

<!-- b000247 | references | pages [21] -->
management under the background of big data [J]. China Circulation Economy,

<!-- b000248 | references | pages [21] -->
2015(5). DOI:10.3969/j.issn.1007-8266.2015.05.015.

<!-- b000249 | references | pages [21] -->
[10] De Carolis A., Macchi M., Negri E., et al. A Maturity Model for Assessing the Digital

<!-- b000250 | references | pages [21] -->
Readiness of Manufacturing Companies[M]. Berlin; Springer International Publishing,

<!-- b000251 | references | pages [21] -->
2017.

<!-- b000252 | references | pages [21] -->
[11] Technology; Reports from Islamic Azad University Describe Recent Advances in Tech-

<!-- b000253 | references | pages [21] -->
nology (Identification of the determinants of Blockchain-based business model using hy-

<!-- b000254 | references | pages [21] -->
brid method: Content analysis & System Dynamics)[J]. Journal of Engineering, 2019.

<!-- b000255 | references | pages [21] -->
[12] Triana, Yaya Sudarya and Retnowardhani, Astari. Analyze System of Quality Manage-

<!-- b000256 | references | pages [21] -->
ment Using ISO 9001:2015 (Case Study: PT. XYZ)[J]. Advanced Science Letters, 2018,

<!-- b000257 | references | pages [21] -->
24(11) : 8774-8777(4).

<!-- b000258 | references | pages [22] -->
Dear ICM Seaport Users:

<!-- b000259 | references | pages [22] -->
We are the researchers invited by ICM to as-

<!-- b000260 | references | pages [22] -->
sess the maturity of its D&A system, As a large

<!-- b000261 | references | pages [22] -->
seaport, ICM generates a large amount of data

<!-- b000262 | references | pages [22] -->
information every day. Only with a sufficiently

<!-- b000263 | references | pages [22] -->
mature data analysis system can these data be

<!-- b000264 | references | pages [22] -->
fully utilized, understand the problems and

<!-- b000265 | references | pages [22] -->
needs of customers in a timely manner, and then

<!-- b000266 | references | pages [22] -->
reasonably deploy the work to provide more con-

<!-- b000267 | references | pages [22] -->
venience for port users and save your precious

<!-- b000268 | references | pages [22] -->
time in the port. Therefore, an objective and reasonable evaluation of the ICM data analysis

<!-- b000269 | references | pages [22] -->
system to provide optimization advice is necessary and closely related to your vital interests.

<!-- b000270 | references | pages [22] -->
Our evaluation system is based on a large number of existing professional theories and

<!-- b000271 | references | pages [22] -->
expert opinions, combined with the actual situation of ICM's D&A system, and has carried

<!-- b000272 | references | pages [22] -->
out a scientific and reasonable analysis of the concerns of ICM and port users. A number of

<!-- b000273 | references | pages [22] -->
indicators are considered in all aspects, and then a comprehensive and objective evaluation

<!-- b000274 | references | pages [22] -->
of ICM's D&A system is carried out.

<!-- b000275 | references | pages [22] -->
In our evaluation system, ICM's data analysis system finally got a score of 0.8173 (the

<!-- b000276 | references | pages [22] -->
highest score is 1), which proves that ICM's data analysis system is at a relatively mature

<!-- b000277 | references | pages [22] -->
level. It also confirms the undoubted data analysis strength of ICM as a large seaport，Only

<!-- b000278 | references | pages [22] -->
slightly lacking in talent management and teamwork. Reasonable optimizations will be made

<!-- b000279 | references | pages [22] -->
under our guidance, and finally its data analysis system will reach a quite ideal level. ICM

<!-- b000280 | references | pages [22] -->
will be more profound to the needs of port users, be more sensitive to problems, and provide

<!-- b000281 | references | pages [22] -->
better services to facilitate the use of seaports by you.

<!-- b000282 | references | pages [22] -->
Because our evaluation system is based on people, technology and process, which is con-

<!-- b000283 | references | pages [22] -->
sistent in large and small ports and other industries, it is also applicable to all enterprises.

<!-- b000284 | references | pages [22] -->
I believe that using our evaluation system, you can also have a deeper understanding of

<!-- b000285 | references | pages [22] -->
yourself. You will also have more trust in ICM's data analysis capabilities to achieve the goal

<!-- b000286 | references | pages [22] -->
of mutual benefit and win-win.

<!-- b000287 | references | pages [22] -->
Yours,Team 2215444
