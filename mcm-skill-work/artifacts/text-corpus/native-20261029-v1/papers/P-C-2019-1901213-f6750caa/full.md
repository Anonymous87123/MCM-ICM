# P-C-2019-1901213-f6750caa

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->


<!-- b000002 | furniture | pages [1] -->


<!-- b000003 | furniture | pages [1] -->


<!-- b000004 | furniture | pages [1] -->


<!-- b000005 | furniture | pages [1] -->


<!-- b000006 | furniture | pages [1] -->


<!-- b000007 | furniture | pages [1] -->
Team Control Number

<!-- b000008 | prose | pages [1] -->
For office use only

<!-- b000009 | prose | pages [1] -->
For office use only

<!-- b000010 | prose | pages [1] -->
1901213

<!-- b000011 | prose | pages [1] -->
T1 ________________

<!-- b000012 | furniture | pages [1] -->


<!-- b000013 | prose | pages [1] -->
T2 ________________

<!-- b000014 | prose | pages [1] -->
F1 ________________ F2 ________________

<!-- b000015 | prose | pages [1] -->
Problem Chosen

<!-- b000016 | prose | pages [1] -->
T3 ________________

<!-- b000017 | prose | pages [1] -->
F3 ________________

<!-- b000018 | title | pages [1] -->
C

<!-- b000019 | prose | pages [1] -->
T4 ________________

<!-- b000020 | furniture | pages [1] -->


<!-- b000021 | prose | pages [1] -->
F4 ________________

<!-- b000022 | furniture | pages [1] -->


<!-- b000023 | prose | pages [1] -->
2019 MCM/ICM

<!-- b000024 | heading | pages [1] -->
Summary Sheet

<!-- b000025 | title | pages [1] -->
Take Me Home:

<!-- b000026 | title | pages [1] -->
Preventing Journeys Down the Opioid Addiction Road

<!-- b000027 | prose | pages [1] -->
In recent years, overdose has been the leading cause of accidental deaths in the United

<!-- b000028 | furniture | pages [1] -->


<!-- b000029 | prose | pages [1] -->
States, and prescription opioids and heroin are among the heaviest offenders in that category. While many people need opioids to manage their chronic and severe pain, a common consequence of these treatments are abuse, addiction, and escalation to worse substances. A variety of strategies exist to combat the spread of drugs, like education, rehabilitation, and law enforcement. However, a more targeted strategy is necessary for opioids, given their new ubiquity in American society.

<!-- b000030 | prose | pages [1] -->
We have developed a model that robustly and accurately predicts the spread of opioids within and between the states of Ohio, Pennsylvania, Virginia, West Virginia, and Kentucky. In doing so, we:

<!-- b000031 | prose | pages [1] -->
● Visualized the movement and spread of opioids within the region between 2010 and 2016 by treating opioid addiction as a disease that spreads deterministically between neighbors and assuming that the spread of it can be modeled in a Markovian fashion. This will allow us to find a transition matrix that tells the influence of each county on one another. We also factored into this matrix the distances between counties. ● Next, we modeled the effect of socioeconomic factors throughout the data set, and correlated these changes with how opioid use in that county grows or shrinks over time. ● We then combined the models in two ways - in a linear and parallel fashion. We used this to estimate epicenters from where the drug problem emanates. ● Finally, we ran multiple simulations and predicted the drug problem well into the future to develop a number of strategies to tackle the epidemic from different perspectives, selecting from the variables that contribute most heavily to the spread of opioids. Our model treats illicit opioid use as a disease that is spread more frequently when more people in a given area have it. This allowed us to design it such that it can be generalized to a larger region in the future. By visualizing this spread, we were able to witness predicted opioid use spread through and along major roads over longer distances than simple adjacency would predict. The counties connected in this way include both the epicenters and the vulnerable ones.

<!-- b000032 | prose | pages [1] -->
To evaluate our external model, we gave it the first two years of drug report data from all the counties, and then allowed it to propagate through the year 2016. Our predictions have an error on the order of 10-5 drug reports per capita. When evaluating our internal model, we realized that while socioeconomic factors are highly correlated, they could not accurately predict opioid abuse.

<!-- b000033 | prose | pages [1] -->
After this, we modified various initial conditions in our model such as socioeconomic factors and influence of the epicenters. By doing so, we were able to find effective and highly targeted strategies which will drastically reduce and reverse the prevalence of opioids in the region provided.

<!-- b000034 | furniture | pages [2] -->
Team #1901213

<!-- b000035 | furniture | pages [2] -->
Page 1 of 29

<!-- b000036 | heading | pages [2] -->
Contents

<!-- b000037 | contents | pages [2] -->
1

<!-- b000038 | heading | pages [2] -->
Introduction

<!-- b000039 | prose | pages [2] -->
2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 Problem Summary 2 Our Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2

<!-- b000040 | prose | pages [2] -->
2

<!-- b000041 | heading | pages [2] -->
Background

<!-- b000042 | prose | pages [2] -->
3 Data

<!-- b000043 | prose | pages [2] -->
3

<!-- b000044 | prose | pages [2] -->
3

<!-- b000045 | prose | pages [2] -->
4 Given data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 4 Additional data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2

<!-- b000046 | prose | pages [2] -->
4

<!-- b000047 | heading | pages [2] -->
Assumptions

<!-- b000048 | prose | pages [2] -->
4

<!-- b000049 | prose | pages [2] -->
5 As a disease . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 5 . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2 The Markovian assumption 5 Proximity to neighboring counties . . . . . . . . . . . . . . . . . . . . . . . . 4.3 5 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.4 All opioids are the same 6 Data homogeneity across counties . . . . . . . . . . . . . . . . . . . . . . . . 4.5

<!-- b000050 | prose | pages [2] -->
5

<!-- b000051 | heading | pages [2] -->
Model

<!-- b000052 | prose | pages [2] -->
6

<!-- b000053 | prose | pages [2] -->
6 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 Deﬁning health 7 Modeling external factors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2 7 Understanding xt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2.1 7 Understanding A . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2.2 8 Understanding Q . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2.3 8 Estimating Q . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2.4 8 Modeling internal factors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.3 9 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.3.1 Linear regression 9 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.3.2 Logistic regression 9 Combining the two models . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.4 9 . . . . . . . . . . . . . . . . . . . . . . . . . . 5.4.1 A convex combination 10 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.4.2 A two stage model

<!-- b000054 | prose | pages [2] -->
6

<!-- b000055 | heading | pages [2] -->
Solutions

<!-- b000056 | prose | pages [2] -->
10

<!-- b000057 | prose | pages [2] -->
10 Estimating δ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 10 Estimating the inﬂuence of external factors . . . . . . . . . . . . . . . . . . . 6.2 12 Estimating the inﬂuence of internal factors . . . . . . . . . . . . . . . . . . . 6.3 12 Building a convex combination of models . . . . . . . . . . . . . . . . . . . . 6.4 13 . . . . . . . . . . . . . . . . . . . . . . . . . . 6.5 Building the two stage model 13 . . . . . . . . . . . . . . . . . . . . . . . . . . 6.6 Epicenters and vulnerabilities 13 Identifying epicenters . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.6.1 14 Identifying vulnerable counties . . . . . . . . . . . . . . . . . . . . . . 6.6.2 6.6.3 Understanding these counties

<!-- b000058 | prose | pages [2] -->
7

<!-- b000059 | heading | pages [2] -->
Sensitivity Analysis

<!-- b000060 | prose | pages [2] -->
15 . . . . . . . . . . . . . . . . . . . . . .

<!-- b000061 | prose | pages [2] -->
15

<!-- b000062 | prose | pages [2] -->
16

<!-- b000063 | furniture | pages [3] -->
Team #1901213

<!-- b000064 | furniture | pages [3] -->
Page 2 of 29

<!-- b000065 | prose | pages [3] -->
Tweaking the external factors . . . . . . . . . . . . . . . . . . . . . . . . . . 7.1 16 . . . . . . . . . . . . . . . . . . . . . . . . . . 7.2 Tweaking the internal factors

<!-- b000066 | prose | pages [3] -->
8

<!-- b000067 | heading | pages [3] -->
Strengths and Weaknesses

<!-- b000068 | prose | pages [3] -->
16

<!-- b000069 | prose | pages [3] -->
17 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.1 Strengths 17 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.2 Weaknesses

<!-- b000070 | prose | pages [3] -->
9 Policy Strategies

<!-- b000071 | heading | pages [3] -->
10 Conclusion

<!-- b000072 | prose | pages [3] -->
17

<!-- b000073 | prose | pages [3] -->
18

<!-- b000074 | prose | pages [3] -->
19

<!-- b000075 | heading | pages [3] -->
11 Policy Letter Regarding Opioid Use in the United States

<!-- b000076 | prose | pages [3] -->
21

<!-- b000077 | prose | pages [3] -->
A Appendix: Epicenters and vulnerable counties 25

<!-- b000078 | prose | pages [3] -->
B Appendix: Top 30 highly correlated socioeconomic factors

<!-- b000079 | prose | pages [3] -->
C Appendix: Supplementary images

<!-- b000080 | prose | pages [3] -->
28

<!-- b000081 | prose | pages [3] -->
29

<!-- b000082 | heading | pages [3] -->
Introduction

<!-- b000083 | prose | pages [3] -->
1

<!-- b000084 | prose | pages [3] -->
In 2015, 33,091 people died of an overdose on heroin and other opioids, representing more than 60 percent of the total overdose deaths in the United States that year [1]. Given that overdose was also the leading cause of accidental deaths that year [1], it is clear that the dispersion of opioids is a serious problem in this country. Opioids are a class of narcotic painkillers, including the illicit drug heroin, that are derived from the poppy ﬂower, or are synthesized artiﬁcially and have a similar structure to other opioids. Some examples of opioid prescription drugs are morphine, hyrocodone, oxycodone, dihydromorphone, and fentanyl. While almost every drug in this class can be prescribed to manage chronic pain, it is clear

<!-- b000085 | prose | pages [3] -->
that the spread of opioid use has spread far beyond the reach of prescribed medicine and presented itself as an epidemic. This plague, while deadly, is highly treatable with proper targeting for law enforcement and strategies for potential victims. For this reason, it is of the utmost importance that we understand and analyze the spread of opioids and ﬁgure out how to reverse the trend. In this report, we do the same by building mathematically rigorous models. In summary, we will take the data pertaining to counties of ﬁve diﬀerent states - Kentucky, West Virginia, Virginia, Ohio and Pennsylvania - and develop a predictive model to analyze how drug abuse spreads and infects the counties. Then, we will attempt to ﬁnd solutions to the same problem using the model.

<!-- b000086 | prose | pages [3] -->
1.1 Problem Summary

<!-- b000087 | prose | pages [3] -->
• Visualize drug report data for each county in the states of Ohio, Kentucky, Pennsylvania, Virginia, and West Virginia for the years 2010-2016.

<!-- b000088 | furniture | pages [4] -->
Team #1901213

<!-- b000089 | furniture | pages [4] -->
Page 3 of 29

<!-- b000090 | prose | pages [4] -->
• Develop a predictive model that anticipates the spread of opioid use over the given time frame, and use it to ﬁnd potential epicenters for the spread of opioids within those states. • Analyze key socioeconomic factors to determine the relationship between these factors and opioid use. Employ these relationships to ﬁnd counties that are demographically prone to abusing opioids. • Determine a course of action to prevent the spread of new addictions and make current ones harder to maintain.

<!-- b000091 | prose | pages [4] -->
1.2 Our Model

<!-- b000092 | prose | pages [4] -->
• Initially we treated opioid addiction as a disease that spreads deterministically between neighbors, by assuming that the spread of it can be modeled in a Markovian fashion. This will allow us to ﬁnd a transition matrix that tells the inﬂuence of each county on one another. We also factored into this matrix the distances between counties. • Next, we modeled the eﬀect of socioeconomic factors throughout the data set, and correlated these changes with how opioid use in that county grows or shrinks over time. • We then combined the models in two ways – in a linear and parallel fashion. We used this to estimate epicenters from where the drug problem emanates. • Finally, we ran multiple simulations and predicted the drug problem well into the future to develop a number of strategies to tackle the epidemic from diﬀerent perspectives, selecting from the variables that contribute most heavily to the spread of opioids.

<!-- b000093 | prose | pages [4] -->
In our model, we analyze the general eﬀect of socioeconomic factors as well as the drug problem of neighboring counties. Due to the general approach taken in model, the model will very likely scale well to larger regions.

<!-- b000094 | prose | pages [4] -->
The rest of this report is organized as follows: Section 2 will provide background information necessary for understanding the condition we are modeling. Section 3 will brieﬂy discuss the provided data for this analysis. In Section 4 we will make the necessary assumptions to allow the situation to be modeled eﬃciently. Section 5 will encapsulate the details of our models, both external and internal. In Section 6 we solve for the parameters of our model, and discuss the results we get. In Section 7, we will modify key factors that appeared to have great inﬂuence over the model, to determine its sensitivity to the initial conditions, and give insight into which the most eﬀective strategies for combating the drug problem. In Section 8, we will evaluate the strengths and weaknesses of our model. In Section 9 will lay out the strategies we have found will work best to reverse the drug crisis. Finally, we will conclude the report in Section 10 by summarizing our key ﬁndings. Additionally, in Section 11, we have written a brief memo to the Drug Enforcement Administration suggesting policy changes to combat the drug crisis.

<!-- b000095 | prose | pages [4] -->
2

<!-- b000096 | heading | pages [4] -->
Background

<!-- b000097 | prose | pages [4] -->
Before modeling the spread of opioids, it is important to understand the science behind addiction. When an opioid is taken, it mimics natural neurotransmitters by locking onto and

<!-- b000098 | furniture | pages [5] -->
Team #1901213

<!-- b000099 | furniture | pages [5] -->
Page 4 of 29

<!-- b000100 | prose | pages [5] -->
preventing the re-uptake of these chemicals. This results in the brain being ﬂooded with dopamine, the chemical the brain normally releases as part of its reward system. This can sometimes result in an unhealthy cycle of needing the drug that creates this feeling, and taking the drug at higher and higher doses due to tolerance. When a person has taken this cycle to the point where the drug becomes one of their basic needs, like food or water, and they suﬀer extreme adverse eﬀects in their life as a result, they have an addiction. Due to the addiction potential of opioids and the frequency with which they are prescribed, the spread of opioid use and abuse can be rapid.

<!-- b000101 | prose | pages [5] -->
In 2012, enough prescriptions for opioid medication were written for every American adult to have their own bottle of pills [2]. It is important to understand how those around one will factor into one’s likelihood to use opioids, due to how common opioids are in everyday life now. Along with one’s surroundings, data supports that certain socioeconomic factors can be correlated to an increase use in opioids [3]. Given these possibilities, it is paramount to ﬁnd if, and how much, these factors can predict future drug use, in order to stop the vicious cycle of addiction for so many victims.

<!-- b000102 | prose | pages [5] -->
3 Data

<!-- b000103 | prose | pages [5] -->
In this section, we will give a brief overview of the data we used to develop the models described in subsequent sections.

<!-- b000104 | prose | pages [5] -->
3.1 Given data

<!-- b000105 | prose | pages [5] -->
We were given 8 diﬀerent data ﬁles. The ﬁrst contained drug report counts from counties

<!-- b000106 | prose | pages [5] -->
of ﬁve states in USA (Kentucky, West Virginia, Virginia, Ohio, Pennsylvania). A drug is reported in this case as part of an investigation by local police departments. The data provided gives total drug reports for each county, and any counts of drug reports for prescription opioids or heroin, courtesy of the National Forensics Laboratory Information System (NFLIS). For our purposes, we used just the opioid and heroin counts. The other 7 data ﬁles contain US Census data for these counties from years 2010-2016. These represent a common set of about 134 socioeconomic factors.

<!-- b000107 | prose | pages [5] -->
While cleaning up the data, we realized that the number of counties diﬀered in some years.

<!-- b000108 | prose | pages [5] -->
If a county was missing drug report data in the ﬁrst ﬁle for any year, we set the drug reports to zero. Further, we realized that Bedford City, VA was incorporated into Bedford County, VA in 2013. So, we ﬁxed this discrepancy by adding the data from Bedford City from years 2010-2012 into those of Bedford County. Also, since 2013, the US Census data divided a few of the larger categories. So, during the cleanup process, we had to account for those discrepancies manually.

<!-- b000109 | prose | pages [5] -->
3.2 Additional data

<!-- b000110 | prose | pages [5] -->
As we were not given any data about the distances between counties, but were allowed to get such data from outside sources, we obtained the distance between counties, as measured in

<!-- b000111 | furniture | pages [6] -->
Team #1901213

<!-- b000112 | furniture | pages [6] -->
Page 5 of 29

<!-- b000113 | prose | pages [6] -->
2010, from [4]. Once again, we had to remove Bedford City from this list as it is no longer independent from the county of the same name.

<!-- b000114 | prose | pages [6] -->
4

<!-- b000115 | heading | pages [6] -->
Assumptions

<!-- b000116 | prose | pages [6] -->
When designing a model, it is necessary to make assumptions to simplify the problem to an

<!-- b000117 | prose | pages [6] -->
eﬀective representation of reality i.e., the data provided, to be able to eﬃciently and closely predict the future. Our model is no diﬀerent and requires assumptions be made about the factors that contribute to drug abuse and the social reaction to witnessing drug use. The following subsections discuss each of our assumptions in the order of their importance.

<!-- b000118 | prose | pages [6] -->
4.1 As a disease

<!-- b000119 | prose | pages [6] -->
Our model treats the opioid crisis as an epidemic and each drug report as an infected individual. This gives us the ability to interpret the given data in a more familiar context.

<!-- b000120 | prose | pages [6] -->
To see why the opioid addiction can be thought of as a disease, consider what happens during addiction. The drug overstimulates the brain’s reward system and as the user builds tolerance - the overstimulated system becomes the ‘new normal - a positive feedback loop is created

<!-- b000121 | prose | pages [6] -->
where the user needs larger doses to get the same high. This implies that opioid addiction is not just dependent on intrinsic factors such as tolerance and drug use habits. It also depends on external factors such as peers, drug availability, legality, etc. This dependence on external and internal factors is analogous to diseases. And treating our model in such a manner gives us simple interpretations to our results.

<!-- b000122 | prose | pages [6] -->
4.2

<!-- b000123 | heading | pages [6] -->
The Markovian assumption

<!-- b000124 | prose | pages [6] -->
In order to reduce computation power, our model is based on the Markovian assumption. The Markovian assumption, otherwise known as the Markov property, states that the next state depends only on the current state. This is also referred to as memorylessness because the model need not remember the past to predict the future. Although this is often used to describe probabilistic models, we will use the same assumption to help build our model, which is not entirely probabilistic. Apart from reduced need for excessive computation, we have made this assumption because it has been successfully used to model population dynamics [5,6] and epidemiology [7,8] in the past.

<!-- b000125 | prose | pages [6] -->
To be precise, we will use the second order Markov property that says that the future depends on the current state and the previous state i.e., state at time t + 1 depends on the states at times t, t −1.

<!-- b000126 | prose | pages [6] -->
4.3 Proximity to neighboring counties

<!-- b000127 | prose | pages [6] -->
The third assumption is that distance to other counties plays an important role in each county’s opioid problem. In other words, counties that are farther will have a diﬀerent, not necessarily small, eﬀect than counties that are closer. Although we have no way of estimating

<!-- b000128 | furniture | pages [7] -->
Team #1901213

<!-- b000129 | furniture | pages [7] -->
Page 6 of 29

<!-- b000130 | prose | pages [7] -->
this relation with distance a priori, we can intuitively hypothesize that it will be an inverse relation.

<!-- b000131 | prose | pages [7] -->
This assumption also follows from the analysis of opioid crisis as an epidemic - a person who is 100 miles away from me and suﬀering from common cold has a diﬀerent eﬀect from a person who is in my town with the same condition.

<!-- b000132 | prose | pages [7] -->
4.4 All opioids are the same

<!-- b000133 | prose | pages [7] -->
Another assumption made in our model is that all opioids are approximately the same, having the same health risks and eﬀects. This allows us to analyze the total reports of opioids in each county, rather than analyze every opioid individually. While this assumption is not entirely realistic, we justify this assumption because the counts of drug reports, sorted by individual opioids, are very sparse. The sparseness of the data, when analyzed by individual drugs, could severely skew our model. This can also be justiﬁed as, the eﬀect of all opioids are very similar, just diﬀerent in magnitude.

<!-- b000134 | prose | pages [7] -->
A consequence of this is that all opioid addictions are also cured in same manner. This allows us to explore intervention strategies using a single model.

<!-- b000135 | prose | pages [7] -->
4.5 Data homogeneity across counties

<!-- b000136 | prose | pages [7] -->
Finally, we assumed that data from each county is collected with the same accuracy across each county. For instance, we assume that the number of opioid reports in a county reﬂect the true use of opioids in that county, rather than the diligence, or lack thereof, to report opioid use.

<!-- b000137 | prose | pages [7] -->
While this might not be realistic, we assume homogeneity because we have no means of verifying and correcting our data to reﬂect any inhomogeneity. Further, this assumption also simpliﬁes our analysis and ensures that the data provided can be represented by our model.

<!-- b000138 | prose | pages [7] -->
5

<!-- b000139 | heading | pages [7] -->
Model

<!-- b000140 | heading | pages [7] -->
Nomenclature

<!-- b000141 | prose | pages [7] -->
nt = Health of all counties in year t sorted by FIPS code xt = Opioid problem of all counties in year t sorted by FIPS code A = Adjacency matrix Q = Transition matrix δ = Threshold for opioid reports per capita to declare a county as infected St = 30 highly correlated socioeconomic factors of all counties in year t sorted by FIPS code β1 = Parameters of the linear regression model using St β2 = Parameters of logisitc regression model using St

<!-- b000142 | prose | pages [7] -->
As hinted in Section 4, we will model the opioid crisis as a disease. Treating this as a disease

<!-- b000143 | furniture | pages [8] -->
Team #1901213

<!-- b000144 | furniture | pages [8] -->
Page 7 of 29

<!-- b000145 | prose | pages [8] -->
helps us decouple the larger problem into two smaller problems – modeling the eﬀect of external factors, and modeling the eﬀect of internal factors. This can be thought of as follows: the future health of an individual depends on the current health of their neighbors and the current health of the individual. Equation 1 shows this relationship.

<!-- b000146 | prose | pages [8] -->
=

<!-- b000147 | prose | pages [8] -->
|{z} Future

<!-- b000148 | prose | pages [8] -->
+

<!-- b000149 | prose | pages [8] -->
(1)

<!-- b000150 | prose | pages [8] -->
|{z}

<!-- b000151 | prose | pages [8] -->
|{z}

<!-- b000152 | prose | pages [8] -->
Surrounding

<!-- b000153 | prose | pages [8] -->
opioid problem

<!-- b000154 | prose | pages [8] -->
Internal well being

<!-- b000155 | prose | pages [8] -->
opioid problem

<!-- b000156 | prose | pages [8] -->
First we will develop a model that predicts health based on the health of all counties. Then, we will create a model that factors in the internal factors i.e., socioeconomic factors for each county. Finally, we will combine these together to form a holistic model.

<!-- b000157 | prose | pages [8] -->
5.1 Deﬁning health

<!-- b000158 | prose | pages [8] -->
So far, we have loosely used the term health to refer to the amount of drug crisis in each county. Here, we will formally deﬁne and quantify health. Using the raw number of drug reports in each county can be misleading because the population of counties are diﬀerent. So, instead, we normalize the number of drug reports every year by the population of that county. This gives us a better representation of the health of the counties.

<!-- b000159 | prose | pages [8] -->
We will use n(k)

<!-- b000160 | prose | pages [8] -->
to denote this health measure of country k in year t, and nt to denote the t health of all counties sorted by the FIPS code in year t. If we have N counties, nt ∈RN×1.

<!-- b000161 | prose | pages [8] -->
5.2

<!-- b000162 | heading | pages [8] -->
Modeling external factors

<!-- b000163 | prose | pages [8] -->
Our model for predicting the drug crisis using external factors takes into account the opioid problem in all counties and the distances between counties. Our model for external factors is summarized in Equation 2.

<!-- b000164 | prose | pages [8] -->
xt+1 = QAxt (2)

<!-- b000165 | prose | pages [8] -->
Now, we will look at what each of these terms represent.

<!-- b000166 | prose | pages [8] -->
5.2.1 Understanding xt

<!-- b000167 | prose | pages [8] -->
xt to represent the opioid problem of each county in year t. We use xt to encapsulate the current health and the trend in health from last year. This makes sense because the current opioid use and the trend of that county’s opioid use will have an eﬀect on the neighboring counties. We calculate xt as:

<!-- b000168 | prose | pages [8] -->
xt = nt + (nt −nt−1)

<!-- b000169 | prose | pages [8] -->
= 2nt −nt−1

<!-- b000170 | prose | pages [8] -->
Thus, xt ∈RN×1. This is also where our second order Markovian assumption comes into play. Going back to Equation 2, notice how xt predicts xt+1 i.e., the opioid problem of counties in year t + 1 depends on the health of counties in years t and t −1. Thus, our model is temporally aware of itself.

<!-- b000171 | furniture | pages [9] -->
Team #1901213

<!-- b000172 | prose | pages [9] -->
5.2.2 Understanding A

<!-- b000173 | furniture | pages [9] -->
Page 8 of 29

<!-- b000174 | prose | pages [9] -->
A refers to a modiﬁed adjacency matrix. This accounts for the distances between counties. Each element in A ∈RN×N is given by:

<!-- b000175 | prose | pages [9] -->
(

<!-- b000176 | prose | pages [9] -->
1 , i̸ = j distance between county i and j

<!-- b000177 | prose | pages [9] -->
ai,j =

<!-- b000178 | prose | pages [9] -->
1 , i = j

<!-- b000179 | prose | pages [9] -->
Thus, all counties have values less than 1 in A, and farther counties will have a smaller value. To understand how this works, let us look at each element of the vector Axt:

<!-- b000180 | prose | pages [9] -->
+ ai,2x(2)

<!-- b000181 | prose | pages [9] -->
(Axt)i = ai,1x(1)

<!-- b000182 | prose | pages [9] -->
t

<!-- b000183 | prose | pages [9] -->
+ · · · + ai,Nx(N) t

<!-- b000184 | prose | pages [9] -->
t

<!-- b000185 | prose | pages [9] -->
As we can see, the opioid problem from a county that is at larger distance from country i contributes a smaller value in the vector Axt. Thus, the i-th element of Axt encodes the information about both, proximity between counties and, the opioid problem across counties. Thus, our model is spatially aware of itself.

<!-- b000186 | prose | pages [9] -->
5.2.3 Understanding Q

<!-- b000187 | prose | pages [9] -->
Q is the transition matrix that propagates the opioid problem at year t into the next year. Q ∈RN×N propagates the model by understanding how the opioid problem in each county aﬀects every other county including itself. Thus, we can use the elements of Q to determine which counties have the largest inﬂuences on other counties.

<!-- b000188 | prose | pages [9] -->
Qi,j = how much does county j aﬀect county i independent of distance

<!-- b000189 | prose | pages [9] -->
After normalizing the rows, we can use the column sums to estimate the most inﬂuential counties in the opioid crisis.

<!-- b000190 | prose | pages [9] -->
5.2.4 Estimating Q

<!-- b000191 | prose | pages [9] -->
At this point, we have xt and A from data. We need to estimate Q, the transition matrix. Notice that we need not ﬁnd a Q that works exactly for all t. In fact, depending on our data, such a Q might not exist at all. Even if we do ﬁnd such a Q, it might not generalize well for examples outside the dataset. Instead, we want to ﬁnd a Q that approximately works best for all t. We can do this by solving a modiﬁed least squares estimation problem:

<!-- b000192 | prose | pages [9] -->
X

<!-- b000193 | prose | pages [9] -->
Q = min

<!-- b000194 | prose | pages [9] -->
Q′

<!-- b000195 | prose | pages [9] -->
t

<!-- b000196 | prose | pages [9] -->
∥xt+1 −Q′Axt∥ (3)

<!-- b000197 | prose | pages [9] -->
Here, the summation of the norms is over all t in our dataset.

<!-- b000198 | prose | pages [9] -->
Thus, we have a model accounting for external factors that is spatiotemporally aware of the opioid problem. Now, we can focus on constructing a model that is based on the internal factors.

<!-- b000199 | furniture | pages [10] -->
Team #1901213

<!-- b000200 | prose | pages [10] -->
5.3

<!-- b000201 | heading | pages [10] -->
Modeling internal factors

<!-- b000202 | furniture | pages [10] -->
Page 9 of 29

<!-- b000203 | prose | pages [10] -->
Going back to the analogy of disease, we can argue that the opioid problem in a county is also dependent on the internal properties of the county i.e., the socioeconomic factors of the county. So, we can develop a model that takes these into account and see the eﬀect of socioeconomic factors on the opioid crisis.

<!-- b000204 | prose | pages [10] -->
The data set given to us has approximately 150 socioeconomic factors. Instead of building a model that uses all the factors, we can instead select the 30 highly correlated factors and use them. This simple pre-processing step has two advantages – it will simplify our model and, make our model more interpretable. To measure correlation, we will use the Pearson correlation coeﬃcient [9].

<!-- b000205 | prose | pages [10] -->
5.3.1 Linear regression

<!-- b000206 | prose | pages [10] -->
We can use these 30 features to build a linear model that would predict the opioid problem

<!-- b000207 | prose | pages [10] -->
in year t with socioeconomic factors of each county in year t. Let us denote the matrix containing the top 30 socioeconomic factors of all counties in year t as St. Each row of St corresponds to a single county and each column corresponds to a single socioeconomic factor. Then, our problem is that of estimating parameters β1 such that:

<!-- b000208 | prose | pages [10] -->
Stβ1 = xt (4)

<!-- b000209 | prose | pages [10] -->
This is once again a least squares estimation problem to ﬁnd the best β1

<!-- b000210 | prose | pages [10] -->
5.3.2 Logistic regression

<!-- b000211 | prose | pages [10] -->
If we deﬁne a threshold of drug reports per capita, δ, for a county to be infected with the opioid problem, we can also use the socioeconomic factors, St to predict whether a county is infected or not. We can do this by constructing a logistic regression model that gives the probability that a county is infected [10]. The probability that county i is infected in year t is given by:

<!-- b000212 | prose | pages [10] -->
p(i)

<!-- b000213 | prose | pages [10] -->
= t 1

<!-- b000214 | prose | pages [10] -->
(5) 1 + e−S(i) β2 t

<!-- b000215 | heading | pages [10] -->
where β2 are the parameters of the model that brings p(i)

<!-- b000216 | prose | pages [10] -->
p(i)

<!-- b000217 | prose | pages [10] -->
→0 for non-infected states. t

<!-- b000218 | prose | pages [10] -->
5.4

<!-- b000219 | heading | pages [10] -->
Combining the two models

<!-- b000220 | prose | pages [10] -->
→1 for infected counties and t

<!-- b000221 | prose | pages [10] -->
So far, we have decoupled the problem into external and internal, and we have developed models that solve both problems. Now, we are ready to combine the models to complete our model development phase. Here, we propose two diﬀerent ways to combine the models.

<!-- b000222 | furniture | pages [11] -->
Team #1901213

<!-- b000223 | furniture | pages [11] -->
Page 10 of 29

<!-- b000224 | prose | pages [11] -->
5.4.1 A convex combination

<!-- b000225 | prose | pages [11] -->
We can combine the external propagation model in Equation 2 and the internal linear

<!-- b000226 | prose | pages [11] -->
regression model in Equation 4 in a convex fashion to predict the opioid problem in year t as:

<!-- b000227 | prose | pages [11] -->
xt+1 = θ · QAxt + (1 −θ) · St+1β1 (6)

<!-- b000228 | prose | pages [11] -->
where θ ∈[0, 1] is a parameter that controls how much each model contributes to the ﬁnal prediction. We can choose a θ that minimizes the error on our prediction.

<!-- b000229 | prose | pages [11] -->
5.4.2

<!-- b000230 | heading | pages [11] -->
A two stage model

<!-- b000231 | prose | pages [11] -->
Instead of directly combining the results from both models, we can use the results indepen- dently to determine if a county is infected or not. Using the external propagation model from Equation 2 and applying the threshold δ, we can identify infected counties. Then, independently, we can use the internal logistic regression model from Equation 5 to identify infected counties. Then, from both results, we can infer potential risk for infection for counties.

<!-- b000232 | prose | pages [11] -->
A county identiﬁed as infected by both models is labeled high risk, while a county identiﬁed by only one model is labelled medium risk, and a county identiﬁed by neither models is labelled low risk. Note that the infection threshold, δ, is kept constant over the time span of both models.

<!-- b000233 | prose | pages [11] -->
6

<!-- b000234 | heading | pages [11] -->
Solutions

<!-- b000235 | prose | pages [11] -->
We estimated parameters to the models developed in Section 5 described in Equations 2,4,5.

<!-- b000236 | prose | pages [11] -->
In this section, we will discuss the results we get from our models.

<!-- b000237 | prose | pages [11] -->
6.1 Estimating δ

<!-- b000238 | prose | pages [11] -->
To ﬁx the threshold to declare a county as infected, we took the ﬁrst year in our dataset i.e., 2010 and calculated the threshold to be one standard deviation greater than the mean drug reports per capita. This allows us to pick the top 16% of counties that are most infected, assuming the the drug reports per capita to be normally distributed.

<!-- b000239 | prose | pages [11] -->
δ = mean(n2010) + std(n2010)

<!-- b000240 | prose | pages [11] -->
This yields, δ ≈0.0038 as the threshold to declare a county as infected. Figure 1 shows the spread of infected counties from year 2010 to 2016 using this threshold. Alternatively, in Appendix C, Figure 3 shows the spread of opioid crisis from year 2010 to 2016 in terms of the actual number of drug reports per 100 people.

<!-- b000241 | furniture | pages [12] -->
Team #1901213

<!-- b000242 | furniture | pages [12] -->
Page 11 of 29

<!-- b000243 | caption | pages [12] -->
Figure 1: Spread of the opioid crisis from year 2010 to 2016. The threshold for infection is

<!-- b000244 | prose | pages [12] -->
δ = 0.0038 drug reports per capita. Counties colored red are infected.

<!-- b000245 | furniture | pages [13] -->
Team #1901213

<!-- b000246 | furniture | pages [13] -->
Page 12 of 29

<!-- b000247 | prose | pages [13] -->
6.2 Estimating the inﬂuence of external factors

<!-- b000248 | prose | pages [13] -->
We estimated Q with the help of Equation 3 using data from years 2010-2015. Then, we

<!-- b000249 | prose | pages [13] -->
tried to predict the number of drug reports per capita in year 2016, n2016 using this Q.1 Our prediction has a mean squared error of 2 × 10−5 drug reports per capita across all counties.

<!-- b000250 | prose | pages [13] -->
Such a small error might be because we have overﬁt our model. So, instead, we also estimated Q using data from years 2010, 2011. Then, we predicted the number of drug reports for years 2012-2016. Here, we observed a mean squared error of 8.42 × 10−5 for year 2016. This shows that our model for external factors does a good job for predicting well into the future.

<!-- b000251 | prose | pages [13] -->
Then, we estimated Q from all the data given to us i.e., from years 2010-2016. Now, we propagated the model forward in time and found that, all else constant, by year 2025, all counties are cured. Further, by year 2038, the drug reports per capita reaches a steady state. In 2038, mean(n2038) = 1.8×10−3 and std(n2038) = 0.002. Further, mean(n2010) ≈1.8×10−3. This shows that as we propagate forward in time, if there are no other changes, the drug reports per capita from all states converge to the mean of the initial data.

<!-- b000252 | prose | pages [13] -->
6.3 Estimating the inﬂuence of internal factors

<!-- b000253 | prose | pages [13] -->
We were given 149 socioeconomic factors for years 2010-2012. Some of these factors were

<!-- b000254 | prose | pages [13] -->
subdivided into multiple categories in subsequent years, so the number of socioeconomic factors increased to 152 in years 2013-2016. We analyzed the correlation between each socioeconomic factor and the health of counties for all years using the Pearson correlation coeﬃcient [9]. Using this, we picked the top 30 highly correlated (including both positive and negative correlations) for our analysis.

<!-- b000255 | prose | pages [13] -->
This simpliﬁed our model as we discarded socioeconomic factors with low magnitude correlations. The list of socioeconomic factors we chose are listed in Appendix B.

<!-- b000256 | prose | pages [13] -->
Using just these socioeconomic factors, we performed regression analysis to determine if it is practical to use a linear model described by Equation 4 in Section 5.3.1 to predict the opioid problem. Our regression coeﬃcient was, R2 = 0.1296. This suggests that we cannot use just the socioeconomic factors to accurately predict the opioid problem. In fact, after training the model on data from years 2010-2015 and attempting to predict the health of counties for year 2016 gives a mean squared error of 1.949 × 10−3 drug reports per capita, which is much larger than the error we got in the external model. This is not surprising because it turns out that human behavior, which is the crux of the opioid problem, is very hard to predict on socioeconomic features [11].

<!-- b000257 | prose | pages [13] -->
However, when we built the logistic model described by Equation 5 in Section 5.3.2, we got a mean accuracy of 87.98 % accuracy i.e., the logistic model seems to do better. A closer look at the results says that our true positive rate is 3.57% and our true negative rate is 99.51%. This suggests that our classiﬁer is skewed. Taking a look at the data, we observed that only 12 % of our original data contains positive examples i.e., infected counties. This was by design when we chose the threshold, δ. Thus our classiﬁer suﬀers from a class imbalance problem that skews the classiﬁer towards predicting negative more often. We argue that we

<!-- b000258 | prose | pages [13] -->
1If we have xt, nt−1, we can ﬁnd nt = 0.5 · (xt + nt−1)

<!-- b000259 | furniture | pages [14] -->
Team #1901213

<!-- b000260 | furniture | pages [14] -->
Page 13 of 29

<!-- b000261 | prose | pages [14] -->
care more about capturing all the infected states, even if there are some false positives, as opposed to choosing to ignore infected states. In other words, it is better to diagnose an infection and have the infection not be there than to claim a group is in good health when it is not. In that case, setting the probability threshold for declaring a county to be infected to 0.1 captures 70 % of all infected counties.

<!-- b000262 | prose | pages [14] -->
These analyses suggest that using socioeconomic factors alone to predict the health is neither accurate nor useful even though there is a lot of correlation. So to make this model work we will have to combine it with the external model.

<!-- b000263 | prose | pages [14] -->
6.4

<!-- b000264 | heading | pages [14] -->
Building a convex combination of models

<!-- b000265 | prose | pages [14] -->
We combined the external and internal models estimated from Sections 6.2, 6.3 to develop

<!-- b000266 | prose | pages [14] -->
the convex combination of the two models as described by Equation 6 in Section 5.4.1. We varied θ from 0 to 1 in steps of 0.001 and found that we get the best prediction when θ = 1 i.e., we only consider the external model developed in Section 6.2.

<!-- b000267 | prose | pages [14] -->
There are two explanations to this: The ﬁrst is that the internal factors alone are not an accurate indicator of county health. Although unlikely, our results from Section 6.3 also suggest the same. The second, more plausible, conclusion is that the socioeconomic factors are already encoded into the health of each county. This explains why there is high correlation, but not enough evidence to make accurate predictions.

<!-- b000268 | prose | pages [14] -->
Since the convex combination of the two models is eﬀectively just the external model, the future predictions from this will be identical to the predictions described in Section 6.2.

<!-- b000269 | prose | pages [14] -->
6.5

<!-- b000270 | heading | pages [14] -->
Building the two stage model

<!-- b000271 | prose | pages [14] -->
Next, we built the two stage model described in Section 5.4.2. Here, we analyzed the spread of the opioid crisis by comparing the infected states predicted, independently, by the external model with internal logistic regression model. A county predicted as infected by both models is determined to be high risk; predicted as infected by only one model is low risk and; predicted by neither is not at risk.

<!-- b000272 | prose | pages [14] -->
Since we do not have socioeconomic data after year 2016, it will not be possible for us to make predictions past this using the two stage model. Instead, to measure the performance of this model, we trained our model on years 2010-2011 and made predictions for years 2012-2016. The results are summarized in Table 1. Our models suggest that the number of high risk counties decreases as we move forward in time while the number of low risk counties increases. This means that the opioid crisis somehow stabilizes across all counties with the infection decreasing in counties with a high opioid problem and increasing in counties with low opioid problem. This is similar to the results we got in Section 6.2 and suggests that the external model once again dominates over the internal model.

<!-- b000273 | prose | pages [14] -->
6.6 Epicenters and vulnerabilities

<!-- b000274 | prose | pages [14] -->
We identiﬁed two diﬀerent classes of counties that are important in the opioid crisis - epicenters

<!-- b000275 | prose | pages [14] -->
and vulnerabilities. We deﬁne an epicenter as an infected county from where the infection

<!-- b000276 | furniture | pages [15] -->
Team #1901213

<!-- b000277 | furniture | pages [15] -->
Page 14 of 29

<!-- b000278 | prose | pages [15] -->
Number of high risk counties Year 2012 6 2013 3 2014 0 2015 0 2016 0 Number of low risk counties 60 66 70 70 76

<!-- b000279 | caption | pages [15] -->
Table 1: Predictions from two stage model

<!-- b000280 | prose | pages [15] -->
spreads outward to surrounding counties in subsequent years and around which there are a lot of other infected counties. And, we deﬁne a county to be vulnerable if its socioeconomic (internal) factors give enough evidence to suggest that it will become infected in the near

<!-- b000281 | prose | pages [15] -->
future, due to low internal immunity to infection.

<!-- b000282 | prose | pages [15] -->
6.6.1 Identifying epicenters

<!-- b000283 | prose | pages [15] -->
From our deﬁnition of epicenter, it makes sense to use the external model to determine the epicenters. To do this, we need to take into account both how much inﬂuence a county has on other counties and how far away the aﬀected counties are. This information is encoded in the transition matrix Q, and the adjacency matrix A respectively. To combine these, we performed the elementwise matrix multiplication operation, ◦,2 on Q and A. So, each element (Q ◦A)i,j tells us the inﬂuence of county j on county i after factoring in the distance. Then,

<!-- b000284 | prose | pages [15] -->
we sum the columns to tell the overall inﬂuence of all counties. Through this method, we chose the 10 counties that had the greatest inﬂuence as epicenters.

<!-- b000285 | prose | pages [15] -->
We predicted that the following counties, in no particular order, are the epicenters:3

<!-- b000286 | prose | pages [15] -->
• Doddridge, Harrison, Marion, and Morgan Counties in West Virginia. • Bracken, Carroll, Harlan, Gallatin, and Campbell Counties in Kentucky. • Mecklenburg County in Virgina

<!-- b000287 | caption | pages [15] -->
Figure 1 shows how the infection spreads from year 2010 to 2016. Here, the threshold for

<!-- b000288 | prose | pages [15] -->
infection is δ = 0.0038 drug reports per capita. Figure 2 shows the epicenters identiﬁed by our model. From both these ﬁgures, we can see that our model was able to accurately identify all the counties from where the infection spreads outward. This gives us evidence that our models are working the way we intended them to.

<!-- b000289 | prose | pages [15] -->
The epicenters in Figure 2 share a common characteristic – they are centrally located with respect to other infected counties, which means the average location inﬂuence would be fairly high. As an outlier, we found that Mecklenburg County, Virginia is an epicenter. We can see that this county does not have a great inﬂuence on surrounding counties. Our model does not distinguish between incoming and outgoing drug reports per capita. So, a plausible explanation is that this county is being infected by neighboring counties outside our data set.

<!-- b000290 | prose | pages [15] -->
2This is often described as the Hadamard product 3The ranking for these counties by strength of inﬂuence can be found in table 4 in Appendix A

<!-- b000291 | furniture | pages [16] -->
Team #1901213

<!-- b000292 | furniture | pages [16] -->
Page 15 of 29

<!-- b000293 | caption | pages [16] -->
Figure 2: Epicenters of the opioid crisis as identiﬁed by our model. The epicenters are colored

<!-- b000294 | prose | pages [16] -->
yellow.

<!-- b000295 | prose | pages [16] -->
6.6.2 Identifying vulnerable counties

<!-- b000296 | prose | pages [16] -->
By deﬁnition, vulnerable counties are determined by the socioeconomic factors. So, we used the logistic regression model and chose 10 counties whose average probability of being infected were the highest across years 2010-2016. These counties, in no particular order, are as follows:4

<!-- b000297 | prose | pages [16] -->
• Scioto, Montgomery, and Hamilton Counties in Ohio • Philadelphia, Pennsylvania • Kanawha County, West Virginia • Pulaski, Pike, Laurel, Bell, and Jeﬀerson Counties in Kentucky

<!-- b000298 | prose | pages [16] -->
We also predicted 10 counties that would be vulnerable in 2017, if their demographic

<!-- b000299 | prose | pages [16] -->
composition stayed constant. To see these counties, consult Table 3 in Appendix A

<!-- b000300 | prose | pages [16] -->
6.6.3 Understanding these counties

<!-- b000301 | prose | pages [16] -->
Although the epicenters in Figure 2 appear to be isolated, these counties are adjacent to four major roadways – (1) I-75 that cuts across Harlan, Kentucky through Bracken, Campbell and Carroll, Kentucky to Hamilton, Ohio and further north; (2) I-64 that runs west to east across Kentucky, West Virginia and Virginia; (3) I-79 from Marion, West Virginia northwards into Pennsylvania and; (4) U.S. Route 23 from the bordering counties of Kentucky, West Virginia, and Virginia northwards into Ohio.

<!-- b000302 | prose | pages [16] -->
Based on these results, it is clear that our models were able to inherently learn the means of transit of opioid drug reports across major roads within the region. We hypothesize that if neighboring states were included in the analysis, such as Maryland or Delaware, other major roads would connect the remaining vulnerable counties and epicenters. So while many vulnerable counties are not currently infected, identifying if they fall along these major roadways could help us in mitigation eﬀorts.

<!-- b000303 | prose | pages [16] -->
4The ranking of these counties can be found in Table 2 in Appendix A

<!-- b000304 | furniture | pages [17] -->
Team #1901213

<!-- b000305 | furniture | pages [17] -->
Page 16 of 29

<!-- b000306 | prose | pages [17] -->
7

<!-- b000307 | heading | pages [17] -->
Sensitivity Analysis

<!-- b000308 | prose | pages [17] -->
In this section, we will test our model under diﬀerent initial conditions to see their eﬀects. First, we will vary the external factors and then the internal factors.

<!-- b000309 | prose | pages [17] -->
7.1 Tweaking the external factors

<!-- b000310 | prose | pages [17] -->
First, we set the health of all identiﬁed epicenters to 0 at year 2010. This is analogous to purging the opioid crisis at the root. Then, we propagated the model to 2016. At the end, we observed that only 7 counties were infected as opposed to 56 in the original data.

<!-- b000311 | prose | pages [17] -->
Then, we implemented a version of border control where we set the distance to and from the epicenters in the adjacency matrix, A, to 0. This is eﬀectively preventing ﬂow of drugs through these counties. Once again, at the end of the simulation, we observed that only 8 counties were infected, 7 of which showed up in the previous simulation. We also implemented another version of border control where we set the entries of Q matrix corresponding to the epicenters to 0. The results were identical to the previous border control experiment.

<!-- b000312 | prose | pages [17] -->
7.2 Tweaking the internal factors

<!-- b000313 | prose | pages [17] -->
We changed some of the highly correlated socioeconomic factors to see if they had any any

<!-- b000314 | prose | pages [17] -->
eﬀect on our logistic regression model. For the following simulations, the probability threshold for declaring a county as infected was set to 0.20, and data from year 2016 was used.

<!-- b000315 | prose | pages [17] -->
We decreased the fraction of children under the age of 18 living with their grandparents by

<!-- b000316 | prose | pages [17] -->
half. This decreased the number of infected counties, as predicted by this model, from 56 to 6. We gathered this trend to be coming from one of two possibilities. The ﬁrst is the fact that many seniors are in chronic pain as a result of age or old injuries, and thus are more likely to be prescribed opioids and become addicted. The other is that the children are stealing opioids from those grandparents and abusing them recreationally.

<!-- b000317 | prose | pages [17] -->
We then lowered the fraction of people who were never married by half. This increased

<!-- b000318 | prose | pages [17] -->
the number of infected counties to 142. Correspondingly, decreasing the fraction of people currently married by half decreases the number of infected counties to 29. This trend is interesting and further research in the ﬁeld of psychology in the future can help us explain this.

<!-- b000319 | prose | pages [17] -->
More interestingly, decreasing the number of veterans above the age of 18 decreases the number of infected states to 0. This trend is likely because veterans are prone to be prescribed opioids to endure the traumas of war and their injuries as a result, and simply were never able to stop upon returning home.

<!-- b000320 | prose | pages [17] -->
It also turns out that decreasing the fraction of people with a Bachelor’s degree increases the number of infected states to 105. This trend is likely because people with an education are more likely to know the adverse eﬀects of prolonged opioid use and are therefore cautious with their usage. They are also less likely to be in a career that requires high amounts of

<!-- b000321 | furniture | pages [18] -->
Team #1901213

<!-- b000322 | furniture | pages [18] -->
Page 17 of 29

<!-- b000323 | prose | pages [18] -->
manual labor, and therefore would necessitate an opioid prescription at some time due to work.

<!-- b000324 | prose | pages [18] -->
Most of these trends can be explained intuitively. This suggests that both our models work in the manner we expect them to and are sensitive to parameters and initial conditions in the way we want them to be. This gives further evidence that our models will generalize well to data outside the data we used to develop the model. In addition, this gives us clear ideas for groups to target with new policy and possibly assistance.

<!-- b000325 | prose | pages [18] -->
8

<!-- b000326 | heading | pages [18] -->
Strengths and Weaknesses

<!-- b000327 | prose | pages [18] -->
In this section, we will discuss the strengths and weaknesses of the model we have developed.

<!-- b000328 | prose | pages [18] -->
8.1

<!-- b000329 | heading | pages [18] -->
Strengths

<!-- b000330 | prose | pages [18] -->
• Our model is nearly memoryless as it uses the Markovian assumption. This allows our model to accurately represent data without the tradeoﬀof computation power. In our model, we are very capable of approximating the drug use in the future based solely oﬀ of the present opioid use and the trend from the previous year. Thus our model does not need to use data that is older than two years to make new predictions. • Our model is incredibly accurate in prediction. Training our model using data from just two years, our model was able to predict the opioid use in each county for the following ﬁve years with a mean squared error of 8.42 × 10−5 opioid reports per capita. • Our model represents the diﬀerence in inﬂuence between counties. This is an important factor given that some counties will have greater inﬂuence on other counties, due to resources, location, and restrictions. This allows our model to be better at predicting future trends. • Our model also gives us interpretable values for each county’s inﬂuence on other counties. Our model thus identiﬁes the most inﬂuential counties giving law enforcers tangible targets. • Finally, our model is able to generalize to all areas and problems.

<!-- b000331 | prose | pages [18] -->
We made no assumptions about the regions we are dealing with when we developed the model – all the intrinsic factors of the regions are just parameters. We also built our model representing the opioid crisis as an epidemic. Thus, we can use the same model and apply it to diﬀerent regions across the world and to other problems that can be thought of as an epidemic.

<!-- b000332 | prose | pages [18] -->
8.2

<!-- b000333 | heading | pages [18] -->
Weaknesses

<!-- b000334 | prose | pages [18] -->
• In our model, epicenter calculation does not distinguish between outgoing and incoming opioid use. This means that inﬂuence of each county, in which the epicenters are determined based oﬀ, counts opioids that ﬂow into the state in the same manner as opioids that ﬂow out of the state. This means that our epicenter calculations do not solely predict counties that have the most inﬂuence on the outwards spread of opioids, but the total spread of opioids.

<!-- b000335 | furniture | pages [19] -->
Team #1901213

<!-- b000336 | furniture | pages [19] -->
Page 18 of 29

<!-- b000337 | prose | pages [19] -->
• While our model incorporates location, the ﬁniteness of the data set does not allow the model to factor in a county’s location to counties outside of the data set. Due to this, our model assigns added inﬂuence to edge counties in the data set. However, this problem could be solved very easily by adjusting the adjacency matrix, A, to reﬂect this. • Our model sets a threshold for an infected county. The threshold set by our model to consider a county infected, is any county whose opioid reports per capita is one standard deviation above the mean. A weakness of this design is that values that do not fall above this threshold, even slightly are not considered infected and therefore are not priority target areas. • Along the same lines, our model does not establish a clear ranking system of counties to target ﬁrst. While our model cares about the overall drug reports per capita in each county, we do not take into account the diﬃculties of law enforcement in diﬀerent counties. This is an important factor when looking from the policy makers’ perspectives. • According to our model, the socioeconomic factors are not helpful in making predictions alone even though the model proves that some speciﬁc socioeconomic factors directly aﬀect opioid use when altered. Even with this knowledge, when the socioeconomic model is combined with the external model(through a convex combination), it is seen that the most eﬀective model is a model in which the socioeconomic factors do not contribute. This is most likely due to the fact that the socioeconomic model is based on modelling the actions of individual humans, which is largely unpredictable through statistics. • Finally, our model does not take into account the feedback loop between opioid crisis and the socioeconomic factors. While our model accounts for the eﬀect of socioeconomic factors on opioid use, it does not factor in how opioid use will cause changes in socioeconomic factors. Thus we are ignoring the eﬀects of this feedback loop, without knowing how strong it is. Studying this feedback loop could help answer why our socioeconomic factors fail in making accurate predictions when used alone.

<!-- b000338 | prose | pages [19] -->
9 Policy Strategies

<!-- b000339 | prose | pages [19] -->
We identiﬁed the top 30 socioeconomic factors that correlate to opioid use. We can target

<!-- b000340 | prose | pages [19] -->
policy changes to aﬀect some of these socioeconomic factors in order to indirectly tackle the opioid crisis. We can also use our knowledge about the epicenters to decrease the spread of opioid use from these counties. In this section, we discuss a few of these strategies to mitigate the opioid crisis.

<!-- b000341 | prose | pages [19] -->
Educating vulnerable groups: The most important strategy would be to educate the groups that ﬁt into the socioeconomic factors that are deemed most vulnerable to spread of opioid use. One of the largest socioeconomic factors that play into opioid abuse is households with both children under 18 and adults over 65. This is likely attributed to teenagers using opioids prescribed to the older family members, and seniors in general having to be prescribed opioids more frequently. One example would be advertising on media frequented by seniors to tell them to lock up drugs from adolescents, and informing them of the dangers of prolonged

<!-- b000342 | furniture | pages [20] -->
Team #1901213

<!-- b000343 | furniture | pages [20] -->
Page 19 of 29

<!-- b000344 | prose | pages [20] -->
opioid use and addiction. We also found that decreasing the number of residents with college degrees intensiﬁed the opioid crisis. Another eﬀort that would mimic a positive change in this regard is to educate young people through school programs about the speciﬁc health eﬀects of opioid use, and the dangers of addiction and overdose.

<!-- b000345 | prose | pages [20] -->
Educating health care providers: Another important correlation with opioid use is the fraction of disabled residents and veterans in a county, which is probably due to increased rates of chronic pain in these groups. A study shows that patients receiving 200 MME (mg Morphine equivalent) per day showed a nearly 3-fold increase in opioid-related mortality [12]. One potential solution would be educating health care providers to prescribe alternative treatments of chronic pain, such as physical therapy or nonnarcotic drugs. Reduction within these two groups resulted in almost complete elimination of the opioid problem in our simulations.

<!-- b000346 | heading | pages [20] -->
Mental health care for people experiencing high life uncertainty: Our model also

<!-- b000347 | prose | pages [20] -->
predicts that those experiencing high uncertainty in their life, like enduring divorce or housing uncertainty, are more likely to abuse opioids [13]. This can be attributed to those experiencing uncertainty being vulnerable to impulsive decisions as a solution to their troubles. A possible solution for these factors would be to encourage mental health care for those experiencing high life uncertainty, and make it more accessible to groups who would have diﬃculty aﬀording it.

<!-- b000348 | prose | pages [20] -->
Law enforcement: One way in which to target the overall ﬂow of opioids is to reduce the access to opioids in the counties that our model deems epicenters. These counties are those that have the largest impact on the spread of opioid use across the data set. Allocating opioid preventative resources towards these counties would allow law enforcement to target suppliers who increase opioid use in their own counties, and prevent the supplies from these counties to spread to other populations. Alternatively, more closely monitoring potential drug traﬃckers through checkpoints at state borders would greatly reduce the threat of those opioids traveling to vulnerable counties along the four major roadways mentioned in Section 6.6.3.

<!-- b000349 | prose | pages [20] -->
10

<!-- b000350 | heading | pages [20] -->
Conclusion

<!-- b000351 | prose | pages [20] -->
The use and abuse of opioids in the United States has become a major problem in the past two decades. Between 1999 and 2014, over 165,000 people died from prescription opioid overdoses alone [2]. The deaths in that time span most likely could have been prevented, with proper strategies employed. We examined the drug reporting data in ﬁve states to develop a model which would inform us as to which speciﬁc strategies would be most eﬀective in preventing future prescription opioid and heroin overdoses, and other medical complications arising from those addictions.

<!-- b000352 | prose | pages [20] -->
We developed our model based on the possible external and internal factors present within

<!-- b000353 | prose | pages [20] -->
the counties and between them. Using the external model, we found that the epicenters for the spread of opioids are the following counties: West Virginia: Doddridge, Harrison, Marion, Morgan; Kentucky: Bracken, Carroll, Harlan, Gallatin, Campbell; Virginia Mecklenburg .

<!-- b000354 | furniture | pages [21] -->
Team #1901213

<!-- b000355 | furniture | pages [21] -->
Page 20 of 29

<!-- b000356 | prose | pages [21] -->
These are therefore the most important counties in terms of law enforcement eﬀorts and reduction of illicit supply. In addition, we predicted the counties that were most probable in becoming infected in subsequent years, based on their socioeconomic proﬁle and the correlations between those demographics and opioid use. These counties were: Ohio: Scioto, Montgomery, Hamilton; Pennsylvania: Philadelphia; West Virginia: Kanawha; Kentucky: Pulaski, Pike, Laurel, Bell, Jeﬀerson.

<!-- b000357 | prose | pages [21] -->
With all of these counties on one map, we ﬁrst believed them to be separate regions that

<!-- b000358 | prose | pages [21] -->
each spread opioids fairly independently. Upon further analysis, they were connected by four important highways in the region, which conﬁrms the inﬂuence values that we predicted. We also witnessed many infected counties moving up and down these roads as time progressed within our simulation. This gave us insight as to which policies with regard to law enforcement to employ to best reduce the ﬂow of opioids around the data.

<!-- b000359 | prose | pages [21] -->
With the external model, our predicted drug reports per capita diﬀered from the data on

<!-- b000360 | prose | pages [21] -->
average by 8.42 × 10−5. This means that this model was extremely robust in knowing where opioids will ﬂow and where they originate. While designing the internal model, we found that there was a high correlation between socioeconomic factors and the drug abuse problem, but the socioeconomic factors alone could not accurately predict the drug abuse problem. Further, when we combined the external and internal models, the external models always dominated. Therefore, we concluded that the socioeconomic factors are important, but are already encoded in the drug reports per capita of each county.

<!-- b000361 | prose | pages [21] -->
By combining the two models and running simulations under various conditions, we were able to identify speciﬁc strategies to combat the drug problem in these ﬁve states.

<!-- b000362 | prose | pages [21] -->
For future development, more data on hospital reports in addition to police reports, can give a better picture of how many people have a problem with opioids. Similar data from more neighboring states can help us understand the problem in a broader context, and possibly connect the isolated epicenter points to show their inﬂuence more eﬀectively. More data on people traveling between these counties can provide additional insights into how the drug problem in each county aﬀects every other county. Overall, however, this model very closely matches the data provided, and we hope that the strategies can be reasonably employed to help those who desperately need it.

<!-- b000363 | furniture | pages [22] -->
Team #1901213

<!-- b000364 | furniture | pages [22] -->
Page 21 of 29

<!-- b000365 | prose | pages [22] -->
11 Policy Letter Regarding Opioid Use in the United States

<!-- b000366 | prose | pages [22] -->
For the attention of the Chief Administrator of the DEA/NFLIS

<!-- b000367 | prose | pages [22] -->
Dear Chief Administrator,

<!-- b000368 | prose | pages [22] -->
One of the most pressing problems in the United States is the spread of opioid use across the nation. Given the severity of opioid addiction and its strong link to overdoses, it is imperative that a plan be developed to stop the rapid dispersion of opioids across the U.S. In an eﬀort to reverse the spread of opioid use, we have developed a predictive model to extract the target areas and demographics to address the opioid crisis across ﬁve neighboring states.

<!-- b000369 | prose | pages [22] -->
Our model identiﬁed the most inﬂuential counties across the states of Kentucky, Virginia, West Virginia, Ohio, and Pennsylvania in the spread of opioid use. We identiﬁed these areas

<!-- b000370 | prose | pages [22] -->
as epicenters from where the problem emanates. These are Doddridge, Harrison, Marion, Morgan, Bracken, Carroll, Harlan, Gallatin, Campbell and Mecklenburg. Our model also determined the 30 most correlated socioeconomic factors in opioid abuse. We believe that policies targeting these factors can indirectly aﬀect opioid crisis.

<!-- b000371 | prose | pages [22] -->
With our model, we tested the eﬀects of limiting the inﬂuence of the identiﬁed epicenters

<!-- b000372 | prose | pages [22] -->
and the results were notably positive. Along with targeting these, we believe that resources should be directed to target features of the socioeconomic proﬁle that are highly correlated with opioid use. Below, we have summarized a few strategies that we think will decrease opioid abuse by targeting the epicenters and the socioeconomic proﬁle of these ﬁve states.

<!-- b000373 | prose | pages [22] -->
Firstly, we suggest directing resources to drug abuse prevention, education programs, and increasing rehabilitation services at the epicenters. We found that, when the prevalence of opioids were cut severely in 2010 in the 10 counties identiﬁed as epicenters, nearly 90 percent of opioid reports disappeared in 6 years. This demonstrates the eﬀectiveness of eliminating opioid use in these epicenters. We realize that it is diﬃcult to reduce the opioid problem in any county to zero instantly, but we believe that targeting these counties will have a ripple eﬀect on the entire region. This will allow for the problem to be combated considerably more eﬃciently than before.

<!-- b000374 | prose | pages [22] -->
Secondly, we suggest increasing border control near these epicenters. When we eliminated communication between the epicenters and the other counties i.e, decreased the inﬂuence of the epicenters on other counties, the results were equally staggering. Our model showed that by eliminating drug ﬂow in and out of these 10 counties, we were able to cut the number of infected counties by 85% in 6 years. We believe that this decrease in opioid inﬂuence could be mimicked through border control along the major roadways in these counties and at state border. This strategy is formulated based on the observation that epicenters are generally located near large highways, thus providing them more inﬂuence in the spread of opioids. Border control would decrease the ability of opioids to ﬂow across state borders along these major roadways and elsewhere, decreasing the inﬂuence these high inﬂuence counties have on the spread of opioid use.

<!-- b000375 | prose | pages [22] -->
Thirdly, we suggest advertising targeted at seniors older than 65 about the dangers of addiction

<!-- b000376 | furniture | pages [23] -->
Team #1901213

<!-- b000377 | furniture | pages [23] -->
Page 22 of 29

<!-- b000378 | prose | pages [23] -->
and the risk presented by teenagers consuming opioids. In our model, one of the highest correlated factors in opioid use is households where seniors are taking care of children under 18. This is likely due to the fact that seniors are more likely than other groups to experience chronic pain, and thus receive a prescription of opioids, which comes with a possibility of addiction. By extension, many of the children in these households have greater access to opioids due to their presence in the household, and consume these opioids for recreational purposes. We tested this hypothesis, and found that when we decreased the proportion of these households by half, the number of infected counties decreases by nearly 90 percent. We understand that while it is very diﬃcult to reduce the number of seniors older than 65

<!-- b000379 | prose | pages [23] -->
taking care of children, it is possible to create informative advertising targeted to this group to make them more aware of the problem. This advertising, placed on channels with high viewership by seniors, would warn them of the dangers of addiction.

<!-- b000380 | prose | pages [23] -->
Fourthly, we suggest encouraging health plans for veterans to include physical therapy, in addition to rehabilitation for those already addicted, as opposed to prescribed opioids. Our model identiﬁed the veteran population as a highly correlated group. We attribute this to the fact that veterans are frequently prescribed opioids to deal with the traumas of war and chronic pain. When we lowered the fraction of veterans in each county to half in our model, the results were shockingly eﬀective with no infected counties. Therefore, we believe that by reducing the destructive relationship between veterans and opioids, we can dramatically reverse the opioid problem. We suggest that veterans be presented better access to physical therapy or other alternative treatments rather than the prescription of opioids. This could be done by encouraging health plans for veterans to include physical therapy. Not only would this limit the connection between this group and opioid use, but it would also decrease potential access to opioids by other groups.

<!-- b000381 | prose | pages [23] -->
Finally, we suggest making education more accessible to everyone.

<!-- b000382 | prose | pages [23] -->
Our model showed a negative correlation between people with a bachelor’s degree and opioid abuse. This demonstrates that people who are educated enough to know the potential drawbacks of long term opioid use will be at lower risk to try them for recreational purposes. When we reduced the number of people with a bachelor’s degree by half, the number of infected counties nearly doubled its previous value. With this in mind, general education of all people on the dangers of opioids will achieve a similar eﬀect. Apart from making education more accessible, we also suggest using television and other media to advertise the overall harm that can be done by opioid use, the overall education of the population with regard to prescription opioids and heroin will increase, resulting in less impulsive decisions to use them without need. While this will not raise the percentage of formally educated people in the region, we believe that it will exhibit a similar change to that predicted in our model.

<!-- b000383 | prose | pages [23] -->
We wholeheartedly hope you consider our suggestions, which will help this country decrease

<!-- b000384 | prose | pages [23] -->
the inﬂuence of an epidemic that has claimed thousands of lives, and millions more currently under the grip of prescription opioids and heroin.

<!-- b000385 | prose | pages [23] -->
Thank You,

<!-- b000386 | furniture | pages [23] -->
Team #1901213

<!-- b000387 | furniture | pages [24] -->
Team #1901213

<!-- b000388 | furniture | pages [24] -->
Page 23 of 29

<!-- b000389 | heading | pages [24] -->
References

<!-- b000390 | references | pages [24] -->
[1] A. S. of Addiction Medicine, “Opioid addiction, 2016 facts & ﬁgures.” https://www.asam.

<!-- b000391 | references | pages [24] -->
org/docs/default-source/advocacy/opioid-addiction-disease-facts-figures.

<!-- b000392 | references | pages [24] -->
pdf, 2016.

<!-- b000393 | references | pages [24] -->
[2] “Cdc guideline for prescribing opioids for chronic pain united states, 2016 — mmwr.”

<!-- b000394 | references | pages [24] -->
https://www.cdc.gov/mmwr/volumes/65/rr/rr6501e1.htm?CDC_AA_refVal=https%

<!-- b000395 | references | pages [24] -->
3A%2F%2Fwww.cdc.gov%2Fmmwr%2Fvolumes%2F65%2Frr%2Frr6501e1er.htm,

<!-- b000396 | references | pages [24] -->
2016.

<!-- b000397 | references | pages [24] -->
March

<!-- b000398 | references | pages [24] -->
[3] N. Volkow, “Addressing the opioid crisis means confronting socioeconomic disparities,”

<!-- b000399 | references | pages [24] -->
2017.

<!-- b000400 | references | pages [24] -->
[4] J.

<!-- b000401 | references | pages [24] -->
Roth,

<!-- b000402 | references | pages [24] -->
“County

<!-- b000403 | references | pages [24] -->
distance

<!-- b000404 | references | pages [24] -->
county-distance-database.html, 2016.

<!-- b000405 | references | pages [24] -->
database.”

<!-- b000406 | references | pages [24] -->
https://www.nber.org/data/

<!-- b000407 | references | pages [24] -->
[5] J. Kingman, “Markov population processes,” Journal of Applied Probability, vol. 6, no. 1,

<!-- b000408 | references | pages [24] -->
pp. 1–18, 1969.

<!-- b000409 | references | pages [24] -->
[6] A. D. Barbour, “On a functional central limit theorem for markov population processes,”

<!-- b000410 | references | pages [24] -->
Advances in Applied Probability, vol. 6, no. 1, pp. 21–39, 1974.

<!-- b000411 | references | pages [24] -->
[7] G. J. Gibson, “Markov chain monte carlo methods for ﬁtting spatiotemporal stochastic

<!-- b000412 | references | pages [24] -->
models in plant epidemiology,” Journal of the Royal Statistical Society: Series C (Applied

<!-- b000413 | references | pages [24] -->
Statistics), vol. 46, no. 2, pp. 215–233, 1997.

<!-- b000414 | references | pages [24] -->
[8] S. Yakowitz, R. Hayes, and J. Gani, “Automatic learning for dynamic markov ﬁelds with

<!-- b000415 | references | pages [24] -->
application to epidemiology,” Operations research, vol. 40, no. 5, pp. 867–876, 1992.

<!-- b000416 | references | pages [24] -->
[9] J. Benesty, J. Chen, Y. Huang, and I. Cohen, “Pearson correlation coeﬃcient,” in Noise

<!-- b000417 | references | pages [24] -->
reduction in speech processing, pp. 1–4, Springer, 2009.

<!-- b000418 | references | pages [24] -->
[10] C. Robert, Machine learning, a probabilistic perspective. Taylor & Francis, 2014.

<!-- b000419 | references | pages [24] -->
[11] J. Frost, “How high does r-squared need to be?,” 2018.

<!-- b000420 | references | pages [24] -->
[12] A. Baldini, “A review of potential adverse eﬀects of long-term opioid therapy: A

<!-- b000421 | references | pages [24] -->
practitioners guide,” 2012.

<!-- b000422 | references | pages [24] -->
[13] J. Garami, “Intolerance of uncertainty in opioid dependency relationship with trait

<!-- b000423 | references | pages [24] -->
anxiety and impulsivity,” 2017.

<!-- b000424 | references | pages [24] -->
[14] S. Spampinato, V. Locatelli, D. Cocchi, L. Vicentini, S. Bajusz, S. Ferri, and E. E.

<!-- b000425 | references | pages [24] -->
M¨uller, “Involvement of brain serotonin in the prolactin-releasing eﬀect of opioid peptides,”

<!-- b000426 | references | pages [24] -->
Endocrinology, vol. 105, no. 1, pp. 163–170, 1979.

<!-- b000427 | references | pages [24] -->
[15] N. A. Battista, L. B. Pearcy, and W. C. Strickland, “Modeling the opioid epidemic,”

<!-- b000428 | references | pages [24] -->
arXiv preprint arXiv:1711.03658, 2017.

<!-- b000429 | references | pages [24] -->
addiction:

<!-- b000430 | references | pages [24] -->
[16] “Preventing

<!-- b000431 | references | pages [24] -->
drug

<!-- b000432 | references | pages [24] -->
misuse

<!-- b000433 | references | pages [24] -->
and

<!-- b000434 | references | pages [24] -->
The

<!-- b000435 | references | pages [24] -->
best

<!-- b000436 | references | pages [24] -->
strategy

<!-- b000437 | references | pages [24] -->
—

<!-- b000438 | references | pages [24] -->
na-

<!-- b000439 | references | pages [24] -->
abuse

<!-- b000440 | references | pages [24] -->
tional

<!-- b000441 | references | pages [24] -->
institute

<!-- b000442 | references | pages [24] -->
on

<!-- b000443 | references | pages [24] -->
drug

<!-- b000444 | references | pages [24] -->
(nida).”

<!-- b000445 | references | pages [24] -->
https://www.drugabuse.

<!-- b000446 | furniture | pages [25] -->
Team #1901213

<!-- b000447 | furniture | pages [25] -->
Page 24 of 29

<!-- b000448 | references | pages [25] -->
gov/publications/drugs-brains-behavior-science-addiction/

<!-- b000449 | references | pages [25] -->
preventing-drug-misuse-addiction-best-strategy.

<!-- b000450 | references | pages [25] -->
[17] “Preventing

<!-- b000451 | references | pages [25] -->
drug

<!-- b000452 | references | pages [25] -->
abuse

<!-- b000453 | references | pages [25] -->
and

<!-- b000454 | references | pages [25] -->
excessive

<!-- b000455 | references | pages [25] -->
alcohol

<!-- b000456 | references | pages [25] -->
use

<!-- b000457 | references | pages [25] -->
—

<!-- b000458 | references | pages [25] -->
surgeongeneral.gov.”

<!-- b000459 | references | pages [25] -->
https://www.surgeongeneral.gov/priorities/prevention/strategy/

<!-- b000460 | references | pages [25] -->
preventing-drug-abuse-excessive-alcohol-use.html. (Accessed on 01/28/2019).

<!-- b000461 | references | pages [25] -->
[18] “Curbing opioid addiction needs more than new drugs,” 2018.

<!-- b000462 | references | pages [25] -->
[19] S. Pei, S. Kandula, W. Yang, and J. Shaman, “Forecasting the spatial transmission

<!-- b000463 | references | pages [25] -->
of inﬂuenza in the united states,” Proceedings of the National Academy of Sciences,

<!-- b000464 | references | pages [25] -->
p. 201708856, 2018.

<!-- b000465 | references | pages [25] -->
[20] A. L. Pitt, K. Humphreys, and M. L. Brandeau, “Modeling health beneﬁts and harms

<!-- b000466 | references | pages [25] -->
of public policy responses to the us opioid epidemic,” American journal of public health,

<!-- b000467 | references | pages [25] -->
vol. 108, no. 10, pp. 1394–1400, 2018.

<!-- b000468 | furniture | pages [26] -->
Team #1901213

<!-- b000469 | furniture | pages [26] -->
Page 25 of 29

<!-- b000470 | heading | pages [26] -->
Appendix: Epicenters and vulnerable counties

<!-- b000471 | prose | pages [26] -->
A

<!-- b000472 | prose | pages [26] -->
Vulnerable Location 1 County State Scioto Ohio Montgomery 2 Ohio Philadelphia 3 4 5 6 7 8 9 10 Pennsylvania Kanawha West Virginia Pulaski Kentucky Pike Kentucky Laurel Kentucky Hamilton Ohio Bell Kentucky Jeﬀerson Kentucky

<!-- b000473 | caption | pages [26] -->
Table 2: Vulnerable Counties by Demographic Model from 2010-2016

<!-- b000474 | prose | pages [26] -->
Vulnerable Location 1 2 County State Kanawha West Virginia Scioto Ohio Montgomery 3 4 5 6 7 8 9 10 Ohio Pike Kentucky Whitley Kentucky Lincoln Kentucky Jackson Kentucky Marion Ohio Richmond Virginia Pulaski Kentucky

<!-- b000475 | caption | pages [26] -->
Table 3: Vulnerable Counties by Demographic Model in 2017

<!-- b000476 | furniture | pages [27] -->
Team #1901213

<!-- b000477 | prose | pages [27] -->
Epicenter County 1 Carroll 2 Bracken 3 Morgan 4 Harlan 5 Marion 6 Doddridge 7 Gallatin 8 Harrison 9 Mecklenburg 10 Campbell

<!-- b000478 | furniture | pages [27] -->
Page 26 of 29

<!-- b000479 | prose | pages [27] -->
State Border Kentucky A Kentucky D West Virginia B Kentucky C West Virginia E West Virginia E Kentucky A West Virginia E Virginia K Kentucky D

<!-- b000480 | caption | pages [27] -->
Table 4: Epicenters Ranked by QA Element-wise Product

<!-- b000481 | prose | pages [27] -->
Epicenter County 1 Carroll 2 Morgan 3 Harlan 4 Campbell 5 Harrison 6 Marion 7 Gallatin 8 Hampshire 9 Bracken 10 Doddridge State Border Kentucky A West Virginia B Kentucky C Kentucky D West Virginia E West Virginia E Kentucky A West Virginia B Kentucky D West Virginia E

<!-- b000482 | caption | pages [27] -->
Table 5: Epicenters Ranked by QA Product

<!-- b000483 | prose | pages [27] -->
Epicenter County 1 Carroll 2 Harlan 3 Morgan 4 Lee 5 Bracken 6 Campbell 7 Harrison 8 Marion 9 Allen 10 Nicholas State Border Kentucky A Kentucky C West Virginia B Kentucky G Kentucky D Kentucky D West Virginia E West Virginia E Kentucky F West Virginia H

<!-- b000484 | caption | pages [27] -->
Table 6: Epicenters Ranked BY Q Alone

<!-- b000485 | furniture | pages [28] -->
Team #1901213

<!-- b000486 | prose | pages [28] -->
Epicenter County 1 Elliot 2 Harlan 3 Bell 4 Lewis 5 Owsley 6 Powell 7 Carroll 8 Lee 9 Bristol 10 Morgan

<!-- b000487 | furniture | pages [28] -->
Page 27 of 29

<!-- b000488 | prose | pages [28] -->
State Border Kentucky I Kentucky C Kentucky C West Virginia E Kentucky G Kentucky G Kentucky A Kentucky G Virginia J West Virginia B

<!-- b000489 | caption | pages [28] -->
Table 7: Epicenters Ranked by |Q|

<!-- b000490 | furniture | pages [29] -->
Team #1901213

<!-- b000491 | furniture | pages [29] -->
Page 28 of 29

<!-- b000492 | prose | pages [29] -->
B

<!-- b000493 | heading | pages [29] -->
Appendix: Top 30 highly correlated socioeconomic factors

<!-- b000494 | prose | pages [29] -->
Here are the top 30 highly correlated socioeconomic factors, in no particular order:

<!-- b000495 | prose | pages [29] -->
• Number of grandparents responsible for own grandchildren under 18 years • Number of grandparents living with own grandchildren under 18 years • Number of females 15 years and over • Number of males 15 years and over • Number of people ever married • Number of people now married • Civilian population 18 years and over • Population 3 years and over enrolled in school • Total population • Number of women 15 to 50 years old who had a birth in the past 12 months • Number of people with a bachelor’s degree • Number of people with Ukrainian ancestors • Number of people with Russian ancestors • Number of people with Italian ancestors • Number of people with Arab ancestors • Number of people who speak Asian and Paciﬁc Islander languages • Number of people who speak English and Asian and Paciﬁc Islander languages • Number of people who lived in a diﬀerent house, but same county • Number of natives who entered the state before 2010 • Number of people born outside the United States who entered the state before 2010 • Number of foreign born who entered before 2010 • The world region of foreign born population • Citizenship status of foreign-born population • Disability status of 18 to 64 years • Disability status of all civilians • Disability status of 65 years and over • Disability status of under 18 years • Households with a spouse • Family households with a married couple • Houses with computers and broadband use

<!-- b000496 | furniture | pages [30] -->
Team #1901213

<!-- b000497 | furniture | pages [30] -->
Page 29 of 29

<!-- b000498 | prose | pages [30] -->
C

<!-- b000499 | heading | pages [30] -->
Appendix: Supplementary images

<!-- b000500 | caption | pages [30] -->
Figure 3: Spread of the opioid crisis from year 2010 to 2016. The legend tells the number of drug

<!-- b000501 | prose | pages [30] -->
reports per 100 people in each county. A darker green indicates a higher number of drug reports per 100 people.
