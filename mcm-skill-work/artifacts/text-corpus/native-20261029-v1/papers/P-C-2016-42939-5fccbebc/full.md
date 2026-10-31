# P-C-2016-42939-5fccbebc

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For ofﬁce use only

<!-- b000003 | prose | pages [1] -->
For ofﬁce use only

<!-- b000004 | title | pages [1] -->
42939

<!-- b000005 | prose | pages [1] -->
T1

<!-- b000006 | prose | pages [1] -->
F1

<!-- b000007 | prose | pages [1] -->
T2

<!-- b000008 | prose | pages [1] -->
F2

<!-- b000009 | prose | pages [1] -->
T3

<!-- b000010 | prose | pages [1] -->
F3

<!-- b000011 | prose | pages [1] -->
Problem Chosen

<!-- b000012 | prose | pages [1] -->
T4

<!-- b000013 | prose | pages [1] -->
F4

<!-- b000014 | title | pages [1] -->
C

<!-- b000015 | heading | pages [1] -->
2016 Mathematical Contest in Modeling (MCM) Summary Sheet

<!-- b000016 | prose | pages [1] -->
(Attach a copy of this page to each copy of your solution paper.)

<!-- b000017 | heading | pages [1] -->
Summary

<!-- b000018 | prose | pages [1] -->
In order to determine the optimal donation strategy, this paper proposes a data- motivated model based on an original deﬁnition of return on investment (ROI) appropriate for charitable organizations.

<!-- b000019 | prose | pages [1] -->
First, after addressing missing data, we develop a composite index, called the performance index, to quantify students’ educational performance. The perfor- mance index is a linear composition of several commonly used performance indi- cators, like graduation rate and graduates’ earnings. And their weights are deter- mined by principal component analysis.

<!-- b000020 | prose | pages [1] -->
Next, to deal with problems caused by high-dimensional data, we employ a lin- ear model and a selection method called post-LASSO to select variables that statis- tically signiﬁcantly affect the performance index and determine their effects (coef- ﬁcients). We call them performance contributing variables. In this case, 5 variables are selected. Among them, tuition & fees in 2010 and Carnegie High-Research- Activity classiﬁcation are insusceptible to donation amount. Thus we only con- sider percentage of students who receive a Pell Grant, share of students who are part-time and student-to-faculty ratio.

<!-- b000021 | prose | pages [1] -->
Then, a generalized adaptive model is adopted to estimate the relation between these 3 variables and donation amount. We ﬁt the relation across all institutions and get a ﬁtted function from donation amount to values of performance contributing variables. Then we divide the impact of donation amount into 2 parts: homogenous and heterogenous one. The homogenous inﬂuence is modeled as the change in ﬁt- ted values of performance contributing variables over increase in donation amount, which can be predicted from the ﬁtted curve. The heterogenous one is modeled as a tuning parameter which adjusts the homogenous inﬂuence based on deviation from the ﬁtted curve. And their product is increase in true values of performance over increase in donation amount.

<!-- b000022 | prose | pages [1] -->
Finally, we calculate ROI, deﬁned as increase in performance index over in- crease in donation amount. This ROI is institution-speciﬁc and dependent on in- crease in donation amount. By adopting a two-step ROI maximization algorithm, we determine the optimal investment strategy.

<!-- b000023 | prose | pages [1] -->
Also, we propose an extended model to handle problems caused by time dura- tion and geographical distribution of donations.

<!-- b000024 | furniture | pages [2] -->
Team # 42939

<!-- b000025 | furniture | pages [2] -->
Page 1 of 24

<!-- b000026 | prose | pages [2] -->
A Letter to the CFO of the Goodgrant Foundation

<!-- b000027 | prose | pages [2] -->
Dear Chiang,

<!-- b000028 | prose | pages [2] -->
Our team has proposed a performance index quantifying the students’ educational per- formance of each institution and deﬁned the return of investment (ROI) appropriately for a charitable organization like Goodgrant Foundation. A mathematical model is built to help predict the return of investment after identifying the mechanism through which the donation generates its impact on the performance. The optimal investment strategy is determined by maximizing the estimated return of investment.

<!-- b000029 | prose | pages [2] -->
More speciﬁcally, the composite performance index is developed after taking all the pos- sible performance indicators into consideration, like graduation rate and graduates’ earnings. The performance index is constructed to represents the performance of the school as well as the positive effect that a college brings to students and the community. From this point of view, our deﬁnition manages to capture social beneﬁts of donation.

<!-- b000030 | prose | pages [2] -->
And then we adopt a variable selection method to ﬁnd out performance contributing vari- ables, which are variables that strongly affect the performance index. Among all the perfor- mance contributing variables we select, three variables which can be directly affected by your generous donation are kept to predict ROI: percentage of students who receive a Pell Grant, share of students who are part-time and student-to-faculty ratio.

<!-- b000031 | prose | pages [2] -->
We ﬁtted a relation between these three variables and the donation amount to predict change in value of each performance contributing variable over your donation amount. And we calculate ROI, deﬁned as increase in the performance index over your donation amount, by multiplying change in value of each performance contributing variable over your donation amount and each performance contributing variable’s effect on performance index, and then summing up the products of all performance contributing variables. The optimal investment strategy is decided after maximizing the return of investment according to an algorithm for selection.

<!-- b000032 | prose | pages [2] -->
In conclusion, our model successfully produced an investment strategy including a list of target institutions and investment amount for each institution. (The list of year 1 is attached at the end of the letter). The time duration for the investment could also be determined based on our model. Since the model as well as the evaluation approach is fully data-motivated with no arbitrary criterion included, it is rather adaptable for solving future philanthropic educational investment problems.

<!-- b000033 | prose | pages [2] -->
We have a strong belief that our model can effectively enhance the efﬁciency of philan- thropic educational investment and provides an appropriate as well as feasible way to best improve the educational performance of students.

<!-- b000034 | prose | pages [2] -->
UNITID names ROI donation United States Merchant Marine Academy 197027 21.85% 2500000 AVTEC-Alaska’s Institute of Technology 102711 21.26% 7500000 Institute of American Indian and Alaska Native Culture 187745 262129 New College of Florida 20.99% 2000000 20.69% 6500000 Thaddeus Stevens College of Technology 216296 229832 Western Texas College 196158 SUNY at Fredonia 234155 Virginia State University 196200 SUNY College at Potsdam 178615 Truman State University 20.66% 3000000 20.26% 10000000 20.24% 5500000 20.04% 10000000 19.75% 5000000 19.60% 3000000 University of North Carolina at Chapel Hill 199120 101648 Marion Military Institute 19.51% 3000000 19.48% 2500000

<!-- b000035 | furniture | pages [3] -->
Team # 42939

<!-- b000036 | prose | pages [3] -->
187912 New Mexico Military Institute 227386 Panola College 434584 Ilisagvik College

<!-- b000037 | furniture | pages [3] -->
Page 2 of 24

<!-- b000038 | prose | pages [3] -->
19.31% 500000 19.28% 10000000 19.19% 4500000 University of North Carolina School of the Arts 199184 19.15% 500000 East San Gabriel Valley Regional Occupational Program 413802 174251 University of Minnesota-Morris 19.09% 6000000 19.09% 8000000 Louisiana State University and Agricultural & Mechanical Col- 159391 lege

<!-- b000039 | prose | pages [3] -->
403487 Wabash Valley College

<!-- b000040 | prose | pages [3] -->
Yours Sincerely,

<!-- b000041 | furniture | pages [3] -->
Team #42939

<!-- b000042 | prose | pages [3] -->
19.07% 8500000

<!-- b000043 | prose | pages [3] -->
19.05% 1500000

<!-- b000044 | furniture | pages [4] -->
Team # 42939

<!-- b000045 | furniture | pages [4] -->
Page 3 of 24

<!-- b000046 | prose | pages [4] -->
An Optimal Strategy of Donation

<!-- b000047 | prose | pages [4] -->
for Educational Purpose

<!-- b000048 | prose | pages [4] -->
Control Number: #42939

<!-- b000049 | prose | pages [4] -->
February , 2016

<!-- b000050 | furniture | pages [5] -->
Team # 42939

<!-- b000051 | furniture | pages [5] -->
Page 4 of 24

<!-- b000052 | heading | pages [5] -->
Contents

<!-- b000053 | contents | pages [5] -->
1

<!-- b000054 | heading | pages [5] -->
Introduction

<!-- b000055 | prose | pages [5] -->
5

<!-- b000056 | prose | pages [5] -->
Statement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 5

<!-- b000057 | prose | pages [5] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 Baseline Model 5

<!-- b000058 | prose | pages [5] -->
Detailed Deﬁnitions & Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3 8

<!-- b000059 | prose | pages [5] -->
Detailed Deﬁnitions: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3.1 8

<!-- b000060 | prose | pages [5] -->
Assumptions: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3.2 9

<!-- b000061 | prose | pages [5] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.4 The Advantages of Our Model

<!-- b000062 | prose | pages [5] -->
2 Addressing the Missing Values

<!-- b000063 | prose | pages [5] -->
3 Determining the Performance Index

<!-- b000064 | prose | pages [5] -->
9

<!-- b000065 | prose | pages [5] -->
9

<!-- b000066 | prose | pages [5] -->
10

<!-- b000067 | prose | pages [5] -->
Performance Indicators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 10

<!-- b000068 | prose | pages [5] -->
Performance Index via Principal-Component Factors 3.2 . . . . . . . . . . . . . . . .

<!-- b000069 | prose | pages [5] -->
10

<!-- b000070 | prose | pages [5] -->
Identifying Performance Contributing Variables via post-LASSO 4 11

<!-- b000071 | prose | pages [5] -->
Determining Investment Strategy based on ROI 5 13

<!-- b000072 | prose | pages [5] -->
Fitted Curve between Performance Contributing Variables and Donation Amount 14 5.1

<!-- b000073 | prose | pages [5] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2 ROI(Return on Investment) 15

<!-- b000074 | prose | pages [5] -->
Model of Fitted ROIs of Performance Contributing Variables fROIi 5.2.1 . . .

<!-- b000075 | prose | pages [5] -->
15

<!-- b000076 | prose | pages [5] -->
Model of the tuning parameter Pi 5.2.2 . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000077 | prose | pages [5] -->
16

<!-- b000078 | prose | pages [5] -->
Calculation of ROI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2.3

<!-- b000079 | prose | pages [5] -->
5.3 School Selection & Investment Strategy

<!-- b000080 | prose | pages [5] -->
6

<!-- b000081 | heading | pages [5] -->
Extended Model

<!-- b000082 | prose | pages [5] -->
17

<!-- b000083 | prose | pages [5] -->
. . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000084 | prose | pages [5] -->
18

<!-- b000085 | prose | pages [5] -->
18

<!-- b000086 | prose | pages [5] -->
Time Duration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 18

<!-- b000087 | prose | pages [5] -->
Geographical Distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2

<!-- b000088 | prose | pages [5] -->
7

<!-- b000089 | heading | pages [5] -->
Conclusions and Discussion

<!-- b000090 | prose | pages [5] -->
8 Reference

<!-- b000091 | prose | pages [5] -->
9

<!-- b000092 | heading | pages [5] -->
Appendix

<!-- b000093 | prose | pages [5] -->
22

<!-- b000094 | prose | pages [5] -->
22

<!-- b000095 | prose | pages [5] -->
23

<!-- b000096 | prose | pages [5] -->
24

<!-- b000097 | furniture | pages [6] -->
Team # 42939

<!-- b000098 | furniture | pages [6] -->
Page 5 of 24

<!-- b000099 | prose | pages [6] -->
1

<!-- b000100 | heading | pages [6] -->
Introduction

<!-- b000101 | prose | pages [6] -->
1.1 Statement of the Problem

<!-- b000102 | prose | pages [6] -->
There exists no doubt in the signiﬁcance of postsecondary education to the development of society, especially with the ascending need for skilled employees capable of complex work. Nevertheless, U.S. ranks only 11th in the higher education attachment worldwide, which makes the ﬁnancial support from large charitable organizations necessary.

<!-- b000103 | prose | pages [6] -->
As it’s essential for charitable organizations to maximize the effectiveness of donations, an objective and systematic assessment model is in demand to develop appropriate investment strategies. To achieve this goal, several large foundations like Gates Foundation and Lumina Foundation have developed different evaluation approaches, where they mainly focus on spe- ciﬁc indexes like attendance and graduation rate. In other empirical literature, a Forbes ap- proach (Shifrin and Chen,2015) proposes a new indicator called the Grateful Graduates Index, using the median amount of private donations per student over a 10-year period to measure the return on investment. Also, performance funding indicators (Burke,2002, Cave,1997, Ser- ban and Burke,1998,Banta et al,1996), which include but are not limited to external indicators like graduates’ employment rate and internal indicators like teaching quality, are one of the most prevailing methods to evaluate effectiveness of educational donations.

<!-- b000104 | prose | pages [6] -->
However, those methods also arise with widely acknowledged concerns (Burke,1998). Most of them require subjective choice of indexes and are rather arbitrary than data-based. And they perform badly in a data environment where there is miscellaneous cross-section data but scarce time-series data. Besides, they lack quantiﬁed analysis in precisely predicting or measuring the social beneﬁts and the positive effect that the investment can generate, which serves as one of the targets for the Goodgrant Foundation.

<!-- b000105 | prose | pages [6] -->
In accordance with Goodgrant Foundation’s request, this paper provides a prudent def- inition of return on investment (ROI) for charitable organizations, and develops an original data-motivated model, which is feasible even faced with tangled cross-section data and absent time-series data, to determine the optimal strategy for funding. The strategy contains selection of institutions and distribution of investment across institutions, time and regions.

<!-- b000106 | prose | pages [6] -->
1.2

<!-- b000107 | heading | pages [6] -->
Baseline Model

<!-- b000108 | prose | pages [6] -->
Our deﬁnition of ROI is similar to its usual meaning, which is the increase in students’ educational performance over the amount Goodgrant Foundation donates (assuming other donations ﬁxed, it’s also the increase in total donation amount).

<!-- b000109 | prose | pages [6] -->
First we cope with data missingness. Then, to quantify students’ educational performance, we develop an index called performance index, which is a linear composition of commonly used performance indicators.

<!-- b000110 | prose | pages [6] -->
Our major task is to build a model to predict the change of this index given a distribution of Goodgrant Foundation $100m donation. However, donation does not directly affect the performance index and we would encounter endogeneity problem or neglect effects of other variables if we solely focus on the relation between performance index and donation amount. Instead, we select several variables that are pivotal in predicting the performance index from many potential candidates, and determine their coefﬁcients/effects on the performance index. We call these variables performance contributing variables.

<!-- b000111 | prose | pages [6] -->
Due to absence of time-series data, it becomes difﬁcult to ﬁgure out how performance con-

<!-- b000112 | furniture | pages [7] -->
Team # 42939

<!-- b000113 | furniture | pages [7] -->
Page 6 of 24

<!-- b000114 | prose | pages [7] -->
tributing variables are affected by donation amount for each institution respectively. Instead, we ﬁt the relation between performance contributing variables and donation amount across all institutions and get a ﬁtted function from donation amount to values of performance contribut- ing variables.

<!-- b000115 | prose | pages [7] -->
Then we divide the impact of donation amount into 2 parts: homogenous and heteroge- nous one. The homogenous inﬂuence is modeled as the change in ﬁtted values of performance contributing variables over increase in donation amount (We call these quotients ﬁtted ROI of performance contributing variable). The heterogenous one is modeled as a tuning parameter, which adjusts the homogenous inﬂuence based on deviation from the ﬁtted function. And their product is the institution-speciﬁc increase in true values of performance contributing variables over increase in donation amount (We call these values ROI of performance contributing vari- able).

<!-- b000116 | prose | pages [7] -->
The next step is to calculate the ROI of the performance index by adding the products of ROIs of performance contributing variables and their coefﬁcients on the performance index. This ROI is institution-speciﬁc and dependent on increase in donation amount. By adopting a two-step ROI maximization algorithm, we determine the optimal investment strategy.

<!-- b000117 | prose | pages [7] -->
Also, we propose an extended model to handle problems caused by time duration and geographical distribution of donations.

<!-- b000118 | prose | pages [7] -->
Note: we only use data from the provided excel table and that mentioned in the pdf ﬁle.

<!-- b000119 | caption | pages [7] -->
Table 1: Data Source

<!-- b000120 | prose | pages [7] -->
Variable

<!-- b000121 | prose | pages [7] -->
Performance index

<!-- b000122 | prose | pages [7] -->
Dataset

<!-- b000123 | prose | pages [7] -->
Excel table

<!-- b000124 | prose | pages [7] -->
Performance contributing variables

<!-- b000125 | prose | pages [7] -->
Donation amount

<!-- b000126 | prose | pages [7] -->
Excel table and pdf ﬁle

<!-- b000127 | prose | pages [7] -->
Pdf ﬁle

<!-- b000128 | prose | pages [7] -->
The ﬂow chart of the whole model is presented below in Fig 1:

<!-- b000129 | furniture | pages [8] -->
Team # 42939

<!-- b000130 | furniture | pages [8] -->
Page 7 of 24

<!-- b000131 | caption | pages [8] -->
Figure 1: Flow Chart Demonstration of the Model

<!-- b000132 | furniture | pages [9] -->
Team # 42939

<!-- b000133 | furniture | pages [9] -->
Page 8 of 24

<!-- b000134 | prose | pages [9] -->
1.3

<!-- b000135 | heading | pages [9] -->
Detailed Deﬁnitions & Assumptions

<!-- b000136 | prose | pages [9] -->
1.3.1 Detailed Deﬁnitions:

<!-- b000137 | furniture | pages [10] -->
Team # 42939

<!-- b000138 | furniture | pages [10] -->
Page 9 of 24

<!-- b000139 | prose | pages [10] -->
1.3.2

<!-- b000140 | heading | pages [10] -->
Assumptions:

<!-- b000141 | prose | pages [10] -->
A1. Stability. We assume data of any institution should be stable without the impact from

<!-- b000142 | prose | pages [10] -->
outside. To be speciﬁc, the key factors like the donation amount and the performance index should remain unchanged if the college does not receive new donations.

<!-- b000143 | prose | pages [10] -->
A2. Goodgrant Foundation’s donation (Increase in donation amount) is discrete rather than

<!-- b000144 | prose | pages [10] -->
continuous. This is reasonable because each donation is usually an integer multiple of a minimum amount, like $1m. After referring to the data of other foundations like Lumina Foundation, we recommend donation amount should be one value in the set below:

<!-- b000145 | prose | pages [10] -->
{500000, 1000000, 1500000, ..., 10000000}

<!-- b000146 | prose | pages [10] -->
A3. The performance index is a linear composition of all given performance indicators.

<!-- b000147 | prose | pages [10] -->
A4. Performance contributing variables linearly affect the performance index.

<!-- b000148 | prose | pages [10] -->
A5. Increase in donation amount affects the performance index through performance con-

<!-- b000149 | prose | pages [10] -->
tributing variables.

<!-- b000150 | prose | pages [10] -->
A6. The impact of increase in donation amount on performance contributing variables con-

<!-- b000151 | prose | pages [10] -->
tains 2 parts: homogenous one and heterogenous one. The homogenous inﬂuence is repre- sented by a smooth function from donation amount to performance contributing variables. And the heterogenous one is represented by deviation from the function.

<!-- b000152 | prose | pages [10] -->
1.4

<!-- b000153 | heading | pages [10] -->
The Advantages of Our Model

<!-- b000154 | prose | pages [10] -->
Our model exhibits many advantages in application:

<!-- b000155 | prose | pages [10] -->
• The evaluation model is fully data based with few subjective or arbitrary decision rules.

<!-- b000156 | prose | pages [10] -->
• Our model successfully identiﬁes the underlying mechanism instead of merely focusing on the relation between donation amount and the performance index.

<!-- b000157 | prose | pages [10] -->
• Our model takes both homogeneity and heterogeneity into consideration.

<!-- b000158 | prose | pages [10] -->
• Our model makes full use of the cross-section data and does not need time-series data to produce reasonable outcomes.

<!-- b000159 | prose | pages [10] -->
2 Addressing the Missing Values

<!-- b000160 | prose | pages [10] -->
The provided datasets suffer from severe data missing, which could undermine the reliabil- ity and interpretability of any results. To cope with this problem, we adopt several different methods for data with varied missing rate.

<!-- b000161 | prose | pages [10] -->
For data with missing rate over 50%, any current prevailing method would fall victim to under- or over-randomization. As a result, we omit this kind of data for simplicity’s sake.

<!-- b000162 | prose | pages [10] -->
For variables with missing rate between 10%-50%, we use imputation techniques (Little and Rubin, 2014) where a missing value was imputed from a randomly selected similar record, and model-based analysis where missing values are substituted with distribution diagrams.

<!-- b000163 | furniture | pages [11] -->
Team # 42939

<!-- b000164 | furniture | pages [11] -->
Page 10 of 24

<!-- b000165 | prose | pages [11] -->
For variables with missing rate under 10%, we address missingness by simply replace miss- ing value with mean of existing values.

<!-- b000166 | prose | pages [11] -->
3 Determining the Performance Index

<!-- b000167 | prose | pages [11] -->
In this section, we derive a composite index, called the performance index, to evaluate the educational performance of students at every institution.

<!-- b000168 | prose | pages [11] -->
3.1 Performance Indicators

<!-- b000169 | prose | pages [11] -->
First, we need to determine which variables from various institutional performance data are direct indicators of Goodgrant Foundation’s major concern – to enhance students’ educational performance.

<!-- b000170 | prose | pages [11] -->
In practice, other charitable foundations such as Gates Foundation place their focus on core indexes like attendance and graduation rate. Logically, we select performance indicators on the basis of its correlation with these core indexes. With this method, miscellaneous performance data from the excel table boils down to 4 crucial variables. C150_4_POOLED_SUPP and C200_L4_POOLED_SUPP, as completion rates for different types of institutions, are directly correlated with graduation rate. We combine them into one variable.Md_earn_wne_p10 and gt_25k_p6, as different measures of graduates’ earnings, are proved in empirical studies (Ehren- berg,2004) to be highly dependent on educational performance. And RPY _3Y R_RT_SUPP, as repayment rate, is also considered valid in the same sense. Let them be Y1, Y2, Y3 and Y4.

<!-- b000171 | prose | pages [11] -->
For easy calculation and interpretation of the performance index, we apply uniformization to all 4 variables, as to make sure they’re on the same scale (from 0 to 100).

<!-- b000172 | prose | pages [11] -->
3.2 Performance Index via Principal-Component Factors

<!-- b000173 | prose | pages [11] -->
As the model assumes the performance index is a linear composition of all performance indicators, all we need to do is determine the weights of these variables.

<!-- b000174 | prose | pages [11] -->
Here we apply the method of Customer Satisfaction Index model (Rogg et al,2001), where principal-component factors (pcf) are employed to determine weights of all aspects.

<!-- b000175 | prose | pages [11] -->
The pcf procedure uses an orthogonal transformation to convert a set of observations of pos- sibly correlated variables into a set of values of linearly uncorrelated variables called principal- component factors, each of which carries part of the total variance. If the cumulative proportion of the variance exceeds 80%, it’s viable to use corresponding pcfs (usually the ﬁrst two pcfs) to determine weights of original variables.

<!-- b000176 | prose | pages [11] -->
In this case, we’ll get 4 pcfs (named PCF1, PCF2, PCF3 and PCF4). First, the procedure provides the linear coefﬁcients of Ym in the expression of PCF1 and PCF2. We get

<!-- b000177 | prose | pages [11] -->
PCF1 = a11Y1 + a12Y2 + a13Y3 + a14Y4

<!-- b000178 | prose | pages [11] -->
PCF2 = a21Y1 + a22Y2 + a23Y3 + a24Y4

<!-- b000179 | prose | pages [11] -->
(akm calculated as corresponding factor loadings over square root of factor k’s eigenvalue) Then, we calculate the rough weights cm for Ym. Let the variance proportions PCF1 and PCF2 represent be N1 and N2. We get cm = (a1mN1 +a2mN2)/(N1 +N2) (This formulation is justiﬁed

<!-- b000180 | furniture | pages [12] -->
Team # 42939

<!-- b000181 | furniture | pages [12] -->
Page 11 of 24

<!-- b000182 | prose | pages [12] -->
because the variance proportions can be viewed as the signiﬁcance of pcfs). If we let perfor- mance index= (PCF1N1 + PCF2N2)/(N1 + N2), cm is indeed the rough weight of Ym in terms of variance) Next, we get the weights by adjusting the sum of rough weights to 1:

<!-- b000183 | prose | pages [12] -->
cm = cm/(c1 + c2 + c3 + c4)

<!-- b000184 | prose | pages [12] -->
Finally, we get the performance index, which is the weighted sum of the 4 performance indicator. Performance index=P

<!-- b000185 | prose | pages [12] -->
m(cmYm)

<!-- b000186 | caption | pages [12] -->
Table 2 presents the 10 institutions with largest values of the performance index. This rank-

<!-- b000187 | prose | pages [12] -->
ing is highly consistent with widely acknowledged rankings, like QS ranking, which indicates the validity of the performance index.

<!-- b000188 | caption | pages [12] -->
Table 2: The Top 10 Institutions in Terms of Performance Index

<!-- b000189 | prose | pages [12] -->
Institution Performance index

<!-- b000190 | prose | pages [12] -->
Los Angeles County College of Nursing and Allied Health

<!-- b000191 | prose | pages [12] -->
Massachusetts Institute of Technology

<!-- b000192 | prose | pages [12] -->
University of Pennsylvania

<!-- b000193 | prose | pages [12] -->
Babson College

<!-- b000194 | prose | pages [12] -->
Georgetown University

<!-- b000195 | prose | pages [12] -->
Stanford University

<!-- b000196 | prose | pages [12] -->
Duke University

<!-- b000197 | prose | pages [12] -->
University of Notre Dame

<!-- b000198 | prose | pages [12] -->
Weill Cornell Medical College

<!-- b000199 | prose | pages [12] -->
79.60372162

<!-- b000200 | prose | pages [12] -->
79.06066895

<!-- b000201 | prose | pages [12] -->
79.05044556

<!-- b000202 | prose | pages [12] -->
78.99269867

<!-- b000203 | prose | pages [12] -->
78.90468597

<!-- b000204 | prose | pages [12] -->
78.70586395

<!-- b000205 | prose | pages [12] -->
78.27719116

<!-- b000206 | prose | pages [12] -->
78.15843964

<!-- b000207 | prose | pages [12] -->
78.14334106

<!-- b000208 | prose | pages [12] -->
Identifying Performance Contributing Variables via post-LASSO 4

<!-- b000209 | prose | pages [12] -->
The next step of our model requires identifying the factors that may exert an inﬂuence on the students’ educational performance from a variety of variables mentioned in the excel table and the pdf ﬁle (108 in total, some of which are dummy variables converted from categorical variables).To achieve this purpose, we used a model called LASSO. A linear model is adopted to describe the relationship between the endogenous variable – performance index – and all variables that are potentially inﬂuential to it. We assign appropriate coefﬁcient to each variable to minimize the square error between our model prediction and the actual value when ﬁtting the data.

<!-- b000210 | prose | pages [12] -->
J

<!-- b000211 | prose | pages [12] -->
1

<!-- b000212 | prose | pages [12] -->
X

<!-- b000213 | prose | pages [12] -->
min

<!-- b000214 | prose | pages [12] -->
J

<!-- b000215 | prose | pages [12] -->
β

<!-- b000216 | prose | pages [12] -->
j=1

<!-- b000217 | prose | pages [12] -->
where J = 2881,xj = (1, x1j, x2j, ..., xpj)T

<!-- b000218 | prose | pages [12] -->
(yj −xT

<!-- b000219 | prose | pages [12] -->
j β)2

<!-- b000220 | prose | pages [12] -->
However, as the amount of the variables included in the model is increasing, the cost func- tion will naturally decrease. So the problem of over ﬁtting the data will arise, which make the model we come up with hard to predict the future performance of the students. Also, since there are hundreds of potential variables as candidates. We need a method to identify the variables that truly matter and have a strong effect on the performance index.

<!-- b000221 | prose | pages [12] -->
Here we take the advantage of a method named post-LASSO (Tibshirani,1996). LASSO, also known as the least absolute shrinkage and selection operator, is a method used for variable

<!-- b000222 | furniture | pages [13] -->
Team # 42939

<!-- b000223 | furniture | pages [13] -->
Page 12 of 24

<!-- b000224 | prose | pages [13] -->
selection and shrinkage in medium- or high-dimensional environment. And post-LASSO is to apply ordinary least squares (OLS) to the model selected by ﬁrst-step LASSO procedure. In LASSO procedure, instead of using the cost function that merely focusing on the square error between the prediction and the actual value, a penalty term is also included into the objective function. We wish to minimize:

<!-- b000225 | prose | pages [13] -->
J

<!-- b000226 | prose | pages [13] -->
1

<!-- b000227 | prose | pages [13] -->
j β)2 + λ||β||1

<!-- b000228 | prose | pages [13] -->
X

<!-- b000229 | prose | pages [13] -->
(yj −xT

<!-- b000230 | prose | pages [13] -->
min

<!-- b000231 | prose | pages [13] -->
J

<!-- b000232 | prose | pages [13] -->
β

<!-- b000233 | prose | pages [13] -->
j=1

<!-- b000234 | prose | pages [13] -->
where λ||β||1 is the penalty term. The penalty term takes the number of variables into con- sideration by penalizing on the absolute value of the coefﬁcients and forcing the coefﬁcients of many variables shrink to zero if this variable is of less importance. The penalty coefﬁcient lambda determines the degree of penalty for including variables into the model. After min- imizing the cost function plus the penalty term, we could ﬁgure out the variables of larger essence to include in the model.

<!-- b000235 | prose | pages [13] -->
We utilize the LARS algorithm to implement the LASSO procedure and cross-validation MSE minimization (Usai et al,2009) to determine the optimal penalty coefﬁcient (represented by shrinkage factor in LARS algorithm). And then OLS is employed to complete the post- LASSO method.

<!-- b000236 | caption | pages [13] -->
Figure 2: LASSO path-coefﬁcients as a function of shrinkage factor s

<!-- b000237 | caption | pages [13] -->
Figure 3: Cross-validated MSE

<!-- b000238 | furniture | pages [14] -->
Team # 42939

<!-- b000239 | furniture | pages [14] -->
Page 13 of 24

<!-- b000240 | prose | pages [14] -->
Fig 2. displays the results of LASSO procedure and Fig 3 displays the cross-validated MSE for different shrinkage factors. As speciﬁed above, the cross-validated MSE reaches minimum with shrinkage factor between 0.4-0.8. We choose 0.6 and ﬁnd in Fig 2 that 6 variables have nonzero coefﬁcients via the LASSO procedure, thus being selected as the performance con- tributing variables. Table 3 is a demonstration of these 6 variables and corresponding post- LASSO results.

<!-- b000241 | caption | pages [14] -->
Table 3: Post-LASSO results

<!-- b000242 | prose | pages [14] -->
PCTPELL

<!-- b000243 | prose | pages [14] -->
PPTUG_EF

<!-- b000244 | prose | pages [14] -->
StudentToFaculty_ratio

<!-- b000245 | prose | pages [14] -->
Tuition&Fees2010

<!-- b000246 | prose | pages [14] -->
Carnegie_HighResearchActivity

<!-- b000247 | prose | pages [14] -->
Constant

<!-- b000248 | prose | pages [14] -->
Observations R2 Adjusted R2

<!-- b000249 | prose | pages [14] -->
Note:

<!-- b000250 | prose | pages [14] -->
Dependent variable:

<!-- b000251 | prose | pages [14] -->
performance_index

<!-- b000252 | prose | pages [14] -->
−26.453∗∗∗

<!-- b000253 | prose | pages [14] -->
(0.872)

<!-- b000254 | prose | pages [14] -->
−14.819∗∗∗

<!-- b000255 | prose | pages [14] -->
(0.781)

<!-- b000256 | prose | pages [14] -->
−0.231∗∗∗

<!-- b000257 | prose | pages [14] -->
(0.025)

<!-- b000258 | prose | pages [14] -->
0.0003∗∗∗

<!-- b000259 | prose | pages [14] -->
(0.00002)

<!-- b000260 | prose | pages [14] -->
5.667∗∗∗

<!-- b000261 | prose | pages [14] -->
(0.775)

<!-- b000262 | prose | pages [14] -->
61.326∗∗∗

<!-- b000263 | prose | pages [14] -->
(0.783)

<!-- b000264 | prose | pages [14] -->
2,880 0.610 0.609

<!-- b000265 | prose | pages [14] -->
PCTPELL is percentage of students who receive a Pell Grant;PPTUG_EF is share of students who are part- time;Carnegie_HighResearchActivity is Carnegie classiﬁca- tion basic: High Research Activity

<!-- b000266 | prose | pages [14] -->
The results presented in Table 3 are consistent with common sense. For instance, the pos- itive coefﬁcient of High Research Activity Carnegie classiﬁcation implies that active research activity helps student’s educational performance; and the negative coefﬁcient of Student-to- Faculty ratio suggests that decrease in faculty quantity undermines students’ educational per- formance. Along with the large R square value and small p-value for each coefﬁcient, the post-LASSO procedure proves to select a valid set of performance contributing variables and describe well their contribution to the performance index.

<!-- b000267 | prose | pages [14] -->
Determining Investment Strategy based on ROI 5

<!-- b000268 | prose | pages [14] -->
We’ve identiﬁed 5 performance contributing variables via post-LASSO. Among them, tu- ition & fees in 2010 and Carnegie High-Research-Activity classiﬁcation are quite insusceptible to donation amount. So we only consider the effects of increase in donation amount on per- centage of students who receive a Pell Grant, share of students who are part-time and student- to-faculty ratio. We denote them with F1, F2 and F3, their post-LASSO coefﬁcients with β1,β2

<!-- b000269 | furniture | pages [15] -->
Team # 42939

<!-- b000270 | furniture | pages [15] -->
Page 14 of 24

<!-- b000271 | prose | pages [15] -->
and β3.

<!-- b000272 | prose | pages [15] -->
In this section, we ﬁrst introduce the procedure used to ﬁt the relation between performance contributing variables and donation amount. Then we provide the model employed to calcu- late ﬁtted ROIs of performance contributing variables (the homogenous inﬂuence of increase in donation amount) and the tuning parameter (the heterogenous inﬂuence of increase in dona- tion amount). Next, we introduce how to determine ROI. Lastly, we show how the maximiza- tion determines the investment strategy, including selection of institutions and distribution of investments.

<!-- b000273 | prose | pages [15] -->
5.1 Fitted Curve between Performance Contributing Variables and Donation Amount

<!-- b000274 | prose | pages [15] -->
Since we have already approximated the linear relation between the performance index with the 3 performance contributing variables, we want to know how increase in donation changes them. In this paper, we use Generalized Adaptive Model (GAM) to smoothly ﬁt the relations. Generalized Adaptive Model is a generalized linear model in which the dependent variable depends linearly on unknown smooth functions of independent variables. The ﬁtted curve of percentage of students who receive a Pell Grant is depicted below in Fig 4 (see the other two ﬁtted curves in Appendix):

<!-- b000275 | caption | pages [15] -->
Figure 4: GAM Approximation

<!-- b000276 | prose | pages [15] -->
A Pell Grant is money the U.S. federal government provides directly for students who need it to pay for college. Intuitively, if the amount of donation an institution receives from other sources such as private donation increases, the institution is likely to use these donations to alleviate students’ ﬁnancial stress, resulting in percentage of students who receive a Pell Grant. Thus it is reasonable to see a ﬁtted curve downward sloping at most part. Also, in common

<!-- b000277 | furniture | pages [16] -->
Team # 42939

<!-- b000278 | furniture | pages [16] -->
Page 15 of 24

<!-- b000279 | prose | pages [16] -->
sense, an increase in donation amount would lead to increase in the performance index. This downward sloping curve is consistent with the negative post-LASSO coefﬁcient of percentage of students who receive a Pell Grant (as two negatives make a positive).

<!-- b000280 | prose | pages [16] -->
5.2 ROI(Return on Investment)

<!-- b000281 | heading | pages [16] -->
Model of Fitted ROIs of Performance Contributing Variables fROIi

<!-- b000282 | prose | pages [16] -->
5.2.1

<!-- b000283 | caption | pages [16] -->
Figure 5: Demonstration of fROI1

<!-- b000284 | prose | pages [16] -->
Again, we use ﬁtted curve of percentage of students who receive a Pell Grant as an example. We modeled the blue ﬁtted curve to represent the homogeneous relation between percentage of students who receive a Pell Grant and donation amount.

<!-- b000285 | prose | pages [16] -->
Recall ﬁtted ROI of percentage of students who receive a Pell Grant (fROI1) is change in ﬁtted values (∆f) over increase in donation amount (∆X). So

<!-- b000286 | prose | pages [16] -->
fROI1 = ∆f/∆X

<!-- b000287 | prose | pages [16] -->
According to assumption A2, the amount of each Goodgrant Foundation’s donation falls into a pre-speciﬁed set, namely, {500000, 1000000, 1500000, ..., 10000000}. So we get a set of possible ﬁtted ROI of percentage of students who receive a Pell Grant (fROI1). Clearly, fROI1 is de- pendent on both donation amount (X) and increase in donation amount (∆X). Calculation of ﬁtted ROIs of other performance contributing variables is similar.

<!-- b000288 | furniture | pages [17] -->
Team # 42939

<!-- b000289 | furniture | pages [17] -->
Page 16 of 24

<!-- b000290 | heading | pages [17] -->
Model of the tuning parameter Pi

<!-- b000291 | prose | pages [17] -->
5.2.2

<!-- b000292 | prose | pages [17] -->
Although we’ve identiﬁed the homogenous inﬂuence of increase in donation amount, we shall not neglect the fact that institutions utilize donations differently. A proportion of do- nations might be appropriated by the university’s administration and different institutions allocate the donation differently. For example, university with a more convenient and well- maintained system of identifying students who need ﬁnancial aid might be willing to use a larger portion of donations to directly aid students, resulting in a lower percentage of under- graduate students receiving Pell grant. Also, university facing lower cost of identifying and hiring suitable faculty members might be inclined to use a larger portion of donations in this direction, resulting in a lower student-to-faculty ratio.

<!-- b000293 | prose | pages [17] -->
These above mentioned reasons make institutions deviate from the homogenous ﬁtted func- tion and presents heterogeneous inﬂuence of increase in donation amount. Thus, while the homogenous inﬂuence only depends on donation amount and increase in donation amount, the heterogeneous inﬂuence is institution-speciﬁc.

<!-- b000294 | prose | pages [17] -->
To account for this heterogeneous inﬂuence, we utilize a tuning parameter Pi to adjust the homogenous inﬂuence. By multiplying the tuning parameter, ﬁtted ROIs of performance con- tributing variables (ﬁtted value changes) convert into ROI of performance contributing variable (true value changes).

<!-- b000295 | prose | pages [17] -->
ROIi = fROIi · Pi

<!-- b000296 | prose | pages [17] -->
We then argue that Pi can be summarized by a function of deviation from the ﬁtted curve (∆h), and the function has the shape shown in Fig 6.

<!-- b000297 | prose | pages [17] -->
The value of Pi ranges from 0 to 2, because Pi can be viewed as an ampliﬁcation or shrinkage of the homogenous inﬂuence. For example, Pi=2 means that the homogeneous inﬂuence is ampliﬁed greatly. Pi =0 means that this homogeneous inﬂuence would be entirely wiped out. The shape of the function is as shown in Fig 6 because of the following reasons. Intuitively, if one institution locates above the ﬁtted line, when deviation is small, the larger it is, the larger Pi is. This is because the institution might be more inclined to utilize donations to change that factor. However, when deviation becomes even larger, the institution grows less willing to invest on this factor. This is because marginal utility decreases. The discussion is similar if one institution initially lies under the ﬁtted line. Thus, we assume the function mapping deviation to Pi is similar to Fig 6. deviation is on the x-axis while Pi is on the y-axis.

<!-- b000298 | caption | pages [17] -->
Figure 6: Function from Deviation to Pi

<!-- b000299 | prose | pages [17] -->
In order to simplify calculation and without loss of generality, we approximate the function

<!-- b000300 | furniture | pages [18] -->
Team # 42939

<!-- b000301 | furniture | pages [18] -->
Page 17 of 24

<!-- b000302 | prose | pages [18] -->
in Fig 6 by a set of linear segments, as is shown in Fig 7. The endpoints from left to right are respectively:

<!-- b000303 | prose | pages [18] -->
• (The minimum of deviations of all institutions, 2)

<!-- b000304 | prose | pages [18] -->
• (Half of the minimum of deviations of all institutions, 4/3)

<!-- b000305 | prose | pages [18] -->
• (Quarter of the minimum of deviations of all institutions, 2/3)

<!-- b000306 | prose | pages [18] -->
• (0, 1)

<!-- b000307 | prose | pages [18] -->
• (Quarter of the maximum of deviations of all institutions, 4/3)

<!-- b000308 | prose | pages [18] -->
• (Half of the maximum of deviations of all institutions, 2/4)

<!-- b000309 | prose | pages [18] -->
• (The minimum of deviations of all institutions, 0)

<!-- b000310 | caption | pages [18] -->
Figure 7: Approximated Function from Deviation to Pi

<!-- b000311 | prose | pages [18] -->
5.2.3 Calculation of ROI

<!-- b000312 | prose | pages [18] -->
Recall that ROI is the increase in the performance index (∆Y ) over increase in donation amount (∆X).

<!-- b000313 | prose | pages [18] -->
ROI = ∆Y/∆X

<!-- b000314 | prose | pages [18] -->
And since we already have the performance contributing variables’ coefﬁcients/effects on the performance index (βi) and change in values of performance contributing variables over in- crease in donation amount (ROIi). We get ROI simply by adding all performance contributing variables’ product of these two values. The mathematical deduction is as follows:

<!-- b000315 | prose | pages [18] -->
ROI = ∆Y/∆X P3

<!-- b000316 | prose | pages [18] -->
i=1(βi · ∆Fi/∆X)

<!-- b000317 | prose | pages [18] -->
=

<!-- b000318 | prose | pages [18] -->
(1)

<!-- b000319 | prose | pages [18] -->
P3

<!-- b000320 | prose | pages [18] -->
i=1(βi · ROIi)

<!-- b000321 | prose | pages [18] -->
=

<!-- b000322 | prose | pages [18] -->
P3

<!-- b000323 | prose | pages [18] -->
i=1(βi · Pi · fROIi/∆X)

<!-- b000324 | prose | pages [18] -->
=

<!-- b000325 | prose | pages [18] -->
βi is the post LASSO regression coefﬁcients; fROIi is ﬁtted ROIs of performance contribut- ing variables; Pi is a tuning parameter to adjust the ﬁtted ROIs of performance contributing variables. As we can see, ROI is institution-speciﬁc and dependent on increase in donation amount (∆X). And because increase in donation amount is discrete, we get a ﬁnite set of pos- sible ROI for every institution.

<!-- b000326 | furniture | pages [19] -->
Team # 42939

<!-- b000327 | furniture | pages [19] -->
Page 18 of 24

<!-- b000328 | prose | pages [19] -->
School Selection & Investment Strategy 5.3

<!-- b000329 | prose | pages [19] -->
The next step is to develop an optimal strategy including a list of institutions to be sponsored and the appropriate amount of money given to each institution. We adopt a two-step selection algorithm to ﬁnd the global optimal allocation strategy.

<!-- b000330 | prose | pages [19] -->
Since we have a ﬁnite set of possible ROI for every institution. The ﬁrst step is to compare ROI among each institution’s set. By maximizing ROI for each institution, we determine the optimal amount of investment on each institution if we invest.

<!-- b000331 | prose | pages [19] -->
Then, the next step is to rank all institutions with their respective maximal ROI. Given the budget constraint of money available ($100m), we pick up the institutions with the largest potential to improve on the performance indicator, namely the largest maximal ROI, until we exhaust the budget.

<!-- b000332 | prose | pages [19] -->
By following the two-step selection algorithm, we can derive the optimal investment strat- egy. And the results for year 1 and geographical distribution of selected institutions are pre- sented below in Table 4 and Fig 8.

<!-- b000333 | caption | pages [19] -->
Table 4: Investment Strategy of Year 1

<!-- b000334 | prose | pages [19] -->
UNITID names ROI donation United States Merchant Marine Academy 197027 21.85% 2500000 AVTEC-Alaska’s Institute of Technology 102711 21.26% 7500000 Institute of American Indian and Alaska Native Culture 187745 262129 20.99% 2000000 New College of Florida 20.69% 6500000 Thaddeus Stevens College of Technology 216296 229832 196158 234155 196200 178615 20.66% 3000000 Western Texas College 20.26% 10000000 SUNY at Fredonia 20.24% 5500000 Virginia State University 20.04% 10000000 SUNY College at Potsdam 19.75% 5000000 Truman State University 19.60% 3000000 University of North Carolina at Chapel Hill 199120 101648 19.51% 3000000 Marion Military Institute 19.48% 2500000 New Mexico Military Institute 187912 227386 434584 19.31% 500000 Panola College 19.28% 10000000 Ilisagvik College 19.19% 4500000 University of North Carolina School of the Arts 199184 19.15% 500000 East San Gabriel Valley Regional Occupational Program 413802 19.09% 6000000 University of Minnesota-Morris 174251 19.09% 8000000 Louisiana State University and Agricultural & Mechanical College 159391 403487

<!-- b000335 | prose | pages [19] -->
6

<!-- b000336 | heading | pages [19] -->
Extended Model

<!-- b000337 | prose | pages [19] -->
19.07% 8500000 Wabash Valley College 19.05% 1500000

<!-- b000338 | prose | pages [19] -->
Currently, we have obtained a candidate list of institution with priority and appropriate amount of money for the donation to each institution in total. In this section, we incorporate other crucial elements into the baseline model.

<!-- b000339 | prose | pages [19] -->
6.1 Time Duration

<!-- b000340 | prose | pages [19] -->
One element is the time duration that the organization’s money should be provided. In this paper, we propose two methods for two scenarios. Scenario 1 is where we have new data of

<!-- b000341 | furniture | pages [20] -->
Team # 42939

<!-- b000342 | furniture | pages [20] -->
Page 19 of 24

<!-- b000343 | caption | pages [20] -->
Figure 8: Geographical Distribution of Selected Institutions

<!-- b000344 | prose | pages [20] -->
every past year as time goes by; and Scenario 2 is where we predict the trends and determine 5-year investment strategy only based on the original dataset.

<!-- b000345 | prose | pages [20] -->
In Scenario 1, we adopt a dynamic calibration method based on the outcome of institutions we have patronized. To be more speciﬁc, we ﬁrst determine the investment strategy for the ﬁrst year. And in year 2, we would have had access to new data of year 1. Then we apply the baseline model again with the new information or merged dataset. This would generate new results after the model learning from the latest behaviors of each institution and making the calibrations on the predicting patterns. Similarly, this updating method can be used in the donation years afterwards.

<!-- b000346 | prose | pages [20] -->
In Scenario 2, we adopt a partial calibration method based on the coefﬁcients we calculate with the original dataset. According to assumption A1, we can simply treat status of institu- tions we have not patronized as ﬁxed. And the only values changed are donation amounts and values of performance contributing variables of patronized institutions. This barely af- fects the post-LASSO procedure considering the large quantity of variables used in the process. However, this would lead to movement of points of patronized institutions in the scatterplots of performance contributing variables and donation amount. So we recommend to recalcu- late the ﬁtted curve and ROI and determine the investment strategy for year 2. As for how to determine the movement of points, below is the procedure:

<!-- b000347 | prose | pages [20] -->
• Find the institutions you have patronized in year 1;

<!-- b000348 | prose | pages [20] -->
• Add the amount you have patronized to their original donation amount;

<!-- b000349 | prose | pages [20] -->
X′ = X + ∆X

<!-- b000350 | prose | pages [20] -->
• Calculate the values of performance contributing variables as follows:

<!-- b000351 | prose | pages [20] -->
F ′

<!-- b000352 | prose | pages [20] -->
i = Fi + ROIi · ∆X

<!-- b000353 | prose | pages [20] -->
The results for Scenario 2 are presented below in Table 5 to Table 8:

<!-- b000354 | furniture | pages [21] -->
Team # 42939

<!-- b000355 | furniture | pages [21] -->
Page 20 of 24

<!-- b000356 | caption | pages [21] -->
Table 5: Investment Strategy of Year 2

<!-- b000357 | prose | pages [21] -->
UNITID names ROI donation United States Merchant Marine Academy 197027 21.82% 2500000 AVTEC-Alaska’s Institute of Technology 102711 21.25% 7000000 Institute of American Indian and Alaska Native Culture 187745 262129 20.93% 2000000 New College of Florida 20.73% 6500000 Thaddeus Stevens College of Technology 216296 229832 196158 234155 196200 178615 20.62% 3000000 Western Texas College 20.23% 10000000 SUNY at Fredonia 20.23% 5500000 Virginia State University 20.02% 9000000 SUNY College at Potsdam 19.74% 5000000 Truman State University 19.64% 3000000 University of North Carolina at Chapel Hill 199120 101648 19.52% 3000000 Marion Military Institute 19.48% 2500000 New Mexico Military Institute 187912 227386 434584 19.31% 1500000 Panola College 19.22% 9500000 Ilisagvik College 19.19% 4500000 University of North Carolina School of the Arts 199184 19.18% 2500000 East San Gabriel Valley Regional Occupational Program 413802 19.13% 6000000 University of Minnesota-Morris 174251 19.07% 8000000 Louisiana State University and Agricultural & Mechanical College 159391 403487 19.07% 8500000 Wabash Valley College 19.00% 500000

<!-- b000358 | caption | pages [21] -->
Table 6: Investment Strategy of Year 3

<!-- b000359 | prose | pages [21] -->
UNITID names ROI donation United States Merchant Marine Academy 197027 21.65% 2000000 AVTEC-Alaska’s Institute of Technology 102711 21.29% 7000000 Institute of American Indian and Alaska Native Culture 187745 21.01% 2000000 Thaddeus Stevens College of Technology 216296 262129 229832 196158 234155 196200 178615 20.99% 3500000 New College of Florida 20.87% 6000000 Western Texas College 20.42% 9500000 SUNY at Fredonia 20.42% 5500000 Virginia State University 20.32% 9000000 SUNY College at Potsdam 20.27% 5000000 Truman State University 20.06% 3000000 New Mexico Military Institute 187912 101648 20.00% 2000000 Marion Military Institute 19.96% 2500000 University of North Carolina at Chapel Hill 199120 227386 434584 19.93% 2500000 Panola College 19.87% 9500000 Ilisagvik College 19.87% 4500000 University of North Carolina School of the Arts 199184 19.73% 2500000 East San Gabriel Valley Regional Occupational Program 413802 19.69% 6000000 University of Minnesota-Morris 174251 19.25% 8000000 Eastern Idaho Technical College 142179 19.15% 1000000 Louisiana State University and Agricultural & Mechanical College 159391 403487 19.04% 7000000 Wabash Valley College 3.16% 2000000

<!-- b000360 | furniture | pages [22] -->
Team # 42939

<!-- b000361 | furniture | pages [22] -->
Page 21 of 24

<!-- b000362 | caption | pages [22] -->
Table 7: Investment Strategy of Year 4

<!-- b000363 | prose | pages [22] -->
UNITID names ROI donation United States Merchant Marine Academy 197027 21.72% 2000000 AVTEC-Alaska’s Institute of Technology 102711 21.34% 6500000 Institute of American Indian and Alaska Native Culture 187745 21.25% 2000000 Thaddeus Stevens College of Technology 216296 262129 196158 229832 234155 21.15% 4000000 New College of Florida 21.13% 6500000 SUNY at Fredonia 20.98% 2500000 Western Texas College 20.92% 10000000 Virginia State University 20.80% 9000000 New Mexico Military Institute 187912 101648 196200 178615 20.73% 3000000 Marion Military Institute 20.68% 2500000 SUNY College at Potsdam 20.66% 1500000 Truman State University 20.37% 4000000 University of North Carolina School of the Arts 199184 227386 434584 20.15% 2000000 Panola College 19.66% 10000000 Ilisagvik College 19.52% 4500000 University of North Carolina at Chapel Hill 199120 19.45% 2000000 East San Gabriel Valley Regional Occupational Program 413802 19.45% 6000000 University of Minnesota-Morris 174251 19.36% 8000000 Eastern Idaho Technical College 142179 19.35% 1500000 Louisiana State University and Agricultural & Mechanical College 159391 19.13% 7000000 California Maritime Academy 111188 18.98% 5500000

<!-- b000364 | caption | pages [22] -->
Table 8: Investment Strategy of Year 5

<!-- b000365 | prose | pages [22] -->
UNITID names ROI donation United States Merchant Marine Academy 197027 21.65% 2000000 AVTEC-Alaska’s Institute of Technology 102711 21.20% 6500000 Institute of American Indian and Alaska Native Culture 187745 21.20% 2500000 Thaddeus Stevens College of Technology 216296 262129 196158 229832 234155 21.05% 4000000 New College of Florida 20.83% 6500000 SUNY at Fredonia 20.78% 2500000 Western Texas College 20.56% 10000000 Virginia State University 20.34% 10000000 New Mexico Military Institute 187912 101648 196200 178615 20.25% 3000000 Marion Military Institute 20.21% 2500000 SUNY College at Potsdam 20.03% 1500000 Truman State University 20.00% 4000000 University of North Carolina School of the Arts 199184 227386 434584 19.76% 2000000 Panola College 19.58% 10000000 Ilisagvik College 19.48% 4500000 University of North Carolina at Chapel Hill 199120 19.46% 2000000 East San Gabriel Valley Regional Occupational Program 413802 19.61% 6000000 University of Minnesota-Morris 174251 19.48% 8000000 Eastern Idaho Technical College 142179 19.35% 500000 Louisiana State University and Agricultural & Mechanical College 159391 18.95% 7000000 California Maritime Academy 111188 19.04% 5000000

<!-- b000366 | prose | pages [22] -->
By following above mentioned methods, it is viable to determine the time duration or the investment strategy across time dimension. This approach can effectively avoid waste on do- nations by calibrating or partially calibrating the baseline model.

<!-- b000367 | furniture | pages [23] -->
Team # 42939

<!-- b000368 | furniture | pages [23] -->
Page 22 of 24

<!-- b000369 | prose | pages [23] -->
6.2 Geographical Distribution

<!-- b000370 | prose | pages [23] -->
Another element that can be incorporated into the baseline model is the geographical distri- bution of donations. It matters in two ways.

<!-- b000371 | prose | pages [23] -->
First, regional equality often raises heated debate among citizens and demands appropri- ate treatment. Consequently, charitable organizations are supposed to avoid displaying clear pattern of regional disparity on donations. Second, according to decreasing marginal utility theory, it’s reasonable to diversify investment with respect to regions. Assuming graduates are more likely to get employed where their colleges are, the marginal utility of corresponding social beneﬁts, such as more taxpayers, smaller crime rate, and increase in GDP, would decline as donations are centralized.

<!-- b000372 | prose | pages [23] -->
To deal with this factor, we can simply divide institutions to different geographical groups, split the donations and then apply the model to every group. Another proposed approach is to apply the baseline model with discounted ROI rather than the original deﬁnition. If the baseline model selects more than a predetermined number of institutions from a single region, we discount the ROI of these investments. For example, we could halve the ROI of excessive investments (Speciﬁc discounting method might need further exploration). Then we deter- mine the strategy to maximize the sum of discounted ROI. In this manner, we could effectively alleviate regional related problems.

<!-- b000373 | prose | pages [23] -->
7

<!-- b000374 | heading | pages [23] -->
Conclusions and Discussion

<!-- b000375 | heading | pages [23] -->
Conclusions:

<!-- b000376 | prose | pages [23] -->
This paper manages to develop a fully data-based model to produce a provi- dent investment strategy that maximizing ROI. Our model exhibits a great potential in drawing the conclusions below:

<!-- b000377 | prose | pages [23] -->
• We formulate a performance index for each institution with principal component analysis and develop an appropriate concept for return of investment (ROI) for the charitable foundations like Goodgrant Foundation.

<!-- b000378 | prose | pages [23] -->
• We identify three main performance contributing variables that generate a strong impact on the performance index with post-LASSO procedure: percentage of students who re- ceive a Pell grant amount, the students that are part time and the student-to-faculty ratio.

<!-- b000379 | prose | pages [23] -->
• We derive the relation between the performance contributing variables and donation amount from a GAM ﬁtting model to predict ROI of performance contributing variables.

<!-- b000380 | prose | pages [23] -->
• The ﬁnal list of selected institutions and appropriate amount of donation is determined by a two-step selection algorithm.

<!-- b000381 | prose | pages [23] -->
Limitation and extensions:

<!-- b000382 | prose | pages [23] -->
Though our model successfully produced an investment strategy, it can be improved in several ways:

<!-- b000383 | prose | pages [23] -->
• Since only cross-section data is available, our results of time duration of donation can be improved if we have access to time-series.

<!-- b000384 | prose | pages [23] -->
• The post-LASSO selection only allows for a relatively simple linear model. A more gen- eral selection method is needed when applying to a complicated model.

<!-- b000385 | furniture | pages [24] -->
Team # 42939

<!-- b000386 | furniture | pages [24] -->
Page 23 of 24

<!-- b000387 | heading | pages [24] -->
References

<!-- b000388 | references | pages [24] -->
[1] Schifrin,

<!-- b000389 | references | pages [24] -->
M.,

<!-- b000390 | references | pages [24] -->
Chen L. (2015). Top 50 ROI Colleges:

<!-- b000391 | references | pages [24] -->
2015 Grateful Grads In-

<!-- b000392 | references | pages [24] -->
dex.

<!-- b000393 | references | pages [24] -->
http://www.forbes.com/sites/schifrin/2015/07/29/top50roicolleges2015grateful-

<!-- b000394 | references | pages [24] -->
gradsindex/#285011fc15cc/

<!-- b000395 | references | pages [24] -->
[2] Burke, J. C. (2002). Funding public colleges and universities for performance. SUNY Press.

<!-- b000396 | references | pages [24] -->
[3] Cave, M. (1997). The use of performance indicators in higher education: The challenge of

<!-- b000397 | references | pages [24] -->
the quality movement. Jessica Kingsley Publishers.

<!-- b000398 | references | pages [24] -->
[4] Serban, A. M., & Burke, J. C. (1998). Meeting the performance funding challenge: A nine-

<!-- b000399 | references | pages [24] -->
state comparative analysis. Public Productivity & Management Review, 157-176.

<!-- b000400 | references | pages [24] -->
[5] Banta, T. W., Rudolph, L. B., Van Dyke, J., & Fisher, H. S. (1996). Performance funding

<!-- b000401 | references | pages [24] -->
comes of age in Tennessee. The Journal of Higher Education, 23-45.

<!-- b000402 | references | pages [24] -->
[6] Burke, J. C. (1998). Performance funding indicators: Concerns, values, and models for

<!-- b000403 | references | pages [24] -->
state colleges and universities. New directions for institutional research, 1998(97), 49-60.

<!-- b000404 | references | pages [24] -->
[7] Little, R. J., & Rubin, D. B. (2014). Statistical analysis with missing data. John Wiley & Sons.

<!-- b000405 | references | pages [24] -->
[8] Ehrenberg, R. G. (2004). Econometric studies of higher education. Journal of econometrics,

<!-- b000406 | references | pages [24] -->
121(1), 19-37.

<!-- b000407 | references | pages [24] -->
[9] Rogg, K. L., Schmidt, D. B., Shull, C., & Schmitt, N. (2001). Human resource practices,

<!-- b000408 | references | pages [24] -->
organizational climate, and customer satisfaction. Journal of management, 27(4), 431-449.

<!-- b000409 | references | pages [24] -->
[10] Tibshirani, R. (1996). Regression shrinkage and selection via the lasso. Journal of the Royal

<!-- b000410 | references | pages [24] -->
Statistical Society. Series B (Methodological), 267-288.

<!-- b000411 | references | pages [24] -->
[11] Usai, M. G., Goddard, M. E., & Hayes, B. J. (2009). LASSO with cross-validation for ge-

<!-- b000412 | references | pages [24] -->
nomic selection. Genetics research, 91(06), 427-436.

<!-- b000413 | furniture | pages [25] -->
Team # 42939

<!-- b000414 | furniture | pages [25] -->
Page 24 of 24

<!-- b000415 | heading | pages [25] -->
Appendix

<!-- b000416 | caption | pages [25] -->
Figure 9: GAM Approximation of Share of Students Who Are Part-time vs Donation Amount

<!-- b000417 | caption | pages [25] -->
Figure 10: GAM Approximation of Student-to-faculty Ratio vs Donation Amount
