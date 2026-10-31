MCM/ICM

Summary Sheet

Summary

The first priority of survival is getting protection from the extreme weather. —Bear Grylls

More frequent and severe extreme weather events are causing greater damage to people’s prop- erty, leading to a reevaluation of the sustainability of insurance companies. On one hand, maintaining enough customers for long-term healthy operation is crucial; on the other hand, avoiding excessively high compensation risks to remain profitable is essential. Therefore, we assessed the sustainability of the insurance sector in areas that were frequently impacted by extreme weather events from two per- spectives: insurance demand and total risk.

For Task 1, we developed a Property Insurance Posture Model for insurance companies. We categorized extreme weather into 4 types and used an ARIMA model to forecast the future risk of extreme weather for each region-disaster pair, and calculated the expected loss. Then, we used Lane’s AFC model to calculate premiums. To measure demand with premiums, we introduced the insurance demand curve. Finally, we established Demand-Risk Equilibrium Model for Insurance(DBMI) to provide decisions on whether to underwrite insurance in specific regions.

Next, we applied the model above to Australia and Southeast Asia, where approximately 60 years of data from 3000 records were available. Then we applied ARIMA model on selected area-event series, with an eminent fit: R2 consistently above 0.625, and IC all below 300. Consequently, we forecast the risks for 2024-2027. This has resulted in the determination of premiums ranging from $119.2 to $1295.6. The optimal solutions indicated that in Australia, QLD and WA should be underwritten; in SE Asia, PHL and THA.

For Task 2, we introduced Innovative Risk Prediction Property Development Method(IRPPDM), which integrated DBMI with real estate companies’ willingness index to construct a Willingness-Risk coordinate system. We specifically targeted High Risk-High Willingness areas, providing 3 possible risk reassessment methods to help transfer them into Low Risk-High Willingness category.

For Task 3, we used Historic Landmark Preservation Model to help community leaders. We estimated the significance of historic landmarks by AHP method considering 8 indicators in 4 dimen- sions. Then we offered suggestions considering both the extent of significance and predicted risks. According to our model, Temple of Literature in Hanoi, Vietnam had a score of 0.463, facing risks of floods and cyclones. Considering its features, we offered 4 tailored suggestions.

In the end, we stated the strengths and weaknesses of models. Based on their performances in application, Property Insurance Posture Model reasonably balanced demand and risk, and Historic Landmark Preservation Model was comprehensive in measuring value.

1 Introduction

1.1 Problem Background

微信公众号：数学模型 Over the past few years, more than 1,000 extreme weather events have resulted in more than $1 trillion in global losses. Swiss Re predicted that losses from weather-related events in Australia, Canada, France, Germany, Japan, the U.K., and the U.S. could increase by 35-120 percent by 2040, due to the impact of natural disasters such as floods, hurricanes, and wildfires. [1]

微信号：MATHmodels

The frequent occurrence of extreme weather events presents a complex challenge for the property insurance industry. These events can lead to substantial financial losses due to increased claims, testing the industry’s resilience. Insurers must navigate the dual pressures of maintaining profitability and offering affordable premiums.

Therefore, there’s a growing need for risk assessment models that accurately reflect the high level risks associated with extreme weather events. This will help insurers to price policies more effectively and encourage investment in protective measures for properties at risk.

1.2 Our Work

For insurance companies, we have developed a property insurance deployment model to assist them in selecting the areas to underwrite against extreme weather events, ensuring the sustainability of their operations. Specifically, we measured sustainability based on the company’s total demand and the total risk they face: Demand reflected the consideration of profitability, while underwriting risk was related to long-term healthy operation. After the model was established, we applied it to two different regions to validate its feasibility.

For real estate developers, we extended the insurance model mentioned above to assist in the decision-making process for property development, providing insights on where, how, and whether to construct buildings. Specifically, using the weather risk predictions obtained from the insurance model, we provided corresponding strategies that developers could implement to mitigate risks during the construction of properties.

For community leaders without the shelter of extreme weather event insurance, we have developed 微信公众号：数学模型 a historical landmark significance model that assesses the significance of historical landmarks based on four aspects: history, culture, economy, and community. Ultimately, this helps them determine the extent of protection needed for their historical landmarks.

The detailed flowchart is illustrated in Figure 2 below:

微信号：MATHmodels

2 Assumptions and Notations

Assumption1: Insurance companies bear the risk independently Justification: In reality, insurance companies often diversify risks through financial products, govern- ment support, and other means. Since we focus on the design of insurance products, we assume that insurance companies do not adopt risk diversification measures.

Assumption2: Insurance demand is negatively correlated with price, and insurance demand re- flects the number of customers. Justification: Insurance, as a normal good, experiences a decrease in demand as its price increases.

微信公众号：数学模型 And insurance demand corresponds to the number of insurance policies, and it can be directly seen as reflecting the number of customers.

Assumption3: Existing real estate development processes do not primarily consider extreme weather risk predictions. Justification: Extreme weather events have low frequencies and high randomness, making them dif- ficult to predict. Additionally, we conducted keyword searches on Google Scholar, and there is little discussion on incorporating extreme weather risk predictions into the primary indicators for real estate development.

Assumption4: The data we use is true and reliable.

Justification: Our data sources include international statistical agencies, academic databases, and rep-

utable insurance companies. Therefore, we can confidently state that the data we use is accurate and 微信号：MATHmodels reliable for modeling purposes.

Notations

Symbol Definition

EL Expected Loss PEL Frequncy of Loss Quantity of Insurance Demand Q D Insurance Demand R Total Risk for Insurance Sustainability Sustainability for Insurance Company DBMI Demand-Risk Equilibrium Model for Insurance IRPPDM Innovative Risk Prediction Property Development Method HLPM Historical Landmark Preservation Model

3 Model I: Property Insurance Posture Model

3.1 The Types of Extreme Weather Events

According to USDA Climate Hubs, extreme events are occurrences of unusually severe weather or climate conditions that can cause devastating impacts on communities and agricultural and natural ecosystems.

NASA provided a brief summary of global extreme weather events, including heat waves, wildfires, droughts, tropical cyclones, heavy precipitation, floods, high-tide flooding, and marine heat waves.[3] As illustrated in Figure 3, we mainly discuss the impact of extreme weather events on property insur- ance, so we only focuse on four main categories: droughts, floods, tropical cyclones, and wildfires.

微信公众号：数学模型 微信号：MATHmodels

• Wildfires: Dry conditions increase the risk of wildfires. With global temperatures on the rise, some regions may experience more frequent and intense wildfires, posing a threat to life and property.

• Floods: Floods present a substantial threat to properties as heightened atmospheric moisture can result in more frequent and heavier rainfall, which can overwhelm both natural and man-made water management systems. This is especially true in coastal areas due to the compounding effect of rising sea levels.

• Tropical Cyclones: Tropical cyclones, fueled by warmer ocean temperatures and more humid air, are likely to cause more severe and long-lasting rainfall events. These natural phenomena can severely impact properties, particularly through enhanced coastal flooding, driven by rising sea levels that elevate storm surge impacts.

• Droughts: The rising aridity in certain regions, exacerbated by global warming, has adverse effects on properties. This not only depletes ground moisture but also perpetuates a cycle of warming and moisture loss, leading to soil degradation, foundation issues, and an increased risk of fire hazards.

• Others: Other types can be listed as heat extremes, heavy precipitation, high-tide flooding, ma- rine heat waves,etc.

3.2 Predicting Extreme Weather Events: Based on ARIMA

To accurately calculate the expected loss of insurance products, insurance companies must precisely predict the probability of various extreme weather events. This step is significant for insurance pricing and risk control.

Given the uncertainty, complexity, and randomness of extreme weather events, we propose the use of time series analysis method to fit and predict the frequency of extreme weather events more accu- rately. Through this approach, we aim to improve the accuracy of predictions to better price insurance products and manage risk.

微信公众号：数学模型

3.2.1 Series Stabilization

For non-stationary time series, predictive models may fail due to changes in the statistical properties of the series over time. Therefore, differencing is employed to reduce or eliminate the trend and seasonal components of the time series, thereby stabilizing the series.

The first-order difference sequence y(n) is obtained by taking the difference between consecutive terms of the original sequence x(n) . If the first-order difference sequence is still not stationary(usually use ADF to test), we can repeat the process to obtain the second-order difference sequence z(n):

y(i + 1) = x(i + 1) −x(i) (1)

z(i + 2) = y(i + 2) −y(i + 1) (2)

where: 微信号：MATHmodels

• x is the original sequence.

• y is the first-order difference sequence.

• z is the second-order difference sequence.

• i represents the timestamp.

3.2.2 ARIMA Model

For the stabilized sequence, we employ the Autoregressive Integrated Moving Average (ARIMA) model for prediction. This model integrates Autoregressive (AR) and Moving Average (MA) methods, incorporating differencing to enhance data stationarity. By examining the autocorrelation in historical data, the model assumes future trends will mimic historical patterns, thereby forecasting future data points.

ARIMA(p,i,q) can be represented by the following equation:

Xt = c + ϕ1Xt−1 + ϕ2Xt−2 + . . . + ϕpXt−p −θ1εt−1 −θ2εt−2 −. . . −θqεt−q + εt (3)

where:

• Xt represents the time series(usually the difference sequence).

• c is the constant term.

• ϕ1, ϕ2, . . . , ϕp are the autoregressive coefficients corresponding to lag time steps 1, 2, . . . , p.

• θ1, θ2, . . . , θq are the moving average coefficients corresponding to lag time steps 1, 2, . . . , q.

• εt represents the white noise error term at time point t.

Obtain appropriate parameters through program execution to determine ARIMA(p, i, q), and com- plete model validation. Then we can get the frequency prediction of different extreme weather events for each area.

Example: Fitting Cyclones and Tornadoes

We conducted first-order differencing on the annual data of tornadoes and hurricanes in New South Wales, Australia. Figure 4 displays the ARIMA model’s fitted line, demonstrating a satisfactory model 微信公众号：数学模型 fit. Based on this, we concluded that our approach is suitable for extreme weather data characterized by significant fluctuations and strong seasonality.

微信号：MATHmodels

3.3 Insurance Price and Demand

3.3.1 Two Types of Insurance

It is important to note the role of insurance in mitigating the impact of extreme weather events, including indemnity-based insurance, index-based insurance, and insurance-linked securities. These tools can assist households and enterprises in adapting to the increasing risks associated with climate change.

Here we mainly focus on the two types of insurance.We determine the type of insurance based on per capita GDP: Developed regions typically use indemnity-based insurance, while developing regions typically use index-based insurance.

Indemnity-based Insurance

It compensates for actual losses caused by an event. Data is collected on the financial loss caused by different types of extreme weather events and the probability of loss in an area over the years. After processing the data, we can obtain the total losses and payouts for each year. This allows us to calculate the expected loss(EL) :

∑ Average Lost of event j EL = (4) Average Affected People of event j j

Index-based Insurance

Payouts to policyholders depend on an index that strongly correlates with losses in income or assets. To estimate loss, we should use a metric to measure the severity of events. However, losses vary from event to event and are measured differently, so the data must be normalized and weighted to obtain a loss index γ. Thus we can determine the extent of loss and expected loss(EL):

∑ γj × Standard Compensation of event j EL = (5) 微信公众号：数学模型 j

3.3.2 Price of Insurance

According to the methods above, we can obtain expected loss caused by extreme weather events. Based on this, we consider the pricing of insurance products.

Insurance premiums usually consist of two parts: pure premium and additional premium. Accord- ing to Lane’s LFC model[4], we use EL to measure the pure premium while considering the expected excess return(EER) to measure addtional premium.Then we get the insurance price, or Premium(P):

P = EL + EER (6)

微信号：MATHmodels We have provided specific formulas to calculate EL in section 3.3.

EER depends on the frequency and severity of loss, represented by the Cobb-Douglas function, as follows: EER = 0.55 × PEL0.495 × CEL0.574 (7) CEL = EL (8) PEL where:

• PEL is referred to as frequency of loss

• CEL is used to measure severity of loss

3.3.3 Demand for Insurance

To measure the revenue of the insurance company, we also need to assess demand(D) of insurance products. Since insurance demand is influenced by many factors in reality, we abstractly use Marshal- lian Demand Curve to simplify analysis. According to this model, demand is inversely proportional to price,as the yellow curve in Figure 5:

where:

(9) Q = aP + b, a < 0, b > 0

Additionally, we consider property owner’s influence on insurance company. The choices of one 微信公众号：数学模型 single property owner are unlikely to significantly affect market demand, but the change of consumer trend in the market would lead to shifts in the demand curve. For example, if consumer’s willingness to consume increases, the demand curve would shift to the right as blue curve in Figure 5.

3.4 Demand-Risk Equilibrium Model for Insurance

We have constructed the Demand-Risk Equilibrium Model for Insurance(DEMI) to comprehen- sively assess the sustainability of an insurance company, considering two aspects: the total demand for insurance and the overall risk undertaken by the insurance company.

The reasons for selecting these two aspects are as follows:

Firstly, there is a significant positive correlation between the customer number of insurance com- pany(means the same as total demand) and the profitability of the insurance company. 微信号：MATHmodels However,insurance companies cannot indiscriminately increase the number of policies, as an ex- cessive increase in extreme weather risk may lead to the insurance company facing insurmountable large claims. Therefore, we introduce the concept of overall risk to impose constraints.

Aim to assist insurance companies in deciding whether to underwrite policies in certain areas, we initially divide high-risk areas within the insurance company’s business scope into n distinct areas and introduce binary variables xi:

{ 1 choose to underwrite in area i, xi = (10) refuse to underwrite in area i . 0

Total Demand

Based on the insurance demand model derived from ARIMA model of extreme weather events, we can obtain forecasts for insurance demand in the future for area i, denoted as di. For the insurance company, its total demand is the sum of the demands from the underwritten areas,which can be defined as follows:

n ∑ xi · di D = (11) i=1

Overall Risk

Based on the predictive model mentioned in Section 3.4, we can derive independent future occurrence probabilities for extreme weather events in different areas. To assess the overall risk, we must consider the impact of different types of extreme weather events and the aggregation of risks across areas.

We opt for a severity weighting method to evaluate the impact of different extreme weather events and obtain the formula for calculating the total risk ri for area i.

∑ pij · αj ri = (12) j ∑ αj = 1 (13) j where:

微信公众号：数学模型

• pij: Probability of event extreme weather type j occurring in area i.

• αj: Impact degree of extreme weather type j.

• j: Different types of extreme weather events.

Optimization for Sustainability

Ultimately, we propose DEMI to assess insurance companies’ sustainability. It is a dual-objective optimization model, wherein we introduce a weight parameter λ to balance the importance of overall risk and total demand.

With an appropriate choice of λ, the model can effectively address both aspects. The specific definition of the model is as follows:

微信号：MATHmodels max Sustainability = λD −(1 −λ)R (14)

Its constraints are the limitations imposed by the binary variables xi mentioned earlier in the this section.

4 Case Study: Australia and Southeast Asia

4.1 Data Processing and Analysis

Data Source and Area Segmentation

We have gathered a total of 744 records of extreme weather events in Australia dating back to 1967 and 2,021 records of extreme weather events in Southeast Asia since 1970.[5] Given Australia’s geographic isolation from other continents, we treat it as a research region, with its individual states considered separate areas. In contrast, due to the multitude of Southeast Asian nations and their relatively small land areas, we consider Southeast Asia as a research region, with different countries categorized as distinct areas.

After excluding missing data and natural disasters outside the scope of our study, we obtained

the categorization of extreme weather events varies between the two regions.

Selection of Study Scope

Based on the original data, in Australia, we choose to classify cyclones and tornadoes into one cate- gory, and hail, hailstorms, and storms into another category, resulting in a total of four types of extreme 微信公众号：数学模型 weather events: bushfire, cyclone, flood, and storm. In Southeast Asia, we retained the original classi- fication: drought, flood, and storm.

微信号：MATHmodels Next, we proceeded to select areas that were significantly impacted by extreme weather events for inclusion in the insurance company’s consideration of whether to underwrite. We determined whether they qualified as high-risk areas based on the frequency distribution of extreme weather events(in Figure 8) in each area.

Lastly, we have chosen the following areas to analysis: in Australia, New South Wales (NSW), Queensland (QLD), Victoria (VIC), and Western Australia (WA), while in Southeast Asia, Indonesia (IDN), Philippines (PHL), Thailand (THA), and Vietnam (VNM) – we consider Thailand to have a higher risk level despite its contribution to the total count being less than 10% due to the high overall frequency in Southeast Asia.

4.2 Use of ARIMA Model

Applying the previously mentioned methodology, we initially conducted a second-order differencing analysis on the frequency of certain types of extreme weather events in each area of the two regions.

Subsequently, we employed the ARIMA model for time series forecasting, yielding equations in the following form (taking the example of bushfire in NSW):

微信公众号：数学模型 ARIMA(3, 2, 1) : Y(t) = −0.002 −0.651Y(t−1) −0.412Y(t−2) −0.105Y(t−3) −0.952ε(t−1) (15)

Then applying the model to all time series of each area-event pair, we obtained corresponding prediction curves. These curves exhibit an excellent fit to the original data, as illustrated in Figures 9 . Here, we provide examples from IND in Southeast Asia and WA in Australia.

微信号：MATHmodels

Next, we employ the coefficient of determination R2 as well as the Akaike Information Criterion (AIC) and Bayesian Information Criterion (BIC) to assess the performance of each model. The defini- tions of AIC and BIC are as follows:

AIC = −2 ln(L) + 2k (16)

BIC = −2 ln(L) + k ln(n) (17)

where:

• L represents the maximum likelihood of the model.

• k is the number of model parameters.

• n is the number of data points.

Part of our model evaluation results are presented in Table 1. Both AIC and BIC remain at accept- able levels, and R2 values consistently exceed 0.6.

Thus, we believe that our model is robust to effectively forecast future extreme weather events. Finally we get the frequency prediction of different area-event for the next 3 years.

R2 Area-Event AIC BIC IDN-Drought 83.023 94.731 0.745 IDN-Flood 279.993 295.603 0.665 IDN-Storm 116.088 125.844 0.767 微信公众号：数学模型 PHL-Drought 82.001 97.611 0.839 PHL-Flood 245.232 254.988 0.629 PHL-Storm 277.507 289.214 0.715 THA-Drought 74.377 86.085 0.837 THA-Flood 222.739 236.398 0.726 THA-Storm 165.383 177.090 0.781 VNM-Drought 64.436 78.095 0.833 VNM-Flood 203.976 217.635 0.781 VNM-Storm 222.338 234.045 0.784

微信号：MATHmodels

4.3 Apply DEMI to Two Areas

4.3.1 Determination of Premiums and Demand

Based on the per capita GDP in Australia and Southeast Asia, we have chosen to calculate the EL for each area using both indemnity-based insurance and index-based insurance models.

By using formulas above, we have computed the probability of loss(PEL) for both Australia and Southeast Asia for the year 2024. By utilizing the PEL and the EL, we calculate the Conditional Ex- pected Loss (CEL),which ultimately allows us to determine the insurance premium:

As shown in Figure 10, it is evident that due to varying levels of risk, there are differences in insurance premiums across different areas. Next, we will incorporate the insurance demand model to obtain the demand di for each area.

4.3.2 Solving DBMI

We have observed that within the range of λ values between 2∗10−5 and 1∗10−6, the model effectively balances risk and demand. Ultimately, we have selected a λ value of 5 ∗10−6, resulting in the optimal insurance coverage plan as follows:

• For the Australian region, we provide coverage for QLD and WA while not covering VIC and NSW.

• In the Southeast Asian region, we offer coverage for PHL and THA while not covering IND and 微信公众号：数学模型 VNM.

Next, we would analyze this outcome by risk and demand data.

Country NSW QLD VIC WA Premium 798.05 823.69 1295.62 267.51 Total Demand 74327 73460 58857 90847 Total Risk 0.54162 0.30394 0.76552 0.06285

In the case of Australia, the model opts for the lowest-risk option, WA, over VIC, which exhibits significantly higher risk compared to other areas. This decision aligns with the sustainability principle 微信号：MATHmodels of risk avoidance. Additionally, we observe that the demand and premiums for NSW and QLD are similar. The model chooses QLD, which has a lower overall risk, thus demonstrating a balance between risk and profitability.

Country IDN PHL THA VNM Premium 543.94 119.20 717.82 267.28 Total Demand 72802 94039 64109 86635 Total Risk 0.29424 0.05597 0.09301 0.17466

For Southeast Asia, we can observe that the two selected areas share a significant characteristic: they both exhibit low overall risk. Additionally, the choice of THA, which commands the highest premiums, enhances the profitability of the insurance company.

As for the other two areas, IDN, despite having high premiums, also carries high risks, making it a less favorable option. On the other hand, VNM presents relatively high risks but offers lower premiums, resulting in a suboptimal cost-benefit ratio for insurance coverage.

In conclusion, we believe that our model has reasonable outcomes in both regions. These results re- flect the balance between profitability and risk management for insurance company. The model’s accuracy in forecasting extreme weather events, coupled with its strong interpretability, provides valuable insights for the insurance company in addressing extreme weather events.

5 Innovative Risk Prediction Property Development Method

Based on Assumption3, we propose innovative risk prediction property development method that considers extreme weather risk predictions. This involves adapting our DBIM to assist developers in evaluating where, how, and whether to build on certain sites.

5.1 Whether to Build: Determined by Willingness and Risk

To provide housing and other real estate services for the ever-growing communities and populations, real estate companies have their own system for for selecting development areas. 微信公众号：数学模型 The specific methods fall outside the scope of our study. Anyway, they can utilize such a system to perform assessment of the developmental potential for each area,which we call as Development Willingness Index (DWI). A higher DWI value indicates a more optimistic profit outlook for property developers, and correspondingly, a stronger inclination to develop such areas.

Next, we adapt our DBMI s weighted risk - to measure the extreme weather risk in a specific area. By setting the development index on the vertical axis and total risk on the horizontal axis, we construct a Cartesian coordinate system(shown in Figure 11(a)). Each prospective development area corresponds to a unique point within this coordinate system. This system is divided into four quadrants, representing different combinations of risk and willingness:

微信号：MATHmodels

• Quadrant I (Low Risk - High Willingness): Areas in this quadrant exhibit low extreme weather risk and a strong desire for development. For these areas, real estate developers need not pay much attention to extreme weather risk. Therefore, these areas can be developed according to the company’s own development system. However, they are not the focus of our method.

• Quadrant II (High Risk - High Willingness): Areas in this quadrant display both a strong desire for development and face high extreme weather risk. If risk reduction measures can be imple- mented to lower the risk while maintaining high willingness, these areas can transit from Quad- rant II to I(Figure 11 (b)), becoming feasible options for developers. Otherwise, they should abandon development plans in such an area. Our method focuses on this quadrant.

• Quadrants III & IV (Low Willingness): Areas in these two quadrants exhibit low development willingness, even without considering the risk of extreme weather, these areas are not suitable candidates for development. Consequently, they are also not the focus of our method.

Next, we will focus on the areas situated in Quadrant II and discuss how and where to build in order to facilitate their transition to Quadrant I.

5.2 How and Where to build: Addressing Specific Event Risk

In our discussion concerning areas in Quadrant II, we focus on how and where to implement real estate development. The objective of developing these areas is to mitigate extreme weather risk effectively 微信公众号：数学模型 while maintaining development willingness, reducing it to an acceptable level. We propose specific measures and assessment methods for mitigating potential risk associated with different types of ex- treme weather.[6]

Bushfire

To mitigate the risk of wildfires, site selection is the most direct approach. Preferred strategies include choosing sites in relatively moist areas and avoiding locations near forests. Additionally, measures taken in house construction can also reduce the risk of fires. These include avoiding the use of highly flammable insulation materials and opting for fire-resistant materials.

To quantify the effectiveness of site selection in reducing wildfire risk, we introduce the adjusted wildfire risk index p∗ b, defined as: 微信号：MATHmodels pb p∗ b = (18) 1 + d where:

• pb is the original wildfire risk, predicted from the DBMI

• d is the distance from the selected site to potential fire source

Cyclone & Storm

Since wind-related disasters often accompany heavy rainfall, we discuss them together here. Due to the widespread impact of cyclones and storms, avoiding their impacts through location selection is ineffective. Therefore, enhancing the resistance of buildings to extreme events becomes a more effec- tive strategy. This includes strengthening the structural design of houses, improving drainage systems around houses, and installing backup power systems.

To quantify the effect of strengthening building structures in reducing tornado risk, we define the adjusted tornado risk index p∗ c as follows:

c = pc × Standard Building Strength p∗ (19) Enhanced Building Strength where:

• pc is the original tornado risk, predicted from the DBMI.

• Standard Building Strength represents the structural capacity without reinforcement.

• Enhanced Building Strength represents the structural capacity with reinforcement.

Drought

While the impact of drought on buildings may not be as direct or severe as some other extreme weather events, prolonged drought can potentially have negative effects on building structures. In terms of location selection, priority should be given to locations with stable foundations, which can help mitigate potential damage caused by soil drying and shrinking. Regarding the construction of houses, building design should focus on the integration of water-saving systems to minimize water consumption.

To quantify the effectiveness of constructing water-saving systems and selecting foundations in reducing drought risk, we define the adjusted drought risk index p∗ d as follows: 微信公众号：数学模型 d = pd × Soil Shrinkage Coefficient p∗ (20) Water Efficiency Coefficient where:

• pd is the original drought risk, predicted from the DBMI.

• Soil Shrinkage Coefficient measures the sensitivity of the soil to water deficiency.

• Water Efficiency Coefficient represents the efficiency of the water-saving system.

Finally, based on the adjusted risk values p∗ j, we can calculate the new total risk r∗using the DBMI. By analyzing this value, we can help determine where, how, and whether to build on certain sites.

微信号：MATHmodels

5.3 Conclusion for IRPPDM

In the preceding sections of this chapter, we have presented the complete workflow of the IRPPDM, with its core concept being the integration of real estate companies’ regional analysis methods with our risk prediction model. This integration allows us to classify different areas based on risk and development willingness, and make decisions on whether construction should proceed accordingly.

Specifically, for high-risk, high-willingness areas, we have analyzed specific events response mea- sures and evaluated the risk levels after implementing specific site selection(where) and construction methods(how). Through this approach, we can reassess the risk and determine whether the site is suitable for development purposes.

It should be noted that we have not provided detailed index explanation for certain indicators in our risk adjustment formulas. This is because they are not the focus of this chapter. Our aim is to explore a new analytical framework to guide real estate development decisions. This framework emphasizes taking construction measures for different types of extreme weather, aiming to enhance the stability and safety of buildings. We hope that this approach can provide new insights for real estate companies.

6 Model II: Historic Landmark Preservation Model

Insurance companies do not underwrite policies all areas due to risk/reward considerations. However, there are historic landmarks in uncovered areas that may be destroyed by extreme weather events. There- fore, we have developed the Historic Landmark Preservation (HLP) Model for communities, which are under the threat of severe extreme weather.

The model construction began with four dimensions: history, culture, economy, and commu-

nity. Secondary indicators were selected based on these dimensions, and analytic hierarchical pro- cess(AHP) was used to measure the comprehensive value of the landmark. The higher the comprehen- sive value, the more necessary the preservation, and the greater the required investment.

Finally, we selected a specific site to demonstrate the effectiveness of the model and provide rec- ommendations for preservation.

6.1 Indicator Selection

As shown in Figure 12, to comprehensively evaluate the value of landmarks, we selected four primary indicators: 微信公众号：数学模型 history, culture, economy, and community.

We considered the universality and objectivity of the indicators when selecting secondary indicators, as well as their measurability with data.

• Economic Value can be measured by two secondary indicators, Tourism Value (TV) and Exploitation Potential (EP). TV represents the existing economic value, which primarily derives from tourism. EP is equivalent to the undeveloped area divided by the to- tal area.

• Cultural Value can be measured by two secondary 微信号：MATHmodels indicators, Intangible Cultural Heritage (ICH) and

Local Culture Research (LCR). ICH is quantified secondary indicators by the number of intangible cultural heritage. LCR can be determined by searching for papers indexed with DOI using the landmark name and community name as keywords.

• Historical Value can be measured by two secondary indicators, Age and Importance in History (IH). Age refers to the number of years of history, while IH refers to the number of significant historical figures and events it is related to.

• Community Value can be measured by two secondary indicators, Regional Educational Ac- tivities (REA) and Community Spirit (CS). REA refers to the number of regional educational activities related to the landmark. CS represents the positive impact of a landmark on the com- munity as a whole. It is measured on a scale of 0 to 1 due to the difficulty in accurately assessing its impact.

After identifying the metrics, we used AHP to assign weights and determine the value of the land- marks.

6.2 Weight Calculation: Based on AHP

Weight Assessment Matrix

After determining the eight secondary indicators above and their measuring methods, we need to assign weights to them. We set landmark value as the target layer and build a hierarchical model with primary indicators and secondary indicators.

Firstly, we compare the indicators within the same level pairwise to obtain the weight assessment matrix. To make the judgment results more professional, we obtained their relative weights from aca- demic papers.[7] The Weighting Judgment Matrix (WJM) for indicators are shown below.

Intermediate Layer Economy Economy 1 Culture History Community 1/3 1/3 1 微信公众号：数学模型 Culture 3 History 3 Community 1

Economic Value TV EP

Tourism Value (TV) 1 2 Exploitation Potential (EP) 1/2 1

1 3 3 1/3 1 3 1/3 1/3 1

Cultural Value ICH LCR

Intangible Cultural Heritage (ICH) 1 5 Local Culture Research (LCR) 1/5 1

微信号：MATHmodels Historical Value Age IH

Age 1 1/3 Importance in History (IH) 3 1

Consistency Testing Community Value REA CS

Regional Educational Activity (REA) 1 1/3 Community Spirit (CS) 3 1

As the data used came from multiple papers, it is necessary to conduct consistency testing on the results. The following explains how to conduct a consistency test on an n × n matrix. Let xi,j represent the data in the i-th row and j-th column.

The product of each row is computed as:

n ∏ Mi = xi,j, j=1 (21) i, j = 1, 2, . . . , n

The normalized principal eigenvector ¯Wi is calculated by taking the n-th root of Mi:

¯Wi =

To normalize the vector ¯W:

¯Wi = n√ (22) Mi

¯Wi ∑n (23) j=1 ¯Wj The maximum eigenvalue of the matrix, λmax, is given by:

n ∑ λmax = i=1 ((λmax ¯Wi) ) (24) n ¯Wi

The consistency index (CI) is obtained as follows, and a lower CI indicates higher consistency:

CI = λmax −n (25) n −1 In our model, the primary indicators’ matrix’s CI is 0.052, corresponding to a mean random consis- tency index (RI) value of 0.882, and the random consistency ratio (CR) is 0.058, passing the consistency test. The 2 × 2 matrices, representing secondary indicators, all have a CI value of 0 and have passed the consistency test. Below is the weight table. 微信公众号：数学模型

Decision Layer Intermediate Layer Factor Layer Weight (%)

Tourism Value 8.135 Economy Exploitation Potential 4.067 Intangible Cultural Heritage 39.434 Culture Local Culture Research 7.887 Historic Landmark Value Historical Importance 21.206 History Age of Landmark 7.069 Regional Educational Activity 3.051 Community 微信号：MATHmodels Community Spirit 9.152

6.3 Value Calculation and Extent Estimation

HLV Calculation

Due to the different dimensions of indicators, we need to normalize them. All eight indicators involved in this article are positive indicators, and the normalization formula is as follows:

x −min(x) x′ = (26) max(x) −min(x) After normalization, all indicators’ values are within the [0, 1] range and dimensionless, allowing for calculations.

The formula for calculating the historical landmark value HLV is as follows:

∑ HLV = WaIa (27) a where:

• a represents the index of the specific indicator.

• I represents the normalized value of the indicator.

• W represents the weight of the indicator.

Estimation of Extent of Preservation Measures

Based on HLV, we can estimate the necessary extent of preservation. The level of preservation is scaled to match the significance of the landmark. Here we propose a three-tiered approach to categorize the protective measures:

• Level I: High Preservation (HLV ≥0.7) Entails advanced measures for preservation and prevention, including relocation for protection when necessary.

微信公众号：数学模型

• Level II: Moderate Preservation (0.3 ≤HLV < 0.7) Encompasses comprehensive protection against common hazards.

• Level III: Low Preservation (HLV < 0.3) Includes routine maintenance and disaster-specific precautions.

6.4 Application: Temple of Literature in Hanoi, Vietnam

Value Assessment and Conservation

According to our insurance model, Vietnam is expected to be significantly affected by extreme weather events in the future. However, due to high risks and low premiums, it is unlikely to be insured. So, we chose the Temple of Literature(Văn Miếu–Quốc TửGiám) in Hanoi, Vietnam as our subject.[8] 微信号：MATHmodels In 1070 AD, Emperor Lý Thánh Tông in Vietnam decided to establish the Temple of Literature to worship Confucius. In 1076 AD, Emperor Lý Nhân Tông built the Imperial Academy next to the Temple of Literature, which became the first formal academy in Vietnam. Today, the Temple of Literature still hosts annual religious ceremonies and cultural activities such as calligraphy and Chinese chess.

According to the model presented in section 6.3, we have assigned a HLV of 0.463 to the Temple of Literature, suggesting a medium level of preservation is advisable. Using the methods described in section 3.3, the site is predicted to face increasing risks of floods and cyclones in the future.

In light of this, we recommended the following conservation measures:

• Regularly clean and clear the riverbeds and drainage channels.

• Apply waterproofing treatment to the surface of the buildings.

• Plant trees in the vicinity.

• Strengthen the load-bearing structures.

Implementing these protection measures can effectively prevent damage caused by flooding, ero- sion, and structural collapse due to strong winds.

Estimated Conservation Effectiveness

We continued to use the indicators from the value estimation to measure the difference between with protection and without protection. However, the historical significance of a landmark will not change in a short period, predicting future local culture research is challenging, and the ”community” indicator is binary (0-1) and does not show significant changes. Therefore, we considered the other five indicators and replaced the ”age” index with “expected lifespan”. We set the current level to a standard value 1 for ease of comparing conservation effectiveness.

微信公众号：数学模型

The predicted conservation effectiveness is shown in Figure 13. 微信号：MATHmodels

• Without protection: Extreme weather will result in building damage, water logging on the premises, reduced visitors, and the inability to conduct development and educational activities. Due to the lack of insurance, these losses cannot be compensated.

• With protection: Damage caused by extreme weather is significantly reduced, and the time when the site cannot operate due to water logging is greatly reduced. Furthermore, with the improve- ment of preservation measures, the number of visitors and activities may increase. So we can say that our HLP model for estimating the extent of protection to historical landmark is reliable and effective.

7 Strength and Weakness

Strength

• For Model I(DBMI) ,we employed time series analysis to develop a reasonably accurate model for extreme weather forecasting. Additionally, we utilized expertise in insurance to calculate the insurance company’s demand and effectively balanced demand and risk for sustainability through optimization.

• For Model II(HLPM), we chose multi-dimensional analysis and applied the Analytic Hierarchy Process, and considered relevant literature to select indicators and weights, resulting in weighted outcomes that closely resemble the true value of historical landmarks. We then implemented corresponding protection measures and assessed their effectiveness based on real case.

Weakness

• For Model I(DBMI) , as we only have several thousand event records within 100 years, our model is less applicable for long-term risk predictions and risk predictions on smaller areas with finer regional divisions.

• For Model II(HLPM), it focuses on assessing the degree of preservation, but it is unable to pro- vide specific guidance on how to choose specific protective measures based on the degree of preservation.

微信公众号：数学模型

Letter of Recommendation

To whom it may concern,

We are a team of Insurance of Catastrophes Modelers(ICM). Extreme weather events have caused 微信公众号：数学模型 increasing losses in recent years. Accordingly, insurance companies are going to change how and where they underwrite. According to models, Vietnam faces high risk of extreme weather events in the future, especially floods and cyclones. Therefore, insurance companies are unlikely to underwrite policies for property losses caused by extreme weather events in your region.

However, some historical landmarks are vulnerable to extreme weather, such as the Temple of Litera- ture(Văn Miếu–Quốc TửGiám). We believe that protective measures can be implemented to safeguard it. A model has been established to assess its value in four dimensions: economy, history, culture, and community. We have prepared suggested measures, a timetable, and a budget for you based on this.

Project Time Budget Budget Explanation

微信号：MATHmodels Cleaning Rainy sea- 1.4 million Viet- In 2023, the average monthly wage for riverbeds and son namese Dong per Vietnamese is 700 Vietnamese Dong. It is drainage channels month estimated that three workers would work for two days each month Waterproofing January to 0.8 million Viet- To ensure better preservation, polymer treatment March namese Dong per material is recommended square meter Planting trees March and 0 Local student volunteers for tree planting April are encouraged for educational purposes Strengthening Rainy sea- Unknown It is challenging to estimate the cost as it aged structures son depends on the actual aging condition

With these measures, we can greatly reduce potential losses caused by extreme weather events. The effectiveness of preservation has been estimated and is shown in the chart on the right.

In the event of severe weather, take protective measures. We will continue to reduce the risks associated with our insur- ance products.

We sincerely hope that the Temple of Literature can serve as a treasure of human civilization and make a long-term contribution to the community.

Sincerely,
