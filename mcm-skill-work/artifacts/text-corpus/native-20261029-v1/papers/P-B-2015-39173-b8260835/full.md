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

<!-- b000012 | heading | pages [2] -->
Contents

<!-- b000013 | contents | pages [2] -->
1

<!-- b000014 | heading | pages [2] -->
Introduction

<!-- b000015 | prose | pages [2] -->
2

<!-- b000016 | heading | pages [2] -->
Model

<!-- b000017 | furniture | pages [2] -->
Page 2 of 32

<!-- b000018 | prose | pages [2] -->
2

<!-- b000019 | prose | pages [2] -->
3 Constructing Probabilities of Containment for a Miss- 2.1 ing Airplane and its Debris . . . . . . . . . . . . . . .

<!-- b000020 | prose | pages [2] -->
3 Partitioning Search Region Through Model Dis- 2.1.1 cretization . . . . . . . . . . . . . . . . . . . . .

<!-- b000021 | prose | pages [2] -->
6 Finding Latitude and Longitude Coordinates for 2.1.2 Search Regions . . . . . . . . . . . . . . . . . .

<!-- b000022 | prose | pages [2] -->
8 Probability of Detection . . . . . . . . . . . . . . . . . 2.2 10 The POC-Updating Algorithm 2.3 . . . . . . . . . . . . .

<!-- b000023 | prose | pages [2] -->
11 Using the POC-Updating Algorithm to Deter- 2.3.1 mine Search Pattern . . . . . . . . . . . . . . .

<!-- b000024 | prose | pages [2] -->
11 Assumptions in the Methodology . . . . . . . . . . . . 2.4 12 Sensitivity Analysis . . . . . . . . . . . . . . . . . . . . 2.5 12 Strengths and Weaknesses of Our Model . . . . . . . . 2.6 15 Strengths . . . . . . . . . . . . . . . . . . . . . 2.6.1 15 Weaknesses . . . . . . . . . . . . . . . . . . . . 2.6.2 16

<!-- b000025 | prose | pages [2] -->
Working Example: Flight ABCD to Lisbon, Portugal 3 Reported Missing

<!-- b000026 | prose | pages [2] -->
4

<!-- b000027 | heading | pages [2] -->
Conclusion

<!-- b000028 | prose | pages [2] -->
16

<!-- b000029 | prose | pages [2] -->
23

<!-- b000030 | prose | pages [2] -->
Summary for an Airline’s Press Conference 5

<!-- b000031 | prose | pages [2] -->
6

<!-- b000032 | heading | pages [2] -->
Appendix A

<!-- b000033 | prose | pages [2] -->
7

<!-- b000034 | heading | pages [2] -->
Appendix B

<!-- b000035 | prose | pages [2] -->
8

<!-- b000036 | heading | pages [2] -->
Appendix C

<!-- b000037 | prose | pages [2] -->
9

<!-- b000038 | heading | pages [2] -->
Appendix D

<!-- b000039 | prose | pages [2] -->
1

<!-- b000040 | heading | pages [2] -->
Introduction

<!-- b000041 | prose | pages [2] -->
23

<!-- b000042 | prose | pages [2] -->
25

<!-- b000043 | prose | pages [2] -->
26

<!-- b000044 | prose | pages [2] -->
27

<!-- b000045 | prose | pages [2] -->
30

<!-- b000046 | prose | pages [2] -->
Since 1948, 83 aircrafts have vanished, some of which have still not been found (Bloomberg). Lost transoceanic ﬂights are among the hardest ﬂights to locate due to the lack of radar coverage. An average radius for radar coverage is approximately 200 miles in any direction (Hartmann). Because radar coverage is not an available method to track a transoceanic ﬂight’s activity, Air Traﬃc Control (ATC) relies

<!-- b000047 | prose | pages [2] -->
2 2

<!-- b000048 | furniture | pages [3] -->
Team #39173

<!-- b000049 | furniture | pages [3] -->
Page 3 of 32

<!-- b000050 | prose | pages [3] -->
on radio or messaging communication with a pilot on a regular, pre- determined basis. If there are no location updates in the designated time frame, signals alert Air Traﬃc Control that there has been a loss of communication, and that there is a potentially missing ﬂight.

<!-- b000051 | prose | pages [3] -->
In the past, Bayesian statistical methods have been used to track the whereabouts of missing ﬂights. Air France Flight 447 went down in 2009 and was not found for over a year. Towards the end of the search, statisticians used Bayesian methods, narrowed the search plane, and picked up the blackbox’s radio transmitter signal, locating the plane (Seidel). The available prior information, such as weather conditions on the ﬂight path, ﬂoating bodies found soon-after, and the signal of the beacon eliminated search zones. On the other hand Malaysian Flight 370 contained little prior information, the search began later, no ﬂoating remnants were found, and individuals presumed the blackbox signal was turned oﬀ(Seidel). To this day, the location of ﬂight MH370 remains unclear.

<!-- b000052 | prose | pages [3] -->
In order to confront the diﬃcult situation in which a plane is lost and prior information is scarce, we set out to create a mathematical model and search plan. Our model accounts for an indeﬁnite time until casualty and impact with the water.

<!-- b000053 | prose | pages [3] -->
Potential deviations oﬀ the intended ﬂight path, relevant to the Malaysian Flight, are also considered and time-eﬃciency is prioritized. We propose an eﬀective search strategy in the case of a lost, signal-less transoceanic ﬂight.

<!-- b000054 | prose | pages [3] -->
2

<!-- b000055 | heading | pages [3] -->
Model

<!-- b000056 | prose | pages [3] -->
Our model considers a lost ﬂight, which starts at some location A and sets out to travel across the ocean linearly to its destination B. In order to develop an optimized search plan, we consider the proba- bilities of containment of the plane’s whereabouts, the probabilities of detecting the plane while eﬃciently and conservatively using resources, and the continuously updating probabilities of the most likely location of the missing airplane.

<!-- b000057 | prose | pages [3] -->
2.1 Constructing Probabilities of Containment for a Missing Airplane and its Debris

<!-- b000058 | prose | pages [3] -->
The containment model maps the probability of the airplane’s con- tainment to speciﬁc regions surrounding the ﬂight’s last known posi- tion. Our ﬁrst consideration in the containment model is estimating how far the plane most likely travels after a signal is lost. The vari- able y0 is the last distance in miles from the starting location where

<!-- b000059 | prose | pages [3] -->
3

<!-- b000060 | furniture | pages [4] -->
Team #39173

<!-- b000061 | furniture | pages [4] -->
Page 4 of 32

<!-- b000062 | prose | pages [4] -->
air traﬃc controllers heard from the pilot. In addition to the mileage covered, it is important to take note of the initial latitude and lon- gitude coordinates at y0. It is assumed that the plane stayed on its Intended Flight Path (IFP) at this time. At this location, it is un- clear if the plane continued traveling in the air or began falling to the ground. The Random Variable Yc refers to the distance to casualty, or the distance on the IFP at which the plane started to malfunction. It is assumed that when a plane malfunctions, its descent for the water begins. The distance to casualty is measured from y0 = 0. We have modeled the probability density function of Yc as follows:

<!-- b000063 | prose | pages [4] -->
(

<!-- b000064 | prose | pages [4] -->
3 (yB−yR)3 (yC −(yB −yR))2

<!-- b000065 | prose | pages [4] -->
fyc(yc) =

<!-- b000066 | prose | pages [4] -->
0 : y0 ≤yC < yB −yR : elsewhere

<!-- b000067 | prose | pages [4] -->
where yB indicates the remaining distance to destination B from y0 and yR is the ﬁnal mileage of the journey for which radar detection is available. Therefore, yB −yR represents the ﬂying distance left before Air-Traﬃc Control (ATC) radar detectors can spot the missing ﬂight.

<!-- b000068 | prose | pages [4] -->
Our Random Variable Yc is constructed under the assumption that it is more likely for the plane to reach a casualty-state immediately or soon after the last communication with ATC. This intuition is reason- able because a loss of communication often occurs due to abnormal plane operation. The probability continues to decrease quadratically and becomes 0 in the radar-detective zone. The parameter yR can be determined using the equation below:

<!-- b000069 | prose | pages [4] -->
(200)2 −h2 =

<!-- b000070 | prose | pages [4] -->
p

<!-- b000071 | prose | pages [4] -->
yR =

<!-- b000072 | prose | pages [4] -->
p

<!-- b000073 | prose | pages [4] -->
40, 000 −h2

<!-- b000074 | prose | pages [4] -->
where h is the cruising altitude in miles of the jet. Radar detectors can track planes within a 200 mile radius, on average (Hartmann), so yR can be determined by manipulating the Pythagorean Theorem.

<!-- b000075 | prose | pages [4] -->
We determine the possible locations where the airplane could have fallen based on a distribution of trajectories. The distance of impact, or the distance from y0 at which the airplane hit the water is YI. This variable takes into account the glide of the airplane and the distance at which it is completely submerged and is modeled as follows:

<!-- b000076 | prose | pages [4] -->
YI = YC + Gh

<!-- b000077 | prose | pages [4] -->
where G is the glide ratio of the plane (NASA). Each airplane model has an average glide ratio which is deﬁned as

<!-- b000078 | prose | pages [4] -->
G = units of distance forward

<!-- b000079 | prose | pages [4] -->
unit of distance downward.

<!-- b000080 | prose | pages [4] -->
The glide ratio is multiplied by the cruising altitude to determine the horizontal distance the plane traveled during its downward fall

<!-- b000081 | prose | pages [4] -->
4 4

<!-- b000082 | furniture | pages [5] -->
Team #39173

<!-- b000083 | furniture | pages [5] -->
Page 5 of 32

<!-- b000084 | prose | pages [5] -->
(NASA). The probability density function of YI can therefore be mod- eled using the following transformation of variables technique:

<!-- b000085 | prose | pages [5] -->
P(YC + Gh < yI) P(YI < yI) =

<!-- b000086 | prose | pages [5] -->
P(YC < yI −Gh) =

<!-- b000087 | prose | pages [5] -->
Z yI−Gh

<!-- b000088 | prose | pages [5] -->
3 = (yB −yR)3

<!-- b000089 | prose | pages [5] -->
3

<!-- b000090 | prose | pages [5] -->
(yC −(yB −yR))2dyC 0 0

<!-- b000091 | prose | pages [5] -->
yI−Gh

<!-- b000092 | furniture | pages [5] -->


<!-- b000093 | prose | pages [5] -->
(yB −yR)3 [(yC −(yB −yR))2dyC] =

<!-- b000094 | prose | pages [5] -->
3

<!-- b000095 | prose | pages [5] -->
0

<!-- b000096 | prose | pages [5] -->
(yB −yR)3 ([(yI −Gh −yB + yR)2][(0 −yB + yR)2] =

<!-- b000097 | prose | pages [5] -->
fyI(yI) = d =⇒

<!-- b000098 | prose | pages [5] -->
dyI

<!-- b000099 | prose | pages [5] -->
3 (yB −yR)3 ([(yI −Gh −yB + yR)2][(0 −yB + yR)2]

<!-- b000100 | prose | pages [5] -->
After taking the derivative with respect to YI we can conclude that the probability density function for YI is:

<!-- b000101 | prose | pages [5] -->
(

<!-- b000102 | prose | pages [5] -->
3 (yB−yR)3 (yI −Gh −(yB −yR))2

<!-- b000103 | prose | pages [5] -->
fyI(yI) =

<!-- b000104 | prose | pages [5] -->
0 : Gh ≤yI < yB −yR : elsewhere

<!-- b000105 | prose | pages [5] -->
The probable distances from the point of lost contact to the point of impact are measured in line with the IFP. While this model has accounted for a single dimension, we can easily extend it to the left and to the right, indicating a plane’s maneuver oﬀcourse. The next portion of our model accounts for the possibility of veering oﬀthe intended linear path.

<!-- b000106 | prose | pages [5] -->
Veering away from the IFP is considered by assuming the segment of water representing the locations of impact are the average, or 0, and that the possible locations of the plane are normally distributed to the sides of yI.

<!-- b000107 | prose | pages [5] -->
5 5

<!-- b000108 | furniture | pages [6] -->
Team #39173

<!-- b000109 | furniture | pages [6] -->
Page 6 of 32

<!-- b000110 | caption | pages [6] -->
Figure 1: One standard deviation is calculated to be the distance from the

<!-- b000111 | prose | pages [6] -->
IFP where a plane gliding π

<!-- b000112 | heading | pages [6] -->
8 oﬀcourse would land.

<!-- b000113 | prose | pages [6] -->
Standard deviation of the normal probability distribution is deter- mined by

<!-- b000114 | prose | pages [6] -->
σx = Gh sin (π

<!-- b000115 | prose | pages [6] -->
8 )

<!-- b000116 | prose | pages [6] -->
Since it is unlikely that a plane veers beyond π

<!-- b000117 | prose | pages [6] -->
8 from the IFP, π 8 will be used to ﬁnd one standard deviation. Thus the normal probability distribution perpendicular to the IFP is:

<!-- b000118 | prose | pages [6] -->
−x2

<!-- b000119 | prose | pages [6] -->
2(Gh sin( π 8 ))2

<!-- b000120 | prose | pages [6] -->
e f(x) =

<!-- b000121 | prose | pages [6] -->
Gh sin(π

<!-- b000122 | prose | pages [6] -->
8 ) √ √

<!-- b000123 | prose | pages [6] -->
2π : −∞< x < ∞

<!-- b000124 | prose | pages [6] -->
Because f(x) and f(yI) are independent distributions, we can cre- ate a joint probability density function by multiplying f(x) and f(yI) as follows: f(x, yI) = f(x)f(yI).

<!-- b000125 | prose | pages [6] -->


<!-- b000126 | prose | pages [6] -->
3(yI−Gh−(yB−yR))2

<!-- b000127 | prose | pages [6] -->
2π(yB−yR)3 e

<!-- b000128 | prose | pages [6] -->


<!-- b000129 | prose | pages [6] -->
√

<!-- b000130 | prose | pages [6] -->
f(x, yI) =

<!-- b000131 | prose | pages [6] -->
Gh sin π

<!-- b000132 | prose | pages [6] -->
8

<!-- b000133 | prose | pages [6] -->
0

<!-- b000134 | prose | pages [6] -->


<!-- b000135 | prose | pages [6] -->
−x2

<!-- b000136 | prose | pages [6] -->
2(Ghsin( π 8 ))2 : −∞< x < ∞, Gh ≤yI < yB −yR : elsewhere

<!-- b000137 | heading | pages [6] -->
Partitioning Search Region Through Model Dis-

<!-- b000138 | prose | pages [6] -->
2.1.1 cretization

<!-- b000139 | prose | pages [6] -->
Given f(x, yI), the search ﬁeld can be divided into distinct regions. Each region is assigned a probability of containment (POC), indicating the probability that the region contains the missing plane and debris.

<!-- b000140 | prose | pages [6] -->
6 6

<!-- b000141 | furniture | pages [7] -->
Team #39173

<!-- b000142 | furniture | pages [7] -->
Page 7 of 32

<!-- b000143 | prose | pages [7] -->
In order to discretize our model, we ﬁrst consider X, the normal ran- dom variable. Since 99.7% of all observations are contained within 3 standard deviations of the mean, our search region is bounded on both sides by three standard deviations. We segment yI over its entire range. Therefore, we consider N −1 partitions and N vertical regions through the following equation:

<!-- b000144 | prose | pages [7] -->
lyB −yR −Gh

<!-- b000145 | prose | pages [7] -->
m

<!-- b000146 | prose | pages [7] -->
N =

<!-- b000147 | prose | pages [7] -->
t0.5vs

<!-- b000148 | prose | pages [7] -->
where t0.5 represents the quantity 0.5 hours and vs is the velocity of the search plane.This guarantees that each search plane spends up to half an hour sweeping a length of each search region. Assuming more than one plane searches a given region at a time, these partitions lead to a highly eﬃcient search duration.

<!-- b000149 | caption | pages [7] -->
Figure 2: The discretization method is modeled by the above SAN×6 search

<!-- b000150 | prose | pages [7] -->
region matrix. Note that in this case N = 4.

<!-- b000151 | prose | pages [7] -->
To ﬁnd the probabilities of containment for each of the above rect- angular regions, the joint probability density function f(x, yI) must be integrated over each region’s boundaries. In order to ﬁnd N × 6 prob- ability values, a loop was created in Mathematica. The loop considers only the regions to the right of the IFP, since the normal distribu- tion has the property of symmetry. The loop iterates through all N partitions in YI given each of the 3 set X regions. Below is the algo- rithm for the probability generation of each region within 1 standard deviation of the IFP:

<!-- b000152 | prose | pages [7] -->
7

<!-- b000153 | furniture | pages [8] -->
Team #39173

<!-- b000154 | furniture | pages [8] -->
Page 8 of 32

<!-- b000155 | prose | pages [8] -->
Z 1( YB−YR−Gh

<!-- b000156 | prose | pages [8] -->
Z Gh sin( π

<!-- b000157 | prose | pages [8] -->
8 )

<!-- b000158 | prose | pages [8] -->
N

<!-- b000159 | prose | pages [8] -->
0( YB−YR−Gh

<!-- b000160 | prose | pages [8] -->
0

<!-- b000161 | prose | pages [8] -->
N

<!-- b000162 | prose | pages [8] -->
)+Gh

<!-- b000163 | prose | pages [8] -->
f(x, yI)dxdyI

<!-- b000164 | prose | pages [8] -->
)+Gh

<!-- b000165 | prose | pages [8] -->
Z 2( YB−YR−Gh

<!-- b000166 | prose | pages [8] -->
Z Gh sin( π

<!-- b000167 | prose | pages [8] -->
8 )

<!-- b000168 | prose | pages [8] -->
N

<!-- b000169 | prose | pages [8] -->
1( YB−YR−Gh

<!-- b000170 | prose | pages [8] -->
0

<!-- b000171 | prose | pages [8] -->
N

<!-- b000172 | prose | pages [8] -->
Z Gh sin( π

<!-- b000173 | prose | pages [8] -->
Z N( YB−YR−Gh

<!-- b000174 | prose | pages [8] -->
8 )

<!-- b000175 | prose | pages [8] -->
N

<!-- b000176 | prose | pages [8] -->
)+Gh

<!-- b000177 | prose | pages [8] -->
f(x, yI)dxdyI

<!-- b000178 | prose | pages [8] -->
)+Gh

<!-- b000179 | prose | pages [8] -->
... ...

<!-- b000180 | prose | pages [8] -->
)+Gh

<!-- b000181 | prose | pages [8] -->
f(x, yI)dxdyI

<!-- b000182 | prose | pages [8] -->
(N−1)( YB−YR−Gh

<!-- b000183 | prose | pages [8] -->
0

<!-- b000184 | prose | pages [8] -->
)+Gh N N

<!-- b000185 | prose | pages [8] -->
The output of this loop is a list of probability values that can be matched to each of the search regions. Refer to Appendix B for the Now that we have determined probabilities of Mathematica Code. containment for each of these ocean search regions, we must obtain the boundaries of each region in latitude and longitude coordinates to facilitate the search and rescue team’s eﬀorts.

<!-- b000186 | prose | pages [8] -->
Finding Latitude and Longitude Coordinates for 2.1.2 Search Regions

<!-- b000187 | prose | pages [8] -->
Initially, the bounds of a given uniform probability region ru×l can be represented as 0 ≤u ≤N and −3 ≤l ≤3 where l, u are integer multiples of n = region number along the IFP, σx respectively.

<!-- b000188 | caption | pages [8] -->
Figure 3: The location of a given ru×l = (l, u) in reference to an IFP and σx

<!-- b000189 | prose | pages [8] -->
In order to reference a discretized probability region to the IFP and y0, we must deﬁne a coordinate axis with a y-axis along the IFP,

<!-- b000190 | prose | pages [8] -->
8 8

<!-- b000191 | furniture | pages [9] -->
Team #39173

<!-- b000192 | furniture | pages [9] -->
Page 9 of 32

<!-- b000193 | prose | pages [9] -->
an x-axis in the direction of σx and an origin at (yI, 0σx). Now the bounds of a region ru×l in miles are:

<!-- b000194 | prose | pages [9] -->
−l(Gh sin (π

<!-- b000195 | prose | pages [9] -->
8 )) ≤x ≤l(Gh sin (π

<!-- b000196 | prose | pages [9] -->
and

<!-- b000197 | prose | pages [9] -->
8 ))

<!-- b000198 | prose | pages [9] -->
0 ≤y ≤u(||yB −y0|| −Gh) . N

<!-- b000199 | prose | pages [9] -->
To translate any given number m of zone-bounding coordinates in (x,y) to latitude and longitude, build a 2 × m matrix

<!-- b000200 | prose | pages [9] -->
C = [c1c2c3...cm]

<!-- b000201 | prose | pages [9] -->
where each bounding coordinate ci where 0 < i ≤m is of the form

<!-- b000202 | prose | pages [9] -->
cx

<!-- b000203 | prose | pages [9] -->
 

<!-- b000204 | prose | pages [9] -->
.

<!-- b000205 | prose | pages [9] -->
cy cy

<!-- b000206 | prose | pages [9] -->
Next, using a rotation matrix, vector addition and vector scaling will eﬀectively shift an “IFP-referenced” coordinate to latitude and longi- tude. y0 and yB are known in the “IFP-referenced” system and in traditional coordinates. The components of yB −y0 in latitude and longitude are designated re, rn. To build a rotation matrix from the “IFP-referenced” system to latitude and longitude, we ﬁrst must ﬁnd the counter-clockwise angle φ between the two coordinate systems as follows:

<!-- b000207 | prose | pages [9] -->
φ = arctan ( re

<!-- b000208 | prose | pages [9] -->
).

<!-- b000209 | prose | pages [9] -->
rn

<!-- b000210 | prose | pages [9] -->
Using φ, the rotation matrix R is either:

<!-- b000211 | prose | pages [9] -->
 cos φ

<!-- b000212 | prose | pages [9] -->


<!-- b000213 | prose | pages [9] -->
: π

<!-- b000214 | prose | pages [9] -->
sin φ

<!-- b000215 | prose | pages [9] -->
R =

<!-- b000216 | prose | pages [9] -->
−sin φ

<!-- b000217 | prose | pages [9] -->
2 ≤φ < 0

<!-- b000218 | prose | pages [9] -->
cos φ

<!-- b000219 | prose | pages [9] -->
or

<!-- b000220 | prose | pages [9] -->
cos φ

<!-- b000221 | prose | pages [9] -->


<!-- b000222 | prose | pages [9] -->
: 0 ≤φ ≤π

<!-- b000223 | prose | pages [9] -->
−sin φ

<!-- b000224 | prose | pages [9] -->
R =

<!-- b000225 | prose | pages [9] -->
sin φ cos φ

<!-- b000226 | prose | pages [9] -->
2 .

<!-- b000227 | prose | pages [9] -->
One way to test whether the rotation matrix is calculated correctly is to verify that det(R) = 1. After ﬁnding a suitable R, multiply C by R to express every c in C in miles of latitude and longitude with reference to y0ρ where ρ is the average distance in miles of one degree North and one degree East from y0. Finally, add the resulting vector to y0 to have coordinates in degrees North and East. In summary, changing C in the “IFP-referenced” system to the corresponding coordinate matrix CL in latitude and longitude amounts to:

<!-- b000228 | prose | pages [9] -->
CL = ρRC + y0.

<!-- b000229 | prose | pages [9] -->
9 9

<!-- b000230 | furniture | pages [10] -->
Team #39173

<!-- b000231 | furniture | pages [10] -->
Page 10 of 32

<!-- b000232 | prose | pages [10] -->
Probability of Detection 2.2

<!-- b000233 | prose | pages [10] -->
A standard model for ﬁnding the Probability of Detection (POD) is the exponential function

<!-- b000234 | prose | pages [10] -->
POD = 1 −e−coverage

<!-- b000235 | prose | pages [10] -->
where coverage is the area eﬀectively swept divided by the entire search area AS (Frost 1999). To determine our region’s POD, we use a slight variation of B.O. Koopman’s Exponential Model. The search area is deﬁned as

<!-- b000236 | prose | pages [10] -->
8 )(yB −yR −Gh

<!-- b000237 | prose | pages [10] -->
AS = Gh sin(π

<!-- b000238 | prose | pages [10] -->
). N

<!-- b000239 | prose | pages [10] -->
where the AS represents the area of a single partitioned region of the overall search region.The area eﬀectively swept is dependent on the eﬀective sweep width S and the eﬀort.

<!-- b000240 | prose | pages [10] -->
The eﬀective sweep width depends on the eﬀective detection distance κϵ of the instrument (eg. human eyes, radar, etc.) used for the search, and the elevation of the cruising search plane is hs. We modify Koopman’s model to account for variations in weather, conditions, search abilities and more. This variation is denoted by the scalar κ, which takes values between 0 and 1. The distance from the search plane’s path projected on the ocean

<!-- b000241 | prose | pages [10] -->
(κϵ)2 −h2s. Assuming the

<!-- b000242 | prose | pages [10] -->
p

<!-- b000243 | prose | pages [10] -->
to the furthest possible detected object is

<!-- b000244 | prose | pages [10] -->
search plane ﬂies in parallel swaths, the eﬀective sweep width would be

<!-- b000245 | prose | pages [10] -->
p

<!-- b000246 | prose | pages [10] -->
S = 2

<!-- b000247 | prose | pages [10] -->
(κϵ)2 −h2s

<!-- b000248 | prose | pages [10] -->
in order to detect all of AS. The eﬀort is said to be dsn where the distance searched by an individual aircraft per swath is ds and the number of search planes included in the search is n. Assuming the search plane ﬂies parallel to the IFP, the number of swaths the plane must ﬂy is the number of subregions N so ds is

<!-- b000249 | prose | pages [10] -->
ds = (yb −yr −Gh

<!-- b000250 | prose | pages [10] -->
). N

<!-- b000251 | prose | pages [10] -->
In order to search simultaneously and most eﬃciently, the planes are assumed to be ﬂying at the same velocity. Thus ds is the same for each plane since they begin searching simultaneously. Incorporating each of these components into a single model yields the following POD equation:

<!-- b000252 | prose | pages [10] -->
−2

<!-- b000253 | prose | pages [10] -->
POD = 1 −e

<!-- b000254 | prose | pages [10] -->
dsn√

<!-- b000255 | prose | pages [10] -->
(κϵ)2−h2s

<!-- b000256 | prose | pages [10] -->
(yB−yR−Gh)

<!-- b000257 | prose | pages [10] -->
Gh sin π

<!-- b000258 | prose | pages [10] -->
8

<!-- b000259 | prose | pages [10] -->
N

<!-- b000260 | prose | pages [10] -->
Unless search eﬀort is changed based on the search region, it is assumed that the POD is uniform among all regions of probable con- tainment.

<!-- b000261 | prose | pages [10] -->
10 10

<!-- b000262 | furniture | pages [11] -->
Team #39173

<!-- b000263 | furniture | pages [11] -->
Page 11 of 32

<!-- b000264 | prose | pages [11] -->
2.3

<!-- b000265 | heading | pages [11] -->
The POC-Updating Algorithm

<!-- b000266 | prose | pages [11] -->
If there were no such thing as instrumentation error or human er- ror, POD would equal 1 and thus not adjust the POC’s of discretized zones. Since search conditions are nowhere near perfect, we assign 1 −PODq to be the probability that the lost plane in region q went undetected. Given that we do not ﬁnd the plane after searching the zone q, we update the POC in q to be

<!-- b000267 | prose | pages [11] -->
POCq′ = (POCq)(1 −PODq).

<!-- b000268 | prose | pages [11] -->
This is the probability that the plane is actually in the searched re- gion, even though it was not detected. Assuming that net probability of containment of all discretized zones is constant, the probability lost when POCq becomes POCq′ must be accounted for in the other regions. To do this, we add

<!-- b000269 | prose | pages [11] -->
POCq −POCq′

<!-- b000270 | prose | pages [11] -->
6N −1 to each of the POC values except POCq′. This process can be iterated during a search to update all the POC values per searched discrete probability zone.

<!-- b000271 | prose | pages [11] -->
2.3.1

<!-- b000272 | heading | pages [11] -->
Using the POC-Updating Algorithm to Determine

<!-- b000273 | prose | pages [11] -->
Search Pattern

<!-- b000274 | prose | pages [11] -->
To determine the best order to search the 6×N diﬀerent regions, we use the POC-updating algorithm described above using gradients to choose the next search region. By the ”best” order we mean the most eﬃcient in terms of resources and time. We want to spend the least amount of time and fuel covering the entire map. Thus we want to minimize ﬂight between nonadjacent regions because that increases less-useful or redundant coverage and increases time needed to cover the entire area. The search plan algorithm involves updating the POC map after completing the search of one region to ﬁnd the new proba- bility of containment map, given the downed aircraft was not detected in the recently-searched region. Using a matrix in Mathematica we represent the map of POC’s.

<!-- b000275 | prose | pages [11] -->
A loop was created in Mathematica to evaluate, for each iteration, the diﬀerences between the updated POC’s of the just-searched region k and its adjacent neighbors. We take the minimum of the diﬀerences, and then locate the row nnew and column σnew of that minimum element, to ﬁnd the next region rnnew,σnew to be searched.

<!-- b000276 | prose | pages [11] -->
Essentially this method consists of up- dating the POC matrix, calculating a gradient/diﬀerence to identify the highest adjacent POC, and taking that region as the next to be searched.

<!-- b000277 | prose | pages [11] -->
11

<!-- b000278 | furniture | pages [12] -->
Team #39173

<!-- b000279 | furniture | pages [12] -->
Page 12 of 32

<!-- b000280 | prose | pages [12] -->
2.4

<!-- b000281 | heading | pages [12] -->
Assumptions in the Methodology

<!-- b000282 | prose | pages [12] -->
There are several assumptions upon which our model and the re- sulting search plan are built. Below is a list of assumptions we con- sider:

<!-- b000283 | prose | pages [12] -->
• The lost plane’s pre-established course is a linear path from point A to point B.

<!-- b000284 | prose | pages [12] -->
• The lost plane’s glide aﬀects its trajectory into the ocean. The plane does not explode in the sky.

<!-- b000285 | prose | pages [12] -->
• Any debris disassembles upon impacting the water.

<!-- b000286 | prose | pages [12] -->
• The plane will not veer more than 3Ghsin(π 8 ) oﬀthe IFP.

<!-- b000287 | prose | pages [12] -->
• There are no forces (eg. currents) to move the debris or plane from where they ﬁrst landed.

<!-- b000288 | prose | pages [12] -->
• All planes (lost plane and search plane(s)) in the model are ﬂying at a constant velocity.

<!-- b000289 | prose | pages [12] -->
• The lost plane is more likely to be found near the last point of communication.

<!-- b000290 | prose | pages [12] -->
• The lost plane remains aﬂoat (detectable) during the entire time the search is in action.

<!-- b000291 | prose | pages [12] -->
• Every searching plane has the same instrumentation, searches at the same speed and ﬂies at the same altitude.

<!-- b000292 | prose | pages [12] -->
2.5

<!-- b000293 | heading | pages [12] -->
Sensitivity Analysis

<!-- b000294 | prose | pages [12] -->
In order to test how changing parameters eﬀect our model, we include a discussion of the relationships between speciﬁc parameters and their eﬀects on the components of our model and search plan.

<!-- b000295 | prose | pages [12] -->
We assess the impacts of changing parameters on f(x, yI) by con- sidering f(G) and f(θ). From experimentation with ﬁxing the random variables x and yI, the shape of the curve of f(G), and f(θ) are strik- ingly similar.

<!-- b000296 | prose | pages [12] -->
12

<!-- b000297 | furniture | pages [13] -->
Team #39173

<!-- b000298 | furniture | pages [13] -->
Page 13 of 32

<!-- b000299 | caption | pages [13] -->
Figure 4: f(G) where (x, yI) = (0.5, 0.5) exempliﬁes the curvature of f(G)

<!-- b000300 | prose | pages [13] -->
and f(θ) regardless of the x and yI values

<!-- b000301 | prose | pages [13] -->
As G and θ increase, the respective f(G) and f(θ) exhibit a rapid decrease. Since the bounded integral of f(x, y) produces a POC, G and θ have the same eﬀect on POC as they do on f(x, y). In short, as G + θ decreases, the probability of ﬁnding the lost plane increases.

<!-- b000302 | prose | pages [13] -->
Increasing θ will directly increase the search area because the X distance is measured in mile-multiples of σx = Gh sin (θ) which is pro- portional to a chosen 0 ≤θ ≤π

<!-- b000303 | prose | pages [13] -->
2 . The following graphs are generated using the constant parameter values found in the Working Example (Section 3).

<!-- b000304 | caption | pages [13] -->
Figure 5: POD(θ) where θ is in radians

<!-- b000305 | prose | pages [13] -->
As θ increases, POD rapidly decreases from one to zero. The most intriguing part of POD(θ) is that the graph suggests POD(0) ≈1. Also, the POD is extremely small for any plane that has veered more than ninety degrees oﬀthe IFP.

<!-- b000306 | prose | pages [13] -->
Increasing the glide ratio eﬀects the POD similarly to increasing θ.

<!-- b000307 | prose | pages [13] -->
13

<!-- b000308 | furniture | pages [14] -->
Team #39173

<!-- b000309 | furniture | pages [14] -->
Page 14 of 32

<!-- b000310 | caption | pages [14] -->
Figure 6: POD(G)

<!-- b000311 | prose | pages [14] -->
Increasing the exponent’s denominator will have an inverse eﬀect on the POD. Thus, a search party following the methodology explained in the Working Example will be more likely to ﬁnd a plane with a small glide ratio.

<!-- b000312 | prose | pages [14] -->
Another variable that clearly eﬀects the search plan is the cruising altitude, hS, at which the search plane ﬂies because the POD depends

<!-- b000313 | prose | pages [14] -->
κϵ2 −h2s. Varying hs within 0 ≤hs < ϵ produces an elliptic

<!-- b000314 | prose | pages [14] -->
p

<!-- b000315 | prose | pages [14] -->
on

<!-- b000316 | prose | pages [14] -->
graph of POD centered around the origin:

<!-- b000317 | caption | pages [14] -->
Figure 7: POD(hs) where 0 ≤hs < ϵ

<!-- b000318 | caption | pages [14] -->
Figure 4 illustrates that when hs

<!-- b000319 | prose | pages [14] -->
increases, the POD increases. ϵ This is a logical relationship because each swath will cover more ground which will in turn decrease the search eﬀort. Thus, it is best to run the search at the lowest possible altitude in order to improve the chance of ﬁnding the lost plane.

<!-- b000320 | prose | pages [14] -->
The number of search planes n also eﬀect the POD because the search eﬀort n is in the numerator of the search eﬀort fraction. Illus- trated graphically:

<!-- b000321 | prose | pages [14] -->
14

<!-- b000322 | furniture | pages [15] -->
Team #39173

<!-- b000323 | furniture | pages [15] -->
Page 15 of 32

<!-- b000324 | caption | pages [15] -->
Figure 8: POD(hs) where n ∈N

<!-- b000325 | prose | pages [15] -->
In a practical sense, incorporating more search planes will increase the likelihood of detection.

<!-- b000326 | prose | pages [15] -->
(κϵ)2 −h2s there

<!-- b000327 | prose | pages [15] -->
p

<!-- b000328 | prose | pages [15] -->
Since the POD equation contains the element

<!-- b000329 | prose | pages [15] -->
may be a square root of a negative number if h2

<!-- b000330 | prose | pages [15] -->
s > (κϵ)2. A plane must ﬂy low enough for the eﬀective range of the instrumentation (κϵ) to reach the ground. Otherwise there is no chance the plane will detect anything below it and thus the POD would be eﬀectively zero.

<!-- b000331 | prose | pages [15] -->
s > (κϵ)2 there is no point in searching until conditions

<!-- b000332 | prose | pages [15] -->
Thus when h2

<!-- b000333 | prose | pages [15] -->
improve.

<!-- b000334 | prose | pages [15] -->
Clearly, our model is sensitive to changes in several of the parame- ters and therefore may not be considered a robust probabilistic model. However, the sensitivity to changes in the input parameters is neces- sary to have a model that is accommodating to the speciﬁcations of diﬀerent types of planes and search instruments.

<!-- b000335 | heading | pages [15] -->
Strengths and Weaknesses of Our Model

<!-- b000336 | prose | pages [15] -->
2.6

<!-- b000337 | prose | pages [15] -->
2.6.1

<!-- b000338 | heading | pages [15] -->
Strengths

<!-- b000339 | prose | pages [15] -->
Our outlined model has particular strengths, unavailable in other Search and Rescue methods. First, we use a quadratic probability density function rather than the commonly-used uniform distribution. In many Search and Rescue Methodologies, it is assumed that the time of casualty is uniformly distributed over all possible times in a given Here, we carefully construct a decreasing, range (Lawrence 1977). concave down distribution to account for the large likelihood that complications arise early after y0. Our model also accounts for a ﬂight trajectory to map the ﬂight’s motion at the time of casualty to a region of the ocean surface. The change of bases allows the searchers to locate the search regions using actual latitude, longitude coordinates rather than tracking angles and distances from the point of lost contact. The POD incorporates several factors, including an added constant k.

<!-- b000340 | prose | pages [15] -->
15 15

<!-- b000341 | furniture | pages [16] -->
Team #39173

<!-- b000342 | furniture | pages [16] -->
Page 16 of 32

<!-- b000343 | prose | pages [16] -->
When k = 1, the search occurs in perfect conditions, while k = 0.5 may indicate some fog, choppy water, or other inhibiting factors. This constant helps to better explain the rate of coverage while still using Koopman’s commonly-used Exponential Model.

<!-- b000344 | prose | pages [16] -->
Our search plan is a constantly updating algorithm keeping time eﬃciency in mind. If an item is not detected in a highly probable re- gion, the POC’s of the other search regions are updated. The cell with the next highest probability in the searched region’s “neighborhood” is investigated. Implementing a neighborhood restriction speeds up the search process, wasting no travel time while still searching regions with high POC’s. Our search plan can easily be generalized to search planes of diﬀerent speeds and larger or smaller regions of the ocean.

<!-- b000345 | prose | pages [16] -->
2.6.2

<!-- b000346 | heading | pages [16] -->
Weaknesses

<!-- b000347 | prose | pages [16] -->
It is important to consider the weaknesses of our model that may be worth addressing in the future. First, the POC of the regions closest to Gh but more than 1 standard deviation away in the X direction are slightly over-allocated.

<!-- b000348 | prose | pages [16] -->
The standard deviation was calculated using trigonometry, indicating that our rectangular probability region is based on a triangular calculation. Refer to Figure 1. Because of this over-allocation, there is a slight under-calculation of probabilities 1 or more standard deviations away from the IFP towards the latter partitions of YI.

<!-- b000349 | prose | pages [16] -->
Another weakness to consider is the lack of consideration of cur- rents in each of our partitioned search regions. With more time, we hope to extend the impacts of surface currents to locating debris and other remnants of the aircraft.

<!-- b000350 | prose | pages [16] -->
3 Working Example: Flight ABCD to Lisbon, Portugal Reported Missing

<!-- b000351 | prose | pages [16] -->
16

<!-- b000352 | furniture | pages [17] -->
Team #39173

<!-- b000353 | furniture | pages [17] -->
Page 17 of 32

<!-- b000354 | prose | pages [17] -->
Imagine that on February 9, 2015 Flight ABCD from Boston, MA to Lisbon Portugal disappeared on a Boeing 777 aircraft. The point of last communication occurred at coordinates 40.9275◦N, 46.2575◦

<!-- b000355 | prose | pages [17] -->
W. Let yB = 1, 912 miles. The plane was cruising at a speed of 560 miles per hour at an altitude of 40, 000 feet (7.58 miles), so yR = 199.86. Assume that the ﬂight is entirely over open ocean and the Lisbon airport is the nearest location to y0 that can detect an airplane. So, yR is measured from the Lisbon airport along the IFP. Below is the probability distribution of YC, the random variable representing the probability that at a given distance in the direction of the IFP the plane experiences a casualty that causes it to begin a downward trajectory.

<!-- b000356 | prose | pages [17] -->
(

<!-- b000357 | prose | pages [17] -->
3 (1912−199.86)3 (yC −(1912 −199.86))2

<!-- b000358 | prose | pages [17] -->
fyc(yc) =

<!-- b000359 | prose | pages [17] -->
0 : 0 ≤yC < 1712.14 : elsewhere

<!-- b000360 | prose | pages [17] -->
This airplane has a glide ratio of approximately 19 : 1, similar to other large aircrafts. With this information, yI can be modeled as follows:

<!-- b000361 | prose | pages [17] -->
(

<!-- b000362 | prose | pages [17] -->
3 (1712.14)3 (yI −1568.12)2

<!-- b000363 | prose | pages [17] -->
fyI(yI) =

<!-- b000364 | prose | pages [17] -->
0 : 144.02 ≤yI < 1712.14 : elsewhere

<!-- b000365 | prose | pages [17] -->
After considering the distribution of distances of impact, we must now account for the possibility of veering oﬀthe IFP. The following X distribution, distributed in the direction perpendicular to the intended ﬂight path, accounts for Flight ABCD’s potential oﬀ-course location of impact:

<!-- b000366 | prose | pages [17] -->
−x2

<!-- b000367 | prose | pages [17] -->
2(144.02 sin( π 8 ))2

<!-- b000368 | prose | pages [17] -->
e

<!-- b000369 | prose | pages [17] -->
√

<!-- b000370 | prose | pages [17] -->
f(x) =

<!-- b000371 | prose | pages [17] -->
144.02 sin(π 8 )

<!-- b000372 | prose | pages [17] -->
2π : −∞< x < ∞

<!-- b000373 | prose | pages [17] -->
17 17

<!-- b000374 | furniture | pages [18] -->
Team #39173

<!-- b000375 | furniture | pages [18] -->
Page 18 of 32

<!-- b000376 | prose | pages [18] -->
By multiplying the independent equations f(x) ∗f(yI), a joint probability density function is obtained.

<!-- b000377 | prose | pages [18] -->


<!-- b000378 | prose | pages [18] -->
3(yI−1568.12)2

<!-- b000379 | prose | pages [18] -->
−x2

<!-- b000380 | prose | pages [18] -->
2(144.02 sin( π 8 ))2 : −∞< x < ∞, 144.02 ≤yI < 1712.14

<!-- b000381 | prose | pages [18] -->
2π(1712.14)3 e

<!-- b000382 | prose | pages [18] -->


<!-- b000383 | prose | pages [18] -->
√

<!-- b000384 | prose | pages [18] -->
f(x, yI) =

<!-- b000385 | prose | pages [18] -->
144.02 sin( π 8 )

<!-- b000386 | prose | pages [18] -->
0

<!-- b000387 | prose | pages [18] -->


<!-- b000388 | prose | pages [18] -->
: elsewhere

<!-- b000389 | caption | pages [18] -->
Figure 9: The joint density function is shown above, indicating the locations

<!-- b000390 | prose | pages [18] -->
in which the POC is largest, and locations where the POC is smallest

<!-- b000391 | prose | pages [18] -->
Now, the multi-dimensional probability distribution, POC, can be discretized into 36 subregion each calculated by a double integral, as described in section 2.1.1 Partitioning Search Regions Through Model Discretization.

<!-- b000392 | prose | pages [18] -->
18 18

<!-- b000393 | furniture | pages [19] -->
Team #39173

<!-- b000394 | furniture | pages [19] -->
Page 19 of 32

<!-- b000395 | caption | pages [19] -->
Figure 10: The graph above represents the discretized POC of Flight ABCD

<!-- b000396 | caption | pages [19] -->
Figure 11: Map representation of POC allocated to each of the search regions

<!-- b000397 | prose | pages [19] -->
Next, the Probability of Detection is found by the formula as de- scribed in the section 2.2:

<!-- b000398 | prose | pages [19] -->
−

<!-- b000399 | prose | pages [19] -->
POD = 1 −e

<!-- b000400 | prose | pages [19] -->
2∗dsn√ (kϵ)2−h2s Gh sin π

<!-- b000401 | prose | pages [19] -->
8 (yB−yR−Gh)/N

<!-- b000402 | prose | pages [19] -->
The list of parameters for this model, either estimated or researched values, is as follows:

<!-- b000403 | prose | pages [19] -->
• Remaining distance of ﬂight from y0 to yR, yB = 1912

<!-- b000404 | prose | pages [19] -->
• Glide constant for a large plane such as a a Boeing 777-200, G = 19

<!-- b000405 | prose | pages [19] -->
19 19

<!-- b000406 | furniture | pages [20] -->
Team #39173

<!-- b000407 | furniture | pages [20] -->
Page 20 of 32

<!-- b000408 | prose | pages [20] -->
• Average altitude at which a commercial airliner cruises, h = 7.58

<!-- b000409 | prose | pages [20] -->
√

<!-- b000410 | prose | pages [20] -->
2002 −h2

<!-- b000411 | prose | pages [20] -->
• yR =

<!-- b000412 | prose | pages [20] -->
• Velocity of the search planes (all of which are the same model in order to facilitate easier coordination and timing in the search), vs = 550

<!-- b000413 | prose | pages [20] -->
• t.05 = .5 hours

<!-- b000414 | prose | pages [20] -->
m

<!-- b000415 | prose | pages [20] -->
l

<!-- b000416 | prose | pages [20] -->
yB−yR−Gh

<!-- b000417 | prose | pages [20] -->
• The number of partitions in the y direction, N =

<!-- b000418 | prose | pages [20] -->
t.05vs

<!-- b000419 | prose | pages [20] -->
• Distance traveled by search planes in searching a single region, ds = (yB−yR−Gh)

<!-- b000420 | prose | pages [20] -->
np • Detection distance of instrument, ϵ = 4

<!-- b000421 | prose | pages [20] -->
• Scales detection distance based on search conditions such as weather, κ = 0.98, note < 0κ < 1. In this case, κ is near one, indicating clear calm search conditions.

<!-- b000422 | prose | pages [20] -->
• Number of search planes n, chosen in this example to be 8.

<!-- b000423 | prose | pages [20] -->
• Then, POD = 0.677831 for our example, when we plug in all the variables

<!-- b000424 | prose | pages [20] -->
Taking the values in Figure 11, we input them to Mathematica to form the initial POC matrix. We then utilize the method described in section 2.3 and subsection 2.3.1, and the Mathematica code in Ap- pendix C, to determine the order and path of the most eﬃcient search pattern. We also utilize the model to update probabilities that certain regions contain the lost plane given the plane was not detected when the an area was most recently searched.

<!-- b000425 | prose | pages [20] -->
20 20

<!-- b000426 | furniture | pages [21] -->
Team #39173

<!-- b000427 | furniture | pages [21] -->
Page 21 of 32

<!-- b000428 | caption | pages [21] -->
Figure 12: The diagram above shows the search path produced by our al-

<!-- b000429 | prose | pages [21] -->
gorithm and described by the output of the Mathematica code in Appendix C.

<!-- b000430 | prose | pages [21] -->
21

<!-- b000431 | furniture | pages [22] -->
Team #39173

<!-- b000432 | furniture | pages [22] -->
Page 22 of 32

<!-- b000433 | caption | pages [22] -->
Figure 13: The diagram above shows the search path produced by an algo-

<!-- b000434 | prose | pages [22] -->
rithm similar to ours but without requiring subsequent search regions to be adjacent. The code for this algorithm is contained in Appendix D.

<!-- b000435 | prose | pages [22] -->
By comparing the two ﬁgures above, we can observe some key diﬀerences. When adjacency is not a requirement in our algorithm, frequently the subsequent search region is the reﬂection of the previous due to the symmetry of the joint probability distribution across the IFP. This leads to much more back-and-forth movement, and as a result, more distance traveled, thus wasting time and fuel.

<!-- b000436 | prose | pages [22] -->
To search a certain region, that region must be described in Lati- tude and Longitude. Continuing with the example, say the region in in need of searching is the discrete probability zone σ, N from 2 to 3. The algorithm from Section 2.3 in action is as follows: First, the rotation matrix:

<!-- b000437 | prose | pages [22] -->
 cos φ

<!-- b000438 | prose | pages [22] -->


<!-- b000439 | prose | pages [22] -->
sin φ

<!-- b000440 | prose | pages [22] -->
=

<!-- b000441 | prose | pages [22] -->
−sin φ cos φ

<!-- b000442 | prose | pages [22] -->
0.9983

<!-- b000443 | prose | pages [22] -->


<!-- b000444 | prose | pages [22] -->
−0.0579 0.0579 0.9983

<!-- b000445 | prose | pages [22] -->
is deﬁned using the rotation angle φ = −0.057939. It calculates the four latitude and longitude bounding coordinates of the rectangular search region σ, N from 2 to 3 as:

<!-- b000446 | prose | pages [22] -->
22 22

<!-- b000447 | furniture | pages [23] -->
Team #39173

<!-- b000448 | furniture | pages [23] -->
Page 23 of 32

<!-- b000449 | prose | pages [23] -->
See Appendix B for the Excel tables used for the calculation.

<!-- b000450 | prose | pages [23] -->
4

<!-- b000451 | heading | pages [23] -->
Conclusion

<!-- b000452 | prose | pages [23] -->
The ﬁnal results of our model present a valid, time-eﬃcient search plan for locating missing ﬂight ABCD from Boston to Portugal. Our methodology accounts for all sizes and types of airplanes as well as all types of search planes. Our sensitivity analysis stresses the impor- tance of careful consideration of resources and the number of search planes. A greater number of search planes drastically increases the probability of detecting the missing plane. While some parameters are more robust than others, carefully choosing the number of search planes per square will optimize time-eﬃciency and overall detection. Our neighborhood-based search plan makes this model a strong choice when considering especially large search regions. While we did not have time, we hoped to incorporate the impacts of currents in the movement of airplane debris. We plan to further explore this topic to eventually extend our model to account for debris search plans too.

<!-- b000453 | prose | pages [23] -->
5 Summary for an Airline’s Press Con- ference

<!-- b000454 | prose | pages [23] -->
There has been a new model proposed for locating missing transoceanic ﬂights, such as Malaysian Flight 370. Since 1948, 83 aircrafts have vanished, some of which have still not been found (Bloomberg). In the case of Malaysian ﬂight 370, not enough information was available on the plane’s modiﬁed path, to eﬀectively use the Search and Res- cue models currently in place(Seidel). This new mathematical model narrows the search region of missing planes and predicts their loca- tion of impact with the water, considering deviations from their in- tended paths. The model incorporates a time-eﬃcient search method, allocating time and eﬀort to the most likely locations of a missing transoceanic ﬂight traveling from point A to point B.

<!-- b000455 | prose | pages [23] -->
Since transoceanic ﬂights are not detected by radar when they are more than 200 miles from a coast, radio communication and the oc- casional satellite imagery is important in tracking the oﬀ-the-radar

<!-- b000456 | prose | pages [23] -->
23

<!-- b000457 | furniture | pages [24] -->
Team #39173

<!-- b000458 | furniture | pages [24] -->
Page 24 of 32

<!-- b000459 | prose | pages [24] -->
plane. These mathematicians created a search plan which is based on the last distance in miles on the intended ﬂight path (IFP) where Air Traﬃc Control heard from the pilot. The mathematicians assign probabilities to diﬀerent search regions. The model accounts for the likelihood that the plane fell closer to the distance of last contact rather than farther away, since loss of contact often indicates a me- chanical issue or takeover of the plane. They use physics, primarily modeling the gliding of planes from the sky, to determine a search area. The trajectories of the planes falling from the sky can be calcu- lated for any aircraft model, as they determine these distances using measurements of the cruising altitude and the Glide Ratio of a given plane. Basically, after performing several calculations, Probabilities of containment (POC) are assigned to each of these search areas. The probabilities will tell searchers how likely it is that the missing plane (or its parts) lie in that region.

<!-- b000460 | prose | pages [24] -->
After mapping the likelihoods that the plane is in each of the re- gions, the mathematicians account for the probabilities that the search equipment will actually detect the plane. The simple equation for the probability of detection makes it easy to quickly input values like the speed of a search plane, a search plane’s radius, the number of search planes and more. If this probability is not as high as the team would like, it can easily be increased by adding more search parties to the team.

<!-- b000461 | prose | pages [24] -->
Once the searchers know their probability of detecting the lost plane, the mathematicians use a new algorithm to search the bounded area. This algorithm applies the probability of detecting the plane to each rectangular region which has a certain chance of containing the plane. If a plane is not found in a given region, the algorithm determines an appropriate neighboring region to search, making the search plan very time eﬃcient, and the process continues until the plane is located. There is still a chance that the plane was missed in a given region, so the search plan includes the possibility of revisiting certain areas later on.

<!-- b000462 | prose | pages [24] -->
This customized neighborhood search plan maximizes resources while remaining time-eﬃcient.

<!-- b000463 | prose | pages [24] -->
Of course we must use this search plan with a few restrictions in mind. If the path from destination A to destination B is not a straight line, this method becomes more diﬃcult to use. The mathematicians note that while statistics are an incredibly powerful tool, there are always assumptions to consider, such as up to how far the plane could have veered from its intended path. This model is a breakthrough in Search and Rescue Theory and will be implemented when needed in the future.

<!-- b000464 | prose | pages [24] -->
24

<!-- b000465 | furniture | pages [25] -->
Team #39173

<!-- b000466 | furniture | pages [25] -->
Page 25 of 32

<!-- b000467 | heading | pages [25] -->
References

<!-- b000468 | references | pages [25] -->
[1] Benson, Tom. “Glide Angle.” Glide Angle. NASA, n.d. Web. 09

<!-- b000469 | references | pages [25] -->
Feb. 2015.

<!-- b000470 | references | pages [25] -->
[2] Frost, J. R. ”Principles of Search Theory.” Sarinfo.bc.ca. Soza and

<!-- b000471 | references | pages [25] -->
Company, Ltd., 1999. Web. 6 Feb. 2015.

<!-- b000472 | references | pages [25] -->
[3] Hartmann, Christoph, and Sonya Angelica Diehn. “The Technolo-

<!-- b000473 | references | pages [25] -->
gies behind the Search for Malaysia Airlines Flight 370.” DW.de.

<!-- b000474 | references | pages [25] -->
Deutsche Welle, 12 Mar. 2014. Web. 7 Feb. 2015.

<!-- b000475 | references | pages [25] -->
[4] Stone, Lawrence D. ”Search Theory: A Mathematical Theory for

<!-- b000476 | references | pages [25] -->
Finding Lost Objects.” Mathematics Magazine 50.5 (1977): 248-56.

<!-- b000477 | references | pages [25] -->
Web. 9 Feb. 2015.

<!-- b000478 | references | pages [25] -->
[5] Merrill,

<!-- b000479 | references | pages [25] -->
Dave,

<!-- b000480 | references | pages [25] -->
Chloe Whitaker,

<!-- b000481 | references | pages [25] -->
and Alex Tribou. ”Dozens

<!-- b000482 | references | pages [25] -->
of Planes Have Vanished in Post-WWII Era.” Bloomberg.com.

<!-- b000483 | references | pages [25] -->
Bloomberg, 20 Mar. 2014. Web. 9 Feb. 2015.

<!-- b000484 | references | pages [25] -->
[6] Seidel, Jamie. ”Missing Malaysia Airlines Flight MH370: Search

<!-- b000485 | references | pages [25] -->
Goes Back to Basics Turning to the Power of Maths to Solve the

<!-- b000486 | references | pages [25] -->
Mystery.” News.com.au. News Limited, 4 June 2014. Web. 6 Feb.

<!-- b000487 | references | pages [25] -->
2015.

<!-- b000488 | references | pages [25] -->
6

<!-- b000489 | heading | pages [25] -->
Appendix A

<!-- b000490 | prose | pages [25] -->
Mathematica Code for Probability Generation:

<!-- b000491 | prose | pages [25] -->
np = Ceiling[(yb - yr - G*h)/(t05*vs)]

<!-- b000492 | prose | pages [25] -->
For[n = 1, n < 7, n++,

<!-- b000493 | prose | pages [25] -->
discretefxyi =

<!-- b000494 | prose | pages [25] -->
Integrate[

<!-- b000495 | prose | pages [25] -->
Integrate[

<!-- b000496 | prose | pages [25] -->
f[x, yi], {yi, (n - 1)*(yb - yr - G*h)/np,

<!-- b000497 | prose | pages [25] -->
n*(yb - yr - G*h)/np}], {x, 0, G*h*Sin[Pi/8]}]; Print[discretefxyi // N]]

<!-- b000498 | prose | pages [25] -->
For[n = 1, n < 7, n++,

<!-- b000499 | prose | pages [25] -->
discretefxyi =

<!-- b000500 | prose | pages [25] -->
Integrate[

<!-- b000501 | prose | pages [25] -->
Integrate[

<!-- b000502 | prose | pages [25] -->
f[x, yi], {yi, (n - 1)*(yb - yr - G*h)/np,

<!-- b000503 | prose | pages [25] -->
n*(yb - yr - G*h)/np}], {x, G*h*Sin[Pi/8], 2*G*h*Sin[Pi/8]}];

<!-- b000504 | prose | pages [25] -->
25

<!-- b000505 | furniture | pages [26] -->
Team #39173

<!-- b000506 | furniture | pages [26] -->
Page 26 of 32

<!-- b000507 | prose | pages [26] -->
Print[discretefxyi // N]]

<!-- b000508 | prose | pages [26] -->
For[n = 1, n < 7, n++,

<!-- b000509 | prose | pages [26] -->
discretefxyi =

<!-- b000510 | prose | pages [26] -->
Integrate[

<!-- b000511 | prose | pages [26] -->
Integrate[

<!-- b000512 | prose | pages [26] -->
f[x, yi], {yi, (n - 1)*(yb - yr - G*h)/np,

<!-- b000513 | prose | pages [26] -->
n*(yb - yr - G*h)/np}], {x, 2*G*h*Sin[Pi/8], 3*G*h*Sin[Pi/8]}]; Print[discretefxyi // N]]

<!-- b000514 | prose | pages [26] -->
Excel tables used to shift from IFP referenced search regions to Lati- tude and Longitude.

<!-- b000515 | prose | pages [26] -->
7

<!-- b000516 | heading | pages [26] -->
Appendix B

<!-- b000517 | prose | pages [26] -->
26

<!-- b000518 | furniture | pages [27] -->
Team #39173

<!-- b000519 | furniture | pages [27] -->
Page 27 of 32

<!-- b000520 | prose | pages [27] -->
8

<!-- b000521 | heading | pages [27] -->
Appendix C

<!-- b000522 | prose | pages [27] -->
Set up parameters and deﬁne POC matrix:

<!-- b000523 | prose | pages [27] -->
yb = 1912; G = 19; h = 7.58; yr = Sqrt[200^2 - h^2]; t05 = .5; vs = 550; ds = (yb - yr - G*h)/np; epsilon = 4; kappa = .98; hs = 2000/5280; np = Ceiling[(yb - yr - G*h)/(t05*vs)]; sp = 8;

<!-- b000524 | prose | pages [27] -->
POCn1s1 = 0.13367; POCn2s1 = 0.09323; POCn3s1 = 0.06008; POCn4s1 = 0.03421; POCn5

<!-- b000525 | prose | pages [27] -->
POCn1s2 = 0.05322; POCn2s2 = 0.03712; POCn3s2 = 0.02392; POCn4s2 = 0.01362; POCn5

<!-- b000526 | prose | pages [27] -->
POCn1s3 = 0.00838; POCn2s3 = 0.00585; POCn3s3 = 0.00377; POCn4s3 = 0.00214; POCn5

<!-- b000527 | prose | pages [27] -->
POCn1negs1 = 0.13367; POCn2negs1 = 0.09323; POCn3negs1 = 0.06008; POCn4negs1 = 0.

<!-- b000528 | prose | pages [27] -->
POCn1negs2 = 0.05322; POCn2negs2 = 0.03712; POCn3negs2 = 0.02392; POCn4negs2 = 0.

<!-- b000529 | prose | pages [27] -->
POCn1negs3 = 0.00838; POCn2negs3 = 0.00585; POCn3negs3 = 0.00377; POCn4negs3 = 0.

<!-- b000530 | prose | pages [27] -->
POC = {{0, 0, 0, 0, 0, 0, 0, 0}, {0, POCn1negs3, POCn1negs2,

<!-- b000531 | prose | pages [27] -->
POCn1negs1, POCn1s1, POCn1s2, POCn1s3, 0}, {0, POCn2negs3, POCn2negs2, POCn2negs1, POCn2s1, POCn2s2, POCn2s3, 0}, {0, POCn3negs3, POCn3negs2, POCn3negs1, POCn3s1, POCn3s2, POCn3s3, 0}, {0, POCn4negs3, POCn4negs2, POCn4negs1, POCn4s1, POCn4s2, POCn4s3, 0}, {0, POCn5negs3, POCn5negs2, POCn5negs1, POCn5s1, POCn5s2, POCn5s3, 0}, {0, POCn6negs3, POCn6negs2, POCn6negs1, POCn6s1, POCn6s2, POCn6s3, 0}, {0, 0, 0, 0, 0, 0, 0, 0}};

<!-- b000532 | prose | pages [27] -->
POD = 1 - Exp[-((2*sp*ds*Sqrt[(k*epsilon)^2 - hs^2])/(

<!-- b000533 | prose | pages [27] -->
G*h*Sin[Pi/8] (yb - yr - G*h)/np))]

<!-- b000534 | prose | pages [27] -->
27

<!-- b000535 | furniture | pages [28] -->
Team #39173

<!-- b000536 | furniture | pages [28] -->
Page 28 of 32

<!-- b000537 | prose | pages [28] -->
Loop for determining the order in which we will search regions without the requirement of adjacency; build loop with initial condi- tions as the highest or one of the highest initial POC regions:

<!-- b000538 | prose | pages [28] -->
n = 2; s = 4; i = 1; POC = {{0, 0, 0, 0, 0, 0, 0, 0}, {0, POCn1negs3, POCn1negs2,

<!-- b000539 | prose | pages [28] -->
POCn1negs1, POCn1s1, POCn1s2, POCn1s3, 0}, {0, POCn2negs3, POCn2negs2, POCn2negs1, POCn2s1, POCn2s2, POCn2s3, 0}, {0, POCn3negs3, POCn3negs2, POCn3negs1, POCn3s1, POCn3s2, POCn3s3,0}, {0, POCn4negs3, POCn4negs2, POCn4negs1, POCn4s1,POCn4s2, POCn4s3, 0}, {0, POCn5negs3, POCn5negs2,POCn5negs1, POCn5s1,POCn5s2, POCn5s3, 0}, {0,POCn6negs3, POCn6negs2, POCn6negs1, POCn6s1,POCn6s2,POCn6s3, 0}, {0, 0, 0, 0, 0, 0, 0, 0}};

<!-- b000540 | prose | pages [28] -->
While[1 < n < 7; 1 < s < 7; 0 < i < 60,

<!-- b000541 | prose | pages [28] -->
POC = (POC - Normal[SparseArray[{{n, s} -> POC[[n, s]]}, {8, 8}]] +

<!-- b000542 | prose | pages [28] -->
Normal[SparseArray[{{n, s} -> (POC[[n, s]]*(1 - POD))}, {8,

<!-- b000543 | prose | pages [28] -->
8}]]) + (Ceiling[ POC - Normal[SparseArray[{{n, s} -> POC[[n, s]]}, {8, 8}]]]*( POC[[n, s]] - (POC[[n, s]]) (1 - POD))/(6*np - 1)); Min[Part[POC, n, s]*ConstantArray[1, {3, 3}] -

<!-- b000544 | prose | pages [28] -->
Part[POC, n - 1 ;; n + 1, s - 1 ;; s + 1]];

<!-- b000545 | prose | pages [28] -->
rnxt = Position[Part[POC, n, s]*ConstantArray[1, {8, 8}] - POC,

<!-- b000546 | prose | pages [28] -->
Min[Part[POC, n, s]*ConstantArray[1, {3, 3}] -

<!-- b000547 | prose | pages [28] -->
Part[POC, n - 1 ;; n + 1, s - 1 ;; s + 1]]];

<!-- b000548 | prose | pages [28] -->
If[Length[rnxt] > 1,

<!-- b000549 | prose | pages [28] -->
n = Part[Part[rnxt, If[Abs[n - Part[Part[rnxt, 1], 1]] > 1, 2, 1]],

<!-- b000550 | prose | pages [28] -->
1], n = Part[Part[rnxt, 1], 1]];

<!-- b000551 | prose | pages [28] -->
If[Length[rnxt] > 1,

<!-- b000552 | prose | pages [28] -->
s = Part[Part[rnxt, If[Abs[s - Part[Part[rnxt, 1], 2]] > 1, 2, 1]],

<!-- b000553 | prose | pages [28] -->
2], s = Part[Part[rnxt, 1], 2]];

<!-- b000554 | prose | pages [28] -->
i++; POC = POC; Print[" n=", n - 1, ", s=" , s - 1]]

<!-- b000555 | prose | pages [28] -->
28

<!-- b000556 | furniture | pages [29] -->
Team #39173

<!-- b000557 | furniture | pages [29] -->
Page 29 of 32

<!-- b000558 | prose | pages [29] -->
Output:

<!-- b000559 | prose | pages [29] -->
n=1, s=4 n=2, s=3 n=2, s=4 n=3, s=3 n=3, s=4 n=2, s=5 n=1, s=5 n=1, s=4 n=1, s=3 n=1, s=2 n=2, s=2 n=2, s=3 n=3, s=2 n=4, s=3 n=4, s=4 n=3, s=5 n=2, s=4 n=3, s=3 n=4, s=2 n=5, s=2 n=5, s=3 n=5, s=4 n=4, s=5 n=3, s=4 n=2, s=5 n=1, s=6 n=1, s=5 n=2, s=6 n=3, s=6 n=4, s=6 n=5, s=5 n=6, s=4 n=6, s=3 n=6, s=2 n=5, s=1 n=4, s=1 n=3, s=1 n=2, s=1 n=1, s=1 n=1, s=2 n=1, s=3 n=1, s=4

<!-- b000560 | prose | pages [29] -->
29

<!-- b000561 | furniture | pages [30] -->
Team #39173

<!-- b000562 | furniture | pages [30] -->
Page 30 of 32

<!-- b000563 | prose | pages [30] -->
n=2, s=3 n=2, s=2 n=3, s=2 n=4, s=3 n=4, s=4 n=3, s=5 n=2, s=4 n=3, s=3 n=4, s=2 n=5, s=2 n=6, s=1 n=6, s=2 n=5, s=3 n=5, s=4 n=6, s=5 n=5, s=6 n=6, s=6

<!-- b000564 | prose | pages [30] -->
9

<!-- b000565 | heading | pages [30] -->
Appendix D

<!-- b000566 | prose | pages [30] -->
Loop for determining the order in which we will search regions without the requirement of adjacency:

<!-- b000567 | prose | pages [30] -->
n = 2; s = 4; i = 1; POC = {{0, 0, 0, 0, 0, 0, 0, 0}, {0, POCn1negs3, POCn1negs2,

<!-- b000568 | prose | pages [30] -->
POCn1negs1, POCn1s1, POCn1s2, POCn1s3, 0}, {0, POCn2negs3, POCn2negs2, POCn2negs1, POCn2s1, POCn2s2, POCn2s3, 0}, {0, POCn3negs3, POCn3negs2, POCn3negs1, POCn3s1, POCn3s2, POCn3s3,0}, {0, POCn4negs3, POCn4negs2, POCn4negs1, POCn4s1,POCn4s2, POCn4s3, 0}, {0, POCn5negs3, POCn5negs2,POCn5negs1, POCn5s1,POCn5s2, POCn5s3, 0}, {0,POCn6negs3, POCn6negs2, POCn6negs1, POCn6s1,POCn6s2,POCn6s3, 0}, {0, 0, 0, 0, 0, 0, 0, 0}};

<!-- b000569 | prose | pages [30] -->
While[1 < n < 7; 1 < s < 7; 0 < i < 60,

<!-- b000570 | prose | pages [30] -->
POC = (POC - Normal[SparseArray[{{n, s} -> POC[[n, s]]}, {8, 8}]] +

<!-- b000571 | prose | pages [30] -->
Normal[SparseArray[{{n, s} -> (POC[[n, s]]*(1 - POD))}, {8,

<!-- b000572 | prose | pages [30] -->
30

<!-- b000573 | furniture | pages [31] -->
Team #39173

<!-- b000574 | furniture | pages [31] -->
Page 31 of 32

<!-- b000575 | prose | pages [31] -->
8}]]) + (Ceiling[ POC - Normal[SparseArray[{{n, s} -> POC[[n, s]]}, {8, 8}]]]*( POC[[n, s]] - (POC[[n, s]]) (1 - POD))/(6*np - 1)); Min[Part[POC, n, s]*ConstantArray[1, {8, 8}] - POC];

<!-- b000576 | prose | pages [31] -->
rnxt = Position[Part[POC, n, s]*ConstantArray[1, {8, 8}] - POC,

<!-- b000577 | prose | pages [31] -->
Min[Part[POC, n, s]*ConstantArray[1, {8, 8}] - POC]];

<!-- b000578 | prose | pages [31] -->
If[Length[rnxt] > 1,

<!-- b000579 | prose | pages [31] -->
n = Part[Part[rnxt, If[Abs[n - Part[Part[rnxt, 1], 1]] > 1, 2, 1]],

<!-- b000580 | prose | pages [31] -->
1], n = Part[Part[rnxt, 1], 1]];

<!-- b000581 | prose | pages [31] -->
If[Length[rnxt] > 1,

<!-- b000582 | prose | pages [31] -->
s = Part[Part[rnxt, If[Abs[s - Part[Part[rnxt, 1], 2]] > 1, 2, 1]],

<!-- b000583 | prose | pages [31] -->
2], s = Part[Part[rnxt, 1], 2]]; i++; POC = POC; Print[" n=", n - 1, ", s=" , s - 1]]

<!-- b000584 | prose | pages [31] -->
n=1, s=4 n=2, s=3 n=2, s=4 n=3, s=3 n=3, s=4 n=1, s=5 n=1, s=2 n=2, s=2 n=2, s=5 n=4, s=4 n=4, s=3 n=3, s=2 n=3, s=5 n=4, s=5 n=4, s=2 n=1, s=3 n=1, s=6 n=1, s=1 n=1, s=4 n=5, s=3 n=5, s=2 n=5, s=5 n=5, s=4 n=2, s=6 n=2, s=1 n=6, s=4

<!-- b000585 | prose | pages [31] -->
31

<!-- b000586 | furniture | pages [32] -->
Team #39173

<!-- b000587 | furniture | pages [32] -->
Page 32 of 32

<!-- b000588 | prose | pages [32] -->
n=6, s=3 n=3, s=6 n=3, s=1 n=4, s=1 n=4, s=6 n=6, s=5 n=6, s=2 n=5, s=1 n=5, s=6 n=2, s=3 n=6, s=6 n=6, s=1 n=2, s=4 n=3, s=3 n=3, s=4 n=1, s=5 n=1, s=2 n=2, s=2 n=2, s=5 n=4, s=4 n=4, s=3 n=3, s=2 n=3, s=5 n=4, s=5 n=4, s=2 n=1, s=3 n=1, s=6 n=1, s=1 n=1, s=4 n=5, s=3 n=5, s=2 n=5, s=5 n=5, s=4

<!-- b000589 | prose | pages [32] -->
32
