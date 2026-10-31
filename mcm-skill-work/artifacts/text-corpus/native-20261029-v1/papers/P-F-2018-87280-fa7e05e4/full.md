# P-F-2018-87280-fa7e05e4

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000002 | furniture | pages [1] -->
Team Control Number

<!-- b000003 | title | pages [1] -->
87280

<!-- b000004 | prose | pages [1] -->
For office use only

<!-- b000005 | prose | pages [1] -->
T1

<!-- b000006 | prose | pages [1] -->
T2

<!-- b000007 | prose | pages [1] -->
T3

<!-- b000008 | prose | pages [1] -->
For office use only

<!-- b000009 | prose | pages [1] -->
F1

<!-- b000010 | prose | pages [1] -->
F2

<!-- b000011 | prose | pages [1] -->
F3

<!-- b000012 | prose | pages [1] -->
Problem Chosen

<!-- b000013 | prose | pages [1] -->
T4

<!-- b000014 | prose | pages [1] -->
F4

<!-- b000015 | title | pages [1] -->
F

<!-- b000016 | heading | pages [1] -->
2018 ICM

<!-- b000017 | prose | pages [1] -->
How much is your privacy information?

<!-- b000018 | heading | pages [1] -->
Summary Sheet

<!-- b000019 | prose | pages [1] -->
For ensuring the stability of the society, we establish a system of privacy pricing.

<!-- b000020 | prose | pages [1] -->
Task1, according to the personal characteristics and information field, we choose 26

<!-- b000021 | prose | pages [1] -->
indexes to measure privacy price, and divide them into 5 categories according to the degree

<!-- b000022 | prose | pages [1] -->
of correlation.

<!-- b000023 | prose | pages [1] -->
Task2, we price the privacy. The present value method is used to quantify the value of

<!-- b000024 | prose | pages [1] -->
privacy. We use the Analytic Hierarchy Process and Gradient Boosting Decision Tree,

<!-- b000025 | prose | pages [1] -->
through the Python language to calculate the coefficients of the parameters. Then we establish

<!-- b000026 | prose | pages [1] -->
Gauss mixture model to evaluate the information related value. Finally, the simulation of 500

<!-- b000027 | prose | pages [1] -->
people's privacy information is selected to verify the feasibility of the model.

<!-- b000028 | prose | pages [1] -->
Task3, we give the pricing method, introduce the demand elasticity coefficient, and

<!-- b000029 | prose | pages [1] -->
analyze that the privacy information is more flexible. Then the life cycle changes in a long

<!-- b000030 | prose | pages [1] -->
time range are predicted.

<!-- b000031 | prose | pages [1] -->
Task4, with the development of the times, the risk factor will be changed. We add

<!-- b000032 | prose | pages [1] -->
dynamic factors and use Matlab to fit the change function of the risk coefficient.

<!-- b000033 | prose | pages [1] -->
Task5, the value of privacy will increase with age and then stabilize at a certain level. We

<!-- b000034 | prose | pages [1] -->
find out the relationship between PI, IP and PP in the privacy market through a number of

<!-- b000035 | prose | pages [1] -->
literature searches.

<!-- b000036 | prose | pages [1] -->
Task6, we use small world model and dynamic game theory to do simulation and

<!-- b000037 | prose | pages [1] -->
prediction, and find that the privacy of individuals and groups will be largely leaked with the

<!-- b000038 | prose | pages [1] -->
development of market.

<!-- b000039 | prose | pages [1] -->
Task7, the impact of data leakage is long tail. The agency can use the actuarial model to

<!-- b000040 | prose | pages [1] -->
calculate the total amount of compensation to the individual.

<!-- b000041 | prose | pages [1] -->
Task8, we put forward some suggestions to the government on the basis of the model.

<!-- b000042 | prose | pages [1] -->
Finally, we perform a sensitivity test to verify the stability of the model.

<!-- b000043 | furniture | pages [2] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000044 | furniture | pages [2] -->
Team # 87280

<!-- b000045 | furniture | pages [2] -->
Page 1 of 20

<!-- b000046 | heading | pages [2] -->
I Introduction

<!-- b000047 | prose | pages [2] -->
With the development of social informatization, the commercialization of privacy becomes an important issue. Therefore, we need to establish a privacy pricing system to maintain the stable and healthy development of the information sales market. Our tasks are as follows:

<!-- b000048 | prose | pages [2] -->
Task 1: considering the level of risk can pass personal information and data fields classifying model, considering the different characteristics of category information, find the best balance of classification accuracy and simplicity.

<!-- b000049 | prose | pages [2] -->
Task 2: the question to think about the integrity of personal information, uniqueness, scarcity, according to the value of different factors, finally comprehensive assessment of the value of personal information.

<!-- b000050 | prose | pages [2] -->
Task 3: consider the information value, risk value, and the impact of information integrity on the final information pricing.

<!-- b000051 | prose | pages [2] -->
Task 4: consider the assumptions and constraints of the pricing model, judge the relationship between information privacy and human rights, and adjust the model to make it universal in the dynamic environment.

<!-- b000052 | prose | pages [2] -->
Task 5: consider the influence of age factors on the risk-benefit ratio of the population,and consider the similarities and differences between PI and PP and IP.

<!-- b000053 | prose | pages [2] -->
Task 6: make sure each individual data sharing information leakage caused by the network effect, and to consider whether the information network effect will affect the value of the personal information system, and to have the same privacy risks related to personnel, thesale of their personal information should be restricted.

<!-- b000054 | prose | pages [2] -->
Task 7: consider the impact of large-scale PI leakage on data vendors, acquirers, and information value systems. And consider whether the responsibility for data disclosure should be responsible for information disclosure.

<!-- b000055 | prose | pages [2] -->
Task 8: organize the above questions into proposals.

<!-- b000056 | prose | pages [2] -->
II Categorize individuals into sub-groups (Task 1)

<!-- b000057 | heading | pages [2] -->
2.1 A brief introduction to personal privacy pricing

<!-- b000058 | prose | pages [2] -->
Personal privacy is a basic resource, if it is used reasonably, it will help to promote the information social development. Culnan[1] find that, if private used by business are not known to individuals, they will increase their concerns about privacy disclosure. Hagel and others’ [2] research shows, some people tend to pay more attention to privacy, the reason is that they want to get compensation for information leakage. Adjei[3]thinks that, people will be willing to provide personal information to get paid if their personal profits outweigh the risks.

<!-- b000059 | prose | pages [2] -->
Thus, it can be seen that, on the premise of the sound pricing system of personal privacy most people are willing to obtain certain compensation or compensation through the sale of personal privacy. So the appropriate pricing system should be set up.

<!-- b000060 | furniture | pages [3] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000061 | furniture | pages [3] -->
Team # 87280

<!-- b000062 | furniture | pages [3] -->
Page 2 of 20

<!-- b000063 | heading | pages [3] -->
2.1.1 The establishment and evaluation of personal privacy information archives

<!-- b000064 | prose | pages [3] -->
The classification of personal privacy information can help research and excavate the real value contained in information, and the value of information can be further evaluated by studying the correlation degree. Therefore, we chose 26 indicators based on the principle of personal information classification and the actual situation of this subject. It includes personal attributes, financial transactions, social networks, personal assets and health care. This paper classifies personal privacy into two aspects: individual characteristics and information field.

<!-- b000065 | prose | pages [3] -->
The indicators and their classification are shown in Figure 2-1.

<!-- b000066 | prose | pages [3] -->
Figure 2-1: Classification

<!-- b000067 | prose | pages [3] -->
The reasons for the selection of personal privacy information in five aspects are analyzed as follows:

<!-- b000068 | prose | pages [3] -->
Citizenship:They belong to the range of attribute information and are objective  information that can be used to identify specific individuals. Social Contact: Because of the unique social attributes of human beings, it has an  important research value in the field of information, which is generated in the process of life with the other spider web information. Finance: It reflects the situation of individual financial trade and has great value for  information mining. Health/Medical: It has certain significance to the study of social medical treat- ment  service system, and reflects the various situations of the individual body. Personal Assets：It reflects the personal economic status, which is valuable for public  interest, such as national economic analysis, and corporate profits, and it can create economic benefits.

<!-- b000069 | furniture | pages [4] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000070 | furniture | pages [4] -->
Team # 87280

<!-- b000071 | furniture | pages [4] -->
Page 3 of 20

<!-- b000072 | heading | pages [4] -->
III Privacy Cost Model（Task2）

<!-- b000073 | heading | pages [4] -->
3.1 Brief Introduction

<!-- b000074 | prose | pages [4] -->
The cost of privacy is a comprehensive pricing of the value of privacy, and we consider three components.

<!-- b000075 | prose | pages [4] -->
The first is the expected value of income, and we divide five two - level parameters into two categories.

<!-- b000076 | prose | pages [4] -->
Difficult to quantify: As citizenship, we empower each parameter by analytic hierarchy process[4].

<!-- b000077 | prose | pages [4] -->
Quantify: The other 16 parameters can be quantified by using the present value method of income in accounting. Then the coefficient of each parameter is calculated by the machine learning method of the Gradient Boosting Decision Tree(GBDT)[5].

<!-- b000078 | prose | pages [4] -->
The second aspect is the risk value of privacy. Because the value of risk is not easy to measure, we use probability theory to estimate the average deviation degree of expected revenue and get the expected risk reward[6].

<!-- b000079 | prose | pages [4] -->
The third aspect is information related value. The cost of privacy depends not only on the integrity of information, but also on the relevance. For example, the value of only the name should be lower compared with the value of the name attached to the person. We set up a Gauss mixed model to study the relationship between the correlation value and the relevant value of information[7].

<!-- b000080 | heading | pages [4] -->
3.2 Model Building

<!-- b000081 | heading | pages [4] -->
3.2.1 Expected Value of Income

<!-- b000082 | prose | pages [4] -->
The expected value of income is ：

<!-- b000083 | prose | pages [4] -->


<!-- b000084 | prose | pages [4] -->
I 

<!-- b000085 | prose | pages [4] -->
Where：

<!-- b000086 | prose | pages [4] -->
I ：Expected total income value

<!-- b000087 | prose | pages [4] -->
：The value coefficient of the jth parameter, 

<!-- b000088 | prose | pages [4] -->
j

<!-- b000089 | prose | pages [4] -->
26 26 jCj j 1 j 1

<!-- b000090 | prose | pages [4] -->


<!-- b000091 | prose | pages [4] -->
j

<!-- b000092 | prose | pages [4] -->
j j

<!-- b000093 | prose | pages [4] -->
C j ：The expected return value of the jth parameter

<!-- b000094 | prose | pages [4] -->
Step1:The empowerment of civil identity information by AHP

<!-- b000095 | prose | pages [4] -->
The related factors of citizenship quantification are decomposed into objectives, guidelines, programs and so on. Based on this, qualitative and quantitative analysis is carried out. The analytic hierarchy process is like Figure 3–1：

<!-- b000096 | furniture | pages [5] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000097 | furniture | pages [5] -->
Team # 87280

<!-- b000098 | furniture | pages [5] -->
Page 4 of 20

<!-- b000099 | prose | pages [5] -->
Figure 3–1: The Structure of AHP Construct a comparison matrix  By consulting relevant information and combining with the reality of life, we analyze the relationship and importance of 10 indicators in citizenship, and build pair wise comparison matrix.

<!-- b000100 | prose | pages [5] -->
Hierarchical single order  The elements of each column of the judgement matrix are normalized, and the general terms of the elements are:

<!-- b000101 | prose | pages [5] -->
n

<!-- b000102 | prose | pages [5] -->
Aij =Aij Aij

<!-- b000103 | prose | pages [5] -->
i,j=1 Using sum and product method are used to calculate and add the judgement matrix of each column after the normalization. The Wiis obtained.

<!-- b000104 | prose | pages [5] -->
n

<!-- b000105 | prose | pages [5] -->
Wi =Bij

<!-- b000106 | prose | pages [5] -->
i,j=1 The element of the Wi is the sort weight value of the relative importance of the same

<!-- b000107 | prose | pages [5] -->
T ,In the

<!-- b000108 | prose | pages [5] -->
level factor to a certain factor of the upper level factor. For W (W ,W ,...,W )

<!-- b000109 | prose | pages [5] -->
1 2 n process of normalization, the approximate solution of the eigenvector is obtained. Calculating the maximum eigenvalue of the judgment matrix max

<!-- b000110 | prose | pages [5] -->
max

<!-- b000111 | prose | pages [5] -->
(AW)i

<!-- b000112 | prose | pages [5] -->
n 

<!-- b000113 | prose | pages [5] -->
nWi

<!-- b000114 | prose | pages [5] -->
i1

<!-- b000115 | prose | pages [5] -->
After that, we can make sure that the rank ordering is consistent with the consistency check. The so-called consistency check is the allowable range of A.

<!-- b000116 | prose | pages [5] -->
Pairwise comparison matrix consistency test  The consistency index of the pairwise comparison matrix is Consistency Index (C.I.),

<!-- b000117 | prose | pages [5] -->
CI max n

<!-- b000118 | prose | pages [5] -->
n 1 To measure the size of CI, a random consistency index RI is introduced. The method is: construct 500 pairwise comparison matrices randomly, and get the consistency index

<!-- b000119 | prose | pages [5] -->
RI CI1CI2 ...CI500

<!-- b000120 | prose | pages [5] -->
500 The ratio of the consistency index CI. to the same order mean random consistency index R.I. is called the random consistency ratio Consistency Ratio(CR)。

<!-- b000121 | prose | pages [5] -->
CR CI

<!-- b000122 | prose | pages [5] -->
RI

<!-- b000123 | furniture | pages [6] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000124 | furniture | pages [6] -->
Team # 87280

<!-- b000125 | furniture | pages [6] -->
Page 5 of 20

<!-- b000126 | prose | pages [6] -->
The CR<0.1 is obtained through the level analysis software, and the consistency check is passed.

<!-- b000127 | prose | pages [6] -->
Determining the weight factor  The eigenvectors are obtained by calculation,which is the weight of the 10 indexes.

<!-- b000128 | prose | pages [6] -->
j[1,10] =W=(0.056,0.019,0.155,0.025,0.075,0.134,0.053,0.095,0.186,0.20)

<!-- b000129 | prose | pages [6] -->
Step2：Earnings present value method quantifies other information

<!-- b000130 | prose | pages [6] -->
Privacy information seems to be difficult to quantify, but as long as the method is appropriate, we can quantify it to a certain extent. We regard privacy information as an intangible asset, a lot of international ways of quantifying intangible assets. Here we use the present value method[8].

<!-- b000131 | prose | pages [6] -->
The present value method of income is a kind of asset evaluation method to estimate the value of the assets evaluated by estimating the future expected revenue of the assessed assets and turning them into the present value. We determine the value of privacy information by calculating the future revenue of the privacy value. For example, Table 3-1 shows that the future earnings of businesses refer to the profits gained by merchants' knowledge of private information, or the expenditure reduced by government agencies and public organizations.

<!-- b000132 | prose | pages [6] -->
Table 3–1: Information value quantization table

<!-- b000133 | prose | pages [6] -->
Step3：GBDT calculation of expected value coefficient Gradient Boosting Decision Tree is a combination algorithm for machine learning[9],By iterating forward distribution algorithm, continue with the new weights, each round of iteration to get a strong learner and loss function, the next iteration of the goal is to find is a weak learning regression tree model, make the next round to minimize the loss, it is to find a decision tree, let sample loss to become smaller. This is the most significant algorithm in machine learning at present. Figure 3 - 2 shows the principle of its calculation[10].

<!-- b000134 | prose | pages [6] -->
The last formula of the above steps is the information gain after the division of the decision tree is created, and the best splitting point is the position with the highest information gain. In order to find the maximum gain position of the feature, we need to traverse all the characteristics, find the highest gain for every feature, calculate all the features gain, the specific process is like Figure 3 – 3, and then use greedy algorithm to repeat the process.

<!-- b000135 | furniture | pages [7] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000136 | furniture | pages [7] -->
Team # 87280

<!-- b000137 | furniture | pages [7] -->
Page 6 of 20

<!-- b000138 | prose | pages [7] -->
Figure 3–2: GBDT Principle We use Python to program according to the above principles, then we can increase the accuracy and find the most appropriate coefficient by adjusting the steps, iterations, the maximum depth of decision tree, the minimum sample size and so on.Finally, we can get the expected value of each parameter value coefficient:

<!-- b000139 | prose | pages [7] -->
Gj

<!-- b000140 | prose | pages [7] -->


<!-- b000141 | prose | pages [7] -->
H

<!-- b000142 | prose | pages [7] -->
j

<!-- b000143 | heading | pages [7] -->
3.2.4 Venture Value

<!-- b000144 | prose | pages [7] -->
Step1. The standard deviation is calculated.

<!-- b000145 | prose | pages [7] -->
Generally, we can use standard deviation to measure the degree of general response risk, but we have multidimensional index. In order to facilitate comparison with other parameters, it is more ideal to use standard deviation rate.

<!-- b000146 | furniture | pages [8] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000147 | furniture | pages [8] -->
Team # 87280

<!-- b000148 | furniture | pages [8] -->
Page 7 of 20

<!-- b000149 | prose | pages [8] -->
Cof 

<!-- b000150 | prose | pages [8] -->
Where

<!-- b000151 | prose | pages [8] -->
E

<!-- b000152 | prose | pages [8] -->
Cof ：coefficient of variation, E ：expected value, ：Standard deviation

<!-- b000153 | prose | pages [8] -->
Figure 3–3:Information gain traversal Step2. Determine the risk factor.

<!-- b000154 | prose | pages [8] -->
By the analytic hierarchy process described above, the weight of each parameter is considered as a risk factor, indicating the risk of privacy exposure.

<!-- b000155 | prose | pages [8] -->
The risk coefficient is determined by the analytic hierarchy process. After introducing the risk factor, we can calculate the expected rate of return on the risk of privacy:

<!-- b000156 | prose | pages [8] -->
Rj 

<!-- b000157 | prose | pages [8] -->
Where

<!-- b000158 | prose | pages [8] -->
26 26

<!-- b000159 | prose | pages [8] -->
 

<!-- b000160 | prose | pages [8] -->
rjCof j 1 j 1

<!-- b000161 | prose | pages [8] -->
jth parameter Rj：The rate of risk reward for the

<!-- b000162 | prose | pages [8] -->
jth parameter rj：The risk coefficient of the

<!-- b000163 | prose | pages [8] -->
Step3. Calculating the amount of the risk of privacy, that is the value of the risk.

<!-- b000164 | prose | pages [8] -->
Where

<!-- b000165 | prose | pages [8] -->
K ：Value of privacy risk, I j：Expected return value of the jth parameter

<!-- b000166 | furniture | pages [9] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000167 | furniture | pages [9] -->
Team # 87280

<!-- b000168 | heading | pages [9] -->
3.2.4 Information related value

<!-- b000169 | furniture | pages [9] -->
Page 8 of 20

<!-- b000170 | prose | pages [9] -->
For the personal privacy information provided, the value of the data should be further excavated. According to practical experience, the more sensitive information is, the more sensitive rules can be mined, so the value of information is bigger, so we define "information related value" to measure the degree of information correlation. According to the study, the relationship between the two is "S" positive correlation, so the Gauss mixed model is established[11], the Gauss probability density function is used to quantify accurately. The relationship between information related value and information correlation is consistent with the following Gauss function curve trend such as figure Figure 3–4.

<!-- b000171 | prose | pages [9] -->
D()ae

<!-- b000172 | prose | pages [9] -->
()2

<!-- b000173 | prose | pages [9] -->
22

<!-- b000174 | prose | pages [9] -->
The and are the parameters, and the maximum likelihood method can

<!-- b000175 | prose | pages [9] -->
used[12]to estimate the parameters

<!-- b000176 | prose | pages [9] -->
be

<!-- b000177 | prose | pages [9] -->
Figure 3–4:Relation diagram of information related value and correlation

<!-- b000178 | prose | pages [9] -->
The MATLAB program is used to program the correlation value of the information provided by the individual, and the information related value can be calculated. Personal data provided that the two person, the expected value and risk return value is the same, privacy cost pricing is not representative of the two men is the same, it is necessary to study the degree of correlation according to specific content provided by the two data, estimate the value of the relevant information, so as to calculate the final cost of privacy pricing. The information related value is calculated on the basis of the expected value of income, and the concrete steps are as follows:

<!-- b000179 | prose | pages [9] -->
D ae

<!-- b000180 | prose | pages [9] -->
Where：

<!-- b000181 | prose | pages [9] -->
()2

<!-- b000182 | prose | pages [9] -->
22

<!-- b000183 | prose | pages [9] -->
D ：Information related value, I ：Expected value of income, ：Correlation

<!-- b000184 | furniture | pages [10] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000185 | furniture | pages [10] -->
Team # 87280

<!-- b000186 | furniture | pages [10] -->
Page 9 of 20

<!-- b000187 | heading | pages [10] -->
3.2.4 Total value of the cost of privacy

<!-- b000188 | prose | pages [10] -->
Where：

<!-- b000189 | heading | pages [10] -->
3.3 Model solution

<!-- b000190 | heading | pages [10] -->
3.3.1 Data compilation

<!-- b000191 | prose | pages [10] -->
Based on the parameters that are quantified, we have collected data for 1997-2016 years in China's census and consumption.

<!-- b000192 | prose | pages [10] -->
Data source:National Bureau of Statistics of China（http://data.stats.gov.cn/）

<!-- b000193 | heading | pages [10] -->
3.3.2 Data processing

<!-- b000194 | prose | pages [10] -->
After a simple arrangement of the data, further processing of the data is needed. Data cleaning: check whether the data is correct. The outliers are modified by fuzzy matching to fill the missing values. Data standardization: using the Z-score method to standardize the data, the research shows that the method has the highest compatibility in many criteria standardization[13].

<!-- b000195 | heading | pages [10] -->
3.3.3 Calculation coefficient

<!-- b000196 | prose | pages [10] -->
Through the above method, we get the risk coefficient, value coefficient and correlation degree of each dimension through the analytic hierarchy process and GBDT by Python programming. The specific values are Table 3–2.

<!-- b000197 | heading | pages [10] -->
3.3.4 Privacy cost pricing

<!-- b000198 | prose | pages [10] -->
The expected value of earnings is based on the data of China's nearly five years (2011- 2016) and is further calculated by the above coefficients.

<!-- b000199 | prose | pages [10] -->
Table 3–2 Value coefficient and risk factor

<!-- b000200 | furniture | pages [11] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000201 | furniture | pages [11] -->
Team # 87280

<!-- b000202 | furniture | pages [11] -->
Page 10 of 20

<!-- b000203 | prose | pages [11] -->
Table 3-3 Privacy cost price

<!-- b000204 | prose | pages [11] -->
l

<!-- b000205 | prose | pages [11] -->
1 of them represent this privacy information, and 0 are not provided.

<!-- b000206 | prose | pages [11] -->
Then, we simulated the transactions of 500 people's personal privacy data, such as Table 3 – 3, and calculated the privacy cost pricing based on these data, and made a brief analysis.

<!-- b000207 | prose | pages [11] -->
We calculate each individual's expected return value, risk value and relative value, have been found according to the total privacy, personal privacy information provided $600-3000 between the floating in.

<!-- b000208 | prose | pages [11] -->
If a person provides all his privacy information is all 1, then we calculate the total privacy for $5578 (per year).

<!-- b000209 | furniture | pages [12] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000210 | furniture | pages [12] -->
Team # 87280

<!-- b000211 | furniture | pages [12] -->
Page 11 of 20

<!-- b000212 | prose | pages [12] -->
IV Pricing system & Supply and demand relationship （Task3）

<!-- b000213 | prose | pages [12] -->
When we sell personal privacy information as commodities, we are bound to be affected

<!-- b000214 | prose | pages [12] -->
by market fluctuations, including micro supply and demand, macro policy adjustment and

<!-- b000215 | prose | pages [12] -->
economic balance.

<!-- b000216 | heading | pages [12] -->
4.1 Pricing system

<!-- b000217 | prose | pages [12] -->
Individuals can earn certain profits by selling their own privacy information. Businesses or government agencies want to purchase these information, and they will pay personal money, plus some profits besides privacy costs.

<!-- b000218 | prose | pages [12] -->
B CP S Where:

<!-- b000219 | prose | pages [12] -->
B ：Pricing of privacy information CP ：The total price of privacy S ：Personal sale of hidden profits

<!-- b000220 | prose | pages [12] -->
According to the current market profits, in addition to luxury accessories and profiteering, the profit margin of a commodity is roughly 10%-30%. As a person's private seller, how much profit can be made for its own price, but the profit margin can not exceed 30%.

<!-- b000221 | prose | pages [12] -->
The profit margin is 0.3，we can get the following:

<!-- b000222 | heading | pages [12] -->
4.2 Demand elasticity of privacy value

<!-- b000223 | prose | pages [12] -->


<!-- b000224 | prose | pages [12] -->
When privacy information becomes a commodity in the market, it will receive the influence of market fluctuations caused by various factors.This kind of influence will cause the change of demand and price of privacy information. In order to respond to the degree and relationship of change, we introduce the concept of demand price elasticity in economics to explain the demand elasticity of privacy value[14].

<!-- b000225 | prose | pages [12] -->
E Q B

<!-- b000226 | prose | pages [12] -->
Where：

<!-- b000227 | prose | pages [12] -->
d d B Q

<!-- b000228 | prose | pages [12] -->
Ed：Elasticity coefficient of demand，Q ：Quantity demanded，

<!-- b000229 | prose | pages [12] -->
B ：Pricing of privacy information In general, the elastic coefficient is negative, and in order to be simple, we see it as a positive number. It is also divided into five cases of Table4-1.

<!-- b000230 | prose | pages [12] -->
Table 4–1 Elasticity coefficient of demand

<!-- b000231 | furniture | pages [13] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000232 | furniture | pages [13] -->
Team # 87280

<!-- b000233 | furniture | pages [13] -->
Page 12 of 20

<!-- b000234 | prose | pages [13] -->
According to the concept of life cycle, we divide the market of this kind of information into three stages, as shown by Figure 4–1

<!-- b000235 | prose | pages [13] -->
Figure 4–1 Life Cycle Development period: In this period, the relationship between the value of privacy and the amount of demand is more flexible. When the price of privacy rises, most people will be willing to sell, and when the price falls, people will choose to keep their privacy.

<!-- b000236 | prose | pages [13] -->
Mature period: With the deepening of the concept of privacy information becoming a commodity, institutions or organizations have fixed demand for privacy information, and the coefficient of elasticity will be smaller, or even a fixed price.

<!-- b000237 | prose | pages [13] -->
Decline period: When most of the people's privacy is sold for years, the market for privacy information is close to saturation, and there may be a price - free phenomenon.

<!-- b000238 | heading | pages [13] -->
V Assumptions and Dynamic improvement（Task 4）

<!-- b000239 | heading | pages [13] -->
5.1 Assumptions and constraints of personal information pricing model

<!-- b000240 | prose | pages [13] -->
1. It is assumed that people with the same conditions have the same willingness to protect privacy. In the real world, due to the particularity of each person, the degree of importance attached to personal information is different. Its distribution is roughly normal distribution. We assume that each person's attention to their personal information is only related to the individual characteristics and information related fields.

<!-- b000241 | prose | pages [13] -->
2. We don't consider the personal information of people in a special field. Special areas include political areas, military areas, and so on. In some special areas, the disclosure of

<!-- b000242 | furniture | pages [14] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000243 | furniture | pages [14] -->
Team # 87280

<!-- b000244 | furniture | pages [14] -->
Page 13 of 20

<!-- b000245 | prose | pages [14] -->
personal information will result in greater consequences and can’t be quantified according to general standards.

<!-- b000246 | prose | pages [14] -->
3. We only consider the data of model system above. In order to quantify the value of personal data, we only select the characteristic factors that have a great impact on the value of personal information and evaluate the value of personal information according to the characteristic factors.

<!-- b000247 | heading | pages [14] -->
5.2 Whether information privacy should be regarded as human rights

<!-- b000248 | prose | pages [14] -->
In our view, information privacy should not be protected fully as human rights. On the one hand, a part of personal information is closely related to the dignity of the person and reflects the personality factors of the individual. From the phenomenon of the commercialization of personal information, we can find that personal information reflects both personality and property interests[15].Therefore, it is reasonable to protect the property right.

<!-- b000249 | prose | pages [14] -->
To sum up, we think that the personal information should be divided into two aspects, that is, the personality elements of personal information and the property elements of personal information. In the collection and utilization of personal information, we should pay attention to the desensitization of personal information and make use of the information data without damaging the legitimate rights and interests of the information owners.

<!-- b000250 | heading | pages [14] -->
5.3 Dynamic analysis of cost of privacy

<!-- b000251 | heading | pages [14] -->
5.3.1 The change of personal values with time

<!-- b000252 | prose | pages [14] -->
With the development of time, the spread of privacy protection ideas is expanding. People are increasingly familiar with the consequences of privacy disclosure and pay more attention to privacy. Therefore, people's expectations for the return of privacy are getting higher and higher. According to the analysis of the privacy cost model, the risk value is changed due to the change of people's thought.

<!-- b000253 | heading | pages [14] -->
5.3.2 The dynamic analysis of the model

<!-- b000254 | prose | pages [14] -->
With the change of time，he value of risk increases gradually, we add dynamic factors on the basis of the original model. The risk factors of 26 indicators ( rj ) are changed from constants to functions , which are changing by time( t ).

<!-- b000255 | prose | pages [14] -->
Taking the total asset as an example, its trend of change is shown in Figure 5-1. The data is fitted by the MATLAB fitting toolbox. We get a higher fitting degree R-square, which is 0.9779. The fitting effect is very good. So, the function relationship between the risk coefficient ( r18) and the time (t ) of the 18th indexes is as follows:

<!-- b000256 | prose | pages [14] -->
r18 0.6404e(0.07066t 0.6887)

<!-- b000257 | prose | pages [14] -->
By fitting the risk coefficients of the other 25 indexes in the same way, we can calculate the function relation of the risk coefficients of each index. Combined with the formula of risk value:

<!-- b000258 | furniture | pages [15] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000259 | furniture | pages [15] -->
Team # 87280

<!-- b000260 | furniture | pages [15] -->
Page 14 of 20

<!-- b000261 | prose | pages [15] -->
We will add the functional relationship between the dynamic factors ( rj )and the time ( t ) into the upper formula, then it can calculate the change of risk value over time to realize the dynamic evaluation of the model.

<!-- b000262 | prose | pages [15] -->
Figure 5-1: The change trend of total assets

<!-- b000263 | prose | pages [15] -->
VI Generational differences and conceptual comparisons（Task5）

<!-- b000264 | heading | pages [15] -->
6.1 Generational Differences

<!-- b000265 | prose | pages [15] -->
With the different ideas of the times and the growth of age, there are more or less differences

<!-- b000266 | prose | pages [15] -->
in the cognition of the risk and income of privacy information. In this regard, we collect

<!-- b000267 | prose | pages [15] -->
relevant data, and do an analysis.

<!-- b000268 | prose | pages [15] -->
Data sources:

<!-- b000269 | prose | pages [15] -->
(1) Data report on China's Internet consumption ecology in 2015- 2017.

<!-- b000270 | prose | pages [15] -->
http://doc.mbalib.com/view/e720ad8eb4ebac9f83d56ec790a6dd1c.html

<!-- b000271 | prose | pages [15] -->
(2) Census of China's national bureau of statistics.

<!-- b000272 | prose | pages [15] -->
http://www.stats.gov.cn/tjsj/pcsj/

<!-- b000273 | prose | pages [15] -->
(3) Chinese data Yearbook

<!-- b000274 | prose | pages [15] -->
http://data.stats.gov.cn/easyquery.htm?cn=C01

<!-- b000275 | prose | pages [15] -->
We get the consumption data of all ages in personal assets, social networking, financial

<!-- b000276 | prose | pages [15] -->
transactions, health care, and then analyze and regress to get Figure 6 - 1, from 19 to 63 years

<!-- b000277 | prose | pages [15] -->
old, the average growth of people's activities and consumption expenditure and 19 years old.

<!-- b000278 | prose | pages [15] -->
According to the analysis of the second problem, consumption expenditure can be

<!-- b000279 | prose | pages [15] -->
regarded as expected value, so our model needs to make some changes.

<!-- b000280 | prose | pages [15] -->
If pertinence is stronger, or we want to accurately calculate the value of privacy information,

<!-- b000281 | prose | pages [15] -->
we can increase the value of each kind of privacy value according to the growth of every

<!-- b000282 | prose | pages [15] -->
dimension.

<!-- b000283 | furniture | pages [16] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000284 | furniture | pages [16] -->
Team # 87280

<!-- b000285 | furniture | pages [16] -->
Page 15 of 20

<!-- b000286 | prose | pages [16] -->
If only for the overall calculation, and without careful consideration of the increase in the

<!-- b000287 | prose | pages [16] -->
situation, the average growth value can be used.

<!-- b000288 | prose | pages [16] -->
Figure6–1 Generational Differences of consumption level

<!-- b000289 | heading | pages [16] -->
6.2 Compare with PI，PP and IP

<!-- b000290 | prose | pages [16] -->
·Private information[16] ：Non - public information ,Commercialization is not entirely beneficial to individuals, and the sale of personal information will bring a series of immeasurable risks, which may be invisible and long-term.

<!-- b000291 | prose | pages [16] -->
PP：Personal property is divided into tangible and intangible assets [17].  The sale of PP by changing the commodity itself to a certain value is not determined by the relationship with the owner.

<!-- b000292 | prose | pages [16] -->
IP：Rights generated by creative activities based on intelligence[18].  The sale of IP will not cause the risk of disclosure of privacy information. The conceptual relationships of PI, PP, and IP are shown in Figure 6 - 2.

<!-- b000293 | prose | pages [16] -->
Figure 6–2 The conceptual relationships of PI, PP, and IP

<!-- b000294 | prose | pages [16] -->
VII Network effects of data sharing（Task 6）

<!-- b000295 | prose | pages [16] -->
We use Matlab to build a small world model for information leakage, and find that individuals who do not sell privacy are increasingly implicated with the development of privacy trading market. Then through the dynamic game theory, it is predicted that the information of the group will be leaked seriously because of the individual behavior, and if it is properly constrained, the interests of the group can be maximized.

<!-- b000296 | furniture | pages [17] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000297 | furniture | pages [17] -->
Team # 87280

<!-- b000298 | furniture | pages [17] -->
Page 16 of 20

<!-- b000299 | heading | pages [17] -->
7.1 The analysis and hypothesis of the problem.

<!-- b000300 | prose | pages [17] -->
1.Using the "economic man" hypothesis in economics, it is assumed that all the residents in the community are economic man, that is, each step should only consider their own interests.

<!-- b000301 | prose | pages [17] -->
2.Using a modified small-world model to simulate group information leaks, members who sell the information leak personal information about members of his or her neighborhood and have a p chance to reveal information about other members.

<!-- b000302 | prose | pages [17] -->
3.Assuming that any member's sale of personal information is immediately known toother members, this is a reasonable assumption in small groups.

<!-- b000303 | prose | pages [17] -->
4.Suppose each member has the same impact on information disclosure. 5.Suppose that the information breakers leak information to themselves and to the associated members have the same impact.

<!-- b000304 | prose | pages [17] -->
6. Information disclosure does not consider human rights constraints.

<!-- b000305 | heading | pages [17] -->
7.2 Model

<!-- b000306 | heading | pages [17] -->
7.2.1 A small world model of personal privacy disclosure.

<!-- b000307 | prose | pages [17] -->
Establish a small world model to describe the degree of privacy disclosure in a group, In the model, the proportion of people willing to sell personal information for profit is n ，The proportion of people who are unwilling to sell personal information in return for benefits is 1n ，individuals who sell their privacy will lose the privacy of two adjacent individuals in the model, the probability of having n causes loss of privacy of non-adjacent individuals. Use Matlab software to simulate.

<!-- b000308 | prose | pages [17] -->
Figure 7– 1 :Simulation of small world model.

<!-- b000309 | furniture | pages [18] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000310 | furniture | pages [18] -->
Team # 87280

<!-- b000311 | furniture | pages [18] -->
Page 17 of 20

<!-- b000312 | prose | pages [18] -->
Assuming that the group has a population of 40, adjust the range of n and p ,and simulate the loss of privacy.

<!-- b000313 | prose | pages [18] -->
The individuals who are connected by the attachment are individuals who are at risk of privacy disclosure. According to the Matlab simulation analysis, it is obvious that with the increasing of the parameters P and N, the privacy disclosure in the group becomes more and more serious.

<!-- b000314 | heading | pages [18] -->
7.2.2 Analysis of prisoner's dilemma based on dynamic game theory.

<!-- b000315 | prose | pages [18] -->
In a group, some people are willing to sell their own privacy, others think that privacy is more important, we assume that the sale of privacy is an open, in groups, there are four kinds of condition.

<!-- b000316 | prose | pages [18] -->
Table 7-1 The game of interest within the group

<!-- b000317 | prose | pages [18] -->
According to "economic man" hypothesis, each group member only consider their interests and action, is willing to sell a member of the privacy will sell their privacy, under this precondition, even if other members do not want to sell privacy, their privacy will be violated, as a result, even if part of the members are reluctant to sell privacy for interests, in seeking to stop the cases, will sell the privacy in order to get more benefits.

<!-- b000318 | prose | pages [18] -->
Based on the above simulation analysis, we get the conclusion. In the outside world without intervention, a group with the same privacy risks into sub-game refining Nash equilibrium, cannot get benefit optimization, in order to jump out of the prisoner's dilemma, to maximize the interests of groups and groups to limit the privacy of personal selling behavior is necessary.

<!-- b000319 | prose | pages [18] -->
VIII Impact of data disclosure on the value of privacy(Task 7)

<!-- b000320 | prose | pages [18] -->
When information security issues arise in the organizations that purchase personal privacy information, there will be a large amount of privacy information leakage. If the privacy is stolen by criminals, it can pose a threat to personal safety and social stability.

<!-- b000321 | heading | pages [18] -->
8.1 The impact of data leakage on the value of privacy

<!-- b000322 | prose | pages [18] -->
We discuss the impact of data leakage based on the components of privacy value. 1. When a large number of data is leaked, personal privacy information is improperly distributed in the market, then the bussiniess’ willingness to purchase personal information will be reduced, and the expected return value of the individual will also decline.

<!-- b000323 | prose | pages [18] -->
2. Because of people's awareness of the risk of personal information leakage is increased, and their willingness to sell information will decline.

<!-- b000324 | prose | pages [18] -->
3. The relevant value will decrease with the decrease of expected return value.

<!-- b000325 | furniture | pages [19] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000326 | furniture | pages [19] -->
Team # 87280

<!-- b000327 | furniture | pages [19] -->
Page 18 of 20

<!-- b000328 | prose | pages [19] -->
In general, as Figure 8-1 shows, data leakage can cause the decline of personal privacy value, and the willingness of people to sell their privacy value will also decline, which will lead to the economic crisis of privacy trading market.

<!-- b000329 | prose | pages [19] -->
Figure 8–1：The impact of data leakage on the value of privacy

<!-- b000330 | heading | pages [19] -->
8.2 Time effect of data leakage

<!-- b000331 | prose | pages [19] -->
As time goes on, the impact of data leaks can change, too. We consider the influence of two trends, one is the long tail effect [19], the other is the bullwhip effect[20]. As shown in Figure 8-2.

<!-- b000332 | prose | pages [19] -->
Figure 8–2: Long Tail and Bullwhip Effect

<!-- b000333 | prose | pages [19] -->
Long tail effect ：If the public opinion of the leak is guided by the demand side of  personal information, such as intermediary companies and government agencies, then there will be a long tail effect. Bullwhip effect：If the message of the leaked data is spread rapidly across the network,  the overall public opinion is not controlled by any organization, then there will be the bullwhip effect.

<!-- b000334 | prose | pages [19] -->
Figure 8–3 : The impact of data leakage changes over time

<!-- b000335 | furniture | pages [20] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000336 | furniture | pages [20] -->
Team # 87280

<!-- b000337 | furniture | pages [20] -->
Page 19 of 20

<!-- b000338 | prose | pages [20] -->
Although these two cases will appear, the bullwhip effect can be controlled by the other.With impact events increasing, effects of data leakage has become smaller. Therefore, the overall impact of data leakage, such as Figure 8-3. It will rise first, then drop, and there will be fluctuations in it.

<!-- b000339 | heading | pages [20] -->
8.3 Agency compensation model

<!-- b000340 | prose | pages [20] -->
When the data leakage occurs, the agency needs to compensate everyone for a certain loss. In addition to the value of the data itself, the agency also needs to compensate for other losses caused by data lost. We use the actuarial model of the insurance[21] industry to calculate the amount of compensation. The establishment method of actuarial model is generally parametric modeling, and its process is shown in Figure 8-4.

<!-- b000341 | prose | pages [20] -->
Figure 8–4 : Flow chart of parameter construction of actuarial model Finally, the amount of compensation we have calculated is as follows:

<!-- b000342 | prose | pages [20] -->
U I  Where：

<!-- b000343 | prose | pages [20] -->
U :The amount of the final compensation to the individual

<!-- b000344 | prose | pages [20] -->
I :The value of the information itself ,and it is also the original expected value. ：Other losses should be compensated for by the actuarial model.

<!-- b000345 | heading | pages [20] -->
IX Sensitivity analysis

<!-- b000346 | prose | pages [20] -->
In order to test the stability of the model, we consider that different people pay different attention to personal privacy information and have different attitudes and tolerance to risk disclosure. Therefore, the weight assignment of value coefficient and risk coefficient is different from person to person. In order to test the universality of the coefficients determined by the gradient lifting tree and the analytic hierarchy process, we have designed a questionnaire on personal privacy information attitude (see Appendix II). In this paper, 50 people of different ages were selected as the respondents, we investigated their weighting of 26 indicators and obtained new value coefficients and risk factors. Through the analysis of the data, 3 groups of invalid data were excluded, and 47 new value coefficients and risk factors were obtained. We put these coefficients into the model and repriced the privacy costs of the 500 people generated by the simulation. The new pricing situation is shown in Figure 9-1.( Because of the large amount of data, only partial data is displayed.)

<!-- b000347 | furniture | pages [21] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000348 | furniture | pages [21] -->
Team # 87280

<!-- b000349 | furniture | pages [21] -->
Page 20 of 20

<!-- b000350 | prose | pages [21] -->
Figure 9-1: Local diagram of new pricing results The average value of the new pricing (Average) is not significantly different from the original model (Original). We use SPSS software to carry out the independent-samples T-test on these two sets of data, and get the test results such as Figure 9- 2.

<!-- b000351 | prose | pages [21] -->
Figure 9-2: The result of independent-samples T-test

<!-- b000352 | prose | pages [21] -->
It can be seen from the test results that, in the test of homogeneity of variance, p=0.775>0.05, we can accept the original hypothesis, it can be considered that the variance is equal, the independent-samples T-test should be used.

<!-- b000353 | heading | pages [21] -->
The results of independent-samples T-test shows, p=0.910<0.05, we can’t accept the original

<!-- b000354 | prose | pages [21] -->
hypothesis. Therefore, there is no significant difference between the above two sets of data, so the stability of the model is good.

<!-- b000355 | heading | pages [21] -->
X Analysis of the advantages and weaknesses of the model

<!-- b000356 | prose | pages [21] -->
Advantages：  1. We consider many basic and derived parameters and establish a personal information pricing model that reflects the impact of all aspects. 2. The impact of the emergency pricing model is considered. 3. Model is a simple but flexible and reliable. When a certain factor changes greatly, the model can be universally adjusted by simple adjustment. 4. The method used in the pricing model is novel, R-squared is high, and the error rate is small.

<!-- b000357 | prose | pages [21] -->
Weaknesses:  1. Some parameters need to be adjusted according to the actual situation. 2. It is impossible for all people can accept the commercialization of privacy. 3. The areas involved are not exhaustive.

<!-- b000358 | furniture | pages [22] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000359 | heading | pages [22] -->
Privacy Pricing Policy Recommendations

<!-- b000360 | prose | pages [22] -->
Dear decision maker: In the information society, the analysis and processing of information has brought great social and economic value. Information becomes more and more important. At present, the personal information of citizens has been circulated in the market, but personal information is an important part of information cluster. The laws, policies and pricing strategies related to the commercialization of personal information still exist in a large gap in related fields, resulting in huge risks. In order to standardize the market order of information, reduce the risk of citizen information leakage brought by information commercialization. Through the comprehensive consideration of various factors, we have set up a pricing system for the commercialization of personal information. Our team considers the value of information from both the information owner and the information user. We obtain cost measurement through information, assess the risk and value of information sharing, and predict the value of information. Furthermore, we consider the influence of dynamic factors and sudden events on information value and establish the information commercialization pricing system.

<!-- b000361 | prose | pages [22] -->
Privacy information pricing

<!-- b000362 | prose | pages [22] -->
We consider the following factors to price the model. prospective earnings ：Consider privacy as an intangible asset, quantifying the value of personal information through the quantitative method of intangible assets. It can also be understood that when individuals sell their privacy as a commodity, they can make a big profit for their privacy buyers.

<!-- b000363 | prose | pages [22] -->
Risk assessment value：When people sell their privacy, the privacy they sell brings certain risks. As compensation, the information buyer should compensate the seller for risk. Because each person's information and information value is different, the risk value is different.

<!-- b000364 | prose | pages [22] -->
Relevance value：In fact, the privacy value of the system is often higher than that of individual privacy prices. Other things being equal,if privacy is a system, the value of privacy is higher.

<!-- b000365 | prose | pages [22] -->
Other factors：In addition to the above three factors, we also consider other factors to dynamically compensate the model.

<!-- b000366 | prose | pages [22] -->
Generational differences：Age differences lead to different ideas. This leads to greater cognitive differences in the value of privacy.

<!-- b000367 | prose | pages [22] -->
Age difference ：The younger age differences can also be reflected in the concept, and the information value of the individual will change as the age changes. Individuals' perceptions of risk and benefits also change with age.

<!-- b000368 | prose | pages [22] -->
Unpredictable risk：Some risks are latent and cannot be predicted in today's

<!-- b000369 | furniture | pages [23] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000370 | prose | pages [23] -->
circumstances.

<!-- b000371 | prose | pages [23] -->
Effect of pricing

<!-- b000372 | prose | pages [23] -->
Applicable fields：We make pricing proposals for PI in three areas

<!-- b000373 | prose | pages [23] -->
social media financial transactions health/medical records

<!-- b000374 | heading | pages [23] -->
Model effect：

<!-- b000375 | prose | pages [23] -->
According to the online survey and simulation, the same crowd divided on the value of information cognition has a little different, but the overall value of the float is less than $10, the pricing model of basic can meet the expected value of people.

<!-- b000376 | prose | pages [23] -->
And more than 50% of people are willing to sell their privacy information at this price, but only if the information can be reasonably used, and it will not pose a threat to personal safety.

<!-- b000377 | prose | pages [23] -->
National macro-control

<!-- b000378 | prose | pages [23] -->
In order to avoid unexpected privacy information market conditions, lead to data leakage or other social instability happens, the government must want to undertake certain macroeconomic regulation and control, limit privacy price within a certain range.

<!-- b000379 | prose | pages [23] -->
Promulgates the laws and regulations of economic regulation and regulation: establish a perfect system to adapt to the development of market economy, and calm the relationship between supply and demand.

<!-- b000380 | prose | pages [23] -->
Disciplinary punishment for illegal behaviors: avoid using other people's privacy information for illegal activities.

<!-- b000381 | prose | pages [23] -->
Restricted trading of special information: information of certain special personnel, groups, such as government circumstances.

<!-- b000382 | prose | pages [23] -->
Accident prevention

<!-- b000383 | prose | pages [23] -->
should be restricted according to

<!-- b000384 | prose | pages [23] -->
If something unexpected happens, for example, a large amount of privacy is leaking, we need to develop a complete solution.

<!-- b000385 | prose | pages [23] -->
Agency compensation: on the basis of personal information value, make certain increment compensation.

<!-- b000386 | prose | pages [23] -->
Guide public opinion: the government and media guide public opinion without infringing on individual rights and interests, and prevent riots or panic, causing social instability.

<!-- b000387 | prose | pages [23] -->
Control the market: try to avoid leaking data into the market to prevent economic recession or imbalance.

<!-- b000388 | prose | pages [23] -->
Deal with it as soon as possible: timely and properly handle the unexpected situation.

<!-- b000389 | prose | pages [23] -->
Sincerely

<!-- b000390 | prose | pages [23] -->
Team 87280

<!-- b000391 | furniture | pages [24] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000392 | heading | pages [24] -->
References:

<!-- b000393 | references | pages [24] -->
[1] Culnan M J.’How did they get my name’:an exploratory investigation of consumer

<!-- b000394 | references | pages [24] -->
attitudes toward secondary information use[J].MIS Quarterly,1993,17(3):341-363.

<!-- b000395 | references | pages [24] -->
[2] Hagel J III,Rayport J F. The coming battle for customer information[J]. Harvard Business

<!-- b000396 | references | pages [24] -->
Review,1997,75(1):53-65

<!-- b000397 | references | pages [24] -->
[3] Adjei J K．Monetization of personal identity information: technological and regulatory

<!-- b000398 | references | pages [24] -->
framework[C].India: International Conference on Information Science&Security,2015

<!-- b000399 | references | pages [24] -->
[4] Al-Harbi A S. Application of the AHP in project management[J]. International Journal of

<!-- b000400 | references | pages [24] -->
Project Management, 2001, 19(1):19-27.

<!-- b000401 | references | pages [24] -->
[5] Dai yixin, sun rongling. Realization and quantification of intangible asset value [J].

<!-- b000402 | references | pages [24] -->
Chinese soft science,2000(07):74-77.

<!-- b000403 | references | pages [24] -->
[6] Zhu guo. Application of EXCEL in financial management -- calculation of investment

<!-- b000404 | references | pages [24] -->
risk value [J]. Journal of chifeng college (natural edition), 2009, 25(4):130-131.

<!-- b000405 | references | pages [24] -->
[7] Sun Guangling, Tang Xianglong. Hierarchical semi supervised learning algorithm based

<!-- b000406 | references | pages [24] -->
on Gauss mixture model [J]. Computer research and development,2004(01):159-164.

<!-- b000407 | references | pages [24] -->
[8] Li Hongxun. Asset evaluation and management: China Forestry Publishing House, 2000

<!-- b000408 | references | pages [24] -->
[9] Friedman J H. Stochastic Gradient Boosting[J]. Computational Statistics & Data Analysis,

<!-- b000409 | references | pages [24] -->
2002, 38(4):367-378.

<!-- b000410 | references | pages [24] -->
[10] Introduction to Boosted Trees, Tianqi Chen, 2014

<!-- b000411 | references | pages [24] -->
From http://homes.cs.washington.edu/~tqchen/pdf/BoostedTree.pdf]

<!-- b000412 | references | pages [24] -->
[11] Sun Guangling, Tang Xianglong. Research and development of semi supervised learning

<!-- b000413 | references | pages [24] -->
algorithm [J]. layered computer based on Gauss mixture model,2004(01):159-164

<!-- b000414 | references | pages [24] -->
[12]

<!-- b000415 | references | pages [24] -->
Zhang Rongquan, Du Yuming, Yang Jianyu. A LFM signal maximum likelihood

<!-- b000416 | references | pages [24] -->
estimation model and a fast algorithm for parameter estimation [J]. Journal of radio wave

<!-- b000417 | references | pages [24] -->
science,2005 Journal of radio wave science (05):101-105.

<!-- b000418 | references | pages [24] -->
[13] Xu Yunhui, Li Zhongfei. Dynamic portfolio selection based on income sequence related

<!-- b000419 | references | pages [24] -->
dynamic mean variance model [J]. Theory and practice of system engineering, 2008(08): 125-

<!-- b000420 | references | pages [24] -->
[14]Diego S. Price elasticity of demand[J]. Betascript Publishing, 2009, 3(4):1717-1718.

<!-- b000421 | references | pages [24] -->
[15] PengYun. Research on property property of personal information from the angle of

<!-- b000422 | references | pages [24] -->
Anglo American Property Law. Legal system and society:ten-day periodical, 2011(11): 249

<!-- b000423 | references | pages [24] -->
[16] A. Beimel and Y.Stahl, Robust information-theoretic private information retrieval, in

<!-- b000424 | references | pages [24] -->
Proceedings of the 3rd International Conference on Security in Communication Networks

<!-- b000425 | references | pages [24] -->
(SCN'02), pp. 326–341, 2003. Cite is from DGH 2012, op. cit.

<!-- b000426 | references | pages [24] -->
[17] Personal property". Sir Robert Harry Inglis Palgrave. Dictionary of political economy,

<!-- b000427 | references | pages [24] -->
Volume 3. 1908. p. 96

<!-- b000428 | references | pages [24] -->
[18] Personal property". Sir Robert Harry Inglis Palgrave. Dictionary of political economy,

<!-- b000429 | references | pages [24] -->
Volume 3. 1908. p. 96

<!-- b000430 | references | pages [24] -->
[19] Tang Haijun. Theory of long tail theory of economics[J]. Modern management science.

<!-- b000431 | references | pages [24] -->
2009(1):62-64.

<!-- b000432 | references | pages [24] -->
[20] Tang Haijun. Theory of long tail theory of economics[J]. Modern management science.

<!-- b000433 | references | pages [24] -->
2009(1):62-64.

<!-- b000434 | references | pages [24] -->
[21] Xiao Yan. Actuarial model [M]. Renmin University of China press, 2013.

<!-- b000435 | furniture | pages [25] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000436 | heading | pages [25] -->
Appendix I

<!-- b000437 | prose | pages [25] -->
Python

<!-- b000438 | prose | pages [25] -->
#####################################GBDT################################

<!-- b000439 | prose | pages [25] -->
import numpy as np

<!-- b000440 | prose | pages [25] -->
from sklearn.ensemble import GradientBoostingRegressor

<!-- b000441 | prose | pages [25] -->
gbdt=GradientBoostingRegressor(loss='ls', learning_rate=0.1,

<!-- b000442 | prose | pages [25] -->
n_estimators=100,

<!-- b000443 | prose | pages [25] -->
subsample=1, min samples split=2, min samples leaf=1, max depth=3 , init=None, random_state=None, max_features=None, alpha=0.9, verbose=0,

<!-- b000444 | prose | pages [25] -->
max_leaf_nodes=None, warm_start=False

<!-- b000445 | prose | pages [25] -->
)

<!-- b000446 | prose | pages [25] -->
train_feat=np.genfromtxt("f_train.txt",dtype=np.float32)

<!-- b000447 | prose | pages [25] -->
train_id=np.genfromtxt("f.txt",dtype=np.float32)

<!-- b000448 | prose | pages [25] -->
test_feat=np.genfromtxt("f_test.txt",dtype=np.float32)

<!-- b000449 | prose | pages [25] -->
test_id=np.genfromtxt("ff.txt",dtype=np.float32)

<!-- b000450 | prose | pages [25] -->
gbdt.fit(train_feat,train_id)

<!-- b000451 | prose | pages [25] -->
pred=gbdt.predict(test_feat)

<!-- b000452 | prose | pages [25] -->
print(gbdt.feature_importances_)

<!-- b000453 | prose | pages [25] -->
total_err=0

<!-- b000454 | prose | pages [25] -->
for i in range(test_feat.shape[0]):

<!-- b000455 | prose | pages [25] -->
print(pred[i],test_id[i])

<!-- b000456 | prose | pages [25] -->
err=(pred[i]-test_id[i])/test_id[i]

<!-- b000457 | prose | pages [25] -->
total_err+=err*err

<!-- b000458 | prose | pages [25] -->
print(total_err/pred.shape[0])

<!-- b000459 | prose | pages [25] -->
##Result##

<!-- b000460 | prose | pages [25] -->
''' ====================== RESTART: F:\math\gbdt\usegbdt.py

<!-- b000461 | prose | pages [25] -->
======================

<!-- b000462 | prose | pages [25] -->
[0.05769512 0.00610115 0.05629678 0.01203783 0.02682956 0.08157958

<!-- b000463 | prose | pages [25] -->
0.03342411 0.09468546 0.03692312 0.05884569 0.03874673 0.06441484

<!-- b000464 | prose | pages [25] -->
0.05666908 0.01886848 0.04130826 0.08557419]

<!-- b000465 | prose | pages [25] -->
2.0430143820015707 2.04364

<!-- b000466 | prose | pages [25] -->
1.7260317333863573 1.72623

<!-- b000467 | prose | pages [25] -->
1.4539094183773056 1.45404

<!-- b000468 | prose | pages [25] -->
1.187036709759271 1.18706

<!-- b000469 | prose | pages [25] -->
0.936417771272397 0.93639

<!-- b000470 | prose | pages [25] -->
2.324334324614137e-08

<!-- b000471 | prose | pages [25] -->
'''

<!-- b000472 | furniture | pages [26] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000473 | prose | pages [26] -->
Matlab

<!-- b000474 | prose | pages [26] -->
%%%%%%%%%%%%%%%%%%%%%%%%Small world model%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

<!-- b000475 | prose | pages [26] -->
function matrix = SW()

<!-- b000476 | prose | pages [26] -->
tic

<!-- b000477 | prose | pages [26] -->
a=1:1:40; c=randperm(numel(a));

<!-- b000478 | prose | pages [26] -->
N=a(c(1:20));m=2;

<!-- b000479 | prose | pages [26] -->
p=0.1;

<!-- b000480 | prose | pages [26] -->
matrix=sparse([],[],[],40,40,0);

<!-- b000481 | prose | pages [26] -->
for i=m+1:N(1:20)-m

<!-- b000482 | prose | pages [26] -->
for j=i-m:i+m

<!-- b000483 | prose | pages [26] -->
matrix(i,j)=1;

<!-- b000484 | prose | pages [26] -->
end

<!-- b000485 | prose | pages [26] -->
end for i=1:m

<!-- b000486 | prose | pages [26] -->
for j=1:i+m

<!-- b000487 | prose | pages [26] -->
matrix(i,j)=1;

<!-- b000488 | prose | pages [26] -->
end

<!-- b000489 | prose | pages [26] -->
end for i=N(1:20)-m+1:N(1:20)

<!-- b000490 | prose | pages [26] -->
for j=i-m:N(1:10)

<!-- b000491 | prose | pages [26] -->
matrix(i,j)=1;

<!-- b000492 | prose | pages [26] -->
end

<!-- b000493 | prose | pages [26] -->
end for i=1:m

<!-- b000494 | prose | pages [26] -->
for j=N(1:20)-m+i:N(1:20)

<!-- b000495 | prose | pages [26] -->
matrix(i,j)=1;matrix(j,i)=1;

<!-- b000496 | prose | pages [26] -->
end

<!-- b000497 | prose | pages [26] -->
end for i=1:N(1:20)-m-1

<!-- b000498 | prose | pages [26] -->
for j=i+1:i+m

<!-- b000499 | prose | pages [26] -->
r=rand(1);

<!-- b000500 | prose | pages [26] -->
if r<=p

<!-- b000501 | prose | pages [26] -->
unconect=find(matrix(i,:)==0);

<!-- b000502 | prose | pages [26] -->
M=length(unconect);

<!-- b000503 | prose | pages [26] -->
r1=ceil(M*rand(1));

<!-- b000504 | prose | pages [26] -->
matrix(i,unconect(r1))=1;

<!-- b000505 | prose | pages [26] -->
matrix(unconect(r1),i)=1;

<!-- b000506 | prose | pages [26] -->
end

<!-- b000507 | prose | pages [26] -->
end

<!-- b000508 | prose | pages [26] -->
end

<!-- b000509 | prose | pages [26] -->
for i=N(1:10)-m+1:N(1:10)-1

<!-- b000510 | furniture | pages [27] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000511 | prose | pages [27] -->
for j=[i+1:N(1:20) 1:i- N(1:20)+m]

<!-- b000512 | prose | pages [27] -->
r=rand(1);

<!-- b000513 | prose | pages [27] -->
if r<=p

<!-- b000514 | prose | pages [27] -->
unconect=find(matrix(i,:)==0);

<!-- b000515 | prose | pages [27] -->
r1=ceil(length(unconect)*rand(1));

<!-- b000516 | prose | pages [27] -->
matrix(i,unconect(r1))=1;

<!-- b000517 | prose | pages [27] -->
matrix(unconect(r1),i)=1;

<!-- b000518 | prose | pages [27] -->
end

<!-- b000519 | prose | pages [27] -->
end

<!-- b000520 | prose | pages [27] -->
end

<!-- b000521 | prose | pages [27] -->
for i=N(1:20)

<!-- b000522 | prose | pages [27] -->
for j=1:m

<!-- b000523 | prose | pages [27] -->
r=rand(1);

<!-- b000524 | prose | pages [27] -->
if r<=p

<!-- b000525 | prose | pages [27] -->
unconect=find(matrix(i,:)==0);

<!-- b000526 | prose | pages [27] -->
r1=ceil(length(unconect)*rand(1));

<!-- b000527 | prose | pages [27] -->
matrix(i,unconect(r1))=1;

<!-- b000528 | prose | pages [27] -->
matrix(unconect(r1),i)=1;

<!-- b000529 | prose | pages [27] -->
matrix(i,j)=0;matrix(j,i)=0;

<!-- b000530 | prose | pages [27] -->
end

<!-- b000531 | prose | pages [27] -->
end

<!-- b000532 | prose | pages [27] -->
end

<!-- b000533 | prose | pages [27] -->
for m=1:N(1:20) matrix(m,m)=0;

<!-- b000534 | prose | pages [27] -->
end

<!-- b000535 | prose | pages [27] -->
toc

<!-- b000536 | prose | pages [27] -->
end

<!-- b000537 | prose | pages [27] -->
function tu_plot(rel,control)

<!-- b000538 | prose | pages [27] -->
r_size=size(rel);

<!-- b000539 | prose | pages [27] -->
if nargin<2

<!-- b000540 | prose | pages [27] -->
control=0;

<!-- b000541 | prose | pages [27] -->
end

<!-- b000542 | prose | pages [27] -->
if r_size(1)~=r_size(2)

<!-- b000543 | prose | pages [27] -->
disp('Wrong Input! The input must be a square matrix!');

<!-- b000544 | prose | pages [27] -->
return;

<!-- b000545 | prose | pages [27] -->
end

<!-- b000546 | prose | pages [27] -->
len=r_size(1);

<!-- b000547 | prose | pages [27] -->
rho=50;

<!-- b000548 | prose | pages [27] -->
r=2/1.05^len;

<!-- b000549 | prose | pages [27] -->
theta=0:(2*pi/len):2*pi*(1-1/len);

<!-- b000550 | prose | pages [27] -->
[pointx,pointy]=pol2cart(theta',rho);

<!-- b000551 | prose | pages [27] -->
theta=0:pi/36:2*pi;

<!-- b000552 | furniture | pages [28] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000553 | prose | pages [28] -->
[tempx,tempy]=pol2cart(theta',r);

<!-- b000554 | prose | pages [28] -->
point=[pointx,pointy];

<!-- b000555 | prose | pages [28] -->
hold on

<!-- b000556 | prose | pages [28] -->
for i=1:len

<!-- b000557 | prose | pages [28] -->
temp=[tempx,tempy]+[point(i,1)*ones(length(tempx),1),point(i,2)*ones(lengt

<!-- b000558 | prose | pages [28] -->
h(tempx),1)];

<!-- b000559 | prose | pages [28] -->
plot(temp(:,1),temp(:,2),'r'); text(point(i,1)-0.3,point(i,2),num2str(i));

<!-- b000560 | prose | pages [28] -->
end

<!-- b000561 | prose | pages [28] -->
for i=1:len

<!-- b000562 | prose | pages [28] -->
for j=1:len

<!-- b000563 | prose | pages [28] -->
if rel(i,j)

<!-- b000564 | prose | pages [28] -->
link_plot(point(i,:),point(j,:),r,control);

<!-- b000565 | prose | pages [28] -->
end

<!-- b000566 | prose | pages [28] -->
end

<!-- b000567 | prose | pages [28] -->
end

<!-- b000568 | prose | pages [28] -->
set(gca,'XLim',[-rho-r,rho+r],'YLim',[-rho-r,rho+r]);

<!-- b000569 | prose | pages [28] -->
axis off

<!-- b000570 | prose | pages [28] -->
function link_plot(point1,point2,r,control)

<!-- b000571 | prose | pages [28] -->
temp=point2-point1;

<!-- b000572 | prose | pages [28] -->
if (~temp(1))&&(~temp(2))

<!-- b000573 | prose | pages [28] -->
return;

<!-- b000574 | prose | pages [28] -->
end

<!-- b000575 | prose | pages [28] -->
theta=cart2pol(temp(1),temp(2));

<!-- b000576 | prose | pages [28] -->
[point1_x,point1_y]=pol2cart(theta,r);

<!-- b000577 | prose | pages [28] -->
point_1=[point1_x,point1_y]+point1;

<!-- b000578 | prose | pages [28] -->
[point2_x,point2_y]=pol2cart(theta+(2*(theta<pi)-1)*pi,r);

<!-- b000579 | prose | pages [28] -->
point_2=[point2_x,point2_y]+point2;

<!-- b000580 | prose | pages [28] -->
if control

<!-- b000581 | prose | pages [28] -->
arrow(point_1,point_2);

<!-- b000582 | prose | pages [28] -->
else

<!-- b000583 | prose | pages [28] -->
plot([point 1(1),point 2(1)],[point 1(2),point 2(2)]); end

<!-- b000584 | prose | pages [28] -->
%%%%%%%%%%%%%%%%%%%%%%%%%%%% Risk factor %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

<!-- b000585 | prose | pages [28] -->
x=0:60;

<!-- b000586 | prose | pages [28] -->
y=0.71*log(x)/log(60)

<!-- b000587 | prose | pages [28] -->
figure('color',[1 1 1]);

<!-- b000588 | prose | pages [28] -->
plot(x,y)

<!-- b000589 | prose | pages [28] -->
hold on;

<!-- b000590 | furniture | pages [29] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000591 | prose | pages [29] -->
plot([28,28],[0,0.581],'g--')

<!-- b000592 | prose | pages [29] -->
hold on;

<!-- b000593 | prose | pages [29] -->
plot([0,28],[0.581,0.581],'g--')

<!-- b000594 | prose | pages [29] -->
xlabel('Year')

<!-- b000595 | prose | pages [29] -->
ylabel('Risk factor')

<!-- b000596 | prose | pages [29] -->
hold on;

<!-- b000597 | prose | pages [29] -->
gl=[0:3:60] Y=interp1(x,y,gl);

<!-- b000598 | prose | pages [29] -->
dian=[0

<!-- b000599 | prose | pages [29] -->
0.182,0.356,0.351,0.420,0.437,0.501,0.535,0.571,0.581,0.599,0.601,0.630,0. 656,0.640,0.668,0.665,0.651,0.683,0.710,0.712];

<!-- b000600 | prose | pages [29] -->
scatter(gl,dian,'k')

<!-- b000601 | prose | pages [29] -->
%%%%%%%%%%%%%%%%%%%%%%%%%%%% The correlation %%%%%%%%%%%%%%%%%%%%%%%%%%%

<!-- b000602 | prose | pages [29] -->
clc,clear

<!-- b000603 | prose | pages [29] -->
a=xlsread('data.xlsx','Sheet1','A4:Z504'); %The data is in Appendix II

<!-- b000604 | prose | pages [29] -->
name=xlsread('data.xlsx','Sheet1','A4:A504');

<!-- b000605 | prose | pages [29] -->
CitizenshipNumber=xlsread('data.xlsx','Sheet1','C4:C504');

<!-- b000606 | prose | pages [29] -->
Address=xlsread('data.xlsx','Sheet1','F4:F504');

<!-- b000607 | prose | pages [29] -->
ContactWay=xlsread('data.xlsx','Sheet1','G4:G504');

<!-- b000608 | prose | pages [29] -->
if(name==0&Citizenship==0&Number==0&Address==0&ContactWay==0)

<!-- b000609 | prose | pages [29] -->
Y=0; else

<!-- b000610 | prose | pages [29] -->
gl=xlsread('data.xlsx','Sheet1','AA4:AA504');

<!-- b000611 | prose | pages [29] -->
x=0:0.00001:5;

<!-- b000612 | prose | pages [29] -->
y=300*gaussmf(x,[1.8 5]); figure('color',[1 1 1]);

<!-- b000613 | prose | pages [29] -->
plot(x,y)

<!-- b000614 | prose | pages [29] -->
Y=interp1(x,y,gl)

<!-- b000615 | prose | pages [29] -->
end xlabel('Information correlation')

<!-- b000616 | prose | pages [29] -->
ylabel('Price(£¤)')

<!-- b000617 | furniture | pages [30] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000618 | heading | pages [30] -->
Appendix II

<!-- b000619 | prose | pages [30] -->
An Investigation Into Attitudes To Personal Privacy.

<!-- b000620 | heading | pages [30] -->
1. Your gender：

<!-- b000621 | prose | pages [30] -->
A. Male B. Female

<!-- b000622 | heading | pages [30] -->
2. Your age：

<!-- b000623 | prose | pages [30] -->
A．≤11years B.12 years—18 years C.19 years—35 years D. 36 years—65 years E.≥65 years

<!-- b000624 | heading | pages [30] -->
3. Your career：

<!-- b000625 | prose | pages [30] -->
A. Government officials B Technical personnel C. Junior officers D. Business services E. Business and service personnel. F. Production, transportation equipment operators and related personnel. G.solder

<!-- b000626 | heading | pages [30] -->
4. You attach great importance to personal privacy information.：

<!-- b000627 | prose | pages [30] -->
A. attach great importance to B. attach importance to C. general emphasis D. do not take the E. it doesn't matter

<!-- b000628 | heading | pages [30] -->
5. Please fill in the following table with the following information you think:

<!-- b000629 | prose | pages [30] -->
For example, if you think the home address information is three times as important as the name information, please fill in the "3" in the corresponding form; If you think the importance of gender information is 1/8 times that of interest and hobbies, please fill in "1/8" in the corresponding form.

<!-- b000630 | furniture | pages [31] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000631 | prose | pages [31] -->
xl x2 x3 x4 xS x6 x7 x8 x9 xlO I xll x12 x13 x14 I x15 x16 xl 71 x18 I x19 I x20 I x21 I x22 x23 x24 x25 x26 N皿阳CxlJ I 1 Gender(x2) C, hzensh,p Number (x3)

<!-- b000632 | prose | pages [31] -->
Age (x4)

<!-- b000633 | prose | pages [31] -->
Educahonal Background (x5)

<!-- b000634 | prose | pages [31] -->
Address (x6)

<!-- b000635 | prose | pages [31] -->
c。ntact曹ay(x7)

<!-- b000636 | prose | pages [31] -->
Fai th(x8)

<!-- b000637 | prose | pages [31] -->
Portrait (x9)

<!-- b000638 | prose | pages [31] -->
H。bby(xlO)

<!-- b000639 | prose | pages [31] -->
Total Assets(xll)

<!-- b000640 | prose | pages [31] -->
Income (x12)

<!-- b000641 | prose | pages [31] -->
Expenditure (x13)

<!-- b000642 | prose | pages [31] -->
Intellectual Pr。perty(x14)

<!-- b000643 | prose | pages [31] -->
s。cial iay(x15)

<!-- b000644 | prose | pages [31] -->
Fnends (x16)

<!-- b000645 | prose | pages [31] -->
Social Signal (xl 7)

<!-- b000646 | prose | pages [31] -->
Financial Credit (x18)

<!-- b000647 | prose | pages [31] -->
Trading Info，回tion(x19)

<!-- b000648 | prose | pages [31] -->
Transactioo 。n Am。unt(x20)

<!-- b000649 | prose | pages [31] -->
Debt(x21)

<!-- b000650 | prose | pages [31] -->
Physical Heal th Status (x22)

<!-- b000651 | prose | pages [31] -->
ledical Insurance (x23)

<!-- b000652 | prose | pages [31] -->
ledical Hist。ry(x24) ledical Expense(x25)

<!-- b000653 | prose | pages [31] -->
Genetic Ian (x26}
