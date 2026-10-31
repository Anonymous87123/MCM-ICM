# P-D-2020-2003723-28f692ff

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Problem Chosen

<!-- b000002 | furniture | pages [1] -->
2020

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | prose | pages [1] -->
MCM/ICM

<!-- b000005 | title | pages [1] -->
D

<!-- b000006 | furniture | pages [1] -->
2003723

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Teaming Strategies in Football: Patterns and Effects

<!-- b000009 | prose | pages [1] -->
Objective analysis of the football team's performance is the main way to set training targets, and improve the team's level. Existing analysis of team performance is mostly based on the traditional technical statistics of individual athletes, but seldom discusses the important roles of the interrelationships and synergies between athletes. In view of this, this paper adopts the perspective of players' cooperation network, constructs the analysis framework of "identifying cooperation network–expanding cooperation model-exploring influence effect–putting forward suggestions", quantitatively analyzes the cooperation relationship of Huskies football team and its influence law on competition performance. We have mainly solved the following four problems: Firstly, in order to identify the cooperation network, this paper constructs a complex network model based on directional weighted graph based on the characteristics and data of passing the ball. This paper constructs cooperation network indicators and other structural indicators from multiple scales. We refer to gene coding types to distinguish binary and ternary structures, use the simulation chart of competition field to mine the team formation rules, and adopt heterogeneity analysis to explore the relationship between individual players and the team, as well as the change rules of different network indicators with time. Secondly, in order to measure team cooperation performance more comprehensively, this paper constructs a comprehensive evaluation index system by integrating Individual contributions to the team, Team structure, Strategic layout, Environment variables and 13 sub-indicators. Among them, in order to make clear the Individual contribution to the team, this paper combines subjective and objective weights, uses AHP and entropy weight to construct a sub-model of player scoring. Thirdly, we research the mechanism where team strategy and other factors affect victory. For heterogeneity analysis, we build multi-classification undirected logistic regression models from two levels, winning and losing situations and score results to distinguish team formations. We also deal with multiple collinearity and other issues. The results show that Huskies is suitable to adopt an attack-defense balanced formation and a right-wing attack style, and it is more effective to adopt counter-strategies appropriately according to the opponent's situation. Fourthly, according to Huskies' network structure and relevant research conclusions, it is believed that the overall framework and contingency mechanisms, individual and collective factors, subjective and objective factors, long-term and short-term situations should be considered in order to form an excellent football team. Extended to other types of teams, other factors such as leadership, gender composition and team culture should be considered as well.

<!-- b000010 | prose | pages [1] -->
To sum up, the advantages of this paper are as follows: (1)Pertinence: choose statistical indicators and models that can better reflect the characteristics of football matches and player networks; (2)Clear hierarchy：make different analysis and comparison from the angles of attack style, team formation, sample range and consider the outcome of the match; (3)Reliability: use robust analysis method and multiple tests; (4)Extensibility: put forward practical suggestions to the football team and even the broader competition team.

<!-- b000011 | keywords | pages [1] -->
Key words: Team Strategy, Football, Network Science, Logistic Regression

<!-- b000012 | prose | pages [1] -->
关注数学模型

<!-- b000013 | furniture | pages [1] -->
2

<!-- b000014 | furniture | pages [1] -->
MATHmodels

<!-- b000015 | furniture | pages [1] -->
获取更多资讯

<!-- b000016 | furniture | pages [2] -->
Team # 2003723                                                            Page  2  of  25

<!-- b000017 | heading | pages [2] -->
Contents

<!-- b000018 | contents | pages [2] -->
1

<!-- b000019 | contents | pages [2] -->
INTRODUCTION .................................................................................................. 3

<!-- b000020 | contents | pages [2] -->
1.1 Background ................................................................................................. 3

<!-- b000021 | contents | pages [2] -->
1.2 Restatement of the Problem ......................................................................... 3

<!-- b000022 | contents | pages [2] -->
1.3 Our Work ..................................................................................................... 3

<!-- b000023 | contents | pages [2] -->
2

<!-- b000024 | contents | pages [2] -->
ASSUMPTIONS AND JUSTIFICATIONS ................................................................... 4

<!-- b000025 | contents | pages [2] -->
3

<!-- b000026 | contents | pages [2] -->
NOTATIONS......................................................................................................... 4

<!-- b000027 | contents | pages [2] -->
4

<!-- b000028 | contents | pages [2] -->
COMPLEX NETWORK MODEL ............................................................................ 5

<!-- b000029 | contents | pages [2] -->
4.1 Network of One Match ................................................................................. 5

<!-- b000030 | contents | pages [2] -->
4.2 Match Networks summary ........................................................................... 8

<!-- b000031 | contents | pages [2] -->
4.3 Time Dimension Exploration ....................................................................... 8

<!-- b000032 | contents | pages [2] -->
5

<!-- b000033 | contents | pages [2] -->
TEAMWORK MODEL .......................................................................................... 9

<!-- b000034 | contents | pages [2] -->
5.1 Individual contributions sub-model ........................................................... 10

<!-- b000035 | contents | pages [2] -->
5.2 Construction of Team’s Network Structure and Strategic Layout Index .... 13

<!-- b000036 | contents | pages [2] -->
5.3 Regression Model ....................................................................................... 14

<!-- b000037 | contents | pages [2] -->
5.4 Multicollinearity Analysis .......................................................................... 14

<!-- b000038 | contents | pages [2] -->
6

<!-- b000039 | contents | pages [2] -->
STRUCTURAL STRATEGY ANALYSIS AND SUGGESTIONS.................................... 17

<!-- b000040 | contents | pages [2] -->
6.1 Results of Team Performance Model of Huskies Team .............................. 17

<!-- b000041 | contents | pages [2] -->
6.2 Suggestions Based on Data Analysis Results ............................................. 18

<!-- b000042 | contents | pages [2] -->
7

<!-- b000043 | contents | pages [2] -->
EXTENSION OF THE MODEL .............................................................................. 19

<!-- b000044 | contents | pages [2] -->
7.1 Sorting out the Existing Conclusions ......................................................... 19

<!-- b000045 | contents | pages [2] -->
7.2 Dimension Extension ................................................................................. 20

<!-- b000046 | contents | pages [2] -->
8

<!-- b000047 | contents | pages [2] -->
STRENGTHS AND WEAKNESSES ........................................................................ 21

<!-- b000048 | contents | pages [2] -->
8.1 Strengths .................................................................................................... 21

<!-- b000049 | contents | pages [2] -->
8.2 Weaknesses ................................................................................................ 22

<!-- b000050 | contents | pages [2] -->
9

<!-- b000051 | contents | pages [2] -->
CONCLUSION .................................................................................................... 22

<!-- b000052 | contents | pages [2] -->
REFERENCE ............................................................................................................ 23

<!-- b000053 | contents | pages [2] -->
APPENDIX ............................................................................................................... 24

<!-- b000054 | contents | pages [2] -->
关注数学模型

<!-- b000055 | furniture | pages [2] -->
2

<!-- b000056 | furniture | pages [2] -->
MATHmodels

<!-- b000057 | furniture | pages [2] -->
获取更多资讯

<!-- b000058 | furniture | pages [3] -->
Team # 2003723                                                            Page  3  of  25

<!-- b000059 | heading | pages [3] -->
1 Introduction

<!-- b000060 | heading | pages [3] -->
1.1 Background

<!-- b000061 | prose | pages [3] -->
As one of the three popular ball games, football's charm is not only because of its entertainment and sports, but also a project that embodies team cooperation and collective wisdom. Football is a team sport with complex interactions between players (Duch et.al 2010) [1]. In the process of team cooperation, the performance and cooperation of the team members are very important. Due to the interaction and cooperation of team members, there are relatively complex relationships in the team, which can be regarded as a complex network. Network science is a field to study complex network relations, and its application in group sports is more and more extensive and in-depth. FanBu et.al constructed the basketball passing network and proposed an evaluation model to describe each player's role in the group passing network [2]. J. M. BuldúJ. showed the different levels of indicators and dimensions of many football match networks [3]. Victor Martins Maimone applies complex network analysis not only to competitions but also to the prediction of results[4]. The perfection of complex network analysis indexes and dimensions provides us with many references for our research. According to many indicators of complex network construction, it will provide important basis for us to further analyze the structure, configuration and dynamics of team cooperation.

<!-- b000062 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000063 | prose | pages [3] -->
To solve the problem of model construction and application of team cooperation, we need to solve the following problems:

<!-- b000064 | prose | pages [3] -->
First of all, we need to construct a passing network for the host and the guest of each match according to the known data set, and construct and solve many structural indexes and network attributes, and need to construct it in multiple dimensions.

<!-- b000065 | prose | pages [3] -->
Then we need to establish a successful team cooperation model combining the passing network and other indicators. This model mainly considers the performance indicators and cooperation process of the team in the competition, grasps the structure, configuration and dynamic aspects of team cooperation, and considers the universality and particularity of the model.

<!-- b000066 | prose | pages [3] -->
Next, we need to analyze according to the passing network and team cooperation model, and put forward specific suggestions for husky's team's structural strategy.

<!-- b000067 | prose | pages [3] -->
Finally, we need to extend the model from special to general, and extend the model from the field of football competition to other fields.  We need to think about how to design an effective team, and point out the idea of extending the model and the conditions that we need to know before extending.

<!-- b000068 | prose | pages [3] -->
1.3 Our Work

<!-- b000069 | prose | pages [3] -->
In response to the questions and requests, we have done the following:

<!-- b000070 | prose | pages [3] -->
For the construction of the passing network, we used the method and index of complex network analysis to visualize the model of the passing network and many

<!-- b000071 | prose | pages [3, 4] -->
关注数学模型 indexes of the network, and recorded the indexes in the data set.

<!-- b000072 | furniture | pages [3] -->
2

<!-- b000073 | furniture | pages [3] -->
MATHmodels

<!-- b000074 | furniture | pages [3] -->
获取更多资讯

<!-- b000075 | furniture | pages [4] -->
Team # 2003723                                                            Page  4  of  25

<!-- b000077 | prose | pages [4] -->
For the construction of team work model, we use logistic regression analysis method and divide the explanatory variables into four aspects: Individual contributions, Team structure ,Strategic layout and environmental variables. Among them, aiming at the variables of Individual contributions, we established a sub-model to score everyone in the team by combining analytic hierarchy process and entropy weight method. We use the methods of literature review and data mining to obtain other variables. After that, we showed, analyzed and corrected the regression results, and gained some inspiration from it.

<!-- b000078 | prose | pages [4] -->
As for the suggestions of Husky team, we will refine the team cooperation model established by all teams to Husky team and make a more detailed analysis of the model.

<!-- b000079 | prose | pages [4] -->
For the development and application of team work model, we have made some reflections on the existing model and team cooperation, consulted a large number of documents, and summarized and sorted out the conclusions.

<!-- b000080 | prose | pages [4] -->
The remainder of this study is organized as follows. The second chapter describes the assumptions we use and explains the rationality of the assumptions. The third chapter describes the symbols we use and their meanings.  The fourth chapter shows the passing network model we have built and many indicators. In the chapter 5, the team performance model is constructed by using 15 dimensions such as passing network parameters. We also test and modify the model. In the chapter 6, we analyzed the potential items of the Husky team according to the model, and put forward suggestions on different aspects of the Husky team such as formation. In the chapter 7, we consider the generalized model of team performance. In the chapter 8, we evaluate the validity and limitation of the model. In the chapter 9,we draw the conclusion.

<!-- b000081 | heading | pages [4] -->
2 Assumptions and Justifications

<!-- b000082 | prose | pages [4] -->
⚫ The principle of difference in the same position: each player has his or her own main responsibilities set in advance. even if players in different positions do the same behavior, the importance of the behavior will be different.

<!-- b000083 | prose | pages [4] -->
⚫ When players in the same position are replaced, the team's tactical style will not change. When players in different positions are replaced, the tactical style may be changed.。 ⚫ The behavior on the court can be divided into four types: attack, defense, passing and mistake. Among them, effective offense, defense and passing are positively affected, while mistakes negatively affect the overall performance.

<!-- b000084 | prose | pages [4] -->
⚫ Team formation is mainly divided into offensive, defensive and court balance. The more forwards, the more offensive, and the more defenders, the more defensive.

<!-- b000085 | prose | pages [4] -->
⚫ The tactical style of the same team in a match remains stable and depends on the formation with the longest duration in the match.

<!-- b000086 | heading | pages [4] -->
3 Notations

<!-- b000087 | prose | pages [4] -->
The notations for the model under study are shown below.

<!-- b000088 | prose | pages [4] -->
关注数学模型

<!-- b000089 | furniture | pages [4] -->
2

<!-- b000090 | furniture | pages [4] -->
MATHmodels

<!-- b000091 | furniture | pages [4] -->
获取更多资讯

<!-- b000092 | furniture | pages [5] -->
Team # 2003723                                                            Page  5  of  25

<!-- b000093 | caption | pages [5] -->
Table1.Notations of the model

<!-- b000094 | heading | pages [5] -->
4 Complex Network Model

<!-- b000095 | prose | pages [5] -->
In this chapter, we create a directional weighted passing network for passing between players in football matches [5]. In this network, each player is a node and each pass is an arc between players. Using this passing network, we can not only identify common passing patterns, but also find out the classical football evaluation indexes and attribute indexes and present these results visually.

<!-- b000096 | prose | pages [5] -->
4.1 Network of One Match

<!-- b000097 | prose | pages [5] -->
Let's take a match as an example, set each player as a node, set each pass as an arc between players, set the number of directional passes between players as a weight, and create adjacency matrix 𝐴𝑖𝑗 and directional weighted pass network 𝐺. According to the passing network, we can identify passing patterns, such as triads, formations, etc. We can solve the classical football evaluation indexes, such as passing rate, Goal attempts, etc. We can solve the network parameters, such as clustering coefficient, maximum eigenvector, maximum eigenvector centrality of players in the team, etc. We can also visualize these results.

<!-- b000098 | prose | pages [5] -->
4.1.1 Structural Indicators

<!-- b000099 | prose | pages [5] -->
We consider Dyad Configurations. There are two types of dyadic configurations, one is the most common i to j, j to others, called "double pass"; The other is I to j, j next to I, called "single pass". We will count the team's highest frequency patterns of dyadic configurations in a match and analyze their passing characteristics. Taking the Huskies in the first game, the Huskies did 46 "double pass" and 280 "single pass".

<!-- b000100 | prose | pages [5] -->
We consider Triadic Configurations. Complex networks often have motifs, which can also be called subgraphs. Among them, the most common mode is[6]. If we select three vertices and the lines among them in the directed network, we always get one of the 16 combinations. The subgraph on three vertices is called a triad. And triads labeling is generally known.

<!-- b000101 | prose | pages [5] -->
From the established passing model, we select the triads pattern with the largest

<!-- b000102 | prose | pages [5, 6] -->
关注数学模型 frequency used by husky team in this match by counting each extracted triads subgraph. Figure1 is its pattern diagram.

<!-- b000103 | furniture | pages [5] -->
2

<!-- b000104 | furniture | pages [5] -->
MATHmodels

<!-- b000105 | furniture | pages [5] -->
获取更多资讯

<!-- b000106 | furniture | pages [6] -->
Team # 2003723                                                            Page  6  of  25

<!-- b000108 | caption | pages [6] -->
Figure1.Schema of main triplet

<!-- b000109 | prose | pages [6] -->
We consider Team Formations. There are many modes of complex networks. For football matches, besides passing tactics, the overall arrangement of troops is also very important. As shown in Figure2, we present the results of Team Formations in the form of a schematic plan of the stadium. In Figure 2, players are represented by round nodes, and the position of each player is determined by the average of all passing positions of the player in the match.  The thickness of the arc indicates its weight, which is determined by the number of directional passes through the arc. This diagram covers many factors that are crucial to the match, such as passing the ball and the player's performance.

<!-- b000110 | caption | pages [6] -->
Figure2. Schematic illustration of a football passing network

<!-- b000111 | prose | pages [6] -->
4.1.2 Classical Football Metrics

<!-- b000112 | prose | pages [6] -->
According to the passing network, we can not only get network-related indicators, but also get many indicators to evaluate the game. We found out the values of a series of indexes of husky team and opponents in this match, and presented the results in the form of bar chart. In Figure3, we respectively show the comparison chart of Shots, on Target, Off Target, Possession, Passes, Passes Completed, Passes Completed Rate.

<!-- b000113 | prose | pages [6, 7] -->
关注数学模型 The basic indexes of both sides in the match are clear at a glance.

<!-- b000114 | furniture | pages [6] -->
2

<!-- b000115 | furniture | pages [6] -->
MATHmodels

<!-- b000116 | furniture | pages [6] -->
获取更多资讯

<!-- b000117 | furniture | pages [7] -->
Team # 2003723                                                            Page  7  of  25

<!-- b000119 | caption | pages [7] -->
Figure3.Comparison of 6 Classical Football Metrics

<!-- b000120 | prose | pages [7] -->
4.1.3 Network Properties

<!-- b000121 | prose | pages [7] -->
There are many parameters to describe the complex network. We selected the most authoritative three indicators to describe the structural characteristics of the passing network, and compared the Husky team with its opponents, and presented the results in the form of column chart. The first graph of Figure4 shows the comparison of C (clustering coefficient).Clustering coefficient is an indicator of the local robustness of the network, because when a triangle connecting three players (nodes) exists, it cannot pass the ball between the two players and can reach another node through the other two sides of the triangle. Therefore, in football, the clustering coefficient is used to coordinate the triangular relationship among the three players. When i, j and k represent different player Numbers, the calculation formula is as follows:

<!-- b000122 | prose | pages [7] -->
𝐶𝑖= 𝛴𝑗,𝑘𝜔𝑖𝑗𝑘𝑎𝑖𝑗𝑎𝑖𝑘𝑎𝑗𝑘 𝑘𝑖(𝑘𝑖−1)

<!-- b000123 | prose | pages [7] -->
𝐴𝑖𝑗= (𝑎𝑖𝑗)

<!-- b000124 | prose | pages [7] -->
𝑎𝑖𝑗+ 𝑎𝑗𝑘 1 𝜔𝑖𝑗= (𝑎𝑖) 2 The third graph of Figure4 shows the index of the standard deviation of closeness (𝑋4).The most central units according to closeness centrality can quickly interact to all others because they are close to all others. This measures is preferable to degree centrality, because it does not take into account only indirect connections. When i and j respectively represent different player labels, the calculation formula is as follows:

<!-- b000125 | prose | pages [7] -->
1 𝛴𝑗∈𝑈𝐷(𝑖, 𝑗) 𝐶𝑙𝑜𝑠𝑠𝑛𝑒𝑠𝑠(𝑖) =

<!-- b000126 | prose | pages [7] -->
𝐷(𝑖, 𝑗) = 1 ′ 𝑘𝑖𝑗

<!-- b000127 | prose | pages [7, 8] -->
关注数学模型 𝑋4 = 𝑠𝑡𝑑(𝐶𝑙𝑜𝑠𝑠𝑛𝑒𝑠𝑠(𝑖)) The second graph of Figure4 shows the index of the dispersion of the players （𝑋5）.Figure4 shows the index of the dispersion of the players (𝑋5).  Spatial dispersion of nodes around the network center.  We use the average distance between the player's position and the center of the team network to measure this indicator.

<!-- b000128 | furniture | pages [7] -->
2

<!-- b000129 | furniture | pages [7] -->
MATHmodels

<!-- b000130 | furniture | pages [7] -->
获取更多资讯

<!-- b000131 | furniture | pages [8] -->
Team # 2003723                                                            Page  8  of  25

<!-- b000133 | caption | pages [8] -->
Figure4.Comparison of 3 network parameters

<!-- b000134 | prose | pages [8] -->
4.2 Match Networks summary

<!-- b000135 | prose | pages [8] -->
In the previous section, we described the process of designing a passing model for a game and getting a set of metrics. In this section, we do the same processing analysis for each game and get these indicators separately. Due to the overlapping of content and the limitation of space, we do not show each game one by one, the detailed code and the result table can be seen in the appendix.

<!-- b000136 | prose | pages [8] -->
4.3 Time Dimension Exploration

<!-- b000137 | prose | pages [8] -->
The ball passing network we build is a static network. Further, we explored the changes of three important indicators over time and presented the results in the form of a line graph. Figure5 shows the movement ratio of the vertical distance to the horizontal distance of the center point of the network of the two teams in a game, as well as the variation of the standard deviation close to the centrality over time. Among them, the ratio of the vertical distance to the horizontal distance of the center of the network reflects the style of the team. If the ratio is small, then the vertical movement range of the team is larger than the horizontal range, reflecting its offensive. In addition, the change of its trend can also reflect the change of team strategy. For example, there is a tendency for the ratio to increase, which reflects that the team gradually adopts more offensive strategies over time, etc.

<!-- b000138 | caption | pages [8] -->
Figure5.Two indicators in the time series

<!-- b000139 | prose | pages [8] -->
关注数学模型

<!-- b000140 | furniture | pages [8] -->
2

<!-- b000141 | furniture | pages [8] -->
MATHmodels

<!-- b000142 | furniture | pages [8] -->
获取更多资讯

<!-- b000143 | furniture | pages [9] -->
Team # 2003723                                                            Page  9  of  25

<!-- b000144 | heading | pages [9] -->
5 Teamwork Model

<!-- b000145 | prose | pages [9] -->
Team cooperation embodied in the performance of the passing network will affect the results of the competition, thus affecting team performance. In order to explore the influence of the structure, configuration and dynamics of team work on successful team cooperation, we take individual contributions to the team, Team structure ,Strategic layout as independent variables, the competition results as dependent variables, use the known data to train the multiple logistic regression model, and test, explain and correct the model[8]. We use the method of combining analytic hierarchy process and entropy weight to build the sub-model of individual contributions to the team index. Since the research on passing network belongs to the cross research between network science and football, the indicators of Team structure include two parts: typical football indicators and typical network indicators already reflected in the previous chapter.  Strategic layout indicators include formation and Offensive style, which will be obtained by mining existing data. The indicators of the entire Teamwork Model are shown in Figure6.

<!-- b000146 | caption | pages [9] -->
Figure6.Classification of regression indicators

<!-- b000147 | prose | pages [9, 10] -->
关注数学模型 5.1 Individual contributions sub-model

<!-- b000148 | furniture | pages [9] -->
2

<!-- b000149 | furniture | pages [9] -->
MATHmodels

<!-- b000150 | furniture | pages [9] -->
获取更多资讯

<!-- b000151 | furniture | pages [10] -->
Team # 2003723                                                            Page  10  of  25

<!-- b000153 | prose | pages [10] -->
In a team, how much contribution each member has made to the team and the distribution of individual contributions is one of the effective indicators to measure team performance. In a team, players in different positions have different responsibilities and division of labor. Therefore, it is illogical to evaluate each player's contribution with a unified standard. In this section, we consider that players in different positions will have different effects if they act with the same nature and will form a new scoring standard by combining subjective and objective methods. We combine analytic hierarchy process and entropy weight method to obtain different weights of different positions and action types on the results, form scoring rules, evaluate the contribution of each player, and then we can analyze the contribution distribution of each team player in each match.

<!-- b000154 | prose | pages [10] -->
5.1.1 Input Items of Personal Contribution Sub-model

<!-- b000155 | caption | pages [10] -->
Table2.Event classification

<!-- b000156 | prose | pages [10] -->
5.1.2 Application of AHP in Establishment

<!-- b000157 | prose | pages [10] -->
In this part, we use AHP to form a set of scoring rules. Analytic Hierarchy Process (AHP) are in line with common sense, but there is a subjective problem in index construction.

<!-- b000158 | prose | pages [10] -->
Construction of Hierarchical Structure Model ⚫

<!-- b000159 | prose | pages [10, 11] -->
关注数学模型 Construction of Judgment matrix ⚫

<!-- b000160 | furniture | pages [10] -->
2

<!-- b000161 | furniture | pages [10] -->
MATHmodels

<!-- b000162 | furniture | pages [10] -->
获取更多资讯

<!-- b000163 | furniture | pages [11] -->
Team # 2003723                                                            Page  11  of  25

<!-- b000164 | caption | pages [11] -->
Figure7. Hierarchical structure model

<!-- b000166 | prose | pages [11] -->
First, we construct the judgment matrix according to the rule of experience and normalize it.

<!-- b000167 | prose | pages [11] -->
𝑛 𝐾𝑖𝑗= 𝐾𝑖𝑗÷ ∑𝐾𝑖𝑗 𝑖,𝑗=1 Then we calculate the weight vector according to the normalized judgment matrix and obtain the eigenvalues.

<!-- b000168 | prose | pages [11] -->
Inspection and Evolution ⚫

<!-- b000169 | prose | pages [11] -->
We use the consistency index CR to test, and CR<0.1 is found, so the consistency test is passed.

<!-- b000170 | prose | pages [11] -->
5.1.3 Application of Entropy Weight Method in Establishment

<!-- b000171 | prose | pages [11] -->
The effect of each player's action on the result depends to a large extent on the difference of the same type of action performed by players in the same position. Based on this principle, entropy weight method can objectively evaluate the scoring rules. The entropy weight method comprises the following steps:

<!-- b000172 | prose | pages [11] -->
Construction of matrix ⚫

<!-- b000173 | prose | pages [11] -->
Normalization of Indicators. As indicators are positive indicators, we ⚫

<!-- b000174 | prose | pages [11] -->
homogenize heterogeneous indicators according to the formula.

<!-- b000175 | prose | pages [11] -->
𝑥𝑖𝑗−𝑚𝑖𝑛(𝑥.𝑗) 𝑚𝑎𝑥(𝑥.𝑗) −𝑚𝑖𝑛(𝑥.𝑗) 𝑦𝑖𝑗=

<!-- b000176 | prose | pages [11] -->
Find the information entropy of each variable. For the jth variable, its information entropy:

<!-- b000177 | prose | pages [11, 12] -->
关注数学模型 𝑛 𝐻𝑗= −1 ln 𝑛∑𝑝𝑖𝑗∗ln 𝑝𝑖𝑗 𝑖=1 𝑦𝑖𝑗 𝑝𝑖𝑗= 𝑛 ∑ 𝑦𝑖𝑗 𝑖=1

<!-- b000178 | furniture | pages [11] -->
2

<!-- b000179 | furniture | pages [11] -->
MATHmodels

<!-- b000180 | furniture | pages [11] -->
获取更多资讯

<!-- b000181 | furniture | pages [12] -->
Team # 2003723                                                            Page  12  of  25

<!-- b000183 | prose | pages [12] -->
The calculation of the weight of each indicator ⚫

<!-- b000184 | prose | pages [12] -->
The information entropy of J variables can be calculated above：𝐻1,𝐻2, … ，𝐻𝑗

<!-- b000185 | prose | pages [12] -->
1 −𝐻𝑗 𝑊𝑗= 𝑝 𝑃−∑ 𝐻𝑗 𝑗=1

<!-- b000186 | prose | pages [12] -->
5.1.4 Establishment of Personal Contribution Sub-model

<!-- b000187 | prose | pages [12] -->
We have respectively obtained two different scoring weights. Because they are subjective and objective respectively, we combine them to carry out equal weight average calculation on the weights obtained by the two methods.

<!-- b000188 | caption | pages [12] -->
Table3.Three methods of scoring weight table

<!-- b000189 | caption | pages [12] -->
Table3 presents the weights calculated in three ways. We count n the number of

<!-- b000190 | prose | pages [12, 13] -->
关注数学模型 actions taken by players at four positions in each match, and calculate the score s of each position player according to the weight w calculated by combining subjective and objective factors.

<!-- b000191 | furniture | pages [12] -->
2

<!-- b000192 | furniture | pages [12] -->
MATHmodels

<!-- b000193 | furniture | pages [12] -->
获取更多资讯

<!-- b000194 | furniture | pages [13] -->
Team # 2003723                                                            Page  13  of  25

<!-- b000196 | prose | pages [13] -->
4 ∗𝑁𝑖, ∀𝑖= 1,2,3,4 𝑠𝑖= ∑𝑤𝑖𝑗 𝑗=1

<!-- b000197 | prose | pages [13] -->
5.1.5 Variables Constructed by Combining Individual Contributions

<!-- b000198 | prose | pages [13] -->
We include the mean and standard deviation of players' scores in the variables of the regression model. The average score of a player represents the overall contribution level of a team member, and the standard deviation of a player's score represents the distribution of a team member's contribution level. These two indicators explain the general level and difference of individual performance in the team and reflect the influence of team members.

<!-- b000199 | prose | pages [13] -->
5.2 Construction of Team’s Network Structure and Strategic Layout Index

<!-- b000200 | prose | pages [13] -->
5.2.1 Team’s Network Structure Index

<!-- b000201 | prose | pages [13] -->
In football matches, the frequent interaction between players makes the whole team like a network structure, closely linked. Combined with the passing network we have built, we supplement and screen the important indicators analyzed in the previous chapter.  We will determine this kind of index from two aspects.  We have selected several most representative indexes on the two aspects of Classical Football Metrics and network quality indexes by consulting literature and other methods.  A detailed explanation of these indicators will be described below.

<!-- b000202 | prose | pages [13] -->
Typical football indicators ⚫ We chose the more commonly used "the classical football metrics", including ball playing rate, pass completion and goal attempt.

<!-- b000203 | prose | pages [13] -->
The ball playing rate is one of the data used to test who controls the initiative and rhythm of a match. Generally, the higher the ball playing rate of a team, the better the team's mastery of the match.pass completion is used to detect the interaction efficiency between players. Generally speaking, the higher the pass completion of a team, the better the coordination and cooperation between players of the team.Goal attempts are one of the commonly used indexes in football matches, which can reflect the attacking rhythm of the team.Therefore, we include ball playing rate, pass completion and goal attempt into the variables of the regression model.

<!-- b000204 | prose | pages [13] -->
Typical network indicators ⚫ After analysis, we selected clustering coefficient, shortest-path length, dispersion of players, std of the players' centrality. These indicators reflect the process information at the team level, and were obtained in the previous chapter. We incorporated them into the variables of the regression model. The clustering coefficient measures the flow of the network. The shortest path length reflects the flexibility of the team. The dispersion of players describes the average distance between the players' average position and the team centroid. The sd of closeness

<!-- b000205 | prose | pages [13, 14] -->
关注数学模型 reflects the adaptability of the team.

<!-- b000206 | furniture | pages [13] -->
2

<!-- b000207 | furniture | pages [13] -->
MATHmodels

<!-- b000208 | furniture | pages [13] -->
获取更多资讯

<!-- b000209 | furniture | pages [14] -->
Team # 2003723                                                            Page  14  of  25

<!-- b000211 | heading | pages [14] -->
5.2.2 Team's Strategic Layout Index

<!-- b000212 | prose | pages [14] -->
Formation ⚫

<!-- b000213 | prose | pages [14] -->
Football formation refers to the arrangement of team members' positions and division of responsibilities on the field. The common formations are 4-3-3, 4-4-2, etc. We divide the formation into three types: offensive, defensive and court balance. According to these three types of formations, classification variables are constructed and included in the independent variables of the regression model.

<!-- b000214 | caption | pages [14] -->
Table4.Formation classification

<!-- b000215 | prose | pages [14] -->
Offensive style ⚫

<!-- b000216 | prose | pages [14] -->
Different teams have different offensive style, and even the same team will try different offensive styles in different matches. Sometimes the team attacks from the left side, the right side and other flanks, which is conducive to the development of offensive speed. Sometimes the team will choose to attack in the middle, this tactic is convenient to shoot directly, but shooting is difficult. We divided the attack style into three types: left attack, right attack and middle attack. According to the most attack style used in the whole match, the attack style was taken as the evaluation standard of the team and included in the independent variables of the regression model.

<!-- b000217 | heading | pages [14] -->
5.3 Regression Model

<!-- b000218 | prose | pages [14] -->
We use the results of the competition as dependent variables and the above-mentioned individual contributions to the team, Team structure and Strategic layout variables, as well as the environment variables as supporting variables as independent variables, to establish a logical regression model. Environmental variables include coaches, opponents and home and away games. These variables are known and reflect the most basic situation of the competition. The structure of this logistic regression model is as follows. 𝑂𝑢𝑡𝑐𝑜𝑚𝑒= 𝐶1 ∗𝑋1 + 𝐶2 ∗𝑃𝑐𝑡+ 𝐶3 ∗𝑋2 + 𝐶4 ∗𝑋3 + 𝐶5 ∗𝑋4 + 𝐶6 ∗𝑋5 + 𝐶7 ∗𝑆1 + 𝐶8 ∗𝑆2 + 𝐶9 ∗𝐿1 + 𝐶10 ∗𝐿2 + 𝐶11 ∗𝐸1 + 𝐶12 ∗𝐸2 + 𝐶13 ∗𝐸3 + 𝐶

<!-- b000219 | heading | pages [14] -->
5.4 Multicollinearity Analysis

<!-- b000220 | prose | pages [14] -->
Due to the small amount of data, there is a great possibility of multicollinearity. Therefore, we use VIF (Variance Inflation Factor) to test multi-collinearity 1 .𝑉𝐼𝐹= 1−𝑅2

<!-- b000221 | prose | pages [14, 15] -->
关注数学模型 It can be seen from the table that the model has serious multicollinearity. So we use VIF test and stepwise regression to establish a logical regression model.

<!-- b000222 | furniture | pages [14] -->
2

<!-- b000223 | furniture | pages [14] -->
MATHmodels

<!-- b000224 | furniture | pages [14] -->
获取更多资讯

<!-- b000225 | furniture | pages [15] -->
Team # 2003723                                                            Page  15  of  25

<!-- b000226 | caption | pages [15] -->
Table5.Multicollinearity checklist

<!-- b000228 | prose | pages [15] -->
5.5 Results and tests

<!-- b000229 | prose | pages [15] -->
In this part, we will obtain the equation of logical regression according to the above stepwise regression method, and carry out significance test and robustness test on the results to further analyze the results.

<!-- b000230 | prose | pages [15] -->
5.5.1 Results Display and Inspection

<!-- b000231 | prose | pages [15] -->
After we corrected multi-collinearity, the results are shown in Table6.

<!-- b000232 | caption | pages [15] -->
Table6.Logistic regression results

<!-- b000233 | prose | pages [15] -->
From the results, it can be seen that the overall fitting effect of the model is better, whose R2 is close to 1 and has a significant p-value. Most of the variables are

<!-- b000234 | prose | pages [15, 16] -->
关注数学模型 significant, while there are still some under the significance level of 0.1, including the shooting times, clustering coefficient, dispersion of players and formation did not pass the significance test.

<!-- b000235 | furniture | pages [15] -->
2

<!-- b000236 | furniture | pages [15] -->
MATHmodels

<!-- b000237 | furniture | pages [15] -->
获取更多资讯

<!-- b000238 | furniture | pages [16] -->
Team # 2003723                                                            Page  16  of  25

<!-- b000240 | prose | pages [16] -->
We will expand the offensive style from three categories to five categories, and subdivide it according to the fineness of position coordinates. It can be seen that the results of the upper and lower regression have passed the significance test. In other words, the logistic regression model is robust.

<!-- b000241 | prose | pages [16] -->
5.5.2 Heterogeneity analysis

<!-- b000242 | prose | pages [16] -->
As the opponent's formation may affect the selection and change of the team's formation, we use the method of grouping and returning. On the basis of opponents of different formations, the whole data set is divided into 3 types (offensive, defensive, court balanced) of smaller data sets, and regression is made respectively. The results of heterogeneous regression are displayed by matrix. Taking our offensive strategy as the control group, the following conclusions are obtained.

<!-- b000243 | prose | pages [16] -->
When the opponent mainly uses offensive formation, our formation has no ⚫ significant influence on the result of the match.

<!-- b000244 | prose | pages [16] -->
When the opponent mainly uses the offensive and defensive balanced formation, ⚫ if we choose the offensive and defensive balanced formation, it has no significant influence on the result of the match. If the defensive type is selected, the probability of winning the competition is 19% of the offensive type.

<!-- b000245 | prose | pages [16] -->
When the opponent mainly uses a balanced offensive and defensive formation, if ⚫ we choose a defensive formation, it has no significant influence on the result of the match. If you choose the court balance type, the probability of winning the competition is 4 times that of adopting the offensive strategy.

<!-- b000246 | caption | pages [16] -->
Table7.Logistic regression results

<!-- b000247 | prose | pages [16] -->
5.5.3 Interpretation of Result

<!-- b000248 | prose | pages [16] -->
Through the above analysis, we have the following variables that affect the team's performance:

<!-- b000249 | prose | pages [16] -->
The standard deviation of scoring has a positive effect on the result of the ⚫ competition. Scoring refers to the standard deviation of scoring the players in the team according to the scoring sub-model constructed above, which reflects the distribution of the contributions of the players in the team. In other words, the more dispersed the contribution distribution of the team members, the better the performance of the team under the same other conditions. Therefore, the success of

<!-- b000250 | prose | pages [16, 17] -->
关注数学模型 team cooperation tends to be heterogeneous in composition.

<!-- b000251 | furniture | pages [16] -->
2

<!-- b000252 | furniture | pages [16] -->
MATHmodels

<!-- b000253 | furniture | pages [16] -->
获取更多资讯

<!-- b000254 | furniture | pages [17] -->
Team # 2003723                                                            Page  17  of  25

<!-- b000256 | prose | pages [17] -->
The success rate of passing the ball has a positive effect on the result of the ⚫ match.

<!-- b000257 | prose | pages [17] -->
The possession rate has a negative influence on the result of the match. Under ⚫ normal circumstances, the possession rate represents the initiative of a team, which is often proud of its high possession rate. However, the analysis results show that high ball possession rate may reflect reasons such as slow pace, which is not conducive to the results of the competition.

<!-- b000258 | prose | pages [17] -->
The standard deviation near the center has a negative influence on the result ⚫ of the competition. Thus, we can see that the success of team cooperation tends to the combination with smaller differences in communication times between team members.

<!-- b000259 | prose | pages [17] -->
Home and away games have a significant impact on the competition results. ⚫ Home court advantage will have a positive impact on the competition.

<!-- b000260 | prose | pages [17] -->
Offensive style has a significant influence on the result of the competition. ⚫ The formation is influenced by the opponent's strategy on the result of the ⚫ match.In addition, we used the model to predict the results of the competition. Of the 76 data, only 3 were predicted incorrectly, with an accuracy of 96.1%, which also proves the validity of the model.

<!-- b000261 | heading | pages [17] -->
6 Structural Strategy Analysis and Suggestions

<!-- b000262 | prose | pages [17] -->
In the existing analysis, we have constructed the network attributes and team cooperation indicators in the network model. In this part, we will analyze the above indicators again to design a more effective structural strategy for the Huskies team and propose suggestions to its coaches for improvement next season.

<!-- b000263 | prose | pages [17] -->
6.1 Results of Team Performance Model of Huskies Team

<!-- b000264 | prose | pages [17] -->
In order to judge the influence of each index and network attribute on the outcome of the match, we take the above indexes as independent variables and the outcome of the match as dependent variables, and carry out two logistic regression analyses according to the different formations and offensive styles.

<!-- b000265 | caption | pages [17] -->
Table8.Heterogeneous regression results of Huskies

<!-- b000266 | prose | pages [17, 18] -->
关注数学模型 In this regression, we also used the test of multicollinearity, and the results are shown in Table8 after removing the variables with greater influence.

<!-- b000267 | furniture | pages [17] -->
2

<!-- b000268 | furniture | pages [17] -->
MATHmodels

<!-- b000269 | furniture | pages [17] -->
获取更多资讯

<!-- b000270 | furniture | pages [18] -->
Team # 2003723                                                            Page  18  of  25

<!-- b000272 | prose | pages [18] -->
6.2 Suggestions Based on Data Analysis Results

<!-- b000273 | prose | pages [18] -->
6.2.1 Suggestions Based on Structural Strategies

<!-- b000274 | prose | pages [18] -->
Choosing an effective structural strategy means choosing a match formation that can make the performance indicators and team processes that reflect successful team cooperation have a more positive impact on the result of the match.

<!-- b000275 | prose | pages [18] -->
Choose the defensive formation of 4-5-1 or 5-4-1 formation ⚫

<!-- b000276 | prose | pages [18] -->
First of all, considering the influence of team formation and observing the regression results in Table8, we can find that the indexes such as ball playing rate, the std of the closeness, shortest path, dispersion and formation have significant influence on the outcome of the match. The regression results show that the defensive formation (4-5-1, 5-4-1) has a significant impact on the result of the draw, while others have no significant impact.

<!-- b000277 | prose | pages [18] -->
At the same time, according to our analysis, Huskies team has won 13 games, lost 15 games, scored 44 goals and conceded 58 goals in this season, belonging to the lower and middle level team. Therefore, we suggest that for teams of this level, defensive counterattack is an effective way to obtain competition results. Thus, 4-5-1 and 5-4-1,which are mainly defensive counterattack, can be used to strengthen the middle and back court ability. The significance of defensive formation coefficient also confirms this view.

<!-- b000278 | prose | pages [18] -->
Adhere to the right-wing offensive style ⚫

<!-- b000279 | prose | pages [18] -->
Secondly, when considering the influence of offensive style, we focus on the variable of offensive style in the regression results of figure 2. We can find that the right attack has a significant impact on the victory of the competition, and the larger the proportion of right attack, the better the victory of the competition.

<!-- b000280 | prose | pages [18] -->
Based on the above analysis, we suggest that when coaching a team of Huskie's level, the coach should mainly use a balanced attack-defense formation to strengthen the middle and back court ability, carry out defensive counter-attacks, and at the same time, carry out more threatening right-wing attacks.

<!-- b000281 | prose | pages [18] -->
6.2.2 Suggestions Based on Network Analysis

<!-- b000282 | prose | pages [18] -->
Different network attribute values reflect different behaviors of the team. By improving the behavior level represented by significant network attributes, team performance can be effectively improved.

<!-- b000283 | prose | pages [18] -->
Logistic regression results in Table9 show that, the regression coefficients of the shortest path, the std of the closeness and dispersion in the network attribute are significant, which respectively represent the flexibility of team passing, whether the number of players passing is average, and attack rhythm. The symbols corresponding to the regression coefficients are negative, negative and positive respectively. The

<!-- b000284 | prose | pages [18, 19] -->
关注数学模型 clustering coefficient is not significant, which represents the attack rhythm of the team.

<!-- b000285 | furniture | pages [18] -->
2

<!-- b000286 | furniture | pages [18] -->
MATHmodels

<!-- b000287 | furniture | pages [18] -->
获取更多资讯

<!-- b000288 | furniture | pages [19] -->
Team # 2003723                                                            Page  19  of  25

<!-- b000290 | prose | pages [19] -->
Therefore, in order to achieve the ideal competition results, we should strive to reduce the minimum distance and center deviation, and improve the dispersion degree of the players, while the clustering coefficient does not need too much attention.

<!-- b000291 | caption | pages [19] -->
Table 9.Comparison Diagram of Huskies and Others

<!-- b000292 | prose | pages [19] -->
Then we compared the average value of the Huskies team with the average level of the opponents (as shown in Table9), and put forward the following suggestions:

<!-- b000293 | prose | pages [19] -->
Maintain and expand advantages in passing flexibility ⚫

<!-- b000294 | prose | pages [19] -->
The Huskies team's minimum distance is lower than the average, indicating that the passing flexibility is higher than the average, which is beneficial. It is necessary to exert its advantages.

<!-- b000295 | prose | pages [19] -->
Pay attention to the level balance of players ⚫ The number of passes received by different players varies greatly, and the positions of players vary greatly. Coaches should pay attention to the balance between players. Different players should be treated roughly equally to get higher scores.

<!-- b000296 | prose | pages [19] -->
Strengthen the player's sense of movement ⚫ The scatter of Huskies players is lower than the average level, and their movements are too concentrated. According to the above results, teams with scattered positions are more likely to win the match. Therefore, spreading their positions as far as possible can they control the whole match.

<!-- b000297 | heading | pages [19] -->
7 Extension of the model

<!-- b000298 | heading | pages [19] -->
7.1 Sorting out the Existing Conclusions

<!-- b000299 | prose | pages [19] -->
Under the controllable environment of football matches, we have established a model with strong pertinence. According to the index considered in the model, we will extend it to the common team cooperation. The expansion of our conclusion is as follows.

<!-- b000300 | prose | pages [19] -->
7.1.1 Individual Contributions to the Team

<!-- b000301 | prose | pages [19] -->
Different positions of players have different scoring systems, which can be ⚫ extended to different treatment of performance appraisal. Different criteria are adopted to judge people with different division of labor in the team, which is

<!-- b000302 | prose | pages [19, 20] -->
关注数学模型 conducive to the formation of a more effective team.

<!-- b000303 | furniture | pages [19] -->
2

<!-- b000304 | furniture | pages [19] -->
MATHmodels

<!-- b000305 | furniture | pages [19] -->
获取更多资讯

<!-- b000306 | furniture | pages [20] -->
Team # 2003723                                                            Page  20  of  25

<!-- b000308 | prose | pages [20] -->
The sd of the grades can be extended to the difference of individual ⚫ contributions. The contribution of everyone in the team tends to be heterogeneous, which is conducive to the formation of a more effective team.

<!-- b000309 | prose | pages [20] -->
7.1.2 Team Structure

<!-- b000310 | prose | pages [20] -->
The standard deviation of Closeness can be extended to the coverage of ⚫ communication in a team. The team should not have a number of key figures to shift the center of the network. As far as possible, the transmission of information can cover every member evenly, which is conducive to the formation of a more effective team.

<!-- b000311 | prose | pages [20] -->
Clustering coefficient can be extended to the frequency of communication ⚫ among team members. Members of the team should not communicate as often as possible. They should pay attention to the efficiency of communication.

<!-- b000312 | prose | pages [20] -->
Shortest path can be extended to the hierarchical mode. The more complex ⚫ the hierarchical structure of the team organization, the more the shortest path will be added, while the flattening mode will have the smaller shortest path. The size of the shortest path has no significant effect on team performance, therefore, for the hierarchical model, the appropriate one is the best.

<!-- b000313 | prose | pages [20] -->
Pass completion can be extended to the effectiveness of communication. ⚫ Effective communication is conducive to the formation of more effective teams.

<!-- b000314 | prose | pages [20] -->
7.1.3 Strategic Layout

<!-- b000315 | prose | pages [20] -->
Formation can be extended to team strategy. The formation of the team is ⚫ closely related to its opponents. Therefore, when the team determines its own strategy, it is helpful to form a more effective team by carefully analyzing the environment, trends and other people's strategies.

<!-- b000316 | prose | pages [20] -->
Offensive style can be extended to team work style. Team style is very ⚫ important, but it is hard to say which style is good or bad. Choosing the right style is conducive to the formation of a more effective team.

<!-- b000317 | prose | pages [20] -->
7.1.4 Environment Variables

<!-- b000318 | prose | pages [20] -->
In the process of influencing team performance, many objective factors will be encountered, such as unpredictable competitors, uncontrollable emergencies, and the influence of macro background. Since the number of objective factors is difficult to measure reliably in uncontrollable environments, it will not be repeated here.

<!-- b000319 | prose | pages [20] -->
7.1.5 Summary

<!-- b000320 | prose | pages [20] -->
The model of controllable system is also of appropriate guiding significance to a wider group, and the specific operation needs to quantify the index according to its actual situation so as to solve the problem more efficiently.

<!-- b000321 | prose | pages [20] -->
7.2 Dimension Extension

<!-- b000322 | prose | pages [20] -->
A team is often much more complicated than a football team simplified by

<!-- b000323 | prose | pages [20, 21] -->
关注数学模型 models. In the cooperation model we established for the team, we only considered the positions and actions of the players, the interaction between the players, and the arrangement of troops, but also lacked the dimensions of leadership and team culture. Players also have gender, personality, stability and other factors that have not been considered.

<!-- b000324 | furniture | pages [20] -->
2

<!-- b000325 | furniture | pages [20] -->
MATHmodels

<!-- b000326 | furniture | pages [20] -->
获取更多资讯

<!-- b000327 | furniture | pages [21] -->
Team # 2003723                                                            Page  21  of  25

<!-- b000329 | heading | pages [21] -->
7.2.1 Dimensions of Leadership

<!-- b000330 | prose | pages [21] -->
Lena Zander and Christina L. Butler focus on leadership modes and multicultural team composition and argue that leadership modes should be an informed strategic choice[9]. Therefore, it is very necessary to obtain the internal centrality of leaders in SNA (Social Network Analysis) and the frequency of information exchange with subordinates when developing common models. The former can be obtained through the nature of networks, while the latter can be obtained through the number of contacts.

<!-- b000331 | prose | pages [21] -->
7.2.2 Dimensions of Gender

<!-- b000332 | prose | pages [21] -->
More and more studies show that women's ability in leadership or their role in the board of directors is not inferior to that of men. According to the research of Brian M. Doornenbal, Liselore A. Havermans. (2015), when gender diversity is promoted, it can have a positive impact on team performance[10]. When developing a common model, we can include the proportion of gender.

<!-- b000333 | prose | pages [21] -->
7.2.3 Dimensions of Team Culture

<!-- b000334 | prose | pages [21] -->
Team culture can not only improve team cohesion, but also improve team efficiency and team performance by relieving member pressure.Samia Jamshed and Nauman Majeed found that team culture can significantly increase team performance through lens of knowledge sharing and team emotional intelligence[11]. At the same time，when developing a common model, you can also include the existence of enterprise Logo, slogan, etc.

<!-- b000335 | heading | pages [21] -->
8 Strengths and Weaknesses

<!-- b000336 | prose | pages [21] -->
8.1 Strengths

<!-- b000337 | prose | pages [21] -->
Based on the controllable environment of football matches, we have set up as ⚫ comprehensive a dimension as possible for all measurable data and constructed professional variables, such as ball possession rate, which improves the information purity of the data. It is worth mentioning that the four dimensions we have constructed are consistent with the current research by scholars.

<!-- b000338 | prose | pages [21] -->
The model results are accurate. First of all, when evaluating the score of ⚫ individual behavior, we adopt a subjective and objective method. In addition, we conducted multicollinearity and robustness processing, and the prediction accuracy of the competition results exceeded 95%.

<!-- b000339 | prose | pages [21] -->
The method of network analysis is used. In the past studies, information such as ⚫ passing the ball and the position of the players were seldom considered, while the

<!-- b000340 | prose | pages [21, 22] -->
关注数学模型 passing network between us was constructed and analyzed, and the characteristic indexes of the network were incorporated into the consideration scope of the model, which has popularization significance.

<!-- b000341 | furniture | pages [21] -->
2

<!-- b000342 | furniture | pages [21] -->
MATHmodels

<!-- b000343 | furniture | pages [21] -->
获取更多资讯

<!-- b000344 | furniture | pages [22] -->
Team # 2003723                                                            Page  22  of  25

<!-- b000346 | prose | pages [22] -->
8.2 Weaknesses

<!-- b000347 | prose | pages [22] -->
The sample size is small. According to the use conditions of the model, the ⚫ amount of data is preferably more than 10 times of the construction index. However, due to the limited data available in this paper, the results may be unstable, which needs further consideration after collecting more reliable data.

<!-- b000348 | prose | pages [22] -->
The transactional analysis between the two players is relatively simple. In the ⚫ analysis of network construction and so on, because it is difficult to quantify the instantaneous positions of both parties and we have not considered the obstacles of our opponents, we will analyze after obtaining more accurate GPS data.

<!-- b000349 | heading | pages [22] -->
9 Conclusion

<!-- b000350 | prose | pages [22] -->
Team cooperation is an important factor in understanding the complexity of football matches. With the arrival of the big data era, the acquisition of massive competition data provides the necessary data basis for quantitative analysis of team relationships and tactical strategies. This study is based on the microscopic data of husky team matches, and from the perspective of network science, it shows that establishing an effective team model is an effective way to improve team performance, thus providing quantifiable evaluation tools for team leaders.

<!-- b000351 | prose | pages [22] -->
This paper uses social network analysis to study the passing characteristics of football matches. Firstly, the network types and characteristics are identified by constructing a directed weighted graph network model. On this basis, combined with individual contributions to the team, Team structure, Strategic layout, and Environment variables, a comprehensive index system to comprehensively measure cooperation performance is constructed and evaluated. Based on this index system, this paper studies the effect mechanism of cooperation performance and other factors on team victory. Finally, according to Husky's network structure and relevant research conclusions, some suggestions are put forward to help football teams and other teams improve team performance.

<!-- b000352 | prose | pages [22] -->
The advantages of this study lie in choosing models and indicators from a new perspective and in combination with the characteristics of team cooperation of football teams. The analysis level is clear, the results are stable, and the conclusions and suggestions are practical. At the same time, there are still some unsolved problems in this paper, such as limitations in the process of selecting indicators, difficulty in quantifying the instantaneous positions of teammates and inability to obtain the obstruction degree of opponents, etc. All of these require in-depth research on the basis of expanding the number of indicators and sample size.

<!-- b000353 | prose | pages [22] -->
关注数学模型

<!-- b000354 | furniture | pages [22] -->
2

<!-- b000355 | furniture | pages [22] -->
MATHmodels

<!-- b000356 | furniture | pages [22] -->
获取更多资讯

<!-- b000357 | furniture | pages [23] -->
Team # 2003723                                                            Page  23  of  25

<!-- b000358 | heading | pages [23] -->
Reference

<!-- b000359 | references | pages [23] -->
[1] Duch J., Waitzman J.S., Amaral L.A.N. (2010). Quantifying the performance of

<!-- b000360 | references | pages [23] -->
individualplayers in a team activity. PLoS ONE, 5: e10937.

<!-- b000361 | references | pages [23] -->
[2]Fan Bu, Sonia Xu, Katherine Heller, Alexander Volfovsky(2018). SMOGS: Social

<!-- b000362 | references | pages [23] -->
Network Metrics of Game SuccessPMLR 2019 89:2406-2414

<!-- b000363 | references | pages [23] -->
[3] Buldú, J.M., Busquets, J., Echegoyen, I. et al. (2019). Defining a historic football

<!-- b000364 | furniture | pages [23] -->
team: UsingNetwork Science to analyze Guardiola’s F.C. Barcelona. Sci Rep, 9,

<!-- b000365 | references | pages [23] -->
13602.

<!-- b000366 | references | pages [23] -->
[4] Victor Martins Maimone, Taha Yasseri (2019)Football is becoming boring;

<!-- b000367 | references | pages [23] -->
Network analysis of 88 thousands matches in 11 major leaguesPhysics and Society

<!-- b000368 | references | pages [23] -->
physics.soc-pharXiv:1908.08991 [physics.soc-ph]

<!-- b000369 | references | pages [23] -->
[5] Ramos, J., Lopes, R. J. & Araújo, D. What’s Next in Complex Networks?

<!-- b000370 | references | pages [23] -->
Capturing the Concept of Attacking Play in Invasive Team Sports. Sports Med. 48,

<!-- b000371 | references | pages [23] -->
17–28 (2018).

<!-- b000372 | references | pages [23] -->
[6] GÜRSAKAL, N., YILMAZ, F., ÇOBANOĞLU, H., ÇAĞLIYOR, S. (2018).

<!-- b000373 | references | pages [23] -->
Network Motifs in Football. Turkish Journal of Sport and Exercise, 20 (3), 263-272.

<!-- b000374 | references | pages [23] -->
[7] The analytic hierarchy process applied to maintenance strategy selection[J] . M

<!-- b000375 | references | pages [23] -->
Bevilacqua, M Braglia.  Reliability Engineering and System Safety . 2000 (1)

<!-- b000376 | references | pages [23] -->
[8]Huang

<!-- b000377 | references | pages [23] -->
Cheng,Lv

<!-- b000378 | references | pages [23] -->
Xiong-Wen,Xu

<!-- b000379 | references | pages [23] -->
Tao,Ni

<!-- b000380 | references | pages [23] -->
Ming-Ming,Xia

<!-- b000381 | references | pages [23] -->
Jia-Lu,Cai

<!-- b000382 | references | pages [23] -->
Shuang-Peng,Zhou Qun,Li Xing,Yang Yang,Zhang Lei,Yao Hong-Wei,Meng

<!-- b000383 | references | pages [23] -->
Xiao-Ming,Wang Hua,Li Jun. Alcohol use in Hefei in relation to alcoholic liver

<!-- b000384 | references | pages [23] -->
disease: A multivariate logistic regression analysis.[J]. Alcohol (Fayetteville,

<!-- b000385 | references | pages [23] -->
N.Y.),2018,71

<!-- b000386 | references | pages [23] -->
[9] Lena Zander,Christina L. Butler. Leadership modes: Success strategies for

<!-- b000387 | references | pages [23] -->
multicultural teams[J]. Scandinavian Journal of Management,2010,26(3)

<!-- b000388 | references | pages [23] -->
[10]Brian M. Doornenbal,Liselore A. Havermans. Gender Diversity and Team

<!-- b000389 | references | pages [23] -->
Identification[J]. Procedia - Social and Behavioral Sciences,2015,194.

<!-- b000390 | references | pages [23] -->
[11]Samia Jamshed,Nauman Majeed. Relationship between team culture and team

<!-- b000391 | references | pages [23] -->
performance through lens of knowledge sharing and team emotional intelligence[J].

<!-- b000392 | references | pages [23] -->
Journal of Knowledge Management,2019,23(1).

<!-- b000393 | references | pages [23] -->
关注数学模型

<!-- b000394 | furniture | pages [23] -->
2

<!-- b000395 | furniture | pages [23] -->
MATHmodels

<!-- b000396 | furniture | pages [23] -->
获取更多资讯

<!-- b000397 | furniture | pages [24] -->
Team # 2003723                                                            Page  24  of  25

<!-- b000398 | heading | pages [24] -->
Appendix

<!-- b000399 | prose | pages [24] -->
Match networks summary

<!-- b000400 | prose | pages [24] -->
⚫ Code

<!-- b000401 | prose | pages [24] -->
1 Network analysis by R rm(list = ls()) library(readxl) inside <- read_excel("C:/Users/Administrator/Desktop/inside.xlsx") View(inside) library('igraph') network <- graph_from_data_frame(d = inside,directed = T) motif = graph.motifs(network,size = 3) motif ga = closeness(network,mode="in") sd(ga) transitivity(network) shortest.paths(network)

<!-- b000402 | prose | pages [24] -->
2 Weight calculation by Matlab

<!-- b000403 | prose | pages [24, 25] -->
关注数学模型 2.1 Entropy weight method [m,n] = size(data); a1 = zeros(m,n); for i = 1:n a1(:,i) = (data(:,i)-min(data(:,i)))/(max(data(:,i))-min(data(:,i))); end ex=sum(a1); a2=zeros(m,n); for i=1:m for j=1:n a2(i,j)=a1(i,j)/ex(j); end end a3=a2.*log(a2); a4=a3; a4(find(isnan(a4)==1)) = 0; ex=sum(a4); ex1=-1/log(m)*ex; weightAHP=(1-ex1)/(n-sum(ex1));

<!-- b000404 | furniture | pages [24] -->
2

<!-- b000405 | furniture | pages [24] -->
MATHmodels

<!-- b000406 | furniture | pages [24] -->
获取更多资讯

<!-- b000407 | furniture | pages [25] -->
Team # 2003723                                                            Page  25  of  25

<!-- b000409 | prose | pages [25] -->
2.2 AHP [m,n]=size(A); [V,D]=eig(A); tempNum1=D(1,1); pos=1; for h=1:n if D(h,h)>tempNum1 tempNum1=D(h,h); pos=h; end end w=abs(V(:,pos)); w=w/sum(w); t=D(pos,pos); CI=(t-n)/(n-1); RI=a; CR=CI/RI(n); if CR<0.10 disp('Succee to pass'); disp('CI=');disp(CI); disp('CR=');disp(CR); else disp('Fail to pass'); end

<!-- b000410 | prose | pages [25] -->
关注数学模型

<!-- b000411 | furniture | pages [25] -->
2

<!-- b000412 | furniture | pages [25] -->
MATHmodels

<!-- b000413 | furniture | pages [25] -->
获取更多资讯
