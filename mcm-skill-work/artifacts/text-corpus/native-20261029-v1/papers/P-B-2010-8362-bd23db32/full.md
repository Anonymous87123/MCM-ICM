# P-B-2010-8362-bd23db32

Status: machine-draft; not source-verified.


<!-- b000001 | title | pages [1] -->
Following the Trail of Data

<!-- b000002 | prose | pages [1] -->
Control # 8362

<!-- b000003 | prose | pages [1] -->
February 22, 2010

<!-- b000004 | prose | pages [1] -->
1

<!-- b000005 | prose | pages [2] -->
Control # 8362 2

<!-- b000006 | prose | pages [2] -->
Summary Statement

<!-- b000007 | prose | pages [2] -->
As contracted by the police, our task was to make a model to help apprehend criminals and prevent future oﬀenses by predicting their locations and the locations of such oﬀenses. We chose to generate probability plots to help assist the police in assessing which areas are of higher priority for searching and monitoring. We assume we are given crime site locations and times for past oﬀenses of the criminal whom we are considering.

<!-- b000008 | prose | pages [2] -->
Our model determines the probability that a criminal will be found at any given location in the search area by evaluating a distance decay function for each crime scene location and adding up the probabilities, generating a distribution which can be used to prioritize a search for the criminal. The distance decay function can take various forms, several of which we present in the paper. We use a linear regression to predict the time of the next crime and compute the probability that a crime will occur in a given spot by calculating how much that crime site would change the probability distribution for the criminal’s location. This ﬁnds the location which best ﬁts with the previous crime sites. We also present a model that uses the time of crime to weight the locations. This gives the model the ability to predict changes in the criminal’s patterns.

<!-- b000009 | prose | pages [2] -->
To test our model with realistic data, we complied several case studies. We asess the quality of our predictions using multiple metrics: error distance and search cost. In the case of Peter Sutcliﬀe, our model was able to reduce the search area to 15% of its original size, and predicted the position of his next victim with very high accuracy. We produce color-gradient plots of the probability distributions which we present in the paper.

<!-- b000010 | prose | pages [3] -->
Control # 8362 3

<!-- b000011 | heading | pages [3] -->
Executive Summary

<!-- b000012 | prose | pages [3] -->
Dear Chief of Police,

<!-- b000013 | prose | pages [3] -->
We have developed a model to help aid you in investigations regarding serial

<!-- b000014 | prose | pages [3] -->
criminals. I am writing to inform you of its functionality and what cases are most

<!-- b000015 | prose | pages [3] -->
appropriate for its uses.

<!-- b000016 | prose | pages [3] -->
Our model requires input from any member of your squad of the time and loca-

<!-- b000017 | prose | pages [3] -->
tions, in latitude and longitude, of the criminal acts you suspect were committed by

<!-- b000018 | prose | pages [3] -->
any speciﬁc criminal. It then uses the locations of these points, along with a function

<!-- b000019 | prose | pages [3] -->
modeling the drop oﬀin probability as the distance from the crime site increases, to

<!-- b000020 | prose | pages [3] -->
generate a probability distribution of the criminal’s location. Further, it creates a

<!-- b000021 | prose | pages [3] -->
probability distribution of possible future crime scenes by ﬁguring out which point

<!-- b000022 | prose | pages [3] -->
would be least surprising in future probability distribution calculations. Overall, it

<!-- b000023 | prose | pages [3] -->
tends to guess the locations relatively accurately, especially when it comes to future

<!-- b000024 | prose | pages [3] -->
crimes.

<!-- b000025 | prose | pages [3] -->
Unfortunately, our model is not a godsend. It assumes that all input on a given

<!-- b000026 | prose | pages [3] -->
run is for a single criminal, even though its inherent clustering could provide relevant

<!-- b000027 | prose | pages [3] -->
data in the case of multiple criminals. Similarly, we assume that the killer has just

<!-- b000028 | prose | pages [3] -->
one base location from which he or she operates. Our model does not work well for

<!-- b000029 | prose | pages [3] -->
commuter criminals, or those driving long distances in order to commit crimes.

<!-- b000030 | prose | pages [3] -->
Additionally, it relies on the hypothesis that the probability of the criminal’s

<!-- b000031 | prose | pages [3] -->
base being at a given location decreases as you move away from the crime scenes.

<!-- b000032 | prose | pages [3] -->
Furthermore, the model ignores any variations in terrain and in population density,

<!-- b000033 | prose | pages [3] -->
instead assuming that they are both homogeneous.

<!-- b000034 | prose | pages [3] -->
Despite these obvious drawbacks, our model does have many strengths. In addi-

<!-- b000035 | prose | pages [4] -->
Control # 8362 4

<!-- b000036 | prose | pages [4] -->
tion to the aforementioned ability to correctly handle clusters of points, it also gives

<!-- b000037 | prose | pages [4] -->
a very well speciﬁed and intuitive suggested search order, helping police minimize

<!-- b000038 | prose | pages [4] -->
time spent searching for the killer. By abstracting its calculation mechanism, our

<!-- b000039 | prose | pages [4] -->
model is ﬂexible enough to allow your department to select the most appropriate of

<!-- b000040 | prose | pages [4] -->
many possible ”submodels” for your speciﬁc case. Thus, your department need not

<!-- b000041 | prose | pages [4] -->
group bank robbers and rapists in the same category: if the two criminal groups tend

<!-- b000042 | prose | pages [4] -->
to have diﬀerent criminal patterns, our model allows for your department to use the

<!-- b000043 | prose | pages [4] -->
techniques you ﬁnd most appropriate.

<!-- b000044 | prose | pages [4] -->
Furthermore, our model is relatively eﬃcient. Despite a mediocre ”classical” run-

<!-- b000045 | prose | pages [4] -->
ning time, the extremely parallelizable nature of our algorithm allows for many com-

<!-- b000046 | prose | pages [4] -->
puters to work on the problem in parallel. With only a small number of machines, our

<!-- b000047 | prose | pages [4] -->
model can complete extremely detailed (one million point) calculations in 4 hours,

<!-- b000048 | prose | pages [4] -->
and ten thousand point calculations (which is still suﬃcient detail for most cases) in

<!-- b000049 | prose | pages [4] -->
a couple of seconds. Thus, your department need not worry about waiting days or

<!-- b000050 | prose | pages [4] -->
weeks for results to come in, saving invaluable time.

<!-- b000051 | prose | pages [4] -->
Our model’s output consists of two maps: one with the probability distribution

<!-- b000052 | prose | pages [4] -->
of the criminal’s location and one with the prediction of the location of his/her next

<!-- b000053 | prose | pages [4] -->
crime. The probabilities are displayed in bands of color: a red band represents an

<!-- b000054 | prose | pages [4] -->
area of high priority and a blue band represents one of low priority. In the case of

<!-- b000055 | prose | pages [4] -->
attempting to locate the criminal, we suggest searching the red areas ﬁrst. In the case

<!-- b000056 | prose | pages [4] -->
of trying to prevent a future crime, we suggest spreading as many oﬃcers as possible

<!-- b000057 | prose | pages [4] -->
in the red and yellow bands, as these regions are likely to contain the criminal’s next

<!-- b000058 | prose | pages [4] -->
target.

<!-- b000059 | prose | pages [4] -->
We wish you luck in your investigations.

<!-- b000060 | prose | pages [5] -->
Control # 8362

<!-- b000061 | heading | pages [5] -->
Contents

<!-- b000062 | contents | pages [5] -->
1

<!-- b000063 | heading | pages [5] -->
Background

<!-- b000064 | prose | pages [5] -->
5

<!-- b000065 | prose | pages [5] -->
6 Biography of the Typical Serial Killer . . . . . . . . . . . . . . . . . . 1.1 6 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 Locating a Killer

<!-- b000066 | prose | pages [5] -->
2 The Problem

<!-- b000067 | prose | pages [5] -->
3

<!-- b000068 | heading | pages [5] -->
Assumptions

<!-- b000069 | prose | pages [5] -->
4 Metrics and Functions

<!-- b000070 | prose | pages [5] -->
6

<!-- b000071 | prose | pages [5] -->
7

<!-- b000072 | prose | pages [5] -->
7

<!-- b000073 | prose | pages [5] -->
8 Simple Spatial Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 8 Simple Cases and Their Spacial Metrics . . . . . . . . . . . . . . . . . 4.2 9 . . . . . . . . . . . . . . . . . . . . . . . . 4.3 Distance Decay Functions

<!-- b000074 | prose | pages [5] -->
5 Our Approach

<!-- b000075 | prose | pages [5] -->
10

<!-- b000076 | prose | pages [5] -->
12 . . . . . . . . . . . . . . . . . . . . . . 5.1 Predicting Criminal Location 12 . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1.1 Computation 14 Pseudocode . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1.2 14 Why it Works . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1.3 15 Predicting Location of the Next Crime . . . . . . . . . . . . . . . . . 5.2 16 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2.1 Method 16 Edge Behavior . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2.2 16 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2.3 Complexity 16 Predicting Time of Future Crimes . . . . . . . . . . . . . . . . . . . . 5.3 18 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.3.1 Method 18 Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.3.2 19 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.4 Time Coupling 19 Why It Helps . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.4.1

<!-- b000077 | prose | pages [5] -->
6

<!-- b000078 | heading | pages [5] -->
Result Discussion

<!-- b000079 | prose | pages [5] -->
21

<!-- b000080 | prose | pages [5] -->
23 Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 23 Procedure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2

<!-- b000081 | prose | pages [5] -->
7

<!-- b000082 | heading | pages [5] -->
Conclusion

<!-- b000083 | prose | pages [5] -->
8 Future Research

<!-- b000084 | prose | pages [5] -->
24

<!-- b000085 | prose | pages [5] -->
25

<!-- b000086 | prose | pages [5] -->
26 Incorporating Statistics and Landscapes 8.1

<!-- b000087 | heading | pages [5] -->
Appendix A

<!-- b000088 | prose | pages [5] -->
. . . . . . . . . . . . . . . .

<!-- b000089 | prose | pages [5] -->
26

<!-- b000090 | prose | pages [5] -->
27

<!-- b000091 | prose | pages [6] -->
Control # 8362 6

<!-- b000092 | prose | pages [6] -->
1

<!-- b000093 | heading | pages [6] -->
Background

<!-- b000094 | prose | pages [6] -->
We attempt, in this paper, to present models and future research avenues to fur- ther the eﬀectiveness of geographic proﬁling in locating serial criminals and their future crimes. Motivation for modeling includes the fact that humans are aﬀected by “prior expectations, overconﬁdence, information retrieval, and information process- ing” (Snook et al., 2004) whereas computer simulations remain unbiased and make predictions based on discrete data. While the category of serial criminals includes rapists, killers, robbers and burglars, we speciﬁcally focus our research on the ef- fort of capturing and inhibiting the crimes of serial killers. We will also discuss the applications of our research, in our ﬁnal discussion, to other types of serial criminals.

<!-- b000095 | prose | pages [6] -->
1.1 Biography of the Typical Serial Killer

<!-- b000096 | prose | pages [6] -->
When considering serial killers, we will conform to the norm set to us in previous literature (Arndt et al., 2004):

<!-- b000097 | prose | pages [6] -->
• Must have killed a minimum of three. • Must include a cooling-oﬀtime between killings, to distinguish from mass and spree killers.

<!-- b000098 | prose | pages [6] -->
We do not consider mass murderers because they are generally classiﬁed as killing many people in a short period of time, making future crimes unlikely and capture of them relatively easier. Spree killers kill few within a short period of time; although our model may very well apply to them, they may not kill again or may reveal themselves more readily. Serial killers are distinct from these other two categories in that they typically have a deﬁned psychological purpose for killing and have spread-out killings, providing the police with more suﬃcient time to assemble a search.

<!-- b000099 | prose | pages [6] -->
Usually traumatized during childhood, repercussions of abuse and homicide be- ginning for the average serial killer at age 27.5 (Hickey, 2002). Many have precursors to killings, including robberies or sexual abuse. This is based on Hickey’s Trauma Control Model of the Serial Killer and seems to be supported statistically; most no- ticeably, 84% admitted to assaults on adults during adolescence (Arndt et al., 2004). When a serial killer does begin his homicidal campaign, each killing leads to more habituation and tolerance to the hormones and relief provided which do not fully alle- viate the cravings, leading to decreased period between killings and a cyclical process (Arndt et al., 2004). The career length of a speciﬁc serial killer varies, ranging from around 1 to 5 years, although many may enter prison on other accounts during such a career. The number of killings also varies drastically, as with their IQ.

<!-- b000100 | prose | pages [6] -->
1.2 Locating a Killer

<!-- b000101 | prose | pages [6] -->
To account for all factors aﬀecting speciﬁc killing sites and travel distances would be impossible, as the human decision process is dynamic and virtually boundless.

<!-- b000102 | prose | pages [7] -->
Control # 8362 7

<!-- b000103 | prose | pages [7] -->
As reported by Laukkanen and Santtila, however, “87% of serial rapists in the UK committed their crimes conﬁrming the so-called circle hypothesis.” This technique predicts that the criminal will live within a circle drawn around the two crime loca- tions furthest from each other. Because diﬃcult-to-solve rapes and homicides tend to occur within similar distances from the perpetrator’s residence (Santtila et al., 2007), we assume that similarly most serial murders occur within the circle.

<!-- b000104 | prose | pages [7] -->
Most serial killers and other types of criminals are also shown to not travel far from their base location, with crimes committed dropping as a function of distance (Santtila et al., 2007) - a theory we will refer to by its common name as distance decay. Surround the crime scenes, there also usually exists a buﬀer zone in which the criminal is not likely to live when avoiding detection.

<!-- b000105 | prose | pages [7] -->
2 The Problem

<!-- b000106 | prose | pages [7] -->
As contracted by the police, we are given crime scene locations and times of a speciﬁc criminal. Based on this data, we must predict the criminal’s base location and their next crime’s location and time.

<!-- b000107 | prose | pages [7] -->
Although humans may appear random, we must ﬁt a geographical proﬁle to the crime scene data for prediction purposes in a way such that our model can be used for any type of serial criminal with any personality type. This geographical proﬁle generates a prioritized search for the police. In our plots, note that red speciﬁes high search priority and blue low. We use bilinear interpolation to smooth the grid for ease of interpretation for the police.

<!-- b000108 | prose | pages [7] -->
3

<!-- b000109 | heading | pages [7] -->
Assumptions

<!-- b000110 | prose | pages [7] -->
As given such location and time data from the police, we assume that the police suspect all points used in a single run of our model are crime sites from a single criminal. We also assume, to simplify locating the criminal, that the speciﬁed killer has precisely one home base which we are trying to ﬁnd.

<!-- b000111 | prose | pages [7] -->
To simplify the problem, we assume we are dealing with serial killers. Although this does not seriously aﬀect our results in any way (Laukkanen & Santtila, 2006; Santtila et al., 2007), we use case studies and research to support location statistics for serial killers and later extend our model results to other types of serial criminals. Also, despite the fact that diﬀerent criminal personalities will commit crimes at dif- ferent distances, we assume a form of the circle theory. Research states that 87% of serial rapists, which can be extended to other types of serial criminals, reside within a circle proposed by the circle hypothesis (see Background - Locating a Criminal) (Santtila et al., 2007); we assume our grid, although not necessarily encompassing the full circle around the furthest two points, will act similarly in encompassing our killer’s location for ease of modeling purposes. We also assume a distance decay, as

<!-- b000112 | prose | pages [8] -->
Control # 8362 8

<!-- b000113 | prose | pages [8] -->
supported by research for typical stable criminals. Thus, we currently do not con- sider commuters who may travel far distances to commit crimes, though in the future we would like to include an option for diﬀerent personality traits to compensate for distance preferences and account for such commuter criminals. We do not inherently assume a buﬀer zone, as will be later discussed, but instead test diﬀerent models and see the accuracy of such an assumption.

<!-- b000114 | prose | pages [8] -->
Some factors which may aﬀect a criminal’s choice of crime site include population density, opportunity, and landscape. In our model, we neglect these diﬀerences and assume a homogeneous geographical area for simplicity. If actually implemented, we would like to include these descriptors in our model, similar to CrimeStat (Levine, 2006). Thus, unfortunately our model may predict the criminal’s base location to be in an inhabitable area and may predict future crimes to be committed where there is, in actuality, little opportunity for such crimes.

<!-- b000115 | prose | pages [8] -->
For more discussion on our future extensions to dispose of such simplifying as- sumptions, see Future Research.

<!-- b000116 | prose | pages [8] -->
4 Metrics and Functions

<!-- b000117 | prose | pages [8] -->
4.1 Simple Spatial Metrics

<!-- b000118 | prose | pages [8] -->
When assuming we are given information including locations of N crime scenes, it is useful to look at spatial metrics to help deﬁne global traits of the locations. We deﬁne the following metrics:

<!-- b000119 | prose | pages [8] -->
Mean Center (“Center of Mass”)

<!-- b000120 | prose | pages [8] -->
This is the point output when taking the average values of latitudes (y) and longitudes (x):

<!-- b000121 | prose | pages [8] -->
N X

<!-- b000122 | prose | pages [8] -->
N X

<!-- b000123 | prose | pages [8] -->
wixi, cy =

<!-- b000124 | prose | pages [8] -->
cx =

<!-- b000125 | prose | pages [8] -->
i=1

<!-- b000126 | prose | pages [8] -->
wiyi .

<!-- b000127 | prose | pages [8] -->
i=1

<!-- b000128 | prose | pages [8] -->
It is possible to include a weight, wi, for each point to skew the center more toward it, which may be useful when speciﬁc points are more important than others.

<!-- b000129 | prose | pages [8] -->
Center of Minimum Distance

<!-- b000130 | prose | pages [8] -->
This is the point where the summed distances to all of the crime scenes is minimal, or the minimum considering every (x, y) point of

<!-- b000131 | prose | pages [8] -->
N

<!-- b000132 | prose | pages [8] -->
q

<!-- b000133 | prose | pages [8] -->
(xi −x)2 + (yi −y)2

<!-- b000134 | prose | pages [8] -->
X

<!-- b000135 | prose | pages [8] -->
i=1

<!-- b000136 | prose | pages [8] -->
.

<!-- b000137 | prose | pages [9] -->
Control # 8362 9

<!-- b000138 | prose | pages [9] -->
Standard Deviational Circle (SDC)

<!-- b000139 | prose | pages [9] -->
Here, a circle is drawn at the mean center, assuming wi = 1, such that the radius is one “standard distance” (related to standard deviation) to cover 68% of the data points (assuming randomness) and 95% for a radius of two standard distances. The larger the radius, the more spread out the data is considered to be.

<!-- b000140 | prose | pages [9] -->
Standard Deviational Ellipse (SDE)

<!-- b000141 | prose | pages [9] -->
While the standard deviational circle ignores skew of the data, the ellipse allows stretching in two dimensions along any two perpendicular lines on our plane.

<!-- b000142 | prose | pages [9] -->
4.2 Simple Cases and Their Spacial Metrics

<!-- b000143 | prose | pages [9] -->
In order to gather intuition about what we would expect from a model given crime sites, we illustrate a few simple examples of possible killing distributions with expec- tations of where we would like to see predictions of home bases and future killings.1

<!-- b000144 | prose | pages [9] -->
We analyze some simple spatial statistics for each basic case: mean center (“center of mass”) and standard deviational circle.

<!-- b000145 | prose | pages [9] -->
Uniform Spread

<!-- b000146 | prose | pages [9] -->
First, we look at a uniform distribution of killings within some shape - a square, speciﬁcally, for its ease of modeling on a grid. While we might expect the killer to live anywhere in the boundary of this square, it would not be surprising if the killer lived directly in the center for the comparative ease of travel to all points on the square. For future killings, it may be diﬃcult to discern a speciﬁc location as the spread is homogeneous.

<!-- b000147 | prose | pages [9] -->
The center of mass is directly in the center, as expected. The SDCs are eﬃcient in grouping the data, meaning that our data is not very spread out.

<!-- b000148 | prose | pages [9] -->
Outline Spread

<!-- b000149 | prose | pages [9] -->
Here we consider killings along the edges of a square. It is not clear where the killer may live, as this killing trail may be part of his daily route or he may live closer to the center for ease of travel, but we would expect future killings to happen also along the boundary.

<!-- b000150 | prose | pages [9] -->
1These models were designed for their intuitive simplicity and to test the accuracy of our models later.

<!-- b000151 | prose | pages [10] -->
Control # 8362 10

<!-- b000152 | prose | pages [10] -->
Our mean center is again in the center, but our SDCs are very large, indicating that the data is very spread out from the mean center.

<!-- b000153 | prose | pages [10] -->
Linear Spread

<!-- b000154 | prose | pages [10] -->
Here, we look at a linear killing distribution. While the future killings may depend on the times of each crime committed, speciﬁcally in this example, if we assume the times are irrelevant then we may expect the killer to live near at least a few of the points.

<!-- b000155 | prose | pages [10] -->
Again, our mean center is in the middle and our SDCs are very large, as the points are spread far from the center. The SDE may be more eﬀective in analyzing this case as there is no spread in latitude.

<!-- b000156 | prose | pages [10] -->
Clustering

<!-- b000157 | prose | pages [10] -->
This clustering example may be most prevalent when considering a killer with two main base locations (for example, one who lives in one city and works in an- other). It again may not be clear where the killer lives, but we should predict killings to occur within the two clusters.

<!-- b000158 | prose | pages [10] -->
Again, we have a large SDC. These may indicate that when looking for next killer location, it may be beneﬁcial to look at SDC radii and SDEs.

<!-- b000159 | prose | pages [10] -->
4.3 Distance Decay Functions

<!-- b000160 | prose | pages [10] -->
When calculating probability distributions, we test diﬀerent distance decay functions. Recall that the theory of distance decay assumes drop-oﬀof likelihood of our killer living at any given location as distance from crime scenes increase (see Figure 1). We consider Linear, Normal, Negative Exponential, Truncated Negative Exponential, and Plateaued Negative Exponential drop-oﬀs.

<!-- b000161 | prose | pages [10] -->
Of particular distinction between these are their behaviors directly surrounding the crime scenes and the rates of decay with increased distance.

<!-- b000162 | prose | pages [10] -->
Linear

<!-- b000163 | prose | pages [10] -->
With this model, we assume a linear drop-oﬀrate of the form:

<!-- b000164 | prose | pages [10] -->
 a −bx if x ≤a/b

<!-- b000165 | prose | pages [10] -->
f(x) =

<!-- b000166 | prose | pages [10] -->
0 if x > a/b.

<!-- b000167 | prose | pages [11] -->
Control # 8362 11

<!-- b000168 | prose | pages [11] -->
Distance Decay Functions

<!-- b000169 | prose | pages [11] -->
10

<!-- b000170 | prose | pages [11] -->
9

<!-- b000171 | prose | pages [11] -->
Crime Probability (Unnormalized)

<!-- b000172 | prose | pages [11] -->
8

<!-- b000173 | prose | pages [11] -->
7

<!-- b000174 | prose | pages [11] -->
6

<!-- b000175 | prose | pages [11] -->
5

<!-- b000176 | prose | pages [11] -->
4

<!-- b000177 | prose | pages [11] -->
3

<!-- b000178 | prose | pages [11] -->
2

<!-- b000179 | prose | pages [11] -->
1

<!-- b000180 | prose | pages [11] -->
0

<!-- b000181 | furniture | pages [11] -->


<!-- b000182 | prose | pages [11] -->
0 1 2 3 4

<!-- b000183 | furniture | pages [11] -->


<!-- b000184 | prose | pages [11] -->
Linear Normal NE Truncated NE

<!-- b000185 | prose | pages [11] -->
5 6 7 8 9 10

<!-- b000186 | prose | pages [11] -->
Distance From Crime Scene

<!-- b000187 | caption | pages [11] -->
Figure 1: A decay plot.

<!-- b000188 | prose | pages [11] -->
This simple model assumes that the expected probability of ﬁnding the criminal at a given location decreases linearly with distance from the crime site until the distance is greater than a/b, after which it remains zero. Despite the simplicity of this model, its behavior is clearly somewhat unrealistic.

<!-- b000189 | prose | pages [11] -->
Normal

<!-- b000190 | prose | pages [11] -->
This model was suggested by Brantingham and Brantingham (1981) to include their hypothesized buﬀer zone. The function exponentially increases and decreases around such a radius as is maximized by the buﬀer zone:

<!-- b000191 | prose | pages [11] -->
f(x) = ae

<!-- b000192 | prose | pages [11] -->
−(x−µ)2

<!-- b000193 | prose | pages [11] -->
2σ2 √

<!-- b000194 | prose | pages [11] -->
. 2πσ

<!-- b000195 | prose | pages [11] -->
Although this does not work well with our idea of serial killers generally living close to their crime scenes, it may be useful when considering other types of serial criminals such as robbers and burglars are expected to on average live further from their crimes.

<!-- b000196 | prose | pages [11] -->
Negative Exponential

<!-- b000197 | prose | pages [11] -->
Here we assume a negative exponential drop-oﬀrate of the form:

<!-- b000198 | prose | pages [11] -->
f(x) = e−cx

<!-- b000199 | prose | pages [11] -->
where f(0)=1 is the maximum value. Thus, this function assumes that the proba- bility of killer location is highest at the speciﬁc crime scenes from which it decays

<!-- b000200 | prose | pages [12] -->
Control # 8362 12

<!-- b000201 | prose | pages [12] -->
exponentially. Although this contradicts our idea of a “buﬀer zone“, presented by Brantingham & Brantingham (1981), this model is shown to work well in its predic- tions. According to Rhodes, it showed a much better than the Normal curve ﬁt when compared with actual serial burglar, robber, and rapist locations versus their crimes (Rhodes & Conly, 1981; Kent, 2003).

<!-- b000202 | prose | pages [12] -->
Truncated Negative Exponential

<!-- b000203 | prose | pages [12] -->
Here we assume a linear growth from each crime scene to a certain point where the probability is maximal and then drops exponentially:

<!-- b000204 | prose | pages [12] -->
 1 + b(x −x0)

<!-- b000205 | prose | pages [12] -->
f(x) =

<!-- b000206 | prose | pages [12] -->
e−c(x−x0) if x ≤x0 if x > x0.

<!-- b000207 | prose | pages [12] -->
This does support the idea of a buﬀer zone and has a quick drop-oﬀafter some maximal distance. In this model, we are able to specify the parameters b, c, and x0 which may help when considering diﬀerent types of criminals and their average found distance from crime scenes, or when considering diﬀerent social proﬁles of criminals and the eﬀects of such on distance.

<!-- b000208 | prose | pages [12] -->
Plateaued Negative Exponential

<!-- b000209 | prose | pages [12] -->
A special case of the truncated negative exponential occurs when we let b = 0. Instead of the usual rise-and-fall, the function stays level when x ≤x0 and from there drops oﬀlike a regular negative exponential. The function takes the form

<!-- b000210 | prose | pages [12] -->
 1

<!-- b000211 | prose | pages [12] -->
f(x) =

<!-- b000212 | prose | pages [12] -->
if x ≤x0 e−c(x−x0) if x > x0.

<!-- b000213 | prose | pages [12] -->
This supports the idea that, although there exists a buﬀer zone around the crime scenes where the killer is less likely to live, the area spanned when moving outwards from the crime scene squares and so it is innate in the spread from the crime scene that the probability is higher as distance increases when maintaining a constant probability at each grid point. It considers that the buﬀer zone is not derived from criminals preferring crimes past a certain distance but rather that opportunities increase with distance since the area increases.

<!-- b000214 | prose | pages [12] -->
5 Our Approach

<!-- b000215 | prose | pages [12] -->
Predicting Criminal Location 5.1

<!-- b000216 | prose | pages [12] -->
To predict the criminal’s location, we employ a strategy that, while similar in some superﬁcial ways, greatly generalizes the strategy of locating the criminal by investi- gating the center of mass. Whereas the center of mass approach returns a single point

<!-- b000217 | prose | pages [13] -->
Control # 8362 13

<!-- b000218 | prose | pages [13] -->
(around which one can center a Gaussian distribution, for instance), our method at- tempts to utilize the locations of the criminal acts to the fullest by instead generating a distribution, assigning each point within the given region a probability. These prob- abilities returned can in turn be used to generate a map, showing which locations the algorithm considers to be of high interest and which can probably be ignored. By transforming the set of crime data points into a specially-constructed distribution rather than a handful of values, our algorithm allows for much more specialized, and in many cases much more accurate, results.

<!-- b000219 | prose | pages [13] -->
The main idea driving the algorithm is the idea that any point p can be assigned a relative “criminal location probability” by taking the sum of some function (men- tioned in Metrics and Functions) of the distances between p and prior incidents. It might help to imagine this as the sum of non-canceling “gravitational pulls” of the various locations: any point with a comparatively high total gravitational pull is going to be near many of the crime scenes, and therefore should rightly be assigned a high criminal location probability. Furthermore, the actual strengths of the pulls from each point can be weighted depending on its recency, allowing for the algorithm to more quickly adapt to the changing habits of the criminal. We will currently treat all weights as equal to one, but we will discuss weighting in more detail in Time Coupling.

<!-- b000220 | caption | pages [13] -->
Figure 2: Example of a probability distribution. Red star signiﬁes actual criminal’s base.

<!-- b000221 | prose | pages [14] -->
Control # 8362 14

<!-- b000222 | prose | pages [14] -->
5.1.1 Computation

<!-- b000223 | prose | pages [14] -->
As it is infeasible to calculate the value at every single point and extremely diﬃcult to model analytically, our algorithm instead discretizes the problem by transforming the candidate search area into a grid and calculating the criminal location probability at each grid point. When increasing the ﬁneness of the grid, which is allowed for in the input to our model, our algorithm better approximates the ideal, smooth, solution. Because the algorithm makes l calculations of f per grid point, it has O(nml) runtime where n is the number of lines on the grid parallel to the Prime Meridian, m is the number of lines parallel to the equator, and l is the number of unlawful acts perpetrated by the criminal. As l is generally relatively small and, at least in our simulations, we often set m and n to be equal, this algorithm can essentially be considered to be O(n2), which is going to be very fast for any reasonable mesh size — consider that a single 2GHz machine can use this algorithm to partition an area the size of England into 36 × 36 meter blocks and create a corresponding probability distribution using some interesting distance functions in only a matter of minutes!

<!-- b000224 | prose | pages [14] -->
5.1.2 Pseudocode

<!-- b000225 | prose | pages [14] -->
To clear up any ambiguities, we provide some pseudocode below for the criminal- ﬁnding function.

<!-- b000226 | heading | pages [14] -->
Program 1 Criminal Location Finding Algorithm

<!-- b000227 | prose | pages [14] -->
1 G is the set of grid points after the search area is partitioned by the mesh 1 C is the set of past crimes, each of which has a location and date 1 f(d) is the distance decay function which returns a higher number for more probable locations 1 Prob is the probability of the killer location based on distance decay aﬀects for the grid

<!-- b000228 | heading | pages [14] -->
1 Function criminalLocationProb (crimes C, function f):

<!-- b000229 | prose | pages [14] -->
Let Prob be a mapping from G into R 1 1 for g ∈G do 1 1 /*Calculate cumulative distance eﬀect from all c ∈C*/ 1 1 1 1 1 1 Prob[g] = 0 for c ∈C do 1 1 1 1 1 1 1 Prob[g] = Prob[g] + f(distance between c and g) 1 1 Normalize the values of Prob so that the sum of the values is 1 1 1 return Prob

<!-- b000230 | prose | pages [15] -->
Control # 8362 15

<!-- b000231 | prose | pages [15] -->
5.1.3 Why it Works

<!-- b000232 | prose | pages [15] -->
Our algorithm has many properties that lead to the generation of useful results.

<!-- b000233 | prose | pages [15] -->
Prioritized Search

<!-- b000234 | prose | pages [15] -->
The probability distribution that our algorithm returns lends to a very simple algo- rithm for determining in what order to search various locations for the criminal. One can simply search the possible locations in descending order of their probabilities! This simple strategy often leads to good results, requiring us to go through about 15% of a certain search area to ﬁnd Peter Sutcliﬀe, one of our case study serial killers, for most distance decay functions.

<!-- b000235 | prose | pages [15] -->
Point Clustering

<!-- b000236 | prose | pages [15] -->
One of the nicest features of our algo- rithm is its handling of point clusters without any outside assistance.

<!-- b000237 | prose | pages [15] -->
Be- cause all crime scenes exert a “gravi- tational pull,” points near any crime scenes will have a probability boost and will create localized “hot-spots” where the algorithm thinks the crimi- nal has some reasonable chance of be- ing caught.

<!-- b000238 | prose | pages [15] -->
This eﬀect can be seen on the ﬁgure on the left/right, in which two diﬀerent clumps form two hotspots, with their relative sizes and magnitudes proportional to the number of points inside.

<!-- b000239 | prose | pages [15] -->
Function/Parameter Independence

<!-- b000240 | prose | pages [15] -->
Another major strength of our algorithm is its generality. Because the function works on any reasonable arbitrary function with arbitrary parameters, the police can hand- pick the functions based on statistics and their historical successes in catching the perpetrators of various types of crimes. For example, because burglars and serial killers generally exhibit diﬀerent behaviors in selecting how far they are willing to travel to commit their crime, it could be that a normal distance decay function would be superior for catching burglars whereas a negative exponential distance decay function could be superior for catching serial killers. As our algorithm is extremely ﬂexible, the police can quickly and easily adapt their search techniques to best match the criminal in question.

<!-- b000241 | prose | pages [16] -->
Control # 8362 16

<!-- b000242 | prose | pages [16] -->
5.2 Predicting Location of the Next Crime

<!-- b000243 | prose | pages [16] -->
5.2.1 Method

<!-- b000244 | prose | pages [16] -->
In order to ﬁnd the location of the next crime, we look for the point on the grid which most closely matches the pattern of the other crimes. If we consider the criminal location probability distribution produced after adding a crime event to our grid, the most probable location for the next crime would be the spot which generates a distribution most similar to the one produced before adding it. This gives us the most likely location for a future crime. Furthermore, for potential crime scenes other than the most probable, we estimate how much worse they are by measuring how much the produced distribution deviates from the original. This gives us a distribution over our search area which can be used to allocate resources for crime prevention.

<!-- b000245 | prose | pages [16] -->
Our algorithm works as follows: First we compute the criminal location proba- bility distribution for the search area. Next we iterate through all of the grid points in the search area, adding a new ”virtual crime scene” at each point, calculating the new criminal location probability distribution with the additional crime scene. We then compare each of these distributions to the original one by summing the squares of the diﬀerences between corresponding grid points, then assigning this pseudo prob- ability deviation number to the location of the ”virtual crime scene.” This gives us a distribution over the search area, where lower numbers mean the point is a more likely spot for the criminal’s next crime because adding this point as a crime location deviates less from the original probability distribution.

<!-- b000246 | prose | pages [16] -->
5.2.2 Edge Behavior

<!-- b000247 | prose | pages [16] -->
If all of the points on the mesh are tested as possible crime scenes, then there is a tendency for points near the edge to be rated higher than appropriate. This is because a point near the edge has fewer other points around it, so when a crime scene is added there it is eﬀecting the criminal location probability distribution of fewer points, and thus has a smaller total eﬀect on the produced distribution. To compensate for this, we add a buﬀer zone around our search area where the criminal location probability distribution is calculated but no crime scenes are added. This eﬀectively removes the bad edge behavior.

<!-- b000248 | prose | pages [16] -->
5.2.3 Complexity

<!-- b000249 | prose | pages [16] -->
When adding each point as a virtual crime scene, we must calculate a diﬀerent crimi- nal location probability distribution for every point in our search area, thus requiring approximately n2 operations, each of which is O(n2) (see Predicting Criminal Loca- tion - Computation). Therefore the algorithm for determining the location of the next crime has a complexity of O(n4). This is a polynomial time algorithm, but it can still become very slow as n increases. To keep our calculation time from getting out of control, we implement various optimizations.

<!-- b000250 | prose | pages [17] -->
Control # 8362 17

<!-- b000251 | heading | pages [17] -->
Program 2 The killer-ﬁnding and future-predicting algorithm

<!-- b000252 | prose | pages [17] -->
1 G is the set of grid points after the search area is partitioned by the mesh 1 G′ is G augmented with a 40% boundary buﬀer zone 1 C is the set of past crimes, each of which has a location and date 1 f(d) is the distance decay function which returns a higher number for more probable locations 1 Prob is the probability of the killer location based on distance decay aﬀects for the grid 1 ∆Prob measures the change in distribution of Prob when adding a new crime scene

<!-- b000253 | heading | pages [17] -->
1 Function criminalLocationProb (crimes C, function f):

<!-- b000254 | prose | pages [17] -->
Let Prob be a mapping from G′ into R 1 1 for g ∈G′ do 1 1 /*Calculate cumulative distance aﬀect from all c ∈C*/ 1 1 1 1 1 1 Prob[g] = 0 for c ∈C do 1 1 1 1 1 1 1 Prob[g] = Prob[g] + f(distance between c and g) 1 1 Normalize the values of Prob so that the sum of the values is 1 1 1 return Prob

<!-- b000255 | heading | pages [17] -->
1 Function nextCrimeProb (crimes C, function f):

<!-- b000256 | prose | pages [17] -->
1 1 killer prob distrib = criminalLocationProb(C,f) Let ∆Prob be a mapping from G′ into R 1 1 for g ∈G′ do 1 1 Let C′ be C augmented with a “virtual crime” at g 1 1 1 V = criminalLocationProb(C′,f) 1 1 1 1 1 1 /*Calculate sum of squared diﬀerences between killer prob distrib and V */ 1 1 1 ∆Prob[g] = 0 for h ∈G′ do 1 1 1 ∆Prob[g] = ∆Prob[g] + (V[h] −killer prob distrib[h])2 1 1 1 1

<!-- b000257 | prose | pages [17] -->
1 1 Normalize the values of ∆Prob so that the sum of the values is 1 1 1 return ∆Prob

<!-- b000258 | prose | pages [18] -->
Control # 8362 18

<!-- b000259 | prose | pages [18] -->
(a) No buﬀer.

<!-- b000260 | prose | pages [18] -->
(b) 30% buﬀer.

<!-- b000261 | caption | pages [18] -->
Figure 3: Varying buﬀer percentages to illustrate boundary conditions.

<!-- b000262 | prose | pages [18] -->
The single most important optimization implemented in our algorithm is caching. Suppose our search area has N crime scenes. For each point on the mesh we add a virtual crime scene and then calculate the criminal location probability distribution over the search area using the N + 1 points. When calculating the new probability distribution with N +1 points, instead of doing the full calculation, we use the original distribution for the ﬁrst N points and combine it with a distribution for only the new point in a way that maintains normalization. This gives the algorithm a factor of N speedup.

<!-- b000263 | prose | pages [18] -->
Our algorithm is also nearly perfectly parallelizable. By multi-threading the code, it can be run over a number of cores with a speedup equal to the number of cores used. This makes running very high resolution calculations practical if a multicore or computing cluster is available.

<!-- b000264 | prose | pages [18] -->
5.3 Predicting Time of Future Crimes

<!-- b000265 | prose | pages [18] -->
5.3.1 Method

<!-- b000266 | prose | pages [18] -->
When considering a serial killer’s next time or date of killing, we look at a basic lin- ear regression model. We ﬁnd the average time between killings to predict the next killing from the last. To test our model, we remove the last point from the N killing times which we attempt to predict using our regression:

<!-- b000267 | prose | pages [19] -->
Control # 8362

<!-- b000268 | prose | pages [19] -->
tN = tN−1 + tN−1 −t1

<!-- b000269 | prose | pages [19] -->
. N −1

<!-- b000270 | prose | pages [19] -->
5.3.2 Motivation

<!-- b000271 | prose | pages [19] -->
Although a linear regression may not be realistic for every killer, it applies more generally to all as some may in-

<!-- b000272 | prose | pages [19] -->
Chester Turner 14

<!-- b000273 | prose | pages [19] -->
19

<!-- b000274 | prose | pages [19] -->
12

<!-- b000275 | prose | pages [19] -->
10

<!-- b000276 | prose | pages [19] -->
Kill Number

<!-- b000277 | prose | pages [19] -->
8

<!-- b000278 | prose | pages [19] -->
6

<!-- b000279 | prose | pages [19] -->
4

<!-- b000280 | prose | pages [19] -->
2

<!-- b000281 | prose | pages [19] -->
0 1986 1988 1990 1992 1994 1996 1998 2000

<!-- b000282 | caption | pages [19] -->
Figure 4: Predicted Nth crime in red; actual

<!-- b000283 | prose | pages [19] -->
crease their frequency of killings as ha-

<!-- b000284 | prose | pages [19] -->
Nth crime in black.

<!-- b000285 | prose | pages [19] -->
bituation sets in and some may de- crease their frequency. Hypothesized by Hickey’s Trauma Control Model and veriﬁed by Arndt’s analysis of Newton’s Hunting Humans which is a collection of data of serial killers, the killing rate of serial killers generally increases with time; however, there are many sources which state that the killing rate may also decrease in some cases (Arndt et al., 2004). Because other interpolation techniques such as exponential or quadratic may greatly over-predict future crimes because of strong end-behavior, we choose to use the linear regression for its simplicity and universal niceness.

<!-- b000286 | prose | pages [19] -->
5.4 Time Coupling

<!-- b000287 | prose | pages [19] -->
Having developed methods for predicting both the criminal location and where the next crime will occur, we now extend these methods by adding in the concept of time. As described so far, the algorithm neglects all chronological properties of the killings, discarding one of the most important pieces of information available to us. Ideally, we want to be able to quickly adapt to the criminal’s motion if they were to move to a diﬀerent location or otherwise alter behavior over time.

<!-- b000288 | prose | pages [19] -->
To account for these possible changes, we weight events more heavily the more recently they occurred. Doing this allows for recent changes in behavior to be more strongly reﬂected in future predictions, which allows for better calibration with the criminal’s latest motives. To keep the algorithm as general as before, we will modify the algorithm to take a weighting function as an input, which is then multiplied by f(dist) when we calculate Prob[g].

<!-- b000289 | prose | pages [19] -->
Although the composition of the weighting function w can be anything, we notice that

<!-- b000290 | prose | pages [19] -->
w(t) = (d −c)a √

<!-- b000291 | prose | pages [19] -->
t + a + c

<!-- b000292 | prose | pages [19] -->
yields reasonable results. Due to time constraints, this w was the only reasonable weighting function which we managed to study in depth, and therefore any future

<!-- b000293 | prose | pages [20] -->
Control # 8362 20

<!-- b000294 | heading | pages [20] -->
Program 3 The killer-ﬁnding and future-predicting algorithm with time-based

<!-- b000295 | prose | pages [20] -->
weighting 1 G is the set of grid points after the search area is partitioned by the mesh 1 G′ is G augmented with a 30% boundary buﬀer zone 1 C is the set of past crimes, each of which has a location and date 1 f(d) is the distance decay function which returns a higher number for more probable locations 1 w(t) is the weight function which returns a higher number for smaller inputs

<!-- b000296 | prose | pages [20] -->
1 Prob is the probability of the killer location based on distance decay aﬀects for the grid 1 ∆Prob measures the change in distribution of Prob when adding a new crime scene

<!-- b000297 | heading | pages [20] -->
1 Function criminalLocationProb (crimes C, decay function f, weight function w):

<!-- b000298 | prose | pages [20] -->
Let Prob be a mapping from G′ into R 1 1 for g ∈G′ do 1 1 /*Calculate cumulative distance eﬀect from all c ∈C*/ 1 1 1 1 1 1 Prob[g] = 0 for c ∈C do 1 1 1 Prob[g] = Prob[g] + w(time since ctime) · f(distance between c and g) 1 1 1 1 1 1 Normalize the values of Prob so that the sum of the values is 1 1 1 return Prob

<!-- b000299 | heading | pages [20] -->
1 Function futureCrimeProb (crimes C, decay function f, weight function w):

<!-- b000300 | prose | pages [20] -->
1 1 killer prob distrib = criminalLocationProb(C,f,w) Let ∆Prob be a mapping from G′ into R 1 1

<!-- b000301 | prose | pages [20] -->
for g ∈G′ do 1 1 Let C′ be C augmented with a “virtual crime” at g 1 1 1 V = criminalLocationProb(C′,f,w) 1 1 1

<!-- b000302 | prose | pages [20] -->
1 1 1 /*Calculate sum of squared diﬀerences between killer prob distrib and V */ 1 1 1 ∆Prob[g] = 0 for h ∈G′ do 1 1 1 ∆Prob[g] = ∆Prob[g] + (V[h] −killer prob distrib[h])2 1 1 1 1

<!-- b000303 | prose | pages [20] -->
1 1 Normalize the values of ∆Prob so that the sum of the values is 1 1 1 return ∆Prob

<!-- b000304 | prose | pages [21] -->
Control # 8362 21

<!-- b000305 | prose | pages [21] -->
Weight Function

<!-- b000306 | prose | pages [21] -->
10

<!-- b000307 | prose | pages [21] -->
9

<!-- b000308 | prose | pages [21] -->
8

<!-- b000309 | prose | pages [21] -->
7

<!-- b000310 | prose | pages [21] -->
Weight

<!-- b000311 | prose | pages [21] -->
6

<!-- b000312 | prose | pages [21] -->
5

<!-- b000313 | prose | pages [21] -->
4

<!-- b000314 | prose | pages [21] -->
3

<!-- b000315 | prose | pages [21] -->
2 0 20 40 60 80 100

<!-- b000316 | prose | pages [21] -->
Time (Days)

<!-- b000317 | caption | pages [21] -->
Figure 5: A decay plot.

<!-- b000318 | prose | pages [21] -->
time-based models use this w as the time weighting function.

<!-- b000319 | prose | pages [21] -->
5.4.1 Why It Helps

<!-- b000320 | prose | pages [21] -->
To help emphasize the beneﬁts of time coupling, we consider a randomly generated scenario. The points in the following graphs were automatically generated to be close- to-linear, and some randomly selected set of times generated by a Poisson process were matched to these points in one of two ways:

<!-- b000321 | prose | pages [21] -->
• In the “correlated” case, the times were chosen to increase monotonically with x. That is, the larger the value of x, the larger the time that was assigned to it.

<!-- b000322 | prose | pages [21] -->
• In the “uncorrelated” case, the various times were assigned randomly to the points.

<!-- b000323 | prose | pages [21] -->
Notice how the addition of time-based weighting in the uncorrelated case had almost no eﬀect when compared to the correlated case, in which the eﬀect of the weighting was pronounced. As there was no correlation in the former case, any small pertur- bations will essentially cancel each other out, leaving each point with no expected

<!-- b000324 | prose | pages [22] -->
Control # 8362

<!-- b000325 | prose | pages [22] -->
(a) Next Crime Probability Plot with unweighted time, uncorrelated points.

<!-- b000326 | prose | pages [22] -->
(c) Next Crime Probability Plot with unweighted time, correlated points.

<!-- b000327 | prose | pages [22] -->
22

<!-- b000328 | prose | pages [22] -->
(b) Next Crime Probability Plot with weighted time, uncorrelated points.

<!-- b000329 | prose | pages [22] -->
(d) Next Crime Probability Plot with weighted time, correlated points.

<!-- b000330 | prose | pages [23] -->
Control # 8362 23

<!-- b000331 | prose | pages [23] -->
(e) Criminal Location Probability Plot with un-

<!-- b000332 | prose | pages [23] -->
(f) Criminal Location Probability Plot with

<!-- b000333 | prose | pages [23] -->
weighted time, correlated points.

<!-- b000334 | prose | pages [23] -->
weighted time, correlated points.

<!-- b000335 | prose | pages [23] -->
change. Thus, the correctness of the plot is not drastically aﬀected, if at all. In the latter case, however, the correlation was captured by the algorithm and the expected location of the next killing shifted rather drastically to accommodate this change. Intuitively, if a serial killer has been moving north one mile every day for a while, it is reasonable to assume that his or her future kills will be more north than average.

<!-- b000336 | prose | pages [23] -->
Perhaps even more interesting, the location of the next crime adapted much more quickly than the estimated location of the criminal. Again, this is sensible: a gradual shift in the location of crimes is much more indicative of a behavior-based shift than one that is residence-based.

<!-- b000337 | prose | pages [23] -->
6

<!-- b000338 | heading | pages [23] -->
Result Discussion

<!-- b000339 | prose | pages [23] -->
To evaluate our models, including various choices for our distance decay function, we look at case study data (see Appendix A) for actual apprehended serial killers: Peter Sutcliﬀe and Chester Turner.

<!-- b000340 | prose | pages [23] -->
6.1 Metrics

<!-- b000341 | prose | pages [23] -->
We use two metrics in quantifying the quality of our results.

<!-- b000342 | prose | pages [23] -->
The ﬁrst is Error Distance and the second is Search Cost.

<!-- b000343 | prose | pages [24] -->
Control # 8362 24

<!-- b000344 | prose | pages [24] -->
Error Distance

<!-- b000345 | prose | pages [24] -->
This mesaures the distance between the calculated most probable spot and the actual spot “as the crow ﬂies”. When searching for the criminal, the error distance tells us how far away our best guess was from the actual location.

<!-- b000346 | prose | pages [24] -->
When predicting the next crime it tells us how far away the crime happened from the location where we allocated the most resources.

<!-- b000347 | prose | pages [24] -->
Search Cost

<!-- b000348 | prose | pages [24] -->
This measures how many grid squares would need to be searched out of the total before the correct spot is found if we go through the squares in the order of their probability. When searching for the criminal this tells us how much area would need to be searched to ﬁnd the criminal. We assume no preference over locations of the same color and thus this may vary in actual police searching where the initial search direction may vary. When predicting the location of the next crime it tells us what percentage of our resources were wasted on locations that had higher priority than the actual location but saw no actual crime.

<!-- b000349 | prose | pages [24] -->
This metric provides a much more realistic assessment of the quality of a prediction; however, in some instances the Error Distance still provides useful information.

<!-- b000350 | prose | pages [24] -->
6.2 Procedure

<!-- b000351 | prose | pages [24] -->
We use the model without the time-dependent weighting ﬁrst. Thus for these calcula- tions the times of the killings are irrelevant to the calculated probability distributions for the criminal’s location and the location of his next crime; however, the times are used to calculate when the next crime will occur.

<!-- b000352 | prose | pages [24] -->
We begin by removing the most recent crime from our datasets. This emulates the position the police would be in while searching for the criminal. Next we calculate the criminal location probability distribution using each of our decay functions. The quality of these calculations is assesed using both of our metrics, comparing the predicted locations to the actual known locations of the killers’ home.

<!-- b000353 | prose | pages [24] -->
Then we calculate the next crime location probability distribution for each decay function. These results are also assesed using the metrics. Finally, we repeat the calculations using the model with time dependent weights. The results is presented below. Plots can be found in the Appedix.

<!-- b000354 | prose | pages [25] -->
Control # 8362 25

<!-- b000355 | prose | pages [25] -->
Criminal Home Method Criminal Home Next Crime Next Crime Coupled Uncoupled Uncoupled Coupled

<!-- b000356 | prose | pages [25] -->
Sutcliﬀe

<!-- b000357 | prose | pages [25] -->
19.26/29.49 Linear 18.17/17.88 3.99/9.47 3.41/8.73 17.05/30.24 Neg. Exp.

<!-- b000358 | prose | pages [25] -->
15.97/30.24 0.27/1.46 0.26/1.46 15.53/24.32 Trunc. Neg. Exp.

<!-- b000359 | prose | pages [25] -->
14.44/24.32 1.98/8.00 1.65/7.28 16.33/25.07 Plateau Neg. Exp.

<!-- b000360 | prose | pages [25] -->
15.00/25.07 1.25/5.70 1.04/4.98 15.99/22.92 Normal 15.00/22.83 0.81/4.27 0.63/3.58

<!-- b000361 | prose | pages [25] -->
Chester Turner

<!-- b000362 | prose | pages [25] -->
60.12/5.92 Linear 58.64/5.52 40.90/4.12 44.46/5.10 60.79/5.07 Neg. Exp.

<!-- b000363 | prose | pages [25] -->
59.80/5.07 41.06/3.12 45.93/3.26 60.79/4.38 Trunc. Neg. Exp.

<!-- b000364 | prose | pages [25] -->
59.80/4.38 40.68/3.46 45.26/4.12 60.79/4.48 Plateau Neg. Exp.

<!-- b000365 | prose | pages [25] -->
59.80/4.48 40.79/3.26 45.58/3.46 66.70/4.46 Normal 66.04/4.46 40.83/3.26 43.38/3.46

<!-- b000366 | caption | pages [25] -->
Table 1: Search Costs / Error Distance using various functions for both the Sutcliﬀe and

<!-- b000367 | prose | pages [25] -->
Chester Turner data.

<!-- b000368 | prose | pages [25] -->
7

<!-- b000369 | heading | pages [25] -->
Conclusion

<!-- b000370 | prose | pages [25] -->
All examined distance decay functions tend to do a good job when examining ”good” data, which is data in which the next kill or killer location tends to be in the general vicinity of the killings. In the case of Peter Sutcliﬀe, our algorithm predicted Sutcliﬀe’s location rather accurately on any distance decay function and guessed the location of the next crime almost exactly in many cases.

<!-- b000371 | prose | pages [25] -->
Unfortunately, the data can be misleading. In the case of Chester Turner, who exclusively committed murders to the east of his home, the algorithm unsurprisingly failed to guess his home address accurately. This is unavoidable: there is no method (as far as we can tell) to accurately guess the killer’s “hub” location if it is suﬃciently removed from the locations of the crimes themselves.

<!-- b000372 | prose | pages [25] -->
In either case, it seems that the guessing accuracy for the next crime location is much better than that for the location of the criminal. While this result is somewhat surprising, as the guess for the next crime location is itself based on the estimated killer location, it is still possible to explain. One simple explanation which can be visually veriﬁed of this phenomenon is that killers tended to cluster their killings closely, allowing for easier guessing for the next crime. Another possible explanation is that the increased number of calculations required to generate the estimated next location resulted in signiﬁcantly smaller random ﬂuctuations, meaning that the data is “smoother” and therefore more likely to behave well.

<!-- b000373 | prose | pages [25] -->
Contrary to our expectations, the addition of time coupling generally, but not always, decreased our performance. While we don’t currently have any explanation much better than “bad luck” for this behavior, this result is something that should

<!-- b000374 | prose | pages [26] -->
Control # 8362 26

<!-- b000375 | prose | pages [26] -->
deﬁnitely be examined before serious use of this tool by the police. It seems that time coupling only gives superior performance when the spatial and temporal aspects of the previous crimes is correlated. Without time coupling, our model misses this pattern in the data, but the time coupled version ﬁnds it.

<!-- b000376 | prose | pages [26] -->
Even with the model’s ﬂaws, we believe that it can be a useful tool for any police station to employ. If the model managed to give us such accurate data for predicting the whereabouts of Sutcliﬀe’s next victim, it is not unreasonable to believe that the tool could repeat this behavior for larger datasets. With this predictive power in hand, the police can better prepare for upcoming attacks and apprehend the criminal.

<!-- b000377 | prose | pages [26] -->
8 Future Research

<!-- b000378 | prose | pages [26] -->
Incorporating Statistics and Landscapes 8.1

<!-- b000379 | prose | pages [26] -->
Although our model avoids human bias toward overconﬁdence and predisposed pre- dictions, one might argue “information that a person, animal or institution knows about a physical or social environment” (Gigerenzer & Selton, 2001, 187) gives hu- mans the beneﬁt for predicting locations; however, we would like to incorporate that information into our model: the landscape, personality proﬁle, population density. Eventually, one may be able to also specify social personality regions - for example, rich areas versus poor, known drug-traﬃcking areas, etc. We believe this augmenta- tion would not only lead to better predictions by our model but also give it a clearer advantage over human predictors. In such cases as we are considering, it is not imme- diately obvious where the serial criminal lives or will commit their next crime. Thus, we support probabilities and statistics against human bias.

<!-- b000380 | prose | pages [26] -->
Diﬀerent personality types of criminals (e.g., team killers, sexually motivated killers, burglars, etc.) also commit crimes at diﬀerent distances from their base. Team killers are less likely to kill women and live in a more geographically localized area; sexually motivated killers are more likely to use a more personal killing method, such as strangulation, and prefer strangers more, but tended to be more geographically stable as compared to non-sexually motivated killers (Arndt et al., 2004). These per- sonality inferences may be made by surveying crime scenes. In our model, therefore, we could have optional inputs for use by police to specify personality traits, which we could then use to alter our parameters automatically to predict more probable distances with more ease for the police.

<!-- b000381 | prose | pages [26] -->
Predicted Crime Serial Killer Actual Crime

<!-- b000382 | prose | pages [26] -->
09-Dec-1980 Sutcliﬀe 17-Nov-1980 30-Dec-1969 Zodiac Killer 11-Oct-1969 07-Oct-1888 Jack the Ripper 09-Nov-1888 24-Feb-2005 Grim Sleeper 01-Jan-2007 01-Jan-1999 Chester Turner 06-Apr-1998

<!-- b000383 | prose | pages [27] -->
Control # 8362

<!-- b000384 | heading | pages [27] -->
Appendix A

<!-- b000385 | prose | pages [27] -->
Serial Killer Case Study Data

<!-- b000386 | prose | pages [27] -->
Serial Killer Latitude

<!-- b000387 | prose | pages [27] -->
27

<!-- b000388 | prose | pages [27] -->
Longitude Date of Killing

<!-- b000389 | prose | pages [27] -->
1◦34’38.03”W 53◦49’22.72”N November 17 1980, 9:25 pm 1◦40’18.26”W 53◦48’30.95”N 53◦48’47.58”N August 20 1980, 11:00 pm 1◦34’3.23”W September 2 1979, 1:00 am 1◦52’18.99”W 53◦42’40.28”N April 4 1979, 11:55 pm 2◦13’35.21”W 53◦27’46.12”N May 16 1978, 11:00 pm 1◦46’46.20”W 53◦39’17.04”N January 31 1978, 9:25 pm 1◦45’59.09”W 53◦47’57.94”N 53◦25’57.94”N January 21 1978, 9:30 pm 2◦15’2.47”W October 1 1977, 9:30 pm 1◦31’58.99”W 53◦49’4.56”N

<!-- b000390 | prose | pages [27] -->
Sutcliﬀe

<!-- b000391 | prose | pages [27] -->
June 26 1977, 2:15 am 1◦45’49.79”W 53◦48’38.70”N 53◦50’1.26”N April 23 1977, 11:15 pm 1◦30’9.15”W February 5 1977, 11:30 pm 1◦31’58.58”W 53◦48’28.75”N January 20 1976, 7:30 pm 1◦54’28.10”W 53◦52’7.83”N July 5 1975, 1:30 am 1◦32’31.71”W 53◦49’7.15”N October 30 1975, 1:30 am 1◦32’28.77”W 53◦48’55.72”N December 14 1977, 8:30 pm 1◦43’47.22”W 53◦47’12.39”N July 10 1977, 3:20 am 1◦51’54.77”W 53◦43’48.65”N August 15 1975, 11:45 pm 1◦56’16.61”W 53◦54’52.78”N August 27 1975, 10:30 pm

<!-- b000392 | prose | pages [27] -->
118◦16’50.04”W 33◦56’36.66”N March 9, 1987 118◦16’49.98”W 33◦56’24.32”N October 29 1987 118◦16’57.66”W 33◦56’49.26”N January 20 1989 118◦16’57.85”W 33◦57’23.37”N September 23 1989 118◦16’50.55”W 33◦56’50.59”N September 30 1992 118◦16’50.55”W 33◦56’50.59”N November 16 1992 118◦16’57.77”W 33◦56’53.00”N

<!-- b000393 | prose | pages [27] -->
Chester Turner

<!-- b000394 | prose | pages [27] -->
December 16 1992 118◦16’57.78”W 33◦58’7.02”N April 2 1993 118◦17’5.57”W 33◦58’40.96”N May 16 1993 118◦16’59.76”W 33◦58’0.20”N February 12 1995 118◦16’42.38”W 33◦56’56.43”N November 6 1996 118◦15’20.32”W 34◦2’56.29”N February 3 1998 118◦14’26.07”W 34◦2’31.22”N April 6 1998

<!-- b000395 | prose | pages [27] -->
122◦8’59.18”W 38◦5’49.94”N December 20 1968, 11:15 pm 122◦11’30.51”W 38◦7’12.90”N

<!-- b000396 | prose | pages [27] -->
Zodiac Killer

<!-- b000397 | prose | pages [27] -->
July 4 1969, 11:55 pm 122◦14’7.71”W 38◦34’9.57”N September 27 1969, 6:15 pm 122◦27’25.98”W 37◦47’19.34”N October 11, 1969, 9:55 pm

<!-- b000398 | prose | pages [27] -->
118◦19’17.57”W 34◦0’17.48”N August 12 1986 118◦18’35.63”W 34◦0’14.98”N September 11 1988 118◦15’4.83”W 33◦59’37.53”N January 10 1987 118◦17’33.75”W 33◦58’41.68”N August 10 1985 118◦18’7.76”W 33◦58’32.96”N August 14 1986 118◦19’0.30”W 33◦57’54.10”N

<!-- b000399 | prose | pages [27] -->
Grim Sleeper

<!-- b000400 | prose | pages [27] -->
March 9 2002 118◦18’31.85”W 33◦57’27.36”N November 1 1987 118◦18’31.24”W 33◦57’7.36”N April 16 1987 118◦18’30.33”W 33◦56’50.31”N January 1 2007 118◦17’55.40”W 33◦57’17.11”N November 20 1988 118◦19’2.66”W 33◦56’41.05”N January 30 1988 118◦18’15.39”W 33◦56’19.68”N

<!-- b000401 | prose | pages [27] -->
51◦31’12.17”N 51◦31’13.51”N 51◦30’49.90”N

<!-- b000402 | prose | pages [27] -->
Jack the Ripper

<!-- b000403 | prose | pages [27] -->
51◦30’49.13”N 51◦31’7.29”N

<!-- b000404 | prose | pages [27] -->
July 11 2003

<!-- b000405 | prose | pages [27] -->
0◦3’37.34”W August 31 1988 0◦4’20.70”W September 8 1988 0◦3’57.16”W September 30 1988 0◦4’39.64”W September 30 1988 0◦4’30.32”W November 9 1988

<!-- b000406 | prose | pages [27] -->
Data collected via GoogleEarthTM and CommunityWalk.

<!-- b000407 | prose | pages [28] -->
Control # 8362 28

<!-- b000408 | heading | pages [28] -->
Model Plots for Sutcliﬀe

<!-- b000409 | prose | pages [28] -->
Here we show our presented functions for distance decay with their plots for Sutcliﬀe and Chester Turner. These are here to illustrate the diﬀerences between the diﬀerent functions.

<!-- b000410 | prose | pages [28] -->
(g) Criminal Location Probability Plot of Sut-

<!-- b000411 | prose | pages [28] -->
(h) Next Crime Probability Plot of Sutcliﬀe using

<!-- b000412 | prose | pages [28] -->
cliﬀe using Linear decay function.

<!-- b000413 | prose | pages [28] -->
Linear decay function.

<!-- b000414 | prose | pages [29] -->
Control # 8362

<!-- b000415 | prose | pages [29] -->
(i) Criminal Location Probability Plot of Sut- cliﬀe using Negative Exponential decay function.

<!-- b000416 | prose | pages [29] -->
(k) Criminal Location Probability Plot of Sut- cliﬀe using Truncated Negative Exponential de- cay function.

<!-- b000417 | prose | pages [29] -->
29

<!-- b000418 | prose | pages [29] -->
(j) Next Crime Probability Plot of Sutcliﬀe using Negative Exponential decay function.

<!-- b000419 | prose | pages [29] -->
(l) Criminal Location Probability Plot of Sut- cliﬀe using Truncated Negative Exponential de- cay function.

<!-- b000420 | prose | pages [30] -->
Control # 8362

<!-- b000421 | prose | pages [30] -->
(m) Criminal Location Probability Plot of Sut- cliﬀe using Plateaud Negative Exponential decay function.

<!-- b000422 | prose | pages [30] -->
(o) Criminal Location Probability Plot of Sut- cliﬀe using Normal decay function.

<!-- b000423 | prose | pages [30] -->
30

<!-- b000424 | prose | pages [30] -->
(n) Next Crime Probability Plot of Sutcliﬀe using Plateaued Negative Exponential decay function.

<!-- b000425 | prose | pages [30] -->
(p) Next Crime Probability Plot of Sutcliﬀe using Normal function.

<!-- b000426 | prose | pages [31] -->
Control # 8362 31

<!-- b000427 | prose | pages [31] -->
(q) Criminal Location Probability Plot of Sut-

<!-- b000428 | prose | pages [31] -->
(r) Next Crime Probability Plot of Sutcliﬀe using

<!-- b000429 | prose | pages [31] -->
cliﬀe using Negative Exponential decay function,

<!-- b000430 | prose | pages [31] -->
Negative Exponential function, time weighted.

<!-- b000431 | prose | pages [31] -->
time weighted.

<!-- b000432 | prose | pages [32] -->
Control # 8362 32

<!-- b000433 | heading | pages [32] -->
Model Plots for Chester Turner

<!-- b000434 | prose | pages [32] -->
(s) Criminal Location Probability Plot of Sut-

<!-- b000435 | prose | pages [32] -->
(t) Next Crime Probability Plot of Sutcliﬀe using

<!-- b000436 | prose | pages [32] -->
cliﬀe using Negative Exponential decay function,

<!-- b000437 | prose | pages [32] -->
Negative Exponential function, time weighted.

<!-- b000438 | prose | pages [32] -->
time weighted.

<!-- b000439 | prose | pages [33] -->
Control # 8362 33

<!-- b000440 | heading | pages [33] -->
References

<!-- b000441 | references | pages [33] -->
Arndt, W. B., Hietpas, T., & Kim, J. (2004). Critical characteristics of male serial

<!-- b000442 | references | pages [33] -->
murderers. American Journal of Criminal Justice, 29(1), 171–131.

<!-- b000443 | references | pages [33] -->
Brantingham, P., & Brantingham, P. (1981). Environmental Criminology. Beverly

<!-- b000444 | references | pages [33] -->
Hills, CA: Sage Publications.

<!-- b000445 | references | pages [33] -->
Gigerenzer, G., & Selton, R. (2001). Bounded rationality. London: MIT Press.

<!-- b000446 | references | pages [33] -->
Hickey, E. W. (2002). Serial murderers and their victims. Belmont, CA: Wadsworth,

<!-- b000447 | references | pages [33] -->
3 ed.

<!-- b000448 | references | pages [33] -->
Kent, J. D. (2003). Using Functional Distance Measures When Calibrating Journey-

<!-- b000449 | references | pages [33] -->
to-Crime Distance Decay Algorithms. Ph.D. thesis, Louisiana State University.

<!-- b000450 | references | pages [33] -->
Laukkanen, M., & Santtila, P. (2006). Predicting the residential location of a serial

<!-- b000451 | references | pages [33] -->
commercial robber. Forensic Science International, 157, 71–82.

<!-- b000452 | references | pages [33] -->
Levine, N. (2006). Crime mapping and the crimestat program. Geographical Analysis,

<!-- b000453 | references | pages [33] -->
38(1), 41–56.

<!-- b000454 | references | pages [33] -->
Newton, M. (1990). Hunting Humans. Port Townsend, WA: Loompanics Unlimited.

<!-- b000455 | references | pages [33] -->
Rhodes, W., & Conly, C. (1981). Crime and Mobility: An Empirical Study. Envi-

<!-- b000456 | references | pages [33] -->
ronmental Criminology. Prospect Heights, IL: Waveland Press, Inc.

<!-- b000457 | references | pages [33] -->
Santtila, P., Laukkanen, M., & Zappala, A. (2007). Crime behaviors and distance

<!-- b000458 | references | pages [33] -->
travelled in homocides and rapes. Journal of Investigative Psychology and Oﬀender

<!-- b000459 | references | pages [33] -->
Proﬁling, 4, 1–15.

<!-- b000460 | references | pages [33] -->
Snook, B., Taylor, P. J., & Bennell, C. (2004). Geographic proﬁling: The fast, frugal,

<!-- b000461 | references | pages [33] -->
and accurate way. Applied Cognitive Psychology, 18, 105–121.
