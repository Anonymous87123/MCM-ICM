Summary

The collapse of the Francis Scott Key Bridge in 2024 cut off a vital route to the port, posing an unprecedented challenge to Baltimore’s transportation system and bringing the optimization of traffic network back into the public view. This paper analyzes the city transportation system based on a multi-layered road network model and proposes several improvement strategies.

Before assessing the traffic conditions in Baltimore, we conduct data preprocessing. Firstly, we use uniqueness of osmid to complete 354,420 missing road names. Subsequently, roads with three or more osmid records (9,953 entries) between two nodes are treated as outliers and removed. For roads with two osmids, we follow the "road smoothing" principle to determine their proper names. Finally, we uniform different road names.

For task 1, to evaluate the influence of bridge collapse on the urban transport system, we establish an impact assessment model, which analyzes the changes in route choices of commuters and non-commuters based on AADT and AAWDT. Additionally, we construct a subnetwork using critical nodes of the highway network, and compute the proximity centrality of these nodes to reflect their efficiency in network propagation, which can reveal the effect of bridge collapse on the connectivity of surrounding areas. Results indicate that in Baltimore Harbor Tunnel Thurway, the traffic flow of commuters increases by 14%, while non-commuters declines by 25%. The Beltway emerges as a heavily loaded segment for diverse user types.

For task 2, we develop a three-layer bus network model to determine the optimal placement of new bus lines. Firstly we use the entropy-weight-TOPSIS method incorporating both infrastructure levels and passenger volume at bus stops, and utilizes the weighted k-shell decomposition method to classify them into core, bridge, and outer layers accordingly. The designed lines aim to enhance inter-layer connectivity and advance the interests of various stakeholders. Statistics demonstrate that the composition of core-bridge edges increases by 18.3% and that of outer layer decreases by 82.9%.

For task 3, we raise a project of adding an Orange Line rail transit to meet the growing demand of residents. The line connecting Penn Station, parks, and large markets, facilitates transfers to the airport and offers benefits to various stakeholders. The total travel time from the farthest station, White Marsh, to the airport is compressed to approximately 65 minutes. Lastly, focusing on the influence on bus stops, we construct a double density fitting model. A quadratic function is utilized to depict the relationship between bus stop density and road network density, thus evaluating the contribution of the rail transit. Results showed an increased demand for bus services along the rail line, averaging around 2.31 times.

The proposed multi-layer network model exhibited strong robustness and stability, as confirmed through sensitivity analysis, highlighting its considerable practical utility. The approach we suggest, by synthesizing a range of transportation factors, provides a robust framework for informing the design and implementation of transportation improvements in Baltimore City.

Introduction

3 1

Background

1.1 3 1.2

Restatement of the Problem

3 1.3 Our Work 4

Model Assumptions and Notation

2 4 4 2.1

Assumptions

Notation

2.2 4 Data Preprocessing 5 3 5 3.1 Imputation of Missing Values 3.2 5 Outlier Removal 6 3.3 Handling Cluttered Road Information 3.4 Processing Abbreviation Information 6 7 Multi-layer Transportation Network Model 4

Task 1: Analysis of the Bridge Collapse's Impact 5 8

Impact Assessment Model(IA)

8 5.1 Model Solution and Results . 10 5.2 10 5.2.1 5.2.2 The Impact in Baltimore 11 Task 2: The impact of the project on the bus system 13 6

Three-layer Bus Network Model (TBN)

6.1 13

Model Solution and Results

6.2 15 17 7

Improved Dijkstra Algorithm

17 7.1 Double Density Fitting Model (DDF) . 7.2 17 Model Solution and Results . . 18 7.3 19 Question a: The Benefits to Residents 7.3.1 Question b: The Impact on Other Stakeholders 19 Question c: Disruption to Other Transportation Needs . 20

Sensitivity Analysis

22 8

22

Model Evaluation and Further Discussion

9 Strengths . 22 9.1 ● 9.2

Weaknesses

23

Further Discussion

23 9.3

10 Memorandum

24

1 Introduction

1.1 Background

Baltimore, Maryland faces significant challenges in its aging transportation infrastructure, 微信公众号：数学模型 which affects both residents and businesses. The collapse of the Francis Scott Key Bridge has disrupted major routes across the harbor, causing delays for commuters, freight, and local traffic[1]. With a bustling port and proximity to key highways, the city is critical for both regional and national commerce. However, the city’s infrastructure has long been a barrier to efficient movement, especially with highways and rail systems that divide neighborhoods and hinder access to jobs, schools, and local businesses.

In response, Baltimore aims to improve its transportation network as part of a broader sustainability initiative. This involves enhancing public transit, such as rail and bus systems, and repairing or upgrading key infrastructure. The city seeks to address both the practical challenges of transportation—such as congestion, poor transit coverage, and access to major 微信号：MATHmodels commercial centers—and broader community goals, like reducing environmental impact and improving safety. These efforts also include rethinking how highways and rail systems can be redesigned to reconnect neighborhoods and improve residents’ quality of life.

1.2 Restatement of the Problem

In order to solve those problems, we will proceed as follows:

• Firstly, develop a network model of the city’s transportation system to assess traffic flow and the impact of the Francis Scott Key Bridge collapse.

• Secondly, analyze key transportation issues, including public transit limitations and pedestrian infrastructure, to identify potential improvements.

• Furthermore, evaluate stakeholder impacts, considering the needs of commuters, resi- dents, and businesses.

• Finally, recommend a project that best improves the city’s transportation, balancing benefits, disruptions, and safety. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

1.3 Our Work

2 Model Assumptions and Notation

2.1 Assumptions

To build up our model, we make the following model assumptions.

• All vehicles within a transportation network operate at the maximum speed limit, with varying speeds across different network layers.

• Commuters travel only on weekdays, while the numbers of non-commuters on weekends and weekdays is identical.

• Any two nodes in the graph are connected by a path.

2.2 Notation

Symbols Description

L(u, v) Hierarchical layer of the arc between nodes u and v t(u, v) Travel time on the segment between nodes u and v ks Weighted degree representing the importance of a node

关注数学模型

3 Data Preprocessing

The "edges_all" and "AADT" files play a crucial role in understanding the distribution of city roads in Baltimore and subsequent analyses. Upon examining the datasets, it became 微信公众号：数学模型 evident that they contained significant noise, necessitating a thorough preprocessing process. The data preprocessing workflow is illustrated in Figure 3.

微信号：MATHmodels

3.1 Imputation of Missing Values

In the "edges_all" file, the "name" column is found to contain missing values. Preliminary analysis indicated a one-to-one correspondence between the "osmid" and the road name, allow- ing the missing values in the "name" column to be imputed based on the corresponding "osmid" values. Table 2 provides a sample of osmids and their corresponding road names.

osmid road_name osmid road_name osmid road_name 5250723 Wells Avenue 355848252 Kelly Way 5289021 Bengies Road 5308620 Maxwell Avenue 435579752 Rushley Road 5320737 Loveton Circle

Using the above correspondence, a total of 354,420 missing values in the "name" column are imputed. Other columns, such as "lanes," which has a large number of missing values, are excluded from further analysis, as they do not significantly impact the problem under investigation.

3.2 Outlier Removal

As previously noted, each "osmid" corresponds to a unique road. Therefore, any occurrence of three or more "osmids" between two nodes, indicating the presence of multiple roads, is considered an outlier and removed. Table 3 presents examples of outliers identified in the "osmid" column.Ultimately, 9,953 outliers are removed from the dataset.

u v osmid 89606346 1930984898 [425106099, 425106102, 974337038] 96250866 968161510 [10832171, 10832167, 61424703] 96250866 37412403 [425007969, 425007970, 10832168, 83204409, 83204413]

3.3 Handling Cluttered Road Information

In the "edges_all" file, there are cases where two roads exist for some edges. Since the provided information does not specify the boundary between the two roads, and to facilitate subsequent processing, this section defines such cases as a single road. First, the nodes A and B with this condition are identified. The slope k3 between these two nodes is then calculated. Assuming that the edge contains two roads, R1 and R2, a node A1, directly connected to node A and exclusive to road R1, is identified, and its slope k1 is computed. Similarly, for node B, a point exclusive to road R2 that is directly connected to node B is found, and its slope k2 is calculated. The following relationship is then evaluated:

|k3 −k1| < |k3 −k2| . (1)

If this condition holds, the edge is considered to belong to road R1; otherwise, it is assigned to road R2. A concrete example is illustrated in Figure 4.

As shown in the figure above, after calculating the three slopes, the original road is identified as Ross Avenue. This method ensures that sharp turns are minimized within a single road.

3.4 Processing Abbreviation Information

During the analysis of the "AADT" file, it is observed that the "Road Name" column contains abbreviations that do not match the previously used road names. Upon further investigation, it is found that the road names are abbreviated. To standardize the road names for subsequent analyses, this section converts all abbreviations to their full forms. Table 4 provides a list of common abbreviations and their corresponding full names.

Abbreviation Full Name Abbreviation Full Name Abbreviation Full Name ST STREET AVE AVENUE RD ROAD DR DRIVE TERR TERRACE BLVD BOULEVARD

关注数学模型

4 Multi-layer Transportation Network Model

Baltimore can be abstracted as a multi-layer Arc-Node grid model, which represents the transportation network with a topological structure [2]. The core concept of the Arc-Node model is to approximate real-world road curves with a series of straight line segments [3]. The entire transportation network consists of nodes and arcs, represented as a graph G = (N, A), where N denotes the set of nodes and A represents the arcs. This is formally defined as:

 G = (N, A)   N = {(x, y) | (x, y) ∈Ns} . (2)  A = {(u, v) | u, v ∈N}  微信公众号：数学模型 Here, N represents the set of nodes with coordinates (x, y) in the road network, and A denotes the set of arcs representing road segments between nodes u and v.

Based on the specific characteristics of the city, Baltimore’s road network can be categorized into different types, such as motorways, residential roads, and primary roads. Consequently, the transportation network can be abstracted into a multi-layer structure. Each layer Li corresponds to a subgraph Gi of the graph G. The layers are independent of one another, ensuring the topo- logical connectivity of the network and enabling hierarchical management of the transportation system. This can be represented as:

微信号：MATHmodels  G = G1 ∪G1 ∪G2 ∪· · · ∪Gk   N(Gi) ∈N(G), ∀i ∈k , (3)  A(Gi) ∈A(G), ∀i ∈k  where N(G) and A(G) denote the sets of nodes and arcs in the graph G, respectively.

A diagram of the multi-layer road network model is shown below:

For each arc, various attributes are constructed to provide a comprehensive description of the city’s transportation network system:

• d(u, v) represents the shortest path length between nodes u and v. In multi-layer path planning, it is necessary to compute the shortest path by transferring input nodes to higher-layer networks. If node u starts at a lower layer, its shortest path to the higher-layer network must be searched within a local area [4]. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m • L(u, v) indicates the hierarchy of the arc between nodes u and v, used to differentiate between main roads and secondary roads. Typically, higher-layer roads allow faster traffic flow.

• t(u, v) represents the travel time from node u to node v, calculated as the path length divided by the speed allowed on that layer:

d(u, v) t(u, v) = v(L(u, v)). (4)

• q(u, v) denotes the traffic flow on the road segment between nodes u and v. In traffic flow models, the flow must be conserved along the same path, i.e.,

X X q(v, u), ∀u, v ∈N. q(u, v) = (5) u∈N v∈N

5 Task 1: Analysis of the Bridge Collapse’s Impact

5.1 Impact Assessment Model(IA)

• The Impact in Baltimore

In order to assess the impact of the bridge collapse on stakeholders in Baltimore, we select AADT (Annual Average Daily Traffic) and AAWDT (Annual Average Weekday Traffic) as the evaluation indicators, which effectively describe the traffic conditions in Baltimore. Based on the changes in these two indicators before and after the bridge collapse, we can analyze the impact of the collapse of the Francis Scott Key Bridge.

As one of the oldest towns in the United States, Baltimore’s economy is steadily growing [5]. It is observed that the AADT and AAWDT data for most roads remained relatively stable Therefore, to estimate the AADT and AAWDT on road i at the between 2014 and 2022. beginning of 2024, with the bridge still in place, we calculate the historical averages:

 2022 AADTi,2024 = 1 X  AADTi,y   9    y=2014 . (6) 2022 AAWDTi,2024 = 1  X  AAWDTi,y   9   y=2014

Here, we categorize the stakeholders into commuters and non-commuters [6]. The average number of commuters passing through road i in year y is denoted by Ji,y, and the number of non-commuters is denoted by Ki,y. The AADT and AAWDT for road i in year y can then be expressed as:

AADTi,y = 5 · Ji,y + 7 · Ki,y    7 . (7) AAWDTi,y = 5 · Ji,y + 5 · Ki,y   5

关注数学模型 After simplification the above equations yields the following formulas for commuters and non-commuters:

Ji,y = 1  2 × (7 · AADTi,y −5 · AAWDTi,y)   微信公众号：数学模型 . (8) Ki,y = 7 2 × (AAWDTi,y −AADTi,y)  

Let the impact coefficient for road i be denoted by βi. For each road, we can analyze the impact of the bridge collapse on commuters and non-commuters. The calculation of the impact coefficient is shown in the figure below.

微信号：MATHmodels

The analysis shows that if the impact coefficient βi is greater than 1, the traffic volume on this road segment increases after the bridge collapse. If βi is less than 1, the traffic volume decreases.

• The Impact around Baltimore

To assess the impact of the bridge collapse on cities surrounding Baltimore, we refer to [7], which indicates that the primary sources of impact come from the highways connecting Baltimore to surrounding cities and the highways crossing Baltimore. Based on this reference, we select 39 representative nodes in Baltimore for analysis, as shown in the diagram below.

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m During the node abstraction process, if node 37 is connected to node 39, this represents the situation before the bridge collapse (denoted as Graph G2); if the connection is broken, it represents the situation after the bridge collapse (denoted as Graph G).

By analyzing the Closeness Centrality of G and G2, we can assess the impact of the bridge collapse before and after its occurrence. Closeness Centrality refers to the inverse of the average shortest path length from a node to all other nodes in the network, reflecting the efficiency of propagation within the network. For node v, the Closeness Centrality CC(v) is calculated as follows:

N −1 CC(v) = t d(v, t), (9) P

where d(v, t) is the shortest path length between node v and node t, and N is the total number of nodes in the network.

5.2 Model Solution and Results

5.2.1 The Impact around Baltimore

The impact of the bridge collapse on areas surrounding Baltimore primarily manifests through the highways. Using the model, we can calculate the Closeness Centrality for 39 highway nodes before and after the bridge collapse. The results are shown in the figure below.

It can be observed that nodes 36-38 are most affected by the bridge collapse, corresponding to nodes 37-39 in Figure 7. Specifically, nodes 38 and 39 are located outside of Baltimore, which suggests that the collapse of the bridge indeed impacted the cities surrounding Baltimore, particularly node 39, which has been affected the most.

It is also evident that the Closeness Centrality of nodes 0-26 remains largely unchanged or experiences only minimal variation, suggesting that the impact of the bridge collapse on these nodes is relatively insignificant.

关注数学模型 5.2.2 The Impact in Baltimore

First, we analyze the impact in Baltimore. Based on the established Impact Assessment Model, we can calculate the AADT and AAWDT for different nodes before the bridge collapse in 2024. Using the formulas from equation (8), we can calculate the traffic volume for both commuters and non-commuters on different roads.

We find that traffic volume for non-commuters is generally concentrated in smaller ranges, while the traffic volume for commuters is distributed more evenly between 0 and 10,000.

Next, using the diagram in Figure 6, we can calculate the impact coefficient βi for road ¿. The impact coefficients for commuters and non-commuters are shown in the figure below.

300 400 Commuter Non-commuter 250 350 300 200 Frequency 250 150 200 150 100 100 50 50 0 0.00 0.25 0.50 1.50 1.75 2.00 0.25 0.50 1.50 1.75 2.00 0.00 0.75 1.00 1.25 0.75 1.00 1.25 Influence Coefficient β Influence Coefficient β

● ●

From this figure, it is clear that the impact coefficients for commuters are mostly concentrated around 1, while those for non-commuters are more dispersed, with the majority of impact coefficients being less than 1. This indicates that the collapse of the bridge hindered non- commuters' travel, resulting in a decrease in traffic volume for non-commuters on many roads. For commuter traffic, some roads saw an increase in traffic, while others experienced a decrease.

We further visualize the top 5 and bottom 5 roads in terms of impact coefficients for both commuters and non-commuters in the figure below.

Commuter Mean Non-commuter Mean RAMP 5 FR RAMP 9 (FR MD655) TO MD 157 58 RR    MS8 Non-commuter Current Commuter Current RAMP 6 FR RAMP 3 TO GREENSPRING AVE RAMP 6 FR RAMP 3 TO GREENSPRING AVE Roeaed Name Roadd Nme RAMP 3 FR MD 158 TO MD 695 NB RAMP 3 FR MD 158 TO MD 695 NB RAMP 8 FRIS 83 S8 TO MT ROYAL AVE RAMP 8 FR IS 83 SB TO MT ROYAL AVE R D      MO O  PGS) R P   P  P  P 9S) 1000 3000 4000 5000 200 400 800 1000 1200 2000 600 Value Value (b) Top 5 Roads with Largest Non-commuter Traffic Increase (a) Top 5 Roads with Largest Commuter Traffic Increase Non-commuter Mean RAMP 3 FR IS 695 EB TO GREENSPRING AVE RAMP 9 FR IS 79S SB TO METRO CENTRE Non-commuter Current RAMP 6 FR PARALLEL DR TO RAMP 8 RAMIP 3 FR IS 695 EB TO GREENSPRING AVE Roadd eame Koadd ame BALTIMORE BLVD LAKE MONTEBELLO DR METROPOLITAN BLVD RAMP 6 FR PARALLEL DR TO RAMP 8 Commuter Mean LAKE MONTEBELLO DR EAST AVE Commuter Current 2000 8000 10000 12000 4000 4000 6000 1000 2000 3000 5000 6000 Value Value (d) Top 5 Roads with Largest Non-commuter Traffic Decrease (c) Top 5 Roads with Largest Commuter Traffic Decrease These roads are most significantly affected by the bridge collapse. The road "RAMP 5 FR RAMP 9 (FR MD695) TO MD 157 SB" has the highest impact coefficient for both commuters and non-commuters, reaching 11.994. Among commuters, the road "RAMP 9 FR IS 795 SB TO METRO CENTRE" has the smallest impact coefficient of 0.005, while for non-commuters, "RAMP 3 FR IS 695 EB TO GREENSPRING AVE" has the smallest impact coefficient of 0.059.

The following visualizations display the top 100 and bottom 100 roads for commuters and non-commuters, providing a more intuitive representation of how different roads in Baltimore are affected by the bridge collapse. Roads where the impact coefficient is closer to blue are negatively affected, while those closer to red are positively heavily impacted.

For commuters, due to the collapse of the bridge, the traffic that previously crossed the Patapsco River must now be rerouted through "Bridge-II" (as shown in the figure), leading to an increase in traffic volume on this bridge, with an impact coefficient greater than 1. However, for non-commuters, the impact coefficient is less than 1, possibly because the collapse of the m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m bridge reduced non-commuters’ willingness to travel across the river, thereby decreasing traffic m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m volume compared to before the collapse. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m The figure also reveals a significant increase in Beltway traffic for both stakeholder groups, m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m particularly on the segment “RAMP 5 FR RAMP 9 (FR MD695) TO MD 157 SB” shown in m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

frequently traveling on the Beltway. A possible explanation for this behavior is the higher speed limit on this road, which allows drivers to reach their destinations more quickly.

关注数学模型 Task 2: The impact of the project on the bus system 6

6.1

Three-layer Bus Network Model (TBN)

As urban development progresses, various modes of transportation have emerged, yet buses remain the preferred mode of travel for most individuals. This study focuses on optimizing the public transportation system of Baltimore City, assessing the potential impact on existing urban residents after its implementation. By utilizing the originally constructed transportation network, we develop a TBN Model to analyze the connectivity between higher and lower layers.

▶Step 1: Classification of Bus Station Levels

We apply and refine the weighted k-shell decomposition algorithm for classifying each bus station[8][9]. In the original weighted k-shell decomposition method, the weighted degree ks is calculated by considering both the degree of the node and the weight of its edges, reflecting the importance of a node. It is defined as follows:

ki ks = [ka(∑ wij)β]a+β, (10) j ● where ki represents the degree of node i; wij represents the weight of the edge between nodes ¿ 1 and j; α andβ denote the influence of degree and weight, respectively.

However, in a bus network, stations are abstracted as nodes, overlooking their intrinsic attributes such as geographical location, connections to surrounding environments, and popu- lation density in the area. To address this, we introduce a weighted metric S to quantify each bus station's attributes, incorporating the POI (Point of Interest) [11] indicator and the num- ber of on-off passengers. This approach ensures a comprehensive consideration of the actual conditions, linking bus stations closely with urban planning.

(11) where Ni represents the total number of passengers boarding and alighting at station i, and the POI indicator reflects the distribution of infrastructure within a defined area, often used to gauge service convenience and resident activity. Based on Baltimore's actual conditions, we classify five types as shown below:

Weight POI Type Weight POI Type Weight POI Type 0.7 1.5 railway station subway exchange tourist attraction 0.5 0.75 markets universities

Next, we employ the entropy weight method (TOPSIS) to compute the weight of the two indicators and derive the bus station scores S. Based on the bus station scores S and equation (11), we design an improved weighted k-shell model, assuming that all bus routes are of equal importance, with edge weights wij set to 1. Typically, α = β = 1, assuming equal influence of degree and weight.

ks = √ki × S, (12) where ki represents the degree of node i, i.e., the number of edges connecting to the node. In the transportation network model, the number of routes served by bus station i is equivalent to its degree:

(13) ki = length(Routes_Seri),

where Routes_Seri denotes the set of routes served by station i.

Thus, we assign a unique ks to each bus station. A higher ks indicates greater importance of the station in the network, and it corresponds to a higher tier in the model.

Finally, we discretize the ks values to facilitate the counting of nodes within each range. In this paper, we define the interval length as 0.05. For example, if ks = 0.045 ∈ (0, 0.05), all nodes within this range have their ks values adjusted to 0.25, which represents the interval mean.

▶Step 2: Construction of the Three-tier Bus Network

At this point, we have obtained the distribution of ks, as shown in the following histogram:

400 80 Derivative of Cumulative Sum 20

15 60 300 Frequency 10

40 5 200

2.0 1.9 1.7 1.8 1.6 20 100

0 0 0.0 0.5 1.0 2.5 1.5 2.0 3.0 Evaluation Score

Based on the distribution of ks values, we divide the transportation network into three tiers: the core layer, the bridge layer, and the peripheral layer [12]. The core layer consists of key traffic nodes that serve as hubs in the network, with the highest ks values. Analyzing the high ks values, we identify a breaking point at a certain value ks,i, which signifies the boundary between the core and bridge layers. Nodes with ks > ks,i are categorized as belonging to the core layer.

We then analyze the nodes with low ks values. Defining the cumulative ksvalue for a node: for a node ks < a, we calculate the total number of nodes within this range and sum their ks values to obtain the cumulative ks value. The point at which the cumulative ks value reaches a peak corresponds to the boundary between the bridge and peripheral layers. Nodes with ks < ks,j are classified into the peripheral layer. The remaining nodes, where ks,i < ks < ks,j, belong to the bridge layer.

关注数学模型

6.2 Model Solution and Results

The project aims to improve the public transportation network by adding two new bus routes after analyzing the tiers of bus stations. To assess the need for additional bus routes, data regarding key infrastructure in Baltimore — such as popular tourist attractions, universities, and supermarkets — are collected to evaluate the residential activity levels at different bus stations. 微信公众号：数学模型 Based on the constructed Three-layer Bus Network (TBN) model, the three-tier bus network of Baltimore is shown in the figure below.

微信号：MATHmodels

In the Core Layer, there are 11 bus stations, in the Bridge Layer there are 1,180 bus stations, and in the Outer Layer, there are 1,444 bus stations. To enhance the network, roads within different layers are classified using a shortest distance search method, dividing the roads into five categories. The locations(a) and distribution percentages of these roads(b) are depicted in the figure below.

Based on the TBN model, our goal is to construct additional bus routes connecting the Core Layer and Bridge Layer, as well as more routes between the Bridge Layer and Outer Layer, to facilitate residents’ travel from the outer regions to the city center, specifically to bus stations in the Core Layer. Thus, the proposed project suggests adding two new bus routes to achieve this objective. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m A 2-kilometer radius circle is drawn with the average coordinates of the 11 bus stations in the Core Layer as the center. The surrounding local transportation network and infrastructure are shown in figure (a). The final bus route plan is shown in figure (b), where the two new routes significantly improve connectivity between the Core Layer and Bridge Layer bus stations.

• Tourists: For tourists, the new bus routes connect many famous attractions, making it easier to travel between different points of interest.

• Suburban Residents: For suburban residents, the project significantly improves connec- tivity between the Bridge and Core Layers, providing easier access from the suburbs to areas with more developed infrastructure.

• College Students: For college students, the project also considers universities such as Johns Hopkins University, offering students more transportation options.

Based on the project, the following five variations in road conditions are observed, as illustrated in the figure below.

As depicted in the figure, the implementation of this project resulted in an 18.3% increase in road conditions between the Core and Bridge layers. Additionally, the road conditions within the Core layer increased by 95%, highlighting the significant advantages of this project. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 关注数学模型 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

7 Task 3: The project best improves the lives of the residents

7.1 Improved Dijkstra Algorithm

To analyze the impact of newly constructed metro lines on the travel patterns of Baltimore’s residents, we have developed a hierarchical path planning model. Unlike the traditional Dijkstra algorithm, we update the weights of road paths to represent travel times, with the primary objective being to minimize the total travel time:

a(u, v) X X Nd ∈N, min T = t(i, j) = v(L(u, v)), (14) 微信公众号：数学模型 i,j∈Nd i,j∈Nd where Nd denotes the set of nodes involved in achieving the shortest travel time.

7.2 Double Density Fitting Model (DDF)

Public transit station density is frequently used as an indicator of transportation accessibility, which is inherently linked to road network density. In this section, we examine the potential correlation between bus station density and road network density. We employ road density to estimate the effect of unconstructed metro stations on the density of public transit stations. Additionally, we calculate the current bus station density surrounding the existing two metro stations to evaluate the impact of metro construction on bus stations. 微信号：MATHmodels  Step 1: Grid Map Creation

A 6×6 grid map is constructed for the central district of Baltimore to estimate the density within each grid cell.

 Step 2: Calculation of Bus Station Density and Road Network Density

Since the area of each grid cell is uniform, we simplify the road network density to the total length of accessible roads within the region, while the bus station density is represented by the total number of bus stations within the grid. This is formalized as:

 X Nb ∈N ρbus = v,     v∈Nb , (15) X Nr ∈N ρroad = a(i, j),     i,j∈Nr m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m where Nb represents the set of bus stations within a grid cell, and Nr represents the set of road nodes within the cell. The term aij denotes the length of the accessible road between nodes i and j.

 Step 3: Fitting and Bus Station Density Prediction

Various methods, including linear, quadratic, cubic, and exponential functions, are used to fit the relationship between road network density and bus station density. The best-fitting method is selected, and the bus station density before the construction of the metro is predicted based on the current road network density.

 Step 4: Metro Impact Analysis

For a more precise analysis of the metro’s impact on public transportation, the map is further refined into a 20×20 grid. The difference between the actual bus station density and the predicted bus station density provides a measure of the impact of metro construction on bus stations, denoted as ∆ρbus:

∆ρbus = ρbus −ˆρbus. (16)

7.3 Model Solution and Results

Despite Baltimore being one of the United States’ primary port cities, existing metro lines, as reported in [10], fail to meet the daily transportation needs of its residents. A study evaluating Baltimore’s current economic condition proposed four additional metro lines. From this, we selected one line as a representative “transportation project most likely to improve residents’ quality of life” for further analysis. Additionally, we proposed the inclusion of new metro stations to accommodate the travel demands of a broader group of stakeholders. The existing metro routes and the line under analysis, marked in orange, are shown below.

The proposed line, as per the original draft, does not connect to the existing two lines, pre- venting seamless transfers. To resolve this, we added new stations, such as “Upton” connecting to the Green Line and “Cultural Center” connecting to the Navy Line, thus enabling passengers to transfer between lines.

关注数学模型

7.3.1 Question a: The Benefits to Residents

By applying the improved Dijkstra algorithm, we calculate the time savings for residents in various locations when traveling to the city center (Charles Center, 39.2895, -76.6163) after the project’s implementation, in addition to the time taken to reach the city center post- implementation.

微信公众号：数学模型 微信号：MATHmodels

From (a), areas shaded in yellow represent the largest time savings, indicating that the project significantly reduces travel time for residents in suburban areas. From (b), it is evident that residents along the new metro line can reach the city center faster. The metro system also offers more travel options for residents, reducing congestion risks on the roads.

- Safety Analysis: Compared to surface transportation, metro operations are unaffected by road traffic, significantly reducing the risk of accidents caused by traffic congestion. Running on independent tracks, the metro system greatly minimizes the risk of collisions with other vehicles or pedestrians and avoids intersections, further lowering the risk of accidents.

7.3.2 Question b: The Impact on Other Stakeholders

Next, we assess the project’s impact on other stakeholders. The following image illustrates the stations along the proposed line and the time required to reach the airport from each station.

• Flight Passengers: For passengers traveling to the airport, the metro line allows transfers at the Cultural Center station to the Navy Line, providing access to BWI Airport. The travel time from various stations to the airport is shown in Figure 20.

• Tourists: Our project passes several major tourist attractions such as “Clifton Park” and “Herring Run Park,” providing tourists with an easy access route from the airport to these locations.

• Business Owners: For businesses such as Walmart, our project will bring increased foot traffic, leading to higher revenues. Additionally, the project makes it easier for people to access the city center, indirectly benefiting local businesses.

• Commuters: As seen in Figure 20, the project also connects to Baltimore’s Penn Station, allowing commuters to travel to their workplaces by transferring from the metro to the train station.

7.3.3 Question c: Disruption to Other Transportation Needs

Based on the constructed DDF model, this section analyzes the impact of the two existing subway lines on bus routes, which in turn helps to assess the effect of the newly constructed subway on bus stations. First, a 6×6 network map is constructed, displaying the road density of Baltimore (a) and the bus stops density (b) as shown in the figure below. In the maps, the closer the color is to yellow, the higher the density; conversely, the closer the color is to blue, the lower the density.

surrounding grids. It is also evident that grids with higher road density tend to have higher bus station density, and vice versa. Therefore, a preliminary correlation between traffic station density and road network density can be inferred.

Linear and various nonlinear fitting methods are applied to analyze this relationship, with the fitting results presented in the following figure.

关注数学模型 微信公众号：数学模型

微信号：MATHmodels The quadratic function provides the best fit, and the relationship between road density (y) and bus station density (x) is expressed as:

y = 16241x2 −15507x + 4751. (17)

Using this fitted relationship, we estimate bus station density, and by subtracting the esti- mated density from the actual density, we obtain the impact of the subway on bus stations, as illustrated in the figure below.

As shown in the figure, areas along the two existing subway lines in Baltimore exhibit a larger difference, indicating an increase in bus stations along the subway corridors after its construction. This suggests a higher demand for bus services. The likely cause is that the subway construction has increased the demand for transfers between subway and bus services, influencing the establishment of bus stations. Therefore, it can be inferred that the construction of our new subway line will similarly impact bus demand along the corridor, leading to an increase in the number of bus stations.

8 Sensitivity Analysis

We conducted a sensitivity analysis to assess the robustness of our results. In evaluating the positive impact of the subway on various sections, we examined the outcomes across multiple segmentation levels, ranging from a side length of 2,400 meters to 120 meters. The results are presented in the following figure.

The analysis reveals that the positive impact of the subway on different sections is robust. As the accuracy of grid segmentation increases, the number of bus stops per grid decreases, leading to a more pronounced positive impact of the subway on the respective sections.

9 Model Evaluation and Further Discussion

9.1 Strengths

• Impact Assessment Model: Leverages real-world AADT and AAWDT data to quantify m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m the impact of the bridge collapse, effectively assessing the consequences for different m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m stakeholder groups, including both commuters and non-commuters. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

• Regional Impact Consideration: Uses closeness centrality to assess not only the im- m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m mediate effect in Baltimore but also the wider regional transportation network, capturing m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

how interconnected areas may be impacted.

• Three-layer Bus Network Model (TBN): Enriches the model by considering points of interest (POI) in bus routes, providing a more realistic representation of commuter needs and prioritizing high-demand areas.

• Weighted K-Shell Decomposition: Uses a structured, tiered approach to classify bus stations based on connectivity, helping to identify important nodes in the network and improve overall transit access.

关注数学模型

9.2 Weaknesses

• Simplified Assumptions in the Impact Assessment Model: Assumes constant growth in AADT and AAWDT, which may not capture future trends or unexpected events affecting traffic.

• Limited Scope of Impact Assessment Model: Primarily focuses on highways, missing the potential impacts on local roads and alternative transportation modes, which may also be crucial to understanding the broader transportation network.

• Subjectivity in Tier Definition in TBN: The division between core, bridge, and pe- ripheral layers of the bus network may be based on somewhat subjective criteria. More objective, data-driven methods could improve accuracy.

微信公众号：数学模型 The strengths and weaknesses of our model can be visually presented and is shown below:

微信号：MATHmodels

9.3 Further Discussion

Although the models provide a solid foundation for analyzing Baltimore’s transportation network, there are several areas for future improvement. Incorporating dynamic traffic patterns using real-time data and predictive algorithms would allow the models to better reflect changing traffic conditions. Expanding the scope to include multi-modal transportation options, such as cycling, walking, and ride-sharing, would offer a more comprehensive view of the transportation system. Additionally, validating the models with real-world data or through simulations would help ensure their practicality and reliability.

Furthermore, integrating socioeconomic factors into the models would enable a more eq- uitable approach to transportation planning, ensuring that the needs of all communities are addressed. Conducting detailed cost-benefit analyses would provide decision-makers with the necessary tools to prioritize projects and allocate resources efficiently. These improvements will make the models more accurate, adaptable, and applicable to a wider range of real-world transportation scenarios.

10 Memorandum

Hamilton To: Baltimore Mayor

From: Team #2519935

Date: Jan 28, 2025

Subject: Two Projects to Improve the Lives of Baltimore Residents

Dear sir or madam:

We have recently conducted an in-depth exploration and study of the transportation system in Baltimore. With great enthusiasm, we would like to present two transportation project proposals aimed at enhancing the efficiency of mission-oriented travel in the city: the introduction of new bus routes and the creation of a new subway line. We understand that a robust transportation system is the foundation of urban development, and we aim to contribute thoughtfully to Baltimore's future transportation planning by weighing the advantages and challenges of these proposed projects.

Project I. Bus Route Optimization

Through gathering data on Baltimore's bus stations and referencing authoritative literature, we have constructed a three-tier bus network model. This model divides the city's bus stops into three layers: the Core Layer, Bridge Layer, and Outer Layer. Each of these layers contains several bus routes; However, we observed that the connections between the layers are not particularly strong. To address this, we propose adding two new bus routes that would link the Core and Bridge Layers. These additional routes would enhance the connectivity of the city's transportation network, allowing residents to more easily reach key destinations such as the city center, train stations, and airports. Not only would this alleviate pressure on the existing rail system, but it would also meet the growing travel needs of Baltimore's residents while supporting the development of surrounding areas. However, we acknowledge that the addition of these bus routes will lead to higher operational and maintenance costs, which could place some strain on the city's budget.

Project II. New Subway Line

We also propose the addition of a new subway line based on a DDF model we have designed. Our analysis indicates that this subway line would significantly reduce travel time to the airport compared to traditional modes of transportation. Furthermore, it is projected to increase the density of existing bus stops, facilitating smoother transfers between different modes of transportation. While the new subway line holds great potential for improving travel efficiency, we recognize that its construction timeline would be lengthy, and certain sections of the route would pass through the city center, potentially affecting short-term mobility for residents.

As university students, we understand that these projects are only preliminary ideas and that further research and feasibility studies will be necessary for implementation. Nevertheless, we sincerely hope that you will consider our proposals and that they can be incorporated into the future urban planning of Baltimore. Thank you for your time and consideration.

Yours Sincerely,

关注数学模型

Output: The TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)

combined with the entropy method offers several advantages over using each of these methods individually, especially in decision-making and multi-criteria decision analysis (MCDA). Here’s how combining these two methods benefits the process:

1. Objective Weight Determination (Entropy Method)

Entropy Method: It helps in determining the weight of each criterion based on the amount of information it provides. In decision problems, the entropy method is often

关注数学模型 used to objectively assign weights to each criterion by analyzing the degree of variation or uncertainty in the data. A criterion with higher variability (more information) gets a higher weight, which is a more objective and data-driven approach than assigning arbitrary or subjective weights. Advantage: When you combine this with TOPSIS, it ensures that the weights assigned to each criterion are not biased or arbitrary. This makes the decision process more transparent and credible. 微信公众号：数学模型 2. Ranking Accuracy (TOPSIS)

TOPSIS: TOPSIS works by calculating the proximity of each alternative to the ideal and negative-ideal solutions, ultimately ranking the alternatives based on their relative closeness to the ideal solution. It’s a widely used method due to its simplicity and interpretability. Advantage: TOPSIS helps to perform the final ranking of alternatives and makes the decision-making process more straightforward by quantifying how close each alternative is to the ideal solution.

3. Handling Uncertainty (Entropy + TOPSIS)

Entropy Method for Uncertainty: In the entropy method, weights are assigned in 微信号：MATHmodels a way that reflects the uncertainty of each criterion. This is especially helpful when there is a lot of variability in the data, as it prevents overemphasis on criteria with low information content. Advantage of Combination: When used together, entropy provides an objective weight assignment that adapts to data variability, while TOPSIS handles the relative ranking based on proximity to the ideal solution. This combination ensures that the rankings are not only driven by subjective preferences but also by the intrinsic uncertainty and information content in the data.

4. Mitigating the Impact of Subjectivity

TOPSIS Alone: Without entropy, the TOPSIS method requires predefined weights, which are often subjective and based on expert judgment or assumption. This can intro- duce bias, particularly when the decision-makers have limited or inconsistent knowledge of the criteria’s relative importance. Advantage of Combination: The entropy method provides a more objective weight assignment, reducing the subjectivity involved in the decision-making process. By using entropy to calculate weights, the model ensures that the weights reflect the data characteristics, making the ranking in TOPSIS more robust and less prone to human bias.

5. Flexibility and Robustness

TOPSIS with Entropy Weights: By integrating entropy with TOPSIS, the method becomes more flexible and robust in handling a wider range of decision problems. It allows for better performance in situations where the importance of criteria may not be immediately obvious or when there is significant variability in the data. Advantage: This combination is particularly useful when dealing with complex multi-criteria decision problems in uncertain or diverse environments. The entropy method ensures that criteria with higher uncertainty or variability are weighted more appropriately, while TOPSIS provides a solid framework for ranking based on those weights.

In essence, combining TOPSIS and the entropy method enhances both the objectivity and accuracy of the decision-making process, addressing the limitations of using either method alone.

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m
