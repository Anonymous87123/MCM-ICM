# P-C-2019-1900577-7ac4ae90

Status: machine-draft; not source-verified.


<!-- b000001 | title | pages [1] -->
The Gravity of the Opioid Crisis

<!-- b000002 | prose | pages [1] -->
The United States is in the midst of a national crisis due to the extreme abuse of opioids all across the country. More than ever before, users of all ages and demo- graphics are becoming addicted. To explore future impacts of this drug epidemic, we model and characterize the spread of substance abuse.

<!-- b000003 | prose | pages [1] -->
We use NFLIS drug report data 2010-2017 to develop a multivariate analysis of the spread of drug use in and between counties of Kentucky, Ohio, Pennsylvania, Virginia, and West Virginia. We base the development of the drug spread model on three main factors:

<!-- b000004 | prose | pages [1] -->
i. Drug-use inﬂuence ii. Current trend in drug reports iii. Pertinent socio-economic factors

<!-- b000005 | prose | pages [1] -->
We identify the current trend of drug reports by implementing a quadratic-weighted linear regression on existing county drug report data across time. To characterize the nature of drug-use inﬂuence on a county, we deﬁne a county’s drug inﬂuence factor as the density of drug reports per area. We ﬁnd the origins of speciﬁc opioids and de- termine the drug identiﬁcation thresholds based on the inﬂuence factor. Six counties crossed our determined threshold for our simulation from 2018 to 2025, indicating that the epidemic is increasing in intensity.

<!-- b000006 | prose | pages [1] -->
Using the principles of geographic gravity, we establish an inverse relationship between inﬂuence on other counties and distance as a weighted factor of their existing trend. We validate our model as a better predictor of the following year’s drug reports than the data from the previous year.

<!-- b000007 | prose | pages [1] -->
We then ﬁnd associations between drug reports and U.S. Census socio-economic factors over time.

<!-- b000008 | prose | pages [1] -->
With the highest correlated socio-economic data, we calculate a multivariate linear regression of the drug reports based on time. This adjusted model shows a 12.2% decrease in residuals of our predicted data against the real data, compared to the baseline.

<!-- b000009 | prose | pages [1] -->
We use strategies from other parts of the United States to make improvements in accommodating drug users. Using factors such as drug education and recovery centers, we estimate a reduction in overall drug consumption.

<!-- b000010 | furniture | pages [2] -->
Team #1900577

<!-- b000011 | furniture | pages [2] -->
1 of 24

<!-- b000012 | heading | pages [2] -->
Contents

<!-- b000013 | contents | pages [2] -->
1

<!-- b000014 | heading | pages [2] -->
Introduction

<!-- b000015 | prose | pages [2] -->
2 Problem Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 2 Data Sources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2.1 Data Cleaning 2 Existing Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.4 Our Model

<!-- b000016 | prose | pages [2] -->
2

<!-- b000017 | heading | pages [2] -->
Background

<!-- b000018 | prose | pages [2] -->
4

<!-- b000019 | prose | pages [2] -->
4 The Opioid Epidemic . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.1 4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.1.1 Classes of Opioids 4 Common Reasons for Substance Abuse . . . . . . . . . . . . . . . . . 2.1.2

<!-- b000020 | prose | pages [2] -->
3

<!-- b000021 | heading | pages [2] -->
Nomenclature

<!-- b000022 | prose | pages [2] -->
4

<!-- b000023 | heading | pages [2] -->
Assumptions

<!-- b000024 | prose | pages [2] -->
5

<!-- b000025 | heading | pages [2] -->
Model Development

<!-- b000026 | prose | pages [2] -->
5

<!-- b000027 | prose | pages [2] -->
5

<!-- b000028 | prose | pages [2] -->
5

<!-- b000029 | prose | pages [2] -->
6 Geographic Gravity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 6 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2 Model Construction 7 Extensions of the Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.3 8 Model Validation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.4 8 Application . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.5 5.5.1 Predicting Points of Origin 10 . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000030 | prose | pages [2] -->
11 Drug Identiﬁcation Threshold . . . . . . . . . . . . . . . . . . . . . . 5.5.2 11 Important Socio-Economic Inﬂuences . . . . . . . . . . . . . . . . . . . . . . 5.6 12 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.7 Adjustments

<!-- b000031 | prose | pages [2] -->
6

<!-- b000032 | heading | pages [2] -->
Results

<!-- b000033 | prose | pages [2] -->
13

<!-- b000034 | prose | pages [2] -->
15 Part I: Origin Prediction and Threshold . . . . . . . . . . . . . . . . . . . . 6.1 15 Part II: Socio-Economic Adjustments . . . . . . . . . . . . . . . . . . . . . . 6.2 15 Part III: Strategy for Countering the Crisis 6.3

<!-- b000035 | prose | pages [2] -->
7

<!-- b000036 | heading | pages [2] -->
Sensitivity Analysis

<!-- b000037 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . .

<!-- b000038 | prose | pages [2] -->
16

<!-- b000039 | prose | pages [2] -->
17 Variation of the Scale of Drug Reports . . . . . . . . . . . . . . . . . . . . . 7.1 7.2 Variation of Socio-economic Factors

<!-- b000040 | prose | pages [2] -->
8

<!-- b000041 | heading | pages [2] -->
Conclusion

<!-- b000042 | prose | pages [2] -->
17 . . . . . . . . . . . . . . . . . . . . . .

<!-- b000043 | prose | pages [2] -->
18

<!-- b000044 | prose | pages [2] -->
18 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.1 Model Strengths 18 Model Weaknesses and Limiting Assumptions . . . . . . . . . . . . . . . . . 8.2 19

<!-- b000045 | heading | pages [2] -->
Memo to the DEA/NFLIS Chief Administrator

<!-- b000046 | prose | pages [2] -->
9

<!-- b000047 | heading | pages [2] -->
References

<!-- b000048 | heading | pages [2] -->
Appendix

<!-- b000049 | prose | pages [2] -->
20

<!-- b000050 | prose | pages [2] -->
22

<!-- b000051 | prose | pages [2] -->
24

<!-- b000052 | furniture | pages [3] -->
Team #1900577

<!-- b000053 | furniture | pages [3] -->
2 of 24

<!-- b000054 | prose | pages [3] -->
1

<!-- b000055 | heading | pages [3] -->
Introduction

<!-- b000056 | prose | pages [3] -->
Drug abuse is an issue that the world has been plagued with for centuries. The ﬁrst study of morphine addiction was done in 1875, identifying the key factors for a user to become addicted to a substance [13]. In the past several decades in the United States, the opioid epidemic has increased at an alarming rate. Currently, an average of 130 citizens of the U.S die of an opioid overdose daily [4]. Understanding the spread of this epidemic can be used to inform government policy to get control of this crisis.

<!-- b000057 | prose | pages [3] -->
1.1 Problem Summary

<!-- b000058 | prose | pages [3] -->
For the U.S. government, it is a challenge to enforce anti-drug laws, especially amid the national crisis that is happening. The Drug Enforcement Administration (DEA) wishes to see if there are factors that contribute to the spread of opioid incidents between 5 states in the eastern United States — Ohio (OH), Kentucky (KY), West Virginia (WV), Virginia (VA), and Pennsylvania (PA).

<!-- b000059 | prose | pages [3] -->
We use data analysis to build a model that describes the spread of opioid cases in these states, with the ability to identify any possible locations where a speciﬁc drug might have originated. We then set a threshold which signiﬁes an unsafe level of drug use in the county, predicting where this will occur in the future. We then

<!-- b000060 | heading | pages [3] -->
add U.S. Census data to our model, implementing socio-economic factors into the

<!-- b000061 | prose | pages [3] -->
model. When then use this model to identify strategies for countering the opioid epidemic, and test the eﬀectiveness of these strategies.

<!-- b000062 | prose | pages [3] -->
1.2

<!-- b000063 | heading | pages [3] -->
Data Sources

<!-- b000064 | prose | pages [3] -->
Our model is informed by 8 years worth of drug identiﬁcation counts, 2010 to 2017, for narcotic analgesics and heroin from the National Forensic Laboratory Information System (NFLIS). We also derived geographic data from the NFLIS dataset [9]. The model is conditioned with 7 years worth of data from the U.S. Census Bureau, 2010 to 2016, that represents a common set of socio-economic factors.

<!-- b000065 | prose | pages [3] -->
1.2.1 Data Cleaning

<!-- b000066 | prose | pages [3] -->
The census data provided had missing and partially ﬁlled in data that would have been challenging to eﬀectively utilize. We did the following to sanitize the data-set:

<!-- b000067 | prose | pages [3] -->
- Remove factors that were not measured at all (represented by the symbol (x),

<!-- b000068 | prose | pages [3] -->
such as HC04 VC03)

<!-- b000069 | furniture | pages [4] -->
Team #1900577

<!-- b000070 | furniture | pages [4] -->
3 of 24

<!-- b000071 | prose | pages [4] -->
- Remove factors that were only measured in certain years, such as computers

<!-- b000072 | prose | pages [4] -->
and internet use (HC01 VC216), as trends across multiple years would be less present and more susceptible to potential outliers. - Remove factors that had incomplete data for all the counties, often represented

<!-- b000073 | prose | pages [4] -->
by the symbol “*****”. Incomplete data for a factor would inhibit the creation of a proper model for drug spread, as there could be hidden trends that are not apparent because of missing data.

<!-- b000074 | prose | pages [4] -->
1.3

<!-- b000075 | heading | pages [4] -->
Existing Models

<!-- b000076 | prose | pages [4] -->
Many comprehensive studies and models of drug spread and impact have been executed in the past. Many of these models focus on the following ideas:

<!-- b000077 | prose | pages [4] -->
• Illicit drug users are broken into 3 groups: light users, susceptible users, and dealers. Each of these groups may enter any of the others through remission, death, or inﬂuence [7]. • Set a threshold quantity to how many new drug abusers an average dealer or light user will generate over their lifetime [12]. • Predict future changes by modeling the previous waves of the opioid epidemic. The ﬁrst wave began in 1999 with prescription opioids, the second started in 2010 with a rise in heroin use, and the third commenced in 2013 with synthetic opioids becoming more common, as can be seen in Figure 1.

<!-- b000078 | caption | pages [4] -->
Figure 1: The three waves of the opioid epidemic [2]

<!-- b000079 | furniture | pages [5] -->
Team #1900577

<!-- b000080 | furniture | pages [5] -->
4 of 24

<!-- b000081 | prose | pages [5] -->
1.4 Our Model

<!-- b000082 | prose | pages [5] -->
For the purpose of determining an eﬀective model to describe the spread of opioid incidents, we characterized the nature of drug-use inﬂuence on each county, both externally and internally. External inﬂuence on a county is determined by the density of drug reports of nearby counties, inversely related by geographic distance. Internally, a county’s inﬂuence comes from a weighted trend analysis of total drug reports based on category.

<!-- b000083 | heading | pages [5] -->
With the addition of socio-economical factors, our model took a multi-variate

<!-- b000084 | prose | pages [5] -->
approach.

<!-- b000085 | prose | pages [5] -->
We determined which factors had the greatest impact on the trends in drug use, and applied a predictive ﬁt to determine how changes in these factors inﬂuence a county. This will allow us to predict how the spread of drug reports will change in the future, creating the opportunity to mitigate the opioid epidemic before it grows more out of control.

<!-- b000086 | prose | pages [5] -->
2

<!-- b000087 | heading | pages [5] -->
Background

<!-- b000088 | prose | pages [5] -->
2.1 The Opioid Epidemic

<!-- b000089 | prose | pages [5] -->
The opioid epidemic is a strange phenomenon of drug addiction where people begin taking prescription opioids for pain management related to a medical issue [5]. By nature, opioids are a highly addictive form of drug, and a user can quickly become dependent due the euphoric feeling they experience while taking them. Users quickly build up a tolerance to this drug, and require more or diﬀerent types for them to continue to be eﬀective [2]. This can cause issues, especially in medical treatment, as a user’s body will no longer respond to certain forms of this drug, causing great pain.

<!-- b000090 | prose | pages [5] -->
2.1.1 Classes of Opioids

<!-- b000091 | prose | pages [5] -->
There are three main classes of opioids:

<!-- b000092 | prose | pages [5] -->
- Opiates (non-synthetic opioids): codeine, morphine, opium, heroin - Semi-synthetic opioids: Hydrocodone, oxycodone, buprenorphine - Synthetic opioids: Fentanyl, butorphanol, methadone, propoxyphene

<!-- b000093 | prose | pages [5] -->
This distinction in type of opioid diﬀerent users will use each category, which can re- sult in varying overall trends. Although heroin is considered an opiate, it is processed from morphine and typically placed in its own category for analysis.

<!-- b000094 | prose | pages [5] -->
Strength of opioids are compared with an Oral Morphine Milligram Equivalent (MME) Conversion Factor. For example, the synthetic opioid tramadol has a 0.1 MME conversion factor, meaning tramadol is 10 times stronger than the equivalent

<!-- b000095 | furniture | pages [6] -->
Team #1900577

<!-- b000096 | furniture | pages [6] -->
5 of 24

<!-- b000097 | prose | pages [6] -->
mass of morphine. The trend is that synthetic opioids are much stronger in their eﬀects than opiates and semi-synthetic opioids.

<!-- b000098 | prose | pages [6] -->
2.1.2 Common Reasons for Substance Abuse

<!-- b000099 | prose | pages [6] -->
There are several factors that researchers generally attribute to increasing the likelihood of addiction [6]:

<!-- b000100 | prose | pages [6] -->
- Mental Health Problems - Career, home, school, or friendship issues - Proximity to other drug users - Past traumatic events

<!-- b000101 | prose | pages [6] -->
3

<!-- b000102 | heading | pages [6] -->
Nomenclature

<!-- b000103 | prose | pages [6] -->
Symbol Deﬁnition Gd,i Gravity of Inﬂuence for drug d and county i Ii Inﬂuence factor of a county i Pi External inﬂuence on county i RE Radius of the Earth r Distance along the earth in kilometers Imax Largest inﬂuence factor in the data set i County identiﬁer m Time derivative of linear best ﬁt in drugs vs time ri,j Distance between counties i and j (m) Si Set containing every county identiﬁer excluding i ∆Drug Predicted change in drug reports ∆φ Diﬀerence of latitudes in radians ∆λ Diﬀerence of longitudes in radians φ1 Radian measure of latitude 1 φ2 Radian measure of latitude 2 µI Median inﬂuence factor

<!-- b000104 | caption | pages [6] -->
Table 1: Variables and functions

<!-- b000105 | prose | pages [6] -->
4

<!-- b000106 | heading | pages [6] -->
Assumptions

<!-- b000107 | prose | pages [6] -->
• Illicit drug use is primarily inﬂuenced by human interaction. Like culture, drug use will spread geographically, more strongly aﬀecting nearby locations than those far away [8].

<!-- b000108 | furniture | pages [7] -->
Team #1900577

<!-- b000109 | furniture | pages [7] -->
6 of 24

<!-- b000110 | prose | pages [7] -->
• The drug report data is representative of overall drug usage in a county or state.

<!-- b000111 | prose | pages [7] -->
• Smaller (rural) populations will be more susceptible to change based outside inﬂuences than larger (urban) populations.

<!-- b000112 | prose | pages [7] -->
• New types of drugs generally appear in waves, which is uncertain to predict based on the drug report data provided. For the purpose of this model, we assume that no new drugs will be introduced to the population.

<!-- b000113 | prose | pages [7] -->
• Without external inﬂuence, an addicted population will continue their current trend of drug use [10].

<!-- b000114 | prose | pages [7] -->
5

<!-- b000115 | heading | pages [7] -->
Model Development

<!-- b000116 | prose | pages [7] -->
In order to quantify and predict the rate of opioid spread between these 5 states, it is necessary to justify the idea of inﬂuence. One of the largest factors that increase the likelihood of drug addiction is proximity to to other drug uses. A county, in some capacity, will be more strongly aﬀected by the drug use of counties nearby than by those that are farther away. To quantify the density of drug use in an area, we deﬁne the inﬂuence factor for a county i:

<!-- b000117 | prose | pages [7] -->
Ii = Number of Drug Reports in County i

<!-- b000118 | prose | pages [7] -->
(1) Area of County i

<!-- b000119 | prose | pages [7] -->
Assuming that the count of drug reports in an area properly represents the actual drug use in that area, we can use this factor as a standardized way to measure drug use in a county. The hypothesis that the spread of the opioid epidemic is correlated to drug reports density rather than strictly the magnitude of these values parallels work previously done in epidemiology [15].

<!-- b000120 | prose | pages [7] -->
5.1 Geographic Gravity

<!-- b000121 | prose | pages [7] -->
The next step is to determine the impact of these inﬂuences on neighboring coun- ties. We begin with the idea of gravity. In physics, the force of gravity on an object is proportional to the product of the mass of each object divided by the distance between the two objects squared:

<!-- b000122 | prose | pages [7] -->
Fg ∝m1m2

<!-- b000123 | prose | pages [7] -->
(2) r2

<!-- b000124 | prose | pages [7] -->
Much like how this quantity is dependent on the inverse square of the distance between to objects, the drug inﬂuence of a county on another decreases with the dis- tance from the county as well. Yanguang Chen’s work in spatial analysis in geography

<!-- b000125 | furniture | pages [8] -->
Team #1900577

<!-- b000126 | furniture | pages [8] -->
7 of 24

<!-- b000127 | prose | pages [8] -->
and social physics upholds this idea, stating that a gravitational model illustrates the interaction between counties, while a exponential decay is more suggestive of local rather than spatial interaction [8].

<!-- b000128 | prose | pages [8] -->
In order for our model to measure distance, we need to utilize external geograph- ical data. We used the FIPS codes provided in the data to match each county with a latitude coordinate, longitude coordinate, and county land area from the U.S. Census Bureau [9]. Although these coordinates point to the center of each county (which may not be completely representative for an unusually-shaped county’s location), it provides us with a method to determine distances between counties. We now use the Haversine formula to determine the distance between any two counties, which accounts for Earth’s curvature to provide a more accurate value than Cartesian esti- mation:

<!-- b000129 | prose | pages [8] -->
r = 2RE arcsin(√a), a = sin2 ∆φ

<!-- b000130 | prose | pages [8] -->
+ cos(φ1) cos(φ2) sin2 ∆λ

<!-- b000131 | prose | pages [8] -->


<!-- b000132 | prose | pages [8] -->


<!-- b000133 | prose | pages [8] -->
2

<!-- b000134 | prose | pages [8] -->
2

<!-- b000135 | prose | pages [8] -->
Equipped with a measure of a county’s drug inﬂuence, along with the distance between each county, we deﬁne the External Inﬂuence Potential on county i as:

<!-- b000136 | prose | pages [8] -->
Ij

<!-- b000137 | prose | pages [8] -->
X

<!-- b000138 | prose | pages [8] -->
Si = {j ∈N | 1 ≤j ≤n; j̸ = i}

<!-- b000139 | prose | pages [8] -->
Pi =

<!-- b000140 | prose | pages [8] -->
,

<!-- b000141 | prose | pages [8] -->
r2

<!-- b000142 | prose | pages [8] -->
i,j

<!-- b000143 | prose | pages [8] -->
jϵSi

<!-- b000144 | prose | pages [8] -->
5.2

<!-- b000145 | heading | pages [8] -->
Model Construction

<!-- b000146 | prose | pages [8] -->
(3)

<!-- b000147 | prose | pages [8] -->
Our opioid spread model focuses on two main ideas: a county’s inﬂuence (both internal and external) along with the current trend of county drug reports with respect to time. Although it would have been beneﬁcial to have more extensive historical data, we utilized the 8 years’ worth of NFLIS to determine the current drug report trend in a county with reasonable accuracy.

<!-- b000148 | prose | pages [8] -->
To ﬁnd this trend, we perform a weighted trend analysis for each county. We apply a linear ﬁt to the total county drug reports with respect to time using a quadratic weight of (year −2009)2 for each point up to the current year. This allows us to take into account a county’s past drug report use, while also placing a much higher signiﬁcance on more recent trends in the data. The time-derivative of this linear ﬁt mi is calculated for every year and county for which there were at least two years’ worth of drug report data.

<!-- b000149 | prose | pages [8] -->
In order to combine inﬂuence factors with current trends in the data, we introduce a normalization coeﬃcient for the inﬂuence values. This coeﬃcient serves to normal- ize these inﬂuence values, along with providing a basis for how much the external inﬂuence potential will aﬀect the change in drug reports for that county. Based on models of social physics, a county with a large inﬂuence will be much aﬀected much

<!-- b000150 | furniture | pages [9] -->
Team #1900577

<!-- b000151 | furniture | pages [9] -->
8 of 24

<!-- b000152 | prose | pages [9] -->
less by outside inﬂuences than a smaller county, thus we base the scale on the ratio between the median and current inﬂuence factor values [8]. This leads to the formula for the change in drug reports for county i in a given year, seen in Equation 4.

<!-- b000153 | prose | pages [9] -->
µI h

<!-- b000154 | prose | pages [9] -->
∆Drugi =

<!-- b000155 | prose | pages [9] -->
IiImax

<!-- b000156 | prose | pages [9] -->
In

<!-- b000157 | prose | pages [9] -->
 X

<!-- b000158 | prose | pages [9] -->
i

<!-- b000159 | prose | pages [9] -->
∗mi

<!-- b000160 | prose | pages [9] -->
+ 1

<!-- b000161 | prose | pages [9] -->
(4)

<!-- b000162 | prose | pages [9] -->
r2

<!-- b000163 | prose | pages [9] -->
n,i

<!-- b000164 | prose | pages [9] -->
nϵSi

<!-- b000165 | prose | pages [9] -->
The ∆Drug is calculated in MATLAB and iterated over for every county for every time step.

<!-- b000166 | prose | pages [9] -->
5.3

<!-- b000167 | heading | pages [9] -->
Extensions of the Model

<!-- b000168 | prose | pages [9] -->
In order to apply this model to speciﬁc drugs or drug categories, rather than solely the total drug growth in a county, we can recalculate the inﬂuence factor values using the drug report count for that speciﬁc drug, rather than the combined total value. The trend values, mi, would also need to be recalculated in a similar way. However, the smaller drug report values when broken down by type of opioid is a signiﬁcant hurdle for our model as it is susceptible to low numbers of counties reporting the drug.

<!-- b000169 | prose | pages [9] -->
5.4

<!-- b000170 | heading | pages [9] -->
Model Validation

<!-- b000171 | prose | pages [9] -->
To test our model, we predict drug report values for a year one time step into the future, and compare it to existing data for that year. For example, we use 2014 data to predict 2015 drug report values and then compare the prediction to the actual 2015 drug reports. A reference line with slope one going through the origin represents the ideal predictor, where every predicted value equals the actual value in the following year.

<!-- b000172 | prose | pages [9] -->
Qualitatively, we can see if the predictions fall close to the line and whether the Quantitatively, we use two measures to judge the predictions trend high or low. quality of the prediction. A least-squares line of best ﬁt for the prediction versus the actual data produces a slope with values close to one. A slope lower than one informs us that our model predictions trend too low and a slope higher than one says our model predictions trend too high. We also calculate the residuals from the points to the reference line of slope one. The sum of residuals allows us to give a magnitude of the closeness of the prediction.

<!-- b000173 | furniture | pages [10] -->
Team #1900577

<!-- b000174 | furniture | pages [10] -->
9 of 24

<!-- b000175 | caption | pages [10] -->
Figure 2: County drug report data for 2015 versus model prediction based oﬀ2014

<!-- b000176 | prose | pages [10] -->
We need to establish a baseline to determine if our predictions were eﬀective. The best choice is to compare the past year to the next year that is being predicted. Our model computes ∆Drugi and adds it to the past year’s drug reports. If our model is to be eﬀective, it would show an improvement over the baseline measure.

<!-- b000177 | prose | pages [10] -->
As illustrated by Figure 2, our model predicts better than the baseline in the year 2015, with best ﬁt slopes of 0.9276 and 0.9262 respectively. The maximum our model could possibly improve the slope is by 1 −0.9262 = 0.0738. Our model improves the slope by 0.0014 which is a 1.9% increase for 2015, and shows an improved slope from the baseline for the years 2013 through 2017 as well. However, the prediction was only marginally better than the baseline. The larger numbers of counties with drug reports in the later years helped our model better predict the directional trend. Likewise, The baseline sum of residuals for the 2015 example is 47408 drug reports. Our model has a reduced sum of residuals at 45539. This is a 3.94% decrease.

<!-- b000178 | furniture | pages [11] -->
Team #1900577

<!-- b000179 | furniture | pages [11] -->
10 of 24

<!-- b000180 | caption | pages [11] -->
Figure 3: Model Prediction of 2017 Drug Reports after 4 Time Steps

<!-- b000181 | prose | pages [11] -->
The next step is to increase the number of time steps our model predicted out from one year.

<!-- b000182 | prose | pages [11] -->
We simulate four years, starting with 2013 drug report data and predicting 2014 through 2017 drug reports, basing each subsequent time step on the previous prediction. This is again compared to the baseline of comparing the 2013 drug reports to the drug reports of the years our model predicted.

<!-- b000183 | prose | pages [11] -->
As expected, the model decreased in accuracy every time step, which can be seen in Figure 3. Regardless, our model beats the baseline at every time-step. By 2017, the predicted 2017 from 2013 data versus the real 2017 data had a linear best ﬁt slope of 0.913 while the baseline (Figure 10) had a slope of 0.786 (16.6% increase). The sum of residuals from this simulation is 82835 drug reports compared to 93656 drug reports for the baseline (11.5% decrease).

<!-- b000184 | prose | pages [11] -->
5.5 Application

<!-- b000185 | prose | pages [11] -->
Based on the characteristics of the data and our model, the epicenters of the opioid epidemic are in counties with cities that consistently have a high inﬂuence factor. The inﬂuence of these counties radiates outwards and inﬂuences the counties nearby. However, the real issue is counties that already have high numbers of drug reports continue to have high numbers of drug reports for years. The U.S. government should also be concerned speciﬁcally with the synthetic opioids like fentanyl and its analogs. The data suggests that synthetic opioids are spreading at a faster rate than the natural opiates. Synthetics have a strength level 400 to 6000 times higher than that morphine, leading to an much higher rate of overdose [3].

<!-- b000186 | furniture | pages [12] -->
Team #1900577

<!-- b000187 | prose | pages [12] -->
5.5.1 Predicting Points of Origin

<!-- b000188 | furniture | pages [12] -->
11 of 24

<!-- b000189 | prose | pages [12] -->
Using an extension of our model, we are able to determine the location of where a speciﬁc drug was most likely to have started. Equation 5 introduces the notion of Gravity of Inﬂuence for any speciﬁc drug d in county i.

<!-- b000190 | prose | pages [12] -->
X

<!-- b000191 | prose | pages [12] -->
Gd,i =

<!-- b000192 | prose | pages [12] -->
nϵSi

<!-- b000193 | prose | pages [12] -->
Ii,dIn,d

<!-- b000194 | prose | pages [12] -->
(5)

<!-- b000195 | prose | pages [12] -->
r2

<!-- b000196 | prose | pages [12] -->
n,i

<!-- b000197 | prose | pages [12] -->
For any drug, the county with the maximum Gd value in the initial outbreak year has the highest likelihood to be its origin of use. As an example, we will look at the upsurge of 3-Methylfentanyl, which ﬁrst appears in the NFLIS data in 2016. Erie County, Ohio has the highest Gd value in 2016 for 3-Methylfentanyl, indicating a high probability that this is where the drug started. Looking at the spread of 3- Methylfentanyl drug reports in Figure 4 supports this hypothesis, as the region of northern Ohio (the location of Erie county) has the most signiﬁcant concentration of this drug in the year of outbreak.

<!-- b000198 | caption | pages [12] -->
Figure 4: 2016 (Left) and 2017 (Right) county drug reports for 3-Methylfentanyl.

<!-- b000199 | prose | pages [12] -->
Map data from GADM [1]

<!-- b000200 | prose | pages [12] -->
5.5.2 Drug Identiﬁcation Threshold

<!-- b000201 | prose | pages [12] -->
For this model to be of use to help with the opioid epidemic, we determine a threshold which signiﬁes a point of concern for the government. We know that there already exist signiﬁcant issues with opioid overdose in high drug use counties. So, we chose our threshold to be the 90th percentile of inﬂuence values from 2017. By basing our threshold on inﬂuence values, this ensures that each county has their own individualized drug report threshold scaled by size.

<!-- b000202 | prose | pages [12] -->
Using our model, we simulated the spread of total drug use through the year 2025. In 2017, where we began this simulation, there were already 11 counties above

<!-- b000203 | furniture | pages [13] -->
Team #1900577

<!-- b000204 | furniture | pages [13] -->
12 of 24

<!-- b000205 | prose | pages [13] -->
the threshold (Lake and Cuyajoga County, OH; Philadelphia, Delaware, and Beaver County, PA; Franklin, Montgomery, and Hamilton County, OH; Arlington, Roanoke, Fairfax City County, VA). Six more counties rose above the threshold when simulat- ing out to 2025. Unfortunately, none of the counties which were already above the threshold in 2017 sank below it again. However, this is understandable, as the opioid epidemic is modeled to expected to continue spreading without external intervention.

<!-- b000206 | prose | pages [13] -->
Year Counties 2018 Fairfax, VA and Kenton, KY 2020 Henrico, VA 2021 Stark, OH 2023 Summit, OH 2024 Lorain, OH

<!-- b000207 | caption | pages [13] -->
Table 2: Counties rising above threshold in simulation from 2018-2025

<!-- b000208 | prose | pages [13] -->
5.6 Important Socio-Economic Inﬂuences

<!-- b000209 | prose | pages [13] -->
Outside of inﬂuence factor, there are other components that may lead to the spread of drug use. As part of the included data, we were given U.S. Census data for a wide range of socio-economic factors. In order to quantify which factors best correlated with trends in drug use, we found the R2 values of the linear ﬁt for the diﬀerence between the total county drug reports and the value of each factor with respect to time. Then, we calculated the median value of these R2 values for each speciﬁc factor across all counties.

<!-- b000210 | prose | pages [13] -->
Using these median values as a baseline, we can examine which factors have the closest trends to total county drug reports. By plotting the distribution of the corre- lation values for a each factor, two main trends emerge, which are depicted in Figure 5. For factors with a high median value, the distribution is heavily skewed towards one end of the scale of possible R2 values (-1 or 1), indicating there is a high num- ber of counties with which these factors could model the trend in drug use. For low median values, the distribution is nearly uniform, indicating that there is little corre- lation between this factor and the trend in drug use, and that it would not be a good candidate for the model.

<!-- b000211 | furniture | pages [14] -->
Team #1900577

<!-- b000212 | prose | pages [14] -->
Low median R2 value

<!-- b000213 | furniture | pages [14] -->
13 of 24

<!-- b000214 | prose | pages [14] -->
High median R2 value

<!-- b000215 | caption | pages [14] -->
Figure 5: Trends in R2

<!-- b000216 | caption | pages [14] -->
Table 3 indicates the factors with the highest median R2 values located in the

<!-- b000217 | prose | pages [14] -->
cleaned data along with their Census metadata codes.

<!-- b000218 | prose | pages [14] -->
Factor Population of > 1 year residency Civilian Population with Veteran Status Estimate of Associate’s Degrees Median R2 Value Metadata Code HC01 VC117 .861 HC01 VC98 .790 HC01 VC89 .744

<!-- b000219 | caption | pages [14] -->
Table 3: Factors and their median R2 values

<!-- b000220 | prose | pages [14] -->
5.7 Adjustments

<!-- b000221 | prose | pages [14] -->
To take into account these correlated socio-economic factors into our model, we turn to a multivariate approach to ﬁnd the current trend of drug reports with respect to time. Instead of using a weighted linear regression to ﬁnd the value of mi, we perform a polynomial regression ﬁt on the total drug reports with respect to time and our most correlated socio-economic factors. Equation 6 indicates the form of this equation ﬁt for county i with socio-economic factors x1 through xn in year y.

<!-- b000222 | prose | pages [14] -->
Total Drug Reportsi = m1y + m2x1 + · · · + mn+1xn (6)

<!-- b000223 | furniture | pages [15] -->
Team #1900577

<!-- b000224 | furniture | pages [15] -->
14 of 24

<!-- b000225 | prose | pages [15] -->
From this, we obtain the value mi,y for county i in year y by inputting the values for the change in each of the factors with respect to time at year y.

<!-- b000226 | prose | pages [15] -->
dx1

<!-- b000227 | prose | pages [15] -->
dxn

<!-- b000228 | prose | pages [15] -->
dt (y) + · · · + mn+1

<!-- b000229 | prose | pages [15] -->
mi,y = m1 + m2

<!-- b000230 | prose | pages [15] -->
dt (y) (7)

<!-- b000231 | prose | pages [15] -->
The overall equation for the opioid spread model remains the same, with the new factor mi,y replacing the previous trend values. After trying diﬀerent combinations of implementations the factors in Table 3 into our model, we found the model that best ﬁt the data was that using just the factor with the greatest median R2 value (HC01 VC117). This makes sense as it was the factor that was, on average, best representative of the trends in drug reports for each county.

<!-- b000232 | caption | pages [15] -->
Figure 6: County drug report data for 2015 versus non-adjusted model prediction

<!-- b000233 | prose | pages [15] -->
based oﬀ2014

<!-- b000234 | prose | pages [15] -->
With the adjusted model, as shown in Figure 7, we examine how the addition of the socio-economic factor inﬂuenced our predictions. After using the adjusted model to predict 2015 drug report spread based oﬀof 2014 data, the slope of the best-ﬁt line stayed only slightly increased (to .9288 from .9276). But, the sum of the residuals with the adjusted model was 41631, which is a 12.2% decrease from the 47408 drug reports in the baseline, and a 3.9% decrease from the 45539 drug reports in the original model (Figure 6).

<!-- b000235 | furniture | pages [16] -->
Team #1900577

<!-- b000236 | furniture | pages [16] -->
15 of 24

<!-- b000237 | caption | pages [16] -->
Figure 7: County drug report data for 2015 versus adjusted model prediction based

<!-- b000238 | prose | pages [16] -->
oﬀ2014

<!-- b000239 | prose | pages [16] -->
6

<!-- b000240 | heading | pages [16] -->
Results

<!-- b000241 | prose | pages [16] -->
6.1 Part I: Origin Prediction and Threshold

<!-- b000242 | prose | pages [16] -->
The model can predict the point of origin of a speciﬁc drug based on each county’s gravity of inﬂuence (Gd). For example, the origin of 3-Methylfentanyl was found to be Erie County, Ohio in 2016. This was determined by ﬁnding the maximum Gd out of all the counties for this speciﬁc drug.

<!-- b000243 | prose | pages [16] -->
The drug identiﬁcation threshold level that we determined was the 90th per- centile of inﬂuence values for counties in 2017. There are already 11 counties above this threshold, and the model predicts that cross this threshold from 2018 to 2025. Unfortunately, none of the counties currently above the threshold are predicted to go below it without changes in governmental policy or actions against opioid addiction.

<!-- b000244 | prose | pages [16] -->
6.2 Part II: Socio-Economic Adjustments

<!-- b000245 | prose | pages [16] -->
We found that population of users with residency of greater than 1 year, civilian population with veteran status, and number of Associate’s degrees were the socio- economic factors that most closely resembled the drug report data. By conditioning

<!-- b000246 | furniture | pages [17] -->
Team #1900577

<!-- b000247 | furniture | pages [17] -->
16 of 24

<!-- b000248 | prose | pages [17] -->
our model based on the most inﬂuential factor, the model prediction residuals de- creased by 12.2% compared to the unconditioned model.

<!-- b000249 | prose | pages [17] -->
6.3 Part III: Strategy for Countering the Crisis

<!-- b000250 | prose | pages [17] -->
In the past several years, there have been numerous eﬀorts to curb the opioid epidemic.

<!-- b000251 | prose | pages [17] -->
Simply arresting drug users does not help the problem, as this simply makes recovery more diﬃcult for these individuals and it is more challenging to ﬁnd a job with a criminal record. A data-driven solution to this problem is necessary to see a signiﬁcant change.

<!-- b000252 | prose | pages [17] -->
From part I, we see that counties with large inﬂuence values are not easily af- fected, but counties with low inﬂuence values can grow exponentially under the right conditions. Early detection of the emergence of new drugs up would be an eﬀective strategy for countering crisis with the correct approach.

<!-- b000253 | prose | pages [17] -->
From part II, we notice that there are several socio-economic factors that seem to be strongly associated with trends in drug use. One of these factors is the number of Associates Degrees. This may be due to there being less opportunities, challenge ﬁnding jobs, or other struggles that are not as present with higher-level college degrees. A solution to this could be to implement a program to incentivize Associate graduates to pursue a 4-year degree upon graduation. By allowing the graduated to continue on in their education, they may be able to get more opportunities than they otherwise would with their associates degrees [14]. Another strongly associated factor was the population of veterans in a county. This could be because veterans have an increased chance of having some form of past trauma, which is a known cause of drug addiction [6]. A possible solution to this would be to oﬀer an addiction recovery course could oﬀer a low cost recovery alternative or supplement, and veterans could be eligible to participate in this course at no or reduced cost.

<!-- b000254 | prose | pages [17] -->
One problem with the current opioid crisis is that counties who already use the most drugs will continue to use the most over time. In order to mitigate this, the government should must changes into the counties with the most annual drug reports. By implementing programs that are self elective, like recovery and educational centers, populations will have access to help they need. And, these programs have already been shown to be eﬀective. The Chinese Needle Exchange Program and Methadone Maintenance Treatment centers saw a signiﬁcant reduction in users after the program had been implemented [11]. These programs were so eﬀective in the private sector in China, the government decided to open four of their own in 2004, to which they expanded to 558 by 2008. Implementing centers like these in the United States would likely follow a similar trajectory of improvement.

<!-- b000255 | furniture | pages [18] -->
Team #1900577

<!-- b000256 | furniture | pages [18] -->
17 of 24

<!-- b000257 | caption | pages [18] -->
Figure 8: Eﬀect of drug recovery centers if they were implemented in 2015

<!-- b000258 | caption | pages [18] -->
Figure 8 shows the possible outcome of implementing drug recovery centers in our

<!-- b000259 | prose | pages [18] -->
modeled counties. We estimated the eﬀect on the trend slope to predict the eﬀects of our policy change. With this adjustment, we can see that the overall change in drug reports is predicted to decrease, implying an overall decrease in addiction and abuse.

<!-- b000260 | prose | pages [18] -->
7

<!-- b000261 | heading | pages [18] -->
Sensitivity Analysis

<!-- b000262 | prose | pages [18] -->
7.1 Variation of the Scale of Drug Reports

<!-- b000263 | prose | pages [18] -->
We tested our model’s sensitivity to high mi values, which simulates a quickly increasing epidemic. We doubled the 2015 drug report values, keeping the 2014 drug report values the same and recalculating the linear ﬁts and mi values. Our model had an excellent linear regression slope of 1.01. The residual was only slightly higher at 60186 drug reports. This low sensitivity is likely due to the quadratic weighted best-ﬁt line, which puts a higher weight on changes closer to the present.

<!-- b000264 | prose | pages [18] -->
We then doubled both the 2014 and 2015 drug reports and recalculated mi. This models high drug report levels but increasing at approximately the same rate as the

<!-- b000265 | furniture | pages [19] -->
Team #1900577

<!-- b000266 | furniture | pages [19] -->
18 of 24

<!-- b000267 | prose | pages [19] -->
original data. The residual was higher at 120190. The prediction trends lower than the expected 2015 data with a slope of 0.890. This shows that our model generally robust to changes in the scale of drug reports.

<!-- b000268 | prose | pages [19] -->
7.2 Variation of Socio-economic Factors

<!-- b000269 | prose | pages [19] -->
We doubled the value census data for residents who have lived in the same place more than a year (the most representative socio-economic factor). The new 2015 drug report prediction had a linear regression slope of 0.971 but had a much larger residual of 106250 drug reports. Our model is highly sensitive to dramatic changes in socio-economic factors.

<!-- b000270 | prose | pages [19] -->
8

<!-- b000271 | heading | pages [19] -->
Conclusion

<!-- b000272 | prose | pages [19] -->
The use of opioids continues to spread across the country as a lucrative and alluring product for both the poor and the wealthy. Despite the best eﬀorts of the government, this spread is challenging to contain and restrict. As many opioids are misused prescription medications, they are available everywhere. Once in the illegal possession of a user or dealer, however, they are far more restricted in mobility.

<!-- b000273 | prose | pages [19] -->
Instead of being able to travel internationally to any pharmacy funded by multi- billion dollar conglomerates, the movement of opioids is limited to a sphere of inﬂu- ence. Like culture, drugs are more likely to spread nearby than far away. Once a drug has been spread, it is hard to stop, as its users become addicted and are willing to pay more to get their ﬁx. This has been a problem for decades, and it will only grow worse as time progresses. In order to reduce the mortality and addiction rates, the government must have a greater impact in helping the people that have become addicted, whilst dissuading others from starting.

<!-- b000274 | prose | pages [19] -->
As states and counties try to regulate and rehabilitate opioid users, they will need to keep adjusting their tactics to the people. Socio-economic factors such as veteran status and length of residency can help predict the trend drug incidents. By implementing programs that are both proactive and reformative, there is a way by which citizens can recover from addiction. Placing facilities and education in the hands of the users helps them to choose self improvement over incarceration. New drugs are more harmful and powerful then ever and it is up to the people and the government to change the nature of drug abuse.

<!-- b000275 | prose | pages [19] -->
8.1

<!-- b000276 | heading | pages [19] -->
Model Strengths

<!-- b000277 | heading | pages [19] -->
• Our model quantiﬁes the nature of drug-use inﬂuence through gravita-

<!-- b000278 | prose | pages [19] -->
tional geography, and illustrates how it aﬀects a county both internally and

<!-- b000279 | furniture | pages [20] -->
Team #1900577

<!-- b000280 | furniture | pages [20] -->
19 of 24

<!-- b000281 | prose | pages [20] -->
externally.

<!-- b000282 | prose | pages [20] -->
• By using a weighted trend analysis of total drug reports, we account for his- torical data while placing a heavier inﬂuence on recent developments.

<!-- b000283 | prose | pages [20] -->
• A multivariate approach to the model characterizes the inﬂuence of related socio-economic factors on the spread of drug use.

<!-- b000284 | prose | pages [20] -->
• The model can calculate the trend in drug use for every drug and drug type for any county given initial data, and is easily veriﬁable against a baseline.

<!-- b000285 | prose | pages [20] -->
• The model is easily expandable to other states and counties. Having drug report data for the neighboring states of our ﬁve states would increase model accuracy.

<!-- b000286 | prose | pages [20] -->
8.2

<!-- b000287 | heading | pages [20] -->
Model Weaknesses and Limiting Assumptions

<!-- b000288 | prose | pages [20] -->
• Since the model is based on only the NFLIS data for 5 states in the Northeastern United States, some county inﬂuence values are not being properly calculated, speciﬁcally those which are close to borders with other states. As such, the model will underestimate the eﬀect that outside inﬂuence will have on these counties, and the model will likely underestimate the trend in drug use. This can be improved by expanding the intial data to contain more counties and states.

<!-- b000289 | prose | pages [20] -->
• The U.S. Census data that was provided only had a subset of possible socio- economic factors. There are other factors not included in this data that are often more indicative to the spread of drug, such as average household income or homeless population. As such, our model was not able to account for changes in these factors.

<!-- b000290 | prose | pages [20] -->
• The model needs a substantial amount of data to properly predict the trend in drug use. As such, trends in drug use in counties with less or incomplete data were not able to be eﬀectively represented.

<!-- b000291 | prose | pages [20] -->
• Since the data provided was on a yearly basis, the model was limited by discrete time steps and lacks a more continuous evaluation for improved accuracy.

<!-- b000292 | prose | pages [20] -->
• Waves of new drugs are hard to predict with the dataset provided, so the model does not account for the introduction of new types of drugs into these counties. This will cause our model to underestimate level of upwards trend in drug use.

<!-- b000293 | furniture | pages [21] -->
Team #1900577

<!-- b000294 | furniture | pages [21] -->
20 of 24

<!-- b000295 | prose | pages [21] -->
9

<!-- b000296 | heading | pages [21] -->
Memo to the DEA/NFLIS Chief Administrator

<!-- b000297 | prose | pages [21] -->
Date: January 29, 2019 To: Chief Administrator, DEA/NFLIS Database From: MCM Team #1900577

<!-- b000298 | heading | pages [21] -->
Subject: Opioid Crisis Insights and Recommendations

<!-- b000299 | prose | pages [21] -->
Chief Administrator,

<!-- b000300 | prose | pages [21] -->
In an eﬀort to address the opioid crisis, we have modeled how it has spread over time. From the heroin crisis in 2010 in Philadelphia county to the recent outbreak of the 3-Methylfentanyl in Erie county in 2016, drugs continue to be a nationwide issue every year. One of the largest oﬀenders in the origin of new drugs is Ohio. Due to this, Ohio also has one of the highest mortality rates in the United States. However, as we continue to model ways to ﬁnd where drugs start, it becomes easier to react to them.

<!-- b000301 | prose | pages [21] -->
It is a grave concern if a county’s inﬂuence factor rises above the 90th percentile (as measured in 2017). Simulating the spread through 2025, we identiﬁed 6 counties that will pass abover the threshold. Above this threshold, it will be very diﬃcult to reduce the drug reports as it will inﬂuence the counties around it and stay above the threshold.

<!-- b000302 | prose | pages [21] -->
There is still hope, though, as we identiﬁed several socio-economic factors that correlate with the drug reports. People who have lived in a county for greater than 1 year, the populations of veterans, and people with associates degrees are all groups whose trends are heavily associated with those of drug reports. Creating programs to help residents be positively involved in the community, providing veterans with job opporitunities while taking care of their mental health, and encouraging the county’s residents pursue higher education are all ways to help ﬁght the opioid epidemic.

<!-- b000303 | prose | pages [21] -->
With new technology comes an ease of communication, and dealers can be further disassociated with buyers, increasing sales. Synthetic opioids are highly alluring and are 400 to 6000 times stronger than their natural counterparts like morphine. With increase in strength comes an increase in mortality. Another problem with opioids, is that many of the people who are misusing them are acquiring them from their friends or relatives. This means that regardless of geography, drugs will always be accessible to those who choose to take them. It is a diﬀerent form of war on drugs.

<!-- b000304 | prose | pages [21] -->
Currently, drug sentencing varies greatly. Some convictions are are low as a $500 ﬁne, while others are as much as 15 years in prison with a $25000 dollar ﬁne for the ﬁrst oﬀense. Although very harsh punishments do cut back on drug use, they also cost the state a signiﬁcant amount in incarceration costs for the convicted. Other states have begun implementing a policy by which the county oﬀers a course to ﬁrst, and

<!-- b000305 | furniture | pages [22] -->
Team #1900577

<!-- b000306 | furniture | pages [22] -->
21 of 24

<!-- b000307 | prose | pages [22] -->
sometimes second oﬀenders, which allows them to try to recover from their addiction on their own or as a part of their sentence. Education and recovery saves the state money for oﬀenders, and oﬀers them an opportunity to change their habits. Programs like this have already been shown to be eﬀective in other counties across the United States and the rest of the world. Insights:

<!-- b000308 | prose | pages [22] -->
• Counties where drugs begin are the often the same as where they are the most harmful.

<!-- b000309 | prose | pages [22] -->
• Counties will always have drugs available to them and so it is an not expectation that one would be able to eradicate them all.

<!-- b000310 | heading | pages [22] -->
Results:

<!-- b000311 | prose | pages [22] -->
• The count of veterans, long term residents, and junior college graduates have the highest association to the trend in drug incidents per year

<!-- b000312 | prose | pages [22] -->
• Pennsylvania has the highest mortality rate from drugs

<!-- b000313 | prose | pages [22] -->
• Erie county has been a recent hot spot for new drugs, such as 3-Methylfentanyl

<!-- b000314 | heading | pages [22] -->
Recommendations:

<!-- b000315 | prose | pages [22] -->
• Begin programs to help recovering addicts, similar to the Chinese Clean Needle exchange.

<!-- b000316 | prose | pages [22] -->
• Make drug eﬀects and use education available to the population at as little cost as possible.

<!-- b000317 | prose | pages [22] -->
• Provide drug users opportunities to rehabilitate over state funded incarceration.

<!-- b000318 | prose | pages [22] -->
Best,

<!-- b000319 | prose | pages [22] -->
MCM Team #1900577

<!-- b000320 | furniture | pages [23] -->
Team #1900577

<!-- b000321 | furniture | pages [23] -->
22 of 24

<!-- b000322 | heading | pages [23] -->
References

<!-- b000323 | references | pages [23] -->
[1] GADM. https://gadm.org/.

<!-- b000324 | references | pages [23] -->
[2] Data Resources | Drug Overdose | CDC Injury Center, November 2018. https:

<!-- b000325 | references | pages [23] -->
//www.cdc.gov/drugoverdose/resources/data.html.

<!-- b000326 | references | pages [23] -->
[3] Drug Overdose Deaths | Drug Overdose | CDC Injury Center, December 2018.

<!-- b000327 | references | pages [23] -->
https://www.cdc.gov/drugoverdose/data/statedeaths.html.

<!-- b000328 | references | pages [23] -->
[4] Understanding the Epidemic | Drug Overdose | CDC Injury Center, December

<!-- b000329 | references | pages [23] -->
2018. https://www.cdc.gov/drugoverdose/epidemic/index.html.

<!-- b000330 | references | pages [23] -->
[5] National Institute on Drug Abuse.

<!-- b000331 | references | pages [23] -->
misuse?

<!-- b000332 | references | pages [23] -->
What is the scope of prescription drug

<!-- b000333 | references | pages [23] -->
https://www.drugabuse.gov/publications/research-reports/

<!-- b000334 | references | pages [23] -->
misuse-prescription-drugs/what-scope-prescription-drug-misuse.

<!-- b000335 | references | pages [23] -->
[6] National Institute on Drug Abuse.

<!-- b000336 | references | pages [23] -->
sion Points, February 2017.

<!-- b000337 | references | pages [23] -->
The Science of Drug Use:

<!-- b000338 | references | pages [23] -->
Discus-

<!-- b000339 | references | pages [23] -->
https://www.drugabuse.gov/related-topics/

<!-- b000340 | references | pages [23] -->
criminal-justice/science-drug-use-discussion-points.

<!-- b000341 | references | pages [23] -->
[7] Afsaneh Bakhtiari and Alexander Rutherford.

<!-- b000342 | references | pages [23] -->
Mathematical Modelling to

<!-- b000343 | references | pages [23] -->
Evaluate Measures and Control the Spread of Illicit Drug Use.

<!-- b000344 | references | pages [23] -->
In Evange-

<!-- b000345 | references | pages [23] -->
los Kranakis, editor, Advances in Network Analysis and its Applications, vol-

<!-- b000346 | references | pages [23] -->
ume 18, pages 257–268. Springer Berlin Heidelberg, Berlin, Heidelberg, 2012.

<!-- b000347 | references | pages [23] -->
http://link.springer.com/10.1007/978-3-642-30904-5_11.

<!-- b000348 | references | pages [23] -->
distance-decay

<!-- b000349 | references | pages [23] -->
[8] Yanguang

<!-- b000350 | references | pages [23] -->
Chen.

<!-- b000351 | references | pages [23] -->
The

<!-- b000352 | references | pages [23] -->
function

<!-- b000353 | references | pages [23] -->
of

<!-- b000354 | references | pages [23] -->
geographical

<!-- b000355 | references | pages [23] -->
gravity

<!-- b000356 | references | pages [23] -->
Power law or exponential law?

<!-- b000357 | references | pages [23] -->
model:

<!-- b000358 | references | pages [23] -->
77:174–189, August 2015.

<!-- b000359 | references | pages [23] -->
Chaos,

<!-- b000360 | references | pages [23] -->
Solitons & Fractals,

<!-- b000361 | references | pages [23] -->
https://linkinghub.elsevier.com/retrieve/

<!-- b000362 | references | pages [23] -->
pii/S0960077915001587.

<!-- b000363 | references | pages [23] -->
[9] US Census Bureau Geography. 2017 U.S. Gazetteer Files Record Layouts. https:

<!-- b000364 | references | pages [23] -->
//www.census.gov/geo/maps-data/data/gazetteer2017.html.

<!-- b000365 | references | pages [23] -->
[10] William M. Holmes. Using Propensity Scores in Quasi-Experimental Designs.

<!-- b000366 | references | pages [23] -->
SAGE Publications, Pg. 231, June 2013. Google-Books-ID: 7Z92AwAAQBAJ.

<!-- b000367 | references | pages [23] -->
[11] Jianhua Li, Toan H Ha, Cunmin Zhang, and Hongjie Liu. The Chinese govern-

<!-- b000368 | references | pages [23] -->
ment’s response to drug use and HIV/AIDS: A review of policies and programs.

<!-- b000369 | references | pages [23] -->
Harm Reduction Journal, 7:4, March 2010. https://www.ncbi.nlm.nih.gov/

<!-- b000370 | references | pages [23] -->
pmc/articles/PMC2847555/.

<!-- b000371 | furniture | pages [24] -->
Team #1900577

<!-- b000372 | furniture | pages [24] -->
23 of 24

<!-- b000373 | references | pages [24] -->
[12] Steady Mushayabasa and Gift Tapedzesa. Modeling Illicit Drug Use Dynam-

<!-- b000374 | references | pages [24] -->
ics and Its Optimal Control Analysis. Computational and Mathematical Meth-

<!-- b000375 | references | pages [24] -->
ods in Medicine, 2015, 2015. https://www.ncbi.nlm.nih.gov/pmc/articles/

<!-- b000376 | references | pages [24] -->
PMC4707024/.

<!-- b000377 | references | pages [24] -->
[13] Institute of Medicine (US) Committee on Opportunities in Drug Abuse Research.

<!-- b000378 | references | pages [24] -->
Drug Abuse Research in Historical Perspective. National Academies Press (US),

<!-- b000379 | references | pages [24] -->
1996. https://www.ncbi.nlm.nih.gov/books/NBK232965/.

<!-- b000380 | references | pages [24] -->
[14] Marisa A. Scala.

<!-- b000381 | references | pages [24] -->
Going Back to School: Participation Motives and Experi-

<!-- b000382 | references | pages [24] -->
ences of Older Adults in an Undergraduate Classroom. Educational Gerontology,

<!-- b000383 | references | pages [24] -->
22(8):747–773, January 1996. https://doi.org/10.1080/0360127960220804.

<!-- b000384 | references | pages [24] -->
[15] Patrick M. Tarwater and Clyde F. Martin. Eﬀects of population density on the

<!-- b000385 | references | pages [24] -->
spread of disease. Complexity, 6(6):29–36, July 2001. http://doi.wiley.com/

<!-- b000386 | references | pages [24] -->
10.1002/cplx.10003.

<!-- b000387 | furniture | pages [25] -->
Team #1900577

<!-- b000388 | furniture | pages [25] -->
24 of 24

<!-- b000389 | heading | pages [25] -->
Appendix

<!-- b000390 | caption | pages [25] -->
Figure 9: Baseline Test using 2014 data as the predictor for 2015

<!-- b000391 | caption | pages [25] -->
Figure 10: Baseline of 2013 Drug Reports after 4 Time Steps
