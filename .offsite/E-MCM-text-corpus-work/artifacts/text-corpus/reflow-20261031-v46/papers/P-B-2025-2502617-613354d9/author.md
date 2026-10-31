Problem Chosen MCM/ICM

B

Summary Sheet

Summary

The rapid growth of tourism has led many countries and regions to recognize the tension between environmental preservation and the short-term economic benefits of traditional tourism models. The overload alarm of tourism industry prompts the question: How should tourism evolve in the future? Sustainable tourism has emerged as a crucial solution to this dilemma. This paper develops a multi-objective planning model that integrates economic, social, and environmental factors, tailored to the current state of the tourism industry in Juneau and its development goals.

In Sub-model I, economic benefit is the primary optimization objective. Considering the diminishing marginal returns and increasing marginal costs associated with a rising number of tourists, we developed a mathematical relationship between economic benefits and costs as a function of tourist volume. Through a cost-benefit analysis (CBA) model, we then defined the feasible domain of economic constraints and determined the maximum economic benefit.

In Sub-model II, social benefit is the second optimization objective. It is assessed through social satisfaction analysis and monetization. Social satisfaction is influenced by residents' living pressure and regional congestion. We use the potential benefit per unit of social satisfaction as the conversion factor and model social benefit changes with tourist numbers. A social welfare optimization model identifies the feasible domain and calculates the maximum social benefit.

● In Sub-model III, environmental benefit is the third optimization objective. Focusing on glacier degradation, the primary y environmental issue in Juneau. Given the link between glacier degradation and carbon emissions, the carbon footprint is chosen as the key environmental indicator. The monetization of this effect follows a similar method to that of social satisfaction. Through ecological carrying capacity analysis, we determine the feasible range for environmental benefits and calculate the maximum achievable value.

Furthermore, we integrate the three preceding models and account for the coupling relationships among them. Using the SLSQP method, we determine the global Pareto-optimal solution for tourist numbers and overall benefits. Specifically, when the number of tourists reaches 1.32 million, the economic measure of the municipal weighted total benefit is 10 million USD, while the net income for Juneau amounts to 576 million USD.

Finally, we analyze the sensitivity of key model parameters, as well as the sources of additional government revenue and spending programs. We also write a memo to the Tourist Council of Juneau and extend the model to Jiuzhaigou, China. The results show that our model has good usability and robustness.

Optimization, SLSQP

Introduction

3 1 3 1.1 Problem Background . 1.2 4 Restatement of the Problem 1.3 4 Literature Review . 1.4 5 Our Work .

Assumptions and Justifications

5 2

Notations

3 6

Multi-Objective Optimization Model

7 4

Sub-model I: Cost-benefit Analysis Considering Marginal Effects

7 4.1 4.1.1 Analysis of Economic benefits 8 4.1.2 Analysis of Economic Costs 8 4.1.3 Overall Economic Performance 9 4.2

Sub-model II: Social Welfare Optimization Model

10 Estimation of Social Satisfaction Indicator 4.2.1 10 4.2.2 Monetized Conversion of Social Satisfaction 10 4.2.3 Overall Social Performance 11

Sub-model III: Environmental Carrying Capacity Model

4.3 11 4.3.1 Carbon Footprint Accounting 12 4.3.2 Monetization of Carbon Footprint 13 4.3.3 13 Overall Environmental Performance 4.4 14 Pareto Optimal Solution for Total benefit 4.4.1 14 Determination of Weight Value 4.4.2 Global Pareto Optimization in the Game between Scenic Spots 15 1 15

Results and Extension

5 Optimization Objectives 15 5.1 Constraints Analysis 15 5.2

Optimization Result Analysis

16 5.3 Key Parameter Determination 5.4 18 19 Additional Income and Expenditure Plan 6

Sensitivity Analysis

20 7 Effect of Changes in Total Tourists and Performance per Tourist 20 7.1 7.2 Effect of Changes in Total benefit 20 21

Strengths and Weaknesses

8

Strengths

1 21 8.1 8.2

Weaknesses

21 21

Conclusion

9

1 Introduction

微信公众号：数学模型

1.1 Problem Background

In recent years, tourism has played an increasingly significant role in driving local economic growth, generating substantial revenue and gradually becoming a pillar industry for both local and global economies[1]. However, with the continuous rise in tourist numbers, issues such as environmental degradation, increased infrastructure costs, and declining resident satisfaction have emerged, posing serious threats to the sustainable development of local tourism. This phenomenon is particularly evident in Juneau, Alaska.

Juneau is renowned for its unique and breathtaking natural landscapes, which include expansive 微信号：MATHmodels national parks, majestic glaciers, and a 6,640-mile coastline. These attractions draw hundreds of thousands to over a million tourists annually, with the majority arriving via luxury cruise ships. In 2023, the tourism sector brought 1.6 million cruise passengers to Juneau, generating $375 million in economic revenue[2] , alongside nearly 4,000 cruise-related jobs and $18 million in tax revenue[3]. However, the influx of tourists has resulted in traffic congestion, overcrowded tourist sites, and rising hidden costs, such as increased infrastructure costs and the need for environmental remediation. Additionally, the noise from passenger helicopters has significantly disrupted the daily lives of local residents. More concerning is the impact of the surge in tourist numbers on the environment, including rising temperatures that have led to the retreat of the iconic Mendenhall Glacier. The pristine air, clean water, and natural beauty that once defined Juneau’s allure are now being threatened by the ongoing influx of tourists.

To mitigate the negative impacts of unsustainable tourism growth, the Juneau government has implemented measures such as raising taxes and limiting visitor numbers to regulate tourist flow. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Additionally, it has intensified efforts to promote alternative attractions, such as wildlife viewing, in areas beyond the Mendenhall Glacier. Moving forward, the Juneau government should consider adopting more effective strategies to balance the social and economic benefits of tourism while developing comprehensive management plans. These plans should aim to advance the tourism sector while protecting the natural environment as much as possible, ensuring the long-term sustainability of tourism. This challenge not only affects the long-term sustainability of Juneau’s tourism industry but also represents a common issue faced by tourist cities worldwide.

1.2 Restatement of the Problem

Based on the current situation in Juneau and the information outlined in the problem statement, it is essential to develop a comprehensive sustainable tourism management plan to maximize economic, social, and environmental benefits. Specifically, the plan must address the following three issues:

Problem 1: Develop a sustainable tourism management model tailored to the specific context of Juneau, considering all factors that may infvluence the long-term sustainable tourism industry. These factors include: environmental carrying capacity, both visible and hidden management costs, and local resident satisfaction.

Problem 2: Extend the model to other cities negatively affected by tourism and demonstrate its applicability in these cities. Analyze the impact of urban differences on the selection of key man- agement measures, promote attractions with fewer tourists, and promote sustainable development of local tourism industry.

Problem 3: Based on the model developed in Problem 1, submit a one page memo to the Juneau Tourism Commission, using actual data to illustrate the necessity of developing sustainable tourism and providing feasible tourism management optimization paths and measures for Juneau.

1.3 Literature Review

The development of tourism has contributed to the growth, but at the same time it has also had some impact on the natural environment[4]. Sustainable tourism has become an important topic of academic research[5]. The main indicators of the relevant discussions focus on the environmental, economic and social aspects[6]. In the existing studies, some scholars analyze the environmental benefits of tourism development[7], while Saayam[8] believe that sustainable tourism contributes to long-term social-economic stability, and Whitford et al.[9] discuss the role of sustainable tourism in product development for local residents. In addition, in the analysis of social benefits, scholars have analyzed the role of sustainable tourism in improving the quality of life of the residents[10], and improving the happiness of the residents’ life[11].

In addition, some scholars try the integrated management model of sustainable tourism. Stoica et al.[12] use the methods of benchmarking and SWOT analysis to construct a tourism manage- ment decision model, and Sripateep et al.[13] comprehensively consider the maximization of the interests of tourism stakeholders on the basis of the multi-objective planning model. However, the models that introduce Pareto optimization method into sustainable tourism management model and comprehensively consider the economic, social and environmental tripartite benefits are still few, and more scholars use Pareto optimization method to analyze the maximization of the interests of

关注数学模型 some classes of stakeholders. For example, Ko,YD [14]derived the economic-environmental effect of sustainable tourism development in Seoul through Pareto optimization model, and Wang,XP et al.[15]analyzed the effect of tourism intermediate product price on the Pareto effectiveness of supply chain.In this analysis, we introduce the Pareto optimization method into the multi-objective model, which is innovative and reasonable.

1.4 Our Work

微信公众号：数学模型 微信号：MATHmodels

2 Assumptions and Justifications

Assumption1: Demandandexpenditureexhibitincreasingmarginalutility, whilerevenue(including hidden costs) follows decreasing marginal returns.

Justification: This aligns with classical economic models characterizing resource-constrained

benefit-cost curves. Demand and expenditure can be modeled as strictly convex functions with tunable parameters, whereas revenue is fitted via concave functions to reflect diminishing returns.

Assumption 2: Hidden costs (e.g., infrastructure strain, carbon footprint) are monetize in USD.

Justification: This provides dimensional consistency for quantitative analysis. Environmental economics employs shadow pricing for such conversions—for instance, carbon trading market rates or public facility maintenance costs can quantify ecological impacts. Empirical carbon pricing frameworks (e.g., Carbon Border Adjustment Mechanism) validate this assumption’s practicality.

Assumption 3: Tourist spending or policy changes instantaneously affect visitor numbers.

Justification: This assumes a full-information market, simplifying tourism’s inherent time-lag dynamics. While idealistic, it enables static Pareto-optimal equilibrium modeling. Deviations from reality are addressable via elasticity coefficients (e.g., price elasticity of demand)

Assumption 4: Parameters are spatiotemporally localized, ignoring external competition, in- frastructure decay, or seasonal fluctuations.

Justification: Focusing on Juneau’s internal resource allocation efficiency, this supports short- term partial equilibrium analysis. Such simplification suits rapid policy pilot evaluations while acknowledging scope limitations.

3 Notations

Symbols Description Unit

Number of Tourists Millions Nt Number of Residents in Juneau Millions Nr Indexes of Decay Elasticity - ki(i = 0, 1, 2)

Economic Notations

Economic benefits USD E Consumption Generated by Tourists USD Ct Economic Revenues of Government USD CGi Economic Cost of Government USD CGc Economic Revenues of Residents USD CRi Infrastructure Costs USD Ci Fixed Expenditure Costs USD Cfix Basic Consumption per Tourist USD A0 Tax Rate % t

Social Notations

Social benefits USD S Virtual Economic Value Equivalent USD Cadd Generated by Unit of Social Satisfaction Incremental Cost of Residents’ Living USD CRc Hidden benefits from Social Satisfaction USD A1 Social Satisfaction - s Pressure on the Lives of Local Residents - Pl Congestion Pressure due to Increased Tourist Flow - Pf

Environmental Notations

Environmental benefits USD Env Government Expenditure on Environmental Governance USD Cenv Hidden Costs Arising Caused by Carbon Emissions USD CCO2 Virtual Costs Corresponding to a Unit of CO2 Emissions USD CperC Total CO2 Emissions ton ECO2 Average Carbon Emissions by Each Tourist ton γ Proportion of Tax to Improve the Environment - A2

关注数学模型 Symbols V alue Notes Symbols V alue Notes

from Statistic[16] 0.032 from Government 0.081 Nr γ 5 from Government 3000 from Government t A0 Estimate from Article[17] 0.0068 Estimate 5 k0 A1 0.3574 Estimate 0.03 from Government k1 A2 1.6000 Estimate k2

微信公众号：数学模型 微信号：MATHmodels

The symbols in Table 1 not mentioned in Table 2 and Figure 3 are all intermediate or decision variations used in model calculation.

4 Multi-Objective Optimization Model

4.1 Sub-model I: Cost-benefit Analysis Considering Marginal Effects

Economic benefits is the first core objective of local tourism development. An increase in the number of tourists not only promotes local economic growth and increases municipal revenues, but also provides more employment opportunities for local residents, thus raising their incomes. In addition, economic efficiency is a key factor in sustainable tourism management strategies. When the economic benefits are too low or the costs do not match the benefits, the local government may seek new economic growth points or even give up the continued development of tourism. Therefore, maximizing economic benefits should be the first objective function in the planning model.

Maximization of economic benefits can be expressed as follows:

(1) max E = CGi −CGc where CGi represents the visible economic revenues of the local government from the growth in the number of tourists, and CGc is the increase of the local government in the cost of infrastructure operation and maintenance and other public services due to the excessive number of tourists. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

4.1.1 Analysis of Economic benefits

The direct consumption generated by tourists is most significantly influenced by the number of tourists, so it can be regarded as a linear function of the number of tourists (i.e., assuming that the expected spending per tourist remains constant over the course of a year). Therefore, the formula for calculating the direct consumption Ct generated by tourists is given by

(2) m m m m m m m m m m m m m m m m m m m m m m Ct = α × Nt m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m where α represents the average economic benefits per tourist, Nt represents the number of tourists, m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m and as the number of tourists increases, the benefits arising from consumption generated by tourists m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m exhibits diminishing marginal returns, meaning that α1 will decrease as Nt increases. The formula m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m for calculating α is as follows:

A0 (3) α = (1 + ek0A0Nt(t−tbasic))(1 + ek0(A0−A0max))

where A0 represents the basic per capita consumption, k0 represents the rate at which per capita consumption tends to saturate as the number of tourists increases, and t represents tax rate. The formula also reflects the tolerance of tourists to the increase of tax and average cost, and the attenuation will be further increased when the tax or average cost is greater than the threshold. By default, we consider t = tbasic, A0max = 1.5A0 A portion of the consumption generated by tourists during their trip is used to pay fees such as VAT on goods and hotel taxes levied by municipalities, while the other portion is used to purchase tourism-related goods and services provided by local residents. Therefore, we can get the following formula:

(4) Ct = CGi + CRi where CGi represents the portion of tourist spending that goes to municipal revenues, and CRi represents the revenues of tourist spending that accrue to residents engaged in the tourism industry. Government benefits and residents’ benefits can be expressed as follows:

( CGi = αNtt (5) CRi = αNt(1 −t)

4.1.2 Analysis of Economic Costs

The components of economic costs are more complex than economic revenues. On the one hand, the government of Juneau needs to invest a certain amount of fixed expenditures on public services every year, such as household garbage removal and sewage disposal, etc. On the other hand, the surge in the number of tourists has led to accelerated destruction of the infrastructure in Juneau, and the government has to invest more revenues in the construction and maintenance of the infrastructure. At the same time, the cruise ship traffic brings a large amount of carbon emissions, the government of Juneau needs to solve these challenges.

It is important to note that the economic costs are not strictly linear with the number of tourists. When the number of tourists is high, the rate of infrastructure damage may be faster, showing an

关注数学模型 increasing trend of marginal costs at the level of government management costs. Therefore, in the economic cost analysis we fully consider the actual situation of increasing marginal cost and 微信公众号：数学模型 construct an economic cost analysis model.

(6) CGc = CiN 2 t + Cfix where Ci represents the cost required for the operation and management of the infrastructure and Cfix is the fixed cost to be incurred by the government.

The additional tax revenues of the Government and a portion of municipal revenues are invested in public services, and a higher level of public services improves the satisfaction of local residents and tourists, thus contributing to the development of sustainable tourism.

微信号：MATHmodels

4.1.3 Overall Economic Performance

As mentioned earlier, total economic efficiency E can be summarized as a composite variable reflecting the overall returns to economic activity. Considering the two key economic principles of diminishing marginal benefits and increasing marginal costs, it can be hypothesized that the government should have two break-even points. The break-even point is the point at which economic benefits equal economic costs, i.e. CGi = CGc, at which the government has neither a profit nor a loss.

The break-even point provides upper and lower thresholds for the number of tourists. As the number of tourists increases, the marginal benefit gradually decreases while the marginal cost gradually increases, resulting in the economic benefit turning negative after the breakeven point is exceeded.

When the number of tourists exceeds this threshold, the marginal benefits from additional tourists are not sufficient to cover the increased costs, which in turn leads to a decline in economic benefits. The break-even point therefore provides the government with a range of acceptable tourist numbers beyond which measures need to be taken to avoid negative economic benefits.

4.2 Sub-model II: Social Welfare Optimization Model

The social benefits is the second key objective that we analyze in our models. When the number of tourists is too high, local residents feel more pressure to live due to the increase in the cost of living, and at the same time, when the number of tourists far exceeds the number of local residents, the regional congestion rises and the social satisfaction of the residents decreases. On the contrary, when the number of tourists is too low, residents mainly engaged in the tourism service industry may feel an increase in life pressure due to a decrease in income.

Combining life stress and crowding, we can obtain the formula for the indicator measure of social satisfaction. Further, combining the historical data of Juneau, we analyze the virtual economic value equivalent that can be generated by a unit of social satisfaction, and calculate the economic benefits of social satisfaction metrics based on this. Ultimately, we can get the result of maximizing social benefits as follows (7) max S = s × Cadd where s represents overall social satisfaction and Cadd represents the hidden economic value equivalent that can be generated by a unit of life satisfaction.

4.2.1 Estimation of Social Satisfaction Indicator

In our model, residents’ social satisfaction is mainly determined by two mutually constraining factors: pressure on living and pressure on congestion. An increase in the number of tourists will both increase residents’ income and lead to an increase in residents’ cost of living. When the increase in residents’ cost of living exceeds the increment in income, residents’ life satisfaction will decrease. Since Juneau has fewer residents, it can be assumed that there is a significant linear relationship between congestion pressure and the number of tourists.

Pl = CRi    CRc  (8) Pf = Nr    Nt

where CRc represents the incremental cost of living to residents due to an increase in the number of tourists, which is considered as a constant since CRi reflects a decrease; and Nr is the number of residents in Juneau. Thus, the dimensionless indicator of social satisfaction s can be denoted as

(9) s = Pl × Pf

4.2.2 Monetized Conversion of Social Satisfaction

We use the virtual economic benefits generated by unit social satisfaction as an equivalent quantitative indicator to comprehensively analyze social satisfaction. Through the monetization transformation of social satisfaction, the quantitative outline of the sub-model can be further ensured to be unified, thus ensuring the model has better usability and comparability.

Specifically, the monetized conversion of social satisfaction indicators includes two steps. (1) the hidden economic benefit equivalent generated by the unit of social satisfaction; (2) the total

关注数学模型 hidden economic benefit generated by social satisfaction.

A1 (10) Cadd = 1 + e(Nt−k1Nr)t where A1 represents the hidden benefits derived from social satisfaction as equivalent quantitative metrics, which diminish when the number of tourists reaches a certain ratio k1 of the local population 微信公众号：数学模型 or when tax revenue increases.

4.2.3 Overall Social Performance

In Model II, we combine the stress of living in Juneau with the stress of overcrowding due to the growth in the number of tourists and obtain the social benefit equivalent by measuring satisfaction through a virtual economic value. Since satisfaction is judged differently by different groups, subject to the 2023 Statistic of Juneau[3], it can be assumed that the social benefits are in an acceptable range when more than 60%, of residents achieve a state of satisfaction.

微信号：MATHmodels

In 2023, Juneau reaches 1.67 million visitors and the reality of residents being dissatisfied with the excessive number of visitors arises. In this context, we take the social satisfaction in 2023 as the baseline social satisfaction and calculate the off between the number of tourists and social satisfaction. That is, when the social satisfaction satisfies S > 0.6 × S2023, the social benefit satisfies the constraint.

4.3 Sub-model III: Environmental Carrying Capacity Model

Minimizing environmental benefits is the third important objective in addition to maximizing economic and social benefits. Excessive numbers of tourists at any given time may result in the destruction of local natural and cultural resources due to insufficient carrying capacity. In addition, the airplanes, cruise ships, and other means of transportation used by tourists to travel to destinations such as Juneau can also lead to increased emissions of greenhouse gases such as carbon dioxide, which in turn leads to higher temperatures and glacier melting.

Environmental damage has significant hidden economic costs for the tourism industry and increases potential government expenditures. In order to quantitatively assess the hidden economic costs of environmental damage, in the environmental benefit analysis, we accounted for the carbon footprint of attractions in the city of Juneau and conducted an economization analysis using the equivalent of economic growth per unit of carbon emissions. Specifically, the primary objectives and key analyses of economic benefits are shown below

(11) min Env = CCO2 −Cenv where, Cenv represents government expenditure on environmental governance, while Cco2 repre- sents the hidden costs arising from environmental degradation caused by carbon emissions. The difference between these two variables quantifies the magnitude of tourism’s environmental impact.

4.3.1 Carbon Footprint Accounting

Since the primary cause of glacier melt is temperature increase, the glacier recession equation summarized for assessing the recession of Mendenhall Glacier in Juneau is as follows m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m ! ∆V 1 + ∆ECO2 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m (12) m m m m m m m m m m m m m m m m m m = λ ln m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m V0 C0 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m where ECO2 represents the total carbon emissions from each scenic area in Juneau City, C0 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m represents the air carbon dioxide concentration in Juneau City in 2023, and λ represents the climate m m m m m m m m m m m m m m m m m m m m m m m m m

sensitivity, which is usually taken as 0.8◦C/(W/m2).

It can be seen from the above equation that the retreat of Mendenhall glacier is mainly related to carbon emission. In addition, in order to prevent over-parameterization, this formula is only used to predict the melting rate of glacier, and it is not added to the environmental benefit evaluation model, but replaced by carbon emission.

In the process of carbon footprint accounting, we take into account that changes in the number of visitors to different attractions may lead to different carbon emissions, and analyze the carbon emissions of different attractions separately, so as to measure the impact of the growth in the number of visitors on the environment. According to the McKinsey Marginal Emission Reduction Curve[18], the carbon emissions from visitors to each attraction can be derived as follows

(13) Eci = γ × (riNt)2 where γ represents the average carbon emissions generated by each tourist, and ri represents the proportion of tourists visiting the i-th attraction out of the total number of tourists. According to the statistics[3], we think the value of r is {0.2, 0.2, 0.6}, among these, 0.6 is the proportion of tourists going to the glacier.

From this, the total carbon emissions from the sites in Juneau can be expressed as

(14) X Eco2 = Eci i where Eci represents the carbon emissions from managing the i-th tourist attraction, and the equation calculates the total decentralized carbon emissions Eco2 by taking the sum of the individual emission costs.

关注数学模型

4.3.2 Monetization of Carbon Footprint

Municipal revenues increase when the number of tourists increases. However, environmental 微信公众号：数学模型 benefits decrease as CO2 emissions increase. To ensure the sustainability of tourism development at the attraction, the hidden environmental management costs of the municipality rise.

In the carbon footprint economic analysis model, for Cenv, we use tax to reflect the government’s additional revenue; for CCO2, firstly estimate the virtual cost equivalent per unit of carbon emissions, and then calculate the potential economic loss due to environmental pollution. Specifically, the model we use is shown below  A2t Cenv = Nt ·   (15) 1 + ek2t CCO2 = CperCECO2   where CperC represents the virtual economic cost corresponding to a unit of CO2 emissions, A2 微信号：MATHmodels represents the proportion of tax revenues used to improve the environment, and k2 represents the elasticity adjustment coefficient, which indicates that as tax revenues increase, their effect in environmental management tends to be saturated.

4.3.3 Overall Environmental Performance

The presented environmental impact model integrates two critical nonlinear dynamics to quan- tify tourism sustainability. The formulation exhibits a dual structure balancing government-led environmental investments against dispersed carbon emission costs. The environmental gover- nance component Cenv reflects diminishing returns on tax-funded ecological improvements as expenditures increase —— a mechanism preventing over-reliance on financial solutions.

Conversely, the carbon cost aggregation CCO2 inherently penalizes concentrated tourism pat- terns through its quadratic summation structure. This mathematical design creates an optimization landscape where effective environmental management requires both strategic fiscal allocation and tourist flow distribution.

The model’s nonlinear interactions emphasize that simply increasing environmental spending becomes progressively less effective, while carbon costs grow disproportionately with visitor con- centration, demanding balanced spatial-temporal management of tourism resources for sustainable outcomes.

4.4 Pareto Optimal Solution for Total benefit

From the analysis in the preceding three sections, expressions for economic, social, and en- vironmental benefits can be derived respectively. The total benefit is formulated as a weighted average of these three dimensions, yielding the following optimization objective:

max E = CGi −CGc    max S = s × Cadd   (16) min Env = Cco2 −Cenv    max T = ω1E + ω2S −ω3Env 

where ωi(i = 1, 2, 3) is the weight of three benefits.

Additionally, the constraints are formulated as follows:

 E > 0    S > Smin     (17) Env < 0 st.

T > 0      Ntmax > Nt > 0   where Ntmax denotes the maximum tourist capacity, which can be set to the 2023 tourist volume(i.e., 1.67 million); where Smin denotes the minimum social benefit that Juneau can sustain, based on the social benefit in 2023 and calculated using the parameters from 2023 according to the aforementioned formula.

4.4.1 Determination of Weight Value

The weights for economic, social, and environmental benefits are derived from state-level reference metrics: U.S. state GDP rankings[19], cost-of-living rankings by the Missouri Economic Research and Information Center (MERIC)[20], and Yale University’s state-level Environmental Performance Index (EPI) rankings[21]. This methodology assumes that a lower ranking (denoted as rki, which i means the i-th dimension) in a specific dimension indicates a greater demand for improvement in that dimension, thus justifying a higher assigned weight. For instance, the Alaska’s multidimensional rankings are expressed as rk = {47/50, 46/50, 43/50}.

It is crucial to emphasize that the relative interdimensional relationships are contingent upon state-specific contextual factors. This dependency thus necessitates the following weight method formulation:

rki (18) ωi = P rki where, the weights for the three dimensions (economic, social, and environmental) in the Alaska are calculated as ω = {0.346, 0.338, 0.316}, which can be approximated as those of Juneau, given its role as the state’s central hub for cruise tourism and primary data collection point.

关注数学模型

4.4.2 Global Pareto Optimization in the Game between Scenic Spots

Economic, social and environmental benefits usually form a competitive relationship. This competition is typically influenced by multiple factors (e.g., the number of tourists and tax rates), and in the absence of coordinated mechanisms, natural game-theoretic interactions often lead to outcomes that deviate from Pareto Optimization, with strategic autonomy tending to converge toward suboptimal equilibria.

Specifically, by solving the Multi-Objective Programming Model using the SLSQP method, under the above constraints, we can obtain a Pareto optimal solution where the benefits are most reasonably allocated, and there is no room for improvement in the total benefit, which is the results 微信公众号：数学模型 of the Multi-Objective Programming Model.

Economic vs Social Trade-off Economic vs Environmental Trade-off Social vs Environmental Trade-off 5000 0 0 Environmental Benefit (Carbon Units) Environmental Benefit (Carbon Units) 1750 1000 4000 4000 Social Benefit (Index Score) 2000 2000 1500 2000 Environmental Benefit 3000 Economic Benefit 1250 3000 3000 Social Benefit 4000 4000 4000 1000 5000 2000 2000 750 6000 6000 6000 500 1000 7000 1000 250 8000 8000 8000 0 微信号：MATHmodels 0 250 500 750 1000 1250 1500 1750 2000 0 250 500 750 1000 1250 1500 1750 2000 0 1000 2000 3000 4000 5000 Economic Benefit (Million USD) Economic Benefit (Million USD) Social Benefit (Index Score)

5 Results and Extension

5.1 Optimization Objectives

In the model, we try to analyze and optimize the total maximization of benefits by finding the optimal number of tourists, in which the economic, social and environmental benefits are all within the acceptable domain are the main constraints in the optimization process.

5.2 Constraints Analysis

• Juneau 1.Economic Constraints Analysis: Taking into account the diminishing marginal benefit and increasing marginal cost effects brought about by the growth in the number of tourists, the acceptable number of tourists under economic constraints can be derived. When the economic benefit is greater than 0, the economic benefit is acceptable. The economic constraint fully takes into account the effects of tourist spending, tax rates and other factors, and is able to reflect the additional revenue generated by tourism development.

2.Social Constraints Analysis: When the number of tourists increases, the income of the residents will increase, but the cost of living necessities, such as rent, food and beverage, will likewise rise. At the same time, when the number of tourists is too high, residents may be dissatisfied with the reduced convenience of social services due to crowding. The acceptable number of tourists under social constraints can be derived. Based on empirical data, the social benefits are acceptable when more than 60% of the residents are satisfied with the standard.

3.Environmental Constraints Analysis: Since the maximum carrying capacity of the envi- ronment is limited, when the number of tourists is too high or the distribution of tourists is too centralized, the possibility of environmental damage increases, which leads to adverse effects. In addition, tourists traveling by cruise ships, airplanes and other means of transportation will produce a certain carbon footprint. Accordingly, the acceptable number of tourists under environmental constraints can be derived.

• Jiuzhaigou As a tourist city that also uses natural resources as its main attraction, Jiuzhaigou’s constraints m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m to sustainable tourism development are roughly the same as those of Juneau. However, unlike the m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m better economic benefit of Juneau, Jiuzhaigou is much more influenced by economic benefit in its m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m development and less influenced by environment benefit due to the temperate, therefore need give m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m more consideration to economic constraints and more consideration to environment constraints.the m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m initial weighting parameters were adjusted to w = {0.625, 0.313, 0.062}. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

5.3 Optimization Result Analysis

• Juneau 1.Optimal Number of Tourists: We traverse the number of tourists in the range of 0-10 million, and through the coupled analysis of social, economic, and environmental benefits, we conclude that the total benefits is maximized when the total number of tourists is 1.32 million.

2.Global Pareto Optimization: The maximum total benefits T is about 8 million when considering only the changes in the decision variables, at which point the net income (Ct −Cgc) is 576 million dollars and the total performance (E + S −Env, means the direct sum of each benefit, representing the total benefit, used to measure the overall benefit; while weighted T used for optimization) is about 15 million. The optimal solution where the benefit first increases and then decreases with the number of tourists is shown in Figure 9, which is obviously in line with reality.

关注数学模型 微信公众号：数学模型 10 0 Economic Benefit Social Benefit 7 Positive Benefit Area Positive Benefit Area Negative Impact Area Negative Impact Area 25 0 6 50 5 Environmental Benefit Economic Benefit 10 Social Benefit 4 75 20 3 100 2 30 125 1 Environmental Benefit 150 Negative Benefit Area 40 0 Positive Impact Area 0 2 4 6 8 10 0 2 4 6 8 10 0 2 4 6 8 10 Nt Nt Nt 1.0 0.3 20 Benefit Increase Velocity Net Income Increase Velocity Performance Increase Velocity 0 0 500 0.8 10 15 0.2 0 0.6 50 20 10 500 30 0.4 0.1 100 40 1000 5 0.2 微信号：MATHmodels 50 0.0 1500 0.0 150 0 60 2000 0.2 0.1 70 Total Performance Total Benefit Net Income 5 200 2500 0 2 4 6 8 10 0 2 4 6 8 10 0 2 4 6 8 10 Nt Nt Nt

• Jiuzhaigou In the process of optimization for Jiuzhaigou, the selection of key parameters is basically the same as that of Juneau, but some parameters have been adjusted according to national conditions and environmental changes. According to China’s value-added tax rate, t=13% of Jiuzhaigou; while the other two key parameters are considered to be approximately the same as Juneau’s.

50 0 Social Benefit 50 Positive Benefit Area 0 Negative Impact Area 100 40 50 Environmental Benefit 200 100 Economic Benefit 30 Social Benefit 150 300 20 200 400 250 10 500 Economic Benefit Environmental Benefit 300 Positive Benefit Area Negative Benefit Area 0 Negative Impact Area Positive Impact Area 350 600 0 5 10 15 20 25 30 0 5 10 15 20 25 30 0 5 10 15 20 25 30 Nt Nt Nt 15 Benefit Increase Velocity Net Income Increase Velocity Performance Increase Velocity 1.0 1.5 0 0 0 10 0.8 1.0 200 0.6 2000 5 50 0.5 0.4 0 400 100 4000 0.0 0.2 5 150 0.0 600 0.5 6000 10 0.2 200 1.0 800 8000 15 0.4 Total Performance Total Benefit Net Income 1.5 250 0 5 10 15 20 25 30 0 5 10 15 20 25 30 0 5 10 15 20 25 30 Nt Nt Nt

1.Optimal Number of Tourists: We traverse the number of tourists in the range of 0-10 million, and through the coupled analysis of social, economic, and environmental benefits, we conclude that the total benefits are maximized when the total number of tourists is 3.32 million.

2.Global Pareto Optimization: The maximum total benefits T (total benefits of the municipal sector) is 37 million when considering only the changes in the decision variables, at which point m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m the net economic is 743 million dollars.

From the Figure 9 and Figure 10, it can be observed that the overall trend of benefits changes is approximately similar, which reflects the good scalability of the model. However, due to the extremely small weight of environmental benefits in Jiuzhaigou, its value is much lower than that of Juneau. This also reflects Jiuzhaigou’s selective neglect of environmental benefits in its pursuit of economic gains, reflecting the differences between different cities.

5.4 Key Parameter Determination

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

• Juneau m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 1.Proportion of Tourist(rglacier):The degree of dispersion of tourists reflects the ratio of the m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m actual number of tourists accommodated in different scenic spots, Juneau Tourism Bureau website m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m statistics show that more than 60% of tourists to Juneau City will go to Mendenhall Glacier. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

2.Tax Rate(t): Based on the data of various local tax rates published on the official website of the Juneau City Government, combined with the data of the total income generated by the tourism industry in Juneau and the municipal economic income, the comprehensive tax rate for tourists during their travel in Juneau is calculated to be 5%.

3.Visitor Consumption(A0):Visitor Consumption reflects the cost of food, lodging, excursions, and souvenir purchases incurred by tourists during their visit to the City of Juneau. In short, tourist consumption reflects to some extent the prices of scenic spots and local life.

Related images of changes in visitor numbers and total benefits when each key factor changes are in the section Sensitivity Analysis.

• Jiuzhaigou

(Performance per Tourist is short for Performance)

From Figure 11, the following observations can be made: (1) When the proportion of tourists visiting Jiuzhaigou valley (r) is approximately equal to the proportion visiting other attractions, the optimal total benefit corresponds to the maximum tourist volume and maximum performance. This indicates that maintaining diversion measures is beneficial for sustainable tourism. (2) As tax rates (t) increase, the additional expenditure for tourists also rises, leading to a reduction in the number of tourists required to achieve optimal performance. Meanwhile, performance itself increases. (3) The effect of increased tourist expenditure is similar to that of increasing t; however, due to diminishing marginal benefits, the graph exhibits an inflection point.

关注数学模型 The total benefit of the first two graphs in Figure 12 is proportional to the tourist volume(Nt), while the third graph is similar to the shape of performance. It can be concluded that the influence of performance increases while the Nt decreases with the increase in Tourist Consumption(A0). This is in line with objective reality; At the same time, it can be seen that T generated by the optimal Nt is slightly different when different key parameters change, which provides convenience for the manager's top placement policy. S

Additional Income and Expenditure Plan 6

• Sources of Additional Revenue:

Additional revenue is the revenue generated when the number of visitors changes. The main sources of additional revenue mainly include:

1. Direct economic income from consumption behavior occurring among tourists. Direct

economic income is reflected in municipal economic benefits through two channels of tax. One is the rate of VAT and hotel tax paid by tourists when they spend; rather, it is the rise in the amount of personal income tax brought about by the increase in residents' income.

2. Hidden sociol benefits generated when the number of tourists decreases. Hidden social

benefits is reflected through the monetized equivalent of social satisfaction, and Hidden social benefits will bring the government some economic gains in the long run.

• Revenue Expenditure Plan:

In order to achieve sustainable development of the tourism industry, the government needs to for- mulate a reasonable additional revenue expenditure plan. Specifically, the elements of expenditure that the government can adjust include the following:

1.Infrastructure management and operation expenditure. Infrastructure, including public build- ing construction and maintenance costs, urban pipeline maintenance fees, etc. A reasonable increase in infrastructure management and maintenance expenditures within a certain range can effectively improve social satisfaction and bring higher social benefits.

2.Environmental maintenance expenditure. Before environmental damage occurs, the gov- ernment needs to set aside and spend on environmental maintenance in advance. The increase of environmental maintenance expenses can improve the carrying capacity of the environment, promote the sustainable development of tourism, and then improve the total benefits.

3.Expenditures on the management of environmental damage. This expenditure is a potential economic expenditure. The government must take this item into account in its revenue and expenditure plan, carefully assess the probability of environmental damage, and prevent the chain reaction caused by reduced environmental benefits.

7 Sensitivity Analysis

7.1 Effect of Changes in Total Tourists and Performance per Tourist

In the model sensitivity analysis, we mainly analyzed the effects of small perturbations in the proportion of tourists, tax rate and tourist consumption, on the total number of tourists and total benefits. The results of the sensitivity analysis are shown in Figures 13 and 14.

The conclusions that can be drawn from the two graphs on the left are that (1) the greatest number of tourists visit the glacier when the proportion of tourists visiting the glacier is roughly equal to the proportion of tourists visiting the other attractions (2) the number of tourists required for optimal performance decreases further as the tax rate increases. These are roughly the same conclusions reached in the Jiuzhaigou analysis.

Compared to Jiuzhaigou, there is a big difference in Juno’s performance when the number of tourists changes. When tourist spending is below US$4,000, consumers view tourism expenses as a price inelastic product, so the number of tourists continues to increase, while the performance gen- erated per tourist shows a slow increase because the rate of diminishing marginal effects is smaller than the rate of rising tourist numbers. Subsequently, when spending per tourist exceeds $4,000, the sensitivity of tourists to price changes increases, and tourism expenditures are transformed into a price-elastic good, with the number of tourists decreasing sharply, the total benefits of the tourist attractions, and the performance generated per tourist decreasing in the same trend.

7.2 Effect of Changes in Total benefit

关注数学模型 In the sensitivity analysis of total benefits, the tax rate, tourist proportion, and tourist consump- 微信公众号：数学模型 tion were analyzed as key parameters. The results are as follows: (1) As the tourist proportion increases by 1% from 0, social, environmental, economic, and total benefits all increase due to a more balanced distribution of tourists. (2) As the tax rate increases by 1% from 5%, environmen- tal benefits rise, while economic, social, and total benefits decline. (3) As tourist consumption increases by 1.25% from 3,000 USD, economic and social benefits rise, environmental benefits decrease, and total benefits first increase and then decrease.

8 Strengths and Weaknesses

8.1 Strengths

微信号：MATHmodels

1. Computational Feasibility:

The model employs Pareto-optimal solutions with nonlinear marginal effect formulations, ensuring theoretical rigor while balancing realism and numerical stability. By integrating economic, social, and ecological dimensions into a unified framework, Pareto optimization explicitly reveals trade-offs among these aspects, providing policymakers with systematic pathways for optimization.

2. Holistic Cost Internalization: Social policies and environmental impacts are consolidated into quantifiable metrics, translating hidden costs (e.g., carbon footprint, infrastructure strain) into monetary terms. This approach mitigates over-parameterization risks in multi-objective models.

3. Generalizability & Practicality: The framework is adaptable to other tourism destinations suffering from overtourism, demonstrating strong generalizability. Its visual outputs and sen- sitivity analyses align with empirical trends, accurately reflecting real-world requirements and policy constraints.

8.2 Weaknesses

1. Temporal Simplification: The model ignores time-lag effects in tourism’s response to policy

changes. While elasticity coefficients partially correct deviations, their calibration remains subjective. Delayed demand adjustments necessitate dynamic extensions, for example, time- series models for long-term impact analysis.

2. Spatiotemporal Narrowness: External competition, infrastructure decay, and seasonal fluctua-

tions are excluded, potentially inflating optimization results. Future iterations should incorporate regional linkage mechanisms (e.g., cross-border tourism flows, shared infrastructure costs) to enhance realism.

9 Conclusion

The model provides a practical tool in places like Juneau, which balances simplicity with real-world applicabilityaddressing economic, society, and environmental benefit by hidden cost monetization . The fixed system approach allows quick policy solutions, matching the focus of cities on short-term budgets. Its strength lies in showing Pareto Optimization –— giving leaders clear metrics when managing tourism pressures. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m After expanding the model to Jiuzhaigou, China, although both locations are affected by overtourism, the measures adopted differ due to the distinct geographical attributes of the two areas. The model can well reflect the differences and similarities between the two places, and has good extensibility. Specific conclusion can be found in the table below:

City Jiuzhaigou, China Juneau, Alaska

Small population

Economiey predominantly dependent on tourism Similar Part Environment and society vulnerable to the impacts of overtourism The tourist destination is concentrated in a certain scenic spot Current Situation Relatively developed Relatively worse economy economy Closer to the Arctic, the Temperate regions have a Different Part ecosystem is even less more stable environment stable

Government spending There are differences in varies government policies

Lower Higher Tax rate

Key Proportion of Similar Similar Tourists Parameter Tourist Higher Lower Consumption Constraint More consideration of More consideration of Measures to Factors environment benefit economy benefit Mitigate Optimized Overtourism Number of tourists in Global Pareto Optimization Factors

Properly reduce local taxes, discount goods for tourists, and reduce tourist expenses to attract tourists

How to Promote Locations Achieve a win-win situation between tourists' that satisfaction and residents' satisfaction to achieve fame Have Fewer Tourists publicity Lucid water and lush mountains are golden hills and invaluable assets, which ensure a good environment as a tourist attraction

关注数学模型

Memo

To: Juneau Tourism Council

微信公众号：数学模型

Subject: Sustainable Tourism Management Recommendations for Juneau

Honorable Members of the Juneau Tourism Council,

The city of Juneau is attracting the attention and love of tourists with its beautiful natural landscape and comfortable living environment, which undoubtedly brings great economic benefits to the city of Juneau. However, it has been noted that due to the rapid increase in the number of tourists, the natural resources of the City of Juneau are being damaged and the normal life of the residents is being disturbed by the swarm of tourists.

Our assessment of the current state of tourism development in the City of Juneau indicates that if no management measures are taken to limit the number of visitors or protect the natural 微信号：MATHmodels environment, the number of visitors will remain above 1.6 million for the next decade, and the most popular attraction, the Mendenhall Glacier, will disappear from its current viewpoints within 25 years and completely recede within 90 years, which will inevitably affect the long- term tourism and economic development of the City of Juneau. As the makers of management decisions for tourism management in Juneau, it is important to develop appropriate management strategies to achieve sustainable tourism. To this end, we have constructed a mathematical model and propose the following actionable measures to you:

Measure 1: Increase Visitor Dispersion Methods: Increase publicity for niche attractions and limit visitor flow or periodically close popular scenic spots

Effect: The greater the dispersion of tourists, the more balanced the number of tourists accepted by each attraction, and when the dispersion of tourists is close to 1/n (n is the total number of attractions), the greater the total benefits.

Measure 2: Increase Tourist Consumption Methods: Increase tax rates and commodity prices at scenic spots Effect: When the tax rate and prices increase, the number of tourists decreases and the total benefits increases. The total benefit is greatest when the tax rate is adjusted to 0.58.

Measure 3: Determine the Optimal Number of Tourists Method: Analyze the number of tourists when the total benefits is maximum through Pareto optimality

Effect: Ensure the Sustainable evelopment of regional tourism and promote the maximization of social benefits. The social benefit is maximized when the total number of tourists is 1.32 million in the year.

Sincerely,

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m
