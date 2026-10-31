# P-C-2016-50193-615bc62f

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For ofﬁce use only

<!-- b000003 | prose | pages [1] -->
For ofﬁce use only

<!-- b000004 | title | pages [1] -->
50193

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

<!-- b000015 | prose | pages [1] -->
2016 MCM/ICM

<!-- b000016 | heading | pages [1] -->
Summary Sheet

<!-- b000017 | prose | pages [1] -->
An Educational Donation Mechanism Based On Data Insight

<!-- b000018 | heading | pages [1] -->
Summary

<!-- b000019 | prose | pages [1] -->
Recent years, Big Data has become increasingly popular and the guidance of big data is required in many ﬁelds, including charitable ﬁeld. In our paper, we construct a new ROI evaluation system for charitable organization using data mining methods to process data, and succeed in determining an optimal investment strategy for Goodgrant Foundation.

<!-- b000020 | prose | pages [1] -->
First, we operate on the data. We do data screening according to the integrity and re- dundancy of the information, deleting data with information less than the threshold, and merging different attributes using linear ﬁtting and PCA. For the reserved attributes and schools, we do data imputation to ﬁll the missing data based on K-means Clustering. Then we normalize all the data to make them comparable in the following analysis.

<!-- b000021 | prose | pages [1] -->
Second, we construct a ROI evaluation criteria, which is a ratio of output and input mul- tiplying an adjustment coefﬁcient, named “urgency”. The ratio reﬂects the beneﬁts in related to the cost, while urgency reﬂects the demand for money which is an important factor should be considered by charitable organization. We use PCA to select attributes, letting salary, education quality and some others to represent output, tuition to represent input and Federal loan, debt and some others to represent urgency. Then, AHP is used to measure the importance between different factors and allocate weights.

<!-- b000022 | prose | pages [1] -->
Third, we put forward two kinds of model, basic model for one year and time series model for ﬁve year. Seeing the ROI as beneﬁts from investment, we introduce the ﬂuctuation of output as “risk”, imitating the concept of Modern Portfolio Theory in the ﬁnancial sector to solve the problems. In the basic model, we develop a Mixed Integer Linear Pro- gramming Algorithm and succeed in ﬁnding 14 schools for the investment. Further, we consider the time factor and improve the model into a time series model, using MILP and Grey Prediction to determine the long-term investment strategy. 16 schools are chosen with different time duration and different amounts of money.

<!-- b000023 | prose | pages [1] -->
Finally, we make sensitivity analysis for our model, changing the amount of schools, the restriction for money, whether allocating the money equally or not and so on to analyze the different results of the output and to ﬁnd the better parameters for ideal results.

<!-- b000024 | prose | pages [1] -->
To sum up, our model is a feasible and reasonable model with technical and data support. Because of the subjectivity, this model can be used ﬂexibly after data training.

<!-- b000025 | furniture | pages [2] -->
Team # 50193

<!-- b000026 | heading | pages [2] -->
Contents

<!-- b000027 | contents | pages [2] -->
1

<!-- b000028 | heading | pages [2] -->
Introduction

<!-- b000029 | furniture | pages [2] -->
Page 2 of 22

<!-- b000030 | prose | pages [2] -->
3

<!-- b000031 | prose | pages [2] -->
Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 3

<!-- b000032 | prose | pages [2] -->
Overview of Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 3

<!-- b000033 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3

<!-- b000034 | heading | pages [2] -->
Assumptions

<!-- b000035 | prose | pages [2] -->
2

<!-- b000036 | heading | pages [2] -->
Data Processing

<!-- b000037 | prose | pages [2] -->
4

<!-- b000038 | prose | pages [2] -->
5

<!-- b000039 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.1 Data Screening 5

<!-- b000040 | prose | pages [2] -->
Data imputation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2 6

<!-- b000041 | prose | pages [2] -->
Data Normalization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.3

<!-- b000042 | prose | pages [2] -->
3 ROI Evaluation System

<!-- b000043 | prose | pages [2] -->
8

<!-- b000044 | prose | pages [2] -->
9

<!-- b000045 | prose | pages [2] -->
Concept of ROI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 9

<!-- b000046 | prose | pages [2] -->
Using Grey Theory to predict ROI . . . . . . . . . . . . . . . . . . . . . 3.2

<!-- b000047 | prose | pages [2] -->
4

<!-- b000048 | heading | pages [2] -->
Model Construction

<!-- b000049 | prose | pages [2] -->
12

<!-- b000050 | prose | pages [2] -->
13

<!-- b000051 | prose | pages [2] -->
Deﬁnition of Risk . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 14

<!-- b000052 | prose | pages [2] -->
Basic Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2 14

<!-- b000053 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3 Results of basic model 15

<!-- b000054 | prose | pages [2] -->
Time series model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.4 17

<!-- b000055 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . 4.5 Results of time series model

<!-- b000056 | prose | pages [2] -->
5

<!-- b000057 | heading | pages [2] -->
Sensitive analysis and validation

<!-- b000058 | prose | pages [2] -->
17

<!-- b000059 | prose | pages [2] -->
18

<!-- b000060 | prose | pages [2] -->
Risk-Return . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 18

<!-- b000061 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2 School number 18

<!-- b000062 | prose | pages [2] -->
Policy of distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.3

<!-- b000063 | prose | pages [2] -->
6

<!-- b000064 | heading | pages [2] -->
Future Work

<!-- b000065 | prose | pages [2] -->
7

<!-- b000066 | heading | pages [2] -->
Conclusion

<!-- b000067 | prose | pages [2] -->
19

<!-- b000068 | prose | pages [2] -->
20

<!-- b000069 | prose | pages [2] -->
21

<!-- b000070 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.1 Strengths 21

<!-- b000071 | prose | pages [2] -->
weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.2 21

<!-- b000072 | furniture | pages [3] -->
Team # 50193

<!-- b000073 | furniture | pages [3] -->
Page 3 of 22

<!-- b000074 | prose | pages [3] -->
1

<!-- b000075 | heading | pages [3] -->
Introduction

<!-- b000076 | prose | pages [3] -->
1.1

<!-- b000077 | heading | pages [3] -->
Background

<!-- b000078 | prose | pages [3] -->
If it were a decade ago, you would not image that the pageview of ”Facebook” can be more than millions in one minute; you would not image that when you open ”google maps”, all the travel information is already in the palm of your hand; you would not image that through data mining you can gain an insight into the development trend of an enterprise to guide your investment. Nowadays big data has penetrated into our work and lives, and has brought such huge changes. In turn, it has become particularly important for us to ﬁnd useful information from the mass of data to guide our work and life.

<!-- b000079 | prose | pages [3] -->
As a special column from ”New York Times” in Feb., 2012 says, Big Data Era has come. In the commercial, economic and other areas, information will increasingly be made based on data and analysis, rather than based on experience and intuition. Also the ﬁeld of charity is in the same case. In the past, it is more difﬁcult to give money away intelligently than to earn it in the ﬁrst place.[1] We do not know how to do the charitable giving rationally, thus, the calculation of ROI is also out of the question. But now new and faster information could make charitable giving more effective and efﬁcient. Moreover, it provides a possibility to link charitable giving issues with the investment issues in the ﬁnancial sector.

<!-- b000080 | prose | pages [3] -->
This article is about a charitable donation issue of universities in the U.S. We aim to design a measure system of the return on investment based on large quantities of data through data mining methods. To solve the problem, we will use the Portfolio Theory, Linear Programming, Grey Theory and some other methods to determine the optimal strategy in terms of dimension of time.

<!-- b000081 | prose | pages [3] -->
1.2 Overview of Our Work

<!-- b000082 | prose | pages [3] -->
First, we ﬁnd a few key points in this question :

<!-- b000083 | prose | pages [3] -->
• The volume of data is large and of different types. How to do the normalization of the data.

<!-- b000084 | prose | pages [3] -->
• Among the massive data, there are many missing data in the ﬁles, which contains less information and not easy to do batch processing.

<!-- b000085 | prose | pages [3] -->
• How to classify the large amount of attributes of universities.

<!-- b000086 | prose | pages [3] -->
• Different attributes focus on different aspects and how to judge their importance.

<!-- b000087 | prose | pages [3] -->
• How to choose schools from the candidate list and how the allocate investment amount among them.

<!-- b000088 | prose | pages [3] -->
• The charitable investment process lasts for 5 years, so time is an important factor which will inﬂuence our ROI criteria.

<!-- b000089 | furniture | pages [4] -->
Team # 50193

<!-- b000090 | furniture | pages [4] -->
Page 4 of 22

<!-- b000091 | prose | pages [4] -->
On the basis of above discussion, to determine the optimal investment strategy, we may boil down the tasks to the following four steps :

<!-- b000092 | prose | pages [4] -->
• First, we do data screening according to the integrity and usefulness of the informa- tion. For the retention attributes and schools, we use K-means clustering method to ﬁll the missing data. And normalize all the data.

<!-- b000093 | prose | pages [4] -->
• Second, we use PCA method to choose and classify different attributes. Then we use AHP method and knowledge of ﬁnance to construct ROI concept. And we use the ROI concept to process data, ranking the candidate schools.

<!-- b000094 | prose | pages [4] -->
• Third, we introduce the concept of Modern Portfolio Theory and construct two models. In the basic model, we develop a Mixed Integer Linear Programming Al- gorithm to determine an optimal investment strategy. Further, we consider the time factor and improve the model into a timing model, using Dynamic Programming Algorithm and Grey Prediction to determine the long-term investment strategy.

<!-- b000095 | prose | pages [4] -->
• Further analysis and discussion of the model.

<!-- b000096 | prose | pages [4] -->
1.3

<!-- b000097 | heading | pages [4] -->
Assumptions

<!-- b000098 | prose | pages [4] -->
• Ignore inﬂation and deﬂation of money and other time value of money. The value of money remains unchanged.

<!-- b000099 | prose | pages [4] -->
• As a charitable organization, our aim is to improve educational performance and expect for more social beneﬁts rather than gaining proﬁt.

<!-- b000100 | prose | pages [4] -->
• Our charitable donation is a comprehensive scholarship, not rewarding for the out- standing contributions in speciﬁc ﬁelds.

<!-- b000101 | prose | pages [4] -->
• If we have different goals and strategies from other charitable organization, we believe it can reduce the possibility of duplication of investment to a great extend.

<!-- b000102 | prose | pages [4] -->
• The object for evaluating and scholarship granting is school, not individual, though some individual information is included in our criteria. And it is business of school to allocate the money.

<!-- b000103 | prose | pages [4] -->
• We focus on the fairness of our strategy so as to invest more schools regardless of the reputation of them.

<!-- b000104 | prose | pages [4] -->
• Because of Marginal utility, we try not to invest large amount of money to one school.

<!-- b000105 | prose | pages [4] -->
• In the timing model, we assume that the inﬂuence of other factors which are ex- cluded outside the model can be ignored. That’s to say, future is predictable.

<!-- b000106 | furniture | pages [5] -->
Team # 50193

<!-- b000107 | furniture | pages [5] -->
Page 5 of 22

<!-- b000108 | prose | pages [5] -->
2

<!-- b000109 | heading | pages [5] -->
Data Processing

<!-- b000110 | prose | pages [5] -->
2.1 Data Screening

<!-- b000111 | prose | pages [5] -->
The amount of raw data is large, so we should ﬁrst do data screening according to the integrity and usefulness of the information.

<!-- b000112 | prose | pages [5] -->
First, we do data screening on 7805 schools :

<!-- b000113 | prose | pages [5] -->
• We only consider the 2978 candidate schools in the ﬁle Problem C - IPEDS UID for Potential Candidate Schools, and match the schools with their 95 attributes in the ﬁle Problem C - Most Recent Cohorts Data (Scorecard Elements).xlsx.

<!-- b000114 | prose | pages [5] -->
• Delete the schools which are not currently operating institution and which are on Heightened Cash Monitoring 2 by Department of Education, meaning that they encounter economic depression and lack students and which has no or very limited information about percentage of degrees awarded. It’s meaningless to invest on these schools.

<!-- b000115 | prose | pages [5] -->
• Delete the schools of whom 50% of the attributes are ”NULL”. If the percentage of missing data exceeds 50%, the imputation will result in great error, which we treat as a threshold for missing data.[2]

<!-- b000116 | prose | pages [5] -->
Second, we do data screening on 95 attributes :

<!-- b000117 | prose | pages [5] -->
• We combine some binary variables together. For example, we delete the net price for different income classes and combine the total net price for public school and private school together, named as ”Net Price”. And we use the total retention rate for weighting to combine retention rate for full-time and part-time students together, named as ”Retention Rate”.

<!-- b000118 | prose | pages [5] -->
• Though there are large quantities of missing data in ”SAT scores” and ”ACT scores”, we reserve the midpoint of them as categorical variables. High entrance require- ments with SAT or ACT scores would indicate higher education quality, which we will treat differently from the low entrance requirements school in the following ROI evaluation system.

<!-- b000119 | prose | pages [5] -->
• Besides, we reserve all the ﬂag attributes like ”ﬂag for Historically Black College and University”, ”ﬂag for women-only college” and all the subject attributes like ”percentage of degrees awarded in Architecture And Related Services”, using them for the clustering and data imputation in the next step.

<!-- b000120 | prose | pages [5] -->
• We delete location, age of students and some other information contributes less to our ROI evaluation system.

<!-- b000121 | prose | pages [5] -->
After data screening, there are about 2700 schools each with about 60 attributes in the candidate list.

<!-- b000122 | furniture | pages [6] -->
Team # 50193

<!-- b000123 | prose | pages [6] -->
2.2 Data imputation

<!-- b000124 | furniture | pages [6] -->
Page 6 of 22

<!-- b000125 | prose | pages [6] -->
In statistics, missing data occur when no data value is stored for the variable in an obser- vation. Missing data are a common occurrence and can have a signiﬁcant effect on the conclusions that can be drawn from the data.

<!-- b000126 | prose | pages [6] -->
• K-means Clustering

<!-- b000127 | prose | pages [6] -->
Many approaches are available for data imputation, such as Listwise Deletion, Mean Imputation, Regression Imputation and Multiple Imputation. Here we use K-means clustering imputation: ﬁrst using complete and meaningful data in the ﬁles to combine schools with similarity together, and then using the means of these similar schools to ﬁll the missing data.[2]. We can see it as an improved method for Mean Imputation.

<!-- b000128 | prose | pages [6] -->
Given a set of observations

<!-- b000129 | prose | pages [6] -->
(x1, x2, . . . , xn)

<!-- b000130 | prose | pages [6] -->
where each observation is a d-dimensional real vector, k-means clustering aims to partition the n observations into k sets

<!-- b000131 | prose | pages [6] -->
S = {S1, S2, . . . , Sk}

<!-- b000132 | prose | pages [6] -->
so as to minimize the within-cluster sum of distance functions of each point in the cluster to the K center.[3] In other words, its objective is to ﬁnd:

<!-- b000133 | prose | pages [6] -->
k X

<!-- b000134 | prose | pages [6] -->
min

<!-- b000135 | prose | pages [6] -->
i=1

<!-- b000136 | prose | pages [6] -->
where µi is the mean of points in Si.

<!-- b000137 | prose | pages [6] -->
2

<!-- b000138 | prose | pages [6] -->
X

<!-- b000139 | prose | pages [6] -->
(x −µi)

<!-- b000140 | prose | pages [6] -->
(1)

<!-- b000141 | prose | pages [6] -->
x∈Si

<!-- b000142 | prose | pages [6] -->
In the K-means algorithm, K is given in advance, but selecting the K value is very difﬁcult. According to the theory of variance, we often determine the K value based on the R2 statistic.[3]

<!-- b000143 | prose | pages [6] -->
nt

<!-- b000144 | prose | pages [6] -->
(X(t)

<!-- b000145 | prose | pages [6] -->
X

<!-- b000146 | prose | pages [6] -->
(t))′(X(t)

<!-- b000147 | prose | pages [6] -->
(t))

<!-- b000148 | prose | pages [6] -->
(i) −X

<!-- b000149 | prose | pages [6] -->
(i) −X

<!-- b000150 | prose | pages [6] -->
Wt =

<!-- b000151 | prose | pages [6] -->
i=1

<!-- b000152 | prose | pages [6] -->
k

<!-- b000153 | prose | pages [6] -->
nt

<!-- b000154 | prose | pages [6] -->
(2)

<!-- b000155 | prose | pages [6] -->
(X(t)

<!-- b000156 | prose | pages [6] -->
X

<!-- b000157 | prose | pages [6] -->
X

<!-- b000158 | prose | pages [6] -->
T =

<!-- b000159 | prose | pages [6] -->
t=1

<!-- b000160 | prose | pages [6] -->
i=1

<!-- b000161 | prose | pages [6] -->
(i) −X)′(X(t)

<!-- b000162 | prose | pages [6] -->
(i) −X) (3)

<!-- b000163 | prose | pages [6] -->
k X

<!-- b000164 | prose | pages [6] -->
Pk =

<!-- b000165 | prose | pages [6] -->
k X

<!-- b000166 | prose | pages [6] -->
Bk =

<!-- b000167 | prose | pages [6] -->
nt(X

<!-- b000168 | prose | pages [6] -->
t=1

<!-- b000169 | prose | pages [6] -->
Wt (4)

<!-- b000170 | prose | pages [6] -->
t=1

<!-- b000171 | prose | pages [6] -->
(t) −X)′(X

<!-- b000172 | prose | pages [6] -->
(t) −X) (5)

<!-- b000173 | prose | pages [6] -->
R2 = Bk

<!-- b000174 | prose | pages [6] -->
T = 1 −Pk

<!-- b000175 | prose | pages [6] -->
(6) T

<!-- b000176 | prose | pages [6] -->
The greater the proportion of sum of square between class is and the smaller the proportion of sum of square inner class is, the better K value is. So we choose the K value that maximize R2 value.

<!-- b000177 | furniture | pages [7] -->
Team # 50193

<!-- b000178 | furniture | pages [7] -->
Page 7 of 22

<!-- b000179 | prose | pages [7] -->
• Variables Choosing In our data ﬁles, the missing data columns needed to be ﬁlled are listed as below :

<!-- b000180 | caption | pages [7] -->
Table 1: Missing data columns

<!-- b000181 | prose | pages [7] -->
Number Variable Name 1 Net Price 2 Retention Rate Number Variable Name 6 gt 25k p6 7 md earn wne p10 GRAD DEBT MDN SUPP 3 4 8 sd earn wne p10 GRAD DEBT MDN10YR SUPP RPY 3YR RT SUPP 5 9 md earn wne p6 10 sd earn wne p6

<!-- b000182 | prose | pages [7] -->
These are all very important variables in our ROI evaluation system. For exam- ple, “Net Price“ is a measure of input of education, and “md earn wne p1“ means median earnings of students working and not enrolled 10 years after entry and is measure of output of education.

<!-- b000183 | prose | pages [7] -->
Having ﬁgured out on what variables to do data imputation, we should determine what variables should the imputation be based on. Following are some integral data columns for us to use :

<!-- b000184 | caption | pages [7] -->
Table 2: Integral data columns

<!-- b000185 | prose | pages [7] -->
Number Variable Name 1 PREDDEG CONTROL 2 3 HBCU PBI 4 5 ANNHI 6 TRIBAL AANAPII 7 8 HSI NANTI 9 Number Variable Name 10 MENONLY 11 WOMENONLY 12 PCIP XXXXX 13 DISTANCEONLY 14 UGDS 15 UGDS XXXXX 16 PPTUG EF 17 PCTFLOAN 18 PCTPELL

<!-- b000186 | prose | pages [7] -->
By contrast, these variables are more integral and have signiﬁcance to guide the imputation. For example, “PCIP XXXXX“ means Percentage of degrees awarded in different subjects (including 38 subjects), indicating the subjects composition of schools; “UGDS“ means the size of schools and “UGDS XXXXX“ means the percentage of students who are WHITE, BLACK, ASIAN and so on(including 9 different attributes), indicating the students composition of schools; and “PCT- FLOAN“ means percent of all federal undergraduate students receiving a federal student loan, indicating the students’ ﬁnancial situation of schools.

<!-- b000187 | prose | pages [7] -->
So we can believe that it has a good description of every school to consider the above variables together. Then the similarity and dissimilarity of schools can be found.

<!-- b000188 | prose | pages [7] -->
• Clustering Output To simplify the model, we only do the K-means clustering once using all the data from integral data columns. We assume that the classiﬁcation using all the integral variables is applicable to all the missing variables. And we

<!-- b000189 | furniture | pages [8] -->
Team # 50193

<!-- b000190 | furniture | pages [8] -->
Page 8 of 22

<!-- b000191 | prose | pages [8] -->
choose the number of classes K from 3 to 8, ending up ﬁnding the optimal value is 5.

<!-- b000192 | prose | pages [8] -->
After clustering, we can believe that the schools in the same class have the maxi- mum similarity. So, we use the means of data of no-missing-data schools from each missing variable column to ﬁll the corresponding blanks of missing-data schools in the same class.

<!-- b000193 | prose | pages [8] -->
Following is the results of K-means clustering and an example of the imputation value of “md earn wne p10“ :

<!-- b000194 | caption | pages [8] -->
Table 3: Clustering Output and Imputation Value

<!-- b000195 | prose | pages [8] -->
Number Size 1 27 2 5 3 1151 4 1499 5 11 md earn wne p10 19655.56 24980.11 31176.46 40780.52 42063.64

<!-- b000196 | prose | pages [8] -->
From above table, the value of “md earn wne p10“ for each of the ﬁve classes is the means value of no-missing-data schools and what we should do next is to ﬁll the value into blank in each class. The same approach is used in all the missing data columns. Up to now, we get the integral value of all the schools with all the attributes.

<!-- b000197 | prose | pages [8] -->
2.3 Data Normalization

<!-- b000198 | prose | pages [8] -->
After ﬁlling all the missing data, we should do the data normalization to facilitate the further analysis of the data. It can provide an approach for comparison of different kinds of data and reﬂect the combined results of different factors.

<!-- b000199 | prose | pages [8] -->
Here we use Min-max normalization, doing linear transformation of the raw data, map- ping data set

<!-- b000200 | prose | pages [8] -->
x = {x1, x2, . . . , xn}

<!-- b000201 | prose | pages [8] -->
into [0,1] interval. Let x′ be the normalized value, the formula is :

<!-- b000202 | prose | pages [8] -->
x −xmin x′ =

<!-- b000203 | prose | pages [8] -->
(7)

<!-- b000204 | prose | pages [8] -->
xmax −xmin

<!-- b000205 | prose | pages [8] -->
While x′

<!-- b000206 | prose | pages [8] -->
min = 0 and x′

<!-- b000207 | prose | pages [8] -->
max = 1. And all the data hereinafter is normalized data.

<!-- b000208 | furniture | pages [9] -->
Team # 50193

<!-- b000209 | furniture | pages [9] -->
Page 9 of 22

<!-- b000210 | prose | pages [9] -->
3 ROI Evaluation System

<!-- b000211 | prose | pages [9] -->
3.1 Concept of ROI

<!-- b000212 | prose | pages [9] -->
In this part, we focus our attention on how to determine the Return on Investment evalu- ation system. In the ﬁnancial sector, ROI is the beneﬁt to the investor resulting from an investment of some resource, which is a way of considering proﬁts in relation to capital invested. According to the original concept, we use the available data to construct a new ROI evaluation system appropriate for our charitable organization. The formula is :

<!-- b000213 | prose | pages [9] -->
ROI = Output

<!-- b000214 | prose | pages [9] -->
Input × Urgency (8)

<!-- b000215 | heading | pages [9] -->
1. Output

<!-- b000216 | prose | pages [9] -->
Output is the measure of the quantity of education, in other words, effectiveness. Here we use four factors to measure Output : Salary After Graduation, Retention Rate, Repayment Ability and Education Enhance Rate. But why these four factors?

<!-- b000217 | prose | pages [9] -->
• First, there is low correlation among the four factors, each of which can be separated out as an impact indicator of Output. To illustrate the independence, and the relationship between different variables, we use Principal Component Analysis(PCA), which is a statistical procedure that uses an orthogonal trans- formation to convert a set of observations of possibly correlated variables into a set of values of linearly uncorrelated variables.[4] When some of the vari- ables can explain a great percentage of the results, we can say these variables are strongly correlated and we can use the great one to represent others.

<!-- b000218 | prose | pages [9] -->
• Second, they are strongly related to Output of a school :

<!-- b000219 | prose | pages [9] -->
(a) Salary After Graduation(SAG) : measures the overall level of students.

<!-- b000220 | prose | pages [9] -->
More salary means the students’ job can make more valuable output. So they can contribute more to the society when they receive the same amount of donation. There are three factors representing salary, “md earn

<!-- b000221 | prose | pages [9] -->
wne p10”, “md earn wne p6” and “gt 25k p6”, meaning midpoint earn- ing in 10 years, midpoint earning in 6 years and share of students earning over $25,000 per year in 6 years. Similarly, using PCA to study the corre- lation between them and assign weights, we ﬁnd that the three factors are strongly related and one of them, “md earn wne p6”, can explain 95% of the result. So we only use the value of “md earn wne p6” to represent Salary After Graduation.

<!-- b000222 | prose | pages [9] -->
(b) Retention Rate(RR) : measures the utilization of the investment. On the

<!-- b000223 | prose | pages [9] -->
one hand, the larger the retention rate is, the more students retained in schools will enjoy the investment. And on the other hand, higher reten- tion rate means greater school spirit and learning atmosphere, which is worthy of investment. “Retention Rate” has been deﬁned above.

<!-- b000224 | prose | pages [9] -->
(c) Repayment Ability(RA) : measures the ability to contribute to the soci-

<!-- b000225 | furniture | pages [10] -->
Team # 50193

<!-- b000226 | furniture | pages [10] -->
Page 10 of 22

<!-- b000227 | prose | pages [10] -->
ety. There is difference between Salary After Graduation and this fac- tor. The former emphasize the potential ability, while higher Repay- ment Ability shows that it is no longer subject to the debt or other bur- den in life, and have real ability to contribute to society. Here we use “RPY 3YR RT SUPP” to represent Repayment Ability.

<!-- b000228 | prose | pages [10] -->
(d) Education Enhance Rate(EER) : measures the education quality of schools.

<!-- b000229 | prose | pages [10] -->
Here we use normalized data of “md earn wne p6” minus normalized data of “SAT scores” and then normalize it again to represent the Edu- cation Enhance Rate. Because the salary can reﬂect the level of students after graduation and the “SAT scores” can reﬂect the level before entry. As for the schools without “SAT scores”, this weight will be assigned to other three factors.

<!-- b000230 | prose | pages [10] -->
In order to get the overall evaluation index, we need to compute the weight of the four factors. In the following, analytical hierarchy process, abbreviated to AHP, will be applied to judge importance of the four factors. We compare the four factors by pairs and give the following matrix according to experience and intuition. (the columns indicate Salary After Graduation, Retention Rate, Repayment Ability and Education Enhance Rate from left to right)

<!-- b000231 | prose | pages [10] -->


<!-- b000232 | prose | pages [10] -->
1 3

<!-- b000233 | prose | pages [10] -->


<!-- b000234 | prose | pages [10] -->
2 1 3

<!-- b000235 | prose | pages [10] -->


<!-- b000236 | prose | pages [10] -->
5 6 3 1 1 2

<!-- b000237 | prose | pages [10] -->


<!-- b000238 | prose | pages [10] -->
2 1 1 1 2 3 1 1 1 6 5

<!-- b000239 | prose | pages [10] -->
Thus, we can ﬁgure out that the weight vector V1 = [0.576 0.125 0.077 0.222]. Finally, in consistency check, the consistency index CI = 0.0113 < 0.10, which means that the weight determined by AHP is very reasonable [5].

<!-- b000240 | prose | pages [10] -->
As for the schools without “SAT scores”, we assign the weight of EER to other three factors and use the same AHP method. The weight vector is V2 = [0.741 0.161 0.098], also passing the consistency check.

<!-- b000241 | prose | pages [10] -->
AHP which we adopted here is the mostly widely used method in the evaluation of the weight, though its objectivity is pretty poor. Nevertheless, the weight deﬁned by objective method cannot match its importance in practice completely. As to the subjective method, it can reﬂect difference of relative importance among the four indexes in spite of the subject process to deﬁne the indexes’ weight. Considering the evaluation of the importance of these four indexes is a subjective judgement, weight deﬁning through the subjective method possesses more scientiﬁc rationality. So we utilize the more subjective AHP method rather than other more objective model to gain the weight.

<!-- b000242 | prose | pages [10] -->
Finally, the comprehensive calculation formula is described as :

<!-- b000243 | prose | pages [10] -->
(

<!-- b000244 | prose | pages [10] -->


<!-- b000245 | prose | pages [10] -->
V1 ·

<!-- b000246 | prose | pages [10] -->
Output =

<!-- b000247 | prose | pages [10] -->
V2 ·

<!-- b000248 | prose | pages [10] -->
T

<!-- b000249 | prose | pages [10] -->
SAG RR RA EER

<!-- b000250 | prose | pages [10] -->
(9) T

<!-- b000251 | prose | pages [10] -->
 

<!-- b000252 | prose | pages [10] -->
SAG RR RA

<!-- b000253 | furniture | pages [11] -->
Team # 50193

<!-- b000254 | heading | pages [11] -->
2. Input

<!-- b000255 | furniture | pages [11] -->
Page 11 of 22

<!-- b000256 | prose | pages [11] -->
Adding Input into the ROI formula, we can get a ratio considering proﬁts in relation to capital invested, in other word, efﬁciency. It means given one dollar, schools with low Input and high Output can create more value. Here we only have one factor, “Net Price”(NP), to represent the Input. We believe that high tuition means the schools need high input to maintain daily routine. “Net Price” has been deﬁned above.

<!-- b000257 | prose | pages [11] -->
There is a problem that the only factor in Input will have huge inﬂuence than the factors in the Output, resulting that the schools with lower tuition will get higher ROI. So we add a correction index “α” (α ∈[0,1]) to verify the formula.

<!-- b000258 | prose | pages [11] -->
Input = (1 −α) + α × NP

<!-- b000259 | prose | pages [11] -->
Here we let α = 0.25.

<!-- b000260 | heading | pages [11] -->
3. Urgency

<!-- b000261 | prose | pages [11] -->
(10)

<!-- b000262 | prose | pages [11] -->
For ﬁnance issue, the deﬁnition of ROI with Input and Output is enough. But for this charitable issue, we add an correction index, “Urgency”, to make the deﬁnition more robust. Because charitable organization should donate money to the people who are the most eager for it. Here we use three factors to measure Urgency : Pell Grants, Federal Loan, Debt. Similarly, we choose these three indexes because of the independence and meaningfulness.

<!-- b000263 | prose | pages [11] -->
(a) Pell Grants(PG) : measures students’ degree of demand for funds in different

<!-- b000264 | prose | pages [11] -->
schools. Here we use “PCTPELL”, percentage of undergraduates who receive a Pell Grant, to represent PG.

<!-- b000265 | prose | pages [11] -->
(b) Federal Loan(FL) : have the similar meaning of PG. Here we use “PCT-

<!-- b000266 | prose | pages [11] -->
FLOAN”, percent of all federal undergraduate students receiving a federal student loan to present it.

<!-- b000267 | prose | pages [11] -->
(c) Debt : measures the degree of liability in different schools. There are two fac-

<!-- b000268 | prose | pages [11] -->
tors, “GRAD DEBT MDN SUPP” and “GRAD DEBT MDN10YR SUPP” related to Debt, but they are strongly related. So we choose “GRAD DEBT M DN SUPP”, median debt of completers, suppressed for n=30, to represent Debt. Though three factors have very similar meaning, the PCA indicates they are independent, each explains 31%, 13%, 56% of the result. We use these three number as their importance in AHP, and get the ﬁnal weight vector V3 = [0.25 0.25 0.50], the consistency index CI = 0.0089 < 0.10.

<!-- b000269 | prose | pages [11] -->
Urgency = V3 ·

<!-- b000270 | prose | pages [11] -->
T

<!-- b000271 | prose | pages [11] -->
 

<!-- b000272 | prose | pages [11] -->
PG FL Debt

<!-- b000273 | prose | pages [11] -->
(11)

<!-- b000274 | prose | pages [11] -->
On the basis of the discussion above, we draw a picture to visually represent our ROI evaluation system.

<!-- b000275 | furniture | pages [12] -->
Team # 50193

<!-- b000276 | furniture | pages [12] -->
Page 12 of 22

<!-- b000277 | caption | pages [12] -->
Figure 1: The model of ROI evaluation system

<!-- b000278 | prose | pages [12] -->
3.2 Using Grey Theory to predict ROI

<!-- b000279 | prose | pages [12] -->
On the following discussion, we have ﬁgured out what the ROI is, and how to calculate the ROI of schools for one year using given data. But the charitable donation will be given for 5 years. In the long run, we can use Grey Theory to predict the future ROI using the previous data.

<!-- b000280 | prose | pages [12] -->
Grey Theory focuses on model uncertainty and information insufﬁciency in analyzing and understanding systems via research on conditional analysis, prediction and decision- making[7]. This theory is applied mainly on in-complete and un-determinable problems. GM(1,1) is one of models of gray theory. which uses an accumulated generation op- eration(AGO) and some equations to produce an inﬁnite grey sequences to predict the following data with observed data. Step 1. Let be a sequence of observed data

<!-- b000281 | prose | pages [12] -->
X(0) = (X(0)(1), X(0)(2), ......, X(0)(n)) (12)

<!-- b000282 | prose | pages [12] -->
where X(0)(i) represents the observed data with respect to time i. Step 2. Generate the ﬁrst-order accumulated generating operation (1 −AGO) sequence X(1)(i) based on the observed sequence X(0)(i)

<!-- b000283 | prose | pages [12] -->
X(1) = (X(1)(1), X(1)(2), ......, X(1)(n)) (13)

<!-- b000284 | prose | pages [12] -->
where X(1)(k) is formed as the following formula

<!-- b000285 | prose | pages [12] -->
k X

<!-- b000286 | prose | pages [12] -->
X(1)(k) =

<!-- b000287 | prose | pages [12] -->
X(0)(i) = X(1)(k −1) + X(0)(k) (14)

<!-- b000288 | prose | pages [12] -->
i=1

<!-- b000289 | furniture | pages [13] -->
Team # 50193

<!-- b000290 | furniture | pages [13] -->
Page 13 of 22

<!-- b000291 | prose | pages [13] -->
Step 3. Establish the ﬁrst-order differential equation of sequence X(1)(k)

<!-- b000292 | prose | pages [13] -->
dX(1)

<!-- b000293 | prose | pages [13] -->
+ aX(1) = u dt (15)

<!-- b000294 | prose | pages [13] -->
Step 4. Derive the estimated ﬁrst-order AGO sequence

<!-- b000295 | prose | pages [13] -->
ˆX(1)(k + 1) = (X(0)(1) −u

<!-- b000296 | prose | pages [13] -->
a)e−ak + u

<!-- b000297 | prose | pages [13] -->
(16) a

<!-- b000298 | prose | pages [13] -->
Step 5. Let ˆa be a sequence of parameters where ˆa = [a, u]T, it can be solved as follow :

<!-- b000299 | prose | pages [13] -->
ˆa = (BTB)−1BTYn

<!-- b000300 | prose | pages [13] -->
where

<!-- b000301 | prose | pages [13] -->
−1

<!-- b000302 | prose | pages [13] -->
(17)

<!-- b000303 | prose | pages [13] -->
2(X(1)(1) + X(1)(2))

<!-- b000304 | prose | pages [13] -->


<!-- b000305 | prose | pages [13] -->
−1

<!-- b000306 | prose | pages [13] -->


<!-- b000307 | prose | pages [13] -->
1

<!-- b000308 | prose | pages [13] -->
2(X(1)(2) + X(1)(3))

<!-- b000309 | prose | pages [13] -->


<!-- b000310 | prose | pages [13] -->
B =

<!-- b000311 | prose | pages [13] -->
−1 1

<!-- b000312 | prose | pages [13] -->
 (18)

<!-- b000313 | prose | pages [13] -->
.......

<!-- b000314 | prose | pages [13] -->
2(X(1)(n −1) + X(1)(n))

<!-- b000315 | prose | pages [13] -->
and

<!-- b000316 | prose | pages [13] -->
1

<!-- b000317 | prose | pages [13] -->
Yn = [X(0)(2), X(0)(3), ......, X(0)(n)]T (19)

<!-- b000318 | prose | pages [13] -->
According to Grey Theory illustrated as above, we use the data of past 5 years, from 2009 to 2013, to predict the future ROI from 2016 to 2020. Following are some ﬁgures of outcome of Grey Prediction for different schools. We can see that complex trend can be ﬁt with grey prediction and it’s better than Linear Fitting.

<!-- b000319 | prose | pages [13] -->
(a) Grey Predicting for Future ROI (b) Grey Predicting for Future ROI

<!-- b000320 | caption | pages [13] -->
Figure 2: general title.

<!-- b000321 | prose | pages [13] -->
4

<!-- b000322 | heading | pages [13] -->
Model Construction

<!-- b000323 | prose | pages [13] -->
The allocation strategy of the Goodgrant foundation given ROI and risk can be modeled as a mixed integer linear programming. At ﬁrst, in the basic model, we ignore the time factor and suppose that we allocate all the fund in one period. The objective is to max- imize the total return of the foundation, and constraints include the control of the risk, the minimize and maximize number of school is awarded, the minimize and maximize

<!-- b000324 | furniture | pages [14] -->
Team # 50193

<!-- b000325 | furniture | pages [14] -->
Page 14 of 22

<!-- b000326 | prose | pages [14] -->
money a school can get and the size of school. We introduce a continuous decision vari- able to denote the fund each school received and a binary variable to indicate whether the school is invested or not. Then, in the complicated model, we take the time period into consideration. Finally, we give two recommendation list in term of both models respectively.

<!-- b000327 | prose | pages [14] -->
4.1 Deﬁnition of Risk

<!-- b000328 | prose | pages [14] -->
In ﬁnancial sector, Modern Portfolio Theory was used to measure risk and beneﬁts, draw- ing the Efﬁcient Frontier of all the risky assets and ﬁnd the Tangency Portfolio.[6] For an investment, risk is certainly attached to beneﬁts. For charitable investment, there also ex- ists risk, which will forbid investment reaching the optimal point though it does not bring any lost for you. Above we have discussed the ROI for charitable investment, which can be seen as beneﬁts. Here we will deﬁne “risk” for our investment.

<!-- b000329 | prose | pages [14] -->
r = σe

<!-- b000330 | prose | pages [14] -->
(20)

<!-- b000331 | prose | pages [14] -->
µe

<!-- b000332 | prose | pages [14] -->
In the formula, we use the concept of coefﬁcient of variation. σe indicates the standard deviation of “md earn wne p6”, and µe indicates the means of “md earn wne p6”. This variable is the only measure we can ﬁnd of ﬂuctuation of the Output, larger ﬂuctuation of Output leads to larger risk. And using ratio form to indicate risk is to prevent the inﬂuence of the different amounts of Output itself. Then we use the concept of Modern Portfolio Theory, drawing risk-beneﬁt plots, using Mixed Integer Linear Programming(MILP) to solve the problem.

<!-- b000333 | prose | pages [14] -->
4.2

<!-- b000334 | heading | pages [14] -->
Basic Model

<!-- b000335 | prose | pages [14] -->
Denote the list of candidate school is i ∈S = {1, 2, ..., S}, the constant and the variables are as following.

<!-- b000336 | caption | pages [14] -->
Table 4: constant

<!-- b000337 | prose | pages [14] -->
ROI of school i, i ∈S ROIi risk of school i, i ∈S ri

<!-- b000338 | prose | pages [14] -->
maximum investment in school i, i ∈S

<!-- b000339 | prose | pages [14] -->
Amax

<!-- b000340 | prose | pages [14] -->
i

<!-- b000341 | prose | pages [14] -->
minimum investment in school i, i ∈S

<!-- b000342 | prose | pages [14] -->
Amin

<!-- b000343 | prose | pages [14] -->
i number of student in school i, i ∈S si N max maximum investment school number N min minimum investment school number rmax maximum acceptable risk Smin minimum acceptable student number A sum of the fund

<!-- b000344 | caption | pages [14] -->
Table 5: variable

<!-- b000345 | prose | pages [14] -->
Investment of school i, i ∈S xi

<!-- b000346 | prose | pages [14] -->
State of school i ,0 means not the the prize list, yi ∈{0, 1} 1 means in the recommendation list ,0 means not in the recommendation list

<!-- b000347 | furniture | pages [15] -->
Team # 50193

<!-- b000348 | furniture | pages [15] -->
Page 15 of 22

<!-- b000349 | prose | pages [15] -->
The objective is to maximize the total return, since the ROI is deﬁne as rate of return, it yields:

<!-- b000350 | prose | pages [15] -->
X

<!-- b000351 | prose | pages [15] -->
max

<!-- b000352 | prose | pages [15] -->
i∈S

<!-- b000353 | prose | pages [15] -->
ROIixi (21)

<!-- b000354 | prose | pages [15] -->
The sum of the money each school get should not exceed the total amount of the available money. The average risk of the allocation strategy should not beyond the maximum acceptable risk, we get:

<!-- b000355 | prose | pages [15] -->
X

<!-- b000356 | prose | pages [15] -->
i∈S

<!-- b000357 | prose | pages [15] -->
X

<!-- b000358 | prose | pages [15] -->
xi ≤A (22)

<!-- b000359 | prose | pages [15] -->
rixi ≤A · rmax

<!-- b000360 | prose | pages [15] -->
i∈S

<!-- b000361 | prose | pages [15] -->
(23)

<!-- b000362 | prose | pages [15] -->
The number of school that get some foundation should less that the maximum number N max and greater than minimum number N min

<!-- b000363 | prose | pages [15] -->
N min ≤

<!-- b000364 | prose | pages [15] -->
X

<!-- b000365 | prose | pages [15] -->
i∈S

<!-- b000366 | prose | pages [15] -->
yi ≤N max (24)

<!-- b000367 | prose | pages [15] -->
The basic logical constraints between xi and yi, i.e., xi ≥0, if and only if yi = 1, if school i is invested, the amount of the money it gets should lies within the Amin

<!-- b000368 | prose | pages [15] -->
Amax

<!-- b000369 | prose | pages [15] -->
, it yields: i

<!-- b000370 | prose | pages [15] -->
and i

<!-- b000371 | prose | pages [15] -->
∀i ∈S

<!-- b000372 | prose | pages [15] -->
yi ≤xi ≤Amin

<!-- b000373 | prose | pages [15] -->
Amin

<!-- b000374 | prose | pages [15] -->
i

<!-- b000375 | prose | pages [15] -->
yi (25) i

<!-- b000376 | prose | pages [15] -->
Finally, if the school is too small, we wouldn’t chose it since the fund wouldn’t beneﬁt enough students.

<!-- b000377 | prose | pages [15] -->
siyi ≤Smin

<!-- b000378 | prose | pages [15] -->
4.3

<!-- b000379 | heading | pages [15] -->
Results of basic model

<!-- b000380 | prose | pages [15] -->
∀i ∈S (26)

<!-- b000381 | prose | pages [15] -->
In the model, ROIi and ri is derived from the pervious work, we set the minimum ac- ceptable student number Smin as 1000, the minimum fund Amin

<!-- b000382 | prose | pages [15] -->
for the school which is i chosen can get as 20000000, since the maximum foundation the school can get is related to the school’s student number, we set Amax

<!-- b000383 | prose | pages [15] -->
i = Amin

<!-- b000384 | prose | pages [15] -->
+b∗si where b = 3000. Finally, we i deﬁne that the foundation must be awarded to at most 30 schools and at least 10 schools. Suppose the decision maker doesn’t care the risk so much, that is, the highest return is the only purpose, by using ILOG CPLEX 12.6 with python API, we get a list of schools that should be recommended according to our model (Ranking according to the ROI).

<!-- b000385 | furniture | pages [16] -->
Team # 50193

<!-- b000386 | furniture | pages [16] -->
Page 16 of 22

<!-- b000387 | caption | pages [16] -->
Table 6: Missing data columns

<!-- b000388 | prose | pages [16] -->
1 446604 Uta Mesivta of Kiryas Joel 2 133979 Florida Memorial University 3 385619 Everglades University 4 197018 United Talmudical Seminary 5 445708 Johnson Wales University-Charlotte 6 414823 Johnson Wales University-North Miami 7 161226 University of Maine at Farmington 8 216667 Washington Jefferson College 9 195128 The Sage Colleges 10 381617 Baker College of Port Huron 11 213251 Juniata College 12 196200 SUNY College at Potsdam 13 146427 Knox College 14 439288 Johnson Wales University-Denver

<!-- b000389 | caption | pages [16] -->
Figure 3: Factors of the investment schools

<!-- b000390 | caption | pages [16] -->
Figure 4: Allocation of the money

<!-- b000391 | furniture | pages [17] -->
Team # 50193

<!-- b000392 | furniture | pages [17] -->
Page 17 of 22

<!-- b000393 | prose | pages [17] -->
Figure(3) shows the factors of the ROI, including risk, output, input and urgency, of the schools that is selected by our model. Figure(4) shows the money allocation of each selected schools, the labels of both ﬁgures are the UNITID of the school.

<!-- b000394 | prose | pages [17] -->
4.4

<!-- b000395 | heading | pages [17] -->
Time series model

<!-- b000396 | prose | pages [17] -->
In the real situation, according to the requirement of the Goodgrant foundation, the total 1000000000 will be distributed to the schools in 5 years, so we modiﬁed our previous mixed integer problem and take the time series into consideration. Similarly, we induce

<!-- b000397 | prose | pages [17] -->
i, in which the time series t ∈T = {1, 2, 3, 4, 5}, corre-

<!-- b000398 | prose | pages [17] -->
the decision variables xt

<!-- b000399 | prose | pages [17] -->
i and yt

<!-- b000400 | prose | pages [17] -->
sponding to year 2016,2017,2018,2019,2020 respectively. The whole model is listed as follows:

<!-- b000401 | prose | pages [17] -->
X

<!-- b000402 | prose | pages [17] -->
max

<!-- b000403 | prose | pages [17] -->
i∈S

<!-- b000404 | prose | pages [17] -->
Subject to:

<!-- b000405 | prose | pages [17] -->
X

<!-- b000406 | prose | pages [17] -->
X

<!-- b000407 | prose | pages [17] -->
i∈S

<!-- b000408 | prose | pages [17] -->
t∈T

<!-- b000409 | prose | pages [17] -->
X

<!-- b000410 | prose | pages [17] -->
X

<!-- b000411 | prose | pages [17] -->
rt

<!-- b000412 | prose | pages [17] -->
ixt

<!-- b000413 | prose | pages [17] -->
i∈S

<!-- b000414 | prose | pages [17] -->
t∈T

<!-- b000415 | prose | pages [17] -->
N min ≤

<!-- b000416 | prose | pages [17] -->
X

<!-- b000417 | prose | pages [17] -->
X

<!-- b000418 | prose | pages [17] -->
ROIt

<!-- b000419 | prose | pages [17] -->
ixt

<!-- b000420 | prose | pages [17] -->
(27) i

<!-- b000421 | prose | pages [17] -->
t∈T

<!-- b000422 | prose | pages [17] -->
xt

<!-- b000423 | prose | pages [17] -->
i ≤A (28)

<!-- b000424 | prose | pages [17] -->
i ≤A · rmax (29)

<!-- b000425 | prose | pages [17] -->
∀t ∈T i ≤N max

<!-- b000426 | prose | pages [17] -->
yt

<!-- b000427 | prose | pages [17] -->
i∈S

<!-- b000428 | prose | pages [17] -->
Amin

<!-- b000429 | prose | pages [17] -->
yt

<!-- b000430 | prose | pages [17] -->
i ≤xi ≤Amin

<!-- b000431 | prose | pages [17] -->
i

<!-- b000432 | prose | pages [17] -->
i

<!-- b000433 | prose | pages [17] -->
siyt

<!-- b000434 | prose | pages [17] -->
i ≤Smin

<!-- b000435 | prose | pages [17] -->
4.5

<!-- b000436 | heading | pages [17] -->
Results of time series model

<!-- b000437 | prose | pages [17] -->
(30)

<!-- b000438 | prose | pages [17] -->
∀t ∈T, ∀i ∈S

<!-- b000439 | prose | pages [17] -->
yt

<!-- b000440 | prose | pages [17] -->
(31) i

<!-- b000441 | prose | pages [17] -->
∀t ∈T, ∀i ∈S (32)

<!-- b000442 | prose | pages [17] -->
The constants in the time series model is similar to the previous one with some minor adjustment, particularly, we set Amin

<!-- b000443 | prose | pages [17] -->
as 5000000 and b as 8000, the value of ROIt i

<!-- b000444 | prose | pages [17] -->
rt i and

<!-- b000445 | prose | pages [17] -->
i is determined by the previous calculation. By using IBM ILOG CPLEX, we solve the model, get the global optimal solution and receive the following result:

<!-- b000446 | caption | pages [17] -->
Figure 5: list of ﬁve years

<!-- b000447 | furniture | pages [18] -->
Team # 50193

<!-- b000448 | furniture | pages [18] -->
Page 18 of 22

<!-- b000449 | prose | pages [18] -->
From the result, we not only select the school but also determine in which years they should be invested in order to maximize the total revenue. In this way, we also, determine the investment period of each school. What’s more, since in our model, we don’t require that foundation is evenly distributed among ﬁve years, instead, we set a upper bound and a lower bound of the total investment in each year. We ﬁnd that actually we should increase the money we invest as time pass by.

<!-- b000450 | prose | pages [18] -->
5

<!-- b000451 | heading | pages [18] -->
Sensitive analysis and validation

<!-- b000452 | prose | pages [18] -->
5.1 Risk-Return

<!-- b000453 | prose | pages [18] -->
In basic model, we change the maximum acceptable risk and analyze the max return, the result are as follow:

<!-- b000454 | caption | pages [18] -->
Figure 6: Return-Risk

<!-- b000455 | prose | pages [18] -->
From the ﬁgure(6), we ﬁnd that as the max acceptable risk become greater, the max return we can get also become greater, which conform to our expectation and reality. Moreover, when the max acceptable risk index is greater than about 0.82, the max return will not increase anymore.

<!-- b000456 | prose | pages [18] -->
5.2 School number

<!-- b000457 | prose | pages [18] -->
In the time series model, we change the number of the schools that should be chosen and analyze the max return, the result are as follow:

<!-- b000458 | furniture | pages [19] -->
Team # 50193

<!-- b000459 | furniture | pages [19] -->
Page 19 of 22

<!-- b000460 | caption | pages [19] -->
Figure 7: Return-Number of selected School

<!-- b000461 | prose | pages [19] -->
From the ﬁgure(7), we ﬁnd that as the number of the schools ought to be chosen in each year increases, the maximum return has a trend of rise ﬁrst then fall. The optimal school number is about 12, which lies in our model’s school number constraint between 10 and 30, this prove that our list that is given before is valid.

<!-- b000462 | prose | pages [19] -->
5.3 Policy of distribution

<!-- b000463 | prose | pages [19] -->
When considering the time, how to allocate the fund properly is important, we test 4 basic policy and compare their results. In policy 1, all the money is distributed in the ﬁrst year; in policy 2 ,the money is distributed evenly in the ﬁve years, that is 200000000 dollars per year; in policy 3, the money is distributed unevenly among years, but there is a constraint that conﬁne the minimum and maximize amount of money that is distributed in each year; ﬁnally in policy 4, we can distributed the money in each year without any constraint. Our recommendation list is based on policy 3.

<!-- b000464 | caption | pages [19] -->
Table 7: return-policy

<!-- b000465 | prose | pages [19] -->
max return policy gap 54579267 1 0.689 157020989 2 0.107 169677616 3 0.035 − 175745328 4

<!-- b000466 | prose | pages [19] -->
From table(7), we ﬁnd that policy 4 get the best result. But, in that situation, only 5000000 dollars are distributed in the ﬁrst year and second year, which is not practi- cal We also ﬁnd that the gap between our policy, i.e. policy3 and policy 4 is only about 3.5% and we avoid the extreme bias among the years, so our model is valid.

<!-- b000467 | furniture | pages [20] -->
Team # 50193

<!-- b000468 | furniture | pages [20] -->
Page 20 of 22

<!-- b000469 | prose | pages [20] -->
6

<!-- b000470 | heading | pages [20] -->
Future Work

<!-- b000471 | prose | pages [20] -->
Due to limitation of time, lack of accessible data and experience in related ﬁeld, our model is not robust based on the real world. And from the results we can see, the chosen university is not very ideal. We cannot ﬁgure out intuitively why we should invest them. So future work may process in this ﬁeld.

<!-- b000472 | prose | pages [20] -->
• Invite experts to do the subjective evaluation. In our model, there are many subjective methods such as AHP, choosing indexes for the variables, constraints for the variables. Some of the indexes are put forward by our own experience and intuition, and not very credible. Some others we do the sensitivity analysis, and also cannot ﬁnd the good value. Maybe an experts can have a better view of the evaluation, verify our model and make a better use of it.

<!-- b000473 | prose | pages [20] -->
• Focus on different subjects and different students. In our model, school is our object and we treat the school as a whole. We only use the information of subjects to do the clustering, not for the evaluating of the ROI. But nowadays, we should judge the level of a schools by its different subjects’ level, not the overall level. An investment of an outstanding subject may gain more valuable beneﬁts and contributes to the development of the society. For example, in future work, we can include information of subjects into evaluation system and give more weights to the subjects such as Medical Science, IT, Ecology and so on. Besides, it’s more important to treat students as the object. We should focus more on the individual differences and the level of demand for different students.

<!-- b000474 | prose | pages [20] -->
• More data is needed. First, more real data should be ﬁlled in the blank of the missing data, which can reduce the error resulting from the data imputation.

<!-- b000475 | prose | pages [20] -->
Second, we should ﬁnd more data for more information of schools. For example, in our model, using tuition to present the input of schools is not credible, we should ﬁnd the Financial Investment or investment of shareholder to see the input. Having more data means we can rethink whether the attributes we have selected are suitable and replaced the improper ones. Having more data means we can do more detailed analysis from the dimension of time.

<!-- b000476 | prose | pages [20] -->
Third, ﬁnd more data of other charitable organization. Lumina’s goal is to increase the proportion of Americans with what it calls ”high-quality” degrees and creden- tials to 60 percent by the year 2025. And Gates foundation aims to help minority students and poor students enjoy good education. Because we have different goals and strategies from these two charitable organization, we believe it can reduce the possibility of duplication of investment. But only relying on the concept is not credible. We need more data of other charitable organization, on the one hand to study their investment strategy to improve ours, on the other hand to reduce the possibility of duplication of investment to a great extend.

<!-- b000477 | furniture | pages [21] -->
Team # 50193

<!-- b000478 | furniture | pages [21] -->
Page 21 of 22

<!-- b000479 | prose | pages [21] -->
7

<!-- b000480 | heading | pages [21] -->
Conclusion

<!-- b000481 | prose | pages [21] -->
In our paper, we have done lots of data processing work, put forward the ROI evaluation system for charitable organization and constructed two kinds of model, basic model for one year and time series model for ﬁve year. We use many theory and methods such as AHP, PCA, K-means clustering, MILP, Grey Theory and other ﬁnancial theory to complete our work. Generally speaking, we are satisﬁed with our work.

<!-- b000482 | prose | pages [21] -->
Like any model, the one present above has its strengths and weaknesses. Some of the major points are presented below.

<!-- b000483 | prose | pages [21] -->
7.1

<!-- b000484 | heading | pages [21] -->
Strengths

<!-- b000485 | prose | pages [21] -->
• Integrity : We comprehensively use all of the data, either for evaluation, or for clustering, making evaluation criteria more credible. And our model is also integral with basic and time series form.

<!-- b000486 | prose | pages [21] -->
• Technical Supporting : We use many theory and methods to support our work. And each one is used reasonably and properly.

<!-- b000487 | prose | pages [21] -->
• Cross Fusion : We get inspiration from ﬁnancial sector and use ﬁnancial knowledge to support our mathematical model.

<!-- b000488 | prose | pages [21] -->
• Flexible and Extendable : To include additional factors, the model could be ex- tended to apply to many situation. And everyone can make different subjective assessment based on the speciﬁc circumstances.

<!-- b000489 | prose | pages [21] -->
7.2

<!-- b000490 | heading | pages [21] -->
weaknesses

<!-- b000491 | prose | pages [21] -->
• Lack of Data Support : This model requires a large amount of data, some of which is hard to obtain. We have no data to validate our model and our result is not very ideal.

<!-- b000492 | prose | pages [21] -->
• Subjective : There are many subjective methods in the model and some of the indexes are put forward by our own experience and intuition, which are not very credible.

<!-- b000493 | prose | pages [21] -->
• Simplifying Assumptions : Simplifying assumptions had to be made in order to create a solvable model. Thus, some valuable data and information are unable to use.

<!-- b000494 | prose | pages [21] -->
• Neglect of Future Dynamics : In our model, we ignore the very fact that the dis- tributed fund will affect the school’s performance and our evaluation in the follow- ing years. In reality, the fund allocation strategy should be based on the schools’ feedback and the response to the previous donation, so it actually a dynamic pro- cess.

<!-- b000495 | furniture | pages [22] -->
Team # 50193

<!-- b000496 | furniture | pages [22] -->
Page 22 of 22

<!-- b000497 | heading | pages [22] -->
References

<!-- b000498 | references | pages [22] -->
[1] Bernholz, Lucy. How Big Data Has the Potential To Transform Philanthropy: New

<!-- b000499 | references | pages [22] -->
and faster information could make charitable giving more effective and efﬁcient,

<!-- b000500 | references | pages [22] -->
but it will require some hard decisions. Wall Street Journal, Eastern edition[New

<!-- b000501 | references | pages [22] -->
York, N.Y].16 Dec 2013: R.2.

<!-- b000502 | references | pages [22] -->
[2] Wu Sen, Feng Xiaodong, Shan Zhiguang. Missing Data Imputation Approach

<!-- b000503 | references | pages [22] -->
Based on Imcomplete Data Clustering. Chinese Journal of Computers,Vol.35(2012)

<!-- b000504 | references | pages [22] -->
[3] K-means Clustering, Wikipedia https://en.wikipedia.org/wiki/K-means clustering

<!-- b000505 | references | pages [22] -->
[4] P.T.harker. Alternative modes of questioning in the analytic hierarchy process, Math

<!-- b000506 | references | pages [22] -->
modeling,Vol.9,No.3-5(1987)

<!-- b000507 | references | pages [22] -->
[5] Jim Freeman. A User’s Guide to Principal Components. Journal of the Operational

<!-- b000508 | references | pages [22] -->
Research Society,2012,Vol.43(6)

<!-- b000509 | references | pages [22] -->
[6] Modern Portfolio Theory, Wikipedia https://en.wikipedia.org/wiki/Modern portfolio

<!-- b000510 | references | pages [22] -->
theory

<!-- b000511 | references | pages [22] -->
[7] Hsu L C. Applying the grey prediction model to the global integrated circuit indus-

<!-- b000512 | references | pages [22] -->
try. Technological Forecasting and Social Change, 2003, 70(6): 563-574.

<!-- b000513 | references | pages [23] -->
Dear Mr. Alpha Chiang,

<!-- b000514 | furniture | pages [23] -->


<!-- b000515 | references | pages [23] -->
We are here to help you with choosing proper targets of donation. This letter will define our ROI,

<!-- b000516 | references | pages [23] -->
explain our optimal investment strategy and list methods used to calculate the ROI more accurate.

<!-- b000517 | references | pages [23] -->
Some colleges and universities recommended by our investment strategy will be pointed out at the

<!-- b000518 | references | pages [23] -->
end.

<!-- b000519 | furniture | pages [23] -->


<!-- b000520 | references | pages [23] -->
As we know, the main purpose of the Goodgrant Foundation is to help improve educational

<!-- b000521 | references | pages [23] -->
performance of undergraduates attending colleges and universities in the United States, and our

<!-- b000522 | references | pages [23] -->
definition of Return on Investment is based on this principle. Educational performance contains two

<!-- b000523 | references | pages [23] -->
implications: achievements in universities and contributions to the society.

<!-- b000524 | furniture | pages [23] -->


<!-- b000525 | references | pages [23] -->
Firstly, the measure of the performance in universities should be clarified. The premise of showing

<!-- b000526 | references | pages [23] -->
their endeavor in school is their economic foundations which is variant among the students. Those

<!-- b000527 | references | pages [23] -->
who are suffering from poverty have this congenital disadvantage that stops them from paying all

<!-- b000528 | references | pages [23] -->
their effort to the college life. So this factor should be considered in the measurement of ROI to

<!-- b000529 | references | pages [23] -->
reflect the effect of the Goodgrant Foundation to meliorate the performance in the school.

<!-- b000530 | furniture | pages [23] -->


<!-- b000531 | references | pages [23] -->
Secondly, the limited money should be spent on those colleges or universities that can enrich

<!-- b000532 | references | pages [23] -->
students better than others and the more different the performance students get after graduation and

<!-- b000533 | references | pages [23] -->
before entrance, the more powerful the university is to educate students. So the key point is to

<!-- b000534 | references | pages [23] -->
measure the average ability of students before entrances and after graduation and correctly

<!-- b000535 | references | pages [23] -->
calculating the difference to reflect the power of education of this school. As an organization of

<!-- b000536 | references | pages [23] -->
charity, the target is the contribution to the society rather than profit and the best contribution is to

<!-- b000537 | references | pages [23] -->
help colleges and universities output more and better students to the society. So evaluating the

<!-- b000538 | references | pages [23] -->
quality of the graduates is also important.

<!-- b000539 | furniture | pages [23] -->


<!-- b000540 | references | pages [23] -->
Our definition of ROI is based on the above views and the data provided. It is calculated based on

<!-- b000541 | references | pages [23] -->
the following formula:

<!-- b000542 | references | pages [23] -->
ROI = 𝑜𝑢𝑡𝑝𝑢𝑡

<!-- b000543 | references | pages [23] -->
𝑖𝑛𝑝𝑢𝑡∗𝑢𝑟𝑔𝑒𝑛𝑐𝑦

<!-- b000544 | references | pages [23] -->
The output is the measurement of the effectiveness of education which is the weighted sum of four

<!-- b000545 | references | pages [23] -->
parts: salary after graduation, retention rate, repayment ability and education enhance rate. The

<!-- b000546 | references | pages [23] -->
education enhance rate is the difference of the average salary and average SAT scores because the

<!-- b000547 | references | pages [23] -->
SAT scores is the measurement of competence before entrance and salary reflects the capability

<!-- b000548 | references | pages [23] -->
after graduation. The urgency means the desire of students to get education. As a charity

<!-- b000549 | references | pages [23] -->
organization, helping those people who are in desperately need is the most fundamental principle.

<!-- b000550 | references | pages [23] -->
To measure how eager those students are for education, this urgency part is the combination of rate

<!-- b000551 | references | pages [23] -->
of got Pell Grants, rate of got Federal Loan and the total debt of the students. These three parts can

<!-- b000552 | references | pages [23] -->
preferably measure the will of asking for help. The input is to access the efficiency of the money

<!-- b000553 | references | pages [23] -->
that donated to this school. So this value is the net price of this college or university. The more

<!-- b000554 | references | pages [23] -->
output of educational performance exaltation and the less cost students need to pay, the more

<!-- b000555 | references | pages [23] -->
efficient this university is.

<!-- b000556 | furniture | pages [23] -->


<!-- b000557 | references | pages [24] -->
As the explanation of every part of ROI, the goal is evident, which high mark of ROI represents the

<!-- b000558 | references | pages [24] -->
good choice of donation targets with good contribution to society, effective use of private fund and

<!-- b000559 | references | pages [24] -->
great help to students in poverty. So the future donation targets should be determined by calculating

<!-- b000560 | references | pages [24] -->
our ROI or giving enough attention to urgency, efficiency and contribution. In addition, we also

<!-- b000561 | references | pages [24] -->
define the risk of assisting each school as the radio between the standard deviation of the wage and

<!-- b000562 | references | pages [24] -->
average wage, the risk is an important in allocating the money, especially when the decision maker

<!-- b000563 | references | pages [24] -->
is risk aversion.

<!-- b000564 | furniture | pages [24] -->


<!-- b000565 | references | pages [24] -->
With the definition of target above, various methods are used to guarantee the accuracy of ROI.

<!-- b000566 | references | pages [24] -->
Principal Component Analysis (PCA) is used to remove redundancy from the data. Cluster analysis

<!-- b000567 | references | pages [24] -->
and fill algorithm are employed to fill the missing data for further analysis. Analytic Hierarchy

<!-- b000568 | references | pages [24] -->
Process (AHP) is adopted to synthetically evaluate the effect of a sequence of independent variables.

<!-- b000569 | references | pages [24] -->
Gray prediction is working when predicting the future plan based on current situation. We build a

<!-- b000570 | references | pages [24] -->
mixed integer linear programming model to find the optimal fund allocation plan base on ROI and

<!-- b000571 | references | pages [24] -->
risk in the future year we derived from the previous definition and analysis. The model set maximize

<!-- b000572 | references | pages [24] -->
the total return as the objective with the constraints including the risk control as well as some

<!-- b000573 | references | pages [24] -->
distribution limitation. A basic model is first introduced followed by a more comprehensive model

<!-- b000574 | references | pages [24] -->
which consider the time series. By doing the sensitivity analysis, we assure the validation of our

<!-- b000575 | references | pages [24] -->
model.  Finally, we get recommendation list of schools including the investment year of each

<!-- b000576 | references | pages [24] -->
school.

<!-- b000577 | furniture | pages [24] -->


<!-- b000578 | references | pages [24] -->
In summary, 16 colleges and universities are selected out of more than 3000 colleges and universities

<!-- b000579 | references | pages [24] -->
spread all over the America: United Talmudical Seminary, Whitworth University, Moravian College,

<!-- b000580 | references | pages [24] -->
Clark University, Juniata College, Hampshire College, Florida Memorial University, Ithaca College,

<!-- b000581 | references | pages [24] -->
Uta Mesivta of Kiryas Joel, Roger Williams University, Fairfield University, Heidelberg University,

<!-- b000582 | references | pages [24] -->
Pitzer College, The Sage Colleges, Western Connecticut State University, Brandman University.

<!-- b000583 | references | pages [24] -->
These schools are the optimal choice of donation based on our definition of ROI and the methods

<!-- b000584 | references | pages [24] -->
and models conducted. They are recommended because they are more efficient in education, less

<!-- b000585 | references | pages [24] -->
economic burden for the students and better average contributions to society than other schools.

<!-- b000586 | references | pages [24] -->
Although we derived a recommendation list of the plan in the successive 5 years, in the reality, the

<!-- b000587 | references | pages [24] -->
company should also take the feedback and performance of chosen schools into consideration to

<!-- b000588 | references | pages [24] -->
make a sounder and more reasonable decision. To know how the money distributed in details, please

<!-- b000589 | references | pages [24] -->
check our paper.

<!-- b000590 | furniture | pages [24] -->


<!-- b000591 | references | pages [24] -->
Wish our optimal investment strategy can inspire you at the key point of choosing the targets of

<!-- b000592 | references | pages [24] -->
donation. We are very eager to hear your opinion on our plan and to have more communication

<!-- b000593 | references | pages [24] -->
about investment strategy. We look forward to hearing from you.

<!-- b000594 | furniture | pages [24] -->


<!-- b000595 | references | pages [24] -->
Yours sincerely,

<!-- b000596 | references | pages [24] -->
A group of modelers who are enthusiastic about donation

<!-- b000597 | furniture | pages [24] -->


<!-- b000598 | furniture | pages [24] -->


<!-- b000599 | furniture | pages [24] -->


<!-- b000600 | furniture | pages [24] -->


<!-- b000601 | references | pages [24] -->
2/2/2016
