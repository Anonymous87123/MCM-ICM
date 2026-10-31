# P-B-2016-52221-f8094e57

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For office use only

<!-- b000003 | prose | pages [1] -->
For office use only

<!-- b000004 | prose | pages [1] -->
52221

<!-- b000005 | prose | pages [1] -->
T1 ________________

<!-- b000006 | prose | pages [1] -->
T2 ________________

<!-- b000007 | furniture | pages [1] -->


<!-- b000008 | prose | pages [1] -->
F1 ________________

<!-- b000009 | prose | pages [1] -->
F2 ________________

<!-- b000010 | prose | pages [1] -->
Problem Chosen

<!-- b000011 | prose | pages [1] -->
T3 ________________

<!-- b000012 | prose | pages [1] -->
T4 ________________

<!-- b000013 | furniture | pages [1] -->


<!-- b000014 | prose | pages [1] -->
F3 ________________

<!-- b000015 | title | pages [1] -->
B

<!-- b000016 | prose | pages [1] -->
F4 ________________

<!-- b000017 | furniture | pages [1] -->


<!-- b000018 | prose | pages [1] -->
2016

<!-- b000019 | prose | pages [1] -->
MCM/ICM

<!-- b000020 | heading | pages [1] -->
Summary Sheet

<!-- b000021 | prose | pages [1] -->
(Your team's summary should be included as the first page of your electronic submission.)

<!-- b000022 | prose | pages [1] -->
Type a summary of your results on this page. Do not include the name of your school, advisor, or team members on this page.

<!-- b000023 | furniture | pages [1] -->


<!-- b000024 | furniture | pages [1] -->


<!-- b000025 | prose | pages [1] -->
A New Space Debris Collisions Insurance Model

<!-- b000026 | furniture | pages [1] -->


<!-- b000027 | prose | pages [1] -->
With the rapid increase of human aerospace activities, the population of space debris has become a

<!-- b000028 | prose | pages [1] -->
universal concern.

<!-- b000029 | prose | pages [1] -->
We successfully find a commercial opportunity under the background of serious space debris

<!-- b000030 | prose | pages [1] -->
population, and that is the space debris collision insurance service. The basic idea of this service is that

<!-- b000031 | prose | pages [1] -->
if any debris collision cause damage to the spacecraft during the insurance duration, we will pay for

<!-- b000032 | prose | pages [1] -->
the claims. Meanwhile, in order to reduce the risks of collision and losing money, we will carry out

<!-- b000033 | prose | pages [1] -->
Active Debris Removal (ADR) measures by renting existing ADR technologies. The structure of

<!-- b000034 | prose | pages [1] -->
whole service is demonstrated in fig.3.

<!-- b000035 | prose | pages [1] -->
To calculate the profit of our proposed service, we should know how much our income (premium)

<!-- b000036 | prose | pages [1] -->
is and how much our cost (ADR cost and claims) is.

<!-- b000037 | prose | pages [1] -->
The premium and claims of this service is determined by the premium rate, which is closely

<!-- b000038 | prose | pages [1] -->
related to the effective collision probability. Therefore, we build an analysis model based on Orbital

<!-- b000039 | prose | pages [1] -->
Debris Engineering Model（ORDEM 2000）to anticipate the distribution and flux of space debris. By

<!-- b000040 | prose | pages [1] -->
improving the method introduced by European Space Agency, and using it on the ORDEM 2000 data,

<!-- b000041 | prose | pages [1] -->
we deduce the effective collision probability from the flux. Furthermore, to connect the effective

<!-- b000042 | prose | pages [1] -->
collision probability with the premium rate, we establish a new insurance model which takes the

<!-- b000043 | prose | pages [1] -->
special features of space debris into consideration.

<!-- b000044 | prose | pages [1] -->
The ADR cost is related to the two-steps strategy of ADR. Firstly, by analyzing the expression of

<!-- b000045 | prose | pages [1] -->
effective collision probability, we set a size limit for the debris to be removed. Secondly, based on

<!-- b000046 | prose | pages [1] -->
fuzzy comprehensive evaluation (FCE) method, we build a model to design the ADR strategy for

<!-- b000047 | prose | pages [1] -->
removing the debris with certain range of size.

<!-- b000048 | prose | pages [1] -->
We simulate the whole insurance service via computer. The result indicates that our insurance

<!-- b000049 | prose | pages [1] -->
service has a great profitability and business competitive.

<!-- b000050 | prose | pages [1] -->
Considering that the debris distribution data from ORDEM varies with time and those data determined both premium rate and ADR strategy, our model is a strongly time-dependent one. We choose premium rate, insurance duration and fuzzy evaluation factor for sensitivity analysis, which show that our model is very robust and can deal with some important “What if?” scenarios.

<!-- b000051 | furniture | pages [1] -->


<!-- b000052 | furniture | pages [1] -->


<!-- b000053 | furniture | pages [2] -->
Team  #52221                                                              Page 1 of 23

<!-- b000054 | prose | pages [2] -->
Content

<!-- b000055 | prose | pages [2] -->
1 Introduction ........................................................................................................................... 2

<!-- b000056 | prose | pages [2] -->
1.1 Background ........................................................................................................................................ 2

<!-- b000057 | prose | pages [2] -->
1.2 Our Work ........................................................................................................................... 3

<!-- b000058 | prose | pages [2] -->
1.3 Symbol Description ............................................................................................................. 3

<!-- b000059 | prose | pages [2] -->
1.4 General Assumptions ........................................................................................................... 4 2 Commercial Opportunity ....................................................................................................... 4 3 Space Debris Distribution Rule ............................................................................................. 5

<!-- b000060 | prose | pages [2] -->
3.1 The Range .......................................................................................................................... 5

<!-- b000061 | prose | pages [2] -->
3.2 ORDEM 2000 ..................................................................................................................... 5

<!-- b000062 | prose | pages [2] -->
3.3 Distribution of Space Debris ................................................................................................. 6

<!-- b000063 | prose | pages [2] -->
3.3.1 General Rule of Space Debris Distribution ....................................................................... 6

<!-- b000064 | prose | pages [2] -->
3.3.2 Flux of Space Debris ..................................................................................................... 7 4 Probability of Effective Collision Probability ....................................................................... 7

<!-- b000065 | prose | pages [2] -->
4.1 Annual Collision Probability ................................................................................................. 7

<!-- b000066 | prose | pages [2] -->
4.2 Effective Collision Probability .............................................................................................. 8 5 Premium Rate ........................................................................................................................ 9

<!-- b000067 | prose | pages [2] -->
5.1 Traditional Model ................................................................................................................ 9

<!-- b000068 | prose | pages [2] -->
5.2 Improved Model ................................................................................................................................. 10 6 Strategy of ADR .................................................................................................................... 11

<!-- b000069 | prose | pages [2] -->
6.1 First Step ............................................................................................................................ 11

<!-- b000070 | prose | pages [2] -->
6.2 Second Step: Fuzzy Comprehensive Evaluation ...................................................................... 12

<!-- b000071 | prose | pages [2] -->
6.2.1 The ADR Measures ....................................................................................................... 12

<!-- b000072 | prose | pages [2] -->
6.2.2 Implementation of Fuzzy Comprehensive Evaluation ......................................................... 12

<!-- b000073 | prose | pages [2] -->
6.2.3 Conclusion ................................................................................................................................... 14 7 The Impact of Insurance Duration (Time) ....................................................................................... 14 8 Model Implementation and Economy Validation .......................................................................... 15 9 “What If” and Sensitive Analysis ...................................................................................................... 17 10 Strengths and Weaknesses ................................................................................................................ 19

<!-- b000074 | prose | pages [2] -->
10.1 Strengths ........................................................................................................................................... 19

<!-- b000075 | prose | pages [2] -->
10.2 Weaknesses ....................................................................................................................................... 19 References ................................................................................................................................................. 20 Executive Summary ................................................................................................................................. 21

<!-- b000076 | furniture | pages [2] -->


<!-- b000077 | furniture | pages [2] -->


<!-- b000078 | furniture | pages [2] -->


<!-- b000079 | furniture | pages [2] -->


<!-- b000080 | furniture | pages [2] -->


<!-- b000081 | furniture | pages [2] -->


<!-- b000082 | furniture | pages [2] -->


<!-- b000083 | furniture | pages [2] -->


<!-- b000084 | furniture | pages [3] -->
Team  #52221                                                              Page 2 of 23

<!-- b000085 | heading | pages [3] -->
1  Introduction

<!-- b000086 | heading | pages [3] -->
1.1  Background

<!-- b000087 | furniture | pages [3] -->


<!-- b000088 | prose | pages [3] -->
In 1957, the first man-made object was launched into space. From then on, more than 5,000 spacecraft had been launched to Earth-centered orbits of various heights. With the rapid increase of the human aerospace activities, the population of space debris has become more and more serious.

<!-- b000089 | prose | pages [3] -->
Space debris is any man-made object in orbit about the Earth which no longer serves a useful function. Such debris includes nonfunctional spacecraft, abandoned launch vehicle stages, mission-related debris and fragmentation debris [1].

<!-- b000090 | prose | pages [3] -->
Most space debris is moving very fast. It can reach speeds of 4.3 to 5 miles per second. Five miles per second is about 18,000 miles per hour. That's almost seven times faster than a bullet. Since it is moving so quickly, a tiny piece of orbital debris can cause a lot of damage. A piece of debris the size of a marble could hit as hard as a bowling ball going 300 miles per hour [2]. It is a severe potential danger especially to the International Space Station, space shuttles and other spacecraft with humans aboard. Today, there are more than 20,000 pieces of debris larger than a softball orbiting the Earth; 500,000 pieces of debris the size of a marble or larger; many millions of pieces of debris that are so small they can’t be tracked [1].

<!-- b000091 | prose | pages [3] -->
Dealing with these dangerous debris scientists have proposed numbers of methods，including water-jets, high energy lasers and large satellites designed to sweep up the debris and so on.

<!-- b000092 | furniture | pages [3] -->


<!-- b000093 | furniture | pages [3] -->


<!-- b000094 | furniture | pages [3] -->


<!-- b000095 | caption | pages [3] -->
Figure 2: Debris in High Earth Orbit [3]

<!-- b000096 | caption | pages [3] -->
Figure 1: Debris in Low Earth Orbit [3]

<!-- b000097 | furniture | pages [3] -->


<!-- b000098 | prose | pages [3] -->
Considering the high expense and high risks of running spacecraft, most of the owners of the satellites tend to cover insurance for their spacecraft in the past decade. Therefore the market of space insurance has grown very large. The premium income for 2014 was closed to USD700m. The growth of orbit debris has compromised the safety of the satellites. Because of not fully considering the impact of increasing debris, the space insurance market is still volatile and reported a loss in 2013. And it was only marginally profitable to insurers in 2014 [4].

<!-- b000099 | furniture | pages [3] -->


<!-- b000100 | furniture | pages [3] -->


<!-- b000101 | furniture | pages [3] -->


<!-- b000102 | furniture | pages [4] -->
Team  #52221                                                              Page 3 of 23

<!-- b000103 | heading | pages [4] -->
1.2  Our Work

<!-- b000104 | furniture | pages [4] -->


<!-- b000105 | prose | pages [4] -->
We are asked to find out whether an economically attractive opportunity exist and develop a model to determine the best alternative or combination of alternatives that a private firm could adopt as a commercial opportunity to address the space debris problem.

<!-- b000106 | prose | pages [4] -->
Since the rising population of space debris has strongly affected the safety of the spacecraft and most of insurers didn’t take this situation into consideration, a good commercial opportunity arose: debris collision space insurance. This insurance consists of two parts. One is that if any debris collision happens to the spacecraft during the insurance duration, we will pay for the claims. Another is that we take the initiative to carry out Active Debris Removal (ADR) to reduce the probability of debris collision which strongly influence the claims probability.

<!-- b000107 | prose | pages [4] -->
We firstly build a general insurance model. Then we establish a space debris distribution rule to estimate the risks and calculate premium rate. In order to decrease the claims, we will rent the existing technology of Active Debris Removal (ADR) and reduce the probability of debris collision. Besides, we use fuzzy comprehensive evaluation (FCE) method to build an alternatives choosing strategy to determine which ADR method to use.

<!-- b000108 | prose | pages [4] -->
We simulate the whole insurance service via computer. The data indicate that our insurance service has a great profitability and business competitive. We choose premium rate, insurance duration and fuzzy evaluation factor for sensitivity analysis, and results show that our model is very robust and can deal with some important “What if?” scenarios. In the last stage, we provide an executive summary.

<!-- b000109 | furniture | pages [4] -->


<!-- b000110 | heading | pages [4] -->
1.3  Symbol Description

<!-- b000111 | furniture | pages [4] -->


<!-- b000112 | caption | pages [4] -->
Table 1: Notation

<!-- b000113 | prose | pages [4] -->
Symbol Meaning

<!-- b000114 | prose | pages [4] -->
q expected value of debris t time S cross sectional area F flux of space debris 𝐹̅ orbit average flux T time of a year N expected value of total debris impacts per unit area when spacecraft travel a year 𝑃𝑐 collision probability index for the debris and meteoroids diameter range [𝐷𝑝,𝑗… 𝐷𝑝,𝑗+1] j flux of debris and meteoroids in the diameter range [𝐷𝑝,𝑗… 𝐷𝑝,𝑗+1] 𝐹𝑗 𝐷𝑡 space system (spacecraft or launch vehicle stage) maximum diameter 𝐷𝑝,𝑗 debris diameter 𝑃𝑐,𝑦𝑟 annual collision probability average flux of debris and meteoroids in the diameter range [𝐷𝑝,𝑗… 𝐷𝑝,𝑗+1] 𝐹̅𝑗 𝑃𝑒 effective collision probability 𝑃𝑖𝑛 ineffective collision probability 𝑀𝑝 projectile mass (i.e. debris) 𝑉𝑖𝑚𝑝 impact velocity (i.e. relative velocity between the projectile and target) 𝑀𝑡 target mass (i.e. the spacecraft)

<!-- b000115 | furniture | pages [4] -->


<!-- b000116 | furniture | pages [5] -->
Team  #52221                                                              Page 4 of 23

<!-- b000117 | prose | pages [5] -->
𝐷𝑝 diameter of debris 𝐷𝑝,𝑐 diameter threshold

<!-- b000118 | prose | pages [5] -->
(𝐴𝑝

<!-- b000119 | prose | pages [5] -->
𝐴𝑝 𝑀𝑝)𝑠𝑡𝑑= 0.01 𝑚2/𝑘𝑔

<!-- b000120 | prose | pages [5] -->
area-to-mass ratio, (

<!-- b000121 | prose | pages [5] -->
)

<!-- b000122 | furniture | pages [5] -->


<!-- b000123 | prose | pages [5] -->
𝑀𝑝

<!-- b000124 | prose | pages [5] -->
𝑠𝑡𝑑

<!-- b000125 | prose | pages [5] -->
𝛼 premium rate 𝐶𝑝 total claims 𝐶𝑧 total premium 𝛽 refers to total failure rate 𝛽̂ the failure rate of the improved model E the expected profit 𝛾 critical failure probability

<!-- b000126 | furniture | pages [5] -->


<!-- b000127 | heading | pages [5] -->
1.4  General Assumptions

<!-- b000128 | furniture | pages [5] -->


<!-- b000129 | prose | pages [5] -->
·The inclination angle of orbit does not affect the number of debris impacts.

<!-- b000130 | prose | pages [5] -->
·The orbit altitude remains the same.

<!-- b000131 | prose | pages [5] -->
·Only space debris will cause damage to spacecraft.

<!-- b000132 | prose | pages [5] -->
·Do not take the research and development costs into consideration.

<!-- b000133 | prose | pages [5] -->
·The number of insurance customers is big enough to satisfies the law of large numbers.

<!-- b000134 | furniture | pages [5] -->


<!-- b000135 | heading | pages [5] -->
2  Commercial Opportunity

<!-- b000136 | furniture | pages [5] -->


<!-- b000137 | prose | pages [5] -->
As discussed above, the rising space debris is a potential threaten to the safety of spacecraft. On the other hand, it is also a potential commercial opportunity for insurance company.

<!-- b000138 | furniture | pages [5] -->


<!-- b000139 | furniture | pages [5] -->


<!-- b000140 | furniture | pages [5] -->


<!-- b000141 | furniture | pages [5] -->


<!-- b000142 | furniture | pages [5] -->


<!-- b000143 | furniture | pages [5] -->


<!-- b000144 | furniture | pages [5] -->


<!-- b000145 | furniture | pages [5] -->


<!-- b000146 | furniture | pages [5] -->


<!-- b000147 | furniture | pages [5] -->


<!-- b000148 | furniture | pages [5] -->


<!-- b000149 | furniture | pages [5] -->


<!-- b000150 | furniture | pages [5] -->


<!-- b000151 | furniture | pages [5] -->


<!-- b000152 | furniture | pages [5] -->


<!-- b000153 | furniture | pages [5] -->


<!-- b000154 | furniture | pages [5] -->


<!-- b000155 | caption | pages [5] -->
Figure 3: Model Schematic Diagram

<!-- b000156 | furniture | pages [5] -->


<!-- b000157 | furniture | pages [6] -->
Team  #52221                                                              Page 5 of 23

<!-- b000158 | prose | pages [6] -->
Most of the insurers didn’t fully consider the impact of increasing debris when calculate the premium rate. Therefore it’s becoming more and more difficult to make money in the area of space insurance. At the same time, there are certain companies and space agency doing research on ADR in recent years，and several methods have been successfully developed.

<!-- b000159 | prose | pages [6] -->
Based on the situations above, we build a brand new space insurance mode, and verify this mode’s ability to make profits. To demonstrate our model better, we plot over a flowchart in Figure 3.

<!-- b000160 | furniture | pages [6] -->


<!-- b000161 | furniture | pages [6] -->


<!-- b000162 | prose | pages [6] -->
Suppose a satellite is planned to be launched into the space, and the owner of the satellite wants to cover insurance this spacecraft. Then we can offer him a space insurance serve which consists of two parts. One is that if any debris collision happens to the spacecraft during the insurance duration, we will pay for the claims. In order to reduce the collision risks, we will carry out Active Debris Removal (ADR) to reduce the probability of debris collision. The premium and claims of this service, as shown in Figure3, is determined by the premium rate. Premium rate is related to the collision risk, and cost is determined by strategy of ADR. Finally they are both connected to the space debris distribution rule, which is influenced by the insurance duration, or time. The claims we might pay for is determined by premium rate and how much premium is.

<!-- b000163 | furniture | pages [6] -->


<!-- b000164 | heading | pages [6] -->
3  Space Debris Distribution Rule

<!-- b000165 | heading | pages [6] -->
3.1  The Range

<!-- b000166 | furniture | pages [6] -->


<!-- b000167 | prose | pages [6] -->
Generally, satellite orbit is divided into three categories, they are:

<!-- b000168 | prose | pages [6] -->
·Low Earth Orbit (LEO)：Its ground clearances rang from 200km to 2000km ·Synchronous Orbit：Its ground clearances are around 35786km. ·Highly Elliptical Orbit (HEO): Its ground clearances are beyond 20000km.

<!-- b000169 | furniture | pages [6] -->


<!-- b000170 | furniture | pages [6] -->


<!-- b000171 | prose | pages [6] -->
We only analyze the space debris environment in LEO and HEO and neglect the situation in HEO. The reasons we can do this are:

<!-- b000172 | prose | pages [6] -->
·The speed of spacecraft in HEO is much lower than in LEO ·In HEO, the size of the spacecraft is much smaller compared with the distance between two spacecraft.

<!-- b000173 | prose | pages [6] -->
·The amount of the spacecraft in HEO is much smaller than in LEO.

<!-- b000174 | furniture | pages [6] -->


<!-- b000175 | heading | pages [6] -->
3.2  ORDEM2000

<!-- b000176 | furniture | pages [6] -->


<!-- b000177 | prose | pages [6] -->
Orbital Debris Engineering Model (ORDEM) is developed by NASA Johnson Space Center in 1996 [5], designed to predict and analyze the debris environment [5]. The latest version of ORDEM is ORDEM 2000, incorporated in which is a large set of observational data (both in-situ and ground-based) that reflect the current debris environment. These data cover the object size range from 10 µm to 1 m and position range from low Earth orbit to synchronous orbit, and that’s exactly what we want [5].

<!-- b000178 | prose | pages [6] -->
Analytical techniques (such as maximum likelihood estimation and Bayesian statistics) are employed to determine the orbit populations used to calculate population fluxes and their

<!-- b000179 | furniture | pages [6] -->


<!-- b000180 | furniture | pages [7] -->
Team  #52221                                                              Page 6 of 23

<!-- b000181 | prose | pages [7] -->
uncertainties.

<!-- b000182 | prose | pages [7] -->
The Debris Assessment Software (DAS) is a software based on ORDEM 2000, its operation interface is shown in figure 4.

<!-- b000183 | furniture | pages [7] -->


<!-- b000184 | furniture | pages [7] -->


<!-- b000185 | furniture | pages [7] -->


<!-- b000186 | furniture | pages [7] -->


<!-- b000187 | furniture | pages [7] -->


<!-- b000188 | furniture | pages [7] -->


<!-- b000189 | furniture | pages [7] -->


<!-- b000190 | furniture | pages [7] -->


<!-- b000191 | furniture | pages [7] -->


<!-- b000192 | furniture | pages [7] -->


<!-- b000193 | furniture | pages [7] -->


<!-- b000194 | furniture | pages [7] -->


<!-- b000195 | furniture | pages [7] -->


<!-- b000196 | furniture | pages [7] -->


<!-- b000197 | furniture | pages [7] -->


<!-- b000198 | furniture | pages [7] -->


<!-- b000199 | furniture | pages [7] -->


<!-- b000200 | furniture | pages [7] -->


<!-- b000201 | caption | pages [7] -->
Figure 4: DAS

<!-- b000202 | furniture | pages [7] -->


<!-- b000203 | furniture | pages [7] -->


<!-- b000204 | heading | pages [7] -->
3.3  Distribution of Space Debris

<!-- b000205 | heading | pages [7] -->
3.3.1  General Rule of Space Debris Distribution

<!-- b000206 | furniture | pages [7] -->


<!-- b000207 | prose | pages [7] -->
Using the DAS, we can figure out how space debris distribution varies with altitude.

<!-- b000208 | caption | pages [7] -->
Figure 5 indicates the number (per year) of debris impacts, of each impactor size we expected.

<!-- b000209 | prose | pages [7] -->
Numbers of debris impacts are given on a logarithmic (base 10) scale. Results are a function of altitude [6].

<!-- b000210 | prose | pages [7] -->
In this plot, we supposed the launch date is on 2016.01.01 and the duration lasts one year. It’s apparent that the smaller debris size is, the more debris are. Also, the number of debris varies with the height, and, particularly, the height of 700-1000 kilometers and 1400-1600 kilometers are two peaks indicating the hardest-hit areas.

<!-- b000211 | furniture | pages [7] -->


<!-- b000212 | furniture | pages [8] -->
Team  #52221                                                              Page 7 of 23

<!-- b000213 | furniture | pages [8] -->


<!-- b000214 | prose | pages [8] -->
Figure 5

<!-- b000215 | furniture | pages [8] -->


<!-- b000216 | heading | pages [8] -->
3.3.2  Flux of Space Debris

<!-- b000217 | furniture | pages [8] -->


<!-- b000218 | prose | pages [8] -->
Flux of space debris is a relevant factor describing the distribution of the space debris. It can be defined as impacts/ unit time/ unit area. In ORDEM 2000 model, the flux is defined as [7]

<!-- b000219 | prose | pages [8] -->
𝐹=

<!-- b000220 | prose | pages [8] -->
where: q   expected value of debris t   time

<!-- b000221 | prose | pages [8] -->
S   cross sectional area

<!-- b000222 | furniture | pages [8] -->


<!-- b000223 | prose | pages [8] -->
The orbit average flux is[7]:

<!-- b000224 | prose | pages [8] -->
𝐹̅ =

<!-- b000225 | prose | pages [8] -->
where: T   time of a year

<!-- b000226 | furniture | pages [8] -->


<!-- b000227 | furniture | pages [8] -->


<!-- b000228 | prose | pages [8] -->
𝜕2𝑞

<!-- b000229 | prose | pages [8] -->
𝜕𝑡𝜕𝑆                              (3.3.1)

<!-- b000230 | prose | pages [8] -->
∑𝐹

<!-- b000231 | prose | pages [8] -->
𝑁 𝑁

<!-- b000232 | prose | pages [8] -->
𝑇=

<!-- b000233 | prose | pages [8] -->
𝑇                          (3.3.2)

<!-- b000234 | prose | pages [8] -->
N   expected value of total debris impacts per unit area when spacecraft travel a year

<!-- b000235 | furniture | pages [8] -->


<!-- b000236 | prose | pages [8] -->
The flux of the debris is in direct proportion to the risk of being collide. The specific value of average flux can be obtained from the ORDEM 2000.

<!-- b000237 | furniture | pages [8] -->


<!-- b000238 | heading | pages [8] -->
4  Probability of Effective Collision

<!-- b000239 | heading | pages [8] -->
4.1  Annual Collision Probability

<!-- b000240 | furniture | pages [8] -->


<!-- b000241 | prose | pages [8] -->
As mentioned above, the collision probability is closely related to the flux of the debris. According

<!-- b000242 | furniture | pages [8] -->


<!-- b000243 | furniture | pages [9] -->
Team  #52221                                                              Page 8 of 23

<!-- b000244 | prose | pages [9] -->
to ESA Space Debris Mitigation Compliance Verification Guidelines, the collision probability can be simply expressed as[8]:

<!-- b000245 | furniture | pages [9] -->


<!-- b000246 | prose | pages [9] -->
𝜋

<!-- b000247 | prose | pages [9] -->
𝑁 4 (𝐷𝑡+ 𝐷𝑝,𝑗)2

<!-- b000248 | prose | pages [9] -->
𝑃𝑐= ∑ 𝐹𝑗

<!-- b000249 | prose | pages [9] -->
𝑗=1

<!-- b000250 | prose | pages [9] -->
where:

<!-- b000251 | prose | pages [9] -->
(4.1.1)

<!-- b000252 | prose | pages [9] -->
j    index for the debris and meteoroids diameter range [Dp,j ,  Dp,j+1]

<!-- b000253 | prose | pages [9] -->
𝐹𝑗   flux of debris and meteoroids in the diameter range [Dp,j , Dp,j+1]

<!-- b000254 | prose | pages [9] -->
Dt    space system (spacecraft or launch vehicle stage) maximum diameter Dp,j   debris diameter

<!-- b000255 | furniture | pages [9] -->


<!-- b000256 | prose | pages [9] -->
𝜋 4 (𝐷𝑡+ 𝐷𝑝,𝑗)2 stands for the collision cross-sectional area, that is, the envelope of

<!-- b000257 | prose | pages [9] -->
The term of

<!-- b000258 | prose | pages [9] -->
the maximum projected area of the space system and the area of the debris [8].

<!-- b000259 | prose | pages [9] -->
Considering the definition of the 𝐹𝑗, 𝑃𝑐 may regard as the sum of a serial expected. Because the

<!-- b000260 | prose | pages [9] -->
output value of ORDEM 2000 is 𝐹̅ , we change formula 3.4.1 into:

<!-- b000261 | furniture | pages [9] -->


<!-- b000262 | prose | pages [9] -->
𝑁

<!-- b000263 | prose | pages [9] -->
𝑃𝑐,𝑦𝑟= ∑ 𝐹̅𝑗

<!-- b000264 | prose | pages [9] -->
𝑗=1

<!-- b000265 | prose | pages [9] -->
where:

<!-- b000266 | prose | pages [9] -->
𝜋 𝜋

<!-- b000267 | prose | pages [9] -->
4 (𝐷𝑡+ 𝐷𝑝,𝑗)2 (4.1.2)

<!-- b000268 | prose | pages [9] -->
𝐹̅𝑗   average flux of debris and meteoroids in the diameter range [Dp,j , Dp,j+1]

<!-- b000269 | furniture | pages [9] -->


<!-- b000270 | prose | pages [9] -->
So, the 𝑃𝑐,𝑦𝑟 become an annual collision probability. From the formula we can find out that the probability is expressed as a form of sum. Every individual terms in the sum stands for the contribution of the debris with a size range from Dp,j to Dp,j+1 to the 𝑃𝑐,𝑦𝑟. This property is very useful to our next steps.

<!-- b000271 | furniture | pages [9] -->


<!-- b000272 | heading | pages [9] -->
4.2  Effective Collision Probability

<!-- b000273 | furniture | pages [9] -->


<!-- b000274 | prose | pages [9] -->
Considering the fact that not every collision will lead to severe damage, we define an concept of effective collision probability:

<!-- b000275 | furniture | pages [9] -->


<!-- b000276 | prose | pages [9] -->
𝑃𝑒= 𝑃𝑐,𝑦𝑟−𝑃𝑖𝑛                           (4.2.1)

<!-- b000277 | furniture | pages [9] -->


<!-- b000278 | prose | pages [9] -->
The effective collision probability equals annual collision probability minus ineffective collision probability. The main parameter to determine whether a collision is catastrophic, is the energy-to-mass ratio (EMR)[8]:

<!-- b000279 | prose | pages [9] -->
1 2𝑀𝑝𝑉𝑖𝑚𝑝2

<!-- b000280 | prose | pages [9] -->
𝐸𝑀𝑅=

<!-- b000281 | furniture | pages [9] -->


<!-- b000282 | prose | pages [9] -->
where:

<!-- b000283 | prose | pages [9] -->
Mp     projectile mass (i.e. debris)

<!-- b000284 | prose | pages [9] -->
(4.2.2) 𝑀𝑡

<!-- b000285 | prose | pages [9] -->
Vimp    impact velocity (i.e. relative velocity between the projectile and target) Mt     target mass (i.e. the spacecraft)

<!-- b000286 | furniture | pages [9] -->


<!-- b000287 | furniture | pages [9] -->


<!-- b000288 | furniture | pages [10] -->
Team  #52221                                                              Page 9 of 23

<!-- b000289 | prose | pages [10] -->
The threshold for a catastrophic collision (EMR)cc is usually assumed to be[8]

<!-- b000290 | furniture | pages [10] -->


<!-- b000291 | prose | pages [10] -->
EMR ≥ (EMR)cc = 40J/g                        (4.2.3)

<!-- b000292 | furniture | pages [10] -->


<!-- b000293 | prose | pages [10] -->
Plugging formula 4.2.2 into the equation 4.2.3 and a standard projectile we obtain:

<!-- b000294 | furniture | pages [10] -->


<!-- b000295 | prose | pages [10] -->
𝐴𝑝

<!-- b000296 | prose | pages [10] -->
8

<!-- b000297 | prose | pages [10] -->
𝐷𝑝≥√

<!-- b000298 | prose | pages [10] -->
𝜋(

<!-- b000299 | prose | pages [10] -->
𝑀𝑝)

<!-- b000300 | prose | pages [10] -->
𝑠𝑡𝑑

<!-- b000301 | prose | pages [10] -->
where: 𝐷𝑝   diameter of debris 𝐷𝑝,𝑐  diameter threshold

<!-- b000302 | prose | pages [10] -->
𝐴𝑝

<!-- b000303 | prose | pages [10] -->
(𝐸𝑀𝑅)𝑐𝑐 𝑀𝑡

<!-- b000304 | prose | pages [10] -->
= 𝐷𝑝,𝑐                     (4.2.4) 𝑉𝑖𝑚𝑝2

<!-- b000305 | prose | pages [10] -->
area-to-mass ratio,(Ap/Mp)std = 0,01 m2/kg

<!-- b000306 | prose | pages [10] -->
(

<!-- b000307 | prose | pages [10] -->
𝑀𝑝)

<!-- b000308 | prose | pages [10] -->
𝑠𝑡𝑑

<!-- b000309 | furniture | pages [10] -->


<!-- b000310 | prose | pages [10] -->
Then we can calculate 𝑃𝑖𝑛 by:

<!-- b000311 | furniture | pages [10] -->


<!-- b000312 | prose | pages [10] -->
𝑁

<!-- b000313 | prose | pages [10] -->
𝑃𝑖𝑛= ∑ 𝐹𝑗

<!-- b000314 | prose | pages [10] -->
𝑗=1

<!-- b000315 | furniture | pages [10] -->


<!-- b000316 | prose | pages [10] -->
𝐴𝑝

<!-- b000317 | prose | pages [10] -->
8

<!-- b000318 | prose | pages [10] -->
(𝐸𝑀𝑅)𝑐𝑐 𝑀𝑡

<!-- b000319 | prose | pages [10] -->
where 𝐷𝑝,𝑗< √

<!-- b000320 | prose | pages [10] -->
𝜋(

<!-- b000321 | prose | pages [10] -->
𝑀𝑝)

<!-- b000322 | prose | pages [10] -->
. 𝑉𝑖𝑚𝑝2

<!-- b000323 | prose | pages [10] -->
𝑠𝑡𝑑

<!-- b000324 | furniture | pages [10] -->


<!-- b000325 | furniture | pages [10] -->


<!-- b000326 | heading | pages [10] -->
5  Premium Rate

<!-- b000327 | heading | pages [10] -->
5.1  Traditional Model

<!-- b000328 | furniture | pages [10] -->


<!-- b000329 | prose | pages [10] -->
𝜋 𝜋

<!-- b000330 | prose | pages [10] -->
4 (𝐷𝑡+ 𝐷𝑝,𝑗)2 (4.2.5)

<!-- b000331 | prose | pages [10] -->
According to traditional insurance model, the premium we expect depends on the premium rate, which is [9]

<!-- b000332 | prose | pages [10] -->
𝐶𝑝 𝐶𝑧× 100%                               (5.1.1)

<!-- b000333 | prose | pages [10] -->
𝛼=

<!-- b000334 | prose | pages [10] -->
where:

<!-- b000335 | prose | pages [10] -->
𝛼    premium rate 𝐶𝑝   total claims

<!-- b000336 | prose | pages [10] -->
𝐶𝑧   total premium

<!-- b000337 | furniture | pages [10] -->


<!-- b000338 | prose | pages [10] -->
It’s obvious that 𝐶𝑝= 𝐶𝑧× 𝛼                                                   (5.1.2) Approximately, the premium rate can be also written as [9]:

<!-- b000339 | furniture | pages [10] -->


<!-- b000340 | furniture | pages [10] -->


<!-- b000341 | prose | pages [10] -->
α ≈(1.2~1.5)𝛽                               (5.1.3)

<!-- b000342 | furniture | pages [10] -->


<!-- b000343 | prose | pages [10] -->
where 𝛽 refers to total failure rate. Then we can get the expected value of the final profit E:

<!-- b000344 | furniture | pages [10] -->


<!-- b000345 | furniture | pages [11] -->
Team  #52221                                                              Page 10 of 23

<!-- b000346 | furniture | pages [11] -->


<!-- b000347 | prose | pages [11] -->
𝐸= 𝐶𝑧× (1 −𝛽) −𝐶𝑝× 𝛽                       (5.1.4)

<!-- b000348 | furniture | pages [11] -->


<!-- b000349 | prose | pages [11] -->
What calls for special attention is that 𝛽 is not the actual failure probability 𝛽∗. The 𝛽∗ depends on every aspect of launching procedure and the whole environment of the space. While 𝛽 comes from statistical method, that is, the total number of failure cases divided by the total number of spacecraft launched. Due to the fact that the amount of the spacecraft launched is not large enough, the laws of large number fail. So 𝛽 usually differs a lot from 𝛽∗. And that’s the reason why the space insurance market is still volatile and reported a loss in 2013. And it was only marginally profitable to insurers in 2014[5].

<!-- b000350 | furniture | pages [11] -->


<!-- b000351 | heading | pages [11] -->
5.2  Improved Model

<!-- b000352 | furniture | pages [11] -->


<!-- b000353 | prose | pages [11] -->
In our business model---debris collision insurance, we only pay for the claims when the failure is caused by debris collision. Therefore the tradition model does not suit well to our situation, and we need a new method to evaluate premium rate.

<!-- b000354 | prose | pages [11] -->
It’s rational to assume that our failure rate 𝛽̂ is equal to 𝑃𝑒:

<!-- b000355 | furniture | pages [11] -->


<!-- b000356 | prose | pages [11] -->
𝛽̂ = 𝑃𝑒                               (5.2.1)

<!-- b000357 | furniture | pages [11] -->


<!-- b000358 | prose | pages [11] -->
Internationally applied space insurance premium rate is about 8% [9]. According to ORDEM 2000 𝑃𝑐 ranges from 10−5~10−3.Given that 10−3 refers to the hardest-hit areas, so the premium rate here should be higher than other areas, and rate of change of premium rate should lower than other areas. Meanwhile our insurance only covers the damage caused by debris collision, so our premium rate should lower than generally applied insurance premium. Fully considering those characters above, we establish a new premium rate model:

<!-- b000359 | furniture | pages [11] -->


<!-- b000360 | prose | pages [11] -->
α = (8 + 𝑙𝑜𝑔10𝛽̂)/100                          (5.2.2)

<!-- b000361 | furniture | pages [11] -->


<!-- b000362 | caption | pages [11] -->
Figure 6 shows how premium rate changes with the failure rate 𝛽̂ in our new premium model.

<!-- b000363 | furniture | pages [11] -->


<!-- b000364 | furniture | pages [11] -->


<!-- b000365 | furniture | pages [11] -->


<!-- b000366 | furniture | pages [11] -->


<!-- b000367 | furniture | pages [11] -->


<!-- b000368 | furniture | pages [11] -->


<!-- b000369 | furniture | pages [11] -->


<!-- b000370 | furniture | pages [11] -->


<!-- b000371 | furniture | pages [11] -->


<!-- b000372 | furniture | pages [11] -->


<!-- b000373 | furniture | pages [11] -->


<!-- b000374 | furniture | pages [11] -->


<!-- b000375 | furniture | pages [11] -->


<!-- b000376 | furniture | pages [11] -->


<!-- b000377 | furniture | pages [11] -->


<!-- b000378 | caption | pages [11] -->
Figure 6: Premium Rate Model

<!-- b000379 | furniture | pages [11] -->


<!-- b000380 | furniture | pages [11] -->


<!-- b000381 | furniture | pages [12] -->
Team  #52221                                                              Page 11 of 23

<!-- b000382 | prose | pages [12] -->
Now we suppose a critical failure probability 𝛾. When 𝛽̂ > 𝛾 we then take ADR measures and make 𝛽̂ smaller than 𝛾, if not, we do not have to take any measures to reduce the collision probability 𝑃𝑐. Then the expected final profit E is

<!-- b000383 | furniture | pages [12] -->


<!-- b000384 | prose | pages [12] -->
𝐸= 𝐶𝑧× (1 −𝛾) −𝐶𝑝× 𝛾−𝑐𝑜𝑠𝑡(𝛽̂,𝛾, 𝑡)                (5.2.3) where:

<!-- b000385 | furniture | pages [12] -->


<!-- b000386 | prose | pages [12] -->
𝑐𝑜𝑠𝑡(𝛽̂,𝛾, 𝑡) = 𝑣𝑎𝑙𝑢𝑒(𝑠𝑡𝑟𝑎𝑡𝑒𝑔𝑦) + 𝑓𝑒𝑒(𝑠𝑡𝑟𝑎𝑡𝑒𝑔𝑦, 𝛽̂, 𝛾, 𝑡)        (5.2.4)

<!-- b000387 | furniture | pages [12] -->


<!-- b000388 | prose | pages [12] -->
The 𝑐𝑜𝑠𝑡(𝛽̂,𝛾, 𝑡) represents the money we should pay for the ADR, including manufacturing costs (𝑣𝑎𝑙𝑢𝑒) and launch costs (𝑓𝑒𝑒). Because the ADR technologies we need has already exist, we don’t take research cost into consideration.

<!-- b000389 | furniture | pages [12] -->


<!-- b000390 | heading | pages [12] -->
6  Strategy of ADR

<!-- b000391 | furniture | pages [12] -->


<!-- b000392 | prose | pages [12] -->
By now, we have solved the problem of how much income (premium) we have.

<!-- b000393 | prose | pages [12] -->
How much cost we should pay for is the next question. This is shown in fig.7 .

<!-- b000394 | furniture | pages [12] -->


<!-- b000395 | furniture | pages [12] -->


<!-- b000396 | furniture | pages [12] -->


<!-- b000397 | furniture | pages [12] -->


<!-- b000398 | furniture | pages [12] -->


<!-- b000399 | furniture | pages [12] -->


<!-- b000400 | furniture | pages [12] -->


<!-- b000401 | furniture | pages [12] -->


<!-- b000402 | furniture | pages [12] -->


<!-- b000403 | furniture | pages [12] -->


<!-- b000404 | furniture | pages [12] -->


<!-- b000405 | furniture | pages [12] -->


<!-- b000406 | furniture | pages [12] -->


<!-- b000407 | furniture | pages [12] -->


<!-- b000408 | caption | pages [12] -->
Figure 7: Model Schematic Diagram

<!-- b000409 | furniture | pages [12] -->


<!-- b000410 | furniture | pages [12] -->


<!-- b000411 | prose | pages [12] -->
The aim of ADR is to reduce the failure probability and claim probability. We take two steps to achieve this goal. Firstly, we should determine a size limit for the debris to be removed. Secondly we should choose a suitable ADR strategy for removing the debris with certain range of size.

<!-- b000412 | furniture | pages [12] -->


<!-- b000413 | heading | pages [12] -->
6.1  First Step

<!-- b000414 | furniture | pages [12] -->


<!-- b000415 | prose | pages [12] -->
As discussed in Section 4, the collision probability is expressed as a form of sum:

<!-- b000416 | furniture | pages [12] -->


<!-- b000417 | prose | pages [12] -->
𝜋 𝑁 4 (𝐷𝑡+ 𝐷𝑝,𝑗)2

<!-- b000418 | prose | pages [12] -->
𝑃𝑐,𝑦𝑟= ∑

<!-- b000419 | prose | pages [12] -->
(4.1.2)

<!-- b000420 | prose | pages [12] -->
𝐹̅𝑗

<!-- b000421 | prose | pages [12] -->
𝑗=1

<!-- b000422 | furniture | pages [12] -->


<!-- b000423 | furniture | pages [12] -->


<!-- b000424 | furniture | pages [13] -->
Team  #52221                                                              Page 12 of 23

<!-- b000425 | prose | pages [13] -->
Every individual term in the expression stands for the contribution of the debris with a size range from Dp,j to Dp,j+1 to the 𝑃𝑐,𝑦𝑟.

<!-- b000426 | prose | pages [13] -->
In order to reduce the collision probability effectively, we can choose one or more terms in the expression who contributes the most to the probability. Usually, a large 𝐹̅𝑗 means a small 𝐷𝑝,𝑗, so the

<!-- b000427 | prose | pages [13] -->
𝜋 4 (𝐷𝑡+ 𝐷𝑝,𝑗)2 is not a monotone function.

<!-- b000428 | prose | pages [13] -->
𝐹̅𝑗

<!-- b000429 | prose | pages [13] -->
𝜋 4 (𝐷𝑡+ 𝐷𝑝,𝑗)2 one by one, till the Pe becomes smaller

<!-- b000430 | prose | pages [13] -->
We remove the terms with the biggest 𝐹̅𝑗

<!-- b000431 | prose | pages [13] -->
than 𝛾.

<!-- b000432 | furniture | pages [13] -->


<!-- b000433 | heading | pages [13] -->
6.2  Second Step: Fuzzy Comprehensive Evaluation

<!-- b000434 | furniture | pages [13] -->


<!-- b000435 | prose | pages [13] -->
With a certain range of the size of the debris decided, we should choose a suitable strategy of ADR to remove them. The fuzzy comprehensive evaluation is a good method to do so. Fuzzy comprehensive evaluation method is a mathematical method to comprehensively evaluate things that are not easy to be clearly defined in the real world by using the thinking and methods of fuzzy mathematics. The method comprehensively evaluate systems by using fuzzy set theory of fuzzy mathematics. Through the fuzzy evaluation information about the priority of various alternatives can be achieved as a reference for decision makers to make decision [10]. Therefore we choose this method to achieve our goal.

<!-- b000436 | furniture | pages [13] -->


<!-- b000437 | heading | pages [13] -->
6.2.1  The ADR Measures

<!-- b000438 | furniture | pages [13] -->


<!-- b000439 | prose | pages [13] -->
Active Debris Removal (ADR) is a very effective solution to reduce the collision occurrence possibility. After a series of method comparison, we choose four kind of candidate ADR technologies. ·Ground-based Laser: Using high-powered laser pulses fired from the ground, the system would create a small plasma jet emanating from the piece of junk itself, essentially turning each piece of debris into its own laser-powered rocket that would remove itself from orbit [11]. ·Space-based Laser: Using high-powered laser pulses fired from the space. ·Microsatellite: The microsatellite will use the camera equipped on it to track the space debris. Then it will grip the debris, slow down and fall into the atmosphere together. ·Large Satellite: The large satellite has several thin metal meshes which are thousands of meters. The mesh grip the debris with the robotic arm. When the mesh is full, it will be separated from the satellite and fall into the atmosphere with the debris it collects.

<!-- b000440 | furniture | pages [13] -->


<!-- b000441 | heading | pages [13] -->
6.2.2  Implementation of Fuzzy Comprehensive Evaluation

<!-- b000442 | furniture | pages [13] -->


<!-- b000443 | prose | pages [13] -->
We choose manufacture costs, cost of using, fitness (applicability to remove debris in certain size) and time consuming as evaluation factors. The weight of each evaluation factor is

<!-- b000444 | prose | pages [13] -->
A= [0.15,0.35,0.2,0.3] The judge decision-making Matrix is R. Then the calculation comes to:  B = A⋅ R.

<!-- b000445 | furniture | pages [13] -->


<!-- b000446 | furniture | pages [13] -->


<!-- b000447 | furniture | pages [13] -->


<!-- b000448 | furniture | pages [13] -->


<!-- b000449 | furniture | pages [14] -->
Team  #52221                                                              Page 13 of 23

<!-- b000450 | prose | pages [14] -->
Non-high-risk area:

<!-- b000451 | prose | pages [14] -->
Small-sized Debris:

<!-- b000452 | furniture | pages [14] -->


<!-- b000453 | furniture | pages [14] -->


<!-- b000454 | prose | pages [14] -->
Cost of manufacture

<!-- b000455 | prose | pages [14] -->
Ground-based Laser 0.7 Space-based Laser 0.2 Microsatellite 1.0 Large Satellite 0.2

<!-- b000456 | furniture | pages [14] -->


<!-- b000457 | prose | pages [14] -->
Cost of using Fitness Time consuming

<!-- b000458 | prose | pages [14] -->
1.0 0.8 0.8 0.6 0.7 0.6 0.7 0.8 0.2 0.5 0.5 0.5

<!-- b000459 | prose | pages [14] -->
Then, B = [0.855, 0.560, 0.615, 0.455]. The ground-based laser is the best method to remove small-sized debris. The microsatellite comes second.

<!-- b000460 | furniture | pages [14] -->


<!-- b000461 | prose | pages [14] -->
Medium-sized Debris:

<!-- b000462 | furniture | pages [14] -->


<!-- b000463 | prose | pages [14] -->
With debris getting larger, both cost and time consuming for laser increase. Therefore:

<!-- b000464 | furniture | pages [14] -->


<!-- b000465 | prose | pages [14] -->
Cost of manufacture

<!-- b000466 | prose | pages [14] -->
Ground-based Laser 0.7 Space-based Laser 0.2 Microsatellite 1.0 Large Satellite 0.2

<!-- b000467 | furniture | pages [14] -->


<!-- b000468 | prose | pages [14] -->
Cost of using Fitness Time consuming

<!-- b000469 | prose | pages [14] -->
0.8 0.5 0.7 0.6 0.8 0.6 0.7 0.3 0.2 0.5 0.7 0.5

<!-- b000470 | prose | pages [14] -->
Then, B = [0.695, 0.580, 0.515, 0.460]. The ground-based laser is the best method to remove medium-sized debris.

<!-- b000471 | furniture | pages [14] -->


<!-- b000472 | prose | pages [14] -->
Large-sized Debris:

<!-- b000473 | furniture | pages [14] -->


<!-- b000474 | prose | pages [14] -->
Microsatellites are not suitable for large debris, so we don’t take it into consideration.

<!-- b000475 | furniture | pages [14] -->


<!-- b000476 | prose | pages [14] -->
Cost of manufacture

<!-- b000477 | prose | pages [14] -->
Ground-based Laser 0.7 Space-based Laser 0.2 Large Satellite 0.2

<!-- b000478 | furniture | pages [14] -->


<!-- b000479 | prose | pages [14] -->
Cost of using Fitness Time consuming

<!-- b000480 | prose | pages [14] -->
0.5 0.2 0.5 0.4 0.6 0.5 0.4 0.8 0.5

<!-- b000481 | prose | pages [14] -->
Then, B = [0.470,0.440,0.480]. The large satellite is the best method to remove large-sized debris.

<!-- b000482 | furniture | pages [14] -->


<!-- b000483 | furniture | pages [14] -->


<!-- b000484 | prose | pages [14] -->
Hardest-hit areas (700-1000 kilometers and 1400-1600 kilometers from earth surface):

<!-- b000485 | furniture | pages [14] -->


<!-- b000486 | prose | pages [14] -->
The debris number in this area are larger than in other areas, so the manufacture costs of microsatellite and the using costs of laser should be paid extra attention to.

<!-- b000487 | furniture | pages [14] -->


<!-- b000488 | prose | pages [14] -->
Small-sized Debris:

<!-- b000489 | furniture | pages [14] -->


<!-- b000490 | furniture | pages [14] -->


<!-- b000491 | furniture | pages [15] -->
Team  #52221                                                              Page 14 of 23

<!-- b000492 | furniture | pages [15] -->


<!-- b000493 | prose | pages [15] -->
Cost of manufacture

<!-- b000494 | prose | pages [15] -->
Ground-based Laser 0.4 Space-based Laser 0.2 Microsatellite 1.0 Large Satellite 0.2

<!-- b000495 | furniture | pages [15] -->


<!-- b000496 | prose | pages [15] -->
Cost of using Fitness Time consuming

<!-- b000497 | prose | pages [15] -->
0.5 0.8 0.4 0.4 0.7 0.4 0.4 0.8 0.1 0.5 0.5 0.4

<!-- b000498 | prose | pages [15] -->
Then, B = [0.515, 0.430, 0.480, 0.425]. The ground-based laser is the best method for removing small-sized debris. However, based on the fact that the debris number is very large in hardest-hit areas, the advantages of the ground-based laser are no longer obvious. The satellites may be more suitable for this situation.

<!-- b000499 | furniture | pages [15] -->


<!-- b000500 | prose | pages [15] -->
Medium-sized Debris:

<!-- b000501 | furniture | pages [15] -->


<!-- b000502 | furniture | pages [15] -->


<!-- b000503 | prose | pages [15] -->
Cost of manufacture

<!-- b000504 | prose | pages [15] -->
Ground-based Laser 0.4 Space-based Laser 0.2 Microsatellite 1.0 Large Satellite 0.2

<!-- b000505 | furniture | pages [15] -->


<!-- b000506 | prose | pages [15] -->
Cost of using Fitness Time consuming

<!-- b000507 | prose | pages [15] -->
0.4 0.5 0.4 0.3 0.7 0.3 0.4 0.3 0.1 0.5 0.7 0.4

<!-- b000508 | prose | pages [15] -->
Then, B = [0.420, 0.385, 0.380, 0.465]. The large satellite is the best method to remove medium-sized debris.

<!-- b000509 | furniture | pages [15] -->


<!-- b000510 | prose | pages [15] -->
Large-sized Debris:

<!-- b000511 | furniture | pages [15] -->


<!-- b000512 | prose | pages [15] -->
Microsatellites are not suitable for large debris, so we don’t take it into consideration.

<!-- b000513 | furniture | pages [15] -->


<!-- b000514 | furniture | pages [15] -->


<!-- b000515 | prose | pages [15] -->
Cost of manufacture

<!-- b000516 | prose | pages [15] -->
Ground-based Laser 0.4 Space-based Laser 0.2 Large Satellite 0.2

<!-- b000517 | furniture | pages [15] -->


<!-- b000518 | prose | pages [15] -->
Cost of using Fitness Time consuming

<!-- b000519 | prose | pages [15] -->
0.2 0.2 0.3 0.2 0.6 0.3 0.4 0.8 0.3

<!-- b000520 | prose | pages [15] -->
Then, B = [0.260, 0.310, 0.420]. The large satellite is the best method to remove large-sized debris.

<!-- b000521 | furniture | pages [15] -->


<!-- b000522 | heading | pages [15] -->
6.2.3  Conclusion

<!-- b000523 | furniture | pages [15] -->


<!-- b000524 | prose | pages [15] -->
From the results above, we can come to a conclusion that laser has the best applicability in most situation. However laser is a little regionally restricted. Though large satellite has a high cost, it has the features as being large in capacity. A large satellite can bring 100 nets with it and is cost-effective.

<!-- b000525 | furniture | pages [15] -->


<!-- b000526 | heading | pages [15] -->
7  The Impact of Insurance Duration (Time)

<!-- b000527 | furniture | pages [15] -->


<!-- b000528 | prose | pages [15] -->
The debris distribution data from ORDEM varies with time and those data determined both

<!-- b000529 | furniture | pages [15] -->


<!-- b000530 | furniture | pages [16] -->
Team  #52221                                                              Page 15 of 23

<!-- b000531 | prose | pages [16] -->
premium rate and ADR strategy, so our model is a strongly time- dependent one.

<!-- b000532 | prose | pages [16] -->
From the plot below, we can find that the number of debris impacts increases obviously with the time passing by. Which means that, if the satellite owners (our customers) buy a longer-duration insurance from us, then the collision probability will increase which leads to a higher premium.

<!-- b000533 | prose | pages [16] -->
The further analysis will be made in section 9.

<!-- b000534 | furniture | pages [16] -->


<!-- b000535 | furniture | pages [16] -->


<!-- b000536 | prose | pages [16] -->
Figure 8

<!-- b000537 | furniture | pages [16] -->


<!-- b000538 | heading | pages [16] -->
8  Model Implementation and Economy Validation

<!-- b000539 | furniture | pages [16] -->


<!-- b000540 | prose | pages [16] -->
We implement our model successfully via MATLAB and DAS 2.0, and simulate three typical situations.

<!-- b000541 | prose | pages [16] -->
Firstly, we focus on the hardest-hit area. Suppose that the owner of the satellite wants to buy insurance with a premium of 7.26million dollars (comes from calculation) and duration for 5 years. The satellite is 1m in length and 30kg in weight and costs half billion dollars. Assume that the collisions are independent from each other.

<!-- b000542 | prose | pages [16] -->
Here comes the diagram showing the flux of the different-sized debris:

<!-- b000543 | furniture | pages [16] -->


<!-- b000544 | furniture | pages [16] -->


<!-- b000545 | furniture | pages [16] -->


<!-- b000546 | furniture | pages [16] -->


<!-- b000547 | furniture | pages [16] -->


<!-- b000548 | furniture | pages [16] -->


<!-- b000549 | furniture | pages [16] -->


<!-- b000550 | furniture | pages [16] -->


<!-- b000551 | furniture | pages [16] -->


<!-- b000552 | furniture | pages [16] -->


<!-- b000553 | furniture | pages [16] -->


<!-- b000554 | furniture | pages [16] -->


<!-- b000555 | furniture | pages [16] -->


<!-- b000556 | furniture | pages [16] -->


<!-- b000557 | prose | pages [16] -->
Figure 9

<!-- b000558 | furniture | pages [16] -->


<!-- b000559 | furniture | pages [17] -->
Team  #52221                                                              Page 16 of 23

<!-- b000560 | prose | pages [17] -->
Based on the calculation, the 𝐷𝑝,𝑐 is 0.39cm and the effective probability of the collision is 0.695‰. We can figure out that the insurance premium rate is 4.84%.

<!-- b000561 | prose | pages [17] -->
Our company aims to cut down the probability by one order of magnitude. Based on our model, we are supposed to clean the debris range from 0.39cm to 1.24cm in size.

<!-- b000562 | prose | pages [17] -->
The result of fuzzy comprehensive evaluation indicates that we should choose ground-based lasers and large satellites to remove the debris in such size. After the ADR, the probability of the collision reduces to 0.0738‰.

<!-- b000563 | prose | pages [17] -->
In this situation, our company could earn 3.04 million dollars.

<!-- b000564 | furniture | pages [17] -->


<!-- b000565 | furniture | pages [17] -->


<!-- b000566 | prose | pages [17] -->
Then, we focus on the space station which runs above 400km. Suppose that the space station is 4m in length and 20000kg in weight, which costs 100 billion dollars to build and launch. The owner of space station wants to buy insurance with a premium of 981 million dollars (comes from calculation) and duration for 5 years.

<!-- b000567 | furniture | pages [17] -->


<!-- b000568 | furniture | pages [17] -->


<!-- b000569 | furniture | pages [17] -->


<!-- b000570 | furniture | pages [17] -->


<!-- b000571 | furniture | pages [17] -->


<!-- b000572 | furniture | pages [17] -->


<!-- b000573 | furniture | pages [17] -->


<!-- b000574 | furniture | pages [17] -->


<!-- b000575 | furniture | pages [17] -->


<!-- b000576 | furniture | pages [17] -->


<!-- b000577 | furniture | pages [17] -->


<!-- b000578 | furniture | pages [17] -->


<!-- b000579 | furniture | pages [17] -->


<!-- b000580 | furniture | pages [17] -->


<!-- b000581 | furniture | pages [17] -->


<!-- b000582 | furniture | pages [17] -->


<!-- b000583 | prose | pages [17] -->
Figure 10

<!-- b000584 | furniture | pages [17] -->


<!-- b000585 | furniture | pages [17] -->


<!-- b000586 | prose | pages [17] -->
Based on the calculation, the 𝐷𝑝,𝑐 is 7.15cm and the effective probability of the collision is 0.0188‰. The insurance premium rate is 3.27%.

<!-- b000587 | prose | pages [17] -->
Based on our model, we are supposed to clean the debris range from 7.15cm to 71.5cm in size.The result of fuzzy comprehensive evaluation indicates that we should choose large satellites to remove the debris in such size. After the ADR, the probability of the collision is down to 0.0016‰.

<!-- b000588 | prose | pages [17] -->
In this situation, our company could make a profit of 780 million dollars.

<!-- b000589 | furniture | pages [17] -->


<!-- b000590 | furniture | pages [17] -->


<!-- b000591 | prose | pages [17] -->
Finally, we move our attention to satellites which runs beyond the hardest-hit area. Other conditions are the same to the first situation mentioned above.

<!-- b000592 | prose | pages [17] -->
Here comes the debris distribution:

<!-- b000593 | furniture | pages [17] -->


<!-- b000594 | furniture | pages [17] -->


<!-- b000595 | furniture | pages [17] -->


<!-- b000596 | furniture | pages [17] -->


<!-- b000597 | furniture | pages [17] -->


<!-- b000598 | furniture | pages [18] -->
Team  #52221                                                              Page 17 of 23

<!-- b000599 | furniture | pages [18] -->


<!-- b000600 | furniture | pages [18] -->


<!-- b000601 | furniture | pages [18] -->


<!-- b000602 | furniture | pages [18] -->


<!-- b000603 | furniture | pages [18] -->


<!-- b000604 | furniture | pages [18] -->


<!-- b000605 | furniture | pages [18] -->


<!-- b000606 | furniture | pages [18] -->


<!-- b000607 | furniture | pages [18] -->


<!-- b000608 | furniture | pages [18] -->


<!-- b000609 | furniture | pages [18] -->


<!-- b000610 | furniture | pages [18] -->


<!-- b000611 | furniture | pages [18] -->


<!-- b000612 | furniture | pages [18] -->


<!-- b000613 | furniture | pages [18] -->


<!-- b000614 | furniture | pages [18] -->


<!-- b000615 | furniture | pages [18] -->


<!-- b000616 | prose | pages [18] -->
Figure 11

<!-- b000617 | furniture | pages [18] -->


<!-- b000618 | furniture | pages [18] -->


<!-- b000619 | prose | pages [18] -->
In this situation, the 𝐷𝑝,𝑐 is 0.62cm and the effective probability of the collision is 0.0128‰. The insurance premium rate turns out to be 3.11%

<!-- b000620 | prose | pages [18] -->
Our company aims to cut down the probability by one order of magnitude. Based on our model, we are supposed to clean the debris range from 0.62cm to 1.96cm in size.The result of fuzzy comprehensive evaluation indicates that we should choose laser and microsatellite to remove the debris in such size. After the ADR, the probability of the collision is down to 0.0012‰. In this situation, our company could make a profit of 3.66 million dollars.

<!-- b000621 | furniture | pages [18] -->


<!-- b000622 | prose | pages [18] -->
In conclusion, our model has an impressing profitability. Besides, our insurance premium is much lower than other space insurance companies and shows a good competitiveness against other companies.

<!-- b000623 | furniture | pages [18] -->


<!-- b000624 | prose | pages [18] -->
9  “ What If ” and Sensitive Analysis

<!-- b000625 | furniture | pages [18] -->


<!-- b000626 | prose | pages [18] -->
There must be a lot of “What if” scenarios happen when the whole business is running. These “What if” scenarios can be reflected in the fluctuation of important parameter of our model. Therefore, we will list three important “What if” scenarios and do sensitive analysis at the same time.

<!-- b000627 | furniture | pages [18] -->


<!-- b000628 | prose | pages [18] -->
Fluctuation in premium rate: If the failure rate fluctuates, causing space insurance market to volatile. We should also make adjustment to the market to change our premium rate. In the meantime, the general trend of premium rate should keep the same. Shown in figure, our model can handle this situation well.

<!-- b000629 | furniture | pages [18] -->


<!-- b000630 | furniture | pages [18] -->


<!-- b000631 | furniture | pages [18] -->


<!-- b000632 | furniture | pages [18] -->


<!-- b000633 | furniture | pages [18] -->


<!-- b000634 | furniture | pages [19] -->
Team  #52221                                                              Page 18 of 23

<!-- b000635 | furniture | pages [19] -->


<!-- b000636 | furniture | pages [19] -->


<!-- b000637 | furniture | pages [19] -->


<!-- b000638 | furniture | pages [19] -->


<!-- b000639 | furniture | pages [19] -->


<!-- b000640 | furniture | pages [19] -->


<!-- b000641 | furniture | pages [19] -->


<!-- b000642 | furniture | pages [19] -->


<!-- b000643 | furniture | pages [19] -->


<!-- b000644 | furniture | pages [19] -->


<!-- b000645 | furniture | pages [19] -->


<!-- b000646 | furniture | pages [19] -->


<!-- b000647 | furniture | pages [19] -->


<!-- b000648 | furniture | pages [19] -->


<!-- b000649 | furniture | pages [19] -->


<!-- b000650 | prose | pages [19] -->
Figure 12

<!-- b000651 | furniture | pages [19] -->


<!-- b000652 | furniture | pages [19] -->


<!-- b000653 | prose | pages [19] -->
Variation in fuzzy evaluation factor: If the technology is advanced, then all the fuzzy evaluation factors will change. Because the judge decision-making matrix is based on the objective data, and the changes of weight of each evaluation factor lead to the changes of the whole strategies. It means that the profit will change obviously. We can’t expect the development of the technology which may cause the changes of the matrix. In a result, the whole evaluation will change greatly. This page will not focus on this.

<!-- b000654 | furniture | pages [19] -->


<!-- b000655 | prose | pages [19] -->
Variation in premium duration: In the real world, the premium duration is not a constant value; it varies with the customers’ needs. The real-life duration usually ranges from one year to ten years. Though our model is a strongly time-dependent one, the ten-year variation won’t affect our model much. The sensitive analysis proves this point directly.

<!-- b000656 | furniture | pages [19] -->


<!-- b000657 | furniture | pages [19] -->


<!-- b000658 | furniture | pages [19] -->


<!-- b000659 | furniture | pages [19] -->


<!-- b000660 | furniture | pages [19] -->


<!-- b000661 | furniture | pages [19] -->


<!-- b000662 | furniture | pages [19] -->


<!-- b000663 | furniture | pages [19] -->


<!-- b000664 | furniture | pages [19] -->


<!-- b000665 | furniture | pages [19] -->


<!-- b000666 | furniture | pages [19] -->


<!-- b000667 | furniture | pages [19] -->


<!-- b000668 | furniture | pages [19] -->


<!-- b000669 | furniture | pages [19] -->


<!-- b000670 | furniture | pages [19] -->


<!-- b000671 | furniture | pages [19] -->


<!-- b000672 | furniture | pages [19] -->


<!-- b000673 | prose | pages [19] -->
Figure 13

<!-- b000674 | furniture | pages [19] -->


<!-- b000675 | furniture | pages [19] -->


<!-- b000676 | furniture | pages [20] -->
Team  #52221                                                              Page 19 of 23

<!-- b000677 | prose | pages [20] -->
Based on the sensitive analysis, our model is very robust. It can face many sorts of challenges and make suitable strategy to deal with various situations.

<!-- b000678 | furniture | pages [20] -->


<!-- b000679 | heading | pages [20] -->
10  Strengths and Weaknesses

<!-- b000680 | furniture | pages [20] -->


<!-- b000681 | prose | pages [20] -->
Like any model, the one present above has its strengths and weakness. Some of the major points are presented below.

<!-- b000682 | furniture | pages [20] -->


<!-- b000683 | heading | pages [20] -->
10.1  Strengths

<!-- b000684 | prose | pages [20] -->
·High accuracy ORDEM 2000 has a large amount of data. The analysis and prediction is based on huge observation data.

<!-- b000685 | furniture | pages [20] -->


<!-- b000686 | prose | pages [20] -->
·A better business model We improved the model of the existing space insurance company from three aspects: (1) Increased a reasonable collision estimation based on space debris model. (2) Designed a strategy to reduce the probabilities of the collision between satellites and debris. (3)Combine the insurance premium rate with the probabilities of the collision.

<!-- b000687 | furniture | pages [20] -->


<!-- b000688 | prose | pages [20] -->
·Good flexibility Thanks to the rational strategy, our model can deal with various kinds of situations.

<!-- b000689 | furniture | pages [20] -->


<!-- b000690 | heading | pages [20] -->
10.2  Weakness

<!-- b000691 | prose | pages [20] -->
·Lack of data Our model is lack of data about the cost of technological products. It means that our profits is evaluated from estimated data.

<!-- b000692 | furniture | pages [20] -->


<!-- b000693 | prose | pages [20] -->
·Ignorance of the orbit inclination angle In our model, we only considered parts of the parameters which are used to describe an orbit, and we ignored the influence of orbit inclination angle. The number of impacts in two orbits with the same altitude but different inclination might be different. This will change the prediction of our model.

<!-- b000694 | furniture | pages [20] -->


<!-- b000695 | prose | pages [20] -->
·Not fully considering the development of technology In our model, the cost for removing space debris is based on current level of technology. With the progress of technology, the cost will be lower. The effect of technology progress should be considered further.

<!-- b000696 | furniture | pages [20] -->


<!-- b000697 | furniture | pages [20] -->


<!-- b000698 | furniture | pages [20] -->


<!-- b000699 | furniture | pages [20] -->


<!-- b000700 | furniture | pages [20] -->


<!-- b000701 | furniture | pages [20] -->


<!-- b000702 | furniture | pages [20] -->


<!-- b000703 | furniture | pages [21] -->
Team  #52221                                                              Page 20 of 23

<!-- b000704 | heading | pages [21] -->
References

<!-- b000705 | references | pages [21] -->
[1] Space Debris and Human Spacecraft, NASA:

<!-- b000706 | references | pages [21] -->
http://www.nasa.gov/mission_pages/station/news/orbital_debris.html

<!-- b000707 | references | pages [21] -->
[2] What Is Orbital Debris? , NASA:

<!-- b000708 | references | pages [21] -->
http://www.nasa.gov/audience/forstudents/k-4/stories/nasa-knows/what-is-orbital-debris-k4.html

<!-- b000709 | references | pages [21] -->
[3] Debris Photo, NASA:

<!-- b000710 | references | pages [21] -->
history.nasa.gov/columbia/debris_pics.html

<!-- b000711 | references | pages [21] -->
[4] The 6th Annual International Conference, 26th February 2015, Moscow

<!-- b000712 | references | pages [21] -->
[5] Medic-Šaric, M, Rastija, V, Singh, V. K, et al. The new NASA Orbital Debris Engineering Model

<!-- b000713 | references | pages [21] -->
ORDEM2000[J]. Psychopharmacology & Therapeutic Values V, 2001, 473(1609-042X):309-313.

<!-- b000714 | references | pages [21] -->
[6] Debris Assessment Software User’s Guide, NASA:

<!-- b000715 | references | pages [21] -->
http://orbitaldebris.jsc.nasa.gov/mitigate/das.html

<!-- b000716 | references | pages [21] -->
[7] Sdunnus H, Beltrami P, Klinkrad H, et al. Comparison of debris flux models[C]. 34th COSPAR

<!-- b000717 | references | pages [21] -->
Scientific Assembly, 2002:1000–1005.

<!-- b000718 | references | pages [21] -->
[8] Space Debris Mitigation Compliance Verification Guidelines, ESA

<!-- b000719 | references | pages [21] -->
[9] Yilin Zhu. Foreign insurance of satellites[J]. Global missile and space,1987,08:34-37.

<!-- b000720 | references | pages [21] -->
[10] Shao C. The Implication of Fuzzy Comprehensive Evaluation Method in Evaluating Internal

<!-- b000721 | references | pages [21] -->
Financial Control of Enterprise[J]. International Business Research, 2009, 2(1):210.

<!-- b000722 | references | pages [21] -->
[11] Gound-Based Laser Cannot to Turn Space Debris into Self-powered Flaming De-orbiting Rockets:

<!-- b000723 | references | pages [21] -->
http://www.popsci.com/technology/article/2011-10/new-space-junk-scheme-turns-debris-small-plasma

<!-- b000724 | references | pages [21] -->
-rockets-remove-themselves-orbit

<!-- b000725 | furniture | pages [21] -->


<!-- b000726 | furniture | pages [21] -->


<!-- b000727 | furniture | pages [21] -->


<!-- b000728 | furniture | pages [21] -->


<!-- b000729 | furniture | pages [21] -->


<!-- b000730 | furniture | pages [21] -->


<!-- b000731 | furniture | pages [21] -->


<!-- b000732 | furniture | pages [21] -->


<!-- b000733 | furniture | pages [21] -->


<!-- b000734 | furniture | pages [21] -->


<!-- b000735 | furniture | pages [21] -->


<!-- b000736 | furniture | pages [21] -->


<!-- b000737 | furniture | pages [21] -->


<!-- b000738 | furniture | pages [21] -->


<!-- b000739 | furniture | pages [22] -->
Team  #52221                                                              Page 21 of 23

<!-- b000740 | heading | pages [22] -->
Executive Summary

<!-- b000741 | prose | pages [22] -->
Problem Background Statement In 1957, the first man-made object was launched into space. From then on, more than 5,000 spacecraft had been launched to Earth-centered orbits of various heights. With the rapid increase of the human aerospace activities, the space debris problem has become more and more serious. Space debris includes nonfunctional spacecraft, fragmentation debris, etc. More than 500,000 pieces of debris are tracked as they orbit the Earth. They all travel at speeds up to 17,500 mph, fast enough for a relatively small piece of orbital debris to damage a satellite or a spacecraft.

<!-- b000742 | furniture | pages [22] -->


<!-- b000743 | prose | pages [22] -->
“The greatest risk to space missions comes from non-trackable debris,” said Nicholas Johnson, NASA chief scientist for orbital debris.

<!-- b000744 | furniture | pages [22] -->


<!-- b000745 | heading | pages [22] -->
Problem Solution

<!-- b000746 | prose | pages [22] -->
Active Debris Removal (ADR) is a very effective solution to reduce the collision occurrence possibility. Many of the space agencies and companies have developed all sorts of ADR technologies. With the increasing number of space debris, the risk induced by space debris is getting higher and its damage might become huge, and the necessity and effectiveness of ADR have been recognized. Many of the space agencies and companies have developed all sorts of ADR technologies.

<!-- b000747 | furniture | pages [22] -->


<!-- b000748 | prose | pages [22] -->
However, even though ADR is effective to lower the risk induced by space debris, ADR cost exceeds the benefit brought by ADR, it is hard to carry out ADR. In order to conquer this situation, we create a new business model, which can both provide commercial benefits and reduce the space debris.

<!-- b000749 | furniture | pages [22] -->


<!-- b000750 | heading | pages [22] -->
Business Model

<!-- b000751 | prose | pages [22] -->
Most of the owners of the satellites tend to cover insurance for their spacecraft in the past decade. Therefore the market of space insurance has grown very large. However，due to not fully considering the increasing debris, the space insurance market is still volatile and reported a loss in 2013. We create a new insurance model under all these backgrounds.

<!-- b000752 | furniture | pages [22] -->


<!-- b000753 | prose | pages [22] -->
We offer the owners of satellites a special space insurance serve which consists of two parts. One is that if any debris collision happens during the insurance duration, we will pay for the claims. In order to reduce the risks of collision which will increase our claims, we will carry out ADR to reduce the probability of debris collision. The model is demonstrated in the figure below:

<!-- b000754 | furniture | pages [22] -->


<!-- b000755 | furniture | pages [22] -->


<!-- b000756 | furniture | pages [22] -->


<!-- b000757 | furniture | pages [22] -->


<!-- b000758 | furniture | pages [22] -->


<!-- b000759 | furniture | pages [22] -->


<!-- b000760 | furniture | pages [22] -->


<!-- b000761 | furniture | pages [22] -->


<!-- b000762 | furniture | pages [22] -->


<!-- b000763 | furniture | pages [22] -->


<!-- b000764 | furniture | pages [22] -->


<!-- b000765 | furniture | pages [22] -->


<!-- b000766 | furniture | pages [22] -->


<!-- b000767 | furniture | pages [22] -->


<!-- b000768 | furniture | pages [23] -->
Team  #52221                                                              Page 22 of 23

<!-- b000769 | prose | pages [23] -->
Using the Matlab and the data from NASA, we did a simulation of our model. The result

<!-- b000770 | heading | pages [23] -->
shows that our model has an impressing profitability and competitiveness against other

<!-- b000771 | prose | pages [23] -->
insurance companies.

<!-- b000772 | furniture | pages [23] -->


<!-- b000773 | prose | pages [23] -->
Active Debris Removal Measurements How to choose the suitable ADR methods among all developed ADR methods is a critical problem, both to our business model and all the space faring parties.

<!-- b000774 | furniture | pages [23] -->


<!-- b000775 | prose | pages [23] -->
We build up a model to determine which ADR methods to be used, considering the manufacture costs, cost of using, applicability to remove the debris in certain size and time consuming of the methods.

<!-- b000776 | furniture | pages [23] -->


<!-- b000777 | prose | pages [23] -->
Based on our model, we can come to a conclusion that laser has the best applicability in most situation. However laser is regionally restricted. Though large satellite has a high cost, it has the features as being large in capacity: a large satellite can bring 100 nets with it, so it is cost-effective.

<!-- b000778 | furniture | pages [23] -->


<!-- b000779 | heading | pages [23] -->
Action Recommendation

<!-- b000780 | prose | pages [23] -->
For the governments, improving space environment is extremely relevant to the space development. Nevertheless, the development costs and the running costs of ADR is very high. According to our work, we recommend high level policy makers to take the following actions:

<!-- b000781 | furniture | pages [23] -->


<!-- b000782 | prose | pages [23] -->
·  Raise the awareness of space debris problem. Prioritize the development of the laser ADR technology and large satellite ADR technology.

<!-- b000783 | furniture | pages [23] -->


<!-- b000784 | prose | pages [23] -->
·  Provide policy support and fund subsidy for the private company related to space debris, such as our company. Encourage private company to participate in improving the space debris environment.

<!-- b000785 | furniture | pages [23] -->

