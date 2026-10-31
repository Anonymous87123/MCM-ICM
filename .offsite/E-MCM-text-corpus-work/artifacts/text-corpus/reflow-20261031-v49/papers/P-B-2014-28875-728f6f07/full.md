# P-B-2014-28875-728f6f07

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Team Control Number

<!-- b000002 | front_matter | pages [1] -->
28875

<!-- b000003 | front_matter | pages [1] -->
For office use only For office use only T1 ________________ F1 ________________ T2 ________________ F2 ________________ T3 ________________ F3 ________________ Problem Chosen T4 ________________ F4 ________________

<!-- b000004 | front_matter | pages [1] -->
B

<!-- b000005 | front_matter | pages [1] -->
2014 Mathematical Contest in Modeling (MCM) Summary Sheet

<!-- b000006 | heading | pages [1] -->
Summary

<!-- b000007 | prose | pages [1] -->
Our goal is a model that finding out the “best all time college coach”. This is crucial to the promotion of the college coaching. Evaluation methods must reflect the practical training level and ability scientific, accurate, comprehensive and objectively. In our paper, to guarantee the fair and equitable of the selection results, comprehensively considered coaches coaching skills, experience, team management and his/her team performance and other aspects of teaching. Determine the metrics such as Games, Winning percentage, Championships, etc. for assessment. Then build a fuzzy comprehensive evaluation model based on improved analytic hierarchy process named IAHP-FCE model to find out The Best All Time College Coach for Sports Illustrated.

<!-- b000008 | prose | pages [1] -->
First of all, we applied the analytic hierarchy process (AHP) and fuzzy comprehensive evaluation method (FCE). Standardized the metrics data we collected by eliminate the effects of dimension. And calculate the relative membership degrees among the metrics. Then according to the fuzzy evaluation matrix constructed by the single metrics relative membership degree, built the modification of judgment matrix in the AHP. Secondly, calculated the weights of each metrics based on the reciprocity of judgment matrix. And carry on the consistency check using the single target linear programming to calculate the consistency index coefficient by Lingo7.0. Thirdly, build a fuzzy comprehensive evaluation model based on Analytic Hierarchy Process named AHP-FCE modelⅠ. Using modelⅠwe can obtain the composite score of each coach. Take NCAA Basketball to test the modelⅠ. Finally, we got the Top 5. Compare with the Authority Top 5 coaches, the accuracy of modelⅠ is 80%. To achieve our goal, we need get a higher Accuracy, so we decided to improve the model by introduced the Classification thought to decompose the metrics into 2 levels. Based on the modelⅠ and combined the new Classification, we built a simplified calculation and higher accuracy modelⅡ named IAHP-FCE modelⅡ. Then also take NCAA Basketball to rank the Top 5, followed by Mike Krzyzewski、Dean Smith、 John Wooden、Bob Knight and Roy Williams. Contrast with the Authority Ranking, the modelⅡ is correct almost 100%. So modelⅡ got a great improvement.

<!-- b000009 | prose | pages [2] -->
As to popularize the model to all possible sports, only need input the metrics data and get the weights, then you can rank the coaches across all possible sports. We applied the model in NCAA Football and Baseball, then got the both rank Top 5 coaches, balance the two Authority ranks, we also gets the high accuracy. So the model we improved can apply in general across all possible sports. For apply the model across both genders, we use the model to calculate the female coach Ranking of NCAA Female Basketball and list their Top 5. Contrast with the official rank, the result is almost perfect. Fully verified the model can apply across both genders. Ranking the final composite score of males and females coach’s which from the three biggest NCAA League. We ultimately find out The Best All Time College Coach----Pat Summitt, winning eight NCAA national championships, and she is the only coach in NCAA history, and one of three college coaches overall, with at least 1,000 victories.

<!-- b000010 | prose | pages [2] -->
In order to clearly articulate the difference which time line horizon, we randomly select multiple coaches from different gender and sports fields. Using the modelⅡ to work out the coach’s each year composite score separately. Draw the line chart with their coaching score and coaching years. Then contrast individually between the same fields and different sex, between the different fields and same sex, between the same fields and same sex, finally we got the conclusion that with the rise of the time line horizon, the coaching score always ups and downs within a certain range. In general, their coaching score ups gradually with the growth of his/her coaching years. What’s more, we tested the model from four aspects, Dimensional consistency test, Model and model results deviation test, assumptions reasonableness test and Sensitivity analysis of the model parameters. Eventually the change threshold average interval of evaluation metrics in sensitivity analysis is 0.0297, less than 10%, all the test results indicate that the model we built is qualified. In summary, the IAHP-FCE model we improved achieved our goal. That is simplified calculation, accurate results and wide utility. It can be applied in general across both genders and all possible sports. In the long run, this model can be used for solving those practical problems in our daily life, for example the housing choice, the investment risk evaluation and tourism plan, etc.

<!-- b000011 | furniture | pages [3] -->
Team#28875                                                                      Page 1 of 33

<!-- b000012 | title | pages [3] -->
Finding Out The Best All Time College Coach

<!-- b000013 | heading | pages [3] -->
Abstract

<!-- b000014 | prose | pages [3] -->
Finding out the “Best All Time College Coach” is crucial to the promotion of the college coaching. We build a fuzzy comprehensive evaluation model based on improved analytic hierarchy process named IAHP-FCE model to find out The Best All Time College Coach for Sports Illustrated.

<!-- b000015 | prose | pages [3] -->
First of all, we applied the content analysis and bibliometrics method to determine the metrics such as games, winning percentage, championships, etc. for assessment. And standardized the metrics data by eliminate the effects of dimension. Then build a fuzzy comprehensive evaluation model based on analytic hierarchy process named AHP-FCE modelⅠ. Take NCAA Basketball to testing. Finally, we got the Top 5. Compare with the authority Top 5 coaches, the accuracy of modelⅠ is 80%. For the sake of a less calculation and higher accuracy model, we improved the model by introduced the classification thought to decompose the metrics into 2 levels. Then obtain the IAHP-FCE modelⅡ. Then also take NCAA Basketball to rank the Top 5, Mike Krzyzewski、Dean Smith、John Wooden、Bob Knight and Roy Williams. Contrast with the authority ranking, the accuracy of modelⅡ is 100%. So the modelⅡ gets a higher accuracy. Input the metrics data and get the weights, we obtained each the coaches Top 5 in NCAA Football, Baseball and Woman’s Basketball. Balance the official ranks, the result is almost perfect. Fully verified the model can applied in general across all possible sports and both genders.

<!-- b000016 | prose | pages [3] -->
Ranking all the coaches composite scores, finally find out The Best All Time College Coach. She is Pat Summitt, winning eight NCAA national championships.

<!-- b000017 | prose | pages [3] -->
Next, we contrast the line chart individually between the same fields and different sex, between the different fields and same sex, between the same fields and same sex, finally got the conclusion that with the rise of the time line horizon, the coaching scores always ups and downs within a certain range. In general, their coaching score ups gradually with the growth of his/her coaching years.

<!-- b000018 | prose | pages [3] -->
What’s more, we tested the model from four aspects, eventually the change threshold average interval of evaluation metrics in sensitivity analysis is 0.0297, all the test results indicate that the model we built is qualified.

<!-- b000019 | prose | pages [3] -->
On the whole, the IAHP-FCE model is simplify calculation, accurate results and wide utility, can be used for housing choice, the investment risk evaluation and tourism plan, etc.

<!-- b000020 | keywords | pages [3] -->
Keywords:  The Best College Coach   Analytic hierarchy process

<!-- b000021 | prose | pages [3] -->
Fuzzy comprehensive evaluation method   Sensitivity analysis

<!-- b000022 | prose | pages [3] -->
1

<!-- b000023 | furniture | pages [4] -->
Team#28875                                                                      Page 2 of 33

<!-- b000024 | heading | pages [4] -->
Introduction

<!-- b000025 | prose | pages [4] -->
Sports Illustrated, a magazine for sports enthusiasts, is an American sports media franchise owned by media conglomerate Time Warner. Its self titled magazine has over 3.5 million subscribers and is read by 23 million adults each week, including over 18 million men. [1]And now, Sports Illustrated is looking for the “best all time college coach” male or female for the previous century.

<!-- b000026 | heading | pages [4] -->
Restatement of the Problem

<!-- b000027 | prose | pages [4] -->
The problem needs us to build a mathematical model to finding out the best all time college coach. We need consider the following.

<!-- b000028 | prose | pages [4] -->
 Build a mathematical model to choose the best college coach or coaches (past or present) from among either male or female coaches in such sports as college hockey or field hockey, football, baseball or softball, basketball, or soccer.

<!-- b000029 | prose | pages [4] -->
 Does it make a difference which time line horizon that you use in your analysis, i.e., does coaching in 1913 differ from coaching in 2013? Clearly articulate your metrics for assessment.

<!-- b000030 | prose | pages [4] -->
 Discuss how your model can be applied in general across both genders and all possible sports. Present your model’s top 5 coaches in each of 3 different sports.

<!-- b000031 | prose | pages [4] -->
 In addition, prepare a 1-2 page article for Sports Illustrated that explains your results and includes a non-technical explanation of your mathematical model that sports fans will understand.

<!-- b000032 | prose | pages [4] -->
Literature Review

<!-- b000033 | prose | pages [4] -->
There are many Evaluation methods of Coaching all over the world, which include Peer Review, Questionnaire Survey, Bibliometrics method, Analytic Hierarchy Process and Fuzzy Comprehensive Evaluation Method etc. Each method has a certain scope and limitations. On the evaluation, there is no universal method. In practice, evaluators often choose different methods for different purposes and objects. They can also be applied to the different stages of a comprehensive evaluation. Here makes a brief introduction on the application of the various evaluation methods.  Peer Review: It is a process used for checking the work performed by one's equals (peers) to ensure it meets specific criteria. Peer review is used in working groups for many professional occupations because it is thought that peers can identify each other's errors quickly and easily, speeding up the time that it takes for mistakes to be identified and corrected. [2]Peer review has its strengths, Wide

<!-- b000034 | prose | pages [4] -->
range of applications and performance well. [3]But it also has shortcomings，owing

<!-- b000035 | prose | pages [4] -->
to the professional restrictions, different expert evaluate the same person might come to different conclusions, and peer review probably form a network of

<!-- b000036 | prose | pages [4, 5] -->
2 acquaintances. Peer review may appear Matthew Effect, heavy subjectivity and short of fairness. [4]  Questionnaire Survey: A research instrument consisting of a series of questions and other prompts for the purpose of gathering information from respondents.

<!-- b000037 | furniture | pages [5] -->
Team#28875                                                                      Page 3 of 33

<!-- b000039 | prose | pages [5] -->
Although they are often designed for statistical analysis of the responses, this is not always the case. The questionnaire was invented by Sir Francis Galton. [5] Strengths: Save time, money and manpower, easy to quantify、statistics and analysis the survey results, and large-scale surveys. But the Survey design is difficult, the survey results is wide rather than deep, and difficult to guarantee the recoveries of the survey. [6]

<!-- b000040 | prose | pages [5] -->
 Content analysis and Bibliometrics [7]: In intelligence analysis method, content analysis is a qualitative analysis method based on quantitative analysis, and bibliometrics is a famous quantitative analysis method. They have their respective merit or limit. At present, most intelligence studying works only adopt single method. So there are a lot of abut and limits in analysis procedure. In order to conquer those weaknesses, we must combine quantitative analysis method and qualitative analysis method, and apply them in the intelligence studying works to promote the efficiency of intelligence studying works and the reliability and veracity of analysis result. [8]

<!-- b000041 | prose | pages [5] -->
Because of those methods above all have their respective merit or limits. We searched more information, and finally we got our method.

<!-- b000042 | prose | pages [5] -->
Our Approach

<!-- b000043 | prose | pages [5] -->
We analyzed the problems above and consulted lots of literature, and then come up with the following approaches.

<!-- b000044 | prose | pages [5] -->
[9] is a structured technique for  Analytic Hierarchy Process (AHP): AHP

<!-- b000045 | prose | pages [5] -->
organizing and analyzing complex decisions, based on mathematics and psychology. It was developed by Thomas L. Saaty in the 1970s and has been extensively studied and refined since then It has particular application. In group

<!-- b000046 | prose | pages [5] -->
[10], and is used around the world in a wide variety of decision decision making

<!-- b000047 | prose | pages [5] -->
situations, in fields such as government, business, industry, healthcare, and education. Rather than prescribing a "correct" decision, the AHP helps decision makers find one that best suits their goal and their understanding of the problem.

<!-- b000048 | prose | pages [5] -->
It provides a comprehensive and rational framework for structuring a decision problem, for representing and quantifying its elements, for relating those

<!-- b000049 | prose | pages [5] -->
[11] elements to overall goals, and for evaluating alternative solutions.

<!-- b000050 | prose | pages [5] -->
 Fuzzy Comprehensive Evaluation Method (FCE): FCE is a comprehensive evaluation method based on fuzzy mathematics. The comprehensive evaluation method based on the theory of fuzzy mathematics degree of membership of the

<!-- b000051 | prose | pages [5, 6] -->
3 qualitative evaluation into quantitative evaluation, which uses fuzzy mathematics subject to many factors thing or object to make an overall assessment. It has a clear result, systematic and strong features can solve vague, difficult to quantify the problem, suitable for solving the problem of non-deterministic. [13] The evaluation result is represented by a fuzzy set, closely combined with Qualitative description and Quantitative Analysis. [14]

<!-- b000052 | furniture | pages [6] -->
Team#28875                                                                      Page 4 of 33

<!-- b000054 | prose | pages [6] -->
In this paper, we integrated with the AHP and FCE, obtained the fuzzy comprehensive evaluation model based on analytic hierarchy process (AHP-FCE). Using the AHP-FCE model, we can get the rank of the coaches for several sports.

<!-- b000055 | heading | pages [6] -->
General Assumption

<!-- b000056 | prose | pages [6] -->
We make the following assumptions about the whole process in this paper to obtain a better model result.

<!-- b000057 | prose | pages [6] -->
About the Coach

<!-- b000058 | prose | pages [6] -->
 We choose almost 200 coaches from different sports according to him or her career achievement.  Assuming the coaches which we searched their data all is the leader of their sport, the best college coach produces from here.  The Best all time coach is come from the three biggest NCAA league of Basketball, Football and baseball.

<!-- b000059 | prose | pages [6] -->
About the Data

<!-- b000060 | prose | pages [6] -->
 Assuming the data we searched on the internet all is true and reliable.

<!-- b000061 | prose | pages [6] -->
 Statistical processing and Data calculation didn’t produce mistake, and the results

<!-- b000062 | prose | pages [6] -->
are trustworthy.

<!-- b000063 | prose | pages [6] -->
About the Metrics

<!-- b000064 | prose | pages [6] -->
 Searching a large literature and using a variety of methods, we assuming that the metrics choose for assessment are reasonable and all are very important in the coaching evaluation.  Assuming the classification of the metrics for Coach Evaluation correspond the assessment principle.  The metrics of coach we abandon all are no or little effect to the coaches coaching ability.

<!-- b000065 | prose | pages [6] -->
 Assuming the first level metrics Experience, Achievement and Competency can reflect the Non-quantifiable metrics Coaching skills and abilities of the team management.

<!-- b000066 | prose | pages [6] -->
Symbols Definitions

<!-- b000067 | prose | pages [6] -->
The Variables, Constant, and their Description are shown as below. If you don't know

<!-- b000068 | prose | pages [6, 7] -->
4 a variables or something, you can look it up in the table 1.

<!-- b000069 | furniture | pages [7] -->
Team#28875                                                                      Page 5 of 33

<!-- b000071 | caption | pages [7] -->
Table 1  Variables

<!-- b000072 | prose | pages [7] -->
Variables Description

<!-- b000073 | prose | pages [7] -->
m the number of coaches

<!-- b000074 | prose | pages [7] -->
n the number of evaluation metrics

<!-- b000075 | prose | pages [7] -->
w weight

<!-- b000076 | prose | pages [7] -->
B the Judgment Matrix

<!-- b000077 | prose | pages [7] -->
s (i ) the sample standard deviation

<!-- b000078 | prose | pages [7] -->
CIC (n ) Consistency Index Coefficient

<!-- b000079 | prose | pages [7] -->
min CIC ( n ) the minimum of consistency Index Coefficient

<!-- b000080 | prose | pages [7] -->
z ( j ) the composite score

<!-- b000081 | prose | pages [7] -->
Key Terms and Terminology  NCAA, The National Collegiate Athletic Association [15] , is a nonprofit association of 1,281 institutions, conferences, organizations, and individuals that organizes the athletic programs of many colleges and universities in the United States and Canada. It is headquartered in Indianapolis, Indiana.

<!-- b000082 | prose | pages [7] -->
 SRS, Simple Rating System [16], a rating that takes into account average point differential and strength of schedule, the rating is denominated in points above/ below average, where zero is average. Non-Division I games are excluded from the ratings.

<!-- b000083 | prose | pages [7] -->
 SOS, Strength of Schedule, a rating of strength of schedule the rating is denominated in points above /below average, where zero is average Non-Division I games are excluded from the ratings [17].

<!-- b000084 | prose | pages [7] -->
 Judgment Matrix: In the method of AHP, to determine the relative importance of each factor on each level given in these judgments represented numerically [18], written in matrix form is to determine the matrix.  The Relative membership degree values are fuzzy evaluation function in the concept: a kind of fuzzy comprehensive evaluation [19] is affected by many factors, things that make a comprehensive evaluation of the very effective multifactor decision-making method, which is characterized by the evaluation results are not absolutely positive or negative , but in a fuzzy set to represent.

<!-- b000085 | prose | pages [7] -->
5

<!-- b000086 | furniture | pages [8] -->
Team#28875                                                                      Page 6 of 33

<!-- b000087 | heading | pages [8] -->
The developing of models

<!-- b000088 | heading | pages [8] -->
ModelⅠ The Fuzzy Comprehensive Evaluation Model based on

<!-- b000089 | heading | pages [8] -->
Analytic Hierarchy Process (AHP-FCE model)

<!-- b000090 | prose | pages [8] -->
Combined with the AHP and FCE, we obtained the Fuzzy comprehensive evaluation model based on analytic hierarchy process (AHP-FCE) [20]. First of all, we collected the data from the internet, and do the Pretreatment. Then we determined the College Coach metrics for assessment. Finally goes the development of the AHP-FCE model.

<!-- b000091 | heading | pages [8] -->
Data collection and pretreatment

<!-- b000092 | prose | pages [8] -->
Data collect method such as face to face, telephone, postal or self completion and so on. But in this problem，those method above is too difficult to carry out. Because of the provides such as Reduced Costs, Fast Delivery, Easily Personalised and Penetrating difficult target groups [21], we search the internet for the relative data mainly from http://www.sports-reference.com and http://www.ncaa.com. For the pretreatment, because of Sports Illustrated is looking for the “best all time college coach” male or female for the previous century and our problem is to finding out the top 5 coaches. So we set a Standard line, to finding out almost 40 better coaches for each sport, and gather their several metrics value. And then make several Excel tables. Arrange NCAA Basketball, Football and Baseball are shown as follows table 1,

<!-- b000093 | caption | pages [8] -->
table2 and table 3.

<!-- b000094 | prose | pages [8] -->
Choose the metrics for assessment

<!-- b000095 | prose | pages [8] -->
For the purpose of looking for the best college coach, we need determined several metrics [22] for assessment to describe their performance. Research those data we searched on the internet, we can choose the metrics for assessment for all possible sports like NCAA Basketball, Football and Baseball, which are shown as follows table 1, table2 and table 3.

<!-- b000096 | prose | pages [8] -->
NCAA Basketball

<!-- b000097 | prose | pages [8] -->
Champ NCAA Final Fours AP High AP Final AP Pre CREG CTRN WL％ Game NCAA Years SRS SOS

<!-- b000098 | caption | pages [8] -->
Figure 1   The metrics for NCAA Basketball coach.

<!-- b000099 | prose | pages [8, 9] -->
6 NCAA Football

<!-- b000100 | furniture | pages [9] -->
Team#28875                                                                      Page 7 of 33

<!-- b000102 | prose | pages [9] -->
Overall Game Bowls Game AP High AP Pre AP post Bowls Years PCT SRS SOS

<!-- b000103 | caption | pages [9] -->
Figure 2   The metrics for NCAA Football coach.

<!-- b000104 | prose | pages [9] -->
NCAA baseball

<!-- b000105 | prose | pages [9] -->
Championship Years Game PCT Lost Win

<!-- b000106 | caption | pages [9] -->
Figure 3   The metrics for NCAA Baseball coach.

<!-- b000107 | heading | pages [9] -->
Development of the model

<!-- b000108 | prose | pages [9] -->
Based on the actual situation of the evaluation system, we established a fuzzy comprehensive evaluation system, from the representation, systematic, fitness point of view. And according to the sample data of each metrics, we built a fuzzy evaluation matrix of the relative membership degree from each evaluation. The ultimate goal of fuzzy comprehensive evaluation is to choose the best coaches relatives though the relative merits of comparison, among m coaches on the field. On the basis of the relative membership degree and scope of this optimization can determine the relative value of each metrics is relative to excellent coaches.

<!-- b000109 | prose | pages [9] -->
Standardized the metrics value

<!-- b000110 | prose | pages [9] -->
Supposing there are n evaluation metrics and m coaches, and the sample set of evaluation metrics is     x ( i , j ) i ,3,2,1 n , j ,3,2,1 m .  

<!-- b000111 | prose | pages [9] -->
Each metrics is a non-negative value. For the purpose of determine the x ( i , j )

<!-- b000112 | prose | pages [9] -->
individual evaluation metrics of the relative membership degree [25] of fuzzy evaluation matrix, eliminate the effect of each metrics dimension and modeling more

<!-- b000113 | prose | pages [9, 10] -->
7 versatility, sample data sets  ) need to standardize treatment [23]. To maintain x ( i , j

<!-- b000114 | furniture | pages [10] -->
Team#28875                                                                      Page 8 of 33

<!-- b000116 | prose | pages [10] -->
each metrics value of change information as much as possible, Standardized the bigger the more superior type metrics formula is

<!-- b000117 | prose | pages [10] -->
x ( i , j )  （1） r ( i , j )  x ( i ) x ( i ) max min

<!-- b000118 | prose | pages [10] -->
The Smaller the more standardized formula excellent type indicators is   x ( i ) x ( i ) x ( i , j )  max min r ( i , j ) （2）  x ( i ) x ( i ) max min

<!-- b000119 | prose | pages [10] -->
The more middle the more standardized formula excellent type indicators is  x ( i , j )   ,) x ( i ) x ( i , j ) ( i )  m i n m i d  x ( i ) x ( i m i d m i n  （3） r ( i , j )    x ( i ) x ( i ) x ( i , j )    m a x m i d , x ( i ) x ( i , j ) ( i )  m i d m a x  x ( i ) x ( i )  m a x m i d

<!-- b000120 | prose | pages [10] -->
The formula: , x max i ( ) and xmid (i ) respectively stands for the minimum, x min i ( ) maximum and the intermediate optimum values of the i metrics ; is the r ( i , j ) normalized value of the evaluation, and also is the relative membership degree from belongs to the optimal value of the j coaches in the i evaluation, and i=1,2,3,…,n,  j=1,2,3,…,n.  Those values of can be r ( i , j ) composed of a single element evaluation of fuzzy evaluation matrix

<!-- b000121 | prose | pages [10] -->
 R ( r ( i , j )) .  n m

<!-- b000122 | prose | pages [10] -->
Construct the Judgment Matrix

<!-- b000123 | prose | pages [10] -->
 R ( r ( i , j )) According to the fuzzy evaluation matrix ，Calculate the Judgment  n m

<!-- b000124 | prose | pages [10] -->
Matrix to determine the weight of each metrics. Fuzzy evaluation, in essence, is a preferred process. If the sample series    r ( 1 i , j ) j 3,2,1 m of the evaluation 

<!-- b000125 | prose | pages [10] -->
1i has a more big degree of change than the sample series metrics

<!-- b000126 | prose | pages [10] -->
   r ( 2 i , j ) j 3,2,1 m 2i , it means that 1i transfer more of the evaluation metrics 

<!-- b000127 | prose | pages [10] -->
2i .Therefore we can use the sample Comprehensive evaluation information than

<!-- b000128 | prose | pages [10] -->
m   2) ( r ( i , j ) r i  j 1  s ( i ) standard deviation , of each evaluation metrics to reflects the m

<!-- b000129 | prose | pages [10] -->
degree of impact on the comprehensive evaluation. Thus Calculate the Judgment

<!-- b000130 | prose | pages [10, 11] -->
8 m  r ( i , j )  j 1  Matrix B, and , i=1,2,..,n, stands for the mean of each evaluation sample r i m sequence. According to Formula (4), get the Judgment Matrix which maximum moment is 9.

<!-- b000131 | furniture | pages [11] -->
Team#28875                                                                      Page 9 of 33

<!-- b000133 | prose | pages [11] -->
  s ( i ) s ( j )     s ( i ) ( b 1 ) ,1 s ( i ) s ( j )  m  s s （4）  m a x m i n 1  b   , s ( i ) s ( j ) ij   s ( j ) s ( i )   ( b 1 ) 1  m  s s  m a x m i n stands for the minimum and maximum of   s ( i ) i 3,2,1 n In the formula, . s s ,  max min

<!-- b000134 | prose | pages [11] -->
  s  max bm min i , int( ) The relative importance of the degree parameter is , min    s 5.0   min

<!-- b000135 | prose | pages [11] -->
and int stands for the min function and the int funcation.

<!-- b000136 | prose | pages [11] -->
Calculate the Weight and Consistency Test

<!-- b000137 | prose | pages [11] -->
 In the Judgment Matrix B, the Consistency test, revise and weight [31] wi ( i 3,2,1 n ) 

<!-- b000138 | prose | pages [11] -->
n and   iw 0 need meeting 1. According to the definition of the Judgment w i  i 1

<!-- b000139 | prose | pages [11] -->
Matrix B, Theoretically that

<!-- b000140 | prose | pages [11] -->
w b   i ( i , j 3,2,1 n ) （5）  ij w j

<!-- b000141 | prose | pages [11] -->
Thus the Judgment Matrix B is   w w w    b 1 b 1 b 1    11 12 1 n w w w   1 2 n   w w w    b 2 b 2 b 2    21 22 2 n w w w   1 2 n  B   w    i b    ij w   j   w w w       n n n b b b 1  n 1 n 2 nn   w w w   1 2 n

<!-- b000142 | prose | pages [11] -->
On the basis of its Units, Reciprocal (reciprocity) and the Consistency condition, we can savvy those characteristics of the Judgment Matrix B,

<!-- b000143 | prose | pages [11, 12] -->
9 w   i b 1 [1] ii w i

<!-- b000144 | furniture | pages [12] -->
Team#28875                                                                      Page 10 of 33

<!-- b000146 | prose | pages [12] -->
w 1 j   b [2] ji w b i ij

<!-- b000147 | prose | pages [12] -->
w w w j     i i b b b [3] ij jk ik w w w j k k

<!-- b000148 | prose | pages [12] -->
 Based on , can calculating the weight of each metrics value, B ( b )  ij n n

<!-- b000149 | prose | pages [12] -->
   wi i 3,2,1 n . If Judgment Matrix B fulfils Formula (5), and fully consistent, thus, 

<!-- b000150 | prose | pages [12] -->
n n    b w w 0 （6） ij j i   i 1 j 1

<!-- b000151 | prose | pages [12] -->
But because of the actual complexity evaluation system, people diversity

<!-- b000152 | prose | pages [12] -->
awareness and sidedness and instability of subjective, the Judgment Matrix B

<!-- b000153 | prose | pages [12] -->
may not fully consistent those requirement, and it is Objective, can not be

<!-- b000154 | prose | pages [12] -->
completely eliminated in practical application.

<!-- b000155 | prose | pages [12] -->
Analytic Hierarchy Process requires Judgment Matrix B has satisfactory

<!-- b000156 | prose | pages [12] -->
consistency, so that can adapt to a variety of complex systems. If Judgment

<!-- b000157 | prose | pages [12] -->
Matrix B cannot meet the satisfactory consistency, it need correct. Supposing the   Y ijy corrected judgment matrix of B is , Its weight denoted  n n

<!-- b000158 | prose | pages [12] -->
   wi i 3,2,1 n , then the minimum Y is known as Optimal consistency of 

<!-- b000159 | prose | pages [12] -->
judgment matrix.

<!-- b000160 | prose | pages [12] -->
n n n n     y b y w w ij ji ij j i      i 1 j 1  i 1 j 1 min CIC ( n ) （7） 2 2 n n

<!-- b000161 | prose | pages [12] -->
Based on above, we established of a single target current planning model. The objective function：

<!-- b000162 | prose | pages [12] -->
n n n n     y b y w w ij ji ij j i     i 1 j 1 i 1 j 1   min CIC ( n ) 2 2 n n

<!-- b000163 | prose | pages [12] -->
And it Restrictions:

<!-- b000164 | prose | pages [12, 13] -->
10    y (,1 i 3,2,1 n )  ii    1          y b db , b db ( i 3,2,1 n , j i ,1 i ,2 n )   ij ij ij ij ij  y ji s .. t    w 0 ( i 3,2,1 n )   i  n    w 1 i   i 1

<!-- b000165 | furniture | pages [13] -->
Team#28875                                                                      Page 11 of 33

<!-- b000167 | prose | pages [13] -->
In the formula, named as Consistency Index Coefficient, d stands for CIC (n )

<!-- b000168 | prose | pages [13] -->
 Non-negative parameter, and . In General, the smaller is, then the d [ 5.0,0 ] CIC (n )

<!-- b000169 | prose | pages [13] -->
 CIC 1.0 better degree of consistency. If , considering subjective judgment matrix

<!-- b000170 | prose | pages [13] -->
consistency is acceptable. Using Lingo, we can get the minimum value of , CIC (n )

<!-- b000171 | prose | pages [13] -->
Thus obtain the most accurate weight.

<!-- b000172 | prose | pages [13] -->
The composite score

<!-- b000173 | prose | pages [13] -->
Multiply and accumulate each metrics weight w and each coach evaluation metrics i

<!-- b000174 | prose | pages [13] -->
relative membership degree , get the Fuzzy Evaluation composite score , r ( i , j ) z ( j )

<!-- b000175 | prose | pages [13] -->
n    （8） z ( j ) w r ( i , j ) ( j 3,2,1 m )  i  i 1

<!-- b000176 | prose | pages [13] -->
And is the larger, means the better the j coach is. So that we can scientific find z ( j )

<!-- b000177 | prose | pages [13] -->
out the Best College Coach.

<!-- b000178 | heading | pages [13] -->
Testing the model

<!-- b000179 | prose | pages [13] -->
Owing to we are familiar with basketball, thus we choose the coach from NCAA Basketball to validate the model AHP-FCE. Through the data collection and pretreatment, we get 13 metrics for 39 coaches. In this sample, from metrics 5 to metrics 8 are the smaller the superior type indicators, then according to formula (2) to Calculating the relative value of membership. And others follow formula (1) to Calculating the relative value of membership. Thus the value of from metrics 1 s (i ) to 13 are 0.110、0.099、0.261、0.323、0.269、0.226、0.215、0.186、0.199、0.340、 0.059、0.270、0.330.

<!-- b000180 | prose | pages [13] -->
Calculate the weight According to formula (4) obtain the Judgment Matrix B as follow.

<!-- b000181 | prose | pages [13, 14] -->
11   .1 000 .1 091 .0 444 .0 361 .0 431 .0 509 .0 533 .0 613 .0 576 .0 344 .0 576 .0 430 .0 356   .0 917 .1 000 .0 427 .0 350 .0 415 .0 486 .0 509 .0 580 .0 547 .0 333 .0 547 .0 414 .0 345     .2 253 .2 342 .1 000 .0 660 .0 939 .1 289 .1 379 .1 622 .1 516 .0 604 .0 346 .0 933 .0 642   .2 768 .2 859 .1 515 .1 000 .1 450 .1 803 .1 893 .2 136 .2 031 .0 877 .0 860 .1 443 .0 958     .2 318 .2 409 .1 065 .0 690 .1 000 .1 355 .1 445 .1 688 .1 582 .0 630 .1 583 .0 995 .0 670   .1 965 .2 056 .0 776 .0 555 .0 738 .1 000 .1 088 .1 331 .1 226 .0 514 .1 226 .0 734 .0 541     .1 875 .1 966 .0 725 .0 528 .0 692 .0 919 .1 000 .1 240 .1 134 .0 491 .1 134 .0 688 .0 515    B .1 631 .1 723 .0 617 .0 468 .0 592 .0 751 .0 806 .1 000 .0 904 .0 439 .0 904 .0 590 .0 459     .1 737 .1 828 .0 660 .0 492 .0 632 .0 816 .0 882 .1 106 .1 000 .0 461 .1 002 .0 630 .0 482     .2 907 .2 999 .1 654 .1 140 .1 588 .1 945 .2 036 .2 277 .2 169 .1 000 .5 687 .3 335 .1 389   .1 737 .1 828 .2 893 .1 163 .0 632 .0 816 .0 881 .1 106 .0 998 .0 176 .1 000 .0 630 .0 482     .2 325 .2 416 .1 072 .0 693 .1 005 .1 362 .1 454 .1 694 .1 586 .0 300 .1 586 .1 000 .0 673     .2 811 27 . 42 .1 558 .1 004 .1 492 .1 849 .1 940 .2 181 .2 073 .0 720 .2 073 .1 486 .1 000     And using the model AHP-FCE, calculate the weight of Judgment Matrix B above.

<!-- b000182 | furniture | pages [14] -->
Team#28875                                                                      Page 12 of 33

<!-- b000184 | prose | pages [14] -->
The initial range of each weight all is . Finally based on the related properties of [ ]1,0

<!-- b000185 | prose | pages [14] -->
Judgment Matrix, calculate the weight for each metrics shown as table 2.

<!-- b000186 | caption | pages [14] -->
Table 2   The weight for each metrics

<!-- b000187 | prose | pages [14] -->
Metrics 1 2 3 4 5 6 7

<!-- b000188 | prose | pages [14] -->
Weight 0.037 0.035 0.076 0.109 0.085 0.067 0.062 Metrics 8 9 10 11 12 13

<!-- b000189 | prose | pages [14] -->
Weight 0.053 0.057 0.151 0.071 0.082 0.115

<!-- b000190 | prose | pages [14] -->
Consistency test

<!-- b000191 | prose | pages [14] -->
 As the model, d stands for Non-negative parameter, and , in this paper d [ 5.0,0 ]

<!-- b000192 | prose | pages [14] -->
named parameter d=0.2. Then using lingo9.0 solve the single objective linear

<!-- b000193 | prose | pages [14] -->
programming model of formula (7) that

<!-- b000194 | prose | pages [14] -->
  min CIC ( n ) .0 032 1.0

<!-- b000195 | prose | pages [14] -->
So it means the Judgment Matrix has a satisfactory consistency.

<!-- b000196 | prose | pages [14] -->
The composite score

<!-- b000197 | prose | pages [14] -->
 wi ( i 3,2,1 n ) Combined the weight with relative membership degree into s (i ) 

<!-- b000198 | prose | pages [14] -->
formula (8), get the coach Fuzzy Evaluation composite score . z ( j )

<!-- b000199 | prose | pages [14] -->
n   z ( j ) w r ( i , j ) i  i 1

<!-- b000200 | prose | pages [14, 15] -->
12 Then using EXCEL to calculate the composite score , list AHP-FCE model’s top z ( j )

<!-- b000201 | furniture | pages [15] -->
Team#28875                                                                      Page 13 of 33

<!-- b000203 | prose | pages [15] -->
5 coaches in NCAA Basketball as table 3.

<!-- b000204 | caption | pages [15] -->
Table 3   AHP-FCE model’s top 5 coaches in NCAA Basketball

<!-- b000205 | prose | pages [15] -->
Rank Coach Composite score 1 Dean Smith 0.774 2 Mike Krzyzewski 0.755 3 Roy Williams 0.658 4 Rick Pitino 0.635 5 Jim Calhou 0.613

<!-- b000206 | heading | pages [15] -->
Testing Conclusion

<!-- b000207 | heading | pages [15] -->
Checking the AHP-FCE model’s result above with the College basketball's 25 most

<!-- b000208 | prose | pages [15] -->
intriguing coaches [26] and Ranking the Top 25 Coaches in College Basketball Today [27], we can easily find that the number 5 Jim Calhou even not rank in the both Top 25. And someone like John Wooden, won ten NCAA national championships in a 12-year period—seven in a row [28]— an unprecedented feat, Bob Knight, led his teams to three NCAA championships, one National Invitation Tournament (NIT) championship, and 11 Big Ten Conference championships [29], and Don Haskins, won 14 Western Athletic Conference championships and four WAC tournament titles, had fourteen NCAA tournament berths and made seven trips to the NIT [30], and so on, all not rank in this model’s top 5. So we validate the model result isn’t very accurately. The reason why the AHP-FCE works not very well is list as follow.

<!-- b000209 | prose | pages [15] -->
 In this model, the metrics is too many almost 13 large than the maximum Judgment Matrix moment 9. So we need separate the metrics into 2 or more levels, to analytic hierarchy process more accurate.

<!-- b000210 | prose | pages [15] -->
 The Judgment Matrix which maximum moment is 9. When the metrics is just large a lot than 9, such as 10, 11, this model will work not very well. So we need improve this model to handle the larger metrics.

<!-- b000211 | prose | pages [15] -->
 This calculation is too complicated specifically calculate the Judgment Matrix and the weight. We need simplify the calculation.

<!-- b000212 | prose | pages [15] -->
Because of the shortcomings of model AHP-FCE, we must improve this model into a better one to handle the larger metrics and simplify the calculation. We named it IAHP-FCE Model.

<!-- b000213 | heading | pages [15] -->
Improving the model

<!-- b000214 | prose | pages [15] -->
Based on the AHP-FCE model, we improved this into a better one named IAHP-FCE Model to simplify the calculation and handle the larger metrics. We quote a Classification of Evaluation metrics to separate the metrics into 2 or more levels, obtain the metrics system for assessment.

<!-- b000215 | prose | pages [15, 16] -->
13 Determine the metrics system for assessment

<!-- b000216 | furniture | pages [16] -->
Team#28875                                                                      Page 14 of 33

<!-- b000218 | prose | pages [16] -->
Build any metrics system must follow certain principles, in order to achieve a reasonable, powerful and evidence construction of the metrics system. In this paper, following the following three basic principles: Comprehensive, Representative and Operability. [31]A simple metrics system for assessment is as follow Figure 4.

<!-- b000219 | prose | pages [16] -->
Goal

<!-- b000220 | prose | pages [16] -->
Classification 1 Classification 2 Classification 3

<!-- b000221 | prose | pages [16] -->
M 1 M 2 M 3 M 4 M 5 M 5 M 6 M 7 M 8

<!-- b000222 | prose | pages [16] -->
                                             

<!-- b000223 | caption | pages [16] -->
Figure 4  A simple metrics system for assessment.

<!-- b000224 | prose | pages [16] -->
As shown in Figure 1, the first level is Classifications [24], the second is metrics and

<!-- b000225 | prose | pages [16] -->
the final is the Goal.

<!-- b000226 | prose | pages [16] -->
Determine the weight

<!-- b000227 | prose | pages [16] -->
According to the metrics system and the AHP-FCE model, we construct the Judgment Matrix, and calculate the weight list as follow table4.

<!-- b000228 | caption | pages [16] -->
Table 4  The Weight of the two level metrics

<!-- b000229 | prose | pages [16] -->
The first level metrics Weight  The second level metrics weight

<!-- b000230 | prose | pages [16] -->
A1  Classification 1 W1 B1      metric 1 w1 B2      metric 2 w2 B3      metric 3 w3   Bx      metric x wx A2  Classification 2 W2 Bx+1    metric x+1 wx+1 Bx+2    metric x+2 wx+2 Bx+3    metric x+3 wx+3   By      metric y wy

<!-- b000231 | prose | pages [16, 17] -->
14 A2  Classification 3 W3 By+1    metric y+1 wy+1 By+2    metric y+2 wy+2 By+3    metric y+3 wy+3   Bn      metric n wn

<!-- b000232 | furniture | pages [17] -->
Team#28875                                                                      Page 15 of 33

<!-- b000234 | prose | pages [17] -->
   

<!-- b000235 | prose | pages [17] -->
The final composite score

<!-- b000236 | prose | pages [17] -->
Combined with the weight of each metrics and the formula (8), respectively calculate the weight w of each second level metrics for corresponding first level i classifications. We obtained the coach Fuzzy Evaluation composite score , and zi ( j ) multiply and accumulate and the weight of each corresponding first level zi ( j ) classifications, then got the final Fuzzy Evaluation composite score . z ( j )

<!-- b000237 | prose | pages [17] -->
y x n           Z ( j ) W z ( j ) W z ( j ) W z ( j ) （9）  1 i 2 i 3 i      i 1 i x 1 i y 1

<!-- b000238 | heading | pages [17] -->
Using the IAHP-FCE model

<!-- b000239 | prose | pages [17] -->
We use the improved model to calculate the IAHP-FCE model’s top 5 coaches in NCAA Basketball，Football and Baseball. Present your model’s top 5 coaches in each of 3 different sports.

<!-- b000240 | heading | pages [17] -->
Model’s Top 5 coaches in NCAA Basketball

<!-- b000241 | prose | pages [17] -->
Based on the Delphi method [16] and mathematical statistic [17] ,we constructed the Basketball college coaches metrics system for assessment as follow figure 5.

<!-- b000242 | prose | pages [17] -->
The Best College Basketball Coach

<!-- b000243 | prose | pages [17] -->
Experience Achievement Competency

<!-- b000244 | prose | pages [17] -->
Champ NCAA AP Final Fours AP Final AP Pre CREG Game NCAA CTRN Years SOS SRS WL％ High

<!-- b000245 | caption | pages [17] -->
Figure 5   College coaches metrics system for assessment

<!-- b000246 | prose | pages [17, 18] -->
15 As shown in Figure 5, we determined Competency, Achievement and Experience as the first level metrics, and defined Final Fours, CTRN, CREG, SOS, WL％, SRS, AP High, AP Final , AP Pre, Champ NCAA , Game , NCAA and Years [18]as the second level metrics. Therefore clearly articulate our College coaches metrics system for assessment.

<!-- b000247 | furniture | pages [18] -->
Team#28875                                                                      Page 16 of 33

<!-- b000249 | prose | pages [18] -->
We separated the metrics into 2 levels, obtain the metrics system for assessment, there is 3 first levels, the second has 13. For second level under the 3 first levels, we used the fuzzy comprehensive evaluation model for solving the weight of second level. Thought processing the data, we get relevant metrics data for 39 coaches. From metrics 5 to metrics 8 are the smaller the superior type indicators. Then according to formula (2) to Calculating the relative membership degree, others are the bigger the superior type indicators. And others follow formula (1) to Calculating the relative membership degree. Thus the value of from metrics 1 to 13 are 0.110、0.099、 s (i ) 0.261、0.323、0.269、0.226、0.215、0.186、0.199、0.340、0.059、0.270、0.330.

<!-- b000250 | prose | pages [18] -->
For the Classification---- Experience

<!-- b000251 | prose | pages [18] -->
The Classification Experience, a total of 3 second level, the corresponding value of  are 0.110、0.099、0.261. The relative degree of importance is b 3 . s (i ) m According to formula (4) obtain the Judgment Matrix B as follow.

<!-- b000252 | prose | pages [18] -->
  .1 000 .1 136 .0 349    B .0 880 .1 000 .0 333   1   .2 864 .3 000 .1 000  

<!-- b000253 | prose | pages [18] -->
And using the model AHP-FCE, calculate the weight of Judgment Matrix B above.

<!-- b000254 | prose | pages [18] -->
The initial range of each weight all is . Finally based on the related properties of [ ]1,0

<!-- b000255 | prose | pages [18] -->
Judgment Matrix, calculate the weight for each metrics shown as below.

<!-- b000256 | prose | pages [18] -->
1 .1 000 .1 136 .0 349     w [ ] .0 213 1       3 .1 000 .0 880 .2 864 .1 136 .1 000 .3 000 .0 349 .0 333 .1 000 1 .0 880 .1 000 .0 333     w [ ] .0 193 2       3 .1 000 .0 880 .2 864 .1 136 .1 000 .3 000 .0 349 .0 333 .1 000 1 .2 864 .3 000 .1 000     w [ ] .0 594 3       3 .1 000 .0 880 .2 864 .1 136 .1 000 .3 000 .0 349 .0 333 .1 000

<!-- b000257 | prose | pages [18] -->
We take the parameter d=0.2, and use lingo9.0 solve the single objective linear programming model of formula (7) and get,  min CIC ( n ) 1.0

<!-- b000258 | prose | pages [18] -->
So it means the Judgment Matrix has a satisfactory consistency. Combined the

<!-- b000259 | prose | pages [18] -->
weight with relative membership degree into formula (8), get the coach Fuzzy

<!-- b000260 | prose | pages [18] -->
z 1 j ( ) Evaluation composite score .

<!-- b000261 | prose | pages [18, 19] -->
16 For the Classification---- Achievement and Competency

<!-- b000262 | furniture | pages [19] -->
Team#28875                                                                      Page 17 of 33

<!-- b000264 | prose | pages [19] -->
Similarly, we calculate them and get   .1 000 .0 592 .0 670 .0 543 .0 500   .1 690 .1 000 .1 197 .0 870 .0 763     .1 493 .0 835 .1 000 .0 742 .0 664  B   2 .1 842 .1 150 .1 347 .1 000 .0 862     .2 000 .1 311 .1 507 .1 600 .1 000    

<!-- b000265 | prose | pages [19] -->
  .1 000 .1 007 .0 740 .0 666 .0 502   .0 993 .1 000 .0 736 .0 663 .0 513     .1 352 .1 359 .1 000 .0 870 .0 609  B   3 .1 502 .1 509 .1 150 .1 000 .0 671     .1 993 .1 950 .1 641 .1 491 .1 000    

<!-- b000266 | prose | pages [19] -->
The weight of each level is shown as Table 5.

<!-- b000267 | caption | pages [19] -->
Table 5   The weight of Classification Achievement and Competency.

<!-- b000268 | prose | pages [19] -->
Achievement Competency

<!-- b000269 | prose | pages [19] -->
w w w w w w w w w w 5 6 7 8 9 10 13 4 12 11

<!-- b000270 | prose | pages [19] -->
0.124 0.205 0.176 0.232 0.263 0.146 0.146 0.191 0.215 0.302

<!-- b000271 | prose | pages [19] -->
We take the parameter d=0.2, and use lingo9.0 solve the single objective linear

<!-- b000272 | prose | pages [19] -->
programming model of formula (7) and get,

<!-- b000273 | prose | pages [19] -->
  min CIC ( n ) .0 014 1.0

<!-- b000274 | prose | pages [19] -->
So it means the Judgment Matrix has a satisfactory consistency. Combined the

<!-- b000275 | prose | pages [19] -->
weight with relative membership degree into formula (8), get the coach Fuzzy

<!-- b000276 | prose | pages [19] -->
z 3 j ( ) z 2 j ( ) Evaluation composite score and . Through access to relevant information,

<!-- b000277 | prose | pages [19] -->
we set the Weights of 3 Classification Experience, Achievement and Competency are

<!-- b000278 | prose | pages [19] -->
0.35、0.4、0.25. Then got the coach Fuzzy Evaluation composite score 3 8 13          Z ( j ) W z ( j ) W z ( j ) W z ( j ) 1 i 2 i 3 i    i 1 i 4 i 9 Using EXCEL to calculate and obtain the model’s Top 5 coaches as Table 6.

<!-- b000279 | prose | pages [19, 20] -->
17 Rank Coach Composite score Years 1 0.713513 1976-2014 Mike Krzyzewski 2 0.703688 1962-1997 Dean Smith 3 0.686056 1965-1975 John Wooden 4 0.669591 1966-2008 Bob Knight 5 0.655007 1989-2014 Roy Williams

<!-- b000280 | furniture | pages [20] -->
Team#28875                                                                      Page 18 of 33

<!-- b000281 | caption | pages [20] -->
Table 6   Model’s Top 5 coaches in NCAA Basketball

<!-- b000283 | prose | pages [20] -->
Contrast with the result of ModelⅠ and Sports Illustrated, the College basketball's 25 most intriguing coaches, this Rank of IAHP-FCE model is more reliable.

<!-- b000284 | heading | pages [20] -->
Popularize the model to all possible sports

<!-- b000285 | prose | pages [20] -->
Owing to this model just need adjust the number of metrics and calculate their weight, then multiply and accumulate the coach Fuzzy Evaluation composite score zi ( j ) and the weight of each corresponding first level classifications, finally got

<!-- b000286 | prose | pages [20] -->
the composite score of each coach. So that ranking the coach, and finding out the top 5 is easy. Using this model, we can popularize the model to all possible sports. In this paper, popularize this model to the famous NCAA Football and NCAA Baseball.

<!-- b000287 | heading | pages [20] -->
Model’s Top 5 coaches in NCAA Football

<!-- b000288 | prose | pages [20] -->
Solving the IAHP-FCE model above, we separate the metrics into 2 levels, there are 3 first levels, the second level has 13. Thought processing the data, we get relevant metrics data for 76 coaches. From metrics 7 to metrics 9 are the smaller the superior type indicators. Then according to formula (2) to calculate the relative membership degree, others are the bigger the superior type indicators. And others follow formula (1) to calculate the relative membership degree. Thus the value of from metrics s (i )

<!-- b000289 | prose | pages [20] -->
1 to 10 are 0.104、0.214、0.110、0.069、0.275、0.284、0.380、0.263、0.305、0.3.

<!-- b000290 | prose | pages [20] -->
 b 3 The relative degree of importance ,according to formula (4) obtain the m Judgment Matrix B as follow.

<!-- b000291 | prose | pages [20] -->
  .1 000 .0 586 .0 970    B .1 707 .1 000 .1 670   1   .1 036 .0 600 .1 000  

<!-- b000292 | prose | pages [20, 21] -->
18   .1 000 .0 430 .0 42    B .2 325 .1 000 .0 945   2   .2 383 .1 058 .1 000  

<!-- b000293 | furniture | pages [21] -->
Team#28875                                                                      Page 19 of 33

<!-- b000295 | prose | pages [21] -->
  .1 000 .1 725 .1 482 .1 514   .0 571 .1 000 .0 787 .0 808    B   3 .0 675 .1 270 .1 000 .1 032   .0 661 .1 238 .0 969 .1 000   According the AHP-FCE, we construct the Judgment Matrix. The initial range of

<!-- b000296 | prose | pages [21] -->
each weight all is . And based on the related properties of Judgment Matrix, [ ]1,0

<!-- b000297 | prose | pages [21] -->
calculate d the weight list as follow table 7.

<!-- b000298 | caption | pages [21] -->
Table 7   The weight of Experience, Achievement and Competency.

<!-- b000299 | prose | pages [21] -->
Experience Competency Achievement

<!-- b000300 | prose | pages [21] -->
w w w w w w w w w w 3 5 6 7 8 9 10 1 2 4

<!-- b000301 | prose | pages [21] -->
0.267 0.458 0.275 0.175 0.403 0.422 0.344 0.189 0.237 0.230

<!-- b000302 | prose | pages [21] -->
We take the parameter d=0.2, and use lingo9.0 solve the single objective linear

<!-- b000303 | prose | pages [21] -->
programming model of formula (7), and get

<!-- b000304 | prose | pages [21] -->
  min CIC ( n ) .0 051 1.0

<!-- b000305 | prose | pages [21] -->
So it means the Judgment Matrix has a satisfactory consistency. Combined the weight with relative membership degree into formula (8), get the coach Fuzzy zi ( j ) Evaluation composite score . Through access to relevant information, we set the Weights of 3 Classification Experience, Achievement and Competency are 0.35、0.4、 0.25. Then got the coach Fuzzy Evaluation composite score

<!-- b000306 | prose | pages [21] -->
3 8 13          Z ( j ) W z ( j ) W z ( j ) W z ( j ) 1 i 2 i 3 i    i 1 i 4 i 9

<!-- b000307 | prose | pages [21] -->
We used EXCEL to calculate and ranking the model’s Top 5 coaches as Table 8.

<!-- b000308 | caption | pages [21] -->
Table 8   Model’s Top 5 coaches in NCAA Football

<!-- b000309 | prose | pages [21] -->
Rank Coach Composite score Years 1 0.701 1966-2011 Joe Paterno 2 0.625 1949-2012 John Gagliardi 3 0.610 1945-1966 Bobby Dodd 4 0.608 1941-1997 Eddie Robinson 5 0.608 1945-1982 Bear Bryant

<!-- b000310 | prose | pages [21] -->
19

<!-- b000311 | furniture | pages [22] -->
Team#28875                                                                      Page 20 of 33

<!-- b000312 | heading | pages [22] -->
Model’s Top 5 coaches in NCAA Baseball

<!-- b000313 | prose | pages [22] -->
As an example of Male baseball coach, we solve the IAHP-FCE model above.

<!-- b000314 | prose | pages [22] -->
We can only find 3 evaluation metrics, the number is less, so we solve them through

<!-- b000315 | prose | pages [22] -->
modelⅠ. Thought processing the data, we get relevant metrics data for 69 coaches.

<!-- b000316 | prose | pages [22] -->
The 3 metrics are the bigger the superior type indicators. According to formula (1) to

<!-- b000317 | prose | pages [22] -->
calculate the relative membership degree, thus the value of are 0.100，0.045 and s (i )

<!-- b000318 | prose | pages [22] -->
 0.098. The relative degree of importance , According to formula (4) obtain the b 2 m

<!-- b000319 | prose | pages [22] -->
Judgment Matrix B

<!-- b000320 | prose | pages [22] -->
  .1 000 2 .1 036    B .0 500 .1 000 .0 510     .0 965 .1 964 .1 000  

<!-- b000321 | prose | pages [22] -->
And using the model AHP-FCE, calculate the weight of Judgment Matrix B above.

<!-- b000322 | prose | pages [22] -->
The initial range of each weight all is . Finally based on the related properties of [ ]1,0

<!-- b000323 | prose | pages [22] -->
Judgment Matrix, calculate the weight for each metrics shown as follow

<!-- b000324 | prose | pages [22] -->
1  2  3  w .0 393 w .0 405 w .0 202 ， ，

<!-- b000325 | prose | pages [22] -->
We take the parameter d=0.2, and use lingo9.0 solve the single objective linear

<!-- b000326 | prose | pages [22] -->
programming model of formula (7)

<!-- b000327 | prose | pages [22] -->
  min CIC ( n ) .0 028 1.0

<!-- b000328 | prose | pages [22] -->
So it means the Judgment Matrix has a satisfactory consistency. Combined the

<!-- b000329 | prose | pages [22] -->
weight with relative membership degree into formula (8), get the coach Fuzzy

<!-- b000330 | prose | pages [22] -->
zi ( j ) Evaluation composite score .We used EXCEL to calculate and ranking the

<!-- b000331 | prose | pages [22] -->
model’s Top 5 coaches as table 9.

<!-- b000332 | caption | pages [22] -->
Table 9   Model’s Top 5 coaches in NCAA Baseball

<!-- b000333 | prose | pages [22] -->
Rank Coach Composite score Years 1 0.748 1953-2003 Gordie Gillespie Augie 2 0.661 1969-2014 Garrido 3 0.612 1960-2006 Chuck Hartman 4 0.592 1978-2013 Gene StephensonBill 5 0.577 1969-2012 Holowaty

<!-- b000334 | prose | pages [22, 23] -->
20 Contrast with the result of Model’s Top 5 coaches of 3 College sports which include NCAA Basketball, Football and Baseball with the news report in Sports Illustrated, we can drew a conclusion that this IAHP-FCE model is trustworthy.

<!-- b000335 | furniture | pages [23] -->
Team#28875                                                                      Page 21 of 33

<!-- b000337 | heading | pages [23] -->
Applied the model across both genders

<!-- b000338 | prose | pages [23] -->
This model proofed can popularize to all possible sports, and now we applied the model across both genders. Taking into the differences between male and female coaches, we take women's basketball coaches as an example. Because the data of women's basketball coaches is less, we can only find 7 evaluation metrics, so we solve them through modelⅠ. Thought processing the data, we get relevant metrics data for 15 coaches. The 7 metrics are the bigger the superior type indicators. The value of are 0.066、0.080、0.111、0.299、0.225、0.284、0.047. The relative degree s (i )  of importance is . According to formula (4) obtain the Judgment Matrix B. b 2 m   .1 000 .0 782 .0 528 .0 178 .0 241 .1 655 .1 378     .1 278 .1 000 .0 619 .0 187 .0 258 .0 198 .0 345   .1 893 .1 616 .1 000 .0 211 .0 306 .0 226 .2 270      B .5 632 .5 355 .4 740 .1 000 .2 469 .1 297 .7 767   .1 156 .3 878 .3 263 .0 405 .1 000 .0 460 .4 525     .5 326 .5 049 .4 434 .0 771 .2 172 .1 000 .5 714     .0 726 .0 604 .0 441 .0 167 .0 221 .0 175 .1 000  

<!-- b000339 | prose | pages [23] -->
And using the model AHP-FCE, calculate the weight of Judgment Matrix B above.

<!-- b000340 | prose | pages [23] -->
The initial range of each weight all is . Finally based on the related properties of [ ]1,0

<!-- b000341 | prose | pages [23] -->
Judgment Matrix, calculate the weight of each metrics as table 10.

<!-- b000342 | caption | pages [23] -->
Table 10   The weight of each metrics

<!-- b000343 | prose | pages [23] -->
w w w w w w w 3 5 6 7 1 2 4

<!-- b000344 | prose | pages [23] -->
0.088 0.045 0.073 0.314 0.173 0.268 0.038

<!-- b000345 | prose | pages [23] -->
We take the parameter d=0.2, and use lingo9.0 solve the single objective linear

<!-- b000346 | prose | pages [23] -->
programming model of formula (7) that

<!-- b000347 | prose | pages [23] -->
  min CIC ( n ) .0 036 1.0

<!-- b000348 | prose | pages [23] -->
So it means the Judgment Matrix has a satisfactory consistency. Combined the weight with relative membership degree into formula (8), get the coach Fuzzy

<!-- b000349 | prose | pages [23] -->
Evaluation composite score zi ( j ) . We used EXCEL to calculate and ranking the

<!-- b000350 | prose | pages [23] -->
model’s Top 5 coaches as Table 11.

<!-- b000351 | prose | pages [23, 24] -->
21 Rank Coach Composite score Years 1 0.883 1974-2012 Pat Summitt 2 0.573 1978-1980 Tara VanDerveer 3 0.470 1998-2014 Nancy Fahey 4 0.442 1980-2008 Amy Ruley 5 0.383 1969-1973 Jody Conradt

<!-- b000352 | furniture | pages [24] -->
Team#28875                                                                      Page 22 of 33

<!-- b000353 | caption | pages [24] -->
Table 11   Model’s Top 5 Woman coaches in NCAA Women's Basketball

<!-- b000355 | prose | pages [24] -->
Using the model we also can get the NCAA women’s Basketball top 5 woman coaches. Juxtaposed with the reporter on the internet, obtained our result exist difference, but the rate of ranking top 5 is 100%. So we can draw a conclusion that this model also can apply the model across both genders.

<!-- b000356 | prose | pages [24] -->
Finding out the Best all time college coach

<!-- b000357 | prose | pages [24] -->
In NCAA the most famous sports ranking as football, basketball and baseball. We find out these best coaches and make the rank top 5 as table 12.

<!-- b000358 | caption | pages [24] -->
Table 12   The Top 5 Coaches of College

<!-- b000359 | prose | pages [24] -->
Rank Coach Composite score College Sports Pat Summitt 1 0.883 Women's Basketball 2 0.748 Baseball Gordie Gillespie 3 0.713513 Basketball Mike Krzyzewski 4 0.703688 Basketball Dean Smith 5 0.701 Football Joe Paterno

<!-- b000360 | prose | pages [24] -->
Comparing with their final composite score,

<!-- b000361 | prose | pages [24] -->
finally we obtain our model’s the Best all time

<!-- b000362 | prose | pages [24] -->
college coach. She is Pat Summitt which

<!-- b000363 | prose | pages [24] -->
final composite score high than 0.88.  Here

<!-- b000364 | prose | pages [24] -->
goes a brief introduction and figure 6 for our

<!-- b000365 | prose | pages [24] -->
Best all time college coach.

<!-- b000366 | prose | pages [24] -->
Patricia Sue "Pat" Summitt (born June 14,

<!-- b000367 | prose | pages [24] -->
1952) is a former women's college

<!-- b000368 | prose | pages [24] -->
basketball head coach. She now serves as

<!-- b000369 | prose | pages [24] -->
the head coach emeritusof the Tennessee Lady Vols

<!-- b000370 | prose | pages [24] -->
basketball team. She holds the most all-time

<!-- b000371 | prose | pages [24] -->
wins for a coach in NCAA basketball history

<!-- b000372 | prose | pages [24] -->
of either a men's or women's team in any division.    Figure 6  Pat Summitt

<!-- b000373 | prose | pages [24, 25] -->
22 She coached from 1974 to 2012, all with the Lady Vols, winning eight NCAA national championships, second only to the record 10 titles won by UCLA men's coach John Wooden. She is the only coach in NCAA history, and one of three college coaches overall, with at least 1,000 victories.

<!-- b000374 | furniture | pages [25] -->
Team#28875                                                                      Page 23 of 33

<!-- b000376 | prose | pages [25] -->
The difference as the time line horizon

<!-- b000377 | prose | pages [25] -->
Considering the relationship between the coach's coaching and time, we randomly selected a few coaches and collected relational data, calculated the Evaluation composite score during the coaching, we used EXCEL to draw a line chart, analyzed the relationship between the time line and coaching.

<!-- b000378 | prose | pages [25] -->
In this paper we selected the data of male basketball coach Dean Smith's to analysis. According to the result of the model above, we get the weight of each evaluation metric. Then calculate the composite score of Dean Smith each year from 1961 to 1997 shown as table 13.

<!-- b000379 | caption | pages [25] -->
Table 13  The composite score of Dean Smith each year

<!-- b000380 | prose | pages [25] -->
year 1961 1962 1963 1964 1965 1966 1967 1968 1969 score 0.455 0.440 0.468 0.398 0.480 0.504 0.523 0.536 0.477 year 1970 1971 1972 1973 1974 1975 1976 1977 1978 score 0.459 0.545 0.494 0.485 0.466 0.513 0.539 0.511 0.474 year 1979 1980 1981 1982 1983 1984 1985 1986 1987 score 0.473 0.501 0.598 0.562 0.601 0.532 0.579 0.611 0.573 year 1988 1989 1990 1991 1992 1993 1994 1995 1996 score 0.569 0.510 0.575 0.495 0.596 0.668 0.601 0.404 0.563

<!-- b000381 | prose | pages [25] -->
The above table shows that in different year the composite score of Dean Smith is different on the whole. In order to show the effects of time on the coaching more intuitionally, we used EXCEL to draw a line chart of Time Line Horizon -Coaching as

<!-- b000382 | caption | pages [25] -->
figure 7.

<!-- b000383 | prose | pages [25] -->
The time line horizon-coaching

<!-- b000384 | prose | pages [25] -->
0.8

<!-- b000385 | prose | pages [25] -->
0.7

<!-- b000386 | prose | pages [25] -->
0.6

<!-- b000387 | prose | pages [25] -->
0.5 Coaching 0.4

<!-- b000388 | prose | pages [25] -->
0.3

<!-- b000389 | prose | pages [25] -->
0.2

<!-- b000390 | prose | pages [25] -->
0.1

<!-- b000391 | prose | pages [25] -->
0 1961 1963 1965 1967 1969 1971 1973 1975 1977 1979 1981 1983 1985 1987 1989 1991 1993 1995

<!-- b000392 | prose | pages [25] -->
Time line horizon

<!-- b000393 | caption | pages [25] -->
Figure 7   The line chart for basketball coach Dean Smith

<!-- b000394 | prose | pages [25, 26] -->
23 With years of coaching increasing, Dean Smith coach's coaching is not the same level, but change within a certain range, ups and downs, with uncertainty, but overall, it is a slight upward trend. Different gender of the same sports In order to avoid accident, we randomly select more coaches from different sports, different gender to study. Using the same method, we calculate the composite score of each year, and draw a line chat of Time Line Horizon -Coaching as figure 8.

<!-- b000395 | furniture | pages [26] -->
Team#28875                                                                      Page 24 of 33

<!-- b000397 | prose | pages [26] -->
The time line horizon-coaching 0.6

<!-- b000398 | prose | pages [26] -->
0.5

<!-- b000399 | prose | pages [26] -->
0.4 Coaching 0.3

<!-- b000400 | prose | pages [26] -->
0.2

<!-- b000401 | prose | pages [26] -->
0.1

<!-- b000402 | prose | pages [26] -->
0 1974 1976 1978 1980 1982 1984 1986 1988 1990 1992 1994 1996 1998 2000 2002 2004 2006 2008 2010 Time line horizon

<!-- b000403 | caption | pages [26] -->
Figure 8  The line chart for women’s basketball coach Pat Summitt

<!-- b000404 | prose | pages [26] -->
The figure compares with figure 7, we found the fluctuation range of women's basketball coach coaching changed large, but the overall situation of change is substantially the same. In order to avoid accident, we analyze the relationship time line horizon and coaching between different sports and different gender. The results similar to Figure 7, Figure 8, as to different gender of the same sports, time line horizon makes a difference in coaching.

<!-- b000405 | prose | pages [26, 27] -->
24 Different sports of the same gender

<!-- b000406 | furniture | pages [27] -->
Team#28875                                                                      Page 25 of 33

<!-- b000408 | prose | pages [27] -->
The time line horizon-coaching

<!-- b000409 | prose | pages [27] -->
0.8

<!-- b000410 | prose | pages [27] -->
0.7

<!-- b000411 | prose | pages [27] -->
0.6

<!-- b000412 | prose | pages [27] -->
0.5 coaching 0.4

<!-- b000413 | prose | pages [27] -->
0.3

<!-- b000414 | prose | pages [27] -->
0.2

<!-- b000415 | prose | pages [27] -->
0.1

<!-- b000416 | prose | pages [27] -->
0 1966 1969 1972 1975 1978 1981 1984 1987 1990 1993 1996 1999 2002 2005 2008 2011

<!-- b000417 | prose | pages [27] -->
Time line horizon

<!-- b000418 | caption | pages [27] -->
Figure 9  The line chart for football coach Joe Paterno

<!-- b000419 | prose | pages [27] -->
The figure compares with figure 7, we found the overall situation of change is substantially the same. In order to avoid accident, we analyze the relationship time line horizon and coaching between different sports and same gender. The results similar to Figure 7, Figure 9, as to different sport of the same gender, time line horizon makes a difference in coaching.

<!-- b000420 | prose | pages [27] -->
Same sports of the same gender

<!-- b000421 | prose | pages [27] -->
The time line horizon-coaching

<!-- b000422 | prose | pages [27] -->
0.8

<!-- b000423 | prose | pages [27] -->
0.7

<!-- b000424 | prose | pages [27] -->
0.6

<!-- b000425 | prose | pages [27] -->
0.5 coaching 0.4

<!-- b000426 | prose | pages [27] -->
0.3

<!-- b000427 | prose | pages [27] -->
0.2

<!-- b000428 | prose | pages [27] -->
0.1

<!-- b000429 | prose | pages [27] -->
0 1970 1973 1976 1979 1982 1985 1988 1991 1994 1997 2000 2003 2006 2009

<!-- b000430 | prose | pages [27] -->
Time line horizon

<!-- b000431 | caption | pages [27] -->
Figure 10  The line chart for football coach Bobby Bowden

<!-- b000432 | prose | pages [27, 28] -->
25 The figure compares with figure 9, we found the overall situation of change is substantially the same. In order to avoid accident, we analyze the relationship time line horizon and coaching between same sports and same gender. The results similar to Figure 9, Figure 10, as to same sport of the same gender, time line horizon makes a difference in coaching.

<!-- b000433 | furniture | pages [28] -->
Team#28875                                                                      Page 26 of 33

<!-- b000435 | heading | pages [28] -->
Conclusion

<!-- b000436 | prose | pages [28] -->
Through analyzing the coach’ career coaching and the time line horizon from different gender of same sports, different sports of same gender, same sports and same gender, we find time line horizon can make a difference in coaching. In different time, coaches’ coaching is different on the whole, but change within a certain range, and from the whole, coaching growth with years increase, it is a slight upward trend. It can be seen, it made a difference which time line horizon that we use in our analysis.

<!-- b000437 | heading | pages [28] -->
Modeling test

<!-- b000438 | prose | pages [28] -->
Finally, we tested the model from dimensional consistency test, model and model solution deviation test, reasonable hypothesis test and sensitivity analysis of the model parameters of these 4 aspects.

<!-- b000439 | prose | pages [28] -->
Dimensional consistency test

<!-- b000440 | prose | pages [28] -->
When we collected data we standardized all of them, so that dimension tends consistency.

<!-- b000441 | heading | pages [28] -->
Model and model solution deviation test

<!-- b000442 | prose | pages [28] -->
Through establishing model Ⅰand model Ⅱ, we calculated comprehensive evaluation score of each college coaches nearly a century, by comparison, we found “best all time college coach”. By solving the model we got our model’s top 5 coaches in each of 3 different sports. We compared the top five coaches with the relevant Official Website recognized in various fields, comparison table as below table 14.

<!-- b000443 | caption | pages [28] -->
Table 14  Basketball Coaches

<!-- b000444 | prose | pages [28] -->
Rank 1 2 3 4 5 Solving the Mike Dean John Bob Roy model drawn Krzyzewski Smith Wooden Knight Williams coach list Coaches List John Dean Mike Roy Bob published on Wooden Smith Krzyzewski Williams Knight the website

<!-- b000445 | prose | pages [28] -->
Above table shows, the result is different to the authority rank of basketball coach. The same rate is up to 100%, thus the model deviation is smaller.

<!-- b000446 | prose | pages [28, 29] -->
26 Rank 1 2 3 4 5 Solving the Pat Tara Nancy Amy Jody model drawn Summitt VanDerveer Fahey Ruley Conradt coach list Coaches List Pat Nancy Amy Tara Jody published on Summitt Fahey Ruley VanDerveer Conradt the website

<!-- b000447 | furniture | pages [29] -->
Team#28875                                                                      Page 27 of 33

<!-- b000448 | caption | pages [29] -->
Table 15  Women’s basketball coach

<!-- b000450 | prose | pages [29] -->
Above table shows, the result is different to the authority rank of women’s basketball coach. The same rate is up to 100%, thus the model deviation is smaller.

<!-- b000451 | caption | pages [29] -->
Table 16  Football coaches

<!-- b000452 | prose | pages [29] -->
Rank 1 2 3 4 5 Solving the Joe John Bobby Eddie Bear model drawn Paterno Gagliardi Dodd Robinson Bryant coach list Coaches List John Bobby Joe Eddie Bear published on Gagliardi Dodd Paterno Robinson Bryant the website

<!-- b000453 | prose | pages [29] -->
Above table shows, the result is different to the authority rank of football coach. The same rate is up to 100%, thus the model deviation is smaller.

<!-- b000454 | caption | pages [29] -->
Table 17  Baseball coach

<!-- b000455 | prose | pages [29] -->
Rank 1 2 3 4 5

<!-- b000456 | prose | pages [29] -->
Solving the Gordie Augie Chuck Gene Bill model drawn Gillespie Garrido Hartman Stephenson Holowaty coach list Coaches List Gordie Raoul“Rod Augie Don Slcip published on Gillespie “Dedeaux Garrido schaly Bertman the website

<!-- b000457 | prose | pages [29] -->
Due to the few of metrics in baseball, the result is different to the authority rank of baseball coach. The same rate is only 40%, thus the model deviation is a litter large.

<!-- b000458 | prose | pages [29] -->
Reasonable hypothesis test

<!-- b000459 | prose | pages [29] -->
According to model and model solution deviation test, we found the overall deviation of the model is relatively small. We conclude the relevant data that we collect are more realistic, reliable, and underlying assumptions of the model is reasonable.

<!-- b000460 | heading | pages [29] -->
Sensitivity analysis of the model parameters [32,33,34]

<!-- b000461 | prose | pages [29] -->
According to model and model solution deviation test, about the comprehensive

<!-- b000462 | prose | pages [29, 30] -->
27 evaluation metrics of baseball coaches, we found that there is deviation. Therefore, we conducted sensitivity analysis of these evaluation metrics.

<!-- b000463 | furniture | pages [30] -->
Team#28875                                                                      Page 28 of 33

<!-- b000465 | prose | pages [30] -->
We get relevant metrics data for 69 baseball coaches, 3 evaluation metrics, and the

<!-- b000466 | prose | pages [30] -->
1  2  3  weight for each metrics are , so the evaluation w .0 393 w .0 405 w .0 202 ， ，

<!-- b000467 | prose | pages [30] -->
score is

<!-- b000468 | prose | pages [30] -->
n   z ( j ) w r ( i , j ) i  i 1

<!-- b000469 | prose | pages [30] -->
As for the 3 evaluation metrics, we consider all evaluation objects increase or decrease as a percentage. Assuming the magnitude of change is r , then the new evaluation

<!-- b000470 | prose | pages [30] -->
     z (' j ) w r ( i , j ) 1( r ) w r ( i , j ) w r ( i , j ) 1 1 j 2 3

<!-- b000471 | prose | pages [30] -->
    j  z (' j ) w r ( i , j ) w r ( i , j ) 1( r ) w r ( i , j ) 2 1 2 3

<!-- b000472 | prose | pages [30] -->
     z (' j ) w r ( i , j ) w r ( i , j ) w r ( i , j ) 1( jr ) 3 1 2 3

<!-- b000473 | prose | pages [30] -->
After conducting data standardization, the maximum of all metrics is 1. We consider the change of metrics score when we conduct sensitivity analysis, we have two sets of parameter setting method: When data increases we set the initial score of 0.001, 0.001 step also, the final score of 1.00; When data reduce we set the initial score of -0.001, -0.001 step also, the final score of -1.00. Sensitivity analysis process of single metric score shows in figure 11.

<!-- b000474 | prose | pages [30] -->
Original data evaluation Sort

<!-- b000475 | prose | pages [30] -->
Given initial r

<!-- b000476 | prose | pages [30] -->
Re-evaluation Sort

<!-- b000477 | prose | pages [30] -->
Y r=r+Δr Sort consistent？

<!-- b000478 | prose | pages [30] -->
N

<!-- b000479 | prose | pages [30] -->
Get the final score of r

<!-- b000480 | caption | pages [30] -->
Figure 11  Sensitivity analysis process flowchart

<!-- b000481 | prose | pages [30, 31] -->
28 Using MATLAB, sensitivity analysis results in the table 18.

<!-- b000482 | furniture | pages [31] -->
Team#28875                                                                      Page 29 of 33

<!-- b000484 | caption | pages [31] -->
Table 18  Metrics score sensitivity analysis

<!-- b000485 | prose | pages [31] -->
Metrics variables years Winning Games Metrics score [-0.001,0.01] [-0.039,0.012] [-0.009,0.02] change threshold Interval Range 0.009 0.051 0.029

<!-- b000486 | prose | pages [31] -->
The table above shows the sensitivity of evaluation Metrics winning is the lowest, the sensitivity of years is the highest. The average interval range is 0.0297 during the three metrics, less than 10%. So we can get the metrics sensitivity of the model is relatively low.

<!-- b000487 | heading | pages [31] -->
Conclusion

<!-- b000488 | prose | pages [31] -->
Through the four aspects of model test above, all the test results indicate that the model we built is qualified.

<!-- b000489 | prose | pages [31] -->
The article for Sports Illustrated

<!-- b000490 | prose | pages [31] -->
College Coaching Legends

<!-- b000491 | prose | pages [31] -->
The rapidly changing field of sports，today's winner could be tomorrow's losers , Who could have been The Legendary Swordsman?

<!-- b000492 | prose | pages [31] -->
Who is The Best All Time College Coach in history? Now, follow me, and I will show you how to “calculate” the best coach！ How do we complete the selection of coaches？ In order to reflect the practical training level and ability scientific, accurate, comprehensive and objectively，and ensure fair and equitable selection results, we make the games played, winning percentage, and number champion ,etc, as a score item. And finally calculate the total score to rank judges. First, excluding the impact of each class of different units, we will have all the data into the same unit.

<!-- b000493 | prose | pages [31] -->
When the number of score item is less (less than 10), calculate the proportion of the score for each item in the total score, and then the score of each item multiplied by its proportion, final sum, you can get a coach's final score;

<!-- b000494 | prose | pages [31] -->
When the number of grading project is more (more than 9), We will classify the similar score item as a classification, all score item first divided into several large classifications, calculated the proportion of the score for each item in the several large classifications, and then calculate the proportion of each large classification in the total score, the score of each item multiplied by its proportion, and the sum score acts the large classification score, calculate the proportion of this large classification in the total score, sum, you can get a coach's final score. We will calculate the final score for each coach ranking, so we can select the Top 5 coaches. Upon examination, this method can be widely applied in different genders and all possible sports fields.

<!-- b000495 | prose | pages [31] -->
Now let's use this mathematical calculation method to rank the coaches of Three American College Students League, the results are as follows.

<!-- b000496 | prose | pages [31, 32] -->
29 Coaches in NCAA Basketball The First: Mike Krzyzewski The Second: Dean Smith Third: John Wooden Fourth: Bob Knight Fifth: Roy Williams

<!-- b000497 | furniture | pages [32] -->
Team#28875                                                                      Page 30 of 33

<!-- b000499 | prose | pages [32] -->
Women Coaches in NCAA female Basketball The First: Pat Summitt The Second: Tara VanDerveer Third: Nancy Fahey Fourth: Amy Ruley Fifth: Jody Conradt

<!-- b000500 | prose | pages [32] -->
Coaches in football The First: Joe Paterno The Second: John Gagliardi Third: Bobby Dodd Fourth: Eddie Robinson Fifth: Bear Bryant

<!-- b000501 | prose | pages [32] -->
Coaches in baseball The First: Gordie Gillespie The Second: Augie Garrido Third: Chuck Hartman Fourth: Gene Stephenson Fifth: Bill Holowaty

<!-- b000502 | prose | pages [32] -->
These rankings have your crazy love sports stars? Who is he Best All Time College Coach in the Three Union is it? Mike Krzyzewski？Gordie Gillespie？ Male and female coaches from all areas of the sort carried out，we can get the The Best All Time College Coach. You must not imagine that she is Pat Summitt！Yes， you are not wrong, She is Pat Summitt，a female coach, She beat out many outstanding male coach, Sitting on the throne champion, What a incredible, Yet it is such a legendary female created another basketball legend. Winning 8 NCAA national championships. She is the only coach in NCAA history, and one of three college coaches overall, with at least 1,000 victories. It is a woman does not allow a man!

<!-- b000503 | prose | pages [32] -->
Also, with this method of calculation, we also analyzed the impact of time line horizon on coaching, we found that coaches are always ups and downs in coaching within a certain range on time line horizon, but with the growth of life coaching, slightly rising trend. Coaches should pay attention! Your coaching ability and time are closely related, Don’t give up because of the failure of several championship dreams, constant dropping wears away a stone was not built in a day, to persevere, continue to accumulate experience, there is always a way out of the day.

<!-- b000504 | prose | pages [32] -->
We look forward to the birth of the next legendary, and you're the next.

<!-- b000505 | prose | pages [32] -->
30

<!-- b000506 | furniture | pages [33] -->
Team#28875                                                                      Page 31 of 33

<!-- b000507 | heading | pages [33] -->
Evaluations of the Models

<!-- b000508 | prose | pages [33] -->
To modeling better next time, we discussed the strengths and weakness of each model. Furthermore, we put forward the improvement and determined the further study.

<!-- b000509 | heading | pages [33] -->
Strengths

<!-- b000510 | prose | pages [33] -->
 We standardized sample data sets to eliminate the effect of each evaluation metrics dimension. So that modeling is universal.

<!-- b000511 | prose | pages [33] -->
 We used the AHP method to see investigative object as a system, according to the decomposition, comparative judgment, comprehensive analysis to make decisions, organically combine qualitative methods and quantitative methods to make complex systems break down. So that the influence degree of each metric is quantified, clear and unambiguous.

<!-- b000512 | prose | pages [33] -->
 Use of literature method and logical analysis method on the evaluation metrics to reference, decomposition, and we determine the evaluation metrics, so the classification is reasonable.

<!-- b000513 | prose | pages [33] -->
 Model Ⅱfully consider the situation that evaluation metrics too many to calculate, so we introduce the concept of classification to simplify the calculation process.

<!-- b000514 | prose | pages [33] -->
 Model is universal, it can be applied in general across both genders and all possible sports.

<!-- b000515 | heading | pages [33] -->
Weakness

<!-- b000516 | prose | pages [33] -->
 Thee too many indicators and statistics when we use AHP to solve weights.

<!-- b000517 | prose | pages [33] -->
 When we do classification for evaluation metrics, we should classify them from coaching skills, experience, experience of the team management and the team performance and other aspects. But because the data is difficult to obtain, and time issues, we lack the data to relevant experience metrics of team management.

<!-- b000518 | heading | pages [33] -->
Improvement and Further Study

<!-- b000519 | prose | pages [33] -->
There is no specific quantitative metric data to relevant experience metrics of team management. Under the condition of sufficient time, we strengthen the collection efforts of data. We quantify the experience of the team management through coaches’ reputation, etc, to make the model more perfect.

<!-- b000520 | prose | pages [33] -->
Popularizing

<!-- b000521 | prose | pages [33] -->
ModelⅠand model Ⅱcan be applied to housing options, investment risk assessment, tourism and other areas. We can use mathematical models to solve real-life problems.

<!-- b000522 | prose | pages [33] -->
31

<!-- b000523 | furniture | pages [34] -->
Team#28875                                                                      Page 32 of 33

<!-- b000524 | heading | pages [34] -->
Reference

<!-- b000525 | references | pages [34] -->
[1] Plunkett, Jack W. (2006). Plunkett's Sports Industry Almanac 2007. Plunkett

<!-- b000526 | references | pages [34] -->
Research, Ltd. ISBN 1593924151.

<!-- b000527 | references | pages [34] -->
[2] Peer-review：http://searchsoftwarequality.techtarget.com/definition/peer-review.

<!-- b000528 | references | pages [34] -->
[3] Strengths of Peer review: Renyi Liu. Research on University Teachers’

<!-- b000529 | references | pages [34] -->
Performance Evaluation in S&T. School of Management, Tianjin University

<!-- b000530 | references | pages [34] -->
Dissertation. 2007.5.

<!-- b000531 | references | pages [34] -->
[4] Shortcomings of Peer review ：Jin Shu-h, Wang Wei, Shen Yan-guang.

<!-- b000532 | references | pages [34] -->
Comprehensive evaluation model based on peer review and AHP. Hebei

<!-- b000533 | references | pages [34] -->
University of Engineering, Handan 056038, hebei, China.

<!-- b000534 | references | pages [34] -->
[5] Questionnaire Survey: http://en.wikipedia.org/wiki/Questionnaire.

<!-- b000535 | references | pages [34] -->
[6] Jianbo Wei. Research on the Construction of Coach’s Quality system. Henan

<!-- b000536 | references | pages [34] -->
University graduate master's degree thesis.2008.3.

<!-- b000537 | references | pages [34] -->
[7] Fei Lu. Comparative and Synthetic Research on Content Analysis and

<!-- b000538 | references | pages [34] -->
Bibliometrics. LIBRARY AND INFORMATION SERVICE, 2005, 49(9).

<!-- b000539 | references | pages [34] -->
[8] Pan qin lei . The design of competence evaluation system for the table tennis

<!-- b000540 | references | pages [34] -->
coach. Wuhan Institute of Physical Education Master Graduation Thesis. 2009.5.

<!-- b000541 | references | pages [34] -->
[9] Jinjun Hou, Yanqing Xiao, Min Tan, Mingke Gao. Mathematical Modeling

<!-- b000542 | references | pages [34] -->
Methods and application. Southeast University Press .2012.7.

<!-- b000543 | references | pages [34] -->
[10] Saaty, Thomas L.; Peniwati, Kirti (2008). Group Decision Making: Drawing out

<!-- b000544 | references | pages [34] -->
and

<!-- b000545 | references | pages [34] -->
Reconciling

<!-- b000546 | references | pages [34] -->
Differences.

<!-- b000547 | references | pages [34] -->
Pittsburgh,

<!-- b000548 | references | pages [34] -->
Pennsylvania:

<!-- b000549 | references | pages [34] -->
RWS

<!-- b000550 | references | pages [34] -->
Publications.  ISBN 978-1-888603-08-8.

<!-- b000551 | references | pages [34] -->
[11] AHP: http://en.wikipedia.org/wiki/Analytic_Hierarchy_Process

<!-- b000552 | references | pages [34] -->
[12] A simple AHP hierarchy: http://en.wikipedia.org/wiki/File:AHPHierarchy3.0.png

<!-- b000553 | references | pages [34] -->
[13] Fuzzy Comprehensive Evaluation Method:

<!-- b000554 | references | pages [34] -->
http://wiki.mbalib.com/wiki/Fuzzy_comprehensive_evaluation_method

<!-- b000555 | references | pages [34] -->
[14] Liu Tao, et al. Fuzzy Comprehensive Evaluation Model of Teaching Quality

<!-- b000556 | references | pages [34] -->
Based on AHP. Department of Mathematics and Physics, Yunyang Madical

<!-- b000557 | references | pages [34] -->
College, Shiyan 442000.

<!-- b000558 | references | pages [34] -->
[15] "NCAA History". NCAA. 2005.

<!-- b000559 | references | pages [34] -->
http://en.wikipedia.org/wiki/National_Collegiate_Athletic_Association

<!-- b000560 | references | pages [34] -->
[16] SRS: http://www.sports-reference.com/cbb/coaches/bob-knight-1.html

<!-- b000561 | references | pages [34] -->
[17] SOS: http://www.sports-reference.com/cbb/coaches/dean-smith-1.html

<!-- b000562 | references | pages [34] -->
[18] Judgment Matrix：

<!-- b000563 | references | pages [34] -->
http://baike.baidu.com/link?url=Q9Pe2xqIEkiW0tqbGw_B6wVrcf0-_PUWgtujQ

<!-- b000564 | references | pages [34] -->
zEhqPRxpKrfqAarLSwFRzhduOmpRVK7XPd0yUpD51yknBG5f

<!-- b000565 | references | pages [34] -->
[19] The Relative membership degree values:

<!-- b000566 | references | pages [34] -->
http://baike.baidu.com/view/3977584.htm

<!-- b000567 | references | pages [34] -->
[20] AHP-FCE: Huo Qi-wei, Jiang Hui-yuan. Research on Passenger Satisfaction

<!-- b000568 | references | pages [34] -->
Evaluation of High Speed Railway based on AHP-FCE Method, RAILWAY

<!-- b000569 | references | pages [34] -->
TRANSPORT AND ECONOMY, 2011, 33(4). C812 U293.3

<!-- b000570 | references | pages [34] -->
32

<!-- b000571 | furniture | pages [35] -->
Team#28875                                                                      Page 33 of 33

<!-- b000572 | references | pages [35] -->
[21] Tangyong Qiang, Wang Jun. The Study of the Evaluation Index System of Youth

<!-- b000573 | references | pages [35] -->
Football Coach of Guangdong Province. Guangzhou Physical Education

<!-- b000574 | references | pages [35] -->
Institute，Guangzhou 510500，China.

<!-- b000575 | references | pages [35] -->
[22] Norman Dalkey, Olaf Helmer (1963) An Experimental Application of the Delphi

<!-- b000576 | references | pages [35] -->
Method to the use of experts. Management Science, 9(3), Apr 1963, pp 458-467

<!-- b000577 | references | pages [35] -->
[23] Freedman, D.A. (2005) Statistical Models: Theory and Practice, Cambridge

<!-- b000578 | references | pages [35] -->
University Press. ISBN 978-0-521-67105-7

<!-- b000579 | references | pages [35] -->
[24] College coaches metrics for assessment:

<!-- b000580 | references | pages [35] -->
http://www.sports-reference.com/cbb/coaches/a-index.html

<!-- b000581 | references | pages [35] -->
[25] http://doc.mbalib.com/view/8acb9f212f587d72274d63f8a9b834a1.html

<!-- b000582 | references | pages [35] -->
[26]http://sports.yahoo.com/news/ncaab--college-basketball-s-25-most-intriguing-coa

<!-- b000583 | references | pages [35] -->
ches-210811820.html

<!-- b000584 | references | pages [35] -->
[27]http://bleacherreport.com/articles/1732117-ranking-the-top-25-coaches-in-college

<!-- b000585 | references | pages [35] -->
-basketball-today/page/4

<!-- b000586 | references | pages [35] -->
[28] "John Wooden, former UCLA coach, dies". Associated Press. 5 June 2010.

<!-- b000587 | references | pages [35] -->
Retrieved 23 November 2010.

<!-- b000588 | references | pages [35] -->
[29] "Bob Knight resigns". Sportsnetwork.com. Retrieved 2010-10-11.

<!-- b000589 | references | pages [35] -->
[30] Official Website of the Naismith Memorial Basketball Hall of Fame - Hall of

<!-- b000590 | references | pages [35] -->
Famers

<!-- b000591 | references | pages [35] -->
[31]weight:http://zhidao.baidu.com/link?url=TBZBdQ3QzJoWWIiOrXsSs9o1CiGrp

<!-- b000592 | references | pages [35] -->
O0Y1Vi1ny36-krkferK3Q74NCC5ER1EBFva7MBXc_qVPlO9HiC-hnwfqa

<!-- b000593 | references | pages [35] -->
[32] Liping Yu, Yuntao Pan,  Yishan Wu. Sensitivity Analysis in Science and

<!-- b000594 | references | pages [35] -->
Technology Evaluation. Institute of Scientific and Technical information of

<!-- b000595 | references | pages [35] -->
China, Beijing 100038.

<!-- b000596 | references | pages [35] -->
[33]Shenyang Li, Xiaowu Zhang. Dynamic metrics selection method based on

<!-- b000597 | references | pages [35] -->
sensitivity analysis [J]. Computer simulation. 2005(3):120-123.

<!-- b000598 | references | pages [35] -->
[34] Masuda T. Hierarchical Sensitivity Analysis of Priorities Used in Analytic

<!-- b000599 | references | pages [35] -->
Hierarchical Process [J].Systems Science. 1990,21(2):415-427.

<!-- b000600 | references | pages [35] -->
33
