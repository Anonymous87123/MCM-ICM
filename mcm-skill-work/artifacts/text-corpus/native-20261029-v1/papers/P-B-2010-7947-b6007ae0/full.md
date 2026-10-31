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
We consider standard deviation, centralization, and probability distance methods for prioritizing a given search area.

<!-- b000006 | prose | pages [1] -->
We also develop analogous methods which weight the spatial data of recent crimes more heavily. We then develop ways of aggregating results from multiple methods.

<!-- b000007 | prose | pages [1] -->
The performance of a geographical proﬁling method is based on its ef- fectiveness in narrowing down a particular search area into regions likely to contain the next crime location. The accuracy of a method for a particu- lar serial criminal is based on the past performance of the method on the spatiotemporal data of that criminal.

<!-- b000008 | prose | pages [1] -->
All of our methods produce a prioritized search area in which the next crime occurs in approximately the top 10% of the search area, a signiﬁcant improvement over a uniform random distribution. However, the diﬀerences in performance among the diﬀerent methods developed were statistically in- signiﬁcant. We also found the accuracy of our methods varied depending on the serial criminal under investigation.

<!-- b000009 | furniture | pages [2] -->
Team number 7947

<!-- b000010 | furniture | pages [2] -->
Page 1 of 2

<!-- b000011 | heading | pages [2] -->
Executive Summary

<!-- b000012 | prose | pages [2] -->
We have developed models to be used in an open investigation of a serial criminal. In this summary we describe how our models can best be employed to help identify probable next target locations of the serial criminal.

<!-- b000013 | prose | pages [2] -->
Our models use the locations and times of previous crimes committed by a serial criminal in order to predict the likely next target location. This prediction prioritizes the search area so that law enforcement resources can

<!-- b000014 | heading | pages [2] -->
be focused on the most probable next target regions. Our models prioritize

<!-- b000015 | prose | pages [2] -->
the search areas in diﬀerent fashions:

<!-- b000016 | heading | pages [2] -->
• Centralization models: These models are based on the assumption

<!-- b000017 | prose | pages [2] -->
that a serial criminal’s activity is centered around a point.

<!-- b000018 | heading | pages [2] -->
• Probability distance models: In these models, the closer a location

<!-- b000019 | prose | pages [2] -->
is to previous crimes, the higher the probability the serial criminal will strike there next.

<!-- b000020 | heading | pages [2] -->
• Time-based models: In these models, a location’s proximity to recent

<!-- b000021 | prose | pages [2] -->
crimes is weighted more heavily than its proximity to crimes in the distant past.

<!-- b000022 | prose | pages [2] -->
• Aggregate models: These models combine the above models.

<!-- b000023 | heading | pages [2] -->
There are multiple factors to consider when deciding if a particular model

<!-- b000024 | prose | pages [2] -->
is applicable to a serial criminal investigation:

<!-- b000025 | prose | pages [2] -->
• Evidence of serial nature: Our models assume that all of the ob- served crimes were committed by one criminal. If there is a strong

<!-- b000026 | heading | pages [2] -->
reason to doubt this assumption, such as the presence of a copy-cat

<!-- b000027 | prose | pages [2] -->
criminal, then our models are not applicable.

<!-- b000028 | heading | pages [2] -->
• Accuracy score: Our models provide a statistic that estimates their

<!-- b000029 | prose | pages [2] -->
accuracy as applied to the serial criminal under investigation. If our

<!-- b000030 | heading | pages [2] -->
models would not have performed well in predicting the locations of

<!-- b000031 | prose | pages [2] -->
this serial criminal’s past crimes, there is no reason to believe that

<!-- b000032 | heading | pages [2] -->
our models would accurately predict the location of the criminal’s next

<!-- b000033 | prose | pages [2] -->
crime.

<!-- b000034 | furniture | pages [3] -->
Team number 7947

<!-- b000035 | furniture | pages [3] -->
Page 2 of 2

<!-- b000036 | heading | pages [3] -->
• Available resources: Our models prioritize the search area such that

<!-- b000037 | prose | pages [3] -->
the next crime location is on average in the top 10% of the prioritized search area. This search area can still be prohibitively large to cover with the resources available to the investigation. If this search area is still too large to cover, then our models are still applicable but may not yield optimal results.

<!-- b000038 | prose | pages [3] -->
If it is determined that our models are applicable to a serial criminal inves- tigation, then there are multiple limitations of our models which need to be taken into consideration:

<!-- b000039 | heading | pages [3] -->
• Our models do not take into account relevant geographical

<!-- b000040 | prose | pages [3] -->
information: For example, if you know the serial criminal is targeting banks, our models do not take this into account. In this example, a list of bank locations can be cross-referenced against the prioritized search area given by our models to determine the banks that are likely to be targeted next.

<!-- b000041 | heading | pages [3] -->
• Our models do not take into account relevant information

<!-- b000042 | prose | pages [3] -->
about the criminal: The average distance that a serial criminal trav- els to commit a crime depends on the type of crime and characteristics

<!-- b000043 | heading | pages [3] -->
of the criminal, including gender, race, and age. Our models assume

<!-- b000044 | prose | pages [3] -->
no information of this type is known about the criminal.

<!-- b000045 | heading | pages [3] -->
• Our computer models may not outperform geographical pro-

<!-- b000046 | prose | pages [3] -->
ﬁling techniques employed by a human: Research has suggested that complex computer geographical proﬁling methods are no more accurate than an investigator with minimal training in geographical proﬁling techniques.

<!-- b000047 | heading | pages [3] -->
Overall, we recommend that our geographical proﬁling models not be used

<!-- b000048 | prose | pages [3] -->
as the only tool used in a serial criminal investigation. Instead, our models should complement traditional investigative techniques. It is our hope that our models can further aid law enforcement agencies in their pursuit of serial criminals.

<!-- b000049 | prose | pages [4] -->
Predicting a Serial Criminal’s Next Crime Location

<!-- b000050 | prose | pages [4] -->
Using Geographical Proﬁling

<!-- b000051 | prose | pages [4] -->
Control Group 7947

<!-- b000052 | prose | pages [4] -->
February 22, 2010

<!-- b000053 | heading | pages [4] -->
Abstract

<!-- b000054 | prose | pages [4] -->
Geographical proﬁling techniques can be useful to law enforcement agencies who are investigating a serial criminal. We develop such meth- ods that determine the probable location of a serial criminal’s next crime based on the spatiotemporal data of their previous crimes. We consider standard deviation, centralization, and probability distance methods for prioritizing a given search area, and also develop analogous methods which weight the spatial data of recent crimes more heavily. We then develop ways of aggregating results from multiple methods. The performance of a geographical proﬁling method is based on its eﬀectiveness in narrowing down a particular search area into regions likely to contain the next crime location. All of our methods produce a prioritized search area in which the next crime occurs in approximately the top 10% of the search area, a signiﬁcant improvement over a uni- form random distribution.

<!-- b000055 | prose | pages [4] -->
However, the diﬀerences in performance among the diﬀerent methods developed were statistically insigniﬁcant. We also found the accuracy of our methods varied depending on the serial criminal under investigation.

<!-- b000056 | prose | pages [4] -->
1

<!-- b000057 | furniture | pages [5] -->
Team number 7947

<!-- b000058 | heading | pages [5] -->
Contents

<!-- b000059 | contents | pages [5] -->
1

<!-- b000060 | heading | pages [5] -->
Introduction

<!-- b000061 | prose | pages [5] -->
2 Problem Background

<!-- b000062 | furniture | pages [5] -->
Page 2 of 25

<!-- b000063 | prose | pages [5] -->
3

<!-- b000064 | prose | pages [5] -->
3

<!-- b000065 | prose | pages [5] -->
Terminology . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.1

<!-- b000066 | prose | pages [5] -->
2.2 Survey of Current Literature

<!-- b000067 | prose | pages [5] -->
3

<!-- b000068 | prose | pages [5] -->
. . . . . . . . . . . . . . . . . .

<!-- b000069 | prose | pages [5] -->
4

<!-- b000070 | prose | pages [5] -->
. . . . . . . . . . . . . . . . . . . . . . . . 2.3 Collection of Data

<!-- b000071 | prose | pages [5] -->
3

<!-- b000072 | heading | pages [5] -->
Constructing a Model

<!-- b000073 | prose | pages [5] -->
5

<!-- b000074 | prose | pages [5] -->
7

<!-- b000075 | prose | pages [5] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1

<!-- b000076 | heading | pages [5] -->
Assumptions

<!-- b000077 | prose | pages [5] -->
7

<!-- b000078 | prose | pages [5] -->
Model Descriptions . . . . . . . . . . . . . . . . . . . . . . . . 3.2 7

<!-- b000079 | prose | pages [5] -->
Model Performance Metric . . . . . . . . . . . . . . . . . . . . 3.3 8

<!-- b000080 | prose | pages [5] -->
Model Accuracy for a Particular Criminal . . . . . . . . . . . 3.4

<!-- b000081 | prose | pages [5] -->
3.5 Search Area Determination

<!-- b000082 | prose | pages [5] -->
4

<!-- b000083 | heading | pages [5] -->
Individual Models

<!-- b000084 | prose | pages [5] -->
9

<!-- b000085 | prose | pages [5] -->
. . . . . . . . . . . . . . . . . . .

<!-- b000086 | prose | pages [5] -->
10

<!-- b000087 | prose | pages [5] -->
10

<!-- b000088 | prose | pages [5] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 Spatial Models 10

<!-- b000089 | prose | pages [5] -->
Spatiotemporal Models . . . . . . . . . . . . . . . . . . . . . . 4.2

<!-- b000090 | prose | pages [5] -->
4.3 Individual Model Results

<!-- b000091 | prose | pages [5] -->
5

<!-- b000092 | heading | pages [5] -->
Aggregation Models

<!-- b000093 | prose | pages [5] -->
5.1 Aggregation Model Results

<!-- b000094 | prose | pages [5] -->
6 Peter Sutcliﬀe: A Case Study

<!-- b000095 | prose | pages [5] -->
7

<!-- b000096 | heading | pages [5] -->
Conclusions

<!-- b000097 | prose | pages [5] -->
8

<!-- b000098 | heading | pages [5] -->
Future Work

<!-- b000099 | prose | pages [5] -->
13

<!-- b000100 | prose | pages [5] -->
. . . . . . . . . . . . . . . . . . . .

<!-- b000101 | prose | pages [5] -->
15

<!-- b000102 | prose | pages [5] -->
16

<!-- b000103 | prose | pages [5] -->
. . . . . . . . . . . . . . . . . . .

<!-- b000104 | prose | pages [5] -->
19

<!-- b000105 | prose | pages [5] -->
20

<!-- b000106 | prose | pages [5] -->
20

<!-- b000107 | prose | pages [5] -->
22

<!-- b000108 | furniture | pages [6] -->
Team number 7947

<!-- b000109 | furniture | pages [6] -->
Page 3 of 25

<!-- b000110 | prose | pages [6] -->
1

<!-- b000111 | heading | pages [6] -->
Introduction

<!-- b000112 | prose | pages [6] -->
Serial criminals present a unique challenge to law enforcement agencies. In a typical crime, investigators are able to draw a connection between the criminal and the victim. This information often provides enough clues to form the basis of a criminal investigation. In the case of serial criminals, however, there is usually no such relationship between the criminal and the victim [1, 2]. This lack of information about the serial criminal forces law enforcement agencies to consider a larger possible target area for the next crime, which hinders the investigation.

<!-- b000113 | prose | pages [6] -->
In order to better utilize limited law enforcement resources in a serial criminal investigation, geographical proﬁling can be used to determine likely next crime locations. Geographical proﬁling is “. . . a procedure that exam- ines the spatial behavior of oﬀenders with regard to the locations of their crime scenes and the spatial relationships between those scenes” [3]. By using geographical proﬁling, investigators are able to take advantage of the spatial patterns of a serial criminal to focus their attention on certain geo- graphically important regions.

<!-- b000114 | prose | pages [6] -->
In this paper we examine diﬀerent geographical proﬁling methodologies and compare their ability to predict the location of a serial criminal’s next crime. In Section 2, we provide the terminology and background informa- tion that will be utilized in the rest of the paper. In Section 3, we describe the features that are common to all geographical proﬁling methods devel- oped and our metrics for determining the performance and accuracy of a particular method. Section 4 develops geographical proﬁling methods and reports on their performance, and Section 5 considers combinations of these methods. In Section 6, we apply our best geographical proﬁling methods to the serial murders committed by Peter Sutcliﬀe. Section 7 summarizes our main conclusions, while Section 8 discusses possible avenues for future work.

<!-- b000115 | prose | pages [6] -->
2 Problem Background

<!-- b000116 | prose | pages [6] -->
2.1 Terminology

<!-- b000117 | prose | pages [6] -->
• Serial Criminal: A serial criminal is a habitual oﬀender who commits three or more related crimes over a span of time [1, 4]. We consider all

<!-- b000118 | furniture | pages [7] -->
Team number 7947

<!-- b000119 | furniture | pages [7] -->
Page 4 of 25

<!-- b000120 | prose | pages [7] -->
forms of serial criminals together, such as murderers, rapists, arsonists, and burglars.

<!-- b000121 | prose | pages [7] -->
• Spatiotemporal Data: The locations and corresponding times of crimes committed by a serial criminal.

<!-- b000122 | prose | pages [7] -->
• Spatial Behavior: The spatial behavior of a serial criminal describes how the serial criminal chooses crime locations [5, 6]. We model the spatial behavior of a criminal based on the spatiotemporal data of their previous crimes.

<!-- b000123 | prose | pages [7] -->
• Geographical Proﬁling Method: A geographical proﬁling method is a particular methodology for modeling the spatial behavior of a serial criminal.

<!-- b000124 | prose | pages [7] -->
We consider spatial methods that only consider the spatial data of previous crimes, spatiotemporal methods that also take into account the times of previous crimes, and aggregate methods that combine two or more geographical proﬁling methods.

<!-- b000125 | prose | pages [7] -->
• Prioritized Search Area: The area to search prioritized by the probability of the next crime given by a speciﬁc model. This area is important in determining how to allocate law enforcement resources.

<!-- b000126 | prose | pages [7] -->
2.2 Survey of Current Literature

<!-- b000127 | prose | pages [7] -->
There is an ongoing debate as to the eﬀectiveness of diﬀerent geographical proﬁling methodologies. Rossmo uses spatial data to determine the resi- dence of a criminal based on assumptions about spatial behavior, such as the tendency to commit crimes close, but not too close, to home [7]. As Rossmo’s paper lacks a detailed description of his algorithm, and relies on empirically determined constants, it is diﬃcult to reproduce his geograph- ical proﬁling methodology accurately [8, 7, 3].

<!-- b000128 | prose | pages [7] -->
Van der Kemp and van Koppen survey and criticize theories of spatial behavior, including theories of crime location proximity to the criminal’s residence and shortcomings of current geographical proﬁling methods [9]. Beauregard et al. and Snook et al. also examine the spatial behavior or serial criminals [10, 5]. Brown et al. take into account spatiotemporal data as well as additional features of the crime locations, such as proximity to highways, to predict crime locations [11, 2]. Recent work by O’Leary provides a mathematical foundation for geographical proﬁling [12].

<!-- b000129 | furniture | pages [8] -->
Team number 7947

<!-- b000130 | furniture | pages [8] -->
Page 5 of 25

<!-- b000131 | prose | pages [8] -->
We note that most of the work in the ﬁeld of geographical proﬁling focuses on identifying the residence of a serial criminal. This allows law enforcement agencies to cross-reference the addresses of potential suspects to the predicted residency of the criminal in order to narrow their search. In contrast, this paper focuses on identifying probable next crime locations in a series of linked crimes. Being able to forecast crime locations would assist law enforcement agencies in ways predicting the residency of the criminal does not. For example, law enforcement agencies would be able to increase patrols along probable crime locations, or alert high-risk neighborhoods to the existence of the serial criminal. Since serial criminals often center their crime locations around their residence [10], these two problems are related, and thus we are able to adapt methods of identifying the residence to the problem of identifying next crime locations.

<!-- b000132 | prose | pages [8] -->
2.3 Collection of Data

<!-- b000133 | prose | pages [8] -->
In order to determine the accuracy of proposed geographical proﬁling mod- els, we needed to see how the models performed against actual spatiotem- poral serial crime data. Unfortunately, there is no large collection of serial crime data to compare our models to, or a standard collection of serial crime data that is used across all geographical proﬁling research. A survey of spatial proﬁling research shows that the data sets used are varied, which leads to diﬀerent quantitative conclusions about the spatial behavior of se- rial criminals; see [9, 8, 10, 5] for contrasting conclusions based on diﬀerent data sets. For example, the circle center method described in Section 4.1 was found to have diﬀerent levels of accuracy for serial crime data sets from diﬀerent countries [4]. Ideally, we would be able to test our geographical proﬁling models against serial crime data that spanned multiple locations, crime types, and periods of time, but such a data set does not exist.

<!-- b000134 | prose | pages [8] -->
In most studies we considered, a sample of serial crime data was either obtained from a government agency or compiled from newspaper and police reports. Unfortunately, due to the constrained time frame of our study, we were unable to obtain data from police departments and government agen- cies. However, we were able to compile a data set consisting of the crimes of nine serial criminals, totaling 124 crimes. For the more notorious crimi- nals in this data set including the Beltway Snipers, Peter Sutcliﬀe, and Dale Hausner we were able to collect data directly from police reports and news articles. We collected data for the remaining crimes from SpotCrime.com, an online crime information source, and veriﬁed the data via the referenced

<!-- b000135 | furniture | pages [9] -->
Team number 7947

<!-- b000136 | furniture | pages [9] -->
Page 6 of 25

<!-- b000137 | prose | pages [9] -->
police reports and news articles [13]. A listing of the crimes in our data set can be found in Table 1.

<!-- b000138 | prose | pages [9] -->
Number Description Accuracy of Temporal of Crimes Murders committed by Pe- ter Sutcliﬀe in West York- shire, England

<!-- b000139 | prose | pages [9] -->
Beltway sniper attacks committed by John Allen Muhammad and Lee Boyd Malvo in the Washington, DC area

<!-- b000140 | prose | pages [9] -->
Murders, arsons, and other crimes committed by serial criminal Dale Hausner in Phoenix, AZ

<!-- b000141 | prose | pages [9] -->
Sexual assaults committed by a serial rapist in Colum- bus, OH

<!-- b000142 | prose | pages [9] -->
Serial robberies at TCF Banks in Frankin Park, IL area

<!-- b000143 | prose | pages [9] -->
Serial robberies committed in Denver, CO

<!-- b000144 | prose | pages [9] -->
Serial bank robberies com- mitted by “The With- drawal Bandit” in Boca Raton, FL

<!-- b000145 | prose | pages [9] -->
Serial robberies committed in Columbus, OH

<!-- b000146 | prose | pages [9] -->
Serial robberies and home invasions committed in Santa Monica, CA

<!-- b000147 | prose | pages [9] -->
Exponential Decay Model

<!-- b000148 | prose | pages [9] -->
12 12 0.048

<!-- b000149 | prose | pages [9] -->
14 14 0.065

<!-- b000150 | prose | pages [9] -->
40 40 0.098

<!-- b000151 | prose | pages [9] -->
7 7 0.517

<!-- b000152 | prose | pages [9] -->
12 12 0.180

<!-- b000153 | prose | pages [9] -->
6 6 0.103

<!-- b000154 | prose | pages [9] -->
12 12 0.119

<!-- b000155 | prose | pages [9] -->
7 7 0.020

<!-- b000156 | prose | pages [9] -->
14 14 0.174

<!-- b000157 | caption | pages [9] -->
Table 1: Description of data sets with accuracy score for temporal exponential

<!-- b000158 | prose | pages [9] -->
decay model.

<!-- b000159 | furniture | pages [10] -->
Team number 7947

<!-- b000160 | furniture | pages [10] -->
Page 7 of 25

<!-- b000161 | prose | pages [10] -->
3

<!-- b000162 | heading | pages [10] -->
Constructing a Model

<!-- b000163 | prose | pages [10] -->
3.1

<!-- b000164 | heading | pages [10] -->
Assumptions

<!-- b000165 | heading | pages [10] -->
• Spatiotemporal data is accurate: A common modeling assump-

<!-- b000166 | prose | pages [10] -->
tion.

<!-- b000167 | heading | pages [10] -->
• Crimes were committed by one serial criminal: Our models

<!-- b000168 | prose | pages [10] -->
are working on the assumption that all the crimes in a data set were committed by the same criminal, and thus the crime locations can be explained by a particular spatial behavior.

<!-- b000169 | prose | pages [10] -->
• Serial criminals do not act randomly: We assume the truth of rational crime theory, the notion that “. . . there is an underlying rea- son why criminals choose to commit crimes at a particular time in a particular location” [2]. Rational crime theory is a necessary condi- tion for productive geographical proﬁling, since if serial criminals are acting randomly, then the best model of their spatial behavior would be random as well.

<!-- b000170 | prose | pages [10] -->
3.2

<!-- b000171 | heading | pages [10] -->
Model Descriptions

<!-- b000172 | prose | pages [10] -->
Let x1, . . . , xn ∈A ⊂R2 denote crime scene locations of a serial crimi- nal, where A is a given search area encompassing the crime locations. Let t1, . . . , tn ∈R with 0 = t1 < . . . < tn denote the corresponding times of the crimes, where (xi, ti) is the spatiotemporal data of the ith crime. Given a location y ∈A, we deﬁne a probability function P such that P(y) is the probability that the next crime will happen at that location.

<!-- b000173 | prose | pages [10] -->
We discretize A into sectors Si,j in the order to simplify our calculations; see Figure 1 for a description of the discretization process. We assume that if y ∈Si,j, then P(y) = P(Si,j), the probability that the next crime location is in the sector. This is a reasonable assumption for small sector sizes relative to the total search area. Thus, the goal of a geographical proﬁling method is to determine P(Si,j) for all sectors.

<!-- b000174 | prose | pages [10] -->
For our models, let d be a given distance metric. This distance metric can be determined using a variety of methods, including standard Euclidean distances, Manhattan distances, or travel-time distances that take into ac- count the road map data of the area. We arbitrarily choose to use Euclidean

<!-- b000175 | furniture | pages [11] -->
Team number 7947

<!-- b000176 | furniture | pages [11] -->
Page 8 of 25

<!-- b000177 | prose | pages [11] -->
distances since we found no evidence that serial criminals evaluate distance using a certain metric, but our models do not make any assumptions about the nature of the distance function.

<!-- b000178 | caption | pages [11] -->
Figure 1: The discretization of a square search area into sectors. In this ﬁgure k

<!-- b000179 | prose | pages [11] -->
is equal to the side length of the search area divided by ∆s.

<!-- b000180 | prose | pages [11] -->
3.3

<!-- b000181 | heading | pages [11] -->
Model Performance Metric

<!-- b000182 | prose | pages [11] -->
There exist two commonly used metrics for the evaluation of the performance of a geographical proﬁling method. The ﬁrst measure is the error distance, which is the Euclidean distance between the most likely exact location of the next crime and the actual next crime location [8]. The second measure represents how much of the prioritized search area would need to be searched in order to ﬁnd the next crime location [12, 7].

<!-- b000183 | prose | pages [11] -->
Our model evaluation metric should reﬂect how useful these models would be to a law enforcement agency tracking a serial criminal. The most likely exact location of the next crime is not very valuable to law enforce- ment agencies, since often they are concerned with ﬁnding an area to search and not a particular point [12, 14, 7].

<!-- b000184 | prose | pages [11] -->
Thus, we consider the following metric that represents how much of the prioritized search area would need to be searched in order to ﬁnd the next crime location, which we call the hit score. Given a geographical proﬁling method with associated probability function P and a known next crime location xn+1, we wish to determine the hit score H.

<!-- b000185 | furniture | pages [12] -->
Team number 7947

<!-- b000186 | furniture | pages [12] -->
Page 9 of 25

<!-- b000187 | prose | pages [12] -->
Let L ∋xn+1 denote the sector Let S denote the set of all sectors. containing the next crime location. Then

<!-- b000188 | prose | pages [12] -->
B = {Si,j ∈S : P(Si,j) > P(L)}

<!-- b000189 | prose | pages [12] -->
is the set of all sectors that have a higher predicted probability than the sector containing the next crime. Thus, we have

<!-- b000190 | prose | pages [12] -->
H = |B|

<!-- b000191 | prose | pages [12] -->
|S|

<!-- b000192 | prose | pages [12] -->
which is the fraction of the search area that would need to be searched in prioritized order before ﬁnding the next crime location. Note that a lower value for the hit score is preferable.

<!-- b000193 | heading | pages [12] -->
Model Accuracy for a Particular Criminal

<!-- b000194 | prose | pages [12] -->
3.4

<!-- b000195 | prose | pages [12] -->
Given an active serial criminal, we wish to determine the accuracy to which the criminal’s spatial behavior is determined by a model. This is important information for law enforcement agencies basing investigative decisions on a geographical proﬁling method, since they want to know the extent to which they can trust a model as it is applied to a particular criminal.

<!-- b000196 | prose | pages [12] -->
We calculate model accuracy for a given serial criminal in the follow- ing way. Given a geographical proﬁling method with associated probability function P, we wish to determine the accuracy score of the method, de- noted Z.

<!-- b000197 | prose | pages [12] -->
Let Hk denote the hit score that considers x1, . . . , xk−1 as the currently known crime locations, and treats xk as the next crime location. Then,

<!-- b000198 | prose | pages [12] -->
1 Z = n −3

<!-- b000199 | prose | pages [12] -->
n X

<!-- b000200 | prose | pages [12] -->
Hk

<!-- b000201 | prose | pages [12] -->
k=4

<!-- b000202 | prose | pages [12] -->
is the mean of the hit scores determined by sequentially adding each crime location, starting with the fourth, to the set of currently known crimes. We start with the fourth crime because criminal behavior is not generally considered serial until the criminal has committed at least three crimes [1]. Note that a lower value for the accuracy score represents a more accurate model.

<!-- b000203 | furniture | pages [13] -->
Team number 7947

<!-- b000204 | furniture | pages [13] -->
Page 10 of 25

<!-- b000205 | prose | pages [13] -->
3.5 Search Area Determination

<!-- b000206 | prose | pages [13] -->
Our notions of performance and accuracy depend heavily on the size of the search area. The hit score can be made arbitrarily small by increasing the size of the search area.

<!-- b000207 | prose | pages [13] -->
This is because additional locations on the periphery of the search area are unlikely to be the next crime location, but these additional locations are included in the total search area.

<!-- b000208 | prose | pages [13] -->
Surprisingly, literature that uses the hit score performance metric does not explicitly address how the search area is to be determined given previous crime locations. We take the search area to be a square centered at the mean location of the previous crimes, with side length equal to double the maximum pairwise distance between previous crimes. In an ongoing serial criminal investigation the search area could be provided by law enforcement, but for our purposes the above search area balances the size of the search area based on previous crime distances.

<!-- b000209 | prose | pages [13] -->
4

<!-- b000210 | heading | pages [13] -->
Individual Models

<!-- b000211 | prose | pages [13] -->
4.1

<!-- b000212 | heading | pages [13] -->
Spatial Models

<!-- b000213 | prose | pages [13] -->
In this section we consider geographical proﬁling methods that only take into account the spatial data of serial crimes.

<!-- b000214 | prose | pages [13] -->
We consider the following spatial models for the calculation of P(Si,j):

<!-- b000215 | prose | pages [13] -->
• Random Method: The random method assigns each P(Si,j) a ran- dom value uniformly.

<!-- b000216 | prose | pages [13] -->
Theoretically, we expect the hit score of the random method to be 0.5 [14]. We include the random method as a basis for comparison of other geographical proﬁling methods.

<!-- b000217 | prose | pages [13] -->
• Standard Deviation Methods: Since standard deviation methods give no information about the distribution of probabilities inside the standard deviation areas, we cannot meaningfully compare them to other methods. Regardless, we include standard deviation methods in this paper because they are the most basic geographical proﬁling methods. These methods provide a rudimentary way by which the potential search area can be narrowed.

<!-- b000218 | prose | pages [13] -->
We consider the following standard deviation methods:

<!-- b000219 | furniture | pages [14] -->
Team number 7947

<!-- b000220 | furniture | pages [14] -->
Page 11 of 25

<!-- b000221 | prose | pages [14] -->
– Standard Deviation Rectangles: These are rectangular areas

<!-- b000222 | prose | pages [14] -->
deﬁned by the points

<!-- b000223 | prose | pages [14] -->
x +

<!-- b000224 | prose | pages [14] -->
x +

<!-- b000225 | prose | pages [14] -->
x +

<!-- b000226 | prose | pages [14] -->
x +

<!-- b000227 | prose | pages [14] -->
(−c σlon, −c σlat)

<!-- b000228 | prose | pages [14] -->
(−c σlon, c σlat)

<!-- b000229 | prose | pages [14] -->
(c σlon, c σlat)

<!-- b000230 | prose | pages [14] -->
(c σlon, −c σlat)

<!-- b000231 | prose | pages [14] -->
where x is the centroid of the crime locations, and σlon and σlat are the standard deviations of the longitudes and latitudes of the crime locations [15].

<!-- b000232 | prose | pages [14] -->
– Standard Deviation Ellipses: These are elliptical areas, ori-

<!-- b000233 | prose | pages [14] -->
ented along the trend line of the data in the least-squares sense. A standard deviation ellipse is an ellipse with its center at the centroid of the crime locations, rotated clockwise by an angle θ, and with axis lengths given by 2cσlon and 2cσlat, where θ, σlon, and σlat are calculated as in [16].

<!-- b000234 | prose | pages [14] -->
In both of the above methods, c is a constant that determines the range of the area. Common values are c = 1 for the 68th percentile area and c = 2 for the 95th percentile area. See Figure 7 for an illustration of these percentile areas.

<!-- b000235 | prose | pages [14] -->
• Centralization Methods: Centralization methods determine a cen- tral focal point for the spatial pattern of the serial criminal. In these models, the probability of the next crime decreases the further the location is from the focal point. Thus, in all these methods, given a central focal point C ∈A, we have

<!-- b000236 | prose | pages [14] -->
1 P(Si,j) = d(Si,j, C)

<!-- b000237 | prose | pages [14] -->
We consider the following ways of determining the central focal point:

<!-- b000238 | prose | pages [14] -->
– Centroid: The central focal point is the mean of the locations

<!-- b000239 | prose | pages [14] -->
of the crimes, given by

<!-- b000240 | prose | pages [14] -->
n

<!-- b000241 | prose | pages [14] -->
C = 1

<!-- b000242 | prose | pages [14] -->
X

<!-- b000243 | prose | pages [14] -->
xi

<!-- b000244 | prose | pages [14] -->
n

<!-- b000245 | prose | pages [14] -->
i=1

<!-- b000246 | furniture | pages [15] -->
Team number 7947

<!-- b000247 | furniture | pages [15] -->
Page 12 of 25

<!-- b000248 | prose | pages [15] -->
– Harmonic Mean: The central focal point is the harmonic mean

<!-- b000249 | prose | pages [15] -->
of the locations of the crimes, given by

<!-- b000250 | prose | pages [15] -->
n C =

<!-- b000251 | prose | pages [15] -->
1

<!-- b000252 | prose | pages [15] -->
Pn

<!-- b000253 | prose | pages [15] -->
i=1

<!-- b000254 | prose | pages [15] -->
xi

<!-- b000255 | prose | pages [15] -->
– Circle Center: The central focal point is the mean location of

<!-- b000256 | prose | pages [15] -->
the two crime locations farthest away from each other. This is de- termined as follows. Let xi, xj be such that d(xi, xj) is maximal.

<!-- b000257 | prose | pages [15] -->
Then we have C = xi + xj

<!-- b000258 | prose | pages [15] -->
2 . .

<!-- b000259 | prose | pages [15] -->
– Median: The central focal point is deﬁned as the point that

<!-- b000260 | prose | pages [15] -->
is the median of the of the longitudes and the median of the latitudes of the crime locations.

<!-- b000261 | prose | pages [15] -->
Compared to the other cen- tralization methods, the median is less sensitive to distant crime locations, which the criminal might have chosen for no particular spatial reason [9].

<!-- b000262 | prose | pages [15] -->
• Probability Distance Method: The probability distance method takes into account a location’s distance from each particular previous crime location. In this model, a probable next crime location would be relatively close to multiple previous crimes. Thus, we have

<!-- b000263 | prose | pages [15] -->
P(Si,j) =

<!-- b000264 | prose | pages [15] -->
n n X

<!-- b000265 | prose | pages [15] -->
f(d(Si,j, xk))

<!-- b000266 | prose | pages [15] -->
k=1

<!-- b000267 | prose | pages [15] -->
where f is a distance decay function deﬁned in one of the following ways:

<!-- b000268 | prose | pages [15] -->
– Linear Distance Decay: The probability of the next crime

<!-- b000269 | prose | pages [15] -->
location decreases linearly away from a particular previous crime location, given by f(d) = α−βd, where α, β are decay constants.

<!-- b000270 | prose | pages [15] -->
– Exponential Distance Decay: The probability of the next

<!-- b000271 | prose | pages [15] -->
crime location decreases exponentially away from a particular previous crime location, given by f(d) = e−γd, where γ is a decay constant.

<!-- b000272 | prose | pages [15] -->
For an illustrative example of the diﬀerence between centralization methods and the probability distance method see Figure 2.

<!-- b000273 | furniture | pages [16] -->
Team number 7947

<!-- b000274 | prose | pages [16] -->
2.0

<!-- b000275 | prose | pages [16] -->
low               Next Crime Probability               high

<!-- b000276 | prose | pages [16] -->
1.5

<!-- b000277 | prose | pages [16] -->
1.0

<!-- b000278 | prose | pages [16] -->
0.5

<!-- b000279 | prose | pages [16] -->
0.0

<!-- b000280 | prose | pages [16] -->
0.5

<!-- b000281 | prose | pages [16] -->
1.0

<!-- b000282 | prose | pages [16] -->
1.5

<!-- b000283 | prose | pages [16] -->
2.0 1.5 1.5 2.0 1.0 0.5 0.0 0.5 1.0 2.0

<!-- b000284 | prose | pages [16] -->
(a) Centroid centralization method on the unit circle

<!-- b000285 | furniture | pages [16] -->
Page 13 of 25

<!-- b000286 | prose | pages [16] -->
2.0

<!-- b000287 | prose | pages [16] -->
low               Next Crime Probability               high

<!-- b000288 | prose | pages [16] -->
1.5

<!-- b000289 | prose | pages [16] -->
1.0

<!-- b000290 | prose | pages [16] -->
0.5

<!-- b000291 | prose | pages [16] -->
0.0

<!-- b000292 | prose | pages [16] -->
0.5

<!-- b000293 | prose | pages [16] -->
1.0

<!-- b000294 | prose | pages [16] -->
1.5

<!-- b000295 | prose | pages [16] -->
2.0 1.5 1.5 2.0 1.0 0.5 0.0 0.5 1.0 2.0

<!-- b000296 | prose | pages [16] -->
(b) Exponential decay method on the unit circle

<!-- b000297 | caption | pages [16] -->
Figure 2: Comparison of prioritized search areas of a hypothetical criminal com-

<!-- b000298 | prose | pages [16] -->
mitting crimes along the unit circle given by a centralization method and a decay method.

<!-- b000299 | prose | pages [16] -->
4.2

<!-- b000300 | heading | pages [16] -->
Spatiotemporal Models

<!-- b000301 | prose | pages [16] -->
In this section we consider geographical proﬁling methods that take into account both the spatial and temporal data of serial crimes. The additional use of temporal data is motivated by the idea that recent crime locations are more relevant to the spatial behavior of a serial criminal than older crime locations. For example, if the serial criminal is traveling while committing crimes, then old crime location information quickly becomes outdated. For an example of this, see Figure 3.

<!-- b000302 | prose | pages [16] -->
Not all of the spatial models in Section 4.1 have extensions that incorpo- rate temporal data. For example, the circle center centralization method has no spatiotemporal analog, since the longest pairwise distance is unaﬀected by temporal data.

<!-- b000303 | prose | pages [16] -->
To incorporate the temporal components of the crime data, we calculate a temporal weighting factor for each crime,

<!-- b000304 | prose | pages [16] -->
wi = ti −t1

<!-- b000305 | prose | pages [16] -->
+ k

<!-- b000306 | prose | pages [16] -->
tn tn

<!-- b000307 | prose | pages [16] -->
where wi denotes the temporal weight of the ith crime. The oﬀset k is included so that the ﬁrst crime will not be given a weight of 0. We chose k = 0.1 so that the last crime is weighted approximately ten times more heavily than the ﬁrst crime. Let W denote the sum of the temporal weights.

<!-- b000308 | furniture | pages [17] -->
Team number 7947

<!-- b000309 | prose | pages [17] -->
low               Next Crime Probability               high

<!-- b000310 | prose | pages [17] -->
5

<!-- b000311 | prose | pages [17] -->
0

<!-- b000312 | prose | pages [17] -->
5

<!-- b000313 | prose | pages [17] -->
5 0 10

<!-- b000314 | prose | pages [17] -->
(a) Exponential Decay

<!-- b000315 | furniture | pages [17] -->
Page 14 of 25

<!-- b000316 | prose | pages [17] -->
low               Next Crime Probability               high

<!-- b000317 | prose | pages [17] -->
5

<!-- b000318 | prose | pages [17] -->
0

<!-- b000319 | prose | pages [17] -->
5

<!-- b000320 | prose | pages [17] -->
5 0 10

<!-- b000321 | prose | pages [17] -->
(b) Temporal Exponential Decay

<!-- b000322 | caption | pages [17] -->
Figure 3: Prioritized search area for a hypothetical serial criminal travelling east

<!-- b000323 | prose | pages [17] -->
over time, as given by the exponential decay and temporal exponential decay mod- els.

<!-- b000324 | prose | pages [17] -->
We modify the following spatial models to consider the temporal weight- ing factors:

<!-- b000325 | prose | pages [17] -->
• Centralization Methods:

<!-- b000326 | prose | pages [17] -->
– Temporal Centroid: The mean of the locations of the crimes,

<!-- b000327 | prose | pages [17] -->
weighted by time, given by

<!-- b000328 | prose | pages [17] -->
n

<!-- b000329 | prose | pages [17] -->
C = 1

<!-- b000330 | prose | pages [17] -->
X

<!-- b000331 | prose | pages [17] -->
xiwi

<!-- b000332 | prose | pages [17] -->
W

<!-- b000333 | prose | pages [17] -->
i=1

<!-- b000334 | prose | pages [17] -->
– Temporal Harmonic Mean: The harmonic mean of the loca-

<!-- b000335 | prose | pages [17] -->
tions of the crimes, weighted by time, given by

<!-- b000336 | prose | pages [17] -->
W C = Pn

<!-- b000337 | prose | pages [17] -->
wi

<!-- b000338 | prose | pages [17] -->
i=1

<!-- b000339 | prose | pages [17] -->
xi

<!-- b000340 | prose | pages [17] -->
• Temporal Probability Distance Methods: The linear distance decay and exponential distance decay methods incorporate the tem- poral weight data by using the following modiﬁed probability function:

<!-- b000341 | prose | pages [17] -->
X

<!-- b000342 | prose | pages [17] -->
P(Si,j) =

<!-- b000343 | prose | pages [17] -->
k=1

<!-- b000344 | prose | pages [17] -->
n n

<!-- b000345 | prose | pages [17] -->
wkf(d(Si,j, xk))

<!-- b000346 | furniture | pages [18] -->
Team number 7947

<!-- b000347 | furniture | pages [18] -->
Page 15 of 25

<!-- b000348 | prose | pages [18] -->
Uniform Random

<!-- b000349 | prose | pages [18] -->
Centroid

<!-- b000350 | prose | pages [18] -->
Temporal

<!-- b000351 | prose | pages [18] -->
Centroid

<!-- b000352 | prose | pages [18] -->
Harmonic

<!-- b000353 | prose | pages [18] -->
Temporal Harmonic

<!-- b000354 | prose | pages [18] -->
Circle Center

<!-- b000355 | prose | pages [18] -->
Median

<!-- b000356 | prose | pages [18] -->
Exponential

<!-- b000357 | prose | pages [18] -->
Decay

<!-- b000358 | prose | pages [18] -->
Temporal Exponential

<!-- b000359 | prose | pages [18] -->
Decay

<!-- b000360 | prose | pages [18] -->
Linear Decay

<!-- b000361 | prose | pages [18] -->
Temporal

<!-- b000362 | prose | pages [18] -->
Linear Decay

<!-- b000363 | prose | pages [18] -->
0.0 0.1 0.2 0.3 0.4 0.5 Hit Score

<!-- b000364 | caption | pages [18] -->
Figure 4: Comparison of the relative performance of each of our models on all of

<!-- b000365 | prose | pages [18] -->
our data sets.

<!-- b000366 | prose | pages [18] -->
4.3

<!-- b000367 | heading | pages [18] -->
Individual Model Results

<!-- b000368 | prose | pages [18] -->
To investigate the eﬀectiveness of each of the aforementioned models, we calculated the mean hit score across all of our data sets. After three crimes have been observed we apply our model and record the hit score for the next crime. This process is repeated for all subsequent crimes in the series.

<!-- b000369 | prose | pages [18] -->
The value of the constants in the linear and exponential decay models do not eﬀect the hit score. This is because the hit score is not aﬀected by the magnitude of the probability of the sector but by the relative probability to the rest of the search area. Consequently for an individual model the values of the constants have no eﬀect.

<!-- b000370 | prose | pages [18] -->
First we investigate the overall performance of each of the models. This can be found in Table 2 and in Figure 4. All of our models signiﬁcantly outperform the random model, but each of the individual models is not statistically superior to any other.

<!-- b000371 | furniture | pages [19] -->
Team number 7947

<!-- b000372 | furniture | pages [19] -->
Page 16 of 25

<!-- b000373 | prose | pages [19] -->
Next we investigate the performance of our models based upon the num- ber of crimes observed as seen in Figure 5. No patterns emerge that would indicate that the performance of the model improves having observed more crimes. The data sets considered do not have suﬃcient data to rule out such a correlation, particularly with the longer streaks as there are only a few data points.

<!-- b000374 | prose | pages [19] -->
0.35

<!-- b000375 | prose | pages [19] -->
0.30

<!-- b000376 | prose | pages [19] -->
0.25

<!-- b000377 | prose | pages [19] -->
0.20

<!-- b000378 | prose | pages [19] -->
Hit score

<!-- b000379 | prose | pages [19] -->
0.15

<!-- b000380 | prose | pages [19] -->
0.10

<!-- b000381 | prose | pages [19] -->
0.05

<!-- b000382 | prose | pages [19] -->
0.00

<!-- b000383 | prose | pages [19] -->
4 2 6 14 8 8 10 12 Number of crimes observed

<!-- b000384 | caption | pages [19] -->
Figure 5: Hit score by number of crimes observed using a exponential decay model

<!-- b000385 | prose | pages [19] -->
and 50% conﬁdence intervals.

<!-- b000386 | prose | pages [19] -->
5

<!-- b000387 | heading | pages [19] -->
Aggregation Models

<!-- b000388 | prose | pages [19] -->
In this section we consider ways of combining predictions from multiple geographical proﬁling methods into one model. The motivation behind these aggregate approaches is that each of the individual models described in Sections 4.1 and 4.2 have strengths and weaknesses, but by aggregating several models we hope enhance the strengths and reduce the weaknesses.

<!-- b000389 | prose | pages [19] -->
This issue of aggregation of models relates to the classic problem of

<!-- b000390 | furniture | pages [20] -->
Team number 7947

<!-- b000391 | prose | pages [20] -->
Model Random Centroid Centralization Temporal Centroid Centralization Harmonic Mean Centralization

<!-- b000392 | furniture | pages [20] -->
Page 17 of 25

<!-- b000393 | prose | pages [20] -->
Hit Score 95% Conﬁdence 0.500 0.001 0.104 0.031 0.106 0.031 0.105 0.031 0.106 0.031 Temporal Harmonic Mean Centralization Circle Center Centralization Median Centralization Exponential Decay Temporal Exponential Decay Linear Decay Temporal Linear Decay 0.116 0.029 0.123 0.042 0.094 0.030 0.092 0.029 0.125 0.043 0.123 0.043

<!-- b000394 | caption | pages [20] -->
Table 2: Models with associated hit scores and 95% conﬁdence intervals.

<!-- b000395 | prose | pages [20] -->
aggregating expert predictions. Consequently, there exist several diﬀerent techniques for aggregating these models. These techniques can be catego- rized as either axiomatic or Bayesian.

<!-- b000396 | prose | pages [20] -->
Clemen and Winkler reported no signiﬁcant diﬀerence in the performance of more complex Bayesian models with more simple axiomatic approaches [17], and as such we have chosen to focus on the more elementary axiomatic approaches.

<!-- b000397 | heading | pages [20] -->
Axiomatic Approaches: Given n models that we wish to aggregate,

<!-- b000398 | prose | pages [20] -->
let Pk(Si,j) denote the probability that a particular sector contains the next crime as predicted by the kth model. Let Wk denote the aggregation weight of the kth model, given such that all Wk’s sum to one.

<!-- b000399 | prose | pages [20] -->
• Linear Opinion Pool: This model is a linear combination of two or more probability distribution functions produced by individual models.

<!-- b000400 | prose | pages [20] -->
P(Si,j) =

<!-- b000401 | prose | pages [20] -->
n X

<!-- b000402 | prose | pages [20] -->
WkPk(Si,j)

<!-- b000403 | prose | pages [20] -->
k=1

<!-- b000404 | prose | pages [20] -->
Examples of this model and the eﬀect of diﬀerent weights can be found in Figure 6.

<!-- b000405 | heading | pages [20] -->
• Logarithmic Opinion Pool: This model is a weighted product of

<!-- b000406 | prose | pages [20] -->
two or more probability distribution functions.

<!-- b000407 | prose | pages [20] -->
P(Si,j) =

<!-- b000408 | prose | pages [20] -->
n Y

<!-- b000409 | prose | pages [20] -->
Pk(Si,j)Wk

<!-- b000410 | prose | pages [20] -->
k=1

<!-- b000411 | furniture | pages [21] -->
Team number 7947

<!-- b000412 | prose | pages [21] -->
39.5

<!-- b000413 | prose | pages [21] -->
low               Next Crime Probability               high

<!-- b000414 | prose | pages [21] -->
39.0

<!-- b000415 | prose | pages [21] -->
38.5

<!-- b000416 | prose | pages [21] -->
38.0

<!-- b000417 | prose | pages [21] -->
37.5

<!-- b000418 | prose | pages [21] -->
48 km

<!-- b000419 | prose | pages [21] -->
77.5 78.0 77.0 76.5 76.0

<!-- b000420 | prose | pages [21] -->
(a) Exponential decay weight 0.00, Circle center weight 1.00

<!-- b000421 | prose | pages [21] -->
39.5

<!-- b000422 | prose | pages [21] -->
low               Next Crime Probability               high

<!-- b000423 | prose | pages [21] -->
39.0

<!-- b000424 | prose | pages [21] -->
38.5

<!-- b000425 | prose | pages [21] -->
38.0

<!-- b000426 | prose | pages [21] -->
37.5

<!-- b000427 | prose | pages [21] -->
48 km

<!-- b000428 | prose | pages [21] -->
77.5 78.0 77.0 76.5 76.0

<!-- b000429 | prose | pages [21] -->
(c) Exponential decay weight 0.50, Circle center weight 0.50

<!-- b000430 | prose | pages [21] -->
39.5

<!-- b000431 | prose | pages [21] -->
39.0

<!-- b000432 | prose | pages [21] -->
38.5

<!-- b000433 | prose | pages [21] -->
38.0

<!-- b000434 | prose | pages [21] -->
37.5

<!-- b000435 | prose | pages [21] -->
48 km

<!-- b000436 | prose | pages [21] -->
77.5 78.0 77.0

<!-- b000437 | furniture | pages [21] -->
Page 18 of 25

<!-- b000438 | prose | pages [21] -->
39.5

<!-- b000439 | prose | pages [21] -->
low               Next Crime Probability               high

<!-- b000440 | prose | pages [21] -->
39.0

<!-- b000441 | prose | pages [21] -->
38.5

<!-- b000442 | prose | pages [21] -->
38.0

<!-- b000443 | prose | pages [21] -->
37.5

<!-- b000444 | prose | pages [21] -->
48 km

<!-- b000445 | prose | pages [21] -->
77.5 78.0 77.0 76.5 76.0

<!-- b000446 | prose | pages [21] -->
(b) Exponential decay weight 0.25, Circle center weight 0.75

<!-- b000447 | prose | pages [21] -->
39.5

<!-- b000448 | prose | pages [21] -->
low               Next Crime Probability               high

<!-- b000449 | prose | pages [21] -->
39.0

<!-- b000450 | prose | pages [21] -->
38.5

<!-- b000451 | prose | pages [21] -->
38.0

<!-- b000452 | prose | pages [21] -->
37.5

<!-- b000453 | prose | pages [21] -->
48 km

<!-- b000454 | prose | pages [21] -->
77.5 78.0 77.0 76.5 76.0

<!-- b000455 | prose | pages [21] -->
(d) Exponential decay weight 0.75, Circle center weight 0.25

<!-- b000456 | prose | pages [21] -->
low               Next Crime Probability               high

<!-- b000457 | prose | pages [21] -->
76.5 76.0

<!-- b000458 | prose | pages [21] -->
(e) Exponential decay weight 1.00, Circle center weight 0.00

<!-- b000459 | caption | pages [21] -->
Figure 6: Prioritized search areas resulting from using diﬀerent weights in the

<!-- b000460 | prose | pages [21] -->
aggregation model of a circle center and exponential decay for the Beltway Sniper.

<!-- b000461 | furniture | pages [22] -->
Team number 7947

<!-- b000462 | furniture | pages [22] -->
Page 19 of 25

<!-- b000463 | prose | pages [22] -->
In the exponential decay and the linear decay spatial models described in Section 4.1, we noted the value of the constants chosen for the model has no impact on the hit score metric. In an aggregate model this is not the case, as the relative magnitude of probability is important when added or multiplied by another model.

<!-- b000464 | prose | pages [22] -->
To set these parameters we used the mean pairwise distance. We deﬁne the mean pairwise distance to be the mean distance between any two crimes

<!-- b000465 | prose | pages [22] -->
2 δ = n(n −1)

<!-- b000466 | prose | pages [22] -->
X

<!-- b000467 | prose | pages [22] -->
d(xi, xj) 1≤i<j≤n

<!-- b000468 | prose | pages [22] -->
In the case of the linear decay model, α was chosen to be 1 and β was chosen

<!-- b000469 | prose | pages [22] -->
q

<!-- b000470 | prose | pages [22] -->
2

<!-- b000471 | prose | pages [22] -->
such that α −βδ = 0. In the case of the exponential decay, we set γ =

<!-- b000472 | prose | pages [22] -->
δ,

<!-- b000473 | prose | pages [22] -->
which gives a mean distance to crime of δ

<!-- b000474 | prose | pages [22] -->
2. We believed these values would provide a reasonable magnitude of probability when compared with other models.

<!-- b000475 | heading | pages [22] -->
Aggregation Model Results

<!-- b000476 | prose | pages [22] -->
5.1

<!-- b000477 | prose | pages [22] -->
To investigate the beneﬁts of aggregation models, we used a 2k factorial experimental design [18]. For each of our models described in Section 4, we investigated two possible scenarios: the model was included in the aggregate and weighted equally with the others, and the model was not included. We then computed the mean hit score for the resultant aggregate model for all possible models on all of our data sets.

<!-- b000478 | prose | pages [22] -->
While a further optimization process could be conducted in which more weights or diﬀerent decay constants were investigated, this process allowed us to see the eﬀect of diﬀerent models on the aggregate as well as see which individual models produce a strong aggregate model.

<!-- b000479 | prose | pages [22] -->
Through this process we found the strongest combination of individual models used the temporal exponential decay and the circle center centraliza- tion each equally weighted. The mean hit score for the linear opinion pool was 0.081 ± 0.027 with a 95% conﬁdence interval. The logarithmic opinion pool did not perform any better than any individual model. Neither model is statistically better than any of our other models.

<!-- b000480 | furniture | pages [23] -->
Team number 7947

<!-- b000481 | furniture | pages [23] -->
Page 20 of 25

<!-- b000482 | prose | pages [23] -->
Peter Sutcliﬀe: A Case Study 6

<!-- b000483 | prose | pages [23] -->
Peter Sutcliﬀe was a serial murderer who targeted women in England during the late 1970’s [19]. A map of his murders can be found in Figure 8(a). We have applied the models we have developed to predict where the next murder in the series would be if Sutcliﬀe had not been arrested and imprisoned.

<!-- b000484 | prose | pages [23] -->
54.2

<!-- b000485 | prose | pages [23] -->
54.0

<!-- b000486 | prose | pages [23] -->
53.8

<!-- b000487 | prose | pages [23] -->
53.6

<!-- b000488 | prose | pages [23] -->
53.4

<!-- b000489 | prose | pages [23] -->
53.2

<!-- b000490 | prose | pages [23] -->
53.0

<!-- b000491 | prose | pages [23] -->
20 km

<!-- b000492 | prose | pages [23] -->
1.4 2.6 2.4 2.2 2.0 1.8 1.6 1.2

<!-- b000493 | prose | pages [23] -->
54.2

<!-- b000494 | prose | pages [23] -->
54.0

<!-- b000495 | prose | pages [23] -->
53.8

<!-- b000496 | prose | pages [23] -->
53.6

<!-- b000497 | prose | pages [23] -->
53.4

<!-- b000498 | prose | pages [23] -->
53.2

<!-- b000499 | prose | pages [23] -->
53.0

<!-- b000500 | prose | pages [23] -->
20 km

<!-- b000501 | prose | pages [23] -->
1.4 2.6 2.4 2.2 2.0 1.8 1.6 1.2

<!-- b000502 | caption | pages [23] -->
Figure 7: Standard deviation rectangles and ellipses for the murders committed

<!-- b000503 | prose | pages [23] -->
by Peter Sutcliﬀe.

<!-- b000504 | prose | pages [23] -->
A common but na¨ıve method of identifying an area of high probability of serial crime generates a rectangle or ellipse in which a standard deviation of previous crimes have taken place. These rudimentary models can bee seen in Figure 7.

<!-- b000505 | prose | pages [23] -->
In Section 4.3, we found the individual model with the lowest mean hit score across our data set was the temporal exponential decay model. See

<!-- b000506 | caption | pages [23] -->
Figure 8 for an application of this model to the data for murders committed

<!-- b000507 | prose | pages [23] -->
by Peter Sutcliﬀe. The known crimes had a hit score of 10.6% using this model, so we use this percentage to ﬁnd a prioritized search area where we can be reasonably conﬁdent Sutcliﬀe would attack next. Of the 27818 km2, we can then isolate 2941 km2 in which to concentrate the search eﬀort.

<!-- b000508 | prose | pages [23] -->
7

<!-- b000509 | heading | pages [23] -->
Conclusions

<!-- b000510 | prose | pages [23] -->
• Every geographical proﬁling method outperformed the ran- dom method: On our data set, every geographical proﬁling method provided a signiﬁcant improvement in hit score over the random method.

<!-- b000511 | prose | pages [23] -->
• All non-random geographical proﬁling methods considered exhibited roughly the same performance: Diﬀerences in the hit

<!-- b000512 | furniture | pages [24] -->
Team number 7947

<!-- b000513 | furniture | pages [24] -->
Page 21 of 25

<!-- b000514 | prose | pages [24] -->
(a) Locations of Peter Sutcliﬀe murders.

<!-- b000515 | prose | pages [24] -->
Map generated via Google Static Maps API [20].

<!-- b000516 | prose | pages [24] -->
54.2

<!-- b000517 | prose | pages [24] -->
54.0

<!-- b000518 | prose | pages [24] -->
53.8

<!-- b000519 | prose | pages [24] -->
53.6

<!-- b000520 | prose | pages [24] -->
53.4

<!-- b000521 | prose | pages [24] -->
53.2

<!-- b000522 | prose | pages [24] -->
53.0

<!-- b000523 | prose | pages [24] -->
20 km

<!-- b000524 | prose | pages [24] -->
2.6 2.4 2.2 2.0

<!-- b000525 | prose | pages [24] -->
low               Next Crime Probability               high

<!-- b000526 | prose | pages [24] -->
1.4 1.8 1.8 1.6 1.2

<!-- b000527 | prose | pages [24] -->
(b) Temporal exponential decay model applied to Peter Sutcliﬀe murders.

<!-- b000528 | caption | pages [24] -->
Figure 8: Comparison of the prioritized search area produced by the temporal

<!-- b000529 | prose | pages [24] -->
exponential decay model to the map of the geographical area of murders committed by Peter Sutcliﬀe. This prioritized search area suggests that the Bradford area is at the highest risk of attack.

<!-- b000530 | furniture | pages [25] -->
Team number 7947

<!-- b000531 | furniture | pages [25] -->
Page 22 of 25

<!-- b000532 | prose | pages [25] -->
score for diﬀerent spatial, spatiotemporal, and aggregation methods were statistically insigniﬁcant, indicating that all the geographical pro- ﬁling methods have the same level of performance. This is a similar conclusion reached by Snook et al., who show that complex geograph- ical proﬁling methods are no more accurate than simple geographical proﬁling methods [4].

<!-- b000533 | prose | pages [25] -->
• Particular geographical proﬁling methods are not applicable to all serial criminals: We can see in Table 1 that the accuracy of our best individual geographical proﬁling method varied largely de- pending on the particular serial criminal being studied. For example, our best individual method, the temporal exponential decay method, is an accurate predictor of the D.C. sniper attacks (with an accuracy of 0.056), but is grossly inaccurate when applied to the serial rapist in Columbus, OH (with an accuracy of 0.533, which is worse than the random method).

<!-- b000534 | prose | pages [25] -->
8

<!-- b000535 | heading | pages [25] -->
Future Work

<!-- b000536 | prose | pages [25] -->
• Standardization of data set: It is currently diﬃcult to compare geographical proﬁling method performance to previous research be- cause each study uses a diﬀerent set of serial crime data to determine performance results. An eﬀort to compile a large, comprehensive list of serial crime data to which all methods would be compared would greatly help the development of geographical proﬁling techniques.

<!-- b000537 | prose | pages [25] -->
• Use of other relevant geographical information: In this pa- per we only consider the spatiotemporal relationships between crimes. Work by O’Leary and Brown et al. develop the notion of a feature space that groups crime locations by their relevant geographical fea- tures, such as population density or proximity to a major highway [12, 11]. The probability that a future crime happens at a particular location is then determined by the proximity of the location to previ- ous crimes in the feature space. Having more information about what connects crime locations could potentially improve our geographical proﬁling methods.

<!-- b000538 | prose | pages [25] -->
• Use of relevant information about the criminal: Research sug- gests that characteristics of the criminal, such as gender, race, and age,

<!-- b000539 | furniture | pages [26] -->
Team number 7947

<!-- b000540 | furniture | pages [26] -->
Page 23 of 25

<!-- b000541 | prose | pages [26] -->
play a role in determining their probable spatial behavior [9, 5, 10]. By taking these factors into account, we may be able to improve the accuracy of our models for a speciﬁc criminal.

<!-- b000542 | prose | pages [26] -->
• Evaluation of cost to law enforcement: Law enforcement agen- cies typically purchase computer-generated geographical proﬁling in- formation [4, 7]. Research by Snook et al. suggests that a person with minimal training in geographical proﬁling techniques can determine the probable residence of a serial criminal with just as much accuracy as a complex computer-generated geographical proﬁling method [8]. Further research should be done to determine if the cost of proprietary geographical proﬁling software is worth the quality of the information provided to law enforcement agencies.

<!-- b000543 | furniture | pages [27] -->
Team number 7947

<!-- b000544 | heading | pages [27] -->
References

<!-- b000545 | furniture | pages [27] -->
Page 24 of 25

<!-- b000546 | references | pages [27] -->
[1] Ronald M. Holmes and Stephen T. Holmes.

<!-- b000547 | references | pages [27] -->
Serial Murder.

<!-- b000548 | references | pages [27] -->
SAGE

<!-- b000549 | references | pages [27] -->
Publications, Thousand Oaks, California, 1998.

<!-- b000550 | references | pages [27] -->
[2] Donald Brown and Justin Stile. Geographic proﬁling with event predic-

<!-- b000551 | references | pages [27] -->
tion. Systems, Man and Cybernetics, 2003. IEEE International Con-

<!-- b000552 | references | pages [27] -->
ference on, 4:3712–3719, 2003.

<!-- b000553 | references | pages [27] -->
[3] Scotia J. Hicks and Bruce D. Sales. Criminal Proﬁling: Developing an

<!-- b000554 | references | pages [27] -->
Eﬀective Science and Practice.

<!-- b000555 | references | pages [27] -->
Washington, DC, 2006.

<!-- b000556 | references | pages [27] -->
American Psychological Association,

<!-- b000557 | references | pages [27] -->
[4] Brent Snook, Michele Zito, Craig Bennell, and Paul J. Taylor. On the

<!-- b000558 | references | pages [27] -->
complexity and accuracy of geographic proﬁling strategies. Journal of

<!-- b000559 | references | pages [27] -->
Quantitative Criminology, 21(1):1–26, 2005.

<!-- b000560 | references | pages [27] -->
[5] Brent Snook, Richard M. Cullen, Andreas Mokros, and Stephan Har-

<!-- b000561 | references | pages [27] -->
bort. Serial murderers’ spatial descisions: Factors that inﬂuence crime

<!-- b000562 | references | pages [27] -->
location choice. Journal of Investigative Psychology and Oﬀender Pro-

<!-- b000563 | references | pages [27] -->
ﬁling, 2(3):147–164, 2005.

<!-- b000564 | references | pages [27] -->
[6] D. Kim Rossmo. Place, space, and police investigations: Hunting se-

<!-- b000565 | references | pages [27] -->
rial violent criminals. In Crime and Place: Crime Prevention Studies.

<!-- b000566 | references | pages [27] -->
Willow Tree Press, NY, 1995.

<!-- b000567 | references | pages [27] -->
[7] D. Kim Rossmo. Geographic proﬁling: Target patterns of serial mur-

<!-- b000568 | references | pages [27] -->
derers. Unpublished doctoral dissertation, 1995.

<!-- b000569 | references | pages [27] -->
[8] Brent Snook, Paul J. Taylor, and Craig Bennell.

<!-- b000570 | references | pages [27] -->
Shortcuts to geo-

<!-- b000571 | references | pages [27] -->
graphic proﬁlling success: A reply to Rossmo (2005). Applied Cognitive

<!-- b000572 | references | pages [27] -->
Psychology, 19(5):655–661, 2005.

<!-- b000573 | references | pages [27] -->
[9] Jasper J. van der Kemp and Peter J. van Koppen. Fine-Tuning Ge-

<!-- b000574 | references | pages [27] -->
ographical Proﬁling, chapter 17.

<!-- b000575 | references | pages [27] -->
2007.

<!-- b000576 | references | pages [27] -->
Criminal Proﬁling. Humana Press,

<!-- b000577 | references | pages [27] -->
[10] Eric Beauregard, Jean Proulx, and D. Kim Rossmo. Spatial patterns of

<!-- b000578 | references | pages [27] -->
sex oﬀenders: Theoretical, empirical, and practical issues. Aggression

<!-- b000579 | references | pages [27] -->
and Violent Behavior, 10(5):579–603, 2005.

<!-- b000580 | references | pages [27] -->
[11] Donald Brown and Hua Liu.

<!-- b000581 | references | pages [27] -->
Spatial-temporal event prediction: A

<!-- b000582 | references | pages [27] -->
new model. Systems, Man, and Cybernetics, 1998. IEEE International

<!-- b000583 | references | pages [27] -->
Conference on, 3:2933–2937, 1998.

<!-- b000584 | furniture | pages [28] -->
Team number 7947

<!-- b000585 | furniture | pages [28] -->
Page 25 of 25

<!-- b000586 | references | pages [28] -->
[12] Mike O’Leary. The mathematics of geographic proﬁling. Journal of

<!-- b000587 | references | pages [28] -->
Investigative Psychology and Oﬀender Proﬁling, 6(3):253–265, 2009.

<!-- b000588 | references | pages [28] -->
[13] Spotcrime.com.

<!-- b000589 | references | pages [28] -->
http://www.spotcrime.com. Accessed on February

<!-- b000590 | references | pages [28] -->
19, 2010.

<!-- b000591 | references | pages [28] -->
[14] D. Kim Rossmo. Geographic heuristics or shortcuts to failure?: Re-

<!-- b000592 | references | pages [28] -->
sponse to Snook et al. Applied Cognitive Psychology, 19(5):651–654,

<!-- b000593 | references | pages [28] -->
2005.

<!-- b000594 | references | pages [28] -->
[15] Steven Gottlieb, Sheldon Arenberg, and Raj Singh. Crime Analysis:

<!-- b000595 | references | pages [28] -->
From First Report to Final Arrest. Alpha, 1994.

<!-- b000596 | references | pages [28] -->
[16] Joshua Kent and Michael Leitner.

<!-- b000597 | references | pages [28] -->
Eﬃcacy of standard deviational

<!-- b000598 | references | pages [28] -->
ellipses in the application of criminal geographic proﬁling. 4(3):147–

<!-- b000599 | references | pages [28] -->
165, 2007.

<!-- b000600 | references | pages [28] -->
[17] Robert T. Clemen and Robert L. Winkler.

<!-- b000601 | references | pages [28] -->
Aggregating probability

<!-- b000602 | references | pages [28] -->
distributions. In Advances in Decision Analysis. Cambridge University

<!-- b000603 | references | pages [28] -->
Press, Cambridge, UK, 2007.

<!-- b000604 | references | pages [28] -->
[18] Averill M. Law. Simulation Modeling and Analysis. McGraw-Hill, 3rd

<!-- b000605 | references | pages [28] -->
edition, 2000.

<!-- b000606 | references | pages [28] -->
[19] Nicole Ward Jouve. ’The Streetcleaner’ The Yorkshire Ripper Case on

<!-- b000607 | references | pages [28] -->
Trial. Marion Boyars Publishers, London, 1986.

<!-- b000608 | references | pages [28] -->
[20] Google Static Maps API.

<!-- b000609 | references | pages [28] -->
http://code.google.com/apis/maps/

<!-- b000610 | references | pages [28] -->
documentation/staticmaps/. Accessed on February 22, 2010.
