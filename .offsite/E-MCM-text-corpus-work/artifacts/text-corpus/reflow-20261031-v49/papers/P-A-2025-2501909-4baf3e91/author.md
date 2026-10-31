MCM/ICM

Summary Sheet

Summary

Even the hardest stone steps can wear down over time under the repeated footsteps of peo- ple. Stairs record history in the unique way. To assist archaeologists in extracting more infor- mation from a set of worn stairs, we analyze measurable data and establish relevant models.

For task1:To analyze stair basic information, we established the Stair Wear Model, which is consisting of the Wear Volume Model (WVM) and the Wear Distribution Model (WDM). We rasterize the top view of the steps and combine it with wear data to create a wear measurement matrix. Based on this matrix and Archard Wear Law, we develop the WVM. We introducing and analyze parameters such as the wear coefﬁcient, average human weight, material hardness, and stair area to calculate the stair’s age and usage frequency. Additionally, we established the WDM based on the Central Limit Theorem. It calculate the marginal distribution of the wear measurement matrix and ﬁt the wear distribution in the X and Y directions with a Gaussian

Mixture Algorithm. In the Y-direction, the number and location of normal distribution indicate walking direction, while the X-direction distribution reﬂects the parallelism of movement.

We provided archaeologists with measurements and queries (Table 3) and detailed usage instructions (Figure 7). All the methods we propose follow the non-destruction principle. As an example, a set of ancient sandstone steps in Edinburgh is analyzed. The results demonstrate the steps were built about a century ago, typically used by three people walking side by side. Both directions were used, with an upward-to-downward ratio of 3:2 and a daily usage frequency of 261. More detailed results are presented in Table 5, Table 6 and Figure 8.

For Task 2: We address further problems with the Stair Wear Model and information avail- able. To assess wear distribution consistency, we deﬁne a consistency parameter between wear matrices. The stairwell age is calculated from step age, with a reliability parameter to evaluate accuracy. To determine if the staircase was repaired, besides the step age method we introduce an innovative non-destructive approach based on the Brinell Scale and KL divergence for a more comprehensive consistency analysis.

Based on the consistency of material hardness, we developed a method to trace material origins. Simulations with the Stair Wear Model help evaluate material wear consistency. Monte Carlo Method reveals the relationship between the standard deviation of X-direction wear and daily stair usage. Applying these methods to the studied steps yielded an age prediction reliability above 95%. Both methods conﬁrms no repairs in this stair, and materials matches archival records. The dispersed X-direction wear indicates heavy use over short periods.

Material hardness demonstrates a high sensitivity in our model. The model shows low sensitivity to weathering rate constant within 4 century but higher sensitivity over a 20-century scale, indicating its strong performance within a certain time frame. Robustness tests across regions further support this. We hope our work can help the archaeologists. The hard stones have their method to record the history, and we have the model to read them.

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

Introduction

3 1 1.1 Problem Background 3 1.2 Our Work 4

2 Assumptions and Notations 4 2.1

Assumptions

4 2.2

Notations

5

Stair Wear Model 6 3 Wear Volume Model 6 3.1 3.1.1 Rasterize The Surface of The Step 6 3.1.2 7 Wear Volumn Model Calculation of Age and Frequency of Stone Steps 3.1.3 9 3.2 Wear Distribution Model 9 Wear Distribution in The Y-direction - Judging The Direction 3.2.1 9 ATHmoc Wear Distribution in The X-direction - Calculating The Number of Par- 3.2.2 11 allels 3.2.3 Wear Distribution Model . 12 3.3 Stair Wear Model . 12 3.3.1 12 Parameters to Be Measured 3.3.2 Overview of Stair Wear Model 13 Solution of the StairWear Model . 3.4 14

Further Problems 1 16 4

4.1 Consistency of Wear Results

16 The Age of The Stairwell and Reliability . 4.2 16

4.3 Repairs or Renovations

17 19

4.4 The Source of The Material .

People Use The Stair on A Typical Day 20 4.5 ●

Sensitivity and Robustness Analysis

22 5 Impact of Material Hardness on Wear Volume 22 5.1 Impact of Weathering Rate Constant on Wear Volume 5.2 23 Impact of Reigon on Wear Volume 23 5.3

24

Strength and Weakness

6

Strength

6.1 24 24 6.2

Weakness

24

Conclusion

7

1 Introduction

1.1 Problem Background

微信公众号：数学模型 As a symbol of permanence, stone is often used for building components. Despite its durability, the stone is not impervious. As people walk up and down over time, steps are molded into different shapes that tell stories of the past, waiting to be explored.

The wear on stairs reﬂects the behavioral patterns of people in the past. Long-term behavior of people is likely to have subjected the steps to uneven wear, leaving the treads with curved tops. For example, in ancient temple staircases, the centers of the steps are more worn than the edges. Archaeologists are interested in the age, the trafﬁc patterns, and the frequency of use of stairs. But the presence of people and the temporal variability in the construction of the 微信号：MATHmodels staircase, and the renovation of the staircase have obscured some of this information.

To assist the archaeologists, the team was asked to build relevant mathematical models for the following tasks:

Task1: Given a set of stairs, develop a mathematical model that considers the wear patterns of a particular staircase. Provide some basic predictions:

• Discuss the frequency of use of this staircase.

• Explore the direction of travel favored by the people using the stairs.

• Study how many people use the stairs at the same time.

When archaeologists are skeptical about a staircase, ﬁeld measurements can be made. A non-destructive surveying program, which requires minimum cost, fewer people, and the fewest tools can be taken.

Task2: Further problem solving. By using the available estimates, determine what guidance can be provided for the following questions:

• The consistency of wear with available information.

• The age of the stairwell and the reliability of the estimate.

• The repairs or renovations have been made to the stairwell.

• Determine the provenance of materials and compare them with the speculations of ar- chaeologists.

• Analyses the use of the stairwell on a typical day. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

1.2 Our Work

According to the requirements, our work is as follow.

2 Assumptions and Notations

2.1 Assumptions

To simplify the problem and make it convenient for us to simulate real-life conditions,we make the following basic assumptions, each of which is properly justiﬁed.

• Assumption 1:All people walk on the stairs with single-step strategy. the same set of steps in the same time subject to the same step.

Justiﬁcation: Single-step(SS) and double-step(DS) are two stepping strategies people m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m prefer when walking on stairway steps[1]. We choose the former strategy to ensure that m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m all steps in a group are trampled equally. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

• Assumption 2: Natural wear and other forms of erosion affect all surfaces of the same m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

set of steps equally.

Justiﬁcation: The same set of steps is typically exposed to identical environmental con- ditions and is often constructed from the same materials. Since environmental factors are spatially uniform, it can be assumed that they exert the same effects on all surfaces of the steps.

关注数学模型 • Assumption 3: Maintenance and renovation methods involve either completely replac- ing the stairs with another material or ﬁlling them with the same material to restore their original shape.

Justiﬁcation: These stairs primarily bear the wear load from people climbing upwards.

It is essential to ensure that the repaired stairs possess sufﬁcient wear resistance and load- bearing capacity to meet usage requirements. Therefore, replacing the entire material or 微信公众号：数学模型 meticulously ﬁlling with the same material ensures the structural integrity and durability of the stairs post-maintenance.

• Assumption 4: The force exerted by the shoe surface and the stair surface when climbing is uniformly directed downward.

Justiﬁcation: The shoe surface and the stair surface can be approximated as rigid bodies.

In real environments, there are certainly frictional forces (for anti-slip or propulsion) and instantaneous mechanical changes caused by foot movements. However, for simpliﬁed 微信号：MATHmodels analysis focusing solely on the overall load-bearing and wear amounts, smaller horizontal component forces or uneven distributions can be temporarily neglected. This results in an idealized "uniform vertical pressure model."

2.2 Notations

Notations

Deﬁnition

d(x,y) The wear depth of the grid (x, y) on the step

Dmeasure Wear measurement(x,y) matrix

T The construction duration of the stair

Nd Usage frequency of the step

G The average gravitational force experienced by walking people

km The amount of wear caused by unit force on the stone step

D(x,y) The foot trafﬁc rate contributing to wear at point (x, y) on the stone step

km The wear coefﬁcient of the material

d The sliding distance of contact on the tread surface of the step

H0 The initial material hardness

The marginal function of D(x,y) alone the x DX

The marginal function of D(x,y) alone the y DY

RS(d1,d2) The correlation between two stone steps d1,d2

PA The correlation between the two matrices

CI The reliability of the age of the step

3 Stair Wear Model

Besides the wear information we are focusing on, for a step, the angle and the area of the steps are easy to get. The smaller the angle, the gentler the steps, making walking less stren- uous. If the terrain in this area is relatively high, it might indicate that people have difﬁculty moving around.

According to assumptions 1 and 2, people all use the single-step strategy (SS) to walk on the stairs. The rest of the factors have the same effect on the given set of steps. Therefore, in the absence of repairs, the condition of a single stone step gives a good picture of the age of a given set of steps, the trafﬁc patterns of the people, and the daily patterns of life. To acquire this interest information to archaeologists, we model the Wear Volume Model and the Wear Distribution Model. Besides, we present the data that need to be measured. Finally, a set of ancient sandstone steps in Edinburgh is used as an example for solving the problems.

3.1 Wear Volume Model

3.1.1 Rasterize The Surface of The Step

In order to represent the actual physical steps by using a mathematical model for easy computer processing, we rasterize the steps. As shown in Figure 3, we take the top view of a step to obtain a rectangle with length X m and width Y m, which is discretized and divided into m×n rasters.

The COP[2] is deﬁned as the center of each grid.

⌊p ⌋ ⌊q ⌋ x = , y = (3.1) Gs Gs

p denotes the distance from this COP to the leftmost side of the step, q denotes the distance from this COR to the bottom edge of the step, and Gs is the size of the grid. d(x,y) is deﬁned as the amount of wear at grid COP(x,y). The archaeologist measures the wear volume of the

关注数学模型 stone steps and then constructs the measure wear matrix Dmeasure (x, y).

3.1.2 Wear Volumn Model

Wear results from behavior over time for a material as hard as stone. The total number of steps taken on the same spot determines the amount of wear on that spot. The length of time determines the time scale of cumulative wear. The hardness and abrasion resistance of the material directly affects the wear rate. In addition, different distributions of steps and applied gravity in different areas can lead to uneven wear. In order to accurately obtain information about the steps, we introduced a comprehensive Wear Volume Model, combining the wear distribution model with the introduction of time, material, and number of footsteps:

(3.2) d(x, y) = T · Nd · D(x, y) · G · km ●

d(x, y) represents the wear measured by the archaeologist, T denotes the age of the stair, Nd indicates the average number of people who walked the stairs each day, which is also known as usage frequency. D(x, y) is the wear distribution function, we discuss it in Section 3.2. G is the average gravitational force experienced by walking people, and km is defined as the wear volume coefficient (the amount of wear and tear per unit of N on the stone steps). Further, we H Y analyze the parameters kmand G.

Archard wear theory is one of the classical wear models, proposed by J.F. Archard. The theory is used to describe the wear behavior of solid surfaces. Each step exerts a certain positive pressure on the step in the process, which can be directly applied to analyze the wear suffered by the step surface. At the same time, although the relative motion distance between the person and the step during walking is limited, the slight sliding of each step will cause localized wear on the step surface. Therefore, Archard's wear theory is applicable to analyze the wear of steps caused by people walking. The theory establishes the fundamental formula for the unit wear coefficient of a solid km, which is defined as: d km = K · (3.3) H where K denotes the stone wear coefficient, d represents the relative sliding distance of the tread surface, and H indicates the material hardness of the stone.

Material hardness H is not static but varies with time, resulting from physical factors (such as temperature changes and wind erosion) and chemical weathering (such as hy- drolysis and oxidation). Hence, we use an exponential decay model to simulate the loss of hardness caused by weathering of rocks:

H(t) = H0e−pt (3.4)

Ho denotes the initial material hardness while p denotes the weathering rate constant.

Moreover, another form of relationship between hardness and age can be provided:

HT = ∫H(t) (3.5)

Based on the site survey, an information review is needed to obtain K, H0 and p.

• Gravity Assessment Model (G) The same step may be used by people of different ages and genders with different weight characteristics. We categorize the population into six groups: male minors (mm), female minors (fm), adult males (am), adult females (af), older men (om), older women (ow).

To make the results more precise, we use their weight expectation as W in the model, which is calculated as follows:

W =∑ui·qi (3.6) i

where u describes the average weight of each population, q indicates the proportion of each population to the total population.

If they do not have this information, based on the global weight data provided by the World Health Organization (WHO)[6][7], we provide the reference data as shown in Table 2.

Proportion (%) Average Weight (kg) Population Group 40 10 Male Minors (mm)

38 10 Female Minors (fm) 75 30 Adult Males (am)

65 30 Adult Females (af)

70 10 Older Men (om) 60 10 Older Women (ow)

The overall average weight of the population is W = 62.8kg. This average is typically calculated as a weighted sum of the proportions qi and the average weights u of each sub- group. To obtain a more precise estimate, archaeologists or researchers can adjust the subgroup proportions qi or their average weights u to better reflect more localized or up-to-date demo- graphic data.This can make the calculation results more accurate and increase the flexibility of the model.

This adjustment allows for a more accurate estimation of the gravitational force G. The gravitational force is calculated using the following formula:

G = W·g (3.7)

where g = 9.81 m/s² [9]is the acceleration due to gravity.

关注数学模型 Integrating Equation 3.2, we obtain the expression for the average wear davg as ∫ 1 T ·Nd ·D(x,y)·G·kmdxdy davg = (3.8) 微信公众号：数学模型 Acef f Acef f

in this equation, Acef f denotes the area of the steps overlook.

3.1.3 Calculation of Age and Frequency of Stone Steps

According to the analysis above, When D,G, and km are determined, the age of stone step T and frequency of use Nd can be solved for each other. The speciﬁc formulas are shown below:

T = Ace f f ·davg 微信号：MATHmodels (3.9) Nd ·G·km

Nd = Acef f ·davg (3.10) T ·G·km At this point, the age of the stone step T and frequency of use Nd can be sought.

3.2 Wear Distribution Model

Each step on the steps can be regarded as obeying independently and identically distributed. Research shows a linear relationship between the number of steps and the amount of wear, and only when the cumulative number of steps reaches a large size, signiﬁcant wear on the surface of the step stone can be produced. According to the Central Limit Theorem, when the number of independent random samples is large enough, even if the original distribution is not normal, the distribution of the sample mean and sum will converge to the normal distribution. Therefore, when the sample size is large, the cumulative distribution of steps tends to be normal, and the cumulative wear will also be normal.

Since there is no signiﬁcant correlation between the lateral and longitudinal positions of the footsteps on the stone stairs, the cumulative wear of pedestrians at each position in both the x- and y-directions can be described as a superposition of normal or multi-normal distributions when the number of steps is sufﬁciently high. And the distributions reﬂect the trafﬁc patterns of people on that set of stairs.

3.2.1 Wear Distribution in The Y-direction - Judging The Direction

Studies of the gait cycle show that during stair ascent, the ﬁrst peak appears in the heel, while during stair descent, the ﬁrst peak is in the forefoot. This is shown in Figure 4. In addition, observing people’s daily stair movement behavior, it is found that pedestrians’ point of impact is closer to the lower edge of the steps when going up the stairs than when going down the stairs[3].

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

(a) stair ascent (b) stair descent

With the conclusion above, we can judge whether people using the stairs favored a certain direction of travel based on the wear distribution of Y-direction.

(a) Double direction - Wear Distribution (b) Double direction

(c) Upward Direction - Wear Distribution (d) Upward Direction

As shown in Figure 5(a), there are two peaks, which means that the marginal distribution in the y-direction is a superposition of two normal distributions. This indicates that stairs were usually used in both directions. The number of people traveling up and down the stairs can be compared based on the size of the peaks. Similarly, one peak in Figure 5(c) demonstrates that people using the stairs favored a certain direction of travel. If the y-value at the peak is small, people favored upward travel. If it is larger, downward travel was favored.

We further quantify the results so that archaeologists can determine the direction and the

关注数学模型 proportion of up-and-down people more intuitively. Using knowledge of probability statistics, we construct the distribution of wear in the Y-direction:

Dy ∼wup ·Ni(µup,σup)+wdown ·Ni(µdown,σdown) (3.11)

wup denotes the ratio of people going up to the total number of people, while wdown denotes the ratio of people going down to the total number of people. µup is the distance between the center of the stepping surface of the person going up and the outermost part of the stone step, and µdown is the distance between the center of the stepping surface of the person going down and the outermost part of the stone step. σup describes the degree of longitudinal dispersion of people going upstairs, and σdown describes the degree of vertical dispersion downstairs.

微信公众号：数学模型

3.2.2 Wear Distribution in The X-direction - Calculating The Number of Parallels

When people walk on the stairs in a single-step strategy, the peaks of the normal distribution in the X-direction of the steps describe the main concentration area of pedestrians. And the number of peaks reﬂects the lateral distribution characteristics of pedestrians on the road. We describe the wear distribution in this direction as:

Dx ∼wi∑ Ni(σi,µi) (3.12) 微信号：MATHmodels i

n represents the number of parallel lanes on the same step of the stone staircase, wi is the ratio of the number of people in the lane i to the total number of people, µi denotes the distance of the center of the lane i from the leftmost end of the stone staircase, and σi indicates the degree of lateral dispersion of lane i.

(a) Travel single - Wear distribution (b) Travel single

(c) Side by side - Wear distribution (d) Side by side The distribution describes how many people used the stairs simultaneously. The number of peaks is the number of people in parallel. In Figure 6, we give some possible results for archaeologists as a reference:

1. When i = 1, there is only one peak in the x-direction. It can be concluded that people using this stair preferred traveling single ﬁles.

2. When there are two peaks in the X-direction(i = 2), pairs of people climb the stairs side-by- side.

3.2.3 Wear Distribution Model

Since the lateral position of a footstep on a stone step is not signiﬁcantly correlated with its longitudinal position, we consider the covariance matrix of the wear distribution to be a diagonal array. For a stone step, we model the wear distribution as follows:

D(x,y) = DX ·DY (3.13)

We compute the actual wear matrix Dmeasure(x,y) obtained from the archaeologist’s mea- surements. Then, we can get its marginal distribution function:

(x) = ∑ Dmeasure Dmeasure(x,y) (3.14) X y

(y) = ∑ Dmeasure Dmeasure(x,y) (3.15) Y x With these two edge functions, we can ﬁt Dx and Dy, which will help archaeologists obtain relevant information, such as people’s trafﬁc patterns.

3.3 Stair Wear Model

3.3.1 Parameters to Be Measured

Archaeologists are needed to carry out non-destructive measurements and access infor- mation to obtain accurate information and implement the model’s solution. We provide the necessary parameters and suggest some measurement methods. It Is shown in Table 3:

关注数学模型 We consider all the methods that require minimum cost, fewer people, and the fewest tools.

微信公众号：数学模型

3.3.2 Overview of Stair Wear Model

Based on the analysis above, the Stair Wear Model is concluded as below:

Wear Volume Model(WVM):

∫ 1 T ·Nd ·D(x,y)·G·kmdxdy davg = Acef f Acef f G = ∑ ui · pi i 微信号：MATHmodels km = K · d (3.16) H H(t) = H0e−pt ∫ HT = t H(t)

Wear Distribution Model(WDM):

D(x,y) = DX ·DY Dx ∼wi∑ Ni(σi,µi) i Dy ∼wup ·Ni(µup,σup)+wdown ·Ni(µdown,σdown) (3.17) (x) = ∑ Dmeasure Dmeasure(x,y) X y (y) = ∑ Dmeasure Dmeasure(x,y) Y x All parameters have been explained above. In order to show our model more clearly and to make it easier for archaeologists to understand it, we give the ﬂow chart for use in Figure 7:

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

3.4 Solution of the Stair Wear Model

In this section, we selected a set of ancient Edinburgh sandstone steps with a rectangu- lar top-view surface. The rectangle is 2 meters long and 0.4 meter wide. Based on the 3D m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m reconstruction of the image, we obtained the measurement matrix. Moreover, based on the m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m information query, we obtained the rest of the required parameters as follows: m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

Parameter Value Unit

G 700 N

1.8×10−7 K (dimensionless)

d 0.8 mm

N/mm2 H 95

To solve the Wear Distribution Model, we design a Gauss Mixtual Algorithm. It can be used to respectively solve for normally distributed cumulants in the X and Y directions by wear measurement matrix Dmeasure. The exact ﬂow of the algorithm is as follows

Gauss Mixtual Algorithm

Wear measurement matrix Dmeasure Input:

P(DX | θ epoch ) and P(DY | θ epoch) Output: k k = 0 , ε = 1e−3

while loss > ε

for t in range(epoch) θt+1 = θt −∂P(DX | θt)/∂θt, where θ = [mi,µi,σi] i=1 mt+1 ·N(µt+1 ,σt+1 P(DX | θt+1) = ∑k ) i i i loss = ∥P(DX | θ epoch )−DX∥ k k = 2

for t in range(epoch) θt+1 = θt −∂P(DY | θt)/∂θt up ·N(µupt+1,σupt+1)+mt+1 P(DY | θt+1) = mt+1 down ·N(µdownt+1,σdownt+1) end

Bringing Dmeasure of the Edinburgh sandstone step into the Gauss Mixtual Algorithm, we obtain the following normal distribution parameters. The parameters for the X and Y directions are placed in Table 5 and Table 6 respectively.

关注数学模型 微信公众号：数学模型 direction direction

From Table 5 and Table 6, we can draw the conclusions that

微信号：MATHmodels 1. The wear distribution in the X-direction is accumulated from three normal distributions.

The mean values of the three normal distributions are 0.30m, 1.10m and 1.76m. They are respectively on the left, centre and right side of the step. This reveals that three people usually walked side by side on this step. This may also show that the stair had a high ﬂow of people.

2. Of the three normal distributions in the x-direction, the second one has the highest probabil- ity and the smallest standard deviation. This indicates that people most often walked down the middle of the stairs.

3. Two normal distributions form a wear distribution in the Y-direction. The stair was used in two direction. The probability ratio of the number of people in the upward and downward direction was 3 : 2. It means that the number of people in the upward row is greater than the number of people in the downward row.

4. The mean of upward direction is 0.08m, while that of downward direction is 0.15m. They both close to the edge side of the step. Moreover, the mean of upward direction is closer to the edge of the step than the downward direction. This is consistent with our analysis.

To describe the results of this set of steps more intuitively, we visualize the wear distribution of the steps and present them in Figure 8.

This graph gives the same conclusions. It visually presents three peaks in the X-direction, indicating that people usually walked side-by-side on it. There are two peaks in the Y-direction. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m The peak corresponding to the downward direction is smaller than that of the upward direction. This suggests that the staircase was used in a double direction.

After obtaining the wear distribution, combined with the parameters in Table 4, the gradient age and frequency of use can be solved for each other. For this set of ancient Edinburgh sand- stone steps, it is determined that this set of steps was constructed in a century ago. according to Equation 3.16, we can have that

Nd = Acef f ·davg = 261 (3.18) T ·G·km

This means that 261 people walked on it every day in the past. On the contrary, when we consider that 260 people walked on it per day, the steps were constructed 36492 days ago.

4 Further Problems

In this section, we propose solutions and computational models for the further problems.

4.1 Consistency of Wear Results

According to the available information, we can get a more accurate wear distribution matrix Davailable. To judge whether the wear is consistent with the information available is to judge the consistency of Davailable and Dmeasure. We deﬁne the following consistency formula:

(dava(x,y) ) PA = Davailable(x,y)∑ x ∑ log (4.1) d(x,y) y

dava(x,y) is the amount wear depth of the stone step on the grid where each COP is located. and d(x,y) is that of the actual measured. PA is a number greater or less than 0. The greater the absolute value PA, the weaker the correlation between the two matrices.

4.2 The Age of The Stairwell and Reliability

In Section 3, we give the method of estimating the age of each step. For a given stair, we measure the ages of all steps and ﬁnd them different. When the difference is slight, it is mainly because the model has errors. However, when the difference is signiﬁcant, it is due to refurbishment or repairs that cause the individual steps to age differently. In a stairwell, if the age of a step is 5% less than the age of the largest step Tlar, it is removed. The average age of the remaining steps as the age of the stairwell Tset. It can be expressed as

Ti Tset = Ti, > 0.95 (4.2) Tlar

There are N steps in tatal. Ti is the age of step i, i = 1,2,··· ,N.

关注数学模型 Age reliability is necessary to be assessed. We estimate the ages of n ancient stone stairs in total. If the error between the result and the real age is within 5%, RA is accepted and included, 微信公众号：数学模型 otherwise RC is included. The age reliability CI is deﬁned as:

[ ]−1 RC +1 CIinf = 1+ (4.3) RA·F1−α/2(2RA,2(RC +1))

[ ]−1 RC CIsup = 1+ (4.4) (RA+1)·F1−α/2(2(RA+1),2(RC))

where α = 0.05.

微信号：MATHmodels We studied 6 Edinburgh sandstone steps living more than one century and calculated that 5 of which have an error within 5%, which means we can say the age reliability is between 0.359 and 0.996

4.3 Repairs or Renovations

Two methods are proposed to ﬁnd out which steps have been repaired or refurbished.

Method 1: Step Age Method

Brief Introduction: Measure the age of each step by the Stair Wear Model and compare them.

According to Assumption 4, each step is trampled at the same frequency. Therefore, in the absence of repairs or renovations, the age of all the steps should vary slightly. The correlation degree RSA between step i and the whole is deﬁned as:

Ti RSA = min (4.5) Tset i

Ti is the age of step i, and Tset is the age of the stair. This coefﬁcient is typically a value between 0 and 1, where higher values indicate greater correlation. When RSAk is smaller than 0.95, it indicates that the kth step has been repaired or renovated. The time of repairs or renovations Tre can also be determined by Tre = Tn −Tk (4.6)

Tn is the year in which the archaeologists began their measurements. Since there may be errors in the calculation of age, we also provide an alternative method.

Method 2: Improved Non-destructive Measurement based on Brinell Scale and KL scatter

Brief Introduction: Combined with the Brinell scale theory and KL scatter, calculate hard- ness of each step material by using the existing wear matrix. Compare its consistency to deter- mine which step has been repaired and give the time calculation formula.

Brinell scale is a scale that measures the hardness of a material and is one of the properties of the material. Brinell scale measurement is a way of measuring the hardness of materials. A typical test uses a hardened steel ball with a diameter of Dp mm as an indenter. A force of F is applied to the indenter and held for a certain amount of time. Then the diameter of the indentation caused by the indenter on the surface of the material is measured. The hardness HB is calculated as follows:

2F (4.7) HB = 0.102 · D2− dp (Dp−√ πDp

where dp = diameter of indentation (mm).

Due to the absence of repairs or renovations, people exert the same continuous pressure on each step of a stair over time. We take the average gravity G as F, the average wear depth of the step as the indenter diameter Dp, and the square root of the area Aceff of a step as the indentation diameter dp. At this time, the hardness Htest is calculated as follows:

2G (4.8) Htest = 0.102. πā(d−√a − Acefs)

When the Htest of each step has a large difference, the step with the larger Htest has been repaired. We use the variance σí to discribe the dispersion of Htest .

Even if the Brinell scale is similar and the materials are consistent , it is possible that it has been repaired. Referring to the KL scatter, we propose a definition of the correlation between two stone steps:

d1(x,y) RS(d1, d2) = D1(x,y)∑∑1og (4.9) d2(x,y) y

RS(d1, d2) is the correlation between the worn volumes of the two stone steps, D1 represents the wear distribution of the comparative stone steps, d1 (x, y) denotes the average wear depth of the corresponding raster of the comparative stone steps, and d2(x, y) denotes that of the compared stone steps. The similarity threshold is set as ε = 0.05. When |RS(d1, d2)| > ε, it is considered that the comparative stone step has been repaired.

Combining Htest and RA, we can determine which repair or renovation occured in this stair. Moreover, the repair time can be determined as:

Td1 = Td2 . eRS(d1,d2) (4.10) repair

where Td1 refers is the length of time from when the stair was built to when the step was repair repaired, and Td2 denotes the time that the stone steps were built.

For the Edinburgh sandstone steps we studied, we calculated that

(1) RSA = 0.02 < 0.05 (2) All the Htext of steps are close to 89.45N/mm2 while σH = 1.8

关注数学模型 (3) RS = 0.03 < 0.05

Therefore, this set of steps has not been repaired or renovated.

微信公众号：数学模型

4.4 The Source of The Material

As analyzed in Section 4.3, we can determine the type of materials to a certain extent through the Brinell scale. In our model, H0 denotes Brinell scale. Therefore, according to the Wear Volume Model (3.16), the average quantity of H over a time scale, Ht, can be obtained, which can be expressed as:

Ht = Nd ·G·T ·K ·d (4.11) davg ·Aceff Nd indicates the stair use frequency, G denotes the average gravity, T indicates the stair age, 微信号：MATHmodels K is the material wear coefﬁcient, d is the average wear distance, davg is the average measured wear depth, and Acef f is the area of the step.

People have studied numerous kinds of materials deeply. Here we demonstrate sevearl Brinell scale (H0)for four commonly used steps[4][5]:

We can refer to available data to obtain the Brinell scale H0A of the material we considered to be the origin, calculating its average H0At over time according to (3.5). Then its agreement with the model theoretical value Ht can be obtained by:

η = |Ht −H0At| ·100% (4.12) H0At

If η < 0.05, we believe that we successfully determine the origin. For instance, considering the Edinburgh steps we studied. It is said to be constructed by sandstones. According to the literature, We know that the Brinell scale H0 of standard sandstone is 95N/mm2. It can be calculated that Ht = 90.44N/mm2. H0At = 93.18. Therefore, η = |Ht −H0At|/H0At = 0.030. We can conﬁrm its origin.

Refering to the analysis of rock, we give the hardness attenuation formula of wood:

H(t) = H0 ·e−(0.0015·T+0.02RH)·t (4.13)

Unlike stone, the hardness of wood is also inﬂuenced by its age when used for constructing stairs. Its age can potentially be determined from the growth rings visible on the stairs.

To determine whether the wear is consistent with materials from the quarry the archaeol- ogist believes to be the original source. We need to perform the same simulation on the raw m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m materials based on the available information. For instance, we set the same environment for the steps of these four materials in Figure 7. People’s walking pattern is constructed by the normal distribution parameters in Figure 5 and Figure 6. Except H0, other parameters in Table 4 are introduced. Each stair is stepped 100 million times in 100 years. Figure 9 shows the intuitive wear conditions of different stone and wood for the reference of archaeological experts.

(a) Metasequoia (b) Poplar

(c) Standstone (d) Marble

As can be seen in Figure 9, after the same amount of stampede, the incress of H will lead to less wear of the step. Moreover, Figure 9(c) exhibits wear patterns similar to those in Figure 8. It provides substantial evidence to support the determination of the source of the step material.

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

4.5 People Use The Stair on A Typical Day

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Based on the observation and analysis of human stair usage behavior, we possess some m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m conclusions and gussess. When several individuals use the stairs over an extended period, m m m m m m m m m m m m m m m m m m m m m m m m m

they tend to walk along the center of the stairs[8]. In such cases, a normal distribution with a small variance is likely to emerge in the X-direction. On the countary, if a large number of individuals use the stairs within a short time, their footsteps become more irregular. It may result in a normal distribution with larger variances or even a multimodal normal distribution.

To further investigate, we simulated different situations. Divide one day into 1000 time steps For each time step, the probability of one person going upwards is Po while the probability of two people going upwards (1 −Po). Po reﬂects the number of people walking on the stairs that day. Assume that each of the following points is the main focus of a step.

We set Po=1,0.8,0.6,0.4,0.2,0 respectively. The visualized simulation results are presented in Figure 10, and the corresponding σ to Po are listed in Figure 8.

From the Figure 10 and Table 8, it can be observed that as Po increases, σ decreases. This indicates that when a few of people use the stairs over a long period, their footsteps are more concentrated in the X direction. Conversely, when lots of people use the stairs in a short time, σ increases, and the footsteps are more dispersed. This cooperates well with our expectations.

关注数学模型 (a) Po=1 (b) Po=0.8

微信公众号：数学模型 (c) Po=0.6 (d) Po=0.4

微信号：MATHmodels (e) Po=0.2 (f) Po=0

We consider ﬁtting population Q (Q = (2−Po)×1000) and the standard deviation σ. Based on observations, a logarithmic function y = aln(bx+c) is chosen for least squares ﬁtting. The ﬁtting results are shown in the ﬁgure below.

The coefﬁcient of Determination R2 is 0.9999. From the image and the value of R2, the ﬁt is quite well. Therefore, we obtain the method to estimate the the number of people using stairs frequency of multiple people in a typical day from the edge distribution of the measurement matrix Dmeasure . The conclusion can be drawn as: x

Npass = 0.339e0.13125·σx +0.92338 (4.14)

where σx is the standard deviation in X-direction.

In the measurements of the Edinburgh sandstone steps, the normal variance of the wear depth is 12.1.Therefore, we obtain an average of 1.14 people walking side by side on each step.

5 Sensitivity and Robustness Analysis

In our model, we also incorporate parameters closely linked to real-world scenarios. In previous modeling stages, these parameters were determined using data from the ancient stone steps in Edinburgh. However, as scenarios evolve, their value may shift accordingly. By ad- justing these parameters to assess the models sensitivity and robustness, we analyze the results and arrive at the following conclusions.

5.1 Impact of Material Hardness on Wear Volume

Under environmental conditions of 30°Cand 70% relative humidity (RH), the rock wear rate is approximately p ≈0.01/year. The initial hardness H0 values for various materials are as follows:

Metasequoia: 18N/mm2, Poplar: 24N/mm2, Sandstone: 95N/mm2, Marble: 175N/mm2[10].

Based on the analysis results, the initial hardness of wood decreases by 25%, and after 20 years of wear, it increases by an additional 48.1%. Meanwhile, the initial hardness of rock decreases by 45.7%, and after 20 years of wear, it increases by an additional 43.6%. It can be

关注数学模型 concluded that our model is sensitive to material hardness. It is feasible to use hardness for relevant calculations.

5.2 Impact of Weathering Rate Constant on Wear Volume

Subsequently, we examine how varying the weathering rate constant of rock (p) influences the accumulation of wear. Specifically, we set p to 0.0001, 0.0005, 0.0025, and 0.005, then simulate 20 centuries of wear.

0.0040 P 0.0001 0.0035 0.0005 0.0025 0.0030 0.005 Cumulative Wear Volume (m²) 0.0025

0.0020

0.0015

0.0010

0.0005

0.0000 Time (years)

When p increases from 0.0025 to 0.005, the time to saturation decreases by 64.2%.This demonstrates that the wear process is some kind of sensitive to changes in environmental factors or material properties that affect p. We can conclude that when the time is relatively short (around 4 centuries), the model is insensitive to p. However, when the time is longer, the model becomes highly sensitive to p.

5.3 Impact of Reigon on Wear Volume

Finally, we test the model's ability to provide more accurate results under varying regional, environmental, and cultural conditions worldwide to test its robustness. We model four coun- tries natural and human factors and assume the stone steps are made of granite with an initial hardness H0 = 175N/mm². Using distinct conditions, the model can be tested and refined to account for different climates and usage patterns, thereby enhancing its overall reliability.

0.00010 Country Parameters China Brazil 0.00008 Scotland America Cumulative Wear Volume (m³) 0.00006

0.00004

0.00002

00000 20 80 100 40 60 Time (years) Over the span of a century, Brazilian stone steps exhibit 0.001% more wear than Chinese steps, 0.005% more than American steps, and 0.006% more than those in Edinburgh.

Because Brazil has high humidity (RH = 80%), its high corrosion rate (p = 0.012) leads to the fastest wear. Although China and the United States share the same p value, the higher foot trafﬁc in China results in a steeper wear curve. Meanwhile, Scotlands parameters are moderate, producing an intermediate trend.

However, based on the data, the model demonstrates strong robustness across different regions. Combined with the two previous sensitivity analyses, it can be concluded that our model performs well within a certain timeframe.

6 Strength and Weakness

6.1 Strength

(1) Comprehensive Integration of Factors: The model incorporates mechanical wear, pop-

ulation usage patterns, and material properties, providing a more holistic picture of how wear accumulates.

(2) Statistical Treatment of Human Foot Trafﬁc: By using normal (and multi-normal) dis- tributions to capture the variability of footsteps in both the X and Y directions, it reﬂects realistic pedestrian movement patterns (e.g., single-ﬁle vs. parallel use, upward vs. down- ward trafﬁc).

(3) Non-Destructive Measurements: The required data (such as the depth of wear, initial material hardness) can be obtained through non-destructive methods, aligning well with archaeological concerns about preserving heritage.

6.2 Weakness

(1) Reliance on Simplifying Assumptions: The model assumes key factors remain fairly

consistent over long periods. Real-world usage can ﬂuctuate signiﬁcantly

(2) Limited Treatment of Environmental Variability: The model uses a single corrosion

or wear rate p to represent different humidity or temperature conditions. Realistically, microclimates or seasonal cycles could cause more complex, time-varying wear rates that the model may oversimplify.

7 Conclusion

To provide additional assistance to archaeologists, we establisht he Stair Wear Model. This model starts with the wear measure matrix of the research steps and establishes the Wear Vol-

关注数学模型 ume Model (WVM) and the Wear Distribution Model (WDM). The WVM focuses on the wear volume of the steps and identiﬁes the relationships between the factors causing the wear. The WDM, on the other hand, focuses on the wear distribution, studying how people used these steps in the past. To gather more information and evaluate our model, we identiﬁe consistency and reliability indicators related to wear distribution and age. We also propose some methods to determine the source of the stone step material and to assess whether repairs had been con- ducted. Simulations are frequently used in this process. The wear on the steps is inevitable, 微信公众号：数学模型 serving as traces left by people of the past. In the future, we aim to minimize the impact of envi- ronmental factors on our stone analysis by introducing more detailed environmental variables. We hope that our model can assist archaeologists in obtaining the information they seek.
