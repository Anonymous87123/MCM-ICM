# P-C-2016-42939-5fccbebc

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For ofﬁce use only For ofﬁce use only

<!-- b000003 | title | pages [1] -->
42939

<!-- b000004 | prose | pages [1] -->
T1 F1 T2 F2 T3 F3 Problem Chosen T4 F4

<!-- b000005 | title | pages [1] -->
C

<!-- b000006 | heading | pages [1] -->
2016 Mathematical Contest in Modeling (MCM) Summary Sheet

<!-- b000007 | front_matter | pages [1] -->
(Attach a copy of this page to each copy of your solution paper.)

<!-- b000008 | heading | pages [1] -->
Summary

<!-- b000009 | prose | pages [1] -->
In order to determine the optimal donation strategy, this paper proposes a data- motivated model based on an original deﬁnition of return on investment (ROI) appropriate for charitable organizations.

<!-- b000010 | prose | pages [1] -->
First, after addressing missing data, we develop a composite index, called the performance index, to quantify students’ educational performance. The perfor- mance index is a linear composition of several commonly used performance indi- cators, like graduation rate and graduates’ earnings. And their weights are deter- mined by principal component analysis.

<!-- b000011 | prose | pages [1] -->
Next, to deal with problems caused by high-dimensional data, we employ a lin- ear model and a selection method called post-LASSO to select variables that statis- tically signiﬁcantly affect the performance index and determine their effects (coef- ﬁcients). We call them performance contributing variables. In this case, 5 variables are selected. Among them, tuition & fees in 2010 and Carnegie High-Research- Activity classiﬁcation are insusceptible to donation amount. Thus we only con- sider percentage of students who receive a Pell Grant, share of students who are part-time and student-to-faculty ratio.

<!-- b000012 | prose | pages [1] -->
Then, a generalized adaptive model is adopted to estimate the relation between these 3 variables and donation amount. We ﬁt the relation across all institutions and get a ﬁtted function from donation amount to values of performance contributing variables. Then we divide the impact of donation amount into 2 parts: homogenous and heterogenous one. The homogenous inﬂuence is modeled as the change in ﬁt- ted values of performance contributing variables over increase in donation amount, which can be predicted from the ﬁtted curve. The heterogenous one is modeled as a tuning parameter which adjusts the homogenous inﬂuence based on deviation from the ﬁtted curve. And their product is increase in true values of performance over increase in donation amount.

<!-- b000013 | prose | pages [1] -->
Finally, we calculate ROI, deﬁned as increase in performance index over in- crease in donation amount. This ROI is institution-speciﬁc and dependent on in- crease in donation amount. By adopting a two-step ROI maximization algorithm, we determine the optimal investment strategy.

<!-- b000014 | prose | pages [1] -->
Also, we propose an extended model to handle problems caused by time dura- tion and geographical distribution of donations.

<!-- b000015 | furniture | pages [2] -->
Team # 42939

<!-- b000016 | furniture | pages [2] -->
Page 1 of 24

<!-- b000017 | heading | pages [2] -->
A Letter to the CFO of the Goodgrant Foundation

<!-- b000018 | prose | pages [2] -->
Dear Chiang,

<!-- b000019 | prose | pages [2] -->
Our team has proposed a performance index quantifying the students’ educational per- formance of each institution and deﬁned the return of investment (ROI) appropriately for a charitable organization like Goodgrant Foundation. A mathematical model is built to help predict the return of investment after identifying the mechanism through which the donation generates its impact on the performance. The optimal investment strategy is determined by maximizing the estimated return of investment.

<!-- b000020 | prose | pages [2] -->
More speciﬁcally, the composite performance index is developed after taking all the pos- sible performance indicators into consideration, like graduation rate and graduates’ earnings. The performance index is constructed to represents the performance of the school as well as the positive effect that a college brings to students and the community. From this point of view, our deﬁnition manages to capture social beneﬁts of donation.

<!-- b000021 | prose | pages [2] -->
And then we adopt a variable selection method to ﬁnd out performance contributing vari- ables, which are variables that strongly affect the performance index. Among all the perfor- mance contributing variables we select, three variables which can be directly affected by your generous donation are kept to predict ROI: percentage of students who receive a Pell Grant, share of students who are part-time and student-to-faculty ratio.

<!-- b000022 | prose | pages [2] -->
We ﬁtted a relation between these three variables and the donation amount to predict change in value of each performance contributing variable over your donation amount. And we calculate ROI, deﬁned as increase in the performance index over your donation amount, by multiplying change in value of each performance contributing variable over your donation amount and each performance contributing variable’s effect on performance index, and then summing up the products of all performance contributing variables. The optimal investment strategy is decided after maximizing the return of investment according to an algorithm for selection.

<!-- b000023 | prose | pages [2] -->
In conclusion, our model successfully produced an investment strategy including a list of target institutions and investment amount for each institution. (The list of year 1 is attached at the end of the letter). The time duration for the investment could also be determined based on our model. Since the model as well as the evaluation approach is fully data-motivated with no arbitrary criterion included, it is rather adaptable for solving future philanthropic educational investment problems.

<!-- b000024 | prose | pages [2] -->
We have a strong belief that our model can effectively enhance the efﬁciency of philan- thropic educational investment and provides an appropriate as well as feasible way to best improve the educational performance of students.

<!-- b000025 | prose | pages [2, 3] -->
UNITID names ROI donation 197027 United States Merchant Marine Academy 21.85% 2500000 102711 AVTEC-Alaska’s Institute of Technology 21.26% 7500000 187745 Institute of American Indian and Alaska Native Culture 20.99% 2000000 262129 New College of Florida 20.69% 6500000 216296 Thaddeus Stevens College of Technology 20.66% 3000000 229832 Western Texas College 20.26% 10000000 196158 SUNY at Fredonia 20.24% 5500000 234155 Virginia State University 20.04% 10000000 196200 SUNY College at Potsdam 19.75% 5000000 178615 Truman State University 19.60% 3000000 199120 University of North Carolina at Chapel Hill 19.51% 3000000 101648 Marion Military Institute 19.48% 2500000 187912 New Mexico Military Institute 19.31% 500000 227386 Panola College 19.28% 10000000 434584 Ilisagvik College 19.19% 4500000 199184 University of North Carolina School of the Arts 19.15% 500000 413802 East San Gabriel Valley Regional Occupational Program 19.09% 6000000 174251 University of Minnesota-Morris 19.09% 8000000 159391 Louisiana State University and Agricultural & Mechanical Col- 19.07% 8500000 lege 403487 Wabash Valley College 19.05% 1500000

<!-- b000026 | furniture | pages [3] -->
Team # 42939

<!-- b000027 | furniture | pages [3] -->
Page 2 of 24

<!-- b000029 | prose | pages [3, 4] -->
Yours Sincerely, An Optimal Strategy of Donation

<!-- b000030 | furniture | pages [3] -->
Team #42939

<!-- b000031 | furniture | pages [4] -->
Team # 42939

<!-- b000032 | furniture | pages [4] -->
Page 3 of 24

<!-- b000034 | prose | pages [4] -->
for Educational Purpose

<!-- b000035 | prose | pages [4] -->
Control Number: #42939

<!-- b000036 | prose | pages [4] -->
February , 2016

<!-- b000037 | furniture | pages [5] -->
Team # 42939

<!-- b000038 | furniture | pages [5] -->
Page 4 of 24

<!-- b000039 | heading | pages [5] -->
Contents

<!-- b000040 | contents | pages [5] -->
1 Introduction

<!-- b000041 | contents | pages [5] -->
5

<!-- b000042 | contents | pages [5] -->
1.1

<!-- b000043 | contents | pages [5] -->
Statement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000044 | contents | pages [5] -->
5

<!-- b000045 | contents | pages [5] -->
1.2

<!-- b000046 | contents | pages [5] -->
Baseline Model

<!-- b000047 | contents | pages [5] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000048 | contents | pages [5] -->
5

<!-- b000049 | contents | pages [5] -->
1.3

<!-- b000050 | contents | pages [5] -->
Detailed Deﬁnitions & Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000051 | contents | pages [5] -->
8

<!-- b000052 | contents | pages [5] -->
1.3.1

<!-- b000053 | contents | pages [5] -->
Detailed Deﬁnitions: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000054 | contents | pages [5] -->
8

<!-- b000055 | contents | pages [5] -->
1.3.2

<!-- b000056 | contents | pages [5] -->
Assumptions: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000057 | contents | pages [5] -->
9

<!-- b000058 | contents | pages [5] -->
1.4

<!-- b000059 | contents | pages [5] -->
The Advantages of Our Model

<!-- b000060 | contents | pages [5] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000061 | contents | pages [5] -->
9

<!-- b000062 | contents | pages [5] -->
2 Addressing the Missing Values

<!-- b000063 | contents | pages [5] -->
9

<!-- b000064 | contents | pages [5] -->
3 Determining the Performance Index

<!-- b000065 | contents | pages [5] -->
10

<!-- b000066 | contents | pages [5] -->
3.1

<!-- b000067 | contents | pages [5] -->
Performance Indicators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000068 | contents | pages [5] -->
10

<!-- b000069 | contents | pages [5] -->
3.2

<!-- b000070 | contents | pages [5] -->
Performance Index via Principal-Component Factors

<!-- b000071 | contents | pages [5] -->
. . . . . . . . . . . . . . . .

<!-- b000072 | contents | pages [5] -->
10

<!-- b000073 | contents | pages [5] -->
4 Identifying Performance Contributing Variables via post-LASSO

<!-- b000074 | contents | pages [5] -->
11

<!-- b000075 | contents | pages [5] -->
5 Determining Investment Strategy based on ROI

<!-- b000076 | contents | pages [5] -->
13

<!-- b000077 | contents | pages [5] -->
5.1

<!-- b000078 | contents | pages [5] -->
Fitted Curve between Performance Contributing Variables and Donation Amount 14

<!-- b000079 | contents | pages [5] -->
5.2

<!-- b000080 | contents | pages [5] -->
ROI(Return on Investment)

<!-- b000081 | contents | pages [5] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000082 | contents | pages [5] -->
15

<!-- b000083 | contents | pages [5] -->
Model of Fitted ROIs of Performance Contributing Variables fROIi

<!-- b000084 | contents | pages [5] -->
5.2.1

<!-- b000085 | contents | pages [5] -->
. . .

<!-- b000086 | contents | pages [5] -->
15

<!-- b000087 | contents | pages [5] -->
Model of the tuning parameter Pi

<!-- b000088 | contents | pages [5] -->
5.2.2

<!-- b000089 | contents | pages [5] -->
. . . . . . . . . . . . . . . . . . . . . . .

<!-- b000090 | contents | pages [5] -->
16

<!-- b000091 | contents | pages [5] -->
5.2.3

<!-- b000092 | contents | pages [5] -->
Calculation of ROI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000093 | contents | pages [5] -->
17

<!-- b000094 | contents | pages [5] -->
5.3

<!-- b000095 | contents | pages [5] -->
School Selection & Investment Strategy

<!-- b000096 | contents | pages [5] -->
. . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000097 | contents | pages [5] -->
18

<!-- b000098 | contents | pages [5] -->
6 Extended Model

<!-- b000099 | contents | pages [5] -->
18

<!-- b000100 | contents | pages [5] -->
6.1

<!-- b000101 | contents | pages [5] -->
Time Duration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000102 | contents | pages [5] -->
18

<!-- b000103 | contents | pages [5] -->
6.2

<!-- b000104 | contents | pages [5] -->
Geographical Distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000105 | contents | pages [5] -->
22

<!-- b000106 | contents | pages [5] -->
7 Conclusions and Discussion

<!-- b000107 | contents | pages [5] -->
22

<!-- b000108 | contents | pages [5] -->
8 Reference

<!-- b000109 | contents | pages [5] -->
23

<!-- b000110 | contents | pages [5] -->
9 Appendix

<!-- b000111 | contents | pages [5] -->
24

<!-- b000112 | furniture | pages [6] -->
Team # 42939

<!-- b000113 | furniture | pages [6] -->
Page 5 of 24

<!-- b000114 | heading | pages [6] -->
1 Introduction

<!-- b000115 | heading | pages [6] -->
1.1 Statement of the Problem

<!-- b000116 | prose | pages [6] -->
There exists no doubt in the signiﬁcance of postsecondary education to the development of society, especially with the ascending need for skilled employees capable of complex work. Nevertheless, U.S. ranks only 11th in the higher education attachment worldwide, which makes the ﬁnancial support from large charitable organizations necessary.

<!-- b000117 | prose | pages [6] -->
As it’s essential for charitable organizations to maximize the effectiveness of donations, an objective and systematic assessment model is in demand to develop appropriate investment strategies. To achieve this goal, several large foundations like Gates Foundation and Lumina Foundation have developed different evaluation approaches, where they mainly focus on spe- ciﬁc indexes like attendance and graduation rate. In other empirical literature, a Forbes ap- proach (Shifrin and Chen,2015) proposes a new indicator called the Grateful Graduates Index, using the median amount of private donations per student over a 10-year period to measure the return on investment. Also, performance funding indicators (Burke,2002, Cave,1997, Ser- ban and Burke,1998,Banta et al,1996), which include but are not limited to external indicators like graduates’ employment rate and internal indicators like teaching quality, are one of the most prevailing methods to evaluate effectiveness of educational donations.

<!-- b000118 | prose | pages [6] -->
However, those methods also arise with widely acknowledged concerns (Burke,1998). Most of them require subjective choice of indexes and are rather arbitrary than data-based. And they perform badly in a data environment where there is miscellaneous cross-section data but scarce time-series data. Besides, they lack quantiﬁed analysis in precisely predicting or measuring the social beneﬁts and the positive effect that the investment can generate, which serves as one of the targets for the Goodgrant Foundation.

<!-- b000119 | prose | pages [6] -->
In accordance with Goodgrant Foundation’s request, this paper provides a prudent def- inition of return on investment (ROI) for charitable organizations, and develops an original data-motivated model, which is feasible even faced with tangled cross-section data and absent time-series data, to determine the optimal strategy for funding. The strategy contains selection of institutions and distribution of investment across institutions, time and regions.

<!-- b000120 | heading | pages [6] -->
1.2 Baseline Model

<!-- b000121 | prose | pages [6] -->
Our deﬁnition of ROI is similar to its usual meaning, which is the increase in students’ educational performance over the amount Goodgrant Foundation donates (assuming other donations ﬁxed, it’s also the increase in total donation amount).

<!-- b000122 | prose | pages [6] -->
First we cope with data missingness. Then, to quantify students’ educational performance, we develop an index called performance index, which is a linear composition of commonly used performance indicators.

<!-- b000123 | prose | pages [6] -->
Our major task is to build a model to predict the change of this index given a distribution of Goodgrant Foundation $100m donation. However, donation does not directly affect the performance index and we would encounter endogeneity problem or neglect effects of other variables if we solely focus on the relation between performance index and donation amount. Instead, we select several variables that are pivotal in predicting the performance index from many potential candidates, and determine their coefﬁcients/effects on the performance index. We call these variables performance contributing variables.

<!-- b000124 | prose | pages [6, 7] -->
Due to absence of time-series data, it becomes difﬁcult to ﬁgure out how performance con- tributing variables are affected by donation amount for each institution respectively. Instead, we ﬁt the relation between performance contributing variables and donation amount across all institutions and get a ﬁtted function from donation amount to values of performance contribut- ing variables.

<!-- b000125 | furniture | pages [7] -->
Team # 42939

<!-- b000126 | furniture | pages [7] -->
Page 6 of 24

<!-- b000128 | prose | pages [7] -->
Then we divide the impact of donation amount into 2 parts: homogenous and heteroge- nous one. The homogenous inﬂuence is modeled as the change in ﬁtted values of performance contributing variables over increase in donation amount (We call these quotients ﬁtted ROI of performance contributing variable). The heterogenous one is modeled as a tuning parameter, which adjusts the homogenous inﬂuence based on deviation from the ﬁtted function. And their product is the institution-speciﬁc increase in true values of performance contributing variables over increase in donation amount (We call these values ROI of performance contributing vari- able).

<!-- b000129 | prose | pages [7] -->
The next step is to calculate the ROI of the performance index by adding the products of ROIs of performance contributing variables and their coefﬁcients on the performance index. This ROI is institution-speciﬁc and dependent on increase in donation amount. By adopting a two-step ROI maximization algorithm, we determine the optimal investment strategy.

<!-- b000130 | prose | pages [7] -->
Also, we propose an extended model to handle problems caused by time duration and geographical distribution of donations.

<!-- b000131 | prose | pages [7] -->
Note: we only use data from the provided excel table and that mentioned in the pdf ﬁle.

<!-- b000132 | caption | pages [7] -->
Table 1: Data Source

<!-- b000133 | prose | pages [7] -->
Variable Dataset

<!-- b000134 | prose | pages [7] -->
Performance index Excel table

<!-- b000135 | prose | pages [7] -->
Performance contributing variables Excel table and pdf ﬁle

<!-- b000136 | prose | pages [7] -->
Donation amount Pdf ﬁle

<!-- b000137 | prose | pages [7] -->
The ﬂow chart of the whole model is presented below in Fig 1:

<!-- b000138 | furniture | pages [8] -->
Team # 42939

<!-- b000139 | furniture | pages [8] -->
Page 7 of 24

<!-- b000140 | caption | pages [8] -->
Figure 1: Flow Chart Demonstration of the Model

<!-- b000141 | furniture | pages [9] -->
Team # 42939

<!-- b000142 | furniture | pages [9] -->
Page 8 of 24

<!-- b000143 | heading | pages [9] -->
1.3 Detailed Deﬁnitions & Assumptions

<!-- b000144 | heading | pages [9] -->
1.3.1 Detailed Deﬁnitions:

<!-- b000145 | furniture | pages [10] -->
Team # 42939

<!-- b000146 | furniture | pages [10] -->
Page 9 of 24

<!-- b000147 | heading | pages [10] -->
1.3.2 Assumptions:

<!-- b000148 | prose | pages [10] -->
A1. Stability. We assume data of any institution should be stable without the impact from outside. To be speciﬁc, the key factors like the donation amount and the performance index should remain unchanged if the college does not receive new donations.

<!-- b000149 | prose | pages [10] -->
A2. Goodgrant Foundation’s donation (Increase in donation amount) is discrete rather than continuous. This is reasonable because each donation is usually an integer multiple of a minimum amount, like $1m. After referring to the data of other foundations like Lumina Foundation, we recommend donation amount should be one value in the set below:

<!-- b000150 | prose | pages [10] -->
{500000, 1000000, 1500000, ..., 10000000}

<!-- b000151 | prose | pages [10] -->
A3. The performance index is a linear composition of all given performance indicators.

<!-- b000152 | prose | pages [10] -->
A4. Performance contributing variables linearly affect the performance index.

<!-- b000153 | prose | pages [10] -->
A5. Increase in donation amount affects the performance index through performance con- tributing variables.

<!-- b000154 | prose | pages [10] -->
A6. The impact of increase in donation amount on performance contributing variables con- tains 2 parts: homogenous one and heterogenous one. The homogenous inﬂuence is repre- sented by a smooth function from donation amount to performance contributing variables.

<!-- b000155 | prose | pages [10] -->
And the heterogenous one is represented by deviation from the function.

<!-- b000156 | heading | pages [10] -->
1.4 The Advantages of Our Model

<!-- b000157 | prose | pages [10] -->
Our model exhibits many advantages in application:

<!-- b000158 | prose | pages [10] -->
• The evaluation model is fully data based with few subjective or arbitrary decision rules.

<!-- b000159 | prose | pages [10] -->
• Our model successfully identiﬁes the underlying mechanism instead of merely focusing on the relation between donation amount and the performance index.

<!-- b000160 | prose | pages [10] -->
• Our model takes both homogeneity and heterogeneity into consideration.

<!-- b000161 | prose | pages [10] -->
• Our model makes full use of the cross-section data and does not need time-series data to produce reasonable outcomes.

<!-- b000162 | heading | pages [10] -->
2 Addressing the Missing Values

<!-- b000163 | prose | pages [10] -->
The provided datasets suffer from severe data missing, which could undermine the reliabil- ity and interpretability of any results. To cope with this problem, we adopt several different methods for data with varied missing rate.

<!-- b000164 | prose | pages [10] -->
For data with missing rate over 50%, any current prevailing method would fall victim to under- or over-randomization. As a result, we omit this kind of data for simplicity’s sake.

<!-- b000165 | prose | pages [10] -->
For variables with missing rate between 10%-50%, we use imputation techniques (Little and Rubin, 2014) where a missing value was imputed from a randomly selected similar record, and model-based analysis where missing values are substituted with distribution diagrams.

<!-- b000166 | furniture | pages [11] -->
Team # 42939

<!-- b000167 | furniture | pages [11] -->
Page 10 of 24

<!-- b000168 | prose | pages [11] -->
For variables with missing rate under 10%, we address missingness by simply replace miss- ing value with mean of existing values.

<!-- b000169 | heading | pages [11] -->
3 Determining the Performance Index

<!-- b000170 | prose | pages [11] -->
In this section, we derive a composite index, called the performance index, to evaluate the educational performance of students at every institution.

<!-- b000171 | heading | pages [11] -->
3.1 Performance Indicators

<!-- b000172 | prose | pages [11] -->
First, we need to determine which variables from various institutional performance data are direct indicators of Goodgrant Foundation’s major concern – to enhance students’ educational performance.

<!-- b000173 | prose | pages [11] -->
In practice, other charitable foundations such as Gates Foundation place their focus on core indexes like attendance and graduation rate. Logically, we select performance indicators on the basis of its correlation with these core indexes. With this method, miscellaneous performance data from the excel table boils down to 4 crucial variables. C150_4_POOLED_SUPP and C200_L4_POOLED_SUPP, as completion rates for different types of institutions, are directly correlated with graduation rate. We combine them into one variable.Md_earn_wne_p10 and gt_25k_p6, as different measures of graduates’ earnings, are proved in empirical studies (Ehren- berg,2004) to be highly dependent on educational performance. And RPY _3Y R_RT_SUPP, as repayment rate, is also considered valid in the same sense. Let them be Y1, Y2, Y3 and Y4.

<!-- b000174 | prose | pages [11] -->
For easy calculation and interpretation of the performance index, we apply uniformization to all 4 variables, as to make sure they’re on the same scale (from 0 to 100).

<!-- b000175 | heading | pages [11] -->
3.2 Performance Index via Principal-Component Factors

<!-- b000176 | prose | pages [11] -->
As the model assumes the performance index is a linear composition of all performance indicators, all we need to do is determine the weights of these variables.

<!-- b000177 | prose | pages [11] -->
Here we apply the method of Customer Satisfaction Index model (Rogg et al,2001), where principal-component factors (pcf) are employed to determine weights of all aspects.

<!-- b000178 | prose | pages [11] -->
The pcf procedure uses an orthogonal transformation to convert a set of observations of pos- sibly correlated variables into a set of values of linearly uncorrelated variables called principal- component factors, each of which carries part of the total variance. If the cumulative proportion of the variance exceeds 80%, it’s viable to use corresponding pcfs (usually the ﬁrst two pcfs) to determine weights of original variables.

<!-- b000179 | prose | pages [11] -->
In this case, we’ll get 4 pcfs (named PCF1, PCF2, PCF3 and PCF4). First, the procedure provides the linear coefﬁcients of Ym in the expression of PCF1 and PCF2. We get

<!-- b000180 | prose | pages [11] -->
PCF1 = a11Y1 + a12Y2 + a13Y3 + a14Y4

<!-- b000181 | prose | pages [11] -->
PCF2 = a21Y1 + a22Y2 + a23Y3 + a24Y4

<!-- b000182 | prose | pages [11, 12] -->
(akm calculated as corresponding factor loadings over square root of factor k’s eigenvalue) Then, we calculate the rough weights cm for Ym. Let the variance proportions PCF1 and PCF2 represent be N1 and N2. We get cm = (a1mN1 +a2mN2)/(N1 +N2) (This formulation is justiﬁed because the variance proportions can be viewed as the signiﬁcance of pcfs). If we let perfor- mance index= (PCF1N1 + PCF2N2)/(N1 + N2), cm is indeed the rough weight of Ym in terms of variance) Next, we get the weights by adjusting the sum of rough weights to 1:

<!-- b000183 | furniture | pages [12] -->
Team # 42939

<!-- b000184 | furniture | pages [12] -->
Page 11 of 24

<!-- b000186 | prose | pages [12] -->
cm = cm/(c1 + c2 + c3 + c4)

<!-- b000187 | prose | pages [12] -->
Finally, we get the performance index, which is the weighted sum of the 4 performance indicator. Performance index=P m(cmYm)

<!-- b000188 | caption | pages [12] -->
Table 2 presents the 10 institutions with largest values of the performance index. This rank-

<!-- b000189 | prose | pages [12] -->
ing is highly consistent with widely acknowledged rankings, like QS ranking, which indicates the validity of the performance index.

<!-- b000190 | caption | pages [12] -->
Table 2: The Top 10 Institutions in Terms of Performance Index

<!-- b000191 | prose | pages [12] -->
Institution Performance index Los Angeles County College of Nursing and Allied Health 79.60372162 Massachusetts Institute of Technology 79.06066895 University of Pennsylvania 79.05044556 Babson College 78.99269867 Georgetown University 78.90468597 Stanford University 78.70586395 Duke University 78.27719116 University of Notre Dame 78.15843964 Weill Cornell Medical College 78.14334106

<!-- b000192 | heading | pages [12] -->
4 Identifying Performance Contributing Variables via post-LASSO

<!-- b000193 | prose | pages [12] -->
The next step of our model requires identifying the factors that may exert an inﬂuence on the students’ educational performance from a variety of variables mentioned in the excel table and the pdf ﬁle (108 in total, some of which are dummy variables converted from categorical variables).To achieve this purpose, we used a model called LASSO. A linear model is adopted to describe the relationship between the endogenous variable – performance index – and all variables that are potentially inﬂuential to it. We assign appropriate coefﬁcient to each variable to minimize the square error between our model prediction and the actual value when ﬁtting the data.

<!-- b000194 | prose | pages [12] -->
J 1 X (yj −xT j β)2 min J β j=1 where J = 2881,xj = (1, x1j, x2j, ..., xpj)T

<!-- b000195 | prose | pages [12] -->
However, as the amount of the variables included in the model is increasing, the cost func- tion will naturally decrease. So the problem of over ﬁtting the data will arise, which make the model we come up with hard to predict the future performance of the students. Also, since there are hundreds of potential variables as candidates. We need a method to identify the variables that truly matter and have a strong effect on the performance index.

<!-- b000196 | prose | pages [12, 13] -->
Here we take the advantage of a method named post-LASSO (Tibshirani,1996). LASSO, also known as the least absolute shrinkage and selection operator, is a method used for variable selection and shrinkage in medium- or high-dimensional environment. And post-LASSO is to apply ordinary least squares (OLS) to the model selected by ﬁrst-step LASSO procedure. In LASSO procedure, instead of using the cost function that merely focusing on the square error between the prediction and the actual value, a penalty term is also included into the objective function. We wish to minimize:

<!-- b000197 | furniture | pages [13] -->
Team # 42939

<!-- b000198 | furniture | pages [13] -->
Page 12 of 24

<!-- b000200 | prose | pages [13] -->
J 1 j β)2 + λ||β||1 X (yj −xT min J β j=1

<!-- b000201 | prose | pages [13] -->
where λ||β||1 is the penalty term. The penalty term takes the number of variables into con- sideration by penalizing on the absolute value of the coefﬁcients and forcing the coefﬁcients of many variables shrink to zero if this variable is of less importance. The penalty coefﬁcient lambda determines the degree of penalty for including variables into the model. After min- imizing the cost function plus the penalty term, we could ﬁgure out the variables of larger essence to include in the model.

<!-- b000202 | prose | pages [13] -->
We utilize the LARS algorithm to implement the LASSO procedure and cross-validation MSE minimization (Usai et al,2009) to determine the optimal penalty coefﬁcient (represented by shrinkage factor in LARS algorithm). And then OLS is employed to complete the post- LASSO method.

<!-- b000203 | caption | pages [13] -->
Figure 2: LASSO path-coefﬁcients as a function of shrinkage factor s

<!-- b000204 | caption | pages [13] -->
Figure 3: Cross-validated MSE

<!-- b000205 | furniture | pages [14] -->
Team # 42939

<!-- b000206 | furniture | pages [14] -->
Page 13 of 24

<!-- b000207 | prose | pages [14] -->
Fig 2. displays the results of LASSO procedure and Fig 3 displays the cross-validated MSE for different shrinkage factors. As speciﬁed above, the cross-validated MSE reaches minimum with shrinkage factor between 0.4-0.8. We choose 0.6 and ﬁnd in Fig 2 that 6 variables have nonzero coefﬁcients via the LASSO procedure, thus being selected as the performance con- tributing variables. Table 3 is a demonstration of these 6 variables and corresponding post- LASSO results.

<!-- b000208 | caption | pages [14] -->
Table 3: Post-LASSO results

<!-- b000209 | prose | pages [14] -->
Dependent variable:

<!-- b000210 | prose | pages [14] -->
performance_index −26.453∗∗∗ PCTPELL (0.872)

<!-- b000211 | prose | pages [14] -->
−14.819∗∗∗ PPTUG_EF (0.781)

<!-- b000212 | prose | pages [14] -->
−0.231∗∗∗ StudentToFaculty_ratio (0.025)

<!-- b000213 | prose | pages [14] -->
0.0003∗∗∗ Tuition&Fees2010 (0.00002)

<!-- b000214 | prose | pages [14] -->
5.667∗∗∗ Carnegie_HighResearchActivity (0.775)

<!-- b000215 | prose | pages [14] -->
61.326∗∗∗ Constant (0.783)

<!-- b000216 | prose | pages [14] -->
Observations 2,880 R2 0.610 Adjusted R2 0.609

<!-- b000217 | prose | pages [14] -->
Note: PCTPELL is percentage of students who receive a Pell Grant;PPTUG_EF is share of students who are part- time;Carnegie_HighResearchActivity is Carnegie classiﬁca- tion basic: High Research Activity

<!-- b000218 | prose | pages [14] -->
The results presented in Table 3 are consistent with common sense. For instance, the pos- itive coefﬁcient of High Research Activity Carnegie classiﬁcation implies that active research activity helps student’s educational performance; and the negative coefﬁcient of Student-to- Faculty ratio suggests that decrease in faculty quantity undermines students’ educational per- formance. Along with the large R square value and small p-value for each coefﬁcient, the post-LASSO procedure proves to select a valid set of performance contributing variables and describe well their contribution to the performance index.

<!-- b000219 | heading | pages [14] -->
5 Determining Investment Strategy based on ROI

<!-- b000220 | prose | pages [14, 15] -->
We’ve identiﬁed 5 performance contributing variables via post-LASSO. Among them, tu- ition & fees in 2010 and Carnegie High-Research-Activity classiﬁcation are quite insusceptible to donation amount. So we only consider the effects of increase in donation amount on per- centage of students who receive a Pell Grant, share of students who are part-time and student- to-faculty ratio. We denote them with F1, F2 and F3, their post-LASSO coefﬁcients with β1,β2 and β3.

<!-- b000221 | furniture | pages [15] -->
Team # 42939

<!-- b000222 | furniture | pages [15] -->
Page 14 of 24

<!-- b000224 | prose | pages [15] -->
In this section, we ﬁrst introduce the procedure used to ﬁt the relation between performance contributing variables and donation amount. Then we provide the model employed to calcu- late ﬁtted ROIs of performance contributing variables (the homogenous inﬂuence of increase in donation amount) and the tuning parameter (the heterogenous inﬂuence of increase in dona- tion amount). Next, we introduce how to determine ROI. Lastly, we show how the maximiza- tion determines the investment strategy, including selection of institutions and distribution of investments.

<!-- b000225 | heading | pages [15] -->
5.1 Fitted Curve between Performance Contributing Variables and Donation Amount

<!-- b000226 | prose | pages [15] -->
Since we have already approximated the linear relation between the performance index with the 3 performance contributing variables, we want to know how increase in donation changes them. In this paper, we use Generalized Adaptive Model (GAM) to smoothly ﬁt the relations. Generalized Adaptive Model is a generalized linear model in which the dependent variable depends linearly on unknown smooth functions of independent variables. The ﬁtted curve of percentage of students who receive a Pell Grant is depicted below in Fig 4 (see the other two ﬁtted curves in Appendix):

<!-- b000227 | caption | pages [15] -->
Figure 4: GAM Approximation

<!-- b000228 | prose | pages [15, 16] -->
A Pell Grant is money the U.S. federal government provides directly for students who need it to pay for college. Intuitively, if the amount of donation an institution receives from other sources such as private donation increases, the institution is likely to use these donations to alleviate students’ ﬁnancial stress, resulting in percentage of students who receive a Pell Grant. Thus it is reasonable to see a ﬁtted curve downward sloping at most part. Also, in common sense, an increase in donation amount would lead to increase in the performance index. This downward sloping curve is consistent with the negative post-LASSO coefﬁcient of percentage of students who receive a Pell Grant (as two negatives make a positive).

<!-- b000229 | furniture | pages [16] -->
Team # 42939

<!-- b000230 | furniture | pages [16] -->
Page 15 of 24

<!-- b000232 | heading | pages [16] -->
5.2 ROI(Return on Investment)

<!-- b000233 | heading | pages [16] -->
5.2.1 Model of Fitted ROIs of Performance Contributing Variables fROIi

<!-- b000234 | caption | pages [16] -->
Figure 5: Demonstration of fROI1

<!-- b000235 | prose | pages [16] -->
Again, we use ﬁtted curve of percentage of students who receive a Pell Grant as an example. We modeled the blue ﬁtted curve to represent the homogeneous relation between percentage of students who receive a Pell Grant and donation amount.

<!-- b000236 | prose | pages [16] -->
Recall ﬁtted ROI of percentage of students who receive a Pell Grant (fROI1) is change in ﬁtted values (∆f) over increase in donation amount (∆X). So

<!-- b000237 | prose | pages [16] -->
fROI1 = ∆f/∆X

<!-- b000238 | prose | pages [16] -->
According to assumption A2, the amount of each Goodgrant Foundation’s donation falls into a pre-speciﬁed set, namely, {500000, 1000000, 1500000, ..., 10000000}. So we get a set of possible ﬁtted ROI of percentage of students who receive a Pell Grant (fROI1). Clearly, fROI1 is de- pendent on both donation amount (X) and increase in donation amount (∆X). Calculation of ﬁtted ROIs of other performance contributing variables is similar.

<!-- b000239 | furniture | pages [17] -->
Team # 42939

<!-- b000240 | furniture | pages [17] -->
Page 16 of 24

<!-- b000241 | heading | pages [17] -->
5.2.2 Model of the tuning parameter Pi

<!-- b000242 | prose | pages [17] -->
Although we’ve identiﬁed the homogenous inﬂuence of increase in donation amount, we shall not neglect the fact that institutions utilize donations differently. A proportion of do- nations might be appropriated by the university’s administration and different institutions allocate the donation differently. For example, university with a more convenient and well- maintained system of identifying students who need ﬁnancial aid might be willing to use a larger portion of donations to directly aid students, resulting in a lower percentage of under- graduate students receiving Pell grant. Also, university facing lower cost of identifying and hiring suitable faculty members might be inclined to use a larger portion of donations in this direction, resulting in a lower student-to-faculty ratio.

<!-- b000243 | prose | pages [17] -->
These above mentioned reasons make institutions deviate from the homogenous ﬁtted func- tion and presents heterogeneous inﬂuence of increase in donation amount. Thus, while the homogenous inﬂuence only depends on donation amount and increase in donation amount, the heterogeneous inﬂuence is institution-speciﬁc.

<!-- b000244 | prose | pages [17] -->
To account for this heterogeneous inﬂuence, we utilize a tuning parameter Pi to adjust the homogenous inﬂuence. By multiplying the tuning parameter, ﬁtted ROIs of performance con- tributing variables (ﬁtted value changes) convert into ROI of performance contributing variable (true value changes).

<!-- b000245 | prose | pages [17] -->
ROIi = fROIi · Pi

<!-- b000246 | prose | pages [17] -->
We then argue that Pi can be summarized by a function of deviation from the ﬁtted curve (∆h), and the function has the shape shown in Fig 6.

<!-- b000247 | prose | pages [17] -->
The value of Pi ranges from 0 to 2, because Pi can be viewed as an ampliﬁcation or shrinkage of the homogenous inﬂuence. For example, Pi=2 means that the homogeneous inﬂuence is ampliﬁed greatly. Pi =0 means that this homogeneous inﬂuence would be entirely wiped out. The shape of the function is as shown in Fig 6 because of the following reasons. Intuitively, if one institution locates above the ﬁtted line, when deviation is small, the larger it is, the larger Pi is. This is because the institution might be more inclined to utilize donations to change that factor. However, when deviation becomes even larger, the institution grows less willing to invest on this factor. This is because marginal utility decreases. The discussion is similar if one institution initially lies under the ﬁtted line. Thus, we assume the function mapping deviation to Pi is similar to Fig 6. deviation is on the x-axis while Pi is on the y-axis.

<!-- b000248 | caption | pages [17] -->
Figure 6: Function from Deviation to Pi

<!-- b000249 | prose | pages [17, 18] -->
In order to simplify calculation and without loss of generality, we approximate the function in Fig 6 by a set of linear segments, as is shown in Fig 7. The endpoints from left to right are respectively:

<!-- b000250 | furniture | pages [18] -->
Team # 42939

<!-- b000251 | furniture | pages [18] -->
Page 17 of 24

<!-- b000253 | prose | pages [18] -->
• (The minimum of deviations of all institutions, 2)

<!-- b000254 | prose | pages [18] -->
• (Half of the minimum of deviations of all institutions, 4/3)

<!-- b000255 | prose | pages [18] -->
• (Quarter of the minimum of deviations of all institutions, 2/3)

<!-- b000256 | prose | pages [18] -->
• (0, 1)

<!-- b000257 | prose | pages [18] -->
• (Quarter of the maximum of deviations of all institutions, 4/3)

<!-- b000258 | prose | pages [18] -->
• (Half of the maximum of deviations of all institutions, 2/4)

<!-- b000259 | prose | pages [18] -->
• (The minimum of deviations of all institutions, 0)

<!-- b000260 | caption | pages [18] -->
Figure 7: Approximated Function from Deviation to Pi

<!-- b000261 | heading | pages [18] -->
5.2.3 Calculation of ROI

<!-- b000262 | prose | pages [18] -->
Recall that ROI is the increase in the performance index (∆Y ) over increase in donation amount (∆X).

<!-- b000263 | prose | pages [18] -->
ROI = ∆Y/∆X

<!-- b000264 | prose | pages [18] -->
And since we already have the performance contributing variables’ coefﬁcients/effects on the performance index (βi) and change in values of performance contributing variables over in- crease in donation amount (ROIi). We get ROI simply by adding all performance contributing variables’ product of these two values. The mathematical deduction is as follows:

<!-- b000265 | prose | pages [18] -->
ROI = ∆Y/∆X P3 i=1(βi · ∆Fi/∆X) = (1) P3 i=1(βi · ROIi) = P3 i=1(βi · Pi · fROIi/∆X) =

<!-- b000266 | prose | pages [18] -->
βi is the post LASSO regression coefﬁcients; fROIi is ﬁtted ROIs of performance contribut- ing variables; Pi is a tuning parameter to adjust the ﬁtted ROIs of performance contributing variables. As we can see, ROI is institution-speciﬁc and dependent on increase in donation amount (∆X). And because increase in donation amount is discrete, we get a ﬁnite set of pos- sible ROI for every institution.

<!-- b000267 | furniture | pages [19] -->
Team # 42939

<!-- b000268 | furniture | pages [19] -->
Page 18 of 24

<!-- b000269 | heading | pages [19] -->
5.3 School Selection & Investment Strategy

<!-- b000270 | prose | pages [19] -->
The next step is to develop an optimal strategy including a list of institutions to be sponsored and the appropriate amount of money given to each institution. We adopt a two-step selection algorithm to ﬁnd the global optimal allocation strategy.

<!-- b000271 | prose | pages [19] -->
Since we have a ﬁnite set of possible ROI for every institution. The ﬁrst step is to compare ROI among each institution’s set. By maximizing ROI for each institution, we determine the optimal amount of investment on each institution if we invest.

<!-- b000272 | prose | pages [19] -->
Then, the next step is to rank all institutions with their respective maximal ROI. Given the budget constraint of money available ($100m), we pick up the institutions with the largest potential to improve on the performance indicator, namely the largest maximal ROI, until we exhaust the budget.

<!-- b000273 | prose | pages [19] -->
By following the two-step selection algorithm, we can derive the optimal investment strat- egy. And the results for year 1 and geographical distribution of selected institutions are pre- sented below in Table 4 and Fig 8.

<!-- b000274 | caption | pages [19] -->
Table 4: Investment Strategy of Year 1

<!-- b000275 | prose | pages [19] -->
UNITID names ROI donation 197027 United States Merchant Marine Academy 21.85% 2500000 102711 AVTEC-Alaska’s Institute of Technology 21.26% 7500000 187745 Institute of American Indian and Alaska Native Culture 20.99% 2000000 262129 New College of Florida 20.69% 6500000 216296 Thaddeus Stevens College of Technology 20.66% 3000000 229832 Western Texas College 20.26% 10000000 196158 SUNY at Fredonia 20.24% 5500000 234155 Virginia State University 20.04% 10000000 196200 SUNY College at Potsdam 19.75% 5000000 178615 Truman State University 19.60% 3000000 199120 University of North Carolina at Chapel Hill 19.51% 3000000 101648 Marion Military Institute 19.48% 2500000 187912 New Mexico Military Institute 19.31% 500000 227386 Panola College 19.28% 10000000 434584 Ilisagvik College 19.19% 4500000 199184 University of North Carolina School of the Arts 19.15% 500000 413802 East San Gabriel Valley Regional Occupational Program 19.09% 6000000 174251 University of Minnesota-Morris 19.09% 8000000 159391 Louisiana State University and Agricultural & Mechanical College 19.07% 8500000 403487 Wabash Valley College 19.05% 1500000

<!-- b000276 | heading | pages [19] -->
6 Extended Model

<!-- b000277 | prose | pages [19] -->
Currently, we have obtained a candidate list of institution with priority and appropriate amount of money for the donation to each institution in total. In this section, we incorporate other crucial elements into the baseline model.

<!-- b000278 | heading | pages [19] -->
6.1 Time Duration

<!-- b000279 | prose | pages [19, 20] -->
One element is the time duration that the organization’s money should be provided. In this paper, we propose two methods for two scenarios. Scenario 1 is where we have new data of every past year as time goes by; and Scenario 2 is where we predict the trends and determine 5-year investment strategy only based on the original dataset.

<!-- b000280 | furniture | pages [20] -->
Team # 42939

<!-- b000281 | furniture | pages [20] -->
Page 19 of 24

<!-- b000282 | caption | pages [20] -->
Figure 8: Geographical Distribution of Selected Institutions

<!-- b000284 | prose | pages [20] -->
In Scenario 1, we adopt a dynamic calibration method based on the outcome of institutions we have patronized. To be more speciﬁc, we ﬁrst determine the investment strategy for the ﬁrst year. And in year 2, we would have had access to new data of year 1. Then we apply the baseline model again with the new information or merged dataset. This would generate new results after the model learning from the latest behaviors of each institution and making the calibrations on the predicting patterns. Similarly, this updating method can be used in the donation years afterwards.

<!-- b000285 | prose | pages [20] -->
In Scenario 2, we adopt a partial calibration method based on the coefﬁcients we calculate with the original dataset. According to assumption A1, we can simply treat status of institu- tions we have not patronized as ﬁxed. And the only values changed are donation amounts and values of performance contributing variables of patronized institutions. This barely af- fects the post-LASSO procedure considering the large quantity of variables used in the process. However, this would lead to movement of points of patronized institutions in the scatterplots of performance contributing variables and donation amount. So we recommend to recalcu- late the ﬁtted curve and ROI and determine the investment strategy for year 2. As for how to determine the movement of points, below is the procedure:

<!-- b000286 | prose | pages [20] -->
• Find the institutions you have patronized in year 1;

<!-- b000287 | prose | pages [20] -->
• Add the amount you have patronized to their original donation amount;

<!-- b000288 | prose | pages [20] -->
X′ = X + ∆X

<!-- b000289 | prose | pages [20] -->
• Calculate the values of performance contributing variables as follows:

<!-- b000290 | prose | pages [20] -->
F ′ i = Fi + ROIi · ∆X

<!-- b000291 | prose | pages [20] -->
The results for Scenario 2 are presented below in Table 5 to Table 8:

<!-- b000292 | furniture | pages [21] -->
Team # 42939

<!-- b000293 | furniture | pages [21] -->
Page 20 of 24

<!-- b000294 | caption | pages [21] -->
Table 5: Investment Strategy of Year 2

<!-- b000295 | prose | pages [21] -->
UNITID names ROI donation 197027 United States Merchant Marine Academy 21.82% 2500000 102711 AVTEC-Alaska’s Institute of Technology 21.25% 7000000 187745 Institute of American Indian and Alaska Native Culture 20.93% 2000000 262129 New College of Florida 20.73% 6500000 216296 Thaddeus Stevens College of Technology 20.62% 3000000 229832 Western Texas College 20.23% 10000000 196158 SUNY at Fredonia 20.23% 5500000 234155 Virginia State University 20.02% 9000000 196200 SUNY College at Potsdam 19.74% 5000000 178615 Truman State University 19.64% 3000000 199120 University of North Carolina at Chapel Hill 19.52% 3000000 101648 Marion Military Institute 19.48% 2500000 187912 New Mexico Military Institute 19.31% 1500000 227386 Panola College 19.22% 9500000 434584 Ilisagvik College 19.19% 4500000 199184 University of North Carolina School of the Arts 19.18% 2500000 413802 East San Gabriel Valley Regional Occupational Program 19.13% 6000000 174251 University of Minnesota-Morris 19.07% 8000000 159391 Louisiana State University and Agricultural & Mechanical College 19.07% 8500000 403487 Wabash Valley College 19.00% 500000

<!-- b000296 | caption | pages [21] -->
Table 6: Investment Strategy of Year 3

<!-- b000297 | prose | pages [21, 22] -->
UNITID names ROI donation 197027 United States Merchant Marine Academy 21.65% 2000000 102711 AVTEC-Alaska’s Institute of Technology 21.29% 7000000 187745 Institute of American Indian and Alaska Native Culture 21.01% 2000000 216296 Thaddeus Stevens College of Technology 20.99% 3500000 262129 New College of Florida 20.87% 6000000 229832 Western Texas College 20.42% 9500000 196158 SUNY at Fredonia 20.42% 5500000 234155 Virginia State University 20.32% 9000000 196200 SUNY College at Potsdam 20.27% 5000000 178615 Truman State University 20.06% 3000000 187912 New Mexico Military Institute 20.00% 2000000 101648 Marion Military Institute 19.96% 2500000 199120 University of North Carolina at Chapel Hill 19.93% 2500000 227386 Panola College 19.87% 9500000 434584 Ilisagvik College 19.87% 4500000 199184 University of North Carolina School of the Arts 19.73% 2500000 413802 East San Gabriel Valley Regional Occupational Program 19.69% 6000000 174251 University of Minnesota-Morris 19.25% 8000000 142179 Eastern Idaho Technical College 19.15% 1000000 159391 Louisiana State University and Agricultural & Mechanical College 19.04% 7000000 403487 Wabash Valley College 3.16% 2000000 UNITID names ROI donation 197027 United States Merchant Marine Academy 21.72% 2000000 102711 AVTEC-Alaska’s Institute of Technology 21.34% 6500000 187745 Institute of American Indian and Alaska Native Culture 21.25% 2000000 216296 Thaddeus Stevens College of Technology 21.15% 4000000 262129 New College of Florida 21.13% 6500000 196158 SUNY at Fredonia 20.98% 2500000 229832 Western Texas College 20.92% 10000000 234155 Virginia State University 20.80% 9000000 187912 New Mexico Military Institute 20.73% 3000000 101648 Marion Military Institute 20.68% 2500000 196200 SUNY College at Potsdam 20.66% 1500000 178615 Truman State University 20.37% 4000000 199184 University of North Carolina School of the Arts 20.15% 2000000 227386 Panola College 19.66% 10000000 434584 Ilisagvik College 19.52% 4500000 199120 University of North Carolina at Chapel Hill 19.45% 2000000 413802 East San Gabriel Valley Regional Occupational Program 19.45% 6000000 174251 University of Minnesota-Morris 19.36% 8000000 142179 Eastern Idaho Technical College 19.35% 1500000 159391 Louisiana State University and Agricultural & Mechanical College 19.13% 7000000 111188 California Maritime Academy 18.98% 5500000

<!-- b000298 | furniture | pages [22] -->
Team # 42939

<!-- b000299 | furniture | pages [22] -->
Page 21 of 24

<!-- b000300 | caption | pages [22] -->
Table 7: Investment Strategy of Year 4

<!-- b000302 | caption | pages [22] -->
Table 8: Investment Strategy of Year 5

<!-- b000303 | prose | pages [22] -->
UNITID names ROI donation 197027 United States Merchant Marine Academy 21.65% 2000000 102711 AVTEC-Alaska’s Institute of Technology 21.20% 6500000 187745 Institute of American Indian and Alaska Native Culture 21.20% 2500000 216296 Thaddeus Stevens College of Technology 21.05% 4000000 262129 New College of Florida 20.83% 6500000 196158 SUNY at Fredonia 20.78% 2500000 229832 Western Texas College 20.56% 10000000 234155 Virginia State University 20.34% 10000000 187912 New Mexico Military Institute 20.25% 3000000 101648 Marion Military Institute 20.21% 2500000 196200 SUNY College at Potsdam 20.03% 1500000 178615 Truman State University 20.00% 4000000 199184 University of North Carolina School of the Arts 19.76% 2000000 227386 Panola College 19.58% 10000000 434584 Ilisagvik College 19.48% 4500000 199120 University of North Carolina at Chapel Hill 19.46% 2000000 413802 East San Gabriel Valley Regional Occupational Program 19.61% 6000000 174251 University of Minnesota-Morris 19.48% 8000000 142179 Eastern Idaho Technical College 19.35% 500000 159391 Louisiana State University and Agricultural & Mechanical College 18.95% 7000000 111188 California Maritime Academy 19.04% 5000000

<!-- b000304 | prose | pages [22] -->
By following above mentioned methods, it is viable to determine the time duration or the investment strategy across time dimension. This approach can effectively avoid waste on do- nations by calibrating or partially calibrating the baseline model.

<!-- b000305 | furniture | pages [23] -->
Team # 42939

<!-- b000306 | furniture | pages [23] -->
Page 22 of 24

<!-- b000307 | heading | pages [23] -->
6.2 Geographical Distribution

<!-- b000308 | prose | pages [23] -->
Another element that can be incorporated into the baseline model is the geographical distri- bution of donations. It matters in two ways.

<!-- b000309 | prose | pages [23] -->
First, regional equality often raises heated debate among citizens and demands appropri- ate treatment. Consequently, charitable organizations are supposed to avoid displaying clear pattern of regional disparity on donations. Second, according to decreasing marginal utility theory, it’s reasonable to diversify investment with respect to regions. Assuming graduates are more likely to get employed where their colleges are, the marginal utility of corresponding social beneﬁts, such as more taxpayers, smaller crime rate, and increase in GDP, would decline as donations are centralized.

<!-- b000310 | prose | pages [23] -->
To deal with this factor, we can simply divide institutions to different geographical groups, split the donations and then apply the model to every group. Another proposed approach is to apply the baseline model with discounted ROI rather than the original deﬁnition. If the baseline model selects more than a predetermined number of institutions from a single region, we discount the ROI of these investments. For example, we could halve the ROI of excessive investments (Speciﬁc discounting method might need further exploration). Then we deter- mine the strategy to maximize the sum of discounted ROI. In this manner, we could effectively alleviate regional related problems.

<!-- b000311 | heading | pages [23] -->
7 Conclusions and Discussion

<!-- b000312 | heading | pages [23] -->
Conclusions:

<!-- b000313 | prose | pages [23] -->
This paper manages to develop a fully data-based model to produce a provi- dent investment strategy that maximizing ROI. Our model exhibits a great potential in drawing the conclusions below:

<!-- b000314 | prose | pages [23] -->
• We formulate a performance index for each institution with principal component analysis and develop an appropriate concept for return of investment (ROI) for the charitable foundations like Goodgrant Foundation.

<!-- b000315 | prose | pages [23] -->
• We identify three main performance contributing variables that generate a strong impact on the performance index with post-LASSO procedure: percentage of students who re- ceive a Pell grant amount, the students that are part time and the student-to-faculty ratio.

<!-- b000316 | prose | pages [23] -->
• We derive the relation between the performance contributing variables and donation amount from a GAM ﬁtting model to predict ROI of performance contributing variables.

<!-- b000317 | prose | pages [23] -->
• The ﬁnal list of selected institutions and appropriate amount of donation is determined by a two-step selection algorithm.

<!-- b000318 | heading | pages [23] -->
Limitation and extensions:

<!-- b000319 | prose | pages [23] -->
Though our model successfully produced an investment strategy, it can be improved in several ways:

<!-- b000320 | prose | pages [23] -->
• Since only cross-section data is available, our results of time duration of donation can be improved if we have access to time-series.

<!-- b000321 | prose | pages [23] -->
• The post-LASSO selection only allows for a relatively simple linear model. A more gen- eral selection method is needed when applying to a complicated model.

<!-- b000322 | furniture | pages [24] -->
Team # 42939

<!-- b000323 | furniture | pages [24] -->
Page 23 of 24

<!-- b000324 | heading | pages [24] -->
References

<!-- b000325 | references | pages [24] -->
[1] Schifrin,

<!-- b000326 | references | pages [24] -->
M.,

<!-- b000327 | references | pages [24] -->
Chen L. (2015). Top 50 ROI Colleges:

<!-- b000328 | references | pages [24] -->
2015 Grateful Grads In-

<!-- b000329 | references | pages [24] -->
dex.

<!-- b000330 | references | pages [24] -->
http://www.forbes.com/sites/schifrin/2015/07/29/top50roicolleges2015grateful-

<!-- b000331 | references | pages [24] -->
gradsindex/#285011fc15cc/

<!-- b000332 | references | pages [24] -->
[2] Burke, J. C. (2002). Funding public colleges and universities for performance. SUNY Press.

<!-- b000333 | references | pages [24] -->
[3] Cave, M. (1997). The use of performance indicators in higher education: The challenge of

<!-- b000334 | references | pages [24] -->
the quality movement. Jessica Kingsley Publishers.

<!-- b000335 | references | pages [24] -->
[4] Serban, A. M., & Burke, J. C. (1998). Meeting the performance funding challenge: A nine-

<!-- b000336 | references | pages [24] -->
state comparative analysis. Public Productivity & Management Review, 157-176.

<!-- b000337 | references | pages [24] -->
[5] Banta, T. W., Rudolph, L. B., Van Dyke, J., & Fisher, H. S. (1996). Performance funding

<!-- b000338 | references | pages [24] -->
comes of age in Tennessee. The Journal of Higher Education, 23-45.

<!-- b000339 | references | pages [24] -->
[6] Burke, J. C. (1998). Performance funding indicators: Concerns, values, and models for

<!-- b000340 | references | pages [24] -->
state colleges and universities. New directions for institutional research, 1998(97), 49-60.

<!-- b000341 | references | pages [24] -->
[7] Little, R. J., & Rubin, D. B. (2014). Statistical analysis with missing data. John Wiley & Sons.

<!-- b000342 | references | pages [24] -->
[8] Ehrenberg, R. G. (2004). Econometric studies of higher education. Journal of econometrics,

<!-- b000343 | references | pages [24] -->
121(1), 19-37.

<!-- b000344 | references | pages [24] -->
[9] Rogg, K. L., Schmidt, D. B., Shull, C., & Schmitt, N. (2001). Human resource practices,

<!-- b000345 | references | pages [24] -->
organizational climate, and customer satisfaction. Journal of management, 27(4), 431-449.

<!-- b000346 | references | pages [24] -->
[10] Tibshirani, R. (1996). Regression shrinkage and selection via the lasso. Journal of the Royal

<!-- b000347 | references | pages [24] -->
Statistical Society. Series B (Methodological), 267-288.

<!-- b000348 | references | pages [24] -->
[11] Usai, M. G., Goddard, M. E., & Hayes, B. J. (2009). LASSO with cross-validation for ge-

<!-- b000349 | references | pages [24] -->
nomic selection. Genetics research, 91(06), 427-436.

<!-- b000350 | furniture | pages [25] -->
Team # 42939

<!-- b000351 | furniture | pages [25] -->
Page 24 of 24

<!-- b000352 | heading | pages [25] -->
Appendix

<!-- b000353 | caption | pages [25] -->
Figure 9: GAM Approximation of Share of Students Who Are Part-time vs Donation Amount

<!-- b000354 | caption | pages [25] -->
Figure 10: GAM Approximation of Student-to-faculty Ratio vs Donation Amount
