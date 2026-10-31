# P-A-2018-76271-27d535ab

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000002 | furniture | pages [1] -->
Team Control Number

<!-- b000003 | prose | pages [1] -->
For office use only

<!-- b000004 | prose | pages [1] -->
For office use only

<!-- b000005 | prose | pages [1] -->
76271

<!-- b000006 | prose | pages [1] -->
T1

<!-- b000007 | prose | pages [1] -->
T2

<!-- b000008 | prose | pages [1] -->
F1

<!-- b000009 | prose | pages [1] -->
F2

<!-- b000010 | prose | pages [1] -->
Problem Chosen

<!-- b000011 | prose | pages [1] -->
T3

<!-- b000012 | prose | pages [1] -->
T4

<!-- b000013 | prose | pages [1] -->
F3

<!-- b000014 | prose | pages [1] -->
A A

<!-- b000015 | prose | pages [1] -->
F4

<!-- b000016 | prose | pages [1] -->
. .

<!-- b000017 | title | pages [1] -->
Wave Goodbye to Poor Reception

<!-- b000018 | prose | pages [1] -->
The discovery of High Frequency skywaves in the 1920’s allowed amateur radio enthusiasts, even those with low powered transmitters, to connect over long distances. Now in common use, skywaves allow communication across the turbulent ocean to ships at sea or distant continents by bouncing waves between the ionosphere and the surface of the Earth. We create a model to tackle the challenge of reliable communication, simulating the unpredictability of skywave communication, including uneven ionosphere density and wild reflection off of non-uniform surfaces.

<!-- b000019 | prose | pages [1] -->
In our model, a transmitter at an initial latitude and longitude on a spherical Earth beams a HF signal with a bearing and elevation angle.

<!-- b000020 | prose | pages [1] -->
We use NASA’s International Reference Ionosphere data set to determine the curved  trajectory resulting from refraction of the signal in the ionosphere. We generate small patches of terrain using either a wave simulator or geological elevation  data, which give the signal a new heading as it bounces. This multi-step process allows our model to create the complete path of a skywave signal.

<!-- b000021 | prose | pages [1] -->
Next, we can calculate how the atmosphere and terrain interfere with skywaves, or prevent them from reflecting at all. We model signal strength using the dominant sources of signal gain and loss, and stop propagation when the signal falls below the 10 dB minimum.

<!-- b000022 | prose | pages [1] -->
The transmitter power, receiver sensitivity, and antenna gain provide 170 dB of margin.  The signal weakens along its trajectory because of the free space path loss.  The signal attenuates due to ionospheric absorption and diffuse surface reflection. 

<!-- b000023 | prose | pages [1] -->
We run high-throughput simulations of skywave paths that bounce on calm and turbulent water, as well as smooth and mountainous land. We randomly vary transmitter locations, and test paths from coastal cities to determine the maximum effective transmission distance. To explore our model’s sensitivity, we alter the wave conditions from calm to super-turbulent, increase the transmission power, and change ionospheric density. Lastly, we co-vary the frequency and elevation angle, which we determine to be the most sensitive parameters.

<!-- b000024 | prose | pages [1] -->
We inspect the average number of hops, distance travelled over the Earth, and power lost after bounces to compare our results. For our default frequency and angle of 3 MHz and 30 degrees, respectively, we find a maximum of two hops. The power after a first bounce is 0.72 dB less for turbulent seas compared to calm, and 0.26 dB less for mountainous land compared to smooth. The signals over turbulent ocean reach 1622 km from the shore. We find that depending on location, angle, and frequency, many signals pass through the ionosphere completely or are absorbed before they can bounce. Mapping bounce locations over ionospheric density, we find thatskywave propagation is most effective on the “greyline” between night and day, when absorption is lessened but the ionosphere can still reflect signals.

<!-- b000025 | furniture | pages [2] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000026 | furniture | pages [2] -->
Team #76271

<!-- b000027 | furniture | pages [2] -->
1 of 30

<!-- b000028 | heading | pages [2] -->
Table of Contents

<!-- b000029 | contents | pages [2] -->
I

<!-- b000030 | heading | pages [2] -->
Introduction

<!-- b000031 | prose | pages [2] -->
2 Problem Summary........................................................................................................ 2 A Our Starting Point: Existing Models......................................................................... 2 B Our Model.......................................................................................................................3 C

<!-- b000032 | prose | pages [2] -->
II Background 3 Transmitter and Receiver............................................................................................ 3 A Radio Propagation and Loss....................................................................................... 4 B Skywave Channel Interaction......................................................................................4 C Performance Evaluation...............................................................................................5 D

<!-- b000033 | heading | pages [2] -->
III Assumptions

<!-- b000034 | prose | pages [2] -->
6 Model Assumptions...................................................................................................... 6 A

<!-- b000035 | heading | pages [2] -->
IV Model Development

<!-- b000036 | prose | pages [2] -->
8 Model Construction...................................................................................................... 8 A Model Validation......................................................................................................... 13 B

<!-- b000037 | heading | pages [2] -->
V Model Application

<!-- b000038 | prose | pages [2] -->
13 Part I..............................................................................................................................13 A Part II............................................................................................................................ 14 B Part III...........................................................................................................................14 C

<!-- b000039 | heading | pages [2] -->
VI Results

<!-- b000040 | prose | pages [2] -->
14 Validation......................................................................................................................14 A Part I..............................................................................................................................14 B Part II............................................................................................................................ 15 C Sensitivity Results....................................................................................................... 16 D Part III...........................................................................................................................16 E

<!-- b000041 | prose | pages [2] -->
VIISensitivity Analysis 17 Explore Parameter Space........................................................................................... 17 A

<!-- b000042 | heading | pages [2] -->
VIII Conclusion

<!-- b000043 | prose | pages [2] -->
19 Our Conclusion............................................................................................................ 19 A Strengths.......................................................................................................................20 B Weaknesses and Limiting Assumptions................................................................. 20 C Future Work................................................................................................................. 20 D

<!-- b000044 | prose | pages [2] -->
IX Letter

<!-- b000045 | prose | pages [2] -->
X Appendix

<!-- b000046 | prose | pages [2] -->
21

<!-- b000047 | prose | pages [2] -->
24

<!-- b000048 | furniture | pages [3] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000049 | furniture | pages [3] -->
Team #76271

<!-- b000050 | furniture | pages [3] -->
2 of 30

<!-- b000051 | prose | pages [3] -->
I.

<!-- b000052 | heading | pages [3] -->
Introduction

<!-- b000053 | prose | pages [3] -->
Innovators since the dawn of humankind havesought a more interconnected society by enhancing our ability to communicate over long distances. The history of telecommunica- tion began in 1800 BC, where Chinese soldiers used smoke signals to warn their comrades

<!-- b000054 | prose | pages [3] -->
1 In 1876, Alexander Graham Bell achieved the first

<!-- b000055 | prose | pages [3] -->
up to 500 miles away of an attack.

<!-- b000056 | prose | pages [3] -->
1 While the telephone was a vast improvement over other technologies at

<!-- b000057 | prose | pages [3] -->
telephone call.

<!-- b000058 | prose | pages [3] -->
the time, it required an enormous infrastructure investment and could only be usedwith static stations. A few decades later, the invention of the radio allowed mobile vehicles to communicate over vast distances. In 1914, the International Convention for the Safety of

<!-- b000059 | prose | pages [3] -->
2 Long-distance

<!-- b000060 | prose | pages [3] -->
Life at Sea required shipboard radio stations to be manned 24 hours a day.

<!-- b000061 | prose | pages [3] -->
communicationviaHFradiowavesremainsthemoststablemeansofcommunicationonthe

<!-- b000062 | prose | pages [3] -->
3 If a vessel is not within line-of-sight of a coastal radio station, the

<!-- b000063 | prose | pages [3] -->
open ocean to this day.

<!-- b000064 | prose | pages [3] -->
coastal radio station uses skywave propagation to reflect radio waves off of the ionosphere

<!-- b000065 | prose | pages [3] -->
4 As the radio wave skips between the surface and the ionosphere, it al-

<!-- b000066 | prose | pages [3] -->
and back to Earth.

<!-- b000067 | prose | pages [3] -->
lows the station to communicate beyond the horizon. Despite the unpredictability of radio over long distances, rugged terrain, and volatile seas, it remains an integral component of communication technologies that allow mankind to stay connected.

<!-- b000068 | prose | pages [3] -->
A.

<!-- b000069 | prose | pages [3] -->
Problem Summary

<!-- b000070 | prose | pages [3] -->
• HighFrequency(HF) radio waves,from 3-30MHz, can“hop”between the ionosphere and the surface of the Earth, travelling a greater distance than they could along the ground. When sufficient signal strength is maintained (>10 dB), this enables long distance communication.

<!-- b000071 | prose | pages [3] -->
• If the signal reflects off the ocean surface, it may be affected by changing electrical and magnetic properties of the waves,as well as size, shape, frequency, and direction.

<!-- b000072 | prose | pages [3] -->
• If the signal reflects off the land, it may be affected by terrain variations.

<!-- b000073 | prose | pages [3] -->
• Followingthelossofamulti-hopsignalnecessitatesthemodelingofthetransmitter, propagation between bounces, interaction with the ionosphere, interaction with the Earth’s surface, and ftnally the receiver.

<!-- b000074 | prose | pages [3] -->
B.

<!-- b000075 | prose | pages [3] -->
Our Starting Point: Existing Models

<!-- b000076 | prose | pages [3] -->
Studies of skywave communication have been performed both empirically and theoret- ically by radio operators and electrical engineers in the decades since its creation. These existing models have been refined over time by our increasing understanding of complex physical phenomenon, improved measuring tools, and the capabilities of modern comput- ers.

<!-- b000077 | prose | pages [3] -->
Before developing our own model, we explored the literature to gain a thorough under- standing of existing models, and which complexities they consider. A few arehighlighted here:

<!-- b000078 | prose | pages [3] -->
• Analyticaland geometricmodelsareeasytoimplementbutmakesimplificationsthat degrade accuracy. Examplesinclude:

<!-- b000079 | furniture | pages [4] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000080 | furniture | pages [4] -->
Team #76271

<!-- b000081 | furniture | pages [4] -->
3 of 30

<!-- b000082 | prose | pages [4] -->
– Assuming that the Earth and ionosphere are flat

<!-- b000083 | prose | pages [4] -->
– Treating radio waves as single or double rays

<!-- b000084 | prose | pages [4] -->
– Formula-based surfaces for terrain

<!-- b000085 | prose | pages [4] -->
• Numerical models can achieve high accuracy and take into account dynamiccondi- tions, but they require large data sets and computational power. Examples include:

<!-- b000086 | prose | pages [4] -->
– Using real ionospheric conditions as a function of time

<!-- b000087 | prose | pages [4] -->
– Statistical fading of signals during propagation

<!-- b000088 | heading | pages [4] -->
– Real terrain from geological or oceanic data sources

<!-- b000089 | prose | pages [4] -->
C.

<!-- b000090 | prose | pages [4] -->
Our Model

<!-- b000091 | prose | pages [4] -->
Our modeling approach is rooted in our conclusion that while this prompt focuses on surface hops, a full model of the signal propagation is necessary. The losses in the ionosphere, for instance, directly determine the remaining signal strength for hops. Thus, our model will focus on implementing complexity where detail is most necessary, and simplicity where detail is not necessary, as determined by our research. Wehope to obtain anaccuratetrajectorythroughtheionosphere,aswellasaccurateinteractions with terrain, but simplify free space propagation.

<!-- b000092 | prose | pages [4] -->
The complexity of the propagation of radio waves requires us to evaluate the trade-offs betweenrealismandcomputationtime. Thisimpactsourterrainandionospheremodeling, the types of loss weconsider during propagation, and radio hardware. In the following sec- tions, we will determine which terrain and ionosphere models to use by considering those

<!-- b000093 | prose | pages [4] -->
5 Wewill determine a propagation model that

<!-- b000094 | prose | pages [4] -->
with availabledata and sufficient resolution.

<!-- b000095 | prose | pages [4] -->
includes losses with a significant magnitude compared to the complexity of the necessary calculations. Finally, we will choose general details about our transmitter, receiver and the system antennae in order to determine our signal strength. By programming different sce- narios into the model to link bounces together, we can track the results for the complete path of each signal.

<!-- b000096 | prose | pages [4] -->
II.

<!-- b000097 | heading | pages [4] -->
Background

<!-- b000098 | prose | pages [4] -->
A.

<!-- b000099 | prose | pages [4] -->
Transmitter and Receiver

<!-- b000100 | prose | pages [4] -->
The ending of each signal’s path can be determined by the point that the remaining signal power falls below the 10 decibel threshold. This threshold is called the “link margin,” and is the minimum power required to have a reliable connection.

<!-- b000101 | prose | pages [4] -->
6

<!-- b000102 | prose | pages [4] -->
The 100 W transmit power can be converted to decibels with the equation:

<!-- b000103 | prose | pages [4] -->
dBm = 10log10(P ∗1000/1) = 50 (1)

<!-- b000104 | prose | pages [4] -->
The decibel is a relative calculation, which in this case is taken as a ratio of power to one milliwatt. In decibel form, the power P , positive antenna gain tt, and negative loss L can be added. The combination of these factors is known as the link budget, and willtell

<!-- b000105 | prose | pages [4] -->
6

<!-- b000106 | prose | pages [4] -->
us the received power.

<!-- b000107 | furniture | pages [5] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000108 | furniture | pages [5] -->
Team #76271

<!-- b000109 | furniture | pages [5] -->
4 of 30

<!-- b000110 | prose | pages [5] -->
PRx = PT x + ttT x + L + ttRx (2)

<!-- b000111 | prose | pages [5] -->
Comparing this result to the receiver sensitivity yields the link margin. Because the characteristics of the receiver and the receiving antenna are part of the equation, we will treat the end of the signal path as the theoretical location where the receiver can no longer detect the signal, meaning the budget does not meet the required link margin.

<!-- b000112 | prose | pages [5] -->
Wedeterminethe antenna gainand receiver sensitivityfrom sources about radioequip-

<!-- b000113 | heading | pages [5] -->
6 We will use the

<!-- b000114 | prose | pages [5] -->
ment. A common range of receiver sensitivity is -90 to -120 dBm.

<!-- b000115 | prose | pages [5] -->
highest sensitivity of -120 dBm, because we do not have any requirements for thebit error rate of the system, or how successfully it sends data.

<!-- b000116 | prose | pages [5] -->
A simple type of antenna is a 1.25 wavelength dipole, which has a gain of 5.03 dBi.

<!-- b000117 | prose | pages [5] -->
7

<!-- b000118 | prose | pages [5] -->
This is relative to an isotropic radiator, which radiates equally in all directions. The gain

<!-- b000119 | prose | pages [5] -->
is due to the antenna signal being focused in certain directions, instead of equal. While the physical length might make it impractical to use, mathematically it represents a basic antennacase. Wewillusethesamefigureforboththetransmittingandreceivingantennas.

<!-- b000120 | prose | pages [5] -->
Lastly, the loss will be determined from the propagation of the radio waves. Once all these parameters are calculated, we can determine how far the signal can travel.

<!-- b000121 | prose | pages [5] -->
B.

<!-- b000122 | prose | pages [5] -->
Radio Propagation and Loss

<!-- b000123 | prose | pages [5] -->
Even without any bounces, the received signal power will be less than the transmitted power. This is due to the spreading of the signal as it propagates through space. Instead of travellinginatightbeam,thewavefrontexpandsoutward,losingpower. Thisphenomenon is called free space loss, and increases with distance.

<!-- b000124 | prose | pages [5] -->
8

<!-- b000125 | prose | pages [5] -->
The free space loss only includes the effects of distance, and not any obstacles or interference the signal might encounter. During propagation, the signal also experiences

<!-- b000126 | prose | pages [5] -->
9 Molecules in

<!-- b000127 | prose | pages [5] -->
loss from absorption in the atmosphere, multipath fading, and shadowing.

<!-- b000128 | prose | pages [5] -->
the atmosphere, like water vapor or gaseous oxygen, can attenuate the signal as it passes through. When the signal interacts with objects, it can split into different paths that arrive atdifferenttimeswithdifferentphases,causinginterference. Thisiscalledshadowingwhen it occurs with large objects, and fading when it occurs with small ones.

<!-- b000129 | prose | pages [5] -->
C.

<!-- b000130 | prose | pages [5] -->
Skywave Channel Interaction

<!-- b000131 | prose | pages [5] -->
Skywave radio follows a “channel” as it bounces between the ionosphere and the Earth. Both types of interactions can introduce losses.

<!-- b000132 | prose | pages [5] -->
1.

<!-- b000133 | prose | pages [5] -->
Ionosphere interaction

<!-- b000134 | prose | pages [5] -->
In the ionosphere, radiation from the sun breaks down molecules into ions and elec- trons. These charged particles form layers. The varying electron density causes the index of refraction to decrease with altitude, bending the signals as they travel. The different layers absorb and refract the signal, until it is attenuated, reflected, or passes

<!-- b000135 | prose | pages [5] -->
10 The charged particles in the ionosphere vary with the sunlight,

<!-- b000136 | prose | pages [5] -->
through into space.

<!-- b000137 | furniture | pages [6] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000138 | furniture | pages [6] -->
Team #76271

<!-- b000139 | furniture | pages [6] -->
5 of 30

<!-- b000140 | prose | pages [6] -->
changing between day and nighttime, different seasons, and periods of high and low so-

<!-- b000141 | prose | pages [6] -->
11 The ionosphere also interacts magnetically with radio waves, due to their

<!-- b000142 | prose | pages [6] -->
lar activity.

<!-- b000143 | prose | pages [6] -->
5

<!-- b000144 | prose | pages [6] -->
electromagnetic nature, but this influence is often neglected in models.

<!-- b000145 | prose | pages [6] -->
In relation to skywaves, the changing layers of the ionosphere cause signals to behave

<!-- b000146 | prose | pages [6] -->
10 During the day, the D-layer from 60 to 90

<!-- b000147 | prose | pages [6] -->
differently over time, even hour to hour.

<!-- b000148 | prose | pages [6] -->
km is generated by Lyman radiation and x-rays. This region contributes the most to absorption loss of the signals, especially those with lower frequency, and can prevent them from penetrating further. At night, however, the D region dissipates, leaving the reflective E and F regions from 100 to 400 km. At higher altitudes, the lower density gas takes longer for ions and electrons to recombine, allowing these regions to persist when the sun is not illuminating them. The signals can travel higher without being attenuated, and become refracted more and more, until they reach the point where they arereflected back. The balance between absorption and reflection means that the day/night terminator is an excellent location for skywaves to propagate. The height of the layer that the signals reach determines how far they can hop, with a 2500 km maximum for the E-layer and a 5000km maximumforthe F-layer. Duetothesignificant roleofthe ionosphereinskywave communication, we plan to incorporate its variations with height and location, although

<!-- b000149 | prose | pages [6] -->
10

<!-- b000150 | prose | pages [6] -->
to do so in time would be too computationally expensive.

<!-- b000151 | prose | pages [6] -->
2.

<!-- b000152 | prose | pages [6] -->
Surface interaction

<!-- b000153 | prose | pages [6] -->
On the surface of the Earth, the signal can be reflected, diffracted, or scattered de-

<!-- b000154 | prose | pages [6] -->
9 The ground or water can impact the polarity of the signal, and

<!-- b000155 | prose | pages [6] -->
pending on the terrain.

<!-- b000156 | prose | pages [6] -->
multipath interference is common as signals interact with the ground and with each other. For modeling purposes, the terrain can be mathematically constructed surfaces, or actual

<!-- b000157 | prose | pages [6] -->
12

<!-- b000158 | prose | pages [6] -->
geographical data, which is only available for land models.

<!-- b000159 | prose | pages [6] -->
Diffraction mostly occurs on “knife edge” surfaces or around the edges of objects like

<!-- b000160 | prose | pages [6] -->
5 The

<!-- b000161 | prose | pages [6] -->
buildings, so reflection and scattering are the most dominant for terrain reflection.

<!-- b000162 | prose | pages [6] -->
surface of the Earth has a complex reflectivity coefficient, which depends on the conduc- tivity and permittivity of the medium, and effects the amplitude of the resulting signal due to phase interference. Depending on the roughness of the surface, the reflection will be specular, having a coherent main signal, or diffuse, and spread out in all directions. The comparison of the specular component versus scattering determines the signal loss due to reflection.

<!-- b000163 | prose | pages [6] -->
D.

<!-- b000164 | prose | pages [6] -->
Performance Evaluation

<!-- b000165 | prose | pages [6] -->
At the completion of the signal’s path, we need to determine how it behaved. We first need to find the number of hops, which can simply be calculated bycounting the number of surface interactions before the signal is lost. We will also calculate the arc length across the Earth’s surface, which tells us the overall distance the signal travelled.

<!-- b000166 | prose | pages [6] -->
While it is beneficial to know how many hops were accomplished, we would also like to predict where the signal ends up on the globe. Using the distances and the directions that the signals are reflected, we can determine the latitude and longitude of the final bounces. The density of the signals on the Earth allows us to determine which locations are likely to receive a strong skywave signal.

<!-- b000167 | furniture | pages [7] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000168 | furniture | pages [7] -->
Team #76271

<!-- b000169 | furniture | pages [7] -->
6 of 30

<!-- b000170 | heading | pages [7] -->
Assumptions

<!-- b000171 | prose | pages [7] -->
III.

<!-- b000172 | prose | pages [7] -->
A.

<!-- b000173 | heading | pages [7] -->
Model Assumptions

<!-- b000174 | prose | pages [7] -->
• The signal is not attenuated by rain, fog, and interactions with molecules in the lower

<!-- b000175 | prose | pages [7] -->
8

<!-- b000176 | prose | pages [7] -->
atmosphere. These losses are only significant for frequencies above 1 GHz.

<!-- b000177 | prose | pages [7] -->
• Ground interference is not a significant because the signal is high above theEarth’s surface for most of its path and the interference from the ground is viewed as a minimal impairment until reflection.

<!-- b000178 | prose | pages [7] -->
5 5

<!-- b000179 | prose | pages [7] -->
• The signal is not polarized and the frequency remains the same during travel. These

<!-- b000180 | prose | pages [7] -->
5

<!-- b000181 | prose | pages [7] -->
factors are not as useful for long-distance radio models compared to free space loss.

<!-- b000182 | prose | pages [7] -->
• The ionosphere reaches from 80 km to 2000 km as a spherical shell above a spherical

<!-- b000183 | prose | pages [7] -->
13 The signal only begins to

<!-- b000184 | prose | pages [7] -->
Earth for increased accuracy compared to flat models.

<!-- b000185 | prose | pages [7] -->
be refracted from bottom of the ionosphere.

<!-- b000186 | prose | pages [7] -->
• The ionosphere follows the Reference Standard Ionosphere data from NASA at a

<!-- b000187 | prose | pages [7] -->
13

<!-- b000188 | prose | pages [7] -->
given epoch, so the global data provides information about both night and day.

<!-- b000189 | prose | pages [7] -->
• When modeling the behavior of a radio wave bouncing off of water or land, every bounce will occur on that specified terrain. The coordinates that we use are only to determine the ionosphere data location and the distance travelled on the Earth.

<!-- b000190 | prose | pages [7] -->
• The ocean surface is stationary compared to the speed of light. The signal reflects off of fixed wave shapes.

<!-- b000191 | prose | pages [7] -->
• A calm ocean has wave heights of less than 1 m, while a rough ocean can have swells from 1 to 10 m. A super-turbulent ocean can have a peak swell of 15 m, based on

<!-- b000192 | prose | pages [7] -->
14

<!-- b000193 | prose | pages [7] -->
National Weather Service wave forecasts for a fully-developed sea.

<!-- b000194 | prose | pages [7] -->
• The land consists of topographical features without anysurface coverings, to simplify computations.

<!-- b000195 | prose | pages [7] -->
• A flat land surface is entirely smooth, while a mountainous region may have sharp altitude deviations in the tens of meters.

<!-- b000196 | prose | pages [7] -->
1 wavelength antennae with • The transmitting and receiving antennae are dipole 1

<!-- b000197 | prose | pages [7] -->
4

<!-- b000198 | prose | pages [7] -->
6 The receiver has a sensitivity of -120 dBm.

<!-- b000199 | prose | pages [7] -->
gains of 5.03 dBi each.

<!-- b000200 | prose | pages [7] -->
6

<!-- b000201 | prose | pages [7] -->
• The velocities of the transmitting and receiving antennas, if in motion, are negligible compared to the speed of light.

<!-- b000202 | prose | pages [7] -->
• All the signal loss occurs between the two antennae, with no loss due to cabling, filters, or other noise at the transmitter and receiver. These values are usuallysmall

<!-- b000203 | prose | pages [7] -->
6

<!-- b000204 | prose | pages [7] -->
compared to path loss, and require defining precise equipment to determine.

<!-- b000205 | furniture | pages [8] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000206 | furniture | pages [8] -->
Team #76271

<!-- b000207 | furniture | pages [8] -->
7 of 30

<!-- b000208 | prose | pages [8] -->
• The communications link only needs to be complete in one direction, meaning that the transmitting station only transmits, and the receiving station only receives. We do not need to determine how successfully information is transmitted, only if the

<!-- b000209 | prose | pages [8] -->
4

<!-- b000210 | prose | pages [8] -->
connection is made.

<!-- b000211 | heading | pages [8] -->
Nomenclature

<!-- b000212 | prose | pages [8] -->
∆A Amplitude change factor ∆h Standard deviation of surface height [m] Initial angle of signal projection [rad] ∆ A Path length from starting point to bottom of the ionosphere[km]

<!-- b000213 | prose | pages [8] -->
Permittivity of free space [8.8541 ∗10−12F ∗m s0

<!-- b000214 | prose | pages [8] -->
1] i Local incidence unit vector nˆ Local normal unit vector rˆ Local reflection unit vector λ Signal wavelength[m] µ(z) The refractive index at a given altitude ω Angular wave frequency [rad/s] φ0 The angle of incidence at pointPin[rad] ψ Phase [rad] ρ Complex reflectivitycoefficient Θj The angle swept out from the waveentering the ionosphere to its peak altitude [rad] θi Incidence angle between ray and surface [rad] ˙r Total reflection unit vector

<!-- b000215 | prose | pages [8] -->
B Total path length [m] brg Initial bearing of a signal[rad] c Velocity of light [2.99792x10

<!-- b000216 | prose | pages [8] -->
8m/s]

<!-- b000217 | prose | pages [8] -->
Charge on the electron [−1.602 ∗10−19C] e f Frequency of the signal wave [hertz] tt Antenna gain [dBi] h0 Distance from surface of the Earth to the lowestpoint of the ionosphere [80km] hr Distance from surfa√ce of the Earth to the highest point the ray reaches [km] Complex variable [ −1] j k Non-deviative absorption loss [dB] L Loss [dB] m Mass of the electron [9.109 10

<!-- b000218 | prose | pages [8] -->
31kg]

<!-- b000219 | prose | pages [8] -->
∗

<!-- b000220 | prose | pages [8] -->
N Electron density [ electrons]

<!-- b000221 | prose | pages [8] -->
m3

<!-- b000222 | prose | pages [8] -->
P Power [W ] Pin/Pout The points of entry/exit into/leaving the ionosphere R Radius of the Earth [km] S Path length the ionosphere[km] v Electron-neutral collision frequency [Hz] z Distance between the ray and the surface of the Earth at any given point in its trajectory [km]

<!-- b000223 | furniture | pages [9] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000224 | furniture | pages [9] -->
Team #76271

<!-- b000225 | furniture | pages [9] -->
8 of 30

<!-- b000226 | prose | pages [9] -->
IV.

<!-- b000227 | heading | pages [9] -->
Model Development

<!-- b000228 | prose | pages [9] -->
A.

<!-- b000229 | heading | pages [9] -->
Model Construction

<!-- b000230 | prose | pages [9] -->
The model is constructed in order to accurately create the path of the bouncing signal. This path provides the loss due to free space and ionospheric absorption, which are determined per distance. The ground model determines the loss from the terrain interaction as well as the new incidence angle for propagation of the next bounce.

<!-- b000231 | prose | pages [9] -->
1.

<!-- b000232 | prose | pages [9] -->
Propagation and Ionosphere Interaction

<!-- b000233 | prose | pages [9] -->
The first portion of the model consists of the signal travelling from the ground to the ionosphere, refracting, and travelling from the ionosphere back to the ground. Over this entire section, we determine the path above and below the ionosphere separately. The

<!-- b000234 | prose | pages [9] -->
515

<!-- b000235 | prose | pages [9] -->
below equations are derived from several sources.

<!-- b000236 | prose | pages [9] -->
The equations in this section are based on a curved radio wave trajectory, as shown in our diagram, Figure 1.

<!-- b000237 | caption | pages [9] -->
Figure 1. Diagram of Skywave Interaction with Ionosphere

<!-- b000238 | furniture | pages [10] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000239 | furniture | pages [10] -->
Team #76271

<!-- b000240 | furniture | pages [10] -->
9 of 30

<!-- b000241 | prose | pages [10] -->
Thedistancefrom thetransmittertothe ionosphereis determined fromthe law of sines using the equation

<!-- b000242 | prose | pages [10] -->
5 therefore

<!-- b000243 | prose | pages [10] -->
By Snell’s law, the angle of incidence is equal to the angle of reflection,

<!-- b000244 | prose | pages [10] -->
the length of the transmitter-ionosphere path is the same as the length of the ionosphere- receiver path.

<!-- b000245 | prose | pages [10] -->
Once the wave enters the ionosphere, it begins on a trajectory towards point Pproj. Due to the variability of the refractive index between the first 80 km of Earth’s atmosphere and the ionosphere, the ray begins to bend along path S until it reaches the reflection point, at which it bends back towards the Earth’s surface. We calculate the length of path S with the equation

<!-- b000246 | prose | pages [10] -->
The above equations convert from polar coordinates to a Cartesian grid with the origin on the earth’s surface directly below the radio wave’s virtual maximum. The value of Θj

<!-- b000247 | prose | pages [10] -->
5

<!-- b000248 | prose | pages [10] -->
is found with

<!-- b000249 | prose | pages [10] -->
We modeled the electron density of the ionosphere using values provided by a NASA

<!-- b000250 | prose | pages [10] -->
13 Our model has a sample for every 10° latitude by 20° longitude by 10km

<!-- b000251 | prose | pages [10] -->
database.

<!-- b000252 | prose | pages [10] -->
section of the ionosphere. These values are taken from January 1, 2001 at 1:30 AM GMT to provide a consistent dataset with both day and night regions, but it does not include variation in the ionosphere from season, solar cycle, and other factors. For computational

<!-- b000253 | prose | pages [10] -->
speed, intermediate electron density is found with linear interpolation. See Figure 5 in the Appendix for an example of a trajectory calculated by our model. This trajectorymatches

<!-- b000254 | caption | pages [10] -->
Figure 1 well.

<!-- b000255 | furniture | pages [11] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000256 | furniture | pages [11] -->
Team #76271

<!-- b000257 | furniture | pages [11] -->
10 of 30

<!-- b000258 | prose | pages [11] -->
2.

<!-- b000259 | prose | pages [11] -->
Ground Interaction

<!-- b000260 | prose | pages [11] -->
When the radio wave comes in contact with the earth, we employ a different model to predict its new direction and loss. This model is generalized to allow for different types of land and water terrains.

<!-- b000261 | prose | pages [11] -->
For fixed terrain such as land masses, geological survey data exists that we can use to createrealisticshapes. TheUnitedStatesGeologicalSurveywebsitecontainsdownloadable data sets for elevation, such as the Space Shuttle Radar Topography Mission data that

<!-- b000262 | prose | pages [11] -->
12 We arbitrarily select one such data set,

<!-- b000263 | prose | pages [11] -->
covers the globe with one arcsecond resolution.

<!-- b000264 | prose | pages [11] -->
containing hills and gullies from the border of Guinea and Mali in western Africa.

<!-- b000265 | prose | pages [11] -->
For unfixed terrain such as water, no permanent data sets exist. Because we only need to capture the motion of the water at a fixed moment in time, we decide to generate instantaneous wave shapes. Such simulations are plentiful in MATLAB, and we adapt

<!-- b000266 | prose | pages [11] -->
17 This simulation models random waves of

<!-- b000267 | prose | pages [11] -->
one provided by StackExchange user “Hoki”.

<!-- b000268 | prose | pages [11] -->
set height based on wind patterns, using the Phillips spectrum of wave amplitude for a

<!-- b000269 | furniture | pages [12] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000270 | furniture | pages [12] -->
Team #76271

<!-- b000271 | furniture | pages [12] -->
11 of 30

<!-- b000272 | prose | pages [12] -->
fully-developed sea. Figure 2 (and Figure 7 in the Appendix) are examples of turbulent and calm random waves, respectively.

<!-- b000273 | caption | pages [12] -->
Figure 2. Incident and Reflected Rays Off Random Turbulent Waves

<!-- b000274 | prose | pages [12] -->
We create the terrain for each type of surface as follows:

<!-- b000275 | prose | pages [12] -->
• Smooth land: We generate a perfectly flat 10 by 10 meter surface in MATLAB, representing a plains environment.

<!-- b000276 | prose | pages [12] -->
• Mountainous land: Our model randomly selects a 50 by 50 point subsection of the Guinea/Mali data set to provide the terrain shape. The size is scaled down to a 10 by 10 meter square, with smoothed elevation changes of 10 meters or less. This terrain can very from gentle slopes to steep mountainsides, but does not include cliffs.

<!-- b000277 | prose | pages [12] -->
• Calm seas: Wegenerate a 10 by 10 meter square of gentle waves, with amplitude less than one meter.

<!-- b000278 | prose | pages [12] -->
• Rough seas: We provide a crosswind to generate large swells, with amplitude from 1 to 10 meters for rough ocean and up to 15 meters for super-turbulent.

<!-- b000279 | prose | pages [12] -->
The size of each patch is determined by our need for a small mesh in order to reduce computation time, which means the area must also be small in order to preserve detail.

<!-- b000280 | prose | pages [12] -->
The next step is to determine the signal loss experienced on each type of terrain, using

<!-- b000281 | prose | pages [12] -->
5 We quantify the roughness of

<!-- b000282 | prose | pages [12] -->
equations for reflection and scattering on rough surfaces.

<!-- b000283 | prose | pages [12] -->
a surface using the standard deviation of the height ∆h over the entire mesh surface. We

<!-- b000284 | prose | pages [12] -->
can then apply the Rayleigh roughness criterion to approximate how much the signal

<!-- b000285 | furniture | pages [13] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000286 | furniture | pages [13] -->
Team #76271

<!-- b000287 | furniture | pages [13] -->
12 of 30

<!-- b000288 | prose | pages [13] -->
will reflect or scatter. The change in phase caused by the height difference, as different rays take different length paths, can be calculated using incidence angle θi and wavelength λ:

<!-- b000289 | prose | pages [13] -->
∆ψ = 4π∆hsin(θi)/λ (16)

<!-- b000290 | prose | pages [13] -->
Thedifferent phases causemultipathinterferenceinthewave,which reduces the am- plitude of the coherent specularly reflected component. This amplitudereduction

<!-- b000291 | prose | pages [13] -->
5

<!-- b000292 | prose | pages [13] -->
can be calculated:

<!-- b000293 | prose | pages [13] -->
∆A = exp (−∆ψ

<!-- b000294 | prose | pages [13] -->
2) (17)

<!-- b000295 | prose | pages [13] -->
The reflection capability of the terrain depends on its reflection coefficient ρ, deter- mined by the relative permittivity sr and conductivity σ. We use the equation for perpendicular polarization, although we have not assigned a polarization to our signal:

<!-- b000296 | prose | pages [13] -->
where χ = 18e9 σ/f , σwater = 5 S/m, σland = 0.002 S/m, srwater = 81, and srland = 13

<!-- b000297 | prose | pages [13] -->
18

<!-- b000298 | prose | pages [13] -->
for mountainous terrain.

<!-- b000299 | prose | pages [13] -->
5

<!-- b000300 | prose | pages [13] -->
The resulting loss, based on the power of the specular component, is:

<!-- b000301 | prose | pages [13] -->
Lreflection = 10log10(ρ(∆A)

<!-- b000302 | prose | pages [13] -->
2) (19)

<!-- b000303 | prose | pages [13] -->
Lastly, we use ray tracing methods to determine the direction that the specular com- ponent will reflect, providing the new incidence angle for the next ionosphere bounce.

<!-- b000304 | prose | pages [13] -->
19

<!-- b000305 | prose | pages [13] -->
Using the terrain surface mesh, we find the local normal vector nˆ at each mesh-point using the MATLAB function surfnorm. Weuse the incidence angle between the incoming signal and the horizontal to find a local incidence vector ˆi, which is constant for each mesh-point. Using these two vectors with the Law of Reflection, we can determine the local reflected vectors rˆ.

<!-- b000306 | prose | pages [13] -->
19

<!-- b000307 | prose | pages [13] -->
rˆ = ˆi + 2cos(θlocal)nˆ (20)

<!-- b000308 | prose | pages [13] -->
where θlocal is the local angle of incidence between the local normal and local incidence vector, determined by:

<!-- b000309 | prose | pages [13] -->
cos(θlocal) = −ˆi · nˆ (21)

<!-- b000310 | prose | pages [13] -->
Once we find the local reflection vectors, we can take the mean of each component in ordertofindthe totalreflectionvector. Weremovethelocalvectorswhere thez-component isnegativefromthecalculation,becausethisrepresentscaseswheretheterrainisshadowed from the incident signal. With the total reflection direction, we extract the azimuth and elevation using MATLAB’s cart2sph converter to provide for the next bounce.

<!-- b000311 | prose | pages [13] -->
The example terrain plots, including Figure 2 and Figure 7 and 6 in the Appendix, display the surfaces with local vectors shown, as well as the mean incidence and reflected vectors.

<!-- b000312 | furniture | pages [14] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000313 | furniture | pages [14] -->
Team #76271

<!-- b000314 | furniture | pages [14] -->
13 of 30

<!-- b000315 | prose | pages [14] -->
3.

<!-- b000316 | prose | pages [14] -->
Loss

<!-- b000317 | prose | pages [14] -->
To tie our model together, we return to the overall link budget, updated with new losses:

<!-- b000318 | prose | pages [14] -->
PRx = PT x + GTx + Lfree + Labsorption + Lreflection + GRx (22)

<!-- b000319 | prose | pages [14] -->
Aftereachionosphereandsurfacebounce,ourmodelreevaluatesthisequationtodeter- mine if the link margin is met. If it is met, the signal continues for another bounce. If not, we determine that signal to be lost, and record its last known surface location. Overall, we have 180 dB in the budget, of which we can lose up to 170 dB to remain over 10 dB.

<!-- b000320 | prose | pages [14] -->
B.

<!-- b000321 | heading | pages [14] -->
Model Validation

<!-- b000322 | prose | pages [14] -->
We will first validate our model qualitatively by following individual rays along their path until they are absorbed, fly into space, or fall below the minimum signal strength. Given accounts of skywave radio operators, we expect that this will depend on the time of

<!-- b000323 | prose | pages [14] -->
10 We expect the signal to follow a straight

<!-- b000324 | prose | pages [14] -->
day and electron density at the bounce location.

<!-- b000325 | prose | pages [14] -->
path from the origin to the bottom of the ionosphere, followed bya curved point that peaks at the calculated point of refraction, followed by a straight path from the bottom of the ionosphere back to the surface. While we don’t have a quantitative expectation of the signal’s behavior after bouncing off of the surface; however, we do expect that the more surface variation, the more variation we will see in subsequent bounces. We expect that theloss willincreasewithdistancetravelled, and increasewitheach surfaceand ionosphere interaction.

<!-- b000326 | prose | pages [14] -->
Quantitatively, wefind that a range for the maximum distance of a hop is between 2500

<!-- b000327 | prose | pages [14] -->
20 We will likely see our maximum distance on our

<!-- b000328 | prose | pages [14] -->
and 5000 km, depending on the height.

<!-- b000329 | prose | pages [14] -->
first bounce because of our ability to control the input frequency and angle.

<!-- b000330 | prose | pages [14] -->
V.

<!-- b000331 | heading | pages [14] -->
Model Application

<!-- b000332 | prose | pages [14] -->
In order to recreate the desired scenarios, we set the model conditions for each test, including input variables, output variables, and number of trials.

<!-- b000333 | prose | pages [14] -->
A.

<!-- b000334 | prose | pages [14] -->
Part I

<!-- b000335 | prose | pages [14] -->
The first application of our model focuses on reflection of the signal off of the ocean.

<!-- b000336 | prose | pages [14] -->
13 we will uniformly

<!-- b000337 | prose | pages [14] -->
Using the January 1, 2000 ionosphere data obtained from NASA,

<!-- b000338 | prose | pages [14] -->
randomly select a latitude, longitude, and bearing as the origin of the signal. This location determines only the local ionospheric conditions, because we assume that the signal will bounce off of water for this problem, no matter where it goes.

<!-- b000339 | prose | pages [14] -->
Wesend this signal initially at an elevation angle of 30°, a frequency of 3 MHz, a power of 100 W, an antenna gain of 5.03 dBi, and a receiver antenna sensitivity of -120 dBm. We

<!-- b000340 | heading | pages [14] -->
will determine a mean, median, and standard deviation of signal strength after

<!-- b000341 | prose | pages [14] -->
a single bounce and the max number of bounces (where bounce 2 and onward are over calm water) given the above initial conditions. Wewill simulate 10000 signals for a

<!-- b000342 | furniture | pages [15] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000343 | furniture | pages [15] -->
Team #76271

<!-- b000344 | furniture | pages [15] -->
14 of 30

<!-- b000345 | prose | pages [15] -->
first bounce on calm seas with <1 m waves (because this is our base case) and 1000 for a first bounce on rough seas with < 10 m waves.

<!-- b000346 | prose | pages [15] -->
B.

<!-- b000347 | prose | pages [15] -->
Part II

<!-- b000348 | prose | pages [15] -->
We will reuse the initial conditions from above, but instead assume that everybounce will take place off land with smooth (perfectly flat) or mountainous (up to 10m deviations). Our results will be in the same format as Part I, and will show the effects of different terrains on the number of reflections of the signal, as well as the power lost for 1000 trials.

<!-- b000349 | prose | pages [15] -->
C.

<!-- b000350 | prose | pages [15] -->
Part III

<!-- b000351 | prose | pages [15] -->
Using the same elevation angle and frequency, weremovethe random starting location, ftxing a transmitter location and bearing near the edge of the water. By running 1000 trials with different elevation angles, and outputting the location of each bounce, we can find the region where a ship would be able to receive the signal.

<!-- b000352 | prose | pages [15] -->
VI.

<!-- b000353 | prose | pages [15] -->
A.

<!-- b000354 | heading | pages [15] -->
Validation

<!-- b000355 | heading | pages [15] -->
Results

<!-- b000356 | prose | pages [15] -->
As we discussed in the Background, we expect that the peak of radio wave reflection to occur in the region of the day/night terminator. This occurs because of a balance of the weak reflection of the night and the strong absorption of the day. Our model matches these results, as shown in Figures 8 and 9 in the Appendix. The former plots the latitude andlongitudeofmodeled oceanic bounces, superimposedoveracolormap ofthemaximum ionosphere electron density that day. The bounces occur between the bright and dark regions, showing a clear preference for the day/night terminator. The latter plot shows the probability of radio waves bursting through the ionosphere as a function of peakelectron density. This probability is near unity the highest and lowest densities, but decreases for intermediate densities, as would be expected near the day/night terminator. Thus, our model matches well with qualitative predictions.

<!-- b000357 | prose | pages [15] -->
B.

<!-- b000358 | prose | pages [15] -->
Part I

<!-- b000359 | prose | pages [15] -->
Werunourmodeltocomparetheperformanceofthesignaloncalmoceanandturbulent ocean measured by the power of the signal after the first bounce. For Part I and Part II, we will use a 2 sample t-test because the observed data are from random samples of a skewed normal distributions. For our analysis, we say that our null hypothesis is that thetwo sets of data are the same.

<!-- b000360 | caption | pages [15] -->
Table 1. Power After First Bounce by Varying Turbulence of Ocean

<!-- b000361 | prose | pages [15] -->
Mean (dB) Calm 25.54 Turbulent 24.82 Std Power (dB) 4.13 4.28

<!-- b000362 | furniture | pages [16] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000363 | furniture | pages [16] -->
Team #76271

<!-- b000364 | furniture | pages [16] -->
15 of 30

<!-- b000365 | prose | pages [16] -->
The distribution of signal strength after the first bounce is shown in Figure 10 in the Appendix and the numerical values are shown in 1. Running our t-test, we get a p-value of 0.0291, which means the difference in power from calm to turbulent is significant at a 5% level.

<!-- b000366 | caption | pages [16] -->
Table 2. Distance of Signal by Varying Turbulence of Water

<!-- b000367 | prose | pages [16] -->
Std Distance (km) Av Distance (km) Calm 1444.67 Turbulent 1006.71 Av Bounces Std Bounces 474.26 1.53 0.50 231.72 1.10 0.33

<!-- b000368 | prose | pages [16] -->
As we extend our analysis to include multiple bounces, we find that the maximum number of bounces with an initial angle of 30° and a frequency of 3 MHz is 2 bounces, for both initial calm and initial turbulent cases. Usingthesamet-teston the average signal distance, we get a p-value of 3.87∗10−32, and a p-value of 7.84∗10−28 for the number of bounces. This means that although both have the same maximum number of bounces, we can conclude that overall the turbulent ocean causes a reduction in both distance and bounce number.

<!-- b000369 | prose | pages [16] -->
C.

<!-- b000370 | prose | pages [16] -->
Part II

<!-- b000371 | prose | pages [16] -->
We run our model to compare the performance of the signal on smooth terrain and rugged terrain measured by the power of the signal after the first bounce.

<!-- b000372 | caption | pages [16] -->
Table 3. Power After First Bounce by Varying Ruggedness of Terrain

<!-- b000373 | prose | pages [16] -->
Mean (dB) Smooth 24.84 Rugged 24.58 Std Power (dB) 4.07 3.97

<!-- b000374 | prose | pages [16] -->
The distribution of signal strength after the first bounce is shown in Figure 11 in the Appendix and the numerical values are shown in 1. Running our t-test on the two data sets, we get a p-value of 0.39 and cannot prove that the power data from the smooth and rugged terrain simulations are different.

<!-- b000375 | caption | pages [16] -->
Table 4. Distance of Signal by Varying Ruggedness of Terrain

<!-- b000376 | prose | pages [16] -->
Std Distance (km) Av Distance (km) Av Bounces Std Bounces 453.67 Smooth 1360.45 1.47 0.50 316.37 Rugged 997.47 1.25 0.44

<!-- b000377 | prose | pages [16] -->
As weextend our analysis to include all signals that do not fall below the SNR threshold of 10 dB, we find that the maximum number of bounces that we observe with an initial angle of 30° and a frequency of 3 MHz over smooth and mountainous terrain is 2 bounces. Using the same t-test on the average signal distance over the Earth, we get a p-value of 2.74 ∗10−44 and reject the null hypothesis because the p-value is well

<!-- b000378 | furniture | pages [17] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000379 | furniture | pages [17] -->
Team #76271

<!-- b000380 | furniture | pages [17] -->
16 of 30

<!-- b000381 | prose | pages [17] -->
below any reasonable statistical measure. Therefore, we can say that the distance data from the smooth and rugged terrain simulations are different. The p-value for bounces is

<!-- b000382 | prose | pages [17] -->
3.74 ∗10−10, which is similarly significant.

<!-- b000383 | prose | pages [17] -->
D.

<!-- b000384 | heading | pages [17] -->
Sensitivity Results

<!-- b000385 | prose | pages [17] -->
Beforeproceeding to Part III, wemust first determine the best initialangle and the best initial frequency for our transmitting station and our boat receiver. Instead of the number of hops, wewill use the highest average Earth distance of an angle-frequency combination.

<!-- b000386 | prose | pages [17] -->
With an ideal angle 30° and frequency 3 MHz, we will sample three potential locations and ship travel directions in order to determine the maximum distance that the ship can travel away from the station while still receiving communication.

<!-- b000387 | prose | pages [17] -->
E.

<!-- b000388 | prose | pages [17] -->
Part III

<!-- b000389 | prose | pages [17] -->
To ensure that our sample size has enough successful bounces to compare the three locations, we choose to sample from locations and directions that showed a highpercent- age of reflection from Parts I and II. Our two realistic locations are Monjaras, Honduras (13°09’07.6”N 87°23’07.2”W) and Los Angeles, California (32°41’19.9”N 117°13’14.7”W),

<!-- b000390 | prose | pages [17] -->
21 After running these

<!-- b000391 | prose | pages [17] -->
and we will aim our transmitter West and Southwest, respectively.

<!-- b000392 | prose | pages [17] -->
three simulations, we will determine the average performance of our radio system.

<!-- b000393 | caption | pages [17] -->
Figure 3. Honduras Trajectory

<!-- b000394 | caption | pages [17] -->
Figure 4. L.A. Trajectory

<!-- b000395 | prose | pages [17] -->
In this simulation, we vary the initial angle ∆from 0° to 60° in increments of 0.1° in order to get a representation of a transmitter dispersing a signal.

<!-- b000396 | caption | pages [17] -->
Table 5. Distance for Signals Aimed at a Ship in Turbulent Seas (Measured in km)

<!-- b000397 | prose | pages [17] -->
B1 Max Dist B1 Min Dist B2 Min Dist B2 Max Dist 1085.87 Honduras (W) 651.77 187.67 1622.24 810.67 L.A. (SW) 676.42 - -

<!-- b000398 | prose | pages [17] -->
Our model tracks the minimum and maximum distance (km) for each bounce that we observe of individual rays. From Honduras, we see that a boat on turbulent oceans could

<!-- b000399 | furniture | pages [18] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000400 | furniture | pages [18] -->
Team #76271

<!-- b000401 | furniture | pages [18] -->
17 of 30

<!-- b000402 | prose | pages [18] -->
maintain a signal with the transmitting station from 187.67km to 1622.24km in a straight line from the shore. As show in Figure 18 in the Appendix, the location of the first points are concentrated between 651.77km and 1085.87km from the shore. The second bounces are scattered by the turbulent waves and would not provide a consistent signal for a boat outside of the first bounce concentration.

<!-- b000403 | prose | pages [18] -->
FromL.A., our signal only bounces a single time and coversthe distance stretchof ocean from 676.42km to 810.42km in a straight line from the shore. Similar to the Honduras simulation, the first bounce points are concentrated along the initial trajectory.

<!-- b000404 | prose | pages [18] -->
VII.

<!-- b000405 | heading | pages [18] -->
Sensitivity Analysis

<!-- b000406 | prose | pages [18] -->
A.

<!-- b000407 | prose | pages [18] -->
Explore Parameter Space

<!-- b000408 | prose | pages [18] -->
Inordertoensurethatourmodelisrobust,weneed tounderstand howourassumptions and inputs effect the results. To do this, we select several key inputs and data sets, and vary them with 1000 trials to see how the model responds.

<!-- b000409 | prose | pages [18] -->
1.

<!-- b000410 | prose | pages [18] -->
Frequency and Elevation Angle

<!-- b000411 | prose | pages [18] -->
The HF band contains frequencies from 3-30MHz, but wechoose 3 MHz as our default, launched at an angle of 30 degrees. This selection is arbitrary, so we decide to perform a study on the model’s sensitivity to combinations of elevation angle and signal frequency. Our metrics are the distance, bounces, and loss due to ionospheric absorption. We select elevation angles of 0, 2, 5, 10, 15, 20, 30, 40, and 50 degrees for this sweep, accompanying the changes in signal from 3 to 21 MHz by multiples of 3 MHz. We expect that some types of loss penalize high frequencies, while some penalize low, so there is a trade-off. Additionally, the elevation angle effects the overall path length, which effects loss.

<!-- b000412 | prose | pages [18] -->
The results of this analysis show that functional angle/frequency pairs exist on a line traversing through the parameter space. Deviation from this line causes the signal to either travel unabated through the ionosphere or be totally deteriorated by loss. Pairs with low frequencies and high angles tend to bounce more, but travel a shorter overall distance, as is seen in Figures 12 and 13 in the Appendix. High frequency/low angle pairs are much more likely to be consumed by loss than low frequency, high angle pairs. This can be observed in Figure 14 in the Appendix.

<!-- b000413 | prose | pages [18] -->
2.

<!-- b000414 | prose | pages [18] -->
Wave Turbulence

<!-- b000415 | prose | pages [18] -->
For the wave turbulence, we wish to determine the limits of the extent to which tur- bulent water can effect the overall distance. We do this by adding an additional metric for super-turbulent swells with a max height of <15 m, representative of extreme storm conditions, as well as running trials that bounce off of the same type of wa- ter for all bounces instead of calm water for bounces after the first. We expect that super-turbulent water will have the most effect on decreasing distance, but changing the subsequent bounces will also decrease the distance.

<!-- b000416 | caption | pages [18] -->
Table6 contains the resultingvalues from the simulation as theturbulence is varied. We

<!-- b000417 | prose | pages [18] -->
performat-testtodeterminewherethesedifferencesaresignificant. Wetestthehypotheses

<!-- b000418 | furniture | pages [19] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000419 | furniture | pages [19] -->
Team #76271

<!-- b000420 | furniture | pages [19] -->
18 of 30

<!-- b000421 | prose | pages [19] -->
that each pair of observations have the same mean and find p-values of essentially 0 for the Calm/Turbulent and Calm/Super Turbulent pairings. The final pairing,Turbulent/Super Turbulent,has an insignificant p-value of 0.64. Thus, we conclude that turbulent and super turbulent oceans tend decrease the mean distance traveled by the radio signal. A box-plot of these data are found in Figure 15 in the Appendix.

<!-- b000422 | caption | pages [19] -->
Table 6. Effects of Ocean Turbulence on Distance Traveled

<!-- b000423 | prose | pages [19] -->
Distance Traveled Calm

<!-- b000424 | prose | pages [19] -->
Mean (km) 1445 Standard Derivation

<!-- b000425 | prose | pages [19] -->
474

<!-- b000426 | prose | pages [19] -->
(km)

<!-- b000427 | prose | pages [19] -->
3.

<!-- b000428 | prose | pages [19] -->
Transmit Power

<!-- b000429 | prose | pages [19] -->
Turbulent Super Turbulent 1007 995

<!-- b000430 | prose | pages [19] -->
232 253

<!-- b000431 | prose | pages [19] -->
The power of the transmitter determines the initial signal strength, so we want to examine if increasing this parameter allows the signal to bounce a greater distance across theEarth. Thetransmitter power is increased inorder of magnitudesteps of 100 W, 1000 W, and 100,000 W, which correspond to 50, 60, and 80 dBm. Including the antenna and receiver sensitivity, the values are 180, 190, and 210 dBm total signal compared to the 10 dB cutoff.

<!-- b000432 | prose | pages [19] -->
Plugging these values into the simulation, we find statistics presented in Table 7. We compare these simulations with a 2-sample t-test, finding the differences between all three pairs to be statistically significant. The lowest p-value, 4E-5, corresponds to the null hypothesis that the 190 and 210 dBm signals have the same average distance travelled. This is much lower than any common significance level. The other p-values are essentially

<!-- b000433 | heading | pages [19] -->
0. Weconclude that the more powerful the transmitter, the greater the overall

<!-- b000434 | prose | pages [19] -->
distance travelled. A box plot of this data can be found in Figure 16 in the Appendix.

<!-- b000435 | caption | pages [19] -->
Table 7. Effects of Transmitter Power on Distance Traveled

<!-- b000436 | heading | pages [19] -->
180 dBm

<!-- b000437 | prose | pages [19] -->
Distance Traveled Mean (km) 1445 Standard Derivation

<!-- b000438 | prose | pages [19] -->
474

<!-- b000439 | prose | pages [19] -->
(km)

<!-- b000440 | prose | pages [19] -->
4.

<!-- b000441 | prose | pages [19] -->
Ionosphere Density

<!-- b000442 | heading | pages [19] -->
190 dBm

<!-- b000443 | heading | pages [19] -->
210 dBm

<!-- b000444 | prose | pages [19] -->
1737 2105

<!-- b000445 | prose | pages [19] -->
672 1168

<!-- b000446 | prose | pages [19] -->
Our sample used NASA’s ionosphere data for January 1, 2000. This year recorded

<!-- b000447 | prose | pages [19] -->
11 a relatively high amount of solar activity compared to neighboring

<!-- b000448 | prose | pages [19] -->
nearly 140 sun spots,

<!-- b000449 | prose | pages [19] -->
years. To test the effect of the number of sun spots on our model, we use NASA data for the years 2003 and 2009, with 70 sun spots and 10 sun spots

<!-- b000450 | prose | pages [19] -->
11, respectively.

<!-- b000451 | furniture | pages [20] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000452 | furniture | pages [20] -->
Team #76271

<!-- b000453 | furniture | pages [20] -->
19 of 30

<!-- b000454 | prose | pages [20] -->
These represent a moderate and low case of solar activity. The solar activity influences the electron density of the ionosphere, which should increase the refractive index, making it more difficult for signals to reflect instead of refract.

<!-- b000455 | prose | pages [20] -->
As in the previous cases, weplugged these parameters into the simulation and recorded the resultant total distances, with overall statistics displayed in Table 8. We perform a two-sample t-test on each of these pairs, and find an insignificant p-value of 0.6 for the 2009/2003 pair. Thus, wecannot conclude that these twodata sets are different. However, the 2009/2000 and 2003/2000 pairs have p-values of 0.03 and 0.003 respectively, which are both significant at the common 5% standard. Thus, we can conclude that high solar activity has a statistically signiftcant negative effect on distance travelled. See

<!-- b000456 | caption | pages [20] -->
Figure 17 in the Appendix for a box-plot of these data.

<!-- b000457 | caption | pages [20] -->
Table 8. Effects of Solar Activity on Distance Traveled

<!-- b000458 | heading | pages [20] -->
2009 Data

<!-- b000459 | prose | pages [20] -->
Distance Traveled (Low)

<!-- b000460 | prose | pages [20] -->
Mean (km) 1587 Standard Derivation

<!-- b000461 | prose | pages [20] -->
520

<!-- b000462 | prose | pages [20] -->
(km)

<!-- b000463 | prose | pages [20] -->
VIII.

<!-- b000464 | prose | pages [20] -->
A.

<!-- b000465 | prose | pages [20] -->
Our Conclusion

<!-- b000466 | heading | pages [20] -->
2003 Data

<!-- b000467 | heading | pages [20] -->
2000 Data

<!-- b000468 | prose | pages [20] -->
(Medium)

<!-- b000469 | prose | pages [20] -->
(High) 1551 1445

<!-- b000470 | prose | pages [20] -->
430 474

<!-- b000471 | heading | pages [20] -->
Conclusion

<!-- b000472 | prose | pages [20] -->
Using high-throughput simulation of radio wavetravel, we explore the parameters that most strongly affect radio communications. Wefind that the interaction between the radio wavesandtheionosphereisthestrongestdeterminantofpropagationbehavior. Thetypical loss a signal experiences in the ionosphere is around 15-20 dB, whereas typical loss from ground interaction is less than one dB.

<!-- b000473 | prose | pages [20] -->
The sensitivity to the ionosphere manifests itself when considering the frequencyand angle of elevation of skywave. Too much interaction with the ionosphere will sap the signal’s strength, while too little interaction will not alter its upward trajectory, allowing it to escape to space. The seasonal and daily changes in the ionosphere also have marked effectsonsignalpropagation,increasingand decreasingtheelectrondensityasmoreorless solar radiation is incident on the atmosphere.

<!-- b000474 | prose | pages [20] -->
Also important to radio wave propagation is interaction with the Earth. We consider multiple terrains in this model, and find that rough oceans or mountainous land slightly reduce signal strength while scattering its trajectory.

<!-- b000475 | prose | pages [20] -->
Through our consideration of all relevant signal attributes, we qualitatively match known radio wave behavior. Thus, we hold this model to be a useful tool for radio enthu- siasts and professionals alike.

<!-- b000476 | furniture | pages [21] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000477 | furniture | pages [21] -->
Team #76271

<!-- b000478 | furniture | pages [21] -->
20 of 30

<!-- b000479 | prose | pages [21] -->
B.

<!-- b000480 | heading | pages [21] -->
Strengths

<!-- b000481 | prose | pages [21] -->
• The model considers the complexity of the layers of the ionosphere, using real global data for day and night that varies with altitude. This allows more accurate cal- culations of ionospheric trajectory and absorption loss, as well as when signals are reflected or transmitted, matching real world expectations for the day/night termi- nator.

<!-- b000482 | prose | pages [21] -->
• The model considers a curved ionosphere and curved Earth, finding more accurate distances as arc lengths over the surface than a flat approximation.

<!-- b000483 | prose | pages [21] -->
• The model uses realistic terrain shapes for land and water, to aid in determining correct reflection loss and bounce direction.

<!-- b000484 | prose | pages [21] -->
• The model is computationally efficient, allowing 1000 trials to run in just a few minutes on a personal laptop.

<!-- b000485 | prose | pages [21] -->
C.

<!-- b000486 | heading | pages [21] -->
Weaknesses and Limiting Assumptions

<!-- b000487 | prose | pages [21] -->
• The model ignores many potential sources of loss, including multipath loss due to polarization in areas other than the ground bounce, as well as Doppler shift and magnetic effects in the ionosphere.

<!-- b000488 | prose | pages [21] -->
• The model only considers a small patch of ground, when in reality the signal would bounce off a much larger area. It also neglects surface coverings.

<!-- b000489 | prose | pages [21] -->
• The model does not consider the ways that the ionosphere changes with time on scales larger than one day-night cycle, unless a completely new data set is provided.

<!-- b000490 | prose | pages [21] -->
• The model does not take into account the use of real radio equipment with cables, noise, and the need to transmit information with a low bit error rate.

<!-- b000491 | prose | pages [21] -->
D.

<!-- b000492 | heading | pages [21] -->
Future Work

<!-- b000493 | prose | pages [21] -->
Our simulation could be extended and improved by increasing the complexity of the data used, and reducing assumptions. If we gained access to or created a model of iono- spheric conditions with time, we could make the time an input to our model. With a full global land data set, we could tie the latitude and longitude to terrain as well as the iono- sphere, and make theterraindeterministicfor a given location. Inaddition, with moretime wecould include bigger land and water patches, so larger features would dominate instead of very local ones. Loss accuracy could be increased by accounting for the signal phase and interference throughout the propagation, as well as considering real radio equipment.

<!-- b000494 | prose | pages [21] -->
Furthermore, we could gain greater understanding of the accuracy of our modelcom- pared to real skywave signals by finding an empirical data. For instance, if we found recorded information about the equipment used, transmit and receive locations, and exact date and time, we could use an ionosphere dataset for that day to simulate the real contact. We could see where the signals bounced on the Earth, and what power we expect themto arrive with, to see if our model is accurately recreating trajectory and loss.

<!-- b000495 | furniture | pages [22] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000496 | furniture | pages [22] -->
Team #76271

<!-- b000497 | furniture | pages [22] -->
21 of 30

<!-- b000498 | prose | pages [22] -->
IX.

<!-- b000499 | heading | pages [22] -->
Letter

<!-- b000500 | prose | pages [22] -->
Skywave communication remains the only non-line-of-sight method of radiocommu- nication over vast, turbulent oceans and disruptive terrain. While bouncing the signal between the ionosphere and the surface of the Earth allows signal transmission over long distances, it introduces the unpredictability of the ionospheric density, the non-uniformity of reflection surfaces, and signal deterioration over the path of the signal.

<!-- b000501 | prose | pages [22] -->
Our model simulates a transmitter at an initial latitude and longitude on a spherical Earth beaming a HF (between 3 MHz and 30 MHz) signal with an initial bearing and eleva- tion angle. For our simulation, we assume a 100-Watt transmitter with a 100-meter dipole antenna. The model of the ionosphere was adapted from a gradient set of data collected by NASA (see NASA’s International Reference Ionosphere data set). Using the variable density, we can determine the refraction of the signal at each layer of the ionosphere.

<!-- b000502 | prose | pages [22] -->
Oncethe signalexits thebottom ofthe ionosphere, itcontinues onits trajectorytowards asimulatedpatchofterrainusingeitherawavesimulatororgeologicalelevationdata. From this bounce we determine the impact loss and the new trajectory of the signal. Weiterate this process until the signal falls below the sensitivity of the radio receiver.

<!-- b000503 | prose | pages [22] -->
With the path determined, we calculate the loss along the path of the signal considering freespacepathlossduetospreadingalongdistance,ionosphericabsorptionloss,andreflec- tion loss from scattering. While other sources of loss exist in real systems, we determined that these three losses constitute most of the loss incurred during transmission.

<!-- b000504 | prose | pages [22] -->
Due to the unpredictability of the ocean and of terrain, we test skywave paths that bounce on calm and turbulent water, as well as smooth and mountainous land. Wedo this by randomly varying transmitter locations, and test paths from coastal cities to determine the maximum effective transmission distance.

<!-- b000505 | prose | pages [22] -->
We observe the largest difference in our results when varying frequency and elevation angle. To determine their relation to one-another, we co-vary the frequency and elevation angle. From this analysis, we find an effective angle and transmission frequency around 10° and 20 MHz. Lower frequency and higher angle pairs, such as 30° and 3 MHz tends to bouncemore,buttravelalowerdistance. Theeffectivenessoftheradiowavesrangingabove 50° and 15 MHz quickly dissipates, as these waves are either absorbed in the ionosphere or launched into space.

<!-- b000506 | prose | pages [22] -->
We also explore our models sensitivity by altering the wave conditions from calm to super-turbulent, increasing the transmission power, and changing ionospheric density. Of these factors, the ruggedness of the terrain has the largest influence of the dispersion of the signal, while the ionospheric density (heavily influenced by sun spot number) causes our waves to be absorbed or lost in space.

<!-- b000507 | prose | pages [22] -->
Inour most realisticsimulation, wesend a signalfrom Honduras directly southwest at 3 MHz and a varying elevation angle. Wefind that the signal distance ranges from 187.67km to 1622.24km in a straight line from the shore. The signal as it first bounces is fairly concentrated, while the secondary bounces shows a near-chaotic dispersion of the signal fromtheroughnessofthewaves. This600raysimulationdemonstratestheunpredictability of the spread of HF radio waves on rough terrain. These results demonstrate the cause for dead-zones of skywave signals, especially on the open ocean.

<!-- b000508 | prose | pages [22] -->
In summary, our model considers the most significant factors in modeling the behavior of HF radio waves. Through these considerations and our sensitivity analysis, wequalita-

<!-- b000509 | furniture | pages [23] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000510 | furniture | pages [23] -->
Team #76271

<!-- b000511 | furniture | pages [23] -->
22 of 30

<!-- b000512 | prose | pages [23] -->
tively match known radio wave behavior as well as approximate ranges expected from the transmission systems described above. Thus, we hold this model to be a useful tool for radio enthusiasts and professionals alike.

<!-- b000513 | furniture | pages [24] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000514 | furniture | pages [24] -->
Team #76271

<!-- b000515 | furniture | pages [24] -->
23 of 30

<!-- b000516 | heading | pages [24] -->
References

<!-- b000517 | references | pages [24] -->
1“The

<!-- b000518 | references | pages [24] -->
Technology,”

<!-- b000519 | references | pages [24] -->
History

<!-- b000520 | references | pages [24] -->
of

<!-- b000521 | references | pages [24] -->
Communication

<!-- b000522 | references | pages [24] -->
https://www.conferencecallsunlimited.com/

<!-- b000523 | references | pages [24] -->
history-of-communication-technology. Accessed: 2018-02-10.

<!-- b000524 | references | pages [24] -->
2“Report and Minutes of Proceedings,” Tech. rep., International Conference on Safety of Life at Sea

<!-- b000525 | references | pages [24] -->
Committee on Life Saving Appliances, 1914.

<!-- b000526 | references | pages [24] -->
3“What Marine Communication Systems Are Used in the Maritime Industry?” https://www.

<!-- b000527 | references | pages [24] -->
marineinsight.com/marine-navigation/marine-communication-systems-used-in-the-maritime-industry.

<!-- b000528 | references | pages [24] -->
cessed: 2018-02-10.

<!-- b000529 | references | pages [24] -->
Ac-

<!-- b000530 | references | pages [24] -->
4MCM 2018: Problem A, Mathematical Contest in Modeling, COMAP, Web, 2018.

<!-- b000531 | references | pages [24] -->
5Barclay, L. and of Electrical Engineers, I., Propagation of Radiowaves, Electromagnetic Waves, In-

<!-- b000532 | references | pages [24] -->
stitution of Engineering and Technology, 2003.

<!-- b000533 | references | pages [24] -->
6Scientific, C., “Link Budget and Fade Margin,” https://s.campbellsci.com/documents/us/ technical-

<!-- b000534 | references | pages [24] -->
papers/link-budget.pdf, 2016.

<!-- b000535 | references | pages [24] -->
7Wescom, G., “Just a Dipole,” , 2007.

<!-- b000536 | references | pages [24] -->
8Modeling the Propagation of Signals, MATLAB Documentation Center, Accessed: 2018-02-10.

<!-- b000537 | references | pages [24] -->
9Farahmand,

<!-- b000538 | references | pages [24] -->
F.,

<!-- b000539 | references | pages [24] -->
“Channel

<!-- b000540 | references | pages [24] -->
Modeling

<!-- b000541 | references | pages [24] -->
and

<!-- b000542 | references | pages [24] -->
Characteristics,”

<!-- b000543 | references | pages [24] -->
https://web.sonoma.edu/users/f/

<!-- b000544 | references | pages [24] -->
farahman/sonoma/courses/cet543/lectures/2011 Lectures/ChannelModels F13.pdf, Sonoma State Univer-

<!-- b000545 | references | pages [24] -->
sity, 2014.

<!-- b000546 | references | pages [24] -->
10ElectronicsNotes, “Ionospheric Layers: D, E, F, F1, and F2 Regions,” https://www.electronics-notes.

<!-- b000547 | references | pages [24] -->
com/articles/antennas-propagation/ionospheric/ionospheric-layers-regions-d-e-f1-f2.php, Accessed: 2018-

<!-- b000548 | references | pages [24] -->
02-10.

<!-- b000549 | references | pages [24] -->
11Gannon, M., “Sun’s 2013 Solar Activity Peak Is Weakest in 100 Years,” https://www.space.com/

<!-- b000550 | references | pages [24] -->
21937-sun-solar-weather-peak-is-weak.html, Accessed: 2018-02-11.

<!-- b000551 | references | pages [24] -->
12Survey, U. S. G., “Shuttle Radar Topography Mission (SRTM) 1 Arc-Second Global,” https://lta.

<!-- b000552 | references | pages [24] -->
cr.usgs.gov/SRTM1Arc, Accessed: 2018-02-11.

<!-- b000553 | references | pages [24] -->
13“International Reference Ionosphere,” https://iri.gsfc.nasa.gov/. Accessed: 2018-02-10.

<!-- b000554 | references | pages [24] -->
14“Sea States,” https://manoa.hawaii.edu/exploringourfluidearth/physical/waves/sea-states, Univer-

<!-- b000555 | references | pages [24] -->
sity of Hawaii, 2018.

<!-- b000556 | references | pages [24] -->
15Davies, K. and of Electrical Engineers, I., Ionospheric Radio, Electromagnetics and Radar Series,

<!-- b000557 | references | pages [24] -->
Peregrinus, 1990.

<!-- b000558 | references | pages [24] -->
16“Calculate distance, bearing and more between Latitude/Longitude points,” http://www.

<!-- b000559 | references | pages [24] -->
movable-type.co.uk/scripts/latlong.html, Accessed: 2018-02-11.

<!-- b000560 | references | pages [24] -->
17Hoki, “MATLAB/CUDA: ocean wave simulation,” https://stackoverflow.com/questions/28279337/

<!-- b000561 | references | pages [24] -->
matlab-cuda-ocean-wave-simulation, Accessed: 2018-02-11.

<!-- b000562 | references | pages [24] -->
18Stroobandt, S., “World Atlas of Ground Conductivity,” http://hamwaves.com/ground/en/index.

<!-- b000563 | references | pages [24] -->
html, Accessed: 2018-02-10.

<!-- b000564 | references | pages [24] -->
19de Greve, B., “Reflections and Refractions in Ray Tracing,” https://graphics.stanford.edu/courses/

<!-- b000565 | references | pages [24] -->
cs148-10-summer/docs/2006--degreve--reflection refraction.pdf, Stanford University, 2006.

<!-- b000566 | references | pages [24] -->
20ElectronicsNotes, “Ionospheric Layers: D, E, F, F1, and F2 Regions,” https://www.electronics-notes.

<!-- b000567 | references | pages [24] -->
com/articles/antennas-propagation/ionospheric/skywaves-skip-distance-zone.php, Accessed: 2018-02-11.

<!-- b000568 | references | pages [24] -->
21“Google Maps,” https://www.google.com/maps/, Accessed: 2018-02-12.

<!-- b000569 | furniture | pages [25] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000570 | furniture | pages [25] -->
Team #76271

<!-- b000571 | furniture | pages [25] -->
24 of 30

<!-- b000572 | references | pages [25] -->
X.

<!-- b000573 | heading | pages [25] -->
Appendix

<!-- b000574 | prose | pages [25] -->
Diagram of Calculated Ionosphere Trajectory

<!-- b000575 | prose | pages [25] -->
This plot provides an example of our ionosphere model, illustrating the bending of the signal before it is reflected.

<!-- b000576 | caption | pages [25] -->
Figure 5. Example Ionosphere Signal Trajectory

<!-- b000577 | prose | pages [25] -->
Example Terrain with Vectors

<!-- b000578 | prose | pages [25] -->
These plots demonstrate the terrain generation and vector reflection calculations. The axes describe the x and y locations, as well as height, in meters. The local vectors are positioned at every mesh-point to illustrate the local calculations. The mean vectors are shown to the side in red and yellow. Land is shown in grey and water in blue. The water plot is formatted identically to land, except the local normal vectors are omitted for clarity.

<!-- b000579 | caption | pages [25] -->
Figure 6. Incident, Normal, and Reflected Rays Off Random Mountainous Terrain

<!-- b000580 | furniture | pages [26] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000581 | furniture | pages [26] -->
Team #76271

<!-- b000582 | furniture | pages [26] -->
25 of 30

<!-- b000583 | caption | pages [26] -->
Figure 7. Incident and Reflected Rays Off Random Calm Waves

<!-- b000584 | prose | pages [26] -->
Model Validation: Comparing Absorbed and Escaped Signals to Modeled Electron Density

<!-- b000585 | caption | pages [26] -->
Figure 8. Oceanic Bounce Locations Plotted Over Ionosphere Electron Density

<!-- b000586 | furniture | pages [27] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000587 | furniture | pages [27] -->
Team #76271

<!-- b000588 | furniture | pages [27] -->
26 of 30

<!-- b000589 | caption | pages [27] -->
Figure 9. Probability of Escaping to Space Versus Ionosphere Electron Density

<!-- b000590 | prose | pages [27] -->
Signal Remaining After First Bounce for Water (Part I) and Land (Part I)

<!-- b000591 | caption | pages [27] -->
Figure 10. Average Power Directly After First Bounce for Calm and Turbulent Water

<!-- b000592 | furniture | pages [28] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000593 | furniture | pages [28] -->
Team #76271

<!-- b000594 | furniture | pages [28] -->
27 of 30

<!-- b000595 | caption | pages [28] -->
Figure 11. Average Power Directly After First Bounce for Smooth and Rugged Terrain

<!-- b000596 | prose | pages [28] -->
Results of Frequency and Elevation Angle Sweep Sensitivity Analysis

<!-- b000597 | caption | pages [28] -->
Figure 12. Average Number of Bounces

<!-- b000598 | furniture | pages [29] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000599 | furniture | pages [29] -->
Team #76271

<!-- b000600 | furniture | pages [29] -->
28 of 30

<!-- b000601 | caption | pages [29] -->
Figure 13. Net Arc Length on the Earth from the Starting Point a.k.a. Total Distance in km

<!-- b000602 | caption | pages [29] -->
Figure 14. Percentage of Signals that are Absorbed by Loss as Opposed to Escaping to Space

<!-- b000603 | furniture | pages [30] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000604 | furniture | pages [30] -->
Team #76271

<!-- b000605 | furniture | pages [30] -->
29 of 30

<!-- b000606 | prose | pages [30] -->
Results of Ocean Turbulence Sensitivity Analysis

<!-- b000607 | caption | pages [30] -->
Figure 15. Total Distance Travelled Related to Ocean Turbulence. Calm distances are sta-

<!-- b000608 | prose | pages [30] -->
tistically different than both turbulent oceans.

<!-- b000609 | prose | pages [30] -->
Results of Transmit Power Sensitivity Analysis

<!-- b000610 | caption | pages [30] -->
Figure 16. Total Distance Travelled Related to Initial Power of Signal

<!-- b000611 | furniture | pages [31] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000612 | furniture | pages [31] -->
Team #76271

<!-- b000613 | furniture | pages [31] -->
30 of 30

<!-- b000614 | prose | pages [31] -->
Results of Ionosphere Electron Density Sensitivity Analysis

<!-- b000615 | caption | pages [31] -->
Figure 17. Total Distance Travelled Depending on Solar Activity

<!-- b000616 | prose | pages [31] -->
Results from Geographic Locations in Part III

<!-- b000617 | caption | pages [31] -->
Figure 18. Dispersion of Radio Signal Originating from Honduras
