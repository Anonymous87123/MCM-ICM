# P-B-2011-12114-03fd7440

Status: machine-draft; not source-verified.


<!-- b000001 | title | pages [1] -->
VHF Repeater Placement

<!-- b000002 | prose | pages [1] -->
Control # 12114

<!-- b000003 | prose | pages [1] -->
February 14, 2011

<!-- b000004 | prose | pages [1] -->
1

<!-- b000005 | prose | pages [2] -->
Control # 12114 2

<!-- b000006 | prose | pages [2] -->
Summary Statement

<!-- b000007 | prose | pages [2] -->
Our task is to develop a model that determines how to minimally and adequately place VHF repeaters so that low-power users, such as mobile stations, can communicate with one another in situations where direct user-to-user contact would not be possible. We assume that we are given a population of users within a circular region of radius 40 miles, and we attempt to ﬁnd the minimal number of repeaters necessary to provide adequate coverage while minimizing the number of radio bands in use and keeping interference negligible. Although we assume that there must be a direct line of sight between a repeater and a user, our model allows for terrains of complex geometry including mountains and valleys. Throughout most of our analysis, we assume that repeater antennas are 18 feet above the ground, which corresponds to a coverage radius of 10 miles in a perfectly ﬂat region.

<!-- b000008 | prose | pages [2] -->
Initially, we employ a greedy algorithm to successively place repeaters in the locations that provide coverage to the most additional users.

<!-- b000009 | prose | pages [2] -->
In subsequent incarnations of the model, we consider goals other than maximal coverage in selecting the optimal positions. To assign frequency channels to these repeaters we form a graph whose vertices represent the repeaters, and we consider vertices to be adjacent if the repeaters are suﬃciently close to one another. This graph is then colored greedily.

<!-- b000010 | prose | pages [2] -->
To test our model, we generate population distributions using both uniformly random placement of users and a preferential attachment model that more closely matches real world population distributions. We ﬁnd that, using realistic population distributions, we were able to provide adequate coverage to 1000 simultaneous users with about 15 repeaters and 10000 users with about 20 repeaters; however by relaxing these conditions and requiring that only 95% of users be covered, we could lower these numbers to 10 and 15 respectively. We also showed that 21 repeaters should always be enough to provide coverage to a region with a radius of 40 miles.

<!-- b000011 | prose | pages [3] -->
Control # 12114

<!-- b000012 | heading | pages [3] -->
Contents

<!-- b000013 | contents | pages [3] -->
1

<!-- b000014 | heading | pages [3] -->
Background

<!-- b000015 | prose | pages [3] -->
3

<!-- b000016 | prose | pages [3] -->
5

<!-- b000017 | prose | pages [3] -->
Very High Frequency (VHF) . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 5

<!-- b000018 | prose | pages [3] -->
Repeaters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2

<!-- b000019 | prose | pages [3] -->
2 Problem Interpretation

<!-- b000020 | prose | pages [3] -->
3

<!-- b000021 | heading | pages [3] -->
Assumptions

<!-- b000022 | prose | pages [3] -->
4 Circle Covering

<!-- b000023 | prose | pages [3] -->
5

<!-- b000024 | prose | pages [3] -->
7

<!-- b000025 | prose | pages [3] -->
7

<!-- b000026 | prose | pages [3] -->
9

<!-- b000027 | prose | pages [3] -->
Radio Wave Propogation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1

<!-- b000028 | prose | pages [3] -->
5 Population Distribution

<!-- b000029 | prose | pages [3] -->
11

<!-- b000030 | prose | pages [3] -->
12

<!-- b000031 | prose | pages [3] -->
Uniform Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 12

<!-- b000032 | prose | pages [3] -->
Preferential Attachment Algorithm . . . . . . . . . . . . . . . . . . . . . . 5.2

<!-- b000033 | prose | pages [3] -->
6 Our Approach

<!-- b000034 | prose | pages [3] -->
13

<!-- b000035 | prose | pages [3] -->
13

<!-- b000036 | prose | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 Basic Coverage 13

<!-- b000037 | prose | pages [3] -->
Algorithmic Runtime . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1.1 15

<!-- b000038 | prose | pages [3] -->
Additional Layers: Maximizing Utility 6.2 . . . . . . . . . . . . . . . . . . . .

<!-- b000039 | prose | pages [3] -->
15

<!-- b000040 | prose | pages [3] -->
Basic Coverage as a Special Case 6.2.1 . . . . . . . . . . . . . . . . . . .

<!-- b000041 | prose | pages [3] -->
16

<!-- b000042 | prose | pages [3] -->
Runtime Analysis and Optimizations . . . . . . . . . . . . . . . . . 6.2.2 16

<!-- b000043 | prose | pages [3] -->
Additional Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2.3 18

<!-- b000044 | prose | pages [3] -->
Frequency Selection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.3

<!-- b000045 | prose | pages [3] -->
7

<!-- b000046 | heading | pages [3] -->
Results

<!-- b000047 | prose | pages [3] -->
18

<!-- b000048 | prose | pages [3] -->
18

<!-- b000049 | prose | pages [3] -->
Basic Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.1

<!-- b000050 | prose | pages [3] -->
7.2 Mountains and Complex Geometries

<!-- b000051 | prose | pages [3] -->
8

<!-- b000052 | heading | pages [3] -->
Conclusions

<!-- b000053 | prose | pages [3] -->
9 Future Considerations

<!-- b000054 | prose | pages [3] -->
18

<!-- b000055 | prose | pages [3] -->
. . . . . . . . . . . . . . . . . . . . .

<!-- b000056 | prose | pages [3] -->
23

<!-- b000057 | prose | pages [3] -->
24

<!-- b000058 | prose | pages [3] -->
25

<!-- b000059 | prose | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.1 Changes to the Model 25

<!-- b000060 | prose | pages [4] -->
Control # 12114 4

<!-- b000061 | prose | pages [4] -->
Ad-hoc Networks and Game Theory 9.1.1 . . . . . . . . . . . . . . . . .

<!-- b000062 | prose | pages [4] -->
25

<!-- b000063 | prose | pages [4] -->
One-to-One Communication . . . . . . . . . . . . . . . . . . . . . . 9.1.2 26

<!-- b000064 | prose | pages [4] -->
Non-static and Introduced Users . . . . . . . . . . . . . . . . . . . . 9.1.3 26

<!-- b000065 | prose | pages [4] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.2 Model Correctness 26

<!-- b000066 | prose | pages [4] -->
Region Topography . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.2.1 26

<!-- b000067 | prose | pages [4] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.3 Real World Data 26

<!-- b000068 | prose | pages [4] -->
Theoretical Issues . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.4

<!-- b000069 | prose | pages [4] -->
9.4.1 Algorithmic Improvement

<!-- b000070 | prose | pages [4] -->
27

<!-- b000071 | prose | pages [4] -->
. . . . . . . . . . . . . . . . . . . . . . .

<!-- b000072 | prose | pages [4] -->
27

<!-- b000073 | prose | pages [5] -->
Control # 12114

<!-- b000074 | prose | pages [5] -->
1

<!-- b000075 | heading | pages [5] -->
Background

<!-- b000076 | prose | pages [5] -->
5

<!-- b000077 | prose | pages [5] -->
Very High Frequency (VHF) 1.1

<!-- b000078 | prose | pages [5] -->
In most countries, the VHF frequencies 144-146 MHz are allocated for amateur radio. In the Americas, this band is 144-148 MHz.

<!-- b000079 | prose | pages [5] -->
These frequencies are commonly referred to The transmissions are local and generally require more as the 2-meter amateur radio. compact machinery than operating on other frequencies. Because of their reliability, this band is also used for communicating emergencies via mobile and hand-held transmission devices. Because they provide back-up emergency communication, transmitting on these frequencies usually requires a license. Transmission time may be limited to a set time, such as 30 seconds, and many people send courtesy tones to remind people to leave gaps between transmissions; these breaks accommodate accident or emergency reporting as well as prevent one person from hogging the frequency.

<!-- b000080 | prose | pages [5] -->
To prevent interference and to control the usage of transmitting, government agencies manage the frequency allocations. In the United States, the Federal Communications Com- mission “is charged with regulating interstate and international communications by radio, television, wire, satellite and cable.”[4] Originally, the spacing between 2-meter channels was 30kHz. When the bands became overloaded with users. the states split in their spac- ing method: some divided the stations in half such that the spacing between them became 15kHz; and others adopted a 20kHz spacing. When frequencies from the transmitters over- lap with only 15kHz diﬀerence, there can still be interference. With a spacing of 20kHz, there is virtually no interference [2].

<!-- b000081 | prose | pages [5] -->
1.2 Repeaters

<!-- b000082 | prose | pages [5] -->
In order to extend the distance a transmission can reach, repeaters receive input on a prescribed frequency and output the ampliﬁed signal at the original frequency ±600kHz. This pair of frequencies for a given repeater is commonly referred to as a channel. Over an antenna, repeaters transmit the signal usually as far as the observable horizon. For mobile and hand-held devices, this line-of-sight provides a very limited range of only a Due to the fact that repeaters are typically placed on high locations such few miles. as mountains, the observable horizon of the repeater spans much further than it would otherwise. Tropospheric bending extends this Radio Horizon even more from

<!-- b000083 | prose | pages [5] -->
√

<!-- b000084 | prose | pages [5] -->
r ≈1.23

<!-- b000085 | prose | pages [5] -->
to

<!-- b000086 | prose | pages [5] -->
√

<!-- b000087 | prose | pages [5] -->
h

<!-- b000088 | prose | pages [5] -->
√ 2h ≈1.41

<!-- b000089 | prose | pages [5] -->
r ≈

<!-- b000090 | prose | pages [5] -->
h,

<!-- b000091 | prose | pages [5] -->
where r is the radius or distance from the repeater antenna to the Radio Horizon and h is the height of the antenna in feet [9]. Note that at the edges of the coverage of a repeater

<!-- b000092 | prose | pages [6] -->
Control # 12114 6

<!-- b000093 | prose | pages [6] -->
– the fringe – the signal becomes weak and may drop out. Repeaters can also broadcast their received signal over the internet through applications such as EchoLink, which allows the transmissions to reach across the globe.

<!-- b000094 | prose | pages [6] -->
As listed on the National Association for Amateur Radio’s website, the band plan for 144-148MHz speciﬁes the following table1:

<!-- b000095 | prose | pages [6] -->
Frequency (MHz) Allocated 146.01-146.37 Repeater inputs Simplex† 146.40-146.58

<!-- b000096 | prose | pages [6] -->
146.52 National Simplex Calling Frequency 146.61-146.97 Repeater outputs 147.00-147.39 Repeater outputs 147.42-147.57 Simplex 147.60-147.99 Repeater inputs

<!-- b000097 | prose | pages [6] -->
UK Repeater Frequencies

<!-- b000098 | prose | pages [6] -->
As an example of actual repeater frequencies, we look at

<!-- b000099 | prose | pages [6] -->
Channel Output #

<!-- b000100 | prose | pages [6] -->
those in the UK.

<!-- b000101 | prose | pages [6] -->
RV48 145.6000 10

<!-- b000102 | prose | pages [6] -->
The UK Amateur Radio Repeater Resource website

<!-- b000103 | prose | pages [6] -->
RV49 145.6125 5

<!-- b000104 | prose | pages [6] -->
lists all of the “existing and licensed analogue and dual-

<!-- b000105 | prose | pages [6] -->
RV50 145.6250 10

<!-- b000106 | prose | pages [6] -->
mode 145MHz amateur repeaters” in the UK. Of the 127

<!-- b000107 | prose | pages [6] -->
RV51 145.6375 4

<!-- b000108 | prose | pages [6] -->
operational repeaters listed, there are only 15 distinct fre-

<!-- b000109 | prose | pages [6] -->
RV52 145.6500 8

<!-- b000110 | prose | pages [6] -->
quencies used. For a given frequency, the regions reached

<!-- b000111 | prose | pages [6] -->
RV53 145.6625 8

<!-- b000112 | prose | pages [6] -->
by the repeaters do not overlap and some repeaters may

<!-- b000113 | prose | pages [6] -->
RV54 145.6750 7

<!-- b000114 | prose | pages [6] -->
even have the same PL code; however, these regions are a

<!-- b000115 | prose | pages [6] -->
RV55 145.6875 7

<!-- b000116 | prose | pages [6] -->
signiﬁcant distance apart (∼200 miles). Furthermore, the

<!-- b000117 | prose | pages [6] -->
RV56 145.7000 10

<!-- b000118 | prose | pages [6] -->
frequencies used for repeaters are in a contiguous band.

<!-- b000119 | prose | pages [6] -->
RV57 145.7125 6

<!-- b000120 | prose | pages [6] -->
[Note that for context, the UK is 94,060 square miles,

<!-- b000121 | prose | pages [6] -->
RV58 145.7250 11

<!-- b000122 | prose | pages [6] -->
whereas our region is approximately 5,027 square miles.]

<!-- b000123 | prose | pages [6] -->
RV59 145.7375 6 RV60 145.7500 9 RV61 145.7625 5 RV62 145.7750 13 RV63 145.7875 8

<!-- b000124 | caption | pages [6] -->
Figure 1: The number of repeaters

<!-- b000125 | prose | pages [6] -->
which output at given frequencies in the UK.[10]

<!-- b000126 | prose | pages [6] -->
1Note that we only show frequencies 146.01-147.99 and that, previous to this, there are blocks of other miscellaneous standards.

<!-- b000127 | prose | pages [7] -->
Control # 12114 7

<!-- b000128 | prose | pages [7] -->
2 Problem Interpretation

<!-- b000129 | prose | pages [7] -->
Given a population of users within a circular region of radius 40 miles, we attempt to minimally and adequately place repeaters to assist with communication via VHF transmit- ters. Because VHF frequencies can be in high demand, we also minimize the number of frequencies used by our repeaters and analyze the beneﬁt of using PL codes. We look at the cases where there are 1, 000 and 10, 000 simultaneous users with two types of population distributions: uniformly random and preferentially attached. The preferential distribution simulates the tendency of users to be found in clusters. In this way, we look at diﬀerent types of regions which encapsulates sparse rural regions, towns, suburbs, and cities.

<!-- b000130 | prose | pages [7] -->
Because signals travel primarily by line-of-sight, we also analyze optimal placement of the repeaters when mountains are present in the given terrain and the eﬀect this has on the number of the repeaters. Further, we discuss the eﬀects of various attenuation factors on the signal.

<!-- b000131 | prose | pages [7] -->
3

<!-- b000132 | heading | pages [7] -->
Assumptions

<!-- b000133 | prose | pages [7] -->
There are three instances possible for when we would need to lay repeaters:

<!-- b000134 | prose | pages [7] -->
1. People reside within the region and no repeaters exist.

<!-- b000135 | prose | pages [7] -->
2. People reside within the region and inadequate repeaters exist.

<!-- b000136 | prose | pages [7] -->
3. The distributions of people and repeaters are unknown or not present.

<!-- b000137 | prose | pages [7] -->
In the third case, in order to adequately and minimally cover all of the simultaneous users, we must cover the entire region. See Circle Covering (Section 4) for repeater placement.

<!-- b000138 | prose | pages [7] -->
In the following analysis, we assume the ﬁrst case, which could also easily be extended to the second case with our model by laying down a framework of already-existing repeaters and checking which users are already covered.

<!-- b000139 | prose | pages [7] -->
Repeaters

<!-- b000140 | prose | pages [7] -->
Usually repeaters are placed on high buildings to maximize their coverage; however, with a strong repeater and a reasonably tall building, this range could easily be more than 40 miles. If we used such repeaters, the minimal repeater placement would be directly in the center of the region.

<!-- b000141 | prose | pages [7] -->
To avoid looking at such a trivial case, we assume an antenna height of 18 feet and consider the range within 10 miles of the repeater, a range which does not impede on the “fringe” area and hence allows us to assume that all people within this circle are adequately

<!-- b000142 | prose | pages [8] -->
Control # 12114 8

<!-- b000143 | prose | pages [8] -->
covered. We discard the “fringe” range as unsatisfactory because is unreliable and signals may drop. Though the 18 feet and 10 mile range are for the most part arbitrary, any smaller of a range would be unrealistically small and any larger converges to the trivial case.

<!-- b000144 | prose | pages [8] -->
We also assume that any person within the range speciﬁed of the repeater can commu- nicate with any other user who is within range of a, possibly distinct, repeater through an application such as EchoLink.

<!-- b000145 | prose | pages [8] -->
Also, we assume that repeaters fail independently.

<!-- b000146 | prose | pages [8] -->
Discretized Space

<!-- b000147 | prose | pages [8] -->
For ease of modeling, we assume a grid on which we place people, repeaters, and do calculations. We generally use a ﬁneness of 1/4 mile for this grid. We also ensure that the people, repeaters, and calculations are within the circle centered at the center of the grid.

<!-- b000148 | prose | pages [8] -->
When placing repeaters, we assume that the circular coverage never escapes the sur- rounding grid boundary.

<!-- b000149 | prose | pages [8] -->
Usage Patterns

<!-- b000150 | prose | pages [8] -->
We assume that one circle covering any number of people is suﬃcient coverage. We address this issue further with utility (Section 6.2).

<!-- b000151 | prose | pages [8] -->
Obstructions

<!-- b000152 | prose | pages [8] -->
In our basic model, we assume that reﬂections, diﬀraction, and obstacles such as buildings have a neglectably small eﬀect on the range of the repeater, which generally holds true in practice. We do discuss obstructions such as forests and consider the eﬀect that mountains have on the line-of-sight, including the eﬀects of diﬀraction (Sections 4.1, 7.2).

<!-- b000153 | prose | pages [8] -->
Interference

<!-- b000154 | prose | pages [8] -->
Interference can occur if two repeaters with the same frequency have overlapping coverages, even if their PL codes diﬀer. We keep this as an assumption in our model and choose frequencies such that they are more than 25 miles apart and are not adjacent. Because we want to minimize the number of frequencies used, as mentioned in Section 2, we also attempt to reuse frequencies in our model and to keep these frequencies in a block as in

<!-- b000155 | caption | pages [8] -->
Figure 1. Also, we assume that given a suﬃciently small number of frequencies required,

<!-- b000156 | prose | pages [8] -->
it is trivial to assign the channels frequencies without collision due to the 600kHz shifting of input and output of repeaters.

<!-- b000157 | prose | pages [9] -->
Control # 12114 9

<!-- b000158 | prose | pages [9] -->
4 Circle Covering

<!-- b000159 | prose | pages [9] -->
One method of ensuring all users have coverage is to cover the entire region. We ﬁrst look analytically at how to minimally cover the entire region with repeaters.

<!-- b000160 | prose | pages [9] -->
Let us assume that each repeater has a circular range with radius 10. Here we analyze the number of repeaters, n, needed to cover the region of radius 40.

<!-- b000161 | prose | pages [9] -->
Simple lower bound

<!-- b000162 | prose | pages [9] -->
We ﬁrst ﬁnd a lower bound on the number of repeaters needed to achieve a full covering. Using the fact that a circle with radius r has area πr2, we note that the region to cover has area

<!-- b000163 | prose | pages [9] -->
Aregion = π(40)2 = 1600π

<!-- b000164 | prose | pages [9] -->
and each repeater has a coverage of area

<!-- b000165 | prose | pages [9] -->
Arepeater = π(10)2 = 100π.

<!-- b000166 | prose | pages [9] -->
Because Aregion

<!-- b000167 | prose | pages [9] -->
= 16,

<!-- b000168 | prose | pages [9] -->
Arepeater

<!-- b000169 | prose | pages [9] -->
we see that the area covered by 16 repeaters is equivalent to the area we intend to cover. This does not, however, imply that we only

<!-- b000170 | caption | pages [9] -->
Figure 2: Circles of radii 40 and 10.

<!-- b000171 | prose | pages [9] -->
need 16 repeaters, because placing the circles would require overlap of their coverages. Hence, we ﬁnd for a lower bound

<!-- b000172 | prose | pages [9] -->
16 ≤n.

<!-- b000173 | prose | pages [9] -->
Hexagonal approximation upper bound

<!-- b000174 | prose | pages [9] -->
To get an upper bound on the number of repeaters needed, we look to hexagonal packing. The problem we are solving is easily relatable to the Disk Covering Problem, where one ﬁnds the smallest radius r for which n disks of radius r can cover the unit disk. This is an unsolved, NP-complete problem with analytic answers for small n and approximations up to n = 10 [5]; however, we are looking at n ≥16. Our problem is also relatable to the Circle Packing Problem, where circles are packed into a region without overlap. Using a circle packing of a smaller radius than that of the repeater coverage, we can ﬁnd a circle packing and then expand the radius to obtain overlapping circles which applies to our problem. On the euclidean plane, hexagonal packing provides the optimal lattice solution for circle packing [6]; however, when the boundary is ﬁnite, this is not usually the case. Because our problem remains unsolved, we look to hexagonal packing for an approximation by placing a hexagonal lattice of smaller circles and extending their boundaries.

<!-- b000175 | prose | pages [10] -->
Control # 12114 10

<!-- b000176 | prose | pages [10] -->
Because we can ﬁnd a hexagonal scheme which uses 21 circles of radius 10 to cover our region of radius 40 (Figure 3), we know that at most we will need 21 repeaters. Hence, our new bounds on n are

<!-- b000177 | prose | pages [10] -->
16 ≤n ≤21.

<!-- b000178 | prose | pages [10] -->
=⇒

<!-- b000179 | prose | pages [10] -->
√

<!-- b000180 | prose | pages [10] -->
Hexagonal lattice covering with circle radii 10.

<!-- b000181 | prose | pages [10] -->
Hexagonal lattice packing with circle radii 5

<!-- b000182 | prose | pages [10] -->
3.

<!-- b000183 | caption | pages [10] -->
Figure 3: Upper bound of 21 derived from hexagonal packing.

<!-- b000184 | prose | pages [10] -->
Thus, optimally we can hope to obtain results from our model which require at least 16 and at most 21 repeaters.

<!-- b000185 | prose | pages [11] -->
Control # 12114 11

<!-- b000186 | prose | pages [11] -->
4.1 Radio Wave Propogation

<!-- b000187 | prose | pages [11] -->
In free space, the power denisty of all electromagnetic radiation follows the inverse square 1 law ρ ∝ r2, so that a doubling of distance results in one-fourth the power density. However propogation of radio waves near the surface of the earth can be signiﬁcantly more compli- cated than this. Lower frequency radio waves often propogate by sticking to the surface of the earth, while higher frequency radio waves need a direct line of sight, and radio waves of certain middle range frequencies can propogate by refraction through the atmosphere. We are considering only VHF radio waves which propogate mostly by direct line of sight, however other factors such as refraction, reﬂection, and diﬀraction have an eﬀect.

<!-- b000188 | prose | pages [11] -->
Refraction

<!-- b000189 | prose | pages [11] -->
Radio waves in the HF range can travel very great distances through a process called sky- wave propogation. In this process, waves are bent downard by refraction in the ionosphere, as if they were reﬂected oﬀa mirror. When the waves reach the earth, they may reﬂect upwards again. This process may occur several times, allowing the wave to travel accross continents. While refraction of VHF waves is not strong enough to induce skywave pro- pogation, it still slightly bends the path of the waves back towards the earth. The result is that the waves are able to propogate farther than if they were traveling in a straight line. Without the refractive eﬀect, VHF waves would only be able to travel as far as the visible horizon before being absorbed into the Earth. However, this bending allows the waves to propogate beyond the visible horizon to something often called the Radio Horizon. The

<!-- b000190 | prose | pages [11] -->
√

<!-- b000191 | prose | pages [11] -->
distance in miles to the Radio Horizon is approximately

<!-- b000192 | prose | pages [11] -->
2A where A is the antenna hight in feet [3].

<!-- b000193 | caption | pages [11] -->
Figure 4: Signal range extends due to tropospheric interference.

<!-- b000194 | prose | pages [11] -->
Reﬂection

<!-- b000195 | prose | pages [11] -->
Ground plane reﬂections creat a second path for radio wave. When this wave recombines with the direct line of sight wave, there can be either constructive or deconstructive inter- ference. However, ordinarily the ground plane reﬂection reduce the strength of the signal considerably, eﬀectively changing the power density relationship to an inverse fourth law 1 ρ ∝ r4 rather than the inverse square law [3].

<!-- b000196 | prose | pages [12] -->
Control # 12114 12

<!-- b000197 | caption | pages [12] -->
Figure 5: Reﬂections of the signal can interfere or strengthen the direct wave.

<!-- b000198 | prose | pages [12] -->
Diﬀraction

<!-- b000199 | prose | pages [12] -->
When VHF radio waves encounter large obstacles such a mountains, the wave is generally absorbed or reﬂected by the object. However in some cases, if the radio wave propogates near the top of the object, diﬀraction can redirect the wave towards the target. In this way the two radios can communicate even when their line of sight is blocked, however the signal strength is reduced by the diﬀraction process. In other cases, when the path goes directly above an object, diﬀraction can attenuate the signal even though there was a direct line of sight between te two antennas. In particular, obstructions inside the fresnel zone contribute to interference by diﬀraction.

<!-- b000200 | caption | pages [12] -->
Figure 6: Diﬀraction over surfaces can cause indirect paths to connect antennas.

<!-- b000201 | prose | pages [12] -->
5 Population Distribution

<!-- b000202 | prose | pages [12] -->
In order to acquire test data on which to execute our model, we need to generate population distributions to recreate user distribution scenarios similar to those that could be expected in real life. We consider two diﬀerent algorithms to generate reasonable distributions within a circle with a 40-mile radius.

<!-- b000203 | prose | pages [12] -->
5.1

<!-- b000204 | heading | pages [12] -->
Uniform Algorithm

<!-- b000205 | prose | pages [12] -->
For each inhabitant, the uniform algorithm na¨ıvely selects a point within the circle uni- formly at random as their place of residence. This covers the circle reasonably evenly, without yielding the unnatural regularity attained by placing the points with equal spac- ing. As we will see in Section 7, this distribution is oftentimes the hardest to deal with as there are few patterns or clusters to be taken advantage of.

<!-- b000206 | prose | pages [13] -->
Control # 12114

<!-- b000207 | prose | pages [13] -->
40

<!-- b000208 | prose | pages [13] -->
30

<!-- b000209 | prose | pages [13] -->
20

<!-- b000210 | prose | pages [13] -->
10

<!-- b000211 | prose | pages [13] -->
0

<!-- b000212 | prose | pages [13] -->
-10

<!-- b000213 | prose | pages [13] -->
-20

<!-- b000214 | prose | pages [13] -->
-30

<!-- b000215 | prose | pages [13] -->
-40 -40 -30 -20 -10 0 10 20 30 40

<!-- b000216 | prose | pages [13] -->
(a) Uniform

<!-- b000217 | prose | pages [13] -->
13

<!-- b000218 | prose | pages [13] -->
40

<!-- b000219 | prose | pages [13] -->
30

<!-- b000220 | prose | pages [13] -->
20

<!-- b000221 | prose | pages [13] -->
10

<!-- b000222 | prose | pages [13] -->
0

<!-- b000223 | prose | pages [13] -->
-10

<!-- b000224 | prose | pages [13] -->
-20

<!-- b000225 | prose | pages [13] -->
-30

<!-- b000226 | prose | pages [13] -->
-40 -40 -30 -20 -10 0 10 20 30 40

<!-- b000227 | prose | pages [13] -->
(b) Preferential

<!-- b000228 | caption | pages [13] -->
Figure 7: The two types of considered user distributions with 1000 users.

<!-- b000229 | heading | pages [13] -->
Preferential Attachment Algorithm

<!-- b000230 | prose | pages [13] -->
5.2

<!-- b000231 | prose | pages [13] -->
An alternative algorithm, based on the model of the preferential attachment suggested by Barab´asi and Albert [1], distributes the users in a slightly more organized way. Initially, some small number of users are distributed uniformly at random throughout the region to act as a seed for the algorithm. Afterwards, new users either select a location uniformly at random with some small ﬁxed probability or select an existing user uniformly at random and located themselves within a small distance of that user.

<!-- b000232 | prose | pages [13] -->
This method ends up forming a population distribution approximating a preferrential attachment network, with clusters of users beneﬁting from the rich-get-richer eﬀect in bringing in additional users. This is a highly desirable quality for our model, as population distributions tend to roughly follow the scale-free design formed by preferential attachment [7].

<!-- b000233 | prose | pages [13] -->
For clarity, pseudocode for this algorithm is given in Program 1.

<!-- b000234 | prose | pages [13] -->
6 Our Approach

<!-- b000235 | prose | pages [13] -->
Here we begin discussing the core of our model and algorithms.

<!-- b000236 | prose | pages [13] -->
6.1 Basic Coverage

<!-- b000237 | prose | pages [13] -->
Two similar goals can be sought in trying to attain basic coverage. We would like to be able to both:

<!-- b000238 | prose | pages [14] -->
Control # 12114 14

<!-- b000239 | heading | pages [14] -->
Program 1 Preferrential Attachment Algorithm

<!-- b000240 | prose | pages [14] -->
1 init users is the number of initial users distributed uniformly at random 1 total users is the number of total users 1 r is the maximum radius between two “attached” users 1 connect chance is the chance of a new user being attached to a random vertex 1 greedy color refers to the common greedy coloring algorithm 1

<!-- b000241 | heading | pages [14] -->
1 Function preferential attachment

<!-- b000242 | prose | pages [14] -->
1

<!-- b000243 | heading | pages [14] -->
1 Let pop be an empty list of users

<!-- b000244 | prose | pages [14] -->
1 1 /*Place the initial set of users*/

<!-- b000245 | heading | pages [14] -->
1 loop init users times:

<!-- b000246 | prose | pages [14] -->
1 1 append to pop a user located uniformly at random in the region of interest 1 1 /*Obtain a coloring of the generated graph*/ 1 coloring = greedy color(G) 1 1 For each vertex v in G: 1 1 freqmap[v] = frequency set[coloring[v]] 1

<!-- b000247 | heading | pages [14] -->
1 return freqmap

<!-- b000248 | prose | pages [15] -->
Control # 12114 15

<!-- b000249 | prose | pages [15] -->
1. Minimize the number of repeaters necessary to cover some fraction p of the population.

<!-- b000250 | prose | pages [15] -->
2. Maximize the number of people covered by some ﬁxed number, n, of repeaters.

<!-- b000251 | prose | pages [15] -->
Since the decision problems corresponding to the above two goals are both known to be NP-hard [11], we employ a greedy algorithm to try approximating the solution by repeatedly taking the locally-optimal move (that is, repeatedly covering users with maximally-covering circles). This greedy approach was shown to be a 2−approximation of the optimal solution in a more general setting, but has been demonstrated to approximate the optimal solution rather well in simulations [11]. Interestingly, the monotonic reasoning of the greedy algorithm allows us to simultaneously calculate our success at attaining the two goals mentioned above: while greedily computing the number of repeaters needed to cover a certain fraction of the population, we can record the total coverage at each intermediate step in order to compute the eﬀectiveness of greedily placing n repeaters.

<!-- b000252 | prose | pages [15] -->
Because this method is a speciﬁc case of the utility method introduced in Section 6.2, we delay the introduction of pseudocode for the time-being. More thorough analysis of the code’s design and implications will be presented with the pseudocode.

<!-- b000253 | prose | pages [15] -->
6.1.1 Algorithmic Runtime

<!-- b000254 | prose | pages [15] -->
Letting k denote the maximum number of circles of radius r needed to cover the 40-mile- radius circle, the 2-approximation factor discussed in the previous section implies that the greedy algorithm will terminate within at most 2k iterations. To ﬁnd the optimal circle in each iteration, the body of the loop iterates over O(s2) grid points (for s representing the ﬁneness of the grid), each of which requires O((rs)2) calculations, leading to an overall runtime of O(r2s4). Because k is O(r−2), the overall runtime of this algorithm is

<!-- b000255 | prose | pages [15] -->
O(r−2r2s4) = O(s4),

<!-- b000256 | prose | pages [15] -->
or quartic in the ﬁneness of the grid.

<!-- b000257 | prose | pages [15] -->
6.2 Additional Layers: Maximizing Utility

<!-- b000258 | prose | pages [15] -->
Although the algorithm described in Section 6.1 can successfully cover any given percentage of users, it often employs a number of repeaters which cover only a relatively small fraction of the population. Instead, a better use of these repeaters might be in the establishment of secondary, backup networks from which the high-population districts can beneﬁt.

<!-- b000259 | prose | pages [15] -->
The reasoning is as follows: if an average repeater is malfunctioning with some fraction p of the time, the expected loss of utility (ignoring regions of overlap) is pn, where n is the number of people covered by the repeater’s signal. Thus, placing a repeater to get rid of most of this downtime in a high-population region might be more beneﬁcial than putting

<!-- b000260 | prose | pages [16] -->
Control # 12114 16

<!-- b000261 | prose | pages [16] -->
one somewhere that covers a small number of users. If we assume that the probabilities of each of two repeaters experiencing faults are independent, the probability of all repeaters in an area covered by q repeaters being down simultaneously is npq. Alternatively, we can treat the ﬁrst repeater covering a speciﬁc individual as having p utility, the next having p2

<!-- b000262 | prose | pages [16] -->
utility, and so on, forming a geometric series that converges to 1/(1 −p) as the supremum of attainable utilities. As this value forms a multiplicative constant for any chosen set of parameters, the fact that the maximum attainable utility per person is more than 1 does not aﬀect the calculation of the placement of repeaters in any scale-independent covering algorithm, including the greedy algorithm we employ.

<!-- b000263 | prose | pages [16] -->
To clarify the workings of our algorithm, we present pseudocode describing its pre- optimization behavior in Program 2.

<!-- b000264 | prose | pages [16] -->
6.2.1 Basic Coverage as a Special Case

<!-- b000265 | prose | pages [16] -->
In addition to maximizing the total utility of the covering, the above pseudocode can actually be used to satisfy the two goals mentioned in Section 6.1. To do this, one simply needs to set u to 0, reducing the utility-maximization problem to coverage maximization, which in turn solves both tasks outlined in Section 6.1. This minimizes the amount of code reuse needed, and simpliﬁes making later changes to the model.

<!-- b000266 | prose | pages [16] -->
6.2.2 Runtime Analysis and Optimizations

<!-- b000267 | prose | pages [16] -->
As the overall structure of the main loop’s body has not changed signiﬁcantly since previous runtime analysis, the runtime of each iteration is again O(r2s4). The number of iterations, however, is now also dependent on the rate of convergence of the utility to the desired amount, namely,

<!-- b000268 | prose | pages [16] -->
k ∼logu (1 −W)

<!-- b000269 | prose | pages [16] -->
r2

<!-- b000270 | prose | pages [16] -->
meaning that the runtime of the algorithm as a whole is

<!-- b000271 | prose | pages [16] -->
s4 logu(1 −W)

<!-- b000272 | prose | pages [16] -->
 

<!-- b000273 | prose | pages [16] -->


<!-- b000274 | prose | pages [16] -->
O

<!-- b000275 | prose | pages [16] -->
whenever u > 0 and O(s4) otherwise.

<!-- b000276 | prose | pages [16] -->
In order to successfully deal with this approximately-quartic runtime, various optimiza- tions had to be made.

<!-- b000277 | prose | pages [16] -->
Firstly, instead of recalculating the populations of the various repeater regions of eﬀect in each iteration, we can precompute each of these populations beforehand. This can be done eﬃciently (in O(rn2) time) using standard dynamic pro- gramming approaches. With these precomputed values and a maintained sorted list of circle populations, we can reduce the O(r2s4) portion of the algorithm to O(rs2 log(rs)) average-case runtime, drastically reducing the number of computations necessary. Further, although not implemented in our model, the search portion of this step can be sped up

<!-- b000278 | prose | pages [17] -->
Control # 12114 17

<!-- b000279 | prose | pages [17] -->
Program 2 Utility-Based Greedy Cover

<!-- b000280 | prose | pages [17] -->
1 r is the eﬀective radius of a repeater’s signal 1 u is the expected proportion of downtime of the repeaters 1 W is the utility ratio at which the program is to stop

<!-- b000281 | prose | pages [17] -->
1

<!-- b000282 | heading | pages [17] -->
1 Function utility based greedy cover

<!-- b000283 | prose | pages [17] -->
1 covering = empty list 1 current utility = 0 1 1 /*Precompute maximum possible utility using inﬁnite geometric series formula*/ 1 max utility = population/(1-u) 1

<!-- b000284 | heading | pages [17] -->
1 set the utility of all users to 1

<!-- b000285 | heading | pages [17] -->
1 loop until broken:

<!-- b000286 | prose | pages [17] -->
1 1 let greedy value = -1, best point = (0, 0) 1 1 for each grid point p: 1 1 1 compute total utility u of all users within r miles of p 1 1 1 if u > greedy value: 1 1 1 1 best point = p 1 1 1 1 greedy value = u 1 1 1

<!-- b000287 | heading | pages [17] -->
/*Store result*/

<!-- b000288 | prose | pages [17] -->
1 1 append best point to covering 1

<!-- b000289 | heading | pages [17] -->
1 for each user x within r miles of best point:

<!-- b000290 | prose | pages [17] -->
1 1 current utility += x.utility 1 1 x.utility *= u 1 1 1 /*Check stopping condition*/ 1 1 if current utility/max utility < W : 1 1 1 break 1

<!-- b000291 | heading | pages [17] -->
1 return covering

<!-- b000292 | prose | pages [18] -->
Control # 12114 18

<!-- b000293 | prose | pages [18] -->
further by parallelizing the search over multiple cores, reducing the total runtime by a small amount.

<!-- b000294 | prose | pages [18] -->
6.2.3 Additional Notes

<!-- b000295 | prose | pages [18] -->
This algorithm can also handle instances in which the search area surrounding the vari- ous potential repeaters is non-circular, although the various sequential optimizations (i.e. all those besides the parallelization) noted in 6.2.2 are eliminated, and the tight runtime is much more diﬃcult to calculate (though it can easily be shown to be no worse than O(s4 max(a)

<!-- b000296 | prose | pages [18] -->
min(a) ) where a is the array of areas of the various regions covered by diﬀerent loca- tions).

<!-- b000297 | prose | pages [18] -->
6.3 Frequency Selection

<!-- b000298 | prose | pages [18] -->
To assign frequencies to the various repeaters, we form a graph whose vertices represent the repeaters and whose edges represent locality between the two repeaters at its endpoints. After this graph is created, a reasonable vertex coloring is found (greedily or otherwise), with the diﬀerent colors representing distinct frequencies of the repeaters. Pseudocode for this idea is given in Program 3. Note that because our model allows for only a small number of frequencies, we assume that assigning these colors to frequencies is trivial and so do not assign speciﬁc numbers.

<!-- b000299 | prose | pages [18] -->
Note that although we can simply deﬁne two repeaters to be adjacent if there’s overlap in the regions covered by the pair, our current algorithm maintains an extra half-radius separating the regions to ensure minimal interference.

<!-- b000300 | prose | pages [18] -->
7

<!-- b000301 | heading | pages [18] -->
Results

<!-- b000302 | prose | pages [18] -->
This section will discuss the results from our model. We will look at the results from the basic model with both uniform and preferential distributions. This includes looking at both potential populations of users, and will look at coverage and utility. In each of the plots, each distinct frequency is a distinct color.

<!-- b000303 | prose | pages [18] -->
7.1

<!-- b000304 | heading | pages [18] -->
Basic Model

<!-- b000305 | prose | pages [18] -->
Covering

<!-- b000306 | prose | pages [18] -->
Using the Greedy Covering Algorithm, described in Program 2, we not only look at the minimum number of circles needed to cover all users but also what happens if a smaller

<!-- b000307 | prose | pages [19] -->
Control # 12114

<!-- b000308 | heading | pages [19] -->
Program 3 Frequency Allocation Algorithm

<!-- b000309 | prose | pages [19] -->
19

<!-- b000310 | prose | pages [19] -->
1 repeater list is the list containing the locations of repeaters 1 r is the eﬀective radius of a repeater’s signal 1 frequency set is a list of allowable, non-overlapping frequencies

<!-- b000311 | prose | pages [19] -->
1

<!-- b000312 | heading | pages [19] -->
1 Function greedy frequency allocator

<!-- b000313 | prose | pages [19] -->
1

<!-- b000314 | heading | pages [19] -->
1 Let G be an edgeless undirected graph with one vertex per repeater in repeater list

<!-- b000315 | heading | pages [19] -->
1 Let freqmap be a mapping from repeaters into frequencies

<!-- b000316 | prose | pages [19] -->
1

<!-- b000317 | heading | pages [19] -->
1 for each repeater pair (i, j) with i̸ = j:

<!-- b000318 | prose | pages [19] -->
if dist(i, j) ≤5 1 1

<!-- b000319 | prose | pages [19] -->
2r: Add an edge in G connecting the vertices representing i and j 1 1 1 1 1 /*Obtain a coloring of G, represented as a vertex →integer map*/ 1 coloring = greedy color(G) 1 1 For each vertex v in G:

<!-- b000320 | prose | pages [19] -->
freqmap[v] = frequency set[coloring[v]] 1 1 1

<!-- b000321 | heading | pages [19] -->
1 return freqmap

<!-- b000322 | prose | pages [19] -->
40

<!-- b000323 | prose | pages [19] -->
40

<!-- b000324 | prose | pages [19] -->
30

<!-- b000325 | prose | pages [19] -->
30

<!-- b000326 | prose | pages [19] -->
20

<!-- b000327 | prose | pages [19] -->
20

<!-- b000328 | prose | pages [19] -->
10

<!-- b000329 | prose | pages [19] -->
10

<!-- b000330 | prose | pages [19] -->
0

<!-- b000331 | prose | pages [19] -->
0

<!-- b000332 | prose | pages [19] -->
-10

<!-- b000333 | prose | pages [19] -->
-10

<!-- b000334 | prose | pages [19] -->
-20

<!-- b000335 | prose | pages [19] -->
-20

<!-- b000336 | prose | pages [19] -->
-30

<!-- b000337 | prose | pages [19] -->
-30

<!-- b000338 | prose | pages [19] -->
-40

<!-- b000339 | prose | pages [19] -->
-40

<!-- b000340 | prose | pages [19] -->
-40 -30 -20 -10 0 10 20 30 40

<!-- b000341 | prose | pages [19] -->
-40 -30 -20 -10

<!-- b000342 | prose | pages [19] -->
40

<!-- b000343 | prose | pages [19] -->
30

<!-- b000344 | prose | pages [19] -->
20

<!-- b000345 | prose | pages [19] -->
10

<!-- b000346 | prose | pages [19] -->
0

<!-- b000347 | prose | pages [19] -->
-10

<!-- b000348 | prose | pages [19] -->
-20

<!-- b000349 | prose | pages [19] -->
-30

<!-- b000350 | prose | pages [19] -->
-40

<!-- b000351 | prose | pages [19] -->
0 0 10 20 30 40

<!-- b000352 | prose | pages [19] -->
-40 -30 -20 -10 0 10 20 30 40

<!-- b000353 | prose | pages [19] -->
(b) 92% Coverage, 5 Colors, 15

<!-- b000354 | prose | pages [19] -->
(a) 80% Coverage, 3 Colors, 11 Circles

<!-- b000355 | prose | pages [19] -->
Circles

<!-- b000356 | prose | pages [19] -->
(c) 100% Coverage, 8 Colors, 28 Circles

<!-- b000357 | caption | pages [19] -->
Figure 8: Uniform distribution of 1000 users with 80%, 92%, and 100% coverage. The number of

<!-- b000358 | prose | pages [19] -->
colors corresponds to the number of frequencies used.

<!-- b000359 | prose | pages [20] -->
Control # 12114

<!-- b000360 | prose | pages [20] -->
40

<!-- b000361 | prose | pages [20] -->
40

<!-- b000362 | prose | pages [20] -->
30

<!-- b000363 | prose | pages [20] -->
30

<!-- b000364 | prose | pages [20] -->
20

<!-- b000365 | prose | pages [20] -->
20

<!-- b000366 | prose | pages [20] -->
10

<!-- b000367 | prose | pages [20] -->
10

<!-- b000368 | prose | pages [20] -->
0

<!-- b000369 | prose | pages [20] -->
0

<!-- b000370 | prose | pages [20] -->
-10

<!-- b000371 | prose | pages [20] -->
-10

<!-- b000372 | prose | pages [20] -->
-20

<!-- b000373 | prose | pages [20] -->
-20

<!-- b000374 | prose | pages [20] -->
-30

<!-- b000375 | prose | pages [20] -->
-30

<!-- b000376 | prose | pages [20] -->
-40

<!-- b000377 | prose | pages [20] -->
-40

<!-- b000378 | prose | pages [20] -->
-40 -30 -20 -10 0 10 20 30 40

<!-- b000379 | prose | pages [20] -->
-40 -30 -20 -10

<!-- b000380 | prose | pages [20] -->
20

<!-- b000381 | prose | pages [20] -->
40

<!-- b000382 | prose | pages [20] -->
30

<!-- b000383 | prose | pages [20] -->
20

<!-- b000384 | prose | pages [20] -->
10

<!-- b000385 | prose | pages [20] -->
0

<!-- b000386 | prose | pages [20] -->
-10

<!-- b000387 | prose | pages [20] -->
-20

<!-- b000388 | prose | pages [20] -->
-30

<!-- b000389 | prose | pages [20] -->
-40

<!-- b000390 | prose | pages [20] -->
0 0 10 20 30 40

<!-- b000391 | prose | pages [20] -->
-40 -30 -20 -10 0 10 20 30 40

<!-- b000392 | prose | pages [20] -->
(b) 92% Coverage, 6 Colors, 18

<!-- b000393 | prose | pages [20] -->
(a) 80% Coverage, 4 Colors, 12 Circles

<!-- b000394 | prose | pages [20] -->
Circles

<!-- b000395 | prose | pages [20] -->
(c) 100% Coverage, 10 Colors, 35 Circles

<!-- b000396 | caption | pages [20] -->
Figure 9: Uniform distribution of 10,000 users with 80%, 92%, and 100% coverage.

<!-- b000397 | prose | pages [20] -->
40

<!-- b000398 | prose | pages [20] -->
40

<!-- b000399 | prose | pages [20] -->
30

<!-- b000400 | prose | pages [20] -->
30

<!-- b000401 | prose | pages [20] -->
20

<!-- b000402 | prose | pages [20] -->
20

<!-- b000403 | prose | pages [20] -->
10

<!-- b000404 | prose | pages [20] -->
10

<!-- b000405 | prose | pages [20] -->
0

<!-- b000406 | prose | pages [20] -->
0

<!-- b000407 | prose | pages [20] -->
-10

<!-- b000408 | prose | pages [20] -->
-10

<!-- b000409 | prose | pages [20] -->
-20

<!-- b000410 | prose | pages [20] -->
-20

<!-- b000411 | prose | pages [20] -->
-30

<!-- b000412 | prose | pages [20] -->
-30

<!-- b000413 | prose | pages [20] -->
-40

<!-- b000414 | prose | pages [20] -->
-40

<!-- b000415 | prose | pages [20] -->
-40 -30 -20 -10 0 10 20 30 40

<!-- b000416 | prose | pages [20] -->
-40 -30 -20 -10

<!-- b000417 | prose | pages [20] -->
40

<!-- b000418 | prose | pages [20] -->
30

<!-- b000419 | prose | pages [20] -->
20

<!-- b000420 | prose | pages [20] -->
10

<!-- b000421 | prose | pages [20] -->
0

<!-- b000422 | prose | pages [20] -->
-10

<!-- b000423 | prose | pages [20] -->
-20

<!-- b000424 | prose | pages [20] -->
-30

<!-- b000425 | prose | pages [20] -->
-40

<!-- b000426 | prose | pages [20] -->
0 0 10 20 30 40

<!-- b000427 | prose | pages [20] -->
-40 -30 -20 -10 0 10 20 30 40

<!-- b000428 | prose | pages [20] -->
(b) 92% Coverage, 4 Colors, 10

<!-- b000429 | prose | pages [20] -->
(a) 80% Coverage, 3 Colors, 6 Circles

<!-- b000430 | prose | pages [20] -->
Circles

<!-- b000431 | prose | pages [20] -->
(c) 100% Coverage, 6 Colors, 21 Circles

<!-- b000432 | caption | pages [20] -->
Figure 11: Preferential distribution of 1000 users with 80%, 92%, and 100% coverage.

<!-- b000433 | prose | pages [20] -->
percentage of users are required to be covered.

<!-- b000434 | prose | pages [20] -->
For instance, if only 90% of users are required to be covered the number of repeaters required may be much smaller. This acts as a sensitivity analysis as well as oﬀering insight into the algorithm used.

<!-- b000435 | prose | pages [20] -->
40

<!-- b000436 | prose | pages [20] -->
The ﬁrst case we look at is that in Figure 8, which

<!-- b000437 | prose | pages [20] -->
30

<!-- b000438 | prose | pages [20] -->
uses a uniform distribution for the population spread. We

<!-- b000439 | prose | pages [20] -->
20

<!-- b000440 | prose | pages [20] -->
see that for 80% coverage of the users, only 11 repeaters

<!-- b000441 | prose | pages [20] -->
10

<!-- b000442 | prose | pages [20] -->
are required. Again, for only 92% of users to be covered,

<!-- b000443 | prose | pages [20] -->
0

<!-- b000444 | prose | pages [20] -->
only 15 are required; however, the last 8% require 13 extra

<!-- b000445 | prose | pages [20] -->
-10

<!-- b000446 | prose | pages [20] -->
repeaters, pushing the number of required repeaters to 28.

<!-- b000447 | prose | pages [20] -->
-20

<!-- b000448 | prose | pages [20] -->
A similar phenomenon occurs in Figure 9 where the last

<!-- b000449 | prose | pages [20] -->
-30

<!-- b000450 | prose | pages [20] -->
8% require 17 extra repeaters, pushing the number to 35.

<!-- b000451 | prose | pages [20] -->
-40 -40 -30 -20 -10 0 10 20 30 40

<!-- b000452 | prose | pages [20] -->
In the preferential distribution case, we notice that cov-

<!-- b000453 | prose | pages [20] -->
(a) 80% Coverage, 3 Colors, 10

<!-- b000454 | prose | pages [20] -->
ering 80% requires less repeaters. This is because a single

<!-- b000455 | prose | pages [20] -->
Circles

<!-- b000456 | caption | pages [20] -->
Figure 10: Preferential distribu-

<!-- b000457 | prose | pages [20] -->
tion of 10,000 users with 80% coverage.

<!-- b000458 | prose | pages [21] -->
Control # 12114

<!-- b000459 | prose | pages [21] -->
Repeater Eﬀectiveness

<!-- b000460 | prose | pages [21] -->
30

<!-- b000461 | furniture | pages [21] -->


<!-- b000462 | prose | pages [21] -->
1,000 Uniform 10,000 Uniform 1,000 Preferential

<!-- b000463 | prose | pages [21] -->
25

<!-- b000464 | prose | pages [21] -->
10,000 Preferential

<!-- b000465 | prose | pages [21] -->
Number of Repeaters

<!-- b000466 | prose | pages [21] -->
20

<!-- b000467 | prose | pages [21] -->
15

<!-- b000468 | prose | pages [21] -->
10

<!-- b000469 | prose | pages [21] -->
5

<!-- b000470 | prose | pages [21] -->
0

<!-- b000471 | furniture | pages [21] -->


<!-- b000472 | prose | pages [21] -->
80 82 84 86 88 90 92 94 96 98

<!-- b000473 | prose | pages [21] -->
Percent of Users Covered

<!-- b000474 | prose | pages [21] -->
(a) Covering

<!-- b000475 | prose | pages [21] -->
21

<!-- b000476 | prose | pages [21] -->
Repeater Eﬀectiveness

<!-- b000477 | prose | pages [21] -->
40

<!-- b000478 | furniture | pages [21] -->


<!-- b000479 | prose | pages [21] -->
1,000 Uniform

<!-- b000480 | prose | pages [21] -->
35

<!-- b000481 | prose | pages [21] -->
10,000 Uniform

<!-- b000482 | prose | pages [21] -->
1,000 Preferential

<!-- b000483 | prose | pages [21] -->
Number of Repeaters

<!-- b000484 | prose | pages [21] -->
30

<!-- b000485 | prose | pages [21] -->
10,000 Preferential

<!-- b000486 | prose | pages [21] -->
25

<!-- b000487 | prose | pages [21] -->
20

<!-- b000488 | prose | pages [21] -->
15

<!-- b000489 | prose | pages [21] -->
10

<!-- b000490 | furniture | pages [21] -->


<!-- b000491 | prose | pages [21] -->
5 80 82 84 86 88 90 92 94 96 98

<!-- b000492 | prose | pages [21] -->
Utility Ratio

<!-- b000493 | prose | pages [21] -->
(b) Utility

<!-- b000494 | caption | pages [21] -->
Figure 12: Uniform and preferential distributions of both 1, 000 and 10, 000 user population,

<!-- b000495 | prose | pages [21] -->
looking at the covering and utility cases. In (a), the minimum number of repeaters, on the y- axis, needed to provide coverage to a percentage of people, on the x-axis, is plotted. In (b), the minimum number of repeaters to achieve the utility ratio is plotted. Each curve of 1000 users averages 100 runs; each of 10,000 users averages 20 runs. The error bars on each curve show one standard deviation away from the average.

<!-- b000496 | prose | pages [21] -->
repeater can cover a larger percentage of the users due to them being clustered in location. The last 8% still requires a signiﬁcant amount of repeaters.

<!-- b000497 | prose | pages [21] -->
Utility

<!-- b000498 | prose | pages [21] -->
Looking at Figures 13 and 14, we again see that as the percentage of users increases, the number of repeaters required increases. There again exists the shift perceived as before, and preferential distributions still require less repeaters than that for uniform distributions.

<!-- b000499 | prose | pages [21] -->
Overview

<!-- b000500 | prose | pages [21] -->
In Figure 12a, we average the minimum number of circles needed to cover some percentage of the population from 100 runs for each curve of 1000 users and 20 runs for each curve of 10,000 users. We do this by incrementally adding circles and checking how many cir- cles pushes the percentage over that in the plot. We can see that either of the uniform populations requires more repeaters than either of the preferential populations. This is because the preferential clusters the points together, making them easier to cover with less repeaters. The uniform population, as the number of users increases, should converge to needing to cover the entire area. In fact, the preferential population should also cause this to happen; however, as we can see, the Greedy Covering Algorithm performs better in this case because the order of selection is close to optimal due to the extreme clusters. For

<!-- b000501 | prose | pages [22] -->
Control # 12114

<!-- b000502 | prose | pages [22] -->
40

<!-- b000503 | prose | pages [22] -->
40

<!-- b000504 | prose | pages [22] -->
30

<!-- b000505 | prose | pages [22] -->
30

<!-- b000506 | prose | pages [22] -->
20

<!-- b000507 | prose | pages [22] -->
20

<!-- b000508 | prose | pages [22] -->
10

<!-- b000509 | prose | pages [22] -->
10

<!-- b000510 | prose | pages [22] -->
0

<!-- b000511 | prose | pages [22] -->
0

<!-- b000512 | prose | pages [22] -->
-10

<!-- b000513 | prose | pages [22] -->
-10

<!-- b000514 | prose | pages [22] -->
-20

<!-- b000515 | prose | pages [22] -->
-20

<!-- b000516 | prose | pages [22] -->
-30

<!-- b000517 | prose | pages [22] -->
-30

<!-- b000518 | prose | pages [22] -->
-40

<!-- b000519 | prose | pages [22] -->
-40

<!-- b000520 | prose | pages [22] -->
-40 -30 -20 -10 0 10 20 30 40

<!-- b000521 | prose | pages [22] -->
-40 -30 -20 -10

<!-- b000522 | prose | pages [22] -->
22

<!-- b000523 | prose | pages [22] -->
40

<!-- b000524 | prose | pages [22] -->
30

<!-- b000525 | prose | pages [22] -->
20

<!-- b000526 | prose | pages [22] -->
10

<!-- b000527 | prose | pages [22] -->
0

<!-- b000528 | prose | pages [22] -->
-10

<!-- b000529 | prose | pages [22] -->
-20

<!-- b000530 | prose | pages [22] -->
-30

<!-- b000531 | prose | pages [22] -->
-40

<!-- b000532 | prose | pages [22] -->
0 0 10 20 30 40

<!-- b000533 | prose | pages [22] -->
-40 -30 -20 -10 0 10 20 30 40

<!-- b000534 | prose | pages [22] -->
(b) 90% Coverage, 6 Colors

<!-- b000535 | prose | pages [22] -->
(a) 80% Coverage, 4 Colors

<!-- b000536 | prose | pages [22] -->
(c) 98% Coverage, 10 Colors

<!-- b000537 | caption | pages [22] -->
Figure 13: Preferential distribution of 10,000 users with 80%, 90%, and 98% utility ratios.

<!-- b000538 | prose | pages [22] -->
40

<!-- b000539 | prose | pages [22] -->
30

<!-- b000540 | prose | pages [22] -->
20

<!-- b000541 | prose | pages [22] -->
10

<!-- b000542 | prose | pages [22] -->
0

<!-- b000543 | prose | pages [22] -->
-10

<!-- b000544 | prose | pages [22] -->
-20

<!-- b000545 | prose | pages [22] -->
-30

<!-- b000546 | prose | pages [22] -->
-40 -40 -30 -20 -10 0 10 20 30 40

<!-- b000547 | prose | pages [22] -->
(a) 90% Coverage, 4 Colors

<!-- b000548 | prose | pages [22] -->
40

<!-- b000549 | prose | pages [22] -->
30

<!-- b000550 | prose | pages [22] -->
20

<!-- b000551 | prose | pages [22] -->
10

<!-- b000552 | prose | pages [22] -->
0

<!-- b000553 | prose | pages [22] -->
-10

<!-- b000554 | prose | pages [22] -->
-20

<!-- b000555 | prose | pages [22] -->
-30

<!-- b000556 | prose | pages [22] -->
-40 -40 -30 -20 -10 0 10 20 30 40

<!-- b000557 | prose | pages [22] -->
(b) 98% Coverage, 6 Colors

<!-- b000558 | caption | pages [22] -->
Figure 14: Preferential distribution of 1000 users with 90% and 98% utility ratios.

<!-- b000559 | prose | pages [23] -->
Control # 12114 23

<!-- b000560 | prose | pages [23] -->
smaller sizes, the greedy algorithm is optimal in the case where there exist only clusters with suﬃcient spacing. We can see the algorithm at work in the ﬁgures, selecting the high density areas ﬁrst and then gathering the remainder population.

<!-- b000561 | prose | pages [23] -->
As the number of users increase, the curves are simply shifted up. This is because more area is covered by users as the number of users increases, and covering the same percentage of users should require more.

<!-- b000562 | prose | pages [23] -->
We perform the same operation to ﬁnd the curves in Figure 12b. The behavior is very similar; however, the scale diﬀers.

<!-- b000563 | prose | pages [23] -->
In each case, we can easily stay within the frequency band of 145-148MHz, and the number of colors rarely grow to above 12, meaning that we only need allocate 12 frequencies to the use of these repeaters.

<!-- b000564 | prose | pages [23] -->
7.2 Mountains and Complex Geometries

<!-- b000565 | prose | pages [23] -->
Up to this point we have only considered a completely ﬂat surface for our reegion of interest. If we allow the elevation of the surface to deviate from the smooth curved surface of a sphere, the problem of placing repeaters becomes considerably more diﬃcult. Previously the coverage of a repeater was independant of its location, however if we allow for complex elevation geometries, we must calculate the coverage of a repeater for any given location. This requires us to check for ever potential repater location at which locations would an antenna be in a direct line of sight path from the antenna of the repeater. To accomplish this we designed and implmented an algorithm that determines whether two points on an elevation map can be connected by an onubstructed line of sight path, and

<!-- b000566 | prose | pages [23] -->
Line of Sight

<!-- b000567 | prose | pages [23] -->
To determine whether or not one point is in the line of sight of another, we ﬁrst ﬁnd the elevation of the mesh points between the two radios, which we call the elevation proﬁle curve. This is done using bilinear interpolation when accuracy is desired, or Bresenham’s line algorithm when speed is desired over accuracy. Next we calculate the heights of the antennas places at the radio locations (generally assumed to be 18 feet). Then we form the straight line connecting the antennas and check to see if it intersects the elevation proﬁle. If there is an intersection, then the line of sight is obstructed. In practice the curve and the line are calculated and compared simultaneously so that intersections can be found more quickly. This algorithm has a runtime of O(n) (although the expectation is constant for large n).

<!-- b000568 | prose | pages [24] -->
Control # 12114 24

<!-- b000569 | prose | pages [24] -->
Repeater Coverage

<!-- b000570 | prose | pages [24] -->
For each mesh point on our grid, we ascertain the area coverage of a potential repeater at that location. We do so by checking the line of sight visibility from that point to each other point on the grid. If the mesh is a square of size n, then ince there are n2 points on the mesh, and for each of these points we must look at every other point, this algorithm calls the line of sight algorithm n4 times, although exploiting the symmetry of the problem allows us to cut this in half (if point A can see B, then point B can see A). Thus determining the coverage of a repeater for every point on the mesh has an algorithmic complexity of O(n5).

<!-- b000571 | prose | pages [24] -->
Constructing Terrain

<!-- b000572 | prose | pages [24] -->
To test our model we need realistic elevation data. While we can use real world elevation data, we also wanted a way to generate our own rough terrain for ﬂexibility. We start with a smooth surface representing the curvature of the earth. This is given by

<!-- b000573 | prose | pages [24] -->
√

<!-- b000574 | prose | pages [24] -->
R2 −x2 −y2 +

<!-- b000575 | prose | pages [24] -->
R2 −r2 −R

<!-- b000576 | prose | pages [24] -->
p

<!-- b000577 | prose | pages [24] -->
f(x, y) =

<!-- b000578 | prose | pages [24] -->
where R is the radius of the earth and r is the radius of the region. Next we can perturb this surface using either real world elevation data, or the Diamond-Square algorithm, to simulate mountains and other complex terrain.

<!-- b000579 | prose | pages [24] -->
Eﬀects of Mountains

<!-- b000580 | prose | pages [24] -->
When we add mountains to our region, we ﬁnd that some locations oﬀer far more coverage for a repeater than other locations. Therefore, in general, our greedy algorithm has a ten- dency to pick these locations as they are more eﬀective at both increasing coverage of users and utility ratio. In some scenarios, we ﬁnd a location that oﬀers an excepetionally great coverage, for instance at the top of a high peak. In these cases, generally fewer repeaters are needed to accomodate the users, since a few well placed ones are particularly eﬀective. However, the mountains and valleys can also isolate users from the repeaters, requiring a repeater to be placed very close to them in order to provide service. These isolated re- peaters only provide coverage to users in very close proximity, limiting there eﬀectiveness. In these cases, more repeaters than usual may be necessary to provide adequate coverage for the region.

<!-- b000581 | prose | pages [24] -->
8

<!-- b000582 | heading | pages [24] -->
Conclusions

<!-- b000583 | prose | pages [24] -->
Although our analytic results in Section 4 suggest that an optimal covering of any col- lection of points within the circle should require no more than 21 repeaters, our greedy

<!-- b000584 | prose | pages [25] -->
Control # 12114 25

<!-- b000585 | prose | pages [25] -->
(a) Smooth Curvature of Earth (b) Perturbed by Mountains

<!-- b000586 | caption | pages [25] -->
Figure 15: Here we shows the curvature of the Earth in our model as well as the curvature

<!-- b000587 | prose | pages [25] -->
perturbed by mountains.

<!-- b000588 | prose | pages [25] -->
approach consistently required more than this number. However, not only is this not sur- prising (given the simple nature of the algorithm), but it also allows for a simple solution: whenever the model requests more than 21 repeaters, simply place the repeaters according to the technique discussed in Section 4. Thus, although our model is weak when 100% coverage is sought, the fact that we know of an optimal solution to the problem (for most population distributions) makes this a moot point.

<!-- b000589 | prose | pages [25] -->
Instead, the strength of our model lies in its ability to present good solutions when fewer than 100% coverage is requested. As portrayed in Figures 8, 9, 11, and 12, relaxing the perfect covering requirement slightly allows for solutions involving much fewer than 21 repeaters, greatly improving the value one is attaining per placed repeater.

<!-- b000590 | prose | pages [25] -->
Interestingly, the same phenomenon holds when attempting to maximize the utility ra- tio. Figures 12, 13, and 14 all show that marginally weaker goals result in a substantially smaller number of required repeaters.

<!-- b000591 | prose | pages [25] -->
9 Future Considerations

<!-- b000592 | prose | pages [25] -->
9.1

<!-- b000593 | heading | pages [25] -->
Changes to the Model

<!-- b000594 | prose | pages [25] -->
9.1.1 Ad-hoc Networks and Game Theory

<!-- b000595 | prose | pages [25] -->
Currently, our model assumes that there is an external medium by which repeaters can communicate. It would be interesting to analyze what happens in the absense of this chan-

<!-- b000596 | prose | pages [26] -->
Control # 12114 26

<!-- b000597 | prose | pages [26] -->
nel, where repeaters relay messages by spreading using their own transmitters (and thereby being bounded by some physical limitations).

<!-- b000598 | prose | pages [26] -->
Further, one can consider the question as to what kinds of game theoretic implications can arise. Can there be an analogue of selﬁsh routing in the VHF wave networks?

<!-- b000599 | prose | pages [26] -->
9.1.2 One-to-One Communication

<!-- b000600 | prose | pages [26] -->
Whereas our model is built for one-to-many communication, there can also exist scenarios where the users wish to communicate between themselves. Although much more complex, creating a system that allows for any pair of users to converse could prove to be enlightening algorithmically.

<!-- b000601 | prose | pages [26] -->
9.1.3 Non-static and Introduced Users

<!-- b000602 | prose | pages [26] -->
As of now, our model assumes all users are completely stationary. Perhaps a more complete model would incorporate dynamic users in addition to static ones, allowing for mobile individuals to participate in the network as well. Further, how can our model incorporate the joining and leaving of additional users? Is it “stable” with respect to small perturbations in the population?

<!-- b000603 | prose | pages [26] -->
9.2

<!-- b000604 | heading | pages [26] -->
Model Correctness

<!-- b000605 | prose | pages [26] -->
9.2.1 Region Topography

<!-- b000606 | prose | pages [26] -->
A truly accurate model of repeater coordination would utilize terrain data to better pre- dict just how the VHF radio waves will propogate throughout the region. Although our model crudely approximates this propogation with perfect circles, the various aspects of terrain data can greatly change the eﬃcacy of various locations in housing repeater. The Longley-Rice Irregular Terrain Model[8], for example, demonstrates a simple way to model wave propogation on complex terrains.

<!-- b000607 | prose | pages [26] -->
9.3 Real World Data

<!-- b000608 | prose | pages [26] -->
Currently, all of our data is randomly generated. The best way to model real-world sce- narios, however, is to acquire the actual population distributions from cities and ﬁnd some topographic map of the regions in question. If chosen carefully, this data can much better reﬂect the intricacies of population spread and the abnormalities of terrain.

<!-- b000609 | prose | pages [27] -->
Control # 12114 27

<!-- b000610 | prose | pages [27] -->
9.4 Theoretical Issues

<!-- b000611 | prose | pages [27] -->
9.4.1 Algorithmic Improvement

<!-- b000612 | prose | pages [27] -->
Currently, our analysis depends heavily on greedy algorithms. Although the optimal solu- tion to these problems might be intractable, our model could still beneﬁt from algorithms with stronger average-case behavior, many of which are readily available.

<!-- b000613 | prose | pages [28] -->
Control # 12114 28

<!-- b000614 | heading | pages [28] -->
References

<!-- b000615 | references | pages [28] -->
[1] Albert, R., & Barab´asi, A.-L. (2002).

<!-- b000616 | references | pages [28] -->
Statistical mechanics of complex networks.

<!-- b000617 | references | pages [28] -->
Reviews of Modern Physics, 74, 47–97.

<!-- b000618 | references | pages [28] -->
[2] American Radio Relay League (2008). The Arrl Operating Manual for Radio Ama-

<!-- b000619 | references | pages [28] -->
teurs. ARRL OPERATING MANUAL. Amer Radio Relay League.

<!-- b000620 | references | pages [28] -->
[3] Barclay, L., & Institution of Electrical Engineers (2003). Propagation of radiowaves.

<!-- b000621 | references | pages [28] -->
Electromagnetic Waves. Institution of Electrical Engineers.

<!-- b000622 | references | pages [28] -->
[4] Federal Communications Commission (2011). About the fcc.

<!-- b000623 | references | pages [28] -->
URL http://www.fcc.gov/aboutus.html

<!-- b000624 | references | pages [28] -->
[5] Fowler, R., Paterson, M., & Tanimoto, S. (1981). Optimal packing and covering in

<!-- b000625 | references | pages [28] -->
the plane are np-complete. Information Processing Letters, 12(3), 133–137.

<!-- b000626 | references | pages [28] -->
[6] Fukshansky, L. (2011).

<!-- b000627 | references | pages [28] -->
Revisiting the hexagonal lattice: On optimal lattice circle

<!-- b000628 | references | pages [28] -->
packing. Elemente der Mathematik, 66(1), 1–9.

<!-- b000629 | references | pages [28] -->
[7] Hernando, A., Villuendas, D., Vesperinas, C., Abad, M., & Plastino, A. (2009). Un-

<!-- b000630 | references | pages [28] -->
ravelling the size distribution of social groups with information theory on complex

<!-- b000631 | references | pages [28] -->
networks. European Physics Journal B.

<!-- b000632 | references | pages [28] -->
[8] Longley, A. G., & Rice, P. L. (1968). Prediction of tropospheric radio transmission

<!-- b000633 | references | pages [28] -->
loss over irregular terrain: A computer method. ESSA Tech. Report ERL65- ITS67.

<!-- b000634 | references | pages [28] -->
[9] Straw, R., Cebik, L., Hallidy, D., & Jansson, D. (2007). The ARRL Antenna Book.

<!-- b000635 | references | pages [28] -->
ARRL ANTENNA BOOK. ARRL.

<!-- b000636 | references | pages [28] -->
[10] ukrepeaters, The UK Amateur Radio Repeater Resource (2011). 2 metres band re-

<!-- b000637 | references | pages [28] -->
peaters (coverage).

<!-- b000638 | references | pages [28] -->
URL http://www.ukrepeater.net/2m.htm

<!-- b000639 | references | pages [28] -->
[11] Xiao, B., Zhuge, Q., He, Y., & Sha, E. H.-M. (2003). Algorithms for disk covering

<!-- b000640 | references | pages [28] -->
problems with the most points. Proceeding of the International Conference on Parallel

<!-- b000641 | references | pages [28] -->
and Distributed Computing and Systems, (pp. 541–546).
