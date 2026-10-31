MCM/ICM

Summary Sheet

Summary

Juneau, Alaska has become a popular tourist destination in recent years While tourism spurs economic growth, it also brings significant pressure on environment and local in- frastructure. To address this issue, we develop a multi-objective dynamic programming model that optimizes economic, environmental, and social outcomes for sustainable tourism management.

For Problem 1, we begin with a total tourist demand model, considering factors of nat- ural growth, seasonal variations, taxation effect, and government promotion. This model serves as an input to the three interconnected models. First, the economic model estimates profit by deducting operational costs from tourism revenue, both of which are assumed to scale linearly with tourist volume. Second, the environmental model quantifies tourism’s impact through an index aggregating key ecological factors of temperature, ocean temper- ature, snowfall, and ocean pH using entropy weight method. This environment model also accounts for natural recovery and government intervention. Third, the social im- pact model evaluates resident satisfaction based on their attitudes towards public service stress, environmental quality decrease, and tourism taxation.

The objective of our model is to maximize economic profit, environmental sustain- ability, and resident satisfaction under constraints of tourist capacity, environmental protection measures, and government budget limitations. We use dynamic program- ming to solve the model and stimulate the results over a 5-year period. Our model recom- mends a dynamic tax rate in a range of 3.2% to 5.0%, and a schema of government expen- ditures with large portions of environmental protection and infrastructure construction. Our results predict a stable tourist volume of around 1.6 million visitors per year. Both government revenue and environment quality rise steadily after implementing our rec- ommended policies. Additionally, we perform a sensitivity analysis to identify the most influential factors and assess the robustness of proposed policy measures.

For Problem 2, we further validate our model by adapting it to the tourism situation of Miami, another destination troubled by overtourism. Differences in culture, visitor behavior, and government intervention require adapation of parameters of our model.

For Problem 3, we prepare a memo for the tourism council of Juneau. Based on the predicted results given by our model, we summarize key findings and offer practical rec- ommendations to achieve sustainable tourism development.

In conclusion, our multi-objective dynamic programming model provides a compre- hensive framework for balancing economic, environmental, and social aspects of Juneau tourism. Our model has certain limitations to some extent, including potential uncertain- ties in data and simplifications made towards complex human-environment interactions. In future work, we could optimize our model using more granular data and refine our assumptions to further improve the model’s predictive capabilities.

Introduction

3 1

1.1 Problem Background

3

Problem Restatement

1.2 3

1.3 Our Work .

4

Preparation of the Models

4 2

2.1Assumptions

4

2.2 Notations .

5 2.3

Data Preparation

6 ITHmodels

The Models

7 3 7 3.1 Tourist Demand Model

Economic Benefit Model

3.2 9

Environmental Impact Model

3.3 10 3.4

Resident Satisfaction Model

12

Model Solving using Dynamie Programming

12 3.5

Sensitivity Analysis

17 4 17 Average Input of Environmental Index 4.1 17 4.2 Average Input of Resident Satisfaction 18 Average Input of Tourist Count 4.3

Adaptability of the Model

19 5

5.1 Data Collection and Processing

19

5.2 Adaptation to Miami tourism

20

5.3 Promotion of Attractions with Fewer Tourists

22

Strengths and Weaknesses

22 6

6.1 Strengths .

22

6.2 Weaknesses

23

Memo: Sustainable Tourism Recommendations for Juneau

24 8 微 25 9

关注数学模型 微信公众号：数学模型

1 Introduction

1.1 Problem Background

Juneau, Alaska has become a popular choice for visitors with its glacier, wild animals, museums, and historic districts. Local tourism has grown significantly in the past decades. This remote town with a population of about 30,000 set a record of 1.6 million cruise pas- sengers in 2023. While the huge number of tourists has brought unprecedented develop- 微信号：MATHmodels ment for the local economy, people should attach importance to the negative environmen- tal and social impacts simultaneously. Mendenhall Glacier has experienced rapid retreat, warning people of the costs of overtourism. Meanwhile, according to recent reports, the rising pressure on public services and the increased congestion in the transportation sys- tem are major concerns of local residents.

In order to restrict the development of overtourism, a few measures are enacted, in- cluding limiting the tourist capacity and increasing tourism taxes. These efforts serve as a start point for pursuing the sustainable tourism plan for Juneau in the long-term. It is imperative to figure out a more considerate approach to achieve an equilibrium between economic growth and social well-being.

1.2 Problem Restatement

The status quo in Juneau demands a solution to the ongoing issues regarding eco- nomic, environmental, and social aspects. Through in-depth investigation and analysis of m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m the problem’s context, the objectives are restated as follows: m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m • Construct a model that takes into account both the economic benefits and hidden costs associated with tourism. Discuss a plan for government expenditures from additional revenues and demonstrate how these expenditures feed back into the model.

• Provide a sensitivity analysis for the model and identify the most important factors.

• Illustrate the adaptability of the model by applying it to another over-touristed desti- nation. Discuss which measures are most important in that context and demonstrate the application of the model on attractions and locations with fewer tourists.

• Write a memo summarizing the results of the model, including predictions, the ef- fects of different measures, and suggestions to promote sustainable tourism.

1.3 Our Work

The following figure describes our work in detail. We construct four models: total tourism demand model, economic benefit model, environmental impact model, and resi- dent satisfaction model. We go through a comprehensive process of preparing data, con- structing the models, analyzing the models, and discussing the results.

2 Preparation of the Models

2.1 Assumptions

Several assumptions are made to provide a robust foundation for model construction 关注数学模型 and analysis.

Assumption 1: Tourism revenue is assumed to increase linearly with the number of tourists, and the revenue per tourist is assumed to be constant.

Assumption 2: Profit maximization is the economic objective of the model, while taxes are still levied on tourism revenue.

Assumption 3: Seasonal effects (the difference between peak seasons and off-peak

seasons) influence tourist arrivals and revenue.

Assumption 4: The expenditure on environmental conservation only comes from

the government revenue generated from tourism taxes (with a constant proportion of tourism revenue).

• Assumption 5: Environment is assumed to have a natural rate of recovery, which is constant over time.

• Assumption 6: Tourism, which results in water pollution, carbon footprint, and other pollutions, is the only reason for environmental harm in Juneau, and can be quantized to a fixed value per tourist.

Assumption 7: Tourism growth rates are assumed to be in a reasonable range with- out abrupt changes. ATH

• Assumption 8: Tourism revenue generated per tourist is assumed to be fixed during the simulated period.

2.2 Notations

The primary notations used in this paper are listed in Table 1. Some detailed variables are not included in this table, which will be explained when used.

● ●

Unit Definition

Symbol

T Number of tourists People Tourism growth rate Percentage (%) 8 R Total tourism revenue million USD G million USD Government revenue from tourism taxation P million USD Total tourism profit Percentage (%) T Tourism tax rate Q Resident satisfaction index Dimensionless E Dimensionless Environmental index M million USD Government expenditures on tourism development S Seasonal adjustment factor Dimensionless

2.3 Data Preparation

Before constructing our model, we collect data related to tourism in Juneau, Alaska from various reliable sources, including government reports, climate monitoring organi- zations, and tourism industry research.

The data used in this study is obtained from the following sources:

• Tourism Data: The number of tourists and tourism revenue figures are collected from the Alaska Travel Industry Association’s annual reports and the City and Bor- ough of Juneau’s 2023 Tourism Survey Report. These reports provide statistics on visitor volume, revenue generation, and public sentiment regarding tourism activi- ties.

• Environmental Data: Climate-change-related information, including average tem- perature, total annual snowfall, and ocean temperature, is obtained from the Na- tional Oceanic and Atmospheric Administration (NOAA) climate database and the Alaska Climate Research Center. These institutions monitor and provide historical climate data for the region.

• Social Impact Data: Resident feedback regarding tourism impacts, particularly neg- ative attitudes of residents, is collected from the CBJ Tourism Survey 2023, which assesses public opinions on the effects of rising tourist numbers on daily life and public services.

from 2019 to 2023, with statistics of 2020 and 2021 affected by pandemic. We do not elim- nate these outliners as they could help us to determine the environmental and social de- velopment without tourists.

Year Tourist Tourism Resident Average Total Average Ocean count revenue negative temper- annual ocean pH (mil- (million attitude ature snowfall tempera- level (◦F) ture (◦C) lion) $) (%) (inches) m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 2019 1.33 237 6 41.2 118.7 6.3 8.06 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 2020 0 0 0 40.7 99.3 6.3 8.06 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 2021 0.125 25.6 8 41.0 121.0 6.4 8.05 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

2022 1.20 301 7 40.8 110.2 6.5 8.04

2023 1.65 375 11 40.6 108.5 6.6 8.04

and tourist volume over the years. The plot shows a strong positive correlation between 关注数学模型 tourist count and revenue, indicating a direct economic benefit from increased tourism.

Tourism Revenue vs Tourist Count Actual Data Fitted Values (Actual Domain) 500 Fitted Values (Extrapolated) Tourism Revenue (in million dollars) 400 微信公众号：数学模型 MSE: 922.28 R2: 0.96 300

200

100

0 0 50 100 150 200 250 Tourist Count (in ten thousands people)

3 The Models

微信号：MATHmodels We aim to find a sustainable tourism strategy that achieves a balance between eco- nomic, environmental, and social aspects. All of the models are built in order to achieve these objectives.

3.1 Tourist Demand Model

3.1.1 Base Tourist Demand Equation

The tourist demand model estimates the number of visitors to Juneau over time. The model accounts for economic conditions, taxation policies, and external demand shocks. The number of tourists, denoted as T(t) in year t, is influenced by the tourism growth rate g(t), the tax rate τ(t) applied to tourism revenue, and random demand shocks δ(t) that reflect external influences. Furthermore, the model includes the demand elasticity parameter γ, which captures the negative impact of taxation on tourism growth.

The detail can be described by equation (1):

T(t) = T(t −1) · (1 + g(t) −γ · τ(t) + δ(t)) (1)

This formulation assumes that tourism demand grows at a predictable rate, where tax increases result in reduced tourist arrivals based on an elasticity effect. The inclusion of stochastic demand shocks accounts for uncertainties such as economic downturns or geopolitical events, ensuring a more realistic model representation and according with economic theories.

3.1.2 Seasonal Adjustments

Tourism in Juneau shows significant seasonal variations due to climatic conditions and cruise ship schedules. To account for these fluctuations, our model introduces seasonal adjustment factors that modify the total number of tourists based on whether it is a peak or off-peak season. The total number of tourists T(t) is divided into peak-season tourists Tpeak(t) and off-peak tourists Toff(t), with the seasonal effects captured by multiplicative factors Speak and Soff. The detail can be described by the system of equations:

 Tpeak(t) = Speak · T(t)   Toff(t) = Soff · T(t)   (2) Speak > 1    Soff < 1 

The seasonal adjustment are determined based on historical trends, accounting for sea- sonal demand fluctuations. It allows better resource allocation and operational planning so that infrastructure and services can accommodate varying tourist volumes through- out the year. We assume that these seasonal factors remain relatively stable across years, influenced primarily by established travel patterns and climatic conditions.

关注数学模型

3.1.3 Policy Impact on Demand

The change of tourism demand is affected by government policies such as visitor caps and promotional efforts. The model incorporates policy-driven adjustments to the tourism growth rate. Specifically, we assume that the growth rate g(t) is affected by the (n    e  ( d   sc ost Meanwhile, M(t) can be represented as a proportion of government revenues generated by local tourism.

型 (g(t) = 8base − β · Ccap(t) + η · M(t) (3) M(t) = λG(t)

Here, 8base represents the baseline tourism growth rate without any government in- tervention, β is a sensitivity parameter that quantifies the negative impact of visitor caps on growth, and η measures the effectiveness of marketing and promotional efforts in rais- ing tourism demand. The visitor cap Ccap(t) is included to manage the carrying capacity of the region. A higher cap results in reduced growth due to negative effects of tourism suus ns p cu  c  a  oo g s snm Government expenditures on tourism, M(t) are implemented to increase demand by in- creasing attractiveness and public visibility.

●

3.2.1 Tourism Revenue

Tourism revenue is primarily dependent on the number of tourists and their average spending. The total tourism revenue R(t) at year t is modeled as a function of the number of tourists T(t), with a constant of the average revenue per tourist r, as described by equation (4):

(4)

Government revenue is obtained by applying a tax rate τ(t) to the total tourism rev- enue. The detail can be described by equation (5):

信 (5) G(t) = τ(t) · R(t)

3.2.2 Tourism Cost

In addition to the revenue, the operational costs associated with tourism must be si- multaneously considered to assess net economic benefits. The total cost C(t) is composed of fixed costs Cfixed and variable costs cvariable that scale with the number of tourists T(t). The detail can be described by equation (6):

C(t) = Cfixed + Cvariable · T(t) (6) The net profit P(t) from tourism activities, after accounting for operational costs, is given by equation (7). It is crucial for evaluating the long-term economic sustainability of tourism and guiding reinvestment strategies.

P(t) = R(t) −C(t) (7)

3.3 Environmental Impact Model

3.3.1 Environmental Index Calculation

The environmental index is computed by integrating various environmental variables, including temperature, snowfall, ocean temperature, and ocean pH level. The methodol- ogy consists of several key steps:

Normalization and Weighting Each environmental variable is normalized to the range [0, 1] to eliminate unit bias, using the formula:

m m m m m m m m m m m m m m m m m m m m m m x −xmin m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Normalized Value = m m m m m m m m m m m m m (8) m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m xmax −xmin m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Weighting is used to reflect the impact of each factor on environmental quality: m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

• Temperature and ocean temperature are assigned a weight of −1 (negative impact).

• Snowfall and ocean pH are assigned a weight of +1 (positive impact).

关注数学模型 Entropy-Based Weighting The importance of each variable is determined using entropy- based weighting. The use of entropy weighting prioritizes variables with greater variabil- 微信公众号：数学模型 ity, ensuring that the index remains sensitive to significant environmental changes. The entropy of each variable is calculated as:

Entropy = −∑pi log(pi) (9)

where pi is the normalized value of the variable. The entropy weight is then computed as:

1 −Entropy Entropy Weight = (10) 微信号：MATHmodels ∑(1 −Entropy)

Final Environmental Index Calculation The environmental index is calculated by com- bining the normalized and weighted environmental data using the following formula:

Environmental Index = ∑wi · xi −Indexmin (11) Indexmax −Indexmin

where wi represents the entropy-based weights and xi denotes the normalized values of the environmental factors.

3.3.2 Government Intervention

To control the negative effects of tourism on the environment, a fraction of govern- ment revenue from tourism taxation is reinvested into environmental conservation. The improved environmental index Esub(t), after applying government intervention. M(t) is the government expenditures, and α is the sensitivity of environment to the additional government expenditures. The environmental index is modeled as follows:

Esub(t) = E(t) + α · M(t) (12)

3.3.3 Environmental Recovery

By assumption, the environment has a natural recovery rate r that helps restore its quality over time. However, tourism activities continuously exert pressure on the ecosys- tem at the same time, as a function of the environmental harm factor caused by tourism h and the carrying capacity Tmax.

 T(t)  E(t + 1) = Esub(t) + r · (1 −Esub(t)) −h · (13) Tmax

3.4 Resident Satisfaction Model

3.4.1 Model Formulation

Resident satisfaction, denoted as Q(t), is influenced by the number of tourists T(t), the environmental index E(t), and the taxation rate τ(t) applied to tourism revenue. Our model assumes that an optimal level of tourism Topt exists, beyond which further in- creases in tourist numbers negatively impact resident satisfaction. In addition, increased taxation on tourism revenue leads to lower resident satisfaction due to potential financial burdens and rising costs.

1 −|T(t) −Topt|   + ω2E(t) −ω3τ(t) Q(t) = ω1 (14) Topt

ω1, ω2, and ω3 are weighting coefficients that represent the relative importance of each factor in determining resident satisfaction. A higher ω1 places more emphasis on managing the tourist population, whereas a greater ω2 prioritizes environmental quality, and ω3 controls the impact of taxation.

3.5 Model Solving using Dynamic Programming

关注数学模型

3.5.1 Variables Being Optimized

微信公众号：数学模型 In our model, we aim to maximize the following factors:

• Economic Profit P(t):

This represents the net benefit derived from tourism, calculated as total revenue minus operational and environmental costs.

• Environmental Index E(t):

A measure of environmental sustainability, reflecting the long-term ecological bal- ance affected by tourism activities. The model incorporates it within the value func- tion to ensure sustainability considerations. 微信号：MATHmodels

• Resident Satisfaction Q(t):

A social metric evaluating how tourism impacts local communities. It accounts for factors such as congestion, public services, and overall community well-being.

In sum, our model aims to maximize the profit derived from tourism while ensur- ing environmental sustainability and maintaining resident satisfaction. The optimization problem is formulated as follows:

V(t) = τ(t),M(t) {P(t) + ω4E(t) + ω5Q(t) + γV(t + 1)} max (15)

3.5.2 Variables Serving as Constraints

The optimization is subject to several constraints that ensure sustainability across mul- tiple dimensions:

T(t) ≤Cmax (16)

E(t) ≥Emin (17)

Q(t) ≥Qmin (18)

G(t) ≥M(t) (19)

where:

• Cmax – the maximum carrying capacity of Juneau’s infrastructure,

• Emin – the minimum acceptable environmental index to ensure sustainability,

• Qmin – the minimum threshold for resident satisfaction,

• M(t) – government expenditures in sustainability initiatives.

3.5.3 Decision Variables

Our model considers the following decision variables to optimize tourism growth while maintaining sustainability:

• τ(t) - The tax rate imposed on tourism revenue, influencing both government rev- enue and resident satisfaction.

• M(t) - Government spending allocated to attract tourists and stimulate economic growth. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

3.5.4 Solution Approach

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m The system evolves over time according to the following state transition equations, as m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

equation (1), equation (13), equation (14):

T(t + 1) = T(t) · (1 + g(t) −γ · τ(t))  T(t)  E(t + 1) = Esub(t) + r · (1 −Esub(t)) −h · Tmax 1 −|T(t + 1) −Topt|   + ω2E(t + 1) −ω3τ(t) Q(t + 1) = ω1 Topt

Our model solves the problem using backward dynamic programming, following these steps. First, we define state variables: tourist count T(t), environmental index E(t), and resident satisfaction Q(t). Second, we identify control variables: taxation τ(t) and promo- tional efforts M(t). Then we apply recursion to compute the optimal solution by solving equation (15) iteratively. At last, we trace back the optimal government decisions in our solution.

3.5.5 Model Solution

The model is implemented to optimize sustainable tourism management in Juneau over a following five-year period from 2024 to 2028 (since the data obtained end in 2023). The results shown in Table 3 provide insights into projected tourist numbers, environ- mental conditions, and economic performance under different demand shocks and policy 关注数学模型 interventions.

Year Tourists (ten Tax Gov Env Index Resident Sat thousands) Rate Revenue 微信公众号：数学模型 (%) (Million $) 1 153.7 4.2 14.0 0.029 0.882 2 154.8 4.2 14.1 0.076 0.893 3 152.2 5.0 16.6 0.123 0.832 4 158.3 4.0 13.8 0.170 0.899 5 168.3 3.2 11.71 0.181 0.917

微信号：MATHmodels

3.5.6 Discussion of Results

The results demonstrate a dynamic evolution of key metrics over the five-year period. The projected tourist population remains relatively stable, fluctuating between 1.52 mil- lion (152.2 ten thousand) and 1.68 million (168.3 ten thousand) visitors per year due to adjustments in taxation and demand shocks. The government applies varying tax rates ranging from 3.2% to 5.0%, generating steady annual revenue between $11.71 million and $16.6 million. The higher tax rates in Year 3 reflect an attempt to balance environmental m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m and social objectives, which is offset by slightly reduced tourist numbers. The environ- m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m mental index shows a clear upward trend, increasing from 0.029 in the first year to 0.181 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m by the fifth year. This indicates that government interventions and policies effectively mitigate environmental impacts while promoting sustainability. Resident satisfaction also exhibits a positive trend, improving from 0.882 in the first year to 0.917 by the fifth year. The results suggest that targeted policies, including cultural investments and controlled taxation, successfully balance economic, environmental, and social priorities. Overall, our model results demonstrate the importance of adaptive policies and balanced revenue al- location in achieving sustainable tourism in Juneau.

3.5.7 Plan for Government Expenditures

The additional revenue generated from tourism, primarily through taxation, should be strategically allocated across various components to support sustainable tourism manage- ment in Juneau. We assume that the expenditures are divided into four main categories: environmental protection and recovery, infrastructure development, subsidies to reduce financial burdens, and advertising to promote tourism. The distribution of these expendi- tures is given by our model’s predictions, taking into account the priorities and challenges faced in each year.

Investment in environmental protection increases significantly over the years, reflect- ing the importance of reducing the ecological impacts of tourism. These funds are directed toward projects such as preserving the Mendenhall Glacier, restoring biodiversity, and ad- dressing pollution caused by tourist activities. Spending on infrastructure development grows in a steady rate, in order to improve accessibility, public transportation, and util- ities to better accommodate the tourist population. Subsidies play an important role in reducing financial burdens on residents and motivating sustainable practices. Subsidies might include support for local businesses, discounted public transportation, or financial incentives for environment-friendly practices. Expenditure on advertisement and promo- tion starts at 17% in Year 1, focusing on attracting tourists to under-visited locations and highlighting off-peak seasons. As tourism stabilizes, the need for advertisement dimin- ishes.

关注数学模型

4 Sensitivity Analysis

微信公众号：数学模型

4.1 Average Input of Environmental Index

Output Components vs. Average Input Environmental Index Output Components Tax rate Infrastructure Subsidy 0.8 Advertisement Environmental protection

0.6 Output Components 0.4 微信号：MATHmodels 0.2

0.0 0.0 0.2 0.4 0.6 0.8 1.0 Average Input Environmental Index

The sensitivity analysis shows that the environmental index has the greatest impact on environmental protection investment. When the index is low, governments allocate more resources to restoration, while improvements reduce the need for such spending. This aligns with the ecosystem’s condition directly influencing preservation efforts.

Additionally, a lower environmental index leads to higher tax rates and reduced sub- sidies to discourage tourism and generate revenue for environmental restoration. These findings highlight the environmental index as a key factor driving investment decisions, emphasizing the need to balance sustainability with economic priorities.

4.2 Average Input of Resident Satisfaction

Output Components vs. Average Input Resident Satisfaction Output Components Tax rate Infrastructure Subsidy 0.5 Advertisement Environmental protection

0.4 Output Components 0.3

0.2

0.1

0.0 0.0 0.2 0.4 0.6 0.8 1.0 Average Resident Satisfaction

The sensitivity analysis shows that average resident satisfaction strongly influences m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m government policies, with subsidies being the most affected component. When resident m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m satisfaction decreases, subsidies are significantly increased as governments aim to address dissatisfaction by providing more financial support to ease public concerns. Conversely, higher satisfaction leads to reduced subsidies, as fewer interventions are needed to main- tain public approval.

Lower resident satisfaction also results in lower tax rates, as governments seek to re- duce the financial burden on residents to improve satisfaction levels. These findings high- light that resident satisfaction is the most important factor driving subsidies and tax rates, emphasizing its central role in shaping policies to balance public welfare and economic priorities.

4.3 Average Input of Tourist Count

Output Components vs. Average Tourist Count 0.8

0.7

0.6

Output Components Tax rate Infrastructure Subsidy Advertisement Environmental protection 0.3

0.2

0.1

0.0 25 75 100 125 150 175 200 225 50 Average Input Tourist Count (Million People)

The sensitivity analysis of average tourist count reveals its significant impact on var- ious output components, with advertisement spending being the most strongly affected. As the tourist count decreases, advertisement spending increases sharply, as governments prioritize promoting tourism to attract more visitors and boost economic activity. Con- versely, higher tourist counts reduce the need for extensive marketing, making tourist count the most critical factor influencing advertisement spending.

Interestingly, environmental protection investment increases as tourist count rises. This reflects the need to address the environmental strain caused by higher tourism activity and to ensure sustainability in the face of growing demand. A lower tourist count results in reduced subsidies and higher tax rates to compensate for the decline in economic con- tributions. These findings emphasize the pivotal role of tourist count in shaping govern- ment policies, particularly in balancing tourism promotion, environmental sustainability, and economic strategies.

关注数学模型

5 Adaptability of the Model

5.1 Data Collection and Processing

Miami and Juneau, though both facing overtourism challenges, show distinct tourism 微信公众号：数学模型 dynamics that require careful consideration in our modeling approach. Juneau, as a sea- sonal cruise-based destination, experiences significant fluctuations in visitor numbers, pri- marily influenced by seasonal factors and environmental constraints. In contrast, Miami is a year-round tourist hub with a diverse range of attractions, including beaches, cultural events, and nightlife, drawing visitors consistently across all seasons.

微信号：MATHmodels

The data is collected from a range of reliable sources. The demographic data such as population density, migration patterns, and ethnic group distributions are obtained from government databases and archival records. Some data are obtained from event statistics from major events such as Art Basel, Wynwood Art Walk, and the South Beach Wine & Food Festival. We also collect financial data related to cultural tourism revenue, public funding for the arts, and investments in cultural infrastructure from city budget reports. Lastly, we look for surveys such as the Knight Foundation’s Soul of the Community study provided insight into community engagement and perception of cultural activities.

To ensure comparability across indicators, the collected data are normalized using min-max scaling, which transforms data values into a comparable range of [0, 1]. Then, in order to determine the relative importance of each cultural indicator, the entropy weight- ing method is applied. Entropy measures the degree of variation in an indicator across all years. Once entropy values are calculated, the weights for each indicator are assigned.

A composite cultural index is derived by aggregating all weighted indicators for each year, providing a single measure of cultural evolution. This index captures the overall cultural development of Miami across different time periods. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m ∑ Ci = wjxij (20) j=1

Cultural Index and Tourist Count Trends in Miami (2019 2023) 7 1.0

6 0.8 Tourist Count (in millions) 5 Cultural Index 0.6 4

3 0.4 2 0.2 1 Cultural Index Tourist Count 0.0 0 2019 2020 2021 2022 2023 Year

5.2 Adaptation to Miami tourism

Miami’s tourism industry differs significantly from Juneau, requiring adjustments to our multi-objective dynamic programming model. While Juneau experiences highly sea- sonal tourism with a strong focus on natural attractions, Miami attracts a steady influx of international tourists year-round, drawn by its cultural, urban, and environmental offer- ings. The differences between the two cities and the corresponding model adjustments are summarized in Table 4.

City City Features

Model Features

• Small population with limited

• Overcrowding heavily im- Juneau pacts resident satisfaction. urban space.

• Transportation relies primar-

• Cruise passengers are consid- ered in tourist volume. ily on cruise lines.

• Environment is the primary

• Environmental impact is a attraction. key optimization factor.

• Infrastructure needs govern-

• Government expenditure is ment support. weighted higher for impact.

Continued on next page 关注数学模型 微信公众号：数学模型 City City Features

Model Features

• Large metropolitan area with

• Overcrowding has less im- Miami high population density. pact on resident satisfaction.

• More international travelers

• Focus on attracting interna- tional travelers. with strong purchasing power.

•

• Multiple factors (culture, en- Attractions and resources include environment, culture, vironment, economy) to opti- and cityscape. mize. 微信号：MATHmodels •

• Government expenditure has Developed infrastructure less impact. with private sector influence.

Year Tourists Tax Rate Gov Revenue Env Culture Resident (thousands) (%) (Million $) Index Index Sat 1 803.6 2.5 260.48 0.090 0.335 0.866 2 1040.1 2.5 337.11 0.149 0.342 0.865 3 1138.2 2.5 368.92 0.210 0.349 0.854 4 1473.4 2.5 477.56 0.273 0.359 0.843 5 1318.2 2.5 427.26 0.286 0.367 0.833

To accurately reflect Miami’s tourism characteristics, several key modifications are made to the model.

Unlike Juneau, Miami experiences relatively stable year-round tourist inflow with slight seasonal peaks. The demand function is adapted to account for these more con- sistent trends and include factors that influence international tourism. Miami’s tourist demand model incorporates cultural attractiveness, quantified by a cultural index C(t), and government promotion, formulated as:

T(t) = T(t −1) · (1 + g(t) −γ · τ(t) + δ(t) + η · C(t)) (21)

Miami’s environmental concerns, such as coastal erosion and pollution, require changes to the environmental index calculation. Snow-related factors are replaced with metrics re- flecting ocean conditions and urban emissions.

Additional variables such as traffic congestion and cultural engagement are incorpo- rated into the resident satisfaction function to capture Miami’s urban dynamics. Incorpo- rating Miami’s cultural diversity and urban challenges, the updated resident satisfaction equation is:

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 1 −|T(t) −Topt|   m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m + ω2E(t) + ω3C(t) −ω4τ(t) m m m m m m m m m m m m m m m m m Q(t) = ω1 (22) m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Topt In contrast to Juneau, Miami’s well-developed infrastructure reduces the role of gov- ernment expenditure, leading to a lower weight on infrastructure investments and a higher allocation towards cultural initiatives.

The results are shown in Table 5.

5.3 Promotion of Attractions with Fewer Tourists

To achieve a better balance in tourist distribution and promote under-visited locations, our model incorporates the following key strategies that align with sustainable tourism objectives:

• Dynamic Visitor Caps Our model dynamically adjusts visitor capacity based on environmental and infras- tructure constraints. We could increase limits for under-visited sites like rainforest trails and cultural heritage locations, so that a balanced tourist distribution can be achieved. The optimization process ensures that environmental degradation is min- imized while maintaining economic benefits.

• Tax Differentiation To encourage tourists to explore less-crowded destinations, the model applies a dif- ferentiated tax scheme. Popular attractions are subject to higher tax rates, while under-visited areas benefit from lower taxes, making them more attractive to budget- conscious travelers. The tax revenue generated from high-demand attractions can be reinvested in infrastructure improvements for less-visited tourist destinations, ensuring long-term sustainability.

• Targeted Promotions Our model optimizes the allocation of promotional budgets to highlight the wonder of less-visited locations. Based on evidence and data, our model identifies areas with growth potential and designs marketing campaigns showcasing diverse attractions such as whale watching and rainforest hikes as viable alternatives to overcrowded sites. This approach enhances the visibility of these locations and engages more tourists.

6 Strengths and Weaknesses

6.1 Strengths

• Comprehensive Framework: Our model integrates economic, environmental, and social dimensions, providing a holistic approach to sustainable tourism manage- ment.

• Adaptability: Our model can be applied to different destinations, as demonstrated in the Miami case study, ensuring its versatility across diverse contexts. 关注数学模型 • Dynamic Decision-Making: The use of dynamic programming allows for adaptive policy measures, such as varying tax rates and expenditure allocations, to respond 微信公众号：数学模型 to changing conditions over time.

• Quantifiable Insights: Our model provides measurable outcomes for decision-making by including key metrics like environmental index and resident satisfaction.

• Emphasis on Sustainability: Our model prioritizes long-term ecological preserva- tion and community well-being, aligning with global sustainable tourism goals.

6.2 Weaknesses

微信号：MATHmodels

• Data Dependency: The accuracy of the model depends heavily on the availability and reliability of historical and real-time data, which may not always be comprehen- sive or consistent. The tourism data is only available for the last five years.

• Simplifying Assumptions: Certain aspects, such as the constant recovery rate of the environment and fixed sensitivity parameters, may oversimplify complex human- environment interactions.

• Limited Stakeholder Representation: The model does not explicitly account for the diverse perspectives of stakeholders, such as local businesses or tourists, which could influence the outcomes.

• Computational Complexity: The dynamic programming approach, while power- ful, can become computationally intensive for more granular data or larger-scale applications.

8 Memo: Sustainable Tourism Recommendations for Juneau

To: Tourist Council of Juneau From: Team 2504448

Re: Sustainable Tourism Recommendations for Juneau

Date: January 28, 2025

In the memo, we want to provide the recommended measures to optimize sustainable tourism in Juneau based on the results of our model. After a comprehensive investigation of the local tourism development in the past years, we integrate economic, environmen- tal, and social objectives, hoping to provide actionable insights for policy decisions.

Predictions and Key Findings: Our multi-objective dynamic programming model gives

a plan for the goal of sustainability as well as the predictions of outcomes over the next five years:

• Optimized Tax Rate: The tax rate should follow a dynamic pattern, starting at 4.2% in Year 1, peaking at 5.0% in Year 3, and then declining to 3.2% by Year 5.

• Government Expenditures: A significant portion of revenue should be allocated to environmental protection. Infrastructure investments should gradually increase, while subsidies need to be a steady component supporting sustainable practices and reducing financial burdens on residents.

• Predicted Outcomes: In our prediction, the tourist volume stabilizes between 1.52 million and 1.68 million, reflecting the effectiveness of adaptive taxation and pro- motional efforts. Government revenue from tourism taxation ranges from $11.71 million to $16.6 million per year. The environmental index (a quantitative index computed in our model) improves significantly from 0.029 to 0.181. The score of resident satisfaction steadily increases from 0.882 to 0.917.

Policy Measures and Their Effects:

• Taxation and Revenue Allocation: Dynamic taxation ensures sustainable revenue while mitigating environmental and social impacts. Our model recommends priori- tizing environmental conservation and infrastructure development.

• Visitor Distribution: Visitor caps and targeted promotions encourage the visit of under-visited locations, reducing pressure on popular sites like Mendenhall Glacier.

• Community Engagement: Subsidies for local businesses and eco-friendly initiatives help reduce the financial burden on residents and encourage sustainable practices.

Recommendations: To optimize sustainable tourism in Juneau, we advise:

• Adaptive Policies: Maintain flexible tax rates and expenditure allocations, guided by real-time environmental and social data.

• Promotional Campaigns: Promote under-visited locations and off-peak seasons through m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m targeted marketing to distribute tourist dynamics more evenly throughout Juneau. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

• Feedback Mechanisms: Regularly gather input from residents and visitors to refine m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 关注数学模型 m m m m m m m m m m m m m m m m m m m m m m m policies and ensure alignment with sustainability goals. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

1. OpenAI Enie (Jan 27, 2025 version, Ernie 4.0)

Query1: What are the key factors of tourism in Juneau, Alaska? 微信公众号：数学模型 Output: Tourism in Juneau, Alaska, is influenced by several key factors:

1. Cruise Ship Tourism: Juneau is a popular stop for Alaska cruise lines, which oper- ate primarily during the summer months (May to September). The number of cruise ship arrivals and the season’s schedule significantly impact the flow of tourists.

2. Natural Attractions: Juneau’s breathtaking natural landscapes, such as the Menden- hall Glacier, Tracy Arm Fjord, and Mount Roberts, draw visitors. Accessibility and conditions of these attractions can influence tourism.

3. Wildlife Viewing: Opportunities to see wildlife, including whales, bears, bald ea- gles, and seals, are a major draw. Seasonal wildlife patterns and tour availability play a crucial role. 微信号：MATHmodels

2. OpenAI Enie (Jan 27, 2025 version, Ernie 4.0)

Query2: What are the key differences between Juneau tourism and Miami tourism?

Output: Key Differences Between Juneau and Miami Tourism:

1. Climate and Geography: Juneau features cool, rainy weather with glaciers and wilderness, while Miami offers tropical weather, beaches, and urban attractions.

2. Primary Activities: Juneau focuses on glacier exploration, wildlife viewing, and outdoor adventures. Miami emphasizes beach activities, nightlife, and cultural im- mersion.

3. Tourism Seasons: Juneau’s peak season is summer (May–September), whereas Miami attracts tourists year-round, with peaks in winter and spring.

3. OpenAI Enie (Jan 27, 2025 version, Ernie 4.0)

Query3: How to model government expenditure in a tourism destination using dy-

namic programming?

Output: Model government expenditure in a tourism destination using dynamic

programming by:

State: Define the state as the current period, available budget, and tourism infras- tructure status.

Decision: Specify spending options for each period (e.g., infrastructure, marketing, or conservation).

Transition: Model how spending decisions affect tourism revenue, infrastructure quality, and future states.

Reward: Define the objective, such as maximizing long-term revenue or tourist sat- isfaction.

Recursion: Use the Bellman equation to optimize spending decisions over time, con- sidering future rewards.

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m
