# P-B-2014-28875-728f6f07

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | title | pages [1] -->
28875

<!-- b000003 | prose | pages [1] -->
For office use only

<!-- b000004 | prose | pages [1] -->
T1 ________________

<!-- b000005 | prose | pages [1] -->
T2 ________________

<!-- b000006 | furniture | pages [1] -->


<!-- b000007 | prose | pages [1] -->
T3 ________________

<!-- b000008 | prose | pages [1] -->
For office use only

<!-- b000009 | prose | pages [1] -->
F1 ________________

<!-- b000010 | prose | pages [1] -->
F2 ________________

<!-- b000011 | prose | pages [1] -->
F3 ________________

<!-- b000012 | prose | pages [1] -->
Problem Chosen

<!-- b000013 | prose | pages [1] -->
T4 ________________

<!-- b000014 | furniture | pages [1] -->


<!-- b000015 | prose | pages [1] -->
F4 ________________

<!-- b000016 | title | pages [1] -->
B

<!-- b000017 | furniture | pages [1] -->


<!-- b000018 | furniture | pages [1] -->


<!-- b000019 | heading | pages [1] -->
2014 Mathematical Contest in Modeling (MCM) Summary Sheet

<!-- b000020 | heading | pages [1] -->
Summary

<!-- b000021 | prose | pages [1] -->
Our goal is a model that finding out the “best all time college coach”. This is crucial to the promotion of the college coaching. Evaluation methods must reflect the practical training level and ability scientific, accurate, comprehensive and objectively. In our paper, to guarantee the fair and equitable of the selection results, comprehensively considered coaches coaching skills, experience, team management and his/her team performance and other aspects of teaching. Determine the metrics such as Games, Winning percentage, Championships, etc. for assessment. Then build a fuzzy comprehensive evaluation model based on improved analytic hierarchy process named IAHP-FCE model to find out The Best All Time College Coach for Sports Illustrated.

<!-- b000022 | prose | pages [1] -->
First of all, we applied the analytic hierarchy process (AHP) and fuzzy comprehensive evaluation method (FCE). Standardized the metrics data we collected by eliminate the effects of dimension. And calculate the relative membership degrees among the metrics. Then according to the fuzzy evaluation matrix constructed by the single metrics relative membership degree, built the modification of judgment matrix in the AHP. Secondly, calculated the weights of each metrics based on the reciprocity of judgment matrix. And carry on the consistency check using the single target linear programming to calculate the consistency index coefficient by Lingo7.0. Thirdly, build a fuzzy comprehensive evaluation model based on Analytic Hierarchy Process named AHP-FCE modelⅠ. Using modelⅠwe can obtain the composite score of each coach. Take NCAA Basketball to test the modelⅠ. Finally, we got the Top 5. Compare with the Authority Top 5 coaches, the accuracy of modelⅠ is 80%. To achieve our goal, we need get a higher Accuracy, so we decided to improve the model by introduced the Classification thought to decompose the metrics into 2 levels. Based on the modelⅠ and combined the new Classification, we built a simplified calculation and higher accuracy modelⅡ named IAHP-FCE modelⅡ. Then also take NCAA Basketball to rank the Top 5, followed by Mike Krzyzewski、Dean Smith、 John Wooden、Bob Knight and Roy Williams. Contrast with the Authority Ranking, the modelⅡ is correct almost 100%. So modelⅡ got a great improvement.

<!-- b000023 | prose | pages [2] -->
As to popularize the model to all possible sports, only need input the metrics data and get the weights, then you can rank the coaches across all possible sports. We applied the model in NCAA Football and Baseball, then got the both rank Top 5 coaches, balance the two Authority ranks, we also gets the high accuracy. So the model we improved can apply in general across all possible sports. For apply the model across both genders, we use the model to calculate the female coach Ranking of NCAA Female Basketball and list their Top 5. Contrast with the official rank, the result is almost perfect. Fully verified the model can apply across both genders. Ranking the final composite score of males and females coach’s which from the three biggest NCAA League. We ultimately find out The Best All Time College Coach----Pat Summitt, winning eight NCAA national championships, and she is the only coach in NCAA history, and one of three college coaches overall, with at least 1,000 victories.

<!-- b000024 | prose | pages [2] -->
In order to clearly articulate the difference which time line horizon, we randomly select multiple coaches from different gender and sports fields. Using the modelⅡ to work out the coach’s each year composite score separately. Draw the line chart with their coaching score and coaching years. Then contrast individually between the same fields and different sex, between the different fields and same sex, between the same fields and same sex, finally we got the conclusion that with the rise of the time line horizon, the coaching score always ups and downs within a certain range. In general, their coaching score ups gradually with the growth of his/her coaching years. What’s more, we tested the model from four aspects, Dimensional consistency test, Model and model results deviation test, assumptions reasonableness test and Sensitivity analysis of the model parameters. Eventually the change threshold average interval of evaluation metrics in sensitivity analysis is 0.0297, less than 10%, all the test results indicate that the model we built is qualified.

<!-- b000025 | heading | pages [2] -->
In summary, the IAHP-FCE model we improved achieved our goal. That is

<!-- b000026 | prose | pages [2] -->
simplified calculation, accurate results and wide utility. It can be applied in general across both genders and all possible sports. In the long run, this model can be used for solving those practical problems in our daily life, for example the housing choice, the investment risk evaluation and tourism plan, etc.

<!-- b000027 | furniture | pages [2] -->


<!-- b000028 | furniture | pages [3] -->
Team#28875                                                                      Page 1 of 33

<!-- b000029 | prose | pages [3] -->
Finding Out The Best All Time College Coach

<!-- b000030 | heading | pages [3] -->
Abstract

<!-- b000031 | prose | pages [3] -->
Finding out the “Best All Time College Coach” is crucial to the promotion of the college coaching. We build a fuzzy comprehensive evaluation model based on improved analytic hierarchy process named IAHP-FCE model to find out The Best All Time College Coach for Sports Illustrated.

<!-- b000032 | prose | pages [3] -->
First of all, we applied the content analysis and bibliometrics method to determine the metrics such as games, winning percentage, championships, etc. for assessment. And standardized the metrics data by eliminate the effects of dimension. Then build a

<!-- b000033 | heading | pages [3] -->
fuzzy comprehensive evaluation model based on analytic hierarchy process named

<!-- b000034 | prose | pages [3] -->
AHP-FCE modelⅠ. Take NCAA Basketball to testing. Finally, we got the Top 5. Compare with the authority Top 5 coaches, the accuracy of modelⅠ is 80%. For the sake of a less calculation and higher accuracy model, we improved the model by introduced the classification thought to decompose the metrics into 2 levels. Then obtain the IAHP-FCE modelⅡ. Then also take NCAA Basketball to rank the Top 5, Mike Krzyzewski、Dean Smith、John Wooden、Bob Knight and Roy Williams. Contrast with the authority ranking, the accuracy of modelⅡ is 100%. So the modelⅡ gets a higher accuracy. Input the metrics data and get the weights, we obtained each the coaches Top 5 in NCAA Football, Baseball and Woman’s Basketball. Balance the official ranks, the result is almost perfect. Fully verified the model can applied in general across all possible sports and both genders.

<!-- b000035 | prose | pages [3] -->
Ranking all the coaches composite scores, finally find out The Best All Time College Coach. She is Pat Summitt, winning eight NCAA national championships.

<!-- b000036 | prose | pages [3] -->
Next, we contrast the line chart individually between the same fields and different sex, between the different fields and same sex, between the same fields and same sex, finally got the conclusion that with the rise of the time line horizon, the coaching scores always ups and downs within a certain range. In general, their coaching score ups gradually with the growth of his/her coaching years.

<!-- b000037 | prose | pages [3] -->
What’s more, we tested the model from four aspects, eventually the change threshold average interval of evaluation metrics in sensitivity analysis is 0.0297, all the test results indicate that the model we built is qualified.

<!-- b000038 | prose | pages [3] -->
On the whole, the IAHP-FCE model is simplify calculation, accurate results and wide utility, can be used for housing choice, the investment risk evaluation and tourism plan, etc.

<!-- b000039 | furniture | pages [3] -->


<!-- b000040 | keywords | pages [3] -->
Keywords:  The Best College Coach   Analytic hierarchy process

<!-- b000041 | prose | pages [3] -->
Fuzzy comprehensive evaluation method   Sensitivity analysis

<!-- b000042 | furniture | pages [3] -->


<!-- b000043 | furniture | pages [3] -->


<!-- b000044 | furniture | pages [3] -->


<!-- b000045 | furniture | pages [3] -->


<!-- b000046 | prose | pages [3] -->
1

<!-- b000047 | furniture | pages [4] -->
Team#28875                                                                      Page 2 of 33

<!-- b000048 | heading | pages [4] -->
Introduction

<!-- b000049 | prose | pages [4] -->
Sports Illustrated, a magazine for sports enthusiasts, is an American sports media franchise owned by media conglomerate Time Warner. Its self titled magazine has over 3.5 million subscribers and is read by 23 million adults each week, including over 18 million men. [1]And now, Sports Illustrated is looking for the “best all time college coach” male or female for the previous century.

<!-- b000050 | prose | pages [4] -->
Restatement of the Problem

<!-- b000051 | prose | pages [4] -->
The problem needs us to build a mathematical model to finding out the best all time college coach. We need consider the following.

<!-- b000052 | prose | pages [4] -->
 Build a mathematical model to choose the best college coach or coaches (past or

<!-- b000053 | prose | pages [4] -->
present) from among either male or female coaches in such sports as college hockey or field hockey, football, baseball or softball, basketball, or soccer.

<!-- b000054 | prose | pages [4] -->
 Does it make a difference which time line horizon that you use in your analysis,

<!-- b000055 | prose | pages [4] -->
i.e., does coaching in 1913 differ from coaching in 2013? Clearly articulate your metrics for assessment.

<!-- b000056 | prose | pages [4] -->
 Discuss how your model can be applied in general across both genders and all

<!-- b000057 | prose | pages [4] -->
possible sports. Present your model’s top 5 coaches in each of 3 different sports.

<!-- b000058 | prose | pages [4] -->
 In addition, prepare a 1-2 page article for Sports Illustrated that explains your

<!-- b000059 | prose | pages [4] -->
results and includes a non-technical explanation of your mathematical model that sports fans will understand.

<!-- b000060 | prose | pages [4] -->
Literature Review

<!-- b000061 | prose | pages [4] -->
There are many Evaluation methods of Coaching all over the world, which include Peer Review, Questionnaire Survey, Bibliometrics method, Analytic Hierarchy Process and Fuzzy Comprehensive Evaluation Method etc. Each method has a certain scope and limitations. On the evaluation, there is no universal method. In practice, evaluators often choose different methods for different purposes and objects. They can also be applied to the different stages of a comprehensive evaluation. Here makes a brief introduction on the application of the various evaluation methods.  Peer Review: It is a process used for checking the work performed by one's

<!-- b000062 | prose | pages [4] -->
equals (peers) to ensure it meets specific criteria. Peer review is used in working groups for many professional occupations because it is thought that peers can identify each other's errors quickly and easily, speeding up the time that it takes for mistakes to be identified and corrected. [2]Peer review has its strengths, Wide

<!-- b000063 | prose | pages [4] -->
range of applications and performance well. [3]But it also has shortcomings，owing

<!-- b000064 | prose | pages [4] -->
to the professional restrictions, different expert evaluate the same person might come to different conclusions, and peer review probably form a network of

<!-- b000065 | furniture | pages [4] -->


<!-- b000066 | prose | pages [4] -->
2

<!-- b000067 | furniture | pages [5] -->
Team#28875                                                                      Page 3 of 33

<!-- b000068 | prose | pages [5] -->
acquaintances. Peer review may appear Matthew Effect, heavy subjectivity and short of fairness. [4]

<!-- b000069 | prose | pages [5] -->
 Questionnaire Survey: A research instrument consisting of a series of questions

<!-- b000070 | prose | pages [5] -->
and other prompts for the purpose of gathering information from respondents. Although they are often designed for statistical analysis of the responses, this is not always the case. The questionnaire was invented by Sir Francis Galton. [5] Strengths: Save time, money and manpower, easy to quantify、statistics and analysis the survey results, and large-scale surveys. But the Survey design is difficult, the survey results is wide rather than deep, and difficult to guarantee the recoveries of the survey. [6]

<!-- b000071 | prose | pages [5] -->
 Content analysis and Bibliometrics [7]: In intelligence analysis method, content

<!-- b000072 | prose | pages [5] -->
analysis is a qualitative analysis method based on quantitative analysis, and bibliometrics is a famous quantitative analysis method. They have their respective merit or limit. At present, most intelligence studying works only adopt single method. So there are a lot of abut and limits in analysis procedure. In order to conquer those weaknesses, we must combine quantitative analysis method and qualitative analysis method, and apply them in the intelligence studying works to promote the efficiency of intelligence studying works and the reliability and veracity of analysis result. [8]

<!-- b000073 | prose | pages [5] -->
Because of those methods above all have their respective merit or limits. We searched more information, and finally we got our method.

<!-- b000074 | prose | pages [5] -->
Our Approach

<!-- b000075 | prose | pages [5] -->
We analyzed the problems above and consulted lots of literature, and then come up with the following approaches.

<!-- b000076 | prose | pages [5] -->
[9] is a structured technique for

<!-- b000077 | prose | pages [5] -->
 Analytic Hierarchy Process (AHP): AHP

<!-- b000078 | prose | pages [5] -->
organizing and analyzing complex decisions, based on mathematics and psychology. It was developed by Thomas L. Saaty in the 1970s and has been extensively studied and refined since then It has particular application. In group

<!-- b000079 | prose | pages [5] -->
[10], and is used around the world in a wide variety of decision

<!-- b000080 | prose | pages [5] -->
decision making

<!-- b000081 | prose | pages [5] -->
situations, in fields such as government, business, industry, healthcare, and education. Rather than prescribing a "correct" decision, the AHP helps decision makers find one that best suits their goal and their understanding of the problem. It provides a comprehensive and rational framework for structuring a decision problem, for representing and quantifying its elements, for relating those

<!-- b000082 | prose | pages [5] -->
[11]

<!-- b000083 | prose | pages [5] -->
elements to overall goals, and for evaluating alternative solutions.

<!-- b000084 | prose | pages [5] -->
 Fuzzy Comprehensive Evaluation Method (FCE): FCE is a comprehensive

<!-- b000085 | prose | pages [5] -->
evaluation method based on fuzzy mathematics. The comprehensive evaluation method based on the theory of fuzzy mathematics degree of membership of the

<!-- b000086 | furniture | pages [5] -->


<!-- b000087 | prose | pages [5] -->
3

<!-- b000088 | furniture | pages [6] -->
Team#28875                                                                      Page 4 of 33

<!-- b000089 | prose | pages [6] -->
qualitative evaluation into quantitative evaluation, which uses fuzzy mathematics subject to many factors thing or object to make an overall assessment. It has a clear result, systematic and strong features can solve vague, difficult to quantify the problem, suitable for solving the problem of non-deterministic. [13] The evaluation result is represented by a fuzzy set, closely combined with Qualitative description and Quantitative Analysis. [14]

<!-- b000090 | prose | pages [6] -->
In this paper, we integrated with the AHP and FCE, obtained the fuzzy comprehensive evaluation model based on analytic hierarchy process (AHP-FCE). Using the AHP-FCE model, we can get the rank of the coaches for several sports.

<!-- b000091 | heading | pages [6] -->
General Assumption

<!-- b000092 | prose | pages [6] -->
We make the following assumptions about the whole process in this paper to obtain a better model result.

<!-- b000093 | prose | pages [6] -->
About the Coach

<!-- b000094 | prose | pages [6] -->
 We choose almost 200 coaches from different sports according to him or her

<!-- b000095 | prose | pages [6] -->
career achievement.  Assuming the coaches which we searched their data all is the leader of their sport,

<!-- b000096 | prose | pages [6] -->
the best college coach produces from here.  The Best all time coach is come from the three biggest NCAA league of

<!-- b000097 | prose | pages [6] -->
Basketball, Football and baseball.

<!-- b000098 | prose | pages [6] -->
About the Data

<!-- b000099 | prose | pages [6] -->
 Assuming the data we searched on the internet all is true and reliable.

<!-- b000100 | prose | pages [6] -->
 Statistical processing and Data calculation didn’t produce mistake, and the results

<!-- b000101 | prose | pages [6] -->
are trustworthy.

<!-- b000102 | prose | pages [6] -->
About the Metrics

<!-- b000103 | prose | pages [6] -->
 Searching a large literature and using a variety of methods, we assuming that the

<!-- b000104 | prose | pages [6] -->
metrics choose for assessment are reasonable and all are very important in the coaching evaluation.  Assuming the classification of the metrics for Coach Evaluation correspond the

<!-- b000105 | prose | pages [6] -->
assessment principle.  The metrics of coach we abandon all are no or little effect to the coaches

<!-- b000106 | prose | pages [6] -->
coaching ability.

<!-- b000107 | prose | pages [6] -->
 Assuming the first level metrics Experience, Achievement and Competency can

<!-- b000108 | prose | pages [6] -->
reflect the Non-quantifiable metrics Coaching skills and abilities of the team management.

<!-- b000109 | prose | pages [6] -->
Symbols Definitions

<!-- b000110 | prose | pages [6] -->
The Variables, Constant, and their Description are shown as below. If you don't know

<!-- b000111 | furniture | pages [6] -->


<!-- b000112 | prose | pages [6] -->
4

<!-- b000113 | furniture | pages [7] -->
Team#28875                                                                      Page 5 of 33

<!-- b000114 | prose | pages [7] -->
a variables or something, you can look it up in the table 1.

<!-- b000115 | caption | pages [7] -->
Table 1  Variables

<!-- b000116 | prose | pages [7] -->
Variables Description

<!-- b000117 | prose | pages [7] -->
m the number of coaches

<!-- b000118 | prose | pages [7] -->
n the number of evaluation metrics

<!-- b000119 | prose | pages [7] -->
w weight

<!-- b000120 | prose | pages [7] -->
B the Judgment Matrix

<!-- b000121 | furniture | pages [7] -->


<!-- b000122 | prose | pages [7] -->
s (i ) the sample standard deviation

<!-- b000123 | furniture | pages [7] -->


<!-- b000124 | prose | pages [7] -->
CIC (n ) Consistency Index Coefficient

<!-- b000125 | furniture | pages [7] -->


<!-- b000126 | prose | pages [7] -->
min CIC ( n ) the minimum of consistency Index Coefficient

<!-- b000127 | furniture | pages [7] -->


<!-- b000128 | prose | pages [7] -->
z ( j ) the composite score

<!-- b000129 | prose | pages [7] -->
Key Terms and Terminology

<!-- b000130 | prose | pages [7] -->
 NCAA, The National Collegiate Athletic Association [15] , is a nonprofit

<!-- b000131 | prose | pages [7] -->
association of 1,281 institutions, conferences, organizations, and individuals that organizes the athletic programs of many colleges and universities in the United States and Canada. It is headquartered in Indianapolis, Indiana.

<!-- b000132 | prose | pages [7] -->
 SRS, Simple Rating System [16], a rating that takes into account average point

<!-- b000133 | prose | pages [7] -->
differential and strength of schedule, the rating is denominated in points above/ below average, where zero is average. Non-Division I games are excluded from the ratings.

<!-- b000134 | prose | pages [7] -->
 SOS, Strength of Schedule, a rating of strength of schedule the rating is

<!-- b000135 | prose | pages [7] -->
denominated in points above /below average, where zero is average Non-Division I games are excluded from the ratings [17].

<!-- b000136 | prose | pages [7] -->
 Judgment Matrix: In the method of AHP, to determine the relative importance of

<!-- b000137 | prose | pages [7] -->
each factor on each level given in these judgments represented numerically [18], written in matrix form is to determine the matrix.

<!-- b000138 | prose | pages [7] -->
 The Relative membership degree values are fuzzy evaluation function in the

<!-- b000139 | prose | pages [7] -->
concept: a kind of fuzzy comprehensive evaluation [19] is affected by many factors, things that make a comprehensive evaluation of the very effective multifactor decision-making method, which is characterized by the evaluation results are not absolutely positive or negative , but in a fuzzy set to represent.

<!-- b000140 | furniture | pages [7] -->


<!-- b000141 | furniture | pages [7] -->


<!-- b000142 | prose | pages [7] -->
5

<!-- b000143 | furniture | pages [8] -->
Team#28875                                                                      Page 6 of 33

<!-- b000144 | heading | pages [8] -->
The developing of models

<!-- b000145 | heading | pages [8] -->
ModelⅠ The Fuzzy Comprehensive Evaluation Model based on

<!-- b000146 | heading | pages [8] -->
Analytic Hierarchy Process (AHP-FCE model)

<!-- b000147 | prose | pages [8] -->
Combined with the AHP and FCE, we obtained the Fuzzy comprehensive evaluation

<!-- b000148 | prose | pages [8] -->
model based on analytic hierarchy process (AHP-FCE) [20]. First of all, we collected the data from the internet, and do the Pretreatment. Then we determined the College

<!-- b000149 | prose | pages [8] -->
Coach metrics for assessment. Finally goes the development of the AHP-FCE model.

<!-- b000150 | heading | pages [8] -->
Data collection and pretreatment

<!-- b000151 | prose | pages [8] -->
Data collect method such as face to face, telephone, postal or self completion and so on. But in this problem，those method above is too difficult to carry out. Because of

<!-- b000152 | prose | pages [8] -->
the provides such as Reduced Costs, Fast Delivery, Easily Personalised and

<!-- b000153 | prose | pages [8] -->
Penetrating difficult target groups [21], we search the internet for the relative data mainly from http://www.sports-reference.com and http://www.ncaa.com. For the

<!-- b000154 | prose | pages [8] -->
pretreatment, because of Sports Illustrated is looking for the “best all time college

<!-- b000155 | prose | pages [8] -->
coach” male or female for the previous century and our problem is to finding out the top 5 coaches. So we set a Standard line, to finding out almost 40 better coaches for

<!-- b000156 | prose | pages [8] -->
each sport, and gather their several metrics value. And then make several Excel tables. Arrange NCAA Basketball, Football and Baseball are shown as follows table 1,

<!-- b000157 | caption | pages [8] -->
table2 and table 3.

<!-- b000158 | prose | pages [8] -->
Choose the metrics for assessment

<!-- b000159 | prose | pages [8] -->
For the purpose of looking for the best college coach, we need determined several

<!-- b000160 | prose | pages [8] -->
metrics [22] for assessment to describe their performance. Research those data we searched on the internet, we can choose the metrics for assessment for all possible

<!-- b000161 | prose | pages [8] -->
sports like NCAA Basketball, Football and Baseball, which are shown as follows

<!-- b000162 | prose | pages [8] -->
table 1, table2 and table 3.

<!-- b000163 | prose | pages [8] -->
NCAA Basketball

<!-- b000164 | prose | pages [8] -->
Champ NCAA

<!-- b000165 | prose | pages [8] -->
AP High

<!-- b000166 | prose | pages [8] -->
WL％

<!-- b000167 | prose | pages [8] -->
Years

<!-- b000168 | prose | pages [8] -->
SRS

<!-- b000169 | prose | pages [8] -->
SOS

<!-- b000170 | prose | pages [8] -->
Final Fours

<!-- b000171 | prose | pages [8] -->
AP Final

<!-- b000172 | prose | pages [8] -->
AP Pre

<!-- b000173 | prose | pages [8] -->
CREG

<!-- b000174 | prose | pages [8] -->
CTRN

<!-- b000175 | prose | pages [8] -->
Game

<!-- b000176 | prose | pages [8] -->
NCAA

<!-- b000177 | furniture | pages [8] -->


<!-- b000178 | caption | pages [8] -->
Figure 1   The metrics for NCAA Basketball coach.

<!-- b000179 | furniture | pages [8] -->


<!-- b000180 | prose | pages [8] -->
6 6

<!-- b000181 | furniture | pages [9] -->
Team#28875                                                                      Page 7 of 33

<!-- b000182 | prose | pages [9] -->
NCAA Football

<!-- b000183 | prose | pages [9] -->
Bowls

<!-- b000184 | prose | pages [9] -->
PCT

<!-- b000185 | prose | pages [9] -->
SRS

<!-- b000186 | prose | pages [9] -->
SOS

<!-- b000187 | prose | pages [9] -->
Overall Game

<!-- b000188 | prose | pages [9] -->
Bowls Game

<!-- b000189 | prose | pages [9] -->
AP High

<!-- b000190 | prose | pages [9] -->
AP Pre

<!-- b000191 | prose | pages [9] -->
AP post

<!-- b000192 | prose | pages [9] -->
Years

<!-- b000193 | furniture | pages [9] -->


<!-- b000194 | caption | pages [9] -->
Figure 2   The metrics for NCAA Football coach.

<!-- b000195 | prose | pages [9] -->
NCAA baseball

<!-- b000196 | prose | pages [9] -->
Years

<!-- b000197 | prose | pages [9] -->
Game

<!-- b000198 | prose | pages [9] -->
PCT

<!-- b000199 | prose | pages [9] -->
Championship

<!-- b000200 | prose | pages [9] -->
Lost

<!-- b000201 | prose | pages [9] -->
Win

<!-- b000202 | furniture | pages [9] -->


<!-- b000203 | caption | pages [9] -->
Figure 3   The metrics for NCAA Baseball coach.

<!-- b000204 | heading | pages [9] -->
Development of the model

<!-- b000205 | prose | pages [9] -->
Based on the actual situation of the evaluation system, we established a fuzzy comprehensive evaluation system, from the representation, systematic, fitness point of view. And according to the sample data of each metrics, we built a fuzzy evaluation matrix of the relative membership degree from each evaluation. The ultimate goal of fuzzy comprehensive evaluation is to choose the best coaches relatives though the relative merits of comparison, among m coaches on the field. On the basis of the relative membership degree and scope of this optimization can determine the relative value of each metrics is relative to excellent coaches.

<!-- b000206 | prose | pages [9] -->
Standardized the metrics value

<!-- b000207 | prose | pages [9] -->
Supposing there are n evaluation metrics and m coaches, and the sample set of evaluation metrics is

<!-- b000208 | prose | pages [9] -->
  x ( i , j ) i ,3,2,1    n , j ,3,2,1 m . 

<!-- b000209 | prose | pages [9] -->
is a non-negative value. For the purpose of determine the Each metrics x ( i , j )

<!-- b000210 | prose | pages [9] -->
individual evaluation metrics of the relative membership degree [25] of fuzzy evaluation matrix, eliminate the effect of each metrics dimension and modeling more

<!-- b000211 | furniture | pages [9] -->


<!-- b000212 | prose | pages [9] -->
7 7

<!-- b000213 | furniture | pages [10] -->
Team#28875                                                                      Page 8 of 33

<!-- b000214 | prose | pages [10] -->
versatility, sample data sets  ) need to standardize treatment [23]. To maintain x ( i , j

<!-- b000215 | prose | pages [10] -->
each metrics value of change information as much as possible, Standardized the bigger the more superior type metrics formula is

<!-- b000216 | prose | pages [10] -->
x

<!-- b000217 | prose | pages [10] -->
(

<!-- b000218 | prose | pages [10] -->
i

<!-- b000219 | prose | pages [10] -->
,

<!-- b000220 | prose | pages [10] -->
 r

<!-- b000221 | prose | pages [10] -->
(

<!-- b000222 | prose | pages [10] -->
i

<!-- b000223 | prose | pages [10] -->
,

<!-- b000224 | prose | pages [10] -->
j

<!-- b000225 | prose | pages [10] -->
)

<!-- b000226 | prose | pages [10] -->


<!-- b000227 | prose | pages [10] -->
x

<!-- b000228 | prose | pages [10] -->
(

<!-- b000229 | prose | pages [10] -->
i

<!-- b000230 | prose | pages [10] -->
)

<!-- b000231 | prose | pages [10] -->
max

<!-- b000232 | prose | pages [10] -->
j j

<!-- b000233 | prose | pages [10] -->
) )

<!-- b000234 | prose | pages [10] -->
（1）

<!-- b000235 | prose | pages [10] -->
x x

<!-- b000236 | prose | pages [10] -->
(

<!-- b000237 | prose | pages [10] -->
i

<!-- b000238 | prose | pages [10] -->
)

<!-- b000239 | prose | pages [10] -->
min

<!-- b000240 | prose | pages [10] -->
The Smaller the more standardized formula excellent type indicators is

<!-- b000241 | prose | pages [10] -->


<!-- b000242 | prose | pages [10] -->
x

<!-- b000243 | prose | pages [10] -->
(

<!-- b000244 | prose | pages [10] -->
i

<!-- b000245 | prose | pages [10] -->
)

<!-- b000246 | prose | pages [10] -->


<!-- b000247 | prose | pages [10] -->
max

<!-- b000248 | prose | pages [10] -->
r

<!-- b000249 | prose | pages [10] -->
(

<!-- b000250 | prose | pages [10] -->
i

<!-- b000251 | prose | pages [10] -->
,

<!-- b000252 | prose | pages [10] -->
j

<!-- b000253 | prose | pages [10] -->
)

<!-- b000254 | prose | pages [10] -->
x

<!-- b000255 | prose | pages [10] -->
(

<!-- b000256 | prose | pages [10] -->
max

<!-- b000257 | prose | pages [10] -->


<!-- b000258 | prose | pages [10] -->
x x

<!-- b000259 | prose | pages [10] -->
(

<!-- b000260 | prose | pages [10] -->
i

<!-- b000261 | prose | pages [10] -->
)

<!-- b000262 | prose | pages [10] -->
x

<!-- b000263 | prose | pages [10] -->
(

<!-- b000264 | prose | pages [10] -->
i

<!-- b000265 | prose | pages [10] -->
,

<!-- b000266 | prose | pages [10] -->
j

<!-- b000267 | prose | pages [10] -->
)

<!-- b000268 | prose | pages [10] -->
min

<!-- b000269 | prose | pages [10] -->
（2）

<!-- b000270 | prose | pages [10] -->


<!-- b000271 | prose | pages [10] -->
i i

<!-- b000272 | prose | pages [10] -->
) )

<!-- b000273 | prose | pages [10] -->
x

<!-- b000274 | prose | pages [10] -->
(

<!-- b000275 | prose | pages [10] -->
i

<!-- b000276 | prose | pages [10] -->
)

<!-- b000277 | prose | pages [10] -->
min

<!-- b000278 | prose | pages [10] -->
The more middle the more standardized formula excellent type indicators is

<!-- b000279 | prose | pages [10] -->


<!-- b000280 | prose | pages [10] -->
x

<!-- b000281 | prose | pages [10] -->
(

<!-- b000282 | prose | pages [10] -->
i

<!-- b000283 | prose | pages [10] -->
,

<!-- b000284 | prose | pages [10] -->
j

<!-- b000285 | prose | pages [10] -->
)

<!-- b000286 | prose | pages [10] -->
,)

<!-- b000287 | prose | pages [10] -->
x

<!-- b000288 | prose | pages [10] -->
(

<!-- b000289 | prose | pages [10] -->


<!-- b000290 | prose | pages [10] -->
m i n

<!-- b000291 | prose | pages [10] -->


<!-- b000292 | prose | pages [10] -->
x

<!-- b000293 | prose | pages [10] -->
(

<!-- b000294 | prose | pages [10] -->
i

<!-- b000295 | prose | pages [10] -->
)

<!-- b000296 | prose | pages [10] -->
x

<!-- b000297 | prose | pages [10] -->
(

<!-- b000298 | prose | pages [10] -->
i

<!-- b000299 | prose | pages [10] -->
m i d

<!-- b000300 | prose | pages [10] -->
m i n

<!-- b000301 | prose | pages [10] -->


<!-- b000302 | furniture | pages [10] -->


<!-- b000303 | prose | pages [10] -->
r

<!-- b000304 | prose | pages [10] -->
(

<!-- b000305 | prose | pages [10] -->
i

<!-- b000306 | prose | pages [10] -->
,

<!-- b000307 | prose | pages [10] -->
j

<!-- b000308 | prose | pages [10] -->
)

<!-- b000309 | prose | pages [10] -->


<!-- b000310 | prose | pages [10] -->
 

<!-- b000311 | prose | pages [10] -->
x

<!-- b000312 | prose | pages [10] -->
(

<!-- b000313 | prose | pages [10] -->
i

<!-- b000314 | prose | pages [10] -->
)

<!-- b000315 | prose | pages [10] -->
x

<!-- b000316 | prose | pages [10] -->
(

<!-- b000317 | prose | pages [10] -->
i

<!-- b000318 | prose | pages [10] -->
)

<!-- b000319 | prose | pages [10] -->
x

<!-- b000320 | prose | pages [10] -->
(

<!-- b000321 | prose | pages [10] -->
i

<!-- b000322 | prose | pages [10] -->
,

<!-- b000323 | prose | pages [10] -->


<!-- b000324 | prose | pages [10] -->
m a x

<!-- b000325 | prose | pages [10] -->
m i d

<!-- b000326 | prose | pages [10] -->


<!-- b000327 | prose | pages [10] -->


<!-- b000328 | prose | pages [10] -->
x

<!-- b000329 | prose | pages [10] -->
(

<!-- b000330 | prose | pages [10] -->
i

<!-- b000331 | prose | pages [10] -->
)

<!-- b000332 | prose | pages [10] -->
x

<!-- b000333 | prose | pages [10] -->
(

<!-- b000334 | prose | pages [10] -->
i

<!-- b000335 | prose | pages [10] -->
)

<!-- b000336 | prose | pages [10] -->


<!-- b000337 | prose | pages [10] -->
m a x

<!-- b000338 | prose | pages [10] -->
m i d

<!-- b000339 | prose | pages [10] -->
The formula:

<!-- b000340 | prose | pages [10] -->
, and x max i ( ) xmid (i x min i ( )

<!-- b000341 | prose | pages [10] -->
 

<!-- b000342 | prose | pages [10] -->
i i

<!-- b000343 | prose | pages [10] -->
) )

<!-- b000344 | prose | pages [10] -->
x

<!-- b000345 | prose | pages [10] -->
(

<!-- b000346 | prose | pages [10] -->
i

<!-- b000347 | prose | pages [10] -->
,

<!-- b000348 | prose | pages [10] -->
j

<!-- b000349 | prose | pages [10] -->
) (

<!-- b000350 | prose | pages [10] -->
i

<!-- b000351 | prose | pages [10] -->
)

<!-- b000352 | prose | pages [10] -->
m i d （3）

<!-- b000353 | prose | pages [10] -->
j j

<!-- b000354 | prose | pages [10] -->
) )

<!-- b000355 | prose | pages [10] -->
 

<!-- b000356 | prose | pages [10] -->
,

<!-- b000357 | prose | pages [10] -->
x

<!-- b000358 | prose | pages [10] -->
(

<!-- b000359 | prose | pages [10] -->
i

<!-- b000360 | prose | pages [10] -->
)

<!-- b000361 | prose | pages [10] -->
x

<!-- b000362 | prose | pages [10] -->
(

<!-- b000363 | prose | pages [10] -->
i

<!-- b000364 | prose | pages [10] -->
,

<!-- b000365 | prose | pages [10] -->
j

<!-- b000366 | prose | pages [10] -->
) (

<!-- b000367 | prose | pages [10] -->
i

<!-- b000368 | prose | pages [10] -->
)

<!-- b000369 | prose | pages [10] -->
m i d

<!-- b000370 | prose | pages [10] -->
m a x

<!-- b000371 | prose | pages [10] -->
respectively stands for the minimum, ) )

<!-- b000372 | prose | pages [10] -->
maximum and the intermediate optimum values of the i metrics ;

<!-- b000373 | prose | pages [10] -->
is the r ( i , j )

<!-- b000374 | prose | pages [10] -->
evaluation, normalized value of the and also is the relative

<!-- b000375 | prose | pages [10] -->
membership degree from belongs to the optimal value of the j coaches in the i

<!-- b000376 | prose | pages [10] -->
evaluation, and i=1,2,3,…,n,  j=1,2,3,…,n.  Those values of can be r ( i , j )

<!-- b000377 | prose | pages [10] -->
composed of a single element evaluation of fuzzy evaluation matrix

<!-- b000378 | prose | pages [10] -->
 R ( r

<!-- b000379 | prose | pages [10] -->
Construct the Judgment Matrix

<!-- b000380 | prose | pages [10] -->
According to the fuzzy evaluation matrix

<!-- b000381 | prose | pages [10] -->
( ( i i , , j )) .  n m

<!-- b000382 | prose | pages [10] -->
 R ( r ( i , j )) ，Calculate the Judgment  n m

<!-- b000383 | prose | pages [10] -->
Matrix to determine the weight of each metrics. Fuzzy evaluation, in essence, is a

<!-- b000384 | prose | pages [10] -->
preferred process. If the sample series    r ( 1 i , j ) j 3,2,1 m of the evaluation 

<!-- b000385 | prose | pages [10] -->
1i has a more big degree of change than the sample series metrics

<!-- b000386 | prose | pages [10] -->
   r ( 2 i , j ) j 3,2,1 m 2i , it means that 1i transfer more of the evaluation metrics 

<!-- b000387 | prose | pages [10] -->
2i .Therefore we can use the sample Comprehensive evaluation information than

<!-- b000388 | prose | pages [10] -->
m

<!-- b000389 | prose | pages [10] -->


<!-- b000390 | prose | pages [10] -->


<!-- b000391 | prose | pages [10] -->
(

<!-- b000392 | prose | pages [10] -->
r

<!-- b000393 | prose | pages [10] -->
(

<!-- b000394 | prose | pages [10] -->
i

<!-- b000395 | prose | pages [10] -->
,

<!-- b000396 | prose | pages [10] -->
j

<!-- b000397 | prose | pages [10] -->
)

<!-- b000398 | prose | pages [10] -->
r

<!-- b000399 | prose | pages [10] -->
i

<!-- b000400 | prose | pages [10] -->


<!-- b000401 | prose | pages [10] -->
j

<!-- b000402 | prose | pages [10] -->
1

<!-- b000403 | prose | pages [10] -->


<!-- b000404 | prose | pages [10] -->
s

<!-- b000405 | prose | pages [10] -->
(

<!-- b000406 | prose | pages [10] -->
i

<!-- b000407 | prose | pages [10] -->
)

<!-- b000408 | prose | pages [10] -->
standard deviation m

<!-- b000409 | prose | pages [10] -->
2) 2) , of each evaluation metrics to reflects the

<!-- b000410 | prose | pages [10] -->
degree of impact on the comprehensive evaluation. Thus Calculate the Judgment

<!-- b000411 | furniture | pages [10] -->


<!-- b000412 | prose | pages [10] -->
8 8

<!-- b000413 | furniture | pages [11] -->
Team#28875                                                                      Page 9 of 33

<!-- b000414 | prose | pages [11] -->
m

<!-- b000415 | prose | pages [11] -->


<!-- b000416 | prose | pages [11] -->
r

<!-- b000417 | prose | pages [11] -->
(

<!-- b000418 | prose | pages [11] -->
i

<!-- b000419 | prose | pages [11] -->
,

<!-- b000420 | prose | pages [11] -->
j

<!-- b000421 | prose | pages [11] -->
)

<!-- b000422 | prose | pages [11] -->


<!-- b000423 | prose | pages [11] -->
j

<!-- b000424 | prose | pages [11] -->
1

<!-- b000425 | prose | pages [11] -->


<!-- b000426 | prose | pages [11] -->
, i=1,2,..,n, stands for the mean of each evaluation sample

<!-- b000427 | prose | pages [11] -->
Matrix B, and

<!-- b000428 | prose | pages [11] -->
r

<!-- b000429 | prose | pages [11] -->
i

<!-- b000430 | prose | pages [11] -->
m

<!-- b000431 | prose | pages [11] -->
sequence. According to Formula (4), get the Judgment Matrix which maximum moment is 9.

<!-- b000432 | prose | pages [11] -->


<!-- b000433 | prose | pages [11] -->


<!-- b000434 | prose | pages [11] -->
s

<!-- b000435 | prose | pages [11] -->
(

<!-- b000436 | prose | pages [11] -->
i

<!-- b000437 | prose | pages [11] -->
)

<!-- b000438 | prose | pages [11] -->
s

<!-- b000439 | prose | pages [11] -->
(

<!-- b000440 | prose | pages [11] -->
j

<!-- b000441 | prose | pages [11] -->
)

<!-- b000442 | prose | pages [11] -->


<!-- b000443 | prose | pages [11] -->
s

<!-- b000444 | prose | pages [11] -->
(

<!-- b000445 | prose | pages [11] -->
i

<!-- b000446 | prose | pages [11] -->
) (

<!-- b000447 | prose | pages [11] -->


<!-- b000448 | prose | pages [11] -->


<!-- b000449 | prose | pages [11] -->
s s

<!-- b000450 | furniture | pages [11] -->


<!-- b000451 | prose | pages [11] -->


<!-- b000452 | prose | pages [11] -->
m a x m i n

<!-- b000453 | prose | pages [11] -->
1

<!-- b000454 | prose | pages [11] -->


<!-- b000455 | prose | pages [11] -->
b

<!-- b000456 | prose | pages [11] -->


<!-- b000457 | prose | pages [11] -->
ij

<!-- b000458 | prose | pages [11] -->


<!-- b000459 | prose | pages [11] -->


<!-- b000460 | prose | pages [11] -->
s

<!-- b000461 | prose | pages [11] -->
(

<!-- b000462 | prose | pages [11] -->
j

<!-- b000463 | prose | pages [11] -->
)

<!-- b000464 | prose | pages [11] -->
s

<!-- b000465 | prose | pages [11] -->
(

<!-- b000466 | prose | pages [11] -->
i

<!-- b000467 | prose | pages [11] -->
)

<!-- b000468 | prose | pages [11] -->


<!-- b000469 | prose | pages [11] -->
(

<!-- b000470 | prose | pages [11] -->
b

<!-- b000471 | prose | pages [11] -->
1

<!-- b000472 | prose | pages [11] -->


<!-- b000473 | prose | pages [11] -->
m

<!-- b000474 | prose | pages [11] -->


<!-- b000475 | prose | pages [11] -->
s s

<!-- b000476 | prose | pages [11] -->


<!-- b000477 | prose | pages [11] -->
m a x m i n

<!-- b000478 | prose | pages [11] -->
  

<!-- b000479 | prose | pages [11] -->
b b

<!-- b000480 | prose | pages [11] -->
1 ) ,1

<!-- b000481 | prose | pages [11] -->
s

<!-- b000482 | prose | pages [11] -->
(

<!-- b000483 | prose | pages [11] -->
i

<!-- b000484 | prose | pages [11] -->
)

<!-- b000485 | prose | pages [11] -->
s

<!-- b000486 | prose | pages [11] -->
(

<!-- b000487 | prose | pages [11] -->
j

<!-- b000488 | prose | pages [11] -->
)

<!-- b000489 | prose | pages [11] -->
m m

<!-- b000490 | prose | pages [11] -->
（4）

<!-- b000491 | prose | pages [11] -->


<!-- b000492 | prose | pages [11] -->
,

<!-- b000493 | prose | pages [11] -->
s

<!-- b000494 | prose | pages [11] -->
(

<!-- b000495 | prose | pages [11] -->
i

<!-- b000496 | prose | pages [11] -->
)

<!-- b000497 | prose | pages [11] -->
s

<!-- b000498 | prose | pages [11] -->
(

<!-- b000499 | prose | pages [11] -->
j

<!-- b000500 | prose | pages [11] -->
)

<!-- b000501 | prose | pages [11] -->
 

<!-- b000502 | prose | pages [11] -->
) ) 1

<!-- b000503 | prose | pages [11] -->
stands for the minimum and maximum of In the formula, s s , max min   s ( i ) i 3,2,1 n . 

<!-- b000504 | prose | pages [11] -->


<!-- b000505 | prose | pages [11] -->


<!-- b000506 | prose | pages [11] -->
s

<!-- b000507 | prose | pages [11] -->


<!-- b000508 | prose | pages [11] -->
max

<!-- b000509 | prose | pages [11] -->
bm

<!-- b000510 | prose | pages [11] -->
min

<!-- b000511 | prose | pages [11] -->
i

<!-- b000512 | prose | pages [11] -->
, int( )

<!-- b000513 | prose | pages [11] -->
The relative importance of the degree parameter is

<!-- b000514 | prose | pages [11] -->
, min

<!-- b000515 | prose | pages [11] -->


<!-- b000516 | prose | pages [11] -->


<!-- b000517 | prose | pages [11] -->


<!-- b000518 | prose | pages [11] -->
s

<!-- b000519 | prose | pages [11] -->
5.0

<!-- b000520 | prose | pages [11] -->


<!-- b000521 | prose | pages [11] -->


<!-- b000522 | prose | pages [11] -->
min

<!-- b000523 | prose | pages [11] -->
and int stands for the min function and the int funcation.

<!-- b000524 | prose | pages [11] -->
Calculate the Weight and Consistency Test

<!-- b000525 | prose | pages [11] -->
 In the Judgment Matrix B, the Consistency test, revise and weight [31]

<!-- b000526 | prose | pages [11] -->
n

<!-- b000527 | prose | pages [11] -->
and 

<!-- b000528 | prose | pages [11] -->


<!-- b000529 | prose | pages [11] -->
iw 0

<!-- b000530 | furniture | pages [11] -->


<!-- b000531 | prose | pages [11] -->
wi ( i 3,2,1 n )

<!-- b000532 | furniture | pages [11] -->


<!-- b000533 | prose | pages [11] -->


<!-- b000534 | prose | pages [11] -->
1. According to the definition of the Judgment

<!-- b000535 | prose | pages [11] -->
need meeting

<!-- b000536 | prose | pages [11] -->
w i

<!-- b000537 | prose | pages [11] -->


<!-- b000538 | prose | pages [11] -->
i

<!-- b000539 | prose | pages [11] -->
1

<!-- b000540 | prose | pages [11] -->
Matrix B, Theoretically that

<!-- b000541 | prose | pages [11] -->
w b  

<!-- b000542 | prose | pages [11] -->
i

<!-- b000543 | furniture | pages [11] -->


<!-- b000544 | prose | pages [11] -->
( i , j

<!-- b000545 | prose | pages [11] -->
ij w

<!-- b000546 | prose | pages [11] -->
j

<!-- b000547 | prose | pages [11] -->
Thus the Judgment Matrix B is

<!-- b000548 | prose | pages [11] -->


<!-- b000549 | prose | pages [11] -->
w

<!-- b000550 | prose | pages [11] -->


<!-- b000551 | prose | pages [11] -->
1

<!-- b000552 | prose | pages [11] -->
b b

<!-- b000553 | prose | pages [11] -->


<!-- b000554 | prose | pages [11] -->
11

<!-- b000555 | prose | pages [11] -->
12

<!-- b000556 | prose | pages [11] -->
w

<!-- b000557 | prose | pages [11] -->


<!-- b000558 | prose | pages [11] -->
1

<!-- b000559 | prose | pages [11] -->


<!-- b000560 | prose | pages [11] -->
w

<!-- b000561 | prose | pages [11] -->


<!-- b000562 | prose | pages [11] -->
2

<!-- b000563 | prose | pages [11] -->
b b

<!-- b000564 | prose | pages [11] -->


<!-- b000565 | prose | pages [11] -->
21

<!-- b000566 | prose | pages [11] -->
22

<!-- b000567 | prose | pages [11] -->
w

<!-- b000568 | prose | pages [11] -->


<!-- b000569 | prose | pages [11] -->
1

<!-- b000570 | prose | pages [11] -->


<!-- b000571 | prose | pages [11] -->
B

<!-- b000572 | prose | pages [11] -->
 

<!-- b000573 | prose | pages [11] -->


<!-- b000574 | prose | pages [11] -->
 

<!-- b000575 | prose | pages [11] -->
w

<!-- b000576 | prose | pages [11] -->


<!-- b000577 | prose | pages [11] -->


<!-- b000578 | prose | pages [11] -->
n

<!-- b000579 | prose | pages [11] -->
b b

<!-- b000580 | prose | pages [11] -->
n

<!-- b000581 | prose | pages [11] -->
1

<!-- b000582 | prose | pages [11] -->
n

<!-- b000583 | prose | pages [11] -->


<!-- b000584 | prose | pages [11] -->
w

<!-- b000585 | prose | pages [11] -->


<!-- b000586 | prose | pages [11] -->
1

<!-- b000587 | prose | pages [11] -->
（5） 3,2,1 n ) 

<!-- b000588 | prose | pages [11] -->


<!-- b000589 | prose | pages [11] -->
w

<!-- b000590 | prose | pages [11] -->
w

<!-- b000591 | prose | pages [11] -->
  

<!-- b000592 | prose | pages [11] -->
1

<!-- b000593 | prose | pages [11] -->
1

<!-- b000594 | prose | pages [11] -->
b

<!-- b000595 | prose | pages [11] -->


<!-- b000596 | prose | pages [11] -->


<!-- b000597 | prose | pages [11] -->
1

<!-- b000598 | prose | pages [11] -->
n

<!-- b000599 | prose | pages [11] -->
w

<!-- b000600 | prose | pages [11] -->
w

<!-- b000601 | prose | pages [11] -->


<!-- b000602 | prose | pages [11] -->
2

<!-- b000603 | prose | pages [11] -->
n

<!-- b000604 | prose | pages [11] -->


<!-- b000605 | prose | pages [11] -->
w w

<!-- b000606 | prose | pages [11] -->
  

<!-- b000607 | prose | pages [11] -->
2

<!-- b000608 | prose | pages [11] -->
2

<!-- b000609 | prose | pages [11] -->
b

<!-- b000610 | prose | pages [11] -->


<!-- b000611 | prose | pages [11] -->


<!-- b000612 | prose | pages [11] -->
2

<!-- b000613 | prose | pages [11] -->
n

<!-- b000614 | prose | pages [11] -->
w w

<!-- b000615 | prose | pages [11] -->


<!-- b000616 | prose | pages [11] -->
2

<!-- b000617 | prose | pages [11] -->
n

<!-- b000618 | furniture | pages [11] -->


<!-- b000619 | prose | pages [11] -->


<!-- b000620 | prose | pages [11] -->
w

<!-- b000621 | prose | pages [11] -->


<!-- b000622 | prose | pages [11] -->


<!-- b000623 | prose | pages [11] -->
i

<!-- b000624 | prose | pages [11] -->
b

<!-- b000625 | prose | pages [11] -->
 

<!-- b000626 | prose | pages [11] -->
ij

<!-- b000627 | prose | pages [11] -->
w

<!-- b000628 | prose | pages [11] -->


<!-- b000629 | prose | pages [11] -->
j

<!-- b000630 | prose | pages [11] -->


<!-- b000631 | prose | pages [11] -->
w w

<!-- b000632 | prose | pages [11] -->


<!-- b000633 | prose | pages [11] -->
   

<!-- b000634 | prose | pages [11] -->
n n

<!-- b000635 | prose | pages [11] -->
b

<!-- b000636 | prose | pages [11] -->
1

<!-- b000637 | prose | pages [11] -->


<!-- b000638 | prose | pages [11] -->
2 2

<!-- b000639 | prose | pages [11] -->
nn

<!-- b000640 | prose | pages [11] -->


<!-- b000641 | prose | pages [11] -->
w w

<!-- b000642 | prose | pages [11] -->


<!-- b000643 | prose | pages [11] -->
2

<!-- b000644 | prose | pages [11] -->
n

<!-- b000645 | prose | pages [11] -->
On the basis of its Units, Reciprocal (reciprocity) and the Consistency condition, we can savvy those characteristics of the Judgment Matrix B,

<!-- b000646 | furniture | pages [11] -->


<!-- b000647 | prose | pages [11] -->
9 9

<!-- b000648 | furniture | pages [12] -->
Team#28875                                                                      Page 10 of 33

<!-- b000649 | prose | pages [12] -->
w

<!-- b000650 | prose | pages [12] -->


<!-- b000651 | prose | pages [12] -->
b

<!-- b000652 | prose | pages [12] -->
[1]

<!-- b000653 | prose | pages [12] -->
ii w

<!-- b000654 | prose | pages [12] -->
w  b

<!-- b000655 | prose | pages [12] -->
[2]

<!-- b000656 | prose | pages [12] -->
ji w

<!-- b000657 | prose | pages [12] -->
b b

<!-- b000658 | prose | pages [12] -->
[3]

<!-- b000659 | prose | pages [12] -->
ij jk

<!-- b000660 | prose | pages [12] -->


<!-- b000661 | prose | pages [12] -->


<!-- b000662 | prose | pages [12] -->
i i

<!-- b000663 | prose | pages [12] -->
1

<!-- b000664 | furniture | pages [12] -->


<!-- b000665 | prose | pages [12] -->
i i

<!-- b000666 | prose | pages [12] -->
1

<!-- b000667 | prose | pages [12] -->
j j

<!-- b000668 | prose | pages [12] -->


<!-- b000669 | furniture | pages [12] -->


<!-- b000670 | prose | pages [12] -->
b

<!-- b000671 | prose | pages [12] -->
i i ij

<!-- b000672 | prose | pages [12] -->
w

<!-- b000673 | prose | pages [12] -->
w

<!-- b000674 | prose | pages [12] -->
w

<!-- b000675 | prose | pages [12] -->
j

<!-- b000676 | prose | pages [12] -->
    

<!-- b000677 | prose | pages [12] -->
i

<!-- b000678 | prose | pages [12] -->
i

<!-- b000679 | prose | pages [12] -->
b

<!-- b000680 | furniture | pages [12] -->


<!-- b000681 | prose | pages [12] -->
ik

<!-- b000682 | prose | pages [12] -->
w

<!-- b000683 | prose | pages [12] -->
w

<!-- b000684 | prose | pages [12] -->
w

<!-- b000685 | prose | pages [12] -->
j

<!-- b000686 | prose | pages [12] -->
k

<!-- b000687 | prose | pages [12] -->
k

<!-- b000688 | prose | pages [12] -->
, can calculating the weight of each metrics value, Based on B ( b )  ij n n

<!-- b000689 | prose | pages [12] -->
   wi i 3,2,1 n . If Judgment Matrix B fulfils Formula (5), and fully consistent, thus, 

<!-- b000690 | prose | pages [12] -->
n

<!-- b000691 | prose | pages [12] -->
n

<!-- b000692 | prose | pages [12] -->
 

<!-- b000693 | prose | pages [12] -->
b w ij j

<!-- b000694 | prose | pages [12] -->
 

<!-- b000695 | prose | pages [12] -->
i

<!-- b000696 | prose | pages [12] -->
1

<!-- b000697 | prose | pages [12] -->
j

<!-- b000698 | prose | pages [12] -->
1 

<!-- b000699 | prose | pages [12] -->
w

<!-- b000700 | prose | pages [12] -->
0

<!-- b000701 | prose | pages [12] -->
（6） i

<!-- b000702 | prose | pages [12] -->
But because of the actual complexity evaluation system, people diversity

<!-- b000703 | prose | pages [12] -->
awareness and sidedness and instability of subjective, the Judgment Matrix B

<!-- b000704 | prose | pages [12] -->
may not fully consistent those requirement, and it is Objective, can not be

<!-- b000705 | prose | pages [12] -->
completely eliminated in practical application.

<!-- b000706 | prose | pages [12] -->
Analytic Hierarchy Process requires Judgment Matrix B has satisfactory

<!-- b000707 | prose | pages [12] -->
consistency, so that can adapt to a variety of complex systems. If Judgment

<!-- b000708 | prose | pages [12] -->
Matrix B cannot meet the satisfactory consistency, it need correct. Supposing the

<!-- b000709 | prose | pages [12] -->
corrected judgment matrix of B is

<!-- b000710 | prose | pages [12] -->
   wi i 3,2,1 n

<!-- b000711 | prose | pages [12] -->
  Y ijy , Its weight denoted  n n

<!-- b000712 | prose | pages [12] -->
, then the minimum Y is known as Optimal consistency of 

<!-- b000713 | prose | pages [12] -->
judgment matrix.

<!-- b000714 | prose | pages [12] -->
n

<!-- b000715 | prose | pages [12] -->
n

<!-- b000716 | prose | pages [12] -->


<!-- b000717 | prose | pages [12] -->


<!-- b000718 | prose | pages [12] -->
y b

<!-- b000719 | prose | pages [12] -->
ij

<!-- b000720 | prose | pages [12] -->
 

<!-- b000721 | prose | pages [12] -->


<!-- b000722 | prose | pages [12] -->
i

<!-- b000723 | prose | pages [12] -->
1

<!-- b000724 | prose | pages [12] -->
j

<!-- b000725 | prose | pages [12] -->
1 min

<!-- b000726 | prose | pages [12] -->
CIC

<!-- b000727 | prose | pages [12] -->
(

<!-- b000728 | prose | pages [12] -->
n

<!-- b000729 | prose | pages [12] -->
) 2

<!-- b000730 | prose | pages [12] -->
n

<!-- b000731 | prose | pages [12] -->
n

<!-- b000732 | prose | pages [12] -->
n

<!-- b000733 | prose | pages [12] -->


<!-- b000734 | prose | pages [12] -->


<!-- b000735 | prose | pages [12] -->
y w w

<!-- b000736 | prose | pages [12] -->
ji ji

<!-- b000737 | prose | pages [12] -->
ij j i

<!-- b000738 | prose | pages [12] -->
 

<!-- b000739 | prose | pages [12] -->


<!-- b000740 | prose | pages [12] -->
i

<!-- b000741 | prose | pages [12] -->
1

<!-- b000742 | prose | pages [12] -->
j

<!-- b000743 | prose | pages [12] -->
1

<!-- b000744 | prose | pages [12] -->
（7）

<!-- b000745 | prose | pages [12] -->
2 n

<!-- b000746 | prose | pages [12] -->
Based on above, we established of a single target current planning model. The objective function：

<!-- b000747 | prose | pages [12] -->
n

<!-- b000748 | prose | pages [12] -->
n

<!-- b000749 | prose | pages [12] -->


<!-- b000750 | prose | pages [12] -->
y

<!-- b000751 | prose | pages [12] -->
ij

<!-- b000752 | prose | pages [12] -->
 

<!-- b000753 | prose | pages [12] -->
i

<!-- b000754 | prose | pages [12] -->
1

<!-- b000755 | prose | pages [12] -->
j

<!-- b000756 | prose | pages [12] -->
1

<!-- b000757 | prose | pages [12] -->


<!-- b000758 | prose | pages [12] -->
min

<!-- b000759 | prose | pages [12] -->
CIC

<!-- b000760 | prose | pages [12] -->
(

<!-- b000761 | prose | pages [12] -->
n

<!-- b000762 | prose | pages [12] -->
)

<!-- b000763 | prose | pages [12] -->
2

<!-- b000764 | prose | pages [12] -->
n

<!-- b000765 | prose | pages [12] -->
And it Restrictions:

<!-- b000766 | furniture | pages [12] -->


<!-- b000767 | prose | pages [12] -->
n

<!-- b000768 | prose | pages [12] -->
n

<!-- b000769 | prose | pages [12] -->


<!-- b000770 | prose | pages [12] -->
  

<!-- b000771 | prose | pages [12] -->
b

<!-- b000772 | prose | pages [12] -->
y w w

<!-- b000773 | prose | pages [12] -->
ji

<!-- b000774 | prose | pages [12] -->
ij j i

<!-- b000775 | prose | pages [12] -->
 

<!-- b000776 | prose | pages [12] -->
i

<!-- b000777 | prose | pages [12] -->
1

<!-- b000778 | prose | pages [12] -->
j

<!-- b000779 | prose | pages [12] -->
1

<!-- b000780 | prose | pages [12] -->


<!-- b000781 | furniture | pages [12] -->


<!-- b000782 | prose | pages [12] -->
2

<!-- b000783 | prose | pages [12] -->
n

<!-- b000784 | prose | pages [12] -->
10 10

<!-- b000785 | furniture | pages [13] -->
Team#28875                                                                      Page 11 of 33

<!-- b000786 | prose | pages [13] -->
 

<!-- b000787 | prose | pages [13] -->


<!-- b000788 | prose | pages [13] -->
y

<!-- b000789 | prose | pages [13] -->
(,1

<!-- b000790 | prose | pages [13] -->
i

<!-- b000791 | prose | pages [13] -->
3,2,1

<!-- b000792 | prose | pages [13] -->
n

<!-- b000793 | prose | pages [13] -->
)

<!-- b000794 | prose | pages [13] -->


<!-- b000795 | prose | pages [13] -->
ii

<!-- b000796 | prose | pages [13] -->


<!-- b000797 | prose | pages [13] -->


<!-- b000798 | prose | pages [13] -->
1

<!-- b000799 | prose | pages [13] -->


<!-- b000800 | prose | pages [13] -->
   

<!-- b000801 | prose | pages [13] -->
y b db

<!-- b000802 | prose | pages [13] -->
,

<!-- b000803 | prose | pages [13] -->
b db

<!-- b000804 | prose | pages [13] -->
ij ij ij ij ij

<!-- b000805 | prose | pages [13] -->


<!-- b000806 | prose | pages [13] -->
y

<!-- b000807 | prose | pages [13] -->
ji

<!-- b000808 | prose | pages [13] -->
s

<!-- b000809 | prose | pages [13] -->
..

<!-- b000810 | prose | pages [13] -->
t

<!-- b000811 | prose | pages [13] -->


<!-- b000812 | prose | pages [13] -->
 

<!-- b000813 | prose | pages [13] -->
w

<!-- b000814 | prose | pages [13] -->
0 (

<!-- b000815 | prose | pages [13] -->
i

<!-- b000816 | prose | pages [13] -->
3,2,1

<!-- b000817 | prose | pages [13] -->
n

<!-- b000818 | prose | pages [13] -->
)

<!-- b000819 | prose | pages [13] -->


<!-- b000820 | prose | pages [13] -->


<!-- b000821 | prose | pages [13] -->
i

<!-- b000822 | prose | pages [13] -->


<!-- b000823 | prose | pages [13] -->
n

<!-- b000824 | prose | pages [13] -->


<!-- b000825 | prose | pages [13] -->


<!-- b000826 | prose | pages [13] -->


<!-- b000827 | prose | pages [13] -->
w

<!-- b000828 | prose | pages [13] -->
1

<!-- b000829 | prose | pages [13] -->
i

<!-- b000830 | prose | pages [13] -->


<!-- b000831 | prose | pages [13] -->


<!-- b000832 | prose | pages [13] -->
i

<!-- b000833 | prose | pages [13] -->
1

<!-- b000834 | prose | pages [13] -->
 

<!-- b000835 | prose | pages [13] -->
   

<!-- b000836 | prose | pages [13] -->
(

<!-- b000837 | prose | pages [13] -->
i

<!-- b000838 | prose | pages [13] -->
3,2,1

<!-- b000839 | prose | pages [13] -->
n

<!-- b000840 | prose | pages [13] -->
,

<!-- b000841 | prose | pages [13] -->
j i

<!-- b000842 | prose | pages [13] -->
,1

<!-- b000843 | prose | pages [13] -->
i

<!-- b000844 | prose | pages [13] -->
,2

<!-- b000845 | prose | pages [13] -->
n

<!-- b000846 | prose | pages [13] -->
)

<!-- b000847 | prose | pages [13] -->
 

<!-- b000848 | furniture | pages [13] -->


<!-- b000849 | prose | pages [13] -->
as Consistency Index Coefficient, d stands for In the formula, named CIC (n )

<!-- b000850 | prose | pages [13] -->
 . In General, the smaller Non-negative parameter, and d [ 5.0,0 ]

<!-- b000851 | prose | pages [13] -->
 CIC 1.0

<!-- b000852 | prose | pages [13] -->
is, then the CIC (n )

<!-- b000853 | prose | pages [13] -->
, considering subjective judgment matrix better degree of consistency. If

<!-- b000854 | prose | pages [13] -->
consistency is acceptable. Using Lingo, we can get the minimum value of

<!-- b000855 | prose | pages [13] -->
Thus obtain the most accurate weight.

<!-- b000856 | prose | pages [13] -->
The composite score

<!-- b000857 | prose | pages [13] -->
, CIC (n )

<!-- b000858 | prose | pages [13] -->
Multiply and accumulate each metrics weight w and each coach evaluation metrics i

<!-- b000859 | prose | pages [13] -->
, get the Fuzzy Evaluation composite score relative membership degree r ( i , j )

<!-- b000860 | prose | pages [13] -->
n

<!-- b000861 | prose | pages [13] -->


<!-- b000862 | prose | pages [13] -->


<!-- b000863 | prose | pages [13] -->
z

<!-- b000864 | prose | pages [13] -->
(

<!-- b000865 | prose | pages [13] -->
j

<!-- b000866 | prose | pages [13] -->
)

<!-- b000867 | prose | pages [13] -->
w r

<!-- b000868 | prose | pages [13] -->
(

<!-- b000869 | prose | pages [13] -->
i

<!-- b000870 | prose | pages [13] -->
,

<!-- b000871 | prose | pages [13] -->
j

<!-- b000872 | prose | pages [13] -->
)

<!-- b000873 | prose | pages [13] -->
i

<!-- b000874 | prose | pages [13] -->


<!-- b000875 | prose | pages [13] -->
i

<!-- b000876 | prose | pages [13] -->
1

<!-- b000877 | prose | pages [13] -->
, z ( j )

<!-- b000878 | prose | pages [13] -->


<!-- b000879 | furniture | pages [13] -->


<!-- b000880 | furniture | pages [13] -->


<!-- b000881 | prose | pages [13] -->
（8） ( ( j 3,2,1 m ) 

<!-- b000882 | prose | pages [13] -->
is the larger, means the better the j coach is. So that we can scientific find And z ( j )

<!-- b000883 | prose | pages [13] -->
out the Best College Coach.

<!-- b000884 | heading | pages [13] -->
Testing the model

<!-- b000885 | prose | pages [13] -->
Owing to we are familiar with basketball, thus we choose the coach from NCAA

<!-- b000886 | heading | pages [13] -->
Basketball to validate the model AHP-FCE. Through the data collection and

<!-- b000887 | prose | pages [13] -->
pretreatment, we get 13 metrics for 39 coaches. In this sample, from metrics 5 to

<!-- b000888 | prose | pages [13] -->
metrics 8 are the smaller the superior type indicators, then according to formula (2) to

<!-- b000889 | prose | pages [13] -->
Calculating the relative value of membership. And others follow formula (1) to

<!-- b000890 | prose | pages [13] -->
Calculating the relative value of membership. Thus the value of from metrics 1 s (i )

<!-- b000891 | prose | pages [13] -->
to 13 are 0.110、0.099、0.261、0.323、0.269、0.226、0.215、0.186、0.199、0.340、

<!-- b000892 | prose | pages [13] -->
0.059、0.270、0.330.

<!-- b000893 | prose | pages [13] -->
Calculate the weight

<!-- b000894 | prose | pages [13] -->
According to formula (4) obtain the Judgment Matrix B as follow.

<!-- b000895 | furniture | pages [13] -->


<!-- b000896 | prose | pages [13] -->
11 11

<!-- b000897 | furniture | pages [14] -->
Team#28875                                                                      Page 12 of 33

<!-- b000898 | prose | pages [14] -->


<!-- b000899 | prose | pages [14] -->
.1 000 .1 091 .0 444 .0 361

<!-- b000900 | prose | pages [14] -->
.0 431 .0 509

<!-- b000901 | prose | pages [14] -->


<!-- b000902 | prose | pages [14] -->
.0 917 .1 000 .0 427 .0 350

<!-- b000903 | prose | pages [14] -->
.0 415 .0 486

<!-- b000904 | prose | pages [14] -->
 

<!-- b000905 | prose | pages [14] -->
.2 253 .2 342 .1 000 .0 660

<!-- b000906 | prose | pages [14] -->
.0 939 .1 289

<!-- b000907 | prose | pages [14] -->


<!-- b000908 | prose | pages [14] -->
.2 768 .2 859 .1 515 .1 000

<!-- b000909 | prose | pages [14] -->
.1 450 .1 803

<!-- b000910 | prose | pages [14] -->
 

<!-- b000911 | prose | pages [14] -->
.2 318 .2 409 .1 065 .0 690

<!-- b000912 | prose | pages [14] -->
.1 000 .1 355

<!-- b000913 | prose | pages [14] -->


<!-- b000914 | prose | pages [14] -->
.1 965 .2 056 .0 776 .0 555

<!-- b000915 | prose | pages [14] -->
.0 738 .1 000

<!-- b000916 | prose | pages [14] -->
 

<!-- b000917 | prose | pages [14] -->
.1 875 .1 966 .0 725 .0 528

<!-- b000918 | prose | pages [14] -->
.0 692 .0 919

<!-- b000919 | prose | pages [14] -->


<!-- b000920 | prose | pages [14] -->


<!-- b000921 | prose | pages [14] -->
B

<!-- b000922 | prose | pages [14] -->
.1 631 .1 723 .0 617 .0 468

<!-- b000923 | prose | pages [14] -->
.0 592 .0 751

<!-- b000924 | prose | pages [14] -->
 

<!-- b000925 | prose | pages [14] -->
.1 737 .1 828 .0 660 .0 492

<!-- b000926 | prose | pages [14] -->
.0 632 .0 816

<!-- b000927 | prose | pages [14] -->
 

<!-- b000928 | prose | pages [14] -->
.2 907 .2 999 .1 654 .1 140

<!-- b000929 | prose | pages [14] -->
.1 588 .1 945

<!-- b000930 | prose | pages [14] -->


<!-- b000931 | prose | pages [14] -->
.1 737 .1 828 .2 893 .1 163

<!-- b000932 | prose | pages [14] -->
.0 632 .0 816

<!-- b000933 | prose | pages [14] -->
 

<!-- b000934 | prose | pages [14] -->
.2 325 .2 416 .1 072 .0 693

<!-- b000935 | prose | pages [14] -->
.1 005 .1 362

<!-- b000936 | prose | pages [14] -->
 

<!-- b000937 | prose | pages [14] -->
.2 811 27 . 42 .1 558 .1 004 .1 492 .1 849

<!-- b000938 | prose | pages [14] -->


<!-- b000939 | prose | pages [14] -->


<!-- b000940 | prose | pages [14] -->


<!-- b000941 | prose | pages [14] -->
.0 .0 533 .0 613

<!-- b000942 | prose | pages [14] -->
.0 576 .0 344 .0 576 .0 430

<!-- b000943 | prose | pages [14] -->
.0 356

<!-- b000944 | prose | pages [14] -->


<!-- b000945 | prose | pages [14] -->
.0 .0 509 .0 580

<!-- b000946 | prose | pages [14] -->
.0 547 .0 333 .0 547 .0 414

<!-- b000947 | prose | pages [14] -->
.0 345

<!-- b000948 | prose | pages [14] -->
 

<!-- b000949 | prose | pages [14] -->
.1 .1 379 .1 622

<!-- b000950 | prose | pages [14] -->
.1 516 .0 604 .0 346 .0 933

<!-- b000951 | prose | pages [14] -->
.0 642

<!-- b000952 | prose | pages [14] -->


<!-- b000953 | prose | pages [14] -->
.1 .1 893 .2 136

<!-- b000954 | prose | pages [14] -->
.2 031 .0 877 .0 860 .1 443

<!-- b000955 | prose | pages [14] -->
.0 958

<!-- b000956 | prose | pages [14] -->
 

<!-- b000957 | prose | pages [14] -->
.1 .1 445 .1 688

<!-- b000958 | prose | pages [14] -->
.1 582 .0 630 .1 583 .0 995

<!-- b000959 | prose | pages [14] -->
.0 670

<!-- b000960 | prose | pages [14] -->


<!-- b000961 | prose | pages [14] -->
.1 .1 088 .1 331

<!-- b000962 | prose | pages [14] -->
.1 226 .0 514 .1 226 .0 734

<!-- b000963 | prose | pages [14] -->
.0 541

<!-- b000964 | prose | pages [14] -->
 

<!-- b000965 | prose | pages [14] -->
.1 .1 000 .1 240

<!-- b000966 | prose | pages [14] -->
.1 134 .0 491 .1 134 .0 688

<!-- b000967 | prose | pages [14] -->
.0 515

<!-- b000968 | prose | pages [14] -->


<!-- b000969 | prose | pages [14] -->
.0 .0 806 .1 000

<!-- b000970 | prose | pages [14] -->
.0 904 .0 439 .0 904 .0 590

<!-- b000971 | prose | pages [14] -->
.0 459

<!-- b000972 | prose | pages [14] -->
 

<!-- b000973 | prose | pages [14] -->
.0 .0 882 .1 106

<!-- b000974 | prose | pages [14] -->
.1 000 .0 461 .1 002 .0 630

<!-- b000975 | prose | pages [14] -->
.0 482

<!-- b000976 | prose | pages [14] -->
 

<!-- b000977 | prose | pages [14] -->
.2 .2 036 .2 277

<!-- b000978 | prose | pages [14] -->
.2 169 .1 000 .5 687 .3 335

<!-- b000979 | prose | pages [14] -->
.1 389

<!-- b000980 | prose | pages [14] -->


<!-- b000981 | prose | pages [14] -->
.0 .0 881 .1 106

<!-- b000982 | prose | pages [14] -->
.0 998 .0 176 .1 000 .0 630

<!-- b000983 | prose | pages [14] -->
.0 482

<!-- b000984 | prose | pages [14] -->
 

<!-- b000985 | prose | pages [14] -->
.1 .1 454 .1 694

<!-- b000986 | prose | pages [14] -->
.1 586 .0 300 .1 586 .1 000

<!-- b000987 | prose | pages [14] -->
.0 673

<!-- b000988 | prose | pages [14] -->
 

<!-- b000989 | prose | pages [14] -->
.1 .1 940 .2 181 .2 073 .0 720 .2 073 .1 486 .1 000

<!-- b000990 | prose | pages [14] -->


<!-- b000991 | prose | pages [14] -->


<!-- b000992 | prose | pages [14] -->
And using the model AHP-FCE, calculate the weight of Judgment Matrix B above.

<!-- b000993 | prose | pages [14] -->
The initial range of each weight all is [ ]1,0 . Finally based on the related properties of

<!-- b000994 | prose | pages [14] -->
Judgment Matrix, calculate the weight for each metrics shown as table 2.

<!-- b000995 | caption | pages [14] -->
Table 2   The weight for each metrics

<!-- b000996 | prose | pages [14] -->
Metrics 1 2 3

<!-- b000997 | prose | pages [14] -->
Weight 0.037 0.035 0.076 Metrics 8 9 10

<!-- b000998 | prose | pages [14] -->
Weight 0.053 0.057 0.151

<!-- b000999 | prose | pages [14] -->
Consistency test

<!-- b001000 | prose | pages [14] -->
4 5 6 7

<!-- b001001 | prose | pages [14] -->
0.109 0.085 0.067 0.062 11 12 13

<!-- b001002 | furniture | pages [14] -->


<!-- b001003 | prose | pages [14] -->
0.071 0.082 0.115

<!-- b001004 | furniture | pages [14] -->


<!-- b001005 | prose | pages [14] -->
 As the model, d stands for Non-negative parameter, and , in this paper d [ 5.0,0 ]

<!-- b001006 | prose | pages [14] -->
named parameter d=0.2. Then using lingo9.0 solve the single objective linear

<!-- b001007 | prose | pages [14] -->
programming model of formula (7) that

<!-- b001008 | prose | pages [14] -->
min CIC ( n )   

<!-- b001009 | furniture | pages [14] -->


<!-- b001010 | prose | pages [14] -->
.0 032 1.0

<!-- b001011 | prose | pages [14] -->
So it means the Judgment Matrix has a satisfactory consistency.

<!-- b001012 | prose | pages [14] -->
The composite score

<!-- b001013 | prose | pages [14] -->
 wi ( i 3,2,1 n ) with relative membership degree Combined the weight  into s (i )

<!-- b001014 | prose | pages [14] -->
formula (8), get the coach Fuzzy Evaluation composite score

<!-- b001015 | prose | pages [14] -->


<!-- b001016 | prose | pages [14] -->


<!-- b001017 | prose | pages [14] -->
z

<!-- b001018 | prose | pages [14] -->
(

<!-- b001019 | prose | pages [14] -->
j

<!-- b001020 | prose | pages [14] -->
)

<!-- b001021 | furniture | pages [14] -->


<!-- b001022 | prose | pages [14] -->
. z ( j )

<!-- b001023 | prose | pages [14] -->
n n

<!-- b001024 | prose | pages [14] -->
w r

<!-- b001025 | prose | pages [14] -->
(

<!-- b001026 | prose | pages [14] -->
i

<!-- b001027 | prose | pages [14] -->
,

<!-- b001028 | prose | pages [14] -->
j

<!-- b001029 | prose | pages [14] -->
)

<!-- b001030 | furniture | pages [14] -->


<!-- b001031 | prose | pages [14] -->
i

<!-- b001032 | prose | pages [14] -->
 

<!-- b001033 | prose | pages [14] -->
i i

<!-- b001034 | prose | pages [14] -->
1 1

<!-- b001035 | prose | pages [14] -->
12 12

<!-- b001036 | furniture | pages [15] -->
Team#28875                                                                      Page 13 of 33

<!-- b001037 | prose | pages [15] -->
Then using EXCEL to calculate the composite score

<!-- b001038 | heading | pages [15] -->
5 coaches in NCAA Basketball as table 3.

<!-- b001039 | prose | pages [15] -->
, list AHP-FCE model’s top z ( j )

<!-- b001040 | caption | pages [15] -->
Table 3   AHP-FCE model’s top 5 coaches in NCAA Basketball

<!-- b001041 | prose | pages [15] -->
Rank Coach 1

<!-- b001042 | prose | pages [15] -->
Dean Smith

<!-- b001043 | prose | pages [15] -->
2 Composite score

<!-- b001044 | prose | pages [15] -->
0.774

<!-- b001045 | prose | pages [15] -->
Mike Krzyzewski

<!-- b001046 | prose | pages [15] -->
3

<!-- b001047 | prose | pages [15] -->
Roy Williams

<!-- b001048 | prose | pages [15] -->
4

<!-- b001049 | prose | pages [15] -->
Rick Pitino

<!-- b001050 | prose | pages [15] -->
5

<!-- b001051 | prose | pages [15] -->
Jim Calhou

<!-- b001052 | heading | pages [15] -->
Testing Conclusion

<!-- b001053 | prose | pages [15] -->
0.755

<!-- b001054 | prose | pages [15] -->
0.658 0.635

<!-- b001055 | prose | pages [15] -->
0.613

<!-- b001056 | heading | pages [15] -->
Checking the AHP-FCE model’s result above with the College basketball's 25 most

<!-- b001057 | prose | pages [15] -->
intriguing coaches [26] and Ranking the Top 25 Coaches in College Basketball Today [27], we can easily find that the number 5 Jim Calhou even not rank in the both Top 25. And someone like John Wooden, won ten NCAA national championships in a 12-year period—seven in a row [28]— an unprecedented feat, Bob Knight, led his teams to three NCAA championships, one National Invitation Tournament (NIT) championship, and 11 Big Ten Conference championships [29], and Don Haskins, won 14 Western Athletic Conference championships and four WAC tournament titles, had fourteen NCAA tournament berths and made seven trips to the NIT [30], and so on, all not rank in this model’s top 5. So we validate the model result isn’t very accurately. The reason why the AHP-FCE works not very well is list as follow.

<!-- b001058 | prose | pages [15] -->
 In this model, the metrics is too many almost 13 large than the maximum

<!-- b001059 | prose | pages [15] -->
Judgment Matrix moment 9. So we need separate the metrics into 2 or more levels, to analytic hierarchy process more accurate.

<!-- b001060 | prose | pages [15] -->
 The Judgment Matrix which maximum moment is 9. When the metrics is just

<!-- b001061 | prose | pages [15] -->
large a lot than 9, such as 10, 11, this model will work not very well. So we need improve this model to handle the larger metrics.

<!-- b001062 | prose | pages [15] -->
 This calculation is too complicated specifically calculate the Judgment Matrix

<!-- b001063 | prose | pages [15] -->
and the weight. We need simplify the calculation.

<!-- b001064 | prose | pages [15] -->
Because of the shortcomings of model AHP-FCE, we must improve this model into a better one to handle the larger metrics and simplify the calculation. We named it IAHP-FCE Model.

<!-- b001065 | heading | pages [15] -->
Improving the model

<!-- b001066 | prose | pages [15] -->
Based on the AHP-FCE model, we improved this into a better one named IAHP-FCE Model to simplify the calculation and handle the larger metrics. We quote a Classification of Evaluation metrics to separate the metrics into 2 or more levels, obtain the metrics system for assessment.

<!-- b001067 | furniture | pages [15] -->


<!-- b001068 | prose | pages [15] -->
13 13

<!-- b001069 | furniture | pages [16] -->
Team#28875                                                                      Page 14 of 33

<!-- b001070 | prose | pages [16] -->
Determine the metrics system for assessment

<!-- b001071 | prose | pages [16] -->
Build any metrics system must follow certain principles, in order to achieve a reasonable, powerful and evidence construction of the metrics system. In this paper, following the following three basic principles: Comprehensive, Representative and Operability. [31]A simple metrics system for assessment is as follow Figure 4.

<!-- b001072 | furniture | pages [16] -->


<!-- b001073 | prose | pages [16] -->
Goal

<!-- b001074 | furniture | pages [16] -->


<!-- b001075 | furniture | pages [16] -->


<!-- b001076 | prose | pages [16] -->
Classification 1 Classification 2

<!-- b001077 | furniture | pages [16] -->


<!-- b001078 | furniture | pages [16] -->


<!-- b001079 | furniture | pages [16] -->


<!-- b001080 | prose | pages [16] -->
Classification 3

<!-- b001081 | prose | pages [16] -->
M 5 M 1 M 2 M 3 M 4 M 5 M 6 M 7 M 8

<!-- b001082 | furniture | pages [16] -->


<!-- b001083 | furniture | pages [16] -->


<!-- b001084 | prose | pages [16] -->
                                             

<!-- b001085 | caption | pages [16] -->
Figure 4  A simple metrics system for assessment.

<!-- b001086 | prose | pages [16] -->
As shown in Figure 1, the first level is Classifications [24], the second is metrics and

<!-- b001087 | prose | pages [16] -->
the final is the Goal.

<!-- b001088 | prose | pages [16] -->
Determine the weight

<!-- b001089 | prose | pages [16] -->
According to the metrics system and the AHP-FCE model, we construct the Judgment Matrix, and calculate the weight list as follow table4.

<!-- b001090 | caption | pages [16] -->
Table 4  The Weight of the two level metrics

<!-- b001091 | prose | pages [16] -->
Weight  The second level metrics The first level metrics

<!-- b001092 | prose | pages [16] -->
A1  Classification 1

<!-- b001093 | prose | pages [16] -->
W1

<!-- b001094 | furniture | pages [16] -->


<!-- b001095 | furniture | pages [16] -->


<!-- b001096 | furniture | pages [16] -->


<!-- b001097 | furniture | pages [16] -->


<!-- b001098 | furniture | pages [16] -->


<!-- b001099 | furniture | pages [16] -->


<!-- b001100 | furniture | pages [16] -->


<!-- b001101 | furniture | pages [16] -->


<!-- b001102 | prose | pages [16] -->
A2  Classification 2

<!-- b001103 | prose | pages [16] -->
W2

<!-- b001104 | furniture | pages [16] -->


<!-- b001105 | furniture | pages [16] -->


<!-- b001106 | furniture | pages [16] -->


<!-- b001107 | furniture | pages [16] -->


<!-- b001108 | furniture | pages [16] -->


<!-- b001109 | furniture | pages [16] -->


<!-- b001110 | furniture | pages [16] -->


<!-- b001111 | furniture | pages [16] -->


<!-- b001112 | furniture | pages [16] -->


<!-- b001113 | prose | pages [16] -->
weight

<!-- b001114 | prose | pages [16] -->
B1      metric 1

<!-- b001115 | prose | pages [16] -->
w1

<!-- b001116 | prose | pages [16] -->
B2      metric 2

<!-- b001117 | prose | pages [16] -->
w2

<!-- b001118 | prose | pages [16] -->
B3      metric 3

<!-- b001119 | prose | pages [16] -->
w3

<!-- b001120 | prose | pages [16] -->


<!-- b001121 | prose | pages [16] -->


<!-- b001122 | prose | pages [16] -->
Bx      metric x

<!-- b001123 | prose | pages [16] -->
wx

<!-- b001124 | prose | pages [16] -->
Bx+1    metric x+1

<!-- b001125 | prose | pages [16] -->
wx+1

<!-- b001126 | prose | pages [16] -->
Bx+2    metric x+2

<!-- b001127 | prose | pages [16] -->
wx+2

<!-- b001128 | prose | pages [16] -->
Bx+3    metric x+3

<!-- b001129 | prose | pages [16] -->
wx+3

<!-- b001130 | prose | pages [16] -->


<!-- b001131 | prose | pages [16] -->


<!-- b001132 | prose | pages [16] -->
By      metric y

<!-- b001133 | prose | pages [16] -->
wy

<!-- b001134 | prose | pages [16] -->
14 14

<!-- b001135 | furniture | pages [17] -->
Team#28875                                                                      Page 15 of 33

<!-- b001136 | prose | pages [17] -->
A2  Classification 3

<!-- b001137 | prose | pages [17] -->
W3

<!-- b001138 | furniture | pages [17] -->


<!-- b001139 | furniture | pages [17] -->


<!-- b001140 | furniture | pages [17] -->


<!-- b001141 | furniture | pages [17] -->


<!-- b001142 | furniture | pages [17] -->


<!-- b001143 | furniture | pages [17] -->


<!-- b001144 | furniture | pages [17] -->


<!-- b001145 | furniture | pages [17] -->


<!-- b001146 | prose | pages [17] -->
 

<!-- b001147 | prose | pages [17] -->
The final composite score

<!-- b001148 | prose | pages [17] -->
By+1    metric y+1

<!-- b001149 | prose | pages [17] -->
wy+1

<!-- b001150 | prose | pages [17] -->
By+2    metric y+2

<!-- b001151 | prose | pages [17] -->
wy+2

<!-- b001152 | prose | pages [17] -->
By+3    metric y+3

<!-- b001153 | prose | pages [17] -->
wy+3

<!-- b001154 | prose | pages [17] -->


<!-- b001155 | prose | pages [17] -->


<!-- b001156 | prose | pages [17] -->
Bn      metric n

<!-- b001157 | prose | pages [17] -->
wn

<!-- b001158 | prose | pages [17] -->
 

<!-- b001159 | prose | pages [17] -->
Combined with the weight of each metrics and the formula (8), respectively

<!-- b001160 | prose | pages [17] -->
w of each second level metrics for corresponding first level calculate the weight i

<!-- b001161 | prose | pages [17] -->
classifications. We obtained the coach Fuzzy Evaluation composite score , and zi ( j ) and the weight of each corresponding first level multiply and accumulate zi ( j )

<!-- b001162 | prose | pages [17] -->
classifications, then got the final Fuzzy Evaluation composite score

<!-- b001163 | prose | pages [17] -->
y

<!-- b001164 | prose | pages [17] -->
x

<!-- b001165 | prose | pages [17] -->
     

<!-- b001166 | prose | pages [17] -->
Z

<!-- b001167 | prose | pages [17] -->
(

<!-- b001168 | prose | pages [17] -->
j

<!-- b001169 | prose | pages [17] -->
)

<!-- b001170 | prose | pages [17] -->
W z

<!-- b001171 | prose | pages [17] -->
(

<!-- b001172 | prose | pages [17] -->
j

<!-- b001173 | prose | pages [17] -->
)

<!-- b001174 | prose | pages [17] -->
W z

<!-- b001175 | furniture | pages [17] -->


<!-- b001176 | prose | pages [17] -->
1

<!-- b001177 | prose | pages [17] -->
i

<!-- b001178 | prose | pages [17] -->
2

<!-- b001179 | prose | pages [17] -->
  

<!-- b001180 | prose | pages [17] -->
i

<!-- b001181 | prose | pages [17] -->
1

<!-- b001182 | prose | pages [17] -->
i x

<!-- b001183 | prose | pages [17] -->
1

<!-- b001184 | heading | pages [17] -->
Using the IAHP-FCE model

<!-- b001185 | prose | pages [17] -->
. z ( j )

<!-- b001186 | prose | pages [17] -->
n

<!-- b001187 | prose | pages [17] -->
   

<!-- b001188 | prose | pages [17] -->
( (

<!-- b001189 | prose | pages [17] -->
j j

<!-- b001190 | prose | pages [17] -->
)

<!-- b001191 | prose | pages [17] -->
W z

<!-- b001192 | prose | pages [17] -->
(

<!-- b001193 | prose | pages [17] -->
j

<!-- b001194 | prose | pages [17] -->
)

<!-- b001195 | prose | pages [17] -->
（9）

<!-- b001196 | prose | pages [17] -->


<!-- b001197 | prose | pages [17] -->
i i

<!-- b001198 | prose | pages [17] -->
3 i

<!-- b001199 | prose | pages [17] -->
 

<!-- b001200 | prose | pages [17] -->
i y

<!-- b001201 | prose | pages [17] -->
1

<!-- b001202 | prose | pages [17] -->
We use the improved model to calculate the IAHP-FCE model’s top 5 coaches in NCAA Basketball，Football and Baseball. Present your model’s top 5 coaches in each of 3 different sports.

<!-- b001203 | heading | pages [17] -->
Model’s Top 5 coaches in NCAA Basketball

<!-- b001204 | prose | pages [17] -->
Based on the Delphi method [16] and mathematical statistic [17] ,we constructed the Basketball college coaches metrics system for assessment as follow figure 5.

<!-- b001205 | prose | pages [17] -->
The Best College Basketball Coach

<!-- b001206 | prose | pages [17] -->
Achievement Experience

<!-- b001207 | prose | pages [17] -->
AP

<!-- b001208 | prose | pages [17] -->
AP Final

<!-- b001209 | prose | pages [17] -->
Game

<!-- b001210 | prose | pages [17] -->
NCAA

<!-- b001211 | prose | pages [17] -->
Years

<!-- b001212 | prose | pages [17] -->
SRS

<!-- b001213 | prose | pages [17] -->
High

<!-- b001214 | prose | pages [17] -->
Competency

<!-- b001215 | prose | pages [17] -->
Champ NCAA

<!-- b001216 | prose | pages [17] -->
Final Fours

<!-- b001217 | prose | pages [17] -->
AP Pre

<!-- b001218 | prose | pages [17] -->
CREG

<!-- b001219 | prose | pages [17] -->
CTRN

<!-- b001220 | prose | pages [17] -->
SOS

<!-- b001221 | prose | pages [17] -->
WL％

<!-- b001222 | furniture | pages [17] -->


<!-- b001223 | caption | pages [17] -->
Figure 5   College coaches metrics system for assessment

<!-- b001224 | furniture | pages [17] -->


<!-- b001225 | prose | pages [17] -->
15 15

<!-- b001226 | furniture | pages [18] -->
Team#28875                                                                      Page 16 of 33

<!-- b001227 | prose | pages [18] -->
As shown in Figure 5, we determined Competency, Achievement and Experience as the first level metrics, and defined Final Fours, CTRN, CREG, SOS, WL％, SRS, AP High, AP Final , AP Pre, Champ NCAA , Game , NCAA and Years [18]as the second level metrics. Therefore clearly articulate our College coaches metrics system for assessment.

<!-- b001228 | prose | pages [18] -->
We separated the metrics into 2 levels, obtain the metrics system for assessment, there is 3 first levels, the second has 13. For second level under the 3 first levels, we used the fuzzy comprehensive evaluation model for solving the weight of second level. Thought processing the data, we get relevant metrics data for 39 coaches. From metrics 5 to metrics 8 are the smaller the superior type indicators. Then according to formula (2) to Calculating the relative membership degree, others are the bigger the superior type indicators. And others follow formula (1) to Calculating the relative membership degree. Thus the value of s (i from metrics 1 to 13 are 0.110、0.099、 ) ) 0.261、0.323、0.269、0.226、0.215、0.186、0.199、0.340、0.059、0.270、0.330.

<!-- b001229 | prose | pages [18] -->
For the Classification---- Experience

<!-- b001230 | prose | pages [18] -->
The Classification Experience, a total of 3 second level, the corresponding value of

<!-- b001231 | prose | pages [18] -->
 are 0.110、0.099、0.261. The relative degree of importance is s (i ) b 3 . m According to formula (4) obtain the Judgment Matrix B as follow.

<!-- b001232 | prose | pages [18] -->


<!-- b001233 | prose | pages [18] -->
.1 000

<!-- b001234 | prose | pages [18] -->


<!-- b001235 | prose | pages [18] -->


<!-- b001236 | prose | pages [18] -->
B

<!-- b001237 | prose | pages [18] -->
.0 880

<!-- b001238 | prose | pages [18] -->


<!-- b001239 | prose | pages [18] -->
1

<!-- b001240 | prose | pages [18] -->


<!-- b001241 | prose | pages [18] -->
.2 864

<!-- b001242 | prose | pages [18] -->


<!-- b001243 | prose | pages [18] -->


<!-- b001244 | prose | pages [18] -->
.1 .1 136 .0 349

<!-- b001245 | prose | pages [18] -->


<!-- b001246 | prose | pages [18] -->
.1 .1 000 .0 333

<!-- b001247 | furniture | pages [18] -->


<!-- b001248 | prose | pages [18] -->
 

<!-- b001249 | prose | pages [18] -->
.3 .3 000 .1 000

<!-- b001250 | prose | pages [18] -->


<!-- b001251 | prose | pages [18] -->
And using the model AHP-FCE, calculate the weight of Judgment Matrix B above.

<!-- b001252 | prose | pages [18] -->
The initial range of each weight all is [ ]1,0 . Finally based on the related properties of

<!-- b001253 | prose | pages [18] -->
Judgment Matrix, calculate the weight for each metrics shown as below.

<!-- b001254 | prose | pages [18] -->
1 .1 000

<!-- b001255 | prose | pages [18] -->
.1

<!-- b001256 | prose | pages [18] -->
  w [ 1   

<!-- b001257 | prose | pages [18] -->
136

<!-- b001258 | prose | pages [18] -->
.0 349

<!-- b001259 | prose | pages [18] -->
 

<!-- b001260 | prose | pages [18] -->
] .0 213

<!-- b001261 | prose | pages [18] -->
  

<!-- b001262 | prose | pages [18] -->
000

<!-- b001263 | prose | pages [18] -->
3

<!-- b001264 | prose | pages [18] -->
.1 000 .0 880 .2 864

<!-- b001265 | prose | pages [18] -->
.1 136 .1

<!-- b001266 | prose | pages [18] -->
1 .0 880

<!-- b001267 | prose | pages [18] -->
.1

<!-- b001268 | prose | pages [18] -->
  w [ 2    3

<!-- b001269 | prose | pages [18] -->
.1 000 .0 880 .2 864

<!-- b001270 | prose | pages [18] -->
.1 136 .1

<!-- b001271 | prose | pages [18] -->
1 .2 864

<!-- b001272 | prose | pages [18] -->
.3

<!-- b001273 | prose | pages [18] -->
  w [ 3   

<!-- b001274 | prose | pages [18] -->
.3 000

<!-- b001275 | prose | pages [18] -->
.0 349 .0 333 .1 000

<!-- b001276 | prose | pages [18] -->
000

<!-- b001277 | prose | pages [18] -->
.0 333

<!-- b001278 | prose | pages [18] -->
 

<!-- b001279 | prose | pages [18] -->
] .0 193

<!-- b001280 | prose | pages [18] -->
  

<!-- b001281 | prose | pages [18] -->
000 .3 000

<!-- b001282 | prose | pages [18] -->
.0 349 .0 333 .1 000

<!-- b001283 | prose | pages [18] -->
000

<!-- b001284 | prose | pages [18] -->
.1 000

<!-- b001285 | prose | pages [18] -->
 

<!-- b001286 | prose | pages [18] -->
] .0 594

<!-- b001287 | furniture | pages [18] -->


<!-- b001288 | prose | pages [18] -->
  

<!-- b001289 | prose | pages [18] -->
000

<!-- b001290 | prose | pages [18] -->
3

<!-- b001291 | prose | pages [18] -->
.1 000 .0 880 .2 864

<!-- b001292 | prose | pages [18] -->
.1 136 .1 .3 000

<!-- b001293 | prose | pages [18] -->
.0 349 .0 333 .1 000

<!-- b001294 | prose | pages [18] -->
We take the parameter d=0.2, and use lingo9.0 solve the single objective linear programming model of formula (7) and get,

<!-- b001295 | prose | pages [18] -->
min CIC  ( ( n n ) 1.0

<!-- b001296 | furniture | pages [18] -->


<!-- b001297 | prose | pages [18] -->
So it means the Judgment Matrix has a satisfactory consistency. Combined the

<!-- b001298 | prose | pages [18] -->
weight with relative membership degree into formula (8), get the coach Fuzzy

<!-- b001299 | prose | pages [18] -->
z 1 j ( ) Evaluation composite score .

<!-- b001300 | furniture | pages [18] -->


<!-- b001301 | prose | pages [18] -->
16 16

<!-- b001302 | furniture | pages [19] -->
Team#28875                                                                      Page 17 of 33

<!-- b001303 | prose | pages [19] -->
For the Classification---- Achievement and Competency

<!-- b001304 | prose | pages [19] -->
Similarly, we calculate them and get

<!-- b001305 | prose | pages [19] -->


<!-- b001306 | prose | pages [19] -->
.1 000 .0 592 .0

<!-- b001307 | prose | pages [19] -->


<!-- b001308 | prose | pages [19] -->
.1 690 .1 000 .1

<!-- b001309 | prose | pages [19] -->
 

<!-- b001310 | prose | pages [19] -->
.1 493 .0 835 .1

<!-- b001311 | prose | pages [19] -->


<!-- b001312 | prose | pages [19] -->
B

<!-- b001313 | prose | pages [19] -->


<!-- b001314 | prose | pages [19] -->
2

<!-- b001315 | prose | pages [19] -->
.1 842 .1 150 .1

<!-- b001316 | prose | pages [19] -->
 

<!-- b001317 | prose | pages [19] -->
.2 000 .1 311 .1

<!-- b001318 | prose | pages [19] -->


<!-- b001319 | prose | pages [19] -->


<!-- b001320 | prose | pages [19] -->


<!-- b001321 | prose | pages [19] -->
.1 000 .1 007 .0

<!-- b001322 | prose | pages [19] -->


<!-- b001323 | prose | pages [19] -->
.0 993 .1 000 .0

<!-- b001324 | prose | pages [19] -->
 

<!-- b001325 | prose | pages [19] -->
.1 352 .1 359 .1

<!-- b001326 | prose | pages [19] -->


<!-- b001327 | prose | pages [19] -->
B

<!-- b001328 | prose | pages [19] -->


<!-- b001329 | prose | pages [19] -->
3

<!-- b001330 | prose | pages [19] -->
.1 502 .1 509 .1

<!-- b001331 | prose | pages [19] -->
 

<!-- b001332 | prose | pages [19] -->
.1 993 .1 950 .1

<!-- b001333 | prose | pages [19] -->


<!-- b001334 | prose | pages [19] -->


<!-- b001335 | prose | pages [19] -->


<!-- b001336 | prose | pages [19] -->
670 .0 543

<!-- b001337 | prose | pages [19] -->
.0 500

<!-- b001338 | prose | pages [19] -->


<!-- b001339 | prose | pages [19] -->
197 .0 870

<!-- b001340 | prose | pages [19] -->
.0 763

<!-- b001341 | prose | pages [19] -->
 

<!-- b001342 | prose | pages [19] -->
000 .0 742

<!-- b001343 | prose | pages [19] -->
.0 664

<!-- b001344 | furniture | pages [19] -->


<!-- b001345 | prose | pages [19] -->


<!-- b001346 | prose | pages [19] -->
347 .1 000

<!-- b001347 | prose | pages [19] -->
.0 862

<!-- b001348 | prose | pages [19] -->
 

<!-- b001349 | prose | pages [19] -->
507 .1 600 .1 000

<!-- b001350 | prose | pages [19] -->


<!-- b001351 | prose | pages [19] -->


<!-- b001352 | prose | pages [19] -->


<!-- b001353 | prose | pages [19] -->
740 .0 666

<!-- b001354 | prose | pages [19] -->
.0 502

<!-- b001355 | prose | pages [19] -->


<!-- b001356 | prose | pages [19] -->
736 .0 663

<!-- b001357 | prose | pages [19] -->
.0 513

<!-- b001358 | prose | pages [19] -->
 

<!-- b001359 | prose | pages [19] -->
000 .0 870

<!-- b001360 | prose | pages [19] -->
.0 609

<!-- b001361 | furniture | pages [19] -->


<!-- b001362 | prose | pages [19] -->


<!-- b001363 | prose | pages [19] -->
150 .1 000

<!-- b001364 | prose | pages [19] -->
.0 671

<!-- b001365 | prose | pages [19] -->
 

<!-- b001366 | prose | pages [19] -->
641 .1 491 .1 000

<!-- b001367 | prose | pages [19] -->


<!-- b001368 | prose | pages [19] -->


<!-- b001369 | prose | pages [19] -->
The weight of each level is shown as Table 5.

<!-- b001370 | caption | pages [19] -->
Table 5   The weight of Classification Achievement and Competency.

<!-- b001371 | prose | pages [19] -->
Achievement

<!-- b001372 | prose | pages [19] -->
w w w w w 5 6 7 8 4

<!-- b001373 | prose | pages [19] -->
0.124 0.205 0.176 0.232 0.263

<!-- b001374 | prose | pages [19] -->
Competency

<!-- b001375 | prose | pages [19] -->
w w w w w 9 10 13 12 11

<!-- b001376 | prose | pages [19] -->
0.146 0.146 0.191 0.215 0.302

<!-- b001377 | prose | pages [19] -->
We take the parameter d=0.2, and use lingo9.0 solve the single objective linear

<!-- b001378 | prose | pages [19] -->
programming model of formula (7) and get,

<!-- b001379 | prose | pages [19] -->
min CIC ( n )    .0 014 1.0

<!-- b001380 | furniture | pages [19] -->


<!-- b001381 | prose | pages [19] -->
So it means the Judgment Matrix has a satisfactory consistency. Combined the

<!-- b001382 | prose | pages [19] -->
weight with relative membership degree into formula (8), get the coach Fuzzy

<!-- b001383 | prose | pages [19] -->
z 3 j ( z 2 j ( ) Evaluation composite score and ) ) . Through access to relevant information,

<!-- b001384 | prose | pages [19] -->
we set the Weights of 3 Classification Experience, Achievement and Competency are

<!-- b001385 | prose | pages [19] -->
0.35、0.4、0.25. Then got the coach Fuzzy Evaluation composite score

<!-- b001386 | prose | pages [19] -->
3

<!-- b001387 | prose | pages [19] -->
    

<!-- b001388 | prose | pages [19] -->
Z

<!-- b001389 | prose | pages [19] -->
(

<!-- b001390 | prose | pages [19] -->
j

<!-- b001391 | prose | pages [19] -->
)

<!-- b001392 | prose | pages [19] -->
W z

<!-- b001393 | prose | pages [19] -->
(

<!-- b001394 | prose | pages [19] -->
j

<!-- b001395 | prose | pages [19] -->
)

<!-- b001396 | furniture | pages [19] -->


<!-- b001397 | prose | pages [19] -->
1 i

<!-- b001398 | prose | pages [19] -->


<!-- b001399 | prose | pages [19] -->
i 1 i

<!-- b001400 | prose | pages [19] -->
8 8

<!-- b001401 | prose | pages [19] -->
13

<!-- b001402 | prose | pages [19] -->
   

<!-- b001403 | prose | pages [19] -->
W z

<!-- b001404 | prose | pages [19] -->
(

<!-- b001405 | prose | pages [19] -->
j

<!-- b001406 | prose | pages [19] -->
)

<!-- b001407 | prose | pages [19] -->
W z

<!-- b001408 | prose | pages [19] -->
(

<!-- b001409 | prose | pages [19] -->
j

<!-- b001410 | prose | pages [19] -->
)

<!-- b001411 | prose | pages [19] -->
2

<!-- b001412 | prose | pages [19] -->
i

<!-- b001413 | prose | pages [19] -->
3

<!-- b001414 | prose | pages [19] -->
i

<!-- b001415 | prose | pages [19] -->
  

<!-- b001416 | prose | pages [19] -->
4 4

<!-- b001417 | prose | pages [19] -->
i

<!-- b001418 | prose | pages [19] -->
9

<!-- b001419 | prose | pages [19] -->
Using EXCEL to calculate and obtain the model’s Top 5 coaches as Table 6.

<!-- b001420 | furniture | pages [19] -->


<!-- b001421 | furniture | pages [19] -->


<!-- b001422 | prose | pages [19] -->
17 17

<!-- b001423 | furniture | pages [20] -->
Team#28875                                                                      Page 18 of 33

<!-- b001424 | caption | pages [20] -->
Table 6   Model’s Top 5 coaches in NCAA Basketball

<!-- b001425 | prose | pages [20] -->
Composite score Rank Coach 1

<!-- b001426 | prose | pages [20] -->
Mike Krzyzewski

<!-- b001427 | prose | pages [20] -->
2

<!-- b001428 | prose | pages [20] -->
Dean Smith

<!-- b001429 | prose | pages [20] -->
3

<!-- b001430 | prose | pages [20] -->
John Wooden

<!-- b001431 | prose | pages [20] -->
4

<!-- b001432 | prose | pages [20] -->
Bob Knight

<!-- b001433 | prose | pages [20] -->
5

<!-- b001434 | prose | pages [20] -->
Roy Williams

<!-- b001435 | prose | pages [20] -->
Years

<!-- b001436 | prose | pages [20] -->
0.713513

<!-- b001437 | prose | pages [20] -->
1976-2014

<!-- b001438 | prose | pages [20] -->
0.703688

<!-- b001439 | prose | pages [20] -->
1962-1997

<!-- b001440 | prose | pages [20] -->
0.686056

<!-- b001441 | prose | pages [20] -->
1965-1975

<!-- b001442 | prose | pages [20] -->
0.669591

<!-- b001443 | prose | pages [20] -->
1966-2008

<!-- b001444 | prose | pages [20] -->
0.655007

<!-- b001445 | prose | pages [20] -->
1989-2014

<!-- b001446 | prose | pages [20] -->
Contrast with the result of ModelⅠ and Sports Illustrated, the College basketball's

<!-- b001447 | prose | pages [20] -->
25 most intriguing coaches, this Rank of IAHP-FCE model is more reliable.

<!-- b001448 | heading | pages [20] -->
Popularize the model to all possible sports

<!-- b001449 | prose | pages [20] -->
Owing to this model just need adjust the number of metrics and calculate their

<!-- b001450 | prose | pages [20] -->
weight, then multiply and accumulate the coach Fuzzy Evaluation composite

<!-- b001451 | prose | pages [20] -->
and the weight of each corresponding first level classifications, finally got score zi ( j )

<!-- b001452 | prose | pages [20] -->
the composite score of each coach. So that ranking the coach, and finding out the top

<!-- b001453 | prose | pages [20] -->
5 is easy. Using this model, we can popularize the model to all possible sports. In this

<!-- b001454 | prose | pages [20] -->
paper, popularize this model to the famous NCAA Football and NCAA Baseball.

<!-- b001455 | heading | pages [20] -->
Model’s Top 5 coaches in NCAA Football

<!-- b001456 | prose | pages [20] -->
Solving the IAHP-FCE model above, we separate the metrics into 2 levels, there

<!-- b001457 | prose | pages [20] -->
are 3 first levels, the second level has 13. Thought processing the data, we get relevant

<!-- b001458 | prose | pages [20] -->
metrics data for 76 coaches. From metrics 7 to metrics 9 are the smaller the superior

<!-- b001459 | prose | pages [20] -->
type indicators. Then according to formula (2) to calculate the relative membership

<!-- b001460 | prose | pages [20] -->
degree, others are the bigger the superior type indicators. And others follow formula

<!-- b001461 | prose | pages [20] -->
(1) to calculate the relative membership degree. Thus the value of from metrics s (i )

<!-- b001462 | prose | pages [20] -->
1 to 10 are 0.104、0.214、0.110、0.069、0.275、0.284、0.380、0.263、0.305、0.3.

<!-- b001463 | prose | pages [20] -->
b The relative degree of importance m

<!-- b001464 | prose | pages [20] -->
Judgment Matrix B as follow.

<!-- b001465 | prose | pages [20] -->


<!-- b001466 | prose | pages [20] -->
.1 000

<!-- b001467 | prose | pages [20] -->


<!-- b001468 | prose | pages [20] -->


<!-- b001469 | prose | pages [20] -->
B

<!-- b001470 | prose | pages [20] -->
.1 707

<!-- b001471 | prose | pages [20] -->


<!-- b001472 | prose | pages [20] -->
1

<!-- b001473 | prose | pages [20] -->


<!-- b001474 | prose | pages [20] -->
.1 036

<!-- b001475 | prose | pages [20] -->


<!-- b001476 | furniture | pages [20] -->


<!-- b001477 | prose | pages [20] -->
  3 3 ,according to formula (4) obtain the

<!-- b001478 | prose | pages [20] -->


<!-- b001479 | prose | pages [20] -->
.0 586 .0 970

<!-- b001480 | prose | pages [20] -->


<!-- b001481 | prose | pages [20] -->
.1 000 .1 670

<!-- b001482 | furniture | pages [20] -->


<!-- b001483 | prose | pages [20] -->
 

<!-- b001484 | prose | pages [20] -->
.0 600 .1 000

<!-- b001485 | prose | pages [20] -->


<!-- b001486 | prose | pages [20] -->
18 18

<!-- b001487 | furniture | pages [21] -->
Team#28875                                                                      Page 19 of 33

<!-- b001488 | prose | pages [21] -->


<!-- b001489 | prose | pages [21] -->
.1 000

<!-- b001490 | prose | pages [21] -->


<!-- b001491 | prose | pages [21] -->


<!-- b001492 | prose | pages [21] -->
B

<!-- b001493 | prose | pages [21] -->
.2 325

<!-- b001494 | prose | pages [21] -->


<!-- b001495 | prose | pages [21] -->
2

<!-- b001496 | prose | pages [21] -->


<!-- b001497 | prose | pages [21] -->
.2 383

<!-- b001498 | prose | pages [21] -->


<!-- b001499 | prose | pages [21] -->


<!-- b001500 | prose | pages [21] -->
.1 000

<!-- b001501 | prose | pages [21] -->


<!-- b001502 | prose | pages [21] -->
.0 571

<!-- b001503 | prose | pages [21] -->


<!-- b001504 | prose | pages [21] -->


<!-- b001505 | prose | pages [21] -->
B

<!-- b001506 | furniture | pages [21] -->


<!-- b001507 | prose | pages [21] -->


<!-- b001508 | prose | pages [21] -->
3

<!-- b001509 | prose | pages [21] -->
.0 675

<!-- b001510 | prose | pages [21] -->


<!-- b001511 | prose | pages [21] -->
.0 661

<!-- b001512 | prose | pages [21] -->


<!-- b001513 | prose | pages [21] -->


<!-- b001514 | prose | pages [21] -->
.0 430 .0 42

<!-- b001515 | prose | pages [21] -->


<!-- b001516 | prose | pages [21] -->
.1 000 .0 945

<!-- b001517 | furniture | pages [21] -->


<!-- b001518 | prose | pages [21] -->
 

<!-- b001519 | prose | pages [21] -->
.1 058 .1 000

<!-- b001520 | prose | pages [21] -->


<!-- b001521 | prose | pages [21] -->


<!-- b001522 | prose | pages [21] -->
.1 725 .1 482 .1 514

<!-- b001523 | prose | pages [21] -->


<!-- b001524 | prose | pages [21] -->
.1 000 .0 787 .0 808

<!-- b001525 | prose | pages [21] -->


<!-- b001526 | furniture | pages [21] -->


<!-- b001527 | prose | pages [21] -->


<!-- b001528 | prose | pages [21] -->
.1 270 .1 000 .1 032

<!-- b001529 | prose | pages [21] -->


<!-- b001530 | prose | pages [21] -->
.1 238 .0 969 .1 000

<!-- b001531 | prose | pages [21] -->


<!-- b001532 | prose | pages [21] -->
According the AHP-FCE, we construct the Judgment Matrix. The initial range of

<!-- b001533 | prose | pages [21] -->
. And based on the related properties of Judgment Matrix, each weight all is [ ]1,0

<!-- b001534 | prose | pages [21] -->
calculate d the weight list as follow table 7.

<!-- b001535 | caption | pages [21] -->
Table 7   The weight of Experience, Achievement and Competency.

<!-- b001536 | prose | pages [21] -->
Competency Experience

<!-- b001537 | prose | pages [21] -->
w w w w w 3 5 2 4 1

<!-- b001538 | prose | pages [21] -->
0.267 0.458 0.275 0.175 0.403

<!-- b001539 | prose | pages [21] -->
Achievement

<!-- b001540 | prose | pages [21] -->
w w w w w 10 6 7 8 9

<!-- b001541 | prose | pages [21] -->
0.422 0.344 0.189 0.237 0.230

<!-- b001542 | prose | pages [21] -->
We take the parameter d=0.2, and use lingo9.0 solve the single objective linear

<!-- b001543 | prose | pages [21] -->
programming model of formula (7), and get

<!-- b001544 | prose | pages [21] -->
min CIC ( n )   

<!-- b001545 | furniture | pages [21] -->


<!-- b001546 | prose | pages [21] -->
.0 051 1.0

<!-- b001547 | prose | pages [21] -->
So it means the Judgment Matrix has a satisfactory consistency. Combined the weight with relative membership degree into formula (8), get the coach Fuzzy

<!-- b001548 | prose | pages [21] -->
zi ( j ) . Through access to relevant information, we set the Evaluation composite score

<!-- b001549 | prose | pages [21] -->
Weights of 3 Classification Experience, Achievement and Competency are 0.35、0.4、 0.25. Then got the coach Fuzzy Evaluation composite score

<!-- b001550 | prose | pages [21] -->
3

<!-- b001551 | prose | pages [21] -->
8

<!-- b001552 | prose | pages [21] -->
    

<!-- b001553 | prose | pages [21] -->
Z

<!-- b001554 | prose | pages [21] -->
(

<!-- b001555 | prose | pages [21] -->
j

<!-- b001556 | prose | pages [21] -->
)

<!-- b001557 | prose | pages [21] -->
W z

<!-- b001558 | prose | pages [21] -->
(

<!-- b001559 | prose | pages [21] -->
j

<!-- b001560 | prose | pages [21] -->
)

<!-- b001561 | prose | pages [21] -->
1 i

<!-- b001562 | prose | pages [21] -->
 

<!-- b001563 | prose | pages [21] -->
i 1 i

<!-- b001564 | prose | pages [21] -->
13

<!-- b001565 | prose | pages [21] -->
   

<!-- b001566 | prose | pages [21] -->
W z

<!-- b001567 | prose | pages [21] -->
(

<!-- b001568 | prose | pages [21] -->
j

<!-- b001569 | prose | pages [21] -->
)

<!-- b001570 | prose | pages [21] -->
W z

<!-- b001571 | prose | pages [21] -->
(

<!-- b001572 | prose | pages [21] -->
j

<!-- b001573 | prose | pages [21] -->
)

<!-- b001574 | furniture | pages [21] -->


<!-- b001575 | prose | pages [21] -->
2

<!-- b001576 | prose | pages [21] -->
i

<!-- b001577 | prose | pages [21] -->
3

<!-- b001578 | prose | pages [21] -->
i

<!-- b001579 | prose | pages [21] -->


<!-- b001580 | prose | pages [21] -->
4 4

<!-- b001581 | prose | pages [21] -->
i

<!-- b001582 | prose | pages [21] -->
9

<!-- b001583 | prose | pages [21] -->
We used EXCEL to calculate and ranking the model’s Top 5 coaches as Table 8.

<!-- b001584 | caption | pages [21] -->
Table 8   Model’s Top 5 coaches in NCAA Football

<!-- b001585 | prose | pages [21] -->
Composite score Rank Coach 1

<!-- b001586 | prose | pages [21] -->
Joe Paterno

<!-- b001587 | prose | pages [21] -->
2

<!-- b001588 | prose | pages [21] -->
John Gagliardi

<!-- b001589 | prose | pages [21] -->
3

<!-- b001590 | prose | pages [21] -->
Bobby Dodd

<!-- b001591 | prose | pages [21] -->
4

<!-- b001592 | prose | pages [21] -->
Eddie Robinson

<!-- b001593 | prose | pages [21] -->
5

<!-- b001594 | prose | pages [21] -->
Bear Bryant

<!-- b001595 | furniture | pages [21] -->


<!-- b001596 | prose | pages [21] -->
Years

<!-- b001597 | prose | pages [21] -->
0.701

<!-- b001598 | prose | pages [21] -->
1966-2011

<!-- b001599 | prose | pages [21] -->
0.625

<!-- b001600 | prose | pages [21] -->
1949-2012

<!-- b001601 | prose | pages [21] -->
0.610

<!-- b001602 | prose | pages [21] -->
1945-1966

<!-- b001603 | prose | pages [21] -->
0.608

<!-- b001604 | prose | pages [21] -->
1941-1997

<!-- b001605 | prose | pages [21] -->
0.608

<!-- b001606 | prose | pages [21] -->
1945-1982

<!-- b001607 | prose | pages [21] -->
19 19

<!-- b001608 | furniture | pages [22] -->
Team#28875                                                                      Page 20 of 33

<!-- b001609 | heading | pages [22] -->
Model’s Top 5 coaches in NCAA Baseball

<!-- b001610 | prose | pages [22] -->
As an example of Male baseball coach, we solve the IAHP-FCE model above.

<!-- b001611 | prose | pages [22] -->
We can only find 3 evaluation metrics, the number is less, so we solve them through

<!-- b001612 | prose | pages [22] -->
modelⅠ. Thought processing the data, we get relevant metrics data for 69 coaches.

<!-- b001613 | prose | pages [22] -->
The 3 metrics are the bigger the superior type indicators. According to formula (1) to

<!-- b001614 | prose | pages [22] -->
calculate the relative membership degree, thus the value of

<!-- b001615 | prose | pages [22] -->
0.098. The relative degree of importance b

<!-- b001616 | prose | pages [22] -->
Judgment Matrix B

<!-- b001617 | prose | pages [22] -->


<!-- b001618 | prose | pages [22] -->
.1 000

<!-- b001619 | prose | pages [22] -->


<!-- b001620 | prose | pages [22] -->


<!-- b001621 | prose | pages [22] -->
B

<!-- b001622 | prose | pages [22] -->
.0 500

<!-- b001623 | prose | pages [22] -->
 

<!-- b001624 | prose | pages [22] -->
.0 965

<!-- b001625 | prose | pages [22] -->


<!-- b001626 | prose | pages [22] -->
are 0.100，0.045 and s (i )

<!-- b001627 | prose | pages [22] -->
 , According to formula (4) obtain the 2 m m

<!-- b001628 | prose | pages [22] -->


<!-- b001629 | prose | pages [22] -->
2 .1 036

<!-- b001630 | prose | pages [22] -->


<!-- b001631 | prose | pages [22] -->
.1 000 .0 510

<!-- b001632 | furniture | pages [22] -->


<!-- b001633 | prose | pages [22] -->
 

<!-- b001634 | prose | pages [22] -->
.1 964 .1 000

<!-- b001635 | prose | pages [22] -->


<!-- b001636 | prose | pages [22] -->
And using the model AHP-FCE, calculate the weight of Judgment Matrix B above.

<!-- b001637 | prose | pages [22] -->
The initial range of each weight all is [ ]1,0 . Finally based on the related properties of

<!-- b001638 | prose | pages [22] -->
Judgment Matrix, calculate the weight for each metrics shown as follow

<!-- b001639 | prose | pages [22] -->
1  2  w .0 405 w ， 3  w .0 393 .0 202 ，

<!-- b001640 | furniture | pages [22] -->


<!-- b001641 | prose | pages [22] -->
We take the parameter d=0.2, and use lingo9.0 solve the single objective linear

<!-- b001642 | prose | pages [22] -->
programming model of formula (7)

<!-- b001643 | prose | pages [22] -->
min CIC ( n )   

<!-- b001644 | furniture | pages [22] -->


<!-- b001645 | prose | pages [22] -->
.0 028 1.0

<!-- b001646 | prose | pages [22] -->
So it means the Judgment Matrix has a satisfactory consistency. Combined the

<!-- b001647 | prose | pages [22] -->
weight with relative membership degree into formula (8), get the coach Fuzzy

<!-- b001648 | prose | pages [22] -->
zi ( j ) .We used EXCEL to calculate and ranking the Evaluation composite score

<!-- b001649 | prose | pages [22] -->
model’s Top 5 coaches as table 9.

<!-- b001650 | caption | pages [22] -->
Table 9   Model’s Top 5 coaches in NCAA Baseball

<!-- b001651 | prose | pages [22] -->
Rank Coach 1

<!-- b001652 | prose | pages [22] -->
Gordie Gillespie Augie

<!-- b001653 | prose | pages [22] -->
2

<!-- b001654 | prose | pages [22] -->
Garrido

<!-- b001655 | prose | pages [22] -->
3

<!-- b001656 | prose | pages [22] -->
Chuck Hartman

<!-- b001657 | prose | pages [22] -->
4

<!-- b001658 | prose | pages [22] -->
Gene StephensonBill

<!-- b001659 | prose | pages [22] -->
5

<!-- b001660 | prose | pages [22] -->
Holowaty

<!-- b001661 | furniture | pages [22] -->


<!-- b001662 | prose | pages [22] -->
Composite score Years

<!-- b001663 | prose | pages [22] -->
0.748

<!-- b001664 | prose | pages [22] -->
1953-2003

<!-- b001665 | prose | pages [22] -->
0.661

<!-- b001666 | prose | pages [22] -->
1969-2014

<!-- b001667 | prose | pages [22] -->
0.612

<!-- b001668 | prose | pages [22] -->
1960-2006

<!-- b001669 | prose | pages [22] -->
0.592

<!-- b001670 | prose | pages [22] -->
1978-2013

<!-- b001671 | prose | pages [22] -->
0.577

<!-- b001672 | prose | pages [22] -->
1969-2012

<!-- b001673 | prose | pages [22] -->
20 20

<!-- b001674 | furniture | pages [23] -->
Team#28875                                                                      Page 21 of 33

<!-- b001675 | prose | pages [23] -->
Contrast with the result of Model’s Top 5 coaches of 3 College sports which include NCAA Basketball, Football and Baseball with the news report in Sports Illustrated, we can drew a conclusion that this IAHP-FCE model is trustworthy.

<!-- b001676 | heading | pages [23] -->
Applied the model across both genders

<!-- b001677 | prose | pages [23] -->
This model proofed can popularize to all possible sports, and now we applied the model across both genders. Taking into the differences between male and female coaches, we take women's basketball coaches as an example. Because the data of women's basketball coaches is less, we can only find 7 evaluation metrics, so we solve them through modelⅠ. Thought processing the data, we get relevant metrics data for 15 coaches. The 7 metrics are the bigger the superior type indicators. The are 0.066、0.080、0.111、0.299、0.225、0.284、0.047. The relative degree value of s (i )  . According to formula (4) obtain the Judgment Matrix B. of importance is b 2 m

<!-- b001678 | prose | pages [23] -->


<!-- b001679 | prose | pages [23] -->
.1 000 .0 782 .0 528

<!-- b001680 | prose | pages [23] -->
 

<!-- b001681 | prose | pages [23] -->
.1 278 .1 000 .0 619

<!-- b001682 | prose | pages [23] -->


<!-- b001683 | prose | pages [23] -->
.1 893 .1 616 .1 000

<!-- b001684 | prose | pages [23] -->


<!-- b001685 | prose | pages [23] -->


<!-- b001686 | prose | pages [23] -->


<!-- b001687 | prose | pages [23] -->
B

<!-- b001688 | prose | pages [23] -->
.5 632 .5 355 .4 740

<!-- b001689 | prose | pages [23] -->


<!-- b001690 | prose | pages [23] -->
.1 156 .3 878 .3 263

<!-- b001691 | prose | pages [23] -->
 

<!-- b001692 | prose | pages [23] -->
.5 326 .5 049 .4 434

<!-- b001693 | prose | pages [23] -->
 

<!-- b001694 | prose | pages [23] -->
.0 726 .0 604 .0 441

<!-- b001695 | prose | pages [23] -->


<!-- b001696 | prose | pages [23] -->


<!-- b001697 | prose | pages [23] -->
.0 .0 178

<!-- b001698 | prose | pages [23] -->
.0 241

<!-- b001699 | prose | pages [23] -->
.1 655

<!-- b001700 | prose | pages [23] -->
.1 378

<!-- b001701 | prose | pages [23] -->
 

<!-- b001702 | prose | pages [23] -->
.0 .0 187

<!-- b001703 | prose | pages [23] -->
.0 258

<!-- b001704 | prose | pages [23] -->
.0 198

<!-- b001705 | prose | pages [23] -->
.0 345

<!-- b001706 | prose | pages [23] -->


<!-- b001707 | prose | pages [23] -->
.0 .0 211

<!-- b001708 | prose | pages [23] -->
.0 306

<!-- b001709 | prose | pages [23] -->
.0 226

<!-- b001710 | prose | pages [23] -->
.2 270

<!-- b001711 | prose | pages [23] -->
 

<!-- b001712 | furniture | pages [23] -->


<!-- b001713 | prose | pages [23] -->
.1 .1 000

<!-- b001714 | prose | pages [23] -->
.2 469

<!-- b001715 | prose | pages [23] -->
.1 297

<!-- b001716 | prose | pages [23] -->
.7 767

<!-- b001717 | prose | pages [23] -->


<!-- b001718 | prose | pages [23] -->
.0 405 .1 000 .0 460

<!-- b001719 | prose | pages [23] -->
.4 525

<!-- b001720 | prose | pages [23] -->
 

<!-- b001721 | prose | pages [23] -->
.0 771 .2 172 .1 000

<!-- b001722 | prose | pages [23] -->
.5 714

<!-- b001723 | prose | pages [23] -->
 

<!-- b001724 | prose | pages [23] -->
.0 167 .0 221 .0 175

<!-- b001725 | prose | pages [23] -->
.1 000

<!-- b001726 | prose | pages [23] -->


<!-- b001727 | prose | pages [23] -->
And using the model AHP-FCE, calculate the weight of Judgment Matrix B above.

<!-- b001728 | prose | pages [23] -->
The initial range of each weight all is [ ]1,0 . Finally based on the related properties of

<!-- b001729 | prose | pages [23] -->
Judgment Matrix, calculate the weight of each metrics as table 10.

<!-- b001730 | caption | pages [23] -->
Table 10   The weight of each metrics

<!-- b001731 | prose | pages [23] -->
w w w 3 2 1 w w w w 5 6 7 4 4

<!-- b001732 | prose | pages [23] -->
0.314 0.088 0.045 0.073 0.173 0.268 0.038

<!-- b001733 | prose | pages [23] -->
We take the parameter d=0.2, and use lingo9.0 solve the single objective linear

<!-- b001734 | prose | pages [23] -->
programming model of formula (7) that

<!-- b001735 | prose | pages [23] -->
min CIC ( n )    .0 036 1.0

<!-- b001736 | furniture | pages [23] -->


<!-- b001737 | prose | pages [23] -->
So it means the Judgment Matrix has a satisfactory consistency. Combined the weight with relative membership degree into formula (8), get the coach Fuzzy

<!-- b001738 | prose | pages [23] -->
Evaluation composite score zi ( j ) . We used EXCEL to calculate and ranking the

<!-- b001739 | prose | pages [23] -->
model’s Top 5 coaches as Table 11.

<!-- b001740 | furniture | pages [23] -->


<!-- b001741 | prose | pages [23] -->
21 21

<!-- b001742 | furniture | pages [24] -->
Team#28875                                                                      Page 22 of 33

<!-- b001743 | caption | pages [24] -->
Table 11   Model’s Top 5 Woman coaches in NCAA Women's Basketball

<!-- b001744 | prose | pages [24] -->
Composite score Rank Coach 1

<!-- b001745 | prose | pages [24] -->
Pat Summitt

<!-- b001746 | prose | pages [24] -->
2

<!-- b001747 | prose | pages [24] -->
Tara VanDerveer

<!-- b001748 | prose | pages [24] -->
3

<!-- b001749 | prose | pages [24] -->
Nancy Fahey

<!-- b001750 | prose | pages [24] -->
4

<!-- b001751 | prose | pages [24] -->
Amy Ruley

<!-- b001752 | prose | pages [24] -->
5

<!-- b001753 | prose | pages [24] -->
Jody Conradt

<!-- b001754 | prose | pages [24] -->
Years

<!-- b001755 | prose | pages [24] -->
0.883

<!-- b001756 | prose | pages [24] -->
1974-2012

<!-- b001757 | prose | pages [24] -->
0.573

<!-- b001758 | prose | pages [24] -->
1978-1980

<!-- b001759 | prose | pages [24] -->
0.470

<!-- b001760 | prose | pages [24] -->
1998-2014

<!-- b001761 | prose | pages [24] -->
0.442

<!-- b001762 | prose | pages [24] -->
1980-2008

<!-- b001763 | prose | pages [24] -->
0.383

<!-- b001764 | prose | pages [24] -->
1969-1973

<!-- b001765 | prose | pages [24] -->
Using the model we also can get the NCAA women’s Basketball top 5 woman coaches. Juxtaposed with the reporter on the internet, obtained our result exist difference, but the rate of ranking top 5 is 100%. So we can draw a conclusion that this model also can apply the model across both genders.

<!-- b001766 | prose | pages [24] -->
Finding out the Best all time college coach

<!-- b001767 | prose | pages [24] -->
In NCAA the most famous sports ranking as football, basketball and baseball. We find out these best coaches and make the rank top 5 as table 12.

<!-- b001768 | caption | pages [24] -->
Table 12   The Top 5 Coaches of College

<!-- b001769 | prose | pages [24] -->
Composite score Rank Coach

<!-- b001770 | prose | pages [24] -->
Pat Summitt

<!-- b001771 | prose | pages [24] -->
1 2

<!-- b001772 | prose | pages [24] -->
Gordie Gillespie

<!-- b001773 | prose | pages [24] -->
3

<!-- b001774 | prose | pages [24] -->
Mike Krzyzewski

<!-- b001775 | prose | pages [24] -->
4

<!-- b001776 | prose | pages [24] -->
Dean Smith

<!-- b001777 | prose | pages [24] -->
5

<!-- b001778 | prose | pages [24] -->
Joe Paterno

<!-- b001779 | prose | pages [24] -->
College Sports

<!-- b001780 | prose | pages [24] -->
0.883

<!-- b001781 | prose | pages [24] -->
Women's Basketball

<!-- b001782 | prose | pages [24] -->
0.748

<!-- b001783 | prose | pages [24] -->
Baseball

<!-- b001784 | prose | pages [24] -->
0.713513

<!-- b001785 | prose | pages [24] -->
Basketball

<!-- b001786 | prose | pages [24] -->
0.703688

<!-- b001787 | prose | pages [24] -->
Basketball

<!-- b001788 | prose | pages [24] -->
0.701

<!-- b001789 | prose | pages [24] -->
Football

<!-- b001790 | prose | pages [24] -->
Comparing with their final composite score,

<!-- b001791 | prose | pages [24] -->
finally we obtain our model’s the Best all time

<!-- b001792 | prose | pages [24] -->
college coach. She is Pat Summitt which

<!-- b001793 | prose | pages [24] -->
final composite score high than 0.88.  Here

<!-- b001794 | heading | pages [24] -->
goes a brief introduction and figure 6 for our

<!-- b001795 | prose | pages [24] -->
Best all time college coach.

<!-- b001796 | prose | pages [24] -->
Patricia Sue "Pat" Summitt (born June 14,

<!-- b001797 | prose | pages [24] -->
college 1952) is a former women's

<!-- b001798 | prose | pages [24] -->
basketball head coach. She now serves as

<!-- b001799 | prose | pages [24] -->
the head coach emeritusof the Tennessee Lady Vols

<!-- b001800 | prose | pages [24] -->
basketball team. She holds the most all-time

<!-- b001801 | prose | pages [24] -->
wins for a coach in NCAA basketball history

<!-- b001802 | prose | pages [24] -->
of either a men's or women's team in any division.    Figure 6  Pat Summitt

<!-- b001803 | furniture | pages [24] -->


<!-- b001804 | prose | pages [24] -->
22 22

<!-- b001805 | furniture | pages [25] -->
Team#28875                                                                      Page 23 of 33

<!-- b001806 | prose | pages [25] -->
She coached from 1974 to 2012, all with the Lady Vols, winning eight NCAA national championships, second only to the record 10 titles won by UCLA men's coach John Wooden. She is the only coach in NCAA history, and one of three college coaches overall, with at least 1,000 victories.

<!-- b001807 | prose | pages [25] -->
The difference as the time line horizon

<!-- b001808 | prose | pages [25] -->
Considering the relationship between the coach's coaching and time, we randomly selected a few coaches and collected relational data, calculated the Evaluation composite score during the coaching, we used EXCEL to draw a line chart, analyzed the relationship between the time line and coaching.

<!-- b001809 | prose | pages [25] -->
In this paper we selected the data of male basketball coach Dean Smith's to analysis. According to the result of the model above, we get the weight of each evaluation metric. Then calculate the composite score of Dean Smith each year from 1961 to

<!-- b001810 | heading | pages [25] -->
1997 shown as table 13.

<!-- b001811 | caption | pages [25] -->
Table 13  The composite score of Dean Smith each year

<!-- b001812 | prose | pages [25] -->
year 1961 1962 1963 1964 score 0.455 0.440 0.468 0.398 year 1970 1971 1972 1973 score 0.459 0.545 0.494 0.485 year 1979 1980 1981 1982 score 0.473 0.501 0.598 0.562 year 1988 1989 1990 1991 score 0.569 0.510 0.575 0.495 1965 1966 1967 1968 1969 0.480 0.504 0.523 0.536 0.477 1974 1975 1976 1977 1978 0.466 0.513 0.539 0.511 0.474 1983 1984 1985 1986 1987 0.601 0.532 0.579 0.611 0.573 1992 1993 1994 1995 1996 0.596 0.668 0.601 0.404 0.563

<!-- b001813 | prose | pages [25] -->
The above table shows that in different year the composite score of Dean Smith is different on the whole. In order to show the effects of time on the coaching more intuitionally, we used EXCEL to draw a line chart of Time Line Horizon -Coaching as

<!-- b001814 | caption | pages [25] -->
figure 7.

<!-- b001815 | prose | pages [25] -->
The time line horizon-coaching

<!-- b001816 | prose | pages [25] -->
0.8

<!-- b001817 | prose | pages [25] -->
0.7

<!-- b001818 | prose | pages [25] -->
0.6

<!-- b001819 | prose | pages [25] -->
0.5

<!-- b001820 | prose | pages [25] -->
Coaching

<!-- b001821 | prose | pages [25] -->
0.4

<!-- b001822 | prose | pages [25] -->
0.3

<!-- b001823 | prose | pages [25] -->
0.2

<!-- b001824 | prose | pages [25] -->
0.1

<!-- b001825 | prose | pages [25] -->
0

<!-- b001826 | prose | pages [25] -->
1961

<!-- b001827 | prose | pages [25] -->
1963

<!-- b001828 | prose | pages [25] -->
1965

<!-- b001829 | prose | pages [25] -->
1967

<!-- b001830 | prose | pages [25] -->
1969

<!-- b001831 | prose | pages [25] -->
1971

<!-- b001832 | prose | pages [25] -->
1973

<!-- b001833 | prose | pages [25] -->
1975

<!-- b001834 | prose | pages [25] -->
1977

<!-- b001835 | prose | pages [25] -->
1979

<!-- b001836 | prose | pages [25] -->
1981

<!-- b001837 | prose | pages [25] -->
1983

<!-- b001838 | prose | pages [25] -->
1985

<!-- b001839 | prose | pages [25] -->
1987

<!-- b001840 | prose | pages [25] -->
1989

<!-- b001841 | prose | pages [25] -->
1991

<!-- b001842 | prose | pages [25] -->
1993

<!-- b001843 | prose | pages [25] -->
1995

<!-- b001844 | prose | pages [25] -->
Time line horizon

<!-- b001845 | furniture | pages [25] -->


<!-- b001846 | caption | pages [25] -->
Figure 7   The line chart for basketball coach Dean Smith

<!-- b001847 | furniture | pages [25] -->


<!-- b001848 | prose | pages [25] -->
23 23

<!-- b001849 | furniture | pages [26] -->
Team#28875                                                                      Page 24 of 33

<!-- b001850 | prose | pages [26] -->
With years of coaching increasing, Dean Smith coach's coaching is not the same

<!-- b001851 | prose | pages [26] -->
level, but change within a certain range, ups and downs, with uncertainty, but overall,

<!-- b001852 | prose | pages [26] -->
it is a slight upward trend.

<!-- b001853 | prose | pages [26] -->
Different gender of the same sports

<!-- b001854 | prose | pages [26] -->
In order to avoid accident, we randomly select more coaches from different sports,

<!-- b001855 | prose | pages [26] -->
different gender to study. Using the same method, we calculate the composite score of

<!-- b001856 | prose | pages [26] -->
each year, and draw a line chat of Time Line Horizon -Coaching as figure 8.

<!-- b001857 | prose | pages [26] -->
The time line horizon-coaching

<!-- b001858 | prose | pages [26] -->
0.6

<!-- b001859 | prose | pages [26] -->
0.5

<!-- b001860 | prose | pages [26] -->
0.4

<!-- b001861 | prose | pages [26] -->
Coaching

<!-- b001862 | prose | pages [26] -->
0.3

<!-- b001863 | prose | pages [26] -->
0.2

<!-- b001864 | prose | pages [26] -->
0.1

<!-- b001865 | prose | pages [26] -->
0

<!-- b001866 | prose | pages [26] -->
1974 1976 1978 1980 1982 1984 1986 1988 1990 1992 1994 1996 1998 2000 2002 2004 2006 2008 2010

<!-- b001867 | prose | pages [26] -->
Time line horizon

<!-- b001868 | furniture | pages [26] -->


<!-- b001869 | caption | pages [26] -->
Figure 8  The line chart for women’s basketball coach Pat Summitt

<!-- b001870 | prose | pages [26] -->
The figure compares with figure 7, we found the fluctuation range of women's

<!-- b001871 | prose | pages [26] -->
basketball coach coaching changed large, but the overall situation of change is

<!-- b001872 | prose | pages [26] -->
substantially the same. In order to avoid accident, we analyze the relationship time

<!-- b001873 | prose | pages [26] -->
line horizon and coaching between different sports and different gender. The results

<!-- b001874 | prose | pages [26] -->
similar to Figure 7, Figure 8, as to different gender of the same sports, time line

<!-- b001875 | prose | pages [26] -->
horizon makes a difference in coaching.

<!-- b001876 | furniture | pages [26] -->


<!-- b001877 | furniture | pages [26] -->


<!-- b001878 | furniture | pages [26] -->


<!-- b001879 | furniture | pages [26] -->


<!-- b001880 | prose | pages [26] -->
24 24

<!-- b001881 | furniture | pages [27] -->
Team#28875                                                                      Page 25 of 33

<!-- b001882 | prose | pages [27] -->
Different sports of the same gender

<!-- b001883 | prose | pages [27] -->
The time line horizon-coaching

<!-- b001884 | prose | pages [27] -->
0.8

<!-- b001885 | prose | pages [27] -->
0.7

<!-- b001886 | prose | pages [27] -->
0.6

<!-- b001887 | prose | pages [27] -->
0.5

<!-- b001888 | prose | pages [27] -->
coaching

<!-- b001889 | prose | pages [27] -->
0.4

<!-- b001890 | prose | pages [27] -->
0.3

<!-- b001891 | prose | pages [27] -->
0.2

<!-- b001892 | prose | pages [27] -->
0.1

<!-- b001893 | prose | pages [27] -->
0

<!-- b001894 | prose | pages [27] -->
1966

<!-- b001895 | prose | pages [27] -->
1969

<!-- b001896 | prose | pages [27] -->
1972

<!-- b001897 | prose | pages [27] -->
1975

<!-- b001898 | prose | pages [27] -->
1978

<!-- b001899 | prose | pages [27] -->
1981

<!-- b001900 | prose | pages [27] -->
1984

<!-- b001901 | prose | pages [27] -->
1987

<!-- b001902 | prose | pages [27] -->
1990

<!-- b001903 | prose | pages [27] -->
1993

<!-- b001904 | prose | pages [27] -->
1996

<!-- b001905 | prose | pages [27] -->
1999

<!-- b001906 | prose | pages [27] -->
2002

<!-- b001907 | prose | pages [27] -->
2005

<!-- b001908 | prose | pages [27] -->
2008

<!-- b001909 | prose | pages [27] -->
2011

<!-- b001910 | prose | pages [27] -->
Time line horizon

<!-- b001911 | furniture | pages [27] -->


<!-- b001912 | caption | pages [27] -->
Figure 9  The line chart for football coach Joe Paterno

<!-- b001913 | prose | pages [27] -->
The figure compares with figure 7, we found the overall situation of change is substantially the same. In order to avoid accident, we analyze the relationship time line horizon and coaching between different sports and same gender. The results similar to Figure 7, Figure 9, as to different sport of the same gender, time line horizon makes a difference in coaching.

<!-- b001914 | prose | pages [27] -->
Same sports of the same gender

<!-- b001915 | prose | pages [27] -->
The time line horizon-coaching

<!-- b001916 | prose | pages [27] -->
0.8

<!-- b001917 | prose | pages [27] -->
0.7

<!-- b001918 | prose | pages [27] -->
0.6

<!-- b001919 | prose | pages [27] -->
0.5

<!-- b001920 | prose | pages [27] -->
coaching

<!-- b001921 | prose | pages [27] -->
0.4

<!-- b001922 | prose | pages [27] -->
0.3

<!-- b001923 | prose | pages [27] -->
0.2

<!-- b001924 | prose | pages [27] -->
0.1

<!-- b001925 | prose | pages [27] -->
0

<!-- b001926 | prose | pages [27] -->
1970

<!-- b001927 | prose | pages [27] -->
1973

<!-- b001928 | prose | pages [27] -->
1976

<!-- b001929 | prose | pages [27] -->
1979

<!-- b001930 | prose | pages [27] -->
1982

<!-- b001931 | prose | pages [27] -->
1985

<!-- b001932 | prose | pages [27] -->
1988

<!-- b001933 | prose | pages [27] -->
1991

<!-- b001934 | prose | pages [27] -->
1994

<!-- b001935 | prose | pages [27] -->
1997

<!-- b001936 | prose | pages [27] -->
2000

<!-- b001937 | prose | pages [27] -->
2003

<!-- b001938 | prose | pages [27] -->
2006

<!-- b001939 | prose | pages [27] -->
2009

<!-- b001940 | prose | pages [27] -->
Time line horizon

<!-- b001941 | furniture | pages [27] -->


<!-- b001942 | caption | pages [27] -->
Figure 10  The line chart for football coach Bobby Bowden

<!-- b001943 | furniture | pages [27] -->


<!-- b001944 | furniture | pages [27] -->


<!-- b001945 | furniture | pages [27] -->


<!-- b001946 | prose | pages [27] -->
25 25

<!-- b001947 | furniture | pages [28] -->
Team#28875                                                                      Page 26 of 33

<!-- b001948 | prose | pages [28] -->
The figure compares with figure 9, we found the overall situation of change is substantially the same. In order to avoid accident, we analyze the relationship time line horizon and coaching between same sports and same gender. The results similar to Figure 9, Figure 10, as to same sport of the same gender, time line horizon makes a difference in coaching.

<!-- b001949 | heading | pages [28] -->
Conclusion

<!-- b001950 | prose | pages [28] -->
Through analyzing the coach’ career coaching and the time line horizon from different gender of same sports, different sports of same gender, same sports and same gender, we find time line horizon can make a difference in coaching. In different time, coaches’ coaching is different on the whole, but change within a certain range, and from the whole, coaching growth with years increase, it is a slight upward trend. It can be seen, it made a difference which time line horizon that we use in our analysis.

<!-- b001951 | heading | pages [28] -->
Modeling test

<!-- b001952 | prose | pages [28] -->
Finally, we tested the model from dimensional consistency test, model and model solution deviation test, reasonable hypothesis test and sensitivity analysis of the model parameters of these 4 aspects.

<!-- b001953 | prose | pages [28] -->
Dimensional consistency test

<!-- b001954 | prose | pages [28] -->
When we collected data we standardized all of them, so that dimension tends consistency.

<!-- b001955 | heading | pages [28] -->
Model and model solution deviation test

<!-- b001956 | prose | pages [28] -->
Through establishing model Ⅰand model Ⅱ, we calculated comprehensive evaluation score of each college coaches nearly a century, by comparison, we found “best all time college coach”. By solving the model we got our model’s top 5 coaches in each of 3 different sports. We compared the top five coaches with the relevant Official Website recognized in various fields, comparison table as below table 14.

<!-- b001957 | caption | pages [28] -->
Table 14  Basketball Coaches

<!-- b001958 | prose | pages [28] -->
Rank 1 2 Solving the

<!-- b001959 | prose | pages [28] -->
Mike

<!-- b001960 | prose | pages [28] -->
Dean

<!-- b001961 | prose | pages [28] -->
model drawn

<!-- b001962 | prose | pages [28] -->
Krzyzewski

<!-- b001963 | prose | pages [28] -->
Smith

<!-- b001964 | prose | pages [28] -->
coach list

<!-- b001965 | prose | pages [28] -->
Coaches List

<!-- b001966 | prose | pages [28] -->
John

<!-- b001967 | prose | pages [28] -->
Dean

<!-- b001968 | prose | pages [28] -->
published on

<!-- b001969 | prose | pages [28] -->
Wooden

<!-- b001970 | prose | pages [28] -->
Smith

<!-- b001971 | prose | pages [28] -->
the website

<!-- b001972 | prose | pages [28] -->
3 4 5

<!-- b001973 | prose | pages [28] -->
John

<!-- b001974 | prose | pages [28] -->
Bob

<!-- b001975 | prose | pages [28] -->
Roy

<!-- b001976 | prose | pages [28] -->
Wooden

<!-- b001977 | prose | pages [28] -->
Knight

<!-- b001978 | prose | pages [28] -->
Williams

<!-- b001979 | prose | pages [28] -->
Mike

<!-- b001980 | prose | pages [28] -->
Roy

<!-- b001981 | prose | pages [28] -->
Bob

<!-- b001982 | prose | pages [28] -->
Krzyzewski

<!-- b001983 | prose | pages [28] -->
Williams

<!-- b001984 | prose | pages [28] -->
Knight

<!-- b001985 | prose | pages [28] -->
Above table shows, the result is different to the authority rank of basketball coach. The same rate is up to 100%, thus the model deviation is smaller.

<!-- b001986 | furniture | pages [28] -->


<!-- b001987 | furniture | pages [28] -->


<!-- b001988 | prose | pages [28] -->
26 26

<!-- b001989 | furniture | pages [29] -->
Team#28875                                                                      Page 27 of 33

<!-- b001990 | caption | pages [29] -->
Table 15  Women’s basketball coach

<!-- b001991 | prose | pages [29] -->
Rank 1 2 Solving the

<!-- b001992 | prose | pages [29] -->
Pat

<!-- b001993 | prose | pages [29] -->
Tara

<!-- b001994 | prose | pages [29] -->
model drawn

<!-- b001995 | prose | pages [29] -->
Summitt

<!-- b001996 | prose | pages [29] -->
VanDerveer

<!-- b001997 | prose | pages [29] -->
coach list

<!-- b001998 | prose | pages [29] -->
Coaches List

<!-- b001999 | prose | pages [29] -->
Pat

<!-- b002000 | prose | pages [29] -->
Nancy

<!-- b002001 | prose | pages [29] -->
published on

<!-- b002002 | prose | pages [29] -->
Summitt

<!-- b002003 | prose | pages [29] -->
Fahey

<!-- b002004 | prose | pages [29] -->
the website

<!-- b002005 | prose | pages [29] -->
3 4 5

<!-- b002006 | prose | pages [29] -->
Nancy

<!-- b002007 | prose | pages [29] -->
Amy

<!-- b002008 | prose | pages [29] -->
Jody

<!-- b002009 | prose | pages [29] -->
Fahey

<!-- b002010 | prose | pages [29] -->
Ruley

<!-- b002011 | prose | pages [29] -->
Conradt

<!-- b002012 | prose | pages [29] -->
Amy

<!-- b002013 | prose | pages [29] -->
Tara

<!-- b002014 | prose | pages [29] -->
Jody

<!-- b002015 | prose | pages [29] -->
Ruley

<!-- b002016 | prose | pages [29] -->
VanDerveer

<!-- b002017 | prose | pages [29] -->
Conradt

<!-- b002018 | prose | pages [29] -->
Above table shows, the result is different to the authority rank of women’s basketball coach. The same rate is up to 100%, thus the model deviation is smaller.

<!-- b002019 | caption | pages [29] -->
Table 16  Football coaches

<!-- b002020 | prose | pages [29] -->
Rank 1 2 Solving the

<!-- b002021 | prose | pages [29] -->
Joe

<!-- b002022 | prose | pages [29] -->
John

<!-- b002023 | prose | pages [29] -->
model drawn

<!-- b002024 | prose | pages [29] -->
Paterno

<!-- b002025 | prose | pages [29] -->
Gagliardi

<!-- b002026 | prose | pages [29] -->
coach list

<!-- b002027 | prose | pages [29] -->
Coaches List

<!-- b002028 | prose | pages [29] -->
John

<!-- b002029 | prose | pages [29] -->
Bobby

<!-- b002030 | prose | pages [29] -->
published on

<!-- b002031 | prose | pages [29] -->
Gagliardi

<!-- b002032 | prose | pages [29] -->
Dodd

<!-- b002033 | prose | pages [29] -->
the website

<!-- b002034 | prose | pages [29] -->
3 4 5

<!-- b002035 | prose | pages [29] -->
Bobby

<!-- b002036 | prose | pages [29] -->
Eddie

<!-- b002037 | prose | pages [29] -->
Bear

<!-- b002038 | prose | pages [29] -->
Dodd

<!-- b002039 | prose | pages [29] -->
Robinson

<!-- b002040 | prose | pages [29] -->
Bryant

<!-- b002041 | prose | pages [29] -->
Joe

<!-- b002042 | prose | pages [29] -->
Eddie

<!-- b002043 | prose | pages [29] -->
Bear

<!-- b002044 | prose | pages [29] -->
Paterno

<!-- b002045 | prose | pages [29] -->
Robinson

<!-- b002046 | prose | pages [29] -->
Bryant

<!-- b002047 | prose | pages [29] -->
Above table shows, the result is different to the authority rank of football coach. The same rate is up to 100%, thus the model deviation is smaller.

<!-- b002048 | caption | pages [29] -->
Table 17  Baseball coach

<!-- b002049 | prose | pages [29] -->
Rank 1 2

<!-- b002050 | prose | pages [29] -->
Solving the

<!-- b002051 | prose | pages [29] -->
Gordie

<!-- b002052 | prose | pages [29] -->
Augie

<!-- b002053 | prose | pages [29] -->
model drawn

<!-- b002054 | prose | pages [29] -->
Gillespie

<!-- b002055 | prose | pages [29] -->
Garrido

<!-- b002056 | prose | pages [29] -->
coach list

<!-- b002057 | prose | pages [29] -->
Coaches List

<!-- b002058 | prose | pages [29] -->
Gordie

<!-- b002059 | prose | pages [29] -->
Raoul“Rod

<!-- b002060 | prose | pages [29] -->
published on

<!-- b002061 | prose | pages [29] -->
Gillespie

<!-- b002062 | prose | pages [29] -->
“Dedeaux

<!-- b002063 | prose | pages [29] -->
the website

<!-- b002064 | prose | pages [29] -->
3 4 5

<!-- b002065 | prose | pages [29] -->
Chuck

<!-- b002066 | prose | pages [29] -->
Gene

<!-- b002067 | prose | pages [29] -->
Bill

<!-- b002068 | prose | pages [29] -->
Hartman

<!-- b002069 | prose | pages [29] -->
Stephenson

<!-- b002070 | prose | pages [29] -->
Holowaty

<!-- b002071 | prose | pages [29] -->
Augie

<!-- b002072 | prose | pages [29] -->
Don

<!-- b002073 | prose | pages [29] -->
Slcip

<!-- b002074 | prose | pages [29] -->
Garrido

<!-- b002075 | prose | pages [29] -->
schaly

<!-- b002076 | prose | pages [29] -->
Bertman

<!-- b002077 | prose | pages [29] -->
Due to the few of metrics in baseball, the result is different to the authority rank of baseball coach. The same rate is only 40%, thus the model deviation is a litter large.

<!-- b002078 | prose | pages [29] -->
Reasonable hypothesis test

<!-- b002079 | prose | pages [29] -->
According to model and model solution deviation test, we found the overall deviation of the model is relatively small. We conclude the relevant data that we collect are more realistic, reliable, and underlying assumptions of the model is reasonable.

<!-- b002080 | heading | pages [29] -->
Sensitivity analysis of the model parameters [32,33,34]

<!-- b002081 | prose | pages [29] -->
According to model and model solution deviation test, about the comprehensive

<!-- b002082 | furniture | pages [29] -->


<!-- b002083 | prose | pages [29] -->
27 27

<!-- b002084 | furniture | pages [30] -->
Team#28875                                                                      Page 28 of 33

<!-- b002085 | prose | pages [30] -->
evaluation metrics of baseball coaches, we found that there is deviation. Therefore, we conducted sensitivity analysis of these evaluation metrics.

<!-- b002086 | prose | pages [30] -->
We get relevant metrics data for 69 baseball coaches, 3 evaluation metrics, and the

<!-- b002087 | prose | pages [30] -->
1  weight for each metrics are w .0 405 ，

<!-- b002088 | prose | pages [30] -->
score is

<!-- b002089 | prose | pages [30] -->
z

<!-- b002090 | prose | pages [30] -->
(

<!-- b002091 | prose | pages [30] -->
j

<!-- b002092 | prose | pages [30] -->
)

<!-- b002093 | prose | pages [30] -->
2  3  , so the evaluation w .0 393 w w .0 202 ，

<!-- b002094 | prose | pages [30] -->
n

<!-- b002095 | prose | pages [30] -->


<!-- b002096 | prose | pages [30] -->
 

<!-- b002097 | furniture | pages [30] -->


<!-- b002098 | prose | pages [30] -->
w r

<!-- b002099 | prose | pages [30] -->
(

<!-- b002100 | prose | pages [30] -->
i

<!-- b002101 | prose | pages [30] -->
,

<!-- b002102 | prose | pages [30] -->
j

<!-- b002103 | prose | pages [30] -->
)

<!-- b002104 | prose | pages [30] -->
i

<!-- b002105 | prose | pages [30] -->


<!-- b002106 | prose | pages [30] -->
i i

<!-- b002107 | prose | pages [30] -->
1

<!-- b002108 | prose | pages [30] -->
As for the 3 evaluation metrics, we consider all evaluation objects increase or decrease as a percentage. Assuming the magnitude of change is r , then the new evaluation

<!-- b002109 | prose | pages [30] -->
   z (' j ) w r ( i , j ) 1( 1 1

<!-- b002110 | prose | pages [30] -->
  z (' j ) w r ( i , j ) w 2 1 2

<!-- b002111 | prose | pages [30] -->
  z (' j ) w r ( i , j ) w 3 1 2

<!-- b002112 | prose | pages [30] -->
  r r ) w r ( i , j ) w r ( i , j )

<!-- b002113 | furniture | pages [30] -->


<!-- b002114 | prose | pages [30] -->
j j 2 3

<!-- b002115 | prose | pages [30] -->
  j  r r ( ( i i , j ) 1( r ) w r ( i , j )

<!-- b002116 | furniture | pages [30] -->


<!-- b002117 | prose | pages [30] -->
3

<!-- b002118 | prose | pages [30] -->
   r r ( ( i i , j ) w r ( i , j ) 1( jr )

<!-- b002119 | furniture | pages [30] -->


<!-- b002120 | prose | pages [30] -->
3

<!-- b002121 | prose | pages [30] -->
After conducting data standardization, the maximum of all metrics is 1. We consider the change of metrics score when we conduct sensitivity analysis, we have two sets of parameter setting method: When data increases we set the initial score of 0.001, 0.001 step also, the final score of 1.00; When data reduce we set the initial score of -0.001, -0.001 step also, the final score of -1.00. Sensitivity analysis process of single metric score shows in figure 11.

<!-- b002122 | prose | pages [30] -->
Original data evaluation

<!-- b002123 | prose | pages [30] -->
Sort

<!-- b002124 | prose | pages [30] -->
Given initial r

<!-- b002125 | prose | pages [30] -->
Re-evaluation

<!-- b002126 | prose | pages [30] -->
Sort

<!-- b002127 | prose | pages [30] -->
Sort consistent？

<!-- b002128 | prose | pages [30] -->
N

<!-- b002129 | prose | pages [30] -->
Get the final

<!-- b002130 | prose | pages [30] -->
score of r

<!-- b002131 | prose | pages [30] -->
Y r=r+Δr

<!-- b002132 | furniture | pages [30] -->


<!-- b002133 | caption | pages [30] -->
Figure 11  Sensitivity analysis process flowchart

<!-- b002134 | furniture | pages [30] -->


<!-- b002135 | prose | pages [30] -->
28 28

<!-- b002136 | furniture | pages [31] -->
Team#28875                                                                      Page 29 of 33

<!-- b002137 | prose | pages [31] -->
Using MATLAB, sensitivity analysis results in the table 18.

<!-- b002138 | caption | pages [31] -->
Table 18  Metrics score sensitivity analysis

<!-- b002139 | prose | pages [31] -->
Metrics variables years Metrics score [-0.001,0.01] change threshold

<!-- b002140 | prose | pages [31] -->
Interval Range 0.009

<!-- b002141 | prose | pages [31] -->
Winning Games

<!-- b002142 | prose | pages [31] -->
[-0.039,0.012] [-0.009,0.02]

<!-- b002143 | prose | pages [31] -->
0.051 0.029

<!-- b002144 | prose | pages [31] -->
The table above shows the sensitivity of evaluation Metrics winning is the lowest, the sensitivity of years is the highest. The average interval range is 0.0297 during the three metrics, less than 10%. So we can get the metrics sensitivity of the model is relatively low.

<!-- b002145 | heading | pages [31] -->
Conclusion

<!-- b002146 | prose | pages [31] -->
Through the four aspects of model test above, all the test results indicate that the model we built is qualified.

<!-- b002147 | prose | pages [31] -->
The article for Sports Illustrated

<!-- b002148 | prose | pages [31] -->
College Coaching Legends

<!-- b002149 | prose | pages [31] -->
The rapidly changing field of sports，today's winner could be tomorrow's losers , Who could have been The Legendary Swordsman?

<!-- b002150 | prose | pages [31] -->
Who is The Best All Time College Coach in history? Now, follow me, and I will show you how to “calculate” the best coach！

<!-- b002151 | prose | pages [31] -->
How do we complete the selection of coaches？ In order to reflect the practical training level and ability scientific, accurate, comprehensive and objectively，and ensure fair and equitable selection results, we make the games played, winning percentage, and number champion ,etc, as a score item. And finally calculate the total score to rank judges. First, excluding the impact of each class of different units, we will have all the data into the same unit.

<!-- b002152 | prose | pages [31] -->
When the number of score item is less (less than 10), calculate the proportion of the score for each item in the total score, and then the score of each item multiplied by its proportion, final sum, you can get a coach's final score;

<!-- b002153 | prose | pages [31] -->
When the number of grading project is more (more than 9), We will classify the similar score item as a classification, all score item first divided into several large classifications, calculated the proportion of the score for each item in the several large classifications, and then calculate the proportion of each large classification in the total score, the score of each item multiplied by its proportion, and the sum score acts the large classification score, calculate the proportion of this large classification in the total score, sum, you can get a coach's final score. We will calculate the final score for each coach ranking, so we can select the Top 5 coaches. Upon examination, this method can be widely applied in different genders and all possible sports fields.

<!-- b002154 | prose | pages [31] -->
Now let's use this mathematical calculation method to rank the coaches of Three American College Students League, the results are as follows.

<!-- b002155 | furniture | pages [31] -->


<!-- b002156 | prose | pages [31] -->
29 29

<!-- b002157 | furniture | pages [32] -->
Team#28875                                                                      Page 30 of 33

<!-- b002158 | prose | pages [32] -->
Coaches in NCAA Basketball

<!-- b002159 | prose | pages [32] -->
The First: Mike Krzyzewski The Second: Dean Smith Third: John Wooden Fourth: Bob Knight Fifth: Roy Williams

<!-- b002160 | prose | pages [32] -->
Women Coaches in NCAA female Basketball

<!-- b002161 | prose | pages [32] -->
The First: Pat Summitt The Second: Tara VanDerveer Third: Nancy Fahey Fourth: Amy Ruley Fifth: Jody Conradt

<!-- b002162 | prose | pages [32] -->
Coaches in football

<!-- b002163 | prose | pages [32] -->
The First: Joe Paterno The Second: John Gagliardi Third: Bobby Dodd Fourth: Eddie Robinson Fifth: Bear Bryant

<!-- b002164 | prose | pages [32] -->
Coaches in baseball

<!-- b002165 | prose | pages [32] -->
The First: Gordie Gillespie The Second: Augie Garrido Third: Chuck Hartman Fourth: Gene Stephenson Fifth: Bill Holowaty

<!-- b002166 | prose | pages [32] -->
These rankings have your crazy love sports stars? Who is he Best All Time College Coach in the Three Union is it? Mike Krzyzewski？Gordie Gillespie？

<!-- b002167 | prose | pages [32] -->
Male and female coaches from all areas of the sort carried out，we can get the The Best All Time College Coach. You must not imagine that she is Pat Summitt！Yes， you are not wrong, She is Pat Summitt，a female coach, She beat out many outstanding male coach, Sitting on the throne champion, What a incredible, Yet it is such a legendary female created another basketball legend. Winning 8 NCAA national championships. She is the only coach in NCAA history, and one of three college coaches overall, with at least 1,000 victories. It is a woman does not allow a man!

<!-- b002168 | prose | pages [32] -->
Also, with this method of calculation, we also analyzed the impact of time line horizon on coaching, we found that coaches are always ups and downs in coaching within a certain range on time line horizon, but with the growth of life coaching, slightly rising trend. Coaches should pay attention! Your coaching ability and time are closely related, Don’t give up because of the failure of several championship dreams, constant dropping wears away a stone was not built in a day, to persevere, continue to accumulate experience, there is always a way out of the day.

<!-- b002169 | prose | pages [32] -->
We look forward to the birth of the next legendary, and you're the next.

<!-- b002170 | furniture | pages [32] -->


<!-- b002171 | furniture | pages [32] -->


<!-- b002172 | prose | pages [32] -->
30

<!-- b002173 | furniture | pages [33] -->
Team#28875                                                                      Page 31 of 33

<!-- b002174 | heading | pages [33] -->
Evaluations of the Models

<!-- b002175 | prose | pages [33] -->
To modeling better next time, we discussed the strengths and weakness of each model. Furthermore, we put forward the improvement and determined the further study.

<!-- b002176 | heading | pages [33] -->
Strengths

<!-- b002177 | prose | pages [33] -->
 We standardized sample data sets to eliminate the effect of each evaluation

<!-- b002178 | prose | pages [33] -->
metrics dimension. So that modeling is universal.

<!-- b002179 | prose | pages [33] -->
 We used the AHP method to see investigative object as a system, according to the

<!-- b002180 | prose | pages [33] -->
decomposition, comparative judgment, comprehensive analysis to make decisions, organically combine qualitative methods and quantitative methods to make complex systems break down. So that the influence degree of each metric is quantified, clear and unambiguous.

<!-- b002181 | prose | pages [33] -->
 Use of literature method and logical analysis method on the evaluation metrics to

<!-- b002182 | prose | pages [33] -->
reference, decomposition, and we determine the evaluation metrics, so the classification is reasonable.

<!-- b002183 | prose | pages [33] -->
 Model Ⅱfully consider the situation that evaluation metrics too many to

<!-- b002184 | prose | pages [33] -->
calculate, so we introduce the concept of classification to simplify the calculation process.

<!-- b002185 | prose | pages [33] -->
 Model is universal, it can be applied in general across both genders and all

<!-- b002186 | prose | pages [33] -->
possible sports.

<!-- b002187 | heading | pages [33] -->
Weakness

<!-- b002188 | prose | pages [33] -->
 Thee too many indicators and statistics when we use AHP to solve weights.

<!-- b002189 | prose | pages [33] -->
 When we do classification for evaluation metrics, we should classify them from

<!-- b002190 | prose | pages [33] -->
coaching skills, experience, experience of the team management and the team performance and other aspects. But because the data is difficult to obtain, and time issues, we lack the data to relevant experience metrics of team management.

<!-- b002191 | prose | pages [33] -->
Improvement and Further Study

<!-- b002192 | prose | pages [33] -->
There is no specific quantitative metric data to relevant experience metrics of team management. Under the condition of sufficient time, we strengthen the collection efforts of data. We quantify the experience of the team management through coaches’ reputation, etc, to make the model more perfect.

<!-- b002193 | prose | pages [33] -->
Popularizing

<!-- b002194 | prose | pages [33] -->
ModelⅠand model Ⅱcan be applied to housing options, investment risk assessment, tourism and other areas. We can use mathematical models to solve real-life problems.

<!-- b002195 | furniture | pages [33] -->


<!-- b002196 | furniture | pages [33] -->


<!-- b002197 | prose | pages [33] -->
31

<!-- b002198 | furniture | pages [34] -->
Team#28875                                                                      Page 32 of 33

<!-- b002199 | prose | pages [34] -->
Reference

<!-- b002200 | prose | pages [34] -->
[1] Plunkett, Jack W. (2006). Plunkett's Sports Industry Almanac 2007. Plunkett

<!-- b002201 | prose | pages [34] -->
Research, Ltd. ISBN 1593924151. [2] Peer-review：http://searchsoftwarequality.techtarget.com/definition/peer-review. [3] Strengths of Peer review: Renyi Liu. Research on University Teachers’

<!-- b002202 | prose | pages [34] -->
Performance Evaluation in S&T. School of Management, Tianjin University Dissertation. 2007.5. [4] Shortcomings of Peer review ：Jin Shu-h, Wang Wei, Shen Yan-guang.

<!-- b002203 | prose | pages [34] -->
Comprehensive evaluation model based on peer review and AHP. Hebei

<!-- b002204 | prose | pages [34] -->
University of Engineering, Handan 056038, hebei, China.

<!-- b002205 | prose | pages [34] -->
[5] Questionnaire Survey: http://en.wikipedia.org/wiki/Questionnaire. [6] Jianbo Wei. Research on the Construction of Coach’s Quality system. Henan

<!-- b002206 | prose | pages [34] -->
University graduate master's degree thesis.2008.3.

<!-- b002207 | prose | pages [34] -->
[7] Fei Lu. Comparative and Synthetic Research on Content Analysis and

<!-- b002208 | prose | pages [34] -->
Bibliometrics. LIBRARY AND INFORMATION SERVICE, 2005, 49(9).

<!-- b002209 | prose | pages [34] -->
[8] Pan qin lei . The design of competence evaluation system for the table tennis

<!-- b002210 | prose | pages [34] -->
coach. Wuhan Institute of Physical Education Master Graduation Thesis. 2009.5. [9] Jinjun Hou, Yanqing Xiao, Min Tan, Mingke Gao. Mathematical Modeling

<!-- b002211 | prose | pages [34] -->
Methods and application. Southeast University Press .2012.7. [10] Saaty, Thomas L.; Peniwati, Kirti (2008). Group Decision Making: Drawing out

<!-- b002212 | prose | pages [34] -->
and Reconciling Differences.

<!-- b002213 | prose | pages [34] -->
Pittsburgh, Pennsylvania:

<!-- b002214 | prose | pages [34] -->
RWS Publications.  ISBN 978-1-888603-08-8. [11] AHP: http://en.wikipedia.org/wiki/Analytic_Hierarchy_Process [12] A simple AHP hierarchy: http://en.wikipedia.org/wiki/File:AHPHierarchy3.0.png [13] Fuzzy Comprehensive Evaluation Method:

<!-- b002215 | prose | pages [34] -->
http://wiki.mbalib.com/wiki/Fuzzy_comprehensive_evaluation_method [14] Liu Tao, et al. Fuzzy Comprehensive Evaluation Model of Teaching Quality

<!-- b002216 | prose | pages [34] -->
Based on AHP. Department of Mathematics and Physics, Yunyang Madical College, Shiyan 442000. [15] "NCAA History". NCAA. 2005. http://en.wikipedia.org/wiki/National_Collegiate_Athletic_Association [16] SRS: http://www.sports-reference.com/cbb/coaches/bob-knight-1.html [17] SOS: http://www.sports-reference.com/cbb/coaches/dean-smith-1.html [18] Judgment Matrix：

<!-- b002217 | prose | pages [34] -->
http://baike.baidu.com/link?url=Q9Pe2xqIEkiW0tqbGw_B6wVrcf0-_PUWgtujQ zEhqPRxpKrfqAarLSwFRzhduOmpRVK7XPd0yUpD51yknBG5f [19] The Relative membership degree values:

<!-- b002218 | prose | pages [34] -->
http://baike.baidu.com/view/3977584.htm [20] AHP-FCE: Huo Qi-wei, Jiang Hui-yuan. Research on Passenger Satisfaction

<!-- b002219 | prose | pages [34] -->
Evaluation of High Speed Railway based on AHP-FCE Method, RAILWAY TRANSPORT AND ECONOMY, 2011, 33(4). C812 U293.3

<!-- b002220 | furniture | pages [34] -->


<!-- b002221 | prose | pages [34] -->
32

<!-- b002222 | furniture | pages [35] -->
Team#28875                                                                      Page 33 of 33

<!-- b002223 | prose | pages [35] -->
[21] Tangyong Qiang, Wang Jun. The Study of the Evaluation Index System of Youth

<!-- b002224 | prose | pages [35] -->
Football Coach of Guangdong Province. Guangzhou Physical Education Institute，Guangzhou 510500，China. [22] Norman Dalkey, Olaf Helmer (1963) An Experimental Application of the Delphi

<!-- b002225 | prose | pages [35] -->
Method to the use of experts. Management Science, 9(3), Apr 1963, pp 458-467 [23] Freedman, D.A. (2005) Statistical Models: Theory and Practice, Cambridge

<!-- b002226 | prose | pages [35] -->
University Press. ISBN 978-0-521-67105-7 [24] College coaches metrics for assessment:

<!-- b002227 | prose | pages [35] -->
http://www.sports-reference.com/cbb/coaches/a-index.html [25] http://doc.mbalib.com/view/8acb9f212f587d72274d63f8a9b834a1.html [26]http://sports.yahoo.com/news/ncaab--college-basketball-s-25-most-intriguing-coa

<!-- b002228 | prose | pages [35] -->
ches-210811820.html [27]http://bleacherreport.com/articles/1732117-ranking-the-top-25-coaches-in-college

<!-- b002229 | prose | pages [35] -->
-basketball-today/page/4 [28] "John Wooden, former UCLA coach, dies". Associated Press. 5 June 2010.

<!-- b002230 | prose | pages [35] -->
Retrieved 23 November 2010. [29] "Bob Knight resigns". Sportsnetwork.com. Retrieved 2010-10-11. [30] Official Website of the Naismith Memorial Basketball Hall of Fame - Hall of

<!-- b002231 | prose | pages [35] -->
Famers [31]weight:http://zhidao.baidu.com/link?url=TBZBdQ3QzJoWWIiOrXsSs9o1CiGrp

<!-- b002232 | prose | pages [35] -->
O0Y1Vi1ny36-krkferK3Q74NCC5ER1EBFva7MBXc_qVPlO9HiC-hnwfqa [32] Liping Yu, Yuntao Pan,  Yishan Wu. Sensitivity Analysis in Science and

<!-- b002233 | prose | pages [35] -->
Technology Evaluation. Institute of Scientific and Technical information of China, Beijing 100038. [33]Shenyang Li, Xiaowu Zhang. Dynamic metrics selection method based on

<!-- b002234 | prose | pages [35] -->
sensitivity analysis [J]. Computer simulation. 2005(3):120-123. [34] Masuda T. Hierarchical Sensitivity Analysis of Priorities Used in Analytic

<!-- b002235 | prose | pages [35] -->
Hierarchical Process [J].Systems Science. 1990,21(2):415-427.

<!-- b002236 | furniture | pages [35] -->


<!-- b002237 | furniture | pages [35] -->


<!-- b002238 | prose | pages [35] -->
33
