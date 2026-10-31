# P-B-2010-8479-b934962b

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
A killer is at large, and the police need our help! Lovers of mystery ﬁction might jump at the chance to engage in a hot pursuit of forensic clues and shady characters, but our reality is not so glamorous. Our task: given a set of crime site locations and times, narrow down a killer’s location and try to predict where the next murder might be.

<!-- b000002 | prose | pages [1] -->
We present two mathematical models to assist in the investigation. The models take the locations of previous crime sites and the times that they occurred as variables. These data are few compared to the seemingly inﬁnite possibilities of the criminal’s actions, but we know at least one thing: the criminal will do his best to avoid being caught. We infer then, in accordance with past research, that he will kill where he knows the surroundings. This motivates the assumption that the killer is more likely to kill closer to his home or to places where he has killed before. We further assume that the future locations of attacks depend only on the location of the killer’s home and the location and relative time of past crimes.

<!-- b000003 | prose | pages [1] -->
The ﬁrst of the two models, the Centrographic model, builds upon earlier work by LeBeau. It uses an analogy to kinematics to derive the location and movement of the “centroid” of a series of crime sites. We consider the change in the location of the centroid over time to predict future crime site locations. In other words, we model the series to have a “velocity” and “momentum” and use this information to predict the future location of the centroid.

<!-- b000004 | prose | pages [1] -->
Our second model, the Rational Serial Criminal model, uses methods from microeconomic theory to model the criminal as a rational agent. This model formalizes the process of looking at a series of crime locations and assessing where the criminal prefers to ﬁnd victims or dump bodies. Using data on a series of crimes, the model outputs contour surfaces representing areas where the killer is more or less likely to live. From here, we extend the model to predict where a killer is likely to strike next.

<!-- b000005 | prose | pages [1] -->
We run simulations on crime site data for diﬀerent serial killers and compare our location predictions to the actual next kill in the series. The centrographic model performs well as measured by the error distance. Unfortunately, the model is sensitive to a parameter that must be determined for each individual series. The rational choice model also performs well predicting home location as measured by the Hit Score %, a metric which compares the eﬃciency of a search informed by prediction to a random search.

<!-- b000006 | prose | pages [1] -->
Our model could be another useful tool for police chasing a serial killer. While we do not incorporate data such as population density or geographic features, we believe that police oﬃcers will have no trouble ﬁlling in these gaps. The model provides a good starting point when data are too few to utilize more complex methods.

<!-- b000007 | prose | pages [1] -->
1

<!-- b000008 | furniture | pages [2] -->
Team # 8479

<!-- b000009 | furniture | pages [2] -->
Page 1 of 25

<!-- b000010 | prose | pages [2] -->
From Kills to Kilometers Using Centrographic Techniques and Rational Choice

<!-- b000011 | prose | pages [2] -->
Theory for Geographical Proﬁling of Serial Killers

<!-- b000012 | prose | pages [2] -->
February 22, 2010

<!-- b000013 | heading | pages [2] -->
Abstract

<!-- b000014 | prose | pages [2] -->
We present two mathematical models to assist in the investigation of a serial killer. The models take the locations of previous crime sites and the order that they occurred as variables. These data are few compared to the seemingly inﬁnite possibilities of the criminal’s actions, but at least one thing is known: the criminal will do his best to avoid being caught. We infer then, in accordance with past research, that he will kill where he knows the surroundings. This motivates the assumption that the killer is more likely to kill closer to his home or places he has killed before. We further assume that the future locations of attacks depend only on the location of the killer’s home and the location and relative time of past crimes.

<!-- b000015 | prose | pages [2] -->
The ﬁrst of the two models, the “centrographic” model, builds upon earlier work by LeBeau. It uses an analogy to kinematics to derive the location and movement of the “centroid” of a series of crime sites. We consider the change in the location of the centroid over time to predict future crime site locations. In other words, we model the series to have a “velocity” and “momentum” and use this information to predict the future location of the centroid.

<!-- b000016 | prose | pages [2] -->
Our second model, the Rational Serial Criminal model, uses methods from microeconomic theory to model the criminal as a rational agent. This model formalizes the process of looking at a series of crime locations and assessing where the criminal prefers to ﬁnd victims or dump bodies. Using data on a series of crimes, the model outputs contoured surfaces representing areas where the killer is more or less likely to live. From here, we extend the model to predict where a killer is likely to strike next.

<!-- b000017 | prose | pages [2] -->
We run simulations on crime site data for diﬀerent serial killers and compare our location predictions to the actual next kill in the series. The centrographic model performs well as measured by the error distance. Un- fortunately, the model is sensitive to a parameter that must be determined for each individual series. The rational choice model also performs well predicting home location as measured by the Hit Score %, a metric which compares the eﬃciency of a search informed by prediction to a random search.

<!-- b000018 | furniture | pages [3] -->
Team # 8479

<!-- b000019 | furniture | pages [3] -->
Page 2 of 25

<!-- b000020 | prose | pages [3] -->
1

<!-- b000021 | heading | pages [3] -->
Introduction

<!-- b000022 | prose | pages [3] -->
When a serial killer is on the prowl 1, the police deploy every available resource to stop the killings and bring the murderer to justice. Serial killers provide an interesting challenge to geographic proﬁlers, due to the relative paucity of data on these criminals and their unique geographic behavior. Statistical prediction methods in widespread use for other types of serial crimes such as burglaries [8] or auto thefts [39] are less useful for ﬁnding serial killers, as these methods rely on a large initial data set to generate predictions.

<!-- b000023 | prose | pages [3] -->
We attempt to predict a serial killer’s future behavior and location data on their crime sites and initial assumptions about their behavior. In Section 3, we adapt two complementary models to predict future crime sites and point to the location of a serial killer’s anchor point [32].

<!-- b000024 | prose | pages [3] -->
We tested our models by implementing each one in a computer simulation, and running them on partial data sets from two historical serial killers. We describe our data collection process and provide examples in Section 5.

<!-- b000025 | prose | pages [3] -->
We compared our models’ predictions for the locations of later crimes to the actual locations where later crimes in each series occurred. We describe the results of these simulations in Section 6. Finally, in Section 7, we note some shortcomings of our approach and propose directions for further research.

<!-- b000026 | prose | pages [3] -->
2 Background Information

<!-- b000027 | prose | pages [3] -->
2.1 Serial Killing

<!-- b000028 | prose | pages [3] -->
The FBI deﬁnes serial murder as three or more killings with “cooling-oﬀ” periods in between [32, 27]. Experience shows that the behavior of such serial criminals follows some predictable patterns. Speciﬁcally, serial killers tend to operate near their homes, in areas with which they are familiar [32]. For example, one study of 126 U.S. serial killers found that 89% of them lived within a circle drawn around the locations where they disposed of bodies [23]. The inclination of a serial killer to work close to a home base or anchor point [32] often leads to a spatial clustering of their crime sites. Therefore, by looking at the geographic locations of crimes, we can say something about where the criminal who committed them is likely to live or might strike next.

<!-- b000029 | prose | pages [3] -->
In the past two decades, “geographical proﬁling” has exploded, and many law-enforcement agencies now use spatial modeling techniques in the pursuit of serial criminals [33]. The most popular approach includes the assumption that the criminal lives near his crime scenes, and has not moved place of residence since the crime spree began [32, 33].

<!-- b000030 | prose | pages [3] -->
1During such an investigation, even if the same modus operandi is followed, the police might not acknowledge a series of crimes as being the work of one person. Thus, one might be inclined to refer to this suspect as an alleged serial killer for precision. For the duration of this paper, we will assume that all such series are the work of one person, and will drop the “alleged”.

<!-- b000031 | furniture | pages [4] -->
Team # 8479

<!-- b000032 | furniture | pages [4] -->
Page 3 of 25

<!-- b000033 | prose | pages [4] -->
2.2 Previous Work

<!-- b000034 | prose | pages [4] -->
At ﬁrst blush, criminals seem diﬃcult, if not impossible, to predict. The crimi- nal, however, must follow some sort of thought process in order to commit his acts and, as such, “crime pattern theory combines rational choice, routine activ- ity theory, and environmental principles to explain the distribution of crimes” [32]. From these ideas, geographical proﬁling was developed. When analyzing serial crimes, few data are available other than that at the crime scene and dis- posal site of the body. This motivates Lundrigan and Canter’s research into a serial killer’s disposal site location choice, which statistically analyzed data on apprehended serial killers to determine how a killer’s home location related to his body disposal sites [23]. Many factors can inﬂuence the serial killer’s disposal site selection. In a study conducted in Germany, the median distance between the disposal site and the killer’s home decreased as age of killer increased, a killer’s higher IQ corresponds to a further distance of disposal site from the home base, though the number of murders and distance between a killer’s home and disposal site was not statistically signiﬁcant [38].

<!-- b000035 | prose | pages [4] -->
Another method of determining the location of a serial killer is to consider the daily routines of the victims. Geographic proﬁlers can use mapping soft- ware to determine where victims’ routines overlap, and these locations can be interpreted as places where the killer might have seen the victims. These data, in turn, can be used to hypothesize the killer’s daily whereabouts [37]. In an age where most people are connected to the rest of the world through cellular telephones and internet, it is possible now more than ever to gather objective data regarding where a person was at a certain time.

<!-- b000036 | prose | pages [4] -->
In modeling serial crime, a primary concern of geographical proﬁling is the prediction of areas at high risk of future crime, known colloquially as crime “hotspots”. Past models for geographical proﬁling of serial oﬀenders have shown varying results. Due to the nature of serial crimes as discrete events, the ma- jority of methods for displaying and analyzing data on serial criminals utilize a technique known as point mapping [10]. A problem with simple point mapping, however, as described by Chainey et al., is that “it is diﬃcult to clearly iden- tify the location, relative scale, size and shape of hotspots when crime data are presented as points”. As such, it becomes necessary to ﬁnd alternate methods of display and analysis.

<!-- b000037 | prose | pages [4] -->
3

<!-- b000038 | heading | pages [4] -->
Models

<!-- b000039 | prose | pages [4] -->
3.1

<!-- b000040 | heading | pages [4] -->
A Centrographic Model

<!-- b000041 | prose | pages [4] -->
3.1.1

<!-- b000042 | heading | pages [4] -->
Background

<!-- b000043 | prose | pages [4] -->
A standard analytical measure in the geographical proﬁling toolbox is the spa- tial mean of point data, obtained by summing the geographic coordinates over all observations independently in each spatial dimension and dividing by the to- tal number of observations [32]. This eﬀectively generates a ‘center’ to the data

<!-- b000044 | furniture | pages [5] -->
Team # 8479

<!-- b000045 | furniture | pages [5] -->
Page 4 of 25

<!-- b000046 | prose | pages [5] -->
set that can be used in conjunction with other methods to describe the concen- tration of a distribution. A long-utilized and relatively simple tool, the spatial mean remains in widespread use today in geographical proﬁling due to its ease of use. Despite the simplicity of calculation, previous studies have shown the spatial mean to perform comparably to alternative, more complex algorithms and even human judgment [39].

<!-- b000047 | prose | pages [5] -->
One drawback to the spatial mean is that it doesn’t intrinsically use time to describe and forecast an evolving distribution such as is seen with serial killings. To utilize the temporal aspect of such a data set, we must extend the model. One extension that arises naturally is to consider the change in the spatial mean over time [21]. Previous work has used analogy to simple physical phenomenon to come up with parallels to velocity (change in position over time), acceleration (change in velocity over time), and momentum (the product of velocity and mass) [32, 21]. In this model we will use several of these concepts to come up with a method of predicting the locations of future kills or crimes in a spree.

<!-- b000048 | prose | pages [5] -->
3.1.2

<!-- b000049 | heading | pages [5] -->
Assumptions

<!-- b000050 | prose | pages [5] -->
To justify a centrographic approach to geographical proﬁling, a few assumptions must be made regarding the behavior of serial killers:

<!-- b000051 | prose | pages [5] -->
• A serial killer is more likely to kill in an area he’s familiar with, (i. e., a place he lives near or has killed near before.)

<!-- b000052 | prose | pages [5] -->
• The distribution of probable locations of next kill changes with time, even if the distribution of known kills does not.

<!-- b000053 | prose | pages [5] -->
• The order in which and time at which kill events in a distribution occur are a factor in determining probable locations of next kill, not just the spatial location.

<!-- b000054 | prose | pages [5] -->
3.1.3

<!-- b000055 | heading | pages [5] -->
Model

<!-- b000056 | prose | pages [5] -->
Deﬁne XKj to be the position vector corresponding to the site of the j-th observed crime, Kj. If we consider the reach or area of activity of a serial killer to be represented by the distribution of the observed events, we can deﬁne the ‘center of mass’ or centroid of the area of activity at the time of the of the j-th event, Cj, to be the geographic mean of XK1 . . . XKj,

<!-- b000057 | prose | pages [5] -->
Cj =

<!-- b000058 | prose | pages [5] -->
j j

<!-- b000059 | prose | pages [5] -->
XKi

<!-- b000060 | prose | pages [5] -->
X

<!-- b000061 | prose | pages [5] -->
j

<!-- b000062 | prose | pages [5] -->
i=1 i=1

<!-- b000063 | prose | pages [5] -->
Utilizing this, a reasonable estimate for a probable area of future encounter with the criminal, A, can be obtained by ﬁnding the mean distance from Cj to each event Ki in each spatial direction and deﬁning A to be the area within the polygon formed by extending from the mean this distance in each corresponding direction.

<!-- b000064 | furniture | pages [6] -->
Team # 8479

<!-- b000065 | furniture | pages [6] -->
Page 5 of 25

<!-- b000066 | prose | pages [6] -->
Since Cj is a spatial location that changes with time, it is natural to calculate the change in position per unit time—the geographic analogue of the velocity of C at the time of the j-th event, tj [32],

<!-- b000067 | prose | pages [6] -->
VCj = dCj

<!-- b000068 | prose | pages [6] -->
dt ,

<!-- b000069 | prose | pages [6] -->
as well as an analogue of the ‘linear momentum’ of C at time tj [21],

<!-- b000070 | prose | pages [6] -->
PCj = jVCj,

<!-- b000071 | prose | pages [6] -->
where the ‘mass’ of the distribution is equal to the current number of serial events, j.

<!-- b000072 | prose | pages [6] -->
The concept of linear momentum PCj is important to our model as it allows for a mathematical analysis of the spatial direction in which the kill spree seems to be moving, relating PCj to PCj−1 by considering the law of conservation of momentum. We deﬁne the velocity of serial event Kj as the distance between event Kj and the previous centroid divided by the time between event Kj and Kj−1

<!-- b000073 | prose | pages [6] -->
VKj = XKj −Cj−1

<!-- b000074 | prose | pages [6] -->
.

<!-- b000075 | prose | pages [6] -->
tj −tj−1

<!-- b000076 | prose | pages [6] -->
It follows from the deﬁnition of mass above that the mass of a single event is 1, and thus the momentum of a single event Kj is equal to its velocity,

<!-- b000077 | prose | pages [6] -->
PKj = VKj.

<!-- b000078 | prose | pages [6] -->
Modeling the state of Cj at time tj as the result of a completely inelastic collision between Cj−1 and Kj (i.e., Kj is absorbed and joins Cj−1 to form Cj), conservation of momentum tells us that

<!-- b000079 | prose | pages [6] -->
PCj = jVCj = PCj−1 + PKj = (j −1)VCj−1 + VKj,

<!-- b000080 | prose | pages [6] -->
or,

<!-- b000081 | prose | pages [6] -->
VCj = (j −1)VCj−1 + VKj

<!-- b000082 | prose | pages [6] -->
where it follows trivially that

<!-- b000083 | prose | pages [6] -->
, j

<!-- b000084 | prose | pages [6] -->
VC1 = 0,

<!-- b000085 | prose | pages [6] -->
which follows expectations for a spree consisting of only one kill (non-serial).

<!-- b000086 | prose | pages [6] -->
To make a prediction for the next kill site in a series Kj+1, we can incorporate both the current centroid Cn and the current velocity of the centroid VCj by deﬁning A(t) as the polygon A as deﬁned above with a center dependent on time according to VCn,

<!-- b000087 | prose | pages [6] -->
CenterA(t) = Cj + f(t)VCj + g(t)ˆaj,

<!-- b000088 | furniture | pages [7] -->
Team # 8479

<!-- b000089 | furniture | pages [7] -->
Page 6 of 25

<!-- b000090 | prose | pages [7] -->
where ˆaj is an estimate of the acceleration of Cj based on a linear regression of velocity data obtained from K1 . . . Kj and f(t) and g(t) are parameter coeﬃ- cients chosen to match the constraints:

<!-- b000091 | prose | pages [7] -->
d(CenterA(t))

<!-- b000092 | prose | pages [7] -->
lim t→∞

<!-- b000093 | prose | pages [7] -->
= 0 (1) dt dt

<!-- b000094 | prose | pages [7] -->
f(t) ≈tfor t < ¯t (2)

<!-- b000095 | prose | pages [7] -->
g(t) ≈t2/2for t < ¯t

<!-- b000096 | prose | pages [7] -->
where ¯t is the mean time between Ki’s.

<!-- b000097 | prose | pages [7] -->
(3)

<!-- b000098 | prose | pages [7] -->
Constraint 1 is necessary to keep our prediction reasonably centered on the observed events over long spans of time, and conditions 2 and 3 are necessary for the kinematic analogue. One possible choice of f(t) and g(t) explored in this paper is

<!-- b000099 | prose | pages [7] -->
2t f(t) = 1 + eβt ,

<!-- b000100 | prose | pages [7] -->
for some real constant β > 0.

<!-- b000101 | prose | pages [7] -->
2t2 g(t) =

<!-- b000102 | prose | pages [7] -->
(1 + eβt)2

<!-- b000103 | prose | pages [7] -->
Note that the ﬁnal model yields a prediction A(t) that is a function of time, consistent with our assumption of an evolving killer. To get a general prediction, it is possible to evaluate A(¯t), yielding the prediction for where the next kill will occur should it happen after the mean time ¯t.

<!-- b000104 | heading | pages [7] -->
A Rational Choice Model

<!-- b000105 | prose | pages [7] -->
3.2

<!-- b000106 | prose | pages [7] -->
3.2.1

<!-- b000107 | heading | pages [7] -->
Background

<!-- b000108 | prose | pages [7] -->
A number of criminologists have suggested that much criminal behavior can be modeled as rational choices made by agents who derive some utility from their crimes [6, 12, 29]. On one hand, criminal activity has historically been seen as defying rationality [12]. If we grant, however, that a given rapist, burglar, or other criminal will rape, burglarize, or otherwise break the law, then their choices of whom to rape or which houses to burglarize may appear rational [16], and may in fact be the result of much planning and deliberation. This makes rational choice theory as implemented in economics particularly well-suited for our purpose here of looking at a collection of crimes to draw inferences about the criminal’s future behavior.

<!-- b000109 | prose | pages [7] -->
Previous studies have applied economic theory to criminology by using Ex- pected Utility Theory [40] and Prospect Theory [20] to model a criminal who weighs the beneﬁts to himself of committing a crime against the odds of getting caught and its associated harm. While our model here is based on the idea from microeconomics of using observed revealed preference data to make inferences about unobserved preferences [34], it does not resemble a traditional economic model so nearly as do these earlier works.

<!-- b000110 | prose | pages [7] -->
The microeconomic model seeks to make predictions about the responses of dependent variables (such as quantities consumed of various goods) to possible

<!-- b000111 | furniture | pages [8] -->
Team # 8479

<!-- b000112 | furniture | pages [8] -->
Page 7 of 25

<!-- b000113 | prose | pages [8] -->
future values of independent variables (such as prices) based on past obser- vations of both [34].

<!-- b000114 | prose | pages [8] -->
In this model, the agent selects a bundle of goods to purchase by assigning quantities to each available good; these quantities form a consumption vector. In our model, the agent assigns probabilities to each possible location for his next crime, forming a probability vector. The economic agent faces a scalar budget and a vector of prices. The dot-product of her cho- sen consumption vector and the environmental price vector must not exceed her budget. She is assumed to maintain a consistent ranking of all possible consumption bundles. For our criminal agent, the analogue of price is perceived risk of getting caught if he commits his next crime in a given location. While we cannot observe this the same way that we observe prices, it is analogous in that it diﬀers across observations, since we expect the risks of getting caught in various locations to change each time the criminal acts (due to increased public awareness or police presence, e.g.). His (unrelated) constraint is that the en- tries in his probability vector must sum to 1. Rather than ranking consumption bundles, he ranks probability distributions.

<!-- b000115 | prose | pages [8] -->
Choosing a probability distribution as a means of agency has precedent in the notion of a mixed strategy in game theory [15]. We believe this reﬂects the nature of the actual choices the criminal makes, particularly about location. Geographical proﬁling expert D. Kim Rossmo notes that “for a direct-contact predatory crime to occur, the paths of the oﬀender and victim must intersect in time and space, within an environment appropriate for criminal activity.” [32]. Since the criminal cannot signiﬁcantly control the ﬂow of potential victims or the suitability of diﬀerent locations, he does not have complete control over where and when he breaks the law. Rather, when he walks down a particular street, he is choosing to increase the probability that he will commit his next crime there.

<!-- b000116 | prose | pages [8] -->
Since a rational agent must have consistent preferences, if our serial criminal is to evolve, then each crime must change his incentive structure. We model this by including a perceived extra risk of capture at any given potential target as a function of the locations of previous acts: you can never go back to the scene of a perfect crime [11]. Since the overall risk of getting caught should already be a signiﬁcant factor in the agent’s preference for one crime scene over another, it is only this additional risk which we call analogous to price.2

<!-- b000117 | prose | pages [8] -->
When we talk about a “rational serial criminal”, we do not mean to suggest that there are good reasons for committing series of crimes.3 We merely hy- pothesize that by assuming this series of crimes to be determined by a consistent preference ﬁeld [30], we may make useful predictions about the criminal. Ad- ditionally, when we talk about “utility” as a function of the probability vector described above, we do not mean to imply that committing crimes fulﬁlls some desire of the criminal’s to a variable extent depending on where he does it. The

<!-- b000118 | prose | pages [8] -->
2One could argue that a fully rational criminal adding up the costs of committing a crime at a particular place would consider the loss in welfare he would experience when it became riskier for him to commit other crimes there in the future. While technically true, we do not consider this point relevant to our analysis, or at all.

<!-- b000119 | prose | pages [8] -->
3But nor do we deny it.

<!-- b000120 | furniture | pages [9] -->
Team # 8479

<!-- b000121 | furniture | pages [9] -->
Page 8 of 25

<!-- b000122 | prose | pages [9] -->
utility function is just a convenient mathematical tool, which is equivalent to making direct inferences from revealed preference [17].

<!-- b000123 | prose | pages [9] -->
To summarize, we construct a model of a rational serial criminal who controls his behavior by determining a probability distribution deﬁned over a bounded geographical range of activity. This is the distribution of a random variable representing the location of his next crime. The model does not include the decision to commit a crime, as we are interested in modeling the behavior of a serial oﬀender in the course of a spree. We assume the distribution to be static over the period between any two crimes, and to change instantaneously at the instant that a crime is committed.

<!-- b000124 | prose | pages [9] -->
3.2.2 Rational Choice: Theory

<!-- b000125 | prose | pages [9] -->
Divide the criminal’s assumed range into n cells, numbered 1 through n. In- cluded in our data, then, is a vector K, where each Kj ∈{1, ..., n} denotes the cell in which the criminal committed his jth crime. Assume the criminal is a rational agent with a utility function

<!-- b000126 | prose | pages [9] -->
U(p, c),

<!-- b000127 | prose | pages [9] -->
where p is a vector deﬁned over all cells of the grid such that pi = the probability that next crime will happen in cell i, and c is a vector of the same dimension such that ci = the criminal’s perception of the increased risk that he will be caught if he commits his next crime in cell i.

<!-- b000128 | prose | pages [9] -->
He chooses p to maximize U subject to the constraint

<!-- b000129 | prose | pages [9] -->
n X

<!-- b000130 | prose | pages [9] -->
i=1

<!-- b000131 | prose | pages [9] -->
This yields the ﬁrst-order conditions

<!-- b000132 | prose | pages [9] -->
∂U

<!-- b000133 | prose | pages [9] -->
pi = 1.

<!-- b000134 | prose | pages [9] -->
(p1, . . . , pn, c1, . . . , cn) ∂p1 ... ∂U = 0 ... (p1, . . . , pn, c1, . . . , cn) ∂pn = 0

<!-- b000135 | prose | pages [9] -->
Assume that U is well-behaved, so that we may invoke the Implicit Function Theorem to deﬁne k(c) such that

<!-- b000136 | prose | pages [9] -->
p1 = k1 ...

<!-- b000137 | prose | pages [9] -->
... pn = kn (c1, ..., cn)

<!-- b000138 | prose | pages [9] -->
.

<!-- b000139 | prose | pages [9] -->
(c1, ..., cn)

<!-- b000140 | prose | pages [9] -->
Assume that each time the criminal commits a crime, c changes, and therefore k changes. As the function k(c) is arbitrary, it may contain any number of parameters α: these may reﬂect any way in which we think the criminal prefers one location for his crime over another. It is these parameters which we hope to ﬁnd.

<!-- b000141 | furniture | pages [10] -->
Team # 8479

<!-- b000142 | furniture | pages [10] -->
Page 9 of 25

<!-- b000143 | prose | pages [10] -->
We begin by assuming a form for c(x). It may be as simple as

<!-- b000144 | prose | pages [10] -->
(

<!-- b000145 | prose | pages [10] -->
c(Xj) =

<!-- b000146 | prose | pages [10] -->
if i ∈Xj 1 1 otherwise , (4) 0 0

<!-- b000147 | prose | pages [10] -->
where Xj = {i| the criminal committed one of his ﬁrst j crimes in cell i}. This form captures the belief, “If I commit a crime twice in the same spot, I will be arrested for sure, but otherwise my past crimes have no impact on my chances of being caught.” Next, assume some form for the ki functions. For a criminal assumed to prefer working near a home base (allowing for a buﬀer zone), a possible one-parameter function would be

<!-- b000148 | prose | pages [10] -->
(

<!-- b000149 | prose | pages [10] -->
0

<!-- b000150 | prose | pages [10] -->
ki(c, α) =

<!-- b000151 | prose | pages [10] -->
if α = i (5) 1−ci otherwise d(α,i)¯k

<!-- b000152 | prose | pages [10] -->
where α represents the location of a home base, d is a metric, and ¯k is a normal- ization constant. Then for any value(s) of α, we can calculate the probability P(Kj|Xj−1, α) that the rational criminal characterized by the functions k and c, having committed j −1 crimes in the set of locations Xj−1 where the ﬁrst j −1 crimes occurred, would have committed his jth crime in the location Kj where the jth crime actually took place. Finally, deﬁne

<!-- b000153 | prose | pages [10] -->
\

<!-- b000154 | prose | pages [10] -->
P(K|α) =

<!-- b000155 | prose | pages [10] -->
j

<!-- b000156 | prose | pages [10] -->
kKj(c(Xj−1), α).

<!-- b000157 | prose | pages [10] -->
(6)

<!-- b000158 | prose | pages [10] -->
Then P(K|α) is the probability that the observed set of crimes K would have been committed by our rational criminal, given α. By evaluating this function over a range of possible values for α, we can get an idea of which parameter values are more probable than others.

<!-- b000159 | prose | pages [10] -->
Rational Serial Criminal: Practice 3.2.3

<!-- b000160 | prose | pages [10] -->
The theory above could be used to model any serial criminal who commits crimes at diﬀerent locations. In the current paper, we are interested in helping a police department catch a serial killer, and in this section we describe our speciﬁc implementation of a Rational Serial Criminal (RSC) model for this task.

<!-- b000161 | prose | pages [10] -->
When a serial killer is at large, law enforcement has two goals: to prevent future killings and to ﬁnd the killer. The rational choice model can help with both of these goals, by making predictions about where the killer lives and about where he may kill again, both based on previous killings. Implementing the model requires making explicit our assumptions about the killer’s behavior. For both purposes, we make the following assumptions:

<!-- b000162 | prose | pages [10] -->
• The killer prefers to kill near, but not at, an anchor point α. This anchor point does not change over the course of the spree.

<!-- b000163 | prose | pages [10] -->
• The killer’s taste for killing in a given location, ki, is a function only of that location’s distance from his anchor point and its distance from previous kill sites X.

<!-- b000164 | furniture | pages [11] -->
Team # 8479

<!-- b000165 | furniture | pages [11] -->
Page 10 of 25

<!-- b000166 | prose | pages [11] -->
• ki is given by Equations 4 and 5.

<!-- b000167 | prose | pages [11] -->
First, we estimate the likelihood that the killer lives in each grid-cell of the city. We make the following additional assumptions:

<!-- b000168 | prose | pages [11] -->
• The prior odds P(α) of the killer living in place α are equal for all α.

<!-- b000169 | prose | pages [11] -->
• The prior odds P(Kj = i) of the killer committing his jth murder in place i are equal for all i.

<!-- b000170 | prose | pages [11] -->
Given these assumptions, Bayes’ Formula

<!-- b000171 | prose | pages [11] -->
P(K|α = i)P(α = i) P(α = i|K) = P(K|α = 1)P(α = 1) + · · · + P(K|α = n)P(α = n)

<!-- b000172 | prose | pages [11] -->
implies

<!-- b000173 | prose | pages [11] -->
P(α = i|K) ∝P(K|α = i).

<!-- b000174 | prose | pages [11] -->
(7)

<!-- b000175 | prose | pages [11] -->
Our goal, and perhaps the limit of our abilities, is to rank potential anchor points in order of likelihood. As such, Equation 7 is suﬃcient to say that the isopleth produced by plotting Equation 6 may be taken as a jeopardy surface, representing the relative likelihood of the killer residing within the region asso- ciated with each grid cell [32]. Such a plot could help the police ﬁnd the killer faster by telling them where to look ﬁrst [32].

<!-- b000176 | prose | pages [11] -->
Next, we estimate the likelihood that the killer will strike next in each grid-cell.

<!-- b000177 | prose | pages [11] -->
For each grid cell i, this is equivalent to pi.

<!-- b000178 | prose | pages [11] -->
Again, we assume P(α|K1, . . . , Kj−1) ∝P(K1, . . . , Kj−1|α) for all α.

<!-- b000179 | prose | pages [11] -->
Using data from J −1 attacks, we estimate the likelihood that the Jth attack will occur in any given cell i by

<!-- b000180 | prose | pages [11] -->
J−1

<!-- b000181 | prose | pages [11] -->
n

<!-- b000182 | prose | pages [11] -->
X

<!-- b000183 | prose | pages [11] -->
X

<!-- b000184 | prose | pages [11] -->
ˆpi ∝

<!-- b000185 | prose | pages [11] -->
ki(c(Xj−1), α)P(K1, . . . , Kj−1|α),

<!-- b000186 | prose | pages [11] -->
α=1

<!-- b000187 | prose | pages [11] -->
j=1

<!-- b000188 | prose | pages [11] -->
where P(K1, . . . , Kj−1|α) is computed by Equation 6. Again, our goal is to rank possible locations for the next attack by likelihood, so we do not bother with normalization constants.

<!-- b000189 | prose | pages [11] -->
4 Data

<!-- b000190 | prose | pages [11] -->
5 Data

<!-- b000191 | prose | pages [11] -->
To calibrate and test our models, we constructed data sets from data on three real serial killers: David Berkowitz, the “Son of Sam”, Angelo Buono and Ken- neth Bianchi, the “Hillside Strangler” (police originally thought there was a single killer), and John Allen Muhammad, the “D.C. Sniper”. For each one, we began with a list of the killer’s victims taken from a Wikipedia [3, 4, 2], and then ﬁlled in details for each murder or attempted murder with details found in newspaper articles from the time. The Berkowitz and Sniper data sets included

<!-- b000192 | furniture | pages [12] -->
Team # 8479

<!-- b000193 | furniture | pages [12] -->
Page 11 of 25

<!-- b000194 | prose | pages [12] -->
address where people were shot, while the Hillside dataset included locations where strangled bodies were found. For calculations, we converted the street addresses to latitude-longitude coordinate pairs (Table 1).

<!-- b000195 | prose | pages [12] -->
Kill# Longitude Latitude RelativeDay -73.833846◦ 40.847067◦ 1 0

<!-- b000196 | prose | pages [12] -->
-73.804809◦ 40.768099◦ 2 25

<!-- b000197 | prose | pages [12] -->
-73.706561◦ 40.738631◦ 3 121

<!-- b000198 | prose | pages [12] -->
-73.845048◦ 40.718511◦ 4 185

<!-- b000199 | prose | pages [12] -->
-73.847051◦ 40.718598◦ 5 222

<!-- b000200 | prose | pages [12] -->
-73.835418◦ 40.847445◦ 6 262

<!-- b000201 | prose | pages [12] -->
-73.771343◦ 40.758704◦ 7 332

<!-- b000202 | prose | pages [12] -->
-74.011712◦ 40.612735◦ 8 367

<!-- b000203 | prose | pages [12] -->
Victim(s) Address Donna Lauria and

<!-- b000204 | prose | pages [12] -->
2860 Burhe Ave,

<!-- b000205 | prose | pages [12] -->
Jody Valenti

<!-- b000206 | prose | pages [12] -->
Bronx, NY Carl Denaro and

<!-- b000207 | prose | pages [12] -->
160th St and 33rd

<!-- b000208 | prose | pages [12] -->
Rosemary Keenan

<!-- b000209 | prose | pages [12] -->
Ave, Queens, NY Joanne Lomino and

<!-- b000210 | prose | pages [12] -->
83-31 262nd St,

<!-- b000211 | prose | pages [12] -->
Donna Demasi

<!-- b000212 | prose | pages [12] -->
Queens, NY Christine Freund

<!-- b000213 | prose | pages [12] -->
1 Station Square,

<!-- b000214 | prose | pages [12] -->
and John Diel

<!-- b000215 | prose | pages [12] -->
Queens, NY Virginia

<!-- b000216 | prose | pages [12] -->
4 Dartmouth St,

<!-- b000217 | prose | pages [12] -->
Voskerichian

<!-- b000218 | prose | pages [12] -->
Queens, NY Alexander Esau

<!-- b000219 | prose | pages [12] -->
1878 Hutchinson

<!-- b000220 | prose | pages [12] -->
and Valentina

<!-- b000221 | prose | pages [12] -->
River Parkway,

<!-- b000222 | prose | pages [12] -->
Suriani

<!-- b000223 | prose | pages [12] -->
Bronx, NY Sal Lubo and Judy

<!-- b000224 | prose | pages [12] -->
45-39 211th St,

<!-- b000225 | prose | pages [12] -->
Placido

<!-- b000226 | prose | pages [12] -->
Queens, NY Stacy Moskowitz

<!-- b000227 | prose | pages [12] -->
86th St and 14th

<!-- b000228 | prose | pages [12] -->
and Robert Vi-

<!-- b000229 | prose | pages [12] -->
Ave, Brooklyn, NY

<!-- b000230 | prose | pages [12] -->
olante

<!-- b000231 | caption | pages [12] -->
Table 1: Example data set: Berkowitz murders [36, 3]

<!-- b000232 | prose | pages [12] -->
6

<!-- b000233 | heading | pages [12] -->
Results

<!-- b000234 | prose | pages [12] -->
6.1

<!-- b000235 | heading | pages [12] -->
Centrographic Model

<!-- b000236 | prose | pages [12] -->
To test the centrographic model’s predictive capabilities, we implemented it via a Python script and ran it on the data from the Hillside kills sequentially, using the ﬁrst j −1 kills to predict the jth starting with j = 4 (Figure 1). As the output from the model changes with time we used the actual time of the subsequent kill Kj in evaluating the prediction function. In our simulations we

<!-- b000237 | prose | pages [12] -->
¯tj ln 15 where ¯tj is the mean time between kills up to

<!-- b000238 | prose | pages [12] -->
adopted an β value of β =

<!-- b000239 | prose | pages [12] -->
kill j. In practice a value of β must be determined according to the previous crime data for the speciﬁc series.

<!-- b000240 | prose | pages [12] -->
To measure accuracy of the model, we calculated the distance between the center of the area of probable next kill and the actual location of the next kill (Table 2). The error distance has been criticized in past works [32], but recent comparisons between the error distance and alternative accuracy measures have shown it to perform comparably [39]. The metric we use in calculating error distance is the L1 or Manhattan metric,

<!-- b000241 | prose | pages [12] -->
d1(p, q) = ||p −q||1 = |px −qx| + |py −qy|

<!-- b000242 | prose | pages [12] -->
Our choice of the Manhattan metric arises from previous work indicating that it most accurately models actual travel distance in urban settings, a more im- portant factor than strict Euclidean distance in geographical proﬁling [32].

<!-- b000243 | furniture | pages [13] -->
Team # 8479

<!-- b000244 | furniture | pages [13] -->
Page 12 of 25

<!-- b000245 | prose | pages [13] -->
To estimate the acceleration of the spatial centroid we perform a linear regression on the calculated centroidal velocity data for each estimate, in both the longitudinal (Table 3) and latitudinal (Table 4) directions independently.

<!-- b000246 | prose | pages [13] -->
Distance from center of predicted area (km) Kill# 19.9032477532 4 13.1624956104 5 26.1455165479 6 12.1278772065 7 4.41086910109 8

<!-- b000247 | caption | pages [13] -->
Table 2: Distance between center of predicted area and actual location of sub-

<!-- b000248 | prose | pages [13] -->
sequent kill, measured with Manhattan metric. Hillside data set [19].

<!-- b000249 | prose | pages [13] -->
Kill# ˆax 4 0.00119566020314 5 0.00110767788734 R2 p 1.0 N/A 0.99360376805 0.0720425343571 0.829782525827 6 0.000787815342892 0.170217474173 0.592338457701 7 0.000494702112585 0.292588804185 0.571437451732 8 0.000422872375405 0.236142632648

<!-- b000250 | caption | pages [13] -->
Table 3: Linear regression data for the centrographic model, x-direction (longi-

<!-- b000251 | prose | pages [13] -->
tudinal). Hillside data set [19].

<!-- b000252 | prose | pages [13] -->
Victim# ˆay 4 0.000665961218837 5 0.000983419577946 6 0.00105866206185 7 0.000983719311558 8 0.000950274912901 R2 p 1.0 N/A 0.90783947974 0.275461438702 0.93384684203 0.0661531579701 0.935632003161 0.0194133564982 0.943853948827 0.00464007177548

<!-- b000253 | caption | pages [13] -->
Table 4: Linear regression data for the centrographic model, y-direction (lati-

<!-- b000254 | prose | pages [13] -->
tudinal). Hillside data set [19].

<!-- b000255 | heading | pages [13] -->
Rational Serial Criminal Model

<!-- b000256 | prose | pages [13] -->
6.2

<!-- b000257 | prose | pages [13] -->
Like Rossmo’s criminal geographic targeting (CGT) model [32], the RSC model yields a jeopardy surface representing the estimated relative probabilities that the killer lives within each grid cell on a map. For this to be useful, it should allow law enforcement to search for the killer more eﬃciently. We tested our results using Microsoft Excel macros in the same way that Rossmo tested the

<!-- b000258 | furniture | pages [14] -->
Team # 8479

<!-- b000259 | furniture | pages [14] -->
Page 13 of 25

<!-- b000260 | caption | pages [14] -->
Figure 1: Simulation results for the centrographic model with the Hillside Stran-

<!-- b000261 | prose | pages [14] -->
gler data set [4]. The blue points represent the kills used to calculate the cen- troid, centroidal velocity and centroidal acceleration. The red diamond repre- sents the estimated area of next probable event (within one mean distance of the centroid along each axis in each direction). The black point represents the actual location of the next event.

<!-- b000262 | furniture | pages [15] -->
Team # 8479

<!-- b000263 | furniture | pages [15] -->
Page 14 of 25

<!-- b000264 | caption | pages [15] -->
Figure 2: Attack sites, jeopardy surface, and homes of David Berkowitz, the

<!-- b000265 | prose | pages [15] -->
“Son of Sam,” using the Berkowitz data set [24].

<!-- b000266 | prose | pages [15] -->
The ranking of quadrant coloring in order from least probable location to most probable location is: blue, red, green, purple.

<!-- b000267 | prose | pages [15] -->
CGT model: by drawing a box called a “hunting area” around the attack sites, plotting the jeopardy surface based on the attack locations, and then asking the question: if the police were to search every cell in the hunting area in order of highest to lowest on the jeopardy surface, what percentage of the grid would they have to search before they got to the killer? This number is called the Hit Score % [32]. Multiplying this by the size of the hunting area yields the eﬀective search area: the actual area the police would have to search, following the jeopardy surface, before ﬁnding the killer. This method of testing allows the modeler some degree of ﬂexibility, in deciding which locations would have been counted as crime sites and in guessing where the killer would have been found.

<!-- b000268 | prose | pages [15] -->
For David Berkowitz, we ran the RSC model with the locations of the eight shooting incidents attributed to him at the time of his capture [24]. The re- sulting jeopardy surface is shown in Figure 2, with locations of shootings and Berkowitz’s last two residences overlaid. While on most occasions he shot or shot at two people, we counted each shooting only once. Berkowitz lived in the Bronx for several years, near his ﬁrst and sixth crime scenes, but moved to Yonkers before shooting his ﬁrst victims [25]. He later admitted to having stabbed two people near his Bronx home while living there [25], but newspaper accounts from the time [36, 24] show no indication that the stabbings had been connected to his shootings before his arrest. Therefore, we did not include them in our analysis, as their location would not have been available for considera- tion by law enforcement at the time. We computed two scores, one using a grid deﬁned by the crime sites to look for Berkowitz former house in the Bronx, and

<!-- b000269 | furniture | pages [16] -->
Team # 8479

<!-- b000270 | furniture | pages [16] -->
Page 15 of 25

<!-- b000271 | prose | pages [16] -->
one using a grid contrived to include his Yonkers house to ﬁnd him there. The results are tabulated in Table 5.

<!-- b000272 | prose | pages [16] -->
Home Hunting Area 1,414 km2 Bronx

<!-- b000273 | prose | pages [16] -->
2,514 km2 Yonkers

<!-- b000274 | prose | pages [16] -->
Hit Score % Search Area 255 km2 18.1%

<!-- b000275 | prose | pages [16] -->
1,588 km2 63.2%

<!-- b000276 | caption | pages [16] -->
Table 5: Performance of RSC model on data for David Berkowitz [24]

<!-- b000277 | prose | pages [16] -->
In October and November of 1977, the bodies of 11 strangled women were discovered in Los Angeles, and were all believed to be the victims of a single “Hillside Strangler” [19]. Using the exact same parameters and assumptions, we ran the RSC model on the 9 of these locations (two of the bodies were found in the same location, which we only counted once; for one body we could not ﬁnd an exact location of discovery). The resulting jeopardy surface is plotted in Figure 3, and the Hit Score % and accompanying data for the house of one of the two oﬀenders, Angelo Buono, [7] can be found in Table 6.

<!-- b000278 | prose | pages [16] -->
There were two main diﬀerences between this data and the data for the Berkowitz shootings: ﬁrst, these were locations where bodies were found dumped, not locations where killings actually took place.

<!-- b000279 | prose | pages [16] -->
Second, the hunting zone around these bodies, determined by their location, stretched over twice as far North to South as it did East to West, while the Berkowitz hunting zone was essentially square. Nonetheless, the model still performed reasonably well on the Hillside Strangler data without modiﬁcation.

<!-- b000280 | prose | pages [16] -->
To test the predictive powers of the RSC model, we used the jeopardy surface with the ﬁrst six kills from the Berkowitz data set and the modiﬁed utility and cost functions (see Section 3) to try to predict the location of the 7th kill (Figure 4). In this case it doesn’t make sense to use a Hit Score % to analyze accuracy as the killer will not necessarily be stationed at the predicted site during the course of an extended search, but it is evident from the jeopardy surface that the model performed favorably, as the kill occurred in one of the regions of highest probability. Of course, this is just one data point, and a month later Berkowitz shot his ﬁnal victims in Brooklyn: this point would not even have been on our map.

<!-- b000281 | prose | pages [16] -->
Hit Score % Hunting Area 2,721 km2 Search Area 379 km2 13.9%

<!-- b000282 | caption | pages [16] -->
Table 6: Performance of RSC model on data for Buono & Bianchi [19]

<!-- b000283 | furniture | pages [17] -->
Team # 8479

<!-- b000284 | furniture | pages [17] -->
Page 16 of 25

<!-- b000285 | caption | pages [17] -->
Figure 3: Attack sites, jeopardy surface, and home of Angelo Buono [7], one half

<!-- b000286 | prose | pages [17] -->
of the “Hillside Strangler” duo. The ranking of quadrant coloring in order from least probable location to most probable location is: blue, red, green, purple.

<!-- b000287 | caption | pages [17] -->
Figure 4: Prediction results with the RSC model for the 7th Berkowitz kill using

<!-- b000288 | prose | pages [17] -->
the ﬁrst six kills from the Berkowitz data [24] to generate the jeopardy surface. The ranking of quadrant coloring in order from least probable location to most probable location is: blue, red, green, purple. The black point is the actual location.

<!-- b000289 | furniture | pages [18] -->
Team # 8479

<!-- b000290 | furniture | pages [18] -->
Page 17 of 25

<!-- b000291 | prose | pages [18] -->
6.3

<!-- b000292 | heading | pages [18] -->
Combined Models

<!-- b000293 | prose | pages [18] -->
As a brief example of using the RSC model and the Centrographic model in conjunction with each other, we used each model on the DC Sniper data set [2] and graphed the outputs (Figures 5 and 6).

<!-- b000294 | caption | pages [18] -->
Figure 5: Simulation results for the centrographic model with the DC Sniper

<!-- b000295 | prose | pages [18] -->
data [2].

<!-- b000296 | prose | pages [18] -->
The blue points represent the kills used to calculate the centroid, centroidal velocity and centroidal acceleration. The red diamond represents the estimated area of next probable event (within one mean distance of the centroid along each axis in each direction). The black point represents the actual location of the next event.

<!-- b000297 | caption | pages [18] -->
Figure 6: Prediction results with the RSC model for the last DC Sniper kill

<!-- b000298 | prose | pages [18] -->
using the previous kills from the DC Sniper data [2]. The ranking of quadrant coloring in order from least probable location to most probable location is: blue, red, green, purple. The black point is the actual location.

<!-- b000299 | furniture | pages [19] -->
Team # 8479

<!-- b000300 | furniture | pages [19] -->
Page 18 of 25

<!-- b000301 | prose | pages [19] -->
7

<!-- b000302 | heading | pages [19] -->
Discussion

<!-- b000303 | prose | pages [19] -->
Any model of serial killer behavior must be somewhat ad hoc. While Rossmo’s macrolevel serial killer dataset lists 225 cases of serial killers in 9 countries going back to the late nineteenth century, of these, he found only 21 to be suitable for testing his model [31].

<!-- b000304 | prose | pages [19] -->
Looking at the data for the Centrographic model, we see in Figure 1 that the predictions seem to get better over time, meaning that as more data become available the model is becoming more accurate.

<!-- b000305 | prose | pages [19] -->
Indeed, the error distances (Table 2) are decreasing with each additional kill, and the mean error distance is only roughly 15.12 km, a small distance considering the search area was the city of Los Angeles.

<!-- b000306 | prose | pages [19] -->
A key part of the Centrographic model is its use of a linear regression to esti- mate the acceleration, ˆa, which brings up a question of how valid a linear regres- sion on the velocity data actually is. Evident in Table 4, our test demonstrated a high correlation coeﬃcient (≈90% correlation) for the Y-acceleration, ˆay, as well as small p-values for the later crimes, implying that the linear regression is a statistically signiﬁcant model that accounts for a large part of the variation in the data. This indicates the linear regression model to be a mathematically valid approach in this case. However, in the case of the X-acceleration, ˆax (Ta- ble 3), the correlation coeﬃcient was smaller and the p-values larger, yielding a statistically insigniﬁcant model that doesn’t account for a large degree of the variation in the data.

<!-- b000307 | prose | pages [19] -->
The problems with the model’s acceleration approximation illustrate once again the problems with performing statistical analysis on a small data set. Even though the ˆax obtained from regression would seem to account for at least 60% of the data variation, it could just be random chance. If we disregard the question of statistical signiﬁcance for a second and just look at the correlation, however, it’s obvious that the linear model does not seem to be enough in the case of ˆax. This indicates that perhaps it is necessary to reconsider the idea of a linear regression to calculate ˆa—perhaps the idea of a centroidal acceleration of a data set is not entirely conducive to geographical proﬁling, or perhaps even a higher-order regression is necessary, introducing analogues to physical concepts such as jerk (the change in acceleration over time) and jounce (the change in jerk over time)4.

<!-- b000308 | prose | pages [19] -->
The Centrographic model performs well on the data available to us, but more extensive testing is needed to determine its validity. To improve the model, it would be advisable to conduct future research on many more data sets in order to determine appropriate choices of the f(t) and g(t) functions used. A weakness of the model as it stands is its sensitivity to the choice of β, so perhaps our choices of the functions in this simulation were ill-advised. Additionally, the model does not incorporate as much temporal modeling as it could, which could strengthen its predictive powers.

<!-- b000309 | prose | pages [19] -->
The Rational Serial Criminal model performed reasonably well on the data

<!-- b000310 | prose | pages [19] -->
4But maybe this is just silly.

<!-- b000311 | furniture | pages [20] -->
Team # 8479

<!-- b000312 | furniture | pages [20] -->
Page 19 of 25

<!-- b000313 | prose | pages [20] -->
for which we tested it. With the Hillside Strangler data, the Hit Score % of our jeopardy surface for the location of the killers home was only 13.9% (Table 6), meaning only 13.9% of the hunting area would need to be searched before ﬁnding the home of Angelo Buono, a vast reduction. With our choice of probability density function k, the RSC model made predictions qualitatively similar to those made by the CGT model [31]. In the case of the Berkowitz data, however, the Hit Score % for our prediction for ﬁnding Berkowitz’s home at the time of the murders was only 63.2% (Table 5)—worse than random chance. This is due to the fact that shortly before the murders took place Berkowitz moved his place of residence. Using Berkowitz’s old home, the RSC model yields a Hit Score % of 18.1%, a much more reasonable ﬁgure.

<!-- b000314 | prose | pages [20] -->
Conducting a χ2 goodness of ﬁt test of the Hit Score % from the three tests against the uniform probability density function implied that the data are not uniformly distributed at the 95% level of signiﬁcance. This implies that the RSC model developed is statistically superior to a random search method for the location of the murderer’s home.

<!-- b000315 | prose | pages [20] -->
The RSC model’s performance in our tests was hampered by a few simpli- fying assumptions we made:

<!-- b000316 | prose | pages [20] -->
• We assumed the initial probability distribution over the hunting area for the location of a serial killer’s home was uniform.

<!-- b000317 | prose | pages [20] -->
• We assumed the initial probability distribution over the hunting area for the location of a murder was uniform.

<!-- b000318 | prose | pages [20] -->
Obviously, as in the case of the Berkowitz data, this is not always the case— half of the area included in our simulation was underwater, indicating zero probability of the killer’s home being in that area, and zero probability of the next kill occurring in much of that area5. To improve the RSC model, it is possible to modify the initial guess of the probability distribution for both of these cases based on simple factors such as population density or geographic landmarks (ie, lakes and harbors).

<!-- b000319 | prose | pages [20] -->
The real strength of our Rational Serial Criminal model is its theoretical indiﬀerence to the choice of utility function. This means that it can be adapted to the pursuit of almost any serial criminal. Besides the well-documented ten- dency for criminals to act locally, police investigating a particular fugitive may have any number of other ideas about the crook’s preferences. If they can write these down as functions, the RSC model can help them as they develop a search plan based on their evidence and intuition. Since one might reasonably consider a group engaged in organized crime to be a single agent, one could also use the RSC model to investigate gang behavior, for example.

<!-- b000320 | prose | pages [20] -->
Independent of any speciﬁc investigation, we could improve the RSC model signiﬁcantly by putting other common themes and population trends [28] about crime sites into functional form. For instance, criminals tend to prefer to act in areas which are like the areas they are familiar with [23]. If we included zoning

<!-- b000321 | prose | pages [20] -->
5Disregarding serial criminals with ﬁshing boats or scuba certiﬁcation.

<!-- b000322 | furniture | pages [21] -->
Team # 8479

<!-- b000323 | furniture | pages [21] -->
Page 20 of 25

<!-- b000324 | prose | pages [21] -->
and demographic data in our grid, we could include a term in the k function which operationalizes this prediction. We could also change the meaning of p to include more sophisticated information about the victims, so that we could model a criminal who tended to ﬁnd his victims in a particular region but then assaulted them or disposed of their bodies in more diverse locations [13]. This could augment the current method of using GIS software to determine how several victims’ daily lives might have led them to interact with a killer, and from this information determining areas where the killer might spend a lot of time [37].

<!-- b000325 | prose | pages [21] -->
In Figures 5 and 6 we see the results of running both the RSC and Centro- graphic model on the DC Sniper data set. Using both methods generates two zones each with theoretically high probability of encounter with the serial killer in question. Looking at the graphs, we see that the models did not predict the actual crime site. This can be explained by the nature of the data. In the RSC model case, there is a crime site in the same location of a previous crime site. This violates the assumptions of the model. In the centrographic model, the killer took an unexpected turn south, resulting in a crime site far from any of the others. Both of the problems above stem from the size of the hunting area for the DC Sniper, which contains large areas of Maryland and parts of Virginia. This, however, is simply a characteristic of the DC Sniper data that makes it diﬃcult to make predictions regarding his actions in general. Additionally, the DC Sniper data diﬀers from the other sets in that many of the kills took place on the same day at diﬀerent times, making some of the calculations involved in the centrographic model diﬃcult or nonsensical (ie, predicting inﬁnite velocity). With a more accurate data set (to the time of day, for example) it is possible the model would perform better.

<!-- b000326 | prose | pages [21] -->
To improve the way the models work together, a number of possible adapta- tions could be made in future models. As the RSC is a resource-intense method, it is possible that using it for a large area with a ﬁne enough quadrant resolution could be simply too slow. Since the Centrographic model theoretically narrows down the search window, it could be useful to consider using a variable quadrant resolution when analyzing large areas, where the resolution outside the area pre- dicted by the Centrographic model is larger than that inside, yielding a faster runtime while still providing a high level of accuracy in high probability areas. Using the models in the other direction, probability data from the RSC model could be used to create a sort of resistance to the motion of the centroid in the Centrographic model to cause it to stay near regions of higher probability.

<!-- b000327 | prose | pages [21] -->
Overall, this model provides a starting point for a police search. It is meant to be another tool to the police, to give a general guideline of where to allocate police sources when very few data are available. In reality, police experience is impossible to replace with any kind of mathematical method, and when dealing with a subject as unpredictable as a serial murderer, experience is necessary to determine the most eﬃcient way to catch the killer.

<!-- b000328 | furniture | pages [22] -->
Team # 8479

<!-- b000329 | furniture | pages [22] -->
Page 21 of 25

<!-- b000330 | prose | pages [22] -->
8

<!-- b000331 | heading | pages [22] -->
Executive Summary

<!-- b000332 | prose | pages [22] -->
This method is a computer program that takes crime site (either body disposal site or scene of the crime) data in absolute coordinates and returns a prediction of the oﬀender’s residence and a prediction of the next crime site. This should be used for two things: to narrow the search for the oﬀender in his daily routine and to narrow the search for the next crime site. It is possible that, after discovering a crime site, that there is another crime site in a location that has not yet been discovered. Furthermore, a search that starts in the most probable area and radiates from this center is more likely to ﬁnd the oﬀender’s residence, or next crime site, than a random search would [32]. The method will provide a starting point and an area for a police force to concentrate the eﬀorts of determining both the location of an oﬀender and where the next crime site might be.

<!-- b000333 | prose | pages [22] -->
In employing the method, the police force makes the same assumptions that are involved with developing the program. The assumptions made are:

<!-- b000334 | prose | pages [22] -->
• The series will occur in an area that the oﬀender is familiar with, meaning a place where he lives, has lived, or has committed crimes before.

<!-- b000335 | prose | pages [22] -->
• The most probable location of the next crime site can change with time, even without new data being acquired regarding former sites in the series.

<!-- b000336 | prose | pages [22] -->
• The order and time at which former crime sites occur aﬀects the location of the predicted next crime site in the series.

<!-- b000337 | prose | pages [22] -->
• Given no crime site data, the oﬀender is equally likely to live or commit a crime at any location.

<!-- b000338 | prose | pages [22] -->
In using the program to predict the oﬀender’s home, it is assumed that the oﬀender has a home base within or close to the crime site, as opposed to com- muting to the area of the crime site. This assumption can be relaxed when predicting where the next crime site might be, as this prediction is made solely on earlier crime site data and thus does not oﬀer additional information. An example of when the method would not apply is when an oﬀender picks up prostitutes in a red light district in order to kill them. If, as in the John Wayne Gacy Jr. case, the crime sites all share a location the model will not apply as no usable predictions could be gleaned from that data.

<!-- b000339 | prose | pages [22] -->
The program utilizes two diﬀerent types of models to make predictions, a centrographic model and a rational choice model. The centrographic model has an analogy in physics, where the crime sites are treated as point masses in a system, and the “centroid” is determined by ﬁnding the center of mass of the system. From this model is output a graph that includes the points of the crime sites and a diamond. Within the diamond lies the prediction for the next crime site. The rational choice model has an analogy in economics. This model uses the idea that the oﬀender is deciding the location of the crime site in order to satisfy his personal goals (mostly of committing another crime) and to minimize his risk of being caught. Thus, it is assumed that the series will continue and that there will not be two crime sites in the same location. There are two types

<!-- b000340 | furniture | pages [23] -->
Team # 8479

<!-- b000341 | furniture | pages [23] -->
Page 22 of 25

<!-- b000342 | prose | pages [23] -->
of this model included in the program, one that predicts where the oﬀender lives and the other predicts the location of the next crime site. In both cases, the model outputs a contour plot. In the two cases, the peaks correspond to either high probability of the oﬀender’s home base and to the location of the next crime site, respectively. There will always be a valley at the location of a previous crime site. Then, when determining where to search for the next crime site, the contour plot from the rational choice model and the plot from the centrographic model can be utilized in conjunction to narrow the initial search area. A key item to note is that the centrographic model makes use of a parameter, β, that is determined by the data of known crime times and must be ¯t derived individually for each serial killer. An example value might be β = ln 15, where ¯t is the mean time between crimes.

<!-- b000343 | prose | pages [23] -->
The method will always output graphs that can be used to begin a police search, but as it is a computerized process, it only responds to the data set provided. Thus, there is an element of subjectivity in determining which crime sites in a given case are useful for predictions [32]. When predicting where the oﬀender lives, the following should be used as a guideline for inputting crime site data:

<!-- b000344 | prose | pages [23] -->
• A minimum of ﬁve crime sites should be used in order to provide a basis for the prediction. Certainly, the program will work with as few as three crime sites, but will not serve to improve the search area greatly. Furthermore, when invoking the program, one assumes that the oﬀender has not changed the home base since the series began. Else, more crime sites are necessary to determine a valid prediction.

<!-- b000345 | prose | pages [23] -->
• Only crime sites that are accurately known should be input to the pro- gram. For example, using data determined from victims acquaintances as to where the victim was last seen to determine where the oﬀender might have met the victim should not be counted as valid input.

<!-- b000346 | prose | pages [23] -->
• If it is clear that two crime sites relate to the same crime (i.e. a site is found where the oﬀender killed the victim, but the body disposal site in a diﬀerent location) one or the other location should be input in to the model, in accordance with the other crime sites [32].

<!-- b000347 | prose | pages [23] -->
When predicting the location of the next crime site the previous also apply, though several crime sites in the same area at diﬀerent points in time might be considered as several diﬀerent sites, as this might be an indication of where the oﬀender’s next act in the series might occur.

<!-- b000348 | prose | pages [23] -->
One of the most powerful tools to be incorporated alongside this program is a GIS mapping software. Using such software will retain perspective of the crime site data when considering the predictions set forth from the program. Furthermore, the program does not account for any sort of victim data that might be gathered during the investigation. Considering these two additional elements will lead to more eﬃcient searches.

<!-- b000349 | furniture | pages [24] -->
Team # 8479

<!-- b000350 | furniture | pages [24] -->
Page 23 of 25

<!-- b000351 | heading | pages [24] -->
References

<!-- b000352 | references | pages [24] -->
[1] Case File - David Berkowitz.

<!-- b000353 | references | pages [24] -->
http://www.fortunecity.com/roswell/streiber/273/berkowitz cf.htm.

<!-- b000354 | references | pages [24] -->
[2] Wikipedia: Beltway sniper attacks.

<!-- b000355 | references | pages [24] -->
http://en.wikipedia.org/wiki/Beltway sniper attacks.

<!-- b000356 | references | pages [24] -->
[3] Wikipedia: David Berkowitz.

<!-- b000357 | references | pages [24] -->
http://en.wikipedia.org/wiki/David Berkowitz.

<!-- b000358 | references | pages [24] -->
[4] Wikipedia: Hillside Strangler.

<!-- b000359 | references | pages [24] -->
http://en.wikipedia.org/wiki/Hillside Strangler.

<!-- b000360 | references | pages [24] -->
[5] AP, Rochester Jury Convicts Parolee in Serial Killings, The New York

<!-- b000361 | references | pages [24] -->
Times, (14 Dec 1990), p. B2.

<!-- b000362 | references | pages [24] -->
[6] G. S. Becker, Crime and punishment: An economic approach, The Jour-

<!-- b000363 | references | pages [24] -->
nal of Political Economy, 76 (1968), pp. 169–217.

<!-- b000364 | references | pages [24] -->
[7] J. Boren, The Hillside Strangler Trial, Loy. LAL Rev., 33 (2000), pp. 707–

<!-- b000365 | references | pages [24] -->
1849.

<!-- b000366 | references | pages [24] -->
[8] K. J. Bowers, S. D. Johnson, and K. Pease, Prospective Hot-Spotting,

<!-- b000367 | references | pages [24] -->
British Journal of Criminology, 44 (2004), pp. 641–658.

<!-- b000368 | references | pages [24] -->
[9] D. Canter, T. Coffey, M. Huntley, and C. Missen, Predicting serial

<!-- b000369 | references | pages [24] -->
killers’ home base using a decision support system, Journal of Quantitative

<!-- b000370 | references | pages [24] -->
Criminology, 16 (2000), pp. 457–478.

<!-- b000371 | references | pages [24] -->
[10] S. Chainey and J. Ratcliffe, GIS and Crime Mapping.

<!-- b000372 | references | pages [24] -->
[11] Concrete Blonde, Scene of a perfect crime, in Recollection, Capitol,

<!-- b000373 | references | pages [24] -->
1996.

<!-- b000374 | references | pages [24] -->
[12] D. B. Cornish and R. V. Clarke, eds., The Reasoning Criminal, New

<!-- b000375 | references | pages [24] -->
York: Springer-Verlag, 1986.

<!-- b000376 | references | pages [24] -->
[13] C. Daniell, Geographic proﬁling in an operational setting: the challenges

<!-- b000377 | references | pages [24] -->
and practical considerations, with reference to a series of sexual assaults in

<!-- b000378 | references | pages [24] -->
bath, england, in Crime Mapping Case Studies, S. Chainey and L. Thomp-

<!-- b000379 | references | pages [24] -->
son, eds., Chichester: John Wiley & Sons, 2008.

<!-- b000380 | references | pages [24] -->
[14] F. Dostoevsky, Crime and Punishment, 1866.

<!-- b000381 | references | pages [24] -->
[15] R. Gibbons, Game Theory for Applied Economists, Princeton: Princeton

<!-- b000382 | references | pages [24] -->
University Press, 1992.

<!-- b000383 | references | pages [24] -->
[16] T. Hirschi, Rational choice and social control theories of crime, in The

<!-- b000384 | references | pages [24] -->
Reasoning Criminal, D. B. Cornish and R. V. Clarke, eds., New York:

<!-- b000385 | references | pages [24] -->
Springer-Verlag, 1986.

<!-- b000386 | furniture | pages [25] -->
Team # 8479

<!-- b000387 | furniture | pages [25] -->
Page 24 of 25

<!-- b000388 | references | pages [25] -->
[17] H. S. Houthakker, Revealed preference and the utility function, Econom-

<!-- b000389 | references | pages [25] -->
ica, 17 (1950), pp. 159–174.

<!-- b000390 | references | pages [25] -->
[18] T. Johnson, E. Porterfield, V. Ho, and H. Castro, Victims’ fam-

<!-- b000391 | references | pages [25] -->
ilies face Green River Killer in court, Seattle-Post Intelligencer, (19 Dec

<!-- b000392 | references | pages [25] -->
2003).

<!-- b000393 | references | pages [25] -->
[19] J. Jones, Body of Woman Found in Brush, Los Angeles Times, (14 Nov

<!-- b000394 | references | pages [25] -->
1977), p. A1.

<!-- b000395 | references | pages [25] -->
[20] D. Kahneman and A. Tversky, Prospect theory: An analysis of decision

<!-- b000396 | references | pages [25] -->
under risk, Econometrica, 47 (1979), pp. 263–291.

<!-- b000397 | references | pages [25] -->
[21] J. L. Lebeau, The Methods and Measures of Centrography and the Spatial

<!-- b000398 | references | pages [25] -->
Dynamics of Rape, Journal of Quantitative Criminology, 3 (1987).

<!-- b000399 | references | pages [25] -->
[22] N. Levine, Crime mapping and the crimestat program, Geographical Anal-

<!-- b000400 | references | pages [25] -->
ysis, 38 (2006), pp. 41–56.

<!-- b000401 | references | pages [25] -->
[23] S. Lundrigan and D. Canter, Spatial Patterns of Serial Murder: An

<!-- b000402 | references | pages [25] -->
Analysis of Disposal Site Location Choice, Behavioral Sciences and the Law,

<!-- b000403 | references | pages [25] -->
19 (2001), pp. 595–610.

<!-- b000404 | references | pages [25] -->
[24] R. D. McFadden, .44 Killer wounds 12th and 13th victims, The New

<!-- b000405 | references | pages [25] -->
York Times, (1 Aug 1977), p. 45.

<!-- b000406 | references | pages [25] -->
[25] C.

<!-- b000407 | references | pages [25] -->
Montaldo,

<!-- b000408 | references | pages [25] -->
David

<!-- b000409 | references | pages [25] -->
berkowitz

<!-- b000410 | references | pages [25] -->
-

<!-- b000411 | references | pages [25] -->
the

<!-- b000412 | references | pages [25] -->
son

<!-- b000413 | references | pages [25] -->
of

<!-- b000414 | references | pages [25] -->
sam.

<!-- b000415 | references | pages [25] -->
http://crime.about.com/od/murder/p/sonofsam.htm, 2010.

<!-- b000416 | references | pages [25] -->
[26] S. P. Morse, Converting addresses to/from latitude/longitude in one step,

<!-- b000417 | references | pages [25] -->
2004.

<!-- b000418 | references | pages [25] -->
[27] F. B. of Investigation, Serial killers in the United States, 1960 to

<!-- b000419 | references | pages [25] -->
present, 2003.

<!-- b000420 | references | pages [25] -->
[28] D. O’Sullivan and D. J. Unwin, Geographic Information Analysis, John

<!-- b000421 | references | pages [25] -->
Wiley & Sons, Ltd. Chichester, UK, 2003.

<!-- b000422 | references | pages [25] -->
[29] A. R. Piquero and S. G. Tibbetts, eds., Rational Choice and Criminal

<!-- b000423 | references | pages [25] -->
Behavior, New York: Routledge, 2002.

<!-- b000424 | references | pages [25] -->
[30] D. Ross, Integrating the dynamics of multi-scale agency, in The Oxford

<!-- b000425 | references | pages [25] -->
Handbook of Philosophy of Economics, D. Ross and H. Kincaid, eds., New

<!-- b000426 | references | pages [25] -->
York: Oxford University Press, 2009.

<!-- b000427 | references | pages [25] -->
[31] D. K. Rossmo, Geographic Proﬁling: Target Patterns of Serial Murderers,

<!-- b000428 | references | pages [25] -->
PhD thesis, Simon Fraser University, 1995.

<!-- b000429 | references | pages [25] -->
[32] D. K. Rossmo, Geographic Proﬁling, Boca Raton: CRC Press, 2000.

<!-- b000430 | furniture | pages [26] -->
Team # 8479

<!-- b000431 | furniture | pages [26] -->
Page 25 of 25

<!-- b000432 | references | pages [26] -->
[33] D. K. Rossmo and L. Velarde, Geographic proﬁling analysis: prin-

<!-- b000433 | references | pages [26] -->
ciples,

<!-- b000434 | references | pages [26] -->
methods,

<!-- b000435 | references | pages [26] -->
and applications,

<!-- b000436 | references | pages [26] -->
in Crime Mapping Case Studies,

<!-- b000437 | references | pages [26] -->
S. Chainey and L. Thompson, eds., Chichester: John Wiley & Sons, 2008.

<!-- b000438 | references | pages [26] -->
[34] P. A. Samuelson, Foundations of Economic Analysis, Cambridge: Har-

<!-- b000439 | references | pages [26] -->
vard University Press, 1947.

<!-- b000440 | references | pages [26] -->
[35] P. Schmidt and A. D. Witte, An Economic Analysis of Crime and

<!-- b000441 | references | pages [26] -->
Justice, Orlando: Academic Press, 1984.

<!-- b000442 | references | pages [26] -->
[36] M. Schumach, 3 Murders of women since July 29 believed actions of same

<!-- b000443 | references | pages [26] -->
gunman, The New York Times, (11 Mar 1977), p. 83.

<!-- b000444 | references | pages [26] -->
[37] C. Shamblin, An application of geographic information systems (GIS): the

<!-- b000445 | references | pages [26] -->
utility of victim activity spaces in the geographic proﬁling of serial killers,

<!-- b000446 | references | pages [26] -->
Master’s thesis, Louisiana State University, 2004.

<!-- b000447 | references | pages [26] -->
[38] B. Snook, R. Cullen, A. Mokros, and S. Harbort, Serial murderers

<!-- b000448 | references | pages [26] -->
spatial decisions: Factors that inﬂuence crime location choice, Journal of

<!-- b000449 | references | pages [26] -->
Investigative Psychology and Oﬀender Proﬁling, 2 (2005).

<!-- b000450 | references | pages [26] -->
[39] M. Tonkin, J. Woodhams, and J. W. Bond, A theoretical and practical

<!-- b000451 | references | pages [26] -->
test of geographical proﬁling with serial vehicle theft in a U.K. context,

<!-- b000452 | references | pages [26] -->
Behavioral Sciences the Law, (2009).

<!-- b000453 | references | pages [26] -->
[40] J. von Neumann and O. Morgerstern, Theory of Games and Eco-

<!-- b000454 | references | pages [26] -->
nomic Behavior, Princeton: Princeton University Press, 1944.
