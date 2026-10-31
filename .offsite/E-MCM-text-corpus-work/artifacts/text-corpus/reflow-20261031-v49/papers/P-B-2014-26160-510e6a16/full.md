# P-B-2014-26160-510e6a16

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Team Control Number

<!-- b000002 | front_matter | pages [1] -->
For office use only For office use only

<!-- b000003 | front_matter | pages [1] -->
26160

<!-- b000004 | front_matter | pages [1] -->
T1 ________________ F1 ________________ T2 ________________ F2 ________________ T3 ________________ Problem Chosen F3 ________________ T4 ________________ F4 ________________

<!-- b000005 | front_matter | pages [1] -->
B

<!-- b000006 | heading | pages [1] -->
Summary

<!-- b000007 | prose | pages [1] -->
Aimed to look for the “best all time college coach” for the previous century, we employ methods in grey and fuzzy fields to build an evaluation model and give out coach ranks in various sports fields by massive calculating. Meanwhile, effects of gender and time criterion on evaluation are also considered.

<!-- b000008 | prose | pages [1] -->
In order to simplify our model, we firstly adopt AHP to filter factors and determine seven most influential criterion, including coaching time, gender, etc. With the weight of each criteria worked out, the abstract problem is transferred to a mathematic one.

<!-- b000009 | prose | pages [1] -->
Based on AHP Model, two advanced models are proposed to rank college coaches. Grey Correlation Model considers the relevance among evaluation criterion and evaluates all coaches by calculating correlation degree with respect to reference data series. Fuzzy Comprehensive Model integrates empirical formulas and membership function to get the membership matrix, through which we can figure out scores of each coach. Comparing two results with current ranks, we find that grey model has slight advantages over fuzzy model.

<!-- b000010 | prose | pages [1] -->
Considering time line horizon’s impact on evaluating results, we augment our model by revising the weights and re-rank, based on membership function. According to the comparison between former rank and the one considering time line horizon, we conclude that it has fewer effects on the top 10 college coaches while has more effects on those ranked behind. The final rank table is as follows:

<!-- b000011 | prose | pages [1] -->
Rank Basketball Field hockey Football

<!-- b000012 | prose | pages [1] -->
1 Harry Statham Jan Hutchinson Joe Paterno 2 Danny Miles Jan Trapp Bobby Bowden 3 Herb Magee Nancy Stevens Bear Bryant 4 Mike Krzyzewski Sharon Pfluger Lou Holtz 5 Bob Knight Pat Rudy Pop Warner

<!-- b000013 | prose | pages [1] -->
Our paper considers multiple factors, employs several models and does plenty of calculations, which makes the ranks more reliable and brings the evaluation model broader applicability. In conclusion, our model successfully achieves our goals that selecting the best college coaches in various sports.

<!-- b000014 | keywords | pages [1] -->
Keywords:  AHP  Grey Correlation Model  Fuzzy Comprehensive Model  final rank

<!-- b000015 | furniture | pages [2] -->
Team #26160                                                             Page 1 of 35

<!-- b000016 | heading | pages [2] -->
Contents

<!-- b000017 | contents | pages [2] -->
1 Introduction ............................................................................................................... 2

<!-- b000018 | contents | pages [2] -->
2 Assumption ................................................................................................................ 3

<!-- b000019 | contents | pages [2] -->
3 Symbols Definition .................................................................................................... 3

<!-- b000020 | contents | pages [2] -->
4 Model Overview ........................................................................................................ 4

<!-- b000021 | contents | pages [2] -->
5 AHP Model ................................................................................................................. 4

<!-- b000022 | contents | pages [2] -->
5.1 Establish a Hierarchical Model ........................................................................ 5

<!-- b000023 | contents | pages [2] -->
5.2 Structure Comparison Matrix .......................................................................... 6

<!-- b000024 | contents | pages [2] -->
5.2.1 Weights of Evaluation Criterion ........................................................... 6

<!-- b000025 | contents | pages [2] -->
5.2.2 Select Evaluation Criterion ................................................................... 8

<!-- b000026 | contents | pages [2] -->
5.3 Explanations about the Seven Criterion ........................................................... 8

<!-- b000027 | contents | pages [2] -->
6 Advanced Model ........................................................................................................ 9

<!-- b000028 | contents | pages [2] -->
6.1 Overview of Evaluation Methods .................................................................... 9

<!-- b000029 | contents | pages [2] -->
6.2 Grey Correlation Model ................................................................................. 10

<!-- b000030 | contents | pages [2] -->
6.2.1 Data Processing ................................................................................... 10

<!-- b000031 | contents | pages [2] -->
6.2.2 Grey Correlation Evaluation Model .................................................... 11

<!-- b000032 | contents | pages [2] -->
6.2.3 Results of Grey Correlation Model ..................................................... 12

<!-- b000033 | contents | pages [2] -->
6.3 Fuzzy Comprehensive Evaluation Model ...................................................... 15

<!-- b000034 | contents | pages [2] -->
6.3.1 Introduction of Fuzzy Comprehensive Algorithm .............................. 15

<!-- b000035 | contents | pages [2] -->
6.3.2 Concrete Calculation ........................................................................... 17

<!-- b000036 | contents | pages [2] -->
6.4 Results Review............................................................................................... 21

<!-- b000037 | contents | pages [2] -->
7 Is Time Line Horizon Influential? ......................................................................... 22

<!-- b000038 | contents | pages [2] -->
8 Sensitivity Analysis.................................................................................................. 24

<!-- b000039 | contents | pages [2] -->
8.1 Sensitivity of Grey Correlation Method ........................................................ 24

<!-- b000040 | contents | pages [2] -->
8.2 Sensitivity of Fuzzy Comprehensive Method ................................................ 25

<!-- b000041 | contents | pages [2] -->
9 Discussion and Conclusion ..................................................................................... 26

<!-- b000042 | contents | pages [2] -->
9.1 Solutions to All Problems .............................................................................. 26

<!-- b000043 | contents | pages [2] -->
9.2 Honor Roll ..................................................................................................... 27

<!-- b000044 | contents | pages [2] -->
9.3 Strengths and Weaknesses ............................................................................. 28

<!-- b000045 | contents | pages [2] -->
9.4 Conclusion ..................................................................................................... 28

<!-- b000046 | contents | pages [2] -->
A Letter to Sports Illustrated ..................................................................................... 29

<!-- b000047 | contents | pages [2] -->
Reference .................................................................................................................... 30

<!-- b000048 | contents | pages [2] -->
Appendix ..................................................................................................................... 31

<!-- b000049 | furniture | pages [3] -->
Team #26160                                                             Page 2 of 35

<!-- b000050 | heading | pages [3] -->
1 Introduction

<!-- b000051 | prose | pages [3] -->
The quality of coaches is becoming critical to raise the level of scientific training of competitive sports. A fair and convincing method to evaluate college coaches is demanded. Plenty of researches are made and a number of notable papers are addressed to get a reasonable evaluation method.

<!-- b000052 | prose | pages [3] -->
MacLean and Chelladurai (1995) proposed a framework for performance evaluation of college coaches. Performance of coaches should be evaluated from two respects, the process of work behavior and the results of work behavior. It is unfair and not convincing to evaluate college coaches only by the result of work behavior. They believe factors of process of work behavior consist of straightforward task behavior, indirect task behavior, daily management behavior and public relations behavior. These factors mainly depend on college coaches’ ability to raise the level of sports teams. George B.Cunningham and Marlene A.Dixion (2003) considered that good results coming from the joint efforts of athletes, coaches and sports teams. Both results and process of sports team should be considered. Based on the consideration, they proposed evaluation theory in multidimensional performance.

<!-- b000053 | prose | pages [3] -->
Despite the evaluation method of college coaches has been studied to different extent with different approaches, the researchers’ work usually focus on special sport. Meanwhile, their evaluation don’t consider the effect of time. Therefore, their research may not appropriate to solve the proposed problems. We need to develop a model to look for the “best all time college coach”. What’s more, the model should be problem-oriented.

<!-- b000054 | prose | pages [3] -->
The three proposed problems are:  Develop a model to look for the best all time college coach for the previous century.  Analyze whether it make a difference with time line horizon or not.  Present top 5 college coaches in each of 3 different sports.

<!-- b000055 | prose | pages [3] -->
Meanwhile, the problems request that model should take gender into consideration and have a broader applicability in all possible sports.

<!-- b000056 | prose | pages [3] -->
A reasonable evaluation method should consider many necessary factors. To classify factors appropriately, we apply Analytic Hierarchy Process (AHP) to the problem. Then, we get the weight of several main factors. To evaluate college coaches scientifically, we propose two models based on Grey Correlation Algorithm and Fuzzy Comprehensive Evaluation Algorithm. Then we make a comparison between results of two models. Furthermore, we optimize our model by considering the effect of time line horizon. At last, a non-technical explanation letter for sports fans is written to the Sports Illustrated magazine.

<!-- b000057 | furniture | pages [4] -->
Team #26160                                                             Page 3 of 35

<!-- b000058 | heading | pages [4] -->
2 Assumption

<!-- b000059 | prose | pages [4] -->
1. Assume that personal quality, training quality and team achievements can perfectly reflect college coaches’ comprehensive impact. 2. Assume that coaching time and gender can perfectly represent college coaches’ personal quality. Organizational capability, management capability and race command capability can perfectly represent college coaches’ training quality.

<!-- b000060 | prose | pages [4] -->
Wins, losses, win-loss percentage and performance in league matches can perfectly represent college coaches’ team achievements. 3. Assume that continuous wins and the difference of competitors’ strength have few effects on rank. 4. The data we used and reference ranks are believable.

<!-- b000061 | heading | pages [4] -->
3 Symbols Definition

<!-- b000062 | heading | pages [4] -->
Symbol

<!-- b000063 | prose | pages [4] -->
Explanation

<!-- b000064 | prose | pages [4] -->
A The sequence of college coach

<!-- b000065 | prose | pages [4] -->
B Second level criterion

<!-- b000066 | prose | pages [4] -->
C Third level criterion

<!-- b000067 | prose | pages [4] -->
Z Total score

<!-- b000068 | prose | pages [4] -->
R Correlation degree

<!-- b000069 | prose | pages [4] -->
D Membership degree

<!-- b000070 | prose | pages [4] -->
T Start coaching time

<!-- b000071 | furniture | pages [5] -->
Team #26160                                                             Page 4 of 35

<!-- b000072 | heading | pages [5] -->
4 Model Overview

<!-- b000073 | prose | pages [5] -->
The process of developing models is shown in Figure 1.

<!-- b000074 | caption | pages [5] -->
Figure 1. Flow diagram of solution

<!-- b000075 | prose | pages [5] -->
To determine the best all time college coach (past or present) from among either male or female coaches in some sports, we have to know what criterion should be used to evaluate college coaches. As is shown in the problem, we search the predecessors' research and find that many of them are qualitative analysis. What’s more, according to some research there exist more than 54 of the evaluation criterion, such as the coach working age, the professional ethics, the ability to communicate with players, management ability statistics and so on. Some evaluation criterion are meaningful, but some of them are of little impact. We must find some methods to process the data in order to distill the crucial criterion.

<!-- b000076 | prose | pages [5] -->
How we could select the most important ones from 54 initial criterion and process scientifically to make them more useful in evaluating quality is a key problem. However, how to accomplish this goal? The Main Components Analysis method and Analytic Hierarchy Process will be helpful for us to devise our first model.

<!-- b000077 | prose | pages [5, 6] -->
Combining the key evaluation criterion with the real data from internet, we select coaches in different sports as model evaluation objects and evaluate them with two different algorithms respectively, that is Grey Correlation Algorithm and Fuzzy Evaluation Algorithm. Grey Correlation Model considers the relevance among evaluation criterion and grades all coaches by calculating correlation degree to reference data. Fuzzy Comprehensive Model integrates empirical formulas and membership function to get the membership matrix, through which we can figure out scores of each coach. Furthermore, we compare the two algorithm and corresponding results and transplant the model to other sports field for evaluating.

<!-- b000078 | furniture | pages [6] -->
Team #26160                                                             Page 5 of 35

<!-- b000080 | prose | pages [6] -->
We choose college filed hockey, basketball, football sport coaches as examples, and get the rank of the coaches respectively.

<!-- b000081 | heading | pages [6] -->
5 AHP Model

<!-- b000082 | heading | pages [6] -->
5.1 Establish a Hierarchical Model

<!-- b000083 | prose | pages [6] -->
MacLean and Chelladurai (1995) thought that evaluation criterion of college coaches should include the process of work behavior and the results of work behavior. Patricia (2005) proposed that different principles should be considered to establish a kind of fair and convincing criterion to evaluate college coaches. With the help of the current literatures, we develop AHP model considering three main factors, these are coaches’ personal quality, training quality and team achievements.

<!-- b000084 | prose | pages [6] -->
Personal quality Coaches’ personal quality consist of coaching time and gender [Yuanming Li, 2009]. College coaches consist of both male and female, we should consider both of them. Coaching time could reflect coaches’ time consumption on their jobs.  Coaching time  Gender

<!-- b000085 | prose | pages [6] -->
Training quality Yu Zhang (2010) proposed the components of training quality in his paper. He thought that training quality should consist of organizational capability, management capability and race command capability. Training quality represent a significant component of the evaluation criterion.  Organizational capability  Management capability  Race command capability

<!-- b000086 | prose | pages [6, 7] -->
Team achievements Team achievements are the results of coaches’ works, they are obvious to reflect coaches’ capability. Meanwhile, people pay more attention to team achievements compared with other factors. However, fair and convincing evaluation criterion should be considered general factors rather than only results.  Wins  Losses  Win-loss percentage  Performance in league matches Through above analysis of three main factors, which affect evaluation significantly, hierarchy figure is shown in Figure 2.

<!-- b000087 | furniture | pages [7] -->
Team #26160                                                             Page 6 of 35

<!-- b000089 | prose | pages [7] -->
Comprehensive impact

<!-- b000090 | prose | pages [7] -->
Team Personal Training achievements qualities qualities

<!-- b000091 | prose | pages [7] -->
Gender C-Time Wins Losses W-L Perfomance OC MC RCC

<!-- b000092 | caption | pages [7] -->
Figure 2. Hierarchy figure

<!-- b000093 | prose | pages [7] -->
In Figure 2, C-Time represents Coaching Time. W-L represents Win-Loss Percentage, OC represent Organization Capability, MC represent Management capability, RCC represent Race Command Capability.

<!-- b000094 | heading | pages [7] -->
5.2 Structure Comparison Matrix

<!-- b000095 | heading | pages [7] -->
5.2.1 Weights of Evaluation Criterion

<!-- b000096 | prose | pages [7] -->
Starting from the second criteria of the above hierarchy figure, we structure comparison matrix by Comparison Method of 1-9. Then, we get the weights of personal quality, training quality and team achievements as is shown in Table 1.

<!-- b000097 | caption | pages [7] -->
Table 1. Pairwise comparison matrix of hierarchyⅠ-Ⅱ

<!-- b000098 | prose | pages [7] -->
Comprehensive Personal Training Team Weight impact quality quality achievements Personal quality 1 3 1/5 0.2496 Training quality 1/3 1 1/8 0.1565 Team achievements 5 8 1 0.5938

<!-- b000099 | prose | pages [7] -->
Through calculating the weights of three factors in hierarchyⅡ, we get the  3.0044 maximum eigenvalue is ，consistency ratio is 0.0043.

<!-- b000100 | caption | pages [7] -->
Table 2. Pairwise comparison matrix of hierarchyⅡ-Ⅲ

<!-- b000101 | prose | pages [7] -->
Personal quality Coaching time Gender Weight

<!-- b000102 | prose | pages [7] -->
Coaching time 1 2 0.5498

<!-- b000103 | prose | pages [7] -->
Gender 1/2 1 0.4502

<!-- b000104 | prose | pages [7] -->
Through calculating the weights of two factors of personal quality in hierarchy  2.0000 Ⅲ, we get the maximum eigenvalue is ，consistency ratio is 0.2496.

<!-- b000105 | furniture | pages [8] -->
Team #26160                                                             Page 7 of 35

<!-- b000106 | caption | pages [8] -->
Table 3. Pairwise comparison matrix of hierarchyⅡ-Ⅲ

<!-- b000107 | prose | pages [8] -->
Training Organizational Management Race command Weight quality capability capability capability Organizational 1 2 1/5 0.2473 capability Management 1/2 1 1/6 0.2024 capability Race command 5 6 1 0.5503 capability

<!-- b000108 | prose | pages [8] -->
Through calculating the weight of two factors of training quality in hierarchyⅢ,  3.0000 we get the maximum eigenvalue is ，consistency ratio is 0.0001.

<!-- b000109 | caption | pages [8] -->
Table 4. Pairwise comparison matrix of hierarchyⅡ-Ⅲ

<!-- b000110 | prose | pages [8] -->
Team Win-loss Performance in Wins Losses Weight achievements percentage league matches

<!-- b000111 | prose | pages [8] -->
C 1 5 1/3 4 0.2853 6

<!-- b000112 | prose | pages [8] -->
Losses 1/5 1 1/8 1/3 0.1160

<!-- b000113 | prose | pages [8] -->
Win-loss 3 8 1 5 0.4256 percentage Performance in 1/4 3 1/5 1 0.1731 league matches

<!-- b000114 | prose | pages [8] -->
Through calculating the weights of two factors of team achievements in  4.0100 hierarchyⅢ, we get the maximum eigenvalue is ，consistency ratio is 0.0037.

<!-- b000115 | prose | pages [8] -->
From above tables, we know that all Consistency Test is right. Combination Weight Vector of criterion with respect to evaluation method of college coaches is shown in Table 5. They can used to evaluate college coaches.

<!-- b000116 | caption | pages [8] -->
Table 5. Criterion’s weights to overall objects

<!-- b000117 | prose | pages [8] -->
Criterion Weight Coaching time 0.1373 Gender 0.1124 Organizational capability 0.0387 Management capability 0.0317 Race command capability 0.0861 Wins 0.1694 Losses 0.0689 Win-loss percentage 0.2528 Performance in league matches 0.1028

<!-- b000118 | furniture | pages [9] -->
Team #26160                                                             Page 8 of 35

<!-- b000119 | heading | pages [9] -->
5.2.2 Select Evaluation Criterion

<!-- b000120 | prose | pages [9] -->
According to importance of every criteria shown in Table 5, we choose several main criterion and decide the final evaluation method. Despite organizational capability and management capability have close relationship with evaluation method in theory. However, from above tables we can find their weights are light. Meanwhile, we lack of quantitative data of them. Therefore, we don’t consider them. The final seven criterion are shown in Table 6.

<!-- b000121 | caption | pages [9] -->
Table 6. Final seven criterion to evaluate college coaches

<!-- b000122 | prose | pages [9] -->
Criterion

<!-- b000123 | heading | pages [9] -->
Symbol

<!-- b000124 | prose | pages [9] -->
Weight

<!-- b000125 | prose | pages [9] -->
C Coaching time ★★★☆☆ 1 C Gender ★★☆☆☆ 2 C Race command capability ★★☆☆☆ 3 C Wins ★★★☆☆ 4 C Losses ★☆☆☆☆ 5 C Win-loss percentage ★★★★★ 6 C Performance in league matches ★★☆☆☆ 7

<!-- b000126 | heading | pages [9] -->
5.3 Explanations about the Seven Criterion

<!-- b000127 | prose | pages [9] -->
In the seven criterion we got, only Losses is the negative criterion, others are positive.

<!-- b000128 | prose | pages [9] -->
Data of performance in league matches Different sports are different in rules and league schedule. Therefore, different sports have different measuring values with respect to the performance in league matches. Based on data, we evaluate performance in league matches of basketball by number of NCAA final four appearances, evaluate performance in league matches of football by the times ranked into top 4, evaluate performance in league matches of college filed hockey by the times ranked into top 4.

<!-- b000129 | prose | pages [9] -->
Data of gender Considering the disadvantage of female, we define value of male as 1, while female as 3. There are three reasonable explanation:  Female have physiological disadvantages in sports.  Once female are banned to participate sports for a long time. This tradition lasted a long time. Therefore, the tradition may have effects on female now.  Male have better force and velocity on sports, so they can draw more attention compared with female. What’s more, the quantity of male athletes is well larger than female, male athlete prefer male coaches.

<!-- b000130 | furniture | pages [10] -->
Team #26160                                                             Page 9 of 35

<!-- b000131 | heading | pages [10] -->
6 Advanced Model

<!-- b000132 | heading | pages [10] -->
6.1 Overview of Evaluation Methods

<!-- b000133 | prose | pages [10] -->
Through AHP algorithm, we get the weights of final seven criterion to evaluate college coaches. To establish a fair and convincing evaluation method and rank the college coaches for the previous century, we proposed Grey Correlation Model and Fuzzy Comprehensive Evaluation Model.

<!-- b000134 | heading | pages [10] -->
 Grey Correlation Model

<!-- b000135 | prose | pages [10] -->
Criterion selected by AHP have inner links with each other. And Grey Correlation Model could take the links into consideration and solve the problem of comprehensive evaluation. First normalize the real data of every coach. Then determine the reference data, which is to be regarded as ideal standard. Find the relationship between every evaluated object and reference data series and finally build the comprehensive evaluation model. From this model, we calculate all coaches’ scores and rank them. Top 5 coaches in basketball, field hockey and football are represented as:

<!-- b000136 | prose | pages [10] -->
Rank Basketball Field hockey Football

<!-- b000137 | prose | pages [10] -->
1 Harry Statham Jan Hutchinson Joe Paterno 2 Danny Miles Jan Trapp Bobby Bowden 3 Herb Magee Nancy Stevens Bear Bryant 4 Mike Krzyzewski Sharon Pfluger Lou Holtz 5 Bob Knight Pat Rudy Pop Warner

<!-- b000138 | heading | pages [10] -->
 Fuzzy Comprehensive Evaluation Model

<!-- b000139 | prose | pages [10] -->
There we use multi-level fuzzy comprehensive evaluation model to rank the coaches. Normally, the first step is formulating evaluation criterion. Then determine the evaluation objects and the comment set. Next confirm the membership function and membership degree, through which we get formula of fuzzy evaluation matrix. According to evaluation matrix and weights determined by AHP method, we give a comprehensive evaluation of coaches.

<!-- b000140 | prose | pages [10] -->
From this model, we calculate all coaches’ scores and rank them. Top 5 coaches in basketball, field hockey and football are represented as:

<!-- b000141 | prose | pages [10] -->
Rank Basketball Field hockey Football

<!-- b000142 | prose | pages [10] -->
1 Harry Statham Jan Hutchinson Bobby Bowden 2 Herb Magee Jan Trapp Joe Paterno 3 Danny Miles Nancy Stevens Bear Bryant 4 Adolph Rupp Pat Rudy Tom Osborne 5 Mike Krzyzewski Beth Anders Pop Warner

<!-- b000143 | furniture | pages [11] -->
Team #26160                                                             Page 10 of 35

<!-- b000144 | heading | pages [11] -->
6.2 Grey Correlation Model

<!-- b000145 | heading | pages [11] -->
6.2.1 Data Processing

<!-- b000146 | prose | pages [11] -->
Based on the current evaluation criterion, we collect related data of college coaches. Assume that data sequence of n coaches form the following matrix iA , the data after ' (Equation 6.1). To simplify calculation, we note original data as iA . dimensionless process is noted as      a (1) a (1) a (1) 1 2 n      a (2) a (2) a (2)   1 2 n    ( A A , , , A ) （6.1） 1 2 n       a m ( ) a m ( ) a m ( )   1 2 n

<!-- b000147 | prose | pages [11] -->
    T   A ( (1) , a a (2) , , a m ( )) , i 1,2, , n i i i i

<!-- b000148 | prose | pages [11] -->
In which, m presents the number of metrics, herein, m=7. Based on evaluation and rank of college coaches provided by Wikipedia and other websites, considering several quality of college coaches generally, we choose about 100 coaches of three sports (basketball, football and college filed hockey) as evaluated objects.

<!-- b000149 | prose | pages [11] -->
Then, taking basketball for example, we analyze and dimensionless process data.

<!-- b000150 | prose | pages [11] -->
We choose 46 college coaches whose achievements are comparatively prominent. Process theirs’ data and rank them. Here we just present top 10 of them, who are Harry Statham, Mike Krzyzewski, etc. [http://www.sports-reference.com/cbb/coaches/] 1A， A， A. The data are represented respectively as ， 2 10   47 1 39 1079 444 0.708 13   42 1 32 1000 409 0.710 10     45 1 26 976 391 0.714 11   39 1 29 975 302 0.764 11        ( A A , , , A ) 38 1 30 942 314 0.750 4 1 2 n  42 1 28 899 374 0.706 5     36 1 27 879 254 0.776 11    40 1 23 877 382 0.697 4    41 1 20 876 190 0.822 6  Because dimensions of every criteria are different, we normalize every criteria, transfer the absolute value to relative value. For positive (negative) criterion, we normalize data with different algorithms.  Positive criterion:

<!-- b000151 | prose | pages [11] -->
          A j ( ) ( A j ( ) A j ( ) ) / ( A j ( ) A j ( ) ) 100% i i i min i max i min  Negative criterion:

<!-- b000152 | prose | pages [11, 12] -->
          A j ( ) ( A j ( ) A j ( )) / ( A j ( ) A j ( ) ) 100% i max i i max i min In which, i represents the sequence of countries, j represents the sequence of  iA j ( ) iA j represents ( ) metrics; represents maximum value of the jth metrics, min normalized value of the jth metrics of the ith coach. Then, we get the normalized value of every criterion of 10 basketball coaches.

<!-- b000153 | furniture | pages [12] -->
Team #26160                                                             Page 11 of 35

<!-- b000155 | caption | pages [12] -->
Table 7. Standardization of basketball college coaches

<!-- b000156 | prose | pages [12] -->
Coach CT Gender RCC Wins Losses W/L% FF Harry Statham 0.963 0.000 1.000 1.000 1.000 0.619 1.000 Danny Miles 0.778 0.000 0.816 0.912 0.876 0.625 0.769 Herb Magee 0.889 0.000 0.658 0.884 0.812 0.639 0.846 Mike Krzyzewski 0.667 0.000 0.737 0.883 0.496 0.806 0.846 Jim Boeheim 0.630 0.000 0.763 0.845 0.539 0.759 0.308 Bob Knight 0.778 0.000 0.711 0.795 0.752 0.612 0.385 Dean Smith 0.556 0.000 0.684 0.772 0.326 0.846 0.846 Jim Calhoun 0.704 0.000 0.579 0.770 0.780 0.582 0.308 Adolph Rupp 0.741 0.000 0.500 0.769 0.099 1.000 0.462 Eddie Sutton 0.593 0.000 0.658 0.688 0.592 0.625 0.231 In the table:

<!-- b000157 | prose | pages [12] -->
CT--Coaching time RCC--Race command capability FF—number of NCAA final four appearance

<!-- b000158 | prose | pages [12] -->
Similarly, we can get the normalized value of every criterion of 10 football coaches and college filed hockey coaches.

<!-- b000159 | heading | pages [12] -->
6.2.2 Grey Correlation Evaluation Model

<!-- b000160 | prose | pages [12] -->
Because of the relationship between every criterion and total evaluation is sophisticated and interacting, we develop Grey Correlation Evaluation Model to analyze and evaluate general capability of college coaches. Grey Correlation Evaluation Method is branch of Grey Theory, the method are usually used to evaluate interacting factors.

<!-- b000161 | prose | pages [12] -->
We use the Grey Correlation Analysis to evaluate college coaches, the steps are shown as following: STEP 1  Note reference data series as ideal comparison criteria. In generally, reference data series consist of the optimal value of every metrics, we can also choose other reference data by different evaluation destination. The relationship is shown in following equation:

<!-- b000162 | prose | pages [12] -->
 A ( a (1) , a (2) , , a m ( )) 0 0 0 0

<!-- b000163 | prose | pages [12, 13] -->
In which, we choose every optimal value as reference data series, that is A  (1,1, ,1) . 0 STEP 2   Calculate the absolute difference between comparison series and reference    data series of every evaluated objects. That is . In which, i ( ) j a ( ) j a ( ) j i i 0  i 1,2, , n represents the sequence of college coaches, ; j represents the sequence of  a 0( ) j represents the reference data of the jth j 1,2, , m evaluation criterion, ; evaluation criterion.

<!-- b000164 | furniture | pages [13] -->
Team #26160                                                             Page 12 of 35

<!-- b000166 | prose | pages [13] -->
STEP 3   determine the value of p and q.

<!-- b000167 | prose | pages [13] -->
    p min min ( ) j i   1 i n 1 j m     q max max ( ) j i   1 i n 1 j m

<!-- b000168 | prose | pages [13] -->
STEP 4   According to Equation 6.2. , We can calculate correlation coefficient with respect to every comparison series and reference data series.

<!-- b000169 | prose | pages [13] -->
  ( p q )   y ( ) j j 1,2, m （6.2） i    ( ( ) j q ) i

<!-- b000170 | prose | pages [13] -->
 (0,1) In which, resolution ratio , the difference of correlation coefficient increase with decreasing. Herein, we choose  0.5 .

<!-- b000171 | prose | pages [13] -->
STEP 5   To find the relationship between every evaluated object and reference data series, we calculate the average value of correlation coefficient of every evaluation criterion and reference data series. We define it as Correlation. As is shown in follows.

<!-- b000172 | prose | pages [13] -->
n 1  r y ( ) j j i n  i 1

<!-- b000173 | prose | pages [13] -->
STEP 6   Calculate the weight of every evaluation criterion. That is:

<!-- b000174 | prose | pages [13] -->
r j   r j 1,2, , m j    r r r 1 2 m

<!-- b000175 | heading | pages [13] -->
STEP 7   Construct general evaluation model

<!-- b000176 | prose | pages [13] -->
        Z r a (1) r a (2) r a m ( ) i 1,2, , n i 1 i 2 i m i

<!-- b000177 | heading | pages [13] -->
6.2.3 Results of Grey Correlation Model

<!-- b000178 | prose | pages [13] -->
Based on above steps, we can get results by MATLAB programming. The evaluation results of basketball, football and college filed hockey coaches can be easily gotten by computer simulation. The results are shown in Table 8.

<!-- b000179 | furniture | pages [14] -->
Team #26160                                                             Page 13 of 35

<!-- b000180 | caption | pages [14] -->
Table 8. Scores of top 15 basketball coaches (Grey Correlation Model)

<!-- b000181 | prose | pages [14] -->
Rank Coach Last School Scores 1 Harry Statham McKendree 0.834 2 Danny Miles Oregon Institute of Technology 0.718 3 Herb Magee† Philadelphia College 0.710 4 Mike Krzyzewski Duke 0.662 5 Bob Knight Texas Tech 0.613 6 Dean Smith North Carolina 0.599 7 Jim Boeheim Syracuse 0.585 8 Jim Calhoun Connecticut 0.570 9 Adolph Rupp Kentucky 0.540 10 Lou Henson Illinois 0.519 11 Eddie Sutton San Francisco 0.517 12 Lute Olson Arizona 0.507 13 Lefty Driesell Georgia State 0.474 14 Ray Meyer DePaul 0.468 15 Hank Iba Oklahoma State 0.462

<!-- b000182 | prose | pages [14] -->
To show scores of top 15 basketball coaches intuitively, we draw Figure 3. as follows by the data from Table 8. According to the figure, we find that the top five basketball college coaches all time are Harry Statham, Danny Miles, Herb Magee†, Mike Krzyzewski, Bob Knight.

<!-- b000183 | prose | pages [14] -->
Scores of top 15 basketball coaches

<!-- b000184 | prose | pages [14] -->
0.9 0.8 0.7 0.6 Scores 0.5 0.4 0.3 0.2 0.1 0

<!-- b000185 | caption | pages [14] -->
Figure 3. Scores of top 15 basketball coaches

<!-- b000186 | prose | pages [14] -->
Similarly, by analysis data of the quality of field hockey coaches,[ http://en.wikipedia.org/wiki/List_of_college_field_hockey_coaches_with_2 50_wins] We can get score of top 5 field hockey coaches in Grey Correlation Method, which is shown in Table 9.

<!-- b000187 | furniture | pages [15] -->
Team #26160                                                             Page 14 of 35

<!-- b000188 | caption | pages [15] -->
Table 9. Scores of top 5 field hockey coaches

<!-- b000189 | prose | pages [15] -->
Jan Nancy Sharon Coach Jan Trapp Pat Rudy Hutchinson Stevens Pfluger

<!-- b000190 | prose | pages [15] -->
Scores 0.847 0.735 0.694 0.674 0.663 Rank 1 2 3 4 5

<!-- b000191 | prose | pages [15] -->
To show scores of top 5 field hockey coaches intuitively, we draw Figure 4. as follows by the data from Table 9. According to the figure, we find that the top five field hockey college coaches all time are Jan Hutchinson, Jan Trapp, Nancy Stevens, Sharon Pfluger, Pat Rudy.

<!-- b000192 | prose | pages [15] -->
Scores of top 15 field hockey coaches

<!-- b000193 | prose | pages [15] -->
0.900 0.800 0.700 0.600 Scores 0.500 0.400 0.300 0.200 0.100 0.000

<!-- b000194 | caption | pages [15] -->
Figure 4. Scores of top 15 field hockey coaches

<!-- b000195 | prose | pages [15] -->
Similarly, by analysis data of the quality of football coaches, [http://en.wikipedia.org/wiki/List_of_college_football_coaches_with_200_wins]We can get scores of top 5 football college coaches in the same method, which is shown in Table 10.

<!-- b000196 | caption | pages [15] -->
Table 10. Scores of top 5 football coaches

<!-- b000197 | prose | pages [15] -->
Bobby Bear Coach Joe Paterno Lou Holtz Pop Warner Bowden Bryant

<!-- b000198 | prose | pages [15] -->
Scores 0.834 0.737 0.647 0.525 0.513

<!-- b000199 | prose | pages [15] -->
Rank 1 2 3 4 5

<!-- b000200 | prose | pages [15] -->
To show scores of top 5 football coaches intuitively, we draw Figure 5. as follows by the data from Table 10. According to the figure, we find that the top five football college coaches all time are Joe Paterno, Bobby Bowden, Bear Bryant, Lou Holtz, Pop Warner.

<!-- b000201 | furniture | pages [16] -->
Team #26160                                                             Page 15 of 35

<!-- b000202 | prose | pages [16] -->
Scores of top 15 football coaches

<!-- b000203 | prose | pages [16] -->
0.900 0.800 0.700 0.600 Scores 0.500 0.400 0.300 0.200 0.100 0.000

<!-- b000204 | caption | pages [16] -->
Figure 5. Scores of top 15 football coaches

<!-- b000205 | heading | pages [16] -->
6.3 Fuzzy Comprehensive Evaluation Model

<!-- b000206 | prose | pages [16] -->
Giving a rank of things according to their nature is common sense. However, in many cases, the nature of the comparison has no distinct boundary and it is often difficult to compare and sort. As our problem showing, we need to give them a evaluation and rank according to the coaches’ accomplishment and ability. But the comprehensive ranking needs to consider personal quality, training quality and team achievements of the coaches, each side is contains a lot of integrated criterion, so direct ranking is difficult. Herein, we use multi-level fuzzy comprehensive evaluation algorithm to evaluate the college coaches of some sports.

<!-- b000207 | heading | pages [16] -->
6.3.1 Introduction of Fuzzy Comprehensive Algorithm

<!-- b000208 | prose | pages [16] -->
In this part, we will show the basic steps of multi-level fuzzy comprehensive evaluation model.

<!-- b000209 | heading | pages [16] -->
1. Giving the set of evaluation objects

<!-- b000210 | prose | pages [16] -->
According to the problem，we select the top 10 coaches of some field as the   

<!-- b000211 | heading | pages [16] -->
X A

<!-- b000212 | prose | pages [16] -->
{ A , , A },0 n 10 ， evaluation objects 1 2 n

<!-- b000213 | heading | pages [16] -->
2. Determining factor set (also called criteria set)

<!-- b000214 | prose | pages [16] -->
  U { , u u , , } u In many evaluation factors, in most cases, we define . What’s 1 2 i more, according to the certain attributes, we divide it into some subset B,   i i i   i 1,2, B , . Here, B is second criterion. U { u , u , , u } i 1 2 i Meet the conditions:

<!-- b000215 | prose | pages [16] -->
B   n n  . All subsets should be included in total set. i  i 1 B  U U  . A subset set should be included in total set. i  i 1     .No association between subsets. U U , i j i j

<!-- b000216 | furniture | pages [17] -->
Team #26160                                                             Page 16 of 35

<!-- b000217 | heading | pages [17] -->
3. Determining the comment set

<!-- b000218 | prose | pages [17] -->
The comment set is crucial to evaluate the coaches. In this problem, we define the comment set as follows:

<!-- b000219 | prose | pages [17] -->
★★★★★ ★★★★ ★★★ ★★ ★ Level

<!-- b000220 | prose | pages [17] -->
Score 5 4 3 2 1

<!-- b000221 | heading | pages [17] -->
4. Membership functions

<!-- b000222 | prose | pages [17] -->
For certain properties of object A, there exists differences. We can use a real number which from 0 to 1 in close interval to represent the difference. Particularly, 0 indicates the evaluation properties of an object is minimum, that is to say, the properties of an object don’t exist. 1 represents the highest level of evaluation properties of certain object.

<!-- b000223 | prose | pages [17] -->
u A , ( ) Define the difference of object A as membership, represented as:

<!-- b000224 | prose | pages [17] -->
 . 0 u A ( ) 1 Furthermore, since the membership is based on the different properties of different objects (as A) obtained, so the study of object properties can determine relative membership function and membership.

<!-- b000225 | prose | pages [17] -->
Through processing the data, we select top 10 college coaches in a sports field, we can get the relationship between membership and membership function. Then we get the membership. Usually, we integrate empirical formulas and membership functions to figure out the membership.

<!-- b000226 | prose | pages [17] -->
  d d d 11 12 1 j   d d d   21 22 2 j  D      d d d   i 1 i 2 ij In which:

<!-- b000227 | prose | pages [17] -->
j: the level of evaluation i: the number of evaluation criterion

<!-- b000228 | heading | pages [17] -->
5. Getting weights according to AHP

<!-- b000229 | prose | pages [17] -->
By the basic model studying, we determine the weight vector of this model.

<!-- b000230 | prose | pages [17] -->
 B ( , b b b , ) B is the weight of personal quality, training quality and team 1 2 3 achievements.

<!-- b000231 | prose | pages [17] -->
   iB i  B ( b , b ) B b B ( b , b , b , b ) ( 1,2,3) , , , is defined as the 1 11 12 2 21 3 31 32 33 34 weights of second criterion.

<!-- b000232 | furniture | pages [18] -->
Team #26160                                                             Page 17 of 35

<!-- b000233 | caption | pages [18] -->
Table 11. Weight vector of this model

<!-- b000234 | prose | pages [18] -->
★ ★ ★ ★ ★ The The ★ ★ ★ ★ First level weight Second level weight ★ ★ ★ criterion criterion ( B ) iB ) ( ★ ★ ij ★ Coaching d d d d d 0.5498 11 12 13 13 15 time Personal 0.2496 quality d d d d d Gender 0.4502 21 22 23 24 25

<!-- b000235 | prose | pages [18] -->
Training Race command d d d d d 0.1565 0.5503 31 32 33 34 35 quality capability

<!-- b000236 | prose | pages [18] -->
d d d d d Win 0.2853 41 42 43 44 45

<!-- b000237 | prose | pages [18] -->
d d d d d Losses 0.1160 51 52 53 54 55 Team 0.5938 achievements Win-loss d d d d d 0.4256 61 62 63 64 65 percentage Performance in d d d d d 0.1731 71 72 73 74 75 league matches

<!-- b000238 | prose | pages [18] -->
The training quality include three aspects. However, organizational capability and management capability have little effects. So we ignore them and adjust the proportion when we calculate the concrete rank.

<!-- b000239 | prose | pages [18] -->
d is defined as concrete calculations of different college coaches in different ij sports field.

<!-- b000240 | heading | pages [18] -->
6. Comprehensive evaluate coach performance

<!-- b000241 | prose | pages [18] -->
    B OR d d d d d 1 1 11 12 13 14 15        D BOR ( , b b b O B OR , ) ( , b b b O d , ) d d d d     1 2 3 2 2 1 2 3 21 22 23 24 25     B OR d d d d d     3 3 31 32 33 34 35  ( d d , , d d , , d ) 1 2 3 4 5   , is defined as M , is defined as a b a b ab O represents ( , )    . The final score is calculated as follows: a b ( a b ) 1

<!-- b000242 | prose | pages [18] -->
T  Z B D

<!-- b000243 | heading | pages [18] -->
6.3.2 Concrete Calculation

<!-- b000244 | prose | pages [18] -->
Based on above steps, we calculate membership functions of every quality of every coach. In our model, the membership function is liner function. Then, we get membership by corresponding membership function. Herein, we choose top 15 of college coaches, which are shown as follows:

<!-- b000245 | furniture | pages [19] -->
Team #26160                                                             Page 18 of 35

<!-- b000246 | caption | pages [19] -->
Table 12. Scores of top 15 basketball coaches’ quality

<!-- b000247 | prose | pages [19] -->
Coach CT Gender RCC Wins Lose W-L% FF

<!-- b000248 | prose | pages [19] -->
Harry Statham 5 2 5 5 5 3 5 Herb Magee 5 2 4 5 5 3 4 Danny Miles 4 2 5 5 5 3 4 Adolph Rupp 4 2 3 4 5 5 3 Mike Krzyzewski 3 2 4 5 3 4 4 Dean Smith 3 2 4 4 4 4 4 Bob Knight 4 2 4 4 4 3 3 Jim Boeheim 3 2 4 4 3 4 2 Jerry Tarkanian 2 2 3 3 5 5 2 Roy Williams 1 2 3 2 5 5 3 Jim Calhoun 4 2 3 4 4 2 2 Lute Olson 2 2 4 3 4 3 3 Eddie Sutton 3 2 4 3 3 3 2 Phog Allen 5 2 1 2 4 3 2 Rick Pitino 1 2 3 2 4 4 3 E.A. Diddle 4 2 1 3 3 3 1 Lefty Driesell 4 2 2 3 5 2 1 Lou Henson 4 2 3 3 5 1 2 Ray Meyer 4 2 2 2 4 2 2 Denny Crum 2 2 3 2 3 2 3 In the table:

<!-- b000249 | prose | pages [19] -->
RCC-- Race command capability CT—coaching time FF—number of NCAA final four appearance

<!-- b000250 | prose | pages [19] -->
The scores of top 15 basketball college coaches are shown in Figure 6. From the figure we can find the top 5 basketball college coaches are Harry Statham, Herb Magee, Danny Miles , Adolph Rupp, Mike Krzyzewski.

<!-- b000251 | prose | pages [19] -->
Scores of top 15 field hockey coaches

<!-- b000252 | prose | pages [19, 20] -->
5 4 Scores 3 2 1 0 Through normalizing the data, we get Fuzzy Decision Matrix. Finally, we get final grades and ranks by fuzzy calculation of Fuzzy Decision Matrix (R) and Weight Matrix (B), which is shown in Table 13.

<!-- b000253 | caption | pages [19] -->
Figure 6. Scores of top 15 basketball coaches

<!-- b000254 | furniture | pages [20] -->
Team #26160                                                             Page 19 of 35

<!-- b000256 | caption | pages [20] -->
Table 13. Scores and rank of top 15 basketball coaches

<!-- b000257 | prose | pages [20] -->
(Fuzzy Comprehensive Evaluation Model) Ranking Coach Last School Score 1 Harry Statham McKendree 4.1557 2 Herb Magee Philadelphia College 3.9668 3 Danny Miles OTT 3.9156 4 Adolph Rupp Kentucky 3.9068 5 Mike Krzyzewski Duke 3.8072 6 Dean Smith North Carolina 3.6367 7 Bob Knight Texas Tech 3.4184 8 Jim Boeheim Syracuse 3.3622 9 Jerry Tarkanian Fresno State 3.2900 10 Roy Williams North Carolina 3.0161 11 Jim Calhoun Connecticut 2.9767 12 Lute Olson Arizona 2.9044 13 Eddie Sutton San Francisco 2.8700 14 Phog Allen Central Missouri 2.7158 15 Rick Pitino Louisville 2.6944

<!-- b000258 | prose | pages [20] -->
Similarly, by analysis of data we get from Wikipedia, [http://en.wikipedia.org/wiki/List_of_college_field_hockey_coaches_with_250_wins] We get the scores and rank of top 15 field hockey college coaches by Fuzzy Comprehensive Algorithm. Top 5 of them are listed in Table 14.

<!-- b000259 | caption | pages [20] -->
Table 14. Scores and rank of top 5 field hockey college coaches

<!-- b000260 | prose | pages [20] -->
Jan Nancy Coach Jan Trapp Pat Rudy Beth Anders Hutchinson Stevens Scores 4.22 3.91 3.75 3.71 3.60 Rank 1 2 3 4 5

<!-- b000261 | prose | pages [20] -->
To show the top 5 field hockey college coaches Intuitively, we draw Figure 7. as follows. From the figure we know that top 5 field hockey coaches are Jan Hutchinson, Jan Trapp, Nancy Stevens, Pat Rudy, Beth Anders. By searching the internet for their information, it is found that the number of honor is large enough to support every one them rank into top 5.

<!-- b000262 | furniture | pages [21] -->
Team #26160                                                             Page 20 of 35

<!-- b000263 | prose | pages [21] -->
Scores of top 15 football coaches

<!-- b000264 | prose | pages [21] -->
5.000 4.500 4.000 3.500 Scores 3.000 2.500 2.000 1.500 1.000 0.500 0.000

<!-- b000265 | caption | pages [21] -->
Figure 7. Scores of top 15 field hockey college coaches

<!-- b000266 | prose | pages [21] -->
Similarly, by analysis of data we get from Wikipedia, [http://en.wikipedia.org/wiki/List_of_college_football_coaches_with_200_wins] We get the scores and rank of top 15 football college coaches by Fuzzy Comprehensive Algorithm. Top 5 of them are listed in Table 15.

<!-- b000267 | caption | pages [21] -->
Table 15. Scores and rank of top 5 football college coaches

<!-- b000268 | prose | pages [21] -->
Bobby Tom Coach Joe Paterno Bear Bryant Pop Warner Bowden Osborne

<!-- b000269 | prose | pages [21] -->
Scores 4.805 4.715 4.579 3.779 3.407

<!-- b000270 | prose | pages [21] -->
Rank 1 2 3 4 5

<!-- b000271 | prose | pages [21] -->
To show the top 5 football college coaches Intuitively, we draw Figure 8. as follows. From the figure we know that top 5 football coaches are Bobby Bowden, Joe Paterno, Bear Bryant, Tom Osborne, Pop Warner.

<!-- b000272 | prose | pages [21] -->
Scores of top 15 football coaches

<!-- b000273 | prose | pages [21] -->
5.000 4.000 Score 3.000 2.000 1.000 0.000

<!-- b000274 | caption | pages [21] -->
Figure 8. Scores of top 15 football college coaches

<!-- b000275 | furniture | pages [22] -->
Team #26160                                                             Page 21 of 35

<!-- b000276 | heading | pages [22] -->
6.4 Results Review

<!-- b000277 | prose | pages [22] -->
We develop the basic model by using AHP algorithm and get the weights of seven main evaluation criterion. Then, we develop two evaluation models to evaluate college coaches of basketball, field hockey and football. Final ranks of three sports are listed respectively. Herein, we discuss the difference of two evaluation models and analyze some reasons. Grey Correlation rank, Fuzzy Comprehensive rank and Current rank are listed in Table 15.

<!-- b000278 | caption | pages [22] -->
Table 15. Ranks comparison

<!-- b000279 | prose | pages [22] -->
Grey Fuzzy Comprehensive Current Coaches Correlation Rank Rank Rank Harry Statham 1 1 1 Danny Miles 2 3 2 Herb Magee 3 2 3 Mike Krzyzewski 4 5 4 Jim Boeheim 7 8 5 Bob Knight 5 7 6 Dean Smith 6 6 7 Jim Calhoun 8 11 8 Adolph Rupp 9 4 9 Eddie Sutton 11 13 10

<!-- b000280 | prose | pages [22] -->
From above rank table, we can find that two evaluation models’ ranks reach great agreement with that of Wikipedia. However, there is little difference between two evaluation models. To show the difference apparently, we draw the figure of three ranks, which is shown in Figure 9.

<!-- b000281 | heading | pages [22] -->
Two models' rank comparison

<!-- b000282 | prose | pages [22] -->
14 12 10 Ranks 8 6 4 Fuzzy Rank 2 Grey Rank 0 Current Rank

<!-- b000283 | prose | pages [22, 23] -->
Basketball Coaches Through compared with current rank, it’s apparent that Grey Correlation rank is better than that of Fuzzy Comprehensive. We analyze reasons for difference as follows:  Fuzzy Comprehensive Algorithm considers inner link of college coaches’ all quality, while the Fuzzy Comprehensive Algorithm doesn’t.  There exists difference in data processing.

<!-- b000284 | caption | pages [22] -->
Figure 9. Two models’ rank comparison

<!-- b000285 | furniture | pages [23] -->
Team #26160                                                             Page 22 of 35

<!-- b000287 | prose | pages [23] -->
Our evaluation ranks are different with that some sports website given. Different websites use different evaluation criterion to evaluate college coaches. For example, criterion in some evaluation systems include the number of consecutive wins, but we didn’t take it into consideration. Therefore, it’s obvious that ranks are different. Concrete analysis and optimal ranks will be discussed in Conclusion part.

<!-- b000288 | heading | pages [23] -->
7 Is Time Line Horizon Influential?

<!-- b000289 | prose | pages [23] -->
In the past 100 years, people’s evaluation to coaches may change. One reason is that different society and live environment has different effects on coaches. Meanwhile, evaluation criterion would change with time changing. These reasons all affect fairness of college coaches’ ranks.

<!-- b000290 | prose | pages [23] -->
By considering time changing, we discuss whether time line horizon has effects on coaches’ ranks or not. Physical environment, spiritual environment and recognition of coaches would change with time changing. Based on considering physical and spiritual environment, we provide new college coaches’ ranks.

<!-- b000291 | prose | pages [23] -->
Through comparing coaches’ scores with their start teaching time, we observe whether their changing trends are in agreement.

<!-- b000292 | prose | pages [23] -->
In AHP model, we ignored approximate 7% weight. In this model, we will assign weight again by considering time changing. We note time as one of the evaluation criterion and assign 7% weight to it. Membership function is used to get normalized membership of time with respect to different coaches. That is :

<!-- b000293 | prose | pages [23] -->
 T 1900  Z 2 100 In which, T represents the start teaching time of coach. Z represents time score 2 after normalized.

<!-- b000294 | prose | pages [23] -->
On the basis of Grey Correlation Algorithm, we calculate scores again and the   weight are and . The normalized scores is: 1=0.93 2=0.07      Z= Z Z 1 1 2 2

<!-- b000295 | prose | pages [23] -->
 represents weight of score calculated by Grey Correlation Model. In which, 1  represents weight of time criteria. Z represents the score calculated by Grey 2 1 Correlation Model. Zrepresents final total score.

<!-- b000296 | prose | pages [23] -->
Comparing normalized scores with former scores, the difference between ranks considering coaching start time or not is shown in Figure 9.

<!-- b000297 | furniture | pages [24] -->
Team #26160                                                             Page 23 of 35

<!-- b000298 | prose | pages [24] -->
Comparison between ranks considering coaching start time or not 8

<!-- b000299 | prose | pages [24] -->
6 Rank difference is very little for top coaches Difference with previous rank 4

<!-- b000300 | prose | pages [24] -->
2

<!-- b000301 | prose | pages [24] -->
0

<!-- b000302 | prose | pages [24] -->
-2

<!-- b000303 | prose | pages [24] -->
-4

<!-- b000304 | prose | pages [24] -->
0 5 10 15 20 25 30 35 40 Rank that considering coaching start time

<!-- b000305 | caption | pages [24] -->
Figure 10. Comparison between ranks considering coaching start time or not of basketball

<!-- b000306 | prose | pages [24] -->
In Figure 10. the horizontal coordinate represents rank that has not considered coaching start time. The vertical coordinate represents difference with previous rank. From the difference value between ranks considering coaching start time or not, we can easily find that time has effects on college coaches’ ranks. What’s more, time criteria has more effects on coaches whose rank is behind, while it has fewer effects on coaches whose rank is front.

<!-- b000307 | prose | pages [24] -->
To examine above conclusion, we use football coaches’ data to verify the results, which are shown in Figure 11. It’s obvious that former conclusion is right.

<!-- b000308 | prose | pages [24] -->
Comparison between ranks considering coaching start time or not

<!-- b000309 | prose | pages [24] -->
15

<!-- b000310 | prose | pages [24] -->
10 Differenci with previous rank Rank difference is little for top 10

<!-- b000311 | prose | pages [24] -->
5

<!-- b000312 | prose | pages [24] -->
0

<!-- b000313 | prose | pages [24] -->
-5

<!-- b000314 | prose | pages [24] -->
0 5 10 15 20 25 30 35 40 Rank that considering coaching start time

<!-- b000315 | caption | pages [24] -->
Figure 11. Comparison between ranks considering coaching start time or not of football

<!-- b000316 | prose | pages [24] -->
In conclusion, time criteria has more effects on coaches whose rank is behind, while it has fewer effects on coaches whose rank is front.

<!-- b000317 | furniture | pages [25] -->
Team #26160                                                             Page 24 of 35

<!-- b000318 | heading | pages [25] -->
8 Sensitivity Analysis

<!-- b000319 | heading | pages [25] -->
8.1 Sensitivity of Grey Correlation Method

<!-- b000320 | prose | pages [25] -->
According to Equation 6.2, resolution ratio is the key parameter to correlation coefficient, which is tightly related to correlation. If is too small, the difference of correlation coefficient will be too large, which results in failing to give out the correlation of every evaluation criterion and reference data series correctly. On the contrary, if is too large, the difference of correlation coefficient is too small, leading to the absolute difference having a little impact on evaluation results. Therefore the value of is crucial to final evaluation results.

<!-- b000321 | prose | pages [25] -->
In the process of calculating, value of is uniformly 0.5. In order to analyze its sensitivity, take basketball coaches for example. For resolution ratio in[0 ,1], we calculate the effect of resolution ratio on evaluating by assigning step length as 0.2. After being processed by computer, ranks of top 10 coaches are shown in Figure 12. In the figure, the horizontal coordinate represents the top 10 coaches, who are represented by A, B, … , J, the vertical coordinate iZ represents correlation of every coach with standard data, （beta）represents resolution ratio, beta represents ranks of top 10 coaches.

<!-- b000322 | prose | pages [25] -->
The effect of resolution ratio on evaluating results

<!-- b000323 | prose | pages [25] -->
0.850 beta=0.1(ABC DGF HEIJ) 0.800 beta=0.3(ABC DGF HEIJ) 0.750 beta=0.5(ABC DFG EHIJ) beta=0.7(ABC DFG EHIJ) 0.700 Z(i) beta=0.9(ABC DFG EHIJ) 0.650

<!-- b000324 | prose | pages [25] -->
0.600

<!-- b000325 | prose | pages [25] -->
0.550

<!-- b000326 | prose | pages [25] -->
0.500 A B C D F G E H I J Coaches

<!-- b000327 | caption | pages [25] -->
Figure 12. The effect of resolution ratio on evaluating results

<!-- b000328 | prose | pages [25] -->
From the results of above figure, it is obviously to find that evaluation results are divided into two parts, because of changes of resolution ratio. The erratic stage as   0.3 0.3 and the stable stage as .

<!-- b000329 | furniture | pages [26] -->
Team #26160                                                             Page 25 of 35

<!-- b000330 | prose | pages [26] -->
 0.3 1. When , result of correlation change greatly and the rank is erratic. If assign resolution ratio small value, stable control capability is weak. Therefore, we couldn’t use in this range.

<!-- b000331 | prose | pages [26] -->
  0.3 0.5 2. When , result of correlation change weakly. We find that when , the change of resolution ratio has no effects on ranks, all of the ranks are consistent. Therefore, in our paper, it’s reasonable to assign =0.5. meanwhile, the result is stable.

<!-- b000332 | heading | pages [26] -->
8.2 Sensitivity of Fuzzy Comprehensive Method

<!-- b000333 | prose | pages [26] -->
The sensitivity analysis is crucial to stability and rank of the reliability evaluation model. Herein, we analyze the sensitivity of evaluation criterion weights. Briefly , to show it’s sensitivity，we change the minimum and maximum weight ratio to get the different score of different coach.

<!-- b000334 | prose | pages [26] -->
We choose basketball coaches’ data as an example.

<!-- b000335 | prose | pages [26] -->
First, we adjust the maximum weight of the evaluation make it increase 0.02, get the score of the coaches.

<!-- b000336 | prose | pages [26] -->
Then, we adjust the maximum weight of the evaluation make it decrease 0.02, get the score of the coaches.

<!-- b000337 | prose | pages [26] -->
The results are showing in Figure 13.

<!-- b000338 | prose | pages [26] -->
The scores in different weight

<!-- b000339 | prose | pages [26] -->
4.5 4.3 Maximum weight increased 4.1 0.02 3.9 3.7 Maximum weight decreased 3.5 0.02 3.3 3.1 initial score 2.9 2.7 2.5

<!-- b000340 | caption | pages [26] -->
Figure 13. The score in different weight

<!-- b000341 | prose | pages [26] -->
Perhaps this approach is not scientific, but it is capable to show us a better strength of this kind of model sensitivity. From the figure we see that the weight change will have an impact on score, but the impact is limited and the ranking changes little. Therefore, we conclude that the model is of high stability.

<!-- b000342 | furniture | pages [27] -->
Team #26160                                                             Page 26 of 35

<!-- b000343 | heading | pages [27] -->
9 Discussion and Conclusion

<!-- b000344 | heading | pages [27] -->
9.1 Solutions to All Problems

<!-- b000345 | prose | pages [27] -->
The three proposed problems have been well answered in our models.

<!-- b000346 | prose | pages [27] -->
 Develop a model to look for the best college coach for the previous century.

<!-- b000347 | prose | pages [27] -->
To answer this problem, AHP is employed to filter seven main criterion, gender and winning courts included, and to get their weights respectively. Then both Grey Relational Model and Fuzzy Comprehensive Evaluation Model are built, each of which is to rank those coaches. The former is about the relevance among the evaluation criterion to get the correlation, while the latter integrates empirical formula and membership functions to figure out the corresponding membership and then to give the evaluation matrix. Furthermore, we compare the results with current ranks and find that grey model has slight advantage over fuzzy model. That is to say that Grey Relational Model is more optimal

<!-- b000348 | prose | pages [27] -->
 Analyze whether it make a difference with time line horizon or not.

<!-- b000349 | prose | pages [27] -->
We adjust the model obtained earlier and get the conclusion that: time line horizon has more effects on coaches whose rank is behind, while it has fewer effects on coaches who rank top.

<!-- b000350 | prose | pages [27] -->
 Present top 5 college coaches in each of 3 different sports.

<!-- b000351 | prose | pages [27] -->
Using the model we obtain, we rank the coaches in the basketball. As the evaluation criterion we chose are comprehensive and the coaches who were engaged in different sport fields have the same quality, we apply the above method to rank other coaches in different sports flied. Such as: field hockey and football. Besides, considering time line horizon, we provide the final general ranks, which are shown as follows:

<!-- b000352 | prose | pages [27] -->
Rank Basketball Field hockey Football

<!-- b000353 | prose | pages [27] -->
1 Harry Statham Jan Hutchinson Joe Paterno 2 Danny Miles Jan Trapp Bobby Bowden 3 Herb Magee Nancy Stevens Bear Bryant 4 Mike Krzyzewski Sharon Pfluger Lou Holtz 5 Bob Knight Pat Rudy Pop Warner

<!-- b000354 | furniture | pages [28] -->
Team #26160                                                             Page 27 of 35

<!-- b000355 | heading | pages [28] -->
9.2 Honor Roll

<!-- b000356 | prose | pages [28] -->
Honor Roll

<!-- b000357 | heading | pages [28] -->
After building mathematical models and analysing

<!-- b000358 | prose | pages [28] -->
the results, we find the top 5 basketball college coaches which are shown as follows:

<!-- b000359 | prose | pages [28] -->
Rank Coach Teams 1 Harry Statham McKendree (1967–present) 2 Danny Miles Oregon Tech (1971–present) 3 Herb Magee Philadelphia (1967–present) 4 Mike Krzyzewski Army (1975–1980), Duke (1980–present) 5 Bob Knight Indiana(1971–2000),Texas Tech (2001–2008)

<!-- b000360 | prose | pages [28] -->
Top 5 football college coaches are shown in the following:

<!-- b000361 | prose | pages [28] -->
Rank Coach Teams 1 Joe Paterno Nittany Lions(1966-2011) 2 Bobby Bowden West Virginia (1970–1975), Florida State (1976–2009) 3 Bear Bryant Texas A&M (1954–1957), Alabama (1958–1982) 4 Lou Holtz Notre Dame (1986–1996), South Carolina (1999–2004) 5 Pop Warner Temple Owls (1933–1938), Stanford Indians (1924–1932)

<!-- b000362 | prose | pages [28] -->
Top 5 college filed hockey college coaches are shown:

<!-- b000363 | prose | pages [28] -->
Rank Coach Teams 1 Jan Hutchinson Bloomsburg 1978-2009 2 Jan Trapp Messiah 1973-2011 3 Nancy Stevens Northwestern 1981-1989, Connecticut 1990-present 4 Sharon Pfluger Kean 1983, Montclair St. 1984, TCNJ 1985-present 5 Pat Rudy SUNY Cortland 1981-95, Lock Haven 1996-present

<!-- b000364 | furniture | pages [29] -->
Team #26160                                                             Page 28 of 35

<!-- b000365 | heading | pages [29] -->
9.3 Strengths and Weaknesses

<!-- b000366 | heading | pages [29] -->
Strengths

<!-- b000367 | prose | pages [29] -->
 Grey Correlation Algorithm and Fuzzy Comprehensive Algorithm are both adopted to evaluate college coaches. Through comparing the ranks, we find that Grey Correlation Algorithm is better. The result is convincing.  Through AHP algorithm, we select seven main evaluation criterion. What’s more, we improve our model by considering gender and time line horizon. Thus, our evaluation method is exhaustive.  Through plenty of figures and tables, it’s intuitively shown that our ranks are in good agreement with that of Wikipedia. That’s to say our model is practical to some extent.  Our data comes from the official website such as National Collegiate Athletic Association (NCAA), it’s believable.

<!-- b000368 | heading | pages [29] -->
Weaknesses

<!-- b000369 | prose | pages [29] -->
 In the wins criteria, we only considered the number of wins and neglected the Simple Rating System (SRS) and Strength of Schedule (SOS). It may lead to little difference with other evaluation method.  We didn’t find much data of female college coaches. So the analysis of gender criteria is not exhaustive.  We only considered objective data, but didn’t consider coaches’ subjective factors, such as moral, spirit and so on.

<!-- b000370 | heading | pages [29] -->
9.4 Conclusion

<!-- b000371 | prose | pages [29] -->
By developing three models, we get an objective rank of college basketball, field hockey and football coaches. Firstly, AHP Model is used to determine seven evaluation criterion. Herein, we consider the effects of gender criteria, which make our evaluation method widespread. Then, we develop Grey Correlation Model and Fuzzy Comprehensive Model to rank college coaches. By comparing with practical rank given by sports fans, we find the above two model both reach well agreement with practical rank. What’s more, we find that the rank calculated by Grey Correlation Algorithm is better than that of Fuzzy Comprehensive Algorithm.

<!-- b000372 | prose | pages [29] -->
Then, we analyze the effects of time criteria on evaluation model. We conclude that time line horizon has more effects on coaches whose rank is behind, while it has fewer effects on coaches whose rank is front. The result is in great agreement with practice. Finally, we provide rank of top 5 college coaches on basketball, field hockey and football sports.

<!-- b000373 | prose | pages [29] -->
Despite our evaluation model include eight criterion, the modeling domain presented by this problem is vast, and there is a large amount of room for improvement. We believe that the work we have presented here is a significant and successful attempt at solving this problem.

<!-- b000374 | furniture | pages [30] -->
Team #26160                                                             Page 29 of 35

<!-- b000375 | heading | pages [30] -->
A Letter to Sports Illustrated

<!-- b000376 | prose | pages [30] -->
February 10, 2014 Dear editor， We all know that sports illustrated is one of the most popular sporting magazine in the world. Hearing that you are looking for the “best all time college coach” male or female for the previous century, it’s our pleasure to make some attempt to do it. Different from previous methods of practical survey, we adopt some mathematical method to build an evaluation system. Based on coaches data available, we give out the ranks of college coaches in three sports, basketball, field hockey and football for recent 100 years.

<!-- b000377 | prose | pages [30] -->
It is thought that an excellent coach must do well in three aspects, that is, personal quality, training quality and team achievements. After filtering from lots of factors, there are 7 key criterion finally determined to be the evaluating standards, which are coaching time, gender，command capability，number of wins， number of losses，win-loss percentage and performance in league matches.

<!-- b000378 | prose | pages [30] -->
When it comes to evaluating process, we have tried two approaches. For the first model, grey model for short, optimal value for every criteria is firstly determined, and we grade these coaches by calculating the approaching degree to the optimal value. For the second model, called fuzzy model, we grade them by considering that different criterion show different importance to final evaluation. Through the analysis of results derived from two models, it is found that the first one is more objective. Therefore, the ranking from grey model is as follows.

<!-- b000379 | prose | pages [30] -->
Rank Basketball Field hockey Football

<!-- b000380 | prose | pages [30] -->
1 Harry Statham Jan Hutchinson Joe Paterno 2 Danny Miles Jan Trapp Bobby Bowden 3 Herb Magee Nancy Stevens Bear Bryant 4 Mike Krzyzewski Sharon Pfluger Lou Holtz 5 Bob Knight Pat Rudy Pop Warner

<!-- b000381 | prose | pages [30] -->
With the development of society, the environment which coaches live would change. To analyze whether time has effects on evaluation results or not, we promote above models by considering time criteria. We find that time has fewer effects on the ranking front college coaches.

<!-- b000382 | prose | pages [30] -->
Finally, we think that best all time college coach should not be one but ones. Since every evaluation method has both advantages and disadvantages. There is only little difference between top 5 college coaches’ scores in every sports field, it is distinguishing in mathematics, but it’s not important for evaluating comprehensive quality of top 5 college coaches. They all have own unique quality, so they are all best. They all have great influence on respective field.

<!-- b000383 | prose | pages [30] -->
Sincerely yours, Team 26160

<!-- b000384 | furniture | pages [31] -->
Team #26160                                                             Page 30 of 35

<!-- b000385 | heading | pages [31] -->
Reference

<!-- b000386 | references | pages [31] -->
[1] Yangping Zhang, Feng Zhai. "Study of a system that evaluates the comprehensive

<!-- b000387 | references | pages [31] -->
capacities of excellent college track and field coaches." Journal of Physical

<!-- b000388 | references | pages [31] -->
Education 16.11 (2009): 77-80.

<!-- b000389 | references | pages [31] -->
[2] Grisaffe, Christie, Lindsey C. Blom, and Kevin L. Burke. "The effects of head

<!-- b000390 | references | pages [31] -->
and assistant coaches' uses of humor on collegiate soccer players' evaluation of

<!-- b000391 | references | pages [31] -->
their coaches." Journal of Sport Behavior 26.2 (2003): 103-108.

<!-- b000392 | references | pages [31] -->
[3] Radicchi, Filippo. "Who is the best player ever? A complex network analysis of

<!-- b000393 | references | pages [31] -->
the history of professional tennis." PloS one 6.2 (2011): e17249.

<!-- b000394 | references | pages [31] -->
[4] Knoppers, Annelies, et al. "Opportunity and work behavior in college coaching."

<!-- b000395 | references | pages [31] -->
Journal of Sport & Social Issues 15.1 (1991): 1-20.

<!-- b000396 | references | pages [31] -->
[5] Knoppers, Annelies, et al. "Gender ratio and social interaction among college

<!-- b000397 | references | pages [31] -->
coaches." Sociology of Sport Journal 10.3 (1993): 256-269.

<!-- b000398 | references | pages [31] -->
[6] Pastore, Donna L., Bernie Goldfine, and H. Riemer. "NCAA college coaches and

<!-- b000399 | references | pages [31] -->
athletic administrative support." Journal of Sport Management 10.4 (1996):

<!-- b000400 | references | pages [31] -->
373-387.

<!-- b000401 | references | pages [31] -->
[7] Caccese, Thomas M., and Cathleen K. Mayerberg. "Gender differences in

<!-- b000402 | references | pages [31] -->
perceived burnout of college coaches." Journal of Sport Psychology (1984).

<!-- b000403 | references | pages [31] -->
[8] Saaty, Thomas L. What is the analytic hierarchy process?. Springer Berlin

<!-- b000404 | references | pages [31] -->
Heidelberg, 1988.

<!-- b000405 | references | pages [31] -->
[9] Saaty, Thomas L. "How to make a decision: the analytic hierarchy process."

<!-- b000406 | references | pages [31] -->
European journal of operational research 48.1 (1990): 9-26.

<!-- b000407 | references | pages [31] -->
[10] Tao, Yang, and Yang Xinmiao. "Fuzzy comprehensive evaluation, fuzzy

<!-- b000408 | references | pages [31] -->
clustering analysis and its application for urban traffic environment quality

<!-- b000409 | references | pages [31] -->
evaluation." Transportation Research Part D: Transport and Environment 3.1

<!-- b000410 | references | pages [31] -->
(1998): 51-57.

<!-- b000411 | references | pages [31] -->
[11] Shiyun, Liu Luxiang Song Qixin Wang. "A PRELIMINARY STUDY ON

<!-- b000412 | references | pages [31] -->
MULTIFACTORIAL EVALUTION OF NEW CROP VARIETIES WITH THE

<!-- b000413 | references | pages [31] -->
APPLICATION OF THE GREY SYSTEM THEORY [J]." Scientia Agricultura

<!-- b000414 | references | pages [31] -->
Sinica 3 (1989): 003.

<!-- b000415 | references | pages [31] -->
[12] http://www.sports-reference.com/cbb/coaches/

<!-- b000416 | references | pages [31] -->
[13] http://en.wikipedia.org/wiki/List_of_college_men's_basketball_coaches_with_60

<!-- b000417 | references | pages [31] -->
0_wins

<!-- b000418 | references | pages [31] -->
[14] http://en.wikipedia.org/wiki/List_of_college_football_coaches_with_200_wins

<!-- b000419 | references | pages [31] -->
[15] http://en.wikipedia.org/wiki/List_of_college_field_hockey_coaches_with_250_w

<!-- b000420 | references | pages [31] -->
ins

<!-- b000421 | references | pages [31] -->
[16] http://www.secsportsfan.com/best-all-time-ncaa-college-football-coach.html

<!-- b000422 | references | pages [31] -->
[17] http://www.amstat.org/sections/SIS/Sports%20Data%20Resources/

<!-- b000423 | references | pages [31] -->
[18] http://www.basketball-reference.com/coaches/

<!-- b000424 | furniture | pages [32] -->
Team #26160                                                             Page 31 of 35

<!-- b000425 | heading | pages [32] -->
Appendix

<!-- b000426 | heading | pages [32] -->
1. Original data of college basketball coaches

<!-- b000427 | prose | pages [32] -->
Coach Last School C-t Gen. RCC Wins Loss W-L FF

<!-- b000428 | prose | pages [32, 33] -->
Harry Statham McKendree 47 1 39 1076 444 0.708 13 Danny Miles O I T 42 1 32 1000 409 0.71 10 Herb Magee† Philadelphia College 45 1 26 976 391 0.714 11 Mike Krzyzewski Duke 39 1 29 975 302 0.764 11 Jim Boeheim Syracuse 38 1 30 942 314 0.75 4 Bob Knight Texas Tech 42 1 28 899 374 0.706 5 Dean Smith North Carolina 36 1 27 879 254 0.776 11 Jim Calhoun Connecticut 40 1 23 877 382 0.697 4 Adolph Rupp Kentucky 41 1 20 876 190 0.822 6 Eddie Sutton San Francisco 37 1 26 806 329 0.71 3 Lefty Driesell Georgia State 41 1 13 786 394 0.666 0 Lute Olson Arizona 34 1 28 776 285 0.731 5 Lou Henson Illinois 41 1 19 775 420 0.649 2 Jerry Tarkanian Fresno State 30 1 18 761 202 0.79 4 E.A. Diddle Western Kentucky 42 1 3 759 302 0.715 0 Hank Iba Oklahoma State 40 1 8 752 333 0.693 4 Ray Meyer DePaul 42 1 13 724 354 0.672 2 Don Haskins Texas-El Paso 38 1 14 719 353 0.671 1 Phog Allen Central Missouri 48 1 4 719 259 0.735 3 Roy Williams North Carolina 26 1 23 715 187 0.793 7 Rick Pitino Louisville 28 1 18 681 239 0.74 7 Denny Crum Louisville 30 1 23 675 295 0.696 6 Ralph Miller Oregon State 38 1 10 674 370 0.646 0 Mike Montgomery California 32 1 16 670 312 0.682 1 Gary Williams Maryland 33 1 17 668 380 0.637 2 Bob Huggins West Virginia 29 1 20 665 270 0.711 2 John Wooden UCLA 29 1 16 664 162 0.804 12 Cliff Ellis Coastal Carolina 36 1 8 662 423 0.61 0 Hugh Durham Jacksonville 37 1 8 634 430 0.596 2 Norm Stewart Missouri 32 1 16 634 333 0.656 0 Billy Tubbs Texas Christian 29 1 12 609 317 0.658 1 Slats Gill Oregon State 36 1 6 599 393 0.604 2 Tom Davis Drake 32 1 11 597 356 0.626 0 Stew Morrill Utah State 28 1 9 597 276 0.684 0 John Thompson Georgetown 27 1 20 596 239 0.714 3 Thomas Penders Houston 33 1 11 594 420 0.586 0 Guy Lewis Houston 30 1 14 592 279 0.68 5 Coach Last School C-t Gen. Rcc Wins Loss W-L FF Bobby Cremins College of Charleston 31 1 11 586 379 0.607 1 John Calipari Kentucky 22 1 14 585 171 0.774 4 Rick Barnes Texas 27 1 20 578 293 0.664 1 Tony Hinkle Butler 41 1 1 558 394 0.586 0 Norm Sloan North Carolina State 33 1 6 558 359 0.609 1 Gene Keady Purdue 27 1 18 550 289 0.656 0 Frank McGuire South Carolina 30 1 8 549 236 0.699 2 Bill Self Kansas 21 1 15 524 169 0.756 2 Teresa Lawrence Tennessee State 28 3 14 212 189 0.523 1

<!-- b000429 | furniture | pages [33] -->
Team #26160                                                             Page 32 of 35

<!-- b000431 | heading | pages [33] -->
2. Original data of college field hockey coaches

<!-- b000432 | prose | pages [33, 34] -->
Coach Teams C-t Wins Losses W-L% Ties Hutchinson Bloomsburg 1978-2009 32 591 75 0.876 20 Beth Anders Old Dominion 2004-present 29 561 136 0.802 7 Nancy Stevens Connecticut 1990-present 33 554 171 0.756 24 Karen Shelton North Carolina 1981-present 31 550 140 0.793 9 Jan Trapp Messiah 1973-2011 38 536 179 0.74 28 Pat Rudy Lock Haven 1996-present 34 532 178 0.742 21 Sharon Pfluger TCNJ 1985-present 29 498 94 0.836 9 Enza Steele Lynchburg, 1979-present 33 495 195 0.714 11 Missy Meharg Maryland 1988-present 24 450 112 0.796 9 Charlene Penn State 1987-present 28 445 174 0.713 17 Bertie Landes Shippensburg 1999-present 32 418 119 0.77 17 Chamberlin Salisbury 1987-present 25 405 99 0.799 8 Sally Starr Boston U. 1981-present 33 401 259 0.604 21 Brenda Meese Wooster 2009-present 31 393 217 0.642 10 Sally Scatton William Smith 1988-present 24 390 121 0.762 3 Murtagh Bentley 1988-present 26 364 205 0.637 13 Kauffman Elizabethtown 1967-83 33 346 175 0.654 36 Betty Wesner Kutztown 1980-present 32 344 257 0.571 15 Sharon Taylor Lock Haven 1973-1995 28 340 121 0.721 35 Sandy Miller E Stroudsburg 1984-present 28 338 236 0.587 11 Amy Watson Keene St. 1994-present 22 319 154 0.672 11 Jennifer Wake Forest 1992-present 23 319 170 0.651 6 Beth Bozman Duke 2003-2010 23 318 133 0.702 6 Kathleen Syracuse 1978-2006 29 316 214 0.594 14 Ann Petracco FDU-Florham 2003-2009 33 311 306 0.504 40 Madison Virginia 2006-present 23 312 197 0.612 6 Carol Miller Lebanon Valley 2011-present 27 309 216 0.584 27 Hallenbeck Skidmore 2001-present 22 254 132 0.657 2 Coach Teams C-t Wins Losses W-L% Ties Hawthorne W & Mary 1987-present 29 306 251 0.549 6 Dana Hall Washington 1990-2010 23 298 138 0.682 4 Ann Gold Lafayette 1982-2006 25 294 186 0.607 23 Anna Meyer Hartwick 1988-present 24 290 184 0.611 3 Wilkinson Ohio St. 1996-present 25 288 215 0.571 9 Fitzpatrick Ball State 1980-2000 21 285 130 0.682 11 Linda Wage Clark (MA) 1985-present 27 283 207 0.574 24 Kostrinsky Ithaca 1969-1995 27 282 135 0.668 21 Ridinger Missouri State 1975-1990 18 281 101 0.722 24 Pam Hixon Massachusetts  1996 17 272 76 0.768 18 DeLorenzo Middlebury 2001-present 20 271 109 0.712 2 Linda Arena Wittenberg 1982-1996, 1998 23 262 133 0.65 34

<!-- b000433 | furniture | pages [34] -->
Team #26160                                                             Page 33 of 35

<!-- b000435 | heading | pages [34] -->
3. Original data of college football coaches

<!-- b000436 | prose | pages [34] -->
Coach Last School C-t R-c-c Wins Losses W-L% Per.

<!-- b000437 | prose | pages [34, 35] -->
Joe Paterno Penn State 46 37 409 136 0.749 0.662 Bobby Bowden Florida State 40 33 357 124 0.74 0.682 Bear Bryant Alabama 38 29 323 85 0.78 0.552 Pop Warner Temple 42 4 311 103 0.733 0.375 Amos Alonzo Chicago 42 0 275 121 0.681 0 LaVell Edwards Brigham Young 29 22 257 101 0.716 0.341 Tom Osborne Nebraska 25 25 255 49 0.836 0.48 Lou Holtz South Carolina 33 22 249 132 0.651 0.591 Mack Brown Texas 29 21 238 117 0.67 0.619 Bo Schembechler Michigan 27 17 234 65 0.775 0.294 Hayden Fry Iowa 37 17 230 180 0.56 0.441 Frank Beamer Virginia Tech 27 21 224 109 0.672 0.429 Steve Spurrier South Carolina 24 19 219 79 0.733 0.474 Woody Hayes Ohio State 28 11 205 61 0.761 0.455 Don Nehlen West Virginia 30 13 202 128 0.609 0.308 Vince Dooley Georgia 25 20 201 77 0.715 0.45 Dan McGugin Vanderbilt 30 0 197 55 0.762 0 John Cooper Ohio State 24 14 192 84 0.691 0.357 Dana Bible Texas 31 4 190 69 0.715 0.875 John Vaught Mississippi 25 18 190 61 0.745 0.556 George Welsh Virginia 28 15 189 132 0.588 0.333 Howard Jones S,California 28 5 188 63 0.732 1 Jess Neely Rice 36 7 187 159 0.539 0.571 Johnny Majors Tennessee 29 16 185 137 0.572 0.563 Darrell Royal Texas 23 16 184 60 0.749 0.531 Dick Tomey San Jose State 29 8 183 145 0.557 0.625 Coach Last School C-t R-c-c Wins Losses W-L% Per. Jerry Claiborne Kentucky 28 11 179 122 0.592 0.273 Jackie Sherrill Mississippi State 26 14 179 121 0.595 0.571 Bill Snyder Kansas State 22 15 178 90 0.664 0.467 Frank Kush Arizona State 22 7 176 54 0.764 0.857 Ralph Jordan Auburn 25 12 175 83 0.674 0.417 Don James Washington 22 15 175 79 0.687 0.667 Gary Pinkel Missouri 23 9 175 100 0.635 0.556 Bob Neyland Tennessee 21 7 173 31 0.829 0.286 Dan Devine Notre Dame 22 10 172 57 0.742 0.7 George Woodruff Georgia 17 0 172 41 0.803 0 Wallace Wade Duke 24 5 171 49 0.765 0.5 Nick Saban Alabama 18 14 170 57 0.748 0.571 Fisher DeBerry Air Force 23 12 169 109 0.608 0.5 Jim Sweeney Fresno State 27 7 169 134 0.557 0.714 Ken Hatfield Rice 27 10 168 140 0.545 0.4 Bill Mallory Indiana 27 10 167 130 0.561 0.4 Red Blaik Army 25 0 166 48 0.759 0 Bobby Dodd Georgia Tech 22 13 165 64 0.713 0.692

<!-- b000438 | furniture | pages [35] -->
Team #26160                                                             Page 34 of 35

<!-- b000440 | heading | pages [35] -->
4. Scores and ranks for basketball coaches of two models

<!-- b000441 | prose | pages [35] -->
Grey Grey Fuzzy Fuzzy

<!-- b000442 | heading | pages [35] -->
C Rank

<!-- b000443 | prose | pages [35] -->
Coach Last School Scores Rank Scores Rank 1 Harry Statham McKendree 0.834 1 4.1557 1 2 Danny Miles OIT 0.718 2 3.9156 3 3 Herb Magee† Philadelphia College 0.710 3 3.9668 2 4 Mike Krzyzewski Duke 0.662 4 3.8072 5 5 Jim Boeheim Syracuse 0.585 7 3.3622 8 6 Bob Knight Texas Tech 0.613 5 3.4184 7 7 Dean Smith North Carolina 0.599 6 3.6367 6 8 Jim Calhoun Connecticut 0.570 8 2.9767 11 9 Adolph Rupp Kentucky 0.540 9 3.9068 4 10 Eddie Sutton San Francisco 0.517 11 2.87 13 11 Lefty Driesell Georgia State 0.474 13 2.6173 17 12 Lute Olson Arizona 0.507 12 2.9044 12 13 Lou Henson Illinois 0.519 10 2.5534 18 14 Jerry Tarkanian Fresno State 0.429 21 3.29 9 15 E.A. Diddle Western Kentucky 0.417 24 2.6462 16 16 Hank Iba Oklahoma State 0.462 15 2.2568 21 17 Ray Meyer DePaul 0.468 14 2.4118 19 18 Phog Allen Central Missouri 0.457 16 2.7158 14 19 Don Haskins Texas-El Paso 0.444 19 2.1717 22 20 Roy Williams North Carolina 0.437 20 3.0161 10

<!-- b000444 | furniture | pages [36] -->
Team #26160                                                             Page 35 of 35

<!-- b000445 | heading | pages [36] -->
5. Scores and ranks for football coaches of two models

<!-- b000446 | prose | pages [36] -->
Grey Grey Fuzzy Fuzzy

<!-- b000447 | heading | pages [36] -->
C Rank

<!-- b000448 | prose | pages [36] -->
Coach Last School Scores Rank Scores Rank

<!-- b000449 | prose | pages [36] -->
1 Joe Paterno Penn State 0.834 1 4.715 2 2 Bobby Bowden Florida State 0.737 2 4.805 1 3 Bear Bryant Alabama 0.647 3 4.579 3 4 Pop Warner Temple 0.513 5 3.407 5 5 Amos Alonzo Stagg Chicago 0.397 13 2.725 11 6 LaVell Edwards Brigham Young 0.468 9 2.987 7 7 Tom Osborne Nebraska 0.498 6 3.779 4 8 Lou Holtz South Carolina 0.525 4 2.795 10 9 Mack Brown Texas 0.492 7 2.839 9 10 Bo Schembechler Michigan 0.410 12 3.358 6 11 Hayden Fry Iowa 0.487 8 2.309 14 12 Frank Beamer Virginia Tech 0.431 10 2.352 13 13 Steve Spurrier South Carolina 0.415 11 2.480 12 14 Woody Hayes Ohio State 0.388 14 2.964 8 15 Don Nehlen West Virginia 0.361 15 1.755 15

<!-- b000450 | heading | pages [36] -->
6. Scores and ranks for field hockey coaches of two models

<!-- b000451 | heading | pages [36] -->
C Rank

<!-- b000452 | prose | pages [36] -->
Coach Grey Scores Grey Rank Fuzzy Scores Fuzzy Rank

<!-- b000453 | prose | pages [36] -->
1 Jan Hutchinson 0.847 1 4.222 1

<!-- b000454 | prose | pages [36] -->
2 Beth Anders 0.638 7 3.605 5

<!-- b000455 | prose | pages [36] -->
3 Nancy Stevens 0.694 3 3.754 3

<!-- b000456 | prose | pages [36] -->
4 Karen Shelton 0.652 6 3.384 6

<!-- b000457 | prose | pages [36] -->
5 Jan Trapp 0.735 2 3.918 2

<!-- b000458 | prose | pages [36] -->
6 Pat Rudy 0.663 5 3.715 4

<!-- b000459 | prose | pages [36] -->
7 Sharon Pfluger 0.674 4 3.281 7

<!-- b000460 | prose | pages [36] -->
8 Enza Steele 0.553 11 2.797 9

<!-- b000461 | prose | pages [36] -->
9 Missy Meharg 0.560 9 2.527 11

<!-- b000462 | prose | pages [36] -->
10 Charlene Morett 0.527 12 2.552 10

<!-- b000463 | prose | pages [36] -->
11 Bertie Landes 0.637 8 2.900 8

<!-- b000464 | prose | pages [36] -->
12 Dawn Chamberlin 0.555 10 2.406 12

<!-- b000465 | prose | pages [36] -->
13 Sally Starr 0.426 14 1.865 15

<!-- b000466 | prose | pages [36] -->
14 Brenda Meese 0.412 15 2.004 14

<!-- b000467 | prose | pages [36] -->
15 Sally Scatton 0.472 13 2.200 13
