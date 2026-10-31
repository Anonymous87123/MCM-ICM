# P-B-2015-36178-d0225ad0

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
In this paper, we develop a model for finding a plane that was lost over a large body of water. Our model is very robust and can be used by searchers throughout the entire search process.

<!-- b000002 | prose | pages [1] -->
Using only basic information about the flight and its last known location and heading, we are able to carefully calculate the area where the plane might have gone down. This area is not just a simple circle - the area is limited by the turn radius of the plane and by the maximum distance the plane could have traveled after losing communications.

<!-- b000003 | prose | pages [1] -->
Once our initial search area is determined, our model calculates how ocean currents would cause the search area would move from day to day, as well as change shape. And when debris has been found, the same ocean current calculations can be used in reverse to trace debris back to the original location of the crash.

<!-- b000004 | prose | pages [1] -->
Our model also implements three different algorithms for searching the area determined by our previous calculations. Our algorithms are very flexible, and adapt to changing weather conditions, number of search planes available, and the size of the area to search. Based on detailed analysis of these three algorithms in over 900 unique search scenarios, our model was able to recommend the ideal algorithm for finding any lost plane. Given any combination of factors for a search, our model can predict the number of days it will take to find debris in that region.

<!-- b000005 | furniture | pages [2] -->
Team # 36178

<!-- b000006 | furniture | pages [2] -->
Page 1 of 17

<!-- b000007 | contents | pages [2] -->
So You Lost a Plane?

<!-- b000008 | contents | pages [2] -->
February 10, 2015

<!-- b000009 | heading | pages [2] -->
Contents

<!-- b000010 | contents | pages [2] -->
1 Introduction to Problem

<!-- b000011 | contents | pages [2] -->
3

<!-- b000012 | contents | pages [2] -->
2 Assumptions and Parameters

<!-- b000013 | contents | pages [2] -->
3

<!-- b000014 | contents | pages [2] -->
2.1

<!-- b000015 | contents | pages [2] -->
Assumptions and Justiﬁcations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000016 | contents | pages [2] -->
3

<!-- b000017 | contents | pages [2] -->
2.2

<!-- b000018 | contents | pages [2] -->
Parameters

<!-- b000019 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000020 | contents | pages [2] -->
3

<!-- b000021 | contents | pages [2] -->
3 Analysis of the Problem

<!-- b000022 | contents | pages [2] -->
4

<!-- b000023 | contents | pages [2] -->
3.1

<!-- b000024 | contents | pages [2] -->
Hypotheses

<!-- b000025 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000026 | contents | pages [2] -->
4

<!-- b000027 | contents | pages [2] -->
4 Statement of Model

<!-- b000028 | contents | pages [2] -->
4

<!-- b000029 | contents | pages [2] -->
4.1

<!-- b000030 | contents | pages [2] -->
Components of the Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000031 | contents | pages [2] -->
4

<!-- b000032 | contents | pages [2] -->
4.1.1

<!-- b000033 | contents | pages [2] -->
Modeling a generic “downed plane” using parameters

<!-- b000034 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . .

<!-- b000035 | contents | pages [2] -->
5

<!-- b000036 | contents | pages [2] -->
4.1.2

<!-- b000037 | contents | pages [2] -->
Calculating the present location of the debris ﬁeld using ocean current data . . . . . .

<!-- b000038 | contents | pages [2] -->
5

<!-- b000039 | contents | pages [2] -->
4.1.3

<!-- b000040 | contents | pages [2] -->
Modeling a generic search plane using parameters

<!-- b000041 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . .

<!-- b000042 | contents | pages [2] -->
6

<!-- b000043 | contents | pages [2] -->
4.1.4

<!-- b000044 | contents | pages [2] -->
Searching the probable debris ﬁeld e↵ectively using search planes . . . . . . . . . . . .

<!-- b000045 | contents | pages [2] -->
6

<!-- b000046 | contents | pages [2] -->
4.1.5

<!-- b000047 | contents | pages [2] -->
Using reverse-drift calculation to approximate the origin of the debris

<!-- b000048 | contents | pages [2] -->
. . . . . . . . .

<!-- b000049 | contents | pages [2] -->
6

<!-- b000050 | contents | pages [2] -->
4.2

<!-- b000051 | contents | pages [2] -->
Generating the Search Area . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000052 | contents | pages [2] -->
7

<!-- b000053 | contents | pages [2] -->
4.3

<!-- b000054 | contents | pages [2] -->
Adjusting the search area over time . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000055 | contents | pages [2] -->
9

<!-- b000056 | contents | pages [2] -->
4.4

<!-- b000057 | contents | pages [2] -->
Search Theory

<!-- b000058 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000059 | contents | pages [2] -->
9

<!-- b000060 | contents | pages [2] -->
4.5

<!-- b000061 | contents | pages [2] -->
Conducting an E↵ective Search . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000062 | contents | pages [2] -->
9

<!-- b000063 | contents | pages [2] -->
4.5.1

<!-- b000064 | contents | pages [2] -->
Parallel search

<!-- b000065 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000066 | contents | pages [2] -->
10

<!-- b000067 | contents | pages [2] -->
4.5.2

<!-- b000068 | contents | pages [2] -->
Diagonal search . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000069 | contents | pages [2] -->
11

<!-- b000070 | contents | pages [2] -->
4.5.3

<!-- b000071 | contents | pages [2] -->
Optimized parallel search . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000072 | contents | pages [2] -->
11

<!-- b000073 | contents | pages [2] -->
4.6

<!-- b000074 | contents | pages [2] -->
Full Statement of the Model’s Main Equation . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000075 | contents | pages [2] -->
12

<!-- b000076 | contents | pages [2] -->
4.7

<!-- b000077 | contents | pages [2] -->
Tracing the Findings to the Crash

<!-- b000078 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000079 | contents | pages [2] -->
12

<!-- b000080 | contents | pages [2] -->
5 Results

<!-- b000081 | contents | pages [2] -->
12

<!-- b000082 | contents | pages [2] -->
5.1

<!-- b000083 | contents | pages [2] -->
Comparisons to real-world searches . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000084 | contents | pages [2] -->
12

<!-- b000085 | contents | pages [2] -->
5.2

<!-- b000086 | contents | pages [2] -->
Optimal search methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000087 | contents | pages [2] -->
12

<!-- b000088 | contents | pages [2] -->
5.2.1

<!-- b000089 | contents | pages [2] -->
Behaviors of di↵erent search algorithms . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000090 | contents | pages [2] -->
13

<!-- b000091 | contents | pages [2] -->
5.2.2

<!-- b000092 | contents | pages [2] -->
Choosing the right algorithm for each search

<!-- b000093 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . .

<!-- b000094 | contents | pages [2] -->
13

<!-- b000095 | contents | pages [2] -->
6 Error/Sensitivity Analysis

<!-- b000096 | contents | pages [2] -->
14

<!-- b000097 | contents | pages [2] -->
6.1

<!-- b000098 | contents | pages [2] -->
Sensitivity with respect to the height of the crashed plane . . . . . . . . . . . . . . . . . . . .

<!-- b000099 | contents | pages [2] -->
14

<!-- b000100 | contents | pages [2] -->
6.2

<!-- b000101 | contents | pages [2] -->
Sensitivity with respect to the speed of the crashed plane

<!-- b000102 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . .

<!-- b000103 | contents | pages [2] -->
15

<!-- b000104 | contents | pages [2] -->
6.3

<!-- b000105 | contents | pages [2] -->
Sensitivity with respect to the speed of the wind at time of crash . . . . . . . . . . . . . . . .

<!-- b000106 | contents | pages [2] -->
15

<!-- b000107 | contents | pages [2] -->
6.4

<!-- b000108 | contents | pages [2] -->
Sensitivity with respect to the number of search planes . . . . . . . . . . . . . . . . . . . . . .

<!-- b000109 | contents | pages [2] -->
15

<!-- b000110 | contents | pages [2] -->
6.5

<!-- b000111 | contents | pages [2] -->
Sensitivity with respect to the speed of the wind while searching

<!-- b000112 | contents | pages [2] -->
. . . . . . . . . . . . . . . .

<!-- b000113 | contents | pages [2] -->
15

<!-- b000114 | contents | pages [2] -->
6.6

<!-- b000115 | contents | pages [2] -->
Sensitivity with respect to the visibility while searching

<!-- b000116 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . .

<!-- b000117 | contents | pages [2] -->
15

<!-- b000118 | furniture | pages [3] -->
Team # 36178

<!-- b000119 | furniture | pages [3] -->
Page 2 of 17

<!-- b000120 | heading | pages [3] -->
7 Analysis of our Model

<!-- b000121 | prose | pages [3] -->
15 7.1 Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15 7.2 Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15 7.3 Future improvements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16

<!-- b000122 | heading | pages [3] -->
8 Conclusion

<!-- b000123 | prose | pages [3] -->
16

<!-- b000124 | furniture | pages [4] -->
Team # 36178

<!-- b000125 | furniture | pages [4] -->
Page 3 of 17

<!-- b000126 | heading | pages [4] -->
1 Introduction to Problem

<!-- b000127 | prose | pages [4] -->
The problem we chose to solve was how to most e↵ectively search for a lost airplane that is expected to have gone down over a large body of water. We developed a method to ﬁnd lost planes in the least amount of time, which entails obtaining an accurate estimation of where the plane may have gone down, developing a fast and eﬃcient search algorithm that adapts to new information, and calculating the location of the lost plane based on ocean currents.

<!-- b000128 | heading | pages [4] -->
2 Assumptions and Parameters

<!-- b000129 | heading | pages [4] -->
2.1 Assumptions and Justiﬁcations

<!-- b000130 | prose | pages [4] -->
Our model makes the following assumptions:

<!-- b000131 | prose | pages [4] -->
1. Generally speaking, the plane crash will occur in the way that will make the search the most diﬃcult.

<!-- b000132 | prose | pages [4] -->
This is justiﬁed because assuming the most diﬃcult scenario in modeling makes the model compatible with the most plane crash scenarios.

<!-- b000133 | prose | pages [4] -->
2. We assume that air drag will not a↵ect the distance a plane travels in a crash. The ﬁrst reason we do not consider air drag is because it greatly complicates the model. Second, data necessary for calculating air drag such as the cross-sectional width of the planes and the coeﬃcient of air drag of the planes was not readily available. Finally, in determining the distance that a plane will travel while crashing, air drag will both limit the distance and increase the distance. This is because air drag opposes the forward motion of the plane but also increases the time that the plane remains in forward motion by limiting the speed with which the plane falls.

<!-- b000134 | prose | pages [4] -->
3. Due to the small size of airplane debris, search planes will not be able to use infrared or radar and will have to rely on visual search alone, even in very calm seas. Our source indicated that even in rather calm seas, forward-looking airborne radar and infrared technology would be completely unable to detect small debris.[2]

<!-- b000135 | prose | pages [4] -->
4. The ﬁeld of debris will not scatter so far from the site of the crash that it will change our overall search area. Justiﬁcation for this assumption can be found in Section 4.2.

<!-- b000136 | prose | pages [4] -->
5. The area in which the plane crashes is completely water and is ﬂat enough to be modeled as a geometric plane. The curvature of the ocean is extremely small and would be insigniﬁcant for all calculations.

<!-- b000137 | prose | pages [4] -->
6. Fatigue of searchers will not impact their e↵ectiveness. Fatigue is too diﬃcult to model because it has di↵erent e↵ects on di↵erent individuals, and we can assume further that individuals impaired by fatigue would not be allowed to participate in the search.

<!-- b000138 | prose | pages [4] -->
7. All search planes are assumed to take o↵200 nautical miles from the search location. We consider this a reasonable distance, since our model does not know where the nearest land mass or aircraft carrier may be. (A discussion of this assumption can be found in Section 7.)

<!-- b000139 | prose | pages [4] -->
8. There will be suﬃcient daylight for searching for only 10 hours each day. In most locations, this will let searchers start at least one hour after sunrise and end at least one hour before sunset.

<!-- b000140 | prose | pages [4] -->
9. Floating debris will not sink until after the search has been completed. Because it’s impossible to accurately model when the debris will sink, we must assume that it has not sunk yet.

<!-- b000141 | heading | pages [4] -->
2.2 Parameters

<!-- b000142 | prose | pages [4] -->
Our model uses several parameters to help determine where a plane was likely to crash. We use the altitude, velocity, and mass of the downed plane as parameters to help determine how far the plane likely traveled while crashing. The wind speed at the time of the crash is also considered when determining this distance.

<!-- b000143 | furniture | pages [5] -->
Team # 36178

<!-- b000144 | furniture | pages [5] -->
Page 4 of 17

<!-- b000145 | prose | pages [5] -->
Another main focus of our model was developing the most e↵ective search pattern. We took many parameters into consideration while determining this search method including the altitude, velocity, and range of search planes, the number of search planes that are available, the time since the crash, and the time allotted for the search each day (assumed to be 10 hours), and what the weather conditions of current search day.

<!-- b000146 | prose | pages [5] -->
Our model also describes how to e↵ectively use found debris to locate the site of the crash. The parameters we used to determine this method are the speed and direction of the ocean currents and the time since the crash, as mentioned earlier.

<!-- b000147 | heading | pages [5] -->
3 Analysis of the Problem

<!-- b000148 | heading | pages [5] -->
3.1 Hypotheses

<!-- b000149 | prose | pages [5] -->
Helping plan a useful search for a generic downed plane is a problem which can be split into two parts: predicting where it went down, and searching that area. After some discussion, we concluded that we should be able to ﬁgure out the area where the plane went down by modeling how far a plane can glide without power, while accounting for the possibility of turning while gliding. We also realized that the currents of the ocean would be moving the debris away from the plane crash as time went on, so the area to search would move each day. We then hypothesized that there are several ways to search the area, such as the three illustrated in Figure 1.

<!-- b000150 | caption | pages [5] -->
Figure 1: Some of our initial ideas for how to search a rectangular area.

<!-- b000151 | prose | pages [5] -->
Some search methods were discounted immediately due to obvious ineﬃciency and inability to be adapted to multiple searchers. We hypothesized that going in straight lines as much as possible when searching an area would maximize the eﬃciency of the search, an assumption that let us rule out searches like the spiral search in Figure 1. That same assumption also brought to the forefront searches that use parallel sweeps, such as the other two illustrated in Figure 1.

<!-- b000152 | heading | pages [5] -->
4 Statement of Model

<!-- b000153 | prose | pages [5] -->
Our model provides suggestions for searchers throughout the entire search process. Based on the parameters stated above, our model calculates the area in which the plane could have crashed, calculates the motion of that area due to ocean currents over time, provides estimates for the time required to ﬁnd crash debris, and uses the speed and direction of local ocean currents to trace debris back to its original location, near the site of the plane crash.

<!-- b000154 | heading | pages [5] -->
4.1 Components of the Model

<!-- b000155 | prose | pages [5] -->
Based on our analysis of the problem, we split the model into the following components:

<!-- b000156 | prose | pages [5] -->
1. Modeling a generic downed plane using parameters

<!-- b000157 | prose | pages [5, 6] -->
2. Calculating the size and shape of the area where the plane likely went down 3. Calculating the probable location of the debris ﬁeld over time using ocean current data

<!-- b000158 | furniture | pages [6] -->
Team # 36178

<!-- b000159 | furniture | pages [6] -->
Page 5 of 17

<!-- b000161 | prose | pages [6] -->
4. Modeling a generic search plane using parameters

<!-- b000162 | prose | pages [6] -->
5. Searching the probable debris ﬁeld e↵ectively using search planes

<!-- b000163 | prose | pages [6] -->
6. Using reverse-drift calculation to approximate the origin of the debris

<!-- b000164 | heading | pages [6] -->
4.1.1 Modeling a generic “downed plane” using parameters

<!-- b000165 | prose | pages [6] -->
We model a downed plane using the following parameters:

<!-- b000166 | prose | pages [6] -->
1. Its last known longitude and latitude as established by an automatic handshake or an Air Traﬃc Control scheduled check-in

<!-- b000167 | prose | pages [6] -->
2. Its direction of travel, in terms of degrees. (0 degrees is East, 90 North, 180 West, and 270 South)

<!-- b000168 | prose | pages [6] -->
3. The family that the plane belongs to:

<!-- b000169 | prose | pages [6] -->
(a) Small bush plane (b) Military ﬁghter (c) Private jet (d) Commercial airliner (e) Cargo plane

<!-- b000170 | prose | pages [6] -->
4. The parameters determined by the family of the plane:

<!-- b000171 | prose | pages [6] -->
(a) Cruising speed (b) Cruising altitude (c) Typical takeo↵mass

<!-- b000172 | prose | pages [6] -->
The ﬁve main families of planes each have di↵erent speeds, altitudes, and masses, so we decided to pick a representative from each family and model it. That representitive would have to be commonly ﬂown and thus be more likely to crash, making it a good choice to model. The representatives chosen are as follows:

<!-- b000173 | prose | pages [6] -->
1. Small bush plane: Cessna 172 Skyhawk[11]

<!-- b000174 | prose | pages [6] -->
2. Military ﬁghter: Lockheed Martin F-22A Raptor[12]

<!-- b000175 | prose | pages [6] -->
3. Private jet: Bombardier Challenger 300[13]

<!-- b000176 | prose | pages [6] -->
4. Commercial airliner: Boeing 737-300 Classic[14][15][16]

<!-- b000177 | prose | pages [6] -->
5. Cargo plane: Lockheed C-5B Galaxy[17]

<!-- b000178 | prose | pages [6] -->
The height and speed of the plane were used to calculate its maximum glide distance without power, which is then used to determine the shape of the probable “splash-down” location. The mass is used to calculate its inertia, which makes it more resistant to the e↵ects of crosswinds as it glides.

<!-- b000179 | heading | pages [6] -->
4.1.2 Calculating the present location of the debris ﬁeld using ocean current data

<!-- b000180 | prose | pages [6] -->
The likely outcome of a plane crash in open water is that, upon impact, the plane is destroyed and debris from the plane will be propelled a relatively short distance. Some of this debris will sink, but some of it will ﬂoat and be carried by the currents in that area. After determining an approximate location for the site of the plane crash, we can calculate where the ocean current will carry the debris. This process is outlined in section 4.3.

<!-- b000181 | prose | pages [6] -->
The parameters that we used to model the ocean currents were the speed and direction of the currents. The debris resulting from a plane crash will continue to be carried by the currents until it is found by searchers. When a piece of debris is found in a search, the time and location of that debris provides important information that can be analyzed mathematically to obtain a better estimation of the location of the crash.

<!-- b000182 | furniture | pages [7] -->
Team # 36178

<!-- b000183 | furniture | pages [7] -->
Page 6 of 17

<!-- b000184 | heading | pages [7] -->
4.1.3 Modeling a generic search plane using parameters

<!-- b000185 | prose | pages [7] -->
The primary parameters that we use for modeling a generic search plane are:

<!-- b000186 | prose | pages [7] -->
1. Flight speed while searching

<!-- b000187 | prose | pages [7] -->
2. Altitude while searching

<!-- b000188 | prose | pages [7] -->
3. Range of the search plane determined by fuel capacity

<!-- b000189 | prose | pages [7] -->
The speed is used to calculate the search plane’s turn radius, as well as to determine how much area the plane can search before the sun goes down. Range is also used as a limiting factor when calculating the area the plane should search.

<!-- b000190 | prose | pages [7] -->
Speed and altitude are also used to calculate the aircraft’s e↵ective sweep width. (A description of e↵ective sweep width is presented in section 4.4.) Due to the many varying factors that may a↵ect an airplane’s sweep width, there is no one formula to calculate this. The United States National Search and Rescue Committee maintains tables of estimated e↵ective sweep widths based on altitude, weather conditions, and size of the lost object.[2] We used Mathematica to interpolate this data and create a global sweep width function that accepts any inputs, even those not on the table.

<!-- b000191 | heading | pages [7] -->
4.1.4 Searching the probable debris ﬁeld e↵ectively using search planes

<!-- b000192 | prose | pages [7] -->
Once the model has generated a search area, it can calculate the best way to search it for debris. There are many parameters used in this calculation: the number of search planes available, the types of planes available and their search e↵ectiveness, prevailing weather conditions, visibility (how far one can see in terms of nautical miles), and the size of the area to search. How the search is actually performed is described below in section 4.5

<!-- b000193 | heading | pages [7] -->
4.1.5 Using reverse-drift calculation to approximate the origin of the debris

<!-- b000194 | prose | pages [7] -->
The exact time and location should be noted when a piece of debris is found. With accurate data that gives the speed and direction of the ocean currents, the calculation used to predict the future location of the debris can be used in reverse to trace the debris back to its origin. This gives us a more accurate estimation of the location of the crash. This process is described mathematically in section 4.3.

<!-- b000195 | caption | pages [7] -->
Figure 2: A vector ﬁeld representing the ocean currents moving an object[21]

<!-- b000196 | furniture | pages [8] -->
Team # 36178

<!-- b000197 | furniture | pages [8] -->
Page 7 of 17

<!-- b000198 | heading | pages [8] -->
4.2 Generating the Search Area

<!-- b000199 | prose | pages [8] -->
To estimate the area where the plane could have gone down, our model takes into account various attributes of the plane. We calculate the maximum unpowered glide distance (d) using this formula:[19]

<!-- b000200 | prose | pages [8] -->
d = altitude tan(✓)

<!-- b000201 | prose | pages [8] -->
where ✓is the angle between the incoming plane’s trajectory and the ocean surface at which the plane descends. We treat d as the maximum distance the plane could have traveled since we last had contact with it.

<!-- b000202 | prose | pages [8] -->
A simpler model would use this maximum travel distance as the radius of a circle. But by using the turn radius of the airplane, we can reﬁne our estimate and reduce the search area. We consider that the plane could have changed direction after we lost contact with it, but that the radius of its turn will a↵ect how far it can travel after changing direction. To calculate the turn radius, we start by assuming completely horizontal motion initially, then integrating horizontal velocity (in nautical miles per second) as the aircraft turns 90 degrees. At a rate of 1.5 degrees per second, this takes 60 seconds.

<!-- b000203 | prose | pages [8] -->
Vx(t) = speed ⇤cos(1.5t) Z 60 (1) r = Vx(t)dt 0 Consider an aircraft travelling at 500 knots, with a maximum glide distance of 40 nautical miles. Its turn radius is then 5.31 nautical miles. If the airplane does not turn, it can travel 40 nautical miles from the last point of contact. But if it makes a 90◦turn, it can only travel another 32 nautical miles because of the distance spent turning. If it turns 180◦, it can only travel another 23 nautical miles. Figure 3 demonstrates this fact visually.

<!-- b000204 | caption | pages [8] -->
Figure 3: The more our example airplane turns, the less it can ﬂy after the turn ends.

<!-- b000205 | prose | pages [8] -->
By generalizing this notion, we arrive at the following equations for the ﬁnal horizontal and vertical positions of the plane, given the angle turned:

<!-- b000206 | prose | pages [8] -->
" # x(✓) = r ⇤sin(✓) + cos(✓) ⇤ d −arclength(✓, r) " # " # (2) y(✓) = r ⇤ −cos(✓) + 1) + sin(✓) ⇤ d −arclength(✓, r) Using these formulas for our example plane gives us the result in Figure 4. When we mirror this result vertically to allow for the plane turning to the right, we get the result in Figure 5.

<!-- b000207 | prose | pages [8, 9] -->
After generating these points, the model applies a rotation matrix to orient the shape to the heading of the airplane at the last point of contact. Because we take the speed of the wind at the time of the crash as a parameter, we know how fast it was blowing, but not which direction it was blowing in. Because of that uncertainty, we decided to increase the size of the search area dependent on that wind. To that end, we The smaller circle represents the airplane’s turn radius.

<!-- b000208 | furniture | pages [9] -->
Team # 36178

<!-- b000209 | furniture | pages [9] -->
Page 8 of 17

<!-- b000210 | caption | pages [9] -->
Figure 4: The possible end locations for our example plane, if it turns only to the left.

<!-- b000212 | caption | pages [9] -->
Figure 5: The full range of end locations for our example plane.

<!-- b000213 | prose | pages [9] -->
had the model iterate through the originally generated edge points, calculate their normal vectors from the center, and add the normal vector scaled by the wind speed to the original point. Thus, the entire perimeter was expanded by the speed of the wind.

<!-- b000214 | prose | pages [9] -->
The model then applies a convex hull algorithm and saves the result as the initial search area. For those unfamiliar with the concept of a convex hull algorithm, it is a method that produces a polygon that “shrinkwraps” a set of points in the (x,y) plane. It does this by iterating through the points to construct a polygon obeying the following rules:

<!-- b000215 | prose | pages [9] -->
1. All points in the set are either inside the polygon or are vertices

<!-- b000216 | prose | pages [9] -->
2. The chord drawn between any two points is either an interior chord or an edge; it can never leave the boundary of the polygon

<!-- b000217 | prose | pages [9] -->
By using a convex hull algorithm, we were able to simplify the complex search shape into an almost elliptical shape, and as such we arrived at our initial area in which the plane could have gone down.

<!-- b000218 | prose | pages [9, 10] -->
We had originally considered adding an additional expansion of perimeter based on the debris ﬂying away from the initial point of impact, creating a “splash” e↵ect. However, we found that due to the terminal velocities of typical pieces of debris, such an expansion would only have a marginal impact on the original shape. As such, we chose not to model this aspect of the crash, and we believe that it does not a↵ect our calculations signiﬁcantly.

<!-- b000219 | furniture | pages [10] -->
Team # 36178

<!-- b000220 | furniture | pages [10] -->
Page 9 of 17

<!-- b000222 | heading | pages [10] -->
4.3 Adjusting the search area over time

<!-- b000223 | prose | pages [10] -->
Now that we have an n-gon that bounds where the plane could have landed in the water at the time of impact, we needed to account for the drifting of debris due to ocean currents. We were able to obtain ocean current data for the vicinity of the Malaysia Airlines MH370 crash, so we decided to model the planes as if they crashed near there. To calculate how the search area would move and reshape, we took the original search area and placed it over a grid. Each square in the grid was given a “search marker”, and that search marker’s longitude and latitude were recorded. To simplify the model, we made it such that the search area only moves discretely overnight, as opposed to the real-life continuous movement of currents. Each cycle took the current search marker locations, drifted that marker by 24 hours, then stored that new location back.

<!-- b000224 | prose | pages [10] -->
We used Euler’s method to approximate the motion of the debris over time. To do that, we scaled the velocity vector of the current at the debris’ location by the time interval, and then added that vector to the position. This process is demonstrated below:[21]

<!-- b000225 | prose | pages [10] -->
(longituden, latituden) ⇡(longitude0, latitude0)+∆t(@(longitude)0 , @(latitude)0 @(hours) ) + ...+ @(hours) (3) ∆t(@(longitude)n−1 , @(latitude)n−1 ) @(hours) @(hours)

<!-- b000226 | prose | pages [10] -->
Once all the original search markers were drifted by a whole day’s displacement, we called the convex hull algorithm again to create the new containing n-gon, and the subsequent search area.

<!-- b000227 | heading | pages [10] -->
4.4 Search Theory

<!-- b000228 | prose | pages [10] -->
In the ﬁeld known as Search Theory, the underlying goal with each search is to maximize the Probability of Detection (POD). The POD is generally deﬁned using the following parameters and equation:[3]

<!-- b000229 | prose | pages [10] -->
1. t = time allotted to perform the search, or the time that the search has been going on

<!-- b000230 | prose | pages [10] -->
2. n = number of searchers

<!-- b000231 | prose | pages [10] -->
3. r = rate of search, or speed of the searchers

<!-- b000232 | prose | pages [10] -->
4. s = e↵ective search width

<!-- b000233 | prose | pages [10] -->
5. a = total area to be searched

<!-- b000234 | prose | pages [10] -->
✓ ◆ −t · r · n · s POD = 1 −eˆ (4) a

<!-- b000235 | prose | pages [10] -->
The e↵ective search width is not an easily deﬁnable number, but more of a concept. One of the simpler ways to think about it is as such: suppose there is a rectangular search area, a, that has n objects to ﬁnd in it. Now suppose that you had just one pass through a and you wanted to ﬁnd at least n 2 objects. Then the e↵ective search width is the the minimum distance around you that would allow you to ﬁnd those n 2 objects by walking in a straight line through a.

<!-- b000236 | heading | pages [10] -->
4.5 Conducting an E↵ective Search

<!-- b000237 | prose | pages [10] -->
Now that we have a search area that changes location and shape with time, the second part of our model compares three search methods and decides which of them gives the best Probability of Detection. These were the methods that we tested:

<!-- b000238 | furniture | pages [11] -->
Team # 36178

<!-- b000239 | furniture | pages [11] -->
Page 10 of 17

<!-- b000240 | prose | pages [11] -->
1. A search that has the searchers moving parallel to the longer edge of the bounding rectangle in parallel segments

<!-- b000241 | prose | pages [11] -->
2. A search that has the searchers moving diagonally at an angle of 45◦to the longer edge of the bounding rectangle in parallel segments

<!-- b000242 | prose | pages [11] -->
3. An optimized version of the ﬁrst search method.

<!-- b000243 | prose | pages [11] -->
All three search algorithms take the following parameters: a list of search planes, the size of the bounding rectangle, visibility, and wind conditions. All three algorithms return the total area swept during that day’s search. This will be represented by A in the sections below.

<!-- b000244 | heading | pages [11] -->
4.5.1 Parallel search

<!-- b000245 | prose | pages [11] -->
The parallel search method is the simplest search algorithm we tested. In this algorithm, search planes simply ﬂy in straight paths parallel to the long edge of the search rectangle. This minimizes time spent turning around for another sweep and maximizes time spent searching.

<!-- b000246 | prose | pages [11] -->
The United States National Search and Rescue Supplement to the International Aeronautical and Mar- itime Search and Rescue Manual deﬁnes some helpful terminology for describing this type of search. The long tracks that the search planes ﬂy along the search area are called searchleg straightaways. The paths that the planes ﬂy while going from one searchleg straightaway to another are called crosslegs. (See Figure 6 for a visual representation of this terminology.)

<!-- b000247 | caption | pages [11] -->
Figure 6: A visual representation of one leg of a search plane’s search path. (Source:

<!-- b000248 | prose | pages [11] -->
United States National Search and Rescue Supplement to the International Aeronautical and Maritime Search and Rescue Manual)

<!-- b000249 | prose | pages [11] -->
In our algorithm, each leg of the plane’s search after the ﬁrst one consists of two searchleg straightaways and two cross segments.[2] The ﬁrst leg of the search only contains one cross segment. Because the searchleg straightaway is the part of the sweep actually spent searching, we attempt to maximize the time spent on these segments. The crosslegs are made up of two quarter-turns and a crossleg straightaway to bring the plane to the next sweep location.

<!-- b000250 | prose | pages [11] -->
Based on the range of each plane, the speed at which they can search, and the total area left to search, the algorithm computes how many full search legs each plane can complete that day. The width of that search area is then assigned to that plane, and the algorithm moves on to the next plane. This process repeats until either there are no planes left with which to search or the entire area has been searched.

<!-- b000251 | prose | pages [11] -->
The area swept by this algorithm can be calculated by Equation 5, where n is the number of planes used in the search and L is the length of one full sweep across the search area:

<!-- b000252 | prose | pages [11] -->
⇣ ⌘ n X sweepwidth(planei) · numlegs(planei) · 2 · L A = (5) i=1

<!-- b000253 | furniture | pages [12] -->
Team # 36178

<!-- b000254 | furniture | pages [12] -->
Page 11 of 17

<!-- b000255 | heading | pages [12] -->
4.5.2 Diagonal search

<!-- b000256 | prose | pages [12] -->
The diagonal search method is based on the same principles as the parallel search method, but in this method the search planes ﬂy at a 45◦angle to the long side of the rectangle. This changes the search in a few key ways.

<!-- b000257 | prose | pages [12] -->
Firstly, this search method allows search planes to make much longer sweeps across the search area. It thus maximizes time spent searching near the middle of the search area. However, near the corners of the search area, the searchlegs can be extremely short, and many more turns must be made. In addition, the angle of the paths causes the crossleg straightaway distance to increase for all crosslegs.

<!-- b000258 | prose | pages [12] -->
The area swept by this algorithm is more diﬃcult to calculate. Equation 6 provides a formula for the calculation, where w and h are the search area’s longer and shorter dimensions, respectively.

<!-- b000259 | prose | pages [12] -->
⇣ ⌘ n X sweepwidth(planei) · numlegs(planei) · 2 SW = i=1 ⌘ ⇣⇡ c1 = h · sin 4 ⌘ ⇣⇡ (6) c2 = w · sin 4 8 SW 2 > if SW < c1 < c2 A = 1 + 2c1 · (SW −c1) if c1 SW < c2 > : wh −(c2 + c1 −SW)2 if c2 SW c2 + c1

<!-- b000260 | heading | pages [12] -->
4.5.3 Optimized parallel search

<!-- b000261 | prose | pages [12] -->
A major drawback of both the ﬁrst two methods is that they cannot use any more search planes once 100% of the search area has been swept. We can improve on this behavior by assigning extra search planes to sweep the area again, increasing the search coverage and probability of detection.

<!-- b000262 | prose | pages [12] -->
This algorithm begins by running the original parallel search algorithm, and saving each of the plane’s search paths as a ”search block” for that type of plane. Each search block stores the type of plane it contains, the number of search legs it contains, and the number of search planes assigned to the block. The algorithm assumes that a search block can contain at most as many planes as it has search legs; for example, a search block with ﬁve search legs can hold at most ﬁve search planes.

<!-- b000263 | prose | pages [12] -->
The planes in a search block cannot all begin their search at the same time; instead, each must ”wait in line” for the plane in front of them to complete a leg. Because all aircraft must ﬁnish searching in the allotted time, aircraft that begin their search later cannot search as great an area. This algorithm has each search plane complete one less search leg than the plane before it; for example, in a block with three search legs and three planes, the ﬁrst plane would complete all three possible legs, the second plane would complete two, and the third plane would complete only one. All planes in the block ﬁnish at the same time, before their allotted search time expires.

<!-- b000264 | prose | pages [12] -->
For every consecutive plane, the algorithm ﬁnds the search block of that plane’s type that has the most empty space for another plane. It repeats this process until all the blocks are ﬁlled or there are no more planes left with which to search.

<!-- b000265 | prose | pages [12] -->
To compute the area e↵ectively swept in each block, the algorithm calculates the number of total search legs swept by planes in the block. If Li is the number of legs in block i and Pi is the number of planes in block i, then the total legs swept in block i is:

<!-- b000266 | prose | pages [12, 13] -->
" # TLi = Li + (Li −1) + (Li −2) + . . . + Li −(Pi −1) Pi X " # Li − 1 + 2 + 3 + . . . + (Pi −1) = (7) k=1 = Li · Pi −Pi · (Pi −1) 2 The total area swept can then be calculated using Equation 8 below, where n is the number of search blocks and L is the length of one full sweep across the search area.

<!-- b000267 | furniture | pages [13] -->
Team # 36178

<!-- b000268 | furniture | pages [13] -->
Page 12 of 17

<!-- b000270 | prose | pages [13] -->
⇣ ⌘ n X sweepwidth(blocki) · TLi · 2 · L Aswept = (8) i=1

<!-- b000271 | heading | pages [13] -->
4.6 Full Statement of the Model’s Main Equation

<!-- b000272 | prose | pages [13] -->
Using the equation above and the equations below, our model can approximate how many days it will take to complete the search.

<!-- b000273 | prose | pages [13] -->
Asearch = (max width of n −gon) · (max height of n −gon) ✓ ◆ −Aswept POD = 1 −eˆ Asearch (9) days X POD > 0.95 i=1

<!-- b000274 | heading | pages [13] -->
4.7 Tracing the Findings to the Crash

<!-- b000275 | prose | pages [13] -->
Given the location of an object that has been moved by the current for t hours, we use Euler’s method once again to trace the object back to its original location. This is done by taking the di↵erence of the position of the debris and the velocity vector of the current scaled by a time interval, ∆t. This process is demonstrated t below and is repeated ∆t times to approximate the original location of the debris.

<!-- b000276 | prose | pages [13] -->
(longitude0, latitude0) ⇡(longitudef, latitudef)−∆t(@(longitude)f , @(latitude)f ) −...− @(hours) @(hours) (10) ∆t(@(longitude)1 , @(latitude)1 @(hours) ) @(hours)

<!-- b000277 | heading | pages [13] -->
5 Results

<!-- b000278 | heading | pages [13] -->
5.1 Comparisons to real-world searches

<!-- b000279 | prose | pages [13] -->
In order to determine whether our search area and current drift calculations are accurate, it is helpful to draw comparisons to searches for lost planes in the real world. The most famous airline crash of recent memory was the March 2014 crash of Malaysia Airlines ﬂight MH370. However, the crash of MH370 involved several other unforeseen variables and uncertainties that make ﬁnding an accurate search area diﬃcult, if not impossible. Instead, we will compare our model’s result to the 2009 crash of Air France ﬂight 447, which is a good example of a standard commercial airliner crash that was found using standard search methods. The search area for AF447 was determined to be a circle of radius 40 nautical miles.[1] However, when we plugged the data from that type of plane into our model (an Airbus A330[18]) we calculated a search radius of about 125 nautical miles. The reason ours is so much larger is because our model assumes we know very little about the crash. In the case of AF447, ﬂight control expected to receive two messages only 60 seconds apart, but it only received one. That gave them a very precise estimation of the time and manner in which the plane went down.[1]. Our model does not expect this level of precision, and thus generates an outer bound of where the plane could have gone down.

<!-- b000280 | heading | pages [13] -->
5.2 Optimal search methods

<!-- b000281 | prose | pages [13] -->
Our model ran detailed analysis on our three di↵erent search methods with varying numbers of search planes, weather conditions, visibility distances, and sizes of search areas. For each combination of variables, we calculated the number of days each algorithm would require in order to raise the probability of detection above 95%. Each search method showed strengths and weaknesses depending on the unique combination of these variables. Figure 7 gives a visual representation of the results from the latter two search methods.

<!-- b000282 | furniture | pages [14] -->
Team # 36178

<!-- b000283 | furniture | pages [14] -->
Page 13 of 17

<!-- b000284 | heading | pages [14] -->
5.2.1 Behaviors of di↵erent search algorithms

<!-- b000285 | prose | pages [14] -->
The simple parallel search worked reliably in all of our di↵erent test cases. While it was usually not as eﬃcient as the diagonal search, it did not produce any unexpected or impractical results. Its worst-case time was 3581 days, with only 1 plane searching in 30+ knot wind and 1 nautical mile of visibility over 112,640 square nautical miles. However, the best-case time for this algorithm was three days, even with dozens of extra planes, because it did not have the means to cover more than 100% of a search area in a given day.

<!-- b000286 | prose | pages [14] -->
The diagonal search generally performed better than the simple parallel search, usually achieving 95% POD in a median of two fewer days. However, if run with only a few planes under adverse conditions, the algorithm produced extremely ineﬃcient searches. With only one plane and limited visibility, this algorithm sometimes took upward of 35,000 days to reach 95% POD—nearly 100 years of searching! The diagonal search algorithm also has the same best-case time of three days, since it likewise cannot put extra planes to use.

<!-- b000287 | prose | pages [14] -->
The diagonal search was our best-performing algorithm overall. Its performance was better than the simple parallel search in most cases. Even though under adverse conditions this search does extremely poor, most of the time, given typical search conditions, it will be faster than the optimized parallel. Under intense time pressure, when the lives of the plane’s passengers may be at stake, this factor is highly desirable.

<!-- b000288 | caption | pages [14] -->
Figure 7: A visual representation of the results from our analysis of di↵erent search meth-

<!-- b000289 | prose | pages [14] -->
ods. Red dots represent results from the diagonal search algorithm; blue dots represent the optimized parallel search algorithm. The horizontal axis is the unique index of the search in our data. The vertical axis is the number of days in which the search was completed.

<!-- b000290 | prose | pages [14] -->
Values toward the right of the plot represent searches with more planes and higher wind speeds.

<!-- b000291 | heading | pages [14] -->
5.2.2 Choosing the right algorithm for each search

<!-- b000292 | prose | pages [14] -->
It is clear that none of our search methods are perfect for every search, because each method has a best and worst case depending on the parameters of the search. When planning a real-life search for a missing aircraft, every single day spent searching is another day that lives may be lost, so choosing the optimal search method for each day is critical. We will compare and contrast our latter two search methods: the diagonal search and the optimized parallel search.

<!-- b000293 | prose | pages [14] -->
The diagonal search algorithm usually exhibits better performance than the optimized parallel search. We suggest that this is because search legs near the middle of the search area can be much longer than those in the parallel method. However, the diagonal search exhibits worse performance than the optimized parallel search under a few speciﬁc conditions—sometimes worse than the optimized parallel search by several orders of magnitude. The worst performance of the diagonal search algorithm occurs when searching a large area with very few search planes and bad weather conditions. As visibility decreases and wind speed increases, this algorithm exhibits poorer and poorer performance until it reports the incredible 35,000 days mentioned above.

<!-- b000294 | furniture | pages [15] -->
Team # 36178

<!-- b000295 | furniture | pages [15] -->
Page 14 of 17

<!-- b000296 | prose | pages [15] -->
The diagonal search also exhibits worse performance when searching a small area with many search planes in good weather conditions. In these situations, the optimized parallel search is able to sweep sections of the search area more than once each day, which can dramatically increase coverage and probability of detection. Under these conditions, the optimized parallel search algorithm can sometimes complete its search in just one day.

<!-- b000297 | prose | pages [15] -->
Based on these results, we can recommend the following courses of action:

<!-- b000298 | prose | pages [15] -->
• If using few search planes, the search area is large, and weather conditions are bad: Use the optimized parallel search.

<!-- b000299 | prose | pages [15] -->
• If using many search planes, the search area is small, and weather conditions are good: Use the optimized parallel search.

<!-- b000300 | prose | pages [15] -->
• Otherwise: Use the diagonal search.

<!-- b000301 | heading | pages [15] -->
6 Error/Sensitivity Analysis

<!-- b000302 | prose | pages [15] -->
Because our model does not ﬁnd an optimal solution, but instead predicts the number of days it will take to search any area, our sensitivity analysis will be based on a median problem, and we will then see how changing the input parameters a↵ects the number of days the search will take. The parameters we analyzed are:

<!-- b000303 | prose | pages [15] -->
1. Height of the crashed plane

<!-- b000304 | prose | pages [15] -->
2. Speed of the crashed plane

<!-- b000305 | prose | pages [15] -->
3. Speed of the wind at the time of the crash

<!-- b000306 | prose | pages [15] -->
4. The number of search planes in the air searching

<!-- b000307 | prose | pages [15] -->
5. The speed of the wind while searching

<!-- b000308 | prose | pages [15] -->
6. The visibility range during the search

<!-- b000309 | prose | pages [15] -->
For our sensitivity analysis, we had each of those parameters set to the following as the “baseline” we would compare against:

<!-- b000310 | prose | pages [15] -->
1. 45000 feet cruising altitude

<!-- b000311 | prose | pages [15] -->
2. 459 knot cruising speed

<!-- b000312 | prose | pages [15] -->
3. 10 knot wind at time of crash

<!-- b000313 | prose | pages [15] -->
4. 21 search planes (AP-3C Orion)[9]

<!-- b000314 | prose | pages [15] -->
5. 20 knot wind while searching

<!-- b000315 | prose | pages [15] -->
6. 14.6 nautical miles of visibility

<!-- b000316 | prose | pages [15] -->
These parameters generate a search area of 85,957 square nautical miles to search. This baseline generates an estimated search time of 11 days.

<!-- b000317 | prose | pages [15] -->
To perform our analysis, we changed each parameter individually and compared the new resulting esti- mated days to our baseline of 11 days. We kept altering the deviation until we had a change on both sides, or until we were convinced that changing in one direction would be ine↵ective.

<!-- b000318 | heading | pages [15] -->
6.1 Sensitivity with respect to the height of the crashed plane

<!-- b000319 | prose | pages [15] -->
We found that changing the altitude that the crashed plane was ﬂying at by a deviation of 4000 feet created a change in both directions. Decreasing the height by 4000 feet led to 10 days of searching, and increasing by 4000 feet led to 12 days of searching. As such, it appears that a linear change of the height results in a linear change in the number of days to search at a rate of 1/4000.

<!-- b000320 | furniture | pages [16] -->
Team # 36178

<!-- b000321 | furniture | pages [16] -->
Page 15 of 17

<!-- b000322 | heading | pages [16] -->
6.2 Sensitivity with respect to the speed of the crashed plane

<!-- b000323 | prose | pages [16] -->
When we changed the speed of the crashed plane, it only altered the turn radius which in turn altered the size of the search area. However, we found that any reasonable change in the speed from our baseline (459 knots) only had a marginal e↵ect on the estimated days, and as such this does not appear to a↵ect our sensitivity analysis.

<!-- b000324 | prose | pages [16] -->
6.3 Sensitivity with respect to the speed of the wind at time of crash

<!-- b000325 | prose | pages [16] -->
When we altered the speed that the wind was blowing at to be anything less than 10 knots, we found that it did not a↵ect the estimated number of days. However, increasing the speed by 5 knots gave us 1 more day that we had to search. Thus, this appears to a↵ect the answer in a linear fashion above 10 knots at a rate of 1/5.

<!-- b000326 | heading | pages [16] -->
6.4 Sensitivity with respect to the number of search planes

<!-- b000327 | prose | pages [16] -->
As we changed the number of planes, we found an interesting result: decreasing the number of search planes by 2 planes increased the search time by 2 days, but adding 2 search planes only decreased the search length by 1 day. As such, it appears that the search time has an inverse exponential relation to the number of search planes.

<!-- b000328 | heading | pages [16] -->
6.5 Sensitivity with respect to the speed of the wind while searching

<!-- b000329 | prose | pages [16] -->
Because of the piecewise function our model has to use to calculate sweep width based on the wind speed at the time of the search, we had to make large changes to the wind speed in order to get a change. When we increased wind speed by 6 knots, it doubled the search time, and when we decreased by 6 knots it halved the search time. In real life, this is most likely a logistic relation, as the time will eventually cap regardless of wind speed, and will bottom out when wind speed gets below a certain level.

<!-- b000330 | heading | pages [16] -->
6.6 Sensitivity with respect to the visibility while searching

<!-- b000331 | prose | pages [16] -->
When we performed our sensitivity analysis on the visibility, we found that any visibility above our original 14.6 nautical miles had no e↵ect on the time it would take to search the area, but going down by 1 nautical mile increased the time it would take by 1 day. From this behavior, it appears that this is another inverse exponential relation.

<!-- b000332 | heading | pages [16] -->
7 Analysis of our Model

<!-- b000333 | heading | pages [16] -->
7.1 Strengths

<!-- b000334 | prose | pages [16] -->
Our model can calculate the possible “splash-down” area using only the altitude, speed, and last known coordinates of the plane, which is much less data than most searches typically require. Using those three parameters, the model is able to generate a more realistic search shape than just a circle or rectangle. It can also use real-life ocean current data to have the debris search area drift accordingly, allowing it to change shape and size. Other models might just have a static search area, and debris might drift out of that. A third strength of the model is that, regardless of the shape of the area, we are able to model and predict how long it will take to search that area suﬃciently to have a 95% chance of ﬁnding a piece of debris, if there is any debris to be found.

<!-- b000335 | heading | pages [16] -->
7.2 Weaknesses

<!-- b000336 | prose | pages [16, 17] -->
While our model is quite robust, it has a few important weaknesses. One of them is that, in order to run our search patterns, the model has to search a rectangle that bounds the search area, rather than only the area itself. This means that, depending on the orientation and shape of the actual search area, the search planes may spend excessive amounts of time searching outside where the debris could be. Another weakness at the moment is that the model can only calculate current drift in the vicinity of where ﬂight MH370 went down; we lack the data necessary to model ocean currents globally. Our model does not account for survivors ﬂoating on debris or in rafts moving the debris against the current and outside the search area as they head for land. Also, our model does not take into account the speed of the crashing plane when it loses power and begins to glide, so the actual search area might be larger than what we are currently estimating.

<!-- b000337 | furniture | pages [17] -->
Team # 36178

<!-- b000338 | furniture | pages [17] -->
Page 16 of 17

<!-- b000340 | heading | pages [17] -->
7.3 Future improvements

<!-- b000341 | prose | pages [17] -->
Due to the limited time available to us, there were some simpliﬁcations that we had to make to our model that we would like to expand upon, given more time. We would like to develop a way to incorporate local current data measured at the site of the last known point of contact and model the drift using that, rather than just a small section of data that we were able to ﬁnd for ﬂight MH370’s area. We would also like to expand upon our “splash-down” shape by accounting for more possible types of loss-of-contact other than just loss of power. A third area we would like to improve in the model is to incorporate other search methods and continue comparing them until we have a deﬁnitive “best” method, rather than the best of three that we chose. The fourth way we would like to improve the model is to continue writing and integrating the program so that each day’s search area is displayed with latitude and longitude coordinates at the corners for reference, and the search pattern the planes are to ﬂy is traced onto the map as well for convenient visualization.

<!-- b000342 | prose | pages [17] -->
We would also like to add a feature that allows you to put more speciﬁc data into the model and thus narrow the search parameters. For example, future versions of our model may allow the user to provide the distance that search planes must ﬂy to reach the search area as a parameter. It may also allow the user to provide the time since the crash occurred, eventually.

<!-- b000343 | heading | pages [17] -->
8 Conclusion

<!-- b000344 | prose | pages [17] -->
The model we have described in this paper is a robust and comprehensive model that can assist searchers throughout the search for a missing airplane. When the airplane goes down, our model can give a maximum bounding area of the plane’s location, carefully limited by the airplane’s turn radius. Every day, when given a search pattern and information about the search conditions, the model can predict the search area covered and report the probability that debris from the crash will be found. Each day, the model can precisely move the search area based on ocean current data, so searchers can know exactly where to focus their e↵orts, and once debris is found, the model can trace the debris back to the original location of the crash.

<!-- b000345 | prose | pages [17] -->
In addition, testing our model on di↵erent search methods revealed that there is no one perfect way to search for a missing plane. Depending on the weather, the area to search, and the number of planes available, di↵erent search algorithms may yield di↵erent results. But by testing these algorithms on a variety of scenarios, our model was able to generate recommended search methods for di↵erent search situations.

<!-- b000346 | prose | pages [17] -->
There is no one way to search for a missing airplane—there are simply too many unknowns, too many variables, too many things that can go wrong in di↵erent ways. But no matter the type of plane, the time it went down, or even the weather, we hope that our model could help searchers at every step of the way.

<!-- b000347 | furniture | pages [18] -->
Team # 36178

<!-- b000348 | furniture | pages [18] -->
Page 17 of 17

<!-- b000349 | heading | pages [18] -->
References

<!-- b000350 | references | pages [18] -->
[1] Australian Transport Safety Bureau. (2014). MH370 - Deﬁnition of underwater search areas. Canberra,

<!-- b000351 | references | pages [18] -->
ACT 2601: Australian Transport Safety Bureau.

<!-- b000352 | references | pages [18] -->
[2] National Search and Rescue Committee [NSARC]. (2000). United States National Search and Rescue

<!-- b000353 | references | pages [18] -->
Supplement to the International Aeronautical and Maritime Search and Rescue Manual. Washington,

<!-- b000354 | references | pages [18] -->
D.C.: U.S. Superintendent of Documents.

<!-- b000355 | references | pages [18] -->
[3] Potomac Management Group, Inc. (2006). A Simple Guide to Conducting Ground Search and Rescue

<!-- b000356 | references | pages [18] -->
Detection Experiments. Washington, D.C.: United States Coast Guard Oﬃce of Search and Rescue.

<!-- b000357 | references | pages [18] -->
[4] Steiner, Margaret F. Ditching behavior of military airplanes as a↵ected by ditching aids. UNT Digital

<!-- b000358 | references | pages [18] -->
Library. http://digital.library.unt.edu/ark:/67531/metadc61115/. Accessed February 6, 2015.

<!-- b000359 | references | pages [18] -->
[5] Sedgewick, R., & Wayne, K. (2011, August 6). Convex hull. Retrieved February 6, 2015, from

<!-- b000360 | references | pages [18] -->
http://algs4.cs.princeton.edu/99hull/

<!-- b000361 | references | pages [18] -->
[6] Long, L., & Weiss, H. (2006). How Terminal Is Terminal Velocity? The American Mathematical Monthly,

<!-- b000362 | references | pages [18] -->
(113), 752-755.

<!-- b000363 | references | pages [18] -->
[7] Carry-on Baggage. (n.d.). Retrieved February 7, 2015, from http://www.delta.com/content/www/en US/traveling-

<!-- b000364 | references | pages [18] -->
with-us/baggage/during-your-trip/carry-on.html

<!-- b000365 | references | pages [18] -->
[8] Aircraft

<!-- b000366 | references | pages [18] -->
Speciﬁcations.

<!-- b000367 | references | pages [18] -->
(n.d.).

<!-- b000368 | references | pages [18] -->
Retrieved

<!-- b000369 | references | pages [18] -->
February

<!-- b000370 | references | pages [18] -->
7,

<!-- b000371 | references | pages [18] -->
2015,

<!-- b000372 | references | pages [18] -->
from

<!-- b000373 | references | pages [18] -->
http://www.gateway-

<!-- b000374 | references | pages [18] -->
group.com/aircraft-speciﬁcations/

<!-- b000375 | references | pages [18] -->
[9] P-3

<!-- b000376 | references | pages [18] -->
Orion

<!-- b000377 | references | pages [18] -->
Speciﬁcations.

<!-- b000378 | references | pages [18] -->
(n.d.).

<!-- b000379 | references | pages [18] -->
Retrieved

<!-- b000380 | references | pages [18] -->
February

<!-- b000381 | references | pages [18] -->
8,

<!-- b000382 | references | pages [18] -->
2015,

<!-- b000383 | references | pages [18] -->
from

<!-- b000384 | references | pages [18] -->
http://www.lockheedmartin.com/us/products/p3/p-3-speciﬁcations.html

<!-- b000385 | references | pages [18] -->
[10] 737

<!-- b000386 | references | pages [18] -->
Airborne

<!-- b000387 | references | pages [18] -->
Early

<!-- b000388 | references | pages [18] -->
Warning

<!-- b000389 | references | pages [18] -->
and

<!-- b000390 | references | pages [18] -->
Control.

<!-- b000391 | references | pages [18] -->
(n.d.).

<!-- b000392 | references | pages [18] -->
Retrieved

<!-- b000393 | references | pages [18] -->
February

<!-- b000394 | references | pages [18] -->
8,

<!-- b000395 | references | pages [18] -->
2015,

<!-- b000396 | references | pages [18] -->
from

<!-- b000397 | references | pages [18] -->
http://www.boeing.com/assets/pdf/defense-space/ic/aewc/docs/737AEWC overview.pdf

<!-- b000398 | references | pages [18] -->
[11] Cessna 172. (n.d.). Retrieved February 6, 2015, from http://en.wikipedia.org/wiki/Cessna 172

<!-- b000399 | references | pages [18] -->
[12] Lockheed

<!-- b000400 | references | pages [18] -->
Martin

<!-- b000401 | references | pages [18] -->
F-22

<!-- b000402 | references | pages [18] -->
Raptor.

<!-- b000403 | references | pages [18] -->
(n.d.).

<!-- b000404 | references | pages [18] -->
Retrieved

<!-- b000405 | references | pages [18] -->
February

<!-- b000406 | references | pages [18] -->
6,

<!-- b000407 | references | pages [18] -->
2015,

<!-- b000408 | references | pages [18] -->
from

<!-- b000409 | references | pages [18] -->
http://en.wikipedia.org/wiki/Lockheed Martin F-22 Raptor

<!-- b000410 | references | pages [18] -->
[13] Bombardier

<!-- b000411 | references | pages [18] -->
Challenger

<!-- b000412 | references | pages [18] -->
300.

<!-- b000413 | references | pages [18] -->
(n.d.).

<!-- b000414 | references | pages [18] -->
Retrieved

<!-- b000415 | references | pages [18] -->
February

<!-- b000416 | references | pages [18] -->
6,

<!-- b000417 | references | pages [18] -->
2015,

<!-- b000418 | references | pages [18] -->
from

<!-- b000419 | references | pages [18] -->
http://en.wikipedia.org/wiki/Bombardier Challenger 300

<!-- b000420 | references | pages [18] -->
[14] The

<!-- b000421 | references | pages [18] -->
Boeing

<!-- b000422 | references | pages [18] -->
Next-Generation

<!-- b000423 | references | pages [18] -->
737

<!-- b000424 | references | pages [18] -->
family.

<!-- b000425 | references | pages [18] -->
(n.d.).

<!-- b000426 | references | pages [18] -->
Retrieved

<!-- b000427 | references | pages [18] -->
February

<!-- b000428 | references | pages [18] -->
6,

<!-- b000429 | references | pages [18] -->
2015,

<!-- b000430 | references | pages [18] -->
from

<!-- b000431 | references | pages [18] -->
http://www.boeing.com/boeing/commercial/737family/background.page

<!-- b000432 | references | pages [18] -->
[15] Boeing 737. (n.d.). Retrieved February 6, 2015, from http://en.wikipedia.org/wiki/Boeing 737

<!-- b000433 | references | pages [18] -->
[16] Boeing

<!-- b000434 | references | pages [18] -->
737-300.

<!-- b000435 | references | pages [18] -->
(n.d.).

<!-- b000436 | references | pages [18] -->
Retrieved

<!-- b000437 | references | pages [18] -->
February

<!-- b000438 | references | pages [18] -->
6,

<!-- b000439 | references | pages [18] -->
2015,

<!-- b000440 | references | pages [18] -->
from

<!-- b000441 | references | pages [18] -->
http://www.airliners.net/aircraft-

<!-- b000442 | references | pages [18] -->
data/stats.main?id=92

<!-- b000443 | references | pages [18] -->
[17] Lockheed

<!-- b000444 | references | pages [18] -->
C-5B

<!-- b000445 | references | pages [18] -->
Galaxy.

<!-- b000446 | references | pages [18] -->
(n.d.).

<!-- b000447 | references | pages [18] -->
Retrieved

<!-- b000448 | references | pages [18] -->
February

<!-- b000449 | references | pages [18] -->
6,

<!-- b000450 | references | pages [18] -->
2015,

<!-- b000451 | references | pages [18] -->
from

<!-- b000452 | references | pages [18] -->
http://en.wikipedia.org/wiki/Lockheed C-5 Galaxy

<!-- b000453 | references | pages [18] -->
[18] Airbus A330. (n.d.). Retrieved February 9, 2015, from http://en.wikipedia.org/wiki/Airbus A33

<!-- b000454 | references | pages [18] -->
[19] Forces of a Glider lab and lecture. (n.d.). Retrieved February 6, 2015, from http://www.t4t.org/wp-

<!-- b000455 | references | pages [18] -->
content/uploads/2013/08/FORCES-The Glider.docx

<!-- b000456 | references | pages [18] -->
[20] OSCAR Project Oﬃce. ”Data Download for Ocean Surface Currents.” Retrieved February 5, 2015, from

<!-- b000457 | references | pages [18] -->
www.oscar.noaa.gov/datadisplay/oscar datadownload.php.

<!-- b000458 | references | pages [18] -->
[21] Hafner,

<!-- b000459 | references | pages [18] -->
Izidor.

<!-- b000460 | references | pages [18] -->
”South

<!-- b000461 | references | pages [18] -->
Indian

<!-- b000462 | references | pages [18] -->
Ocean

<!-- b000463 | references | pages [18] -->
Currents,

<!-- b000464 | references | pages [18] -->
Flight

<!-- b000465 | references | pages [18] -->
MH370.”

<!-- b000466 | references | pages [18] -->
Demonstrations

<!-- b000467 | references | pages [18] -->
RSS.

<!-- b000468 | references | pages [18] -->
Wolfram,

<!-- b000469 | references | pages [18] -->
21

<!-- b000470 | references | pages [18] -->
Apr.

<!-- b000471 | references | pages [18] -->
2014.

<!-- b000472 | references | pages [18] -->
Web.

<!-- b000473 | references | pages [18] -->
05

<!-- b000474 | references | pages [18] -->
Feb.

<!-- b000475 | references | pages [18] -->
2015.

<!-- b000476 | references | pages [18] -->
¡http://www.demonstrations.wolfram.com/SouthIndianOceanCurrentsFlightMH370/¿.

<!-- b000477 | references | pages [19] -->
Addressing)the)Press)Regarding)the)Plan)for)

<!-- b000478 | references | pages [19] -->
Future)Searches)

<!-- b000479 | references | pages [19] -->
)

<!-- b000480 | references | pages [19] -->
Our new plan for searching for planes that are lost over large bodies of water can

<!-- b000481 | references | pages [19] -->
be summarized by three stages: finding an approximate location for the site of where the

<!-- b000482 | references | pages [19] -->
plane went down, searching this location for evidence of the location of the plane, and

<!-- b000483 | references | pages [19] -->
analyzing the findings to obtain a better approximation for the location of the plane. This

<!-- b000484 | references | pages [19] -->
process is repeated until the plane is found. These stages will now be explained in further

<!-- b000485 | references | pages [19] -->
detail.

<!-- b000486 | references | pages [19] -->
Upon receiving news that one of our planes has been lost over a large body of

<!-- b000487 | references | pages [19] -->
water, we will first gather information regarding the situation, such as the model of plane,

<!-- b000488 | references | pages [19] -->
the point of last contact, the time of last contact, the weather in the area, and the heading

<!-- b000489 | references | pages [19] -->
of the plane. We will then use this information to determine an area that the plane could

<!-- b000490 | references | pages [19] -->
have gone down in. This area is usually a circular shape.

<!-- b000491 | references | pages [19] -->
After determining the area that

<!-- b000492 | references | pages [19] -->
the plane could have gone down in,

<!-- b000493 | references | pages [19] -->
we will trace a rectangle around this

<!-- b000494 | references | pages [19] -->
area and search the rectangle with

<!-- b000495 | references | pages [19] -->
search planes. If few search planes are

<!-- b000496 | references | pages [19] -->
available, they will search in a

<!-- b000497 | references | pages [19] -->
straight-line pattern across the long

<!-- b000498 | references | pages [19] -->
side of the rectangle. If ten or more

<!-- b000499 | references | pages [19] -->
planes are available for the search,

<!-- b000500 | references | pages [19] -->
The$full$range$of$end$locations$that$the$plane$could$have$crashed$at$

<!-- b000501 | references | pages [20] -->
then the planes will fly diagonally across the rectangle to cover the area more efficiently.

<!-- b000502 | references | pages [20] -->
The planes will use visual techniques to spot evidence of the plane’s location, such as

<!-- b000503 | references | pages [20] -->
debris.

<!-- b000504 | references | pages [20] -->
The$different$search$patterns$

<!-- b000505 | references | pages [20] -->
Every time debris is found, we will use data of ocean currents of that location to

<!-- b000506 | references | pages [20] -->
determine where that debris originated. This will give us a better approximation of the

<!-- b000507 | references | pages [20] -->
location of the plane, and we will start again with the first stage and repeat this process

<!-- b000508 | references | pages [20] -->
until the plane has been found.

<!-- b000509 | references | pages [20] -->
(  		 
)

<!-- b000510 | references | pages [20] -->
A$vector$field$showing$how$ocean$currents$move$debris1$
