Summary

There are mainly three water problems in China: too little water in northern and northwestern part; too much floods in southern part; and too dirty water produced by industry and agricultural pollutants.

In order to address problems above and provide a thirteen-year water strategy (2013-2025) for the

leadership of China, we conclude five sub-problems and its solution in our paper: 1)Prediction of the supply and demand of water in a period of thirteen years based on historical data;2) Model building of national water storage and movement strategy to solve China’s uneven distribution of water in time and space; 3)Model designing of regional water de-salinization strategy to increase the total amount of available water;4)Model building of water conservation strategy, including regional water pollution treatment and national water-saving; 5)Long run cost-benefit analysis of four water strategies above and the discussion of the optimal combination of water strategies.

In first model, we choose the most appropriate Fitting Function. Using Grey Predicted Model, we can get the correlation degree between water consumption and population, industrial GDP and agriculture output. Then we successfully finger out the water demand in 2025 is 6770 hundred million m^3 by using GM prediction. In our second model, we use CV (coefficient of Variation) and water supply pressure 𝛛 as the decision-making index and work out a water storage project list by using Goal Programming. Based on cost and benefits analysis, we build Minimum Spanning Tree to work out the optimal water transfer plan. That is, we should transfer water from Yangtze watershed to Yellow watershed and Hai watershed. Besides, we devise a local water transfer strategy. In the third model, we build a set of parameters to describe the degree of water purification demand of each city and successfully get the water de-salinization plant building scheme. In the fifth model, we do long run cost-benefit analysis of four water strategies above. We first analyze weights of economic, physical, environmental implications by using AHP (analytic hierarchy process). Then we use Neural Network Algorithm to classify the quality of each strategy and finally get a reasonable strategy evaluation model.

In the whole modeling process, we give full consideration to validity, feasibility and cost-efficiency of our model.

1 Introduction

Water, the magic encounter between one hydrogen and two oxygen atoms, is vital for all kinds of life forms in the earth. The human body, myriad ecological systems and the big biosphere of our entire planet, all of these can’t live without the beautiful gift from our Almighty God. However, in many parts of the world nowadays, we human are facing severe water problems.

Take China for example. With more than 20 percent of world’s population but less than 7 percent of its freshwater, China is continuously facing issues associated with water. There are mainly three problems in China: too little water in northern and northwestern part of country; too much floods in southern part; and too dirty water produced by industry and agricultural pollutants. Furthermore, www.madio.net being a developing country, China has the responsibility to deal both the soaring water demand caused by booming economy and the increasing need to improve water consumption efficiency.

In order to address problems above and provide a thirteen-year water strategy (2013-2025) for the leadership of China, we conclude five sub-problems to tackle in our paper.

 Prediction of the supply and demand of water in a period of thirteen years (2013-2025) 数学中国 based on historical data

 Model building of national water storage and movement strategy to solve China’s uneven distribution of water in time and space

 Model designing of regional water de-salinization strategy to increase the total amount of available water

    Model building of water conservation strategy, including regional water pollution treatment and national water-saving

 Long run cost-benefit analysis of four water strategies above and the discussion of the optimal combination of water strategies

In the whole modeling process, we give full consideration to validity, feasibility and cost-efficiency of our model.

2 Nomenclatures

D The fresh water demand of a region S The fresh water supply of a region W The total amount of water resources of a region 𝐷nation The fresh water demand of whole nation The fresh water demand of whole nation U The groundwater resources of a region O The surface water resources of a region N The population size of a region GDP Gross Domestic Products www.madio.net g Real GDP per capita α The water supply pressure of a region 𝛼0 The national average water supply pressure β The water consumption per unit GDP C The capacity of a reservoir E The average construction costs of a reservoir η The actual benefit of a project 数学中国 ∆𝑂 The range of water resource in a certain period of time 𝑃𝑖 The number of a certain province in model two ∆𝑤𝑖 The amount of water a region can’t provide by itself 𝑏𝑖 The watershed attribute of the number i province 𝑒𝑖 The terrace attribute of the number i province (x, y) The geographical coordinates of a region’s capital city 𝑑𝑖𝑗 The distance between region i and j r The Earth Radius ω The edge weights of national water transferring network 𝐷0 The estimated water consumption in 2013 Θ The growth rate of water consumption p The desalinization cost of tons of seawater p0 The desalinization cost of tons of seawater in 2013 𝑡𝑜𝑝𝑡 The optimal time to build water purification plant σ The measurement of the seawater’s desalination cost 𝛾𝑘 Demand for water-pollution control degree of number k watershed 𝛼𝑘 The water supply pressure of a watershed Ⅰ The highest level of water quality The middle level of water quality Ⅱ The lowest level of water quality Ⅲ 𝜌𝑘 The ratio between the sum of Ⅰ ,Ⅱ and Ⅲ water of resources to the total water resources 𝜇𝑘,𝑗 Demand for Water-pollution Control Degree of the number j city in number k watershed 𝑘𝑗 Water Resources of the number k city in number j watershed 𝐶𝑘𝑗 The total COD in the city’s water of the number k city in number j watershed COD The chemical oxygen demand 𝑐𝑜𝑑𝑘𝑗 The emission of COD per year of the number k city in number j watershed Β The water consumption of a unit GDP

www.madio.net

3 Model one: Water demand and supply Forecast

(2013-2025) 数学中国

3.1 Introduction

In order to devise an effective water strategy, we firstly need to predict the total amount of water demanded and that should be supplied in 2013-2025. The water demand and supply forecast is the preparation work for models aiming to increase water resource. That is to say, our water storage and movement, water purification, conservation strategy are all based on the forecast of water.

3.2 Assumptions

 Assume that China's population and other policies don’t have sharp change in the 2013-2025  Assume that China maintains a steady economic growth from 2013 to 2025  Assume that the world’s climate don’t have dramatic changes from 2013 to 2025

3.3 Function Fit Model

To do water forecast, we apply Function Fit Model. First, we collect ten-year water resources data (2000-2010) from China Statistical Yearbook, including total water use, Industrial water consumption, Agricultural water consumption and Live water consumption. Considering the relationship between time and China’s total water use per year, we then build a Function Fit Model. Namely, we get the most approximate year-water-use function by minimizing the residual sum of squares. Then, putting the time value into the estimated function, we can predict the water demand and supply in next thirteen years.

3.3.1 Analysis of China’s water use

Based on data we have got, we can draw a 1997-2010 China’s water use table as shown below:

Water 1997 1998 1999 2000 2001 2002 2003 consumption 5566 5435 5590.88 5497.59 5567.43 5497.28 5320.4 100million m3 Water 2004 2005 2006 2007 2008 2009 2010 consumption 5547.8 5632.98 5794.969 5818.67 5909.95 5965.1545 6021.99 100million m3 www.madio.net Then, we can get a water consumption trends figure as shown below:

数学中国

From the figure above, we can see that the average water consumption per year from 1997 to 2004 fluctuates up and down around an intermediate value of 5500. And the deviation value of 2003, which fell sharply to 532 billion cubic meters, probably results from the drought happened in 2003 spring. After 2004, national water consumption per year rise steadily.

Using the Fit Function Model to fit the data, we firstly can get the Linear and Nonlinear Fit Function as shown below:

www.madio.net From the two linear and non-linear figures above, we conclude the Linear and Nonlinear Fit Function don’t achieve the ideal imitative effect. Thus, aiming to exclude the climate change factor which restricts water use, in the fitting process we abandon data with sharp fluctuations during 1997-2000, and finally find the real demand of China's water resources.

数学中国

The figure above shows results of three fitting methods: linear fitting, interpolant and power function fitting, and the table below shows the fitting degree of those three kinds of fitting methods.

Linear fitting Power fitting Interpolant fitting

y=59.35*x-113300 y=1.248e-066x^21.1 - Function 1.119e+005 1.086e+005 0 SSE 0.7759 0.7826 1 R-square 0.751 0.7283 - Adjusted R-square 111.5 116.5 - RMSE We can draw the conclusion that the first two fitting results are very close to each other.

3.3.2 Model Testing

Now, we need to test whether this Function Fitting Model is right. We find the data from “China's sustainable development of water resources in the Strategic Studies”. The data shows that the predicted water use in 2013 is 7000-8000 one hundred million cubic meters. Then we use our own model to predict the water use in 2013. Comparing these two kinds of data, we find our water use prediction is in great consistency with the data we have find in the report. That is to say, Our model is efficient to predict the probable water use in the future.

3.3.3 Prediction Results and Conclusion

Using the Function Fitting Model, we successfully predict the water demand in 2025. The results show in the table below:

www.madio.net Year Linear fitting Power fitting Interpolant fitting 2013 6166.41 6187.05 6201.94 2014 6225.76 6252.21 6264.81 2015 6285.12 6318.03 6329.02 2016 6344.47 6384.5 6394.48 数学中国 2017 6403.82 6451.64 6461.13 2018 6463.18 6519.45 6528.89 2019 6522.53 6587.95 6597.69 2020 6581.89 6657.12 6667.46 2021 6641.24 6726.99 6738.13 2022 6700.59 6797.56 6809.61 2023 6759.95 6868.83 6881.85 2024 6819.3 6940.81 6954.77 2025 6878.65 7013.51 7028.3

However, the confidence of the results obtained by the Function Fitting Model is not very high. We believe the reason lies in the fact that we only use data from 2000 to 2010. And it is difficult to do a thirteen-year prediction by using ten-year data. Because of China’s current rapid economic development, the growth of population and the speed of economic development is changeable. So we must take changes in social indicators into account to better predict water consumption.

3.4 Grey Forecasting Model

3.4.1 Reasons for Improvement

The result we get from Function Fit Model is not very ideal, and we believe the key reason lies in the lack of data. In other words, we only get the data from 1997 to 2010. So the fourteen-year data is too less to forecast the thirteen-year trends of future and the exact results is based on the fact that we have get the data of past forty or fifty years. In view of current situation, we devise a Grey Forecasting Model to get data with higher reliability, thus successfully overcoming the weakness of Function Fit Model.

www.madio.net The advantage of using Grey Forecasting Model is that we can get more reliable results with lacking accessible data, which perfectly fitted with our current situation. The total amount of water use is consists of agricultural, industrial, live water consumption, and these values are respectively relevant to agricultural GDP, industrial GDP and population, whose data of recent decades can be easily found in China Statistical Yearbook. Thus, if we quantify the interdependence coefficients between each consumption and respective production and the coefficients between production and its influencing factors, we can accurately predict the demand of water based on agricultural GDP, 数学中国 industrial GDP and population data of past decades we have got.

Food Production

Agricultrual Populaiton Water Consumption

Agricultural GDP

Water Industrial Water Industrial GDP consumption Consumption

Population Live water Consumption GDP

3.4.2 Correlation Degree Analysis

Calculation of Correlation Coefficient First, select a reference sequence as shown below:

𝑥0 = {𝑥0(k)|k = 1,2, … n} = (𝑥0(1),𝑥0(2) … , 𝑥0(𝑛)) And the other group of sequence is, 𝑥𝑖= {𝑥𝑖(k)|k = 1,2, … n} = (𝑥𝑖(1),𝑥𝑖(2)… , 𝑥𝑖(𝑛)), i = 1 … . m Then the correlation degree of xi to x0 is, 𝑛 𝑟𝑖= 1 𝑛∑ 𝑖(𝑘) 𝑘=1 in which, www.madio.net 𝑚𝑖𝑛 𝑚𝑎𝑥 𝑚𝑖𝑛 𝑚𝑎𝑥 |𝑥0(t) −𝑥𝑠(t)| |𝑥0(t) −𝑥𝑠(t)| + ρ 𝑠 𝑠 𝑡 𝑡  𝑖(𝑘) = 𝑚𝑎𝑥 𝑚𝑎𝑥 |𝑥0(t) −𝑥𝑠(t)| + ρ |𝑥0(t) −𝑥𝑠(t)| 𝑠 𝑡

Thus, we use ri to describe the correlation degree between xi and x0, namely to describe the influence on x0 caused by the change of xi.

Water Use and agricultural, industrial and live water consumption 数学中国 Water consumption is equal to the total amount of agricultural, industrial and live water consumption, but the influence contributed by each type of consumption to total amount is unequal. We define water use change in 10 years as sequence x0 while respectively defining agricultural , industrial and live water consumption as sequence x1，x2，x3. Then, we begin our calculation by using MATLAB. The figure below shows the relationship between water use and agricultural, industrial and live water consumption.

Putting water consumption x0, agricultural water consumption x1, industrial water consumptionx2, and live water consumption x3 into MATLAB, we can get results of correlation degree analysis.

www.madio.net 数学中国 Water Consumption Correlation Analysis Factors Associate degree(1) Sub-factors Associate degree(2) Agriculture water Food production 0.9388 consumption 0.9998 Population 0.9090 Agriculture GDP 0.6799 Industrial water consumption 0.9997 Industrial GDP 0.7053

Live water consumption 0.3746 Population 0.9022 GDP 0.7081

3.4.3 Thirteen-year water forecast based on Verhulst Model

In grey forecasting, we try to find and grasp the law of development of the fund data and at last make a scientific quantitative prediction for the future condition of the system by raw data processing and grey model building. Currently, the gray forecasting model GM (1,1) is the main application of grey forecasting, but GM (1,1) model is applicable to sequences with strong exponentially, and can only describe the monotonous process of change. The amount of water is a dynamic time-varying system with some random volatility, and therefore it is more suitable for us to use Verhulst model for non-monotonic swing development sequence.

3.4.4 Model Solution

We define X (0)as the original data sequence of the total water consumption in year 1997-2010:

(0) ⋯X X(0) = {X1 (0), X2 (0), X3 (0)} Then we can get the whitened equation of Verhulst model, dX(1) + aX(1) = b dt in which the X(1) is the accumulated generating operation sequence of X (0) . After that, we use the least square methods (LSM) to get the parameter a and b as:

α̂ = (a,b)T = (BTB)−1BTY in which,

(1) (0) -z2 X2 www.madio.net 1 1 (1) (0) -z3 X3 B= Y = ⋮ ⋮ ⋮ ] (0) (1) X -zn 1] [ [

(1) + Xk−1 (1) ), (1) = 0.5(Xk zk

The respective time response sequence of Verhulst model is: 数学中国 (0)(1) −𝑏 𝑎)𝑒−𝑎𝑘+ 𝑏 (1)=(𝑋 𝑎        𝑘= 1,2,3⋯,𝑛−1 X̂k+1

(0) by repeated decreasing: And we can get the reduced X̂

(0) = Xk+1 (1) −Xk (1) Xk+1

3.4.5 Model Testing

We test our model by residual analysis. Define gray forecast sequence as, X̂(0) = (X̂1 (0), X̂2 (0), ⋯, X̂ (0)) and residual sequence as (0) −X̂1 (0) −X̂2 (0) −X̂ ε(0) = (X1 (0), X2 (0), ⋯, X (0)) Then, we get relative error sequence:

∆= (| ε1 (0)| , | ε1 (0)| , ⋯, | ε1 (0)|) X1 X2 X Finally, we get the Average relative error sequence as shown below:

∆̅= 1 n ∑∆k k=1

3.4.6 Results and Conclusions

After model testing, we can use the Grey Prediction Model to give a more accurate prediction of water consumption from 2013-2025. The following figure and table shows the results of prediction.

www.madio.net Although the actual water consumption dropped drastically in 2003, the GM prediction results is relatively consistent to data in recent years.

Then we analyze the Residual Error, Relative Error, Limit Deviation Value of GM prediction, and 数学中国 the following table shows the results.

Year Actual Predicted Residual Relative Limit water water Error Error Deviation consumption consumption Value 5623.0 5623.0 0.0 0.0000 - 1997 5470.0 5440.6 29.4 0.0054 -0.0363 1998 5613.3 5484.9 128.5 0.0229 0.0176 1999 5530.7 5529.5 1.3 0.0002 -0.0232 2000 5567.4 5574.4 -7.0 0.0013 -0.0015 2001 5497.3 5619.7 -122.4 0.0223 -0.0210 2002 5320.4 5665.4 -345.0 0.0648 -0.0416 2003 5547.8 5711.5 -163.7 0.0295 0.0332 2004 5633.0 5757.9 -124.9 0.0222 0.0071 2005 5795.0 5804.7 -9.8 0.0017 0.0201 2006 5818.7 5851.9 -33.2 0.0057 -0.0040 2007 5910.0 5899.5 10.5 0.0018 0.0074 2008 5965.2 5947.5 17.7 0.0030 0.0012 2009 6022.0 5995.8 26.2 0.0043 0.0014 2010

By calculating Residual Error, Relative Error and Limit Deviation Value, we can prove the consistency between GM prediction result and the actual water consumption.

Then, we can predict water consumption of 2013-2025.

Year 2013 2014 2015 2016 2017 2018 2019 6143.9 6193.2 6243.5 6294.3 6345.5 6397.1 6449.1 Water Consumption Year 2020 2021 2022 2023 2024 2025 6501.5 6554.4 6607.7 6661.4 6715.5 6770.1 Water Consumption

According to GM prediction, water consumption will reach to 7039(hundred million cubic meters) while the government predict that the water consumption would not exceed 7000(hundred million cubic meter) “State Council, <<The views of the State Council on the implementation of the most stringent water management system>>, 2012)”

www.madio.net Therefore, the GM (1,1) Model is efficient and accurate.

4 Model Two: Water Storage and Movement

4.1 Terminology

数学中国 𝑾 The total amount of water resources of a region The total amount of water resources is approximately equal to the surface water plus groundwater (we do not consider repeated measures in statistics). We believe that, in the relatively short term, the changes in the water resources depends only on the impact of climate change over time, namely being in a dynamic equilibrium state. So we assume that in the relatively short period of time, total water resources is fixed, and we select the average amount of water resources of a spell as the representative of the amount of water resources.

W ≈U + O 𝑮𝑫𝑷 Gross Domestic Product GDP equals per capita GDP times population size, and the per capita GDP is an efficient measure for  economic development in a region. So GDP represents the combined effect of population size and economic development.

GDP = N · g 𝜶    The water supply pressure of a region α is the result of D divided by W. It stands for the ratio between the amount of water a region should supply and the total amount of water resources, so it is an efficient measure of ecological pressure on water resources in order to meet the water consumption demand.

4.2 Water Storage Model: Time Balancing Strategy of Water

Resources

4.2.1 Introduction

The goal of water storage is to solve the problem caused by the unevenly distributed water resources in different seasons and years. Namely, our goal in this part is to devise an efficient, reasonable, cost-efficient Time Balancing Strategy of Water Resources.

China's has been explored hundreds of years to work out efficient water storage projects, such as the Three Gorges Reservoir, the Ming Tombs Reservoir and Qiandao Lake Reservoir. However, due to www.madio.net the incompatible development of China’s economy in recent decades and some unscientific projects planning in the last century, and also the effects of climate change, some areas of China still suffer from sharp water fluctuations, and can’t solve the water shortage problem in the drought period.

4.2.2 Analysis

Water storage aims to solve the unevenly distribution of water over time, namely the dramatic water resource change in different seasons and years. Thus, we define the regional variation of the total 数学中国 water resources (W) as the standard measure of the need to build reservoirs, in which W ≈ U + O.

The Groundwater storage involves continuous improvement of the environment, like the increase of vegetation coverage rate, which is difficult to achieve through storage strategy. Besides, the under- ground water (U) makes up only half of the surface water (O). So in our model, we neglect the amount of underground water. In order to taking out the influence caused by the unevenly distribution of water resource in different regions, here we use the Coefficient of Variation (CV) to measure the degree of change of surface water resources.

CV = σ/μ where σ stands for the standard deviation of total water resource of a region μ stands for the mean of total water resource of a region The coefficient of variation (CV) is defined as the ratio of the standard deviation σ to the mean μ.

Based on the particular value of CV in one region, we can reasonably judge whether this region need a water storage project. Then, we go further towards the specific construction of a reservoir. We use E (The average construction costs of a reservoir) and C (The capacity of a reservoir) to do the cost-benefit analysis.

E = 𝐸0 · ω · log 𝐶 where 𝐸0 is the proportionality coefficient ω stands for the geographical factor’s impact on costs, like topography log 𝐶 stands for the size effect on the construction cost

C = k · [max(O) −min(O)] = 𝑘· ∆𝑂

k is the proportionality coefficient. And C must greater than a threshold 𝐶0, namely achieve an established scale in order to decide implementing a water storage project.

The actual benefit of a reservoir project η, η = 𝐶 𝐶 𝑘 ∆𝑂 𝐸= 𝐸0 · ω · log 𝐶= 𝐸0 · ω · log 𝑘+ log ∆𝑂

The equation above implicates that if the project’s costs is fixed, the greater ∆O, the higher actual benefits. www.madio.net

4.2.3 Model Solution

Based on China's actual conditions and data sources, we use provinces as the basis for zoning. The following is the water consumption of all provinces in China from 2000-2010. From the data, we can analyze the change of provinces’ surface water over years.

数学中国 The 2000-2010 line graph of surface water resources in China provinces Does it need? –determined by CV

Then, we calculate the CV(S) of provinces and divide them into three levels.

Level 1 Level 2 Level 3 0.0558087 Ningxia 0.206058 Shanghai 0.278128 Tibet 0.1150357 Inner 0.211229 Hainan 0.304979 Xinjiang Mongolia 0.1187557 Hebei 0.228055 Shanxi 0.320728 Sichuan 0.1285748 Hubei 0.234022 Jilin 0.341804 Guizhou 0.1610587 Zhejiang 0.242901 Jiangsu 0.351941 Yunnan 0.1727455 Shanxi 0.244948 Henan 0.414924 Qinghai www.madio.net 0.1778758 Beijing 0.248488 Shandong 0.415128 Gansu 0.1796035 Jiangxi 0.252123 Liaoning 0.527334 Hunan 0.1919238 Anhui 0.27147 0.574195 Guangxi Tianjin Guangdong 0.1923498 Fujian 0.274358 0.1925482 Heilongjiang 0.276789 Chongqing

From the table above, on the one hand, we can conclude that surface water resource change in the 数学中国 western provinces (Tibet, Xinjiang, Sichuan, Guizhou, Yunnan, Qinghai, Gansu, Guangxi and Chongqing) is less volatile and has the lowest water change level. So in general, we do not consider the construction of water storage projects in these provinces.

On the other hand, the surface water resources of the northern and eastern provinces (Shanghai, Jiangsu, Jilin, Henan, Shandong, Liaoning, Tianjin) is more volatile and has the highest level of water change over years. In order to address these regions' unevenly distribution of water resources, we should consider implementing storage projects in these areas.

Is it cost-saving?--determined by 𝜼

Taking the sequence of building water storage projects into consideration, it is not sufficient enough to decide whether to build a reservoir by only using CV. In other words, we need consider its economic factors. Thus, we take the region with both greater CV and η into our top priority list of implementing water storage projects.

Comprehensive Consideration

Considering both demand and economy, we get the following table:

∆𝐎 𝛈∝∆𝐎/ 𝐥𝐨𝐠∆𝑶 Province CV 0.206058 4.77 7.030023 Ningxia 0.248488 6.743545 8.13565 Beijing 0.574195 12.98 11.6593 Tianjin 0.278128 30.95 20.76261 Shanghai 0.228055 39 24.51189 Hebei 0.244948 49.7519 29.32085 Shanxi Inner Mongolia 0.211229 172.556 77.13965 0.415128 297.3048 120.2105 Shandong 0.320728 324.9316 129.3625 Shanxi 0.1150357 337.5545 133.5082 Xinjiang 0.351941 367.3848 143.2232 Jiangsu 0.341804 369.29 143.8399 Jilin 0.414924 413.3637 157.9936 Henan 0.527334 449.24 169.3661 Liaoning 0.276789 503.6865 186.4014 Heilongjiang 0.27147 624.9 223.513 Anhui www.madio.net 0.234022 679.33 239.8696 Hubei 0.242901 818.9488 281.1111 Zhejiang 0.274358 940.51 316.3118 Fujian 0.252123 1238.69 400.4866 Jiangxi

From the table above, we can finally figure out the province in which we need to build a water 数学中国 storage project in order to meet water demand in dry seasons. Henan, Liaoning, Heilongjiang, Anhui, Hubei, Zhejiang, Fujian and Jiangxi, these eight province need to pay special attention to water storage, because the building water storage in these area is both in urgent need and economically efficient.

4.2.4 Conclusion

In Time Balancing Strategy of Water Resources, we mainly focus on the uneven deployment of regional water resources in time, especially the surface water resources allocation. And finally figure out eight provinces in which we need to primarily implement water storage project. In our future work, we will consider some other factors. In terms of economy, we will take additive impacts of building a reservoir into consideration, like power generation, fish breeding. On the other hand, we will consider the role a reservoir play in redeploying water in different regions. That is to say, a water storage project has the ability to solving uneven water resource distribution not only in one region but in regions by being an end of inter-regional water transfer.

4.3 Water Transfer Model: Spatial Balancing of Water

Resources Strategy

4.3.1 Introduction

Our goal in Spatial Balancing of Water Resources Strategy is to solve inter-regional unevenly distribution of water resources in space. In other words, no matter what kind of season, wet or dry, if a region suffers from high water supply pressure all the time, we need to consider inter-regional water transfer.

Similarly, China has long history in solving the water movement problem. The Dayu Legend, which happened five thousand years ago, tells us the story of the first water movement project of ancient China. At that time, the water transfer project mainly aimed to solve the flood, but nowadays we build these projects to better meet the needs of human development and ecological conservation. Over the last decade, the Chinese government not only constructed large-scale water transfer project like South-to-North water diversion but also built local water transfer project like Dujiangyan Dam. Some projects are effective, but others remain to improve.

Therefore, in order to efficiently solve spatial problems, we must consider the following sub-problems:

 Geography and Topography  Watershed Delineation www.madio.net  Cost Accounting

4.3.2 Backgrounds and Water Movement Principles

Backgrounds In terms of Geography and Topography, distribution of the law of the terrain is low-lying West High East, was three-terrace, from west to east, gradually decline. So we can divide three types of terrace: 数学中国 first terrace (4000m above), second terrace (1000m-2000m) and third terrace (1000m below).

In terms of Watershed Delineation, China has nine watersheds: Songliao, Yellow River, Yangtze River, Hai River, Huai River, Pearl River, Southwest, Southeast and Northwest.

Figure China’s Nine Watersheds           Figure. China’s Three Terrace

The provincial administrative division in China gives full consideration to watershed delineation and terrace division, so we give each province a unique watershed attribute and a unique terrace attribute.

Water Movement Principle We should follow principles below to work out an efficient water movement strategy.

 We use inner-regional water transfer when water resource supply is complementary within a region

 We use inter-regional water transfer when most water resource supply within a region is too big or too small

 We only transfer water from high terrace to low terrace or in the same level of terrace

www.madio.net

4.3.3 Model Analysis

The basic 𝜶 Firstly, we choose the province as a basic unit because it’s relationship with Watershed Delineation and statistical convenience, and calculate water supply pressure  α of 31 provinces of mainland China.

数学中国 By calculatingα of each province, we can get the relative value of water supply pressure. In order to determine a reference, we define

𝛼0 = 𝐷𝑛𝑎𝑡𝑖𝑜𝑛 nation = 0.2 2 ⁄

as the national average water supply pressure. Then we can calculate the relative water supply pressure using the equation below.

∆α = α −𝛼0

∆α  stands for water supply difference between province and national average value.

If ∆α of a region greater than zero, we need to transfer water from other water-rich region to this region and vice versa. We divide  ∆α into five sections as shown in the following Figure.

Figure Classification of Water Supply Pressure www.madio.net Figure Colored Graph Based on  at r   pply pr    r  α

数学中国 From the figure above, we can conclude the overall water supply pressure trend: the eastern and northern have big pressure while western and southern have small pressure. However, in order to specify the problem, we need a more detailed model.

Other Parameters and Requirements

1) Parameters: Attributes of 𝑷𝒊

First we number 31 provinces of mainland china as shown in the following table:

i 1 2 3 4 5 6 7 8 Beijing Tianjin Hebei Shanx Inner Liaoning Jilin Heilo Province i Mongolia ngjia ng 9 10 11 12 13 14 15 16 i Shanghai Jiangsu Zhejiang Anhui Fujian Jiangxi Shandong Hena Province n 17 18 19 20 21 22 23 24 i Hubei Hunan Guangdon Guan Hainan Chongqi Sichuan Guizh Province g gxi ng ou

25 26 27 28 29 30 31 i Yunnan Tibet Shaanxi Gansu Qinghai Ningxia Xinjiang Province

Then we define each province 𝑃𝑖 has following four attributes, 𝑃𝑖(∆𝑤𝑖,𝑏𝑖, 𝑒𝑖, x, y)    𝑖= 1,2,3 ⋯31 in which, www.madio.net ∆𝑤𝑖 stands for the amount of water a region can’t provide by itself, ∆𝑤𝑖= 𝑤𝑖· (𝛼−𝛼0) = 𝑤𝑖· ∆α 𝑏𝑖 is the terrace attribute, which stands for the number i terrace in which the region situated 𝑏𝑖∈{1,2,3} 𝑒𝑖 is the watershed attribute, which stands for the number i watershed in which the region situated 𝑒𝑖∈{1,2 ⋯9} x represents altitude, y represents longitude, we use the coordinates of the capital city in 𝑃𝑖. 数学中国

2) Water Transferring Distance (𝒅𝒊𝒋)

We define the length of water transferring route from region i to region j as, 𝑑𝑖𝑗= r · arcco  [𝑐𝑜𝑠𝑦𝑖𝑐𝑜𝑠𝑦𝑗co (𝑥𝑖−𝑥𝑗) + in𝑦𝑖 in𝑦𝑗 Then we can build a 31 by 31 matrix describing the distance between province i and j, 0 𝑑1,2 𝑑1,31 𝑑2,1 ⋮ ⋮ d = ⋱ ⋮ ⋮ ⋮ 0 ] 𝑑31,1 𝑑31,2 [ in which r stands for earth radius

3) Parameters of cost and benefit

∆𝑤= min {|∆𝑤𝑖|, |∆𝑤𝑗|}

E = 𝑘0 · 𝑒−𝑏𝑖𝑏𝑗· 𝑑𝑖𝑗· log ∆𝑤𝑖𝑗

= min {|∆𝑤𝑖|, |∆𝑤𝑗|} 𝑖𝑗= ∆𝑤 j  𝐸 𝐸

∆𝑤 j  𝑖𝑗∝ 𝑒−𝑏𝑖𝑏𝑗· 𝑑𝑖𝑗· log ∆𝑤𝑖𝑗

4) Requirements

Then the requirement of water transfer from region i to region is, We only transfer water from high terrace to low terrace or in the same level of terrace, namely 𝑏𝑖≤𝑏𝑗 We do not consider building water transfer project within a watershed, namely 𝑒𝑖≠𝑒𝑗

4.3.4 Objective Function of water transfer strategy

Based on parameters and requirements we have mentioned above, we can get the Objective Function to make our water transfer strategy cost-efficient.

𝐸= min {|∆𝑤𝑖|,|∆𝑤𝑗|} z = min {= ∆𝑤 } 𝐸 𝑏𝑖≤𝑏𝑗 www.madio.net 𝑒𝑖≠𝑒𝑗 . t. { ∆𝑤𝑖< 0 < ∆𝑤𝑗

4.3.5 Model Testing

A simple example 数学中国 We can use Beijing as an example to test our model, and efficiently work out a plan of transferring water from other province to Beijing. Considering all the restrictions, we have

𝑏𝑖≤𝑏𝑗 𝑒𝑖≠𝑒𝑗 t. { ∆𝑤𝑖< 0 < ∆𝑤𝑗 ∆𝑤𝑗= 29.1552 Provinces which can provide the water to be transferred include Hunan, Jiangxi, Fujian, Sichuan and Guizhou (eliminate infeasible results like Tibet and Qinghai).

Hunan Jiangxi Fujian Sichuan Guizhou 𝒅𝒊, 1341.107 1248.448 1558.67 1520.881 1734.504 𝒊 2 1 1 2 2 𝒊 2 2 2 2 2 ∆ -55.6685 -90.907 -53.1004 -283.435 -104.649 η(relative value) 0.10968278 0.043344793 0.03471787 0.096717846 0.084805997

From the table we can see, we can achieve the optimal efficiency by transferring water from Hunan to Beijing.

4.3.6 National water transfer strategy

For all the regions in China, we can build a network connecting every region, and attach weights to every edge in this network.

ω = 1/ The smaller the ω, the greater benefit of the route. Thus, we can work out an effective national water transfer strategy by using minimum spanning tree. The following figure show six optimal water transfer route of China.

Figure. Six Optimal Water Transfer Routes of China

www.madio.net 数学中国 The figure above shows six water routes in China. Line 4 is in perfectly consistency with the Middle Route Scheme of the South-North Water Diversion Project of China. Besides, Line 5 and Line 6 are similar to the West and Eastern Route Scheme of the South-North Water Diversion Project of China. Thus, our model is efficient and cost-efficient.

4.3.7 Conclusion

Spatial Balancing of Water Resources Strategy Model solves problem in the decision-making process of cross-watershed water transferring, and put forward a realistic water transfer plan.

Although the plan we discussed above is nationwide, we can also apply the model to small watershed and local water transfer strategy. That is to say, we simply need to refine the geographic attributes and watershed attributes to solve a more detailed water transfer strategy. So our model is universal and feasible.

In a word, our model is efficient, feasible, cost-efficient and universal.

5 Model Three: Water De-salinization Strategy

5.1 Introduction

In our Spatial Balancing of Water Resource Model, we successfully figure out six nationwide routes of water transferring.

Now we will narrow down the range to discuss water de-salinization by focusing on one single region. Because we have discovered that, some provinces like Tianjin and Shandong, which are in urgent need of water, are located near the sea. So it is more cost-efficient to solve water scarcity problem by de-salinization rather than water transfer. Furthermore, de-salinization is a way to produce new water. www.madio.net

5.2 Terminology

𝐷0 The estimated water consumption in 2013 Θ The growth rate of water consumption from 2013 to 2025 T The total number of year from 2012 to 2025 which equals to 12 p The desalinization cost of tons of seawater, including power, chemicals and maintenance. 数学中国 p0 The desalinization cost of tons of seawater in 2013 𝑡𝑜𝑝𝑡 The optimal time to build water purification plant σ The measurement of the seawater’s desalination cost

5.3 Assumptions

 Desalination plant is distributed in the coastal cities. And the establishment of desalination model just only for the purposes of a city.

 We forecast the coastal city's water consumption is linear growth

 In the 2013 to 2025 year, due to the high cost of construction and maintenance costs of desalination, we cannot establish many desalination plants in a city. We think that in a coastal city within the 2013-2025 year, construction of two desalination plants is reasonable

 As technology advances, the cost of desalination annually is reduced. We can use p = p0𝑒−σ   as the cost of a ton of seawater’s desalination.

 We assume that we need to build a new desalination plant when the demand for water is bigger than the sum of water supply and another amount of desalination plant’s seawater’s desalination.

5.4 Model Building

In 2013, a region builds a new desalination plant, and it needs to build a new desalination plant before 2025. We are now considering how to control the scale of the two desalination plants and when to build another desalination plant.

The 2013 year’s demand of water is predicted as𝐷0, and an annual growth rate of water demands θ is constant. We assume a new desalination plant in the year (2013+t) as follows:

www.madio.net 数学中国 The first and second plant’s seawater’s desalination each year is

1 1 2 𝜃𝑡 , 2 𝜃𝑇 And the cost of the first and the second desalination plant:

1 1 2 p0θT𝑒−σ 2 p0θt , The total cost is p0 1 2 θt + 1 2 p0θT𝑒−σ = 1 2 𝑝0𝜃(𝑡+ 𝑇𝑒−σ )

5.5 Model Solving

Model solution:

We consider σ = 5 is reasonable, We use MATLAB to calculate the 𝑡𝑜𝑝𝑡 to minimize the total cost:

𝑡𝑜𝑝𝑡= ln (𝑇𝜎) ≈5 𝜎

5.6 Analysis and Conclusion

For a coastal city, the minimum total cost is E = 𝑝0𝜃[1 + ln (Tσ)] 2𝜎 And its 13 year’s seawater’s desalination amount is ∆W = 1 2 θ𝑇2 Its economic benefits:

η = ∆ 2𝑇𝜎 𝐸= 𝑝0[1 + ln (Tσ)] www.madio.net And considering the cost of seawater’s desalination per ton in China is 4 RMB, η = 5.889

6 Model Four: Water Conservation Strategy

数学中国

6.1 Introduction

Based on the above analysis, China is facing a severe water shortage problem. In addition to storage, water transfer, desalination, we should also consider the conservation. The conservation strategy mainly consists of two parts: water-saving and sewage control. We are going to consider the two scenarios.

6.2 Water Pollution Control Model

6.2.1 Introduction

In this model, we will grade the water pollution control demand of cities and use the grading system to decide the sequence of water pollution. In model 2, we work out an efficient water transfer plan by classifying nine watersheds in China. Similarly, we will apply this method to explore water pollution control problem.

Firstly we consider the emergency of water-pollution of each watershed, which can be described as Demand for Water-pollution control degree γ. Then we use γ to decide whether the watershed needs pollution control. After, we take one of these watersheds as our Examination Object and analyze the city’s demand for pollution control.

6.2.2 Assumptions

 Assume that the sewage emissions last year don’t exceed the environmental self-recovery capabilities. In other words, the sewage emission per year has no impact on next year's water quality.

 Assume that a large city (100-300 million) belongs to only one watershed and a watershed can have several large cities.

 Assume that the price of the sewage treatment has no regional differences

 Assume that water treatment costs rise with the increase of COD concentration in water resources www.madio.net

6.2.3 Terminology

𝛾𝑘 Demand for water-pollution control degree of number k watershed 𝛼𝑘 The water supply pressure of a watershed Ⅰ The highest level of water quality The middle level of water quality Ⅱ 数学中国 The lowest level of water quality Ⅲ 𝜌𝑘 The ratio between the sum of Ⅰ ,Ⅱ and Ⅲ water of resources to the total water resources 𝜇𝑘,𝑗 Demand for Water-pollution Control Degree of the number j city in number k watershed 𝑘𝑗 Water Resources of the number k city in number j watershed 𝐶𝑘𝑗 The total COD in the city’s water of the number k city in number j watershed COD The chemical oxygen demand 𝑐𝑜𝑑𝑘𝑗The emission of COD per year of the number k city in number j watershed

6.2.4 Model building:

Demand for Water-pollution Control of different watershed:

We define the watershed’s Demand for Water-pollution Control Degree 𝛾𝑘 as 𝛾𝑘= 𝛼𝑘𝑒−𝜌𝑘    k = 1,2, ⋯,9

in which, 𝛼𝑘 is the water pressure of a watershed 𝑤𝐼+𝑤𝐼𝐼+𝑤𝐼𝐼𝐼 𝜌𝑘= is the ratio of the sum Ⅰ ,Ⅱ and Ⅲ water to the total water resources. 𝑊

𝑒−𝜌𝑘 represents the water-pollution situation of a area. Considering that the control for pollution is more urgent than water pressure, we take exponential index of 𝑒−𝜌𝑘.

𝛾𝑘 is the critical criteria of water-pollution control considering the both sides of water pressure and pollution situation.

Water-pollution for cities in a watershed: The chemical oxygen demand COD is a critical index to test the water-pollution degree of an area.

𝐶𝑘𝑗 We take 𝜇𝑘,j = 𝛼𝑘𝑗 𝑊𝑘𝑗 as the emergency for control of the number j city of the number k

watershed, in which the greater 𝜇𝑘,j means the more emergence of control. 𝐶𝑘𝑗 means the COD

mount in the k, j city’s water:

𝑗 𝐶𝑘𝑗= ∑cod𝑘𝑗𝑒−(𝑗−𝑖) j = 1,2, ⋯, n 𝑖=1

We take the 𝑒−(𝑗−𝑘) as the interference of upstream city i to the downstream city j and n is the www.madio.net number of cities the watershed flowing through.

The total amount of missions of COD of the number k watershed is (𝑐𝑜𝑑𝑘1, 𝑐𝑜𝑑𝑘2, 𝑐𝑜𝑑𝑘3, ⋯, 𝑐𝑜𝑑𝑘𝑛) and we think the minimum of the emergency degree 𝜇𝑘is the best:

𝑛 𝑗 = ∑𝛼𝑘𝑗 min {𝜇𝑘= ∑𝜇𝑘𝑗 } ∑cod𝑘𝑗𝑒−(𝑗−𝑖) 𝑘𝑗 𝑗 𝑗 𝑖=1 数学中国 Now we adjust the emissions of COD to minimize𝜇𝑘. The optimal COD emission change is:

(∆𝑐𝑜𝑑𝑘1, ∆𝑐𝑜𝑑𝑘2, ∆𝑐𝑜𝑑𝑘3, ⋯, ∆𝑐𝑜𝑑𝑘𝑛)𝑜𝑝𝑡= −∇𝜇𝑘 The ∇𝜇𝑘 is the minus gradient of 𝜇𝑘:

𝑛 𝑛 𝛼𝑘𝑗 ∇𝜇𝑘= (𝛼𝑘1 , ⋯, 𝛼𝑘𝑛 ∑𝑒−( −j) ∑𝑒−( −1) , ⋯, ) 𝑘𝑗 𝑘1 𝑘𝑛 𝑖=j 𝑖=1 𝛼𝑘𝑗 𝑛 𝑒−( −j) ∑ We consider as the best decline emissions of COD. 𝑖=j 𝑊𝑘𝑗

6.2.5 Model solution:

Demand for Water-pollution Control of different watershed:

The following is the datai and the result of the various watershed: Watershed Songliao Hai Huai Yangtze Yellow Southeast Pearl Southwest Northwestern

1 2 3 4 5 6 7 8 9 k 43.1% 40.6% 43.5% 76.8% 38.6% 76.9% 75.1% 92.6% 90.3% Dk(108m3) 566.04 399.83 612.18 1682.31 388.61 319.31 850.78 103.30 103.30 Wk(108m3) 1372.98 158.99 701.83 10890.79 473.40 2314.36 5251.13 5640.51 1457.31 𝜶 0.412271 2.514812 0.872263 0.154471 0.820891 0.137969 0.162018 0.018314 0.070884 0.267918 1.675645 0.564585 0.071665 0.558018 0.063945 0.076455 0.007255 0.028733 www.madio.net 数学中国 As we can see from the figure above, the largest demand for water-pollution control is the Hai watershed, Huai watershed and the Yellow watershed comes next and the least is southwest watershed.

Water-pollution control for cities in a watershed: We analysis the Hai watershed as its 𝛾𝑘 is the greatest. And Datong city, Beijing city and Tianjing city is carefully considered:

Datong Beijing Tianjin Water 4.95 35.1 22.3 consumption /108m3 Water 8.0312 34.2 18.3 resources /108m3 𝜶 𝒋 ∑ −( − ) 0.9265 1.4038 1.2186 𝑾 𝒋 𝒊= Therefore, the Beijing gets the bigger control priority, lower priority shared by Datong.

6.2.6 Model analysis:

Validity Analysis We consider the k watershed city’s Demand for Water-pollution Control Degree 𝛾𝑘as the k, j city’s Demand for Water-pollution Control Degree’s weight. And 𝛾𝑘𝜇𝑘𝑗 can decide the city’s demand in the whole country.

Feasible analysis

We isolate each year to consider the 𝐶𝑘𝑗. But for a city, its pollution situation should also relate to the last year’s pollution situation:

𝑗 𝐶𝑘𝑗(Y) = ∑cod𝑘𝑗(𝑌)𝑒−(𝑗−𝑖) + 𝐶𝑘𝑗(Y −1)      j = 1,2, ⋯, n      ∈(0,1) 𝑖=1 in which,

Y stands for year. www.madio.net 𝐶𝑘𝑗(Y)   means the Y year’s COD amount in the city’s water, and cod𝑘𝑗(𝑦 ) means the ye year’s COD emission.

 is the previous year COD amount and next year COD amount ratio, which means the environmental self-recovery capabilities. 数学中国 Economic benefits analysis In fact, investment in various cities of controlling water-pollution is limited by the degree of economic development of the city. And we have to consider the economic benefits.

The consumption of a city’s whole water-pollution control is

𝐸𝑖𝑗= 𝐾0(𝑒𝐶𝑘𝑗−1)

in which 𝐾0 is the coefficient. If  𝐶𝑘𝑗= 0, the consumption 𝐸𝑖𝑗 is 0.

The greater the 𝐶𝑘𝑗, the greater the amount of money spent on pollution control. And the economic benefits:

𝜂𝑘𝑗= ∆𝐶𝑘𝑗 𝐸𝑘𝑗

And the whole watershed’s economic benefits:

𝑛 ∑∆𝐶𝑘𝑗 𝑗 𝜂𝑘= 𝑛 ∑𝐸𝑘𝑗 𝑗

6.3 Water-saving Model

6.3.1 𝜷 The water consumption per unit GDP β means the water consumption of a unit GDP. Thus, it shows the water utilization degree of the population and economy. The higher the utilization degree, the smaller water supply required per unit of GDP.

𝐷 𝐷 β = 𝑁· g = 𝐺𝐷𝑃 In order to determine a reference, we define β0 = 𝐷nation 𝐺𝐷𝑃 = 0.0255 ⁄

as the national average water consumption of a unit GDP.

Analysis and Conclusion

6.3.2 Analyzing the data from the National Statistical Yearbook of China，We divide ∆β into five sections as shown in the following Figure.

www.madio.net Figure. Classification of Water Consumption of a Unit GDP (𝛃) Beijing Tianjin Shandong Shanghai Shanxi Zhejiang Liaoning

𝛃 0.005079 0.005135 0.01101 0.012024 0.012917 0.014096 0.014475

Shanxi Henan Hebei  Guangdong Chongqing   Fujian Sichuan Jiangsu  Jilin 数学中国 0.0177 0.0179 0.018 0.019118 0.019299 0.02431 0.02453 0.02465 0.0248

Hubei Anhui   Inner Yunnan Hunan Guizhou Hainan Mongolia 0.032379 0.036172 0.03621 0.037898 0.041205 0.041823 0.043392

Qinghai Jiangxi Heilongjiang Gansu Guangxi

0.046207 0.04669 0.047083 0.056697 0.063333

Ningxia Tibet Xinjiang

0.10345 0.113901 0.176276 Comparing the table above with the previous Figure? Classification of Water Supply Pressure ( in Model 2), we are able to draw the conclusion. Water supply pressure of some areas ,such as Beijing、 Tianjin and Shanghai, is relatively high, and at the same time the water utilization degree of these region is also very high, so the need of water-saving is less urgent. But in Ningxia and Gansu, we have much room to improve β ( the water consumption of a unit GDP) so as to relive the water supply pressure.

So, we can justify whether one region needs to pay attention to water-saving strategy according to its β, the water consumption of a unit GDP.

7 Model Five: Impacts Evaluation Model

7.1 Introduction

In four models above, we have thoroughly analyzed the four water strategies: storage, movement, de-salinization, sewage treatment. To identify the best water strategy, we need a comprehensive analysis.

7.2 The Comparison of η (the actual benefit of a project)

Firstly, we compare the actual benefit of four strategies we have devised：

www.madio.net 𝑘 ∆𝑂 η = 𝐸0 · ω · log 𝑘+ log ∆𝑂⋯⋯⋯𝑚𝑜𝑑𝑒𝑙 2. 1 ∆𝑤ij η𝑖𝑗∝ ⋯⋯⋯𝑚𝑜𝑑𝑒𝑙 2. 2 𝑒−𝑏𝑖𝑏𝑗· 𝑑𝑖𝑗· log ∆𝑤𝑖𝑗 2𝑇𝜎 η = 𝑝0[1 + ln (Tσ)] ⋯⋯⋯𝑚𝑜𝑑𝑒𝑙 3 ∑∆𝐶𝑘𝑗 𝑛 数学中国 𝑗 𝜂𝑘= ⋯⋯⋯𝑚𝑜𝑑𝑒𝑙 ∑𝐸𝑘𝑗 𝑛 { 𝑗

According to these function from four models, the benefit analysis of a water strategy takes factors such as topography, watersheds, and engineering scale into account. Then we can determine the specific values of the parameters in these equations using Data Mining.

However, η only relates to the current cost and results. It does not take the future impact into account, such as economic, physical, cultural, and environment implications.

7.3 Evaluation of Economic, Physical, and Environmental

impacts using AHP When we identify the best water strategy, we should consider its economic, physical, environmental and other impacts. And the different strategies have different impacts, so we decide carry out the analytic hierarchy method (AHP).

Analytic Hierarchy Process (Analytic Hierarchy Process, AHP) is a simple method of making complex and fuzzy decision, and it is particularly suitable for those which is difficult to do fully quantitative analysis of the problem.

Modeling with AHP，we in general follow four steps:

(i) establish a hierarchical structure model;

(ii) construct all levels and in all judgment matrix; (iii) sort Single-level and consistency checking; (iv) sort total-levels and consistency checking.

www.madio.net 数学中国 Grade Relative importance Equally Important 1 Generally more Important 3 Far more Important 5 More Important at the second highest degree 7 More Important at the highest 9 level is in between according to the above 2，4，6，8 represents the importance express ‘Less important’ The reciprocal value(1/2,1/7…)

According to the situation of China, we change the test matrix and get the following results,

Economic Physical impact environmental impact impact 1 7/5 7/4 Economic impact 5/7 1 5/4 Physical impact 4/7 4/5 1 environmental impact

Economic Storage Movement De-Salinization Sewage impact treatment Storage 1 5/6 5/6 5/3 Movement 6/5 1 1 2 De-Salinization 6/5 1 1 2 Sewage 3/5 1/2 1/2 1 treatment

Environmental Storage Movement De-Salinization Sewage impact treatment Storage 1 6/7 6/4 6/9 Movement 7/6 1 7/4 7/9 De-Salinization 4/6 4/7 1 4/9 Sewage 4/9 9/7 9/4 1 www.madio.net treatment

Consistency Check of Test Matrix A n=3, RI=0.508

/5 / 1 5/ 1 5/ A = ( ) 数学中国 /5 1 / 𝐶𝐼 Calculated by MATLAB, 𝐶𝑅= 𝑅𝐼< 0.1 .So the coherence of the matrix is qualified.

The Consistency Check of Total Sequencing of each level CR = 𝑎1𝐶𝐼1 + 𝑎2𝐶𝐼2 + ⋯+ 𝑎3𝐶𝐼3 𝑎1𝑅𝐼1 + 𝑎2𝑅𝐼2 + ⋯+ 𝑎3𝑅𝐼3

Through calculation by MATLAB, CR<0.1 So the coherence of the matrix is qualified.

However, we can’t simply think that the greater the value of impact t, the better. We need a dedicated parameter to indicate the degree of quality of water strategy.

7.4 Neural Network Evaluation Algorithm

7.4.1 Analysis

Through continuous research projects that have been implemented, it is able to accurately determine their economic, physical, environmental impacts, and the general degree of quality. Evaluation will be more credibility by establishing relationship between quality and impacts.

So we use a method based on analytical hierarchy process(AHP) for Neural Network Evaluation Algorithm.

We define that one method 𝑚𝑖 which contains some attributes:

𝑚𝑖= (𝑒𝑐𝑖, 𝑝ℎ𝑖, 𝑒𝑛𝑖, 𝑜𝑡ℎ𝑒𝑟𝑠𝑖) 𝑒𝑐𝑖: Economic impact 𝑝ℎ𝑖: Physical impact 𝑒𝑛𝑖: Environmental impact 𝑜𝑡ℎ𝑒𝑟𝑠𝑖: Other impacts which implies the properties considered in the model is scalable

In addition, implemented method has a determined degree of quality:

𝑑𝑒𝑖= 1,2,··· 10

According to 𝑑𝑒𝑖, we can divide 𝑚𝑖 into 10 categories.

We should collect the data of impacts and degrees of quality. In the following table, we select only a typical embodiment of each strategy, and assume that the effects of other water strategies to expand www.madio.net the number of neurons.

𝑒𝑐𝑖 𝑝ℎ𝑖 𝑒𝑛𝑖 𝑜𝑡ℎ𝑒𝑟𝑠𝑖 𝑑𝑒𝑖 Three Gorges Reservoir 6 7 5 8 4 The South–North Water Transfer 7 9 7 6 7 Project 数学中国 Tianjin Dagang Desalination Plant 5 4 3 4 8 Taihu Lake Sewage Treatment 7 8 6 3 6 Others ··· ··· ··· ··· ··· (All various numerical range is 1-10)

7.4.2 Conclusion

Therefore, to evaluate a water strategy, we should:

 Firstly, build the neural network model;

 Secondly, draw attributes of the water strategy using AHP;

𝑚𝑖= (𝑒𝑐𝑖, 𝑝ℎ𝑖, 𝑒𝑛𝑖, 𝑜𝑡ℎ𝑒𝑟𝑠𝑖)

 ·Thirdly, input 𝑚𝑖 into the neural network model;

 ·Fourthly, analyze the output results of the degree of quality from neural network model.

8 Strengths and Weaknesses

8.1 Strengths

 Model 1 is based on quantitative analysis, so our results of prediction progress are objective and efficient.

 In Model 1, we use different methods to solve the prediction problem and the results we get is in perfectly consistency.

 In Model 3, we successfully quantify various indicators and get the expected results by www.madio.net reasonable mathematical derivation.

 In Model 4, we define an effective method to judge the urgency of water pollution control demand of an area. Based on this method, we can solve water pollution problem effectively.

 In Model 5, we use Neural Network Algorithm to train the Judgment Matrix of the Analytic Hierarchy Process , thus we eliminate the influence of subjective factors 数学中国

8.2 Weaknesses

 In Model 1, our Function Fitting Model is restricted by limited data.

 In Model 3, we define several restrictions to simplify calculation process, which is go against our goal to access the optimal result.

 In Model 4, we don’t get the exact value of the benefits due to lack of data

9 Position paper for the Governmental leadership

of China

To whom it may concern,

Green lands, beautiful flowers and crystal mountain streams are common sights in many parts of China. But it is also a fact that China is a country facing severe water problems. To help heal the water, we devise the 2015 water strategy and it may include the following 2 aspects:

Inter-watersheds:

www.madio.net The water transfer strategy should be from Yangtze Watershed to Yellow Watershed, Huai Watershed and Hai Watershed。 In addition, we should transfer water from the Southwest Watershed to the Northwest Watershed, and from Southeast Watershed to Pearl Watershed.

And according to the different water-pollution situation between different watersheds, water pollution of Huai Watershed, Hai Watershed and Yellow Watershed are most serious. The earlier the 数学中国 problem be solved, the lower the cost.

Within a watershed, we should carry out water storage where water resources change sharply.

To heal the water and to better life of people in China, please consider our plan. The future of China lies in your hand. You won’t regret.

Yours sincerely

11 Appendix and Supporting Datas

11.1Regression analysis

clc clear x=importdata('97-10data.txt'); total=x(:,8); live=x(:,11); arg=x(:,9); ind=x(:,11); pop=x(:,15); argGDP=x(:,16); food=x(:,14); indGDP=x(:,17); popGDP=x(:,19); argf=[ones(14,1),food,argGDP,pop]; arg_re=regress(arg,argf) livef=[ones(14,1),pop,popGDP];

live_re=regress(live,livef) indf=[ones(14,1),indGDP]; ind_re=regress(ind,indf) totalf=[ones(14,1),pop,popGDP,argGDP,food,indGDP]; total_re=regress(total,totalf)

11.2Function fitting

clc;clear; x=importdata('00-10 water supply.txt'); year=x(:,1);

www.madio.net total_water_consumption=x(:,2); dibiao=x(:,3); dixia=x(:,4); renjun=x(:,11);

11.3GrayModel(1,1)

数学中国 clc clear x0=[5623 5470 5613.33 5530.73 5567.43 5497.28 5320.4 5547.8 5632.98 5794.966575 5818.669827 5909.95 5965.151465 6021.994065]; n=length(x0); lamda=x0(1:n-1)./x0(2:n); range=minmax(lamda); x1=cumsum(x0); for i=2:n z(i)=0.5*(x1(i)+x1(i-1)); end B=[-z(2:n)',ones(n-1,1)]; Y=x0(2:n)'; u=B\Y; x=dsolve('Dx+a*x=b','x(5)=x0'); x=subs(x,{'a','b','x0'},{u(1),u(2),x1(7)}); yuce1=subs(x,'t',[0:28]); digits(6),y=vpa(x) yuce=[x0(1),diff(yuce1)]; xx=1997:2010; xxx=1997:2025; plot(xx,x0,'o-',xxx,yuce) title('GM Predition'); xlabel('Year'); ylabel('Water consumption') epsilon=x0-yuce(1:14) ; delta=abs(epsilon./x0) ;

rho=1-(1-0.5*u(1))/(1+0.5*u(1))*lamda ;

11.4 Association analysis

clear X=importdata('B_Data.txt'); x1=[X(:,9),X(:,14),X(:,16),X(:,15)]; x2=[X(:,10),X(:,17)]; x3=[X(:,11),X(:,15),X(:,19)]; x4=[X(:,8),X(:,9),X(:,10),X(:,11)] x=x1';

www.madio.net rou=0.5; for i=1:4 x(i,:)=x(i,:)/x(i,1); end plot(X(:,1),x(1,:),'r-') hold on plot(X(:,1),x(2,:),'k-') 数学中国 data=x; n=size(data,1); ck=data(1,:);m1=size(ck,1); bj=data(2:n,:);m2=size(bj,1); for i=1:m1 for j=1:m2 t(j,:)=bj(j,:)-ck(i,:); end jc1=min(min(abs(t')));jc2=max(max(abs(t'))); rho=0.5; ksi=(jc1+rho*jc2)./(abs(t)+rho*jc2); rt=sum(ksi')/size(ksi,2); [q,p]=size(rt); o=1:1:p; r(i,o)=rt(1,o); end r [rs,rind]=sort(r,'descend') %water for live changes with population X=importdata('B_Data.txt'); figure(1) subplot(3,1,1) [ax1,h11,h12]=plotyy(X(:,1),X(:,11),X(:,1),X(:,15)*100); xlabel('Year') set(h11,'linestyle','-','color','r'); set(h12,'linestyle','- -','color','k');

legend([h11 h12],'WaterForLive/hundred million m^3','population/million')

www.madio.net 数学中国
