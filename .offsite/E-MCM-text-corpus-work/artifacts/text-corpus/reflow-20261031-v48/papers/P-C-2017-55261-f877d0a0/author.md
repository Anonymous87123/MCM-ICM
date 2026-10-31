MCM/ICM

Summary Sheet

Once the stuff of wildly speculative science fiction novels, self-driving and cooperative vehicles are now at the cusp of mainstream adoption. As this technology comes closer to the point of deployment on real roads amongst conventional vehicles, it is necessary to understand how it will affect the characteristics and behavior of transportation systems worldwide. Seattle, WA and the surrounding King County area are prime subjects for investigation of this question, with traffic in the region being a chronic problem due to overcrowded roads and a high commuter population. In this paper, we aim to identify key impacts on the everyday experiences of highway travellers of the proporiton of self-driving and/or cooperative vehicles on the road, and use our findings to inform suggestions to policy makers.

Our solution consists of three main sections. In the first, we propose a macroscopic (continuum) model for the relationship between traffic flow, density, and mean speed. In addition to an improved justifiability over traditional empirical models, ours also allows for a straightfoward adjustment to reflect the percentage of self-driving/cooperative vehicles present. We find that at a given density of cars on the road, traffic flow and average speed increase fairly uniformly with that parameter, and show how an increase in overall number of cars on the road is likely to negate this beneficial effect.

Secondly, we develop a discrete model to describe lane changing dynamics in various levels of traffic, as well as how the performance of conventional, self-driving/non- interacting, and self-driving/cooperative cars compare in these cases. Our results indicate that the presence of self-driving cars on a highway can significantly decrease the average time required to find a sufficient gap when merging or changing lanes, with the greatest advantages arising for self-driving, cooperative cars. We also find that even interactions between conventional and autonomous vehicles can experience reduced delays during a lane change event.

Lastly, we test our model for the flow-density-mean speed relations on the real-world data provided in the problem. Although experimental traffic flows tend to be systematically higher than predicted by the theory (even after adjustment of certain key input parameters), the output generally confirms expected trends and enables us to identify times and locations of increased flux of vehicles onto or off of the highway.

Driving Towards the Future:

Modeling the Impact of Driverless

Vehicles on Traﬃc Patterns

Letter to the Governor

Dear Governor Inslee,

We are glad to hear that your administration is seeking out a diverse range of opinions in an eﬀort to inform policy making in your state around self-driving and cooperative vehicles. As America moves further into the 21st century, the pervasiveness and rapid advancement of technology in nearly every aspect of daily life can sometimes feel daunting. For example, in the case of driverless cars, it is not a trivial matter to assess potential risks and rewards for individual drivers and for society as a whole.

While we are far from providing a comprehensive study of this issue in our model for the eﬀect of driverless vehicles on traﬃc patterns, we feel that a few of our central results can provide some insight for lawmakers seeking to craft laws and regulations, make decisions about investment in certain infrastructures, and communicate eﬀectively with constituents about the eﬀects of self-driving cars on our roads.

The ﬁrst of these is that although increasing the amount of self-driving cars as a percentage of vehicles on highways is projected to relieve the burden of heavy traﬃc to some extent, these beneﬁts would quite likely be outweighed if the total number of vehicles were to increase. In other words, even if relaxing the driving age for these vehicles or providing tax incentives to use them may seem promising politically, these are actions which might encourage more people to drive, which has the potential to worsen overall traﬃc conditions.

That being said, our models indicate that self-driving and/or cooperative cars far outperform conventional drivers when it comes to changing lanes and merg- ing, which is a principle cause of delay on highways. We also show that, as would be expected, the ﬂux of vehicles onto or oﬀof highways increases dramatically during rush hours. These ﬁndings would indicate that oﬀering designated lanes for carpoolers in driverless vehicles during peak periods might mitigate jams while also promoting eﬃcient use of resources.

We hope you will ﬁnd this report riveting and that it will be helpful for you and your staﬀas you grapple with the legal complications of this new and exciting technology. We wish you the best in your endeavors.

Respectfully, Team 55261

1

Solution

Restatement and Clariﬁcation of the Problem

As the city of Seattle (and the broader King County area) reckon with the chal- lenges of adapting infrastructure designed and built in the late 20th century to current 21st century demands, technological advances such as self-driving, co- operative vehicles may oﬀer some respite. However, before investing signiﬁcant time and resources in accommodating such vehicles, it is desirable to know to what extent they are capable of mitigating the traﬃc jams that occur with some regularity on busy commuter highways. Here, we investigate the eﬀect of the ratio of self-driving and/or cooperative vehicles to conventional vehicles on the road, with the goal of identifying points of either diminishing or particularly increased returns with respect to improving traﬃc ﬂow. This is accomplished by developing a model for traﬃc ﬂow as a function of volume demand and road capacity, and subsequently applying the model to real-world data. *Note that throughout this paper, numbers in square brackets are citations to listed references and those in parentheses refer to the numbered equations.

Assumptions and Justiﬁcations

In the literature of traﬃc ﬂow modeling, there are three general paradigms: microscopic, mesoscopic, and macroscopic [1, 2, 3, 4]. These paradigms treat traﬃc as discreet vehicles, modular groups of vehicles, or a continuous ﬂow of vehicles, respectively. In the ﬁrst part of our model, designed to describe broader trends and patterns in traﬃc ﬂow, we chose to analyze the problem from the macroscopic view, for the following reasons. First, the data provided are not granular enough to be easily applied to microscopic formulae (i.e. behavior of individual cars/drivers); second, the structure of equations in the macroscopic model are more amenable to numerical analysis such as ﬁnite diﬀerence methods; third, the macroscopic paradigm is well-established in the ﬁeld of traﬃc ﬂow modeling and we therefore reason that it has at least a baseline capability to describe emergent patterns [1, 2, 3]. This is the main assumption shaping the basic structure of our ﬁrst model.

The second part of our model, designed to describe lane changing behavior, we consider the interaction of individual vehicles on the microscopic level. In this context the microscopic approach makes more sense, because a change in lane is a discreet event.

Additional assumptions are listed below, and while we provide justiﬁcation for all of them, they could generally be adjusted to reﬂect more realistic condi- tions, given additional time and computing resources.

• The distribution of traﬃc ﬂow over a 24-hour daily period is not uniform.

for weekends, weekdays, and an average. Both the average and week- day curves were consistent with the statement given in the problem that roughly 8% of traﬃc volume occurs during peak hours, so we arbitrarily selected the curve for weekdays.

• Given average daily traﬃc counts did not specify direction, and therefore it is necessary to make an assumption here. On any given day, a certain

2 stationed at a Seattle viaduct. Taken from [5].

proportion of drivers will be commuters (ie, intending to make a round trip), and a certain portion passing through to other destinations. We feel it is fair to assume that the drivers passing though will be distributed evenly between the ”increasing” and ”decreasing” directions (as deﬁned in the problem statement). The distribution among commuters is not as straightforward, since presumably a diﬀerent number commute out of the central metropolitan area than into it. However, based on the fact that the highways of interest are generally centered around downtown Seattle, as well as census data indicating that the majority (92% ± 0.7%) of com- muters to locations in King County are from King County [6], justify an approximation that traﬃc volume is also divided evenly between the two directions for commuter vehicles. In absence of a more reliable statistic, we used this assumption when analyzing the data, but this could be easily adjusted if desired.

• We were not able to ﬁnd data on whether any of the highways of inter- est contained traﬃc lights that require vehicles to stop periodically, and assume their absence, as is typical on busy urban freeways.

• For simplicity, we made a ”safe drivers assumption,” i.e. that at any density of traﬃc lower than the road’s maximal capacity at the speed limit, all cars travel at precisely that limit. This is obviously not reﬂective of real driving patterns, but most likely captures overall average behavior.

• Once the breaks of a car are applied, the distance required to bring that car to a complete stop is roughly quadratic in the initial speed [7]. This is best rationalized by the fact that an object’s kinetic energy is proportional to the square of its velocity, although there are many other physical eﬀects at play. We interpolated a stopping distance curve from two points: zero

3 Constant Name Description Value

Model Design and Justiﬁcation

Flow-Density-Mean Speed Relations Model

As stated in the justiﬁcations, our model treats traﬃc ﬂow as a continuous variable in space and time. The fundamental equation governing the relation between traﬃc ﬂow, q (number of cars passing a given point on the highway per unit time) and traﬃc density, k (number of cars per unit length of the highway at a given time) is:

∂q(x, t) + ∂k(x, t) = N(x, t), (1) ∂x ∂t where N(x, t) is the source ﬂux (cars per unit time per unit length), namely vehicles entering or exiting the highway from oﬀ- and on-ramps. Equation (1) is analogous to the standard conservation of matter equations in ﬂuid ﬂow or mass transport problems in physics. The space mean speed, us, is given by:

n 1 1 X (2) 1 n ui i=1 Here n is the number of cars in the space and time interval of interest, and ui is the speed of the ith car. q and k are related as [3, 12]:

q = usk (3)

We now invoke our ”safe drivers assumption” that, until a given part of the highway reaches its maximal density, us will be precisely equal to the speed

4 limit, denoted uf. This means us is a constant, so substitution of (3) into (1) gives a simple non-homogeneous transport partial diﬀerential equation (PDE) for k(x, t).

In order to investigate the eﬀects of this criterion, we must deﬁne maximal density. This maximal density is a function of us (as anyone who has ever been in a traﬃc jam has discovered empirically), because following distance (the space between the front of one car and the back of the car in front) decreases with mean vehicle speed. Our expression for maximal density at us is:

L(x, t) kmax(us(x, t)) = (4) dcar + dstop(us(x, t)) (We have made space and time dependence explicit here, for clarity). L(x, t) represents the number of open lanes at a given time and place, dcar is the length of an average car, and dstop(us) is the estimated distance it takes for a car to break to zero speed, starting from us. We deﬁne this distance as follows:

( trxnus + Au2 s + d0 For human driver dstop(us) = (5) Au2 s + d0 For driverless car

Here we are using the assumptions that a driverless car will have essentially zero reaction time, and that, once the car begins decelerating, stopping distance is roughly quadratic in initial speed. The constant d0 represents the small bumper-to-bumper gap maintained even when traﬃc is at a standstill. The constant A was derived from empirical data (see Model Testing section).

Therefore, us(x, t) is a piecewise function of k(x, t): if k(x, t) < kmax(uf), then us(x, t) = uf. Otherwise, us(x, t) is obtained by inverting (4), which amounts to solving a simple quadratic equation, given the forms in (5). We assume us will decrease just enough to adjust to the new density in excess of kmax. This eﬀect turns (1) into a nonlinear PDE in two variables.

It is worth making note at this point of a brief history of traﬃc ﬂow theory in the continuum treatment. In his seminal 1935 report, Greenshields reported, based on empirical data, a quadratic relationship between density and ﬂow [11]:

q = ufk −uf k2 (6) kj Alternatively, using (3),

us = uf(1 −k ) (7) kj Here, uf represents the ”free speed” of a car as it travels alone on the road, and kj represents ”jam density”, or the point at which us and q go to zero. As pointed out by Hall in 1992 [12], this model served as the foundation for analysis of traﬃc ﬂow for several decades, despite its reliance on a very small and sparse data set. Although equation (6) has the correct limiting behavior, there is little rationale behind its precise form; for example, it is unclear why a marginal increase in car density near the origin would result in an immediate decrease in mean speed. Other models (overviewed in [12]) have been proposed, and tend to be supported by the speciﬁc data set collected by the proponent of a given formula. In the absence of compelling evidence to agree with any single one of them, we believe our equation (restated in generality as (8)), which takes

5 more of a ”ﬁrst principles” approach, and shows reasonable limiting behavior, is entirely reasonable and furthermore allows for an educated investigation of the eﬀect of the ratio of self-driving/cooperative cars on the road, as emphasized by (5).

( k ≤kmax uf −trxn+√ us = (8) t2rxn−4A(dzero+dcar−L k ) k > kmax 2A Flow versus density and speed versus density curves for various percentages P of self-driving/cooperative cars on the road were generated by multiplying P trxn by (1 − 100) for each case. This is justiﬁed in the continuous limit where the density of cars is treated as an overall average rather than a property of discreet members. The results are shown in Figures 2 and 3. The constants in

= 0 (blue), 10 (red), 50 (yellow), 90 (purple) and 100 (green).

It is clear that in steady state conditions (no interruptions or ﬂux of vehi- cles onto or oﬀof the highway), the presence of self-driving vehicles allows for greater ﬂow (alternatively, mean speed) at the same density, which is desirable. However, the results in this analysis do not reveal clear equilibria or tipping points; the beneﬁts from an increase from P = 0 to P = 10 is similar to that for an increase from P = 90 to P = 100, and likewise for the comparison between P = 10 to P = 50 and P = 50 to P = 90.

A reasonable hypothesis regarding self-driving vehicles might be that intro- duction of the new technology would result in an increased number of people

6 P = 0 (blue), 10 (red), 50 (yellow), 90 (purple) and 100 (green).

who chose to commute by car, whether due to convenience or perhaps change in policy that would allow younger people or the elderly to ride in autonomous cars who might not have otherwise been able to drive themselves. Would an increase in the overall number of vehicles on the road outweigh the beneﬁts demonstrated above? In order to answer this, us was re-expressed as a function P of k and f = 100 as they have been deﬁned above:

q (1 −f)2t2rxn −4A(dzero + dcar −L −(1 −f)trxn + k ) us = (9) 2A Here we consider only the case where k > kmax, since below that point a change in density has no impact on the mean speed, by deﬁnition. If k increases by a factor of χ and we assume that 100% of the additional cars are driverless, then it is easily shown that the corresponding increase in f is given by:

∆f = χ(1 −f) (10) 1 + χ

Taking the total derivative of (9) yields:

7 δus = ∂us ∂k dk + ∂us ∂f df = −χL rxn −4A(dzero + dcar −L −1/2+ (1 −f)2t2   k ) k −1/2 rxn −4A(dzero + dcar −L B −(1 −f)B2  (1 −f)2t2 k ) χ(1 −f)  1 + χ 2A (11)

Here we have made the approximation dk = ∆k and df = ∆f. Since (11) is negative for all values of k for f < 1, it follows that an increase in density will necessarily result in a decrease in mean speed, even if the proportion of driverless vehicles increases. This result is shown graphically for a few selected values of χ and f in Figure 4. The eﬀect is visibly greatest at very low or very high densities.

f = 0.1] (red), [χ = 0.5, f = 0.5] (yellow). Number of lanes was taken to be constant at 3.

Lane Change Model

Another main aspect in traﬃc ﬂow is the interactions among vehicles as they change their lanes. A change of lane occurs when ramp vehicles merge into a highway stream, highway vehicles leave for minor roads, and when vehicles change into a diﬀerent lane of the route to prepare to turn or leave the road.

8 Such behavior negatively aﬀects traﬃc performance as it causes delay, decelera- tion and further impact the following vehicles. Self-driving cars and cooperating systems relieve the eﬀect by their higher sensibility, reliability, and adaptabil- ity. The following model simulates and three discrete scenarios and compares relevant factors to analyze self-driving and cooperating cars’ eﬀect on traﬃc performance. Our analysis makes use of selected traﬃc ﬂow formulae in [3].

Drivers determine whether or not to change lanes mainly by estimating the gap between the two vehicles adjacent to them, and accepting if the gap would be enough for them to merge in. Critical gap (tc) is deﬁned here as the gap for which the number of accepted gaps shorter than it is equal to the number of rejected gaps longer than it. Thus, an average vehicle would decide to merge if a gap is larger than the critical gap. We estimate the critical gap as the summation of the diﬀerence traveled between vehicle B and vehicle A during the lane change, and the safety distance from the following vehicle as in the previous model. An assumption must be made here about the average time it takes to change lanes; a study conducted by Toledo and Zohar by observing cars in a variety of traﬃc conditions [13] found that this value, which we call τ, was approximately 4.6±2.3 seconds. Assuming that car A continues to travel the same speed, u as it changes lanes and using the pythagorean theorem gives:

(uτ)2 −d2 p tc = uτ − lane + dcar + dstop(u) (12) u Where dlane is given in the problem statement as 12 feet, and dstop(u) was deﬁned in the ﬁrst section of the model.

Following a usual assumption for light-to-medium traﬃc, we assume the rate of vehicle arrivals on the lane is described by a Poisson distribution. Then the probability of x arrivals in the interval of time t is:

P(x) = µxe−µ for x = 0, 1, 2, ... (13) x!

where P(x) is the probability that x vehicles arrive in the interval time t, and µ is the average number of vehicles arriving in the interval time t.

The distribution of waiting times, i.e. gap (h) between two consecutive Poisson arrivals is exponential, which has density:

f(t) = λe−t t ≥0 for (14) where λ = µ t is the average number of vehicles arriving during a given time 1 interval. Expected value is λ, and therefore the probability that a gap h is larger than a ﬁxed gap t is:

P(h ≥t) = e−t t ≥0 for (15)

Thus, the probability Pc that a gap h is larger than critical gap tc is:

Pc = P(h ≥tc) = e−tc (16)

When an average vehicle begins to look to merge, it needs to wait until a gap larger than critical gap appears. The number of gaps the vehicle waits until a gap larger than critical gap appears follows a geometric distribution:

9 P(x = k) = (1 −P)kP for k = 0, 1, 2, ... (17)

where the probability P is given in (3). Therefore the expected value is 1 P . Thus for an average vehicle, the expected waiting time for a gap Ew is the expected number of gaps waiting times the expected length of each gap:

λ = etc Ew = 1 ∗1 e−tc ∗1 1 λ = (18) Pc λ Let ∆d be the distance between the vehicle’s position at which it starts to look for a gap and the exit that it needs to turn through. The criterion to avoid missing the exit, starting at speed u, is:

u ≤Ew = etc ∆d (19) λ If the vehicle cannot satisfy the above inequality with its current constant speed, it needs to decelerate, which would cause the vehicles behind it to decel- erate into the same speed, further aﬀecting the traﬃc ﬂow and density. Thus the minimum ∆d (∆dmin ) to successfully merge at the exit without decelerating is:

∆dmin = eλtcu (20) λ If ∆d > ∆dmin, the vehicle needs to decelerate into speed u′ = u−u0, which can be calculated from:

u′ = eλtc ∆d therefore, λ (21) u′ = ∆dλ eλtc

We simulated three scenarios of interactions between vehicle A, which is changing lanes, and vehicle B, which would take the place of A after the merge occurs (denoted as A →B). We will ﬁrst analyze under normal circumstances with average traﬃc volume, and then special cases during peak hours.

Case 1: Non-self-driving or self-driving vehicle merges before a non-self- driving vehicle.

This is the original circumstance, where tc is found using (12). The diﬀerence between vehicle A being self-driving or non-self driving is negligible, because it must still take full cautionary measures, not being able to predict the behavior of a conventional driver.

Case 2: Non-self-driving vehicle merges before a self-driving vehicle.

We assume that drivers can visually identify any self-driving vehicle. When drivers of vehicle A evaluate the gap and make decisions on merging, they con- sider the risk that vehicle B would exhibit unusual behaviors such as acceleration and ﬁnite reaction time. Such risk would greatly decrease for a self-driving vehi- cle as its behavior is more predictable under the control of a computer. Vehicle B cannot know vehicle A’s action beforehand because they cannot communi- cate, but the self-driving car has no human reaction time to adjust the gap if necessary. These two factors will inﬂuence driver A’s decision and cause the

10 critical gap to decrease. In our model, as a self-driving vehicle does not have reaction time, dstop(u0) = Au2 0 + dzero. This decreases the critical gap, caus- ing the probability of encountering an acceptable gap to increase, the expected waiting time to decrease, and minimum gap without decelerating to increase.

Case 3: When a self-driving vehicle merges before a self-driving vehicle in a cooperating system.

Within a self-driving cooperating system, vehicle A makes reservations to merge beforehand, and vehicle B is informed of the action and decelerates to create an optimal gap if needed. The coordinated system calculates an optimal time and position for vehicle A to merge, minimizing the negative eﬀect on traﬃc ﬂow. With the cooperation of vehicle B happening concurrently, vehicle A does not need as big a gap as in the preceding cases, as any gap will guarantee a successful merge. Assuming vehicle B decelerates into the same speed u′ as vehicle A, dstop = Au′2 + dzero. Given a distance ∆d, u′ and tc can then be calculated from this equation derived from the previous formulae:

lane + Au′2 + dcar + dzero (uoτ)2 −d2 tc = ln( ∆dλ p u′ ) = uoτ − (22) λ uo The lane change model was simulated using input data calculated from the ﬂow-density-mean speed model, shown below in Table 2. We took the percentage of cars that are self-driving to be 50%, and number of lanes to be constant at 3. The jam density kj (where us goes to zero) is therefore 638 cars/mile. We compared wait times for light, moderate, and heavy traﬃc (deﬁned by the ratio of k to kj) in the three cases outlined above; results are tabulated in Tables 4 through 6.

Density(k) Flow(q) Speed(u) Traﬃc type (cars/mile) (cars/sec) (mile/sec) 0.2*kj Light traﬃc 1.4200 0.0112 = 42.5333 0.5*kj Moderate traﬃc 1.5900 0.0005 = 106.3333 0.8*kj Heavy traﬃc 1.0180 0.0002 = 170.1333

Light Traﬃc Simulation Results

Case # dt (mile) dstop (mile) tc (sec) Pc Ew (sec) ∆dmin (mile) 1 0.0001 0.0275 2.4632 0.0303 23.2665 0.2606 2 0.0001 0.0197 1.7632 0.0818 8.6108 0.0964 3 0.0001 0.0194 1.7401 0.2492 5.6978 0.0638

In Case 3, we use ∆d = 0.09, a value close to dmin for Case 2, to solve tc and other variables. As expected from the previous model and scenario hypothesis, the interactions with self-driving and cooperating vehicles decrease the safety distance from the following vehicle (dstop) and therefore decrease the critical gap.

11 From Case 1 to 2, as a vehicle merges to precede a self-driving vehicle, the probability that an upcoming gap h is larger than critical gap increases by 170%, expected waiting time for an accepted gap decreases from 23.27 seconds to 8.61 seconds, and the minimum distance to successfully merge at the exit without decelerating decreases into 37% of original value. These changes would greatly reduce the eﬀects of lane changes on the traﬃc ﬂow on the road.

Moderate Traﬃc Simulation Results

Case # dt (mile) dstop (mile) tc (sec) Pc Ew (sec) ∆dmin (mile) 1 0.0001 0.0112 2.2650 0.0273 23.0506 0.1153 2 0.0001 0.0077 1.5650 0.0830 7.5738 0.0379 3 0.0001 0.0072 1.4710 0.3652 4.3535 0.0218

Similarly, we use ∆d = 0.03 in Scenario 3, a value close to dmin for Case 2. From Case 1 to 2, Pc increases by 204%, Ew and dmin decrease to 33% of their original values. The proportions and rates of change are similar in light and moderate traﬃcs, being slightly more prominent in moderate traﬃc due to its higher density.

In peak traﬃc, ﬂow decreases considerably, and therefore λ becomes small. The Poisson distribution in this case predicts a steep curve concentrated near the vertical axis; however, this would correspond to a situation in which drivers did not leave any distance between themselves and the back of the car in front of them; in terms of our previously deﬁned terms, dzero would be zero. In order to adjust the Poisson distribution to traﬃc analysis during peak hours, we specify a ﬁnite minimum time gap tmin in order to restrict the gap range. Then the probability that a gap h is larger than critical gap tc to be acceptable is:

P(h ≥tc) = e−λ(tc−tmin) (23)

We estimate the minimum gap distance in Case 1 as the minimum safety distance to keep from vehicle B when the speed of vehicle B is zero. Given that minimum gap is tested as an extreme situation, we include a factor of 1/3. Then the minimum gap is calculated as:

min = dzero t1 (24) 3uo We take the minimum gap for Case 2 to be smaller, as some drivers be- lieve self-driving vehicles (which we assume are visually identiﬁable) will always decelerate to assist them with merging even with a very small gap. Thus we estimate t2 min as 50% of t1 min:

min = t1 = dzero t2 min (25) 2 6 After adjusting for heavy traﬃc, we obtain the results shown in Table 5.

If vehicle A does not have enough time to ﬁnd an acceptable gap, it must decelerate in order to complete the lane change in time to reach its destination (for example, an exit on the freeway). Such situations are represented in our model as when ∆d < ∆dmin, and the vehicle reduces speed from uo to u′. We

12

Heavy Traﬃc Simulation Results

Case # dt (mile) dstop (mile) tc (sec) Pc Ew (sec) ∆dmin (mile) 1 0.0003 0.0066 3.1309 0.0413 23.7926 0.0476 2 0.0003 0.0052 2.5884 0.0717 13.6961 0.0274 3 0.0003 0.0002 2.5841 0.0768 13.2509 0.0265

wish to measure the eﬀect on traﬃc performance when an event such as this occurs.

Given ∆d, the reduced speed u′ can be calculated from (21). As the vehicles behind A must keep the minimum safety distance with respect to one other, the new density behind A, k′, is the reciprocal of the sum of the average vehicle length and the safety distance:

1 1 k′ = dstop(u′) = (26) Au′2 + trxnu + dcar + dzero We make the simplifying assumption that the speed of the vehicles behind A travel at a new constant and uniform speed in order to obtain the new traﬃc ﬂow:

q′ = k′u′ (27)

The eﬀect of this mass deceleration can be described by shock wave theory [3], which assumes an instantaneous change in speed at one point and uses a conservation of ”mass” (cars) argument, along with the fundamental relation (3), to calculate the rate of propagation of the resulting ”wave” of slowed cars. This rate, uw, is given by:

uw = q′ −qo (28) k′ −ko As the shock wave moves along opposite the direction of the main traﬃc stream, the growth rate of the queue of slowed vehicles, ug, is:

ug = u′ + uw (29) Knowing u′ and ∆d, we calculate the average waiting time that vehicle A would need to merge at the exit or enter point is Ew. Therefore the expected (average) time to successfully merge is Ew 2 . Then the length of the queue, lq, and the number of vehicles involved, nq until the vehicle ﬁnishes merging are:

lq = ug ∗Ew (30) 2 nq = lq ∗k′ (31)

Based on these equations, we ran the following simulation to compare the improvement from Case 1 to Case 2 on delays resulting from the shock wave phenomenon. Due to the diﬀerence in the minimum distance, while ∆d is in the range of ∆d1 min < ∆d ≤∆d2 min, merging will result in speed reduction in Case 1 but not in Case 2. Thus, the merging in Case 2 will not cause a shock wave, whereas merging in Case 1 will. For each traﬃc type subgroup, we set ∆d

13 equal to ∆d2 min, and the results and eﬀects for Case 1 is shown in the following tables:

Simulation of ”shock wave” due to lane change delay, Case #1 Traﬃc type uo(mile/sec) ko(cars/mile) qo(cars/sec) ∆d(mile) Light traﬃc 0.0112 42.5333 1.4200 0.1153 Medium traﬃc 0.0050 106.3333 1.5900 0.0379 Heavy traﬃc 0.0020 170.1333 1.0180 0.0218

u′(mile/sec) k′(cars/mile) q′(cars/sec) Traﬃc type uw(mile/sec) ug(mile/sec) Light traﬃc 0.0050 89.8846 0.4453 -0.0206 0.0255 Medium traﬃc 0.0016 161.2373 0.2649 -0.0241 0.0258 Heavy traﬃc 0.0009 182.8054 0.1672 -0.0671 0.0681

q′ k′ Traﬃc type lq (miles) nq (cars) qo ko Light traﬃc 0.3 26.7 0.3136 2.1133 Medium traﬃc 0.3 47.9 0.1666 1.5163 Heavy traﬃc 0.81 147.99 0.1643 1.0745

We can see from Tables 6 through 8 the impact on traﬃc performances when a queue results from merging in Case 1. For example, in light traﬃc, the situation decreases the temporary ﬂow into 31.36% of original value, increases the temporary density into 200.11% of original value, and causes a queue of 0.30 miles with 26.7 vehicles involved. All these negative eﬀects would not occur in Cases 2 or 3 (involving self-driving and/or cooperative cars) because the vehicles do not need to decelerate for merging.

Model Testing and Error/Sensitivity Analysis

In order to apply our model to the given data, we replicated the curve for weekday traﬃc volume in Figure 1 and normalized it to obtain a distribution function, which was scaled by the ”Average Daily Traﬃc Count” statistic given in the problem for each point in space on each highway (use of the same distri- bution for all points in space discussed in the Assumptions and Justiﬁcations section). This provided estimates for traﬃc ﬂow at all points (s, t). We used a 30 second time interval, and for space intervals we used the distances between consecutive mile markers. Those intervals are roughly characteristic of average car speeds on the highways, since many markers were spaced less than one mile apart.

Solving for u(x, t) and k(x, t) from ﬂow values using (3) and (8) required the additional assumption that all points lay on the upper half of the q −u curve shown in Figure 5, since that relation is noninvertible. We reasoned that a transition to the lower half of the curve would manifest as a noticeable feature

14 in the ﬂow distribution curve, for example shown in Figure 6, corresponding to an approach towards standstill conditions. This type of scenario would be interesting to investigate in future studies.

Upon analyzing the empirical ﬂow data, it became apparent that maximal ﬂow values signiﬁcantly exceeded those predicted by the curve in Figure 5, using our initial input parameters for the constants in Table 1. In order to address this, we lowered the values of the constants A, trxn, and dzero to 0.0245 ft/mph2, 0.5 sec, and 0 ft, respectively. These reﬂect lower bound estimates found in other references [14, 15]. Despite this adjustment, some q values still exceeded the maximum prediction, and this was handled by holding u at its value for the maximum theoretical q (indicated in the ﬁgures below).

Once q(x, t), u(x, t), and k(x, t) were all known, values were plugged into (1) to determine vehicle ﬂux onto or oﬀof the highways. In doing this we hoped to identify locations and times where many cars would likely be changing lanes or merging, resulting in increased delays as described in the Model Design section.

Several representative plots are shown in Figures 7 and 8. Due to the error in predictions of q described above, the data show certain areas of discontinuity, but nevertheless give a rational description of traﬃc patterns over the course of one day. Some notable features are listed below.

• Traﬃc ﬂux shows a noticeable increase during times of heavier traﬃc, since a greater number of cars are entering and exiting the freeway during peak hours. Without conducting a rigorous analysis, Figures 7 b and d also seem to reﬂect the location of major interchanges along I-5 (with I-90 near mile 160 and with I-705 near mile 130).

15 transition to lower branch of q −u curve, indicated by arrow.

• As shown in Figure 8 b, traﬃc ﬂux generally follows traﬃc ﬂow in mag- nitude throughout the day at most times (spikes in this graph likely cor- respond to the artiﬁcial cutoﬀon q imposed when processing the data).

• Our model indicates a rapid decrease in mean speed once kmax, given in (4), is reached. As shown in the ﬁrst section of our model, increasing the percentage of self-driving cars on the roads would help to forestall this precipitous decline, but only if measures are taken to insure that the technology does not lead to a net increase in total number of vehicles in the system.

• The eﬀects of the temporal distribution of ﬂow values appear much stronger than those of the spatial distribution, which is somewhat to be expected since the Average Daily Traﬃc Counts show little discernible correlation in space. While the approximation of a universal time distribution in traf- ﬁc ﬂow is a rough estimate, our ﬁndings nevertheless suggest that lanes dedicated speciﬁcally to autonomous vehicles may confer the most signif- icant beneﬁt during peak periods, especially given our ﬁndings of drastic reduction in lane changing times for these cars in the second section of our model. Therefore, policymakers may ﬁnd that the availability in time (rather than in location) of designated lanes for self-driving/cooperative cars is the more important factor; for example, express lanes might be opened only during rush hours.

Additional ﬁgures for other highways are shown in the appendix.

16 bound, 1:50pm; (c) Southbound, 12:50am; (d) Southbound, 1:50pm

17 of a 24-hour period at mile marker 155.18 on I-5 North. Dashed red lines indicate the point at which empirical data exceed the maximum prediction of our model.

18 Because our model relies heavily on the deﬁnition of the relationship between space mean speed and vehicle density, it is useful to understand the relative sensitivity of that equation to the various constants used in (8). These are, to restate: A, the quadratic coeﬃcient for speed dependence of stopping distance; trxn, the linear coeﬃcient; dcar + dzero, the presumed gap between the front bumpers of consecutive cars in standstill traﬃc; uf, the nominal speed limit; and L, the number of lanes. For each of these, the constant value given in Table 1 was varied from 0 to double the original value (L was given a baseline value of 3). Results are depicted graphically using us vs k curves in Figure 9.

baseline values for (a) A; (b) trxn; (c) dcar + dzero; (d) uf; and (e) L. Values progress through 0, 50, 100, 150, and 200% of their baseline values in the order blue, red, yellow, purple, green.

The behavior of these graphs reﬂects common sense intuition (another ad- vantage of our model over empirical forms which use parameters that do not carry a physical meaning). For example, it is logical that mean speed would decrease at a given density along with the number of lanes, while increasing as the driver’s reaction time decreases (shortening the requisite gap between cars). It is worth noting that the curves are divergent as the value of dcar + dstop goes to zero, as this would imply the possibility of inﬁnite density of vehicles.

19

Discussion:

Strengths and Potential Areas for Improve-

ment of the Model

Strengths of the ﬂow-density-mean speed model include the following:

• The model is not overly complex and, as such, does not take much compu- tational power in order to calculate, which allows for real-time stream of input data to generate a real-time stream of output data with insigniﬁcant delays.

• The model is general enough to allow for additional parameters, such as the delay in response time of self-driving cars which can be incorporated into the reaction rate trxn.

• The model incorporates known mathematical relationships between speed, density, and ﬂow, but does not propose any equations that do not carry some measure of physical or rational motivation.

• The number of lanes is a function of distance and time which accommo- dates for time-dependent lane changes, for instance during traﬃc acci- dents, construction work, or lane additions, in addition to the data pro- vided for analysis.

• The diﬀerence between the reaction times of human-driven cars and self- driving cars is accounted for in our model.

Strengths of the lane change model include the following:

• The solution uses concepts from the macroscopic continuous approach in ﬂow-density-mean speed model and a discrete simulation approach in the lane change model. This ensures a measure of continuity between the two.

• The model measures the lane change eﬀects by both common factors of critical gap and expected waiting time and the special case of shock waves and vehicle queues.

• The model simulates lane change in three scenarios with diﬀerent degree of interaction of self-driving and cooperating vehicles, and presents the eﬀect by comparing the simulation results numerically.

• Adjusted with the daily peak traﬃc hour distribution, the simulation sep- arately discuss three subgroups of light, moderate, and heavy traﬃc and compare their degrees of eﬀects.

• The stochastics approach simulates the random process and analyzes the expected values of variables to measure the eﬀects on traﬃc performance.

• The model agrees with ﬂow-density-mean speed model by using same as- sumptions and main relationships, and integrates by using some outputs and formulas of ﬂow-density-mean speed model as simulation input and model construction.

20

Weaknesses of the ﬂow-density-mean speed model include the follow-

ing:

• The model does not account for interchanges or merging lanes in traﬃc and their eﬀects on the mean speed or traﬃc density.

• The model does not account for cooperation between self-driving cars or the interaction between self-driving and non-self-driving cars.

• The model does not account for diﬀerences in car length of self-driving cars from the current average car length.

• The results presented made use of an invariant, daily, peak traﬃc hours distribution which was bimodal in nature which does not account for the diﬀerence in typical traﬃc and holiday or weekend traﬃc.

• The results presented used a ﬁnite diﬀerence approximation for the deriva- tive, which introduces error for ﬁnite time and space intervals.

Weaknesses of the lane change model include the following:

• The main assumption of Poisson distribution of arriving vehicles ﬁts heavy traﬃc less well. The factors we include to adjust for peak hours are esti- mated and do not fully reﬂect the situations in heavy traﬃc.

• The measurement of most variables by expected value may not reﬂect special conditions such as peak hours and cooperating systems accurately.

• The critical gap, which should be obtained from real collected data dis- tribution by nature of deﬁnition, is calculated by physics formulae in the model.

• The measurements of critical gap for Case 3 and reduced speed in shock wave analysis are functions of ∆d, thus the comparison results are subject to the choice of ∆d.

• The simulation is conducted on data of one segment of highway and lacks the generality to be applied to all circumstances.

21

Appendix

bound, 1:50pm; (c) Westbound, 12:50am; (d) Westbound, 1:50pm

22 of a 24-hour period at mile marker 14.32 on I-90 East. Dashed red lines indicate the point at which empirical data exceed the maximum prediction of our model.

23 Northbound, 1:50pm; (c) Southbound, 12:50am; (d) Southbound, 1:50pm

24 course of a 24-hour period at mile marker 15.76 on I-405 North. Dashed red lines indicate the point at which empirical data exceed the maximum prediction of our model.

25 Eastbound, 1:50pm; (c) Westbound, 12:50am; (d) Westbound, 1:50pm

26 course of a 24-hour period at mile marker 5.39 on SR-520 East. Dashed red lines indicate the point at which empirical data exceed the maximum prediction of our model.

27
