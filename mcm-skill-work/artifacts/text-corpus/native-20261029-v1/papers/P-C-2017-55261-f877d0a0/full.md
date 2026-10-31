# P-C-2017-55261-f877d0a0

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For office use only

<!-- b000003 | prose | pages [1] -->
For office use only

<!-- b000004 | title | pages [1] -->
55261

<!-- b000005 | prose | pages [1] -->
T1 ________________

<!-- b000006 | furniture | pages [1] -->


<!-- b000007 | prose | pages [1] -->
T2 ________________

<!-- b000008 | prose | pages [1] -->
F1 ________________

<!-- b000009 | prose | pages [1] -->
F2 ________________

<!-- b000010 | prose | pages [1] -->
Problem Chosen

<!-- b000011 | prose | pages [1] -->
T3 ________________

<!-- b000012 | prose | pages [1] -->
F3 ________________

<!-- b000013 | title | pages [1] -->
C

<!-- b000014 | prose | pages [1] -->
T4 ________________

<!-- b000015 | furniture | pages [1] -->


<!-- b000016 | prose | pages [1] -->
F4 ________________

<!-- b000017 | furniture | pages [1] -->


<!-- b000018 | title | pages [1] -->
2017

<!-- b000019 | prose | pages [1] -->
MCM/ICM

<!-- b000020 | heading | pages [1] -->
Summary Sheet

<!-- b000021 | furniture | pages [1] -->


<!-- b000022 | furniture | pages [1] -->


<!-- b000023 | prose | pages [1] -->
Once the stuff of wildly speculative science fiction novels, self-driving and cooperative vehicles are now at the cusp of mainstream adoption. As this technology comes closer to the point of deployment on real roads amongst conventional vehicles, it is necessary to understand how it will affect the characteristics and behavior of transportation systems worldwide. Seattle, WA and the surrounding King County area are prime subjects for investigation of this question, with traffic in the region being a chronic problem due to overcrowded roads and a high commuter population. In this paper, we aim to identify key impacts on the everyday experiences of highway travellers of the proporiton of self-driving and/or cooperative vehicles on the road, and use our findings to inform suggestions to policy makers.

<!-- b000024 | prose | pages [1] -->
Our solution consists of three main sections. In the first, we propose a macroscopic (continuum) model for the relationship between traffic flow, density, and mean speed. In addition to an improved justifiability over traditional empirical models, ours also allows for a straightfoward adjustment to reflect the percentage of self-driving/cooperative vehicles present. We find that at a given density of cars on the road, traffic flow and average speed increase fairly uniformly with that parameter, and show how an increase in overall number of cars on the road is likely to negate this beneficial effect.

<!-- b000025 | prose | pages [1] -->
Secondly, we develop a discrete model to describe lane changing dynamics in various levels of traffic, as well as how the performance of conventional, self-driving/non-

<!-- b000026 | heading | pages [1] -->
interacting, and self-driving/cooperative cars compare in these cases. Our results indicate

<!-- b000027 | prose | pages [1] -->
that the presence of self-driving cars on a highway can significantly decrease the average time required to find a sufficient gap when merging or changing lanes, with the greatest advantages arising for self-driving, cooperative cars. We also find that even interactions between conventional and autonomous vehicles can experience reduced delays during a lane change event.

<!-- b000028 | prose | pages [1] -->
Lastly, we test our model for the flow-density-mean speed relations on the real-world data provided in the problem. Although experimental traffic flows tend to be systematically higher than predicted by the theory (even after adjustment of certain key input parameters), the output generally confirms expected trends and enables us to identify times and locations of increased flux of vehicles onto or off of the highway.

<!-- b000029 | furniture | pages [1] -->


<!-- b000030 | furniture | pages [1] -->


<!-- b000031 | furniture | pages [1] -->


<!-- b000032 | furniture | pages [2] -->
Team #55261

<!-- b000033 | furniture | pages [2] -->
Page 1 of 28

<!-- b000034 | prose | pages [2] -->
Driving Towards the Future:

<!-- b000035 | heading | pages [2] -->
Modeling the Impact of Driverless

<!-- b000036 | prose | pages [2] -->
Vehicles on Traﬃc Patterns

<!-- b000037 | heading | pages [2] -->
Letter to the Governor

<!-- b000038 | prose | pages [2] -->
Dear Governor Inslee,

<!-- b000039 | prose | pages [2] -->
We are glad to hear that your administration is seeking out a diverse range of opinions in an eﬀort to inform policy making in your state around self-driving and cooperative vehicles. As America moves further into the 21st century, the pervasiveness and rapid advancement of technology in nearly every aspect of daily life can sometimes feel daunting. For example, in the case of driverless cars, it is not a trivial matter to assess potential risks and rewards for individual drivers and for society as a whole.

<!-- b000040 | prose | pages [2] -->
While we are far from providing a comprehensive study of this issue in our model for the eﬀect of driverless vehicles on traﬃc patterns, we feel that a few of our central results can provide some insight for lawmakers seeking to craft laws and regulations, make decisions about investment in certain infrastructures, and communicate eﬀectively with constituents about the eﬀects of self-driving cars on our roads.

<!-- b000041 | prose | pages [2] -->
The ﬁrst of these is that although increasing the amount of self-driving cars as a percentage of vehicles on highways is projected to relieve the burden of heavy traﬃc to some extent, these beneﬁts would quite likely be outweighed if the total number of vehicles were to increase. In other words, even if relaxing the driving age for these vehicles or providing tax incentives to use them may seem promising politically, these are actions which might encourage more people to drive, which has the potential to worsen overall traﬃc conditions.

<!-- b000042 | prose | pages [2] -->
That being said, our models indicate that self-driving and/or cooperative cars far outperform conventional drivers when it comes to changing lanes and merg- ing, which is a principle cause of delay on highways. We also show that, as would be expected, the ﬂux of vehicles onto or oﬀof highways increases dramatically during rush hours. These ﬁndings would indicate that oﬀering designated lanes for carpoolers in driverless vehicles during peak periods might mitigate jams while also promoting eﬃcient use of resources.

<!-- b000043 | prose | pages [2] -->
We hope you will ﬁnd this report riveting and that it will be helpful for you and your staﬀas you grapple with the legal complications of this new and exciting technology. We wish you the best in your endeavors.

<!-- b000044 | prose | pages [2] -->
Respectfully, Team 55261

<!-- b000045 | prose | pages [2] -->
1

<!-- b000046 | furniture | pages [3] -->
Team #55261

<!-- b000047 | furniture | pages [3] -->
Page 2 of 28

<!-- b000048 | heading | pages [3] -->
Solution

<!-- b000049 | prose | pages [3] -->
Restatement and Clariﬁcation of the Problem

<!-- b000050 | prose | pages [3] -->
As the city of Seattle (and the broader King County area) reckon with the chal- lenges of adapting infrastructure designed and built in the late 20th century to current 21st century demands, technological advances such as self-driving, co- operative vehicles may oﬀer some respite. However, before investing signiﬁcant time and resources in accommodating such vehicles, it is desirable to know to what extent they are capable of mitigating the traﬃc jams that occur with some regularity on busy commuter highways. Here, we investigate the eﬀect of the ratio of self-driving and/or cooperative vehicles to conventional vehicles on the road, with the goal of identifying points of either diminishing or particularly increased returns with respect to improving traﬃc ﬂow. This is accomplished by developing a model for traﬃc ﬂow as a function of volume demand and road capacity, and subsequently applying the model to real-world data. *Note that throughout this paper, numbers in square brackets are citations to listed references and those in parentheses refer to the numbered equations.

<!-- b000051 | heading | pages [3] -->
Assumptions and Justiﬁcations

<!-- b000052 | prose | pages [3] -->
In the literature of traﬃc ﬂow modeling, there are three general paradigms: microscopic, mesoscopic, and macroscopic [1, 2, 3, 4]. These paradigms treat traﬃc as discreet vehicles, modular groups of vehicles, or a continuous ﬂow of vehicles, respectively. In the ﬁrst part of our model, designed to describe broader trends and patterns in traﬃc ﬂow, we chose to analyze the problem from the macroscopic view, for the following reasons. First, the data provided are not granular enough to be easily applied to microscopic formulae (i.e. behavior of individual cars/drivers); second, the structure of equations in the macroscopic model are more amenable to numerical analysis such as ﬁnite diﬀerence methods; third, the macroscopic paradigm is well-established in the ﬁeld of traﬃc ﬂow modeling and we therefore reason that it has at least a baseline capability to describe emergent patterns [1, 2, 3]. This is the main assumption shaping the basic structure of our ﬁrst model.

<!-- b000053 | prose | pages [3] -->
The second part of our model, designed to describe lane changing behavior, we consider the interaction of individual vehicles on the microscopic level. In this context the microscopic approach makes more sense, because a change in lane is a discreet event.

<!-- b000054 | prose | pages [3] -->
Additional assumptions are listed below, and while we provide justiﬁcation for all of them, they could generally be adjusted to reﬂect more realistic condi- tions, given additional time and computing resources.

<!-- b000055 | prose | pages [3] -->
• The distribution of traﬃc ﬂow over a 24-hour daily period is not uniform.

<!-- b000056 | caption | pages [3] -->
Figure 1 shows the typical variation of traﬃc volume versus time of day

<!-- b000057 | prose | pages [3] -->
for weekends, weekdays, and an average.

<!-- b000058 | prose | pages [3] -->
Both the average and week- day curves were consistent with the statement given in the problem that roughly 8% of traﬃc volume occurs during peak hours, so we arbitrarily selected the curve for weekdays.

<!-- b000059 | prose | pages [3] -->
• Given average daily traﬃc counts did not specify direction, and therefore it is necessary to make an assumption here. On any given day, a certain

<!-- b000060 | prose | pages [3] -->
2

<!-- b000061 | furniture | pages [4] -->
Team #55261

<!-- b000062 | furniture | pages [4] -->
Page 3 of 28

<!-- b000063 | caption | pages [4] -->
Figure 1: Plot of typical traﬃc volume versus hour of day from a traﬃc sensor

<!-- b000064 | prose | pages [4] -->
stationed at a Seattle viaduct. Taken from [5].

<!-- b000065 | prose | pages [4] -->
proportion of drivers will be commuters (ie, intending to make a round trip), and a certain portion passing through to other destinations. We feel it is fair to assume that the drivers passing though will be distributed evenly between the ”increasing” and ”decreasing” directions (as deﬁned in the problem statement). The distribution among commuters is not as straightforward, since presumably a diﬀerent number commute out of the central metropolitan area than into it. However, based on the fact that the highways of interest are generally centered around downtown Seattle, as well as census data indicating that the majority (92% ± 0.7%) of com- muters to locations in King County are from King County [6], justify an approximation that traﬃc volume is also divided evenly between the two directions for commuter vehicles. In absence of a more reliable statistic, we used this assumption when analyzing the data, but this could be easily adjusted if desired.

<!-- b000066 | prose | pages [4] -->
• We were not able to ﬁnd data on whether any of the highways of inter- est contained traﬃc lights that require vehicles to stop periodically, and assume their absence, as is typical on busy urban freeways.

<!-- b000067 | prose | pages [4] -->
• For simplicity, we made a ”safe drivers assumption,” i.e.

<!-- b000068 | prose | pages [4] -->
that at any density of traﬃc lower than the road’s maximal capacity at the speed limit, all cars travel at precisely that limit. This is obviously not reﬂective of real driving patterns, but most likely captures overall average behavior.

<!-- b000069 | prose | pages [4] -->
• Once the breaks of a car are applied, the distance required to bring that car to a complete stop is roughly quadratic in the initial speed [7]. This is best rationalized by the fact that an object’s kinetic energy is proportional to the square of its velocity, although there are many other physical eﬀects at play. We interpolated a stopping distance curve from two points: zero

<!-- b000070 | prose | pages [4] -->
3

<!-- b000071 | furniture | pages [5] -->
Team #55261

<!-- b000072 | prose | pages [5] -->
Constant Name Description dcar Average car length

<!-- b000073 | furniture | pages [5] -->
Page 4 of 28

<!-- b000074 | prose | pages [5] -->
Value Reference 15 ft [9] Zero-speed bumper- d0 to-bumper gap 10 ft [10]

<!-- b000075 | prose | pages [5] -->
0.049 ft/mph2 Ratio of stopping distance A [8] to square of initial speed Nominal speed limit uf 60 mph Problem statement Average human reaction time trxn 0.7 sec [7]

<!-- b000076 | caption | pages [5] -->
Table 1: Constants used in model

<!-- b000077 | prose | pages [5] -->
stopping distance at zero speed, and the recommended 175 feet at 60mph (constant deceleration) [8]. See Table 1.

<!-- b000078 | prose | pages [5] -->
• Before the breaks of the car are applied, there is a ﬁnite time during which the driver or computer must recognize and react to an interruption. We used an accepted value for average human reaction time, and approxi- mated the reaction time for a computer as zero (the fraction of a second required for it to make a calculation being much less than that for a human being). See Table 1.

<!-- b000079 | prose | pages [5] -->
• Various numerical constants used in our model are listed in Table 1. Fur- ther explanation is provided in the Model Design section.

<!-- b000080 | heading | pages [5] -->
Model Design and Justiﬁcation

<!-- b000081 | heading | pages [5] -->
Flow-Density-Mean Speed Relations Model

<!-- b000082 | prose | pages [5] -->
As stated in the justiﬁcations, our model treats traﬃc ﬂow as a continuous variable in space and time. The fundamental equation governing the relation between traﬃc ﬂow, q (number of cars passing a given point on the highway per unit time) and traﬃc density, k (number of cars per unit length of the highway at a given time) is:

<!-- b000083 | prose | pages [5] -->
∂q(x, t)

<!-- b000084 | prose | pages [5] -->
+ ∂k(x, t) ∂x

<!-- b000085 | prose | pages [5] -->
= N(x, t), (1) ∂t ∂t

<!-- b000086 | prose | pages [5] -->
where N(x, t) is the source ﬂux (cars per unit time per unit length), namely vehicles entering or exiting the highway from oﬀ- and on-ramps. Equation (1) is analogous to the standard conservation of matter equations in ﬂuid ﬂow or mass transport problems in physics. The space mean speed, us, is given by:

<!-- b000087 | prose | pages [5] -->
1

<!-- b000088 | prose | pages [5] -->
X

<!-- b000089 | prose | pages [5] -->
n

<!-- b000090 | prose | pages [5] -->
i=1

<!-- b000091 | prose | pages [5] -->
n n

<!-- b000092 | prose | pages [5] -->
1

<!-- b000093 | prose | pages [5] -->
(2)

<!-- b000094 | prose | pages [5] -->
1 ui

<!-- b000095 | prose | pages [5] -->
Here n is the number of cars in the space and time interval of interest, and ui is the speed of the ith car. q and k are related as [3, 12]:

<!-- b000096 | prose | pages [5] -->
q = usk (3)

<!-- b000097 | prose | pages [5] -->
We now invoke our ”safe drivers assumption” that, until a given part of the highway reaches its maximal density, us will be precisely equal to the speed

<!-- b000098 | prose | pages [5] -->
4 4

<!-- b000099 | furniture | pages [6] -->
Team #55261

<!-- b000100 | furniture | pages [6] -->
Page 5 of 28

<!-- b000101 | prose | pages [6] -->
limit, denoted uf. This means us is a constant, so substitution of (3) into (1) gives a simple non-homogeneous transport partial diﬀerential equation (PDE) for k(x, t).

<!-- b000102 | prose | pages [6] -->
In order to investigate the eﬀects of this criterion, we must deﬁne maximal density. This maximal density is a function of us (as anyone who has ever been in a traﬃc jam has discovered empirically), because following distance (the space between the front of one car and the back of the car in front) decreases with mean vehicle speed. Our expression for maximal density at us is:

<!-- b000103 | prose | pages [6] -->
kmax(us(x, t)) = L(x, t) (4) dcar + dstop(us(x, t))

<!-- b000104 | prose | pages [6] -->
(We have made space and time dependence explicit here, for clarity). L(x, t) represents the number of open lanes at a given time and place, dcar is the length of an average car, and dstop(us) is the estimated distance it takes for a car to break to zero speed, starting from us. We deﬁne this distance as follows:

<!-- b000105 | prose | pages [6] -->
(

<!-- b000106 | prose | pages [6] -->
trxnus + Au2

<!-- b000107 | prose | pages [6] -->
dstop(us) =

<!-- b000108 | prose | pages [6] -->
Au2

<!-- b000109 | prose | pages [6] -->
s + d0

<!-- b000110 | prose | pages [6] -->
s + d0 For human driver

<!-- b000111 | prose | pages [6] -->
(5) For driverless car

<!-- b000112 | prose | pages [6] -->
Here we are using the assumptions that a driverless car will have essentially zero reaction time, and that, once the car begins decelerating, stopping distance is roughly quadratic in initial speed.

<!-- b000113 | prose | pages [6] -->
The constant d0 represents the small bumper-to-bumper gap maintained even when traﬃc is at a standstill.

<!-- b000114 | prose | pages [6] -->
The constant A was derived from empirical data (see Model Testing section).

<!-- b000115 | prose | pages [6] -->
Therefore, us(x, t) is a piecewise function of k(x, t): if k(x, t) < kmax(uf), Otherwise, us(x, t) is obtained by inverting (4), which then us(x, t) = uf. amounts to solving a simple quadratic equation, given the forms in (5). We assume us will decrease just enough to adjust to the new density in excess of kmax. This eﬀect turns (1) into a nonlinear PDE in two variables.

<!-- b000116 | prose | pages [6] -->
It is worth making note at this point of a brief history of traﬃc ﬂow theory in the continuum treatment. In his seminal 1935 report, Greenshields reported, based on empirical data, a quadratic relationship between density and ﬂow [11]:

<!-- b000117 | prose | pages [6] -->
q = ufk −uf

<!-- b000118 | prose | pages [6] -->
Alternatively, using (3),

<!-- b000119 | prose | pages [6] -->
k2 (6)

<!-- b000120 | prose | pages [6] -->
kj

<!-- b000121 | prose | pages [6] -->
us = uf(1 −k

<!-- b000122 | prose | pages [6] -->
) (7)

<!-- b000123 | prose | pages [6] -->
kj

<!-- b000124 | prose | pages [6] -->
Here, uf represents the ”free speed” of a car as it travels alone on the road, and kj represents ”jam density”, or the point at which us and q go to zero. As pointed out by Hall in 1992 [12], this model served as the foundation for analysis of traﬃc ﬂow for several decades, despite its reliance on a very small and sparse data set. Although equation (6) has the correct limiting behavior, there is little rationale behind its precise form; for example, it is unclear why a marginal increase in car density near the origin would result in an immediate decrease in mean speed. Other models (overviewed in [12]) have been proposed, and tend to be supported by the speciﬁc data set collected by the proponent of a given formula. In the absence of compelling evidence to agree with any single one of them, we believe our equation (restated in generality as (8)), which takes

<!-- b000125 | prose | pages [6] -->
5 5

<!-- b000126 | furniture | pages [7] -->
Team #55261

<!-- b000127 | furniture | pages [7] -->
Page 6 of 28

<!-- b000128 | prose | pages [7] -->
more of a ”ﬁrst principles” approach, and shows reasonable limiting behavior, is entirely reasonable and furthermore allows for an educated investigation of the eﬀect of the ratio of self-driving/cooperative cars on the road, as emphasized by (5).

<!-- b000129 | prose | pages [7] -->
(

<!-- b000130 | prose | pages [7] -->
uf −trxn+√

<!-- b000131 | prose | pages [7] -->
us =

<!-- b000132 | prose | pages [7] -->
k ≤kmax

<!-- b000133 | prose | pages [7] -->
(8)

<!-- b000134 | prose | pages [7] -->
t2rxn−4A(dzero+dcar−L

<!-- b000135 | prose | pages [7] -->
2A k ) k > kmax

<!-- b000136 | prose | pages [7] -->
Flow versus density and speed versus density curves for various percentages P of self-driving/cooperative cars on the road were generated by multiplying P trxn by (1 − 100) for each case. This is justiﬁed in the continuous limit where the density of cars is treated as an overall average rather than a property of discreet members. The results are shown in Figures 2 and 3. The constants in

<!-- b000137 | caption | pages [7] -->
Table 1 were used, and the number of lanes was taken to be 3.

<!-- b000138 | caption | pages [7] -->
Figure 2: Flow versus density for percentage of self-driving/cooperative cars P

<!-- b000139 | prose | pages [7] -->
= 0 (blue), 10 (red), 50 (yellow), 90 (purple) and 100 (green).

<!-- b000140 | prose | pages [7] -->
It is clear that in steady state conditions (no interruptions or ﬂux of vehi- cles onto or oﬀof the highway), the presence of self-driving vehicles allows for greater ﬂow (alternatively, mean speed) at the same density, which is desirable. However, the results in this analysis do not reveal clear equilibria or tipping points; the beneﬁts from an increase from P = 0 to P = 10 is similar to that for an increase from P = 90 to P = 100, and likewise for the comparison between P = 10 to P = 50 and P = 50 to P = 90.

<!-- b000141 | prose | pages [7] -->
A reasonable hypothesis regarding self-driving vehicles might be that intro- duction of the new technology would result in an increased number of people

<!-- b000142 | prose | pages [7] -->
6 6

<!-- b000143 | furniture | pages [8] -->
Team #55261

<!-- b000144 | furniture | pages [8] -->
Page 7 of 28

<!-- b000145 | caption | pages [8] -->
Figure 3: Speed versus density for percentage of self-driving/cooperative cars

<!-- b000146 | prose | pages [8] -->
P = 0 (blue), 10 (red), 50 (yellow), 90 (purple) and 100 (green).

<!-- b000147 | prose | pages [8] -->
who chose to commute by car, whether due to convenience or perhaps change in policy that would allow younger people or the elderly to ride in autonomous cars who might not have otherwise been able to drive themselves. Would an increase in the overall number of vehicles on the road outweigh the beneﬁts demonstrated above? In order to answer this, us was re-expressed as a function P of k and f = 100 as they have been deﬁned above:

<!-- b000148 | prose | pages [8] -->
q

<!-- b000149 | prose | pages [8] -->
(1 −f)2t2rxn −4A(dzero + dcar −L

<!-- b000150 | prose | pages [8] -->
−(1 −f)trxn +

<!-- b000151 | prose | pages [8] -->
us =

<!-- b000152 | prose | pages [8] -->
k )

<!-- b000153 | prose | pages [8] -->
(9) 2A

<!-- b000154 | prose | pages [8] -->
Here we consider only the case where k > kmax, since below that point a change in density has no impact on the mean speed, by deﬁnition. If k increases by a factor of χ and we assume that 100% of the additional cars are driverless, then it is easily shown that the corresponding increase in f is given by:

<!-- b000155 | prose | pages [8] -->
∆f = χ(1 −f)

<!-- b000156 | prose | pages [8] -->
(10) 1 + χ

<!-- b000157 | prose | pages [8] -->
Taking the total derivative of (9) yields:

<!-- b000158 | prose | pages [8] -->
7 7

<!-- b000159 | furniture | pages [9] -->
Team #55261

<!-- b000160 | prose | pages [9] -->
δus = ∂us

<!-- b000161 | prose | pages [9] -->
∂k dk + ∂us

<!-- b000162 | prose | pages [9] -->
∂f df

<!-- b000163 | prose | pages [9] -->
= −χL

<!-- b000164 | furniture | pages [9] -->
Page 8 of 28

<!-- b000165 | prose | pages [9] -->
rxn −4A(dzero + dcar −L

<!-- b000166 | prose | pages [9] -->
(1 −f)2t2

<!-- b000167 | prose | pages [9] -->
 

<!-- b000168 | prose | pages [9] -->
k

<!-- b000169 | prose | pages [9] -->
−1/2+

<!-- b000170 | prose | pages [9] -->
k )

<!-- b000171 | prose | pages [9] -->
−1/2

<!-- b000172 | prose | pages [9] -->
rxn −4A(dzero + dcar −L

<!-- b000173 | prose | pages [9] -->
(1 −f)2t2

<!-- b000174 | prose | pages [9] -->
B −(1 −f)B2 

<!-- b000175 | prose | pages [9] -->
χ(1 −f)

<!-- b000176 | prose | pages [9] -->
1 + χ

<!-- b000177 | prose | pages [9] -->
k )

<!-- b000178 | prose | pages [9] -->


<!-- b000179 | prose | pages [9] -->
2A

<!-- b000180 | prose | pages [9] -->
(11)

<!-- b000181 | prose | pages [9] -->
Here we have made the approximation dk = ∆k and df = ∆f. Since (11) is negative for all values of k for f < 1, it follows that an increase in density will necessarily result in a decrease in mean speed, even if the proportion of driverless vehicles increases. This result is shown graphically for a few selected values of χ and f in Figure 4. The eﬀect is visibly greatest at very low or very high densities.

<!-- b000182 | caption | pages [9] -->
Figure 4: Total derivative in mean speed for [χ = 0.1, f = 0.5] (blue), [χ = 0.5,

<!-- b000183 | prose | pages [9] -->
f = 0.1] (red), [χ = 0.5, f = 0.5] (yellow). Number of lanes was taken to be constant at 3.

<!-- b000184 | heading | pages [9] -->
Lane Change Model

<!-- b000185 | prose | pages [9] -->
Another main aspect in traﬃc ﬂow is the interactions among vehicles as they change their lanes. A change of lane occurs when ramp vehicles merge into a highway stream, highway vehicles leave for minor roads, and when vehicles change into a diﬀerent lane of the route to prepare to turn or leave the road.

<!-- b000186 | prose | pages [9] -->
8 8

<!-- b000187 | furniture | pages [10] -->
Team #55261

<!-- b000188 | furniture | pages [10] -->
Page 9 of 28

<!-- b000189 | prose | pages [10] -->
Such behavior negatively aﬀects traﬃc performance as it causes delay, decelera- tion and further impact the following vehicles. Self-driving cars and cooperating systems relieve the eﬀect by their higher sensibility, reliability, and adaptabil- ity. The following model simulates and three discrete scenarios and compares relevant factors to analyze self-driving and cooperating cars’ eﬀect on traﬃc performance. Our analysis makes use of selected traﬃc ﬂow formulae in [3].

<!-- b000190 | prose | pages [10] -->
Drivers determine whether or not to change lanes mainly by estimating the gap between the two vehicles adjacent to them, and accepting if the gap would be enough for them to merge in. Critical gap (tc) is deﬁned here as the gap for which the number of accepted gaps shorter than it is equal to the number of rejected gaps longer than it. Thus, an average vehicle would decide to merge if a gap is larger than the critical gap.

<!-- b000191 | prose | pages [10] -->
We estimate the critical gap as the summation of the diﬀerence traveled between vehicle B and vehicle A during the lane change, and the safety distance from the following vehicle as in the previous model. An assumption must be made here about the average time it takes to change lanes; a study conducted by Toledo and Zohar by observing cars in a variety of traﬃc conditions [13] found that this value, which we call τ, was approximately 4.6±2.3 seconds. Assuming that car A continues to travel the same speed, u as it changes lanes and using the pythagorean theorem gives:

<!-- b000192 | prose | pages [10] -->
(uτ)2 −d2

<!-- b000193 | prose | pages [10] -->
p

<!-- b000194 | prose | pages [10] -->
tc = uτ −

<!-- b000195 | prose | pages [10] -->
lane + dcar + dstop(u)

<!-- b000196 | prose | pages [10] -->
(12) u

<!-- b000197 | prose | pages [10] -->
Where dlane is given in the problem statement as 12 feet, and dstop(u) was deﬁned in the ﬁrst section of the model.

<!-- b000198 | prose | pages [10] -->
Following a usual assumption for light-to-medium traﬃc, we assume the rate of vehicle arrivals on the lane is described by a Poisson distribution. Then the probability of x arrivals in the interval of time t is:

<!-- b000199 | prose | pages [10] -->
P(x) = µxe−µ

<!-- b000200 | prose | pages [10] -->
x!

<!-- b000201 | prose | pages [10] -->
for x = 0, 1, 2, ...

<!-- b000202 | prose | pages [10] -->
(13)

<!-- b000203 | prose | pages [10] -->
where P(x) is the probability that x vehicles arrive in the interval time t, and µ is the average number of vehicles arriving in the interval time t.

<!-- b000204 | prose | pages [10] -->
The distribution of waiting times, i.e.

<!-- b000205 | prose | pages [10] -->
gap (h) between two consecutive Poisson arrivals is exponential, which has density:

<!-- b000206 | prose | pages [10] -->
f(t) = λe−t

<!-- b000207 | prose | pages [10] -->
where λ = µ

<!-- b000208 | prose | pages [10] -->
t ≥0 for (14)

<!-- b000209 | prose | pages [10] -->
t is the average number of vehicles arriving during a given time 1 λ, and therefore the probability that a gap h is interval. Expected value is larger than a ﬁxed gap t is:

<!-- b000210 | prose | pages [10] -->
P(h ≥t) = e−t t ≥0 for (15)

<!-- b000211 | prose | pages [10] -->
Thus, the probability Pc that a gap h is larger than critical gap tc is:

<!-- b000212 | prose | pages [10] -->
Pc = P(h ≥tc) = e−tc (16)

<!-- b000213 | prose | pages [10] -->
When an average vehicle begins to look to merge, it needs to wait until a gap larger than critical gap appears. The number of gaps the vehicle waits until a gap larger than critical gap appears follows a geometric distribution:

<!-- b000214 | prose | pages [10] -->
9 9

<!-- b000215 | furniture | pages [11] -->
Team #55261

<!-- b000216 | prose | pages [11] -->
P(x = k) = (1 −P)kP

<!-- b000217 | furniture | pages [11] -->
Page 10 of 28

<!-- b000218 | prose | pages [11] -->
for k = 0, 1, 2, ...

<!-- b000219 | prose | pages [11] -->
(17)

<!-- b000220 | prose | pages [11] -->
where the probability P is given in (3). 1 Therefore the expected value is P . Thus for an average vehicle, the expected waiting time for a gap Ew is the expected number of gaps waiting times the expected length of each gap:

<!-- b000221 | prose | pages [11] -->
Ew = 1

<!-- b000222 | prose | pages [11] -->
∗1

<!-- b000223 | prose | pages [11] -->
λ =

<!-- b000224 | prose | pages [11] -->
Pc

<!-- b000225 | prose | pages [11] -->
λ = etc

<!-- b000226 | prose | pages [11] -->
e−tc ∗1 1

<!-- b000227 | prose | pages [11] -->
(18) λ

<!-- b000228 | prose | pages [11] -->
Let ∆d be the distance between the vehicle’s position at which it starts to look for a gap and the exit that it needs to turn through. The criterion to avoid missing the exit, starting at speed u, is:

<!-- b000229 | prose | pages [11] -->
u ≤Ew = etc

<!-- b000230 | prose | pages [11] -->
∆d

<!-- b000231 | prose | pages [11] -->
(19) λ

<!-- b000232 | prose | pages [11] -->
If the vehicle cannot satisfy the above inequality with its current constant speed, it needs to decelerate, which would cause the vehicles behind it to decel- erate into the same speed, further aﬀecting the traﬃc ﬂow and density. Thus the minimum ∆d (∆dmin ) to successfully merge at the exit without decelerating is:

<!-- b000233 | prose | pages [11] -->
∆dmin = eλtcu

<!-- b000234 | prose | pages [11] -->
(20) λ

<!-- b000235 | prose | pages [11] -->
If ∆d > ∆dmin, the vehicle needs to decelerate into speed u′ = u−u0, which can be calculated from:

<!-- b000236 | prose | pages [11] -->
u′ = eλtc

<!-- b000237 | prose | pages [11] -->
∆d

<!-- b000238 | prose | pages [11] -->
λ

<!-- b000239 | prose | pages [11] -->
u′ = ∆dλ

<!-- b000240 | prose | pages [11] -->
eλtc

<!-- b000241 | prose | pages [11] -->
therefore,

<!-- b000242 | prose | pages [11] -->
(21)

<!-- b000243 | prose | pages [11] -->
We simulated three scenarios of interactions between vehicle A, which is changing lanes, and vehicle B, which would take the place of A after the merge occurs (denoted as A →B). We will ﬁrst analyze under normal circumstances with average traﬃc volume, and then special cases during peak hours.

<!-- b000244 | prose | pages [11] -->
Case 1: Non-self-driving or self-driving vehicle merges before a non-self- driving vehicle.

<!-- b000245 | prose | pages [11] -->
This is the original circumstance, where tc is found using (12). The diﬀerence between vehicle A being self-driving or non-self driving is negligible, because it must still take full cautionary measures, not being able to predict the behavior of a conventional driver.

<!-- b000246 | prose | pages [11] -->
Case 2: Non-self-driving vehicle merges before a self-driving vehicle. We assume that drivers can visually identify any self-driving vehicle. When drivers of vehicle A evaluate the gap and make decisions on merging, they con- sider the risk that vehicle B would exhibit unusual behaviors such as acceleration and ﬁnite reaction time. Such risk would greatly decrease for a self-driving vehi- cle as its behavior is more predictable under the control of a computer. Vehicle B cannot know vehicle A’s action beforehand because they cannot communi- cate, but the self-driving car has no human reaction time to adjust the gap if necessary. These two factors will inﬂuence driver A’s decision and cause the

<!-- b000247 | prose | pages [11] -->
10 10

<!-- b000248 | furniture | pages [12] -->
Team #55261

<!-- b000249 | furniture | pages [12] -->
Page 11 of 28

<!-- b000250 | prose | pages [12] -->
critical gap to decrease. In our model, as a self-driving vehicle does not have reaction time, dstop(u0) = Au2

<!-- b000251 | prose | pages [12] -->
0 + dzero. This decreases the critical gap, caus- ing the probability of encountering an acceptable gap to increase, the expected waiting time to decrease, and minimum gap without decelerating to increase.

<!-- b000252 | prose | pages [12] -->
Case 3: When a self-driving vehicle merges before a self-driving vehicle in a cooperating system.

<!-- b000253 | prose | pages [12] -->
Within a self-driving cooperating system, vehicle A makes reservations to merge beforehand, and vehicle B is informed of the action and decelerates to create an optimal gap if needed. The coordinated system calculates an optimal time and position for vehicle A to merge, minimizing the negative eﬀect on traﬃc ﬂow. With the cooperation of vehicle B happening concurrently, vehicle A does not need as big a gap as in the preceding cases, as any gap will guarantee a successful merge. Assuming vehicle B decelerates into the same speed u′ as vehicle A, dstop = Au′2 + dzero. Given a distance ∆d, u′ and tc can then be calculated from this equation derived from the previous formulae:

<!-- b000254 | prose | pages [12] -->
lane + Au′2 + dcar + dzero

<!-- b000255 | prose | pages [12] -->
(uoτ)2 −d2

<!-- b000256 | prose | pages [12] -->
tc = ln( ∆dλ

<!-- b000257 | prose | pages [12] -->
p

<!-- b000258 | prose | pages [12] -->
u′ ) = uoτ − λ

<!-- b000259 | prose | pages [12] -->
(22)

<!-- b000260 | prose | pages [12] -->
uo

<!-- b000261 | prose | pages [12] -->
The lane change model was simulated using input data calculated from the ﬂow-density-mean speed model, shown below in Table 2. We took the percentage of cars that are self-driving to be 50%, and number of lanes to be constant at 3. The jam density kj (where us goes to zero) is therefore 638 cars/mile. We compared wait times for light, moderate, and heavy traﬃc (deﬁned by the ratio of k to kj) in the three cases outlined above; results are tabulated in Tables 4 through 6.

<!-- b000262 | prose | pages [12] -->
Density(k) Traﬃc type (cars/mile)

<!-- b000263 | prose | pages [12] -->
0.2*kj Light traﬃc = 42.5333

<!-- b000264 | prose | pages [12] -->
0.5*kj Moderate traﬃc = 106.3333

<!-- b000265 | prose | pages [12] -->
0.8*kj Heavy traﬃc = 170.1333

<!-- b000266 | prose | pages [12] -->
Flow(q)

<!-- b000267 | prose | pages [12] -->
Speed(u)

<!-- b000268 | prose | pages [12] -->
(cars/sec)

<!-- b000269 | prose | pages [12] -->
(mile/sec)

<!-- b000270 | prose | pages [12] -->
1.4200 0.0112

<!-- b000271 | prose | pages [12] -->
1.5900 0.0005

<!-- b000272 | prose | pages [12] -->
1.0180 0.0002

<!-- b000273 | caption | pages [12] -->
Table 2: Input data for lane changing model.

<!-- b000274 | heading | pages [12] -->
Light Traﬃc Simulation Results

<!-- b000275 | prose | pages [12] -->
Case # dt (mile) dstop (mile) 1 0.0001 0.0275 2 0.0001 0.0197 3 0.0001 0.0194 tc (sec) Pc Ew (sec) ∆dmin (mile) 2.4632 0.0303 23.2665 0.2606 1.7632 0.0818 8.6108 0.0964 1.7401 0.2492 5.6978 0.0638

<!-- b000276 | caption | pages [12] -->
Table 3: Results for light traﬃc.

<!-- b000277 | prose | pages [12] -->
In Case 3, we use ∆d = 0.09, a value close to dmin for Case 2, to solve tc and other variables. As expected from the previous model and scenario hypothesis, the interactions with self-driving and cooperating vehicles decrease the safety distance from the following vehicle (dstop) and therefore decrease the critical gap.

<!-- b000278 | prose | pages [12] -->
11 11

<!-- b000279 | furniture | pages [13] -->
Team #55261

<!-- b000280 | furniture | pages [13] -->
Page 12 of 28

<!-- b000281 | prose | pages [13] -->
From Case 1 to 2, as a vehicle merges to precede a self-driving vehicle, the probability that an upcoming gap h is larger than critical gap increases by 170%, expected waiting time for an accepted gap decreases from 23.27 seconds to 8.61 seconds, and the minimum distance to successfully merge at the exit without decelerating decreases into 37% of original value. These changes would greatly reduce the eﬀects of lane changes on the traﬃc ﬂow on the road.

<!-- b000282 | heading | pages [13] -->
Moderate Traﬃc Simulation Results

<!-- b000283 | prose | pages [13] -->
Case # dt (mile) dstop (mile) 1 0.0001 0.0112 2 0.0001 0.0077 3 0.0001 0.0072 tc (sec) Pc Ew (sec) ∆dmin (mile) 2.2650 0.0273 23.0506 0.1153 1.5650 0.0830 7.5738 0.0379 1.4710 0.3652 4.3535 0.0218

<!-- b000284 | caption | pages [13] -->
Table 4: Results for moderate traﬃc.

<!-- b000285 | prose | pages [13] -->
Similarly, we use ∆d = 0.03 in Scenario 3, a value close to dmin for Case 2. From Case 1 to 2, Pc increases by 204%, Ew and dmin decrease to 33% of their original values. The proportions and rates of change are similar in light and moderate traﬃcs, being slightly more prominent in moderate traﬃc due to its higher density.

<!-- b000286 | prose | pages [13] -->
In peak traﬃc, ﬂow decreases considerably, and therefore λ becomes small. The Poisson distribution in this case predicts a steep curve concentrated near the vertical axis; however, this would correspond to a situation in which drivers did not leave any distance between themselves and the back of the car in front of them; in terms of our previously deﬁned terms, dzero would be zero. In order to adjust the Poisson distribution to traﬃc analysis during peak hours, we specify a ﬁnite minimum time gap tmin in order to restrict the gap range. Then the probability that a gap h is larger than critical gap tc to be acceptable is:

<!-- b000287 | prose | pages [13] -->
P(h ≥tc) = e−λ(tc−tmin) (23)

<!-- b000288 | prose | pages [13] -->
We estimate the minimum gap distance in Case 1 as the minimum safety distance to keep from vehicle B when the speed of vehicle B is zero. Given that minimum gap is tested as an extreme situation, we include a factor of 1/3. Then the minimum gap is calculated as:

<!-- b000289 | prose | pages [13] -->
min = dzero

<!-- b000290 | prose | pages [13] -->
t1

<!-- b000291 | prose | pages [13] -->
(24) 3uo

<!-- b000292 | prose | pages [13] -->
We take the minimum gap for Case 2 to be smaller, as some drivers be- lieve self-driving vehicles (which we assume are visually identiﬁable) will always decelerate to assist them with merging even with a very small gap. Thus we estimate t2

<!-- b000293 | prose | pages [13] -->
min as 50% of t1

<!-- b000294 | prose | pages [13] -->
min:

<!-- b000295 | prose | pages [13] -->
min = t1

<!-- b000296 | prose | pages [13] -->
min

<!-- b000297 | prose | pages [13] -->
t2

<!-- b000298 | prose | pages [13] -->
= dzero

<!-- b000299 | prose | pages [13] -->
(25)

<!-- b000300 | prose | pages [13] -->
2 2

<!-- b000301 | prose | pages [13] -->
6

<!-- b000302 | prose | pages [13] -->
After adjusting for heavy traﬃc, we obtain the results shown in Table 5. If vehicle A does not have enough time to ﬁnd an acceptable gap, it must decelerate in order to complete the lane change in time to reach its destination (for example, an exit on the freeway). Such situations are represented in our model as when ∆d < ∆dmin, and the vehicle reduces speed from uo to u′. We

<!-- b000303 | prose | pages [13] -->
12 12

<!-- b000304 | furniture | pages [14] -->
Team #55261

<!-- b000305 | furniture | pages [14] -->
Page 13 of 28

<!-- b000306 | heading | pages [14] -->
Heavy Traﬃc Simulation Results

<!-- b000307 | prose | pages [14] -->
Case # dt (mile) dstop (mile) 1 0.0003 0.0066 2 0.0003 0.0052 3 0.0003 0.0002 tc (sec) Pc Ew (sec) ∆dmin (mile) 3.1309 0.0413 23.7926 0.0476 2.5884 0.0717 13.6961 0.0274 2.5841 0.0768 13.2509 0.0265

<!-- b000308 | caption | pages [14] -->
Table 5: Results for heavy traﬃc.

<!-- b000309 | prose | pages [14] -->
wish to measure the eﬀect on traﬃc performance when an event such as this occurs.

<!-- b000310 | prose | pages [14] -->
Given ∆d, the reduced speed u′ can be calculated from (21). As the vehicles behind A must keep the minimum safety distance with respect to one other, the new density behind A, k′, is the reciprocal of the sum of the average vehicle length and the safety distance:

<!-- b000311 | prose | pages [14] -->
1 k′ = dstop(u′) = 1

<!-- b000312 | prose | pages [14] -->
(26)

<!-- b000313 | prose | pages [14] -->
Au′2 + trxnu + dcar + dzero

<!-- b000314 | prose | pages [14] -->
We make the simplifying assumption that the speed of the vehicles behind A travel at a new constant and uniform speed in order to obtain the new traﬃc ﬂow:

<!-- b000315 | prose | pages [14] -->
q′ = k′u′ (27)

<!-- b000316 | prose | pages [14] -->
The eﬀect of this mass deceleration can be described by shock wave theory [3], which assumes an instantaneous change in speed at one point and uses a conservation of ”mass” (cars) argument, along with the fundamental relation (3), to calculate the rate of propagation of the resulting ”wave” of slowed cars. This rate, uw, is given by:

<!-- b000317 | prose | pages [14] -->
uw = q′ −qo

<!-- b000318 | prose | pages [14] -->
(28)

<!-- b000319 | prose | pages [14] -->
k′ −ko

<!-- b000320 | prose | pages [14] -->
As the shock wave moves along opposite the direction of the main traﬃc stream, the growth rate of the queue of slowed vehicles, ug, is:

<!-- b000321 | prose | pages [14] -->
ug = u′ + uw (29)

<!-- b000322 | prose | pages [14] -->
Knowing u′ and ∆d, we calculate the average waiting time that vehicle A would need to merge at the exit or enter point is Ew. Therefore the expected (average) time to successfully merge is Ew

<!-- b000323 | prose | pages [14] -->
2 . Then the length of the queue, lq, and the number of vehicles involved, nq until the vehicle ﬁnishes merging are:

<!-- b000324 | prose | pages [14] -->
lq = ug ∗Ew

<!-- b000325 | prose | pages [14] -->
(30) 2

<!-- b000326 | prose | pages [14] -->
nq = lq ∗k′ (31)

<!-- b000327 | prose | pages [14] -->
Based on these equations, we ran the following simulation to compare the improvement from Case 1 to Case 2 on delays resulting from the shock wave phenomenon. Due to the diﬀerence in the minimum distance, while ∆d is in the range of ∆d1

<!-- b000328 | prose | pages [14] -->
min < ∆d ≤∆d2

<!-- b000329 | prose | pages [14] -->
min, merging will result in speed reduction in Case 1 but not in Case 2. Thus, the merging in Case 2 will not cause a shock wave, whereas merging in Case 1 will. For each traﬃc type subgroup, we set ∆d

<!-- b000330 | prose | pages [14] -->
13 13

<!-- b000331 | furniture | pages [15] -->
Team #55261

<!-- b000332 | prose | pages [15] -->
equal to ∆d2

<!-- b000333 | furniture | pages [15] -->
Page 14 of 28

<!-- b000334 | prose | pages [15] -->
min, and the results and eﬀects for Case 1 is shown in the following tables:

<!-- b000335 | prose | pages [15] -->
Simulation of ”shock wave” due to lane change delay, Case #1 ko(cars/mile) Traﬃc type uo(mile/sec) qo(cars/sec) ∆d(mile) 42.5333 Light traﬃc 0.0112 1.4200 0.1153 106.3333 Medium traﬃc 0.0050 1.5900 0.0379 170.1333 Heavy traﬃc 0.0020 1.0180 0.0218

<!-- b000336 | caption | pages [15] -->
Table 6: Part one of simulation results.

<!-- b000337 | prose | pages [15] -->
k′(cars/mile) u′(mile/sec) Traﬃc type q′(cars/sec) uw(mile/sec) ug(mile/sec) 89.8846 Light traﬃc 0.0050 0.4453 -0.0206 0.0255 161.2373 Medium traﬃc 0.0016 0.2649 -0.0241 0.0258 182.8054 Heavy traﬃc 0.0009 0.1672 -0.0671 0.0681

<!-- b000338 | caption | pages [15] -->
Table 7: Part two of simulation results.

<!-- b000339 | prose | pages [15] -->
Traﬃc type lq (miles)

<!-- b000340 | prose | pages [15] -->
Light traﬃc 0.3 Medium traﬃc 0.3 Heavy traﬃc 0.81

<!-- b000341 | prose | pages [15] -->
q′

<!-- b000342 | prose | pages [15] -->
k′

<!-- b000343 | prose | pages [15] -->
nq (cars)

<!-- b000344 | prose | pages [15] -->
qo

<!-- b000345 | prose | pages [15] -->
ko 26.7 0.3136 2.1133 47.9 0.1666 1.5163 147.99 0.1643 1.0745

<!-- b000346 | caption | pages [15] -->
Table 8: Part three of simulation results.

<!-- b000347 | prose | pages [15] -->
We can see from Tables 6 through 8 the impact on traﬃc performances when a queue results from merging in Case 1. For example, in light traﬃc, the situation decreases the temporary ﬂow into 31.36% of original value, increases the temporary density into 200.11% of original value, and causes a queue of 0.30 miles with 26.7 vehicles involved. All these negative eﬀects would not occur in Cases 2 or 3 (involving self-driving and/or cooperative cars) because the vehicles do not need to decelerate for merging.

<!-- b000348 | heading | pages [15] -->
Model Testing and Error/Sensitivity Analysis

<!-- b000349 | prose | pages [15] -->
In order to apply our model to the given data, we replicated the curve for weekday traﬃc volume in Figure 1 and normalized it to obtain a distribution function, which was scaled by the ”Average Daily Traﬃc Count” statistic given in the problem for each point in space on each highway (use of the same distri- bution for all points in space discussed in the Assumptions and Justiﬁcations section). This provided estimates for traﬃc ﬂow at all points (s, t). We used a 30 second time interval, and for space intervals we used the distances between consecutive mile markers. Those intervals are roughly characteristic of average car speeds on the highways, since many markers were spaced less than one mile apart.

<!-- b000350 | prose | pages [15] -->
Solving for u(x, t) and k(x, t) from ﬂow values using (3) and (8) required the additional assumption that all points lay on the upper half of the q −u curve shown in Figure 5, since that relation is noninvertible. We reasoned that a transition to the lower half of the curve would manifest as a noticeable feature

<!-- b000351 | prose | pages [15] -->
14 14

<!-- b000352 | furniture | pages [16] -->
Team #55261

<!-- b000353 | furniture | pages [16] -->
Page 15 of 28

<!-- b000354 | prose | pages [16] -->
in the ﬂow distribution curve, for example shown in Figure 6, corresponding to an approach towards standstill conditions. This type of scenario would be interesting to investigate in future studies.

<!-- b000355 | caption | pages [16] -->
Figure 5: Branches of q −u curve.

<!-- b000356 | prose | pages [16] -->
Upon analyzing the empirical ﬂow data, it became apparent that maximal ﬂow values signiﬁcantly exceeded those predicted by the curve in Figure 5, using our initial input parameters for the constants in Table 1. In order to address this, we lowered the values of the constants A, trxn, and dzero to 0.0245 ft/mph2, 0.5 sec, and 0 ft, respectively. These reﬂect lower bound estimates found in other references [14, 15]. Despite this adjustment, some q values still exceeded the maximum prediction, and this was handled by holding u at its value for the maximum theoretical q (indicated in the ﬁgures below).

<!-- b000357 | prose | pages [16] -->
Once q(x, t), u(x, t), and k(x, t) were all known, values were plugged into (1) to determine vehicle ﬂux onto or oﬀof the highways. In doing this we hoped to identify locations and times where many cars would likely be changing lanes or merging, resulting in increased delays as described in the Model Design section.

<!-- b000358 | prose | pages [16] -->
Several representative plots are shown in Figures 7 and 8. Due to the error in predictions of q described above, the data show certain areas of discontinuity, but nevertheless give a rational description of traﬃc patterns over the course of one day. Some notable features are listed below.

<!-- b000359 | prose | pages [16] -->
• Traﬃc ﬂux shows a noticeable increase during times of heavier traﬃc, since a greater number of cars are entering and exiting the freeway during peak hours. Without conducting a rigorous analysis, Figures 7 b and d also seem to reﬂect the location of major interchanges along I-5 (with I-90 near mile 160 and with I-705 near mile 130).

<!-- b000360 | prose | pages [16] -->
15

<!-- b000361 | furniture | pages [17] -->
Team #55261

<!-- b000362 | furniture | pages [17] -->
Page 16 of 28

<!-- b000363 | caption | pages [17] -->
Figure 6: Example of expected deviation in ﬂow distribution curve arising from

<!-- b000364 | prose | pages [17] -->
transition to lower branch of q −u curve, indicated by arrow.

<!-- b000365 | prose | pages [17] -->
• As shown in Figure 8 b, traﬃc ﬂux generally follows traﬃc ﬂow in mag- nitude throughout the day at most times (spikes in this graph likely cor- respond to the artiﬁcial cutoﬀon q imposed when processing the data).

<!-- b000366 | prose | pages [17] -->
• Our model indicates a rapid decrease in mean speed once kmax, given in (4), is reached.

<!-- b000367 | prose | pages [17] -->
As shown in the ﬁrst section of our model, increasing the percentage of self-driving cars on the roads would help to forestall this precipitous decline, but only if measures are taken to insure that the technology does not lead to a net increase in total number of vehicles in the system.

<!-- b000368 | prose | pages [17] -->
• The eﬀects of the temporal distribution of ﬂow values appear much stronger than those of the spatial distribution, which is somewhat to be expected since the Average Daily Traﬃc Counts show little discernible correlation in space. While the approximation of a universal time distribution in traf- ﬁc ﬂow is a rough estimate, our ﬁndings nevertheless suggest that lanes dedicated speciﬁcally to autonomous vehicles may confer the most signif- icant beneﬁt during peak periods, especially given our ﬁndings of drastic reduction in lane changing times for these cars in the second section of our model. Therefore, policymakers may ﬁnd that the availability in time (rather than in location) of designated lanes for self-driving/cooperative cars is the more important factor; for example, express lanes might be opened only during rush hours.

<!-- b000369 | prose | pages [17] -->
Additional ﬁgures for other highways are shown in the appendix.

<!-- b000370 | prose | pages [17] -->
16

<!-- b000371 | furniture | pages [18] -->
Team #55261

<!-- b000372 | furniture | pages [18] -->
Page 17 of 28

<!-- b000373 | caption | pages [18] -->
Figure 7: Traﬃc ﬂux along Interstate 5, (a) Northbound, 12:50am; (b) North-

<!-- b000374 | prose | pages [18] -->
bound, 1:50pm; (c) Southbound, 12:50am; (d) Southbound, 1:50pm

<!-- b000375 | prose | pages [18] -->
17

<!-- b000376 | furniture | pages [19] -->
Team #55261

<!-- b000377 | furniture | pages [19] -->
Page 18 of 28

<!-- b000378 | caption | pages [19] -->
Figure 8: (a) Traﬃc ﬂux; (b) Traﬃc ﬂow; (c) Space mean speed over the course

<!-- b000379 | prose | pages [19] -->
of a 24-hour period at mile marker 155.18 on I-5 North. Dashed red lines indicate the point at which empirical data exceed the maximum prediction of our model.

<!-- b000380 | prose | pages [19] -->
18

<!-- b000381 | furniture | pages [20] -->
Team #55261

<!-- b000382 | furniture | pages [20] -->
Page 19 of 28

<!-- b000383 | prose | pages [20] -->
Because our model relies heavily on the deﬁnition of the relationship between space mean speed and vehicle density, it is useful to understand the relative sensitivity of that equation to the various constants used in (8). These are, to restate: A, the quadratic coeﬃcient for speed dependence of stopping distance; trxn, the linear coeﬃcient; dcar + dzero, the presumed gap between the front bumpers of consecutive cars in standstill traﬃc; uf, the nominal speed limit; and L, the number of lanes. For each of these, the constant value given in Table 1 was varied from 0 to double the original value (L was given a baseline value of 3). Results are depicted graphically using us vs k curves in Figure 9.

<!-- b000384 | caption | pages [20] -->
Figure 9: Sensitivity of the proposed us vs k relationship to variations from

<!-- b000385 | prose | pages [20] -->
baseline values for (a) A; (b) trxn; (c) dcar + dzero; (d) uf; and (e) L. Values progress through 0, 50, 100, 150, and 200% of their baseline values in the order blue, red, yellow, purple, green.

<!-- b000386 | prose | pages [20] -->
The behavior of these graphs reﬂects common sense intuition (another ad- vantage of our model over empirical forms which use parameters that do not carry a physical meaning). For example, it is logical that mean speed would decrease at a given density along with the number of lanes, while increasing as the driver’s reaction time decreases (shortening the requisite gap between cars). It is worth noting that the curves are divergent as the value of dcar + dstop goes to zero, as this would imply the possibility of inﬁnite density of vehicles.

<!-- b000387 | prose | pages [20] -->
19

<!-- b000388 | furniture | pages [21] -->
Team #55261

<!-- b000389 | furniture | pages [21] -->
Page 20 of 28

<!-- b000390 | heading | pages [21] -->
Discussion:

<!-- b000391 | heading | pages [21] -->
Strengths and Potential Areas for Improve-

<!-- b000392 | heading | pages [21] -->
ment of the Model

<!-- b000393 | heading | pages [21] -->
Strengths of the ﬂow-density-mean speed model include the following:

<!-- b000394 | prose | pages [21] -->
• The model is not overly complex and, as such, does not take much compu- tational power in order to calculate, which allows for real-time stream of input data to generate a real-time stream of output data with insigniﬁcant delays.

<!-- b000395 | prose | pages [21] -->
• The model is general enough to allow for additional parameters, such as the delay in response time of self-driving cars which can be incorporated into the reaction rate trxn.

<!-- b000396 | prose | pages [21] -->
• The model incorporates known mathematical relationships between speed, density, and ﬂow, but does not propose any equations that do not carry some measure of physical or rational motivation.

<!-- b000397 | prose | pages [21] -->
• The number of lanes is a function of distance and time which accommo- dates for time-dependent lane changes, for instance during traﬃc acci- dents, construction work, or lane additions, in addition to the data pro- vided for analysis.

<!-- b000398 | prose | pages [21] -->
• The diﬀerence between the reaction times of human-driven cars and self- driving cars is accounted for in our model.

<!-- b000399 | heading | pages [21] -->
Strengths of the lane change model include the following:

<!-- b000400 | prose | pages [21] -->
• The solution uses concepts from the macroscopic continuous approach in ﬂow-density-mean speed model and a discrete simulation approach in the lane change model. This ensures a measure of continuity between the two.

<!-- b000401 | prose | pages [21] -->
• The model measures the lane change eﬀects by both common factors of critical gap and expected waiting time and the special case of shock waves and vehicle queues.

<!-- b000402 | prose | pages [21] -->
• The model simulates lane change in three scenarios with diﬀerent degree of interaction of self-driving and cooperating vehicles, and presents the eﬀect by comparing the simulation results numerically.

<!-- b000403 | prose | pages [21] -->
• Adjusted with the daily peak traﬃc hour distribution, the simulation sep- arately discuss three subgroups of light, moderate, and heavy traﬃc and compare their degrees of eﬀects.

<!-- b000404 | prose | pages [21] -->
• The stochastics approach simulates the random process and analyzes the expected values of variables to measure the eﬀects on traﬃc performance.

<!-- b000405 | prose | pages [21] -->
• The model agrees with ﬂow-density-mean speed model by using same as- sumptions and main relationships, and integrates by using some outputs and formulas of ﬂow-density-mean speed model as simulation input and model construction.

<!-- b000406 | prose | pages [21] -->
20

<!-- b000407 | furniture | pages [22] -->
Team #55261

<!-- b000408 | furniture | pages [22] -->
Page 21 of 28

<!-- b000409 | heading | pages [22] -->
Weaknesses of the ﬂow-density-mean speed model include the follow-

<!-- b000410 | prose | pages [22] -->
ing:

<!-- b000411 | prose | pages [22] -->
• The model does not account for interchanges or merging lanes in traﬃc and their eﬀects on the mean speed or traﬃc density.

<!-- b000412 | prose | pages [22] -->
• The model does not account for cooperation between self-driving cars or the interaction between self-driving and non-self-driving cars.

<!-- b000413 | prose | pages [22] -->
• The model does not account for diﬀerences in car length of self-driving cars from the current average car length.

<!-- b000414 | prose | pages [22] -->
• The results presented made use of an invariant, daily, peak traﬃc hours distribution which was bimodal in nature which does not account for the diﬀerence in typical traﬃc and holiday or weekend traﬃc.

<!-- b000415 | prose | pages [22] -->
• The results presented used a ﬁnite diﬀerence approximation for the deriva- tive, which introduces error for ﬁnite time and space intervals.

<!-- b000416 | heading | pages [22] -->
Weaknesses of the lane change model include the following:

<!-- b000417 | prose | pages [22] -->
• The main assumption of Poisson distribution of arriving vehicles ﬁts heavy traﬃc less well. The factors we include to adjust for peak hours are esti- mated and do not fully reﬂect the situations in heavy traﬃc.

<!-- b000418 | prose | pages [22] -->
• The measurement of most variables by expected value may not reﬂect special conditions such as peak hours and cooperating systems accurately.

<!-- b000419 | prose | pages [22] -->
• The critical gap, which should be obtained from real collected data dis- tribution by nature of deﬁnition, is calculated by physics formulae in the model.

<!-- b000420 | prose | pages [22] -->
• The measurements of critical gap for Case 3 and reduced speed in shock wave analysis are functions of ∆d, thus the comparison results are subject to the choice of ∆d.

<!-- b000421 | prose | pages [22] -->
• The simulation is conducted on data of one segment of highway and lacks the generality to be applied to all circumstances.

<!-- b000422 | prose | pages [22] -->
21

<!-- b000423 | furniture | pages [23] -->
Team #55261

<!-- b000424 | furniture | pages [23] -->
Page 22 of 28

<!-- b000425 | heading | pages [23] -->
Appendix

<!-- b000426 | caption | pages [23] -->
Figure 10: Traﬃc ﬂux along Interstate 90, (a) Eastbound, 12:50am; (b) East-

<!-- b000427 | prose | pages [23] -->
bound, 1:50pm; (c) Westbound, 12:50am; (d) Westbound, 1:50pm

<!-- b000428 | prose | pages [23] -->
22

<!-- b000429 | furniture | pages [24] -->
Team #55261

<!-- b000430 | furniture | pages [24] -->
Page 23 of 28

<!-- b000431 | caption | pages [24] -->
Figure 11: (a) Traﬃc ﬂux; (b) Traﬃc ﬂow; (c) Space mean speed over the course

<!-- b000432 | prose | pages [24] -->
of a 24-hour period at mile marker 14.32 on I-90 East. Dashed red lines indicate the point at which empirical data exceed the maximum prediction of our model.

<!-- b000433 | prose | pages [24] -->
23

<!-- b000434 | furniture | pages [25] -->
Team #55261

<!-- b000435 | furniture | pages [25] -->
Page 24 of 28

<!-- b000436 | caption | pages [25] -->
Figure 12: Traﬃc ﬂux along Interstate 405, (a) Northbound, 12:50am; (b)

<!-- b000437 | prose | pages [25] -->
Northbound, 1:50pm; (c) Southbound, 12:50am; (d) Southbound, 1:50pm

<!-- b000438 | prose | pages [25] -->
24

<!-- b000439 | furniture | pages [26] -->
Team #55261

<!-- b000440 | furniture | pages [26] -->
Page 25 of 28

<!-- b000441 | caption | pages [26] -->
Figure 13: (a) Traﬃc ﬂux; (b) Traﬃc ﬂow; (c) Space mean speed over the

<!-- b000442 | prose | pages [26] -->
course of a 24-hour period at mile marker 15.76 on I-405 North. Dashed red lines indicate the point at which empirical data exceed the maximum prediction of our model.

<!-- b000443 | prose | pages [26] -->
25

<!-- b000444 | furniture | pages [27] -->
Team #55261

<!-- b000445 | furniture | pages [27] -->
Page 26 of 28

<!-- b000446 | caption | pages [27] -->
Figure 14: Traﬃc ﬂux along State Road 520, (a) Eastbound, 12:50am; (b)

<!-- b000447 | prose | pages [27] -->
Eastbound, 1:50pm; (c) Westbound, 12:50am; (d) Westbound, 1:50pm

<!-- b000448 | prose | pages [27] -->
26

<!-- b000449 | furniture | pages [28] -->
Team #55261

<!-- b000450 | furniture | pages [28] -->
Page 27 of 28

<!-- b000451 | caption | pages [28] -->
Figure 15: (a) Traﬃc ﬂux; (b) Traﬃc ﬂow; (c) Space mean speed over the

<!-- b000452 | prose | pages [28] -->
course of a 24-hour period at mile marker 5.39 on SR-520 East. Dashed red lines indicate the point at which empirical data exceed the maximum prediction of our model.

<!-- b000453 | prose | pages [28] -->
27

<!-- b000454 | furniture | pages [29] -->
Team #55261

<!-- b000455 | heading | pages [29] -->
References

<!-- b000456 | furniture | pages [29] -->
Page 28 of 28

<!-- b000457 | references | pages [29] -->
[1] Mannering, Fred L., and Walter P. Kilareski. Principles of highway en-

<!-- b000458 | references | pages [29] -->
gineering and traﬃc analysis. 5th ed. New York: Wiley, 2013. Print.

<!-- b000459 | references | pages [29] -->
[2] Highway capacity manual. Washington, D.C.: Transportation Research

<!-- b000460 | references | pages [29] -->
Board, National Research Council, 2000. Print.

<!-- b000461 | references | pages [29] -->
[3] Garber, Nicholas J., and Lester A. Hoel. Traﬃc and highway engineering.

<!-- b000462 | references | pages [29] -->
5th ed. Paciﬁc Grove, CA: Brooks/Cole Pub. Co., 2015. Print.

<!-- b000463 | references | pages [29] -->
[4] Monteil, Julien . Investigating the eﬀects of cooperative vehicles on high-

<!-- b000464 | references | pages [29] -->
way traﬃc ﬂow homogenization: analytical and simulation studies.

<!-- b000465 | references | pages [29] -->
Thesis.

<!-- b000466 | references | pages [29] -->
Universit´e de Lyon, 2013. N.p.: n.p., n.d. Print.

<!-- b000467 | references | pages [29] -->
[5] USA. Washington State Department of Transportation.

<!-- b000468 | references | pages [29] -->
Traﬃc Report. N.p.: n.p., n.d. Print.

<!-- b000469 | references | pages [29] -->
2006 Annual

<!-- b000470 | references | pages [29] -->
[6] United States. Census Bureau. Population Division. ”Table 1. County to

<!-- b000471 | references | pages [29] -->
County Commuting Flows for the United States and Puerto Rico: 2009-2013.”

<!-- b000472 | references | pages [29] -->
United States Census 2009-2013. Washington: US Census Bureau. Web. 21

<!-- b000473 | references | pages [29] -->
Jan. 2009.

<!-- b000474 | references | pages [29] -->
[7] UK. Department for Transport. The Highway Code. N.p., 5 Dec. 2016.

<!-- b000475 | references | pages [29] -->
Web. 21 Jan. 2017. https://www.gov.uk/guidance/the-highway-code/general-

<!-- b000476 | references | pages [29] -->
rules-techniques-and-advice-for-all-drivers-and-riders-103-to-158#rule126.

<!-- b000477 | references | pages [29] -->
[8] USA. Washington State Department of Licensing.

<!-- b000478 | references | pages [29] -->
Washington driver

<!-- b000479 | references | pages [29] -->
guide. Olympia: State of Washington, Dept. of Licensing, 2006. Print.

<!-- b000480 | references | pages [29] -->
[9] ”What is the average length of a car?” Reference. N.p., n.d. Web. 21

<!-- b000481 | references | pages [29] -->
Jan. 2017.

<!-- b000482 | references | pages [29] -->
[10] Houchin, Andrew Jeremy. An investigation of freeway standstill dis-

<!-- b000483 | references | pages [29] -->
tance, headway, and time gap data in heterogeneous traﬃc in Iowa. Thesis.

<!-- b000484 | references | pages [29] -->
Iowa State University, 2015. N.p.: n.p., n.d. Print.

<!-- b000485 | references | pages [29] -->
[11] Greenshields, B. D. A Study of Traﬃc Capacity.

<!-- b000486 | references | pages [29] -->
Highway Research

<!-- b000487 | references | pages [29] -->
Board Proceedings, 14. 1935. pp. 448-477.

<!-- b000488 | references | pages [29] -->
[12] Lieu, Henry, ed. Rep. N.p.: n.p., 1992. U.S. Department of Transporta-

<!-- b000489 | references | pages [29] -->
tion - Revised Monograph on Traﬃc Flow Theory. Ch. 2: Traﬃc Stream Char-

<!-- b000490 | references | pages [29] -->
acteristics. DOT, 03 Aug. 2016. Web. 22 Jan. 2017. http://dothr.ost.dot.gov/

<!-- b000491 | references | pages [29] -->
pdf/dot200711strathcplan.pdf.

<!-- b000492 | references | pages [29] -->
[13] Toledo, Tomer, and David Zohar. ”Modeling Duration of Lane Changes.”

<!-- b000493 | references | pages [29] -->
Transportation Research Record: Journal of the Transportation Research Board

<!-- b000494 | references | pages [29] -->
1999 (2007): 71-78. Web.

<!-- b000495 | references | pages [29] -->
[14] ”NYS DMV - Driver’s Manual - Chapter 8: Defensive Driving”. New

<!-- b000496 | references | pages [29] -->
York State Department of Motor Vehicles.

<!-- b000497 | references | pages [29] -->
2017.

<!-- b000498 | references | pages [29] -->
September 2011.

<!-- b000499 | references | pages [29] -->
Web.

<!-- b000500 | references | pages [29] -->
23 Jan.

<!-- b000501 | references | pages [29] -->
[15] ”Chapter 16: Stopping Distance.” SAFE DRIVE TRAINING - Defen-

<!-- b000502 | references | pages [29] -->
sive and Advanced Driving Courses available across Asia-Paciﬁc region. N.p.,

<!-- b000503 | references | pages [29] -->
n.d. Web. 23 Jan. 2017. http://www.sdt.com.au/safedrive-directory-

<!-- b000504 | references | pages [29] -->
STOPPINGDISTANCE.htm.

<!-- b000505 | references | pages [29] -->
28

<!-- b000506 | references | pages [29] -->
28
