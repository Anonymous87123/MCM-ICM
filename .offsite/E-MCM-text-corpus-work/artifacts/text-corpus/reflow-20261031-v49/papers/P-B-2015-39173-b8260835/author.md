Abstract

This paper proposes a model which determines the most probable locations of a missing transoceanic ﬂight traveling from point A to point B. Since transoceanic ﬂights are not detected by radar when they are more than 200 miles from a coast, radio communication and the occasional satellite imagery is essential to the construction of an eﬀective search plan. Our search plan is built oﬀthe last distance in miles on the intended ﬂight path (IFP) where Air Traﬃc Control heard from the pilot. We create a quadratic distance to casualty probability density function to predict the distance from the point of last contact to where the plane likely fell. Through trajectories and the possibility of veering oﬀthe IFP, a two-dimensional search region is determined and discretized into smaller areas. The trajectories account for any aircraft model, as parameters such as cruising altitude and Glide Ratio are assessed. Probabilities of containment (POC) are then assigned to each of these search areas, determining the probability the lost plane is within the given region.

We next consider the probabilities of detection (POD) during the search. We apply Koopman’s equation for the probability of detecting a missing boat. Furthermore, Koopman’s equation provides ﬂexibility to input appropriate values pertaining to a given model of search plane and its instrumentation. Upon determining POD, we create an algo- rithm to eﬀectively search the bounded area. Our algorithm applies the POD to the POC’s and redistributes probabilities if the search plane is not found in a region while still considering the chance that the plane was actually in the region searched. If the plane is not found in a given cell, the algorithm outputs a neighboring region to search next. This customized neighborhood search plan maximizes resources while remaining time-eﬃcient. An example of missing Transatlantic Flight ABCD is included as a demonstration of our methodology.

Our mathematically-derived search plan is built on a series of as- sumptions. These assumptions include that the IFP from point A to point B is linear and that the plane disassembled only upon impact- ing the water. Our model is sensitive to speciﬁc parameter changes but is therefore accommodating to diﬀerent plane types. Strengths of the model include non-uniform probability distributions modeling dis- tance to casualty and impact and a neighborhood-based, continuously- updating search mechanism.

1

2 Model

Our model considers a lost ﬂight, which starts at some location A and sets out to travel across the ocean linearly to its destination B. In order to develop an optimized search plan, we consider the proba- bilities of containment of the plane’s whereabouts, the probabilities of detecting the plane while eﬃciently and conservatively using resources, and the continuously updating probabilities of the most likely location of the missing airplane.

2.1 Constructing Probabilities of Containment

for a Missing Airplane and its Debris

The containment model maps the probability of the airplane’s con- tainment to speciﬁc regions surrounding the ﬂight’s last known posi- tion. Our ﬁrst consideration in the containment model is estimating how far the plane most likely travels after a signal is lost. The vari- able y0 is the last distance in miles from the starting location where

3 air traﬃc controllers heard from the pilot. In addition to the mileage covered, it is important to take note of the initial latitude and lon- gitude coordinates at y0. It is assumed that the plane stayed on its Intended Flight Path (IFP) at this time. At this location, it is un- clear if the plane continued traveling in the air or began falling to the ground. The Random Variable Yc refers to the distance to casualty, or the distance on the IFP at which the plane started to malfunction. It is assumed that when a plane malfunctions, its descent for the water begins. The distance to casualty is measured from y0 = 0. We have modeled the probability density function of Yc as follows:

( 3 (yB−yR)3 (yC −(yB −yR))2 : y0 ≤yC < yB −yR fyc(yc) = 0 : elsewhere

where yB indicates the remaining distance to destination B from y0 and yR is the ﬁnal mileage of the journey for which radar detection is available. Therefore, yB −yR represents the ﬂying distance left before Air-Traﬃc Control (ATC) radar detectors can spot the missing ﬂight.

Our Random Variable Yc is constructed under the assumption that it is more likely for the plane to reach a casualty-state immediately or soon after the last communication with ATC. This intuition is reason- able because a loss of communication often occurs due to abnormal plane operation. The probability continues to decrease quadratically and becomes 0 in the radar-detective zone. The parameter yR can be determined using the equation below:

(200)2 −h2 = p p 40, 000 −h2 yR =

where h is the cruising altitude in miles of the jet. Radar detectors can track planes within a 200 mile radius, on average (Hartmann), so yR can be determined by manipulating the Pythagorean Theorem.

We determine the possible locations where the airplane could have fallen based on a distribution of trajectories. The distance of impact, or the distance from y0 at which the airplane hit the water is YI. This variable takes into account the glide of the airplane and the distance at which it is completely submerged and is modeled as follows:

YI = YC + Gh where G is the glide ratio of the plane (NASA). Each airplane model has an average glide ratio which is deﬁned as

G = units of distance forward unit of distance downward. The glide ratio is multiplied by the cruising altitude to determine the horizontal distance the plane traveled during its downward fall

4 (NASA). The probability density function of YI can therefore be mod- eled using the following transformation of variables technique:

P(YI < yI) = P(YC + Gh < yI) P(YC < yI −Gh) = Z yI−Gh 3 (yC −(yB −yR))2dyC = (yB −yR)3 0 3 yI−Gh (yB −yR)3 [(yC −(yB −yR))2dyC] = 0 3 (yB −yR)3 ([(yI −Gh −yB + yR)2][(0 −yB + yR)2] =

fyI(yI) = d 3 (yB −yR)3 ([(yI −Gh −yB + yR)2][(0 −yB + yR)2] =⇒ dyI

After taking the derivative with respect to YI we can conclude that the probability density function for YI is:

( 3 (yB−yR)3 (yI −Gh −(yB −yR))2 : Gh ≤yI < yB −yR fyI(yI) = 0 : elsewhere

The probable distances from the point of lost contact to the point of impact are measured in line with the IFP. While this model has accounted for a single dimension, we can easily extend it to the left and to the right, indicating a plane’s maneuver oﬀcourse. The next portion of our model accounts for the possibility of veering oﬀthe intended linear path.

Veering away from the IFP is considered by assuming the segment of water representing the locations of impact are the average, or 0, and that the possible locations of the plane are normally distributed to the sides of yI.

5 IFP where a plane gliding π 8 oﬀcourse would land.

Standard deviation of the normal probability distribution is deter- mined by σx = Gh sin (π 8 ) Since it is unlikely that a plane veers beyond π 8 from the IFP, π 8 will be used to ﬁnd one standard deviation. Thus the normal probability distribution perpendicular to the IFP is:

−x2 2(Gh sin( π 8 ))2 e √ 2π : −∞< x < ∞ f(x) = Gh sin(π 8 )

Because f(x) and f(yI) are independent distributions, we can cre- ate a joint probability density function by multiplying f(x) and f(yI) as follows: f(x, yI) = f(x)f(yI).

−x2  3(yI−Gh−(yB−yR))2 2(Ghsin( π 8 ))2 : −∞< x < ∞, Gh ≤yI < yB −yR 2π(yB−yR)3 e  √ f(x, yI) = Gh sin π 8 0 : elsewhere 

2.1.1 Partitioning Search Region Through Model Dis-

cretization

Given f(x, yI), the search ﬁeld can be divided into distinct regions.

Each region is assigned a probability of containment (POC), indicating the probability that the region contains the missing plane and debris.

6 In order to discretize our model, we ﬁrst consider X, the normal ran- dom variable. Since 99.7% of all observations are contained within 3 standard deviations of the mean, our search region is bounded on both sides by three standard deviations. We segment yI over its entire range. Therefore, we consider N −1 partitions and N vertical regions through the following equation:

lyB −yR −Gh m N = t0.5vs where t0.5 represents the quantity 0.5 hours and vs is the velocity of the search plane.This guarantees that each search plane spends up to half an hour sweeping a length of each search region. Assuming more than one plane searches a given region at a time, these partitions lead to a highly eﬃcient search duration.

region matrix. Note that in this case N = 4.

To ﬁnd the probabilities of containment for each of the above rect- angular regions, the joint probability density function f(x, yI) must be integrated over each region’s boundaries. In order to ﬁnd N × 6 prob- ability values, a loop was created in Mathematica. The loop considers only the regions to the right of the IFP, since the normal distribu- tion has the property of symmetry. The loop iterates through all N partitions in YI given each of the 3 set X regions. Below is the algo- rithm for the probability generation of each region within 1 standard deviation of the IFP:

7 Z Gh sin( π Z 1( YB−YR−Gh 8 ) )+Gh N f(x, yI)dxdyI 0( YB−YR−Gh 0 )+Gh N

Z Gh sin( π Z 2( YB−YR−Gh 8 ) )+Gh N f(x, yI)dxdyI 1( YB−YR−Gh 0 )+Gh N

...

Z Gh sin( π Z N( YB−YR−Gh 8 ) )+Gh N f(x, yI)dxdyI (N−1)( YB−YR−Gh 0 )+Gh N The output of this loop is a list of probability values that can be matched to each of the search regions. Refer to Appendix B for the Mathematica Code. Now that we have determined probabilities of containment for each of these ocean search regions, we must obtain the boundaries of each region in latitude and longitude coordinates to facilitate the search and rescue team’s eﬀorts.

2.1.2 Finding Latitude and Longitude Coordinates for

Search Regions

Initially, the bounds of a given uniform probability region ru×l can be represented as 0 ≤u ≤N and −3 ≤l ≤3 where l, u are integer multiples of n = region number along the IFP, σx respectively.

In order to reference a discretized probability region to the IFP and y0, we must deﬁne a coordinate axis with a y-axis along the IFP,

8 an x-axis in the direction of σx and an origin at (yI, 0σx). Now the bounds of a region ru×l in miles are:

−l(Gh sin (π 8 )) ≤x ≤l(Gh sin (π 8 ))

and 0 ≤y ≤u(||yB −y0|| −Gh) . N To translate any given number m of zone-bounding coordinates in (x,y) to latitude and longitude, build a 2 × m matrix

C = [c1c2c3...cm]

where each bounding coordinate ci where 0 < i ≤m is of the form

cx  . cy

Next, using a rotation matrix, vector addition and vector scaling will eﬀectively shift an “IFP-referenced” coordinate to latitude and longi- tude. y0 and yB are known in the “IFP-referenced” system and in traditional coordinates. The components of yB −y0 in latitude and longitude are designated re, rn. To build a rotation matrix from the “IFP-referenced” system to latitude and longitude, we ﬁrst must ﬁnd the counter-clockwise angle φ between the two coordinate systems as follows: φ = arctan ( re ). rn Using φ, the rotation matrix R is either:

 cos φ  : π sin φ 2 ≤φ < 0 R = −sin φ cos φ

or cos φ  : 0 ≤φ ≤π −sin φ R = 2 . sin φ cos φ

One way to test whether the rotation matrix is calculated correctly is to verify that det(R) = 1. After ﬁnding a suitable R, multiply C by R to express every c in C in miles of latitude and longitude with reference to y0ρ where ρ is the average distance in miles of one degree North and one degree East from y0. Finally, add the resulting vector to y0 to have coordinates in degrees North and East. In summary, changing C in the “IFP-referenced” system to the corresponding coordinate matrix CL in latitude and longitude amounts to:

CL = ρRC + y0.

9

2.2 Probability of Detection

A standard model for ﬁnding the Probability of Detection (POD) is the exponential function

POD = 1 −e−coverage

where coverage is the area eﬀectively swept divided by the entire search area AS (Frost 1999). To determine our region’s POD, we use a slight variation of B.O. Koopman’s Exponential Model. The search area is deﬁned as 8 )(yB −yR −Gh AS = Gh sin(π ). N where the AS represents the area of a single partitioned region of the overall search region.The area eﬀectively swept is dependent on the eﬀective sweep width S and the eﬀort. The eﬀective sweep width depends on the eﬀective detection distance κϵ of the instrument (eg. human eyes, radar, etc.) used for the search, and the elevation of the cruising search plane is hs. We modify Koopman’s model to account for variations in weather, conditions, search abilities and more. This variation is denoted by the scalar κ, which takes values between 0 and 1. The distance from the search plane’s path projected on the ocean (κϵ)2 −h2s. Assuming the p to the furthest possible detected object is search plane ﬂies in parallel swaths, the eﬀective sweep width would be (κϵ)2 −h2s p S = 2

in order to detect all of AS. The eﬀort is said to be dsn where the distance searched by an individual aircraft per swath is ds and the number of search planes included in the search is n. Assuming the search plane ﬂies parallel to the IFP, the number of swaths the plane must ﬂy is the number of subregions N so ds is

ds = (yb −yr −Gh ). N

In order to search simultaneously and most eﬃciently, the planes are assumed to be ﬂying at the same velocity. Thus ds is the same for each plane since they begin searching simultaneously. Incorporating each of these components into a single model yields the following POD equation: dsn√ (κϵ)2−h2s −2 (yB−yR−Gh) Gh sin π POD = 1 −e 8 N

Unless search eﬀort is changed based on the search region, it is assumed that the POD is uniform among all regions of probable con- tainment.

10

2.3 The POC-Updating Algorithm

If there were no such thing as instrumentation error or human er- ror, POD would equal 1 and thus not adjust the POC’s of discretized zones. Since search conditions are nowhere near perfect, we assign 1 −PODq to be the probability that the lost plane in region q went undetected. Given that we do not ﬁnd the plane after searching the zone q, we update the POC in q to be

POCq′ = (POCq)(1 −PODq).

This is the probability that the plane is actually in the searched re- gion, even though it was not detected. Assuming that net probability of containment of all discretized zones is constant, the probability lost when POCq becomes POCq′ must be accounted for in the other regions. To do this, we add POCq −POCq′ 6N −1 to each of the POC values except POCq′. This process can be iterated during a search to update all the POC values per searched discrete probability zone.

2.3.1 Using the POC-Updating Algorithm to Determine

Search Pattern

To determine the best order to search the 6×N diﬀerent regions, we use the POC-updating algorithm described above using gradients to choose the next search region. By the ”best” order we mean the most eﬃcient in terms of resources and time. We want to spend the least amount of time and fuel covering the entire map. Thus we want to minimize ﬂight between nonadjacent regions because that increases less-useful or redundant coverage and increases time needed to cover the entire area. The search plan algorithm involves updating the POC map after completing the search of one region to ﬁnd the new proba- bility of containment map, given the downed aircraft was not detected in the recently-searched region. Using a matrix in Mathematica we represent the map of POC’s. A loop was created in Mathematica to evaluate, for each iteration, the diﬀerences between the updated POC’s of the just-searched region k and its adjacent neighbors. We take the minimum of the diﬀerences, and then locate the row nnew and column σnew of that minimum element, to ﬁnd the next region rnnew,σnew to be searched. Essentially this method consists of up- dating the POC matrix, calculating a gradient/diﬀerence to identify the highest adjacent POC, and taking that region as the next to be searched.

11

2.4 Assumptions in the Methodology

There are several assumptions upon which our model and the re- sulting search plan are built. Below is a list of assumptions we con- sider:

• The lost plane’s pre-established course is a linear path from point A to point B.

• The lost plane’s glide aﬀects its trajectory into the ocean. The plane does not explode in the sky.

• Any debris disassembles upon impacting the water.

• The plane will not veer more than 3Ghsin(π 8 ) oﬀthe IFP.

• There are no forces (eg. currents) to move the debris or plane from where they ﬁrst landed.

• All planes (lost plane and search plane(s)) in the model are ﬂying at a constant velocity.

• The lost plane is more likely to be found near the last point of communication.

• The lost plane remains aﬂoat (detectable) during the entire time the search is in action.

• Every searching plane has the same instrumentation, searches at the same speed and ﬂies at the same altitude.

2.5 Sensitivity Analysis

In order to test how changing parameters eﬀect our model, we include a discussion of the relationships between speciﬁc parameters and their eﬀects on the components of our model and search plan.

We assess the impacts of changing parameters on f(x, yI) by con- sidering f(G) and f(θ). From experimentation with ﬁxing the random variables x and yI, the shape of the curve of f(G), and f(θ) are strik- ingly similar.

12 and f(θ) regardless of the x and yI values

As G and θ increase, the respective f(G) and f(θ) exhibit a rapid decrease. Since the bounded integral of f(x, y) produces a POC, G and θ have the same eﬀect on POC as they do on f(x, y). In short, as G + θ decreases, the probability of ﬁnding the lost plane increases.

Increasing θ will directly increase the search area because the X distance is measured in mile-multiples of σx = Gh sin (θ) which is pro- portional to a chosen 0 ≤θ ≤π 2 . The following graphs are generated using the constant parameter values found in the Working Example (Section 3).

As θ increases, POD rapidly decreases from one to zero. The most intriguing part of POD(θ) is that the graph suggests POD(0) ≈1.

Also, the POD is extremely small for any plane that has veered more than ninety degrees oﬀthe IFP.

Increasing the glide ratio eﬀects the POD similarly to increasing θ.

13 Increasing the exponent’s denominator will have an inverse eﬀect on the POD. Thus, a search party following the methodology explained in the Working Example will be more likely to ﬁnd a plane with a small glide ratio.

Another variable that clearly eﬀects the search plan is the cruising altitude, hS, at which the search plane ﬂies because the POD depends κϵ2 −h2s. Varying hs within 0 ≤hs < ϵ produces an elliptic p on graph of POD centered around the origin:

increases, the POD increases. ϵ This is a logical relationship because each swath will cover more ground which will in turn decrease the search eﬀort. Thus, it is best to run the search at the lowest possible altitude in order to improve the chance of ﬁnding the lost plane.

The number of search planes n also eﬀect the POD because the search eﬀort n is in the numerator of the search eﬀort fraction. Illus- trated graphically:

14 In a practical sense, incorporating more search planes will increase the likelihood of detection.

(κϵ)2 −h2s there p Since the POD equation contains the element may be a square root of a negative number if h2 s > (κϵ)2. A plane must ﬂy low enough for the eﬀective range of the instrumentation (κϵ) to reach the ground. Otherwise there is no chance the plane will detect anything below it and thus the POD would be eﬀectively zero.

s > (κϵ)2 there is no point in searching until conditions Thus when h2 improve.

Clearly, our model is sensitive to changes in several of the parame- ters and therefore may not be considered a robust probabilistic model. However, the sensitivity to changes in the input parameters is neces- sary to have a model that is accommodating to the speciﬁcations of diﬀerent types of planes and search instruments.

2.6 Strengths and Weaknesses of Our Model

2.6.1 Strengths

Our outlined model has particular strengths, unavailable in other Search and Rescue methods. First, we use a quadratic probability density function rather than the commonly-used uniform distribution. In many Search and Rescue Methodologies, it is assumed that the time of casualty is uniformly distributed over all possible times in a given range (Lawrence 1977). Here, we carefully construct a decreasing, concave down distribution to account for the large likelihood that complications arise early after y0. Our model also accounts for a ﬂight trajectory to map the ﬂight’s motion at the time of casualty to a region of the ocean surface. The change of bases allows the searchers to locate the search regions using actual latitude, longitude coordinates rather than tracking angles and distances from the point of lost contact. The POD incorporates several factors, including an added constant k.

15 When k = 1, the search occurs in perfect conditions, while k = 0.5 may indicate some fog, choppy water, or other inhibiting factors. This constant helps to better explain the rate of coverage while still using Koopman’s commonly-used Exponential Model.

Our search plan is a constantly updating algorithm keeping time eﬃciency in mind. If an item is not detected in a highly probable re- gion, the POC’s of the other search regions are updated. The cell with the next highest probability in the searched region’s “neighborhood” is investigated. Implementing a neighborhood restriction speeds up the search process, wasting no travel time while still searching regions with high POC’s. Our search plan can easily be generalized to search planes of diﬀerent speeds and larger or smaller regions of the ocean.

2.6.2 Weaknesses

It is important to consider the weaknesses of our model that may be worth addressing in the future. First, the POC of the regions closest to Gh but more than 1 standard deviation away in the X direction are slightly over-allocated. The standard deviation was calculated using trigonometry, indicating that our rectangular probability region is based on a triangular calculation. Refer to Figure 1. Because of this over-allocation, there is a slight under-calculation of probabilities 1 or more standard deviations away from the IFP towards the latter partitions of YI.

Another weakness to consider is the lack of consideration of cur- rents in each of our partitioned search regions. With more time, we hope to extend the impacts of surface currents to locating debris and other remnants of the aircraft.

3 Working Example: Flight ABCD to

Lisbon, Portugal Reported Missing

16 Imagine that on February 9, 2015 Flight ABCD from Boston, MA to Lisbon Portugal disappeared on a Boeing 777 aircraft. The point of last communication occurred at coordinates 40.9275◦N, 46.2575◦ W. Let yB = 1, 912 miles. The plane was cruising at a speed of 560 miles per hour at an altitude of 40, 000 feet (7.58 miles), so yR = 199.86. Assume that the ﬂight is entirely over open ocean and the Lisbon airport is the nearest location to y0 that can detect an airplane. So, yR is measured from the Lisbon airport along the IFP. Below is the probability distribution of YC, the random variable representing the probability that at a given distance in the direction of the IFP the plane experiences a casualty that causes it to begin a downward trajectory.

( 3 (1912−199.86)3 (yC −(1912 −199.86))2 : 0 ≤yC < 1712.14 fyc(yc) = 0 : elsewhere

This airplane has a glide ratio of approximately 19 : 1, similar to other large aircrafts. With this information, yI can be modeled as follows:

( 3 (1712.14)3 (yI −1568.12)2 : 144.02 ≤yI < 1712.14 fyI(yI) = 0 : elsewhere

After considering the distribution of distances of impact, we must now account for the possibility of veering oﬀthe IFP. The following X distribution, distributed in the direction perpendicular to the intended ﬂight path, accounts for Flight ABCD’s potential oﬀ-course location of impact:

−x2 2(144.02 sin( π 8 ))2 e √ 2π : −∞< x < ∞ f(x) = 144.02 sin(π 8 )

17 By multiplying the independent equations f(x) ∗f(yI), a joint probability density function is obtained.

−x2  3(yI−1568.12)2 2(144.02 sin( π 8 ))2 : −∞< x < ∞, 144.02 ≤yI < 1712.14 2π(1712.14)3 e  √ f(x, yI) = 144.02 sin( π 8 ) 0 : elsewhere 

in which the POC is largest, and locations where the POC is smallest

Now, the multi-dimensional probability distribution, POC, can be discretized into 36 subregion each calculated by a double integral, as described in section 2.1.1 Partitioning Search Regions Through Model Discretization.

18 Next, the Probability of Detection is found by the formula as de- scribed in the section 2.2:

2∗dsn√ (kϵ)2−h2s − Gh sin π POD = 1 −e 8 (yB−yR−Gh)/N

The list of parameters for this model, either estimated or researched values, is as follows:

• Remaining distance of ﬂight from y0 to yR, yB = 1912

• Glide constant for a large plane such as a a Boeing 777-200, G = 19

19 • Average altitude at which a commercial airliner cruises, h = 7.58 √ 2002 −h2

• yR =

• Velocity of the search planes (all of which are the same model in order to facilitate easier coordination and timing in the search), vs = 550

• t.05 = .5 hours l m yB−yR−Gh

• The number of partitions in the y direction, N = t.05vs

• Distance traveled by search planes in searching a single region, ds = (yB−yR−Gh) np

• Detection distance of instrument, ϵ = 4

• Scales detection distance based on search conditions such as weather, κ = 0.98, note < 0κ < 1. In this case, κ is near one, indicating clear calm search conditions.

• Number of search planes n, chosen in this example to be 8.

• Then, POD = 0.677831 for our example, when we plug in all the variables

Taking the values in Figure 11, we input them to Mathematica to form the initial POC matrix. We then utilize the method described in section 2.3 and subsection 2.3.1, and the Mathematica code in Ap- pendix C, to determine the order and path of the most eﬃcient search pattern. We also utilize the model to update probabilities that certain regions contain the lost plane given the plane was not detected when the an area was most recently searched.

20 gorithm and described by the output of the Mathematica code in Appendix C.

21 rithm similar to ours but without requiring subsequent search regions to be adjacent. The code for this algorithm is contained in Appendix D.

By comparing the two ﬁgures above, we can observe some key diﬀerences. When adjacency is not a requirement in our algorithm, frequently the subsequent search region is the reﬂection of the previous due to the symmetry of the joint probability distribution across the IFP. This leads to much more back-and-forth movement, and as a result, more distance traveled, thus wasting time and fuel.

To search a certain region, that region must be described in Lati- tude and Longitude. Continuing with the example, say the region in in need of searching is the discrete probability zone σ, N from 2 to 3. The algorithm from Section 2.3 in action is as follows: First, the rotation matrix:

 cos φ  0.9983  −0.0579 sin φ = −sin φ cos φ 0.0579 0.9983

is deﬁned using the rotation angle φ = −0.057939. It calculates the four latitude and longitude bounding coordinates of the rectangular search region σ, N from 2 to 3 as:

22 See Appendix B for the Excel tables used for the calculation.

4 Conclusion

The ﬁnal results of our model present a valid, time-eﬃcient search plan for locating missing ﬂight ABCD from Boston to Portugal. Our methodology accounts for all sizes and types of airplanes as well as all types of search planes. Our sensitivity analysis stresses the impor- tance of careful consideration of resources and the number of search planes. A greater number of search planes drastically increases the probability of detecting the missing plane. While some parameters are more robust than others, carefully choosing the number of search planes per square will optimize time-eﬃciency and overall detection. Our neighborhood-based search plan makes this model a strong choice when considering especially large search regions. While we did not have time, we hoped to incorporate the impacts of currents in the movement of airplane debris. We plan to further explore this topic to eventually extend our model to account for debris search plans too.

5 Summary for an Airline’s Press Con-

ference

There has been a new model proposed for locating missing transoceanic ﬂights, such as Malaysian Flight 370. Since 1948, 83 aircrafts have vanished, some of which have still not been found (Bloomberg). In the case of Malaysian ﬂight 370, not enough information was available on the plane’s modiﬁed path, to eﬀectively use the Search and Res- cue models currently in place(Seidel). This new mathematical model narrows the search region of missing planes and predicts their loca- tion of impact with the water, considering deviations from their in- tended paths. The model incorporates a time-eﬃcient search method, allocating time and eﬀort to the most likely locations of a missing transoceanic ﬂight traveling from point A to point B.

Since transoceanic ﬂights are not detected by radar when they are more than 200 miles from a coast, radio communication and the oc- casional satellite imagery is important in tracking the oﬀ-the-radar

23 plane. These mathematicians created a search plan which is based on the last distance in miles on the intended ﬂight path (IFP) where Air Traﬃc Control heard from the pilot. The mathematicians assign probabilities to diﬀerent search regions. The model accounts for the likelihood that the plane fell closer to the distance of last contact rather than farther away, since loss of contact often indicates a me- chanical issue or takeover of the plane. They use physics, primarily modeling the gliding of planes from the sky, to determine a search area. The trajectories of the planes falling from the sky can be calcu- lated for any aircraft model, as they determine these distances using measurements of the cruising altitude and the Glide Ratio of a given plane. Basically, after performing several calculations, Probabilities of containment (POC) are assigned to each of these search areas. The probabilities will tell searchers how likely it is that the missing plane (or its parts) lie in that region.

After mapping the likelihoods that the plane is in each of the re- gions, the mathematicians account for the probabilities that the search equipment will actually detect the plane. The simple equation for the probability of detection makes it easy to quickly input values like the speed of a search plane, a search plane’s radius, the number of search planes and more. If this probability is not as high as the team would like, it can easily be increased by adding more search parties to the team.

Once the searchers know their probability of detecting the lost plane, the mathematicians use a new algorithm to search the bounded area. This algorithm applies the probability of detecting the plane to each rectangular region which has a certain chance of containing the plane. If a plane is not found in a given region, the algorithm determines an appropriate neighboring region to search, making the search plan very time eﬃcient, and the process continues until the plane is located. There is still a chance that the plane was missed in a given region, so the search plan includes the possibility of revisiting certain areas later on. This customized neighborhood search plan maximizes resources while remaining time-eﬃcient.

Of course we must use this search plan with a few restrictions in mind. If the path from destination A to destination B is not a straight line, this method becomes more diﬃcult to use. The mathematicians note that while statistics are an incredibly powerful tool, there are always assumptions to consider, such as up to how far the plane could have veered from its intended path. This model is a breakthrough in Search and Rescue Theory and will be implemented when needed in the future.

24

6 Appendix A

Mathematica Code for Probability Generation:

np = Ceiling[(yb - yr - G*h)/(t05*vs)]

For[n = 1, n < 7, n++, discretefxyi = Integrate[ Integrate[ f[x, yi], {yi, (n - 1)*(yb - yr - G*h)/np, n*(yb - yr - G*h)/np}], {x, 0, G*h*Sin[Pi/8]}]; Print[discretefxyi // N]]

For[n = 1, n < 7, n++, discretefxyi = Integrate[ Integrate[ f[x, yi], {yi, (n - 1)*(yb - yr - G*h)/np, n*(yb - yr - G*h)/np}], {x, G*h*Sin[Pi/8], 2*G*h*Sin[Pi/8]}];

25 Print[discretefxyi // N]]

For[n = 1, n < 7, n++, discretefxyi = Integrate[ Integrate[ f[x, yi], {yi, (n - 1)*(yb - yr - G*h)/np, n*(yb - yr - G*h)/np}], {x, 2*G*h*Sin[Pi/8], 3*G*h*Sin[Pi/8]}]; Print[discretefxyi // N]]

Excel tables used to shift from IFP referenced search regions to Lati- tude and Longitude.

7 Appendix B

26

8 Appendix C

Set up parameters and deﬁne POC matrix:

yb = 1912; G = 19; h = 7.58; yr = Sqrt[200^2 - h^2]; t05 = .5; vs = 550; ds = (yb - yr - G*h)/np; epsilon = 4; kappa = .98; hs = 2000/5280; np = Ceiling[(yb - yr - G*h)/(t05*vs)]; sp = 8;

POCn1s1 = 0.13367; POCn2s1 = 0.09323; POCn3s1 = 0.06008; POCn4s1 = 0.03421; POCn5

POCn1s2 = 0.05322; POCn2s2 = 0.03712; POCn3s2 = 0.02392; POCn4s2 = 0.01362; POCn5

POCn1s3 = 0.00838; POCn2s3 = 0.00585; POCn3s3 = 0.00377; POCn4s3 = 0.00214; POCn5

POCn1negs1 = 0.13367; POCn2negs1 = 0.09323; POCn3negs1 = 0.06008; POCn4negs1 = 0.

POCn1negs2 = 0.05322; POCn2negs2 = 0.03712; POCn3negs2 = 0.02392; POCn4negs2 = 0.

POCn1negs3 = 0.00838; POCn2negs3 = 0.00585; POCn3negs3 = 0.00377; POCn4negs3 = 0.

POC = {{0, 0, 0, 0, 0, 0, 0, 0}, {0, POCn1negs3, POCn1negs2, POCn1negs1, POCn1s1, POCn1s2, POCn1s3, 0}, {0, POCn2negs3, POCn2negs2, POCn2negs1, POCn2s1, POCn2s2, POCn2s3, 0}, {0, POCn3negs3, POCn3negs2, POCn3negs1, POCn3s1, POCn3s2, POCn3s3, 0}, {0, POCn4negs3, POCn4negs2, POCn4negs1, POCn4s1, POCn4s2, POCn4s3, 0}, {0, POCn5negs3, POCn5negs2, POCn5negs1, POCn5s1, POCn5s2, POCn5s3, 0}, {0, POCn6negs3, POCn6negs2, POCn6negs1, POCn6s1, POCn6s2, POCn6s3, 0}, {0, 0, 0, 0, 0, 0, 0, 0}};

POD = 1 - Exp[-((2*sp*ds*Sqrt[(k*epsilon)^2 - hs^2])/( G*h*Sin[Pi/8] (yb - yr - G*h)/np))]

27 Loop for determining the order in which we will search regions without the requirement of adjacency; build loop with initial condi- tions as the highest or one of the highest initial POC regions:

n = 2; s = 4; i = 1; POC = {{0, 0, 0, 0, 0, 0, 0, 0}, {0, POCn1negs3, POCn1negs2, POCn1negs1, POCn1s1, POCn1s2, POCn1s3, 0}, {0, POCn2negs3, POCn2negs2, POCn2negs1, POCn2s1, POCn2s2, POCn2s3, 0}, {0, POCn3negs3, POCn3negs2, POCn3negs1, POCn3s1, POCn3s2, POCn3s3,0}, {0, POCn4negs3, POCn4negs2, POCn4negs1, POCn4s1,POCn4s2, POCn4s3, 0}, {0, POCn5negs3, POCn5negs2,POCn5negs1, POCn5s1,POCn5s2, POCn5s3, 0}, {0,POCn6negs3, POCn6negs2, POCn6negs1, POCn6s1,POCn6s2,POCn6s3, 0}, {0, 0, 0, 0, 0, 0, 0, 0}};

While[1 < n < 7; 1 < s < 7; 0 < i < 60,

POC = (POC - Normal[SparseArray[{{n, s} -> POC[[n, s]]}, {8, 8}]] + Normal[SparseArray[{{n, s} -> (POC[[n, s]]*(1 - POD))}, {8, 8}]]) + (Ceiling[ POC - Normal[SparseArray[{{n, s} -> POC[[n, s]]}, {8, 8}]]]*( POC[[n, s]] - (POC[[n, s]]) (1 - POD))/(6*np - 1)); Min[Part[POC, n, s]*ConstantArray[1, {3, 3}] - Part[POC, n - 1 ;; n + 1, s - 1 ;; s + 1]];

rnxt = Position[Part[POC, n, s]*ConstantArray[1, {8, 8}] - POC, Min[Part[POC, n, s]*ConstantArray[1, {3, 3}] - Part[POC, n - 1 ;; n + 1, s - 1 ;; s + 1]]];

If[Length[rnxt] > 1, n = Part[Part[rnxt, If[Abs[n - Part[Part[rnxt, 1], 1]] > 1, 2, 1]], 1], n = Part[Part[rnxt, 1], 1]];

If[Length[rnxt] > 1, s = Part[Part[rnxt, If[Abs[s - Part[Part[rnxt, 1], 2]] > 1, 2, 1]], 2], s = Part[Part[rnxt, 1], 2]];

i++; POC = POC; Print[" n=", n - 1, ", s=" , s - 1]]

28 Output:

n=1, s=4 n=2, s=3 n=2, s=4 n=3, s=3 n=3, s=4 n=2, s=5 n=1, s=5 n=1, s=4 n=1, s=3 n=1, s=2 n=2, s=2 n=2, s=3 n=3, s=2 n=4, s=3 n=4, s=4 n=3, s=5 n=2, s=4 n=3, s=3 n=4, s=2 n=5, s=2 n=5, s=3 n=5, s=4 n=4, s=5 n=3, s=4 n=2, s=5 n=1, s=6 n=1, s=5 n=2, s=6 n=3, s=6 n=4, s=6 n=5, s=5 n=6, s=4 n=6, s=3 n=6, s=2 n=5, s=1 n=4, s=1 n=3, s=1 n=2, s=1 n=1, s=1 n=1, s=2 n=1, s=3 n=1, s=4

29 n=2, s=3 n=2, s=2 n=3, s=2 n=4, s=3 n=4, s=4 n=3, s=5 n=2, s=4 n=3, s=3 n=4, s=2 n=5, s=2 n=6, s=1 n=6, s=2 n=5, s=3 n=5, s=4 n=6, s=5 n=5, s=6 n=6, s=6

9 Appendix D

Loop for determining the order in which we will search regions without the requirement of adjacency:

n = 2; s = 4; i = 1; POC = {{0, 0, 0, 0, 0, 0, 0, 0}, {0, POCn1negs3, POCn1negs2, POCn1negs1, POCn1s1, POCn1s2, POCn1s3, 0}, {0, POCn2negs3, POCn2negs2, POCn2negs1, POCn2s1, POCn2s2, POCn2s3, 0}, {0, POCn3negs3, POCn3negs2, POCn3negs1, POCn3s1, POCn3s2, POCn3s3,0}, {0, POCn4negs3, POCn4negs2, POCn4negs1, POCn4s1,POCn4s2, POCn4s3, 0}, {0, POCn5negs3, POCn5negs2,POCn5negs1, POCn5s1,POCn5s2, POCn5s3, 0}, {0,POCn6negs3, POCn6negs2, POCn6negs1, POCn6s1,POCn6s2,POCn6s3, 0}, {0, 0, 0, 0, 0, 0, 0, 0}};

While[1 < n < 7; 1 < s < 7; 0 < i < 60,

POC = (POC - Normal[SparseArray[{{n, s} -> POC[[n, s]]}, {8, 8}]] + Normal[SparseArray[{{n, s} -> (POC[[n, s]]*(1 - POD))}, {8,

30 8}]]) + (Ceiling[ POC - Normal[SparseArray[{{n, s} -> POC[[n, s]]}, {8, 8}]]]*( POC[[n, s]] - (POC[[n, s]]) (1 - POD))/(6*np - 1)); Min[Part[POC, n, s]*ConstantArray[1, {8, 8}] - POC];

rnxt = Position[Part[POC, n, s]*ConstantArray[1, {8, 8}] - POC, Min[Part[POC, n, s]*ConstantArray[1, {8, 8}] - POC]];

If[Length[rnxt] > 1, n = Part[Part[rnxt, If[Abs[n - Part[Part[rnxt, 1], 1]] > 1, 2, 1]], 1], n = Part[Part[rnxt, 1], 1]];

If[Length[rnxt] > 1, s = Part[Part[rnxt, If[Abs[s - Part[Part[rnxt, 1], 2]] > 1, 2, 1]], 2], s = Part[Part[rnxt, 1], 2]]; i++; POC = POC; Print[" n=", n - 1, ", s=" , s - 1]]

n=1, s=4 n=2, s=3 n=2, s=4 n=3, s=3 n=3, s=4 n=1, s=5 n=1, s=2 n=2, s=2 n=2, s=5 n=4, s=4 n=4, s=3 n=3, s=2 n=3, s=5 n=4, s=5 n=4, s=2 n=1, s=3 n=1, s=6 n=1, s=1 n=1, s=4 n=5, s=3 n=5, s=2 n=5, s=5 n=5, s=4 n=2, s=6 n=2, s=1 n=6, s=4

31 n=6, s=3 n=3, s=6 n=3, s=1 n=4, s=1 n=4, s=6 n=6, s=5 n=6, s=2 n=5, s=1 n=5, s=6 n=2, s=3 n=6, s=6 n=6, s=1 n=2, s=4 n=3, s=3 n=3, s=4 n=1, s=5 n=1, s=2 n=2, s=2 n=2, s=5 n=4, s=4 n=4, s=3 n=3, s=2 n=3, s=5 n=4, s=5 n=4, s=2 n=1, s=3 n=1, s=6 n=1, s=1 n=1, s=4 n=5, s=3 n=5, s=2 n=5, s=5 n=5, s=4

32
