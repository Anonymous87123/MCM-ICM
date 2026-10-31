# P-B-2010-8362-bd23db32

Status: machine-draft; not source-verified.


<!-- b000001 | title | pages [1] -->
Following the Trail of Data

<!-- b000002 | front_matter | pages [1] -->
Control # 8362 February 22, 2010

<!-- b000003 | furniture | pages [1] -->
1

<!-- b000004 | furniture | pages [2] -->
Control # 8362 2

<!-- b000005 | heading | pages [2] -->
Summary Statement

<!-- b000006 | prose | pages [2] -->
As contracted by the police, our task was to make a model to help apprehend criminals and prevent future oﬀenses by predicting their locations and the locations of such oﬀenses. We chose to generate probability plots to help assist the police in assessing which areas are of higher priority for searching and monitoring. We assume we are given crime site locations and times for past oﬀenses of the criminal whom we are considering.

<!-- b000007 | prose | pages [2] -->
Our model determines the probability that a criminal will be found at any given location in the search area by evaluating a distance decay function for each crime scene location and adding up the probabilities, generating a distribution which can be used to prioritize a search for the criminal. The distance decay function can take various forms, several of which we present in the paper. We use a linear regression to predict the time of the next crime and compute the probability that a crime will occur in a given spot by calculating how much that crime site would change the probability distribution for the criminal’s location. This ﬁnds the location which best ﬁts with the previous crime sites. We also present a model that uses the time of crime to weight the locations. This gives the model the ability to predict changes in the criminal’s patterns.

<!-- b000008 | prose | pages [2] -->
To test our model with realistic data, we complied several case studies. We asess the quality of our predictions using multiple metrics: error distance and search cost. In the case of Peter Sutcliﬀe, our model was able to reduce the search area to 15% of its original size, and predicted the position of his next victim with very high accuracy. We produce color-gradient plots of the probability distributions which we present in the paper.

<!-- b000009 | furniture | pages [3] -->
Control # 8362 3

<!-- b000010 | heading | pages [3] -->
Executive Summary

<!-- b000011 | prose | pages [3] -->
Dear Chief of Police,

<!-- b000012 | prose | pages [3] -->
We have developed a model to help aid you in investigations regarding serial criminals. I am writing to inform you of its functionality and what cases are most appropriate for its uses.

<!-- b000013 | prose | pages [3] -->
Our model requires input from any member of your squad of the time and locations, in latitude and longitude, of the criminal acts you suspect were committed by any speciﬁc criminal. It then uses the locations of these points, along with a function modeling the drop oﬀ in probability as the distance from the crime site increases, to generate a probability distribution of the criminal’s location. Further, it creates a probability distribution of possible future crime scenes by ﬁguring out which point would be least surprising in future probability distribution calculations. Overall, it tends to guess the locations relatively accurately, especially when it comes to future crimes.

<!-- b000014 | prose | pages [3] -->
Unfortunately, our model is not a godsend. It assumes that all input on a given run is for a single criminal, even though its inherent clustering could provide relevant data in the case of multiple criminals. Similarly, we assume that the killer has just one base location from which he or she operates. Our model does not work well for commuter criminals, or those driving long distances in order to commit crimes.

<!-- b000015 | prose | pages [3] -->
Additionally, it relies on the hypothesis that the probability of the criminal’s base being at a given location decreases as you move away from the crime scenes. Furthermore, the model ignores any variations in terrain and in population density, instead assuming that they are both homogeneous.

<!-- b000016 | prose | pages [3] -->
Despite these obvious drawbacks, our model does have many strengths. In addi

<!-- b000017 | furniture | pages [4] -->
Control # 8362 4

<!-- b000018 | prose | pages [4] -->
tion to the aforementioned ability to correctly handle clusters of points, it also gives a very well speciﬁed and intuitive suggested search order, helping police minimize time spent searching for the killer. By abstracting its calculation mechanism, our model is ﬂexible enough to allow your department to select the most appropriate of many possible ”submodels” for your speciﬁc case. Thus, your department need not group bank robbers and rapists in the same category: if the two criminal groups tend to have diﬀerent criminal patterns, our model allows for your department to use the techniques you ﬁnd most appropriate.

<!-- b000019 | prose | pages [4] -->
Furthermore, our model is relatively eﬃcient. Despite a mediocre ”classical” running time, the extremely parallelizable nature of our algorithm allows for many computers to work on the problem in parallel. With only a small number of machines, our model can complete extremely detailed (one million point) calculations in 4 hours, and ten thousand point calculations (which is still suﬃcient detail for most cases) in a couple of seconds. Thus, your department need not worry about waiting days or weeks for results to come in, saving invaluable time.

<!-- b000020 | prose | pages [4] -->
Our model’s output consists of two maps: one with the probability distribution of the criminal’s location and one with the prediction of the location of his/her next crime. The probabilities are displayed in bands of color: a red band represents an area of high priority and a blue band represents one of low priority. In the case of attempting to locate the criminal, we suggest searching the red areas ﬁrst. In the case of trying to prevent a future crime, we suggest spreading as many oﬃcers as possible in the red and yellow bands, as these regions are likely to contain the criminal’s next target.

<!-- b000021 | prose | pages [4] -->
We wish you luck in your investigations.

<!-- b000022 | contents | pages [5] -->
Control # 8362

<!-- b000023 | contents | pages [5] -->
5

<!-- b000024 | heading | pages [5] -->
Contents

<!-- b000025 | contents | pages [5] -->
1 Background

<!-- b000026 | contents | pages [5] -->
6

<!-- b000027 | contents | pages [5] -->
1.1

<!-- b000028 | contents | pages [5] -->
Biography of the Typical Serial Killer . . . . . . . . . . . . . . . . . .

<!-- b000029 | contents | pages [5] -->
6

<!-- b000030 | contents | pages [5] -->
1.2

<!-- b000031 | contents | pages [5] -->
Locating a Killer

<!-- b000032 | contents | pages [5] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000033 | contents | pages [5] -->
6

<!-- b000034 | contents | pages [5] -->
2 The Problem

<!-- b000035 | contents | pages [5] -->
7

<!-- b000036 | contents | pages [5] -->
3 Assumptions

<!-- b000037 | contents | pages [5] -->
7

<!-- b000038 | contents | pages [5] -->
4 Metrics and Functions

<!-- b000039 | contents | pages [5] -->
8

<!-- b000040 | contents | pages [5] -->
4.1

<!-- b000041 | contents | pages [5] -->
Simple Spatial Metrics . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000042 | contents | pages [5] -->
8

<!-- b000043 | contents | pages [5] -->
4.2

<!-- b000044 | contents | pages [5] -->
Simple Cases and Their Spacial Metrics . . . . . . . . . . . . . . . . .

<!-- b000045 | contents | pages [5] -->
9

<!-- b000046 | contents | pages [5] -->
4.3

<!-- b000047 | contents | pages [5] -->
Distance Decay Functions

<!-- b000048 | contents | pages [5] -->
. . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000049 | contents | pages [5] -->
10

<!-- b000050 | contents | pages [5] -->
5 Our Approach

<!-- b000051 | contents | pages [5] -->
12

<!-- b000052 | contents | pages [5] -->
5.1

<!-- b000053 | contents | pages [5] -->
Predicting Criminal Location

<!-- b000054 | contents | pages [5] -->
. . . . . . . . . . . . . . . . . . . . . .

<!-- b000055 | contents | pages [5] -->
12

<!-- b000056 | contents | pages [5] -->
5.1.1

<!-- b000057 | contents | pages [5] -->
Computation

<!-- b000058 | contents | pages [5] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000059 | contents | pages [5] -->
14

<!-- b000060 | contents | pages [5] -->
5.1.2

<!-- b000061 | contents | pages [5] -->
Pseudocode . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000062 | contents | pages [5] -->
14

<!-- b000063 | contents | pages [5] -->
5.1.3

<!-- b000064 | contents | pages [5] -->
Why it Works . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000065 | contents | pages [5] -->
15

<!-- b000066 | contents | pages [5] -->
5.2

<!-- b000067 | contents | pages [5] -->
Predicting Location of the Next Crime . . . . . . . . . . . . . . . . .

<!-- b000068 | contents | pages [5] -->
16

<!-- b000069 | contents | pages [5] -->
5.2.1

<!-- b000070 | contents | pages [5] -->
Method

<!-- b000071 | contents | pages [5] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000072 | contents | pages [5] -->
16

<!-- b000073 | contents | pages [5] -->
5.2.2

<!-- b000074 | contents | pages [5] -->
Edge Behavior . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000075 | contents | pages [5] -->
16

<!-- b000076 | contents | pages [5] -->
5.2.3

<!-- b000077 | contents | pages [5] -->
Complexity

<!-- b000078 | contents | pages [5] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000079 | contents | pages [5] -->
16

<!-- b000080 | contents | pages [5] -->
5.3

<!-- b000081 | contents | pages [5] -->
Predicting Time of Future Crimes . . . . . . . . . . . . . . . . . . . .

<!-- b000082 | contents | pages [5] -->
18

<!-- b000083 | contents | pages [5] -->
5.3.1

<!-- b000084 | contents | pages [5] -->
Method

<!-- b000085 | contents | pages [5] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000086 | contents | pages [5] -->
18

<!-- b000087 | contents | pages [5] -->
5.3.2

<!-- b000088 | contents | pages [5] -->
Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000089 | contents | pages [5] -->
19

<!-- b000090 | contents | pages [5] -->
5.4

<!-- b000091 | contents | pages [5] -->
Time Coupling

<!-- b000092 | contents | pages [5] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000093 | contents | pages [5] -->
19

<!-- b000094 | contents | pages [5] -->
5.4.1

<!-- b000095 | contents | pages [5] -->
Why It Helps . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000096 | contents | pages [5] -->
21

<!-- b000097 | contents | pages [5] -->
6 Result Discussion

<!-- b000098 | contents | pages [5] -->
23

<!-- b000099 | contents | pages [5] -->
6.1

<!-- b000100 | contents | pages [5] -->
Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000101 | contents | pages [5] -->
23

<!-- b000102 | contents | pages [5] -->
6.2

<!-- b000103 | contents | pages [5] -->
Procedure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000104 | contents | pages [5] -->
24

<!-- b000105 | contents | pages [5] -->
7 Conclusion

<!-- b000106 | contents | pages [5] -->
25

<!-- b000107 | contents | pages [5] -->
8 Future Research

<!-- b000108 | contents | pages [5] -->
26

<!-- b000109 | contents | pages [5] -->
8.1

<!-- b000110 | contents | pages [5] -->
Incorporating Statistics and Landscapes

<!-- b000111 | contents | pages [5] -->
. . . . . . . . . . . . . . . .

<!-- b000112 | contents | pages [5] -->
26

<!-- b000113 | contents | pages [5] -->
Appendix A

<!-- b000114 | contents | pages [5] -->
27

<!-- b000115 | contents | pages [6] -->
Control # 8362

<!-- b000116 | contents | pages [6] -->
6

<!-- b000117 | heading | pages [6] -->
1 Background

<!-- b000118 | prose | pages [6] -->
We attempt, in this paper, to present models and future research avenues to fur- ther the eﬀectiveness of geographic proﬁling in locating serial criminals and their future crimes. Motivation for modeling includes the fact that humans are aﬀected by “prior expectations, overconﬁdence, information retrieval, and information process- ing” (Snook et al., 2004) whereas computer simulations remain unbiased and make predictions based on discrete data. While the category of serial criminals includes rapists, killers, robbers and burglars, we speciﬁcally focus our research on the ef- fort of capturing and inhibiting the crimes of serial killers. We will also discuss the applications of our research, in our ﬁnal discussion, to other types of serial criminals.

<!-- b000119 | heading | pages [6] -->
1.1 Biography of the Typical Serial Killer

<!-- b000120 | prose | pages [6] -->
When considering serial killers, we will conform to the norm set to us in previous literature (Arndt et al., 2004):

<!-- b000121 | prose | pages [6] -->
• Must have killed a minimum of three.

<!-- b000122 | prose | pages [6] -->
• Must include a cooling-oﬀtime between killings, to distinguish from mass and spree killers.

<!-- b000123 | prose | pages [6] -->
We do not consider mass murderers because they are generally classiﬁed as killing many people in a short period of time, making future crimes unlikely and capture of them relatively easier. Spree killers kill few within a short period of time; although our model may very well apply to them, they may not kill again or may reveal themselves more readily. Serial killers are distinct from these other two categories in that they typically have a deﬁned psychological purpose for killing and have spread-out killings, providing the police with more suﬃcient time to assemble a search.

<!-- b000124 | prose | pages [6] -->
Usually traumatized during childhood, repercussions of abuse and homicide be- ginning for the average serial killer at age 27.5 (Hickey, 2002). Many have precursors to killings, including robberies or sexual abuse. This is based on Hickey’s Trauma Control Model of the Serial Killer and seems to be supported statistically; most no- ticeably, 84% admitted to assaults on adults during adolescence (Arndt et al., 2004). When a serial killer does begin his homicidal campaign, each killing leads to more habituation and tolerance to the hormones and relief provided which do not fully alle- viate the cravings, leading to decreased period between killings and a cyclical process (Arndt et al., 2004). The career length of a speciﬁc serial killer varies, ranging from around 1 to 5 years, although many may enter prison on other accounts during such a career. The number of killings also varies drastically, as with their IQ.

<!-- b000125 | heading | pages [6] -->
1.2 Locating a Killer

<!-- b000126 | prose | pages [6] -->
To account for all factors aﬀecting speciﬁc killing sites and travel distances would be impossible, as the human decision process is dynamic and virtually boundless.

<!-- b000127 | prose | pages [7] -->
Control # 8362 7

<!-- b000128 | prose | pages [7] -->
As reported by Laukkanen and Santtila, however, “87% of serial rapists in the UK committed their crimes conﬁrming the so-called circle hypothesis.” This technique predicts that the criminal will live within a circle drawn around the two crime loca- tions furthest from each other. Because diﬃcult-to-solve rapes and homicides tend to occur within similar distances from the perpetrator’s residence (Santtila et al., 2007), we assume that similarly most serial murders occur within the circle.

<!-- b000129 | prose | pages [7] -->
Most serial killers and other types of criminals are also shown to not travel far from their base location, with crimes committed dropping as a function of distance (Santtila et al., 2007) - a theory we will refer to by its common name as distance decay. Surround the crime scenes, there also usually exists a buﬀer zone in which the criminal is not likely to live when avoiding detection.

<!-- b000130 | heading | pages [7] -->
2 The Problem

<!-- b000131 | prose | pages [7] -->
As contracted by the police, we are given crime scene locations and times of a speciﬁc criminal. Based on this data, we must predict the criminal’s base location and their next crime’s location and time.

<!-- b000132 | prose | pages [7] -->
Although humans may appear random, we must ﬁt a geographical proﬁle to the crime scene data for prediction purposes in a way such that our model can be used for any type of serial criminal with any personality type. This geographical proﬁle generates a prioritized search for the police. In our plots, note that red speciﬁes high search priority and blue low. We use bilinear interpolation to smooth the grid for ease of interpretation for the police.

<!-- b000133 | heading | pages [7] -->
3 Assumptions

<!-- b000134 | prose | pages [7] -->
As given such location and time data from the police, we assume that the police suspect all points used in a single run of our model are crime sites from a single criminal. We also assume, to simplify locating the criminal, that the speciﬁed killer has precisely one home base which we are trying to ﬁnd.

<!-- b000135 | prose | pages [7, 8] -->
To simplify the problem, we assume we are dealing with serial killers. Although this does not seriously aﬀect our results in any way (Laukkanen & Santtila, 2006; Santtila et al., 2007), we use case studies and research to support location statistics for serial killers and later extend our model results to other types of serial criminals. Also, despite the fact that diﬀerent criminal personalities will commit crimes at dif- ferent distances, we assume a form of the circle theory. Research states that 87% of serial rapists, which can be extended to other types of serial criminals, reside within a circle proposed by the circle hypothesis (see Background - Locating a Criminal) (Santtila et al., 2007); we assume our grid, although not necessarily encompassing the full circle around the furthest two points, will act similarly in encompassing our killer’s location for ease of modeling purposes. We also assume a distance decay, as Control # 8362 8

<!-- b000137 | prose | pages [8] -->
supported by research for typical stable criminals. Thus, we currently do not con- sider commuters who may travel far distances to commit crimes, though in the future we would like to include an option for diﬀerent personality traits to compensate for distance preferences and account for such commuter criminals. We do not inherently assume a buﬀer zone, as will be later discussed, but instead test diﬀerent models and see the accuracy of such an assumption.

<!-- b000138 | prose | pages [8] -->
Some factors which may aﬀect a criminal’s choice of crime site include population density, opportunity, and landscape. In our model, we neglect these diﬀerences and assume a homogeneous geographical area for simplicity. If actually implemented, we would like to include these descriptors in our model, similar to CrimeStat (Levine, 2006). Thus, unfortunately our model may predict the criminal’s base location to be in an inhabitable area and may predict future crimes to be committed where there is, in actuality, little opportunity for such crimes.

<!-- b000139 | prose | pages [8] -->
For more discussion on our future extensions to dispose of such simplifying as- sumptions, see Future Research.

<!-- b000140 | heading | pages [8] -->
4 Metrics and Functions

<!-- b000141 | heading | pages [8] -->
4.1 Simple Spatial Metrics

<!-- b000142 | prose | pages [8] -->
When assuming we are given information including locations of N crime scenes, it is useful to look at spatial metrics to help deﬁne global traits of the locations. We deﬁne the following metrics:

<!-- b000143 | prose | pages [8] -->
Mean Center (“Center of Mass”)

<!-- b000144 | prose | pages [8] -->
This is the point output when taking the average values of latitudes (y) and longitudes (x):

<!-- b000145 | prose | pages [8] -->
N N X X cx = wixi, cy = wiyi .

<!-- b000146 | prose | pages [8] -->
i=1 i=1 It is possible to include a weight, wi, for each point to skew the center more toward it, which may be useful when speciﬁc points are more important than others.

<!-- b000147 | prose | pages [8] -->
Center of Minimum Distance

<!-- b000148 | prose | pages [8] -->
This is the point where the summed distances to all of the crime scenes is minimal, or the minimum considering every (x, y) point of

<!-- b000149 | prose | pages [8] -->
N q (xi −x)2 + (yi −y)2 X

<!-- b000150 | prose | pages [8] -->
i=1 .

<!-- b000151 | prose | pages [9] -->
Control # 8362 9

<!-- b000152 | prose | pages [9] -->
Standard Deviational Circle (SDC)

<!-- b000153 | prose | pages [9] -->
Here, a circle is drawn at the mean center, assuming wi = 1, such that the radius is one “standard distance” (related to standard deviation) to cover 68% of the data points (assuming randomness) and 95% for a radius of two standard distances. The larger the radius, the more spread out the data is considered to be.

<!-- b000154 | prose | pages [9] -->
Standard Deviational Ellipse (SDE)

<!-- b000155 | prose | pages [9] -->
While the standard deviational circle ignores skew of the data, the ellipse allows stretching in two dimensions along any two perpendicular lines on our plane.

<!-- b000156 | heading | pages [9] -->
4.2 Simple Cases and Their Spacial Metrics

<!-- b000157 | prose | pages [9] -->
In order to gather intuition about what we would expect from a model given crime sites, we illustrate a few simple examples of possible killing distributions with expec- tations of where we would like to see predictions of home bases and future killings.1 We analyze some simple spatial statistics for each basic case: mean center (“center of mass”) and standard deviational circle.

<!-- b000158 | prose | pages [9] -->
Uniform Spread

<!-- b000159 | prose | pages [9] -->
First, we look at a uniform distribution of killings within some shape - a square, speciﬁcally, for its ease of modeling on a grid. While we might expect the killer to live anywhere in the boundary of this square, it would not be surprising if the killer lived directly in the center for the comparative ease of travel to all points on the square. For future killings, it may be diﬃcult to discern a speciﬁc location as the spread is homogeneous.

<!-- b000160 | prose | pages [9] -->
The center of mass is directly in the center, as expected. The SDCs are eﬃcient in grouping the data, meaning that our data is not very spread out.

<!-- b000161 | prose | pages [9] -->
Outline Spread

<!-- b000162 | prose | pages [9] -->
Here we consider killings along the edges of a square. It is not clear where the killer may live, as this killing trail may be part of his daily route or he may live closer to the center for ease of travel, but we would expect future killings to happen also along the boundary.

<!-- b000163 | prose | pages [9] -->
1These models were designed for their intuitive simplicity and to test the accuracy of our models later.

<!-- b000164 | prose | pages [10] -->
Control # 8362 10

<!-- b000165 | prose | pages [10] -->
Our mean center is again in the center, but our SDCs are very large, indicating that the data is very spread out from the mean center.

<!-- b000166 | prose | pages [10] -->
Linear Spread

<!-- b000167 | prose | pages [10] -->
Here, we look at a linear killing distribution. While the future killings may depend on the times of each crime committed, speciﬁcally in this example, if we assume the times are irrelevant then we may expect the killer to live near at least a few of the points.

<!-- b000168 | prose | pages [10] -->
Again, our mean center is in the middle and our SDCs are very large, as the points are spread far from the center. The SDE may be more eﬀective in analyzing this case as there is no spread in latitude.

<!-- b000169 | prose | pages [10] -->
Clustering

<!-- b000170 | prose | pages [10] -->
This clustering example may be most prevalent when considering a killer with two main base locations (for example, one who lives in one city and works in an- other). It again may not be clear where the killer lives, but we should predict killings to occur within the two clusters.

<!-- b000171 | prose | pages [10] -->
Again, we have a large SDC. These may indicate that when looking for next killer location, it may be beneﬁcial to look at SDC radii and SDEs.

<!-- b000172 | heading | pages [10] -->
4.3 Distance Decay Functions

<!-- b000173 | prose | pages [10] -->
When calculating probability distributions, we test diﬀerent distance decay functions. Recall that the theory of distance decay assumes drop-oﬀof likelihood of our killer living at any given location as distance from crime scenes increase (see Figure 1). We consider Linear, Normal, Negative Exponential, Truncated Negative Exponential, and Plateaued Negative Exponential drop-oﬀs. Of particular distinction between these are their behaviors directly surrounding the crime scenes and the rates of decay with increased distance.

<!-- b000174 | prose | pages [10] -->
Linear

<!-- b000175 | prose | pages [10] -->
With this model, we assume a linear drop-oﬀrate of the form:

<!-- b000176 | prose | pages [10] -->
 a −bx if x ≤a/b f(x) = 0 if x > a/b.

<!-- b000177 | prose | pages [11] -->
Control # 8362 11

<!-- b000178 | prose | pages [11] -->
Distance Decay Functions 10 Linear 9 Normal Crime Probability (Unnormalized) NE 8 Truncated NE 7

<!-- b000179 | prose | pages [11] -->
6

<!-- b000180 | prose | pages [11] -->
5

<!-- b000181 | prose | pages [11] -->
4

<!-- b000182 | prose | pages [11] -->
3

<!-- b000183 | prose | pages [11] -->
2

<!-- b000184 | prose | pages [11] -->
1

<!-- b000185 | prose | pages [11] -->
0 0 1 2 3 4 5 6 7 8 9 10 Distance From Crime Scene

<!-- b000186 | caption | pages [11] -->
Figure 1: A decay plot.

<!-- b000187 | prose | pages [11] -->
This simple model assumes that the expected probability of ﬁnding the criminal at a given location decreases linearly with distance from the crime site until the distance is greater than a/b, after which it remains zero. Despite the simplicity of this model, its behavior is clearly somewhat unrealistic.

<!-- b000188 | prose | pages [11] -->
Normal

<!-- b000189 | prose | pages [11] -->
This model was suggested by Brantingham and Brantingham (1981) to include their hypothesized buﬀer zone. The function exponentially increases and decreases around such a radius as is maximized by the buﬀer zone:

<!-- b000190 | prose | pages [11] -->
−(x−µ)2 f(x) = ae 2σ2 √ . 2πσ

<!-- b000191 | prose | pages [11] -->
Although this does not work well with our idea of serial killers generally living close to their crime scenes, it may be useful when considering other types of serial criminals such as robbers and burglars are expected to on average live further from their crimes.

<!-- b000192 | prose | pages [11] -->
Negative Exponential

<!-- b000193 | prose | pages [11] -->
Here we assume a negative exponential drop-oﬀrate of the form:

<!-- b000194 | prose | pages [11] -->
f(x) = e−cx

<!-- b000195 | prose | pages [11, 12] -->
where f(0)=1 is the maximum value. Thus, this function assumes that the proba- bility of killer location is highest at the speciﬁc crime scenes from which it decays Control # 8362 12

<!-- b000197 | prose | pages [12] -->
exponentially. Although this contradicts our idea of a “buﬀer zone“, presented by Brantingham & Brantingham (1981), this model is shown to work well in its predic- tions. According to Rhodes, it showed a much better than the Normal curve ﬁt when compared with actual serial burglar, robber, and rapist locations versus their crimes (Rhodes & Conly, 1981; Kent, 2003).

<!-- b000198 | prose | pages [12] -->
Truncated Negative Exponential

<!-- b000199 | prose | pages [12] -->
Here we assume a linear growth from each crime scene to a certain point where the probability is maximal and then drops exponentially:

<!-- b000200 | prose | pages [12] -->
 1 + b(x −x0) if x ≤x0 f(x) = e−c(x−x0) if x > x0.

<!-- b000201 | prose | pages [12] -->
This does support the idea of a buﬀer zone and has a quick drop-oﬀafter some maximal distance. In this model, we are able to specify the parameters b, c, and x0 which may help when considering diﬀerent types of criminals and their average found distance from crime scenes, or when considering diﬀerent social proﬁles of criminals and the eﬀects of such on distance.

<!-- b000202 | prose | pages [12] -->
Plateaued Negative Exponential

<!-- b000203 | prose | pages [12] -->
A special case of the truncated negative exponential occurs when we let b = 0. Instead of the usual rise-and-fall, the function stays level when x ≤x0 and from there drops oﬀlike a regular negative exponential. The function takes the form  1 if x ≤x0 f(x) = e−c(x−x0) if x > x0.

<!-- b000204 | prose | pages [12] -->
This supports the idea that, although there exists a buﬀer zone around the crime scenes where the killer is less likely to live, the area spanned when moving outwards from the crime scene squares and so it is innate in the spread from the crime scene that the probability is higher as distance increases when maintaining a constant probability at each grid point. It considers that the buﬀer zone is not derived from criminals preferring crimes past a certain distance but rather that opportunities increase with distance since the area increases.

<!-- b000205 | heading | pages [12] -->
5 Our Approach

<!-- b000206 | heading | pages [12] -->
5.1 Predicting Criminal Location

<!-- b000207 | prose | pages [12, 13] -->
To predict the criminal’s location, we employ a strategy that, while similar in some superﬁcial ways, greatly generalizes the strategy of locating the criminal by investi- gating the center of mass. Whereas the center of mass approach returns a single point Control # 8362 13

<!-- b000209 | prose | pages [13] -->
(around which one can center a Gaussian distribution, for instance), our method at- tempts to utilize the locations of the criminal acts to the fullest by instead generating a distribution, assigning each point within the given region a probability. These prob- abilities returned can in turn be used to generate a map, showing which locations the algorithm considers to be of high interest and which can probably be ignored. By transforming the set of crime data points into a specially-constructed distribution rather than a handful of values, our algorithm allows for much more specialized, and in many cases much more accurate, results.

<!-- b000210 | prose | pages [13] -->
The main idea driving the algorithm is the idea that any point p can be assigned a relative “criminal location probability” by taking the sum of some function (men- tioned in Metrics and Functions) of the distances between p and prior incidents. It might help to imagine this as the sum of non-canceling “gravitational pulls” of the various locations: any point with a comparatively high total gravitational pull is going to be near many of the crime scenes, and therefore should rightly be assigned a high criminal location probability. Furthermore, the actual strengths of the pulls from each point can be weighted depending on its recency, allowing for the algorithm to more quickly adapt to the changing habits of the criminal. We will currently treat all weights as equal to one, but we will discuss weighting in more detail in Time Coupling.

<!-- b000211 | caption | pages [13] -->
Figure 2: Example of a probability distribution. Red star signiﬁes actual criminal’s base.

<!-- b000212 | prose | pages [14] -->
Control # 8362 14

<!-- b000213 | heading | pages [14] -->
5.1.1 Computation

<!-- b000214 | prose | pages [14] -->
As it is infeasible to calculate the value at every single point and extremely diﬃcult to model analytically, our algorithm instead discretizes the problem by transforming the candidate search area into a grid and calculating the criminal location probability at each grid point. When increasing the ﬁneness of the grid, which is allowed for in the input to our model, our algorithm better approximates the ideal, smooth, solution. Because the algorithm makes l calculations of f per grid point, it has O(nml) runtime where n is the number of lines on the grid parallel to the Prime Meridian, m is the number of lines parallel to the equator, and l is the number of unlawful acts perpetrated by the criminal. As l is generally relatively small and, at least in our simulations, we often set m and n to be equal, this algorithm can essentially be considered to be O(n2), which is going to be very fast for any reasonable mesh size — consider that a single 2GHz machine can use this algorithm to partition an area the size of England into 36 × 36 meter blocks and create a corresponding probability distribution using some interesting distance functions in only a matter of minutes!

<!-- b000215 | heading | pages [14] -->
5.1.2 Pseudocode

<!-- b000216 | prose | pages [14] -->
To clear up any ambiguities, we provide some pseudocode below for the criminal- ﬁnding function.

<!-- b000217 | heading | pages [14] -->
Program 1 Criminal Location Finding Algorithm

<!-- b000218 | prose | pages [14] -->
1 G is the set of grid points after the search area is partitioned by the mesh 1 C is the set of past crimes, each of which has a location and date 1 f(d) is the distance decay function which returns a higher number for more probable locations 1 Prob is the probability of the killer location based on distance decay aﬀects for the grid

<!-- b000219 | heading | pages [14] -->
1 Function criminalLocationProb (crimes C, function f):

<!-- b000220 | prose | pages [14, 15] -->
Let Prob be a mapping from G into R 1 1 for g ∈G do 1 1 /*Calculate cumulative distance eﬀect from all c ∈C*/ 1 1 1 1 1 1 Prob[g] = 0 for c ∈C do 1 1 1 1 1 1 1 Prob[g] = Prob[g] + f(distance between c and g) 1 1 Normalize the values of Prob so that the sum of the values is 1 1 1 return Prob Control # 8362 15

<!-- b000222 | heading | pages [15] -->
5.1.3 Why it Works

<!-- b000223 | prose | pages [15] -->
Our algorithm has many properties that lead to the generation of useful results.

<!-- b000224 | prose | pages [15] -->
Prioritized Search

<!-- b000225 | prose | pages [15] -->
The probability distribution that our algorithm returns lends to a very simple algo- rithm for determining in what order to search various locations for the criminal. One can simply search the possible locations in descending order of their probabilities! This simple strategy often leads to good results, requiring us to go through about 15% of a certain search area to ﬁnd Peter Sutcliﬀe, one of our case study serial killers, for most distance decay functions.

<!-- b000226 | prose | pages [15] -->
Point Clustering

<!-- b000227 | prose | pages [15] -->
One of the nicest features of our algo- rithm is its handling of point clusters without any outside assistance. Be- cause all crime scenes exert a “gravi- tational pull,” points near any crime scenes will have a probability boost and will create localized “hot-spots” where the algorithm thinks the crimi- nal has some reasonable chance of be- ing caught. This eﬀect can be seen on the ﬁgure on the left/right, in which two diﬀerent clumps form two hotspots, with their relative sizes and magnitudes proportional to the number of points inside.

<!-- b000228 | prose | pages [15] -->
Function/Parameter Independence

<!-- b000229 | prose | pages [15] -->
Another major strength of our algorithm is its generality. Because the function works on any reasonable arbitrary function with arbitrary parameters, the police can hand- pick the functions based on statistics and their historical successes in catching the perpetrators of various types of crimes. For example, because burglars and serial killers generally exhibit diﬀerent behaviors in selecting how far they are willing to travel to commit their crime, it could be that a normal distance decay function would be superior for catching burglars whereas a negative exponential distance decay function could be superior for catching serial killers. As our algorithm is extremely ﬂexible, the police can quickly and easily adapt their search techniques to best match the criminal in question.

<!-- b000230 | prose | pages [16] -->
Control # 8362 16

<!-- b000231 | heading | pages [16] -->
5.2 Predicting Location of the Next Crime

<!-- b000232 | heading | pages [16] -->
5.2.1 Method

<!-- b000233 | prose | pages [16] -->
In order to ﬁnd the location of the next crime, we look for the point on the grid which most closely matches the pattern of the other crimes. If we consider the criminal location probability distribution produced after adding a crime event to our grid, the most probable location for the next crime would be the spot which generates a distribution most similar to the one produced before adding it. This gives us the most likely location for a future crime. Furthermore, for potential crime scenes other than the most probable, we estimate how much worse they are by measuring how much the produced distribution deviates from the original. This gives us a distribution over our search area which can be used to allocate resources for crime prevention.

<!-- b000234 | prose | pages [16] -->
Our algorithm works as follows: First we compute the criminal location proba- bility distribution for the search area. Next we iterate through all of the grid points in the search area, adding a new ”virtual crime scene” at each point, calculating the new criminal location probability distribution with the additional crime scene. We then compare each of these distributions to the original one by summing the squares of the diﬀerences between corresponding grid points, then assigning this pseudo prob- ability deviation number to the location of the ”virtual crime scene.” This gives us a distribution over the search area, where lower numbers mean the point is a more likely spot for the criminal’s next crime because adding this point as a crime location deviates less from the original probability distribution.

<!-- b000235 | heading | pages [16] -->
5.2.2 Edge Behavior

<!-- b000236 | prose | pages [16] -->
If all of the points on the mesh are tested as possible crime scenes, then there is a tendency for points near the edge to be rated higher than appropriate. This is because a point near the edge has fewer other points around it, so when a crime scene is added there it is eﬀecting the criminal location probability distribution of fewer points, and thus has a smaller total eﬀect on the produced distribution. To compensate for this, we add a buﬀer zone around our search area where the criminal location probability distribution is calculated but no crime scenes are added. This eﬀectively removes the bad edge behavior.

<!-- b000237 | heading | pages [16] -->
5.2.3 Complexity

<!-- b000238 | prose | pages [16] -->
When adding each point as a virtual crime scene, we must calculate a diﬀerent crimi- nal location probability distribution for every point in our search area, thus requiring approximately n2 operations, each of which is O(n2) (see Predicting Criminal Loca- tion - Computation). Therefore the algorithm for determining the location of the next crime has a complexity of O(n4). This is a polynomial time algorithm, but it can still become very slow as n increases. To keep our calculation time from getting out of control, we implement various optimizations.

<!-- b000239 | prose | pages [17] -->
Control # 8362 17

<!-- b000240 | heading | pages [17] -->
Program 2 The killer-ﬁnding and future-predicting algorithm

<!-- b000241 | prose | pages [17] -->
1 G is the set of grid points after the search area is partitioned by the mesh 1 G′ is G augmented with a 40% boundary buﬀer zone 1 C is the set of past crimes, each of which has a location and date 1 f(d) is the distance decay function which returns a higher number for more probable locations 1 Prob is the probability of the killer location based on distance decay aﬀects for the grid 1 ∆Prob measures the change in distribution of Prob when adding a new crime scene

<!-- b000242 | heading | pages [17] -->
1 Function criminalLocationProb (crimes C, function f):

<!-- b000243 | prose | pages [17] -->
Let Prob be a mapping from G′ into R 1 1 for g ∈G′ do 1 1 /*Calculate cumulative distance aﬀect from all c ∈C*/ 1 1 1 1 1 1 Prob[g] = 0 for c ∈C do 1 1 1 1 1 1 1 Prob[g] = Prob[g] + f(distance between c and g) 1 1 Normalize the values of Prob so that the sum of the values is 1 1 1 return Prob

<!-- b000244 | heading | pages [17] -->
1 Function nextCrimeProb (crimes C, function f):

<!-- b000245 | prose | pages [17, 18] -->
1 1 killer prob distrib = criminalLocationProb(C,f) Let ∆Prob be a mapping from G′ into R 1 1 for g ∈G′ do 1 1 Let C′ be C augmented with a “virtual crime” at g 1 1 1 V = criminalLocationProb(C′,f) 1 1 1 1 1 1 /*Calculate sum of squared diﬀerences between killer prob distrib and V */ 1 1 1 ∆Prob[g] = 0 for h ∈G′ do 1 1 1 ∆Prob[g] = ∆Prob[g] + (V[h] −killer prob distrib[h])2 1 1 1 1 1 1 Normalize the values of ∆Prob so that the sum of the values is 1 1 1 return ∆Prob Control # 8362 18

<!-- b000247 | prose | pages [18] -->
(a) No buﬀer. (b) 30% buﬀer.

<!-- b000248 | caption | pages [18] -->
Figure 3: Varying buﬀer percentages to illustrate boundary conditions.

<!-- b000249 | prose | pages [18] -->
The single most important optimization implemented in our algorithm is caching. Suppose our search area has N crime scenes. For each point on the mesh we add a virtual crime scene and then calculate the criminal location probability distribution over the search area using the N + 1 points. When calculating the new probability distribution with N +1 points, instead of doing the full calculation, we use the original distribution for the ﬁrst N points and combine it with a distribution for only the new point in a way that maintains normalization. This gives the algorithm a factor of N speedup.

<!-- b000250 | prose | pages [18] -->
Our algorithm is also nearly perfectly parallelizable. By multi-threading the code, it can be run over a number of cores with a speedup equal to the number of cores used. This makes running very high resolution calculations practical if a multicore or computing cluster is available.

<!-- b000251 | heading | pages [18] -->
5.3 Predicting Time of Future Crimes

<!-- b000252 | heading | pages [18] -->
5.3.1 Method

<!-- b000253 | prose | pages [18] -->
When considering a serial killer’s next time or date of killing, we look at a basic lin- ear regression model. We ﬁnd the average time between killings to predict the next killing from the last. To test our model, we remove the last point from the N killing times which we attempt to predict using our regression:

<!-- b000254 | prose | pages [19] -->
Chester Turner 14 Control # 8362 19 12

<!-- b000255 | prose | pages [19] -->
10 tN = tN−1 + tN−1 −t1 Kill Number 8 . N −1 6

<!-- b000256 | prose | pages [19] -->
4

<!-- b000257 | heading | pages [19] -->
5.3.2 Motivation

<!-- b000258 | prose | pages [19] -->
2 Although a linear regression may not be realistic for every killer, it applies 0 1986 1988 1990 1992 1994 1996 1998 2000 more generally to all as some may in-

<!-- b000259 | caption | pages [19] -->
Figure 4: Predicted Nth crime in red; actual

<!-- b000260 | prose | pages [19] -->
crease their frequency of killings as ha- Nth crime in black. bituation sets in and some may de- crease their frequency. Hypothesized by Hickey’s Trauma Control Model and veriﬁed by Arndt’s analysis of Newton’s Hunting Humans which is a collection of data of serial killers, the killing rate of serial killers generally increases with time; however, there are many sources which state that the killing rate may also decrease in some cases (Arndt et al., 2004). Because other interpolation techniques such as exponential or quadratic may greatly over-predict future crimes because of strong end-behavior, we choose to use the linear regression for its simplicity and universal niceness.

<!-- b000261 | heading | pages [19] -->
5.4 Time Coupling

<!-- b000262 | prose | pages [19] -->
Having developed methods for predicting both the criminal location and where the next crime will occur, we now extend these methods by adding in the concept of time. As described so far, the algorithm neglects all chronological properties of the killings, discarding one of the most important pieces of information available to us. Ideally, we want to be able to quickly adapt to the criminal’s motion if they were to move to a diﬀerent location or otherwise alter behavior over time.

<!-- b000263 | prose | pages [19] -->
To account for these possible changes, we weight events more heavily the more recently they occurred. Doing this allows for recent changes in behavior to be more strongly reﬂected in future predictions, which allows for better calibration with the criminal’s latest motives. To keep the algorithm as general as before, we will modify the algorithm to take a weighting function as an input, which is then multiplied by f(dist) when we calculate Prob[g].

<!-- b000264 | prose | pages [19] -->
Although the composition of the weighting function w can be anything, we notice that

<!-- b000265 | prose | pages [19, 20] -->
w(t) = (d −c)a √ t + a + c yields reasonable results. Due to time constraints, this w was the only reasonable weighting function which we managed to study in depth, and therefore any future Control # 8362 20

<!-- b000267 | heading | pages [20] -->
Program 3 The killer-ﬁnding and future-predicting algorithm with time-based

<!-- b000268 | prose | pages [20] -->
weighting 1 G is the set of grid points after the search area is partitioned by the mesh 1 G′ is G augmented with a 30% boundary buﬀer zone 1 C is the set of past crimes, each of which has a location and date 1 f(d) is the distance decay function which returns a higher number for more probable locations 1 w(t) is the weight function which returns a higher number for smaller inputs

<!-- b000269 | prose | pages [20] -->
1 Prob is the probability of the killer location based on distance decay aﬀects for the grid 1 ∆Prob measures the change in distribution of Prob when adding a new crime scene

<!-- b000270 | heading | pages [20] -->
1 Function criminalLocationProb (crimes C, decay function f, weight function w):

<!-- b000271 | prose | pages [20] -->
Let Prob be a mapping from G′ into R 1 1 for g ∈G′ do 1 1 /*Calculate cumulative distance eﬀect from all c ∈C*/ 1 1 1 1 1 1 Prob[g] = 0 for c ∈C do 1 1 1 Prob[g] = Prob[g] + w(time since ctime) · f(distance between c and g) 1 1 1 1 1 1 Normalize the values of Prob so that the sum of the values is 1 1 1 return Prob

<!-- b000272 | heading | pages [20] -->
1 Function futureCrimeProb (crimes C, decay function f, weight function w):

<!-- b000273 | prose | pages [20] -->
1 1 killer prob distrib = criminalLocationProb(C,f,w) Let ∆Prob be a mapping from G′ into R 1 1

<!-- b000274 | prose | pages [20] -->
for g ∈G′ do 1 1 Let C′ be C augmented with a “virtual crime” at g 1 1 1 V = criminalLocationProb(C′,f,w) 1 1 1

<!-- b000275 | prose | pages [20] -->
1 1 1 /*Calculate sum of squared diﬀerences between killer prob distrib and V */ 1 1 1 ∆Prob[g] = 0 for h ∈G′ do 1 1 1 ∆Prob[g] = ∆Prob[g] + (V[h] −killer prob distrib[h])2 1 1 1 1

<!-- b000276 | prose | pages [20, 21] -->
1 1 Normalize the values of ∆Prob so that the sum of the values is 1 1 1 return ∆Prob Control # 8362 21

<!-- b000278 | prose | pages [21] -->
Weight Function 10

<!-- b000279 | prose | pages [21] -->
9

<!-- b000280 | prose | pages [21] -->
8

<!-- b000281 | prose | pages [21] -->
7 Weight 6

<!-- b000282 | prose | pages [21] -->
5

<!-- b000283 | prose | pages [21] -->
4

<!-- b000284 | prose | pages [21] -->
3

<!-- b000285 | prose | pages [21] -->
2 0 20 40 60 80 100 Time (Days)

<!-- b000286 | caption | pages [21] -->
Figure 5: A decay plot.

<!-- b000287 | prose | pages [21] -->
time-based models use this w as the time weighting function.

<!-- b000288 | heading | pages [21] -->
5.4.1 Why It Helps

<!-- b000289 | prose | pages [21] -->
To help emphasize the beneﬁts of time coupling, we consider a randomly generated scenario. The points in the following graphs were automatically generated to be close- to-linear, and some randomly selected set of times generated by a Poisson process were matched to these points in one of two ways:

<!-- b000290 | prose | pages [21] -->
• In the “correlated” case, the times were chosen to increase monotonically with x. That is, the larger the value of x, the larger the time that was assigned to it.

<!-- b000291 | prose | pages [21] -->
• In the “uncorrelated” case, the various times were assigned randomly to the points.

<!-- b000292 | prose | pages [21, 22] -->
Notice how the addition of time-based weighting in the uncorrelated case had almost no eﬀect when compared to the correlated case, in which the eﬀect of the weighting was pronounced. As there was no correlation in the former case, any small pertur- bations will essentially cancel each other out, leaving each point with no expected Control # 8362 22

<!-- b000294 | prose | pages [22] -->
(a) Next Crime Probability Plot with unweighted (b) Next Crime Probability Plot with weighted time, uncorrelated points. time, uncorrelated points.

<!-- b000295 | prose | pages [22] -->
(c) Next Crime Probability Plot with unweighted (d) Next Crime Probability Plot with weighted time, correlated points. time, correlated points.

<!-- b000296 | prose | pages [23] -->
Control # 8362 23

<!-- b000297 | prose | pages [23] -->
(e) Criminal Location Probability Plot with un- (f) Criminal Location Probability Plot with weighted time, correlated points. weighted time, correlated points.

<!-- b000298 | prose | pages [23] -->
change. Thus, the correctness of the plot is not drastically aﬀected, if at all. In the latter case, however, the correlation was captured by the algorithm and the expected location of the next killing shifted rather drastically to accommodate this change. Intuitively, if a serial killer has been moving north one mile every day for a while, it is reasonable to assume that his or her future kills will be more north than average.

<!-- b000299 | prose | pages [23] -->
Perhaps even more interesting, the location of the next crime adapted much more quickly than the estimated location of the criminal. Again, this is sensible: a gradual shift in the location of crimes is much more indicative of a behavior-based shift than one that is residence-based.

<!-- b000300 | heading | pages [23] -->
6 Result Discussion

<!-- b000301 | prose | pages [23] -->
To evaluate our models, including various choices for our distance decay function, we look at case study data (see Appendix A) for actual apprehended serial killers: Peter Sutcliﬀe and Chester Turner.

<!-- b000302 | heading | pages [23] -->
6.1 Metrics

<!-- b000303 | prose | pages [23] -->
We use two metrics in quantifying the quality of our results. The ﬁrst is Error Distance and the second is Search Cost.

<!-- b000304 | prose | pages [24] -->
Control # 8362 24

<!-- b000305 | prose | pages [24] -->
Error Distance

<!-- b000306 | prose | pages [24] -->
This mesaures the distance between the calculated most probable spot and the actual spot “as the crow ﬂies”. When searching for the criminal, the error distance tells us how far away our best guess was from the actual location. When predicting the next crime it tells us how far away the crime happened from the location where we allocated the most resources.

<!-- b000307 | prose | pages [24] -->
Search Cost

<!-- b000308 | prose | pages [24] -->
This measures how many grid squares would need to be searched out of the total before the correct spot is found if we go through the squares in the order of their probability. When searching for the criminal this tells us how much area would need to be searched to ﬁnd the criminal. We assume no preference over locations of the same color and thus this may vary in actual police searching where the initial search direction may vary. When predicting the location of the next crime it tells us what percentage of our resources were wasted on locations that had higher priority than the actual location but saw no actual crime. This metric provides a much more realistic assessment of the quality of a prediction; however, in some instances the Error Distance still provides useful information.

<!-- b000309 | heading | pages [24] -->
6.2 Procedure

<!-- b000310 | prose | pages [24] -->
We use the model without the time-dependent weighting ﬁrst. Thus for these calcula- tions the times of the killings are irrelevant to the calculated probability distributions for the criminal’s location and the location of his next crime; however, the times are used to calculate when the next crime will occur.

<!-- b000311 | prose | pages [24] -->
We begin by removing the most recent crime from our datasets. This emulates the position the police would be in while searching for the criminal. Next we calculate the criminal location probability distribution using each of our decay functions. The quality of these calculations is assesed using both of our metrics, comparing the predicted locations to the actual known locations of the killers’ home. Then we calculate the next crime location probability distribution for each decay function. These results are also assesed using the metrics. Finally, we repeat the calculations using the model with time dependent weights. The results is presented below. Plots can be found in the Appedix.

<!-- b000312 | prose | pages [25] -->
Control # 8362 25

<!-- b000313 | prose | pages [25] -->
Method Criminal Home Criminal Home Next Crime Next Crime Uncoupled Coupled Uncoupled Coupled

<!-- b000314 | prose | pages [25] -->
Sutcliﬀe

<!-- b000315 | prose | pages [25] -->
Linear 18.17/17.88 19.26/29.49 3.99/9.47 3.41/8.73 Neg. Exp. 15.97/30.24 17.05/30.24 0.27/1.46 0.26/1.46 Trunc. Neg. Exp. 14.44/24.32 15.53/24.32 1.98/8.00 1.65/7.28 Plateau Neg. Exp. 15.00/25.07 16.33/25.07 1.25/5.70 1.04/4.98 Normal 15.00/22.83 15.99/22.92 0.81/4.27 0.63/3.58

<!-- b000316 | prose | pages [25] -->
Chester Turner

<!-- b000317 | prose | pages [25] -->
Linear 58.64/5.52 60.12/5.92 40.90/4.12 44.46/5.10 Neg. Exp. 59.80/5.07 60.79/5.07 41.06/3.12 45.93/3.26 Trunc. Neg. Exp. 59.80/4.38 60.79/4.38 40.68/3.46 45.26/4.12 Plateau Neg. Exp. 59.80/4.48 60.79/4.48 40.79/3.26 45.58/3.46 Normal 66.04/4.46 66.70/4.46 40.83/3.26 43.38/3.46

<!-- b000318 | caption | pages [25] -->
Table 1: Search Costs / Error Distance using various functions for both the Sutcliﬀe and

<!-- b000319 | prose | pages [25] -->
Chester Turner data.

<!-- b000320 | heading | pages [25] -->
7 Conclusion

<!-- b000321 | prose | pages [25] -->
All examined distance decay functions tend to do a good job when examining ”good” data, which is data in which the next kill or killer location tends to be in the general vicinity of the killings. In the case of Peter Sutcliﬀe, our algorithm predicted Sutcliﬀe’s location rather accurately on any distance decay function and guessed the location of the next crime almost exactly in many cases.

<!-- b000322 | prose | pages [25] -->
Unfortunately, the data can be misleading. In the case of Chester Turner, who exclusively committed murders to the east of his home, the algorithm unsurprisingly failed to guess his home address accurately. This is unavoidable: there is no method (as far as we can tell) to accurately guess the killer’s “hub” location if it is suﬃciently removed from the locations of the crimes themselves.

<!-- b000323 | prose | pages [25] -->
In either case, it seems that the guessing accuracy for the next crime location is much better than that for the location of the criminal. While this result is somewhat surprising, as the guess for the next crime location is itself based on the estimated killer location, it is still possible to explain. One simple explanation which can be visually veriﬁed of this phenomenon is that killers tended to cluster their killings closely, allowing for easier guessing for the next crime. Another possible explanation is that the increased number of calculations required to generate the estimated next location resulted in signiﬁcantly smaller random ﬂuctuations, meaning that the data is “smoother” and therefore more likely to behave well.

<!-- b000324 | prose | pages [25, 26] -->
Contrary to our expectations, the addition of time coupling generally, but not always, decreased our performance. While we don’t currently have any explanation much better than “bad luck” for this behavior, this result is something that should Control # 8362 26

<!-- b000326 | prose | pages [26] -->
deﬁnitely be examined before serious use of this tool by the police. It seems that time coupling only gives superior performance when the spatial and temporal aspects of the previous crimes is correlated. Without time coupling, our model misses this pattern in the data, but the time coupled version ﬁnds it.

<!-- b000327 | prose | pages [26] -->
Even with the model’s ﬂaws, we believe that it can be a useful tool for any police station to employ. If the model managed to give us such accurate data for predicting the whereabouts of Sutcliﬀe’s next victim, it is not unreasonable to believe that the tool could repeat this behavior for larger datasets. With this predictive power in hand, the police can better prepare for upcoming attacks and apprehend the criminal.

<!-- b000328 | heading | pages [26] -->
8 Future Research

<!-- b000329 | heading | pages [26] -->
8.1 Incorporating Statistics and Landscapes

<!-- b000330 | prose | pages [26] -->
Although our model avoids human bias toward overconﬁdence and predisposed pre- dictions, one might argue “information that a person, animal or institution knows about a physical or social environment” (Gigerenzer & Selton, 2001, 187) gives hu- mans the beneﬁt for predicting locations; however, we would like to incorporate that information into our model: the landscape, personality proﬁle, population density. Eventually, one may be able to also specify social personality regions - for example, rich areas versus poor, known drug-traﬃcking areas, etc. We believe this augmenta- tion would not only lead to better predictions by our model but also give it a clearer advantage over human predictors. In such cases as we are considering, it is not imme- diately obvious where the serial criminal lives or will commit their next crime. Thus, we support probabilities and statistics against human bias.

<!-- b000331 | prose | pages [26] -->
Diﬀerent personality types of criminals (e.g., team killers, sexually motivated killers, burglars, etc.) also commit crimes at diﬀerent distances from their base. Team killers are less likely to kill women and live in a more geographically localized area; sexually motivated killers are more likely to use a more personal killing method, such as strangulation, and prefer strangers more, but tended to be more geographically stable as compared to non-sexually motivated killers (Arndt et al., 2004). These per- sonality inferences may be made by surveying crime scenes. In our model, therefore, we could have optional inputs for use by police to specify personality traits, which we could then use to alter our parameters automatically to predict more probable distances with more ease for the police.

<!-- b000332 | prose | pages [26] -->
Serial Killer Predicted Crime Actual Crime

<!-- b000333 | prose | pages [26, 27] -->
Sutcliﬀe 09-Dec-1980 17-Nov-1980 Zodiac Killer 30-Dec-1969 11-Oct-1969 Jack the Ripper 07-Oct-1888 09-Nov-1888 Grim Sleeper 24-Feb-2005 01-Jan-2007 Chester Turner 01-Jan-1999 06-Apr-1998 Control # 8362 27

<!-- b000335 | heading | pages [27] -->
Appendix A

<!-- b000336 | prose | pages [27] -->
Serial Killer Case Study Data

<!-- b000337 | prose | pages [27] -->
Serial Killer Latitude Longitude Date of Killing 53◦49’22.72”N 1◦34’38.03”W November 17 1980, 9:25 pm 53◦48’30.95”N 1◦40’18.26”W August 20 1980, 11:00 pm 53◦48’47.58”N 1◦34’3.23”W September 2 1979, 1:00 am 53◦42’40.28”N 1◦52’18.99”W April 4 1979, 11:55 pm 53◦27’46.12”N 2◦13’35.21”W May 16 1978, 11:00 pm 53◦39’17.04”N 1◦46’46.20”W January 31 1978, 9:25 pm 53◦47’57.94”N 1◦45’59.09”W January 21 1978, 9:30 pm 53◦25’57.94”N 2◦15’2.47”W October 1 1977, 9:30 pm 53◦49’4.56”N 1◦31’58.99”W June 26 1977, 2:15 am Sutcliﬀe 53◦48’38.70”N 1◦45’49.79”W April 23 1977, 11:15 pm 53◦50’1.26”N 1◦30’9.15”W February 5 1977, 11:30 pm 53◦48’28.75”N 1◦31’58.58”W January 20 1976, 7:30 pm 53◦52’7.83”N 1◦54’28.10”W July 5 1975, 1:30 am 53◦49’7.15”N 1◦32’31.71”W October 30 1975, 1:30 am 53◦48’55.72”N 1◦32’28.77”W December 14 1977, 8:30 pm 53◦47’12.39”N 1◦43’47.22”W July 10 1977, 3:20 am 53◦43’48.65”N 1◦51’54.77”W August 15 1975, 11:45 pm 53◦54’52.78”N 1◦56’16.61”W August 27 1975, 10:30 pm 33◦56’36.66”N 118◦16’50.04”W March 9, 1987 33◦56’24.32”N 118◦16’49.98”W October 29 1987 33◦56’49.26”N 118◦16’57.66”W January 20 1989 33◦57’23.37”N 118◦16’57.85”W September 23 1989 33◦56’50.59”N 118◦16’50.55”W September 30 1992 33◦56’50.59”N 118◦16’50.55”W November 16 1992 33◦56’53.00”N 118◦16’57.77”W Chester Turner December 16 1992 33◦58’7.02”N 118◦16’57.78”W April 2 1993 33◦58’40.96”N 118◦17’5.57”W May 16 1993 33◦58’0.20”N 118◦16’59.76”W February 12 1995 33◦56’56.43”N 118◦16’42.38”W November 6 1996 34◦2’56.29”N 118◦15’20.32”W February 3 1998 34◦2’31.22”N 118◦14’26.07”W April 6 1998 38◦5’49.94”N 122◦8’59.18”W December 20 1968, 11:15 pm 38◦7’12.90”N 122◦11’30.51”W July 4 1969, 11:55 pm Zodiac Killer 38◦34’9.57”N 122◦14’7.71”W September 27 1969, 6:15 pm 37◦47’19.34”N 122◦27’25.98”W October 11, 1969, 9:55 pm 34◦0’17.48”N 118◦19’17.57”W August 12 1986 34◦0’14.98”N 118◦18’35.63”W September 11 1988 33◦59’37.53”N 118◦15’4.83”W January 10 1987 33◦58’41.68”N 118◦17’33.75”W August 10 1985 33◦58’32.96”N 118◦18’7.76”W August 14 1986 33◦57’54.10”N 118◦19’0.30”W March 9 2002 Grim Sleeper 33◦57’27.36”N 118◦18’31.85”W November 1 1987 33◦57’7.36”N 118◦18’31.24”W April 16 1987 33◦56’50.31”N 118◦18’30.33”W January 1 2007 33◦57’17.11”N 118◦17’55.40”W November 20 1988 33◦56’41.05”N 118◦19’2.66”W January 30 1988 33◦56’19.68”N 118◦18’15.39”W July 11 2003 51◦31’12.17”N 0◦3’37.34”W August 31 1988 51◦31’13.51”N 0◦4’20.70”W September 8 1988 51◦30’49.90”N 0◦3’57.16”W Jack the Ripper September 30 1988 51◦30’49.13”N 0◦4’39.64”W September 30 1988 51◦31’7.29”N 0◦4’30.32”W November 9 1988

<!-- b000338 | prose | pages [27] -->
Data collected via GoogleEarthTM and CommunityWalk.

<!-- b000339 | prose | pages [28] -->
Control # 8362 28

<!-- b000340 | heading | pages [28] -->
Model Plots for Sutcliﬀe

<!-- b000341 | prose | pages [28] -->
Here we show our presented functions for distance decay with their plots for Sutcliﬀe and Chester Turner. These are here to illustrate the diﬀerences between the diﬀerent functions.

<!-- b000342 | prose | pages [28] -->
(g) Criminal Location Probability Plot of Sut- (h) Next Crime Probability Plot of Sutcliﬀe using cliﬀe using Linear decay function. Linear decay function.

<!-- b000343 | prose | pages [29] -->
Control # 8362 29

<!-- b000344 | prose | pages [29] -->
(i) Criminal Location Probability Plot of Sut- (j) Next Crime Probability Plot of Sutcliﬀe using cliﬀe using Negative Exponential decay function. Negative Exponential decay function.

<!-- b000345 | prose | pages [29] -->
(k) Criminal Location Probability Plot of Sut- (l) Criminal Location Probability Plot of Sut- cliﬀe using Truncated Negative Exponential de- cliﬀe using Truncated Negative Exponential de- cay function. cay function.

<!-- b000346 | prose | pages [30] -->
Control # 8362 30

<!-- b000347 | prose | pages [30] -->
(m) Criminal Location Probability Plot of Sut- (n) Next Crime Probability Plot of Sutcliﬀe using cliﬀe using Plateaud Negative Exponential decay Plateaued Negative Exponential decay function. function.

<!-- b000348 | prose | pages [30] -->
(o) Criminal Location Probability Plot of Sut- (p) Next Crime Probability Plot of Sutcliﬀe using cliﬀe using Normal decay function. Normal function.

<!-- b000349 | prose | pages [31] -->
Control # 8362 31

<!-- b000350 | prose | pages [31] -->
(q) Criminal Location Probability Plot of Sut- (r) Next Crime Probability Plot of Sutcliﬀe using cliﬀe using Negative Exponential decay function, Negative Exponential function, time weighted. time weighted.

<!-- b000351 | prose | pages [32] -->
Control # 8362 32

<!-- b000352 | heading | pages [32] -->
Model Plots for Chester Turner

<!-- b000353 | prose | pages [32] -->
(s) Criminal Location Probability Plot of Sut- (t) Next Crime Probability Plot of Sutcliﬀe using cliﬀe using Negative Exponential decay function, Negative Exponential function, time weighted. time weighted.

<!-- b000354 | prose | pages [33] -->
Control # 8362 33

<!-- b000355 | heading | pages [33] -->
References

<!-- b000356 | references | pages [33] -->
Arndt, W. B., Hietpas, T., & Kim, J. (2004). Critical characteristics of male serial

<!-- b000357 | references | pages [33] -->
murderers. American Journal of Criminal Justice, 29(1), 171–131.

<!-- b000358 | references | pages [33] -->
Brantingham, P., & Brantingham, P. (1981). Environmental Criminology. Beverly

<!-- b000359 | references | pages [33] -->
Hills, CA: Sage Publications.

<!-- b000360 | references | pages [33] -->
Gigerenzer, G., & Selton, R. (2001). Bounded rationality. London: MIT Press.

<!-- b000361 | references | pages [33] -->
Hickey, E. W. (2002). Serial murderers and their victims. Belmont, CA: Wadsworth,

<!-- b000362 | references | pages [33] -->
3 ed.

<!-- b000363 | references | pages [33] -->
Kent, J. D. (2003). Using Functional Distance Measures When Calibrating Journey-

<!-- b000364 | references | pages [33] -->
to-Crime Distance Decay Algorithms. Ph.D. thesis, Louisiana State University.

<!-- b000365 | references | pages [33] -->
Laukkanen, M., & Santtila, P. (2006). Predicting the residential location of a serial

<!-- b000366 | references | pages [33] -->
commercial robber. Forensic Science International, 157, 71–82.

<!-- b000367 | references | pages [33] -->
Levine, N. (2006). Crime mapping and the crimestat program. Geographical Analysis,

<!-- b000368 | references | pages [33] -->
38(1), 41–56.

<!-- b000369 | references | pages [33] -->
Newton, M. (1990). Hunting Humans. Port Townsend, WA: Loompanics Unlimited.

<!-- b000370 | references | pages [33] -->
Rhodes, W., & Conly, C. (1981). Crime and Mobility: An Empirical Study. Envi-

<!-- b000371 | references | pages [33] -->
ronmental Criminology. Prospect Heights, IL: Waveland Press, Inc.

<!-- b000372 | references | pages [33] -->
Santtila, P., Laukkanen, M., & Zappala, A. (2007). Crime behaviors and distance

<!-- b000373 | references | pages [33] -->
travelled in homocides and rapes. Journal of Investigative Psychology and Oﬀender

<!-- b000374 | references | pages [33] -->
Proﬁling, 4, 1–15.

<!-- b000375 | references | pages [33] -->
Snook, B., Taylor, P. J., & Bennell, C. (2004). Geographic proﬁling: The fast, frugal,

<!-- b000376 | references | pages [33] -->
and accurate way. Applied Cognitive Psychology, 18, 105–121.
