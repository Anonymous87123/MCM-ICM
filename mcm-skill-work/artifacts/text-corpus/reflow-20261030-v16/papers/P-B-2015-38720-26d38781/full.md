# P-B-2015-38720-26d38781

Status: machine-draft; not source-verified.


<!-- b000001 | title | pages [1] -->
Hidden in Plane Sight:

<!-- b000002 | title | pages [1] -->
Finding Lost Airplanes Before Time Runs Out

<!-- b000003 | prose | pages [1] -->
When a plane disappears over remote waters, time is of the essence. The faster we learn the fate of the plane, the more likely it is that we can rescue survivors or bring closure to grieving families. In light of the failed search effort for Malaysia Flight MH370, we must strive to expedite and optimize response effectiveness in the future.

<!-- b000004 | prose | pages [1] -->
First we investigate how and where airplanes crash and discover that finding a lost plane begins with predicting its location based on variables such as flight speed, glide ratio, and altitude. We also consider the search plane’s speed and detection distance. Our simulations test different flight paths to determine which best minimizes search time and maximizes chances of finding the crash site debris.

<!-- b000005 | prose | pages [1] -->
● Where to look: ​ Projecting a commercial airplane’s flight path, we construct a Gaussian normal distribution bounded by a rectangular search area.

<!-- b000006 | prose | pages [1] -->
●

<!-- b000007 | heading | pages [1] -->
Simulate Solutions with Ideal Accuracy: ​

<!-- b000008 | prose | pages [1] -->
Assuming the search will certainly detect a wreck within radar range,​ ​ we test random flight paths, but they prove inefficient—the most successful takes 38 hours. By searching systematically, reducing redundancy and focusing on high probability areas, we cut mean search time to 3.6 hours.

<!-- b000009 | prose | pages [1] -->
●

<!-- b000010 | heading | pages [1] -->
Simulate Solutions with Imperfect Accuracy:​

<!-- b000011 | prose | pages [1] -->
We now incorporate uncertain detection probability into our model. Applying Bayesian Search Theory to our most efficient solution results in a relatively low mean search time of 4.7 hours, with 95% of crashes located within one day.

<!-- b000012 | prose | pages [1] -->
● Flexibility: ​ We can easily repurpose our solutions for different numbers of search planes or sizes of crashed planes.

<!-- b000013 | prose | pages [1] -->
Ultimately, our recommended solution — an application of Bayes' Theorem — takes a realistic and accurate approach to quickly find the majority of lost planes.

<!-- b000014 | furniture | pages [2] -->
Team #38720

<!-- b000015 | furniture | pages [2] -->
Page 2 of 61

<!-- b000016 | heading | pages [2] -->
Table of Contents

<!-- b000017 | heading | pages [2] -->
1 Introduction

<!-- b000018 | prose | pages [2] -->
4

<!-- b000019 | heading | pages [2] -->
2 Research

<!-- b000020 | prose | pages [2] -->
6 2.1 Amelia Earhart: A Crash that Haunted History 6 2.2 Malaysia Flight MH370: A Modern Day Example 6 2.3 An Analysis on the History of Ocean Plane Crashes 7 2.4 Oceanic Airspace Communication 10 2.5 History of Oceanic Search Theory 11 2.6 Search Planes and Sensors 12

<!-- b000021 | heading | pages [2] -->
3 Foundation of Analysis

<!-- b000022 | prose | pages [2] -->
13 3.1 Variables and Definitions 13 3.2 Determining a Realistic Scenario 15 3.3 Search Plane Calculations 18

<!-- b000023 | heading | pages [2] -->
4 Compilation of General Assumptions

<!-- b000024 | prose | pages [2] -->
20 4.1 Environmental 20 4.2 Crash 20 4.3 Search 21

<!-- b000025 | heading | pages [2] -->
5 Models

<!-- b000026 | prose | pages [2] -->
22 5.1 Normal Distribution 22 Solution 5.1.1: Completely Random Flight Path 24 Solution 5.1.2: Bounded Random Flight Path 26 Solution 5.1.3: Bounded Weighted Random Flight Path 29 Solution 5.1.4: Descending Striped Flight Path 32 Solution 5.1.5: Spiral Striped Flight Path 35 Solution 5.1.6: Sinusoidal Flight Path 38 5.2 Normal Distribution with Discovery Uncertainty 41 Solution 5.2.1: Bayesian Adjusted Flight Paths 44 Solution 5.2.2: Spiral Striped Flight Path 47

<!-- b000027 | furniture | pages [3] -->
Team #38720

<!-- b000028 | furniture | pages [3] -->
Page 3 of 61

<!-- b000029 | heading | pages [3] -->
6 Solution Stability

<!-- b000030 | prose | pages [3] -->
49 6.1 Bayesian Adjusted Flight Path with a lost Cessna 172 49 6.2 Two Planes Flying Striped Patterns 51

<!-- b000031 | heading | pages [3] -->
7 Results

<!-- b000032 | prose | pages [3] -->
53 7.1 The Normal Distribution Model 53 7.2 Discovery Uncertainty Model 54

<!-- b000033 | heading | pages [3] -->
8 Conclusion

<!-- b000034 | prose | pages [3] -->
56 8.1 Recommendation 56 8.2 Strengths and Weaknesses of Recommendation 57

<!-- b000035 | heading | pages [3] -->
9 Press Conference Document

<!-- b000036 | prose | pages [3] -->
58

<!-- b000037 | heading | pages [3] -->
10 References

<!-- b000038 | references | pages [3] -->
59

<!-- b000039 | furniture | pages [4] -->
Team #38720

<!-- b000040 | furniture | pages [4] -->
Page 4 of 61

<!-- b000041 | heading | pages [4] -->
1 Introduction

<!-- b000042 | prose | pages [4] -->
Despite modern design and tracking capabilities, airplanes such as Malaysian flight MH370 occasionally disappear over swathes of open ocean. With no communication from the downed plane, searchers must determine the optimal strategy for recovery. Meanwhile, family members of passengers wait anxiously for news of their loved ones’ fates.

<!-- b000043 | prose | pages [4] -->
The Dilemma:

<!-- b000044 | prose | pages [4] -->
● The primary objective is to find the missing plane.

<!-- b000045 | prose | pages [4] -->
● Our second consideration is to reduce the time it takes to find the plane and any surviving passengers, improving the odds of rescuing them alive.

<!-- b000046 | prose | pages [4] -->
● In addition, we will take into account the different types of downed planes, search planes, and sensors.

<!-- b000047 | prose | pages [4] -->
The Approach:

<!-- b000048 | prose | pages [4] -->
● First we examine historic plane crashes to build context—their locations, causes, and the potential downed planes involved.

<!-- b000049 | prose | pages [4] -->
● Taking into account various communication methods and FAA regulations, we determine what constitutes a plane “lost” and the time it takes to reach that conclusion.

<!-- b000050 | prose | pages [4] -->
● We learn about the origin and evolution of ocean search technique.

<!-- b000051 | prose | pages [4] -->
● We research various search planes and sensors to find their speed, sight, and accuracy.

<!-- b000052 | prose | pages [4] -->
● We define all the variables we will use throughout the development of our model.

<!-- b000053 | prose | pages [4] -->
● Using our chosen downed plane specifications, we calculate the maximum search area that we need to consider.

<!-- b000054 | prose | pages [4] -->
● Based on our crash research, we determine the probability distribution of downed planes within the search area.

<!-- b000055 | furniture | pages [5] -->
Team #38720

<!-- b000056 | furniture | pages [5] -->
Page 5 of 61

<!-- b000057 | prose | pages [5] -->
● Using our chosen search plane specifications, we calculate the maximum speed, search sight, and accuracy to be used in our solutions.

<!-- b000058 | prose | pages [5] -->
● We outline all the assumptions we need to begin modeling.

<!-- b000059 | prose | pages [5] -->
● We numerically model lost airplanes with our chosen distribution inside the search area and evaluate random, striped, and sinusoidal search solutions.

<!-- b000060 | prose | pages [5] -->
● Increasing the complexity of our model, we consider what would happen to the search time if we have non-ideal sensor accuracy and redistribute the probability after each pass.

<!-- b000061 | prose | pages [5] -->
● We will simulate our normal model using different inputs to examine the effectiveness and flexibility of our best solutions when searching for varying kinds of downed planes.

<!-- b000062 | prose | pages [5] -->
● Based on our simulation results, we will analyze our generated data and make recommendations for a useful procedure for finding lost airplanes crashed in open water.

<!-- b000063 | furniture | pages [6] -->
Team #38720

<!-- b000064 | furniture | pages [6] -->
Page 6 of 61

<!-- b000065 | heading | pages [6] -->
2 Research

<!-- b000066 | heading | pages [6] -->
2.1 Amelia Earhart: A Crash that Haunted History

<!-- b000067 | prose | pages [6] -->
Mankind resides in a state of perpetual discontent staying static while barriers remain unbroken. We first achieved controlled and sustained flight on December 17, [1]​. Although the Wright Brother’s flight only lasted a mere 12 seconds, the 1903​ barrier of controlled flight is one mankind sought to break from centuries.

<!-- b000068 | prose | pages [6] -->
Aviators realized sustained flight opened a door to a land of infinite possibilities. Amelia Earhart, renowned for her advocacy of women’s rights, became [2]​. Earhart’s thirst for achieving new the first woman to fly across the Atlantic in 1928​ heights, both socially and aeronautically, became the characteristic that would bring her both fame and, sadly, an untimely death.

<!-- b000069 | prose | pages [6] -->
On the morning of July 2, 1937, Amelia set off to land on Howland Island, a [2]​. Her projected flight path, an astounding tiny, remote island in the south Pacific​ 2,556 miles, was the most difficult of her career. Historians believe Earhart’s communication antenna broke off mid flight, hindering her ability to receive navigation instructions. Due to a series of storms, her plane ran out of fuel and she [2]​. crashed into the dark waters of the south Pacific​ Although her plane was not the first to crash in open water, the unresolved loss of a celebrated aviation hero captured the attention the world. Earhart’s disappearance yielded one of the largest search parties of all time. Fragments of her [2]​. Though both plane were finally found last year, 77 years after her initial crash​ airplane and search technology have improved drastically since that time, the heartbreaking mysteries of lost planes continue to occur.

<!-- b000070 | heading | pages [6] -->
2.2 Malaysia Flight MH370: A Modern Day Example

<!-- b000071 | prose | pages [6] -->
[3]​ that have gone missing over Over the last hundred years, there are 89 planes​ the ocean, never to be found again. We decided to investigate the disappearance of Malaysia Flight MH370 as it seemed to be the most modern and applicable case study.

<!-- b000072 | furniture | pages [7] -->
Team #38720

<!-- b000073 | furniture | pages [7] -->
Page 7 of 61

<!-- b000074 | prose | pages [7] -->
[4]​. On March 4, 2014, MH370 departed from Kuala Lumpur en route to Beijing​ Air traffic control lost contact with the plane only 38 minutes after departure, and the last known position and orientation of the plane was less than 2 hours from takeoff. With its fuel capacity nearly full, analysts have determined that the radius of the search area is equal to the maximum distance the plane could have flown with the fuel it [4]​. Fortunately, had onboard​ satellites received signals from MH370 thousands of miles southwest from the last point of contact, effectively narrowing down the search area with high probability.

<!-- b000075 | prose | pages [7] -->
This signal, although not identical to our problem, gave us insight as to how analysts determine search areas and, more specifically, search areas with high probability of success.

<!-- b000076 | prose | pages [7] -->
From the information from MH370 (Figure 1), we determined the search area to [4]​. be basically rectangular in shape, with the expected flight path in the middle​

<!-- b000077 | heading | pages [7] -->
2.3 Analysis of the History of Ocean Plane Crashes

<!-- b000078 | prose | pages [7] -->
Obviously, the two case studies we have already discussed are not a firm basis to [3]​ for us develop our models around. However, there are 88 other missing plane cases​ to examine. If we examine the Aviation Safety Network’s database of lost flights from 1948-2014, we can determine the most common locations, types of planes, and crash [3]​. causes upon which to base our models​

<!-- b000079 | prose | pages [7] -->
Locations:

<!-- b000080 | prose | pages [7] -->
● 31 of the 89 missing flights list the Atlantic Ocean as the place of [3]​. disappearance, exactly half of the 62 oceanic disappearances​

<!-- b000081 | prose | pages [7] -->
● These flights vary in type from transatlantic to shorter hops between islands ​ (Figure 2)​ .

<!-- b000082 | furniture | pages [8] -->
Team #38720

<!-- b000083 | furniture | pages [8] -->
Page 8 of 61

<!-- b000084 | prose | pages [8] -->
● Considering the abundance of aircraft missing without a trace from the Atlantic region, as well as the diversity of flight paths of those planes, we believe that analyzing this ocean specifically will provide the best representation of possible flights in need of rescue.

<!-- b000085 | prose | pages [8] -->
Airplane Categories:

<!-- b000086 | prose | pages [8] -->
● For simplification, we wish to consider only the most common type of missing plane—passenger aircraft—including commercial, business, and [3]​. privately owned​

<!-- b000087 | prose | pages [8] -->
● We also want the specific examples of each type of plane to be commonly available and frequently used around the Atlantic region.

<!-- b000088 | prose | pages [8] -->
Jumbo Commercial Wide-Body: The twin engine Boeing 777-200, ○ seating a maximum of 440 passengers, often flies the popular [5]​. transatlantic route from London to New York​

<!-- b000089 | prose | pages [8, 9] -->
Large Business Jet: The Gulfstream G450, a long range ○ twin-engine aircraft, is a common choice for companies to take up [6]​. to 16 passengers between continents​ Small Personal Aircraft: The best-selling aircraft of all time, the 4 ○ passenger single engine Cessna 172 is flown by private citizens [7]​. across the Atlantic with land-based or ferry stops for refueling​

<!-- b000090 | furniture | pages [9] -->
Team #38720

<!-- b000091 | furniture | pages [9] -->
Page 9 of 61

<!-- b000093 | prose | pages [9] -->
● For our models, we will consider the Boeing 777, Gulfstream G450, and Cessna 172 as standard examples of potential missing aircraft.

<!-- b000094 | prose | pages [9] -->
Causes of Historical Plane Crashes

<!-- b000095 | prose | pages [9] -->
In order to evaluate the types of plane crashes we will need to consider, we first broke down notable oceanic plane crashes into several categories; the number inside [8]​. the parenthesis is the number of cases of this type reported​

<!-- b000096 | prose | pages [9] -->
Types of Incidents We Will Consider:

<!-- b000097 | prose | pages [9] -->
● Stall-related (82): Commonly, stalls are caused by icing of a plane’s wings, icing and failure of speed indicators causing a steep climb, and [8]​. failure of ailerons or other stabilizing equipment​

<!-- b000098 | prose | pages [9] -->
● Engine Failure/Quick Descent (52): Crashes of this nature could result from bird strikes, explosions/failure in a plane’s engines, cabin fires, [8]​. navigational equipment failure and loss of cabin pressure in flight​

<!-- b000099 | prose | pages [9] -->
● Sustainable Glide (9): Glides are some of the most rare crashes. Pilots must experience loss of thrust capability while still maintaining control of their aircraft—an unlikely combination. Potential causes include [8]​. complete engine failure and fuel starvation​

<!-- b000100 | prose | pages [9] -->
Types of Incidents We Will Disregard:

<!-- b000101 | prose | pages [9] -->
● Air Traffic Control: Crashes related to an ATC error most likely happen [8]​; neither of these situations apply to our during takeoff and landing​ models because we are only discussing mid-flight incidents where the plane would be over water.

<!-- b000102 | prose | pages [9] -->
● Hijacking: The search area of a plane that has been hijacked can be extremely wide because we must assume the plane is still fully [8]​. No reliable search area could be created if operational​ communication ceases and the hijackers are in control of the plane.

<!-- b000103 | furniture | pages [10] -->
Team #38720

<!-- b000104 | furniture | pages [10] -->
Page 10 of 61

<!-- b000105 | heading | pages [10] -->
2.4 Oceanic Airspace Communication

<!-- b000106 | prose | pages [10] -->
It seems unbelievable in this day and age, with GPS technology readily available and easy to use, that a vehicle as large and seemingly conspicuous as an airplane could be lost without a trace. In truth, the massive oceans that cover the majority of Earth’s surface present a remote and dangerous wilderness for any plane unfortunate enough to crash there.

<!-- b000107 | prose | pages [10] -->
Radar Tracking:

<!-- b000108 | prose | pages [10] -->
● Radar is a relatively old and well-tested technology used for determining the positions of ships and aircraft; however, the range of civilian radar [9]​. extends only 200 miles from the coastline​

<!-- b000109 | prose | pages [10] -->
● On a typical New York-to-London transatlantic flight, the plane would be out of radar range while over the ocean for more than half the flight [9]​. time​

<!-- b000110 | prose | pages [10] -->
Air Traffic Control:

<!-- b000111 | prose | pages [10] -->
● During oceanic flights, multiple control towers from different countries exchange control of the aircraft.

<!-- b000112 | prose | pages [10] -->
● Some crashes, such as Air France Flight 447, involve a botched exchange where no one raises an alarm that the plane is missing for several [10]​. We must assume this will not be the case. hours​

<!-- b000113 | prose | pages [10] -->
● Older planes and outdated control towers, common in less-developed countries, use high frequency radio while the plane is out of regular [10]​. radio and radar range. Communication occurs about once per hour​

<!-- b000114 | prose | pages [10] -->
● Modern satellite-based systems, used in the US, Europe, and Canada, [10]​. mandate 14-minute update cycles and provide much more accuracy​

<!-- b000115 | prose | pages [10, 11] -->
● The Federal Aviation Administration’s Oceanic Emergency Procedures state that a gap in communication of 30 minutes or longer is cause for an [11]​. escalating emergency state​ ● We will account for both methods of ATC communication by following the FAA’s guidelines. A lapse of half an hour means that the plane began crashing and lost communication capabilities sometime within that interval.

<!-- b000116 | furniture | pages [11] -->
Team #38720

<!-- b000117 | furniture | pages [11] -->
Page 11 of 61

<!-- b000119 | heading | pages [11] -->
2.5  History of Oceanic Search Theory

<!-- b000120 | prose | pages [11] -->
The branch of applied mathematics known as “Search Theory” originated during World War II as a method for locating enemy ships, and was quickly adapted for [12]​. These historical searchers had an rescuing airmen that crash-landed in the ocean​ advantage over our situation due to abundance of manpower and the frequency of [12]​. military radio contact; they generally knew the exact moment the plane crashed​ This information allowed the searchers to look radially outward from the point of lost contact and quickly perform their rescue.

<!-- b000121 | prose | pages [11] -->
Our Theory:

<!-- b000122 | prose | pages [11] -->
● Our models will be more complex than this early one, but follow the concepts developed by past search theorists.

<!-- b000123 | prose | pages [11] -->
● A savvy searcher must weigh two elements: the probability that a given area contains the lost plane and the probability that the searcher will detect the lost plane while searching that area.

<!-- b000124 | prose | pages [11] -->
These are referred to in Search Theory as Probability of ○ [12]​. Containment​ P(C)​ and Probability of Detection ​ P(D)​

<!-- b000125 | prose | pages [11] -->
● The total probability of finding the downed plane is then the [12]​. product of P(C) and P(D)​

<!-- b000126 | prose | pages [11] -->
(1)

<!-- b000127 | prose | pages [11] -->
● The best search technique would clearly start at places that total probability is highest and then continue searching through areas of decreasing probability.

<!-- b000128 | prose | pages [11] -->
● Our models will need to cover different probability distributions of airplane containment to discover which is the most accurate

<!-- b000129 | prose | pages [11] -->
● The P(D) will depend on the type of sensor we select.

<!-- b000130 | furniture | pages [12] -->
Team #38720

<!-- b000131 | furniture | pages [12] -->
Page 12 of 61

<!-- b000132 | heading | pages [12] -->
2.6 Search Planes and Sensors

<!-- b000133 | prose | pages [12] -->
The most ancient method for detection of lost objects is visual. Besides the obvious inefficiency of searching thousands of square miles of ocean by vision alone, the [12]​. For this model for visual search accuracy is related to the inverse cube of distance​ reason, we will ignore visual search as both too ineffective and too complex to model.

<!-- b000134 | prose | pages [12] -->
The two most common types of search planes are military aircraft—the older P-3 [13]​. The Orion carries revolving multi-mode radar for Orion and the new P-8 Poseidon​ broad sweeps to detect debris as well as infrared and acoustic sensors for smaller [13]​. For the modern plane, data on its sensing capabilities is classified, but searches​ we can find specifications for a much older model that the current sensors are based [14]​. on​

<!-- b000135 | prose | pages [12] -->
Usually, once the radar search discovers likely debris, a more focused infrared scan will cover the surrounding area to spot the residual heat signature of the submerged [15]​.​ plane​ For the sake of simplification in our first model, we will focus on the radar search and imagine that it is an ideal sensor with 100% effective probability of detection and no range uncertainty.

<!-- b000136 | furniture | pages [13] -->
Team #38720

<!-- b000137 | furniture | pages [13] -->
Page 13 of 61

<!-- b000138 | heading | pages [13] -->
3 Foundation of Analysis

<!-- b000139 | heading | pages [13] -->
3.1  Variables and Definitions

<!-- b000140 | prose | pages [13] -->
Lost Plane Variables:

<!-- b000141 | prose | pages [13] -->
Name of Variable (Symbol) Definition (Units)

<!-- b000142 | prose | pages [13] -->
The typical speed of an aircraft (mph) Cruising Speed ( ) v

<!-- b000143 | prose | pages [13] -->
The typical altitude of a transatlantic flight for the Cruising Altitude ( α ) specific type of aircraft (ft)

<!-- b000144 | prose | pages [13] -->
The total time from last contact (hr) Total Time Elapsed ( T )

<!-- b000145 | prose | pages [13] -->
Time of Last Contact The time an airplane last relayed its heading and coordinates to ground control—the last evidence of ( T = 0 ) normal operations (hr)

<!-- b000146 | prose | pages [13] -->
Point A’ The plane’s coordinates at last contact (mi, mi)

<!-- b000147 | prose | pages [13] -->
Failure The instant when the plane crashes: communications and normal operations stop, and thrust ceases

<!-- b000148 | prose | pages [13] -->
The max distance a plane can move after failure (mi) Glide Range ( ) r

<!-- b000149 | prose | pages [13] -->
The ratio of horizontal distance covered to altitude [16]​ ( Glide Ratio​ κ ) lost that maximizes total horizontal distance (none)

<!-- b000150 | prose | pages [13] -->
0.5 hr, the time window in which the airplane could Crash Uncertainty Time ( ) τ have crashed

<!-- b000151 | prose | pages [13] -->
The time controllers first suspect a problem when Time of First Alert ( T = τ ) the plane misses a routine communication (hr)

<!-- b000152 | prose | pages [13] -->
Point B’ The plane’s expected location if it flew for exactly time  after last contact but before failure (mi, mi) τ

<!-- b000153 | prose | pages [13] -->
The maximum distance an airplane can cover at Distance ( L ) cruising speed in time (mi) τ

<!-- b000154 | prose | pages [13, 14] -->
Points A and B The points at the beginning and end of the flight path segment contained in the search area (mi, mi) Search Variables:

<!-- b000155 | furniture | pages [14] -->
Team #38720

<!-- b000156 | furniture | pages [14] -->
Page 14 of 61

<!-- b000158 | prose | pages [14] -->
Name of Variable (Symbol) Definition (Units)

<!-- b000159 | prose | pages [14] -->
The typical speed of a search aircraft (mph) Searching Speed ( v s )

<!-- b000160 | prose | pages [14] -->
The radius of the detection area (mi) Sight ( ) d

<!-- b000161 | prose | pages [14] -->
The vertical height above the water that the search Searching Altitude ( ) a plane flies (ft)

<!-- b000162 | prose | pages [14] -->
The time from the start of the search to present (hr) Search Time Elapsed ( )t

<!-- b000163 | prose | pages [14] -->
The straight line distance from the search plane to Distance to Lost Plane ( ) l lost plane debris (mi)

<!-- b000164 | prose | pages [14] -->
The approximate rectangular area taken up by the Size of Lost Plane ( Z ) 2​) lost plane (ft​

<!-- b000165 | prose | pages [14] -->
The location along the surface of the ocean in the Coordinates ( ) x , y x-y plane (mi, mi)

<!-- b000166 | prose | pages [14] -->
The position of the lost plane (mi, mi) Crash Coordinates ( xc   c ) , y

<!-- b000167 | prose | pages [14] -->
→ The position vector of the search plane Position ( ) S

<!-- b000168 | prose | pages [14] -->
Direction (ε) The direction of the search plane, either left or right, for striped and sinusoidal solutions (either 1 or -1)

<!-- b000169 | prose | pages [14] -->
Distance from search plane Distance from the plane to point A (mi) to A (d​ A​)

<!-- b000170 | prose | pages [14] -->
Distance from search plane Distance from the plane to point B (mi) to B (d​ B​)

<!-- b000171 | prose | pages [14] -->
j An index used for sequences in striped and sinusoidal solutions

<!-- b000172 | prose | pages [14] -->
A temporary variable for the striped and sinusoidal Temporary ( ) u solutions

<!-- b000173 | furniture | pages [15] -->
Team #38720

<!-- b000174 | furniture | pages [15] -->
Page 15 of 61

<!-- b000175 | heading | pages [15] -->
3.2 Determining a Realistic Scenario

<!-- b000176 | prose | pages [15] -->
Design of Search Area:

<!-- b000177 | prose | pages [15] -->
To analyze and effectively develop a maximum search area, we must assume that in some cases the plane will glide perfectly, encountering absolutely no stalls. This will give us the glide range of the aircraft—the maximum distance the plane could have deviated from the flight path.

<!-- b000178 | prose | pages [15] -->
(2)

<!-- b000179 | prose | pages [15] -->
We must also consider the distance the plane traveled between A’ and B’ over the 30 minute time period in which it could have crashed. Because we assume the velocity of the plane is constant, we can conclude:

<!-- b000180 | prose | pages [15] -->
(3)

<!-- b000181 | prose | pages [15] -->
It’s unknown exactly where the aircraft crashed along the flight path, so we must sweep a circle with radius  along the entire segment of length to cover every r L possible crash site. For modeling simplicity, we are also going to include the corners bordering the circles in our search area (Figure 3).

<!-- b000182 | furniture | pages [16] -->
Team #38720

<!-- b000183 | furniture | pages [16] -->
Page 16 of 61

<!-- b000184 | prose | pages [16] -->
Specifications of Downed Plane:

<!-- b000185 | prose | pages [16] -->
Based on our research, we constructed three different categories of aircraft (as discussed in Section 2.3) and chose one specific model of aircraft for each category based on frequency of transatlantic flights. We compiled their specifications below:

<!-- b000186 | prose | pages [16] -->
We decided to use the Boeing 777 as the specific example to base our model on for several reasons.

<!-- b000187 | prose | pages [16] -->
● The Boeing 777 was the aircraft involved in the disappearance of Malaysia Flight MH370.

<!-- b000188 | prose | pages [16] -->
● The 777 has a search area smaller than the Gulfstream but larger than the Cessna, making it a good compromise.

<!-- b000189 | prose | pages [16] -->
● Out of the three planes, the 777 is by far the largest with the most potential for debris, making it the easiest to detect.

<!-- b000190 | prose | pages [16] -->
● This type of airplane commonly makes transatlantic flights with many passengers, making it especially important that it is found quickly.

<!-- b000191 | prose | pages [16] -->
The data we will use for the lost plane in our models is as follows:

<!-- b000192 | prose | pages [16] -->
L = 320 miles r = 100 miles Dimensions of search Area = 520 miles along the x-axis by 200 miles along the y-axis.

<!-- b000193 | furniture | pages [17] -->
Team #38720

<!-- b000194 | furniture | pages [17] -->
Page 17 of 61

<!-- b000195 | prose | pages [17] -->
Probability Distribution of Downed Plane:

<!-- b000196 | prose | pages [17] -->
Given our calculated search area, we must determine the probability of the plane being at any specific place within the rectangle. From the plane crash information discussed in Section 2.3, we conclude that this probability of containment, P(C), would not be equal at every point within the area. In fact, very few crashing planes could be capable of a perfect glide. Additionally, even if a perfect glide was possible, the pilot would attempt to keep the plane headed along the flight path unless he or she completely lost control. ​ From data of recorded crashes we can assume that the majority of planes would crash into the ocean either directly below or near the flight path.

<!-- b000197 | prose | pages [17] -->
Recalling our search area design, outlined by circles of radius ​ r centered along the segment from A’ to B’, we must consider that no planes fail on the flight path between Points A and A’ and between B’ and B. Any crashed planes in these areas glided there from along ​ L​ , so there should be [12]​. Unfortunately, taking this into fewer here than near the rest of the flight path​ account makes the distribution significantly more complex (Figure 4).

<!-- b000198 | prose | pages [17] -->
To simplify the distribution for greater ease in modeling later, we will imagine that just as many planes end up between Points A and A’ and between B’ and B as along the rest of the flight path (Figure 5). ​ Therefore, we can reasonably conclude that the probability of the plane’s location is evenly distributed parallel to the flight path (x-axis). A normal distribution centered on the flight path can reasonably represent the probability of the plane’s location [12]​. parallel to the y-axis​

<!-- b000199 | furniture | pages [18] -->
Team #38720

<!-- b000200 | furniture | pages [18] -->
Page 18 of 61

<!-- b000201 | heading | pages [18] -->
3.3  Search Plane Calculations

<!-- b000202 | prose | pages [18] -->
Sensor Sight and Determining Search Plane:

<!-- b000203 | prose | pages [18] -->
We will use different methods to calculate the sight radius for our two potential search planes.

<!-- b000204 | prose | pages [18] -->
P-8 Poseidon:

<!-- b000205 | prose | pages [18] -->
An engineering report for the sensor we decided to use for this aircraft recommends an altitude of 1000 ft and an average sight range of 10 miles for maximum probability [14]​. Although we are using outdated sensor of detection​ information, we can find the specifications of the plane [13]​. It is not itself that list its search speed as 400 mph​ outside the realm of reason to assume that the plane’s classified sensors are capable of at least the same accuracy as the old sensors at this high speed.

<!-- b000206 | prose | pages [18] -->
P-3 Orion:

<!-- b000207 | prose | pages [18] -->
We found a specification sheet for the P-3’s AN/APS-115B radar that listed the range for search purposes as variable [16]​; however we were unable to determine recommendations for from 0 to 20 miles​ [18]​ and an altitude of 650 ft​ [13]​. accuracy. The P-3 has a speed of 375 mph​

<!-- b000208 | prose | pages [18] -->
Type of Speed of Type of Sensor Typical Search Sensor Sight Plane Search Plane Altitude  (ft) Range (mi) a d (mph) v s

<!-- b000209 | prose | pages [18] -->
[18] [13] [16] P-3 Orion 375​ AN/APS-115B 650​ 0-20​ radar

<!-- b000210 | prose | pages [18, 19] -->
[13] [14] [14] P-8 400​ AN/APS-119 1,000​ 10​ [14] Poseidon radar​ We choose the P-8 Poseidon as our specific search plane.

<!-- b000211 | furniture | pages [19] -->
Team #38720

<!-- b000212 | furniture | pages [19] -->
Page 19 of 61

<!-- b000214 | prose | pages [19] -->
● The P-8 is the more modern of the two search planes with a higher flight speed.

<!-- b000215 | prose | pages [19] -->
● We were unable to find any accuracy data for the P-3’s sensors, making the P-8 a more realistic choice.

<!-- b000216 | prose | pages [19] -->
The data we will use for the search plane in our models is as follows:

<!-- b000217 | prose | pages [19] -->
= 400 miles per hour v s = 10 miles d

<!-- b000218 | prose | pages [19] -->
Search Path:

<!-- b000219 | prose | pages [19] -->
For each variation of the model we will develop one or more solutions that answer the question: how should our search plane determine its route to find the downed plane in the shortest amount of time?

<!-- b000220 | furniture | pages [20] -->
Team #38720

<!-- b000221 | furniture | pages [20] -->
Page 20 of 61

<!-- b000222 | heading | pages [20] -->
4 Compilation of General

<!-- b000223 | heading | pages [20] -->
Assumptions:

<!-- b000224 | heading | pages [20] -->
4.1. Environmental

<!-- b000225 | prose | pages [20] -->
● We will assume that the Earth is flat, so planes travel between locations on a linear path.

<!-- b000226 | prose | pages [20] -->
● Wind and ocean currents will not affect the lost plane.

<!-- b000227 | prose | pages [20] -->
● We will use the Atlantic ocean as the basis for our model and solutions.

<!-- b000228 | prose | pages [20] -->
● All airplanes are required to transmit to Air Traffic Control every half an hour. An oceanic ATC tower will be responsible for listening for the plane’s regular communications at all times, and will notice when the plane stops responding.

<!-- b000229 | heading | pages [20] -->
4.2. Crash

<!-- b000230 | prose | pages [20] -->
● The airplane will experience the crash -causing failure instantaneously over water somewhere between Point A’ and Point B’, and will not deviate from the flight path until that instant.

<!-- b000231 | prose | pages [20] -->
This failure is equally likely to occur at any point between A’ and ○ B’.

<!-- b000232 | prose | pages [20] -->
● The airplane will lose all communication capacity during and after the failure.

<!-- b000233 | prose | pages [20] -->
● The airplane cannot travel further than its glide range from the point that failure occurs in any direction from the flight path.

<!-- b000234 | prose | pages [20] -->
● The search area for a Boeing 777 is simplified to a rectangle 520 miles long by 200 miles wide.

<!-- b000235 | prose | pages [20] -->
We will set this area on a coordinate system where the flight path ○ is the x-axis (y=0) and Point A is the origin (0, 0).

<!-- b000236 | furniture | pages [21] -->
Team #38720

<!-- b000237 | furniture | pages [21] -->
Page 21 of 61

<!-- b000238 | prose | pages [21] -->
The rectangle is bounded by the points (0, 100), (520, 100), (520, ○ -100), (0, -100).

<!-- b000239 | prose | pages [21] -->
● The downed airplane will remain on the ocean floor directly under where it lands.

<!-- b000240 | prose | pages [21] -->
● The crash will result in visible debris on the surface of the ocean proportional to the size of the downed airplane.

<!-- b000241 | prose | pages [21] -->
● The probability of containment P(C) follows a normal distribution of three standard deviations across the search area, centered on the flight path.

<!-- b000242 | heading | pages [21] -->
4.3. Search

<!-- b000243 | prose | pages [21] -->
● The debris does not move from directly above the body of the submerged plane.

<!-- b000244 | prose | pages [21] -->
Finding the debris is equivalent to finding the lost plane itself. ○

<!-- b000245 | prose | pages [21] -->
● The search effort will consist of one P-8 Poseidon plane (unless otherwise indicated) that searches continuously at 400 mph until it discovers the debris, without needing to stop for refuel or rest.

<!-- b000246 | prose | pages [21] -->
● Weather or sea conditions will not hinder the search effort or radar visibility.

<!-- b000247 | prose | pages [21] -->
● Cost and fuel are not an issue; the priority is rapidly finding the lost plane.

<!-- b000248 | prose | pages [21] -->
● The search plane will use radar with a sight range of 0 to 10 miles that is uniformly accurate for the entire range.

<!-- b000249 | prose | pages [21] -->
● The time for the search effort to mobilize is negligible and the search plane arrives instantaneously at the search area when calculating total search time.

<!-- b000250 | furniture | pages [22] -->
Team #38720

<!-- b000251 | furniture | pages [22] -->
Page 22 of 61

<!-- b000252 | heading | pages [22] -->
5 Models

<!-- b000253 | heading | pages [22] -->
5.1 Normal Distribution

<!-- b000254 | prose | pages [22] -->
This section contains all descriptions and testing done using our normal distribution model. Every solution contains a brief description, any equations used during simulations, a diagram of how the solution works, an example solution trial, the simulation data and a conclusion.

<!-- b000255 | heading | pages [22] -->
Model-Specific Assumptions:

<!-- b000256 | prose | pages [22] -->
● There are no false targets within the search area that could be confused with floating debris.

<!-- b000257 | prose | pages [22] -->
● The radar has a 100% probability of detection P(D) within its sight range.

<!-- b000258 | prose | pages [22] -->
Crash Simulation Technique:

<!-- b000259 | prose | pages [22] -->
In order to test the effectiveness of multiple solutions, we simulate plane crashes based on the normal distribution model. 5,000 of these crashes are displayed below:

<!-- b000260 | prose | pages [22] -->
We can see that the distribution is normal centered on the projected flight path (shown in red). Very few crashes end up outside of the blue search area.

<!-- b000261 | furniture | pages [23] -->
Team #38720

<!-- b000262 | furniture | pages [23] -->
Page 23 of 61

<!-- b000263 | prose | pages [23] -->
Completed Simulation:

<!-- b000264 | prose | pages [23] -->
For all solutions in this section, we define the completion of the search to be when the plane debris is found. In all our simulations, this is when the difference between the position of the search plane and the position of the crash debris is less than the sight range and is evaluated at every time step:

<!-- b000265 | prose | pages [23] -->
(4)

<!-- b000266 | prose | pages [23] -->
Essentially, this shows that any debris within the radius of the search plane’s radar will be spotted.

<!-- b000267 | prose | pages [23] -->
Statistical Analysis:

<!-- b000268 | prose | pages [23] -->
For each solution for which a large number of simulations can be generated, we perform basic statistical analysis. The mean, median, standard deviation, standard error of the mean, and 95% confidence interval are calculated. The standard error of the mean is the standard deviation of the sampling distribution of the mean, and is used to calculate the 95% confidence interval (CI). 95% of samples of the same size will fall within the CI. If the CI for two solutions overlap, there is no statistically significant difference between the two solutions. The equations expressing this relation are shown below:

<!-- b000269 | prose | pages [23, 24] -->
(5) Solution 5.1.1: Completely Random Flight Path

<!-- b000270 | furniture | pages [24] -->
Team #38720

<!-- b000271 | furniture | pages [24] -->
Page 24 of 61

<!-- b000273 | prose | pages [24] -->
A Brief Description:

<!-- b000274 | prose | pages [24] -->
In our first solution, we assume that the search plane will leave Point A and then travel randomly. Because we have no restrictive bounds on its route, the plane can move freely and will not necessarily stay within the search area.

<!-- b000275 | prose | pages [24] -->
How It Works:

<!-- b000276 | prose | pages [24] -->
The search plane will fly at constant velocity and will reevaluate its path every 15 → minutes, each time choosing a random normalized x and y component to form . The R time step is set at a relatively large value because the simulation would not be able to finish for a smaller step, because of the shear amount of data being generated.

<!-- b000277 | prose | pages [24] -->
→ Because is normalized, the length of the random vector will be 1. This random unit R vector will be multiplied by ​ Δ​ t​ , which represents the distance the search plane can v fly in a single time step.

<!-- b000278 | prose | pages [24] -->
The position of the plane at any time during the trial can be determined by:

<!-- b000279 | prose | pages [24] -->
(6)

<!-- b000280 | prose | pages [24] -->
Using Equation 6, we develop a simple solution to compare with future, more accurate search techniques. This relation is displayed below:

<!-- b000281 | furniture | pages [25] -->
Team #38720

<!-- b000282 | furniture | pages [25] -->
Page 25 of 61

<!-- b000283 | prose | pages [25] -->
A typical simulation of the search plane’s flight path as it moves randomly from Point A shows it flying well outside the search area. The dot representing the crashed plane is obscured by the solution at this scale.

<!-- b000284 | prose | pages [25] -->
Conclusion:

<!-- b000285 | prose | pages [25] -->
The problem with the above solution lies in its basic principle: the search plane frequently never finds the crashed aircraft because its path is unbounded. Because most simulations never finish, no consistent mean can be established from this particular model. Also, we can conclude that the completely random search method is not a viable option.

<!-- b000286 | furniture | pages [26] -->
Team #38720

<!-- b000287 | furniture | pages [26] -->
Page 26 of 61

<!-- b000288 | prose | pages [26] -->
Solution 5.1.2: Bounded Random Flight Path

<!-- b000289 | prose | pages [26] -->
A Brief Description:

<!-- b000290 | prose | pages [26] -->
Expanding from the completely random search solution, we decided to improve it with some “guidance”. We added the boundaries of our calculated search area to the solution in order to keep the search plane in the general vicinity of the crashed plane.

<!-- b000291 | prose | pages [26] -->
How It Works:

<!-- b000292 | prose | pages [26] -->
The search plane will fly at constant velocity and reevaluate its direction every 3 minutes. The time step is reduced to 3 minutes in this solution because these simulations generally finish quickly and the simulator can afford more precision. Just like the last solution, the plane will fly in a random direction; the distance between → each position will be kept constant by the normalized random vector. The search S i plane will be allowed to freely fly within the search area along the route described with the same equation used for the completely random solution in Section 5.1.1.

<!-- b000293 | prose | pages [26] -->
As soon as the plane leaves the box, it will be redirected orthogonally back into the search area in order to improve total search time.

<!-- b000294 | prose | pages [26] -->
If the plane leaves the search area horizontally, its vector will be determined using the equation:

<!-- b000295 | prose | pages [26] -->
(7)

<!-- b000296 | prose | pages [26] -->
If the plane leaves the search area vertically, its vector will be determined using the equation:

<!-- b000297 | prose | pages [26, 27] -->
(8) This redirection method is illustrated below:

<!-- b000298 | furniture | pages [27] -->
Team #38720

<!-- b000299 | furniture | pages [27] -->
Page 27 of 61

<!-- b000301 | prose | pages [27] -->
A sample simulation:

<!-- b000302 | caption | pages [27] -->
Figure 11 shows a typical solution as it moves according to the bounded random flight

<!-- b000303 | prose | pages [27] -->
path. Although the search plane does have some overlap in its path, this is a vast improvement from the random search method and we can accurately provide statistical data collected from our simulations.

<!-- b000304 | prose | pages [27] -->
Simulation Data:

<!-- b000305 | prose | pages [27] -->
This solution was able to complete 100 simulations; the data is listed below. These data describe the amount of time it took each of the simulated planes to find the crashed plane using this solution:

<!-- b000306 | prose | pages [27, 28] -->
Number of trials = 100 Median = 24.425 hours Mean = 42.7105 hours Standard deviation = 47.3783 hours Standard error = 4.73783 hours 95% Confidence interval about the mean: [33.2348,52.1862] hours

<!-- b000307 | furniture | pages [28] -->
Team #38720

<!-- b000308 | furniture | pages [28] -->
Page 28 of 61

<!-- b000310 | prose | pages [28] -->
The distribution within the sample is plotted in the following histogram:

<!-- b000311 | prose | pages [28] -->
Conclusion:

<!-- b000312 | prose | pages [28] -->
The most important of the data above is the 95% confidence interval, which says that the mean time required of a sample of 100 simulations has a 95% chance of falling between 33.2 and 52.2 hours. The difference between the mean (42.7 hours) and the median (24.4 hours) demonstrate the heavy skew within the sample distribution. This skew is visible in the histogram, where a few exceptionally long searches drag out the mean search time. The positive skew reflects well on the model, because most simulations require a low amount of time, with only some outliers that drag out the mean; however, it also has negative implications, because the solution is ineffective at locating some planes.

<!-- b000313 | prose | pages [28] -->
This solution is crucial, because it establishes a baseline with which to compare other solutions. Ideally, more sophisticated solutions should have a lower average time than this solution.

<!-- b000314 | furniture | pages [29] -->
Team #38720

<!-- b000315 | furniture | pages [29] -->
Page 29 of 61

<!-- b000316 | prose | pages [29] -->
Solution 5.1.3: Bounded Weighted Random Flight Path

<!-- b000317 | prose | pages [29] -->
A Brief Description:

<!-- b000318 | prose | pages [29] -->
Expanding on the bounded random solution, this solution slightly weights the plane’s flight toward the endpoints A and B.  By encouraging the search plane to fly nearer the downed plane’s flight path, we begin to focus our searches on the area with the highest probability of containment. The path will be mostly random and the plane will be kept inside the search area, as in the previous solution.

<!-- b000319 | prose | pages [29] -->
How It Works:

<!-- b000320 | prose | pages [29] -->
The plane will reevaluate its position every three minutes. Additionally, it measures its distance from points A and B and weights its random direction vector toward the more distant point.

<!-- b000321 | prose | pages [29] -->
If the distance from point A is larger than the distance from point B, the plane will move in a direction weighted 15 parts random for every 1 part toward A:

<!-- b000322 | prose | pages [29] -->
(9)

<!-- b000323 | prose | pages [29] -->
If the distance from point B is larger than the distance from point A, the plane will move in a direction weighted 15 parts random for every 1 part toward B:

<!-- b000324 | prose | pages [29] -->
(10)

<!-- b000325 | prose | pages [29] -->
This method is demonstrated in the diagram below:

<!-- b000326 | furniture | pages [30] -->
Team #38720

<!-- b000327 | furniture | pages [30] -->
Page 30 of 61

<!-- b000328 | prose | pages [30] -->
A sample simulation:

<!-- b000329 | prose | pages [30] -->
The path still has a high degree of randomness (15 parts random for every part nonrandom), meaning that the path still shows the chaotic nature evident in earlier solutions.

<!-- b000330 | prose | pages [30] -->
Simulation Data:

<!-- b000331 | prose | pages [30] -->
This solution was able to complete 100 simulations, with the important data listed below. These data describe the amount of time it took each of the simulated planes to find the crashed plane using this solution:

<!-- b000332 | prose | pages [30, 31] -->
Number of trials = 100 Median = 16.6 hours Mean = 37.5575 hours Standard deviation = 55.4901 hours Standard error = 5.54901 hours 95% Confidence interval about the mean: [26.4795,48.6755] hours The distribution within the sample is plotted in the following histogram:

<!-- b000333 | furniture | pages [31] -->
Team #38720

<!-- b000334 | furniture | pages [31] -->
Page 31 of 61

<!-- b000336 | heading | pages [31] -->
Conclusion:

<!-- b000337 | prose | pages [31] -->
The simulation data for the weighted, bounded random path show even more skew than was present in the bounded random path, seen in the difference between the mean (37.6 hours) and the median (16.6 hours.) The skew is also evident in the large right tail on the histogram, with some searches taking upwards of 200 hours. Both the mean and median are lower than the mean and median for the bounded random path, in which the mean is 42.7 hours and the median is 24.4 hours. ​ The confidence intervals for these two trials overlap, meaning that there is not a statistically significant difference between the two solutions.

<!-- b000338 | prose | pages [31] -->
The example simulation shows the main problem with this type of solution: the search plane’s path often overlaps with places it has searched in the path. A more advanced model should prevent this redundancy.

<!-- b000339 | furniture | pages [32] -->
Team #38720

<!-- b000340 | furniture | pages [32] -->
Page 32 of 61

<!-- b000341 | prose | pages [32] -->
Solution 5.1.4: Descending Striped Flight Path

<!-- b000342 | prose | pages [32] -->
A Brief Description:

<!-- b000343 | prose | pages [32] -->
This solution simulates a plane systematically eliminating stripes of the search area with straight paths. We can then compare straight path searches to random path searches and begin to draw conclusions on the most effective solution.

<!-- b000344 | prose | pages [32] -->
How It Works:

<!-- b000345 | prose | pages [32] -->
The plane begins in the top left corner of the search area and travels parallel to the x-axis until it reaches an edge. It then descends ​ 2d​ miles, the distance that eliminates any overlap of the flight path, before turning perpendicular to the y-axis, heading in the opposite direction of the previous strip. For this and the following two solutions, the plane reevaluates its position vector every 0.001 hours. Because the flight path of the search plane is predictable, we can afford more accuracy without needing significantly more computing time.

<!-- b000346 | prose | pages [32] -->
The flight path within the search area is determined by:

<!-- b000347 | prose | pages [32] -->
(11)

<!-- b000348 | prose | pages [32] -->
The variable ε describes the direction the plane flies parallel to the x-axis. If ε is equal to 1, the plane will fly in the positive direction. If ε is equal to -1, the plane will fly in the negative direction. Each time the plane reaches the edge of the search area, ε changes sign and we adjust the value of the y-position and the direction of the plane in order to initiate the next stripe.

<!-- b000349 | prose | pages [32, 33] -->
(12) The stripe technique is illustrated below:

<!-- b000350 | furniture | pages [33] -->
Team #38720

<!-- b000351 | furniture | pages [33] -->
Page 33 of 61

<!-- b000353 | prose | pages [33] -->
A sample simulation:

<!-- b000354 | prose | pages [33] -->
Simulation Data:

<!-- b000355 | prose | pages [33] -->
This solution was able to complete 100 simulations, with the important data listed below. These data describe the amount of time it took each of the simulated planes to find the crashed plane using this solution:

<!-- b000356 | prose | pages [33, 34] -->
Number of trials = 100 Median = 7.031 hours Mean = 7.10273 hours Standard deviation = 2.41002 hours Standard error = 0.241002 hours 95% Confidence interval about the mean: [6.62073,7.58473] hours The distribution within the sample is plotted in the following histogram:

<!-- b000357 | furniture | pages [34] -->
Team #38720

<!-- b000358 | furniture | pages [34] -->
Page 34 of 61

<!-- b000360 | prose | pages [34] -->
Conclusion:

<!-- b000361 | prose | pages [34] -->
This solution takes a nonrandom approach to the search, which drastically reduces the search time necessary. Unlike previous solutions, this sample simulation shows little to no skew, with the mean (7.1 hours) and the median (7.0 hours) being approximately equal. Based on the histogram, the distribution is approximately normal. This reflects the normal distribution of plane crashes, because the search plane starts at one tail of the normal distribution, moves toward the center, and then moves toward the other tail. The upside of the normal distribution is its consistency in locating planes; the downside is that few crashes are found in the first couple hours.

<!-- b000362 | prose | pages [34] -->
The 95% confidence interval about the mean ([6.6,7.6] hours) does not overlap with the confidence interval for the bounded random path ([33.2,52.2] hours.) ​ Therefore, the difference between the descending stripes solution and the bounded random solution is statistically significant, with the descending stripes solution producing smaller search times.

<!-- b000363 | prose | pages [34] -->
While this solution is significantly better than previous solutions, it hints that search times could be further reduced by considering the effect of the normal distribution.

<!-- b000364 | furniture | pages [35] -->
Team #38720

<!-- b000365 | furniture | pages [35] -->
Page 35 of 61

<!-- b000366 | prose | pages [35] -->
Solution 5.1.5: Spiral Striped Flight Path

<!-- b000367 | prose | pages [35] -->
A Brief Description:

<!-- b000368 | prose | pages [35] -->
This solution uses the same basic technique as the previous simulation. Based on the normal distribution of the lost planes, we determined that the most effective technique would start in the area with the highest probability of finding the plane and move outward to areas of gradually decreasing probability.

<!-- b000369 | prose | pages [35] -->
How It Works:

<!-- b000370 | prose | pages [35] -->
Similar to the previous solution, the search plane will fly horizontal stripes parallel to the x-axis while eliminating overlap of surveilled areas. The plane starts at Point A and flies along the x-axis—mimicking the flight path of the downed plane. It then travels to a position ​ C(u)​ miles along the y-axis before initiating another stripe. Continuing this, the plane forms a spiral pattern inside the search area.

<!-- b000371 | prose | pages [35] -->
The search plane’s vector is determined using the equation:

<!-- b000372 | prose | pages [35] -->
(13)

<!-- b000373 | prose | pages [35] -->
When the plane reaches the edge of the search area, the magnitude of the y-coordinate of its position vector is determined by:

<!-- b000374 | prose | pages [35] -->
(14)

<!-- b000375 | prose | pages [35] -->
The plane’s movement in the y-direction after reaching the edge of the search area is determined by incrementing the index  and changing direction by alternating the j sign of : ε

<!-- b000376 | prose | pages [35, 36] -->
(15) This method is demonstrated below:

<!-- b000377 | furniture | pages [36] -->
Team #38720

<!-- b000378 | furniture | pages [36] -->
Page 36 of 61

<!-- b000380 | prose | pages [36] -->
A sample simulation:

<!-- b000381 | prose | pages [36] -->
Simulation Data:

<!-- b000382 | prose | pages [36] -->
This solution was able to complete 100 simulations, with the important data listed below. These data describe the amount of time it took each of the simulated planes to find the crashed plane using this solution:

<!-- b000383 | prose | pages [36, 37] -->
Number of trials = 100 Median = 3.113 hours Mean = 3.62286 hours Standard deviation = 2.85127 hours Standard error = 0.285127 hours 95% Confidence interval about the mean: [3.05261,4.19311] hours The distribution within the sample is plotted in the following histogram:

<!-- b000384 | furniture | pages [37] -->
Team #38720

<!-- b000385 | furniture | pages [37] -->
Page 37 of 61

<!-- b000387 | heading | pages [37] -->
Conclusion:

<!-- b000388 | prose | pages [37] -->
This solution takes into account the normal distribution of plane crashes and prevents the overlap present in the random models. Unlike the descending stripes solution, it has significant positive skew and does not appear normally distributed. The discrepancy between the mean (3.6 hours) and the median (3.1 hours) is not as large as in the random models, indicating that the skew is not as pronounced.

<!-- b000389 | prose | pages [37] -->
The 95% confidence interval of [3.0,4.2] indicates that the​ ​ difference between the spiral stripes solution and all previous solution is statistically significant, with the spiral stripes solution producing smaller search times. ​ The differences are significant because the confidence intervals do not overlap.

<!-- b000390 | prose | pages [37] -->
Therefore, this solution is an effective way to reduce search times for this model.

<!-- b000391 | furniture | pages [38] -->
Team #38720

<!-- b000392 | furniture | pages [38] -->
Page 38 of 61

<!-- b000393 | prose | pages [38] -->
Solution 5.1.6: Sinusoidal Flight Path

<!-- b000394 | prose | pages [38] -->
A Brief Description:

<!-- b000395 | prose | pages [38] -->
The success of solution 5.1.5 warrants further investigation. Forming stripes starting at the area of highest probability is both a realistic and effective search method; however, we want to develop a similar solution that approaches the technique differently. Our sinusoidal solution fulfills this by forming wider stripes of surveilled areas in an attempt to maximize the effectiveness of every pass.

<!-- b000396 | prose | pages [38] -->
How It Works:

<!-- b000397 | prose | pages [38] -->
The search plane starts at Point A traveling in a positive direction along the x-axis in a path mirroring a sine curve. This forms a wider stripe than a straight path, reducing the amount of times ​ C(u) ​ is incremented and the distance the search plane must travel along the edge of the search area. Just as in the previous model, as soon as the plane reaches the edge of the search area, its position along the y-axis is reevaluated before starting a new stripe.

<!-- b000398 | prose | pages [38] -->
Setting the amplitude to the the sight range and wavelength to twice the sight range ensures that there are no areas left unsurveyed in between passes. The path of the plane inside the search area is determined by:

<!-- b000399 | prose | pages [38] -->
(16)

<!-- b000400 | prose | pages [38] -->
When the plane reaches the edge of the search area, the magnitude of the y-coordinate of its position vector is determined by:

<!-- b000401 | prose | pages [38] -->
(17)

<!-- b000402 | prose | pages [38] -->
The plane’s movement in the y-direction after exiting the search area is determined by incrementing the index  and changing direction by alternating : ε j

<!-- b000403 | prose | pages [38, 39] -->
(18) The sinusoidal method is illustrated below:

<!-- b000404 | furniture | pages [39] -->
Team #38720

<!-- b000405 | furniture | pages [39] -->
Page 39 of 61

<!-- b000407 | prose | pages [39] -->
A sample simulation:

<!-- b000408 | prose | pages [39] -->
Simulation Data:

<!-- b000409 | prose | pages [39] -->
This solution was able to complete 100 simulations, with the important data listed below. These data describe the amount of time it took each of the simulated planes to find the crashed plane using this solution:

<!-- b000410 | prose | pages [39, 40] -->
Number of trials = 100 Median = 4.489 hours Mean = 6.44989 hours Standard deviation = 6.08373 hours Standard error = 0.608373 hours 95% Confidence interval about the mean: [5.23314, 7.66664] hours The distribution within the sample is plotted in the following histogram:

<!-- b000411 | furniture | pages [40] -->
Team #38720

<!-- b000412 | furniture | pages [40] -->
Page 40 of 61

<!-- b000414 | heading | pages [40] -->
Conclusion:

<!-- b000415 | prose | pages [40] -->
Like the spiral striped solution, this solution shows significant positive skew, which is visible on the histogram.  The mean (6.4 hours) is greater than the median (4.5 hours), indicative of the skew. This solution is much more vulnerable to extreme values that pull the mean higher than the median.

<!-- b000416 | prose | pages [40] -->
The 95% CI of [5.2,7.7] hours does not overlap with that of the spiral striped solution, indicating that the difference between the sinusoidal model and spiral striped solution is statistically significant, with the spiral stripes solution producing smaller search times. The CI overlaps with that of the descending striped solution, meaning that there is no significant difference between the two.

<!-- b000417 | heading | pages [40] -->
Normal Distribution Overall Conclusion

<!-- b000418 | prose | pages [40] -->
Based on the results from this and the previous 5 solutions, we can conclude that the spiral striped solution offers the lowest search times of those tested.

<!-- b000419 | furniture | pages [41] -->
Team #38720

<!-- b000420 | furniture | pages [41] -->
Page 41 of 61

<!-- b000421 | heading | pages [41] -->
5.2 Normal Distribution with Discovery Uncertainty

<!-- b000422 | prose | pages [41] -->
Up until this point we have assumed that the probability of detection is 100% for the radar sensor and the operator aboard the P-8 search plane. How would our model change if we altered that assumption? ​ Each pass along the search route will no longer eliminate the surveilled area from the possible locations of the lost plane.

<!-- b000423 | heading | pages [41] -->
Discovery Uncertainty Model-Specific Variables and Assumptions:

<!-- b000424 | prose | pages [41] -->
Variables:

<!-- b000425 | prose | pages [41] -->
Name of Variable (Symbol) Definition (Units)

<!-- b000426 | prose | pages [41] -->
Total Probability of The probability that the debris will be spotted and the plane we be found, if it is within the radius of Detection ( ) P(D  ) u the radar (%)

<!-- b000427 | prose | pages [41] -->
Probability of Radar The probability that the radar will detect the debris as it flies by (%) Detection ( ) P(R )

<!-- b000428 | prose | pages [41] -->
Probability of Operator The probability that the operator will identify the debris (%) Identification ( ) P(O)

<!-- b000429 | prose | pages [41] -->
The probability that the operator will identify the Probability of given P (O) debris given the radar has successfully detected the Radar Detection P (R) debris (%) ( ) P (O|R)

<!-- b000430 | prose | pages [41] -->
Probability of Containment The probability that any given area, , contains the C ( ) P (C) missing plane, originally determined by a normal distribution (%)

<!-- b000431 | prose | pages [41, 42] -->
Probability of Containment The probability that any single area other than , C in ( ) C i P (C ) the current area being searched, contains the lost i plane (%) A Brief Explanation of Bayesian Search Theory

<!-- b000432 | furniture | pages [42] -->
Team #38720

<!-- b000433 | furniture | pages [42] -->
Page 42 of 61

<!-- b000435 | prose | pages [42] -->
We are no longer going to assume that radars and operators will identify objects in [19]​, we can adjust ​ the ocean 100% of the time. Using Bayesian Search Theory​ P(C) ​ after each pass if we don’t find the debris in a searched area. Failing to find the debris in one area would make the probability that the debris is contained in any other location [19]​. higher​

<!-- b000436 | prose | pages [42] -->
The probability of the plane being in the search area directly after being searched is ’​(C)​ denoted by ​ P​ , where:

<!-- b000437 | prose | pages [42] -->
(19)

<!-- b000438 | prose | pages [42] -->
The probability of the plane being in any other ​ specific ​ area ​ C​ i​ just after ​ P(C)​ has been searched is calculated using:

<!-- b000439 | prose | pages [42] -->
(20)

<!-- b000440 | prose | pages [42] -->
Determining Realistic Uncertainty:

<!-- b000441 | prose | pages [42] -->
The increased complexity of Model 5.2 stems from the inconsistency of the radar’s ability to detect debris and the radar operator’s ability to effectively scan the radar [14]​. screen—and distinguish debris from radar noise and sea clutter​

<!-- b000442 | prose | pages [42] -->
[20]​ and assuming our only Using the Multiplication Rule for Conditional Probability​ uncertainties are the abilities of the radar and the operator, we can conclude the total probability of spotting the debris in any pass is:

<!-- b000443 | prose | pages [42] -->
(21)

<!-- b000444 | prose | pages [42, 43] -->
According to test data performed with the AN/APS-119 radar, we can accurately estimate P(R) to be 80% for a search plane flying at 1000 ft altitude over calm [14]​. seas with a 10 mile sight​ Because the plane travels at a constant speed of 400 mph, it would cross the sight range—the radius of the radar sweep—in 1.5 minutes, so we can safely assume that the radar operator would have at least 90 seconds to identify pieces of the lost plane.

<!-- b000445 | furniture | pages [43] -->
Team #38720

<!-- b000446 | furniture | pages [43] -->
Page 43 of 61

<!-- b000448 | prose | pages [43] -->
Studies simulating the ability of an operator observing a screen similar to the [14] ​conclude a 97% probability of all objects display of the AN/APS-119 radar ​ [21]​. Because the operator will have a minimum of being spotted within 90 seconds​ 90 seconds to observe each object during a single pass we can approximate ​ P(O)​ so that:

<!-- b000449 | prose | pages [43] -->
(22)

<!-- b000450 | prose | pages [43] -->
Given the inputs, we can determine:

<!-- b000451 | prose | pages [43] -->
(23)

<!-- b000452 | prose | pages [43] -->
Assumptions:

<!-- b000453 | prose | pages [43] -->
● False targets in the form of sea clutter and radar noise diminish the detection accuracy of the radar.

<!-- b000454 | prose | pages [43] -->
● The radar operator will have ample time, at least 90 seconds, to identify debris that the radar sees.

<!-- b000455 | prose | pages [43] -->
● The probability of detection for the uncertain discovery model is about 80% according to the capabilities of radar and operator.

<!-- b000456 | prose | pages [43] -->
We assume that this 80% accuracy is still uniform within the 10 ○ mile radius of radar sight range.

<!-- b000457 | prose | pages [43] -->
A Limiting Factor:

<!-- b000458 | prose | pages [43] -->
For simplicity’s sake, the search time was capped at 24 hours. The Bayesian solution becomes exponentially harder to simulate with each pass, so it requires a significant amount of computing time to recommend a course of action after about 24 hours of searching. If the crashed plane is not found within this time, this is recorded and the sample size used in calculations is reduced. Because the capped time caused a reduction in computing time, we increased the sample size to 500 to increase precision.

<!-- b000459 | furniture | pages [44] -->
Team #38720

<!-- b000460 | furniture | pages [44] -->
Page 44 of 61

<!-- b000461 | prose | pages [44] -->
Solution 5.2.1: Bayesian Adjusted Flight Paths

<!-- b000462 | prose | pages [44] -->
A Brief Description:

<!-- b000463 | prose | pages [44] -->
This solution uses Bayesian Search Theory to predict the optimal flight path. The solution is quite like the spiral striped model used for the purely normal model, but with different locations for each pass depending on where the new peak of the probability distribution lies.

<!-- b000464 | prose | pages [44] -->
How it Works:

<!-- b000465 | prose | pages [44] -->
Before the plane makes any passes, the probability distribution looks identical to the normal distribution we used for our simpler model. A three-dimensional (Figure 25) and two-dimensional graph (Figure 26) of the initial distribution are displayed below:

<!-- b000466 | prose | pages [44] -->
Once the plane makes its initial pass of width ​ 2d​ through the area of highest probability—the center of the graph—the probability is not completely reduced to zero because ​ P(D​ u​) ​ is not 100% and the lost plane could be missed. Instead, ​ P(C)​ of the center is lowered and the probabilities for the rest of the unsearched area are adjusted upward using Bayes’s Theorem. The next pass the plane makes will be through the new area of highest probability, which in this case can be either the strip centered at y=20 mi or the strip centered at y=-20 mi, because they are equivalent (Figure 27).

<!-- b000467 | furniture | pages [45] -->
Team #38720

<!-- b000468 | furniture | pages [45] -->
Page 45 of 61

<!-- b000469 | prose | pages [45] -->
After the second pass, the areas not covered by the second strip are adjusted up. Now, the location of the third pass can be determined by finding the highest remaining probability distribution, here centered around y=-20 miles (Figure 28).

<!-- b000470 | prose | pages [45] -->
The search plane continues to choose the area of highest ​ P(C) ​ determined by Bayes’s Theorem for the next part of its flight. We will not illustrate the further repeated steps of this solution. According to our simulation, they will follow the sequence y= 0, 20, -20, 40, -40, 60, -60, 0, 20, -20, 40, -40, 80, -80, 60, -60, 0, 20, -20,...

<!-- b000471 | prose | pages [45] -->
Simulation Data:

<!-- b000472 | prose | pages [45] -->
The following data describe the amount of time it took each of the simulated planes to find the crashed plane using this solution:

<!-- b000473 | prose | pages [45, 46] -->
Number of planes not found: 25 Number of planes found: 475 Median: 4.05 hours Mean: 6.21463 hours Standard deviation: 5.37383 hours Standard error of the mean: 0.246568 hours 95% Confidence interval: [5.57215, 6.70777] hours The distribution within the sample is plotted in the following histogram:

<!-- b000474 | furniture | pages [46] -->
Team #38720

<!-- b000475 | furniture | pages [46] -->
Page 46 of 61

<!-- b000477 | prose | pages [46] -->
Conclusion:

<!-- b000478 | prose | pages [46] -->
The samples for this solution show a high degree of skew, visible in the histogram. The mean (6.2 hours) is greater than the median (4.1 hours), supporting the visual trend in skew.

<!-- b000479 | prose | pages [46] -->
Of the 500 planes simulated, 475 were found within 24 hours.​ The proportion of planes found by the bayesian method is 95%. This proportion seems reasonable, but must be compared to other possible solutions.

<!-- b000480 | prose | pages [46] -->
The confidence interval for this solution is [5.6,6.7] hours, meaning that a 95% of samples of size 100 will have a mean between 5.6 and 6.7 hours. This range is still quite small, considering that the probability of finding the crash given that it’s in range is less than 1. To get a good idea of the effectiveness of the Bayesian method, we can compare it to the Spiral Stripes approach, our previous model’s most successful solution.

<!-- b000481 | furniture | pages [47] -->
Team #38720

<!-- b000482 | furniture | pages [47] -->
Page 47 of 61

<!-- b000483 | prose | pages [47] -->
Solution 5.2.2: Spiral Striped Flight Path

<!-- b000484 | prose | pages [47] -->
A Brief Description:

<!-- b000485 | prose | pages [47] -->
This solution is essentially identical to the spiral striped solution in 5.1.5. We decided to try it here for comparison’s sake because it was the most successful model for the normal distribution. The only difference is that it will not necessarily find the debris, even if it is within range of the search plane.

<!-- b000486 | prose | pages [47] -->
How it Works:

<!-- b000487 | prose | pages [47] -->
Refer to “How it Works” in 5.1.5.

<!-- b000488 | prose | pages [47] -->
Simulation Data:

<!-- b000489 | prose | pages [47] -->
Number of planes not found: 101 Number of planes found: 399 Median: 4.05 hours Mean: 4.76078 hours Standard deviation: 3.24672 hours Standard error of the mean: 0.162539 hours 95% Confidence interval: [4.4357,5.08586] hours

<!-- b000490 | prose | pages [47] -->
The distribution within the sample is plotted in the following histogram:

<!-- b000491 | furniture | pages [48] -->
Team #38720

<!-- b000492 | furniture | pages [48] -->
Page 48 of 61

<!-- b000493 | prose | pages [48] -->
Conclusion:

<!-- b000494 | prose | pages [48] -->
This solution shows minor positive skew, with the median (4.1 hours) being slightly less than the mean (4.8 hours).

<!-- b000495 | prose | pages [48] -->
Of the 500 planes simulated, only 399 were found within 24 hours. This proportion is 80%, as opposed to the 95% proportion found in the Bayesian solution.

<!-- b000496 | prose | pages [48] -->
The confidence interval for this solution is [4.4, 5.1] hours does not overlap with the confidence interval of the Bayesian solution,​ ​ indicating that the difference between the spiral striped solution and spiral Bayesian solution is statistically significant, with the Bayesian solution yielding greater search times. However, the proportion of planes found is greater with the Bayesian solution, making Bayesian the preferable solution if chance of rescue is our priority.

<!-- b000497 | furniture | pages [49] -->
Team #38720

<!-- b000498 | furniture | pages [49] -->
Page 49 of 61

<!-- b000499 | heading | pages [49] -->
6 Solution Stability

<!-- b000500 | prose | pages [49] -->
To further test the flexibility of our models and best solutions, we decide to try two new scenarios.

<!-- b000501 | heading | pages [49] -->
6.1 Bayesian Adjusted Flight Path with a lost Cessna 172

<!-- b000502 | prose | pages [49] -->
A Brief Description:

<!-- b000503 | prose | pages [49] -->
On the opposite end of the spectrum from the Boeing 777, this miniscule craft has a search area of only 29 by 99 miles and is about 42 times smaller in size, according to our chart in Section 3.2. In our model, we will adjust the search area to match the Cessna’s and the probability of detection to one fortieth the 777’s, which gives us P(D) = 2%​ . We will keep the search plane, sensor, and everything else the same, searching for 24 hours.

<!-- b000504 | prose | pages [49] -->
How it works:

<!-- b000505 | prose | pages [49] -->
Refer to “How it Works” in 5.2.1.

<!-- b000506 | prose | pages [49] -->
Simulation Data:

<!-- b000507 | prose | pages [49] -->
Number of planes not found: 89 Number of planes found: 411 Median: 6.435 hours Mean: 8.38549 hours Standard deviation: 6.55782 hours Standard error of the mean: 0.322474 hours 95% Confidence interval: [7.73855,9.03244] hours

<!-- b000508 | prose | pages [49] -->
The distribution within the sample is plotted in the histogram:

<!-- b000509 | furniture | pages [50] -->
Team #38720

<!-- b000510 | furniture | pages [50] -->
Page 50 of 61

<!-- b000511 | prose | pages [50] -->
Conclusion:

<!-- b000512 | prose | pages [50] -->
Like its counterpart in 5.2.1, this solution shows slight rightward skew, with the median (6.4 hours) being slightly below the mean (8.4 hours).

<!-- b000513 | prose | pages [50] -->
Of the 500 Cessnas lost, 82% of them were found within 24 hours, which is lower, but comparable to, the 95% of Boeing 777s found within 24 hours.

<!-- b000514 | prose | pages [50] -->
The 95% confidence interval for this solution is [7.7,9.0] hours, which does not overlap with the confidence interval for the Boeing 777 with the Bayesian path. Therefore, the difference between finding the Cessna 172 and Boeing 777 is statistically significant. This conclusion makes sense, because the probability of finding the Cessna on a single flight is quite small (2%.)​ Despite this low probability, the Bayesian solution does a surprisingly good job finding Cessnas.

<!-- b000515 | furniture | pages [51] -->
Team #38720

<!-- b000516 | furniture | pages [51] -->
Page 51 of 61

<!-- b000517 | heading | pages [51] -->
6.2 Two Planes Flying Striped Patterns

<!-- b000518 | prose | pages [51] -->
A Brief Description:

<!-- b000519 | prose | pages [51] -->
Now we wish to examine what will happen if we add a second search plane identical to the first to our effort to find a Boeing 777. Common sense dictates that the time will be shorter with twice the search effort, but by how much? We will use the successful stripe method, but start both planes in the center flying opposite directions, completely removing any overlap.

<!-- b000520 | prose | pages [51] -->
A sample simulation is shown below:

<!-- b000521 | prose | pages [51] -->
How it Works:

<!-- b000522 | prose | pages [51] -->
Refer to “How it Works” in 5.1.4

<!-- b000523 | prose | pages [51] -->
Simulation Data:

<!-- b000524 | prose | pages [51, 52] -->
Number of trials: 100 Median: 2.1435 hours Mean: 2.39551 hours Standard deviation: 1.39534 hours Standard error of the mean: 0.139534 hours 95% Confidence interval: [2.11644, 2.67458] hours The distribution within the sample is plotted in the following histogram:

<!-- b000525 | furniture | pages [52] -->
Team #38720

<!-- b000526 | furniture | pages [52] -->
Page 52 of 61

<!-- b000528 | prose | pages [52] -->
Conclusion:

<!-- b000529 | prose | pages [52] -->
The skew for this distribution is visible in the histogram, but is less pronounced in the difference between the mean (2.4 hours) and the median (2.1 hours.)

<!-- b000530 | prose | pages [52] -->
Unsurprisingly, this solution performed better than any others. Not only did it include an extra search plane to double the effort, it started on the area of highest probability distribution ​ and ​ excluded any overlap.

<!-- b000531 | prose | pages [52] -->
Without discovery uncertainty, this model lacks the realism of others, but it remains an ideal solution for 100% effective radar. Logically, the more search planes added, the more the time will decrease.

<!-- b000532 | furniture | pages [53] -->
Team #38720

<!-- b000533 | furniture | pages [53] -->
Page 53 of 61

<!-- b000534 | heading | pages [53] -->
7 Results

<!-- b000535 | heading | pages [53] -->
7.1 The Normal Distribution Model

<!-- b000536 | prose | pages [53] -->
For the Normally Distributed Model (described in 5.1), a total of 7 solutions are tested, including the Two Plane Solution in 6.2. The completely random solution (5.1.1) is not a viable option because most simulations did not ultimately find the plane. Of the remaining 6 solutions, 2 are random and 4 are nonrandom. Large sample size simulations run for these models provide 95% confidence intervals (CI) for each of these solutions. Because of the large difference between the CIs for the random and nonrandom solutions, these are displayed on separate graphs, shown below:

<!-- b000537 | furniture | pages [54] -->
Team #38720

<!-- b000538 | furniture | pages [54] -->
Page 54 of 61

<!-- b000539 | prose | pages [54] -->
The overlap between the random solution CIs indicates that it cannot be proven whether the two solutions differ in search time. However, none of the CIs for the nonrandom solutions overlap with either of the random solution CIs, meaning that each of the nonrandom solutions produce lower search times than the random solutions.

<!-- b000540 | prose | pages [54] -->
Comparing the CIs for the nonrandom solutions allows for several interesting conclusions. Predictably, the two plane striped solution, with a mean of 2.4 hours, performs better than any other solution. If only one search plane operates, spiral striped is clearly the best solution, with a mean of 3.6 hours and a standard deviation of 2.9 hours.

<!-- b000541 | prose | pages [54] -->
Between the sinusoidal and descending stripes solutions, no statistically significant difference exists. While the sinusoidal model has a lower mean than the descending striped solution (6.4 hours vs 7.1 hours), it has a large standard deviation (6.1 hours.) This means that the the sinusoidal solution has a very high variability. If the plane crash is close to the center of the search area, it will be found quickly; if the crash is toward the edges, it will take a significant amount of time. These large trials account for the significant skew.

<!-- b000542 | heading | pages [54] -->
7.2 Discovery Uncertainty Model

<!-- b000543 | prose | pages [54] -->
For the discovery uncertain model discussed in 5.2, 3 simulations were run. Every simulation completed a large number of trials with relatively slim 95% confidence intervals. For simplicity, the search time was capped at 24 hours with the number unsuccessful trials recorded. The CIs for these simulations are displayed below:

<!-- b000544 | furniture | pages [55] -->
Team #38720

<!-- b000545 | furniture | pages [55] -->
Page 55 of 61

<!-- b000546 | prose | pages [55] -->
The most useful comparisons can be made between the two Boeing 777 simulations (5.2.1 and 5.2.2) and between the two Bayesian simulations (5.2.1 and 6.1.) For a lost Boeing 777, the CI for the spiral solution does not overlap with the CI of the Bayesian solution, meaning that the spiral solution generally produces lower search times. A possible reason for this difference is that the striped spiral solution only find 80% of crashed planes within 24 hours, while the Bayesian solution finds 95%. The large search times for unsuccessful attempts are not factored into the mean, which shifts the mean leftward for the striped spiral solution. A more useful comparison can be found from comparing the medians, which are equal for both cases (4.05 hours). For cases with high skew, the median is a useful indicator of the center of a distribution. Therefore, given that the medians are equal, the Bayesian solution, which finds 95% of crashed planes within 24 hours, is preferable to the striped spiral solution, which only finds 80%.

<!-- b000547 | prose | pages [55] -->
Understandably, the difference in CIs between the Bayesian solutions for the Boeing-777 and for the Cessna-172 indicates that the Boeing-777 has a lower mean search time. This difference is confirmed by comparing the medians (4.05 hours for the Boeing-777, and 6.44 for the Cessna-172.) Additionally, the percentage of planes found within the time limit of 24 hours differs significantly, with 95% of Boeing-777s being found and 82% of Cessna-172s. ​ Therefore, it can be concluded that it is easier and faster to locate a Boeing-777 than a Cessna-172, even though the search area for a Cessna is much smaller.

<!-- b000548 | furniture | pages [56] -->
Team #38720

<!-- b000549 | furniture | pages [56] -->
Page 56 of 61

<!-- b000550 | heading | pages [56] -->
8 Conclusion

<!-- b000551 | heading | pages [56] -->
8.1 Recommendation

<!-- b000552 | prose | pages [56] -->
As we established in the Introduction, the measure of success for our solutions is first, whether they find the lost plane, and second, if they can reasonably expect to rescue plane crash survivors before they die of exposure. In a scenario where passengers are adrift without rafts in normal clothes (low insulation) and life vests in the ~20℃ Atlantic Ocean, they will have about 18 hours before hypothermia begins to kill [22]​. them​

<!-- b000553 | prose | pages [56] -->
Although all the Striped and Sinusoidal Normal Distribution Solutions’ means are very likely to be below 8 hours, easily fast enough to save the passengers, we do not believe they are realistic enough to recommend.

<!-- b000554 | prose | pages [56] -->
For the more realistic, complex Discovery Uncertainty Model, both the Bayesian and Spiral Striped Solutions have high skew so we compare them by their medians, which are equal at 4.05 hours each, plenty of time for rescue. To arrive at our final recommendation, we examine the percentage of planes found for these solutions—a critically important factor considering that the search is all in vain if the plane remains lost. The Bayesian Solution finds 95% of Boeing 777s within 24 hours, while the Spiral Striped Solution finds only 80%. Furthermore, the Bayesian Solution

<!-- b000555 | prose | pages [56] -->
We recommend the most accurate model and its most successful solution: the Normal Distribution with Discovery Uncertainty (Section 5.2) paired with the Bayesian Search flight path (5.2.1).

<!-- b000556 | furniture | pages [57] -->
Team #38720

<!-- b000557 | furniture | pages [57] -->
Page 57 of 61

<!-- b000558 | heading | pages [57] -->
8.2 Strengths and Weaknesses of Recommendation

<!-- b000559 | prose | pages [57] -->
Strengths:

<!-- b000560 | prose | pages [57] -->
● Our model takes into account, and can be adjusted for, many different probabilities of detection, search areas, and sight ranges.

<!-- b000561 | prose | pages [57] -->
● The solution locates a high proportion of plane crashes (95% of Boeing-777s and 82% of Cessna-172s) within 24 hours.

<!-- b000562 | prose | pages [57] -->
● The 95% CI around the mean for Boeing-777s is [5.6,6.7] hours, far below the lower bound of the death window (18 hour). Therefore, it is likely that most planes will be located before it is too late for any passengers who survived the crash.

<!-- b000563 | prose | pages [57] -->
Weaknesses:

<!-- b000564 | prose | pages [57] -->
● The search time is capped at 24 hours due to limitations in computing power because it becomes exponentially harder to use the Bayesian Solution to estimate the best flight path for the next flight.

<!-- b000565 | prose | pages [57] -->
● Although it focuses on areas of high probability, our solution does not entirely eliminate unnecessary overlap especially when transitioning between passes.

<!-- b000566 | prose | pages [57] -->
Limiting Assumptions

<!-- b000567 | prose | pages [57] -->
● Our normal distribution of planes is simplified from the search area design and the standard deviation we estimated has a high degree of uncertainty.

<!-- b000568 | prose | pages [57] -->
● Our model assumes that the plane did not deviate from its flight path before it began to crash.

<!-- b000569 | prose | pages [57] -->
● Factors we ignored, such as curvature of flight paths, ocean currents, questionable existence of debris, weather, and sea conditions while searching could have a significant effect on the difficulty of finding the lost plane.

<!-- b000570 | prose | pages [57] -->
● We assume that the search is a one-step process and finding debris means finding the plane, when in reality this could require additional searching.

<!-- b000571 | prose | pages [57] -->
● We discount the time it takes for the search effort to mobilize and for the search plane to arrive at the search area.

<!-- b000572 | prose | pages [57] -->
● We do not take into account fuel and cost as limiting factors.

<!-- b000573 | furniture | pages [58] -->
Team #38720

<!-- b000574 | furniture | pages [58] -->
Page 58 of 61

<!-- b000575 | heading | pages [58] -->
9 Press Conference Document

<!-- b000576 | prose | pages [58] -->
We, the airlines, would like to take this opportunity to offer our deepest and most sincere apologies for the tragic events that took place concerning Malaysia Flight MH370. We know that you, our patrons and customers, place your trust in us when you book a flight on one of our aircraft. Violation of this trust is unacceptable to us so we will take every possible measure to mitigate future disasters. In light of the ineffective search that failed to recover Flight MH370, we have put significant effort into revising and updating our emergency search procedures for immediate application.

<!-- b000577 | prose | pages [58] -->
We acknowledge that some factors in the response process are out of our control, but we will strive to adjust our methods for maximum effectiveness. Ocean currents, weather, sea clutter, and roughness all have the potential to detract from our operations but we remain confident that our new procedure will still outperform others under these conditions.

<!-- b000578 | prose | pages [58] -->
The outline of our plan is as follows: as soon as a plane fails to check in on time, we will predict its location based on its last transmitted signal and flight path. Our mathematicians will develop a rectangular boundary for the ideal search area so we can immediately deploy search and rescue planes to the area where the lost plane is most likely to be.

<!-- b000579 | prose | pages [58] -->
Our search planes will fly across the search area in parallel paths that entirely cover the region. We will decide on these paths based on where we predict the plane probably is. We can use data we collect during our search to update our prediction of the plane’s location, and adjust our plan accordingly. Our response plan can and will be rapidly adjusted for different factors to meet the situation’s needs. During the course of the search, we must be sure to consider imperfections in our equipment, such as our radar, and ensure that we do not miss the plane. We will look quickly, look thoroughly, and continue to look until the plane is found.

<!-- b000580 | prose | pages [58] -->
In the future, we believe we can refine our procedure even further by extending our abilities to better account for environmental challenges and equipment imperfections. Through detailed and extensive study, our model can always improve. We owe nothing less to the families and friends of those lost on MH370.

<!-- b000581 | prose | pages [58] -->
To those out there who now question the wisdom of travelling by air—we promise that there is no need to worry for the safety of yourself and your loved ones.

<!-- b000582 | furniture | pages [59] -->
Team #38720

<!-- b000583 | furniture | pages [59] -->
Page 59 of 61

<!-- b000584 | heading | pages [59] -->
10 References

<!-- b000585 | references | pages [59] -->
[1] "The Wright Brothers - First Flight, 1903", EyeWitness to History,

<!-- b000586 | references | pages [59] -->
www.eyewitnesstohistory.com (2003).

<!-- b000587 | references | pages [59] -->
[2] Adler, Jerry. "Will the Search for Amelia Earhart Ever End?" ​

<!-- b000588 | references | pages [59] -->
Smithsonian​

<!-- b000589 | references | pages [59] -->
.

<!-- b000590 | references | pages [59] -->
Smithsonian Magazine, Jan. 2015. Web. 06 Feb. 2015.

<!-- b000591 | references | pages [59] -->
[3]"ASN Records over 80 Aircraft Missing since 1948." ASN News. N.p., 18 Mar. 2014.

<!-- b000592 | references | pages [59] -->
Web. 06 Feb. 2015.

<!-- b000593 | references | pages [59] -->
<​

<!-- b000594 | references | pages [59] -->
http://news.aviation-safety.net/2014/03/18/asn-records-over-80-aircraft-missing-si

<!-- b000595 | references | pages [59] -->
nce-1948/​

<!-- b000596 | references | pages [59] -->
>.

<!-- b000597 | references | pages [59] -->
[4] "Missing Malaysia Plane: What We Know." ​

<!-- b000598 | references | pages [59] -->
BBC News​

<!-- b000599 | references | pages [59] -->
. N.p., 30 Jan. 2015. Web. 02

<!-- b000600 | references | pages [59] -->
Feb. 2015.

<!-- b000601 | references | pages [59] -->
[5]"777 Family." Boeing: 777-200/-200ER Technical Characteristics. The Boeing

<!-- b000602 | references | pages [59] -->
Company, n.d. Web. 06 Feb. 2015.

<!-- b000603 | references | pages [59] -->
<​

<!-- b000604 | references | pages [59] -->
http://www.boeing.com/boeing/commercial/777family/pf/pf_200product.page​

<!-- b000605 | references | pages [59] -->
>.

<!-- b000606 | references | pages [59] -->
[6]"Aircraft - G450." Gulfstream Aerospace, n.d. Web. 06 Feb. 2015.

<!-- b000607 | references | pages [59] -->
<​

<!-- b000608 | references | pages [59] -->
http://www.gulfstream.com/aircraft/gulfstream-g450​

<!-- b000609 | references | pages [59] -->
>.

<!-- b000610 | references | pages [59] -->
[7]"Skyhawk Model 172S Specification & Description." Cessna Aircraft Company, Dec.

<!-- b000611 | references | pages [59] -->
2012. Web. 6 Feb. 2015.

<!-- b000612 | references | pages [59] -->
<​

<!-- b000613 | references | pages [59] -->
http://cessna.txtav.com/~/media/Files/Single%20Engine/skyhawk/Skyhawk%202013

<!-- b000614 | references | pages [59] -->
%20172S%20SD.ashx​

<!-- b000615 | references | pages [59] -->
>.

<!-- b000616 | references | pages [59] -->
[8] Kebabjian, Richard. "STATISTICS." ​

<!-- b000617 | references | pages [59] -->
Accident Statistics​

<!-- b000618 | references | pages [59] -->
. N.p., n.d. Web. 06 Feb.

<!-- b000619 | references | pages [59] -->
2015. <​

<!-- b000620 | references | pages [59] -->
http://www.planecrashinfo.com/cause.htm​

<!-- b000621 | references | pages [59] -->
>.

<!-- b000622 | references | pages [59] -->
[9]Cox, John. "Ask the Captain: How Do Planes Communicate over Ocean?"USA Today.

<!-- b000623 | references | pages [59] -->
Gannett, 06 Oct. 2014. Web. 06 Feb. 2015.

<!-- b000624 | references | pages [59] -->
<​

<!-- b000625 | references | pages [59] -->
http://www.usatoday.com/story/travel/columnist/cox/2014/10/06/air-traffic-contr

<!-- b000626 | references | pages [59] -->
ol-satellite-radar/16645853/​

<!-- b000627 | references | pages [59] -->
>.

<!-- b000628 | references | pages [59] -->
[10]McCartney, Scott. "Building a Better Air-Traffic-Control System." ​

<!-- b000629 | references | pages [59] -->
The Wall Street

<!-- b000630 | references | pages [59] -->
Journal​

<!-- b000631 | references | pages [59] -->
. The Wall Street Journal, 22 Oct. 2009. Web. 06 Feb. 2015.

<!-- b000632 | references | pages [59] -->
<​

<!-- b000633 | references | pages [59] -->
http://www.wsj.com/articles/SB10001424052748703816204574487173981612780​

<!-- b000634 | references | pages [59] -->
>.

<!-- b000635 | furniture | pages [60] -->
Team #38720

<!-- b000636 | furniture | pages [60] -->
Page 60 of 61

<!-- b000637 | references | pages [60] -->
[11]United States. U.S. DEPARTMENT OF TRANSPORTATION. FEDERAL AVIATION

<!-- b000638 | references | pages [60] -->
ADMINISTRATION. Air Traffic Organization Policy. N.p., 03 Apr. 2014. Web. 06 Feb.

<!-- b000639 | references | pages [60] -->
2015. <​

<!-- b000640 | references | pages [60] -->
https://www.faa.gov/air_traffic/publications/ATpubs/ATC/atc1006.html​

<!-- b000641 | references | pages [60] -->
>.

<!-- b000642 | references | pages [60] -->
[12]United States. US Coast Guard. Office of Search and Rescue. The Theory of

<!-- b000643 | references | pages [60] -->
Search: A Simplified Explanation. N.p.: n.p., n.d. Print.

<!-- b000644 | references | pages [60] -->
[13]Davies, Anne. "Marshalling Forces in the Search for MH370." Sydney Morning

<!-- b000645 | references | pages [60] -->
Herald, 22 Mar. 2014. Web. 7 Feb. 2015.

<!-- b000646 | references | pages [60] -->
<http%3A%2F%2F​

<!-- b000647 | references | pages [60] -->
www.smh.com.au%2Fworld%2Fmarshalling-forces-in-the-search-for-m

<!-- b000648 | references | pages [60] -->
h370-20140322-hvll6.html​

<!-- b000649 | references | pages [60] -->
>.

<!-- b000650 | references | pages [60] -->
[14]Currie, N. C. ​

<!-- b000651 | references | pages [60] -->
Performance Tests on the AN/APS-119 Radar System​

<!-- b000652 | references | pages [60] -->
. Tech. no.

<!-- b000653 | references | pages [60] -->
AD-787 182. N.p.: Georgia Institute of Technology, 1979. Defense Technical

<!-- b000654 | references | pages [60] -->
Information Center. Web. 8 Feb. 2015.

<!-- b000655 | references | pages [60] -->
<​

<!-- b000656 | references | pages [60] -->
http://www.dtic.mil/get-tr-doc/pdf?AD=AD0787182​

<!-- b000657 | references | pages [60] -->
>.

<!-- b000658 | references | pages [60] -->
[15] Neuman, Scott. "Sub-Hunting Planes Use High-Tech Gear To Search For Flight

<!-- b000659 | references | pages [60] -->
370." ​

<!-- b000660 | references | pages [60] -->
NPR​

<!-- b000661 | references | pages [60] -->
. NPR, 20 Mar. 2014. Web. 07 Feb. 2015.

<!-- b000662 | references | pages [60] -->
<​

<!-- b000663 | references | pages [60] -->
http://www.npr.org/blogs/thetwo-way/2014/03/20/291927968/sub-hunting-planes-

<!-- b000664 | references | pages [60] -->
use-high-tech-gear-to-search-for-mh370​

<!-- b000665 | references | pages [60] -->
>.

<!-- b000666 | references | pages [60] -->
[16]"Radar." ​

<!-- b000667 | references | pages [60] -->
RADAR​

<!-- b000668 | references | pages [60] -->
(n.d.): n. pag. ​

<!-- b000669 | references | pages [60] -->
Global Security​

<!-- b000670 | references | pages [60] -->
. Web. 8 Feb. 2015.

<!-- b000671 | references | pages [60] -->
<​

<!-- b000672 | references | pages [60] -->
http://www.globalsecurity.org/military/library/policy/navy/nrtc/14030_ch3.pdf​

<!-- b000673 | references | pages [60] -->
>.

<!-- b000674 | references | pages [60] -->
[17]"How Far Can Airplanes Glide?" Aviation - Stack Exchange. N.p., 05 Apr. 2014.

<!-- b000675 | references | pages [60] -->
Web. 06 Feb. 2015.

<!-- b000676 | references | pages [60] -->
<​

<!-- b000677 | references | pages [60] -->
http://aviation.stackexchange.com/questions/2999/how-far-can-airplanes-glide​

<!-- b000678 | references | pages [60] -->
>.

<!-- b000679 | references | pages [60] -->
[18] "The US Navy." ​

<!-- b000680 | references | pages [60] -->
The US Navy​

<!-- b000681 | references | pages [60] -->
. US Navy, 18 Feb. 2009. Web. 07 Feb. 2015.

<!-- b000682 | references | pages [60] -->
<​

<!-- b000683 | references | pages [60] -->
http://www.navy.mil/navydata/fact_print.asp?cid=1100&tid=1400&ct=1&page=2​

<!-- b000684 | references | pages [60] -->
>.

<!-- b000685 | references | pages [60] -->
[19]Simmering, Jacob. "Bayesian Search Models." ​

<!-- b000686 | references | pages [60] -->
Rbloggers​

<!-- b000687 | references | pages [60] -->
. N.p., 13 Mar. 2014. Web.

<!-- b000688 | references | pages [60] -->
08 Feb. 2015. <​

<!-- b000689 | references | pages [60] -->
http://www.r-bloggers.com/bayesian-search-models/​

<!-- b000690 | references | pages [60] -->
>.

<!-- b000691 | references | pages [60] -->
[20]Ross, Sheldon M. "Conditional Probability And Independence." ​

<!-- b000692 | references | pages [60] -->
A First Course in

<!-- b000693 | references | pages [60] -->
Probability​

<!-- b000694 | references | pages [60] -->
. 9th ed. New York: Macmillan, 1976. 59. Print.

<!-- b000695 | references | pages [60] -->
[21]Krendel, Erza S., and Jerome Wodinsky. ​

<!-- b000696 | references | pages [60] -->
Visual Search in Unstructured Fields​

<!-- b000697 | references | pages [60] -->
.

<!-- b000698 | references | pages [60] -->
Thesis. U.S. Armed Forces, 1960. N.p.: n.p., n.d. Print.

<!-- b000699 | furniture | pages [61] -->
Team #38720

<!-- b000700 | furniture | pages [61] -->
Page 61 of 61

<!-- b000701 | references | pages [61] -->
[22] Piantadosi, Claude. "Prediction of Survival Time in Cold Water." ​

<!-- b000702 | references | pages [61] -->
The Biology of

<!-- b000703 | references | pages [61] -->
Human Survival : Life and Death in Extreme Environments​

<!-- b000704 | references | pages [61] -->
. N.p.: Oxford UP, n.d.

<!-- b000705 | references | pages [61] -->
121-23. Print.

<!-- b000706 | heading | pages [61] -->
8.2 Image References

<!-- b000707 | prose | pages [61] -->
"ASN Records over 80 Aircraft Missing since 1948." ASN News. N.p., 18 Mar. 2014. Web. 06 Feb. 2015. <​ http://news.aviation-safety.net/2014/03/18/asn-records-over-80-aircraft-missing-si nce-1948/​ >.

<!-- b000708 | prose | pages [61] -->
McCaskill, Steve. "Air Traffic Control Systems Could Ditch Radar And Release 5G Spectrum." ​ Tech Week​ . N.p., 13 Feb. 2013. Web. 8 Feb. 2015. <http%253A%252F%252F​ www.techweekeurope.co.uk%252Fworkspace%252F5g-mobile-n etworks-air-traffic-control-107240%2B​ >.

<!-- b000709 | prose | pages [61] -->
"Missing Malaysia Plane: What We Know." ​ BBC News​ . N.p., 30 Jan. 2015. Web. 02 Feb. 2015.

<!-- b000710 | prose | pages [61] -->
Paint.net. Computer software. =. Vers. 4.0.4. DotPDN LLC, n.d. Web. 6 Feb. 2015. <​ http://www.getpaint.net/​ >.

<!-- b000711 | prose | pages [61] -->
Piantadosi, Claude. "Prediction of Survival Time in Cold Water." ​ The Biology of Human Survival : Life and Death in Extreme Environments​ . N.p.: Oxford UP, n.d. 121-23. Print.

<!-- b000712 | prose | pages [61] -->
Wolfram Research, Inc., Mathematica, Version 10.0, Champaign, IL (2014).

<!-- b000713 | prose | pages [61] -->
Microsoft. Microsoft Excel. Redmond, Washington: Microsoft, 2013. Computer Software.
