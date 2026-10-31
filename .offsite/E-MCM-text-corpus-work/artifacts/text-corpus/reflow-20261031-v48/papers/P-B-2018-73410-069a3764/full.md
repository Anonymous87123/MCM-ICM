# P-B-2018-73410-069a3764

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000002 | front_matter | pages [1] -->
Team Control Number

<!-- b000003 | front_matter | pages [1] -->
For office use only For office use only

<!-- b000004 | front_matter | pages [1] -->
73410

<!-- b000005 | prose | pages [1] -->
T1 F1 T2 F2 T3 Problem Chosen F3

<!-- b000006 | front_matter | pages [1] -->
B

<!-- b000007 | prose | pages [1] -->
T4 F4

<!-- b000008 | front_matter | pages [1] -->
2018

<!-- b000009 | prose | pages [1] -->
MCM/ICM

<!-- b000010 | heading | pages [1] -->
Summary Sheet

<!-- b000011 | title | pages [1] -->
Language Population Projection and Location

<!-- b000012 | title | pages [1] -->
Optimizaion Model Based on Inhomogeneous

<!-- b000013 | title | pages [1] -->
Transition Matrix and Simulated Annealing

<!-- b000014 | title | pages [1] -->
Algorithm

<!-- b000015 | heading | pages [1] -->
Summary

<!-- b000016 | prose | pages [1] -->
With the advent of increasingly accelerated globalization, the intricate ge- ographic distributions of languages start to hamper international business op- erations and cross-culture interactions. Comprehending the distribution dy- namics has never been more crucial, yet projecting the distributions is difficult, particularly due to the complicated composition of speakers, the influence of various exogenous factors like the migration, government policies, economic development, and eagerness to learn. Therefore, we establish a new model to replace the projection model based purely on population, as it is not only inaccurate but also invalid faced with the scarcity of supporting data.

<!-- b000017 | prose | pages [1] -->
Our model focuses on native speakers and non-native speakers of lan- guages. We introduce the transition matrix to describe the transition between native speakers and non-native speakers of different languages, because the population growth of a language doesn’t solely come from natural births, but also migration and learning. Additionally, we introduce two new groups: learners and migrants to further analyze the transition. In the end, we intro-duce a set of parameters to represent the exogenous influences, a new variable to express time changes, and establish our inhomogeneous transition matrix.

<!-- b000018 | prose | pages [1] -->
It has been tested that our matrix only requires relatively little amount of data input to function well. We employ the model to successfully project the geographic distributions of languages in 2067, based on the data in 2017. In the end, we adopt the simulated annealing algorithm to help our client, a large multinational service corporation, select optimal location options for new of-fices.

<!-- b000019 | keywords | pages [1] -->
Keywords: Population of languages, Transition, Office locations

<!-- b000020 | furniture | pages [2] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000021 | furniture | pages [2] -->
Team # 73410

<!-- b000022 | furniture | pages [2] -->
Page 1 of 27

<!-- b000023 | heading | pages [2] -->
Contents

<!-- b000024 | contents | pages [2] -->
1 Introduction

<!-- b000025 | contents | pages [2] -->
2

<!-- b000026 | contents | pages [2] -->
2 Preliminary Model

<!-- b000027 | contents | pages [2] -->
2

<!-- b000028 | contents | pages [2] -->
2.1

<!-- b000029 | contents | pages [2] -->
Notations and Symbol Description . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000030 | contents | pages [2] -->
2

<!-- b000031 | contents | pages [2] -->
2.1.1

<!-- b000032 | contents | pages [2] -->
Symbol Description . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000033 | contents | pages [2] -->
2

<!-- b000034 | contents | pages [2] -->
2.1.2

<!-- b000035 | contents | pages [2] -->
Notations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000036 | contents | pages [2] -->
3

<!-- b000037 | contents | pages [2] -->
2.2

<!-- b000038 | contents | pages [2] -->
General Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000039 | contents | pages [2] -->
3

<!-- b000040 | contents | pages [2] -->
2.3

<!-- b000041 | contents | pages [2] -->
Analysis of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000042 | contents | pages [2] -->
3

<!-- b000043 | contents | pages [2] -->
2.3.1

<!-- b000044 | contents | pages [2] -->
N=2 Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000045 | contents | pages [2] -->
4

<!-- b000046 | contents | pages [2] -->
2.4

<!-- b000047 | contents | pages [2] -->
Calculating and Simplifying the Model . . . . . . . . . . . . . . . . . . . .

<!-- b000048 | contents | pages [2] -->
6

<!-- b000049 | contents | pages [2] -->
2.5

<!-- b000050 | contents | pages [2] -->
The Model Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000051 | contents | pages [2] -->
8

<!-- b000052 | contents | pages [2] -->
3 Modified Model

<!-- b000053 | contents | pages [2] -->
9

<!-- b000054 | contents | pages [2] -->
3.1 Notations and Symbool Description . . . . . . . . . . . . . . . . . . . . . .

<!-- b000055 | contents | pages [2] -->
9

<!-- b000056 | contents | pages [2] -->
3.1.1

<!-- b000057 | contents | pages [2] -->
Additional Notations . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000058 | contents | pages [2] -->
9

<!-- b000059 | contents | pages [2] -->
3.1.2

<!-- b000060 | contents | pages [2] -->
Additional Symbol Description . . . . . . . . . . . . . . . . . . . . .

<!-- b000061 | contents | pages [2] -->
10

<!-- b000062 | contents | pages [2] -->
3.2 Additional Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000063 | contents | pages [2] -->
10

<!-- b000064 | contents | pages [2] -->
3.3 Analysis of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000065 | contents | pages [2] -->
10

<!-- b000066 | contents | pages [2] -->
3.4 Calculating and Simplifying the Model . . . . . . . . . . . . . . . . . . . .

<!-- b000067 | contents | pages [2] -->
12

<!-- b000068 | contents | pages [2] -->
3.5 The Model Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000069 | contents | pages [2] -->
13

<!-- b000070 | contents | pages [2] -->
3.5.1

<!-- b000071 | contents | pages [2] -->
Graph of Population of Different Language Groups . . . . . . . . .

<!-- b000072 | contents | pages [2] -->
13

<!-- b000073 | contents | pages [2] -->
3.5.2

<!-- b000074 | contents | pages [2] -->
Graph of the Scale of Migration . . . . . . . . . . . . . . . . . . . . .

<!-- b000075 | contents | pages [2] -->
14

<!-- b000076 | contents | pages [2] -->
3.5.3

<!-- b000077 | contents | pages [2] -->
Distribution of Non-native English Speakers . . . . . . . . . . . . .

<!-- b000078 | contents | pages [2] -->
14

<!-- b000079 | contents | pages [2] -->
3.6 Sensitivity Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000080 | contents | pages [2] -->
15

<!-- b000081 | contents | pages [2] -->
3.6.1

<!-- b000082 | contents | pages [2] -->
High Uniformity Scenario . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000083 | contents | pages [2] -->
15

<!-- b000084 | contents | pages [2] -->
3.6.2

<!-- b000085 | contents | pages [2] -->
Low Uniformity Scenario . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000086 | contents | pages [2] -->
16

<!-- b000087 | contents | pages [2] -->
4 Application of Our Model

<!-- b000088 | contents | pages [2] -->
17

<!-- b000089 | contents | pages [2] -->
4.1

<!-- b000090 | contents | pages [2] -->
Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000091 | contents | pages [2] -->
17

<!-- b000092 | contents | pages [2] -->
4.2

<!-- b000093 | contents | pages [2] -->
Symbol Descrption . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000094 | contents | pages [2] -->
18

<!-- b000095 | contents | pages [2] -->
4.3

<!-- b000096 | contents | pages [2] -->
Calculating and Simplifying . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000097 | contents | pages [2] -->
18

<!-- b000098 | contents | pages [2] -->
4.3.1

<!-- b000099 | contents | pages [2] -->
The Year of 2017 . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000100 | contents | pages [2] -->
18

<!-- b000101 | contents | pages [2] -->
4.3.2

<!-- b000102 | contents | pages [2] -->
The Year of 2067 . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000103 | contents | pages [2] -->
19

<!-- b000104 | contents | pages [2] -->
5 Strengths and Weaknesses

<!-- b000105 | contents | pages [2] -->
20

<!-- b000106 | contents | pages [2] -->
6 Memo

<!-- b000107 | contents | pages [2] -->
21

<!-- b000108 | contents | pages [2] -->
Appendices

<!-- b000109 | contents | pages [2] -->
24

<!-- b000110 | furniture | pages [3] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000111 | furniture | pages [3] -->
Team # 73410

<!-- b000112 | furniture | pages [3] -->
Page 2 of 27

<!-- b000113 | heading | pages [3] -->
Appendix A Tables

<!-- b000114 | prose | pages [3] -->
24

<!-- b000115 | heading | pages [3] -->
Appendix B Figures

<!-- b000116 | prose | pages [3] -->
26

<!-- b000117 | heading | pages [3] -->
1 Introduction

<!-- b000118 | prose | pages [3] -->
There are about 6,900 languages spoken on Earth nowadays. About half of the world’s population take one of ten languages as their native language and much of the world population also speaks a second language. However, because of a variety of influences, the population of speakers of a language may increase or decrease over time. Our target is to investigate trends of global languages and location options for new offices.

<!-- b000119 | prose | pages [3] -->
In part I, we compared our problem with the idea of Markov chain, and add transition matrix to describe the population transition from native speakers of a language to second language speakers of another language to native speakers of another language. Consid- ering that transitions are inhomogeneous, we finally built up inhomogeneous transition matrix and used this matrix to predict the populations of different languages and their geographical distribution. In part II, based on prediction of our model in part I, we used simulated annealing algorithm to find the best location options for new offices.

<!-- b000120 | heading | pages [3] -->
2 Preliminary Model

<!-- b000121 | heading | pages [3] -->
2.1 Notations and Symbol Description

<!-- b000122 | heading | pages [3] -->
2.1.1 Symbol Description

<!-- b000123 | prose | pages [3] -->
Symbol Descrption N The number of languages in consideration Yi(n)(i = 1; 2; :::; N; n = 0; 1; 2:::) The number of native speakers of language i in the year of n yi(n)(i = 1; 2; :::; N; n = 0; 1; 2:::) The number of non-native speakers of language i in the year of n the state vector of the model in the year of n Y(n) A The transition matrix The annual birth rate of native speakers of language i ii The annual proportion of non-native speakers of i(N+i) language i giving birth to native speakers of this language The annual death rate of native speakers of language i ii The annual death rate of non-native speakers of (N+i)(N+i) language i The annual proportion (learning rate) of native speakers (N+i)j of language j successfully starting to master language i The total learning rate of language i i

<!-- b000124 | furniture | pages [4] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000125 | furniture | pages [4] -->
Team # 73410

<!-- b000126 | furniture | pages [4] -->
Page 3 of 27

<!-- b000127 | heading | pages [4] -->
2.1.2 Notations

<!-- b000128 | prose | pages [4] -->
Native speakers of A are individuals whose first language is A.

<!-- b000129 | prose | pages [4] -->
Non-native speakers of A are individuals whose first language is not A, but who master A as a foreign language (Implying that the individual possesses advanced skills of language A and is fluent in both speaking and writing).

<!-- b000130 | heading | pages [4] -->
2.2 General Assumptions

<!-- b000131 | prose | pages [4] -->
1. Speakers of any particular language can be categorized into two groups: native speakers and non-native speakers.

<!-- b000132 | prose | pages [4] -->
2. The number of native speakers only increases out of natural birth, and all new- born babies remain native speakers at the year of their birth (Leaving out rare cases of prodigies who can instantly learn to speak foreign languages); The number of native speakers is only reduced by death (Leaving out rare cases of postnatal first language disability).

<!-- b000133 | prose | pages [4] -->
3. Native speakers of a certain language cannot be converted to non-native speakers of this language, but can become non-native speakers of other languages.

<!-- b000134 | prose | pages [4] -->
4. The number of non-native speakers only increases out of postnatal learning, and only decreases due to death (Leaving out rare cases of forgetting learnt foreign lan-guages).

<!-- b000135 | prose | pages [4] -->
5. Non-native speakers of a certain language cannot be converted to native speakers of this language, but can become non-native speakers of other languages.

<!-- b000136 | prose | pages [4] -->
6. Once an individual has mastered a new language, he becomes a non-native speaker of this language, while remaining all previous identities.

<!-- b000137 | prose | pages [4] -->
7. No radical and unpredicted events will occur, causing utter shifting in the popula- tion structure.

<!-- b000138 | heading | pages [4] -->
2.3 Analysis of the Problem

<!-- b000139 | prose | pages [4] -->
It is apparent that native speakers and non-native speakers of the same language are more closely related, which mainly reflects in:

<!-- b000140 | prose | pages [4] -->
1. Parents usually raise their children to have the same first languages, or at least languages they master. Therefore, we can assume that new native speakers can only be given birth to by native speakers or non-native speakers of the same language (Leaving out refugees, asylum seekers etc.).

<!-- b000141 | prose | pages [4] -->
2. It’s unlikely that native speakers of a certain language can abandon their first lan- guage. Therefore, we can assume that no native speakers of a certain language can be converted to non-native speakers of this language (Leaving out rare cases of postnatal first language disability).

<!-- b000142 | furniture | pages [5] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000143 | furniture | pages [5] -->
Team # 73410

<!-- b000144 | furniture | pages [5] -->
Page 4 of 27

<!-- b000145 | prose | pages [5] -->
Furthermore, A number of people who cannot master a certain language will be con-verted to non-native speakers of this language through learning every year. There will also be natural deaths causing the number of each group of people to drop.

<!-- b000146 | heading | pages [5] -->
2.3.1 N=2 Model

<!-- b000147 | prose | pages [5] -->
Take the simplest model with only two languages (N = 2) as an example, we are able to plot the transition between different groups of people (See Figure 1).

<!-- b000148 | caption | pages [5] -->
Figure 1: Transition Between Different Groups with Only Two Languages

<!-- b000149 | prose | pages [5] -->
It can be concluded that this model much resembles the model of homogeneous Markow chain (After converted to the new group, the element will remain in the previous groups). The transition follows the following rules:

<!-- b000150 | prose | pages [5] -->
In expression (1), parameters are set as follows:

<!-- b000151 | prose | pages [5] -->
1. 11; 22 represents the annual birth rate of native speakers of language 1 and 2 re- spectively.

<!-- b000152 | prose | pages [5] -->
2. 11; 22 represents the annual death rate of native speakers of language 1 and 2 respectively.

<!-- b000153 | prose | pages [5] -->
3. 13; 24 represents the ratio of non-native speakers of language 1 and 2 giving birth to native speakers of corresponding language respectively (Assuming all births are single births).

<!-- b000154 | furniture | pages [6] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000155 | furniture | pages [6] -->
Team # 73410

<!-- b000156 | furniture | pages [6] -->
Page 5 of 27

<!-- b000157 | prose | pages [6] -->
4. 32; 41 represents the ratio of native speakers of language 1 and 2 learn to speak the other language respectively.

<!-- b000158 | prose | pages [6] -->
5. 33; 44 represents the annual death rate of non-native speakers of language 1 and 2 respectively.

<!-- b000159 | prose | pages [6] -->
6. It should be noted that we set zero the (3; 4) and the (4; 3) element in the matrix to prevent double counting.

<!-- b000160 | prose | pages [6] -->
7. Additionally, we also set zero the (1; 4) and the (2; 3) element to prevent double counting (e.g. offspring of people who are native speakers of language 1 and non- native speakers of language 2 will be counted twice).

<!-- b000161 | prose | pages [6] -->
If the transition reaches a steady state (Implying that each group takes up a steady split of total population, rather than in terms of absolute quantity), it can be derived:

<!-- b000162 | prose | pages [6] -->
is the growth rate of total population, Y(0) is an arbitrary initial vector,Y is a con- stant vector.

<!-- b000163 | prose | pages [6] -->
When the transition reaches the steady state, we have:

<!-- b000164 | prose | pages [6] -->
Obviously, is the eigenvalue of matrix A, and Y is the eigenvector of this matrix. We can derive the proportion of each group through matrix normalization Y.

<!-- b000165 | prose | pages [6] -->
To simplify the test of this model, let’s consider a particular scenario with following parameters:

<!-- b000166 | prose | pages [6] -->
The transition matrix is:

<!-- b000167 | prose | pages [6] -->
This matrix possesses four different eigenvalues, and only when = 1:01049, can the eigenvector be positive semidefinite vector (all elements are non-negative):

<!-- b000168 | prose | pages [6] -->
This is the steady state of language population structure, which represents that no matter what the initial distribution is, non-native speakers of these two languages will both take up 1:124 of the total population.

<!-- b000169 | furniture | pages [7] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000170 | furniture | pages [7] -->
Team # 73410

<!-- b000171 | furniture | pages [7] -->
Page 6 of 27

<!-- b000172 | prose | pages [7] -->
Apparently, in the bilingual (N = 2) model, the number of non-native speakers of each language exceeds that of native speakers of each language, which poses an indi- rect constraint on the range of parameter (learning rate). By employing the Matlab, we derive the quantitative influence of learning rate on the proportion of non-native speakers.

<!-- b000173 | caption | pages [7] -->
Figure 2: Correlation Between the Proportion of Non-native Speakers and Learning

<!-- b000174 | prose | pages [7] -->
Rate ( )

<!-- b000175 | prose | pages [7] -->
We can see in (Figure 2), when > 0:021, the proportion of non-native speakers ex- ceeds that of native speakers. Therefore, this model cannot stay at a learning rate greater than 0.021 in the long run.

<!-- b000176 | heading | pages [7] -->
2.4 Calculating and Simplifying the Model

<!-- b000177 | prose | pages [7] -->
Since the top twenty-six languages cover most of the world population, we have rea- son to believe that the majority of verbal communications and information exchanges are conducted through these twenty-six languages. Due to limited data[1], we will only be analyzing twenty-two major languages out of these twenty-six languages in this sub- section (We will come back to the twenty-six-language model in the following sections). Thus, we only consider a model with twenty-two languages (N = 22), and the transition matrix for this model is:

<!-- b000178 | prose | pages [7] -->
To make a more accurate projection, we should set the values of parameters in this model to better fit the real scenario:

<!-- b000179 | prose | pages [7] -->
1. Given that native speakers of different languages have distinctive birth rates and death rates, we introduce a set of new data to reflect the difference[1].

<!-- b000180 | prose | pages [7] -->
To derive the birth rate and death rate of different language groups, we first catego-rize nations by official language, and select several major nations to represent each group (Total number of native speakers in these countries taking up more than 90% of the total number of native speakers of this language worldwide). We have the following table in Appendix A.

<!-- b000181 | furniture | pages [7] -->
Team # 73410

<!-- b000182 | furniture | pages [7] -->
Page 7 of 27

<!-- b000183 | furniture | pages [8] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000184 | prose | pages [8] -->
We draw upon public sources for population, annual birth rate and death rate of aforementioned nations (2013). We then compute the weighted average an-nual birth rate and death rate of language groups, and list in the table in Ap-pendix A)[4][5] 2. Since non-native speakers of a language can come from any nations (other than nations where this language is commonly regarded as first language), we may as well assume non-native speakers of different languages share the same birth rate and death rate (equal to world average death rate):

<!-- b000185 | prose | pages [8] -->
Drawing upon public sources, world average death rate: = 0:0083; world average birth rate: = 0:0193, and the proportion of immigrants to non-native speakers of a certain language is: r = 0:172, Therefore, we may assume:

<!-- b000186 | prose | pages [8] -->
3. Considering different languages bear different level of attractiveness, the learning rate for each language should also be different. To simplify the model, it is rea- sonable for us to assume a language is indifferently attractive to different groups of people, therefore leading to the same learning rate amongst different groups, though it may not be the real case.

<!-- b000187 | prose | pages [8] -->
The learning rate (shown above) is a constant rate. We can temporarily assume that the learning rate of a language equals the proportion of its non-native speakers to total non-native speakers, multiplied by the total learning rate.

<!-- b000188 | prose | pages [8] -->
Note that the last equation is normalized.

<!-- b000189 | prose | pages [8] -->
Therefore, the annual learning rate (N+j);i from group i to group j (non-native speakers) is the normalization ratio y^j(0) shown, multiplied by the group’s annual total learning rate i, which is:

<!-- b000190 | prose | pages [8] -->
The modified transition matrix is too huge (44 44), so we will not present it here to save space:

<!-- b000191 | furniture | pages [9] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000192 | furniture | pages [9] -->
Team # 73410

<!-- b000193 | furniture | pages [9] -->
Page 8 of 27

<!-- b000194 | heading | pages [9] -->
2.5 The Model Results

<!-- b000195 | prose | pages [9] -->
We use data in 2013 to establish the initial vector Y(0), and obtain the projected statistics in 2017 after four alterations. Y(4) = A4Y(0) (Presenting only the top 10 figures) (Table 1):

<!-- b000196 | prose | pages [9] -->
Language Native Native Non-native Non-native (predict) (real) (predict) (real) Mandarin 870 897 180 193 English 353 371 521 611 Spanish 422 436 92 91 Hindi/Urdu 340 329 219 215 Russian 170 153 27 113 Portuguese 206 218 31 11 Bengali 201 242 20 19 French 78 76 89 153 Japanese 129 128 ? ?

<!-- b000197 | prose | pages [9] -->
German 78 76 8 52

<!-- b000198 | caption | pages [9] -->
Table 1: Projections for Population Statistics of Major Languages in 2017

<!-- b000199 | prose | pages [9] -->
There are deviations between projected and real statistics in a number of items, like the number of non-native German speakers. To quote the data in 2013, there are only eight million non-native German speakers, whereas the figure reaches fifty-two million in 2017. This apparently goes against common sense, so we believe that these deviations are mostly caused by the inaccuracy of the data (In fact the inaccuracy of the data is also pronounced by the data source itself).

<!-- b000200 | prose | pages [9] -->
The data in 2013 is in Appendix A[1].

<!-- b000201 | prose | pages [9] -->
Additionally we can compute the positive semidefinite eigenvector Y (Normalized according to statistics of the former 22 groups) and the eigenvalue of the transition matrix A:

<!-- b000202 | prose | pages [9] -->
These two items have corresponding practical meanings:

<!-- b000203 | prose | pages [9] -->
1. Eigenvector: the equilibrium ratio (in the long run) of the population of each group to total population.

<!-- b000204 | prose | pages [9] -->
2. Eigenvalue: the equilibrium total growth rate (in the long run) (accumulated growth rate of all language groups).

<!-- b000205 | prose | pages [9] -->
We can find that native speakers of Panjabi will take up more than 96% of total pop- ulation when reaching equilibrium, which obviously goes against common sense. The reason why this phenomenon takes place is that the birth rate of native speaker of Pan- jabi is the highest (0.0286) amongst all native speaker groups, and that the group with the highest growth rate will dominate in a homogeneous model.

<!-- b000206 | prose | pages [9] -->
Therefore, to conduct a more accurate projection in the long run, we must introduce time as a new variable into the model, or rather: an inhomogeneous model.

<!-- b000207 | furniture | pages [10] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000208 | furniture | pages [10] -->
Team # 73410

<!-- b000209 | furniture | pages [10] -->
Page 9 of 27

<!-- b000210 | heading | pages [10] -->
3 Modified Model

<!-- b000211 | prose | pages [10] -->
The aforementioned preliminary model yields quite accurate projections for population of different language groups in the short run. However, the model is lacking in accuracy when it comes to long-run projections. Defects of the model are:

<!-- b000212 | prose | pages [10] -->
1. No regard to the process of learning a language, which implies that it takes time for an individual to master a new language, and that the length of time is influenced by education level, language similarity (e.g. English is more similar to French than to Mandarin), and eagerness to learn

<!-- b000213 | prose | pages [10] -->
2. No regard to the change of birth rate and death rate over time

<!-- b000214 | prose | pages [10] -->
3. No regard to the economic development over time

<!-- b000215 | prose | pages [10] -->
4. Fail to reveal the exact impact of population migration

<!-- b000216 | prose | pages [10] -->
5. Fail to derive the distribution of English population group as requested by our client

<!-- b000217 | prose | pages [10] -->
Therefore, building upon the preliminary model, we introduce time as a new vari- able to better fit the real case. Furthermore, we introduce a new dimension of variables (language learners, migrants, a breakdown of English speakers) to observe the process of learning and migration.

<!-- b000218 | prose | pages [10] -->
Note: For convenience, we number English as 1, and Chinese as 2.

<!-- b000219 | heading | pages [10] -->
3.1 Notations and Symbool Description

<!-- b000220 | heading | pages [10] -->
3.1.1 Additional Notations

<!-- b000221 | prose | pages [10] -->
Learners of language B from language A are native speakers of language A who are starting to learn language B (not non-native speakers of language B). Language group (region) A are regions where native speakers of language A take resi- dence (Implying that the total population of language region A is the population of native speakers of language A, and that we use the economic data of aforemen- tioned major countries to represent their corresponding language groups (regions)).

<!-- b000222 | prose | pages [10] -->
Migrants to language B region are non-native speakers of language B whose offspring is native speaker of language B, or rather the first-generation immigrants.

<!-- b000223 | prose | pages [10] -->
Decrease matrix is the matrix evaluating the natural death and migration of a language group.

<!-- b000224 | furniture | pages [11] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000225 | furniture | pages [11] -->
Team # 73410

<!-- b000226 | furniture | pages [11] -->
Page 10 of 27

<!-- b000227 | heading | pages [11] -->
3.1.2 Additional Symbol Description

<!-- b000228 | heading | pages [11] -->
3.2 Additional Assumptions

<!-- b000229 | prose | pages [11] -->
1. The birth rate and death rate of each group is not affected by the population of each group, and only changes over time.

<!-- b000230 | prose | pages [11] -->
2. An individual will not be born as a learner (Implying that the number of learners only increase due to learning, not reproduction), and will not die during learn-ing (However, the natural death rate will not be affected, since learners are mostly young and unlikely to die).

<!-- b000231 | prose | pages [11] -->
3. Offspring of migrants will be considered as native speakers of the language region they migrate into.

<!-- b000232 | prose | pages [11] -->
4. Once an individual successfully migrates into a foreign language region, he will not be considered a non-native speaker of this language (Implying that the non- native speaker group in the aforementioned preliminary model can actually be broken down into two groups in this model: non-speaker group and migrant group of this language).

<!-- b000233 | heading | pages [11] -->
3.3 Analysis of the Problem

<!-- b000234 | prose | pages [11] -->
Example graph of transition between different groups in a bilingual model with regard to learners and immigrants is shown below (Figure 3):

<!-- b000235 | furniture | pages [12] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000236 | furniture | pages [12] -->
Team # 73410

<!-- b000237 | furniture | pages [12] -->
Page 11 of 27

<!-- b000238 | caption | pages [12] -->
Figure 3: Example Graph of Transition Between Different Groups in a Bilingual Model

<!-- b000239 | prose | pages [12] -->
The transition matrix in the year of n is:

<!-- b000240 | furniture | pages [13] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000241 | furniture | pages [13] -->
Team # 73410

<!-- b000242 | furniture | pages [13] -->
Page 12 of 27

<!-- b000243 | prose | pages [13] -->
If we want to analyze the distribution of English speakers separately, we should mod-ify the aforementioned matrix as follows:

<!-- b000244 | prose | pages [13] -->
It should be noted that we only consider the distribution of non-native English speak-ers in the aforementioned matrixes, but the distribution of English speakers can be influ-enced by emigrants of native English speakers. However, since the number of non-native speakers far exceeds that of emigrants’, we’ll leave out such an influence.

<!-- b000245 | prose | pages [13] -->
We have considered three exogenous factors in total:

<!-- b000246 | prose | pages [13] -->
1. Government policy factor will influence parameter pij and rj.

<!-- b000247 | prose | pages [13] -->
2. Economic factor and initial population factor will influence parameter pij and rj.

<!-- b000248 | prose | pages [13] -->
3. Education factor will influence parameter i and ai

<!-- b000249 | heading | pages [13] -->
3.4 Calculating and Simplifying the Model

<!-- b000250 | prose | pages [13] -->
We take the year of 2017 as the starting year. Since the top twenty-six languages cover most of the world population, we have reason to believe that the majority of verbal communications and information exchanges are conducted through these twenty-six lan-guages. Therefore, we only consider a model with twenty-six languages (N = 26).

<!-- b000251 | prose | pages [13] -->
Prior to determining the transition matrix, we should first set the initial vector, which stands for the initial distribution of non-native English speakers. We assume the initial distribution of non-native English speakers to be proportional to the distribution of na- tive speakers in total, which is:

<!-- b000252 | prose | pages [13, 14] -->
To save time, we adopt the annual birth rate, death rate and migration rate projected for the next fifty years by United Nations. We employ the weighted average method to compute the birth rate, death rate and migration rate in the upcoming fifty years, and plot the trend in passing. See: Apendix B Building upon these data, we can set: , 1, , ,S,R1,R. Then we should attempt to set G; G1:

<!-- b000253 | furniture | pages [13] -->
Team # 73410

<!-- b000254 | furniture | pages [13] -->
Page 13 of 27

<!-- b000255 | furniture | pages [14] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000257 | prose | pages [14] -->
The learning rate ji(n) from language group i to language j satisfies that:

<!-- b000258 | prose | pages [14] -->
We assume the eagerness p(jin) to learn is proportional to the number of non-native speakers of language j (Assuming that people’s eagerness to learn a language in the past reflects people’s eagerness to learn this language in the future):

<!-- b000259 | prose | pages [14] -->
We assume that any two languages from the same language family have the first- level similarity (Implying a similarity parameter equal to 1), whereas any two languages from different language families have the second-level similarity (Implying a similarity parameter equal to 2), which can be expressed as:

<!-- b000260 | prose | pages [14] -->
This implies that one in a hundred people start to learn a foreign language annually in each country. On average, it takes them three years to master a foreign language from the same language family as their first language, and six years if from different language families.

<!-- b000261 | heading | pages [14] -->
3.5 The Model Results

<!-- b000262 | heading | pages [14] -->
3.5.1 Graph of Population of Different Language Groups

<!-- b000263 | prose | pages [14] -->
We will skip the computation process to save space. Through repeated alterations, we can plot the graph of population of different language groups in the next fifty years (Figure 4).

<!-- b000264 | prose | pages [14] -->
Based on the projections, we can align the top ten languages in terms of population in 2017 and 2067: (Table 2):

<!-- b000265 | prose | pages [14] -->
According to this ranking, Portuguese and French both drop out of the top ten, whereas Hausa and Punjabi make it to the top ten. We observe the following patterns for lan-guages whose ranking elevates:

<!-- b000266 | prose | pages [14, 15] -->
1. High birth rate, e.g. Hausa and Punjabi 2. For language groups whose migration is mostly immigration, belonging to a bigger family (more languages from the same family) would be better, whereas it is the opposite for language groups whose migration is mostly emigration, e.g. Arabic 3. High attractiveness (Implying people’s stronger eagerness to learn this language), e.g. English (See in Apendix B for the rest twenty-one language groups)

<!-- b000267 | furniture | pages [15] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000268 | furniture | pages [15] -->
Team # 73410

<!-- b000269 | furniture | pages [15] -->
Page 14 of 27

<!-- b000270 | caption | pages [15] -->
Figure 4: Graph of Population of Top Five Language Groups in the Next Fifty Years

<!-- b000272 | prose | pages [15] -->
Ranking 2017 2067 1 Mandarin English 2 English Mandarin 3 Hindi/Urdu Arabic 4 Spanish Spanish 5 Arabic Hindi/Urdu 6 Malay Bengali 7 Russian Hausa 8 Bengali Malay 9 Portuguese Punjabi 10 French Russian

<!-- b000273 | caption | pages [15] -->
Table 2: Ranking of Languages by Population in 2017 and 2067

<!-- b000274 | heading | pages [15] -->
3.5.2 Graph of the Scale of Migration

<!-- b000275 | prose | pages [15] -->
Additionally, we can easily derive the graph of the scale of migration starting from the year of 2017 (Figure 5) We only label in the graph the top four attractive language regions for immigrants, and it’s apparent that they are all developed countries except for Russia (Mostly due to the historical factor that the population is not clearly divided amongst neighboring countries after the disintegration of USSR). Furthermore, the quantity of immigrants to English region (Over one hundred million) far exceeds that of other language regions’, mostly driven by the extensive acceptance of this language.

<!-- b000276 | heading | pages [15] -->
3.5.3 Distribution of Non-native English Speakers

<!-- b000277 | prose | pages [15] -->
We can also easily derive the distribution of non-native English speakers (Figure 6):

<!-- b000278 | prose | pages [15] -->
The scale of non-native English speakers is unparalleled. According to our projec- tions, there are more than ninety million non-native English speakers amongst all native Chinese speakers.

<!-- b000279 | prose | pages [15, 16] -->
What intrigues us is that despite most English nations (e.g. U.S.A., UK) being isolated of 2017)

<!-- b000280 | furniture | pages [16] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000281 | furniture | pages [16] -->
Team # 73410

<!-- b000282 | furniture | pages [16] -->
Page 15 of 27

<!-- b000283 | caption | pages [16] -->
Figure 5: Graph of the Scale of Migration in the Next Fifty Years (Starting from the year

<!-- b000285 | caption | pages [16] -->
Figure 6: Distribution of Non-native English Speakers in 2067

<!-- b000286 | prose | pages [16] -->
in terms of geography, English regions have the largest scale of immigrants and non- native speakers. This implies that geographic factors will not pose significant impact on migration in the next fifty years.

<!-- b000287 | heading | pages [16] -->
3.6 Sensitivity Analysis

<!-- b000288 | prose | pages [16] -->
In this subsection, we will be mainly analyzing the sensitivity of our model to the uni- formity of eagerness to learn of different language groups (Implying that and that if a language group has a barely uniform eagerness to learn, people in this language group tends to learn different foreign languages).

<!-- b000289 | heading | pages [16] -->
3.6.1 High Uniformity Scenario

<!-- b000290 | prose | pages [16] -->
If a language group has high uniformity in terms of eagerness to learn, people’s proba- bility of choosing to learn each language is more uniformly distributed. The major corre- sponding real cases are:

<!-- b000291 | prose | pages [16, 17] -->
1. Governments impose no restrictions over second language, and people in this lan- guage group can choose which foreign language to learn at their discretion.

<!-- b000292 | furniture | pages [17] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000293 | furniture | pages [17] -->
Team # 73410

<!-- b000294 | furniture | pages [17] -->
Page 16 of 27

<!-- b000296 | prose | pages [17] -->
2. People are not highly purposeful when it comes to learning a foreign language, which means that they are not learning foreign languages merely for the purpose of attaining more opportunities.

<!-- b000297 | prose | pages [17] -->
To reflect the characteristics of a high uniformity scenario, we modify expression (17) to:

<!-- b000298 | prose | pages [17] -->
The higher k is, the lower the uniformity is. The initial model adopts k = 1, and when k = 0:1, the graph of population of different language groups are as follows: (Figure 7).

<!-- b000299 | caption | pages [17] -->
Figure 7: Graph of Population of Different Language Groups When k=0.1

<!-- b000300 | prose | pages [17] -->
We can find that the population of English doesn’t exceed that of Mandarin’s. The attractiveness of English is impaired.

<!-- b000301 | heading | pages [17] -->
3.6.2 Low Uniformity Scenario

<!-- b000302 | prose | pages [17] -->
If a language group has high uniformity in terms of eagerness to learn, people’s prob- ability of choosing to learn each language is less uniformly distributed (concentrated at widely accepted foreign languages). The major corresponding real cases are:

<!-- b000303 | prose | pages [17] -->
1. Governments introduce restrictions over second language, e.g. all people should learn a specified foreign language.

<!-- b000304 | prose | pages [17] -->
2. People are highly purposeful when it comes to learning foreign languages, eager to attain more opportunities through language learning.

<!-- b000305 | prose | pages [17] -->
When k = 10, the graph of population of different language groups is as follows (Figure 8).

<!-- b000306 | prose | pages [17] -->
We can find that the population of English is rocketing, surpassing that of Mandarin’s tens of years earlier. The attractiveness of English is further reinforced.

<!-- b000307 | furniture | pages [18] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000308 | furniture | pages [18] -->
Team # 73410

<!-- b000309 | furniture | pages [18] -->
Page 17 of 27

<!-- b000310 | caption | pages [18] -->
Figure 8: Graph of Population of Different Language Groups When k=10

<!-- b000311 | heading | pages [18] -->
4 Application of Our Model

<!-- b000312 | heading | pages [18] -->
4.1 Assumptions

<!-- b000313 | prose | pages [18] -->
With regard to our client company being a large multinational service company, we de- rive their extrinsic and intrinsic needs for additional international offices:

<!-- b000314 | prose | pages [18] -->
1. These six new offices should cover the population of major languages (twenty- three major languages listed by our client) in a mutually exclusive and collectively ex-haustive way (Implying that each language can only be covered by one of the six offices except for English).

<!-- b000315 | prose | pages [18] -->
2. The basic working languages of an office are English and local language.

<!-- b000316 | prose | pages [18] -->
3. These offices should cover languages with the largest population and the most ro- bust economy (Evaluated based on the GDP of different language regions). The transportation costs between each office and the language regions they cover should also be the smallest.

<!-- b000317 | prose | pages [18] -->
4. One office shouldn’t cover too many different languages, or else there will be an impairment on profit due to lower operation efficiency and higher costs.

<!-- b000318 | prose | pages [18] -->
5. There must be English speaking residents near each office (Each language region is projected to have English speaking residents by our previous models)

<!-- b000319 | prose | pages [18] -->
Drawing upon the analysis above, we establish our rating model for office locations:

<!-- b000320 | furniture | pages [19] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000321 | furniture | pages [19] -->
Team # 73410

<!-- b000322 | furniture | pages [19] -->
Page 18 of 27

<!-- b000323 | heading | pages [19] -->
4.2 Symbol Descrption

<!-- b000324 | heading | pages [19] -->
4.3 Calculating and Simplifying

<!-- b000325 | prose | pages [19] -->
To start with, we propose a list of candidate cities for further examination and selec-tion. These cities cover major nations of all twenty-three languages, except for English, Mandarin and Wu (Because our client has already set up offices in cities covering those language regions):

<!-- b000326 | prose | pages [19] -->
Bombay, Dubai, Madrid, Jakarta, Moscow, Rio de Janeiro, Dhaka, Paris, Abuja, Islam-abad, Tokyo, Berlin, Tehran, Dodoma, Seoul, Hong Kong, Istanbul, Ho Chi Minh City, Rome.

<!-- b000327 | heading | pages [19] -->
4.3.1 The Year of 2017

<!-- b000328 | prose | pages [19] -->
We conduct simulation on the data of 2017, with weight coefficients set as (Set to fit the real case and their orders of magnitude):

<!-- b000329 | furniture | pages [20] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000330 | furniture | pages [20] -->
Team # 73410

<!-- b000331 | furniture | pages [20] -->
Page 19 of 27

<!-- b000332 | prose | pages [20] -->
Office location Covering languages (Exclusive of English) Tokyo Japanese, Korean, Javanese, Malay Bombay Hindustani, Telugu, Tamil, marathi Madrid Spanish, Italian Rio de Janeiro Portuguese Moscow Arabic ,Russian ,Bengali, Hausa, Punjabi, Persian, Swahili, Yue, Vietnamese, Turkish Paris French, Germany Accumulated scores 43.0 If we set up only five offices, then the optimal stable solution is as follows:

<!-- b000333 | prose | pages [20] -->
Office location Covering languages (Exclusive of English) Tokyo Japanese, Korean, Javanese, Malay Bombay Hindustani, Telugu, Tamil, marathi Madrid Spanish, Germany Moscow Arabic ,Russian ,Bengali, Hausa, Punjabi, Persian, Swahili, Yue, Vietnamese, Turkish Paris French, Portuguese, Italian Accumulate scores 39.7 We can see that despite the costs of opening more offices, opening six offices is still superior to opening five offices.

<!-- b000334 | prose | pages [20] -->
We also simulate other scenarios with different weight coefficients if our client at- taches great importance to regional economy or population. See: Appendix A

<!-- b000335 | heading | pages [20] -->
4.3.2 The Year of 2067

<!-- b000336 | prose | pages [20] -->
Given an intrinsic change in communications and transportation in 2067 (Compared to 2017), the geographic factor is less significant. We set the coefficients as:

<!-- b000337 | prose | pages [20] -->
We make projections about the economy (GDP) of each language region (Evaluated based on major nations in each region), by establishing a cycle projection model. We integrate the Kitchin cycle, Juglar cycle, Kuznets swing and Kondratiev wave, and sim-ulate the integrated cycle with a trigonometric function. We then use the GDP data of each region in the past forty-six years to solve for the coefficients, and then employ the function to forecast GDP of each language region in 2067. See Appendix A[6] for our projected growth rate in each cycle and terminal GDP (Starting at 2015, with each cycle representing approximately thirteen years).

<!-- b000338 | prose | pages [20] -->
Combined with the projected distribution of population of different languages in 2067 by our previous models, we can derive the optimal stable solution:

<!-- b000339 | furniture | pages [21] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000340 | furniture | pages [21] -->
Team # 73410

<!-- b000341 | furniture | pages [21] -->
Page 20 of 27

<!-- b000342 | prose | pages [21] -->
Office location Covering languages (Exclusive of English) Tokyo Japanese, Swahili, Yue, Vietnamese Bombay Hindustani, Telugu, Tamil, marathi Madrid Spanish, French, Germany Jakarta Javanese, Malay, Hausa, Korean Dubai Arabic ,Russian ,Bengali, Punjabi, Persian, Turkish Paris French,Italian Accumulated scores 236.2 If we open only five offices, then the optimal stable solution is:

<!-- b000343 | prose | pages [21] -->
Office location Covering languages (Exclusive of English) Bombay Hindustani, Telugu, Tamil, marathi Madrid Spanish, French, Germany Jakarta Javanese, Malay, Japanese, Korean, Yue Dubai Arabic ,Russian ,Bengali, Hausa, Punjabi, Persian, Turkish Rio de Janeiro Portuguese, Swahili, Vietnamese,Italian Accumulated scores 225.2 We can see that opening six offices is still superior to opening five offices, yet the gap is narrowing. If the management cost is taken into consideration, opening five offices can be a viable option for our client.

<!-- b000344 | heading | pages [21] -->
5 Strengths and Weaknesses

<!-- b000345 | heading | pages [21] -->
Strengths

<!-- b000346 | prose | pages [21] -->
1. We preserve sufficient interfaces in our model, for further analysis and consid-eration of more variables.

<!-- b000347 | prose | pages [21] -->
2. We leave out irrelevant (Or weakly correlated) variables, making the model simple and concise.

<!-- b000348 | prose | pages [21] -->
3. We make our model more legible and applicable, by introducing the transition matrix and transition graph.

<!-- b000349 | prose | pages [21] -->
4. We make our model fit the real case better, by separating learners, migrants, and English speakers from other groups.

<!-- b000350 | heading | pages [21] -->
Weaknesses

<!-- b000351 | prose | pages [21] -->
1. Our consideration of the influence of economic development is not sufficient.

<!-- b000352 | prose | pages [21] -->
2. We regard natural growth, migration, and language learning as major factors influencing the language structure. However, the change in language structure can influence these three factors in turn. We only consider its influence on language learning in our model.

<!-- b000353 | prose | pages [21] -->
3. The first language of migrants can also influence the language structure of the regions they migrate to. This model doesn’t take this into consideration.

<!-- b000354 | prose | pages [21] -->
4. The distinctions of education level in different language regions are not suffi- ciently considered in our model.

<!-- b000355 | furniture | pages [22] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000356 | furniture | pages [22] -->
Team # 73410

<!-- b000357 | furniture | pages [22] -->
Page 21 of 27

<!-- b000358 | heading | pages [22] -->
6 Memo

<!-- b000359 | prose | pages [22] -->
Dear Sir or Madame, In accordance to your requests, we establish two customized models to develop accu-rate projections and help your company deliver successful global solutions at the lowest possible costs.

<!-- b000360 | prose | pages [22] -->
First, we investigate trends of global languages through our inhomogeneous transi- tion model, and cast a projection for population of different languages in the next 50 years (With regard to the uneven distribution of population amongst languages, we only examine languages with a population larger than 50 million in 2017).

<!-- b000361 | prose | pages [22] -->
The projected distribution is rather different from that in 2017, and the key findings are:

<!-- b000362 | prose | pages [22] -->
1. The population of English rises to surpass Mandarin, and dominates as the inter- national language with most speakers, mostly due to its extensive acceptance by people across the world. The population of non-native English speakers will reach approximately 490 million, with most of being native Chinese speakers (91 million).

<!-- b000363 | prose | pages [22] -->
2. The population of Arabic / Punjabi / Hausa increases greatly (The number of Ara- bic speakers only falls behind that of English’s and Mandarin’s), mostly due to the high birth rate.

<!-- b000364 | prose | pages [22] -->
3. The population of Mandarin / Japanese / Russian / Korean / Yue / Wu decreases sharply, mostly due to the declining birth rate and aging population.

<!-- b000365 | prose | pages [22] -->
4. The geographic distribution of migrants is extremely uneven in 2067, with the En- glish region hosting most immigrants (More than 100 million), mostly due to the imbalanced migration amongst developed and under-developed regions.

<!-- b000366 | prose | pages [22] -->
Building upon our language population model, we establish the site rating model. If your company value cost savings and revenues expansion equally, we hereby propose the optimal location options for new offices:

<!-- b000367 | prose | pages [22] -->
Office location Covering languages (Exclusive of English) Tokyo Japanese, Korean, Javanese, Malay Bombay Hindustani, Telugu, Tamil, marathi Madrid Spanish, Italian Rio de Janeiro Portuguese Moscow Arabic ,Russian ,Bengali, Hausa, Punjabi, Persian, Swahili, Yue, Vietnamese, Turkish Paris French, Germany If your company offers necessities (Implying that prices of your offerings vary little to consumption power / GDP), then total population of covered languages has a greater impact on the revenues of each office. We hereby propose:

<!-- b000368 | furniture | pages [23] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000369 | furniture | pages [23] -->
Team # 73410

<!-- b000370 | furniture | pages [23] -->
Page 22 of 27

<!-- b000371 | prose | pages [23] -->
Office location Covering languages (Exclusive of English) Tokyo Japanese, Korean, Hausa Bombay Hindustani, Telugu, Tamil,marathi Madrid Spanish, Portuguese Jakarta Javanese, Malay, Bengali Moscow Arabic, Russian, Punjabi, Persian, Swahili, Yue, Vietnamese, Turkish Paris French, Italian, German

<!-- b000372 | prose | pages [23] -->
If your company offers non-necessities (Implying that prices of your offerings vary greatly to consumption power / GDP), then accumulated GDP of covered language re- gions has a greater impact on the revenues of each office. We hereby propose:

<!-- b000373 | prose | pages [23] -->
Office location Covering languages (Exclusive of English) Tokyo Japanese, Korean, Malay, Javanese Bombay Hindustani, Telugu, Tamil, marathi Madrid Spanish, Portuguese Beilin German, Hausa Moscow Arabic, Russian, Punjabi, Persian, Swahili, Yue, Vietnamese, Turkish, Bengali Paris French, Italian

<!-- b000374 | prose | pages [23] -->
Note that:

<!-- b000375 | prose | pages [23] -->
1. We select these locations from a list of candidate cities that are major cities or pivot cities in different language regions. For example, we choose Berlin to represent the German region, and Rio de Janeiro to represent the Portuguese region (Because Brazil has a higher GDP than Portugal).

<!-- b000376 | prose | pages [23] -->
2. With regard to your established offices in New York, U.S.A. and Shanghai, China, we exclude English, Mandarin, and Wu in our model (Shanghai office can cover Mandarin and Wu, and English is mandatory for all offices).

<!-- b000377 | prose | pages [23] -->
3. In the light of your globalization strategy, we assume that these 6 new offices can cover all 23 languages left of major languages in a mutually exclusive and collec- tively exhaustive way to save resources.

<!-- b000378 | prose | pages [23] -->
Drawing upon both models, we project our proposal to be still valid even after 50 years. However, due to economic development of Middle East and Southeast Asia, as well as the population growth of Arabic and multiple languages in Southeast Asia, we suggest that your company should move the offices in Moscow and Paris to Dubai and Jakarta. Meanwhile, the languages each office cover should also be adjusted.

<!-- b000379 | prose | pages [23] -->
We do not recommend cutting down the number of new offices below 6 in the short term, but our model projects that over time the returns of opening 5 new offices are catch-ing up with those of opening 6 new offices, due to the development of communications and transportation. In 2067, the difference is around 5%, so we recommend your com-pany may consider to shut down one office, if the saved costs can compensate the lost 5% revenues.

<!-- b000380 | prose | pages [23] -->
Sincerely,

<!-- b000381 | furniture | pages [23] -->
Team# 73410

<!-- b000382 | furniture | pages [24] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000383 | furniture | pages [24] -->
Team # 73410

<!-- b000384 | furniture | pages [24] -->
Page 23 of 27

<!-- b000385 | heading | pages [24] -->
References

<!-- b000386 | references | pages [24] -->
[1] https://en.wikipedia.org/wiki/List_of_languages_by_total_

<!-- b000387 | references | pages [24] -->
number_of_speakers

<!-- b000388 | references | pages [24] -->
[2] UN Data. Net migration rate.

<!-- b000389 | references | pages [24] -->
http://data.un.org/Data.aspx?q=migration&d=PopDiv&f=

<!-- b000390 | references | pages [24] -->
variableID%3a85

<!-- b000391 | references | pages [24] -->
[3] UN Data. GDP by Type of Expenditure at current prices - US dollars.

<!-- b000392 | references | pages [24] -->
http://data.un.org/Data.aspx?q=GDP&d=SNAAMA&f=grID%3a101%

<!-- b000393 | references | pages [24] -->
3bcurrID%3aUSD%3bpcFlag%3a0

<!-- b000394 | references | pages [24] -->
[4] UN Data. Crude death rate.

<!-- b000395 | references | pages [24] -->
http://data.un.org/Data.aspx?q=death+rate&d=PopDiv&f=

<!-- b000396 | references | pages [24] -->
variableID%3a65

<!-- b000397 | references | pages [24] -->
[5] UN Data. Crude birth rate.

<!-- b000398 | references | pages [24] -->
http://data.un.org/Data.aspx?q=birth+rate&d=PopDiv&f=

<!-- b000399 | references | pages [24] -->
variableID%3a53

<!-- b000400 | references | pages [24] -->
[6] 2018 | 22nd ANNUAL EDITION LONG-TERM CAPITAL MARKET ASSUMP-

<!-- b000401 | references | pages [24] -->
TIONS, by J.P. Morgan Asset Management

<!-- b000402 | furniture | pages [25] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000403 | furniture | pages [25] -->
Team # 73410

<!-- b000404 | furniture | pages [25] -->
Page 24 of 27

<!-- b000405 | heading | pages [25] -->
Appendices

<!-- b000406 | heading | pages [25] -->
Appendix A

<!-- b000407 | prose | pages [25] -->
Tables

<!-- b000408 | prose | pages [25] -->
Language Countries Mandarin China, Singapore English United Kingdom, United States of America, Canada, Australia, New Zealand, South Africa Spanish Spain, Mexico, Colombia, Argentina Hindi/Urdu India, Pakistan Russian Russia, Belarus, Kyrgyz Republic, Kazakhstan Portuguese Portugal, Brazil Bengali Bangladesh French France, Canada, Belgium, Switzerland Japanese Japan German Germany, Austria, Switzerland

<!-- b000409 | caption | pages [25] -->
Table 3: Major Countries of Different Language Groups

<!-- b000410 | prose | pages [25] -->
Language Weighted average birth rate Weighted average death rate Mandarin 0.0121 0.0071 English 0.0136 0.0086 Spanish 0.0206 0.0078 Hindi/Urdu 0.0161 0.0058 Russian 0.0140 0.0141 Portuguese 0.0141 0.0067 Bengali 0.0193 0.0057 French 0.0113 0.0082 Japanese 0.0082 0.0094 German 0.0097 0.0093

<!-- b000411 | caption | pages [25] -->
Table 4: Birth Rate and Death Rate of Major Language Groups

<!-- b000412 | prose | pages [25] -->
Language Native Non-native Mandarin 850 178 English 353 510 Spanish 400 90 Hindi/Urdu 324 214 Russian 170 26 Portuguese 200 30 Bengali 190 20 French 76 87 Japanese 130 ?

<!-- b000413 | prose | pages [25, 26] -->
German 78 8 Office location Covering languages (Exclusive of English) Tokyo Japanese, Korean, Hausa Bombay Hindustani, Telugu, Tamil,marathi Madrid Spanish, Portuguese Jakarta Javanese, Malay, Bengali Moscow Arabic, Russian, Punjabi, Persian, Swahili, Yue, Vietnamese, Turkish Paris French, Italian, German

<!-- b000414 | caption | pages [25] -->
Table 5: Population Statistics of Major Languages in 2013

<!-- b000415 | furniture | pages [26] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000416 | furniture | pages [26] -->
Team # 73410

<!-- b000417 | furniture | pages [26] -->
Page 25 of 27

<!-- b000419 | caption | pages [26] -->
Table 6: Office Location Selections When 1 = 2; 2 = 3 = 1 (More regard to population)

<!-- b000420 | prose | pages [26] -->
Office location Covering languages (Exclusive of English) Tokyo Japanese, Korean, Malay, Javanese Bombay Hindustani, Telugu, Tamil, marathi Madrid Spanish, Portuguese Beilin German, Hausa Moscow Arabic, Russian, Punjabi, Persian, Swahili, Yue, Vietnamese, Turkish, Bengali Paris French, Italian

<!-- b000421 | caption | pages [26] -->
Table 7: Office Location Selections When 1 = 2; 2 = 3 = 1 (More regard to population)

<!-- b000422 | prose | pages [26] -->
Cycle 1 Cycle 2 Cycle 3 Cycle 4 2017 GDP 2067 GDP India 1.77093244 1.79285437 1.20503007 1.18984108 2.11624E+12 9.63382E+12 UAE 2.34739506 2.39043403 1.32380487 1.29887136 3.70296E+11 3.57275E+12 Spain 1.77925415 1.80145680 1.20690268 1.19156508 1.19296E+12 5.49389E+12 Malaysia 2.04379203 2.07530650 1.26381944 1.24388686 8.61934E+11 5.74723E+12 Rassia 1.17979323 1.18406734 1.05484027 1.05099867 1.32602E+12 2.05362E+12 Bengaladesh 1.74035172 1.76124883 1.19810151 1.18346095 1.94466E+11 8.45179E+11 Spain 1.93249998 1.96000801 1.24046279 1.22243396 1.77259E+12 1.01811E+13 France 1.63293805 1.65032250 1.17315091 1.16046588 2.41895E+12 8.87464E+12 Nigeria 1.80587369 1.82897954 1.21285675 1.19704555 4.94583E+11 2.37168E+12 Pakistan 1.68267193 1.70166563 1.18482564 1.17122932 2.66458E+11 1.05876E+12 Japan 1.70175575 1.72137488 1.18924877 1.17530547 4.38308E+12 1.79463E+13 Germany 1.62696655 1.64415981 1.17173442 1.15915950 3.3636E+12 1.222078E+13 Iran 1.90019888 1.92656774 1.23352935 1.21606083 3.98563E+11 2.18869E+12 Tanzania 1.67179450 1.69043368 1.18229065 1.16889277 4.56282E+10 1.78202E+11 Korea 2.09597423 2.12940922 1.27450158 1.25369008 1.37787E+12 9.82618E+12 Hong Kong 1.94604458 1.97403352 1.24334890 1.22508618 3.09236E+11 1.80953E+12 Turkey 1.81628507 1.83974633 1.21517075 1.19917504 7.17888E+11 3.49557E+12 Vietnam 2.02929384 2.06027943 1.26082183 1.24113496 1.93241E+11 1.26428E+12 Italy 1.63241448 1.64978215 1.17302684 1.16035146 1.82158E+12 6.67733E+12

<!-- b000423 | caption | pages [26] -->
Table 8: Economic Outlook for the Next Fifty Years

<!-- b000424 | furniture | pages [27] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000425 | furniture | pages [27] -->
Team # 73410

<!-- b000426 | furniture | pages [27] -->
Page 26 of 27

<!-- b000427 | heading | pages [27] -->
Appendix B

<!-- b000428 | prose | pages [27] -->
Figures

<!-- b000429 | caption | pages [27] -->
Figure 9: Graph of Birth Rate in the Next Fifty Years

<!-- b000430 | caption | pages [27] -->
Figure 10: Graph of Death Rate in the Next Fifty Years

<!-- b000431 | caption | pages [27] -->
Figure 11: Graph of Population of Top 6 to 16 Language Groups in the Next Fifty Years

<!-- b000432 | furniture | pages [28] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000433 | furniture | pages [28] -->
Team # 73410

<!-- b000434 | furniture | pages [28] -->
Page 27 of 27

<!-- b000435 | caption | pages [28] -->
Figure 12: Graph of Population of Top 17 to 26 Language Groups in the Next Fifty Years
