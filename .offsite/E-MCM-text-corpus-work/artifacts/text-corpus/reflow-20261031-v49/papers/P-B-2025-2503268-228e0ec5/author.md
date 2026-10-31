MCM/ICM

Summary Sheet

Overtourism has become a global challenge, disrupting economic growth, environmental protec- tion, and residents’ quality of life. Rising tourist numbers have caused environmental damage, strained

infrastructure, and social tensions. Meanwhile, strict tourism limits can reduce local income and well- being. This dual challenge highlights the need for sustainable tourism strategies and data-driven models to optimize resources and maximize overall beneﬁts.

We selected Juneau, Alaska, as the representative city for modeling. Tourist numbers, Equilibrium Line Altitude (ELA), and hotel tax revenue were chosen as indicators for population, environment, and economy, respectively. Inspired by the Lotka-Volterra model, logistic population model, and SIS model, we developed the Sustainable Tourism Dynamics Model (STDM). This system uses ordinary diﬀerential equations to capture and visualize interactions among the three dimensions.

Intervention strategies include tax revenue allocation and policies, enacted by the government. Both consist of predeﬁned measures represented by constraint vectors, serving as impact factors in the

STDM and evaluation model. Static and dynamic constraints ensure the feasibility of these strategies.

According to some materials, we propose to three main factors (life of local residents, local en- vironmental protection, local economy and development of society), and four secondary indicators for each main factor combined with Analytic Hierarchy Process (AHP) to attain the comprehen- sive evaluation score. The values from the strategies and the dynamic system are input to the system, related to the score via various equations.

The model integrates all components into a uniﬁed system, where variables strongly connect the sub-models. Intervention strategies serve as inputs to the STDM, and its outputs, combined with strat- egy choices, determine the AHP-based evaluation model’s score. This score provides feedback to optimize strategies dynamically. Using this process, governments can adjust interventions and pre- dict their outcomes. For example, our model improves a score from 0.446 to 0.692 through targeted interventions.

We assessed our model’s sensitivity using two methods. The Morris method identiﬁed key factors through the µ-ω diagram, showing that the environmental degradation coeﬃcient (k2) and tourism rev- enue factor (k6) had the strongest direct eﬀects and moderate parameter interactions. Local sensitivity analysis revealed that the growth rate of tourist numbers (r1) and baseline economic growth rate (k5) were most sensitive, with partial derivatives of 792.18 and 575.2. In contrast, crowding perception (εc) and carbon footprint scaling (ϑCE) showed low sensitivities, at 0.017 and -34.5 . These results highlight the importance of high-impact parameters and conﬁrm the model’s stability under small changes.

We tested our model’s adaptability in Big Sur, a coastal destination facing overtourism. Glacier- related parameters were replaced with region-speciﬁc indicators, such as coastal landslide rates (HSur = 2.1 m/year) and visitor numbers (NSur = 1,532,000 annually). The recalibrated model improved the normalized sustainability score from 0.32773 to 0.73563 with optimized strategies. Key recommenda- tions included strengthening infrastructure resilience and promoting inland attractions to ease coastal pressure. These results highlight the model’s versatility in managing overtourism and supporting sus- tainable tourism. A memo to the Juneau Tourism Council outlines predictions, impacts of measures, and strategic recommendations for sustainable tourism in Juneau.

Intervention Strategies, Analytic Hierarchy Process, Sensitivity Analysis

Memo

Dear Members of the Juneau Tourist Council,

Juneau's record-breaking 1.6 million cruise passengers in 2023 has undoubtedly brought significant economic benefits, but it has also amplified the challenges of overcrowding, resource depletion, and ecological strain, particularly on Mendenhall Glacier. As the glacier continues to recede, we must confront the reality that the very attractions drawing visitors to Juneau are under threat. Strikinga balance between tourism growth and sustainability is not just essential—it is urgent.

Our team has developed a dynamic model to address these challenges by evaluating the interplay between economic benefits, environmental conservation, and community well-being. Through this framework, we've identified actionable strategies that can optimize outcomes for all stakeholders.

First, we recommend implementing visitor caps at key attractions like Mendenhall Glacier to mitigate environmental stress while maintaining toun   dd sis  d   tsts sne ecological protection with revenue retention. Additionally, allocating a gr orrf  u nr  user o rtod rueos glaats d a i e  ai ie the natural environment and extend the lifespan of Juneau's unique attractions. For example, directing 40% of annual tourism revenue toward environmental initiatives could reduce glacier degradation rates by up to 30% annually.

Equally important is addressing the concerns of Juneau's residents. Overcrowdingand rising housing costs have left many locals feeling sidelined tn em  e l  r     ust  s using tourism revenues to improve housingaffordability andprovide community incentives, such as tax relief or subsidies for residents. These measures not only ease tensions but also reinforce the idea that sustainable tourism benefits everyone—not just visitors.

Sustainable tourism is a delicate yet achievable goal for Juneau. By integrating ecological protection, community engagement, and thoughtful revenue allocation into its policies, the city can preserve its natural beauty and economic vitality for years to come. We are confident that the strategies outlined above will provide a robust starting point for achieving this vision.

Sincerely,

MCM Team #2503268

January 27, 2025

1 Introduction

1.1 Problem Background

Juneau, Alaska, renowned for its stunning natural landscapes and rich tourism resources, has be- come a prominent destination for cruise passengers. But the rapid increase in tourist numbers in recent years has posed signiﬁcant challenges to the local environment, infrastructure, and residents’ quality of life. While measures such as daily visitor caps and agreements with cruise operators represent initial steps toward addressing these issues, they remain insuﬃcient to ensure the sustainable development of tourism in the region.

Notably, the challenges faced by Juneau reﬂect a global issue. Numerous destinations worldwide grapple with similar issues. Destinations like Mount Rainier National Park use reservation systems, while Venice and Barcelona impose day-trip fees. Athens is exploring tourist limits, highlighting the need for a framework balancing economic beneﬁts and conservation. This work aims to create a scal- able model for sustainable tourism, addressing Juneau’s needs and oﬀering solutions for overtourism and long-term resilience.

1.2 Restatement of the Problem

To ensure the sustainable development of Juneau’s tourism industry, we aim to develop a scien- tiﬁc model and management strategies to balance the number of visitors, revenue, and resource conservation. To achieve this, we need to address the following problems:

1. Develop a model to optimize the sustainability of Juneau’s tourism industry. Clearly deﬁne the objectives to optimize (e.g., number of visitors, revenue growth) and constraints (e.g., infras- tructure capacity, environmental protection), and propose management strategies to stabilize the industry.

2. Perform sensitivity analysis to evaluate the impact of various factors in the model and identify key variables that critically inﬂuence sustainable development, enabling policymakers to adjust strategies eﬀectively.

3. Adapt the model to other tourist destinations, assess its applicability, and reﬁne it to promote less-visited attractions and improve tourism balance across diﬀerent locations.

1.3 Our Work

To address the challenges of sustainable tourism in Juneau, we propose a tourism system made up of a Sustainable Tourism Dynamics Model (STDM), an Evaluation Model and Intervention Strate- gies. The SDTM, formulated with ordinary diﬀerential equations (ODE), establishes the relationships among key variables, including environmental degradation, tourist numbers and tax revenue from tourism. The Intervention Strategies contain ﬁnite number of predeﬁned strategy combination that will inﬂuence the dynamics with the STDM. The resulting outputs from the STDM, along with the strategy combinations, are assessed through an Analytical Hierarchy Process (AHP)-based evaluation model, which will give feedback to reﬁne and optimize the strategy combination.

Then, we apply the model to both Juneau and Big Sur, utilizing location speciﬁc parameters to conduct comparative analyses and predict optimal strategies for sustainable development. By applying this model, we predict the best intervention strategies and the comprehensive development of the places. In this way, we can give useful suggestions to the government. By analyzing results and doing sensitivity analysis, we have an insight of the strengths and weaknesses of the model. 关注数学模型 微信公众号：数学模型 微信号：MATHmodels

2 Assumptions and Justiﬁcations

Through the full analysis of the problem, to simplify our model, we make the following reasonable assumptions.

• Assumption 1:Government policies are assumed to be fully implemented instantaneously.

→Justiﬁcation: In reality, the time required for policy implementation can vary depending on administrative processes, public response, and logistical challenges. However, these delays are often unpredictable and context-dependent, making them diﬃcult to generalize within a theoretical framework. By assuming instantaneous implementation, the model prioritizes the analysis of long-term systemic outcomes and policy eﬀectiveness, enabling clearer insights into the relationships between variables.

• Assumption 2: Incidents, sudden changes, minor factors and extreme situations are not taken into consideration.

→Justiﬁcation: Including these factors would greatly increase the model’s complexity without

signiﬁcantly enhancing its predictive accuracy in typical scenarios. Such events are rare, unpredictable, and context-speciﬁc, making them hard to generalize. Focusing on primary factors ensures the model remains eﬃcient, broadly applicable, and capable of capturing essential system dynamics.

• Assumption 3: When determining strategies, some stable variables, are treated as con- stants. →Justiﬁcation: Stable variables like the local population show minimal short-term ﬂuctuations and have little impact on system dynamics. Treating them as constants avoids unnecessary complexity, allowing the model to focus on key drivers of change while remaining eﬃcient and easy to analyze.

• Assumption 4: The data and materials used in the model are accurate, reliable, and sourced from trusted and authoritative databases or publications.

→Justiﬁcation: The assumption of data reliability ensures consistency and avoids errors caused

by faulty or incomplete information. All data used in this model is sourced from reputable organizations, government reports, or peer-reviewed publications, which guarantees its cred- ibility and relevance.

3 Notations

Important notations used in this paper are listed below.

Symbol

Description Unit HJuneau Glacier ELA height in Juneau, m NJuneau Annual number of tourists in Juneau / TJuneau Annual hotel tax revenue in Juneau $ H↑ Normalized HJuneau / Juneau N↑ Normalized NJuneau / Juneau T ↑ Normalized TJuneau / Juneau P↑ The resident population in Juneau / Juneau HS ur Height of coastal landslide loss in Pfeiﬀer Big Sur cm NS ur Annual number of tourists in Pfeiﬀer Big Sur / TS ur Annual revenue gained from tourism in Pfeiﬀer Big Sur $ H↑ Normalized HS ur / S ur N↑ Normalized NS ur / S ur T ↑ Normalized TS ur / S ur P↑ The resident population in Pfeiﬀer Big Sur / S ur S core The weighted comprehensive assessment score of the current year / S corei The weighted score considering the ith factor / S coreij The score considering the jth secondary indicator in the ith factor / Factors of disturbance in variable x % ϖx Percentage distribution of tax revenue of infrastructure, glacier protection, µ1 to µ5 % waste disposal, cultural development and police security.

关注数学模型

Model Preparation

4

4.1 Data Collection

This problem lacks predefined data, requiring careful selection of data to collect before and during modeling. Key data sources are outlined in Table 2. Due to the vast and diverse data available, listing everything is impractical. Instead, we focus on accurate and representative data for effective modeling.

Data Description

Annual Hotel Tax in Juneau Annual Number of Tourists in Juneau

Data Source

https://juneau.org/finance/controller https://juneau.org/wp-content/uploads/2024/02/ Juneau-Visitor-Circulator-Study-Final-Report-2024-1.pdf Annual Glacier ELA height in Juneau Juneau Tourism Management Plan https://www.nature.com/articles https://juneau.org/wp-content/Juneau-Tourism-Mgt-Plan State Park System Statistical Report California Coastal Cliff Erosion Survey https://www.parks.ca.gov https://siocpg.ucsd.edu/ca-cliff-viewer/

To minimize the influence of unknown factors and simplify the complexity of the model, we estab- lish a three-dimensional coordinate system encompassing population, environment and economy. We collect data on glacier ELA height, tourist numbers and hotel tax revenue as representative indicators for each dimension. In the following subsections, we will elaborate on the rationale behind selections.

1 Data Selection Explanation 4.2

First, from an environmental perspective, the carbon footprint is a common evaluation standard in academia. To visualize our model, we analyze its direct impact on the Equilibrium Line Altitude (ELA)—the glacier elevation where annual snow accumulation equals annual melt, separating the accumulation and ablation zones. The process is shown in the figure below.

Snow Equilibriu line

Sublimation Calving Iceberg Zone of ablation Zone of accumulation

Flow trajectory Meltwater pool on glacier Terminus (toe) Meltwater Meltwater tunnel stream Secondly, considering that the number of tourists far exceeds the local resident population, and given the distinct impacts these two groups have on the environment and economy, the local population can be considered negligible in the population dimension. This makes it reasonable to use tourist numbers as a representative indicator for the population metric. According to the most recent Juneau Tourism Survey, hotel revenue consistently accounts for a stable proportion of the total government revenue. Therefore, we use hotel tax revenue as an indicator to represent the economic dimension.

5 Model Design

5.1 Sustainable Tourism Dynamics Model (STDM)

Natural environments, economic factors, and population dynamics are deeply interconnected. This study aims to represent the dynamics between glacier ELA height, annual number of tourists, and annual hotel tax revenue using fundamental data. Such a model provides an essential explanatory m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m framework for understanding the logical relationships between these factors, laying the foundation for m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m more detailed analysis and decision-making in subsequent sections. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

5.1.1 Glacier ELA Height Dynamics

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m One critical aspect of glacier health is the Equilibrium Line Altitude (ELA), which represents the altitude on a glacier where accumulation and ablation are balanced. According to the study by Braithwaite et al. [1], changes in ELA are driven primarily by temperature and precipitation. As the ELA rises, it reﬂects increased glacier melting and reduced stability. Similarly, another study by Oerlemans [2] highlights that ELA is a key indicator of glacier health and is directly aﬀected by climatic variations.

The ELA is inﬂuenced by feedback mechanisms within the glacier itself. For instance, the albedo eﬀect causes melting glaciers to absorb more solar radiation as their surface darkens, further acceler- ating the loss of ice. This intrinsic dependency makes the ELA height of glacier HJuneau sensitive to its prior state, represented in the model by k1HJuneau.

Tourism signiﬁcantly aﬀects glacier health. Increased tourist numbers NJuneau can lead to en- vironmental degradation through waste, infrastructure development, and direct interaction with the glacier environment. These impacts are proportional to both the existing glacier health and the level of tourism, captured in the term k2HJuneauNJuneau.

Economic factors, such as investments in preservation funded by hotel tax revenue TJuneau, also play a vital role in mitigating the negative eﬀects of tourism. Higher revenues enable conservation projects, such as restricting access to sensitive areas or implementing restoration eﬀorts. This dynamic is mod- eled as k3TJuneauHJuneau, showing how economic resources contribute to sustaining glacier health.

Bringing these factors together, the equation governing glacier health HJuneau is expressed as:

dHJuneau = k1HJuneau + k2HJuneauNJuneau + k3TJuneauHJuneau. (1) dt

Here, k1 represents the intrinsic changes in glacier health due to natural processes, k2 quantiﬁes the impact of tourism, and k3 captures the restorative eﬀects of economic investments.

关注数学模型

5.1.2 Tourist Number Dynamics

The dynamics of tourist numbers NJuneau are governed by both natural growth patterns and their in- teraction with the glacier environment. According to Verhulst’s logistic model [3], population growth typically follows an S-shaped curve, with initial exponential growth slowing as it approaches the car- ! " 微信公众号：数学模型 1 ↓NJuneau rying capacity K. This relationship is represented by the term r1NJuneau , where r1 is the K intrinsic growth rate and K is the environmental or infrastructural limit for tourist numbers.

The health of the glacier environment HJuneau also plays a critical role in attracting tourists. Re- search by Buckley [4] shows that pristine natural environments signiﬁcantly boost tourism demand. This inﬂuence is captured by the term k4HJuneauNJuneau, which indicates that better glacier health am- pliﬁes tourist numbers.

Combining these factors, the equation for tourist numbers NJuneau is expressed as:

# $ dNJuneau 1 ↓NJuneau = r1NJuneau + k4HJuneauNJuneau. (2) dt K 微信号：MATHmodels Here, r1 represents the natural growth rate of tourism, constrained by the carrying capacity K, while k4 quantiﬁes the positive impact of glacier health HJuneau on tourism growth. Together, these terms de- scribe the interplay between environmental conditions and tourism dynamics, providing a framework to assess the sustainability of tourism in glacier regions.

5.1.3 Economic Dynamics

The dynamics of annual hotel tax revenue TJuneau are closely tied to tourism and economic factors. According to studies on tourism-driven economies [5], the revenue generated from hotel taxes is di- rectly proportional to the number of tourists. This relationship is captured by the term k6NJuneau, which indicates that an increase in tourist numbers NJuneau results in higher tax revenue.

In addition, economic growth independent of tourism also plays a role. Research by Frechtling [6] shows that baseline economic trends contribute to steady growth in tax revenue, even in the absence of signiﬁcant changes in tourism. This baseline growth is represented by the term k5TJuneau, which accounts for general economic development and inﬂationary factors.

Combining these inﬂuences, the equation for hotel tax revenue TJuneau is expressed as:

dTJuneau = k5TJuneau + k6NJuneau. (3) dt Here, k5 represents the baseline economic growth, while k6 quantiﬁes the direct contribution of tourist numbers NJuneau to tax revenue.

5.1.4 Model Integration and Parameter Estimation

To evaluate the interconnected dynamics of glacier health, tourist numbers, and hotel tax revenue, we integrate the above equations into a single system. Using data from 2010 to 2019, we estimate the parameters ki and ri through nonlinear regression. Due to the complexity of real-world systems, these parameters are inﬂuenced not only by the core variables but also by external, unmeasured factors. Speciﬁcally, the anomalous marine heatwave event known as “The Blob” in 2013 signiﬁcantly aﬀected m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m glacier data for that year. To address this, we excluded the 2013 data from the analysis and performed interpolation on the remaining years to ensure consistency. The adjusted dataset was then used to ﬁt the equations and estimate ki and ri.

The ﬁnal integrated system of equations, including ϖ, is expressed as:

dHJuneau = k1HJuneau + k2HJuneauNJuneau + k3TJuneauHJuneau + ϖHJuneau, (4) dt # $ dNJuneau 1 ↓NJuneau = r1NJuneau + k4HJuneauNJuneau + ϖNJuneau, (5) dt K dTJuneau = k5TJuneau + k6NJuneau + ϖTJuneau. (6) dt

关注数学模型 The ﬁtting results and the corresponding parameter values are visualized in Figure3, and the ac- curacy of the model is validated using historical data. Using data from 2010 to 2019, we performed parameter ﬁtting for the integrated model equations. The resulting parameter values were derived through nonlinear regression, incorporating the error terms ϖHJuneau, ϖNJuneau, and ϖTJuneau to account for external unmeasured inﬂuences.

showing the dynamic interactions between glacier health HJuneau, tourist numbers NJuneau, and hotel 微信公众号：数学模型 tax revenue TJuneau. The ﬁtted trajectories closely align with the observed data points, suggesting that the model captures the essential dynamics of the system.

Additionally, Figure3 displays the feasible regions in the (HJuneau, NJuneau), (HJuneau, TJuneau), and (NJuneau, TJuneau) planes. These regions represent the range of plausible model outcomes given the ﬁtted parameters. The observed data points (red stars) fall predominantly within these feasible regions, further validating the model’s predictive accuracy.

The results highlight several key insights:

1. The positive correlation between the ELA height of the glacier HJuneau and the tourist numbers NJuneau is evident in the trajectories, supporting the hypothesis that an increase in visitors nega- 微信号：MATHmodels tively impacts the environment, thereby causing the ELA height to rise.

2. Annual hotel tax revenue TJuneau shows a direct dependency on tourist numbers NJuneau, as indi- cated by the tight clustering of observed data along the model trajectories in the (NJuneau, TJuneau) plane.

3. Variability in the system, represented by the error terms ϖ, likely captures external factors such as climatic anomalies or economic shocks, which are not directly modeled but are essential for explaining deviations.

These ﬁtting results provide a robust foundation for analyzing the dynamic interplay among nat- ural, social, and economic factors, and they oﬀer valuable insights for policy-making and resource management in glacier regions.

5.2 Intervention Strategies

5.2.1 Intervention Impact on Models

To maintain a balance between the three variables when maximizing utility, we categorize our intervention strategies into two components: tax revenue allocation and policies. Each component features a ﬁnite set of typical and representative solutions. By iterating through these solutions, we obtain a ﬁnite set of potential strategy combinations.

Given the current values of HJuneau, NJuneau, and TJuneau, each combination, under the given con- straints, produces new HJuneau, NJuneau, and TJuneau values along with corresponding scores. We then select the combination with the highest score to serve as the current intervention strategy, and update HJuneau, NJuneau, and TJuneau accordingly to these new values.

5.2.2 Tax Revenue Allocation

The variables µ1, µ2, µ3, µ4, µ5 are inputs to the evaluation model. We modeled nine representative arrays [µ1, µ2, µ3, µ4, µ5] based on diﬀerent allocation patterns, which are displayed in the ﬁgure below.

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

5.2.3 Policies

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m We design 8 policies with diﬀerent focuses and assign diﬀerent vectors v1, v2, v3 to each policy. The vector satisﬁes ↓v1 + v2 + v3 = 10 as 10 is the sum assigned to the policies but H is a negative indicator. The detailed 8 policies are as follows:

Policy Description Vector Promote local business development [0, 0, 10] Comprehensive and balanced development [↓3, 3, 4] Develop infrastructure [↓4, 4, 2] Market promotion and brand building [0, 4, 6] Direct measures to attract tourists [↓2, 8, 0] Improve tourist experience [0, 8, 2] Natural resource conservation [↓13, 0, ↓3], [↓14, ↓2, ↓2]

model to decide the policies too.

6 Evaluation Model

6.1 Indicators Determination

Based on the statement of the question and the literature, the degree of comprehensive devel- opment in the City of Juneau can be mainly categorized into three factors, which are life of local

关注数学模型 微信公众号：数学模型

residents(LoR), local environmental protection(EP), along with local economy and development of society(EDoS). 微信号：MATHmodels In consideration of tourism impact, We have overall listed 29 secondary indicators that are related to the three main factors, and picked 4 most signiﬁcant secondary indicators for each main factor. The main factors and related secondary indicators are listed below.

Factor Indicator Score No- tation LoR the increase of average individual income S 11 crowding level S 12 housing aﬀordability S 13 noise level S 14 EP natural resources like glacier coverage S 21 water and energy usage S 22 waste production level S 23 carbon footprint S 24 EDoS tourism tax revenue S 31 employment growth S 32 cultural resource protection or utilization S 33 social safety or security index S 34

6.2 Score Calculation Model

Here, P = 31685. Here we use the Analytic Hierarchy Process(AHP). AHP assigns weights to criteria through pairwise comparisons, checks the consistency of these comparisons, and calculates an overall score by aggregating the weighted scores, which is displayed in the formulas below. S core1, m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m S core2 and S core3 are scores computed from secondary scores, and the ﬁnal S core is the overall sum. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

• w1i, w2i, w3i: the weights assigned to each sub-indicator within the three factors that satisfy %4 i=1 wmi = 1, m = 1, 2, 3. This implies that for each main factor, the four sub-indicators sum to a total weight of 1.

• wi: the weight assigned to each of the three main factors S core1, S core2, S core3. These must satisfy:

& 3 wi = 1.

i=1 S core1 = Σ4 S core2 = Σ4 S core3 = Σ4 i=1w1iS 1i i=1w2iS 2i i=1w3iS 3i S core = Σ3 i=1wiS corei

According to some materials, the average time of tourists’ stay is around 4 days. So, the average number of tourists in Juneau each day is Nt = 4NJuneau 365 .

• The increase in average individual income The formula reﬂects the impact of tourism on average individual income by considering the ratio Juneau))↓ε ac- of tax income to population as a measure of income of tourism. The factor (1/(1+H↑ counts for the negative inﬂuence of glacier retreat on sustainable tourism growth, assuming that environmental degradation can harm long-term economic beneﬁts. Additionally, the logarithmic term incorporates the proportional allocation of tax revenue (µ1) to infrastructure, reﬂecting how government investments boosts economy. Normalization term T0/P ensures that income growth is evaluated in comparison with a baseline, while logarithm smooth out extreme values.

Inc = TJuneau 1 )↓ε · (1 + ϱ1 ln µ1 + 1 · ( µI + 1) (7) 1 + H↑ P Juneau S 11 = Inc T0/P = TJuneau 1 )↓ε · (1 + ϱ1 ln µ1 + 1 · ( µI + 1) (8) 1 + H↑ T0

• Crowding level Juneau

The formula quantiﬁes crowding based on the ratio of average daily tourists to the population (Nt/P), using a Sigmoid function to capture how perceived crowding increases at a decreasing rate as tourist density grows. This ensures that the score accounts for diminishing sensitivity to additional tourists in high-density scenarios. Also, the score is guaranteed to be normalized.

Parameters like εc and ς control the steepness and inﬂection point of the curve, respectively.

1 S 12 = ϑ · (9) 1 + e↓εc(Nt/P↓ς)

• Housing aﬀordability The formula for S 13 estimates housing costs (HCost) based on tourist density (Nt/P) and tax rev- enue allocated to infrastructure (T ↑ Juneauµ1). The study by Glaeser et al. [7] reveals the relation between number of tourists and housing aﬀorability.This reﬂects the dual pressures of increased demand for short-term housing and inﬂuences of infrastructure investments. The score is nor- malized within a historical range. The normalization method ensures that higher housing costs reduce the aﬀordability score.

关注数学模型 Nt P + ε2T ↑ HCost = ε1 (10) Juneauµ1 S 13 = Cmax ↓HCost (11) Cmax ↓Cmin

• Noise level We calculate noise levels as the sum of a baseline noise level (N0) and a power-law term , where 微信公众号：数学模型 tourist density contributes exponentially to increased noise. The normalization by CNN0 scales the score to reﬂect relative changes. The power-law term avoids extreme values by bounding the output.

Noise = N0 + N↑ϱ (12) Juneau = N0 + N↑ϱ S 14 = Noise Juneau (13) CNN0 CNN0

• Natural resources Measure natural resources by considering glacier retreat and tax revenue allocation to environ- mental protection. A Sigmoid function ensures a smooth transition as environmental pressure increases. The term εN · µE+1 µ2+1 · H↑ Juneau highlights the trade-oﬀbetween environmental investment 微信号：MATHmodels and degradation, as well as avoiding extreme values.

φ0 S 21 = (14) 1 + eεN· µE+1 µ2+1 ·H↑ Juneau

• Water and energy usage The formula evaluates water and energy consumption based on the combined population and tourist density (P + Nt). Sigmoid function captures the nonlinear relation, with ϱWE controlling the rate of increase and E0 serving as a baseline threshold. Meanwhile, the score is guaranteed to be normalized in this way.

Energy = ϱWE(P + Nt) (15) e↓(ϱWE(P+Nt)↓E0) 1 S 22 = 1 ↓ (16) 1 + e↓(Energy↓E0) = 1 + e↓(ϱWE(P+Nt)↓E0)

• Waste production level Waste production is calculated as the diﬀerence between normalized tourist density (N↑) and waste management impact (ϱCµ3T ↑), with a lower bound of zero. When waste generation ex- ceeds management reduction, penalize the score. The normalization by Cw(N↑+ 1) ensures the score remains bounded.

Waste = min(N↑ Juneau ↓ϱCµ3T ↑ Juneau, 0) (17) Cw(N↑+ 1) = 1 ↓min(N↑ Juneau ↓ϱCµ3T ↑ Juneau, 0) Waste S 23 = 1 ↓ (18) Cw(N↑ Juneau + 1)

• Carbon footprint The formula uses a Sigmoid function to keep the score in a reasonable range considering tourist population(Nt). ϑCE and NC control the sensitivity and baseline.

1 S 24 = 1 ↓ (19) 1 + eϑCE(NC↓Nt) • Tourism tax revenue Normalize the score in a reasonable range with history data.

S 31 = TJuneau ↓Tmin (20) Tmax ↓Tmin

• Employment growth The S 32 formula models employment growth as a linear combination of normalized tax income (T ↑ Juneau) and population (N↑ Juneau), with coeﬃcients representing the respective contributions of tourism and local demographics.

S 32 = ϱTT ↑ Juneau + ϱNN↑ (21) Juneau

• Cultural resource protection or utilization The S 33 formula measures cultural factors as an inverse exponential function of tax investment of culture (µ4T ↑ Juneau) and number of tourists’ spreading (N↑).

Juneau)N↑ S 33 = (µ4T ↑ (22)

• Social safety or security index According to study in an article by Hall, C. M. et al. [8], the S 34 formula was constructed to evaluate social safety by considering government allocated investment(µ5T ↑ Juneau) and population N↑ Juneau+1 (N↑ Juneau) on security resources. The term 1 ↓ Juneau+1) prevents division by zero and smooths ϑT µ5(T ↑ the impact of extreme values.

N↑ Juneau + 1 S 34 = 1 ↓ (23) ϑTµ5(T ↑ Juneau + 1)

6.3 Values of Parameters

We estimate the parameters using methods that substitute some speciﬁc values to compute the scores and make the scores reasonable. Some of the parameters are experience-based, and some come from multiplying known data by a certain ratio, which might be a growth rate or a disturbance rate, etc. The following table of parameter values was eventually obtained.

6.4 Weights Distribution Outcomes

To calculate the weights of AHP, we compare each each combinations of factors or secondary indicators and build up four judgment matrices. Through consistency check, by making sure CR < 0.1, we guarantee that the matrices are usable. The weights along with other useful calculated results and a heatmap of weights are as follows.

7 Analysis of Factors

We have now established the STDM model. In this section, we will compare and categorize the various factors, speciﬁcally identifying which components are to be optimized and which will serve as constraints. This analysis directly addresses the requirements of the ﬁrst sub-question in our study.

Considering the ultimate goal of sustainable development, all factors listed in the Score Calculation Model can be regarded as Optimization Factors. For the Constraints Factors, we approach the

关注数学模型 Parameter Value Parameter Value Parameter Value Parameter Value 0.2 T0 2448159 0.3 0.2 ε ϱ1 µI 0.8 0.6 2 0.4 ϑ εc ς ε1 微信公众号：数学模型 0.6 Cmax 0.5 Cmin 0.2 N0 1 ε2 3 CN 1.5 1 0.8 ϱ φ0 εN 1 0.2 E0 1 4 µE ϱWE ϱC 47528 1 Cw 1 Nc 24252 Tmax 1632106 ϑCE 25000 Tmin 1029604 0.25 0.75 5 ϱT ϱN ϑt

Parameter Score Score_1 Score_2 Score_3 微信号：MATHmodels Judgment Matrix         1 0.5 2.5 1 3 6 5 1 4 3 2 1 1 5 4 1 1 1 1 2 1 4 1 3 2 1 1 1 6 3 3 4 2 2.5 1 1 2 1 5 2 1 1 5 0.4 0.25 1 1 1 1 6 3 3 3 2 3 5 6 6 1 1 3 1 3 1 1 6 1 2 1 1 5 2 2 2 2 4 3 5

Max Eigen- 3.006 4.016 4.037 4.024 values Consistency 0.0028 0.0052 0.0125 0.0079 Index (CI) Consistency 0.0048 < 0.1 0.0057 < 0.1 0.0139 < 0.1 0.0088 < 0.1 Ratio (CR) Weights 0.3041, 0.5784, 0.4744, 0.4092, 0.5648, 0.2230, 0.1011, 0.4017, 0.1311 0.0823, 0.1873, 0.0795, 0.1163 0.2372 0.1096

system from three dimensions—population, environment, and economy—examining the limitations imposed by diﬀerent policies on these factors. For instance, as identiﬁed in the Juneau Climate Action and Implementation Plan, the policy introduced by the City of Juneau in 2016, which imposed caps on the number of daily visitors, serves as a constraint within the population dimension.

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

8 Results and Discussion

The ﬁtting results of the proposed model are shown in Figure 8, which compares the modeled and observed data for glacier health (H), tourist numbers (N), and hotel tax revenue (T). The red markers represent the observed data, while the blue dashed lines depict the model’s predictions. Overall, the model demonstrates a strong ability to capture the dynamic relationships among the three variables, with certain limitations in speciﬁc scenarios.

Based on the intrinsic relationships derived from the HNT data (glacier health, tourism numbers, and economic revenue) between time steps 10 and 19, we developed a quantiﬁable policy evaluation model. By integrating policy parameters (µ1, µ2, µ3, µ4, µ5) into the model, we identiﬁed the intersec- tion between the feasible policy region and the directional optimization boundary. This intersection represents the controllable scope of policies under current conditions. From this range, the model samples points and selects the one yielding the highest evaluation score as the optimal strategy.

关注数学模型 As the data of 2019 is the latest we have, we can approximate the situations then as those of now. As calculated, the best combination of allocation and policy is [0.15, 0.10, 0.35, 0.10, 0.30] and [↓3, 3, 4], which represents an allocation focused on safety and waste management and a policy highlighting 微信公众号：数学模型 comprehensive and balanced development, with a ﬁnal score of 0.6894.

We set a baseline of strategies representing a fairly average strategy. Sample some points of speciﬁc time and output the scores after applying our model and baseline and make a comparison, we draw a bar chart:

微信号：MATHmodels

According to the ﬁgure, the model-determined strategies make a diﬀerence, performing better than baseline. Under ideal circumstances, our model helps the government with making better decisions.

9 Sensitivity Analysis

9.1 Qualitative analysis: Morris Method

In order to understand which parameters predominantly shape the model outputs and where the strongest nonlinear interactions may arise, we perform a Morris global sensitivity analysis on two key aspects of our framework: (i) the ODE parameters {k1, . . . , k11}, which govern how H, N, and T evolve over time, and (ii) the evaluation model, which combines policy-related variables such as µi, ε, and ϱ1 into a single sustainability metric.

parameters, treating the residual ﬁtting cost as the model’s single-output measure, while the right panel (b) targets the evaluation function. In both panels, the horizontal axis µ↔represents each parameter’s main eﬀect: a larger µ↔implies that changes in that parameter lead to larger variations in the output on average. Meanwhile, the vertical axis ω captures interaction or nonlinearity: the higher the ω, the more the parameter’s eﬀect ﬂuctuates across diﬀerent combinations of other parameters.

In panel (a), k2 and k6 show the largest µ↔among ODE parameters, signiﬁcantly impacting model m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m ﬁt. Their moderately high ω suggests potential interactions or context-dependent eﬀects. Conversely, k10 and k1 show minimal eﬀects and nonlinearity.

Turning to panel (b), we observe that µ5 emerges with both a large µ↔and a relatively high ω in the evaluation function’s sensitivity plot, indicating a strong direct eﬀect on the score and pronounced variability under diﬀerent conditions. Other variables like ε or µ2 remain clustered near the origin, suggesting they exert less inﬂuence within the current parameter bounds. As in last year’s analysis, we conclude that parameters with high µ↔deserve focused calibration or policy-level prioritization, while those with large ω should be investigated for potential nonlinear or combined eﬀects.

Overall, these ﬁndings guide us in prioritizing certain ODE coeﬃcients (e.g., k2, k6) for reﬁned data collection or modeling eﬀorts, while also highlighting which policy parameters (e.g., µ5) most strongly aﬀect the sustainability outcome. The interplay between large µ↔and ω is especially important for anticipating how small changes in one parameter might yield disproportionately large or context- dependent shifts in ﬁnal model results.

9.2 Quantitative analysis: Local Sensitivity Analysis

Beyond the Morris global sensitivity, we have also conducted a local sensitivity analysis to evalu- ate how small perturbations in each parameter pi aﬀect the ﬁnal score ↼Score ↼pi . Table 7 shows a condensed version of the partial derivatives for selected top parameters, while Figure 7 provides a bar chart sum- marizing the average absolute sensitivity across multiple µ settings.

In general, parameters such as ϱ, r1, and k5 exhibit consistently large partial derivatives with respect to Score, indicating that even small changes can signiﬁcantly alter the sustainability metric. This aligns well with the global Morris analysis, in which these parameters also showed large µ↔values. On the policy side, µ5 retains notable sensitivity, reinforcing the idea that certain intervention intensities or policy measures (µ5) can drastically shift overall outcomes on log scale.

关注数学模型 微信公众号：数学模型

sent standard deviation across diﬀerent µ sets.

10 Reimagining Big Sur

微信号：MATHmodels

10.1 Fundamental Information

Overtourism is inherently site-speciﬁc [9], as each destination has unique contributing factors. However, various response strategies have been proposed or implemented to address these challenges. Our developed model enhances decision-making for better evaluation outcomes, and we have selected Big Sur, California, to validate its eﬀectiveness.

Big Sur, renowned for its rugged coastline, redwood forests, and scenic Highway 1, attracts mil- lions of visitors annually. However, its popularity presents sustainability challenges, exacerbated by natural disasters, road closures, and overtourism pressures. These issues raise critical concerns for both travelers and the tourism industry regarding the long-term accessibility and sustainability of this iconic destination.

In our data selection process, we have chosen Pfeiﬀer Big Sur State Park, a renowned tourist desti- nation, as a representative site for the Big Sur Section. To obtain relevant data on tourist numbers and economic growth, we utilized the annually published California State Park System Statistical Report. For visitor attendance, we aggregated the ﬁgures from Paid Day Use, Free Day Use, and Camping categories to represent the annual number of tourists in Pfeiﬀer Big Sur, denoted as NSur. Similarly, for government revenue, we calculated the total annual revenue generated from tourism in Pfeiﬀer Big Sur, denoted as TSur, by summing the income from User Fees, Concessions, and Miscellaneous revenue sources.

For the representation of environmental factors, we adopt a methodology inspired by the inno- vative approach of Cheryl J. Hapke and Krystal R. Green [10], who assessed the rates of landsliding and cliﬀretreat along the Big Sur coast by measuring crucial baseline indicators. Similarly, we incor- porate insights from the work of Zuzanna M. Swirad [11], who analyzed spatial and temporal trends m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Left Column Right Column ∂Score ∂Score Std Mean Rank Std Rank Param Param Mean ∂pi ∂pi 3.945 1.366 0.046 k2 0.134 k1 7 8 4.502 0.154 2.08 792.18 2 k3 6 r1 k4 463.57 k5 1.21 575.2 10.0 3 5 k6 2.15 k7 10 506.2 4 0 0 k8 12 0 k9 0 11 0 0 k11 4639 15.2 k10 13 0 0 1 0.98 0.53 0.01 15 X 234.6 9 β 18 T0 0.042 0.003 0.023 0.001 16 α1 19 -0.294 0.004 0.0617 0.002 20 γ μI 0.0008 22 -0.0027 0.0172 0.0001 23 βc θ -0.4874 0.019 21 -0.15 0.008 24 β1 β2 Hmax Hmin 0.90 0.021 -0.81 0.019 4 5 -18.14 0.45 25 40.2 N0 0 1 α CN -12.11 0.32 26 0.006 27 0.1048 φ0 -0.035 0.002 -0.024 0.001 29 βN 28 μE -332.5 9.12 E0 30 2 0.0015 0.0002 αWE Cw 78.45 1.23 24.78 0.98 3 6 αc Nc -34.5 1.01 45.87 1.45 17 14 γCE Tmax Tmin 0.84 0.02 -0.72 0.03 8 9 0.402 10 0.4825 0.012 0.011 11 αN lx 31 0.06 12 0.0033 0.0002 P 1.2 γt 32 0.02 0.001 33 -0.16 0.005 μ1 μ2 34 35 -0.0017 0.0001 0 0 μ4 μ3 36 0.1085 0.003 μ5

per row for compactness.

in California coastal cliff retreat. By leveraging these approaches and utilizing relevant data from the California Coastal Cliff Erosion Survey, we derive the height of coastal landslide loss in Pfeiffer Big Sur, denoted as Hsur:

10.2

Model Validation and Generalization

To assess the validity and generalizability of our model, we utilize three primary metrics derived from the data collected in Pfeiffer Big Sur State Park: annual visitor attendance (Nsur), govern- ment revenue (Tsur), and environmental impact indicators (Hsur). By normalizing these variables to eliminate dimensional discrepancies, we represent the dynamics of overtourism in a standardized form.

Our model is defined as a system of coupled differential equations, where each variable influences the others through non-linear interactions. Specifically, Hsur, representing the environmental degrada- tion, is influenced by visitor numbers (Nsur) and tourism revenue (Tsur) through terms like k2HsurNsur

关注数学模型 1993 2001 "The challenge is not to stop tourism. The challenge is how do we get it right." Costas Christ, Beyond Green Travel, Big Sur DsP Consultant

Join Monterey County Board of Supervisors, MCCVB, Big Sur businesses, and concerned 1986 93 residents to protect our coastal community and Point Sur State Historic ark its natural resources for generations to come.

Cos Nat ΔZ 1976 86 Mon OVENTOUISM ILING RG SUR

Coastal Cliff Retreat in Big Sur.

and k3TsurHsur, which account for the accelerated erosion due to human activity and mitigation efforts ● financed by tourism income. ●

dHsur = k1HSur + k2HSurNSur + k3TSurHSur, dt dNsur = r1Nsur (1 − (24) tp dTSur = k5T sur + k6Nsur. 1p

The model parameters (k1, k2, k3, . . .) were optimized using least squares to minimize the residuals between the predicted values and the normalized observed data, while incorporating tolerance thresh- olds to account for inherent variability in real-world systems. The optimization results demonstrated a high degree of alignment with the empirical data, indicating the robustness of the proposed model in capturing the dynamics of overtourism in Big Sur.

O For instance, when the data is normalized to [0.65694513,0.83935834,0.91277344], the model identifies a state of relative harmony among the environmental, economic, and passenger factors. This balance indicates that a policy focusing on comprehensive development is optimal. Specifically, the coordination across these dimensions ensures that growth in one factor does not come at the expense of another, fostering a sustainable and synergistic development strategy.

Comparing the original score of 0.32773 with the updated score of 0.73563, it is evident that the chosen policy direction significantly improves the overall system performance. The substantial increase in the normalized score reflects better alignment with the model's objectives and the achieve- ment of a more robust and balanced state. Thus, on the basis of balancing the environment, economy, and population, it helps us reimagining the fantasy of Big Sur.

11 Strengths and Weaknesses

11.1 Strengths

Strength 1: Comprehensive and Thorough Consideration of Key Aspects The model systematically addresses three critical dimensions: local residents' quality of life, natu- ral resource conservation, and economic and social development. In the quality of life dimension, it incorporates factors such as average individual income, crowding levels, housing affordability, and noise from tourists. For natural resource conservation, it evaluates natural resource utilization, energy consumption management, waste management, and carbon footprint. The economic and social devel- opment dimension includes tourism tax revenue, employment growth, cultural resource protection, and social safety. This multidimensional approach ensures that the model provides a holistic perspective and a robust foundation for policy-making.

Strength 2: Dynamic and Time-Responsive Design The model employs dynamic differential equations to simulate the evolution of key variables such as glacier health, tourist numbers, and hotel tax revenue over time. This enables the model to capture the interplay between factors like resource depletion and economic reinvestment, providing an insightful depiction of how policies affect outcomes in the long term. Its ability to simulate time-dependent interactions makes it a powerful tool for real-world application.

Strength 3: High Generalizability and Applicability

With its flexible structure, the model can be easily adapted to other cities or tourist destinations by adjusting region-specific parameters such as population size, tourism capacity, and resource allocation proportions. This versatility ensures that the model can serve as a standardized yet adaptable tool for addressing sustainability challenges in diverse contexts.

Strength 4: Quantifiable Policy Evaluation The model employs a scoring mechanism to quantitatively evaluate policy impacts across the three di- mensions. By aggregating the scores for local residents' quality of life, natural resource conservation, and economic and social development, it provides a clear and intuitive representation of policy effec- tiveness. This enables policymakers to quickly identify optimal strategies and focus on areas requiring improvement.

11.2 Weaknesses

Weakness 1: Limited Capacity to Address Unexpected Events

The model assumes a relatively stable external environment, making it less effective in accounting for sudden disruptions. For instance, the 2013 marine heatwave significantly impacted glacier conditions, and the COVID-19 pandemic in 2020 drastically altered human behavior globally. Such events fall outside the model's predictive scope.

Weakness 2: Ignorance of the Delay of Policy Implementation The model presumes policies are enacted and become effective immediately upon their introduction. In real-world scenarios, there is typically a delay between the announcement of a policy and its full implementation and impact. Accounting for the time required for policies to be rolled out and to in- fluence the system would add considerable complexity to the model, which is not currently addressed. This assumption may lead to inaccuracies in scenarios where timing of policy effects is critical.

关注数学模型
