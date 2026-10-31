# P-C-2025-2524070-816ac5d5

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Problem Chosen

<!-- b000002 | furniture | pages [1] -->
2025

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | prose | pages [1] -->
MCM/ICM

<!-- b000005 | title | pages [1] -->
C

<!-- b000006 | furniture | pages [1] -->
2524070

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
From Data to Podiums: A Study for Olympic Medal

<!-- b000009 | title | pages [1] -->
Forecasting

<!-- b000010 | heading | pages [1] -->
Summary

<!-- b000011 | title | pages [1] -->
微信公众号：数学模型

<!-- b000012 | prose | pages [1] -->
This research examines the forecasting of Olympic medal counts by analyzing the competitive outcomes of various nations since the inception of the Olympic Games in 1896. The study addresses five primary concerns:

<!-- b000013 | prose | pages [1] -->
Predict Medal Standings for the 2028 LA Olympics: To effectively model the number of medals awarded to countries, we propose a zero-inflated negative binomial regression model (ZINB). Adopting a Bayesian framework, we employ the Markov Chain Monte Carlo (MCMC) method to derive the posterior distribution of the model parameters. Subsequently, we conduct random simulations to predict the medal standings for the 2028 Olympics. Comprehensive testing of all parameters yielded Rhat values of 1,

<!-- b000014 | title | pages [1] -->
微信号：MATHmodels

<!-- b000015 | prose | pages [1] -->
with both Bulk Effective Sample Size (ESS) and Tail ESS values reaching ten thousand, thereby demonstrating the model’s exceptional predictive stability and precision.

<!-- b000016 | prose | pages [1] -->
Overcoming the Historical Lack of Medals: We introduced the concepts of sampling zero and structural zero within the ZIBN model. By evaluating the probability of generating structural zeros in various countries, we predicted which nations might secure their first medal at the 2028 Los Angeles Olympics. The findings indicate that Mauritania has a 24.8% chance of achieving this milestone!

<!-- b000017 | prose | pages [1] -->
Factors Influencing Medal Totals: In this section,we employed an Association Rule Model utilizing GRI algorithm. Using the United States as a case study,we developed a ’type-num’ comprehensive indicator 𝜑𝑖as the antecedent and the medal count as the consequent, which led to the identification of five strong association rules. Furthermore, the model reinforced the finding that "the host’s choice contribute to its medal success", resulting in two strong rules. The analysis revealed that ’Athletics’ plays a vital role The support for these rules was as high as 80.56%, with confidence for all nations. levels generally exceeding 80%, and lift values all above 1, confirming the validity of the findings.

<!-- b000018 | prose | pages [1] -->
Great Coach Effect: To investigate the presence of the "great coach" effect while accounting for the influence of both the coach and the country they represent, we developed a mixed-effects model. In this model, the pairing of coach and country is treated as a random block, while the "great coach" factor is considered a fixed two-level factor. Our analysis confirmed the existence of the "great coach" effect and provided a point estimate of 3.74. For the countries we analyzed, hiring a "great coach" increases the likelihood of winning a silver or gold medal to over 50%.

<!-- b000019 | prose | pages [1] -->
Original Insights: Based on the results of the regression parameter estimates and the established association rules, we found that the number of events has a minimal impact on performance and can be considered negligible. Therefore, we recommend targeted resource allocation, prioritization of qualifications based on medal probability, and precise talent scouting to synergistically enhance medal efficiency.

<!-- b000020 | keywords | pages [1] -->
Keywords: Zero-Inflated Negative Binomial Regression; Association Rules; GRI Algo-

<!-- b000021 | prose | pages [1] -->
rithm; Mixed-effects Model; Prediction of the LA Olympics.

<!-- b000022 | furniture | pages [2] -->
Page 2of 25

<!-- b000023 | furniture | pages [2] -->
Team 2524070

<!-- b000024 | heading | pages [2] -->
Contents

<!-- b000025 | contents | pages [2] -->
模型

<!-- b000026 | contents | pages [2] -->
3

<!-- b000027 | heading | pages [2] -->
Introduction

<!-- b000028 | prose | pages [2] -->
1

<!-- b000029 | heading | pages [2] -->
Background

<!-- b000030 | prose | pages [2] -->
1.1 3

<!-- b000031 | heading | pages [2] -->
Problem Restatement

<!-- b000032 | prose | pages [2] -->
1.2 3 1.3 4 Our Work

<!-- b000033 | heading | pages [2] -->
Assumptions and Notations

<!-- b000034 | prose | pages [2] -->
2 4

<!-- b000035 | prose | pages [2] -->
Data Preprocessing 5 3

<!-- b000036 | prose | pages [2] -->
Who Will Rule the Medal Race at the 2028 LA Olympics? 6 4

<!-- b000037 | prose | pages [2] -->
4.1

<!-- b000038 | heading | pages [2] -->
Count Regression Model

<!-- b000039 | prose | pages [2] -->
6 4.2 Zero-Inflated Model . 7

<!-- b000040 | heading | pages [2] -->
Zero-Inflated Negative Binomial Model

<!-- b000041 | prose | pages [2] -->
4.3 8

<!-- b000042 | heading | pages [2] -->
Fitting the Model Using Bayesian Inference and MCMC

<!-- b000043 | prose | pages [2] -->
4.4 8 4.5 Problem Solutions . . 10 4.6 10 Results .

<!-- b000044 | heading | pages [2] -->
Model Assessment

<!-- b000045 | prose | pages [2] -->
13 4.7

<!-- b000046 | prose | pages [2] -->
How Events of Various Sports Impact the Results? 13 5 Establishment of Indicators 13 5.1

<!-- b000047 | heading | pages [2] -->
Events-Medals Association Rule Model Based on GRI Algorithm

<!-- b000048 | prose | pages [2] -->
5.2 14 5.3

<!-- b000049 | heading | pages [2] -->
Results Analysis

<!-- b000050 | prose | pages [2] -->
17

<!-- b000051 | prose | pages [2] -->
19 Could a Great Coach Boost Your Country's Medal Count? 6 20 6.1 Analysis of Variance, Mixed-effects Model . 6.2 Definition of the Response Variable 20 6.3 21

<!-- b000052 | heading | pages [2] -->
Fitting the Model

<!-- b000053 | prose | pages [2] -->
21 6.4 6.5 23 Results .

<!-- b000054 | prose | pages [2] -->
24 What Else Is Included in Our Model? 7 1 24 Model Evaluation 8 24 Advantages 8.1 25 Limitations 8.2

<!-- b000055 | prose | pages [2] -->
关注数学模型

<!-- b000056 | furniture | pages [2] -->
获取更多资讯

<!-- b000057 | furniture | pages [3] -->
Team 2524070

<!-- b000058 | furniture | pages [3] -->
Page 3of 25

<!-- b000059 | heading | pages [3] -->
1 Introduction

<!-- b000060 | heading | pages [3] -->
1.1 Background

<!-- b000061 | prose | pages [3] -->
微信公众号：数学模型 During each Olympic Games, spectators not only follow the thrilling sports competitions but also keep an eye on the national medal standings. Figure 1 illustrates the fluctuations in the total medal counts of seven nations, including the United States and China, over the past five Summer Olympics.

<!-- b000062 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000063 | caption | pages [3] -->
Figure 1: Total Medal Count of the Last 5 Summer Olympics – 7 Countries

<!-- b000064 | prose | pages [3] -->
For these relatively strong nations, fans are particularly interested in ranking changes, such as whether they have made it into the top 5 or top 3. They also pay attention to variations in the total number of medals, especially gold medals. Conversely, for some countries, securing even a single medal is a noteworthy accomplishment.

<!-- b000065 | prose | pages [3] -->
Given this context, forecasting the medal counts for each nation in the upcoming Olympic Games is valuable. This article utilizes historical data from the Summer Olympics to predict the number of medals anticipated for the 2028 Games and seeks to identify factors that may influence medal outcomes based on past data.

<!-- b000066 | heading | pages [3] -->
1.2 Problem Restatement

<!-- b000067 | prose | pages [3] -->
Through an in-depth analysis of the background, while considering the existing constraints, we can only use the given datasets to build the model. We need to address the following issues:

<!-- b000068 | prose | pages [3] -->
• Develop a predictive model for the medal count for the 2028 Summer Olympics. This model should estimate the number of gold, silver, and bronze medals for each participating country, as well as the overall medal tally, and should include a prediction interval. Furthermore, an analysis of the results should be conducted to determine whether the performance of each country is comparatively better or worse, with particular emphasis on including predictions for nations that have not previously secured any medals.

<!-- b000069 | prose | pages [3, 4] -->
• Create a model to investigate the correlation between various sporting events and the medal outcomes of different countries. This model should account for both the quantity of events and the diversity of disciplines, thereby identifying which sports are significant for multiple nations. Additionally, it should consider the influence of event additions motivated by the host country's objectives in prior Olympic Games on the resulting medal outcomes.

<!-- b000070 | furniture | pages [4] -->
Page 4of 25

<!-- b000071 | furniture | pages [4] -->
Team 2524070

<!-- b000073 | prose | pages [4] -->
• Formulate a model to evaluate the influence of prominent coaches. This model must ascertain the existence of such an impact exists and, if present, assess its magnitude. Subsequently, three countries should be identified for analysis regarding which sports would benefit from investment in elite coaching, along with an indication of the potential advantages.

<!-- b000074 | prose | pages [4] -->
• Utilize the model previously developed to uncover additional distinctive insights and communi- cate these findings to the Olympic Committee.

<!-- b000075 | heading | pages [4] -->
1.3 Our Work

<!-- b000076 | prose | pages [4] -->
Framework of our work are as follows.

<!-- b000077 | prose | pages [4] -->
TASK 1 28 PART 2 Zero-inflated Zero-inflated Beta Regressions MCMC Probability of certain Fit the model parameters countries winning their first medal Posterior Probability Population GDP Distribution Mauritania, Bosnia and Herzegovina, Lesotho Simulate LA 2028 Medal Table PART 3 Medal share:Z The importance of sports Zi Comparison with 2024 20 Countries Correlation analysis Events type:x Antecedent Consequent mc φi = ω1xi + ω2yi GRI Worse countries Better countries Events number:y ifint,ifpar ifhave,ifmax PART 1

<!-- b000078 | prose | pages [4] -->
TASK 2 TASK 3

<!-- b000079 | prose | pages [4] -->
Fixed factor Box-Cox transformation Mixed effects model if great coach distribution QQ plot Several Analysis of variance original Random block Small variance Normal distribution insights Variance inequality Country, Coach Fixed-effect model

<!-- b000080 | prose | pages [4] -->
Correction, inspection White robust standard error under heteroscedasticity

<!-- b000081 | caption | pages [4] -->
Figure 2: Framework of Our Work.

<!-- b000082 | heading | pages [4] -->
Assumptions and Notations

<!-- b000083 | prose | pages [4] -->
2

<!-- b000084 | prose | pages [4] -->
Concerning the assumptions of the model, we have:

<!-- b000085 | prose | pages [4, 5] -->
关注数学模型 Assumption 1: Countries that have never won a medal at the Olympics are those that participated in the Olympics but have never won any awards in summerOly_athletes.csv'. I Assumption 2: The number of medals won by the country follows a negative binomial distribution.

<!-- b000086 | furniture | pages [4] -->
获取更多资讯

<!-- b000087 | furniture | pages [5] -->
Team 2524070

<!-- b000088 | furniture | pages [5] -->
Page 5of 25

<!-- b000090 | prose | pages [5] -->
Assumption 3: A country's performance in the next Olympic Games can be predicted based on its performance in previous Olympic Games, whether it is the host country, and the number of events that year.

<!-- b000091 | heading | pages [5] -->
With respect to the notation, we define the following:

<!-- b000092 | prose | pages [5] -->
Explanation

<!-- b000093 | heading | pages [5] -->
Symbol

<!-- b000094 | prose | pages [5] -->
number of gold medals in the ith most recent Olympic Games ngold,i number of silver medals in the ith most recent Olympic Games Nsilver,i number of bronze medals in the ith most recent Olympic Games nbronze,i number of events in that Olympic Games Nevents host binary variable: whether that country is the host country random effect of different countries country 2 variance of the random effect country σc probability of a structural zero occurring po Y random variable of the number of medals overdispersion of the negative binomial regression model φ αi βi regression coefficients of the negative binomial regression model value of the response variable for the k-th replicate in the j-th block at the i-th level. aijk

<!-- b000095 | caption | pages [5] -->
Table 1: List of Symbols

<!-- b000096 | prose | pages [5] -->
●

<!-- b000097 | heading | pages [5] -->
3 Data Preprocessing

<!-- b000098 | prose | pages [5] -->
In the analysis of the provided datasets, specifically 'data_dictionary.csv', 'summerOly_athletes.csv', 'summerOly_hosts.csv', 'summerOly_medal_counts.csv', and 'summerOly_programs.csv' (hereafter referred to as dic, athletes, hosts, medals, and programs), the following processing steps were undertaken:

<!-- b000099 | prose | pages [5] -->
1. The medals dataset did not include countries that did not win any medals. Therefore, we retrieved data on countries that participated in the Olympics but did not win any medals from the athletes dataset.

<!-- b000100 | prose | pages [5] -->
2. Within the athletes dataset, the Team column contained notations such as -1 and -2, and it is noted that early Olympic Games featured teams represented by cities. For the purpose of data screening, only the National Olympic Committee (NOC) was considered, excluding the Team column.

<!-- b000101 | prose | pages [5] -->
3. Data pertaining to the year 1906, which is classified as an unofficial competition, was entirely removed from the datasets.

<!-- b000102 | prose | pages [5, 6] -->
4. An analysis of the NOC revealed that certain countries have undergone changes due to historical and political developments. As a result, all data associated with the original countries of the Soviet Union, Yugoslavia, and other nations that have subsequently fragmented have been removed. Further- more, data from countries such as East Germany and West Germany, which have ceased to exist due to historical circumstances, have also been excluded.

<!-- b000103 | furniture | pages [6] -->
m

<!-- b000104 | furniture | pages [6] -->
m

<!-- b000105 | furniture | pages [6] -->
m

<!-- b000106 | furniture | pages [6] -->
m

<!-- b000107 | furniture | pages [6] -->
m

<!-- b000108 | furniture | pages [6] -->
m

<!-- b000109 | furniture | pages [6] -->
m

<!-- b000110 | furniture | pages [6] -->
m

<!-- b000111 | furniture | pages [6] -->
m

<!-- b000112 | furniture | pages [6] -->
m

<!-- b000113 | furniture | pages [6] -->
m

<!-- b000114 | furniture | pages [6] -->
m

<!-- b000115 | furniture | pages [6] -->
m

<!-- b000116 | furniture | pages [6] -->
m

<!-- b000117 | furniture | pages [6] -->
m

<!-- b000118 | furniture | pages [6] -->
m

<!-- b000119 | furniture | pages [6] -->
m

<!-- b000120 | furniture | pages [6] -->
m

<!-- b000121 | furniture | pages [6] -->
m

<!-- b000122 | furniture | pages [6] -->
m

<!-- b000123 | furniture | pages [6] -->
m

<!-- b000124 | furniture | pages [6] -->
m

<!-- b000125 | furniture | pages [6] -->
m

<!-- b000126 | furniture | pages [6] -->
m

<!-- b000127 | furniture | pages [6] -->
m

<!-- b000128 | furniture | pages [6] -->
m

<!-- b000129 | furniture | pages [6] -->
m

<!-- b000130 | furniture | pages [6] -->
m

<!-- b000131 | furniture | pages [6] -->
m

<!-- b000132 | furniture | pages [6] -->
m

<!-- b000133 | furniture | pages [6] -->
m

<!-- b000134 | furniture | pages [6] -->
m

<!-- b000135 | furniture | pages [6] -->
m

<!-- b000136 | furniture | pages [6] -->
m

<!-- b000137 | furniture | pages [6] -->
m

<!-- b000138 | furniture | pages [6] -->
m

<!-- b000139 | furniture | pages [6] -->
m

<!-- b000140 | furniture | pages [6] -->
m

<!-- b000141 | furniture | pages [6] -->
m

<!-- b000142 | furniture | pages [6] -->
m

<!-- b000143 | furniture | pages [6] -->
m

<!-- b000144 | furniture | pages [6] -->
m

<!-- b000145 | furniture | pages [6] -->
m

<!-- b000146 | furniture | pages [6] -->
m

<!-- b000147 | furniture | pages [6] -->
m

<!-- b000148 | furniture | pages [6] -->
m

<!-- b000149 | furniture | pages [6] -->
m

<!-- b000150 | furniture | pages [6] -->
m

<!-- b000151 | furniture | pages [6] -->
m

<!-- b000152 | furniture | pages [6] -->
m

<!-- b000153 | furniture | pages [6] -->
m

<!-- b000154 | furniture | pages [6] -->
m

<!-- b000155 | furniture | pages [6] -->
m

<!-- b000156 | furniture | pages [6] -->
m

<!-- b000157 | furniture | pages [6] -->
m

<!-- b000158 | furniture | pages [6] -->
m

<!-- b000159 | furniture | pages [6] -->
m

<!-- b000160 | furniture | pages [6] -->
m

<!-- b000161 | furniture | pages [6] -->
m

<!-- b000162 | furniture | pages [6] -->
m

<!-- b000163 | furniture | pages [6] -->
m

<!-- b000164 | furniture | pages [6] -->
m

<!-- b000165 | furniture | pages [6] -->
m

<!-- b000166 | furniture | pages [6] -->
m

<!-- b000167 | furniture | pages [6] -->
m

<!-- b000168 | furniture | pages [6] -->
m

<!-- b000169 | furniture | pages [6] -->
m

<!-- b000170 | furniture | pages [6] -->
m

<!-- b000171 | furniture | pages [6] -->
m

<!-- b000172 | furniture | pages [6] -->
m

<!-- b000173 | furniture | pages [6] -->
m

<!-- b000174 | furniture | pages [6] -->
m

<!-- b000175 | furniture | pages [6] -->
m

<!-- b000176 | furniture | pages [6] -->
m

<!-- b000177 | furniture | pages [6] -->
m

<!-- b000178 | furniture | pages [6] -->
m

<!-- b000179 | furniture | pages [6] -->
m

<!-- b000180 | furniture | pages [6] -->
m

<!-- b000181 | furniture | pages [6] -->
m

<!-- b000182 | furniture | pages [6] -->
m

<!-- b000183 | furniture | pages [6] -->
m

<!-- b000184 | furniture | pages [6] -->
m

<!-- b000185 | furniture | pages [6] -->
m

<!-- b000186 | furniture | pages [6] -->
m

<!-- b000187 | furniture | pages [6] -->
m

<!-- b000188 | furniture | pages [6] -->
m

<!-- b000189 | furniture | pages [6] -->
m

<!-- b000190 | furniture | pages [6] -->
m

<!-- b000191 | furniture | pages [6] -->
m

<!-- b000192 | furniture | pages [6] -->
m

<!-- b000193 | furniture | pages [6] -->
m

<!-- b000194 | furniture | pages [6] -->
m

<!-- b000195 | furniture | pages [6] -->
m

<!-- b000196 | furniture | pages [6] -->
m

<!-- b000197 | furniture | pages [6] -->
m

<!-- b000198 | furniture | pages [6] -->
m

<!-- b000199 | furniture | pages [6] -->
m

<!-- b000200 | furniture | pages [6] -->
m

<!-- b000201 | furniture | pages [6] -->
m

<!-- b000202 | furniture | pages [6] -->
m

<!-- b000203 | furniture | pages [6] -->
m

<!-- b000204 | furniture | pages [6] -->
m

<!-- b000205 | furniture | pages [6] -->
m

<!-- b000206 | furniture | pages [6] -->
m

<!-- b000207 | furniture | pages [6] -->
m

<!-- b000208 | furniture | pages [6] -->
m

<!-- b000209 | furniture | pages [6] -->
m

<!-- b000210 | furniture | pages [6] -->
m

<!-- b000211 | furniture | pages [6] -->
m

<!-- b000212 | furniture | pages [6] -->
m

<!-- b000213 | furniture | pages [6] -->
m

<!-- b000214 | furniture | pages [6] -->
m

<!-- b000215 | furniture | pages [6] -->
m

<!-- b000216 | furniture | pages [6] -->
m

<!-- b000217 | furniture | pages [6] -->
m

<!-- b000218 | furniture | pages [6] -->
m

<!-- b000219 | furniture | pages [6] -->
m

<!-- b000220 | furniture | pages [6] -->
m

<!-- b000221 | furniture | pages [6] -->
m

<!-- b000222 | furniture | pages [6] -->
m

<!-- b000223 | furniture | pages [6] -->
m

<!-- b000224 | furniture | pages [6] -->
m

<!-- b000225 | furniture | pages [6] -->
m

<!-- b000226 | furniture | pages [6] -->
m

<!-- b000227 | furniture | pages [6] -->
m

<!-- b000228 | furniture | pages [6] -->
m

<!-- b000229 | furniture | pages [6] -->
m

<!-- b000230 | furniture | pages [6] -->
m

<!-- b000231 | furniture | pages [6] -->
m

<!-- b000232 | furniture | pages [6] -->
m

<!-- b000233 | furniture | pages [6] -->
m

<!-- b000234 | furniture | pages [6] -->
m

<!-- b000235 | furniture | pages [6] -->
m

<!-- b000236 | furniture | pages [6] -->
m

<!-- b000237 | furniture | pages [6] -->
m

<!-- b000238 | furniture | pages [6] -->
m

<!-- b000239 | furniture | pages [6] -->
m

<!-- b000240 | furniture | pages [6] -->
m

<!-- b000241 | furniture | pages [6] -->
m

<!-- b000242 | furniture | pages [6] -->
m

<!-- b000243 | furniture | pages [6] -->
m

<!-- b000244 | furniture | pages [6] -->
m

<!-- b000245 | furniture | pages [6] -->
m

<!-- b000246 | furniture | pages [6] -->
m

<!-- b000247 | furniture | pages [6] -->
m

<!-- b000248 | furniture | pages [6] -->
m

<!-- b000249 | furniture | pages [6] -->
m

<!-- b000250 | furniture | pages [6] -->
m

<!-- b000251 | furniture | pages [6] -->
m

<!-- b000252 | furniture | pages [6] -->
m

<!-- b000253 | furniture | pages [6] -->
m

<!-- b000254 | furniture | pages [6] -->
m

<!-- b000255 | furniture | pages [6] -->
m

<!-- b000256 | furniture | pages [6] -->
m

<!-- b000257 | furniture | pages [6] -->
m

<!-- b000258 | furniture | pages [6] -->
m

<!-- b000259 | furniture | pages [6] -->
m

<!-- b000260 | furniture | pages [6] -->
m

<!-- b000261 | furniture | pages [6] -->
m

<!-- b000262 | furniture | pages [6] -->
m

<!-- b000263 | furniture | pages [6] -->
m

<!-- b000264 | furniture | pages [6] -->
m

<!-- b000265 | furniture | pages [6] -->
m

<!-- b000266 | furniture | pages [6] -->
m

<!-- b000267 | furniture | pages [6] -->
m

<!-- b000268 | furniture | pages [6] -->
m

<!-- b000269 | furniture | pages [6] -->
m

<!-- b000270 | furniture | pages [6] -->
m

<!-- b000271 | furniture | pages [6] -->
m

<!-- b000272 | furniture | pages [6] -->
m

<!-- b000273 | furniture | pages [6] -->
m

<!-- b000274 | furniture | pages [6] -->
m

<!-- b000275 | furniture | pages [6] -->
m

<!-- b000276 | furniture | pages [6] -->
m

<!-- b000277 | furniture | pages [6] -->
m

<!-- b000278 | furniture | pages [6] -->
m

<!-- b000279 | furniture | pages [6] -->
m

<!-- b000280 | furniture | pages [6] -->
m

<!-- b000281 | furniture | pages [6] -->
m

<!-- b000282 | furniture | pages [6] -->
m

<!-- b000283 | furniture | pages [6] -->
m

<!-- b000284 | furniture | pages [6] -->
m

<!-- b000285 | furniture | pages [6] -->
m

<!-- b000286 | furniture | pages [6] -->
m

<!-- b000287 | furniture | pages [6] -->
m

<!-- b000288 | furniture | pages [6] -->
m

<!-- b000289 | furniture | pages [6] -->
m

<!-- b000290 | furniture | pages [6] -->
m

<!-- b000291 | furniture | pages [6] -->
m

<!-- b000292 | furniture | pages [6] -->
m

<!-- b000293 | furniture | pages [6] -->
m

<!-- b000294 | furniture | pages [6] -->
m

<!-- b000295 | furniture | pages [6] -->
m

<!-- b000296 | furniture | pages [6] -->
m

<!-- b000297 | furniture | pages [6] -->
m

<!-- b000298 | furniture | pages [6] -->
m

<!-- b000299 | furniture | pages [6] -->
m

<!-- b000300 | furniture | pages [6] -->
m

<!-- b000301 | furniture | pages [6] -->
m

<!-- b000302 | furniture | pages [6] -->
m

<!-- b000303 | furniture | pages [6] -->
m

<!-- b000304 | furniture | pages [6] -->
m

<!-- b000305 | furniture | pages [6] -->
m

<!-- b000306 | furniture | pages [6] -->
m

<!-- b000307 | furniture | pages [6] -->
m

<!-- b000308 | furniture | pages [6] -->
m

<!-- b000309 | furniture | pages [6] -->
m

<!-- b000310 | furniture | pages [6] -->
m

<!-- b000311 | furniture | pages [6] -->
m

<!-- b000312 | furniture | pages [6] -->
m

<!-- b000313 | furniture | pages [6] -->
m

<!-- b000314 | furniture | pages [6] -->
m

<!-- b000315 | furniture | pages [6] -->
m

<!-- b000316 | furniture | pages [6] -->
m

<!-- b000317 | furniture | pages [6] -->
m

<!-- b000318 | furniture | pages [6] -->
m

<!-- b000319 | furniture | pages [6] -->
m

<!-- b000320 | furniture | pages [6] -->
m

<!-- b000321 | furniture | pages [6] -->
m

<!-- b000322 | furniture | pages [6] -->
m

<!-- b000323 | furniture | pages [6] -->
m

<!-- b000324 | furniture | pages [6] -->
m

<!-- b000325 | furniture | pages [6] -->
m

<!-- b000326 | furniture | pages [6] -->
m

<!-- b000327 | furniture | pages [6] -->
m

<!-- b000328 | furniture | pages [6] -->
m

<!-- b000329 | furniture | pages [6] -->
m

<!-- b000330 | furniture | pages [6] -->
m

<!-- b000331 | furniture | pages [6] -->
m

<!-- b000332 | furniture | pages [6] -->
m

<!-- b000333 | furniture | pages [6] -->
m

<!-- b000334 | furniture | pages [6] -->
m

<!-- b000335 | furniture | pages [6] -->
m

<!-- b000336 | furniture | pages [6] -->
m

<!-- b000337 | furniture | pages [6] -->
m

<!-- b000338 | furniture | pages [6] -->
m

<!-- b000339 | furniture | pages [6] -->
m

<!-- b000340 | furniture | pages [6] -->
m

<!-- b000341 | furniture | pages [6] -->
m

<!-- b000342 | furniture | pages [6] -->
m

<!-- b000343 | furniture | pages [6] -->
m

<!-- b000344 | furniture | pages [6] -->
m

<!-- b000345 | furniture | pages [6] -->
m

<!-- b000346 | furniture | pages [6] -->
m

<!-- b000347 | furniture | pages [6] -->
m

<!-- b000348 | furniture | pages [6] -->
m

<!-- b000349 | furniture | pages [6] -->
m

<!-- b000350 | furniture | pages [6] -->
m

<!-- b000351 | furniture | pages [6] -->
m

<!-- b000352 | furniture | pages [6] -->
m

<!-- b000353 | furniture | pages [6] -->
m

<!-- b000354 | furniture | pages [6] -->
m

<!-- b000355 | furniture | pages [6] -->
m

<!-- b000356 | furniture | pages [6] -->
m

<!-- b000357 | furniture | pages [6] -->
m

<!-- b000358 | furniture | pages [6] -->
m

<!-- b000359 | furniture | pages [6] -->
m

<!-- b000360 | furniture | pages [6] -->
m

<!-- b000361 | furniture | pages [6] -->
m

<!-- b000362 | furniture | pages [6] -->
m

<!-- b000363 | furniture | pages [6] -->
m

<!-- b000364 | furniture | pages [6] -->
m

<!-- b000365 | furniture | pages [6] -->
m

<!-- b000366 | furniture | pages [6] -->
m

<!-- b000367 | furniture | pages [6] -->
m

<!-- b000368 | furniture | pages [6] -->
m

<!-- b000369 | furniture | pages [6] -->
m

<!-- b000370 | furniture | pages [6] -->
m

<!-- b000371 | furniture | pages [6] -->
m

<!-- b000372 | furniture | pages [6] -->
m

<!-- b000373 | furniture | pages [6] -->
m

<!-- b000374 | furniture | pages [6] -->
m

<!-- b000375 | furniture | pages [6] -->
m

<!-- b000376 | furniture | pages [6] -->
m

<!-- b000377 | furniture | pages [6] -->
m

<!-- b000378 | furniture | pages [6] -->
m

<!-- b000379 | furniture | pages [6] -->
m

<!-- b000380 | furniture | pages [6] -->
m

<!-- b000381 | furniture | pages [6] -->
m

<!-- b000382 | furniture | pages [6] -->
m

<!-- b000383 | furniture | pages [6] -->
m

<!-- b000384 | furniture | pages [6] -->
m

<!-- b000385 | furniture | pages [6] -->
m

<!-- b000386 | furniture | pages [6] -->
m

<!-- b000387 | furniture | pages [6] -->
m

<!-- b000388 | furniture | pages [6] -->
m

<!-- b000389 | furniture | pages [6] -->
m

<!-- b000390 | furniture | pages [6] -->
m

<!-- b000391 | furniture | pages [6] -->
m

<!-- b000392 | furniture | pages [6] -->
m

<!-- b000393 | furniture | pages [6] -->
m

<!-- b000394 | furniture | pages [6] -->
m

<!-- b000395 | furniture | pages [6] -->
m

<!-- b000396 | furniture | pages [6] -->
m

<!-- b000397 | furniture | pages [6] -->
m

<!-- b000398 | furniture | pages [6] -->
m

<!-- b000399 | furniture | pages [6] -->
m

<!-- b000400 | furniture | pages [6] -->
m

<!-- b000401 | furniture | pages [6] -->
m

<!-- b000402 | furniture | pages [6] -->
m

<!-- b000403 | furniture | pages [6] -->
m

<!-- b000404 | furniture | pages [6] -->
m

<!-- b000405 | furniture | pages [6] -->
m

<!-- b000406 | furniture | pages [6] -->
m

<!-- b000407 | furniture | pages [6] -->
m

<!-- b000408 | furniture | pages [6] -->
m

<!-- b000409 | furniture | pages [6] -->
m

<!-- b000410 | furniture | pages [6] -->
m

<!-- b000411 | furniture | pages [6] -->
m

<!-- b000412 | furniture | pages [6] -->
m

<!-- b000413 | furniture | pages [6] -->
m

<!-- b000414 | furniture | pages [6] -->
m

<!-- b000415 | furniture | pages [6] -->
m

<!-- b000416 | furniture | pages [6] -->
m

<!-- b000417 | furniture | pages [6] -->
m

<!-- b000418 | furniture | pages [6] -->
m

<!-- b000419 | furniture | pages [6] -->
Team 2524070

<!-- b000420 | furniture | pages [6] -->
Page 6of 25

<!-- b000422 | prose | pages [6] -->
5. The issue of missing values within the provided datasets was systematically addressed. The 𝑎𝑡ℎ𝑙𝑒𝑡𝑒𝑠and 𝑚𝑒𝑑𝑎𝑙𝑠datasets contained no missing values. For the 𝑝𝑟𝑜𝑔𝑟𝑎𝑚𝑠dataset, if related events were recorded in the 𝑎𝑡ℎ𝑙𝑒𝑡𝑒𝑠, the occurrences were counted to supplement the missing data; if no related events were recorded, all occurrences for that particular year were recorded as 0.

<!-- b000423 | prose | pages [6] -->
6. The treatment of question marks within the 𝑝𝑟𝑜𝑔𝑟𝑎𝑚𝑠dataset was conducted as follows: for ’?0’, it was interpreted that the event did not occur during that year for unspecified reasons. For ’? non-0’, after verification, if the event was not recorded in the athletes data, it was also noted as zero. The ’??’ designation, which appeared in the athletes table, was determined to refer to informal competitions, such as exhibitions, which do not contribute to medal counts; consequently, data pertaining to these informal competitions was deleted. Furthermore, the items Jeu de Paume and Roque, which appeared with ’?’ in the Code, were found through research to have been briefly included as official events in the early Olympic Games but are no longer recognized; therefore, this data was also removed.

<!-- b000424 | prose | pages [6] -->
7. A garbled text issue was identified in the 𝑝𝑟𝑜𝑔𝑟𝑎𝑚𝑠dataset, where ’Baseball**nd Softball’ was recorded, while the 𝑎𝑡ℎ𝑙𝑒𝑡𝑒𝑠dataset correctly listed it as ’Baseball/Softball’. Consequently, the 𝑝𝑟𝑜𝑔𝑟𝑎𝑚𝑠dataset was subsequently amended to align with the format used in the 𝑎𝑡ℎ𝑙𝑒𝑡𝑒𝑠dataset.

<!-- b000425 | prose | pages [6] -->
4 Who Will Rule the Medal Race at the 2028 LA Olympics?

<!-- b000426 | heading | pages [6] -->
4.1 Count Regression Model

<!-- b000427 | prose | pages [6] -->
Problem 1 requires us to predict the medal outcomes for various countries at the 2028 Los Angeles Olympics. Since the dependent variable—the number of medals—is a count variable, meaning it can only take on non-negative integer values, we have opted to use a count regression model instead of a general regression or machine learning model.

<!-- b000428 | prose | pages [6] -->
In counting problems, there are two primary types of regression models: Poisson regression and negative binomial regression. Poisson regression is predicated on the assumption that the data follows a Poisson distribution, which necessitates that the mean and variance are approximately equal. Upon examining this assumption, we found the variances for the number of gold medals and the total number of medals to be 28.57 and 202.05, respectively, while the means were only 1.64 and 5.11. The variance of the total number of medals significantly exceeds the mean, indicating that the data is overdispersed. Consequently, we chose to employ negative binomial regression for our analysis.

<!-- b000429 | prose | pages [6] -->
Type Expectation Variance

<!-- b000430 | prose | pages [6] -->
Gold Medals 1.64 28.57

<!-- b000431 | prose | pages [6] -->
Total Medals 5.11 202.05

<!-- b000432 | caption | pages [6] -->
Table 2: Expectation and Variance for Gold Medals and Total Medals

<!-- b000433 | prose | pages [6, 7] -->
关注数学模型 微信公众号：数学模型 微信号：MATHmodels (a) Distribution of Gold Medals (b) Distribution of Total Medals

<!-- b000434 | furniture | pages [6] -->
2

<!-- b000435 | furniture | pages [6] -->
MATHmodels

<!-- b000436 | furniture | pages [6] -->
获取更多资讯

<!-- b000437 | furniture | pages [7] -->
Team 2524070

<!-- b000438 | furniture | pages [7] -->
Page 7of 25

<!-- b000440 | caption | pages [7] -->
Figure 3: Histograms of Gold and Total Medals

<!-- b000441 | prose | pages [7] -->
We believe that a country’s performance in a specific Olympic Games can be predicted by con- sidering several factors: the number of events that year, whether the country is the host, and its performance in the previous three Olympic Games. This reasoning is intuitive: more events provide greater opportunities to win medals; host countries often benefit from a home advantage and typically secure more medals; and past performance reflects the country’s overall strength. Based on these factors, we developed the following model1:

<!-- b000442 | prose | pages [7] -->
𝑦 𝜙 𝑦+ 𝜙−1 𝜇 𝜙   𝑃(𝑌= 𝑦) = (1) 𝑦 𝜇+ 𝜙 𝜇+ 𝜙

<!-- b000443 | prose | pages [7] -->
where 𝜙is the overdispersion parameter and 𝜇is the mean number of medals, which can be calculated as follows:

<!-- b000444 | prose | pages [7] -->
3 ∑︁ ln(𝜇) = 𝛽0 + 𝛽𝑖𝑛𝑔𝑜𝑙𝑑,𝑖+ 𝛽4𝑛𝑒𝑣𝑒𝑛𝑡𝑠+ 𝛽5ℎ𝑜𝑠𝑡 (2) 𝑖=1

<!-- b000445 | heading | pages [7] -->
4.2 Zero-Inflated Model

<!-- b000446 | prose | pages [7] -->
The Olympic Games, a prominent international sporting event, attract a significant number of athletes from around the world for each iteration. However, it is important to note that in each competition, typically only three nations are awarded medals, and instances of tied results are relatively rare. Historically, since the inception of the Olympic Games in 1896, numerous countries have yet to secure any medals. As a result, the dataset contains a substantial number of zero values. The prevalence of these zeros presents a challenge, as the negative binomial distribution does not adequately account

<!-- b000447 | prose | pages [7, 8] -->
1Using the count of gold medals as an illustration, the scenario for all medal totals is similar, with the only difference being that in the explanatory variables, the count of gold medals from the previous three years is replaced with the overall medal count from those same three years. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m for the frequent occurrence of zeros. This necessitates the use of the Zero-Inflated Model, which incorporates an additional framework specifically designed to address the zeros within the dataset, thereby providing a more accurate representation of the phenomenon of high-frequency zeros.

<!-- b000448 | furniture | pages [7] -->
m

<!-- b000449 | furniture | pages [7] -->
m

<!-- b000450 | furniture | pages [7] -->
m

<!-- b000451 | furniture | pages [7] -->
m

<!-- b000452 | furniture | pages [7] -->
m

<!-- b000453 | furniture | pages [7] -->
m

<!-- b000454 | furniture | pages [7] -->
m

<!-- b000455 | furniture | pages [7] -->
m

<!-- b000456 | furniture | pages [7] -->
m

<!-- b000457 | furniture | pages [7] -->
m

<!-- b000458 | furniture | pages [7] -->
m

<!-- b000459 | furniture | pages [7] -->
m

<!-- b000460 | furniture | pages [7] -->
m

<!-- b000461 | furniture | pages [7] -->
m

<!-- b000462 | furniture | pages [7] -->
m

<!-- b000463 | furniture | pages [7] -->
m

<!-- b000464 | furniture | pages [7] -->
m

<!-- b000465 | furniture | pages [7] -->
m

<!-- b000466 | furniture | pages [7] -->
m

<!-- b000467 | furniture | pages [7] -->
m

<!-- b000468 | furniture | pages [7] -->
m

<!-- b000469 | furniture | pages [7] -->
m

<!-- b000470 | furniture | pages [7] -->
m

<!-- b000471 | furniture | pages [7] -->
m

<!-- b000472 | furniture | pages [7] -->
m

<!-- b000473 | furniture | pages [7] -->
m

<!-- b000474 | furniture | pages [7] -->
m

<!-- b000475 | furniture | pages [7] -->
m

<!-- b000476 | furniture | pages [7] -->
m

<!-- b000477 | furniture | pages [7] -->
m

<!-- b000478 | furniture | pages [7] -->
m

<!-- b000479 | furniture | pages [7] -->
m

<!-- b000480 | furniture | pages [7] -->
m

<!-- b000481 | furniture | pages [7] -->
m

<!-- b000482 | furniture | pages [7] -->
m

<!-- b000483 | furniture | pages [7] -->
m

<!-- b000484 | furniture | pages [7] -->
m

<!-- b000485 | furniture | pages [7] -->
m

<!-- b000486 | furniture | pages [7] -->
m

<!-- b000487 | furniture | pages [7] -->
m

<!-- b000488 | furniture | pages [7] -->
m

<!-- b000489 | furniture | pages [7] -->
m

<!-- b000490 | furniture | pages [7] -->
m

<!-- b000491 | furniture | pages [7] -->
m

<!-- b000492 | furniture | pages [7] -->
m

<!-- b000493 | furniture | pages [7] -->
m

<!-- b000494 | furniture | pages [7] -->
m

<!-- b000495 | furniture | pages [7] -->
m

<!-- b000496 | furniture | pages [7] -->
m

<!-- b000497 | furniture | pages [7] -->
m

<!-- b000498 | furniture | pages [7] -->
m

<!-- b000499 | furniture | pages [7] -->
m

<!-- b000500 | furniture | pages [7] -->
m

<!-- b000501 | furniture | pages [7] -->
m

<!-- b000502 | furniture | pages [7] -->
m

<!-- b000503 | furniture | pages [7] -->
m

<!-- b000504 | furniture | pages [7] -->
m

<!-- b000505 | furniture | pages [7] -->
m

<!-- b000506 | furniture | pages [7] -->
m

<!-- b000507 | furniture | pages [7] -->
m

<!-- b000508 | furniture | pages [7] -->
m

<!-- b000509 | furniture | pages [7] -->
m

<!-- b000510 | furniture | pages [7] -->
m

<!-- b000511 | furniture | pages [7] -->
m

<!-- b000512 | furniture | pages [7] -->
m

<!-- b000513 | furniture | pages [7] -->
m

<!-- b000514 | furniture | pages [7] -->
m

<!-- b000515 | furniture | pages [7] -->
m

<!-- b000516 | furniture | pages [7] -->
m

<!-- b000517 | furniture | pages [7] -->
m

<!-- b000518 | furniture | pages [7] -->
m

<!-- b000519 | furniture | pages [7] -->
m

<!-- b000520 | furniture | pages [7] -->
m

<!-- b000521 | furniture | pages [7] -->
m

<!-- b000522 | furniture | pages [7] -->
m

<!-- b000523 | furniture | pages [7] -->
m

<!-- b000524 | furniture | pages [7] -->
m

<!-- b000525 | furniture | pages [7] -->
m

<!-- b000526 | furniture | pages [7] -->
m

<!-- b000527 | furniture | pages [7] -->
m

<!-- b000528 | furniture | pages [7] -->
m

<!-- b000529 | furniture | pages [7] -->
m

<!-- b000530 | furniture | pages [7] -->
m

<!-- b000531 | furniture | pages [7] -->
m

<!-- b000532 | furniture | pages [7] -->
m

<!-- b000533 | furniture | pages [7] -->
m

<!-- b000534 | furniture | pages [7] -->
m

<!-- b000535 | furniture | pages [7] -->
m

<!-- b000536 | furniture | pages [7] -->
m

<!-- b000537 | furniture | pages [7] -->
m

<!-- b000538 | furniture | pages [7] -->
m

<!-- b000539 | furniture | pages [7] -->
m

<!-- b000540 | furniture | pages [7] -->
m

<!-- b000541 | furniture | pages [7] -->
m

<!-- b000542 | furniture | pages [7] -->
m

<!-- b000543 | furniture | pages [7] -->
m

<!-- b000544 | furniture | pages [7] -->
m

<!-- b000545 | furniture | pages [7] -->
m

<!-- b000546 | furniture | pages [7] -->
m

<!-- b000547 | furniture | pages [7] -->
m

<!-- b000548 | furniture | pages [7] -->
m

<!-- b000549 | furniture | pages [7] -->
m

<!-- b000550 | furniture | pages [7] -->
m

<!-- b000551 | furniture | pages [7] -->
m

<!-- b000552 | furniture | pages [7] -->
m

<!-- b000553 | furniture | pages [7] -->
m

<!-- b000554 | furniture | pages [7] -->
m

<!-- b000555 | furniture | pages [7] -->
m

<!-- b000556 | furniture | pages [7] -->
m

<!-- b000557 | furniture | pages [7] -->
m

<!-- b000558 | furniture | pages [7] -->
m

<!-- b000559 | furniture | pages [7] -->
m

<!-- b000560 | furniture | pages [7] -->
m

<!-- b000561 | furniture | pages [7] -->
m

<!-- b000562 | furniture | pages [7] -->
m

<!-- b000563 | furniture | pages [7] -->
m

<!-- b000564 | furniture | pages [7] -->
m

<!-- b000565 | furniture | pages [7] -->
m

<!-- b000566 | furniture | pages [7] -->
m

<!-- b000567 | furniture | pages [7] -->
m

<!-- b000568 | furniture | pages [7] -->
m

<!-- b000569 | furniture | pages [7] -->
m

<!-- b000570 | furniture | pages [7] -->
m

<!-- b000571 | furniture | pages [7] -->
m

<!-- b000572 | furniture | pages [7] -->
m

<!-- b000573 | furniture | pages [7] -->
m

<!-- b000574 | furniture | pages [7] -->
m

<!-- b000575 | furniture | pages [7] -->
m

<!-- b000576 | furniture | pages [7] -->
m

<!-- b000577 | furniture | pages [7] -->
m

<!-- b000578 | furniture | pages [7] -->
m

<!-- b000579 | furniture | pages [7] -->
m

<!-- b000580 | furniture | pages [7] -->
m

<!-- b000581 | furniture | pages [7] -->
m

<!-- b000582 | furniture | pages [7] -->
m

<!-- b000583 | furniture | pages [7] -->
m

<!-- b000584 | furniture | pages [7] -->
m

<!-- b000585 | furniture | pages [7] -->
m

<!-- b000586 | furniture | pages [7] -->
m

<!-- b000587 | furniture | pages [7] -->
m

<!-- b000588 | furniture | pages [7] -->
m

<!-- b000589 | furniture | pages [7] -->
m

<!-- b000590 | furniture | pages [7] -->
m

<!-- b000591 | furniture | pages [7] -->
m

<!-- b000592 | furniture | pages [7] -->
m

<!-- b000593 | furniture | pages [7] -->
m

<!-- b000594 | furniture | pages [7] -->
m

<!-- b000595 | furniture | pages [7] -->
m

<!-- b000596 | furniture | pages [7] -->
m

<!-- b000597 | furniture | pages [7] -->
m

<!-- b000598 | furniture | pages [7] -->
m

<!-- b000599 | furniture | pages [7] -->
m

<!-- b000600 | furniture | pages [7] -->
m

<!-- b000601 | furniture | pages [7] -->
m

<!-- b000602 | furniture | pages [7] -->
m

<!-- b000603 | furniture | pages [7] -->
m

<!-- b000604 | furniture | pages [7] -->
m

<!-- b000605 | furniture | pages [7] -->
m

<!-- b000606 | furniture | pages [7] -->
m

<!-- b000607 | furniture | pages [7] -->
m

<!-- b000608 | furniture | pages [7] -->
m

<!-- b000609 | furniture | pages [7] -->
m

<!-- b000610 | furniture | pages [7] -->
m

<!-- b000611 | furniture | pages [7] -->
m

<!-- b000612 | furniture | pages [7] -->
m

<!-- b000613 | furniture | pages [7] -->
m

<!-- b000614 | furniture | pages [7] -->
m

<!-- b000615 | furniture | pages [7] -->
m

<!-- b000616 | furniture | pages [7] -->
m

<!-- b000617 | furniture | pages [7] -->
m

<!-- b000618 | furniture | pages [7] -->
m

<!-- b000619 | furniture | pages [7] -->
m

<!-- b000620 | furniture | pages [7] -->
m

<!-- b000621 | furniture | pages [7] -->
m

<!-- b000622 | furniture | pages [7] -->
m

<!-- b000623 | furniture | pages [7] -->
m

<!-- b000624 | furniture | pages [7] -->
m

<!-- b000625 | furniture | pages [7] -->
m

<!-- b000626 | furniture | pages [7] -->
m

<!-- b000627 | furniture | pages [7] -->
m

<!-- b000628 | furniture | pages [7] -->
m

<!-- b000629 | furniture | pages [7] -->
m

<!-- b000630 | furniture | pages [7] -->
m

<!-- b000631 | furniture | pages [7] -->
m

<!-- b000632 | furniture | pages [7] -->
m

<!-- b000633 | furniture | pages [7] -->
m

<!-- b000634 | furniture | pages [7] -->
m

<!-- b000635 | furniture | pages [7] -->
m

<!-- b000636 | furniture | pages [7] -->
m

<!-- b000637 | furniture | pages [7] -->
m

<!-- b000638 | furniture | pages [7] -->
m

<!-- b000639 | furniture | pages [7] -->
m

<!-- b000640 | furniture | pages [7] -->
m

<!-- b000641 | furniture | pages [7] -->
m

<!-- b000642 | furniture | pages [7] -->
m

<!-- b000643 | furniture | pages [7] -->
m

<!-- b000644 | furniture | pages [7] -->
m

<!-- b000645 | furniture | pages [7] -->
m

<!-- b000646 | furniture | pages [7] -->
m

<!-- b000647 | furniture | pages [7] -->
m

<!-- b000648 | furniture | pages [7] -->
m

<!-- b000649 | furniture | pages [7] -->
m

<!-- b000650 | furniture | pages [7] -->
m

<!-- b000651 | furniture | pages [7] -->
m

<!-- b000652 | furniture | pages [7] -->
m

<!-- b000653 | furniture | pages [7] -->
m

<!-- b000654 | furniture | pages [7] -->
m

<!-- b000655 | furniture | pages [7] -->
m

<!-- b000656 | furniture | pages [7] -->
m

<!-- b000657 | furniture | pages [7] -->
m

<!-- b000658 | furniture | pages [7] -->
m

<!-- b000659 | furniture | pages [7] -->
m

<!-- b000660 | furniture | pages [7] -->
m

<!-- b000661 | furniture | pages [7] -->
m

<!-- b000662 | furniture | pages [7] -->
m

<!-- b000663 | furniture | pages [7] -->
m

<!-- b000664 | furniture | pages [7] -->
m

<!-- b000665 | furniture | pages [7] -->
m

<!-- b000666 | furniture | pages [7] -->
m

<!-- b000667 | furniture | pages [7] -->
m

<!-- b000668 | furniture | pages [7] -->
m

<!-- b000669 | furniture | pages [7] -->
m

<!-- b000670 | furniture | pages [7] -->
m

<!-- b000671 | furniture | pages [7] -->
m

<!-- b000672 | furniture | pages [7] -->
m

<!-- b000673 | furniture | pages [7] -->
m

<!-- b000674 | furniture | pages [7] -->
m

<!-- b000675 | furniture | pages [7] -->
m

<!-- b000676 | furniture | pages [7] -->
m

<!-- b000677 | furniture | pages [7] -->
m

<!-- b000678 | furniture | pages [7] -->
m

<!-- b000679 | furniture | pages [7] -->
m

<!-- b000680 | furniture | pages [7] -->
m

<!-- b000681 | furniture | pages [7] -->
m

<!-- b000682 | furniture | pages [7] -->
m

<!-- b000683 | furniture | pages [7] -->
m

<!-- b000684 | furniture | pages [7] -->
m

<!-- b000685 | furniture | pages [7] -->
m

<!-- b000686 | furniture | pages [7] -->
m

<!-- b000687 | furniture | pages [7] -->
m

<!-- b000688 | furniture | pages [7] -->
m

<!-- b000689 | furniture | pages [7] -->
m

<!-- b000690 | furniture | pages [7] -->
m

<!-- b000691 | furniture | pages [7] -->
m

<!-- b000692 | furniture | pages [7] -->
m

<!-- b000693 | furniture | pages [7] -->
m

<!-- b000694 | furniture | pages [7] -->
m

<!-- b000695 | furniture | pages [7] -->
m

<!-- b000696 | furniture | pages [7] -->
m

<!-- b000697 | furniture | pages [7] -->
m

<!-- b000698 | furniture | pages [7] -->
m

<!-- b000699 | furniture | pages [7] -->
m

<!-- b000700 | furniture | pages [7] -->
m

<!-- b000701 | furniture | pages [7] -->
m

<!-- b000702 | furniture | pages [7] -->
m

<!-- b000703 | furniture | pages [7] -->
m

<!-- b000704 | furniture | pages [7] -->
m

<!-- b000705 | furniture | pages [7] -->
m

<!-- b000706 | furniture | pages [7] -->
m

<!-- b000707 | furniture | pages [7] -->
m

<!-- b000708 | furniture | pages [7] -->
m

<!-- b000709 | furniture | pages [7] -->
m

<!-- b000710 | furniture | pages [7] -->
m

<!-- b000711 | furniture | pages [7] -->
m

<!-- b000712 | furniture | pages [7] -->
m

<!-- b000713 | furniture | pages [7] -->
m

<!-- b000714 | furniture | pages [7] -->
m

<!-- b000715 | furniture | pages [7] -->
m

<!-- b000716 | furniture | pages [7] -->
m

<!-- b000717 | furniture | pages [7] -->
m

<!-- b000718 | furniture | pages [7] -->
m

<!-- b000719 | furniture | pages [7] -->
m

<!-- b000720 | furniture | pages [7] -->
m

<!-- b000721 | furniture | pages [7] -->
m

<!-- b000722 | furniture | pages [7] -->
m

<!-- b000723 | furniture | pages [7] -->
m

<!-- b000724 | furniture | pages [7] -->
m

<!-- b000725 | furniture | pages [7] -->
m

<!-- b000726 | furniture | pages [7] -->
m

<!-- b000727 | furniture | pages [7] -->
m

<!-- b000728 | furniture | pages [7] -->
m

<!-- b000729 | furniture | pages [7] -->
m

<!-- b000730 | furniture | pages [7] -->
m

<!-- b000731 | furniture | pages [7] -->
m

<!-- b000732 | furniture | pages [7] -->
m

<!-- b000733 | furniture | pages [7] -->
m

<!-- b000734 | furniture | pages [7] -->
m

<!-- b000735 | furniture | pages [7] -->
m

<!-- b000736 | furniture | pages [7] -->
m

<!-- b000737 | furniture | pages [7] -->
m

<!-- b000738 | furniture | pages [7] -->
m

<!-- b000739 | furniture | pages [7] -->
m

<!-- b000740 | furniture | pages [7] -->
m

<!-- b000741 | furniture | pages [7] -->
m

<!-- b000742 | furniture | pages [7] -->
m

<!-- b000743 | furniture | pages [7] -->
m

<!-- b000744 | furniture | pages [7] -->
m

<!-- b000745 | furniture | pages [7] -->
m

<!-- b000746 | furniture | pages [7] -->
m

<!-- b000747 | furniture | pages [7] -->
m

<!-- b000748 | furniture | pages [7] -->
m

<!-- b000749 | furniture | pages [7] -->
m

<!-- b000750 | furniture | pages [7] -->
m

<!-- b000751 | furniture | pages [7] -->
m

<!-- b000752 | furniture | pages [7] -->
m

<!-- b000753 | furniture | pages [7] -->
m

<!-- b000754 | furniture | pages [7] -->
m

<!-- b000755 | furniture | pages [7] -->
m

<!-- b000756 | furniture | pages [7] -->
m

<!-- b000757 | furniture | pages [7] -->
m

<!-- b000758 | furniture | pages [7] -->
m

<!-- b000759 | furniture | pages [7] -->
m

<!-- b000760 | furniture | pages [7] -->
m

<!-- b000761 | furniture | pages [7] -->
m

<!-- b000762 | furniture | pages [7] -->
m

<!-- b000763 | furniture | pages [7] -->
m

<!-- b000764 | furniture | pages [7] -->
m

<!-- b000765 | furniture | pages [7] -->
m

<!-- b000766 | furniture | pages [7] -->
m

<!-- b000767 | furniture | pages [7] -->
m

<!-- b000768 | furniture | pages [7] -->
m

<!-- b000769 | furniture | pages [7] -->
m

<!-- b000770 | furniture | pages [7] -->
m

<!-- b000771 | furniture | pages [7] -->
m

<!-- b000772 | furniture | pages [8] -->
Team 2524070

<!-- b000773 | furniture | pages [8] -->
Page 8of 25

<!-- b000775 | prose | pages [8] -->
We propose that there are two distinct scenarios that may result in a value of zero. The first scenario occurs when a nation has the potential to secure a medal but ultimately fails to do so due to random factors; we categorize this type of zero value as a sampling zero, signifying that it is merely a random outcome derived from sampling. The second scenario arises when a nation lacks the requisite strength in a particular sport and, as a result, has no realistic chance of winning a medal; we designate this type of zero value as a structural zero. Subsequently, we will model the occurrence of zero values as a Bernoulli distribution process, which will be executed through logistic regression, as follows:

<!-- b000776 | prose | pages [8] -->
1 𝑝0 = 𝑃(𝑌= 0) = (3) 1 + 𝑒−𝜆 3 6 9 ∑︁ ∑︁ ∑︁ 𝜆= 𝛼0 + 𝛼𝑖𝑛𝑔𝑜𝑙𝑑,𝑖+ 𝛼𝑖𝑛𝑠𝑖𝑙𝑣𝑒𝑟,𝑖−3 + 𝛼𝑖𝑛𝑏𝑟𝑜𝑛𝑧𝑒,𝑖−6 + 𝑐𝑜𝑢𝑛𝑡𝑟𝑦 (4) 𝑖=7 𝑖=1 𝑖=4 𝑐𝑜𝑢𝑛𝑡𝑟𝑦∼N(0, 𝜎2 𝑐) (5)

<!-- b000777 | prose | pages [8] -->
In this analysis, we incorporate a random effect for the variable ’country’ to examine the variations in medal counts among various countries. This random effect is denoted as ’country’.

<!-- b000778 | heading | pages [8] -->
4.3 Zero-Inflated Negative Binomial Model

<!-- b000779 | prose | pages [8] -->
We integrate the zero-inflated model with the negative binomial model to create the Zero-Inflated

<!-- b000780 | heading | pages [8] -->
Negative Binomial model, ZINB:

<!-- b000781 | prose | pages [8] -->
1 𝑝0 = 1 + 𝑒−𝜆, 𝑦= 0  𝑃(𝑌= 𝑦) = (6) 𝑦 𝜙 𝜇 𝜙   (1 −𝑝0)𝑃(𝑌= 𝑦|𝑌> 0) = (1 −𝑝0) 𝑦+𝜙−1 , 𝑦> 0  𝑦 𝜇+𝜙 𝜇+𝜙

<!-- b000782 | prose | pages [8] -->
This model typically consists of two components: one part employs a binomial distribution to model the generation of zeros, while the other utilizes a negative binomial distribution to characterize the non-zero values. This dual structure enables the model to effectively address both actual zero counts and non-zero count data simultaneously.

<!-- b000783 | heading | pages [8] -->
4.4 Fitting the Model Using Bayesian Inference and MCMC

<!-- b000784 | prose | pages [8] -->
In this problem, we utilized Bayesian inference in conjunction with Markov Chain Monte Carlo(MCMC) methods to fit the model and derive its posterior distribution. Bayesian inference allows for the integration of prior knowledge or beliefs regarding the parameters, which can sub- sequently be updated in light of the observed data. The application of MCMC techniques enables efficient sampling from the posterior distribution, particularly in scenarios where direct computation is challenging or unfeasible. The detailed procedural framework of the algorithm is illustrated in the following diagram.

<!-- b000785 | prose | pages [8, 9] -->
关注数学模型 微信公众号：数学模型

<!-- b000786 | furniture | pages [8] -->
2

<!-- b000787 | furniture | pages [8] -->
MATHmodels

<!-- b000788 | furniture | pages [8] -->
获取更多资讯

<!-- b000789 | furniture | pages [9] -->
Team 2524070

<!-- b000790 | furniture | pages [9] -->
Page 9of 25

<!-- b000792 | heading | pages [9] -->
Algorithm 1 MCMC Algorithm for Bayesian Model Fitting with Multiple Chains

<!-- b000793 | prose | pages [9] -->
1: Input: Data {𝑦𝑖, 𝑋𝑖}, initial parameter values 𝜃(0) 2: Output: Samples from the posterior distribution of 𝜃 3: Initialization: Set initial values for the model parameters:

<!-- b000794 | prose | pages [9] -->
𝜃(0) = {𝛽0, 𝛽1, . . . , 𝛽5, 𝛼0, 𝛼1, . . . , 𝛼9, 𝜇, 𝜙} 4:

<!-- b000795 | prose | pages [9] -->
where 𝛽are the negative binomial regression coefficients, 𝛼are the zero-inflation coefficients, 5:

<!-- b000796 | prose | pages [9] -->
and 𝜇and 𝜙are the parameters of the negative binomial distribution. 6: Initialize chains: Run 𝐶parallel chains, each starting with random initial values of 𝜃(0) for chain 𝑐 𝑐∈{1, 2, . . . , 𝐶} 7: for each chain 𝑐= 1, . . . , 𝐶do 微信号：MATHmodels for each iteration 𝑡= 1, . . . ,𝑇do 8:

<!-- b000797 | heading | pages [9] -->
Step 1: Compute the log-likelihood of the model with current parameter values:

<!-- b000798 | prose | pages [9] -->
9:

<!-- b000799 | prose | pages [9] -->
𝑁 ∑︁ log(𝑝(𝑦𝑖|𝜃𝑐)) log-likelihood𝑐= 𝑖=1

<!-- b000800 | prose | pages [9] -->
where 𝑝(𝑦𝑖|𝜃𝑐) is the likelihood of the data given the parameters for chain 𝑐.

<!-- b000801 | prose | pages [9] -->
Step 2: Calculate the posterior distribution using Bayes’ Theorem: 10:

<!-- b000802 | prose | pages [9] -->
𝑝(𝜃𝑐|data) ∝𝑝(data|𝜃𝑐) · 𝑝(𝜃𝑐)

<!-- b000803 | prose | pages [9] -->
where 𝑝(data|𝜃𝑐) is the likelihood, and 𝑝(𝜃𝑐) is the prior distribution for chain 𝑐.

<!-- b000804 | prose | pages [9] -->
Step 3: Propose new values for the parameters 𝜃∗ 𝑐= {𝛽∗ 0, 𝛽∗ 1, . . . , 𝜇∗, 𝜙∗} using a proposal 11:

<!-- b000805 | prose | pages [9] -->
distribution.

<!-- b000806 | prose | pages [9] -->
Step 4: Calculate the acceptance probability for the new parameter set: 12:

<!-- b000807 | prose | pages [9] -->
1, 𝑝(𝜃∗ 𝑐|data)   𝐴(𝜃∗ 𝑐→𝜃𝑐) = min 𝑝(𝜃𝑐|data)

<!-- b000808 | prose | pages [9] -->
if a random number 𝑢∼𝑈(0, 1) is less than the acceptance probability 𝐴then 13:

<!-- b000809 | prose | pages [9] -->
Accept the new parameter set: 𝜃(𝑡) = 𝜃∗ 14: 𝑐 𝑐 else 15: Reject the new parameter set: 𝜃(𝑡) = 𝜃(𝑡−1) 16: 𝑐 𝑐 end if 17:

<!-- b000810 | prose | pages [9] -->
end for 18: 19: end for 20: Return: The concatenated set of accepted parameter samples from all chains:

<!-- b000811 | prose | pages [9] -->
1 , . . . , 𝜃(𝑇) 𝐶, . . . , 𝜃(𝑇) n o 𝜃(1) 1 , 𝜃(2) 1 , . . . , 𝜃(1) 𝐶, 𝜃(2) 𝜃= 𝐶

<!-- b000812 | furniture | pages [10] -->
Team 2524070

<!-- b000813 | furniture | pages [10] -->
Page 10of 25

<!-- b000814 | heading | pages [10] -->
4.5 Problem Solutions

<!-- b000815 | prose | pages [10] -->
We have previously derived the posterior distributions of the parameters associated with the zero- inflated negative binomial regression model using MCMC methods. To determine the medal standings of various nations for the year 2028, we employ simulation techniques to estimate the medal outcomes for each country. The detailed algorithmic procedure is outlined as follows:

<!-- b000816 | heading | pages [10] -->
Algorithm 2 Bayesian Zero-Inflated Negative Binomial Model Prediction

<!-- b000817 | prose | pages [10] -->
1: Input: Trained Bayesian model, new data 𝑋new 2: Output: Point estimate and prediction interval 3: 1. Get posterior samples: 𝜃(𝑠) ∼𝑝(𝜃|𝑋,𝑌) 4: 2. Make predictions for new data: 5: for 𝑠= 1 to 𝑆do Compute 𝑝(𝑠) and 𝜇(𝑠) 6: 0 Sample 𝑦(𝑠) new ∼NegBin(𝜇(𝑠), 𝜃(𝑠) disp) 7:

<!-- b000818 | prose | pages [10] -->
With probability 1 −𝑝(𝑠) 0 , set 𝑦(𝑠) 8: new 9: end for 10: 3. Point estimate: 𝑠=1 𝑦(𝑠) Í𝑆 11: Compute point estimate ˆ𝑦new = 1 𝑆 new 12: 4. Prediction interval: 13: Calculate the 2.5 14: 5. Output: Return ˆ𝑦new and the prediction interval

<!-- b000819 | prose | pages [10] -->
Based on the construction of the previous zero-inflated negative binomial model, we choose to use the zero-inflation factor to evaluate the likelihood of these nations achieving their first medal at the 2028 Los Angeles Olympics. The relevant formula can be expressed as follows:

<!-- b000820 | prose | pages [10] -->
1 𝑃(𝑖) 𝑓𝑖𝑟𝑠𝑡= 1 − 1 + 𝑒−𝜆𝑖 3 6 9 ∑︁ ∑︁ ∑︁ 𝜆𝑖= 𝛼0 + 𝛼𝑖𝑛𝑔𝑜𝑙𝑑,𝑖+ 𝛼𝑖𝑛𝑠𝑖𝑙𝑣𝑒𝑟,𝑖−3 + 𝛼𝑖𝑛𝑏𝑟𝑜𝑛𝑧𝑒,𝑖−6 + 𝑐𝑜𝑢𝑛𝑡𝑟𝑦𝑖 𝑖=7 𝑖=1 𝑖=4 = 𝛼0 + 𝑐𝑜𝑢𝑛𝑡𝑟𝑦𝑖

<!-- b000821 | prose | pages [10] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000822 | heading | pages [10] -->
4.6 Results

<!-- b000823 | prose | pages [10] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Based on analytical assessments, the anticipated medal rankings for the 2028 Los Angeles Olympics m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m are as follows. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000824 | prose | pages [10, 11, 12] -->
关注数学模型 微信公众号：数学模型 微信号：MATHmodels To evaluate the performance of countries in 2028 relative to 2024, we identified the twenty countries predicted to win the most medals in 2028 and the twenty countries that ranked highest in the 2024 medal standings for our analysis. Here are the findings.

<!-- b000825 | furniture | pages [10] -->
2

<!-- b000826 | furniture | pages [10] -->
MATHmodels

<!-- b000827 | furniture | pages [10] -->
获取更多资讯

<!-- b000828 | furniture | pages [11] -->
Team 2524070

<!-- b000829 | furniture | pages [11] -->
Page 11of 25

<!-- b000831 | furniture | pages [12] -->
Team 2524070

<!-- b000832 | furniture | pages [12] -->
Page 12of 25

<!-- b000834 | caption | pages [12] -->
Figure 4: Comparison of the top twenty predicted medal-winning countries in 2028 with the highest-

<!-- b000835 | prose | pages [12] -->
ranked countries in the 2024 medal standings.Russia, Poland, and Cuba are anticipated to break into the top twenty, while Uzbekistan, Iran, Kenya, and Sweden are expected to fall short. The United States, Japan, Germany, and Ukraine are projected to earn more medals than they did in 2024, whereas China, Great Britain, France, Australia, Italy, the Netherlands, South Korea, Canada, Brazil, Hungary, and Spain are expected to win fewer medals. New Zealand’s medal count is anticipated to remain unchanged.

<!-- b000836 | prose | pages [12] -->
The anticipated medal distribution for the leading six countries in the 2028 medal standings is projected to be as follows.

<!-- b000837 | caption | pages [12] -->
Figure 5: Predicted Medal Distribution for Top 6 Nations at LA28.

<!-- b000838 | prose | pages [12] -->
The following six nations have the potential to secure their inaugural Olympic medal at the 2028 Los Angeles Games.

<!-- b000839 | prose | pages [12, 13] -->
关注数学模型 微信公众号：数学模型

<!-- b000840 | furniture | pages [12] -->
2

<!-- b000841 | furniture | pages [12] -->
MATHmodels

<!-- b000842 | furniture | pages [12] -->
获取更多资讯

<!-- b000843 | furniture | pages [13] -->
Team 2524070

<!-- b000844 | furniture | pages [13] -->
Page 13of 25

<!-- b000845 | caption | pages [13] -->
Figure 6: The top six nations poised to win the inaugural medal at the Los Angeles Olympics.

<!-- b000847 | heading | pages [13] -->
4.7 Model Assessment

<!-- b000848 | prose | pages [13] -->
Due to space limitations, only the performance evaluation and uncertainty measurement of the gold medal count prediction model are presented. The analysis process for the other models is similar, and the results are comparable.

<!-- b000849 | prose | pages [13] -->
According to the findings from MCMC, the parameter estimates for the zero-inflated negative binomial model and the highest density interval (HDI) are as follows: the standard errors for each parameter are quite small, indicating minimal uncertainty associated with each estimate. 微信号：MATHmodels The table also presents the Rhat and Effective Sample Size (ESS) values for each parameter. In this model, all Rhat values are 1.00, indicating that all parameters have converged, which reflects excellent model convergence. The Bulk ESS values for all parameters are substantial, suggesting that the MCMC chains provide a sufficient number of effective samples, thereby enhancing the reliability of the results. Additionally, the Tail ESS values are also high, indicating that the model possesses an adequate number of effective samples in the tail region, which ensures that the estimation of extreme predictions is equally reliable.

<!-- b000850 | prose | pages [13] -->
Estimate 95% HDI Rhat Bulk ESS Tail ESS 𝛽0 -0.05 -0.49-0.38 1.00 24043 10826 𝛽1 0.41 0.38-0.44 1.00 11050 10315 𝛽2 0.28 0.24-0.31 1.00 10853 9464 𝛽3 0.22 0.19-0.26 1.00 11291 10474 𝛽4 0.00 -0.00-0.00 1.00 25202 10858 𝛽5 10.47 9.55-11.36 1.00 13949 11491 𝜎2 2.53 2.46-2.60 1.00 13927 11230 𝑐

<!-- b000851 | caption | pages [13] -->
Table 3: Model Estimates with Uncertainty Intervals, Rhat, and ESS values

<!-- b000852 | prose | pages [13] -->
5 How Events of Various Sports Impact the Results?

<!-- b000853 | heading | pages [13] -->
5.1 Establishment of Indicators

<!-- b000854 | prose | pages [13] -->
This section aims to investigate the influence of events on the outcomes of the Olympic Games. Specifically, we seek to determine whether the number of events within each discipline for each Olympic game, as well as the types of events, affect the performance of participating countries, thereby impacting the overall medal standings.

<!-- b000855 | furniture | pages [14] -->
Team 2524070

<!-- b000856 | furniture | pages [14] -->
Page 14of 25

<!-- b000857 | prose | pages [14] -->
To analyze this phenomenon, it is essential to establish several key indicators. For a given country (designated as A) participating in a specific Olympic Games, let p denote the total number of events conducted, q represent the total number of events in which country A participated, and s signify the total number of events in which country A secured medals (i.e., the total number of medals awarded to country A). Furthermore, for a particular discipline i, let a indicate the total number of events held, b represent the number of events in discipline i that country A participated in, and c denote the total number of medals won by country A in that discipline. To facilitate this analysis, it is necessary to filter the athletes and programs data. It is noteworthy that discrepancies were identified in the notation of sport within the athletes dataset, which correspond to discipline outlined in the programs dataset.

<!-- b000858 | prose | pages [14] -->
Meaning Method of Calculation Explanation Discipline Indicators

<!-- b000859 | prose | pages [14] -->
b/q Proficiency level Type influencing factor Xi i b/p Number influencing factor Popularity level yi c/s Discipline importance factor Award winning ability Zi

<!-- b000860 | caption | pages [14] -->
Table 4: Relevant Indicators

<!-- b000861 | prose | pages [14] -->
Consequently, by considering both the quantity and type of events, we can derive a comprehensive indicator reflecting the competitive advantage of discipline i for country A. We propose the following indicators:

<!-- b000862 | prose | pages [14] -->
(7) φi = ω1xi + ω2yi

<!-- b000863 | prose | pages [14] -->
In this context, ω1 and ω2 are designated weights, and a higher value of φindicates a greater advantage of discipline i for country A.

<!-- b000864 | heading | pages [14] -->
5.2 Events-Medals Association Rule Model Based on GRI Algorithm

<!-- b000865 | prose | pages [14] -->
The correlation between events and medal counts can be examined through the application of association rule models. Association analysis reveals causal relationships among sets of items by categorizing various data item sets as either antecedents or consequents. In summary, the formal representation of association rules is as follows: (mc denotes the counts of medals).

<!-- b000866 | prose | pages [14] -->
if antecedent → consequent if φi → mc

<!-- b000867 | prose | pages [14] -->
Association analysis can be conducted using various algorithms, with the GRI algorithm and the Apriori algorithm being among the most prevalent. This study employs the GRI algorithm due to its advantages over the Apriori algorithm, particularly in minimizing the generation of redundant rules through the incorporation of concepts such as interaction entropy and information gain, thereby enhancing the efficiency of rule discovery. Furthermore, given the extensive range of disciplines involved, the GRI algorithm demonstrates greater adaptability in exploring rules within large item sets compared to the Apriori algorithm.

<!-- b000868 | prose | pages [14, 15] -->
关注数学模型 The fundamental principle of the GRI algorithm can be expressed through a specific formula, which delineates the disparity between the probability of 𝑚𝑐occurring in the presence of 𝜑𝑖and the overall probability of 𝑚𝑐.

<!-- b000869 | furniture | pages [14] -->
获取更多资讯

<!-- b000870 | furniture | pages [15] -->
Team 2524070

<!-- b000871 | furniture | pages [15] -->
Page 15of 25

<!-- b000873 | prose | pages [15] -->
𝑝(𝑚𝑐|𝜑𝑖)𝑙𝑜𝑔𝑃(𝑚𝑐|𝜑𝑖) + (1 −𝑝(𝑚𝑐|𝜑𝑖))𝑙𝑜𝑔1 −𝑝(𝑚𝑐|𝜑𝑖)   𝐽(𝑚𝑐|𝜑𝑖) = 𝑝(𝜑𝑖) (8) 𝑝(𝑚𝑐) 1 −𝑝(𝑚𝑐) 微信公众号：数学模型 Utilizing the aforementioned algorithm, we conducted an analysis of data from the 29 Summer Olympic Games in which the United States has participated, spanning the years 1896 to 2024. In accordance with Formula 7, we assigned a value of 0.5 to both 𝜔1 and 𝜔2, reflecting the equal significance attributed to the type factor and the number factor of events. Following this, we computed 𝜑𝑖for 65 disciplines based on the established formula, with select data presented in Table 5.

<!-- b000874 | prose | pages [15] -->
Year Wrestling(𝜑1) Athletics(𝜑2) Golf(𝜑3) Rowing(𝜑4) Fencing(𝜑5) Swimming(𝜑6) ...... 𝑚𝑐 1896 0 0.617 0 0 0 0.061 20 1900 0 0.648 0.068 0.011 0.034 0.023 48 微信号：MATHmodels 1904 0.160 0.611 0.042 0.097 0.097 0.153 231 ...... 1908 0.052 0.554 0 0 0 0.073 47 1912 0.009 0.597 0 0 0.036 0.071 64 1920 0.085 0.339 0 0.024 0.036 0.145 95 ...... 2016 0.045 0.236 0.010 0.035 0.035 0.182 121 2020 0.047 0.218 0.012 0.028 0.040 0.165 ...... 113 2024 0.051 0.250 0.009 0.038 0.041 0.161 126

<!-- b000875 | caption | pages [15] -->
Table 5: Events-Medals Data Matrix

<!-- b000876 | prose | pages [15] -->
For the variable 𝜑𝑖, classification is Association rules necessitate the classification of data. conducted using the threshold 𝑄0.5; values exceeding 𝑄0.5 are designated as 1, signifying that the discipline is advantageous, while values that are less than or equal to 𝑄0.5 are assigned a value of -1, indicating a normative status. In relation to the variable mc, its quantitative representation is illustrated in Figure 4. This variable is categorized into three segments: high, low, and normal, based on the prevailing conditions in the United States, with corresponding values of 1, 0, and -1, respectively.

<!-- b000877 | caption | pages [15] -->
Figure 7: Total Medal Count of the USA in Past Summer Olympics

<!-- b000878 | prose | pages [15, 16] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Consequently, we construct a data matrix of dimensions 29 by 66 and employ the GRI algorithm to extract the following robust association rules:

<!-- b000879 | furniture | pages [15] -->
m

<!-- b000880 | furniture | pages [15] -->
m

<!-- b000881 | furniture | pages [15] -->
m

<!-- b000882 | furniture | pages [15] -->
m

<!-- b000883 | furniture | pages [15] -->
m

<!-- b000884 | furniture | pages [15] -->
m

<!-- b000885 | furniture | pages [15] -->
m

<!-- b000886 | furniture | pages [15] -->
m

<!-- b000887 | furniture | pages [15] -->
m

<!-- b000888 | furniture | pages [15] -->
m

<!-- b000889 | furniture | pages [15] -->
m

<!-- b000890 | furniture | pages [15] -->
m

<!-- b000891 | furniture | pages [15] -->
m

<!-- b000892 | furniture | pages [15] -->
m

<!-- b000893 | furniture | pages [15] -->
m

<!-- b000894 | furniture | pages [15] -->
m

<!-- b000895 | furniture | pages [15] -->
m

<!-- b000896 | furniture | pages [15] -->
m

<!-- b000897 | furniture | pages [15] -->
m

<!-- b000898 | furniture | pages [15] -->
m

<!-- b000899 | furniture | pages [15] -->
m

<!-- b000900 | furniture | pages [15] -->
m

<!-- b000901 | furniture | pages [15] -->
m

<!-- b000902 | furniture | pages [15] -->
m

<!-- b000903 | furniture | pages [15] -->
m

<!-- b000904 | furniture | pages [15] -->
m

<!-- b000905 | furniture | pages [15] -->
m

<!-- b000906 | furniture | pages [15] -->
m

<!-- b000907 | furniture | pages [15] -->
m

<!-- b000908 | furniture | pages [15] -->
m

<!-- b000909 | furniture | pages [15] -->
m

<!-- b000910 | furniture | pages [15] -->
m

<!-- b000911 | furniture | pages [15] -->
m

<!-- b000912 | furniture | pages [15] -->
m

<!-- b000913 | furniture | pages [15] -->
m

<!-- b000914 | furniture | pages [15] -->
m

<!-- b000915 | furniture | pages [15] -->
m

<!-- b000916 | furniture | pages [15] -->
m

<!-- b000917 | furniture | pages [15] -->
m

<!-- b000918 | furniture | pages [15] -->
m

<!-- b000919 | furniture | pages [15] -->
m

<!-- b000920 | furniture | pages [15] -->
m

<!-- b000921 | furniture | pages [15] -->
m

<!-- b000922 | furniture | pages [15] -->
m

<!-- b000923 | furniture | pages [15] -->
m

<!-- b000924 | furniture | pages [15] -->
m

<!-- b000925 | furniture | pages [15] -->
m

<!-- b000926 | furniture | pages [15] -->
m

<!-- b000927 | furniture | pages [15] -->
m

<!-- b000928 | furniture | pages [15] -->
m

<!-- b000929 | furniture | pages [15] -->
m

<!-- b000930 | furniture | pages [15] -->
m

<!-- b000931 | furniture | pages [15] -->
m

<!-- b000932 | furniture | pages [15] -->
m

<!-- b000933 | furniture | pages [15] -->
m

<!-- b000934 | furniture | pages [15] -->
m

<!-- b000935 | furniture | pages [15] -->
m

<!-- b000936 | furniture | pages [15] -->
m

<!-- b000937 | furniture | pages [15] -->
m

<!-- b000938 | furniture | pages [15] -->
m

<!-- b000939 | furniture | pages [15] -->
m

<!-- b000940 | furniture | pages [15] -->
m

<!-- b000941 | furniture | pages [15] -->
m

<!-- b000942 | furniture | pages [15] -->
m

<!-- b000943 | furniture | pages [15] -->
m

<!-- b000944 | furniture | pages [15] -->
m

<!-- b000945 | furniture | pages [15] -->
m

<!-- b000946 | furniture | pages [15] -->
m

<!-- b000947 | furniture | pages [15] -->
m

<!-- b000948 | furniture | pages [15] -->
m

<!-- b000949 | furniture | pages [15] -->
m

<!-- b000950 | furniture | pages [15] -->
m

<!-- b000951 | furniture | pages [15] -->
m

<!-- b000952 | furniture | pages [15] -->
m

<!-- b000953 | furniture | pages [15] -->
m

<!-- b000954 | furniture | pages [15] -->
m

<!-- b000955 | furniture | pages [15] -->
m

<!-- b000956 | furniture | pages [15] -->
m

<!-- b000957 | furniture | pages [15] -->
m

<!-- b000958 | furniture | pages [15] -->
m

<!-- b000959 | furniture | pages [15] -->
m

<!-- b000960 | furniture | pages [15] -->
m

<!-- b000961 | furniture | pages [15] -->
m

<!-- b000962 | furniture | pages [15] -->
m

<!-- b000963 | furniture | pages [15] -->
m

<!-- b000964 | furniture | pages [15] -->
m

<!-- b000965 | furniture | pages [15] -->
m

<!-- b000966 | furniture | pages [15] -->
m

<!-- b000967 | furniture | pages [15] -->
m

<!-- b000968 | furniture | pages [15] -->
m

<!-- b000969 | furniture | pages [15] -->
m

<!-- b000970 | furniture | pages [15] -->
m

<!-- b000971 | furniture | pages [15] -->
m

<!-- b000972 | furniture | pages [15] -->
m

<!-- b000973 | furniture | pages [15] -->
m

<!-- b000974 | furniture | pages [15] -->
m

<!-- b000975 | furniture | pages [15] -->
m

<!-- b000976 | furniture | pages [15] -->
m

<!-- b000977 | furniture | pages [15] -->
m

<!-- b000978 | furniture | pages [15] -->
m

<!-- b000979 | furniture | pages [15] -->
m

<!-- b000980 | furniture | pages [15] -->
m

<!-- b000981 | furniture | pages [15] -->
m

<!-- b000982 | furniture | pages [15] -->
m

<!-- b000983 | furniture | pages [15] -->
m

<!-- b000984 | furniture | pages [15] -->
m

<!-- b000985 | furniture | pages [15] -->
m

<!-- b000986 | furniture | pages [15] -->
m

<!-- b000987 | furniture | pages [15] -->
m

<!-- b000988 | furniture | pages [15] -->
m

<!-- b000989 | furniture | pages [15] -->
m

<!-- b000990 | furniture | pages [15] -->
m

<!-- b000991 | furniture | pages [15] -->
m

<!-- b000992 | furniture | pages [15] -->
m

<!-- b000993 | furniture | pages [15] -->
m

<!-- b000994 | furniture | pages [15] -->
m

<!-- b000995 | furniture | pages [15] -->
m

<!-- b000996 | furniture | pages [15] -->
m

<!-- b000997 | furniture | pages [15] -->
m

<!-- b000998 | furniture | pages [15] -->
m

<!-- b000999 | furniture | pages [15] -->
m

<!-- b001000 | furniture | pages [15] -->
m

<!-- b001001 | furniture | pages [15] -->
m

<!-- b001002 | furniture | pages [15] -->
m

<!-- b001003 | furniture | pages [15] -->
m

<!-- b001004 | furniture | pages [15] -->
m

<!-- b001005 | furniture | pages [15] -->
m

<!-- b001006 | furniture | pages [15] -->
m

<!-- b001007 | furniture | pages [15] -->
m

<!-- b001008 | furniture | pages [15] -->
m

<!-- b001009 | furniture | pages [15] -->
m

<!-- b001010 | furniture | pages [15] -->
m

<!-- b001011 | furniture | pages [15] -->
m

<!-- b001012 | furniture | pages [15] -->
m

<!-- b001013 | furniture | pages [15] -->
m

<!-- b001014 | furniture | pages [15] -->
m

<!-- b001015 | furniture | pages [15] -->
m

<!-- b001016 | furniture | pages [15] -->
m

<!-- b001017 | furniture | pages [15] -->
m

<!-- b001018 | furniture | pages [15] -->
m

<!-- b001019 | furniture | pages [15] -->
m

<!-- b001020 | furniture | pages [15] -->
m

<!-- b001021 | furniture | pages [15] -->
m

<!-- b001022 | furniture | pages [15] -->
m

<!-- b001023 | furniture | pages [15] -->
m

<!-- b001024 | furniture | pages [15] -->
m

<!-- b001025 | furniture | pages [15] -->
m

<!-- b001026 | furniture | pages [15] -->
m

<!-- b001027 | furniture | pages [15] -->
m

<!-- b001028 | furniture | pages [15] -->
m

<!-- b001029 | furniture | pages [15] -->
m

<!-- b001030 | furniture | pages [15] -->
m

<!-- b001031 | furniture | pages [15] -->
m

<!-- b001032 | furniture | pages [15] -->
m

<!-- b001033 | furniture | pages [15] -->
m

<!-- b001034 | furniture | pages [15] -->
m

<!-- b001035 | furniture | pages [15] -->
m

<!-- b001036 | furniture | pages [15] -->
m

<!-- b001037 | furniture | pages [15] -->
m

<!-- b001038 | furniture | pages [15] -->
m

<!-- b001039 | furniture | pages [15] -->
m

<!-- b001040 | furniture | pages [15] -->
m

<!-- b001041 | furniture | pages [15] -->
m

<!-- b001042 | furniture | pages [15] -->
m

<!-- b001043 | furniture | pages [15] -->
m

<!-- b001044 | furniture | pages [15] -->
m

<!-- b001045 | furniture | pages [15] -->
m

<!-- b001046 | furniture | pages [15] -->
m

<!-- b001047 | furniture | pages [15] -->
m

<!-- b001048 | furniture | pages [15] -->
m

<!-- b001049 | furniture | pages [15] -->
m

<!-- b001050 | furniture | pages [15] -->
m

<!-- b001051 | furniture | pages [15] -->
m

<!-- b001052 | furniture | pages [15] -->
m

<!-- b001053 | furniture | pages [15] -->
m

<!-- b001054 | furniture | pages [15] -->
m

<!-- b001055 | furniture | pages [15] -->
m

<!-- b001056 | furniture | pages [15] -->
m

<!-- b001057 | furniture | pages [15] -->
m

<!-- b001058 | furniture | pages [15] -->
m

<!-- b001059 | furniture | pages [15] -->
m

<!-- b001060 | furniture | pages [15] -->
m

<!-- b001061 | furniture | pages [15] -->
m

<!-- b001062 | furniture | pages [15] -->
m

<!-- b001063 | furniture | pages [15] -->
m

<!-- b001064 | furniture | pages [15] -->
m

<!-- b001065 | furniture | pages [15] -->
m

<!-- b001066 | furniture | pages [15] -->
m

<!-- b001067 | furniture | pages [15] -->
m

<!-- b001068 | furniture | pages [15] -->
m

<!-- b001069 | furniture | pages [15] -->
m

<!-- b001070 | furniture | pages [15] -->
m

<!-- b001071 | furniture | pages [15] -->
m

<!-- b001072 | furniture | pages [15] -->
m

<!-- b001073 | furniture | pages [15] -->
m

<!-- b001074 | furniture | pages [15] -->
m

<!-- b001075 | furniture | pages [15] -->
m

<!-- b001076 | furniture | pages [15] -->
m

<!-- b001077 | furniture | pages [15] -->
m

<!-- b001078 | furniture | pages [15] -->
m

<!-- b001079 | furniture | pages [15] -->
m

<!-- b001080 | furniture | pages [15] -->
m

<!-- b001081 | furniture | pages [15] -->
m

<!-- b001082 | furniture | pages [15] -->
m

<!-- b001083 | furniture | pages [15] -->
m

<!-- b001084 | furniture | pages [15] -->
m

<!-- b001085 | furniture | pages [15] -->
m

<!-- b001086 | furniture | pages [15] -->
m

<!-- b001087 | furniture | pages [15] -->
m

<!-- b001088 | furniture | pages [15] -->
m

<!-- b001089 | furniture | pages [15] -->
m

<!-- b001090 | furniture | pages [15] -->
m

<!-- b001091 | furniture | pages [15] -->
m

<!-- b001092 | furniture | pages [15] -->
m

<!-- b001093 | furniture | pages [15] -->
m

<!-- b001094 | furniture | pages [15] -->
m

<!-- b001095 | furniture | pages [15] -->
m

<!-- b001096 | furniture | pages [15] -->
m

<!-- b001097 | furniture | pages [15] -->
m

<!-- b001098 | furniture | pages [15] -->
m

<!-- b001099 | furniture | pages [15] -->
m

<!-- b001100 | furniture | pages [15] -->
m

<!-- b001101 | furniture | pages [15] -->
m

<!-- b001102 | furniture | pages [15] -->
m

<!-- b001103 | furniture | pages [15] -->
m

<!-- b001104 | furniture | pages [15] -->
m

<!-- b001105 | furniture | pages [15] -->
m

<!-- b001106 | furniture | pages [15] -->
m

<!-- b001107 | furniture | pages [15] -->
m

<!-- b001108 | furniture | pages [15] -->
m

<!-- b001109 | furniture | pages [15] -->
m

<!-- b001110 | furniture | pages [15] -->
m

<!-- b001111 | furniture | pages [15] -->
m

<!-- b001112 | furniture | pages [15] -->
m

<!-- b001113 | furniture | pages [15] -->
m

<!-- b001114 | furniture | pages [15] -->
m

<!-- b001115 | furniture | pages [15] -->
m

<!-- b001116 | furniture | pages [15] -->
m

<!-- b001117 | furniture | pages [15] -->
m

<!-- b001118 | furniture | pages [15] -->
m

<!-- b001119 | furniture | pages [15] -->
m

<!-- b001120 | furniture | pages [15] -->
m

<!-- b001121 | furniture | pages [15] -->
m

<!-- b001122 | furniture | pages [15] -->
m

<!-- b001123 | furniture | pages [15] -->
m

<!-- b001124 | furniture | pages [15] -->
m

<!-- b001125 | furniture | pages [15] -->
m

<!-- b001126 | furniture | pages [15] -->
m

<!-- b001127 | furniture | pages [15] -->
m

<!-- b001128 | furniture | pages [15] -->
m

<!-- b001129 | furniture | pages [15] -->
m

<!-- b001130 | furniture | pages [15] -->
m

<!-- b001131 | furniture | pages [15] -->
m

<!-- b001132 | furniture | pages [15] -->
m

<!-- b001133 | furniture | pages [15] -->
m

<!-- b001134 | furniture | pages [15] -->
m

<!-- b001135 | furniture | pages [15] -->
m

<!-- b001136 | furniture | pages [15] -->
m

<!-- b001137 | furniture | pages [15] -->
m

<!-- b001138 | furniture | pages [15] -->
m

<!-- b001139 | furniture | pages [15] -->
m

<!-- b001140 | furniture | pages [15] -->
m

<!-- b001141 | furniture | pages [15] -->
m

<!-- b001142 | furniture | pages [15] -->
m

<!-- b001143 | furniture | pages [15] -->
m

<!-- b001144 | furniture | pages [15] -->
m

<!-- b001145 | furniture | pages [15] -->
m

<!-- b001146 | furniture | pages [15] -->
m

<!-- b001147 | furniture | pages [15] -->
m

<!-- b001148 | furniture | pages [15] -->
m

<!-- b001149 | furniture | pages [15] -->
m

<!-- b001150 | furniture | pages [15] -->
m

<!-- b001151 | furniture | pages [15] -->
m

<!-- b001152 | furniture | pages [15] -->
m

<!-- b001153 | furniture | pages [15] -->
m

<!-- b001154 | furniture | pages [15] -->
m

<!-- b001155 | furniture | pages [15] -->
m

<!-- b001156 | furniture | pages [15] -->
m

<!-- b001157 | furniture | pages [15] -->
m

<!-- b001158 | furniture | pages [15] -->
m

<!-- b001159 | furniture | pages [15] -->
m

<!-- b001160 | furniture | pages [15] -->
m

<!-- b001161 | furniture | pages [15] -->
m

<!-- b001162 | furniture | pages [15] -->
m

<!-- b001163 | furniture | pages [15] -->
m

<!-- b001164 | furniture | pages [15] -->
m

<!-- b001165 | furniture | pages [15] -->
m

<!-- b001166 | furniture | pages [15] -->
m

<!-- b001167 | furniture | pages [15] -->
m

<!-- b001168 | furniture | pages [15] -->
m

<!-- b001169 | furniture | pages [15] -->
m

<!-- b001170 | furniture | pages [15] -->
m

<!-- b001171 | furniture | pages [15] -->
m

<!-- b001172 | furniture | pages [15] -->
m

<!-- b001173 | furniture | pages [15] -->
m

<!-- b001174 | furniture | pages [15] -->
m

<!-- b001175 | furniture | pages [15] -->
m

<!-- b001176 | furniture | pages [15] -->
m

<!-- b001177 | furniture | pages [15] -->
m

<!-- b001178 | furniture | pages [15] -->
m

<!-- b001179 | furniture | pages [15] -->
m

<!-- b001180 | furniture | pages [15] -->
m

<!-- b001181 | furniture | pages [15] -->
m

<!-- b001182 | furniture | pages [15] -->
m

<!-- b001183 | furniture | pages [15] -->
m

<!-- b001184 | furniture | pages [15] -->
m

<!-- b001185 | furniture | pages [15] -->
m

<!-- b001186 | furniture | pages [15] -->
m

<!-- b001187 | furniture | pages [15] -->
m

<!-- b001188 | furniture | pages [15] -->
m

<!-- b001189 | furniture | pages [15] -->
m

<!-- b001190 | furniture | pages [15] -->
m

<!-- b001191 | furniture | pages [15] -->
m

<!-- b001192 | furniture | pages [15] -->
m

<!-- b001193 | furniture | pages [15] -->
m

<!-- b001194 | furniture | pages [15] -->
m

<!-- b001195 | furniture | pages [15] -->
m

<!-- b001196 | furniture | pages [15] -->
m

<!-- b001197 | furniture | pages [15] -->
m

<!-- b001198 | furniture | pages [15] -->
m

<!-- b001199 | furniture | pages [15] -->
m

<!-- b001200 | furniture | pages [15] -->
m

<!-- b001201 | furniture | pages [15] -->
m

<!-- b001202 | furniture | pages [15] -->
m

<!-- b001203 | furniture | pages [16] -->
Team 2524070

<!-- b001204 | furniture | pages [16] -->
Page 16of 25

<!-- b001206 | prose | pages [16] -->
(a) Illustration of 5 Strong Rules (b) Network Graph Visualization

<!-- b001207 | caption | pages [16] -->
Figure 8: The Result of Association Rule Model(USA)

<!-- b001208 | prose | pages [16] -->
According to the aforementioned criteria, it can be inferred that Basketball, Swimming, Volleyball, Judo, Archery, Tennis, and Rhythmic Gymnastics hold considerable significance for the United States. Increased participation in these sports may enhance the likelihood of the U.S. securing additional medals.

<!-- b001209 | prose | pages [16] -->
Employing a similar analytical framework, it is feasible to derive insights for other nations and perform comparative assessments to identify disciplines of importance across multiple countries. Furthermore, the previously defined indicator 𝑧𝑖warrants examination. By calculating the average 7Í value of 𝑧𝑖for all participating countries over the last seven Olympic Games, one can derive 𝑧𝑖= 1 𝑧𝑖 7 𝑖 (the average medal-winning proportion for each event), which serves as a metric of importance. Visualization through a heatmap indicates that Athletics is of considerable significance for numerous countries.

<!-- b001210 | caption | pages [16] -->
Figure 9: Importance of Sports(disciplines) to Various Countries

<!-- b001211 | prose | pages [16, 17] -->
关注数学模型 Moreover, through the application of association rules, we can investigate whether the introduction of new disciplines by the host country contributes positively to the increase in medal counts. We construct item sets as delineated in the table..., where 𝑖𝑓𝑖𝑛𝑡indicates whether the new discipline was primarily introduced at the behest of the host country, 𝑖𝑓𝑝𝑎𝑟denotes the host country’s participation in this discipline, 𝑖𝑓ℎ𝑎𝑣𝑒indicates whether the host country secured an award, and 𝑖𝑓𝑚𝑎𝑥signifies whether the host country achieved the highest number of awards in this event. Each row of the data matrix encapsulates information regarding the new disciplines introduced in previous Olympic Games:

<!-- b001212 | furniture | pages [16] -->
2

<!-- b001213 | furniture | pages [16] -->
MATHmodels

<!-- b001214 | furniture | pages [16] -->
获取更多资讯

<!-- b001215 | furniture | pages [17] -->
Team 2524070

<!-- b001216 | furniture | pages [17] -->
Page 17of 25

<!-- b001218 | prose | pages [17] -->
微信公众号：数学模型 𝑖𝑓𝑖𝑛𝑡 𝑖𝑓𝑝𝑎𝑟 𝑖𝑓ℎ𝑎𝑣𝑒 𝑖𝑓𝑚𝑎𝑥

<!-- b001219 | heading | pages [17] -->
Symbol

<!-- b001220 | prose | pages [17] -->
Sign 1/-1 1/-1 1/-1 1/-1

<!-- b001221 | caption | pages [17] -->
Table 6: Relevant indicators of Host Countries

<!-- b001222 | prose | pages [17] -->
We designate 𝑖𝑓𝑖𝑛𝑡and 𝑖𝑓𝑝𝑎𝑟as the antecedents, while 𝑖𝑓ℎ𝑎𝑣𝑒and 𝑖𝑓𝑚𝑎𝑥serve as the consequents, and we perform association analysis utilizing the GRI algorithm to derive the following rules.It can be posited that the inclusion of events at the behest of the host country is likely to be advantageous for that country, potentially facilitating an increase in their medal count: 微信号：MATHmodels (a) Illustration of 2 Strong Rules (b) Network Graph Visualization

<!-- b001223 | caption | pages [17] -->
Figure 10: The Result of Association Rule Model(Host Country)

<!-- b001224 | heading | pages [17] -->
5.3 Results Analysis

<!-- b001225 | prose | pages [17] -->
To assess the efficacy of a rule, it is essential to examine it through the lens of validity indicators pertinent to association rules. For instance, consider the association analysis where the antecedent is denoted as 𝜑𝑖and the consequent as 𝑚𝑐:

<!-- b001226 | prose | pages [17, 18] -->
• Support Ñ 𝑚𝑐) 𝑆𝜑𝑖→𝑚𝑐= 𝑁(𝜑𝑖 (9) 𝑁 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Ñ 𝑚𝑐) signifies the number of transactions that include both 𝜑𝑖and 𝑚𝑐, while N denotes the 𝑁(𝜑𝑖 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m total number of transactions. The support metric of the rule indicates its generalizability; a higher m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m support value suggests a greater universality of the rule. In general, the minimum level for support m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m can be established at a fairly low point. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001227 | furniture | pages [17] -->
m

<!-- b001228 | furniture | pages [17] -->
m

<!-- b001229 | furniture | pages [17] -->
m

<!-- b001230 | furniture | pages [17] -->
m

<!-- b001231 | furniture | pages [17] -->
m

<!-- b001232 | furniture | pages [17] -->
m

<!-- b001233 | furniture | pages [17] -->
m

<!-- b001234 | furniture | pages [17] -->
m

<!-- b001235 | furniture | pages [17] -->
m

<!-- b001236 | furniture | pages [17] -->
m

<!-- b001237 | furniture | pages [17] -->
m

<!-- b001238 | furniture | pages [17] -->
m

<!-- b001239 | furniture | pages [17] -->
m

<!-- b001240 | furniture | pages [17] -->
m

<!-- b001241 | furniture | pages [17] -->
m

<!-- b001242 | furniture | pages [17] -->
m

<!-- b001243 | furniture | pages [17] -->
m

<!-- b001244 | furniture | pages [17] -->
m

<!-- b001245 | furniture | pages [17] -->
m

<!-- b001246 | furniture | pages [17] -->
m

<!-- b001247 | furniture | pages [17] -->
m

<!-- b001248 | furniture | pages [17] -->
m

<!-- b001249 | furniture | pages [17] -->
m

<!-- b001250 | furniture | pages [17] -->
m

<!-- b001251 | furniture | pages [17] -->
m

<!-- b001252 | furniture | pages [17] -->
m

<!-- b001253 | furniture | pages [17] -->
m

<!-- b001254 | furniture | pages [17] -->
m

<!-- b001255 | furniture | pages [17] -->
m

<!-- b001256 | furniture | pages [17] -->
m

<!-- b001257 | furniture | pages [17] -->
m

<!-- b001258 | furniture | pages [17] -->
m

<!-- b001259 | furniture | pages [17] -->
m

<!-- b001260 | furniture | pages [17] -->
m

<!-- b001261 | furniture | pages [17] -->
m

<!-- b001262 | furniture | pages [17] -->
m

<!-- b001263 | furniture | pages [17] -->
m

<!-- b001264 | furniture | pages [17] -->
m

<!-- b001265 | furniture | pages [17] -->
m

<!-- b001266 | furniture | pages [17] -->
m

<!-- b001267 | furniture | pages [17] -->
m

<!-- b001268 | furniture | pages [17] -->
m

<!-- b001269 | furniture | pages [17] -->
m

<!-- b001270 | furniture | pages [17] -->
m

<!-- b001271 | furniture | pages [17] -->
m

<!-- b001272 | furniture | pages [17] -->
m

<!-- b001273 | furniture | pages [17] -->
m

<!-- b001274 | furniture | pages [17] -->
m

<!-- b001275 | furniture | pages [17] -->
m

<!-- b001276 | furniture | pages [17] -->
m

<!-- b001277 | furniture | pages [17] -->
m

<!-- b001278 | furniture | pages [17] -->
m

<!-- b001279 | furniture | pages [17] -->
m

<!-- b001280 | furniture | pages [17] -->
m

<!-- b001281 | furniture | pages [17] -->
m

<!-- b001282 | furniture | pages [17] -->
m

<!-- b001283 | furniture | pages [17] -->
m

<!-- b001284 | furniture | pages [17] -->
m

<!-- b001285 | furniture | pages [17] -->
m

<!-- b001286 | furniture | pages [17] -->
m

<!-- b001287 | furniture | pages [17] -->
m

<!-- b001288 | furniture | pages [17] -->
m

<!-- b001289 | furniture | pages [17] -->
m

<!-- b001290 | furniture | pages [17] -->
m

<!-- b001291 | furniture | pages [17] -->
m

<!-- b001292 | furniture | pages [17] -->
m

<!-- b001293 | furniture | pages [17] -->
m

<!-- b001294 | furniture | pages [17] -->
m

<!-- b001295 | furniture | pages [17] -->
m

<!-- b001296 | furniture | pages [17] -->
m

<!-- b001297 | furniture | pages [17] -->
m

<!-- b001298 | furniture | pages [17] -->
m

<!-- b001299 | furniture | pages [17] -->
m

<!-- b001300 | furniture | pages [17] -->
m

<!-- b001301 | furniture | pages [17] -->
m

<!-- b001302 | furniture | pages [17] -->
m

<!-- b001303 | furniture | pages [17] -->
m

<!-- b001304 | furniture | pages [17] -->
m

<!-- b001305 | furniture | pages [17] -->
m

<!-- b001306 | furniture | pages [17] -->
m

<!-- b001307 | furniture | pages [17] -->
m

<!-- b001308 | furniture | pages [17] -->
m

<!-- b001309 | furniture | pages [17] -->
m

<!-- b001310 | furniture | pages [17] -->
m

<!-- b001311 | furniture | pages [17] -->
m

<!-- b001312 | furniture | pages [17] -->
m

<!-- b001313 | furniture | pages [17] -->
m

<!-- b001314 | furniture | pages [17] -->
m

<!-- b001315 | furniture | pages [17] -->
m

<!-- b001316 | furniture | pages [17] -->
m

<!-- b001317 | furniture | pages [17] -->
m

<!-- b001318 | furniture | pages [17] -->
m

<!-- b001319 | furniture | pages [17] -->
m

<!-- b001320 | furniture | pages [17] -->
m

<!-- b001321 | furniture | pages [17] -->
m

<!-- b001322 | furniture | pages [17] -->
m

<!-- b001323 | furniture | pages [17] -->
m

<!-- b001324 | furniture | pages [17] -->
m

<!-- b001325 | furniture | pages [17] -->
m

<!-- b001326 | furniture | pages [17] -->
m

<!-- b001327 | furniture | pages [17] -->
m

<!-- b001328 | furniture | pages [17] -->
m

<!-- b001329 | furniture | pages [17] -->
m

<!-- b001330 | furniture | pages [17] -->
m

<!-- b001331 | furniture | pages [17] -->
m

<!-- b001332 | furniture | pages [17] -->
m

<!-- b001333 | furniture | pages [17] -->
m

<!-- b001334 | furniture | pages [17] -->
m

<!-- b001335 | furniture | pages [17] -->
m

<!-- b001336 | furniture | pages [17] -->
m

<!-- b001337 | furniture | pages [17] -->
m

<!-- b001338 | furniture | pages [17] -->
m

<!-- b001339 | furniture | pages [17] -->
m

<!-- b001340 | furniture | pages [17] -->
m

<!-- b001341 | furniture | pages [17] -->
m

<!-- b001342 | furniture | pages [17] -->
m

<!-- b001343 | furniture | pages [17] -->
m

<!-- b001344 | furniture | pages [17] -->
m

<!-- b001345 | furniture | pages [17] -->
m

<!-- b001346 | furniture | pages [17] -->
m

<!-- b001347 | furniture | pages [17] -->
m

<!-- b001348 | furniture | pages [17] -->
m

<!-- b001349 | furniture | pages [17] -->
m

<!-- b001350 | furniture | pages [17] -->
m

<!-- b001351 | furniture | pages [17] -->
m

<!-- b001352 | furniture | pages [17] -->
m

<!-- b001353 | furniture | pages [17] -->
m

<!-- b001354 | furniture | pages [17] -->
m

<!-- b001355 | furniture | pages [17] -->
m

<!-- b001356 | furniture | pages [17] -->
m

<!-- b001357 | furniture | pages [17] -->
m

<!-- b001358 | furniture | pages [17] -->
m

<!-- b001359 | furniture | pages [17] -->
m

<!-- b001360 | furniture | pages [17] -->
m

<!-- b001361 | furniture | pages [17] -->
m

<!-- b001362 | furniture | pages [17] -->
m

<!-- b001363 | furniture | pages [17] -->
m

<!-- b001364 | furniture | pages [17] -->
m

<!-- b001365 | furniture | pages [17] -->
m

<!-- b001366 | furniture | pages [17] -->
m

<!-- b001367 | furniture | pages [17] -->
m

<!-- b001368 | furniture | pages [17] -->
m

<!-- b001369 | furniture | pages [17] -->
m

<!-- b001370 | furniture | pages [17] -->
m

<!-- b001371 | furniture | pages [17] -->
m

<!-- b001372 | furniture | pages [17] -->
m

<!-- b001373 | furniture | pages [17] -->
m

<!-- b001374 | furniture | pages [17] -->
m

<!-- b001375 | furniture | pages [17] -->
m

<!-- b001376 | furniture | pages [17] -->
m

<!-- b001377 | furniture | pages [17] -->
m

<!-- b001378 | furniture | pages [17] -->
m

<!-- b001379 | furniture | pages [17] -->
m

<!-- b001380 | furniture | pages [17] -->
m

<!-- b001381 | furniture | pages [17] -->
m

<!-- b001382 | furniture | pages [17] -->
m

<!-- b001383 | furniture | pages [17] -->
m

<!-- b001384 | furniture | pages [17] -->
m

<!-- b001385 | furniture | pages [17] -->
m

<!-- b001386 | furniture | pages [17] -->
m

<!-- b001387 | furniture | pages [17] -->
m

<!-- b001388 | furniture | pages [17] -->
m

<!-- b001389 | furniture | pages [17] -->
m

<!-- b001390 | furniture | pages [17] -->
m

<!-- b001391 | furniture | pages [17] -->
m

<!-- b001392 | furniture | pages [17] -->
m

<!-- b001393 | furniture | pages [17] -->
m

<!-- b001394 | furniture | pages [17] -->
m

<!-- b001395 | furniture | pages [17] -->
m

<!-- b001396 | furniture | pages [17] -->
m

<!-- b001397 | furniture | pages [17] -->
m

<!-- b001398 | furniture | pages [17] -->
m

<!-- b001399 | furniture | pages [17] -->
m

<!-- b001400 | furniture | pages [17] -->
m

<!-- b001401 | furniture | pages [17] -->
m

<!-- b001402 | furniture | pages [17] -->
m

<!-- b001403 | furniture | pages [17] -->
m

<!-- b001404 | furniture | pages [17] -->
m

<!-- b001405 | furniture | pages [17] -->
m

<!-- b001406 | furniture | pages [17] -->
m

<!-- b001407 | furniture | pages [17] -->
m

<!-- b001408 | furniture | pages [17] -->
m

<!-- b001409 | furniture | pages [17] -->
m

<!-- b001410 | furniture | pages [17] -->
m

<!-- b001411 | furniture | pages [17] -->
m

<!-- b001412 | furniture | pages [17] -->
m

<!-- b001413 | furniture | pages [17] -->
m

<!-- b001414 | furniture | pages [17] -->
m

<!-- b001415 | furniture | pages [17] -->
m

<!-- b001416 | furniture | pages [17] -->
m

<!-- b001417 | furniture | pages [17] -->
m

<!-- b001418 | furniture | pages [17] -->
m

<!-- b001419 | furniture | pages [17] -->
m

<!-- b001420 | furniture | pages [17] -->
m

<!-- b001421 | furniture | pages [17] -->
m

<!-- b001422 | furniture | pages [17] -->
m

<!-- b001423 | furniture | pages [17] -->
m

<!-- b001424 | furniture | pages [17] -->
m

<!-- b001425 | furniture | pages [17] -->
m

<!-- b001426 | furniture | pages [17] -->
m

<!-- b001427 | furniture | pages [17] -->
m

<!-- b001428 | furniture | pages [17] -->
m

<!-- b001429 | furniture | pages [17] -->
m

<!-- b001430 | furniture | pages [17] -->
m

<!-- b001431 | furniture | pages [17] -->
m

<!-- b001432 | furniture | pages [17] -->
m

<!-- b001433 | furniture | pages [17] -->
m

<!-- b001434 | furniture | pages [17] -->
m

<!-- b001435 | furniture | pages [17] -->
m

<!-- b001436 | furniture | pages [17] -->
m

<!-- b001437 | furniture | pages [17] -->
m

<!-- b001438 | furniture | pages [17] -->
m

<!-- b001439 | furniture | pages [17] -->
m

<!-- b001440 | furniture | pages [17] -->
m

<!-- b001441 | furniture | pages [17] -->
m

<!-- b001442 | furniture | pages [17] -->
m

<!-- b001443 | furniture | pages [17] -->
m

<!-- b001444 | furniture | pages [17] -->
m

<!-- b001445 | furniture | pages [17] -->
m

<!-- b001446 | furniture | pages [17] -->
m

<!-- b001447 | furniture | pages [17] -->
m

<!-- b001448 | furniture | pages [17] -->
m

<!-- b001449 | furniture | pages [17] -->
m

<!-- b001450 | furniture | pages [17] -->
m

<!-- b001451 | furniture | pages [17] -->
m

<!-- b001452 | furniture | pages [17] -->
m

<!-- b001453 | furniture | pages [17] -->
m

<!-- b001454 | furniture | pages [17] -->
m

<!-- b001455 | furniture | pages [17] -->
m

<!-- b001456 | furniture | pages [17] -->
m

<!-- b001457 | furniture | pages [17] -->
m

<!-- b001458 | furniture | pages [17] -->
m

<!-- b001459 | furniture | pages [17] -->
m

<!-- b001460 | furniture | pages [17] -->
m

<!-- b001461 | furniture | pages [17] -->
m

<!-- b001462 | furniture | pages [17] -->
m

<!-- b001463 | furniture | pages [17] -->
m

<!-- b001464 | furniture | pages [17] -->
m

<!-- b001465 | furniture | pages [17] -->
m

<!-- b001466 | furniture | pages [17] -->
m

<!-- b001467 | furniture | pages [17] -->
m

<!-- b001468 | furniture | pages [17] -->
m

<!-- b001469 | furniture | pages [17] -->
m

<!-- b001470 | furniture | pages [17] -->
m

<!-- b001471 | furniture | pages [17] -->
m

<!-- b001472 | furniture | pages [17] -->
m

<!-- b001473 | furniture | pages [17] -->
m

<!-- b001474 | furniture | pages [17] -->
m

<!-- b001475 | furniture | pages [17] -->
m

<!-- b001476 | furniture | pages [17] -->
m

<!-- b001477 | furniture | pages [17] -->
m

<!-- b001478 | furniture | pages [17] -->
m

<!-- b001479 | furniture | pages [17] -->
m

<!-- b001480 | furniture | pages [17] -->
m

<!-- b001481 | furniture | pages [17] -->
m

<!-- b001482 | furniture | pages [17] -->
m

<!-- b001483 | furniture | pages [17] -->
m

<!-- b001484 | furniture | pages [17] -->
m

<!-- b001485 | furniture | pages [17] -->
m

<!-- b001486 | furniture | pages [17] -->
m

<!-- b001487 | furniture | pages [17] -->
m

<!-- b001488 | furniture | pages [17] -->
m

<!-- b001489 | furniture | pages [17] -->
m

<!-- b001490 | furniture | pages [17] -->
m

<!-- b001491 | furniture | pages [17] -->
m

<!-- b001492 | furniture | pages [17] -->
m

<!-- b001493 | furniture | pages [17] -->
m

<!-- b001494 | furniture | pages [17] -->
m

<!-- b001495 | furniture | pages [17] -->
m

<!-- b001496 | furniture | pages [17] -->
m

<!-- b001497 | furniture | pages [17] -->
m

<!-- b001498 | furniture | pages [17] -->
m

<!-- b001499 | furniture | pages [17] -->
m

<!-- b001500 | furniture | pages [17] -->
m

<!-- b001501 | furniture | pages [17] -->
m

<!-- b001502 | furniture | pages [17] -->
m

<!-- b001503 | furniture | pages [17] -->
m

<!-- b001504 | furniture | pages [17] -->
m

<!-- b001505 | furniture | pages [17] -->
m

<!-- b001506 | furniture | pages [17] -->
m

<!-- b001507 | furniture | pages [17] -->
m

<!-- b001508 | furniture | pages [17] -->
m

<!-- b001509 | furniture | pages [17] -->
m

<!-- b001510 | furniture | pages [17] -->
m

<!-- b001511 | furniture | pages [17] -->
m

<!-- b001512 | furniture | pages [17] -->
m

<!-- b001513 | furniture | pages [17] -->
m

<!-- b001514 | furniture | pages [17] -->
m

<!-- b001515 | furniture | pages [17] -->
m

<!-- b001516 | furniture | pages [17] -->
m

<!-- b001517 | furniture | pages [17] -->
m

<!-- b001518 | furniture | pages [17] -->
m

<!-- b001519 | furniture | pages [17] -->
m

<!-- b001520 | furniture | pages [17] -->
m

<!-- b001521 | furniture | pages [17] -->
m

<!-- b001522 | furniture | pages [17] -->
m

<!-- b001523 | furniture | pages [17] -->
m

<!-- b001524 | furniture | pages [17] -->
m

<!-- b001525 | furniture | pages [17] -->
m

<!-- b001526 | furniture | pages [17] -->
m

<!-- b001527 | furniture | pages [17] -->
m

<!-- b001528 | furniture | pages [17] -->
m

<!-- b001529 | furniture | pages [17] -->
m

<!-- b001530 | furniture | pages [17] -->
m

<!-- b001531 | furniture | pages [17] -->
m

<!-- b001532 | furniture | pages [17] -->
m

<!-- b001533 | furniture | pages [17] -->
m

<!-- b001534 | furniture | pages [17] -->
m

<!-- b001535 | furniture | pages [17] -->
m

<!-- b001536 | furniture | pages [17] -->
m

<!-- b001537 | furniture | pages [17] -->
m

<!-- b001538 | furniture | pages [17] -->
m

<!-- b001539 | furniture | pages [17] -->
m

<!-- b001540 | furniture | pages [17] -->
m

<!-- b001541 | furniture | pages [17] -->
m

<!-- b001542 | furniture | pages [17] -->
m

<!-- b001543 | furniture | pages [17] -->
m

<!-- b001544 | furniture | pages [17] -->
m

<!-- b001545 | furniture | pages [17] -->
m

<!-- b001546 | furniture | pages [17] -->
m

<!-- b001547 | furniture | pages [17] -->
m

<!-- b001548 | furniture | pages [17] -->
m

<!-- b001549 | furniture | pages [17] -->
m

<!-- b001550 | furniture | pages [17] -->
m

<!-- b001551 | furniture | pages [18] -->
Team 2524070

<!-- b001552 | furniture | pages [18] -->
Page 18of 25

<!-- b001554 | prose | pages [18] -->
• Confidence

<!-- b001555 | prose | pages [18] -->
Ñ 𝑚𝑐) = 𝑆𝜑𝑖→𝑚𝑐 𝐶𝜑𝑖→𝑚𝑐= 𝑁(𝜑𝑖 (10) 𝑁(𝜑𝑖) 𝑆𝜑𝑖

<!-- b001556 | prose | pages [18] -->
𝑁(𝜑𝑖) represents the number of transactions that include 𝜑𝑖. The confidence of the rule can be interpreted as a conditional probability; a higher confidence level indicates a stronger reliability of the rule. In general, the minimum confidence threshold should be established at a fairly high level.

<!-- b001557 | prose | pages [18] -->
• Lift

<!-- b001558 | prose | pages [18] -->
𝑁(𝑚𝑐) Ñ 𝑚𝑐) = 𝐶𝜑𝑖→𝑚𝑐 𝐿𝜑𝑖→𝑚𝑐= 𝑁(𝜑𝑖 (11) 𝑁(𝜑𝑖) 𝑁 𝑆𝑚𝑐

<!-- b001559 | prose | pages [18] -->
The lift of a rule is defined as the ratio of the rule’s confidence to the support of the consequent. This metric illustrates the extent to which the antecedent influences the consequent in comparison to the overall context. Consequently, when 𝐿𝜑𝑖→𝑚𝑐> 1 holds true, the antecedent exerts a positive influence on the consequent, with a greater lift indicating a stronger degree of positive influence. Conversely, if 𝐿𝜑𝑖→𝑚𝑐< 1 is true, even with high support and confidence, the rule still not be deemed effective.

<!-- b001560 | prose | pages [18] -->
• Deployment Capability

<!-- b001561 | prose | pages [18] -->
𝐷𝜑𝑖→𝑚𝑐= 𝑆𝜑𝑖−𝑆𝜑𝑖→𝑚𝑐 (12)

<!-- b001562 | prose | pages [18] -->
Deployment capability measures the proportion of instances where the antecedent is true but the consequent is not. A higher deployment capability suggests greater potential for improvement in the rule; therefore, a lower deployment capability is generally preferred.

<!-- b001563 | prose | pages [18] -->
In conclusion, we have conducted a validity analysis of the rule outcomes from the preceding section, and the findings indicate that all our rules are valid and of considerable quality.

<!-- b001564 | prose | pages [18, 19] -->
关注数学模型 Antecedent Consequent Supp. Conf. Lift Deploy. Rules Strength Basketball=1 Swimming=1 𝑚𝑐=high

<!-- b001565 | furniture | pages [18] -->
2

<!-- b001566 | furniture | pages [18] -->
MATHmodels

<!-- b001567 | furniture | pages [18] -->
获取更多资讯

<!-- b001568 | furniture | pages [19] -->
Team 2524070

<!-- b001569 | furniture | pages [19] -->
Page 19of 25

<!-- b001571 | prose | pages [19] -->
• • • 34.48 90.0 3.175 2.448 Volleyball=1 Judo=1 𝑚𝑐=high •• Rhythmic Gymnastics=1 31.03 88.89 2.148 3.447 Archery=1 微信公众号：数学模型 𝑚𝑐=high • 34.48 80.0 1.933 6.896 Tennis =1 Art Competitions=-1 Diving=-1 𝑚𝑐=high •• 41.38 83.33 2.014 6.898 Modern Pentathlon=-1 Polo=-1 Art Competitions=-1 Diving=-1 𝑚𝑐=high •• 41.38 83.33 2.014 6.898 Modern Pentathlon=-1 Rugby=-1 微信号：MATHmodels

<!-- b001572 | caption | pages [19] -->
Table 7: Analysis of the Validity of Association Rules 1

<!-- b001573 | prose | pages [19] -->
Antecedent Consequent Supp. Conf. Lift Deploy. Rules Strength 𝑖𝑓𝑖𝑛𝑡=1 𝑖𝑓ℎ𝑎𝑣𝑒=1

<!-- b001574 | prose | pages [19] -->
• • • 80.56 100 1.2 0 𝑖𝑓𝑝𝑎𝑟=1 𝑖𝑓𝑖𝑛𝑡=1 𝑖𝑓𝑚𝑎𝑥=1 • 80.56 68.97 1.241 24.998 𝑖𝑓𝑝𝑎𝑟=1

<!-- b001575 | caption | pages [19] -->
Table 8: Analysis of the Validity of Association Rules 2

<!-- b001576 | prose | pages [19] -->
6 Could a Great Coach Boost Your Country’s Medal Count?

<!-- b001577 | prose | pages [19] -->
In competitive sports, achieving success depends not only on the skills and training of athletes but also significantly on the influence of coaches. The term "great coach" refers to those who achieve remarkable achievements with various teams or countries due to their outstanding tactical knowledge, extensive expertise, and ability to inspire their teams. These coaches are not limited by their nationality; they can transcend borders, sharing their coaching experience and strategies in diverse sports environments, which can enhance the overall performance of their teams. However, this is merely a perception. Is the "great coach" effect genuinely real? In the following discussion, we will explore the existence of the "great coach" effect and attempt to assess its impact on the medal tallies of different nations.

<!-- b001578 | prose | pages [19] -->
To examine the "Great Coach" phenomenon, we initially selected four prominent coaches:

<!-- b001579 | prose | pages [19, 20] -->
1. Lang Ping, who led the U.S. women’s volleyball team to a silver medal at the 2008 Beijing Olympics and guided the Chinese women’s volleyball team to a gold medal at the 2016 Rio Olympics; m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 2. Bela Karolyi, the head coach of the women’s gymnastics team, led the Romanian team to three gold medals, one silver medal and two bronze medals at the 1976 Montreal Olympics. He later coached the U.S. team to a gold medal at the 1996 Atlanta Olympics.

<!-- b001580 | furniture | pages [19] -->
m

<!-- b001581 | furniture | pages [19] -->
m

<!-- b001582 | furniture | pages [19] -->
m

<!-- b001583 | furniture | pages [19] -->
m

<!-- b001584 | furniture | pages [19] -->
m

<!-- b001585 | furniture | pages [19] -->
m

<!-- b001586 | furniture | pages [19] -->
m

<!-- b001587 | furniture | pages [19] -->
m

<!-- b001588 | furniture | pages [19] -->
m

<!-- b001589 | furniture | pages [19] -->
m

<!-- b001590 | furniture | pages [19] -->
m

<!-- b001591 | furniture | pages [19] -->
m

<!-- b001592 | furniture | pages [19] -->
m

<!-- b001593 | furniture | pages [19] -->
m

<!-- b001594 | furniture | pages [19] -->
m

<!-- b001595 | furniture | pages [19] -->
m

<!-- b001596 | furniture | pages [19] -->
m

<!-- b001597 | furniture | pages [19] -->
m

<!-- b001598 | furniture | pages [19] -->
m

<!-- b001599 | furniture | pages [19] -->
m

<!-- b001600 | furniture | pages [19] -->
m

<!-- b001601 | furniture | pages [19] -->
m

<!-- b001602 | furniture | pages [19] -->
m

<!-- b001603 | furniture | pages [19] -->
m

<!-- b001604 | furniture | pages [19] -->
m

<!-- b001605 | furniture | pages [19] -->
m

<!-- b001606 | furniture | pages [19] -->
m

<!-- b001607 | furniture | pages [19] -->
m

<!-- b001608 | furniture | pages [19] -->
m

<!-- b001609 | furniture | pages [19] -->
m

<!-- b001610 | furniture | pages [19] -->
m

<!-- b001611 | furniture | pages [19] -->
m

<!-- b001612 | furniture | pages [19] -->
m

<!-- b001613 | furniture | pages [19] -->
m

<!-- b001614 | furniture | pages [19] -->
m

<!-- b001615 | furniture | pages [19] -->
m

<!-- b001616 | furniture | pages [19] -->
m

<!-- b001617 | furniture | pages [19] -->
m

<!-- b001618 | furniture | pages [19] -->
m

<!-- b001619 | furniture | pages [19] -->
m

<!-- b001620 | furniture | pages [19] -->
m

<!-- b001621 | furniture | pages [19] -->
m

<!-- b001622 | furniture | pages [19] -->
m

<!-- b001623 | furniture | pages [19] -->
m

<!-- b001624 | furniture | pages [19] -->
m

<!-- b001625 | furniture | pages [19] -->
m

<!-- b001626 | furniture | pages [19] -->
m

<!-- b001627 | furniture | pages [19] -->
m

<!-- b001628 | furniture | pages [19] -->
m

<!-- b001629 | furniture | pages [19] -->
m

<!-- b001630 | furniture | pages [19] -->
m

<!-- b001631 | furniture | pages [19] -->
m

<!-- b001632 | furniture | pages [19] -->
m

<!-- b001633 | furniture | pages [19] -->
m

<!-- b001634 | furniture | pages [19] -->
m

<!-- b001635 | furniture | pages [19] -->
m

<!-- b001636 | furniture | pages [19] -->
m

<!-- b001637 | furniture | pages [19] -->
m

<!-- b001638 | furniture | pages [19] -->
m

<!-- b001639 | furniture | pages [19] -->
m

<!-- b001640 | furniture | pages [19] -->
m

<!-- b001641 | furniture | pages [19] -->
m

<!-- b001642 | furniture | pages [19] -->
m

<!-- b001643 | furniture | pages [19] -->
m

<!-- b001644 | furniture | pages [19] -->
m

<!-- b001645 | furniture | pages [19] -->
m

<!-- b001646 | furniture | pages [19] -->
m

<!-- b001647 | furniture | pages [19] -->
m

<!-- b001648 | furniture | pages [19] -->
m

<!-- b001649 | furniture | pages [19] -->
m

<!-- b001650 | furniture | pages [19] -->
m

<!-- b001651 | furniture | pages [19] -->
m

<!-- b001652 | furniture | pages [19] -->
m

<!-- b001653 | furniture | pages [19] -->
m

<!-- b001654 | furniture | pages [19] -->
m

<!-- b001655 | furniture | pages [19] -->
m

<!-- b001656 | furniture | pages [19] -->
m

<!-- b001657 | furniture | pages [19] -->
m

<!-- b001658 | furniture | pages [19] -->
m

<!-- b001659 | furniture | pages [19] -->
m

<!-- b001660 | furniture | pages [19] -->
m

<!-- b001661 | furniture | pages [19] -->
m

<!-- b001662 | furniture | pages [19] -->
m

<!-- b001663 | furniture | pages [19] -->
m

<!-- b001664 | furniture | pages [19] -->
m

<!-- b001665 | furniture | pages [19] -->
m

<!-- b001666 | furniture | pages [19] -->
m

<!-- b001667 | furniture | pages [19] -->
m

<!-- b001668 | furniture | pages [19] -->
m

<!-- b001669 | furniture | pages [19] -->
m

<!-- b001670 | furniture | pages [19] -->
m

<!-- b001671 | furniture | pages [19] -->
m

<!-- b001672 | furniture | pages [19] -->
m

<!-- b001673 | furniture | pages [19] -->
m

<!-- b001674 | furniture | pages [19] -->
m

<!-- b001675 | furniture | pages [19] -->
m

<!-- b001676 | furniture | pages [19] -->
m

<!-- b001677 | furniture | pages [19] -->
m

<!-- b001678 | furniture | pages [19] -->
m

<!-- b001679 | furniture | pages [19] -->
m

<!-- b001680 | furniture | pages [19] -->
m

<!-- b001681 | furniture | pages [19] -->
m

<!-- b001682 | furniture | pages [19] -->
m

<!-- b001683 | furniture | pages [19] -->
m

<!-- b001684 | furniture | pages [19] -->
m

<!-- b001685 | furniture | pages [19] -->
m

<!-- b001686 | furniture | pages [19] -->
m

<!-- b001687 | furniture | pages [19] -->
m

<!-- b001688 | furniture | pages [19] -->
m

<!-- b001689 | furniture | pages [19] -->
m

<!-- b001690 | furniture | pages [19] -->
m

<!-- b001691 | furniture | pages [19] -->
m

<!-- b001692 | furniture | pages [19] -->
m

<!-- b001693 | furniture | pages [19] -->
m

<!-- b001694 | furniture | pages [19] -->
m

<!-- b001695 | furniture | pages [19] -->
m

<!-- b001696 | furniture | pages [19] -->
m

<!-- b001697 | furniture | pages [19] -->
m

<!-- b001698 | furniture | pages [19] -->
m

<!-- b001699 | furniture | pages [19] -->
m

<!-- b001700 | furniture | pages [19] -->
m

<!-- b001701 | furniture | pages [19] -->
m

<!-- b001702 | furniture | pages [19] -->
m

<!-- b001703 | furniture | pages [19] -->
m

<!-- b001704 | furniture | pages [19] -->
m

<!-- b001705 | furniture | pages [19] -->
m

<!-- b001706 | furniture | pages [19] -->
m

<!-- b001707 | furniture | pages [19] -->
m

<!-- b001708 | furniture | pages [19] -->
m

<!-- b001709 | furniture | pages [19] -->
m

<!-- b001710 | furniture | pages [19] -->
m

<!-- b001711 | furniture | pages [19] -->
m

<!-- b001712 | furniture | pages [19] -->
m

<!-- b001713 | furniture | pages [19] -->
m

<!-- b001714 | furniture | pages [19] -->
m

<!-- b001715 | furniture | pages [19] -->
m

<!-- b001716 | furniture | pages [19] -->
m

<!-- b001717 | furniture | pages [19] -->
m

<!-- b001718 | furniture | pages [19] -->
m

<!-- b001719 | furniture | pages [19] -->
m

<!-- b001720 | furniture | pages [19] -->
m

<!-- b001721 | furniture | pages [19] -->
m

<!-- b001722 | furniture | pages [19] -->
m

<!-- b001723 | furniture | pages [19] -->
m

<!-- b001724 | furniture | pages [19] -->
m

<!-- b001725 | furniture | pages [19] -->
m

<!-- b001726 | furniture | pages [19] -->
m

<!-- b001727 | furniture | pages [19] -->
m

<!-- b001728 | furniture | pages [19] -->
m

<!-- b001729 | furniture | pages [19] -->
m

<!-- b001730 | furniture | pages [19] -->
m

<!-- b001731 | furniture | pages [19] -->
m

<!-- b001732 | furniture | pages [19] -->
m

<!-- b001733 | furniture | pages [19] -->
m

<!-- b001734 | furniture | pages [19] -->
m

<!-- b001735 | furniture | pages [19] -->
m

<!-- b001736 | furniture | pages [19] -->
m

<!-- b001737 | furniture | pages [19] -->
m

<!-- b001738 | furniture | pages [19] -->
m

<!-- b001739 | furniture | pages [19] -->
m

<!-- b001740 | furniture | pages [19] -->
m

<!-- b001741 | furniture | pages [19] -->
m

<!-- b001742 | furniture | pages [19] -->
m

<!-- b001743 | furniture | pages [19] -->
m

<!-- b001744 | furniture | pages [19] -->
m

<!-- b001745 | furniture | pages [19] -->
m

<!-- b001746 | furniture | pages [19] -->
m

<!-- b001747 | furniture | pages [19] -->
m

<!-- b001748 | furniture | pages [19] -->
m

<!-- b001749 | furniture | pages [19] -->
m

<!-- b001750 | furniture | pages [19] -->
m

<!-- b001751 | furniture | pages [19] -->
m

<!-- b001752 | furniture | pages [19] -->
m

<!-- b001753 | furniture | pages [19] -->
m

<!-- b001754 | furniture | pages [19] -->
m

<!-- b001755 | furniture | pages [19] -->
m

<!-- b001756 | furniture | pages [19] -->
m

<!-- b001757 | furniture | pages [19] -->
m

<!-- b001758 | furniture | pages [19] -->
m

<!-- b001759 | furniture | pages [19] -->
m

<!-- b001760 | furniture | pages [19] -->
m

<!-- b001761 | furniture | pages [19] -->
m

<!-- b001762 | furniture | pages [19] -->
m

<!-- b001763 | furniture | pages [19] -->
m

<!-- b001764 | furniture | pages [19] -->
m

<!-- b001765 | furniture | pages [19] -->
m

<!-- b001766 | furniture | pages [19] -->
m

<!-- b001767 | furniture | pages [19] -->
m

<!-- b001768 | furniture | pages [19] -->
m

<!-- b001769 | furniture | pages [19] -->
m

<!-- b001770 | furniture | pages [19] -->
m

<!-- b001771 | furniture | pages [19] -->
m

<!-- b001772 | furniture | pages [19] -->
m

<!-- b001773 | furniture | pages [19] -->
m

<!-- b001774 | furniture | pages [19] -->
m

<!-- b001775 | furniture | pages [19] -->
m

<!-- b001776 | furniture | pages [19] -->
m

<!-- b001777 | furniture | pages [19] -->
m

<!-- b001778 | furniture | pages [19] -->
m

<!-- b001779 | furniture | pages [19] -->
m

<!-- b001780 | furniture | pages [19] -->
m

<!-- b001781 | furniture | pages [19] -->
m

<!-- b001782 | furniture | pages [19] -->
m

<!-- b001783 | furniture | pages [19] -->
m

<!-- b001784 | furniture | pages [19] -->
m

<!-- b001785 | furniture | pages [19] -->
m

<!-- b001786 | furniture | pages [19] -->
m

<!-- b001787 | furniture | pages [19] -->
m

<!-- b001788 | furniture | pages [19] -->
m

<!-- b001789 | furniture | pages [19] -->
m

<!-- b001790 | furniture | pages [19] -->
m

<!-- b001791 | furniture | pages [19] -->
m

<!-- b001792 | furniture | pages [19] -->
m

<!-- b001793 | furniture | pages [19] -->
m

<!-- b001794 | furniture | pages [19] -->
m

<!-- b001795 | furniture | pages [19] -->
m

<!-- b001796 | furniture | pages [19] -->
m

<!-- b001797 | furniture | pages [19] -->
m

<!-- b001798 | furniture | pages [19] -->
m

<!-- b001799 | furniture | pages [19] -->
m

<!-- b001800 | furniture | pages [19] -->
m

<!-- b001801 | furniture | pages [19] -->
m

<!-- b001802 | furniture | pages [19] -->
m

<!-- b001803 | furniture | pages [19] -->
m

<!-- b001804 | furniture | pages [19] -->
m

<!-- b001805 | furniture | pages [19] -->
m

<!-- b001806 | furniture | pages [19] -->
m

<!-- b001807 | furniture | pages [19] -->
m

<!-- b001808 | furniture | pages [19] -->
m

<!-- b001809 | furniture | pages [19] -->
m

<!-- b001810 | furniture | pages [19] -->
m

<!-- b001811 | furniture | pages [19] -->
m

<!-- b001812 | furniture | pages [19] -->
m

<!-- b001813 | furniture | pages [19] -->
m

<!-- b001814 | furniture | pages [19] -->
m

<!-- b001815 | furniture | pages [19] -->
m

<!-- b001816 | furniture | pages [19] -->
m

<!-- b001817 | furniture | pages [19] -->
m

<!-- b001818 | furniture | pages [19] -->
m

<!-- b001819 | furniture | pages [19] -->
m

<!-- b001820 | furniture | pages [19] -->
m

<!-- b001821 | furniture | pages [19] -->
m

<!-- b001822 | furniture | pages [19] -->
m

<!-- b001823 | furniture | pages [19] -->
m

<!-- b001824 | furniture | pages [19] -->
m

<!-- b001825 | furniture | pages [19] -->
m

<!-- b001826 | furniture | pages [19] -->
m

<!-- b001827 | furniture | pages [19] -->
m

<!-- b001828 | furniture | pages [19] -->
m

<!-- b001829 | furniture | pages [19] -->
m

<!-- b001830 | furniture | pages [19] -->
m

<!-- b001831 | furniture | pages [19] -->
m

<!-- b001832 | furniture | pages [19] -->
m

<!-- b001833 | furniture | pages [19] -->
m

<!-- b001834 | furniture | pages [19] -->
m

<!-- b001835 | furniture | pages [19] -->
m

<!-- b001836 | furniture | pages [19] -->
m

<!-- b001837 | furniture | pages [19] -->
m

<!-- b001838 | furniture | pages [19] -->
m

<!-- b001839 | furniture | pages [19] -->
m

<!-- b001840 | furniture | pages [19] -->
m

<!-- b001841 | furniture | pages [19] -->
m

<!-- b001842 | furniture | pages [19] -->
m

<!-- b001843 | furniture | pages [19] -->
m

<!-- b001844 | furniture | pages [19] -->
m

<!-- b001845 | furniture | pages [19] -->
m

<!-- b001846 | furniture | pages [19] -->
m

<!-- b001847 | furniture | pages [19] -->
m

<!-- b001848 | furniture | pages [19] -->
m

<!-- b001849 | furniture | pages [19] -->
m

<!-- b001850 | furniture | pages [19] -->
m

<!-- b001851 | furniture | pages [19] -->
m

<!-- b001852 | furniture | pages [19] -->
m

<!-- b001853 | furniture | pages [19] -->
m

<!-- b001854 | furniture | pages [19] -->
m

<!-- b001855 | furniture | pages [19] -->
m

<!-- b001856 | furniture | pages [19] -->
m

<!-- b001857 | furniture | pages [19] -->
m

<!-- b001858 | furniture | pages [19] -->
m

<!-- b001859 | furniture | pages [19] -->
m

<!-- b001860 | furniture | pages [19] -->
m

<!-- b001861 | furniture | pages [19] -->
m

<!-- b001862 | furniture | pages [19] -->
m

<!-- b001863 | furniture | pages [19] -->
m

<!-- b001864 | furniture | pages [19] -->
m

<!-- b001865 | furniture | pages [19] -->
m

<!-- b001866 | furniture | pages [19] -->
m

<!-- b001867 | furniture | pages [19] -->
m

<!-- b001868 | furniture | pages [19] -->
m

<!-- b001869 | furniture | pages [19] -->
m

<!-- b001870 | furniture | pages [19] -->
m

<!-- b001871 | furniture | pages [19] -->
m

<!-- b001872 | furniture | pages [19] -->
m

<!-- b001873 | furniture | pages [19] -->
m

<!-- b001874 | furniture | pages [19] -->
m

<!-- b001875 | furniture | pages [19] -->
m

<!-- b001876 | furniture | pages [19] -->
m

<!-- b001877 | furniture | pages [19] -->
m

<!-- b001878 | furniture | pages [19] -->
m

<!-- b001879 | furniture | pages [19] -->
m

<!-- b001880 | furniture | pages [19] -->
m

<!-- b001881 | furniture | pages [19] -->
m

<!-- b001882 | furniture | pages [19] -->
m

<!-- b001883 | furniture | pages [19] -->
m

<!-- b001884 | furniture | pages [19] -->
m

<!-- b001885 | furniture | pages [19] -->
m

<!-- b001886 | furniture | pages [19] -->
m

<!-- b001887 | furniture | pages [19] -->
m

<!-- b001888 | furniture | pages [19] -->
m

<!-- b001889 | furniture | pages [19] -->
m

<!-- b001890 | furniture | pages [19] -->
m

<!-- b001891 | furniture | pages [19] -->
m

<!-- b001892 | furniture | pages [19] -->
m

<!-- b001893 | furniture | pages [19] -->
m

<!-- b001894 | furniture | pages [19] -->
m

<!-- b001895 | furniture | pages [19] -->
m

<!-- b001896 | furniture | pages [19] -->
m

<!-- b001897 | furniture | pages [19] -->
m

<!-- b001898 | furniture | pages [19] -->
m

<!-- b001899 | furniture | pages [19] -->
m

<!-- b001900 | furniture | pages [19] -->
m

<!-- b001901 | furniture | pages [19] -->
m

<!-- b001902 | furniture | pages [19] -->
m

<!-- b001903 | furniture | pages [19] -->
m

<!-- b001904 | furniture | pages [20] -->
Team 2524070

<!-- b001905 | furniture | pages [20] -->
Page 20of 25

<!-- b001907 | prose | pages [20] -->
3. Anastasia Bliznyuk, who began coaching in China in 2022, secured a gold medal in the Group All-Around Rhythmic Gymnastics event at the 2024 Paris Olympics;

<!-- b001908 | prose | pages [20] -->
4. Erwann Le Péchoux, who has been coaching the Chinese fencing team since 2021 and won a gold medal in Men’s Foil Team fencing.

<!-- b001909 | heading | pages [20] -->
6.1 Analysis of Variance, Mixed-effects Model

<!-- b001910 | prose | pages [20] -->
We aim to investigate the role of a "great coach" as a variable influencing a country’s sports performance. This variable has two levels: a value of 1 indicates the presence of a "great coach," while a value of 0 indicates their absence. However, we recognize that the effectiveness of a "great coach" may depend on the specific conditions within a country. Even with an outstanding coach, if the athletes are unable to collaborate effectively or lack the necessary skills, the country’s sports performance may not improve. Therefore, it is essential to consider each country’s unique circumstances alongside the "great coach" factor to accurately assess the coach’s impact.

<!-- b001911 | prose | pages [20] -->
To facilitate this analysis, we will categorize our units of analysis into distinct "blocks", each comprising a specific coach and the country they represent. For example, Lang Ping coaching the U.S. team would represent one block, while her coaching of the Chinese team would constitute another. This approach will enhance our understanding of the relationship between coaches and countries and its impact on performance.

<!-- b001912 | prose | pages [20] -->
In our analysis, the presence of a "great coach" will be treated as a fixed effect, enabling us to concentrate on the specific impact of each coach. Conversely, the "block effect" will be regarded as a random effect, given that our study involves a limited selection of coaches and countries.

<!-- b001913 | prose | pages [20] -->
In summary, a country’s performance can be decomposed as follows:

<!-- b001914 | prose | pages [20] -->
𝑆𝑐𝑜𝑟𝑒= 𝜑0 + 𝜑1𝜔+ 𝛿+ 𝜀 (13) ( 1, if a "great" coach is present 𝜔= (14) 0, if no "great" coach is present 𝛿∼N(0, 𝜎2 𝛿), 𝜀∼N(0, 𝜎2) (15)

<!-- b001915 | prose | pages [20] -->
In this context, 𝜑1 denotes the constant effect of the "great coach", 𝛿signifies the random effect associated with the block, and 𝜀stands for the error term.

<!-- b001916 | heading | pages [20] -->
6.2 Definition of the Response Variable

<!-- b001917 | prose | pages [20] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m How should we define the response variable? We believe that using the total number of medals m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m earned by teams led by "great coaches" is not appropriate. Gold, silver, and bronze medals should not m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m be treated as equal; for some nations, achieving their first bronze medal is a significant milestone, while m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m for already successful countries, progressing from silver to gold represents a substantial advancement. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Selecting only one type of medal fails to capture the true impact of "great coaches". Furthermore,

<!-- b001918 | prose | pages [20, 21] -->
关注数学模型 different types of medals cannot be simply aggregated to reflect the influence of "great coaches" on a country's performance in a specific sport. After thorough consideration, we have decided to assign weights to each type of medal, and the final weights are presented in the table below:

<!-- b001919 | furniture | pages [20] -->
2

<!-- b001920 | furniture | pages [20] -->
MATHmodels

<!-- b001921 | furniture | pages [20] -->
获取更多资讯

<!-- b001922 | furniture | pages [21] -->
Team 2524070

<!-- b001923 | furniture | pages [21] -->
Page 21of 25

<!-- b001925 | prose | pages [21] -->
Silver Bronze No Medal Gold

<!-- b001926 | prose | pages [21] -->
Weights 10 5 0

<!-- b001927 | caption | pages [21] -->
Table 9: Weights of Different Medals

<!-- b001928 | prose | pages [21] -->
The definition and calculation formula for the response variable value is as follows:

<!-- b001929 | prose | pages [21] -->
● Score = 10× ngold + 5× nsilver + 2× nbronze (16)

<!-- b001930 | heading | pages [21] -->
6.3 Problem Solutions

<!-- b001931 | prose | pages [21] -->
We believe that the influence of a "great coach" can have a significant but short-lived impact on the countries they coach. To analyze this phenomenon, we examine the year a country hired the "great coach" and review the outcomes of the last three Olympic Games in which they participated, as well as the results of the subsequent two Olympic Games, totaling six Olympic Games. For each experimental point, we conduct three repetitions and perform a variance analysis of these results using a mixed-effects model with equal repetitions. If the fixed effect is both significant and positive, it indicates the existence of the "great coach" effect, allowing us to estimate this effect based on the point estimate of the effect of the fixed factor in the mixed-effects model.

<!-- b001932 | prose | pages [21] -->
● Block1 Block2 Block3 Block5 Block4 0 a011, a012, a013 a021, a022, a023 a051, a052, a053 a031, a032, a033 a041, a042, a043 1 a111, a112, a113 a131, a132, a133 a141, a142, a143 a151, a152, a153 a121, a122, a123

<!-- b001933 | caption | pages [21] -->
Table 10: Repeated Measures Mixed-effects Experimental Data Table

<!-- b001934 | heading | pages [21] -->
6.4 Fitting the Model

<!-- b001935 | prose | pages [21] -->
We have conducted a preliminary fitting of the model and obtained the following results.

<!-- b001936 | prose | pages [21] -->
The table below indicates that the variance of the random factor is quite low and can be ignored. We create a residual plot and a QQ plot to assess if the data satisfy the assumptions of normality and homoscedasticity.

<!-- b001937 | furniture | pages [22] -->
Team 2524070

<!-- b001938 | furniture | pages [22] -->
Page 22of 25

<!-- b001939 | prose | pages [22] -->
Random Effects Variance Std. Dev.

<!-- b001940 | prose | pages [22] -->
Block 7.220e-14 2.687e-07 Residual 9.395 3.065

<!-- b001941 | prose | pages [22] -->
Number of observations: 32, groups: block, 5

<!-- b001942 | prose | pages [22] -->
Fixed Effects Estimate Std. Error df t value Pr(>|t|)

<!-- b001943 | prose | pages [22] -->
(Intercept) 0.4118 0.7434 30.0000 0.554 0.584 Fixed Factor 6.7216 1.0858 30.0000 6.190 8.2e-07 ***

<!-- b001944 | prose | pages [22] -->
Significance codes: 0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

<!-- b001945 | caption | pages [22] -->
Table 11: Random and Fixed Effects Summary

<!-- b001946 | prose | pages [22] -->
(a) Distribution of Gold Medals (b) Distribution of Total Medals

<!-- b001947 | caption | pages [22] -->
Figure 11: QQ Plot and Residuals Plot for Model Diagnostics

<!-- b001948 | prose | pages [22] -->
The QQ plot indicates that the data fails to satisfy the normality assumption, and the residual plot reveals a noticeable trend. To address this issue, we apply the Box-Cox transformation in an effort to adjust the parameters to align with the Gauss-Markov assumptions. Since the Box-Cox transformation requires the data to be positive and our dataset contains zeros, we have adjusted the values by adding one to each. The calculated coefficient for the Box-Cox transformation is 0.38. After performing the transformation and refitting the data, we generate new QQ and residual plots.

<!-- b001949 | prose | pages [22] -->
(a) Distribution of Gold Medals (b) Distribution of Total Medals

<!-- b001950 | caption | pages [22] -->
Figure 12: QQ Plot and Residuals Plot for Model Diagnostics(After Box-Cox Transformation)

<!-- b001951 | prose | pages [22, 23] -->
关注数学模型 At this stage, the QQ plot shows a slanted straight line, with data points scattered around it, indicating that the data appears to satisfy the normality assumption. However, an analysis of the residual plot reveals that there is still a noticeable trend in the data following the Box-Cox transformation, suggesting that the residuals do not meet the homoscedasticity requirement. Consequently, we applied 微信公众号：数学模型 White’s robust standard errors to adjust and evaluate the model fitting results, which are presented in the table below. The effect of the "great coach" factor, obtained through the Box-Cox inverse

<!-- b001952 | furniture | pages [22] -->
2

<!-- b001953 | furniture | pages [22] -->
MATHmodels

<!-- b001954 | furniture | pages [22] -->
获取更多资讯

<!-- b001955 | furniture | pages [23] -->
Team 2524070

<!-- b001956 | furniture | pages [23] -->
Page 23of 25

<!-- b001958 | prose | pages [23] -->
Variable Estimate Std. Error t value Pr(>|t|)

<!-- b001959 | heading | pages [23] -->
CI Lower

<!-- b001960 | heading | pages [23] -->
CI Upper

<!-- b001961 | prose | pages [23] -->
df

<!-- b001962 | prose | pages [23] -->
(Intercept) 0.1289 0.08992 1.434 0.1619 -0.05471 0.3126 30 Fixed Factor 1.1719 0.14391 8.143 4.329e-09 0.87800 1.4658 30

<!-- b001963 | caption | pages [23] -->
Table 12: Model Estimates with Confidence Intervals and t-Statistics

<!-- b001964 | prose | pages [23] -->
transformation formula, is 3.74.

<!-- b001965 | prose | pages [23] -->
微信号：MATHmodels

<!-- b001966 | heading | pages [23] -->
6.5 Results

<!-- b001967 | prose | pages [23] -->
We conducted research to identify countries eager to achieve breakthroughs in specific sporting events. We found that Australia is particularly focused on advancing in basketball and tennis, with tennis being a traditional sport. However, in recent years, both men’s singles tennis and men’s basketball have failed to secure any medals. A similar situation is observed in France with men’s 100m sprint athletics and in Canada with men’s basketball.

<!-- b001968 | prose | pages [23] -->
Based on the estimated "Great Coach" effect and the conversion relationship between effect size and medal weight, if these nations choose to invest in a "great coach", the following outcomes are expected:

<!-- b001969 | prose | pages [23] -->
1. For countries that currently lack the capacity to secure a medal, there is a 74.8% probability of winning a silver medal following investment;

<!-- b001970 | prose | pages [23] -->
2. For countries that can achieve a bronze medal but not a silver, there is a 57.4% probability of winning a gold medal following investment;

<!-- b001971 | prose | pages [23] -->
3. For countries that are capable of winning a silver medal but not a gold, there is an 87.4% probability of winning a gold medal following investment.

<!-- b001972 | caption | pages [23] -->
Figure 13: If these countries invest in great coaches, they will reap the rewards of medals.

<!-- b001973 | prose | pages [23, 24] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 7 What Else Is Included in Our Model?

<!-- b001974 | furniture | pages [23] -->
m

<!-- b001975 | furniture | pages [23] -->
m

<!-- b001976 | furniture | pages [23] -->
m

<!-- b001977 | furniture | pages [23] -->
m

<!-- b001978 | furniture | pages [23] -->
m

<!-- b001979 | furniture | pages [23] -->
m

<!-- b001980 | furniture | pages [23] -->
m

<!-- b001981 | furniture | pages [23] -->
m

<!-- b001982 | furniture | pages [23] -->
m

<!-- b001983 | furniture | pages [23] -->
m

<!-- b001984 | furniture | pages [23] -->
m

<!-- b001985 | furniture | pages [23] -->
m

<!-- b001986 | furniture | pages [23] -->
m

<!-- b001987 | furniture | pages [23] -->
m

<!-- b001988 | furniture | pages [23] -->
m

<!-- b001989 | furniture | pages [23] -->
m

<!-- b001990 | furniture | pages [23] -->
m

<!-- b001991 | furniture | pages [23] -->
m

<!-- b001992 | furniture | pages [23] -->
m

<!-- b001993 | furniture | pages [23] -->
m

<!-- b001994 | furniture | pages [23] -->
m

<!-- b001995 | furniture | pages [23] -->
m

<!-- b001996 | furniture | pages [23] -->
m

<!-- b001997 | furniture | pages [23] -->
m

<!-- b001998 | furniture | pages [23] -->
m

<!-- b001999 | furniture | pages [23] -->
m

<!-- b002000 | furniture | pages [23] -->
m

<!-- b002001 | furniture | pages [23] -->
m

<!-- b002002 | furniture | pages [23] -->
m

<!-- b002003 | furniture | pages [23] -->
m

<!-- b002004 | furniture | pages [23] -->
m

<!-- b002005 | furniture | pages [23] -->
m

<!-- b002006 | furniture | pages [23] -->
m

<!-- b002007 | furniture | pages [23] -->
m

<!-- b002008 | furniture | pages [23] -->
m

<!-- b002009 | furniture | pages [23] -->
m

<!-- b002010 | furniture | pages [23] -->
m

<!-- b002011 | furniture | pages [23] -->
m

<!-- b002012 | furniture | pages [23] -->
m

<!-- b002013 | furniture | pages [23] -->
m

<!-- b002014 | furniture | pages [23] -->
m

<!-- b002015 | furniture | pages [23] -->
m

<!-- b002016 | furniture | pages [23] -->
m

<!-- b002017 | furniture | pages [23] -->
m

<!-- b002018 | furniture | pages [23] -->
m

<!-- b002019 | furniture | pages [23] -->
m

<!-- b002020 | furniture | pages [23] -->
m

<!-- b002021 | furniture | pages [23] -->
m

<!-- b002022 | furniture | pages [23] -->
m

<!-- b002023 | furniture | pages [23] -->
m

<!-- b002024 | furniture | pages [23] -->
m

<!-- b002025 | furniture | pages [23] -->
m

<!-- b002026 | furniture | pages [23] -->
m

<!-- b002027 | furniture | pages [23] -->
m

<!-- b002028 | furniture | pages [23] -->
m

<!-- b002029 | furniture | pages [23] -->
m

<!-- b002030 | furniture | pages [23] -->
m

<!-- b002031 | furniture | pages [23] -->
m

<!-- b002032 | furniture | pages [23] -->
m

<!-- b002033 | furniture | pages [23] -->
m

<!-- b002034 | furniture | pages [23] -->
m

<!-- b002035 | furniture | pages [23] -->
m

<!-- b002036 | furniture | pages [23] -->
m

<!-- b002037 | furniture | pages [23] -->
m

<!-- b002038 | furniture | pages [23] -->
m

<!-- b002039 | furniture | pages [23] -->
m

<!-- b002040 | furniture | pages [23] -->
m

<!-- b002041 | furniture | pages [23] -->
m

<!-- b002042 | furniture | pages [23] -->
m

<!-- b002043 | furniture | pages [23] -->
m

<!-- b002044 | furniture | pages [23] -->
m

<!-- b002045 | furniture | pages [23] -->
m

<!-- b002046 | furniture | pages [23] -->
m

<!-- b002047 | furniture | pages [23] -->
m

<!-- b002048 | furniture | pages [23] -->
m

<!-- b002049 | furniture | pages [23] -->
m

<!-- b002050 | furniture | pages [23] -->
m

<!-- b002051 | furniture | pages [23] -->
m

<!-- b002052 | furniture | pages [23] -->
m

<!-- b002053 | furniture | pages [23] -->
m

<!-- b002054 | furniture | pages [23] -->
m

<!-- b002055 | furniture | pages [23] -->
m

<!-- b002056 | furniture | pages [23] -->
m

<!-- b002057 | furniture | pages [23] -->
m

<!-- b002058 | furniture | pages [23] -->
m

<!-- b002059 | furniture | pages [23] -->
m

<!-- b002060 | furniture | pages [23] -->
m

<!-- b002061 | furniture | pages [23] -->
m

<!-- b002062 | furniture | pages [23] -->
m

<!-- b002063 | furniture | pages [23] -->
m

<!-- b002064 | furniture | pages [23] -->
m

<!-- b002065 | furniture | pages [23] -->
m

<!-- b002066 | furniture | pages [23] -->
m

<!-- b002067 | furniture | pages [23] -->
m

<!-- b002068 | furniture | pages [23] -->
m

<!-- b002069 | furniture | pages [23] -->
m

<!-- b002070 | furniture | pages [23] -->
m

<!-- b002071 | furniture | pages [23] -->
m

<!-- b002072 | furniture | pages [23] -->
m

<!-- b002073 | furniture | pages [23] -->
m

<!-- b002074 | furniture | pages [23] -->
m

<!-- b002075 | furniture | pages [23] -->
m

<!-- b002076 | furniture | pages [23] -->
m

<!-- b002077 | furniture | pages [23] -->
m

<!-- b002078 | furniture | pages [23] -->
m

<!-- b002079 | furniture | pages [23] -->
m

<!-- b002080 | furniture | pages [23] -->
m

<!-- b002081 | furniture | pages [23] -->
m

<!-- b002082 | furniture | pages [23] -->
m

<!-- b002083 | furniture | pages [23] -->
m

<!-- b002084 | furniture | pages [23] -->
m

<!-- b002085 | furniture | pages [23] -->
m

<!-- b002086 | furniture | pages [23] -->
m

<!-- b002087 | furniture | pages [23] -->
m

<!-- b002088 | furniture | pages [23] -->
m

<!-- b002089 | furniture | pages [23] -->
m

<!-- b002090 | furniture | pages [23] -->
m

<!-- b002091 | furniture | pages [23] -->
m

<!-- b002092 | furniture | pages [23] -->
m

<!-- b002093 | furniture | pages [23] -->
m

<!-- b002094 | furniture | pages [23] -->
m

<!-- b002095 | furniture | pages [23] -->
m

<!-- b002096 | furniture | pages [23] -->
m

<!-- b002097 | furniture | pages [23] -->
m

<!-- b002098 | furniture | pages [23] -->
m

<!-- b002099 | furniture | pages [23] -->
m

<!-- b002100 | furniture | pages [23] -->
m

<!-- b002101 | furniture | pages [23] -->
m

<!-- b002102 | furniture | pages [23] -->
m

<!-- b002103 | furniture | pages [23] -->
m

<!-- b002104 | furniture | pages [23] -->
m

<!-- b002105 | furniture | pages [23] -->
m

<!-- b002106 | furniture | pages [23] -->
m

<!-- b002107 | furniture | pages [23] -->
m

<!-- b002108 | furniture | pages [23] -->
m

<!-- b002109 | furniture | pages [23] -->
m

<!-- b002110 | furniture | pages [23] -->
m

<!-- b002111 | furniture | pages [23] -->
m

<!-- b002112 | furniture | pages [23] -->
m

<!-- b002113 | furniture | pages [23] -->
m

<!-- b002114 | furniture | pages [23] -->
m

<!-- b002115 | furniture | pages [23] -->
m

<!-- b002116 | furniture | pages [23] -->
m

<!-- b002117 | furniture | pages [23] -->
m

<!-- b002118 | furniture | pages [23] -->
m

<!-- b002119 | furniture | pages [23] -->
m

<!-- b002120 | furniture | pages [23] -->
m

<!-- b002121 | furniture | pages [23] -->
m

<!-- b002122 | furniture | pages [23] -->
m

<!-- b002123 | furniture | pages [23] -->
m

<!-- b002124 | furniture | pages [23] -->
m

<!-- b002125 | furniture | pages [23] -->
m

<!-- b002126 | furniture | pages [23] -->
m

<!-- b002127 | furniture | pages [23] -->
m

<!-- b002128 | furniture | pages [23] -->
m

<!-- b002129 | furniture | pages [23] -->
m

<!-- b002130 | furniture | pages [23] -->
m

<!-- b002131 | furniture | pages [23] -->
m

<!-- b002132 | furniture | pages [23] -->
m

<!-- b002133 | furniture | pages [23] -->
m

<!-- b002134 | furniture | pages [23] -->
m

<!-- b002135 | furniture | pages [23] -->
m

<!-- b002136 | furniture | pages [23] -->
m

<!-- b002137 | furniture | pages [23] -->
m

<!-- b002138 | furniture | pages [23] -->
m

<!-- b002139 | furniture | pages [23] -->
m

<!-- b002140 | furniture | pages [23] -->
m

<!-- b002141 | furniture | pages [23] -->
m

<!-- b002142 | furniture | pages [23] -->
m

<!-- b002143 | furniture | pages [23] -->
m

<!-- b002144 | furniture | pages [23] -->
m

<!-- b002145 | furniture | pages [23] -->
m

<!-- b002146 | furniture | pages [23] -->
m

<!-- b002147 | furniture | pages [23] -->
m

<!-- b002148 | furniture | pages [23] -->
m

<!-- b002149 | furniture | pages [23] -->
m

<!-- b002150 | furniture | pages [23] -->
m

<!-- b002151 | furniture | pages [23] -->
m

<!-- b002152 | furniture | pages [23] -->
m

<!-- b002153 | furniture | pages [23] -->
m

<!-- b002154 | furniture | pages [23] -->
m

<!-- b002155 | furniture | pages [23] -->
m

<!-- b002156 | furniture | pages [23] -->
m

<!-- b002157 | furniture | pages [23] -->
m

<!-- b002158 | furniture | pages [23] -->
m

<!-- b002159 | furniture | pages [23] -->
m

<!-- b002160 | furniture | pages [23] -->
m

<!-- b002161 | furniture | pages [23] -->
m

<!-- b002162 | furniture | pages [23] -->
m

<!-- b002163 | furniture | pages [23] -->
m

<!-- b002164 | furniture | pages [23] -->
m

<!-- b002165 | furniture | pages [23] -->
m

<!-- b002166 | furniture | pages [23] -->
m

<!-- b002167 | furniture | pages [23] -->
m

<!-- b002168 | furniture | pages [23] -->
m

<!-- b002169 | furniture | pages [23] -->
m

<!-- b002170 | furniture | pages [23] -->
m

<!-- b002171 | furniture | pages [23] -->
m

<!-- b002172 | furniture | pages [23] -->
m

<!-- b002173 | furniture | pages [23] -->
m

<!-- b002174 | furniture | pages [23] -->
m

<!-- b002175 | furniture | pages [23] -->
m

<!-- b002176 | furniture | pages [23] -->
m

<!-- b002177 | furniture | pages [23] -->
m

<!-- b002178 | furniture | pages [23] -->
m

<!-- b002179 | furniture | pages [23] -->
m

<!-- b002180 | furniture | pages [23] -->
m

<!-- b002181 | furniture | pages [23] -->
m

<!-- b002182 | furniture | pages [23] -->
m

<!-- b002183 | furniture | pages [23] -->
m

<!-- b002184 | furniture | pages [23] -->
m

<!-- b002185 | furniture | pages [23] -->
m

<!-- b002186 | furniture | pages [23] -->
m

<!-- b002187 | furniture | pages [23] -->
m

<!-- b002188 | furniture | pages [23] -->
m

<!-- b002189 | furniture | pages [23] -->
m

<!-- b002190 | furniture | pages [23] -->
m

<!-- b002191 | furniture | pages [23] -->
m

<!-- b002192 | furniture | pages [23] -->
m

<!-- b002193 | furniture | pages [23] -->
m

<!-- b002194 | furniture | pages [23] -->
m

<!-- b002195 | furniture | pages [23] -->
m

<!-- b002196 | furniture | pages [23] -->
m

<!-- b002197 | furniture | pages [23] -->
m

<!-- b002198 | furniture | pages [23] -->
m

<!-- b002199 | furniture | pages [23] -->
m

<!-- b002200 | furniture | pages [23] -->
m

<!-- b002201 | furniture | pages [23] -->
m

<!-- b002202 | furniture | pages [23] -->
m

<!-- b002203 | furniture | pages [23] -->
m

<!-- b002204 | furniture | pages [23] -->
m

<!-- b002205 | furniture | pages [23] -->
m

<!-- b002206 | furniture | pages [23] -->
m

<!-- b002207 | furniture | pages [23] -->
m

<!-- b002208 | furniture | pages [23] -->
m

<!-- b002209 | furniture | pages [23] -->
m

<!-- b002210 | furniture | pages [23] -->
m

<!-- b002211 | furniture | pages [23] -->
m

<!-- b002212 | furniture | pages [23] -->
m

<!-- b002213 | furniture | pages [23] -->
m

<!-- b002214 | furniture | pages [23] -->
m

<!-- b002215 | furniture | pages [23] -->
m

<!-- b002216 | furniture | pages [23] -->
m

<!-- b002217 | furniture | pages [23] -->
m

<!-- b002218 | furniture | pages [23] -->
m

<!-- b002219 | furniture | pages [23] -->
m

<!-- b002220 | furniture | pages [23] -->
m

<!-- b002221 | furniture | pages [23] -->
m

<!-- b002222 | furniture | pages [23] -->
m

<!-- b002223 | furniture | pages [23] -->
m

<!-- b002224 | furniture | pages [23] -->
m

<!-- b002225 | furniture | pages [23] -->
m

<!-- b002226 | furniture | pages [23] -->
m

<!-- b002227 | furniture | pages [23] -->
m

<!-- b002228 | furniture | pages [23] -->
m

<!-- b002229 | furniture | pages [23] -->
m

<!-- b002230 | furniture | pages [23] -->
m

<!-- b002231 | furniture | pages [23] -->
m

<!-- b002232 | furniture | pages [23] -->
m

<!-- b002233 | furniture | pages [23] -->
m

<!-- b002234 | furniture | pages [23] -->
m

<!-- b002235 | furniture | pages [23] -->
m

<!-- b002236 | furniture | pages [23] -->
m

<!-- b002237 | furniture | pages [23] -->
m

<!-- b002238 | furniture | pages [23] -->
m

<!-- b002239 | furniture | pages [23] -->
m

<!-- b002240 | furniture | pages [23] -->
m

<!-- b002241 | furniture | pages [23] -->
m

<!-- b002242 | furniture | pages [23] -->
m

<!-- b002243 | furniture | pages [23] -->
m

<!-- b002244 | furniture | pages [23] -->
m

<!-- b002245 | furniture | pages [23] -->
m

<!-- b002246 | furniture | pages [23] -->
m

<!-- b002247 | furniture | pages [23] -->
m

<!-- b002248 | furniture | pages [23] -->
m

<!-- b002249 | furniture | pages [23] -->
m

<!-- b002250 | furniture | pages [23] -->
m

<!-- b002251 | furniture | pages [23] -->
m

<!-- b002252 | furniture | pages [23] -->
m

<!-- b002253 | furniture | pages [23] -->
m

<!-- b002254 | furniture | pages [23] -->
m

<!-- b002255 | furniture | pages [23] -->
m

<!-- b002256 | furniture | pages [23] -->
m

<!-- b002257 | furniture | pages [23] -->
m

<!-- b002258 | furniture | pages [23] -->
m

<!-- b002259 | furniture | pages [23] -->
m

<!-- b002260 | furniture | pages [23] -->
m

<!-- b002261 | furniture | pages [23] -->
m

<!-- b002262 | furniture | pages [23] -->
m

<!-- b002263 | furniture | pages [23] -->
m

<!-- b002264 | furniture | pages [23] -->
m

<!-- b002265 | furniture | pages [23] -->
m

<!-- b002266 | furniture | pages [23] -->
m

<!-- b002267 | furniture | pages [23] -->
m

<!-- b002268 | furniture | pages [23] -->
m

<!-- b002269 | furniture | pages [23] -->
m

<!-- b002270 | furniture | pages [23] -->
m

<!-- b002271 | furniture | pages [23] -->
m

<!-- b002272 | furniture | pages [23] -->
m

<!-- b002273 | furniture | pages [23] -->
m

<!-- b002274 | furniture | pages [23] -->
m

<!-- b002275 | furniture | pages [23] -->
m

<!-- b002276 | furniture | pages [23] -->
m

<!-- b002277 | furniture | pages [23] -->
m

<!-- b002278 | furniture | pages [23] -->
m

<!-- b002279 | furniture | pages [23] -->
m

<!-- b002280 | furniture | pages [23] -->
m

<!-- b002281 | furniture | pages [23] -->
m

<!-- b002282 | furniture | pages [23] -->
m

<!-- b002283 | furniture | pages [23] -->
m

<!-- b002284 | furniture | pages [23] -->
m

<!-- b002285 | furniture | pages [23] -->
m

<!-- b002286 | furniture | pages [23] -->
m

<!-- b002287 | furniture | pages [23] -->
m

<!-- b002288 | furniture | pages [23] -->
m

<!-- b002289 | furniture | pages [23] -->
m

<!-- b002290 | furniture | pages [23] -->
m

<!-- b002291 | furniture | pages [23] -->
m

<!-- b002292 | furniture | pages [23] -->
m

<!-- b002293 | furniture | pages [23] -->
m

<!-- b002294 | furniture | pages [23] -->
m

<!-- b002295 | furniture | pages [23] -->
m

<!-- b002296 | furniture | pages [23] -->
m

<!-- b002297 | furniture | pages [23] -->
m

<!-- b002298 | furniture | pages [24] -->
Team 2524070

<!-- b002299 | furniture | pages [24] -->
Page 24of 25

<!-- b002301 | prose | pages [24] -->
While conventional wisdom holds that "more events lead to higher medal chances", our Bayesian regression model shows: The regression coefficient for event count (𝛽4) has a 95% Highest Density Interval (HDI) that fully overlaps with zero. This means increasing the number of events entered does not have a statistically significant impact on a nation’s total medal count.

<!-- b002302 | prose | pages [24] -->
Furthermore, the findings from the Events-Medals Association Rule Model in the United States show a significant link between restricted involvement in specific sports and an increased total medal tally for the nation. This suggests that it is crucial for a country to carefully select the events it competes in, rather than taking part in a wide range of competitions.

<!-- b002303 | prose | pages [24] -->
Strategic Implications for Olympic Committees:

<!-- b002304 | heading | pages [24] -->
1. Resource Reallocation Opportunity: Concentrating resources on dominant events rather than

<!-- b002305 | prose | pages [24] -->
dispersing them across multiple disciplines may create a "focus effect" for higher returns.

<!-- b002306 | heading | pages [24] -->
2. Qualification Strategy Overhaul: Transition from a "quantity-driven" participation model to

<!-- b002307 | prose | pages [24] -->
a "medal conversion rate" evaluation system to prioritize high-potential events.

<!-- b002308 | heading | pages [24] -->
3. Talent Development Shift: Targeted investments in athletes/projects with podium potential

<!-- b002309 | prose | pages [24] -->
yield better results than a broad but shallow approach to talent cultivation.

<!-- b002310 | heading | pages [24] -->
8 Model Evaluation

<!-- b002311 | heading | pages [24] -->
8.1 Advantages

<!-- b002312 | prose | pages [24] -->
1. Zero-Inflated Negative Binomial Model.

<!-- b002313 | prose | pages [24] -->
(a) This model generally has two elements: one uses a binomial distribution to represent the creation of zeros, and the other applies a negative binomial distribution to describe the non-zero values. This two-part framework allows the model to effectively handle both true zero counts and non-zero count data at the same time.

<!-- b002314 | prose | pages [24] -->
(b) Unlike regression models or machine learning algorithms designed for continuous out- comes, the Zero-Inflated Negative Binomial model is specifically tailored for count data. It ensures that predictions are non-negative integers, thus avoiding the problem of predicting continuous values or negative numbers, which would be unrealistic in count data scenarios.

<!-- b002315 | prose | pages [24] -->
2. GRI Association Rule Model.

<!-- b002316 | prose | pages [24] -->
(a) Association rule mining is an automated analysis method that does not rely on pre-set hypotheses but directly extracts relationships from data, avoiding biases from manual assumptions.

<!-- b002317 | prose | pages [24] -->
(b) This model can handle large-scale datasets. The historical data of the Olympics involves a vast and complex array of data from multiple countries, spanning various years, and numerousevents, andusing associationrulescanefficientlyrevealthe intricaterelationships between the data.

<!-- b002318 | prose | pages [24, 25] -->
关注数学模型 (c) The output of association rules is typically presented in the form of "if... then...", making the interpretation of the rules intuitive and easy to understand.

<!-- b002319 | furniture | pages [24] -->
2

<!-- b002320 | furniture | pages [24] -->
MATHmodels

<!-- b002321 | furniture | pages [24] -->
获取更多资讯

<!-- b002322 | furniture | pages [25] -->
Team 2524070

<!-- b002323 | furniture | pages [25] -->
Page 25of 25

<!-- b002325 | prose | pages [25] -->
(d) GRI can discover multi-level associations. For example, it can reveal not only the relation- ship between a single event and the total number of medals but also the combined impact of multiple events on the number of medals.

<!-- b002326 | prose | pages [25] -->
3. Mixed-effects Model. Mixed-effects models are highly effective for assessing significant differ- 微信公众号：数学模型 ences among various levels of factors and accurately estimating the effects associated with fixed factor levels. This model facilitates the investigation of the "great coach" effect, showcasing both efficacy and clarity in their application.

<!-- b002327 | heading | pages [25] -->
8.2 Limitations

<!-- b002328 | prose | pages [25] -->
1. The resolution of the zero-inflated negative binomial model is accomplished through the imple- mentation of the Markov Chain Monte Carlo (MCMC) algorithm, which necessitates consider- able computational resources and is marked by lengthy processing times.

<!-- b002329 | prose | pages [25] -->
微信号：MATHmodels 2. Forecasting medal counts utilizes a simulation approach that also demands significant compu- tational resources and entails extended solving durations.

<!-- b002330 | prose | pages [25] -->
3. When mining rules, GRI may encounter false positive issues (irrelevant rules mistakenly iden- tified as having strong associations). For instance, we may not be particularly concerned about strong rules where mc equals 0, but such rules can still occur.

<!-- b002331 | heading | pages [25] -->
References

<!-- b002332 | references | pages [25] -->
[1] Csurilla, Gergely, and Imre Fertő. 2024. "How to win the first Olympic medal? And the second?".

<!-- b002333 | references | pages [25] -->
Social Science Quarterly 105: 1544–1564. https://doi.org/10.1111/ssqu.13436.

<!-- b002334 | references | pages [25] -->
[2] Olympic Games France Delegation.

<!-- b002335 | references | pages [25] -->
[3] How patience helps French sprinter Lemaitre to aim for a third Olympic podium.

<!-- b002336 | references | pages [25] -->
[4] World Bank.
