# P-D-2020-2006782-8d6d48b4

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
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
2006782

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Teaming Wisdom Coming from Soccer Field

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | prose | pages [1] -->
Nowadays teamwork is playing an increasingly important role in all walks of life, especially team sports. Team success is much more than the sum of the abilities of individual players. Rather, it is based on many other factors that involve how well the teammates play together. The purpose of this paper is to create a model that captures performance indicators that reﬂect successful teamwork, and generalize the model to other domains.

<!-- b000011 | prose | pages [1] -->
In TASK 1, we establish a ball passing network based on the passing events, in which each player is a node and each pass constitutes a link between players. We deﬁne several indicators helping us know about the network on the whole. Then we utilize K-means Algorithm to classify dyadic and triadic conﬁgurations in the network, which help to identify the network patterns. Moreover, we explore the network with other scales like time and region to further study the network.

<!-- b000012 | prose | pages [1] -->
In TASK 2, we ﬁrst identify performance indicators that reﬂect successful team- work, such as coordination, distribution, tempo, ﬂexibility and pressing. Then an Eval- uation model based on Adversarial Regression is built to score the teamwork performance of both our team and opponent in one match. To make scores of both teams satisfy the ﬁnal result of each game, we regulate the weights of ﬁve indicators, and record every possible solution. Furthermore, we choose the weight with LowestError as the regression equation. Finally, we notice that only by adjusting the strategy based on the opponents’ strategy, trying to make the total score higher or repress the score of opponents, can the Huskies more likely to win.

<!-- b000013 | prose | pages [1] -->
In TASK 3, we analyze the formations and strategies Huskies adopt, along with the indicators and ﬁnal results. Considering the actual situation of the Huskies, the most effective strategy is Defensive counterattack. Then comparing Huskies with Typical representative of this strategy (Italy National Team), we get to know that the huge gap with the strong teams is mainly reﬂected in Coordination, Flexibility and Pressing. Based on the conclusion we draw, we offer the coach some advice on ﬂexible formation, core players and coherence that help them succeed in the next season.

<!-- b000014 | prose | pages [1] -->
In TASK 4, we generalize our model to more teamwork, not limited to team sports. With reference to the indicators we identify for football match, we come up with the complex set of factors that make some groups perform better. In addition, other aspects of teamwork are taken into account to organize more effective teams.

<!-- b000015 | prose | pages [1] -->
Finally, we conduct a sensitivity analysis in order to gain some deep understanding of our model, and verify the robustness of the model in many cases. Additionally, we analyze the strengths and weaknesses of our model.

<!-- b000016 | keywords | pages [1] -->
Keywords: Passing network, Adversarial Regression, Defensive Counterattack

<!-- b000017 | prose | pages [1] -->
关注数学模型

<!-- b000018 | furniture | pages [1] -->
2

<!-- b000019 | furniture | pages [1] -->
MATHmodels

<!-- b000020 | furniture | pages [1] -->
获取更多资讯

<!-- b000021 | heading | pages [2] -->
Contents

<!-- b000022 | contents | pages [2] -->
1

<!-- b000023 | heading | pages [2] -->
Introduction

<!-- b000024 | prose | pages [2] -->
1 Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 1 Our work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2

<!-- b000025 | prose | pages [2] -->
2

<!-- b000026 | heading | pages [2] -->
Preparation of the Models

<!-- b000027 | prose | pages [2] -->
1

<!-- b000028 | prose | pages [2] -->
1 Assumptions and Justiﬁcations . . . . . . . . . . . . . . . . . . . . . . . . 2.1 1 Notations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2

<!-- b000029 | prose | pages [2] -->
3

<!-- b000030 | heading | pages [2] -->
TASK 1: Ball Passing Network Model

<!-- b000031 | prose | pages [2] -->
2

<!-- b000032 | prose | pages [2] -->
2 Construction of Ball Passing Network . . . . . . . . . . . . . . . . . . . . 3.1 2 . . . . . . . . . . . . . . . . . . . . . . . . . 3.1.1 Ball Passing Network 2 Determination of Network Parameter . . . . . . . . . . . . . . . . 3.1.2 3 Identiﬁcation of Network Patterns . . . . . . . . . . . . . . . . . . . . . . 3.2 5 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2.1 Team Formation 5 Dyadic and Triadic Conﬁgurations . . . . . . . . . . . . . . . . . . 3.2.2 5 Other Structural Indicators . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.3 6 Time Scale . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.3.1 6 Region Scale . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.3.2 8

<!-- b000033 | prose | pages [2] -->
TASK 2: Evaluation of Successful Teamwork 4 9 Identiﬁcation of Performance Indicators . . . . . . . . . . . . . . . . . . . 4.1 9 Static Layer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1.1 9 Dynamic Layer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1.2 9 Evaluation model based on Adversarial Regression 4.2 . . . . . . . . . . . .

<!-- b000034 | prose | pages [2] -->
11 Application of Evaluation Model . . . . . . . . . . . . . . . . . . . . . . . 4.3 11 Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.4 13

<!-- b000035 | prose | pages [2] -->
TASK 3: Advice on Improving Team Success 5 14 Structural Strategy Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 14 Comparison with Italy National Team . . . . . . . . . . . . . . . . . . . . . 5.2 15 Advise on next Season . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.3 16

<!-- b000036 | prose | pages [2] -->
TASK 4: How to Design more Effective Teams 6 17 Generalization of our Model . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 17 Other Aspects . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2

<!-- b000037 | prose | pages [2] -->
7

<!-- b000038 | heading | pages [2] -->
Analysis on Model’s Sensitivity

<!-- b000039 | prose | pages [2] -->
18

<!-- b000040 | prose | pages [2] -->
18 Evaluation Model sensitivity to Draw situations 7.1 . . . . . . . . . . . . . .

<!-- b000041 | prose | pages [2] -->
18 Analysis on performance indicator Tempo . . . . . . . . . . . . . . . . . . 7.2

<!-- b000042 | prose | pages [2] -->
8

<!-- b000043 | heading | pages [2] -->
Strengths and Weaknesses

<!-- b000044 | prose | pages [2] -->
19

<!-- b000045 | prose | pages [2] -->
20 Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.1 20 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.2 Weaknesses

<!-- b000046 | heading | pages [2] -->
References

<!-- b000047 | heading | pages [2] -->
Appendix: Code

<!-- b000048 | prose | pages [2] -->
20

<!-- b000049 | prose | pages [2] -->
21

<!-- b000050 | prose | pages [2] -->
22

<!-- b000051 | prose | pages [2] -->
关注数学模型

<!-- b000052 | furniture | pages [2] -->
2

<!-- b000053 | furniture | pages [2] -->
MATHmodels

<!-- b000054 | furniture | pages [2] -->
获取更多资讯

<!-- b000055 | furniture | pages [3] -->
Team # 2006782

<!-- b000056 | prose | pages [3] -->
1

<!-- b000057 | heading | pages [3] -->
Introduction

<!-- b000058 | prose | pages [3] -->
1.1 Problem Background

<!-- b000059 | furniture | pages [3] -->
Page 1 of 25

<!-- b000060 | prose | pages [3] -->
With the development of social interconnections, the challenge people faced has become complex increasingly. Some reports point out the best strategies for team for- mation, the best interaction between teammates, and the ideal leadership style. A strong team across departments and domains can complete complex tasks that cannot be accomplished through individual efforts or additional contributions from a series of teammates.

<!-- b000061 | prose | pages [3] -->
The coach has asked ICM to quantify and formalize the structural and dynami- cal features that have been successful (and unsuccessful) for the team. The team are provided with the following tasks:

<!-- b000062 | prose | pages [3] -->
• Create a network for the ball passing between players, and explore multiple scales such as regions and time.

<!-- b000063 | prose | pages [3] -->
• Identify performance indicators that reﬂect successful teamwork.

<!-- b000064 | prose | pages [3] -->
• Make suggestions to the coach using the opinions gained from the model.

<!-- b000065 | prose | pages [3] -->
• Indicate how to build an effective team and give other important factors for form- ing an dynamic team.

<!-- b000066 | prose | pages [3] -->
1.2 Our work

<!-- b000067 | heading | pages [3] -->
1. Firstly, we establish a ball passing network based on the passing events.Then we uti-

<!-- b000068 | prose | pages [3] -->
lize K-means agAlgorithmm to classify dyadic and triadic conﬁgurations in the net- work.

<!-- b000069 | heading | pages [3] -->
2. Then we build an Evaluation model based on Adversarial Regression, and get the re-

<!-- b000070 | prose | pages [3] -->
gression equation. Taking the opponents into account, we have a discussion about whether strategies are universally effective.

<!-- b000071 | heading | pages [3] -->
3. Furthermore, We analyze the formations and strategies Huskies adopt and recom-

<!-- b000072 | prose | pages [3] -->
mend the team to adopt Defensive counterattack. What’s more, we get to know the gap with strong team after comparing with Italy National Team.

<!-- b000073 | heading | pages [3] -->
4. Last but not least, we generalize our model to more teamwork and indicate how

<!-- b000074 | prose | pages [3] -->
to build an effective team and give other important factors for forming an dynamic team.

<!-- b000075 | prose | pages [3] -->
2

<!-- b000076 | heading | pages [3] -->
Preparation of the Models

<!-- b000077 | heading | pages [3] -->
Assumptions and Justiﬁcations

<!-- b000078 | prose | pages [3] -->
2.1

<!-- b000079 | prose | pages [3] -->
• The ball passing network is an undirected graph.

<!-- b000080 | prose | pages [3] -->
• The incoming player substitutes the outgoing player directly, without changing the team formation.

<!-- b000081 | prose | pages [3] -->
关注数学模型

<!-- b000082 | furniture | pages [3] -->
2

<!-- b000083 | furniture | pages [3] -->
MATHmodels

<!-- b000084 | furniture | pages [3] -->
获取更多资讯

<!-- b000085 | furniture | pages [4] -->
Team # 2006782

<!-- b000086 | furniture | pages [4] -->
Page 2 of 25

<!-- b000087 | prose | pages [4] -->
• There is no difference between the opponents’ strength level, which lies in the opponents’ counter strategy.

<!-- b000088 | prose | pages [4] -->
• Each player, either of Huskies or of opponents, has the same physical quality and individual ability.

<!-- b000089 | prose | pages [4] -->
2.2

<!-- b000090 | heading | pages [4] -->
Notations

<!-- b000091 | prose | pages [4] -->
The primary notations used in this paper are listed in Table 1.

<!-- b000092 | caption | pages [4] -->
Table 1: Notations

<!-- b000093 | prose | pages [4] -->
Symbol

<!-- b000094 | prose | pages [4] -->
L

<!-- b000095 | prose | pages [4] -->
Deﬁnition

<!-- b000096 | prose | pages [4] -->
Total links of network ρ Network Density wij Number of passes dij topological distance D Network Diameter C(i) Clustering Coefﬁcient f ratio of goals to shots d ratio of defenses to losses φ Distribution of contributes tb 50-ball Passing Time µi Number of shots νi Number of defenses S Score of teamwork βi Weight of indicators γ Coordination among players

<!-- b000097 | heading | pages [4] -->
TASK 1: Ball Passing Network Model

<!-- b000098 | prose | pages [4] -->
3

<!-- b000099 | prose | pages [4] -->
Construction of Ball Passing Network 3.1

<!-- b000100 | prose | pages [4] -->
3.1.1 Ball Passing Network

<!-- b000101 | prose | pages [4] -->
Considering the relationship between players on the football ﬁeld, the network for

<!-- b000102 | prose | pages [4] -->
[1] in Data Structure. An ad-

<!-- b000103 | prose | pages [4] -->
the ball passing can be described as an adjacency matrix

<!-- b000104 | prose | pages [4] -->
jacency matrix can be generated to perform network analysis, which represents the connections between a node (player) and an adjacency node (teammate). To generate an adjacency matrix for network analysis, you must deﬁne criteria that characterize the connections. We deﬁne wij as the number of passes between player i and player j. The adjacency matrix between players can be expressed as:

<!-- b000105 | prose | pages [4] -->
关注数学模型

<!-- b000106 | furniture | pages [4] -->
2

<!-- b000107 | furniture | pages [4] -->
MATHmodels

<!-- b000108 | furniture | pages [4] -->
获取更多资讯

<!-- b000109 | furniture | pages [5] -->
Team # 2006782

<!-- b000110 | prose | pages [5] -->
1 2

<!-- b000111 | prose | pages [5] -->


<!-- b000112 | prose | pages [5] -->
w11 w12 1

<!-- b000113 | prose | pages [5] -->


<!-- b000114 | prose | pages [5] -->
w21 w21 2

<!-- b000115 | prose | pages [5] -->
 

<!-- b000116 | prose | pages [5] -->
...

<!-- b000117 | prose | pages [5] -->
...

<!-- b000118 | prose | pages [5] -->
...

<!-- b000119 | prose | pages [5] -->


<!-- b000120 | prose | pages [5] -->
w11,1 w11,2 11

<!-- b000121 | furniture | pages [5] -->
Page 3 of 25

<!-- b000122 | prose | pages [5] -->
··· 11

<!-- b000123 | prose | pages [5] -->


<!-- b000124 | prose | pages [5] -->
· · · w1,11

<!-- b000125 | prose | pages [5] -->


<!-- b000126 | prose | pages [5] -->
· · · w2,11

<!-- b000127 | prose | pages [5] -->
 ,  (1)

<!-- b000128 | prose | pages [5] -->
... · · ·

<!-- b000129 | prose | pages [5] -->
· · · w11,11

<!-- b000130 | prose | pages [5] -->
In this paper, we assume that the ball passing network is an undirected graph, which means the edge has no direction. Therefore, we have the number of passes between players wij = wji

<!-- b000131 | prose | pages [5] -->
Meanwhile, the ball passing network can be vividly illustrated in Figure 1 by Gephi.

<!-- b000132 | prose | pages [5] -->
D1 D1

<!-- b000133 | prose | pages [5] -->
D2 D2

<!-- b000134 | prose | pages [5] -->
G1 G1

<!-- b000135 | prose | pages [5] -->
D3 D3

<!-- b000136 | prose | pages [5] -->
D4 D4

<!-- b000137 | prose | pages [5] -->
M1 M1

<!-- b000138 | prose | pages [5] -->
F1 F1

<!-- b000139 | prose | pages [5] -->
M2 M2

<!-- b000140 | prose | pages [5] -->
F2 F2

<!-- b000141 | prose | pages [5] -->
M3 M3

<!-- b000142 | prose | pages [5] -->
F3 F3

<!-- b000143 | caption | pages [5] -->
Figure 1: An example of the ball passing network

<!-- b000144 | prose | pages [5] -->
Where width of the links are proportional to their weights, while the size of the nodes correspond to the number of passes.

<!-- b000145 | prose | pages [5] -->
Determination of Network Parameter 3.1.2

<!-- b000146 | prose | pages [5] -->
In order to further understand the network model, we should select some relevant indicators. The ball passing network analysis of the Huskies was focused on the fol- lowing four measures based on the connections between teammates: total links, density, diameter, and clustering coefﬁcient.

<!-- b000147 | prose | pages [5] -->
• Total Links L

<!-- b000148 | prose | pages [5] -->
The sum of the elements of each row of the adjacency matrix ∑11

<!-- b000149 | prose | pages [5] -->
j=1 is the total num- ber of passes between player i and all other teammates, which is the degree in Graph Theory. A node with a higher degree is a player who made more considerable passes with most of its teammates. This shows that the player is involved in the attacking development of his team..

<!-- b000150 | prose | pages [5] -->
In an undirected graph, the Total Links (L) between each team player is a signiﬁcant parameter in the analysis, which the value is half of the total sum of each adjacency matrix row sum.

<!-- b000151 | prose | pages [5] -->
∑

<!-- b000152 | prose | pages [5] -->
L = 1

<!-- b000153 | prose | pages [5] -->
2

<!-- b000154 | prose | pages [5] -->
j=1

<!-- b000155 | prose | pages [5] -->
11 11

<!-- b000156 | prose | pages [5] -->
11 ∑

<!-- b000157 | prose | pages [5] -->
wij.

<!-- b000158 | prose | pages [5] -->
(2)

<!-- b000159 | prose | pages [5] -->
i=1

<!-- b000160 | prose | pages [5] -->
The Total Links is very useful when evaluating the performance of a team, as it is

<!-- b000161 | prose | pages [5] -->
关注数学模型

<!-- b000162 | prose | pages [5] -->
the absolute number of total interactions between teammates in a match. Therefore,

<!-- b000163 | furniture | pages [5] -->
2

<!-- b000164 | furniture | pages [5] -->
MATHmodels

<!-- b000165 | furniture | pages [5] -->
获取更多资讯

<!-- b000166 | furniture | pages [6] -->
Team # 2006782

<!-- b000167 | furniture | pages [6] -->
Page 4 of 25

<!-- b000168 | prose | pages [6] -->
the team’s average total link index is higher than the average, which indicates a strong cooperation among team members.

<!-- b000169 | prose | pages [6] -->
• Network Density ρ

<!-- b000170 | prose | pages [6] -->
Total Links is the number of absolute interactions between one player and another player. However, the Network Density of team is a relative parameter, and it can also

<!-- b000171 | prose | pages [6] -->
[2]

<!-- b000172 | prose | pages [6] -->
measure the overall emotion between teammates.

<!-- b000173 | prose | pages [6] -->
In graph theory, the density of a graph is proportional to the maximum number of possible adjacency edges. Let’s consider the number of edges in the graph as n. Thus, the Network Density ρ is deﬁned as the ratio of the Total Links L to the maximum number of possible adjacency edges as follow:

<!-- b000174 | prose | pages [6] -->
ρ = L

<!-- b000175 | prose | pages [6] -->
, (3)

<!-- b000176 | prose | pages [6] -->
C2

<!-- b000177 | prose | pages [6] -->
n

<!-- b000178 | prose | pages [6] -->
where in this paper the number of edges n = 11, so the density ρ = L

<!-- b000179 | prose | pages [6] -->
• Network Diameter D

<!-- b000180 | prose | pages [6] -->
55.

<!-- b000181 | prose | pages [6] -->
The Network Diameter D of a network reﬂects how far, at most, two nodes in the graph are. The topological distance dij of the link between two players i and j is de- ﬁned as the inverse of the link weight.

<!-- b000182 | prose | pages [6] -->
dij = 1

<!-- b000183 | prose | pages [6] -->
(4)

<!-- b000184 | prose | pages [6] -->
wij

<!-- b000185 | prose | pages [6] -->
[3] (the length of the

<!-- b000186 | prose | pages [6] -->
The Diameter D of a graph is the maximum topological distance

<!-- b000187 | prose | pages [6] -->
largest geodesic) between any two players and can be expressed as:

<!-- b000188 | prose | pages [6] -->
D = max

<!-- b000189 | prose | pages [6] -->
i max

<!-- b000190 | prose | pages [6] -->
dij.

<!-- b000191 | prose | pages [6] -->
(5) j

<!-- b000192 | prose | pages [6] -->
In case of team players, a small diameter reﬂects a low maximum distance between teammates, which may reveal that the team’s passing game was diffused among most of its players (rather than a few acting as central ones).

<!-- b000193 | prose | pages [6] -->
• Clustering coefﬁcient C(i)

<!-- b000194 | prose | pages [6] -->
Considering the network is weighted, we can not simply account for the number of nodes connected between them but how the link weights are distributed. In the case of the ball passing network, the number of passes between pairs of players is not

<!-- b000195 | prose | pages [6] -->
[4] Cw(i) to measure

<!-- b000196 | prose | pages [6] -->
constant. As a consequence, we use a Weighted Clustering Coefﬁcient

<!-- b000197 | prose | pages [6] -->
the possibility that a given player i’s teammates will also create a connection between them:

<!-- b000198 | prose | pages [6] -->
∑

<!-- b000199 | prose | pages [6] -->
j

<!-- b000200 | prose | pages [6] -->
∑

<!-- b000201 | prose | pages [6] -->
Cw(i) =

<!-- b000202 | prose | pages [6] -->
j

<!-- b000203 | prose | pages [6] -->
∑

<!-- b000204 | prose | pages [6] -->
wijwjkwik

<!-- b000205 | prose | pages [6] -->
k k

<!-- b000206 | prose | pages [6] -->
∑

<!-- b000207 | prose | pages [6] -->
.

<!-- b000208 | prose | pages [6] -->
(6)

<!-- b000209 | prose | pages [6] -->
wijwik

<!-- b000210 | prose | pages [6] -->
k

<!-- b000211 | prose | pages [6] -->
Where j and k are the two teammates of player i, wij and wik are the number of ball passes between player i and both them. At last, the Clustering Coefﬁcient Ci for the entire network is obtained by averaging Cw(i) for all players, i.e.

<!-- b000212 | prose | pages [6] -->
C = 1

<!-- b000213 | prose | pages [6] -->
n

<!-- b000214 | prose | pages [6] -->
n n ∑

<!-- b000215 | prose | pages [6] -->
Cw(i), (7)

<!-- b000216 | prose | pages [6] -->
i=1

<!-- b000217 | prose | pages [6] -->
关注数学模型

<!-- b000218 | prose | pages [6] -->
where in this paper the number of edges n = 11.

<!-- b000219 | furniture | pages [6] -->
2

<!-- b000220 | furniture | pages [6] -->
MATHmodels

<!-- b000221 | furniture | pages [6] -->
获取更多资讯

<!-- b000222 | furniture | pages [7] -->
Team # 2006782

<!-- b000223 | furniture | pages [7] -->
Page 5 of 25

<!-- b000224 | prose | pages [7] -->
Identiﬁcation of Network Patterns 3.2

<!-- b000225 | prose | pages [7] -->
3.2.1 Team Formation

<!-- b000226 | prose | pages [7] -->
The formation of each game can be easily obtained by looking through the player list. In the dataset provided for us, all players are placed in four positions, which are goalkeeper, defense, midﬁeld and forward. So when we study the formation in one game, we place the players in the position his ID indicates, thus obtaining the formation. To simplify the model, we assume that the substituted player replaces the player substi- tuted directly, without changing the formation. We take the 1st, the 2nd and the 4th

<!-- b000227 | prose | pages [7] -->
match as examples. The formation of these matches means a teamwork strategy. Take 4-3-3 as an example, this formation means we have 4 defenses , 3 midﬁelds and 3 forwards.

<!-- b000228 | prose | pages [7] -->
The 1st match Huskies take 4-3-3 formation, while the formations of the 2nd and the 4th matches are 5-3-2 and 4-4-2 respectively. In each game, the coach will take differ- ent formations according to the strategy, so ﬁguring out the formation is important to understand the strategy, thus better identifying the network pattern. However, forma- tion just gives us a general view of the network. To identify the network pattern more comprehensively, we need more details of the network.

<!-- b000229 | prose | pages [7] -->
3.2.2 Dyadic and Triadic Conﬁgurations

<!-- b000230 | prose | pages [7] -->
Considering the difference in opponent and strategy, the ball passing network we build varies from match to match. Therefore, in order to identify the network pattern, we need to analyze a speciﬁc game in detail. In this chapter, we take the 1st match as an example.

<!-- b000231 | prose | pages [7] -->
G1 D1 D2 D4 D3

<!-- b000232 | prose | pages [7] -->
G1 ∞ ∞ 1/4 1/3 1/8

<!-- b000233 | prose | pages [7] -->
∞ D1 1/4

<!-- b000234 | prose | pages [7] -->
M1 M2 M3 F1 F2 F3

<!-- b000235 | prose | pages [7] -->
∞ ∞ ∞ 1/4 1 1/2

<!-- b000236 | prose | pages [7] -->
1/14 1/24 1/2 1 1/29

<!-- b000237 | prose | pages [7] -->
D2 1/3 1/29 ∞

<!-- b000238 | prose | pages [7] -->
1/10 1/5 1/6 1

<!-- b000239 | prose | pages [7] -->
1/2 1/11 1/3 1/15 1/24 1/10 1

<!-- b000240 | prose | pages [7] -->
D4 ∞ ∞

<!-- b000241 | prose | pages [7] -->
1

<!-- b000242 | prose | pages [7] -->
1/13 1/4 1 1

<!-- b000243 | prose | pages [7] -->
D3 1/8 1/14 1/24 1/13 ∞

<!-- b000244 | prose | pages [7] -->
M1 1/4 1/24 1/10 1/4 1/4

<!-- b000245 | prose | pages [7] -->
M2 1 1/2 1/2 1/10 1/8

<!-- b000246 | prose | pages [7] -->
M3 ∞

<!-- b000247 | prose | pages [7] -->
1/10 1/4 1 1/4 1/2

<!-- b000248 | prose | pages [7] -->
1/8 1/14 1/4 1 1/6 1/3

<!-- b000249 | prose | pages [7] -->
∞ 1/5 1/17 1/6 1/24 1/3

<!-- b000250 | prose | pages [7] -->
∞ 1 1/4 1/6 1/5 1/13

<!-- b000251 | prose | pages [7] -->
1/10 1/11 1/4 1/14 1/17 1/13 ∞

<!-- b000252 | prose | pages [7] -->
F1 1/2 1/5 1/3 1 1

<!-- b000253 | prose | pages [7] -->
F2 ∞

<!-- b000254 | prose | pages [7] -->
∞ 1/10 1/3

<!-- b000255 | prose | pages [7] -->
∞ ∞ 1/6 1 1/8 1/3

<!-- b000256 | prose | pages [7] -->
∞ 1/6 1/24 1/4 1/6 1/15 1/4

<!-- b000257 | prose | pages [7] -->
F3 ∞ 1 1 1/2 1/3

<!-- b000258 | prose | pages [7] -->
1/10 1/8 1/7

<!-- b000259 | prose | pages [7] -->
∞ 1/3 1/6 1/3 1/3 1/7

<!-- b000260 | caption | pages [7] -->
Figure 2: Topological Distance Matrix of the 1st match

<!-- b000261 | prose | pages [7] -->
关注数学模型

<!-- b000262 | furniture | pages [7] -->
2

<!-- b000263 | furniture | pages [7] -->
MATHmodels

<!-- b000264 | furniture | pages [7] -->
获取更多资讯

<!-- b000265 | furniture | pages [8] -->
Team # 2006782

<!-- b000266 | furniture | pages [8] -->
Page 6 of 25

<!-- b000267 | prose | pages [8] -->
First, we apply our model to the 1st match and build the ball passing network. From the adjacency matrix, the Total Links L and Network Density ρ can be easily obtained by the equation (2) and (3) we give, which are 369 and 6.71 respectively. Moreover, we can use the equation (4) to obtain the topological distance matrix (see Figure 2).

<!-- b000268 | prose | pages [8] -->
In the topological distance matrix, ∞means the distance between the two nodes is inﬁnite, which suggests that they don’t have any passing in the game. There is no doubt that the statistics marked by red box is smaller than other statistic, which means the two nodes are very close in topological distance.

<!-- b000269 | prose | pages [8] -->
In Graph Theory, we call these nodes with higher similarity (distance) cluster. There-

<!-- b000270 | prose | pages [8] -->
[5] to

<!-- b000271 | prose | pages [8] -->
fore, the passing network has many clusters in it and we use a K-means Algorithm

<!-- b000272 | prose | pages [8] -->
classify the clusters in our passing network. The results have been shown in Figure 3.

<!-- b000273 | prose | pages [8] -->
F1

<!-- b000274 | prose | pages [8] -->
F2

<!-- b000275 | prose | pages [8] -->
M1

<!-- b000276 | prose | pages [8] -->
D1 D2

<!-- b000277 | prose | pages [8] -->
F3

<!-- b000278 | prose | pages [8] -->
M3 M2

<!-- b000279 | prose | pages [8] -->
D3 D4

<!-- b000280 | prose | pages [8] -->
G1 G1

<!-- b000281 | caption | pages [8] -->
Figure 3: Dyadic and Triadic Conﬁgurations

<!-- b000282 | prose | pages [8] -->
Consequently, we classify (D1, D2, D3), (D1, M1, F2) and (M2, M3) into three clusters, which are so-called Dyadic and Triadic Conﬁgurations. Also, we can conclude that the passing network patterns involve one dyadic conﬁguration and two triadic conﬁgurations.

<!-- b000283 | prose | pages [8] -->
Then we explore more deeply on (D1, M1, F2). According to the passing net- work, these three players make 227 passes in total, while the passes between these three account for 26.7%. Moreover, the cluster coefﬁcient C of the three equals 7.31, much smaller than that of the whole team (7.62), which means the connectivity between the (D1, M1, F2) is much higher than that between the three and other players. In this case, it’s more likely to form clusters just like these three players.

<!-- b000284 | prose | pages [8] -->
3.3 Other Structural Indicators

<!-- b000285 | prose | pages [8] -->
3.3.1 Time Scale

<!-- b000286 | prose | pages [8] -->
In a gesture to explore other structured indicators to evaluate the ball passing net- work, we next analyse the time scale. As small as every minute and every second, and as large as the entire game and season, the time scale can undoubtedly reﬂect the team’s game status. In this part, we mainly discuss two aspects: 10-minute network passes and the entire game network passes.

<!-- b000287 | prose | pages [8] -->
关注数学模型

<!-- b000288 | furniture | pages [8] -->
2

<!-- b000289 | furniture | pages [8] -->
MATHmodels

<!-- b000290 | furniture | pages [8] -->
获取更多资讯

<!-- b000291 | furniture | pages [9] -->
Team # 2006782

<!-- b000292 | prose | pages [9] -->
• 10-minute Network Passes

<!-- b000293 | furniture | pages [9] -->
Page 7 of 25

<!-- b000294 | prose | pages [9] -->
When it comes to the relatively small period of time throughout the game, we have to introduce the tempo in football. Tempo, in a word, is the speed of any movement or activity, which mainly includes the speed of advancement, transmission, and running. Players in the ﬁeld determine when to be fast and when to be slow through factors such as technology, vision, anticipation, tactics, and the actual situation of the game.

<!-- b000295 | prose | pages [9] -->
An important indicator of tempo is the number of passes. Team with more passes in a unit time are those generate more passes in less time, and indicates that they have a well capability of controlling tempo. In our case, we analyzed the effects of using different time intervals t of passes and chose t = 10 min = 600 sec as a trade-off value.

<!-- b000296 | prose | pages [9] -->
At the same time, we take the 1st match as an example to study the number of passes of the Huskies every ten minutes, which is deﬁned as α. Considering the interval between two half, we didn’t talk about the number of ball passes between 40 - 45 min in both half.

<!-- b000297 | prose | pages [9] -->
80

<!-- b000298 | prose | pages [9] -->
70

<!-- b000299 | prose | pages [9] -->
60

<!-- b000300 | prose | pages [9] -->
50

<!-- b000301 | prose | pages [9] -->
40

<!-- b000302 | prose | pages [9] -->
30

<!-- b000303 | prose | pages [9] -->
20

<!-- b000304 | prose | pages [9] -->
10

<!-- b000305 | prose | pages [9] -->
0

<!-- b000306 | prose | pages [9] -->
0 10 20 30 40 Ball

<!-- b000307 | prose | pages [9] -->
51 46 72 43

<!-- b000308 | prose | pages [9] -->
Passes Internal 55 65 75 85 90

<!-- b000309 | prose | pages [9] -->
50 49 32 10

<!-- b000310 | prose | pages [9] -->
Substitution

<!-- b000311 | prose | pages [9] -->
Substitution

<!-- b000312 | prose | pages [9] -->
Substitution

<!-- b000313 | prose | pages [9] -->
2nd half: 60 s

<!-- b000314 | prose | pages [9] -->
D5

<!-- b000315 | prose | pages [9] -->
2nd half: 900 s

<!-- b000316 | prose | pages [9] -->
2nd half: 1920 s

<!-- b000317 | prose | pages [9] -->
D2

<!-- b000318 | prose | pages [9] -->
M4 M2

<!-- b000319 | prose | pages [9] -->
M5 F3

<!-- b000320 | caption | pages [9] -->
Figure 4: 10-minute Network passes of Huskies in the 1st match

<!-- b000321 | prose | pages [9] -->
As is clearly depicted in Figure 4, Huskies’ 10-minute Network passes is relatively stable. From the timeline, we can ﬁnd that in about 30 minutes, the Huskies changed the tempo, the attack speed accelerated, and the rhythm showed a simple and bright. In the last 10 minutes, the Huskies were relatively conservative and had fewer passes, and we can attribute it to exhaust.

<!-- b000322 | prose | pages [9] -->
• Entire Game and Entire Season Network Passes

<!-- b000323 | prose | pages [9] -->
In this part, we explore the passing network at the level of the whole game. Using the ball passing matrix and equation (2), we get the following Figure 5.

<!-- b000324 | prose | pages [9] -->
Six matches are chosen from different period of the whole season. As is shown in Figure 5, we can conclude that at the beginning of the season, the teamwork perfor- mance is unstable.

<!-- b000325 | prose | pages [9] -->
However, As the season progresses, the Huskies’ performance has gradually stabi- lized, and a stronger connectivity between the players has also formed.

<!-- b000326 | prose | pages [9] -->
关注数学模型

<!-- b000327 | furniture | pages [9] -->
2

<!-- b000328 | furniture | pages [9] -->
MATHmodels

<!-- b000329 | furniture | pages [9] -->
获取更多资讯

<!-- b000330 | furniture | pages [10] -->
Team # 2006782

<!-- b000331 | prose | pages [10] -->
D1 D1

<!-- b000332 | prose | pages [10] -->
D1 D1

<!-- b000333 | prose | pages [10] -->
D2 D2

<!-- b000334 | prose | pages [10] -->
M1 M1

<!-- b000335 | prose | pages [10] -->
F1 F1

<!-- b000336 | prose | pages [10] -->
D2 D2

<!-- b000337 | prose | pages [10] -->
D3 D3

<!-- b000338 | prose | pages [10] -->
G1 G1

<!-- b000339 | prose | pages [10] -->
M2 M2

<!-- b000340 | prose | pages [10] -->
G1 G1

<!-- b000341 | prose | pages [10] -->
F2 F2

<!-- b000342 | prose | pages [10] -->
D3 D3

<!-- b000343 | prose | pages [10] -->
D4 D4

<!-- b000344 | prose | pages [10] -->
M3 M3

<!-- b000345 | prose | pages [10] -->
F3 F3

<!-- b000346 | prose | pages [10] -->
D4 D4

<!-- b000347 | prose | pages [10] -->
D6 D6

<!-- b000348 | furniture | pages [10] -->
Page 8 of 25

<!-- b000349 | prose | pages [10] -->
D1 D1

<!-- b000350 | prose | pages [10] -->
M1 M1

<!-- b000351 | prose | pages [10] -->
M1 M1

<!-- b000352 | prose | pages [10] -->
F1 F1

<!-- b000353 | prose | pages [10] -->
F2 F2

<!-- b000354 | prose | pages [10] -->
D2 D2

<!-- b000355 | prose | pages [10] -->
M3 M3

<!-- b000356 | prose | pages [10] -->
D3 D3

<!-- b000357 | prose | pages [10] -->
M4 M4

<!-- b000358 | prose | pages [10] -->
G1 G1

<!-- b000359 | prose | pages [10] -->
F2 F2

<!-- b000360 | prose | pages [10] -->
D4 D4

<!-- b000361 | prose | pages [10] -->
F3 F3

<!-- b000362 | prose | pages [10] -->
M4 M4

<!-- b000363 | prose | pages [10] -->
M6 M6

<!-- b000364 | prose | pages [10] -->
D6 D6

<!-- b000365 | prose | pages [10] -->
(b) Match 2 (L = 180)

<!-- b000366 | prose | pages [10] -->
(a) Match 1 (L = 369)

<!-- b000367 | prose | pages [10] -->
D2 D2

<!-- b000368 | prose | pages [10] -->
M1 M1

<!-- b000369 | prose | pages [10] -->
D1 D1

<!-- b000370 | prose | pages [10] -->
D3 D3

<!-- b000371 | prose | pages [10] -->
F2 F2 M2 M2

<!-- b000372 | prose | pages [10] -->
D2 D2

<!-- b000373 | prose | pages [10] -->
G1 G1

<!-- b000374 | prose | pages [10] -->
G1 G1

<!-- b000375 | prose | pages [10] -->
D4 D4

<!-- b000376 | prose | pages [10] -->
F3 F3

<!-- b000377 | prose | pages [10] -->
M3 M3 D4 D4

<!-- b000378 | prose | pages [10] -->
D7 D7

<!-- b000379 | prose | pages [10] -->
M6 M6

<!-- b000380 | prose | pages [10] -->
D5 D5

<!-- b000381 | prose | pages [10] -->
(c) Match 3 (L = 324)

<!-- b000382 | prose | pages [10] -->
M1 M1

<!-- b000383 | prose | pages [10] -->
D1 D1

<!-- b000384 | prose | pages [10] -->
M1 M1

<!-- b000385 | prose | pages [10] -->
M3 M3

<!-- b000386 | prose | pages [10] -->
D3 D3

<!-- b000387 | prose | pages [10] -->
F1 F1

<!-- b000388 | prose | pages [10] -->
M4 M4

<!-- b000389 | prose | pages [10] -->
F1 F1

<!-- b000390 | prose | pages [10] -->
M5 M5

<!-- b000391 | prose | pages [10] -->
G1 G1

<!-- b000392 | prose | pages [10] -->
D4 D4

<!-- b000393 | prose | pages [10] -->
F2 F2 M5 M5

<!-- b000394 | prose | pages [10] -->
M6 M6

<!-- b000395 | prose | pages [10] -->
D7 D7

<!-- b000396 | prose | pages [10] -->
M8 M8

<!-- b000397 | prose | pages [10] -->
M8 M8

<!-- b000398 | prose | pages [10] -->
(e) Match 10 (L = 359)

<!-- b000399 | prose | pages [10] -->
(d) Match 4 (L = 354)

<!-- b000400 | prose | pages [10] -->
(f) Match 13 (L = 347)

<!-- b000401 | caption | pages [10] -->
Figure 5: Entire Game and Entire Season Network Passes

<!-- b000402 | prose | pages [10] -->
3.3.2 Region Scale

<!-- b000403 | prose | pages [10] -->
In spite of time scale, we can also analyze the passing network by region scale. The football ﬁeld can be divided into eight regions averagely. Then we use the location where each passes occur to have an overview.

<!-- b000404 | caption | pages [10] -->
Figure 6: An overview of the passes in football ﬁeld

<!-- b000405 | prose | pages [10] -->
As is shown in Figure 6, Huskies make their most passes in the backcourt, which is in line with their highlight in defense. Moreover, the connectivity between defense players is higher than that of forward players. However, Figure 6 also shows that Huskies hasn’t made full use of the width of the ﬁeld. They can try to make more passes in those regions with light color.

<!-- b000406 | prose | pages [10] -->
关注数学模型

<!-- b000407 | furniture | pages [10] -->
2

<!-- b000408 | furniture | pages [10] -->
MATHmodels

<!-- b000409 | furniture | pages [10] -->
获取更多资讯

<!-- b000410 | furniture | pages [11] -->
Team # 2006782

<!-- b000411 | furniture | pages [11] -->
Page 9 of 25

<!-- b000412 | prose | pages [11] -->
TASK 2: Evaluation of Successful Teamwork 4

<!-- b000413 | prose | pages [11] -->
Identiﬁcation of Performance Indicators 4.1

<!-- b000414 | prose | pages [11] -->
To further evaluate whether the teamwork is success, we should select some rel- evant indicators. This paper simpliﬁes the performance indicators into two aspects: Static and Dynamic. The Static performance indicators mainly contain: Coordination among players, Distribution of contributions. And the Dynamic performance indicators involve: tempo, ﬂexibility, Pressing.

<!-- b000415 | prose | pages [11] -->
4.1.1 Static Layer

<!-- b000416 | prose | pages [11] -->
• Coordination among players

<!-- b000417 | prose | pages [11] -->
In terms of coordination among players, we use cluster coefﬁcient C to quantify it. One player’s cluster coefﬁcient means his connectivity with other teammates. The team’s average cluster coefﬁcient embodies the level of coordination in the team. There- fore, the higher average cluster coefﬁcient C is, the stronger coordination γ is.

<!-- b000418 | prose | pages [11] -->
• Distribution of contributions

<!-- b000419 | prose | pages [11] -->
Considering the contribution distribution, we may consider the contribution of each player into two aspects, namely forward and defense. Set the number of shots per player i to µi and the number of defenses to ν1.

<!-- b000420 | prose | pages [11] -->
Below we discuss forward and defense success rates. Forward success rate can be obtained by the ratio of the number of goals to the number of shots, which can be described as:

<!-- b000421 | prose | pages [11] -->
f = µgoal

<!-- b000422 | prose | pages [11] -->
,

<!-- b000423 | prose | pages [11] -->
∑11

<!-- b000424 | prose | pages [11] -->
(8)

<!-- b000425 | prose | pages [11] -->
i=1 µi

<!-- b000426 | prose | pages [11] -->
Defense success rate can be obtained by the ratio of the number of defenses to the number of losses plus one, which can be expressed as:

<!-- b000427 | prose | pages [11] -->
∑11

<!-- b000428 | prose | pages [11] -->
j=1 νj νloss + 1.

<!-- b000429 | prose | pages [11] -->
d =

<!-- b000430 | prose | pages [11] -->
(9)

<!-- b000431 | prose | pages [11] -->
Where we add one to the denominator of f to prevent the denominator from being zero.

<!-- b000432 | prose | pages [11] -->
Then we get a parameter φ about Distribution of contributions:

<!-- b000433 | prose | pages [11] -->
φ = f · d.

<!-- b000434 | prose | pages [11] -->
(10)

<!-- b000435 | prose | pages [11] -->
Where Larger φ means fewer mistakes and more success.

<!-- b000436 | prose | pages [11] -->
4.1.2 Dynamic Layer

<!-- b000437 | prose | pages [11] -->
• Tempo

<!-- b000438 | prose | pages [11] -->
In TASK 1, we have talked about tempo by means of 10-minute Network Passes, which is the number of passes per ten minutes. However, when we discuss team per- formance evaluation, the performance of 10-minute Network Passes is not very obvious,

<!-- b000439 | prose | pages [11] -->
关注数学模型

<!-- b000440 | furniture | pages [11] -->
2

<!-- b000441 | furniture | pages [11] -->
MATHmodels

<!-- b000442 | furniture | pages [11] -->
获取更多资讯

<!-- b000443 | furniture | pages [12] -->
Team # 2006782

<!-- b000444 | furniture | pages [12] -->
Page 10 of 25

<!-- b000445 | prose | pages [12] -->
[6]. We construct the 50-ball Passing Time with the aim

<!-- b000446 | prose | pages [12] -->
we choose 50-ball Passing Time

<!-- b000447 | prose | pages [12] -->
of accounting for the temporal evolution of the game. 50-ball Passing contain only 50 consecutive passes and are assigned the time of the last of these passes.

<!-- b000448 | prose | pages [12] -->
The 50-ball Passing Time tb is the time required to construct a 50 ball passes. It is obtained subtracting the time of the ﬁrst pass of the network from the time of the last pass. Teams with shorter tb are those that generate more passes in less time.

<!-- b000449 | prose | pages [12] -->
• Flexibility

<!-- b000450 | prose | pages [12] -->
In this section, we use the y-coordinate standard deviation σy to represent team ﬂexibility. The better the team’s ﬂexibility, the greater the standard deviation σy, and the more the off-center disturbances occur. The ﬂexibility can be marked as:

<!-- b000451 | prose | pages [12] -->
n n ∑

<!-- b000452 | prose | pages [12] -->
σy = 1

<!-- b000453 | prose | pages [12] -->
n

<!-- b000454 | prose | pages [12] -->
(yj −¯y) (11)

<!-- b000455 | prose | pages [12] -->
j=1 j=1

<!-- b000456 | prose | pages [12] -->
As is shown in Figure 7, the team with higher σy has more attack strategy, either from both sides or in the middle. In contrast, the team with smaller σy has fewer attack strategy. As a result, if the opponents focus on the defense of the middle, they will not be ﬂexible enough to change their attack strategy like attacking from left or right.

<!-- b000457 | prose | pages [12] -->
100

<!-- b000458 | prose | pages [12] -->
95

<!-- b000459 | prose | pages [12] -->
90

<!-- b000460 | prose | pages [12] -->
85

<!-- b000461 | prose | pages [12] -->
80

<!-- b000462 | prose | pages [12] -->
75

<!-- b000463 | prose | pages [12] -->
70

<!-- b000464 | prose | pages [12] -->
65

<!-- b000465 | prose | pages [12] -->
60

<!-- b000466 | prose | pages [12] -->
55

<!-- b000467 | prose | pages [12] -->
50

<!-- b000468 | prose | pages [12] -->
0 20 40 60 80 100

<!-- b000469 | prose | pages [12] -->
(a) Match with higher Flexibility σy = 33.70

<!-- b000470 | prose | pages [12] -->
100

<!-- b000471 | prose | pages [12] -->
95

<!-- b000472 | prose | pages [12] -->
90

<!-- b000473 | prose | pages [12] -->
85

<!-- b000474 | prose | pages [12] -->
80

<!-- b000475 | prose | pages [12] -->
75

<!-- b000476 | prose | pages [12] -->
70

<!-- b000477 | prose | pages [12] -->
65

<!-- b000478 | prose | pages [12] -->
60

<!-- b000479 | prose | pages [12] -->
55

<!-- b000480 | prose | pages [12] -->
50

<!-- b000481 | prose | pages [12] -->
0 20 40 60 80 100

<!-- b000482 | prose | pages [12] -->
(b) Match with smaller Flexibility σy = 26.66

<!-- b000483 | caption | pages [12] -->
Figure 7: Comparison of matches with different ﬂexibility

<!-- b000484 | prose | pages [12] -->
• Pressing

<!-- b000485 | prose | pages [12] -->
Pressing is an indicator of offense and defense status. Gegenpressing refers to the premise of the entire defense of the team, forcing the opponent to rush the ball from Pressing can be estimated by the expectation of the x- the opponent’s backcourt. coordinate.

<!-- b000486 | prose | pages [12] -->
¯x = 1

<!-- b000487 | prose | pages [12] -->
n ∑

<!-- b000488 | prose | pages [12] -->
xi (12)

<!-- b000489 | prose | pages [12] -->
n n

<!-- b000490 | prose | pages [12] -->
i=1

<!-- b000491 | prose | pages [12] -->
When ¯x = 50, we can consider that there is no gegenpressing and the situation on the court is balanced; when ¯x > 50, there is a situation of gegenpressing on football ﬁeld.

<!-- b000492 | prose | pages [12] -->
关注数学模型

<!-- b000493 | furniture | pages [12] -->
2

<!-- b000494 | furniture | pages [12] -->
MATHmodels

<!-- b000495 | furniture | pages [12] -->
获取更多资讯

<!-- b000496 | furniture | pages [13] -->
Team # 2006782

<!-- b000497 | furniture | pages [13] -->
Page 11 of 25

<!-- b000498 | prose | pages [13] -->
Low Pressing

<!-- b000499 | prose | pages [13] -->
Moderate Pressing

<!-- b000500 | prose | pages [13] -->
Gegenpressing

<!-- b000501 | caption | pages [13] -->
Figure 8: Situation of Gegenpressing on football ﬁeld

<!-- b000502 | heading | pages [13] -->
Evaluation model based on Adversarial Regression

<!-- b000503 | prose | pages [13] -->
4.2

<!-- b000504 | prose | pages [13] -->
We describe the performance of a team S during a football game by ﬁve network measures extracted from its passing network: x1 (Coordination among players γ), x2 (Dis- tribution of contributions φ), x3 (Tempo tb), x4 (Flexibility σy), x5 (Pressing ¯x). We compute the ﬁve network measures of teams for every game and observe a correlation among the proposed network measures and the success of a team during the competition, and therefore set up a simulation experiment to validate our approach.

<!-- b000505 | prose | pages [13] -->
We simulate the result of the match i of the Huskies (or the opponent) through the following ﬁve steps:

<!-- b000506 | prose | pages [13] -->
Step 1: For each of the two teams, we compute the score S of previous performances

<!-- b000507 | prose | pages [13] -->
of the team separately. (S1 for the Huskies, and S2 for the opponent)

<!-- b000508 | prose | pages [13] -->
Si = β1x1 + β2x2 + β3x3 + β4x4 + β5x5 (i = 1, 2) (13)

<!-- b000509 | prose | pages [13] -->
Step 2: Compare the predicted measures of the two teams. If the Huskies win, S1 > S2;

<!-- b000510 | prose | pages [13] -->
if they lose, S1 < S2. When the two teams draw, there should be |S1 −S2| < 1. If not, turn to Step 1.

<!-- b000511 | prose | pages [13] -->
Step 3: Through the former 2 steps, we can obtain all the possible solutions. Set the

<!-- b000512 | prose | pages [13] -->
standard deviation of Huskies’ all matches as error value LowestError.

<!-- b000513 | prose | pages [13] -->
Step 4: We choose the weights with LowestError as the regression equation.

<!-- b000514 | prose | pages [13] -->
So far, we have established our Evaluation model based on Adversarial Regression. The main reason is to introduce the opponent’s confrontation factors, which makes the model more fair in evaluation and accords with the actual situation.

<!-- b000515 | heading | pages [13] -->
Application of Evaluation Model

<!-- b000516 | prose | pages [13] -->
4.3

<!-- b000517 | heading | pages [13] -->
• Data collection

<!-- b000518 | prose | pages [13] -->
In order to calculate the weight βi in equation (13), we take the ﬁrst 33 football matches of this season as an example, as our training dataset, and the last 5 matches as our test dataset, as shown in Table 2.

<!-- b000519 | prose | pages [13] -->
In our statistics of 33 matches, we cleaned and denoised the data. Among them,

<!-- b000520 | prose | pages [13] -->
关注数学模型

<!-- b000521 | prose | pages [13] -->
the 31st and 33rd matched had certain problems. We artiﬁcially adjusted the parameter

<!-- b000522 | furniture | pages [13] -->
2

<!-- b000523 | furniture | pages [13] -->
MATHmodels

<!-- b000524 | furniture | pages [13] -->
获取更多资讯

<!-- b000525 | furniture | pages [14] -->
Team # 2006782

<!-- b000526 | furniture | pages [14] -->
Page 12 of 25

<!-- b000527 | caption | pages [14] -->
Table 2: Identiﬁcation of performance indicators in 33 matches

<!-- b000528 | prose | pages [14] -->
Tempo Coordination Distribution ID H*** O H O H Flexibilty Pressing Result O H O H O

<!-- b000529 | prose | pages [14] -->
539.50 1476.57 32.42 1 7.61 4.00 62.25 12.60 28.58 42.37 51.23 win 1019.95 692.49 2 2.88 8.25 28.71 11.17 29.30 27.34 46.36 49.81 tie 634.78 596.98 3 5.10 9.00 8.43 34.17 27.77 27.03 40.43 52.02 loss 760.01 934.64 4 6.01 5.66 6.14 62.40 ...

<!-- b000530 | prose | pages [14] -->
...

<!-- b000531 | prose | pages [14] -->
...

<!-- b000532 | prose | pages [14] -->
...

<!-- b000533 | prose | pages [14] -->
...

<!-- b000534 | prose | pages [14] -->
...

<!-- b000535 | prose | pages [14] -->
32.74 31.94 44.14 51.62 loss ...

<!-- b000536 | prose | pages [14] -->
...

<!-- b000537 | prose | pages [14] -->
...

<!-- b000538 | prose | pages [14] -->
...

<!-- b000539 | prose | pages [14] -->
...

<!-- b000540 | prose | pages [14] -->
... 707.96 2018.52 30.94 30 5.61 3.00 62.25 7.13 6.58* 30.18 50.75 58.75 win 986.98 1014.37 32.53 31 4.21 20.10 13.87 32** / / / / / 3.75* 26.66 44.20 50.13 win / / / / / / 1159.30 479.62 33 3.35 39.83 21.90 29.43 27.61 51.34 51.20 tie

<!-- b000541 | prose | pages [14] -->
* We artiﬁcially adjusted the parameter value which the value is italic. ** For too large deviation, we discard the 32nd match’s data. *** ‘H’ for the Huskies, and ‘O’ for the opponent.

<!-- b000542 | prose | pages [14] -->
value of Coordination among players γ. The deviation of the 32nd match’s data was too large, and we rounded it off. And then we normalize the remaining data so that its distribution satisﬁes zero-mean and unit variance.

<!-- b000543 | heading | pages [14] -->
• Training algorithm

<!-- b000544 | prose | pages [14] -->
For the data of 32 matches (rounded off the 32nd match), we use a Greedy Algorithm to experiment and calculate each possible weight βi in the model. Then we put the possible weights into the model, and put the data of 33 matches of Huskies into the evaluation system to score, calculate the standard deviation sum of 33 games, and use it as the LowestError of the evaluation model.

<!-- b000545 | prose | pages [14] -->
0.16

<!-- b000546 | prose | pages [14] -->
0.14

<!-- b000547 | prose | pages [14] -->
0.12

<!-- b000548 | prose | pages [14] -->
0.1

<!-- b000549 | prose | pages [14] -->
0.08

<!-- b000550 | prose | pages [14] -->
0.06

<!-- b000551 | prose | pages [14] -->
0.071

<!-- b000552 | prose | pages [14] -->
0.04

<!-- b000553 | prose | pages [14] -->
0.02

<!-- b000554 | prose | pages [14] -->
0

<!-- b000555 | prose | pages [14] -->
1 2 3 4 5 6 7 8 9 10

<!-- b000556 | prose | pages [14] -->
(0.4, 0.6, 0.2, 0.1, 0.1)

<!-- b000557 | prose | pages [14] -->
11 12 13 14 15 16 17 18 19 20

<!-- b000558 | caption | pages [14] -->
Figure 9: LowestError of each possible weight

<!-- b000559 | prose | pages [14] -->
According to the training of the Greedy Algorithm, there are 20 groups of weight coefﬁcient combinations that meet the conditions. We calculate their lowestError re- spectively. As shown in Figure 9, the group with the lowest lowestError is selected as the ﬁnal simulation result weight value ˆβi.

<!-- b000560 | heading | pages [14] -->
• Simulation results and accuracy test

<!-- b000561 | prose | pages [14] -->
According to our supervised observations of the model, the model can keep one dec- imal place for the weight value of each indicator. Finally, we put the last 5 matches

<!-- b000562 | prose | pages [14] -->
关注数学模型

<!-- b000563 | prose | pages [14] -->
into the test, and we can conclude that the model is valid. The model considers the

<!-- b000564 | furniture | pages [14] -->
2

<!-- b000565 | furniture | pages [14] -->
MATHmodels

<!-- b000566 | furniture | pages [14] -->
获取更多资讯

<!-- b000567 | furniture | pages [15] -->
Team # 2006782

<!-- b000568 | furniture | pages [15] -->
Page 13 of 25

<!-- b000569 | prose | pages [15] -->
regression formula for successful teamwork to be:

<!-- b000570 | prose | pages [15] -->
S = 0.4x1 + 0.6x2 + 0.2x3 + 0.1x4 + 0.1x5 + C

<!-- b000571 | prose | pages [15] -->
i.e.

<!-- b000572 | prose | pages [15] -->
(14)

<!-- b000573 | prose | pages [15] -->
S = 0.4γ + 0.6φ + 0.2tb + 0.1σy + 0.1¯x + C (15)

<!-- b000574 | prose | pages [15] -->
Where the minimum error in the optimal weight lowestError = 0.071, is valid for both data ﬁtting and model regression. Through this model, we can score the team for each or teamwork for the entire season, and compare it with opponents, thus making the model adaptable.

<!-- b000575 | prose | pages [15] -->
From the regression equation (15) we get, we can have a general idea about the importance between the ﬁve indicators.

<!-- b000576 | prose | pages [15] -->
• The most signiﬁcant factor is the Distribution of contributions as predicted, because it is linked with the ﬁnal result directly. There is no doubt that a team, where every teammate contributes to the teamwork in his own position efﬁciently, has the strongest energy.

<!-- b000577 | prose | pages [15] -->
• Next is the Coordination among players, which is not difﬁcult to understand.

<!-- b000578 | prose | pages [15] -->
• Then comes the ﬂexibility, tempo and pressing, which has relatively small weight, however can’t be ignored.

<!-- b000579 | prose | pages [15] -->
4.4

<!-- b000580 | heading | pages [15] -->
Discussion

<!-- b000581 | prose | pages [15] -->
Depending on the model we constructed above, we can evaluate the success level of teamwork. The higher the value of performance indicators are, the higher the score S is. However, in the model discussed above, we haven’t taken the opponent into account. It’s of great signiﬁcance to clarify whether strategies are universally effective or dependent on opponents’ counter-strategies.

<!-- b000582 | prose | pages [15] -->
From the Evaluation Model we built in this section, the weights of different indica- tors are ascertained. It seems that as long as Huskies insists its strategy, which can be embodied by the ﬁve indicators, the score remains the same. However, this thought hasn’t taken opponents’ counter-strategies into consideration. We take the pressing as an example and draw the following Figure 10.

<!-- b000583 | prose | pages [15] -->
Huskies

<!-- b000584 | prose | pages [15] -->
65

<!-- b000585 | prose | pages [15] -->
60

<!-- b000586 | prose | pages [15] -->
55

<!-- b000587 | prose | pages [15] -->
50

<!-- b000588 | prose | pages [15] -->
45

<!-- b000589 | prose | pages [15] -->
40

<!-- b000590 | prose | pages [15] -->
35

<!-- b000591 | prose | pages [15] -->
30

<!-- b000592 | prose | pages [15] -->
0 1 2 3 4

<!-- b000593 | prose | pages [15] -->
Opponent

<!-- b000594 | prose | pages [15] -->
5 6 7 8 9 10

<!-- b000595 | caption | pages [15] -->
Figure 10: Comparison of Pressing

<!-- b000596 | prose | pages [15] -->
From the Evaluation Model we built in this section, the weights of different indica-

<!-- b000597 | prose | pages [15] -->
关注数学模型

<!-- b000598 | prose | pages [15] -->
tors are ascertained. It seems that as long as Huskies insists its strategy, which can be

<!-- b000599 | furniture | pages [15] -->
2

<!-- b000600 | furniture | pages [15] -->
MATHmodels

<!-- b000601 | furniture | pages [15] -->
获取更多资讯

<!-- b000602 | furniture | pages [16] -->
Team # 2006782

<!-- b000603 | furniture | pages [16] -->
Page 14 of 25

<!-- b000604 | prose | pages [16] -->
embodied by the ﬁve indicators, the score remains the same. However, this thought hasn’t taken opponents’ counter-strategies into consideration. For example, if the op- ponent’s strategy makes the degree of pressing high, which means raise the ¯xopponent, the ¯xHuskies of Huskies will decrease accordingly. That’s to say, the value of indicators will be affected by opponents’ strategy, thus inﬂuencing the score. Therefore, the strat- egy is not universally effective. Only by adjusting the strategy based on the opponents’ strategy, trying to make the total score higher or repress the score of opponents, can one team make the likelihood to win higher.

<!-- b000605 | prose | pages [16] -->
TASK 3: Advice on Improving Team Success 5

<!-- b000606 | prose | pages [16] -->
5.1 Structural Strategy Analysis

<!-- b000607 | prose | pages [16] -->
After statistics of this season, the Huskies won 13 matches, lost 15 matches and tied

<!-- b000608 | heading | pages [16] -->
10 matches in 38 games. For the team, the year-end data of this season is not ideal. In

<!-- b000609 | prose | pages [16] -->
the next season, the team needs to make a huge change.

<!-- b000610 | prose | pages [16] -->
We have conducted a detailed analysis of the team data this season. In terms of team formation, the formations used by different coaches are similar. From the data of 38 games, the main formation 4-3-3, 4-4-2, 5-3-2, each game basically changes between these three formations. In general, we use 4-3-3 to represent the team’s offense more, 4-4-2 to represent a conservative formation, and 5-3-2 to represent a more defensive formation.

<!-- b000611 | prose | pages [16] -->
Below we analyze the ﬁve performance indicators mentioned in TASK 2 to deter- mine the tactical system suitable for the current Huskies team. From the ﬁve indicators, we selected Coordination among players (an indicator of teammate teamwork), Flexibility (an indicator of offensive line diversity), and Pressing (an indicator of team offense and defense status) to explore the three formations. Fitness for the team. We use indicators to determine the ﬁtness of the three formations for the team separately.

<!-- b000612 | caption | pages [16] -->
Table 3: Fitness of the three formations for the Huskies

<!-- b000613 | prose | pages [16] -->
Coordination Formation

<!-- b000614 | prose | pages [16] -->
4-3-3 5.1043 4-4-2 6.0104 5-3-2 7.5032

<!-- b000615 | prose | pages [16] -->
Flexibility Pressing

<!-- b000616 | prose | pages [16] -->
32.42 42.37 40.88 43.58 23.50 49.67

<!-- b000617 | prose | pages [16] -->
As is shown in Table 3, the most suitable tactical formation for Huskies last season was 5-3-2.

<!-- b000618 | prose | pages [16] -->
• In this defense-based formation, the team’s teamwork and offensive oppression are the highest, and it is the most effective strategy for now.

<!-- b000619 | prose | pages [16] -->
• However, this form of attack is not ﬂexible enough, and the oppression is also very poor. It is almost oppressed by its opponents in its own half.

<!-- b000620 | prose | pages [16] -->
So for Huskies at present, it is urgent to improve the offensive ability to win the match.

<!-- b000621 | prose | pages [16] -->
In summary, the Huskies need to give play to the characteristics of good defense, and

<!-- b000622 | prose | pages [16] -->
关注数学模型

<!-- b000623 | prose | pages [16] -->
strengthen the team’s offensive capabilities. There are many classic football strategies,

<!-- b000624 | furniture | pages [16] -->
2

<!-- b000625 | furniture | pages [16] -->
MATHmodels

<!-- b000626 | furniture | pages [16] -->
获取更多资讯

<!-- b000627 | furniture | pages [17] -->
Team # 2006782

<!-- b000628 | furniture | pages [17] -->
Page 15 of 25

<!-- b000629 | prose | pages [17] -->
such as Tiki-Taka (Barcelona), and Total Football (Netherlands). Considering the actual situation of the Huskies, the most effective strategy is Defensive counterattack.

<!-- b000630 | prose | pages [17] -->
Comparison with Italy National Team 5.2

<!-- b000631 | prose | pages [17] -->
There are many teams that use defensive counterattacks in football, such as Real Madrid and Atlético Madrid. Here we choose Italy National Team which play the defensive counterattack to the extreme peak, and selected the classic battle - 2012 Euro-

<!-- b000632 | prose | pages [17] -->
[7], and compared with average match

<!-- b000633 | prose | pages [17] -->
pean Cup semi-ﬁnal Italy v.s. Germany match data

<!-- b000634 | prose | pages [17] -->
data of the Huskies in this season.

<!-- b000635 | prose | pages [17] -->
ITALY HUSKIES

<!-- b000636 | prose | pages [17] -->
Ball Control Rate 43.8%

<!-- b000637 | prose | pages [17] -->
11

<!-- b000638 | prose | pages [17] -->
27.4%

<!-- b000639 | prose | pages [17] -->
Shot 18

<!-- b000640 | prose | pages [17] -->
Success Duel 19 10

<!-- b000641 | prose | pages [17] -->
Offside 2

<!-- b000642 | prose | pages [17] -->
0

<!-- b000643 | prose | pages [17] -->
8

<!-- b000644 | prose | pages [17] -->
Foul 23

<!-- b000645 | prose | pages [17] -->
Coordination 14.39 5.37

<!-- b000646 | prose | pages [17] -->
Flexibility 124.35 30.27

<!-- b000647 | prose | pages [17] -->
Pressing 55.32 45.96

<!-- b000648 | caption | pages [17] -->
Figure 11: Comparison with Italy National Team

<!-- b000649 | prose | pages [17] -->
From the data in Figure 11, we can ﬁnd that when facing opponents that are stronger than themselves theoretically, such as Italy (FIFA World Ranking 14th) v.s. Germany (FIFA World Ranking 1st), whether it is in the case of Ball control rate, or shot is not dominant, still won the match 2-1. The winning experience of the Italy is the ﬂexible

<!-- b000650 | prose | pages [17] -->
[8].

<!-- b000651 | prose | pages [17] -->
change of formation and the effective counterattack strategy

<!-- b000652 | prose | pages [17] -->
Below we comment on Huskies’ performance in this season.

<!-- b000653 | prose | pages [17] -->
• The value of Coordination has been low, the team’s cooperation lacking, resulting in a large number of Offside and Foul, unable to play a threatening cooperation.

<!-- b000654 | prose | pages [17] -->
• The number of Flexibility is not high enough. The team’s offensive line is actually more simplistic. The tactics of the midﬁeld straight out of the penalty zone cannot guarantee the goal rate and attack efﬁciency. The Huskies must choose to start from a wide open area.

<!-- b000655 | prose | pages [17] -->
• The Pressing value shows that the team is too conservative in defense. Most of the time it has been active in its own half, staying away from the opponent’s goal, it is difﬁcult to pose a threat, which reﬂects the lack of offensive organization ability of the team.

<!-- b000656 | prose | pages [17] -->
In summary, in the change of next season, we should mainly consider the three indicators of Coordination, Flexibility and Pressing, improve the diversiﬁcation of the team’s offensive methods, and defensive counterattack with efﬁcient and threatening organizations.

<!-- b000657 | prose | pages [17] -->
关注数学模型

<!-- b000658 | furniture | pages [17] -->
2

<!-- b000659 | furniture | pages [17] -->
MATHmodels

<!-- b000660 | furniture | pages [17] -->
获取更多资讯

<!-- b000661 | furniture | pages [18] -->
Team # 2006782

<!-- b000662 | prose | pages [18] -->
5.3 Advise on next Season

<!-- b000663 | furniture | pages [18] -->
Page 16 of 25

<!-- b000664 | prose | pages [18] -->
After analyzing our team’s network and strategy this season, in order to achieve successful teamwork and better team performance next season, the changes that the team needs to make now are:

<!-- b000665 | prose | pages [18] -->
Change 1: Adjusted the formation to a more ﬂexible formation

<!-- b000666 | prose | pages [18] -->
From the data of this season, we can see that the team is good at defending this work, but the cooperation is not enough. So we will choose 4-1-3-2 as the team’s main formation next season. It is ﬂexible and can be evolved into 5-3-2 and 4-3-3.

<!-- b000667 | prose | pages [18] -->
Change 2: Highlight the importance of core players

<!-- b000668 | prose | pages [18] -->
In team cooperation, we must make the best use of every character in the team to maximize their value. From the situation of last season, M2 and F1, F2 should be the core points of the offense. When M2 holds the ball, it should The deformed formation is 5-3-2 or 4-3-3 to protect M2 players from holding the ball. F1 and F2 should ﬁnd more neutral and running positions in the frontcourt to respond to the midﬁeld pass.

<!-- b000669 | prose | pages [18] -->
Change 3: Coherence of possession and defense

<!-- b000670 | prose | pages [18] -->
The key to the 4-1-3-2 formation of ball control is not multi-ball control, but to control the ball on the center line of the court as far as possible, where Advance attack, retreat defend.

<!-- b000671 | caption | pages [18] -->
Figure 12: A schematic diagram of Defensive counterattack

<!-- b000672 | prose | pages [18] -->
As is shown in Figure 12, the white dotted line represents the player’s moving route. Adapt to the player’s moving route, the 4-1-3-2 formation can be changed to 5-3-2, 4-3-3, 4-3-1-2 and other formations according to the situation on the court or the op- ponent’s strategy. The red solid line represents the team’s pass line when attacking. The

<!-- b000673 | prose | pages [18] -->
关注数学模型

<!-- b000674 | prose | pages [18] -->
initiator of the attack is usually organized by M2. At this time, M1 and M3 need to back

<!-- b000675 | furniture | pages [18] -->
2

<!-- b000676 | furniture | pages [18] -->
MATHmodels

<!-- b000677 | furniture | pages [18] -->
获取更多资讯

<!-- b000678 | furniture | pages [19] -->
Team # 2006782

<!-- b000679 | furniture | pages [19] -->
Page 17 of 25

<!-- b000680 | prose | pages [19] -->
up and protect M2 to control the ball, or insert to create an offensive opportunity. The yellow solid line represents the passing route when defensive is needed or when there is no good offensive neutral, increases the ball control rate, and stabilizes the ball right near the center axis. The yellow Warning sign barrel represents the position that the re- turning player needs to return. The orange ﬂag bucket represents where the offensive player can launch a threatening attack.

<!-- b000681 | prose | pages [19] -->
TASK 4: How to Design more Effective Teams 6

<!-- b000682 | prose | pages [19] -->
6.1

<!-- b000683 | heading | pages [19] -->
Generalization of our Model

<!-- b000684 | prose | pages [19] -->
In a gesture to design more effective teams, we can generalize our model to other practical teamwork. It is of great signiﬁcance to understanding the complex set of factors that make some groups perform better than others. In this chapter, we make several analogies to the indicators we used in the team sport model.

<!-- b000685 | prose | pages [19] -->
• Coordination among teammates

<!-- b000686 | prose | pages [19] -->
B

<!-- b000687 | prose | pages [19] -->
A

<!-- b000688 | prose | pages [19] -->
D

<!-- b000689 | prose | pages [19] -->
C

<!-- b000690 | caption | pages [19] -->
Figure 13: Coordination among teammates

<!-- b000691 | prose | pages [19] -->
Similar to the connection between players, the closeness of connection between colleagues is also an important indicator of teamwork. In terms of the coordination among teammates, we can use the informational passing distance d to quantify this pa- rameter, which means the number of the teammates the instruction get through when it is being passed between the team. Just as Figure 13 shows.

<!-- b000692 | prose | pages [19] -->
The distance between A and B is 1, while A is 3 away from C. Then we can get a similar network matrix like passing matrix. In this way, cluster coefﬁcient can also be used here to quantify the coordination among teammates.

<!-- b000693 | prose | pages [19] -->
• Distribution of contributions

<!-- b000694 | prose | pages [19] -->
For teamwork, a reasonable and appropriate division of labor is also an important indicator of cooperation efﬁciency. In teamwork, everyone should perform his or her own duties to promote strengths and avoid weaknesses.

<!-- b000695 | prose | pages [19] -->
Unlike football games where contribution can be easily divided into two aspects, offence and defense, the contribution in other teamwork is more complex. Each team- mate has his or her own position and performance evaluation criteria. Therefore, for people in different position the quantiﬁcation rules vary from each other.

<!-- b000696 | prose | pages [19] -->
• Flexibility

<!-- b000697 | prose | pages [19] -->
In teamwork, it is inevitable that we will encounter difﬁculties and setbacks. At this time, we need to be ﬂexible to make changes and try boldly. The Huskies performed poorly with the 4-3-3 formation in the 9th match, but later quickly changed to reverse the situation.

<!-- b000698 | prose | pages [19] -->
关注数学模型

<!-- b000699 | prose | pages [19] -->
With reference to the variety of attack strategy, we can make an analogy to the

<!-- b000700 | furniture | pages [19] -->
2

<!-- b000701 | furniture | pages [19] -->
MATHmodels

<!-- b000702 | furniture | pages [19] -->
获取更多资讯

<!-- b000703 | furniture | pages [20] -->
Team # 2006782

<!-- b000704 | furniture | pages [20] -->
Page 18 of 25

<!-- b000705 | prose | pages [20] -->
standard deviation of x-coordinate value where each passing event happens. For each team, the ﬁnal target may be unique, but the plan isn’t limited. Consequently, we can use the standard deviation of the number of people dispatched to different plans to quantify the ﬂexibility.

<!-- b000706 | prose | pages [20] -->
6.2 Other Aspects

<!-- b000707 | prose | pages [20] -->
Considering the complexity in other practical teamwork, we need to take more aspects into consideration to develop generalized models of team performance.

<!-- b000708 | prose | pages [20] -->
• Ideal leadership style

<!-- b000709 | prose | pages [20] -->
Each team has one leader, who help leverage the skills of all their teammates and make overall plan. A good leader can make teamwork more efﬁcient. Therefore, it is important to evaluate the leadership and leadership style.

<!-- b000710 | prose | pages [20] -->
There are many leadership styles. A leader will lead several people directly or indirectly. We can use the distance to quantify the leader’s leadership intensity I as the formula shows:

<!-- b000711 | prose | pages [20] -->
∑

<!-- b000712 | prose | pages [20] -->
l =

<!-- b000713 | prose | pages [20] -->
N N

<!-- b000714 | prose | pages [20] -->
1

<!-- b000715 | prose | pages [20] -->
.

<!-- b000716 | prose | pages [20] -->
(16)

<!-- b000717 | prose | pages [20] -->
dN

<!-- b000718 | prose | pages [20] -->
i=1 i=1

<!-- b000719 | prose | pages [20] -->
Where N is the total number of people the leader leads, and dN is the distance between the person and the leader. The management scientists make out a leadership intensity

<!-- b000720 | prose | pages [20] -->
[9]. When this leadership strength is exceeded, the leader will be tired in the

<!-- b000721 | prose | pages [20] -->
standard

<!-- b000722 | prose | pages [20] -->
management process. On the contrary, when the management intensity is too low, the managerial talents are not fully applied, which causes the idleness of human capital. Therefore, building a leadership model and choosing the ideal leadership style also play a dominant role.

<!-- b000723 | prose | pages [20] -->
• Effective coordination over time

<!-- b000724 | prose | pages [20] -->
The effective coordination can be expressed as follow:

<!-- b000725 | prose | pages [20] -->
∑

<!-- b000726 | prose | pages [20] -->
i=1

<!-- b000727 | prose | pages [20] -->
E =

<!-- b000728 | prose | pages [20] -->
N N

<!-- b000729 | prose | pages [20] -->
twork

<!-- b000730 | prose | pages [20] -->
.

<!-- b000731 | prose | pages [20] -->
(17)

<!-- b000732 | prose | pages [20] -->
ttotal

<!-- b000733 | prose | pages [20] -->
Where twork is the total time one person working, and ttotal is the total duration of the entire cooperation.

<!-- b000734 | prose | pages [20] -->
For example in football game, as one player steals the ball from an opponent, an- other player is poised for offense. Their total working time is deﬁnitely larger than the time the whole event takes, which means they have higher effectivity. In comparison, we can also use this method to quantify the effective coordination over time.

<!-- b000735 | heading | pages [20] -->
Analysis on Model’s Sensitivity

<!-- b000736 | prose | pages [20] -->
7

<!-- b000737 | heading | pages [20] -->
Evaluation Model sensitivity to Draw situations

<!-- b000738 | prose | pages [20] -->
7.1

<!-- b000739 | prose | pages [20] -->
When studying the Evaluation model in TASK 2, we dealt with the situation when

<!-- b000740 | prose | pages [20] -->
关注数学模型

<!-- b000741 | prose | pages [20] -->
the two teams were tied by absolute difference. When the difference in absolute value

<!-- b000742 | furniture | pages [20] -->
2

<!-- b000743 | furniture | pages [20] -->
MATHmodels

<!-- b000744 | furniture | pages [20] -->
获取更多资讯

<!-- b000745 | furniture | pages [21] -->
Team # 2006782

<!-- b000746 | furniture | pages [21] -->
Page 19 of 25

<!-- b000747 | prose | pages [21] -->
of evaluation score S is less than 1, we regard this situation as the indicator passed. Next, we will study the inﬂuence of the constraints on the difference between the scores of the two teams (error limit) on the weight value βi in the model.

<!-- b000748 | prose | pages [21] -->
We let |S1 −S2| < ε, where error limit ε ∈[0, 2]. We substitute the error limit into the model algorithm, calculate the value of each weight βi under different error limit ε, and calculate the lowestError. Finally, we draw a visual smooth curve like Figure 14.

<!-- b000749 | prose | pages [21] -->
b1

<!-- b000750 | prose | pages [21] -->
β1

<!-- b000751 | prose | pages [21] -->
0.9

<!-- b000752 | prose | pages [21] -->
b2

<!-- b000753 | prose | pages [21] -->
β2

<!-- b000754 | prose | pages [21] -->
0.8

<!-- b000755 | prose | pages [21] -->
b3

<!-- b000756 | prose | pages [21] -->
Performance Indicators

<!-- b000757 | prose | pages [21] -->
β3

<!-- b000758 | prose | pages [21] -->
0.7

<!-- b000759 | prose | pages [21] -->
b4

<!-- b000760 | prose | pages [21] -->
β4

<!-- b000761 | prose | pages [21] -->
0.6

<!-- b000762 | prose | pages [21] -->
b5

<!-- b000763 | prose | pages [21] -->
β5

<!-- b000764 | prose | pages [21] -->
0.5

<!-- b000765 | prose | pages [21] -->
0.4

<!-- b000766 | prose | pages [21] -->
0.3

<!-- b000767 | prose | pages [21] -->
0.2

<!-- b000768 | prose | pages [21] -->
0.1

<!-- b000769 | prose | pages [21] -->
0

<!-- b000770 | prose | pages [21] -->
-0.1

<!-- b000771 | prose | pages [21] -->
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1

<!-- b000772 | prose | pages [21] -->
e

<!-- b000773 | prose | pages [21] -->
0.2

<!-- b000774 | prose | pages [21] -->
0.15

<!-- b000775 | prose | pages [21] -->
LowestError

<!-- b000776 | prose | pages [21] -->
0.1

<!-- b000777 | prose | pages [21] -->
0.05

<!-- b000778 | prose | pages [21] -->
0

<!-- b000779 | prose | pages [21] -->
1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9 2

<!-- b000780 | caption | pages [21] -->
Figure 14: Five performance indicators and lowestError with different error limit ε

<!-- b000781 | prose | pages [21] -->
In Figure 14, we can see that when ε < 1, the lowestError has been kept at a low level. However, at this time the weights of the ﬁve indicators of the model have been in a chaotic state and cannot reﬂect the reality and the importance of the indicators. When ε > 1, the weight of each indicator is relatively stable. At this time, we must also consider the value of lowestError, and the deviation should not be too large. It can be seen that when ε = 1, 1.5, 1.8, it is more reasonable as a tie. So our model is more sensitive to the situation of a draw.

<!-- b000782 | prose | pages [21] -->
Analysis on performance indicator Tempo 7.2

<!-- b000783 | prose | pages [21] -->
In Task 2, the quantitative indicator for reﬂecting the Tempo on the football ﬁeld is the time it takes for a player to pass 50 goals. Here we consider whether the time when players pass 10, 30, 50, 70, 90 balls can appropriately reﬂect the changing rhythm on the court. In order to make the time of different foot counts analyzable, we choose the same game time to prevent the situation where tempo cannot be compared due to different time intervals.

<!-- b000784 | prose | pages [21] -->
After our analysis of the data, we chose 46 s - 1305 s in the ﬁrst half of the match. And we removed the 10-pass and 90-pass time because their time is too short or too long to analyze the sensitivity. Through calculation, we obtain the time curve of ball passing time per 30, 50, 70 passes during this period.

<!-- b000785 | prose | pages [21] -->
As can be seen from Figure 15, when calculating the 30-pass time, the curve shows more jagged parts, that is, the tempo on the football ﬁeld has a clear turning point. This is well understood according to the actual situation of the football ﬁeld. When dividing the passing time, the tempo displayed on the court will not change much (i.e., it is difﬁcult to change the defensive or offensive rhythm within 30 feet). When calculating the 70-pass time, there is almost no change in tempo on the ﬁeld, which is obviously not reasonable. The tempo indicator in our model is sensitive to the number

<!-- b000786 | prose | pages [21] -->
关注数学模型

<!-- b000787 | furniture | pages [21] -->
2

<!-- b000788 | furniture | pages [21] -->
MATHmodels

<!-- b000789 | furniture | pages [21] -->
获取更多资讯

<!-- b000790 | furniture | pages [22] -->
Team # 2006782

<!-- b000791 | prose | pages [22] -->
900

<!-- b000792 | prose | pages [22] -->
800

<!-- b000793 | prose | pages [22] -->
700

<!-- b000794 | prose | pages [22] -->
Ball passing time

<!-- b000795 | prose | pages [22] -->
600

<!-- b000796 | prose | pages [22] -->
500

<!-- b000797 | prose | pages [22] -->
400

<!-- b000798 | prose | pages [22] -->
300

<!-- b000799 | prose | pages [22] -->
200

<!-- b000800 | prose | pages [22] -->
100

<!-- b000801 | prose | pages [22] -->
0 200 400 600

<!-- b000802 | furniture | pages [22] -->
Page 20 of 25

<!-- b000803 | prose | pages [22] -->
30 ball passing 50 ball passing 70 ball passing

<!-- b000804 | prose | pages [22] -->
800 1000 1200 1400 Time

<!-- b000805 | caption | pages [22] -->
Figure 15: Ball passing time per 30, 50, 70 passes

<!-- b000806 | prose | pages [22] -->
of passes hence. This is why the 50-pass time is the most scientiﬁc and reasonable to calculate tempo.

<!-- b000807 | prose | pages [22] -->
8

<!-- b000808 | heading | pages [22] -->
Strengths and Weaknesses

<!-- b000809 | prose | pages [22] -->
8.1

<!-- b000810 | heading | pages [22] -->
Strengths

<!-- b000811 | prose | pages [22] -->
• The selection of the network parameters of the passing network is scientiﬁc and reasonable. The network model is highly applicable and can reﬂect the charac- teristics of various aspects of the team and the evaluation scale. • The evaluation model also introduces the opponent into the evaluation system. In order to be able to compare against the Huskies team, the weight coefﬁcients of the ﬁve indicators are returned to be more scientiﬁc and reasonable. • Our model analyzes the Huskies team’s data thoroughly, ﬁnds more effective strategies for the team, proposes constructive changes, and visualizes our strate- gies.

<!-- b000812 | prose | pages [22] -->
8.2

<!-- b000813 | heading | pages [22] -->
Weaknesses

<!-- b000814 | prose | pages [22] -->
• Our model did not have enough analysis and processing for the eventsubtype part, and did not take out each team member for individual analysis. • The indicators of the popularization model cannot be quantiﬁed, resulting in a low persuasibility of the model.

<!-- b000815 | prose | pages [22] -->
关注数学模型

<!-- b000816 | furniture | pages [22] -->
2

<!-- b000817 | furniture | pages [22] -->
MATHmodels

<!-- b000818 | furniture | pages [22] -->
获取更多资讯

<!-- b000819 | furniture | pages [23] -->
Team # 2006782

<!-- b000820 | heading | pages [23] -->
References

<!-- b000821 | furniture | pages [23] -->
Page 21 of 25

<!-- b000822 | references | pages [23] -->
[1] Leighton, F. Thomson. Introduction to parallel algorithms and architectures: array,

<!-- b000823 | references | pages [23] -->
trees, hypercubes. 2014.

<!-- b000824 | references | pages [23] -->
[2] Clemente, Filipe Manuel, et al. "General network analysis of national soccer teams

<!-- b000825 | references | pages [23] -->
in FIFA World Cup 2014." International Journal of Performance Analysis in Sport 15.1

<!-- b000826 | references | pages [23] -->
(2015): 80-96.

<!-- b000827 | references | pages [23] -->
[3] Dijkstra, Edsger Wybe. "A Note on Two Problems in Connexion With Graphs."

<!-- b000828 | references | pages [23] -->
Numerische Mathematik 1(1959):269-271.

<!-- b000829 | references | pages [23] -->
[4] Ahnert, Sebastian E., et al. "Ensemble approach to the analysis of weighted net-

<!-- b000830 | references | pages [23] -->
works.." Physical Review E 76.1 (2007).

<!-- b000831 | references | pages [23] -->
[5] Wong, J. A. Hartiganm. A. . "Algorithm AS 136:

<!-- b000832 | references | pages [23] -->
A K-Means Clustering

<!-- b000833 | references | pages [23] -->
Algorithm." Journal of the Royal Statistical Society. Series C (Applied Statistics)

<!-- b000834 | references | pages [23] -->
28.1(1979):100-108.

<!-- b000835 | references | pages [23] -->
[6] Buldu, J. M., et al. "Deﬁning a historic football team: Using Network Science to

<!-- b000836 | references | pages [23] -->
analyze Guardiolas F.C. Barcelona." Scientiﬁc Reports 9.1 (2019): 1-14.

<!-- b000837 | references | pages [23] -->
[7] Balotelli sends Italy past Germany. (2012). Retrieved December 10, 2014, from

<!-- b000838 | references | pages [23] -->
https://www.uefa.com/uefaeuro/season=2012/matches/round=

<!-- b000839 | references | pages [23] -->
15174/match=2003379/index.html

<!-- b000840 | references | pages [23] -->
[8] Sigari, Mohamad Hoseyn, et al. "Counterattack detection in broadcast soccer

<!-- b000841 | references | pages [23] -->
videos using camera motion estimation." international symposium on artiﬁcial in-

<!-- b000842 | references | pages [23] -->
telligence (2015): 101-106.

<!-- b000843 | references | pages [23] -->
[9] Abdelmahmoud Hassan Elsheikh. Effect of Leadership Intensity on Integrating Some

<!-- b000844 | references | pages [23] -->
Formal and Informal Organizational Efforts for Community Development in Khartoum

<!-- b000845 | references | pages [23] -->
Province. 2016.

<!-- b000846 | references | pages [23] -->
关注数学模型

<!-- b000847 | furniture | pages [23] -->
2

<!-- b000848 | furniture | pages [23] -->
MATHmodels

<!-- b000849 | furniture | pages [23] -->
获取更多资讯

<!-- b000850 | furniture | pages [24] -->
Team # 2006782

<!-- b000851 | heading | pages [24] -->
Appendix: Code

<!-- b000852 | prose | pages [24] -->
TASK 1 - matrix.m

<!-- b000853 | prose | pages [24] -->
clear,clc w=zeros(11,11); data=xlsread(’MatchID1.xlsx’); [m,n]=size(data);

<!-- b000854 | furniture | pages [24] -->
Page 22 of 25

<!-- b000855 | prose | pages [24] -->
%% Calculate the number of passing balls between each player for i=1:1:m

<!-- b000856 | prose | pages [24] -->
w(data(i,1),data(i,2))=w(data(i,1),data(i,2))+data(i,3); w(data(i,2),data(i,1))=w(data(i,2),data(i,1))+data(i,3); end for i=1:1:11

<!-- b000857 | prose | pages [24] -->
w(i,i)=0; end w %% Calculate the Total Link L=0; for i=1:1:11

<!-- b000858 | prose | pages [24] -->
for j=1:1:11

<!-- b000859 | prose | pages [24] -->
L=L+w(i,j); end end L=L/2 %% Calculate the density of match pho=2*L/(n*(n-1)) %% Calculate the topological distance d=zeros(11,11)-1; for i=1:1:11

<!-- b000860 | prose | pages [24] -->
for j=1:1:11

<!-- b000861 | prose | pages [24] -->
if w(i,j)~=0

<!-- b000862 | prose | pages [24] -->
d(i,j)=1./w(i,j); end end end d %% Calculate the matrix of distance D=0; for i=1:1:11

<!-- b000863 | prose | pages [24] -->
for j=1:1:11

<!-- b000864 | prose | pages [24] -->
if d(i,j)>D

<!-- b000865 | prose | pages [24] -->
D=d(i,j); end end end D %% Calculate the cluster coeffient of each player Cw=zeros(11,1); for i=1:1:11

<!-- b000866 | prose | pages [24] -->
s=0; for j=1:1:11

<!-- b000867 | prose | pages [24] -->
for k=1:1:11

<!-- b000868 | prose | pages [24] -->
if i~=j && j~=k && i~=k

<!-- b000869 | prose | pages [24] -->
Cw(i)=Cw(i)+w(i,j)*w(j,k)*w(i,k); end if i~=j && i~=k

<!-- b000870 | prose | pages [24] -->
s=s+w(i,j)*w(i,k); end

<!-- b000871 | prose | pages [24] -->
关注数学模型

<!-- b000872 | furniture | pages [24] -->
2

<!-- b000873 | furniture | pages [24] -->
MATHmodels

<!-- b000874 | furniture | pages [24] -->
获取更多资讯

<!-- b000875 | furniture | pages [25] -->
Team # 2006782

<!-- b000876 | prose | pages [25] -->
end end Cw(i)=Cw(i)/s; end Cw %% Calculate the cluster coeffient C=0; for i=1:1:11

<!-- b000877 | prose | pages [25] -->
C=C+Cw(i); end C=C/11

<!-- b000878 | prose | pages [25] -->
TASK 1 - passingtime.m

<!-- b000879 | prose | pages [25] -->
clear,clc time=xlsread(’passingtime.xlsx’); t=[];t_s=[]; i=1;k=0;

<!-- b000880 | furniture | pages [25] -->
Page 23 of 25

<!-- b000881 | prose | pages [25] -->
%% Calculate the time of 50 passing ball [m,n]=size(time); while time(i,1)==1

<!-- b000882 | prose | pages [25] -->
k=k+1; t(k)=time(i+49,2)-time(i,2); t_s(k,1)=time(i,2);t_s(k,2)=time(i+49,2); i=i+50; if time(i+49,1)~=1

<!-- b000883 | prose | pages [25] -->
break end end % Judge the half part of the match while time(i,1)==1

<!-- b000884 | prose | pages [25] -->
i=i+1; end while time(i,1)==2

<!-- b000885 | prose | pages [25] -->
k=k+1; t(k)=time(i+49,2)-time(i,2); t_s(k,1)=time(i,2);t_s(k,2)=time(i+49,2); i=i+50; if i+49>m

<!-- b000886 | prose | pages [25] -->
break end end

<!-- b000887 | prose | pages [25] -->
%% Calculate the number of passing balls in 10 minutes of the overall match % [n,q]=size(time); % t=10; % i=1;p=[];k=0; % while time(i,1)==1 % if time(i,2)-time(1,2)>(k+1)*t*60 % k=k+1; % if k==1 % p(k)=i; % else % p(k)=i-sum(p); % end % end % i=i+1; % end % j=i;m=k; % while time(i,1)==2

<!-- b000888 | prose | pages [25] -->
关注数学模型

<!-- b000889 | furniture | pages [25] -->
2

<!-- b000890 | furniture | pages [25] -->
MATHmodels

<!-- b000891 | furniture | pages [25] -->
获取更多资讯

<!-- b000892 | furniture | pages [26] -->
Team # 2006782

<!-- b000893 | furniture | pages [26] -->
Page 24 of 25

<!-- b000894 | prose | pages [26] -->
if time(i,2)-time(j,2)>(k-m+1)*60*t % % k=k+1; % p(k)=i-sum(p); % end % i=i+1; % if i>n % break % end % end

<!-- b000895 | prose | pages [26] -->
TASK 2 - AdversarialRegression.py

<!-- b000896 | prose | pages [26] -->
import numpy as np import pandas as pd

<!-- b000897 | prose | pages [26] -->
def writeTxt(result1, result2, fileName):

<!-- b000898 | prose | pages [26] -->
f = open(fileName,’a’) for ele in result1:

<!-- b000899 | prose | pages [26] -->
f.write(str(ele)+’ ’) f.write(str(result2)) f.write(’\n’)

<!-- b000900 | prose | pages [26] -->
def read_csv(filename):

<!-- b000901 | prose | pages [26] -->
read_file = pd.read_csv(filename, header = None) read_file = np.array(read_file) return read_file

<!-- b000902 | prose | pages [26] -->
def panduan(w,re,vec_one,vec_two,m):

<!-- b000903 | prose | pages [26] -->
flag=1 for i in range(m):

<!-- b000904 | prose | pages [26] -->
if re[i]==1:

<!-- b000905 | prose | pages [26] -->
y1=np.dot(vec_one[i],w) y2=np.dot(vec_two[i],w) if y1<y2:

<!-- b000906 | prose | pages [26] -->
flag=0 break elif re[i]==-1:

<!-- b000907 | prose | pages [26] -->
y1=np.dot(vec_one[i],w) y2=np.dot(vec_two[i],w) if y1>y2:

<!-- b000908 | prose | pages [26] -->
flag=0 break else:

<!-- b000909 | prose | pages [26] -->
y1=np.dot(vec_one[i],w) y2=np.dot(vec_two[i],w) if abs(y1-y2)>1:

<!-- b000910 | prose | pages [26] -->
flag=0 break return flag

<!-- b000911 | prose | pages [26] -->
def lowestError(w,vec_one,vec_two,m):

<!-- b000912 | prose | pages [26] -->
y=[] for i in range(m):

<!-- b000913 | prose | pages [26] -->
y1=np.dot(vec_one[i],w) y.append(y1) return np.var(y)

<!-- b000914 | prose | pages [26] -->
vec_one=read_csv(’Huskies.csv’) vec_two=read_csv(’Opponent.csv’) re=read_csv(’result.csv’)

<!-- b000915 | prose | pages [26] -->
关注数学模型

<!-- b000916 | furniture | pages [26] -->
2

<!-- b000917 | furniture | pages [26] -->
MATHmodels

<!-- b000918 | furniture | pages [26] -->
获取更多资讯

<!-- b000919 | furniture | pages [27] -->
Team # 2006782

<!-- b000920 | prose | pages [27] -->
fileName = "var_y.txt" m=vec_one.shape[0] k=0 for w1 in range(1,10):

<!-- b000921 | prose | pages [27] -->
for w2 in range(1,10):

<!-- b000922 | prose | pages [27] -->
for w3 in range(1,10):

<!-- b000923 | prose | pages [27] -->
for w4 in range(1,10):

<!-- b000924 | furniture | pages [27] -->
Page 25 of 25

<!-- b000925 | prose | pages [27] -->
for w5 in range(1,10):

<!-- b000926 | prose | pages [27] -->
w=np.array([w1,w2,w3,w4,w5])*0.1 print(w) if panduan(w,re,vec_one,vec_two,m):

<!-- b000927 | prose | pages [27] -->
s=lowestError(w,vec_one,vec_two,m) k=k+1 writeTxt(w,s,fileName) else:

<!-- b000928 | prose | pages [27] -->
w=[]

<!-- b000929 | prose | pages [27] -->
# for j in range(20): # for w1 in range(1,10): # for w2 in range(1,10): # for w3 in range(1,10):

<!-- b000930 | prose | pages [27] -->
for w4 in range(1,10): # for w5 in range(1,10): # w=np.array([w1,w2,w3,w4,w5])*0.1 # # print(w) if panduan(w,re,vec_one,vec_two,m,j): # s=lowestError(w,vec_one,vec_two,m) # # k=k+1 writeTxt(w,s,fileName) # # else: # w=[]

<!-- b000931 | heading | pages [27] -->
print("sum of result:")

<!-- b000932 | prose | pages [27] -->
print(k)

<!-- b000933 | prose | pages [27] -->
关注数学模型

<!-- b000934 | furniture | pages [27] -->
2

<!-- b000935 | furniture | pages [27] -->
MATHmodels

<!-- b000936 | furniture | pages [27] -->
获取更多资讯
