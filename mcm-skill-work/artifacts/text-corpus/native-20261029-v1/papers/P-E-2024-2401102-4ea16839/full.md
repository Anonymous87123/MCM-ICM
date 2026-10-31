# P-E-2024-2401102-4ea16839

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Problem Chosen

<!-- b000002 | furniture | pages [1] -->
2024

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | prose | pages [1] -->
MCM/ICM

<!-- b000005 | title | pages [1] -->
E

<!-- b000006 | furniture | pages [1] -->
2401102

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
In Face of Increasingly Severe Extreme Weather:

<!-- b000009 | title | pages [1] -->
Sustainable Property Insurance under Risk

<!-- b000010 | title | pages [1] -->
微信公众号：数学模型

<!-- b000011 | heading | pages [1] -->
Summary

<!-- b000012 | prose | pages [1] -->
The first priority of survival is getting protection from the extreme weather. —Bear Grylls

<!-- b000013 | prose | pages [1] -->
More frequent and severe extreme weather events are causing greater damage to people’s prop- erty, leading to a reevaluation of the sustainability of insurance companies. On one hand, maintaining enough customers for long-term healthy operation is crucial; on the other hand, avoiding excessively high compensation risks to remain profitable is essential. Therefore, we assessed the sustainability of the insurance sector in areas that were frequently impacted by extreme weather events from two per- spectives: insurance demand and total risk.

<!-- b000014 | title | pages [1] -->
微信号：MATHmodels

<!-- b000015 | prose | pages [1] -->
For Task 1, we developed a Property Insurance Posture Model for insurance companies. We categorized extreme weather into 4 types and used an ARIMA model to forecast the future risk of extreme weather for each region-disaster pair, and calculated the expected loss. Then, we used Lane’s AFC model to calculate premiums. To measure demand with premiums, we introduced the insurance demand curve. Finally, we established Demand-Risk Equilibrium Model for Insurance(DBMI) to provide decisions on whether to underwrite insurance in specific regions.

<!-- b000016 | prose | pages [1] -->
Next, we applied the model above to Australia and Southeast Asia, where approximately 60 years of data from 3000 records were available. Then we applied ARIMA model on selected area-event series, with an eminent fit: R2 consistently above 0.625, and IC all below 300. Consequently, we forecast the risks for 2024-2027. This has resulted in the determination of premiums ranging from $119.2 to $1295.6. The optimal solutions indicated that in Australia, QLD and WA should be underwritten; in SE Asia, PHL and THA.

<!-- b000017 | prose | pages [1] -->
For Task 2, we introduced Innovative Risk Prediction Property Development Method(IRPPDM), which integrated DBMI with real estate companies’ willingness index to construct a Willingness-Risk coordinate system. We specifically targeted High Risk-High Willingness areas, providing 3 possible risk reassessment methods to help transfer them into Low Risk-High Willingness category.

<!-- b000018 | prose | pages [1] -->
For Task 3, we used Historic Landmark Preservation Model to help community leaders. We estimated the significance of historic landmarks by AHP method considering 8 indicators in 4 dimen- sions. Then we offered suggestions considering both the extent of significance and predicted risks. According to our model, Temple of Literature in Hanoi, Vietnam had a score of 0.463, facing risks of floods and cyclones. Considering its features, we offered 4 tailored suggestions.

<!-- b000019 | prose | pages [1] -->
In the end, we stated the strengths and weaknesses of models. Based on their performances in application, Property Insurance Posture Model reasonably balanced demand and risk, and Historic Landmark Preservation Model was comprehensive in measuring value.

<!-- b000020 | keywords | pages [1] -->
Keywords: Extreme Weather Event; Property Insurance; ARIMA; Dual-objective Optimization; AHP

<!-- b000021 | furniture | pages [1] -->
关注数学模型

<!-- b000022 | furniture | pages [1] -->
2

<!-- b000023 | furniture | pages [1] -->
MATHmodels

<!-- b000024 | furniture | pages [1] -->
获取更多资讯

<!-- b000025 | furniture | pages [2] -->
Team # 2401102

<!-- b000026 | heading | pages [2] -->
Contents

<!-- b000027 | contents | pages [2] -->
1

<!-- b000028 | heading | pages [2] -->
Introduction

<!-- b000029 | furniture | pages [2] -->
Page 1 of 25

<!-- b000030 | prose | pages [2] -->
2 Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 2

<!-- b000031 | prose | pages [2] -->
微信公众号：数学模型

<!-- b000032 | prose | pages [2] -->
Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2

<!-- b000033 | prose | pages [2] -->
2

<!-- b000034 | heading | pages [2] -->
Assumptions and Notations

<!-- b000035 | prose | pages [2] -->
2

<!-- b000036 | prose | pages [2] -->
3

<!-- b000037 | heading | pages [2] -->
Model I: Property Insurance Posture Model

<!-- b000038 | prose | pages [2] -->
3 4 The Types of Extreme Weather Events . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 4 Predicting Extreme Weather Events: Based on ARIMA . . . . . . . . . . . . . . . . . 3.2 5 Series Stabilization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2.1 6 ARIMA Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2.2 6 Insurance Price and Demand . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.3 7 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.3.1 Two Types of Insurance 7 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.3.2 Price of Insurance 8

<!-- b000039 | prose | pages [2] -->
微信号：MATHmodels

<!-- b000040 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.3.3 Demand for Insurance 8 Demand-Risk Equilibrium Model for Insurance . . . . . . . . . . . . . . . . . . . . . 3.4

<!-- b000041 | prose | pages [2] -->
4 Case Study: Australia and Southeast Asia

<!-- b000042 | prose | pages [2] -->
9

<!-- b000043 | prose | pages [2] -->
10 Data Processing and Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 10 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2 Use of ARIMA Model 11 Apply DEMI to Two Areas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3 13 Determination of Premiums and Demand . . . . . . . . . . . . . . . . . . . . 4.3.1 13 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3.2 Solving DBMI 13

<!-- b000044 | prose | pages [2] -->
Innovative Risk Prediction Property Development Method 5 14 Whether to Build: Determined by Willingness and Risk . . . . . . . . . . . . . . . . . 5.1 15 How and Where to build: Addressing Specific Event Risk . . . . . . . . . . . . . . . . 5.2 16 Conclusion for IRPPDM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.3 17

<!-- b000045 | heading | pages [2] -->
Model II: Historic Landmark Preservation Model

<!-- b000046 | prose | pages [2] -->
6 17 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 Indicator Selection 6.2 Weight Calculation: Based on AHP 18 . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000047 | prose | pages [2] -->
18 Value Calculation and Extent Estimation . . . . . . . . . . . . . . . . . . . . . . . . . 6.3 20 Application: Temple of Literature in Hanoi, Vietnam . . . . . . . . . . . . . . . . . . 6.4

<!-- b000048 | prose | pages [2] -->
7

<!-- b000049 | heading | pages [2] -->
Strength and Weakness

<!-- b000050 | heading | pages [2] -->
References

<!-- b000051 | heading | pages [2] -->
Letter of Recommendation

<!-- b000052 | prose | pages [2] -->
21

<!-- b000053 | prose | pages [2] -->
22

<!-- b000054 | prose | pages [2] -->
23

<!-- b000055 | prose | pages [2] -->
24

<!-- b000056 | furniture | pages [2] -->
关注数学模型

<!-- b000057 | furniture | pages [2] -->
2

<!-- b000058 | furniture | pages [2] -->
MATHmodels

<!-- b000059 | furniture | pages [2] -->
获取更多资讯

<!-- b000060 | furniture | pages [3] -->
Team # 2401102

<!-- b000061 | prose | pages [3] -->
1

<!-- b000062 | heading | pages [3] -->
Introduction

<!-- b000063 | prose | pages [3] -->
1.1 Problem Background

<!-- b000064 | furniture | pages [3] -->
Page 2 of 25

<!-- b000065 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000066 | prose | pages [3] -->
Over the past few years, more than 1,000 extreme weather events have resulted in more than $1 trillion in global losses. Swiss Re predicted that losses from weather-related events in Australia, Canada, France, Germany, Japan, the U.K., and the U.S. could increase by 35-120 percent by 2040, due to the impact of natural disasters such as floods, hurricanes, and wildfires. [1]

<!-- b000067 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000068 | caption | pages [3] -->
Figure 1: Global Impact of Natural Disasters[2]

<!-- b000069 | prose | pages [3] -->
The frequent occurrence of extreme weather events presents a complex challenge for the property insurance industry. These events can lead to substantial financial losses due to increased claims, testing the industry’s resilience. Insurers must navigate the dual pressures of maintaining profitability and offering affordable premiums.

<!-- b000070 | prose | pages [3] -->
Therefore, there’s a growing need for risk assessment models that accurately reflect the high level risks associated with extreme weather events. This will help insurers to price policies more effectively and encourage investment in protective measures for properties at risk.

<!-- b000071 | prose | pages [3] -->
1.2 Our Work

<!-- b000072 | prose | pages [3] -->
For insurance companies, we have developed a property insurance deployment model to assist them in selecting the areas to underwrite against extreme weather events, ensuring the sustainability of their operations. Specifically, we measured sustainability based on the company’s total demand and the total risk they face: Demand reflected the consideration of profitability, while underwriting risk was related to long-term healthy operation. After the model was established, we applied it to two different regions to validate its feasibility.

<!-- b000073 | prose | pages [3] -->
For real estate developers, we extended the insurance model mentioned above to assist in the decision-making process for property development, providing insights on where, how, and whether

<!-- b000074 | furniture | pages [3] -->
关注数学模型

<!-- b000075 | furniture | pages [3] -->
2

<!-- b000076 | furniture | pages [3] -->
MATHmodels

<!-- b000077 | furniture | pages [3] -->
获取更多资讯

<!-- b000078 | furniture | pages [4] -->
Team # 2401102

<!-- b000079 | furniture | pages [4] -->
Page 3 of 25

<!-- b000080 | prose | pages [4] -->
to construct buildings. Specifically, using the weather risk predictions obtained from the insurance model, we provided corresponding strategies that developers could implement to mitigate risks during the construction of properties.

<!-- b000081 | prose | pages [4] -->
For community leaders without the shelter of extreme weather event insurance, we have developed

<!-- b000082 | prose | pages [4] -->
微信公众号：数学模型

<!-- b000083 | prose | pages [4] -->
a historical landmark significance model that assesses the significance of historical landmarks based on four aspects: history, culture, economy, and community. Ultimately, this helps them determine the extent of protection needed for their historical landmarks.

<!-- b000084 | prose | pages [4] -->
The detailed flowchart is illustrated in Figure 2 below:

<!-- b000085 | prose | pages [4] -->
微信号：MATHmodels

<!-- b000086 | caption | pages [4] -->
Figure 2: Flowchart

<!-- b000087 | prose | pages [4] -->
2

<!-- b000088 | heading | pages [4] -->
Assumptions and Notations

<!-- b000089 | prose | pages [4] -->
Assumption1: Insurance companies bear the risk independently Justification: In reality, insurance companies often diversify risks through financial products, govern- ment support, and other means. Since we focus on the design of insurance products, we assume that insurance companies do not adopt risk diversification measures.

<!-- b000090 | furniture | pages [4] -->
关注数学模型

<!-- b000091 | furniture | pages [4] -->
2

<!-- b000092 | furniture | pages [4] -->
MATHmodels

<!-- b000093 | furniture | pages [4] -->
获取更多资讯

<!-- b000094 | furniture | pages [5] -->
Team # 2401102

<!-- b000095 | furniture | pages [5] -->
Page 4 of 25

<!-- b000096 | prose | pages [5] -->
Assumption2: Insurance demand is negatively correlated with price, and insurance demand re- flects the number of customers. Justification: Insurance, as a normal good, experiences a decrease in demand as its price increases.

<!-- b000097 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000098 | prose | pages [5] -->
And insurance demand corresponds to the number of insurance policies, and it can be directly seen as reflecting the number of customers.

<!-- b000099 | prose | pages [5] -->
Assumption3: Existing real estate development processes do not primarily consider extreme weather risk predictions. Justification: Extreme weather events have low frequencies and high randomness, making them dif- ficult to predict. Additionally, we conducted keyword searches on Google Scholar, and there is little discussion on incorporating extreme weather risk predictions into the primary indicators for real estate development.

<!-- b000100 | prose | pages [5] -->
Assumption4: The data we use is true and reliable.

<!-- b000101 | heading | pages [5] -->
Justification: Our data sources include international statistical agencies, academic databases, and rep-

<!-- b000102 | prose | pages [5] -->
utable insurance companies. Therefore, we can confidently state that the data we use is accurate and

<!-- b000103 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000104 | prose | pages [5] -->
reliable for modeling purposes.

<!-- b000105 | heading | pages [5] -->
Notations

<!-- b000106 | prose | pages [5] -->
Symbol

<!-- b000107 | prose | pages [5] -->
EL PEL

<!-- b000108 | prose | pages [5] -->
Definition

<!-- b000109 | prose | pages [5] -->
Expected Loss Frequncy of Loss Quantity of Insurance Demand Q D R Insurance Demand Total Risk for Insurance Sustainability for Insurance Company Sustainability Demand-Risk Equilibrium Model for Insurance DBMI Innovative Risk Prediction Property Development Method IRPPDM Historical Landmark Preservation Model HLPM

<!-- b000110 | heading | pages [5] -->
Model I: Property Insurance Posture Model

<!-- b000111 | prose | pages [5] -->
3

<!-- b000112 | prose | pages [5] -->
The Types of Extreme Weather Events 3.1

<!-- b000113 | prose | pages [5] -->
According to USDA Climate Hubs, extreme events are occurrences of unusually severe weather or climate conditions that can cause devastating impacts on communities and agricultural and natural ecosystems.

<!-- b000114 | prose | pages [5] -->
NASA provided a brief summary of global extreme weather events, including heat waves, wildfires, droughts, tropical cyclones, heavy precipitation, floods, high-tide flooding, and marine heat waves.[3]

<!-- b000115 | furniture | pages [5] -->
关注数学模型

<!-- b000116 | furniture | pages [5] -->
2

<!-- b000117 | furniture | pages [5] -->
MATHmodels

<!-- b000118 | furniture | pages [5] -->
获取更多资讯

<!-- b000119 | furniture | pages [6] -->
Team # 2401102

<!-- b000120 | furniture | pages [6] -->
Page 5 of 25

<!-- b000121 | prose | pages [6] -->
As illustrated in Figure 3, we mainly discuss the impact of extreme weather events on property insur- ance, so we only focuse on four main categories: droughts, floods, tropical cyclones, and wildfires.

<!-- b000122 | prose | pages [6] -->
微信公众号：数学模型

<!-- b000123 | prose | pages [6] -->
微信号：MATHmodels

<!-- b000124 | caption | pages [6] -->
Figure 3: Four types of extreme weather events studied

<!-- b000125 | prose | pages [6] -->
• Wildfires: Dry conditions increase the risk of wildfires. With global temperatures on the rise, some regions may experience more frequent and intense wildfires, posing a threat to life and property. • Floods: Floods present a substantial threat to properties as heightened atmospheric moisture can result in more frequent and heavier rainfall, which can overwhelm both natural and man-made water management systems. This is especially true in coastal areas due to the compounding effect of rising sea levels. • Tropical Cyclones: Tropical cyclones, fueled by warmer ocean temperatures and more humid air, are likely to cause more severe and long-lasting rainfall events. These natural phenomena can severely impact properties, particularly through enhanced coastal flooding, driven by rising sea levels that elevate storm surge impacts. • Droughts: The rising aridity in certain regions, exacerbated by global warming, has adverse effects on properties. This not only depletes ground moisture but also perpetuates a cycle of warming and moisture loss, leading to soil degradation, foundation issues, and an increased risk of fire hazards. • Others: Other types can be listed as heat extremes, heavy precipitation, high-tide flooding, ma- rine heat waves,etc.

<!-- b000126 | prose | pages [6] -->
Predicting Extreme Weather Events: Based on ARIMA 3.2

<!-- b000127 | prose | pages [6] -->
To accurately calculate the expected loss of insurance products, insurance companies must precisely predict the probability of various extreme weather events. This step is significant for insurance pricing and risk control.

<!-- b000128 | prose | pages [6] -->
Given the uncertainty, complexity, and randomness of extreme weather events, we propose the use of time series analysis method to fit and predict the frequency of extreme weather events more accu-

<!-- b000129 | furniture | pages [6] -->
关注数学模型

<!-- b000130 | furniture | pages [6] -->
2

<!-- b000131 | furniture | pages [6] -->
MATHmodels

<!-- b000132 | furniture | pages [6] -->
获取更多资讯

<!-- b000133 | furniture | pages [7] -->
Team # 2401102

<!-- b000134 | furniture | pages [7] -->
Page 6 of 25

<!-- b000135 | prose | pages [7] -->
rately. Through this approach, we aim to improve the accuracy of predictions to better price insurance products and manage risk.

<!-- b000136 | prose | pages [7] -->
微信公众号：数学模型

<!-- b000137 | prose | pages [7] -->
3.2.1 Series Stabilization

<!-- b000138 | prose | pages [7] -->
For non-stationary time series, predictive models may fail due to changes in the statistical properties of the series over time. Therefore, differencing is employed to reduce or eliminate the trend and seasonal components of the time series, thereby stabilizing the series.

<!-- b000139 | prose | pages [7] -->
The first-order difference sequence y(n) is obtained by taking the difference between consecutive terms of the original sequence x(n) . If the first-order difference sequence is still not stationary(usually use ADF to test), we can repeat the process to obtain the second-order difference sequence z(n):

<!-- b000140 | prose | pages [7] -->
y(i + 1) = x(i + 1) −x(i) (1)

<!-- b000141 | prose | pages [7] -->
z(i + 2) = y(i + 2) −y(i + 1)

<!-- b000142 | prose | pages [7] -->
where:

<!-- b000143 | prose | pages [7] -->
(2)

<!-- b000144 | prose | pages [7] -->
微信号：MATHmodels

<!-- b000145 | prose | pages [7] -->
• x is the original sequence.

<!-- b000146 | prose | pages [7] -->
• y is the first-order difference sequence.

<!-- b000147 | prose | pages [7] -->
• z is the second-order difference sequence.

<!-- b000148 | prose | pages [7] -->
• i represents the timestamp.

<!-- b000149 | prose | pages [7] -->
3.2.2

<!-- b000150 | heading | pages [7] -->
ARIMA Model

<!-- b000151 | prose | pages [7] -->
For the stabilized sequence, we employ the Autoregressive Integrated Moving Average (ARIMA) model for prediction. This model integrates Autoregressive (AR) and Moving Average (MA) methods, incorporating differencing to enhance data stationarity. By examining the autocorrelation in historical data, the model assumes future trends will mimic historical patterns, thereby forecasting future data points.

<!-- b000152 | prose | pages [7] -->
ARIMA(p,i,q) can be represented by the following equation:

<!-- b000153 | prose | pages [7] -->
Xt = c + ϕ1Xt−1 + ϕ2Xt−2 + . . . + ϕpXt−p −θ1εt−1 −θ2εt−2 −. . . −θqεt−q + εt

<!-- b000154 | prose | pages [7] -->
where:

<!-- b000155 | prose | pages [7] -->
(3)

<!-- b000156 | prose | pages [7] -->
• Xt represents the time series(usually the difference sequence).

<!-- b000157 | prose | pages [7] -->
• c is the constant term.

<!-- b000158 | prose | pages [7] -->
• ϕ1, ϕ2, . . . , ϕp are the autoregressive coefficients corresponding to lag time steps 1, 2, . . . , p.

<!-- b000159 | prose | pages [7] -->
• θ1, θ2, . . . , θq are the moving average coefficients corresponding to lag time steps 1, 2, . . . , q.

<!-- b000160 | prose | pages [7] -->
• εt represents the white noise error term at time point t.

<!-- b000161 | prose | pages [7] -->
Obtain appropriate parameters through program execution to determine ARIMA(p, i, q), and com- plete model validation. Then we can get the frequency prediction of different extreme weather events for each area.

<!-- b000162 | furniture | pages [7] -->
关注数学模型

<!-- b000163 | furniture | pages [7] -->
2

<!-- b000164 | furniture | pages [7] -->
MATHmodels

<!-- b000165 | furniture | pages [7] -->
获取更多资讯

<!-- b000166 | furniture | pages [8] -->
Team # 2401102

<!-- b000167 | prose | pages [8] -->
Example: Fitting Cyclones and Tornadoes

<!-- b000168 | furniture | pages [8] -->
Page 7 of 25

<!-- b000169 | prose | pages [8] -->
We conducted first-order differencing on the annual data of tornadoes and hurricanes in New South Wales, Australia. Figure 4 displays the ARIMA model’s fitted line, demonstrating a satisfactory model

<!-- b000170 | prose | pages [8] -->
微信公众号：数学模型

<!-- b000171 | prose | pages [8] -->
fit. Based on this, we concluded that our approach is suitable for extreme weather data characterized by significant fluctuations and strong seasonality.

<!-- b000172 | prose | pages [8] -->
微信号：MATHmodels

<!-- b000173 | caption | pages [8] -->
Figure 4: Curve Fitting Example: Wind Events in 1975-2023

<!-- b000174 | prose | pages [8] -->
3.3 Insurance Price and Demand

<!-- b000175 | prose | pages [8] -->
3.3.1 Two Types of Insurance

<!-- b000176 | prose | pages [8] -->
It is important to note the role of insurance in mitigating the impact of extreme weather events, including indemnity-based insurance, index-based insurance, and insurance-linked securities. These tools can assist households and enterprises in adapting to the increasing risks associated with climate change.

<!-- b000177 | prose | pages [8] -->
Here we mainly focus on the two types of insurance.We determine the type of insurance based on per capita GDP: Developed regions typically use indemnity-based insurance, while developing regions typically use index-based insurance.

<!-- b000178 | prose | pages [8] -->
Indemnity-based Insurance

<!-- b000179 | prose | pages [8] -->
It compensates for actual losses caused by an event. Data is collected on the financial loss caused by different types of extreme weather events and the probability of loss in an area over the years. After processing the data, we can obtain the total losses and payouts for each year. This allows us to calculate the expected loss(EL) :

<!-- b000180 | prose | pages [8] -->
∑

<!-- b000181 | prose | pages [8] -->
Average Lost of event j

<!-- b000182 | prose | pages [8] -->
EL =

<!-- b000183 | prose | pages [8] -->
(4) Average Affected People of event j

<!-- b000184 | prose | pages [8] -->
j

<!-- b000185 | prose | pages [8] -->
Index-based Insurance

<!-- b000186 | prose | pages [8] -->
Payouts to policyholders depend on an index that strongly correlates with losses in income or assets. To estimate loss, we should use a metric to measure the severity of events. However, losses vary from

<!-- b000187 | furniture | pages [8] -->
关注数学模型

<!-- b000188 | furniture | pages [8] -->
2

<!-- b000189 | furniture | pages [8] -->
MATHmodels

<!-- b000190 | furniture | pages [8] -->
获取更多资讯

<!-- b000191 | furniture | pages [9] -->
Team # 2401102

<!-- b000192 | furniture | pages [9] -->
Page 8 of 25

<!-- b000193 | prose | pages [9] -->
event to event and are measured differently, so the data must be normalized and weighted to obtain a loss index γ. Thus we can determine the extent of loss and expected loss(EL):

<!-- b000194 | prose | pages [9] -->
∑

<!-- b000195 | prose | pages [9] -->
γj × Standard Compensation of event j

<!-- b000196 | prose | pages [9] -->
EL =

<!-- b000197 | prose | pages [9] -->
(5)

<!-- b000198 | prose | pages [9] -->
微信公众号：数学模型

<!-- b000199 | prose | pages [9] -->
j

<!-- b000200 | prose | pages [9] -->
3.3.2 Price of Insurance

<!-- b000201 | prose | pages [9] -->
According to the methods above, we can obtain expected loss caused by extreme weather events. Based on this, we consider the pricing of insurance products.

<!-- b000202 | prose | pages [9] -->
Insurance premiums usually consist of two parts: pure premium and additional premium. Accord- ing to Lane’s LFC model[4], we use EL to measure the pure premium while considering the expected excess return(EER) to measure addtional premium.Then we get the insurance price, or Premium(P):

<!-- b000203 | prose | pages [9] -->
P = EL + EER (6)

<!-- b000204 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000205 | prose | pages [9] -->
We have provided specific formulas to calculate EL in section 3.3. EER depends on the frequency and severity of loss, represented by the Cobb-Douglas function, as follows:

<!-- b000206 | prose | pages [9] -->
EER = 0.55 × PEL0.495 × CEL0.574 (7)

<!-- b000207 | prose | pages [9] -->
CEL = EL

<!-- b000208 | prose | pages [9] -->
where:

<!-- b000209 | prose | pages [9] -->
• PEL is referred to as frequency of loss

<!-- b000210 | prose | pages [9] -->
• CEL is used to measure severity of loss

<!-- b000211 | prose | pages [9] -->
3.3.3 Demand for Insurance

<!-- b000212 | prose | pages [9] -->
(8) PEL

<!-- b000213 | prose | pages [9] -->
To measure the revenue of the insurance company, we also need to assess demand(D) of insurance products. Since insurance demand is influenced by many factors in reality, we abstractly use Marshal- lian Demand Curve to simplify analysis. According to this model, demand is inversely proportional to price,as the yellow curve in Figure 5:

<!-- b000214 | caption | pages [9] -->
Figure 5: Demand- Price Curve

<!-- b000215 | furniture | pages [9] -->
关注数学模型

<!-- b000216 | furniture | pages [9] -->
2

<!-- b000217 | furniture | pages [9] -->
MATHmodels

<!-- b000218 | furniture | pages [9] -->
获取更多资讯

<!-- b000219 | furniture | pages [10] -->
Team # 2401102

<!-- b000220 | prose | pages [10] -->
where:

<!-- b000221 | furniture | pages [10] -->
Page 9 of 25

<!-- b000222 | prose | pages [10] -->
(9) Q = aP + b, a < 0, b > 0

<!-- b000223 | prose | pages [10] -->
Additionally, we consider property owner’s influence on insurance company. The choices of one

<!-- b000224 | prose | pages [10] -->
微信公众号：数学模型

<!-- b000225 | prose | pages [10] -->
single property owner are unlikely to significantly affect market demand, but the change of consumer trend in the market would lead to shifts in the demand curve. For example, if consumer’s willingness to consume increases, the demand curve would shift to the right as blue curve in Figure 5.

<!-- b000226 | heading | pages [10] -->
Demand-Risk Equilibrium Model for Insurance

<!-- b000227 | prose | pages [10] -->
3.4

<!-- b000228 | prose | pages [10] -->
We have constructed the Demand-Risk Equilibrium Model for Insurance(DEMI) to comprehen- sively assess the sustainability of an insurance company, considering two aspects: the total demand for insurance and the overall risk undertaken by the insurance company.

<!-- b000229 | prose | pages [10] -->
The reasons for selecting these two aspects are as follows: Firstly, there is a significant positive correlation between the customer number of insurance com- pany(means the same as total demand) and the profitability of the insurance company.

<!-- b000230 | prose | pages [10] -->
微信号：MATHmodels

<!-- b000231 | prose | pages [10] -->
However,insurance companies cannot indiscriminately increase the number of policies, as an ex- cessive increase in extreme weather risk may lead to the insurance company facing insurmountable large claims. Therefore, we introduce the concept of overall risk to impose constraints.

<!-- b000232 | prose | pages [10] -->
Aim to assist insurance companies in deciding whether to underwrite policies in certain areas, we initially divide high-risk areas within the insurance company’s business scope into n distinct areas and introduce binary variables xi:

<!-- b000233 | prose | pages [10] -->
{

<!-- b000234 | prose | pages [10] -->
choose to underwrite in area i, 1

<!-- b000235 | prose | pages [10] -->
xi =

<!-- b000236 | prose | pages [10] -->
(10) refuse to underwrite in area i . 0

<!-- b000237 | prose | pages [10] -->
Total Demand

<!-- b000238 | prose | pages [10] -->
Based on the insurance demand model derived from ARIMA model of extreme weather events, we can obtain forecasts for insurance demand in the future for area i, denoted as di. For the insurance company, its total demand is the sum of the demands from the underwritten areas,which can be defined as follows:

<!-- b000239 | prose | pages [10] -->
D =

<!-- b000240 | prose | pages [10] -->
Overall Risk

<!-- b000241 | prose | pages [10] -->
n ∑

<!-- b000242 | prose | pages [10] -->
xi · di (11)

<!-- b000243 | prose | pages [10] -->
i=1

<!-- b000244 | prose | pages [10] -->
Based on the predictive model mentioned in Section 3.4, we can derive independent future occurrence probabilities for extreme weather events in different areas. To assess the overall risk, we must consider the impact of different types of extreme weather events and the aggregation of risks across areas.

<!-- b000245 | prose | pages [10] -->
We opt for a severity weighting method to evaluate the impact of different extreme weather events and obtain the formula for calculating the total risk ri for area i.

<!-- b000246 | prose | pages [10] -->
ri =

<!-- b000247 | prose | pages [10] -->
∑

<!-- b000248 | prose | pages [10] -->
pij · αj (12)

<!-- b000249 | prose | pages [10] -->
j j

<!-- b000250 | furniture | pages [10] -->
关注数学模型

<!-- b000251 | furniture | pages [10] -->
2

<!-- b000252 | furniture | pages [10] -->
MATHmodels

<!-- b000253 | furniture | pages [10] -->
获取更多资讯

<!-- b000254 | furniture | pages [11] -->
Team # 2401102

<!-- b000255 | prose | pages [11] -->
∑

<!-- b000256 | prose | pages [11] -->
j

<!-- b000257 | prose | pages [11] -->
where:

<!-- b000258 | furniture | pages [11] -->
Page 10 of 25

<!-- b000259 | prose | pages [11] -->
(13) αj = 1

<!-- b000260 | prose | pages [11] -->
微信公众号：数学模型

<!-- b000261 | prose | pages [11] -->
• pij: Probability of event extreme weather type j occurring in area i.

<!-- b000262 | prose | pages [11] -->
• αj: Impact degree of extreme weather type j.

<!-- b000263 | prose | pages [11] -->
• j: Different types of extreme weather events.

<!-- b000264 | prose | pages [11] -->
Optimization for Sustainability

<!-- b000265 | prose | pages [11] -->
Ultimately, we propose DEMI to assess insurance companies’ sustainability. It is a dual-objective optimization model, wherein we introduce a weight parameter λ to balance the importance of overall risk and total demand.

<!-- b000266 | prose | pages [11] -->
With an appropriate choice of λ, the model can effectively address both aspects. The specific definition of the model is as follows:

<!-- b000267 | prose | pages [11] -->
微信号：MATHmodels

<!-- b000268 | prose | pages [11] -->
max Sustainability = λD −(1 −λ)R (14)

<!-- b000269 | prose | pages [11] -->
Its constraints are the limitations imposed by the binary variables xi mentioned earlier in the this section.

<!-- b000270 | prose | pages [11] -->
Case Study: Australia and Southeast Asia 4

<!-- b000271 | prose | pages [11] -->
4.1

<!-- b000272 | heading | pages [11] -->
Data Processing and Analysis

<!-- b000273 | heading | pages [11] -->
Data Source and Area Segmentation

<!-- b000274 | prose | pages [11] -->
We have gathered a total of 744 records of extreme weather events in Australia dating back to 1967 and 2,021 records of extreme weather events in Southeast Asia since 1970.[5] Given Australia’s geographic isolation from other continents, we treat it as a research region, with its individual states considered separate areas. In contrast, due to the multitude of Southeast Asian nations and their relatively small land areas, we consider Southeast Asia as a research region, with different countries categorized as distinct areas.

<!-- b000275 | prose | pages [11] -->
After excluding missing data and natural disasters outside the scope of our study, we obtained

<!-- b000276 | caption | pages [11] -->
Figure 6. It’s important to note that due to the differences in data sources and classification methods,

<!-- b000277 | prose | pages [11] -->
the categorization of extreme weather events varies between the two regions.

<!-- b000278 | caption | pages [11] -->
Figure 6: The frequencies of different events in the two regions.

<!-- b000279 | furniture | pages [11] -->
关注数学模型

<!-- b000280 | furniture | pages [11] -->
2

<!-- b000281 | furniture | pages [11] -->
MATHmodels

<!-- b000282 | furniture | pages [11] -->
获取更多资讯

<!-- b000283 | furniture | pages [12] -->
Team # 2401102

<!-- b000284 | prose | pages [12] -->
Selection of Study Scope

<!-- b000285 | furniture | pages [12] -->
Page 11 of 25

<!-- b000286 | prose | pages [12] -->
Based on the original data, in Australia, we choose to classify cyclones and tornadoes into one cate- gory, and hail, hailstorms, and storms into another category, resulting in a total of four types of extreme

<!-- b000287 | prose | pages [12] -->
微信公众号：数学模型

<!-- b000288 | prose | pages [12] -->
weather events: bushfire, cyclone, flood, and storm. In Southeast Asia, we retained the original classi- fication: drought, flood, and storm.

<!-- b000289 | caption | pages [12] -->
Figure 7: Categorized events in the two regions

<!-- b000290 | prose | pages [12] -->
微信号：MATHmodels

<!-- b000291 | prose | pages [12] -->
Next, we proceeded to select areas that were significantly impacted by extreme weather events for inclusion in the insurance company’s consideration of whether to underwrite. We determined whether they qualified as high-risk areas based on the frequency distribution of extreme weather events(in Figure 8) in each area.

<!-- b000292 | caption | pages [12] -->
Figure 8: Distribution of events in areas in the two regions

<!-- b000293 | prose | pages [12] -->
Lastly, we have chosen the following areas to analysis: in Australia, New South Wales (NSW), Queensland (QLD), Victoria (VIC), and Western Australia (WA), while in Southeast Asia, Indonesia (IDN), Philippines (PHL), Thailand (THA), and Vietnam (VNM) – we consider Thailand to have a higher risk level despite its contribution to the total count being less than 10% due to the high overall frequency in Southeast Asia.

<!-- b000294 | prose | pages [12] -->
4.2

<!-- b000295 | heading | pages [12] -->
Use of ARIMA Model

<!-- b000296 | prose | pages [12] -->
Applying the previously mentioned methodology, we initially conducted a second-order differencing analysis on the frequency of certain types of extreme weather events in each area of the two regions.

<!-- b000297 | furniture | pages [12] -->
关注数学模型

<!-- b000298 | furniture | pages [12] -->
2

<!-- b000299 | furniture | pages [12] -->
MATHmodels

<!-- b000300 | furniture | pages [12] -->
获取更多资讯

<!-- b000301 | furniture | pages [13] -->
Team # 2401102

<!-- b000302 | furniture | pages [13] -->
Page 12 of 25

<!-- b000303 | prose | pages [13] -->
Subsequently, we employed the ARIMA model for time series forecasting, yielding equations in the following form (taking the example of bushfire in NSW):

<!-- b000304 | prose | pages [13] -->
微信公众号：数学模型

<!-- b000305 | prose | pages [13] -->
ARIMA(3, 2, 1) : Y(t) = −0.002 −0.651Y(t−1) −0.412Y(t−2) −0.105Y(t−3) −0.952ε(t−1) (15)

<!-- b000306 | prose | pages [13] -->
Then applying the model to all time series of each area-event pair, we obtained corresponding prediction curves. These curves exhibit an excellent fit to the original data, as illustrated in Figures 9 . Here, we provide examples from IND in Southeast Asia and WA in Australia.

<!-- b000307 | prose | pages [13] -->
微信号：MATHmodels

<!-- b000308 | caption | pages [13] -->
Figure 9: Events Fitting Curves

<!-- b000309 | prose | pages [13] -->
Next, we employ the coefficient of determination R2 as well as the Akaike Information Criterion (AIC) and Bayesian Information Criterion (BIC) to assess the performance of each model. The defini- tions of AIC and BIC are as follows:

<!-- b000310 | prose | pages [13] -->
AIC = −2 ln(L) + 2k (16)

<!-- b000311 | prose | pages [13] -->
BIC = −2 ln(L) + k ln(n)

<!-- b000312 | prose | pages [13] -->
where:

<!-- b000313 | prose | pages [13] -->
(17)

<!-- b000314 | prose | pages [13] -->
• L represents the maximum likelihood of the model.

<!-- b000315 | prose | pages [13] -->
• k is the number of model parameters.

<!-- b000316 | prose | pages [13] -->
• n is the number of data points. Part of our model evaluation results are presented in Table 1. Both AIC and BIC remain at accept- able levels, and R2 values consistently exceed 0.6.

<!-- b000317 | prose | pages [13] -->
Thus, we believe that our model is robust to effectively forecast future extreme weather events. Finally we get the frequency prediction of different area-event for the next 3 years.

<!-- b000318 | furniture | pages [13] -->
关注数学模型

<!-- b000319 | furniture | pages [13] -->
2

<!-- b000320 | furniture | pages [13] -->
MATHmodels

<!-- b000321 | furniture | pages [13] -->
获取更多资讯

<!-- b000322 | furniture | pages [14] -->
Team # 2401102

<!-- b000323 | prose | pages [14] -->
Area-Event

<!-- b000324 | furniture | pages [14] -->
Page 13 of 25

<!-- b000325 | prose | pages [14] -->
R2 AIC BIC

<!-- b000326 | prose | pages [14] -->
83.023 IDN-Drought 94.731 0.745 279.993 IDN-Flood 295.603 0.665 116.088 IDN-Storm 125.844 0.767

<!-- b000327 | prose | pages [14] -->
微信公众号：数学模型

<!-- b000328 | prose | pages [14] -->
82.001 PHL-Drought 97.611 0.839 245.232 PHL-Flood 254.988 0.629 277.507 PHL-Storm 289.214 0.715 74.377 THA-Drought 86.085 0.837 222.739 THA-Flood 236.398 0.726 165.383 THA-Storm 177.090 0.781 64.436 VNM-Drought 78.095 0.833 203.976 VNM-Flood 217.635 0.781 222.338 VNM-Storm 234.045 0.784

<!-- b000329 | caption | pages [14] -->
Table 1: Model validation for the Southeast Asian

<!-- b000330 | prose | pages [14] -->
微信号：MATHmodels

<!-- b000331 | prose | pages [14] -->
4.3 Apply DEMI to Two Areas

<!-- b000332 | prose | pages [14] -->
Determination of Premiums and Demand 4.3.1

<!-- b000333 | prose | pages [14] -->
Based on the per capita GDP in Australia and Southeast Asia, we have chosen to calculate the EL for each area using both indemnity-based insurance and index-based insurance models.

<!-- b000334 | prose | pages [14] -->
By using formulas above, we have computed the probability of loss(PEL) for both Australia and Southeast Asia for the year 2024. By utilizing the PEL and the EL, we calculate the Conditional Ex- pected Loss (CEL),which ultimately allows us to determine the insurance premium:

<!-- b000335 | caption | pages [14] -->
Figure 10: Premium for two areas

<!-- b000336 | prose | pages [14] -->
As shown in Figure 10, it is evident that due to varying levels of risk, there are differences in insurance premiums across different areas. Next, we will incorporate the insurance demand model to obtain the demand di for each area.

<!-- b000337 | prose | pages [14] -->
4.3.2 Solving DBMI

<!-- b000338 | prose | pages [14] -->
We have observed that within the range of λ values between 2∗10−5 and 1∗10−6, the model effectively balances risk and demand. Ultimately, we have selected a λ value of 5 ∗10−6, resulting in the optimal insurance coverage plan as follows:

<!-- b000339 | furniture | pages [14] -->
关注数学模型

<!-- b000340 | furniture | pages [14] -->
2

<!-- b000341 | furniture | pages [14] -->
MATHmodels

<!-- b000342 | furniture | pages [14] -->
获取更多资讯

<!-- b000343 | furniture | pages [15] -->
Team # 2401102

<!-- b000344 | furniture | pages [15] -->
Page 14 of 25

<!-- b000345 | prose | pages [15] -->
• For the Australian region, we provide coverage for QLD and WA while not covering VIC and NSW.

<!-- b000346 | prose | pages [15] -->
• In the Southeast Asian region, we offer coverage for PHL and THA while not covering IND and

<!-- b000347 | prose | pages [15] -->
微信公众号：数学模型

<!-- b000348 | prose | pages [15] -->
VNM. Next, we would analyze this outcome by risk and demand data.

<!-- b000349 | prose | pages [15] -->
Country NSW Premium 798.05 Total Demand 74327 Total Risk 0.54162 QLD VIC WA 823.69 1295.62 267.51 73460 58857 90847 0.30394 0.76552 0.06285

<!-- b000350 | caption | pages [15] -->
Table 2: Insurance data of Australia

<!-- b000351 | prose | pages [15] -->
In the case of Australia, the model opts for the lowest-risk option, WA, over VIC, which exhibits significantly higher risk compared to other areas. This decision aligns with the sustainability principle

<!-- b000352 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000353 | prose | pages [15] -->
of risk avoidance. Additionally, we observe that the demand and premiums for NSW and QLD are similar. The model chooses QLD, which has a lower overall risk, thus demonstrating a balance between risk and profitability.

<!-- b000354 | prose | pages [15] -->
Country IDN Premium 543.94 Total Demand 72802 Total Risk 0.29424 PHL THA VNM 119.20 717.82 267.28 94039 64109 86635 0.05597 0.09301 0.17466

<!-- b000355 | caption | pages [15] -->
Table 3: Insurance data of Southeast Asia

<!-- b000356 | prose | pages [15] -->
For Southeast Asia, we can observe that the two selected areas share a significant characteristic: they both exhibit low overall risk. Additionally, the choice of THA, which commands the highest premiums, enhances the profitability of the insurance company.

<!-- b000357 | prose | pages [15] -->
As for the other two areas, IDN, despite having high premiums, also carries high risks, making it a less favorable option. On the other hand, VNM presents relatively high risks but offers lower premiums, resulting in a suboptimal cost-benefit ratio for insurance coverage.

<!-- b000358 | prose | pages [15] -->
In conclusion, we believe that our model has reasonable outcomes in both regions. These results re- flect the balance between profitability and risk management for insurance company. The model’s accuracy in forecasting extreme weather events, coupled with its strong interpretability, provides valuable insights for the insurance company in addressing extreme weather events.

<!-- b000359 | prose | pages [15] -->
Innovative Risk Prediction Property Development Method 5

<!-- b000360 | prose | pages [15] -->
Based on Assumption3, we propose innovative risk prediction property development method that considers extreme weather risk predictions. This involves adapting our DBIM to assist developers in evaluating where, how, and whether to build on certain sites.

<!-- b000361 | furniture | pages [15] -->
关注数学模型

<!-- b000362 | furniture | pages [15] -->
2

<!-- b000363 | furniture | pages [15] -->
MATHmodels

<!-- b000364 | furniture | pages [15] -->
获取更多资讯

<!-- b000365 | furniture | pages [16] -->
Team # 2401102

<!-- b000366 | furniture | pages [16] -->
Page 15 of 25

<!-- b000367 | prose | pages [16] -->
5.1 Whether to Build: Determined by Willingness and Risk

<!-- b000368 | prose | pages [16] -->
To provide housing and other real estate services for the ever-growing communities and populations, real estate companies have their own system for for selecting development areas.

<!-- b000369 | prose | pages [16] -->
微信公众号：数学模型

<!-- b000370 | prose | pages [16] -->
The specific methods fall outside the scope of our study. Anyway, they can utilize such a system to perform assessment of the developmental potential for each area,which we call as Development Willingness Index (DWI). A higher DWI value indicates a more optimistic profit outlook for property developers, and correspondingly, a stronger inclination to develop such areas.

<!-- b000371 | prose | pages [16] -->
Next, we adapt our DBMI s weighted risk - to measure the extreme weather risk in a specific area. By setting the development index on the vertical axis and total risk on the horizontal axis, we construct a Cartesian coordinate system(shown in Figure 11(a)). Each prospective development area corresponds to a unique point within this coordinate system. This system is divided into four quadrants, representing different combinations of risk and willingness:

<!-- b000372 | prose | pages [16] -->
微信号：MATHmodels

<!-- b000373 | caption | pages [16] -->
Figure 11: Cartesian coordinate system

<!-- b000374 | prose | pages [16] -->
• Quadrant I (Low Risk - High Willingness): Areas in this quadrant exhibit low extreme weather risk and a strong desire for development. For these areas, real estate developers need not pay much attention to extreme weather risk. Therefore, these areas can be developed according to the company’s own development system. However, they are not the focus of our method.

<!-- b000375 | prose | pages [16] -->
• Quadrant II (High Risk - High Willingness): Areas in this quadrant display both a strong desire for development and face high extreme weather risk. If risk reduction measures can be imple- mented to lower the risk while maintaining high willingness, these areas can transit from Quad- rant II to I(Figure 11 (b)), becoming feasible options for developers. Otherwise, they should abandon development plans in such an area. Our method focuses on this quadrant.

<!-- b000376 | prose | pages [16] -->
• Quadrants III & IV (Low Willingness): Areas in these two quadrants exhibit low development willingness, even without considering the risk of extreme weather, these areas are not suitable candidates for development. Consequently, they are also not the focus of our method.

<!-- b000377 | prose | pages [16] -->
Next, we will focus on the areas situated in Quadrant II and discuss how and where to build in order to facilitate their transition to Quadrant I.

<!-- b000378 | furniture | pages [16] -->
关注数学模型

<!-- b000379 | furniture | pages [16] -->
2

<!-- b000380 | furniture | pages [16] -->
MATHmodels

<!-- b000381 | furniture | pages [16] -->
获取更多资讯

<!-- b000382 | furniture | pages [17] -->
Team # 2401102

<!-- b000383 | furniture | pages [17] -->
Page 16 of 25

<!-- b000384 | prose | pages [17] -->
How and Where to build: Addressing Specific Event Risk 5.2

<!-- b000385 | prose | pages [17] -->
In our discussion concerning areas in Quadrant II, we focus on how and where to implement real estate development. The objective of developing these areas is to mitigate extreme weather risk effectively

<!-- b000386 | prose | pages [17] -->
微信公众号：数学模型

<!-- b000387 | prose | pages [17] -->
while maintaining development willingness, reducing it to an acceptable level. We propose specific measures and assessment methods for mitigating potential risk associated with different types of ex- treme weather.[6]

<!-- b000388 | prose | pages [17] -->
Bushfire

<!-- b000389 | prose | pages [17] -->
To mitigate the risk of wildfires, site selection is the most direct approach. Preferred strategies include choosing sites in relatively moist areas and avoiding locations near forests. Additionally, measures taken in house construction can also reduce the risk of fires. These include avoiding the use of highly flammable insulation materials and opting for fire-resistant materials.

<!-- b000390 | prose | pages [17] -->
To quantify the effectiveness of site selection in reducing wildfire risk, we introduce the adjusted wildfire risk index p∗

<!-- b000391 | prose | pages [17] -->
b, defined as:

<!-- b000392 | prose | pages [17] -->
微信号：MATHmodels

<!-- b000393 | prose | pages [17] -->
p∗

<!-- b000394 | prose | pages [17] -->
b =

<!-- b000395 | prose | pages [17] -->
where:

<!-- b000396 | prose | pages [17] -->
pb (18) 1 + d

<!-- b000397 | prose | pages [17] -->
• pb is the original wildfire risk, predicted from the DBMI

<!-- b000398 | prose | pages [17] -->
• d is the distance from the selected site to potential fire source

<!-- b000399 | prose | pages [17] -->
Cyclone & Storm

<!-- b000400 | prose | pages [17] -->
Since wind-related disasters often accompany heavy rainfall, we discuss them together here. Due to the widespread impact of cyclones and storms, avoiding their impacts through location selection is ineffective. Therefore, enhancing the resistance of buildings to extreme events becomes a more effec- tive strategy. This includes strengthening the structural design of houses, improving drainage systems around houses, and installing backup power systems.

<!-- b000401 | prose | pages [17] -->
To quantify the effect of strengthening building structures in reducing tornado risk, we define the adjusted tornado risk index p∗

<!-- b000402 | prose | pages [17] -->
c as follows:

<!-- b000403 | prose | pages [17] -->
c = pc × Standard Building Strength

<!-- b000404 | prose | pages [17] -->
p∗

<!-- b000405 | prose | pages [17] -->
(19) Enhanced Building Strength

<!-- b000406 | prose | pages [17] -->
where:

<!-- b000407 | prose | pages [17] -->
• pc is the original tornado risk, predicted from the DBMI.

<!-- b000408 | prose | pages [17] -->
• Standard Building Strength represents the structural capacity without reinforcement.

<!-- b000409 | prose | pages [17] -->
• Enhanced Building Strength represents the structural capacity with reinforcement.

<!-- b000410 | prose | pages [17] -->
Drought

<!-- b000411 | prose | pages [17] -->
While the impact of drought on buildings may not be as direct or severe as some other extreme weather events, prolonged drought can potentially have negative effects on building structures. In terms of location selection, priority should be given to locations with stable foundations, which can help mitigate

<!-- b000412 | furniture | pages [17] -->
关注数学模型

<!-- b000413 | furniture | pages [17] -->
2

<!-- b000414 | furniture | pages [17] -->
MATHmodels

<!-- b000415 | furniture | pages [17] -->
获取更多资讯

<!-- b000416 | furniture | pages [18] -->
Team # 2401102

<!-- b000417 | furniture | pages [18] -->
Page 17 of 25

<!-- b000418 | prose | pages [18] -->
potential damage caused by soil drying and shrinking. Regarding the construction of houses, building design should focus on the integration of water-saving systems to minimize water consumption.

<!-- b000419 | prose | pages [18] -->
To quantify the effectiveness of constructing water-saving systems and selecting foundations in reducing drought risk, we define the adjusted drought risk index p∗

<!-- b000420 | prose | pages [18] -->
d as follows:

<!-- b000421 | prose | pages [18] -->
微信公众号：数学模型

<!-- b000422 | prose | pages [18] -->
d = pd × Soil Shrinkage Coefficient

<!-- b000423 | prose | pages [18] -->
p∗

<!-- b000424 | prose | pages [18] -->
(20) Water Efficiency Coefficient

<!-- b000425 | prose | pages [18] -->
where:

<!-- b000426 | prose | pages [18] -->
• pd is the original drought risk, predicted from the DBMI.

<!-- b000427 | prose | pages [18] -->
• Soil Shrinkage Coefficient measures the sensitivity of the soil to water deficiency.

<!-- b000428 | prose | pages [18] -->
• Water Efficiency Coefficient represents the efficiency of the water-saving system. Finally, based on the adjusted risk values p∗

<!-- b000429 | prose | pages [18] -->
j, we can calculate the new total risk r∗using the DBMI. By analyzing this value, we can help determine where, how, and whether to build on certain sites.

<!-- b000430 | prose | pages [18] -->
微信号：MATHmodels

<!-- b000431 | prose | pages [18] -->
5.3

<!-- b000432 | heading | pages [18] -->
Conclusion for IRPPDM

<!-- b000433 | prose | pages [18] -->
In the preceding sections of this chapter, we have presented the complete workflow of the IRPPDM, with its core concept being the integration of real estate companies’ regional analysis methods with our risk prediction model. This integration allows us to classify different areas based on risk and development willingness, and make decisions on whether construction should proceed accordingly.

<!-- b000434 | prose | pages [18] -->
Specifically, for high-risk, high-willingness areas, we have analyzed specific events response mea- sures and evaluated the risk levels after implementing specific site selection(where) and construction methods(how). Through this approach, we can reassess the risk and determine whether the site is suitable for development purposes.

<!-- b000435 | prose | pages [18] -->
It should be noted that we have not provided detailed index explanation for certain indicators in our risk adjustment formulas. This is because they are not the focus of this chapter. Our aim is to explore a new analytical framework to guide real estate development decisions. This framework emphasizes taking construction measures for different types of extreme weather, aiming to enhance the stability and safety of buildings. We hope that this approach can provide new insights for real estate companies.

<!-- b000436 | heading | pages [18] -->
Model II: Historic Landmark Preservation Model

<!-- b000437 | prose | pages [18] -->
6

<!-- b000438 | prose | pages [18] -->
Insurance companies do not underwrite policies all areas due to risk/reward considerations. However, there are historic landmarks in uncovered areas that may be destroyed by extreme weather events. There- fore, we have developed the Historic Landmark Preservation (HLP) Model for communities, which are under the threat of severe extreme weather.

<!-- b000439 | heading | pages [18] -->
The model construction began with four dimensions: history, culture, economy, and commu-

<!-- b000440 | prose | pages [18] -->
nity. Secondary indicators were selected based on these dimensions, and analytic hierarchical pro- cess(AHP) was used to measure the comprehensive value of the landmark. The higher the comprehen- sive value, the more necessary the preservation, and the greater the required investment.

<!-- b000441 | prose | pages [18] -->
Finally, we selected a specific site to demonstrate the effectiveness of the model and provide rec- ommendations for preservation.

<!-- b000442 | furniture | pages [18] -->
关注数学模型

<!-- b000443 | furniture | pages [18] -->
2

<!-- b000444 | furniture | pages [18] -->
MATHmodels

<!-- b000445 | furniture | pages [18] -->
获取更多资讯

<!-- b000446 | furniture | pages [19] -->
Team # 2401102

<!-- b000447 | prose | pages [19] -->
6.1 Indicator Selection

<!-- b000448 | furniture | pages [19] -->
Page 18 of 25

<!-- b000449 | prose | pages [19] -->
As shown in Figure 12, to comprehensively evaluate the value of landmarks, we selected four primary indicators:

<!-- b000450 | prose | pages [19] -->
微信公众号：数学模型

<!-- b000451 | prose | pages [19] -->
history, culture, economy, and community.

<!-- b000452 | prose | pages [19] -->
We considered the universality and objectivity of the indicators when selecting secondary indicators, as well as their measurability with data.

<!-- b000453 | prose | pages [19] -->
• Economic Value can be measured by two secondary indicators, Tourism Value (TV) and Exploitation Potential (EP). TV represents the existing economic value, which primarily derives from tourism. EP is equivalent to the undeveloped area divided by the to- tal area. • Cultural Value can be measured by two secondary

<!-- b000454 | prose | pages [19] -->
微信号：MATHmodels

<!-- b000455 | prose | pages [19] -->
indicators, Intangible Cultural Heritage (ICH) and

<!-- b000456 | caption | pages [19] -->
Figure 12: Introduction to primary and

<!-- b000457 | prose | pages [19] -->
Local Culture Research (LCR). ICH is quantified

<!-- b000458 | prose | pages [19] -->
secondary indicators

<!-- b000459 | prose | pages [19] -->
by the number of intangible cultural heritage. LCR can be determined by searching for papers indexed with DOI using the landmark name and community name as keywords. • Historical Value can be measured by two secondary indicators, Age and Importance in History (IH). Age refers to the number of years of history, while IH refers to the number of significant historical figures and events it is related to. • Community Value can be measured by two secondary indicators, Regional Educational Ac- tivities (REA) and Community Spirit (CS). REA refers to the number of regional educational activities related to the landmark. CS represents the positive impact of a landmark on the com- munity as a whole. It is measured on a scale of 0 to 1 due to the difficulty in accurately assessing its impact.

<!-- b000460 | prose | pages [19] -->
After identifying the metrics, we used AHP to assign weights and determine the value of the land- marks.

<!-- b000461 | prose | pages [19] -->
Weight Calculation: Based on AHP 6.2

<!-- b000462 | prose | pages [19] -->
Weight Assessment Matrix

<!-- b000463 | prose | pages [19] -->
After determining the eight secondary indicators above and their measuring methods, we need to assign weights to them. We set landmark value as the target layer and build a hierarchical model with primary indicators and secondary indicators.

<!-- b000464 | prose | pages [19] -->
Firstly, we compare the indicators within the same level pairwise to obtain the weight assessment matrix. To make the judgment results more professional, we obtained their relative weights from aca- demic papers.[7] The Weighting Judgment Matrix (WJM) for indicators are shown below.

<!-- b000465 | furniture | pages [19] -->
关注数学模型

<!-- b000466 | furniture | pages [19] -->
2

<!-- b000467 | furniture | pages [19] -->
MATHmodels

<!-- b000468 | furniture | pages [19] -->
获取更多资讯

<!-- b000469 | furniture | pages [20] -->
Team # 2401102

<!-- b000470 | furniture | pages [20] -->
Page 19 of 25

<!-- b000471 | caption | pages [20] -->
Table 4: Historical Landmark value WJM

<!-- b000472 | prose | pages [20] -->
Intermediate Layer Economy Economy 1 Culture History Community 1/3 1/3 1

<!-- b000473 | prose | pages [20] -->
微信公众号：数学模型

<!-- b000474 | prose | pages [20] -->
Culture 3 History 3 Community 1

<!-- b000475 | caption | pages [20] -->
Table 5: Economic Value WJM

<!-- b000476 | prose | pages [20] -->
Economic Value TV EP

<!-- b000477 | prose | pages [20] -->
Tourism Value (TV) 1 2 Exploitation Potential (EP) 1/2 1

<!-- b000478 | caption | pages [20] -->
Table 7: Historical Value WJM

<!-- b000479 | prose | pages [20] -->
1 3 3 1/3 1 3 1/3 1/3 1

<!-- b000480 | caption | pages [20] -->
Table 6: Cultural Value WJM

<!-- b000481 | prose | pages [20] -->
Cultural Value ICH LCR

<!-- b000482 | prose | pages [20] -->
Intangible Cultural Heritage (ICH) 1 5 Local Culture Research (LCR) 1/5 1

<!-- b000483 | caption | pages [20] -->
Table 8: Community Value WJM

<!-- b000484 | prose | pages [20] -->
微信号：MATHmodels

<!-- b000485 | prose | pages [20] -->
Historical Value Age IH

<!-- b000486 | prose | pages [20] -->
Age 1 1/3 Importance in History (IH) 3 1

<!-- b000487 | prose | pages [20] -->
Consistency Testing

<!-- b000488 | prose | pages [20] -->
Community Value REA CS

<!-- b000489 | prose | pages [20] -->
Regional Educational Activity (REA) 1 1/3 Community Spirit (CS) 3 1

<!-- b000490 | prose | pages [20] -->
As the data used came from multiple papers, it is necessary to conduct consistency testing on the results. The following explains how to conduct a consistency test on an n × n matrix. Let xi,j represent the data in the i-th row and j-th column.

<!-- b000491 | prose | pages [20] -->
The product of each row is computed as:

<!-- b000492 | prose | pages [20] -->
n ∏

<!-- b000493 | prose | pages [20] -->
Mi =

<!-- b000494 | prose | pages [20] -->
xi,j,

<!-- b000495 | prose | pages [20] -->
j=1

<!-- b000496 | prose | pages [20] -->
(21) i, j = 1, 2, . . . , n

<!-- b000497 | prose | pages [20] -->
The normalized principal eigenvector ¯Wi is calculated by taking the n-th root of Mi:

<!-- b000498 | prose | pages [20] -->
¯Wi =

<!-- b000499 | prose | pages [20] -->
To normalize the vector ¯W:

<!-- b000500 | prose | pages [20] -->
¯Wi =

<!-- b000501 | prose | pages [20] -->
n√

<!-- b000502 | prose | pages [20] -->
(22) Mi

<!-- b000503 | prose | pages [20] -->
¯Wi ∑n

<!-- b000504 | prose | pages [20] -->
(23)

<!-- b000505 | prose | pages [20] -->
j=1 ¯Wj

<!-- b000506 | prose | pages [20] -->
The maximum eigenvalue of the matrix, λmax, is given by:

<!-- b000507 | prose | pages [20] -->
n ∑

<!-- b000508 | prose | pages [20] -->
λmax =

<!-- b000509 | prose | pages [20] -->
i=1

<!-- b000510 | prose | pages [20] -->
((λmax ¯Wi)

<!-- b000511 | prose | pages [20] -->
)

<!-- b000512 | prose | pages [20] -->
(24)

<!-- b000513 | prose | pages [20] -->
n ¯Wi

<!-- b000514 | prose | pages [20] -->
The consistency index (CI) is obtained as follows, and a lower CI indicates higher consistency:

<!-- b000515 | prose | pages [20] -->
CI = λmax −n

<!-- b000516 | prose | pages [20] -->
(25) n −1

<!-- b000517 | furniture | pages [20] -->
关注数学模型

<!-- b000518 | furniture | pages [20] -->
2

<!-- b000519 | furniture | pages [20] -->
MATHmodels

<!-- b000520 | furniture | pages [20] -->
获取更多资讯

<!-- b000521 | furniture | pages [21] -->
Team # 2401102

<!-- b000522 | furniture | pages [21] -->
Page 20 of 25

<!-- b000523 | prose | pages [21] -->
In our model, the primary indicators’ matrix’s CI is 0.052, corresponding to a mean random consis- tency index (RI) value of 0.882, and the random consistency ratio (CR) is 0.058, passing the consistency test. The 2 × 2 matrices, representing secondary indicators, all have a CI value of 0 and have passed the consistency test. Below is the weight table.

<!-- b000524 | prose | pages [21] -->
微信公众号：数学模型

<!-- b000525 | caption | pages [21] -->
Table 9: Criteria Weights for Historic Landmark Value Assessment

<!-- b000526 | prose | pages [21] -->
Intermediate Layer Decision Layer

<!-- b000527 | prose | pages [21] -->
Economy

<!-- b000528 | prose | pages [21] -->
Culture

<!-- b000529 | prose | pages [21] -->
Historic Landmark Value

<!-- b000530 | prose | pages [21] -->
History

<!-- b000531 | prose | pages [21] -->
Community

<!-- b000532 | prose | pages [21] -->
Factor Layer Weight (%)

<!-- b000533 | prose | pages [21] -->
Tourism Value 8.135 Exploitation Potential 4.067

<!-- b000534 | prose | pages [21] -->
Intangible Cultural Heritage 39.434 Local Culture Research 7.887

<!-- b000535 | prose | pages [21] -->
Historical Importance 21.206 Age of Landmark 7.069

<!-- b000536 | prose | pages [21] -->
Regional Educational Activity 3.051

<!-- b000537 | prose | pages [21] -->
微信号：MATHmodels

<!-- b000538 | prose | pages [21] -->
Community Spirit 9.152

<!-- b000539 | prose | pages [21] -->
Value Calculation and Extent Estimation 6.3

<!-- b000540 | prose | pages [21] -->
HLV Calculation

<!-- b000541 | prose | pages [21] -->
Due to the different dimensions of indicators, we need to normalize them. All eight indicators involved in this article are positive indicators, and the normalization formula is as follows:

<!-- b000542 | prose | pages [21] -->
x′ = x −min(x) (26) max(x) −min(x)

<!-- b000543 | prose | pages [21] -->
After normalization, all indicators’ values are within the [0, 1] range and dimensionless, allowing for calculations.

<!-- b000544 | prose | pages [21] -->
The formula for calculating the historical landmark value HLV is as follows:

<!-- b000545 | prose | pages [21] -->
HLV =

<!-- b000546 | prose | pages [21] -->
where:

<!-- b000547 | prose | pages [21] -->
∑

<!-- b000548 | prose | pages [21] -->
(27) WaIa

<!-- b000549 | prose | pages [21] -->
a

<!-- b000550 | prose | pages [21] -->
• a represents the index of the specific indicator.

<!-- b000551 | prose | pages [21] -->
• I represents the normalized value of the indicator.

<!-- b000552 | prose | pages [21] -->
• W represents the weight of the indicator.

<!-- b000553 | prose | pages [21] -->
Estimation of Extent of Preservation Measures

<!-- b000554 | prose | pages [21] -->
Based on HLV, we can estimate the necessary extent of preservation. The level of preservation is scaled to match the significance of the landmark. Here we propose a three-tiered approach to categorize the protective measures:

<!-- b000555 | furniture | pages [21] -->
关注数学模型

<!-- b000556 | furniture | pages [21] -->
2

<!-- b000557 | furniture | pages [21] -->
MATHmodels

<!-- b000558 | furniture | pages [21] -->
获取更多资讯

<!-- b000559 | furniture | pages [22] -->
Team # 2401102

<!-- b000560 | prose | pages [22] -->
• Level I: High Preservation (HLV ≥0.7)

<!-- b000561 | furniture | pages [22] -->
Page 21 of 25

<!-- b000562 | prose | pages [22] -->
Entails advanced measures for preservation and prevention, including relocation for protection when necessary.

<!-- b000563 | prose | pages [22] -->
微信公众号：数学模型

<!-- b000564 | prose | pages [22] -->
• Level II: Moderate Preservation (0.3 ≤HLV < 0.7) Encompasses comprehensive protection against common hazards.

<!-- b000565 | prose | pages [22] -->
• Level III: Low Preservation (HLV < 0.3) Includes routine maintenance and disaster-specific precautions.

<!-- b000566 | prose | pages [22] -->
Application: Temple of Literature in Hanoi, Vietnam 6.4

<!-- b000567 | prose | pages [22] -->
Value Assessment and Conservation

<!-- b000568 | prose | pages [22] -->
According to our insurance model, Vietnam is expected to be significantly affected by extreme weather events in the future. However, due to high risks and low premiums, it is unlikely to be insured. So, we chose the Temple of Literature(Văn Miếu–Quốc TửGiám) in Hanoi, Vietnam as our subject.[8]

<!-- b000569 | prose | pages [22] -->
微信号：MATHmodels

<!-- b000570 | prose | pages [22] -->
In 1070 AD, Emperor Lý Thánh Tông in Vietnam decided to establish the Temple of Literature to worship Confucius. In 1076 AD, Emperor Lý Nhân Tông built the Imperial Academy next to the Temple of Literature, which became the first formal academy in Vietnam. Today, the Temple of Literature still hosts annual religious ceremonies and cultural activities such as calligraphy and Chinese chess.

<!-- b000571 | prose | pages [22] -->
According to the model presented in section 6.3, we have assigned a HLV of 0.463 to the Temple of Literature, suggesting a medium level of preservation is advisable. Using the methods described in section 3.3, the site is predicted to face increasing risks of floods and cyclones in the future.

<!-- b000572 | prose | pages [22] -->
In light of this, we recommended the following conservation measures:

<!-- b000573 | prose | pages [22] -->
• Regularly clean and clear the riverbeds and drainage channels.

<!-- b000574 | prose | pages [22] -->
• Apply waterproofing treatment to the surface of the buildings.

<!-- b000575 | prose | pages [22] -->
• Plant trees in the vicinity.

<!-- b000576 | prose | pages [22] -->
• Strengthen the load-bearing structures. Implementing these protection measures can effectively prevent damage caused by flooding, ero- sion, and structural collapse due to strong winds.

<!-- b000577 | prose | pages [22] -->
Estimated Conservation Effectiveness

<!-- b000578 | prose | pages [22] -->
We continued to use the indicators from the value estimation to measure the difference between with protection and without protection. However, the historical significance of a landmark will not change in a short period, predicting future local culture research is challenging, and the ”community” indicator is binary (0-1) and does not show significant changes. Therefore, we considered the other five indicators and replaced the ”age” index with “expected lifespan”. We set the current level to a standard value 1 for ease of comparing conservation effectiveness.

<!-- b000579 | furniture | pages [22] -->
关注数学模型

<!-- b000580 | furniture | pages [22] -->
2

<!-- b000581 | furniture | pages [22] -->
MATHmodels

<!-- b000582 | furniture | pages [22] -->
获取更多资讯

<!-- b000583 | furniture | pages [23] -->
Team # 2401102

<!-- b000584 | furniture | pages [23] -->
Page 22 of 25

<!-- b000585 | prose | pages [23] -->
微信公众号：数学模型

<!-- b000586 | caption | pages [23] -->
Figure 13: Prediction of Protection Effect

<!-- b000587 | prose | pages [23] -->
The predicted conservation effectiveness is shown in Figure 13.

<!-- b000588 | prose | pages [23] -->
微信号：MATHmodels

<!-- b000589 | prose | pages [23] -->
• Without protection: Extreme weather will result in building damage, water logging on the premises, reduced visitors, and the inability to conduct development and educational activities. Due to the lack of insurance, these losses cannot be compensated. • With protection: Damage caused by extreme weather is significantly reduced, and the time when the site cannot operate due to water logging is greatly reduced. Furthermore, with the improve- ment of preservation measures, the number of visitors and activities may increase. So we can say that our HLP model for estimating the extent of protection to historical landmark is reliable and effective.

<!-- b000590 | prose | pages [23] -->
7

<!-- b000591 | heading | pages [23] -->
Strength and Weakness

<!-- b000592 | heading | pages [23] -->
Strength

<!-- b000593 | prose | pages [23] -->
• For Model I(DBMI) ,we employed time series analysis to develop a reasonably accurate model for extreme weather forecasting. Additionally, we utilized expertise in insurance to calculate the insurance company’s demand and effectively balanced demand and risk for sustainability through optimization.

<!-- b000594 | prose | pages [23] -->
• For Model II(HLPM), we chose multi-dimensional analysis and applied the Analytic Hierarchy Process, and considered relevant literature to select indicators and weights, resulting in weighted outcomes that closely resemble the true value of historical landmarks. We then implemented corresponding protection measures and assessed their effectiveness based on real case.

<!-- b000595 | heading | pages [23] -->
Weakness

<!-- b000596 | prose | pages [23] -->
• For Model I(DBMI) , as we only have several thousand event records within 100 years, our model is less applicable for long-term risk predictions and risk predictions on smaller areas with finer regional divisions.

<!-- b000597 | furniture | pages [23] -->
关注数学模型

<!-- b000598 | furniture | pages [23] -->
2

<!-- b000599 | furniture | pages [23] -->
MATHmodels

<!-- b000600 | furniture | pages [23] -->
获取更多资讯

<!-- b000601 | furniture | pages [24] -->
Team # 2401102

<!-- b000602 | furniture | pages [24] -->
Page 23 of 25

<!-- b000603 | prose | pages [24] -->
• For Model II(HLPM), it focuses on assessing the degree of preservation, but it is unable to pro- vide specific guidance on how to choose specific protective measures based on the degree of preservation.

<!-- b000604 | prose | pages [24] -->
微信公众号：数学模型

<!-- b000605 | heading | pages [24] -->
References

<!-- b000606 | references | pages [24] -->
[1] Lorenzo Fantini et al. An Insurance Risk Framework for Climate Adaptation. Boston Con-sulting

<!-- b000607 | references | pages [24] -->
Group. Dec. 2023. url: https://www.bcg.com/publications/2023/an-insurance-risk-framework-

<!-- b000608 | references | pages [24] -->
for-climate-adaptation (visited on 02/03/2024).

<!-- b000609 | references | pages [24] -->
[2] Our World in Data. Natural Disasters. https://ourworldindata.org/natural-disasters

<!-- b000610 | references | pages [24] -->
Agriculture

<!-- b000611 | references | pages [24] -->
[3] United

<!-- b000612 | references | pages [24] -->
States

<!-- b000613 | references | pages [24] -->
Department

<!-- b000614 | references | pages [24] -->
of

<!-- b000615 | references | pages [24] -->
Climate

<!-- b000616 | references | pages [24] -->
Hubs.

<!-- b000617 | references | pages [24] -->
Extreme

<!-- b000618 | references | pages [24] -->
Weather.

<!-- b000619 | references | pages [24] -->
https://www.climatehubs.usda.gov/content/extreme-weather. Accessed: 2024-02-03. 2023.

<!-- b000620 | references | pages [24] -->
微信号：MATHmodels

<!-- b000621 | references | pages [24] -->
[4] Lane, Morton. (2000). Pricing risk transfer transactions. ASTIN Bulletin. 30. 259-293.

<!-- b000622 | references | pages [24] -->
[5] Insurance Council of Australia. (n.d.). Data hub. Insurance Council of Australia. Retrieved Febru-

<!-- b000623 | references | pages [24] -->
ary 5, 2024, from https://insurancecouncil.com.au/industry-members/data-hub/

<!-- b000624 | references | pages [24] -->
[6] Christopher A. Jensen and Jessamie Yule(s). (2022). Response strategies used to mitigate

<!-- b000625 | references | pages [24] -->
the effect of extreme weather on rural and remote housing in Australia. IOP Conference

<!-- b000626 | references | pages [24] -->
Series: Materials Science and Engineering, 1218(1), 012049. https://doi.org/10.1088/1757-

<!-- b000627 | references | pages [24] -->
899X/1218/1/012049

<!-- b000628 | references | pages [24] -->
[7] Si Lichao. Research on the Protection Strategy and Techniques for Taiyuan’s Modern and Con-

<!-- b000629 | references | pages [24] -->
temporary Cultural Heritage Buildings Based on Value Assessment. 2021. Taiyuan University of

<!-- b000630 | references | pages [24] -->
Technology, MA thesis. doi:10.27352/d.cnki.gylgu.2021.000262.

<!-- b000631 | references | pages [24] -->
[8] Centre for Research on the Epidemiology of Disasters - CRED, Université catholique de Louvain.

<!-- b000632 | references | pages [24] -->
(2024). EM-DAT Public Platform. Retrieved February 5, 2024, from https://public.emdat.be/data

<!-- b000633 | furniture | pages [24] -->
关注数学模型

<!-- b000634 | furniture | pages [24] -->
2

<!-- b000635 | furniture | pages [24] -->
MATHmodels

<!-- b000636 | furniture | pages [24] -->
获取更多资讯

<!-- b000637 | furniture | pages [25] -->
Team # 2401102

<!-- b000638 | furniture | pages [25] -->
Page 24 of 25

<!-- b000639 | heading | pages [25] -->
Letter of Recommendation

<!-- b000640 | prose | pages [25] -->
To whom it may concern,

<!-- b000641 | prose | pages [25] -->
We are a team of Insurance of Catastrophes Modelers(ICM). Extreme weather events have caused

<!-- b000642 | prose | pages [25] -->
微信公众号：数学模型

<!-- b000643 | prose | pages [25] -->
increasing losses in recent years. Accordingly, insurance companies are going to change how and where they underwrite. According to models, Vietnam faces high risk of extreme weather events in the future, especially floods and cyclones. Therefore, insurance companies are unlikely to underwrite policies for property losses caused by extreme weather events in your region.

<!-- b000644 | prose | pages [25] -->
However, some historical landmarks are vulnerable to extreme weather, such as the Temple of Litera- ture(Văn Miếu–Quốc TửGiám). We believe that protective measures can be implemented to safeguard it. A model has been established to assess its value in four dimensions: economy, history, culture, and community. We have prepared suggested measures, a timetable, and a budget for you based on this.

<!-- b000645 | prose | pages [25] -->
Project Time Budget Budget Explanation

<!-- b000646 | prose | pages [25] -->
微信号：MATHmodels

<!-- b000647 | prose | pages [25] -->
1.4 million Viet-

<!-- b000648 | prose | pages [25] -->
Cleaning

<!-- b000649 | prose | pages [25] -->
Rainy sea-

<!-- b000650 | prose | pages [25] -->
In 2023, the average monthly wage for

<!-- b000651 | prose | pages [25] -->
namese Dong per

<!-- b000652 | prose | pages [25] -->
riverbeds and

<!-- b000653 | prose | pages [25] -->
son

<!-- b000654 | prose | pages [25] -->
drainage channels

<!-- b000655 | prose | pages [25] -->
month

<!-- b000656 | prose | pages [25] -->
Vietnamese is 700 Vietnamese Dong. It is estimated that three workers would work for two days each month

<!-- b000657 | prose | pages [25] -->
0.8 million Viet-

<!-- b000658 | prose | pages [25] -->
Waterproofing

<!-- b000659 | prose | pages [25] -->
January to

<!-- b000660 | prose | pages [25] -->
To ensure better preservation, polymer

<!-- b000661 | prose | pages [25] -->
namese Dong per

<!-- b000662 | prose | pages [25] -->
treatment

<!-- b000663 | prose | pages [25] -->
March

<!-- b000664 | prose | pages [25] -->
square meter

<!-- b000665 | prose | pages [25] -->
Planting trees March and

<!-- b000666 | prose | pages [25] -->
0

<!-- b000667 | prose | pages [25] -->
April

<!-- b000668 | prose | pages [25] -->
Strengthening

<!-- b000669 | prose | pages [25] -->
Rainy sea-

<!-- b000670 | prose | pages [25] -->
Unknown

<!-- b000671 | prose | pages [25] -->
aged structures

<!-- b000672 | prose | pages [25] -->
son

<!-- b000673 | prose | pages [25] -->
material is recommended

<!-- b000674 | prose | pages [25] -->
Local student volunteers for tree planting are encouraged for educational purposes

<!-- b000675 | prose | pages [25] -->
It is challenging to estimate the cost as it depends on the actual aging condition

<!-- b000676 | prose | pages [25] -->
With these measures, we can greatly reduce potential losses The effectiveness of caused by extreme weather events. preservation has been estimated and is shown in the chart on the right.

<!-- b000677 | prose | pages [25] -->
In the event of severe weather, take protective measures. We will continue to reduce the risks associated with our insur- ance products.

<!-- b000678 | prose | pages [25] -->
We sincerely hope that the Temple of Literature can serve as a treasure of human civilization and make a long-term contribution to the community.

<!-- b000679 | prose | pages [25] -->
Sincerely,

<!-- b000680 | furniture | pages [25] -->
Team #2401102

<!-- b000681 | furniture | pages [25] -->
关注数学模型

<!-- b000682 | furniture | pages [25] -->
2

<!-- b000683 | furniture | pages [25] -->
MATHmodels

<!-- b000684 | furniture | pages [25] -->
获取更多资讯
