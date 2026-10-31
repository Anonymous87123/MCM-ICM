A killer is at large, and the police need our help! Lovers of mystery ﬁction might jump at the chance to engage in a hot pursuit of forensic clues and shady characters, but our reality is not so glamorous. Our task: given a set of crime site locations and times, narrow down a killer’s location and try to predict where the next murder might be.

We present two mathematical models to assist in the investigation. The models take the locations of previous crime sites and the times that they occurred as variables. These data are few compared to the seemingly inﬁnite possibilities of the criminal’s actions, but we know at least one thing: the criminal will do his best to avoid being caught. We infer then, in accordance with past research, that he will kill where he knows the surroundings. This motivates the assumption that the killer is more likely to kill closer to his home or to places where he has killed before. We further assume that the future locations of attacks depend only on the location of the killer’s home and the location and relative time of past crimes.

The ﬁrst of the two models, the Centrographic model, builds upon earlier work by LeBeau. It uses an analogy to kinematics to derive the location and movement of the “centroid” of a series of crime sites. We consider the change in the location of the centroid over time to predict future crime site locations. In other words, we model the series to have a “velocity” and “momentum” and use this information to predict the future location of the centroid.

Our second model, the Rational Serial Criminal model, uses methods from microeconomic theory to model the criminal as a rational agent. This model formalizes the process of looking at a series of crime locations and assessing where the criminal prefers to ﬁnd victims or dump bodies. Using data on a series of crimes, the model outputs contour surfaces representing areas where the killer is more or less likely to live. From here, we extend the model to predict where a killer is likely to strike next.

We run simulations on crime site data for diﬀerent serial killers and compare our location predictions to the actual next kill in the series. The centrographic model performs well as measured by the error distance. Unfortunately, the model is sensitive to a parameter that must be determined for each individual series. The rational choice model also performs well predicting home location as measured by the Hit Score %, a metric which compares the eﬃciency of a search informed by prediction to a random search.

Our model could be another useful tool for police chasing a serial killer. While we do not incorporate data such as population density or geographic features, we believe that police oﬃcers will have no trouble ﬁlling in these gaps. The model provides a good starting point when data are too few to utilize more complex methods.

1 From Kills to Kilometers Using Centrographic Techniques and Rational Choice Theory for Geographical Proﬁling of Serial Killers

Abstract

We present two mathematical models to assist in the investigation of a serial killer. The models take the locations of previous crime sites and the order that they occurred as variables. These data are few compared to the seemingly inﬁnite possibilities of the criminal’s actions, but at least one thing is known: the criminal will do his best to avoid being caught. We infer then, in accordance with past research, that he will kill where he knows the surroundings. This motivates the assumption that the killer is more likely to kill closer to his home or places he has killed before. We further assume that the future locations of attacks depend only on the location of the killer’s home and the location and relative time of past crimes.

The ﬁrst of the two models, the “centrographic” model, builds upon earlier work by LeBeau. It uses an analogy to kinematics to derive the location and movement of the “centroid” of a series of crime sites. We consider the change in the location of the centroid over time to predict future crime site locations. In other words, we model the series to have a “velocity” and “momentum” and use this information to predict the future location of the centroid.

Our second model, the Rational Serial Criminal model, uses methods from microeconomic theory to model the criminal as a rational agent. This model formalizes the process of looking at a series of crime locations and assessing where the criminal prefers to ﬁnd victims or dump bodies. Using data on a series of crimes, the model outputs contoured surfaces representing areas where the killer is more or less likely to live. From here, we extend the model to predict where a killer is likely to strike next.

We run simulations on crime site data for diﬀerent serial killers and compare our location predictions to the actual next kill in the series. The centrographic model performs well as measured by the error distance. Un- fortunately, the model is sensitive to a parameter that must be determined for each individual series. The rational choice model also performs well predicting home location as measured by the Hit Score %, a metric which compares the eﬃciency of a search informed by prediction to a random search.

1 Introduction

When a serial killer is on the prowl 1, the police deploy every available resource to stop the killings and bring the murderer to justice. Serial killers provide an interesting challenge to geographic proﬁlers, due to the relative paucity of data on these criminals and their unique geographic behavior. Statistical prediction methods in widespread use for other types of serial crimes such as burglaries [8] or auto thefts [39] are less useful for ﬁnding serial killers, as these methods rely on a large initial data set to generate predictions.

We attempt to predict a serial killer’s future behavior and location data on their crime sites and initial assumptions about their behavior. In Section 3, we adapt two complementary models to predict future crime sites and point to the location of a serial killer’s anchor point [32].

We tested our models by implementing each one in a computer simulation, and running them on partial data sets from two historical serial killers. We describe our data collection process and provide examples in Section 5. We compared our models’ predictions for the locations of later crimes to the actual locations where later crimes in each series occurred. We describe the results of these simulations in Section 6. Finally, in Section 7, we note some shortcomings of our approach and propose directions for further research.

2 Background Information

2.1 Serial Killing

The FBI deﬁnes serial murder as three or more killings with “cooling-oﬀ” periods in between [32, 27]. Experience shows that the behavior of such serial criminals follows some predictable patterns. Speciﬁcally, serial killers tend to operate near their homes, in areas with which they are familiar [32]. For example, one study of 126 U.S. serial killers found that 89% of them lived within a circle drawn around the locations where they disposed of bodies [23]. The inclination of a serial killer to work close to a home base or anchor point [32] often leads to a spatial clustering of their crime sites. Therefore, by looking at the geographic locations of crimes, we can say something about where the criminal who committed them is likely to live or might strike next.

In the past two decades, “geographical proﬁling” has exploded, and many law-enforcement agencies now use spatial modeling techniques in the pursuit of serial criminals [33]. The most popular approach includes the assumption that the criminal lives near his crime scenes, and has not moved place of residence since the crime spree began [32, 33].

1During such an investigation, even if the same modus operandi is followed, the police might not acknowledge a series of crimes as being the work of one person. Thus, one might be inclined to refer to this suspect as an alleged serial killer for precision. For the duration of this paper, we will assume that all such series are the work of one person, and will drop the “alleged”.

2.2 Previous Work

At ﬁrst blush, criminals seem diﬃcult, if not impossible, to predict. The crimi- nal, however, must follow some sort of thought process in order to commit his acts and, as such, “crime pattern theory combines rational choice, routine activ- ity theory, and environmental principles to explain the distribution of crimes” [32]. From these ideas, geographical proﬁling was developed. When analyzing serial crimes, few data are available other than that at the crime scene and dis- posal site of the body. This motivates Lundrigan and Canter’s research into a serial killer’s disposal site location choice, which statistically analyzed data on apprehended serial killers to determine how a killer’s home location related to his body disposal sites [23]. Many factors can inﬂuence the serial killer’s disposal site selection. In a study conducted in Germany, the median distance between the disposal site and the killer’s home decreased as age of killer increased, a killer’s higher IQ corresponds to a further distance of disposal site from the home base, though the number of murders and distance between a killer’s home and disposal site was not statistically signiﬁcant [38].

Another method of determining the location of a serial killer is to consider the daily routines of the victims. Geographic proﬁlers can use mapping soft- ware to determine where victims’ routines overlap, and these locations can be interpreted as places where the killer might have seen the victims. These data, in turn, can be used to hypothesize the killer’s daily whereabouts [37]. In an age where most people are connected to the rest of the world through cellular telephones and internet, it is possible now more than ever to gather objective data regarding where a person was at a certain time.

In modeling serial crime, a primary concern of geographical proﬁling is the prediction of areas at high risk of future crime, known colloquially as crime “hotspots”. Past models for geographical proﬁling of serial oﬀenders have shown varying results. Due to the nature of serial crimes as discrete events, the ma- jority of methods for displaying and analyzing data on serial criminals utilize a technique known as point mapping [10]. A problem with simple point mapping, however, as described by Chainey et al., is that “it is diﬃcult to clearly iden- tify the location, relative scale, size and shape of hotspots when crime data are presented as points”. As such, it becomes necessary to ﬁnd alternate methods of display and analysis.

3 Models

3.1 A Centrographic Model

3.1.1 Background

A standard analytical measure in the geographical proﬁling toolbox is the spa- tial mean of point data, obtained by summing the geographic coordinates over all observations independently in each spatial dimension and dividing by the to- tal number of observations [32]. This eﬀectively generates a ‘center’ to the data set that can be used in conjunction with other methods to describe the concen- tration of a distribution. A long-utilized and relatively simple tool, the spatial mean remains in widespread use today in geographical proﬁling due to its ease of use. Despite the simplicity of calculation, previous studies have shown the spatial mean to perform comparably to alternative, more complex algorithms and even human judgment [39].

One drawback to the spatial mean is that it doesn’t intrinsically use time to describe and forecast an evolving distribution such as is seen with serial killings. To utilize the temporal aspect of such a data set, we must extend the model. One extension that arises naturally is to consider the change in the spatial mean over time [21]. Previous work has used analogy to simple physical phenomenon to come up with parallels to velocity (change in position over time), acceleration (change in velocity over time), and momentum (the product of velocity and mass) [32, 21]. In this model we will use several of these concepts to come up with a method of predicting the locations of future kills or crimes in a spree.

3.1.2 Assumptions

To justify a centrographic approach to geographical proﬁling, a few assumptions must be made regarding the behavior of serial killers:

• A serial killer is more likely to kill in an area he’s familiar with, (i. e., a place he lives near or has killed near before.)

• The distribution of probable locations of next kill changes with time, even if the distribution of known kills does not.

• The order in which and time at which kill events in a distribution occur are a factor in determining probable locations of next kill, not just the spatial location.

3.1.3 Model

Deﬁne XKj to be the position vector corresponding to the site of the j-th observed crime, Kj. If we consider the reach or area of activity of a serial killer to be represented by the distribution of the observed events, we can deﬁne the ‘center of mass’ or centroid of the area of activity at the time of the of the j-th event, Cj, to be the geographic mean of XK1 . . . XKj,

j XKi X Cj = j i=1

Utilizing this, a reasonable estimate for a probable area of future encounter with the criminal, A, can be obtained by ﬁnding the mean distance from Cj to each event Ki in each spatial direction and deﬁning A to be the area within the polygon formed by extending from the mean this distance in each corresponding direction.

Since Cj is a spatial location that changes with time, it is natural to calculate the change in position per unit time—the geographic analogue of the velocity of C at the time of the j-th event, tj [32],

VCj = dCj dt ,

as well as an analogue of the ‘linear momentum’ of C at time tj [21],

PCj = jVCj,

where the ‘mass’ of the distribution is equal to the current number of serial events, j.

The concept of linear momentum PCj is important to our model as it allows for a mathematical analysis of the spatial direction in which the kill spree seems to be moving, relating PCj to PCj−1 by considering the law of conservation of momentum. We deﬁne the velocity of serial event Kj as the distance between event Kj and the previous centroid divided by the time between event Kj and Kj−1 VKj = XKj −Cj−1 . tj −tj−1 It follows from the deﬁnition of mass above that the mass of a single event is 1, and thus the momentum of a single event Kj is equal to its velocity,

PKj = VKj.

Modeling the state of Cj at time tj as the result of a completely inelastic collision between Cj−1 and Kj (i.e., Kj is absorbed and joins Cj−1 to form Cj), conservation of momentum tells us that

PCj = jVCj = PCj−1 + PKj = (j −1)VCj−1 + VKj,

or, VCj = (j −1)VCj−1 + VKj , j where it follows trivially that VC1 = 0, which follows expectations for a spree consisting of only one kill (non-serial).

To make a prediction for the next kill site in a series Kj+1, we can incorporate both the current centroid Cn and the current velocity of the centroid VCj by deﬁning A(t) as the polygon A as deﬁned above with a center dependent on time according to VCn,

CenterA(t) = Cj + f(t)VCj + g(t)ˆaj, where ˆaj is an estimate of the acceleration of Cj based on a linear regression of velocity data obtained from K1 . . . Kj and f(t) and g(t) are parameter coeﬃ- cients chosen to match the constraints:

d(CenterA(t)) lim = 0 (1) dt t→∞ f(t) ≈tfor t < ¯t (2) g(t) ≈t2/2for t < ¯t (3)

where ¯t is the mean time between Ki’s.

Constraint 1 is necessary to keep our prediction reasonably centered on the observed events over long spans of time, and conditions 2 and 3 are necessary for the kinematic analogue. One possible choice of f(t) and g(t) explored in this paper is 2t2 2t f(t) = 1 + eβt , g(t) = (1 + eβt)2

for some real constant β > 0.

Note that the ﬁnal model yields a prediction A(t) that is a function of time, consistent with our assumption of an evolving killer. To get a general prediction, it is possible to evaluate A(¯t), yielding the prediction for where the next kill will occur should it happen after the mean time ¯t.

3.2 A Rational Choice Model

3.2.1 Background

A number of criminologists have suggested that much criminal behavior can be modeled as rational choices made by agents who derive some utility from their crimes [6, 12, 29]. On one hand, criminal activity has historically been seen as defying rationality [12]. If we grant, however, that a given rapist, burglar, or other criminal will rape, burglarize, or otherwise break the law, then their choices of whom to rape or which houses to burglarize may appear rational [16], and may in fact be the result of much planning and deliberation. This makes rational choice theory as implemented in economics particularly well-suited for our purpose here of looking at a collection of crimes to draw inferences about the criminal’s future behavior.

Previous studies have applied economic theory to criminology by using Ex- pected Utility Theory [40] and Prospect Theory [20] to model a criminal who weighs the beneﬁts to himself of committing a crime against the odds of getting caught and its associated harm. While our model here is based on the idea from microeconomics of using observed revealed preference data to make inferences about unobserved preferences [34], it does not resemble a traditional economic model so nearly as do these earlier works.

The microeconomic model seeks to make predictions about the responses of dependent variables (such as quantities consumed of various goods) to possible future values of independent variables (such as prices) based on past obser- vations of both [34]. In this model, the agent selects a bundle of goods to purchase by assigning quantities to each available good; these quantities form a consumption vector. In our model, the agent assigns probabilities to each possible location for his next crime, forming a probability vector. The economic agent faces a scalar budget and a vector of prices. The dot-product of her cho- sen consumption vector and the environmental price vector must not exceed her budget. She is assumed to maintain a consistent ranking of all possible consumption bundles. For our criminal agent, the analogue of price is perceived risk of getting caught if he commits his next crime in a given location. While we cannot observe this the same way that we observe prices, it is analogous in that it diﬀers across observations, since we expect the risks of getting caught in various locations to change each time the criminal acts (due to increased public awareness or police presence, e.g.). His (unrelated) constraint is that the en- tries in his probability vector must sum to 1. Rather than ranking consumption bundles, he ranks probability distributions.

Choosing a probability distribution as a means of agency has precedent in the notion of a mixed strategy in game theory [15]. We believe this reﬂects the nature of the actual choices the criminal makes, particularly about location. Geographical proﬁling expert D. Kim Rossmo notes that “for a direct-contact predatory crime to occur, the paths of the oﬀender and victim must intersect in time and space, within an environment appropriate for criminal activity.” [32]. Since the criminal cannot signiﬁcantly control the ﬂow of potential victims or the suitability of diﬀerent locations, he does not have complete control over where and when he breaks the law. Rather, when he walks down a particular street, he is choosing to increase the probability that he will commit his next crime there.

Since a rational agent must have consistent preferences, if our serial criminal is to evolve, then each crime must change his incentive structure. We model this by including a perceived extra risk of capture at any given potential target as a function of the locations of previous acts: you can never go back to the scene of a perfect crime [11]. Since the overall risk of getting caught should already be a signiﬁcant factor in the agent’s preference for one crime scene over another, it is only this additional risk which we call analogous to price.2 When we talk about a “rational serial criminal”, we do not mean to suggest that there are good reasons for committing series of crimes.3 We merely hy- pothesize that by assuming this series of crimes to be determined by a consistent preference ﬁeld [30], we may make useful predictions about the criminal. Ad- ditionally, when we talk about “utility” as a function of the probability vector described above, we do not mean to imply that committing crimes fulﬁlls some desire of the criminal’s to a variable extent depending on where he does it. The

2One could argue that a fully rational criminal adding up the costs of committing a crime at a particular place would consider the loss in welfare he would experience when it became riskier for him to commit other crimes there in the future. While technically true, we do not consider this point relevant to our analysis, or at all.

3But nor do we deny it.

utility function is just a convenient mathematical tool, which is equivalent to making direct inferences from revealed preference [17].

To summarize, we construct a model of a rational serial criminal who controls his behavior by determining a probability distribution deﬁned over a bounded geographical range of activity. This is the distribution of a random variable representing the location of his next crime. The model does not include the decision to commit a crime, as we are interested in modeling the behavior of a serial oﬀender in the course of a spree. We assume the distribution to be static over the period between any two crimes, and to change instantaneously at the instant that a crime is committed.

3.2.2 Rational Choice: Theory

Divide the criminal’s assumed range into n cells, numbered 1 through n. In- cluded in our data, then, is a vector K, where each Kj ∈{1, ..., n} denotes the cell in which the criminal committed his jth crime. Assume the criminal is a rational agent with a utility function

U(p, c),

where p is a vector deﬁned over all cells of the grid such that pi = the probability that next crime will happen in cell i, and c is a vector of the same dimension such that ci = the criminal’s perception of the increased risk that he will be caught if he commits his next crime in cell i.

He chooses p to maximize U subject to the constraint

n X pi = 1.

i=1

This yields the ﬁrst-order conditions

∂U (p1, . . . , pn, c1, . . . , cn) = 0 ∂p1 ... ...

∂U (p1, . . . , pn, c1, . . . , cn) = 0 ∂pn Assume that U is well-behaved, so that we may invoke the Implicit Function Theorem to deﬁne k(c) such that

p1 = k1 (c1, ..., cn) ... ... .

pn = kn (c1, ..., cn)

Assume that each time the criminal commits a crime, c changes, and therefore k changes. As the function k(c) is arbitrary, it may contain any number of parameters α: these may reﬂect any way in which we think the criminal prefers one location for his crime over another. It is these parameters which we hope to ﬁnd.

We begin by assuming a form for c(x). It may be as simple as

( if i ∈Xj 1 c(Xj) = otherwise , (4) 0

where Xj = {i| the criminal committed one of his ﬁrst j crimes in cell i}. This form captures the belief, “If I commit a crime twice in the same spot, I will be arrested for sure, but otherwise my past crimes have no impact on my chances of being caught.” Next, assume some form for the ki functions. For a criminal assumed to prefer working near a home base (allowing for a buﬀer zone), a possible one-parameter function would be

( 0 if α = i ki(c, α) = (5) 1−ci otherwise d(α,i)¯k where α represents the location of a home base, d is a metric, and ¯k is a normal- ization constant. Then for any value(s) of α, we can calculate the probability P(Kj|Xj−1, α) that the rational criminal characterized by the functions k and c, having committed j −1 crimes in the set of locations Xj−1 where the ﬁrst j −1 crimes occurred, would have committed his jth crime in the location Kj where the jth crime actually took place. Finally, deﬁne

\ P(K|α) = kKj(c(Xj−1), α). (6) j

Then P(K|α) is the probability that the observed set of crimes K would have been committed by our rational criminal, given α. By evaluating this function over a range of possible values for α, we can get an idea of which parameter values are more probable than others.

3.2.3 Rational Serial Criminal: Practice

The theory above could be used to model any serial criminal who commits crimes at diﬀerent locations. In the current paper, we are interested in helping a police department catch a serial killer, and in this section we describe our speciﬁc implementation of a Rational Serial Criminal (RSC) model for this task.

When a serial killer is at large, law enforcement has two goals: to prevent future killings and to ﬁnd the killer. The rational choice model can help with both of these goals, by making predictions about where the killer lives and about where he may kill again, both based on previous killings. Implementing the model requires making explicit our assumptions about the killer’s behavior. For both purposes, we make the following assumptions:

• The killer prefers to kill near, but not at, an anchor point α. This anchor point does not change over the course of the spree.

• The killer’s taste for killing in a given location, ki, is a function only of that location’s distance from his anchor point and its distance from previous kill sites X.

• ki is given by Equations 4 and 5.

First, we estimate the likelihood that the killer lives in each grid-cell of the city. We make the following additional assumptions:

• The prior odds P(α) of the killer living in place α are equal for all α.

• The prior odds P(Kj = i) of the killer committing his jth murder in place i are equal for all i.

Given these assumptions, Bayes’ Formula

P(K|α = i)P(α = i) P(α = i|K) = P(K|α = 1)P(α = 1) + · · · + P(K|α = n)P(α = n)

implies P(α = i|K) ∝P(K|α = i). (7)

Our goal, and perhaps the limit of our abilities, is to rank potential anchor points in order of likelihood. As such, Equation 7 is suﬃcient to say that the isopleth produced by plotting Equation 6 may be taken as a jeopardy surface, representing the relative likelihood of the killer residing within the region asso- ciated with each grid cell [32]. Such a plot could help the police ﬁnd the killer faster by telling them where to look ﬁrst [32].

Next, we estimate the likelihood that the killer will strike next in each grid-cell. For each grid cell i, this is equivalent to pi. Again, we assume P(α|K1, . . . , Kj−1) ∝P(K1, . . . , Kj−1|α) for all α. Using data from J −1 attacks, we estimate the likelihood that the Jth attack will occur in any given cell i by J−1 n X X ˆpi ∝ ki(c(Xj−1), α)P(K1, . . . , Kj−1|α), α=1 j=1

where P(K1, . . . , Kj−1|α) is computed by Equation 6. Again, our goal is to rank possible locations for the next attack by likelihood, so we do not bother with normalization constants.

4 Data

5 Data

To calibrate and test our models, we constructed data sets from data on three real serial killers: David Berkowitz, the “Son of Sam”, Angelo Buono and Ken- neth Bianchi, the “Hillside Strangler” (police originally thought there was a single killer), and John Allen Muhammad, the “D.C. Sniper”. For each one, we began with a list of the killer’s victims taken from a Wikipedia [3, 4, 2], and then ﬁlled in details for each murder or attempted murder with details found in newspaper articles from the time. The Berkowitz and Sniper data sets included address where people were shot, while the Hillside dataset included locations where strangled bodies were found. For calculations, we converted the street addresses to latitude-longitude coordinate pairs (Table 1).

Kill# Longitude Latitude RelativeDay Victim(s) Address -73.833846◦ 40.847067◦ 1 0 Donna Lauria and 2860 Burhe Ave, Jody Valenti Bronx, NY -73.804809◦ 40.768099◦ 2 25 Carl Denaro and 160th St and 33rd Rosemary Keenan Ave, Queens, NY -73.706561◦ 40.738631◦ 3 121 Joanne Lomino and 83-31 262nd St, Donna Demasi Queens, NY -73.845048◦ 40.718511◦ 4 185 Christine Freund 1 Station Square, and John Diel Queens, NY -73.847051◦ 40.718598◦ 5 222 Virginia 4 Dartmouth St, Voskerichian Queens, NY -73.835418◦ 40.847445◦ 6 262 Alexander Esau 1878 Hutchinson and Valentina River Parkway, Suriani Bronx, NY -73.771343◦ 40.758704◦ 7 332 Sal Lubo and Judy 45-39 211th St, Placido Queens, NY -74.011712◦ 40.612735◦ 8 367 Stacy Moskowitz 86th St and 14th and Robert Vi- Ave, Brooklyn, NY olante

6 Results

6.1 Centrographic Model

To test the centrographic model’s predictive capabilities, we implemented it via a Python script and ran it on the data from the Hillside kills sequentially, using the ﬁrst j −1 kills to predict the jth starting with j = 4 (Figure 1). As the output from the model changes with time we used the actual time of the subsequent kill Kj in evaluating the prediction function. In our simulations we ¯tj ln 15 where ¯tj is the mean time between kills up to adopted an β value of β = kill j. In practice a value of β must be determined according to the previous crime data for the speciﬁc series.

To measure accuracy of the model, we calculated the distance between the center of the area of probable next kill and the actual location of the next kill (Table 2). The error distance has been criticized in past works [32], but recent comparisons between the error distance and alternative accuracy measures have shown it to perform comparably [39]. The metric we use in calculating error distance is the L1 or Manhattan metric,

d1(p, q) = ||p −q||1 = |px −qx| + |py −qy|

Our choice of the Manhattan metric arises from previous work indicating that it most accurately models actual travel distance in urban settings, a more im- portant factor than strict Euclidean distance in geographical proﬁling [32].

To estimate the acceleration of the spatial centroid we perform a linear regression on the calculated centroidal velocity data for each estimate, in both the longitudinal (Table 3) and latitudinal (Table 4) directions independently.

Kill# Distance from center of predicted area (km) 4 19.9032477532 5 13.1624956104 6 26.1455165479 7 12.1278772065 8 4.41086910109

sequent kill, measured with Manhattan metric. Hillside data set [19].

R2 Kill# ˆax p 4 0.00119566020314 1.0 N/A 5 0.00110767788734 0.99360376805 0.0720425343571 6 0.000787815342892 0.829782525827 0.170217474173 7 0.000494702112585 0.592338457701 0.292588804185 8 0.000422872375405 0.571437451732 0.236142632648

tudinal). Hillside data set [19].

R2 Victim# ˆay p 4 0.000665961218837 1.0 N/A 5 0.000983419577946 0.90783947974 0.275461438702 6 0.00105866206185 0.93384684203 0.0661531579701 7 0.000983719311558 0.935632003161 0.0194133564982 8 0.000950274912901 0.943853948827 0.00464007177548

tudinal). Hillside data set [19].

6.2 Rational Serial Criminal Model

Like Rossmo’s criminal geographic targeting (CGT) model [32], the RSC model yields a jeopardy surface representing the estimated relative probabilities that the killer lives within each grid cell on a map. For this to be useful, it should allow law enforcement to search for the killer more eﬃciently. We tested our results using Microsoft Excel macros in the same way that Rossmo tested the gler data set [4]. The blue points represent the kills used to calculate the cen- troid, centroidal velocity and centroidal acceleration. The red diamond repre- sents the estimated area of next probable event (within one mean distance of the centroid along each axis in each direction). The black point represents the actual location of the next event.

“Son of Sam,” using the Berkowitz data set [24]. The ranking of quadrant coloring in order from least probable location to most probable location is: blue, red, green, purple.

CGT model: by drawing a box called a “hunting area” around the attack sites, plotting the jeopardy surface based on the attack locations, and then asking the question: if the police were to search every cell in the hunting area in order of highest to lowest on the jeopardy surface, what percentage of the grid would they have to search before they got to the killer? This number is called the Hit Score % [32]. Multiplying this by the size of the hunting area yields the eﬀective search area: the actual area the police would have to search, following the jeopardy surface, before ﬁnding the killer. This method of testing allows the modeler some degree of ﬂexibility, in deciding which locations would have been counted as crime sites and in guessing where the killer would have been found.

For David Berkowitz, we ran the RSC model with the locations of the eight shooting incidents attributed to him at the time of his capture [24]. The re- sulting jeopardy surface is shown in Figure 2, with locations of shootings and Berkowitz’s last two residences overlaid. While on most occasions he shot or shot at two people, we counted each shooting only once. Berkowitz lived in the Bronx for several years, near his ﬁrst and sixth crime scenes, but moved to Yonkers before shooting his ﬁrst victims [25]. He later admitted to having stabbed two people near his Bronx home while living there [25], but newspaper accounts from the time [36, 24] show no indication that the stabbings had been connected to his shootings before his arrest. Therefore, we did not include them in our analysis, as their location would not have been available for considera- tion by law enforcement at the time. We computed two scores, one using a grid deﬁned by the crime sites to look for Berkowitz former house in the Bronx, and one using a grid contrived to include his Yonkers house to ﬁnd him there. The results are tabulated in Table 5.

Home Hunting Area Hit Score % Search Area 1,414 km2 255 km2 Bronx 18.1% 2,514 km2 1,588 km2 Yonkers 63.2%

In October and November of 1977, the bodies of 11 strangled women were discovered in Los Angeles, and were all believed to be the victims of a single “Hillside Strangler” [19]. Using the exact same parameters and assumptions, we ran the RSC model on the 9 of these locations (two of the bodies were found in the same location, which we only counted once; for one body we could not ﬁnd an exact location of discovery). The resulting jeopardy surface is plotted in Figure 3, and the Hit Score % and accompanying data for the house of one of the two oﬀenders, Angelo Buono, [7] can be found in Table 6.

There were two main diﬀerences between this data and the data for the Berkowitz shootings: ﬁrst, these were locations where bodies were found dumped, not locations where killings actually took place. Second, the hunting zone around these bodies, determined by their location, stretched over twice as far North to South as it did East to West, while the Berkowitz hunting zone was essentially square. Nonetheless, the model still performed reasonably well on the Hillside Strangler data without modiﬁcation.

To test the predictive powers of the RSC model, we used the jeopardy surface with the ﬁrst six kills from the Berkowitz data set and the modiﬁed utility and cost functions (see Section 3) to try to predict the location of the 7th kill (Figure 4). In this case it doesn’t make sense to use a Hit Score % to analyze accuracy as the killer will not necessarily be stationed at the predicted site during the course of an extended search, but it is evident from the jeopardy surface that the model performed favorably, as the kill occurred in one of the regions of highest probability. Of course, this is just one data point, and a month later Berkowitz shot his ﬁnal victims in Brooklyn: this point would not even have been on our map.

Hunting Area Hit Score % Search Area 2,721 km2 379 km2 13.9% of the “Hillside Strangler” duo. The ranking of quadrant coloring in order from least probable location to most probable location is: blue, red, green, purple.

the ﬁrst six kills from the Berkowitz data [24] to generate the jeopardy surface. The ranking of quadrant coloring in order from least probable location to most probable location is: blue, red, green, purple. The black point is the actual location.

6.3 Combined Models

As a brief example of using the RSC model and the Centrographic model in conjunction with each other, we used each model on the DC Sniper data set [2] and graphed the outputs (Figures 5 and 6).

data [2]. The blue points represent the kills used to calculate the centroid, centroidal velocity and centroidal acceleration. The red diamond represents the estimated area of next probable event (within one mean distance of the centroid along each axis in each direction). The black point represents the actual location of the next event.

using the previous kills from the DC Sniper data [2]. The ranking of quadrant coloring in order from least probable location to most probable location is: blue, red, green, purple. The black point is the actual location.

7 Discussion

Any model of serial killer behavior must be somewhat ad hoc. While Rossmo’s macrolevel serial killer dataset lists 225 cases of serial killers in 9 countries going back to the late nineteenth century, of these, he found only 21 to be suitable for testing his model [31].

Looking at the data for the Centrographic model, we see in Figure 1 that the predictions seem to get better over time, meaning that as more data become available the model is becoming more accurate. Indeed, the error distances (Table 2) are decreasing with each additional kill, and the mean error distance is only roughly 15.12 km, a small distance considering the search area was the city of Los Angeles.

A key part of the Centrographic model is its use of a linear regression to esti- mate the acceleration, ˆa, which brings up a question of how valid a linear regres- sion on the velocity data actually is. Evident in Table 4, our test demonstrated a high correlation coeﬃcient (≈90% correlation) for the Y-acceleration, ˆay, as well as small p-values for the later crimes, implying that the linear regression is a statistically signiﬁcant model that accounts for a large part of the variation in the data. This indicates the linear regression model to be a mathematically valid approach in this case. However, in the case of the X-acceleration, ˆax (Ta- ble 3), the correlation coeﬃcient was smaller and the p-values larger, yielding a statistically insigniﬁcant model that doesn’t account for a large degree of the variation in the data.

The problems with the model’s acceleration approximation illustrate once again the problems with performing statistical analysis on a small data set. Even though the ˆax obtained from regression would seem to account for at least 60% of the data variation, it could just be random chance. If we disregard the question of statistical signiﬁcance for a second and just look at the correlation, however, it’s obvious that the linear model does not seem to be enough in the case of ˆax. This indicates that perhaps it is necessary to reconsider the idea of a linear regression to calculate ˆa—perhaps the idea of a centroidal acceleration of a data set is not entirely conducive to geographical proﬁling, or perhaps even a higher-order regression is necessary, introducing analogues to physical concepts such as jerk (the change in acceleration over time) and jounce (the change in jerk over time)4.

The Centrographic model performs well on the data available to us, but more extensive testing is needed to determine its validity. To improve the model, it would be advisable to conduct future research on many more data sets in order to determine appropriate choices of the f(t) and g(t) functions used. A weakness of the model as it stands is its sensitivity to the choice of β, so perhaps our choices of the functions in this simulation were ill-advised. Additionally, the model does not incorporate as much temporal modeling as it could, which could strengthen its predictive powers.

The Rational Serial Criminal model performed reasonably well on the data

4But maybe this is just silly.

for which we tested it. With the Hillside Strangler data, the Hit Score % of our jeopardy surface for the location of the killers home was only 13.9% (Table 6), meaning only 13.9% of the hunting area would need to be searched before ﬁnding the home of Angelo Buono, a vast reduction. With our choice of probability density function k, the RSC model made predictions qualitatively similar to those made by the CGT model [31]. In the case of the Berkowitz data, however, the Hit Score % for our prediction for ﬁnding Berkowitz’s home at the time of the murders was only 63.2% (Table 5)—worse than random chance. This is due to the fact that shortly before the murders took place Berkowitz moved his place of residence. Using Berkowitz’s old home, the RSC model yields a Hit Score % of 18.1%, a much more reasonable ﬁgure.

Conducting a χ2 goodness of ﬁt test of the Hit Score % from the three tests against the uniform probability density function implied that the data are not uniformly distributed at the 95% level of signiﬁcance. This implies that the RSC model developed is statistically superior to a random search method for the location of the murderer’s home.

The RSC model’s performance in our tests was hampered by a few simpli- fying assumptions we made:

• We assumed the initial probability distribution over the hunting area for the location of a serial killer’s home was uniform.

• We assumed the initial probability distribution over the hunting area for the location of a murder was uniform.

Obviously, as in the case of the Berkowitz data, this is not always the case— half of the area included in our simulation was underwater, indicating zero probability of the killer’s home being in that area, and zero probability of the next kill occurring in much of that area5. To improve the RSC model, it is possible to modify the initial guess of the probability distribution for both of these cases based on simple factors such as population density or geographic landmarks (ie, lakes and harbors).

The real strength of our Rational Serial Criminal model is its theoretical indiﬀerence to the choice of utility function. This means that it can be adapted to the pursuit of almost any serial criminal. Besides the well-documented ten- dency for criminals to act locally, police investigating a particular fugitive may have any number of other ideas about the crook’s preferences. If they can write these down as functions, the RSC model can help them as they develop a search plan based on their evidence and intuition. Since one might reasonably consider a group engaged in organized crime to be a single agent, one could also use the RSC model to investigate gang behavior, for example.

Independent of any speciﬁc investigation, we could improve the RSC model signiﬁcantly by putting other common themes and population trends [28] about crime sites into functional form. For instance, criminals tend to prefer to act in areas which are like the areas they are familiar with [23]. If we included zoning

5Disregarding serial criminals with ﬁshing boats or scuba certiﬁcation.

and demographic data in our grid, we could include a term in the k function which operationalizes this prediction. We could also change the meaning of p to include more sophisticated information about the victims, so that we could model a criminal who tended to ﬁnd his victims in a particular region but then assaulted them or disposed of their bodies in more diverse locations [13]. This could augment the current method of using GIS software to determine how several victims’ daily lives might have led them to interact with a killer, and from this information determining areas where the killer might spend a lot of time [37].

In Figures 5 and 6 we see the results of running both the RSC and Centro- graphic model on the DC Sniper data set. Using both methods generates two zones each with theoretically high probability of encounter with the serial killer in question. Looking at the graphs, we see that the models did not predict the actual crime site. This can be explained by the nature of the data. In the RSC model case, there is a crime site in the same location of a previous crime site. This violates the assumptions of the model. In the centrographic model, the killer took an unexpected turn south, resulting in a crime site far from any of the others. Both of the problems above stem from the size of the hunting area for the DC Sniper, which contains large areas of Maryland and parts of Virginia. This, however, is simply a characteristic of the DC Sniper data that makes it diﬃcult to make predictions regarding his actions in general. Additionally, the DC Sniper data diﬀers from the other sets in that many of the kills took place on the same day at diﬀerent times, making some of the calculations involved in the centrographic model diﬃcult or nonsensical (ie, predicting inﬁnite velocity). With a more accurate data set (to the time of day, for example) it is possible the model would perform better.

To improve the way the models work together, a number of possible adapta- tions could be made in future models. As the RSC is a resource-intense method, it is possible that using it for a large area with a ﬁne enough quadrant resolution could be simply too slow. Since the Centrographic model theoretically narrows down the search window, it could be useful to consider using a variable quadrant resolution when analyzing large areas, where the resolution outside the area pre- dicted by the Centrographic model is larger than that inside, yielding a faster runtime while still providing a high level of accuracy in high probability areas. Using the models in the other direction, probability data from the RSC model could be used to create a sort of resistance to the motion of the centroid in the Centrographic model to cause it to stay near regions of higher probability.

Overall, this model provides a starting point for a police search. It is meant to be another tool to the police, to give a general guideline of where to allocate police sources when very few data are available. In reality, police experience is impossible to replace with any kind of mathematical method, and when dealing with a subject as unpredictable as a serial murderer, experience is necessary to determine the most eﬃcient way to catch the killer.

8 Executive Summary

This method is a computer program that takes crime site (either body disposal site or scene of the crime) data in absolute coordinates and returns a prediction of the oﬀender’s residence and a prediction of the next crime site. This should be used for two things: to narrow the search for the oﬀender in his daily routine and to narrow the search for the next crime site. It is possible that, after discovering a crime site, that there is another crime site in a location that has not yet been discovered. Furthermore, a search that starts in the most probable area and radiates from this center is more likely to ﬁnd the oﬀender’s residence, or next crime site, than a random search would [32]. The method will provide a starting point and an area for a police force to concentrate the eﬀorts of determining both the location of an oﬀender and where the next crime site might be.

In employing the method, the police force makes the same assumptions that are involved with developing the program. The assumptions made are:

• The series will occur in an area that the oﬀender is familiar with, meaning a place where he lives, has lived, or has committed crimes before.

• The most probable location of the next crime site can change with time, even without new data being acquired regarding former sites in the series.

• The order and time at which former crime sites occur aﬀects the location of the predicted next crime site in the series.

• Given no crime site data, the oﬀender is equally likely to live or commit a crime at any location.

In using the program to predict the oﬀender’s home, it is assumed that the oﬀender has a home base within or close to the crime site, as opposed to com- muting to the area of the crime site. This assumption can be relaxed when predicting where the next crime site might be, as this prediction is made solely on earlier crime site data and thus does not oﬀer additional information. An example of when the method would not apply is when an oﬀender picks up prostitutes in a red light district in order to kill them. If, as in the John Wayne Gacy Jr. case, the crime sites all share a location the model will not apply as no usable predictions could be gleaned from that data.

The program utilizes two diﬀerent types of models to make predictions, a centrographic model and a rational choice model. The centrographic model has an analogy in physics, where the crime sites are treated as point masses in a system, and the “centroid” is determined by ﬁnding the center of mass of the system. From this model is output a graph that includes the points of the crime sites and a diamond. Within the diamond lies the prediction for the next crime site. The rational choice model has an analogy in economics. This model uses the idea that the oﬀender is deciding the location of the crime site in order to satisfy his personal goals (mostly of committing another crime) and to minimize his risk of being caught. Thus, it is assumed that the series will continue and that there will not be two crime sites in the same location. There are two types of this model included in the program, one that predicts where the oﬀender lives and the other predicts the location of the next crime site. In both cases, the model outputs a contour plot. In the two cases, the peaks correspond to either high probability of the oﬀender’s home base and to the location of the next crime site, respectively. There will always be a valley at the location of a previous crime site. Then, when determining where to search for the next crime site, the contour plot from the rational choice model and the plot from the centrographic model can be utilized in conjunction to narrow the initial search area. A key item to note is that the centrographic model makes use of a parameter, β, that is determined by the data of known crime times and must be ¯t derived individually for each serial killer. An example value might be β = ln 15, where ¯t is the mean time between crimes.

The method will always output graphs that can be used to begin a police search, but as it is a computerized process, it only responds to the data set provided. Thus, there is an element of subjectivity in determining which crime sites in a given case are useful for predictions [32]. When predicting where the oﬀender lives, the following should be used as a guideline for inputting crime site data:

• A minimum of ﬁve crime sites should be used in order to provide a basis for the prediction. Certainly, the program will work with as few as three crime sites, but will not serve to improve the search area greatly. Furthermore, when invoking the program, one assumes that the oﬀender has not changed the home base since the series began. Else, more crime sites are necessary to determine a valid prediction.

• Only crime sites that are accurately known should be input to the pro- gram. For example, using data determined from victims acquaintances as to where the victim was last seen to determine where the oﬀender might have met the victim should not be counted as valid input.

• If it is clear that two crime sites relate to the same crime (i.e. a site is found where the oﬀender killed the victim, but the body disposal site in a diﬀerent location) one or the other location should be input in to the model, in accordance with the other crime sites [32].

When predicting the location of the next crime site the previous also apply, though several crime sites in the same area at diﬀerent points in time might be considered as several diﬀerent sites, as this might be an indication of where the oﬀender’s next act in the series might occur.

One of the most powerful tools to be incorporated alongside this program is a GIS mapping software. Using such software will retain perspective of the crime site data when considering the predictions set forth from the program. Furthermore, the program does not account for any sort of victim data that might be gathered during the investigation. Considering these two additional elements will lead to more eﬃcient searches.
