Summary

In Baltimore, the population continues to grow, and the aging transportation network is struggling to meet the increasing travel demands. The collapse of the Francis Scott Key Bridge has exacerbated the already strained city traffic. Optimizing the transportation system has become urgent. To address this, we conducted an evaluation of Baltimore’s transportation network based on stakeholder needs, followed by targeted optimization measures.

For Task 1, we first visualized Baltimore's transportation network. To assess the overall traffic conditions, we used Queueing Theory to calculate the congestion index. For each stakeholder, we quantified their needs using Accessibility to various locations, with different types of accessibility considered for each stakeholder. We used a method combining A* and GA to calculate Accessibility. Finally, we simulated actual data on the map, comparing the changes in the above metrics and the overall network before and after the bridge collapse to highlight its severe negative impact. The results are shown in Figure 6, Figure 7, and Figure 9.

For Task 2, we chose bus route optimization as a potential project. First, we established the Baltimore bus network and measured the importance of each station using node Betweenness Centrality and Degree Centrality, identifying areas in need of optimization. We then created a nonlinear programming model with the objective of maximizing bus coverage, subject to constraints on the coordinates and number of new stations, as well as the distance between new and original stations. Since the area is irregular, we used Monte Carlo Simulations to calculate the bus coverage. This project increased bus coverage from 61.37% to 78.13%. Finally, we compared stakeholder ratings before and after the improvement, proving the significant positive impact on stakeholders, as shown in Figure 12.

For Task 3, we recommended a project to improve Road Availability in neighborhoods. We selected Connectivity Index, Congestion Index, and Mixing Index as metrics for Road Availability. We used Approximate Dynamic Programming(ADP) to optimize paths in low-scoring areas, with the results shown in Figure 13. We proved this project had a positive impact on multiple aspects for various stakeholders.

Additionally, to ensure the safety of the transportation system, we developed software that integrates the indicators and conclusions from the three models.

Lastly, we conducted sensitivity analysis to prove the robustness of the models and the reasonableness of parameter selection. The key highlight of this study is the comprehensive visualization and in-depth analysis of local conditions, the practical selection of models, and the thorough simulation of the established models.

1 Introduction

1.1 Problem Background

"Traffic safety is a very serious matter. Every year thousands of people die in 微信公众号：数学模型 traffic-related accidents. This is not a matter of numbers; it’s about lives, families, and communities. We need to act together to make our roads safer."

Barbara Boxer

The transportation system directly impacts urban development and residents' lives. An efficient transportation network can promote economic growth, attract new businesses and residents, but it often faces conflicts between the needs of different groups. Baltimore is currently dealing with issues such as aging infrastructure, limited transportation options, and problems like the collapse of the Francis Scott Key Bridge, 微信号：MATHmodels which have caused traffic congestion, affecting residents' mobility and the city's economic development. To address these issues, Baltimore is undergoing a transportation network overhaul, with the goal of enhancing public transit, improving infrastructure, and achieving sustainable development.

1.2 Restatement of the Problem

Your team needs to propose recommendations to help improve Baltimore's transportation network, with a focus on the following issues: the impact of the collapse of the Francis Scott Key Bridge on the transportation system, the inadequacy of public transit and walking infrastructure, and the disruption caused by urban highways to communities. By building a transportation network model, you need to analyze how these issues affect different groups and propose corresponding solutions.

· Impact of Bridge Collapse: Analyze the impact of the Francis Scott Key Bridge collapse on transportation, particularly how it affects commuters, businesses, and residents, and propose improvements.

· Public Transit and Walking Infrastructure: Study potential projects to improve the bus or walking systems, analyze how these projects can enhance residents' mobility, and their impact on other groups.

·Improvement Recommendations: Propose a project to improve Baltimore's

transportation network, detailing the project's advantages and disadvantages, especially its impact on residents' lives, travel safety, and economic activities.

1.3 Our Work

Based on the problem analysis, we construct three distinctive models—Bridge Collapse Impact Quantification Model, Transit Network Optimization Model and Community transportation availability optimization model. Then we have designed a software to enhance the traffic safety of Baltimore City. Finally, we conduct sensitivity to test the robustness of our models. The work we have done is mainly shown in Figure 2.

2 Assumptions and Justifications

▲Assumption: The departure and destination points of stakeholders follow a

specific spatial flow pattern.

▼Justification: In reality, the exact departure and destination points for each stakeholder in the traffic network are difficult to predict and influenced by various factors. However, as a general trend, the flow patterns tend to follow certain

关注数学模型 regularities, which can be modeled based on known spatial patterns and specific probability distributions.

▲Assumption: Traffic flow in the network is stable, with no consideration for short-term disruptions (such as weather, accidents, etc.).

▼Justification: To simplify the analysis, short-term external factors such as weather and accidents are excluded, and the focus is placed on the impact of large-scale disruptive events, like bridge collapses.

微信公众号：数学模型

▲Assumption: Vehicles arrive at a road segment randomly and independently,

with the same travel time through the segment.

▼Justification: The travel decisions of different vehicles are independent. In some traffic-controlled routes in Baltimore, vehicles are strictly required to maintain a specific speed, significantly reducing speed differences, which makes the time taken by vehicles to pass through these segments nearly identical.

3 Notations

微信号：MATHmodels The key mathematical notations used in this paper are listed in Table 1.

Symbol

Description Unit 퐿푞 Traffic Congestion Index 5 푁표푑푒푠 Crossroads Collection 5 퐸푑푔푒푠 Path Collection 5 퐶퐵(푣) Betweenness Centrality 6 퐶퐷(푣) Degree centrality 6 퐶퐼 The connectivity index 7 퐿푈푀퐼 The hybrid index 7 Note: There are some variables that are not listed here and will be discussed in detail in each section.

4 Data Processing

·Data Filtering To ensure that all routes belong to the Baltimore transportation network, we screened the routes according to the latitude and longitude range of Baltimore, and only retained the sections with latitudes between 39.18 and 39.33 and longitudes between -76.71 and -76.45. ·Data Cleaning Outliers: Some fields in the dataset have serious data missing, exceeding 50%, and it is impossible to use interpolation or other methods to supplement valid data. Therefore, we decided not to use these fields in subsequent modeling.

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

5 Bridge Collapse Impact Quantification Model

5.1 Network model building and visualization

To clearly understand the actual traffic situation in Baltimore, we first need to build a transportation network. In the city’s spatial structure, intersections and turning points play a significant role. From the perspective of the road network and daily lo-cations, they are intuitive and easily identifiable. In terms of the relationship between buildings and roads, small building clusters are typically surrounded by intersections. When constructing the graph model, these intersections serve as nodes, simulating brain cognition to make the model more realistic and provide a more practical per-spective for urban space analysis.The intersections and turning points of the path are taken as nodes of the traffic network, recorded as the set 푁표푑푒푠= {푛표푑푒푖} .The path is taken as the edge of the traffic network, recorded as the set 퐸푑푔푒푠= {푒푑푔푒푠푖}.The starting point u and the ending node v of the path can both be found in the set Node, that is, 푢, 푣∈푁표푑푒.The time required to pass the path is taken as the weight, that is, 푊= {푇푖푚푒푖}.

Here's a visualization of the entire Baltimore transit network.

The different colored nodes in the diagram represent various types of road inter-sections, corresponding to the "highway" column in the edges_all dataset. The width of the edges reflects the weight, which represents the significance of each road. In general, the weight of an edge is closely related to the importance of the road, with higher weights indicating main roads. Since major roads experience heavier traffic and are more prone to congestion, vehicles tend to spend more time traveling through these areas. From the diagram, it’s evident that Baltimore’s urban traffic network is

关注数学模型 highly complex, with a dense web of roads, which could potentially impact traffic safety.

Traditional network graphs are difficult to visually present the absolute position relationship between nodes. To overcome this limitation, we build a search set 푑푖푐푡= {[표푠푚푖푑, 푙푎푡푖푡푢푑푒, 푙표푛푔푖푡푢푑푒]} based on the dataset nodes_all. Each item in the set contains a node unique 微信公众号：数学模型 identifier (osmid) and a geographic location, providing a basis for mapping nodes to actual locations. By searching the set to determine the location of each node on the actual map, the abstract network graph is closely associated with the real geographic space. The result is shown in Figure 4.

微信号：MATHmodels

5.2 Quantification of impact indicators

The collapse of the Francis Scott Key Bridge had a significant impact on city residents, business owners, suburban residents, commuters, passthrough travelers, and tourists. These impacts can be categorized into common and individual aspects. From a common perspective, the collapse forced all individuals who originally relied on the bridge to find alternative routes. This change led to a surge in traffic on other routes, causing congestion. This negative effect is consistent across all stakeholders, as it di-rectly disrupted daily commutes, goods transportation, and travel plans. However, the detour’s shortest path varies depending on factors such as travel mode, destination, and time of travel, reflecting the individual impacts on each stakeholder.

1. Common Impacts

A. Congestion Index The Francis Scott Key Bridge is a suburban fortress in Baltimore, with a large amount of traffic every day. After the bridge collapsed, vehicles that originally passed through the bridge had to take a detour, which would increase the traffic volume on other traffic routes and would greatly cause traffic congestion. Therefore, we use the queuing theory (MMC) model to measure the changes in the congestion index of other routes around the bridge. In the previous article, we demonstrated the rationality of Assumption 1, so we believe that vehicle arrivals follow a Poisson distribution. Taking into account realistic factors, we have improved the queuing theory model. The state formula of the queuing theory is as follows:

2 /n! μ (1) Pn k λ /k! μ k=0 Where Pn represents the state probability distribution, c represents the number of lanes, and k represents the correction factor, which is related to the road type. λ represents the number of vehicles arriving per unit time. Here we take the unit time as 1 hour and use the AADT field data in the dataset “MDOT"to calculate.

AADT (2) λ= 24

μ indicates the number of vehicles passing through the road per unit time, which is inversely proportional to the time it takes a vehicle to pass through the road section.

1 ν (3) = n1 L T

Where L represents the length of the road section, and v represents the driving speed of the road section. Generally speaking, different types of road sections have different speeds. We supplemented the data based on the ClassCode data representing the road section type in the table.

v(m·s−1) Class Name Class Code 65~75 Interstate 1 2/3 60~70 Principal Arterial 35~45 4 Minor Arterial 40~50 5 Major Collector 30~40 6 Minor Collector 25~40 Local 7 For the MMC queuing system, we can calculate its average queue length.

C λ 1 1 2 io μ λ cμ (4) Ⅱ k λ μ 3 k! k=0 We use the average queue length as the congestion index of the road section. The longer the average queue length, the more congested the road section is.

2. Individual Impacts

We mainly use Accessibility to quantify the interests among various stakeholders.

关注数学模型 Accessibility is denoted as the function of measuring interests,Co is the community, Ci is the city,Bi is the enterprise,Si is the suburb,Mi is the urban edge,Ai is the area with concentrated scenic spots, and Pi is the port and shipping center.

tourists

stakeholders

Office locatic

Within the city

B.Residents The Francis Scott Key Bridge plays a crucial role as a connective link in Baltimore's urban spatial structure, primarily linking the city to the suburbs. Based on this charac-teristic, we can divide residents into city and suburban categories.

a.Urban Residents The port and shipping center are located far from the city, making it difficult for city residents to access related jobs. The bridge collapse affects port operations, and its reconstruction is essential to restore connectivity. The accessibility between the city and the portinfluences both employment opportunities and the residents' daily lives. Additionally, city residents often travel between communities, making in-ter-community accessibility important. The bridge's reconstruction should avoid cre-ating barriers between communities to prevent reducing travel efficiency and nega-tively impacting residents' quality of life.

(5) BC = Accessibility(Co j, Pi) + Accessibility(Co j, Cok) ● b.Suburbanites Suburban residents often work, entertain, and seek medical care in the city, mak-ing frequent trips between the city and the suburbs. The accessibility from the city to the suburbs affects travel costs, which in turn impacts the quality of life and work efficiency. Poor accessibility leads to longer commute times, reducing overall well-being, while better accessibility saves time and could even drive suburban real estate development.

(6) BS = Accessibility(Ci, Sj)

C. Commuters

Most commuters live and work within the city, so the city's transportation layout affects their commute time. Good internal accessibility in the city shortens commute times, improves work-life efficiency, reduces commuter fatigue, and enhances overall satisfaction with both work and life.

(7) ( , ) BM Accessibility C C  i j

D.Transit passengers Travelers with intercity needs, such as those connecting flights or buses, or on cross-city road trips, are impacted by the accessibility between the urban fringes. Poor accessibility can lead to missed connections and higher costs, while good accessibility ensures a smooth journey and improves the overall impression of the city.

(8) ( , ) BP Accessibility M M  i j

E.Visitors Tourists often visit multiple attractions in a single day, and the accessibility be-tween these attractions affects their experience and time management. Good connec-tivity allows tourists to move between attractions more easily, visit more sites, and have a higher level of satisfaction. On the other hand, poor connectivity may lead them to skip some attractions, reducing the overall experience. We quantify the bene-fits for tourists based on the accessibility between these attractions.

(9) ( , ) BT Accessibility A A  i j

F. Entrepreneur The accessibility from businesses to communities affects entrepreneurs' business strategies and operational costs. External connectivity also plays a key role in deter-mining logistics costs and market expansion efficiency. For example, good connectiv-ity with the port reduces logistics costs, while strong connections with other cities fa-cilitate collaboration opportunities.

(10) ( , ) BB Accessibility B Co  i j

5.3 Accessibility definition and solution

The function is used to calculate the shortest path between regions. In the specific calculation process, we innovatively combine the A* algorithm with the genetic algorithm to improve both efficiency and accuracy. The improved A* heuristic cost function is as follows:

(11) ( ) ( ) ( ) f  n g n h n    

Where 훼represents the weighted parameter, 푔(푛) represents the sum of the weights of the paths, and ℎ(푛) is the heuristic distance. We usually think that the cost of

关注数学模型 getting from one place to another is not only related to the weight, but also to the spatial distance. We use the Haversine formula to measure the spatial distance between two points on the sphere.

(12)   2 1 2 1 La La Lon Lon       2 2 2 1 2 ( ) asin sin cos( ) cos( ) sin h n R L L              2 2       微信公众号：数学模型 Where 퐿푎1 and 퐿푎2 represent the latitude (푟푎푑) between two points, and 퐿표푛1 and 퐿표푛2 represent the longitude (푟푎푑) between two points.

The fitness is calculated as follows.

1 1 ( ) fitness P   (13) 1 k  ( ) g n  ( , ) w v v 1 i i  1 i 

The selection probability is calculated as follows.

微信号：MATHmodels  fitness P i (14) p  i N    fitness P j 1 j 

The specific algorithm design ideas are given in pseudocode form.

Algorithm 1 A* and GA

Input: Baltimore transportation network graph, A List of starting and ending points Output: A set of shortest paths 1: for search in List do 2: Use the A* algorithm to search for a path as a better initial population for the genetic algorithm.

for generation in 100 do 3:

path1,path2=the last two parent paths generated 4:

child= combine path1 and path2 5:

if len(path) > 2 and random.random() < self.mutation_rate do 6: 7: Swap two nodes and recalculate the path end if 8:

best_path=The path with the highest fitness 9:

best_cost=The cost of the best path 10:

end for 11: 12: Add the shortest path to the result set ans 13: end for 14: return ans

5.4 Bridge collapse data processing

The Francis Scott Key Bridge is a transportation hub in Baltimore, mainly used to connect the city with external areas.

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Therefore, in the dataset edges_all, the ref column records the reference code of the road. The path number of the Francis Scott Key Bridge is 푟푒푓= 퐼695. The osmid represents the path or relationship to which the edge belongs, which is the unique identifier of the road segment. We use the path number to find the osmid of all sections of the Francis Scott Key Bridge and put them in set 퐴. We believe that the collapse of this bridge has made all sections containing this bridge impassable, so all osmids in 푒푑푔푒_푎푙푙are compared with the elements in set 퐴. If the 표푠푚푖푑휖퐴, delete this edge.

5.5 Solution

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m The left figure represents the traffic network before the bridge collapse, while the m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m right figure shows the traffic network after the collapse. Figure 6 illustrates that the m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m collapse of the bridge has rendered many road segments impassable, significantly m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m re-ducing the number of accessible routes. We can also observe that most of the road construction around the bridge was primarily designed to facilitate travel between the city and the suburbs, but key connections between the two areas are limited. As a re-sult, the traffic network after the bridge collapse only maintains connectivity within a small area.

We calculated the degree of road congestion at different longitudes and latitudes every year. As can be seen from the figure, the changing trends in different years are roughly similar, which can be explained by the fact that the traffic volume on some

关注数学模型 sections of the road is indeed greater than that on other sections, which is more likely to cause congestion. It also shows that the traffic layout in the Baltimore area has basically not changed in recent years. We can also know that the degree of congestion was the lowest in 2014, and since then the degree of congestion has basically shown an increasing trend year by year, which may be due to urban development and population growth. So far, the existing transportation network has been difficult to meet the needs of Baltimore. The congestion level in 2020 ranks first in the figure, which may be the impact of the new crown epidemic on the city, which is a relatively special change. Finally, the congestion level after the bridge collapsed was second only to 2020, which fully demonstrates the importance of the bridge in the transportation network. 微信公众号：数学模型 To verify and improve the interest measurement system, we conducted simulations. We focused on the area around the bridge collapse and randomly collected 100 data samples, which were divided into categories such as communities and cities according to their attributes. We used the established model to calculate the shortest path for 微信号：MATHmodels each category of data and depict the road sections. The results are shown in the figure on the right. We also calculated accessibility and scores for each

stakeholder based on this, and the results results are as follows.

and after the bridge collapsed. We use accessibility to measure the impact of bridge

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m collapse on stakeholders. Accessibility is determined by the time it takes for vehicles or pedestrians to pass through the road section. The longer the time, the greater the accessibility value and the more inconvenient the passage. As can be seen from the figure, the travel time of various stakeholders increased significantly after the bridge collapsed. Among them, suburban residents were most affected because there were few routes available between urban and suburban areas; urban residents were least affected because their daily activities were mostly in the urban area and they rarely traveled between urban and suburban areas.

6 Transit Network Optimization Model

Baltimore's aging infrastructure has significantly impacted residents' daily lives, and its transportation network needs urgent optimization. Given that buses are envi-ronmentally friendly and affordable, making them the preferred mode of transport for many city residents, we have decided to focus on optimizing the bus network to im-prove overall transportation efficiency and accessibility. 6.1 Urban Bus Network Visualization

Based on the Bus_Stop and Bus_Routes datasets, we analyze Baltimore's bus routes, treating them as network edges (set E) and bus stops as nodes (set V). We first record the station IDs for each route, and then plot the bus stops and routes on a map based on their geographic coordinates. The resulting map is shown in Figure 10.

To measure the importance of each bus stop, we use both betweenness centrality and degree centrality. The calculation method for betweenness centrality is as follows:

σst (v) CB(v)= ∑ (15) sevet∈V

Where σst represents the number of shortest paths from node s to node t, and σst(v) represents the number of shortest paths from node s to node t passing through node v.

Degree centrality is calculated as follows.

kv (16) CD(v)= n-1

Where kvis the degree of node v and n is the total number of nodes in the graph.

The importance of a node is calculated as follows.

CB(v) CD(v) +0.5 imp(v) = 0.5 (17) CD,max

关注数学模型 微信公众号：数学模型

From the diagram, we can see that the Baltimore bus network is densely distributed in the center and sparsely distributed around, which is related to the population residence and geographical characteristics of different areas of the city. The population is dense and the traffic demand is large in the city, so buses can relieve the pressure; the population is scattered in the suburbs, the distance is far, the bus efficiency is low, and the network is sparse. The importance score of bus stations, 푖푚푝(푣) , shows that most scores are between 0 and 0.5, which means that most 微信号：MATHmodels stations only have one or two routes stopping, and residents need to transfer, the travel cost is high, and the setting is unreasonable. There are few bus routes around the Francis Scott Key Bridge. Considering its importance and travel demand, subsequent modeling will focus on optimizing the bus network in this area to improve service quality and travel convenience.

6.2 Single-objective Optimization Model

·Parameters and decision variables 푑represents the service radius of the bus station, which is 0.3 km here. 푆푠푒푟푣푖푐푒 represents the total service area of all bus stations, and 푆푐푖푡푦represents the area of the city. 푏represents the number of new bus stations. [푋, 푌] represents the location set of the new bus stations.

The decision variables are { 푿풊, 풀풊}, 푏.

·Objective function In order to facilitate people's travel, we hope that the service range of the bus station can cover the entire city, that is, we hope that the value of the bus station service area/city area is 1, which is difficult to achieve in real life, so we hope to maximize this ratio. Note that this ratio is calculated after adding b bus stops with different longitudes and latitudes.

S max service (18) S city Since the service ranges of different bus stops overlap and the city area is difficult to calculate, we use Monte Carlo simulation to calculate this ratio.

Step1 Randomly generate 10,0000 coordinates within the city to simulate the m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m location of people who need to take the bus. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Step2 Calculate the distances from these 10,0000 sample points to the m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m surrounding stations. If there is a station with a distance from the sample point less m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m than 0.3 km, it means that the sample can take the bus conveniently and is added to m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m the set Service; if the distance between the station and the sample point is greater than 0.3 km, it means that the sample is not within the service range of the bus station.

Step3 The number of samples in the set Service/100000 is the current service range ratio.

·Constraints First, due to limited funds, the number of bus stations to be built is also limited.

(19) 0 b N  

Where 푁represents the number of bus stops that can be built with sufficient funds.

Secondly, the location of the bus station must be within the selected optimized area.

(20) 76 617382 76 584337 1 2 . . ( , ... ) X i b     i (21) 39 207759 39 237561 1 2 . . ( , ... ) iY i b   

(22) 0 90186 29 860591 . . Y X   i i

Among them, 푋푖represents the latitude of the newly added node, and 푌푖represents the longitude of the newly added node.

Finally, when planning new stations, the rationality of the distance between stations must be fully considered. Too long a distance between stations may cause large blank areas in the bus line coverage, which cannot meet the travel needs of residents along the line. We stipulate that the distance between a new station and any surrounding station cannot be greater than the maximum distance between the original adjacent stations.

(23) min( ( , )) max( ( , )) Ha new v Ha v v   1 i j j

Where 퐻푎represents the Hafsin formula, 푛푒푤represents the newly added node and

푣represents the original node. min 퐻푎푛푒푤, 푣푖 represents the shortest distance

between the newly added node and the surrounding nodes, and

min 퐻푎푣푗, 푣푗+1 represents the longest distance between the original adjacent

nodes.

To sum up, the planning model is as follows:

关注数学模型 푚푎푥푆푠푒푟푣푖푐푒 푆푐푖푡푦 0 b N    (24)  76 617382 76 584337 1 2 . . ( , ... ) X i b     i 39 207759 39 237561 1 2 . . ( , ... ) . . #(24) Y i b s t     i  min( ( , )) max( ( , )) Ha new v Ha v v   1 i j j  0 90186 29 860591 . . Y X    i i 微信公众号：数学模型

6.3 Solution

Here we mainly show the optimization process of the selected triangular area bus station. The greedy algorithm is used to solve Single-objective nonlinear programming model. The longitude and latitude of the five newly added bus stations are as follows:

1 2 3 4 5 微信号：MATHmodels Latitude 39.232 39.220 39.22711 39.23373 39.2345 Longitude -76.605466 -76.594134 -76.592677 -76.590588 -76.585844

The above figure is a comparison of the results of Monte Carlo simulation before and after adding stations, marking only the sample points within the service range. The red color indicates the location where the sample points appear most frequently, and the blue color indicates the location where the sample points appear less frequently. The histogram shows the traffic coverage at different longitudes and latitudes.From the figure, we can see that the five newly added stations have brought more sample points within the service range, which means that more residents can take the bus conveniently. Each bus station maximizes the service coverage, so the distance is reasonable. This is enough to prove that the model has effectively optimized the bus network. After the addition of new stations, traffic coverage increased from 61.37% to 78.13%.

To measure the changes in the convenience of travel for each stakeholder before and after the traffic improvement, we selected some buildings in the traffic improvement area, simulated the arrival process of four types of stakeholders, namely

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m urban residents, suburban residents, tourists and transit passengers, and scored them, and then compared the scores. Considering that businesses and suburban commuters rarely use public transportation, they were not included in the evaluation scope.Taking urban residents as an example, we selected the Brooklyn Ave residential area as the starting point and six places closely related to the lives of urban residents, such as the port, as the destination for simulation. The simulation process for other stakeholders is the same. Finally, the scores of each stakeholder before and after the traffic improvement are plotted into a graph, and the results are as follows.

It is worth noting that due to the different locations selected, horizontal comparison between stakeholders is meaningless. We focus on the score changes before and after traffic improvement. It can be seen that the hexagons framed by the scores before the improvement completely surround the hexagons after the improvement. The accessibility of stakeholders is determined by the time it takes for vehicles or pedestrians to pass through the road section, that is, the longer the time spent, the greater the accessibility value, which means the more inconvenient the

关注数学模型 passage. Therefore, after the traffic improvement, the travel of various stakeholders is indeed more convenient.

7 Community Road Availability Optimization Model

7.1 Supplementary Datasets

Step1 Use OpenStreetMap API to obtain highway and land use information in urban areas, extract vector data and boundary data of highways.

Step2 Use QGIS to identify the area surrounded by highways as polygons, and divide the area into plots surrounded by highways.

Step3 Correspond each plot to its land type.

7.2 Community transportation availability evaluation

We evaluate the traffic availability of each community and focus on optimizing roads in areas with lower scores. We selected three indicators to measure the traffic availability of a community: connectivity index, congestion index, and hybrid index.

1. The connectivity index is used to measure the complexity and accessibility of the transportation network. The better the accessibility, the higher the availability.

(25) nodes 1 2.The Congestion Index is used to measure the degree of road congestion. The higher the congestion, the lower the traffic availability. See formula 4 for calculation.

3.The hybrid index is usually used to measure the degree of mixing of land with different uses in a specific area. Generally speaking, the larger the index, the more diverse the land uses, and the more favorable it is for road availability. We express the hybrid index in the form of entropy.

n LUMI = −∑hi · ln(hi) (26) i=1

Where n represents the number of types of land use in the community, and hrepresents the proportion of land of each type of use.

The final formula for calculating community transportation availability is as follows:

1 1 1 L (27) CI + LUMI + score = 3 3 3

7.3 Traffic Layout Optimization Model

For communities with lower scores, we optimize the paths.

·Decision variables 퐿푈푀퐼푡표푡푎푙represents the overall mixedness index of the optimized area,퐶퐼푡표푡푎푙 represents the overall connectivity index of the area, 푞푢푎푛푡푖푡푦represents the total number of constructed paths, and 푙푒푛푔푡ℎrepresents the total length of constructed paths.

·Objective function The goal of the model is to change the direction of some highways to maximize the overall availability. While ensuring availability, the cost issue also needs to be considered, that is, the road to be built should be as short as possible.

length max( ) LUMI CI        (28) length H max

Where 퐻represents the planning and design variables of the highway, and 훼, 훽, and 훿are weight parameters used to balance the importance of 퐿푈푀퐼and 퐶퐼.

·Constraints Due to budget constraints, the total length of the construction and the number of construction paths also need to be limited.

(29) 0 0 quantity Q length Le     , 푄 and 퐿푒 represent the maximum number and the longest path that can be constructed by the operation.

Not all types of land are suitable for building roads. For example, near residential areas, highways will hinder the normal life of residents.

(30) ( ) L H H  allowed

We use approximate dynamic programming to solve the above model. Compared with the traditional dynamic programming algorithm, the approximate dynamic programming algorithm can continuously update and adjust the strategy according to the real-time data, can better cope with the dynamic changes and uncertainties of the problem, and can solve the problem of dimensionality explosion. Approximate dynamic programming uses a function of one parameter to approximate the state value function.

length ˆ( ; ) LUMI( ) ( ) U s s CI s          (31) 1 2 3 length max

Among them, 휃1, 휃2, 휃3 are learnable parameters, and their update process is as follows.

(32)   2   ˆ ˆ   ( ; ) ( , ) ;  U s r s a U s               

关注数学模型 Regarding the state transition conditions, we consider the impact of action a on the network availability index CI.

(33)    , CI s  f V  E  

Where 푓(푉', 퐸') is the connectivity calculated for the latest node set and edge set. The probability of connectivity change after executing action a is as follows.

(34) length   , max( ( ) ( ) )  P s s a soft LUMI s CI s          ∣ 1 2 3 length max 微信公众号：数学模型 When the action satisfies the constraints, the probability of change approaches 1, and when the action does not meet the constraints, the probability of change approaches 0.

The path selection strategy will be updated in real time according to the current situation, tending to select high-quality actions.

(35)      ˆ  ( | ; ) arg max ( , ) , ;    a s r s a P s s a U s       ∣   A a     S s 

7.4 Solution

微信号：MATHmodels

Through the calculation of community traffic availability, several areas with low availability scores were identified. As shown in the figure, this community has low traffic availability. It can be observed that a certain area of the community is surrounded by highways, which makes it inconvenient for residents in the area to travel. In response to this problem, the following improvement plans are proposed: first, build a highway connecting the area with other areas of the community; second, add a highway exit. Based on these two goals, the approximate dynamic programming method is used to solve the construction locations of the two plans, and the final results are shown in the blue box in the figure.

This project has a great impact on the lives of the people of Baltimore.

a. For local residents, the project to break regional isolation will undoubtedly make their travel more convenient.

b. For entrepreneurs, the impact has both advantages and disadvantages. After the project is completed, the optimized highway will improve logistics and transportation efficiency and expand the reachable range. In addition, more convenient transportation may stimulate real estate development in the area and increase land value, so it may increase revenue. The biggest disadvantage is that it may cause highway congestion during construction. In the long run, for local governments, the project requires research and development funds and long-term maintenance, which may increase financial pressure.

c. In the past few years, traffic congestion has spread across the country, billions of hours of time and productivity have been lost due to detours and traffic jams, and civil lawsuits regarding traffic accidents have taken up the court system's time. If our model can be promoted and applied, the city's transportation network can be effectively rebuilt, greatly alleviating the problem of traffic congestion and reducing people's unnecessary time. At the same time, the optimization of traffic roads is beneficial to the appearance of the city, beautifying the urban landscape and improving the quality of life of urban residents.

8 Model Application for Security

Traffic accidents occur frequently in the United States, which has caused serious damage to the interests of stakeholders. Relevant data show that the congestion level and the number of traffic accidents in the United States are on the rise.

In order to effectively protect the interests of stakeholders, we have summarized the indicators of the three models and designed a software that can view the traffic conditions in Baltimore in real time, help to understand traffic dynamics in a timely manner, and reduce the occurrence of traffic accidents. This software contains the following four modules:

关注数学模型 The first module can monitor structural changes and establish inspection cycles. The second module can analyze real-time data to predict possible traffic congestion and dangerous areas ,then remind users. The third module can connect emergency service departments through the platform once a traffic accident is detected, the system will automatically send a reminder mess age to residents within a certain range around the accident site by diversified ways Th e fourth module provide safety education focusing on the traffic safety awareness.

微信公众号：数学模型 微信号：MATHmodels

9 Sensitivity Analysis

In order to explore the impact of service radius on bus coverage and verify the rationality of parameter selection, we conducted a sensitivity analysis on the constant 푑 representing the service radius of bus stops in the planning model. The service radius was adjusted from 100 meters to 600 meters in steps of 20 meters, and the bus coverage corresponding to each service radius was calculated. The results are shown in the figure.

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m The bus coverage rate is sensitive to changes in the service radius. In the range of 100-480 meters, the coverage rate increases significantly with the increase of the service radius; after exceeding 500 meters, the coverage rate approaches the theoretical maximum value, and the growth slows down and enters a plateau period, indicating that expanding the service radius within a certain range can effectively improve the coverage rate, and the effect of exceeding the critical point gradually weakens.This study has practical significance. Expanding the service radius can reduce the cost of station construction, but the time for residents to walk to the station will become longer. In order to balance the construction cost and the interests of residents, the service radius corresponding to the midpoint of the coverage rate is selected for modeling, and this parameter selection is reasonable.

10 Model Evaluation

10.1 Strengths

Visualization: We used a reasonable visualization method to make the traffic conditions in Baltimore more intuitive.

Authenticity: For each traffic project before and after optimization, the traffic conditions before and after optimization were evaluated by simulating real scenes.

Innovation: The queuing theory was innovated in combination with the specific conditions of the model; the A* algorithm was combined with the genetic algorithm to enable the algorithm to obtain the global optimal solution for the shortest path.

10.2 Weaknesses

Although approximate dynamic programming can effectively solve the problem, the time complexity of the algorithm is high and it takes a lot of time to solve it.
