# P-B-2011-10496-de9286d6

Status: machine-draft; not source-verified.


<!-- b000001 | heading | pages [1] -->
Summary

<!-- b000002 | prose | pages [1] -->
Our task is to construct an efﬁcient network of radio repeaters that can accommodate 1,000 simultaneous users on a spectrum from 145 to 148 MHz in a circular, ﬂat area of radius 40 miles. In the United States, this fre- quency range is used by licensed amateur ”ham” radio operators. Because the United States government requires ham radio operators to undergo a certiﬁcation process, we assume that we can implement protocols that the users will follow when using the network. Our goal is to minimize the number of repeaters used by the network while also providing a reason- able amount of service to users.

<!-- b000003 | prose | pages [1] -->
We approach this problem by trying to construct a network that places more repeaters in regions with the highest population density. We utilize privacy lines in a systematic way to allow parallel communication and min- imize interference across our network. To form the basis of our network, we use a clustering algorithm to group points in areas of dense population and then place repeaters at the centroids of each region. If the resulting graph is disconnected, this preliminary network is connected using a minimum spanning tree algorithm.

<!-- b000004 | prose | pages [1] -->
In order to test our network we came up with sample population data using a clumped distribution model. The model produces data that had a similar distribution to actual density data taken from a ﬂat region in the Southeastern United States. We measure the coverage of our network by the percentage of users within range of our network’s repeaters. We calcu- late the transmission capacity of the network is through repeated simula- tions of users in the network attempting to send messages to other users in the network. Sensitivity analysis was performed on this to determine the accuracy of this metric to be within 1.5% error. Our model was able to sig- niﬁcantly increase the transmission capacities up to 98% transmission over the network in our model. This compares to a maximum of 32% for a naive approach of evenly distributing repeaters throughout the area.

<!-- b000005 | prose | pages [1] -->
We provide color-gradient plots for different population distributions and plots of our generated networks for these distributions in our paper. Our algorithm works very well for most clumped populations. However, it is limited in the extent to which we can cluster the data. In addition to this information, we provide a method for constructing subnetworks around nodes with high load, a strategy that can improve the ability of the network to accommodate larger numbers of users.

<!-- b000006 | prose | pages [2] -->
Clustering on a Network

<!-- b000007 | prose | pages [2] -->
MCM Contest Question B

<!-- b000008 | furniture | pages [2] -->
Team # 10496

<!-- b000009 | prose | pages [2] -->
February 14, 2011

<!-- b000010 | heading | pages [2] -->
Contents

<!-- b000011 | contents | pages [2] -->
1

<!-- b000012 | heading | pages [2] -->
Introduction

<!-- b000013 | prose | pages [2] -->
3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 Background 3 The Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2

<!-- b000014 | prose | pages [2] -->
2

<!-- b000015 | heading | pages [2] -->
Assumptions

<!-- b000016 | prose | pages [2] -->
3 Metric

<!-- b000017 | prose | pages [2] -->
4

<!-- b000018 | prose | pages [2] -->
4

<!-- b000019 | prose | pages [2] -->
7 Measuring Transmission Capacity 3.1 . . . . . . . . . . . . . . .

<!-- b000020 | prose | pages [2] -->
7 Generating Requests . . . . . . . . . . . . . . . . . . . . . . . 3.2 9 Measuring Overall Quality . . . . . . . . . . . . . . . . . . . . 3.3

<!-- b000021 | prose | pages [2] -->
4 Approach

<!-- b000022 | prose | pages [2] -->
9

<!-- b000023 | prose | pages [2] -->
10 Modeling Population Density . . . . . . . . . . . . . . . . . . 4.1 10 Linking Strategies . . . . . . . . . . . . . . . . . . . . . . . . . 4.2 10 Two Different Strategies . . . . . . . . . . . . . . . . . 4.2.1 10 Bi-directional and Extended Chains . . . . . . . . . . 4.2.2 12 Naive Approach . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3 13 Implementing Privacy Lines to Reduce Interference . . . . . 4.4 14 K-Means Clustering . . . . . . . . . . . . . . . . . . . . . . . . 4.5 16 Connecting Clusters . . . . . . . . . . . . . . . . . . . 4.5.1 4.5.2 Assigning Channels

<!-- b000024 | prose | pages [2] -->
5

<!-- b000025 | heading | pages [2] -->
Results

<!-- b000026 | prose | pages [2] -->
18 . . . . . . . . . . . . . . . . . . .

<!-- b000027 | prose | pages [2] -->
19

<!-- b000028 | prose | pages [2] -->
20 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 Procedure 20 Number of Repeaters . . . . . . . . . . . . . . . . . . . . . . . 5.2 21 Coverage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.3 21

<!-- b000029 | furniture | pages [2] -->
Page 1 of 33

<!-- b000030 | furniture | pages [3] -->
Team # 10496

<!-- b000031 | furniture | pages [3] -->
Page 2 of 33

<!-- b000032 | prose | pages [3] -->
Transmission Capacity . . . . . . . . . . . . . . . . . . . . . . 5.4

<!-- b000033 | prose | pages [3] -->
6

<!-- b000034 | heading | pages [3] -->
Discussion

<!-- b000035 | prose | pages [3] -->
22

<!-- b000036 | prose | pages [3] -->
23 . . . . . . . . . . . . . . . . . . . . . . 6.1 Effects of 10,000 Users 23 Effects of Mountainous Terrain . . . . . . . . . . . . . . . . . 6.2

<!-- b000037 | prose | pages [3] -->
7

<!-- b000038 | heading | pages [3] -->
Conclusion

<!-- b000039 | prose | pages [3] -->
8

<!-- b000040 | heading | pages [3] -->
Future Work

<!-- b000041 | prose | pages [3] -->
26

<!-- b000042 | prose | pages [3] -->
26

<!-- b000043 | prose | pages [3] -->
27 Limitations of our model . . . . . . . . . . . . . . . . . . . . . 8.1 27 Ways to improve the model . . . . . . . . . . . . . . . . . . . 8.2

<!-- b000044 | prose | pages [3] -->
A Appendix

<!-- b000045 | prose | pages [3] -->
29

<!-- b000046 | prose | pages [3] -->
30

<!-- b000047 | furniture | pages [4] -->
Team # 10496

<!-- b000048 | furniture | pages [4] -->
Page 3 of 33

<!-- b000049 | prose | pages [4] -->
1

<!-- b000050 | heading | pages [4] -->
Introduction

<!-- b000051 | prose | pages [4] -->
1.1

<!-- b000052 | heading | pages [4] -->
Background

<!-- b000053 | prose | pages [4] -->
The goal of this paper is to present an extendible, ﬂexible algorithm for the optimal placement of a repeater network intended to serve users along the 145-148MHz range. In the United States, this particular band of fre- quencies corresponds to those used by amateur ”ham” radio users [6]. Be- cause of how radio repeaters work, interference is a signiﬁcant, persistent problem. With more than 700,000 licensed amateur radio operators in the United States, there is a real need to further develop strategies to optimize the number of repeaters needed to service an area as well as methods for managing interference [3]. This need is especially acute in extremely ﬂat areas, where the repeaters’ limited maximum range requires chains of re- peaters to be used.

<!-- b000054 | prose | pages [4] -->
Technological Background

<!-- b000055 | prose | pages [4] -->
Radio waves in the 145-148MHz range are considered very high fre- quency (VHF). Very high frequency waves are often used for short-range radio communication. For one thing, they are generally not reﬂected much by the ionosphere, so communication via VHF waves is largely limited to slightly more than line-of-sight communication. The line-of-sight property is so important that in a ﬂat area, you can make a reasonable approximation of a transmitter’s broadcast radius simply based on its height. A rough ap- proximation of the line-of-sight horizon (in miles) for an antenna of height h (in feet) is:

<!-- b000056 | prose | pages [4] -->
√

<!-- b000057 | prose | pages [4] -->
1.5 · h

<!-- b000058 | prose | pages [4] -->
distance =

<!-- b000059 | prose | pages [4] -->
[4]

<!-- b000060 | prose | pages [4] -->
While the limited range of VHF transmissions provides one avenue for avoiding interference with other transmissions, it also limits the broadcast- ing range of an individual user. On ﬂat ground, the broadcast radius of an average handheld amateur radio is somewhere in the neighborhood of 3-5 miles [2]. For amateur radio enthusiasts who want to be able to communi- cate with other people like them, this is an extremely limited range.

<!-- b000061 | prose | pages [4] -->
To address this issue, amateur radio users can tap into any of hundreds of radio ”repeaters” distributed across the country. What a repeater does is clear from its name: it repeats the signals it receives, often with additional power or from a higher vantage point. The type of repeater available for our use is called a ”duplex” repeater. The repeater is tuned to pick up a par- ticular frequency (in the 145-148MHz range), and then outputs the same

<!-- b000062 | furniture | pages [5] -->
Team # 10496

<!-- b000063 | furniture | pages [5] -->
Page 4 of 33

<!-- b000064 | prose | pages [5] -->
signal at a frequency offset by 600KHz. Because repeaters have a much larger range than the average user due to their increased height, repeaters allow an amateur radio operator broadcast to a much wider audience.

<!-- b000065 | prose | pages [5] -->
The ability to broadcast across a much wider area is a positive one for amateur radio operators, but it does present certain challenges. Most importantly, offering users a greater broadcast range greatly ampliﬁes the likelihood of interference. One tool that has been used to address the prob- lem is the ”continuous tone-coded squelch system” (CTCSS) technology. The idea is clever and simple: each repeater is associated with a particular subaudible tone. A given repeater remains in a deactivated state until it hears a signal that is of the proper frequency and contains its subaudible tone. As long as the repeater hears the signal with the subaudible tone, it will remain active and will rebroadcast any signals it receives at its input frequency.

<!-- b000066 | prose | pages [5] -->
1.2 The Problem

<!-- b000067 | prose | pages [5] -->
We have been tasked with determining the minimum number of re- peaters needed to accommodate a particular number of users - initially, 1000 - spread across a ﬂat, circular area of radius 40 miles. In part because we are dealing with the relatively narrow range of 145-148 MHz, we have 54 distinct privacy lines at our disposal to help mitigate potential interfer- ence problems.

<!-- b000068 | prose | pages [5] -->
The problem statement mentions that this network must be able to ac- commodate a certain number of “simultaneous users”. This is a vague phrase that is open to a number of interpretations. One way to interpret it is to say that there are 1,000 people making demands on the radio net- work at any given time. For a network of repeaters used for amateur radio, this is completely unrealistic from an interference standpoint. As a conse- quence, for the purpose of this problem, we deﬁned ”1,000 simultaneous users” to mean “1,000 people who might make demands on the system”, where the average number of requests per user is a parameter of our model.

<!-- b000069 | prose | pages [5] -->
2

<!-- b000070 | heading | pages [5] -->
Assumptions

<!-- b000071 | prose | pages [5] -->
Over the course of our analysis, we make a number of assumptions both to simplify the problem and to more clearly deﬁne it. We believe that the

<!-- b000072 | furniture | pages [6] -->
Team # 10496

<!-- b000073 | furniture | pages [6] -->
Page 5 of 33

<!-- b000074 | prose | pages [6] -->
majority of these assumptions are reasonable and based on solid real-world justiﬁcation; we will note when we deviate from this practice.

<!-- b000075 | prose | pages [6] -->
First, over the course of this paper we are assume that both repeaters and individual users broadcast in a radially symmetric manner. That is, their broadcast range can be represented by a circle on a two-dimensional map. Given the fact that transmissions in the VHF range are largely depen- dent on having a line-of-sight connection, this makes sense for a ﬂat area - transmission range is going to be limited mostly by the curvature of the earth, something that is roughly constant in each direction. In addition, we will make the assumption that if the broadcast radii of two repeaters touch, then they are able to communicate with one another. This is a reasonable assumption as well — the broadcast radius measures how far a source can broadcast to a point on the ground. Provided that power is not an issue and the radio waves don’t fade too much with distance, the distance a 40- foot-high antenna will be able to broadcast to another 40-foot-high tower will be roughly twice its broadcast range [9].

<!-- b000076 | prose | pages [6] -->
Second, we assume that the radio waves are traveling instantaneously. Because radio waves travel at near the speed of light, this is not a huge dis- tortion, especially at scales of eighty miles or less [8]. While a wave that needs to travel through several repeaters to get to its destination will suffer a noticeable delay, it will not be more than a second or two. In practice, this requires users to build in a buffer between receiving and transmitting signals. For the purpose of analyzing interference between two 30-second or minute-long signals, this buffer is rather small. As a consequence, we will use a set interval and ignore any requisite buffer when running any network load simulations.

<!-- b000077 | prose | pages [6] -->
Third, any repeater we use can have a maximum range of about 9 miles. This corresponds to an antenna height of about 40 feet [9]. Across a ﬂat area that does not have any signiﬁcant rises upon which to place an an- tenna, this is a reasonable maximum antenna height. An ”average” user — presumably with in possession of a radio at least as powerful as a hand- held amateur radio — is assumed to have a radial broadcast distance of roughly 3 miles. For the purposes of this paper, we assumed that a hand- held radio could transmit a maximum of 5 miles to another handheld and assumed that a handheld radio could only transmit to a repeater if that re- peater could reach the handheld radio. To account for power constraints on these mobile devices that could cause degradation of waves over large distances [4], we rounded down to 3 miles when considering the maximum transmission distance from a handheld device.

<!-- b000078 | prose | pages [6] -->
Fourth, the very real threat of interference as well as amateur radio li-

<!-- b000079 | furniture | pages [7] -->
Team # 10496

<!-- b000080 | furniture | pages [7] -->
Page 6 of 33

<!-- b000081 | prose | pages [7] -->
censing requirements have led to very widely-adopted broadcasting codes of conduct [10]. Before broadcasting on a particular frequency or using a nearby repeater, users are required to listen on all privacy lines for several minutes to see if it is in use. If it is not, then the user will make his or her broadcast. Therefore, during analysis, we assumed that users are both ca- pable and polite. That is, they do not make requests when a local tower is in use.

<!-- b000082 | prose | pages [7] -->
Fifth, while this rules out the possibility of interference at a local level, it does not rule out the possibility of interference across a long chain of con- nected repeaters. Ideally, this type of interference would count as a ”failed attempt to communicate”. However, to simplify and accelerate the model- development process, we made a temporary assumption that, due to time constraints, ended up becoming permanent. Instead of counting the inter- fering signals as ”failed” requests, we simply make the network unable to process two conﬂicting requests at the same time. So while this type of in- terference counts against a network, it isn’t penalized as much as it should be.

<!-- b000083 | prose | pages [7] -->
Sixth, it makes sense to think about a minimum spacing such that two frequencies are clearly distinguishable from one another. In our case, we simply went with the information that was given to us. Presumably, there is a good reason that the repeaters we are given output a signal that is off- set 600KHz from the signal they receive. For the purposes of this paper, we assume that it is because 600KHz is a good minimum discrepancy.

<!-- b000084 | prose | pages [7] -->
Seventh, we assume that each user places a roughly equal strain on the network. While this would certainly not hold true in the real-world, over a large body of users things will average out and this will tend to be a rea- sonable approximation.

<!-- b000085 | prose | pages [7] -->
Eight, we assume that the location we are dealing with is in the United States. This assumption is what tells us that we are in fact dealing with constructing a repeater network for use by amateur radio operators.

<!-- b000086 | prose | pages [7] -->
Finally, we make the assumption that the distribution of calls being made is strongly biased toward local connections. However, we feel that it is also a very reasonable one. In the real world, extended chains of re- peaters have very difﬁcult issues managing interference — unless the sig- nal is passing solely through a user’s local repeater, there’s no way to tell when it will be possible to make a call to a distant location. As a conse- quence, linked chains of repeaters are most frequently used for public ser- vice announcements during emergencies or in areas where there is a very limited amount of demand CITE. Simply looking at the numbers, it is ex- tremely unlikely that it is possible to accommodate a large number of users

<!-- b000087 | furniture | pages [8] -->
Team # 10496

<!-- b000088 | furniture | pages [8] -->
Page 7 of 33

<!-- b000089 | prose | pages [8] -->
unless each makes a minimal demand on the network as a whole. In this light, a heavy bias toward calls that use a small number of repeaters is rea- sonable.

<!-- b000090 | prose | pages [8] -->
3 Metric

<!-- b000091 | prose | pages [8] -->
3.1 Measuring Transmission Capacity

<!-- b000092 | prose | pages [8] -->
In order to get some sense for whether or not a given solution was valid, we needed to develop some way to measure a given solution’s efﬁcacy. More importantly, for a given network we needed to be able to return a yes or no answer for whether or not that network “accommodates” its users. In order to develop a reasonable metric, we ﬁrst asked “what, fundamentally, does an amateur radio operator want a repeater network to do?” At a basic level, the answer is very simple: an amateur radio user is going to want to broadcast something. The user will be satisﬁed if he or she is able to do this in a reasonable, timely manner, with a minimum number of interference- related issues.

<!-- b000093 | prose | pages [8] -->
With this deﬁnition of accommodation in mind, there is a very straight- forward way to deﬁne our metric. One network is better at accommodating its users than another if it can successfully process more transmission at- tempts than another. Similarly, we can designate a network as satisfactory if it can handle a minimum number of transmission attempts over a given time period. Expressing this as a ratio, we have:

<!-- b000094 | prose | pages [8] -->
Q = # transmissions processed

<!-- b000095 | prose | pages [8] -->
# transmissions attempted

<!-- b000096 | prose | pages [8] -->
Note that requests made by or to a user that is not covered by the net- work are automatically counted as ”failed” attempts at communication. The pseudocode in Algorithm 1 describes how we calculated Q.

<!-- b000097 | furniture | pages [9] -->
Team # 10496

<!-- b000098 | furniture | pages [9] -->
Page 8 of 33

<!-- b000099 | heading | pages [9] -->
Algorithm 1 Measure Network Quality

<!-- b000100 | prose | pages [9] -->
Require: UserPositions, UserRepeaterAssignment, UserTransmissionNumber, SimulationLength, NetworkAdjacencyMatrix, UserRanges Ensure: Un f ul f illedTransmissions equals the number of desired user

<!-- b000101 | prose | pages [9] -->
transmissions that could not be completed during the simulation.

<!-- b000102 | prose | pages [9] -->
GenerateUserTransmissions() Run UserRepeaterAssignments, with inputs UserTransmissionNumber and SimulationLength to get Transmissions, which represents where each user will transmit to and when they will try to do so. Set TransmissionQueue be an empty array. Set Un f ul f illedTransmissions to zero. for all timesteps in SimulationLength do

<!-- b000103 | prose | pages [9] -->
for all Transmissions in Transmissions do

<!-- b000104 | prose | pages [9] -->
scheduled If this request is TransmissionQueue end for for this timestep, add it to

<!-- b000105 | prose | pages [9] -->
Set CurrentTransmissions to be an empty array. for all Transmissions in TransmissionQueue in order do

<!-- b000106 | prose | pages [9] -->
if this transmission is being made by or to a user who is not covered by the network then

<!-- b000107 | prose | pages [9] -->
Increment Un f ul f illedTransmissions Remove this transmissions from TransmissionQueue else if this transmission will not interfere with any

<!-- b000108 | prose | pages [9] -->
transmissions in CurrentTransmissions then Add this transmission to CurrentTransmissions and remove it from TransmissionQueue. end if end for end for Add the number of elements remaining in TransmissionQueue to Un f ul f illedTransmissions.

<!-- b000109 | prose | pages [9] -->
Though the metric itself is pretty straightforward, it is less clear what exactly a reasonable proportion of successful communications should be required in order to consider a repeater network successful. As a result, our model has a parameter for Q. This allows someone who has a better idea for how accommodating they need the network to be to set it at what- ever threshold they desire.

<!-- b000110 | furniture | pages [10] -->
Team # 10496

<!-- b000111 | prose | pages [10] -->
3.2 Generating Requests

<!-- b000112 | furniture | pages [10] -->
Page 9 of 33

<!-- b000113 | prose | pages [10] -->
In order to generate requests for using the network we need to assign a starting location and an ending location for this request. Typically people are more likely to make requests closer to their current location since they will have more interaction with people locally then over a long distance. To model this type of distribution of requests by a given person, we use a Poisson distribution to calculate the probability of a call going a distance l between two towers,

<!-- b000114 | prose | pages [10] -->
λk

<!-- b000115 | prose | pages [10] -->


<!-- b000116 | prose | pages [10] -->
n

<!-- b000117 | prose | pages [10] -->
l!

<!-- b000118 | prose | pages [10] -->
l

<!-- b000119 | prose | pages [10] -->
n−l

<!-- b000120 | prose | pages [10] -->
1 −λ

<!-- b000121 | prose | pages [10] -->
.

<!-- b000122 | prose | pages [10] -->
n

<!-- b000123 | prose | pages [10] -->
Here, n corresponds to the maximum number of towers that one can send a request. The number of towers was used for calculating this since people with closer towers will generally have shorter Euclidean distances given us the desired effect. In addition to this, amateur radio users might consider the amount of network they are using for a call which would also result in a decay as l increases. By choosing λ = 1 to provide the desired decay of the requests as l increases.

<!-- b000124 | prose | pages [10] -->
3.3 Measuring Overall Quality

<!-- b000125 | prose | pages [10] -->
There is more that goes into determining the overall quality of a network than whether or not it is able to handle a certain percentage of user requests. For example, there are a huge number of distinct networks (inﬁnite if we don’t specify a grid of coordinates) that will all satisfy the minimum accom- modation requirements. We need to have some method to distinguish be- tween two “passing” networks. Fortunately, the problem statement makes it very clear what the primary criterion should be, saying: “determine the minimum number of repeaters necessary to accommodate 1,000 simulta- neous users”. To address this, we examined the solutions generated by our algorithm for a particular number of maximum repeaters used. Using this approach, it is easy to ﬁnd a lower bound for the number of repeaters needed to adequately accommodate present users with a network gener- ated by our algorithm. Other factors that might be worth considering when comparing the overall quality of networks include factors such as coverage percentage and how they perform with different levels of demand.

<!-- b000126 | furniture | pages [11] -->
Team # 10496

<!-- b000127 | prose | pages [11] -->
4 Approach

<!-- b000128 | furniture | pages [11] -->
Page 10 of 33

<!-- b000129 | heading | pages [11] -->
Modeling Population Density

<!-- b000130 | prose | pages [11] -->
4.1

<!-- b000131 | prose | pages [11] -->
Our preliminary model for modeling the population distribution within our region was to simply randomly locate 1000 people inside of our region with a uniform distribution. However, humans are social animals, so as- signing each person a random location independently of each other is a poor model for what actual population distributions look like. It is more common to model a human population by using a clumped population dis- tribution. This involves people aggregating around certain areas which is common in the formation of communities. Population data on the density of people in different communities suggests that within different regions we will have different population size [5].

<!-- b000132 | prose | pages [11] -->
We modeled different types of population distributions that can occur by choosing a set number of clumps that occur within our region. We used a variety of different numbers of clumps to account for different distribu- tions that can occur depending on the given region. The mean of a each clump was selected by generating a random point inside the circle. For a given clump we modeled the distribution of the population around the center by using a multivariate Gaussian distribution. Since the x and y co- ordinate of the person’s location are independent of each other, we used the multivariate distribution:

<!-- b000133 | prose | pages [11] -->
1 f (x, y) = 2πσxσy

<!-- b000134 | prose | pages [11] -->


<!-- b000135 | prose | pages [11] -->


<!-- b000136 | prose | pages [11] -->
(y−µy)2

<!-- b000137 | prose | pages [11] -->
(x−µx)2

<!-- b000138 | prose | pages [11] -->
+ σ2x

<!-- b000139 | prose | pages [11] -->
σ2y

<!-- b000140 | prose | pages [11] -->
e e

<!-- b000141 | prose | pages [11] -->
.

<!-- b000142 | prose | pages [11] -->
We used values for σx = σy = 20, which seemed to provide a reasonable range of models for the data. This was determined by looking at actual data for population density in ﬂat areas of the United States and comparing our density distributions to the actual distribution [1].

<!-- b000143 | prose | pages [11] -->
4.2 Linking Strategies

<!-- b000144 | prose | pages [11] -->
4.2.1 Two Different Strategies

<!-- b000145 | prose | pages [11] -->
Before jumping into our overall approach, it makes sense to talk a little bit about the methods at our disposal for creating a chain of repeaters al- lowing for two-way communication. In order for a repeater to be com- municate to another, its transmission frequency must be the same as the

<!-- b000146 | furniture | pages [12] -->
Team # 10496

<!-- b000147 | prose | pages [12] -->
−30

<!-- b000148 | prose | pages [12] -->
−20

<!-- b000149 | prose | pages [12] -->
−10

<!-- b000150 | prose | pages [12] -->
0

<!-- b000151 | prose | pages [12] -->
10

<!-- b000152 | prose | pages [12] -->
20

<!-- b000153 | prose | pages [12] -->
30

<!-- b000154 | prose | pages [12] -->
−30 −20 −10 0 10 20 30

<!-- b000155 | prose | pages [12] -->
(a) Random Population Distribution

<!-- b000156 | prose | pages [12] -->
−30

<!-- b000157 | prose | pages [12] -->
−20

<!-- b000158 | prose | pages [12] -->
−10

<!-- b000159 | prose | pages [12] -->
0

<!-- b000160 | prose | pages [12] -->
10

<!-- b000161 | prose | pages [12] -->
20

<!-- b000162 | prose | pages [12] -->
30

<!-- b000163 | prose | pages [12] -->
−30 −20 −10 0 10 20 30

<!-- b000164 | prose | pages [12] -->
(c) Clumped Population Distribution with 10 Clumps

<!-- b000165 | prose | pages [12] -->
−30

<!-- b000166 | prose | pages [12] -->
−20

<!-- b000167 | prose | pages [12] -->
−10

<!-- b000168 | prose | pages [12] -->
0

<!-- b000169 | prose | pages [12] -->
10

<!-- b000170 | prose | pages [12] -->
20

<!-- b000171 | prose | pages [12] -->
30

<!-- b000172 | prose | pages [12] -->
−30 −20 −10 0 10 20 30

<!-- b000173 | prose | pages [12] -->
(e) Clumped Population Distribution with 40 Clumps

<!-- b000174 | furniture | pages [12] -->
Page 11 of 33

<!-- b000175 | prose | pages [12] -->
−30

<!-- b000176 | prose | pages [12] -->
−20

<!-- b000177 | prose | pages [12] -->
−10

<!-- b000178 | prose | pages [12] -->
0

<!-- b000179 | prose | pages [12] -->
10

<!-- b000180 | prose | pages [12] -->
20

<!-- b000181 | prose | pages [12] -->
30

<!-- b000182 | prose | pages [12] -->
−30 −20 −10 0 10 20

<!-- b000183 | prose | pages [12] -->
(b) Clumped Population Distribution with 5 Clumps

<!-- b000184 | prose | pages [12] -->
−30

<!-- b000185 | prose | pages [12] -->
−20

<!-- b000186 | prose | pages [12] -->
−10

<!-- b000187 | prose | pages [12] -->
0

<!-- b000188 | prose | pages [12] -->
10

<!-- b000189 | prose | pages [12] -->
20

<!-- b000190 | prose | pages [12] -->
30

<!-- b000191 | prose | pages [12] -->
−30 −20 −10 0 10 20 30

<!-- b000192 | prose | pages [12] -->
(d) Clumped Population Distribution with 20 Clumps

<!-- b000193 | prose | pages [12] -->
(f) Actual Population Distribution

<!-- b000194 | caption | pages [12] -->
Figure 1: Pictures of the different population distributions we generated

<!-- b000195 | prose | pages [12] -->
and a comparison to the actual population distribution taken from the Southeastern United States [1]

<!-- b000196 | furniture | pages [13] -->
Team # 10496

<!-- b000197 | furniture | pages [13] -->
Page 12 of 33

<!-- b000198 | prose | pages [13] -->
other’s receiver frequency. The most basic way to create two-way capabil- ity is to, for example, give receiver A a receiving frequency of 145MHz and a transmission frequency of 145.6MHz and have receiver A’ be the inverse of that (145.6MHz receiving, 145.0MHz transmission). A deeper analysis shows an immediate, serious ﬂaw with this approach. When a signal is be- ing transmitted from one to the other, it will be (essentially) immediately transmitted back to the ﬁrst, creating an feedback loop of transmission. As a repeater is actively receiving whenever it is transmitting, there will be some amount of feedback even if we attempt to implement privacy lines in some clever way.

<!-- b000199 | prose | pages [13] -->
The other approach to creating a chain of is to ”stagger” the receiving and transmission frequencies such that the ﬁrst repeater in a chain trans- mits at the frequency the second chain receives on, and so on. From our assumed minimum spacing of 600KHz, we have 5 distinct pairs of frequen- cies to work with. Let us assign names to the types of repeaters as follows:

<!-- b000200 | prose | pages [13] -->
• A - receiving frequency = 145.0MHz, transmitting frequency = 145.6MHz

<!-- b000201 | prose | pages [13] -->
• B - receiving frequency = 145.6MHz, transmitting frequency = 146.2MHz

<!-- b000202 | prose | pages [13] -->
• C - receiving frequency = 146.2MHz, transmitting frequency = 146.8MHz

<!-- b000203 | prose | pages [13] -->
• D - receiving frequency = 146.8MHz, transmitting frequency = 147.4MHz

<!-- b000204 | prose | pages [13] -->
• E - receiving frequency = 147.4MHz, transmitting frequency = 148.0MHz

<!-- b000205 | prose | pages [13] -->
Using these sets of frequencies, we see that a chain like A-B-C-D-E is a vi- able method for providing more long-range communication. Indeed, this method of chaining is the one we adopt in our approach to the problem.

<!-- b000206 | prose | pages [13] -->
4.2.2 Bi-directional and Extended Chains

<!-- b000207 | prose | pages [13] -->
One issue yet to be addressed by the chaining method described above is how one can transmit in the opposite direction. An effective way of deal- ing with this issue - and the one we’ve adopted for the rest of this report - is using the ”inverses” of the repeaters enumerated above to transmit in the opposite direction. If we pair an A’ repeater with every B, B’ with C, C’ with D and D’ with E, then we can get two-way transmission along this line. Without using private lines in a clever way, we still run into the feed- back issue we ran into above - we’ll describe how we plan to get around

<!-- b000208 | furniture | pages [14] -->
Team # 10496

<!-- b000209 | furniture | pages [14] -->
Page 13 of 33

<!-- b000210 | prose | pages [14] -->
this below.

<!-- b000211 | prose | pages [14] -->
In addition to bi-directionality, it’s not immediately clear from the above description how to create a chain of repeaters longer than 5. First, given the size of area involved, the range of the repeaters being used, and how each repeater is assigned a type, it’s unlikely there will be very many longer chains. However, in the interest of covering extreme cases and allowing this algorithm to be generalized to larger regions, we provide a method for creating longer chains. We could create a very weak-broadcasting E’ tower at the edge of the range of the end of an A-B-C-D-E chain (weak enough that its transmission back to the E repeater is not an issue), pairing it with both a D and a D’ repeater at the same location. The D and D’ repeaters would be set to different privacy lines so they wouldn’t be activated simul- taneously - if they are activated simultaneously, we can simply shut them both down or have the repeaters time out after a ﬁxed amount of time. Af- ter this point, the chain could continue to be extended through linking in a C/C’ node, then a B/B’ node, and so on.

<!-- b000212 | prose | pages [14] -->
4.3 Naive Approach

<!-- b000213 | prose | pages [14] -->
An extremely simpliﬁed way to view this problem is as follows: let us provide a way for anybody to broadcast anywhere by simply blanketing the entire area under consideration with a network of evenly-spaced, con- nected repeaters (and then removing those repeaters that don’t cover any people). There are a number of issues with this approach. First, it’s far from efﬁcient - depending on the population distribution, it’s very likely that at least some of the given area is at most sparsely populated, and unneces- sary to cover with repeaters. Second, if it is implemented by alternating ”inverse” repeaters (repeaters who can speak to each other), it’s likely there would be signiﬁcant issues in practice. Without using some kind of privacy lines, there would be no way to prevent some kind of feedback loop from occurring. Using a staggered repeater approach without running into the feedback issue would allow for only one-way transmission, something that would be unacceptable for most amateur radio use.

<!-- b000214 | furniture | pages [15] -->
Team # 10496

<!-- b000215 | prose | pages [15] -->
50

<!-- b000216 | prose | pages [15] -->
40

<!-- b000217 | prose | pages [15] -->
30

<!-- b000218 | prose | pages [15] -->
20

<!-- b000219 | prose | pages [15] -->
10

<!-- b000220 | prose | pages [15] -->
0

<!-- b000221 | prose | pages [15] -->
−10

<!-- b000222 | prose | pages [15] -->
−20

<!-- b000223 | prose | pages [15] -->
−30

<!-- b000224 | prose | pages [15] -->
−40

<!-- b000225 | prose | pages [15] -->
−50 −50 −40 −30 −20 −10

<!-- b000226 | furniture | pages [15] -->
Page 14 of 33

<!-- b000227 | prose | pages [15] -->
0 0 10 20 30 40 50

<!-- b000228 | caption | pages [15] -->
Figure 2: The network generated by the naive approach described above

<!-- b000229 | prose | pages [15] -->
Finally, even if there were no issue with feedback, a single, blanketing network would allow for very little usage. The user would have two op- tions: either he or she could talk locally without using a repeater or he or she could broadcast to the entire area. As a consequence, only a single user could use the network at any given time. For a large number of users, this would be untenable.

<!-- b000230 | prose | pages [15] -->
Implementing Privacy Lines to Reduce Interference 4.4

<!-- b000231 | prose | pages [15] -->
As mentioned earlier in the document, using privacy lines can help miti- gate interference. However, they need to be used carefully in order to be of much use. Two repeaters with differing privacy lines that are within range of one another can still interfere with one another if both are activated and broadcasting at the same time. Indeed, with the node layout above, there is really no “direction” of talk, and broadcasts take multiple paths to get to the same location. Because of these complexities, there’s really no way to assign privacy lines to organize communications in a controlled, rational manner.

<!-- b000232 | prose | pages [15] -->
One common method of organization for repeater networks is to assign one repeater to be the central“”hub” of the entire network CITE. Assign-

<!-- b000233 | furniture | pages [16] -->
Team # 10496

<!-- b000234 | furniture | pages [16] -->
Page 15 of 33

<!-- b000235 | prose | pages [16] -->
ing a hub affords us a number of beneﬁts. For one thing, it lets us assign a direction to each broadcast - each transmission can either be “toward” or “away from” the hub. In addition, it lets us create subnetworks across which users can talk without monopolizing the whole network, something that has a very important beneﬁts. Along with our assumption about the distribution of calls, these subnetworks let us localize demand - a call be- tween two people along a certain subnetwork can be entirely conﬁned to that subnetwork, leaving the rest of the network free for others to use.

<!-- b000236 | prose | pages [16] -->
Being able to categorize a signal as moving in a particular “direction” does no good if we cannot actually control how the signal propagates through the network. Below is an image illustrating the method we use to achieve directional control:

<!-- b000237 | caption | pages [16] -->
Figure 3: A typical network generated by our algorithm. The colors corre-

<!-- b000238 | prose | pages [16] -->
spond to the particular type of repeaters present at that location. Dark blue = A, light blue = B/A’, yellow = C/B’ and maroon = D/C’.

<!-- b000239 | prose | pages [16] -->
As can be seen above, most repeaters have two privacy lines associated with them. This is a destination label rather than the particular privacy lines accepted there. The above system works as follows. First, the red numbers represent the privacy lines associated with incoming calls des- tined for other sub-branches of the network. For example, if repeater 6/13

<!-- b000240 | furniture | pages [17] -->
Team # 10496

<!-- b000241 | furniture | pages [17] -->
Page 16 of 33

<!-- b000242 | prose | pages [17] -->
wants to send a message to repeater 8/15, it would broadcast a signal on privacy line 15. Depending on which B/A’ repeater it is primarily linked with one it is linked with, the signal from 6/13 will be picked up by both 5/11 and 4/12 and then rebroadcast with privacy line 15 (under our as- sumption of instantaneous transmission, this is OK. However, in practical applications, this is a potential issue, and is addressed in our ”Limitations” section). When it reaches the hub, the hub hears the signal and rebroad- casts it with the outgoing privacy line associated with repeater 15 (in this case, 8). The node 7/14 is the only B/A’ node to recognize that privacy line, and so it is the only one to pick it up and rebroadcast it (again, with privacy line 8). This is heard by the 8/15 node, which in turn broadcasts a signal with privacy line 54, indicating that the transmission is not to be passed any further.

<!-- b000243 | prose | pages [17] -->
That example was a little bit long, so let us review the core idea. The location of each pair of repeaters is associated with two privacy lines, one ingoing and one outgoing. Outgoing repeaters (A-B-C-D-E) accept the pri- vacy line associated with their current location as well as the outgoing pri- vacy lines associated with locations that they are “on the way” to, from the perspective of the hub. Ingoing repeaters also accept the ingoing privacy lines associated with repeaters that they are “on the way” to. This includes locations on the way to the hub on their subnetwork as well as those re- peaters on other subnetworks. Effectively, users are free to communicate within their subnetworks without having to worry about affecting broad- casts in other subnetworks. The net result is a reduction of interference and an increase in the network’s overall capacity.

<!-- b000244 | prose | pages [17] -->
4.5 K-Means Clustering

<!-- b000245 | prose | pages [17] -->
One of the weaknesses of the naive algorithm is its failure to adapt to the population distribution that it is presented with. Heuristically speaking, the best way to cover as many users as possible with as few repeaters as possible is to center repeaters in areas with high population density. This approach is especially effective in realistic population distributions since users are likely to be clumped together in regions of high density.

<!-- b000246 | prose | pages [17] -->
For this reason, clustering is an important part of our repeater network generation algorithm (which is outlined in the Main Network Generation We use the k-means clustering algorithm, Algorithm, included below). which seeks to group n data points into k clusters (where k must be spec- iﬁed) so that each data point is assigned to the cluster with mean closest

<!-- b000247 | furniture | pages [18] -->
Team # 10496

<!-- b000248 | prose | pages [18] -->
40

<!-- b000249 | prose | pages [18] -->
30

<!-- b000250 | prose | pages [18] -->
20

<!-- b000251 | prose | pages [18] -->
10

<!-- b000252 | prose | pages [18] -->
0

<!-- b000253 | prose | pages [18] -->
−10

<!-- b000254 | prose | pages [18] -->
−20

<!-- b000255 | prose | pages [18] -->
−30

<!-- b000256 | prose | pages [18] -->
−40 −40 −30 −20 −10

<!-- b000257 | furniture | pages [18] -->
Page 17 of 33

<!-- b000258 | prose | pages [18] -->
0 0 10 20 30 40

<!-- b000259 | caption | pages [18] -->
Figure 4: k-means clustering on a population

<!-- b000260 | prose | pages [18] -->
to its value, to assign each user to a cluster. Conceptually,k-means clus- tering assigns data points of similar value to the same cluster [7]. In our case, this means that users situated close together are grouped together. We then place a repeater in the mean location (or centroid) of each clus- ter. In general, this gives us a list of repeater locations located in regions of high density. In realistic population distributions, these repeater locations are likely to encompass population centers.

<!-- b000261 | heading | pages [18] -->
Algorithm 2 Main Network Generation Algorithm

<!-- b000262 | prose | pages [18] -->
MaximumRepeaterRange, Require: UserPositions, NumberO f Clusters UserRanges,

<!-- b000263 | prose | pages [18] -->
Ensure: RepeaterPositions contains a list of all of the repeater positions,

<!-- b000264 | prose | pages [18] -->
Channels contains their channel assignments.

<!-- b000265 | prose | pages [18] -->
Cluster() UserPositions with Run algorithm inputs and NumberO f Clusters to cluster the data, obtaining the positions of the centroids of the clusters. Set RepeaterPositions equal to the positions of the centroids. Run GetRepeaterRanges() with inputs UserRanges, RepeaterPositions, and MaximumRegionRange to obtain RepeaterRanges ConnectComponents() Run RepeaterPositions, with inputs RepeaterRanges and MaximumRepeaterRange to obtain new values for those variables. This connects any disconnected repeaters. Obtain RepeaterAdjacencies, the adjacency matrix of the network by de- termining which repeaters are within range of each other.

<!-- b000266 | prose | pages [18] -->
AssignChannels() RepeaterAdjacencies input Run with to obtain Channels, which contains the channel assignment for each repeater.

<!-- b000267 | furniture | pages [19] -->
Team # 10496

<!-- b000268 | furniture | pages [19] -->
Page 18 of 33

<!-- b000269 | heading | pages [19] -->
Note: The Cluster() algorithm referred to above is simply the k-means

<!-- b000270 | prose | pages [19] -->
clustering method described earlier in this section.

<!-- b000271 | prose | pages [19] -->
4.5.1 Connecting Clusters

<!-- b000272 | prose | pages [19] -->
By using a clustering process we can obtain some given number of posi- tions at which to place repeaters to extend coverage to users. While some of these repeaters might be within range of each other, it is unlikely that they form a network with a single component. It is far more likely, especially when working with the clumped population models discussed above, that there exist at least two disconnected components in our repeater network. As mentioned previously, we would like all users within range of a repeater to be able to communicate with any other user that is within range of a re- peater. Thus, we must somehow connect the disconnected components of our network. Since our goal is to minimize the number of repeaters used, we would like to do so using as few repeaters as possible.

<!-- b000273 | prose | pages [19] -->
Let di,j be the minimum distance between any node in component i and any node in component j. Consider the components of our network to be the nodes of a graph where the weight of the edge between component i and component j is di,j. In conceptual terms, the most efﬁcient way to span this graph is by constructing a minimum spanning tree. Similarly, the shortest way to connect the components in our network is by constructing a minimum spanning tree using repeaters. This will ensure that all of our network components are connected while using as few repeaters to do so as possible.

<!-- b000274 | prose | pages [19] -->
We used Algorithm 3 (detailed in pseudocode below) to accomplish this goal.

<!-- b000275 | furniture | pages [20] -->
Team # 10496

<!-- b000276 | heading | pages [20] -->
Algorithm 3 Connect Components

<!-- b000277 | furniture | pages [20] -->
Page 19 of 33

<!-- b000278 | prose | pages [20] -->
Require: RepeaterPositions, RegionRanges, MaxRegionRange Ensure: All of the repeaters in RepeaterPositions are part of the same com-

<!-- b000279 | prose | pages [20] -->
ponent of the repeater graph. Repeaters are connected if they are within range of each other. while NumberO f Components > 1 do

<!-- b000280 | prose | pages [20] -->
Let minDist be the minimum distance between two repeaters in differ- ent components. Let startRepeaterPosition and endRepeaterPosition be the positions of these repeaters. Let numRepeatersRequired be the number of repeaters required to span minDist if their ranges are MaxRegionRange.

<!-- b000281 | prose | pages [20] -->
minDist Add a repeater miles away from numRepeatersRequired startRepeaterPosition in the direction of endRepeaterPosition.

<!-- b000282 | prose | pages [20] -->
Note that this repeater will be part of the same network component as startRepeater. end while

<!-- b000283 | prose | pages [20] -->
Note: This algorithm essentially constructs a minimum spanning tree of a graph containing the disconnected repeater components in our network as nodes. We then use that minimum spanning tree as part of our network to ensure continuity.

<!-- b000284 | prose | pages [20] -->
4.5.2 Assigning Channels

<!-- b000285 | prose | pages [20] -->
Once the network is connected, channels must be assigned to implement the interference-reducing structure described in Section 4.4.

<!-- b000286 | prose | pages [20] -->
First, we must choose a repeater to serve as the hub of the network. We prefer a hub which has the least average geodesic distance to other nodes in the network (also known as the greatest closeness centrality) for a number of reasons. First, this reduces the likelihood that we will need to include an extended chain (see section 4.2) in our network, which requires more nodes than a bi-directional chain. Also, choosing a hub with the least average geodesic distance minimizes the number of nodes that will be tied up by a message passing through the hub.

<!-- b000287 | prose | pages [20] -->
Once we have chosen a hub, we assign channels of increasing number stepping outward from the hub as described in Algorithm 4 below. Note that repeater frequencies are assigned according to the table below:

<!-- b000288 | furniture | pages [21] -->
Team # 10496

<!-- b000289 | prose | pages [21] -->
Channel Number 1 2 3 4 5

<!-- b000290 | heading | pages [21] -->
Algorithm 4 Assign Channels

<!-- b000291 | furniture | pages [21] -->
Page 20 of 33

<!-- b000292 | prose | pages [21] -->
Frequencies A B/A’ C/B’ D/ C’ E/D’

<!-- b000293 | prose | pages [21] -->
Require: RepeaterAdjacencies, the adjacency matrix for our repeater net-

<!-- b000294 | prose | pages [21] -->
work. Ensure: Channels contains a list of the channel assignments of each re-

<!-- b000295 | prose | pages [21] -->
peater such that each repeater is of the proper channel to communicate with its neighbor closest to the hub of the network. Find the repeater with the highest closeness centrality in the network. This is our hub repeater. Assign it channel 1. Let CurrentChannel = 1. Let ConnectedRepeaters contain all of the repeaters connected to the hub. while At least one repeater does not have a channel do

<!-- b000296 | prose | pages [21] -->
Let NextConnectedRepeaters be an empty array for all Repeaters in ConnectedRepeaters do

<!-- b000297 | prose | pages [21] -->
Assign the repeater to channel CurrentChannel + 1. Add all of the repeaters connected to the repeater that do not have channels to NextConnectedRepeaters end for Increment CurrentChannel Let ConnectedRepeaters equal NextConnectedRepeaters end while

<!-- b000298 | prose | pages [21] -->
5

<!-- b000299 | heading | pages [21] -->
Results

<!-- b000300 | prose | pages [21] -->
5.1 Procedure

<!-- b000301 | prose | pages [21] -->
We evaluate our model by attempting to measure the overall quality of the network. The ﬁrst metric we measure is the coverage of the network by looking at the number of people not covered the network. In addition to this, we generate results of our algorithm for different cluster sizes which effects the number of repeaters used in the network. The last metric we use to measure this is the transmission capacity for our network, which is very

<!-- b000302 | furniture | pages [22] -->
Team # 10496

<!-- b000303 | furniture | pages [22] -->
Page 21 of 33

<!-- b000304 | prose | pages [22] -->
Population Distribution

<!-- b000305 | prose | pages [22] -->
5 clumps # of clusters Random 10 clumps 20 clumps 40 clumps

<!-- b000306 | prose | pages [22] -->
12.60 ± 4.98 17.00 ± 0.00 5 16.60 ± 0.89 17.00 ± 0.00 17.00 ± 0.00 24.60 ± 5.90 36.20 ± 1.10 10 27.80 ± 3.63 26.60 ± 2.61 31.00 ± 4.24 37.00 ± 5.10 43.40 ± 2.19 15 39.00 ± 1.41 37.00 ± 2.83 40.60 ± 2.97 49.00 ± 6.48 55.00 ± 2.45 20 50.60 ± 2.97 50.60 ± 2.97 51.00 ± 3.16 61.80 ± 4.82 74.60 ± 3.85 25 62.20 ± 1.79 64.20 ± 3.35 65.80 ± 3.35 25.2 ± 1.92 43.20 ± 0.84 Naive 33.0 ± 2.45 33.6 ± 2.610 40.0 ± 1.58

<!-- b000307 | caption | pages [22] -->
Table 1: Mean number of repeaters that were used in constructing the net-

<!-- b000308 | prose | pages [22] -->
work

<!-- b000309 | prose | pages [22] -->
important for the network to be usable. We measure this for both our algo- rithm and the naive algorithm to provide a comparison between the two. Sensitivity analysis is calculated for each of the metrics by determining the variability of each metric within a given population.

<!-- b000310 | prose | pages [22] -->
We generate clumped population distributions containing different num- ber of clumps sizes (5, 10, 20, and 40) to test the network. A random pop- ulation distribution is used as well to see how our network deals with a disperse population. We test the algorithm on this variety of different dis- tributions to account for the variability of population distributions with different locations. For each of these 5 types of population distributions we generate a 5 test populations data set to allow us to measure the variability of our algorithm within a given population distribution.

<!-- b000311 | prose | pages [22] -->
5.2 Number of Repeaters

<!-- b000312 | prose | pages [22] -->
The number of repeaters used in the naive algorithm is simply determined by the number that it takes to completely cover the network. In our algo- rithm the number of repeaters initially placed is based on the number of clusters used in the k-means algorithm. More repeaters can also be added to connect disconnected regions of the graph. In general though, we see an increase in the number of repeaters being placed as the # of initial clusters increases.

<!-- b000313 | prose | pages [22] -->
5.3 Coverage

<!-- b000314 | prose | pages [22] -->
The naive algorithm is guaranteed to have 100% coverage by construction. It is guarenteed to cover all of the people regardless of how many repeaters

<!-- b000315 | furniture | pages [23] -->
Team # 10496

<!-- b000316 | prose | pages [23] -->
# of clusters Random

<!-- b000317 | furniture | pages [23] -->
Page 22 of 33

<!-- b000318 | prose | pages [23] -->
Population Distribution

<!-- b000319 | prose | pages [23] -->
5 clumps 10 clumps 20 clumps 40 clumps

<!-- b000320 | prose | pages [23] -->
18.40 ± 23.38 382.20 ± 25.11 5 84.60 ± 56.18 183.0 ± 52.65 294.40 ± 51.93 5.400 ± 1.14 88.80 ± 24.05 10 8.80 ± 1.92 46.60 ± 11.50 50.60 ± 28.48 5.800 ± 1.92 18.40 ± 8.17 15 16.40 ± 20.49 17.60 ± 5.18 21.80 ± 4.09 5.800 ± 2.17 10.20 ± 2.17 20 7.80 ± 3.49 10.20 ± 2.28 12.20 ± 1.48 6.00 ± 1.58 7.80 ± 1.64 25 6.60 ± 0.89 10.80 ± 4.09 9.600 ± 2.61 0.00 ± 0.00 0.00 ± 0.00 Naive 0.00 ± 0.00 0.00 ± 0.00 0.00 ± 0.00

<!-- b000321 | caption | pages [23] -->
Table 2: Mean number of people who were not covered by the network for

<!-- b000322 | prose | pages [23] -->
different population distributions

<!-- b000323 | prose | pages [23] -->
that it must place. Our k-means clustering algorithm has a decrease in the population that is not covered by the network as the number of clusters used increased. This corresponds to more repeaters being placed in our preliminary construction of the network, which corresponds to a larger re- gion being covered by our network.

<!-- b000324 | prose | pages [23] -->
5.4 Transmission Capacity

<!-- b000325 | prose | pages [23] -->
The transmission capacity is measured through a simulation of potential requests made across the network. This metric has the potential to be very variable for different requests so it is run 10 times to get an average value. We perform sensitivity analysis by measuring the standard deviation in the results across the 10 simulations. This is done for each population distribu- tion to see if this metric remains effective across all distributions.

<!-- b000326 | prose | pages [23] -->
Population Distribution

<!-- b000327 | prose | pages [23] -->
10 clumps Random 5 clumps

<!-- b000328 | prose | pages [23] -->
K-means 0.0033 0.0144 Naive 0.0065 0.0076

<!-- b000329 | prose | pages [23] -->
20 clumps 40 clumps

<!-- b000330 | prose | pages [23] -->
0.0104 0.0104 0.0052 0.0083 0.0076 0.0075

<!-- b000331 | caption | pages [23] -->
Table 3: Standard deviation of the transmission capacity metric for different

<!-- b000332 | prose | pages [23] -->
population distributions

<!-- b000333 | prose | pages [23] -->
The standard deviation of the transmission capacity was ≈1% for most of the population distributions. For the naive algorithm the standard devi- ation for each one was approximately uniform illustrating that the metric

<!-- b000334 | furniture | pages [24] -->
Team # 10496

<!-- b000335 | furniture | pages [24] -->
Page 23 of 33

<!-- b000336 | prose | pages [24] -->
Population Distribution

<!-- b000337 | prose | pages [24] -->
5 clumps # of clusters Random 10 clumps 20 clumps 40 clumps

<!-- b000338 | prose | pages [24] -->
0.715 ± 0.102 0.621 ± 0.022 5 0.803 ± 0.047 0.780 ± 0.050 0.687 ± 0.033 0.850 ± 0.046 0.906 ± 0.029 10 0.951 ± 0.030 0.921 ± 0.019 0.943 ± 0.029 0.830 ± 0.074 0.977 ± 0.010 15 0.938 ± 0.058 0.967 ± 0.010 0.974 ± 0.004 0.828 ± 0.073 0.984 ± 0.004 20 0.950 ± 0.034 0.967 ± 0.014 0.981 ± 0.003 0.814 ± 0.042 0.985 ± 0.003 25 0.900 ± 0.037 0.954 ± 0.011 0.980 ± 0.004 0.313 ± 0.016 0.221 ± 0.002 Naive 0.274 ± 0.008 0.252 ± 0.010 0.236 ± 0.002

<!-- b000339 | caption | pages [24] -->
Table 4: Percentage of transmission requests that were processed by the

<!-- b000340 | prose | pages [24] -->
clustering network and naive network for different population distribu- tions

<!-- b000341 | prose | pages [24] -->
was valid across different population distributions. For our model using the k-means algorithm the standard deviation was a bit larger for the 5 clump data set of populations. However, even this had a standard devia- tion of < 1.5% which illustrates that our metric for transmission capacity was consistent.

<!-- b000342 | prose | pages [24] -->
The results for the transmission capacity show a signiﬁcant improve- ment in our algorithm to process requests over the network in comparison to the naive approach. In addition to this, we notice that as we increase the number of initial clusters the transmission capacity of our network in- creases. This creates a trade off between the number of repeaters and the transmission capacity and allows a balance to be chosen between the two based on the purpose of the network.

<!-- b000343 | prose | pages [24] -->
6

<!-- b000344 | heading | pages [24] -->
Discussion

<!-- b000345 | prose | pages [24] -->
6.1 Effects of 10,000 Users

<!-- b000346 | prose | pages [24] -->
In addition to developing a method for determining the minimum num- ber of repeaters necessary to accommodate 1000 simultaneous users, we were also asked how our solution would change if there were instead 10000 users.

<!-- b000347 | prose | pages [24] -->
Our algorithm can easily be run to generate networks to serve 10000 users. However, the quality of service these networks provide is uninspir- ing. In general, our algorithm’s networks were only able to successfully handle about half of the 10,000 transmissions attempted over 200 units of

<!-- b000348 | furniture | pages [25] -->
Team # 10496

<!-- b000349 | furniture | pages [25] -->
Page 24 of 33

<!-- b000350 | prose | pages [25] -->
time for any number of repeaters between 15 and 20. While this is signif- icantly better than the naive algorithm which only handles around 700 of 10,000 requests, it is obviously not ideal.

<!-- b000351 | prose | pages [25] -->
Increasing the number of users by an order of magnitude increases net- work trafﬁc by an order of magnitude as well, at least according to our assumptions. As a result, each repeater is roughly ten times as likely to be tied up in each timestep. This leads to many transmissions being blocked, especially transmissions through the hub of the network.

<!-- b000352 | prose | pages [25] -->
We have developed a number of approaches to dealing with this prob- lem. Our modeling of user transmissions indicates that approximately one third of user communications are between users that are only one repeater apart (i.e. within range of the same repeater). These sorts of communica- tions tie up that repeater, blocking transmissions through that part of the network. If such communications could be routed in a way that did not block the repeater, it follows that the network’s capacity would increase signiﬁcantly.

<!-- b000353 | prose | pages [25] -->
One strategy that we have considered adding to our algorithm is the ability to recursively add subnetworks to our network (using the same pro- cess as our main algorithm) at nodes where user density and therefore de- mand is high. These subnetworks are composed of repeaters with frequen- cies incompatible with the frequencies of the adjacent main node, elimi- nating the possibility of intereference. (see ﬁgure 4 below). Unfortunately, time constraints have prevented us from ﬁnishing this feature or conduct- ing an analysis of its effects.

<!-- b000354 | prose | pages [25] -->
Even though the idea hasn’t been fully developed, we illustrate how a subnetwork would look in the ﬁgure below. The addition of the 3 repeaters occurs near the central hub, which, in this example, we are assuming is an area of high population density. Therefore by adding this subnetwork, we would be assuming that the beneﬁt added by increasing the transmission capacity of the network would outweigh the cost of adding the extra re- peaters. A nice feature of this structure is it would allow you to place cost parameters on the repeaters and the transmission capacity to determine in what situations that it would be beneﬁcial to place an extra repeater.

<!-- b000355 | furniture | pages [26] -->
Team # 10496

<!-- b000356 | prose | pages [26] -->
40

<!-- b000357 | prose | pages [26] -->
30

<!-- b000358 | prose | pages [26] -->
20

<!-- b000359 | prose | pages [26] -->
10

<!-- b000360 | prose | pages [26] -->
0

<!-- b000361 | prose | pages [26] -->
−10

<!-- b000362 | prose | pages [26] -->
−20

<!-- b000363 | prose | pages [26] -->
−30

<!-- b000364 | prose | pages [26] -->
−40

<!-- b000365 | prose | pages [26] -->
−50 −50 −40 −30 −20 −10

<!-- b000366 | furniture | pages [26] -->
Page 25 of 33

<!-- b000367 | prose | pages [26] -->
0 10 20 30 40

<!-- b000368 | prose | pages [26] -->
(a) No subnetwork

<!-- b000369 | prose | pages [26] -->
40

<!-- b000370 | prose | pages [26] -->
30

<!-- b000371 | prose | pages [26] -->
20

<!-- b000372 | prose | pages [26] -->
10

<!-- b000373 | prose | pages [26] -->
0

<!-- b000374 | prose | pages [26] -->
−10

<!-- b000375 | prose | pages [26] -->
−20

<!-- b000376 | prose | pages [26] -->
−30

<!-- b000377 | prose | pages [26] -->
−40

<!-- b000378 | prose | pages [26] -->
−50 −50 −40 −30 −20 −10 0 10 20 30 40

<!-- b000379 | prose | pages [26] -->
(b) With subnetwork

<!-- b000380 | caption | pages [26] -->
Figure 5: A typical network generated by our algorithm with a localized

<!-- b000381 | prose | pages [26] -->
subnetwork included

<!-- b000382 | prose | pages [26] -->
One of the weaknesses of our network design is its dependence on a central hub, which in many cases serves as a chokepoint limiting the ﬂow of cross-network communications. If more private lines were available for

<!-- b000383 | furniture | pages [27] -->
Team # 10496

<!-- b000384 | furniture | pages [27] -->
Page 26 of 33

<!-- b000385 | prose | pages [27] -->
use we could use them to add multiple hubs to our network, similar to the way IP addresses are used to route trafﬁc to different hubs on the Internet.

<!-- b000386 | prose | pages [27] -->
6.2 Effects of Mountainous Terrain

<!-- b000387 | prose | pages [27] -->
Currently our algorithm assumes a ﬂat terrain devoid of features that might impact the range of repeaters or mobile devices. However, we feel that our algorithm could be more or less readily adapted to deal with defects in line-of-sight-propagation caused by mountainous areas.

<!-- b000388 | prose | pages [27] -->
The main complication introduced by mountainous areas is the intro- duction of non-symmetrical maximum repeater ranges that vary with po- sition. This would mainly affect the way in which we use clustering to place our initial repeaters and our method for connecting the disconnected components of our network. The other parts of our algorithm, speciﬁcally the use of private lines and the assignment of channels, are dependent only on the adjacencies of repeaters in our network and would not be affected.

<!-- b000389 | prose | pages [27] -->
While more experimentation is needed, we feel that the use of clustering would still serve well as an initial method for determining where to place repeaters. However, we would then attempt to optimize the position of the repeaters to encompass more users through an optimization technique such as simulated annealing.

<!-- b000390 | prose | pages [27] -->
A similar approach could be taken to connect disconnected network components. The straight-line minimum spanning tree approach could be used as a starting point for the placement of additional repeaters, with op- timization then applied to try to maximize the reduction in the distance between disconnected components.

<!-- b000391 | prose | pages [27] -->
Obviously, this additional optimization would come with signiﬁcant runtime penalties.

<!-- b000392 | prose | pages [27] -->
We feel that mountainous terrain could even decrease the number of repeaters needed, since repeaters could be placed on elevated terrain to achieve increased range.

<!-- b000393 | prose | pages [27] -->
7

<!-- b000394 | heading | pages [27] -->
Conclusion

<!-- b000395 | prose | pages [27] -->
Overall, the proposed algorithm tends to do a pretty good job of pro- ducing a network that passes the “eyeball test” from a heuristic viewpoint. That is, our algorithm proposes a solution that mimics the overall shape of the population distribution, covers the vast majority of potential users and uses few obviously wasteful repeater nodes.

<!-- b000396 | furniture | pages [28] -->
Team # 10496

<!-- b000397 | furniture | pages [28] -->
Page 27 of 33

<!-- b000398 | prose | pages [28] -->
While the algorithm performs well in many situations, when the num- ber of clusters used to generate our initial repeaters is too large, we run into problems. Our network is heavily dependent upon using privacy lines to control the ﬂow of signal trafﬁc. Because there are a limited number of privacy lines available to us, this puts a hard cap - of having repeaters in at most about 25 distinct locations - on the number of repeaters that can be used. As a result, there is also an effective cap on the number of initial clusters that we can use to generate our initial repeater locations. Once we get past about 20, we no longer have enough privacy lines to implement the signal-control scheme outlined in section 4.4.

<!-- b000399 | prose | pages [28] -->
Though the cap on the number of initial clusters reduces our options when it comes to designing a network, it also greatly diminishes our prob- lem space. Because of the limited number of options, we could very easily search across all possible numbers of initial clusters (in increasing order) to ﬁnd the minimum value that gave us a network satisfying our transmis- sions capacity requirements for a given population distribution. This ap- proach is not as direct as searching across the number of available nodes, but it should give us the best possible solution generated by our approach for a particular population distribution.

<!-- b000400 | prose | pages [28] -->
When our algorithm does receive a good value for the number of clus- ters in the population, the data shows that the network it creates does an excellent job of handling trafﬁc under the assumptions that we have made. For example, for the case of 15 initial clusters above, the algorithm created a network that covers over 97% of the population and is able to transmit ≈95% of the requests on average. This performance corresponds to a net- work that typically contains only about 40 repeaters. Overall, when used properly, our algorithm can produce very efﬁcient, effective networks. We feel that it could serve as a useful tool in VHF radio network planning.

<!-- b000401 | prose | pages [28] -->
8

<!-- b000402 | heading | pages [28] -->
Future Work

<!-- b000403 | prose | pages [28] -->
8.1

<!-- b000404 | heading | pages [28] -->
Limitations of our model

<!-- b000405 | prose | pages [28] -->
Though we feel our algorithm is quite strong in general, it does have a num- ber of limitations. For one thing, k-means clustering is a non-deterministic algorithm. It simply ﬁnds a ”good” way to cluster the data and runs with it. Because of this, for a given population distribution, our algorithm doesn’t return the same result each time. This isn’t the most reassuring when we’re supposed to be ﬁnding the ”optimal” solution.

<!-- b000406 | furniture | pages [29] -->
Team # 10496

<!-- b000407 | furniture | pages [29] -->
Page 28 of 33

<!-- b000408 | prose | pages [29] -->
In addition to the concern above, the method of using privacy lines for controlling the ﬂow of where a signal gets broadcasted contains a poten- tial complication in certain circumstances (recall ﬁgure 3 above) . In real- world applications, repeaters take a bit of time to process a signal before re-broadcasting it. When both the 5/11 and 4/12 towers pick up the signal from 6/13, there’s a very real chance that the two repeaters will process the signal at a slightly different speed. If this happens, then 1 would receive two identical signals, slightly offset, which would be less than ideal. Using the same brand of repeater throughout the network might help mitigate the impact of this issue. In addition, with enough private lines (though admit- tedly, you’d need a lot), this effect can be completely addressed.

<!-- b000409 | prose | pages [29] -->
The limited number of private lines imposes a couple of very important limitations on our model. First of all, it introduces a bound on the number of repeaters that can be used in the overall network. Because each pair of repeaters needs two distinct private lines and private lines must be used to specify both local communication and communication across the entire network, the overall network can have at most 25 distinct repeater loca- tions. In addition, we have limited tools to limit the amount of demand on key repeaters such as the hub. As mentioned above, we use privacy lines the way the internet uses IP addresses. With a larger number of them at our disposal, we could create a larger (if needed), more ﬂexible network that could route much of its ﬂow around the hub.

<!-- b000410 | prose | pages [29] -->
The algorithm as currently implemented can really only be used for optimizing with respect to the number of repeaters. Someone who is con- sidering this problem may wish to, for example, enforce a steep penalty for not including a user in the network. Presently, the model doesn’t allow for this. More generally, the model doesn’t allow the user to weigh the cost of including an extra repeater versus the other beneﬁts that extra repeater would bring.

<!-- b000411 | prose | pages [29] -->
Another area that the model fails to address is any kind of variation in atmospheric conditions or weather that could reduce the broadcast range of our repeaters. This is a much larger concern for chains of repeaters, be- cause if the range of any is sufﬁciently reduced it could break the chain. Though it is not explicitly addressed, the risk of this concern can be miti- gated by building a buffer into the maximum range of our broadcast towers (for example, assuming a 7-8 mile broadcast radius when we actually have a 9-mile radius).

<!-- b000412 | prose | pages [29] -->
Finally, the code currently doesn’t allow the user to exactly specify the number of repeaters being used for a given network—rather, this is roughly controlled by the number of clusters given as input to the k-means cluster-

<!-- b000413 | furniture | pages [30] -->
Team # 10496

<!-- b000414 | furniture | pages [30] -->
Page 29 of 33

<!-- b000415 | prose | pages [30] -->
ing algorithm. The ability to exactly specify could relatively easily added via a post-processing step in which the repeaters whose removal would lead to the least reduction in network quality are removed until the desired number of repeaters is reached.

<!-- b000416 | prose | pages [30] -->
8.2

<!-- b000417 | heading | pages [30] -->
Ways to improve the model

<!-- b000418 | prose | pages [30] -->
In addition to the issues raised in our ”Discussion” section, there were sev- eral other considerations that we did not have time to fully address. First, we could extend our model to take into account the “blind interference” phenomenon discussed in the assumptions section.

<!-- b000419 | prose | pages [30] -->
Second, in the real world, repeaters do not immediately transmit radio messages; ideally we would take into account this nontrivial switching time in a more rigorous fashion. Third, we assumed throughout that users make equal demand on the system, something that just isn’t true in the real world. Including the option for a user to have higher demand than others - something that could be simulated in our model by placing “multiple users” at the location of a heavy user—would increase the value and accuracy of the model. Finally, it would be nice if our heavily-stressed hub repeater was located in a less populous area to isolate it from local demand.

<!-- b000420 | furniture | pages [31] -->
Team # 10496

<!-- b000421 | prose | pages [31] -->
A

<!-- b000422 | heading | pages [31] -->
Appendix

<!-- b000423 | prose | pages [31] -->
40

<!-- b000424 | prose | pages [31] -->
30

<!-- b000425 | prose | pages [31] -->
20

<!-- b000426 | prose | pages [31] -->
10

<!-- b000427 | prose | pages [31] -->
0

<!-- b000428 | prose | pages [31] -->
−10

<!-- b000429 | prose | pages [31] -->
−20

<!-- b000430 | prose | pages [31] -->
−30

<!-- b000431 | prose | pages [31] -->
−40 −40 −30 −20 −10 0 10 20 30

<!-- b000432 | prose | pages [31] -->
(a) Random Population Distribution

<!-- b000433 | prose | pages [31] -->
40

<!-- b000434 | prose | pages [31] -->
30

<!-- b000435 | prose | pages [31] -->
20

<!-- b000436 | prose | pages [31] -->
10

<!-- b000437 | prose | pages [31] -->
0

<!-- b000438 | prose | pages [31] -->
−10

<!-- b000439 | prose | pages [31] -->
−20

<!-- b000440 | prose | pages [31] -->
−30

<!-- b000441 | prose | pages [31] -->
−40 −40 −30 −20 −10 0 10 20 30

<!-- b000442 | prose | pages [31] -->
(c) Clumped Distribution - 5 Clumps

<!-- b000443 | furniture | pages [31] -->
Page 30 of 33

<!-- b000444 | prose | pages [31] -->
40

<!-- b000445 | prose | pages [31] -->
30

<!-- b000446 | prose | pages [31] -->
20

<!-- b000447 | prose | pages [31] -->
10

<!-- b000448 | prose | pages [31] -->
0

<!-- b000449 | prose | pages [31] -->
−10

<!-- b000450 | prose | pages [31] -->
−20

<!-- b000451 | prose | pages [31] -->
−30

<!-- b000452 | prose | pages [31] -->
−40

<!-- b000453 | prose | pages [31] -->
40 40

<!-- b000454 | prose | pages [31] -->
−40 −30 −20 −10 0 10 20 30 40

<!-- b000455 | prose | pages [31] -->
(b) Random Population Distribution

<!-- b000456 | prose | pages [31] -->
40

<!-- b000457 | prose | pages [31] -->
30

<!-- b000458 | prose | pages [31] -->
20

<!-- b000459 | prose | pages [31] -->
10

<!-- b000460 | prose | pages [31] -->
0

<!-- b000461 | prose | pages [31] -->
−10

<!-- b000462 | prose | pages [31] -->
−20

<!-- b000463 | prose | pages [31] -->
−30

<!-- b000464 | prose | pages [31] -->
−40

<!-- b000465 | prose | pages [31] -->
40 40

<!-- b000466 | prose | pages [31] -->
−40 −30 −20 −10 0 10 20 30 40

<!-- b000467 | prose | pages [31] -->
(d) Clumped Distribution - 5 Clumps

<!-- b000468 | caption | pages [31] -->
Figure 6: Examples of the network that our algorithm constructs on various

<!-- b000469 | prose | pages [31] -->
population distributions

<!-- b000470 | furniture | pages [32] -->
Team # 10496

<!-- b000471 | prose | pages [32] -->
40

<!-- b000472 | prose | pages [32] -->
30

<!-- b000473 | prose | pages [32] -->
20

<!-- b000474 | prose | pages [32] -->
10

<!-- b000475 | prose | pages [32] -->
0

<!-- b000476 | prose | pages [32] -->
−10

<!-- b000477 | prose | pages [32] -->
−20

<!-- b000478 | prose | pages [32] -->
−30

<!-- b000479 | prose | pages [32] -->
−40 −40 −30 −20 −10 0 10 20 30 40

<!-- b000480 | prose | pages [32] -->
(a) Clumped Distribution - 10 Clumps

<!-- b000481 | prose | pages [32] -->
40

<!-- b000482 | prose | pages [32] -->
30

<!-- b000483 | prose | pages [32] -->
20

<!-- b000484 | prose | pages [32] -->
10

<!-- b000485 | prose | pages [32] -->
0

<!-- b000486 | prose | pages [32] -->
−10

<!-- b000487 | prose | pages [32] -->
−20

<!-- b000488 | prose | pages [32] -->
−30

<!-- b000489 | prose | pages [32] -->
−40 −40 −30 −20 −10 0 10 20 30 40

<!-- b000490 | prose | pages [32] -->
(c) Clumped Distribution - 20 Clumps

<!-- b000491 | furniture | pages [32] -->
Page 31 of 33

<!-- b000492 | prose | pages [32] -->
40

<!-- b000493 | prose | pages [32] -->
30

<!-- b000494 | prose | pages [32] -->
20

<!-- b000495 | prose | pages [32] -->
10

<!-- b000496 | prose | pages [32] -->
0

<!-- b000497 | prose | pages [32] -->
−10

<!-- b000498 | prose | pages [32] -->
−20

<!-- b000499 | prose | pages [32] -->
−30

<!-- b000500 | prose | pages [32] -->
−40 −40 −30 −20 −10 0 10 20 30 40

<!-- b000501 | prose | pages [32] -->
(b) Clumped Distribution - 10 Clumps

<!-- b000502 | prose | pages [32] -->
40

<!-- b000503 | prose | pages [32] -->
30

<!-- b000504 | prose | pages [32] -->
20

<!-- b000505 | prose | pages [32] -->
10

<!-- b000506 | prose | pages [32] -->
0

<!-- b000507 | prose | pages [32] -->
−10

<!-- b000508 | prose | pages [32] -->
−20

<!-- b000509 | prose | pages [32] -->
−30

<!-- b000510 | prose | pages [32] -->
−40 −40 −30 −20 −10 0 10 20 30 40

<!-- b000511 | prose | pages [32] -->
(d) Clumped Distribution - 20 Clumps

<!-- b000512 | caption | pages [32] -->
Figure 7: More examples of the network that our algorithm constructs on

<!-- b000513 | prose | pages [32] -->
various population distributions

<!-- b000514 | furniture | pages [33] -->
Team # 10496

<!-- b000515 | prose | pages [33] -->
40

<!-- b000516 | prose | pages [33] -->
30

<!-- b000517 | prose | pages [33] -->
20

<!-- b000518 | prose | pages [33] -->
10

<!-- b000519 | prose | pages [33] -->
0

<!-- b000520 | prose | pages [33] -->
−10

<!-- b000521 | prose | pages [33] -->
−20

<!-- b000522 | prose | pages [33] -->
−30

<!-- b000523 | prose | pages [33] -->
−40 −40 −30 −20 −10 0

<!-- b000524 | furniture | pages [33] -->
Page 32 of 33

<!-- b000525 | prose | pages [33] -->
10 20 30 40

<!-- b000526 | prose | pages [33] -->
(a) Clumped Distribution - 40 Clumps

<!-- b000527 | prose | pages [33] -->
40

<!-- b000528 | prose | pages [33] -->
30

<!-- b000529 | prose | pages [33] -->
20

<!-- b000530 | prose | pages [33] -->
10

<!-- b000531 | prose | pages [33] -->
0

<!-- b000532 | prose | pages [33] -->
−10

<!-- b000533 | prose | pages [33] -->
−20

<!-- b000534 | prose | pages [33] -->
−30

<!-- b000535 | prose | pages [33] -->
−40 −40 −30 −20 −10 0 10 20 30 40

<!-- b000536 | prose | pages [33] -->
(b) Clumped Distribution - 40 Clumps

<!-- b000537 | caption | pages [33] -->
Figure 8: A few examples of the network that our algorithm constructs on

<!-- b000538 | prose | pages [33] -->
various population distributions

<!-- b000539 | furniture | pages [34] -->
Team # 10496

<!-- b000540 | heading | pages [34] -->
References

<!-- b000541 | furniture | pages [34] -->
Page 33 of 33

<!-- b000542 | references | pages [34] -->
[1] Socioeconomic data and applications center. ”http://sedac.ciesin.

<!-- b000543 | references | pages [34] -->
columbia.edu/gpw/”. Viewed on 2011 February 13.

<!-- b000544 | references | pages [34] -->
[2] Vhf radios: Why you need one.

<!-- b000545 | references | pages [34] -->
”www.boatus.com/boattech/vhf.

<!-- b000546 | references | pages [34] -->
htm”, 2007. Viewed on 2011 February 12.

<!-- b000547 | references | pages [34] -->
”www.hamdata.com/

<!-- b000548 | references | pages [34] -->
[3] Information for the amateur radio enthusiast.

<!-- b000549 | references | pages [34] -->
fccinfo.html”, 2011. Viewed on 2011 February 11.

<!-- b000550 | references | pages [34] -->
[4] The Paciﬁc Crest Company.

<!-- b000551 | references | pages [34] -->
VHF/UHF Range Calculations.

<!-- b000552 | references | pages [34] -->
”http://www.mertind.com/argentina/Soporte20tecnico/

<!-- b000553 | references | pages [34] -->
Instrumentos/PDL/PDL20UHF-VHF20RANGE20CALCULATIONS.pdf”.

<!-- b000554 | references | pages [34] -->
Viewed on 2011 February 11.

<!-- b000555 | references | pages [34] -->
[5] Otis Dudley Duncan. The measurement of population distribution.

<!-- b000556 | references | pages [34] -->
Population Studies, 11(1):pp. 27–45, 1957.

<!-- b000557 | references | pages [34] -->
[6] The American Radio Relay League. Us amateur radio frequency allo-

<!-- b000558 | references | pages [34] -->
cations. ”www.arrl.org/frequency-allocations”. Viewed on 2011

<!-- b000559 | references | pages [34] -->
February 11.

<!-- b000560 | references | pages [34] -->
Information theory, inference and learning al-

<!-- b000561 | references | pages [34] -->
[7] David MacKay.

<!-- b000562 | references | pages [34] -->
”http://www.inference.phy.cam.ac.uk/

<!-- b000563 | references | pages [34] -->
gorithms, chapter 20.

<!-- b000564 | references | pages [34] -->
mackay/itprnn/ps/284.292.pdf”, 2003. Viewed on 2011 February 11.

<!-- b000565 | references | pages [34] -->
[8] The National Radio Astronomy Observatory.

<!-- b000566 | references | pages [34] -->
How radio waves

<!-- b000567 | references | pages [34] -->
”http://www.nrao.edu/index.php/learn/

<!-- b000568 | references | pages [34] -->
are

<!-- b000569 | references | pages [34] -->
produced.

<!-- b000570 | references | pages [34] -->
radioastronomy/radiowaves”, 2002.

<!-- b000571 | references | pages [34] -->
11.

<!-- b000572 | references | pages [34] -->
Viewed on 2011 February

<!-- b000573 | references | pages [34] -->
[9] John Owen. VHF/UHF TV Line of Sight Calculator. ”http://www.

<!-- b000574 | references | pages [34] -->
naval.com/sight/index.htm”, 2003. Viewed on 2011 February 11.

<!-- b000575 | references | pages [34] -->
[10] The International Amateur Radio Union.

<!-- b000576 | references | pages [34] -->
Ethics and operating

<!-- b000577 | references | pages [34] -->
”http://www.hamradiosecrets.com/support-files/

<!-- b000578 | references | pages [34] -->
procedures.

<!-- b000579 | references | pages [34] -->
ham-radio-operator-guidelines.pdf”, 2009.

<!-- b000580 | references | pages [34] -->
February 11.

<!-- b000581 | references | pages [34] -->
Viewed on 2011
