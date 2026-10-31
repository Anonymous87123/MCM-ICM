# P-B-2014-26636-060c74b1

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Team Control Number

<!-- b000002 | front_matter | pages [1] -->
For office use only For office use only

<!-- b000003 | front_matter | pages [1] -->
26636

<!-- b000004 | front_matter | pages [1] -->
T1 ________________ F1 ________________ T2 ________________ F2 ________________ T3 ________________ F3 ________________ Problem Chosen T4 ________________ F4 ________________ B

<!-- b000005 | title | pages [1] -->
An evaluation model of college coaches

<!-- b000006 | heading | pages [1] -->
Summary

<!-- b000007 | prose | pages [1] -->
In working out a evaluation system that would fairly judge the best all-time college coaches, our team decided to apply the grey correlation analysis model. To figure out parameters in this model, we firstly refer to some expertise and then select four indi- cators that would be applied in general across both genders and all possible sports –NCAA Champions, Pct, wins, and Coach Awards. We use fuzzy consistent matrix to grant each kind of indicator a proper weight in our evaluation system. Then we use specific statistics in basketball, football and ice hockey and give out the ranks of the coaches. To further examine our model, we compare the top 5 coaches in our lists with those in the reports from ESPN or other research institutes.

<!-- b000008 | prose | pages [1] -->
We also find out that the competition system of different events of NCAA will inevi- tably change over time, and that the time line horizon we choose will result in differ- ences in our four factors. The real data prove our supposition – in both of the basket- ball and the football fields, the “ancient” coaches enjoy a significantly higher average of winning percentage than the present coaches, while the other three factors show no discrimination. To enhance the accuracy of the model, we modify our original model with a correction factor that derives from the moving weighted average method to ad- just the winning percentage over time, which is the shining point of our theory. In ad- dition, we find out the significant difference among coaches before 1950s and those in later periods, which is also taken into consideration in the adjustment of our model. In terms of gender, we reach the conclusion that it has no influence on our selection of factors and the metric of our assessment.

<!-- b000009 | prose | pages [1] -->
We test our model by examining its stability and sensitivity. In stability test, we change the priority of the four factors to judge if the model is still applicable. Fur- thermore, since fuzzy consistent matrix has inborn disadvantage in subjectivity, Shannon’s entropy method is applied to substantiate the stability. In addition, we im-

<!-- b000010 | prose | pages [1] -->
plement sensitivity test by changing the in the grey correlation analysis model.

<!-- b000011 | prose | pages [1] -->
In the last part of this report, we state the strengths and weaknesses of our model. Convenience and universality are the greatest advantage of our model, while the sub- jectivity in selecting indicators may still exist.

<!-- b000012 | heading | pages [2] -->
Contents

<!-- b000013 | contents | pages [2] -->
1 Introduction ............................................................... 2

<!-- b000014 | contents | pages [2] -->
1.1 Background ....................................................................................................... 2

<!-- b000015 | contents | pages [2] -->
1.2 Our Work ........................................................................................................... 2

<!-- b000016 | contents | pages [2] -->
2 Model .......................................................................... 3

<!-- b000017 | contents | pages [2] -->
2.1 Introduction ....................................................................................................... 3

<!-- b000018 | contents | pages [2] -->
2.2 Notation and definitions .................................................................................... 4

<!-- b000019 | contents | pages [2] -->
2.3 Model designing................................................................................................ 5

<!-- b000020 | contents | pages [2] -->
3 Application ................................................................. 7

<!-- b000021 | contents | pages [2] -->
3.1 Introduction ....................................................................................................... 7

<!-- b000022 | contents | pages [2] -->
3.2 The selection of factors ..................................................................................... 7

<!-- b000023 | contents | pages [2] -->
3.3 Data collection .................................................................................................. 8

<!-- b000024 | contents | pages [2] -->
3.4 Calculation ........................................................................................................ 8

<!-- b000025 | contents | pages [2] -->
3.5 Application of our model to other sports ........................................................ 13

<!-- b000026 | contents | pages [2] -->
4 Comparison of the ranks from different sources... 15

<!-- b000027 | contents | pages [2] -->
5 The analysis of time line horizon ............................ 16

<!-- b000028 | contents | pages [2] -->
5.1 Introduction ..................................................................................................... 16

<!-- b000029 | contents | pages [2] -->
5.2 Procedures ....................................................................................................... 16

<!-- b000030 | contents | pages [2] -->
6 The analysis of gender ............................................. 20

<!-- b000031 | contents | pages [2] -->
7 Stability test .............................................................. 21

<!-- b000032 | contents | pages [2] -->
7.1 Testing the influence of changing the method on the determination of weights .

<!-- b000033 | contents | pages [2] -->
…………………………………………………………………………………...21

<!-- b000034 | contents | pages [2] -->
7.2 Testing the influence of changing the comparative importance among the four

<!-- b000035 | contents | pages [2] -->
factors .................................................................................................................... 24

<!-- b000036 | contents | pages [2] -->
8 Sensitivity test .......................................................... 26

<!-- b000037 | contents | pages [2] -->
9 Strengths and Weaknesses ....................................... 27

<!-- b000038 | contents | pages [2] -->
9.1 Strengths ......................................................................................................... 27

<!-- b000039 | contents | pages [2] -->
9.2 Weaknesses ..................................................................................................... 28

<!-- b000040 | contents | pages [2] -->
Reference ..................................................................... 28

<!-- b000041 | contents | pages [2] -->
Appendix ..................................................................... 29

<!-- b000042 | contents | pages [2] -->
An article for Sports Illustrated ................................ 36

<!-- b000043 | furniture | pages [3] -->
Team #26636

<!-- b000044 | furniture | pages [3] -->
Page 2 of 38

<!-- b000045 | heading | pages [3] -->
1 Introduction

<!-- b000046 | heading | pages [3] -->
1.1 Background

<!-- b000047 | prose | pages [3] -->
College sports teams occupy a pivotal position in the sporting world. The major col- lege sports events, such as National Collegiate Athletic Association (NCAA) champi- onships, have long been the focus of attention of the public. Each year, not only the top sports teams but also the head coaches grab the eye of a considerable number of people. To promote the development of college sports, people are increasingly apt to seek for the help of modern science and technology to evaluate the performance of college coaches.

<!-- b000048 | prose | pages [3] -->
Designing an objective and effective system to evaluate the performance of college coaches has many advantages. Such system will enable either college sports teams or mess media to analyze the strengths and weaknesses of a specific coach, as well as to reveal the keys of victory of those legendary coaches. Current approaches of evalua- tion, however, are neither quantitative nor broadly applicable. Most of studies use subjective and qualitative methods for assessment. The methods they use for collecting data include: Designing questionnaires for athletes to judge their coaches (Rushall, B. S.,et, al.,1985), interviewing coaches (Cassidy.,et,al.,2006), observation (Nelson, Lee J.,et,al., 2006), etc. Using the above methods, the evaluation of coaches simply relies on human judgment, which is not optimal since numerous data are accessible on the Internet.

<!-- b000049 | heading | pages [3] -->
1.2 Our work

<!-- b000050 | prose | pages [3] -->
As modelers, we are required to build a mathematical model for Sports Illustrator to select the best college coach or coaches (male or female, past or present) in various kinds of sports. In addition, we are required to discuss the influence of time line hori- zon and gender on our model.

<!-- b000051 | prose | pages [3] -->
Instead of using subjective evaluation method, we adopt a quantitative method to measure and rank the performance of college coaches.

<!-- b000052 | prose | pages [3, 4] -->
 Firstly, we determine the elements of our evaluation system. In order to make our model applicable in various kinds of sports and both genders, we select wins (the number of times that one specific coach has successfully led a team to win), win- ning percentage, the number of times that they had led their teams to win national championships, and the number of times that they have won the title of Coach of the Year as evaluation factors.  Secondly, we create a fuzzy consistent matrix to determine the weight of each factor. This approach includes processes of determining fuzzy preferential rela- tion matrix and fuzzy consistent matrix, as well as the introduction of root meth- od. We will further explain the above processes in the next section.  Thirdly, we develop a grey correlation analysis model to evaluate and rank the performance of college coaches. This model includes the calculation of grey rela- tional coefficient and grey rational degree, which will be displayed in the next section.

<!-- b000053 | furniture | pages [4] -->
Team #26636

<!-- b000054 | furniture | pages [4] -->
Page 3 of 38

<!-- b000056 | heading | pages [4] -->
2 Model

<!-- b000057 | heading | pages [4] -->
2.1 Introduction

<!-- b000058 | prose | pages [4] -->
The evaluation model we adopt is based on the principle of grey correlation analysis. Using this approach, we can calculate the grey relational degree between the coaches on our lists and the ideal coaches (the fictitious coaches with ideal data). Then we sort the grey relational degrees by descending order to get the rank of the coaches. Note that the prerequisite of our model is the determination of the weights of all factors. This prerequisite can be met by establishing a fuzzy consistent matrix.

<!-- b000059 | prose | pages [4] -->
Therefore, our evaluation system can be divided into two parts:

<!-- b000060 | prose | pages [4] -->
The first part is the determination of the weight of each factor, which is critical in our model and will exert vital influence on our conclusion. Theoretically speaking, both subjective methods and objective methods can be applied to the determination of weights. Subjective methods are mainly based on human judgment. Such methods depend on the experience of experts. Currently prevailing subjective methods include: The Delphi method (Hwang, C.L.; et, al., 1987), analytic hierarchy process (Saaty, T.L., 1980), the weighted least square method (Chu, A.T.W.; et, al., 1979). Objective methods involve the use of quantitative models. Based on the data collected from da- tabases or websites, researchers can use mathematical models to determine the weights of factors that mostly reflect the performance of the objects they study. Cur- rently prevailing objective methods include: Entropy method (Shannon, C.E., 1948), principle component analytical method (Fan, Z.P., 1996), etc. Therefore, considering the features of NCAA competitions and the interrelationship among factors, we de- termine the weights of factors by creating fuzzy consistent matrix.

<!-- b000061 | prose | pages [4] -->
The second part of our evaluation system is the grey relational analysis model. We use this model to evaluate and rank coaches. Because of the scarcity of data sources and the complexity of interrelationship among factors, it is difficult for modelers to ac- quire enough information. Therefore, it is comparatively advantageous to use grey relational analysis to analyze such a small-sample data system. This system can elim- inate the subjectivity to some degree and will thusly lead to an objective conclusion.

<!-- b000062 | furniture | pages [5] -->
Team #26636

<!-- b000063 | heading | pages [5] -->
2.2 Notations and definitions

<!-- b000064 | heading | pages [5] -->
2.2.1 Notations

<!-- b000065 | heading | pages [5] -->
Notations

<!-- b000066 | prose | pages [5] -->
F A w k

<!-- b000067 | prose | pages [5] -->
x k 0( )

<!-- b000068 | prose | pages [5] -->
ix k ( )

<!-- b000069 | prose | pages [5] -->
 i k ( )

<!-- b000070 | prose | pages [5] -->
 E ir R

<!-- b000071 | heading | pages [5] -->
2.2.2 Definitions

<!-- b000072 | prose | pages [5] -->
Fuzzy consistent matrix

<!-- b000073 | prose | pages [5] -->
  1) For fuzzy matrix , if F ( f ) f ij m m ij 

<!-- b000074 | furniture | pages [5] -->
Page 4 of 38

<!-- b000075 | prose | pages [5] -->
Explanations Fuzzy consistent matrix Fuzzy preferential relation matrix Weights of factors The kth factor Standard data array (The best value of factor k among all coaches) Correlation data array (The raw data ar- ray of factor k among all coaches)

<!-- b000076 | prose | pages [5] -->
Grey relational coefficient

<!-- b000077 | prose | pages [5] -->
Distinguishing coefficient Evaluation matrix Grey correlational degree Grey comprehensive evaluation matrix

<!-- b000078 | prose | pages [5] -->
, then this matrix is defined as fuzzy f 1 ji

<!-- b000079 | prose | pages [5] -->
   reciprocal matrix. For any k (k =1,2,…m), if

<!-- b000080 | prose | pages [5] -->
defined as fuzzy consistent matrix.

<!-- b000081 | prose | pages [5] -->
 2) For fuzzy consistent matrix F (

<!-- b000082 | prose | pages [5] -->
 element j are equally important. If 0 ijf , then matrix F is f f f 0 5. ij ik jk

<!-- b000083 | prose | pages [5] -->
ijf  , if , then element i and f ) 0 5. ij m m 

<!-- b000084 | prose | pages [5] -->
 , then element j is more important than 0 5.

<!-- b000085 | prose | pages [5] -->
is, the more important element j is than element i . If element i . The smaller ijf

<!-- b000086 | prose | pages [5] -->
, then element i is more important than element j . The greater  0 5 . ijf 1

<!-- b000087 | prose | pages [5] -->
important element i is than element j .

<!-- b000088 | prose | pages [5] -->
Fuzzy preferential relation matrix ijf is, the more

<!-- b000089 | prose | pages [5] -->
We use three numbers (0, 0.5, and 1) to measure the comparative importance among

<!-- b000090 | prose | pages [5, 6] -->
 A ( a ) the factors. For fuzzy matrix ij m m  a  0 5. , if , then element i and element j are ij a  equally important to the upper level. If , then element j is more important to the 0 ij

<!-- b000091 | furniture | pages [6] -->
Team #26636

<!-- b000092 | furniture | pages [6] -->
Page 5 of 38

<!-- b000094 | prose | pages [6] -->
a , then element i is more important to the upper lev- upper level than element i . If 1 ij

<!-- b000095 | prose | pages [6] -->
el than element j .

<!-- b000096 | prose | pages [6] -->
For example, suppose that we have four factors: a ,b ,c , andd . If the degree of im- portance to the upper level degrades from a tod , then we create the fuzzy preferential relation matrix A as follows:

<!-- b000097 | prose | pages [6] -->
  0 5 . 1 1 1   0 0 5 . 1 1    A  0 0 0 5 . 1   0 0 0 0 5 .  

<!-- b000098 | heading | pages [6] -->
2.3 Model Designing

<!-- b000099 | prose | pages [6] -->
Process I: How to determine the weight of each factor

<!-- b000100 | heading | pages [6] -->
1) We create the fuzzy preferential relation matrix A .

<!-- b000101 | prose | pages [6] -->
2) We convert the fuzzy preferential relation matrix into a fuzzy consistent matrix:

<!-- b000102 | prose | pages [6] -->
Sum column vectors of each row in the fuzzy preferential matrix:

<!-- b000103 | prose | pages [6] -->
m    f a , i 1 2 , ,..., m i ik  k 1

<!-- b000104 | prose | pages [6] -->
Apply the following conversion:

<!-- b000105 | prose | pages [6] -->
 f f i j   f 0 5 . ij 2 m  Thus the fuzzy consistent matrix F ( f ) is created. ij m m 

<!-- b000106 | prose | pages [6] -->
3) We use the root method to determine the weights of each factor. The procedures of the root method are displayed as follows.

<!-- b000107 | prose | pages [6] -->
Normalize each column of matrix F :

<!-- b000108 | prose | pages [6] -->
f ij  w ij n  f ij  i 1

<!-- b000109 | prose | pages [6, 7] -->
w by row and extract the nth root: Multiply column vectors of ij n  1 n / w ( w ) i ij  i 1

<!-- b000110 | furniture | pages [7] -->
Team #26636

<!-- b000111 | furniture | pages [7] -->
Page 6 of 38

<!-- b000113 | prose | pages [7] -->
Normalize w : i

<!-- b000114 | prose | pages [7] -->
w i  w i n  w i  i 1

<!-- b000115 | prose | pages [7] -->
Therefore, the approximate feature vector is:

<!-- b000116 | prose | pages [7] -->
 T w ( w w , ,..., w n) 1 2

<!-- b000117 | prose | pages [7] -->
Process II: Using grey correlation analysis to rank coaches

<!-- b000118 | prose | pages [7] -->
1) We determine the factors used for evaluation and collect the data of college coaches. Assume that the number of coaches on the list is m , and the number of factors used

<!-- b000119 | prose | pages [7] -->
is n. The standard data array x k is the best values of factor k among all coaches. 0( )

<!-- b000120 | prose | pages [7] -->
The correlation data array ix k is a raw data array of factor k among coaches on the ( )

<!-- b000121 | prose | pages [7] -->
list.

<!-- b000122 | prose | pages [7] -->
Therefore, for each factor k , the standard data array is:

<!-- b000123 | prose | pages [7] -->
  x { x k ( )| k 1 2 , ,..., } n 0 0

<!-- b000124 | prose | pages [7] -->
And the correlation data array is:

<!-- b000125 | prose | pages [7] -->
  x { x k ( )| k 1 2 , ,..., m } i i

<!-- b000126 | prose | pages [7] -->
Then we normalize the standard data array and the correlation data array by scaling between 0 and 1.

<!-- b000127 | prose | pages [7] -->
Next, we calculate the grey relational coefficient as follows:

<!-- b000128 | prose | pages [7] -->
    minmin x ( k ) x k ( ) maxmax x ( k ) x k ( ) 0 i 0 i   i k i k ( k ) i     x ( k ) x k ( ) maxmax x ( k ) x k ( ) 0 i 0 i i k

<!-- b000129 | prose | pages [7] -->
 Where i k ( ) is the grey relational coefficient that measures the relationship between

<!-- b000130 | prose | pages [7] -->
the standard data array x k and the correlation data array ix k , when the k th factor 0( ) ( )

<!-- b000131 | prose | pages [7] -->
is the object of study. And is named as distinguishing coefficient, the values of

<!-- b000132 | prose | pages [7] -->
which range from 0 to 1. The greater is, the greater the distinguishing rate will be,

<!-- b000133 | prose | pages [7, 8] -->
 and vice versa. In our model, we choose 0.5 as the value of . Using i k ( ) , we can   get the evaluation matrix . E ( ( k ))  i n m

<!-- b000134 | furniture | pages [8] -->
Team #26636

<!-- b000135 | furniture | pages [8] -->
Page 7 of 38

<!-- b000137 | prose | pages [8] -->
2) Then we calculate the grey relational degree as follows:

<!-- b000138 | prose | pages [8] -->
n   r w ( k ) i i i  k 1

<!-- b000139 | prose | pages [8] -->
Where ir is the grey relational degree of the standard data array to the correlation data array.

<!-- b000140 | prose | pages [8] -->
ir and w , we get the grey comprehensive evaluation model: 3) Using

<!-- b000141 | prose | pages [8] -->
   T R w E ( r r , ,... ) r 1 2 n

<!-- b000142 | prose | pages [8] -->
By sorting the listed coaches by grey relational degree ir in descending order, we get the rank of all coaches, which enable us to select the top coaches.

<!-- b000143 | heading | pages [8] -->
3 Application

<!-- b000144 | heading | pages [8] -->
3.1 Introduction

<!-- b000145 | prose | pages [8] -->
In this section, we apply our evaluation system to the selection of top 5 all-time col- lege men’s basketball coaches.

<!-- b000146 | heading | pages [8] -->
3.2 The selection of factors

<!-- b000147 | prose | pages [8] -->
We elect two types of factors to represent the accomplishments the coaches have achieved: The awards they have received as excellent coaches and the performance of the teams they coach. This thusly leads to the choice of four factors: Wins, Pct., NCAAB1 Champions, and Coach Awards. Table 1 shows the definition of each fac- tor.

<!-- b000148 | caption | pages [8] -->
Table 1 Factors and Explanations

<!-- b000149 | prose | pages [8] -->
Factors Explanations The number of times that one specific Wins coach has successfully led a team to win Pct. The winning percentage The number of times of winning NCAAB NCAAB Champions championships The number of times of winning the fol- lowing awards: NABC Coach of the Year, Coach Awards Basketball Times National Coach of the year, National Coach of the Year, AP na- tional coach, and Henry iba awards.

<!-- b000150 | prose | pages [8] -->
1 NCAAB: National College Athletic Association Basketball

<!-- b000151 | furniture | pages [9] -->
Team #26636

<!-- b000152 | furniture | pages [9] -->
Page 8 of 38

<!-- b000153 | heading | pages [9] -->
3.3 Data Collection

<!-- b000154 | prose | pages [9] -->
We obtain the data of college men’s basketball coaches, who meet two criteria as fol- lows:  The coaches selected should be the head coaches of NCAA Division I teams be- cause Division I teams represent the highest level of intercollegiate teams.  The wins of coaches, which denote the times that the coaches have led their teams to win, should reach a certain number.

<!-- b000155 | prose | pages [9] -->
The process of data collection consists of the following steps:  We obtain a list of college men’s basketball coaches with more than 600 wins on Wikipedia.2  Having obtained the name list of coaches, we refer to the NCAA Basketball Coaching Records3 to select the coaches of Division I teams.  Next, we searched for the data of the Division I coaches with more than 600 wins in the NCAA database4 to get the data of the four factors we need (wins, winning percentage, times of winning NCAAB championships, and times of winning the title of Coach of the Year).

<!-- b000156 | heading | pages [9] -->
3.4 Calculation

<!-- b000157 | prose | pages [9] -->
Process I: The determination of weights

<!-- b000158 | prose | pages [9] -->
Firstly, we sort the importance of the four factors and create a fuzzy consistent matrix to determine the weight of each factor. This step can be divided into two parts as fol- lows:

<!-- b000159 | prose | pages [9] -->
1) Determine the fuzzy preferential relation matrix Among the four factors, we assume that the times of winning NCAAB championships has greater influence on the evaluation of college coaches’ performances than other factors, while the times of winning the title of Coach of the Year has the least influ- ence. The winning percentage and wins rank second and third respectively. Table 2 summarizes the interrelationship among the four factors.

<!-- b000160 | prose | pages [9, 10] -->
2 Data source: List of college men’s basketball coaches with 600 wins, http://en.wikipedia.org/wiki/List_of_college_men%27s_basketball_coaches_with_600_wins 3 Data source: "NCAA Basketball Coaching Records". NCAA. Retrieved June 14, 2012. http://web1.ncaa.org/web_files/stats/m_basketball_RB/2011/Coaching.pdf 4 Data source: “NCAA Career Statistics Database”. NCAA. Retrieved June 14, 2012. (The NCAA Career Statis- tics database allows the viewer to obtain coaching records for all NCAA coaches by inputting the individual’s name in the linked window.) http://web1.ncaa.org/stats/StatsSrv/careersearch Wins Pct. NCAAB champions Coach Awards Wins 0.5 0 0 1 Pct. 1 0.5 0 1 NCAAB champions 1 1 0.5 1 Coach Awards 0 0 0 0.5

<!-- b000161 | furniture | pages [10] -->
Team #26636

<!-- b000162 | furniture | pages [10] -->
Page 9 of 38

<!-- b000163 | caption | pages [10] -->
Table 2.Interrelationship among the four factors5

<!-- b000165 | prose | pages [10] -->
Therefore, the fuzzy preferential relation matrix is:

<!-- b000166 | prose | pages [10] -->
  0 5 . 0 0 1   1 0 5 . 0 1    A  1 1 0 5 . 1   0 0 0 0 5 .  

<!-- b000167 | prose | pages [10] -->
2) Convert the fuzzy preferential relation matrix to a fuzzy consistent matrix. Using the calculation we have previously explained. The fuzzy consistent matrix is:

<!-- b000168 | prose | pages [10] -->
  0 5000 . 0 3750 . 0 2500 . 0 6250 .   0 6250 . 0 5000 . 0 3750 . 0 7500 .    F  0 7500 . 0 6250 . 0 5000 . 0 8750 .   0 3750 . 0 2500 . 0 1250 . 0 5000 .   Therefore, the weights of the four factors are:

<!-- b000169 | prose | pages [10] -->
  T w  0 2169 . 0 2854 . 0 3527 . 0 1450 .

<!-- b000170 | prose | pages [10] -->
Where 0.2169 is the weight of the times of winning NCAAB championships; 0.2854 is the weight of winning percentage; 0.3527 is the weight of wins; and 0.1450 is the weight of times of winning the title of Coach of the Year.

<!-- b000171 | prose | pages [10] -->
Process II: Using grey correlation analysis to rank coaches

<!-- b000172 | prose | pages [10] -->
1) After preprocessing the data (see Appendix), we get the correlation data array and standard data array by normalizing them by the scaling between 0 and 1. Table 3 dis- plays the correlation data array and the standard data array.

<!-- b000173 | caption | pages [10] -->
Table 3.Correlation data array and standard data array

<!-- b000174 | prose | pages [10] -->
NCAAB Best Name Wins Pct Coach award Champions Coach Mike Krzyzewski 1 0.725118 0.4 0.714285714 1 Jim Boeheim 0.89939 0.658768 0.1 0.285714286 1 Bob Knight 0.77743 0.464455 0.3 0.142857143 1

<!-- b000175 | prose | pages [10] -->
5 The metric of measuring the interrelationship among the factor has already be explained when we define the fuzzy preferential relation matrix.

<!-- b000176 | furniture | pages [11] -->
Team #26636

<!-- b000177 | furniture | pages [11] -->
Page 10 of 38

<!-- b000178 | prose | pages [11, 12] -->
9 0.70731 Dean Smith 0.781991 0.2 0.571428571 1 7 0.69817 Adolph Rupp 1 0.4 0.714285714 1 1 0.68902 Jim Calhoun 0.436019 0.3 0 1 4 0.55792 Jim Phelan 0.009479 0.1 0.142857143 1 7 0.47865 Eddie Sutton 0.469194 0 0.285714286 1 9 Lefty Driesell 0.42378 0.260664 0.1 0 1 0.40548 Lute Olson 0.592417 0.1 0.142857143 1 8 0.40243 Lou Henson 0.203791 0 0 1 9 0.35670 Henry Iba 0.388626 0.2 0 1 7 0.34146 Edgar Diddle 0.492891 0 0 1 3 0.30182 Phog Allen 0.606635 0.1 0 1 9 Jerry Tarkanian 0.25 0.819905 0.1 0 1 0.24695 Norm Stewart 0.236967 0 0 1 1 0.23475 Ray Meyer 0.2891 0.1 0.428571429 1 6 0.21951 Don Haskins 0.28436 0.1 0 1 2 0.19207 Bob Huggins 0.549763 0 0 1 3 0.19512 Roy Williams 0.85782 0.2 0.428571429 1 2 0.08536 Denny Crum 0.402844 0.2 0.428571429 1 6 0.06402 Gary Williams 0.123223 0.1 0 1 4 0.05182 John Wooden 0.914692 1 1 1 9 0.05182 Rick Pitino 0.587678 0.2 0.285714286 1 9 0.03048 Ralph Miller 0.099526 0 0.285714286 1 8 0.02743 Mike Montgomery 0.345972 0 0.285714286 1 9 Cliff Ellis 0 0 0 0 1

<!-- b000179 | furniture | pages [12] -->
Team #26636

<!-- b000180 | furniture | pages [12] -->
Page 11 of 38

<!-- b000182 | prose | pages [12] -->
2) Calculate the grey relational coefficient and the grey relational degree.

<!-- b000183 | caption | pages [12] -->
Table 4. Grey relational coefficient and Grey relational degree matrix

<!-- b000184 | prose | pages [12, 13] -->
NCAAB Cham- Coach Grey relational Name Wins Pct. pions Awards degree Mike 0.6452 0.63636363 1 0.454545455 0.653648096 Krzyzewski 6 6 0.8324 0.5943 0.41176470 Jim Boeheim 0.357142857 0.535868778 87 66 6 0.6919 0.4828 0.36842105 Bob Knight 0.416666667 0.488272356 83 38 3 0.6307 0.6963 0.53846153 Dean Smith 0.384615385 0.54928851 69 7 8 0.6235 0.63636363 Adolph Rupp 1 0.454545455 0.673244141 74 6 0.6165 0.4699 0.33333333 Jim Calhoun 0.416666667 0.463138417 41 33 3 0.5307 0.3354 0.36842105 Jim Phelan 0.357142857 0.3902421 44 53 3 0.4895 0.4850 0.41176470 Eddie Sutton 0.333333333 0.421891832 52 57 6 0.4645 0.4034 0.33333333 Lefty Driesell 0.357142857 0.39020928 89 42 3 0.4568 0.5509 0.36842105 Lute Olson 0.357142857 0.435701385 25 14 3 0.4555 0.3857 0.33333333 Lou Henson 0.333333333 0.374800311 56 4 3 0.4373 0.4498 0.33333333 Henry Iba 0.384615385 0.407244353 33 93 3 0.4315 0.4964 0.33333333 Edgar Diddle 0.333333333 0.40120218 79 71 3 0.4173 0.5596 0.33333333 Phog Allen 0.357142857 0.424543753 03 82 3 0.7351 0.33333333 Jerry Tarkanian 0.4 0.357142857 0.470881312 92 3 0.3990 0.3958 0.33333333 Norm Stewart 0.333333333 0.365430894 27 72 3 0.3951 0.4129 0.46666666 Ray Meyer 0.357142857 0.397191835 81 16 7 Don Haskins 0.3904 0.4113 0.357142857 0.33333333 0.376378649 76 06 3 0.3822 0.5261 0.33333333 Bob Huggins 0.333333333 0.39899055 84 85 3 0.3831 0.7785 0.46666666 Roy Williams 0.384615385 0.508643536 78 98 7 0.3534 0.4557 0.46666666 Denny Crum 0.384615385 0.410046943 48 24 7 0.3481 0.3631 0.33333333 Gary Williams 0.357142857 0.353469034 95 67 3 0.3452 0.8542 John Wooden 1 1 0.816390818 63 51 0.3452 0.5480 0.41176470 Rick Pitino 0.384615385 0.426661333 63 52 6 0.3402 0.3570 0.41176470 Ralph Miller 0.333333333 0.352966627 49 22 6 Mike Mont- 0.3395 0.4332 0.41176470 0.333333333 0.374573553 gomery 45 65 6 0.3333 0.3333 0.33333333 Cliff Ellis 0.333333333 0.333333333 33 33 3

<!-- b000185 | furniture | pages [13] -->
Team #26636

<!-- b000186 | furniture | pages [13] -->
Page 12 of 38

<!-- b000188 | prose | pages [13] -->
3) Sort the listed coaches by grey relational degree in descending order to select the top coaches.

<!-- b000189 | caption | pages [13] -->
Table 5. Rank of college men’s basketball coaches

<!-- b000190 | prose | pages [13, 14] -->
Win NCAAB Champi- Coach Grey relational de- Name Pct s ons Awards gree 0.80 John Wooden 664 10 7 0.816421266 4 0.82 Adolph Rupp 876 4 5 0.673237909 2 Mike 0.76 975 4 5 0.653625969 Krzyzewski 4 0.77 Dean Smith 879 2 4 0.549279075 6 Jim Boeheim 942 0.75 1 2 0.535847239 0.79 Roy Williams 711 2 3 0.508643731 2 0.70 Bob Knight 902 3 1 0.488258607 9 0.78 Jerry Tarkanian 729 1 0 0.470877508 4 0.70 Jim Calhoun 873 3 0 0.463127488 3 Lute Olson 780 0.73 1 1 0.435696335 6 0.73 Rick Pitino 664 2 2 0.426663053 5 0.73 Phog Allen 746 1 0 0.424539802 9 Eddie Sutton 804 0.71 0 2 0.421885645 0.69 Denny Crum 675 2 3 0.410049682 6 0.69 Henry Iba 764 2 0 0.407240719 3 0.71 Edgar Diddle 759 0 0 0.401197092 5 0.72 Bob Huggins 710 0 0 0.398987605 7 0.67 Ray Meyer 724 1 3 0.397191997 2 0.61 Jim Phelan 830 1 1 0.390234465 3 0.66 Lefty Driesell 786 1 0 0.390203744 6 0.67 Don Haskins 719 1 0 0.37637647 1 0.65 Lou Henson 779 0 0 0.374794534 4 Mike Montgom- 0.68 656 0 2 0.374574409 ery 4 0.66 Norm Stewart 728 0 0 0.365427663 1 0.63 Gary Williams 668 1 0 0.353468964 7 0.63 Ralph Miller 657 0 2 0.352967731 2 0.61 Cliff Ellis 647 0 0 0.333333333 1 Coaches marked in grey are the top 5 basketball coaches of all time.

<!-- b000191 | furniture | pages [14] -->
Team #26636

<!-- b000192 | furniture | pages [14] -->
Page 13 of 38

<!-- b000194 | heading | pages [14] -->
3.5 Application of our model to other sports

<!-- b000195 | prose | pages [14] -->
In our model, the four factors we choose can be broadly applied to various kinds of college sports. When we apply our model to other fields, what we should to is just to choose the projects which can represent NCAA champions and Coach Awards in the specific field. So it is convenient for us to apply our model to other fields. The factors and explanations are shown in Table 6.1 and Table 6.2. The top 5 of both sports are shown in Table 7.1 and Table 7.2 respectively.

<!-- b000196 | furniture | pages [15] -->
Team #26636

<!-- b000197 | furniture | pages [15] -->
Page 14 of 38

<!-- b000198 | caption | pages [15] -->
Table 6.1. Factors and Explanations in football

<!-- b000199 | prose | pages [15] -->
Factors Explanations The number of times that one specific coach has success- Wins fully led a team to win Pct. The winning percentage NCAA National Cham- The amount of Bowl pionship Bobby Dodd Coach of the Year Award Walter Camp Coach of the Year Award Amos Alonzo Stagg Award AFCA Coach of the Year Paul 'Bear' Bryant Award Coach Awards George Munger Award Home Depot Coach of the Year Award Sporting News College Football Coach of the Year Associated Press Coach of the Year Joseph V. Paterno Award National Coach of the Year

<!-- b000200 | caption | pages [15] -->
Table 6.2. Factors and Explanations in ice-hockey

<!-- b000201 | prose | pages [15] -->
Factors Explanations The number of times that one specific coach has successfully Wins led a team to win Pct. The winning percentage NCCA Champions NCAA National Championship Spencer Penrose national Coach of the Year(only for division one) Coach Awards Lester Patrick Trophy (start from 1966) Jack Adams Award NCAA Coach of the Year

<!-- b000202 | caption | pages [15] -->
Table 7.1.Top 5college men’s football coaches

<!-- b000203 | prose | pages [15] -->
National cham- Coach Grey relational Name Wins Pct. pions Awards degree Bear Bryant 323 0.78 6 3 0.744053013 Jim Tressel 229 0.74 5 12 0.605457523 Tom Osborne 255 0.84 3 2 0.605088237 Bobby Bowden 377 0.74 2 3 0.592330117 Woody Hayes 238 0.76 5 4 0.588162393

<!-- b000204 | caption | pages [15] -->
Table 7.2.Top 5 college men’s ice hockey coaches

<!-- b000205 | prose | pages [15, 16] -->
Name Wins Pct. NCAA champions Coach Grey relation- Awards al degree Jerry York 935 0.614 5 2 0.694032022 Vic Heyliger 352 0.685 6 1 0.684648603 Jack Parker 897 0.643 3 3 0.609648054 Ron Mason 924 0.696 0 1 0.598317509 Ned Harkness 380 0.74 3 1 0.590984292

<!-- b000206 | furniture | pages [16] -->
Team #26636

<!-- b000207 | furniture | pages [16] -->
Page 15 of 38

<!-- b000209 | heading | pages [16] -->
4 Comparison of the ranks from different sources

<!-- b000210 | prose | pages [16] -->
We compare the top 5 coaches in our lists with those in the reports from ESPN or oth- er research institutes. We find that the results are mostly identical.

<!-- b000211 | caption | pages [16] -->
Table 8.Comparison of the rank of top 5 college men’s basketball coaches

<!-- b000212 | prose | pages [16] -->
ESPN(include wom- Yahoo RANK The Model Bleacher Report an) Sports John 1 John Wooden John wooden John Wooden Wooden Mike 2 Adolph Rupp Bob knight Dean Smith Krzyzew sk Dean 3 Mike Krzyzewski Mike Krzyzewski Mike Krzyzewski Smith Bob 4 Dean Smith Adolph Rupp Pat Summitt Knight Jerry Tar- 5 Jim Boeheim Dean Smith John Mclendon Tar- kanian

<!-- b000213 | caption | pages [16] -->
Table 9.Comparison of the rank of top 5 college men’s football coaches

<!-- b000214 | prose | pages [16] -->
RANK The Model Yahoo Sports Statesman Orlando Sentinel 1 Bobby Bowden Bear Bryant Bear Bryant Bear Bryant 2 Bear Bryant Knute Rockne Knute Rockne Nick Saban 3 Glenn Scobey Warner Joe Paterno Glenn Pop Warner Bobby Bowden 4 Amos Alonzo Stagg Tom Osborne Fielding Yost Eddie Robinson 5 Joe Paterno Woody Hayes Joe Paterno Woody Hayes

<!-- b000215 | caption | pages [16] -->
Table 10. Comparison of the rank of top 5 college men’s ice-hockey coaches

<!-- b000216 | prose | pages [16, 17] -->
RANK The Model Inside College Hockey 1 Jerry York Bob Johnson 2 Vic Heyliger Herb Brooks 3 Jack Parker Murray Armstrong 4 Ron Mason Jack Parker 5 Ned Harkness Ned Harkness

<!-- b000217 | furniture | pages [17] -->
Team #26636

<!-- b000218 | furniture | pages [17] -->
Page 16 of 38

<!-- b000220 | heading | pages [17] -->
5 The analysis of time line horizon

<!-- b000221 | heading | pages [17] -->
5.1 Introduction

<!-- b000222 | prose | pages [17] -->
The NCAA Championships have a history of approximately seventy years. During such a long span of time, the competition system has experienced a series of reforms. In early years, the number of sports events was much less than it is today, thus the competition among sports teams might be less intense. Therefore, there might be a difference among the average winning percentages in different time line horizon. If so, we can no longer justify our previous model, which ignores the influence of time line horizon and equally treats coaches from different periods in terms of winning per- centage.

<!-- b000223 | prose | pages [17] -->
Therefore, we intend to explore whether there is a connection, to some degree, be- tween the factors we choose and the time line horizon. Note that it is difficult to ac- quire the data of the times of winning coach of the year within limited amount of time. So we decide to use the rest of factors (Wins, Pct., and times of winning national championships) to examine if those factors change during different time line horizons. If the time line horizon does have significant influence on the rest of our factors, we need to modify our model. Now we process the data of college men’s basketball coaches to see if there is a need for us to modify our model.

<!-- b000224 | heading | pages [17] -->
5.2 Procedures

<!-- b000225 | prose | pages [17] -->
Step 1.Firstly, we obtain the data of college men’s basketball coaches who have coached their teams in more than 400 games. We select the coaches from all three di- visions because the reforms of competition system cover all the divisions. The raw data are attached in appendix.

<!-- b000226 | prose | pages [17] -->
Step 2.Secondly, we sort the coaches by the year they start their coaching career and divide them into five groups as follows:  Coaches who started their career before 1930s (group 1).  Coaches who started their career during 1930s and 1940s (group 2).  Coaches who started their career during 1950s and 1960s (group 3).  Coaches who started their career during 1970s and 1980s (group 4).  Coaches who started their career during 1990s and 2000s (group 5).

<!-- b000227 | prose | pages [17] -->
Then we calculate the mean and variance of each factor in each group. Figure 1 shows the means of winning percentages in all groups. Figure 2 shows the means of wins in all groups. Figure 3 shows the mean values of the times of winning NCAAB champi- onships in all groups.

<!-- b000228 | furniture | pages [18] -->
Team #26636

<!-- b000229 | furniture | pages [18] -->
Page 17 of 38

<!-- b000230 | caption | pages [18] -->
Figure 1.The mean values of winning percentages

<!-- b000231 | caption | pages [18] -->
Figure 2.The mean values of wins

<!-- b000232 | furniture | pages [19] -->
Team #26636

<!-- b000233 | furniture | pages [19] -->
Page 18 of 38

<!-- b000234 | caption | pages [19] -->
Figure 3.The mean values of NCAAB Champions6

<!-- b000235 | prose | pages [19] -->
Step 3. We find that the line in Figure 1 smoothly goes down, which means that it is easier for good college basketball coaches in early years to get a high winning percentage. This is reasonable because the competition in not so intense in previous years as it is today. Therefore, with the same weights, using winning percentage to evaluate performance is not fair for younger coaches. Thus we should devise a correction factor to modify it.

<!-- b000236 | prose | pages [19] -->
Although this trend is clearly shown in Figure 1. It is still necessary for us to use one-way analysis of variance to test whether there is a significant difference among the variances of different groups. If the difference among variances is acceptable, we need to make adjustment to our model according to the tendency.

<!-- b000237 | caption | pages [19] -->
Table 11.

<!-- b000238 | prose | pages [19] -->
Source of SS Df MS F P-value F crit Difference Among the 1.988653 0.026814016 2 0.013407 0.138645 3.025253 five groups 5 Within each 2.062976049 306 0.006742 group Sum 2.08979006 308

<!-- b000239 | caption | pages [19] -->
Table 12.

<!-- b000240 | prose | pages [19] -->
Source of SS Df MS F P-value F crit Difference Among the 3.3817 0.009770 2.3950026 0.114121057 4 0.02853026 five groups 495 28 16 Within each 3.264940845 387 0.00843654 group sum 3.3790619 391

<!-- b000241 | caption | pages [19] -->
Table 11 demonstrates that the P-value is greater than 0.05, which means there is not a

<!-- b000242 | prose | pages [19] -->
significant difference of variances among group 3, group 4 and group 5. Table 12 shows that there is a significant difference of variances among all five groups. So there exists some extreme values (the data of some outstanding coaches) that raises the variances of group 1 and group 2.

<!-- b000243 | prose | pages [19] -->
Therefore, only the increasing tendency of group 3, group 4, and group 5’s winning percentages can be used to set a correction factor. Under two circumstances as follows, we should adopt different approaches to set correction factors.

<!-- b000244 | prose | pages [19] -->
6 The sharp change of the line in 1930s-1940s is because that John wooden had won about 10 champions, if we exclude him from the sample, the line will become flat, so the time line horizon makes no difference on the NCAAB champion.

<!-- b000245 | furniture | pages [20] -->
Team #26636

<!-- b000246 | furniture | pages [20] -->
Page 19 of 38

<!-- b000247 | prose | pages [20] -->
 The selection of the best all-time coaches who start coaching after 1950s  The selection of the best all-time coaches who start coaching after 1900s

<!-- b000248 | prose | pages [20] -->
Step 4. Now we set a correction factor to reduce the winning percentages of coaches in previous years and increase the winning percentages of present coaches. We adopt the weighted moving average method to calculate the correction factor.

<!-- b000249 | prose | pages [20] -->
1) To select the best all-time coaches who started their coaching careers after 1950s, is: we need to modify our model. The correction factor i 1  i iS

<!-- b000250 | prose | pages [20] -->
n  Y Z i i  i 1 Where S , iZ is the number of samples within group i , iY is the mean val- i n  Z i  i 1

<!-- b000251 | prose | pages [20] -->
ue of the winning percentage of group i .

<!-- b000252 | caption | pages [20] -->
Table 13 shows the winning percentages and grey relational degree of top 10 coaches

<!-- b000253 | prose | pages [20] -->
before adjustment, while Table 14 shows the winning percentages and grey relational degree of top 10 coaches after adjustment.

<!-- b000254 | caption | pages [20] -->
Table 13.The rank of Top 10 college men’s basketball coaches before adjustment

<!-- b000255 | prose | pages [20] -->
Name Pct. Grey relational degree 0.804 0.816421 John Wooden 0.822 0.673238 Adolph Rupp 0.764 0.653626 Mike Krzyzewski 0.776 0.549279 Dean Smith 0.75 0.535847 Jim Boeheim 0.792 0.508644 Roy Williams 0.709 0.488259 Bob Knight 0.784 0.470878 Jerry Tarkanian 0.703 0.463127 Jim Calhoun 0.736 0.435696 Lute Olson

<!-- b000256 | caption | pages [20] -->
Table 147.The rank of Top 10 college men’s basketball coaches after adjustment

<!-- b000257 | prose | pages [20] -->
Name Correction factor Pct. Grey relational degree Mike Krzyzewski 1.733399695 1.324317367 0.9204074 Roy Williams 1.733399695 1.372852558 0.586667007 Dean Smith 1.695298373 1.315551537 0.574608911 Jim Boeheim 1.733399695 1.300049771 0.53458653

<!-- b000258 | prose | pages [20] -->
7 Because we select the best all time coaches who start coaching after 1950s, John Wooden and Adolph Rupp who start their coaching careers in 1930s should not have been on the list.

<!-- b000259 | furniture | pages [21] -->
Team #26636

<!-- b000260 | furniture | pages [21] -->
Page 20 of 38

<!-- b000261 | prose | pages [21] -->
Bob Knight 1.695298373 1.201966546 0.525580488 Jim Calhoun 1.733399695 1.218579985 0.508524212 Jerry Tarkanian 1.733399695 1.35898536 0.496549075 Rick Pitino 1.733399695 1.274048775 0.438797739 Lute Olson 1.733399695 1.275782175 0.419173266 Denny Crum 1.733399695 1.206446187 0.417960291

<!-- b000262 | prose | pages [21] -->
2) For coaches who started their coaching careers between 1900s and 1950s, we find out that group 1 and group 2 contains extreme values. The two outstanding coaches, those data are probably the extreme values, are John Wooden and Adolph Rupp. After eliminating their data, we repeat our one-way data analysis of variance and find that the P-value among five groups increases to 0.08, which is greater than 0.05. Thus we can know for sure that the data of John Wooden and Adolph Rupp are extreme values.

<!-- b000263 | prose | pages [21] -->
Although John Wooden and Adolph Rupp are among the greatest coaches in NCAAB in early years, we cannot assume that they would be as successful today. Therefore, when we select the best all-time coaches who started their coaching careers after 1900s, we should set a correction factor to reduce their grey relational degrees. However, because of the scarcity of data, we cannot use a precise formulation for calculation.

<!-- b000264 | prose | pages [21] -->
Although we only explain the principle for modifying our model based on the data of college men’s basketball coaches in this section, this approach is applicable to other sports (such as football and ice-hockey) because of the generality of the factors we select. We also find that the winning percentage we use to select the best all-time coaches in NCAA football has the same tendency as it is when we analyze the relationship between winning percentage and the time line horizon. Using the one-way analysis of variance, we find that its P-value is 0.07 (greater than 0.05), which means that we can still use the moving weighted average method to get our correction factor in the evaluation of best all-time college men’s football coaches.

<!-- b000265 | heading | pages [21] -->
6 The analysis of gender

<!-- b000266 | prose | pages [21] -->
By analyzing the data of college women’s basketball coaches, we find that the four factors we select have no relation to gender and that the weight of each indicator doesn’t change. Table 15 displays the top 5 of college women’s basketball coaches.

<!-- b000267 | caption | pages [21] -->
Table 15 The top 5 of college women’s basketball coaches

<!-- b000268 | prose | pages [21, 22] -->
Grey NCAA Coach Name Wins Pct. relational Champions Awards degree Pat Summitt 1098 0.841 8 8 0.989807143 C. Vivian 916 0.732 0 0 0.60757619 Stringer Tara 910 0.817 2 4 0.54686006 VanDerveer Sylvia 908 0.739 1 6 0.481908161 Hatchell Barbara Ste- 900 0.785 0 0 0.476794451 vens

<!-- b000269 | furniture | pages [22] -->
Team #26636

<!-- b000270 | furniture | pages [22] -->
Page 21 of 38

<!-- b000272 | heading | pages [22] -->
7 Stability test

<!-- b000273 | heading | pages [22] -->
7.1 Testing the influence of changing the method on the de-

<!-- b000274 | prose | pages [22] -->
termination of weights

<!-- b000275 | heading | pages [22] -->
7.1.1 Introduction

<!-- b000276 | prose | pages [22] -->
In this section, we use Shannon’s entropy method to determine the weight of each factor. Then we use grey correlation analysis, which has identical processes as above, to obtain the rank of coaches to see if there is any difference between the two methods (the fuzzy consistent matrix method and the entropy method) for determining weights.

<!-- b000277 | heading | pages [22] -->
7.1.2 Notation

<!-- b000278 | heading | pages [22] -->
Notation

<!-- b000279 | prose | pages [22] -->
Explanation C Raw data matrix

<!-- b000280 | prose | pages [22] -->
' Modified raw data matrix C

<!-- b000281 | prose | pages [22] -->
Q Decision matrix

<!-- b000282 | prose | pages [22] -->
ih Entropy W Weights of factors under the entropy method

<!-- b000283 | heading | pages [22] -->
7.1.3 Using Shannon’s entropy method to determine the weight of

<!-- b000284 | prose | pages [22] -->
each factor

<!-- b000285 | prose | pages [22] -->
Shannon’s entropy method is a well-known method for determining the weights for multiple attribute decision making (MADM) process (Lotfi., et, al.,2010). Entropy is a metric for measuring the degree of disorder in a system. For a specific factor in the system, when there is a large difference among its values, the entropy value is com- paratively large, while a factor with less discrepancy among its values has smaller en- tropy value.

<!-- b000286 | prose | pages [22, 23] -->
Using this approach, we can determine the weight of each factor in our coach evalua- tion system. The factor with larger entropy is less importance in our system, and thus has smaller weight. The factor with smaller entropy is more important in our system, and thus has larger weight.

<!-- b000287 | furniture | pages [23] -->
Team #26636

<!-- b000288 | furniture | pages [23] -->
Page 22 of 38

<!-- b000290 | prose | pages [23] -->
Therefore, the procedures for determining weights can be expressed as follows:

<!-- b000291 | prose | pages [23] -->
1) If the i th factor has some extreme values, we should modify the raw data ma-

<!-- b000292 | prose | pages [23] -->
  ' trix to create a new matrix and thusly eliminate the negative C ( c ) C ( c )   ij n m ij n m

<!-- b000293 | prose | pages [23] -->
influence of extreme values on our model.

<!-- b000294 | prose | pages [23] -->
' The formula for creating C is:

<!-- b000295 | prose | pages [23] -->
 c min( c ) ij ij    ' c u v ij  max( c ) min( c ) ij ij

<!-- b000296 | prose | pages [23] -->
m m m        2 2 Where u c / ( c c ) , v 1 / ( c c ) . ij ij ij ij ij    i 1 i 1 i 1

<!-- b000297 | prose | pages [23] -->
  ' 2) Normalize the raw data matrix to create matrix . C ( c ) Q ( q )   ij n m ij n m

<!-- b000298 | prose | pages [23] -->
The factors of this model are positive factors, which mean that the factors with greater

<!-- b000299 | prose | pages [23] -->
values are better. Therefore, the formula for creatingQ is:

<!-- b000300 | prose | pages [23] -->
 c min{ c } ij ij j   q 1 ij  max{ c } min{ c } ij ij j j By normalizing the modified raw data matrix, we can eliminate the anomalies resulted from different dimensions and metrics for measuring the data.

<!-- b000301 | heading | pages [23] -->
3) Based on the decision matrixQ , we calculate the entropy of each factor:

<!-- b000302 | prose | pages [23] -->
m  h k d ln d i ij ij  j 1

<!-- b000303 | prose | pages [23] -->
m   .ln d is defined as 0 Where ih is the i th factor’s entropy. d q / q . k=1/ ln m ij ij ij ij  i 1 d  0 if . ij

<!-- b000304 | prose | pages [23] -->
4) Now we can calculate the weight of each factor. Suppose that the number of objects is m and the number of factors is n.

<!-- b000305 | prose | pages [23, 24] -->
By using the following formula, we can calculate the weight of each factor in a sys- tem.

<!-- b000306 | furniture | pages [24] -->
Team #26636

<!-- b000307 | furniture | pages [24] -->
Page 23 of 38

<!-- b000309 | prose | pages [24] -->
 1 h i  W i n  n h i i=1

<!-- b000310 | prose | pages [24] -->
n     Where . 0 W 1 , W 1 i i  i 1

<!-- b000311 | prose | pages [24] -->
In our model, we calculate the weights of the four factors as follows:

<!-- b000312 | prose | pages [24] -->
  T W  0 2493 . 0 2492 . 0 2508 . 0 2507 .

<!-- b000313 | prose | pages [24] -->
Where 0.2493 is the weight of the times of winning NCAAB championships; 0.2492 is the weight of winning percentage; 0.2508 is the weight of wins; and 0.2507 is the weight of times of winning the title of Coach of the Year.

<!-- b000314 | caption | pages [24] -->
Table 16 shows the rank of college coaches based on Shannon’s entropy method and

<!-- b000315 | prose | pages [24] -->
grey correlation analysis.

<!-- b000316 | caption | pages [24] -->
Table 16.Results based on Entropy Method

<!-- b000317 | prose | pages [24, 25] -->
NCAAB Coach Grey relational NAME WINS Pct. degree Champions Awards John Wooden 664 0.804 10 7 0.80048 Mike Krzyzewski 975 0.764 4 5 0.68361 Adolph Rupp 876 0.822 4 5 0.678202 Dean Smith 879 0.776 2 4 0.562236 Jim Boeheim 942 0.75 1 2 0.548441 Roy Williams 711 0.792 2 3 0.503022 Bob Knight 902 0.709 3 1 0.489688 Jim Calhoun 873 0.703 3 0 0.458873 Jerry Tarkanian 729 0.784 1 0 0.456083 Lute Olson 780 0.736 1 1 0.433112 Eddie Sutton 804 0.71 0 2 0.429747 Rick Pitino 664 0.735 2 2 0.422348 Phog Allen 746 0.739 1 0 0.416651 Denny Crum 675 0.696 2 3 0.415138 Ray Meyer 724 0.672 1 3 0.407979 Henry Iba 764 0.693 2 0 0.401171 Edgar Diddle 759 0.715 0 0 0.398482 Jim Phelan 830 0.613 1 1 0.397834 Bob Huggins 710 0.727 0 0 0.393601 Lefty Driesell 786 0.666 1 0 0.389495 Mike Montgomery 656 0.684 0 2 0.379449 Lou Henson 779 0.654 0 0 0.376859 Don Haskins 719 0.671 1 0 0.372983 Norm Stewart 728 0.661 0 0 0.365295 Ralph Miller 657 0.632 0 2 0.360621 Gary Williams 668 0.637 1 0 0.350446 Cliff Ellis 647 0.611 0 0 0.333333 Coaches marked in grey are the top 5 basketball coaches of all time.

<!-- b000318 | furniture | pages [25] -->
Team #26636

<!-- b000319 | furniture | pages [25] -->
Page 24 of 38

<!-- b000321 | heading | pages [25] -->
7.1.4 Comparison of the outcomes

<!-- b000322 | prose | pages [25] -->
In order to test the stability of our model, we now compare the outcome from using the fuzzy consistent matrix to determine weights with the outcome from using the en- tropy method.

<!-- b000323 | caption | pages [25] -->
Table 17.Comparison between Fuzzy Consistent Matrix Method and Entropy Method

<!-- b000324 | prose | pages [25] -->
RANK Fuzzy Consistent Matrix Entropy Method 1 John Wooden John Wooden 2 Adolph Rupp Mike Krzyzewski 3 Mike Krzyzewski Adolph Rupp 4 Dean Smith Dean Smith 5 Jim Boeheim Jim Boeheim 6 Roy Williams Roy Williams 7 Bob Knight Bob Knight 8 Jerry Tarkanian Jim Calhoun 9 Jim Calhoun Jerry Tarkanian 10 Lute Olson Lute Olson

<!-- b000325 | caption | pages [25] -->
Table 17 shows that the name lists of top 10 coaches generated from the above two

<!-- b000326 | prose | pages [25] -->
methods are identical, while there is a slight difference among the ranks. Therefore, we can reach the conclusion that our model is stable.

<!-- b000327 | heading | pages [25] -->
7.2 Testing the influence of changing the comparative im-

<!-- b000328 | prose | pages [25] -->
portance among the four factors

<!-- b000329 | prose | pages [25] -->
Now we change the comparative importance among the four factors in the evaluation of college men’s basketball coaches to see if there is a significant difference between the outcomes.

<!-- b000330 | caption | pages [25] -->
Table 18.The comparative importance among factors after adjustment

<!-- b000331 | prose | pages [25, 26] -->
Wins Pct. NCCAB Champions Coach Awards Wins 0.5 0 0 0 Pct. 1 0.5 0 0 NCCAB Champions 1 1 0.5 1 Coach Awards 1 1 0 0.5

<!-- b000332 | furniture | pages [26] -->
Team #26636

<!-- b000333 | furniture | pages [26] -->
Page 25 of 38

<!-- b000335 | caption | pages [26] -->
Table 19 displays the rank of college men’s basketball coaches after adjustment. Table

<!-- b000336 | prose | pages [26] -->
20 compares the outcome in this section with the outcome in the previous section.

<!-- b000337 | caption | pages [26] -->
Table 19.Rank of college men’s basketball coaches after adjustment

<!-- b000338 | prose | pages [26] -->
NCAAB Coach Grey rela- NAME WINS Pct. Champions Awards tional degree John Wooden 664 0.804 10 7 0.873444278 Adolph Rupp 876 0.822 4 5 0.649232275 Mike Krzyzewski 975 0.764 4 5 0.626894346 Dean Smith 879 0.776 2 4 0.531824804 Roy Williams 711 0.792 2 3 0.493260791 Jim Boeheim 942 0.75 1 2 0.493108718 Bob Knight 902 0.709 3 1 0.45717316 Jerry Tarkanian 729 0.784 1 0 0.438544324 Jim Calhoun 873 0.703 3 0 0.433420385 Rick Pitino 664 0.735 2 2 0.422098796 Denny Crum 675 0.696 2 3 0.4189328 Lute Olson 780 0.736 1 1 0.416837441 Eddie Sutton 804 0.71 0 2 0.411274136 Ray Meyer 724 0.672 1 3 0.406011386 Phog Allen 746 0.739 1 0 0.402993475 Henry Iba 764 0.693 2 0 0.391780608 Edgar Diddle 759 0.715 0 0 0.382957853 Bob Huggins 710 0.727 0 0 0.382252792 Jim Phelan 830 0.613 1 1 0.380833646 Mike Montgomery 656 0.684 0 2 0.378288688 Lefty Driesell 786 0.666 1 0 0.375969596 Don Haskins 719 0.671 1 0 0.366927201 Lou Henson 779 0.654 0 0 0.362422603 Ralph Miller 657 0.632 0 2 0.361857247 Norm Stewart 728 0.661 0 0 0.356422014 Gary Williams 668 0.637 1 0 0.350356494 Cliff Ellis 647 0.611 0 0 0.333333333

<!-- b000339 | caption | pages [26] -->
Table 20.Comparison of outcomes based on two different Fuzzy Consistent Matrixes

<!-- b000340 | prose | pages [26, 27] -->
RANK Fuzzy Consistent Matrix1 Fuzzy Consistent Matrix2 1 John Wooden John Wooden 2 Adolph Rupp Adolph Rupp 3 Mike Krzyzewski Mike Krzyzewski 4 Dean Smith Dean Smith 5 Jim Boeheim Roy Williams 6 Roy Williams Jim Boeheim 7 Bob Knight Bob Knight 8 Jerry Tarkanian Jerry Tarkanian 9 Jim Calhoun Jim Calhoun 10 Lute Olson Rick Pitino

<!-- b000341 | furniture | pages [27] -->
Team #26636

<!-- b000342 | furniture | pages [27] -->
Page 26 of 38

<!-- b000344 | prose | pages [27] -->
We can see from Table 20 that the outcome is slightly different when compared with the outcome in the previous section. Based on section 6.1 and 6.2, we can reach the conclusion that our model is stable.

<!-- b000345 | heading | pages [27] -->
8 Sensitivity test

<!-- b000346 | prose | pages [27] -->
 In previous section, we assume that the distinguishing coefficient . This as- 0 5.

<!-- b000347 | prose | pages [27] -->
sumption of this value is based on experience. Therefore, we need to change the value

<!-- b000348 | prose | pages [27] -->
of to see if the value of will exert significant influence on our model.

<!-- b000349 | prose | pages [27] -->


<!-- b000350 | caption | pages [27] -->
Table 21 shows the rank of coaches when

<!-- b000351 | prose | pages [27] -->
, while Table 22 and Table 23show 0 5.

<!-- b000352 | prose | pages [27] -->
the rank of coaches when is equal to 0.4 and 0.6 respectively.

<!-- b000353 | caption | pages [27] -->
Table 21. Rank of college men’s basketball coaches ( =0.5)

<!-- b000354 | prose | pages [27] -->
Grey Relational Degree ( =0.5) RANK NAME

<!-- b000355 | prose | pages [27] -->
1 Mike Krzyzewski 0.816390818 2 Jim Boeheim 0.673244141 3 Bob Knight 0.653648096 4 Dean Smith 0.54928851 5 Adolph Rupp 0.535868778 6 Jim Calhoun 0.508643536 7 Jim Phelan 0.488272356 8 Eddie Sutton 0.470881312 9 Lefty Driesell 0.463138417 10 Lute Olson 0.435701385

<!-- b000356 | caption | pages [27] -->
Table 22. Rank of college men’s basketball coaches ( =0.4)

<!-- b000357 | prose | pages [27] -->
Grey Relational Degree ( =0.4) RANK NAME

<!-- b000358 | prose | pages [27, 28] -->
1 Mike Krzyzewski 0.816421 2 Jim Boeheim 0.673238 3 Bob Knight 0.653626 4 Dean Smith 0.549279 5 Adolph Rupp 0.535847 6 Jim Calhoun 0.508644 7 Jim Phelan 0.488259 8 Eddie Sutton 0.470878 9 Lefty Driesell 0.463127 10 Lute Olson 0.435696

<!-- b000359 | furniture | pages [28] -->
Team #26636

<!-- b000360 | furniture | pages [28] -->
Page 27 of 38

<!-- b000362 | caption | pages [28] -->
Table 23.Rank of college men’s basketball coaches ( =0.6)

<!-- b000363 | prose | pages [28] -->
Grey Relational Degree ( =0.6)公式 RANK NAME

<!-- b000364 | prose | pages [28] -->
1 Mike Krzyzewski 0.831661964 2 Jim Boeheim 0.70427652 3 Bob Knight 0.687185051 4 Dean Smith 0.590853876 5 Adolph Rupp 0.574939217 6 Jim Calhoun 0.54878576 7 Jim Phelan 0.531490084 8 Eddie Sutton 0.511362919 9 Lefty Driesell 0.507122379 10 Lute Olson 0.479680225

<!-- b000365 | prose | pages [28] -->
By comparing the above three tables, we find that the top 10 college men’s basketball

<!-- b000366 | prose | pages [28] -->
coaches are identical, which means that our model is insensitive to the change of .

<!-- b000367 | heading | pages [28] -->
9 Strengths and Weaknesses

<!-- b000368 | heading | pages [28] -->
9.1 Strengths

<!-- b000369 | prose | pages [28] -->
 It is convenient and broadly applicable to use our model to select the top col- lege coaches. Utilizing the grey correlation analysis method, our model has high precision and is convenient for researches to assess the performances of coaches.

<!-- b000370 | prose | pages [28] -->
The four factors we select can be universally adopted when analyzing different sports in NCAA or coaches of different genders.  Our model has good stability. Our outcomes are nearly identical when different method of analyzing stability and sensitivity is adopted.

<!-- b000371 | furniture | pages [29] -->
Team #26636

<!-- b000372 | furniture | pages [29] -->
Page 28 of 38

<!-- b000373 | heading | pages [29] -->
9.2 Weaknesses

<!-- b000374 | prose | pages [29] -->
 The standard for selecting factors is rigorous to some degree. In terms of se- lection of best all-time college men’s football coaches, we choose Division I coaches with more than 200 wins. However, some famous coaches, although fail to achieve 200 wins, should have been granted the qualification to be selected as best all-time coaches.  The collection of the numbers of Coach Awards is subjective. Some awards should not have been included.  The analysis of time line horizon is imperfect. For example, it is difficult for us to set a correction factor for coaches who started their careers before 1950s.

<!-- b000375 | heading | pages [29] -->
Reference

<!-- b000376 | references | pages [29] -->
[1] Rushall, B. S., and K. Wiznuk. "Athletes' assessment of the coach--the coach

<!-- b000377 | references | pages [29] -->
evaluation questionnaire." Canadian journal of applied sport sciences. Journal cana-

<!-- b000378 | references | pages [29] -->
dien des sciences appliquées au sport.10.3 (1985): 157.

<!-- b000379 | references | pages [29] -->
[2] Cassidy, Tania, Paul Potrac, and Alex McKenzie. "Evaluating and Reflecting Upon

<!-- b000380 | references | pages [29] -->
a Coach Education Initiative: The CoDe^ 1 of Rugby." Sport Psychologist20.2 (2006):

<!-- b000381 | references | pages [29] -->
145.

<!-- b000382 | references | pages [29] -->
[3] Nelson, Lee J., and Christopher J. Cushion. "Reflection in coach education: the

<!-- b000383 | references | pages [29] -->
case of the national governing body coaching certificate." Sport Psychologist20.2

<!-- b000384 | references | pages [29] -->
(2006): 174.

<!-- b000385 | references | pages [29] -->
[4] Lotfi F H, Fallahnejad R. Imprecise Shannon’s entropy and multi attribute deci-

<!-- b000386 | references | pages [29] -->
sion making[J]. Entropy, 2010, 12(1): 53-62.

<!-- b000387 | references | pages [29] -->
[5] Saaty, T.L. The Analytic Hierarchy Process; McGraw-Hill: NewYork, NY, USA,

<!-- b000388 | references | pages [29] -->
1980.

<!-- b000389 | references | pages [29] -->
[6] Hwang, C.L.; Lin, M.J. Group Decision Making under Multiple Criteria: Methods

<!-- b000390 | references | pages [29] -->
and Applications; Springer: Berlin, Germany, 1987.

<!-- b000391 | references | pages [29] -->
[7] Fan, Z.P. Complicated multiple attribute decision making: Theory and applica-

<!-- b000392 | references | pages [29] -->
tions. Ph.D Dissertation; Northeastern University, Shenyang, China, 1996.

<!-- b000393 | references | pages [29] -->
[8] Chu, A.T.W.; Kalaba, R.E.; Spingarn, K. A comparison of two methods for de-

<!-- b000394 | references | pages [29] -->
termining the weights of belonging to fuzzy sets. J. Optimiz. Theor. App. 1979, 27,

<!-- b000395 | references | pages [29] -->
531–538.

<!-- b000396 | references | pages [29] -->
[9] Shannon, C.E. A mathematical theory of communication. Bell Syst. Tech. J. 1948,

<!-- b000397 | references | pages [29] -->
27, 379–423.

<!-- b000398 | furniture | pages [30] -->
Team #26636

<!-- b000399 | furniture | pages [30] -->
Page 29 of 38

<!-- b000400 | references | pages [30] -->
[10]Sun, L. J.; Xing, X. J.; Zhou, D. Q. Improvement of Entropy Method. Statistics and Deci-

<!-- b000401 | references | pages [30] -->
sion. J. 2010,21.

<!-- b000402 | references | pages [30] -->
[11]Lu, T. C.; Kang, K. The Application of Entropy method and AHP in determining the

<!-- b000403 | references | pages [30] -->
weights . Computer Programming Skills & Maintenance. J. 2009, 22.

<!-- b000404 | references | pages [30] -->
[12]Chen, X. The Application of fuzzy analytic hierarchy process in the preferred aspects of

<!-- b000405 | references | pages [30] -->
the program. Computer Engineering and Design. J. 2004, 10.

<!-- b000406 | heading | pages [30] -->
Appendix

<!-- b000407 | prose | pages [30] -->
Men’s basketball college coaches

<!-- b000408 | prose | pages [30] -->
a NCCAB Champions b Coach Awards NABC Coach of the Year c Basketball Times National Coach of the Year d e National coach of the year f AP national coach Henry iba awards g Coach Year h

<!-- b000409 | prose | pages [30, 31] -->
Name Year Wins Pct. a b c d e f g h Mike Krzyzewski 38 975 0.764 4 5 1 2 0 2 0 1976 Jim Boeheim 37 942 0.75 1 2 1 0 0 1 0 1977 Bob Knight 42 902 0.709 3 1 0 0 0 1 0 1966 Dean Smith 36 879 0.776 2 4 0 0 4 0 0 1962 Adolph Rupp 41 876 0.822 4 5 0 0 5 0 0 1931 Jim Calhoun 39 873 0.703 3 0 0 0 0 0 0 1973 Jim Phelan 49 830 0.613 1 1 0 0 1 0 0 1989 Eddie Sutton 37 804 0.71 0 2 0 0 0 2 0 1970 Lefty Driesell 41 786 0.666 1 0 0 0 0 0 0 1961 Lute Olson 34 780 0.736 1 1 0 0 1 0 0 1974 Lou Henson 41 779 0.654 0 0 0 0 0 0 0 1963 Henry Iba 41 764 0.693 2 0 0 0 0 0 0 1930 Edgar Diddle 42 759 0.715 0 0 0 0 0 0 0 1959 Phog Allen 48 746 0.739 1 0 0 0 0 0 0 1906 Jerry Tarkanian 31 729 0.784 1 0 0 0 0 0 0 1970 Norm Stewart 38 728 0.661 0 0 0 0 0 0 0 1968 Ray Meyer 42 724 0.672 1 3 1 0 0 2 0 1943 Don Haskins 38 719 0.671 1 0 0 0 0 0 0 1962 Bob Huggins 30 710 0.727 0 0 0 0 0 0 0 1985 Roy Williams 24 711 0.792 2 3 1 0 0 1 1 1989 Denny Crum 30 675 0.696 2 3 0 0 3 0 0 1972 Gary Williams 33 668 0.637 1 0 0 1 0 0 0 1979 John Wooden 29 664 0.804 10 7 0 0 7 0 0 1947 Rick Pitino 27 664 0.735 2 2 1 0 1 0 0 1979 Ralph Miller 38 657 0.632 0 2 0 0 2 0 0 1952 Mike Mont- gomery 31 656 0.684 0 2 1 0 1 0 0 1979 Cliff Ellis 37 647 0.611 0 0 0 0 0 0 0 1976

<!-- b000410 | furniture | pages [31] -->
Team #26636

<!-- b000411 | furniture | pages [31] -->
Page 30 of 38

<!-- b000413 | prose | pages [31] -->
Men’s football college coach

<!-- b000414 | prose | pages [31] -->
a NCCA Champions b Coach Awards c Bobby Dodd Coach of the Year Award d Walter Camp Coach of the Year Award e Amos Alonzo Stagg Award f AFCA Coach of the Year g Paul 'Bear' Bryant Award h George Munger Award i Home Depot Coach of the Year Award j Sporting News College Football Coach of the Year k Associated Press Coach of the Year l Joseph V. Paterno Award m National Coach of the Year

<!-- b000415 | prose | pages [31, 32] -->
a b c d e f g h i j k l m Name Years Wins Pct. Bowden, Bobby 44 377 0.743 22 3 1 1 1 0 0 0 0 0 0 0 0 Bryant, Bear 38 323 0.78 15 3 0 0 0 3 0 0 0 0 0 0 0 Warner, Glenn Scobey 49 319 0.733 4 1 0 0 1 0 0 0 0 0 0 0 0 Stagg, Amos Alonzo 57 314 0.605 2 1 0 0 0 1 0 0 0 0 0 0 0 Paterno, Joe 46 298 0.685 24 17 2 3 1 5 1 3 1 1 0 0 0 Beamer, Frank 33 266 0.666 9 7 1 1 0 1 1 1 0 0 1 1 0 Edwards, LaVell 29 257 0.716 7 3 1 0 1 1 0 0 0 0 0 0 0 Osborne, Tom 25 255 0.836 12 2 1 0 0 0 0 0 0 0 0 0 1 Holtz, Lou 33 249 0.651 12 5 0 1 0 0 2 0 0 2 0 0 0 Brown, Mack 30 244 0.666 13 2 1 1 0 0 0 0 0 0 0 0 0 Moore, Jerry 31 243 0.642 3 0 0 0 0 0 0 0 0 0 0 0 0 Hayes, Woody 33 238 0.759 5 4 0 1 1 1 0 0 0 1 0 0 0 Schembechler, Bo 27 234 0.804 5 4 1 1 1 1 0 0 0 0 0 0 0 Ault, Chris 28 233 0.681 2 0 0 0 0 0 0 0 0 0 0 0 0 Fry, Hayden 37 232 0.564 7 2 0 0 1 0 0 0 0 1 0 0 0 Tressel, Jim 25 229 0.742 6 12 12 0 0 0 0 0 0 0 0 0 0 Laycock, Jimmye 34 222 0.573 1 0 0 0 0 0 0 0 0 0 0 0 0 Spurrier, Ste- ve 24 219 0.733 9 0 0 0 0 0 0 0 0 0 0 0 0 Nehlen, Don 30 202 0.609 4 3 1 1 0 1 0 0 0 0 0 0 0 Dooley, Vince 25 201 0.715 8 5 1 1 1 1 0 0 0 1 0 0 0

<!-- b000416 | furniture | pages [32] -->
Team #26636

<!-- b000417 | furniture | pages [32] -->
Page 31 of 38

<!-- b000419 | prose | pages [32] -->
Men’s ice-hockey college coach

<!-- b000420 | prose | pages [32] -->
a NCAA Champions b Coach Awards c Lester Patrick Trophy(1966 起评) d Spencer Penrose national Coach of the Year(only for division one) e Jack Adams Award f NCAA Coach of the Year

<!-- b000421 | prose | pages [32, 33] -->
Name Years Wins Pct. a b c d e f Jerry York 40 935 0.61 5 2 1 1 0 0 Jack Parker 40 897 0.64 3 3 0 3 0 0 Red Berenson 30 770 0.66 2 2 0 1 1 0 Don Lucia 26 623 0.64 2 1 0 1 0 0 John "Snooks" Kelley 36 501 0.67 1 3 1 2 0 0 Ron Mason 36 924 0.7 0 1 0 1 0 0 Rick Comley 37 783 0.56 0 2 0 2 0 0 R.H. "Bob" Peters 36 744 0.7 2 0 0 0 0 0 Len Ceglarski 35 689 0.66 0 3 0 3 0 0 Jeff Sauer 31 655 0.55 2 0 0 0 0 0 John MacInnes 26 555 0.65 3 6 1 2 0 3 Don Brose 34 540 0.59 0 0 0 0 0 0 Dick Umile 23 519 0.64 0 0 0 0 0 0 John P. Riley, Jr. 36 542 0.61 0 0 0 0 0 0 Bruce Marshall 25 351 0.48 0 0 0 0 0 0 Murray Armstrong 21 460 0.67 0 2 1 1 0 0 Bill Wilkinson 26 437 0.48 0 0 0 0 0 0 Shawn Walsh 17 423 0.68 0 1 0 1 0 0 John Gasparini 17 407 0.6 0 0 0 0 0 0 Doug Woog 14 390 0.66 0 0 0 0 0 0 Amo Bessone 31 387 0.46 1 1 0 1 0 0 Ned Harkness 23 380 0.74 3 1 0 1 0 0 Jeff Jackson 14 367 0.68 2 1 0 1 0 0 Vic Heyliger 23 352 0.69 6 1 0 1 0 0 Bob Daniels 21 350 0.48 0 2 0 2 0 0 Mike McShane 32 633 0.65 0 0 0 0 0 0 George Gwozdecky 27 592 0.6 2 2 0 2 0 0 Joe Marsh 26 482 0.53 0 1 0 2 0 0 Doug Ross 27 457 0.6 0 0 0 0 0 0 Rick Gotkin 25 453 0.58 0 0 0 0 0 0 Mike Gilligan 25 407 0.54 0 0 0 0 0 0 Craig Dahl 24 407 0.5 0 0 0 0 0 0 Mike Sertich 21 375 0.49 0 1 0 1 0 0 Rand Pecknold 19 367 0.6 0 0 0 0 0 0 Bruce Marshall 25 351 0.48 0 0 0 0 0 0

<!-- b000422 | furniture | pages [33] -->
Team #26636

<!-- b000423 | furniture | pages [33] -->
Page 32 of 38

<!-- b000425 | prose | pages [33] -->
Woman’s basketball college coach

<!-- b000426 | prose | pages [33] -->
a NCAA Champions b Coach Awards c NCAA Coach of the Year d Naismith Coach of the 20th Century e NAIA

<!-- b000427 | prose | pages [33, 34] -->
Name Year Wins Pct. a b c d e Pat Summitt 38 1098 0.841 8 8 7 1 0 C.Vivian Stringer 42 916 0.732 0 0 0 0 0 Tara VanDerveer 34 910 0.817 2 4 4 0 0 Sylvia Hatchell 38 908 0.739 1 3 2 0 1 Barbara Stevens 36 900 0.785 0 0 0 0 0 Jody Conradt 38 900 0.744 2 6 6 0 0 Debbie Ryan 34 739 0.695 1 1 0 1 0 Kay Yow 38 737 0.682 0 0 0 0 0 Sue Gunter 34 708 0.697 0 0 0 0 0 Muffet McGraw 31 714 0.735 1 1 0 1 0 Amy Ruley 29 671 0.772 5 0 0 0 0 Theresa Grentz 33 671 0.683 0 0 0 0 0 Nancy Fahey 27 639 0.844 5 0 0 0 0

<!-- b000428 | furniture | pages [34] -->
Team #26636

<!-- b000429 | furniture | pages [34] -->
Page 33 of 38

<!-- b000431 | prose | pages [34] -->
Program

<!-- b000432 | prose | pages [34] -->
1)Apply Fuzzy Consistent Matrix to determine weight

<!-- b000433 | prose | pages [34] -->
A=[0.5 0 0 1 1 0.5 0 1 1 1 0.5 1 0 0 0 0.5]

<!-- b000434 | prose | pages [34] -->
c=sum(A,2); b=sum(A); m=c(1,:)+b(:,1); for i=1:4 for j=1:4 r(i,j)=(c(i,:)-c(j,:))/(2*m)+0.5; end end

<!-- b000435 | prose | pages [34] -->
d=sum(r); for j=1:4 for i=1:4 s(i,j)=r(i,j)/d(:,j); end end

<!-- b000436 | prose | pages [34] -->
k=power(prod(s,2),1/4);

<!-- b000437 | prose | pages [34] -->
for i=1:4 w(i,:)=k(i,:)/sum(k); end w=w’

<!-- b000438 | prose | pages [34] -->
2)Apply Entropy Method to determine weight

<!-- b000439 | prose | pages [34] -->
x=xlsread('E:\2014 美赛\B 题\数据\basketball.xls'); x=x'; k=mean(x,1) t=sum(x) s3=0; s4=0;

<!-- b000440 | furniture | pages [35] -->
Team #26636

<!-- b000441 | furniture | pages [35] -->
Page 34 of 38

<!-- b000442 | prose | pages [35] -->
for i=1:27 a3=(x(i,3)-k(3))^2; s3=s3+a3; end d3=1/(sqrt(s3)) c3=t(:,3)/(sqrt(s3))

<!-- b000443 | prose | pages [35] -->
for i=1:27 a4=(x(i,4)-k(4))^2; s4=s4+a4; end d4=1/(sqrt(s4)) c4=t(:,4)/(sqrt(s4)) y=[] [m,n]=size(x); for i=1:n y(:,i)=x(:,i)/sum([x(:,i)]); end

<!-- b000444 | prose | pages [35] -->
for i=1:27 y(i,3)=y(i,3)*d3+c3; y(i,4)=y(i,4)*d4+c4; end

<!-- b000445 | prose | pages [35] -->
for i=1:n y(:,i)=x(:,i)/sum([x(:,i)])+1; end

<!-- b000446 | prose | pages [35] -->
for l=1:n s(1,l)=0; for j=1:m p(1,l)=y(j,l)*log(y(j,l)) s(1,l)=s(1,l)+p(1,l) end end k=(log(m))^(-1) e=-k*s h=ones(1,n)-e w=h/(n-sum(h)) w=w/sum(w,2)

<!-- b000447 | prose | pages [35, 36] -->
3)Total model Weight and calculate grey relational degree A=[0.5 0 0 1 1 0.5 0 1 1 1 0.5 1 0 0 0 0.5]

<!-- b000448 | furniture | pages [36] -->
Team #26636

<!-- b000449 | furniture | pages [36] -->
Page 35 of 38

<!-- b000451 | prose | pages [36] -->
c=sum(A,2); b=sum(A); m=c(1,:)+b(:,1); for i=1:4 for j=1:4 r(i,j)=(c(i,:)-c(j,:))/(2*m)+0.5; end end

<!-- b000452 | prose | pages [36] -->
d=sum(r); for j=1:4 for i=1:4 s(i,j)=r(i,j)/d(:,j); end end

<!-- b000453 | prose | pages [36] -->
k=power(prod(s,2),1/4); for i=1:4 w(i,:)=k(i,:)/sum(k); end w=w';

<!-- b000454 | prose | pages [36] -->
a=xlsread('E:\2014 美赛\B 题\数据\basketball.xls'); for i=1:4 a(i,:)=(a(i,:)-min(a(i,:)))/(max(a(i,:))-min(a(i,:))); end [m,n]=size(a); cankao=max(a')' t=repmat(cankao,[1,n])-a; mmin=min(min(t)); mmax=max(max(t)); rho=0.5; xishu=(mmin+rho*mmax)./(t+rho*mmax); correlation=w*xishu

<!-- b000455 | prose | pages [36, 37] -->
xlswrite('C:\Users\Administrator\Desktop\correlation.xls',correlation) An article for Sports Illustrated

<!-- b000456 | furniture | pages [37] -->
Team #26636

<!-- b000457 | furniture | pages [37] -->
Page 36 of 38

<!-- b000459 | prose | pages [37] -->
The best all-time college coaches

<!-- b000460 | prose | pages [37] -->
College coaches are critical to the performance of their teams. As the heat of National College Athletic Association Championships spreads throughout the country, the coaches that have led their teams to win a considerable number of trophies become the legends among sports fans. Who is your favorite college coach?

<!-- b000461 | prose | pages [37] -->
May be he is John Wooden, the legend on basketball court, who won the most amount of NCAA champions?

<!-- b000462 | prose | pages [37] -->
May be he is “Bear” Bryant, the hero in the field of football ,who held the record for most wins as head coach when he retired as a coach in 1982?

<!-- b000463 | prose | pages [37] -->
May be she is Pat Summitt, the most successful woman basketball coach, who hold the most all-time wins in NCAA basketball history above 1000 victories?

<!-- b000464 | prose | pages [37] -->
We know that you are tired of the endless debate on your choice of the best all-time coaches. Thus we build a quantitative evaluation system to rank the college coaches of all time. The results are just in! Check whether your favorite college coach is among the top!

<!-- b000465 | prose | pages [37, 38] -->
Top 5 College Men’s Basketball Coaches 1. John Wooden 2. Adolph Rupp 3. Mike Krzyzewski 4. Dean Smith 5. Jim Boeheim Top 5 College Men’s Football Coaches 1. Bear Bryant 2. Jim Tressel 3. Tom Osborne 4. Bobby Bowden 5. Woody Hayes

<!-- b000466 | furniture | pages [38] -->
Team #26636

<!-- b000467 | furniture | pages [38] -->
Page 37 of 38

<!-- b000469 | prose | pages [38] -->
Top 5 College Men’s Ice Hockey Coaches 1. Jerry York 2. Vic Heyliger 3. Jack Parker 4. Ron Mason 5. Ned Harkness

<!-- b000470 | prose | pages [38] -->
In our evaluation system, we select four indicators to assess the performance of coaches: The times that they lead their teams to win NCAA championships, the win- ning percentage, the times of victory throughout their coaching career, and the times they win the title of Coach of the Year. We use appropriate method to determine the weight of each factor, and then use mathematical model to rank all the coaches.

<!-- b000471 | prose | pages [38] -->
One of the advantages of this model is that it eliminates the arbitrariness of human judgment. We know that most of media use online-voting system to collect data and rank the coaches, which is not convincible. Instead of that, we obtain the data of all college coaches from NCAA database, and use mathematical model to determine which indicator is more important.

<!-- b000472 | prose | pages [38] -->
Another advantage is that our model is universally applicable. We can apply this model across both genders and various kinds of sports.

<!-- b000473 | prose | pages [38] -->
The function of our model might be limited, but your enthusiasm of sports is unlim- ited!
