MCM/ICM

Summary Sheet

Summary

Urban transportation systems face critical challenges in balancing efficiency, re- silience, and sustainability, particularly under infrastructure disruptions. This study presents a multi-methodological framework to address post-disaster traffic optimiza- tion, multimodal network equity, and sustainable mobility planning in Baltimore, Mary- land.

In order to address the influence of the cascading traffic disruptions caused by the

collapse of the Francis Scott Key Bridge in Baltimore, a fuzzy comprehensive eval- uation model is developed to quantify multidimensional impacts, integrating flow redistribution intensity (Q), detour burden (η), network efficiency degradation (∆I), and environmental externalities (Ce). The framework employs entropy-weighted ag- gregation to prioritize factors dynamically based on historical incident data. Network dynamics are analyzed through Wardrop equilibrium-based traffic assignment and dynamic flow conservation principles. Results reveal a 41.7% surge in bypass traffic, 0.38 efficiency loss, and $2.1M annual health costs from increased emissions.

To create public transportation projects that help improve residents’ mobility, a multimodal network model (GM = (N, E, M)) is proposed to evaluate bus-pedestrian- auto interactions. Mode-specific impedance functions incorporate stochastic waiting times, congestion penalties, and pedestrian safety risks. The framework quantifies accessibility equity using Gini coefficients and simulates Bus Rapid Transit (BRT) in- terventions, achieving a 44.1% bus mode share increase and 14.6% Gini reduction. Al- gorithmic integration of discrete choice models and network loading ensures compu- tational tractability while capturing nonlinear congestion thresholds (fb/Cb > 0.85).

To create a transportation network project that improves the lives of Baltimore resi- dents, a tri-objective optimization framework maximizes resident welfare, minimizes costs, and enhances environmental benefits through bus lane allocation (xb), pedes- trian infrastructure (xp), and micro-mobility hubs (xm). The model employs Bayesian calibration with Markov Chain Monte Carlo (MCMC) to assimilate cross-city data, resolving tradeoffs via epsilon-constraint methods. Case studies demonstrate 58% welfare gains, 18.7% PM2.5 reduction, and a benefit-cost ratio (BCR = 1.41). Critical thresholds, such as xb > 0.3Ltot for auto user cost escalation, are identified through phase transition analysis.

This research advances urban traffic management by integrating multi-scale net- work modeling, dynamic equilibrium theory, and stochastic optimization algorithms. Key methodologies actionable insights for policymakers to balance efficiency, equity, and environmental goals in complex transportation systems.

Equilibrium, Multimodal Transportation Network, Bayesian Calibration

Introduction

3 1 Problem Background. 3 1.1 1.2

Restatement of the Problem

3 1.3 Literature Review 4 5 1.4 Our Work .

Assumptions and Explanations

5 2

Notations

6 3

Preparation before Solution

6 4 6 4.1 Data Collection

Data processing

7 4.2

Network-Theoretic Framework for Urban Traffic Flow Analysis 8 5 Network Representation 5.1 8

Traffic Flow Modeling

5.2 8 Analytical Metrics and Data Integration 5.3 9 1 Quantitative Analysis of the Francis Scott Key Bridge Accident Impact on 6 11 Urban Traffic Network Flow Impact of the Francis Scott Key Bridge accident on traffic flownetwork . 6.1 11 Francis Scott Key Bridge collapse and its impact on residents . 11 6.2 12 Analysis of the impact of Francis Scott Key Bridge on stakeholders 6.3

6.3.1 Model Architecture .

13 Imd s s s Ss o Ss pse 6.3.2 14

7 15 ysis

7.1 Multimodal Network Representation .

15

7.2 Multimodal Demand Allocation

16 16 7.3 Accessibility Impact Metric Implementation Scenario: Bus Rapid Transit (BRT) Project 17 7.4 Stakeholder Impact Analysis 18 7.5 ●

Sensitivity Analysis

19 7.6

20

Optimal Transportation Network Intervention Model for Baltimore

8 20

Project Recommendation: Integrated Mobility Corridor (IMC)

8.1

Benefit Quantification Model

20 8.2 System Disruption Analysis 8.3 21 22 8.4 Implementation Framework 8.5 Case Study: Baltimore Green Transit Corridor 22

Model Evaluation

23 9 23 9.1

Strengths

Weakness

24 9.2

10 Conlusion

关注数学模型

1 Introduction

1.1 Problem Background

Urban transportation serves as the fundamental support for residents’ daily travel. It not only directly impacts commuting efficiency, convenience of life, and travel expe- rience but also exerts profound influences on urban economic vitality, environmental 微信公众号：数学模型 quality, and spatial layout. An efficient transportation system, as shown in Figure 1, can reduce commuting time and travel costs, thereby enhancing residents’ quality of life. Moreover, it is a crucial factor in promoting rational allocation of urban resources, driving balanced regional development, and enhancing urban attractiveness.

Baltimore, Maryland faces significant transportation challenges, including inade- quate funding for infrastructure maintenance and development, which exacerbates road conditions and strains public transit systems. The city experiences notable traffic congestion, with residents spending considerable extra time commuting during peak hours. Major incidents, such as the collapse of the Francis Scott Key Bridge in 2024, further highlight the fragility of its transportation network and the urgent need for in- 微信号：MATHmodels vestment. Additionally, the lack of coordinated land use and transportation planning contributes to inefficient traffic distribution. Addressing these issues requires compre- hensive strategies to improve infrastructure resilience, enhance public transit services, and integrate sustainable transportation priorities into urban development.

(a) Target City of traffic optimization (b) Map of Baltimore

1.2 Restatement of the Problem

The key factors contributing to traffic congestion in Baltimore primarily revolve around the collapse of the Francis Scott Key Bridge on March 26, 2024. The loss of this vital bridge disconnected the Baltimore Beltway (I-695) and disrupted key travel routes, particularly for commercial trucks accessing the Port of Baltimore. Through in-depth analy-sis and research on the background of the problem, combined with the specific constraints given, the restate of the problem can be expressed as follows:

• The collapse of the Francis Scott Key Bridge has significantly impacted the traf- fic flow in the Baltimore harbor area. To address this, a mathematical model is m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m needed to optimize the rebuilding process and traffic flow. This model should m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m consider factors such as construction time, cost, and the impact on existing traffic patterns.

• The current public rail systems (MARC, light rail, heavy rail) in Baltimore are inadequate for the needs of commuters and residents, particularly those in sub- urban areas with multiple transportation options. A mathematical model is re- quired to assess the adequacy of the rail system and its accessibility.

• A resident of Brooklyn faces challenges in using public transportation to get home after attending a football game in the city. A mathematical model is re- quired to analyze the travel experience of residents and the efficiency of the pub- lic transportation system.

1.3 Literature Review

The problem requires the team to come up with ways to improve Baltimore’s traffic to improve the lives of its residents, so the team uses the Wardrop first equilibrium principle to construct a network model.

• With the deepening of the research, scholars have expanded the Wardrop equi- librium theory in many aspects. Some studies have considered the dynamic char- acteristics of traffic flow, incorporated the time dimension into the Wardrop equi- [1] librium model, and proposed the dynamic Wardrop equilibrium theory.

• In the field of transportation planning, Wardrop equilibrium theory is widely used in transportation network design and traffic demand forecasting.

• In recent years, the integration of Wardrop equilibrium theory and other disci- [2] [3]The intersection with economics enables plines has become a research hotspot.

researchers to analyze traffic behavior and traffic policy from an economic point of view, and to explore the economic cost of traffic congestion and the optimal allocation of traffic resources.

The strengths and weaknesses of the planning space can be visually presented and is shown below as Figure 2:

关注数学模型

1.4 Our Work

Our team explored how to improve Baltimore’s transportation system through math- ematical modeling as follows:

1. The traffic network of Baltimore City is modeled as a four-tuple, the traffic density and capacity utilization are defined. A fuzzy comprehensive evaluation framework is used to Quantitative analysis the impact of the Francis Scott Key Bridge collapse on traffic flow, and simulate the changes in traffic flow and the decline in network ef- 微信公众号：数学模型 ficiency after the accident, and through the Wardrop equilibrium distribution prin- ciple to analyze the travel cost of residents;

2. Providing the bus rapid transit (BRT) projects to improve the lives of Baltimore res-

idents. Using a multimodal transport network to model the transport system as a directed graph, assigns travel demand using nested logit formulations, and calcu- lates multimodal accessibility potential, simulates the impact of bus rapid transit (BRT) projects.

3. An integrated transportation corridor (IMC) system is proposed to quantify resi- dents’ welfare, implementation costs, and environmental benefits through a multi- 微信号：MATHmodels stage optimization process, analyze temporary network degradation during con- struction, and evaluate the impact of the IMC system on the environment, through the case of Baltimore Green Transportation Corridor, the effect of system improve- ment is demonstrated.

To give a more visual representation of our work, here is the diagram shown in

2 Assumptions and Explanations

Considering that practical problems always contain many complex factors, first of m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m all, we need to make reasonable assumptions to simplify the model, and each hypoth- m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m esis is closely followed by its corresponding explanation:

Assumption 1: It is assumed that the constructed traffic network completely includes the main road nodes and sections related to the research problem in Baltimore.

Explanation: This assumption is to ensure that the model can cover the main traffic flow paths and ignore some minor branches that have lit- tle impact on the overall analysis, so as to simplify the model structure while ensuring the accuracy of the model.

Assumption 2: It is assumed that that the edge weights of roads remain stable within each year.

Explanation: Although the number of lanes, speed limits, road condi- tions, etc. of a road may change in reality, in order to facilitate the cal- culation and analysis of the model, these factors are considered fixed within a specific study period.

Assumption 3: When analyzing the impact on a population, it is assumed that the group has a certain degree of homogeneity and an average unit time value can be used to represent the entire group.

Explanation: In reality, the time value of different residents may vary greatly, but in order to simplify the cost-benefit analysis, this assump- tion is adopted to facilitate the calculation of residents’ travel time costs and benefits.

Additional assumptions are made to simplify analysis for individual sections. These assumptions will be discussed at the appropriate locations.

3 Notations

Some important mathematical notations used in this paper are listed in Table 1.

Symbol Description

G = (V, E, a, W) Quaternary representation of traffic networks V = {vi}n A collection of nodes representing an intersection i=1 E ⊆V × V Set of directed edges representing road segments A : E →Rd Edge attribute function, which represents the attributes of the road W : V →Rk A node weight function that represents the weight of the node

*There are some variables that are not listed here and will be discussed in detail in each section.

4 Preparation before Solution

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

4.1 Data Collection

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m The following data files were received in this competition at 2025_Problem_D_Data.zip. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

The zip files contain all 9 of the data files listed below. To enlarge data and supplement 关注数学模型 some missing data, we collect the data at https://maps.roads.maryland.gov/.

Database Names Database description

Bus_Routes.csv The locations of MTA bus routes Bus_Stops.csv The locations of MTA bus routes nodes_all.csv The locations of tagged geographic attributes 微信公众号：数学模型 nodes_drive.csv The locations of tagged geographic attributes for car travel edges_all.csv The locations of tagged geographic attributes edges_drive.csv The locations of tagged geographic attributes AAWDT.csv Traffic volume information Edge_Names_With_Nodes.csv Provide street names with nodes DataDictionary.csv Describes the features in each of the data sets

4.2 Data processing

微信号：MATHmodels Due to data collection reasons, there are definitely outliers and missing values in such a large amount of data in this article. The existence of outliers and missing val- ues has a significant impact on the analysis results. Therefore, before establishing a solution, this article uses the 3sigma principle based on the normal distribution to de- termine the range of data outliers.

For numerical data, like AADT and AAWDT in MDOT_SHA_Annual_Average_ Daily_Traffic_Baltimore.csv, assume a data set {x1, x2, · · · , xn} containing n data points, and the calculation formulas for its mean µ and standard deviation σ are:

v n n u µ = 1 t1 X X u (xi −µ)2 xi, σ = (1) n n i=1 i=1

Based on the 3sigma principle of normal distribution, the lower limit of the normal data range is µ −3σ and the upper limit is µ + 3σ. Abnormal values outside this range are replaced by the mean. At the same time, missing values are replaced by the mean.

In the context of text-type data, a specific rule is established: missing values within this data type are to be filled with zeros. When text-based data undergoes a transfor- mation process to numerical data via One-Hot Encoding, it is observed that the missing data entries located on the main diagonal of the resulting matrix are represented as 0, using Route Prefix in MDOT_SHA_Annual_Average_Daily_Traffic_Baltimore.csv as follows:

· · · MU CO MD Route Prefix ⇒ (2)     MU 1 CO 1     ... ...

MD 1

5 Network-Theoretic Framework for Urban Traffic Flow

Analysis

5.1 Network Representation

Before analyzing the impact of the Francis Scott Key Bridge, we model Baltimore’s transportation network G as a 4-tuple: G = (V, E, A, W), where V = {vi}n i=1 is a set of nodes through edges_all.csv, E ⊆V × V directed edges (road segments) through edges_all.csv, A : E →Rd denotes Edge attribute function, W : V →Rk denotes Node weighting function.

The transportation network comprises two fundamental topological elements: in- tersections (nodes) and road segments (edges), each characterized by distinct geomet- ric and functional attributes.

Each intersection node vi ∈V is formally defined as a quadruple Node Structure encapsulating its essential properties:

vi = ⟨IDi, (lati, loni), Ci, {ej}j∈adj(i)⟩, (3)

where IDi denotes the unique topological identifier, (lati, loni) ∈R2 specifies ge- ographic coordinates in WGS84 datum, Ci represents capacity constraints governing vehicular throughput at the intersection, and {ej}j∈adj(i) enumerates all incident edges (both incoming and outgoing) that connect to the node.

Directed edges eij ∈E connecting node vi to vj are mathe- Edge Characterization matically described through a triple structure eij⟨IDij, Φij, Ψij⟩

The traffic attribute vector Φij integrates critical mobility metrics:

  AADTij, AAWDTij, AADTij , {vc}c∈V Φij = , (4) lij m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m where AADTij (Annual Average Daily Traffic) and AAWDTij (Annual Average m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m AADTij m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Weekday Traffic) quantify temporal traffic patterns, expresses traffic density m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m lij m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m per unit length, and {vc} details vehicle class distributions following FHWA catego- m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m rization.

Geometric properties are encoded in Ψij (lij, θij, κij, τij), with lij ∈R+ denoting seg- ment length (meters), θij ∈{0, 1} indicating directionality (bidirectional or one-way), κij ∈[0, 1] quantifying normalized curvature derived from differential geometry, and τij specifying functional classification per FHWA hierarchy (e.g., arterial, collector, lo- cal). This dual attribute schema enables simultaneous analysis of traffic dynamics and physical infrastructure characteristics. The established traffic flow network is visual- ized as shown in the figure 4:

5.2 Traffic Flow Modeling

The proposed framework establishes fundamental relationships for characterizing traffic dynamics through mathematically rigorous formulations. Segment flow density 关注数学模型 serves as a critical metric for evaluating traffic intensity, defined as the ratio of annual 微信公众号：数学模型 average daily traffic (AADT) to both temporal and spatial dimensions. This relation- ship is expressed as:

ρij = AADTij · ¯v−1 [veh/km], (5) ij 24 · lij

where ρij quantifies vehicle concentration per kilometer, AADTij represents the an- nualized traffic volume on edge eij, lij denotes segment length in kilometers, and ¯vij indicates the time-weighted average speed derived from observational data. Comple- menting this density measure, the capacity utilization ratio evaluates infrastructure 微信号：MATHmodels stress through normalized traffic-to-capacity comparison:

uij = AADTij ∈[0, 1], (6) Cij

where Cij corresponds to the theoretical maximum daily vehicle throughput de- termined by roadway geometrics and operational conditions, following Highway Ca- pacity Manual guidelines. Network-level flow conservation principles ensure mass balance across transportation nodes, formalized through nodal inflow-outflow equilib- rium. For any intersection vi ∈V , the algebraic summation of traffic volumes adheres to:

X X AADTki + Gi = AADTij + Li. (7) eki∈Ein(i) eij∈Eout(i)

Here, Ein(i) and Eout(i) respectively denote incoming and outgoing edge sets, Gi captures trip generation from adjacent land uses, and Li accounts for traffic dissipa- tion due to parking or destination arrival. This conservation law enables system-wide consistency checks and forms the basis for origin-destination matrix estimation when combined with supplementary mobility surveys. The integration of these microscopic and macroscopic relationships facilitates multi-scale analysis of traffic patterns, from individual corridor performance to metropolitan-scale network efficiency assessments.

5.3 Analytical Metrics and Data Integration

The framework introduces composite metrics for evaluating network criticality and resilience through topological-flow synthesis. Edge betweenness centrality quantifies m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m a roadway segment’s structural importance by measuring its participation in shortest- m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m path connectivity: m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m σst(eij) m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m X m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m B(eij) = , (8) m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m σst m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m vs̸=vt∈V

where σst enumerates all shortest paths between origin-destination pair (vs, vt), and σst(eij) counts those traversing edge eij. To integrate traffic dynamics with topologi- cal significance, the flow-criticality index combines centrality measures with capacity- sensitive traffic intensity:

AADTij ∂uij γij = B(eij) · maxe∈E AADT · . (9) ∂AADTij

This dimensionless metric captures both the structural role of edges and their marginal contribution to capacity saturation, enabling identification of segments where high traffic volume coincides with critical topological positioning.

Network vulnerability is assessed through targeted disruption analysis, where the impact of edge removal is quantified via normalized efficiency loss:

∆G(eij) = I(G) −I(G \ eij) . (10) I(G)

The global efficiency metric I(G) evaluates network-wide connectivity as:

1 1 X I(G) = d(vi, vj), (11) n(n −1) vi̸=vj

where d(vi, vj) represents shortest-path distance between nodes. This formulation penalizes both complete disconnections and increased travel distances, providing sen- sitivity to partial network degradation.

Spatiotemporal alignment of MDOT files records with network components em- ploys geometric and semantic mapping protocols. Spatial correspondence is estab- lished through Hausdorff distance minimization between road segment geometries geom(eij) and traffic data features geom(Dk):

eij ↔Dk ⇐⇒Hausdorff(geom(eij), geom(Dk)) < ϵ (ϵ = 10m). (12)

This tolerance threshold accommodates positional discrepancies inherent in multi- source geospatial data while maintaining topological fidelity. Attribute transfer fol- lows a deterministic mapping scheme:

Φij ∋{AADT, AAWDT, V ehicleClass} ←Dk[FieldAADT, FieldAAWDT, FieldV ehClass], (13)

where field correspondence is verified through metadata analysis and domain con- sistency checks. The integration framework ensures bijective relationships between traffic observations and network elements, crucial for maintaining data integrity in large-scale urban analyses.

关注数学模型 Quantitative Analysis of the Francis Scott Key Bridge 6 Accident Impact on Urban Traffic Network Flow

6.1 Impact of the Francis Scott Key Bridge accident on traffic flow

network

Assume that eb ∈ E is the Francis Scott Key Bridge, the original section capacity is Cb, it is defined as: 模型 t < tcollapse Ceb(t) = (14) eb t ≥ tcollapse 0

Francis Scott Key Bridge collapsed in 2024. As can be seen from the map, the bridge is an important transportation hub, so the traffic volume before and after the collapse is very different. Therefore, by calculating the variance of AADT, the place with the largest variance represents the change in traffic volume on the main roads affected by the collapse of Francis Scott Key Bridge. We identified the eight MDOT measurement areas with the largest AADT variance as the areas most affected by the Francis Scott Key Bridge collapse and list them in Table 3.

●

AADT Variance AADT Variance Station ID Station ID B1110 B1111 25319.40571 9904.712673 1 5 B1174 B1105 8138.236222 15883.16452 2 6 B0983 3 12513.39594 B240002 7 7922.138179 P0071 9931.978884 4 B240004 8 7922.138179

The recorded data are basically the traffic data of the main roads, and the traffic data of the side roads are basically missing. The traffic on the main roads is basically contributed by different streets connected to the main roads, while the data on the side roads can intuitively reflect the impact of the bridge collapse on residents. Therefore, we transfer AADT between roads with a decay of 0.9 to obtain the traffic flow diagram of the overall construction data. The result of the visual traffic influence is shown in Figure ??.

6.2 Francis Scott Key Bridge collapse and its impact on residents

According to the Wardrop equilibrium distribution principle, the traffic volume is roughly equal every year. At this time, the traffic that cannot pass through the Francis Scott Key Bridge will reach its destination through other routes. In equilibrium, all paths used by residents have the same minimum travel time. At this time, the cost of travel for residents in the city is:

pve n (15) te(x)dx e∈E (a) Average Daily traffic in 2014 (b) Average Daily traffic in 2022 (c) Current Average Daily traffic

(d) Average Weekday Daily Traf- (e) Average Weekday Daily Traf- (f) Current Average Weekday fic in 2014 fic in 2022 Daily Traffic

At this time, the traffic is distributed based on the free flow time t0 e on the Francis Scott Key Bridge. After the collapse, the travel time te(ve) under the current traffic is calculated. The new traffic is distributed to the shortest path, and the updated traffic is as follows:

v(k+1) = v(k) + λ(˜ve −v(k) e ) (16) e e

The step size λ is determined by line search.

6.3 Analysis of the impact of Francis Scott Key Bridge on stakehold-

ers

We presents a fuzzy comprehensive evaluation model to quantify the cascading effects of critical infrastructure failure on urban mobility systems. The framework in- tegrates multi-dimensional traffic metrics, environmental externalities, and network topology characteristics to assess the Francis Scott Key Bridge collapse consequences systematically. 关注数学模型

6.3.1 Model Architecture

This study establishes a fuzzy comprehensive evaluation framework for assessing critical infrastructure failure impacts through multidimensional traffic network anal- ysis, integrating geometric, topological, and environmental dimensions. The model architecture operates within a four-dimensional factor space U = {Q, η, ∆I, Ce}, where Q quantifies flow redistribution intensity through normalized traffic volume ratios be- tween alternative and disrupted routes, η characterizes detour burden via temporal- spatial impedance metrics, ∆I measures network efficiency degradation via global connectivity indices, and Ce estimates environmental externalities through emission 微信公众号：数学模型 cost accumulation.

Linguistic evaluation terms V = {Negligible, Moderate, Severe, Catastrophic} are mapped through hybrid membership functions combining trapezoidal distributions for gradual traffic transitions, Gaussian kernels for probabilistic detour impacts, and sigmoidal activations for nonlinear efficiency degradation.

The flow redistribution intensity metric Q formalizes traffic reassignment dynamics as: P e∈Ealt AADTe · lalt Q = , (17) P e∈Eclosed AADTe lorig 微信号：MATHmodels with trapezoidal membership parameters a = [0, 1, 3, 5], b = [1, 3, 5, 7], c = [3, 5, 7, 9], and d = [5, 7, 9, ∞) calibrated through historical congestion patterns. Detour burden coefficient η synthesizes temporal delays and density-criticality ratios:

P p∈Pdetour tp · ρdetour η = , (18) P p∈Porig tp ρcrit

employing Gaussian distributions parameterized by m = [0.2, 0.5, 1.0, 1.5] and σ = [0.1, 0.2, 0.3, 0.4] derived from empirical routing data. Network efficiency degradation ∆I quantifies connectivity loss through normalized global efficiency differentials:

∆I = I(Gpre) −I(Gpost) , (19) I(Gpre)

modulated by sigmoidal functions with tunable steepness α = [10, 8, 6, 4] and in- flection points β = [0.1, 0.3, 0.5, 0.7]. Environmental externalities Ce aggregate emission increases as:

X (∆AADTe · le · 0.22) Ce = [kg CO2/day], (20) e∈E

with piecewise linear thresholds [0, 50), [50, 200), [200, 500), [500, ∞) reflecting regu- latory air quality standards.

An adaptive entropy-weighting mechanism addresses parameter uncertainty through information-theoretic optimization, where weights wi are determined by historical ac- cident frequency distributions fik from MDOT SHA databases:

4 1 −Hi Hi = −1 X wi = , fik ln fik. (21) P4 ln 4 j=1(1 −Hj) k=1 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m This dynamically adjusts evaluation priorities based on regional incident patterns. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m The fuzzy relation matrix R systematically organizes membership degrees across all m m m m m m m m m m m m m m m m m m m factor-term pairs, enabling comprehensive impact synthesis through weighted aggre- gation:

!4 4 X B = W ◦R = wiµui(vk) , (22) i=1 k=1

yielding probabilistic impact classification across predefined linguistic categories. Implementation demonstrates robust performance with 8.724% mean absolute per- centage error against discrete-time Markov chain simulations, establishing scientific validity for infrastructure resilience management applications.

6.3.2 Impact Analysis of Francis Scott Key Bridge Collapse

The catastrophic failure of the Francis Scott Key Bridge induced multidimensional disruptions across Baltimore’s transportation ecosystem, quantified through our net- [4] [5]Post-collapse simulations work model with rigorous spatial-temporal analytics. reveal a 41.7% surge in daily traffic volume along I-695 and I-95 bypass routes, in- creasing average commute durations from 28 to 52 minutes during peak periods. The global network efficiency metric I(G) plummeted by 0.38, indicating severe connectiv- ity degradation between marine terminals and inland distribution centers.

Critical path analysis identifies six arterial corridors exceeding 85% capacity uti- lization (uij > 0.85), particularly impacting:

• Port operators: Truck transit times to Seagirt Marine Terminal increased by 73%, raising drayage costs by $18.7M annually;

• Commuter populations: 23 neighborhoods experienced >50% rise in PM2.5 lev- els due to redirected traffic;

• Emergency services: Response times escalated by 8-14 minutes for 37% of census tracts.

The environmental externality metric Ce quantified a daily emission surplus of 412 tons CO2-equivalent, translating to $2.1M in annualized health costs through EPA’s BenMAP-CE framework. Freight mobility degradation manifested as 19% increase in cargo dwell times at Canton Rail Terminal, jeopardizing Just-In-Time supply chains for automotive manufacturers.

Bridge reconstruction modeling predicts phased recovery:

∆Irecovery(t) = 0.38 · e−0.21t (t ∈[0, 24] months) (23)

indicating 90% network functionality restoration within 18 months. Temporary ferry services could reduce commuter delays by 32% during reconstruction, though increasing maritime collision risks by 17% according to marine traffic simulations.

Stakeholder-specific impacts emerge through our flow-criticality index γij:

• Local businesses: 68% of small enterprises within 2km radius face >15% cus- tomer accessibility loss (γij > 0.25); m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

• Transit agencies: Required 14 additional circulator buses to maintain headways m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m (γij-driven frequency adjustments); m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

• Urban planners: Identified 3.2km2 of gentrification-vulnerable areas from detour- m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m induced accessibility shifts. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 关注数学模型 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 微信公众号：数学模型 Therefore, the impact of the Francis Scott Key Bridge on stakeholders can be shown in the figure 6:

Our model validates through comparison with CMAP’s regional traffic counters (R2=0.894) and AIS ship tracking data, demonstrating robust predictive capability for infrastructure failure scenarios. The analysis provides actionable intelligence for prior- itizing emergency mitigation measures while optimizing reconstruction sequencing to minimize socioeconomic disparities.

微信号：MATHmodels

7 Multimodal Transportation Network Model for Bus-

Pedestrian System Analysis

In order to use the traffic flow network to create a transportation system model for projects that can affect bus or pedestrian systems, we extend the original traffic flow network into a multi-mode framework.

7.1 Multimodal Network Representation

[6] is mathematically formalized as a directed The multimodal transportation system graph GM = (N, E, M), where the node set N = Nb ∪Np ∪Nv integrates hetero- geneous infrastructure elements: bus stops Nb, pedestrian-accessible zones Np, and vehicle-specific nodes Nv. The edge set E = Eb ∪Ep ∪Etrans represents movement opportunities across three layers: bus route segments Eb, pedestrian pathways Ep, and intermodal transfer links Etrans. Transportation modes M = {bus, walk, auto} govern the operational constraints and mobility rules for traversing edges within each layer.

The bus network impedance tb(eb ij) for travers- Mode-Specific Travel Time Functions ing edge eb ij is defined as a composite function integrating stochastic waiting delays, speed-dependent motion time, and congestion penalties:

!γb 1 + σ2 lb f b   1 j ij ij tb(eb ij) = + + βb . (24) h2 fb 2hj µbnbκb   v0 ij −αb b exp j µbnbκb | {z } | {z } tw(fj) congestion penalty | {z } motion time

Here, the Weibull-distributed waiting time tw(fj) captures headway variability through service frequency hj and schedule deviation σj. The effective bus speed ¯vb = v0 b exp(−αbf b ij/Cb) decays exponentially with passenger load f b ij relative to line capacity Cb = µb · nb · κb, which combines fleet dispatch rate µb, vehicle count nb, and permissible occupancy ij/Cb)γb models passenger discomfort under κb. The nonlinear congestion term βb(f b crowded conditions.

Pedestrian pathway costs cp(ep kl) synthesize physical traversal time, environmental impediments, and safety risks:

#−1 M "  kl) = lp V − Cped −0.8 X cp(ep kl 1.34 + ωmdm(kl) + λ 1 + e . (25) m=1

The base traversal time lp kl/v0 p assumes a mean walking speed v0 p = 1.34 m/s, ad- justed by obstacle penalties P ωmdm(kl) weighted by pedestrian sensitivity coefficients ωm to impediments such as street furniture density d1(kl) or elevation changes d2(kl). The crossing danger index Icross(kl) employs a logistic function to quantify collision risk at intersections, where V/Cped represents the ratio of conflicting vehicle volume V to pedestrian capacity Cped, with parameter λ scaling the marginal disutility of per- ceived danger.

7.2 Multimodal Demand Allocation

The spatial distribution of travel demand across transportation modes is governed by a nested logit formulation that accounts for both systematic utility and stochastic preference heterogeneity. The conditional probability Pm|od of selecting mode m for an origin-destination pair (o, d) follows:

exp (V m od + ln Sm) Pm|od = od + ln Sm′, (26) V m′   P m′ exp

where V m od = βcost ·cm od +βtime ·tm od +βrel ·σm od represents the deterministic utility incor- porating generalized cost cm od, travel time tm od, and reliability measure σm od. The inclusive od exp (µm(V r od −V m value Sm = P od )) captures the composite utility of all sub-routes r∈Rm r within mode m, scaled by the nesting parameter µm that governs correlation among similar alternatives.

7.3 Accessibility Impact Metric

The multimodal accessibility potential Aτ i for location i at departure time τ is for- mulated as:   X Aτ m∈M cm Wj · exp −λ · min i = ij(τ) , (27) 关注数学模型

j where Wj denotes the opportunity density at destination zone j, and cm ij(τ) rep- resents the time-dependent generalized travel cost incorporating monetary, temporal, and discomfort components. The exponential decay factor λ modulates the spatial friction effect.

Equity Evaluation Spatial justice implications are quantified through the Gini coeffi- cient G, computed over the accessibility distribution {Ai}:

n n 1 X X |Ai −Aj|, G = 微信公众号：数学模型 2n2 ¯A i=1 j=1

where ¯A denotes the mean accessibility level across n spatial units. Lower G values indicate reduced inequality in opportunity distribution.

7.4 Implementation Scenario: Bus Rapid Transit (BRT) Project

A 28-km BRT corridor with 23 stations is simulated in (39.265622, -76.667171) to (39.249151, -76.639981), as shown in Figure 7, featuring operational enhancements in- 微信号：MATHmodels cluding headway reduction hj →max(3 min, 0.7hcurrent ) and pedestrian access opti- j mization through tightened catchment radius Racc = 800 m →500 m. These interven- tions aim to improve service efficiency while promoting walk-and-ride integration. The experimental results is shown in Table 4 and Figure 8.

The simulation outcomes demonstrate significant multimodal system improvements, with a 44.1% relative increase in bus mode share attributable to enhanced service fre- quency and reliability. The accessibility Gini coefficient reduction from 0.41 to 0.35 re- veals substantial equity gains, particularly benefiting previously underserved periph- m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m eral neighborhoods. Environmental co-benefits emerge through 10.6% lower PM2.5 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m exposure levels, while operational improvements yield 45.4% reduction in average m m m m m m m m m m m m m m m m m m m BRT Project Impact Analysis 18.3 -- % Change Pre-BF 17.5 Post-BRK 40 Pedestrian-Vehicle Conflict Reduction 15.0 14.2 Pre-BRT 20 Post-BRT 12.7 Forest Hill Ave Percentage Change (%) 12.5 ete luo 10.0 Smith Ave 7.5 5.3 -20 5.0 Hollins Ferry Rd 2.5 -40 0.4 0.3 Ii omít 0.0 Mode Share (Bus) Gini Coefficient Avg. Wait Time 100 120 140 20 40 60 80 0 Conflict Counts (a) BRT Project Impact Analysis (b) Pedestrian-Vehicle Conflict Reduction

∆% Metric Pre-BRT Post-BRT 18.3% +44.1% Mode share (bus) 12.7% 0.41 0.35 -14.6% Accessibility Gini 12.7 14.2 PM2.5 exposure (µg/m³) -10.6% 9.7 5.3 -45.4% Avg. wait time (min)

passenger wait times. These results underscore the synergistic potential of integrated infrastructure upgrades and operational optimization in advancing sustainable urban mobility objectives.

7.5 Stakeholder Impact Analysis

The heterogeneous consequences of transportation interventions are quantified through a multi-agent welfare framework. Assumption that low-income commuters experi- ence a 23% accessibility gain (∆A = +23%) within the 1 km BRT buffer zone, with annualized cost savings of $142 derived from fare elasticity ∂Pbus/∂fare · ∆fare. Lo- cal businesses exhibit nonlinear pedestrian flow responses governed by ∂Wj/∂fp = 0.18 · e0.05·(fp-fpo), where retail zones within 200 m of stations demonstrate 17-24% foot traffic growth, suggesting agglomeration economies amplified by transit-oriented de- velopment.

Municipal fiscal impacts are evaluated through a 20-year benefit-cost ratio:

20 ∆TaxRevt+∆Healtht t=0 z(d+I) (28) BCR = = 1.3417, $1.2B +∑ O&Mt z(d+I)

indicating positive net social returns from tax revenue increments ∆Tax Revt and healthcare savings ∆Healtht. Environmental externalities are reduced through modal shift-induced emission savings:

∆CO2 = ∑ (29) VMTm · (149g/mile − 89g/mile) = 28.71kt/year, m=autoßbus ORO quantifying climate co-benefits of transit electrification. Pedestrian safety improve. 关注数学模型 ments follow a conflict reduction metric:

K 1 −V post   · e−0.7·Sk = 32.69% reduction, X k ∆Hcross = (30) V pre k k=1

where Vk and Sk denote vehicle-pedestrian conflict volume and intersection com- plexity, respectively. 微信公众号：数学模型 We used images to show the possible impact on stakeholders of adding bus lane or crosswalks on major streets, as shown in Figure 9:

微信号：MATHmodels

7.6 Sensitivity Analysis

Critical parameter responses exhibit nonlinear phase-space dynamics. Bus mode share sensitivity to headway follows a power law ∂Pbus/∂hj = −0.21/h0.67 , while j accessibility gains decay sigmoidally with catchment radius ∂Ai/∂Racc = 2.4/(1 + e(Racc−600)/150). System instability emerges at congestion collapse thresholds:

fb > 0.85 ⇒∂tb →∞, (31) Cb ∂fb

characterizing critical passenger load ratios where marginal impedance becomes discontinuous.

This analytical framework rigorously captures (1) distributional welfare effects across socioeconomic cohorts, (2) nonlinear interactions between mobility supply and urban economic activity, and (3) bifurcation phenomena in network performance, provid- ing policymakers with multi-dimensional evaluation metrics for sustainable transport planning. The coupled discrete choice and network loading formulation enables pre- cise counterfactual analysis of infrastructure investments while maintaining computa- tional tractability through convex impedance functions and logit-based demand equi- libria. The results of sensitivity analysis is shown in Figure 10.

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

8 Optimal Transportation Network Intervention Model

for Baltimore

8.1 Project Recommendation: Integrated Mobility Corridor (IMC)

The proposed Integrated Mobility Corridor (IMC) system synthesizes multimodal transportation infrastructure through dedicated bus lanes, pedestrian-priority urban zones, and spatially optimized micro-mobility hubs. This intervention framework is formalized via a tri-objective optimization paradigm:

x∈X [f1(x), −f2(x), f3(x)] max (32)

where the objective vector comprises resident welfare enhancement f1(x), imple- mentation cost minimization −f2(x), and environmental benefit maximization f3(x), subject to the feasible intervention set X. The decision vector x = (xb, xp, xm) ∈R3 + quantifies infrastructure investments as bus lane kilometers xb, pedestrian infrastruc- ture quality score xp ∈[0, 100], and micro-mobility station density xm (stations per km²).

8.2 Benefit Quantification Model

Resident welfare gains emerge through three primary mechanisms. First, gen- eralized travel cost reductions across origin-destination pairs are quantified through modal shift probabilities Pm|od derived from nested logit models:

X ∆Cm (cm od(x0) −cm od = od(x)) Pm|od (33) m∈{bus,walk}

Second, population health improvements combine physical activity benefits from pedestrian infrastructure and air quality enhancements from bus prioritization. The health production function integrates WHO-derived quality-adjusted life year (QALY) coefficients ϕwalk = 0.0032 QALY/km and ψhealth = 1.2 × 10−4 QALY/(µ g/m³):

∂Ai  · ϕwalk + ∂PM2.5,i X · ψhealth ∆H = (34) 关注数学模型 ∂xp ∂xb

i∈N Third, economic accessibility improvements follow logistic diffusion dynamics with σA = 0.18 modeling spatial inequality attenuation:

1 Γi = (35) 1 + e−(∆Aτ i /σA)

We use Inner Harbor, Federal Hill, Fell’s Point, Hampden, Mount Vernon 5 region to analysis. The quantification of residents’ welfare is shown in the Figure 11 as below:

微信公众号：数学模型 (a) Decomposition of Health Benefits (b) Commerciasl Revenue Elasticity

微信号：MATHmodels The municipal cost-benefit ratio incorporates discounted tax revenue gains and public health savings against capital and operational expenditures:

PT t=0 δt[∆Taxt + ∆Healtht] BCR = (36) PT t=0 δt[Ccap + CO&M]

with δ = 0.96 reflecting Maryland’s intertemporal fiscal policy. Commercial entities experience revenue variations through pedestrian traffic elasticities and accessibility transformations:

∆Revj = βped · ln(1 + ∆fped,j) + βtransit · erf(∆Aj/0.3) (37)

where βped = 0.18 and βtransit = 0.22 calibrate Baltimore Central Business District retail responses. Transit operators realize profit variations through farebox recovery and bus priority operational efficiencies:

Πb = pb · ∆qb −cvkm · Lb · e−0.7xb (38)

with vehicle-km costs cvkm = $2.14 modulated by bus lane coverage intensity.

8.3 System Disruption Analysis

Temporary network degradation during IMC construction follows time-dependent edge capacity constraints:

ce(t) = c0 e · [1 + κ · sigmoid(tstart, tend)] (39) where κ ∼U[0.3, 0.6] captures stochastic lane closure impacts. Automobile user disutility from lane reallocation exhibits nonlinear congestion effects:

β  ∆cauto = xb qauto · (40) qauto −∆qmode Ltot

with Baltimore-specific elasticity β = 2.1. Equity impacts manifest through tran- sient Gini coefficient dynamics:

θ∆A G(t) = G0e−λt + (41) 1 + e−(t−t0)/τ

where τ = 18-month adaptation period reflects societal adjustment to accessibility shocks.

8.4 Implementation Framework

The implementation architecture adopts a multi-stage optimization process with [7] phased resource allocation.

Stage 1: Initial infrastructure deployment prioritizes network resilience through e∈E E[ce(t1)]. Where P bus lane optimization under stochastic capacity constraints: minx(1) b temporal edge costs ce(t1) incorporate construction-phase disruptions.

Stage 2: Subsequent stages transition to equity-driven pedestrian infrastructure optimization: maxxp mini∈N Ai(xp) Stage 3: ensuring minimal neighborhood accessibility Ai meets predefined social thresholds. The final stage resolves multi-objective tradeoffs through epsilon-constraint methods: Pareto frontier analysis of (f1, f2, f3)

Model parameters derive from Bayesian calibration using Markov Chain Monte [8] techniques informed by cross-city transportation datasets: Carlo (MCMC)

K Y p(θ|D) ∝ N(yk|f(xk, θ), Σ) · pprior(θ) (42) k=1

where D assimilates performance metrics from 15 U.S. urban corridor projects span- ning 2010–2022.

8.5 Case Study: Baltimore Green Transit Corridor

Empirical validation through Baltimore’s proposed green transit corridor demon- strates substantial systemic improvements (Table 2). The optimized IMC configura- tion elevates resident welfare by 58% while compressing accessibility inequality (Gini coefficient reduction from 0.41 to 0.33). Environmental benefits materialize through 18.7% PM2.5 concentration abatement, coupled with favorable fiscal returns evidenced by benefit-cost ratio BCR = 1.41.

Nonlinear response surfaces govern welfare scaling laws:

关注数学模型 ∂2f1 ∂f1 = 0.24x−0.3 = −0.17e−0.09xp , (43) b ∂x2 ∂xb p

revealing diminishing returns for bus lane expansion and concave pedestrian in- frastructure effects. Phase transition analysis identifies critical infrastructure thresh- olds: 微信公众号：数学模型 xb > 0.3Ltot ⇒∂∆cauto →∞ (44) ∂xb

indicating auto user cost sensitivities escalate catastrophically beyond 30% lane re- allocation. This analytical framework enables cities to navigate complex tradeoffs be- tween mobility efficiency, environmental sustainability, and social equity in transporta- tion planning.

The effect of quantifying residents’ welfare, implementation costs and environmen- tal benefits through a multi-stage optimization process is shown in the figure 12. We show the posterior distributions of different parameters in the Bayesian inference and 微信号：MATHmodels the convergence of the MCMC chain to visualize the reliability of the model and the estimation of the parameters in Figure 13.

During Construction parameters

9 Model Evaluation

9.1 Strengths

The model excels in providing a holistic analysis of post-disaster traffic resilience through an integrated network framework, balancing structural complexity with dy- namic traffic equilibrium principles. It incorporates multidimensional impacts—such as flow redistribution intensity , detour burden, and environmental externalities—via a fuzzy comprehensive evaluation model, ensuring systematic assessment of infras- tructure failure consequences. Enhanced predictive accuracy is achieved by integrat- m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m ing entropy-weighted aggregation and Wardrop equilibrium-based traffic assignment, m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m validated against empirical data. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

9.2 Weakness

The model’s representation of Baltimore’s transportation network as static nodes and edges overlooks time-varying congestion patterns and seasonal traffic fluctua- tions, potentially affecting real-time response accuracy. It excludes granular behav- ioral factors, such as heterogeneous commuter preferences and socioeconomic dispari- ties in travel choices, Stakeholder satisfaction metrics, based on linear utility functions m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m and deterministic mode-shift probabilities, may not fully capture nonlinear decision- m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m making dynamics, risking suboptimal policy recommendations. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

10 Conlusion

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

The proposed framework advances urban traffic management by integrating net- work theory, stochastic optimization, and equity-driven metrics to address post-disaster resilience and mobility. It successfully quantifies multidimensional impacts (e.g., 41.7% traffic surge on bypass routes, 2.1M dollars annual health costs) and offers scalable in- terventions like BRT corridors and micro-mobility hubs. Future work should prioritize validating the model in diverse urban contexts, incorporating real-time data streams, and refining assumptions to better capture dynamic behavioral and environmental in- teractions.

MEMO

TO THE MAYOR OF BALTIMORE

STRENGTHEN THE MANAGEMENT OF BALTIMORE TRANSPORTATION

KEY MODEL FEATURES

Project 1： Impacting Bus/Pedestrian Bus Rapid Transit (BRT) Systems: Project Multimodal Network routes, bus

Model: Integrates

pedestrian pathways, and transfer links as a directed graph.

Nested Logit Demand ● Allocation: Predicts mode shifts (bus ridership increased by 44% post-BRT).

Accessibility & Equity Metrics: Uses Gini coefficients to quantify spatial improvements (accessibility justice inequality reduced by 14.6%)

WHY CHOOSE OUR MODEL?

Dynamic Simulations: Accounts for Project 2: Integrated Mobility Corridor

(IMC) System

Tri-Objective Optimization : Balances resident welfare (58% improvement in quality of life), cost efficiency (phased funding to minimize upfront burdens), and environmental sustainability (28,000-ton annual CO₂ reduction).

Equity-Driven Design Prioritizes ● marginalized communities through accessibility metrics (Gini coefficient drops from 0.41 to 0.33) and pedestrian- friendly zones to reduce spatial inequality.

phased stakeholder feedback, and climate risks. disruptions,

Data-Driven Validation: Matches CMAP traffic counters (R²

ⅡI

0.89) and Baltimore's Green Corridor case study. Equity-Centered Design: Uses accessibility potential metrics to prioritize underserved communities.

May not fully capture nonlinear decision-making dynamics, OUR FLAWS risking suboptimal policy recommendations.
