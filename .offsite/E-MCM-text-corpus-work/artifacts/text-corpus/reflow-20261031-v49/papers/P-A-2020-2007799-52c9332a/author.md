Problem Chosen 2020

MCM/ICM

Summary Sheet

Summary

Changes in global ocean temperature affect a large number of marine lives in colder environments. As a consultant to the Scottish North Atlantic Fisheries Management Consortium, our paper studied Scottish fishing companies’ business strategies with species migration

First, we collected sea surface temperature changes in the Northeast Atlantic and North Sea over the past forty years and use the Power Function to describe the temperature development trend and Trigonometric Function to describe the periodic temperature change, then we build a superposing model to predict sea temperature in the next fifty years. In order to identify the position of herring and mackerel, we established a Moore-type Cellular Automaton. Com- bined with predicted temperature data, the model shows herring will live in the sea near Alesund, Norway, which is 801 km northeast of Scotland, mackerel will live in the sea which is 268km northwest of Bergen, Norway and 544 km northeast of Scotland in 2070. Secondly, we studied the relationship between speeds and vessel design parameters and established a speed estimation formula. Combined with the fish preservation time for fresh, we established a Maximum Range of Fishing Vessel Model. Model shows the maximum range of a middle fishing vessel is a circle with a radius of 108.6km. Next, we selected 10 typical port locations in Scotland, substituted the range into the CA cell space, use the SST prediction data of best case and worst case to simulate the elapsed time of each port. The results show that the average elapsed time of each port in the best and worst case are 21.2 years and 13.7 years respectively and most ports will be unavailable after 2050.

Based on the above analysis, we believe that small fisheries companies should change their operations. In order to quantify the migration routes of herring and mackerel, we used Fourth- Order Polynomials to fit, so as to calculate the distance relations among ports, fishing boats and fish stocks. Then, we use above formula establish a Cost-Benefit Model to measure the benefits of two options that one is only relocating company to the port near fish population without buy new vessel, one is only buy ship with refrigeration without relocating. Model showed that between 2020 and 2040, the return of option 1 as a strategy is much higher than that of option 2, between 2040 and 2070, only option 2 as a strategy because option 1 fails. We also assess impact of the transfer of fisheries to the territorial waters of neighboring countries.

Not only that, we explore the factors that affect the return of options in the sensitivity analysis, namely the speed of the fishing boat, the cargo capacity and the price of fish to explore the role these factors play in the choice of strategy. Last but not least, we wrote an article for Hook Line and Sinker magazine to help fishermen analyze the seriousness of the current problem and provide them with solutions to improve their business in a straightforward way.

关注数学模型

1 Introduction

1.1 Restatement of the Problem

Global warming is an objective fact that people all over the world have to face. Since 1980, global temperatures have risen rapidly. According to satellite temperature detection, the tropospheric temperature has risen by 0.12 to 0.22 degrees (Celsius) every ten years. Relatively stable, but since 2015, ocean surface temperatures have increased year by year [1]. One of the immediate effects of global warming is rising sea temperatures, with summer temperatures in the North-East Atlantic off Scotland rising at 0.0048 degrees per year [2], rising seawater temperatures have led to the migration of marine habitats near Scotland, especially herring and mackerel, which are important for Scottish fisheries. The migration of herring and mackerel can make the fishing economy impractical for some smaller fisheries companies. Our team was hired as a consultant by the Scottish North Atlantic Fisheries Management Consortium to help study species migration and company management related issues. Under some assumptions, we need to model to solve the following series of problems:

1. Based on historical observation data of the Northeast Atlantic, study the trend of sea temperature change and the biological characteristics of two fish species, establish mathematical models to predict sea temperature changes and the most likely locations for mackerel and herring to survive in the next 50 years.

2. Based on the sea temperature change model, determine the best- and worst-case sea temperature changes. Based on surveys of actual Scottish ports and small fishing vessels, establish a fishing cost model for small fishing vessels to determine the elapse time that can’t harvest.

3. By investigating fishery data, modeling the revenues of small fisheries companies, and assessing whether business operation should be changed. At the same time, we need to study the influence of various strategies on the company's operations, determine the optimal port migration location, the number of small fishing vessels, etc. Finally, the effect of fishery transfer to the territorial sea of another country is need to be studied.

1.2 Analysis of the Problem

The scope of all our research objects is limited to the oceans around the United Kingdom and the adjacent European continent. The related oceans include the Northeast Atlantic Ocean, the North Sea, and the Norwegian Sea. The scope of the study is the past 40 years and the next 50 years (2070-2080). The types of marine organisms studied include herring and mackerel, which are two types of fish with significant changes in migration. The area of the study refers to Figure 1.

First of all, considering that the sea temperature changes have a clear trend over time, and that the internal temperature changes every year are periodic. We assume that the overall upward trend is constant, so we established a superposition fitting equation, using a power function to fit the overall trend, and then using a periodic function to fit the periodic changes in sea temperature. The fitting is closer to the actual data, and we use this model to predict the temperature change in the study area.

关注数学模型 Biological population migration is a group behavior, including chaos and randomness, so we use cellular automata to simulate the migration behavior of fish schools. We simulated the land and sea terrain of the study area and divided the entire range into 7x7 blocks, each of which changed in temperature over time. Here we assume that the biggest factor influencing fish migration is seawater temperature, so the driving force for cell movements comes largely from the pursuit of an appropriate temperature. The results show that after 50 years, both species will move far north.

67 Secondly, for fishing boats without refrigeration equipment, the most important factor restricting the 65 voyage size is the freshness of the fishing products. Fishes without refrigeration will lose their freshness after a period of time at room temperature, leading to 60 spoilage. Before the deterioration, it is necessary to ensure that the fishing boat can return to the port, so the range of the fishing boat is limited. We have established speed models for fishing boats of 55 different sizes and powers. It is assumed that fishing companies use medium-sized fishing boats to harvest 50 and find their speed to obtain a circular driving range with a maximum range. Beyond this range, fishing boats will not be able to operate due to fish spoilage. -18 -15 -10 -5 0 5 10 Next, we analyze each of the main fish ports in

Scotland, and superimpose the fishing range and fish migration process. The fishing range and the fish migration process are superimposed to obtain the time point at which the school of fish intersects and leaves the fishing range, and calculates the duration of operation. Next, we need to substitute the slowest heating rate and the fastest heating rate model into the cellular automaton to find the fishing duration in two extreme cases.

Thirdly, based on the movement of fish group in the next 50 years, we need to analyze different fishing ports and choose the best option for them. For option 1, we assume that the fishing port will be relocated once a year, each time moving to a coastal area with proper distance to keep the fish fresh, so that the income will be the same as usual. For option 2, we need to get the relationship between the position and time of the fish group through the predicted moving track, and calculate the distance between the fish group and the port every year, then calculate the number of fishing boats going to sea every year through the distance, finally get the total fishing amount and income. For each fishing port, compare the income of the two options and select a better alternative. It is worth noting that after a certain time point, the fish may be too far away to execute option 1, only option 2.

2 Assumption

Our models rely on the following assumptions. Some assumptions are throughout the text. These assumptions will simplify the problem. Other assumptions may not be as follows, but will be put forward in the model push.

1. Sea temperature rise is mainly caused by the absorption of heat generated by global warming. The trend of sea temperature changes is consistent with the previous years and will not rise or fall suddenly. Only float within a certain range.

关注数学模型 2. The population of mackerel and herring will not change in 50 years. Regardless of the predator, living environment and human activities, each fish in the school is an adult fish, and it is sensitive to temperature.

3. Small fishery companies' ships do not have refrigeration units and return to port immediately after catching fish without intermediate stops.

4. Fishing boats equipped with refrigeration can keep fish fresh indefinitely.

5. In order to ignore the rest time of fishermen, it is believed that every fishing boat works 24 hours a day without rest

3 Notation

We begin by deﬁning a list of nomenclature (symbols) used in this report, cf. Table1.

Symbols Description a The coefficient of temperature growth rate b The exponential of the rate of temperature increase c The base of temperature increase The optimum temperature of fish school to survive t optimal The temperature of the block where the fish is currently located t current The degree of stimulation of the fish school by the temperature p stimulate The threshold of fish school for temperature changes p threshold The speed of fishing vessels v vessel Maximum range of a fishing vessel D max Fish coordination ip The ship period iT Distance between ship and fish stock id Time of 365 days multiply 24 hours T y Maximum carrying capacity of a ship W max Revenue of a company R Revenue of a company in option1 R 1 Revenue of a company in option2 R 2 S Fish price

4 Survival position of two fish species over next 50 years

4.1 Description of ocean temperature

4.1.1 Single-point model for prediction of sea temperature change

We collected temperature data from the NOAA in the study sea area from 1990, and fitted the data from 2012. The reason for selecting data after 2012 is that the changes in ocean

关注数学模型 temperature were gentle before 2012 and after 2012 The temperature data began to rise, and we assume that the temperature change will continue in this trend in the future. Figure 3 shows the changes in SST over the northeast Atlantic in western Scotland since 1990.

1 2 3 4 5 6 7 In order to make calculations convenient and convenient for later modeling, we divide the study area 1 into 7×7 blocks, each block is given a number, cf. Figure 2 2, the longitude and latitude spanned by each block are 4 ° and 3 ° respectively. We assume that the sea 3 temperature in each block is the same. Take the block's center point temperature as a representative of the block 4 temperature, and study 49 blocks separately. Each block 5 is regarded as a point to predict the temperature change.

6 The SST curve can be regarded as a periodic function with an upward trend. We tried to predict the 7 time series model. The results show that the model

distortion is very serious over a 50-year span. Therefore, we use a simple power function and a periodic function superposition to solve problem. Let the power function (1) represent the overall trend, the growth rate of temperature depends mainly on the coefficient a in front of x and the exponent b of x

  b f x ( ) ax c (1)

Where x represents time, unit is day. Let the periodic function of temperature change throughout the year be (2)

  (2) g x ( ) p sin( qx r )

Combining (1) and (2) linearly to obtain the overall prediction equation

    b pre x ( ) p sin( qx r ) ax c (3)

Taking block (3,3) as an example, the overall prediction equation is substituted into the historical data, and the parameters obtained are (4)

关注数学模型        11 p 4.194, q 0.0172, r 2.3 542 , 5 a 1.289 e , b 2.348, c 1.3 9 9 (4)

It can be seen from the figure 4 that the first half of the prediction equation fits the historical data to a high degree, and the second half without red line is slow climb, as shown in the figure 4, in the next 10 years, which is 2030, the temperature reached 6℃, the highest temperature occurred in summer, about 10℃, and the lowest temperature occurred in winter, about 2℃. After 50 years, that is, 2070, the annual average temperature reached 9℃. The highest temperature is 12.2℃ and the lowest temperature is 4.2℃. Refer to Appendix A for the temperature prediction diagram for all blocks.

4.1.2 Ocean temperature changes in the overall research area

We plot the temperature of the research area at different points in time over the next 50 years, the temperature situation is displayed at an interval every ten years, and the temperature is taken as the average temperature of the year, cf. Figure 5

1 2 3 4 5 6 7 1 2 3 4 5 6 7 1 2 3 4 5 6 7 1 1 1

2 2 2

3 3 3

4 4 4

5 5 5

6 6 6

7 7 7

Conclusion From Figure 5 that the temperature of the sea area near Scotland gradually rises with time. It will be about 6.5 degrees in the Northeast Atlantic in 2030, and 4 degrees in the Norwegian sea. By 2050, the temperature in these two regions will be 7 degrees and 5 degrees at the same time, the temperature near the Celtic Sea and the English Channel rose to 9 degrees. In 2070, the Norwegian Sea warmed to 6-7 degrees, the Northeast Atlantic warmed to 8 degrees, and the Celtic Sea rose to 10 degrees. From 2030 to 2070, the Northeast Atlantic

关注数学模型 rises by an average of 0.0375 per year, and the Norwegian Sea rises by an average of 0.075 degrees per year.

4.2 Cellular automaton model of fish migration

The North Atlantic mackerel lives in the ocean at a depth of 0-200 meters per year. For the convenience of calculation, we assume that the adult fish is about 27cm in length, and regardless of the characteristics of the mackerel close to the continental shelf during the spawning period, it is believed that the habitat migration of mackerel is mainly affected by temperature, and the survival temperature range of mackerel is 7-17.5℃, and the optimal temperature is 6.6℃ [3]. Similarly, Atlantic herrings live in the ocean at a depth of 0-364 meters. For the convenience of calculation, we assume that the adult fish body length is 30cm, and Regardless of the impact of other marine factors on fish migration, it is believed that the habitat of herring depends mainly on the temperature of the ocean, and that the survival temperature range of herring is 0.5-11.2℃, and the optimal temperature is 5.6℃ [4]. In the future changes, the numbers of these two fish species will not change.

We use the Moore-type cellular automaton to build the fish migration model. The neighbors of the Moore-type cellular automaton are 8 cells around the cell, while 4 cells of the Von Neuman-type cell. Set the research area as cell space with a size of 300x300 pixels, similar to the SST model, divided into 7x7 blocks, each block is 43x43 pixels. Each block has a different temperature. Based on the above assumptions for fish, in each step, every small school of fish, that is, a cell, has two modes of action. When fish school is in an appropriate temperature area, they will choose a random nearby position and move randomly. The probability depends on the number of nearby fishes. The more nearby fishes, the greater the probability of moving. This is to simulate the behavior of fishes in allocating living resources, because the unit area of plankton that the fish prey on is certain. When the temperature of the area where fish school exceeds the threshold of fish school temperature, fish school will move to the block near the appropriate temperature, and fish school still has a chance to move randomly at this time. The cell’s mode of action is shown in Figure 6.

Check the Less than threshold Random Walk number of neighbors Start Check seawater Move decision temperature Move to the Optimal temperature direction More than threshold

In order to better reflect the sensitivity of the organism to temperature, we assume that the sensitivity of the fish to the temperature changes conforms to the S-curve, so we use the Sigmoid t function to represent the degree of stimulation of the fish to different temperatures. Let optimal t denote the optimum temperature of fish school, denote the temperature of the school current

关注数学模型 where the school is currently located, and p denote the degree of stimulation of the fish stimulate school by the temperature difference from the appropriate temperature. p represents the threshold threshold of fish school for temperature changes. Thus, the degree of temperature difference stimulus can be expressed as (5).

1  p (5)    stimulate (| t t | 5)  1 e current optimal

 The sigmoid function maps values in the real range to values in [0,1], so p [0,1] . threshold  p p When , the temperature change is not enough to drive fish school to move, threshold stimulate  p p and fish school does random motion. When , the temperature drives fish threshold stimulate school to move towards a suitable place.

The sea temperature model prediction data is substituted into the cell automata block. From the literature we obtained the initial habitat of herring [5] and mackerel [6] respectively. Here we assume that the two fish parameters are generally shown in Table 2, the model operation results are shown in Table 3, and the position distribution is shown in Figure 7.

Species Parameter Value 5.6 t (℃) optimal Herring 0.2 p threshold Initial position 55°N 3°E (In the middle of North Sea) 6.6 t (℃) optimal Mackerel 0.1 p threshold Initial position 59°N 5°W (114 km northwest of Shetland)

1 2 3 4 5 6 7 1 2 3 4 5 6 7 1 2 3 4 5 6 7 1 1 1

2 2 2

3 3 3 4 4 4 5 5 5

6 6 6

7 7 2030 7 2020 2040 1 2 3 4 5 6 7 1 2 3 4 5 6 7 1 2 3 4 5 6 7 1 1 1

2 2 2

3 3 3 4 4 4 5 5 5

6 6 6

7 7 7 2060 2050 2070

关注数学模型 1 2 3 4 5 6 7 1 2 3 4 5 6 7 1 2 3 4 5 6 7 1 1 1

2 2 2

3 3 3 4 4 4 5 5 5

6 6 6

7 7 7 2040 2030 2020 1 2 3 4 5 6 7 1 2 3 4 5 6 7 1 2 3 4 5 6 7 1 1

2 2

3 3 4 4 5 5

6 6

7 7 2050 2060 2070

Conclusion about most likely location For herrings living in the North Sea, the possible location of herring in the next 50 years will gradually move northward, leaving the North Sea and close to the Norwegian Sea. In 2030, 10 years later, the fish school will move north to about 544 km west of Scotland, and 20 years later, it will move 230 km north in 2040. It will be close to the waters near the port of Åkrehamn in Norway. In 2050, 30 years later, the school of fish will continue moved 109 km north to reach the waters near Bergen, Norway, and in 2060, 40 years later, it traveled 194 km north. Finally it moved 310 km northeast in 2070, which is 50 years later, to reach the sea near Namsos.

For mackerel living in the Northeast Atlantic, the possible location of mackerel in the next 50 years will also gradually move northeast, gradually leaving the waters near Scotland and reaching the coast of Norway. By 2030, 10 years later, the mackerel school will move to the middle of Scotland and Norway. By 2040, 20 years later, the mackerel school will continue to move 222km westward and reach the waters near Stavanger, Norway. Between 2050 and 2060, the school of fish migrated northward, until 2070, 50 years later, the school of fish's habitat moved to 268km northwest of Bergen, Norway.

5 Duration that small fisheries companies can still harvest

Based on the results of our current analysis, we can know the migration rate and location of the two fish schools in the next 50 years. At the same time, we also know that for the different values of the parameters a , b , and c in the temperature prediction model, different heating rates can be obtained, and different seawater temperature changes will lead to different rates of fish migration, that is, although fish migration the route is the same, but at different rates of temperature change, the time to reach the same location may be different. Here we insist on the assumption that small fishing vessels have no refrigeration equipment and return to port immediately after harvesting fish at a certain point.

5.1 Maximum range of fishing vessel model

There are many factors that limit the reach of small fishing vessels, such as the maximum voyage, the cost-effectiveness ratio of fishing and fuel consumption value, etc. We believe that

关注数学模型 the most important factor in the current situation is to maintain the freshness of marine fish and avoid rotting when transported to the fishing port. In the absence of refrigeration equipment, t we assume that the maximum time a fish stays fresh is and the speed of the fishing boat fresh is v . According to the fishing boat speed evaluation formula [7], the speed of a vessel is vessel (6)

P  0.237 (6) v 1.84( ) L vessel 

Where P is main engine power (kW),  is displacement (ton), L is the length between perpendiculars, that is, the horizontal distance between the forward and aft perpendiculars (m). Therefore, let us denote the longest voyage distance of a medium-sized fishing boat as D , max then D can be expressed as (7) max

 D t v (7) max fresh vessel

Based on the information consulted, fishing boats generally less than 12m in length are classified as small fishing boats, and 12-24m are classified as medium-sized fishing boats. According to the Scottish Sea fisheries report, we set the hull length L is 24m, power P is 440kw, and displacement  is 70t [8] . We get  t v 18.1 km s / . Set to 6 hours, then fresh vessel  D 108.6 km the boat can travel . At this speed, the medium-sized fishing boat can travel up max to 108.6km after catching the fish. Beyond this voyage, the fish will be spoiled because the preservation period has passed. At the capture point, the area of action of the fishing boat is about 74066km2.

There are many fishing ports in Scotland. According to Scottish fishery statistics, we have simplified the distribution of Scottish ports to one region correspond one port [9]. Then the activity range of each port for fishing boat is a circular area with a radius of about 108km in the vicinity, cf. Figure 8.

r = 108.6 km

v = 18.1 km/s

S = 74066 km2

关注数学模型 5.2 the elapsed time of the catch at best and worst case

For the carbon emissions in the next 50 years assessed by different experts, we adjust the a b c parameters in the temperature prediction model to get the best- and worst-case sea , , temperature changes. Still taking (3,3) blocks as an example, the adjusted best case the following parameters are

    11 a 1.314 e , b 2.34, c 3.899 (8)

While worst case is

    11 a 1.289 e , b 2.348, c 1.399 (9)

Finally, we have a possible sea temperature change interval in the next 50 years. In the worst case, the temperature of block (3,3) will reach 9 degrees in 2070, and in the best case, the temperature of block (3,3) will reach 7.1 degrees.cf. Figure 9.

In the case of accelerated temperature rise, the migration of fish will accelerate. When the coverage of a port and the habitat of fish no longer intersect, we reckon that the distance is too far to harvest at this time point. After substituting the temperature prediction equation and the port range into the cellular automaton, the model results are shown in Table 3.

Conclusion In the best case, elapsed time is 33 years, after that all fishery companies in each port except Shetland will not be able to capture because they are too far away. In the worst case, the elapsed time is approximately 21 years. One interesting fact is that the small fishing companies on Shetland won't be able to fish until 2020-2035, but after that, both mackerel and herring habitat have moved to Shetland, allowing the company to harvest until 2070. Despite low initial value, Shetland has huge fishing potential in the future of global warming.

关注数学模型 Fishing Port Best Case Worst Case Fish Type herring mackerel herring mackerel Shetland 30(2050-2070) 10(2060-2070) 30(2035-2055) 20(2050-2070) Orkney 0 33(2020-2053) 0 21(2020-2041) Kinlochbervie 0 25(2020-2045) 0 15(2020-2035) Stornoway 0 29(2020-2049) 0 14(2020-2034) Portree 0 20(2020-2040) 0 6(2020-2026) Campbeltown 0 20(2020-2040) 0 5(2020-2025) Ayr 0 0 0 0 Fraseburgh 23(2020-2043) 0 13(2020-2033) 0 Anstruther 13(2020-2033) 0 8(2020-2028) 0 Eyemouth 9(2020-2029) 0 5(2020-2025) 0

5 Strategies of small fishing companies and future impact

Based on the above analysis, we know that in the worst case, except for the port in Shetland, the rest of the ports that rely on fishing vessels without refrigeration devices will not be able to catch two kinds of fish. Without any action, these small fisheries company will go bankrupt because it has no income. Therefore, we believe that these small fishing companies should make changes to their operations. After determining that small-scale fisheries companies should change their operations, we should clearly define two strategic options.

 (Option 1) Does not buy new fishing boats. The port should be relocated every once in a while, and the cost of the relocation is expressed by C . After the relocation, the rel  port always guarantees that the fish population is within D 108.6 km . Assuming max that the boat does not rest, it will return from the port to the school after catching the fish, and all will fish according to the longest distance of 108.6km.

 (Option 2) Does not replace fishing port location. Boat switch to a new type of refrigerated fishing boat. Assume that this kind of boat can keep unlimited freshness  power, and the speed is v 18.1 km h / like a boat without refrigerating device. vessel There is no distance limit. Use C to indicate the cost of purchasing a boat boat

5.1 A fitting equation for the movement of a shoal of fish

In Section 4.2, we used a cellular automaton to simulate the movement course of the school of fish. In order to quantitatively describe the relationship between the migration route of herring and mackerel and time, we need to establish a fitting equation for the two fish routes fitting. We define the location of a fish's habitat (that is, this school of fish) as the geometric center of its overall range. The coordinates of the two fish migration routes are shown in Table 4. The fourth-order polynomial is used to fit the changes in longitude and latitude. The fitting formula is (10)

    4 3 2 1 position p i p i p i p i (10) 1 2 3 4

Where i the number of year. The fitting results are shown in Figure 10. The polynomial

关注数学模型 parameters are shown in Appendix C. The position coordinates of the school of fish in the i year are expressed as (11)

 ip ( lon i lat i ( ), ( )) (11)

Where ip is the fish coordinates, lon i is the longitude, and ( ) lat i is the latitude. ( )

Time Herring Mackerel 2020 58, -6 55，3 2030 58, 4 59, -0.4 2040 59.5, 4.4 58, 3.2 2050 61, 4.2 59, 4.6 2060 62, 4 60, 4 2070 65, 8 60, 0.1

5.2 The cost-benefit model of the two options

When a fishing boat starts fishing from the port, it needs to travel one round trip. We define the fishing boat from departure to the position of the school of fish. The time of returning to the port is a period T . The position of the school of fish changes every year, in the i year. The period is denoted by iT , we define id as the distance from the port to the school of fish in the i year, and the distance can be expressed as (12)

关注数学模型   d i ( ) | p i ( ) p | (12) port

Where p is the position of fishing port. Since we know the v , so we can represent port vessel iT as

2 ( ) d i  T i ( ) (13) v vessel

We assume that the fishing boat works 24 hours a day for 365 days, and time is T . The y weight of the cargo carried by each trip is W , and the price of fish is S . Then the total max revenue R of a fishing boat in year i is

T y  R i ( ) W S (14) max T i ( )

As for Option 1, because it does not include ships with refrigeration, the solution can only be implemented until 2040. Assuming that the port location needs to be changed every 5 years, the revenue R is 1

2040    (15) R 1 R i ( ) 10 C rel  i 2020

 Where C is cost of relocation and d i ( ) (0, D ] . For the option 2, since it is not a rel max replaceable port, but the navigation distance of the ship is not limited, this option can be implemented until 2070, and its total revenue R is 2

2070    (16) R 2 R i ( ) aC boat  i 2020

Where C is cost of buying a new refrigerated fishing boat and a is number of boats, boat we assume it is 1.

The data collection The average selling prices of herring and mackerel obtained from the Scottish Fisheries Statistics Report are = 444.75 pound and S = 883.75 pound S herring mac ker el respectively [10]. At the same time, we checked the information to find that the cost of a relocation R is 750,000 pounds, and the price of buying a fishing boat with refrigeration rel R is 220,000 pounds. At the same time we can know the coordinates of the port, see boat Appendix C, substitute the cost-benefit model for calculation, and calculate the benefits of 10 ports under the two schemes respectively. After comparison, it is learned that the benefit of option 1 is much higher than that of option 2 in 2020 to 2040. Figure 11 shows Eyemouth port as an example to show the difference revenue comparison by year, for all ports revenue info, refer Appendix A.

关注数学模型 The strategy of small fishing companies In the interval from 2020 to 2040, the benefits of Option 1 in the 10 ports are far greater than Option 2, and at this time, Option 1, relocation is an optimal choice. After 2040, since all ports except Shetland will not be able to use Option 1, in the period from 2040 to 2070, we cannot compare the advantages and disadvantages of the two options, and we can only choose Option 2 and purchase fishing boats with refrigeration devices to harvest.

5.3 The impact of the transfer of fisheries to neighboring territorial waters

As the temperature of the ocean continues to rise, the fish populations in the waters around Scotland, including herring and mackerel, will gradually migrate northward, eventually migrating to the Norwegian Sea and distributed along the Norwegian coastline. At this time, the fishery has entered the territorial sea of the neighboring country. For our strategy, the biggest impact is that offshore fishing may not be possible, because at this time option 1 has expired, and only new fishing vessels of option 2 are available. However, fishing vessels face the problem of being unable to enter Norwegian territorial waters to compete for Norwegian fishing quotas. The European Union has divided fishing areas for each country along the North Atlantic Ocean, and each country has fishing quotas. As a matter of fact, as early as 2009, there was a serious loss of mackerel in Norway due to early sea temperature changes due to sea temperature changes [11]. Our model cannot specifically estimate the impact, but can only be assessed through data.

6 Sensitivity analysis

When deciding a business strategy for a small fishery company, the speed of the ship v , the price of the fish S , and the weight of the cargo that the ship can carry W will vessel max affect the decision-making income. Here we fix two of these variables and observe the change in the other variable Impact.

6.1 Impact of ship speed on strategy revenue

The speed of a fishing boat can affect the length of its period time. We fixed the price of the fish S at 883.75 pound and the payload W of 30 tons. We increased the ship speed max v from 14.1km/h linearly in steps of 2 to 22.1km/h. The income curve corresponding to the vessel two options was plot and shown in Figure 12 and Figure 13

关注数学模型 It can be seen from the figure that the benefit of option 1 is much higher than that of option 2. The speed is proportional to the income of all options. This is also intuitive. The higher the speed, the shorter the period and the greater the number of running fish. Option 2 also shows an interesting phenomenon. The income reached its maximum in 2030. This may be because after 2030, the school of fish is getting farther and farther from the port, leading to higher costs and lower income.

6.2 Impact of carrying capacity on strategy revenue

The carrying capacity determines the carrying capacity of the ship, which indirectly affects the level of revenue. We fixed the ship speed v at 18.1 km/h, and the price of fish S was vessel 883.75 pound. We increased the payload W linearly from 10 ton in steps of 10 to 50 ton, and max plotted the income change curves corresponding to the two options, as shown in Figure 14 and

关注数学模型 It can be seen from the figure that the benefit of option 1 is still much higher than that of option 2. The carrying capacity is proportional to the income of all options. This is also intuition. The larger the carrying capacity, the greater the number of fish in one run. Option 2 once again presents an interesting phenomenon. As the carrying capacity gradually increases, the influence of this factor on income has become increasingly prominent. This may be because the higher the carrying capacity, the higher the cost-effective ratio in long-distance transportation.

6.3 Impact of fish price on strategy revenue

The price of fish directly affects the company's revenue. We fixed the ship speed v at vessel 18.1km/h and the payload W capacity at 30 tons. We increased the price of fish linearly max from 683.75 pound in steps of 100 to 1083.75 pound, and plotted the income change curves corresponding to the two options, shown in Figure 16 and Figure 17.

关注数学模型 It can be seen from the figure that the benefit of option 1 is still much higher than that of option 2. The price of fish is proportional to the income of all options. The higher the unit price, the higher the total price.

7 Model Evaluation and Discussion

7.1 Model Evaluation

It is a very valuable topic to discuss the problem of biological migration and the related industry shocks caused by it in the context of global warming. The fact of global warming is clear, and the impact it brings can already be felt. In the light of an unknown future, making predictions and taking actions to turn disadvantages into opportunities is a challenge but valuable things. As a consultant, in order to predict sea temperature changes, we establish a simple but effective sea temperature prediction model. In order to simulate the operation of fish populations in the natural environment, we have established a cellular automaton model to set the cell's action mode. The data of ocean temperature changes were input into an automaton to simulate real fish school behavior. At the same time, we set up the xx model to make decisions for small fisheries companies.

We obtained real data from the official report for evaluation, so the model has real reference. At the same time, we conducted a sensitivity analysis of the model to analyze how our decisions will change under the influence of different parameters, and also proved that in some aspects, our model is stable.

Our innovation lies in the combination of cellular automata and temperature model to simulate the behavior of fish in the natural environment, and simulate the morphological changes and migration routes of fish.

But our model still has obvious flaws:

 The temperature prediction model is just a simple function superposition, which follows the trend of data changes since 2012 without considering the data of previous years, and the fitting is simpler. Temperature changes can be affected by many factors, and our model has fewer considerations.

 In order to simplify the analysis, in the cellular automata, we simply considered the effect of temperature on biological migration, superimposed a layer of temperature on the cellular space, and did not consider other factors, making the simulation behavior simple and not well fitted the actual situation.

 In the maximum range voyage model, because the company's ship parameters are different, the maximum range is also different, we can only predict the duration under one parameter.

 In the cost-benefit model, for option 1, we did not consider the optimal addressing algorithm, but assumed that the location was randomly selected during migration, which caused the model to have some randomness and not close to reality.

关注数学模型

7.2 Further Discussion

If we add more influential factors to the cellular automaton, such as ocean depth, ocean current factors, coastline, etc., we can more accurately fit the migration of biological habitats and some other behaviors.

In fact, some of the models we have a wider range of uses. Cellular automata models can arbitrarily add multiple factors, set complex behavior patterns to simulate real environments, or extend to land to simulate the evolution of terrestrial biological communities. Our value appraisal model can evaluate any task that fits the purchase of equipment and relocation.

9 An Article for Hook Line and Sinker (next page)

关注数学模型 Ready for the impact of global warming on fisheries?

As we all know, our world is getting hotter and hotter. Global warming has led to drastic changes in the ecological environment around the world. For small fishing companies in Scotland, this impact is also happening. As a consultant to the Scottish North Atlantic Fisheries Management Association, we are invited to publish our research in an article published in this magazine, in which we will analyze the effects of ocean warming on fish around Scotland, especially herring and mackerel The impact of habitat changes will also predict future fishery changes and provide strategic advice for the development and transformation of small fisheries companies.

Based on data from 2012, we have established a combined power and trigono- metric function model to predict the temp- erature of the seas around Scotland. The result of the prediction surprised us. In the next 20 years, the temperature in the waters around Scotland will reach 7 degrees Celsius, and the current temperature is only about 6 degrees C. In the next 50 years, 2070, the temperature in the seas around Scotland will reach 8 degrees The temperature in the English Channel rises to 9 degrees, and the waters near Norway will rise to 6.5 degrees.

As fishermen, we all know that herring and mackerel near Scotland are marine creatures that prefer low-temperature environments. The suitable temperature for herring is 5.6 degrees Celsius and mackerel is 6.6 degrees Celsius. In order to understand the changes in their habitats, we have established a cellular automaton to simulate the migration of two organisms in the next 50 years, see Figure 1. Both herring and mack- erel habitats gradually moved northward. Herrings set off from the North Sea, all the way along the European continent to the Norwegian coast, and mackerel moved westward from Scotland and finally north- ward to Shetland. In 2070, herring will live in the sea near Alesund, Norway, which is 801 km northeast of Scotland, mackerel will live in the sea which is 268km northwest of Bergen, Norway and 544 km northeast of Scotland.

But how will these migrations affect fisheries? So, we studied the range of a medium-sized fishing boat without refrigeration, and added this range to 10 Scottish ports. It is calculated that the maximum range of a medium-sized fishing boat is a circle with a radius of 108km, that is to say, fishermen can only operate around 108km of the port. After comparing the migration route of herring and mackerel with the operating range of the port, we have come to a more serious conclusion. In the case of the fastest temperature rise in the world, all ports except Shetland will not be able to fish after 21 years (2041). With these two species, at the slowest temperature changes, all ports except Shetland will not be able to fish after 33 years (2053).

In other words, if the company's business strategy is not changed, the company will face bankruptcy after 21 years. At that time, you will face the risk of losing job. By the way, Shetland has great potential in the future. Therefore, it is inevitable for small fisheries companies to change their operations. To this end, our team has established a value

关注数学模型 2070

2070

2050 2030 2050

2030

mackerel herring

evaluation model and provided two solutions for the company.

1. When the school of fish is gradually moving away from the port where the company is located, move some or all of the assets of the fishery company from the current location of the current port to a place closer to where both fish are moving

2. Purchase refrigerated fishing boats, increase the sailing range, expand the current operating range of the port, and wrap the school of fish in this range

Since all ports will not be able to reach fish schools after 2040, the purchase of refrigerated fishing vessels will become the only strategy. Therefore, we analyze the situation before 2040 and conclude that strategy 1 is more cost-effective. But after 2040, the purchase of new refrigerated fishing boats has become the only option for small Scottish fishing companies, and fishermen must drive new fishing vessels to begin their fishing operations. So, 2040 is an important time point to change the strategy. In addition, the movement of fish stocks may lead to the invalidation of the previous EU fishing resource quotas, because in the future, fish resources will be more concentrated in the cold sea waters near Norway, and it will be more difficult for Scottish fishers to harvest in their own area. In addition to the cost of buying fishing boats, fishing companies should also make long- term plans for future resource disputes with Norway.

In conclusion, we make the following recommendations for fishermen and small fisheries companies

1. Before 2040, if herring and macke- rel are too far away from the port, choosing to move to a closer port is a good choice

2. After 2040, if the same situation happens, choose to buy a new type of refrigerated fishing boat

3. Call on the Scottish Government to reassign fishery resource quotas wi- th other countries or regions as soon as possible, and call on Scottish fishermen to be treated fairly under climate change

4. Choose Shetland as the new address, the place is promising after 2050

5. Choose to catch other fish in warm environments and reduce the propor- tion of herring and mackerel

2020.2.17

关注数学模型

Appendices

Appendix A Plots

Temperature Plots

Port Revenue

关注数学模型 关注数学模型

Appendix B Code

MATLAB Source Code: Befit-Cost Model year_time = 365*24;%total hours of a year vessel_speed = 18.1;%vessel speed (km/h) mackerel_price = 883.75;%price of mackerel (Pound) max_weight = 30;%max weight for a vessel to load

distances_1 = unifrnd(0,108.6,10,50);%random distances from new port positions to fish group for option1

for i = 1:10 for j = 1:50 distances_2(i,j) = distance(P(i,:),[Lat_m(2020+j),Lon_m(2020+j)],6371);%Calculate distances base on predicted moving tracks for option2 end end

for i = 1:10 for j = 1:50 incomes_2(i,j) = 0.5 * year_time * vessel_speed * max_weight * mackerel_price / distances_2(i,j);%get the income of every year of option2 end end

for i = 1:10 for j = 1:50 incomes_1(i,j) = 0.5 * year_time * vessel_speed * max_weight * mackerel_price / distances_1(i,j);%get the income of every year of option1 end end

plot(2021:2040,incomes_2(10,1:20),'LineWidth',2,'Color',[0.93 0.57 0.13]);

关注数学模型 title('option1 vs option2 - Eyemouth - income change','Fontname', 'Times New Roman','FontSize',12); xlabel('time','Fontname', 'Times New Roman','FontSize',12); ylabel('income','Fontname', 'Times New Roman','FontSize',12); hold on; plot(2021:2040,incomes_1(10,1:20),'LineWidth',2,'Color',[0.2 0.63 0.79]); xlabel('time','Fontname', 'Times New Roman','FontSize',12); ylabel('income','Fontname', 'Times New Roman','FontSize',12); legend('option2','option1')

function result = Lat_m(i) %relationship between mackerel's latitude and time p1 = -1.02564110268265e-05; p2 =    0.0838756861891964; p3 =       -257.214494926180; p4 =      350557.892310225; p5 =       -179160687.207539;

result = p1*i.^4 + p2*i.^3 + p3*i.^2 + p4*i + p5; end

function result = Lon_m(i) %relationship between mackerel's lontitude and time p1 = 3.31002303239508e-06; p2 =    -0.0271224530551578; p3 =       83.3267494669017; p4 =      -113758.376474619; p5 =       58228997.7952488;

result = p1*i.^4 + p2*i.^3 + p3*i.^2 + p4*i + p5; end

function result = Lat_h(i) %relationship between herring's latitude and time p1 = -6.99300851104721e-07; p2 =    0.00585781010041642; p3 =       -18.3904758421972; p4 =      25646.9972197086; p5 =       -13405718.3436972;

result = p1*i.^4 + p2*i.^3 + p3*i.^2 + p4*i + p5; end

function result = Lon_h(i) %relationship between herring's lontitude and time p1 = 5.82750624265166e-06; p2 =    -0.0474655822679289; p3 =       144.974974325811;

关注数学模型 p4 =      -196793.870276591; p5 =       100172408.915139;

result = p1*i.^4 + p2*i.^3 + p3*i.^2 + p4*i + p5; end

MATLAB Source Code: CA for i=135:2:165 for j=105:2:120 if cells(i,j)==1 continue end cells(i,j)=2; end end escape = 0.8; idle = 0.1; optimalDegree = 10.2; degreeCubic = ones(7,7) * 10.2; sensitive = 0.1; sch=[]; skz=[]; t=1; [x,y]=size(cells); run=0; freeze=0; stop=0; while (stop==0) if(run==1) for i=2:x-1 for j=2:y-1 if(cells(i,j)~=1 && cells(i,j)~=0) eindex = abs(degreeCubic(idivide(int32(i),50,'floor') + 2, idivide(int32(j),50,'floor') + 2) - optimalDegree) - 5; sigmoid = 1/(1+exp(-eindex)); if (sigmoid < sensitive) if(rand<escape count = countNeibor(i,j,cells);

movchance = count / 8 + 0.2; if rand < movchance dx = rand; dy = rand; if(dx<0.3) dx=-1; elseif(dx <0.6) dx = 0;

关注数学模型 else dx = 1; end if(dy<0.3) dy=-1; elseif(dy <0.6) dy = 0; else dy = 1; end cells(i,j)=0; if cells(i+dx,j+dy) ~= 1 && cells(i+dx,j+dy) ~= 2 cells(i+dx,j+dy)=2; else cells(i,j)=2; end end end else if(rand<escape) if(rand < idle) dx = rand; dy = rand; if(dx<0.3) dx=-1; elseif(dx <0.6) dx = 0; else dx = 1; end if(dy<0.3) dy=-1; elseif(dy <0.6) dy = 0; else dy = 1; end cells(i,j)=0; if cells(i+dx,j+dy) ~= 1 && cells(i+dx,j+dy) ~= 2 cells(i+dx,j+dy)=2; else cells(i,j)=2; end continue; end

cx = idivide(int32(i),50,'floor') + 2; cy = idivide(int32(j),50,'floor') + 2; [dx,dy] = choseOptimalDegree(cx,cy, optimalDegree, degreeCubic); cells(i,j)=0; if (cells(i+dx,j+dy) ~= 1 && cells(i+dx,j+dy) ~= 2) cells(i+dx,j+dy)=2; else cells(i,j)=2; end

关注数学模型 end end end end end

Appendix A Data

Polynomial fitting parameters

Table: longitude Name Value P1 3.31002303239508e-06 P2 -0.0271224530551578 P3 83.3267494669017 P4 -113758.376474619 P5 58228997.7952488

Table: latitude Name Value P1 -1.02564110268265e-05;

P2 0.0838756861891964 P3 257.214494926180 P4 350557.892310225 P5 179160687.207539

Fishing port coordinates

Port Latitude Longtitude Port Latitude Longtitude Shetland 60 -1 Campbeltown 55 -5 Orkney 59 -3 Ayr 55 -5 Kinlochbervie 58 -5 Fraseburgh 57.5 -1.9 Stornoway 58 -6 Anstruther 56 -2.7 Portree 56 -6 Eyemouth 55.7 -2

关注数学模型
