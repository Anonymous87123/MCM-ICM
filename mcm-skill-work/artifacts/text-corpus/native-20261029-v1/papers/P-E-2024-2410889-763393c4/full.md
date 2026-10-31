# P-E-2024-2410889-763393c4

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
2024

<!-- b000002 | prose | pages [1] -->
Problem Chosen

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | prose | pages [1] -->
MCM/ICM

<!-- b000005 | title | pages [1] -->
E

<!-- b000006 | furniture | pages [1] -->
2410889

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Find a Home for Your Property

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | title | pages [1] -->
微信公众号：数学模型

<!-- b000011 | prose | pages [1] -->
As the frequency of extreme weather events increases globally, the threat to prop- erty safety is growing, leading to higher insurance claim risks and consequently rapid increases in insurance rates. This results in potential losses for insurance companies and unaffordable insurance premiums for property owners. This paper develops an insurance model to assess whether insurance companies should conduct business in these areas. Additionally, a protection model is established to identify properties of cultural and community signiﬁcance and to provide recommendations for protective measures.

<!-- b000012 | prose | pages [1] -->
For Task 1, we developed an underwriting decision model based on whether the insurance company is proﬁtable as the decision criterion. Using Monte Carlo simula- tions, we generated 100 insurance scenarios to calculate the probability of proﬁtability for the insurance company, which informed the underwriting decisions. Demonstrat-

<!-- b000013 | title | pages [1] -->
微信号：MATHmodels

<!-- b000014 | prose | pages [1] -->
ing this model in Guangdong Province, China, and Florida, USA, the probability of proﬁtable underwriting in Guangdong is 63%, while it is 26% in Florida. Therefore, the insurance company undertakes underwriting in Guangdong but not in Florida. Addi- tionally, when the base rate is high, the insurance company opts for risk-taking. Prop- erty owners can inﬂuence the insurance company’s decision by using a risk checklist to reduce the probability of property damage.

<!-- b000015 | prose | pages [1] -->
For Task 2, we improved the underwriting decision model to quantify the level of real estate protection in different locations within speciﬁc areas. Furthermore, we quantiﬁed convenience based on the distance from the location to living service areas. Then, we established a goal programming model that maximizes both the level of protection and convenience, solving for the optimal construction site using particle swarm optimization. We recommend not constructing in locations with a target value lower than 0.5 and choosing high disaster-resistant building materials for locations with lower levels of protection.

<!-- b000016 | prose | pages [1] -->
For Task 3, we proposed a protection value assessment model that considers cul- tural, historical, economic, and community values. Using EWM-TOPSIS, we calcu- lated protection value scores and divided them into four levels: no protection (0-0.1), ﬁrst-level protection (0.1-0.3), second-level protection (0.3-0.5), and third-level pro- tection (0.5-1.0). The level into which a building falls determines whether it is pro- tected, with speciﬁc protective measures proposed for each protection level. For Task 4, we selected the Forbidden City in Beijing as the case study. Using the underwriting decision model and protection value assessment model, we found that the Forbidden City has signiﬁcant cultural, historical, economic, and community values with high sustainable development value. Its protection value is 0.618, qualifying it as a third- level protection building.

<!-- b000017 | heading | pages [1] -->
Finally, we conducted a sensitivity analysis on the underwriting decision model

<!-- b000018 | prose | pages [1] -->
and protection value assessment model. With the investment interest rate varying between [0.002,0.007], the insurance company’s decisions remain unchanged. A 20% variation in the protection value indicators results in a total value score change of no more than 5%, demonstrating the reliability of the models proposed in this paper.

<!-- b000019 | keywords | pages [1] -->
Keywords: Underwriting decision model; Monte Carlo simulations; Risk checklist;

<!-- b000020 | prose | pages [1] -->
关注数学模型 Goal programming; EWM-TOPSIS; protection value model

<!-- b000021 | furniture | pages [1] -->
2

<!-- b000022 | furniture | pages [1] -->
MATHmodels

<!-- b000023 | furniture | pages [1] -->
获取更多资讯

<!-- b000024 | furniture | pages [2] -->
Team # 2410889

<!-- b000025 | furniture | pages [2] -->
Page 2 of 23

<!-- b000026 | heading | pages [2] -->
Contents

<!-- b000027 | contents | pages [2] -->
1

<!-- b000028 | heading | pages [2] -->
Introduction

<!-- b000029 | prose | pages [2] -->
3 Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 3

<!-- b000030 | prose | pages [2] -->
微信公众号：数学模型

<!-- b000031 | prose | pages [2] -->
Restatement of the problem and our work . . . . . . . . . . . . . . . . . . 1.2

<!-- b000032 | prose | pages [2] -->
2

<!-- b000033 | heading | pages [2] -->
Assumption and Justiﬁcations

<!-- b000034 | prose | pages [2] -->
3

<!-- b000035 | heading | pages [2] -->
Notations

<!-- b000036 | prose | pages [2] -->
4

<!-- b000037 | heading | pages [2] -->
Underwriting Decision Model

<!-- b000038 | prose | pages [2] -->
3

<!-- b000039 | prose | pages [2] -->
4

<!-- b000040 | prose | pages [2] -->
5

<!-- b000041 | prose | pages [2] -->
5 Policy Risk Assessment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 6 Income reallocation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2 7 Pricing of premiums . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2.1 7 Reallocation of premium income . . . . . . . . . . . . . . . . . . . 4.2.2 8 Perform underwriting decisions . . . . . . . . . . . . . . . . . . . . . . . . 4.3 9 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3.1 Cost Calculation 9

<!-- b000042 | prose | pages [2] -->
微信号：MATHmodels

<!-- b000043 | prose | pages [2] -->
Judgment Criteria for Decision-making . . . . . . . . . . . . . . . 4.3.2 4.4 Demonstration of Model Results 10 . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000044 | prose | pages [2] -->
10

<!-- b000045 | heading | pages [2] -->
Underwriting Decision-Goal Programming Model

<!-- b000046 | prose | pages [2] -->
5 12 Adaptation of UDM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 12 Model of Property Decisions . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2 12 Model Effect Demonstration . . . . . . . . . . . . . . . . . . . . . . . . . . 5.3

<!-- b000047 | prose | pages [2] -->
6

<!-- b000048 | heading | pages [2] -->
Protection Value Assessment Model

<!-- b000049 | prose | pages [2] -->
13

<!-- b000050 | prose | pages [2] -->
14 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 Discussion of Indicators 14 Scoring based on the EWM-TOPSIS . . . . . . . . . . . . . . . . . . . . . . 6.2 16 Protection Measures Under Each Level . . . . . . . . . . . . . . . . . . . . 6.3

<!-- b000051 | prose | pages [2] -->
7 Case Study: the Forbidden City

<!-- b000052 | prose | pages [2] -->
17

<!-- b000053 | prose | pages [2] -->
19 Underwriting Decision Model . . . . . . . . . . . . . . . . . . . . . . . . . 7.1 19 Protection Value Assessment Model 7.2

<!-- b000054 | prose | pages [2] -->
8

<!-- b000055 | heading | pages [2] -->
Sensitivity Analysis

<!-- b000056 | prose | pages [2] -->
9

<!-- b000057 | heading | pages [2] -->
Strengths and Weaknesses

<!-- b000058 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . .

<!-- b000059 | prose | pages [2] -->
20

<!-- b000060 | prose | pages [2] -->
21

<!-- b000061 | prose | pages [2] -->
22 Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.1 22 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.2 Weaknesses

<!-- b000062 | heading | pages [2] -->
References

<!-- b000063 | references | pages [2] -->
22

<!-- b000064 | references | pages [2] -->
23

<!-- b000065 | references | pages [2] -->
关注数学模型

<!-- b000066 | furniture | pages [2] -->
2

<!-- b000067 | furniture | pages [2] -->
MATHmodels

<!-- b000068 | furniture | pages [2] -->
获取更多资讯

<!-- b000069 | furniture | pages [3] -->
Team # 2410889

<!-- b000070 | references | pages [3] -->
1

<!-- b000071 | heading | pages [3] -->
Introduction

<!-- b000072 | prose | pages [3] -->
1.1 Problem Background

<!-- b000073 | furniture | pages [3] -->
Page 3 of 23

<!-- b000074 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000075 | prose | pages [3] -->
As the global population and economy grow, the frequency of human activities is also increasing. The result of this increased human activity is an increasing concen- tration of greenhouse gases in the atmosphere and an intensiﬁcation of the problem of global warming. Petteri Taras, Secretary General of the World Meteorological Orga- nization, said in an interview in 2021, "Humans are no strangers to extreme weather, but climate change has undoubtedly increased the frequency and severity of extreme weather."

<!-- b000076 | prose | pages [3] -->
Extreme weather events are also taking an increasing toll on people. According to the World Meteorological Organization, economic losses from extreme weather in- creased 7-fold from the 1970s to the 2010s. And that’s a huge blow to the insurance industry because it means insurers also face higher claims. The Boston Consulting

<!-- b000077 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000078 | prose | pages [3] -->
Group predicts that climate change will increase insurance premiums by 30 to 60 per- cent by 2040, which could reﬂect a worse proﬁtability for insurers. So how insurers should adjust in an environment where extreme events continue is a question worth considering.

<!-- b000079 | caption | pages [3] -->
Figure 1: Abnormal temperatures(Image courtesy of The Copernicus Climate Change Service

<!-- b000080 | prose | pages [3] -->
(C3S))

<!-- b000081 | prose | pages [3] -->
Restatement of the problem and our work 1.2

<!-- b000082 | heading | pages [3] -->
(1) Problem Restatement: Develop an insurance model to identify whether in-

<!-- b000083 | prose | pages [3] -->
surance companies are underwriting in places where extreme weather is increasing. And apply the model to two regions on different continents that experience extreme weather events.

<!-- b000084 | prose | pages [3] -->
Our work: We construct a model of the proﬁtability of insurance companies, using whether or not they are proﬁtable as the basis for decisions about whether to under- write a policy. The probability of payout for each policy is quantiﬁed, and 1000 times Monte Carlo sampling is performed, which in turn yields the proﬁtability of an insur- ance company in terms of a region. Guangdong Province in China and Florida in the U.S. are chosen to demonstrate the model.

<!-- b000085 | prose | pages [3] -->
关注数学模型

<!-- b000086 | furniture | pages [3] -->
2

<!-- b000087 | furniture | pages [3] -->
MATHmodels

<!-- b000088 | furniture | pages [3] -->
获取更多资讯

<!-- b000089 | furniture | pages [4] -->
Team # 2410889

<!-- b000090 | furniture | pages [4] -->
Page 4 of 23

<!-- b000091 | heading | pages [4] -->
(2) Problem Restatement: In a given region, the insurance model evaluates where

<!-- b000092 | prose | pages [4] -->
to build real estate, how to build it, and whether to build it at all.

<!-- b000093 | prose | pages [4] -->
Our work: Considering the degree of protection and convenience of real estate, the farther away from the place where extreme weather occurs the higher the degree

<!-- b000094 | prose | pages [4] -->
微信公众号：数学模型

<!-- b000095 | prose | pages [4] -->
of protection will be, and the closer to the living service area the higher the degree of convenience will be. Therefore, we combine the insurance model to build a goal programming model to solve to get the optimal construction location.

<!-- b000096 | heading | pages [4] -->
(3) Problem Restatement: Develop a conservation model that identiﬁes the build-

<!-- b000097 | prose | pages [4] -->
ings that should be protected and the corresponding conservation measures.

<!-- b000098 | prose | pages [4] -->
Our work: We consider the impact of 4 dimensions: Cultures, Histories, Eco- nomics, and Communities. We also establish a conservation value assessment model through the EWM-TOPSIS method. Finally, the score is divided into 4 intervals: no protection, primary protection, secondary protection, and tertiary protection, and cor- responding protection measures are taken according to the protection level.

<!-- b000099 | prose | pages [4] -->
(4) Problem Restatement: Select a landmark that has experienced an extreme weather

<!-- b000100 | prose | pages [4] -->
微信号：MATHmodels

<!-- b000101 | prose | pages [4] -->
event and evaluate the value of the landmark using an insurance model and a protec- tion model.

<!-- b000102 | prose | pages [4] -->
Our work: Select the Forbidden City located in Beijing, China to assess the value of the landmark and use the insurance model to get the probability that the Forbidden City can enjoy the insurance service, and use the conservation model to get the value of the Forbidden City in terms of its history, economy, and so on.

<!-- b000103 | prose | pages [4] -->
For a clearer understanding of our processa more intuitive understanding of our approach can be seen in the ﬂowchart below.

<!-- b000104 | caption | pages [4] -->
Figure 2: Flowchart of ideas

<!-- b000105 | prose | pages [4] -->
2

<!-- b000106 | heading | pages [4] -->
Assumption and Justiﬁcations

<!-- b000107 | prose | pages [4] -->
• Assumption:The demand for one year’s worth of policies in an area is known and does not change due to changes in policy rates.

<!-- b000108 | heading | pages [4] -->
Justiﬁcation:Reducing the complexity of the model scenario makes the scenario

<!-- b000109 | prose | pages [4] -->
关注数学模型 easier to simulate.

<!-- b000110 | furniture | pages [4] -->
2

<!-- b000111 | furniture | pages [4] -->
MATHmodels

<!-- b000112 | furniture | pages [4] -->
获取更多资讯

<!-- b000113 | furniture | pages [5] -->
Team # 2410889

<!-- b000114 | furniture | pages [5] -->
Page 5 of 23

<!-- b000115 | heading | pages [5] -->
• Assumption:The probability of a policy payout occurring is positively related to

<!-- b000116 | prose | pages [5] -->
the risk of the policy. Justiﬁcation:The risk of a policy is often measured by the probability of a claim occurring; the higher the probability of a claim, the higher the risk.

<!-- b000117 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000118 | prose | pages [5] -->
• hypothesis:Buildings within an area have the same external risk, and internal risk is related to their own building risk. Justiﬁcation:External risk comes mainly from the effects of extreme weather, which can have a large impact and can cover an entire region. • Assumption:Insurance companies can spread the risk by reinsurance.

<!-- b000119 | prose | pages [5] -->
Justiﬁcation:There are a large number of insurance companies in the world, and one insurance company can buy insurance from another.

<!-- b000120 | prose | pages [5] -->
3

<!-- b000121 | heading | pages [5] -->
Notations

<!-- b000122 | prose | pages [5] -->
In the following table we list some of the symbols and deﬁnitions we use.

<!-- b000123 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000124 | prose | pages [5] -->
Symbols Deﬁnition

<!-- b000125 | prose | pages [5] -->
O A policy OS A collection of policies OSi A collection of low-risk policies OSh A collection of high-risk policies CO Policy premiums AO Policy amount PO Policy beneﬁt amount FO Rate of the policy RO Risk of the policy βj Extent of damage to property in area j ratej Annual expected investment yield in area j dIi,j Distance of location i from the jth extreme weather occurrence dLi,k Distance of location i from the kth life service area

<!-- b000126 | prose | pages [5] -->
Other symbols will be described as they are used

<!-- b000127 | prose | pages [5] -->
4

<!-- b000128 | heading | pages [5] -->
Underwriting Decision Model

<!-- b000129 | prose | pages [5] -->
For the underwriting decision modeling, our premise is that insurance companies are "economic beings". That is, insurance companies are most concerned with proﬁt, and when the proﬁt is positive, insurance companies are willing to underwrite policies in a region. In order to calculate the proﬁt, we ﬁrst consider how to evaluate the risk of a policy in a region, which is set as RO in this model. Then we develop a premium pricing strategy based on RO. To obtain greater income as well as to reduce risk, we consider that the insurance company will redistribute the total premium income (set as RI in this model) into reserve funds, investment assets, and reinsurance funds. Thus关注数学模型

<!-- b000130 | furniture | pages [5] -->
2

<!-- b000131 | furniture | pages [5] -->
MATHmodels

<!-- b000132 | furniture | pages [5] -->
获取更多资讯

<!-- b000133 | furniture | pages [6] -->
Team # 2410889

<!-- b000134 | furniture | pages [6] -->
Page 6 of 23

<!-- b000135 | prose | pages [6] -->
the insurance company’s true income over the policy term is RI′. Finally, the proﬁt is calculated by subtracting costs from the true income RI′.

<!-- b000136 | prose | pages [6] -->
微信公众号：数学模型

<!-- b000137 | prose | pages [6] -->
4.1 Policy Risk Assessment

<!-- b000138 | prose | pages [6] -->
To assess the risk of an order, we consider the external risk RE

<!-- b000139 | prose | pages [6] -->
RI O and the internal risk

<!-- b000140 | prose | pages [6] -->
O of the order. External risk refers to the risk of damage to the property caused by an extreme weather event; internal risk refers to the insured property’s risk proﬁle, e.g., if the insured property has a high level of resilience, then the risk of damage occurring in the face of equivalent extreme weather is lower. We believe that it is more comprehensive and reasonable to assess the risk of a policy through both internal and external risks.

<!-- b000141 | prose | pages [6] -->
(1) Quantify external risk RE

<!-- b000142 | prose | pages [6] -->
O Most extreme weather events cause economic damage to the area, and insurance companies then pay out to their customers. A higher number of extreme weather

<!-- b000143 | prose | pages [6] -->
微信号：MATHmodels

<!-- b000144 | prose | pages [6] -->
events in a region means that insurers are exposed to a higher risk of paying out. We therefore use the frequency of extreme weather events in a region in a year as a measure of external risk, which is

<!-- b000145 | prose | pages [6] -->
Pn

<!-- b000146 | prose | pages [6] -->
RE

<!-- b000147 | prose | pages [6] -->
O =

<!-- b000148 | prose | pages [6] -->
i=1 ewni (1) n × 365

<!-- b000149 | prose | pages [6] -->
Where, ewni means the number of times the ith type of extreme weather occurs in a year, and n means the number of extreme weather types occurring in a region during the insurance period.

<!-- b000150 | prose | pages [6] -->
(2) Quantify internal risk RI

<!-- b000151 | prose | pages [6] -->
O We use the risk checklist checklist methodology in risk management to quantify

<!-- b000152 | prose | pages [6] -->
[1]. The risk checklist includes multiple risk dimensions that help users to

<!-- b000153 | prose | pages [6] -->
internal risks

<!-- b000154 | prose | pages [6] -->
more fully understand the nature and extent of risks and to predict the probability of a compromised risk occurring and the impact it may result in.

<!-- b000155 | prose | pages [6] -->
One of the property risk management evaluation forms we have produced is shown below

<!-- b000156 | caption | pages [6] -->
Table 1: Internal risk checksheet

<!-- b000157 | prose | pages [6] -->
关注数学模型

<!-- b000158 | furniture | pages [6] -->
2

<!-- b000159 | furniture | pages [6] -->
MATHmodels

<!-- b000160 | furniture | pages [6] -->
获取更多资讯

<!-- b000161 | furniture | pages [7] -->
Team # 2410889

<!-- b000162 | furniture | pages [7] -->
Page 7 of 23

<!-- b000163 | prose | pages [7] -->
After scoring and normalizing each detail according to the evaluation criteria, we then average the total of all the evaluation metrics scores as the internal risk score for the policy. That is

<!-- b000164 | prose | pages [7] -->
Pm

<!-- b000165 | prose | pages [7] -->
i=1 TOi

<!-- b000166 | prose | pages [7] -->
微信公众号：数学模型

<!-- b000167 | prose | pages [7] -->
RI

<!-- b000168 | prose | pages [7] -->
O =

<!-- b000169 | prose | pages [7] -->
(2) m

<!-- b000170 | prose | pages [7] -->
Where TOi means the score of the ith indicator in the risk checklist and m means the number of indicators.

<!-- b000171 | prose | pages [7] -->
(3) Quantify policy risk

<!-- b000172 | prose | pages [7] -->
Considering that internal risks can be intervened through human intervention, for example, in Japan most of the building materials are wooden structures, which are well suited to minimize the damage caused by earthquakes. External risks, on the other hand, are usually difﬁcult to intervene, or to intervene effectively. This is be- cause the weather system is very complex, and consists of a variety of factors such as atmospheric circulation, water cycle, etc., which work together and affect each other. It is still difﬁcult to make accurate predictions and interventions with our current re-

<!-- b000173 | prose | pages [7] -->
微信号：MATHmodels

<!-- b000174 | prose | pages [7] -->
sources and technology.

<!-- b000175 | prose | pages [7] -->
In summary, we believe that external risks will have a greater impact on a policy than internal risks, so we assign a weight of 0.6 to external risks and 0.4 to internal risks:

<!-- b000176 | prose | pages [7] -->
RO = 0.6RE

<!-- b000177 | prose | pages [7] -->
4.2 Income reallocation

<!-- b000178 | prose | pages [7] -->
4.2.1 Pricing of premiums

<!-- b000179 | prose | pages [7] -->
O + 0.4RI

<!-- b000180 | prose | pages [7] -->
(3) O

<!-- b000181 | prose | pages [7] -->
The most direct source of income for insurance companies is premium income. Let us set O to be a policy, CO to be the premium of a policy, AO to be the amount of a policy, and FO to be the rate of a policy then the insurance company’s premium income from a policy is

<!-- b000182 | prose | pages [7] -->
CO = AO × FO (4)

<!-- b000183 | prose | pages [7] -->
where the policy amount AO is determined by the value of the insured property. We assume that policyholders buy full insurance policies, i.e., the policy amount is equal to the insured value. We assume that there are 1000 policies in a region and the policy amount AO is randomly generated under the N(µ, σ) distribution. The µ denotes the average property value in the area and σ is set to 0.2 times µ.

<!-- b000184 | prose | pages [7] -->
The policy rate FO consists of a base rate, which is related to the operating condition of the insurance company, and a risk rate, which is related to the risk of the policy. We set the base rate to be 0.3% and the coefﬁcient of the risk rate to be 0.1%, then the formula for calculating the insurance rate for a region is

<!-- b000185 | prose | pages [7] -->
FO = α + λ × RO (5)

<!-- b000186 | prose | pages [7] -->
Where α is the base rate and λ is the risk rate coefﬁcient, in this paper, the base rate is set at 0.3% and the coefﬁcient of the risk rate is 0.1%.

<!-- b000187 | prose | pages [7] -->
关注数学模型

<!-- b000188 | furniture | pages [7] -->
2

<!-- b000189 | furniture | pages [7] -->
MATHmodels

<!-- b000190 | furniture | pages [7] -->
获取更多资讯

<!-- b000191 | furniture | pages [8] -->
Team # 2410889

<!-- b000192 | prose | pages [8] -->
4.2.2 Reallocation of premium income

<!-- b000193 | furniture | pages [8] -->
Page 8 of 23

<!-- b000194 | prose | pages [8] -->
After collecting premiums, based on the need for risk diversiﬁcation, insurance companies will also re-insure, i.e., by signing insurance contracts with other insurance

<!-- b000195 | prose | pages [8] -->
微信公众号：数学模型

<!-- b000196 | prose | pages [8] -->
companies, they will spread part of their risks to the other party. In addition, insur- ance companies usually use part of the premiums to invest in other ﬁnancial products

<!-- b000197 | prose | pages [8] -->
[2]. All these behaviors will affect the income of the in-

<!-- b000198 | prose | pages [8] -->
in order to obtain more income

<!-- b000199 | prose | pages [8] -->
surance company, so we need to consider these behaviors to get the ﬁnal income of the insurance company.

<!-- b000200 | prose | pages [8] -->
(1) Reserve Assets RIa

<!-- b000201 | prose | pages [8] -->
An insurance company needs to have a certain amount of money as a reserve for policy payments as well as to maintain the company’s normal operations. We set the insurance company to keep half of its premium income for one year as a reserve, which can be thought of as cash on hand, i.e., the amount does not change. Given that the insurance company’s total premium income for one year is RI, the money value of the reserve fund after one year will be

<!-- b000202 | prose | pages [8] -->
微信号：MATHmodels

<!-- b000203 | prose | pages [8] -->
RI′

<!-- b000204 | prose | pages [8] -->
X

<!-- b000205 | prose | pages [8] -->
a = RIa = 0.5RI =

<!-- b000206 | prose | pages [8] -->
CO (6)

<!-- b000207 | prose | pages [8] -->
O∈OS

<!-- b000208 | prose | pages [8] -->
Where RIa means the funds used for the imprest and OS means the collection of all policies.

<!-- b000209 | prose | pages [8] -->
(2) Reinsurance Assets RIb

<!-- b000210 | prose | pages [8] -->
We categorize policies into high-risk and low-risk policies, and set a risk threshold such that policies larger than the risk threshold are high-risk policies, otherwise they are low-risk policies. The insurance company is set to reinsure only high-risk policies to achieve risk diversiﬁcation. Set OSh to denote the set of high-risk policies, set OSl to denote the set of low-risk policies, and RIb to denote the funds used for reinsurance, then there are

<!-- b000211 | prose | pages [8] -->
RIb =

<!-- b000212 | prose | pages [8] -->
X

<!-- b000213 | prose | pages [8] -->
CO (7)

<!-- b000214 | prose | pages [8] -->
O∈OSh

<!-- b000215 | prose | pages [8] -->
For policies that are reinsured, they may be in force within the next year, i.e., claims will need to be made. But it is also possible that it will not be in force. We need to distinguish between such cases. Let each policy in the pool of high-risk policies have a premium funding value of EO after one year, and we have

<!-- b000216 | prose | pages [8] -->
(

<!-- b000217 | prose | pages [8] -->
COh −C′

<!-- b000218 | prose | pages [8] -->
Oh,

<!-- b000219 | prose | pages [8] -->
EO =

<!-- b000220 | prose | pages [8] -->
COh −C′

<!-- b000221 | prose | pages [8] -->
Oh + P ′

<!-- b000222 | prose | pages [8] -->
Policy O not in force

<!-- b000223 | prose | pages [8] -->
(8) Oh, Policy O in force

<!-- b000224 | prose | pages [8] -->
Oh denotes the premium for reinsurance, and P ′

<!-- b000225 | prose | pages [8] -->
Where Oh ∈OSh, C′

<!-- b000226 | prose | pages [8] -->
Oh denotes the amount of payout received for reinsurance (the quantitative formula for PO is given in 4.3.1).

<!-- b000227 | prose | pages [8] -->
Since reinsurance transfers part of the risk to other ﬁrms rather than transferring the whole risk. Therefore we set C′

<!-- b000228 | prose | pages [8] -->
Oh = 0.8COh. If the rate of reinsurance is lower than the rate of original insurance, then the amount of payout received should be less, we set P ′

<!-- b000229 | prose | pages [8] -->
Oh = 0.4POh.

<!-- b000230 | prose | pages [8] -->
In summary, we can get the capital value of reinsurance after one year as

<!-- b000231 | prose | pages [8] -->
RI′

<!-- b000232 | prose | pages [8] -->
b =

<!-- b000233 | prose | pages [8] -->
X

<!-- b000234 | prose | pages [8] -->
EO (9)关注数学模型

<!-- b000235 | furniture | pages [8] -->
2

<!-- b000236 | prose | pages [8] -->
O∈OSh

<!-- b000237 | furniture | pages [8] -->
MATHmodels

<!-- b000238 | furniture | pages [8] -->
获取更多资讯

<!-- b000239 | furniture | pages [9] -->
Team # 2410889

<!-- b000240 | prose | pages [9] -->
(3) Investment Assets RIc

<!-- b000241 | furniture | pages [9] -->
Page 9 of 23

<!-- b000242 | prose | pages [9] -->
Suppose that the insurance company allocates only three parts of its premium in- come in a year, i.e., reserve funds, reinsurance funds and investment funds. Setting the

<!-- b000243 | prose | pages [9] -->
微信公众号：数学模型

<!-- b000244 | prose | pages [9] -->
value of the funds used for investment as RIc, we have

<!-- b000245 | prose | pages [9] -->
RIc = RI −RIa −RIb (10)

<!-- b000246 | prose | pages [9] -->
Insurance companies typically purchase a variety of ﬁnancial products when mak- ing investments. To simplify the model, we assume that the insurance company owns equal proportions of each ﬁnancial product and purchases the ﬁnancial products in the corresponding underwriting regions. From this we can obtain the expected annual rate of return on investment in a region j, which is set to ratej. The value of the funds used for investment by the insurance company after one year is then

<!-- b000247 | prose | pages [9] -->
RI′

<!-- b000248 | prose | pages [9] -->
c = RIc × (1 + ratej) (11)

<!-- b000249 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000250 | prose | pages [9] -->
Summing up, we can get the real income R of the insurance company after one year as

<!-- b000251 | prose | pages [9] -->
a + RI′

<!-- b000252 | prose | pages [9] -->
R = RI′

<!-- b000253 | prose | pages [9] -->
b + RI′

<!-- b000254 | prose | pages [9] -->
(12) c

<!-- b000255 | prose | pages [9] -->
Perform underwriting decisions 4.3

<!-- b000256 | prose | pages [9] -->
4.3.1 Cost Calculation

<!-- b000257 | prose | pages [9] -->
The main cost of an insurance company is the cost of claims, so we use the cost of claims as the cost of the insurance company. Setting the amount of the claim as PO, the cost C of the insurance company is

<!-- b000258 | prose | pages [9] -->
X

<!-- b000259 | prose | pages [9] -->
C =

<!-- b000260 | prose | pages [9] -->
O∈OS

<!-- b000261 | prose | pages [9] -->
PO × ZO (13)

<!-- b000262 | prose | pages [9] -->
Where O means one policy and OS means the set of policies within one year. ZO ∈ {0, 1} is a judgment coefﬁcient, ZO = 1 when the policy is in force, which means that a payout occurs, otherwise ZO = 0.

<!-- b000263 | prose | pages [9] -->
Since the payout amount PO is determined by the extent of damage to the property, we need to consider how to measure the extent of damage to the property. In the model, we use the loss per unit area caused by extreme weather to measure the degree of damage to the property. Given that βj ∈[0, 1] denotes the degree of damage to the property in area j, there are

<!-- b000264 | prose | pages [9] -->
TLj βj = Lj/Lmax =

<!-- b000265 | prose | pages [9] -->
(14)

<!-- b000266 | prose | pages [9] -->
Sj × Lmax

<!-- b000267 | prose | pages [9] -->
Where, TLj means the total loss of area j in a year, Sj means the land area of area j, and Lmax is the maximum value in Lj.

<!-- b000268 | prose | pages [9] -->
Then the quantization formula for the payout amount can be further obtained as

<!-- b000269 | prose | pages [9] -->
PO = AO × βj (15)

<!-- b000270 | prose | pages [9] -->
关注数学模型

<!-- b000271 | furniture | pages [9] -->
2

<!-- b000272 | furniture | pages [9] -->
MATHmodels

<!-- b000273 | furniture | pages [9] -->
获取更多资讯

<!-- b000274 | furniture | pages [10] -->
Team # 2410889

<!-- b000275 | furniture | pages [10] -->
Page 10 of 23

<!-- b000276 | prose | pages [10] -->
Judgment Criteria for Decision-making 4.3.2

<!-- b000277 | prose | pages [10] -->
If a risk has proﬁt potential, the insurance company will choose to take the risk to make a proﬁt. Based on all of the above discussion, we can obtain a quantitative

<!-- b000278 | prose | pages [10] -->
微信公众号：数学模型

<!-- b000279 | prose | pages [10] -->
formula for the proﬁt P that an insurance company makes if it chooses to underwrite in an area where extreme weather events occur

<!-- b000280 | prose | pages [10] -->
P = R −C

<!-- b000281 | prose | pages [10] -->
Which,R = RI′

<!-- b000282 | prose | pages [10] -->
a + RI′

<!-- b000283 | prose | pages [10] -->
b + RI′

<!-- b000284 | prose | pages [10] -->
X

<!-- b000285 | prose | pages [10] -->
EO + RIc × (1 + ratej)

<!-- b000286 | prose | pages [10] -->
c = 0.5RIa +

<!-- b000287 | prose | pages [10] -->
X

<!-- b000288 | prose | pages [10] -->
PO×ZO =

<!-- b000289 | prose | pages [10] -->
C =

<!-- b000290 | prose | pages [10] -->
O∈OS

<!-- b000291 | prose | pages [10] -->
(16)

<!-- b000292 | prose | pages [10] -->
O∈OSh

<!-- b000293 | prose | pages [10] -->
X

<!-- b000294 | prose | pages [10] -->
(AO × βj) × ZO

<!-- b000295 | prose | pages [10] -->
O∈OS

<!-- b000296 | prose | pages [10] -->
When the proﬁt P is positive, the insurance company is able to underwrite in the respective area.

<!-- b000297 | prose | pages [10] -->
微信号：MATHmodels

<!-- b000298 | heading | pages [10] -->
Demonstration of Model Results

<!-- b000299 | prose | pages [10] -->
4.4

<!-- b000300 | prose | pages [10] -->
We chose Florida in the United States and Guangdong Province in China to demon- strate our model. According to a news release from the National Oceanic and Atmo-

<!-- b000301 | prose | pages [10] -->
[3], in 2023 the United States suffered 28 disasters with

<!-- b000302 | prose | pages [10] -->
spheric Administration (NOAA)

<!-- b000303 | prose | pages [10] -->
single losses of more than one billion dollars, of which eight affected Florida. Guang- dong Province, a coastal city, was affected by six typhoons in 2022, with 25 days of heavy rainfall during the storm period and direct economic losses of over half a billion dollars. These two regions are therefore well suited to demonstrate our model.

<!-- b000304 | prose | pages [10] -->
Since the probability of a policy payout is positively correlated with the policy risk, through continuous debugging, we decided to divide the policy risk by 10 to get the probability of the policy incurring a payout. We take a random number at [0,1] and consider the policy not in force when the random number is greater than the prob- ability of payout, otherwise it is in force. The effectiveness of n policies in a region constitutes an insurance scenario for that region

<!-- b000305 | prose | pages [10] -->
U = [u1, u2, ..., un] (17)

<!-- b000306 | prose | pages [10] -->
Considering the randomness of the results obtained by generating the scenario only once, we performed Monte Carlo sampling 100 times to make the coverage decision by

<!-- b000307 | prose | pages [10] -->
[4].

<!-- b000308 | prose | pages [10] -->
observing the frequency of P > 0

<!-- b000309 | prose | pages [10] -->
Fig3 shows the simulation results. It can be clearly observed that the frequency of proﬁts P < 0 in Florida is much larger than the frequency of P > 0, and therefore we do not recommend insurance companies to underwrite in this region. The frequency of proﬁt P > 0 is much higher in Guangdong Province, so we believe that insurers can underwrite here.

<!-- b000310 | prose | pages [10] -->
关注数学模型

<!-- b000311 | furniture | pages [10] -->
2

<!-- b000312 | furniture | pages [10] -->
MATHmodels

<!-- b000313 | furniture | pages [10] -->
获取更多资讯

<!-- b000314 | furniture | pages [11] -->
Team # 2410889

<!-- b000315 | furniture | pages [11] -->
Page 11 of 23

<!-- b000316 | prose | pages [11] -->
微信公众号：数学模型

<!-- b000317 | prose | pages [11] -->
(a) Results for Florida (b) Results for Guangdong

<!-- b000318 | caption | pages [11] -->
Figure 3: Results of multiple simulations of the UDM model in the region

<!-- b000319 | prose | pages [11] -->
Analyzing the reason for this result, we believe it is related to the number of ex- treme weather events in the two regions. The number of extreme weather events in a

<!-- b000320 | prose | pages [11] -->
微信号：MATHmodels

<!-- b000321 | prose | pages [11] -->
year is 57 in Florida and 35 in Guangdong Province, and the higher the number of ex- treme weather events, the higher the policy external risk RE

<!-- b000322 | prose | pages [11] -->
O, the higher the policy risk and the probability of payout. Although premiums also increase, they increase more slowly and cannot keep up with the increase in claims costs because insurers cannot set premiums too high or they will face the problem of customer churn. So premiums don’t increase as fast as claims costs, causing the insurance company to lose money.

<!-- b000323 | prose | pages [11] -->
Both insurance companies and property owners are concerned about insurance rates, so we examined how insurance companies operate under different base rates.

<!-- b000324 | caption | pages [11] -->
Figure 4: Operations of insurance companies at different rates

<!-- b000325 | prose | pages [11] -->
As can be seen in Fig4, insurance companies begin to make a proﬁt when the policy base rate is approximately 0.0034. So when the base rate is higher in areas with more extreme weather events, the insurance company may choose to take a chance on un- derwriting the policy. Since the change in base rate is what ultimately affects the policy rate FO, it can be assumed that FO plays a decisive role in the insurer’s decision. So for homeowners, they can reduce their risk rate by reducing their property’s own risk and thus affecting FO, which ultimately affects the insurance company’s decision.

<!-- b000326 | prose | pages [11] -->
关注数学模型

<!-- b000327 | furniture | pages [11] -->
2

<!-- b000328 | furniture | pages [11] -->
MATHmodels

<!-- b000329 | furniture | pages [11] -->
获取更多资讯

<!-- b000330 | furniture | pages [12] -->
Team # 2410889

<!-- b000331 | furniture | pages [12] -->
Page 12 of 23

<!-- b000332 | heading | pages [12] -->
Underwriting Decision-Goal Programming Model

<!-- b000333 | prose | pages [12] -->
5

<!-- b000334 | prose | pages [12] -->
To reduce exposure to extreme weather events, communities and property devel-

<!-- b000335 | prose | pages [12] -->
微信公众号：数学模型

<!-- b000336 | prose | pages [12] -->
opers need to consider where to build properties or what materials to use to build properties to make them more resilient. It is also important to consider ease of living and not just build in remote areas to reduce risk. In order to help real estate develop- ers make sound decisions within a speciﬁc region, we made some adjustments to the underwriting decision model to make it generalizable.

<!-- b000337 | prose | pages [12] -->
5.1 Adaptation of UDM

<!-- b000338 | prose | pages [12] -->
In the risk assessment portion of our underwriting decision model, the policy ex- ternal risk RE

<!-- b000339 | prose | pages [12] -->
O only considers extreme weather conditions in one region. To apply the model to real estate construction decisions, it is necessary to consider how the dis- tance of a location from the site of an extreme weather event affects the external risk,

<!-- b000340 | prose | pages [12] -->
微信号：MATHmodels

<!-- b000341 | prose | pages [12] -->
rather than assuming that every location within an entire region is equally affected by extreme weather.

<!-- b000342 | prose | pages [12] -->
Setting the distance of a house from the disaster site as dI, for each house we can get a new external risk RE′

<!-- b000343 | prose | pages [12] -->
O

<!-- b000344 | prose | pages [12] -->
RE′

<!-- b000345 | prose | pages [12] -->
O = RE

<!-- b000346 | prose | pages [12] -->
O × f(dI) (18)

<!-- b000347 | prose | pages [12] -->
Where f(dI) is a function of dI and the probability of an area being insured.

<!-- b000348 | prose | pages [12] -->
The function f(d) is obtained by taking 30 points in [0,3] and performing 1000 Monte Carlo samples, taking the frequency of p > 0 as the probability that the corresponding location can purchase insurance, and then performing a regression method by least squares. Setting f(dI) = a + b ∗ln(dI), the regression yields f(dI) = 0.5454 + 0.0874 ∗ ln(dI), and the residual sum of squares SSE 0.008, which can be regarded as a better ﬁt. The function image is shown in Fig5.

<!-- b000349 | caption | pages [12] -->
Figure 5: Graph of the function f(dI)

<!-- b000350 | prose | pages [12] -->
5.2

<!-- b000351 | heading | pages [12] -->
Model of Property Decisions

<!-- b000352 | prose | pages [12] -->
In order to better evaluate how to choose a construction site in a certain area, we assume that the shape of the area is a rectangle with length m and width n.The lower-关注数学模型

<!-- b000353 | furniture | pages [12] -->
2

<!-- b000354 | furniture | pages [12] -->
MATHmodels

<!-- b000355 | furniture | pages [12] -->
获取更多资讯

<!-- b000356 | furniture | pages [13] -->
Team # 2410889

<!-- b000357 | furniture | pages [13] -->
Page 13 of 23

<!-- b000358 | prose | pages [13] -->
left corner of the rectangle is taken as the origin of the Cartesian coordinate system.

<!-- b000359 | prose | pages [13] -->
(1) Measurement of Living Convenience

<!-- b000360 | prose | pages [13] -->
The convenience of living can be measured by the distance of the property from the

<!-- b000361 | prose | pages [13] -->
微信公众号：数学模型

<!-- b000362 | prose | pages [13] -->
living service area. We set the distance between the house and the living service area as dL. In general, the radius of the living service area is 2km, and the area beyond 2km can be considered as unable to enjoy the convenience brought by this living service area. Within 2km, the enjoyment of convenience has a linear monotonically decreasing trend with increasing distance. Therefore, we can get a functional expression for dL

<!-- b000363 | prose | pages [13] -->


<!-- b000364 | prose | pages [13] -->
−dL

<!-- b000365 | prose | pages [13] -->


<!-- b000366 | prose | pages [13] -->
0 ≤dL ≤2 2 + 1,

<!-- b000367 | prose | pages [13] -->
g(dL) =

<!-- b000368 | prose | pages [13] -->


<!-- b000369 | prose | pages [13] -->
(19)

<!-- b000370 | prose | pages [13] -->
dL > 2 0,

<!-- b000371 | heading | pages [13] -->
(2) Building Models based on Goal Planning

<!-- b000372 | prose | pages [13] -->
Real estate developers need to consider both the degree of housing security as well as the degree of amenity when making decisions, which serve as the evaluation dimen- sions of housing satisfaction. Here we set the degree of housing security as IS, which

<!-- b000373 | prose | pages [13] -->
微信号：MATHmodels

<!-- b000374 | prose | pages [13] -->
can be measured by the function f(dI). This is because the higher the probability that an insurance company is willing to underwrite an area, it can indicate to a certain ex- tent that the place has a higher degree of security. Set the ease of living as RS, which can be measured by the function g(dL). That is

<!-- b000375 | prose | pages [13] -->
IS = f(dI), RS = g(dL) (20)

<!-- b000376 | prose | pages [13] -->
Given (x, y) as the location coordinates of the property under consideration for con- struction, (xi, yi) as the location coordinates of the disaster site i, and (xj, yj) as the location coordinates of the living service area j. Then we can get

<!-- b000377 | prose | pages [13] -->
p

<!-- b000378 | prose | pages [13] -->
(x −xi)2 + (y −yi)2

<!-- b000379 | prose | pages [13] -->
dIi =

<!-- b000380 | prose | pages [13] -->
q

<!-- b000381 | prose | pages [13] -->
(21) (x −xj)2 + (y −yj)2

<!-- b000382 | prose | pages [13] -->
dLj =

<!-- b000383 | prose | pages [13] -->
There may be more than one disaster site and life service area in an area, and we need to calculate the distance between the construction site and the nearest disaster site and life service area. Let dImin = mindIi and dLmin = mindLj.

<!-- b000384 | prose | pages [13] -->
For property developers, the higher the housing security and the higher the ease of living in a place, the more suitable it is to build properties in that place. We consider these two indicators to be equally important, which means that the weights are equal.

<!-- b000385 | prose | pages [13] -->
With the above, we can get a target planning model

<!-- b000386 | prose | pages [13] -->
0.5 ∗IS+0.5 ∗RS = 0.5f(dImin) + 0.5g(dLmin) Max

<!-- b000387 | prose | pages [13] -->


<!-- b000388 | prose | pages [13] -->
0 ≤x ≤m

<!-- b000389 | prose | pages [13] -->
   

<!-- b000390 | prose | pages [13] -->
0 ≤y ≤n

<!-- b000391 | prose | pages [13] -->
s.t.

<!-- b000392 | prose | pages [13] -->


<!-- b000393 | prose | pages [13] -->
x̸ = xi,j

<!-- b000394 | prose | pages [13] -->
  

<!-- b000395 | prose | pages [13] -->
y̸ = yI,j

<!-- b000396 | prose | pages [13] -->
5.3

<!-- b000397 | heading | pages [13] -->
Model Effect Demonstration

<!-- b000398 | prose | pages [13] -->
(22)

<!-- b000399 | prose | pages [13] -->
We derive the optimal construction location within a region by particle swarm al-

<!-- b000400 | prose | pages [13] -->
[5], which is displayed as follows.关注数学模型

<!-- b000401 | prose | pages [13] -->
gorithm. We show the partial solution by rasterization

<!-- b000402 | furniture | pages [13] -->
2

<!-- b000403 | furniture | pages [13] -->
MATHmodels

<!-- b000404 | furniture | pages [13] -->
获取更多资讯

<!-- b000405 | furniture | pages [14] -->
Team # 2410889

<!-- b000406 | furniture | pages [14] -->
Page 14 of 23

<!-- b000407 | prose | pages [14] -->
微信公众号：数学模型

<!-- b000408 | caption | pages [14] -->
Figure 6: Partial Results of the UD-GPM

<!-- b000409 | prose | pages [14] -->
微信号：MATHmodels

<!-- b000410 | prose | pages [14] -->
In the picture, the closer the color is to green indicates a higher level of satisfaction and the closer the color is to red indicates a lower level of satisfaction. The highest review scores are located at coordinates (1.2,0.4) in the image, so consider building your property here.

<!-- b000411 | prose | pages [14] -->
The optimal building location is further away from extreme weather events. In order to save on construction costs, there is no need to build with expensive, highly disaster-resistant building materials. If the construction site is closer to the extreme weather event site, it is necessary to use highly disaster-resistant construction for safety reasons. When the satisfaction level is less than 0.5, it is not recommended to build in this location because it is less secure and less convenient to live in.

<!-- b000412 | heading | pages [14] -->
Protection Value Assessment Model

<!-- b000413 | prose | pages [14] -->
6

<!-- b000414 | prose | pages [14] -->
Under the assumption of rational economic agents, some buildings with cultural or community signiﬁcance may be considered unworthy of resource allocation for preser- vation due to their inability to generate apparent economic beneﬁts. However, in real life, we should not solely consider economic interests but also take into account vari- ous factors such as social and cultural aspects, seeking a balance of various interests. Therefore, we have constructed a conservation value assessment model that includes four indicators: Culture, History, Economics, and Community. We employ the EWM- TOPSIS method to determine the conservation value of buildings, categorizing it into four levels and proposing different preservation measures for each level.

<!-- b000415 | prose | pages [14] -->
6.1

<!-- b000416 | heading | pages [14] -->
Discussion of Indicators

<!-- b000417 | prose | pages [14] -->
The worthiness of preserving a building should involve considering multiple val- ues and ﬁnding a point of balance among these interests. Hence, we have set four in- dicators: Culture, History, Economics, and Community, each with two sub-indicators as follows

<!-- b000418 | prose | pages [14] -->
关注数学模型

<!-- b000419 | furniture | pages [14] -->
2

<!-- b000420 | furniture | pages [14] -->
MATHmodels

<!-- b000421 | furniture | pages [14] -->
获取更多资讯

<!-- b000422 | furniture | pages [15] -->
Team # 2410889

<!-- b000423 | furniture | pages [15] -->
Page 15 of 23

<!-- b000424 | prose | pages [15] -->
微信公众号：数学模型

<!-- b000425 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000426 | caption | pages [15] -->
Figure 7: Indicator Display Chart

<!-- b000427 | prose | pages [15] -->
(1) Culture

<!-- b000428 | prose | pages [15] -->
Culture is one of the key factors in assessing the importance and value of a building. The sub-indicators are Cultural Activities Numbers (CAN) and Inclusiveness (INC).

<!-- b000429 | prose | pages [15] -->
A higher quantity of cultural activities indicates that the building holds greater cul- tural signiﬁcance and contributes to the development of local culture. Inclusivity is measured by the number of tourists from different countries. The more diverse the tourists a building attracts, the broader its cultural inﬂuence is considered, facilitat- ing shared experiences and interactions among people from different cultural back- grounds.

<!-- b000430 | prose | pages [15] -->
(2) History

<!-- b000431 | prose | pages [15] -->
Some buildings may be closely related to signiﬁcant historical events, famous ﬁg- ures, or speciﬁc time periods, and their historical signiﬁcance should be taken into account. In this regard, we select the sub-indicators of the Era of Construction ((EOC)) and the Major Historical Events (MHE).

<!-- b000432 | prose | pages [15] -->
The age of a building reﬂects its historical and traditional value, with older build- ings typically possessing deeper historical backgrounds and cultural heritage. A build- ing that is closely associated with more signiﬁcant historical events holds greater his- torical signiﬁcance for the region.

<!-- b000433 | prose | pages [15] -->
(3) Economics

<!-- b000434 | prose | pages [15] -->
The economic value of a building can directly impact its societal status and role, subsequently inﬂuencing its overall value. Here, we use two sub-indicators for mea- surement: Tourism Revenue (TR) and Popularity (POP).

<!-- b000435 | prose | pages [15] -->
If a building positively affects the local tourism industry and attracts a large num- ber of visitors, it is considered to have higher economic value. Moreover, a widely recognized building may attract more tourists and investments, thus generating more economic beneﬁts. Popularity is quantiﬁed using Google search index. A building with a higher search index is considered to have greater popularity.

<!-- b000436 | prose | pages [15] -->
(4) Communities 关注数学模型

<!-- b000437 | furniture | pages [15] -->
2

<!-- b000438 | furniture | pages [15] -->
MATHmodels

<!-- b000439 | furniture | pages [15] -->
获取更多资讯

<!-- b000440 | furniture | pages [16] -->
Team # 2410889

<!-- b000441 | furniture | pages [16] -->
Page 16 of 23

<!-- b000442 | prose | pages [16] -->
The community signiﬁcance of a building lies in fostering emotional connections among people, holding signiﬁcant social value. In this context, we employ two sub- indicators for measurement: Per Capita Length of Stay (PCL) and Flow of People (FOP).

<!-- b000443 | prose | pages [16] -->
微信公众号：数学模型

<!-- b000444 | prose | pages [16] -->
A longer average dwell time at a building promotes interpersonal communication and a sense of belonging. Higher foot trafﬁc means that people have more opportuni- ties to interact, enriching emotional connections.

<!-- b000445 | prose | pages [16] -->
Scoring based on the EWM-TOPSIS 6.2

<!-- b000446 | prose | pages [16] -->
The Entropy Weight Method (EWM) is an objective approach for determining the weights of multiple indicators. It utilizes the concept of information entropy to cal- culate the weight of each indicator. TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) is a multi-criteria decision analysis method used to deter- mine the best choice by comparing the similarity of each alternative to the ideal and

<!-- b000447 | prose | pages [16] -->
微信号：MATHmodels

<!-- b000448 | prose | pages [16] -->
worst solutions. In this context, we use the EWM method to assign weights to each in- dicator and then apply the TOPSIS method to assess the conservation value of different locations.

<!-- b000449 | prose | pages [16] -->
(1) Normalize the original score matrix.

<!-- b000450 | prose | pages [16] -->
Since all our indicators are of the maximization type, there is no need for normal- ization. However, the indicators may have different scales and ranges, so we use the Min-Max method to map the score Xij of location i under indicator j to the range [0, 1]:

<!-- b000451 | prose | pages [16] -->
st_Xij = Xij −Xj,max

<!-- b000452 | prose | pages [16] -->
(23)

<!-- b000453 | prose | pages [16] -->
Xj,max −Xj,min

<!-- b000454 | prose | pages [16] -->
(2) Determine the weights using the EWM method.

<!-- b000455 | prose | pages [16] -->
Let pij represent the probability of occurrence of Xij. Then, we can calculate the information entropy H(Xj) and the weight Wj for indicator Xj as follows:

<!-- b000456 | prose | pages [16] -->
st_Xij Pn pij =

<!-- b000457 | prose | pages [16] -->
i=1 st_Xij

<!-- b000458 | prose | pages [16] -->
n X

<!-- b000459 | prose | pages [16] -->
H(Xj) = −1

<!-- b000460 | prose | pages [16] -->
Wj = 1 −

<!-- b000461 | prose | pages [16] -->
(3) Obtain the weighted score matrix Z:

<!-- b000462 | prose | pages [16] -->
pij ln(pij)

<!-- b000463 | prose | pages [16] -->
(24)

<!-- b000464 | prose | pages [16] -->
ln n

<!-- b000465 | prose | pages [16] -->
j=1

<!-- b000466 | prose | pages [16] -->
H(Xj) Pn

<!-- b000467 | prose | pages [16] -->
j=1 1 −Hj

<!-- b000468 | prose | pages [16] -->
Z = (zij)m × n = (st_XijWj)m×n (25)

<!-- b000469 | prose | pages [16] -->
(4) Determine the conservation value of locations using TOPSIS.

<!-- b000470 | prose | pages [16] -->
i and the worst solution as D−

<!-- b000471 | prose | pages [16] -->
Deﬁne the best solution as D+

<!-- b000472 | prose | pages [16] -->
i , with the conserva- tion value score for the ith location as Si. Alternatives that are closer to the best solution are considered optimal:

<!-- b000473 | prose | pages [16] -->
关注数学模型

<!-- b000474 | furniture | pages [16] -->
2

<!-- b000475 | furniture | pages [16] -->
MATHmodels

<!-- b000476 | furniture | pages [16] -->
获取更多资讯

<!-- b000477 | furniture | pages [17] -->
Team # 2410889

<!-- b000478 | prose | pages [17] -->
Z+

<!-- b000479 | prose | pages [17] -->
j = max(Z+

<!-- b000480 | prose | pages [17] -->
1 , Z+ 2 , . . . ,Z+

<!-- b000481 | prose | pages [17] -->
v u u t

<!-- b000482 | prose | pages [17] -->
D+

<!-- b000483 | prose | pages [17] -->
i =

<!-- b000484 | furniture | pages [17] -->
Page 17 of 23

<!-- b000485 | prose | pages [17] -->
Z−

<!-- b000486 | prose | pages [17] -->
j = min(Z−

<!-- b000487 | prose | pages [17] -->
1 , Z− 2 , . . . , Z−

<!-- b000488 | prose | pages [17] -->
m),

<!-- b000489 | prose | pages [17] -->
m)

<!-- b000490 | prose | pages [17] -->
m X

<!-- b000491 | prose | pages [17] -->
(Z+

<!-- b000492 | prose | pages [17] -->
j −zij)2

<!-- b000493 | prose | pages [17] -->
微信公众号：数学模型

<!-- b000494 | prose | pages [17] -->
v u u t

<!-- b000495 | prose | pages [17] -->
D−

<!-- b000496 | prose | pages [17] -->
i =

<!-- b000497 | prose | pages [17] -->
Si =

<!-- b000498 | prose | pages [17] -->
D+

<!-- b000499 | prose | pages [17] -->
j=1

<!-- b000500 | prose | pages [17] -->
(26)

<!-- b000501 | prose | pages [17] -->
m X

<!-- b000502 | prose | pages [17] -->
(Z−

<!-- b000503 | prose | pages [17] -->
j −zij)2

<!-- b000504 | prose | pages [17] -->
j=1

<!-- b000505 | prose | pages [17] -->
D+

<!-- b000506 | prose | pages [17] -->
i

<!-- b000507 | prose | pages [17] -->
i + D−

<!-- b000508 | prose | pages [17] -->
i

<!-- b000509 | prose | pages [17] -->
The weights for each indicator are shown in the following chart 8.

<!-- b000510 | prose | pages [17] -->
微信号：MATHmodels

<!-- b000511 | caption | pages [17] -->
Figure 8: Indicator weighting charts

<!-- b000512 | prose | pages [17] -->
We collected data for various landmarks and conducted conservation value assess- ments. Based on the scores, we categorized them into four protection levels: No pro- tection, Primary protection, Secondary protection, and Tertiary protection, as shown in the ﬁgure 9.

<!-- b000513 | caption | pages [17] -->
Figure 9: Classiﬁcation of Protection Levels

<!-- b000514 | prose | pages [17] -->
Protection Measures Under Each Level 6.3

<!-- b000515 | prose | pages [17] -->
For buildings that fall into the "No Protection" level, we consider them to have no conservation value and do not recommend any protection measures. However, for buildings that fall into the protection levels, the intensity of protection measures should increase with the higher protection level, and the cost will also increase accord- ingly. Therefore, buildings with lower protection levels should not adopt advanced关注数学模型

<!-- b000516 | furniture | pages [17] -->
2

<!-- b000517 | furniture | pages [17] -->
MATHmodels

<!-- b000518 | furniture | pages [17] -->
获取更多资讯

<!-- b000519 | furniture | pages [18] -->
Team # 2410889

<!-- b000520 | furniture | pages [18] -->
Page 18 of 23

<!-- b000521 | prose | pages [18] -->
protection measures, while those with higher protection levels can consider higher- cost advanced protection measures.

<!-- b000522 | prose | pages [18] -->
The protection measures are as follows:

<!-- b000523 | prose | pages [18] -->
微信公众号：数学模型

<!-- b000524 | prose | pages [18] -->
微信号：MATHmodels

<!-- b000525 | caption | pages [18] -->
Figure 10: Protection measures under each level

<!-- b000526 | prose | pages [18] -->
For buildings falling into the "Primary Protection " category, we recommend the following protection measures:

<!-- b000527 | prose | pages [18] -->
• Regular Maintenance and Repairs: Close the building to the public for one day every month and invite professional architects, engineers, and conservation ex- perts to conduct a comprehensive inspection and assessment of the building to identify potential issues and areas in need of repair. Any damage found should be promptly addressed. • Conduct Conservation Awareness Lectures: Organize conservation awareness lectures to increase people’s awareness of the landmark’s preservation. During these lectures, emphasize the importance of sustainability and encourage people to recognize themselves as both beneﬁciaries and protectors of the landmark, motivating their active involvement in its preservation. • Manage Visitor Flow: Implement a reservation system for visits, restricting the number of visitors during each time slot to reduce overcrowding within the land- mark and prevent potential damage due to congestion.

<!-- b000528 | prose | pages [18] -->
For buildings falling into the "Secondary Protection " category, we recommend the following protection measures:

<!-- b000529 | prose | pages [18] -->
• Restrict Surrounding Development: Deﬁne the permissible development range and construction intensity limits in the vicinity of the landmark. Each company’s construction intensity should not exceed the speciﬁed limit to reduce noise and vibrations caused by nearby development and prevent damage to the building’s structure. • Establish Controlled Zones: Divide the area into two zones: the Core Zone and the Buffer Zone. The Core Zone, which contains the most important, sensitive, and fragile parts of the site, should be off-limits to general tourists and only ac- cessible to professional archaeologists or heritage conservation personnel. The Buffer Zone, located farther from the Core Zone, is relatively open but still sub- ject to certain regulations, such as prohibiting the indiscriminate placement of objects or littering.

<!-- b000530 | prose | pages [18] -->
For buildings falling into the "Tertiary Protection " category, we recommend the following protection measures:

<!-- b000531 | prose | pages [18] -->
关注数学模型

<!-- b000532 | furniture | pages [18] -->
2

<!-- b000533 | furniture | pages [18] -->
MATHmodels

<!-- b000534 | furniture | pages [18] -->
获取更多资讯

<!-- b000535 | furniture | pages [19] -->
Team # 2410889

<!-- b000536 | furniture | pages [19] -->
Page 19 of 23

<!-- b000537 | prose | pages [19] -->
• Legal and Regulatory Protection: Designate the building as a national or local cultural heritage site and establish corresponding protection policies and mea- sures. Additionally, stipulate that all construction activities in the surrounding area require government approval and guidance.

<!-- b000538 | prose | pages [19] -->
微信公众号：数学模型

<!-- b000539 | prose | pages [19] -->
• Digital Twin Protection: Use digital technology to create a virtual 3D model of the building, input its data into a Building Information Model (BIM), and con- duct simulations and testing in a virtual environment. This approach provides a better understanding of the building’s structure, materials, and history, facilitat- ing more precise planning for maintenance and restoration work. • Relocation: For landmarks located in high-risk areas, consider relocating them to a safer location to reduce the risk of damage.

<!-- b000540 | prose | pages [19] -->
7 Case Study: the Forbidden City

<!-- b000541 | prose | pages [19] -->
We choose the Forbidden City in Bejing, China, for our study because it is one of

<!-- b000542 | prose | pages [19] -->
微信号：MATHmodels

<!-- b000543 | prose | pages [19] -->
the most important and inﬂuential historical landmarks in China and has experienced a large number of extreme weather events. There was also a rainstorm event in Beijing in July 2023 with an initial reported loss of 166 million RMB. Assessing the value of the Forbidden City using the Proﬁt Underwriting Model and the Protection Value Scoring Model is important for the sustainable development of the Forbidden City and can provide managers with relevant conservation measures.

<!-- b000544 | prose | pages [19] -->
7.1

<!-- b000545 | heading | pages [19] -->
Underwriting Decision Model

<!-- b000546 | prose | pages [19] -->
Collect the relevant data of the Forbidden City, substitute the data into the un- derwriting decision model, and perform 100 Monte Carlo sampling simulations. The results obtained are shown in Fig11.

<!-- b000547 | caption | pages [19] -->
Figure 11: Underwriting Decision Modeling Results for the Forbidden City

<!-- b000548 | prose | pages [19] -->
From the picture, it can be known that there are more points with proﬁtP > 0 and the frequency is 61%. It can be assumed that the insurance company has a greater willingness to underwrite in Beijing, and the probability that the Forbidden City can关注数学模型

<!-- b000549 | furniture | pages [19] -->
2

<!-- b000550 | furniture | pages [19] -->
MATHmodels

<!-- b000551 | furniture | pages [19] -->
获取更多资讯

<!-- b000552 | furniture | pages [20] -->
Team # 2410889

<!-- b000553 | furniture | pages [20] -->
Page 20 of 23

<!-- b000554 | prose | pages [20] -->
enjoy the insurance service is higher. The security of the Forbidden City is higher and has a higher value of sustainable development.

<!-- b000555 | prose | pages [20] -->
微信公众号：数学模型

<!-- b000556 | heading | pages [20] -->
Protection Value Assessment Model

<!-- b000557 | prose | pages [20] -->
7.2

<!-- b000558 | prose | pages [20] -->
Inputting the data of cultural, historical, economic and community dimensions of the Forbidden City into the protection value assessment model, we get its protection value of 0.618, which belongs to the third level of protected buildings. Compare the Forbidden City with Mogao Grottoes and Canton Tower for some data, as shown in the table2

<!-- b000559 | caption | pages [20] -->
Table 2: Historic Landmarks Partial Raw Data

<!-- b000560 | prose | pages [20] -->
Cultural Activities

<!-- b000561 | prose | pages [20] -->
Era of Construction Inclusiveness Number

<!-- b000562 | prose | pages [20] -->
the Forbidden City 78 112 the Mogao caves 16 12 Canton Tower 23 52

<!-- b000563 | prose | pages [20] -->
Tourism Revenue Popularity Flow of People Score

<!-- b000564 | prose | pages [20] -->
604 2,300,000,000 3817 3,0000 0.618 1658 5,000,000 1696 2,000 0.364 15 800,000,000 2297 15,000 0.215

<!-- b000565 | prose | pages [20] -->
We can ﬁnd that the Forbidden City is far more inclusive, well-known and crowded

<!-- b000566 | prose | pages [20] -->
微信号：MATHmodels

<!-- b000567 | prose | pages [20] -->
than Mogao Grottoes and Canton Tower. Although the Mogao Caves have the longest history of continuation, they are geographically remote and have a lower economic value. The Forbidden City, on the other hand, is located in China’s capital city and has a high economic value due to its high visibility and the number of tourists from all over the world. In addition, the Forbidden City has a large number of cultural activities, such as an AR cloud tour of the Forbidden City, play theater in the Forbidden City, etc., to do the cultural heritage and high cultural value. Therefore, synthesizing the value of all aspects, the conservation value of Beijing is extremely high.

<!-- b000568 | prose | pages [20] -->
Taking into account the current conservation status of the Forbidden City, we pro- vide managers with the following conservation recommendations according to its con- servation level.

<!-- b000569 | prose | pages [20] -->
(1) Conduct conservation publicity lectures

<!-- b000570 | prose | pages [20] -->
Tell the story of the history of the Forbidden City, such as the major historical events that happened in each location during the various dynasties in history, and then increase people’s motivation to protect the landmarks of the Forbidden City.

<!-- b000571 | prose | pages [20] -->
(2) Control the ﬂow of people

<!-- b000572 | prose | pages [20] -->
Implementing a reservation system for visits, limiting the number of people at each period to reduce crowding, and closing the museum on Sundays for main- tenance.

<!-- b000573 | prose | pages [20] -->
(3) Setting up control zones

<!-- b000574 | prose | pages [20] -->
Designate the most vulnerable part of the Forbidden City as the core zone, strictly static the entry of tourists, and allow tourists to visit only in the buffer zone.

<!-- b000575 | prose | pages [20] -->
(4) Digital twin conservation

<!-- b000576 | prose | pages [20] -->
Create a digital twin for the Forbidden City, where simulations and tests will be conducted to predict possible future dangers to take precautions.

<!-- b000577 | prose | pages [20] -->
关注数学模型

<!-- b000578 | furniture | pages [20] -->
2

<!-- b000579 | furniture | pages [20] -->
MATHmodels

<!-- b000580 | furniture | pages [20] -->
获取更多资讯

<!-- b000581 | furniture | pages [21] -->
Team # 2410889

<!-- b000582 | prose | pages [21] -->
8

<!-- b000583 | heading | pages [21] -->
Sensitivity Analysis

<!-- b000584 | furniture | pages [21] -->
Page 21 of 23

<!-- b000585 | prose | pages [21] -->
微信公众号：数学模型

<!-- b000586 | prose | pages [21] -->
(a) Florida (b) Guangdong

<!-- b000587 | caption | pages [21] -->
Figure 12: Impact of rate adjustments on results in two regions

<!-- b000588 | prose | pages [21] -->
微信号：MATHmodels

<!-- b000589 | prose | pages [21] -->
We conducted a sensitivity analysis on the insurance model to verify its stability and to ascertain whether the model would be susceptible to various factors. We ad- justed the interest rates on insurance company investments within a range of 2% to 7% to observe whether different interest rate conditions would affect the insurance com- pany’s decision to conduct business in a given area. We conducted experiments in Guangdong and Florida, the results indicated that changes in interest rates have mini- mal impact on the decisions of insurance companies. Therefore, we believe our model is stable and capable of addressing real-world problems.

<!-- b000590 | caption | pages [21] -->
Figure 13: Impact of rate adjustments on the model

<!-- b000591 | prose | pages [21] -->
Additionally, we conducted a sensitivity analysis on the conservation model, utiliz- ing data from the Forbidden City. By altering the values of various primary indicators, we observed changes in the scoring system, with the historical indicator showing the largest variation at 5% and the cultural indicator the smallest at 1%. The results in- dicate that changing a single indicator does not signiﬁcantly affect the overall score. Our model effectively measures the comprehensive value of a building from multiple dimensions.

<!-- b000592 | prose | pages [21] -->
关注数学模型

<!-- b000593 | furniture | pages [21] -->
2

<!-- b000594 | furniture | pages [21] -->
MATHmodels

<!-- b000595 | furniture | pages [21] -->
获取更多资讯

<!-- b000596 | furniture | pages [22] -->
Team # 2410889

<!-- b000597 | prose | pages [22] -->
9

<!-- b000598 | heading | pages [22] -->
Strengths and Weaknesses

<!-- b000599 | prose | pages [22] -->
9.1

<!-- b000600 | heading | pages [22] -->
Strengths

<!-- b000601 | furniture | pages [22] -->
Page 22 of 23

<!-- b000602 | prose | pages [22] -->
微信公众号：数学模型

<!-- b000603 | prose | pages [22] -->
• Our underwriting decision model takes into account the real needs of insurance companies, making decisions driven by proﬁt to ensure the long-term health of the insurance company. It also allocates the premiums received by the insurance company reasonably, considering the reinsurance decisions for risk diversiﬁca- tion. • By using a large number of samples in the Monte Carlo simulation, it realisti- cally replicates the actual insurance scenarios, resulting in high credibility of the outcomes. • Our underwriting decision model separately considers and calculates internal and external risks, allowing for a more comprehensive assessment of a policy’s risk. • We provide targeted protection measures for buildings of different protection

<!-- b000604 | prose | pages [22] -->
微信号：MATHmodels

<!-- b000605 | prose | pages [22] -->
levels, ensuring that the intensity of protection is matched with the cost and value of the buildings.

<!-- b000606 | prose | pages [22] -->
9.2

<!-- b000607 | heading | pages [22] -->
Weaknesses

<!-- b000608 | prose | pages [22] -->
• The assessment of external risks relies too heavily on data from extreme weather events, lacking assessment of external risks from other dimensions. • We use the entropy weighting method to determine the weights of indicators, but most of the data collected is from China, without gathering data from other international landmarks. Therefore, when assessing the value of buildings in other countries, our model needs more data to ensure a more accurate evaluation. • Our protection value assessment model does not consider indicators compre- hensively enough and could further distinguish between different dimensions to more accurately measure a building’s comprehensive value in cultural, historical, economic, and social aspects.

<!-- b000609 | prose | pages [22] -->
关注数学模型

<!-- b000610 | furniture | pages [22] -->
2

<!-- b000611 | furniture | pages [22] -->
MATHmodels

<!-- b000612 | furniture | pages [22] -->
获取更多资讯

<!-- b000613 | furniture | pages [23] -->
Team # 2410889

<!-- b000614 | heading | pages [23] -->
References

<!-- b000615 | furniture | pages [23] -->
Page 23 of 23

<!-- b000616 | references | pages [23] -->
[1] Mora, S., Keipi, K. Disaster risk management in development projects: models

<!-- b000617 | references | pages [23] -->
微信公众号：数学模型

<!-- b000618 | references | pages [23] -->
and checklists[J].˘aBull Eng Geol Environ˘a65, 155165 (2006)

<!-- b000619 | references | pages [23] -->
[2] Shuang Wu, Xilian Deng. Corporate Diversiﬁcation, Ownership, and Solvency

<!-- b000620 | references | pages [23] -->
in Chinas Property-Liability Insurance Companies[J]. ˘aMathematical Problems in

<!-- b000621 | references | pages [23] -->
Engineering. vol. 2021, Article ID 1562771, 9 pages, 2021.

<!-- b000622 | references | pages [23] -->
https://www.climate.gov/

<!-- b000623 | references | pages [23] -->
[3]

<!-- b000624 | references | pages [23] -->
[4] Rui Wang. Study on optimal operation of distribution network considering ex-

<!-- b000625 | references | pages [23] -->
treme weather and mobile energy storage ﬂexibility[D].North China Electric

<!-- b000626 | references | pages [23] -->
Power University (Beijing),2023

<!-- b000627 | references | pages [23] -->
[5] Yuan, C., Ye, Y., Tang, C.˘aet al.˘aAccuracy comparison of gridded historical culti-

<!-- b000628 | references | pages [23] -->
vated land data in Jiangsu and Anhui provinces[J].˘aChin. Geogr. Sci.˘a27, 273285

<!-- b000629 | references | pages [23] -->
微信号：MATHmodels

<!-- b000630 | references | pages [23] -->
(2017)

<!-- b000631 | references | pages [23] -->
https://data.stats.gov.cn/index.htm

<!-- b000632 | references | pages [23] -->
[6]

<!-- b000633 | references | pages [23] -->
https://www.gddat.cn/newGlobalWeb/#/home

<!-- b000634 | references | pages [23] -->
[7]

<!-- b000635 | references | pages [23] -->
https://www.ncdc.noaa.gov/stormevents/

<!-- b000636 | references | pages [23] -->
[8]

<!-- b000637 | references | pages [23] -->
关注数学模型

<!-- b000638 | furniture | pages [23] -->
2

<!-- b000639 | furniture | pages [23] -->
MATHmodels

<!-- b000640 | furniture | pages [23] -->
获取更多资讯

<!-- b000641 | furniture | pages [24] -->


<!-- b000642 | references | pages [24] -->
Dear Community Members:

<!-- b000643 | references | pages [24] -->
We are Insurance of Catastrophes Modelers, with our primary research focus on the sustainability

<!-- b000644 | references | pages [24] -->
of the property insurance industry. Today, we are reaching out to share the insights derived from

<!-- b000645 | references | pages [24] -->
applying our insurance and preservation models to the Forbidden City in Beijing. As one of the most

<!-- b000646 | references | pages [24] -->
significant historical landmarks in Beijing and across China, this endeavor is pivotal for

<!-- b000647 | references | pages [24] -->
微信公众号：数学模型

<!-- b000648 | references | pages [24] -->
understanding the Forbidden City's value, its risk exposures, and the steps necessary to ensure its

<!-- b000649 | references | pages [24] -->
future sustainability.

<!-- b000650 | references | pages [24] -->
Our insurance decision model, which involved Monte Carlo simulations using collected data,

<!-- b000651 | references | pages [24] -->
indicated a high probability of willingness to provide insurance, with a profit point frequency of 61%.

<!-- b000652 | references | pages [24] -->
This high likelihood of insurance coverage in this area is due to a combination of factors, such as the

<!-- b000653 | references | pages [24] -->
relatively low frequency of extreme weather events and the lower height of buildings. This not only

<!-- b000654 | references | pages [24] -->
bolsters our confidence in the sustainable protection of the Forbidden City but also reveals certain

<!-- b000655 | references | pages [24] -->
risks from the perspective of insurance companies.

<!-- b000656 | references | pages [24] -->
Furthermore, our preservation value assessment model has classified the Forbidden City as a

<!-- b000657 | references | pages [24] -->
Level Three protected structure, with a protection value of 0.618. This is the highest protection value

<!-- b000658 | references | pages [24] -->
achieved by our evaluation model so far, attributed to the Forbidden City's central location in the

<!-- b000659 | references | pages [24] -->
capital, the influx of global visitors, and its significant economic contributions.

<!-- b000660 | references | pages [24] -->
微信号：MATHmodels

<!-- b000661 | references | pages [24] -->
In light of these findings, we recommend the following plan for the protection and enhancement

<!-- b000662 | references | pages [24] -->
of the Forbidden City:

<!-- b000663 | references | pages [24] -->
1.Educational Initiatives: Launch educational programs and lectures to share the rich history of

<!-- b000664 | references | pages [24] -->
the Forbidden City, highlighting significant historical events across dynasties to foster a sense of

<!-- b000665 | references | pages [24] -->
responsibility and enthusiasm for its preservation.

<!-- b000666 | heading | pages [24] -->
2. Restricted Access Areas: Designate the most vulnerable areas of the Forbidden City as core

<!-- b000667 | prose | pages [24] -->
zones, strictly limiting visitor access and allowing public visitation only in buffer zones.

<!-- b000668 | heading | pages [24] -->
3. Digital Twin Technology: Develop a digital twin of the Forbidden City for simulation and

<!-- b000669 | prose | pages [24] -->
testing, to predict and prevent potential future risks. Additionally, we have outlined short-term and long-term risk mitigation measures to address the potential increase in extreme weather events in the future:

<!-- b000670 | prose | pages [24] -->
Short-term (1-3 years): Conduct periodic safety inspections and assess the structural integrity of buildings. Medium to long-term (3-10 years): Given that Beijing is prone to sandstorms, which can directly damage ancient buildings, we propose the establishment of the Forbidden City Forest Park in the northwest of Beijing, where sandstorms originate. Long-term (over 10 years): Continuously engage in scientific research and development, collaborating with research institutions to explore better measures for the preservation of cultural relics, minimizing the damage to artifacts from inevitable natural disasters. Regarding cost recommendations, we suggest that the Forbidden City allocate at least 60% of its annual net profit to implement the above plans. Strong financial support will ensure the high-quality execution of these initiatives. This plan aims not only to protect the Forbidden City but also to enhance its value as a cultural heritage for future generations to cherish.

<!-- b000671 | prose | pages [24] -->
We look forward to further discussions with you and the community to ensure that the Forbidden City remains a treasured landmark for centuries to come.

<!-- b000672 | prose | pages [24] -->
Sincerely

<!-- b000673 | furniture | pages [24] -->
Team #2410889

<!-- b000674 | prose | pages [24] -->
关注数学模型

<!-- b000675 | furniture | pages [24] -->
2

<!-- b000676 | furniture | pages [24] -->
MATHmodels

<!-- b000677 | furniture | pages [24] -->
获取更多资讯
