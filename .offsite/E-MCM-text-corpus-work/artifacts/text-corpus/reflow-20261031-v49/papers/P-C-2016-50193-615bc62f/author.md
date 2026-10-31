For ofﬁce use only For ofﬁce use only

T1 F1 T2 F2 T3 F3 Problem Chosen T4 F4

2016 MCM/ICM

Summary Sheet

An Educational Donation Mechanism Based On Data Insight

Summary

Recent years, Big Data has become increasingly popular and the guidance of big data is required in many ﬁelds, including charitable ﬁeld. In our paper, we construct a new ROI evaluation system for charitable organization using data mining methods to process data, and succeed in determining an optimal investment strategy for Goodgrant Foundation.

First, we operate on the data. We do data screening according to the integrity and re- dundancy of the information, deleting data with information less than the threshold, and merging different attributes using linear ﬁtting and PCA. For the reserved attributes and schools, we do data imputation to ﬁll the missing data based on K-means Clustering. Then we normalize all the data to make them comparable in the following analysis.

Second, we construct a ROI evaluation criteria, which is a ratio of output and input mul- tiplying an adjustment coefﬁcient, named “urgency”. The ratio reﬂects the beneﬁts in related to the cost, while urgency reﬂects the demand for money which is an important factor should be considered by charitable organization. We use PCA to select attributes, letting salary, education quality and some others to represent output, tuition to represent input and Federal loan, debt and some others to represent urgency. Then, AHP is used to measure the importance between different factors and allocate weights.

Third, we put forward two kinds of model, basic model for one year and time series model for ﬁve year. Seeing the ROI as beneﬁts from investment, we introduce the ﬂuctuation of output as “risk”, imitating the concept of Modern Portfolio Theory in the ﬁnancial sector to solve the problems. In the basic model, we develop a Mixed Integer Linear Pro- gramming Algorithm and succeed in ﬁnding 14 schools for the investment. Further, we consider the time factor and improve the model into a time series model, using MILP and Grey Prediction to determine the long-term investment strategy. 16 schools are chosen with different time duration and different amounts of money.

Finally, we make sensitivity analysis for our model, changing the amount of schools, the restriction for money, whether allocating the money equally or not and so on to analyze the different results of the output and to ﬁnd the better parameters for ideal results.

To sum up, our model is a feasible and reasonable model with technical and data support. Because of the subjectivity, this model can be used ﬂexibly after data training.

1 Introduction

1.1 Background

If it were a decade ago, you would not image that the pageview of ”Facebook” can be more than millions in one minute; you would not image that when you open ”google maps”, all the travel information is already in the palm of your hand; you would not image that through data mining you can gain an insight into the development trend of an enterprise to guide your investment. Nowadays big data has penetrated into our work and lives, and has brought such huge changes. In turn, it has become particularly important for us to ﬁnd useful information from the mass of data to guide our work and life.

As a special column from ”New York Times” in Feb., 2012 says, Big Data Era has come. In the commercial, economic and other areas, information will increasingly be made based on data and analysis, rather than based on experience and intuition. Also the ﬁeld of charity is in the same case. In the past, it is more difﬁcult to give money away intelligently than to earn it in the ﬁrst place.[1] We do not know how to do the charitable giving rationally, thus, the calculation of ROI is also out of the question. But now new and faster information could make charitable giving more effective and efﬁcient. Moreover, it provides a possibility to link charitable giving issues with the investment issues in the ﬁnancial sector.

This article is about a charitable donation issue of universities in the U.S. We aim to design a measure system of the return on investment based on large quantities of data through data mining methods. To solve the problem, we will use the Portfolio Theory, Linear Programming, Grey Theory and some other methods to determine the optimal strategy in terms of dimension of time.

1.2 Overview of Our Work

First, we ﬁnd a few key points in this question :

• The volume of data is large and of different types. How to do the normalization of the data.

• Among the massive data, there are many missing data in the ﬁles, which contains less information and not easy to do batch processing.

• How to classify the large amount of attributes of universities.

• Different attributes focus on different aspects and how to judge their importance.

• How to choose schools from the candidate list and how the allocate investment amount among them.

• The charitable investment process lasts for 5 years, so time is an important factor which will inﬂuence our ROI criteria.

On the basis of above discussion, to determine the optimal investment strategy, we may boil down the tasks to the following four steps :

• First, we do data screening according to the integrity and usefulness of the informa- tion. For the retention attributes and schools, we use K-means clustering method to ﬁll the missing data. And normalize all the data.

• Second, we use PCA method to choose and classify different attributes. Then we use AHP method and knowledge of ﬁnance to construct ROI concept. And we use the ROI concept to process data, ranking the candidate schools.

• Third, we introduce the concept of Modern Portfolio Theory and construct two models. In the basic model, we develop a Mixed Integer Linear Programming Al- gorithm to determine an optimal investment strategy. Further, we consider the time factor and improve the model into a timing model, using Dynamic Programming Algorithm and Grey Prediction to determine the long-term investment strategy.

• Further analysis and discussion of the model.

1.3 Assumptions

• Ignore inﬂation and deﬂation of money and other time value of money. The value of money remains unchanged.

• As a charitable organization, our aim is to improve educational performance and expect for more social beneﬁts rather than gaining proﬁt.

• Our charitable donation is a comprehensive scholarship, not rewarding for the out- standing contributions in speciﬁc ﬁelds.

• If we have different goals and strategies from other charitable organization, we believe it can reduce the possibility of duplication of investment to a great extend.

• The object for evaluating and scholarship granting is school, not individual, though some individual information is included in our criteria. And it is business of school to allocate the money.

• We focus on the fairness of our strategy so as to invest more schools regardless of the reputation of them.

• Because of Marginal utility, we try not to invest large amount of money to one school.

• In the timing model, we assume that the inﬂuence of other factors which are ex- cluded outside the model can be ignored. That’s to say, future is predictable.

2 Data Processing

2.1 Data Screening

The amount of raw data is large, so we should ﬁrst do data screening according to the integrity and usefulness of the information.

First, we do data screening on 7805 schools :

• We only consider the 2978 candidate schools in the ﬁle Problem C - IPEDS UID for Potential Candidate Schools, and match the schools with their 95 attributes in the ﬁle Problem C - Most Recent Cohorts Data (Scorecard Elements).xlsx.

• Delete the schools which are not currently operating institution and which are on Heightened Cash Monitoring 2 by Department of Education, meaning that they encounter economic depression and lack students and which has no or very limited information about percentage of degrees awarded. It’s meaningless to invest on these schools.

• Delete the schools of whom 50% of the attributes are ”NULL”. If the percentage of missing data exceeds 50%, the imputation will result in great error, which we treat as a threshold for missing data.[2]

Second, we do data screening on 95 attributes :

• We combine some binary variables together. For example, we delete the net price for different income classes and combine the total net price for public school and private school together, named as ”Net Price”. And we use the total retention rate for weighting to combine retention rate for full-time and part-time students together, named as ”Retention Rate”.

• Though there are large quantities of missing data in ”SAT scores” and ”ACT scores”, we reserve the midpoint of them as categorical variables. High entrance require- ments with SAT or ACT scores would indicate higher education quality, which we will treat differently from the low entrance requirements school in the following ROI evaluation system.

• Besides, we reserve all the ﬂag attributes like ”ﬂag for Historically Black College and University”, ”ﬂag for women-only college” and all the subject attributes like ”percentage of degrees awarded in Architecture And Related Services”, using them for the clustering and data imputation in the next step.

• We delete location, age of students and some other information contributes less to our ROI evaluation system.

After data screening, there are about 2700 schools each with about 60 attributes in the candidate list.

2.2 Data imputation

In statistics, missing data occur when no data value is stored for the variable in an obser- vation. Missing data are a common occurrence and can have a signiﬁcant effect on the conclusions that can be drawn from the data.

• K-means Clustering

Many approaches are available for data imputation, such as Listwise Deletion, Mean Imputation, Regression Imputation and Multiple Imputation. Here we use K-means clustering imputation: ﬁrst using complete and meaningful data in the ﬁles to combine schools with similarity together, and then using the means of these similar schools to ﬁll the missing data.[2]. We can see it as an improved method for Mean Imputation.

Given a set of observations (x1, x2, . . . , xn) where each observation is a d-dimensional real vector, k-means clustering aims to partition the n observations into k sets

S = {S1, S2, . . . , Sk}

so as to minimize the within-cluster sum of distance functions of each point in the cluster to the K center.[3] In other words, its objective is to ﬁnd:

k 2 X X (x −µi) min (1) i=1 x∈Si

where µi is the mean of points in Si.

In the K-means algorithm, K is given in advance, but selecting the K value is very difﬁcult. According to the theory of variance, we often determine the K value based on the R2 statistic.[3]

nt (t))′(X(t) (t)) (X(t) X (i) −X (i) −X Wt = (2) i=1 k nt (X(t) (i) −X)′(X(t) X X (i) −X) T = (3) t=1 i=1 k X Pk = Wt (4) t=1 k (t) −X)′(X (t) −X) X Bk = nt(X (5) t=1 R2 = Bk T = 1 −Pk (6) T

The greater the proportion of sum of square between class is and the smaller the proportion of sum of square inner class is, the better K value is. So we choose the K value that maximize R2 value.

• Variables Choosing In our data ﬁles, the missing data columns needed to be ﬁlled are listed as below :

Number Variable Name Number Variable Name 1 Net Price 6 gt 25k p6 2 Retention Rate 7 md earn wne p10 3 GRAD DEBT MDN SUPP 8 sd earn wne p10 4 GRAD DEBT MDN10YR SUPP 9 md earn wne p6 5 RPY 3YR RT SUPP 10 sd earn wne p6

These are all very important variables in our ROI evaluation system. For exam- ple, “Net Price“ is a measure of input of education, and “md earn wne p1“ means median earnings of students working and not enrolled 10 years after entry and is measure of output of education.

Having ﬁgured out on what variables to do data imputation, we should determine what variables should the imputation be based on. Following are some integral data columns for us to use :

Number Variable Name Number Variable Name 1 PREDDEG 10 MENONLY 2 CONTROL 11 WOMENONLY 3 HBCU 12 PCIP XXXXX 4 PBI 13 DISTANCEONLY 5 ANNHI 14 UGDS 6 TRIBAL 15 UGDS XXXXX 7 AANAPII 16 PPTUG EF 8 HSI 17 PCTFLOAN 9 NANTI 18 PCTPELL

By contrast, these variables are more integral and have signiﬁcance to guide the imputation. For example, “PCIP XXXXX“ means Percentage of degrees awarded in different subjects (including 38 subjects), indicating the subjects composition of schools; “UGDS“ means the size of schools and “UGDS XXXXX“ means the percentage of students who are WHITE, BLACK, ASIAN and so on(including 9 different attributes), indicating the students composition of schools; and “PCT- FLOAN“ means percent of all federal undergraduate students receiving a federal student loan, indicating the students’ ﬁnancial situation of schools.

So we can believe that it has a good description of every school to consider the above variables together. Then the similarity and dissimilarity of schools can be found.

• Clustering Output To simplify the model, we only do the K-means clustering once using all the data from integral data columns. We assume that the classiﬁcation using all the integral variables is applicable to all the missing variables. And we choose the number of classes K from 3 to 8, ending up ﬁnding the optimal value is 5.

After clustering, we can believe that the schools in the same class have the maxi- mum similarity. So, we use the means of data of no-missing-data schools from each missing variable column to ﬁll the corresponding blanks of missing-data schools in the same class.

Following is the results of K-means clustering and an example of the imputation value of “md earn wne p10“ :

Number Size md earn wne p10 1 27 19655.56 2 5 24980.11 3 1151 31176.46 4 1499 40780.52 5 11 42063.64

From above table, the value of “md earn wne p10“ for each of the ﬁve classes is the means value of no-missing-data schools and what we should do next is to ﬁll the value into blank in each class. The same approach is used in all the missing data columns. Up to now, we get the integral value of all the schools with all the attributes.

2.3 Data Normalization

After ﬁlling all the missing data, we should do the data normalization to facilitate the further analysis of the data. It can provide an approach for comparison of different kinds of data and reﬂect the combined results of different factors.

Here we use Min-max normalization, doing linear transformation of the raw data, map- ping data set x = {x1, x2, . . . , xn} into [0,1] interval. Let x′ be the normalized value, the formula is :

x −xmin x′ = (7) xmax −xmin

While x′ min = 0 and x′ max = 1. And all the data hereinafter is normalized data.

3 ROI Evaluation System

3.1 Concept of ROI

In this part, we focus our attention on how to determine the Return on Investment evalu- ation system. In the ﬁnancial sector, ROI is the beneﬁt to the investor resulting from an investment of some resource, which is a way of considering proﬁts in relation to capital invested. According to the original concept, we use the available data to construct a new ROI evaluation system appropriate for our charitable organization. The formula is :

ROI = Output Input × Urgency (8)

1. Output

Output is the measure of the quantity of education, in other words, effectiveness.

Here we use four factors to measure Output : Salary After Graduation, Retention Rate, Repayment Ability and Education Enhance Rate. But why these four factors?

• First, there is low correlation among the four factors, each of which can be separated out as an impact indicator of Output. To illustrate the independence, and the relationship between different variables, we use Principal Component Analysis(PCA), which is a statistical procedure that uses an orthogonal trans- formation to convert a set of observations of possibly correlated variables into a set of values of linearly uncorrelated variables.[4] When some of the vari- ables can explain a great percentage of the results, we can say these variables are strongly correlated and we can use the great one to represent others.

• Second, they are strongly related to Output of a school :

(a) Salary After Graduation(SAG) : measures the overall level of students.

More salary means the students’ job can make more valuable output.

So they can contribute more to the society when they receive the same amount of donation. There are three factors representing salary, “md earn wne p10”, “md earn wne p6” and “gt 25k p6”, meaning midpoint earn- ing in 10 years, midpoint earning in 6 years and share of students earning over $25,000 per year in 6 years. Similarly, using PCA to study the corre- lation between them and assign weights, we ﬁnd that the three factors are strongly related and one of them, “md earn wne p6”, can explain 95% of the result. So we only use the value of “md earn wne p6” to represent Salary After Graduation.

(b) Retention Rate(RR) : measures the utilization of the investment. On the one hand, the larger the retention rate is, the more students retained in schools will enjoy the investment. And on the other hand, higher reten- tion rate means greater school spirit and learning atmosphere, which is worthy of investment. “Retention Rate” has been deﬁned above.

(c) Repayment Ability(RA) : measures the ability to contribute to the soci- ety. There is difference between Salary After Graduation and this fac- tor. The former emphasize the potential ability, while higher Repay- ment Ability shows that it is no longer subject to the debt or other bur- den in life, and have real ability to contribute to society. Here we use “RPY 3YR RT SUPP” to represent Repayment Ability.

(d) Education Enhance Rate(EER) : measures the education quality of schools.

Here we use normalized data of “md earn wne p6” minus normalized data of “SAT scores” and then normalize it again to represent the Edu- cation Enhance Rate. Because the salary can reﬂect the level of students after graduation and the “SAT scores” can reﬂect the level before entry.

As for the schools without “SAT scores”, this weight will be assigned to other three factors.

In order to get the overall evaluation index, we need to compute the weight of the four factors. In the following, analytical hierarchy process, abbreviated to AHP, will be applied to judge importance of the four factors. We compare the four factors by pairs and give the following matrix according to experience and intuition. (the columns indicate Salary After Graduation, Retention Rate, Repayment Ability and Education Enhance Rate from left to right)

  1 5 6 3 1 3 1 2   2 1 1 2 1 2 3 1 1 1 1 3 6 5

Thus, we can ﬁgure out that the weight vector V1 = [0.576 0.125 0.077 0.222]. Finally, in consistency check, the consistency index CI = 0.0113 < 0.10, which means that the weight determined by AHP is very reasonable [5].

As for the schools without “SAT scores”, we assign the weight of EER to other three factors and use the same AHP method. The weight vector is V2 = [0.741 0.161 0.098], also passing the consistency check.

AHP which we adopted here is the mostly widely used method in the evaluation of the weight, though its objectivity is pretty poor. Nevertheless, the weight deﬁned by objective method cannot match its importance in practice completely. As to the subjective method, it can reﬂect difference of relative importance among the four indexes in spite of the subject process to deﬁne the indexes’ weight. Considering the evaluation of the importance of these four indexes is a subjective judgement, weight deﬁning through the subjective method possesses more scientiﬁc rationality. So we utilize the more subjective AHP method rather than other more objective model to gain the weight.

Finally, the comprehensive calculation formula is described as :

( T  V1 · SAG RR RA EER Output = (9) T  V2 · SAG RR RA

2. Input

Adding Input into the ROI formula, we can get a ratio considering proﬁts in relation to capital invested, in other word, efﬁciency. It means given one dollar, schools with low Input and high Output can create more value. Here we only have one factor, “Net Price”(NP), to represent the Input. We believe that high tuition means the schools need high input to maintain daily routine. “Net Price” has been deﬁned above.

There is a problem that the only factor in Input will have huge inﬂuence than the factors in the Output, resulting that the schools with lower tuition will get higher ROI. So we add a correction index “α” (α ∈[0,1]) to verify the formula.

Input = (1 −α) + α × NP (10)

Here we let α = 0.25.

3. Urgency

For ﬁnance issue, the deﬁnition of ROI with Input and Output is enough. But for this charitable issue, we add an correction index, “Urgency”, to make the deﬁnition more robust. Because charitable organization should donate money to the people who are the most eager for it. Here we use three factors to measure Urgency : Pell Grants, Federal Loan, Debt. Similarly, we choose these three indexes because of the independence and meaningfulness.

(a) Pell Grants(PG) : measures students’ degree of demand for funds in different schools. Here we use “PCTPELL”, percentage of undergraduates who receive a Pell Grant, to represent PG.

(b) Federal Loan(FL) : have the similar meaning of PG. Here we use “PCT- FLOAN”, percent of all federal undergraduate students receiving a federal student loan to present it.

(c) Debt : measures the degree of liability in different schools. There are two fac- tors, “GRAD DEBT MDN SUPP” and “GRAD DEBT MDN10YR SUPP” related to Debt, but they are strongly related. So we choose “GRAD DEBT M DN SUPP”, median debt of completers, suppressed for n=30, to represent Debt.

Though three factors have very similar meaning, the PCA indicates they are independent, each explains 31%, 13%, 56% of the result. We use these three number as their importance in AHP, and get the ﬁnal weight vector V3 = [0.25 0.25 0.50], the consistency index CI = 0.0089 < 0.10.

T  Urgency = V3 · PG FL Debt (11)

On the basis of the discussion above, we draw a picture to visually represent our ROI evaluation system.

3.2 Using Grey Theory to predict ROI

On the following discussion, we have ﬁgured out what the ROI is, and how to calculate the ROI of schools for one year using given data. But the charitable donation will be given for 5 years. In the long run, we can use Grey Theory to predict the future ROI using the previous data.

Grey Theory focuses on model uncertainty and information insufﬁciency in analyzing and understanding systems via research on conditional analysis, prediction and decision- making[7]. This theory is applied mainly on in-complete and un-determinable problems. GM(1,1) is one of models of gray theory. which uses an accumulated generation op- eration(AGO) and some equations to produce an inﬁnite grey sequences to predict the following data with observed data. Step 1. Let be a sequence of observed data

X(0) = (X(0)(1), X(0)(2), ......, X(0)(n)) (12)

where X(0)(i) represents the observed data with respect to time i. Step 2. Generate the ﬁrst-order accumulated generating operation (1 −AGO) sequence X(1)(i) based on the observed sequence X(0)(i)

X(1) = (X(1)(1), X(1)(2), ......, X(1)(n)) (13)

where X(1)(k) is formed as the following formula

k X X(1)(k) = X(0)(i) = X(1)(k −1) + X(0)(k) (14) i=1 Step 3. Establish the ﬁrst-order differential equation of sequence X(1)(k)

dX(1) + aX(1) = u (15) dt

Step 4. Derive the estimated ﬁrst-order AGO sequence

ˆX(1)(k + 1) = (X(0)(1) −u a)e−ak + u (16) a

Step 5. Let ˆa be a sequence of parameters where ˆa = [a, u]T, it can be solved as follow :

ˆa = (BTB)−1BTYn (17)

where −1 2(X(1)(1) + X(1)(2))   1 −1 2(X(1)(2) + X(1)(3)) 1   B = (18) .......

−1 2(X(1)(n −1) + X(1)(n)) 1

and Yn = [X(0)(2), X(0)(3), ......, X(0)(n)]T (19)

According to Grey Theory illustrated as above, we use the data of past 5 years, from 2009 to 2013, to predict the future ROI from 2016 to 2020. Following are some ﬁgures of outcome of Grey Prediction for different schools. We can see that complex trend can be ﬁt with grey prediction and it’s better than Linear Fitting.

(a) Grey Predicting for Future ROI (b) Grey Predicting for Future ROI

4 Model Construction

The allocation strategy of the Goodgrant foundation given ROI and risk can be modeled as a mixed integer linear programming. At ﬁrst, in the basic model, we ignore the time factor and suppose that we allocate all the fund in one period. The objective is to max- imize the total return of the foundation, and constraints include the control of the risk, the minimize and maximize number of school is awarded, the minimize and maximize money a school can get and the size of school. We introduce a continuous decision vari- able to denote the fund each school received and a binary variable to indicate whether the school is invested or not. Then, in the complicated model, we take the time period into consideration. Finally, we give two recommendation list in term of both models respectively.

4.1 Deﬁnition of Risk

In ﬁnancial sector, Modern Portfolio Theory was used to measure risk and beneﬁts, draw- ing the Efﬁcient Frontier of all the risky assets and ﬁnd the Tangency Portfolio.[6] For an investment, risk is certainly attached to beneﬁts. For charitable investment, there also ex- ists risk, which will forbid investment reaching the optimal point though it does not bring any lost for you. Above we have discussed the ROI for charitable investment, which can be seen as beneﬁts. Here we will deﬁne “risk” for our investment.

r = σe (20) µe

In the formula, we use the concept of coefﬁcient of variation. σe indicates the standard deviation of “md earn wne p6”, and µe indicates the means of “md earn wne p6”. This variable is the only measure we can ﬁnd of ﬂuctuation of the Output, larger ﬂuctuation of Output leads to larger risk. And using ratio form to indicate risk is to prevent the inﬂuence of the different amounts of Output itself. Then we use the concept of Modern Portfolio Theory, drawing risk-beneﬁt plots, using Mixed Integer Linear Programming(MILP) to solve the problem.

4.2 Basic Model

Denote the list of candidate school is i ∈S = {1, 2, ..., S}, the constant and the variables are as following.

ROI of school i, i ∈S ROIi risk of school i, i ∈S ri maximum investment in school i, i ∈S Amax i minimum investment in school i, i ∈S Amin i number of student in school i, i ∈S si N max maximum investment school number N min minimum investment school number rmax maximum acceptable risk Smin minimum acceptable student number A sum of the fund

Investment of school i, i ∈S xi State of school i ,0 means not the the prize list, yi ∈{0, 1} 1 means in the recommendation list ,0 means not in the recommendation list The objective is to maximize the total return, since the ROI is deﬁne as rate of return, it yields:

X max ROIixi (21) i∈S The sum of the money each school get should not exceed the total amount of the available money. The average risk of the allocation strategy should not beyond the maximum acceptable risk, we get:

X xi ≤A (22) i∈S X rixi ≤A · rmax (23) i∈S

The number of school that get some foundation should less that the maximum number N max and greater than minimum number N min

N min ≤ X yi ≤N max (24) i∈S

The basic logical constraints between xi and yi, i.e., xi ≥0, if and only if yi = 1, if school i is invested, the amount of the money it gets should lies within the Amin and i Amax , it yields: i ∀i ∈S Amin yi ≤xi ≤Amin yi (25) i i Finally, if the school is too small, we wouldn’t chose it since the fund wouldn’t beneﬁt enough students.

∀i ∈S siyi ≤Smin (26)

4.3 Results of basic model

In the model, ROIi and ri is derived from the pervious work, we set the minimum ac- ceptable student number Smin as 1000, the minimum fund Amin for the school which is i chosen can get as 20000000, since the maximum foundation the school can get is related to the school’s student number, we set Amax = Amin +b∗si where b = 3000. Finally, we i i deﬁne that the foundation must be awarded to at most 30 schools and at least 10 schools. Suppose the decision maker doesn’t care the risk so much, that is, the highest return is the only purpose, by using ILOG CPLEX 12.6 with python API, we get a list of schools that should be recommended according to our model (Ranking according to the ROI).

1 446604 Uta Mesivta of Kiryas Joel 2 133979 Florida Memorial University 3 385619 Everglades University 4 197018 United Talmudical Seminary 5 445708 Johnson Wales University-Charlotte 6 414823 Johnson Wales University-North Miami 7 161226 University of Maine at Farmington 8 216667 Washington Jefferson College 9 195128 The Sage Colleges 10 381617 Baker College of Port Huron 11 213251 Juniata College 12 196200 SUNY College at Potsdam 13 146427 Knox College 14 439288 Johnson Wales University-Denver Figure(3) shows the factors of the ROI, including risk, output, input and urgency, of the schools that is selected by our model. Figure(4) shows the money allocation of each selected schools, the labels of both ﬁgures are the UNITID of the school.

4.4 Time series model

In the real situation, according to the requirement of the Goodgrant foundation, the total 1000000000 will be distributed to the schools in 5 years, so we modiﬁed our previous mixed integer problem and take the time series into consideration. Similarly, we induce i, in which the time series t ∈T = {1, 2, 3, 4, 5}, corre- the decision variables xt i and yt sponding to year 2016,2017,2018,2019,2020 respectively. The whole model is listed as follows:

X X ROIt ixt max (27) i i∈S t∈T Subject to:

X X xt i ≤A (28) i∈S t∈T X X rt ixt i ≤A · rmax (29) i∈S t∈T N min ≤ X ∀t ∈T yt i ≤N max (30) i∈S ∀t ∈T, ∀i ∈S Amin yt i ≤xi ≤Amin yt (31) i i i ∀t ∈T, ∀i ∈S siyt i ≤Smin (32)

4.5 Results of time series model

The constants in the time series model is similar to the previous one with some minor adjustment, particularly, we set Amin as 5000000 and b as 8000, the value of ROIt i and i rt i is determined by the previous calculation. By using IBM ILOG CPLEX, we solve the model, get the global optimal solution and receive the following result:

From the result, we not only select the school but also determine in which years they should be invested in order to maximize the total revenue. In this way, we also, determine the investment period of each school. What’s more, since in our model, we don’t require that foundation is evenly distributed among ﬁve years, instead, we set a upper bound and a lower bound of the total investment in each year. We ﬁnd that actually we should increase the money we invest as time pass by.

5 Sensitive analysis and validation

5.1 Risk-Return

In basic model, we change the maximum acceptable risk and analyze the max return, the result are as follow:

From the ﬁgure(6), we ﬁnd that as the max acceptable risk become greater, the max return we can get also become greater, which conform to our expectation and reality. Moreover, when the max acceptable risk index is greater than about 0.82, the max return will not increase anymore.

5.2 School number

In the time series model, we change the number of the schools that should be chosen and analyze the max return, the result are as follow:

From the ﬁgure(7), we ﬁnd that as the number of the schools ought to be chosen in each year increases, the maximum return has a trend of rise ﬁrst then fall. The optimal school number is about 12, which lies in our model’s school number constraint between 10 and 30, this prove that our list that is given before is valid.

5.3 Policy of distribution

When considering the time, how to allocate the fund properly is important, we test 4 basic policy and compare their results. In policy 1, all the money is distributed in the ﬁrst year; in policy 2 ,the money is distributed evenly in the ﬁve years, that is 200000000 dollars per year; in policy 3, the money is distributed unevenly among years, but there is a constraint that conﬁne the minimum and maximize amount of money that is distributed in each year; ﬁnally in policy 4, we can distributed the money in each year without any constraint. Our recommendation list is based on policy 3.

policy max return gap 54579267 0.689 1 157020989 0.107 2 169677616 0.035 3 − 175745328 4

From table(7), we ﬁnd that policy 4 get the best result. But, in that situation, only 5000000 dollars are distributed in the ﬁrst year and second year, which is not practi- cal We also ﬁnd that the gap between our policy, i.e. policy3 and policy 4 is only about 3.5% and we avoid the extreme bias among the years, so our model is valid.

6 Future Work

Due to limitation of time, lack of accessible data and experience in related ﬁeld, our model is not robust based on the real world. And from the results we can see, the chosen university is not very ideal. We cannot ﬁgure out intuitively why we should invest them. So future work may process in this ﬁeld.

• Invite experts to do the subjective evaluation.

In our model, there are many subjective methods such as AHP, choosing indexes for the variables, constraints for the variables. Some of the indexes are put forward by our own experience and intuition, and not very credible. Some others we do the sensitivity analysis, and also cannot ﬁnd the good value. Maybe an experts can have a better view of the evaluation, verify our model and make a better use of it.

• Focus on different subjects and different students.

In our model, school is our object and we treat the school as a whole. We only use the information of subjects to do the clustering, not for the evaluating of the ROI. But nowadays, we should judge the level of a schools by its different subjects’ level, not the overall level. An investment of an outstanding subject may gain more valuable beneﬁts and contributes to the development of the society. For example, in future work, we can include information of subjects into evaluation system and give more weights to the subjects such as Medical Science, IT, Ecology and so on.

Besides, it’s more important to treat students as the object. We should focus more on the individual differences and the level of demand for different students.

• More data is needed.

First, more real data should be ﬁlled in the blank of the missing data, which can reduce the error resulting from the data imputation.

Second, we should ﬁnd more data for more information of schools. For example, in our model, using tuition to present the input of schools is not credible, we should ﬁnd the Financial Investment or investment of shareholder to see the input. Having more data means we can rethink whether the attributes we have selected are suitable and replaced the improper ones. Having more data means we can do more detailed analysis from the dimension of time.

Third, ﬁnd more data of other charitable organization. Lumina’s goal is to increase the proportion of Americans with what it calls ”high-quality” degrees and creden- tials to 60 percent by the year 2025. And Gates foundation aims to help minority students and poor students enjoy good education. Because we have different goals and strategies from these two charitable organization, we believe it can reduce the possibility of duplication of investment. But only relying on the concept is not credible. We need more data of other charitable organization, on the one hand to study their investment strategy to improve ours, on the other hand to reduce the possibility of duplication of investment to a great extend.

7 Conclusion

In our paper, we have done lots of data processing work, put forward the ROI evaluation system for charitable organization and constructed two kinds of model, basic model for one year and time series model for ﬁve year. We use many theory and methods such as AHP, PCA, K-means clustering, MILP, Grey Theory and other ﬁnancial theory to complete our work. Generally speaking, we are satisﬁed with our work.

Like any model, the one present above has its strengths and weaknesses. Some of the major points are presented below.

7.1 Strengths

• Integrity : We comprehensively use all of the data, either for evaluation, or for clustering, making evaluation criteria more credible. And our model is also integral with basic and time series form.

• Technical Supporting : We use many theory and methods to support our work. And each one is used reasonably and properly.

• Cross Fusion : We get inspiration from ﬁnancial sector and use ﬁnancial knowledge to support our mathematical model.

• Flexible and Extendable : To include additional factors, the model could be ex- tended to apply to many situation. And everyone can make different subjective assessment based on the speciﬁc circumstances.

7.2 weaknesses

• Lack of Data Support : This model requires a large amount of data, some of which is hard to obtain. We have no data to validate our model and our result is not very ideal.

• Subjective : There are many subjective methods in the model and some of the indexes are put forward by our own experience and intuition, which are not very credible.

• Simplifying Assumptions : Simplifying assumptions had to be made in order to create a solvable model. Thus, some valuable data and information are unable to use.

• Neglect of Future Dynamics : In our model, we ignore the very fact that the dis- tributed fund will affect the school’s performance and our evaluation in the follow- ing years. In reality, the fund allocation strategy should be based on the schools’ feedback and the response to the previous donation, so it actually a dynamic pro- cess.
