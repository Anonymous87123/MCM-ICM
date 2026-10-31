Problem Chosen 2022

MCM/ICM

Summary Sheet

Summary

With the intensification of drought in southwestern United States during the past 20 years, Lake Mead and Lake Powell, as important water suppliers, are facing water shortage. To solve a series of problems of optimizing water resources allocation, here are three models.

For Model 1, the whole process of resources allocation carefully simulated, we propose a Resources Allocation Network(RAN) of water availability and electricity requirements. In the case of sufficient resources but without the additional water, the allocation problem is transformed into a linear programming problem. Then the corresponding algorithm (Time-varying Linear Optimization Algorithm) is designed to solve this problem efficiently. The results of the optimiza- tion show that the Allocation Network can last for 21 days without the additional water with the allocation plan of the five states.

For Model 2, to measure the scarcity of general usage water and hydropower as well as evaluate the value of resources brought to each state when making a decision, we introduce the notion of Marginal Utility in economics and set up the Ii function, the Utilityi function and the V aluei function (i = 1, 2, · · · , 5) , the important basis of the Model 3 (IPV model), to quantify the competing interests of water availability and electricity production.

For Model 3, considering the situation of inadequate water resources and hydropower, we innovatively introduce the Auction Theory to try our utmost to close to the optimal of the allocation, namely Pareto optimum. Thus the independent Private Value (IPV) Model was proposed and it can be solved out by the Generalized Backwards-Shooting (BS) Algorithm. Based on the V aluei function (i = 1, 2, · · · , 5) proposed by the Marginal Utility model, the allocation scheme proposed by the IPV model is better than the Resources Allocation Network (Model 1), and the calculation results show that the scheme is more economical and more sustainable.

Then we deal with more complex situations with our models and give detailed descriptions about the whole principle. At the same time, we did sensitivity analysis for the models and the robustness of the models is verified. In order to meet the needs of the model, we finally give a specific rule for calculating the amount of fine to promote water and electricity conservation measures for citizens and businesses.

By careful analysis of the strengths and weaknesses, we further suggest possible future work and make a conclusion.

Theory; Marginal Utility; Independent Private Value (IPV) Model;

1 Introduction

1.1 Background

According to historical research, the reservoir was first built around 600 BC. With the devel- opment of science and technology, the function of reservoirs has gradually expanded to irrigating farmland, supplying domestic water, preventing floods and developing hydropower to help maintain people’s normal life.

However, because of the deterioration of the ecological environment in recent years, in some areas, people face a serious shortage of water resources in their daily life. In 2021, the United States suffered a severe drought. As the important source of water supply for the western, the water levels of the Lake Mead and Lake Powell were declining, creating a new historical low. Take Lake Mead as an example. In the past two decades, the water storage of the Lake Mead has always been lower than its normal volumetric capacity, and the current water storage is only 34%. The water level of Lake Mead also dropped to about 1067 feet, approaching the minimum power generation level of 950 feet of Hoover Dam. [1].

Short-term water saving and electricity saving can only alleviate a temporary shortage of water. Therefore, how to allocate and utilize water resources has become an urgent problem to be solved. This is also the problem to be solved by our model.

1.2 Problem Restatement and Analysis

• Problem One: Establish a model to calculate how much water needs to be pumped from those two lakes to meet the demand under the conditions that the water level of Lake Meade is M, the water level of Lake Powell is P, and the demand of water is fixed. Besides, how long the the first model can lasts and how much additional water are needed to meet the fixed demand.

• Problem Two: A standard for dealing with competition is formulated in advance, and then how to allocate general usage water and hydropower usage water when there is interest competition.

• Problem Three: The model needs to include practices when water is not enough which means supply quantity is less than demand.

• Problem Four: The models are able to respond to these situations, including the relevant factors in affected areas change, the proportion of other renewable energy increases, and water-saving and electricity-saving are taken.

• An Article:Write an article which wii be published in the journal Drought and Thirst to illustrate the results of the model.

1.3 Overview of our work

To avoid complicated description , intuitively reflect our work process, the flow chart is show as the following figure:

2 Assumptions

• Assumption 1: All water in Lake Mead and Lake Powell is used for general usage and hydropower production only.

• Assumption 2: Both water and hydropower for Arizona, California, Colorado, New Mexico and Wyoming all come from the Hoover Dam and the Glen Canyon Dam.

• Assumption 3: In the calculation of water consumption in the five states involved, public supply and domestic are classified as residental, irrigation, aquaculture and livestock as agricultural, industrial, thermal power and mining as industry. When it comes to hydropower, commercial and residential are classified as residential, five percent of industry as agriculture, and the rest part of industry and transportation as industry.

• Assumption 4: The loss of water and electricity during transport is proportional to the transporting distance.

• Assumption 5: To simplify the calculation, take the lake as a cylindrical container.

• Assumption 6: On the way of water flowing from Lake Powell to Lake Mead, the effects of tributaries are not taken into account solely, because the river has much more mainstream water than tributaries.

3 List of Notation

Symbol Meaning

v(t) the volume of water available for general usage from dam i to state j at time t ij u(t) the volume of water available for the hydropwoer production from dam i to state ij j at time t w(t) the effectively produced electric energy through ultra-high voltage grid from ij dam i to state j at time t dwater the demand on general water usage of state j within unit time j delec the demand on hydropower of state j within unit time j V (t) the water storage amount of dam i at time t i

Notice: The index i = 1, 2 refers to the Glen Canyon Dam and the Hoover Dam respectively. And the index j = 1, 2, 3, 4, 5 refers to state Arizona, California, Wyoming, New Mexico and Colorado respectively.

4 A Resources Allocation Network of River Colorado

The flow direction map of the River Colorado is shown in the following figure [3]. In the map, locations of two dams (the Glen Canyon Dam, the Hoover Dam) and two lakes (Lake Powell, Lake Mead) are clearly marked. For a dam, the direction of water flows that we care about are the resources are used for agricultural, industrial and residential, (b) while the green arrow indicates that some water resources are used for power generation and flood discharge.

direction of water for general usage and the direction of water for hydropower, as you can see below figure [3].

Since there exist inevitable natural loss and consumption in the process of water transportation and hydropower, we introduce transportation rate to measure the transmission efficiency from dam i to state j, namely the percentage of successful transmission. If not specifically mentioned in the following article, the transportation rate is defined as above.[4]

Let v(t) ij be the volume of water available for general usage from dam i to state j and let αij be the transportation rate, we get the following conservation equation.

2 αijv(t) X ij = dwater , j = 1, 2, 3, 4, 5 (1) j i=1

It guarantees that the total amount of v(t) ij transported to state j meets state j’s water demand . The same is true for electricity. Let w(t) dwater ij be the effectively produced electric energy through j ultra-high voltage grid from dam i to state j and let γij be the transportation rate, we derive the identity equation of electric quantity as follows.

2 γijw(t) X ij = delec , j = 1, 2, 3, 4, 5 (2) j i=1

where delec represents the state j’s electricity demand. j

To update volume parameter V (t) for Lake Powell to V t+1 , we need the following iterative 1 1 formula.

5 V (t+1) = V (t) (v(t) 1j + u(t) X − 1j ) + vf∆t (3) 1 1 j=1 where vf represents the rate of inflow from the upstream of the Glen Canyon dam while ∆t represents an interval of a certain length of time.

The volumetric renewal formula for Lake Mead is similar. What is different is that the inflow from the upstream of the Hoover dam is the outflow from the Glen Canyon dam due to electricity production.

5 5 V (t+1) = V (t) (v(t) 2j + u(t) u(t) X X − 2j ) + (4) 2 2 1j j=1 j=1

The specific process is shown below (figure [5]).

In order to simplify the model and make it easy to be solved, the model of reservoirs is abstracted as a cylinder and the water level h(t) at time t can be calculated by the cylinder volume formula. i

= V (t) h(t) i , i = 1, 2 (5) i Si Where Si represents for the base area of the lake.

Then, we should further consider how uij (the amount of water utilized to generate electricity) which is converted to w(t) ij (the amount of electric energy effectively converted from the potential energy) by a generator. The way it works in physics is as follows according to the Law of Conservation of Mechanical Energy.

w(t) ij = βiρwateru(t) ij ghi, i ∈{1, 2}, j ∈{1, 2, 3, 4, 5} (6)

Where βi is the efficiency coefficient of the generator.What’s more,ρwater and g stands for the density of water and the gravitational acceleration respectively.

Finally,we need ensure that electricity is generated only when hi ≥hlowest .Since the power of i generator i is proportional to h(t) i , we denote the proportionality coefficient as ηi and denote the interval as ∆t.

5 ηih(t)  hi ≥hlowest i ∆t, w(t) X i ij ≤ , i = 1, 2 (7) 0, else j=1 What’s more, in order to save energy, we should reduce v(t) ij and u(t) ij as much as possible.

Taking all the factors above into account, we obtain the following optimization problem by considering the formulas Eq (1)(2)(3)(4)(5)(6)(7).

2 5 2 5 v(t) u(t) X X X X min ij + (8) ij v(t) ij ,u(t) i=1 j=1 i=1 j=1 ij

2  αijv(t) X ij = dwater  , j = 1, 2, 3, 4, 5  j    i=1   2    γijw(t) X ij = delec  , j = 1, 2, 3, 4, 5  j    i=1    5   V (t+1) = V (t) (v(t) 1j + u(t) X  − 1j ) + vf∆t   1 1    j=1   5 5   V (t+1) = V (t) (v(t) 2j + u(t) u(t) X X s.t. (9) − 2j ) + 2 2 1j  j=1 j=1    = V (t) h(t)  Si , i = 1, 2  i  i   w(t) ij = βiρwateru(t) ij gh(t)  i ∈{1, 2}, j ∈{1, 2, 3, 4, 5} i ,     5  ηih(t)  hi ≥hlowest  i ∆t, w(t)  X i ij ≤ , i = 1, 2    0, else   j=1    vij, wij ≥0, i ∈{1, 2}, j ∈{1, 2, 3, 4, 5}     V (t+1) ≥0, i = 1, 2  i

4.1 Solution for the Allocation Network: A Pseudo-Code

The problem Eq(8)(9) is a time-varying linear optimization problem. Therefore, our algorithm idea is to use an iterative method, in which we optimize the water and hydropower allocation of the network in the (t) step. The following is the pseudo-code (Algorithm [1]) for this stage, which gives a good representation of the entire code flow.

Algorithm 1: Time-Varying Linear Optimization

αij, γij, vf, Si, βi, ρwater, g, hlowest  , for i = 1, 2, j = 1, 2, · · · , 5 input : i n o v(t) i,j , u(t) , for i = 1, 2, j = 1, 2, . . . , 5, ∀t = 1, 2, . . . ij , t1, t2 output :

n o V 0 (1), V 0 (2), h0 (1), h0 , t ←0

1 Initialization:

(2) 2 while h(t) and h(t) 1 > hlowest 2 > hlowest do 1 2 t ←t + 1 3 if V (t) > 0 and V (t) > 0 then 4 1 2 n o P2  v(t) i,j , u(t) j=1 v(t) j=1 u(t) P5 ij + P2 P5 ←argmin , for 5 ij ij i=1 i=1 i = 1, 2, j = 1, 2, · · · , 5 else if V (t) ≤0 and V (t) > 0 then 6 1 2 n o v(t) ←0, for j = 1, 2, · · · , 5 7 1j n o P5  v(t) 2,j, u(t) j=1 v(t) j=1 u(t) 2j + P2 P5 ←argmin , for 8 ij ij i=1 i = 1, 2, j = 1, 2, · · · , 5 else if V (t) > 0 and V (t) ≤0 then 9 1 2 n o v(t) ←0, for j = 1, 2, · · · , 5 10 2j n o P5  v(t) 1,j, u(t) j=1 v(t) j=1 u(t) 1j + P2 P5 ←argmin , for 11 ij ij i=1 i = 1, 2, j = 1, 2, · · · , 5 else 12 BREAK 13 if h(t) or h(t) 1 ≤hlowest 2 ≤hlowest for the first time then 14 1 2 t1 ←t · ∆t 15 5 Update: V (t+1) ←V(t) (v(t) 1j + u(t) X 1 − 1j ) + vf∆t 16 1 j=1 5 5 Update: V (t+1) ←V(t) (v(t) 2j + u(t) (v(t) 1j + u(t) X X 2 − 2j ) + 1j ) 17 2 j=1 j=1 ←V (t+1) Update: h(t+1) , for i = 1, 2 i 18 i Si 19 t2 ←t · ∆t

According to the constraints in Eq [9], when the water level of the dam is lower than the minimum water level of the power generation, but higher than the minimum water level of the dam, the dam can still provide water resources, but cannot generate hydropower. What is more, the algorithm is terminated immediately when the water levels of both dams are below their respective minimum water levels, or cannot meet the demands of the individual states.

4.2 Results and Analysis

By looking up the relevant data, we get the data on the water level of the two dams (tab [2]) and the Agricultural, industrial, residential demand in five states (figre [4.2]).

the Name of the Dam Minimum Minimum Water Level Average Maximum Water Level for Power Generation Water Level Water Level

65m 110m 142m 216m Glen Canyon Dam 79m 119m 158m 221m Hoover Dam

For the water level P and M given by the problem, we compute the allocation schemes in three cases respectively,

• P = 142m (dark blue line), M = 158m (red-brown line), the average water level Before 18 days, the curve was a straight line, indicating that a single dam had enough water for five states. From the 18th day to the 21st day, the curve has twists and turns, indicating that there is a dam that cannot generate electricity (but can supply water). After the 21st day, the two dams were unable to meet the water and electricity needs of the five states.

• P = 110m (brownish yellow line), M = 119m (purple line), the minimum water level for power generation Before 4 days, the curve was a straight line, indicating that a single dam had enough water for five states. After the 4st day, the two dams were unable to meet the water and electricity needs of the five states.

• P = 216m (green line), M = 221m (light blue line), the maximum water level Before 32 days, the curve was a straight line, indicating that a single dam had enough water for five states. From the 32th day to the 49st day, the curve has twists and turns, indicating that there is a dam that cannot generate electricity (but can supply water). After the 49st day, the two dams were unable to meet the water and electricity needs of the five states.

Obviously, the algorithm is closely related to time and the initial water level. Taking these three cases into consideration, we choose the first case as the average. We get that in these 21 days, in the absence of rain and other water supply, the water allocation for the Problem One is (visualized results shown in figure [4.2]):

There are some conclusions for the Resources Allocation Network:

• From the 1th day to the 18th day, the Glen Canyon Dam distributes 4.42 × 108m3 to WY each day; the Hoover 2.38 × 108m3 to AZ, 1.12 × 109m3 to CA, 1.23 × 108m3 to NW and 4.45 × 108 to CO each day.

• From the 19th day to the 21th day, the Glen Canyon Dam distributes 2.66 × 108m3 to AZ each day, 1.35 × 109m3 to CA, 4.42 × 108m3 to WY, 1.26 × 108m3 to NW and 4.56 × 108 to CO each day.

• The Allocation Network can last for 21 consecutive days without the additional water.

• The water allocation plan recommend re-run the model every 21 days.

• There is P5 j=1 u2j = 3.51 × 107m3/day allowed to flow from the Colorado River into the Gulf of California.

With the help of data from USGS [9] and EIA [10], two pie charts of water usage and hydropower allocation for each department in each state are made in figure[7] and figure[8].

Usage Allocation Allocation The result of the first model,which contains the water usage and hydropower allocation for each department in each state,can be made into sankey diagrams better showing the flow of the process in figure[4.2].

Usage

5 Marginal Utility Model: Resources Interests and Valuation

of Each State

Due to the large number of variables in the model, we tend to do the following simplification to avoid making the expression verbose.

function(Resourcei) = function(argwater , indwater , reswater , argelec , indelec , reselec ) (10) i i i i i i

where argwater , argelec represent the water resources and hydropower allocated to the agricul- i i tural in i-th state respectively, and similarly, indwater , indelec to the industrial, reswater , reselec to i i i i the residential. We will refer to Resourcei as six variables including argwater , indwater , reswater , i i i argelec , indelec , reselec . i i i

There is a strong nexus between water and energy [2]. For example, machines in factories need to be heated by electricity and cooled by water, and in farmland, they can only be driven by electricity for irrigation. Therefore, we assume that only when water and hydropower are allocated in a certain proportion, the two resources can jointly play the maximum effect. In economics, we call the result coincide with Pareto Optimum. The Marginal Utility function is often utilized in economics to help determine whether or not the final result coincides with Pareto optimum. By similar ideas, we define a function whose range is in [0, 1] and increases first and then decreases, with the only condition that the maximum value is: water and hydropower are in a certain proportion. It is obvious that the magnitude of the negative gradient of the marginal utility efficiency function represents the corresponding profit of the unit effort along the direction. The definitions related are as follows.

Ii(Resourcei) = 2 ln e(xi+1) 2 ∈[0, 1] (11) xi + 1   argwater /karg + indwater /kind + reswater where xi = 1 reselec /kind and e is the Euler’s constant. i i i argelec indelec 3 i i According to the definition of the Marginal Utility by R. Layard et al. (2008) [1], the key issue for Competing Interests is how this effect changes with income, but not how strongly income affects the utility of the states. Therefore, we define the utility function as follows,

1−µwater 1−µelec −µwater −µelec Utilityi(Resourcei) = y + z i i i i i i (12) 1 −µwater 1 −µelec i i

where yi = argwater + indwater + reswater and zi = argelec + indelec + reselec . The parameter i i i i i i µwater , µelec represent the effect induced by the change of the independent variable on the utility i i of the states. However, It is difficult to determine the value of µwater and µelec , especially in the i i absence of data. In this paper, to simplify the model, we determine these two parameters µwater i and µelec based on the demand for water and electricity in different states. i

By multiplying Ii function and Utilityi function, we derive the V aluei function, which means that the five states assess the value of the same resource differently. We implement V aluei function to quantify the competing interests of water availability and electricity production.

V aluei(Resourcei) = Ii(Resourcei) · Utilityi(Resourcei) (13)

Notice: IPV Model in Section 6 is based on the Marginal Utility Model, so we will discuss the results of the Marginal Utility Model in the next section.

6 Auction Theory for Competing Interests: Independent Pri-

vate Value (IPV) Model

From now on, the water from the Colorado River has become more and more scarce, and if we continue to exploit it without restraint,the entire river would be drained to the last drop of water. In this sense, we should at our utmost to take less water from the Colorado River. But water and electricity are essential to the basic needs of every industry. This suggests that we need to find another solutions to make the whole program feasible and sustainable.

Based on the above considerations, we introduce the following IPV model (figure[11]).

In point of fact, one of the primary causes of the scarcity of water and electricity resources in the western United States is the widespread wasting habits among the American population. The Colorado River is becoming more and more dangerous and both water and hydropower resources are becoming increasingly valuable. But many Americans are unabated in their habits of extravagance and waste. The current crisis could be ameliorated considerably if the waste could be minimized. As a good means of monitoring, fining wasters is an effective method. In addition, fines can raise a large amount of money, which helps a lot in our IPV model.

Here comes the core of the IPV model. The model is mainly based on Auction Theory, which is an important branch of microeconomics. Historically, auction theory, which was awarded several Nobel Prizes in economics , has its unique role and significance. In our model, the creative introduction of this theory and modification combined with specific scenes is to achieve the optimal solution (in economics we call it Pareto Optimality [3]) of the whole problem. The specific algorithm to figure out this problem will be explained later and here we only need to know that it is at the core of the model and how it works in the whole system.

• At first a certain amount of water and electricity were divided equally among five states. Treat each state as an independent bidder and then there are five bidders bidding for the remaining water. Each bidder will weigh its own interest and decide whether to pay his bid(mainly from fines and other sources can be included). At the same time, the highest bidder gets the resources, which meets the bidding rules we all know.

• After the rest of the resources having been divided up, each state can manage the money left itself. Our suggestion is to put the money left as much as possible to the construction in the development and exploration of renewable energy. That is beacause such investment will be positive in the long run.

• The money from the auction for the remaining resources will be used as investment capital to help those states, who profit least or none from the auction, in their construction. In this way, the successful bidder can use capital in exchange for resources they deem worthwhile.

• Those water and hydroelectric resources are also reckoned as a compensation to alleviate the shortage of water and electricity. Although such compensation is limited, it is believed that such benefits are still positive for the bidder contributing to the auction because the bidding behavior is based on sufficient interest considerations. In short, those who bid for resources obtained at least a short-term gain from the auction, and the results for them were positive.

• One the other hand, the states that benefit least from the auctions get the corresponding investment to help with construction, and the results must be positive in the long run. They can gradually wean themselves off the river’s associated resources and turn to seawater desalination, solar power generation and so on as to replace.

In general, both sides benefit from it, and the pressure on the river decreases over time, which is conducive to ecological restoration and sustainable development.

Thus, we consider here an Independent Private Value (IPV) first-price auction [4] [5]: The N = 5 states , called bidders, submit sealed bids and the highest bidder wins and pays his bid. Only those whose private valuation is higher than the reserve price, R, set by the auctioneer submit competitive bids.

Different states (bidders) value the water and the electricity resources differently, following the marginal utility [1], which means that more resources bring less incremental utility. Each state is assumed to be risk neutral with utility, and characterized by a distribution function Hi on a common support [pleft, pright]. Bid functions are denoted by φi, i = 1, · · · N.

Let t = φi(p) denote the equilibrium bid submitted by state i with private signal p ∈ [pleft, pright]. And let p = λi(t) denote inverse bid functions. State i with signal p ∈[R, p] submits a bid t, which is solution of the optimization problem.

Y q∈(R,pright) (p −q) t = arg max Hj(λj(q)) (14) j̸=i

Defined by the First Order Conditions, the following formula derived as,

" N # ′ H i(λj(t)) Y H−1   (Hi(λi(t))) −t · , i = 1, · · · , 5 1 = (15) i Hi(λj(t)) j=1,j̸=i

6.1 Solution of the Independent Private Value (IPV) Model

In order to solve such problem, Gayle and Richard (2008) [6] generalized the Backwards- Shooting(BS) Algorithm of Marshall et al. (1994) [7] which is a numerical solution in auction. Gale and Richard’s algorithm relies on valuation support which is equally spaced subdivisions. According to the [6], the expected profit of the state i is given by

Z t∗ n ′ · H i(λi(t)) Y H−1   i (H(λi(t))) −t Hi(λi(t)) · Gi(R) = [H(λj(t))] (16) R j=1

The Generalized Backwards-Shooting(BS) Algorithm incorporates the following steps [6]. First, we input Taylor-series expansions of H−1 to the algorithm (the method [3] to calculate H−1 i i will be mentioned below),

where iteration equation Eq.(17)(18)(19)(20) in the Generalized Backwards-Shooting(BS) Al- gorithm [2] are:

Algorithm 2: Generalized Backwards-Shooting(BS) Algorithm

1 while from J = 1 to n do To calculate aiJ, iterative Eq(19) in step J −1 into Eq(17) for next step through 2 ′(λi(t)) h i ′(λi(t)) = H(λi(t)) · H H H(λi(t)) Calculate biJ through the Taylor-series Expansions 3 Calculate ciJ, using the links of Eq(18) and Eq(19) 4 Then, calculate diJ through Eq(20) 5

∞ X aij(t −t0)j H(λi(t)) = (17) j=0 ∞ X H−1 bij(tt0)j i (H(λi(t))) −t = (18) j=0 ∞ ′(λi(t)) H X cij(t −t0)j H(λi(t)) = (19) j=0 ∞ X H−1 dij(x −x0)j i (x) = (20) j=0

To calculate the Taylor-series expansions mentioned above in Algorithm [2], the following steps are incorporated:

Algorithm 3: Computation of Taylor-series Expansions

1 Construct an equally spaced grid {pj; j : 1 →J} for the interval [0, 1] 2 Calculate the the corresponding grid for the inverse CDF F −1, {qj; qj = F −1(pk);

j : 1 →J} by using a standard root finder

3 Construct a B-spline interpolator for F −1, invoking the IMSL subroutines DBSNAK (to

construct a kont sequence) and DBSINT (to compute B-spline coefficients) by [8]

4 Invoke the IMSL subroutine BSCPP to convert the B-spline interpolator into a

piece-wise polynomial approximation

6.2 Results and Analysis

It has been assumed that in the case of scarce water resources only come from the upstream of the River Colorado, that is, 505m3 flow per second is the only source of water for the whole river. In this case, we take this source as an auction, which is auctioned by the five states at the highest price. According the generalized the Backwards-Shooting(BS) Algorithm by Gayle and Richard (2008) [6], we compute the best competitive strategy which may bring the best interests for all the states and Mexico,

According to the IPV model, we divide the whole water resource into two pieces and set a corresponding ratio (a parameter) to modify the total amount of auctioned water resources, while the unauctioned portions are used for average distribution to five states. Here is the results in tab [3].

Allotted Water after the Auction AZ CA WY NM CO

none for auction (control group) 57.0149 227.3120 77.6765 36.3715 106.7070

50% for auction 57.0149 227.3120 77.6765 36.3715 106.7070 growth rate of 50% for auction 1.0478 0.9355 1.0418 1.3498 1.0872 70% for auction 55.0809 223.3868 76.8827 37.1827 112.0978 growth rate of 70% for auction 1.0191 0.9272 1.0342 1.3770 1.1206 100% for auction 51.0264 222.0100 74.5972 37.3735 119.9878 growth rate of 100% for auction 0.9581 0.9242 1.0123 1.3833 1.1684

of Each State

In figure [12], compared with the control group (the case of all water resources are equally distributed to the states, blue bar in the figure), the more water resources are auctioned, the less water resources are obtained in California, while the water resources obtained in the other four states are increased or almost equal, which means that the equality between different states has improved. What is more, the sustainable use of natural resources is respected by our world today. On the other hand, in the figure, the variable "rate" represents the ratio of the value obtained by the state after a competitive game to that by the control group. Obviously, the values of Wyoming, New Mexico and Colorado are rising, and the overall values of the five states are also rising. In summary, the IPV auction model has promoted the development of the five states. Moreover, the money paid for bidding can be used to compensate Mexico or regions with relatively backward water conservancy systems.

7 Sensitivity Analysis

–Our Model Dealing with More Complex Situations

7.1 Growth or Shrinkage in Affected Areas

In general, If there is population, agricultural, and industrial growth in Affected areas, the demand for water and hydropower in these areas will certainly rise. In order to avoid more losses and derive development, those states must be willing to bid for more water than before, even if the price is much higher. At this point, they are willing to accept higher price because even one more drop of water is reckoned to be more meaningful and valuable to them than ever before. The increase in auction prices improves the amount of investment fund for those benefit least in the auction. According to our previous interpretation of the model, the investment should be utilized for construction to ease the pressure on energy needs in the long run, At the same time, to reduce the high dependence on both water and hydropower resources from the Colorado River basin in the future. This helps a lot to achieve long-term sustainable development.

On the contrary, when the shrinkage occurs, the total pressure of resource demands on the river basin will decrease, and the corresponding bidding expenditure will also decrease.

• Population & Agricultural & Industrial

We assume that there is some perturbation, σ, in one of these three, which affects the maximum time the model will last without additional water.

Specifically, from the Figure [13], it is not difficult to see that, under slight perturbations, days that the model lasts remain basically unchanged. The error fluctuation keeps no more than three days, which shows the good robustness of our model.

7.2 Increase of the Proportion of Renewable Energy Technologies

First of all, the increase of the proportion of renewable energy technologies means less energy consumption and more efficient use of resources. In our model, this is equivalent to the gradual decrease of the demands for resources from the Colorado River basin, which is mainly reflected in the gradual shift of the focus of resource utilization.

In fact, the improvement of the proportion of the renewable energy (especially when it exceeds the initial default value we set in the model) will extend the duration of the model to a certain extent, which can also be verified in the sensitivity tests of the model. This is also confirmed in our tests. As shown in the Figure [14], good resistance to disturbance is again demonstrated.

7.3 Water and Electricity Conservation Measures

As a matter of fact, once additional water and electricity conservation measures have been implemented, the efficiency of water and electricity usage would be greatly improved. In our model, additional water and hydropower conservation measures comes in the form of penalties for wasteful practices, namely fines. Under the pressure of fines, more efficient use of water and electricity could help reduce unnecessary wastage. In our model, this has great significance for long-term development and is the fundamental guarantee of long-term interests.

However, if there isn’t a complete and effective penalty rules, it would be difficult to realize the plans and visions. Here we offer the following suggestions for constructing a set of penalty rules.

Finetotal(i) = Finebasic(i) + Fineextra(i) = i ∗Finebasic + Utility(i) (21)

where the total amount of the i-th penalty is composed of the basic penalty amount and the addi- tional penalty amount. The total amount of the i-th basic penalty is equal to i ∗Finebasic, and the extra penalty amount represents the opportunity cost of the i-th waste, which can be well described by the utility function.

8 Discussion

8.1 Strengths and Weaknesses

8.1.1 Strengths

• Comprehensive consideration

We take into account as many details as possible, such as the possible losses during the transportation etc. Our model also comprehensively considers the whole interest, and pursues the global optimization under the premise of satisfying the interest of each state and Mexico.

• Specially innovative

We utilize economic concepts and theory(like marginal utility, auction theory) to establish models, which provides a unique and revolutionary view of the resource competition system.

• Good visualization

The visualization work is done well by us, including the framework of our work, the vi- sualization of locations of dams and two lakes, the overview of state water distribution by double-deck pie chart,the schematic diagram of IPV model etc.

• Highly extensible

The problems about optimizing resource allocation are much common in daily life. The model has strong theoretical guarantee, and can be applied with a little modification combined with the actual background. What’s more, our models are less dependent on data.

8.1.2 Weaknesses

• Rough approximation

In the assumption 5, we regard the lake as two cylinders to calculate the volumes. Although the calculation is simplified, there must be an error with the actual situation. In this problem, we think that the volume calculation is not the core problem that needs to be solved. Due to time constraints and schedule requirements, we finally choose to simplify this step.

• Idealized design

Our models are intended to capture the essence of the problems through idealized and abstract descriptions first. Therefore, the model is relatively complete in theory, but there maybe a deviation from the actual, for the model lacks practical testing.

8.2 Future Work

The essence of this problem is the optimal allocation of resources. Solving this kind of problem is of great significance in our daily life. In the case of full resources, many problems involve the allocation of hundreds or even thousands of objects. In this regard, our future work can focus on extending the model to a larger number of objects and improving the computational speed of the algorithm, or designing algorithms that can be applied to a wider range and are more convenient and efficient.

In the subsequent model introduced in the case of resources shortage, due to time constraints, we did not jump out of the problem and have an in-depth research. For example, we put forward using the model to provide bidders benefiting least in the auction with considerable benefits to develop technology and infrastructure like desalination, solar power and wind power generation. Our model is able to explain the existence of long-term returns theoretically, but how to maximizing profits and where should be selected as the optimal construction site have still yet to be solved. These questions are related to, but not central to, the problem. However, It is undeniable that the solution of these problems also contributes to the detailed implementation, which needs further reasearch.

9 Conclusion

Based on our work, it is not difficult to draw the following conclusions. Since the Colorado River is one of the most important source of general usage water and hydropower for the western United States, necessary protective measures neeed to be taken. In addition, despite the fact that the United States is a developed country with abundant recources, American citizens should be encouraged to develop good habits of saving water and electricity. As a supplement, we believe that imposing fines on wasteful behaviors is an effective way. What’s more, for long-term sustainable development, priority should be given to the development and construction about new renewable energy sources. Only in this way could the Colorado River be revitalized. Only by this way can the rights of both the United States and Mexico be protected simutaneously.
