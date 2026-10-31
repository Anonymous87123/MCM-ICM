For ofﬁce use only For ofﬁce use only

T1 F1

T2 F2

T3 F3 Problem Chosen

T4 F4

MCM/ICM

Summary Sheet

Summary

Located on the Zambezi River, the Kariba Dam holds back the world’s largest reser- voir. After so many years, despite efforts to slow its structural problems, the Kariba Dam is in great danger.

To address this situation, our paper provides a detailed analysis of one option, re- moving the Kariba Dam and replacing it with a series of ten to twenty smaller dams along the river. We propose a model iMoDS(Integrated Model of Dams in Series) to fully analyze different aspects, such as the number, placement, and height of the new dams. In the meantime, we can set the total water management capabilities as same as the existing dam, providing protection and water management options for Lake Kariba.

We ﬁrst analyze the water ﬂow using Manning formula which helps us to analyze a single dam. After that, we simulate a dam in real life with 3ds MAX, show the simpliﬁed dam model on it and derive its storage capacity and building cost.

iMoDS model consists of three main submodels, Risk Cost Model, Power Supply Ability Model, and Series Safety Model. For explanation, there is a ﬁgure which connects all related parts together.

Risk Cost Model aims at every single dam. It implements risk analysis, using accept- able risk ratio, Pf. Thus, it can make a good balance between cost and safety.

Power Supply Ability Model also aims at every single dam, the sum of which mea- sures the beneﬁts our dam system can produce.

Series Safety Model measures how safe the whole system is, based on an ideal distri- bution of dams along a river.

Then we use AHP to analyze these three submodels and propose iMoDS.

To get enough data, we surveyed the literature and other sources. Using genetic algorithm to determine the number and placement, we further solve each dam’s height.

Another section of our paper discusses strategies for addressing several situations, including the balance between safety and costs, protection for Lake Kariba, guidances for emergency water ﬂow situations and extreme water ﬂows.

In the end, we make sensitivity analysis and discuss strengths and weaknesses.

7 Model Analysis

19

7.1 Sensitivity Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19

Impact of Planned Working Years N for a Dam . . . . . . . . . . . . 7.1.1 19

Impact of Extreme Condition ratio α . . . . . . . . . . . . . . . . . . 7.1.2 19

7.2 Strengths and Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20

7.2.1 Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20

7.2.2 Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20

8 Conclusion

20

Brief Assessment Report 21

Option 1: Repairing the existing Kariba Dam . . . . . . . . . . . . . . . . . . . . 21

Option 2: Rebuilding the existing Kariba Dam . . . . . . . . . . . . . . . . . . . 22

Option 3: Removing the Kariba Dam and replacing it with a series of ten to twenty smaller dams along the Zambezi River . . . . . . . . . . . . . . . . 22

Appendices

24

Appendix A Implemented Genetic Algorithm

24

Appendix B

Fitness Function 24

1 Introduction

1.1 Problem Background

Over ﬁfty years ago, a giant was born on the Zambezi river, along the border be- tween Zimbabwe and Zambia. It provides the two countries with a huge amount of hydropower. The world’s largest reservoir is held by it. This giant was named as Kariba Dam.

Kariba Dam is a double curvature concrete arch dam with 128 metres (420 ft) tall and 579 metres (1,900 ft) long. It was designed to have six spillway gates, which have a discharge capacity of 9500m3/s. Total storage, or overall water management capabilities, is up to 180.6km3. [1].

Kariba was designed as a single prupose hydropower project, but as it turned out both ﬁshery and tourism bacame important beniﬁts [1]. Since it was built, this dam is more a landmark than an actual dam for tourists. This area provides them with wa- ter sports and sufﬁcient wildlife resources. Not to mention the fact that Kariba water helps develop the industry of agriculture and ﬁshing. Every coin has two sides. Despite these economical beneﬁts, there are other great environmental impacts, like population displacement and resettlement, and drowned vegetation. [2]

However, such a great construction is in great danger and dire need of maintenance. Kariba is threatned by severe droughts, which has lowered the reservoir’s volume to twelve percent of the capacity. What makes the situation more complicated is that if we reﬁll the reservoir, then the dam is very likely to collapse. Due to unexpected ﬂoods and climate changes, the dam seems to be greatly dangerous.

1.2 Our Work

To address this situation, we have three different options: repairing, rebuilding, or removing the existing Kariba Dam and replacing it with a series of ten to twenty smaller dams along the Zambezi River.

In this paper, we focus on the last option and provide a detailed analysis of it. We propose an integrated model of dams in series. This model not only recommends the number and placement of the dams along the Zambezi River, but also make a balacne between safety and costs. Our system have the same overall water management capa- bilities as the existing Kariba Dam while providing greater levels protection and water management options for Lake Kariba.

In Section.2, we state several basic assumptions. Section.3 contains the nomenclature used in model statement. Section.4 provides sufﬁcient details about our model. Section.5 carrys out experiment and analysis about our proposed model. Section.6 provides de- tailed strategies dealing with several conditions. At last, we further study our model in Section.7 and make some conclusions in Section.8.

2 Assumptions

Our model makes the following assumptions:

1. In the phase of modeling, we don’t consider extreme conditions on the river, like waterfalls, water cutoff seasons. Because these conditions require extremely big data. They are even unnecessary for in real life dams have dynamic strategies to handle them. We will discuss emergency water ﬂow situations in another Section.

2. Other existing dams are ignored. They are not as big as Kariba Dam. Few data about other dams on the river are accessible, especially thier effects on runoff of the river and slope of its hydraulic grade line. This assumption is ﬂexible because it only affects the input data of the river, but not our model.

3. We simpliﬁes the water ﬂow into an open-channel ﬂow. Open-channel ﬂow has a free surface. Based on this assumption, we are able to estimate the average velocity of the river’s water ﬂow.

3 Nomenclature

In this paper we use the nomenclature in Table.1 to descibe our model. Other symbols that are used only once will be described later.

4 Statement of our Model

In this section, we will discuss all details about our model. This model takes several ﬁelds into consideration, ranging from liquid ﬂow theory to economy. To begin with, we ﬁrst investigate the behavior of water ﬂow. Then we provide our integrated model of dams in series. This model makes a great balance between safety and costs.

Symbol Deﬁnition i the ith dam in a series of small dams Xi Distance from the river’s beginning to dam i Series(X) Value of safety evaluation under a series of dams Supply(Xi) Value of power supply ability at dam i Risk(Xi) Risk Cost of dam i Pf Acceptable risk ratio Q(Xi; t) Volumetric ﬂow rate at time t for dam i k(Xi) Slope of the hydraulic grade line at dam i N Planned working years for a dam n Number of small dams M Overall water management L Length of the Zambezi River d The width of the Zambezi River α Extreme Condition ratio h(Xi) The height of a dam i

4.1 Behavior of Water Flow

In our model, we need to calculate power supply ability of each dam. One of the key variables is the average velocity of water ﬂowing when it reaches a dam. We have assumed the water ﬂow in the Zambezi river to be a channel ﬂow. Thus, we can employ an empirical formula, the Manning formula, to estimate this velocity. [3]

v = k nRh2/3S1/2 (1)

where:

• v is the cross-sectional average velocity;

• n is the Gauckler-Manning coefﬁcient;

• Rh is the hydraulic radius (L; ft, m);

• S is the slope of the hydraulic grade line or the linear hydraulic head loss (L/L);

• k is a conversion factor between SI and English units.

This formula can be obtained by use of dimensional analysis. With this formula, it is easy to ﬁnd that when water ﬂow reaches a dam, its average velocity only depends on the channel slope S and hydraulic radius Rh.

4.2 Analysis of A Single Dam

Figure.2 is the simulation of a dam in real life. We determine a reservoir’s storage capacity based on this model. In the literature, Cone method [4] is a common method. Its formula is: n ∑ √ 1 Ai × Ai+1) × △Li CA(Xi) = 3(Ai + Ai+1 + i=0 where:

• V is the capacity of reservoir;

• Ai is the area of ith cross section;

• △Li is the gap between ith and i+1th cross section.

For simplicity, we further consider that a reservoir has the areas enclosed by contours in Figure.2, which is colored in black. We use the parameter d to denote the width of the river. Thus, we derive the capacity formula:

CA(Xi) = 1 3(1 2d × h + d × h) × h(Xi) k(Xi) = h(Xi)2 3k(Xi)(3 2d) = h(Xi)2d (2) 2k(Xi)

The other key measurement is a dam’s building cost.

A basic function contains two parts, construction cost and other unavoidable cost. Construction cost is linear to the volume of the dam. To calculate this volume, we need the bottom width. Actually it is linear to the pressure Pa = ρgh [5].

Note that here we calculate the volume of the dam, but not the volume of the reser- voir that is calculated by Equation.2.

Finally, it is reasonable to simplify other cost to a constant β, because every construc- tion work has its initial cost. And there is a safety factor for compressive stress σ [5].

Cost(Xi) = λρgh(Xi) × d × h(Xi) + β 2σ = λρgdh(Xi)2 + β (3) 2σ where λ a is volume-to-expense coefﬁcient.

4.3 iMoDS: Integrated Model of Dams in Series

After investigating water’s behavior when it reaches a dam and a single dam, we further proposed an integrated model of dams in series. This model consists of three main parts, Risk Cost Model, Power Supply Ability Model, and Series Safety Model. As illustrated in Figure.3, our model works as an integrated machine which evaluate both a single dam and the whole group. Basically, we can regard it as a nonlinear programming method. Three main parts work as three features derived from different ﬁelds. They are also assigned with different weights according to their own contribution to the whole system.

4.3.1 Prerequisites

1. Q(Xi; t) The value of Q(Xi; t) is volumetric ﬂow rate at time t for dam i. In our modeling phase, for simplication we replace Q(Xi; t) with Q(Xi; t) to denote the annual av- erage volumetric ﬂow rate. In our paper, d remains the same, so volumetric ﬂow rate upstream is greater than the one downstream.

Later we will further discuss and provide speciﬁc guidance for extreme water ﬂows ranging from maximum expected discharges to minimum expected discharges.

2. k(Xi) = dElevation(x) |x=Xi dx The placement of each dam is described by the distance from the river’s starting point, Xi. We set the slope of the hydraulic grade line at dam i as the value of k(Xi).

More details about k(Xi) will be discussed in Section.5.1.

4.3.2 Risk Cost Model

As Figure.3 shows, Risk Loss and Fundamental Investment determine the output of Risk Cost Model. To build a dam, there are two key factors that we should keep in mind: cost and safety. However, before we try to ﬁnd an equilibrium between them, we have to change it into a math problem. Here we combine them based on risk analysis, a widely used theory in economics. Based on this theory, we numerically determine the safety loss and fundamental cost with an acceptable risk ratio. Because acceptable risk ratio measures the extent that a person focus more on safety than merely cost.

Cost - Fundamental Investment Cost reveals how feasible a dam project is. Investors always expect to spend less money while maintaining the same water management abil- ity. A ground truth is that investors must spend more money while paying more atten- tion on safety. Thus, Pf is negatively related to the cost. Its exponent is set by experiment. Slightly modify Equation.3, then it is the equation we need here:

Fundamental Investment = Cost(Xi) (4) P 1.1 f

Given Pf, Equation.4 can measure one dam’s fundamental investment.

Safety - Risk Loss Safety reveals how environmental-friendly a dam project is. Projects that pay less attention on safety will result in a high possibility of collaspe. We call it Risk Loss. Equation.5 is the evaluation model. [1 −(1 −Pf)N] is the probability distribution that measures the possibility to collapse. So, we deﬁne the loss at dam i as:

collapse probability * (1+ indirect damage index)*Volumetric ﬂow rate

Risk Loss = [1 −(1 −Pf)N]α(1 + λ)Q(Xi; t) (5)

where α is an coefﬁcent that reveals how likely and serious a river is to suffer from extreme conditions.

This method contributes to the evolution of risk-based dam safety assessment meth- ods.

Risk(Xi) = Risk Loss + Fundamental Investment

Figure.4 shows the function of Pf and Risk Value. Curves with different colors de- note different value of α. From top to bottom, each time α is decreased by 0.05.

Observation 1 For each curve, it is strictly decreasing on the left while increasing on the right.

Illustraion Risk Value is not a monotonic function because Risk Loss is a monoton- ically increasing function of Pf while Fundamental Investment is a monotonically de- creasing function of Pf.

Compared with different curves, the larger α is, the higher Risk Cost Observation 2 is, with the extreme point moving left.

If the coefﬁcient α is larger, then it reveals that for a same Pf the govern- Illustraion ment has to handle higher potential losses. Thus, to balance the fundamental cost and safety, the government will have a lower Pf. That’s exactly what our function reveals.

4.3.3 Series Safety Model

Our system removes the Kariba Dam and replaces it with a series of ten to twenty smaller dams. In this model, our goal is to assess a series of dams along the river and give a mark. Researches show that if dams are built uniformly on a river, then this dam system can be operated to produce greater beneﬁts than operating a single large dam.

To quantify safety based on locations, we consider two factors involved. One is the average distance between two neighbouring dams. The other is the degree of even dis- tribution. Here we bring in and modify Pearson Chi-Square test to represent it. The more even this distribution is, the safer we consider this system is. Thus, we get the following formula.

d Series(X) = (6) ∑n−1 (di−d)2 d2 i=1 e where d is the average distance between two neighbouring dams.

4.3.4 Power Supply Ability Model

Kariba was designed as a single-purpose hydropower project. Embarking on any hy- dropower generation project, it is essential to calculate its amount of hydropower. In our model, the last part is to estimate this kind of economic beneﬁts. If we sum up the power supply of each dam, this model can numerically calculate our new system’s hrdropower supply. Based on the hydropower equation [6], intuitively we get Equation.7 which is a function of the hydraulic head and rate of ﬂuid ﬂow.

How much work a unit of water can do depends on its weight times the head. And the power available from a dam can be measured by the density of water, acceleration due to gravity, the ﬂow rate, and the height of fall.

Supply(Xi) = ηρgh(Xi)Q(Xi; t) (7)

where:

• η is the dimensionless efﬁciency of the turbine;

• ρ is the density of water in kilograms per cubic metre;

• g is the acceleration due to gravity.

4.3.5 Integration

Based on previous illustrations, we are able to integrate all these features together.

• Series(X) Positively related to the safety level. The higher Series(X)’s score is, the better our system is.

• Risk(Xi) There is an equilibrium between investment and loss which reaches the lower bound of this model. We always want to save money while ensuring safety.

So, the lower Risk(Xi)’s score is, the better our system is.

• Supply(Xi) Positively related to power supply. The higher Supply(Xi)’s score is, the better our system is.

To make all features equal, we need feature scaling, or data nomalization, because these features all have a broad range of values. If we don’t process thier value, the result of our integrated model may be governed by one of them. In our model, we implement rescaling method. This method rescale the range of features to sacle the range in [0, 1]. The general formula is like this:

x −min(x) ′ = x max(x) −min(x)

where:

• x is an original value;

′ is the normalized value.

• x ′, After resacling, normalized Series(Xi), Risk(Xi), and Supply(Xi) is Series(Xi) ′ respectively. As we can see, Risk(Xi) is negatively related. ′, and Supply(Xi) Risk(Xi) Thus we modify it to be positively related by a modiﬁed rescaling method.

′ = Series(X) × n −1 Series(X) L ′ = min(Risk(Xi))/Risk(Xi) Risk(Xi) ′ = Supply(X) × n −1 Supply(X) L

In our model, the goal is to minimize the Final Value. Thus, we scale Supply(Xi) and Series(X) into [−1, 0]. Write our model into a nonlinear programming form then we get the Integrated Model of Dams in Series:

n n ∑ ∑ ′ + ′ + ′ max Final Value = Series(X) Risk(Xi) Supply(Xi) i=1 i=1 Xi ≤L, ∀Xi ∈[1, n] s.t n ∑ CA(Xi) ≥M i=1 10 ≤n ≤20, n ∈Z Xi ≥0, ∀Xi ∈[1, n]

where:

n n ∑ ∑ ′ + ′ + ′ Final Value = Series(X) Risk(Xi) Supply(Xi) i=1 i=1 n ∑ × n −1 d min(Risk(Xi))/{Cost(Xi) = + + ∑n−1 P 1.1 (di−d)2 L f d2 i=1 i=1 e n ∑ [1 −(1 −Pf)N]α(1 + λ)Q(Xi; t)} + ρgηLk(Xi)Q(Xi; t) i=1

4.3.6 Ranking Submodels with AHP

The analytic hierarchy process (AHP) is a structured technique for organizing and analyzing complex decisions, based on mathematics and psychology. Our goal is to rank previous three submodels and assign weights to iMoDS model.

Feature Weight Risk Cost 0.5403 Series Safety 0.3478 Power Supply Ability 0.1119

Table.2 shows the result of AHP. We then assign them to the model derived in Sec- tion.4.3.5:

n n ∑ ∑ ′ + 0.54 ′ + 0.11 ′ max Final Value = 0.35Series(X) Risk(Xi) Supply(Xi) i=1 i=1 Xi ≤L, ∀Xi ∈[1, n] s.t n ∑ CA(Xi) ≥M i=1 10 ≤n ≤20, n ∈Z Xi ≥0, ∀Xi ∈[1, n]

5 Implementation

5.1 Data

We tried to ﬁnd some existing dataset about dams, but failed. Thus, in this paper we ourselves analyzed many textual data and ﬁgures from reliable sources and experiment with them. Google Earth provide us with the elevation proﬁle of the Zambezi River. We use Matlab to ﬁt a curve which is shown in Figure.5. The set of blue spots is the raw data while the red curve represents the river’s elevation. This curve is ﬁtted as an eighth-power polynomials.

f(Xi) relies on these data.

river’s source while Y-Axis is altitude.

Thanks for the basin analysis [7], we are able to analyze the river’s ﬂow data. Fig- ure.6(a) and Figure.6(b) show the Zambezi River mean annual river ﬂow.

Q(Xi; t) relies on these data.

(a) 2D version. It includes surrounding coun- (b) 3D version. It includes the river’s elevation tries and cities. changes.

represents the upstream, midstream, and downstream, respectively. Width of each band measures the value of mean annual river ﬂow.

5.2 Number and placement of the new dams

5.2.1 Whole Procedures

1. Set all small dams to have equal height;

2. Use heuristic algorithm, like generic algorithm, to run iMoDS model;

3. Based on the set {Xi} which is found in Step 2, use Equation.8 to reset each one’s height.

4. Test constraint by Equation.9. If it doesn’t meet, tune {Xi} and go to Step 3.

5.2.2 Determining the number and placement by genetic algorithm

The optimization of a dam group is high dimensional, multilevel, and nonlinear. Classical algorithm that solves linear programming problems are impossible to ﬁnd the global optimum. Heuristic algorithm, however, can solve this optimization problem. Genetic algorithm(GA), based on a antural selection process that mimics biological evo- lution, is one of them.

In this section, we give an analysis about the number and placement of dams, and also provide a recommendation. However, if the height of each dam is dynamic, it will be a problem of over 20 dimensions. For simpliﬁcation we assume that each small dam is in equal size.

Because of the simpliﬁcation, h(Xi) is a constant. The whole evaluation is sensitive to the variables, {Xi}, Pf and n. To ﬁnd the optimal solution, we use genetic algorithm to simulate the evaluation process. Codes are listed in Appendices.

Weights of three key features have been provided by AHP. Risk Cost dominates the other two features. To maximum min Risk(Xi) and meet the constraint, total water man- Risk(Xi) agement M, the algorithm will select Pf to an optimal value which has been introduced in Figure.4, i.e., locating dams to relatively gentle slopes. Although Power Supply takes a small weight, the value will greatly increase when the dam is on a steep terrain. Fi- nally, Series is more likely to let these dams in a evenly distribution. Considering the interaction between three features, the ﬁnal placement shows like Figure.7.

Figure.8 shows that when n = 13 and Pf = 0.0024, the evaluation reaches the peak value, or the optimal value. It is cogent for our model.

This result is convincing. If the quantity of dams n increases, then:

1. ∑min(Risk(Xi)) decreases. Although the height of each dam is smaller, sum of ini- Risk(Xi) tial cost β increases.

2. ∑Supply(Xi) increases and then decreases. With n increasing, the ideal hydropower supply goes higher. But when n goes to large, Series(X) will restrict it to goes

Distance Xi/m Elevation/m Order of Dam 1 288.3 1160.2 2 494.5 1136.3 3 664.4 1084.55 4 810.0 1057 5 843 932 6 879 790 7 954 651 8 1160 638 9 1323 520 10 1552 468 11 1729 453 12 1924 257 13 2098 195 lower.

3. Series(X) is not relevant to the quantity of n.

Thus, in this decision-making process, there is an equilibrium between ten and twenty. We ﬁnd that it is n = 13 with Pf = 0.0024.

Table.3 shows the optimal result of this new dam system. From dam 1 to dam 13, we recommend each dam’s placement. Note that DistanceXi denotes the distance from the river’s source to dam i. Due to the restriction in this nonlinear programming, the overall water management capacities is the same as the existing Kariba Dam.

5.2.3 Determining the height of each dam

Here we eliminate the assumption that each small dam is in equal size. If we refer to Section.4.2, the height of a dam is really a key factor to the ﬁnal evaluation as it inﬂuences the system’s risk cost and power supply that these dams can totally provide. It is critical to determine the height of each dam so that the system’s ﬁnal value can be optimized. Given Pf, a single dam’s contribution to the whole system(iMoDS model) is a function of one variable, h(Xi). So we can ignore Series(Xi). To optimize the contribution, let the labelled with its height. The blue areas are each dam’s corresponding reservoirs.

differential equation to be zero:

Supply(Xi)′ −Risk(Xi)′ = 0 ηρgQ(Xi; t) −λ2ρgdh(Xi) = 0 2σP 1.1 f ησP 1.1 f h(Xi) = Q(Xi; t) (8) λd

We can ﬁnd that with Q(Xi; t) increasing, the best h(Xi) increases. However, there is a constraint to h(Xi).

n n ∑ ∑ h(Xi)2d 2k(Xi) ≥M CA(Xi) = (9) i=1 i=1

1. If our optimal {Xi} meets the constraint, Equation.9, then it is the ﬁnal result.

2. Else, we can slightly modify Xi to meet the constraint.

Thus, Final Value of iMoDS model and each dam’s height are both determined by {Xi}.

Figure.9 is our ﬁnal result of placement and number.

6 Strategies

6.1 A Balance Between Safety and Costs

Our new multiple dam system is modeled based on three key factors, Risk Cost, Power Supply, and Series Safety. Risk Cost fully considers the balance between safety and costs by acceptable risk ratio Pf. Series Safety further investigates the safety of a dam group. Thus, our system is well-balanced. What’s more, we also take beneﬁts into consideration.

6.2 Protection for Lake Kariba

Now we take the ability of protecting Lake Kariba into consideration. In the former section, we degenerate this factor to the total volume of the reservoirs. However, we ﬁnd it is reasonable to evaluate it with the relative distance between a reservoir and the lake. We ﬁnally determined to use a gentle Gaussian curve to give a weight of each dam.

n ∑ CA(Xi)N (XLake, σ2) Protection = (10) i=1

where XLake is the location of Lake Kariba, σ is a ﬁtting factor.

To as greatly as possible increase the total Protection to the River, we can build dams near the lake with more capacity,i.e., stronger ability of management of the water.

When it is the period of the dry season, the lower dams near Lake Kariba should start to reserve water and higher dams start to discharge water untill this season passes. On the contrary, when it is the wet season, the behavior of dams near the lake are opposite to the former condition.

We also need to consider the ecosystem of the lake, so dams near the lake need to be designed carefully to minimize the damage to the environment.

6.3 Guidance for Emergency Water Flow Situations

Emergency water ﬂow situation(i.e. ﬂooding and prolonged low water conditions) can generate catastrophe. Flood water may wash away any cities downstream and cause considerable loss of life. Extreme low water conditions could destory many ﬁelds of a country. To ensure the safety of our new dam system, we will provide the ZRA managers with speciﬁc guidance.

The aim of this guidance is prevent an uncontrolled release of water from reservoirs.

For ﬂood control, our objective is to maintain as much control over ﬂows entering the system above a critical ﬂood-prone reach as possible. [8]

Method Filling the upper reserviors ﬁrst and emptying the lower reservoirs ﬁrst.

An illustration of this method has been studied [9]. Flood storage at the reservoir close to upstream provides greater ﬂood controlability than the lower reservoirs.

However, an exception is that if the lower reservoir’s outﬂow capacity is restricted, then it is better to ﬁll the lower reservoir ﬁrst to increase head on the outlet. In this way we can increase the release capacity from the entire sistem to the downstream channel capacity. This exception is prepared for some extremely serious ﬂoods.

For prolonged low water conditions, our objective is to maintain the river runoff.

Method Emptying the reservoirs from lower ones to higher ones

In this kind of periods, the river’s natural runoff is considerably smaller than an- nual water runoff. We must take advantage of the dam system’s capability of dynamic scheduling. In other owrds, we maintain the river’s minimum runoff by compensative regulation. Empty the reservoirs downstream ﬁrst can avoid people’s water shortage while enabling reservoirs upstream to store water.

6.4 Guidance for Extreme Water Flows

In our previous analysis, we use Q(Xi; t) to denote the annual water ﬂow. However in real life, Q(Xi; t) should be a function of time t. Along the Zambezi River there is a dry season and a wet season.

1. Dry Season

It is clear that the dam system need to discharge in dry season. First, we suppose that dry season lasts for time T. At the beginning of the dry season all reservoirs have reached their full capacities. Second, we introduce three parameters,p, k, and m. p denotes the speed of discharging. k denotes the rate of lost water because of evaporation and washing away. m is the amount of remaining water. The problem is then simpliﬁed as an expression of discharging all reserved water during the dry season with some speed.

dm dt = −p −km Solve this function, we get:

m = ce−kt −p k Let m(0) = M, m(T) = 0 Then p = Mke−kT 1 −e−kT

Now we qualitatively analyze this discharging speed. Because the water in the upper reservoirs is shared by all the terrain along the river. On the contrary, the water of the reservoirs downstream is only used by relatively small terrain. It is reasonable that in the dry season, the reservoirs upstream have a larger speed than those downstream. And the average speed of the whole system is p.

2. Wet Season

It has a high rainfall in wet season, so we need to charge reservoirs to avoid great increment of the level of riverway and prepare for the next dry season. We can assume that rainfall is uniformly distributed along the whole river. The upper reservoirs must start to store water ﬁrst. Because if a reservoir downstream ﬁrst to start storing water, Q(Xi; t) will be too large and leads to great risk and waste of water.

7 Model Analysis

7.1 Sensitivity Analysis

Our iMoDS model contains several parameters. We determine some of the parame- ters through least square ﬁtting, some of them by knowledge in the literature, and other methods. In this section, we would like to produce a sensitibity analysis to show whether our model is sensitive to different values of parameters.

We will study the impact of two importnant parameters in our model.

7.1.1 Impact of Planned Working Years N for a Dam

N is set to be 50 and not changed ever since. In the literature, a dam over 50 years old is deﬁned to be dangerous. The Kariba Dam is one of them. We vary this value from 50 to 100 by 10. Figure.10 proves that the trends of Risk Loss remains to be the same. Therefore, we come to the conclusion that our model is not sensitive to N.

7.1.2 Impact of Extreme Condition ratio α

Figure.4 shows the sensitivity analysis of α. To avoid repetition, we don’t illustrate it here again.

7.2 Strengths and Weaknesses

7.2.1 Strengths

1. Use accurate data of the Zambezi River. From the very beginning of our analysis, we emphasize on mining useful data. Only with these dependable data, we can conclude that the model we built is appropriate.

2. Design a novel and innovative evaluation rules of dam construction. We used methods across disciplines to give an integrated evaluation function of dams. AHP and GA are leveraged in our simulation which can provide reliable results of the model.

3. Use fancy visualization to display our model.

7.2.2 Weaknesses

1. Heuristic algorithm has randomness. Because of the high dimensional constraint, we used GA as our simulation algorithm. We cannot always get the optimal results for the sites selection

2. Some real water conditions are omitted. We simpliﬁed the river as an open chan- nel. However, the real condition is much more complex. It will also inﬂuence the construction cost and safety evaluation.

3. Lacking details of the trade-off function. We paid an emphasis on the balance be- tween cost and safety. Though we have added power supply to our model, it still lacks other beneﬁts of dam construction.

8 Conclusion

Our papaer provides a detailed analysis of removing the Kariba Dam and replacing it with a series of ten to twenty smaller dams along the river. Before introducing the model, we analyze water ﬂow and a single dam. Then our model iMoDS is proposed. It takes safety, cost, and beneﬁts into consideration and makes a balance of them. Three submodels, Risk Cost Model, Power Supply Ability Model, and Series Safety Model, form the integrated model.

We use real data to give a recommendation as to the number, placement, and height of the new dams. For this is a high dimensional problem, we implement GA to ﬁnd a global optimum result.

Strategies are fully discussed. Balance between safety and costs have been inlcuded in the integrated model. Protection for Lake Kariba uses Gaussian curve to give a weight of each dam. And two guidances include speciﬁc instructions of the dam group when facing these conditions.

Brief Assessment Report

The Kariba Dam, which was opened in 1959 and held back the world’s largest reser- voir, has been working for over 50 years and faces the possibility of callapse. Also serv- ing as a major supply of Zambia and nearby contries’ electricity, it is in dire need of maintenance. To deal with this situation, there are three major options available to the Zambezi River Authority (ZRA). For each option, we will access its potential cost ne- murically and provide other aspects of information.

In the literature, the rate of failure for dams has been studied. With Bayesian analysis approach, researchers [10] evaluated the dam failure rate uncertainty. They found uni- versal failure rate to be steady and got the value of 3 × 10−4. However, we investigate the whole life cycle of a dam. Its failure rate [11] should be a function of time t, denoted as FR(T) { 3 × 10−4 if 0 ≤T < 50 years FR(T) = (11) 1 −e−( t+143.67 )3 if T ≥50 years 100

Figure.11 shows a dam’s failure rate with the change of years.

Option 1: Repairing the existing Kariba Dam

Once mechanized systems supplant natural ones, they must be managed in perpetu- ity, or else they break down [12]. In the past ﬁfties years, the torrents has been consis- tantly eroding the dam’s structure. The ﬁrst option is to repair this existing giant.

Potential Cost One report [13] said that expected cost will be $294 million this time. However, repair can handle current situation but never eliminate the potential danger. Thus, we explore an expectation of future failure rate by modifying Equation.11

FRrepair(t) = 1 −e−( t+143.67 )3, (12) 100

where t = how many years have passed since last repair.

Thus, given a speciﬁc year Y and annual cost of repair C, the potential costs will be:

∫Y −2017 294 + C × FRrepair(t)dt (13) 0 Beneﬁts Repair signiﬁcantly saves the construction period.It doesn’t affect hydro power supply which is generated from the reservior.

Shortcomings

Potential danger to collapse. High repair rate with high cost each time.

Option 2: Rebuilding the existing Kariba Dam

Potential Cost Rebuilding such a giant dam is extremely expensive. According to Kariba Dam - Case Study [1], the project was built in two stages. The total cost of two stages amounted to $1.8 billion. To know how much it will cost now, we estimate it with The Consumer Price Index(CPI) [14]. CPI for the 1950’s was 27.2 while current CPI is about 241.4. Thus, the total cost of rebuilding is about 241.4/27.2 × $1.8 = $15.975 billion.

Also we calculate future cost: given a speciﬁc year Y and annual cost of repair C, the potential costs will be: ∫Y −2017 7440 + C × FR(t)dt (14) 0

Beneﬁts No severe potential danger any more. No need to repair very often.

Shortcomings

A long period of time under construction. Lack of a Dam, affecting hydro power supply, and protection for Lake Kariba.

Option 3: Removing the Kariba Dam and replacing it with a series of ten to twenty smaller dams along the Zambezi River

Potential Costs The construction cost can be described as:

Construction cost = k ∗capacity + basic cost

Considering that the total capacity of these small dams is equal to the capacity of Kariba Dam, the construction cost of Option 3 is close to n times of basic cost plus the cost of Option 2, where n is the number of these small dams. Here we suppose that the basic cost is 10% of the total construction cost and the cost of removing Kariba Dam is about 15% of the total construction cost, thus, the total construction cost is about $15.975∗ (1 + 10% ∗n + 15%) = $34.363 to $50.321 billion.

Let n = 13, the cost of the solution we give in our model is about $39.139 billion.

Beneﬁts Strengthen the ability to handle emergency water ﬂow, protect Lake Kariba, and adjust water ﬂow between seasons.

Shortcomings

It costs most in these 3 options, and it brings in new problems of coor- dinating and control in a dam system.

Appendices

Appendix A

Implemented Genetic Algorithm

n=13;% need adjust B_sub1=[zeros(n,1);0.00001]; %B_sub1 means the VLB of the Xi B_sub2=[ones(n,1)*2100;0.1]; %B_sub2 means the VUB of the Xi B=[B_sub1,B_sub2]; % constraint of Xi initPop=initializega(n,B,’fitness’); [x endPop,bPop,trace]=ga(B,’fitness’,[],initPop,[1e-6 1 1], ’maxGenTerm’,10000,’normGeomSelect’,... [0.08],[’arithXover’],[2],’nonUnifMutation’,[2 10000 3]); %3000 generations xx=sort(x(1:14)); % sites selection sorts as ascending order x=[xx,x(15)]; % the last one is the evaluation value

Appendix B

Fitness Function

function[sol,eval]=fitness(sol,~) n=13; x=sol(1,1:n+1); xx=sort(x(1:n)); x=[xx,x(n+1)]; p1=0; p2=0; cc=0; N=50; Ca=300; BB=6000; aa1=400; rr=0.8; pp=1005; yy=0.5; l=200; Cmin=2e6; Pm=1e8; % above are the constant parameter setting wei=[0.12,0.54,0.34]; % wei means the weight of three key function for i=1:n k=my(x(i)); Q=my2(x(i)); R=(1-(1-x(n+1))^N)*Q*aa1*(1+rr); C=((Ca/n)*k+BB)*(1/(x(n+1))^1.1); Power=Q*pp*yy*k*l*9.8/1000; p1=p1+Power; p2=p2+C+R; end p1=p1/Pm p2=Cmin/p2 for j=1:n-1 cc=cc+((x(n)-x(1))/(n-1)-(x(j+1)-x(j)))^2; end Sa=((x(n)-x(1))/exp(cc/((x(n)-x(1))/(n-1))^2))/2100 eval=p1*wei(1)+Sa*wei(3)+p2*wei(2) end
