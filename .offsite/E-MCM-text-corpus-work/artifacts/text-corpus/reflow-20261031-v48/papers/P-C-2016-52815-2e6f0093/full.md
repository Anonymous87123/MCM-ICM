# P-C-2016-52815-2e6f0093

Status: machine-draft; not source-verified.


<!-- b000001 | title | pages [1] -->
x

<!-- b000002 | prose | pages [1] -->
Print This Page Close This Window

<!-- b000003 | front_matter | pages [1] -->
Team Control Number

<!-- b000004 | front_matter | pages [1] -->
For office use only For office use only

<!-- b000005 | front_matter | pages [1] -->
52815

<!-- b000006 | title | pages [1] -->
F1

<!-- b000007 | title | pages [1] -->
T1

<!-- b000008 | title | pages [1] -->
F2

<!-- b000009 | title | pages [1] -->
T2

<!-- b000010 | title | pages [1] -->
T3

<!-- b000011 | title | pages [1] -->
F3

<!-- b000012 | front_matter | pages [1] -->
Problem Chosen

<!-- b000013 | title | pages [1] -->
T4

<!-- b000014 | title | pages [1] -->
F4

<!-- b000015 | front_matter | pages [1] -->
C

<!-- b000016 | prose | pages [1] -->
2016 MCM/ICM

<!-- b000017 | heading | pages [1] -->
Summary Sheet

<!-- b000018 | prose | pages [1] -->
(Your team's summary should be included as the first page of your electronic submission.)

<!-- b000019 | front_matter | pages [1] -->
Type a summary of your results on this page. Do not include

<!-- b000020 | front_matter | pages [1] -->
the name of your school, advisor, or team members on this page.

<!-- b000021 | prose | pages [1] -->
We propose a Bayesian multi-stage model to maximize Return on Investment (RI) over the next five years.

<!-- b000022 | prose | pages [1] -->
First, a model was made to relate the distribution of students' majors at a school to the expected number of jobs that that school will add to to the economy. Here, we relate the unemployment outlook in each particular discipline to the percentage of students at each school pursuing that particular course of study. In the case that a school was going to produce a high number of graduates in a field that is already oversaturated (that is, has a high unemployment rate), it is actually assigned a negative contribution to the number of jobs in the economy.

<!-- b000023 | prose | pages [1] -->
Next, a model was fit to give the relationship between jobs added to the economy and change in real Gross Domestic Product (GDP). This was based on a linear relationship we observed between changes in logGDP and changes in unemployment, fit to data gathered beginning in 1948. This particular model has a surprisingly good fit considering the field.

<!-- b000024 | prose | pages [1] -->
Each school was given a Goodness rating based on added GDP and the median salary of its alumni. Salary was simply scaled and added to GDP in order to compute this metric.

<!-- b000025 | prose | pages [1] -->
The centerpiece of our proposal is a linear regression model relating Goodness to a combination of the school's tuition and enrollment. This model is meant to contain general information about how a school's resources impact its Goodness.

<!-- b000026 | prose | pages [1] -->
The posteriors of this overall model are used as priors for the parameters of a series of models (these priors are injected with additional variance so as not to overwhelm the data), each one fit to a particular school. Each of these models represents a predicted relationship between a school's available funds per student and its Goodness, as well as how a change in its funds would affect its Goodness, which we call a Goodness curve.

<!-- b000027 | prose | pages [1] -->
We model the investment of money in a school as increasing the "effective tuition" of that school, which will increase the Goodness of that school according to its Goodness curve. This change in Goodness is our proposal for measuring RoI.

<!-- b000028 | prose | pages [1] -->
Given this definition of RoI, we are presented with the question of where investments should be disbursed such that the sum of RoI is maximized: a simple optimization problem which we solve in order to obtain our results for proposal.

<!-- b000029 | prose | pages [1] -->
Such curves are calculated for each year from 2016 to 2020, based on econometrics forecasts in US GDP changes and population growth.

<!-- b000030 | prose | pages [1] -->
Each single stage of our model is simple, and the model in its entirety is complex rather than com- plicated. This leads to a model which, while far from trivial, is easy to interpret.

<!-- b000031 | prose | pages [1] -->
We present 73 schools to be funded based on our analysis. Among them are such well known schools as Princeton, Harvard, and MIT, along with a collection of other, lesser well known schools, which are expected to be as important of investment targets for the American economy according to our model. We also present the time periods during which we believe funding would be most effective.

<!-- b000032 | prose | pages [1] -->
Data manipulation was performed in R and Python. BUGS was used for Bayesian inference on the model parameters, and R was used to solve the concomitant optimization problem.

<!-- b000033 | furniture | pages [2] -->
Team #52815

<!-- b000034 | furniture | pages [2] -->
Page 1 of 17

<!-- b000035 | prose | pages [2] -->
Mr. Alpha Chiang :

<!-- b000036 | prose | pages [2] -->
We are writing to you regarding the investment strategy of the Goodgrant Foundation. We have created a suﬃcient model for dispersing the donations to colleges in a way that would enhance the Return on Investment (RoI) for Goodgrant and thus the beneﬁts for the impacted students. This model was developed due in large part to the analysis of data provided by the U.S. National Center on Education Statistics. Considering the lack of an oﬃcial RoI measurement regarding the funding of schools, we opted to create our own before model creation. This measurement was a function of what we called Goodness obtained by and resources available to a given school. Goodness was assessed as a school’s contribution to the U.S. Gross Domestic Product (GDP). Resources were deﬁned as a school’s annual income from tuition and external funds. This RoI was optimized by the model’s simulations.

<!-- b000037 | prose | pages [2] -->
Jobs added by a given school were calculated by considering the unemployment rates for each major and the number of undergraduate degrees awarded by a school. This was compared to the unemployment rate of those with bachelor’s degrees in the respective majors across the United States. A positive relationship was then found between the amount of jobs added and the change in GDP. Therefore, schools were assigned high goodness if they awarded a large amount of degrees in ﬁelds that were undersaturated in the U.S. economy.

<!-- b000038 | prose | pages [2] -->
The $500,000,000 that Goodgrant plans to donate is disbursed on a yearly basis in the analysis. The simulations determine which schools to invest in and how much to invest in each school. The time duration over which the money should be invested is also included. These durations were a result of forecasted GDP and population data over the next ﬁve years.

<!-- b000039 | prose | pages [2] -->
We ﬁrst computed an overall model by looking at the relationship between resources and goodness for all the schools on which we had data. Then, using this ﬁrst model as a starting point, we developed individual models for each school. That is to say, we have an individual relationship between how much funding each school receives and how much it’s able to contribute to the economy based on that income, as well as a custom estimation for the rate at which decreasing marginal returns occur for each school.

<!-- b000040 | prose | pages [2] -->
Based on these data, we estimated RoI over time by comparing the change in resources to the change in Goodness as a result of each respective investment. Then, we ran a number of simulations to allocate the individual investments that maximized the RoI. These investments are allocated until the overall donation amount is exhausted, leaving us with a plan to best disburse the grants every year.

<!-- b000041 | prose | pages [2] -->
After optimizing RoI, 73 schools were given at least some sort of investment. Most were small, possibly underdeveloped schools that would beneﬁt greatly from a private contribution. There are also a few highly developed schools that were recommended for investment such as Princeton. The yearly investments in these schools are provided by the model.

<!-- b000042 | prose | pages [2] -->
The recommended investments output from the model optimize an acceptable metric for gauging the added value to the invested schools. Multiple models were compared to one another to arrive at a concluded model for the recommended investments. We are conﬁdent that this model will realize its full potential.

<!-- b000043 | prose | pages [2] -->
Sincerely,

<!-- b000044 | prose | pages [2] -->
MCM Team Members

<!-- b000045 | furniture | pages [3] -->
Team #52815

<!-- b000046 | furniture | pages [3] -->
Page 2 of 17

<!-- b000047 | contents | pages [3] -->
A Multilevel Bayesian Model based on Economic Contribution of

<!-- b000048 | contents | pages [3] -->
University Alumni

<!-- b000049 | contents | pages [3] -->
February 1, 2016

<!-- b000050 | heading | pages [3] -->
Contents

<!-- b000051 | contents | pages [3] -->
1 Introduction

<!-- b000052 | contents | pages [3] -->
3

<!-- b000053 | contents | pages [3] -->
2 Data Cleaning and Imputation Schema

<!-- b000054 | contents | pages [3] -->
3

<!-- b000055 | contents | pages [3] -->
2.1

<!-- b000056 | contents | pages [3] -->
Data Gathering, Cleaning and Filtering

<!-- b000057 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000058 | contents | pages [3] -->
3

<!-- b000059 | contents | pages [3] -->
2.2

<!-- b000060 | contents | pages [3] -->
Imputation Schema . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000061 | contents | pages [3] -->
4

<!-- b000062 | contents | pages [3] -->
3 Model Components

<!-- b000063 | contents | pages [3] -->
4

<!-- b000064 | contents | pages [3] -->
3.1

<!-- b000065 | contents | pages [3] -->
Model Overview

<!-- b000066 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000067 | contents | pages [3] -->
5

<!-- b000068 | contents | pages [3] -->
3.2

<!-- b000069 | contents | pages [3] -->
Contribution to GDP

<!-- b000070 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000071 | contents | pages [3] -->
5

<!-- b000072 | contents | pages [3] -->
3.3

<!-- b000073 | contents | pages [3] -->
Final Cross Sectional Model Speciﬁcation

<!-- b000074 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000075 | contents | pages [3] -->
8

<!-- b000076 | contents | pages [3] -->
3.4

<!-- b000077 | contents | pages [3] -->
Funding Over Time . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000078 | contents | pages [3] -->
8

<!-- b000079 | contents | pages [3] -->
3.5

<!-- b000080 | contents | pages [3] -->
Analysis of Linear Model Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000081 | contents | pages [3] -->
8

<!-- b000082 | contents | pages [3] -->
4 Solving the Optimization Problem

<!-- b000083 | contents | pages [3] -->
10

<!-- b000084 | contents | pages [3] -->
4.1

<!-- b000085 | contents | pages [3] -->
Minimal Equivalent Example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000086 | contents | pages [3] -->
10

<!-- b000087 | contents | pages [3] -->
4.2

<!-- b000088 | contents | pages [3] -->
Full Optimization Scheme . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000089 | contents | pages [3] -->
10

<!-- b000090 | contents | pages [3] -->
4.3

<!-- b000091 | contents | pages [3] -->
Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000092 | contents | pages [3] -->
11

<!-- b000093 | contents | pages [3] -->
5 Problem Statement and Special Considerations

<!-- b000094 | contents | pages [3] -->
11

<!-- b000095 | contents | pages [3] -->
6 Model Analysis

<!-- b000096 | contents | pages [3] -->
12

<!-- b000097 | contents | pages [3] -->
6.1

<!-- b000098 | contents | pages [3] -->
Why Bayes? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000099 | contents | pages [3] -->
12

<!-- b000100 | contents | pages [3] -->
6.2

<!-- b000101 | contents | pages [3] -->
Model Limitations

<!-- b000102 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000103 | contents | pages [3] -->
12

<!-- b000104 | contents | pages [3] -->
6.3

<!-- b000105 | contents | pages [3] -->
Model Assumptions

<!-- b000106 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000107 | contents | pages [3] -->
12

<!-- b000108 | contents | pages [3] -->
6.4

<!-- b000109 | contents | pages [3] -->
Model Strengths

<!-- b000110 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000111 | contents | pages [3] -->
13

<!-- b000112 | contents | pages [3] -->
6.5

<!-- b000113 | contents | pages [3] -->
Potential Improvements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000114 | contents | pages [3] -->
13

<!-- b000115 | contents | pages [3] -->
7 Results from Model

<!-- b000116 | contents | pages [3] -->
13

<!-- b000117 | contents | pages [3] -->
8 Conclusions

<!-- b000118 | contents | pages [3] -->
15

<!-- b000119 | contents | pages [3] -->
8.1

<!-- b000120 | contents | pages [3] -->
Unconstrained Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000121 | contents | pages [3] -->
15

<!-- b000122 | contents | pages [3] -->
8.2

<!-- b000123 | contents | pages [3] -->
Constrained Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000124 | contents | pages [3] -->
16

<!-- b000125 | contents | pages [3] -->
8.3

<!-- b000126 | contents | pages [3] -->
Evaluation of Assumptions

<!-- b000127 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000128 | contents | pages [3] -->
16

<!-- b000129 | furniture | pages [4] -->
Team #52815

<!-- b000130 | furniture | pages [4] -->
Page 3 of 17

<!-- b000131 | heading | pages [4] -->
1 Introduction

<!-- b000132 | prose | pages [4] -->
Starting in July 2016, the Goodgrant Foundation will provide an overall donation amount of $500,000,000 over the course of 5 years ($100,000,000 per year) to various schools. This donation amount will be allotted to certain schools based on the school’s return on investment (RoI). A school’s projected RoI will determine whether or not the school will receive any investment whatsoever, how much money the school will receive, and the time duration over which the school will receive the money. Solid investments will have a positive eﬀect on overall student performance.

<!-- b000133 | prose | pages [4] -->
While it is acknowledged that, in general, investment in tertiary education has lower RoI than invest- ment in primary education, there are still important returns to expanding higher education, especially in developed countries such as the United States [24]. In particular, we will show the impact that investment in universities can have on GDP. Investing money in the development of skilled workers is not only beneﬁcial to the economy, it is necessary for the US to compete globally. We hope that this document will help to show how best that can be achieved.

<!-- b000134 | prose | pages [4] -->
Return on Investment was calculated as a function of the school’s ”goodness” and the school’s resources. Goodness and resources were determined using the provided data sets and external data sets. Before review, the data required various preparation techniques.

<!-- b000135 | heading | pages [4] -->
2 Data Cleaning and Imputation Schema

<!-- b000136 | prose | pages [4] -->
Any serious statistical analysis begins with substantial work on the data. The data provided had a panoply of issues ranging from unnatural variables, structural and seemingly random missingness, and impossible observations. Their rectiﬁcation was prerequisite to model ﬁtting and analysis.

<!-- b000137 | heading | pages [4] -->
2.1 Data Gathering, Cleaning and Filtering

<!-- b000138 | prose | pages [4] -->
For our approach to evaluating RoI, the gathering of unemployment measurements for each major that was referred to in the given data sets was required. Multiple sources were referred to in collecting these measurements [6, 12, 19, 25, 26]. It was also necessary to obtain average starting salary for each major [8, 9, 13, 14, 15, 16, 17, 20].

<!-- b000139 | prose | pages [4] -->
Initial data cleaning was performed in Python, where we re-organized variables into a more natural structure (for example, there were two tuition variables, one for public and one for private schools, as opposed to one tuition variable and one private/public ﬂag). Certain schools were found to have negative average tuition. We considered this to be measurement error, and removed from consideration for funding any school reporting negative average tuition.

<!-- b000140 | prose | pages [4] -->
Next, we analyzed the missingness structure in R. The MI package (short for Multiple Imputation) [23] has many useful tools for dealing with missing data problems. Among these is a heatmap of missing cases and observations clustered by missingness structure. Figure 1 shows the initial missingness structure.

<!-- b000141 | prose | pages [4, 5] -->
In Figure 1, the x axis represents cases, the y variables (the names of which are not intended to be legible). There are a number of schools which are missing the majority of variables, shown at the top of the missingness image. These schools were not considered for funding due to the lack of information, and were removed from the analysis. There is a large block on the left, representing the lack of SAT or ACT scores for a majority of schools. These variables were not included in our analysis because of this lack of data for most schools. On the right, a strange missingness pattern is observed, but this is due to the factors applying either to public or private schools and is rectiﬁed in the python script. Any further missingness was handled by our imputation schema.

<!-- b000142 | furniture | pages [5] -->
Team #52815

<!-- b000143 | furniture | pages [5] -->
Page 4 of 17

<!-- b000144 | caption | pages [5] -->
Figure 1: Initial Missingness Structure of Data

<!-- b000146 | heading | pages [5] -->
2.2 Imputation Schema

<!-- b000147 | prose | pages [5] -->
We identiﬁed two distinct kinds of missingness in the data, and modeled it with two diﬀerent mecha- nisms.

<!-- b000148 | prose | pages [5] -->
Firstly, data simply missing from the model were assumed to be Missing Completely at Random (MCAR). BUGS treats missing values as parameters and conducts inference on them automatically. As we are acting as Bayesians, we must specify priors for them, and choose to use a very disperse normal distribution centered at zero.

<!-- b000149 | prose | pages [5] -->
We were not comfortable making this same assumption with the ”Privacy Suppressed” Data. In reporting the data, aggregators are required to censor data if they believe it may be possible to make reasonable inferences on personal data of any individual. Oftentimes, this is the case if the data represents an aggregation from very few people. We believe that schools with few people may have diﬀerent characterisitcs than schools in general, and so these were not assumed to be MCAR, but Missing at Random (MAR), that is, whether or not they are missing depends on other variables in our model. These data were estimated using a multiple regression model depending on the complete data [21].

<!-- b000150 | heading | pages [5] -->
3 Model Components

<!-- b000151 | prose | pages [5] -->
There were two means of assessing how contributions to a school would increase its goodness. The ﬁrst was a measurement of how well the school is doing at satisfying the nation’s needs with respect to the skills of its graduated students. The second was simply a function of the median salary for that school.

<!-- b000152 | furniture | pages [6] -->
Team #52815

<!-- b000153 | furniture | pages [6] -->
Page 5 of 17

<!-- b000154 | prose | pages [6] -->
The resources of a given school were calculated by estimating the annual tuition income and the annual funds added externally to the school.

<!-- b000155 | heading | pages [6] -->
3.1 Model Overview

<!-- b000156 | prose | pages [6] -->
The data did not come with any kind of response; there was no measurement of how deserving a school was of money. As such, we had to create our own, which we will refer to as Goodness. Return on Investment was deﬁned as a change in Goodness. We hypothesized that there would be a positive, concave down relationship between the amount of resources available to a school and its Goodness. The relationship was expected to be positive because, in general, a school with access to more money is expected to be able to produce better results, and concave down due to the law of diminishing marginal returns.

<!-- b000157 | prose | pages [6] -->
Speciﬁcally, resources are deﬁned as the tuition per student, as well as the total enrollment for the school, and Goodness is a linear combination of a school’s contribution to GDP (deﬁned below) and the median salary of its alumni. We ﬁrst computed an overall model:

<!-- b000158 | prose | pages [6] -->
Goodness = ln(Tuition) + Enrollment + ϵ

<!-- b000159 | prose | pages [6] -->
ϵ N(0, τI)

<!-- b000160 | prose | pages [6] -->
Next, we computed an individual model for each school. The posterior for the model described above was given extra uncertainty (variance), and was used as a prior for each school [1].

<!-- b000161 | prose | pages [6] -->
P(Ms|X) ∝L(Ms|Xs)P(Ms|X)

<!-- b000162 | prose | pages [6] -->
This gave us an estimated Goodness or RoI Curve for each school. Given these curves, the idea was to maximize RoI through a change in per capita dollar amount, theoretically added to each school’s resources to change its eﬀective tuition. A more precise overview of how schools were chose based on this model may be found in the optimization section.

<!-- b000163 | heading | pages [6] -->
3.2 Contribution to GDP

<!-- b000164 | prose | pages [6] -->
The model related the proportion of students in each course of study to GDP in a several step process. The ﬁrst step was to identify how many jobs each school is expected to add to the economy. This was calculated based on the unemployment in the ﬁelds which a university was preparing students to work in. For example, if there is higher than usual unemployment in Psychology, we would rate colleges producing many Psychology majors as producing negative jobs (which would lead to an increase in unemployment). On the other hand, if there is lower than average unemployment in Computer Science, schools with many computer scientists would be rated as producing many jobs. The calculations were conducted as follows (DegreesAwardedπ is the proportion of degrees awarded, Unemployment is the mean unemployment of all majors, Unemploymentσ is the standard deviation of employment for all majors):

<!-- b000165 | prose | pages [6, 7] -->
Students = DegreesAwardedπ(Enrollment) Unemploymentδ = Unemployment −Unemployment Unemploymentσ

<!-- b000166 | furniture | pages [7] -->
Team #52815

<!-- b000167 | furniture | pages [7] -->
Page 6 of 17

<!-- b000169 | prose | pages [7] -->
JobsAdded = Students(DegreesAwardedπ)(Unemploymentδ)

<!-- b000170 | prose | pages [7] -->
If a school was found to have a net decrease in jobs, it was removed from consideration for fund- ing.

<!-- b000171 | prose | pages [7] -->
We next map jobs added to the economy to a change in the unemployment rate for each major. This is simply deﬁned as follows:

<!-- b000172 | prose | pages [7] -->
CurrentJobs = LaborForce(1 −Unemploymentinitial)

<!-- b000173 | prose | pages [7] -->
Unemploymentfinal = 1 −CurrentJobs + JobsAdded LaborForce

<!-- b000174 | prose | pages [7] -->
Unemployment∆= Unemploymentfinal −Unemploymentinitial

<!-- b000175 | prose | pages [7] -->
It is well known that there is a relationship between real gross domestic product (GDP) and unemploy- ment [4], and there exist complicated economic models relating the two [22]. However, we chose to ﬁt our own simple model to unemployment and GDP data spanning from 1948 to 2015 obtained from the Bureau of Economic Analysis [11] and the Bureau of Labor Statistics [2], respectively, for use in our greater model. We are not directly concerned with the relationship between GDP and unemployment, but with the relationship between a change in GDP and a change in unemployment. As such our model is as such:

<!-- b000176 | prose | pages [7] -->
ln(∆GDP) = ∆Unemployment + ϵ

<!-- b000177 | prose | pages [7] -->
ϵ N(0, σI)

<!-- b000178 | prose | pages [7] -->
We use the natural log of a change in GDP because while reasonable values for GDP have greatly increased since 1948, reasonable values for unemployment have remained about the same. So our model predicts not on an absolute change in GDP, but a percent change in GDP (when back-transformed from log space).

<!-- b000179 | prose | pages [7] -->
ln(∆GDP) = ln(GDPfinal) −ln(GDPinitial)

<!-- b000180 | prose | pages [7] -->
ln(∆GDP) = ln(GDPfinal/GDPinitial)

<!-- b000181 | prose | pages [7, 8] -->
eln(∆GDP ) = GDPfinal/GDPinitial But in our model, we want an absolute change in GDP. We obtain this using the following for- mula:

<!-- b000182 | furniture | pages [8] -->
Team #52815

<!-- b000183 | furniture | pages [8] -->
Page 7 of 17

<!-- b000184 | caption | pages [8] -->
Figure 2: Regression of ∆logGDP vs ∆Unemployment

<!-- b000186 | prose | pages [8] -->
∆GDP = eMLEGDPinitial −GDPinitial

<!-- b000187 | prose | pages [8] -->
∆GDP = eln(GDPfinal/GDPinitial)GDPinitial −GDPinitial

<!-- b000188 | prose | pages [8] -->
∆GDP = GDPfinal GDPinitial −GDPinitial GDPinitial

<!-- b000189 | prose | pages [8] -->
∆GDP = GDPfinal −GDPinitial

<!-- b000190 | prose | pages [8] -->
The model ﬁt looks surprisingly good. See in Figure 2 a scatterplot of the chart with regression line plotted.

<!-- b000191 | prose | pages [8] -->
This negative relationship was manipulated to evaluate the goodness that would be added by a possible Goodgrant contribution. The jobs that are added to a particular ﬁeld decrease the overall unemployment rate and thus increase the GDP. While keeping resources constant, an increase in GDP leads to a positive ROI.

<!-- b000192 | furniture | pages [9] -->
Team #52815

<!-- b000193 | furniture | pages [9] -->
Page 8 of 17

<!-- b000194 | heading | pages [9] -->
3.3 Final Cross Sectional Model Speciﬁcation

<!-- b000195 | prose | pages [9] -->
Once the data were manipulated as desired in Python and R, BUGS was called from within R to sample from the posterior distribution. The model as speciﬁed to BUGS was as such:

<!-- b000196 | prose | pages [9] -->
Goodness = β0 + β1ln(Price) + β2Enrollment + β3ln(Price)Enrollment + ϵ

<!-- b000197 | prose | pages [9] -->
ϵ ∼N(0, τI)

<!-- b000198 | prose | pages [9] -->
β ∼N(0, 0.00001)

<!-- b000199 | prose | pages [9] -->
τ ∼Γ(0.00001, 0.00001)

<!-- b000200 | prose | pages [9] -->
For Missing Completely at Random Data:

<!-- b000201 | prose | pages [9] -->
Salary ∼N(0, 0.00001)

<!-- b000202 | prose | pages [9] -->
For Missing at Random Data:

<!-- b000203 | prose | pages [9] -->
Salary =⃗γX

<!-- b000204 | prose | pages [9] -->
Where X is a matrix of other covariates and γ is a vector of coeﬃcients relating the two.

<!-- b000205 | heading | pages [9] -->
3.4 Funding Over Time

<!-- b000206 | prose | pages [9] -->
In order to answer the question of when these funds should be dispersed, we simply recomputed our model posteriors for diﬀerent values of economic data. We used forecasted econometric [10] and population data [7] in our calculations. We assumed that the percent of the US population making up the Labor Force would stay constant over the next ﬁve years for our Job Added calculations. We did not inject any other diﬀerent information into the model when computing the coeﬃcients at diﬀerent times.

<!-- b000207 | heading | pages [9] -->
3.5 Analysis of Linear Model Assumptions

<!-- b000208 | prose | pages [9] -->
We will in this section perform an analysis of the residuals of the regression model in order to determine whether any of the assumptions of linear models have been validated.

<!-- b000209 | prose | pages [9] -->
We ﬁrst consider a normal Quantile-Quantile Plot (Figure 3). It does not look perfectly normal, contrary to the assumptions which lead to our posterior estimates, but it is close enough.

<!-- b000210 | prose | pages [9] -->
This predicted versus residual plot is more worrisome (Figure 4). We actually see a decrease in variance as the predicted value increases. This plot shows that our model is not perfect.

<!-- b000211 | prose | pages [9] -->
The error of the prediction seems to increase as the predicted value increases (Figure 5). This plot again serves as evidence against this model the most correct.

<!-- b000212 | furniture | pages [10] -->
Team #52815

<!-- b000213 | furniture | pages [10] -->
Page 9 of 17

<!-- b000214 | caption | pages [10] -->
Figure 3: Q-Q Plot for Main Model

<!-- b000215 | caption | pages [10] -->
Figure 4: Residual vs Predicted Plot for Main Model

<!-- b000216 | furniture | pages [11] -->
Team #52815

<!-- b000217 | furniture | pages [11] -->
Page 10 of 17

<!-- b000218 | caption | pages [11] -->
Figure 5: Actual vs Predicted Plot for Main Model

<!-- b000219 | heading | pages [11] -->
4 Solving the Optimization Problem

<!-- b000220 | prose | pages [11] -->
Our model as described above is only part of our solution. Given it, we are able to calculate the most beneﬁcial distribution of available funds. How this is done will be described here.

<!-- b000221 | heading | pages [11] -->
4.1 Minimal Equivalent Example

<!-- b000222 | prose | pages [11] -->
Consider an example (see Figure 6) in which we have only two schools competing for Goodgrant’s funds. School A has a coeﬃcient of 1 to relate log of funding with Goodness, while School B has a coeﬃcient of 0.2. Both graphs above show what the change in Goodness is for a disbursement of 1.3 thousand dollars to each school would be.

<!-- b000223 | prose | pages [11] -->
Obviously, the disbursement has a larger eﬀect on the school on the left (School A), so we would choose to fund it over the school on the right (School B). This is essentially how our optimization problem works; we iteratively check which school would most beneﬁt from a small disbursement until we have exhausted our funds.

<!-- b000224 | prose | pages [11] -->
The above example is just a simple case of our investments. When considering our real model, the problem becomes how much overall disbursement each school should be given from the Goodgrant Foundation to maximize RoI.

<!-- b000225 | heading | pages [11] -->
4.2 Full Optimization Scheme

<!-- b000226 | prose | pages [11, 12] -->
Our approach for the full optimization problem is simply to iteratively calculate the Goodness/Resource slope for each school, and choosing to fund the school which resulted in the largest increase in Goodness on each iteration until all our funds are depleted.

<!-- b000227 | furniture | pages [12] -->
Team #52815

<!-- b000228 | furniture | pages [12] -->
Page 11 of 17

<!-- b000229 | caption | pages [12] -->
Figure 6: 2D Example of Optimizing Funding Distribution

<!-- b000231 | heading | pages [12] -->
4.3 Algorithm

<!-- b000232 | prose | pages [12] -->
Below is the algorithm we have created for the optimization process. We denotes r as resources, s as number of students enrolled in a school, and β as the parameter matrix (recall that this is matrix as opposed to a vector because each school has its own model). The variable of interest, Goodness, is represented by g, and constant money distributed denotes as m

<!-- b000233 | prose | pages [12] -->
Algorithm 1 Initiate r, s, and m0 Compute ginit = β ∗r while m0 > 0 —–Compute gnext = β ∗(r + 1) —–Compute ∆= gnext −ginit —–Find where.max(δ) = i —–Updates mk = m0 −si —–Updates ginit = gnext end

<!-- b000234 | heading | pages [12] -->
5 Problem Statement and Special Considerations

<!-- b000235 | prose | pages [12] -->
The concern of this paper is an allocation of resources problem. The goal is to maximize the impact of 100 million dollars injected into the US tertiary education system per year for the next ﬁve years.

<!-- b000236 | prose | pages [12] -->
We are to make a recommendation to the Goodgrant foundation for how to evaluate the impact of disbursed money on a school, to which schools to give money, how much to give to each school, and the expected return for each school.

<!-- b000237 | prose | pages [12, 13] -->
Outside of analysis, various characteristics were considered when evaluating a school’s worthiness of investment. These characteristics impacted our approaches to analysis. Among these characteristics are the external funds added. In general, public schools are given more external funds than are private schools. An estimated amount of twice that of private schools was used when calculating a public school’s resources [5]. Further, community colleges’ funding was multiplied by ﬁve. Justiﬁcation for this is based on results from such models.

<!-- b000238 | furniture | pages [13] -->
Team #52815

<!-- b000239 | furniture | pages [13] -->
Page 12 of 17

<!-- b000241 | heading | pages [13] -->
6 Model Analysis

<!-- b000242 | prose | pages [13] -->
6.1 Why Bayes?

<!-- b000243 | prose | pages [13] -->
Many times, Bayesian approaches can be more diﬃcult computationally than frequentist ones. Further, the frequentist approach is the standard approach in statistics. As such, we feel it necessary to defend our use of full Bayesian methods. We chose to implement a Bayesian model for two main reasons.

<!-- b000244 | prose | pages [13] -->
Firstly, imputation of missing data is natural in a Bayesian model, both in theory and in implementa- tion.

<!-- b000245 | prose | pages [13] -->
Second, it is important to maintain full accountability for uncertainty when we are applying functions with non-zero concavity to data in which we are not absolutely certain [27]. For instance, consider the exponential function relating Jobs Added an GDP. Because exponential functions are concave up, we would underestimate change in GDP if we did not account for our uncertainty.

<!-- b000246 | heading | pages [13] -->
6.2 Model Limitations

<!-- b000247 | prose | pages [13] -->
Because our gathered unemployment data relates only to undergraduate degrees, we only considered univer- sities which primarily granted undergraduate degrees.

<!-- b000248 | prose | pages [13] -->
One of the model’s most serious weaknesses is the lack of any time series data with respect to most of the model’s inputs. As mentioned in Section 3.3, all data directly related to schools, as well as ﬁeld-speciﬁc unemployment, is entirely cross-sectional, and time series estimates are a result of varying only national economic data.

<!-- b000249 | prose | pages [13] -->
Much data on school funding was estimated, oftentimes in an ad-hoc manner. Should reality diﬀer signiﬁcantly from our estimates, the model will be wrong.

<!-- b000250 | heading | pages [13] -->
6.3 Model Assumptions

<!-- b000251 | prose | pages [13] -->
As this is a linear model, it assumes that the relationships as described by the model equation are accurate. That is, that goodness is approximately a linear combination of the log of its tuition and its enrollment. The Section 3.5 shows that there are some issues with this assumption. As discussed in Model Limitations, this model assumes that much of its inputs stay constant over the next ﬁve years.

<!-- b000252 | prose | pages [13] -->
Unemployment data for diﬀerent majors were not all found for the same year; as such, we make the assumption that unemployment rates have been fairly constant between and within ﬁelds during the last few years, and will remain so for the next ﬁve years.

<!-- b000253 | prose | pages [13] -->
Because there are so many missing variables, the correctness of the model depends strongly on the assumption that there is no signiﬁcant structure in the missing data which cannot be accounted for in other known variables, that is to say, we must assume the data are not missing based on unobserved predictors[3].

<!-- b000254 | furniture | pages [14] -->
Team #52815

<!-- b000255 | furniture | pages [14] -->
Page 13 of 17

<!-- b000256 | heading | pages [14] -->
6.4 Model Strengths

<!-- b000257 | prose | pages [14] -->
While there are many steps to go from inputs to outputs, each step individually is easy to understand, meaning that the model at each stage, as well as as a whole, is easily interpretable. In the same vein, mapping from a subset of the variables to a change in GDP is very easily interpretable as a form of Return on Investment.

<!-- b000258 | prose | pages [14] -->
Because we take a Bayesian approach, we maintain full accountability for uncertainty, as described in Section 6.1.

<!-- b000259 | heading | pages [14] -->
6.5 Potential Improvements

<!-- b000260 | prose | pages [14] -->
We believe there are many improvements which could be made to this model under diﬀerent time constraints. The ﬁrst would be a change from what is essentially a linear regression model to a dynamic linear model. It is possible to download historical data similar to those provided with the problem, which would allow such a model to be ﬁt. However, signiﬁcant data manipulation eﬀorts would need to be undertaken.

<!-- b000261 | prose | pages [14] -->
The accuracy of the model would potentially increase with more resource factors to act as ”controls”, such as faculty:student ratios or more precise state and alumni funding estimates.

<!-- b000262 | prose | pages [14] -->
The model would also beneﬁt from additional factors included in Goodness. In particular, we hypoth- esize that the inclusion of some measure of how much research is produced by a university would be very beneﬁcial.

<!-- b000263 | heading | pages [14] -->
7 Results from Model

<!-- b000264 | caption | pages [14] -->
Table 1 shows the result from Bayesian Time-Series Model with constraints on the maximum disbursement

<!-- b000265 | prose | pages [14] -->
to a particular school. Another table 2 is generated from Bayesian model with no constrains from how much a school should receive.

<!-- b000266 | caption | pages [14] -->
Table 1: Schools Investment Strategy with Max Investment Constraints

<!-- b000267 | prose | pages [14, 15] -->
Schools Year One Year Two Year Three Year Four Year Five Total ROI Georgia Perimeter College 50017570 0 0 0 0 50017570 145.520 CUNY Bernard M Baruch College 0 14465088 21889404 13656906 0 50011398 92.565 University of Wisconsin Colleges 0 13181345 27852585 8976693 0 50010623 89.411 Harvard University 7903908 22066896 11198661 8835492 0 50004957 86.323 Princeton University 23615407 13446146 6746626 6191822 0 50000001 85.440 Bergen Community College 0 0 0 8254656 17071199 25325855 81.962 Moorpark College 0 0 3668301 8734050 8330940 20733291 81.962 United States Merchant Marine Academy 11182734 3809966 1880554 1816368 1008774 19698396 81.962 MCPHS University 0 0 0 9588544 5712000 15300544 81.962 Richland College 0 0 0 0 14668722 14668722 81.962 University of Puerto Rico-Arecibo 0 0 0 0 14623308 14623308 81.961 Massachusetts Institute of Technology 0 0 1573990 7328750 4167240 13069980 81.961 Shorter College 908490 0 10073910 0 0 10982400 81.961 University of Puerto Rico-Aguadilla 0 9492054 0 0 1292928 10784982 81.961 Stanford University 0 0 0 5702660 4446260 10148920 81.961 Tallahassee Community College 0 0 0 0 9725706 9725706 81.961 Leeward Community College 0 1358428 3096504 2645672 2331276 9431880 81.961 New England College of Business and Finance 0 8653068 0 0 0 8653068 81.961 University of Puerto Rico-Humacao 0 0 0 0 8166562 8166562 81.961 Baptist Memorial College of Health Sciences 1074576 2287878 1156050 1105404 642984 6266892 81.960 Albany College of Pharmacy and Health Sciences 0 0 2160750 2478950 1394275 6033975 81.960 Berea College 2031360 961722 477687 461817 260268 4192854 81.960 Universidad Pentecostal Mizpa 0 0 0 4042477 0 4042477 81.960 Christian Brothers University 337552 1513204 750244 723656 405756 3730412 81.960 Belanger School of Nursing 0 0 0 3687048 0 3687048 81.959 St Paul’s School of Nursing-Staten Island 0 0 1220598 1282599 721602 3224799 81.959 Yeshivat Mikdash Melech 282112 0 497192 1673216 0 2452520 81.959 Machzikei Hadath Rabbinical College 0 2286008 0 0 0 2286008 81.959 Eastern West Virginia Community and Technical College 0 727872 1323008 0 0 2050880 81.959 Talmudical Seminary of Bobov 0 382522 221040 991303 0 1594865 81.958 Lincoln Trail College 805363 343252 172159 164697 94874 1580345 81.958 Doane College-Lincoln Grand Island and Master 0 110313 451346 431879 248024 1241562 81.958 Jewish Theological Seminary of America 0 0 0 33327 1190273 1223600 81.957 Crouse Hospital College of Nursing 0 287616 358176 345744 193200 1184736 81.957 Divine Word College 0 467072 675866 0 0 1142938 81.957 Curtis Institute of Music 757376 361730 0 0 0 1119106 81.957 Saint John Vianney College Seminary 335951 0 0 144298 359282 839531 81.956 Hobe Sound Bible College 0 0 0 0 677448 677448 81.955 Uta Mesivta of Kiryas Joel 0 0 675913 0 0 675913 81.955 Soka University of America 0 596576 0 0 0 596576 81.953 Olney Central College 0 115971 179800 169012 105183 569966 81.337 Leech Lake Tribal College 0 543660 0 0 0 543660 80.123 Bethesda University of California 0 0 0 0 525511 525511 78.548 College of the Marshall Islands 0 519688 0 0 0 519688 77.618 Cleary University 0 0 0 301500 213300 514800 68.546 Universidad Teologica del Caribe 0 273625 207756 0 0 481381 62.110 Yeshiva Derech Chaim 0 251576 0 0 225368 476944 59.620 Rabbinical Academy Mesivta Rabbi Chaim Berlin 137104 209428 0 114472 0 461004 56.118 Carolina Christian College 346140 0 95436 0 0 441576 51.497 Maple Springs Baptist Bible College and Seminary 0 0 438520 0 0 438520 51.485 Bais Medrash Toras Chesed 0 165072 0 0 179322 344394 45.115 Sh’or Yoshuv Rabbinical College 0 0 0 0 332310 332310 44.451 San Juan Bautista School of Medicine 13257 77382 197694 38394 0 326727 43.746 National Institute of Massotherapy 0 306234 0 0 0 306234 38.073 St Vincent’s College 0 0 0 0 287956 287956 35.602 Rabbinical Seminary of America 0 0 0 0 281643 281643 31.962 Yeshiva College of the Nations Capital 90620 148419 0 25415 0 264454 30.920 Allegheny Wesleyan College 0 0 263588 0 0 263588 29.886 Boise Bible College 0 263337 0 0 0 263337 29.779 University of the West 0 232114 0 0 0 232114 23.546 Talmudical Academy-New Jersey 160480 0 0 0 10064 170544 22.952 Telshe Yeshiva-Chicago 0 0 155909 0 0 155909 19.602 Talmudical Institute of Upstate New York 0 0 110177 0 0 110177 17.663 Rabbinical College Telshe 0 0 99848 0 0 99848 15.885 University of the Potomac-VA Campus 0 13598 31590 30602 16848 92638 15.295 White Earth Tribal and Community College 0 0 20938 0 69658 90596 15.105 Heritage Bible College 0 0 74638 0 0 74638 14.640 Southeastern Baptist College 0 69190 0 0 0 69190 14.216 South Florida Bible College and Theological Seminary 0 0 0 22577 0 22577 11.547 Central Maine Medical Center College of Nursing and Health Professions 0 0 0 0 19936 19936 9.632 Huntsville Bible College 0 11950 0 0 0 11950 2.642 American Indian College of the Assemblies of God Inc 0 0 3542 0 0 3542 2.585

<!-- b000268 | furniture | pages [15] -->
Team #52815

<!-- b000269 | furniture | pages [15] -->
Page 14 of 17

<!-- b000271 | caption | pages [15] -->
Table 2: Schools Investment Strategy without Constraints

<!-- b000272 | prose | pages [15, 16] -->
Schools Year One Year Two Year Three Year Four Year Five Total ROI Georgia Perimeter College 58544804 53548222 41285850 34604186 32971734 220954796 92.5870 University of Wisconsin Colleges 0 0 13530241 19085225 17326555 49942021 92.5870 Princeton University 21103488 8369166 5155490 4867620 3250314 42746078 92.5866 CUNY Bernard M Baruch College 0 0 13807584 15081498 13259664 42148746 92.5864 Harvard University 3813672 13782453 8573484 8056746 5480334 39706689 92.5859 United States Merchant Marine Academy 10464234 2357638 1431252 1363234 882318 16498676 92.5856 Moorpark College 0 0 0 2472408 7336602 9809010 92.5850 Shorter College 815100 0 8850600 0 0 9665700 92.5849 University of Puerto Rico-Aguadilla 0 7442994 0 0 683982 8126976 92.5848 University of Puerto Rico-Arecibo 0 0 0 0 7642122 7642122 92.5847 New England College of Business and Finance 0 6862050 0 0 0 6862050 92.5846 Leeward Community College 0 0 1738076 2088064 2052472 5878612 92.5843 Baptist Memorial College of Health Sciences 649590 1426896 885204 832356 562611 4356657 92.5840 Berea College 1852029 596712 365010 345966 228528 3388245 92.5840 Universidad Pentecostal Mizpa 0 0 0 3340905 0 3340905 92.5840 Belanger School of Nursing 0 0 0 3151014 0 3151014 92.5837 University of Puerto Rico-Humacao 0 0 0 0 2855252 2855252 92.5837 Christian Brothers University 53176 938672 571064 543320 356048 2462280 92.5830 Yeshivat Mikdash Melech 264936 0 414352 1472424 0 2151712 92.5825 Machzikei Hadath Rabbinical College 0 1948716 0 0 0 1948716 92.5820 Albany College of Pharmacy and Health Sciences 0 0 0 467625 1219050 1686675 92.5817 Eastern West Virginia Community and Technical College 0 343808 1140224 0 0 1484032 92.5812 Talmudical Seminary of Bobov 0 273844 185121 864512 0 1323477 92.5805 Lincoln Trail College 741403 213200 131651 124189 83148 1293591 92.5803 Divine Word College 0 410557 598614 0 0 1009171 92.5802 Curtis Institute of Music 717482 267302 0 0 0 984784 92.5801 St Paul’s School of Nursing-Staten Island 0 0 0 343620 630468 974088 92.5800 Jewish Theological Seminary of America 0 0 0 0 952637 952637 92.5789 Saint John Vianney College Seminary 317625 0 0 89859 317702 725186 92.5758 Crouse Hospital College of Nursing 0 0 149184 259392 169008 577584 92.5723 Doane College-Lincoln Grand Island and Master 0 0 0 273259 217021 490280 89.7398 Hobe Sound Bible College 0 0 0 0 378106 378106 89.4726 Carolina Christian College 325656 0 48240 0 0 373896 88.6888 Yeshiva Derech Chaim 0 155584 0 0 177840 333424 87.2778 Rabbinical Academy Mesivta Rabbi Chaim Berlin 97416 129560 0 74784 0 301760 86.6832 Olney Central College 0 0 66526 128557 91698 286781 76.5440 Universidad Teologica del Caribe 0 117211 167757 0 0 284968 68.5279 Maple Springs Baptist Bible College and Seminary 0 0 280440 0 0 280440 67.3181 Massachusetts Institute of Technology 0 0 0 0 279620 279620 62.6718 San Juan Bautista School of Medicine 8910 63504 174879 30159 0 277452 57.5081 Yeshiva College of the Nations Capital 84755 125557 0 16146 0 226458 50.1864 Bethesda University of California 0 0 0 0 226366 226366 49.7724 Bais Medrash Toras Chesed 0 84246 0 0 140448 224694 49.3984 Allegheny Wesleyan College 0 0 215377 0 0 215377 42.9887 National Institute of Massotherapy 0 211572 0 0 0 211572 35.6938 Sh’or Yoshuv Rabbinical College 0 0 0 0 172140 172140 34.1147 Talmudical Academy-New Jersey 145724 0 0 0 0 145724 32.9731 University of the West 0 143792 0 0 0 143792 25.6321 Soka University of America 0 137608 0 0 0 137608 21.8912 Telshe Yeshiva-Chicago 0 0 87770 0 0 87770 19.4881 Talmudical Institute of Upstate New York 0 0 87431 0 0 87431 17.7403 Rabbinical College Telshe 0 0 55216 0 0 55216 16.8754 Southeastern Baptist College 0 49136 0 0 0 49136 16.0518 White Earth Tribal and Community College 0 0 0 0 41470 41470 13.0379 University of the Potomac-VA Campus 0 0 884 22932 14742 38558 10.7562 Heritage Bible College 0 0 2479 0 0 2479 2.9507

<!-- b000273 | furniture | pages [16] -->
Team #52815

<!-- b000274 | furniture | pages [16] -->
Page 15 of 17

<!-- b000276 | heading | pages [16] -->
8 Conclusions

<!-- b000277 | heading | pages [16] -->
8.1 Unconstrained Model

<!-- b000278 | prose | pages [16] -->
Looking through the unconstrained data, we are pleased to see well-known, highly-respected schools such as Princeton, Harvard and the Massachusetts Institute of Technology. We believe this provides on its own some legitimacy to the model. We are also pleased to some lesser known universities, even including colleges in Puerto Rico, which is going through a kind of economic crisis at present [18]. However, we are investing almost half of all our total to Georgia Perimeter College. In order to rectify this, we introduce the constrained model.

<!-- b000279 | furniture | pages [17] -->
Team #52815

<!-- b000280 | furniture | pages [17] -->
Page 16 of 17

<!-- b000281 | heading | pages [17] -->
8.2 Constrained Model

<!-- b000282 | prose | pages [17] -->
Here, we cap the total investment in any one school to 50 million dollars. This has the eﬀect of increasing the number of schools to which we disburse any funds, and obviously of decreasing the mean investment to schools. We believe this model to be better because it better protects the potential RoI against unforeseen issues at any single school. This constrained model serves as our ﬁnal recommendation to the charity for how to disburse their funds.

<!-- b000283 | heading | pages [17] -->
8.3 Evaluation of Assumptions

<!-- b000284 | prose | pages [17] -->
Overall, we are satisﬁed with the model’s conformity to its assumptions. To the best of our knowledge, missing data do not pose an issue. There may be some issues with the linear model assumptions, but we do not believe them to be so serious as to seriously threaten the model’s power. Given this, we are conﬁdent in the conclusions of our model.

<!-- b000285 | heading | pages [17] -->
References

<!-- b000286 | references | pages [17] -->
[1] Bayesian linear models: Gory details.

<!-- b000287 | references | pages [17] -->
[2] Economy at a glance.

<!-- b000288 | references | pages [17] -->
[3] Missing data imputation.

<!-- b000289 | references | pages [17] -->
[4] Okun’s law.

<!-- b000290 | references | pages [17] -->
[5] State funding trends and policies on aﬀordability.

<!-- b000291 | references | pages [17] -->
[6] Unemployment by major - some degrees pay while others leave you paying. 2011.

<!-- b000292 | references | pages [17] -->
[7] 2014 national population projections, 2014.

<!-- b000293 | references | pages [17] -->
[8] The college degrees with the highest starting salaries in 2015, 2014.

<!-- b000294 | references | pages [17] -->
[9] College graduate salaries by major, 2014.

<!-- b000295 | references | pages [17] -->
[10] Eiu economic and commodity forecast, december 2015, 2015.

<!-- b000296 | references | pages [17] -->
[11] National economic accounts, 2015.

<!-- b000297 | references | pages [17] -->
[12] Accomodation and food services: Naics 72, 2016.

<!-- b000298 | references | pages [17] -->
[13] Architect 1 salaries, biologist 1 salaries, equipment engineer 1 salaries, information security analyst

<!-- b000299 | references | pages [17] -->
1 salaries, mechanic technician 1 salaries, precision assembler 1 salaries, public relations specialist 1

<!-- b000300 | references | pages [17] -->
salaries, production assistant salaries, 2016.

<!-- b000301 | references | pages [17] -->
[14] Average family consumer science salaries, average entry level personal assistant salaries, 2016.

<!-- b000302 | references | pages [17] -->
[15] Entry-level environmental consultant salary, entry-level transportation salary, 2016.

<!-- b000303 | references | pages [17] -->
[16] Entry-level translator salary, 2016.

<!-- b000304 | references | pages [17] -->
[17] Entry-level translator salary, entry-level librarian salary, entry-level naval architect salary, religious

<!-- b000305 | references | pages [17] -->
education director salary, entry level chaplain salary, 2016.

<!-- b000306 | furniture | pages [18] -->
Team #52815

<!-- b000307 | furniture | pages [18] -->
Page 17 of 17

<!-- b000308 | references | pages [18] -->
[18] For richer, for poorer, 2016.

<!-- b000309 | references | pages [18] -->
[19] Rate of unemployment by major, 2016.

<!-- b000310 | references | pages [18] -->
[20] Stem grads projected to earn class of 2016’s highest average starting salaries, 2016.

<!-- b000311 | references | pages [18] -->
[21] Charles DiMaggio. Bayesian analysis for epidemiologists part v: Special topics.

<!-- b000312 | references | pages [18] -->
[22] Jonathan Eaton, Samuel Kortum, and Brent Neiman.

<!-- b000313 | references | pages [18] -->
On deﬁcits and unemployment.

<!-- b000314 | references | pages [18] -->
Revue

<!-- b000315 | references | pages [18] -->
´economique, 64(3):405–420, 2013.

<!-- b000316 | references | pages [18] -->
[23] Andrew Gelman and Jennifer Hill. Opening windows to the black box. Journal of Statistical Software,

<!-- b000317 | references | pages [18] -->
40, 2011.

<!-- b000318 | references | pages [18] -->
[24] Claudio E Montenegro and Harry Anthony Patrinos. Returns to schooling around the world. Background

<!-- b000319 | references | pages [18] -->
Paper for the World Development Report, pages 8258024–132095074719, 2013.

<!-- b000320 | references | pages [18] -->
[25] Lynn O’Shaughnessy. 25 college majors with the highest unemployment rates.

<!-- b000321 | references | pages [18] -->
[26] Anna Swanson. The college majors with the highest unemployment rates, 2015.

<!-- b000322 | references | pages [18] -->
[27] Nassim Nicholas Taleb. Antifragile: Things That Gain From Disorder. Random House, 2012.
