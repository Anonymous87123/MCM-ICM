# P-B-2014-28414-5bd5b982

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team#28414                                                             Page 1 of 33

<!-- b000002 | title | pages [1] -->
Evaluation System for College Coaching Legends

<!-- b000003 | heading | pages [1] -->
Summary

<!-- b000004 | prose | pages [1] -->
In order to evaluate the performance of a coach, we describe metrics in five

<!-- b000005 | prose | pages [1] -->
aspects: historical record, game gold content, playoff performance, honors and

<!-- b000006 | prose | pages [1] -->
contribution to the sports. Moreover, each aspect is subdivided into several secondary

<!-- b000007 | prose | pages [1] -->
metrics. Take playoff performance as example, we collect postseason result (Sweet

<!-- b000008 | prose | pages [1] -->
Sixteen, Final Four, etc.) per year from NCAA official website, Wikimedia and so on.

<!-- b000009 | prose | pages [1] -->
First, Analytic Hierarchy Process (AHP) Model is established to determine the

<!-- b000010 | furniture | pages [1] -->


<!-- b000011 | prose | pages [1] -->
weight of each metric to coaches’ evaluation grade. All metrics are adequately filled

<!-- b000012 | prose | pages [1] -->
into the three-hierarchy structure, and then we obtain the metric weight based on

<!-- b000013 | prose | pages [1] -->
which evaluation grade is calculated. Second, Fuzzy Synthetic Evaluation (FSE) is

<!-- b000014 | prose | pages [1] -->
built to overcome weakness of excess subjective factors in AHP. This model takes

<!-- b000015 | heading | pages [1] -->
data processing by membership function to generate fuzzy matrix. After that, entropy

<!-- b000016 | prose | pages [1] -->
method and linear weighted method are applied to obtain evaluation grade.

<!-- b000017 | prose | pages [1] -->
To evaluate the accuracy of the two models, hit score is defined. It is supposed to

<!-- b000018 | furniture | pages [1] -->


<!-- b000019 | prose | pages [1] -->
reflect the difference between our results and standard rankings from several

<!-- b000020 | prose | pages [1] -->
authorities such as ESPN and Sporting News. Take NCAA basketball as a case study,

<!-- b000021 | prose | pages [1] -->
AHP receives 78.77 hit score while FSE gets 81.81, which indicates that FSE

<!-- b000022 | prose | pages [1] -->
performs better than AHP. Afterwards, Aggregation Model (AM) can be developed by

<!-- b000023 | prose | pages [1] -->
combining the two models based on hit score. The top 5 college basketball coaches,

<!-- b000024 | prose | pages [1] -->
in turn, are John Wooden, Mike Krzyzewski, Adolph Rupp, Dean Smith and Bob Knight.

<!-- b000025 | prose | pages [1] -->
Time line horizon does make a difference. According to turning points in NCAA

<!-- b000026 | prose | pages [1] -->
history, we divide the previous century into six periods with different time weights

<!-- b000027 | prose | pages [1] -->
which lead to the change of ranking. We apply our model into college women’s

<!-- b000028 | prose | pages [1] -->
basketball only to find that genders do not matter. Model proves to be efficient in

<!-- b000029 | prose | pages [1] -->
other sports. The ranking of college football is: Bear Bryant, Knute Rockne, Tom

<!-- b000030 | prose | pages [1] -->
Osborne, Joe Paterno , Bobby Bowden, and the top 5 coaches in college hockey are

<!-- b000031 | prose | pages [1] -->
Bob Johnson, Red Berenson, Jack Parker, Jerry York, Ron Mason.

<!-- b000032 | furniture | pages [1] -->


<!-- b000033 | prose | pages [1] -->
We conduct sensitivity analysis on FSE to find best membership function and

<!-- b000034 | heading | pages [1] -->
calculation rule. Sensitivity analysis on aggregation weight is also performed. It

<!-- b000035 | prose | pages [1] -->
proves AM performs better than single model. As a creative use, top 3 presidents

<!-- b000036 | prose | pages [1] -->
(U.S.) are picked out: Abraham Lincoln, George Washington, Franklin D. Roosevelt.

<!-- b000037 | furniture | pages [1] -->


<!-- b000038 | prose | pages [1] -->
At last, the strength and weakness of our mode are discussed, non-technical

<!-- b000039 | prose | pages [1] -->
explanation is presented and the future work is pointed as well.

<!-- b000040 | furniture | pages [1] -->


<!-- b000041 | furniture | pages [2] -->
Team#28414                                                             Page 2 of 33

<!-- b000042 | prose | pages [2] -->
I.

<!-- b000043 | prose | pages [2] -->
Introduction ............................................................................................. 3 1.1 Problem Background......................................................................................... 3 1.2 Previous Research ............................................................................................ 3 1.3 Our Work ........................................................................................................... 3 II. Symbols, Definitions and Assumptions ................................................ 4

<!-- b000044 | prose | pages [2] -->
2.1 Symbols and Definitions .................................................................................... 4 2.2 General Assumptions ........................................................................................ 5 III. Articulate our metrics ............................................................................. 5

<!-- b000045 | prose | pages [2] -->
3.1 Specify evaluation norms .................................................................................. 5 3.2 Collect data ....................................................................................................... 8 3.3 Preprocess data ................................................................................................ 9 IV. Two models for coach ranking ............................................................. 10

<!-- b000046 | prose | pages [2] -->
4.1 Model I: Analytic Hierarchy Process (AHP) ..................................................... 10 4.1.1 The three-hierarchy structure ................................................................... 10 4.1.2 Obtain the index weight ............................................................................ 10 4.1.3 Results & analysis .................................................................................... 11 4.2 Model II: Fuzzy Synthetic Evaluation (FSE) .................................................... 12 4.2.1 Quantify grades in the five aspects ........................................................... 12 4.2.2 Determine membership functions ............................................................. 13 4.2.3 Determine the weights using entropy method .......................................... 14 4.2.4 Results & analysis .................................................................................... 15 V. Models Combination ............................................................................. 15

<!-- b000047 | prose | pages [2] -->
5.1 Evaluation of individual model ......................................................................... 15 5.2 Aggregation Model .......................................................................................... 17 5.3 Results & analysis ........................................................................................... 17 VI. Extend Our Models ................................................................................ 18

<!-- b000048 | prose | pages [2] -->
6.1 Genders do not matter .................................................................................... 18 6.2 Time factor does make a difference ................................................................ 19 6.2.1 Why time factor matters? .......................................................................... 19 6.2.2 How time factor matters? .......................................................................... 19 6.2.3 What is the variation tendency? ............................................................... 23 6.3 Model also works in other sports ..................................................................... 23 VII. Further discussion ................................................................................ 25

<!-- b000049 | prose | pages [2] -->
7.1 Sensitive Analysis on FSE .............................................................................. 25 7.1.1 Vary Membership function ........................................................................ 25 7.1.2 Vary calculation rule ................................................................................. 27 7.2 Sensitive Analysis on Aggregation weight ....................................................... 28 7.3 Explore: Evaluating Best President ................................................................. 29 VIII.

<!-- b000050 | prose | pages [2] -->
Strength and Weakness ................................................................. 30 IX. Non-technical Explanation ................................................................... 30 X. Future work ............................................................................................ 32 XI. References ............................................................................................. 32

<!-- b000051 | furniture | pages [2] -->


<!-- b000052 | furniture | pages [3] -->
Team#28414                                                             Page 3 of 33

<!-- b000053 | prose | pages [3] -->
I.

<!-- b000054 | heading | pages [3] -->
Introduction

<!-- b000055 | heading | pages [3] -->
1.1 Problem Background

<!-- b000056 | prose | pages [3] -->
Sports Illustrated is an American sports media franchise owned by media

<!-- b000057 | prose | pages [3] -->
conglomerate Time Warner [1]. This magazine is looking for the “best all time college

<!-- b000058 | prose | pages [3] -->
coach” male or female for the previous century. The best college coach or coaches

<!-- b000059 | prose | pages [3] -->
can be from among either male or female coaches in different fields, such as college

<!-- b000060 | prose | pages [3] -->
hockey or field hockey, football, baseball or softball, basketball, or soccer.

<!-- b000061 | prose | pages [3] -->
We face mainly four problems:

<!-- b000062 | prose | pages [3] -->
 Articulate our own metrics and build a mathematical model;

<!-- b000063 | prose | pages [3] -->
 Set up the evaluation system for the performance of the model.

<!-- b000064 | prose | pages [3] -->
 Discuss how our model can be applied with time factor or across both genders

<!-- b000065 | prose | pages [3] -->
and all possible sports;

<!-- b000066 | prose | pages [3] -->
 Analyze the influences of the parameters, then discuss whether your model could

<!-- b000067 | prose | pages [3] -->
be applied into wide fields.

<!-- b000068 | heading | pages [3] -->
1.2 Previous Research

<!-- b000069 | prose | pages [3] -->
Some magazines or websites that focus mainly on college sports have ranked the

<!-- b000070 | prose | pages [3] -->
top college coaches of different sports. For example, rivels.com has made a basket-

<!-- b000071 | prose | pages [3] -->
ball power rankings [2] which shows the top 25 coaches of college basketball.

<!-- b000072 | furniture | pages [3] -->


<!-- b000073 | prose | pages [3] -->
Considering the best college coaches is an evaluation problem. There are some

<!-- b000074 | prose | pages [3] -->
models which can solve such problem. One is the Analytic hierarchy process (AHP),

<!-- b000075 | prose | pages [3] -->
which was developed by Thomas L. Saaty [3] in the 1970s. The AHP provides a

<!-- b000076 | prose | pages [3] -->
comprehensive and rational framework for structuring a decision problem, for

<!-- b000077 | prose | pages [3] -->
representing and quantifying its elements, for relating those elements to overall goals,

<!-- b000078 | prose | pages [3] -->
and for evaluating alternative solutions [4]. Another is the Fuzzy Synthetic Evaluation

<!-- b000079 | prose | pages [3] -->
Model. Fuzzy mathematics forms a branch of mathematics related to fuzzy set theory

<!-- b000080 | prose | pages [3] -->
and fuzzy logic [5]. It started in 1965 after the publication of Lotfi Asker Zadeh's

<!-- b000081 | prose | pages [3] -->
seminal work Fuzzy sets [6].

<!-- b000082 | heading | pages [3] -->
1.3 Our Work

<!-- b000083 | prose | pages [3] -->
In this paper we determine the best college coaches from among either male or

<!-- b000084 | prose | pages [3] -->
female coaches in different sports. In Section 2, we provide the terminology definitions

<!-- b000085 | prose | pages [3] -->
and assumptions that will be utilized in the rest of the paper. In Section 3, we give the

<!-- b000086 | prose | pages [3] -->
definitions of evaluation standard and specific evaluation norms which we used in our

<!-- b000087 | furniture | pages [4] -->
Team#28414                                                             Page 4 of 33

<!-- b000088 | prose | pages [4] -->
models, and show some of the data we have collected. In Section 4, we build two

<!-- b000089 | prose | pages [4] -->
mathematical models to choose the best college coaches, and Section 5 considers

<!-- b000090 | prose | pages [4] -->
combination of the two models mentioned above. In Section 6 we extend our models

<!-- b000091 | prose | pages [4] -->
and take time, genders and types of sports into consideration. Section 7 provides

<!-- b000092 | prose | pages [4] -->
further discuss of our models. In Section 8, we provide an overview of our approach

<!-- b000093 | prose | pages [4] -->
and give a non-technical explanation of our models that sports fans will understand.

<!-- b000094 | prose | pages [4] -->
Section 9 shows some work we can do in the future.

<!-- b000095 | heading | pages [4] -->
II. Symbols, Definitions and Assumptions

<!-- b000096 | heading | pages [4] -->
2.1 Symbols and Definitions

<!-- b000097 | prose | pages [4] -->
 Symbols for evaluation norms:

<!-- b000098 | prose | pages [4] -->
𝒂𝒂𝒊𝒊 wins for the 𝑖𝑖𝑡𝑡ℎ year

<!-- b000099 | heading | pages [4] -->
Symbol

<!-- b000100 | prose | pages [4] -->
Definition

<!-- b000101 | prose | pages [4] -->
𝒃𝒃𝒊𝒊 losses for the 𝑖𝑖𝑡𝑡ℎ year

<!-- b000102 | prose | pages [4] -->
𝐑𝐑

<!-- b000103 | prose | pages [4] -->
𝐎𝐎

<!-- b000104 | prose | pages [4] -->
the average SRS

<!-- b000105 | prose | pages [4] -->
𝒏𝒏𝒌𝒌

<!-- b000106 | prose | pages [4] -->
the average SOS

<!-- b000107 | prose | pages [4] -->
𝓴𝓴𝒊𝒊

<!-- b000108 | prose | pages [4] -->
the times for each class of playoff

<!-- b000109 | prose | pages [4] -->
𝓬𝓬𝒊𝒊

<!-- b000110 | prose | pages [4] -->
the weight of each award

<!-- b000111 | prose | pages [4] -->
point for each aspect of contribution

<!-- b000112 | prose | pages [4] -->
 Symbols for Analytic Hierarchy Process:

<!-- b000113 | prose | pages [4] -->
𝐀𝐀

<!-- b000114 | heading | pages [4] -->
Symbol

<!-- b000115 | prose | pages [4] -->
Definition

<!-- b000116 | prose | pages [4] -->
𝝀𝝀𝒎𝒎𝒎𝒎𝒎𝒎

<!-- b000117 | prose | pages [4] -->
the judging matrix

<!-- b000118 | prose | pages [4] -->
𝐂𝐂𝐂𝐂

<!-- b000119 | prose | pages [4] -->
the greatest eigenvalue of matrix A

<!-- b000120 | prose | pages [4] -->
𝐂𝐂𝐂𝐂

<!-- b000121 | prose | pages [4] -->
the indicator of consistency check

<!-- b000122 | prose | pages [4] -->
𝐑𝐑𝐑𝐑

<!-- b000123 | prose | pages [4] -->
the consistency ratio

<!-- b000124 | prose | pages [4] -->
𝐂𝐂𝐂𝐂

<!-- b000125 | prose | pages [4] -->
the random consistency index

<!-- b000126 | prose | pages [4] -->
𝐀𝐀𝐀𝐀

<!-- b000127 | prose | pages [4] -->
the weight vector for criteria level

<!-- b000128 | prose | pages [4] -->
𝒀𝒀𝟏𝟏

<!-- b000129 | prose | pages [4] -->
the weight vector for alternatives level

<!-- b000130 | prose | pages [4] -->
the evaluation grade for model I

<!-- b000131 | prose | pages [4] -->
 Symbols for Fuzzy Synthetic Evaluation:

<!-- b000132 | prose | pages [4] -->
𝑿𝑿𝒊𝒊

<!-- b000133 | heading | pages [4] -->
Symbol

<!-- b000134 | prose | pages [4] -->
Definition

<!-- b000135 | prose | pages [4] -->
𝝁𝝁𝒋𝒋൫𝑿𝑿𝒊𝒊𝒊𝒊൯

<!-- b000136 | prose | pages [4] -->
the grades for each aspect

<!-- b000137 | prose | pages [4] -->
the membership function

<!-- b000138 | furniture | pages [5] -->
Team#28414                                                             Page 5 of 33

<!-- b000139 | prose | pages [5] -->
𝑿𝑿𝒇𝒇

<!-- b000140 | prose | pages [5] -->
𝒑𝒑𝒊𝒊𝒊𝒊

<!-- b000141 | prose | pages [5] -->
the fuzzy matrix

<!-- b000142 | prose | pages [5] -->
𝒆𝒆𝒋𝒋 the entropy for the 𝑗𝑗𝑡𝑡ℎ evaluation grade

<!-- b000143 | prose | pages [5] -->
the characteristic weight

<!-- b000144 | prose | pages [5] -->
𝑬𝑬𝐖𝐖

<!-- b000145 | prose | pages [5] -->
𝒀𝒀𝟐𝟐

<!-- b000146 | prose | pages [5] -->
the weight vector in entropy method

<!-- b000147 | prose | pages [5] -->
the evaluation grade for model II

<!-- b000148 | prose | pages [5] -->
 Symbols for Aggregation Model:

<!-- b000149 | prose | pages [5] -->
𝐃𝐃

<!-- b000150 | heading | pages [5] -->
Symbol

<!-- b000151 | prose | pages [5] -->
Definition

<!-- b000152 | prose | pages [5] -->
𝑾𝑾𝟏𝟏

<!-- b000153 | prose | pages [5] -->
the average offset distance

<!-- b000154 | prose | pages [5] -->
𝐘𝐘

<!-- b000155 | prose | pages [5] -->
the weight for model I

<!-- b000156 | prose | pages [5] -->
the evaluation grade for aggregation model

<!-- b000157 | heading | pages [5] -->
2.2 General Assumptions

<!-- b000158 | prose | pages [5] -->
 The elements that we already have taken into consideration play a vital role in the

<!-- b000159 | prose | pages [5] -->
evaluation.

<!-- b000160 | prose | pages [5] -->
 The ignored elements of coach do not influence the ranking.

<!-- b000161 | prose | pages [5] -->
 The data that we have collected is enough and accurate and the quantification is

<!-- b000162 | prose | pages [5] -->
correct.

<!-- b000163 | prose | pages [5] -->
 There exists objective and accurate ranking for coaches, and the rankings from

<!-- b000164 | prose | pages [5] -->
selected media could reflect the accurate ranking to some extent.

<!-- b000165 | heading | pages [5] -->
III. Articulate our metrics

<!-- b000166 | heading | pages [5] -->
3.1 Specify evaluation norms

<!-- b000167 | prose | pages [5] -->
As for the evaluation standard for players, there are mainly five aspects [9] that

<!-- b000168 | prose | pages [5] -->
count: strength, speed, skill, defense and attack. Similarly a coach could be evaluated

<!-- b000169 | prose | pages [5] -->
from following five aspects: historical record, game gold content, play-off performance,

<!-- b000170 | prose | pages [5] -->
honors and contribution to the sports. What follows in the chapter will hammer at

<!-- b000171 | prose | pages [5] -->
accounting for the five aspects.

<!-- b000172 | prose | pages [5] -->
 Historical record: The team’s record undoubtedly accounts for the largest

<!-- b000173 | prose | pages [5] -->
proportion in the coach evaluation. According to the mainstream statistic indexes

<!-- b000174 | prose | pages [5] -->
for the team record, wins and losses are most notable. The team’s historical

<!-- b000175 | prose | pages [5] -->
The total wins a could be calculated as follows:

<!-- b000176 | prose | pages [5] -->
record could directly reflects the coaching ability.

<!-- b000177 | prose | pages [5] -->
a = ෍𝑎𝑎𝑖𝑖

<!-- b000178 | prose | pages [5] -->
(3.1)

<!-- b000179 | prose | pages [5] -->
𝑖𝑖

<!-- b000180 | furniture | pages [6] -->
Team#28414                                                             Page 6 of 33

<!-- b000181 | prose | pages [6] -->
-Where 𝑎𝑎𝑖𝑖 denotes wins for the 𝑖𝑖𝑡𝑡ℎ year.

<!-- b000182 | prose | pages [6] -->
The total loses b could be calculated as follows:

<!-- b000183 | prose | pages [6] -->
b = ෍𝑏𝑏𝑖𝑖

<!-- b000184 | prose | pages [6] -->
𝑖𝑖

<!-- b000185 | prose | pages [6] -->
(3.2)

<!-- b000186 | prose | pages [6] -->
-Where 𝑏𝑏𝑖𝑖 denotes losses for the 𝑖𝑖𝑡𝑡ℎ year.

<!-- b000187 | prose | pages [6] -->
 Game gold content: If all wins are produced during the fights with weak teams,

<!-- b000188 | prose | pages [6] -->
apparently the wins could not illustrate the real coaching ability. At the same time,

<!-- b000189 | prose | pages [6] -->
the average point difference also makes a difference. It reflects the coaching style

<!-- b000190 | prose | pages [6] -->
that whether a coach is conservative or radical. To illustrate the upon two points,

<!-- b000191 | prose | pages [6] -->
we choose the following two norms:

<!-- b000192 | prose | pages [6] -->
 Simple Rating System (SRS) [8]: The simple rating system works by first

<!-- b000193 | prose | pages [6] -->
finding how many points, on average, a team wins/loses by. For each game,

<!-- b000194 | prose | pages [6] -->
the point differential is then weighted based on how much better or worse than

<!-- b000195 | prose | pages [6] -->
average their opponent's point differential is.

<!-- b000196 | prose | pages [6] -->
R = ∑𝑆𝑆𝑆𝑆𝑆𝑆𝑖𝑖

<!-- b000197 | prose | pages [6] -->
(3.3)

<!-- b000198 | prose | pages [6] -->
Let R denote the total SRS, then it could be calculated as follows:

<!-- b000199 | prose | pages [6] -->
𝑖𝑖

<!-- b000200 | prose | pages [6] -->
𝑡𝑡 𝑡𝑡

<!-- b000201 | prose | pages [6] -->
-Where 𝑆𝑆𝑆𝑆𝑆𝑆𝑖𝑖 denotes the SRS value for the 𝑖𝑖𝑡𝑡ℎ year, t denotes the number

<!-- b000202 | furniture | pages [6] -->


<!-- b000203 | prose | pages [6] -->
of the years.

<!-- b000204 | prose | pages [6] -->
 Strength of Schedule (SOS) [8]: In sports, strength of schedule (SOS) refers to

<!-- b000205 | prose | pages [6] -->
the difficulty or ease of a team's/person's opponent as compared to other

<!-- b000206 | prose | pages [6] -->
teams/persons. This is especially important if teams in a league do not play

<!-- b000207 | prose | pages [6] -->
each other the same number of times.

<!-- b000208 | prose | pages [6] -->
O = ∑𝑆𝑆𝑆𝑆𝑆𝑆𝑖𝑖

<!-- b000209 | prose | pages [6] -->
(3.4)

<!-- b000210 | prose | pages [6] -->
Let O denote the total SOS, then it could be calculated as follows:

<!-- b000211 | prose | pages [6] -->
𝑖𝑖 𝑖𝑖

<!-- b000212 | prose | pages [6] -->
𝑡𝑡

<!-- b000213 | prose | pages [6] -->
-Where 𝑆𝑆𝑆𝑆𝑆𝑆𝑖𝑖 denotes the SOS value for the 𝑖𝑖𝑡𝑡ℎ year, t denotes the number of the years.

<!-- b000214 | prose | pages [6] -->
 Playoff performance: Generally, during the regular season, teams play more

<!-- b000215 | prose | pages [6] -->
games in their division than outside it, but the league's best teams might not play

<!-- b000216 | prose | pages [6] -->
against each other in the regular season [11]. Therefore, in the postseason any

<!-- b000217 | prose | pages [6] -->
group-winning team is eligible to participate thus making the playoff performance

<!-- b000218 | prose | pages [6] -->
extremely important in the coach evaluating [12]. For college basketball in U.S., the

<!-- b000219 | prose | pages [6] -->
playoff performance could be divided as follows:

<!-- b000220 | prose | pages [6] -->
 First round: The team is eliminated in the first round.

<!-- b000221 | prose | pages [6] -->
 Second round: The team is eliminated in the second round.

<!-- b000222 | furniture | pages [7] -->
Team#28414                                                             Page 7 of 33

<!-- b000223 | prose | pages [7] -->
 Sweet sixteen: The last sixteen teams remaining in the playoff tournament

<!-- b000224 | prose | pages [7] -->
 Final four: The last four teams remaining in the playoff tournament.

<!-- b000225 | prose | pages [7] -->
 Runner-up: The team loses in the finals.

<!-- b000226 | prose | pages [7] -->
 Champion: The team wins in the finals.

<!-- b000227 | prose | pages [7] -->
symbol 𝑛𝑛𝑘𝑘. Let a binary variable 𝑚𝑚𝑘𝑘𝑘𝑘 denote whether the team get the 𝑘𝑘𝑡𝑡ℎ (for first

<!-- b000228 | prose | pages [7] -->
To quantify the aspect, we count the number of times for each class using the

<!-- b000229 | prose | pages [7] -->
round k = 1, champion k = 7) class in the 𝑖𝑖𝑡𝑡ℎ year. Thus  𝑛𝑛𝑘𝑘 could be calculated as

<!-- b000230 | prose | pages [7] -->
follows:

<!-- b000231 | prose | pages [7] -->
𝑛𝑛𝑘𝑘= ෍𝑚𝑚𝑘𝑘𝑘𝑘

<!-- b000232 | prose | pages [7] -->
(3.5)

<!-- b000233 | prose | pages [7] -->
𝑖𝑖

<!-- b000234 | prose | pages [7] -->
 Honors: There are various awards in this field which make up the honors of the

<!-- b000235 | prose | pages [7] -->
coach, at the same time, the basketball hall of fame and college basketball hall of

<!-- b000236 | prose | pages [7] -->
fame [7] are also honors. To quantify the honor, we count the times of main award

<!-- b000237 | prose | pages [7] -->
such as the Naismith College Coach of the Year, Basketball Times National

<!-- b000238 | prose | pages [7] -->
determine the weight of each award (𝓀𝓀𝑖𝑖), we collect its time period, based on

<!-- b000239 | prose | pages [7] -->
Coach of the Year [9] and so on. Different awards have different gold content. To

<!-- b000240 | prose | pages [7] -->
which weights are designated. Let ℋ denote the total weights of all the awards

<!-- b000241 | prose | pages [7] -->
a coach has got:

<!-- b000242 | prose | pages [7] -->
ℋ= ෍𝓀𝓀𝑖𝑖

<!-- b000243 | prose | pages [7] -->
(3.6)

<!-- b000244 | prose | pages [7] -->
𝑖𝑖

<!-- b000245 | prose | pages [7] -->
Namely ℋ reflects the how much honor a coach have ever obtained.

<!-- b000246 | prose | pages [7] -->
 Contribution to sports: This concept covers a wide range. In order to quantify

<!-- b000247 | prose | pages [7] -->
the contribution, we divide the contribution into five parts:

<!-- b000248 | prose | pages [7] -->
 Star players: Evaluate the number of the star players the coach have trained.

<!-- b000249 | prose | pages [7] -->
 Coaching age: When the coaching career start and how long does it last.

<!-- b000250 | prose | pages [7] -->
 Tactical Innovation: Have the coach invented tactical innovation?

<!-- b000251 | prose | pages [7] -->
 Performance in international competitions: Have the coach ever fight in the

<!-- b000252 | prose | pages [7] -->
international competitions? Then How many gold or silver medals?

<!-- b000253 | prose | pages [7] -->
We give 𝒸𝒸𝑖𝑖 points for each aspect above: 0 for mediocre, 1 for good, 2 for

<!-- b000254 | prose | pages [7] -->
 Popularity: The number of the results when search its name in Google.

<!-- b000255 | prose | pages [7] -->
excellent. Then add the points up to form the final grade 𝒞𝒞 in this aspect (the full

<!-- b000256 | prose | pages [7] -->
mark is 10):

<!-- b000257 | prose | pages [7] -->
𝒞𝒞= ෍𝒸𝒸𝑖𝑖

<!-- b000258 | prose | pages [7] -->
(3.7)

<!-- b000259 | prose | pages [7] -->
𝑖𝑖

<!-- b000260 | furniture | pages [8] -->
Team#28414                                                             Page 8 of 33

<!-- b000261 | prose | pages [8] -->
A figure is prepared to conclude the evaluation norms above. (See figure)

<!-- b000262 | furniture | pages [8] -->


<!-- b000263 | caption | pages [8] -->
Figure 3.1 First level evaluation norms

<!-- b000264 | furniture | pages [8] -->


<!-- b000265 | caption | pages [8] -->
Figure 3.2 Second level evaluation norms

<!-- b000266 | heading | pages [8] -->
3.2 Collect data

<!-- b000267 | furniture | pages [8] -->


<!-- b000268 | prose | pages [8] -->
We use men’s college basketball that will be utilized in the following models

<!-- b000269 | prose | pages [8] -->
discussion as an example, and collect relative data from the Internet. We choose

<!-- b000270 | prose | pages [8] -->
those 70 coaches who were in the list of the National Collegiate Basketball Hall of

<!-- b000271 | prose | pages [8] -->
Fame [7], because those coaches had gained tremendous glory and are more

<!-- b000272 | prose | pages [8] -->
competitive to be chosen as the best coaches. What’s more, we select other 5 college

<!-- b000273 | prose | pages [8] -->
coaches who are not in the Hall of Fame but still made significant contributions.

<!-- b000274 | furniture | pages [8] -->


<!-- b000275 | prose | pages [8] -->
Searching from the sports-reference.com [8], a website that can provide specific

<!-- b000276 | prose | pages [8] -->
data about coaches, we can find relative data of our specific evaluation norms.

<!-- b000277 | prose | pages [8] -->
Combining those data with the statistics we search from the Wikipedia, we finally

<!-- b000278 | prose | pages [8] -->
conclude the relative statistics of those 75 college coaches and list them in a form.

<!-- b000279 | prose | pages [8] -->
Here we give statistics of 10 coaches as an example.

<!-- b000280 | prose | pages [8] -->
In the following table, “FR”, “SR”, “SS”, “EE”, “FF”, “RU”, and “CH” refer to “First

<!-- b000281 | furniture | pages [9] -->
Team#28414                                                             Page 9 of 33

<!-- b000282 | prose | pages [9] -->
Round”, “Second Round”, “Sweet Sixteen”, “Elite Eight”, “Final Four”, “Runner-Up”,

<!-- b000283 | prose | pages [9] -->
and “Campion”, respectively.

<!-- b000284 | prose | pages [9] -->
Name from to year win lose

<!-- b000285 | prose | pages [9] -->
Jim

<!-- b000286 | prose | pages [9] -->
1905 1995 48 719 259

<!-- b000287 | prose | pages [9] -->
Boeheim

<!-- b000288 | prose | pages [9] -->
Jim

<!-- b000289 | prose | pages [9] -->
1972 2001 40 877 382

<!-- b000290 | prose | pages [9] -->
Calhoun

<!-- b000291 | prose | pages [9] -->
Larry

<!-- b000292 | prose | pages [9] -->
1979 2013 9 210 83

<!-- b000293 | prose | pages [9] -->
Brown

<!-- b000294 | prose | pages [9] -->
…

<!-- b000295 | furniture | pages [9] -->


<!-- b000296 | furniture | pages [9] -->


<!-- b000297 | furniture | pages [9] -->


<!-- b000298 | furniture | pages [9] -->


<!-- b000299 | furniture | pages [9] -->


<!-- b000300 | prose | pages [9] -->
Mike

<!-- b000301 | prose | pages [9] -->
1975 2013 39 975 302

<!-- b000302 | prose | pages [9] -->
Krzyzewski

<!-- b000303 | prose | pages [9] -->
SRS SOS FR SR SS EE FF RU CH

<!-- b000304 | prose | pages [9] -->
15.81 7.27 5 8 11 2 1 2 1

<!-- b000305 | prose | pages [9] -->
12.64 4.74 5 5 4 5 1 0 3

<!-- b000306 | prose | pages [9] -->
13.08 5.95 0 3 1 0 1 1 1

<!-- b000307 | furniture | pages [9] -->


<!-- b000308 | furniture | pages [9] -->


<!-- b000309 | furniture | pages [9] -->


<!-- b000310 | furniture | pages [9] -->


<!-- b000311 | furniture | pages [9] -->


<!-- b000312 | furniture | pages [9] -->


<!-- b000313 | furniture | pages [9] -->


<!-- b000314 | furniture | pages [9] -->


<!-- b000315 | furniture | pages [9] -->


<!-- b000316 | furniture | pages [9] -->


<!-- b000317 | prose | pages [9] -->
20.16 8.78 2 6 6 2 3 4 4

<!-- b000318 | caption | pages [9] -->
Table 3.1 the relevant data of the “best college coaches” candidates

<!-- b000319 | prose | pages [9] -->
We also collect college basketball coaching record about each season of every

<!-- b000320 | furniture | pages [9] -->


<!-- b000321 | prose | pages [9] -->
candidate. Here we take Larry Brown as an example.

<!-- b000322 | prose | pages [9] -->
AP Pre Season win lose SRS SOS

<!-- b000323 | prose | pages [9] -->
1979-80 22 10 15.67 6.1 8

<!-- b000324 | prose | pages [9] -->
1980-81 20 7 14.89 5.26 6

<!-- b000325 | prose | pages [9] -->
1983-84 22 10 9.76 5.86 17

<!-- b000326 | prose | pages [9] -->
1984-85 26 8 11.84 6.27 19

<!-- b000327 | prose | pages [9] -->
1985-86 35 4 23.18 10.42 5

<!-- b000328 | prose | pages [9] -->
1986-87 25 11 13.36 7.73 8

<!-- b000329 | prose | pages [9] -->
1987-88 27 11 15.71 10.77 7

<!-- b000330 | prose | pages [9] -->
— 2012-13 15 17 -0.59 -1.33

<!-- b000331 | prose | pages [9] -->
— 2013-14 18 5 13.88 2.45

<!-- b000332 | prose | pages [9] -->
AP High AP Final

<!-- b000333 | heading | pages [9] -->
Result

<!-- b000334 | prose | pages [9] -->
— 7 NCAA Runner-up

<!-- b000335 | prose | pages [9] -->
3 10 NCAA Second Round

<!-- b000336 | prose | pages [9] -->
— 17 NCAA Second Round

<!-- b000337 | prose | pages [9] -->
9 13 NCAA Second Round

<!-- b000338 | prose | pages [9] -->
2 2 NCAA Final Four

<!-- b000339 | prose | pages [9] -->
6 20 NCAA Sweet Sixteen

<!-- b000340 | prose | pages [9] -->
7

<!-- b000341 | furniture | pages [9] -->


<!-- b000342 | prose | pages [9] -->
NCAA Champions

<!-- b000343 | prose | pages [9] -->
— — —

<!-- b000344 | prose | pages [9] -->
— — —

<!-- b000345 | caption | pages [9] -->
Table 3.2 the college basketball coaching record about each season of Larry Brown

<!-- b000346 | heading | pages [9] -->
3.3 Preprocess data

<!-- b000347 | prose | pages [9] -->
When we collect data from Internet, we notice that some data is missing due to

<!-- b000348 | furniture | pages [9] -->


<!-- b000349 | prose | pages [9] -->
age. Given the fact, we have to preprocess the data from Internet. As for the data for

<!-- b000350 | prose | pages [9] -->
college basketball, SRS&SOS are sometimes missing. The solution adopt by us is

<!-- b000351 | prose | pages [9] -->
filling the data mainly based on interpolation according to the ranking generated by

<!-- b000352 | prose | pages [9] -->
the other metrics.

<!-- b000353 | furniture | pages [10] -->
Team#28414                                                             Page 10 of 33

<!-- b000354 | heading | pages [10] -->
IV. Two models for coach ranking

<!-- b000355 | heading | pages [10] -->
4.1 Model I: Analytic Hierarchy Process (AHP)

<!-- b000356 | prose | pages [10] -->
When we try to obtain the weight of mainly five aspects as the first class index and

<!-- b000357 | furniture | pages [10] -->


<!-- b000358 | prose | pages [10] -->
the weight of several second class index, subjective judgment is ill-considered. So we

<!-- b000359 | prose | pages [10] -->
choose the Analytic Hierarchy Process [4] (AHP) as the way to conform the weighting

<!-- b000360 | prose | pages [10] -->
coefficient of all the indicators in the evaluation system.

<!-- b000361 | heading | pages [10] -->
4.1.1 The three-hierarchy structure

<!-- b000362 | prose | pages [10] -->
The three hierarchy structure which contains criteria level and alternatives level is

<!-- b000363 | furniture | pages [10] -->


<!-- b000364 | prose | pages [10] -->
shown in following table.

<!-- b000365 | prose | pages [10] -->
Goal Criteria

<!-- b000366 | prose | pages [10] -->
The influence of coach

<!-- b000367 | prose | pages [10] -->
Alternatives

<!-- b000368 | prose | pages [10] -->
Historical Record Wins

<!-- b000369 | prose | pages [10] -->
Losses

<!-- b000370 | prose | pages [10] -->
Game Gold Content SRS

<!-- b000371 | prose | pages [10] -->
SOS

<!-- b000372 | prose | pages [10] -->
Playoff Performance

<!-- b000373 | prose | pages [10] -->
Honors

<!-- b000374 | prose | pages [10] -->
First Round

<!-- b000375 | prose | pages [10] -->
…

<!-- b000376 | prose | pages [10] -->
Champion

<!-- b000377 | prose | pages [10] -->
Different Awards

<!-- b000378 | prose | pages [10] -->
Hall of Fame

<!-- b000379 | prose | pages [10] -->
Contribution to sports Star Player

<!-- b000380 | prose | pages [10] -->
Coaching Age

<!-- b000381 | prose | pages [10] -->
Tactical Innovation

<!-- b000382 | prose | pages [10] -->
International Games

<!-- b000383 | prose | pages [10] -->
Popularity

<!-- b000384 | caption | pages [10] -->
Table 4.1 the three hierarchy structure of our model

<!-- b000385 | heading | pages [10] -->
4.1.2 Obtain the index weight

<!-- b000386 | prose | pages [10] -->
 Determine the judging matrix

<!-- b000387 | prose | pages [10] -->
judging matrix A = (𝑎𝑎𝑖𝑖𝑖𝑖).

<!-- b000388 | prose | pages [10] -->
We use the pairwise comparison method and one-nine method to construct

<!-- b000389 | prose | pages [10] -->
𝑎𝑎𝑖𝑖𝑖𝑖∗𝑎𝑎𝑘𝑘𝑘𝑘= 𝑎𝑎𝑖𝑖𝑖𝑖           (4.1).

<!-- b000390 | prose | pages [10] -->
Where 𝑎𝑎𝑖𝑖𝑖𝑖 is set according to the one-nine method

<!-- b000391 | furniture | pages [10] -->


<!-- b000392 | furniture | pages [11] -->
Team#28414                                                             Page 11 of 33

<!-- b000393 | prose | pages [11] -->
The greatest eigenvalue of matrix A is 𝜆𝜆𝑚𝑚𝑚𝑚𝑚𝑚, and the corresponding eigenvector

<!-- b000394 | prose | pages [11] -->
 Calculate the eigenvalues and eigenvectors

<!-- b000395 | prose | pages [11] -->
is u = (𝑢𝑢1,𝑢𝑢2,𝑢𝑢3, … 𝑢𝑢𝑛𝑛)𝑇𝑇. Then we normalize the u by the expression:

<!-- b000396 | furniture | pages [11] -->


<!-- b000397 | prose | pages [11] -->
(4.2)

<!-- b000398 | prose | pages [11] -->
𝑥𝑥𝑖𝑖=

<!-- b000399 | prose | pages [11] -->
𝑢𝑢𝑖𝑖 ∑ 𝑢𝑢𝑗𝑗 𝑛𝑛 𝑖𝑖=0

<!-- b000400 | prose | pages [11] -->
 Do the consistency check

<!-- b000401 | prose | pages [11] -->
CI = 𝜆𝜆𝑚𝑚𝑚𝑚𝑚𝑚−𝑛𝑛

<!-- b000402 | prose | pages [11] -->
(4.3)

<!-- b000403 | prose | pages [11] -->
The indicator of consistency check formula:

<!-- b000404 | furniture | pages [11] -->


<!-- b000405 | prose | pages [11] -->
𝑛𝑛−1

<!-- b000406 | prose | pages [11] -->
Where n denotes the exponent number of matrix.

<!-- b000407 | prose | pages [11] -->
CR = 𝐶𝐶𝐶𝐶

<!-- b000408 | prose | pages [11] -->
𝑅𝑅𝑅𝑅                                     (4.4)

<!-- b000409 | prose | pages [11] -->
The expression of consistency ratio:

<!-- b000410 | prose | pages [11] -->
As we have confirmed the weighting coefficient of all the indicators in the

<!-- b000411 | prose | pages [11] -->
𝐶𝐶𝐶𝐶𝑖𝑖 denotes the weight of 𝑖𝑖𝑡𝑡ℎ criteria level factor, where 𝐴𝐴𝐴𝐴𝑗𝑗 is the weight of

<!-- b000412 | prose | pages [11] -->
evaluation system, now we quantify the importance of coaches.

<!-- b000413 | prose | pages [11] -->
𝑗𝑗𝑡𝑡ℎ secondary critical level factor, and 𝐹𝐹𝑗𝑗 denotes the 𝑗𝑗𝑡𝑡ℎ secondary critical level

<!-- b000414 | prose | pages [11] -->
The evaluation grade 𝑌𝑌1 should be:

<!-- b000415 | prose | pages [11] -->
factor.

<!-- b000416 | prose | pages [11] -->
5

<!-- b000417 | prose | pages [11] -->
𝑚𝑚𝑚𝑚

<!-- b000418 | prose | pages [11] -->
𝑌𝑌1 = ෍𝐶𝐶𝐶𝐶𝑖𝑖∗෍𝐴𝐴𝐴𝐴𝑗𝑗∗𝐹𝐹𝑗𝑗

<!-- b000419 | prose | pages [11] -->
𝑖𝑖=1

<!-- b000420 | prose | pages [11] -->
𝑗𝑗=1

<!-- b000421 | heading | pages [11] -->
4.1.3 Results & analysis

<!-- b000422 | prose | pages [11] -->
(4.5)

<!-- b000423 | prose | pages [11] -->
Based on the data we have already collected in section 3.2, we solve the model

<!-- b000424 | prose | pages [11] -->
and obtain the following results:

<!-- b000425 | prose | pages [11] -->
⎡1 5

<!-- b000426 | prose | pages [11] -->
 Judging matrix:

<!-- b000427 | prose | pages [11] -->
1/5 1 ⎢ 7/5 7

<!-- b000428 | prose | pages [11] -->
A =

<!-- b000429 | prose | pages [11] -->
⎢ 1 5 ⎢ ⎣ 1 5

<!-- b000430 | prose | pages [11] -->
CW = [0.1996 0.0399

<!-- b000431 | prose | pages [11] -->
 Weight vector of criteria level:

<!-- b000432 | prose | pages [11] -->
5/9 1 1 ⎤ 1/9 1/5 1/5 ⎥ 1 7/5 9/5 ⎥ 5/7 1 9/5 ⎥

<!-- b000433 | furniture | pages [11] -->


<!-- b000434 | prose | pages [11] -->
5/7 1/5 1 ⎦

<!-- b000435 | prose | pages [11] -->
0.2092] 0.3093 0.2419

<!-- b000436 | prose | pages [11] -->
For this level, CI=0.301, CR=0.0269 satisfying

<!-- b000437 | prose | pages [11] -->
 Historical Record:A𝑊𝑊1 = [1.5 −0.5]

<!-- b000438 | prose | pages [11] -->
 Weight vector of alternatives level:

<!-- b000439 | prose | pages [11] -->
𝑅𝑅𝑅𝑅< 0.1.

<!-- b000440 | prose | pages [11] -->
𝐶𝐶𝐶𝐶

<!-- b000441 | furniture | pages [12] -->
Team#28414                                                             Page 12 of 33

<!-- b000442 | prose | pages [12] -->
0.25]  Game Gold Content:A𝑊𝑊2 = [0.75

<!-- b000443 | prose | pages [12] -->
 Playoff Performance: A𝑊𝑊3 = [0.0079 0.5039] 0.0157 0.0315 0.126 0.252

<!-- b000444 | prose | pages [12] -->
𝑅𝑅𝑅𝑅< 0.1.

<!-- b000445 | prose | pages [12] -->
All of these eight vectors satisfy

<!-- b000446 | prose | pages [12] -->
𝐶𝐶𝐶𝐶

<!-- b000447 | prose | pages [12] -->
Finally, we can obtain the final rankings of the top ten college basketball coaches

<!-- b000448 | prose | pages [12] -->
Grade(𝒀𝒀𝟏𝟏) Rank

<!-- b000449 | prose | pages [12] -->
using AHP models.

<!-- b000450 | prose | pages [12] -->
Rank Name

<!-- b000451 | prose | pages [12] -->
1 Mike Krzyzewski 0.8426

<!-- b000452 | prose | pages [12] -->
2 John Wooden 0.7334

<!-- b000453 | prose | pages [12] -->
3 Adolph Rupp 0.6048

<!-- b000454 | prose | pages [12] -->
4 Jim Boeheim 0.5985

<!-- b000455 | prose | pages [12] -->
5 Dean Smith 0.5844

<!-- b000456 | prose | pages [12] -->
Grade(𝒀𝒀𝟏𝟏) Name

<!-- b000457 | prose | pages [12] -->
6 Roy Williams 0.5637

<!-- b000458 | prose | pages [12] -->
7 Bob Knight 0.5479

<!-- b000459 | prose | pages [12] -->
8 Phog Allen 0.4788

<!-- b000460 | prose | pages [12] -->
9 Rick Pitino 0.4683

<!-- b000461 | prose | pages [12] -->
10 Lute Olson 0.4132

<!-- b000462 | caption | pages [12] -->
Table 4.2 the top ten college basketball coaches’ rankings

<!-- b000463 | prose | pages [12] -->
Conclusion:

<!-- b000464 | prose | pages [12] -->
 Analyzing the weight vector of criteria level, we can know that the highest value is

<!-- b000465 | prose | pages [12] -->
the weight of Playoff Performance, so coaches with better game results have

<!-- b000466 | prose | pages [12] -->
more chance in top ranking.

<!-- b000467 | prose | pages [12] -->
 SOS plays a less important role than SRS when determining the Game Gold

<!-- b000468 | prose | pages [12] -->
Content, and the weight of the Game Gold Content is the lowest value in criteria

<!-- b000469 | prose | pages [12] -->
value.

<!-- b000470 | heading | pages [12] -->
4.2 Model II: Fuzzy Synthetic Evaluation (FSE)

<!-- b000471 | heading | pages [12] -->
4.2.1 Quantify grades in the five aspects

<!-- b000472 | prose | pages [12] -->
Fuzzy set theory [6] has been developed and extensively applied since 1965

<!-- b000473 | prose | pages [12] -->
(Zadeh, 1965). It was designed to supplement the interpretation of linguistic or

<!-- b000474 | prose | pages [12] -->
measured uncertainties for real-world random phenomena.

<!-- b000475 | prose | pages [12] -->
In section III, we have already articulate our metrics for ranking. Totally, there are

<!-- b000476 | prose | pages [12] -->
five aspects: historical record, game gold content, playoff performance, honors,

<!-- b000477 | prose | pages [12] -->
{𝑋𝑋1, 𝑋𝑋2, 𝑋𝑋3, 𝑋𝑋4, 𝑋𝑋5}in each of the 5 aspect using the collected data.

<!-- b000478 | prose | pages [12] -->
contribution to sports. Before using the fuzzy set theory, we calculate the grades

<!-- b000479 | prose | pages [12] -->
𝒶𝒶 denotes the number of wins, 𝒷𝒷 denotes the number of loses, 𝜆𝜆𝑤𝑤𝑤𝑤𝑤𝑤 denotes

<!-- b000480 | prose | pages [12] -->
 Calculation rule for historical record:

<!-- b000481 | prose | pages [12] -->
the weight for single win, and 𝜆𝜆𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝑙 denotes the weight for single lose.

<!-- b000482 | prose | pages [12] -->
𝑋𝑋1 = 𝜆𝜆𝑤𝑤𝑤𝑤𝑤𝑤𝒶𝒶−𝜆𝜆𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝒷𝒷                 (4.6)

<!-- b000483 | furniture | pages [13] -->
Team#28414                                                             Page 13 of 33

<!-- b000484 | prose | pages [13] -->
obviously 𝜆𝜆𝑤𝑤𝑤𝑤𝑤𝑤> 𝜆𝜆𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝑙.

<!-- b000485 | furniture | pages [13] -->


<!-- b000486 | prose | pages [13] -->
This formula provides a comprehensive assessment for wins and losses,

<!-- b000487 | prose | pages [13] -->
R denotes the value of SRS, O denotes the value of SOS，𝑂𝑂𝑚𝑚𝑚𝑚𝑚𝑚 denotes the

<!-- b000488 | prose | pages [13] -->
 Calculation rule for game gold content:

<!-- b000489 | prose | pages [13] -->
𝑂𝑂 𝑋𝑋2 = 𝑅𝑅൬1 +

<!-- b000490 | prose | pages [13] -->
൰                    (4.7)

<!-- b000491 | prose | pages [13] -->
maximum value of SOS in the Strength of Schedule system.

<!-- b000492 | prose | pages [13] -->
𝑂𝑂𝑚𝑚𝑚𝑚𝑚𝑚

<!-- b000493 | furniture | pages [13] -->


<!-- b000494 | prose | pages [13] -->
If a coach has higher SRS, it will have higher grade in this aspect because his

<!-- b000495 | prose | pages [13] -->
team is always far ahead its opponents. At the same time, the higher SOS is, the

<!-- b000496 | prose | pages [13] -->
harder games are. So we let the SOS be an addition to SRS.

<!-- b000497 | prose | pages [13] -->
𝑛𝑛𝑘𝑘 denotes the number of times for each class of the playoff results.

<!-- b000498 | prose | pages [13] -->
 Calculation rule for playoff performance:

<!-- b000499 | prose | pages [13] -->
7

<!-- b000500 | prose | pages [13] -->
𝑋𝑋3 = ෍2𝑘𝑘𝑛𝑛𝑘𝑘

<!-- b000501 | prose | pages [13] -->
(4.8)

<!-- b000502 | prose | pages [13] -->
𝑘𝑘=1

<!-- b000503 | furniture | pages [13] -->


<!-- b000504 | prose | pages [13] -->
The number of teams decreases exponentially with power of 2, thus making the

<!-- b000505 | prose | pages [13] -->
then we could finally draw 𝑋𝑋3.

<!-- b000506 | prose | pages [13] -->
weight increase exponentially with power of 2. Sum up the times by designated weight

<!-- b000507 | prose | pages [13] -->
We have already count up the awards by weight (ℋ) in section III, so the formula:

<!-- b000508 | prose | pages [13] -->
 Calculation rule for honors:

<!-- b000509 | prose | pages [13] -->
𝑋𝑋4 = ℋ                                (4.9)

<!-- b000510 | prose | pages [13] -->
We have already give a final grade 𝒞𝒞 for this aspect in section III, so the formula

<!-- b000511 | prose | pages [13] -->
 Calculation rule for contribution to sports:

<!-- b000512 | prose | pages [13] -->
𝑋𝑋5 = 𝒞𝒞                                    (4.10)

<!-- b000513 | prose | pages [13] -->
is:

<!-- b000514 | prose | pages [13] -->
⎧𝑋𝑋1 = 𝜆𝜆𝑤𝑤𝑤𝑤𝑤𝑤𝒶𝒶−𝜆𝜆𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝒷𝒷

<!-- b000515 | prose | pages [13] -->
In conclusion, we form the following quantification rules:

<!-- b000516 | prose | pages [13] -->
𝑂𝑂

<!-- b000517 | prose | pages [13] -->
⎪

<!-- b000518 | prose | pages [13] -->
𝑋𝑋2 = 𝑅𝑅൬1 +

<!-- b000519 | prose | pages [13] -->
൰

<!-- b000520 | prose | pages [13] -->
𝑂𝑂𝑚𝑚𝑚𝑚𝑚𝑚

<!-- b000521 | prose | pages [13] -->
⎪

<!-- b000522 | prose | pages [13] -->
(4.11)

<!-- b000523 | prose | pages [13] -->
7

<!-- b000524 | prose | pages [13] -->
𝑋𝑋3 = ෍2𝑘𝑘𝑛𝑛𝑘𝑘

<!-- b000525 | prose | pages [13] -->
⎨ ⎪

<!-- b000526 | prose | pages [13] -->
𝑘𝑘=1 𝑋𝑋4 = ℋ

<!-- b000527 | prose | pages [13] -->
⎪ ⎩

<!-- b000528 | prose | pages [13] -->
𝑋𝑋5 = 𝒞𝒞

<!-- b000529 | heading | pages [13] -->
4.2.2 Determine membership functions

<!-- b000530 | prose | pages [13] -->
A fuzzy set is defined in terms of a membership function [6] which maps the

<!-- b000531 | furniture | pages [14] -->
Team#28414                                                             Page 14 of 33

<!-- b000532 | prose | pages [14] -->
domain of interest, e.g. concentrations, onto the interval [0, 1]. The shape of the

<!-- b000533 | prose | pages [14] -->
curves shows the membership function for each set. The membership functions

<!-- b000534 | prose | pages [14] -->
Let 𝑋𝑋𝑖𝑖𝑖𝑖 denote the 𝑋𝑋𝑗𝑗 value for the 𝑖𝑖𝑡𝑡ℎ coach and 𝑋𝑋𝑗𝑗(𝑚𝑚𝑚𝑚𝑚𝑚) denote the maximum

<!-- b000535 | prose | pages [14] -->
represent the degree, or weighting, that the specified value belongs to the set.

<!-- b000536 | prose | pages [14] -->
𝑋𝑋𝑗𝑗 value for all the coaches.

<!-- b000537 | prose | pages [14] -->
𝑋𝑋𝑖𝑖𝑖𝑖

<!-- b000538 | prose | pages [14] -->
Here we use the normalization function as membership function:

<!-- b000539 | prose | pages [14] -->
𝜇𝜇𝑗𝑗൫𝑋𝑋𝑖𝑖𝑖𝑖൯= 𝑋𝑋𝑗𝑗(𝑚𝑚𝑚𝑚𝑚𝑚)

<!-- b000540 | prose | pages [14] -->
(4.12)

<!-- b000541 | prose | pages [14] -->
After calculating 𝜇𝜇𝑗𝑗൫𝑋𝑋𝑖𝑖𝑖𝑖൯ for each of the 𝑋𝑋𝑖𝑖𝑖𝑖, we could concluded the fuzzy

<!-- b000542 | prose | pages [14] -->
matrix 𝑋𝑋𝑓𝑓 (N denotes the total number of the coaches).

<!-- b000543 | furniture | pages [14] -->


<!-- b000544 | prose | pages [14] -->
𝜇𝜇1(𝑋𝑋11) …

<!-- b000545 | prose | pages [14] -->
𝑋𝑋𝑓𝑓= [

<!-- b000546 | prose | pages [14] -->
𝜇𝜇𝑁𝑁(𝑋𝑋𝑁𝑁1) 𝜇𝜇1(𝑋𝑋15) … 𝜇𝜇𝑗𝑗൫𝑋𝑋𝑖𝑖𝑖𝑖൯ …

<!-- b000547 | prose | pages [14] -->
]

<!-- b000548 | prose | pages [14] -->
𝜇𝜇𝑁𝑁(𝑋𝑋𝑁𝑁5) …

<!-- b000549 | heading | pages [14] -->
4.2.3 Determine the weights using entropy method

<!-- b000550 | prose | pages [14] -->
The principle of entropy method [13] states that, subject to precisely stated prior

<!-- b000551 | prose | pages [14] -->
data (such as a proposition that expresses testable information), the probability

<!-- b000552 | prose | pages [14] -->
distribution which best represents the current state of knowledge is the one with

<!-- b000553 | prose | pages [14] -->
 Calculate the characteristic weight 𝑝𝑝𝑖𝑖𝑖𝑖for the 𝑖𝑖𝑡𝑡ℎ coach’s 𝑗𝑗𝑡𝑡ℎ evaluation grade

<!-- b000554 | prose | pages [14] -->
largest entropy. To use entropy method, there are mainly 5 steps:

<!-- b000555 | prose | pages [14] -->
(𝑋𝑋𝑖𝑖𝑖𝑖) based on the normalized fuzzy matrix 𝑋𝑋𝑓𝑓:

<!-- b000556 | prose | pages [14] -->
𝑋𝑋𝑓𝑓(𝑖𝑖,𝑗𝑗)

<!-- b000557 | prose | pages [14] -->
𝑝𝑝𝑖𝑖𝑖𝑖=

<!-- b000558 | prose | pages [14] -->
∑ 𝑋𝑋𝑓𝑓(𝑖𝑖,𝑗𝑗) 𝑁𝑁 𝑖𝑖=1

<!-- b000559 | prose | pages [14] -->
(4.13)

<!-- b000560 | prose | pages [14] -->
 Calculate the entropy for the 𝑗𝑗𝑡𝑡ℎ evaluation grade:

<!-- b000561 | prose | pages [14] -->
1

<!-- b000562 | prose | pages [14] -->
𝑁𝑁

<!-- b000563 | prose | pages [14] -->
ln(𝑁𝑁) ෍𝑝𝑝𝑖𝑖𝑖𝑖𝑙𝑙𝑙𝑙(𝑝𝑝𝑖𝑖𝑖𝑖) 𝑒𝑒𝑗𝑗= −

<!-- b000564 | prose | pages [14] -->
𝑖𝑖=1

<!-- b000565 | prose | pages [14] -->
(4.14)

<!-- b000566 | prose | pages [14] -->
 Calculate the diversity factor for the 𝑗𝑗𝑡𝑡ℎ evaluation grade:

<!-- b000567 | prose | pages [14] -->
𝑔𝑔𝑗𝑗= 1 −𝑒𝑒𝑗𝑗                                (4.15)

<!-- b000568 | prose | pages [14] -->
𝑔𝑔𝑗𝑗 𝑤𝑤𝑗𝑗=

<!-- b000569 | prose | pages [14] -->
(4.16)

<!-- b000570 | prose | pages [14] -->
 Determine the weight for each evaluation grade:

<!-- b000571 | prose | pages [14] -->
∑ 𝑔𝑔𝑗𝑗 5 𝑗𝑗=1

<!-- b000572 | prose | pages [14] -->
 Determine the final score Y for each coach；

<!-- b000573 | prose | pages [14] -->
𝑌𝑌2 = W ∗ 𝑋𝑋𝑓𝑓                     (4.17)

<!-- b000574 | furniture | pages [15] -->
Team#28414                                                             Page 15 of 33

<!-- b000575 | heading | pages [15] -->
4.2.4 Results & analysis

<!-- b000576 | prose | pages [15] -->
𝒑𝒑𝒊𝒊𝒊𝒊 𝑿𝑿𝟏𝟏 𝑿𝑿𝟐𝟐 𝑿𝑿𝟑𝟑 𝑿𝑿𝟑𝟑 𝑿𝑿𝟓𝟓 𝒀𝒀𝟐𝟐

<!-- b000577 | prose | pages [15] -->
Characteristic weight, entropy, diversity factor and weight are shown as follows:

<!-- b000578 | prose | pages [15] -->
0.15 0.04 0.06 John Wooden 0.13 0.08 0.8708

<!-- b000579 | prose | pages [15] -->
0.10 0.07 0.06 Mike Krzy 0.13 0.08 0.8629

<!-- b000580 | prose | pages [15] -->
0.08 0.06 0.06 Adolph Rupp 0.11 0.02 0.675

<!-- b000581 | prose | pages [15] -->
0.08 0.06 0.06 Dean Smith 0.04 0.05 0.609

<!-- b000582 | prose | pages [15] -->
0.06 0.05 0.06 Bob Knight 0.07 0.05 0.6052

<!-- b000583 | prose | pages [15] -->
0.06 0.06 0.05 Roy Williams 0.04 0.08 0.5872

<!-- b000584 | prose | pages [15] -->
0.05 0.06 0.03 Jim Boeheim 0.03 0.01 0.5864

<!-- b000585 | prose | pages [15] -->
0.05 0.04 0.04 Phog Allen 0.05 0.05 0.4874

<!-- b000586 | prose | pages [15] -->
0.04 0.04 0.04 Henry Iba

<!-- b000587 | prose | pages [15] -->
𝒈𝒈𝒋𝒋

<!-- b000588 | prose | pages [15] -->
0.04 0.02 0.4664

<!-- b000589 | prose | pages [15] -->
0.04 0.06 0.04 Lute Olson

<!-- b000590 | prose | pages [15] -->
𝒘𝒘𝒋𝒋

<!-- b000591 | prose | pages [15] -->
0.06 0.07 0.4538

<!-- b000592 | prose | pages [15] -->
-1.04 -0.99 -1.00 -0.96 -0.93 0.4336

<!-- b000593 | prose | pages [15] -->
0.23 0.18 0.16 0.20 0.22 0.8708

<!-- b000594 | caption | pages [15] -->
Table 4.3 the results for FSE

<!-- b000595 | prose | pages [15] -->
 The playoff performance (𝑋𝑋3) plays the most important role (with 0.23 weight) in

<!-- b000596 | prose | pages [15] -->
 The weights for each aspect is near to each other.

<!-- b000597 | prose | pages [15] -->
FSE evaluating.

<!-- b000598 | prose | pages [15] -->
 The coaches whose playoff performance is better will enjoy priority to some extent.

<!-- b000599 | prose | pages [15] -->
At the same time, the coaches who have amazing game gold content (with only

<!-- b000600 | prose | pages [15] -->
0.16 weight) might not outstand.

<!-- b000601 | heading | pages [15] -->
V. Models Combination

<!-- b000602 | heading | pages [15] -->
5.1 Evaluation of individual model

<!-- b000603 | prose | pages [15] -->
distance D is defined.

<!-- b000604 | prose | pages [15] -->
In order to evaluate the accuracy of our two individual models, average offset

<!-- b000605 | furniture | pages [15] -->


<!-- b000606 | prose | pages [15] -->
We collect ranking lists of top 10 NCAA basketball coaches from several

<!-- b000607 | furniture | pages [15] -->


<!-- b000608 | prose | pages [15] -->
News [15]. Then compare our results to those lists and average offset distance D

<!-- b000609 | prose | pages [15] -->
authoritative media such as ESPN, Bleacher Report, Yahoo Sports, and Sporting

<!-- b000610 | prose | pages [15] -->
reflects the difference.

<!-- b000611 | prose | pages [15] -->
Here we use the first-order Minkowski distance to denote the average offset

<!-- b000612 | furniture | pages [15] -->


<!-- b000613 | prose | pages [15] -->
distance of the top 10.

<!-- b000614 | furniture | pages [16] -->
Team#28414                                                             Page 16 of 33

<!-- b000615 | prose | pages [16] -->
D = 1

<!-- b000616 | prose | pages [16] -->
𝑛𝑛

<!-- b000617 | prose | pages [16] -->
10

<!-- b000618 | prose | pages [16] -->
10𝑛𝑛෍෍ห𝑗𝑗− 𝑟𝑟𝑗𝑗ห

<!-- b000619 | prose | pages [16] -->
𝑖𝑖=1

<!-- b000620 | prose | pages [16] -->
𝑗𝑗=1

<!-- b000621 | prose | pages [16] -->
(5.1)

<!-- b000622 | prose | pages [16] -->
Where n is the number of the top 10 ranking lists, j is the ranking in the 𝑖𝑖𝑡𝑡ℎ list,

<!-- b000623 | prose | pages [16] -->
and 𝑟𝑟𝑗𝑗 is the ranking of 𝑗𝑗𝑡𝑡ℎ coach in our results. So ห𝑗𝑗− 𝑟𝑟𝑗𝑗ห denotes the difference

<!-- b000624 | prose | pages [16] -->
between result of media and ours, and D means the average difference. If our results

<!-- b000625 | prose | pages [16] -->
𝐷𝐷𝛼𝛼  is the average offset distance of top 5

<!-- b000626 | prose | pages [16] -->
are the same as all media selection results, then D is equal to zero.

<!-- b000627 | prose | pages [16] -->
𝐷𝐷𝛼𝛼= 1

<!-- b000628 | prose | pages [16] -->
𝑛𝑛

<!-- b000629 | prose | pages [16] -->
5

<!-- b000630 | prose | pages [16] -->
5𝑛𝑛෍෍ห𝑗𝑗− 𝑟𝑟𝑗𝑗ห

<!-- b000631 | prose | pages [16] -->
𝑖𝑖=1

<!-- b000632 | prose | pages [16] -->
𝑗𝑗=1

<!-- b000633 | prose | pages [16] -->
(5.2)

<!-- b000634 | prose | pages [16] -->
𝐷𝐷𝛽𝛽  is the average offset distance of 6th to 10th.

<!-- b000635 | prose | pages [16] -->
𝐷𝐷𝛽𝛽= 1

<!-- b000636 | prose | pages [16] -->
𝑛𝑛

<!-- b000637 | prose | pages [16] -->
10

<!-- b000638 | prose | pages [16] -->
5𝑛𝑛෍෍ห𝑗𝑗− 𝑟𝑟𝑗𝑗ห

<!-- b000639 | prose | pages [16] -->
𝑖𝑖=1

<!-- b000640 | prose | pages [16] -->
𝑗𝑗=6

<!-- b000641 | prose | pages [16] -->
(5.3)

<!-- b000642 | prose | pages [16] -->
Obviously model with smaller average offset distance should get higher score. So

<!-- b000643 | furniture | pages [16] -->


<!-- b000644 | prose | pages [16] -->
We can define hit score

<!-- b000645 | prose | pages [16] -->
9+𝐷𝐷 (0 < 𝑔𝑔< 100)           (5.4)

<!-- b000646 | prose | pages [16] -->
g =

<!-- b000647 | prose | pages [16] -->
900

<!-- b000648 | prose | pages [16] -->
When D = 0, g= 100, means if there is no average offset distance, this model can

<!-- b000649 | prose | pages [16] -->
get full marks 100. Here are our results:

<!-- b000650 | prose | pages [16] -->
𝑫𝑫𝜶𝜶

<!-- b000651 | furniture | pages [16] -->


<!-- b000652 | prose | pages [16] -->
AHP

<!-- b000653 | prose | pages [16] -->
1.75

<!-- b000654 | prose | pages [16] -->
𝑫𝑫𝜷𝜷 3.1

<!-- b000655 | prose | pages [16] -->
𝐃𝐃

<!-- b000656 | prose | pages [16] -->
𝒈𝒈𝜶𝜶

<!-- b000657 | prose | pages [16] -->
2.425

<!-- b000658 | prose | pages [16] -->
83.72

<!-- b000659 | prose | pages [16] -->
𝒈𝒈𝜷𝜷 73.38

<!-- b000660 | prose | pages [16] -->
𝐠𝐠 78.77

<!-- b000661 | prose | pages [16] -->
FSE

<!-- b000662 | prose | pages [16] -->
1.15

<!-- b000663 | prose | pages [16] -->
2.85

<!-- b000664 | prose | pages [16] -->
2

<!-- b000665 | prose | pages [16] -->
88.67

<!-- b000666 | prose | pages [16] -->
75.94

<!-- b000667 | prose | pages [16] -->
81.81

<!-- b000668 | caption | pages [16] -->
Table 5.1 the results for evaluation

<!-- b000669 | prose | pages [16] -->
 Vertical comparison: Either AHP or Fuzzy Synthetic Evaluation  𝐷𝐷𝛼𝛼 is obviously

<!-- b000670 | prose | pages [16] -->
Conclusions:

<!-- b000671 | prose | pages [16] -->
smaller than 𝐷𝐷𝛽𝛽. It means that the results are more reasonable in top 5 than in top

<!-- b000672 | prose | pages [16] -->
10.

<!-- b000673 | furniture | pages [17] -->
Team#28414                                                             Page 17 of 33

<!-- b000674 | prose | pages [17] -->
 Horizontal comparison: Fuzzy Synthetic Evaluation performs better than AHP in

<!-- b000675 | prose | pages [17] -->
both top 5 and top 10. It proves that Fuzzy Synthetic Evaluation is more accurate

<!-- b000676 | prose | pages [17] -->
than AHP. Because AHP depends on artificial scoring which is too subjective.

<!-- b000677 | heading | pages [17] -->
5.2 Aggregation Model

<!-- b000678 | prose | pages [17] -->
AHP is a subjective method, it largely depends on artificial scoring; Relatively,

<!-- b000679 | furniture | pages [17] -->


<!-- b000680 | prose | pages [17] -->
Fuzzy Synthetic Evaluation is an objective method, it all depends on the data. To

<!-- b000681 | prose | pages [17] -->
comprehensively consider the effect of subjective and objective factors, we adopt

<!-- b000682 | prose | pages [17] -->
൜ 𝑊𝑊1 + 𝑊𝑊2 = 1

<!-- b000683 | prose | pages [17] -->
linear weighted method:

<!-- b000684 | prose | pages [17] -->
Y =  𝑊𝑊1𝑌𝑌1 + 𝑊𝑊2𝑌𝑌2         (5.5)

<!-- b000685 | prose | pages [17] -->
𝑌𝑌1 is the evaluation grade of AHP model , 𝑌𝑌2 is the evaluation grade of Fuzzy

<!-- b000686 | prose | pages [17] -->
To determine the weight 𝑊𝑊1 and 𝑊𝑊2, we take D(the average offset distance) into

<!-- b000687 | prose | pages [17] -->
Synthetic Evaluation model. All of them range from 0 to 1.

<!-- b000688 | furniture | pages [17] -->


<!-- b000689 | prose | pages [17] -->
consideration. Since smaller average offset distance means the more accuracy

<!-- b000690 | prose | pages [17] -->
𝐷𝐷2 ⎧𝑊𝑊1 =

<!-- b000691 | prose | pages [17] -->
results, we can assign higher weight to the mode with smaller D. Then we get

<!-- b000692 | prose | pages [17] -->
𝐷𝐷1 + 𝐷𝐷2

<!-- b000693 | prose | pages [17] -->
𝐷𝐷1

<!-- b000694 | prose | pages [17] -->
⎨

<!-- b000695 | prose | pages [17] -->
𝑊𝑊2 =

<!-- b000696 | prose | pages [17] -->
⎩

<!-- b000697 | prose | pages [17] -->
𝐷𝐷1 + 𝐷𝐷2

<!-- b000698 | prose | pages [17] -->
(5.6)

<!-- b000699 | prose | pages [17] -->
Y =  𝑊𝑊1𝑌𝑌1 + 𝑊𝑊2𝑌𝑌2              (5.7)

<!-- b000700 | prose | pages [17] -->
In conclusion, our final model can be defined as:

<!-- b000701 | heading | pages [17] -->
5.3 Results & analysis

<!-- b000702 | furniture | pages [17] -->


<!-- b000703 | furniture | pages [17] -->


<!-- b000704 | prose | pages [17] -->
AHP

<!-- b000705 | prose | pages [17] -->
Rank 1 Mike Krzyzewski

<!-- b000706 | prose | pages [17] -->
Rank 2 John Wooden

<!-- b000707 | prose | pages [17] -->
Rank 3 Adolph Rupp

<!-- b000708 | prose | pages [17] -->
Rank 4 Jim Boeheim

<!-- b000709 | prose | pages [17] -->
Rank 5 Dean Smith

<!-- b000710 | prose | pages [17] -->
Rank 6 Roy Williams

<!-- b000711 | prose | pages [17] -->
Rank 7 Bob Knight

<!-- b000712 | prose | pages [17] -->
Rank 8 Phog Allen

<!-- b000713 | prose | pages [17] -->
Rank 9 Rick Pitino

<!-- b000714 | prose | pages [17] -->
Rank 10 Lute Olson

<!-- b000715 | prose | pages [17] -->
FSE AM

<!-- b000716 | prose | pages [17] -->
John Wooden John Wooden

<!-- b000717 | prose | pages [17] -->
Mike Krzyzewski Mike Krzyzewski

<!-- b000718 | prose | pages [17] -->
Adolph Rupp Adolph Rupp

<!-- b000719 | prose | pages [17] -->
Dean Smith Dean Smith

<!-- b000720 | prose | pages [17] -->
Bob Knight Bob Knight

<!-- b000721 | prose | pages [17] -->
Roy Williams Jim Boeheim

<!-- b000722 | prose | pages [17] -->
Jim Boeheim Roy Williams

<!-- b000723 | prose | pages [17] -->
Phog Allen Phog Allen

<!-- b000724 | prose | pages [17] -->
Rick Pitino Rick Pitino

<!-- b000725 | prose | pages [17] -->
Henry Iba Henry Iba

<!-- b000726 | furniture | pages [18] -->
Team#28414                                                             Page 18 of 33

<!-- b000727 | prose | pages [18] -->
Top5 Hit score 83.72

<!-- b000728 | prose | pages [18] -->
Top10 Hit score 78.77

<!-- b000729 | prose | pages [18] -->
88.67 88.67

<!-- b000730 | prose | pages [18] -->
81.81 82.57

<!-- b000731 | caption | pages [18] -->
Table 5.2 the ranking comparison among the models

<!-- b000732 | prose | pages [18] -->
Conclusion:

<!-- b000733 | prose | pages [18] -->
 All our models perform better in top 5 than in top 10. It proves that the top 5

<!-- b000734 | prose | pages [18] -->
coaches in college basketball history are less controversial than top 10.

<!-- b000735 | prose | pages [18] -->
 The result of AM is very similar to FSE. They have the same hit score 88.67 in top

<!-- b000736 | prose | pages [18] -->
5; but in top 10, AM have highest hit score 82.57 in these three models. It proves

<!-- b000737 | prose | pages [18] -->
the combination can improve our model.

<!-- b000738 | prose | pages [18] -->
 According to our final result, our model’s top 5 coaches in college basketball are

<!-- b000739 | prose | pages [18] -->
John Wooden, Mike Krzyzewski, Adolph Rupp, Dean Smith and Bob Knight.

<!-- b000740 | heading | pages [18] -->
VI. Extend Our Models

<!-- b000741 | heading | pages [18] -->
6.1 Genders do not matter

<!-- b000742 | prose | pages [18] -->
Now we take genders into consideration. We still use basketball as an example,

<!-- b000743 | furniture | pages [18] -->


<!-- b000744 | prose | pages [18] -->
and rank the top ten college women’s basketball coaches [20] for the previous century.

<!-- b000745 | prose | pages [18] -->
Searching from the internet, we collect the relative data about 50 college women’s

<!-- b000746 | prose | pages [18] -->
basketball coaches [18] with 600 and other 5 coaches who have established

<!-- b000747 | prose | pages [18] -->
outstanding traditions, earned many awards and garnered recognition for their

<!-- b000748 | prose | pages [18] -->
colleges. Then we rank them with our models mentioned above.

<!-- b000749 | prose | pages [18] -->
Coaches’ ranking with the Aggregation Model:

<!-- b000750 | prose | pages [18] -->
Rank Name Grade

<!-- b000751 | prose | pages [18] -->
Pat Summitt 1 0.8532

<!-- b000752 | prose | pages [18] -->
Geno Auriemma 2 0.8434

<!-- b000753 | prose | pages [18] -->
Tara VanDerveer 3 0.7465

<!-- b000754 | prose | pages [18] -->
Leon Barmore 4 0.7236

<!-- b000755 | prose | pages [18] -->
C. Vivian Stringer 5 0.6074

<!-- b000756 | prose | pages [18] -->
Rank Name Grade

<!-- b000757 | prose | pages [18] -->
Sylvia Hatchell 6 0.5875

<!-- b000758 | prose | pages [18] -->
Jody Conradt 7 0.5673

<!-- b000759 | prose | pages [18] -->
Kay Yow 8 0.5486

<!-- b000760 | prose | pages [18] -->
Sue Gunter 9 0.4783

<!-- b000761 | prose | pages [18] -->
Gail Goestenkors 10 0.4379

<!-- b000762 | caption | pages [18] -->
Table 6.1 the ranking for coaches of women’s basketball

<!-- b000763 | prose | pages [18] -->
From the sports.yahoo.com [19], we get a list of the all-time top ten NCAA women’s

<!-- b000764 | prose | pages [18] -->
basketball coaches, and the list is shown in following table.

<!-- b000765 | prose | pages [18] -->
Rank Name

<!-- b000766 | prose | pages [18] -->
Pat Summitt 1

<!-- b000767 | prose | pages [18] -->
Geno Auriemma 2

<!-- b000768 | prose | pages [18] -->
Rank Name

<!-- b000769 | prose | pages [18] -->
Jody Conradt 6

<!-- b000770 | prose | pages [18] -->
Kay Yow 7

<!-- b000771 | furniture | pages [19] -->
Team#28414                                                             Page 19 of 33

<!-- b000772 | prose | pages [19] -->
Leon Barmore 3

<!-- b000773 | prose | pages [19] -->
C. Vivian Stringer 4

<!-- b000774 | prose | pages [19] -->
Tara VanDerveer 5

<!-- b000775 | prose | pages [19] -->
Sylvia Hatchell 8

<!-- b000776 | prose | pages [19] -->
9 Gail Goestenkors

<!-- b000777 | prose | pages [19] -->
Sue Gunter 10

<!-- b000778 | caption | pages [19] -->
Table 6.2 the ranking from Yahoo

<!-- b000779 | prose | pages [19] -->
Using the average offset distance mentioned in section 5; we can measure the hit

<!-- b000780 | prose | pages [19] -->
score for our models. All results of our models are in agreement within reasonable

<!-- b000781 | prose | pages [19] -->
error range (hit score = 87.57), so that we can safely address the conclusion that our

<!-- b000782 | prose | pages [19] -->
models can be applied in general across both genders.

<!-- b000783 | heading | pages [19] -->
6.2 Time factor does make a difference

<!-- b000784 | heading | pages [19] -->
6.2.1 Why time factor matters?

<!-- b000785 | prose | pages [19] -->
National Collegiate Athletic Association Basketball Tournament [14] started at 1939,

<!-- b000786 | prose | pages [19] -->
during the 74 years’ development, while the number of teams participating in the

<!-- b000787 | prose | pages [19] -->
tournament increasing a lot, the competition becomes fiercer. Also in different

<!-- b000788 | prose | pages [19] -->
historical periods, the NCAA Basketball Tournament gained different popularity, and

<!-- b000789 | prose | pages [19] -->
To quantify the time factor, we attach weight 𝑤𝑤𝑖𝑖 (1-10) to different time periods

<!-- b000790 | prose | pages [19] -->
this also influences the quality of the evaluation grades.

<!-- b000791 | prose | pages [19] -->
mainly based on the turning points that occurred in the period.

<!-- b000792 | prose | pages [19] -->
𝒘𝒘𝒊𝒊

<!-- b000793 | prose | pages [19] -->
The following table shows the critical years in the NCAA history [14]:

<!-- b000794 | prose | pages [19] -->
Year Turning points

<!-- b000795 | prose | pages [19] -->
1913-1939 There are no national college basketball competition.

<!-- b000796 | prose | pages [19] -->
1939-1951

<!-- b000797 | prose | pages [19] -->
5

<!-- b000798 | prose | pages [19] -->
NCAA Basketball Tournament started, and 8 teams

<!-- b000799 | prose | pages [19] -->
6

<!-- b000800 | prose | pages [19] -->
anticipated. There are two college tournament: NIT and

<!-- b000801 | prose | pages [19] -->
NCAA.

<!-- b000802 | prose | pages [19] -->
1951-1975 16 teams anticipated, NIT became second class competition.

<!-- b000803 | prose | pages [19] -->
1975-1980

<!-- b000804 | prose | pages [19] -->
7

<!-- b000805 | prose | pages [19] -->
32 teams anticipated, especially in 1979, Magic Johnson fight

<!-- b000806 | prose | pages [19] -->
8

<!-- b000807 | prose | pages [19] -->
with Larry Bird in the finals, achieving 24.1% audience rating,

<!-- b000808 | prose | pages [19] -->
then a golden age came.

<!-- b000809 | prose | pages [19] -->
1980-1985 48 teams anticipated,

<!-- b000810 | prose | pages [19] -->
1985-2013 64 teams anticipated.

<!-- b000811 | prose | pages [19] -->
9

<!-- b000812 | prose | pages [19] -->
10

<!-- b000813 | caption | pages [19] -->
Table 6.3 the time weights for each time period

<!-- b000814 | heading | pages [19] -->
6.2.2 How time factor matters?

<!-- b000815 | prose | pages [19] -->
The whole metric system will change after introducing the time weight. What

<!-- b000816 | furniture | pages [20] -->
Team#28414                                                             Page 20 of 33

<!-- b000817 | prose | pages [20] -->
 The evaluation norms will change after introducing the time weight (𝑤𝑤𝑖𝑖).

<!-- b000818 | prose | pages [20] -->
follows in the chapter will be devoted to explaining the changes in detail.

<!-- b000819 | prose | pages [20] -->
⎧a = ෍𝑤𝑤𝑖𝑖𝑎𝑎𝑖𝑖 ⎪

<!-- b000820 | prose | pages [20] -->
𝑖𝑖

<!-- b000821 | prose | pages [20] -->
⎪

<!-- b000822 | prose | pages [20] -->
b = ෍𝑤𝑤𝑖𝑖𝑏𝑏𝑖𝑖

<!-- b000823 | prose | pages [20] -->
⎪ ⎪

<!-- b000824 | prose | pages [20] -->
𝑖𝑖

<!-- b000825 | prose | pages [20] -->
R = ∑𝑤𝑤𝑖𝑖𝑆𝑆𝑆𝑆𝑆𝑆𝑖𝑖

<!-- b000826 | prose | pages [20] -->
⎪ ⎪

<!-- b000827 | prose | pages [20] -->
𝑖𝑖

<!-- b000828 | prose | pages [20] -->
𝑡𝑡

<!-- b000829 | prose | pages [20] -->
⎪

<!-- b000830 | prose | pages [20] -->
O = ∑𝑤𝑤𝑖𝑖𝑆𝑆𝑆𝑆𝑆𝑆𝑖𝑖 𝑖𝑖

<!-- b000831 | prose | pages [20] -->
𝑡𝑡

<!-- b000832 | prose | pages [20] -->
⎨ ⎪

<!-- b000833 | prose | pages [20] -->
(6.1)

<!-- b000834 | prose | pages [20] -->
𝑛𝑛𝑘𝑘= ෍𝑤𝑤𝑖𝑖𝑚𝑚𝑘𝑘𝑘𝑘

<!-- b000835 | prose | pages [20] -->
⎪ ⎪

<!-- b000836 | prose | pages [20] -->
𝑖𝑖

<!-- b000837 | prose | pages [20] -->
⎪

<!-- b000838 | prose | pages [20] -->
ℋ= ෍𝓀𝓀𝑖𝑖

<!-- b000839 | prose | pages [20] -->
⎪ ⎪

<!-- b000840 | prose | pages [20] -->
𝑖𝑖

<!-- b000841 | prose | pages [20] -->
⎪

<!-- b000842 | prose | pages [20] -->
𝒞𝒞= ෍𝒸𝒸𝑖𝑖

<!-- b000843 | prose | pages [20] -->
⎩

<!-- b000844 | prose | pages [20] -->
𝑖𝑖

<!-- b000845 | prose | pages [20] -->
 a  denotes the wins, 𝑎𝑎𝑖𝑖 denotes the wins per year. Where  b  denotes the loses, 𝑏𝑏𝑖𝑖 denotes the loses per year.  R denotes the average SRS, 𝑆𝑆𝑆𝑆𝑆𝑆𝑖𝑖 denotes the losses per year.  O denotes the average SOS, 𝑆𝑆𝑆𝑆𝑆𝑆𝑖𝑖 denotes the losses per year, t denotes the

<!-- b000846 | prose | pages [20] -->
 The binary variable 𝑚𝑚𝑘𝑘𝑘𝑘 denotes whether the team get the 𝑘𝑘𝑡𝑡ℎ class in the 𝑖𝑖𝑡𝑡ℎ number of years.

<!-- b000847 | prose | pages [20] -->
year.  𝑛𝑛𝑘𝑘 denotes the number of times for each class.  𝓀𝓀𝑖𝑖 denotes the weight for each award, ℋ denotes the total weights of all the

<!-- b000848 | prose | pages [20] -->
 𝒸𝒸𝑖𝑖 denotes the points for each aspect, 𝒞𝒞 denotes the total points.

<!-- b000849 | prose | pages [20] -->
awards a coach has ever got.

<!-- b000850 | furniture | pages [20] -->


<!-- b000851 | prose | pages [20] -->
 Accordingly, the results for AHP (model I) & FSE (model II) will change.

<!-- b000852 | prose | pages [20] -->
The following table shows how AHP (model I) will change (The names in bold are the

<!-- b000853 | prose | pages [20] -->
AHP(without 𝒘𝒘𝒊𝒊)

<!-- b000854 | prose | pages [20] -->
people whose rank has changed):

<!-- b000855 | prose | pages [20] -->
Grades (Top 10)

<!-- b000856 | prose | pages [20] -->
Mike Krzyzewski 0.8426

<!-- b000857 | prose | pages [20] -->
John Wooden 0.7334

<!-- b000858 | prose | pages [20] -->
Adolph Rupp 0.6048

<!-- b000859 | prose | pages [20] -->
Jim Boeheim 0.5985

<!-- b000860 | prose | pages [20] -->
Dean Smith 0.5844

<!-- b000861 | prose | pages [20] -->
Roy Williams 0.5637

<!-- b000862 | prose | pages [20] -->
Bob Knight 0.5479

<!-- b000863 | prose | pages [20] -->
AHP(with 𝒘𝒘𝒊𝒊 ) Grades (Top 10)

<!-- b000864 | prose | pages [20] -->
Mike Krzyzewski 0.8894

<!-- b000865 | prose | pages [20] -->
John Wooden 0.7601

<!-- b000866 | prose | pages [20] -->
Jim Boeheim 0.6465

<!-- b000867 | prose | pages [20] -->
Adolph Rupp 0.6322

<!-- b000868 | prose | pages [20] -->
Dean Smith 0.6251

<!-- b000869 | prose | pages [20] -->
Roy Williams 0.6137

<!-- b000870 | prose | pages [20] -->
Bob Knight 0.5922

<!-- b000871 | furniture | pages [21] -->
Team#28414                                                             Page 21 of 33

<!-- b000872 | prose | pages [21] -->
Phog Allen 0.4788

<!-- b000873 | prose | pages [21] -->
Rick Pitino 0.4683

<!-- b000874 | prose | pages [21] -->
Lute Olson 0.4132

<!-- b000875 | prose | pages [21] -->
Top10 Hit score 78.77

<!-- b000876 | prose | pages [21] -->
Top5 Hit score 83.72

<!-- b000877 | prose | pages [21] -->
Rick Pitino 0.5171

<!-- b000878 | prose | pages [21] -->
Phog Allen 0.5062

<!-- b000879 | prose | pages [21] -->
Lute Olson 0.4606

<!-- b000880 | prose | pages [21] -->
Top10 Hit score 76.60

<!-- b000881 | prose | pages [21] -->
Top5 Hit score 83.56

<!-- b000882 | caption | pages [21] -->
Table 6.4 what is different in AHP introducing time weight?

<!-- b000883 | prose | pages [21] -->
Conclusion:  In model I (AHP), Top5 hit score changes from 83.72 to 83.56, namely, Top5 hit

<!-- b000884 | prose | pages [21] -->
score nearly remains unchanged.  Top10 hit score changes from 78.77 to 76.60, namely, Top10 hit score falls to

<!-- b000885 | prose | pages [21] -->
some extent.  The changes in rankings occur only locally, not globally.

<!-- b000886 | furniture | pages [21] -->


<!-- b000887 | prose | pages [21] -->
The following table shows how FSE (model II) will change (The names in bold are

<!-- b000888 | prose | pages [21] -->
FSE (without 𝒘𝒘𝒊𝒊)

<!-- b000889 | prose | pages [21] -->
the people whose rank has changed):

<!-- b000890 | prose | pages [21] -->
Grades (Top 10)

<!-- b000891 | prose | pages [21] -->
John Wooden 0.8708

<!-- b000892 | prose | pages [21] -->
Mike Krzyzewski 0.8629

<!-- b000893 | prose | pages [21] -->
Adolph Rupp 0.6750

<!-- b000894 | prose | pages [21] -->
Dean Smith 0.6090

<!-- b000895 | prose | pages [21] -->
Bob Knight 0.6052

<!-- b000896 | prose | pages [21] -->
Roy Williams 0.5872

<!-- b000897 | prose | pages [21] -->
Jim Boeheim 0.5864

<!-- b000898 | prose | pages [21] -->
Phog Allen 0.4874

<!-- b000899 | prose | pages [21] -->
Rick Pitino 0.4664

<!-- b000900 | prose | pages [21] -->
Henry Iba 0.4538

<!-- b000901 | prose | pages [21] -->
Top10 Hit score 81.81

<!-- b000902 | prose | pages [21] -->
Top5 Hit score 88.67

<!-- b000903 | prose | pages [21] -->
FSE (with 𝒘𝒘𝒊𝒊 ) Grades (Top 10)

<!-- b000904 | prose | pages [21] -->
Mike Krzyzewski 0.9337

<!-- b000905 | prose | pages [21] -->
John Wooden 0.7850

<!-- b000906 | prose | pages [21] -->
Roy Williams 0.6556

<!-- b000907 | prose | pages [21] -->
Jim Boeheim 0.6260

<!-- b000908 | prose | pages [21] -->
Bob Knight 0.6207

<!-- b000909 | prose | pages [21] -->
Dean Smith 0.5984

<!-- b000910 | prose | pages [21] -->
Adolph Rupp 0.5445

<!-- b000911 | prose | pages [21] -->
Rick Pitino 0.5164

<!-- b000912 | prose | pages [21] -->
Lute Olson 0.4603

<!-- b000913 | prose | pages [21] -->
Tom Izzo 0.4292

<!-- b000914 | prose | pages [21] -->
Top10 Hit score 75.31

<!-- b000915 | prose | pages [21] -->
Top5 Hit score 84.51

<!-- b000916 | caption | pages [21] -->
Table 6.5 what is different in FSE introducing time weight?

<!-- b000917 | prose | pages [21] -->
Conclusion:  In model II (FSE), Top5 hit score changes from 88.67 to 84.51, namely, Top5 hit

<!-- b000918 | prose | pages [21] -->
score falls to some extent.  Top10 hit score changes from 81.81 to 75.31, namely, Top10 hit score falls a lot.

<!-- b000919 | prose | pages [21] -->
The model appears to be more inaccurate.  The changes in rankings occur globally. The model appears to be easily

<!-- b000920 | prose | pages [21] -->
influenced by the time weights.

<!-- b000921 | furniture | pages [21] -->


<!-- b000922 | prose | pages [21] -->
 There is no doubt that the results for Aggregation Model (AM) will also change.

<!-- b000923 | furniture | pages [22] -->
Team#28414                                                             Page 22 of 33

<!-- b000924 | prose | pages [22] -->
The following table shows how aggregation model (final model) will change (The

<!-- b000925 | prose | pages [22] -->
AM (without 𝒘𝒘𝒊𝒊) AM (with 𝒘𝒘𝒊𝒊 )

<!-- b000926 | prose | pages [22] -->
names in bold are the people whose rank has changed):

<!-- b000927 | prose | pages [22] -->
Grades (Top 10)

<!-- b000928 | prose | pages [22] -->
John Wooden 0.8568

<!-- b000929 | prose | pages [22] -->
Mike Krzyzewski 0.8296

<!-- b000930 | prose | pages [22] -->
Adolph Rupp 0.6539

<!-- b000931 | prose | pages [22] -->
Dean Smith 0.6016

<!-- b000932 | prose | pages [22] -->
Bob Knight 0.5900

<!-- b000933 | prose | pages [22] -->
Jim Boeheim 0.5880

<!-- b000934 | prose | pages [22] -->
Roy Williams 0.5802

<!-- b000935 | prose | pages [22] -->
Phog Allen 0.4848

<!-- b000936 | prose | pages [22] -->
Rick Pitino 0.4669

<!-- b000937 | prose | pages [22] -->
Henry Iba 0.4308

<!-- b000938 | prose | pages [22] -->
Top10 Hit score 82.57

<!-- b000939 | prose | pages [22] -->
Top5 Hit score 88.67

<!-- b000940 | prose | pages [22] -->
Grades (Top 10)

<!-- b000941 | prose | pages [22] -->
Mike Krzyzewski 0.9204

<!-- b000942 | prose | pages [22] -->
John Wooden 0.7775

<!-- b000943 | prose | pages [22] -->
Roy Williams 0.6430

<!-- b000944 | prose | pages [22] -->
Jim Boeheim 0.6322

<!-- b000945 | prose | pages [22] -->
Bob Knight 0.6122

<!-- b000946 | prose | pages [22] -->
Dean Smith 0.6064

<!-- b000947 | prose | pages [22] -->
Adolph Rupp 0.5708

<!-- b000948 | prose | pages [22] -->
Rick Pitino 0.5166

<!-- b000949 | prose | pages [22] -->
Lute Olson 0.4604

<!-- b000950 | prose | pages [22] -->
Phog Allen 0.4354

<!-- b000951 | prose | pages [22] -->
Top10 Hit score 76.6

<!-- b000952 | prose | pages [22] -->
Top5 Hit score 85.47

<!-- b000953 | caption | pages [22] -->
Table 6.6 what is different in AM introducing time weight?

<!-- b000954 | prose | pages [22] -->
Conclusion:  The changes in rankings occur globally. The model appears to be easily

<!-- b000955 | prose | pages [22] -->
influenced by the time weights.  The performance for AM appears to be easily influenced by FSE because of the

<!-- b000956 | prose | pages [22] -->
weight distribution for the two models. Take Bob Knight for example, the following figure shows how evaluation grade changes in the two different situations:

<!-- b000957 | furniture | pages [22] -->


<!-- b000958 | caption | pages [22] -->
Figure 6.1 every year’s evaluation of Bob Knight

<!-- b000959 | furniture | pages [23] -->
Team#28414                                                             Page 23 of 33

<!-- b000960 | heading | pages [23] -->
6.2.3 What is the variation tendency?

<!-- b000961 | prose | pages [23] -->
From the results in section 6.2.2, variation tendency could be concluded as

<!-- b000962 | prose | pages [23] -->
follows:

<!-- b000963 | prose | pages [23] -->
 For coaches in earlier ages, their rankings will fall to some extent.

<!-- b000964 | prose | pages [23] -->
Take Phog Allen [21]for example, he is known as the "Father of Basketball

<!-- b000965 | prose | pages [23] -->
Coaching", but most of his games occurred in 1920-1959, which means that NCAA

<!-- b000966 | prose | pages [23] -->
had not started or though started the teams were few. The time weight for his age is

<!-- b000967 | prose | pages [23] -->
relatively low thus making the ranking fall.

<!-- b000968 | prose | pages [23] -->
 For coaches in recent years, they will enjoy some superiority.

<!-- b000969 | prose | pages [23] -->
Take Roy Williams [22]and Adolph Rupp [20]for example, the two coaches’

<!-- b000970 | prose | pages [23] -->
performance are quiet close to each other, Adolph Rupp was even better in in

<!-- b000971 | prose | pages [23] -->
historical record, but due to the time weight, the historical record for Adolph Rupp

<!-- b000972 | prose | pages [23] -->
does not count that much, and Roy Williams is ahead of him.

<!-- b000973 | prose | pages [23] -->
 Introducing time weights does not necessarily mean higher hit score.

<!-- b000974 | prose | pages [23] -->
In section V, We have stated that we choose some existed rankings as criterion,

<!-- b000975 | prose | pages [23] -->
but these rankings generally do not take coaching ages into consideration, moreover,

<!-- b000976 | prose | pages [23] -->
some authorities hold the viewpoints that the coaches in early ages are of more

<!-- b000977 | prose | pages [23] -->
authority, leading to the hit score falling.

<!-- b000978 | heading | pages [23] -->
6.3 Model also works in other sports

<!-- b000979 | prose | pages [23] -->
It obviously could not live up to our expectations if the model could only be used in

<!-- b000980 | prose | pages [23] -->
basketball. This chapter we will explain in detail how our models can be applied in

<!-- b000981 | prose | pages [23] -->
general across all possible sports.

<!-- b000982 | prose | pages [23] -->
There are mainly 4 steps to apply the model in any sport as you want.

<!-- b000983 | prose | pages [23] -->
 Step1: Adjust the metrics according to the feature of the sports.

<!-- b000984 | prose | pages [23] -->
Main differences are in the Playoff Performance, different sports may have

<!-- b000985 | prose | pages [23] -->
different playoff rules, so the metrics in this aspect should be adapted according to the

<!-- b000986 | prose | pages [23] -->
rule. Take football as example:

<!-- b000987 | prose | pages [23] -->
Metrics for 5-aspect norms

<!-- b000988 | prose | pages [23] -->
Metrics for

<!-- b000989 | prose | pages [23] -->
basketball

<!-- b000990 | prose | pages [23] -->
Historical record Wins

<!-- b000991 | prose | pages [23] -->
Losses

<!-- b000992 | prose | pages [23] -->
Gold content SRS

<!-- b000993 | prose | pages [23] -->
SOS

<!-- b000994 | prose | pages [23] -->
football

<!-- b000995 | prose | pages [23] -->
Wins

<!-- b000996 | prose | pages [23] -->
Losses

<!-- b000997 | prose | pages [23] -->
SRS

<!-- b000998 | prose | pages [23] -->
SOS

<!-- b000999 | furniture | pages [24] -->
Team#28414                                                             Page 24 of 33

<!-- b001000 | prose | pages [24] -->
First round

<!-- b001001 | furniture | pages [24] -->


<!-- b001002 | furniture | pages [24] -->


<!-- b001003 | prose | pages [24] -->
Fiesta Bowl

<!-- b001004 | prose | pages [24] -->
Second round

<!-- b001005 | furniture | pages [24] -->


<!-- b001006 | prose | pages [24] -->
Orange Bowl

<!-- b001007 | prose | pages [24] -->
Sweet sixteen

<!-- b001008 | prose | pages [24] -->
Playoff

<!-- b001009 | prose | pages [24] -->
Elite eight

<!-- b001010 | prose | pages [24] -->
Performance

<!-- b001011 | prose | pages [24] -->
Final four

<!-- b001012 | prose | pages [24] -->
Sugar Bowl

<!-- b001013 | prose | pages [24] -->
Rose Bowl

<!-- b001014 | prose | pages [24] -->
National

<!-- b001015 | prose | pages [24] -->
Championship

<!-- b001016 | prose | pages [24] -->
Runner-up

<!-- b001017 | prose | pages [24] -->
Champion

<!-- b001018 | prose | pages [24] -->
Honors Awards

<!-- b001019 | prose | pages [24] -->
Game

<!-- b001020 | prose | pages [24] -->
Non-BSC bowls

<!-- b001021 | prose | pages [24] -->
Awards

<!-- b001022 | prose | pages [24] -->
Star players

<!-- b001023 | prose | pages [24] -->
Contribution

<!-- b001024 | prose | pages [24] -->
to sports

<!-- b001025 | prose | pages [24] -->
Star players

<!-- b001026 | prose | pages [24] -->
Coaching ages Coaching ages

<!-- b001027 | prose | pages [24] -->
Tactical innovation Tactical innovation

<!-- b001028 | prose | pages [24] -->
International

<!-- b001029 | prose | pages [24] -->
Popularity

<!-- b001030 | prose | pages [24] -->
International

<!-- b001031 | prose | pages [24] -->
Popularity

<!-- b001032 | caption | pages [24] -->
Table 6.7 the metrics for college football

<!-- b001033 | prose | pages [24] -->
 Step2: Adapt the calculation rules according to the feature of the sports.

<!-- b001034 | prose | pages [24] -->
For example, the metrics for football in playoff performance have already changed,

<!-- b001035 | prose | pages [24] -->
each class of performance should be assigned another weight according to the gold

<!-- b001036 | prose | pages [24] -->
content of different bowls. At the same time, the awards and their weights under

<!-- b001037 | prose | pages [24] -->
consideration should also be adjusted for the “Honors” aspect.

<!-- b001038 | prose | pages [24] -->
 Step3: Adjust the time weight according to the history of the sport.

<!-- b001039 | prose | pages [24] -->
For example, as for football, before 2006, there are no BSC bowls. After 2006, 5

<!-- b001040 | prose | pages [24] -->
BSC bowls came into being, enjoying extremely high gold content.

<!-- b001041 | prose | pages [24] -->
 Step4: Solve the Aggregation model again and analyze the results.

<!-- b001042 | prose | pages [24] -->
The following figure shows the steps of applying the model into all possible sports:

<!-- b001043 | furniture | pages [25] -->
Team#28414                                                             Page 25 of 33

<!-- b001044 | prose | pages [25] -->
Start

<!-- b001045 | prose | pages [25] -->
Adjust the metrics

<!-- b001046 | prose | pages [25] -->
Adjust the calculation rules

<!-- b001047 | prose | pages [25] -->
Adjust time weights

<!-- b001048 | prose | pages [25] -->
Solve the model

<!-- b001049 | furniture | pages [25] -->


<!-- b001050 | caption | pages [25] -->
Figure 6.2 the flow chart of the four steps

<!-- b001051 | prose | pages [25] -->
Following the 4 steps presented above, we apply the model in other 2 different

<!-- b001052 | prose | pages [25] -->
sports: football and hockey.

<!-- b001053 | prose | pages [25] -->
Top5 for hockey Top5 for football  Grades Grades

<!-- b001054 | prose | pages [25] -->
Bob Johnson Bear Bryant 0.8874 0.8963

<!-- b001055 | prose | pages [25] -->
Red Berenson Knute Rockne 0.8664 0.8732

<!-- b001056 | prose | pages [25] -->
Jack Parker Tom Osborne 0.8538 0.8525

<!-- b001057 | prose | pages [25] -->
Jerry York Joe Paterno 0.7872 0.7756

<!-- b001058 | prose | pages [25] -->
Ron Mason Bobby Bowden 0.7864 0.7632

<!-- b001059 | caption | pages [25] -->
Table 6.8 the rankings for football & hockey

<!-- b001060 | heading | pages [25] -->
VII. Further discussion

<!-- b001061 | heading | pages [25] -->
7.1 Sensitivity Analysis on FSE

<!-- b001062 | heading | pages [25] -->
7.1.1 Vary Membership function

<!-- b001063 | prose | pages [25] -->
In FSE discussed in section 4.2, we choose (4.12) as the membership function.

<!-- b001064 | prose | pages [25] -->
But there are also other available membership functions. The following table shows

<!-- b001065 | prose | pages [25] -->
the membership functions that are taken into consideration in this part.

<!-- b001066 | furniture | pages [25] -->


<!-- b001067 | furniture | pages [26] -->
Team#28414                                                             Page 26 of 33

<!-- b001068 | prose | pages [26] -->
𝑋𝑋𝑖𝑖𝑖𝑖

<!-- b001069 | prose | pages [26] -->
Membership function Type

<!-- b001070 | prose | pages [26] -->
𝜇𝜇𝑗𝑗൫𝑋𝑋𝑖𝑖𝑖𝑖൯= ( 1

<!-- b001071 | prose | pages [26] -->
)𝑘𝑘

<!-- b001072 | prose | pages [26] -->
𝑋𝑋𝑗𝑗(𝑚𝑚𝑚𝑚𝑚𝑚)

<!-- b001073 | prose | pages [26] -->
𝑋𝑋𝑖𝑖𝑖𝑖−𝑋𝑋𝑗𝑗(𝑚𝑚𝑚𝑚𝑚𝑚) 𝜇𝜇𝑗𝑗൫𝑋𝑋𝑖𝑖𝑖𝑖൯= ( 2

<!-- b001074 | prose | pages [26] -->
)𝑘𝑘

<!-- b001075 | prose | pages [26] -->
𝑋𝑋𝑗𝑗(𝑚𝑚𝑚𝑚𝑚𝑚) −𝑋𝑋𝑗𝑗(𝑚𝑚𝑚𝑚𝑚𝑚)

<!-- b001076 | prose | pages [26] -->
𝜇𝜇𝑗𝑗൫𝑋𝑋𝑖𝑖𝑖𝑖൯= 1 −𝑒𝑒−𝑘𝑘(𝑋𝑋𝑖𝑖𝑖𝑖−𝑋𝑋𝑗𝑗(𝑚𝑚𝑚𝑚𝑚𝑚)) 3

<!-- b001077 | caption | pages [26] -->
Table 7.1 membership functions

<!-- b001078 | prose | pages [26] -->
 For type 1, we will analyze how the weight distribution (only for FSE) for different

<!-- b001079 | prose | pages [26] -->
aspects will change while varying k.

<!-- b001080 | furniture | pages [26] -->


<!-- b001081 | caption | pages [26] -->
Figure 7.1 the weight of each factor for each aspect

<!-- b001082 | prose | pages [26] -->
Conclusions:  Weight distribution is sensitive to the value of k and changes of weight distribution

<!-- b001083 | prose | pages [26] -->
 As the value of k increases, 𝑋𝑋1 and 𝑋𝑋2 tend to be less important but 𝑋𝑋3 and 𝑋𝑋5 can be seen clearly in Figure 7.1。

<!-- b001084 | prose | pages [26] -->
 When  1 ≤k ≤4, 𝑋𝑋3 and 𝑋𝑋5 have the highest weight, 𝑋𝑋1 and 𝑋𝑋2 have the tend to be more important.

<!-- b001085 | prose | pages [26] -->
lowest weight.

<!-- b001086 | prose | pages [26] -->
 For all three types, we will analyze how hit score (only for FSE) will change

<!-- b001087 | prose | pages [26] -->
varying k.

<!-- b001088 | furniture | pages [27] -->
Team#28414                                                             Page 27 of 33

<!-- b001089 | furniture | pages [27] -->


<!-- b001090 | caption | pages [27] -->
Figure 7.2 sensitivity analysis on k for FSE

<!-- b001091 | prose | pages [27] -->
Conclusions:  Membership function 1 and member function 2 are sensitive to the value of k,

<!-- b001092 | prose | pages [27] -->
while membership function 3 is not sensitive to the value of k.  Membership function 1 reaches its maximum value at k = 3; membership function

<!-- b001093 | prose | pages [27] -->
2 reaches its maximum value at k = 2.  Obviously, membership function1 and membership function 2 perform much

<!-- b001094 | prose | pages [27] -->
better than membership function 3. And membership function 3 is not suitable for our model.  For best results, membership function1 with k = 3 is most appropriate in this

<!-- b001095 | prose | pages [27] -->
model.

<!-- b001096 | heading | pages [27] -->
7.1.2 Vary calculation rule

<!-- b001097 | prose | pages [27] -->
𝜆𝜆𝑤𝑤𝑤𝑤𝑤𝑤 𝜆𝜆𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝑙.

<!-- b001098 | furniture | pages [27] -->


<!-- b001099 | prose | pages [27] -->
Here we focus on figuring out how hit score will change to the ratio

<!-- b001100 | furniture | pages [27] -->


<!-- b001101 | caption | pages [27] -->
Figure 7.3 sensitivity analysis to the weight of win and lose

<!-- b001102 | furniture | pages [28] -->
Team#28414                                                             Page 28 of 33

<!-- b001103 | prose | pages [28] -->
Conclusions:  Model performs best when the weight of winning a game is two times as much as

<!-- b001104 | prose | pages [28] -->
losing a game.  If we attach the same weight to winning a game and losing a game, the model will

<!-- b001105 | prose | pages [28] -->
have a poor hit score. And if the ratio of the weight of wins and loses is too high, it will also lead to a bad result.

<!-- b001106 | heading | pages [28] -->
7.2 Sensitivity Analysis on Aggregation weight

<!-- b001107 | prose | pages [28] -->
varying the weight for AHP (𝑊𝑊1).

<!-- b001108 | prose | pages [28] -->
In this part, we will analyze how hit score (For AM) and rankings will change while

<!-- b001109 | furniture | pages [28] -->


<!-- b001110 | furniture | pages [28] -->


<!-- b001111 | caption | pages [28] -->
Figure 7.4 && 7.5

<!-- b001112 | furniture | pages [29] -->
Team#28414                                                             Page 29 of 33

<!-- b001113 | prose | pages [29] -->
Conclusion:  As the weight of AHP increases, the rank list will change. The rank of Dean Smith

<!-- b001114 | prose | pages [29] -->
and Bob knight tend to decline and the rank of Jim Boeheim tend to rise.  Since AHP is less accurate than FSE, hit score of AM would be optimal when the

<!-- b001115 | prose | pages [29] -->
weight of AHP is small. But when the weight of AHP is zero, hit score doesn’t reach the maximum. The maximum hit score is reached when the weight of AHP is 0.1-0.2.  It proves that AM can perform well than either AHP or FSE.

<!-- b001116 | heading | pages [29] -->
7.3 Exploration: Evaluating Best President

<!-- b001117 | prose | pages [29] -->
Now we use our models to find the top ten presidents of the United States. We

<!-- b001118 | prose | pages [29] -->
choose the 43 men who have been president of USA, and collect relative data from

<!-- b001119 | prose | pages [29] -->
the internet [24].

<!-- b001120 | prose | pages [29] -->
A president can be evaluated also from following five aspects: personal qualities,

<!-- b001121 | prose | pages [29] -->
presidential achievements, leadership qualities, failures and faults, and popular

<!-- b001122 | prose | pages [29] -->
opinion:

<!-- b001123 | furniture | pages [29] -->


<!-- b001124 | caption | pages [29] -->
Figure 7.6 5-aspect norm of president of USA

<!-- b001125 | prose | pages [29] -->
The personal qualities includes imagination, intelligence and being willing to

<!-- b001126 | prose | pages [29] -->
take risks, while the presidential achievements can be valued with ability of

<!-- b001127 | prose | pages [29] -->
domestic accomplishments, executive appointments, foreign policy accomplishments,

<!-- b001128 | prose | pages [29] -->
and ability of compromise. And the leadership qualities can be measured by party

<!-- b001129 | prose | pages [29] -->
leadership ability and relations with congress. We also take popular opinion into

<!-- b001130 | prose | pages [29] -->
consideration, and we gather votes from different polls, such as C-SPAN poll, ABC

<!-- b001131 | prose | pages [29] -->
News poll, Washington College poll, Gallup poll, Rasmussen poll, and 2012 Gallup

<!-- b001132 | prose | pages [29] -->
poll. The ranking of presidents of the United States is shown in following table.

<!-- b001133 | prose | pages [29] -->
Rank Name

<!-- b001134 | prose | pages [29] -->
Abraham Lincoln 1

<!-- b001135 | prose | pages [29] -->
George Washington 2

<!-- b001136 | prose | pages [29] -->
Rank Name

<!-- b001137 | prose | pages [29] -->
Harry S. Truman 6

<!-- b001138 | prose | pages [29] -->
Woodrow Wilson 7

<!-- b001139 | furniture | pages [30] -->
Team#28414                                                             Page 30 of 33

<!-- b001140 | prose | pages [30] -->
Franklin D. Roosevelt 3

<!-- b001141 | prose | pages [30] -->
Thomas Jefferson 4

<!-- b001142 | prose | pages [30] -->
Theodore Roosevelt 5

<!-- b001143 | prose | pages [30] -->
Dwight D. Eisenhower 8

<!-- b001144 | prose | pages [30] -->
James K. Polk 9

<!-- b001145 | prose | pages [30] -->
Andrew Jackson 10

<!-- b001146 | caption | pages [30] -->
Table 7.2 the ranking of presidents of the United States

<!-- b001147 | heading | pages [30] -->
VIII. Strength and Weakness

<!-- b001148 | prose | pages [30] -->
Strength:

<!-- b001149 | prose | pages [30] -->
 When we articulate our own metrics for assessment, we try our best to include all

<!-- b001150 | prose | pages [30] -->
the important elements of a coach to make the ranking more accurate. Time factor,

<!-- b001151 | prose | pages [30] -->
gender, category are all discussed in the model.

<!-- b001152 | prose | pages [30] -->
 We evaluate the performance of a coach from 5 specific perspectives.

<!-- b001153 | prose | pages [30] -->
 We set up two different models to form an aggregation model. AHP includes more

<!-- b001154 | prose | pages [30] -->
subjective factors while FSE appears to be more objective. The aggregation

<!-- b001155 | prose | pages [30] -->
model is devoted to make clear the tradeoff between the two sides.

<!-- b001156 | prose | pages [30] -->
 We states a distinct quantification system which is expected to live up to the

<!-- b001157 | prose | pages [30] -->
common sense.

<!-- b001158 | prose | pages [30] -->
Weakness:

<!-- b001159 | prose | pages [30] -->
 We adopt totally eighteen indicators to evaluate a coach, namely not all elements

<!-- b001160 | prose | pages [30] -->
is under consideration.

<!-- b001161 | prose | pages [30] -->
 Weights are everywhere in the model, but some weight assignments might not be

<!-- b001162 | prose | pages [30] -->
the best scheme.

<!-- b001163 | heading | pages [30] -->
IX. Non-technical Explanation

<!-- b001164 | prose | pages [30] -->
For better or worse, coaches are often the faces of college sports programs.

<!-- b001165 | prose | pages [30] -->
Different from players who stay only for a few years, coaches can exert longer

<!-- b001166 | prose | pages [30] -->
influence in the college games. Here is a list of the top 5 coaches in the college

<!-- b001167 | prose | pages [30] -->
basketball, college football, and college hockey.

<!-- b001168 | furniture | pages [30] -->


<!-- b001169 | furniture | pages [30] -->


<!-- b001170 | prose | pages [30] -->
college football Rank college basketball

<!-- b001171 | prose | pages [30] -->
1

<!-- b001172 | furniture | pages [30] -->


<!-- b001173 | furniture | pages [30] -->


<!-- b001174 | furniture | pages [30] -->


<!-- b001175 | prose | pages [30] -->
John Wooden

<!-- b001176 | prose | pages [30] -->
college hockey

<!-- b001177 | furniture | pages [30] -->


<!-- b001178 | furniture | pages [30] -->


<!-- b001179 | furniture | pages [30] -->


<!-- b001180 | furniture | pages [30] -->


<!-- b001181 | furniture | pages [30] -->


<!-- b001182 | furniture | pages [30] -->


<!-- b001183 | prose | pages [30] -->
Bear Bryant

<!-- b001184 | prose | pages [30] -->
Bob Johnson

<!-- b001185 | furniture | pages [31] -->
Team#28414                                                             Page 31 of 33

<!-- b001186 | prose | pages [31] -->
2

<!-- b001187 | furniture | pages [31] -->


<!-- b001188 | furniture | pages [31] -->


<!-- b001189 | furniture | pages [31] -->


<!-- b001190 | prose | pages [31] -->
Mike Krzyzewski

<!-- b001191 | furniture | pages [31] -->


<!-- b001192 | furniture | pages [31] -->


<!-- b001193 | furniture | pages [31] -->


<!-- b001194 | furniture | pages [31] -->


<!-- b001195 | furniture | pages [31] -->


<!-- b001196 | furniture | pages [31] -->


<!-- b001197 | prose | pages [31] -->
Knute Rockne

<!-- b001198 | furniture | pages [31] -->


<!-- b001199 | prose | pages [31] -->
3

<!-- b001200 | furniture | pages [31] -->


<!-- b001201 | furniture | pages [31] -->


<!-- b001202 | prose | pages [31] -->
Red Berenson

<!-- b001203 | furniture | pages [31] -->


<!-- b001204 | furniture | pages [31] -->


<!-- b001205 | furniture | pages [31] -->


<!-- b001206 | furniture | pages [31] -->


<!-- b001207 | furniture | pages [31] -->


<!-- b001208 | furniture | pages [31] -->


<!-- b001209 | prose | pages [31] -->
Tom Osborne

<!-- b001210 | prose | pages [31] -->
Adolph Rupp

<!-- b001211 | furniture | pages [31] -->


<!-- b001212 | prose | pages [31] -->
4

<!-- b001213 | furniture | pages [31] -->


<!-- b001214 | furniture | pages [31] -->


<!-- b001215 | prose | pages [31] -->
Dean Smith

<!-- b001216 | prose | pages [31] -->
Jack Parker

<!-- b001217 | furniture | pages [31] -->


<!-- b001218 | furniture | pages [31] -->


<!-- b001219 | furniture | pages [31] -->


<!-- b001220 | furniture | pages [31] -->


<!-- b001221 | furniture | pages [31] -->


<!-- b001222 | furniture | pages [31] -->


<!-- b001223 | prose | pages [31] -->
Joe Paterno

<!-- b001224 | furniture | pages [31] -->


<!-- b001225 | prose | pages [31] -->
5

<!-- b001226 | furniture | pages [31] -->


<!-- b001227 | furniture | pages [31] -->


<!-- b001228 | prose | pages [31] -->
Jerry York

<!-- b001229 | furniture | pages [31] -->


<!-- b001230 | furniture | pages [31] -->


<!-- b001231 | furniture | pages [31] -->


<!-- b001232 | furniture | pages [31] -->


<!-- b001233 | furniture | pages [31] -->


<!-- b001234 | furniture | pages [31] -->


<!-- b001235 | prose | pages [31] -->
Bobby Bowden

<!-- b001236 | prose | pages [31] -->
Bob Knight

<!-- b001237 | prose | pages [31] -->
Ron Mason

<!-- b001238 | prose | pages [31] -->
The rankings proved to be a difficult task and job of a college coach is

<!-- b001239 | furniture | pages [31] -->


<!-- b001240 | prose | pages [31] -->
multifaceted. Firstly, we choose some coaches, who are in the list of Hall of Fame, or

<!-- b001241 | prose | pages [31] -->
people who have established outstanding traditions and earned many awards, as our

<!-- b001242 | prose | pages [31] -->
ranking candidates. Then, searching from the internet or other data sources, we try to

<!-- b001243 | prose | pages [31] -->
collect relative data as detailed as possible. After choosing proper data, college

<!-- b001244 | prose | pages [31] -->
coaches’ rankings can be obtained. What’s more, we search the existing rankings

<!-- b001245 | prose | pages [31] -->
from the internet to serve as the evaluation criterion.

<!-- b001246 | prose | pages [31] -->
During the procedure of choosing data, we evaluate the coaches in our list of

<!-- b001247 | furniture | pages [31] -->


<!-- b001248 | prose | pages [31] -->
candidates from five aspects. As is known to all, the best college coaches tend to

<!-- b001249 | prose | pages [31] -->
have good team’s historical record, such as more wins and high win rate. What’s more,

<!-- b001250 | prose | pages [31] -->
SRS (Simple Rating System) and SOS (Strength of Schedule) can reflect the

<!-- b001251 | prose | pages [31] -->
coaching ability. We also examined each coach’s success in the postseason. Taking

<!-- b001252 | prose | pages [31] -->
basketball as an example, the performance could be valued by counting the number

<!-- b001253 | prose | pages [31] -->
of times for “Champion”, “Runner-up”, “Final Four”, “Sweet Sixteen”, “Second Round”,

<!-- b001254 | prose | pages [31] -->
and “First Round”. In many case, we take into account coaches’ contribution to the

<!-- b001255 | prose | pages [31] -->
sports and honors, such as various awards in their field or putting their name in the

<!-- b001256 | prose | pages [31] -->
“Hall of Fame”.

<!-- b001257 | prose | pages [31] -->
After collecting and choosing coaches’ detailed data, we define the importance of

<!-- b001258 | furniture | pages [31] -->


<!-- b001259 | furniture | pages [32] -->
Team#28414                                                             Page 32 of 33

<!-- b001260 | prose | pages [32] -->
those aspects which can measure coaches’ ability, and use the results to give each

<!-- b001261 | prose | pages [32] -->
coach a score. The higher the coaches’ scored on the relative aspects, the better their

<!-- b001262 | prose | pages [32] -->
position on the ranking.

<!-- b001263 | furniture | pages [32] -->


<!-- b001264 | prose | pages [32] -->
We use the data of the best college basketball coach–John Wooden to give some

<!-- b001265 | prose | pages [32] -->
example. In his college basketball coach career, his team had won 826 games, and

<!-- b001266 | prose | pages [32] -->
during his sixteen years NCAA tournament, he won ten championships and twelve

<!-- b001267 | prose | pages [32] -->
straight trips to Final Fours. John Wooden has been recognized tremendous times for

<!-- b001268 | prose | pages [32] -->
his achievements and created longer legacies in the college basketball games.

<!-- b001269 | prose | pages [32] -->
Besides his fantastic and glory record, Wooden was recognized for his impact on

<!-- b001270 | prose | pages [32] -->
college basketball as a member of the founding class of the National Collegiate

<!-- b001271 | prose | pages [32] -->
Basketball Hall of Fame and was named The Sporting News "Greatest Coach of All

<!-- b001272 | prose | pages [32] -->
Time" [23]. With so many honors and awards which can’t be listed in detail there, John

<!-- b001273 | prose | pages [32] -->
gets the highest score when we rank the coaches and is worthy the title of the best

<!-- b001274 | prose | pages [32] -->
college basketball coach.

<!-- b001275 | heading | pages [32] -->
X. Future work

<!-- b001276 | prose | pages [32] -->
 Consider all possible sports coaches together, and make a college coaches

<!-- b001277 | prose | pages [32] -->
rankings, regardless of what kind of sports coaches they are.

<!-- b001278 | prose | pages [32] -->
 Take other relevant coach information into consideration, because research

<!-- b001279 | prose | pages [32] -->
suggests that characteristics of the coaches, such as the breadth of coaches’

<!-- b001280 | prose | pages [32] -->
knowledge, authority, the ability of searching and cultivating talents, and attention

<!-- b001281 | prose | pages [32] -->
to details, play a role in determining the best college coaches.

<!-- b001282 | prose | pages [32] -->
 Develop a general method to rank everything when there is one way to quantify.

<!-- b001283 | heading | pages [32] -->
XI. References

<!-- b001284 | references | pages [32] -->
[1] http://en.wikipedia.org/wiki/Sports_Illustrated

<!-- b001285 | references | pages [32] -->
[2] http://collegebasketball.rivals.com/viewcbse.asp?selposition=9

<!-- b001286 | references | pages [32] -->
[3] Saaty, Thomas L.; Peniwati, Kirti (2008). Group Decision Making: Drawing out and

<!-- b001287 | references | pages [32] -->
Reconciling Differences. Pittsburgh, Pennsylvania: RWS Publications. ISBN

<!-- b001288 | references | pages [32] -->
978-1-888603-08-8.

<!-- b001289 | references | pages [32] -->
[4] http://en.wikipedia.org/wiki/Analytic_hierarchy_process

<!-- b001290 | references | pages [32] -->
[5] http://en.wikipedia.org/wiki/Fuzzy_mathematics

<!-- b001291 | references | pages [32] -->
[6] Zadeh, L. A. (1965) "Fuzzy sets", Information and Control, 8, 338–353

<!-- b001292 | references | pages [32] -->
[7] http://en.wikipedia.org/wiki/National_Collegiate_Basketball_Hall_of_Fame

<!-- b001293 | furniture | pages [33] -->
Team#28414                                                             Page 33 of 33

<!-- b001294 | references | pages [33] -->
[8] http://www.sports-reference.com/cbb/coaches/

<!-- b001295 | references | pages [33] -->
[9] http://www.sportingcharts.com/

<!-- b001296 | references | pages [33] -->
[10] http://en.wikipedia.org/wiki/Strength_of_schedule

<!-- b001297 | references | pages [33] -->
[11] http://en.wikipedia.org/wiki/Playoffs

<!-- b001298 | references | pages [33] -->
[12] http://en.wikipedia.org/wiki/NCAA_Men's_Division_I_Basketball_Championship

<!-- b001299 | references | pages [33] -->
[13] Dahiya S, Singh B, Gaur S, et al. Analysis of groundwater quality using fuzzy

<!-- b001300 | references | pages [33] -->
synthetic evaluation[J]. Journal of Hazardous Materials, 2007, 147(3): 938-946

<!-- b001301 | references | pages [33] -->
[14]http://en.wikipedia.org/wiki/College_basketball.

<!-- b001302 | references | pages [33] -->
[15]http://sports.espn.go.com/espn/page2/story?page=list/050304/collegehoopscoac

<!-- b001303 | references | pages [33] -->
hes

<!-- b001304 | references | pages [33] -->
[16] http://sports.yahoo.com/ncaa/basketball/news?slug=ycn-7791514

<!-- b001305 | references | pages [33] -->
[17]http://www.sportingnews.com/ncaa-basketball/story/2009-07-29/sporting-news-50

<!-- b001306 | references | pages [33] -->
-greatest-coaches-all-time

<!-- b001307 | references | pages [33] -->
[18]http://en.wikipedia.org/wiki/List_of_college_women's_basketball_coaches_with_6

<!-- b001308 | references | pages [33] -->
00_wins

<!-- b001309 | references | pages [33] -->
[19] http://sports.yahoo.com/ncaa/football/news?slug=ac-7168152

<!-- b001310 | references | pages [33] -->
[20] http://en.wikipedia.org/wiki/Adolph_Rupp

<!-- b001311 | references | pages [33] -->
[21] http://en.wikipedia.org/wiki/Phog_Allen

<!-- b001312 | references | pages [33] -->
[22] http://en.wikipedia.org/wiki/Roy_Williams

<!-- b001313 | references | pages [33] -->
[23]http://en.wikipedia.org/wiki/Historical_rankings_of_Presidents_of_the_United_Sta

<!-- b001314 | references | pages [33] -->
tes

<!-- b001315 | references | pages [33] -->
[24] "Sporting News honors Wooden". ESPN. Associated Press. 30 July 2009.

<!-- b001316 | references | pages [33] -->
Retrieved 7 June 2010.
