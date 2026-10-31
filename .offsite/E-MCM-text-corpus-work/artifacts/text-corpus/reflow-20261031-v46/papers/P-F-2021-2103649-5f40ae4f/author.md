MCM/ICM

Summary Sheet

Summary

Higher education system is an essential part of the development of a country. It directly undertakes the national scientiﬁc research tasks, providing most of the major research results. More importantly, the system has been cultivating talents for the future, which ensures the nation’s future development.

Every country has its unique higher education system, with the corresponding strengths and weak- nesses. It is necessary to analyze and evaluate a system comprehensively, continuing its strengths and adjusting its weaknesses. However, the discrepancy between systems of different countries has made it hard to build a uniform evaluation standard for every country. In this article, we build a suite of measurement models to assess the health and sustainability of higher education systems.

To measure the health status of each country’s system, we select raw data for six main factors

and fourteen indicators of ﬁfty countries, with the time period from 2009 to 2018. Then we verify the distribution law of the data and choose 80% quantile as the health range for each indicator. Afterwards, we use the analytic hierachy process (AHP) to determine the weight for each indicator. We introduce the concept of overall point gain (OPG), representing the general health status of a system.

We also establish the method for examine sustainability by using DEA - Malmquist model. It is a highly objective model, commonly applied in time series analysis. According to the comparisons of the relative efﬁciency between different years, we can obtain the efﬁciency change trend. Then we can analyze the sustainability with the trend.

Then we select ﬁve countries as analysis objects: the US, the UK, Germany, Japan, India. With our models, we evaluate the health and sustainability of them. Our conclusion is: The US’ system is sub-healthy and sustainable, the UK’s system is sub-healthy with poor sustainability, the Germany’s system is completely healthy with excellent sustainability, the Japan’s system is unhealthy but sus- tainable, the India’s system is unhealthy and unsustainable. Since the higher education system of India has much room for improvement, we choose India to analyze further.

First, we measure India’s current system. Limited resources, large population, and economic pres- sure cause the low enrollment rate and high unemployment rate. Second, based on the analysis above, we propose our three-phase vision, including short-term, mid-term and long-term. For our vision, we propose some targeted policies. In short-term policies, we increase the indicators quickly. The policies includes to reduce the cost of education for the poor, to lower the minimum wage standard, and to Lower the admission standards for foreign students. In long-term policies, we take the social situation of India into considered. The policies includes Family planning, Economic structure transformation, and Educational environment improvement. We also use Markov Chain to predict the implementa- tion of policies in the future, which can reﬂect the ﬂexibility of policies. Then, we assess the real-world impacts and the difﬁculty to the policy implementation.

Finally, we discuss the strengths and weaknesses of our models, leaving room for further studies.

targeted policies, Markov chain

关注数学模型

7 Model Strengths and Weaknesses

23

7.1 Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23

7.2 Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23

Appendices

24

Appendix A Codes

24 微信号：MATHmodels A.1 Code for AHP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24

A.2 Code for Malkov Chain . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25

关注数学模型

1 Introduction

1.1 Background

The higher education system is the core competitiveness of a country’s education system. The sys- tem not only undertakes the task of cultivating talents for the country, but also shoulders its unique 微信公众号：数学模型 economic and research responsibilities. Therefore, it is of great signiﬁcance to establish a model that can fully evaluate the higher education system.

However, countries in the world have different national conditions, and the problems they face in higher education construction are also different. Just building an evaluation model is far from enough. How to determine the weak part of a country’s higher education and how to give reasonable policies in accordance with the national conditions is a question worth pondering.

1.2 Our Works

In order to deal with the situation, we have completed the following tasks:

• We select raw data for 14 indicators of 50 countries with the time period from 2009 to 2018. Then 微信号：MATHmodels we verify the distribution law of the data through Kolmogorov - Smirnov test and choose 80% quantile as the acceptance range (health range). This quantile is a choice based on our basic assumptions.

• We use the analytic hierachy process to determine the weight for each indicator. The result can be used to measure the health status for speciﬁc countries. We also establish the method for examine sustainability using DEA - Malmquist model.

• Then we apply our models to ﬁve selected countries to test the efﬁciency. By applying the models, we make brief diagnosis for their health and sustainability conditions.

• By comparing the test results of ﬁve countries, we selected India, which has a larger upside po- tential, as the case we study. After evaluating its status, we build our vision and develop targeted policies. We then use Markov chain to predict the effect of our polies and draw the timeline for prediction. Afterwards, we analyzed the impact of the policy on the actual situation and possible obstacles.

2 General Assumption and Symbol Explanation

2.1 General Assumption

In order to enable the model to accurately reﬂect the health status of higher education system, we analogize the health evaluation method of the medical system and make the following assumptions.

1. Statistics we collect from the website are actual and reliable.

2. The overall health of higher education is only related to our evaluation indicators.

3. The indicators we choose possess the same distribution law as the population of higher educa- tion system, so the overall situation can be estimated through samples.

4. The population of the higher education system conforms to the hypothetical distribution law and can be used to measure the health status. The population does not actually exist, it is not inconsistent with the totality of all countries.

5. Similar to physical examination indicators, there is a speciﬁc interval that determines whether

关注数学模型 the values for indicators are healthy.

6. Within a certain period of time, some indicators will not be affected by the implementation of policies and can be regarded as constants.

Based on the above assumptions, we have selected a reasonable data set and used corresponding processing methods to establish a comprehensive evaluation standard for the higher education system.

微信公众号：数学模型

2.2 Symbol Explanation

Name Explanation Iij Input indicators for sustainability analysis Oij Output indicators for sustainability ananlysis Sig. Signiﬁcance level for K-S test OPG Overall point gain {pi} 0 - 1 sequence showing the health status PIE Policy implementation effect BU Buffer for modeling parameters DCN Difference between the current value and the normal value of the index

微信号：MATHmodels

3 Main Factors and Data Selection

3.1 Main Factors

In order to make a sound assessment of the higher education system, we need to measure its health and sustainability. Similar to the deﬁnation of biological health, the health of a system refers to its ability to perform normal functions and respond to changes in the outside world. For a healthy higher education system, it needs to have the normal function of education, and be able to repair and renew itself [1]. The sustainability consists of normativity, equity, integration, and dynamism [2], it measures the ability of a system to maintain and update itself.

Based on the above deﬁnitions, we have compiled the six factors that measure the higher education system, which will be described below.

3.1.1 Investment

The investment factor measures a government’s willingness to invest in higher education, making it one of the most important indicators. With limited resources, the more the government invests in higher education, the more the country attaches importance to it. This factor will be qualiﬁed through two indicators: government expenditure on tertiary education and research and development expen- diture. The former one measures how willing the country wants to enhance its higher education, the latter one shows the government support on further education.

3.1.2 Accessibility

Accessibility measures the difﬁculty of receiving higher education in a country. Higher accessibility can reﬂect a better construction for the system. In this part, we take the admission rate and number of higher education institutions per capita as detailed indicators. The admission rate can intuitively show the degree of higher education of the right-age population, and can be used to measure the perfection of the education system. The number of higher education institutions per capita can reﬂect the difﬁculty of individual receiving higher education, which is another description from the micro level.

关注数学模型

3.1.3 Education Level

Education level (written as "E-level" below) is the evaluation for teaching level in different countries. This is the measure of system efﬁciency. In this section, we have selected three indicators as represen- tatives. The number of top 1000 universities per capita reﬂects the country’s high-level educational capabilities. This determines the academic reputation of the country. Net ﬂow of internationally mo- 微信公众号：数学模型 bile students works as an important output indicator for education sustainability. When the indicator is negative, it means that the current country’s higher education system is relatively weak. The third indicator, pupil-teacher ratio, measures the distribution of educational resources in the country. The lower the ratio, the more educational resources the individual gets.

3.1.4 Research Level

Research level (written as "R-level" below) is the evaluation for research level. This part is relatively complicated, so we discribe it with three indicators: highly cited paper per institution, nature-index research per institution, and patent per institution. The three indicators measure the level of scientiﬁc research education, the level of experimental research and the level of applied research. Considering the values of these three indicators comprehensively, we can infer the corresponding research level through the research results. 微信号：MATHmodels

3.1.5 Educational Equity

Educational equity (written as "equity" below) is a measure of achievement, fairness, and opportu- nity in education [3]. It consists of socioeconomic equity, gender equity and racial equity. Since racial inequality is not a global phenomenon, and there is no uniﬁed evaluation standard, this element will not be considered.

We use the ratio of average tuition fee and GDP per capita to evaluate the socioeconomic equity, and gender equity is measured with school enrollment gender parity index (GPI).

3.1.6 Attraction

In addition to the aforementioned reasons, the attraction of the higher education system is also an important evaluation factor for healthy and sustainable development. In general, we evaluate the attractiveness through research interest and educational interest. The attractiveness of research comes from the collision of excellent thinking and the birth of inspiration, which can be measured by academic exchanges. We initially selected the number of academic conferences and the number of outstanding award winners as indicators for this content. However, academic conferences are highly mobile and are not suitable for national assessments, so we chose the award winners (including Nobel, Turing and Fields) as the indicator. Educational interest is measured by Employment rate of people with higher education1. Too low the employment rate indicates that the national education system is inperfect, while too high shows that the system is not attractive enough.

3.2 Data Selection

To assess health status and sustainable development, we use the same set of data but different evaluation methods. To assess the health status, we will calculate the weight of the data and list the main indicators, thereby constructing a conﬁdence interval similar to the pathology test.

The method of assessing sustainability is slightly different. We select indicators for evaluating sev- eral aspects of sustainability based on the sustainability principle discussed before and use them as

1In the database of World Bank, this indicator is named as the labor force with advanced education (% of total working-age population with advanced education).

关注数学模型 output variables. The remaining indicators will be used as input variables to determine changes in output indicators. In short, we treat decision variables as input variables and reﬂection variables as output variables to measure sustainability. When assessing sustainability, we will select appropriate indicators from the given input and output.

Here is a table of selected indicators. The letter ‘P’ for impact column means the indicator has a positive effect on higher education. ‘N’ refers to the opposite. Certain indicators will have a negative 微信公众号：数学模型 impact on the results when they are too high or too low, so we allocate letter ‘B’ to them.

For input variables, they are encoded with Iij, for the output ones, we use symbol Oij as the repre- sentatives. ‘i’ shows the number of each indicator and ‘j’ represents the country.

Factor Indicator Symbol Unit Impact D.S.

I1j Investment Government expenditure on tertiary educa- % P a tion as % Of GDP I2j Research and development expenditure (% of % P a GDP) I3j Accessibility School enrollment, tertiary (% gross) % P a I4j Number of higher education institutions per - P b capita 微信号：MATHmodels I5j E-level Number of top 1000 universities per capita - P c O1j Net ﬂow ratio of internationally mobile stu- % P a dents (inbound - outbound) I6j Pupil-teacher ratio, tertiary - N a O2j R-level Highly cited paper per institution - P d O3j Nature-index research per institution - P e O4j Patent per institution - P a O5j Equity Ratio of average tuition fee and GDP per - N c capita I7j School enrollment, tertiary (gross), gender - B a parity index (GPI) O6j Attraction Important award winners - P b O7j The labor force with advanced education (% % B a of total working-age population with ad- vanced education)

Note: D.S. is the abstract of data source. D.S. a is collected from World Bank World Development Indicators [4] and Education Statistics - All Indicators [5]. D.S. b is quoted from the corresponding page of Wikipedia. D.S. c is compiled from the public information of QS Rankings [6]. D.S. d and e come from webofscience [?] and Nature-index [7], respectively.

Considering assumption 3 and 4, we randomly sample from countries with more complete higher education systems and investigate their indicators from 2009 to 2018. The 50 selected samples are shown below.

Countries 1 2 3 4 5 1 Argentina Czech Republic Ireland New Zealand South Korea 2 Australia Denmark Israel Norway Spain 3 Austria Egypt Italy Pakistan Sweden 4 Belarus Estonia Japan Philippines Switzerland 5 Belgium Finland Kazakhstan Poland Thailand 6 Brazil France Lebanon Portugal Turkey 7 Canada Germany Malaysia Russia Ukraine 8 Chile Greece Mexico Saudi Arabia United Arab Emirates 9 China India Mongolia Singapore United Kindom 10 Colombia Iodonesia Netherlands South Africa United States

Here is a map showing the countries we select. 关注数学模型 微信公众号：数学模型

With reference to the indicators in Table 1, we surveyed 50 countries and completed the standard- ization of the data, making preparations for the establishment of the model.

4 Diagnosis Methods: Models for Health and Sustainability

微信号：MATHmodels In this section, we build up the health model and sustainability model for higher education system. Using both models together, we are able to run the physical examination and make a diagnosis of the health and sustainability of each country. The process can be described with the following graph.

Selection of Health Range

Weights of Analysis of AHP Health Different Factors Each Factor

Data DEA- Efficiency Malmquist Sustainability Change Trend

Model

Results

Diagnosis methods

Modeling

4.1 Health Model

During the physical examination, the doctor usually checks the patient’s various indicators and judges whether they are in the normal range. These indicators possess different weights, and indicators with larger weights have a greater impact on health conditions. We use similar methods to measure the health of the higher education system. Based on the previous assumptions, we determined the corresponding health range for each indicator, and determined the weight of each indicator through Analytic Hierarchy Process. The overall health status and the health status of each factor will be given through these analyses.

4.1.1 Determine the Weight of Indicators

The main method we use to determine the weight is analytic hierachy process.

关注数学模型 Consistency Weights of Factors Pairwise Comparison Maximum True Test Different Factors Selection Comparisons Matrix Eigenvalue 微信公众号：数学模型 False

Analytic Hierarchy Process (AHP) is an accurate approach for quantifying the weights of decision criteria, widely used in different decision situations, in ﬁelds like government, business, healthcare, shipbuilding, industry and education [8]. In our analysis, we use this method to determine weights of different main factors. Similarly, we determine the weights of different indicators in each factor. The following are the steps.

• Factors selection

We have selected several main factors previously. For each main factor, we have chosen some 微信号：MATHmodels indicators as well.

• Pairwise comparisons between different factors

According to pairwise comparisons, we establish priorities among the factors. We think that the importance of main factors satisﬁes the following relationship:

Investment ≈Access ⩾Education ≈Research ⩾Equity ≈Attraction

• Calculation of comparison matrix With the relationship discussed before, we get our comparison matrix (bij)6×6.

F1 F2 F3 F4 F5 F6   1 1 1 1 1 F1 1 3 5 5 7 9   1 1 1 1 F2 3 1   3 3 5 7   1 1 F3 5 3 1 1   3 5 ,   1 1 F4 5 3 1 1   3 5   1 F5 7 5 3 3 1 3 F6 9 7 5 5 3 1

where Fi for i = 1, 2, · · · , 6 represent investment, access, education, research, equity, attraction respectively.

• Consistency Test

We can calculate the eigenvalues and eigenvectors of the matrix before. Next we need to perform consistency test with the maximum eigenvalue λmax.

CI = λmax −n , (1) n −1 CR = CI RI , (2)

where RI = 1.24 when n = 6. For the above comparison matrix, we obtain CR = 0.0416 ⩽0.1, thus the comparison matrix is acceptable.

• Calculation of weights Passing the consistency test, we can get the weights of main factors by the eigenvector corresponding to the maximum eigenvalue: investment (0.4615), access (0.2402),

关注数学模型 education (0.1095), research (0.1095), equity(0.0515), attraction (0.0515) .

With the same method, we get the weights of different indicators of each factor, shown in the fol- lowing graph.

Weight of each indicator

Top 1000 universities: 5.91% ​Top 1000 universities: 5.91% Higher education ​Higher education 微信公众号：数学模型 ​institutions: 12.01% ​institutions: 12.01% Student-teacher ratio: 3.25% ​Student-teacher ratio: 3.25% Net flow ratio: 1.79% ​Net flow ratio: 1.79% Highly cited paper: 6.37% ​Highly cited paper: 6.37% School enrollment: 12.01% ​School enrollment: 12.01% Nature-index: 3.38% ​Nature-index: 3.38% Education ​Education Access ​Access Patent: 1.2% ​Patent: 1.2% Research ​Research Employment rate: 3.6% ​Employment rate: 3.6% Attraction ​Attraction Equity ​Equity Major award winners: 1.55% ​Major award winners: 1.55% Investment ​Investment Gender parity index: 1.55% ​Gender parity index: 1.55% Tuition fee: 3.6% ​Tuition fee: 3.6% Education: 23.075% ​Education: 23.075%

Research and ​Research and ​development: 23.075% ​development: 23.075%

微信号：MATHmodels Through weight analysis, we can get the rankings of indicators according to weight. The top-ranked indicator is called the main indicator, which has a huge impact on the overall health. The lower-ranked indicators are called secondary indicators, which have little impact on the overall health, but their cumulative effects cannot be ignored.

4.1.2 Select Health Range

Most countries with complete higher education systems have healthy higher education. By apply- ing analysis from QS Rankings, we ﬁx the ratio of healthy higher education to 0.8. This shows that 80% of the population is healthy. Based on the assumptions, we have developed the following principles for healthy range selection.

• Positive indicators: Select the sample data from high to low 80% quantile as the estimator of the overall lower bound2.

• Negative indicators: Select the sample data from low to high 80% quantile as the estimator of the overall upper bound.

• Others: Estimate the distribution law of the population through the sample and determine the interval.

The health range corresponding to positive and negative indicators is better given, and what needs to be considered is the distribution law of other indicators: GPI and employment rate. By drawing the frequency histograms of these two indicators, we found that they have a law similar to the normal distribution. In order to verify this conjecture, we performed the Kolmogorov - Smirnov test (K-S test) [9] on these two indicators using SPSS. Due to space limitations, the detailed principles of K-S test will not be discussed here, only the results will be shown.

Given the signiﬁcance level α = 0.05, we obtain the results of the K-S test for the two indicators, as shown below. Since the signiﬁcance levels for both indicators are above α, we can conclude that they all passed the K-S test.

Here are the Q-Q plots of the two data to verify the correctness of the results. It can be seen that the data points are distributed near the straight line, and the results of the K-S test can be accepted.

2Note that the net ﬂow ratio is slightly different from other indicators. When it is negative, it means that this country’s

关注数学模型 indicator is unhealthy. With this in mind, the lower bound of this indicator is set to 0.

Tests of Normality Tests of Normality Kolmogorov-Smirnov Shapiro-Wilk Kolmogorov-Smirnov Shapiro-Wilk Statistic df Sig. Statistic df Sig. Statistic df Sig. Statistic df Sig.

0.087 0.200 GPI 47 47 0.981 0.615 Empl. Rate 0.122 50 0.061 0.964 50 0.129

Normal Q-Q Plot of GPI Normal Q-Q Plot of Empl. Rate 微信公众号：数学模型 3

2 2

1 Expected Normal Expected Normal 0 0

-1 -2

-2

-3 -4 0.8 1.0 1.2 1.4 60 70 80 90 Observed Value Observed Value

微信号：MATHmodels In result, the acceptable health range of the two can be given by using normal distribution proper- ties.

Indicator Upper Bound Lower Bound Education expenditure 100 1 Research and development expenditure 100 0.6 School enrollment - 50 1.63 × 10−6 Number of higher education institutions per capita - 1.15 × 10−7 Number of top 1000 universities per capita - Net ﬂow ratio - 0 Pupil-teacher ratio 22 0 Highly cited paper per institution - 1 Nature-index per institution - 0.76 Patent per institution - 3.27 Average tuition fee ratio 0.54 - GPI 1.344 0.966 Major award winners - 2 Employment rate 84.57 68.98

4.1.3 Diagnosis of Health Conditions

We use a simple acceptance/rejection model (0-1 model) to determine the health conditions.

The overall health condition can be measured with point gain and the occuring problem can be located. For each indicator i, if the value falls in the range of health, the point pi = 1, otherwise pi = 0. ωi is the weight of indicator i.

We caculate the point gain with the equation below:

14 ∑ OPG = ωipi (3) i=1

Overall point gain (OPG) describes the health condition of a system, but only when its value is 1 can it prove that the system is completely healthy. If the OPG value is too low, it means that the countrys education system has at least one main indicator or a large number of secondary indicators that are

关注数学模型 wrong.

We have classiﬁed the health status as follows:

• Healthy: OPG = 1, showing that all indicators are normal.

• Sub-healthy: OPG ⩾0.9, showing that the system has small problems.

• Unhealthy: 0.6 ⩽OPG < 0.9, showing that one or more main indicators are wrong, which can 微信公众号：数学模型 be improved.

• Extremely unhealthy: 0.4 ⩽OPG < 0.6, showing that the overall problem of the system is serious, and more reasonable construction of higher education is needed.

• Serious: 0.2 ⩽OPG < 0.4, showing that the higher education system is seriously out of balance and cannot perform its normal functions.

• Bad: OPG ⩽0.2, showing that the country has no higher education system.

The following ﬁgure shows the lower bound for each status more intuitively.

Lower Bound for OPG Rankings 微信号：MATHmodels Basic Distinction Based on Health Status Rank

Healthy

Sub-Healthy

Unhealthy

Extremely Unhealthy

Serious OPG 0 0.2 0.4 0.6 0.8 1

Unhealthy Healthy

4.2 Sustainability analysis with DEA-Malmquist model

4.2.1 Basic DEA model

Data envelopment analysis (DEA) is one of the most common methods in the analysis of the per- formance of universities. There are several models of DEA. Among them, the CCR model by Charnes, Cooper and Rhodes, has a simple form and a complete theory. The model is easy to understand and perform.

Without prior weights on the inputs and outputs, DEA can be used to evaluate the relative efﬁciency among multiple-input and multiple-output different decision making units (DMUs) [10]. In a one- input, one-output situation, efﬁciency is usually deﬁned as the ratio of output over input [11]. Similarly, the efﬁciency is deﬁned as Equation 4:

∑ M ymjumj m=1 θj = , (4) N∑ xnjvnj n=1

关注数学模型 where xnj(n = 1, 2, · · · , N), ymj(m = 1, 2, · · · , M) represent N inputs and M outputs of the jth DMU respectively, with the corresponding input weights and output weights umj, vnj, with all inputs, outputs and weights non-negative.

Thus the analysis to the performance of the system is transformed to the following linear program- ming problem:

∑ M 微信公众号：数学模型 ymjumj m=1 max θj = , N∑ xnjvnj n=1  ∑ M   ymkumj   m=1 ⩽1, k = 1, 2, · · · , K, ∑ N s.t. (5) xnkvnj    n=1  umj, vnj ⩾0, m = 1, 2, · · · , M; n = 1, 2, · · · , N,

where K is the total of DMUs. If the optimal solution of the above problem exists and max θj is 1, then we can judge this DMU is effective, meaning the corresponding ratio of outputs to inputs can be maxmized.

微信号：MATHmodels

4.2.2 DEA-Malmquist model

As discussed above, DEA can be used to measure the relative efﬁciency among a series of DMUs. However, in the analysis of time series, basic CCR model just calculate and compare the values of efﬁciency of different time. It ignores the temporal change of productivity. Therefore, we use DEA- Malmquist model, more commonly applied in time series analysis. This method introduces the Malmquist distance, considering the time-varying productivity. We can make a dynamic analysis to efﬁciency with it.

4.2.3 Sustainability analysis

From DEA-Malmquist model, we obtain the efﬁciency ratio between two adjacent years. The re- sults can be calculated fast by DEAP, a software of DEA related model. If we assume that the efﬁciency of the ﬁrst year were 1, then we can get the temporal trend of efﬁciency. Based on the four aspects of sustainability and the trend, we propose the following criteria:

• If in the last ﬁve years, one country’s efﬁciency has declined for three consecutive years, then its system is not considered sustainable.

• If in the last ﬁve years, one country’s efﬁciency has declined for only two consecutive years, then its system’s sustainability is considered poor.

• If in the last ﬁve years, one country’s efﬁciency has declined for no more than one year, then its system is considered highly sustainable.

In the ﬁrst scenario, we think this system cannot maintain its effectiveness. In the second scenario, the system can sometimes maintain its current situation. Finally, we believe the existence of ﬂuctuation, but a highly sustainable system can recover from its decline quickly.

5 Case Tracking: Model Application on Different Countries

Since the measuring models are completed, we try to apply our models to speciﬁc countries to evaluate their health and sustainability status. We randomly select the following ﬁve countries, and the

situation for each country will be discussed detailedly. 关注数学模型 微信公众号：数学模型

5.1 the United States

We ﬁrst evaluate the current health status of the US compared to the health range in Table 3. The indicator point sequence {pi} and OPG are as follows:

{pi} = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1}, OPG = 0.964 微信号：MATHmodels We found that the average tuition fee ratio of the US is abnormal, making the status of the US sub- healthy. The abnormality of this indicator shows that the cost of education in the United States is high, and the equity of education is not strong enough.

For sustainability, the efﬁciency (2009 to 2018) can be shown in the following plot:

Sustainability Analysis Data for the US 1.5

1.2

0.9

0.6

0.3

0 Year 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018

The efﬁciency turns out to have a steady and growing trend, showing that the higher education in the US is sustainable and innovative.

5.2 the United Kingdom

Similar to the former ways, we ﬁrst evaluate the grade sequence and OPG:

{pi} = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0}, OPG = 0.964

And then the efﬁciency for sustainability:

The health status for the UK is sub-healthy. The employment rate is a little bit higher than the upper bound. This shows that the UK’s vocational education and scientiﬁc research education are not balanced, and need to be improved through policies and teaching methods. The sustainability of UK

关注数学模型 is a bit poor, the policies should be improved actively.

Sustainability Analysis Data for England 1.2

1

0.8

0.6 微信公众号：数学模型 0.4

0.2

0 Year 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018

5.3 Germany

The situation for Germany is slightly different from former countries. For health status, we have:

{pi} = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}, OPG = 1.00 微信号：MATHmodels This means that the higher education system in Germany is completely healthy. As for sustainabil- ity, we have:

Sustainability Analysis Data for Germany 2.5

2

1.5

1

0.5

0 Year 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018

It is a completely growing trend, showing that German system possesses great sustainability.

5.4 Japan

For Japan, the point sequence, OPG and sustainability plot are as follows:

{pi} = {0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1}, OPG = 0.7774

The health status for Japan is unhealthy, causing by the lack of education investment and gender inequalty. However, the sustainability plot shows that the higher education is sustainable, the gov- ernment is trying to deal with the problems and improve its system structure, creating a better future for Japanese education.

5.5 India

Compared with the above-mentioned countries, India’s higher education system has more serious

关注数学模型 problems. This can be reﬂected through the structure of point sequence:

Sustainability Analysis Data for Japan 1.5

1.2

0.9

微信公众号：数学模型 0.6

0.3

0 Year 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018

{pi} = {1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0}, OPG = 0.5783

The health condition for India is extremely unhealthy, resulting in different factors. The problem mainly occurs in accessibility, education level, reasearch level, educational equity, and attraction.

微信号：MATHmodels This shows that there is still much room for improvement in Indian higher education.

As for the sustainability, we have the plot below:

Sustainability Analysis Data for India 1.5

1.2

0.9

0.6

0.3

0 Year 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018

The higher education in India seems to be unstable, presenting a unsustainable development in recent years. The education department should take appropriate actions to deal with it.

6 Treatment Plan: Case Study on the Higher Education System of India

By comparing the ﬁve countries mentioned above, we ﬁnd that the state of higher education in India is worrying. To study the impact of policies on the higher education system, India acts as an ideal sample. In this section, we will treat India as our "patient", give out a complete analysis and determine the treatment plan. After that, we will analyze the feasibility of the plan in combination with reality.

This case study can provide clearer policy guidance for the current dilemma of higher education in India, making itself a strong social application value.

6.1 The Analysis of Current System

We have already evaluated the health condition for India in subsection 5.5, and now we will conduct a more detailed analysis of its health problems based on the real world situation.

关注数学模型

6.1.1 Health

• Education investment

The investment factor of India reaches the standard, but it can still reﬂect many problems. The state’s insufﬁcient funding of public educational institutions has led to the rapid growth of private 微信公众号：数学模型 higher education. More and more public institutions are forced to develop self-ﬁnanced courses, with the rising tuition fees [12]. As a result, the popularization and development of higher education are further restricted.

• Universality of higher education

India’s higher education enrollment rate is only 29%, far below 50%. The number of higher edu- cation institutions is also relatively low. The average tuition fee is much higher than the standard. In addition, the population receiving higher education is mainly composed of urban residents, meaning the low enrollment rate in rural areas. These indicators represent that higher education is not popular enough in India. Large amount of low-income people cannot afford the high cost of education, and most people do not have the opportunity to receive higher education.

微信号：MATHmodels

• The level of research

India has excellent performance in research factor with more than ten important award winners, which contrasts with India’s relatively low research expenditures.

• Educational gap

The student-teacher ratio in India is as high as 25, which indicates the lack of educational resources and quality of education in most universities in India. In contrast, among the top 1,000 universities in QS, there are 24 in India, reﬂecting that Indias top universities still have a high level of teaching and research. On the other hand, many graduates from top schools will choose to go abroad for further studies, and prefer to stay there after graduation. Too much human capital ﬂight further aggravates the decline in India’s education level, forming a vicious circle.

• High unemployment rate

Among the population with higher education in India, the employment rate is only 60%, which is also not up to standard. The Indian curriculum lacks both the main elements of learning content and the depth and ﬂuency of the international curriculum. The lack of quality of education has led to un- qualiﬁed and unclear knowledge acquired by students, causing mass unemployment among educated young people. [wiki-India]

6.1.2 Sustainability

According to DEA-Malmquist model, the India’s efﬁciency has declined for four adjacent years. The expenditure have been increasing, while the results have hardly increased. It can be predicted that without policy intervention, Indias efﬁciency will continue to decline in the future. Thus, its system is not considered sustainable.

6.2 Our Vision and Comparison

The problems in the Indian higher education system are complex and serious, and it is difﬁcult to make changes simply. In order to normalize higher education in India, we have to build our vision for different period of time. With the goal of achieving a comprehensive health of education (OPG = 1),

we have formulated the following three-phase vision for short-term, medium-term and long-term.关注数学模型 • Short-term vision: Normalize the main indicators (including school enrollment, employment rate, and related indicators) in 10 - 15 years.

The ﬁrst requirement for disease treatment is to prevent the deterioration of the disease. Similarly, for the higher education in India, our vision is to prevent the deterioration of the higher education in India and make it develop sustainably. Compared with the current situation, the OPG value of India, which has realized its short-term vision, will be greater than 0.7324, approaching the 微信公众号：数学模型 current situation of Japan. At the same time, the stability of the system will be greatly improved, from a downward trend to an upward trend.

• Mid-term vision: Adjust the remaining indicators except the number of higher education institu- tions to make the system close to the sub-health state in 50 years.

Through economic development and education construction, gradually improve the entrance fees and the treatment of foreign students, and increase the number of teachers. According to the best estimate, in about 50 years, India’s net ﬂow ratio will break through zero, while other indicators will basically normalize. The value of OPG will be close to 0.8799, reaching the lower bound of sub-healthy. Compared with the previous sustainable growth rate, it will gradually slow down and approach a steady state.

• Long-term (ﬁnal) vision: build a healthy higher education system in a hundred years.

微信号：MATHmodels Through centuries of continuous efforts, gradually increase the number of higher education in- stitutions in India and improve educational capabilities. Our vision is to make the value of OPG equal to 1, while maintaining sustainability without decline. This is the ﬁnal destination for our policies.

6.3 Treatment Plan: Our Targeted Policies

Considering the vision given before, we have formulated the short-term policies to realize the short- and medium-term vision and the long-term policies to realize the ﬁnal vision. We will give the speciﬁc impact of the policies and the methods to measure the changes in the indicators after the implementa- tion of the policies. Based on these contents, we will determine the implementation timeline from the original state to the target state.

6.3.1 Declaration for Our Policies

1. Short-term policies

Due to India’s limited resources, large population, and economic pressure, it is not realistic to invest extensively to improve all relevant variables. In the long run, the problem of education quality is also a problem of economic development. Only when the economy is sufﬁciently developed can there be a chance to invest enough in education. Without that, the basic problems like school coverage, the allocation of education resources etc. cannot be solved radically. However, the problem of India’s education system is too serious to hold any longer, the actions shall be taken immediately. Considering the situation, we formulate policies that can quickly change indicators with unhealthy conditions in a short period of time.

• Reduce the cost of education for the poor.

In our statistics, we can ﬁnd that the average education cost of the 50 countries accounts for 49.3% of the GDP per capita, but the ratio in India is as high as 238.1%. Many people cannot receive higher education because of unaffordable high education costs. In this regard, we suggest that the govern- ment lower the tuition fees of higher education or give more education subsidies to poor families to support their higher education (this solution partly refers to the suggestion given in [13]). Increasing the enrollment rate can also be a solution.

关注数学模型 • Lower the minimum wage standard.

Refering to multiple research results in history, it is found that the minimum wage standard has a negative correlation with the enrollment rate. Compared to the high cost for higher education, In- dian teenagers prefer getting a job directly to furthering their studies. If the minimum wage declines, the proportion of the labor force receiving higher education will increase, and the higher education 微信公众号：数学模型 enrollment rate will increase accordingly.

• Lower the admission standards for foreign students.

India has 24 universities ranking top 1000 in the world, which is higher than the world’s average. However, the international students admitted is less than the students studying abroad. It is mainly caused by the lack of high scholarships and appropriate standards for international students. For top business schools in India, the GMTA score requirement is around 710 points. This score is sufﬁcient for 6-7 top American universities to provide full tuition waivers for such students. In India, less than 10% of the local students can reach the standard, and domestic education may not be able to satisfy the international students who rank the top in India. Therefore, the standards should be lowered to attract more foreign students and improve the enviroment for academic exchanges.

微信号：MATHmodels

2. Long-term policies

In contrast, the purpose of short-term policies is to move indicators closer to healthy values. But in order to achieve a healthy state, we also need to consider sustainable long-term policies. Therefore, we made the following recommendations.

• Family planning.

We found that India’s education expenditure and research & development expenditure is higher than the normal value, which means that its education investment is already healthy. If more investment is applied to build more facilities, it will put more pressure to the on the economy, and the quality of education cannot be guaranteed. It is more reasonable to solve the problem from the population than to solve the problem from the investment. Therefore, it is imperative to slow the growth of population down, and the policy should encourage family planning. Reducing the population of the right age can signiﬁcantly reduce the pressure on education and increase the enrollment rate.

• Economic structure transformation.

When the national education becomes healthy, the increase of enrollment rate and the net ﬂow ratio of international students will increase the workforce receiving higher education. In that case, we are able to invest more talents for economic construction. These talents will serve as the guiding force for economic development and contribute to increasing education investment. This input-output-input model realizes the positive feedback of the economic system, possessing good sustainability.

• Educational environment improvement.

The teacher-student ratio in India is a difﬁcult problem to deal with. Teachers in India are treated well. They are paid with high salaries and are always respected. However ,even if the current en- rollment rate is very low, higher education is still facing the dilemma of insufﬁcient teachers in India. Why is this happening? After consulting relevant information, we found that the educational environ- ment in India is the main reason affecting the number of teachers. Indias own educational environment has greatly increased the difﬁculty of recruiting foreign teachers, while local students with teacher po- tential usually choose to ﬁnd employment or go abroad. In conclusion, improving the educational environment in India is a necessary condition for solving the problem of insufﬁcient teachers, it must

关注数学模型 be considered while excuting the policies.

6.3.2 Policy Implementation Model Realized by Using Markov Chain

Since we have selected a healthy range for each indicator, we put forward speciﬁc policy recom- mendations for its ‘unhealthy’ indicators to converge towards ‘healthy’. However, our policies can only provide the direction for the changes, the efﬁciency can not be speciﬁed. In that case, we believe that the effect of policy implementation is a random process.

微信公众号：数学模型 In order to facilitate subsequent modeling, we make the following assumptions based on the general assumptions:

• One of the three states of policy implementation is excuted every year: good, poor, counterpro- ductive. If the policy is effectively implemented, the indicator will change quickly to approach the normal value, but if the policy is not effectively implemented, the indicator state will remain unchanged or even worse.

• The state that happens in the next year depends on the current state and value of current in- dicators. If the policy functions well in the previous year, it is easier to implement in the next year. Moreover, the closer the current indicator is to the normal, the weaker the role regulatory policy plays. This assumption is made in consideration of the relationship between the degree of unhealthy indicators and the role of policies. The more unhealthy the indicators, the greater the willingness to implement the corresponding policies and the greater the acceptability of the 微信号：MATHmodels policies. On the contrary, if the indicators are reaching the health limit, the policies will not result so obvious.

• Under the control of the policies, unhealthy education indicators will eventually reach normal values. The policies are ﬂexible. When the effect is reduced due to its close to the normal value, the policies will be adjusted appropriately, and ﬁnally the index will converge to the normal value.

We model with the assumptions above, determine the to use Markov chain to predict the trend of indicators under policy intervention. We believe that policy implementation effect ( PIE ) and buffer ( BU ) are factors determining the current state and they are random variables, whose distribution are shown below. Since the difference between the current value and the normal value of the index ( DCN ) affects the policy intensity, we add it to the distribution function of PIE to represent its role. The distribution law of PIE and BU is shown in the following table:

Last state PIE BU Distribution law X1 ∼N(k · DCN + 0.01, 0.01), Y 1 ∼N(0.01, 0.01) X1 Y 1 Good X2 ∼N(k · DCN, 0.01), Y 2 ∼N(0, 0.01) X2 Y 2 Poor X3 ∼N(k · DCN −0.01, 0.01), Y 3 ∼N(−0.01, 0.01) X3 Y 3 Counterproductive

The variable k is used to control the severity of the value change. It varies from indicator to indicator. As for modeling, if X +Y > 0.05, it indicates that the policy is in good state. If X +Y < 0.05, it indicates that the policy has counterproductive effect.

With the discussion above, we We can use the indicator value of the i-th year to determine the value of the i + 1-th year, and the transfer equation can be given in the following form:

value(i + 1) = value(i) × (1 −(X + Y )) (6)

6.3.3 Implementation Timeline for India

Based on the above model, we have predicted the effect of the policy implementation. Due to the large amount of forecast data, we choose the changes in the main indicators of each stage to reﬂect the overall changes.

For the short-term vision, the main indicators are the enrollment and the employment rate. Apply-

关注数学模型 ing ﬂexible policies to both indicators, the prediction curves are as follows:

The Prediction for Employment Rate The Prediction for Enrollment Rate 85 60 55 80 50 75 45 40 70 35 65 30 60 25 微信公众号：数学模型 0 5 10 15 20 25 30 0 5 10 15 20 25 30

0 1 2 3 4 5 6 0 1 2 3 4 5 6 7 8 9 7 8 9 10 11 12 13 10 11 12 13 14 15 16 17 18 19 14 15 16 17 18 19

After twenty independent repeated experiments (different curves in the plot), we found that em- ployment rate achieves the lower bound of health range with the average of 10 years and the school enrollment rate turns normal in about 13 years. The short-term vision seem to be achieved success- fully.

As for the mid-term vision, it can be represented by the net ﬂow ratio of international mobile students. For the vision we proposed, its value would turn normal in 50 years. The Markov chain gives out prediction results shown below:

微信号：MATHmodels The Prediction of Net Flow Ratio 0.5

0 0 10 20 30 40 50 60 70 80 90 100

‐0.5

‐1

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19

The average cost for the net ﬂow ratio to be normal is 48 years, meeting the requirement of mid- term vision.

For the long-time vision, the main factor, number of higher education institutions, act as a discrete variable. Although it cannot be predicted through Markov chain, we can set speciﬁed goals for the government to achieve. Here is the implementation timeline for health status:

Policy Implementation Effect Schedule

India's education system The policy began School enrollment rate achieves healthy and to be implemented reaches health level sustainable development

2118 2031 2066 2018 2028

The employment rate Net flow ratio of internationally reaches health level mobile students reaches health level

For the sustainability part, our policies begin with curing and maintaining a sustainable system, so

关注数学模型 a sharp turn can be observed at the beginning. With short-term and mid-term visions achieved, the growth of sustainability slows down and shows a stable trend. Using DEA-Malmquist model, we can plot the timeline for sustainability. Observation concluded that all our visions are achieved properly.

Sustainbility Analysis Efficiency from 2009 to 2018 4 Third Stage 微信公众号：数学模型 (2068-2118) Second Stage (2033-2068) 3 First Stage (2018-2033)

2

1

0 2009 2015 2021 2027 2033 2039 2045 2051 2057 2063 2069 2075 2081 2087 2093 2099 2105 2111 2117

微信号：MATHmodels 6.4 the Real-World Impacts and Difﬁculties

We believe that the short-term policies we designed are for the transition period, and the long-term policies are for the end state. If they can be implemented well, the India’s education system will reach the state of healthy and sustainable in a hundred years. But in fact, the policies may encounter many problems when implementing in India. These problems will hinder the implementation of policies to some extent, creating obstacles for the excution. Here are some of them.

1. Higher education in India is elite education. The cost is relatively high. The government may only be able to afford tuition for a small portion of outstanding students. The increase in enrollment rate may not be as ideal as predicted.

2. Although lowering the minimum wage can motivate young people to receive higher education, there is still a large number of people who can only support their families by doing odd jobs in India. If the minimum wage is suddenly lowered, their lives will be severely affected.

3. Newly added domestic and foreign students may put great pressure on teachers. India inherently lacks teachers in higher education. If the increase in foreign students and the increase in teachers cannot maintain a relative balance, the teacher retention rate will decrease. This will constitute a negative feedback: the teacher’s departure leads to the decrease of students, making the attempt to increase the number of foreign students fail.

4. The most serious problem is dealing with social concepts.A Although the caste system has been abolished in law, the idea of hierarchy still exists. Indians of the lowest rank cannot receive normalized education as the others do, and there is no real fairness for people with low caste.

This backward feudal concept severely limited India’s development potential. If changes are not made, the efﬁciency of the policy will be affected.

However, we are still optimistic about the development of higher education in India. Although change is difﬁcult, it is not impossible. We believe that through the reasonable guidance of policies, the national education environment and the education level of citizens will be gradually improved. Education in India will eventually reach a healthy and sustainable state.

关注数学模型

7 Model Strengths and Weaknesses

7.1 Strengths

• We have established clear criteria for health and sustainability.

For each indicator, we have determined a clear range of health through data analysis. For the 微信公众号：数学模型 measurement of sustainability, we adopted the DEA-Malmquist model by comparing the relative efﬁciency of higher education in different years. The relative efﬁciency between different years can reﬂect the changes in system quality over time and can be used to measure sustainability.

• We have selected enough indicators.

We have selected six main factors and fourteen indicators, which can fully reﬂect the health of the higher education system. Meanwhile, it also provides speciﬁc directions for our policy analysis.

• DEA is a completely objective method.

Using DEA to analyze efﬁciency does not need to specify the weights of various indicators in advance. Each weight is completely determined by the data. It is a completely objective method.

Moreover, the basic DEA model is not suitable for analyzing time series. We adopt the DEA- Malmquist model that considers the changes in productivity over time. Thus, the analysis is 微信号：MATHmodels more reasonable.

• Markov chain can predict the impact of policy well.

The premise of Markov chain is that the next state of the system is only related to the current state. In the process of policy implementation, the government will adjust the policy direction of the next year according to the implementation in that year. Therefore, the Markov chain is very suitable for analyzing the impact of policies.

7.2 Weaknesses

• There are not enough countries.

When determining the health range, we assumed and veriﬁed that certain indicators obey a nor- mal distribution, thereby determining the reasonable range of the indicators. However, due to the small total number of countries in the world, our calculated range may deviate from the range of true normal distribution.

• We did not consider the changes in standards over time.

When analyzing the vision system, we followed the standards in 2018. However, the various indicators of different countries may change in the future. In our model, we have not considered changes in standards.

关注数学模型

Appendices

Appendix A

Codes

A.1 Code for AHP

clc, clear B=[1 1/3 1/5 1/5 1/7 1/9 %Attraction 3 1 1/3 1/3 1/5 1/7 %Equity 5 3 1 1 1/3 1/5 %Research 5 3 1 1 1/3 1/5 %Education 7 5 3 3 1 1/3 %Access 9 7 5 5 3 1]; %Expenditure [n,m]=size(B); for i=1:n for j=1:n if B(i,j)*B(j,i)~=1 fprintf(’i=%d,j=%d,B(i,j)=%d,B(j,i)=%d\n’,i,j,B(i,j),B(j,i)) end end end [Vec,Dig]=eig(B);%Eigenvalues and eigenvectors eigen=max(Dig); eigmax=max(eigen);%The maximum eigenvalue

关注数学模型 c1=find(eigen(1,:)==max(eigen));

eigmaxv=Vec(:,c1);%eigenvector corresponding to the maximum eigenvalue weight=zeros(n,1); for i=1:n weight(i,1)=eigmaxv(i,1)/sum(eigmaxv); end weight=weight’ %Consistency test RI=[0,0,0.58,0.9,1.12,1.24,1.32,1.41,1.45,1.49,1.52,1.54,1.56,1.58,1.59]; CI=(eigmax-n)/(n-1); CR=CI/RI(1,n); 微信公众号：数学模型 CR if CR>=0.1 fprintf(’Consistency test failed\n’); else fprintf(’Consistency test passed\n’); end

A.2 Code for Malkov Chain

import numpy as np import pandas as pd def loadDatadet(infile):

f=open(infile,’r’) sourceInLine=f.readlines() dataset=[] for line in sourceInLine:

temp1=line.strip(’\n’) temp2=temp1.split(’\t’) 微信号：MATHmodels dataset.append(temp2) return dataset infile=’data.txt’ infile=loadDatadet(infile) k=0.0017 tmp=0 normal=77 n=100 j=0 all=[] writer=pd.ExcelWriter("output2.xlsx") while j < 20:

a=60 al=[a] i=0 while i < n:

p=float(infile[j+30][i])+float(infile[j+31][i])+k*(a-normal)+tmp a = a*(1-p) i=i+1 if p>0.05:

tmp=0.01 if p<-0.05:

tmp=-0.01 else:

tmp=0 print(’a’+str(i)+’:’+str(a)) al.append(a) all.append(al) j+=1 data=pd.DataFrame(all) data.to_excel(writer,’page_1’,float_format=’%.5f’) writer.save writer.close()

关注数学模型
