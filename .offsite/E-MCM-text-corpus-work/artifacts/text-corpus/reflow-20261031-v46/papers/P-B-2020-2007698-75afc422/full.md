# P-B-2020-2007698-75afc422

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Problem Chosen

<!-- b000002 | furniture | pages [1] -->
2020

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | prose | pages [1] -->
MCM

<!-- b000005 | title | pages [1] -->
B

<!-- b000006 | furniture | pages [1] -->
2007698

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
A Simulation Based Assessment of Sandcastle

<!-- b000009 | title | pages [1] -->
Foundation

<!-- b000010 | heading | pages [1] -->
Summary

<!-- b000011 | prose | pages [1] -->
Sandcastle building is a common way to recreating for beach goers. Sand lovers always rack their brains to build a stronger castle and take pride in it. Still, sandcas- tle is inevitably eroded by the waves and tides. Therefore, how to establish a stable foundation is of great signiﬁcance to the duration of sand castles.

<!-- b000012 | prose | pages [1] -->
In order to explore the most stable three-dimensional geometric shape, we establish a periodic sand-water cell automaton model to experiment with the most likely mul- tiple geometric shapes. We discretize the sand base into a three-dimensional geometry consisting of a stack of rigid sand cells and water cells. Based on the knowledge of engineering mechanics and the feasibility in practice, we select ﬁve types of inertial frustum which has signiﬁcant characteristics: triangular frustum, square frustum, six- arris frustum, conical frustum, ellipse frustum and so on for simulation experiments. The optimum geometric shape we obtain is triangle frustum.

<!-- b000013 | prose | pages [1] -->
In the model, we formulate the state transition rules through multivariate analy- sis based on multi-criteria judgments, and carry out quantitative calculations on the waves’ sediment carrying and capillary phenomena between sand and water. We em- ploy complex trigonometric functions to simulate and reproduce the tidal waves in three dimensions. Therefore, through regression analysis of the data obtained from multiple experiments on each frustum, we have obtained a reliable and optimal geo- metric shape result. Besides, it can be quantiﬁed and visualized.

<!-- b000014 | prose | pages [1] -->
In the practice of building sand castles, it was found that different sand-to-water mixture ratios also played a crucial role in the sand foundations’ stability. By using the sand-water cell automaton model of problem 1, we use the concentration gradi- ent method to adjust the water-sand ratio and obtain a series of data points on the sand-to-water proportion and the sand-based stability. Then we use the least squares polynomial function approximation to ﬁt the curve of these data. Therefore, we obtain an estimated function of sand-to-water ratio and sand-base stability. Then we can ﬁnd that the optimal sand-to-water mixture proportion is 0.55.

<!-- b000015 | prose | pages [1] -->
In order to study rain’s effect on the result, we introduce a rainfall module based on the original model. It will work on the sandy base with the wave tide module. Similarly, we get a series of data for regression analysis. We ﬁnd that the original best geometry does not the only one which perform well under rainfall conditions, and ellipse frustum is the another better geometry when it is rainy.

<!-- b000016 | prose | pages [1] -->
Sensitivity analysis shows the strong robustness of our model. Meanwhile, we also propose some other strategies for increasing the stability of the sandy base. Subse- quently, we summarize the experimental models and conclusions into plain language for publication on Fun in the Sun.

<!-- b000017 | prose | pages [1] -->
In addition, our model is easy to implement and extend. By changing few parame- ters in our code, we can stimulate more complex conditions on the beach.

<!-- b000018 | keywords | pages [1] -->
Keywords: periodic sand-water cell automaton model, multivariate analysis, quantiﬁed

<!-- b000019 | prose | pages [1] -->
and visualized, concentration gradient method 关注数学模型

<!-- b000020 | furniture | pages [1] -->
2

<!-- b000021 | furniture | pages [1] -->
MATHmodels

<!-- b000022 | furniture | pages [1] -->
获取更多资讯

<!-- b000023 | heading | pages [2] -->
Contents

<!-- b000024 | contents | pages [2] -->
1 Introduction

<!-- b000025 | contents | pages [2] -->
2

<!-- b000026 | contents | pages [2] -->
1.1

<!-- b000027 | contents | pages [2] -->
Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000028 | contents | pages [2] -->
2

<!-- b000029 | contents | pages [2] -->
1.2

<!-- b000030 | contents | pages [2] -->
Literature Review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000031 | contents | pages [2] -->
2

<!-- b000032 | contents | pages [2] -->
1.3

<!-- b000033 | contents | pages [2] -->
Our work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000034 | contents | pages [2] -->
3

<!-- b000035 | contents | pages [2] -->
2 Preparation of the Models

<!-- b000036 | contents | pages [2] -->
3

<!-- b000037 | contents | pages [2] -->
2.1

<!-- b000038 | contents | pages [2] -->
Analysis of Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000039 | contents | pages [2] -->
3

<!-- b000040 | contents | pages [2] -->
2.2

<!-- b000041 | contents | pages [2] -->
Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000042 | contents | pages [2] -->
4

<!-- b000043 | contents | pages [2] -->
2.3

<!-- b000044 | contents | pages [2] -->
Notations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000045 | contents | pages [2] -->
4

<!-- b000046 | contents | pages [2] -->
3 The Optimal 3D Geometric Shape

<!-- b000047 | contents | pages [2] -->
5

<!-- b000048 | contents | pages [2] -->
3.1

<!-- b000049 | contents | pages [2] -->
Model Preparation

<!-- b000050 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000051 | contents | pages [2] -->
5

<!-- b000052 | contents | pages [2] -->
3.1.1

<!-- b000053 | contents | pages [2] -->
Model Principle . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000054 | contents | pages [2] -->
5

<!-- b000055 | contents | pages [2] -->
3.1.2

<!-- b000056 | contents | pages [2] -->
Model Assumption . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000057 | contents | pages [2] -->
5

<!-- b000058 | contents | pages [2] -->
3.1.3

<!-- b000059 | contents | pages [2] -->
Model Construction

<!-- b000060 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000061 | contents | pages [2] -->
6

<!-- b000062 | contents | pages [2] -->
3.1.4

<!-- b000063 | contents | pages [2] -->
The Rules

<!-- b000064 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000065 | contents | pages [2] -->
6

<!-- b000066 | contents | pages [2] -->
3.1.5

<!-- b000067 | contents | pages [2] -->
The Steps of the Algorithm

<!-- b000068 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . .

<!-- b000069 | contents | pages [2] -->
8

<!-- b000070 | contents | pages [2] -->
Estimation of P and M . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000071 | contents | pages [2] -->
3.1.6

<!-- b000072 | contents | pages [2] -->
8

<!-- b000073 | contents | pages [2] -->
3.2

<!-- b000074 | contents | pages [2] -->
Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000075 | contents | pages [2] -->
9

<!-- b000076 | contents | pages [2] -->
4 The Optimal Sand-to-Water Mixture Proportion

<!-- b000077 | contents | pages [2] -->
11

<!-- b000078 | contents | pages [2] -->
4.1

<!-- b000079 | contents | pages [2] -->
Model Preparation

<!-- b000080 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000081 | contents | pages [2] -->
11

<!-- b000082 | contents | pages [2] -->
4.1.1

<!-- b000083 | contents | pages [2] -->
The Principle of Model . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000084 | contents | pages [2] -->
11

<!-- b000085 | contents | pages [2] -->
4.1.2

<!-- b000086 | contents | pages [2] -->
The Steps of Algorithm

<!-- b000087 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000088 | contents | pages [2] -->
11

<!-- b000089 | contents | pages [2] -->
4.2

<!-- b000090 | contents | pages [2] -->
Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000091 | contents | pages [2] -->
12

<!-- b000092 | contents | pages [2] -->
5 The Optimal Shape in Rainy Day

<!-- b000093 | contents | pages [2] -->
13

<!-- b000094 | contents | pages [2] -->
5.1

<!-- b000095 | contents | pages [2] -->
Modiﬁed CA Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000096 | contents | pages [2] -->
13

<!-- b000097 | contents | pages [2] -->
5.1.1

<!-- b000098 | contents | pages [2] -->
Model Assumption . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000099 | contents | pages [2] -->
13

<!-- b000100 | contents | pages [2] -->
5.1.2

<!-- b000101 | contents | pages [2] -->
Similarities and Difference from Basic Model . . . . . . . . . . . .

<!-- b000102 | contents | pages [2] -->
13

<!-- b000103 | contents | pages [2] -->
5.1.3

<!-- b000104 | contents | pages [2] -->
The Steps of Algorithm

<!-- b000105 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000106 | contents | pages [2] -->
13

<!-- b000107 | contents | pages [2] -->
5.2

<!-- b000108 | contents | pages [2] -->
Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000109 | contents | pages [2] -->
14

<!-- b000110 | contents | pages [2] -->
6 Sensitivity Analysis

<!-- b000111 | contents | pages [2] -->
16

<!-- b000112 | contents | pages [2] -->
7 Strengths and Weaknesses

<!-- b000113 | contents | pages [2] -->
17

<!-- b000114 | contents | pages [2] -->
7.1

<!-- b000115 | contents | pages [2] -->
Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000116 | contents | pages [2] -->
17

<!-- b000117 | contents | pages [2] -->
7.2

<!-- b000118 | contents | pages [2] -->
Weaknesses

<!-- b000119 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000120 | contents | pages [2] -->
18

<!-- b000121 | contents | pages [2] -->
7.3

<!-- b000122 | contents | pages [2] -->
Promption . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000123 | contents | pages [2] -->
18

<!-- b000124 | contents | pages [2] -->
8 Strategies to Make sandcastle More Lasting

<!-- b000125 | contents | pages [2] -->
18

<!-- b000126 | contents | pages [2] -->
9 Conclusion

<!-- b000127 | contents | pages [2] -->
19

<!-- b000128 | contents | pages [2] -->
Article

<!-- b000129 | contents | pages [2] -->
20

<!-- b000130 | contents | pages [2] -->
References

<!-- b000131 | contents | pages [2] -->
21

<!-- b000132 | contents | pages [2] -->
Appendix: Our Code

<!-- b000133 | contents | pages [2] -->
23

<!-- b000134 | contents | pages [2] -->
关注数学模型

<!-- b000135 | furniture | pages [2] -->
2

<!-- b000136 | furniture | pages [2] -->
MATHmodels

<!-- b000137 | furniture | pages [2] -->
获取更多资讯

<!-- b000138 | furniture | pages [3] -->
Team # 2007698

<!-- b000139 | furniture | pages [3] -->
Page 2 of 29

<!-- b000140 | heading | pages [3] -->
1 Introduction

<!-- b000141 | heading | pages [3] -->
1.1 Problem Background

<!-- b000142 | prose | pages [3] -->
Playing is the nature of human, but it is not easy to get some kind of inspiration while playing. There are castles of various shapes on the beach, either simple or deli- cate. Even under the same condition, some castles can be maintained for a long time, while some castles can’t withstand a wave and disappear without a trace. How to make our castles more durable is a question that most poeple are curious about. There are many factors which inﬂuence the ﬁrmness of sandcastles, such as sand-to-water mixture proportion, the type of sand, weather etc.

<!-- b000143 | prose | pages [3] -->
In this paper, we attempt to explore a three-dimensional geometric model of a sand- castle foundation having the best stability. First, we need to build a mathematical mod- el that analyzes the optimal three-dimensional geometry shape. Second, based on this model, we are required to consider the optimal sand-to-water mixture proportion to achieve the best adhesion between the sands. Furthermore, taking the impact of the weather into consideration, we need investigate the optimal 3D geometric shape once again.

<!-- b000144 | heading | pages [3] -->
1.2 Literature Review

<!-- b000145 | prose | pages [3] -->
Since the last century, the interaction between water and sediment has been the focus of scholars in related ﬁelds. They have carried out a large number of experiments and researches to explore water-sand interactions and their effects on stability.

<!-- b000146 | prose | pages [3] -->
Sandpile problem. Mason, TG and Levine, AJ and Erta¸s, D and Halsey, TC (1999)[11] had studied the critical angle of wet sandpiles. Dumont, Serge and IGBIDA, Noured- dine (2009) [4] based on implict Euler dicretization in time, improved formula in Prigozhin model.J.P. Bouchaud, J.-P. and Cates, M. E. and Prakash, J. Ravi and Edwards, S. F. (1995) [1] propose a new continuum description of the dynamic of sandpile surfaces and found a "spinodal" angle at which the surface of sandpile will be unstable. Du- mont, Serge and Igbida, Noureddine (2011)[5] analysed this problem by using the col- lapsing model introduced by Evans.

<!-- b000147 | prose | pages [3] -->
Sediment mathematical model. Emiro˘glu, Mehmet and Yalama, Ahmet and Er- do˘gdu, Yasemin (2015)[6] explored the ratio of the water and the clay/sand to study the material’s satablity. Then they found the optimal ratio was between 0.43 and 0.66. Gröger, Torsten and Tüzün, Ugur and Heyes, David M (2003)[8] used CDEM to mea- sure od cohesion in wet granular materials and proved Rumpf’s equation’s genaral agreement.

<!-- b000148 | prose | pages [3, 4] -->
Slope stability. "Slope stability is one of the basic problems in geotechnical mechan- ics and engineering." Research on this topic is signiﬁcant for river and trafﬁc safety. Af- ter reviewing literatures, we ﬁnd that the mainstream analysis method is still around the traditional three methods: limit equilibrium, limit analysis and numerical analy- sis method. These three methods are kind of a generalization from two-dimensional to three-dimensional space, and thus have various limitations(Gao, Wang & Zhang, 2009[15]). Futhermore, more and more literatures have begun to consider changes in slope stability under different weather conditions(Yeh, Lee & Chang, 2020[14]; Chen, Liu & Li, 2020[2]). In this paper, we employ cellular automata, etc. 关注数学模型 Sandcastle problem. Halsey, Thomas C and Levine, Alex J (1997)[9] thought the capillary force signiﬁcantlly affect the sandpiles’ stability and the critical angle is costan- t in the limit of large system. Then they analyzed the reason why sandcastle will fall. Coincidently, at the same year, Hornbaker, DJ and Albert, Réka and Albert, István and Barabási, A-L and Schiffer, Peter (1997) [10] expored why sandcastles can stand and drew the conclusion that wetting liquid can change the properties of qranular me- dia resulting in a great increase of citicle angle. Fraysse, N and Thomé, H and Petit, L(1999) [7] also explored the inﬂuence of humidity on the castles’ stability. Recent year, Pakpour, Maryam and Habibi, Mehdi and Møller, Peder and Bonn, Daniel(2012) [12] demonstrated how to build the perfect castle from the prospect of sandcastles’ height.

<!-- b000149 | furniture | pages [3] -->
2

<!-- b000150 | furniture | pages [3] -->
MATHmodels

<!-- b000151 | furniture | pages [3] -->
获取更多资讯

<!-- b000152 | furniture | pages [4] -->
Team # 2007698

<!-- b000153 | furniture | pages [4] -->
Page 3 of 29

<!-- b000155 | prose | pages [4] -->
The sandcastle foundation has the same principle as the slope stability, and relate to above several problems. There are varying methods to deal with simlilar problems. Inspired by cell automaton, We hope to provide a new solution to the study of slope stability through the sandcastle foundation model.

<!-- b000156 | heading | pages [4] -->
1.3 Our work

<!-- b000157 | prose | pages [4] -->
Under the assumption that castles are built at roughly the same distance from the water on the same beach with the same type and amount of sand. We establish a model based on cellular automata to formulate the problem.

<!-- b000158 | prose | pages [4] -->
˜Task 1 We use periodic cellular automaton to simulate the environment of the sand- castle to ﬁnd the optimal 3D model. We suppose several most likely geometric shapes as alternative shape. Then we formulate State Transition Rules through multivariate analysis based on multi-criteria judgments. By running the cellu- lar automaton several times, we explore the most stable shape of the sandcastle foundation.

<!-- b000159 | prose | pages [4] -->
˜Task 2 We address the problem of optimal sand-to-water mixture proportion by ﬁt- ting function of the lasting time and sand-to-water proportion. Based on the 3D geometric shape we sort out in Task 1, we adjust the ratio accourding to the concentration gradient method. Record the duration of the model with differ- ent sand-to-water ratio. The longest lasting sandy foundation’s sand-to-water proportion is the target value we anticipate.

<!-- b000160 | prose | pages [4] -->
˜Task 3 Considering the effect of rainfall, we adjust our cellular automaton and repeat the procedure in Task 1. Then we ﬁnd out the optimal 3D geometric shape in this case.

<!-- b000161 | heading | pages [4] -->
2 Preparation of the Models

<!-- b000162 | heading | pages [4] -->
2.1 Analysis of Problems

<!-- b000163 | prose | pages [4] -->
Different from the analysis of the sandpile problem, the sand castle on the beach is the result of mixing water and sand. On one hand, with the degree of sand adhesion increases, the stability of the sand castle will increase. On the other hand, the sand castle will also be affected by external forces. Continuously being eroded by the waves and tides, will accelerate the destruction of the sand castle. Therefore, we need to ﬁnd a 关注数学模型 model that can comprehensively consider the impact of two aspects on the sandcastles.

<!-- b000164 | furniture | pages [4] -->
2

<!-- b000165 | furniture | pages [4] -->
MATHmodels

<!-- b000166 | furniture | pages [4] -->
获取更多资讯

<!-- b000167 | furniture | pages [5] -->
Team # 2007698

<!-- b000168 | furniture | pages [5] -->
Page 4 of 29

<!-- b000169 | heading | pages [5] -->
2.2 Assumptions

<!-- b000170 | prose | pages [5] -->
We make the following assumptions about our Cellular Automaton Simulation Pro- cess:

<!-- b000171 | prose | pages [5] -->
• The sandcastle foundation is only a mixture of sand and water, and all air has been exhausted. In reality, it is impossible for us to turn the inside of the sand pile into a vacuum with bare hands. For the accuracy of the experiment, the sandcastle foundation used is carefully designed so that all the air in the sand- water mixture can be considered exhausted.

<!-- b000172 | prose | pages [5] -->
• The side of the sandcastle foundation is sloped. The stability of the triangle shows that the sloped side has higher stability.

<!-- b000173 | prose | pages [5] -->
• Only the damaging effect of the waves on the surface of sandcastle founda- tion is considered. In fact, there are both waves and tides having an inﬂuence on the surface and structure. However, we do not consider the structural dam- age caused by the waves. Because people usually build sand castles at a certain distance from the sea, and the side of the slope is enough to greatly reduce the impact of the waves on the sandcastle.

<!-- b000174 | prose | pages [5] -->
• The sandy base is stable. Sandcastle foundation will not collapse by the non- wave factor.

<!-- b000175 | prose | pages [5] -->
• The waves will not change the water-sand mixture ratio of the sandcastle foun- dation, but will only corrode the foundation from the surface. The mixture of sand and water has a capillarity phenomenon, and the surface of the sand base can block most of the water from entering the interior.

<!-- b000176 | prose | pages [5] -->
• Sea waves take sand from the surface of sandy bases with their maximum ca- pacity for sand transport.The relationship between sediment content and sedi- ment transport capacity is expressed by Dou Guoren’s equation[3]

<!-- b000177 | prose | pages [5] -->
∂(hs) + ∂(hvs) + αω (S −S∗) = 0 ∂t ∂x

<!-- b000178 | prose | pages [5] -->
At the ideal state,we have

<!-- b000179 | prose | pages [5] -->
∂(hs) + ∂(hvs) = 0 ∂t ∂x

<!-- b000180 | prose | pages [5] -->
Hence, the sediment transport capacity is equal to the sediment content.

<!-- b000181 | prose | pages [5] -->
• The beach sand is composed of natural sand, white bakelite sand and brown bakelite sand. The wave’s sediment carrying capacity of volume Sv is estimated at 55%[13] on the beach.

<!-- b000182 | prose | pages [5] -->
Additional assumptions are made to simplify analysis for individuals sections. These assumptions will be discussed at the appropriate locations.

<!-- b000183 | heading | pages [5] -->
2.3 Notations

<!-- b000184 | prose | pages [5] -->
关注数学模型 The primary notations used in this paper are listed in table 1.

<!-- b000185 | furniture | pages [5] -->
2

<!-- b000186 | furniture | pages [5] -->
MATHmodels

<!-- b000187 | furniture | pages [5] -->
获取更多资讯

<!-- b000188 | furniture | pages [6] -->
Team # 2007698

<!-- b000189 | furniture | pages [6] -->
Page 5 of 29

<!-- b000190 | caption | pages [6] -->
Table 1: Notations

<!-- b000191 | prose | pages [6] -->
Symbol Deﬁnition

<!-- b000192 | prose | pages [6] -->
Sv Waves’ sediment carrying of volume F Number of water cells adjacent to sand cells Uj Number of the water cells around the each surrounding sand cell M, m Sand-to-water proportion P Boundary conditions for the "fall" of sand cells K Instable factors L Cell space size H Maximum height of sandcastle foundation d Width of sandcastle foundation Gi Number of the cells on the top of the foudation = G0 Gmin 2 , Collapsed boundary conditions tj Lasting time of the sand foundation Stability Coefﬁcient σ

<!-- b000193 | heading | pages [6] -->
3 The Optimal 3D Geometric Shape

<!-- b000194 | prose | pages [6] -->
In this section, we will use cellular automata to simulate the interaction between sand and water. We do experiment with several simple geometries to ﬁnd the most stable one of the sandy base.

<!-- b000195 | heading | pages [6] -->
3.1 Model Preparation

<!-- b000196 | heading | pages [6] -->
3.1.1 Model Principle

<!-- b000197 | prose | pages [6] -->
Theoretically, the sandcastle base with a inclined side is the most stable. For a ge- ometric shape, the arris are the most prominent features of the side. Therefore, We choose the most representative shape to do experiment, such as triangular, square, six-arris, conical, ellipse frustum and so on(shown in Figure 1). We carry out several experiments to study the inﬂuence of arris on the stability of sandy bases.

<!-- b000198 | prose | pages [6] -->
Many complex problems can be modeled by cellular automata. Cellular automaton is essentially a dynamic system deﬁned in a cell space composed of cells with discrete and ﬁnite states. According to certain local rules, these cells evolve in discrete time dimensions. The dynamic system has evolved in the time dimension has been widely applied to various ﬁelds of social, economic, military and scientiﬁc research.

<!-- b000199 | prose | pages [6] -->
This model is a periodic cellular automaton model.

<!-- b000200 | heading | pages [6] -->
3.1.2 Model Assumption

<!-- b000201 | prose | pages [6] -->
• Both sand and water can be regarded as incompressible particles.

<!-- b000202 | prose | pages [6] -->
• The sand and water can be mixed together in a certain ratio, and a relatively stable sand foundation can be built at the same time.

<!-- b000203 | prose | pages [6] -->
关注数学模型

<!-- b000204 | prose | pages [6] -->
• We do not take water evaporation into consideration.

<!-- b000205 | furniture | pages [6] -->
2

<!-- b000206 | furniture | pages [6] -->
MATHmodels

<!-- b000207 | furniture | pages [6] -->
获取更多资讯

<!-- b000208 | furniture | pages [7] -->
Team # 2007698

<!-- b000209 | furniture | pages [7] -->
Page 6 of 29

<!-- b000210 | caption | pages [7] -->
Figure 1: Geometric Shape to be Tested

<!-- b000211 | prose | pages [7] -->
• The contact between the waves and the sandy base is mild and will not cause water and sand splashes.

<!-- b000212 | heading | pages [7] -->
3.1.3 Model Construction

<!-- b000213 | prose | pages [7] -->
We physically characterize the system in following aspects.

<!-- b000214 | prose | pages [7] -->
• Cell is the most basic unit of cellular automata.

<!-- b000215 | prose | pages [7] -->
• Cells can memorize storage status.

<!-- b000216 | prose | pages [7] -->
• Each cell of the cellular automaton have three states, namely empty cell, water cell, and sand cell.

<!-- b000217 | prose | pages [7] -->
• The state of any cell at the next moment is determined by its own state and the states of its 26 neighbors, with certain rules.This is shown in Figure2.

<!-- b000218 | caption | pages [7] -->
Figure 2: The Schematic Diagram

<!-- b000219 | heading | pages [7] -->
3.1.4 The Rules

<!-- b000220 | prose | pages [7] -->
1. All cells cannot move upward and each time tne cells can only move to the grid adjacent to itself.

<!-- b000221 | prose | pages [7, 8] -->
关注数学模型 2. If there are F (F ≥P) water cells and n sand cells adjacent to the sand cell, let this cell’s "instable factor" to be K. Then,

<!-- b000222 | furniture | pages [7] -->
2

<!-- b000223 | furniture | pages [7] -->
MATHmodels

<!-- b000224 | furniture | pages [7] -->
获取更多资讯

<!-- b000225 | furniture | pages [8] -->
Team # 2007698

<!-- b000226 | furniture | pages [8] -->
Page 7 of 29

<!-- b000228 | prose | pages [8] -->
n ∑ K = F −σ Uj j=1

<!-- b000229 | prose | pages [8] -->
Where, K is the stability of the sand cell considering the viscosity between sand and water Uj is the number of the sand cells around the center sand cell

<!-- b000230 | heading | pages [8] -->
3. If K ≥P, the sand cell begin to "move downward" follow the principle:

<!-- b000231 | prose | pages [8] -->
Sand cells can only move downward or horizontally, and preferentially in the di- rection downward and with the most water cells. The target position change into a sand cell, and the original position becomes a water cell.

<!-- b000232 | prose | pages [8] -->
When the sand cell moves down, the water cell in the middle change ﬁrst. If the middle one is not a water cell, both neighboring cell will change in the same proba- bility.

<!-- b000233 | prose | pages [8] -->
If there are no water cell below the sand cell, the sand cell will move to the water or empty cell on its right. Otherwise, move to the cell adhere.

<!-- b000234 | prose | pages [8] -->
4. If there are less than P water cells adjacent to the sand cell, the state of the cell holds still.

<!-- b000235 | caption | pages [8] -->
Figure 3: Transition Rule of Sand and Water Cell

<!-- b000236 | prose | pages [8] -->
5. If the water cell is adjacent to 15 or more sand cells, the cell keep constant.

<!-- b000237 | prose | pages [8] -->
6. If there are empty cells below the water cell, the water cell preferentially moves to the empty cells below with equal probability; if not, the cell moves with equal prob- ability to other empty cells. After the target cell becomes a water cell, the original cell becomes empty.

<!-- b000238 | prose | pages [8] -->
7. "Sea waves" (composed of water cells) appear on the left side of the model with a certain pattern.

<!-- b000239 | prose | pages [8, 9] -->
If there is an empty cell to the right of "sea wave", this empty cell will convert into a 关注数学模型 water cell(The middle one change ﬁrst, if the middle one is not an empty cell, both neighboring cell can change in the same probability). The original water cell is con- verted into an empty cell.

<!-- b000240 | furniture | pages [8] -->
2

<!-- b000241 | furniture | pages [8] -->
MATHmodels

<!-- b000242 | furniture | pages [8] -->
获取更多资讯

<!-- b000243 | furniture | pages [9] -->
Team # 2007698

<!-- b000244 | furniture | pages [9] -->
Page 8 of 29

<!-- b000246 | prose | pages [9] -->
If there is no empty cell on the right side of the "sea wave", the water cell moves with equal probability in other directions. This process is repeated until all water cells meet the empty cells and cause a change in state.

<!-- b000247 | heading | pages [9] -->
8. The sand cells and empty cells at the bottom no longer convert state.

<!-- b000248 | heading | pages [9] -->
3.1.5 The Steps of the Algorithm

<!-- b000249 | prose | pages [9] -->
Step 1 Initialize the cellular automata to make all cells empty.

<!-- b000250 | prose | pages [9] -->
Step 2 Add a "sandcastle foundation" to the cellular automaton which at an appropri- ate distance from the cellular automaton.

<!-- b000251 | prose | pages [9] -->
Step 3 Randomly assign the cells. Let the san-to-water proportion of the sandcastle foundation to be M, and assign i = 0.

<!-- b000252 | prose | pages [9] -->
Step 4 At the left end of the cellular automaton, a "sea wave"(composed of water cells) is simulated with width L and height h.And the formula for h is

<!-- b000253 | prose | pages [9] -->
(  2π  , 2kd < i < (2k + 1) d 2H sin d i h = , (2k + 1) d < i < (2k + 2) d (k = 0, 1, 2, ...) 0

<!-- b000254 | prose | pages [9] -->
Where

<!-- b000255 | prose | pages [9] -->
L is the cell space size H is the maximum height of the sand base d is the width of the sand substrate surface

<!-- b000256 | prose | pages [9] -->
Step 5 Run the cellular automaton once and count the cells on the top of the tested geometry Gi.

<!-- b000257 | prose | pages [9] -->
Step 6 If (2k + 1)d < i < (2k + 2)d, (k = 0, 1, 2), water cells at the bottom will inﬁltrate into the ground and disappear at a certain probabilityv.(v = H 2d).

<!-- b000258 | prose | pages [9] -->
Step 7 If Gi > G0 2 , set i = i + 1, return to Step 4.

<!-- b000259 | prose | pages [9] -->
Step 8 The value of output i is the time that the sandy of the geometry persists.

<!-- b000260 | prose | pages [9] -->
This algorithm’s ﬂowchat can be viewed in Figure4.

<!-- b000261 | heading | pages [9] -->
3.1.6 Estimation of P and M

<!-- b000262 | prose | pages [9] -->
Suppose the waves’ sediment carrying capacity is Sv. While the number of water cell satisﬁes p 27 >= 1 −Sv , this cell begins to move downward.

<!-- b000263 | prose | pages [9] -->
Here we suppose Sv = 25%. Plugging Sv into the equation above, we obtain P = 12.

<!-- b000264 | prose | pages [9] -->
From information above, we know M represent the ratio of sand cells to water cells. The optimal value of M will be discussed in Chapter 4. Here we suppose M = 3.5 关注数学模型 temporarily.

<!-- b000265 | furniture | pages [9] -->
2

<!-- b000266 | furniture | pages [9] -->
MATHmodels

<!-- b000267 | furniture | pages [9] -->
获取更多资讯

<!-- b000268 | furniture | pages [10] -->
Team # 2007698

<!-- b000269 | furniture | pages [10] -->
Page 9 of 29

<!-- b000270 | caption | pages [10] -->
Figure 4: The Schematic of Algorithm 1

<!-- b000271 | heading | pages [10] -->
3.2 Result

<!-- b000272 | prose | pages [10] -->
The result of stimulation is shown in Figure 5-9.

<!-- b000273 | heading | pages [10] -->
Analysis of Result

<!-- b000274 | prose | pages [10] -->
From the results of Matlab simulation, it is not difﬁcult to see that the Triangular Frustum has been the longest lasting in the beating of waves. This seems to contradict our common sense. Because in daily life, the most common is a round-shaped sandy base. However, from the inspiration that nature, in order to reduce the stress, the formation of the returning geese is usually herringbone. In terms of ﬂuid dynamics, this shape can reduce the force on the following geese by the leading geese. Therefore, this structure is also conducive to the stability of the second half of our geometry when the waves are washing sand base. Therefore, our sandy foundation can be built into a triangular shape that protrudes like the coast, and then our "castle" is built in the second half of the sandy base, so that our foundation will last longer and our castle will be even more Firm.

<!-- b000275 | prose | pages [10] -->
In real life, we also have many applications of this conclusion. For example, the bow of a ship is always designed in the shape of an inverted triangle. These are all inspired by the principles of ﬂuid dynamics. Then, in the process of playing, we can

<!-- b000276 | prose | pages [10] -->
(a) Begin (b) In the Process (c) End

<!-- b000277 | caption | pages [10] -->
Figure 5: Triangular Frustum

<!-- b000278 | prose | pages [10, 11] -->
关注数学模型 (a) Begin (b) In the Process (c) End

<!-- b000279 | furniture | pages [10] -->
2

<!-- b000280 | furniture | pages [10] -->
MATHmodels

<!-- b000281 | furniture | pages [10] -->
获取更多资讯

<!-- b000282 | furniture | pages [11] -->
Team # 2007698

<!-- b000283 | furniture | pages [11] -->
Page 10 of 29

<!-- b000285 | caption | pages [11] -->
Figure 6: Square Frustum

<!-- b000286 | prose | pages [11] -->
(a) Begin (b) In the Process (c) End

<!-- b000287 | caption | pages [11] -->
Figure 7: Six-arris Frustum

<!-- b000288 | prose | pages [11] -->
(a) Begin (b) In the Process (c) End

<!-- b000289 | caption | pages [11] -->
Figure 8: Conical frustum

<!-- b000290 | prose | pages [11] -->
(a) Begin (b) In the Process (c) End

<!-- b000291 | caption | pages [11] -->
Figure 9: Ellipse Frustum

<!-- b000292 | prose | pages [11] -->
also apply these principles. 关注数学模型

<!-- b000293 | furniture | pages [11] -->
2

<!-- b000294 | furniture | pages [11] -->
MATHmodels

<!-- b000295 | furniture | pages [11] -->
获取更多资讯

<!-- b000296 | furniture | pages [12] -->
Team # 2007698

<!-- b000297 | furniture | pages [12] -->
Page 11 of 29

<!-- b000298 | heading | pages [12] -->
4 The Optimal Sand-to-Water Mixture Proportion

<!-- b000299 | heading | pages [12] -->
4.1 Model Preparation

<!-- b000300 | heading | pages [12] -->
4.1.1 The Principle of Model

<!-- b000301 | prose | pages [12] -->
We do experiment with different water-sand mixture proportion mj. After each ex- periment, we record the time (tj) it takes to make the sandy base disappear completely, and write down the data points(mj, tj). By ﬁtting function curve of these points, we obtain the best ﬁtting curve. Then we can calculate the optimum proportion of sand- to-water.

<!-- b000302 | heading | pages [12] -->
4.1.2 The Steps of Algorithm

<!-- b000303 | prose | pages [12] -->
Using the same model we determine in the Section 3.1.3, we test the stability of sandcastle foundation with different sand-to-water ratio.

<!-- b000304 | prose | pages [12] -->
Step 1 Set j = 1.

<!-- b000305 | prose | pages [12] -->
Step 2 Initialize the cell automaton: Let mj = j 2 and generate a cell space large enough.

<!-- b000306 | prose | pages [12] -->
Assign all cells to be empty. At an appropriate distance from cell space, gener- ate the sandcastle base of the best geometry according to the result of Section 3.1.3.

<!-- b000307 | prose | pages [12] -->
Step 3 Randomly assign the value of sand-to-water ratio (satisty sand : water = mi), and assign i = 0.

<!-- b000308 | prose | pages [12] -->
Step 4 At the left end of the cellular automaton, a "sea wave" is simulated with width L and height h.And the formula for h is

<!-- b000309 | prose | pages [12] -->
(  2π  , 2kd < i < (2k + 1) d 2H sin d i h = , (2k + 1) d < i < (2k + 2) d (k = 0, 1, 2, ...) 0

<!-- b000310 | prose | pages [12] -->
Where

<!-- b000311 | prose | pages [12] -->
L is the cell space size H is the maximum height of the sand base d is the width of the sand substrate surface

<!-- b000312 | prose | pages [12] -->
Step 5 Run the cellular automaton once and count the cells on the top of the tested geometry Gi.

<!-- b000313 | prose | pages [12] -->
Step 6 If (2k + 1)d < i < (2k + 2)d, (k = 0, 1, 2), the water cells at the bottom will inﬁltrate into the ground and disappear with certain probabilityv = H 2d.

<!-- b000314 | prose | pages [12] -->
Step 7 If Gi > G0 2 , set i = i + 1, return to Step 4. Step 8 Let tj = i, record the data points(mj, tj). If mj < 40, set j = j + 1, return Step 2.

<!-- b000315 | prose | pages [12] -->
Step 9 Get the ﬁt function of the curve by the ﬁtting all the data points.

<!-- b000316 | prose | pages [12] -->
关注数学模型 This algorithm’s ﬂowchat can be viewed in Figure10.

<!-- b000317 | furniture | pages [12] -->
2

<!-- b000318 | furniture | pages [12] -->
MATHmodels

<!-- b000319 | furniture | pages [12] -->
获取更多资讯

<!-- b000320 | furniture | pages [13] -->
Team # 2007698

<!-- b000321 | furniture | pages [13] -->
Page 12 of 29

<!-- b000322 | caption | pages [13] -->
Figure 10: The Schematic of Algorithm 2

<!-- b000323 | heading | pages [13] -->
4.2 Result

<!-- b000324 | prose | pages [13] -->
Using the perodic cellular automata, we collect the duration as a function of the sand-to-water ratio.The table below is data points generated from our experiment.

<!-- b000325 | caption | pages [13] -->
Table 2: Duration of Different Water-sand proportion

<!-- b000326 | prose | pages [13] -->
water:sand 0.0200 0.0500 0.0800 0.1100 0.1400 0.1700 0.2000 0.2300 0.2600 time 163 209 163 147 150 90 88 34 33

<!-- b000327 | prose | pages [13] -->
Then we ﬁt the above results with a ten-degree polynomial, and we get the follow- ing picture(Figure 11).

<!-- b000328 | caption | pages [13] -->
Figure 11: Fitting Curve

<!-- b000329 | heading | pages [13] -->
Analysis of Result

<!-- b000330 | prose | pages [13, 14] -->
Through the concentration gradient method research on the water-sand ratio and 关注数学模型 stability, we have obtained a series of data. By approximating the ﬁtting with a poly- nomial function based on the least squares, the ﬁtting curve is obtained. The curve shows that the optimal water-to-sand ratio is around 0.05.

<!-- b000331 | furniture | pages [13] -->
2

<!-- b000332 | furniture | pages [13] -->
MATHmodels

<!-- b000333 | furniture | pages [13] -->
获取更多资讯

<!-- b000334 | furniture | pages [14] -->
Team # 2007698

<!-- b000335 | furniture | pages [14] -->
Page 13 of 29

<!-- b000337 | heading | pages [14] -->
5 The Optimal Shape in Rainy Day

<!-- b000338 | heading | pages [14] -->
5.1 Modiﬁed CA Model

<!-- b000339 | heading | pages [14] -->
5.1.1 Model Assumption

<!-- b000340 | prose | pages [14] -->
• The capillary phenomenon of water and sand on the surface of the sand base is strong enough. Thence rainwater can only slowly affect the surface of the foun- dation without changing the internal structure of it.

<!-- b000341 | prose | pages [14] -->
• Although the sand-to-water ratio changes gradually, the sand-to-water ratio does not affect the stability of the geometric shape, so the effect of sand-to-water ratio can be ignored.

<!-- b000342 | prose | pages [14] -->
• Rainfall and waves affect sandy foundation together, but do not affect the pene- tration rate of water on the bottom surface.

<!-- b000343 | prose | pages [14] -->
• The rainfall’s intensity will not cause the sand foundation to collapse suddenly.

<!-- b000344 | heading | pages [14] -->
5.1.2 Similarities and Difference from Basic Model

<!-- b000345 | prose | pages [14] -->
Difference A rainfall module was added to the original model. The impact of the waves on the sandy base still exists besides rain erosion.

<!-- b000346 | prose | pages [14] -->
Similarities Still choose the most representative triangular, square, six-arris and conical, ellipse frustum for experiments, and study the inﬂuence of different geometric upper surface on the stability of the sand foundation.

<!-- b000347 | heading | pages [14] -->
5.1.3 The Steps of Algorithm

<!-- b000348 | prose | pages [14] -->
Step 1 Initialize the cellular automata, namely generate a large enough cell space and initialize all cells to empty.

<!-- b000349 | prose | pages [14] -->
Step 2 Add the "Sandcastle Foundation" to the cellular automaton which at an appro- priate distance from the cellular automata.

<!-- b000350 | prose | pages [14] -->
Step 3 Randomly assign the cells. Set the sand-to-water proportion of the sandcastle foundation to be M, and assign i = 0.

<!-- b000351 | prose | pages [14] -->
Step 4 At the left end of the cellular automaton, a "sea wave"(water cells) is simulated with width L and height h.And the formula for h is

<!-- b000352 | prose | pages [14, 15] -->
(  2π  , 2kd < i < (2k + 1) d 2H sin d i h = , (2k + 1) d < i < (2k + 2) d (k = 0, 1, 2, ...) 关注数学模型 Where

<!-- b000353 | furniture | pages [14] -->
0

<!-- b000354 | furniture | pages [14] -->
2

<!-- b000355 | furniture | pages [14] -->
MATHmodels

<!-- b000356 | furniture | pages [14] -->
获取更多资讯

<!-- b000357 | furniture | pages [15] -->
Team # 2007698

<!-- b000358 | furniture | pages [15] -->
Page 14 of 29

<!-- b000359 | caption | pages [15] -->
Figure 12: The Schematic of Algorithm 3

<!-- b000361 | prose | pages [15] -->
L is the cell space size H is the maximum height of the sand base d is the width of the sand substrate surface

<!-- b000362 | prose | pages [15] -->
Step 5 At the top of the cell space, the cell will transform itself into a water cell with a H certain probability u = 20d.

<!-- b000363 | prose | pages [15] -->
Step 6 Run the cellular automaton once and count the cells on the top of the tested geometry Gi.

<!-- b000364 | prose | pages [15] -->
Step 7 If (2k + 1)d < i < (2k + 2)d, (k = 0, 1, 2), water cells at the bottom will inﬁltrate into the ground and disappear at a certain probability v. Here we suppose v = H 2d.

<!-- b000365 | prose | pages [15] -->
Step 8 If Gi > G0 2 , set i = i + 1, return to Step 4.

<!-- b000366 | prose | pages [15] -->
Step 9 The value of output i is the time that the sandy of the geometry persists.

<!-- b000367 | prose | pages [15] -->
This algorithm’s ﬂowchat can be viewed in Figure12.

<!-- b000368 | heading | pages [15] -->
5.2 Result

<!-- b000369 | prose | pages [15] -->
The result of stimulation is shown in Figure 13-17.

<!-- b000370 | heading | pages [15] -->
Analysis of Result

<!-- b000371 | prose | pages [15, 16] -->
From the results, we can see that when there is rainfall, the stability of the geom- etry changes. The advantage of the triangular prism to reduce the impact force is not obvious. The performance of the ellipse frustum is slightly better. Presumably because of the rainfall and the same amount of sand, the surface area of the triangular frustum is larger than that of the ellipse frustum. Therefore, when interference occurs from 关注数学模型 above, the ellipse frustum can reduce the force to a certain extent in the horizontal (a) Begin (b) Outcome

<!-- b000372 | furniture | pages [15] -->
2

<!-- b000373 | furniture | pages [15] -->
MATHmodels

<!-- b000374 | furniture | pages [15] -->
获取更多资讯

<!-- b000375 | furniture | pages [16] -->
Team # 2007698

<!-- b000376 | furniture | pages [16] -->
Page 15 of 29

<!-- b000378 | caption | pages [16] -->
Figure 13: Triangular Frustum

<!-- b000379 | prose | pages [16] -->
(a) Begin (b) Outcome

<!-- b000380 | caption | pages [16] -->
Figure 14: Square Frustum

<!-- b000381 | prose | pages [16] -->
(a) Begin (b) Outcome

<!-- b000382 | caption | pages [16] -->
Figure 15: Six-arris Frustum

<!-- b000383 | prose | pages [16] -->
(a) Begin (b) Outcome

<!-- b000384 | caption | pages [16] -->
Figure 16: Conical frustum

<!-- b000385 | prose | pages [16, 17] -->
direction and reduce the contact area in the vertical direction. At the same time, the ellipse frustum has no edges and corners, so it is not easy to collapse in some parts. 关注数学模型 (a) Begin (b) Outcome

<!-- b000386 | furniture | pages [16] -->
2

<!-- b000387 | furniture | pages [16] -->
MATHmodels

<!-- b000388 | furniture | pages [16] -->
获取更多资讯

<!-- b000389 | furniture | pages [17] -->
Team # 2007698

<!-- b000390 | furniture | pages [17] -->
Page 16 of 29

<!-- b000392 | caption | pages [17] -->
Figure 17: Ellipse Cone

<!-- b000393 | prose | pages [17] -->
Triangular frustum has a strong ability to resist the waves, which to some extent offsets the inﬂuence brought by his edges and corners. Therefore, on rainy days, the triangular and ellipse frustums have considerable stability.

<!-- b000394 | heading | pages [17] -->
6 Sensitivity Analysis

<!-- b000395 | prose | pages [17] -->
Through the above analysis, we obtained the optimal shape of the sand base and the optimal sand-water ratio. At the same time, we presume many parameters in the model. In order to ensure the robustness of the model, we test the model from the following aspects.(Due to time constraints, analysis is only performed on the triangular prism.)

<!-- b000396 | prose | pages [17] -->
First of all, the sediment carrying of the waves. Waves of different sizes can cause varying degrees’ impacts on the surface of the sandy foundation. It will also affect the persistence of foundation. In the previous model, we obtained from the sediment transport equation of Dou.

<!-- b000397 | prose | pages [17] -->
∂(hs) + ∂(hvs) = 0 ∂t ∂x Under ideal experimental conditions, the capacity of sediment transport is equal to the sediment content. And we set Sv = 55%.

<!-- b000398 | prose | pages [17] -->
Second, the width of the sand base. According to common sense, items with a large base area stand more stable than those with a small base area. For sandy foun- dations, larger sandy foundations are good for dispersing the impact of the waves. It is also possible to last longer. This parameter’s selection may have an inﬂuence on the selection of the optimal sandy model.

<!-- b000399 | prose | pages [17] -->
Furthermore, the stability factor of sand. In the simulation process, we assumed the stability factor to be σ, so that the instability factor of the sand was calculated based on it. Thereby, it is judged whether or not the sand will move according to K. Depending on the stability factor, the calculated instability factors of the sand are also different. Then, the steady state of the sandy base may also change.

<!-- b000400 | prose | pages [17, 18] -->
Finally, the critical condition of the upper surface being destroyed. Since the cas- tle is to be built on the mound, it is important to have a stable one. In the above experiment, when Gi < G0 2 , it is considered that the surface of the sandy base has been damaged, and it is not qualiﬁed for building a castle. So Gmin = G0 2 . When we change the value of Gmin, the best sandy model may change. 关注数学模型 Our model design allows us to change these parameters. Next we develop a de- tailed analysis of following elements’ impact on the model.

<!-- b000401 | furniture | pages [17] -->
2

<!-- b000402 | furniture | pages [17] -->
MATHmodels

<!-- b000403 | furniture | pages [17] -->
获取更多资讯

<!-- b000404 | furniture | pages [18] -->
Team # 2007698

<!-- b000405 | furniture | pages [18] -->
Page 17 of 29

<!-- b000407 | prose | pages [18] -->
• Sediment Capacity

<!-- b000408 | prose | pages [18] -->
• Geometric Shape’s Length Attribute

<!-- b000409 | prose | pages [18] -->
• Unstable Factors

<!-- b000410 | prose | pages [18] -->
• Sand Foundation Damage Judgment

<!-- b000411 | prose | pages [18] -->
We record the results in each case with changes of 10%, 5%, -5%, and -10%. And the

<!-- b000412 | caption | pages [18] -->
table 3 has shown the results.

<!-- b000413 | caption | pages [18] -->
Table 3: Results of Sensitivity Analysis

<!-- b000414 | prose | pages [18] -->
-10% -5% 0 5% 10% Sv 1684i 875i 796i 615i time out H 636i 726i 875i 1354i time out d 702i 835i 875i 926i 953i 693i 805i 875i 948i 1062i σ Gmin 1242i 966i 875i 801i 762i

<!-- b000415 | prose | pages [18] -->
According the above data, we can see these parameters’ impact extend on the sta- bility.

<!-- b000416 | prose | pages [18] -->
The analysis results of the sediment capacity analysis indicate that the effect of the sediment capacity on the sand foundation cannot be underestimated. To build a stable sand foundation, choosing the appropriate sand is essential. We should try to ﬁnd sand with strong adhesion, so as to relatively reduce the ability of the waves’ sediment.

<!-- b000417 | prose | pages [18] -->
The analysis results of the geometric properties of sand foundation show that es- tablishing a wider sand foundation is also a good method to improve its stability. The wider the sand dunes, the more likely it is to disperse the impact of the waves. It is possible for the sandy base to persist longer.

<!-- b000418 | prose | pages [18] -->
The analysis results of instability factors show that the adhesion between sand and water also has a huge impact on the stability of sand foundation.

<!-- b000419 | prose | pages [18] -->
The analysis result of the sensitivity of sandy damage judgment shows that no mat- ter what is used as the judgment basis, it does not affect the ﬁnal result of the model.

<!-- b000420 | heading | pages [18] -->
7 Strengths and Weaknesses

<!-- b000421 | heading | pages [18] -->
7.1 Strengths

<!-- b000422 | prose | pages [18] -->
• Our model is formulated on a certain theoretical basis. After consulting a lot of literature, we carefully selected the parameters of the model. In this way ,we can make our model as close to reality as possible.

<!-- b000423 | prose | pages [18] -->
• We carry out reasonable simpliﬁcation, and establish a cellular automaton model to solve the problem. The results are consistent with actual practice, and have 关注数学模型 high credibility.

<!-- b000424 | furniture | pages [18] -->
2

<!-- b000425 | furniture | pages [18] -->
MATHmodels

<!-- b000426 | furniture | pages [18] -->
获取更多资讯

<!-- b000427 | furniture | pages [19] -->
Team # 2007698

<!-- b000428 | furniture | pages [19] -->
Page 18 of 29

<!-- b000429 | prose | pages [19] -->
• We take the reality conditions into account and test several basic geometric shape.

<!-- b000430 | prose | pages [19] -->
Then we obtain a much meaningful model. What’s more, the experimental result- s are all easy-to-implement geometric shapes with high Operability.

<!-- b000431 | prose | pages [19] -->
• Though we did not do experiment on every shapes, our model has enough ﬂexi- bility to test more conditions. We just need to alter a few parameters to do deeper research. For example, the model can test the stability of the sand foundation of any geometric shape, and what will be different if we built the castle a little farther from the sea.

<!-- b000432 | prose | pages [19] -->
• The model can also be tested according to the type of sand used to ﬁnd its optimal sand-to-water mixture ratio. As long as some parameters of this type of sand are known, we can meet the requirements of different sandcastle enthusiasts.

<!-- b000433 | heading | pages [19] -->
7.2 Weaknesses

<!-- b000434 | prose | pages [19] -->
• Limited to the limitation of equipment, the cellular automaton model is not quite exact, and the quality may not meet our higher expectations.

<!-- b000435 | prose | pages [19] -->
• Ignore the impact of the enormous waves, so the applicability on the beach with violent waves needs to further improve the model.

<!-- b000436 | prose | pages [19] -->
• Indeed, the assumptions may be not hold in some cases. There still be some controversy about our model.

<!-- b000437 | heading | pages [19] -->
7.3 Promption

<!-- b000438 | prose | pages [19] -->
We tried to simulate the situation on the beach with simulation methods. However, due to time constraints, we made many assumptions about the real situation. For example, regardless of the evaporation of water, setting the frequency of the waves to a relatively ﬁxed value, and so on. Next, we can try to release some assumptions, so that the sand castle can also change more vividly according to reality. We can explore more possibilities by changing some parameters of the program and adding more rules.

<!-- b000439 | heading | pages [19] -->
8 Strategies to Make sandcastle More Lasting

<!-- b000440 | prose | pages [19] -->
Based on the results of the sensitivity analysis and our discussions, we ﬁnd out the strategies below to increase the stability of the sandy foundation.

<!-- b000441 | prose | pages [19] -->
• Look for different sands on the beach. The stability of the sandcastle foundation formed by mixing different sands may show very different stability. If we could select different sand and admix some water, we can test the sand by hand. If the sand could be pressed into a ball and could be rolled back and forth without spreading out, then the sand is suitable.

<!-- b000442 | prose | pages [19] -->
• Since it is a "castle", the site selection is also very important. We had better to choose a place some distance from the waves the high tide of the waves. But there may be a trouble that we need to pay more efforts to fetch water. To address 关注数学模型 this problem, we may dig a deep enough hole near your "construction site".

<!-- b000443 | furniture | pages [19] -->
2

<!-- b000444 | furniture | pages [19] -->
MATHmodels

<!-- b000445 | furniture | pages [19] -->
获取更多资讯

<!-- b000446 | furniture | pages [20] -->
Team # 2007698

<!-- b000447 | furniture | pages [20] -->
Page 19 of 29

<!-- b000448 | prose | pages [20] -->
• Try to tamp the sand to drain excess water. Too much water makes the sand ﬂow around and is not easy to ﬁx. Too little water makes the sand lack of stickiness.

<!-- b000449 | prose | pages [20] -->
So we need to accurately grasp the proportion of sand and water. From the above conclusions we can know, the optimal water-sand ratio ? . If we do not have the right tools to control the proportion, we may choose some sand that has been soaked in seawater in the place washed by the waves.

<!-- b000450 | prose | pages [20] -->
• Ensure that each grain of sand is moist. When building a sandy foundation, we can get some inspiration from stirring cement. Build a â ˘AIJannulusâ ˘A˙I on the top of your foundation and pour water into the crater until it is as high as the outer edge. Afterwards, in order to accelerate the inﬁltration of water, we can continuously churn the sand with your hands until the water basically inﬁltrates.

<!-- b000451 | prose | pages [20] -->
More importantly, during the construction of the castle, as the water evaporates, the sand on the surface will become more and more dry, so we need to constantly spray water on the castle surface. Or take other measures to ensure that the sand is moist.

<!-- b000452 | prose | pages [20] -->
• Establish a larger sand foundation within the circumstances of the force. This can enhance its anti-interference ability. If possible, use stones, wooden boards, plastic plates, etc. to block the waves or reinforce the sandy surface.

<!-- b000453 | heading | pages [20] -->
9 Conclusion

<!-- b000454 | prose | pages [20] -->
In our experiments, we design a periodic sand-water cell automaton model. The model simulates the actual situation on the beach. Employing multivariate analysis methods, we designed the rules of state changes of various cells in cell space. First, we set up the sand-foundaion module and the wave module, and simulate their interac- tion in cell space to ﬁnd the best geometry. It is triangle frustum. We then use the least squares method to ﬁt the curve of snad-to-water proportion and duration. Analyze the function image to determine the best water-sand ratio. Since it is outdoors, we have to consider the impact of the weather. After adding the rainfall module to the model, we found that the results of Problem 1 have some changes and the optimal shape is trian- gular and ellipse frustum. After sensitivity analysis, our results have good robustness and the results are credible. Although our model has good scalability and ﬂexibility, there are certain defects in the model. Too many assumptions make the model still have a certain gap with the actual situation. However, we have discussed some practi- cal ways to enhance the stability of sand castles. For example, how to choose the sand and construction site, how to achieve the sand-water ratio and so on. In the future, we still have the opportunity to continue to optimize our model.

<!-- b000455 | prose | pages [20, 21] -->
关注数学模型 Article

<!-- b000456 | furniture | pages [20] -->
2

<!-- b000457 | furniture | pages [20] -->
MATHmodels

<!-- b000458 | furniture | pages [20] -->
获取更多资讯

<!-- b000459 | furniture | pages [21] -->
Team # 2007698

<!-- b000460 | furniture | pages [21] -->
Page 20 of 29

<!-- b000462 | prose | pages [21] -->
The Secret of Sandcastle Building

<!-- b000463 | prose | pages [21] -->
"Oh, no! My ’castle’ is wrecked by waves once again."A guy shouted.

<!-- b000464 | prose | pages [21] -->
Have you ever been confused about how to make your sandcastle more last- ing? Do you wonder what is the hardest sandcastle in the world? Now let me tell you the secret of it.

<!-- b000465 | prose | pages [21] -->
Since many factors have an inﬂuence on the sandcastle. We design an auto- matic model to simulate the foundation of the sandcastle. By set the surround- ings and materials, we invite computers to be our "designer". It can stimulate the Resource:www.photophoto.com surroundings on the beach automatically.

<!-- b000466 | prose | pages [21] -->
After trying again and again, it can tell us which shape is most beneﬁcial for our "castle" to hold longer.

<!-- b000467 | prose | pages [21] -->
The ﬁrst step, build the foundation of your castle. The shape of the sandcastle foundation determines the force it bears. Sandy bases come in various shapes. We ﬁnd that there is a common ground of them—-they all have sloped sides. Therefore, we pick several typical inertial frustum to test their stability. For example, triangular, square, six-arris, triangular and ellipse frustum and so on.

<!-- b000468 | prose | pages [21] -->
By trying many times, our "designer" tells us the most lasting geometric shape is Triangular Frustum for this shape can minimizes the impact on the second half of the sandy foundation. In our experiment, it can stand on the beach much longer than others. So it is suggested that you make a foundation like this.

<!-- b000469 | prose | pages [21] -->
The next step is to admix sand with water. Since you know the best shape of san- dacastle foundation, you may wonder how much water we should add to the sand.

<!-- b000470 | prose | pages [21] -->
As it is known to all, sands are too loose to be ﬁxed. It is all down to water that en- able sand grain to "humble" each other. "Too much water and your sand will ﬂow, too little and it will crumble."1 So, how much is appropriate? In our experiment, we determine the optimal sand-to-water mixture proportion by plotting the function graph of the duration and the sand-to-water ratio. And the results are shown in the ﬁgure below. As the image demonstrated, the best water-to-sand ratio is around 0.05.

<!-- b000471 | prose | pages [21] -->
So far, we assume the weather is sunny. What if it is rainy? Does the "secret" still work? Again, we run our model but there should be some adjustments for our castle. To mimic the process of rain, we added raindrop on top of the sand. Then, we can ﬁnd that the deformation process of the sand pile shows different characteristics. It is more likely to be washed over the sand. The optimal geometry this time is an Triangular Frustum or Ellipse Frustum.

<!-- b000472 | prose | pages [21, 22] -->
Although in rainy day you don’t need to constantly do everything possible to keep the sand pile moist in this case, you need to be more carefull about the water-sand 关注数学模型 1Retrieved from https://www.pbs.org/newshour/science/build-perfect-sandcastle-science ratio.

<!-- b000473 | furniture | pages [21] -->
2

<!-- b000474 | furniture | pages [21] -->
MATHmodels

<!-- b000475 | furniture | pages [21] -->
获取更多资讯

<!-- b000476 | furniture | pages [22] -->
Team # 2007698

<!-- b000477 | furniture | pages [22] -->
Page 21 of 29

<!-- b000478 | caption | pages [22] -->
Figure 18: Fitting Curve

<!-- b000480 | prose | pages [22] -->
Besides, you try to admix different kinds of sand. While you are curving you castle, do not forget to keep your castle moist. But be cautious of adding too much water into your model. If possible, you even can make use of your feet to drain redudant water and tamper your foundation.

<!-- b000481 | prose | pages [22] -->
Certainly there are many other strategies that you can apply to build your castle. But what I want to remind you is that practice makes perfect. If you want to become a master, you need to master more skills. Don’t lose heart just because of failure. There are still numer- ous secrets of building castle waiting for you to discover.

<!-- b000482 | prose | pages [22] -->
The next time you go to the beach, you may try these techniques out and see whether it is effective. "Real knowledge comes from prac- tice." To be a real great master, you need to ﬁnd the secret that suits you.

<!-- b000483 | heading | pages [22] -->
References

<!-- b000484 | references | pages [22] -->
Resource:www.51yuansu.com

<!-- b000485 | references | pages [22] -->
[1] J.-P. Bouchaud, M. E. Cates, J. Ravi Prakash, and S. F. Edwards. Hysteresis and

<!-- b000486 | references | pages [22] -->
metastability in a continuum sandpile model. Phys. Rev. Lett., 74:1982–1985, Mar

<!-- b000487 | references | pages [22] -->
1995.

<!-- b000488 | references | pages [22] -->
[2] You-Liang Chen, Geng-Tun Liu, Ning Li, Xi Du, Su-Ran Wang, and Ragﬁg Az-

<!-- b000489 | references | pages [22] -->
zam. Stability evaluation of slope subjected to semismic effect combined with

<!-- b000490 | references | pages [22] -->
consequent rainfall. Engineering Geologe, 266, 202.

<!-- b000491 | references | pages [22] -->
[3] Guoren Dou, Fengwu Dong, and Xibing Dou. The sediment carrying capacity of

<!-- b000492 | references | pages [22] -->
waves and trides. Science Bulleitn, pages 443–446, 1995. 11-1784/N.

<!-- b000493 | references | pages [22] -->
[4] Serge Dumont and Noureddine IGBIDA. On a dual formulation for the growing

<!-- b000494 | references | pages [22] -->
关注数学模型

<!-- b000495 | references | pages [22] -->
sandpile problem. European Journal of Applied Mathematics, 20(2):169–185, 2009.

<!-- b000496 | furniture | pages [22] -->
2

<!-- b000497 | furniture | pages [22] -->
MATHmodels

<!-- b000498 | furniture | pages [22] -->
获取更多资讯

<!-- b000499 | furniture | pages [23] -->
Team # 2007698

<!-- b000500 | furniture | pages [23] -->
Page 22 of 29

<!-- b000501 | references | pages [23] -->
[5] Serge Dumont and Noureddine Igbida. On the collapsing sandpile problem. 2011.

<!-- b000502 | references | pages [23] -->
[6] Mehmet Emiro˘glu, Ahmet Yalama, and Yasemin Erdo˘gdu. Performance of ready-

<!-- b000503 | references | pages [23] -->
mixed clay plasters produced with different clay/sand ratios. Applied Clay Science,

<!-- b000504 | references | pages [23] -->
115:221–229, 2015.

<!-- b000505 | references | pages [23] -->
[7] N Fraysse, H Thomé, and L Petit. Humidity effects on the stability of a sandpile.

<!-- b000506 | references | pages [23] -->
The European Physical Journal B-Condensed Matter and Complex Systems, 11(4):615–

<!-- b000507 | references | pages [23] -->
619, 1999.

<!-- b000508 | references | pages [23] -->
[8] Torsten Gröger, Ugur Tüzün, and David M Heyes. Modelling and measuring of

<!-- b000509 | references | pages [23] -->
cohesion in wet granular materials. Powder Technology, 133(1-3):203–215, 2003.

<!-- b000510 | references | pages [23] -->
[9] Thomas C Halsey and Alex J Levine. How sandcastles fall. Physical Review Letters,

<!-- b000511 | references | pages [23] -->
80(14):3141, 1998.

<!-- b000512 | references | pages [23] -->
[10] DJ Hornbaker, Réka Albert, István Albert, A-L Barabási, and Peter Schiffer. What

<!-- b000513 | references | pages [23] -->
keeps sandcastles standing? Nature, 387(6635):765–765, 1997.

<!-- b000514 | references | pages [23] -->
[11] TG Mason, AJ Levine, D Erta¸s, and TC Halsey. Critical angle of wet sandpiles.

<!-- b000515 | references | pages [23] -->
Physical Review E, 60(5):R5044, 1999.

<!-- b000516 | references | pages [23] -->
[12] Maryam Pakpour, Mehdi Habibi, Peder Møller, and Daniel Bonn. How to con-

<!-- b000517 | references | pages [23] -->
struct the perfect sandcastle. Scientiﬁc reports, 2(1):1–3, 2012.

<!-- b000518 | references | pages [23] -->
[13] Yangui Wang, Zhaoyin Wang, Qinghua Zeng, and Xiuzhen Lv. Experimental s-

<!-- b000519 | references | pages [23] -->
tudy and similar analysis of physical properties of simulated sand. Journal of Sed-

<!-- b000520 | references | pages [23] -->
iment Research, 1992.

<!-- b000521 | references | pages [23] -->
[14] Po-Tsun Yeh, Kevin Zeh-Zon, and Kuang-Tsung Chang. 3d effects of permeability

<!-- b000522 | references | pages [23] -->
and strength abistropy in the stability of weakly cemented rock slopes subjected

<!-- b000523 | references | pages [23] -->
to reainfall inﬁltaction. 266, 2020.

<!-- b000524 | references | pages [23] -->
[15] GAO Yufeng, WANG Di, and ZHANG Fei. Current research and propects od 3d

<!-- b000525 | references | pages [23] -->
earth slope stability analysis methods. 43:456–464, 2015.

<!-- b000526 | references | pages [23] -->
关注数学模型

<!-- b000527 | furniture | pages [23] -->
2

<!-- b000528 | furniture | pages [23] -->
MATHmodels

<!-- b000529 | furniture | pages [23] -->
获取更多资讯

<!-- b000530 | furniture | pages [24] -->
Team # 2007698

<!-- b000531 | furniture | pages [24] -->
Page 23 of 29

<!-- b000532 | heading | pages [24] -->
Appendix: Our Code

<!-- b000533 | prose | pages [24] -->
function createSandWorld(long, width, height,ratio) close; space = zeros(3*width,2*long,4*height); space(:,1:end,1) = 2; d=10; space = createThreePyramid(space,long,width,height,.5,d,ratio); G=getSandNum(space,height); Gi=getSandNum(space,height); time=0; draw(space,time,Gi) while Gi>=(G/2) time=time+1; space = createWave(space,time,width,height); draw(space,time,Gi) space = moveWater(space); space = permeate(space,time,width,height); draw(space,time,Gi) space = moveSand(space); draw(space,time,Gi) Gi=getSandNum(space,height); end end

<!-- b000534 | prose | pages [24, 25] -->
function sixPyramid=createSixPyramid(B,L,H,s,d,p) dim=size(B); pos=sym(’pos’,[9,3]); pos(1,:)=[dim(1)-1-d,round(dim(2)/2-L/4),2]; pos(2,:)=[pos(1,1),round(dim(2)/2+L/4),2]; pos(3,:)=[round(pos(1,1)-sqrt(3)*L/4),round(pos(2,2)+L/4),2]; pos(4,:)=[round(pos(1,1)-sqrt(3)*L/2),pos(2,2),2]; pos(5,:)=[pos(4,1),pos(1,2),2]; pos(6,:)=[pos(3,1),round(pos(1,2)-L/4),2]; pos(7,:)=[pos(6,1),round(dim(2)/2-L*s/2),H+pos(1,3)-1]; pos(8,:)=[round(pos(7,1)+sqrt(3)*s*L/4), round(pos(7,2)+3*s*L/4),H+pos(1,3)-1]; pos(9,:)=[pos(7,1),round(dim(2)/2+L*s/2),H+pos(1,3)-1]; plane=sym(’plane’,[1,6]); plane(1)=getPlane(pos(1,:),pos(2,:),pos(8,:)); plane(2)=getPlane(pos(2,:),pos(8,:),pos(3,:)); plane(3)=getPlane(pos(4,:),pos(9,:),pos(3,:)); syms x plane(4)=subs(plane(1),x,2*pos(3,1)-x); plane(5)=getPlane(pos(5,:),pos(6,:),pos(7,:)); plane(6)=getPlane(pos(1,:),pos(6,:),pos(7,:)); z1=double(pos(8,3));z2=double(pos(1,3)); x1=double(pos(4,1));x2=double(pos(1,1)); y1=double(pos(6,2));y2=double(pos(3,2)); for z=z1:-1:z2 for x=x1:x2 for y=y1:y2 if eval(plane(1))>=z && eval(plane(2))>=z && eval(plane(3))>=z && eval(plane(4))>=z && eval(plane(5))>=z && eval(plane(6))>=z 关注数学模型 B(x,y,z)=1; end end end end B=insertWater(B,p); sixPyramid=B; end function circular=createCircular(B,L,W,H,d,p) dim=size(B); a=W/2;b=L/2;c=dim(3)-1; pos=sym(’pos’,[4,3]); pos(1,:)=[dim(1)-1-d,ceil(dim(2)/2),2]; pos(2,:)=[ceil(pos(1,1)-a),ceil(pos(1,2)+b),2]; pos(3,:)=[ceil(pos(1,1)-2*a),pos(1,2),2]; pos(4,:)=[pos(2,1),ceil(pos(1,2)-b),2]; x1=double(pos(3,1));x2=double(pos(1,1)); y1=double(pos(4,2));y2=double(pos(2,2)); for z=H+1:-1:2 for x=x1:x2 for y=y1:y2 if z <= c+1-sqrt(cˆ2*((x-pos(2,1))ˆ2/aˆ2+(y-pos(1,2))ˆ2/bˆ2)) B(x,y,z)=1; end end end end B=insertWater(B,p); circular=B; end

<!-- b000535 | furniture | pages [24] -->
2

<!-- b000536 | furniture | pages [24] -->
MATHmodels

<!-- b000537 | furniture | pages [24] -->
获取更多资讯

<!-- b000538 | furniture | pages [25] -->
Team # 2007698

<!-- b000539 | furniture | pages [25] -->
Page 24 of 29

<!-- b000541 | prose | pages [25] -->
function fourPyramid=createFourPyramid(B,L,W,H,s,d,p) pos=sym(’pos’,[4,3]); dim=size(B); pos(1,:)=[dim(1)-1-d,round((dim(2)-L)/2),2]; pos(2,:)=[pos(1,1),pos(1,2)+L,2]; pos(3,:)=[pos(1,1)-W,pos(2,2),2]; pos(4,:)=[round((pos(1,1)+pos(3,1))/2 + (W*s)/2),... round((pos(1,2)+pos(2,2))/2 + (L*s)/2),... H+pos(1,3)-1]; plane=sym(’plane’,[1,4]); plane(1)=getPlane(pos(1,:),pos(2,:),pos(4,:)); plane(2)=getPlane(pos(2,:),pos(3,:),pos(4,:)); syms x y plane(3)=subs(plane(1),x,pos(1,1)+pos(3,1)-x); plane(4)=subs(plane(2),y,pos(1,2)+pos(2,2)-y); z1=double(pos(4,3));z2=double(pos(1,3)); x1=double(pos(3,1));x2=double(pos(1,1)); y1=double(pos(1,2));y2=double(pos(3,2));

<!-- b000542 | prose | pages [25, 26] -->
关注数学模型 for z=z1:-1:z2 for x=x1:x2 for y=y1:y2 if eval(plane(1))>=z && eval(plane(2))>=z && eval(plane(3))>=z && eval(plane(4))>=z B(x,y,z)=1; end end end end B=insertWater(B,p); fourPyramid=B; end

<!-- b000543 | furniture | pages [25] -->
2

<!-- b000544 | furniture | pages [25] -->
MATHmodels

<!-- b000545 | furniture | pages [25] -->
获取更多资讯

<!-- b000546 | furniture | pages [26] -->
Team # 2007698

<!-- b000547 | furniture | pages [26] -->
Page 25 of 29

<!-- b000549 | prose | pages [26] -->
function threePyramid=createThreePyramid(B,L,W,H,s,d,p) dim=size(B); pos=sym(’pos’,[5,3]); pos(1,:)=[dim(1)-1-d,round(dim(2)/2),2]; pos(2,:)=[pos(1,1)-W,pos(1,2)-round(L/2),2]; pos(3,:)=[pos(2,1),pos(1,2)+round(L/2),2]; pos(4,:)=[pos(1,1)+round((2/3)*W*(s-1)),pos(1,2),H+pos(1,3)-1]; pos(5,:)=[pos(4,1)-W*s,pos(4,2)+round((L*s)/2),pos(4,3)]; plane=sym(’plane’,[1,3]); plane(1)=getPlane(pos(1,:),pos(2,:),pos(4,:)); plane(2)=getPlane(pos(1,:),pos(3,:),pos(4,:)); plane(3)=getPlane(pos(3,:),pos(2,:),pos(5,:)); z1=double(pos(4,3));z2=double(pos(1,3)); x1=double(pos(3,1));x2=double(pos(1,1)); y1=double(pos(2,2));y2=double(pos(3,2)); for z=z1:-1:z2 for x=x1:x2 for y=y1:y2 if eval(plane(1))>=z && eval(plane(2))>=z && eval(plane(3))>=z B(x,y,z)=1; end end end end B=insertWater(B,p); threePyramid=B; end

<!-- b000550 | prose | pages [26] -->
function rain=createRain(B,W,H) dim=size(B); p=H/(20*W); for x=2:dim(1)-1 for y=2:dim(2)-1 if rand(1)<p B(x,y,dim(3)-50)=-1; end end end rain=B; end

<!-- b000551 | prose | pages [26] -->
function water=insertWater(B,p) if p<1 waterNum = round(length(ﬁnd(B==1))*(1-p));

<!-- b000552 | prose | pages [26, 27] -->
关注数学模型 sx,sy,sz =getSandPos(B); sand=[sx,sy,sz]; for i=1:waterNum inserted=0; while inserted==0 randIndex=randi(length(sand)); point=sand(randIndex,:); if B(point(1),point(2),point(3))==- 1 continue else B(point(1),point(2),point(3))=-1; inserted=1; end end end end water=B; end

<!-- b000553 | furniture | pages [26] -->
2

<!-- b000554 | furniture | pages [26] -->
MATHmodels

<!-- b000555 | furniture | pages [26] -->
获取更多资讯

<!-- b000556 | furniture | pages [27] -->
Team # 2007698

<!-- b000557 | furniture | pages [27] -->
Page 26 of 29

<!-- b000559 | prose | pages [27] -->
function pos=moveSand(B) P=12; [sx,sy,sz]=getSandPos(B); sands = [sx,sy,sz].’; for sand = sands x=sand(1);y=sand(2);z=sand(3); if y<1 continue end if x<2 || y==1 B(x,y,z)=0; continue end if B(x,y,z-1)==0 B(x,y,z)=0; B(x,y,z-1)=1; continue end U=getClassNum(B,[x,y,z],1,-1); if U<P continue else K=getUnstableFactor(B,[x,y,z],U); if K<P continue else if (isempty(ﬁnd(B(x-1:x+1,y-1:y+1,z-1)==-1,1)) && isempty(ﬁnd(B(x-1:x+1,y-1:y+1,z-1)==0,1)))if B(x,y,z-1)==-1 B(x,y,z)=-1; B(x,y,z-1)=1; continue end set1=B(x-1,y-1:y+1,z-1).’; set2=B(x+1,y-1:y+1,z-1).’; set3=B(x-1:x+1,y-1,z-1); set4=B(x-1:x+1,y+1,z-1); sets=[set1,set2,set3,set4]; nums=zeros(1,4); for i=1:4 nums(i)=length(ﬁnd(sets(:,i)==-1)); end num,index =max(nums); if index==1 if B(x-1,y,z-1)==0 B(x,y,z)=0; B(x-1,y,z-1)=1; elseif B(x+1,y,z-1)==-1 B(x,y,z)=-1; B(x-1,y,z-1)=1; else if num==2 B(x,y,z)=-1; B(x-1,y+(-1)ˆrandi(2),z-1)=1; elseif num==1 if B(x-1,y-1,z-1)==-1 B(x,y,z)=-1; B(x-1,y-1,z-1)=1; else B(x,y,z)=-1; B(x-1,y+1,z-1)=1; end end end

<!-- b000560 | prose | pages [27] -->
elseif index==2 if B(x+1,y,z-1)==0 B(x,y,z)=0; B(x+1,y,z-1)=1; elseif B(x+1,y,z-1)==-1 B(x,y,z)=-1; B(x+1,y,z-1)=1; else if num==2 B(x,y,z)=-1; B(x+1,y+(-1)ˆrandi(2),z-1)=1; elseif num==1 if B(x+1,y-1,z-1)==-1 B(x,y,z)=-1; B(x+1,y-1,z-1)=1; else B(x,y,z)=-1; B(x+1,y+1,z-1)=1; end end end

<!-- b000561 | prose | pages [27] -->
elseif index==3 if B(x,y-1,z-1)==0 B(x,y,z)=0; B(x,y-1,z-1)=1; elseif B(x,y-1,z-1)==-1 B(x,y,z)=-1; B(x,y-1,z-1)=1; else if num==2 B(x,y,z)=-1; B(x+(-1)ˆrandi(2),y-1,z-1)=1; elseif num==1 if B(x-1,y-1,z-1)==-1 B(x,y,z)=-1; B(x-1,y-1,z-1)=1; else B(x,y,z)=-1; B(x+1,y-1,z-1)=1; end end end

<!-- b000562 | prose | pages [27, 28] -->
else if B(x,y+1,z-1)==0 B(x,y,z)=0; B(x,y+1,z-1)=1; elseif B(x,y+1,z-1)==-1 B(x,y,z)=-1; B(x,y+1,z-1)=1; else if num==2 B(x,y,z)=-1; B(x+(-1)ˆrandi(2),y+1,z-1)=1; elseif num==1 if B(x-1,y+1,z-1)==-1 B(x,y,z)=-1; B(x-1,y+1,z-1)=1; else B(x,y,z)=-1; B(x+1,y+1,z- 1)=1; end end end end continue else peerArea=B(x-1:x,y-1:y+1,z); peerClass=vertcat(ﬁnd(peerArea==0),ﬁnd(peerArea==-1)); peerClassNum=length(peerClass); if peerClassNum>0 if isempty(ﬁnd(mod(peerClass,2)==1, 1)) k=ﬁnd(mod(peerClass,2)==1); index=peerClass(k).’; randIndex=randi(length(index)); 关注数学模型 offset=index(randIndex); if B(x-1,y-1+ﬂoor(offset/2),z)==-1 B(x,y,z)=-1; B(x-1,y-1+ﬂoor(offset/2),z)=1; else B(x,y,z)=0; B(x-1,y-1+ﬂoor(offset/2),z)=1; end continue else if length(ﬁnd(mod(peerClass,2)==0))==2 if B(x,y+(-1)ˆrandi(2),z)==-1 B(x,y,z)=-1; B(x,y+(-1)ˆrandi(2),z)=1; else B(x,y,z)=0; B(x,y+(-1)ˆrandi(2),z)=1; end else offset=peerClass/2; if B(x,y-2+offset,z)==- 1 B(x,y,z)=-1; B(x,y-2+offset,z)=1; else B(x,y,z)=0; B(x,y-2+offset,z)=1; end end continue end end end end end end pos = B; end

<!-- b000563 | furniture | pages [27] -->
2

<!-- b000564 | furniture | pages [27] -->
MATHmodels

<!-- b000565 | furniture | pages [27] -->
获取更多资讯

<!-- b000566 | furniture | pages [28] -->
Team # 2007698

<!-- b000567 | furniture | pages [28] -->
Page 27 of 29

<!-- b000569 | prose | pages [28] -->
function pos=moveWater(B) [wx,wy,wz]=getWaterPos(B); sea = [wx,wy,wz].’; dim=size(B); for water = sea x=water(1);y=water(2);z=water(3); if (x==1||y==1||x>dim(1)-1||y>dim(2)- 1)&& y =0 B(x,y,z)=0; continue elseif y==0||x==0 continue end if getClassNum(B,[x,y,z],-1,1) >= 12 continue else underArea=B(x-1:x+1,y-1:y+1,z-1); underNull=ﬁnd(underArea==0); un- derNullNum=length(underNull); peerArea=B(x-1:x+1,y-1:y+1,z); peerNull=ﬁnd(peerArea==0); peerNullNum=length(peerNull); if underNullNum > 0 offset=getOffset(underNull); if mod(offset,3)==2 B(x,y,z)=0; B(x,y-1+ﬂoor(offset/3),z-1)=-1; elseif mod(offset,3)==0 B(x,y,z)=0; B(x+1,y-2+ﬂoor(offset/3),z- 1)=-1; elseif mod(offset,3)==1 B(x,y,z)=0; B(x-1,y-1+ﬂoor(offset/3),z-1)=-1; end continue elseif peerNullNum>0 offset=getOffset(peerNull); if mod(offset,3)==2 B(x,y,z)=0; B(x,y-1+ﬂoor(offset/3),z)=-1; elseif mod(offset,3)==0 B(x,y,z)=0; B(x+1,y-2+ﬂoor(offset/3),z)=-1; elseif mod(offset,3)==1 B(x,y,z)=0; B(x-1,y-1+ﬂoor(offset/3),z)=-1; end continue end end end pos = B; end

<!-- b000570 | prose | pages [28] -->
function pos=permeate(B,time,W,H) [wx,wy,wz]=getWaterPos(B); sea=[wx,wy,wz]; groundIndexs=ﬁnd(wz==2).’; p=H/(2*W); a1 = time/(2*W); a2 = round(a1); if (a1<=a2) && isempty(groundIndexs) for index=groundIndexs if rand(1)<=p x=sea(index,1);y=sea(index,2);z=sea(index,3); if x==0 || y==0 continue end B(x,y,z)=0; end end end pos=B; end

<!-- b000571 | prose | pages [28] -->
function wave=createWave(B,time,W,H) d = size(B); x = d(1)-1; a1 = time/(2*W); a2 = round(a1); if a1<=a2 wave=B; else h=ceil(2*H*sin(2*pi*time/W)); if h<2 h=2; end B(x,:,2:h+1) = -1; wave=B; end end

<!-- b000572 | prose | pages [28] -->
function equation=getPlane(A,B,C) syms x y jz D=[ones(4,1),[[x,y,jz];A;B;C]];detd=det(D); z=solve(detd,jz);equation=z; end

<!-- b000573 | prose | pages [28, 29] -->
function k=getUnstableFactor(B,Pos,factor) x=Pos(1);y=Pos(2);z=Pos(3); p=0.02; area=B(x-1:x+1,y-1:y+1,z-1:z+1); angles=[1,3,7,9,19,21,25,27]; edges=[2,4,6,8,10,12,16,18,20,22,24,26]; centers=[5,11,13,15,17,23]; indexs=ﬁnd(area==1).’; for index=indexs dz=ceil(index/9); dx=mod(mod(index,9),3); if dx==0 dx=3; end dy=ceil(mod(index,9)/3); if dy==0 dy=3; end 关注数学模型 if isempty(ﬁnd(angles==index,1)) if dx>2 a=area(2:dx,:,:); else a=area(dx:2,:,:); end if dy>2 a=a(:,2:dy,:); else a=a(:,dy:2,:); end if dz>2 a=a(:,:,2:dz); else a=a(:,:,dz:2); end count=length(ﬁnd(a==-1)); factor=factor-(p*count); elseif isempty(ﬁnd(edges==index,1)) if dx==2 if dy>2 a=area(:,2:dy,:); else a=area(:,dy:2,:); end if dz>2 a=a(:,:,2:dz); else a=a(:,:,dz:2); end elseif dy==2 if dx>2 a=area(2:dx,:,:); else a=area(dx:2,:,:); end if dz>2 a=a(:,:,2:dz); else a=a(:,:,dz:2); end elseif dz==2 if dy>2 a=area(:,2:dy,:); else a=area(:,dy:2,:); end if dx>2 a=a(2:dx,:,:); else a=a(dx:2,:,:); end end count=length(ﬁnd(a==-1)); factor=factor-(p*count); elseif isempty(ﬁnd(centers==index,1)) if dx =2 if dx>2 a=area(2:dx,:,:); else a=area(dx:2,:,:); end elseif dy =2 if dy>2 a=area(:,2:dy,:); else a=area(:,dy:2,:); end elseif dz =2 if dz>2 a=area(:,:,2:dz); else a=area(:,:,dz:2); end end count=length(ﬁnd(a==-1)); factor=factor-(p*count); else factor=factor+0; end end k=factor; end

<!-- b000574 | furniture | pages [28] -->
2

<!-- b000575 | furniture | pages [28] -->
MATHmodels

<!-- b000576 | furniture | pages [28] -->
获取更多资讯

<!-- b000577 | furniture | pages [29] -->
Team # 2007698

<!-- b000578 | furniture | pages [29] -->
Page 28 of 29

<!-- b000580 | prose | pages [29] -->
function offset=getOffset(posNull) if isempty(ﬁnd(mod(posNull,3)==1, 1)) k=ﬁnd(mod(posNull,3)==1); index=posNull(k).’; randIndex=randi(length(index)); offset=index(randIndex); else randIn- dex=randi(length(posNull)); offset=posNull(randIndex); end end

<!-- b000581 | prose | pages [29] -->
function num=getClassNum(B,Pos,rowClass,assignClass) x=Pos(1);y=Pos(2);z=Pos(3); area=B(x-1:x+1,y-1:y+1,z-1:z+1); num=length(ﬁnd(area==assignClass)); if rowClass==assignClass num=num-1; end end

<!-- b000582 | prose | pages [29] -->
function num=getSandNum(B,h) num=length(ﬁnd(z==(h+1))); end

<!-- b000583 | prose | pages [29] -->
function draw(B,time,g) dim=size(B); [x1,y1,z1]=getWaterPos(B); [x2,y2,z2]=getSandPos(B); [x3,y3,z3]=getLandPos(B); ﬁgure(1) clf(’reset’); hold off h3=scatter3(x3,y3,z3,’MarkerEdgeColor’,[1 .75 0],’MarkerFaceColor’,[1 .75 0]); h3.DisplayName=’Land Cell’; xlim([0 dim(1)]) ylim([1 dim(2)]) zlim([0 dim(3)]) title([’time=’,num2str(time),’ G=’,num2str(g)]); hold on h1=scatter3(x1,y1,z1,’MarkerEdgeColor’,[0 .75 .75],’MarkerFaceColor’,[0 .75 .75]); h1.DisplayName=’Water Cell’; hold on h2=scatter3(x2,y2,z2,’MarkerEdgeColor’,[.6 .2 0],’MarkerFaceColor’,[.6 .2 0]); h2.DisplayName=’Sand Cell’; view(218,46); end

<!-- b000584 | prose | pages [29] -->
function [x,y,z]=getWaterPos(B) dim = size(B);

<!-- b000585 | prose | pages [29] -->
wX,wY = ﬁnd(B==-1); water = [wX,mod(wY,dim(2)),ceil(wY./dim(2))]; x=water(:,1);y=water(:,2);z=water(:,3); end

<!-- b000586 | prose | pages [29] -->
function [x,y,z]=getSandPos(B) 关注数学模型 dim = size(B);

<!-- b000587 | furniture | pages [29] -->
2

<!-- b000588 | furniture | pages [29] -->
MATHmodels

<!-- b000589 | furniture | pages [29] -->
获取更多资讯

<!-- b000590 | furniture | pages [30] -->
Team # 2007698

<!-- b000591 | furniture | pages [30] -->
Page 29 of 29

<!-- b000592 | prose | pages [30] -->
sX,sY = ﬁnd(B==1); sand = [sX,mod(sY,dim(2)),ceil(sY./dim(2))]; x=sand(:,1);y=sand(:,2);z=sand(:,3); end

<!-- b000593 | prose | pages [30] -->
function [x,y,z]=getLandPos(B) dim = size(B);

<!-- b000594 | prose | pages [30] -->
lX,lY = ﬁnd(B==2); land = [lX,mod(lY,dim(2)),ceil(lY./dim(2))]; x=land(:,1);y=land(:,2);z=land(:,3); end

<!-- b000595 | prose | pages [30] -->
关注数学模型

<!-- b000596 | furniture | pages [30] -->
2

<!-- b000597 | furniture | pages [30] -->
MATHmodels

<!-- b000598 | furniture | pages [30] -->
获取更多资讯
