# P-B-2015-39173-b8260835

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team #39173

<!-- b000002 | furniture | pages [1] -->
Page 1 of 32

<!-- b000003 | title | pages [1] -->
Searching for a Lost Plane: A Probabilistic,

<!-- b000004 | title | pages [1] -->
Neighborhood-Based Model for Locating Transoceanic

<!-- b000005 | title | pages [1] -->
Flights

<!-- b000006 | heading | pages [1] -->
Abstract

<!-- b000007 | prose | pages [1] -->
This paper proposes a model which determines the most probable locations of a missing transoceanic ﬂight traveling from point A to point B. Since transoceanic ﬂights are not detected by radar when they are more than 200 miles from a coast, radio communication and the occasional satellite imagery is essential to the construction of an eﬀective search plan. Our search plan is built oﬀthe last distance in miles on the intended ﬂight path (IFP) where Air Traﬃc Control heard from the pilot. We create a quadratic distance to casualty probability density function to predict the distance from the point of last contact to where the plane likely fell. Through trajectories and the possibility of veering oﬀthe IFP, a two-dimensional search region is determined and discretized into smaller areas. The trajectories account for any aircraft model, as parameters such as cruising altitude and Glide Ratio are assessed. Probabilities of containment (POC) are then assigned to each of these search areas, determining the probability the lost plane is within the given region.

<!-- b000008 | prose | pages [1] -->
We next consider the probabilities of detection (POD) during the search. We apply Koopman’s equation for the probability of detecting a missing boat. Furthermore, Koopman’s equation provides ﬂexibility to input appropriate values pertaining to a given model of search plane and its instrumentation. Upon determining POD, we create an algo- rithm to eﬀectively search the bounded area. Our algorithm applies the POD to the POC’s and redistributes probabilities if the search plane is not found in a region while still considering the chance that the plane was actually in the region searched. If the plane is not found in a given cell, the algorithm outputs a neighboring region to search next. This customized neighborhood search plan maximizes resources while remaining time-eﬃcient. An example of missing Transatlantic Flight ABCD is included as a demonstration of our methodology.

<!-- b000009 | prose | pages [1] -->
Our mathematically-derived search plan is built on a series of as- sumptions. These assumptions include that the IFP from point A to point B is linear and that the plane disassembled only upon impact- ing the water. Our model is sensitive to speciﬁc parameter changes but is therefore accommodating to diﬀerent plane types. Strengths of the model include non-uniform probability distributions modeling dis- tance to casualty and impact and a neighborhood-based, continuously- updating search mechanism.

<!-- b000010 | prose | pages [1] -->
1

<!-- b000011 | furniture | pages [2] -->
Team #39173

<!-- b000012 | furniture | pages [2] -->
Page 2 of 32

<!-- b000013 | heading | pages [2] -->
Contents

<!-- b000014 | contents | pages [2] -->
1 Introduction

<!-- b000015 | contents | pages [2] -->
2

<!-- b000016 | contents | pages [2] -->
2 Model

<!-- b000017 | contents | pages [2] -->
3

<!-- b000018 | contents | pages [2] -->
2.1

<!-- b000019 | contents | pages [2] -->
Constructing Probabilities of Containment for a Miss-

<!-- b000020 | contents | pages [2] -->
ing Airplane and its Debris

<!-- b000021 | contents | pages [2] -->
. . . . . . . . . . . . . . .

<!-- b000022 | contents | pages [2] -->
3

<!-- b000023 | contents | pages [2] -->
2.1.1

<!-- b000024 | contents | pages [2] -->
Partitioning Search Region Through Model Dis-

<!-- b000025 | contents | pages [2] -->
cretization . . . . . . . . . . . . . . . . . . . . .

<!-- b000026 | contents | pages [2] -->
6

<!-- b000027 | contents | pages [2] -->
2.1.2

<!-- b000028 | contents | pages [2] -->
Finding Latitude and Longitude Coordinates for

<!-- b000029 | contents | pages [2] -->
Search Regions . . . . . . . . . . . . . . . . . .

<!-- b000030 | contents | pages [2] -->
8

<!-- b000031 | contents | pages [2] -->
2.2

<!-- b000032 | contents | pages [2] -->
Probability of Detection . . . . . . . . . . . . . . . . .

<!-- b000033 | contents | pages [2] -->
10

<!-- b000034 | contents | pages [2] -->
2.3

<!-- b000035 | contents | pages [2] -->
The POC-Updating Algorithm

<!-- b000036 | contents | pages [2] -->
. . . . . . . . . . . . .

<!-- b000037 | contents | pages [2] -->
11

<!-- b000038 | contents | pages [2] -->
2.3.1

<!-- b000039 | contents | pages [2] -->
Using the POC-Updating Algorithm to Deter-

<!-- b000040 | contents | pages [2] -->
mine Search Pattern . . . . . . . . . . . . . . .

<!-- b000041 | contents | pages [2] -->
11

<!-- b000042 | contents | pages [2] -->
2.4

<!-- b000043 | contents | pages [2] -->
Assumptions in the Methodology . . . . . . . . . . . .

<!-- b000044 | contents | pages [2] -->
12

<!-- b000045 | contents | pages [2] -->
2.5

<!-- b000046 | contents | pages [2] -->
Sensitivity Analysis . . . . . . . . . . . . . . . . . . . .

<!-- b000047 | contents | pages [2] -->
12

<!-- b000048 | contents | pages [2] -->
2.6

<!-- b000049 | contents | pages [2] -->
Strengths and Weaknesses of Our Model . . . . . . . .

<!-- b000050 | contents | pages [2] -->
15

<!-- b000051 | contents | pages [2] -->
2.6.1

<!-- b000052 | contents | pages [2] -->
Strengths . . . . . . . . . . . . . . . . . . . . .

<!-- b000053 | contents | pages [2] -->
15

<!-- b000054 | contents | pages [2] -->
2.6.2

<!-- b000055 | contents | pages [2] -->
Weaknesses . . . . . . . . . . . . . . . . . . . .

<!-- b000056 | contents | pages [2] -->
16

<!-- b000057 | contents | pages [2] -->
3 Working Example: Flight ABCD to Lisbon, Portugal

<!-- b000058 | contents | pages [2] -->
Reported Missing

<!-- b000059 | contents | pages [2] -->
16

<!-- b000060 | contents | pages [2] -->
4 Conclusion

<!-- b000061 | contents | pages [2] -->
23

<!-- b000062 | contents | pages [2] -->
5 Summary for an Airline’s Press Conference

<!-- b000063 | contents | pages [2] -->
23

<!-- b000064 | contents | pages [2] -->
6 Appendix A

<!-- b000065 | contents | pages [2] -->
25

<!-- b000066 | contents | pages [2] -->
7 Appendix B

<!-- b000067 | contents | pages [2] -->
26

<!-- b000068 | contents | pages [2] -->
8 Appendix C

<!-- b000069 | contents | pages [2] -->
27

<!-- b000070 | contents | pages [2] -->
9 Appendix D

<!-- b000071 | contents | pages [2] -->
30

<!-- b000072 | contents | pages [2] -->
1 Introduction

<!-- b000073 | contents | pages [2] -->
Since 1948, 83 aircrafts have vanished, some of which have still

<!-- b000074 | contents | pages [2] -->
not been found (Bloomberg). Lost transoceanic ﬂights are among the

<!-- b000075 | contents | pages [2] -->
hardest ﬂights to locate due to the lack of radar coverage. An average

<!-- b000076 | contents | pages [2] -->
radius for radar coverage is approximately 200 miles in any direction

<!-- b000077 | contents | pages [2] -->
(Hartmann). Because radar coverage is not an available method to

<!-- b000078 | contents | pages [2] -->
track a transoceanic ﬂight’s activity, Air Traﬃc Control (ATC) relies

<!-- b000079 | contents | pages [2] -->
2

<!-- b000080 | furniture | pages [3] -->
Team #39173

<!-- b000081 | furniture | pages [3] -->
Page 3 of 32

<!-- b000082 | contents | pages [3] -->
on radio or messaging communication with a pilot on a regular, pre-

<!-- b000083 | contents | pages [3] -->
determined basis. If there are no location updates in the designated

<!-- b000084 | contents | pages [3] -->
time frame, signals alert Air Traﬃc Control that there has been a loss

<!-- b000085 | contents | pages [3] -->
of communication, and that there is a potentially missing ﬂight.

<!-- b000086 | contents | pages [3] -->
In the past, Bayesian statistical methods have been used to track

<!-- b000087 | contents | pages [3] -->
the whereabouts of missing ﬂights. Air France Flight 447 went down in

<!-- b000088 | contents | pages [3] -->
2009 and was not found for over a year. Towards the end of the search,

<!-- b000089 | contents | pages [3] -->
statisticians used Bayesian methods, narrowed the search plane, and

<!-- b000090 | contents | pages [3] -->
picked up the blackbox’s radio transmitter signal, locating the plane

<!-- b000091 | contents | pages [3] -->
(Seidel). The available prior information, such as weather conditions

<!-- b000092 | contents | pages [3] -->
on the ﬂight path, ﬂoating bodies found soon-after, and the signal

<!-- b000093 | contents | pages [3] -->
of the beacon eliminated search zones. On the other hand Malaysian

<!-- b000094 | contents | pages [3] -->
Flight 370 contained little prior information, the search began later, no

<!-- b000095 | contents | pages [3] -->
ﬂoating remnants were found, and individuals presumed the blackbox

<!-- b000096 | contents | pages [3] -->
signal was turned oﬀ(Seidel). To this day, the location of ﬂight MH370

<!-- b000097 | contents | pages [3] -->
remains unclear.

<!-- b000098 | contents | pages [3] -->
In order to confront the diﬃcult situation in which a plane is lost

<!-- b000099 | contents | pages [3] -->
and prior information is scarce, we set out to create a mathematical

<!-- b000100 | contents | pages [3] -->
model and search plan. Our model accounts for an indeﬁnite time

<!-- b000101 | contents | pages [3] -->
until casualty and impact with the water.

<!-- b000102 | contents | pages [3] -->
Potential deviations oﬀ

<!-- b000103 | contents | pages [3] -->
the intended ﬂight path, relevant to the Malaysian Flight, are also

<!-- b000104 | contents | pages [3] -->
considered and time-eﬃciency is prioritized. We propose an eﬀective

<!-- b000105 | contents | pages [3] -->
search strategy in the case of a lost, signal-less transoceanic ﬂight.

<!-- b000106 | heading | pages [3] -->
2 Model

<!-- b000107 | prose | pages [3] -->
Our model considers a lost ﬂight, which starts at some location A and sets out to travel across the ocean linearly to its destination B. In order to develop an optimized search plan, we consider the proba- bilities of containment of the plane’s whereabouts, the probabilities of detecting the plane while eﬃciently and conservatively using resources, and the continuously updating probabilities of the most likely location of the missing airplane.

<!-- b000108 | heading | pages [3] -->
2.1 Constructing Probabilities of Containment

<!-- b000109 | prose | pages [3] -->
for a Missing Airplane and its Debris

<!-- b000110 | prose | pages [3] -->
The containment model maps the probability of the airplane’s con- tainment to speciﬁc regions surrounding the ﬂight’s last known posi- tion. Our ﬁrst consideration in the containment model is estimating how far the plane most likely travels after a signal is lost. The vari- able y0 is the last distance in miles from the starting location where

<!-- b000111 | prose | pages [3, 4] -->
3 air traﬃc controllers heard from the pilot. In addition to the mileage covered, it is important to take note of the initial latitude and lon- gitude coordinates at y0. It is assumed that the plane stayed on its Intended Flight Path (IFP) at this time. At this location, it is un- clear if the plane continued traveling in the air or began falling to the ground. The Random Variable Yc refers to the distance to casualty, or the distance on the IFP at which the plane started to malfunction. It is assumed that when a plane malfunctions, its descent for the water begins. The distance to casualty is measured from y0 = 0. We have modeled the probability density function of Yc as follows:

<!-- b000112 | furniture | pages [4] -->
Team #39173

<!-- b000113 | furniture | pages [4] -->
Page 4 of 32

<!-- b000115 | prose | pages [4] -->
( 3 (yB−yR)3 (yC −(yB −yR))2 : y0 ≤yC < yB −yR fyc(yc) = 0 : elsewhere

<!-- b000116 | prose | pages [4] -->
where yB indicates the remaining distance to destination B from y0 and yR is the ﬁnal mileage of the journey for which radar detection is available. Therefore, yB −yR represents the ﬂying distance left before Air-Traﬃc Control (ATC) radar detectors can spot the missing ﬂight.

<!-- b000117 | prose | pages [4] -->
Our Random Variable Yc is constructed under the assumption that it is more likely for the plane to reach a casualty-state immediately or soon after the last communication with ATC. This intuition is reason- able because a loss of communication often occurs due to abnormal plane operation. The probability continues to decrease quadratically and becomes 0 in the radar-detective zone. The parameter yR can be determined using the equation below:

<!-- b000118 | prose | pages [4] -->
(200)2 −h2 = p p 40, 000 −h2 yR =

<!-- b000119 | prose | pages [4] -->
where h is the cruising altitude in miles of the jet. Radar detectors can track planes within a 200 mile radius, on average (Hartmann), so yR can be determined by manipulating the Pythagorean Theorem.

<!-- b000120 | prose | pages [4] -->
We determine the possible locations where the airplane could have fallen based on a distribution of trajectories. The distance of impact, or the distance from y0 at which the airplane hit the water is YI. This variable takes into account the glide of the airplane and the distance at which it is completely submerged and is modeled as follows:

<!-- b000121 | prose | pages [4] -->
YI = YC + Gh where G is the glide ratio of the plane (NASA). Each airplane model has an average glide ratio which is deﬁned as

<!-- b000122 | prose | pages [4] -->
G = units of distance forward unit of distance downward. The glide ratio is multiplied by the cruising altitude to determine the horizontal distance the plane traveled during its downward fall

<!-- b000123 | prose | pages [4, 5] -->
4 (NASA). The probability density function of YI can therefore be mod- eled using the following transformation of variables technique:

<!-- b000124 | furniture | pages [5] -->
Team #39173

<!-- b000125 | furniture | pages [5] -->
Page 5 of 32

<!-- b000127 | prose | pages [5] -->
P(YI < yI) = P(YC + Gh < yI) P(YC < yI −Gh) = Z yI−Gh 3 (yC −(yB −yR))2dyC = (yB −yR)3 0 3 yI−Gh (yB −yR)3 [(yC −(yB −yR))2dyC] = 0 3 (yB −yR)3 ([(yI −Gh −yB + yR)2][(0 −yB + yR)2] =

<!-- b000128 | prose | pages [5] -->
fyI(yI) = d 3 (yB −yR)3 ([(yI −Gh −yB + yR)2][(0 −yB + yR)2] =⇒ dyI

<!-- b000129 | prose | pages [5] -->
After taking the derivative with respect to YI we can conclude that the probability density function for YI is:

<!-- b000130 | prose | pages [5] -->
( 3 (yB−yR)3 (yI −Gh −(yB −yR))2 : Gh ≤yI < yB −yR fyI(yI) = 0 : elsewhere

<!-- b000131 | prose | pages [5] -->
The probable distances from the point of lost contact to the point of impact are measured in line with the IFP. While this model has accounted for a single dimension, we can easily extend it to the left and to the right, indicating a plane’s maneuver oﬀcourse. The next portion of our model accounts for the possibility of veering oﬀthe intended linear path.

<!-- b000132 | prose | pages [5] -->
Veering away from the IFP is considered by assuming the segment of water representing the locations of impact are the average, or 0, and that the possible locations of the plane are normally distributed to the sides of yI.

<!-- b000133 | prose | pages [5, 6] -->
5 IFP where a plane gliding π 8 oﬀcourse would land.

<!-- b000134 | furniture | pages [6] -->
Team #39173

<!-- b000135 | furniture | pages [6] -->
Page 6 of 32

<!-- b000136 | caption | pages [6] -->
Figure 1: One standard deviation is calculated to be the distance from the

<!-- b000138 | prose | pages [6] -->
Standard deviation of the normal probability distribution is deter- mined by σx = Gh sin (π 8 ) Since it is unlikely that a plane veers beyond π 8 from the IFP, π 8 will be used to ﬁnd one standard deviation. Thus the normal probability distribution perpendicular to the IFP is:

<!-- b000139 | prose | pages [6] -->
−x2 2(Gh sin( π 8 ))2 e √ 2π : −∞< x < ∞ f(x) = Gh sin(π 8 )

<!-- b000140 | prose | pages [6] -->
Because f(x) and f(yI) are independent distributions, we can cre- ate a joint probability density function by multiplying f(x) and f(yI) as follows: f(x, yI) = f(x)f(yI).

<!-- b000141 | prose | pages [6] -->
−x2  3(yI−Gh−(yB−yR))2 2(Ghsin( π 8 ))2 : −∞< x < ∞, Gh ≤yI < yB −yR 2π(yB−yR)3 e  √ f(x, yI) = Gh sin π 8 0 : elsewhere 

<!-- b000142 | heading | pages [6] -->
2.1.1 Partitioning Search Region Through Model Dis-

<!-- b000143 | prose | pages [6] -->
cretization

<!-- b000144 | prose | pages [6] -->
Given f(x, yI), the search ﬁeld can be divided into distinct regions.

<!-- b000145 | prose | pages [6] -->
Each region is assigned a probability of containment (POC), indicating the probability that the region contains the missing plane and debris.

<!-- b000146 | prose | pages [6, 7] -->
6 In order to discretize our model, we ﬁrst consider X, the normal ran- dom variable. Since 99.7% of all observations are contained within 3 standard deviations of the mean, our search region is bounded on both sides by three standard deviations. We segment yI over its entire range. Therefore, we consider N −1 partitions and N vertical regions through the following equation:

<!-- b000147 | furniture | pages [7] -->
Team #39173

<!-- b000148 | furniture | pages [7] -->
Page 7 of 32

<!-- b000150 | prose | pages [7] -->
lyB −yR −Gh m N = t0.5vs where t0.5 represents the quantity 0.5 hours and vs is the velocity of the search plane.This guarantees that each search plane spends up to half an hour sweeping a length of each search region. Assuming more than one plane searches a given region at a time, these partitions lead to a highly eﬃcient search duration.

<!-- b000151 | caption | pages [7] -->
Figure 2: The discretization method is modeled by the above SAN×6 search

<!-- b000152 | prose | pages [7] -->
region matrix. Note that in this case N = 4.

<!-- b000153 | prose | pages [7] -->
To ﬁnd the probabilities of containment for each of the above rect- angular regions, the joint probability density function f(x, yI) must be integrated over each region’s boundaries. In order to ﬁnd N × 6 prob- ability values, a loop was created in Mathematica. The loop considers only the regions to the right of the IFP, since the normal distribu- tion has the property of symmetry. The loop iterates through all N partitions in YI given each of the 3 set X regions. Below is the algo- rithm for the probability generation of each region within 1 standard deviation of the IFP:

<!-- b000154 | prose | pages [7, 8] -->
7 Z Gh sin( π Z 1( YB−YR−Gh 8 ) )+Gh N f(x, yI)dxdyI 0( YB−YR−Gh 0 )+Gh N

<!-- b000155 | furniture | pages [8] -->
Team #39173

<!-- b000156 | furniture | pages [8] -->
Page 8 of 32

<!-- b000158 | prose | pages [8] -->
Z Gh sin( π Z 2( YB−YR−Gh 8 ) )+Gh N f(x, yI)dxdyI 1( YB−YR−Gh 0 )+Gh N

<!-- b000159 | prose | pages [8] -->
...

<!-- b000160 | prose | pages [8] -->
Z Gh sin( π Z N( YB−YR−Gh 8 ) )+Gh N f(x, yI)dxdyI (N−1)( YB−YR−Gh 0 )+Gh N The output of this loop is a list of probability values that can be matched to each of the search regions. Refer to Appendix B for the Mathematica Code. Now that we have determined probabilities of containment for each of these ocean search regions, we must obtain the boundaries of each region in latitude and longitude coordinates to facilitate the search and rescue team’s eﬀorts.

<!-- b000161 | heading | pages [8] -->
2.1.2 Finding Latitude and Longitude Coordinates for

<!-- b000162 | prose | pages [8] -->
Search Regions

<!-- b000163 | prose | pages [8] -->
Initially, the bounds of a given uniform probability region ru×l can be represented as 0 ≤u ≤N and −3 ≤l ≤3 where l, u are integer multiples of n = region number along the IFP, σx respectively.

<!-- b000164 | caption | pages [8] -->
Figure 3: The location of a given ru×l = (l, u) in reference to an IFP and σx

<!-- b000165 | prose | pages [8] -->
In order to reference a discretized probability region to the IFP and y0, we must deﬁne a coordinate axis with a y-axis along the IFP,

<!-- b000166 | prose | pages [8, 9] -->
8 an x-axis in the direction of σx and an origin at (yI, 0σx). Now the bounds of a region ru×l in miles are:

<!-- b000167 | furniture | pages [9] -->
Team #39173

<!-- b000168 | furniture | pages [9] -->
Page 9 of 32

<!-- b000170 | prose | pages [9] -->
−l(Gh sin (π 8 )) ≤x ≤l(Gh sin (π 8 ))

<!-- b000171 | prose | pages [9] -->
and 0 ≤y ≤u(||yB −y0|| −Gh) . N To translate any given number m of zone-bounding coordinates in (x,y) to latitude and longitude, build a 2 × m matrix

<!-- b000172 | prose | pages [9] -->
C = [c1c2c3...cm]

<!-- b000173 | prose | pages [9] -->
where each bounding coordinate ci where 0 < i ≤m is of the form

<!-- b000174 | prose | pages [9] -->
cx  . cy

<!-- b000175 | prose | pages [9] -->
Next, using a rotation matrix, vector addition and vector scaling will eﬀectively shift an “IFP-referenced” coordinate to latitude and longi- tude. y0 and yB are known in the “IFP-referenced” system and in traditional coordinates. The components of yB −y0 in latitude and longitude are designated re, rn. To build a rotation matrix from the “IFP-referenced” system to latitude and longitude, we ﬁrst must ﬁnd the counter-clockwise angle φ between the two coordinate systems as follows: φ = arctan ( re ). rn Using φ, the rotation matrix R is either:

<!-- b000176 | prose | pages [9] -->
 cos φ  : π sin φ 2 ≤φ < 0 R = −sin φ cos φ

<!-- b000177 | prose | pages [9] -->
or cos φ  : 0 ≤φ ≤π −sin φ R = 2 . sin φ cos φ

<!-- b000178 | prose | pages [9] -->
One way to test whether the rotation matrix is calculated correctly is to verify that det(R) = 1. After ﬁnding a suitable R, multiply C by R to express every c in C in miles of latitude and longitude with reference to y0ρ where ρ is the average distance in miles of one degree North and one degree East from y0. Finally, add the resulting vector to y0 to have coordinates in degrees North and East. In summary, changing C in the “IFP-referenced” system to the corresponding coordinate matrix CL in latitude and longitude amounts to:

<!-- b000179 | prose | pages [9] -->
CL = ρRC + y0.

<!-- b000180 | prose | pages [9] -->
9

<!-- b000181 | furniture | pages [10] -->
Team #39173

<!-- b000182 | furniture | pages [10] -->
Page 10 of 32

<!-- b000183 | heading | pages [10] -->
2.2 Probability of Detection

<!-- b000184 | prose | pages [10] -->
A standard model for ﬁnding the Probability of Detection (POD) is the exponential function

<!-- b000185 | prose | pages [10] -->
POD = 1 −e−coverage

<!-- b000186 | prose | pages [10] -->
where coverage is the area eﬀectively swept divided by the entire search area AS (Frost 1999). To determine our region’s POD, we use a slight variation of B.O. Koopman’s Exponential Model. The search area is deﬁned as 8 )(yB −yR −Gh AS = Gh sin(π ). N where the AS represents the area of a single partitioned region of the overall search region.The area eﬀectively swept is dependent on the eﬀective sweep width S and the eﬀort. The eﬀective sweep width depends on the eﬀective detection distance κϵ of the instrument (eg. human eyes, radar, etc.) used for the search, and the elevation of the cruising search plane is hs. We modify Koopman’s model to account for variations in weather, conditions, search abilities and more. This variation is denoted by the scalar κ, which takes values between 0 and 1. The distance from the search plane’s path projected on the ocean (κϵ)2 −h2s. Assuming the p to the furthest possible detected object is search plane ﬂies in parallel swaths, the eﬀective sweep width would be (κϵ)2 −h2s p S = 2

<!-- b000187 | prose | pages [10] -->
in order to detect all of AS. The eﬀort is said to be dsn where the distance searched by an individual aircraft per swath is ds and the number of search planes included in the search is n. Assuming the search plane ﬂies parallel to the IFP, the number of swaths the plane must ﬂy is the number of subregions N so ds is

<!-- b000188 | prose | pages [10] -->
ds = (yb −yr −Gh ). N

<!-- b000189 | prose | pages [10] -->
In order to search simultaneously and most eﬃciently, the planes are assumed to be ﬂying at the same velocity. Thus ds is the same for each plane since they begin searching simultaneously. Incorporating each of these components into a single model yields the following POD equation: dsn√ (κϵ)2−h2s −2 (yB−yR−Gh) Gh sin π POD = 1 −e 8 N

<!-- b000190 | prose | pages [10] -->
Unless search eﬀort is changed based on the search region, it is assumed that the POD is uniform among all regions of probable con- tainment.

<!-- b000191 | prose | pages [10] -->
10

<!-- b000192 | furniture | pages [11] -->
Team #39173

<!-- b000193 | furniture | pages [11] -->
Page 11 of 32

<!-- b000194 | heading | pages [11] -->
2.3 The POC-Updating Algorithm

<!-- b000195 | prose | pages [11] -->
If there were no such thing as instrumentation error or human er- ror, POD would equal 1 and thus not adjust the POC’s of discretized zones. Since search conditions are nowhere near perfect, we assign 1 −PODq to be the probability that the lost plane in region q went undetected. Given that we do not ﬁnd the plane after searching the zone q, we update the POC in q to be

<!-- b000196 | prose | pages [11] -->
POCq′ = (POCq)(1 −PODq).

<!-- b000197 | prose | pages [11] -->
This is the probability that the plane is actually in the searched re- gion, even though it was not detected. Assuming that net probability of containment of all discretized zones is constant, the probability lost when POCq becomes POCq′ must be accounted for in the other regions. To do this, we add POCq −POCq′ 6N −1 to each of the POC values except POCq′. This process can be iterated during a search to update all the POC values per searched discrete probability zone.

<!-- b000198 | heading | pages [11] -->
2.3.1 Using the POC-Updating Algorithm to Determine

<!-- b000199 | prose | pages [11] -->
Search Pattern

<!-- b000200 | prose | pages [11] -->
To determine the best order to search the 6×N diﬀerent regions, we use the POC-updating algorithm described above using gradients to choose the next search region. By the ”best” order we mean the most eﬃcient in terms of resources and time. We want to spend the least amount of time and fuel covering the entire map. Thus we want to minimize ﬂight between nonadjacent regions because that increases less-useful or redundant coverage and increases time needed to cover the entire area. The search plan algorithm involves updating the POC map after completing the search of one region to ﬁnd the new proba- bility of containment map, given the downed aircraft was not detected in the recently-searched region. Using a matrix in Mathematica we represent the map of POC’s. A loop was created in Mathematica to evaluate, for each iteration, the diﬀerences between the updated POC’s of the just-searched region k and its adjacent neighbors. We take the minimum of the diﬀerences, and then locate the row nnew and column σnew of that minimum element, to ﬁnd the next region rnnew,σnew to be searched. Essentially this method consists of up- dating the POC matrix, calculating a gradient/diﬀerence to identify the highest adjacent POC, and taking that region as the next to be searched.

<!-- b000201 | prose | pages [11] -->
11

<!-- b000202 | furniture | pages [12] -->
Team #39173

<!-- b000203 | furniture | pages [12] -->
Page 12 of 32

<!-- b000204 | heading | pages [12] -->
2.4 Assumptions in the Methodology

<!-- b000205 | prose | pages [12] -->
There are several assumptions upon which our model and the re- sulting search plan are built. Below is a list of assumptions we con- sider:

<!-- b000206 | prose | pages [12] -->
• The lost plane’s pre-established course is a linear path from point A to point B.

<!-- b000207 | prose | pages [12] -->
• The lost plane’s glide aﬀects its trajectory into the ocean. The plane does not explode in the sky.

<!-- b000208 | prose | pages [12] -->
• Any debris disassembles upon impacting the water.

<!-- b000209 | prose | pages [12] -->
• The plane will not veer more than 3Ghsin(π 8 ) oﬀthe IFP.

<!-- b000210 | prose | pages [12] -->
• There are no forces (eg. currents) to move the debris or plane from where they ﬁrst landed.

<!-- b000211 | prose | pages [12] -->
• All planes (lost plane and search plane(s)) in the model are ﬂying at a constant velocity.

<!-- b000212 | prose | pages [12] -->
• The lost plane is more likely to be found near the last point of communication.

<!-- b000213 | prose | pages [12] -->
• The lost plane remains aﬂoat (detectable) during the entire time the search is in action.

<!-- b000214 | prose | pages [12] -->
• Every searching plane has the same instrumentation, searches at the same speed and ﬂies at the same altitude.

<!-- b000215 | heading | pages [12] -->
2.5 Sensitivity Analysis

<!-- b000216 | prose | pages [12] -->
In order to test how changing parameters eﬀect our model, we include a discussion of the relationships between speciﬁc parameters and their eﬀects on the components of our model and search plan.

<!-- b000217 | prose | pages [12] -->
We assess the impacts of changing parameters on f(x, yI) by con- sidering f(G) and f(θ). From experimentation with ﬁxing the random variables x and yI, the shape of the curve of f(G), and f(θ) are strik- ingly similar.

<!-- b000218 | prose | pages [12, 13] -->
12 and f(θ) regardless of the x and yI values

<!-- b000219 | furniture | pages [13] -->
Team #39173

<!-- b000220 | furniture | pages [13] -->
Page 13 of 32

<!-- b000221 | caption | pages [13] -->
Figure 4: f(G) where (x, yI) = (0.5, 0.5) exempliﬁes the curvature of f(G)

<!-- b000223 | prose | pages [13] -->
As G and θ increase, the respective f(G) and f(θ) exhibit a rapid decrease. Since the bounded integral of f(x, y) produces a POC, G and θ have the same eﬀect on POC as they do on f(x, y). In short, as G + θ decreases, the probability of ﬁnding the lost plane increases.

<!-- b000224 | prose | pages [13] -->
Increasing θ will directly increase the search area because the X distance is measured in mile-multiples of σx = Gh sin (θ) which is pro- portional to a chosen 0 ≤θ ≤π 2 . The following graphs are generated using the constant parameter values found in the Working Example (Section 3).

<!-- b000225 | caption | pages [13] -->
Figure 5: POD(θ) where θ is in radians

<!-- b000226 | prose | pages [13] -->
As θ increases, POD rapidly decreases from one to zero. The most intriguing part of POD(θ) is that the graph suggests POD(0) ≈1.

<!-- b000227 | prose | pages [13] -->
Also, the POD is extremely small for any plane that has veered more than ninety degrees oﬀthe IFP.

<!-- b000228 | prose | pages [13] -->
Increasing the glide ratio eﬀects the POD similarly to increasing θ.

<!-- b000229 | prose | pages [13, 14] -->
13 Increasing the exponent’s denominator will have an inverse eﬀect on the POD. Thus, a search party following the methodology explained in the Working Example will be more likely to ﬁnd a plane with a small glide ratio.

<!-- b000230 | furniture | pages [14] -->
Team #39173

<!-- b000231 | furniture | pages [14] -->
Page 14 of 32

<!-- b000232 | caption | pages [14] -->
Figure 6: POD(G)

<!-- b000234 | prose | pages [14] -->
Another variable that clearly eﬀects the search plan is the cruising altitude, hS, at which the search plane ﬂies because the POD depends κϵ2 −h2s. Varying hs within 0 ≤hs < ϵ produces an elliptic p on graph of POD centered around the origin:

<!-- b000235 | caption | pages [14] -->
Figure 7: POD(hs) where 0 ≤hs < ϵ

<!-- b000236 | caption | pages [14] -->
Figure 4 illustrates that when hs

<!-- b000237 | prose | pages [14] -->
increases, the POD increases. ϵ This is a logical relationship because each swath will cover more ground which will in turn decrease the search eﬀort. Thus, it is best to run the search at the lowest possible altitude in order to improve the chance of ﬁnding the lost plane.

<!-- b000238 | prose | pages [14] -->
The number of search planes n also eﬀect the POD because the search eﬀort n is in the numerator of the search eﬀort fraction. Illus- trated graphically:

<!-- b000239 | prose | pages [14, 15] -->
14 In a practical sense, incorporating more search planes will increase the likelihood of detection.

<!-- b000240 | furniture | pages [15] -->
Team #39173

<!-- b000241 | furniture | pages [15] -->
Page 15 of 32

<!-- b000242 | caption | pages [15] -->
Figure 8: POD(hs) where n ∈N

<!-- b000244 | prose | pages [15] -->
(κϵ)2 −h2s there p Since the POD equation contains the element may be a square root of a negative number if h2 s > (κϵ)2. A plane must ﬂy low enough for the eﬀective range of the instrumentation (κϵ) to reach the ground. Otherwise there is no chance the plane will detect anything below it and thus the POD would be eﬀectively zero.

<!-- b000245 | prose | pages [15] -->
s > (κϵ)2 there is no point in searching until conditions Thus when h2 improve.

<!-- b000246 | prose | pages [15] -->
Clearly, our model is sensitive to changes in several of the parame- ters and therefore may not be considered a robust probabilistic model. However, the sensitivity to changes in the input parameters is neces- sary to have a model that is accommodating to the speciﬁcations of diﬀerent types of planes and search instruments.

<!-- b000247 | heading | pages [15] -->
2.6 Strengths and Weaknesses of Our Model

<!-- b000248 | heading | pages [15] -->
2.6.1 Strengths

<!-- b000249 | prose | pages [15] -->
Our outlined model has particular strengths, unavailable in other Search and Rescue methods. First, we use a quadratic probability density function rather than the commonly-used uniform distribution. In many Search and Rescue Methodologies, it is assumed that the time of casualty is uniformly distributed over all possible times in a given range (Lawrence 1977). Here, we carefully construct a decreasing, concave down distribution to account for the large likelihood that complications arise early after y0. Our model also accounts for a ﬂight trajectory to map the ﬂight’s motion at the time of casualty to a region of the ocean surface. The change of bases allows the searchers to locate the search regions using actual latitude, longitude coordinates rather than tracking angles and distances from the point of lost contact. The POD incorporates several factors, including an added constant k.

<!-- b000250 | prose | pages [15, 16] -->
15 When k = 1, the search occurs in perfect conditions, while k = 0.5 may indicate some fog, choppy water, or other inhibiting factors. This constant helps to better explain the rate of coverage while still using Koopman’s commonly-used Exponential Model.

<!-- b000251 | furniture | pages [16] -->
Team #39173

<!-- b000252 | furniture | pages [16] -->
Page 16 of 32

<!-- b000254 | prose | pages [16] -->
Our search plan is a constantly updating algorithm keeping time eﬃciency in mind. If an item is not detected in a highly probable re- gion, the POC’s of the other search regions are updated. The cell with the next highest probability in the searched region’s “neighborhood” is investigated. Implementing a neighborhood restriction speeds up the search process, wasting no travel time while still searching regions with high POC’s. Our search plan can easily be generalized to search planes of diﬀerent speeds and larger or smaller regions of the ocean.

<!-- b000255 | heading | pages [16] -->
2.6.2 Weaknesses

<!-- b000256 | prose | pages [16] -->
It is important to consider the weaknesses of our model that may be worth addressing in the future. First, the POC of the regions closest to Gh but more than 1 standard deviation away in the X direction are slightly over-allocated. The standard deviation was calculated using trigonometry, indicating that our rectangular probability region is based on a triangular calculation. Refer to Figure 1. Because of this over-allocation, there is a slight under-calculation of probabilities 1 or more standard deviations away from the IFP towards the latter partitions of YI.

<!-- b000257 | prose | pages [16] -->
Another weakness to consider is the lack of consideration of cur- rents in each of our partitioned search regions. With more time, we hope to extend the impacts of surface currents to locating debris and other remnants of the aircraft.

<!-- b000258 | heading | pages [16] -->
3 Working Example: Flight ABCD to

<!-- b000259 | prose | pages [16] -->
Lisbon, Portugal Reported Missing

<!-- b000260 | prose | pages [16, 17] -->
16 Imagine that on February 9, 2015 Flight ABCD from Boston, MA to Lisbon Portugal disappeared on a Boeing 777 aircraft. The point of last communication occurred at coordinates 40.9275◦N, 46.2575◦ W. Let yB = 1, 912 miles. The plane was cruising at a speed of 560 miles per hour at an altitude of 40, 000 feet (7.58 miles), so yR = 199.86. Assume that the ﬂight is entirely over open ocean and the Lisbon airport is the nearest location to y0 that can detect an airplane. So, yR is measured from the Lisbon airport along the IFP. Below is the probability distribution of YC, the random variable representing the probability that at a given distance in the direction of the IFP the plane experiences a casualty that causes it to begin a downward trajectory.

<!-- b000261 | furniture | pages [17] -->
Team #39173

<!-- b000262 | furniture | pages [17] -->
Page 17 of 32

<!-- b000264 | prose | pages [17] -->
( 3 (1912−199.86)3 (yC −(1912 −199.86))2 : 0 ≤yC < 1712.14 fyc(yc) = 0 : elsewhere

<!-- b000265 | prose | pages [17] -->
This airplane has a glide ratio of approximately 19 : 1, similar to other large aircrafts. With this information, yI can be modeled as follows:

<!-- b000266 | prose | pages [17] -->
( 3 (1712.14)3 (yI −1568.12)2 : 144.02 ≤yI < 1712.14 fyI(yI) = 0 : elsewhere

<!-- b000267 | prose | pages [17] -->
After considering the distribution of distances of impact, we must now account for the possibility of veering oﬀthe IFP. The following X distribution, distributed in the direction perpendicular to the intended ﬂight path, accounts for Flight ABCD’s potential oﬀ-course location of impact:

<!-- b000268 | prose | pages [17] -->
−x2 2(144.02 sin( π 8 ))2 e √ 2π : −∞< x < ∞ f(x) = 144.02 sin(π 8 )

<!-- b000269 | prose | pages [17, 18] -->
17 By multiplying the independent equations f(x) ∗f(yI), a joint probability density function is obtained.

<!-- b000270 | furniture | pages [18] -->
Team #39173

<!-- b000271 | furniture | pages [18] -->
Page 18 of 32

<!-- b000273 | prose | pages [18] -->
−x2  3(yI−1568.12)2 2(144.02 sin( π 8 ))2 : −∞< x < ∞, 144.02 ≤yI < 1712.14 2π(1712.14)3 e  √ f(x, yI) = 144.02 sin( π 8 ) 0 : elsewhere 

<!-- b000274 | caption | pages [18] -->
Figure 9: The joint density function is shown above, indicating the locations

<!-- b000275 | prose | pages [18] -->
in which the POC is largest, and locations where the POC is smallest

<!-- b000276 | prose | pages [18] -->
Now, the multi-dimensional probability distribution, POC, can be discretized into 36 subregion each calculated by a double integral, as described in section 2.1.1 Partitioning Search Regions Through Model Discretization.

<!-- b000277 | prose | pages [18, 19] -->
18 Next, the Probability of Detection is found by the formula as de- scribed in the section 2.2:

<!-- b000278 | furniture | pages [19] -->
Team #39173

<!-- b000279 | furniture | pages [19] -->
Page 19 of 32

<!-- b000280 | caption | pages [19] -->
Figure 10: The graph above represents the discretized POC of Flight ABCD

<!-- b000281 | caption | pages [19] -->
Figure 11: Map representation of POC allocated to each of the search regions

<!-- b000283 | prose | pages [19] -->
2∗dsn√ (kϵ)2−h2s − Gh sin π POD = 1 −e 8 (yB−yR−Gh)/N

<!-- b000284 | prose | pages [19] -->
The list of parameters for this model, either estimated or researched values, is as follows:

<!-- b000285 | prose | pages [19] -->
• Remaining distance of ﬂight from y0 to yR, yB = 1912

<!-- b000286 | prose | pages [19] -->
• Glide constant for a large plane such as a a Boeing 777-200, G = 19

<!-- b000287 | prose | pages [19, 20] -->
19 • Average altitude at which a commercial airliner cruises, h = 7.58 √ 2002 −h2

<!-- b000288 | furniture | pages [20] -->
Team #39173

<!-- b000289 | furniture | pages [20] -->
Page 20 of 32

<!-- b000291 | prose | pages [20] -->
• yR =

<!-- b000292 | prose | pages [20] -->
• Velocity of the search planes (all of which are the same model in order to facilitate easier coordination and timing in the search), vs = 550

<!-- b000293 | prose | pages [20] -->
• t.05 = .5 hours l m yB−yR−Gh

<!-- b000294 | prose | pages [20] -->
• The number of partitions in the y direction, N = t.05vs

<!-- b000295 | prose | pages [20] -->
• Distance traveled by search planes in searching a single region, ds = (yB−yR−Gh) np

<!-- b000296 | prose | pages [20] -->
• Detection distance of instrument, ϵ = 4

<!-- b000297 | prose | pages [20] -->
• Scales detection distance based on search conditions such as weather, κ = 0.98, note < 0κ < 1. In this case, κ is near one, indicating clear calm search conditions.

<!-- b000298 | prose | pages [20] -->
• Number of search planes n, chosen in this example to be 8.

<!-- b000299 | prose | pages [20] -->
• Then, POD = 0.677831 for our example, when we plug in all the variables

<!-- b000300 | prose | pages [20] -->
Taking the values in Figure 11, we input them to Mathematica to form the initial POC matrix. We then utilize the method described in section 2.3 and subsection 2.3.1, and the Mathematica code in Ap- pendix C, to determine the order and path of the most eﬃcient search pattern. We also utilize the model to update probabilities that certain regions contain the lost plane given the plane was not detected when the an area was most recently searched.

<!-- b000301 | prose | pages [20, 21] -->
20 gorithm and described by the output of the Mathematica code in Appendix C.

<!-- b000302 | furniture | pages [21] -->
Team #39173

<!-- b000303 | furniture | pages [21] -->
Page 21 of 32

<!-- b000304 | caption | pages [21] -->
Figure 12: The diagram above shows the search path produced by our al-

<!-- b000306 | prose | pages [21, 22] -->
21 rithm similar to ours but without requiring subsequent search regions to be adjacent. The code for this algorithm is contained in Appendix D.

<!-- b000307 | furniture | pages [22] -->
Team #39173

<!-- b000308 | furniture | pages [22] -->
Page 22 of 32

<!-- b000309 | caption | pages [22] -->
Figure 13: The diagram above shows the search path produced by an algo-

<!-- b000311 | prose | pages [22] -->
By comparing the two ﬁgures above, we can observe some key diﬀerences. When adjacency is not a requirement in our algorithm, frequently the subsequent search region is the reﬂection of the previous due to the symmetry of the joint probability distribution across the IFP. This leads to much more back-and-forth movement, and as a result, more distance traveled, thus wasting time and fuel.

<!-- b000312 | prose | pages [22] -->
To search a certain region, that region must be described in Lati- tude and Longitude. Continuing with the example, say the region in in need of searching is the discrete probability zone σ, N from 2 to 3. The algorithm from Section 2.3 in action is as follows: First, the rotation matrix:

<!-- b000313 | prose | pages [22] -->
 cos φ  0.9983  −0.0579 sin φ = −sin φ cos φ 0.0579 0.9983

<!-- b000314 | prose | pages [22] -->
is deﬁned using the rotation angle φ = −0.057939. It calculates the four latitude and longitude bounding coordinates of the rectangular search region σ, N from 2 to 3 as:

<!-- b000315 | prose | pages [22, 23] -->
22 See Appendix B for the Excel tables used for the calculation.

<!-- b000316 | furniture | pages [23] -->
Team #39173

<!-- b000317 | furniture | pages [23] -->
Page 23 of 32

<!-- b000319 | heading | pages [23] -->
4 Conclusion

<!-- b000320 | prose | pages [23] -->
The ﬁnal results of our model present a valid, time-eﬃcient search plan for locating missing ﬂight ABCD from Boston to Portugal. Our methodology accounts for all sizes and types of airplanes as well as all types of search planes. Our sensitivity analysis stresses the impor- tance of careful consideration of resources and the number of search planes. A greater number of search planes drastically increases the probability of detecting the missing plane. While some parameters are more robust than others, carefully choosing the number of search planes per square will optimize time-eﬃciency and overall detection. Our neighborhood-based search plan makes this model a strong choice when considering especially large search regions. While we did not have time, we hoped to incorporate the impacts of currents in the movement of airplane debris. We plan to further explore this topic to eventually extend our model to account for debris search plans too.

<!-- b000321 | heading | pages [23] -->
5 Summary for an Airline’s Press Con-

<!-- b000322 | prose | pages [23] -->
ference

<!-- b000323 | prose | pages [23] -->
There has been a new model proposed for locating missing transoceanic ﬂights, such as Malaysian Flight 370. Since 1948, 83 aircrafts have vanished, some of which have still not been found (Bloomberg). In the case of Malaysian ﬂight 370, not enough information was available on the plane’s modiﬁed path, to eﬀectively use the Search and Res- cue models currently in place(Seidel). This new mathematical model narrows the search region of missing planes and predicts their loca- tion of impact with the water, considering deviations from their in- tended paths. The model incorporates a time-eﬃcient search method, allocating time and eﬀort to the most likely locations of a missing transoceanic ﬂight traveling from point A to point B.

<!-- b000324 | prose | pages [23] -->
Since transoceanic ﬂights are not detected by radar when they are more than 200 miles from a coast, radio communication and the oc- casional satellite imagery is important in tracking the oﬀ-the-radar

<!-- b000325 | prose | pages [23, 24] -->
23 plane. These mathematicians created a search plan which is based on the last distance in miles on the intended ﬂight path (IFP) where Air Traﬃc Control heard from the pilot. The mathematicians assign probabilities to diﬀerent search regions. The model accounts for the likelihood that the plane fell closer to the distance of last contact rather than farther away, since loss of contact often indicates a me- chanical issue or takeover of the plane. They use physics, primarily modeling the gliding of planes from the sky, to determine a search area. The trajectories of the planes falling from the sky can be calcu- lated for any aircraft model, as they determine these distances using measurements of the cruising altitude and the Glide Ratio of a given plane. Basically, after performing several calculations, Probabilities of containment (POC) are assigned to each of these search areas. The probabilities will tell searchers how likely it is that the missing plane (or its parts) lie in that region.

<!-- b000326 | furniture | pages [24] -->
Team #39173

<!-- b000327 | furniture | pages [24] -->
Page 24 of 32

<!-- b000329 | prose | pages [24] -->
After mapping the likelihoods that the plane is in each of the re- gions, the mathematicians account for the probabilities that the search equipment will actually detect the plane. The simple equation for the probability of detection makes it easy to quickly input values like the speed of a search plane, a search plane’s radius, the number of search planes and more. If this probability is not as high as the team would like, it can easily be increased by adding more search parties to the team.

<!-- b000330 | prose | pages [24] -->
Once the searchers know their probability of detecting the lost plane, the mathematicians use a new algorithm to search the bounded area. This algorithm applies the probability of detecting the plane to each rectangular region which has a certain chance of containing the plane. If a plane is not found in a given region, the algorithm determines an appropriate neighboring region to search, making the search plan very time eﬃcient, and the process continues until the plane is located. There is still a chance that the plane was missed in a given region, so the search plan includes the possibility of revisiting certain areas later on. This customized neighborhood search plan maximizes resources while remaining time-eﬃcient.

<!-- b000331 | prose | pages [24] -->
Of course we must use this search plan with a few restrictions in mind. If the path from destination A to destination B is not a straight line, this method becomes more diﬃcult to use. The mathematicians note that while statistics are an incredibly powerful tool, there are always assumptions to consider, such as up to how far the plane could have veered from its intended path. This model is a breakthrough in Search and Rescue Theory and will be implemented when needed in the future.

<!-- b000332 | prose | pages [24] -->
24

<!-- b000333 | furniture | pages [25] -->
Team #39173

<!-- b000334 | furniture | pages [25] -->
Page 25 of 32

<!-- b000335 | heading | pages [25] -->
References

<!-- b000336 | references | pages [25] -->
[1] Benson, Tom. “Glide Angle.” Glide Angle. NASA, n.d. Web. 09

<!-- b000337 | references | pages [25] -->
Feb. 2015.

<!-- b000338 | references | pages [25] -->
[2] Frost, J. R. ”Principles of Search Theory.” Sarinfo.bc.ca. Soza and

<!-- b000339 | references | pages [25] -->
Company, Ltd., 1999. Web. 6 Feb. 2015.

<!-- b000340 | references | pages [25] -->
[3] Hartmann, Christoph, and Sonya Angelica Diehn. “The Technolo-

<!-- b000341 | references | pages [25] -->
gies behind the Search for Malaysia Airlines Flight 370.” DW.de.

<!-- b000342 | references | pages [25] -->
Deutsche Welle, 12 Mar. 2014. Web. 7 Feb. 2015.

<!-- b000343 | references | pages [25] -->
[4] Stone, Lawrence D. ”Search Theory: A Mathematical Theory for

<!-- b000344 | references | pages [25] -->
Finding Lost Objects.” Mathematics Magazine 50.5 (1977): 248-56.

<!-- b000345 | references | pages [25] -->
Web. 9 Feb. 2015.

<!-- b000346 | references | pages [25] -->
[5] Merrill,

<!-- b000347 | references | pages [25] -->
Dave,

<!-- b000348 | references | pages [25] -->
Chloe Whitaker,

<!-- b000349 | references | pages [25] -->
and Alex Tribou. ”Dozens

<!-- b000350 | references | pages [25] -->
of Planes Have Vanished in Post-WWII Era.” Bloomberg.com.

<!-- b000351 | references | pages [25] -->
Bloomberg, 20 Mar. 2014. Web. 9 Feb. 2015.

<!-- b000352 | references | pages [25] -->
[6] Seidel, Jamie. ”Missing Malaysia Airlines Flight MH370: Search

<!-- b000353 | references | pages [25] -->
Goes Back to Basics Turning to the Power of Maths to Solve the

<!-- b000354 | references | pages [25] -->
Mystery.” News.com.au. News Limited, 4 June 2014. Web. 6 Feb.

<!-- b000355 | references | pages [25] -->
2015.

<!-- b000356 | heading | pages [25] -->
6 Appendix A

<!-- b000357 | prose | pages [25] -->
Mathematica Code for Probability Generation:

<!-- b000358 | prose | pages [25] -->
np = Ceiling[(yb - yr - G*h)/(t05*vs)]

<!-- b000359 | prose | pages [25] -->
For[n = 1, n < 7, n++, discretefxyi = Integrate[ Integrate[ f[x, yi], {yi, (n - 1)*(yb - yr - G*h)/np, n*(yb - yr - G*h)/np}], {x, 0, G*h*Sin[Pi/8]}]; Print[discretefxyi // N]]

<!-- b000360 | prose | pages [25] -->
For[n = 1, n < 7, n++, discretefxyi = Integrate[ Integrate[ f[x, yi], {yi, (n - 1)*(yb - yr - G*h)/np, n*(yb - yr - G*h)/np}], {x, G*h*Sin[Pi/8], 2*G*h*Sin[Pi/8]}];

<!-- b000361 | prose | pages [25, 26] -->
25 Print[discretefxyi // N]]

<!-- b000362 | furniture | pages [26] -->
Team #39173

<!-- b000363 | furniture | pages [26] -->
Page 26 of 32

<!-- b000365 | prose | pages [26] -->
For[n = 1, n < 7, n++, discretefxyi = Integrate[ Integrate[ f[x, yi], {yi, (n - 1)*(yb - yr - G*h)/np, n*(yb - yr - G*h)/np}], {x, 2*G*h*Sin[Pi/8], 3*G*h*Sin[Pi/8]}]; Print[discretefxyi // N]]

<!-- b000366 | prose | pages [26] -->
Excel tables used to shift from IFP referenced search regions to Lati- tude and Longitude.

<!-- b000367 | heading | pages [26] -->
7 Appendix B

<!-- b000368 | prose | pages [26] -->
26

<!-- b000369 | furniture | pages [27] -->
Team #39173

<!-- b000370 | furniture | pages [27] -->
Page 27 of 32

<!-- b000371 | heading | pages [27] -->
8 Appendix C

<!-- b000372 | prose | pages [27] -->
Set up parameters and deﬁne POC matrix:

<!-- b000373 | prose | pages [27] -->
yb = 1912; G = 19; h = 7.58; yr = Sqrt[200^2 - h^2]; t05 = .5; vs = 550; ds = (yb - yr - G*h)/np; epsilon = 4; kappa = .98; hs = 2000/5280; np = Ceiling[(yb - yr - G*h)/(t05*vs)]; sp = 8;

<!-- b000374 | prose | pages [27] -->
POCn1s1 = 0.13367; POCn2s1 = 0.09323; POCn3s1 = 0.06008; POCn4s1 = 0.03421; POCn5

<!-- b000375 | prose | pages [27] -->
POCn1s2 = 0.05322; POCn2s2 = 0.03712; POCn3s2 = 0.02392; POCn4s2 = 0.01362; POCn5

<!-- b000376 | prose | pages [27] -->
POCn1s3 = 0.00838; POCn2s3 = 0.00585; POCn3s3 = 0.00377; POCn4s3 = 0.00214; POCn5

<!-- b000377 | prose | pages [27] -->
POCn1negs1 = 0.13367; POCn2negs1 = 0.09323; POCn3negs1 = 0.06008; POCn4negs1 = 0.

<!-- b000378 | prose | pages [27] -->
POCn1negs2 = 0.05322; POCn2negs2 = 0.03712; POCn3negs2 = 0.02392; POCn4negs2 = 0.

<!-- b000379 | prose | pages [27] -->
POCn1negs3 = 0.00838; POCn2negs3 = 0.00585; POCn3negs3 = 0.00377; POCn4negs3 = 0.

<!-- b000380 | prose | pages [27] -->
POC = {{0, 0, 0, 0, 0, 0, 0, 0}, {0, POCn1negs3, POCn1negs2, POCn1negs1, POCn1s1, POCn1s2, POCn1s3, 0}, {0, POCn2negs3, POCn2negs2, POCn2negs1, POCn2s1, POCn2s2, POCn2s3, 0}, {0, POCn3negs3, POCn3negs2, POCn3negs1, POCn3s1, POCn3s2, POCn3s3, 0}, {0, POCn4negs3, POCn4negs2, POCn4negs1, POCn4s1, POCn4s2, POCn4s3, 0}, {0, POCn5negs3, POCn5negs2, POCn5negs1, POCn5s1, POCn5s2, POCn5s3, 0}, {0, POCn6negs3, POCn6negs2, POCn6negs1, POCn6s1, POCn6s2, POCn6s3, 0}, {0, 0, 0, 0, 0, 0, 0, 0}};

<!-- b000381 | prose | pages [27] -->
POD = 1 - Exp[-((2*sp*ds*Sqrt[(k*epsilon)^2 - hs^2])/( G*h*Sin[Pi/8] (yb - yr - G*h)/np))]

<!-- b000382 | prose | pages [27, 28] -->
27 Loop for determining the order in which we will search regions without the requirement of adjacency; build loop with initial condi- tions as the highest or one of the highest initial POC regions:

<!-- b000383 | furniture | pages [28] -->
Team #39173

<!-- b000384 | furniture | pages [28] -->
Page 28 of 32

<!-- b000386 | prose | pages [28] -->
n = 2; s = 4; i = 1; POC = {{0, 0, 0, 0, 0, 0, 0, 0}, {0, POCn1negs3, POCn1negs2, POCn1negs1, POCn1s1, POCn1s2, POCn1s3, 0}, {0, POCn2negs3, POCn2negs2, POCn2negs1, POCn2s1, POCn2s2, POCn2s3, 0}, {0, POCn3negs3, POCn3negs2, POCn3negs1, POCn3s1, POCn3s2, POCn3s3,0}, {0, POCn4negs3, POCn4negs2, POCn4negs1, POCn4s1,POCn4s2, POCn4s3, 0}, {0, POCn5negs3, POCn5negs2,POCn5negs1, POCn5s1,POCn5s2, POCn5s3, 0}, {0,POCn6negs3, POCn6negs2, POCn6negs1, POCn6s1,POCn6s2,POCn6s3, 0}, {0, 0, 0, 0, 0, 0, 0, 0}};

<!-- b000387 | prose | pages [28] -->
While[1 < n < 7; 1 < s < 7; 0 < i < 60,

<!-- b000388 | prose | pages [28] -->
POC = (POC - Normal[SparseArray[{{n, s} -> POC[[n, s]]}, {8, 8}]] + Normal[SparseArray[{{n, s} -> (POC[[n, s]]*(1 - POD))}, {8, 8}]]) + (Ceiling[ POC - Normal[SparseArray[{{n, s} -> POC[[n, s]]}, {8, 8}]]]*( POC[[n, s]] - (POC[[n, s]]) (1 - POD))/(6*np - 1)); Min[Part[POC, n, s]*ConstantArray[1, {3, 3}] - Part[POC, n - 1 ;; n + 1, s - 1 ;; s + 1]];

<!-- b000389 | prose | pages [28] -->
rnxt = Position[Part[POC, n, s]*ConstantArray[1, {8, 8}] - POC, Min[Part[POC, n, s]*ConstantArray[1, {3, 3}] - Part[POC, n - 1 ;; n + 1, s - 1 ;; s + 1]]];

<!-- b000390 | prose | pages [28] -->
If[Length[rnxt] > 1, n = Part[Part[rnxt, If[Abs[n - Part[Part[rnxt, 1], 1]] > 1, 2, 1]], 1], n = Part[Part[rnxt, 1], 1]];

<!-- b000391 | prose | pages [28] -->
If[Length[rnxt] > 1, s = Part[Part[rnxt, If[Abs[s - Part[Part[rnxt, 1], 2]] > 1, 2, 1]], 2], s = Part[Part[rnxt, 1], 2]];

<!-- b000392 | prose | pages [28] -->
i++; POC = POC; Print[" n=", n - 1, ", s=" , s - 1]]

<!-- b000393 | prose | pages [28, 29] -->
28 Output:

<!-- b000394 | furniture | pages [29] -->
Team #39173

<!-- b000395 | furniture | pages [29] -->
Page 29 of 32

<!-- b000397 | prose | pages [29] -->
n=1, s=4 n=2, s=3 n=2, s=4 n=3, s=3 n=3, s=4 n=2, s=5 n=1, s=5 n=1, s=4 n=1, s=3 n=1, s=2 n=2, s=2 n=2, s=3 n=3, s=2 n=4, s=3 n=4, s=4 n=3, s=5 n=2, s=4 n=3, s=3 n=4, s=2 n=5, s=2 n=5, s=3 n=5, s=4 n=4, s=5 n=3, s=4 n=2, s=5 n=1, s=6 n=1, s=5 n=2, s=6 n=3, s=6 n=4, s=6 n=5, s=5 n=6, s=4 n=6, s=3 n=6, s=2 n=5, s=1 n=4, s=1 n=3, s=1 n=2, s=1 n=1, s=1 n=1, s=2 n=1, s=3 n=1, s=4

<!-- b000398 | prose | pages [29, 30] -->
29 n=2, s=3 n=2, s=2 n=3, s=2 n=4, s=3 n=4, s=4 n=3, s=5 n=2, s=4 n=3, s=3 n=4, s=2 n=5, s=2 n=6, s=1 n=6, s=2 n=5, s=3 n=5, s=4 n=6, s=5 n=5, s=6 n=6, s=6

<!-- b000399 | furniture | pages [30] -->
Team #39173

<!-- b000400 | furniture | pages [30] -->
Page 30 of 32

<!-- b000402 | heading | pages [30] -->
9 Appendix D

<!-- b000403 | prose | pages [30] -->
Loop for determining the order in which we will search regions without the requirement of adjacency:

<!-- b000404 | prose | pages [30] -->
n = 2; s = 4; i = 1; POC = {{0, 0, 0, 0, 0, 0, 0, 0}, {0, POCn1negs3, POCn1negs2, POCn1negs1, POCn1s1, POCn1s2, POCn1s3, 0}, {0, POCn2negs3, POCn2negs2, POCn2negs1, POCn2s1, POCn2s2, POCn2s3, 0}, {0, POCn3negs3, POCn3negs2, POCn3negs1, POCn3s1, POCn3s2, POCn3s3,0}, {0, POCn4negs3, POCn4negs2, POCn4negs1, POCn4s1,POCn4s2, POCn4s3, 0}, {0, POCn5negs3, POCn5negs2,POCn5negs1, POCn5s1,POCn5s2, POCn5s3, 0}, {0,POCn6negs3, POCn6negs2, POCn6negs1, POCn6s1,POCn6s2,POCn6s3, 0}, {0, 0, 0, 0, 0, 0, 0, 0}};

<!-- b000405 | prose | pages [30] -->
While[1 < n < 7; 1 < s < 7; 0 < i < 60,

<!-- b000406 | prose | pages [30] -->
POC = (POC - Normal[SparseArray[{{n, s} -> POC[[n, s]]}, {8, 8}]] + Normal[SparseArray[{{n, s} -> (POC[[n, s]]*(1 - POD))}, {8,

<!-- b000407 | prose | pages [30, 31] -->
30 8}]]) + (Ceiling[ POC - Normal[SparseArray[{{n, s} -> POC[[n, s]]}, {8, 8}]]]*( POC[[n, s]] - (POC[[n, s]]) (1 - POD))/(6*np - 1)); Min[Part[POC, n, s]*ConstantArray[1, {8, 8}] - POC];

<!-- b000408 | furniture | pages [31] -->
Team #39173

<!-- b000409 | furniture | pages [31] -->
Page 31 of 32

<!-- b000411 | prose | pages [31] -->
rnxt = Position[Part[POC, n, s]*ConstantArray[1, {8, 8}] - POC, Min[Part[POC, n, s]*ConstantArray[1, {8, 8}] - POC]];

<!-- b000412 | prose | pages [31] -->
If[Length[rnxt] > 1, n = Part[Part[rnxt, If[Abs[n - Part[Part[rnxt, 1], 1]] > 1, 2, 1]], 1], n = Part[Part[rnxt, 1], 1]];

<!-- b000413 | prose | pages [31] -->
If[Length[rnxt] > 1, s = Part[Part[rnxt, If[Abs[s - Part[Part[rnxt, 1], 2]] > 1, 2, 1]], 2], s = Part[Part[rnxt, 1], 2]]; i++; POC = POC; Print[" n=", n - 1, ", s=" , s - 1]]

<!-- b000414 | prose | pages [31] -->
n=1, s=4 n=2, s=3 n=2, s=4 n=3, s=3 n=3, s=4 n=1, s=5 n=1, s=2 n=2, s=2 n=2, s=5 n=4, s=4 n=4, s=3 n=3, s=2 n=3, s=5 n=4, s=5 n=4, s=2 n=1, s=3 n=1, s=6 n=1, s=1 n=1, s=4 n=5, s=3 n=5, s=2 n=5, s=5 n=5, s=4 n=2, s=6 n=2, s=1 n=6, s=4

<!-- b000415 | prose | pages [31, 32] -->
31 n=6, s=3 n=3, s=6 n=3, s=1 n=4, s=1 n=4, s=6 n=6, s=5 n=6, s=2 n=5, s=1 n=5, s=6 n=2, s=3 n=6, s=6 n=6, s=1 n=2, s=4 n=3, s=3 n=3, s=4 n=1, s=5 n=1, s=2 n=2, s=2 n=2, s=5 n=4, s=4 n=4, s=3 n=3, s=2 n=3, s=5 n=4, s=5 n=4, s=2 n=1, s=3 n=1, s=6 n=1, s=1 n=1, s=4 n=5, s=3 n=5, s=2 n=5, s=5 n=5, s=4

<!-- b000416 | furniture | pages [32] -->
Team #39173

<!-- b000417 | furniture | pages [32] -->
Page 32 of 32

<!-- b000419 | prose | pages [32] -->
32
