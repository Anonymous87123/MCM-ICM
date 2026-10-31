# P-B-2010-7273-e234c9a6

Status: machine-draft; not source-verified.


<!-- b000001 | title | pages [1] -->
Tracking Serial Criminals with a Road Metric

<!-- b000002 | title | pages [1] -->
Control #7273

<!-- b000003 | title | pages [1] -->
February 22, 2010

<!-- b000004 | heading | pages [1] -->
Abstract

<!-- b000005 | prose | pages [1] -->
In this paper, we present a computerized model to predict future crime locations and probable residences for a serial criminal based on the loca- tions and times of a sequence of past crimes. We ﬁrst create a “road metric” in order to measure distances by automobile travel time. In order to predict future crime locations, we apply the nonparametric statistical technique of kernel density estimation with our road metric, which allows us to estimate a time dependent probability distribution function. In or- der to predict the residences of serial criminals, we use a reﬁnement of a model developed by Rossmo, again adapting it to the road metric. This method develops a probability distribution for where a criminal might live by balancing the convenience of previous attack locations with the observation that greater distances from home aﬀord more opportunities for crime and a lesser chance of being caught. We apply our model to several high proﬁle serial murder cases, namely the case of Peter Sutcliﬀe, the “Yorkshire Ripper” and that of Wayne Williams, the “Atlanta Child Murderer.” In both cases, our model was successful in predicting the region of the criminal, and might prove useful in a criminal investigation.

<!-- b000006 | prose | pages [1] -->
1

<!-- b000007 | furniture | pages [2] -->
Page 2 of 19

<!-- b000008 | contents | pages [2] -->
Control #7273

<!-- b000009 | heading | pages [2] -->
Contents

<!-- b000010 | contents | pages [2] -->
1 Introduction

<!-- b000011 | contents | pages [2] -->
3

<!-- b000012 | contents | pages [2] -->
1.1

<!-- b000013 | contents | pages [2] -->
Outline of Our Approach

<!-- b000014 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . .

<!-- b000015 | contents | pages [2] -->
3

<!-- b000016 | contents | pages [2] -->
1.2

<!-- b000017 | contents | pages [2] -->
Assumptions

<!-- b000018 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000019 | contents | pages [2] -->
3

<!-- b000020 | contents | pages [2] -->
2 Mapping Crime and the Road Metric

<!-- b000021 | contents | pages [2] -->
4

<!-- b000022 | contents | pages [2] -->
2.1

<!-- b000023 | contents | pages [2] -->
Road Metric . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000024 | contents | pages [2] -->
4

<!-- b000025 | contents | pages [2] -->
3 Estimating and Extrapolating a Probability Density Function

<!-- b000026 | contents | pages [2] -->
5

<!-- b000027 | contents | pages [2] -->
3.1

<!-- b000028 | contents | pages [2] -->
Kernel Density Estimation . . . . . . . . . . . . . . . . . . . . . .

<!-- b000029 | contents | pages [2] -->
5

<!-- b000030 | contents | pages [2] -->
3.2

<!-- b000031 | contents | pages [2] -->
Extrapolating Future Probability Density Functions

<!-- b000032 | contents | pages [2] -->
. . . . . . .

<!-- b000033 | contents | pages [2] -->
6

<!-- b000034 | contents | pages [2] -->
4 Best Fit Circle and Rossmo’s Model

<!-- b000035 | contents | pages [2] -->
7

<!-- b000036 | contents | pages [2] -->
4.1

<!-- b000037 | contents | pages [2] -->
Centrography . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000038 | contents | pages [2] -->
7

<!-- b000039 | contents | pages [2] -->
4.2

<!-- b000040 | contents | pages [2] -->
Best Fit Circle

<!-- b000041 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000042 | contents | pages [2] -->
7

<!-- b000043 | contents | pages [2] -->
4.2.1

<!-- b000044 | contents | pages [2] -->
A First Attempt . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000045 | contents | pages [2] -->
7

<!-- b000046 | contents | pages [2] -->
4.2.2

<!-- b000047 | contents | pages [2] -->
A More Reﬁned Best Fit Circle . . . . . . . . . . . . . . .

<!-- b000048 | contents | pages [2] -->
8

<!-- b000049 | contents | pages [2] -->
4.3

<!-- b000050 | contents | pages [2] -->
Application to Rossmo’s Model . . . . . . . . . . . . . . . . . . .

<!-- b000051 | contents | pages [2] -->
8

<!-- b000052 | contents | pages [2] -->
5 Case Studies

<!-- b000053 | contents | pages [2] -->
10

<!-- b000054 | contents | pages [2] -->
5.1

<!-- b000055 | contents | pages [2] -->
Yorkshire Ripper . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000056 | contents | pages [2] -->
10

<!-- b000057 | contents | pages [2] -->
5.1.1

<!-- b000058 | contents | pages [2] -->
Map and Metric

<!-- b000059 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . .

<!-- b000060 | contents | pages [2] -->
10

<!-- b000061 | contents | pages [2] -->
5.1.2

<!-- b000062 | contents | pages [2] -->
Probability Density Estimate . . . . . . . . . . . . . . . .

<!-- b000063 | contents | pages [2] -->
11

<!-- b000064 | contents | pages [2] -->
5.1.3

<!-- b000065 | contents | pages [2] -->
Rossmo’s Model

<!-- b000066 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . .

<!-- b000067 | contents | pages [2] -->
11

<!-- b000068 | contents | pages [2] -->
5.1.4

<!-- b000069 | contents | pages [2] -->
Assessment of Results . . . . . . . . . . . . . . . . . . . .

<!-- b000070 | contents | pages [2] -->
11

<!-- b000071 | contents | pages [2] -->
5.2

<!-- b000072 | contents | pages [2] -->
Atlanta Child Murders . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000073 | contents | pages [2] -->
13

<!-- b000074 | contents | pages [2] -->
5.2.1

<!-- b000075 | contents | pages [2] -->
Metric and Map

<!-- b000076 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . .

<!-- b000077 | contents | pages [2] -->
13

<!-- b000078 | contents | pages [2] -->
5.2.2

<!-- b000079 | contents | pages [2] -->
Probability Density Estimate . . . . . . . . . . . . . . . .

<!-- b000080 | contents | pages [2] -->
13

<!-- b000081 | contents | pages [2] -->
5.2.3

<!-- b000082 | contents | pages [2] -->
Application to Rossmo’s Method . . . . . . . . . . . . . .

<!-- b000083 | contents | pages [2] -->
13

<!-- b000084 | contents | pages [2] -->
5.2.4

<!-- b000085 | contents | pages [2] -->
Assessment of Results . . . . . . . . . . . . . . . . . . . .

<!-- b000086 | contents | pages [2] -->
14

<!-- b000087 | contents | pages [2] -->
6 Improving the Model

<!-- b000088 | contents | pages [2] -->
16

<!-- b000089 | contents | pages [2] -->
6.1

<!-- b000090 | contents | pages [2] -->
Expanding the Road Metric . . . . . . . . . . . . . . . . . . . . .

<!-- b000091 | contents | pages [2] -->
16

<!-- b000092 | contents | pages [2] -->
6.2

<!-- b000093 | contents | pages [2] -->
Proﬁling Potential Victims . . . . . . . . . . . . . . . . . . . . . .

<!-- b000094 | contents | pages [2] -->
16

<!-- b000095 | contents | pages [2] -->
6.3

<!-- b000096 | contents | pages [2] -->
Improving Computational Eﬃciency . . . . . . . . . . . . . . . .

<!-- b000097 | contents | pages [2] -->
17

<!-- b000098 | contents | pages [2] -->
6.4

<!-- b000099 | contents | pages [2] -->
Testing to Choose Optimal Parameters . . . . . . . . . . . . . . .

<!-- b000100 | contents | pages [2] -->
17

<!-- b000101 | contents | pages [2] -->
7 Conclusion

<!-- b000102 | contents | pages [2] -->
17

<!-- b000103 | contents | pages [2] -->
8 Executive Summary

<!-- b000104 | contents | pages [2] -->
17

<!-- b000105 | contents | pages [2] -->
References

<!-- b000106 | contents | pages [2] -->
19

<!-- b000107 | contents | pages [2] -->
2

<!-- b000108 | furniture | pages [3] -->
Page 3 of 19

<!-- b000109 | contents | pages [3] -->
Control #7273

<!-- b000110 | heading | pages [3] -->
1 Introduction

<!-- b000111 | prose | pages [3] -->
In this paper we present a computerized model for studying serial crime patterns. Our model takes highway systems into account as a signiﬁcant determiner of how criminals behave. Speciﬁcally, we created a road metric to give a measure of the time it takes for a driver to travel between two points on a map. We incorporate this road metric into several diﬀerent models to give an estimate of where future crimes may occur and where the perpetrator may live. Our models give law enforcement agencies an estimate as to where they could patrol with the highest likelihood of apprehending the criminal, as well as where they should conduct their investigation into the residence of the criminal.

<!-- b000112 | heading | pages [3] -->
1.1 Outline of Our Approach

<!-- b000113 | prose | pages [3] -->
The beginning of our paper will be devoted to presenting the theoretical frame- work and an outline of our computer implementation. The later sections of our paper will be devoted to applying our model to famous notable criminal cases and assessing the accuracy of the model. For each criminal investigation we will do roughly the following:

<!-- b000114 | prose | pages [3] -->
• Develop the “road metric” to measure distances based on how long it takes to drive between them. This metric will be based primarily on the local highway system.

<!-- b000115 | prose | pages [3] -->
• Estimate and extrapolate probability density functions for where criminals are likely to commit future crimes.

<!-- b000116 | prose | pages [3] -->
• Estimate oﬀender’s residence using a best ﬁt circle under the road metric and by applying a modiﬁcation of current models.

<!-- b000117 | heading | pages [3] -->
1.2 Assumptions

<!-- b000118 | prose | pages [3] -->
Due to the huge variation in criminal activity, as well as the highly unusually and unpredictable psychological pathologies that high proﬁle serial killers often have, using a relatively simple computer model to predict serial crime in general faces several hurdles. Below are the assumptions we take about the crimes that our model is applied to:

<!-- b000119 | prose | pages [3] -->
• Crimes are committed by individuals. We assume the series of crimes has been attribute with a high degree of certainty to a single individual.

<!-- b000120 | prose | pages [3] -->
We did not design our model to analyze organized crime, gang, or mob activity.

<!-- b000121 | prose | pages [3] -->
• Criminals travel mostly by automobile. Our model makes signiﬁcant use of analyzing highway patterns to judge distances based on how long it takes to travel them by automobile.

<!-- b000122 | prose | pages [3, 4] -->
3 Control #7273

<!-- b000123 | furniture | pages [4] -->
Page 4 of 19

<!-- b000125 | prose | pages [4] -->
• Crimes are committed near to at where they are discovered by police In terms of murder cases, this means that body dump sites are murder sites. This is not an unreasonable assumption, as disorganized serial killers often leave their victims near the murder site [9]. Note that in serial crimes such as serial rape, burglary, or arson, there is no distinction between the site of the crime and the site found by police.

<!-- b000126 | prose | pages [4] -->
• Crimes are occurring within a small region, i.e. roughly within a city or county. This eliminates the case that crimes are occurring across multiples states or countries. In those cases, our model should be applied to each cluster of crimes.

<!-- b000127 | heading | pages [4] -->
2 Mapping Crime and the Road Metric

<!-- b000128 | prose | pages [4] -->
We used the mathematical software Sage to create a map of the area surrounding serial criminal incidents. The main features we included in the maps are the major highways, as well as the locations of criminal activities. We treat the highway system as a graph, considering each highway entrance and exit as a vertex in the graph, and each road section in between a pair of entrances and exits as an edge of the graph. Each edge is given a weight corresponding to to the Euclidean length between its corresponding vertices.

<!-- b000129 | heading | pages [4] -->
2.1 Road Metric

<!-- b000130 | prose | pages [4] -->
For each map M, we computed a road metric d : M × M →R+. The road metric measures distances within a region based on the approximate total travel time by car. The metric makes the assumption that drivers will usually take the shortest path between two points, utilizing highways as much as possible instead of traveling entirely via side-streets. The metric makes the assumptions that

<!-- b000131 | prose | pages [4] -->
• Time spent on side streets is proportional to the Manhattan metric since side streets are often organized into a grid shape,

<!-- b000132 | prose | pages [4] -->
• Time spent on the freeway is proportional to the Euclidean dis- tance.

<!-- b000133 | prose | pages [4] -->
Given points a and b on the map, we compute the road metric as follows:

<!-- b000134 | heading | pages [4] -->
1. For each vertex v in our highway system (which correspond to entrances

<!-- b000135 | prose | pages [4] -->
or exits on the freeway), we compute the Manhattan distances M(v, a) and M(v, b).

<!-- b000136 | heading | pages [4] -->
2. For each pair of vertices v1, v2, we apply Dijkstra’s algorithm to ﬁnd the

<!-- b000137 | prose | pages [4] -->
shortest path (taking into consideration the lengths of the edge segments) on the graph of our highway system from v1 to v2. We call this distance E(v1, v2).

<!-- b000138 | prose | pages [4, 5] -->
4 Control #7273

<!-- b000139 | furniture | pages [5] -->
Page 5 of 19

<!-- b000141 | prose | pages [5] -->
3. Then our road metric is deﬁned as

<!-- b000142 | prose | pages [5] -->
  v1,v2{M(a, v1) + E(v1, v2) + M(v2, b)}, M(a, b) d(a, b) = min min ,

<!-- b000143 | prose | pages [5] -->
or in other words, the minimum of the fastest way to take the highway, and taking a route which avoids the highway.

<!-- b000144 | prose | pages [5] -->
In terms of actually computing the road metric, we divided the maps into m × n grids and computed and then stored the distance from each grid space to each other grid space.

<!-- b000145 | heading | pages [5] -->
3 Estimating and Extrapolating a Probability

<!-- b000146 | prose | pages [5] -->
Density Function

<!-- b000147 | heading | pages [5] -->
3.1 Kernel Density Estimation

<!-- b000148 | prose | pages [5] -->
Given the locations and positions of criminal incident, we created a ﬁrst estimate for the probability density distribution for future crimes as follows. In the case of a Euclidean distances, given a set of sample points {x1, . . . , xn} generated by a random variable, one often estimates the probability density function as

<!-- b000149 | prose | pages [5] -->
N φ(x) = 1 X KA(x −xi) N i=1

<!-- b000150 | prose | pages [5] -->
where 1 2π|A|1/2 e−((x−xi)tA−1(x−xi)) KA(x −xi) =

<!-- b000151 | prose | pages [5] -->
where A is a covariance matrix, which amounts to adding small normal distri- butions around each point to generate an estimated probability density function [7], [10],[2]. We observe that since covariance matrices are positive deﬁnite, the quadratic form xtAx induces a norm on Rn deﬁned by √ xtAx, ∥x∥=

<!-- b000152 | prose | pages [5] -->
which in turn induces a metric. This naturally presents an application of our road metric by replacing the Gaussian function K (shown above) with the mod- iﬁed Gaussian function, G, deﬁned by

<!-- b000153 | prose | pages [5] -->
−d(x, xi)2   1 G(x, xi, t) = Mi(t)Exp , (h(t −ti))2

<!-- b000154 | prose | pages [5] -->
where d is the road metric deﬁned above, and h is essentially an indirect control the covariance of this kernel and Mi is the normalizing constant deﬁned by

<!-- b000155 | prose | pages [5] -->
−d(x, xi)2   Z Mi(t) = Exp dx. (h(t −ti))2

<!-- b000156 | prose | pages [5, 6] -->
5 Control #7273

<!-- b000157 | furniture | pages [6] -->
Page 6 of 19

<!-- b000159 | prose | pages [6] -->
We treat h as a function of time since it is reasonable to assume that more recent crimes are more useful in predicting future crimes than earlier crimes and hence it is reasonable to let the modiﬁed Gaussian functions “diﬀuse” over time by letting h be an increasing function. We empirically determined that setting h(t) = 2.5 arctan(2t + .2), where t is measured in weeks, was a good ﬁt. Our estimate for the probability density function thus becomes

<!-- b000160 | prose | pages [6] -->
N φ(x, t) = 1 X G(x, xi, t). (1) N i=1

<!-- b000161 | prose | pages [6] -->
In terms of actually computing φ(x, t), as we did with the road metric, we computing φ for each grid space in our partitioned m × n grid using the precomputed values of our road metric.

<!-- b000162 | heading | pages [6] -->
3.2 Extrapolating Future Probability Density Functions

<!-- b000163 | prose | pages [6] -->
Our above discussion gives a reasonable idea of where crimes have been commit- ted, but it is not necessarily reasonable to expect that a criminal will distribute his or her crimes based on a single probability distribution function for all time. Therefore we decided to perform a weighted least squares approximation based on trends in the probability distribution functions discussed above. The idea is to make a linear approximation to the probability density functions and predict a future probability density function outside of our data set. Our method is as follows. Suppose x1, . . . , xn represent the location of crimes which occurred respectively at t1 < t2 < · · · < tn, and that we want a probability density function at some time t∗> tn.

<!-- b000164 | prose | pages [6] -->
• In our equation for φ(x, t) (Equation 1), we sum over only the crimes which have occurred before time t.

<!-- b000165 | prose | pages [6] -->
• So that our linear approximation is not biased by the initial spikes from the kernels functions resulting from individual murders initially being point masses, we wish to let our density functions “diﬀuse” as much as possible.

<!-- b000166 | prose | pages [6] -->
Using the probability density estimation in Equation 1, we compute the probability density functions

<!-- b000167 | prose | pages [6] -->
φ(x, t2 −ϵ), φ(x, t3 −ϵ), . . . , φ(x, tn −ϵ)

<!-- b000168 | prose | pages [6] -->
for some small ϵ as well as φ(x, tM) for some tM between tn and t∗.

<!-- b000169 | prose | pages [6] -->
• We now do a weighted least squares approximation to estimate φ(x, t∗).

<!-- b000170 | prose | pages [6] -->
To do this, we consider φ(x, t) pointwise over our m × n map grid and perform a weighted least squares. We modify the well known normal

<!-- b000171 | prose | pages [6, 7] -->
6 Control #7273

<!-- b000172 | furniture | pages [7] -->
Page 7 of 19

<!-- b000174 | prose | pages [7] -->
equations for a standard least squares problem XtX ˆβ = Xty as described in [1] to get the modiﬁed normal equations

<!-- b000175 | prose | pages [7] -->
XtWX ˆβ = XtWy

<!-- b000176 | prose | pages [7] -->
where W is a weight matrix. We chose to weight the the probability density functions φ(x, tn) linearly in time (so that later crimes are weighted much more than earlier crimes).

<!-- b000177 | heading | pages [7] -->
4 Best Fit Circle and Rossmo’s Model

<!-- b000178 | heading | pages [7] -->
4.1 Centrography

<!-- b000179 | prose | pages [7] -->
One common method for estimating the residence of a serial criminal is to treat the location of each crime as a point mass and ﬁnd the centroid of the point masses by means of a spacial average. According to [9], centrography is one of the most common search methods for criminal investigations and has been used to examine serial rape cases in San Diego, as well as the case of the Yorkshire Ripper. According to [4], there is a signiﬁcant amount of evidence showing that serial rapists often live close to the centroid of their oﬀense locations.

<!-- b000180 | heading | pages [7] -->
4.2 Best Fit Circle

<!-- b000181 | prose | pages [7] -->
A reasonable extension of the idea of using a centroid to estimate the location of a criminals residence is to attempt to ﬁt a circle to the location of criminal activities. This is based on the assumption that criminals will typically try to avoid committing crimes very near to where they live, but at the same time will expend roughly the same amount of eﬀort in each of their crimes. Since we would expect the energy put into a crime by a criminal would be comparable to the total amount of time they spend traveling, we thought to apply the road metric we discussed earlier.

<!-- b000182 | heading | pages [7] -->
4.2.1 A First Attempt

<!-- b000183 | prose | pages [7] -->
The most naive thing we could do is ﬁt a circle to the data by minimizing the square of the distance from our crime locations to a circle, i.e. minimize

<!-- b000184 | prose | pages [7] -->
(d(Cr(x), y))2 = X X |d(x, y) −r|2, i i

<!-- b000185 | prose | pages [7] -->
where the sum is taken over all of crime locations xi. Unfortunately this method is very unstable. Consider the example in Figure 1 of the best ﬁt circle for three points. Moving the middle point slightly produces a tremendous change in the best ﬁt circle’s radius and center.

<!-- b000186 | prose | pages [7, 8] -->
7 Control #7273

<!-- b000187 | furniture | pages [8] -->
Page 8 of 19

<!-- b000189 | caption | pages [8] -->
Figure 1: The unstable behavior of a naive best ﬁt circle.

<!-- b000190 | heading | pages [8] -->
4.2.2 A More Reﬁned Best Fit Circle

<!-- b000191 | prose | pages [8] -->
A better generalization would be to notice that in Euclidean coordinates, given a set of points x1, . . . xn, then the point x such that

<!-- b000192 | prose | pages [8] -->
n X ∥x −xn∥2 i=1

<!-- b000193 | prose | pages [8] -->
is minimized is the centroid of the region.

<!-- b000194 | prose | pages [8] -->
This provides a natural generalization to the road metric which is perhaps a better extension of the often used method of centrography. Namely, we deﬁne the center of our best ﬁt circle to be the point x such that

<!-- b000195 | prose | pages [8] -->
n X (d(x, xi))2 i=1

<!-- b000196 | prose | pages [8] -->
is minimized. We will deﬁne the radius, r, to be the average distance from x to the crime locations, namely

<!-- b000197 | prose | pages [8] -->
n r = 1 X (d(x, xi)). n i=1

<!-- b000198 | prose | pages [8] -->
In Figure 2, we show an example of a circle in the road metric induced by a highway system. The particular highway system is from the Sutcliﬀe murder case which is discussed in further detail later in the paper.

<!-- b000199 | heading | pages [8] -->
4.3 Application to Rossmo’s Model

<!-- b000200 | prose | pages [8] -->
In [9], Rossmo presents the model for estimating the the residence of a criminal based on the location of their oﬀenses. The model makes use of the idea of a buﬀer zone. The buﬀer zone is an area surrounding a criminals residence in which a criminal avoids committing crimes. The idea behind the buﬀer zone is that criminals will attempt to balance the energy they need to expend in order to go long distances away from their residence to commit crimes, and the increased risk of committing crimes near to where they live. There is a signiﬁcant amount of research supporting Rossmo’s model, as well as the idea

<!-- b000201 | prose | pages [8, 9] -->
8 Control #7273

<!-- b000202 | furniture | pages [9] -->
Page 9 of 19

<!-- b000204 | caption | pages [9] -->
Figure 2: A circle in the road metric induced by the graph for the Manchester

<!-- b000205 | prose | pages [9] -->
Leeds area of England. The highway system graph is black and the circle is grey.

<!-- b000206 | prose | pages [9] -->
of a buﬀer zone, both in terms of criminal patterns as well as animal hunting patterns [5],[8].

<!-- b000207 | prose | pages [9] -->
Rossmo’s model is based on subdividing a map of the general location of the crimes into a grid and then computing the estimated probability of a perpetrator residing in a particular grid space as

<!-- b000208 | prose | pages [9] -->
N (1 −φ)Bg−f   φ X pjk = K ∥xjk −xi∥f + (2B −∥xjk −xi∥)g i=1 where

<!-- b000209 | prose | pages [9] -->
( if ∥xjk −xi∥< B 1 φ = if ∥xjk −xi∥≥B, 0

<!-- b000210 | prose | pages [9] -->
and f, g are constants, B is the radius of the buﬀer zone, and K is some con- stant used to normalize the entire probability distribution. Empirically, Rossmo found that for criminal cases the optimal values for f and g were f = g = 1.2. In our model we adapted the formulation of Rossmo’s model to use the road metric. Thus the formulation of Rossmo’s model that we used in our simulations becomes N  (1 −φ)  φ X pjk = K |d(xjk, xi)|1.2 + . |2B −d(xjk, xi)|1.2 i=1 In order to estimate the radius of the buﬀer zone, we used our best ﬁt circle in order to approximate the radius of a best ﬁt circle under our metric, and then used half of this distance as the estimated radius of the buﬀer zone.

<!-- b000211 | prose | pages [9, 10] -->
9 Control #7273

<!-- b000212 | furniture | pages [10] -->
Page 10 of 19

<!-- b000214 | heading | pages [10] -->
5 Case Studies

<!-- b000215 | prose | pages [10] -->
In this section we apply the models discussed earlier to two notable cases, namely the Yorkshire Ripper (Peter Sutcliﬀe) and the Atlanta Child Murderer (Wayne Williams).

<!-- b000216 | heading | pages [10] -->
5.1 Yorkshire Ripper

<!-- b000217 | prose | pages [10] -->
The Yorkshire Ripper murders were a series of murders which occurred between 1975 and 1981 in which 13 women were murdered and 7 attacked in the Manch- ester and Leeds area of England. Most of the women killed were prostitutes. Peter Sutcliﬀe was convicted of the murders and attacks. According to [3], the bodies did not appear to have been moved after the murders. We treated attacks and murders identically in our analysis.

<!-- b000218 | heading | pages [10] -->
5.1.1 Map and Metric

<!-- b000219 | prose | pages [10] -->
Using a map of the Manchester and Leeds area, we represented the highways as a graph, making sure to concentrate the exits and entrances (the nodes of the graph) around population centers. Figure 3 shows a color plot of the distance under the road metric from what was later determined to be Sutcliﬀe’s residence.

<!-- b000220 | caption | pages [10] -->
Figure 3: This shows the distance from Sutcliﬀe’s house under the road metric

<!-- b000221 | prose | pages [10] -->
with an overlay of our graph representation of the nearby highway system. Sutcliﬀe’s house is at the house symbol. Red corresponds to a very short distance and dark blue corresponds to a long distance.

<!-- b000222 | prose | pages [10, 11] -->
10 Control #7273

<!-- b000223 | furniture | pages [11] -->
Page 11 of 19

<!-- b000225 | heading | pages [11] -->
5.1.2 Probability Density Estimate

<!-- b000226 | prose | pages [11] -->
There were a total of 20 criminal incidents committed by Sutcliﬀe. We ran our density distribution model on the ﬁrst 19 cases in order to predict the location of the 20th. We used the locations of the ﬁrst 19 attacks and the time of the 20th in order to predict the location of the 20th. If one were to use our model in real life, the time of the next crime would not actually be known, but this is not of great importance since our choice of the variance function in our kernel causes the model to stabilize very quickly. The results are shown in Figure 4.

<!-- b000227 | caption | pages [11] -->
Figure 4: This shows the estimated probability distribution for the 20th attack

<!-- b000228 | prose | pages [11] -->
knowing the ﬁrst 19. The dots represent the attacks and the ‘x’ denotes the actual location of the 20th attack. Red indicates the highest probability and purple the lowest.

<!-- b000229 | heading | pages [11] -->
5.1.3 Rossmo’s Model

<!-- b000230 | prose | pages [11] -->
As discussed earlier, Rossmo’s model is designed to predict the location of the oﬀender’s residence. We modiﬁed Rossmo’s model to make use of our road metric. As was discussed earlier, we ﬁrst computed a best ﬁt circle for the crimes using a generalized centroid, which is shown in Figure 5. We then used half of this value in the equation for Rossmo’s model to estimate the location of the residence of the murderer. A colorized plot is shown in Figure 6 and a plot of the estimated function as a surface is shown in Figure 7.

<!-- b000231 | heading | pages [11] -->
5.1.4 Assessment of Results

<!-- b000232 | prose | pages [11] -->
Our kernel method produced a strong hotspot around where the 20th murder actually took place. From our extrapolated probability distribution, the 20th attack was 8.58 times more likely to occur in the cell containing the actual murder site than it was to occur in an average square. More importantly, the

<!-- b000233 | prose | pages [11, 12] -->
11 Control #7273

<!-- b000234 | furniture | pages [12] -->
Page 12 of 19

<!-- b000236 | caption | pages [12] -->
Figure 5: The best ﬁt circle of the attack locations under the road metric. The

<!-- b000237 | prose | pages [12] -->
circle is shown in black, the graph is shown in grey, and the kill locations are shown in red.

<!-- b000238 | caption | pages [12] -->
Figure 6: The probability density estimated by Rossmo’s model for the perpe-

<!-- b000239 | prose | pages [12] -->
trator’s residence. Red indicates the highest probability. The actual location of Sutcliﬀe’s house is shown with the house symbol.

<!-- b000240 | prose | pages [12] -->
result of our model would direct law enforcement oﬃcers to begin their search in precisely the square where the murder occurred.

<!-- b000241 | prose | pages [12] -->
Although Rossmo’s model did not generate a hotspot directly on Sutcliﬀe’s residence, it still provided a good starting point for a police investigation. Sut- cliﬀe’s house was on a second or third priority band and would be located reasonably quickly in a search eﬀort.

<!-- b000242 | prose | pages [12, 13] -->
12 Control #7273

<!-- b000243 | furniture | pages [13] -->
Page 13 of 19

<!-- b000245 | caption | pages [13] -->
Figure 7: Rossmo’s probability estimate as a surface.

<!-- b000246 | heading | pages [13] -->
5.2 Atlanta Child Murders

<!-- b000247 | prose | pages [13] -->
The Atlanta child murders refers to the murders of 29 boys and men between 1979 and 1981. Only 22 of these murders were conclusively linked to Wayne Williams, so we will use only these data points in our models. There is evidence that the bodies were found not far from where they were murdered [6]. Williams was tried and convicted of two of the murders in 1982.

<!-- b000248 | heading | pages [13] -->
5.2.1 Metric and Map

<!-- b000249 | prose | pages [13] -->
We used a map in [6] of the highway system surrounding the murder locations. As described earlier in the paper, we implement this as a graph and compute the road metric for this case. The distance from Williams’ house is shown in

<!-- b000250 | caption | pages [13] -->
Figure 8.

<!-- b000251 | heading | pages [13] -->
5.2.2 Probability Density Estimate

<!-- b000252 | prose | pages [13] -->
We ran our model using the kernel probability function on 21 of the data points in order to predict the location of the 22nd murder. The results are shown in ﬁgure 9.

<!-- b000253 | heading | pages [13] -->
5.2.3 Application to Rossmo’s Method

<!-- b000254 | prose | pages [13] -->
Following the description of our model above, we ﬁrst computed the best ﬁt circle for the kills in the Atlanta data set. This is shown in Figure 10.

<!-- b000255 | prose | pages [13, 14] -->
13 Control #7273

<!-- b000256 | furniture | pages [14] -->
Page 14 of 19

<!-- b000258 | caption | pages [14] -->
Figure 8: The distance from Wayne Williams’ residence under the road metric.

<!-- b000259 | caption | pages [14] -->
Figure 9: This shows our computed probability distribution for the 22nd attack

<!-- b000260 | prose | pages [14] -->
knowing the ﬁrst 21. The actual location of the 22nd attack is shown as an ‘x’.

<!-- b000261 | prose | pages [14] -->
We then applied a modiﬁcation of Rossmo’s method to estimate a probability distribution of where the criminal lives. A colorized illustration of the results are shown in Figure 11 and a representation of the results as a surface is shown in Figure 12.

<!-- b000262 | heading | pages [14] -->
5.2.4 Assessment of Results

<!-- b000263 | prose | pages [14] -->
Our application of the kernel method for this case was not as successful as it was for the Sutcliﬀe case. It happened that the 22nd murder was in an unexpected position relative to the prior kills. The model was still able to predict a very nontrivial probability for the 22nd murder being in this region, and the hotspot

<!-- b000264 | prose | pages [14, 15] -->
14 Control #7273

<!-- b000265 | furniture | pages [15] -->
Page 15 of 19

<!-- b000267 | caption | pages [15] -->
Figure 10: The best ﬁt circle for the Atlanta child murders data.

<!-- b000268 | caption | pages [15] -->
Figure 11: A colorized representation of the prediction made by Rossmo’s model

<!-- b000269 | prose | pages [15] -->
for the location of the criminal’s residence with the locations of the crimes overlaid. Wayne Williams’ residence is represented by the house symbol.

<!-- b000270 | prose | pages [15] -->
it generated is reasonably near this section. Surprisingly, the hotspot happens to be centered over Williams’ residence.

<!-- b000271 | prose | pages [15] -->
Rossmo’s model was also able to create a hotspot very near the murderer’s residence. Given the result of the model as guidance, law-enforcement could very easily locate Williams.

<!-- b000272 | prose | pages [15, 16] -->
15 Control #7273

<!-- b000273 | furniture | pages [16] -->
Page 16 of 19

<!-- b000275 | caption | pages [16] -->
Figure 12: Rossmo’s probability estimate as a surface.

<!-- b000276 | heading | pages [16] -->
6 Improving the Model

<!-- b000277 | heading | pages [16] -->
6.1 Expanding the Road Metric

<!-- b000278 | prose | pages [16] -->
One of the most novel aspects of our approach was the design of the road metric to accurately estimate the cost of travel to a criminal. We can improve this estimate by taking into account other geographical features on a map, such as lakes, rivers or terrains of varying elevation. The presence of irregularly-shaped bodies of water can potentially have a signiﬁcant impact on the results of our computations.

<!-- b000279 | heading | pages [16] -->
6.2 Proﬁling Potential Victims

<!-- b000280 | prose | pages [16] -->
As we observed in the case of the Atlanta Child Murderer, the kernel method was unable to predict a relatively unexpected kill site (in terms of pure ge- ography). We may be able to improve our model by skewing our probability distribution toward areas with high concentrations of potential victims. For in- stance, Peter Sutcliﬀe generally targeted prostitutes, so our model would beneﬁt from increasing the probability of a region being a potential kill site if it has a high level of prostitution.

<!-- b000281 | prose | pages [16, 17] -->
16 Control #7273

<!-- b000282 | furniture | pages [17] -->
Page 17 of 19

<!-- b000284 | heading | pages [17] -->
6.3 Improving Computational Eﬃciency

<!-- b000285 | prose | pages [17] -->
Our algorithm saves time by overlaying a grid on the map of the region and saving the distance between every pair of cells. As each distance computation requires an application of Dijkstra’s algorithm, the determination of all of these distances is quite slow. With a more eﬃcient algorithm (or implementation that is faster than what Sage has available) for measuring distances in the road metric, we can make our grids ﬁner and improve the precision of our model.

<!-- b000286 | heading | pages [17] -->
6.4 Testing to Choose Optimal Parameters

<!-- b000287 | prose | pages [17] -->
Since we had a limited amount of time to perform computationally hard tests, our empirically-determined choice for the variance function h in the kernel method may be far from optimal. Our model could improve substantially if we make a diﬀerent choice for h. Further, the values for f and g that we used in Rossmo’s model were determined to be optimal for the Manhattan metric; there may be better choices for these parameters depending on the road metric in use.

<!-- b000288 | heading | pages [17] -->
7 Conclusion

<!-- b000289 | prose | pages [17] -->
The problem of tracking a serial criminal given a limited amount of data has proven to be very nontrivial. The signiﬁcant diﬀerence between our approaches highlights the creativity needed to tackle this problem. Both of our methods proved to be accurate means of locating the hotspots they were designed to ﬁnd. The kernel method was particularly viable in the Sutcliﬀe case, most likely due to the tendency of attacks to cluster. However, it became less accurate as attacks spread out more uniformly. Rossmo’s method had strong predictive power in both of our test cases. It consistently gave hotspots that would allow law- enforcement to easily locate the criminal. Synthesizing our models by informing police of all the hotspots we locate is an eﬀective way of balancing accuracy with the size of search regions.

<!-- b000290 | heading | pages [17] -->
8 Executive Summary

<!-- b000291 | prose | pages [17] -->
In our paper we present a computerized model for predicting future crimes and

<!-- b000292 | prose | pages [17] -->
estimating the location of a criminal based on the location and times of past

<!-- b000293 | prose | pages [17] -->
crimes. The model is based on geographic proﬁling and makes heavy use of the

<!-- b000294 | prose | pages [17] -->
local highway systems near to the crimes. For our model to be useful, it must

<!-- b000295 | prose | pages [17] -->
be applied to cases where the location of crimes has been determined. For in-

<!-- b000296 | prose | pages [17] -->
stance, the predictive power of our model is greatly reduced if body dump sites

<!-- b000297 | prose | pages [17, 18] -->
17 Control #7273

<!-- b000298 | furniture | pages [18] -->
Page 18 of 19

<!-- b000300 | prose | pages [18] -->
are used instead of kill sites. Secondly, our model is most useful if applied to rel- atively small areas, such as over the area of a county or city. Our model greatly factors local highway systems into consideration, and thus should be applied primarily to cases where the perpetrator is suspected of using an automobile for transportation.

<!-- b000301 | prose | pages [18] -->
Our model makes two predictions. Firstly it gives an estimate of where future crimes will occur. The estimate is based on where past crimes have occurred, putting the most weight on the most recent ones, and also taking into account the local highway system. It does not give an accurate estimate for the absolute probability that an oﬀender will be within a particular region, but instead provides the locations of hotspots where law enforcement should begin its investigation. By following the paths of constant and slowly changing color, the oﬃcers can logically search progressively larger areas around these hotspots to gradually increase the scope of their investigation.

<!-- b000302 | prose | pages [18] -->
Secondly, our model makes an estimate based on Rossmo’s model. This ap- proach balances two factors aﬀecting the distance a criminal travels to commit a crime. The ﬁrst factor reﬂects the eﬀort expended by a criminal in traveling farther away from their residence, whereas the second reﬂects the risk involved in committing crimes near where a criminal lives. As with the previous com- ponent of the model, this method provides hotspots at which law enforcement should begin its investigation, and sequentially larger regions for it to expand its investigation.

<!-- b000303 | prose | pages [18] -->
Empirical tests of our model on high proﬁle criminal cases has shown that both of these methods give useful starting points for investigation. We recom- mend that your oﬃcers apply our techniques to complement the other methods at their disposal.

<!-- b000304 | prose | pages [18, 19] -->
18 Control #7273

<!-- b000305 | furniture | pages [19] -->
Page 19 of 19

<!-- b000307 | heading | pages [19] -->
References

<!-- b000308 | references | pages [19] -->
[1] Anthony Atkinson, Marco Riani, Robust Diagnostic Regression Analysis,

<!-- b000309 | references | pages [19] -->
Springer Press, 2000.

<!-- b000310 | references | pages [19] -->
[2] Adrian W. Bowman, Adelchi Azzalini. Applied Smoothing Techniques for

<!-- b000311 | references | pages [19] -->
Data Analysis, Clarendon Press, 1997.

<!-- b000312 | references | pages [19] -->
[3] Lawrence Byford. The Yorkshire Ripper Case: Review of the Police In-

<!-- b000313 | references | pages [19] -->
vestigation of the Case. Presented to the Secretary of State for the Home

<!-- b000314 | references | pages [19] -->
Department. December 1981.

<!-- b000315 | references | pages [19] -->
[4] David Canter, Laura Hammond, “Prioritizing Burglars: Comparing the

<!-- b000316 | references | pages [19] -->
Eﬀectiveness of Geographical Proﬁling Methods”. Police Practice and Re-

<!-- b000317 | references | pages [19] -->
search, Vol. 8, No. 4, September 2007, pp. 371-384.

<!-- b000318 | references | pages [19] -->
[5] Steven C. Le Comber, Barry Nicholls, D. Kim Rossmo, Paul A. Racey.

<!-- b000319 | references | pages [19] -->
“Geographic proﬁling and animal foraging.” Journal of Theoretical Biology

<!-- b000320 | references | pages [19] -->
279 (2009) 111-118.

<!-- b000321 | references | pages [19] -->
[6] Chet Dettlinger. The List. Philmay Enterprises, 1983.

<!-- b000322 | references | pages [19] -->
[7] David Hand, Heikki Mannila, Padhraic Smyth, Principles of Data Mining,

<!-- b000323 | references | pages [19] -->
MIT Press, 2001.

<!-- b000324 | references | pages [19] -->
[8] Martin, Rossmo, Hammerschlag. “Hunting patterns and geographic proﬁl-

<!-- b000325 | references | pages [19] -->
ing of white shark predation.” Journal of Zoology v20 (2006) 233-240.

<!-- b000326 | references | pages [19] -->
[9] Darcy Kim Rossmo, Geographic Proﬁling: Target Patterns of Serial Mur-

<!-- b000327 | references | pages [19] -->
derers. Doctoral Dissertation, Simon Fraser University, 1995.

<!-- b000328 | references | pages [19] -->
[10] Xibin

<!-- b000329 | references | pages [19] -->
Zhang,

<!-- b000330 | references | pages [19] -->
Maxwell

<!-- b000331 | references | pages [19] -->
L.

<!-- b000332 | references | pages [19] -->
King,

<!-- b000333 | references | pages [19] -->
Rob

<!-- b000334 | references | pages [19] -->
J.

<!-- b000335 | references | pages [19] -->
Hyndman,

<!-- b000336 | references | pages [19] -->
Band-

<!-- b000337 | references | pages [19] -->
width

<!-- b000338 | references | pages [19] -->
Selection

<!-- b000339 | references | pages [19] -->
for

<!-- b000340 | references | pages [19] -->
Multivariate

<!-- b000341 | references | pages [19] -->
Kernel

<!-- b000342 | references | pages [19] -->
Density

<!-- b000343 | references | pages [19] -->
Estimation

<!-- b000344 | references | pages [19] -->
Using

<!-- b000345 | references | pages [19] -->
MCMC.

<!-- b000346 | references | pages [19] -->
Monash

<!-- b000347 | references | pages [19] -->
University,

<!-- b000348 | references | pages [19] -->
Clayton,

<!-- b000349 | references | pages [19] -->
Victory.

<!-- b000350 | references | pages [19] -->
2004.

<!-- b000351 | references | pages [19] -->
http://editorialexpress.com/cgi-bin/conference/download.cgi?

<!-- b000352 | references | pages [19] -->
db_name=ESAM04&paper_id=120. Accessed 2/20/2010.

<!-- b000353 | references | pages [19] -->
19
