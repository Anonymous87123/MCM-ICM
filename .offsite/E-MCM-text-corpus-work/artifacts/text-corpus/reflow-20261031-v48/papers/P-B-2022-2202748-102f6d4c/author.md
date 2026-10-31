Problem Chosen 2022

MCM/ICM

Summary Sheet

As drought worsens in the western United States, the Colorado River, the lifeline of the Southwest, is in dire straits. In the Colorado River basin, it is important to allocate water wisely. This paper aims at measuring competing interests of different users in different states and making a water and hydroelectric power allocation plan suitable for different environmental conditions.

Two models are mainly established: Model I: Water and Electricity Transportation Model； Model II: Coordinated Development of Multi-objective Programming Model.

Before all the models are established, we analyze the reservoirs of the Glen Canyon dam and Hoover dam, get the relationship between water height in the reservoir and the volume of water in the reservoirs.

For Model I: In order to reasonably allocation water and electricity, we set up a Transportation Model of water and electricity. The objective function is the minimum supply of water from the two dams. The constraint conditions are mainly the constraint of minimum generating water level on supply and the constraint of demand on supply.

By analyzing the geographical position and topography of five states, the Glen Canyon dam and Hoover dam, we get the relationship between water flow direction and water resource transfer between the two dams, which reflects the water supply situation. After analyzing the loss of water and electricity during transportation, the final constraint conditions are obtained. Then, we designed the Maintenance Time Calculation Algorithm to solve the longest time to maintain the demand without the addition of additional water. Finally, we assign the initial water level of Lake Powell and Lake Mead to the numerical result Section 5.4.

For Model II: This Model is a further extension of Model I, which balances the competing interests of industry, agriculture and residents in five states. The supply of water is reflected in three aspects: Social effect, Economic effect and Environmental effect. The supply of electricity is reflected in Social effect and Economic effect.

When the situation of water shortage does not occur, we mainly consider the Economic effect of industrial, agricultural and residential use objects in five states. When water shortage occurs, we combine three effects to carry out multi-objective planning. See Section 6.3 for the results.

Additionally, we have taken into account the rights and interests of Mexico and propose an allocation plan for Mexico under the condition of different water resources remaining.

Finally, sensitivity analysis includes the influences of the changes over time in the demand for water and electricity of three types of objects (industry, agriculture and residents), the development of renewable energy technology and water and electricity conservation measures.

1 Introduction

1.1 Background

"Please join me and the people of Utah, regardless of religion, in humbly praying for rain for one weekend," Utah Governor Spencer J.Cox said in a video plea on June 4, 2021.[1] "The 'water shortage era' in the Western United States has officially arrived," Xinhua News Agency reported in Los Angeles on August 18.[2] The Colorado River[3] originates in the Rocky Mountains of Colorado in the United States, with a length of more than 2,300 kilometers. Its main stream flows through Utah, Arizona, Nevada, California and Mexico, and finally empties into the Pacific Ocean. The Colorado River forms the largest water system in the Western United States -- known as the "lifeline of the Southwest" because it flows through vast arid and semi-arid areas.

As can be seen from the Figure 1, the drought in the western United States has been severe. Actually, as early as the summer of 2021, it was reported[1] that lake Mead, the Hoover Dam that provides water to 25 million people in western States, was at historically low levels On June 9, the water level dropped to 1,071.57 feet, breaking the previous record low set in 2016. Climate change has reduced the amount of snow flowing into the Colorado River and its tributaries; Warmer temperatures are also making soil thirstier and increasing evaporation as rivers flow through arid areas of the western United States.

In the western part of the United States, in the Colorado River basin, two artificial lakes, the Lake Powell and Lake Mead, correspond to two dam (Glen Canyon and Hoover Dam) reservoirs. Water from the two dams is needed to meet the water and electricity demands of five U.S. states, Arizona (AZ), California (CA), Wyoming (WY), New Mexico (NM), and Colorado (CO), with extra water flowing into Mexico from the Colorado River into the Gulf of California.

1.2 Restatement of the Problem

The strained distribution of water affects competing interests in various regions. Through the analysis and investigation of the background and negotiators’ guidance of the problem, the restate of the problem can be expressed as follows: ⚫Build a mathematical model to solve the problem of water allocation under the condition of fixed supply and demand conditions.

✓Given the initial water level of the two lakes, figure out how much water should be drawn from each lake to meet the water and electricity demands.

✓In the absence of additional water supply, and the demands are fixed, solve for the maximum maintenance time that the demands can be met.

✓Figure out how much additional water must be supplied overtime to ensure that these fixed demands are met. ⚫Establish a model to determine the allocation of water for general (Agricultural, Industrial, Residential) usage and electricity production among five states, and describe the criteria for resolving competing interests. ⚫Based on the model, improve the solution in the case of water shortage, so that it can meet all the water and electricity demands. ⚫Analyze the changes in model results according to the following situations:

✓As the demands for water and electricity change over time, population, agricultural, and industrial change.

✓The initial value of renewable energy technologies increases.

✓Measures are taken to save water and electricity. ⚫Summarize the findings and prepare a one - to two-page article to submit to Drought and Thirst magazine.

1.3 Our Work

The problem requires us to work out a reasonable allocation plan for water and electricity demands of three categories of objects (industrial, agricultural and residential) in five states, and for different environmental conditions, considering the needs of Mexico. Our main work is as follows: 1) In the case of a certain demand, the Water and Electricity Transportation Model is established by analyzing the transportation of water and electricity and the water transferred between two lakes.

Figure out the daily supply of water for the two lakes, the maximum maintenance time without additional water, and the additional water needed to meet demands. 2) The Coordinated Development of multi-objective Programming Model is established by considering the water and electricity demands of industry, agriculture and residents from three perspectives of society, economy and environment. The distribution of water and electricity when water resource is sufficient and water resource is tight is analyzed respectively. 3) Based on the above two models, the Mexican Allocation Model is established to consider the distribution of Mexico's interests. 4) The sensitivity of the model was analyzed from the perspectives of demand and renewable Energy Technologies.

2 Assumptions and Justifications

In order to build the mathematical model to solve the problems, we make the following supplementary assumptions on the basis of the problem, following a reasonable explanation for each

assumption

⚫ Lake Powell and Lake Mead are the reservoirs of Glen Canyon dam and Hoover Dam, respectively. These two lakes are artificial lakes and the distance between the reservoir and the dam is very close. Due to the theory of communicating vessels, the lake water height can be considered as the water height of the upstream of the dam, and the error can be ignored. ⚫ The dam will not overflow due to conditions such as a breach. The main trend of climate change is the decrease of precipitation and the increase of temperature, and water resources are strained, so the overflow situation is not considered. ⚫ The lowest water level for power generation is the lowest water level allowed by the reservoir.

After a data search, we set the lowest water level at 3,490 feet for Lake Powell and 950 feet for Lake Mead.

⚫ The supply of electricity in the states is only hydroelectric. In order to simplify the model and reduce the burden of data search, only hydroelectric power is considered. ⚫ The water can be reused, and all the water that flows through the dam generates electricity.

Based on resource reusability, this assumption is more realistic. ⚫ Consider the effects of rainfall, temperature changes, and river evaporation. Climate change has reduced the amount of snow flowing into the Colorado River and its tributaries; Warmer temperatures are also making soil thirstier and increasing evaporation as rivers flow through arid areas of the western United States. The consideration of evaporation is necessary and reasonable. ⚫ The water transferred from Lake Powell into Lake Mead and then supplied to users is deemed to belong to Lake Mead. ⚫ The supply of water depends on rivers. In practice, each region follows the "proximity principle" for water resources, that is, only the main stream or tributaries flowing through the region can be used for water. Electricity transportation is related to the geography of the five states. ⚫ Electrical energy is lost because of the thermal power generated by the resistance of the wire.

Transporting electricity from the same dam causes states farther from the dam to generate more power and lose more than states closer to the dam. As the state Wyoming is far from the dam, it is necessary to consider the power loss.

3 Notations

The important symbols used in this article and their meanings are shown in Table 1. There are some variables that are not listed here and will be discussed in detail in each section.

Symbol

Description l The height of the water level of a reservoir v Volume of water in a reservoir

W Total volume of water supply suply

Volume of water supplied from Reservoir i to State W j j = ( 1,2, ,5) ij

W Volume of water lost through transport loss

Electricity demand (transferred to the volume of water) in D j j = w State ( 1,2, ,5) j

j j = D Water demand in State ( 1,2, ,5) je

Supply for m (water or electricity) from source i to k k = ( 1,2,3) object (industrial, agricultural and km ijx j j = residential) of State ( 1,2, ,5)

Demand for m (water or electricity) of object k k = ( 1,2,3) (industrial, agricultural and residential) in km D j j j = State ( 1,2, ,5)

4 Model Preparation

4.1 Data Collection

The problem doesn't give us data, so we need to collect data to build a model. To analyze the problem, we need to collect data on two lakes and dams, as well as the water and electricity demands of agriculture, industry and residential use in five states. After the data is collected, certain processing and analysis are carried out to prepare for the subsequent model establishment.

The official websites of the two lakes and dams provide us with a lot of data about the dams. Detailed data sources are shown in the Table 2 below. (Additional data sources are included in the Reference.)

Database Names Database Websites

Lake Powell http://lakepowell.water-data.com/

Lake Mead http://lakemead.water-data.com/

Electricity Consumption https://www.eia.gov/electricity/state/

4.2 Relationship between Water Level and Storage Volume

Lake Powell and Lake Mead are the reservoirs of Glen Canyon Dam and Hoover Dam respectively. The higher the elevation of the lake, the larger the content of the reservoir. After analyzing and studying the water level of the two lakes in the past 12 months (data sources are shown in the Table 1), we conclude that there is a linear correlation between the elevation and content of the lakes.

Therefore, we perform polynomial fitting analysis on elevation and content, and the steps are as follows:

Step1: Take a set of data points, including m, as sample points

{( , l v )( , l v ) ( , ) l v ( , l v )} (1) 1 1 2 2 i i m m

= where ( il i 1,2, , m ) represents the height of the water level of a reservoir corresponding to the sample = = iv i ( 1,2, , m ) point ( i i 1,2, , m ) , namely the elevation of the lake; represents the volume of water in a reservoir, namely the content of the lake.

Step2: Use polynomial for curve fitting − − = + + + + + n n 1 n 2 ˆ v a l a l a l a l a (2) − 0 1 2 n 1 n

n degree polynomial; ˆv is the predicted value. th na represents fitting coefficient, stands for where Step3: Calculate the sum of squares of residuals

m   = − 2 ˆ( v v ) (3) i i = i 1

We use MATLAB for polynomial fitting of elevation and content, and the results are as follows

After many times of curve fitting, we find that the fitting effect of quadratic polynomial is more ideal. As can be seen from Figure 2, sample points of Lake Powell and Lake Mead are relatively close to the fitting curve. The relationship between water level and volume of the two reservoirs is as follows = − + 2 6 9 v 224.26 l 1.5157*10 l 2.5622*10 powell (4) = − + 2 5 8 v 338.64 l 6.719*10 l 3.4155*10 mead

We verify the function by comparing the predicted value with the actual value. According to Wikipedia, Lake Powell[5] is 3,700 feet above sea level and has an active capacity of 20,876,000 acre-feet with a fitting value of 24,229,400 acre-feet; Lake Mead[6] has an elevation of 1221.4 feet and an effective capacity of 26,120,000 acre-feet with a fitting value of 26,080,000 acre-feet. From the numerical point of view, the fitting effect is ideal.

5 Model I: Water and Electricity Transportation Model

5.1 Basic Ideas

In the basin of the Colorado River, Lake Powell and Lake Mead are two water clusters. The two lakes are at higher elevations and water can flows from them to the surrounding areas. Additionally, Lake Mead has a higher elevation than Lake Powell. So the water flows from the Glen Canyon Dam (Lake Powell) to the Hoover Dam (Lake Mead) and eventually to the Gulf of California.

The geographical map is shown in Figure 3.

Demands includes water demand and electricity demand, which includes agriculture, industry and residents in five states.

1. Water supply: It is assumed that each region draws water from the river that flows through it, and this water can be traced back to Lake Powell or Lake Mead. Among them, part of the water of Lake Powell will be supplied to users after flowing into Lake Mead, which is regarded as belonging to Lake Mead. In the process of water transportation, the hydraulic loss caused by evaporation is mainly considered.

2. Electricity supply: hydroelectric power is to convert the potential energy of water into mechanical energy and then into electrical energy. Similarly, we can also transform the loss of electric power in the transmission process into the loss of water potential energy, thus producing constraints on reservoir stock.

The problem is thus simplified to two lakes distributing water resources to the five continents. The distribution of the three industries (agriculture, industry and resident) will be discussed in detail in the Section 6.

In the case of water demand and electricity demand are certain, we can make a reasonable allocation of water resources through Transportation Model.

5.2 Establishment of Transportation Model

5.2.1 Objective Function

In order to make full use of water resources, we hope that the water supply from the two dams will meet the water and electricity demands of each state while providing as little water as possible

2 5 = = + min W W W W (5) suply 1 2 ij = = i 1 j 1

W is the water supply from the Glen Canyon W where represents the total volume of water supply, 1 suply W is the water supply from the Hoover dam. W means the volume of water supplied from dam, and 2 ij i i = j j = Reservoir ( 1,2) to State ( 1,2, ,5) . If there is no corresponding river flowing through, then W = 0 . ij

W For a lake, water supply can be divided into two types: water supplied directly without the dam , iup i = represents the Glen Canyon dam, i = W 1 2 and water supplied through the dam . ( represents the idown Hoover dam).

Considering that some water will flow to Lake Mead after Glen Canyon dam, we set the volume of  , where  is a proportional parameter. Additionally, it is W this part of transferred water as 1down W after being transferred. assumed that the transferred water is included in Lake Mead's water supply 2 Thus, the water supply can be expressed as follows = + −  + + W W (1 ) W W W suply 1 up 1 down 2 up 2 down (6) 2  = + −  ( W W ) W iup idown 1 down = i 1

W For dam i , includes the water provided to users by lake i after the dam, which is constrained idown D and electricity demand D , namely by users' water demand (transferred to the volume of water) e w  + W max{ D D } (7) idown e w

The relationship between water and electricity conversion and the loss of water and electricity during transportation will be discussed in detail in Section 5.2.3.

5.2.2 Supply constraints

The water supply must not exceed the minimum level of the reservoir, otherwise there will be no electricity supply. It is assumed that the lowest water level is the minimum content of reservoir.

Therefore, the water supply by Glen Canyon dam  W Q (8) 1 G

W represents the water supplied by the Glen Canyon dam, and Q represents the reservoir where, 1 G content of the Glen Canyon dam.

For Hoover Dam, its water supply  +  W Q W (9) 2 H 1 down

W represents the water supplied by the Hoover Dam, and Q represents the reservoir content of where, 2 G  is the water transferred form Glen Canyon dam to Hoover Dam.  is a W the Hoover Dam. 1down parameter, which indicating the loss of water during the transportation (the details are discussed Section 5.2.3)

5.2.3 Demand constraints

Demands are divided into water demand and electricity demand. Our solution needs to meet both needs on five continents. ⚫ Electricity demand When the volume of water in the reservoir is small, the corresponding water flow will decrease. When the water level is low enough, it can even shut down power generation.

For hydraulic power generation, the formula[7] of translational power of turbines is as follows

= =  +    E f W ( ) ( )( V g h t ) (10)

where E is electric energy and W is the volume of the water, which means the relationship between Potential energy and electric energy of water.  +  is the coefficient of efficiency (a unitless, scalar coefficient, ranging from 0 for completely inefficient to 1 for completely efficient).  represents the function of the renewable energy technologies enhancement.  is the density of water. V is the  is the change in height. t  represents the volumetric flow rate. g is acceleration due to gravity. h working time.

The generation height difference is the current water level minus the lowest water level.

 = − h P P 1 min (11)  = − h M M 2 min

P where P is water level in Lake Powell, is the lowest generating water level of the Glen Canyon dam, min M M is water level in Lake Mead, and is lowest generating water level of the Hoover dam. min

The electrical energy will be lost during transmission due to the resistance of the wire   2 I ' L t ij i = E (12) loss s ij

Thus, additional water supply is available because of the loss of electrical energy, which is denoted W by . For electricity, supply needs to meet demand, expressed as follows eloss

2 2   −  W W D (13) down eloss e ij ij j = = i 1 i 1

W where can be obtained by combining the Formula (10,12). eloss

⚫ Water demand The transportation of water depends mainly on river systems. Rivers are largely exposed to sunlight and are greatly affected by evaporation. Evaporation is greatly affected by temperature. Therefore, the loss of water during transportation can be expressed as follows

 Td =  (14) W W ij wloss ij ij

 Td j j =  W represents the volume of water supplied from Reservoiri to State ( 1,2, ,5) where , and is ij ij the evaporation coefficient affected by temperature.  and  are parameters. T is the temperature. d is ij the distance from Reservoiri to State j .

It is assumed that the water will still be available to users after the electricity is generated. Therefore, the transport loss of water and electricity should be considered comprehensively when considering the provision of water = + (15) W W W loss wloss eloss ij ij ij

For water, supply needs to meet demand, expressed as follows

2 2   −  W W D (16) down loss w ij ij j = = i 1 i 1

5.2.4 The model summary

By summarizing the objective function and constraint equation above, we can get the following water and electricity transportation model.

2 5 = W W min (17) suply ij = = i 1 j 1

st. .

 2  = + −  W ( W W ) W  suply iup idown 1 down  = i 1  +  W max{ D D } idown e w   W Q  1 G   +  W Q W  2 H 1 down (18) 2 2    −  W W D  down eloss e ij ij j = = i 1 i 1  2 2    −  W W D  down loss w ij ij j = = i 1 i 1   W 0  ij

See the Formula (6-16) for a symbolic explanation.

5.3 Maintenance Time Calculation Algorithm

In order to solve the maximum maintenance time without additional water, we designed an algorithm to calculate the maintenance time.

The idea of this algorithm is to repeatedly iterate Model One to solve how long the water in two reservoirs can last without considering the external water supply.

The pseudo-code for the algorithm is as follows:

Algorithm: Maintenance Time Calculation Algorithm

P M W i [ ][ ] j , demand, n←0 Input: P , M , , , min min

Output: n 1  /*calculate the height and volume of water in the reservoirs base based 2  on the fitting function*/

P M 3  while P ≥ or M ≥ do min min

4 n ⟵n + 1;

5    cost ⟵ 0;

6 for i←0 to 1 do 7        for j←0 to 4 do if demand> 0 then 8 W i [ ][ ] j ∗𝛼 + E[i][j]∗𝛽; cost ← cost + 9

W i [ ][ ] j ∗(1 −𝛼) −E[i][j]∗(1 −𝛽); demand ← demand− 10

11       end 12    end 13    if cost = min{cost} then P ←P which is calculated based on the volume 14

M M ← which is calculated based on the volume; 15 min

16  end

The parameters to be input are: the initial water level heights P and M of the two reservoirs, and P M the lowest power level heights and . W is a matrix, and if there is no viable waterway from min min W i [ ][ ] j is initialized to 0. Demand D. The number of days n persisted is reservoir i to state j , then initialized to 0.

The parameters in the model are: calculated waterway transport loss α, calculated circuit transmission loss β, W matrix element represents the amount of water transported from reservoir i to state j, similarly, E matrix element codes the amount of electricity generated from reservoir i to state j .

Solution and output of the model: According to Model One, the reservoir water consumption required to meet the demand and guarantee the minimum loss can be obtained each time. The corresponding water level of the reservoir is calculated according to the fitting curve. If the water level of both reservoirs is lower than the lowest power generation water level, it indicates that the reservoirs can no longer provide electricity, that is, they can no longer meet the demand. The algorithm exits, and the number of days n is output.

5.4 Calculation Results

5.4.1 The water drawn from each lake

= P 3600 feet We assign values to the initial water levels of Lake Powell and Lake Mead. and = M 1210 feet .Based on past data, we assume that water demand is 43,411 million gallons and electricity demand is 1,073 gigawatt hours.

We analyzed the problem on a daily basis. Using the model, we get a total water supply of 59,467 million gallons. The water should be drown from Lake Mead: 41,602 million gallons, The water should be drown from Lake Powell: 17,865 million gallons.

After a day of use, the water level of the two lakes changed by 0.45 feet and 1.55feet respectively. The results are reasonable.

5.4.2 Maintenance time

In the absence of additional water supplies (e.g. rainfall, etc.), water levels will decrease over time. When the water level drops to the lowest generating level, the reservoir can no longer provide electricity, that is, it cannot meet the demand. The maximum maintenance time is from the initial water level to the lowest water level.

On the basis of the previous result, combined with Model One and Maintenance time Calculation algorithm, the solution is obtained as 63 days.

5.4.3 Additional water

Additional water is needed to keep the supply system going when it reaches a critical state where demand cannot be met. At this point, the demand is certain, and the water in the reservoir is a constant value, equivalent to the supply of water is the additional water, so there is little difference in the results. The difference is that the model is based on time lines, and the actual temperature we consider will lead to different evaporation losses, so the actual amount of additional water that needs to be replenished will also be different. The calculation results are shown in the figure below:

The amount of water that needs to be replenished is positively correlated with temperature, and the higher the temperature, the higher the loss, and the more additional water needs to be replenished.

6 Model II: Coordinated Development of Multi-objective

Programming Model

Model Two is a further improvement on Model One. In model One, we only distribute the water supply and electricity supply among each state. In Model Two, we take into account the proportion of water consumption by industry, agriculture and residents.

6.1 The Establishment of Multi-objective Programming Model

6.1.1 Objective function

The proportion of water and electricity used by industry, agriculture and residents will ultimately have social, economic and environmental implications.[8] Our goal is to harmonize social, economic and environmental development. The social, economic and environmental conditions correspond to the situation before, during and after the use of water. Electricity before and during use corresponds to this society and economy respectively. ➢ Social effect refers to the lack of water (or electricity) when the demand is not met. In other words, the social benefit refers to the negative effect caused by the lack of water (or electricity). When there is no water shortage, social benefits are not considered in the objective function. ➢ Economic effect refers to the industrial output from water (or electricity). The supply for industry, agriculture and residents in an area affects the economic situation of the area to varying degrees. ➢ Environmental effect refers to the amount of pollutants that water brings with it after use. From the perspective of environmental sustainability, we want the total amount of pollutants to be as small as possible.

= F opt f x [ ( ), f ( ), x f x ( )] (19) 1 2 3

x k = kf ( )( 1,2,3) where, correspond to social, economic and environmental implications respectively.

Water supply and demand affect all three effects simultaneously, whereas electricity supply and demand affect only the social effect and economic effect.

f x 1( ) ⚫ Social effect

i = i = There are three main sources of water supply: Glen Canyon dam ( 1) , Hoover Dam ( 2) and i = i = rainfall ( 3) . There are two sources of electricity supply: Glen Canyon dam ( 1) and Hoover Dam i = ( 2) .

When the supply cannot meet the demand, the water (or electricity) shortage is the quantity demanded minus the supply. We want the social effect to be as small as possible.

I m ( ) 2 3 5   = − − km km max f x ( ) min [ D x ] (20) 1 j ij = = = = m 1 k 1 j 1 i 1

m = m = k = km 1 2 ) of object k (industrial 1 where is the demand for m (water or electricity , D j k = k = ) in State ( m = or j j = 2 3 km 1 1,2, ,5) agricultural and residential , is the supply for m (water ijx m = k = k = k = 2 ) to object k (industrial 1 2 3 electricity , agricultural and residential ) of State j j = ( 1,2, ,5) .

f 2( ) x ⚫ Economic effect

The economy mainly includes the value of water (or electricity) brought by water resources, and the benefits brought by the utilization of water (or electricity).

The value of water (or electricity) brought by water resources is directly reflected in the charging system of hydropower, which is expressed by the charging coefficient c . The benefits brought by the utilization of hydropower are expressed by the benefit coefficient b . For example, for a factory, its utilities can be reflected in the charging coefficient, its profit can be reflected in the benefit coefficient.

I m ( ) 2 3 5  = −  km km km m km m max f ( ) x max ( b c ) x w (21) 2 ij ij ij ij j j = = = = m 1 k 1 j 1 i 1

 km km km m where, is the benefit coefficient, is the charging coefficient, is the supply, is the order ijb ijc ijx ij  km m coefficient, is the fairness coefficient and is the regional tradeoff coefficient. w j j

The influence of three economic factors: the supply difference in different regions, the demand difference in different regions, and the demand difference in different industries in the same region.

The influence of water evaporation and power loss in the process of electric transportation are both constrained by distance. Each state is located at a different distance from the two dams, which determines the different priority of the two dams’ supply to the five states, expressed by order coefficient . The three types of objects (industry, agriculture and residents) are the three types of fixed demand groups of hydropower resources. Their demands are different, and the difference of their demand proportion is represented by fairness coefficient . The distribution of resources among the five states is expressed as regional tradeoff coefficient w.

The specific acquisition and method of the three coefficients will be introduced in detail in Section 6.2 combined with examples.

f 3( ) x ⚫ Environmental effect

After the use of water, there will be a large number of sewage discharge containing important pollutants (such as COD, BOD)[9], which will have a negative impact on the environment, such as the destruction of the ecosystem. The smaller the environmental effect, the better.

3 5 3   = − k k k max f x ( ) min d p x (22) 3 j j ij = = = k 1 j 1 i 1

k k = k ( 1,2,3) where jp is the pollutant emission coefficient of object (industrial, agricultural and j j = k residential) in State ( 1,2, ,5) , and d is the content of important pollutants (mg/L) in the amount j k k = ( 1,2,3) of water discharged by object (industrial, agricultural and residential) in State j j = ( 1,2, ,5) .

6.1.2 Constraints

The constraints of supply and demand can be followed by Model One, with some additional constraints due to the inclusion of social, economic and environmental factors in Model Two. ⚫ Demand constraint

Users will have maximum and minimum demand for water. Maximum demand refers to the maximum output of production capacity, that is, to achieve the maximum satisfaction of users. Minimum demand is what the user needs to maintain basic operations.

When the supply is greater than the maximum demand, it will cause the waste of resources. When the supply is less than the minimum demand, demand is not guaranteed. So, the supply and demand constraints are as follows

3    k k k D x D (23) j min ij j max = i 1

⚫ Pollutant constraint

The discharge of pollutants cannot exceed the maximum allowable total amount of pollutants

3 5 3    k k k k d p x M (24) j j ij max = = = k 1 j 1 i 1

k k = k ( 1,2,3) where jp is the pollutant emission coefficient of object (industrial, agricultural and j j = k residential) in State ( 1,2, ,5) , and d is the content of important pollutants (mg/L) in the amount j k k = ( 1,2,3) of water discharged by object (industrial, agricultural and residential) in State j j = k ( 1,2, ,5) M . is the maximum allowable total amount of contaminants, and the value is 5989kg max (total COG/day)[9].

6.1.3 The model summary

By summarizing the objective function and constraint equation above, we can get the following coordinated development multi-objective programming model.

= obj F X . ( ) opt f x [ ( ), f ( ), x f ( )] x 1 2 3   I m ( ) 2 3 5   = − − km km max f x ( ) min [ D x ]   1 j ij   = = = = m 1 k 1 j 1 i 1   (25) I m ( ) 2 3 5  = = −  km km km m km m max f ( ) x max ( b c ) x w   2 ij ij ij ij j j   = = = = m 1 k 1 j 1 i 1   I m ( ) 3 5     = − k k k max f ( ) x min d p x 3 j j ij   = = = k 1 j 1 i 1

st. .

  W Q 1 G   +  W Q W  2 H 1 down  3    k k k D x D  j min ij j max (26) = i 1  3 5 3     k k k k d p x M j j ij max  = = = k 1 j 1 i 1   k x 0  ij

See the Formula (8-24) for a symbolic explanation. More parameters are determined in the Section 6.2.

6.2 Parameters to Determine

Due to the limitation of paper space, it is impossible to list every case. Therefore, we take California as an example to explain the determination of each parameter in the model.

f 2( ) x

6.2.1 Parameters in economic effect

f 2( ) x : Benefit coefficient km There are five parameters in economic effect , Charging coefficient ijb   km m km m , Order coefficient , Fairness coefficient , and Regional tradeoff coefficient w . ijc ij j j

km ⚫ Benefit coefficient ijb

The benefits brought by the utilization of hydropower are expressed by the benefit coefficient.

The benefit coefficient of industrial and agricultural water (or electricity) can be determined by the reciprocal of the water (or electricity) demand of output value. According to the data we checked[11,12], we can get:

Benefit Benefit Total output value Total water volume Total Object coefficient(water) coefficient(electricity) /million dollars /million gallons electricity/KMWh dollars/gallons dollars/KWh

Industry 9,025,218 19183 47631.5 470.48 189.48

Agriculture 196037.6 399 6804.5 491.3223 28.80999

Domestic water (electricity) coefficient is generally difficult to have a clear value[8], in order to ensure the supply, we give a large value according to the Table 3. The benefit coefficient of water is 550 dollars/gallons, and the benefit coefficient of electricity is 200 dollars/kwh.

km ⚫ Charging coefficient ijc

The value of water and electricity brought by water resources is directly reflected in the charging system of hydropower, which is expressed by the charging coefficient.

The charging coefficient can be determined by the California unit price of water and electricity[13,14,15].

Industry Object Agriculture Residents Water price 3.77 2.12 5.85 (dollars/gallons） Electricity price 8.16 17.5 15.98 (cents/KWh）

 m ⚫ Order coefficient ij

The different priority of the three water sources’ supply to the five states, expressed by order coefficient.

The conversion of water (or electricity) use priority to order coefficient can be obtained from the following transformation relationship[8]:

+ − m m 1 n n max j ij  = m (27) ij I m ( )  + − m m (1 n n ) max j ij = i 1

m = (or electricity m = 1 2 m where, n represents the conversion of water ) use priority. ij

i = 1 For a given state, water is provided from three sources: Glen Canyon dam ）, Hoover Dam （ i = i = 2 3 ）, and rainfall ）. As the increase of transport distance will cause the loss of water due to （ （ evaporation, the priority is determined by distance. For California, rainfall is available in a very short period of time, and its distance to Hoover Dam is less than Glen Canyon dam. Therefore, the priority = = = respectively.  1 1 1 1 degree is rainfall first, Hoover second, and Glenn last, denoted by n 3, n 2, n 1 1 j 2 j 3 j ij (water) are 1/3, 1/2, 1/6 respectively.

i = i = 1 2 Electricity comes from two sources: Glen Canyon dam ） and Hoover Dam ）. As the （ （ increase of transportation distance will cause loss due to power loss, its priority is also determined by the distance. The degree of priority is: Hoover is the first, Glenn is the second, respectively expressed by = = , it is obtained that  (electricity) are 1/3, 2/3 respectively. 2 2 1 n 2, n 1 1 j 2 j ij

 km ⚫ Fairness coefficient j

Their demands are different, and the difference of their demand proportion is represented by fairness coefficient.

+ − km km 1 n n max j  = km (28) j 3  + − km km (1 n n ) max j = k 1

Water demand priority[16]: residential water first, agricultural water second, industrial water last, = = = . Substitute into the formula, and the water use fairness 11 21 31 corresponding to the order: n 3, n 2, n 1 j j j coefficients are 1/3, 1/2, 1/6 respectively.

Priority of electricity demand[17]: agricultural electricity consumption occupies a small part of electricity consumption, so we give priority to domestic electricity consumption, followed by industrial electricity consumption, and agricultural electricity consumption last. Corresponding:

= = = , plug into the formula, and the electricity fairness coefficient is 1/3, 1/6, 1/2, 11 21 31 n 2, n 3, n 1 j j j respectively.

m ⚫ Regional tradeoff coefficient w j

The distribution of resources among the five states is expressed as regional tradeoff coefficient.

Taking water as an example, we have data[10] on water use in five states. According to the data, the weight of the five states is shown in the following Figure 5.

f 3( ) x

6.2.2 Parameters in environmental effect

f 3( ) x : pollutant emission coefficient k There are two parameters in environmental effect jp ,and the k content of important pollutants d . j

Through data search[19], California's COD (or other pollutants) emissions k d 190mg/L, emission j k coefficient is 0.20. jp

6.3 Calculation Results

6.3.1 The answer to question two

In order to better represent the relationship between agricultural, industrial, residential water use and power generation, we assume that each state has sufficient water supply and rainfall of 1000 million gallons, calculate the optimal economic benefit, and obtain the distribution of hydropower resources in each state as shown in the table  below.

As can be seen from the table :(1) in most areas, agricultural and residential water use is relatively high. This is because (1) each state has a relatively large area of farmland and a high demand for irrigation water. (2) The priority of residential water is high. We give priority to residential water in the redistribution of water resources, so the proportion of residential water is relatively high.

As can be seen from the table, the proportion of industrial and residential electricity consumption is relatively high, while that of agriculture is relatively low. This is because (1) industrial output has a high demand for electricity, (2) residents are given priority to power consumption to ensure their living needs, and (3) the main demand of agriculture is water, which has a low demand for electricity.

6.3.2 The answer to question three

Question two considers resource allocation in the absence of water shortage. At this point, Economic effect is mainly used for consideration. The third problem is the consideration of water shortage, so the multi-objective planning with Social effect, Economic effect and Environmental effect is used. The guarantee rate is listed in the following table

f x 1( ) f 2( ) x f 3( ) x Guarantee rate /million gallons /million dollars /kg 50% 2071.65 37965.48 1235.68 75% 2748.52 34545.59 1396.32 95% 3107.47 28675.33 1731.43

In the process of the guarantee rate changing from 50% to 95%, the total water shortage increases, and the discharge of important pollutants in the state also increases, but the benefit value generated in the state decreases, that is, the improvement of regional economic effect is at the cost of the reduction of social effect and environmental effect. It shows that the three objectives are interacting and competing with each other in the established coordinated multi-objective programming model.

6.3.3 The re-run of the model

Considering the work of reservoir operation and dispatching in real life and the need to make corresponding adjustments after a certain period of time in the model, we run the model at an interval of one month. Each time you run the model, you get a month of scheduling data. In case of surplus and shortage, corresponding adjustment can be made next month.

7 Mexican Allocation Model

7.1 The Establishment of Mexican Allocation Model

The model is based on the allocation plan for Mexico after the reservoir allocation.

In either Model One or Model Two, after allocating resources to each state, if there are no resources =  remainRem 0 . (Rem 0 means insufficient resources, Rem=0 means just used up), then the model is not applicable. No allocation of resources to Mexico.

If there is surplus after allocating resources: consider allocating resources to Mexico. We take every month as the operation cycle of the model, run the model according to the data, and obtain the water consumption Req required by the United States in a month. Taking the estimated total amount of water minus the estimated monthly water consumption Req, we get Rem. This is where the model applies. The amount allocated to Mexico is μ*Req(calculated as a scaling factor multiplied by a month's demand from the United States).

We refer to the Logistic curve and set parameters to make it conform to our model:

1  = ( ) t (29)  − + − rt 1 ( 1) e m  0

7.2 Calculation Results

We use MATLAB to set the parameters to conform to our model and get the final parameter value = =1, = r = 1 0.0001 9.2 , . m 0 When the remaining Rem is very small and μ is close to 0, the resources allocated to Mexico are also close to 0. When Rem is greater than or equal to twice America's monthly demand Req, μ is almost 1, giving Mexico the amount of the United States in a month, i.e., giving Mexico the amount of the United States in a month at most. (The calculation period is one month). When Rem is exactly equal to Req, μ=0.5, giving the United States half of what it needs in a month.

8 Sensitivity Analysis

8.1 Change in Demand

Over time, demand for hydropower may rise or fall in various industries. At this point, we select industrial, agricultural and residential water consumption demand to increase by 5% on the basis of the original demand, industrial, agricultural and residential electricity consumption demand to decrease by 5% on the basis of the original demand, so as to explore the impact on the final result of our model solution.

It can be seen that the original proportion of residential water consumption is relatively large, and the water resource base used is relatively large. Therefore, when the industrial, agricultural and residential water demand increases by 5% respectively, the overall proportion changes greatly, and the residential proportion increases more. However, the original industrial proportion is relatively small. After the 5% increase in demand, it has little influence on the overall proportion, and the industrial proportion is also less adjusted. For electricity consumption, it can also be seen that the industry with a large original share will cause a large change in the overall share.

8.2 Renewable Energy Technologies

In our model, only the technological upgrading of hydropower generation in renewable energy technologies is considered for the time being. If considering wind power, solar power and other renewable energy technologies, you just add the power supply. In the first model, it is mentioned that the utilization efficiency of water energy conversion into electric energy is η+β, where η is the basic utilization efficiency, which is 80%.  represents the function of the renewable energy technologies enhancement., and the added value is assumed to be 5%, 10% and 15% respectively. The calculated water supply decreases with the increase of utilization efficiency. This is quite understandable because there is less extra energy lost, so there is less water to provide.

β 5% 10% 15%

Supply 55567 53722 52642

It can be seen from the data that after the increase of β in our model, the water supply decreased, but not significantly, indicating that the water use efficiency η+β has little influence on our model, which may be because the loss caused by evaporation is greater than that of water use efficiency.

8.3 Water and Electricity Conservation Measures

We believe that additional water and electricity conservation measures will lead to a reduction in residential demand for water and electricity. The need for less resources will keep the dam at a higher  is high), so the more demand water level, which will keep generating capacity at a higher level ( h decreases, the more water the reservoir provides. However, when the demand is reduced to a certain extent, the water level of the reservoir is high enough and there is little change, and the power generation capacity is basically stable. With the decrease of the demand, the reduced water provided by the dam also tends to be positively correlated.

9 Strengths and Weaknesses

9.1 Strengths

(1) The two main models used in this paper are universal and can deal with different supply and demand conditions and get better distribution schemes.

(2) Model Two comprehensively considers social effect, economic effect and environmental effect, which interact and compete with each other to improve the rationality of the results (3) In terms of water and electricity conversion and power loss, a large number of literatures are referred to ensure the rigor of the model.

9.2 Weakness

(1) In the model calculation, specific values of some parameters are not found, which may have certain influence on the results.

(2) Only hydroelectric power generation is considered in the model. If other power generation methods such as wind power generation are considered, the results will be more realistic.
