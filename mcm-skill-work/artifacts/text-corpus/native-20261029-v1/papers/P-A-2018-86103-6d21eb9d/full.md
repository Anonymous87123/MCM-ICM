# P-A-2018-86103-6d21eb9d

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000002 | furniture | pages [1] -->
Team Control Number

<!-- b000003 | prose | pages [1] -->
For office use only For office use only

<!-- b000004 | title | pages [1] -->
86103

<!-- b000005 | prose | pages [1] -->
T1 F1

<!-- b000006 | prose | pages [1] -->
T2 F2

<!-- b000007 | prose | pages [1] -->
Problem Chosen T3 F3

<!-- b000008 | title | pages [1] -->
A

<!-- b000009 | prose | pages [1] -->
T4 F4

<!-- b000010 | prose | pages [1] -->
2018

<!-- b000011 | prose | pages [1] -->
MCM/ICM

<!-- b000012 | heading | pages [1] -->
Summary Sheet

<!-- b000013 | title | pages [1] -->
Simulation Analysis of Multi-hop HF Radio

<!-- b000014 | heading | pages [1] -->
Summary

<!-- b000015 | prose | pages [1] -->
HF radio propagation plays an extremely important role in communication at sea and mountains. It may be influenced by various factors, resulting in great loss of signal transmission. In this paper we focus on transmission and reflection loss of HF radio propagation in reflecting surface changes.

<!-- b000016 | prose | pages [1] -->
First, according to the PM wave spectrum and random wave theory, we establish a three-dimensional random wave model to simulate the motion of waves. On this ba- sis, we analyze the reflection of electromagnetic waves on the sea surface. We consider the influence of wave height caused by different wind levels on the reflection coefficient and obtain the reflection loss of electromagnetic wave under different conditions suc- cessfully. Then we get the sum of the lossin the transmission and the The first reflection intensity of the turbulent ocean and the calm one. At last we analyze the signal electric- field and atmospheric noise electric field of the receiving point, get the relation between SNR, transmission distance and hops, and the maximum number of hops should be 6 when SNR attenuates to 10dB.

<!-- b000017 | prose | pages [1] -->
Second, we analyze the transmission on the ground on the basis of the wave model. We simulate the topography with the wave fluctuation. Because the electromagnetic characteristics of the earth are different from the sea surface, we correct the relative di- electric constant and conductivity. Since there are more obstacles on the ground than on the sea, so we also analyze the diffraction phenomenon of electromagnetic wave prop- agation on the ground. We calculate and compare the first reflection intensity between mountainous or rugged terrain and smooth terrain. Surprisingly, the effectivedistance of sky-wave transmission is shorter than that of sea surface reflection. Under the same conditions, the maximum number of hops of HF radio propagation is4.

<!-- b000018 | prose | pages [1] -->
Finally, we consider the wind and waves that the ship may encounter on the sea sur- face, and calculate the longest distance that the received signal can propagate at a given wind level (i.e., SNR not less than 10 dB). Because ships usually travel longer, we also analyze the periodic variation of the ionosphere with time, and obtain the influence of the periodic variation of the ionosphere on the propagation of sky wave. On the basis of this, we get the optimal radio frequency under different conditions. After taking the ship speed into account, we amend the original model and obtain the maximum time for the ship to maintain the same multi-hop path.

<!-- b000019 | furniture | pages [2] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000020 | prose | pages [2] -->
Simulation Analysis of Multi-hop HF Radio

<!-- b000021 | heading | pages [2] -->
Abstract

<!-- b000022 | prose | pages [2] -->
HF radio is widely used in long-distance propagation in a lot of countries because of its advantages of long propagation distance, low transmission loss and no external influence on the quality of propagation, especially maritime propagation.

<!-- b000023 | prose | pages [2] -->
Because it is capable of reflections off the ionosphere and the earth, "jumping" to its destination. Besides, the characteristics of the reflected surface determine the intensity of the reflected waves and the extent to which the signal eventually travels. In this paper, we simulate different environments of the ocean and ground, and obtain the degree of signal loss and the propagation distance finally.

<!-- b000024 | heading | pages [2] -->
Ocean wave model

<!-- b000025 | prose | pages [2] -->
According to the wave spectrum and random wave theory, we take the actual wave as the superposition result of sinusoidal wave with different frequency, different propagation direction, different wave height and different initial phase. Then we establish the Longuet- Higgins long peak wave model. On this basis, we analyze the possible superposition of waves, and get the three-dimensional simulation diagram of the waves, and simulate it.

<!-- b000026 | caption | pages [2] -->
Figure 1 The wave situation

<!-- b000027 | prose | pages [2] -->
when the wind scale is 6

<!-- b000028 | prose | pages [2] -->
Transmission loss analysis

<!-- b000029 | prose | pages [2] -->
In the process of transmission, SNR of the signal may be reduced due to various factors. For a fixed reception point, the loss of the signal is related to the angle of the signal emission, the transmission distance, the ionospheric absorption intensity, sea situation and so on. We have a simple classification of the loss of the signal: free space transmission loss, ionospheric absorption loss, additional loss and sea surface reflection loss.

<!-- b000030 | prose | pages [2] -->
Then, we lay special stress on the relationship between sea surface reflection loss and various factors. By simulating the reflection path, we study the relationship between reflection path and reflection coefficient, and draw the conclusion that when the hop count is 1, the relationship between the first reflection intensity and the wind scale is as follows:

<!-- b000031 | caption | pages [2] -->
Figure 2 The relationship between the wind scale

<!-- b000032 | prose | pages [2] -->
and the first reflection intensity

<!-- b000033 | prose | pages [2] -->
In long-distance propagation, the number of multi-hop is often greater than 1 so that the wave can travel enough distance. But the integrity of the signal also attenuates gradually with the propagation. By calculation, we know that the maximum number of hops at calm sea is 6 when the power is 100 w and the frequency is 15 MHz.

<!-- b000034 | furniture | pages [3] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000035 | prose | pages [3] -->
Compare with the

<!-- b000036 | heading | pages [3] -->
model on the ground

<!-- b000037 | prose | pages [3] -->
Based on the three-dimensional wave model, we simulate the relief of the terrain with the wave fluctuation. Considering diffraction may occur during the ground propagation, and the variation of the conductivity and relative dielectric constant caused by the complex ground.

<!-- b000038 | prose | pages [3] -->
We modify the existing models, calculate the first reflection intensity and the maximum number of hops on different ground forms.

<!-- b000039 | prose | pages [3] -->
Modification based on navigation

<!-- b000040 | prose | pages [3] -->
In the actual navigation, the receiving point is motional. Thus, it cannot be regarded as a fixed point and to be calculated.

<!-- b000041 | prose | pages [3] -->
So we modify the model to calculate the emission angle, frequency, power and so on as variables. Based on these, we obtain the maximum distance and the time to maintain the same multi-hop path before the SNR attenuates to 10 dB. We also conclude that the absorption loss will increase due to the periodic variation of the ionosphere. So the launch frequency needs to be adjusted at different times.

<!-- b000042 | furniture | pages [4] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000043 | furniture | pages [4] -->
Team # 86103

<!-- b000044 | furniture | pages [4] -->
Page 1 of 25

<!-- b000045 | heading | pages [4] -->
Contents

<!-- b000046 | contents | pages [4] -->
1

<!-- b000047 | heading | pages [4] -->
Introduction

<!-- b000048 | prose | pages [4] -->
3

<!-- b000049 | prose | pages [4] -->
Background................................................................................................................. 3 1.1

<!-- b000050 | prose | pages [4] -->
Restatement of the problem...................................................................................... 3 1.2

<!-- b000051 | prose | pages [4] -->
2

<!-- b000052 | heading | pages [4] -->
Assumptions

<!-- b000053 | prose | pages [4] -->
3

<!-- b000054 | heading | pages [4] -->
Notation

<!-- b000055 | prose | pages [4] -->
4

<!-- b000056 | heading | pages [4] -->
Radio propagation on sea surface model

<!-- b000057 | prose | pages [4] -->
3

<!-- b000058 | prose | pages [4] -->
4

<!-- b000059 | prose | pages [4] -->
4

<!-- b000060 | prose | pages [4] -->
Introduction to HF propagation...............................................................................4 4.1

<!-- b000061 | prose | pages [4] -->
Way of HF propagation.................................................................................4 4.1.1

<!-- b000062 | prose | pages [4] -->
Structure of ionosphere.................................................................................5 4.1.2

<!-- b000063 | prose | pages [4] -->
Best usable frequency....................................................................................5 4.1.3

<!-- b000064 | prose | pages [4] -->
Wave model.................................................................................................................6 4.2

<!-- b000065 | prose | pages [4] -->
Longuet - Higgins wave model................................................................... 6 4.2.1

<!-- b000066 | prose | pages [4] -->
Three dimensional wave model...................................................................6 4.2.2

<!-- b000067 | prose | pages [4] -->
Model simulation...........................................................................................7 4.2.3

<!-- b000068 | prose | pages [4] -->
Transmission loss of HF radio waves Lb................................................................. 7 4.3

<!-- b000069 | prose | pages [4] -->
Free space transmission loss Lbf...................................................................8 4.3.1

<!-- b000070 | prose | pages [4] -->
Ionospheric absorption lossLa......................................................................8 4.3.2

<!-- b000071 | prose | pages [4] -->
Sea surface reflection loss Lg.........................................................................9 4.3.3

<!-- b000072 | prose | pages [4] -->
Additional loss YP.........................................................................................12 4.3.4

<!-- b000073 | prose | pages [4] -->
First reflection intensity...........................................................................................12 4.4

<!-- b000074 | prose | pages [4] -->
Calculation of SNR...................................................................................................13 4.5

<!-- b000075 | prose | pages [4] -->
4.5.1 HF sky-wave field intensity

<!-- b000076 | prose | pages [4] -->
[10]......................................................................................................................................13

<!-- b000077 | prose | pages [4] -->
Field intensity of atmospheric noise......................................................... 14 4.5.2

<!-- b000078 | prose | pages [4] -->
Maximum number of hops.........................................................................14 4.5.3

<!-- b000079 | heading | pages [4] -->
Comparison between sea surface model and ground surface model

<!-- b000080 | prose | pages [4] -->
5 15

<!-- b000081 | prose | pages [4] -->
Motion analysis of ships using HF radio propagation on turbulent ocean 6 16

<!-- b000082 | furniture | pages [5] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000083 | furniture | pages [5] -->
Team # 86103

<!-- b000084 | furniture | pages [5] -->
Page 2 of 25

<!-- b000085 | prose | pages [5] -->
Maximum time(tmax) using the same multi-hop path......................................... 16 6.1

<!-- b000086 | prose | pages [5] -->
Suggestions on frequency selection of transmitter..............................................18 6.2

<!-- b000087 | prose | pages [5] -->
7

<!-- b000088 | heading | pages [5] -->
Strengths and weaknesses

<!-- b000089 | prose | pages [5] -->
18

<!-- b000090 | prose | pages [5] -->
Strengths.................................................................................................................... 18 7.1

<!-- b000091 | prose | pages [5] -->
Weaknesses................................................................................................................18 7.2

<!-- b000092 | heading | pages [5] -->
Appendices

<!-- b000093 | prose | pages [5] -->
21

<!-- b000094 | heading | pages [5] -->
Appendix A First appendix

<!-- b000095 | prose | pages [5] -->
21

<!-- b000096 | furniture | pages [6] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000097 | furniture | pages [6] -->
Team # 86103

<!-- b000098 | furniture | pages [6] -->
Page 3 of 25

<!-- b000099 | prose | pages [6] -->
1

<!-- b000100 | heading | pages [6] -->
Introduction

<!-- b000101 | prose | pages [6] -->
1.1

<!-- b000102 | heading | pages [6] -->
Background

<!-- b000103 | prose | pages [6] -->
It is universally acknowledged that a ship sailing in the boundless sea will encounter a variety of danger at any time. With the increasing number of ships in the world and the trend toward large-scale and high-speed ocean shipping, the world’s waterways are becoming more and more crowded and crisis may occur at any time. In this case, HF radio propagation has played a significant role. HF radio propagation can attract us to transmitting messages, thats mainly because that HF communication can be achieved only by appropriate transmitting power and moderate equipment cost even far apart.

<!-- b000104 | prose | pages [6] -->
1.2 Restatement of the problem

<!-- b000105 | prose | pages [6] -->
As required by the question, we are supposed to determine the strength of the first re- flection off a turbulent ocean and compare it with the strength off a calm ocean. Mean- while, we will also determine the maximum number of hops the signal can take before its strength falls below a usable SNR. After that, we will compare the findings with hf reflections off different topography. Moreover, we are going to change our model to accommodate a shipboard receiver moving on a turbulent ocean.

<!-- b000106 | prose | pages [6] -->
There are two forms of shortwave propagation. One is ground wave, which consists of surface wave, direct wave and reflected wave; and another is sky wave that reaches the ground reception point being reflected by the ionospheric. In this article, we only model the reflection of sky waves.

<!-- b000107 | prose | pages [6] -->
2

<!-- b000108 | heading | pages [6] -->
Assumptions

<!-- b000109 | prose | pages [6] -->
• We consider the transmission of sky waves as the main way. Reason: Energy is lost with the propagation of ground wave, and the higher the frequency(that is, the shorter the wave length), the greater the loss. However, sky-wave communication has the advantages of long propagation distance, low transmission loss and not being affected by the geological types of both sides. So we consider the transmission of sky waves as the main way.

<!-- b000110 | prose | pages [6] -->
• The reflection of sky-waves in the ionosphere is mainly considered in the F2 layer. Reason: (1) It’s exist all day. (2) It’s height can accommodate the longest path. (3) MUF(maximum usable frequency) is the biggest.

<!-- b000111 | prose | pages [6] -->
• The main factor affecting wave height is wind speed.

<!-- b000112 | prose | pages [6] -->
• We regard the relative permittivity and conductivity of seawater as fixed values. Reason: The changes of relative dielectric constant and conductivity are mainly

<!-- b000113 | furniture | pages [7] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000114 | furniture | pages [7] -->
Team # 86103

<!-- b000115 | furniture | pages [7] -->
Page 4 of 25

<!-- b000116 | prose | pages [7] -->
caused by the change of salt content and temperature, and the wave and sea wa- ter motion have little effect on them, so we think that they are almost unchanged, and regard them as fixed values.

<!-- b000117 | prose | pages [7] -->
• We consider ships movement on the sea as a uniform motion.

<!-- b000118 | prose | pages [7] -->
3

<!-- b000119 | heading | pages [7] -->
Notation

<!-- b000120 | heading | pages [7] -->
Notation

<!-- b000121 | prose | pages [7] -->
Definition Lb Transmission loss Lbf Free space transmission loss La Ionospheric absorption loss Lg Ground reflection loss ε Electric medium constant σ Conductivity YP Additional loss r Propagation distance D Maximum propagation distance Elevation angle of transmission ∆ n Number of hops f Working frequency P0 Power of the transmitter P1 First reflection intensity R Reflection coefficient θ Incidence angle of electromagnetic wave

<!-- b000122 | prose | pages [7] -->
P.s. Other symbols instruction will be given in the text.

<!-- b000123 | prose | pages [7] -->
4

<!-- b000124 | heading | pages [7] -->
Radio propagation on sea surface model

<!-- b000125 | prose | pages [7] -->
4.1

<!-- b000126 | heading | pages [7] -->
Introduction to HF propagation

<!-- b000127 | prose | pages [7] -->
4.1.1 Way of HF propagation

<!-- b000128 | prose | pages [7] -->
HF propagation is the radio propagation of radio waves in the range of 3 to 30MHz(corre- sponding wave length 100 to 10m). HF communication has the advantages of long communication distance, strong persistence and simple equipment,meanwhile, it has the disadvantages of channel congestion, time-varying, dispersion characteristics, and so on. Moreover, it is easy to be influenced by other external factors and is unstable. HF propagation can propagate along the ground as the ground-wave, and it can also prop- agate through reflections off the ionospheric as the sky-wave. The propagation diagram is as follows:

<!-- b000129 | furniture | pages [8] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000130 | furniture | pages [8] -->
Team # 86103

<!-- b000131 | furniture | pages [8] -->
Page 5 of 25

<!-- b000132 | caption | pages [8] -->
Figure 1 HF propagation diagram

<!-- b000133 | prose | pages [8] -->
4.1.2 Structure of ionosphere

<!-- b000134 | prose | pages [8] -->
Ionosphere is a ionization region of the earths atmosphere. It is ionized by highenergy radiation from the sun and cosmic rays. For the existence of a huge number of free electrons and ions, radio waves can change the speed of propagation ,and refraction, reflection and scattering occurred. The ionosphere can be divided into layer D, E, F

<!-- b000135 | prose | pages [8] -->
[1]. The height of each layer

<!-- b000136 | prose | pages [8] -->
and so on, and the layer F can be divided into F1 and F

<!-- b000137 | prose | pages [8] -->
2

<!-- b000138 | prose | pages [8] -->
changes over time, and some layers even disappear at night.

<!-- b000139 | caption | pages [8] -->
Figure 2 Inner layers of ionosphere

<!-- b000140 | prose | pages [8] -->
4.1.3 Best usable frequency

<!-- b000141 | prose | pages [8] -->
According to the theory of ionospheric propagation, shortwave with a higher frequency can only return to the ground from the reflection off ionosphere with a higher electron density distribution. There is a maximum frequency of radio waves that can be reflected back to the ground, which we call MUF(maximum usable frequency). the frequency of propagation should be as high as possible to reduce absorption, but generally only at the frequency of 0.85 MUF. Because if we use MUF, as long as the ionosphere changes slightly, the radio waves would go through the ionosphere without going back. So we

<!-- b000142 | prose | pages [8] -->
[2]the best usablefrequency.

<!-- b000143 | prose | pages [8] -->
call the frequency of 0.85 MUF

<!-- b000144 | furniture | pages [9] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000145 | furniture | pages [9] -->
Team # 86103

<!-- b000146 | furniture | pages [9] -->
Page 6 of 25

<!-- b000147 | prose | pages [9] -->
4.2

<!-- b000148 | heading | pages [9] -->
Wave model

<!-- b000149 | prose | pages [9] -->
4.2.1

<!-- b000150 | heading | pages [9] -->
Longuet - Higgins wave model

<!-- b000151 | prose | pages [9] -->
The wave phenomenon is very complex, and its speculative and nonlinear. Therefore, it is very difficult to establish an accurate wave model. According to the wave spectrum and random wave theory, we can regard the actual wave as the result of sinusoidal wave superposition with different frequency, different propagation directions, different wave

<!-- b000152 | prose | pages [9] -->
[3] describes the waves

<!-- b000153 | prose | pages [9] -->
heights and different initial phases. The Longuet-Higgins model

<!-- b000154 | prose | pages [9] -->
of long-peak waves by the superposition of countless random cosine waves, and the amplitude is expressed as follows:

<!-- b000155 | prose | pages [9] -->
Where ξai refers to the amplitude of the i cosine wave, ωi refers to the frequency of the i cosine wave, and εi refers to the phase of the i cosine wave.

<!-- b000156 | prose | pages [9] -->
In practical applications, the Longuet-Higgins model is often expressed by the wave spectrum:

<!-- b000157 | prose | pages [9] -->
In the formula, Sζ ∆ωis the wave spectrum. At present, there are several widely used ocean spectrum,such as Pierson-Moscowitz spectrum(PM spectrum), Neumann spectrum(N spectrum), ITTC spectrum and so on, among which PM spectrum is the most widely used. It can well represent the fully developed random waves. Therefore, we use the PM spectrum. And the expression of PM spectrum is as follows:

<!-- b000158 | prose | pages [9] -->
Where v is the wind speed with a height of 19.5m above the sea level.

<!-- b000159 | prose | pages [9] -->
4.2.2

<!-- b000160 | heading | pages [9] -->
Three dimensional wave model

<!-- b000161 | prose | pages [9] -->
In the above model, we consider only one direction. But in the actual wave, the wave not only changes in height and frequency, but also spread in more than one direction. So ±π/2inthemainwaveasthreedimensionalirregularshortpeakrandomwavemodel. we define the waves which are superimposed on each other and diffused randomly to

<!-- b000162 | prose | pages [9] -->
We overlay the above model in many directions, and finally we get the following expression:

<!-- b000163 | prose | pages [9] -->
Where ζaij , ωi , ki , µj and εij are the amplitude, the angular frequency, the wave number, the direction angle and the random initial phase of the component harmonics, εij is random number between 0 and π/2, (ξ, η)is the coordinates of a certain point on a wave surface.

<!-- b000164 | furniture | pages [10] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000165 | furniture | pages [10] -->
Team # 86103

<!-- b000166 | furniture | pages [10] -->
Page 7 of 25

<!-- b000167 | prose | pages [10] -->
4.2.3

<!-- b000168 | heading | pages [10] -->
Model simulation

<!-- b000169 | prose | pages [10] -->
We simulated the model in MATLAB, and the results are as follows:

<!-- b000170 | caption | pages [10] -->
Figure 3 Wave situation of 5∼8 winds

<!-- b000171 | prose | pages [10] -->
Transmission loss of HF radio waves Lb 4.3

<!-- b000172 | prose | pages [10] -->
During the transmission of radio waves, there are many factors that can affect the trans- mission loss. We divide the basic transmission loss(Lb) during the whole propagation process into four parts: free space transmission loss Lbf , ionospheric absorption loss La , ground reflection loss Lg, and additional loss YP . If all losses are expressed in deci- bel(dB), the basic transmission loss of sky-wave propagation is as follows:

<!-- b000173 | prose | pages [10] -->
(5) Lb = Lbf + Li + Lg + YP

<!-- b000174 | caption | pages [10] -->
Figure 4 Parts of transmission loss

<!-- b000175 | furniture | pages [11] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000176 | furniture | pages [11] -->
Team # 86103

<!-- b000177 | prose | pages [11] -->
Free space transmission loss Lbf 4.3.1

<!-- b000178 | furniture | pages [11] -->
Page 8 of 25

<!-- b000179 | prose | pages [11] -->
The free space transmission loss is the loss of energy caused by geometric factors after

<!-- b000180 | prose | pages [11] -->
[4]:

<!-- b000181 | prose | pages [11] -->
radio wave detaching antenna. The equality of Lbf is as follows

<!-- b000182 | prose | pages [11] -->
(6) Lbf = 32.44 + 20lgf + 20lgr

<!-- b000183 | prose | pages [11] -->
Where f is the working frequency in MHz and r is the effective path of HF radio propagation in km.

<!-- b000184 | prose | pages [11] -->
The curvature of the earth and the height of the ionosphere limit the one-time maxi-

<!-- b000185 | prose | pages [11] -->
[5]:

<!-- b000186 | prose | pages [11] -->
mum jump distance of the reflection off the ionosphericDmax

<!-- b000187 | prose | pages [11] -->
In the equation, ∆min is the minimum elevation angle of the antenna, and we know that the general elevation angle of the antenna is greater than 3◦. The Re is the radius of the earth, and we value it as 6371km. The h is the reflection virtual height of the ionosphere. The height of each layer is shown in the diagram. For F2 reflection, the maximum propagation distance Dmax is 4000km.

<!-- b000188 | prose | pages [11] -->
Ionospheric absorption lossLa 4.3.2

<!-- b000189 | prose | pages [11] -->
In HF radio propagation, the loss caused by ionospheric absorption mainly occurs in layer D, because there are more neutral molecules in layer D and the collision loss is

<!-- b000190 | prose | pages [11] -->
[6]. The concentration of electrons in layer D decreases at night, and the absorption

<!-- b000191 | prose | pages [11] -->
larger

<!-- b000192 | prose | pages [11] -->
loss decreases. The loss is mainly non-offset absorption. The emission absorption in

<!-- b000193 | prose | pages [11] -->
very small (≤1 dB).

<!-- b000194 | prose | pages [11] -->
[7] . We ignore it in calculation for its

<!-- b000195 | prose | pages [11] -->
layer 4 E or F mainly refers to offset absorption

<!-- b000196 | prose | pages [11] -->
Whereϕistheincidentangleataheightof100km,f(MHz)istheworkingfrequency and fH(MHz) is the gyromagnetic frequency,I is the absorption index and n is number of hops in the path.

<!-- b000197 | prose | pages [11] -->
The absorption index I is:

<!-- b000198 | prose | pages [11] -->
(9) I = (1 +0.037R)(cos 0.881χ)1.3

<!-- b000199 | prose | pages [11] -->
Where R is the number of sunspots and χ is the zenith angle of two 100 km high absorbs.

<!-- b000200 | prose | pages [11] -->
For the ionospheric absorption loss is related to transmitter, issue time and teh pa- rameters of receiving spots, and that the calculation is too complex, we take it as 4dB to make the calculation easy.

<!-- b000201 | furniture | pages [12] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000202 | furniture | pages [12] -->
Team # 86103

<!-- b000203 | furniture | pages [12] -->
Page 9 of 25

<!-- b000204 | prose | pages [12] -->
Sea surface reflection loss Lg 4.3.3

<!-- b000205 | prose | pages [12] -->
(1) Calm sea reflection

<!-- b000206 | prose | pages [12] -->
For multi-hop sea surface reﬂection loss suppose incident wave is messy polariza-tionThe energy of the radio waves is evenly distributed on the horizontal and vertical polarizations, so that the formula for calculating the energy is

<!-- b000207 | prose | pages [12] -->
(10)

<!-- b000208 | prose | pages [12] -->
WhereRHandRVarethereﬂectioncoefﬁcientsofhorizontalandverticalpolarizedwaves, respectively, as follows:

<!-- b000209 | prose | pages [12] -->
Where θ is the incident angle, is the complex permittivity of the sea surface, ε is the permittivity of seawater, λ is the wavelength of the incident wave and σ is the con-ductivity. Accordingtothisformula,therelationshipbetweenRH，Rvandtheangleofincidence.

<!-- b000210 | caption | pages [12] -->
Figure 5 The relationship between RH , RV and incidence angle

<!-- b000211 | prose | pages [12] -->
Accordingtothe ﬁgure,it isnotdifﬁcultto ﬁnd thatforthehorizontal polarized wave,the reﬂection coefﬁcientdecreases graduallyfrom 1, while the amplitude is verysmall.For the vertical polarized wave, with the reﬂection coefﬁcient increases with the increase of the incident angle,thereﬂectioncoefﬁcientincreasesto1gradually afterde-creasingrapidlyatﬁrst.The comparison shows that the change of reﬂection coefﬁcient

<!-- b000212 | furniture | pages [13] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000213 | furniture | pages [13] -->
Team # 86103

<!-- b000214 | furniture | pages [13] -->
Page 10 of 25

<!-- b000215 | prose | pages [13] -->
of the horizontal polarization wave is much more sensitive to the incident angle.

<!-- b000216 | heading | pages [13] -->
(2) Ocean Wave Model algorithm for turbulentocean

<!-- b000217 | prose | pages [13] -->
Forthe three dimensionalirregular short-peak randomwave model mentioned above, we randomly select a wave cross section to analyze. When the electromagnetic wave shines on the wave, most of the available electromagnetic waves are emitted in the form of reflection and scattering, and reflection is the main one.

<!-- b000218 | caption | pages [13] -->
Figure 6 Diagram of electromagnetic wave reflection on turbulent ocean

<!-- b000219 | prose | pages [13] -->
For the wave function ξ(x) of this cross section at a certain time, we take the deriva- tive of it and obtain the tangent equation of the section irradiated by electromagnetic

<!-- b000220 | prose | pages [13] -->
y = ξ′(x)(x −x0) + y0

<!-- b000221 | prose | pages [13] -->
wave.

<!-- b000222 | prose | pages [13] -->
(14)

<!-- b000223 | prose | pages [13] -->
Where (x0, y0) is the coordinate of surface element α. According to Sneel’s law, we assume that the grazing angle of electromagnetic wave incident to plane α is θ, and then we obtain the propagation path equation of reflected wave as shown below:

<!-- b000224 | prose | pages [13] -->
y = tan(∆+ arctan ξ′(x))(x −x0) + y0 (15)

<!-- b000225 | prose | pages [13] -->
Because the water surface has a certain dip angle, the full incident wave cant be reflected in the positive direction. Therefore, we differentiate the wave surface, analyze each micro-element plane, and find out the total number of reflected waves reflected in the forward direction, and get the correction coefficient finally:

<!-- b000226 | prose | pages [13] -->
m (16) ρ = M

<!-- b000227 | prose | pages [13] -->
Where m is the total number of positive and negative reflection electromagnetic waves and M is the total number of incident electromagnetic waves.

<!-- b000228 | furniture | pages [14] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000229 | furniture | pages [14] -->
Team # 86103

<!-- b000230 | furniture | pages [14] -->
Page 11 of 25

<!-- b000231 | caption | pages [14] -->
Figure 7 Diagram of wave shadow

<!-- b000232 | prose | pages [14] -->
As shown in the figure, the actual waves will have ups and downs. Especially when the wind and waves are high, some of the sea surface will be covered by the waves. At this point, we have corrected the occluded part, ignoring the reflected light in that part. The correction method is as follows:

<!-- b000233 | prose | pages [14] -->
We obtain the second derivative for wave function ξ(x) and obtain the tangent equa- tion of extreme value point corresponding to its extreme point. Then the second inter- section point of electromagnetic wave and wave is the intersection point of the equation

<!-- b000234 | prose | pages [14] -->
S −s

<!-- b000235 | prose | pages [14] -->
and wave function, and the shading is the shaded area.

<!-- b000236 | prose | pages [14] -->
∗

<!-- b000237 | prose | pages [14] -->
ρ′ = ρ

<!-- b000238 | prose | pages [14] -->
(17)

<!-- b000239 | prose | pages [14] -->
S

<!-- b000240 | prose | pages [14] -->
Where S is the surface area of a wave and s is the shaded area.

<!-- b000241 | caption | pages [14] -->
Figure 8 Diagrams of correction coefficients

<!-- b000242 | furniture | pages [15] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000243 | furniture | pages [15] -->
Team # 86103

<!-- b000244 | furniture | pages [15] -->
Page 12 of 25

<!-- b000245 | prose | pages [15] -->
In the figure above, the left image shows the correction coefficients at different wind speeds when the grazing angle is 1◦/5◦/15◦, and the right image shows the correction coefficients at different wind speeds when the frequency is 10 MHz / 20 MHz / 30 MHz.

<!-- b000246 | prose | pages [15] -->
Wecan get the following curve, which is the final reflection coefficient bymultiply- ing it with the reflection coefficient when it is stationary:

<!-- b000247 | caption | pages [15] -->
Figure 9 Relation curve of reflection coefficient under different wind speed

<!-- b000248 | prose | pages [15] -->
Then we can get the loss of turbulent ocean:

<!-- b000249 | prose | pages [15] -->
L′g = Lg −10 lg(ρ′) (18)

<!-- b000250 | prose | pages [15] -->
Additional loss YP 4.3.4

<!-- b000251 | prose | pages [15] -->
Additional loss is the loss caused by other factors in addition to the main reasonsmen- tioned above. The detailed calculation is too complicated, but we conclude that it is

<!-- b000252 | prose | pages [15] -->
[9].

<!-- b000253 | prose | pages [15] -->
mainly related to local time, which is assumed to be about 15 dB here

<!-- b000254 | prose | pages [15] -->
4.4 First reflection intensity

<!-- b000255 | prose | pages [15] -->
Combined with the loss analysis above, for a single jump signal source, we can get the following formula:

<!-- b000256 | prose | pages [15] -->
10lg(P1) = 10lg(P0) −Lbf −La −Lg −YP (19)

<!-- b000257 | prose | pages [15] -->
Among them, P1(w) is the electromagnetic wave power of the transmitting point and P0(w) is the first reflection intensity. For the electromagnetic wave propagation

<!-- b000258 | furniture | pages [16] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000259 | furniture | pages [16] -->
Team # 86103

<!-- b000260 | furniture | pages [16] -->
Page 13 of 25

<!-- b000261 | prose | pages [16] -->
route which has been determined in both time and space, only Lg is alterable because of the different sea conditions, we get the following chart bycalculation:

<!-- b000262 | caption | pages [16] -->
Figure 10 The strength of the first reflection P1

<!-- b000263 | caption | pages [16] -->
Table 1 Related Parameters

<!-- b000264 | prose | pages [16] -->
Reference value Unit Parameter 4 La 15 YP 100 f

<!-- b000265 | prose | pages [16] -->
100

<!-- b000266 | prose | pages [16] -->
P0 θ

<!-- b000267 | prose | pages [16] -->
3

<!-- b000268 | prose | pages [16] -->
dB dB MHz

<!-- b000269 | prose | pages [16] -->
w

<!-- b000270 | prose | pages [16] -->
◦

<!-- b000271 | prose | pages [16] -->
As is shown in the figure, its the first reflection intensity of a signal with different frequencies under different wind speeds. We can get the curve of reflection intensity changing with sea condition by fitting. From the diagram, we can know that the first reflection intensity decreases with the increase of frequency and the increase of wind speed. Thus, we must consider the influence of weather in the process of maritime communication.

<!-- b000272 | prose | pages [16] -->
4.5 Calculation of SNR

<!-- b000273 | prose | pages [16] -->
[10]

<!-- b000274 | prose | pages [16] -->
4.5.1 HF sky-wave field intensity

<!-- b000275 | prose | pages [16] -->
The field strength of the receiving point can be calculated by the following formula:

<!-- b000276 | prose | pages [16] -->
Et= 137.2 + 20 lg f + 10 lg P 0+ Gt−Lb (20)

<!-- b000277 | prose | pages [16] -->
In the formula, Et(dB) is the signal intensity of the receiving point during the prop- agation of sky wave, f(MHz) is the working frequency, P(kw) is the power of the trans- mitter, tt(dB) is the normal gain of the transmitter antenna radiation, and Lb(dB) is the transmission loss of sky-wave.

<!-- b000278 | furniture | pages [17] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000279 | furniture | pages [17] -->
Team # 86103

<!-- b000280 | prose | pages [17] -->
4.5.2 Field intensity of atmospheric noise

<!-- b000281 | furniture | pages [17] -->
Page 14 of 25

<!-- b000282 | prose | pages [17] -->
[11] . It is the main noise source of ma-

<!-- b000283 | prose | pages [17] -->
Atmospheric noise is mainly caused by lightning

<!-- b000284 | prose | pages [17] -->
rine HF radio propagation at present. The formula for calculating the effective value of atmospheric noise field intensity is as follows:

<!-- b000285 | prose | pages [17] -->
En = Fa + 10 lg B + 20 lg f−96.8 (21)

<!-- b000286 | prose | pages [17] -->
In the formula, En(dB) is the field intensity of atmospheric noise, Fa(dB) is the ef- fective noise coefficient of atmospheric radio, B(dB) is the effective noise bandwidth of receiver, F(MHz) is working frequency.

<!-- b000287 | prose | pages [17] -->
Atmospheric noise is usually estimated by the noise data provided in the CCIR322nd report. A complete set of atmospheric noise data contains 72 charts. The calculation pro- cess is very complicated and the accuracy is not high enough. Thus we use themethod of establishing a database to make a simple estimate. The following figure shows the

<!-- b000288 | prose | pages [17] -->
[12].

<!-- b000289 | prose | pages [17] -->
atmospheric noise table at different times in a certain area in summer

<!-- b000290 | caption | pages [17] -->
Table 2 Atmospheric noise at different times in a certain area in summer

<!-- b000291 | prose | pages [17] -->
4.5.3 Maximum number of hops

<!-- b000292 | prose | pages [17] -->
According to the formula for calculating the electric field intensity of HF sky-wave and the formula for calculating the effective value of atmospheric noise field intensity, we obtain the formula for calculating signal-to-noise ratio of shortwave sky-wave commu- nication under natural conditions.

<!-- b000293 | prose | pages [17] -->
SNR = 201.56 + 10lgP0 −20lgf −20lgr −10lgB −La −Lg −YP −Fa (22)

<!-- b000294 | prose | pages [17] -->
In the formula, after n jumps, we found that

<!-- b000295 | prose | pages [17] -->
(23) r = nDmax

<!-- b000296 | prose | pages [17] -->
L′g = (n −1)× Lg

<!-- b000297 | prose | pages [17] -->
L′a = n × La

<!-- b000298 | prose | pages [17] -->
(24)

<!-- b000299 | prose | pages [17] -->
(25)

<!-- b000300 | prose | pages [17] -->
With reference to the following table for each parameter, we can get n = 6 by using the fsolve function of MATLAB.

<!-- b000301 | furniture | pages [18] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000302 | furniture | pages [18] -->
Team # 86103

<!-- b000303 | furniture | pages [18] -->
Page 15 of 25

<!-- b000304 | heading | pages [18] -->
Comparison between sea surface model and ground surface

<!-- b000305 | prose | pages [18] -->
5

<!-- b000306 | heading | pages [18] -->
model

<!-- b000307 | prose | pages [18] -->
Because the ground environment is more complicated than the sea surface and is com- posed of various materials, we take the relative permittivity of 3 to 8 as the basic value and the geodetic equivalent conductivity as the electrical conductivity in the calculation.

<!-- b000308 | prose | pages [18] -->
By using the proposed model and the algorithm proposed above, we take the undu- lation of the mountain as the motion of the wave and calculate it approximately. Because

<!-- b000309 | prose | pages [18] -->
there are many obstacles on the ground, the electromagnetic wave will be diffracted when it meets the obstacle. However, because the short wave wavelength is not enough to avoid obstacles, most of them will be blocked by various obstacles, so the propagation ability of short wave on the ground is very weak. According to the analysis,we substi- tute the electromagnetic parameters of ground into the formula and get the solutionas

<!-- b000310 | prose | pages [18] -->
[13]:

<!-- b000311 | prose | pages [18] -->
follows

<!-- b000312 | caption | pages [18] -->
Figure 11 Reflection coefficient relationship curves under different ground conditions

<!-- b000313 | prose | pages [18] -->
The related parameters are shown in the table.

<!-- b000314 | caption | pages [18] -->
Table 3 ε,σ in different environments

<!-- b000315 | prose | pages [18] -->
Variation Ground form ε(F/m) Average 1∼4.3 σ(S/m) ε(F/m) σ(S/m) 10−3 ∼2.4×10−2 Seawater 80 80 4

<!-- b000316 | prose | pages [18] -->
3×10−3 ∼2.4 × 10−2 10∼30

<!-- b000317 | prose | pages [18] -->
Freshwater 80 10−3 80

<!-- b000318 | prose | pages [18] -->
1.1×10−5 ∼2 × 10−2 3∼4

<!-- b000319 | prose | pages [18] -->
Wet soil

<!-- b000320 | prose | pages [18] -->
Dry soil

<!-- b000321 | prose | pages [18] -->
10−2 10

<!-- b000322 | prose | pages [18] -->
10−3 4

<!-- b000323 | prose | pages [18] -->
The first reflection intensity in hilly areas is as shown in the diagram, especially when the terrain is smooth, the relief degree is 0.

<!-- b000324 | furniture | pages [19] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000325 | furniture | pages [19] -->
Team # 86103

<!-- b000326 | furniture | pages [19] -->
Page 16 of 25

<!-- b000327 | caption | pages [19] -->
Figure 12 Strength of the first reflection

<!-- b000328 | prose | pages [19] -->
Wetake Lg as 6.53dB when the ground is flat and we get that n = 4. Compared with the sea surface, the propagation distance of the HF radio through the ground is much shorter than that of the sea surface.

<!-- b000329 | prose | pages [19] -->
6 Motion analysis of ships using HF radio propagation on tur- bulent ocean

<!-- b000330 | prose | pages [19] -->
Maximum time(tmax) using the same multi-hop path 6.1

<!-- b000331 | prose | pages [19] -->
In the above model, we only consider the condition that the reception point is fixed. This model is applicable to the communication between two fixed points , or the case where the position change of the receiving point is negligible. The ship in the turbulent ocean has a long moving distance, so we can not only calculate the effective propaga-

<!-- b000332 | prose | pages [19] -->
[14]. At this point, the propagation distance r is related

<!-- b000333 | prose | pages [19] -->
tion distance r as a fixed value

<!-- b000334 | prose | pages [19] -->
to the emission angle ∆, and La, Lg is related to n(the number of hops of sky-wave), meanwhile, Lg is also related to the emission angle ∆. To ensure that the received signal is clear enough, we conclude that the SNR should be greater than or equal to 10, that is:

<!-- b000335 | prose | pages [19] -->
SNR = 201.56+10 lg P 0 −20 lg f −20 lg r−10 lg B −nLa−(n−1)Lg −Yp−Fa ≥10 (24)

<!-- b000336 | prose | pages [19] -->
Through analysis, we know that since Lg is related to ∆, the longer the route distance is, the higher the power transmitter and the increase antenna are needed to assist the ship in the sea course. Or the radio frequency can be adjusted to avoid overattenuating to make the SNR too low and difficult to distinguish.

<!-- b000337 | furniture | pages [20] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000338 | furniture | pages [20] -->
Team # 86103

<!-- b000339 | furniture | pages [20] -->
Page 17 of 25

<!-- b000340 | caption | pages [20] -->
Figure 13 Relationships among distance, frequency and SNR

<!-- b000341 | prose | pages [20] -->
different frequencies and distances, with the number of hops n = 1 ∼6, the wind scale As shown in the figure, SNR of 100w signal is obtained at the receiving pointswith

<!-- b000342 | prose | pages [20] -->
is 5, and the receiving points at different frequencies and distances.

<!-- b000343 | caption | pages [20] -->
Table 4 Maximum propagation distance r when f=15Hz, P =100w

<!-- b000344 | prose | pages [20] -->
Maximum propagation distance r(km) Number of hops n 1 2 3 4 5 6 SNR(dB) 3225 54.0977 6449 23.2859 9674 16.9728 10125 10 <10125 10 <10125 10

<!-- b000345 | prose | pages [20] -->
We can know from the figure that when n is fixed, the propagation distance is insuf- ficient or the signal-to-noise ratio is too low with increasingdistance.

<!-- b000346 | prose | pages [20] -->
By analyzing the data above, we draw a conclusion that when the number of hops is too high, for the ship traveling on the turbulent sea surface, the signal reflects too many times between the sea surface and the ionosphere, and the loss of the propagation path is too large, which results in the decrease of the maximum propagation distance. It is not enough to spread the signal far enough. Therefore, in this case, we need to increase the transmission power or signal frequency to increase the signal-to-noise ratio and the maximum propagation distance.

<!-- b000347 | prose | pages [20] -->
In summary, the maximum time for ships to maintain multi-hop paths in turbulent ocean is :

<!-- b000348 | prose | pages [20] -->
tmax = r (27)

<!-- b000349 | prose | pages [20] -->
v

<!-- b000350 | prose | pages [20] -->
Where v is the speed of the ship moving at sea. In the case of the table above, the

<!-- b000351 | furniture | pages [21] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000352 | furniture | pages [21] -->
Team # 86103

<!-- b000353 | furniture | pages [21] -->
Page 18 of 25

<!-- b000354 | prose | pages [21] -->
multi-hop path must be changed for every 3000km movement. In the case of 100W and 15MHz, the signal power and frequency must be increased when the transmission distance is over 10000 km.

<!-- b000355 | prose | pages [21] -->
6.2 Suggestions on frequency selection oftransmitter

<!-- b000356 | prose | pages [21] -->
Because not only the periodic variation of the ionosphere,but also the influence of the day and night, the season, the solar activity and so on can affect the value of the iono- spheric propagation loss La. In order for ships to have better communication at sea, the emitter must choose different frequency at different time to achieve better propagation. The following table shows the range of radio broadcasts commonly used to take into account ionospheric effects:

<!-- b000357 | prose | pages [21] -->
2∼4 MHz

<!-- b000358 | caption | pages [21] -->
Table 5 Recommended emission frequency

<!-- b000359 | prose | pages [21] -->
Tropical frequency, small number of sunspots and transmission is good. 6∼7 MHz Some countries near the equator can use it as domestic broadcasting More suitable using in autumn and winter or night for close-range broa- 9∼11 MHz dcasting Moderate and suitable for all-day broadcasting both inside and outside 13 MHz Effect would be better at daytime and is suitable for long distance broa- 15∼17MHz dcasting Better in spring and summer

<!-- b000360 | prose | pages [21] -->
7

<!-- b000361 | heading | pages [21] -->
Strengths and weaknesses

<!-- b000362 | prose | pages [21] -->
7.1

<!-- b000363 | heading | pages [21] -->
Strengths

<!-- b000364 | prose | pages [21] -->
• Weclassify and analyze the propagation path, which makes our calculation more accurate.

<!-- b000365 | prose | pages [21] -->
• Wehave established a three-dimensional wave model, which is more intuitive.

<!-- b000366 | prose | pages [21] -->
• Weadopt the correction method of reflection coefficient, which is different from the previous empirical formula, and can analyze the reflection coefficient under different sea conditions quantitatively.

<!-- b000367 | prose | pages [21] -->
• Wetake the effects of periodic ionospheric variations into account, which are sensitive and can be used in various situations.

<!-- b000368 | prose | pages [21] -->
7.2

<!-- b000369 | heading | pages [21] -->
Weaknesses

<!-- b000370 | heading | pages [21] -->
• Weonly consider the HF sky-wave transmission model, but the ground-wave

<!-- b000371 | prose | pages [21] -->
transmission also has certain influence.

<!-- b000372 | prose | pages [21] -->
• In real life, the ionospheric loss is complicated and varies greatly with latitude, longitude, seasons and so on. However, we only calculate the reasonable values

<!-- b000373 | furniture | pages [22] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000374 | furniture | pages [22] -->
Team # 86103

<!-- b000375 | furniture | pages [22] -->
Page 19 of 25

<!-- b000376 | prose | pages [22] -->
according to the literature.

<!-- b000377 | prose | pages [22] -->
• We only focus on the characteristics of shortwave propagation at sea level and the effect of reflection without considering the effect of refractiondiffraction.

<!-- b000378 | prose | pages [22] -->
• The dielectric constant and conductivity of the reflected surface change with the frequency, but we only use the fixed value to calculate. When the salinity and temperature of seawater change sharply, the reliability of the data will decrease.

<!-- b000379 | furniture | pages [23] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000380 | furniture | pages [23] -->
Team # 86103

<!-- b000381 | furniture | pages [23] -->
Page 20 of 25

<!-- b000382 | heading | pages [23] -->
References

<!-- b000383 | references | pages [23] -->
[1] LI Wei. Influence of Ionospheric Characteristics on Shortwave Transmission[J]. In-

<!-- b000384 | references | pages [23] -->
ner Mongolia Radio & TV Broadcast Engineering,2016,33(06):68-71. Mathematical

<!-- b000385 | references | pages [23] -->
Society and Addison-Wesley Publishing Company , 1984-1986.

<!-- b000386 | references | pages [23] -->
[2] SHI Xiang-tong, WANG Lei, HU Bo. Frequency Selection of Shortwave Communi-

<!-- b000387 | references | pages [23] -->
cation Radio[J]. Ship Electronic Engineering, 2013, 33(10):39-41.

<!-- b000388 | references | pages [23] -->
[3] QI Ning, XIA Tian, LI Wen-yan, ZHAO Li-guang. Simulation of the Mathematical

<!-- b000389 | references | pages [23] -->
Model of 3-D Irregular Wave Based on MATLAB[J]. Computer Knowledge and

<!-- b000390 | references | pages [23] -->
Technology,2013,9(25):5737-5739.

<!-- b000391 | references | pages [23] -->
[4] PENG Feng-hua, ZHOU Xue-jun. Propagation of Maritime Short-wave Telecom-

<!-- b000392 | references | pages [23] -->
munication Link[J]. Ship Electronic Engineering,2011,31(12):125-127.

<!-- b000393 | references | pages [23] -->
[5] ZHAO Yu-cai. Research and Realization on Radio Propagation Prediction and

<!-- b000394 | references | pages [23] -->
Interference Analyzing Technology[D]. National University of Defense Technol-

<!-- b000395 | references | pages [23] -->
ogy,2009.

<!-- b000396 | references | pages [23] -->
[6] YUAN Xiao-bo. Shortwave Sky Wave Propagation Loss Prediction and Prediction

<!-- b000397 | references | pages [23] -->
of Field Strength[J]. Information & Communications,2013(05):11-12.

<!-- b000398 | references | pages [23] -->
[7] LI Xue-hongLI FazhongHAN LongCHEN Lijun. Method and Models of Field

<!-- b000399 | references | pages [23] -->
Strength Calculation in HF Sky Wave Communication[J]. Communications

<!-- b000400 | references | pages [23] -->
Technology,2016,49(04):418-422.

<!-- b000401 | references | pages [23] -->
[8] WANG Ying, GU Jian. Research and simulation analysis of radio reflection char-

<!-- b000402 | references | pages [23] -->
acteristic over the ocean[J]. International Electronic Elements, 2016, 24(05):113-

<!-- b000403 | references | pages [23] -->
115+119.

<!-- b000404 | references | pages [23] -->
[9] LUO Jia, ZHANG Wen-ming, WANG Xue-song. Modeling and Simulation of

<!-- b000405 | references | pages [23] -->
HF Skywave Transmission Loss in Communication Countermeasure[J]. Computer

<!-- b000406 | references | pages [23] -->
Simulation,2007(08):28-31+35.

<!-- b000407 | references | pages [23] -->
[10] DONG HangXU ChiYI TaoHAN Dong. HF Communication Aid DecisionMaking

<!-- b000408 | references | pages [23] -->
Model basedon SNR Evaluation[J]. CommunicationsTechnology,2014,47(11):1313-

<!-- b000409 | references | pages [23] -->
1317.

<!-- b000410 | references | pages [23] -->
[11] Qu Gui-cheng, Wang Rui. Research on the Feasibility of Shortwave Commu-

<!-- b000411 | references | pages [23] -->
nication at Sea under the Condition of Atmosphere Yawp.[J]. Ship Electronic

<!-- b000412 | references | pages [23] -->
Engineering,2009,29(01):92-95.

<!-- b000413 | references | pages [23] -->
[12] ZHANG Hai-yong. Evaluation of SNR and SIR Based on HF Field-Strength Predic-

<!-- b000414 | references | pages [23] -->
tion[A]. Thirteen Chinese Conference SSTA :2011:5.

<!-- b000415 | references | pages [23] -->
[13] ZHUANG Qian-boSUN Fang-gang. Influence of Different Ground Forms on Short-

<!-- b000416 | references | pages [23] -->
wave Communication[J]. China NewTelecommunications,2014,16(09):92+97.

<!-- b000417 | references | pages [23] -->
[14] HUANG Fang. Research on Characteristics of Maritime Wireless Radio Propaga-

<!-- b000418 | references | pages [23] -->
tion and Channel Modeling[D]. HainanUniversity,2016,49(04):418-422.

<!-- b000419 | furniture | pages [24] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000420 | furniture | pages [24] -->
Team # 86103

<!-- b000421 | furniture | pages [24] -->
Page 21 of 25

<!-- b000422 | heading | pages [24] -->
Appendices

<!-- b000423 | heading | pages [24] -->
Appendix A

<!-- b000424 | prose | pages [24] -->
First appendix

<!-- b000425 | prose | pages [24] -->
Here are simulation programmes we used in our model as follow.

<!-- b000426 | prose | pages [24] -->
%Wave situaion fengji=8; pinpushu=1000; jiaodushu=5;

<!-- b000427 | prose | pages [24] -->
wavewmin = [2.438306 1.462983 1.044989 0.812770 0.664988 0.562683 0.487659 0.430288]; wavewmax = [16.444115 9.866469 7.047480 5.481373 4.484760 3.794799 3.288826 2.90190]; wavewp=[4.053570 2.432142 1.737244 1.351190 1.105519 0.935439 0.810714 0.715336];

<!-- b000428 | prose | pages [24] -->
%----------------------------------------------------- u=[3,5,7,9,11,13,15,17]; %---------------------------------------------------

<!-- b000429 | prose | pages [24] -->
if fengji>8

<!-- b000430 | prose | pages [24] -->
fengji=8; end if fengji<1

<!-- b000431 | prose | pages [24] -->
fengji=1; end fi=fengji; wmin=wavewmin(fi); wmax=wavewmax(fi); wp=wavewp(fi); ui=u(fi); M=pinpushu; N=jiaodushu; wavewn=(wmax-wmin)/M; thetawn=pi/N; dx=1; dy=1; x=[0:dx:500]; y=[0:dy:300]; [x,y]=meshgrid(x,y); z=zeros(size(x)); for wi=1:M

<!-- b000432 | prose | pages [24] -->
for ki=1:N

<!-- b000433 | prose | pages [24] -->
theta=-pi/2+(ki-1)*thetawn;

<!-- b000434 | prose | pages [24] -->
epsin=rand*2*pi; w=wmin+(wi-1)*wavewn+wavewn/2; swi=0.81*exp(-7400/(w*ui+eps).^4)*2*(cos(theta)).^2/(pi*(w.^5+eps)); an=sqrt(2*swi*wavewn*theta); z1=w*w*x*cos(theta)/9.8+w*w*y*sin(theta)/9.8+epsin; z=an*cos(z1)+z; end end surfl(x,y,abs(z)); shading flat; colormap ;

<!-- b000435 | furniture | pages [25] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000436 | furniture | pages [25] -->
Team # 86103

<!-- b000437 | furniture | pages [25] -->
Page 22 of 25

<!-- b000438 | prose | pages [25] -->
lightangle(-45,30); set(findobj(gca,’type’,’surface’),’FaceLighting’,’phong’,’AmbientStrength’,.3,’DiffuseStrength ’Sp

<!-- b000439 | prose | pages [25] -->
ecularStrength’,.9,’SpecularExponent’,200) set(gca,’ztick’,[0,5]);

<!-- b000440 | prose | pages [25] -->
%Figure 5:calculate the relationship between Rh,Rv and incidence angle thetas=(0:1:90); theta=thetas./180.*pi; niu=10; lambda=1./niu; epsilon=80-1i.*60.*lambda.*50; RH1=sin(theta)-sqrt(epsilon-cos(theta).^2); RH2=sin(theta)+sqrt(epsilon-cos(theta).^2); RHh=abs(RH1./RH2); subplot(1,2,1); plot(thetas,RHh,’LineWidth’,1.5);axis([0 90 0.2 1]);hold; xlabel(’incident angle(a˛)’) ylabel(’reflection coefficient’) RH1=epsilon.*sin(theta)-sqrt(epsilon-cos(theta).^2); RH2=epsilon.*sin(theta)+sqrt(epsilon-cos(theta).^2); RHv=abs(RH1./RH2); subplot(1,2,2); plot(thetas,RHv,’LineWidth’,1.5);axis([0 90 0.2 1]);hold; xlabel(’incident angle(a˛)’) ylabel(’reflection coefficient’) niu=20; lambda=1./niu; epsilon=80-1i.*60.*lambda.*50; RH1=sin(theta)-sqrt(epsilon-cos(theta).^2); RH2=sin(theta)+sqrt(epsilon-cos(theta).^2); RHh=abs(RH1./RH2); subplot(1,2,1); plot(thetas,RHh,’r’,’LineWidth’,1.5);axis([0 90 0.2 1]);hold; set(get(gca,’YLabel’),’Fontsize’,12) set(get(gca,’XLabel’),’Fontsize’,12) RH1=epsilon.*sin(theta)-sqrt(epsilon-cos(theta).^2); RH2=epsilon.*sin(theta)+sqrt(epsilon-cos(theta).^2); RHv=abs(RH1./RH2); subplot(1,2,2); plot(thetas,RHv,’r’,’LineWidth’,1.5);axis([0 90 0.2 1]);hold; set(get(gca,’YLabel’),’Fontsize’,12) set(get(gca,’XLabel’),’Fontsize’,12)

<!-- b000441 | prose | pages [25] -->
%Figure 8:Diagrams of correction coefficients clc;clear; niu1=30*10^6;c=3*10^8;niu2=20*10^6;niu3=10*10^6; theta=1/180*pi; omega=[0:20]; h=0.0051.*omega.^2; g1=0.5*(4.*pi.*h.*niu1.*sin(theta)./c); g2=0.5*(4.*pi.*h.*niu2.*sin(theta)./c); g3=0.5*(4.*pi.*h.*niu3.*sin(theta)./c); rou1=1./(sqrt(3.2.*g1-2+sqrt((3.2.*g1).^2-7.*g1+9))); rou2=1./(sqrt(3.2.*g2-2+sqrt((3.2.*g2).^2-7.*g2+9))); rou3=1./(sqrt(3.2.*g3-2+sqrt((3.2.*g3).^2-7.*g3+9))); subplot(1,2,1); plot(omega,rou1,’r’,omega,rou2,’b’,omega,rou3,’g’,’LineWidth’,1.5);axis([0 20 0.97 1]);hold on

<!-- b000442 | furniture | pages [26] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000443 | furniture | pages [26] -->
Team # 86103

<!-- b000444 | furniture | pages [26] -->
Page 23 of 25

<!-- b000445 | prose | pages [26] -->
legend(’10MHz’,’20MHz’,’30MHz’) xlabel(’wind speed(m/s)’) ylabel(’ correction coefficient’) set(get(gca,’YLabel’),’Fontsize’,12) set(get(gca,’XLabel’),’Fontsize’,12) niu=20*10^6; theta1=1/180*pi;c=3*10^8;theta2=5/180*pi;theta3=15/180*2; omega=[0:20]; h=0.0051.*omega.^2; g1=0.5*(4.*pi.*h.*niu.*sin(theta1)./c); g2=0.5*(4.*pi.*h.*niu.*sin(theta2)./c); g3=0.5*(4.*pi.*h.*niu.*sin(theta3)./c); rou1=1./(sqrt(3.2.*g1-2+sqrt((3.2.*g1).^2-7.*g1+9))); rou2=1./(sqrt(3.2.*g2-2+sqrt((3.2.*g2).^2-7.*g2+9))); rou3=1./(sqrt(3.2.*g3-2+sqrt((3.2.*g3).^2-7.*g3+9))); subplot(1,2,2); plot(omega,rou1,’r’,omega,rou2,’b’,omega,rou3,’g’,’LineWidth’,1.5);axis([0 20 0.84 1]); legend(’1a˛’,’5a˛’,’15a˛’) xlabel(’wind speed(m/s)’) ylabel(’ correction coefficient’) set(get(gca,’YLabel’),’Fontsize’,12) set(get(gca,’XLabel’),’Fontsize’,12)

<!-- b000446 | prose | pages [26] -->
%Figure9 Relation curve of reflection coefficient under different wind %speed clc;clear; theta=87/180.*pi; niu=(3:30); lambda=1./niu; epsilon=80-1i.*60.*lambda.*50; RH1=sin(theta)-sqrt(epsilon-cos(theta).^2); RH2=sin(theta)+sqrt(epsilon-cos(theta).^2); RHh=abs(RH1./RH2); RH1=epsilon.*sin(theta)-sqrt(epsilon-cos(theta).^2); RH2=epsilon.*sin(theta)+sqrt(epsilon-cos(theta).^2); RHv=abs(RH1./RH2); RH=(power(RHh,2)+power(RHv,2))/2; theta1=87/180*pi; c=3*10^8; nius=[3:30]; niu=nius.*10^6; h1=0;h2=1.5;h3=3,h4=4.5; g1=0.5*(4.*pi.*h1.*niu.*sin(theta1)./c); g2=0.5*(4.*pi.*h2.*niu.*sin(theta1)./c); g3=0.5*(4.*pi.*h3.*niu.*sin(theta1)./c); g4=0.5*(4.*pi.*h4.*niu.*sin(theta1)./c); rou1=1./(sqrt(3.2.*g1-2+sqrt((3.2.*g1).^2-7.*g1+9))); rou2=1./(sqrt(3.2.*g2-2+sqrt((3.2.*g2).^2-7.*g2+9))); rou3=1./(sqrt(3.2.*g3-2+sqrt((3.2.*g3).^2-7.*g3+9))); rou4=1./(sqrt(3.2.*g4-2+sqrt((3.2.*g4).^2-7.*g4+9))); RH_1=RH.*rou1;RH_2=RH.*rou2;RH_3=RH.*rou3;RH_4=RH.*rou4; plot(nius,RH_1,’r’,nius,RH_2,’b’,nius,RH_3,’g’,nius,RH_4,’y’,’LineWidth’,1.5); xlabel(’frequency(MHz)’) ylabel(’reflection coefficient’) set(get(gca,’YLabel’),’Fontsize’,12) set(get(gca,’XLabel’),’Fontsize’,12) legend(’calm’,’level 2’,’level 4’,’level 6’)

<!-- b000447 | furniture | pages [27] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000448 | furniture | pages [27] -->
Team # 86103

<!-- b000449 | furniture | pages [27] -->
Page 24 of 25

<!-- b000450 | prose | pages [27] -->
%Figure11 Reflection coefficient relationship curves under different ground %conditions clc;clear; theta=87/180.*pi; niu=(3:30); lambda=1./niu; epsilon=80-1i.*60.*lambda.*50; epsilon=8; RH1=sin(theta)-sqrt(epsilon-cos(theta).^2); RH2=sin(theta)+sqrt(epsilon-cos(theta).^2); RHh=abs(RH1./RH2); RH1=epsilon.*sin(theta)-sqrt(epsilon-cos(theta).^2); RH2=epsilon.*sin(theta)+sqrt(epsilon-cos(theta).^2); RHv=abs(RH1./RH2); RH=(power(RHh,2)+power(RHv,2))/2; theta1=87/180*pi; c=3*10^8; nius=[3:30]; niu=nius.*10^6; h1=0;h2=1.5;h3=3,h4=4.5; g1=0.5*(4.*pi.*h1.*niu.*sin(theta1)./c); g2=0.5*(4.*pi.*h2.*niu.*sin(theta1)./c); g3=0.5*(4.*pi.*h3.*niu.*sin(theta1)./c); g4=0.5*(4.*pi.*h4.*niu.*sin(theta1)./c); rou1=1./(sqrt(3.2.*g1-2+sqrt((3.2.*g1).^2-7.*g1+9))); rou2=1./(sqrt(3.2.*g2-2+sqrt((3.2.*g2).^2-7.*g2+9))); rou3=1./(sqrt(3.2.*g3-2+sqrt((3.2.*g3).^2-7.*g3+9))); rou4=1./(sqrt(3.2.*g4-2+sqrt((3.2.*g4).^2-7.*g4+9))); RH_1=RH.*rou1;RH_2=RH.*rou2;RH_3=RH.*rou3;RH_4=RH.*rou4; subplot(1,2,1) plot(nius,RH_1,’r’,nius,RH_2,’b’,nius,RH_3,’g’,nius,RH_4,’y’,’LineWidth’,1.5); xlabel(’frequency(MHz)’) ylabel(’reflection coefficient’) set(get(gca,’YLabel’),’Fontsize’,12) set(get(gca,’XLabel’),’Fontsize’,12) RH_1=-10*log10(RH_1);RH_2=-10*log10(RH_2);RH_3=-10*log10(RH_3);RH_4=-10*log10(RH_4); subplot(1,2,2) plot(nius,RH_1,’r’,nius,RH_2,’b’,nius,RH_3,’g’,nius,RH_4,’y’,’LineWidth’,1.5); xlabel(’frequency(MHz)’) ylabel(’Sea surface reflection loss’);legend(’calm’,’hills’,’low mountains’,’middle mountains’ set(get(gca,’YLabel’),’Fontsize’,12) set(get(gca,’XLabel’),’Fontsize’,12)

<!-- b000451 | prose | pages [27] -->
%figure 13 relationship among distances frequency and SNR clear;clc;format ; P=100;B=3000*10^-6;Yp=15;La=4;Fa=80;f=[3:30]; r=[4000:1000:20000];R=6371;h=300;c=3*10^8;flow=3; n=1;thetas=(3:3:90);theta=thetas.*pi./180; D=2*R*(acos(R/(R+h)*cos(theta))-theta); lambda=1./f; epsilon=80-1i.*60.*lambda.*50; RH1=zeros(length(theta),length(epsilon)); RH2=zeros(length(theta),length(epsilon)); RHh=zeros(length(theta),length(epsilon)); RHv=zeros(length(theta),length(epsilon)); RH=zeros(length(theta),length(epsilon)); for i=1:length(theta)

<!-- b000452 | furniture | pages [28] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000453 | furniture | pages [28] -->
Team # 86103

<!-- b000454 | furniture | pages [28] -->
Page 25 of 25

<!-- b000455 | prose | pages [28] -->
for j=1:length(f)

<!-- b000456 | prose | pages [28] -->
RH1(i,j)=sin(theta(i))-sqrt(epsilon(j)-cos(theta(i))^2); RH2(i,j)=sin(theta(i))+sqrt(epsilon(j)-cos(theta(i))^2); RHh(i,j)=abs(RH1(i,j)/RH2(i,j)); RH1(i,j)=epsilon(j)*sin(theta(i))-sqrt(epsilon(j)-cos(theta(i))^2); RH2(i,j)=epsilon(j)*sin(theta(i))+sqrt(epsilon(j)-cos(theta(i))^2); RHh(i,j)=abs(RH1(i,j)/RH2(i,j)); RH(i,j)=(power(RHh(i,j),2)+power(RHv(i,j),2));%¡ˇn end end rou=zeros(length(theta),length(epsilon)); g=zeros(length(theta),length(epsilon)); niu=f.*10^6; for i=1:length(theta)

<!-- b000457 | prose | pages [28] -->
for j=1:length(f)

<!-- b000458 | prose | pages [28] -->
g(i,j)=0.5*(4.*pi.*flow.*niu(j).*sin(theta(i))./c); rou(i,j)=1./(sqrt(3.2.*g(i,j)-2+sqrt((3.2.*g(i,j)).^2-7.*g(i,j)+9))); end end RH=RH.*rou; Lg=-10*log10(RH); for n=1:6

<!-- b000459 | prose | pages [28] -->
for j=1:30

<!-- b000460 | prose | pages [28] -->
thetax=3*j; L(1,j)=n*D(1,j); for i=1:28

<!-- b000461 | prose | pages [28] -->
fs=i+2; SNR(j,i)=201.56+10*log10(P)-20*log10(fs)-20*log10(L(1,j))-10*log10(B)-n*La-(n-1)* if i==13

<!-- b000462 | prose | pages [28] -->
dis(n)=L(1,1)

<!-- b000463 | prose | pages [28] -->
end

<!-- b000464 | prose | pages [28] -->
end

<!-- b000465 | prose | pages [28] -->
end

<!-- b000466 | prose | pages [28] -->
mesh(f,L,SNR);hold on; max(n)=min(SNR(:,13))

<!-- b000467 | prose | pages [28] -->
end
