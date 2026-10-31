# P-B-2014-29696-84be6e3a

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Team Control Number

<!-- b000002 | front_matter | pages [1] -->
29696

<!-- b000003 | front_matter | pages [1] -->
For office use only For office use only T1 ________________ F1 ________________ T2 ________________ F2 ________________ T3 ________________ F3 ________________ Problem Chosen T4 ________________ F4 ________________

<!-- b000004 | front_matter | pages [1] -->
B

<!-- b000005 | front_matter | pages [1] -->
2014 Mathematical Contest in Modeling (MCM) Summary Sheet

<!-- b000006 | prose | pages [1] -->
College Coaches’ Mount Rushmore

<!-- b000007 | heading | pages [1] -->
Summary

<!-- b000008 | prose | pages [1] -->
College coaches’ e exposure is growing these days, as a result of the increase on attention to college sports. In this paper, we build a mathematical model to rank college coaches among either gender across generations in varied sports.

<!-- b000009 | prose | pages [1] -->
Firstly, we build a factors pool to collect evaluation factors of all sports. By principle component analysis (PCA), we obtain three components used to evaluate the coach’s performance. Then we take American college basketball as an example to build the Coaches Ranking Model (CRM). The first step of CRM is to classify the ranking coaches by Cluster Analysis. Next we compare all coaches with the “idealistic coach” whose factors are the best of factors pool by means of adjusted Cosine Similarity. We hereby obtain the top 5 college basketball coaches in the previous century.

<!-- b000010 | prose | pages [1] -->
Secondly, we optimize CRM across generations by modified coefficient of coaching difficulty and social influence. The coefficients are calculated by Regression Analysis. Based on the optimized model, we take the impacts of genders into consideration. Modified coefficient in genders is calculated by Analysis of covariance (AVOVA) and Data Whitening. We hereby obtain the optimized CRM.

<!-- b000011 | prose | pages [1] -->
Thirdly, the optimized model is applied to other sports in the worldwide. As for sports, we figure out an advanced ranking model related to different sports with the update of factors pool. Hence, we obtain the coaches ranking list of football, baseball and softball. As for countries, we obtain a list of top 5 college basketball coaches in China.

<!-- b000012 | prose | pages [1] -->
Finally, we test the sensitivity and robustness of the coaches ranking model. The test result illustrates the stability and adaptability of the model. Besides, based on the ranking results, we discuss the significance of the relation between ranking state distribution and economy, society, culture development in America. Generally, the prosperity of sports stimulates the development of the region.

<!-- b000013 | prose | pages [1] -->
Above all, our model is accessible to both genders across generations in varied sports. It can be applied further to other countries and organizations. Therefore, our model has a high degree of adaptability and stability.

<!-- b000014 | keywords | pages [1] -->
Key Words:  Adjusted Cosine Similarity, Principle Component Analysis, Data

<!-- b000015 | prose | pages [1] -->
Whitening, Cluster Analysis, CRM

<!-- b000016 | furniture | pages [2] -->
Team # 29696

<!-- b000017 | furniture | pages [2] -->
Page 1 of 42

<!-- b000018 | heading | pages [2] -->
Model Execution Flow

<!-- b000019 | heading | pages [2] -->
College Coaches Ranking Model

<!-- b000020 | prose | pages [2] -->
STEP1: Collect evaluation factors of college coaches STEP2: Results and Conclusion Principle Component Classify 12 factors into 3 Principle components Analysis (PCA) of principle components ranking by importance data for basketball

<!-- b000021 | heading | pages [2] -->
Sensitivity and Robustness Analysis

<!-- b000022 | prose | pages [2] -->
Z : coach-ability, 1 coaches Z : coach-influence-school,   Z Z Z 2 1 2 3 Z :coach-influence-society. 3

<!-- b000023 | prose | pages [2] -->
STEP3: Results and Conclusion Cluster analysis of Pick out the better groups in 9 for ranking with data simplification the latter calculation.

<!-- b000024 | prose | pages [2] -->
Results and Conclusion STEP4： Best coaches ranking Ranking result： by Cosine Similarity 1st:John Wooden 2nd:Geno Auriemma 3rd:Pat Summitt 4th:Dean Smith 5th:Mike Krzyzewski

<!-- b000025 | heading | pages [2] -->
Model Optimization

<!-- b000026 | prose | pages [2] -->
Process and Approach Conclusions and Results STEP1： Find the relation Calculate modification 1st:John Wooden 2nd:Geno between generations coefficient of time line Auriemma 3rd:Pat Summitt andcoaching horizon by linear 4th:Dean Smith 5th:Mike difficulty across time regression analysis Krzyzewski line horizons.

<!-- b000027 | prose | pages [2] -->
Process and Approach Conclusions and Results STEP2： Analysis of variance Analyze the significant 1st:John Wooden 2nd:Geno (ANOVA) of data and difference in factors across Auriemma 3rd:Pat Summitt discussion of gender the gender and modify 4th:Dean Smith 5th:Mike differences data by Data Whitening. Krzyzewski

<!-- b000028 | heading | pages [2] -->
Model Extension

<!-- b000029 | prose | pages [2] -->
 Factors pool extension  Sports extension: baseball, football, softball.  Countries and organizations extension: China

<!-- b000030 | heading | pages [2] -->
Further Discussion Upon Model

<!-- b000031 | prose | pages [2] -->
Discussion upon sports impact on economy, culture, social developments.

<!-- b000032 | furniture | pages [3] -->
Team # 29696

<!-- b000033 | furniture | pages [3] -->
Page 1 of 42

<!-- b000034 | prose | pages [3] -->
Looking for the “best all time college coaches”?  See here!

<!-- b000035 | prose | pages [3] -->
Over the previous century, outstanding college coaches have pushed college sports a lot further. Skill improvement, strategies update and tactics developments, such changes contributed by coaches stimulate college sports to sparkle.  It’s s time to take stock of the coaching landscape in the past 10 decades.

<!-- b000036 | prose | pages [3] -->
In this article, a ranking system is applied to pick out the “best all time college coaches”.  This is not simply a ranking of who are the best coaches in the previous century. It's a scientific ranking of who would be the best to lead a team going forward. Through the system, we find out the top 5 best coaches in basketball, football and baseball as the following figure 1.

<!-- b000037 | prose | pages [3] -->
Basketball Football

<!-- b000038 | prose | pages [3] -->
Baseball

<!-- b000039 | prose | pages [3] -->
Figure 1

<!-- b000040 | prose | pages [3] -->
The rankings proved to be a tough job. The best coaches in college should be outstanding in all aspects: recruiting, teaching, tactics design and players motivation.

<!-- b000041 | furniture | pages [4] -->
Team # 29696

<!-- b000042 | furniture | pages [4] -->
Page 2 of 42

<!-- b000043 | prose | pages [4] -->
We are eager to find out the well-rounded coaches, who can wisely handle all. The following in figure 2 evaluation factors are weighed in our system.

<!-- b000044 | prose | pages [4] -->
Pct

<!-- b000045 | prose | pages [4] -->
Tenure

<!-- b000046 | prose | pages [4] -->
Games lost

<!-- b000047 | prose | pages [4] -->
Games won

<!-- b000048 | prose | pages [4] -->
Games directed “Idealistic coach” Ranked coach Teams directed

<!-- b000049 | prose | pages [4] -->
Social influence

<!-- b000050 | prose | pages [4] -->
Figure 2

<!-- b000051 | prose | pages [4] -->
So how are these factors weighed in the ranking system?

<!-- b000052 | prose | pages [4] -->
Firstly, we create an “idealistic coach” whose factors are the best among all ranked coaches in basketball, virtually, of course. Secondly, compare each coach with the “idealistic coach” by means of Cosine Similarity. In addition, we also keep an eye on gender differences and generation gap by means of Data Whitening. And eventually, we promote the basketball system to football and baseball across countries. Why is this system accessible?

<!-- b000053 | prose | pages [4] -->
Genders, generations, countries and sports, such considerations complete the system. In advance, the ranking result makes our system convincing. And why is this system reliable?

<!-- b000054 | prose | pages [4] -->
We tested the system’s s stability and sensitivity. The results were stable with slight factor fluctuation. Besides, a large amount of data is used to establish and test the system.

<!-- b000055 | prose | pages [4] -->
Therefore, we have strong confidence to carry out the ranking system. What does the ranking result show?

<!-- b000056 | prose | pages [4] -->
We have to admit that coaching is one of the driving forces in building a national championship team. The job of a coach is multi-faceted and challenging. Coaches picked out in our system are not only excellent among their peers, but leave impression on the career for decades as well. The ranking system is capable of evaluating coaches among organizations across sports.

<!-- b000057 | furniture | pages [5] -->
Team # 29696

<!-- b000058 | furniture | pages [5] -->
Page 3 of 42

<!-- b000059 | heading | pages [5] -->
Table of Content

<!-- b000060 | contents | pages [5] -->
Looking for the “best all time college coaches”?  See here! ........................................ 1

<!-- b000061 | contents | pages [5] -->
1. Introduction ............................................................................................................... 5

<!-- b000062 | contents | pages [5] -->
2. Assumptions .............................................................................................................. 6

<!-- b000063 | contents | pages [5] -->
3. Factors Analysis Model Based on Principal Component Analysis ........................... 6

<!-- b000064 | contents | pages [5] -->
3.1.

<!-- b000065 | contents | pages [5] -->
Model overview .................................................................................................................. 6

<!-- b000066 | contents | pages [5] -->
3.2.

<!-- b000067 | contents | pages [5] -->
Justification of our approach ............................................................................................ 7

<!-- b000068 | contents | pages [5] -->
3.3.

<!-- b000069 | contents | pages [5] -->
Model formulation ............................................................................................................. 8

<!-- b000070 | contents | pages [5] -->
3.4.

<!-- b000071 | contents | pages [5] -->
Result analysis .................................................................................................................. 10

<!-- b000072 | contents | pages [5] -->
4. Coaches Ranking Model Based on Cosine Similarity ...................................... 11

<!-- b000073 | contents | pages [5] -->
4.1.

<!-- b000074 | contents | pages [5] -->
Model overview ................................................................................................................ 11

<!-- b000075 | contents | pages [5] -->
4.2.

<!-- b000076 | contents | pages [5] -->
Model justification ........................................................................................................... 11

<!-- b000077 | contents | pages [5] -->
4.3.

<!-- b000078 | contents | pages [5] -->
Model formulation ........................................................................................................... 12

<!-- b000079 | contents | pages [5] -->
4.3.1. Vector definition of the “idealistic coach” and ranking ................................................ 12

<!-- b000080 | contents | pages [5] -->
4.3.2. Adjusted Cosine Similarity ............................................................................................. 13

<!-- b000081 | contents | pages [5] -->
4.3.3. Model computing by Euclidean distance-based clustering analysis ............................ 14

<!-- b000082 | contents | pages [5] -->
4.4.

<!-- b000083 | contents | pages [5] -->
Results analysis ................................................................................................................ 17

<!-- b000084 | contents | pages [5] -->
5. Model Optimization of Time Line Horizon Based on Regression Analysis ........... 17

<!-- b000085 | contents | pages [5] -->
5.1.

<!-- b000086 | contents | pages [5] -->
Justification of our generation-based model optimization ........................................... 17

<!-- b000087 | contents | pages [5] -->
5.2.

<!-- b000088 | contents | pages [5] -->
Generation-based model optimization ........................................................................... 17

<!-- b000089 | contents | pages [5] -->
5.2.1. Giant effect ....................................................................................................................... 17

<!-- b000090 | contents | pages [5] -->
5.2.2. Coaching difficulty optimization .................................................................................... 18

<!-- b000091 | contents | pages [5] -->
5.2.3. Social influence optimization .......................................................................................... 20

<!-- b000092 | contents | pages [5] -->
5.3.

<!-- b000093 | contents | pages [5] -->
Generation-based model optimization results ............................................................... 20

<!-- b000094 | contents | pages [5] -->
5.4.

<!-- b000095 | contents | pages [5] -->
Generation-based results analysis .................................................................................. 21

<!-- b000096 | contents | pages [5] -->
6. Model Optimization of Gender Based on Data Whitening ..................................... 22

<!-- b000097 | contents | pages [5] -->
6.1.

<!-- b000098 | contents | pages [5] -->
Justification of our gender-based model optimization.................................................. 22

<!-- b000099 | contents | pages [5] -->
6.2.

<!-- b000100 | contents | pages [5] -->
Gender-based model optimization.................................................................................. 23

<!-- b000101 | contents | pages [5] -->
6.3.

<!-- b000102 | contents | pages [5] -->
Gender-based optimization results ................................................................................. 25

<!-- b000103 | contents | pages [5] -->
6.4.

<!-- b000104 | contents | pages [5] -->
Gender-based results analysis ......................................................................................... 25

<!-- b000105 | contents | pages [5] -->
7. Model Extension ..................................................................................................... 26

<!-- b000106 | contents | pages [5] -->
7.1.

<!-- b000107 | contents | pages [5] -->
Establishment of factors pool ......................................................................................... 26

<!-- b000108 | contents | pages [5] -->
7.2.

<!-- b000109 | contents | pages [5] -->
Sports extension ............................................................................................................... 28

<!-- b000110 | contents | pages [5] -->
7.3.

<!-- b000111 | contents | pages [5] -->
Country extension ............................................................................................................ 29

<!-- b000112 | contents | pages [5] -->
7.4.

<!-- b000113 | contents | pages [5] -->
Factors extension ............................................................................................................. 29

<!-- b000114 | contents | pages [5] -->
7.4.1. Salary ................................................................................................................................ 29

<!-- b000115 | contents | pages [5] -->
7.4.2. Popularity of college ........................................................................................................ 29

<!-- b000116 | contents | pages [5] -->
7.4.3. Formal performance of the college team ....................................................................... 29

<!-- b000117 | contents | pages [5] -->
8. Results and results analysis ..................................................................................... 30

<!-- b000118 | contents | pages [5] -->
8.1.

<!-- b000119 | contents | pages [5] -->
Results ............................................................................................................................... 30

<!-- b000120 | contents | pages [5] -->
8.2.

<!-- b000121 | contents | pages [5] -->
What the results illustrate ............................................................................................... 33

<!-- b000122 | furniture | pages [6] -->
Team # 29696

<!-- b000123 | furniture | pages [6] -->
Page 4 of 42

<!-- b000124 | contents | pages [6] -->
9. Model Stability Analysis ......................................................................................... 34

<!-- b000125 | contents | pages [6] -->
9.1.

<!-- b000126 | contents | pages [6] -->
Sensitivity analysis ........................................................................................................... 34

<!-- b000127 | contents | pages [6] -->
9.2.

<!-- b000128 | contents | pages [6] -->
Robustness analysis ......................................................................................................... 35

<!-- b000129 | contents | pages [6] -->
9.3.

<!-- b000130 | contents | pages [6] -->
Strengths and Weaknesses .............................................................................................. 36

<!-- b000131 | contents | pages [6] -->
9.3.1. Strengths ........................................................................................................................... 36

<!-- b000132 | contents | pages [6] -->
9.3.2. Weaknesses ....................................................................................................................... 36

<!-- b000133 | contents | pages [6] -->
10.Conclusions ............................................................................................................. 37

<!-- b000134 | contents | pages [6] -->
11. Reference ................................................................................................................ 37

<!-- b000135 | contents | pages [6] -->
12.Appendix ................................................................................................................. 39

<!-- b000136 | furniture | pages [7] -->
Team # 29696

<!-- b000137 | furniture | pages [7] -->
Page 5 of 42

<!-- b000138 | heading | pages [7] -->
1. Introduction

<!-- b000139 | heading | pages [7] -->
Restatement of the problem

<!-- b000140 | prose | pages [7] -->
College Coaching Legends Sports Illustrated, a magazine for sports enthusiasts, is looking for the “best all time college coach” male or female for the previous century. Build a mathematical model to choose the best college coach or coaches (past or present) from among either male or female coaches in such sports as college hockey or field hockey, football, baseball or softball, basketball, or soccer. Does it make a difference which time line horizon that you use in your analysis, i.e. , does coaching in 1913 differ from coaching in 2013? Clearly articulate your metrics for assessment. Discuss how your model can be applied in general across both genders and all possible sports. Present your model’s s top 5 coaches in each of 3 different sports.

<!-- b000141 | prose | pages [7] -->
In addition to the MCM format and requirements, prepare a 1-2 page article for Sports Illustrated that explains your results and includes a non-technical explanation of your mathematical model that sports fans will understand.

<!-- b000142 | heading | pages [7] -->
Background

<!-- b000143 | prose | pages [7] -->
The “Sports Illustrated” is a magazine for sports enthusiasts, as the problem above demonstrates. Therefore, after a brief survey of the formal rankings in this magazine, we sort out the following basic idea related to college sports coaches ranking, combined with data resources and other researches.

<!-- b000144 | prose | pages [7] -->
The National Collegiate Athletic Association (NCAA) is a nonprofit association of 1,281 institutions, conferences, organizations, and individuals that organizes the athletic programs of many colleges and universities in the United States and Canada. Based on the game statistics from this association and its similar conferences, we found that hockey, football, baseball or softball, basketball, and soccer teams are supposed to attend national conferences or games annually. The performance of a team, which is bond with its head coach, is the core element determining the result in a game, win or loss. Therefore, a coach’s quality can be evaluated by the team’s s performance. In advance, the assessed coach is possible to have coached more than one team. Hence, the overall team-directing experience of a coach is considered, including the number of the games the coach has directed, wins and losses all counted, the winning rate, significant awards the coach has won and the his or her career length. Through this process, the fact of gender, time line horizon and varied sports can make a difference to the ranking result.

<!-- b000145 | prose | pages [7] -->
In order to solve this problem, we collected a large amount of statistics. Considered the purpose is to build a coach judging model as reasonable as possible and present our model’s top 5 coaches in each 3 different sports, we applied all the statistics to test the model and ranking the coaches whose statistics have been pre-processed. Hereby, there is guarantee in accuracy and efficiency for the model.

<!-- b000146 | furniture | pages [8] -->
Team # 29696

<!-- b000147 | heading | pages [8] -->
2. Assumptions

<!-- b000148 | furniture | pages [8] -->
Page 6 of 42

<!-- b000149 | caption | pages [8] -->
Table 1.

<!-- b000150 | prose | pages [8] -->
General assumption

<!-- b000151 | heading | pages [8] -->
Assumptions

<!-- b000152 | prose | pages [8] -->
The factors used in this model are qualified to represent a comprehensive ability of college sports coaches.

<!-- b000153 | prose | pages [8] -->
The data used in this paper are real and effective and the coach ability can be well-judged by the data.

<!-- b000154 | prose | pages [8] -->
The relation between difficulty coefficient and time ling horizon is positive linear.

<!-- b000155 | prose | pages [8] -->
The coaching difficulty and social influence are the only factors affected by time line horizon.

<!-- b000156 | heading | pages [8] -->
Justification of assumptions

<!-- b000157 | prose | pages [8] -->
There are many ways of valuing a coach. For simplifying the mathematical model, we picked some of the quantifiable and non-quantifiable factors. Factors we haven’t picked out can be explained by the factors we used in this model.

<!-- b000158 | prose | pages [8] -->
The data source in this paper is authorized statistics website. College coach’s ability can be judged by the data.

<!-- b000159 | prose | pages [8] -->
We adjust the difficulty coefficient according to the difficulty caused by different generations. After analysis, we find that the degree of difficulty varies with generation shows an increasing trend. Other factors caused by generation are considered to be explained by the two modification coefficient.

<!-- b000160 | heading | pages [8] -->
3. Factors Analysis Model Based on

<!-- b000161 | prose | pages [8] -->
Principal Component Analysis

<!-- b000162 | heading | pages [8] -->
3.1. Model overview

<!-- b000163 | prose | pages [8] -->
In this topic, we found that there are 12 factors affecting the ability evaluation of coaches after data collecting [1]. In order to simplify the data processing, we used Principal Component Analysis (PCA) to find the core components.

<!-- b000164 | prose | pages [8] -->
The results provide a three-component factor assemblage. The three components each can represent an inner ability of the coach.

<!-- b000165 | furniture | pages [9] -->
Team # 29696

<!-- b000166 | furniture | pages [9] -->
Page 7 of 42

<!-- b000167 | heading | pages [9] -->
3.2. Justification of our approach

<!-- b000168 | prose | pages [9] -->
PCA, is a statistical procedure concerned with elucidating the covariance structure of a set of variables. In particular it allows us to identify the principal directions in which the data varies.

<!-- b000169 | prose | pages [9] -->
In this project, firstly, we make a survey on 60 coaches(30 males 30 females), who are from NCCAB (National Committee Association America Basketball). The game of basketball in American college is used as an example. Then we collected the data including tenure, the number of the games has been directed, experiences in NCCA, the number of the games wins and losses all counted respectively, the number of the teams have been directed, the winning rate, the times of final four in NCCA and the times of championships in NCCA, the number of championships in other games such as tournaments and regular seasons, social influence which mainly accounted by the amount of searches on Google and the number of significant awards have been won. In this process, the fact of gender, time line horizon is out of consideration.

<!-- b000170 | prose | pages [9] -->
Therefore, the factors mentioned above are listed as follows.

<!-- b000171 | heading | pages [9] -->
1. Tenure: the term during which the coach conducts a team

<!-- b000172 | prose | pages [9] -->
2. Games: directed: the number of the games have been directed

<!-- b000173 | heading | pages [9] -->
3. Tenure in: NCAA: tenure when the coach attended NCAA

<!-- b000174 | prose | pages [9] -->
4. Games won: the number of the games have been won 5. Games lost: the number of the games have been lost 6. Teams directed: the number of the teams have been directed 7. Winning rate: the percentage of the games has been won in al games directed 8. Final four in NCAA: the number of the times when the coach’s s team was in final 4 in NCAA

<!-- b000175 | heading | pages [9] -->
9. Championship in NCCA: the number of the times when the coach’s s team

<!-- b000176 | prose | pages [9] -->
won the championship

<!-- b000177 | heading | pages [9] -->
10. Championship in other games: the number of the times when the coach’s s

<!-- b000178 | prose | pages [9] -->
team won the championship in other games

<!-- b000179 | heading | pages [9] -->
11. Social influence: the amount of searches on Google

<!-- b000180 | prose | pages [9] -->
12. Significant Awards: the number of the significant awards have been won.

<!-- b000181 | prose | pages [9] -->
The factors are justified because:

<!-- b000182 | prose | pages [9] -->
 With the development of sports, coaches can be evaluated in increasing factors. But elder coaches are not included in some of the new factors. In order to be fair, we chose factors that are shared by coaches in different generations.

<!-- b000183 | prose | pages [9] -->
 There are also many non-quantifiable factors that can reflect the coach's ability. For a more comprehensive measure of evaluating the coaches, we quantify some non-quantifiable factors and take them into consideration. For example, as for the factor of social influence, we use searches on Google to represent it.

<!-- b000184 | furniture | pages [10] -->
Team # 29696

<!-- b000185 | furniture | pages [10] -->
Page 8 of 42

<!-- b000186 | prose | pages [10] -->
 Other minor factors out of the consideration can be covered by the existing factors, such as the factor of salary. In this way, we avoid the factor repetition and hereby simplify the calculation.

<!-- b000187 | heading | pages [10] -->
3.3. Model formulation

<!-- b000188 | prose | pages [10] -->
X ~ X are used to represent the 12 factors above. Hence, we get an 60×12 1 12 matrix. Considering the large sorts of the factors, we will apply dimension reduction with the PCA process.

<!-- b000189 | prose | pages [10] -->
Through PCA process, we analyze the standardized factors data and build a correlation matrix. Through the correlation matrix’ s eigenvalue and eigenvector, we figure out inner relation across several factors in the origin data sample. The factors whose inner relations with each other are strong are classified as a new component,   named principle component. iZ ( i 1,2,..., ) p ( p 12)  are used to represent the inner connection among some of Z Z , ,..., Z ( m p ) 1 2 m the factors above. It can be demonstrated as the following equation,      Z a X a X a X 1 11 1 12 2 1 p p       Z a X a X a X  m m 1 1 m 2 2 mp p       2 2 2 a a a 1 (1 i m ) where, and Z Z , ,..., Z ( m p ) is the first, i 1 i 2 ip 1 2 m second,…principle component.

<!-- b000190 | prose | pages [10] -->
In order to eliminate the downturn impact caused by the dimension and the order of magnitude according to the statistics collected. We process the data with the approach of z-score standardization, based on the formula as follows,  X E   i i X ' (1 i p ) i S i

<!-- b000191 | prose | pages [10] -->
where iE is the mean value of the factors of group i , iS is the variance value of the factors of group i .

<!-- b000192 | prose | pages [10] -->
Then we can get the standardized data matrix., and we can work on the correlation coefficient through the standardized data. Accordingly, we get the correlation matrix R as follows,   r r r 11 12 1 p   r    21 R    r r     p 1 pp where,

<!-- b000193 | prose | pages [10, 11] -->
n    ( x x )( x x ) i j ki kj      i j , 1,2,3 , p k 1 r ij n n     2 2 ( x x ) ( x x ) i j ki kj   k 1 i 1         , ( 0) ie (1 i p ) Each eigenvalue , is with an eigenvector , 1 2 p 1 2 p i refers to the eigenvalue while  ie (1 i p ) where refers to the eigenvector. Each i of the correlation matrix and its eigenvector ie is with a possible eigenvalue iZ . principle component The eigenvalue of the correlation matrix satisfies the equation,   det( iI R ) 0

<!-- b000194 | furniture | pages [11] -->
Team # 29696

<!-- b000195 | furniture | pages [11] -->
Page 9 of 42

<!-- b000197 | prose | pages [11] -->
where I is an identity matrix.

<!-- b000198 | prose | pages [11] -->
iV of the eigenvalues, based on the Then we can get the contribution rate formula as follows,

<!-- b000199 | prose | pages [11] -->
     i V i 1,2,3 , p i p   k  k 1

<!-- b000200 | prose | pages [11] -->
V is, In advance, the cumulative contribution rate m

<!-- b000201 | prose | pages [11] -->
i   i     i 1 V i 1,2,3 , p m p   k  k 1

<!-- b000202 | prose | pages [11] -->
In general, the variable correspondence to the eigenvalues whose cumulative V is from 95% to 75% is regarded as the first, second,.. principle contribution rate m component respectively. Based on the cumulative contribution rate of correlation Z Z and matrix’ s eigenvalue, through SPSS17.0, we get the principle components 1 2 Z .The results is shown in Table 2. 3

<!-- b000203 | caption | pages [11] -->
Table 2.

<!-- b000204 | prose | pages [11] -->
Result of PCA process Component % of Variance Cumulative %

<!-- b000205 | prose | pages [11, 12] -->
1 52.395 52.395 2 16.050 68.445 3 8.521 76.966 4 6.323 83.289 5 4.898 88.187 6 4.416 92.602 7 3.788 96.390 8 1.742 98.132 9 1.098 99.230 10 0.474 99.705 11 0.295 100.000 0.13 12 100.000 Z and

<!-- b000206 | furniture | pages [12] -->
Team # 29696

<!-- b000208 | furniture | pages [12] -->
Page 10 of 42

<!-- b000209 | prose | pages [12] -->
Z is shown as follow. Z , The Component Matrix of 2 1 3

<!-- b000210 | caption | pages [12] -->
Table3.

<!-- b000211 | prose | pages [12] -->
Component Matrix

<!-- b000212 | prose | pages [12] -->
Z Factors

<!-- b000213 | prose | pages [12] -->
Tenure .928 NCAA Tenure .842 Wins .971 Losses .711 Games .948 Winning Rate .631 Teams .255 NCAA Final Fours .791 NCAA Champions .574 Conference Champion .757 Googles .042 awards .613

<!-- b000214 | heading | pages [12] -->
3.4. Result analysis

<!-- b000215 | prose | pages [12] -->
It is indicated that,  The first Principal Component Z Z 2 1 3

<!-- b000216 | prose | pages [12] -->
.271 .032 .100 -.151 .142 -.003 .598 .055 .276 .013 -.324 -.001 .716 -.017 -.473 .012 -.582 -.031 -.271 .105 -.037 .987 -.366 -.095

<!-- b000217 | prose | pages [12, 13] -->
Z is relatively bond with the factors of 1 experiences in career, experiences in NCCA, the number of the games wins and losses, the winning rate, the times of final four in NCCA and the times of championships in NCCA, and the number of significant awards have been Z can be described as a coach-ability variable. won. Consequently, 1  The second Principal Component Z is relatively bond with the factors of 2 the number of the teams have been directed, and the times of championships Z can be described as a coach-influence-college in NCCA. Hence, 2 variable.  The third Principal Component Z is relatively bond with the factors of 3 social influence which mainly accounted by the amount of searches on Z can be described as a coach-influence-society Google. Therefore, 3 variable. The degree of influence count down is Z Z and , Z . Based on the analysis of the 1 2 3 Z and Z is the biggest, with eigenvalue, the eigenvalue of 1 Z following it. 2 3 Z , which is the “coach-ability” Therefore, we believe that the factors belonged to 1 variable contributes most to the “coach evaluation system”. It is shown as follows in Fig. 1 60

<!-- b000218 | furniture | pages [13] -->
Team # 29696

<!-- b000219 | furniture | pages [13] -->
Page 11 of 42

<!-- b000221 | prose | pages [13] -->
50

<!-- b000222 | prose | pages [13] -->
40

<!-- b000223 | prose | pages [13] -->
Z1 30 Inflence Z2

<!-- b000224 | prose | pages [13] -->
Z3 20

<!-- b000225 | prose | pages [13] -->
10

<!-- b000226 | prose | pages [13] -->
0 Principal Component

<!-- b000227 | prose | pages [13] -->
Fig 1. The Influence of Principal Components

<!-- b000228 | heading | pages [13] -->
4. Coaches Ranking Model Based on Cosine

<!-- b000229 | prose | pages [13] -->
Similarity

<!-- b000230 | heading | pages [13] -->
4.1. Model overview

<!-- b000231 | prose | pages [13] -->
In this topic,  in order to select the best college coach or coaches (past or present) from among either male or female coaches in such sports as college hockey or field hockey, football, baseball or softball, basketball, or soccer, we take the basketball game is used as example. We establish a standard——“idealistic coach”, which is a virtual coach whose factors data are the best of all. Then, based on the idea of vector space mapping, we apply Cosine Similarity and its adjustment to compare all coaches with the “idealistic coach”. Coaches with higher similarity to the   “idealistic coach” are expected to take a better seat in the ranking list. When it comes to the computation of the model, we use Euclidean distance-based clustering analysis to process the data. In this way, we obtain the college coaches ranking result in the field of basketball.

<!-- b000232 | heading | pages [13] -->
4.2. Model justification

<!-- b000233 | prose | pages [13] -->
In this model, Cosine Similarity is used to compare the assessed coach’s every factors to the all twelve factors set as the best.

<!-- b000234 | prose | pages [13, 14] -->
The measure of similarity is to calculate the degree of similarity between individuals. Cosine Similarity is an approach to measure the gap between two identities. Firstly, we map the data of each individual to the vector space. Then we measure the similarity between them by measuring the cosine value of the angle between the two individuals with dot product in vectors space [6]. The more it is close to 1, the more the vector angle is close to 0 degree, which means more similar the two vectors are. The more it is close to 0, the more the vector angle is close to 90 degree, which means less similar the two vectors are.

<!-- b000235 | furniture | pages [14] -->
Team # 29696

<!-- b000236 | furniture | pages [14] -->
Page 12 of 42

<!-- b000238 | prose | pages [14] -->
The angle between two vectors is small，so they are similar. B 10° O A

<!-- b000239 | prose | pages [14] -->
B The angle between two vectors is large，so they are not similar.

<!-- b000240 | prose | pages [14] -->
68° A O

<!-- b000241 | prose | pages [14] -->
Fig 2.Explanation of Cosine Similarity

<!-- b000242 | prose | pages [14] -->
In this project, we rank all the coaches by calculating the similarity between the vector of each coach and the set vector of the virtual “idealistic coach”. The higher the similarity is, the closer to the top seat in the ranking.

<!-- b000243 | prose | pages [14] -->
The cosine value between two vectors can be easily obtained through Euclidean dot product equation,

<!-- b000244 | prose | pages [14] -->
   a b a b cos

<!-- b000245 | prose | pages [14] -->
where cos is the similarity between the two vectors.

<!-- b000246 | prose | pages [14] -->
Then we obtain the formula of individual similarity as,      x , x ... x x , x ... x X X    i 1 i 2 in s 1 s 2 sn i s cos X X n n       2 2 i s  x x ij sj   j 1 j 1

<!-- b000247 | heading | pages [14] -->
4.3. Model formulation

<!-- b000248 | heading | pages [14] -->
4.3.1. Vector definition of the “idealistic coach” and ranking

<!-- b000249 | prose | pages [14] -->
In this topic, there are 12 factors that make impacts on the ranking of coaches, after data analysis. Accordingly, standardized vector’s dimension is eleven.

<!-- b000250 | prose | pages [14] -->
Considering the large amount of the data, we classified all the coaches firstly. Then we ranked the coaches from the first group, who are the best coaches of all groups. In this case, we used Euclidean distance-based clustering analysis to classification.

<!-- b000251 | furniture | pages [15] -->
Team # 29696

<!-- b000252 | furniture | pages [15] -->
Page 13 of 42

<!-- b000253 | prose | pages [15] -->
We mapped the collected factors of 60 male and female coaches to the vector  iV (1 i 60) iV is a 1× space. Then we obtained the coach’s ability factor vector . 12 row vector. And each vector component is the value of the factors.

<!-- b000254 | prose | pages [15] -->
 V ( x , x , x , x , x , x , x , x , x , x , x , x ) i i 1 i 2 i 3 i 4 i 5 i 6 i 7 i 8 i 9 i 10 i 11 i 12

<!-- b000255 | prose | pages [15] -->
Firstly, we defined a standard vector to combine the factors with cosine similarity so as to ranking the coaches. We defined the vector in reality as a coach whose achievement is beyond all ever, which is the “idealistic coach”. The data of his factors are picked from the highest ones. Table 4.

<!-- b000256 | caption | pages [15] -->
Table 4.

<!-- b000257 | prose | pages [15] -->
Data of „idealistic coach‟

<!-- b000258 | prose | pages [15] -->
T NC T W L G W R T NFF NCC CC G A 23.1 16.3 1204 133 1337 0.9 2 13 10 41 18.1k 11

<!-- b000259 | prose | pages [15] -->
We compared each individual vector of all coaches to the standard vector, and then we calculate the similarity between them by cosine similarity. The bigger the cosine value is, the higher the similarity is, and hereby the better the coach will be. In the ranking list, the coach is closer to the top seat. The example is as follows.

<!-- b000260 | prose | pages [15] -->
Fig 3. Comparison between coaches and the “idealistic coach”

<!-- b000261 | heading | pages [15] -->
4.3.2. Adjusted Cosine Similarity

<!-- b000262 | prose | pages [15] -->
Cosine Similarity is sensitive to direction instead of absolute value.[8] Value’s differences in each dimension, therefore, are not accessible to measure. Cosine Similarity’ s insensitivity leads the result to be less accurate. [10]For example, we 1x =(10,5). While the two of suppose two of a coach’s s factors are the highest in all, 2x =(2,1). It is obvious that there is a gap another coach’s s factors are the lowest, between the two coaches’ a ability. But the angle between the two vectors is 0 degree so cos is 1. It is illustrated in Fig 4.

<!-- b000263 | furniture | pages [16] -->
Team # 29696

<!-- b000264 | furniture | pages [16] -->
Page 14 of 42

<!-- b000265 | prose | pages [16] -->
Vector B Vector A 0° O

<!-- b000266 | prose | pages [16] -->
Fig 4. Situation when two vectors overlap

<!-- b000267 | prose | pages [16] -->
We hereby normalize all of the values to amend the unreasonable results.

<!-- b000268 | prose | pages [16] -->
The amendment equation is as follows,  x E ij j     x ' (1 i 60,1 j 12) ij  X X j max j min ijx represents the factor j of the coach i , x 'ij where is the standardized represents the minimum of factor j , X X factor, represents the maximum j min j max of factor j , E is the mean value of the data sample j . j We apply the adjustment in the example. Then we find that the angle between the     x    1' 0.5,0.5 x 2' 0.5, 0.5 vector and the vector is 180 degree. In this case, the difference between the two coaches’ ability is well presented. In fact, the example we used here is a special situation. Generally, the angle ranges from 0 degree to 180 degree and the cosine value ranges from -1 to 1, in which, 1 represents that the ability of the two coaches’ are practically same, while -1 represents that the gap between the ability of the two coaches’ are biggest.

<!-- b000269 | heading | pages [16] -->
4.3.3. Model computing by Euclidean distance-based clustering analysis

<!-- b000270 | prose | pages [16] -->
Cluster analysis is mainly used to classify factors or variables. Generally speaking, there are two procedures, data standardization and clustering.

<!-- b000271 | prose | pages [16] -->
Data standardization: Data standardization is used to normalize the statistics, in case of the statistics’ dimension gap and value differences making unreasonable impacts. We suppose that there are n  specimens, and each specimen has m ijx . The mean value is, factors, then each variable can be expressed as

<!-- b000272 | prose | pages [16] -->
n 1  x x j ij n  i 1

<!-- b000273 | prose | pages [16] -->
The standard deviation is,

<!-- b000274 | prose | pages [16] -->
n 1    2   s x x j ij ij n 1  i 1

<!-- b000275 | prose | pages [16] -->
Finally, the standardization form is,  x x   ij j   * x s 0 ij j s j

<!-- b000276 | prose | pages [16, 17] -->
Clustering:  Based on the distance between specimens and sorts, we classify a larger sort of given sorts. At the beginning, each specimen is regarded as a single sort and the distances between sorts are equal. We choose two specimens whose distances are the smallest of all. Next we calculate the distance between the new sort and other sorts. Then we merge the nearest two together. Continue this process until there is only one sort left. During this process, distance refers to the measurement used to estimate close degree among specimens. It is because each specimen and factor can ijx as the factor j , d as the distance form a matrix in the vector space. We suppose ij between specimen i and other specimen. There are several ways of calculating the distance between sorts, such as, single linkage, the longest distance method, group average method, and centroid method. In this problem, we apply single linkage to clustering analysis.

<!-- b000277 | furniture | pages [17] -->
Team # 29696

<!-- b000278 | furniture | pages [17] -->
Page 15 of 42

<!-- b000280 | prose | pages [17] -->
Single linkage can be described as follows.

<!-- b000281 | prose | pages [17] -->
First of all, we need to know about the distance called Minkowski . The most common method to calculate the distance is Minkowski 1/ q   p    q   d x x   ij ik jk    k 1 q  2 When d is called Euclidean distance. ij 1/2   p     2   d 2 x x   ij ik jk    k 1 G 、 G 、 G as three respective sort, then we get the formula as We suppose p q r follows,    D ( , ) p q min{ d j G l , G } k jl p q G with sort G as sort G . So the distance formula is, Then we merge the sort p q r

<!-- b000282 | prose | pages [17] -->
   2 D min d min{ min d , min d } min{ D , D } kr ij ij ij kp kq       X G , X G X G , X G X G , X G i k j r i k j p i k j q

<!-- b000283 | prose | pages [17] -->
Fig 5 shows the demonstration of Cluster Analysis.

<!-- b000284 | prose | pages [17, 18] -->
Fig 5. Demonstration of Cluster Analysis.[21] Continuing the process, we classify the 60 coaches into nine levels, of which, there are 24 coaches in the first five levels. Finally, we get the results of the clustering analysis is shown in Table 5.

<!-- b000285 | furniture | pages [18] -->
Team # 29696

<!-- b000286 | furniture | pages [18] -->
Page 16 of 42

<!-- b000288 | caption | pages [18] -->
Table 5.

<!-- b000289 | prose | pages [18] -->
Result of clustering analysis Name Cluster Name Cluster Name Cluster

<!-- b000290 | prose | pages [18] -->
6:John 1:John Wooden 1 3 8:Tom Izzo 4 Calipari 7:Denny 2:Dean Smith 2 3 9:Billy Donovan 4 Crum

<!-- b000291 | prose | pages [18] -->
4:Mike Krzyzewski 2 12:Bill Self 3 19:Jack Gardner 4

<!-- b000292 | prose | pages [18] -->
13:Rick 5:Adolph Rupp 2 3 22:Thad Matta 4 Pitino 15:Jerry 11:Jim Calhoun 2 3 23:Sean Miller 4 Tarkanian 16:Lute 17:Jim Boeheim 2 3 25:Jay Wright 4 Olson 32:Tara 3:Roy Williams 3 3 27:Anthony Grant 4 VanDerveer

<!-- b000293 | prose | pages [18] -->
Name Cluster Name Cluster Name Cluster

<!-- b000294 | prose | pages [18] -->
41:Brenda 28:Bo Ryan 4 4 50:Sharon Versyp 4 Fres 42:Tina 29:Jim Valvano 4 4 51:Pam Borton 4 Martin 43:Jamelle 30:Jamie Dixon 4 4 52:Joanne Boyle 4 Renee Elliott 33:Kimberly Duane 44:Deb 4 4 53:Nikki Caldwell 4 Mulkey Patterson 46:Sue 35:JoanneMcCallie 4 4 55:Kellie Harper 4 Semrau 47:Suzy 56:Kim Barnes 36:Sherri Coale 4 4 4 Merchant Arico 48:MaChelle 57:Melissa 39:Jennifer Rizzotti 4 4 4 Joseph McFerrin

<!-- b000295 | furniture | pages [19] -->
Team # 29696

<!-- b000296 | furniture | pages [19] -->
Page 17 of 42

<!-- b000297 | heading | pages [19] -->
4.4. Results analysis

<!-- b000298 | caption | pages [19] -->
Table 6.

<!-- b000299 | prose | pages [19] -->
Ranking result of cosine similarity model Ranking Name. Gender

<!-- b000300 | prose | pages [19] -->
1 John Wooden M 2 Geno Auriemma F(M) 3 Pat Summitt F 4 Dean Smith M 5 Mike Krzyzewski M 6 Roy Williams M 7 John Calipari M 8 Bill Self M 9 Adolph Rupp M 10 John Thompson M

<!-- b000301 | prose | pages [19] -->
From the results above, we obtain result analysis as follows,  Analyzing the top few of the factors in the ranking list, we find that each basic factor has played a role in the ranking. Therefore, the pick of these rankings is reasonable.

<!-- b000302 | prose | pages [19] -->
 There are differences in some factors across different time line horizon, such as the searches on Google, winning rate, the games won by the coach and so on. Therefore, it should be a modification considering the impact of timeline horizon.

<!-- b000303 | prose | pages [19] -->
 There are differences in some factors across both genders.

<!-- b000304 | heading | pages [19] -->
5. Model Optimization of Time Line

<!-- b000305 | prose | pages [19] -->
Horizon Based on Regression Analysis

<!-- b000306 | heading | pages [19] -->
5.1. Justification of our generation-based model optimization

<!-- b000307 | prose | pages [19] -->
With the gradual development of NCAA, the number of teams attending the NCAA basketball game is changing. Accordingly, the difficulty and pressure the coach faces is changing. Besides, with the development of science and technology, the social influence of basketball is affected by internet transmission. Therefore, model optimization is supposed to consist of the coaching difficulty optimization and the social influence optimization.

<!-- b000308 | heading | pages [19] -->
5.2. Generation-based model optimization

<!-- b000309 | heading | pages [19] -->
5.2.1. Giant effect

<!-- b000310 | prose | pages [19, 20] -->
When considering the difficulty coefficient brought by time line horizon, we supposed that the difficulty is positively related to time line horizon. So we set the coefficient as a value between 1 and 1.5. However, younger coaches can learn from the elder ones. With such endowed advantage, younger coaches are expected a relatively better performance. Still, we set the difficulty coefficient below 1.5. So we consider it as a minor influence instead of paying too much attention.

<!-- b000311 | furniture | pages [20] -->
Team # 29696

<!-- b000312 | furniture | pages [20] -->
Page 18 of 42

<!-- b000314 | heading | pages [20] -->
5.2.2. Coaching difficulty optimization

<!-- b000315 | prose | pages [20] -->
After analysis, we believe that there is a significant impact on the factor of winning rate caused by different coaching time line horizon. In early times, the teams that participated NCAA games are less, and hereby, they got a greater chance of winning, compared with those today. However, with the progressive development of NCAA games, teams participate in are much more. As a result, the pressure is higher to not only players but also coaches and the opportunity to win is harder to earn.

<!-- b000316 | prose | pages [20] -->
We carried on the statistics of the active coaches in NCAA from 1942 to 2013. [3].Here is the approximate linear relationship between the number of active coaches and the time line horizon in Fig 6. based on regression analysis.

<!-- b000317 | prose | pages [20] -->
Fig 6. Approximate linear relationship between the number of active coaches and the time line horizon

<!-- b000318 | prose | pages [20] -->
Based on the result of regression analysis, we found that the number of active coaches and the time line horizon satisfy the equation,

<!-- b000319 | prose | pages [20] -->
  A t ( ) 0.734 t 1421.8

<!-- b000320 | prose | pages [20] -->
We believe that the difficulty coefficient of a match is directly proportional to the number of active coaches each year. Hence, it can be expressed as follows,

<!-- b000321 | prose | pages [20, 21] -->
 D t ( ) k A t ( ) Based on the formal equations, we get the relation between the difficulty coefficient of a match and time line horizon as follows,

<!-- b000322 | furniture | pages [21] -->
Team # 29696

<!-- b000323 | furniture | pages [21] -->
Page 19 of 42

<!-- b000325 | prose | pages [21] -->
 0.734 t 1421.8  D t ( ) k

<!-- b000326 | prose | pages [21] -->
k , therefore, 1 where we suppose

<!-- b000327 | prose | pages [21] -->
  D t ( ) 0.734 t 1421.8

<!-- b000328 | prose | pages [21] -->
It is shown in Fig 7.

<!-- b000329 | prose | pages [21] -->
70

<!-- b000330 | prose | pages [21] -->
60

<!-- b000331 | prose | pages [21] -->
50

<!-- b000332 | prose | pages [21] -->
40 Difficulty 30

<!-- b000333 | prose | pages [21] -->
20

<!-- b000334 | prose | pages [21] -->
10

<!-- b000335 | prose | pages [21] -->
0 1950 1960 1970 1980 1990 2000 2010 2020 Years

<!-- b000336 | prose | pages [21] -->
Fig 7. Relation between Coaching difficulty and Generation

<!-- b000337 | prose | pages [21] -->
Considering the fact that there are coaches whose career life is over a relatively long time period, we looked up the year when the coach started coaching and the year when the coach stopped coaching, instead of measuring the comprehensive difficulty  iC (1 i 60) coefficient by a single year. [5]We define as the comprehensive difficulty coefficient in coach i ’s whole career life. The formula is as follows,

<!-- b000338 | prose | pages [21] -->
1 end T    i C D (t)dt (1 i 60) i  end start T T start T i i i

<!-- b000339 | prose | pages [21] -->
C with Max-min method ,we can obtain C Standardizing i si  C C   i min C (1 i 60) si  C C max min

<!-- b000340 | prose | pages [21, 22] -->
C values of which is above 0.5 Because of the ‘Effect of Giants’, we let all the si C is as follows, ' be 0.5. Hence,   1.5 C 0.5 si   C ' (1 i 60)  i   C 1 C 0.5  si

<!-- b000341 | furniture | pages [22] -->
Team # 29696

<!-- b000342 | furniture | pages [22] -->
Page 20 of 42

<!-- b000344 | prose | pages [22] -->
1.6

<!-- b000345 | prose | pages [22] -->
1.5

<!-- b000346 | prose | pages [22] -->
1.4

<!-- b000347 | prose | pages [22] -->
1.3 C'

<!-- b000348 | prose | pages [22] -->
1.2

<!-- b000349 | prose | pages [22] -->
1.1

<!-- b000350 | prose | pages [22] -->
1 1 1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9 2 C+1

<!-- b000351 | prose | pages [22] -->
Fig 8.  Adjustment of Difficulty Coefficient

<!-- b000352 | heading | pages [22] -->
5.2.3. Social influence optimization

<!-- b000353 | prose | pages [22] -->
With the popularization of sports events and development of internet technology, the social influence of basketball is rising. Hereby, college coaches’ visibility is also rising. It is illustrated by the amount of searches on Google. Therefore, there is a significant impact on the amount of searches results on Google in different time line horizon. A reasonable optimization coefficient is needed to minimize this impact.

<!-- b000354 | prose | pages [22] -->
It is obvious that coaches in earlier years are less possible to obtain an idealistic search result. So the start coaching year is positively relation to the search results. In order to weaken the positive relation, we let the search results divided by a coefficient which is above 1. That is to say, we add 1 to the standardized result. We hereby get statistics in the section of [1,2]. The formula is as follows,

<!-- b000355 | prose | pages [22] -->
 s s  min G = 1  s s max min

<!-- b000356 | prose | pages [22] -->
Where s is the start coaching year for each coach, G is the social influence optimization coefficient.

<!-- b000357 | heading | pages [22] -->
5.3. Generation-based model Optimization results

<!-- b000358 | prose | pages [22] -->
C , and ' Based on the formal analysis, we multiply the optimization coefficient divide the amount of searches results on Google byG . Then we continue to model calculate through cosine similarity as illustrated before.

<!-- b000359 | furniture | pages [23] -->
Team # 29696

<!-- b000360 | furniture | pages [23] -->
Page 21 of 42

<!-- b000361 | heading | pages [23] -->
5.4. Generation-based results analysis

<!-- b000362 | prose | pages [23] -->
The final result is in Table 7.

<!-- b000363 | caption | pages [23] -->
Table 7.

<!-- b000364 | heading | pages [23] -->
Final ranking result

<!-- b000365 | prose | pages [23] -->
Ranking Name. Gender

<!-- b000366 | prose | pages [23] -->
1 John Wooden M 2 Geno Auriemma F(M) 3 Pat Summitt F 4 Dean Smith M 5 Mike Krzyzewski M 6 Roy Williams M 7 John Calipari M 8 Bill Self M 9 Adolph Rupp M 10 Billy Donovan M

<!-- b000367 | caption | pages [23] -->
Table 8.

<!-- b000368 | prose | pages [23] -->
Camparson of the 2 ranking result before time optimized After time optimized

<!-- b000369 | prose | pages [23] -->
Ranking Name. Gender 1 John Wooden John Wooden 2 Geno Auriemma Geno Auriemma 3 Pat Summitt Pat Summitt 4 Dean Smith Dean Smith 5 Mike Krzyzewski Mike Krzyzewski 6 Roy Williams Roy Williams 7 John Calipari John Calipari 8 Bill Self Bill Self 9 Adolph Rupp Adolph Rupp 10 John Thompson Billy Donovan

<!-- b000370 | prose | pages [23] -->
Therefore, we analyzed the result as follows,  When considering the difficulty coefficient, we put the difficulty of winning with increasing numbers of teams year by year as a core indicator. However, Young coaches can usually learn from the reference according to previous experience. The foundation laid by the old coach cannot be ignored.

<!-- b000371 | prose | pages [23] -->
Therefore, the difficulty coefficient should not be too high. Eventually, we set its maximum as 1.5.

<!-- b000372 | furniture | pages [24] -->
Team # 29696

<!-- b000373 | furniture | pages [24] -->
Page 22 of 42

<!-- b000374 | prose | pages [24] -->
 It is obvious that, after comparison the ranking of before and after the optimization, the overall ranking hasn’t changes tremendously. Only those whose tenure has some obvious features are adjusted slimly in the ranking.

<!-- b000375 | prose | pages [24] -->
 After comprehensive analysis of the factors data adjusted of the ranked coaches, we can see that the modified ranking result is more reasonable.

<!-- b000376 | prose | pages [24] -->
Therefore, the optimization model is relatively correct.

<!-- b000377 | heading | pages [24] -->
6. Model Optimization of Gender Based

<!-- b000378 | prose | pages [24] -->
on Data Whitening

<!-- b000379 | heading | pages [24] -->
6.1. Justification of our gender-based model optimization

<!-- b000380 | prose | pages [24] -->
By the optimization model as above, we considered the time line horizon and achieved the modifying of the origin model. Still, the gender difference has a significant impact on the coach ranking result. Therefore, we believe that there is significant difference among some factors, affected by the intense degree and competition pressure in matches across both gender.

<!-- b000381 | prose | pages [24] -->
In order to figure out which factor will be affected by the factor of gender, we apply analysis of variance (ANOVA) to test whether or not there is a significant difference of factors modified by time line horizon across both genders. Because the gender factor is the single consideration, we apply one way analysis of variance (ANOVA) in this problem.[23] ix is supposed as one single factor of coaches, and ix is supposed as the mean value of the factor. N refers to the number of the coach kinds, which is 2 considering the gender factor. Therefore, Factor：  2 2   SSA n y N y i i i i Error：   2   2 SSE y n y ,i k i i i k i Mean squares：

<!-- b000382 | prose | pages [24] -->
SSA SSE   MSSA MSSE  ,  I 1 N I

<!-- b000383 | prose | pages [24] -->
F value:

<!-- b000384 | prose | pages [24, 25] -->
MSSA  F MSSE     p P F c Probability   I 1, N I In this problem, we use hypothesis tests in the analysis of variance, that is , to H assuming that all the average observed measures are the average propose 0 observed measures are the same. If the value of the probability p <, with  0.05 H should be rejected. Otherwise, the the selected confidence level, the hypothesis 0 hypothesis cannot be rejected.

<!-- b000385 | furniture | pages [25] -->
Team # 29696

<!-- b000386 | furniture | pages [25] -->
Page 23 of 42

<!-- b000388 | prose | pages [25] -->
We input the two groups of data belong to male and female coaches respectively in SPSS, and the result is illustrated in Table 9.

<!-- b000389 | caption | pages [25] -->
Table 9.

<!-- b000390 | prose | pages [25] -->
Result of ANOVA

<!-- b000391 | prose | pages [25] -->
Factors NC T W L G W R T NFF NCC CC G Sig. 0.002 0.381 0.004 0.013 0.006 0.002 0.008 0.301 0.000 0.108 （p ） From the given table, for the factor of Los, p >, we hereby accept the hypothesis. That is to say, this factor makes less difference across both genders. However, for the factors of, NCAAExp(NCT), Win（W）, WinRate,(WR) p <, so we rejected the hypothesis ,which is, the factors mentioned have significant difference across both genders.

<!-- b000392 | prose | pages [25] -->
Hence,  The factor of gender makes difference on majority of the factors. A modifying approach is needed.

<!-- b000393 | prose | pages [25] -->
 Not all of factors across both genders are affected. Consequently, our purpose of optimizing the model can be completed by modifying the factors influenced.

<!-- b000394 | heading | pages [25] -->
6.2. Gender-based model optimization

<!-- b000395 | prose | pages [25] -->
In this topic, we apply the approach of Data Whitening [23]to eliminate the impact caused by the gender difference. The factor of games won is used to demonstrate how the approach is applied.

<!-- b000396 | prose | pages [25] -->
According to the results from ANOVA as above, we know that the factors of games won across both genders are different. The variance of the factors of games won is demonstrated in Table 10.

<!-- b000397 | caption | pages [25] -->
Table 10.

<!-- b000398 | prose | pages [25] -->
Var. comparison between genders on ‘win games’ Factors N Std. Deviation Variance

<!-- b000399 | prose | pages [25, 26] -->
Games Won of male 30 333.96398 111531.941 Games Won of female 30 383.33084 146942.534 390 Std.

<!-- b000400 | furniture | pages [26] -->
Team # 29696

<!-- b000401 | furniture | pages [26] -->
Page 24 of 42

<!-- b000403 | prose | pages [26] -->
380 Deviation 370 360 Std. Deviation of 350 malecoach Wins 340 Std. Deviation of 330 femalecoach Wins 320 310 300 malecoach or femalecoach

<!-- b000404 | prose | pages [26] -->
Fig 9 Variance Comparison of Wins across gender

<!-- b000405 | prose | pages [26] -->
Then we use the approach of Data Whitening to make the factor of games won consistent, in order to eliminate the impact of gender difference.

<!-- b000406 | prose | pages [26] -->
E The mean value of the factor of games won by male coaches is supposed as , mw n  ( 30)   x x 2... x  mw 1 mw mwn E mw n E , The mean value of the factor of games won by female coaches is supposed as fw

<!-- b000407 | prose | pages [26] -->
  x x 2... x fw 1 fw fwn  E fw n

<!-- b000408 | prose | pages [26] -->
2 S The variance of the factor of games won by male coaches is supposed as mw

<!-- b000409 | prose | pages [26] -->
n    2  x E mwi mw  2  i 1 S mw  n 1 2 S The variance of the factor of games won by female coaches is supposed as fw

<!-- b000410 | prose | pages [26] -->
n    2  x E fwi fw  2  i 1 S fw  n 1

<!-- b000411 | prose | pages [26] -->
Because the variance value of female coaches is higher, we can make the variance value of female and the variance value of male be consistent by data whitening formula. Hence, the optimization formula based on variance is as follows,    x E fwi fw   x ' E fwi fw 2 S fw 2 S mw

<!-- b000412 | furniture | pages [27] -->
Team # 29696

<!-- b000413 | furniture | pages [27] -->
Page 25 of 42

<!-- b000414 | heading | pages [27] -->
6.3. Gender-based optimization results

<!-- b000415 | prose | pages [27] -->
The optimized variance result is demonstrated in Table 11.

<!-- b000416 | caption | pages [27] -->
Table 11.

<!-- b000417 | prose | pages [27] -->
Var. of ‘win games’ after adjusted Factors N Std. Deviation Variance

<!-- b000418 | prose | pages [27] -->
Games Won of male 30 333.96398 111531.941 Games Won of female 30 333.89086 111483.103

<!-- b000419 | prose | pages [27] -->
Std. Deviation of 340 malecoach

<!-- b000420 | prose | pages [27] -->
Std. Deviation of femalecoach 330

<!-- b000421 | prose | pages [27] -->
320

<!-- b000422 | prose | pages [27] -->
310

<!-- b000423 | prose | pages [27] -->
300 Male coach or Female coach

<!-- b000424 | prose | pages [27] -->
Fig 10.  Modified Variance of Wins

<!-- b000425 | prose | pages [27] -->
In this way, the influence made by the factor of gender can be eliminated. So other factors affected by the gender can be processed by data whitening in the same way. The result is in appendix.

<!-- b000426 | prose | pages [27] -->
Then we apply the cosine similarity to the results.

<!-- b000427 | heading | pages [27] -->
6.4. Gender-based results analysis

<!-- b000428 | prose | pages [27] -->
The ranking list after gender optimization and time line horizon optimization is shown in Table 12.

<!-- b000429 | furniture | pages [28] -->
Team # 29696

<!-- b000430 | furniture | pages [28] -->
Page 26 of 42

<!-- b000431 | caption | pages [28] -->
Table 12.

<!-- b000432 | prose | pages [28] -->
Ranking result after gender factor adjusted Ranking Name. Gender

<!-- b000433 | prose | pages [28] -->
1 John Wooden M 2 Geno Auriemma F(M) 3 Pat Summitt F 4 Dean Smith M Mike Krzyzewski 5 M 6 Roy Williams M 7 Adolph Rupp M 8 John Calipari M 9 Tara VanDerveer F 10 Tom Izzo M

<!-- b000434 | prose | pages [28] -->
Based on the results, we have analysis as follows,  It is obvious that, after comparison the ranking of before and after the optimization, the overall ranking hasn’t t changed tremendously. Part of the ranking of female coaches declined slightly overall.

<!-- b000435 | prose | pages [28] -->
 The influence caused by the gender factor can be eliminated at some point by data whitening.

<!-- b000436 | prose | pages [28] -->
 Although the ranking of female coaches declined slightly overall, the ranking of female coaches whose seat is in front of others haven’t changed a bit.

<!-- b000437 | prose | pages [28] -->
Therefore, the optimization model is relatively correct.

<!-- b000438 | prose | pages [28] -->
 We obtain the final ranking list with the consideration of gender and time line horizon.

<!-- b000439 | heading | pages [28] -->
7. Model Extension

<!-- b000440 | heading | pages [28] -->
7.1. Establishment of factors pool

<!-- b000441 | prose | pages [28] -->
The mathematical model above has provided a relatively reasonable ranking result. Hence, we can classify sports coaches according to the factors by pushing this model further to other sports. Considering that the factors in each sport can be varied, but the principle and basic model are the same, we hereby establish a factors pool, which includes all the factors across sports when ranking the college coaches.  In this way, a coach in some sport can be ranked by the factors belong to the sport. After screening out the factors, we apply the formal mathematical model to ranking the coaches.

<!-- b000442 | prose | pages [28] -->
The factors pool is demonstrated in Fig 11. The sports of basketball, football and baseball are considered.

<!-- b000443 | furniture | pages [29] -->
Team # 29696

<!-- b000444 | furniture | pages [29] -->
Page 27 of 42

<!-- b000445 | prose | pages [29] -->
Tenure

<!-- b000446 | prose | pages [29] -->
Tenure in NCAA

<!-- b000447 | prose | pages [29] -->
Wins

<!-- b000448 | prose | pages [29] -->
Losses Basketball Coach Softball Coach Ranking Ranking Ties

<!-- b000449 | prose | pages [29] -->
Games

<!-- b000450 | prose | pages [29] -->
Winning Rate

<!-- b000451 | prose | pages [29] -->
Teams

<!-- b000452 | prose | pages [29] -->
Awards

<!-- b000453 | prose | pages [29] -->
Bowl Times Baseball Coach Football Coach Ranking Ranking Bowl Wins

<!-- b000454 | prose | pages [29] -->
Bowl Losses

<!-- b000455 | prose | pages [29] -->
Bowl Ties

<!-- b000456 | prose | pages [29] -->
Google Searches

<!-- b000457 | prose | pages [29] -->
Fig 11. The demonstration of Factors Pool

<!-- b000458 | prose | pages [29] -->
Merits of establishing the factors pool:  The mathematical model can be pushed further to other sports in this way. So the application range of the model is expanded.  Referring to one kind of sports, we can pick out the factors belong to the sport in the pool and complete the later ranking process. The operation is simplified.  The factors pool is a universal data base including factors of varying sports.

<!-- b000459 | prose | pages [29] -->
Such feature makes the factors pool easy to be up-dated. Other sports factors can be added to the pool at any time. plus, the factors existed in the pool can be refreshed immediately.

<!-- b000460 | furniture | pages [30] -->
Team # 29696

<!-- b000461 | furniture | pages [30] -->
Page 28 of 42

<!-- b000462 | heading | pages [30] -->
7.2. Sports extension

<!-- b000463 | prose | pages [30] -->
From the factors pool, we notice that rankings for coaches across different sports are based on the factors. Therefore, we take the ranking for football as an example to illustrate the ranking model extension.

<!-- b000464 | prose | pages [30] -->
It is illustrated in the factors pool that there are factors belong to not only basketball but also football, such as the winning rate value, games lost, tenure and so on. There are also factors that belong to football instead of basketball such as games end up with tie, winning rate of bowls and wins, losses, ties in bowls. Likewise, there are factors that belong to basketball instead of football, such as championships in NCAA and tenure in NCAA.

<!-- b000465 | prose | pages [30] -->
Hence, we use the factors needed and their data to rank the college football coaches. Then the optimized model can be applied to the coaches ranking.

<!-- b000466 | prose | pages [30] -->
Based on all of above, the ranking result of college football coaches is illustrated in Table 13.

<!-- b000467 | caption | pages [30] -->
Table 13.

<!-- b000468 | prose | pages [30] -->
Football Coach Ranking Ranking Names 1 Bear Bryant 2 Vince Dooley 3 Joe Paterno 4 Lou Holtz 5 Darrell Royal

<!-- b000469 | prose | pages [30] -->
Likewise, the ranking result of college softball and baseball coaches is shown in

<!-- b000470 | caption | pages [30] -->
Table 14. and Table 15.

<!-- b000471 | caption | pages [30] -->
Table 14.

<!-- b000472 | prose | pages [30] -->
Softball Coach Ranking Ranking Names 1 Sue Enquist 2 Sharon Backus 3 Patty Gasso 4 Sandy Jerstad 5 Judi Garman

<!-- b000473 | caption | pages [30] -->
Table 15.

<!-- b000474 | prose | pages [30] -->
Softball Coach Ranking Ranking Names 1 Ron Fraser 2 Ray Tanner 3 Bill Holowaty 4 Mike Martin 5 Ron Fraser

<!-- b000475 | furniture | pages [31] -->
Team # 29696

<!-- b000476 | furniture | pages [31] -->
Page 29 of 42

<!-- b000477 | heading | pages [31] -->
7.3. Country extension

<!-- b000478 | prose | pages [31] -->
It is demonstrated from the ranking across sports that the ranking model is universal. We hereby try to apply the model to other countries. However, there may be some difference referring to some sports in varying countries. So an update and adjustment to the formal factors pool is needed. After that, the optimized mathematical model can be used to rank college coaches in the country across sports. Through our model, we figure out the top five college basketball coaches in China is shown in Table 16.

<!-- b000479 | caption | pages [31] -->
Table 16.

<!-- b000480 | prose | pages [31] -->
Chinese Coach Ranking Ranking Names 1 Baoqiang Sun 2 Changshan Li 3 Daohong Chen 4 Guangbi Xiao 5 Huaiyu Wang

<!-- b000481 | heading | pages [31] -->
7.4. Factors extension

<!-- b000482 | heading | pages [31] -->
7.4.1. Salary

<!-- b000483 | prose | pages [31] -->
A college coach’s salary demonstrates his status in his expertise at some point. Salary levels of college sports coaches can therefore explain the coaches’ personal abilities from outside. So salary could be a factor when considering the ranking of coaches. Still, salary level of some coach is always determined by the coach’s directing performances, which include factors of tenure, wins and losses, winning rate and so on. That is to say, in the formal model, the influence caused by salary can be covered with factors considered.

<!-- b000484 | heading | pages [31] -->
7.4.2. Popularity of college

<!-- b000485 | prose | pages [31] -->
The popularity of the college the coach is in plays a role in social influence and reflection of audience, with varied degree of social concern. Hence, the investment of the college team and the environment players faced in the middle of a game may be affected. So the team’s performance is inevitably affected. As a result, the factors such as wins and losses, winning rate may have a difference. Still, the impact brought by popularity of college is overweighed compared with the 12 prior factors. So we consider it as a minor influence instead of paying too much attention.

<!-- b000486 | heading | pages [31] -->
7.4.3. Formal performance of the college team

<!-- b000487 | prose | pages [31] -->
Factors used to judge coaches are based on the coaches’ teams. In fact, the formal performance of a team takes a critical part in the team’s later performance, which, hereby, influences the coach’s data. Still, the impact brought by formal performance of the college team is overweighed compared with the 12 prior factors. So we consider it as a minor influence instead of paying too much attention.

<!-- b000488 | furniture | pages [32] -->
Team # 29696

<!-- b000489 | furniture | pages [32] -->
Page 30 of 42

<!-- b000490 | heading | pages [32] -->
8. Results and results analysis

<!-- b000491 | heading | pages [32] -->
8.1. Results

<!-- b000492 | caption | pages [32] -->
Table 17.

<!-- b000493 | prose | pages [32] -->
Basketball Coach Ranking Winning Ranking Name Tenure Wins Games Rate

<!-- b000494 | prose | pages [32] -->
1 29 644 806 0.8

<!-- b000495 | prose | pages [32] -->
John Wooden

<!-- b000496 | prose | pages [32] -->
2 27 862 995 0.866

<!-- b000497 | prose | pages [32] -->
Geno Auriemma

<!-- b000498 | prose | pages [32] -->
3 37 1098 1306 0.84

<!-- b000499 | prose | pages [32] -->
Pat Summitt

<!-- b000500 | prose | pages [32] -->
4 36 879 1133 0.78

<!-- b000501 | prose | pages [32, 33] -->
Dean Smith 5 39 975 1277 0.76

<!-- b000502 | furniture | pages [33] -->
Team # 29696

<!-- b000503 | furniture | pages [33] -->
Page 31 of 42

<!-- b000505 | prose | pages [33] -->
Mike Krzyzewski

<!-- b000506 | caption | pages [33] -->
Table 18.

<!-- b000507 | prose | pages [33] -->
Football Coach Ranking Winning Ranking Name Tenure Wins Games Rate

<!-- b000508 | prose | pages [33] -->
1 38 323 425 0.76

<!-- b000509 | prose | pages [33] -->
Bear Bryant

<!-- b000510 | prose | pages [33] -->
2 25 201 288 0.697917

<!-- b000511 | prose | pages [33] -->
Vince Dooley

<!-- b000512 | prose | pages [33] -->
3 46 409 548 0.74635

<!-- b000513 | prose | pages [33, 34] -->
Joe Paterno 4 33 249 388 0.641753

<!-- b000514 | furniture | pages [34] -->
Team # 29696

<!-- b000515 | furniture | pages [34] -->
Page 32 of 42

<!-- b000517 | prose | pages [34] -->
Lou Holtz

<!-- b000518 | prose | pages [34] -->
5 23 184 249 0.738956

<!-- b000519 | prose | pages [34] -->
Darrell Royal

<!-- b000520 | caption | pages [34] -->
Table 19.

<!-- b000521 | prose | pages [34] -->
Baseball Coach Ranking Winning Ranking Name Tenure Wins Games Rate

<!-- b000522 | prose | pages [34] -->
1 40 1442 1784 0.76

<!-- b000523 | prose | pages [34] -->
Don Schaly

<!-- b000524 | prose | pages [34] -->
2 30 1271 1718 0.70

<!-- b000525 | prose | pages [34, 35] -->
Ron Fraser 3 25 1133 1625 0.75

<!-- b000526 | furniture | pages [35] -->
Team # 29696

<!-- b000527 | furniture | pages [35] -->
Page 33 of 42

<!-- b000529 | prose | pages [35] -->
Ray Tanner

<!-- b000530 | prose | pages [35] -->
4 45 1404 1936 0.64

<!-- b000531 | prose | pages [35] -->
Bill Holowaty

<!-- b000532 | prose | pages [35] -->
5 34 1771 2386 0.74

<!-- b000533 | prose | pages [35] -->
Mike Martin Images come from Google Image Search

<!-- b000534 | heading | pages [35] -->
8.2. What the results illustrate

<!-- b000535 | prose | pages [35] -->
We draw a map of the United States based on the performance of the basketball regionally.

<!-- b000536 | caption | pages [35] -->
Fig.12 Map of U.S.A. [22]

<!-- b000537 | furniture | pages [36] -->
Team # 29696

<!-- b000538 | furniture | pages [36] -->
Page 34 of 42

<!-- b000539 | prose | pages [36] -->
Indeed, sports have an influence on every aspects of society and all walks of life.

<!-- b000540 | prose | pages [36] -->
Sports effect on society: Sports, with their impact and significance, have always been a critical role in society. As for players and coaches, sports bring competition, self-confidence integrity and ambition. As for audience, sports bring the sense of excitement, amusement and challenge. The most of all, however, is the spiritual power they bring us.

<!-- b000541 | prose | pages [36] -->
Sports effect on economy: The sports industry as a whole brings roughly $14.3 billion in earnings a year — and that’s s not even counting the Niagara of indirect economic activity generated by Super Bowl Sunday (well-known for being the second foodiest day in the country, behind Thanksgiving). The industry also contributes 456,000 jobs with an average salary of $39,000 per job”, quoted from American website “Find the best”. It is obviously that profits brought by sports are hard to be ignored. The basketball distribution difference hereby leads to a gap among states in American.

<!-- b000542 | prose | pages [36] -->
Sports effect on culture: Sports players are icons for some people today. Sports are also about pride and integrity. When people share a sports idol, they become a community, and when the number of those people grows, there would be an increase on sense of unity even patriotism.  Unity is never a downturn of progress of either economy or others, which is also illustrated in the map above.

<!-- b000543 | heading | pages [36] -->
9. Model Stability Analysis

<!-- b000544 | heading | pages [36] -->
9.1. Sensitivity analysis

<!-- b000545 | prose | pages [36] -->
In this paper, the basic model is established on the approach of cosine similarity. Then we optimized the model from the aspect of time line horizon and gender. The ranking list before and after the optimization is as follows (basketball as an example). It is illustrated in the result that the relatively better coaches ’ ranking hasn’t ch t changed tremendously. Obviously, the model is stable. The slight adjustment of the parameters change hasn’t t led to a dramatic change of the result. It is shown in the Table 20.

<!-- b000546 | caption | pages [36] -->
Table 20.

<!-- b000547 | prose | pages [36, 37] -->
Ranking list before and after the optimization Ranking before Ranking before adjustment adjustment John Wooden John Wooden Geno Auriemma Geno Auriemma Pat Summitt Pat Summitt Dean Smith Dean Smith Mike Krzyzewski Mike Krzyzewski Roy Williams Roy Williams Adolph Rupp John Calipari John Calipari Bill Self Tara VanDerveer Adolph Rupp Tom Izzo John Thompson

<!-- b000548 | furniture | pages [37] -->
Team # 29696

<!-- b000549 | furniture | pages [37] -->
Page 35 of 42

<!-- b000551 | heading | pages [37] -->
9.2. Robustness analysis

<!-- b000552 | prose | pages [37] -->
Robustness testing is a quality assurance methodology focused on testing the robustness of software and mathematical model. Robustness testing has also been used to describe the process of verifying the correctness of the system.

<!-- b000553 | prose | pages [37] -->
By adding input noise to the first 15 coaches’ factors, we obtain the changed data of the first 15 coaches. The data comparison of a coach is shown in Table 21.

<!-- b000554 | caption | pages [37] -->
Table 21.

<!-- b000555 | prose | pages [37] -->
Data comparison of John Wooden

<!-- b000556 | prose | pages [37] -->
T NC T W L G W R T NFF NCC CC G A 29 16 759 162 921 0.8241 2 12 10 16 5752963 12 29 16 755 162 917 0.8231 2 12 10 16 5743239 11

<!-- b000557 | prose | pages [37] -->
1.2 Original Data Data added with noise 1

<!-- b000558 | prose | pages [37] -->
Standardized Score of Factors 0.8

<!-- b000559 | prose | pages [37] -->
0.6

<!-- b000560 | prose | pages [37] -->
0.4

<!-- b000561 | prose | pages [37] -->
0.2

<!-- b000562 | prose | pages [37] -->
0 0 2 4 6 8 10 12 12 Different Factors

<!-- b000563 | caption | pages [37] -->
Fig. 13 Data Comparison of John Wooden before and after noise input

<!-- b000564 | prose | pages [37] -->
The new ranking is shown in Table 22.

<!-- b000565 | caption | pages [37] -->
Table 22.

<!-- b000566 | prose | pages [37, 38] -->
Comparison of adding noise Ranking list after noise input Ranking list before noise input John Wooden John Wooden Geno Auriemma Geno Auriemma Pat Summitt Pat Summitt Dean Smith Dean Smith John Calipari Mike Krzyzewski Rick Pitino Roy Williams Roy Williams John Calipari Tom Izzo Bill Self John Thompson Adolph Rupp Billy Donovan Tom Izzo

<!-- b000567 | furniture | pages [38] -->
Team # 29696

<!-- b000568 | furniture | pages [38] -->
Page 36 of 42

<!-- b000570 | prose | pages [38] -->
Analyzing the ranking list of coaches after adding input noise, we find that the ranking of the first 5 coaches hasn’t t changed. It proves that the robustness of our model is relatively well. The noise influence is little.

<!-- b000571 | heading | pages [38] -->
9.3. Strengths and Weaknesses

<!-- b000572 | heading | pages [38] -->
9.3.1. Strengths

<!-- b000573 | prose | pages [38] -->
Objectively analyzed, the core strengths of our model are,  Credibility: Coaches ranking result in this model is convincing compared to college coaches evaluation from famous advisers and media.

<!-- b000574 | prose | pages [38] -->
 Accessibility: Our model can be applied to genders, varied time line horizons and different countries.

<!-- b000575 | heading | pages [38] -->
 Self-improvement: The approaches of optimization in our model simplify the

<!-- b000576 | prose | pages [38] -->
overall ranking system and push it further to other data sources in different countries among sports.

<!-- b000577 | prose | pages [38] -->
 Reliability: Our model is based on a large amount of data. The stability and robustness of our model are guaranteed. The accuracy and sensitivity is also presented in the results analysis section.

<!-- b000578 | prose | pages [38] -->
 Adaptability: The basic idea of our model can be applied to other ranking systems due to its scientific approach and easy-handled model.

<!-- b000579 | heading | pages [38] -->
9.3.2. Weaknesses

<!-- b000580 | prose | pages [38] -->
With merits above, there is still limitation in our model.

<!-- b000581 | prose | pages [38] -->
 The model can be less flexible when the evaluation factors are narrowed down to one or two. So it can be less reliable when ranking coaches on s specific factor.

<!-- b000582 | prose | pages [38] -->
 The model can be inaccurate referring to coaches whose ability is less impressing.

<!-- b000583 | furniture | pages [39] -->
Team # 29696

<!-- b000584 | furniture | pages [39] -->
Page 37 of 42

<!-- b000585 | heading | pages [39] -->
10. Conclusions

<!-- b000586 | prose | pages [39] -->
 The approach of cosine similarity is used for optimization in aspects of time line horizon and gender. We obtained a best coaches ranking list in basketball as an example. The best coach of basketball will be John Wooden. The model was then applied to other sports. We ranked the coaches of baseball, softball and football.

<!-- b000587 | prose | pages [39] -->
 The factor of time line horizon makes an important impact. So we analyzed the factors contributing to the difficulty gap, which is the number of active coaches in NCAA. We supposed that the difficulty in coaching is positively linear with it. The difficulty in coaching is also positively linear with time line horizon.

<!-- b000588 | prose | pages [39] -->
 The factor of gender contributes to the pressure difference across genders.

<!-- b000589 | prose | pages [39] -->
Therefore, there are significant differences in factors between male and female coaches. It is also proven by the analysis of variance. In order to fix the problem, we apply the approach of data whitening to modify the data with a significant difference. After the elimination of the difference, we rank the coaches again.

<!-- b000590 | prose | pages [39] -->
 We applied the ranking model further to other sports. To achieve this purpose, we established a factors pool. When considering one specific sport, we picked factors in the factors pool and then applied the same model to rank the coaches.

<!-- b000591 | prose | pages [39] -->
 At the end, we changed several parameters and add some input noise. The final result is consistent with the formal one. Therefore, the stability and robustness is considerably well.

<!-- b000592 | heading | pages [39] -->
11. Reference

<!-- b000593 | references | pages [39] -->
[1] http://www.usatoday.com/sports/college/salaries/

<!-- b000594 | references | pages [39] -->
[2]2012: NCAA Men's Basketball Tournament Records of Active

<!-- b000595 | references | pages [39] -->
Coacheshttp://www.dbwoerner.com/basketball/coaches/coach112.html

<!-- b000596 | references | pages [39] -->
[3] http://www.masseyratings.com/theory/massey97.pdf

<!-- b000597 | references | pages [39] -->
[4]10 Greatest Coaches in NCAA Basketball History

<!-- b000598 | references | pages [39] -->
http://bleacherreport.com/articles/1341064-10-greatest-coaches-in-ncaa-basketball-his

<!-- b000599 | references | pages [39] -->
tory

<!-- b000600 | references | pages [39] -->
[5] Sports-Reference.com - Sports Statistics and History

<!-- b000601 | references | pages [39] -->
http://www.sports-reference.com/

<!-- b000602 | references | pages [39] -->
[6]Cosine similarity - Wikipedia, the free encyclopedia

<!-- b000603 | references | pages [39] -->
http://en.wikipedia.org/wiki/Cosine_similarity

<!-- b000604 | references | pages [39] -->
[7]Division I (NCAA) - Wikipedia, the free encyclopedia

<!-- b000605 | references | pages [39] -->
http://en.wikipedia.org/wiki/Division_I_(NCAA)

<!-- b000606 | references | pages [39] -->
[8] Adjusted Cosine Similarity  http://www10.org/cdrom/papers/519/node14.html

<!-- b000607 | furniture | pages [40] -->
Team # 29696

<!-- b000608 | furniture | pages [40] -->
Page 38 of 42

<!-- b000609 | references | pages [40] -->
[9] Recommender Systems > PART I: Introduction to basic concepts > 4.3.1 Defaults -

<!-- b000610 | references | pages [40] -->
Pg. 89e

<!-- b000611 | references | pages [40] -->
http://my.safaribooksonline.com/book/-/9780521493369/2dot2-item-based-nearest-nei

<!-- b000612 | references | pages [40] -->
ghbor-recommendation/221_the_cosine_similarity_meas#X2ludGVybmFsX0J2ZGV

<!-- b000613 | references | pages [40] -->
wRmxhc2hSZWFkZXI/eG1saWQ9OTc4MDUyMTQ5MzM2OS84OQ

<!-- b000614 | references | pages [40] -->
[10] Xin J. and Bamshad M. School of Computer Science, Telecommunication and

<!-- b000615 | references | pages [40] -->
Information Systems DePaul University USING SEMANTIC SIMILARITY TO

<!-- b000616 | references | pages [40] -->
ENHANCE ITEM-BASED COLLABORATIVE FILTERING

<!-- b000617 | references | pages [40] -->
www.csee.umbc.edu/~kolari1/Mining/papers/JM03.pdf

<!-- b000618 | references | pages [40] -->
[11] http://www.sports.yahoo.com/news/ncca-college-basketball/

<!-- b000619 | references | pages [40] -->
[12]http://www.articles.sun-sentinel.com/sports/

<!-- b000620 | references | pages [40] -->
[13]http://www.Find the best.com/

<!-- b000621 | references | pages [40] -->
[14]http://www.wiseGEEK.com/how-are-college-football-teams-ranked.htm/

<!-- b000622 | references | pages [40] -->
[15]http://www.economicmodeling.com/sports/

<!-- b000623 | references | pages [40] -->
[16] Matrix-based Methods  for College  Football Rankings Vladimir Boginski1,

<!-- b000624 | references | pages [40] -->
Sergiy Butenko and Panos M. Pardalos1 University of Florida, USA  Texas A&M

<!-- b000625 | references | pages [40] -->
University, USA

<!-- b000626 | references | pages [40] -->
[17] College Football Rankings: Do the Computers Know Best? By Joseph Martinich

<!-- b000627 | references | pages [40] -->
College of Business Administration University of Missouri - St. Louis Final Version:

<!-- b000628 | references | pages [40] -->
May 7, 2002

<!-- b000629 | references | pages [40] -->
[18] An overview of some methods for ranking sports teams Soren P. Sorensen

<!-- b000630 | references | pages [40] -->
University of Tennessee Knoxville

<!-- b000631 | references | pages [40] -->
[19] http://college-basketball-coaches.findthebest.com/

<!-- b000632 | references | pages [40] -->
[20]http://bbs.hupu.com/91418.html

<!-- b000633 | references | pages [40] -->
[21]http://www.slate.com/articles/sports/slate_labs/2013/10/united_sports_of_america

<!-- b000634 | references | pages [40] -->
_map_if_each_state_could_have_only_one_sport_what.html

<!-- b000635 | references | pages [40] -->
[22] http://en.wikipedia.org/wiki/Cluster_analysis

<!-- b000636 | references | pages [40] -->
[23]Dingyu Xue 2009 Solving Applied Mathematical Problems with MATLAB Bejing:

<!-- b000637 | references | pages [40] -->
Tsinghua

<!-- b000638 | furniture | pages [41] -->
Team # 29696

<!-- b000639 | furniture | pages [41] -->
Page 39 of 42

<!-- b000640 | heading | pages [41] -->
12. Appendix

<!-- b000641 | prose | pages [41] -->
Original Data

<!-- b000642 | prose | pages [41, 42] -->
Name. G Exp NExp W L G WR T John Wooden M 29 16 644 162 806 0.8 2 Geno Auriemma F(M) 27 27 862 133 995 0.866 1 Pat Summitt F 37 31 1098 208 1306 0.84 1 Dean Smith M 36 27 879 254 1133 0.78 1 Mike Krzyzewski M 39 29 975 302 1277 0.76 2 Roy Williams M 26 23 715 187 902 0.79 2 John Calipari M 22 14 585 171 756 0.77 3 Bill Self M 21 15 524 169 693 0.76 4 Adolph Rupp M 41 20 876 190 1066 0.82 1 John Thompson M 27 20 596 239 835 0.71 1 Billy Donovan M 20 13 470 188 658 0.71 2 Tom Izzo M 19 16 458 181 639 0.72 1 Tara VanDerveer F 36 33 891 203 1094 0.81 3 Denny Crum M 30 23 675 295 970 0.7 1 Bob Knight M 42 28 899 374 1273 0.71 3 Rick Pitino M 28 18 681 239 920 0.74 4 Lon Kruger M 28 14 531 338 869 0.611 5 Jim Calhoun M 40 23 877 382 1259 0.7 2 Jerry Tarkanian M 30 18 761 202 963 0.79 3 Lute Olson M 34 28 776 285 1061 0.73 3 Jim Boeheim M 38 30 942 314 1256 0.75 1 Jack Gardner M 28 8 486 235 721 0.67 2 Kimberly Mulkey F 14 14 376 81 457 0.85 1 Gene Keady M 27 18 550 289 839 0.66 2 Thad Matta M 14 11 370 109 479 0.77 3 Anthony Grant M 8 3 171 90 261 0.66 2 Hank Iba M 40 8 752 333 1085 0.69 3 Sean Miller M 10 6 237 91 328 0.72 2 Mike Montgomery M 32 16 670 312 982 0.68 3 Jay Wright M 20 10 399 231 630 0.63 2 Tonya Cardoza F 20 20 107 57 164 0.65 2 Joanne McCallie F 21 19 457 180 637 0.73 3 Bo Ryan M 15 12 339 145 484 0.7 2 Sherri Coale F 17 14 381 179 560 0.68 1 Eddie Sutton M 37 26 806 329 1135 0.71 5 Jim Valvano M 18 9 337 200 537 0.63 3 Jamie Dixon M 11 9 281 90 371 0.757 1 Muffet McGraw F 31 23 714 258 972 0.73 5 Lisa Stockton F 26 20 464 221 685 0.56 2 Brenda Fres F 14 12 335 123 458 0.7 3 Charlaine Vivian F 43 32 901 332 1233 0.73 3 Deb Patterson F 17 17 339 207 546 0.62 1 Tina Martin F 18 17 341 181 522 0.65 2 June Daugherty F 24 20 369 335 704 0.52 3 JenniferRizzotti F 14 8 276 146 422 0.45 1 Suzy Merchant F 18 17 341 172 513 0.66 3 Lisa Bluder F 29 19 617 297 914 0.69 4 Sue Semrau F 18 13 309 203 512 0.6 1 Sharon Versyp F 14 10 283 144 427 0.66 3 MaChelle Joseph F 11 7 204 126 330 0.44 1 Nikki Caldwell F 6 5 133 52 185 0.72 2 Pam Borton F 10 10 283 185 468 0.45 2 Joanne Boyle F 11 9 244 118 362 0.51 3 Melissa McFerrin F 6 1 155 147 302 0.51 2 Connie Yori F 21 12 410 275 685 0.47 4 Kellie Harper F 10 10 171 135 306 0.52 3 Beth Couture F 25 20 436 275 711 0.44 4 Regina Miller F 22 19 235 226 461 0.51 4 Kim Barnes Arico F 10 8 292 216 508 0.42 2 Jamelle Elliott F 5 3 72 49 121 0.41 1

<!-- b000643 | furniture | pages [42] -->
Team # 29696

<!-- b000644 | furniture | pages [42] -->
Page 40 of 42

<!-- b000646 | prose | pages [42] -->
Modified Data

<!-- b000647 | prose | pages [42, 43, 44] -->
Name. G Exp NExp W L G WR T John Wooden M 29 16 755 162 917 0.823337 2 Geno Auriemma F(M) 27 27 1204 133 1337 0.9005236 1 Pat Summitt F 37 31 1512 208 1720 0.8790698 1 Dean Smith M 36 27 1300 254 1554 0.8365508 1 Mike Krzyzewski M 39 29 1462 302 1764 0.8287982 2 Roy Williams M 26 23 1072 187 1259 0.8514694 2 Adolph Rupp M 41 20 897 190 1087 0.825207 1 John Calipari M 22 14 877 171 1048 0.8368321 3 Tara VanDerveer F 36 33 1241 203 1444 0.8594183 3 Tom Izzo M 19 16 687 181 868 0.7914747 1 Billy Donovan M 20 13 705 188 893 0.7894737 2 John Thompson M 27 20 894 239 1133 0.7890556 1 Bill Self M 21 15 786 169 955 0.8230366 4 Denny Crum M 30 23 1012 295 1307 0.7742923 1 Rick Pitino M 28 18 1021 239 1260 0.8103175 4 Bob Knight M 42 28 1348 374 1722 0.7828107 3 Jerry Tarkanian M 30 18 1141 202 1343 0.8495905 3 Jim Calhoun M 40 23 1315 382 1697 0.7748969 2 Lute Olson M 34 28 1164 285 1449 0.8033126 3 Jim Boeheim M 38 30 1413 314 1727 0.8181818 1 Kimberly Duane 14 14 569 81 650 0.8753846 1 Mulkey F Jack Gardner M 28 8 542 235 777 0.6975547 2 Thad Matta M 14 11 555 109 664 0.8358434 3 Gene Keady M 27 18 825 289 1114 0.7405745 2 Anthony Grant M 8 3 256 90 346 0.7398844 2 Mike Montgomery M 32 16 1005 312 1317 0.7630979 3 Sean Miller M 10 6 355 91 446 0.7959641 2 Tonya Cardoza F 20 20 217 57 274 0.7919708 2 Jay Wright M 20 10 598 231 829 0.721351 2 Bo Ryan M 15 12 508 145 653 0.7779479 2 Joanne P. McCallie F 21 19 674 180 854 0.7892272 3 Hank Iba M 40 8 752 333 1085 0.6930876 3 Sherri Coale F 17 14 575 179 754 0.7625995 1 Eddie Sutton M 37 26 1209 329 1538 0.7860858 5 Lisa Stockton F 26 20 684 221 905 0.7558011 2 Jamie Dixon M 11 9 421 90 511 0.8238748 1 Jennifer Rizzotti F 14 8 438 146 584 0.75 1 Muffet McGraw F 31 23 1010 258 1268 0.79653 5 Jim Valvano M 18 9 505 200 705 0.7163121 3 Brenda Fres F 14 12 515 123 638 0.80721 3 MaChelle Joseph F 11 7 344 126 470 0.7319149 1 Charlaine Vivian 43 32 1254 332 1586 0.7906683 3 Stringer F Tina Martin F 18 17 523 181 704 0.7428977 2 Deb Patterson F 17 17 520 207 727 0.7152682 1 Pam Borton F 10 10 447 185 632 0.7072785 2 Suzy Merchant F 18 17 523 172 695 0.752518 3 Sharon Versyp F 14 10 447 144 591 0.7563452 3 Lisa Bluder F 29 19 883 297 1180 0.7483051 4 Sue Semrau F 18 13 481 203 684 0.7032164 1 Joanne Boyle F 11 9 396 118 514 0.770428 3 June Daugherty F 24 20 559 335 894 0.6252796 3 Kim Barnes Arico F 10 8 459 216 675 0.68 2 Connie Yori F 21 12 613 275 888 0.6903153 4 Nikki Caldwell F 6 5 251 52 303 0.8283828 2 Beth Couture F 25 20 647 275 922 0.7017354 4 Kellie Harper F 10 10 300 135 435 0.6896552 3 Lon Kruger M 30 14 531 338 869 0.611 5 Melissa McFerrin F 6 1 279 147 426 0.6549296 2 Jamelle Renee F 5 3 171 49 220 0.7772727 1 Elliott Regina Miller F 22 19 384 226 610 0.6295082 4

<!-- b000648 | furniture | pages [43] -->
Team # 29696

<!-- b000649 | furniture | pages [43] -->
Page 41 of 42

<!-- b000651 | furniture | pages [44] -->
Team # 29696

<!-- b000652 | furniture | pages [44] -->
Page 42 of 42
