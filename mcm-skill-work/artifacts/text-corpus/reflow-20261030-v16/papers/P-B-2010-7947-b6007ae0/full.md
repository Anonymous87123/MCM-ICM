# P-B-2010-7947-b6007ae0

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team number 7947

<!-- b000002 | furniture | pages [1] -->
Page 1 of 1

<!-- b000003 | heading | pages [1] -->
Summary

<!-- b000004 | prose | pages [1] -->
We develop geographical proﬁling methods that determine the probable lo- cation of a serial criminal’s next crime based on the spatiotemporal data of their previous crimes. We assume that the spatial behavior of a serial criminal is non-random.

<!-- b000005 | prose | pages [1] -->
We consider standard deviation, centralization, and probability distance methods for prioritizing a given search area. We also develop analogous methods which weight the spatial data of recent crimes more heavily. We then develop ways of aggregating results from multiple methods.

<!-- b000006 | prose | pages [1] -->
The performance of a geographical proﬁling method is based on its ef- fectiveness in narrowing down a particular search area into regions likely to contain the next crime location. The accuracy of a method for a particu- lar serial criminal is based on the past performance of the method on the spatiotemporal data of that criminal.

<!-- b000007 | prose | pages [1] -->
All of our methods produce a prioritized search area in which the next crime occurs in approximately the top 10% of the search area, a signiﬁcant improvement over a uniform random distribution. However, the diﬀerences in performance among the diﬀerent methods developed were statistically in- signiﬁcant. We also found the accuracy of our methods varied depending on the serial criminal under investigation.

<!-- b000008 | furniture | pages [2] -->
Team number 7947

<!-- b000009 | furniture | pages [2] -->
Page 1 of 2

<!-- b000010 | heading | pages [2] -->
Executive Summary

<!-- b000011 | prose | pages [2] -->
We have developed models to be used in an open investigation of a serial criminal. In this summary we describe how our models can best be employed to help identify probable next target locations of the serial criminal.

<!-- b000012 | prose | pages [2] -->
Our models use the locations and times of previous crimes committed by a serial criminal in order to predict the likely next target location. This prediction prioritizes the search area so that law enforcement resources can be focused on the most probable next target regions. Our models prioritize the search areas in diﬀerent fashions:

<!-- b000013 | prose | pages [2] -->
• Centralization models: These models are based on the assumption that a serial criminal’s activity is centered around a point.

<!-- b000014 | prose | pages [2] -->
• Probability distance models: In these models, the closer a location is to previous crimes, the higher the probability the serial criminal will strike there next.

<!-- b000015 | prose | pages [2] -->
• Time-based models: In these models, a location’s proximity to recent crimes is weighted more heavily than its proximity to crimes in the distant past.

<!-- b000016 | prose | pages [2] -->
• Aggregate models: These models combine the above models.

<!-- b000017 | prose | pages [2] -->
There are multiple factors to consider when deciding if a particular model is applicable to a serial criminal investigation:

<!-- b000018 | prose | pages [2] -->
• Evidence of serial nature: Our models assume that all of the ob- served crimes were committed by one criminal. If there is a strong reason to doubt this assumption, such as the presence of a copy-cat criminal, then our models are not applicable.

<!-- b000019 | prose | pages [2] -->
• Accuracy score: Our models provide a statistic that estimates their accuracy as applied to the serial criminal under investigation. If our models would not have performed well in predicting the locations of this serial criminal’s past crimes, there is no reason to believe that our models would accurately predict the location of the criminal’s next crime.

<!-- b000020 | furniture | pages [3] -->
Team number 7947

<!-- b000021 | furniture | pages [3] -->
Page 2 of 2

<!-- b000022 | prose | pages [3] -->
• Available resources: Our models prioritize the search area such that the next crime location is on average in the top 10% of the prioritized search area. This search area can still be prohibitively large to cover with the resources available to the investigation. If this search area is still too large to cover, then our models are still applicable but may not yield optimal results.

<!-- b000023 | prose | pages [3] -->
If it is determined that our models are applicable to a serial criminal inves- tigation, then there are multiple limitations of our models which need to be taken into consideration:

<!-- b000024 | prose | pages [3] -->
• Our models do not take into account relevant geographical information: For example, if you know the serial criminal is targeting banks, our models do not take this into account. In this example, a list of bank locations can be cross-referenced against the prioritized search area given by our models to determine the banks that are likely to be targeted next.

<!-- b000025 | prose | pages [3] -->
• Our models do not take into account relevant information about the criminal: The average distance that a serial criminal trav- els to commit a crime depends on the type of crime and characteristics of the criminal, including gender, race, and age. Our models assume no information of this type is known about the criminal.

<!-- b000026 | prose | pages [3] -->
• Our computer models may not outperform geographical pro- ﬁling techniques employed by a human: Research has suggested that complex computer geographical proﬁling methods are no more accurate than an investigator with minimal training in geographical proﬁling techniques.

<!-- b000027 | heading | pages [3] -->
Overall, we recommend that our geographical proﬁling models not be used

<!-- b000028 | prose | pages [3] -->
as the only tool used in a serial criminal investigation. Instead, our models should complement traditional investigative techniques. It is our hope that our models can further aid law enforcement agencies in their pursuit of serial criminals.

<!-- b000029 | prose | pages [4] -->
Predicting a Serial Criminal’s Next Crime Location Using Geographical Proﬁling

<!-- b000030 | prose | pages [4] -->
Control Group 7947

<!-- b000031 | prose | pages [4] -->
February 22, 2010

<!-- b000032 | heading | pages [4] -->
Abstract

<!-- b000033 | prose | pages [4] -->
Geographical proﬁling techniques can be useful to law enforcement agencies who are investigating a serial criminal. We develop such meth- ods that determine the probable location of a serial criminal’s next crime based on the spatiotemporal data of their previous crimes. We consider standard deviation, centralization, and probability distance methods for prioritizing a given search area, and also develop analogous methods which weight the spatial data of recent crimes more heavily. We then develop ways of aggregating results from multiple methods. The performance of a geographical proﬁling method is based on its eﬀectiveness in narrowing down a particular search area into regions likely to contain the next crime location. All of our methods produce a prioritized search area in which the next crime occurs in approximately the top 10% of the search area, a signiﬁcant improvement over a uni- form random distribution. However, the diﬀerences in performance among the diﬀerent methods developed were statistically insigniﬁcant. We also found the accuracy of our methods varied depending on the serial criminal under investigation.

<!-- b000034 | prose | pages [4] -->
1

<!-- b000035 | furniture | pages [5] -->
Team number 7947

<!-- b000036 | furniture | pages [5] -->
Page 2 of 25

<!-- b000037 | heading | pages [5] -->
Contents

<!-- b000038 | contents | pages [5] -->
1 Introduction

<!-- b000039 | contents | pages [5] -->
3

<!-- b000040 | contents | pages [5] -->
2 Problem Background

<!-- b000041 | contents | pages [5] -->
3

<!-- b000042 | contents | pages [5] -->
2.1

<!-- b000043 | contents | pages [5] -->
Terminology . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000044 | contents | pages [5] -->
3

<!-- b000045 | contents | pages [5] -->
2.2

<!-- b000046 | contents | pages [5] -->
Survey of Current Literature

<!-- b000047 | contents | pages [5] -->
. . . . . . . . . . . . . . . . . .

<!-- b000048 | contents | pages [5] -->
4

<!-- b000049 | contents | pages [5] -->
2.3

<!-- b000050 | contents | pages [5] -->
Collection of Data

<!-- b000051 | contents | pages [5] -->
. . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000052 | contents | pages [5] -->
5

<!-- b000053 | contents | pages [5] -->
3 Constructing a Model

<!-- b000054 | contents | pages [5] -->
7

<!-- b000055 | contents | pages [5] -->
3.1

<!-- b000056 | contents | pages [5] -->
Assumptions

<!-- b000057 | contents | pages [5] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000058 | contents | pages [5] -->
7

<!-- b000059 | contents | pages [5] -->
3.2

<!-- b000060 | contents | pages [5] -->
Model Descriptions . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000061 | contents | pages [5] -->
7

<!-- b000062 | contents | pages [5] -->
3.3

<!-- b000063 | contents | pages [5] -->
Model Performance Metric . . . . . . . . . . . . . . . . . . . .

<!-- b000064 | contents | pages [5] -->
8

<!-- b000065 | contents | pages [5] -->
3.4

<!-- b000066 | contents | pages [5] -->
Model Accuracy for a Particular Criminal . . . . . . . . . . .

<!-- b000067 | contents | pages [5] -->
9

<!-- b000068 | contents | pages [5] -->
3.5

<!-- b000069 | contents | pages [5] -->
Search Area Determination

<!-- b000070 | contents | pages [5] -->
. . . . . . . . . . . . . . . . . . .

<!-- b000071 | contents | pages [5] -->
10

<!-- b000072 | contents | pages [5] -->
4 Individual Models

<!-- b000073 | contents | pages [5] -->
10

<!-- b000074 | contents | pages [5] -->
4.1

<!-- b000075 | contents | pages [5] -->
Spatial Models

<!-- b000076 | contents | pages [5] -->
. . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000077 | contents | pages [5] -->
10

<!-- b000078 | contents | pages [5] -->
4.2

<!-- b000079 | contents | pages [5] -->
Spatiotemporal Models . . . . . . . . . . . . . . . . . . . . . .

<!-- b000080 | contents | pages [5] -->
13

<!-- b000081 | contents | pages [5] -->
4.3

<!-- b000082 | contents | pages [5] -->
Individual Model Results

<!-- b000083 | contents | pages [5] -->
. . . . . . . . . . . . . . . . . . . .

<!-- b000084 | contents | pages [5] -->
15

<!-- b000085 | contents | pages [5] -->
5 Aggregation Models

<!-- b000086 | contents | pages [5] -->
16

<!-- b000087 | contents | pages [5] -->
5.1

<!-- b000088 | contents | pages [5] -->
Aggregation Model Results

<!-- b000089 | contents | pages [5] -->
. . . . . . . . . . . . . . . . . . .

<!-- b000090 | contents | pages [5] -->
19

<!-- b000091 | contents | pages [5] -->
6 Peter Sutcliﬀe: A Case Study

<!-- b000092 | contents | pages [5] -->
20

<!-- b000093 | contents | pages [5] -->
7 Conclusions

<!-- b000094 | contents | pages [5] -->
20

<!-- b000095 | contents | pages [5] -->
8 Future Work

<!-- b000096 | contents | pages [5] -->
22

<!-- b000097 | furniture | pages [6] -->
Team number 7947

<!-- b000098 | furniture | pages [6] -->
Page 3 of 25

<!-- b000099 | heading | pages [6] -->
1 Introduction

<!-- b000100 | prose | pages [6] -->
Serial criminals present a unique challenge to law enforcement agencies. In a typical crime, investigators are able to draw a connection between the criminal and the victim. This information often provides enough clues to form the basis of a criminal investigation. In the case of serial criminals, however, there is usually no such relationship between the criminal and the victim [1, 2]. This lack of information about the serial criminal forces law enforcement agencies to consider a larger possible target area for the next crime, which hinders the investigation.

<!-- b000101 | prose | pages [6] -->
In order to better utilize limited law enforcement resources in a serial criminal investigation, geographical proﬁling can be used to determine likely next crime locations. Geographical proﬁling is “. . . a procedure that exam- ines the spatial behavior of oﬀenders with regard to the locations of their crime scenes and the spatial relationships between those scenes” [3]. By using geographical proﬁling, investigators are able to take advantage of the spatial patterns of a serial criminal to focus their attention on certain geo- graphically important regions.

<!-- b000102 | prose | pages [6] -->
In this paper we examine diﬀerent geographical proﬁling methodologies and compare their ability to predict the location of a serial criminal’s next crime. In Section 2, we provide the terminology and background informa- tion that will be utilized in the rest of the paper. In Section 3, we describe the features that are common to all geographical proﬁling methods devel- oped and our metrics for determining the performance and accuracy of a particular method. Section 4 develops geographical proﬁling methods and reports on their performance, and Section 5 considers combinations of these methods. In Section 6, we apply our best geographical proﬁling methods to the serial murders committed by Peter Sutcliﬀe. Section 7 summarizes our main conclusions, while Section 8 discusses possible avenues for future work.

<!-- b000103 | heading | pages [6] -->
2 Problem Background

<!-- b000104 | heading | pages [6] -->
2.1 Terminology

<!-- b000105 | prose | pages [6, 7] -->
• Serial Criminal: A serial criminal is a habitual oﬀender who commits three or more related crimes over a span of time [1, 4]. We consider all forms of serial criminals together, such as murderers, rapists, arsonists, and burglars.

<!-- b000106 | furniture | pages [7] -->
Team number 7947

<!-- b000107 | furniture | pages [7] -->
Page 4 of 25

<!-- b000109 | prose | pages [7] -->
• Spatiotemporal Data: The locations and corresponding times of crimes committed by a serial criminal.

<!-- b000110 | prose | pages [7] -->
• Spatial Behavior: The spatial behavior of a serial criminal describes how the serial criminal chooses crime locations [5, 6]. We model the spatial behavior of a criminal based on the spatiotemporal data of their previous crimes.

<!-- b000111 | prose | pages [7] -->
• Geographical Proﬁling Method: A geographical proﬁling method is a particular methodology for modeling the spatial behavior of a serial criminal. We consider spatial methods that only consider the spatial data of previous crimes, spatiotemporal methods that also take into account the times of previous crimes, and aggregate methods that combine two or more geographical proﬁling methods.

<!-- b000112 | prose | pages [7] -->
• Prioritized Search Area: The area to search prioritized by the probability of the next crime given by a speciﬁc model. This area is important in determining how to allocate law enforcement resources.

<!-- b000113 | heading | pages [7] -->
2.2 Survey of Current Literature

<!-- b000114 | prose | pages [7] -->
There is an ongoing debate as to the eﬀectiveness of diﬀerent geographical proﬁling methodologies. Rossmo uses spatial data to determine the resi- dence of a criminal based on assumptions about spatial behavior, such as the tendency to commit crimes close, but not too close, to home [7]. As Rossmo’s paper lacks a detailed description of his algorithm, and relies on empirically determined constants, it is diﬃcult to reproduce his geograph- ical proﬁling methodology accurately [8, 7, 3]. Van der Kemp and van Koppen survey and criticize theories of spatial behavior, including theories of crime location proximity to the criminal’s residence and shortcomings of current geographical proﬁling methods [9]. Beauregard et al. and Snook et al. also examine the spatial behavior or serial criminals [10, 5]. Brown et al. take into account spatiotemporal data as well as additional features of the crime locations, such as proximity to highways, to predict crime locations [11, 2]. Recent work by O’Leary provides a mathematical foundation for geographical proﬁling [12].

<!-- b000115 | furniture | pages [8] -->
Team number 7947

<!-- b000116 | furniture | pages [8] -->
Page 5 of 25

<!-- b000117 | prose | pages [8] -->
We note that most of the work in the ﬁeld of geographical proﬁling focuses on identifying the residence of a serial criminal. This allows law enforcement agencies to cross-reference the addresses of potential suspects to the predicted residency of the criminal in order to narrow their search. In contrast, this paper focuses on identifying probable next crime locations in a series of linked crimes. Being able to forecast crime locations would assist law enforcement agencies in ways predicting the residency of the criminal does not. For example, law enforcement agencies would be able to increase patrols along probable crime locations, or alert high-risk neighborhoods to the existence of the serial criminal. Since serial criminals often center their crime locations around their residence [10], these two problems are related, and thus we are able to adapt methods of identifying the residence to the problem of identifying next crime locations.

<!-- b000118 | heading | pages [8] -->
2.3 Collection of Data

<!-- b000119 | prose | pages [8] -->
In order to determine the accuracy of proposed geographical proﬁling mod- els, we needed to see how the models performed against actual spatiotem- poral serial crime data. Unfortunately, there is no large collection of serial crime data to compare our models to, or a standard collection of serial crime data that is used across all geographical proﬁling research. A survey of spatial proﬁling research shows that the data sets used are varied, which leads to diﬀerent quantitative conclusions about the spatial behavior of se- rial criminals; see [9, 8, 10, 5] for contrasting conclusions based on diﬀerent data sets. For example, the circle center method described in Section 4.1 was found to have diﬀerent levels of accuracy for serial crime data sets from diﬀerent countries [4]. Ideally, we would be able to test our geographical proﬁling models against serial crime data that spanned multiple locations, crime types, and periods of time, but such a data set does not exist.

<!-- b000120 | prose | pages [8, 9] -->
In most studies we considered, a sample of serial crime data was either obtained from a government agency or compiled from newspaper and police reports. Unfortunately, due to the constrained time frame of our study, we were unable to obtain data from police departments and government agen- cies. However, we were able to compile a data set consisting of the crimes of nine serial criminals, totaling 124 crimes. For the more notorious crimi- nals in this data set including the Beltway Snipers, Peter Sutcliﬀe, and Dale Hausner we were able to collect data directly from police reports and news articles. We collected data for the remaining crimes from SpotCrime.com, an online crime information source, and veriﬁed the data via the referenced police reports and news articles [13]. A listing of the crimes in our data set can be found in Table 1.

<!-- b000121 | furniture | pages [9] -->
Team number 7947

<!-- b000122 | furniture | pages [9] -->
Page 6 of 25

<!-- b000124 | prose | pages [9] -->
Number Accuracy of Temporal Description of Crimes Exponential Decay Model Murders committed by Pe- ter Sutcliﬀe in West York- 12 0.048 shire, England Beltway sniper attacks committed by John Allen Muhammad and Lee Boyd 14 0.065 Malvo in the Washington, DC area Murders, arsons, and other crimes committed by serial 40 0.098 criminal Dale Hausner in Phoenix, AZ Sexual assaults committed by a serial rapist in Colum- 7 0.517 bus, OH Serial robberies at TCF Banks in Frankin Park, IL 12 0.180 area Serial robberies committed 6 0.103 in Denver, CO Serial bank robberies com- mitted by “The With- 12 0.119 drawal Bandit” in Boca Raton, FL Serial robberies committed 7 0.020 in Columbus, OH Serial robberies and home invasions committed in 14 0.174 Santa Monica, CA

<!-- b000125 | caption | pages [9] -->
Table 1: Description of data sets with accuracy score for temporal exponential

<!-- b000126 | prose | pages [9] -->
decay model.

<!-- b000127 | furniture | pages [10] -->
Team number 7947

<!-- b000128 | furniture | pages [10] -->
Page 7 of 25

<!-- b000129 | heading | pages [10] -->
3 Constructing a Model

<!-- b000130 | heading | pages [10] -->
3.1 Assumptions

<!-- b000131 | prose | pages [10] -->
• Spatiotemporal data is accurate: A common modeling assump- tion.

<!-- b000132 | prose | pages [10] -->
• Crimes were committed by one serial criminal: Our models are working on the assumption that all the crimes in a data set were committed by the same criminal, and thus the crime locations can be explained by a particular spatial behavior.

<!-- b000133 | prose | pages [10] -->
• Serial criminals do not act randomly: We assume the truth of rational crime theory, the notion that “. . . there is an underlying rea- son why criminals choose to commit crimes at a particular time in a particular location” [2]. Rational crime theory is a necessary condi- tion for productive geographical proﬁling, since if serial criminals are acting randomly, then the best model of their spatial behavior would be random as well.

<!-- b000134 | heading | pages [10] -->
3.2 Model Descriptions

<!-- b000135 | prose | pages [10] -->
Let x1, . . . , xn ∈A ⊂R2 denote crime scene locations of a serial crimi- nal, where A is a given search area encompassing the crime locations. Let t1, . . . , tn ∈R with 0 = t1 < . . . < tn denote the corresponding times of the crimes, where (xi, ti) is the spatiotemporal data of the ith crime. Given a location y ∈A, we deﬁne a probability function P such that P(y) is the probability that the next crime will happen at that location.

<!-- b000136 | prose | pages [10] -->
We discretize A into sectors Si,j in the order to simplify our calculations; see Figure 1 for a description of the discretization process. We assume that if y ∈Si,j, then P(y) = P(Si,j), the probability that the next crime location is in the sector. This is a reasonable assumption for small sector sizes relative to the total search area. Thus, the goal of a geographical proﬁling method is to determine P(Si,j) for all sectors.

<!-- b000137 | prose | pages [10, 11] -->
For our models, let d be a given distance metric. This distance metric can be determined using a variety of methods, including standard Euclidean distances, Manhattan distances, or travel-time distances that take into ac- count the road map data of the area. We arbitrarily choose to use Euclidean distances since we found no evidence that serial criminals evaluate distance using a certain metric, but our models do not make any assumptions about the nature of the distance function.

<!-- b000138 | furniture | pages [11] -->
Team number 7947

<!-- b000139 | furniture | pages [11] -->
Page 8 of 25

<!-- b000141 | caption | pages [11] -->
Figure 1: The discretization of a square search area into sectors. In this ﬁgure k

<!-- b000142 | prose | pages [11] -->
is equal to the side length of the search area divided by ∆s.

<!-- b000143 | heading | pages [11] -->
3.3 Model Performance Metric

<!-- b000144 | prose | pages [11] -->
There exist two commonly used metrics for the evaluation of the performance of a geographical proﬁling method. The ﬁrst measure is the error distance, which is the Euclidean distance between the most likely exact location of the next crime and the actual next crime location [8]. The second measure represents how much of the prioritized search area would need to be searched in order to ﬁnd the next crime location [12, 7].

<!-- b000145 | prose | pages [11] -->
Our model evaluation metric should reﬂect how useful these models would be to a law enforcement agency tracking a serial criminal. The most likely exact location of the next crime is not very valuable to law enforce- ment agencies, since often they are concerned with ﬁnding an area to search and not a particular point [12, 14, 7].

<!-- b000146 | prose | pages [11] -->
Thus, we consider the following metric that represents how much of the prioritized search area would need to be searched in order to ﬁnd the next crime location, which we call the hit score. Given a geographical proﬁling method with associated probability function P and a known next crime location xn+1, we wish to determine the hit score H.

<!-- b000147 | furniture | pages [12] -->
Team number 7947

<!-- b000148 | furniture | pages [12] -->
Page 9 of 25

<!-- b000149 | prose | pages [12] -->
Let L ∋xn+1 denote the sector Let S denote the set of all sectors. containing the next crime location. Then

<!-- b000150 | prose | pages [12] -->
B = {Si,j ∈S : P(Si,j) > P(L)}

<!-- b000151 | prose | pages [12] -->
is the set of all sectors that have a higher predicted probability than the sector containing the next crime. Thus, we have

<!-- b000152 | prose | pages [12] -->
H = |B| |S|

<!-- b000153 | prose | pages [12] -->
which is the fraction of the search area that would need to be searched in prioritized order before ﬁnding the next crime location. Note that a lower value for the hit score is preferable.

<!-- b000154 | heading | pages [12] -->
3.4 Model Accuracy for a Particular Criminal

<!-- b000155 | prose | pages [12] -->
Given an active serial criminal, we wish to determine the accuracy to which the criminal’s spatial behavior is determined by a model. This is important information for law enforcement agencies basing investigative decisions on a geographical proﬁling method, since they want to know the extent to which they can trust a model as it is applied to a particular criminal.

<!-- b000156 | prose | pages [12] -->
We calculate model accuracy for a given serial criminal in the follow- ing way. Given a geographical proﬁling method with associated probability function P, we wish to determine the accuracy score of the method, de- noted Z.

<!-- b000157 | prose | pages [12] -->
Let Hk denote the hit score that considers x1, . . . , xk−1 as the currently known crime locations, and treats xk as the next crime location. Then,

<!-- b000158 | prose | pages [12] -->
n 1 X Z = Hk n −3 k=4

<!-- b000159 | prose | pages [12] -->
is the mean of the hit scores determined by sequentially adding each crime location, starting with the fourth, to the set of currently known crimes. We start with the fourth crime because criminal behavior is not generally considered serial until the criminal has committed at least three crimes [1]. Note that a lower value for the accuracy score represents a more accurate model.

<!-- b000160 | furniture | pages [13] -->
Team number 7947

<!-- b000161 | furniture | pages [13] -->
Page 10 of 25

<!-- b000162 | heading | pages [13] -->
3.5 Search Area Determination

<!-- b000163 | prose | pages [13] -->
Our notions of performance and accuracy depend heavily on the size of the search area. The hit score can be made arbitrarily small by increasing the size of the search area. This is because additional locations on the periphery of the search area are unlikely to be the next crime location, but these additional locations are included in the total search area.

<!-- b000164 | prose | pages [13] -->
Surprisingly, literature that uses the hit score performance metric does not explicitly address how the search area is to be determined given previous crime locations. We take the search area to be a square centered at the mean location of the previous crimes, with side length equal to double the maximum pairwise distance between previous crimes. In an ongoing serial criminal investigation the search area could be provided by law enforcement, but for our purposes the above search area balances the size of the search area based on previous crime distances.

<!-- b000165 | heading | pages [13] -->
4 Individual Models

<!-- b000166 | heading | pages [13] -->
4.1 Spatial Models

<!-- b000167 | prose | pages [13] -->
In this section we consider geographical proﬁling methods that only take into account the spatial data of serial crimes.

<!-- b000168 | prose | pages [13] -->
We consider the following spatial models for the calculation of P(Si,j):

<!-- b000169 | prose | pages [13] -->
• Random Method: The random method assigns each P(Si,j) a ran- dom value uniformly. Theoretically, we expect the hit score of the random method to be 0.5 [14]. We include the random method as a basis for comparison of other geographical proﬁling methods.

<!-- b000170 | prose | pages [13] -->
• Standard Deviation Methods: Since standard deviation methods give no information about the distribution of probabilities inside the standard deviation areas, we cannot meaningfully compare them to other methods. Regardless, we include standard deviation methods in this paper because they are the most basic geographical proﬁling methods. These methods provide a rudimentary way by which the potential search area can be narrowed. We consider the following standard deviation methods:

<!-- b000171 | furniture | pages [14] -->
Team number 7947

<!-- b000172 | furniture | pages [14] -->
Page 11 of 25

<!-- b000173 | prose | pages [14] -->
– Standard Deviation Rectangles: These are rectangular areas deﬁned by the points

<!-- b000174 | prose | pages [14] -->
(−c σlon, −c σlat) x + (−c σlon, c σlat) x + x + (c σlon, c σlat) (c σlon, −c σlat) x +

<!-- b000175 | prose | pages [14] -->
where x is the centroid of the crime locations, and σlon and σlat are the standard deviations of the longitudes and latitudes of the crime locations [15].

<!-- b000176 | prose | pages [14] -->
– Standard Deviation Ellipses: These are elliptical areas, ori- ented along the trend line of the data in the least-squares sense.

<!-- b000177 | prose | pages [14] -->
A standard deviation ellipse is an ellipse with its center at the centroid of the crime locations, rotated clockwise by an angle θ, and with axis lengths given by 2cσlon and 2cσlat, where θ, σlon, and σlat are calculated as in [16].

<!-- b000178 | prose | pages [14] -->
In both of the above methods, c is a constant that determines the range of the area. Common values are c = 1 for the 68th percentile area and c = 2 for the 95th percentile area. See Figure 7 for an illustration of these percentile areas.

<!-- b000179 | prose | pages [14] -->
• Centralization Methods: Centralization methods determine a cen- tral focal point for the spatial pattern of the serial criminal. In these models, the probability of the next crime decreases the further the location is from the focal point. Thus, in all these methods, given a central focal point C ∈A, we have

<!-- b000180 | prose | pages [14] -->
1 P(Si,j) = d(Si,j, C)

<!-- b000181 | prose | pages [14] -->
We consider the following ways of determining the central focal point:

<!-- b000182 | prose | pages [14] -->
– Centroid: The central focal point is the mean of the locations of the crimes, given by

<!-- b000183 | prose | pages [14, 15] -->
n C = 1 X xi n i=1 – Harmonic Mean: The central focal point is the harmonic mean of the locations of the crimes, given by

<!-- b000184 | furniture | pages [15] -->
Team number 7947

<!-- b000185 | furniture | pages [15] -->
Page 12 of 25

<!-- b000187 | prose | pages [15] -->
n C = 1 Pn i=1 xi

<!-- b000188 | prose | pages [15] -->
– Circle Center: The central focal point is the mean location of the two crime locations farthest away from each other. This is de- termined as follows. Let xi, xj be such that d(xi, xj) is maximal.

<!-- b000189 | prose | pages [15] -->
Then we have C = xi + xj . 2 – Median: The central focal point is deﬁned as the point that is the median of the of the longitudes and the median of the latitudes of the crime locations. Compared to the other cen- tralization methods, the median is less sensitive to distant crime locations, which the criminal might have chosen for no particular spatial reason [9].

<!-- b000190 | prose | pages [15] -->
• Probability Distance Method: The probability distance method takes into account a location’s distance from each particular previous crime location. In this model, a probable next crime location would be relatively close to multiple previous crimes. Thus, we have

<!-- b000191 | prose | pages [15] -->
n X P(Si,j) = f(d(Si,j, xk)) k=1

<!-- b000192 | prose | pages [15] -->
where f is a distance decay function deﬁned in one of the following ways:

<!-- b000193 | prose | pages [15] -->
– Linear Distance Decay: The probability of the next crime location decreases linearly away from a particular previous crime location, given by f(d) = α−βd, where α, β are decay constants.

<!-- b000194 | prose | pages [15] -->
– Exponential Distance Decay: The probability of the next crime location decreases exponentially away from a particular previous crime location, given by f(d) = e−γd, where γ is a decay constant.

<!-- b000195 | prose | pages [15] -->
For an illustrative example of the diﬀerence between centralization methods and the probability distance method see Figure 2.

<!-- b000196 | furniture | pages [16] -->
Team number 7947

<!-- b000197 | furniture | pages [16] -->
Page 13 of 25

<!-- b000198 | prose | pages [16] -->
2.0 2.0 low               Next Crime Probability               high low               Next Crime Probability               high 1.5 1.5

<!-- b000199 | prose | pages [16] -->
1.0 1.0

<!-- b000200 | prose | pages [16] -->
0.5 0.5

<!-- b000201 | prose | pages [16] -->
0.0 0.0

<!-- b000202 | prose | pages [16] -->
0.5 0.5

<!-- b000203 | prose | pages [16] -->
1.0 1.0

<!-- b000204 | prose | pages [16] -->
1.5 1.5

<!-- b000205 | prose | pages [16] -->
2.0 2.0 1.5 1.5 1.5 1.5 2.0 1.0 0.5 0.0 0.5 1.0 2.0 2.0 1.0 0.5 0.0 0.5 1.0 2.0

<!-- b000206 | prose | pages [16] -->
(a) Centroid centralization method on (b) Exponential decay method on the the unit circle unit circle

<!-- b000207 | caption | pages [16] -->
Figure 2: Comparison of prioritized search areas of a hypothetical criminal com-

<!-- b000208 | prose | pages [16] -->
mitting crimes along the unit circle given by a centralization method and a decay method.

<!-- b000209 | heading | pages [16] -->
4.2 Spatiotemporal Models

<!-- b000210 | prose | pages [16] -->
In this section we consider geographical proﬁling methods that take into account both the spatial and temporal data of serial crimes. The additional use of temporal data is motivated by the idea that recent crime locations are more relevant to the spatial behavior of a serial criminal than older crime locations. For example, if the serial criminal is traveling while committing crimes, then old crime location information quickly becomes outdated. For an example of this, see Figure 3.

<!-- b000211 | prose | pages [16] -->
Not all of the spatial models in Section 4.1 have extensions that incorpo- rate temporal data. For example, the circle center centralization method has no spatiotemporal analog, since the longest pairwise distance is unaﬀected by temporal data.

<!-- b000212 | prose | pages [16] -->
To incorporate the temporal components of the crime data, we calculate a temporal weighting factor for each crime,

<!-- b000213 | prose | pages [16] -->
wi = ti −t1 + k tn

<!-- b000214 | prose | pages [16] -->
where wi denotes the temporal weight of the ith crime. The oﬀset k is included so that the ﬁrst crime will not be given a weight of 0. We chose k = 0.1 so that the last crime is weighted approximately ten times more heavily than the ﬁrst crime. Let W denote the sum of the temporal weights.

<!-- b000215 | furniture | pages [17] -->
Team number 7947

<!-- b000216 | furniture | pages [17] -->
Page 14 of 25

<!-- b000217 | prose | pages [17] -->
low               Next Crime Probability               high low               Next Crime Probability               high 5 5

<!-- b000218 | prose | pages [17] -->
0 0

<!-- b000219 | prose | pages [17] -->
5 5

<!-- b000220 | prose | pages [17] -->
5 5 0 10 0 10

<!-- b000221 | prose | pages [17] -->
(a) Exponential Decay (b) Temporal Exponential Decay

<!-- b000222 | caption | pages [17] -->
Figure 3: Prioritized search area for a hypothetical serial criminal travelling east

<!-- b000223 | prose | pages [17] -->
over time, as given by the exponential decay and temporal exponential decay mod- els.

<!-- b000224 | prose | pages [17] -->
We modify the following spatial models to consider the temporal weight- ing factors:

<!-- b000225 | prose | pages [17] -->
• Centralization Methods:

<!-- b000226 | prose | pages [17] -->
– Temporal Centroid: The mean of the locations of the crimes, weighted by time, given by

<!-- b000227 | prose | pages [17] -->
n C = 1 X xiwi W i=1

<!-- b000228 | prose | pages [17] -->
– Temporal Harmonic Mean: The harmonic mean of the loca- tions of the crimes, weighted by time, given by

<!-- b000229 | prose | pages [17] -->
W C = Pn wi i=1 xi

<!-- b000230 | prose | pages [17] -->
• Temporal Probability Distance Methods: The linear distance decay and exponential distance decay methods incorporate the tem- poral weight data by using the following modiﬁed probability function:

<!-- b000231 | prose | pages [17, 18] -->
n X P(Si,j) = wkf(d(Si,j, xk)) k=1 Uniform Random Centroid Temporal Centroid Harmonic Temporal Harmonic Circle Center Median Exponential Decay Temporal Exponential Decay Linear Decay Temporal Linear Decay 0.0 0.1 0.2 0.3 0.4 0.5 Hit Score

<!-- b000232 | furniture | pages [18] -->
Team number 7947

<!-- b000233 | furniture | pages [18] -->
Page 15 of 25

<!-- b000235 | caption | pages [18] -->
Figure 4: Comparison of the relative performance of each of our models on all of

<!-- b000236 | prose | pages [18] -->
our data sets.

<!-- b000237 | heading | pages [18] -->
4.3 Individual Model Results

<!-- b000238 | prose | pages [18] -->
To investigate the eﬀectiveness of each of the aforementioned models, we calculated the mean hit score across all of our data sets. After three crimes have been observed we apply our model and record the hit score for the next crime. This process is repeated for all subsequent crimes in the series.

<!-- b000239 | prose | pages [18] -->
The value of the constants in the linear and exponential decay models do not eﬀect the hit score. This is because the hit score is not aﬀected by the magnitude of the probability of the sector but by the relative probability to the rest of the search area. Consequently for an individual model the values of the constants have no eﬀect.

<!-- b000240 | prose | pages [18] -->
First we investigate the overall performance of each of the models. This can be found in Table 2 and in Figure 4. All of our models signiﬁcantly outperform the random model, but each of the individual models is not statistically superior to any other.

<!-- b000241 | furniture | pages [19] -->
Team number 7947

<!-- b000242 | furniture | pages [19] -->
Page 16 of 25

<!-- b000243 | prose | pages [19] -->
Next we investigate the performance of our models based upon the num- ber of crimes observed as seen in Figure 5. No patterns emerge that would indicate that the performance of the model improves having observed more crimes. The data sets considered do not have suﬃcient data to rule out such a correlation, particularly with the longer streaks as there are only a few data points.

<!-- b000244 | prose | pages [19] -->
0.35

<!-- b000245 | prose | pages [19] -->
0.30

<!-- b000246 | prose | pages [19] -->
0.25

<!-- b000247 | prose | pages [19] -->
0.20 Hit score 0.15

<!-- b000248 | prose | pages [19] -->
0.10

<!-- b000249 | prose | pages [19] -->
0.05

<!-- b000250 | prose | pages [19] -->
0.00 4 14 2 6 8 10 12 Number of crimes observed

<!-- b000251 | caption | pages [19] -->
Figure 5: Hit score by number of crimes observed using a exponential decay model

<!-- b000252 | prose | pages [19] -->
and 50% conﬁdence intervals.

<!-- b000253 | heading | pages [19] -->
5 Aggregation Models

<!-- b000254 | prose | pages [19] -->
In this section we consider ways of combining predictions from multiple geographical proﬁling methods into one model. The motivation behind these aggregate approaches is that each of the individual models described in Sections 4.1 and 4.2 have strengths and weaknesses, but by aggregating several models we hope enhance the strengths and reduce the weaknesses.

<!-- b000255 | prose | pages [19, 20] -->
This issue of aggregation of models relates to the classic problem of Model Hit Score 95% Conﬁdence Random 0.500 0.001 Centroid Centralization 0.104 0.031 Temporal Centroid Centralization 0.106 0.031 Harmonic Mean Centralization 0.105 0.031 Temporal Harmonic Mean Centralization 0.106 0.031 Circle Center Centralization 0.116 0.029 Median Centralization 0.123 0.042 Exponential Decay 0.094 0.030 Temporal Exponential Decay 0.092 0.029 Linear Decay 0.125 0.043 Temporal Linear Decay 0.123 0.043

<!-- b000256 | furniture | pages [20] -->
Team number 7947

<!-- b000257 | furniture | pages [20] -->
Page 17 of 25

<!-- b000259 | caption | pages [20] -->
Table 2: Models with associated hit scores and 95% conﬁdence intervals.

<!-- b000260 | prose | pages [20] -->
aggregating expert predictions. Consequently, there exist several diﬀerent techniques for aggregating these models. These techniques can be catego- rized as either axiomatic or Bayesian. Clemen and Winkler reported no signiﬁcant diﬀerence in the performance of more complex Bayesian models with more simple axiomatic approaches [17], and as such we have chosen to focus on the more elementary axiomatic approaches.

<!-- b000261 | heading | pages [20] -->
Axiomatic Approaches: Given n models that we wish to aggregate,

<!-- b000262 | prose | pages [20] -->
let Pk(Si,j) denote the probability that a particular sector contains the next crime as predicted by the kth model. Let Wk denote the aggregation weight of the kth model, given such that all Wk’s sum to one.

<!-- b000263 | prose | pages [20] -->
• Linear Opinion Pool: This model is a linear combination of two or more probability distribution functions produced by individual models.

<!-- b000264 | prose | pages [20] -->
n X P(Si,j) = WkPk(Si,j) k=1

<!-- b000265 | prose | pages [20] -->
Examples of this model and the eﬀect of diﬀerent weights can be found in Figure 6.

<!-- b000266 | prose | pages [20] -->
• Logarithmic Opinion Pool: This model is a weighted product of two or more probability distribution functions.

<!-- b000267 | prose | pages [20, 21] -->
n Y Pk(Si,j)Wk P(Si,j) = k=1 39.5 39.5 low               Next Crime Probability               high low               Next Crime Probability               high 39.0 39.0

<!-- b000268 | furniture | pages [21] -->
Team number 7947

<!-- b000269 | furniture | pages [21] -->
Page 18 of 25

<!-- b000271 | prose | pages [21] -->
38.5 38.5

<!-- b000272 | prose | pages [21] -->
38.0 38.0

<!-- b000273 | prose | pages [21] -->
37.5 37.5 48 km 48 km 78.0 77.5 77.0 76.5 76.0 78.0 77.5 77.0 76.5 76.0

<!-- b000274 | prose | pages [21] -->
(a) Exponential decay weight 0.00, (b) Exponential decay weight 0.25, Circle center weight 1.00 Circle center weight 0.75

<!-- b000275 | prose | pages [21] -->
39.5 39.5 low               Next Crime Probability               high low               Next Crime Probability               high 39.0 39.0

<!-- b000276 | prose | pages [21] -->
38.5 38.5

<!-- b000277 | prose | pages [21] -->
38.0 38.0

<!-- b000278 | prose | pages [21] -->
37.5 37.5 48 km 48 km 78.0 77.5 77.0 76.5 76.0 78.0 77.5 77.0 76.5 76.0

<!-- b000279 | prose | pages [21] -->
(c) Exponential decay weight 0.50, (d) Exponential decay weight 0.75, Circle center weight 0.50 Circle center weight 0.25

<!-- b000280 | prose | pages [21] -->
39.5 low               Next Crime Probability               high 39.0

<!-- b000281 | prose | pages [21] -->
38.5

<!-- b000282 | prose | pages [21] -->
38.0

<!-- b000283 | prose | pages [21] -->
37.5 48 km 78.0 77.5 77.0 76.5 76.0

<!-- b000284 | prose | pages [21] -->
(e) Exponential decay weight 1.00, Circle center weight 0.00

<!-- b000285 | caption | pages [21] -->
Figure 6: Prioritized search areas resulting from using diﬀerent weights in the

<!-- b000286 | prose | pages [21] -->
aggregation model of a circle center and exponential decay for the Beltway Sniper.

<!-- b000287 | furniture | pages [22] -->
Team number 7947

<!-- b000288 | furniture | pages [22] -->
Page 19 of 25

<!-- b000289 | prose | pages [22] -->
In the exponential decay and the linear decay spatial models described in Section 4.1, we noted the value of the constants chosen for the model has no impact on the hit score metric. In an aggregate model this is not the case, as the relative magnitude of probability is important when added or multiplied by another model.

<!-- b000290 | prose | pages [22] -->
To set these parameters we used the mean pairwise distance. We deﬁne the mean pairwise distance to be the mean distance between any two crimes

<!-- b000291 | prose | pages [22] -->
2 X δ = d(xi, xj) n(n −1) 1≤i<j≤n

<!-- b000292 | prose | pages [22] -->
In the case of the linear decay model, α was chosen to be 1 and β was chosen q 2 such that α −βδ = 0. In the case of the exponential decay, we set γ = δ, which gives a mean distance to crime of δ 2. We believed these values would provide a reasonable magnitude of probability when compared with other models.

<!-- b000293 | heading | pages [22] -->
5.1 Aggregation Model Results

<!-- b000294 | prose | pages [22] -->
To investigate the beneﬁts of aggregation models, we used a 2k factorial experimental design [18]. For each of our models described in Section 4, we investigated two possible scenarios: the model was included in the aggregate and weighted equally with the others, and the model was not included. We then computed the mean hit score for the resultant aggregate model for all possible models on all of our data sets.

<!-- b000295 | prose | pages [22] -->
While a further optimization process could be conducted in which more weights or diﬀerent decay constants were investigated, this process allowed us to see the eﬀect of diﬀerent models on the aggregate as well as see which individual models produce a strong aggregate model.

<!-- b000296 | prose | pages [22] -->
Through this process we found the strongest combination of individual models used the temporal exponential decay and the circle center centraliza- tion each equally weighted. The mean hit score for the linear opinion pool was 0.081 ± 0.027 with a 95% conﬁdence interval. The logarithmic opinion pool did not perform any better than any individual model. Neither model is statistically better than any of our other models.

<!-- b000297 | furniture | pages [23] -->
Team number 7947

<!-- b000298 | furniture | pages [23] -->
Page 20 of 25

<!-- b000299 | heading | pages [23] -->
6 Peter Sutcliﬀe: A Case Study

<!-- b000300 | prose | pages [23] -->
Peter Sutcliﬀe was a serial murderer who targeted women in England during the late 1970’s [19]. A map of his murders can be found in Figure 8(a). We have applied the models we have developed to predict where the next murder in the series would be if Sutcliﬀe had not been arrested and imprisoned.

<!-- b000301 | prose | pages [23] -->
54.2 54.2

<!-- b000302 | prose | pages [23] -->
54.0 54.0

<!-- b000303 | prose | pages [23] -->
53.8 53.8

<!-- b000304 | prose | pages [23] -->
53.6 53.6

<!-- b000305 | prose | pages [23] -->
53.4 53.4

<!-- b000306 | prose | pages [23] -->
53.2 53.2

<!-- b000307 | prose | pages [23] -->
53.0 53.0 20 km 20 km 2.6 2.4 2.2 2.0 1.8 1.6 1.4 1.2 2.6 2.4 2.2 2.0 1.8 1.6 1.4 1.2

<!-- b000308 | caption | pages [23] -->
Figure 7: Standard deviation rectangles and ellipses for the murders committed

<!-- b000309 | prose | pages [23] -->
by Peter Sutcliﬀe.

<!-- b000310 | prose | pages [23] -->
A common but na¨ıve method of identifying an area of high probability of serial crime generates a rectangle or ellipse in which a standard deviation of previous crimes have taken place. These rudimentary models can bee seen in Figure 7.

<!-- b000311 | prose | pages [23] -->
In Section 4.3, we found the individual model with the lowest mean hit score across our data set was the temporal exponential decay model. See

<!-- b000312 | caption | pages [23] -->
Figure 8 for an application of this model to the data for murders committed

<!-- b000313 | prose | pages [23] -->
by Peter Sutcliﬀe. The known crimes had a hit score of 10.6% using this model, so we use this percentage to ﬁnd a prioritized search area where we can be reasonably conﬁdent Sutcliﬀe would attack next. Of the 27818 km2, we can then isolate 2941 km2 in which to concentrate the search eﬀort.

<!-- b000314 | heading | pages [23] -->
7 Conclusions

<!-- b000315 | prose | pages [23] -->
• Every geographical proﬁling method outperformed the ran- dom method: On our data set, every geographical proﬁling method provided a signiﬁcant improvement in hit score over the random method.

<!-- b000316 | prose | pages [23, 24] -->
• All non-random geographical proﬁling methods considered exhibited roughly the same performance: Diﬀerences in the hit (a) Locations of Peter Sutcliﬀe murders. Map generated via Google Static Maps API [20].

<!-- b000317 | furniture | pages [24] -->
Team number 7947

<!-- b000318 | furniture | pages [24] -->
Page 21 of 25

<!-- b000320 | prose | pages [24] -->
low               Next Crime Probability               high 54.2

<!-- b000321 | prose | pages [24] -->
54.0

<!-- b000322 | prose | pages [24] -->
53.8

<!-- b000323 | prose | pages [24] -->
53.6

<!-- b000324 | prose | pages [24] -->
53.4

<!-- b000325 | prose | pages [24] -->
53.2

<!-- b000326 | prose | pages [24] -->
53.0 20 km

<!-- b000327 | prose | pages [24] -->
1.4 2.6 2.4 2.2 2.0 1.8 1.6 1.2

<!-- b000328 | prose | pages [24] -->
(b) Temporal exponential decay model applied to Peter Sutcliﬀe murders.

<!-- b000329 | caption | pages [24] -->
Figure 8: Comparison of the prioritized search area produced by the temporal

<!-- b000330 | prose | pages [24] -->
exponential decay model to the map of the geographical area of murders committed by Peter Sutcliﬀe. This prioritized search area suggests that the Bradford area is at the highest risk of attack.

<!-- b000331 | furniture | pages [25] -->
Team number 7947

<!-- b000332 | furniture | pages [25] -->
Page 22 of 25

<!-- b000333 | prose | pages [25] -->
score for diﬀerent spatial, spatiotemporal, and aggregation methods were statistically insigniﬁcant, indicating that all the geographical pro- ﬁling methods have the same level of performance. This is a similar conclusion reached by Snook et al., who show that complex geograph- ical proﬁling methods are no more accurate than simple geographical proﬁling methods [4].

<!-- b000334 | prose | pages [25] -->
• Particular geographical proﬁling methods are not applicable to all serial criminals: We can see in Table 1 that the accuracy of our best individual geographical proﬁling method varied largely de- pending on the particular serial criminal being studied. For example, our best individual method, the temporal exponential decay method, is an accurate predictor of the D.C. sniper attacks (with an accuracy of 0.056), but is grossly inaccurate when applied to the serial rapist in Columbus, OH (with an accuracy of 0.533, which is worse than the random method).

<!-- b000335 | heading | pages [25] -->
8 Future Work

<!-- b000336 | prose | pages [25] -->
• Standardization of data set: It is currently diﬃcult to compare geographical proﬁling method performance to previous research be- cause each study uses a diﬀerent set of serial crime data to determine performance results. An eﬀort to compile a large, comprehensive list of serial crime data to which all methods would be compared would greatly help the development of geographical proﬁling techniques.

<!-- b000337 | prose | pages [25] -->
• Use of other relevant geographical information: In this pa- per we only consider the spatiotemporal relationships between crimes.

<!-- b000338 | prose | pages [25] -->
Work by O’Leary and Brown et al. develop the notion of a feature space that groups crime locations by their relevant geographical fea- tures, such as population density or proximity to a major highway [12, 11]. The probability that a future crime happens at a particular location is then determined by the proximity of the location to previ- ous crimes in the feature space. Having more information about what connects crime locations could potentially improve our geographical proﬁling methods.

<!-- b000339 | prose | pages [25, 26] -->
• Use of relevant information about the criminal: Research sug- gests that characteristics of the criminal, such as gender, race, and age, play a role in determining their probable spatial behavior [9, 5, 10].

<!-- b000340 | furniture | pages [26] -->
Team number 7947

<!-- b000341 | furniture | pages [26] -->
Page 23 of 25

<!-- b000343 | prose | pages [26] -->
By taking these factors into account, we may be able to improve the accuracy of our models for a speciﬁc criminal.

<!-- b000344 | prose | pages [26] -->
• Evaluation of cost to law enforcement: Law enforcement agen- cies typically purchase computer-generated geographical proﬁling in- formation [4, 7]. Research by Snook et al. suggests that a person with minimal training in geographical proﬁling techniques can determine the probable residence of a serial criminal with just as much accuracy as a complex computer-generated geographical proﬁling method [8].

<!-- b000345 | prose | pages [26] -->
Further research should be done to determine if the cost of proprietary geographical proﬁling software is worth the quality of the information provided to law enforcement agencies.

<!-- b000346 | furniture | pages [27] -->
Team number 7947

<!-- b000347 | furniture | pages [27] -->
Page 24 of 25

<!-- b000348 | heading | pages [27] -->
References

<!-- b000349 | references | pages [27] -->
[1] Ronald M. Holmes and Stephen T. Holmes.

<!-- b000350 | references | pages [27] -->
Serial Murder.

<!-- b000351 | references | pages [27] -->
SAGE

<!-- b000352 | references | pages [27] -->
Publications, Thousand Oaks, California, 1998.

<!-- b000353 | references | pages [27] -->
[2] Donald Brown and Justin Stile. Geographic proﬁling with event predic-

<!-- b000354 | references | pages [27] -->
tion. Systems, Man and Cybernetics, 2003. IEEE International Con-

<!-- b000355 | references | pages [27] -->
ference on, 4:3712–3719, 2003.

<!-- b000356 | references | pages [27] -->
[3] Scotia J. Hicks and Bruce D. Sales. Criminal Proﬁling: Developing an

<!-- b000357 | references | pages [27] -->
Eﬀective Science and Practice.

<!-- b000358 | references | pages [27] -->
American Psychological Association,

<!-- b000359 | references | pages [27] -->
Washington, DC, 2006.

<!-- b000360 | references | pages [27] -->
[4] Brent Snook, Michele Zito, Craig Bennell, and Paul J. Taylor. On the

<!-- b000361 | references | pages [27] -->
complexity and accuracy of geographic proﬁling strategies. Journal of

<!-- b000362 | references | pages [27] -->
Quantitative Criminology, 21(1):1–26, 2005.

<!-- b000363 | references | pages [27] -->
[5] Brent Snook, Richard M. Cullen, Andreas Mokros, and Stephan Har-

<!-- b000364 | references | pages [27] -->
bort. Serial murderers’ spatial descisions: Factors that inﬂuence crime

<!-- b000365 | references | pages [27] -->
location choice. Journal of Investigative Psychology and Oﬀender Pro-

<!-- b000366 | references | pages [27] -->
ﬁling, 2(3):147–164, 2005.

<!-- b000367 | references | pages [27] -->
[6] D. Kim Rossmo. Place, space, and police investigations: Hunting se-

<!-- b000368 | references | pages [27] -->
rial violent criminals. In Crime and Place: Crime Prevention Studies.

<!-- b000369 | references | pages [27] -->
Willow Tree Press, NY, 1995.

<!-- b000370 | references | pages [27] -->
[7] D. Kim Rossmo. Geographic proﬁling: Target patterns of serial mur-

<!-- b000371 | references | pages [27] -->
derers. Unpublished doctoral dissertation, 1995.

<!-- b000372 | references | pages [27] -->
[8] Brent Snook, Paul J. Taylor, and Craig Bennell.

<!-- b000373 | references | pages [27] -->
Shortcuts to geo-

<!-- b000374 | references | pages [27] -->
graphic proﬁlling success: A reply to Rossmo (2005). Applied Cognitive

<!-- b000375 | references | pages [27] -->
Psychology, 19(5):655–661, 2005.

<!-- b000376 | references | pages [27] -->
[9] Jasper J. van der Kemp and Peter J. van Koppen. Fine-Tuning Ge-

<!-- b000377 | references | pages [27] -->
ographical Proﬁling, chapter 17.

<!-- b000378 | references | pages [27] -->
Criminal Proﬁling. Humana Press,

<!-- b000379 | references | pages [27] -->
2007.

<!-- b000380 | references | pages [27] -->
[10] Eric Beauregard, Jean Proulx, and D. Kim Rossmo. Spatial patterns of

<!-- b000381 | references | pages [27] -->
sex oﬀenders: Theoretical, empirical, and practical issues. Aggression

<!-- b000382 | references | pages [27] -->
and Violent Behavior, 10(5):579–603, 2005.

<!-- b000383 | references | pages [27] -->
[11] Donald Brown and Hua Liu.

<!-- b000384 | references | pages [27] -->
Spatial-temporal event prediction: A

<!-- b000385 | references | pages [27] -->
new model. Systems, Man, and Cybernetics, 1998. IEEE International

<!-- b000386 | references | pages [27] -->
Conference on, 3:2933–2937, 1998.

<!-- b000387 | furniture | pages [28] -->
Team number 7947

<!-- b000388 | furniture | pages [28] -->
Page 25 of 25

<!-- b000389 | references | pages [28] -->
[12] Mike O’Leary. The mathematics of geographic proﬁling. Journal of

<!-- b000390 | references | pages [28] -->
Investigative Psychology and Oﬀender Proﬁling, 6(3):253–265, 2009.

<!-- b000391 | references | pages [28] -->
[13] Spotcrime.com.

<!-- b000392 | references | pages [28] -->
http://www.spotcrime.com. Accessed on February

<!-- b000393 | references | pages [28] -->
19, 2010.

<!-- b000394 | references | pages [28] -->
[14] D. Kim Rossmo. Geographic heuristics or shortcuts to failure?: Re-

<!-- b000395 | references | pages [28] -->
sponse to Snook et al. Applied Cognitive Psychology, 19(5):651–654,

<!-- b000396 | references | pages [28] -->
2005.

<!-- b000397 | references | pages [28] -->
[15] Steven Gottlieb, Sheldon Arenberg, and Raj Singh. Crime Analysis:

<!-- b000398 | references | pages [28] -->
From First Report to Final Arrest. Alpha, 1994.

<!-- b000399 | references | pages [28] -->
[16] Joshua Kent and Michael Leitner.

<!-- b000400 | references | pages [28] -->
Eﬃcacy of standard deviational

<!-- b000401 | references | pages [28] -->
ellipses in the application of criminal geographic proﬁling. 4(3):147–

<!-- b000402 | references | pages [28] -->
165, 2007.

<!-- b000403 | references | pages [28] -->
[17] Robert T. Clemen and Robert L. Winkler.

<!-- b000404 | references | pages [28] -->
Aggregating probability

<!-- b000405 | references | pages [28] -->
distributions. In Advances in Decision Analysis. Cambridge University

<!-- b000406 | references | pages [28] -->
Press, Cambridge, UK, 2007.

<!-- b000407 | references | pages [28] -->
[18] Averill M. Law. Simulation Modeling and Analysis. McGraw-Hill, 3rd

<!-- b000408 | references | pages [28] -->
edition, 2000.

<!-- b000409 | references | pages [28] -->
[19] Nicole Ward Jouve. ’The Streetcleaner’ The Yorkshire Ripper Case on

<!-- b000410 | references | pages [28] -->
Trial. Marion Boyars Publishers, London, 1986.

<!-- b000411 | references | pages [28] -->
[20] Google Static Maps API.

<!-- b000412 | references | pages [28] -->
http://code.google.com/apis/maps/

<!-- b000413 | references | pages [28] -->
documentation/staticmaps/. Accessed on February 22, 2010.
