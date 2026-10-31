# P-A-2018-86103-6d21eb9d

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000002 | front_matter | pages [1] -->
Team Control Number

<!-- b000003 | front_matter | pages [1] -->
For office use only For office use only

<!-- b000004 | front_matter | pages [1] -->
86103

<!-- b000005 | prose | pages [1] -->
T1 F1 T2 F2 Problem Chosen T3 F3

<!-- b000006 | front_matter | pages [1] -->
A

<!-- b000007 | prose | pages [1] -->
T4 F4

<!-- b000008 | front_matter | pages [1] -->
2018

<!-- b000009 | prose | pages [1] -->
MCM/ICM

<!-- b000010 | heading | pages [1] -->
Summary Sheet

<!-- b000011 | title | pages [1] -->
Simulation Analysis of Multi-hop HF Radio

<!-- b000012 | heading | pages [1] -->
Summary

<!-- b000013 | prose | pages [1] -->
HF radio propagation plays an extremely important role in communication at sea and mountains. It may be influenced by various factors, resulting in great loss of signal transmission. In this paper we focus on transmission and reflection loss of HF radio propagation in reflecting surface changes.

<!-- b000014 | prose | pages [1] -->
First, according to the PM wave spectrum and random wave theory, we establish a three-dimensional random wave model to simulate the motion of waves. On this ba- sis, we analyze the reflection of electromagnetic waves on the sea surface. We consider the influence of wave height caused by different wind levels on the reflection coefficient and obtain the reflection loss of electromagnetic wave under different conditions suc- cessfully. Then we get the sum of the lossin the transmission and the The first reflection intensity of the turbulent ocean and the calm one. At last we analyze the signal electric- field and atmospheric noise electric field of the receiving point, get the relation between SNR, transmission distance and hops, and the maximum number of hops should be 6 when SNR attenuates to 10dB.

<!-- b000015 | prose | pages [1] -->
Second, we analyze the transmission on the ground on the basis of the wave model. We simulate the topography with the wave fluctuation. Because the electromagnetic characteristics of the earth are different from the sea surface, we correct the relative di- electric constant and conductivity. Since there are more obstacles on the ground than on the sea, so we also analyze the diffraction phenomenon of electromagnetic wave prop- agation on the ground. We calculate and compare the first reflection intensity between mountainous or rugged terrain and smooth terrain. Surprisingly, the effectivedistance of sky-wave transmission is shorter than that of sea surface reflection. Under the same conditions, the maximum number of hops of HF radio propagation is4.

<!-- b000016 | prose | pages [1] -->
Finally, we consider the wind and waves that the ship may encounter on the sea sur- face, and calculate the longest distance that the received signal can propagate at a given wind level (i.e., SNR not less than 10 dB). Because ships usually travel longer, we also analyze the periodic variation of the ionosphere with time, and obtain the influence of the periodic variation of the ionosphere on the propagation of sky wave. On the basis of this, we get the optimal radio frequency under different conditions. After taking the ship speed into account, we amend the original model and obtain the maximum time for the ship to maintain the same multi-hop path.

<!-- b000017 | furniture | pages [2] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000018 | title | pages [2] -->
Simulation Analysis of Multi-hop HF Radio

<!-- b000019 | heading | pages [2] -->
Abstract

<!-- b000020 | prose | pages [2] -->
HF radio is widely used in long-distance propagation in a lot of countries because of its advantages of long propagation distance, low transmission loss and no external influence on the quality of propagation, especially maritime propagation. Because it is capable of reflections off the ionosphere and the earth, "jumping" to its destination. Besides, the characteristics of the reflected surface determine the intensity of the reflected waves and the extent to which the signal eventually travels. In this paper, we simulate different environments of the ocean and ground, and obtain the degree of signal loss and the propagation distance finally.

<!-- b000021 | heading | pages [2] -->
Ocean wave model

<!-- b000022 | prose | pages [2] -->
According to the wave spectrum and random wave theory, we take the actual wave as the superposition result of sinusoidal wave with different frequency, different propagation direction, different wave height and different initial phase. Then we establish the Longuet- Higgins long peak wave model. On this basis, we analyze the possible superposition of waves, and get the three-dimensional simulation diagram of the waves, and simulate it.

<!-- b000023 | caption | pages [2] -->
Figure 1 The wave situation

<!-- b000024 | prose | pages [2] -->
when the wind scale is 6 Transmission loss analysis In the process of transmission, SNR of the signal may be reduced due to various factors. For a fixed reception point, the loss of the signal is related to the angle of the signal emission, the transmission distance, the ionospheric absorption intensity, sea situation and so on. We have a simple classification of the loss of the signal: free space transmission loss, ionospheric absorption loss, additional loss and sea surface reflection loss.

<!-- b000025 | prose | pages [2] -->
Then, we lay special stress on the relationship between sea surface reflection loss and various factors. By simulating the reflection path, we study the relationship between reflection path and reflection coefficient, and draw the conclusion that when the hop count is 1, the relationship between the first reflection intensity and the wind scale is as follows:

<!-- b000026 | caption | pages [2] -->
Figure 2 The relationship between the wind scale

<!-- b000027 | prose | pages [2] -->
and the first reflection intensity

<!-- b000028 | prose | pages [2] -->
In long-distance propagation, the number of multi-hop is often greater than 1 so that the wave can travel enough distance. But the integrity of the signal also attenuates gradually with the propagation. By calculation, we know that the maximum number of hops at calm sea is 6 when the power is 100 w and the frequency is 15 MHz.

<!-- b000029 | furniture | pages [3] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000030 | prose | pages [3] -->
Compare with the model on the ground

<!-- b000031 | prose | pages [3] -->
Based on the three-dimensional wave model, we simulate the relief of the terrain with the wave fluctuation. Considering diffraction may occur during the ground propagation, and the variation of the conductivity and relative dielectric constant caused by the complex ground. We modify the existing models, calculate the first reflection intensity and the maximum number of hops on different ground forms. Modification based on navigation

<!-- b000032 | prose | pages [3] -->
In the actual navigation, the receiving point is motional. Thus, it cannot be regarded as a fixed point and to be calculated. So we modify the model to calculate the emission angle, frequency, power and so on as variables. Based on these, we obtain the maximum distance and the time to maintain the same multi-hop path before the SNR attenuates to 10 dB. We also conclude that the absorption loss will increase due to the periodic variation of the ionosphere. So the launch frequency needs to be adjusted at different times.

<!-- b000033 | furniture | pages [4] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000034 | furniture | pages [4] -->
Team # 86103

<!-- b000035 | furniture | pages [4] -->
Page 1 of 25

<!-- b000036 | heading | pages [4] -->
Contents

<!-- b000037 | contents | pages [4] -->
1 Introduction

<!-- b000038 | contents | pages [4] -->
3

<!-- b000039 | contents | pages [4] -->
Background................................................................................................................. 3

<!-- b000040 | contents | pages [4] -->
1.1

<!-- b000041 | contents | pages [4] -->
Restatement of the problem...................................................................................... 3

<!-- b000042 | contents | pages [4] -->
1.2

<!-- b000043 | contents | pages [4] -->
2 Assumptions

<!-- b000044 | contents | pages [4] -->
3

<!-- b000045 | contents | pages [4] -->
3 Notation

<!-- b000046 | contents | pages [4] -->
4

<!-- b000047 | contents | pages [4] -->
4 Radio propagation on sea surface model

<!-- b000048 | contents | pages [4] -->
4

<!-- b000049 | contents | pages [4] -->
Introduction to HF propagation...............................................................................4

<!-- b000050 | contents | pages [4] -->
4.1

<!-- b000051 | contents | pages [4] -->
Way of HF propagation.................................................................................4

<!-- b000052 | contents | pages [4] -->
4.1.1

<!-- b000053 | contents | pages [4] -->
Structure of ionosphere.................................................................................5

<!-- b000054 | contents | pages [4] -->
4.1.2

<!-- b000055 | contents | pages [4] -->
Best usable frequency....................................................................................5

<!-- b000056 | contents | pages [4] -->
4.1.3

<!-- b000057 | contents | pages [4] -->
Wave model.................................................................................................................6

<!-- b000058 | contents | pages [4] -->
4.2

<!-- b000059 | contents | pages [4] -->
Longuet - Higgins wave model................................................................... 6

<!-- b000060 | contents | pages [4] -->
4.2.1

<!-- b000061 | contents | pages [4] -->
Three dimensional wave model...................................................................6

<!-- b000062 | contents | pages [4] -->
4.2.2

<!-- b000063 | contents | pages [4] -->
Model simulation...........................................................................................7

<!-- b000064 | contents | pages [4] -->
4.2.3

<!-- b000065 | contents | pages [4] -->
4.3

<!-- b000066 | contents | pages [4] -->
Transmission loss of HF radio waves Lb................................................................. 7

<!-- b000067 | contents | pages [4] -->
4.3.1

<!-- b000068 | contents | pages [4] -->
Free space transmission loss Lbf...................................................................8

<!-- b000069 | contents | pages [4] -->
4.3.2

<!-- b000070 | contents | pages [4] -->
Ionospheric absorption lossLa......................................................................8

<!-- b000071 | contents | pages [4] -->
4.3.3

<!-- b000072 | contents | pages [4] -->
Sea surface reflection loss Lg.........................................................................9

<!-- b000073 | contents | pages [4] -->
4.3.4

<!-- b000074 | contents | pages [4] -->
Additional loss YP.........................................................................................12

<!-- b000075 | contents | pages [4] -->
First reflection intensity...........................................................................................12

<!-- b000076 | contents | pages [4] -->
4.4

<!-- b000077 | contents | pages [4] -->
Calculation of SNR...................................................................................................13

<!-- b000078 | contents | pages [4] -->
4.5

<!-- b000079 | contents | pages [4] -->
[10]......................................................................................................................................13

<!-- b000080 | contents | pages [4] -->
4.5.1

<!-- b000081 | contents | pages [4] -->
HF sky-wave field intensity

<!-- b000082 | contents | pages [4] -->
Field intensity of atmospheric noise......................................................... 14

<!-- b000083 | contents | pages [4] -->
4.5.2

<!-- b000084 | contents | pages [4] -->
Maximum number of hops.........................................................................14

<!-- b000085 | contents | pages [4] -->
4.5.3

<!-- b000086 | contents | pages [4] -->
5 Comparison between sea surface model and ground surface model

<!-- b000087 | contents | pages [4] -->
15

<!-- b000088 | contents | pages [4] -->
6 Motion analysis of ships using HF radio propagation on turbulent ocean

<!-- b000089 | contents | pages [4] -->
16

<!-- b000090 | furniture | pages [5] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000091 | furniture | pages [5] -->
Team # 86103

<!-- b000092 | furniture | pages [5] -->
Page 2 of 25

<!-- b000093 | contents | pages [5] -->
Maximum time(tmax) using the same multi-hop path......................................... 16

<!-- b000094 | contents | pages [5] -->
6.1

<!-- b000095 | contents | pages [5] -->
Suggestions on frequency selection of transmitter..............................................18

<!-- b000096 | contents | pages [5] -->
6.2

<!-- b000097 | heading | pages [5] -->
7 Strengths and weaknesses

<!-- b000098 | prose | pages [5] -->
18 Strengths.................................................................................................................... 18 7.1 Weaknesses................................................................................................................18 7.2

<!-- b000099 | heading | pages [5] -->
Appendices

<!-- b000100 | prose | pages [5] -->
21

<!-- b000101 | heading | pages [5] -->
Appendix A First appendix

<!-- b000102 | prose | pages [5] -->
21

<!-- b000103 | furniture | pages [6] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000104 | furniture | pages [6] -->
Team # 86103

<!-- b000105 | furniture | pages [6] -->
Page 3 of 25

<!-- b000106 | heading | pages [6] -->
1 Introduction

<!-- b000107 | heading | pages [6] -->
1.1 Background

<!-- b000108 | prose | pages [6] -->
It is universally acknowledged that a ship sailing in the boundless sea will encounter a variety of danger at any time. With the increasing number of ships in the world and the trend toward large-scale and high-speed ocean shipping, the world’s waterways are becoming more and more crowded and crisis may occur at any time. In this case, HF radio propagation has played a significant role. HF radio propagation can attract us to transmitting messages, thats mainly because that HF communication can be achieved only by appropriate transmitting power and moderate equipment cost even far apart.

<!-- b000109 | heading | pages [6] -->
1.2 Restatement of the problem

<!-- b000110 | prose | pages [6] -->
As required by the question, we are supposed to determine the strength of the first re- flection off a turbulent ocean and compare it with the strength off a calm ocean. Mean- while, we will also determine the maximum number of hops the signal can take before its strength falls below a usable SNR. After that, we will compare the findings with hf reflections off different topography. Moreover, we are going to change our model to accommodate a shipboard receiver moving on a turbulent ocean.

<!-- b000111 | prose | pages [6] -->
There are two forms of shortwave propagation. One is ground wave, which consists of surface wave, direct wave and reflected wave; and another is sky wave that reaches the ground reception point being reflected by the ionospheric. In this article, we only model the reflection of sky waves.

<!-- b000112 | heading | pages [6] -->
2 Assumptions

<!-- b000113 | prose | pages [6] -->
• We consider the transmission of sky waves as the main way.

<!-- b000114 | prose | pages [6] -->
Reason: Energy is lost with the propagation of ground wave, and the higher the frequency(that is, the shorter the wave length), the greater the loss. However, sky-wave communication has the advantages of long propagation distance, low transmission loss and not being affected by the geological types of both sides. So we consider the transmission of sky waves as the main way.

<!-- b000115 | prose | pages [6] -->
• The reflection of sky-waves in the ionosphere is mainly considered in the F2 layer.

<!-- b000116 | prose | pages [6] -->
Reason: (1) It’s exist all day. (2) It’s height can accommodate the longest path. (3) MUF(maximum usable frequency) is the biggest.

<!-- b000117 | prose | pages [6] -->
• The main factor affecting wave height is wind speed.

<!-- b000118 | prose | pages [6] -->
• We regard the relative permittivity and conductivity of seawater as fixed values.

<!-- b000119 | prose | pages [6, 7] -->
Reason: The changes of relative dielectric constant and conductivity are mainly caused by the change of salt content and temperature, and the wave and sea wa- ter motion have little effect on them, so we think that they are almost unchanged, and regard them as fixed values.

<!-- b000120 | furniture | pages [7] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000121 | furniture | pages [7] -->
Team # 86103

<!-- b000122 | furniture | pages [7] -->
Page 4 of 25

<!-- b000124 | prose | pages [7] -->
• We consider ships movement on the sea as a uniform motion.

<!-- b000125 | heading | pages [7] -->
3 Notation

<!-- b000126 | heading | pages [7] -->
Notation

<!-- b000127 | prose | pages [7] -->
Definition Lb Transmission loss Lbf Free space transmission loss La Ionospheric absorption loss Lg Ground reflection loss ε Electric medium constant σ Conductivity YP Additional loss r Propagation distance D Maximum propagation distance Elevation angle of transmission ∆ n Number of hops f Working frequency P0 Power of the transmitter P1 First reflection intensity R Reflection coefficient θ Incidence angle of electromagnetic wave

<!-- b000128 | prose | pages [7] -->
P.s. Other symbols instruction will be given in the text.

<!-- b000129 | heading | pages [7] -->
4 Radio propagation on sea surface model

<!-- b000130 | heading | pages [7] -->
4.1 Introduction to HF propagation

<!-- b000131 | heading | pages [7] -->
4.1.1 Way of HF propagation

<!-- b000132 | prose | pages [7] -->
HF propagation is the radio propagation of radio waves in the range of 3 to 30MHz(corre- sponding wave length 100 to 10m). HF communication has the advantages of long communication distance, strong persistence and simple equipment,meanwhile, it has the disadvantages of channel congestion, time-varying, dispersion characteristics, and so on. Moreover, it is easy to be influenced by other external factors and is unstable. HF propagation can propagate along the ground as the ground-wave, and it can also prop- agate through reflections off the ionospheric as the sky-wave. The propagation diagram is as follows:

<!-- b000133 | furniture | pages [8] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000134 | furniture | pages [8] -->
Team # 86103

<!-- b000135 | furniture | pages [8] -->
Page 5 of 25

<!-- b000136 | caption | pages [8] -->
Figure 1 HF propagation diagram

<!-- b000137 | heading | pages [8] -->
4.1.2 Structure of ionosphere

<!-- b000138 | prose | pages [8] -->
Ionosphere is a ionization region of the earths atmosphere. It is ionized by highenergy radiation from the sun and cosmic rays. For the existence of a huge number of free electrons and ions, radio waves can change the speed of propagation ,and refraction, reflection and scattering occurred. The ionosphere can be divided into layer D, E, F [1]. The height of each layer and so on, and the layer F can be divided into F1 and F 2 changes over time, and some layers even disappear at night.

<!-- b000139 | caption | pages [8] -->
Figure 2 Inner layers of ionosphere

<!-- b000140 | heading | pages [8] -->
4.1.3 Best usable frequency

<!-- b000141 | prose | pages [8] -->
According to the theory of ionospheric propagation, shortwave with a higher frequency can only return to the ground from the reflection off ionosphere with a higher electron density distribution. There is a maximum frequency of radio waves that can be reflected back to the ground, which we call MUF(maximum usable frequency). the frequency of propagation should be as high as possible to reduce absorption, but generally only at the frequency of 0.85 MUF. Because if we use MUF, as long as the ionosphere changes slightly, the radio waves would go through the ionosphere without going back. So we [2]the best usablefrequency. call the frequency of 0.85 MUF

<!-- b000142 | furniture | pages [9] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000143 | furniture | pages [9] -->
Team # 86103

<!-- b000144 | furniture | pages [9] -->
Page 6 of 25

<!-- b000145 | heading | pages [9] -->
4.2 Wave model

<!-- b000146 | heading | pages [9] -->
4.2.1 Longuet - Higgins wave model

<!-- b000147 | prose | pages [9] -->
The wave phenomenon is very complex, and its speculative and nonlinear. Therefore, it is very difficult to establish an accurate wave model. According to the wave spectrum and random wave theory, we can regard the actual wave as the result of sinusoidal wave superposition with different frequency, different propagation directions, different wave [3] describes the waves heights and different initial phases. The Longuet-Higgins model of long-peak waves by the superposition of countless random cosine waves, and the amplitude is expressed as follows:

<!-- b000148 | prose | pages [9] -->
Where ξai refers to the amplitude of the i cosine wave, ωi refers to the frequency of the i cosine wave, and εi refers to the phase of the i cosine wave.

<!-- b000149 | prose | pages [9] -->
In practical applications, the Longuet-Higgins model is often expressed by the wave spectrum:

<!-- b000150 | prose | pages [9] -->
In the formula, Sζ ∆ωis the wave spectrum. At present, there are several widely used ocean spectrum,such as Pierson-Moscowitz spectrum(PM spectrum), Neumann spectrum(N spectrum), ITTC spectrum and so on, among which PM spectrum is the most widely used. It can well represent the fully developed random waves. Therefore, we use the PM spectrum. And the expression of PM spectrum is as follows:

<!-- b000151 | prose | pages [9] -->
Where v is the wind speed with a height of 19.5m above the sea level.

<!-- b000152 | heading | pages [9] -->
4.2.2 Three dimensional wave model

<!-- b000153 | prose | pages [9] -->
In the above model, we consider only one direction. But in the actual wave, the wave not only changes in height and frequency, but also spread in more than one direction. So we define the waves which are superimposed on each other and diffused randomly to ±π/2inthemainwaveasthreedimensionalirregularshortpeakrandomwavemodel.

<!-- b000154 | prose | pages [9] -->
We overlay the above model in many directions, and finally we get the following expression:

<!-- b000155 | prose | pages [9] -->
Where ζaij , ωi , ki , µj and εij are the amplitude, the angular frequency, the wave number, the direction angle and the random initial phase of the component harmonics, εij is random number between 0 and π/2, (ξ, η)is the coordinates of a certain point on a wave surface.

<!-- b000156 | furniture | pages [10] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000157 | furniture | pages [10] -->
Team # 86103

<!-- b000158 | furniture | pages [10] -->
Page 7 of 25

<!-- b000159 | heading | pages [10] -->
4.2.3 Model simulation

<!-- b000160 | prose | pages [10] -->
We simulated the model in MATLAB, and the results are as follows:

<!-- b000161 | caption | pages [10] -->
Figure 3 Wave situation of 5∼8 winds

<!-- b000162 | prose | pages [10] -->
Transmission loss of HF radio waves Lb 4.3

<!-- b000163 | prose | pages [10] -->
During the transmission of radio waves, there are many factors that can affect the trans- mission loss. We divide the basic transmission loss(Lb) during the whole propagation process into four parts: free space transmission loss Lbf , ionospheric absorption loss La , ground reflection loss Lg, and additional loss YP . If all losses are expressed in deci- bel(dB), the basic transmission loss of sky-wave propagation is as follows:

<!-- b000164 | prose | pages [10] -->
(5) Lb = Lbf + Li + Lg + YP

<!-- b000165 | caption | pages [10] -->
Figure 4 Parts of transmission loss

<!-- b000166 | furniture | pages [11] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000167 | furniture | pages [11] -->
Team # 86103

<!-- b000168 | furniture | pages [11] -->
Page 8 of 25

<!-- b000169 | heading | pages [11] -->
4.3.1 Free space transmission loss Lbf

<!-- b000170 | prose | pages [11] -->
The free space transmission loss is the loss of energy caused by geometric factors after [4]: radio wave detaching antenna. The equality of Lbf is as follows

<!-- b000171 | prose | pages [11] -->
(6) Lbf = 32.44 + 20lgf + 20lgr

<!-- b000172 | prose | pages [11] -->
Where f is the working frequency in MHz and r is the effective path of HF radio propagation in km.

<!-- b000173 | prose | pages [11] -->
The curvature of the earth and the height of the ionosphere limit the one-time maxi- [5]: mum jump distance of the reflection off the ionosphericDmax

<!-- b000174 | prose | pages [11] -->
In the equation, ∆min is the minimum elevation angle of the antenna, and we know that the general elevation angle of the antenna is greater than 3◦. The Re is the radius of the earth, and we value it as 6371km. The h is the reflection virtual height of the ionosphere. The height of each layer is shown in the diagram. For F2 reflection, the maximum propagation distance Dmax is 4000km.

<!-- b000175 | heading | pages [11] -->
4.3.2 Ionospheric absorption lossLa

<!-- b000176 | prose | pages [11] -->
In HF radio propagation, the loss caused by ionospheric absorption mainly occurs in layer D, because there are more neutral molecules in layer D and the collision loss is [6]. The concentration of electrons in layer D decreases at night, and the absorption larger loss decreases. The loss is mainly non-offset absorption. The emission absorption in [7] . We ignore it in calculation for its layer 4 E or F mainly refers to offset absorption very small (≤1 dB).

<!-- b000177 | prose | pages [11] -->
Whereϕistheincidentangleataheightof100km,f(MHz)istheworkingfrequency and fH(MHz) is the gyromagnetic frequency,I is the absorption index and n is number of hops in the path.

<!-- b000178 | prose | pages [11] -->
The absorption index I is:

<!-- b000179 | prose | pages [11] -->
(9) I = (1 +0.037R)(cos 0.881χ)1.3

<!-- b000180 | prose | pages [11] -->
Where R is the number of sunspots and χ is the zenith angle of two 100 km high absorbs.

<!-- b000181 | prose | pages [11] -->
For the ionospheric absorption loss is related to transmitter, issue time and teh pa- rameters of receiving spots, and that the calculation is too complex, we take it as 4dB to make the calculation easy.

<!-- b000182 | furniture | pages [12] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000183 | furniture | pages [12] -->
Team # 86103

<!-- b000184 | furniture | pages [12] -->
Page 9 of 25

<!-- b000185 | heading | pages [12] -->
4.3.3 Sea surface reflection loss Lg

<!-- b000186 | prose | pages [12] -->
(1) Calm sea reflection For multi-hop sea surface reﬂection loss suppose incident wave is messy polariza-tionThe energy of the radio waves is evenly distributed on the horizontal and vertical polarizations, so that the formula for calculating the energy is

<!-- b000187 | prose | pages [12] -->
(10)

<!-- b000188 | prose | pages [12] -->
WhereRHandRVarethereﬂectioncoefﬁcientsofhorizontalandverticalpolarizedwaves, respectively, as follows:

<!-- b000189 | prose | pages [12] -->
Where θ is the incident angle, is the complex permittivity of the sea surface, ε is the permittivity of seawater, λ is the wavelength of the incident wave and σ is the con-ductivity. Accordingtothisformula,therelationshipbetweenRH，Rvandtheangleofincidence.

<!-- b000190 | caption | pages [12] -->
Figure 5 The relationship between RH , RV and incidence angle

<!-- b000191 | prose | pages [12, 13] -->
Accordingtothe ﬁgure,it isnotdifﬁcultto ﬁnd thatforthehorizontal polarized wave,the reﬂection coefﬁcientdecreases graduallyfrom 1, while the amplitude is verysmall.For the vertical polarized wave, with the reﬂection coefﬁcient increases with the increase of the incident angle,thereﬂectioncoefﬁcientincreasesto1gradually afterde-creasingrapidlyatﬁrst.The comparison shows that the change of reﬂection coefﬁcient of the horizontal polarization wave is much more sensitive to the incident angle.

<!-- b000192 | furniture | pages [13] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000193 | furniture | pages [13] -->
Team # 86103

<!-- b000194 | furniture | pages [13] -->
Page 10 of 25

<!-- b000196 | heading | pages [13] -->
(2) Ocean Wave Model algorithm for turbulentocean

<!-- b000197 | prose | pages [13] -->
Forthe three dimensionalirregular short-peak randomwave model mentioned above, we randomly select a wave cross section to analyze. When the electromagnetic wave shines on the wave, most of the available electromagnetic waves are emitted in the form of reflection and scattering, and reflection is the main one.

<!-- b000198 | caption | pages [13] -->
Figure 6 Diagram of electromagnetic wave reflection on turbulent ocean

<!-- b000199 | prose | pages [13] -->
For the wave function ξ(x) of this cross section at a certain time, we take the deriva- tive of it and obtain the tangent equation of the section irradiated by electromagnetic wave.

<!-- b000200 | prose | pages [13] -->
(14) y = ξ′(x)(x −x0) + y0 Where (x0, y0) is the coordinate of surface element α. According to Sneel’s law, we assume that the grazing angle of electromagnetic wave incident to plane α is θ, and then we obtain the propagation path equation of reflected wave as shown below:

<!-- b000201 | prose | pages [13] -->
(15) y = tan(∆+ arctan ξ′(x))(x −x0) + y0

<!-- b000202 | prose | pages [13] -->
Because the water surface has a certain dip angle, the full incident wave cant be reflected in the positive direction. Therefore, we differentiate the wave surface, analyze each micro-element plane, and find out the total number of reflected waves reflected in the forward direction, and get the correction coefficient finally:

<!-- b000203 | prose | pages [13] -->
m (16) ρ = M

<!-- b000204 | prose | pages [13] -->
Where m is the total number of positive and negative reflection electromagnetic waves and M is the total number of incident electromagnetic waves.

<!-- b000205 | furniture | pages [14] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000206 | furniture | pages [14] -->
Team # 86103

<!-- b000207 | furniture | pages [14] -->
Page 11 of 25

<!-- b000208 | caption | pages [14] -->
Figure 7 Diagram of wave shadow

<!-- b000209 | prose | pages [14] -->
As shown in the figure, the actual waves will have ups and downs. Especially when the wind and waves are high, some of the sea surface will be covered by the waves. At this point, we have corrected the occluded part, ignoring the reflected light in that part. The correction method is as follows:

<!-- b000210 | prose | pages [14] -->
We obtain the second derivative for wave function ξ(x) and obtain the tangent equa- tion of extreme value point corresponding to its extreme point. Then the second inter- section point of electromagnetic wave and wave is the intersection point of the equation and wave function, and the shading is the shaded area.

<!-- b000211 | prose | pages [14] -->
S −s ρ′ = ρ (17) ∗ S Where S is the surface area of a wave and s is the shaded area.

<!-- b000212 | caption | pages [14] -->
Figure 8 Diagrams of correction coefficients

<!-- b000213 | furniture | pages [15] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000214 | furniture | pages [15] -->
Team # 86103

<!-- b000215 | furniture | pages [15] -->
Page 12 of 25

<!-- b000216 | prose | pages [15] -->
In the figure above, the left image shows the correction coefficients at different wind speeds when the grazing angle is 1◦/5◦/15◦, and the right image shows the correction coefficients at different wind speeds when the frequency is 10 MHz / 20 MHz / 30 MHz.

<!-- b000217 | prose | pages [15] -->
Wecan get the following curve, which is the final reflection coefficient bymultiply- ing it with the reflection coefficient when it is stationary:

<!-- b000218 | caption | pages [15] -->
Figure 9 Relation curve of reflection coefficient under different wind speed

<!-- b000219 | prose | pages [15] -->
Then we can get the loss of turbulent ocean:

<!-- b000220 | prose | pages [15] -->
(18) L′g = Lg −10 lg(ρ′)

<!-- b000221 | heading | pages [15] -->
4.3.4 Additional loss YP

<!-- b000222 | prose | pages [15] -->
Additional loss is the loss caused by other factors in addition to the main reasonsmen- tioned above. The detailed calculation is too complicated, but we conclude that it is [9]. mainly related to local time, which is assumed to be about 15 dB here

<!-- b000223 | heading | pages [15] -->
4.4 First reflection intensity

<!-- b000224 | prose | pages [15] -->
Combined with the loss analysis above, for a single jump signal source, we can get the following formula:

<!-- b000225 | prose | pages [15] -->
(19) 10lg(P1) = 10lg(P0) −Lbf −La −Lg −YP

<!-- b000226 | prose | pages [15, 16] -->
Among them, P1(w) is the electromagnetic wave power of the transmitting point and P0(w) is the first reflection intensity. For the electromagnetic wave propagation route which has been determined in both time and space, only Lg is alterable because of the different sea conditions, we get the following chart bycalculation:

<!-- b000227 | furniture | pages [16] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000228 | furniture | pages [16] -->
Team # 86103

<!-- b000229 | furniture | pages [16] -->
Page 13 of 25

<!-- b000231 | caption | pages [16] -->
Figure 10 The strength of the first reflection P1

<!-- b000232 | caption | pages [16] -->
Table 1 Related Parameters

<!-- b000233 | prose | pages [16] -->
Parameter Reference value Unit dB 4 La 15 dB YP MHz 100 f w 100 P0 ◦ θ 3

<!-- b000234 | prose | pages [16] -->
As is shown in the figure, its the first reflection intensity of a signal with different frequencies under different wind speeds. We can get the curve of reflection intensity changing with sea condition by fitting. From the diagram, we can know that the first reflection intensity decreases with the increase of frequency and the increase of wind speed. Thus, we must consider the influence of weather in the process of maritime communication.

<!-- b000235 | heading | pages [16] -->
4.5 Calculation of SNR

<!-- b000236 | prose | pages [16] -->
[10]

<!-- b000237 | heading | pages [16] -->
4.5.1 HF sky-wave field intensity

<!-- b000238 | prose | pages [16] -->
The field strength of the receiving point can be calculated by the following formula:

<!-- b000239 | prose | pages [16] -->
(20) Et= 137.2 + 20 lg f + 10 lg P 0+ Gt−Lb

<!-- b000240 | prose | pages [16] -->
In the formula, Et(dB) is the signal intensity of the receiving point during the prop- agation of sky wave, f(MHz) is the working frequency, P(kw) is the power of the trans- mitter, tt(dB) is the normal gain of the transmitter antenna radiation, and Lb(dB) is the transmission loss of sky-wave.

<!-- b000241 | furniture | pages [17] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000242 | furniture | pages [17] -->
Team # 86103

<!-- b000243 | furniture | pages [17] -->
Page 14 of 25

<!-- b000244 | heading | pages [17] -->
4.5.2 Field intensity of atmospheric noise

<!-- b000245 | prose | pages [17] -->
[11] . It is the main noise source of ma- Atmospheric noise is mainly caused by lightning rine HF radio propagation at present. The formula for calculating the effective value of atmospheric noise field intensity is as follows:

<!-- b000246 | prose | pages [17] -->
(21) En = Fa + 10 lg B + 20 lg f−96.8

<!-- b000247 | prose | pages [17] -->
In the formula, En(dB) is the field intensity of atmospheric noise, Fa(dB) is the ef- fective noise coefficient of atmospheric radio, B(dB) is the effective noise bandwidth of receiver, F(MHz) is working frequency.

<!-- b000248 | prose | pages [17] -->
Atmospheric noise is usually estimated by the noise data provided in the CCIR322nd report. A complete set of atmospheric noise data contains 72 charts. The calculation pro- cess is very complicated and the accuracy is not high enough. Thus we use themethod of establishing a database to make a simple estimate. The following figure shows the [12]. atmospheric noise table at different times in a certain area in summer

<!-- b000249 | caption | pages [17] -->
Table 2 Atmospheric noise at different times in a certain area in summer

<!-- b000250 | heading | pages [17] -->
4.5.3 Maximum number of hops

<!-- b000251 | prose | pages [17] -->
According to the formula for calculating the electric field intensity of HF sky-wave and the formula for calculating the effective value of atmospheric noise field intensity, we obtain the formula for calculating signal-to-noise ratio of shortwave sky-wave commu- nication under natural conditions.

<!-- b000252 | prose | pages [17] -->
(22) SNR = 201.56 + 10lgP0 −20lgf −20lgr −10lgB −La −Lg −YP −Fa

<!-- b000253 | prose | pages [17] -->
In the formula, after n jumps, we found that

<!-- b000254 | prose | pages [17] -->
(23) r = nDmax

<!-- b000255 | prose | pages [17] -->
(24) L′g = (n −1)× Lg (25) L′a = n × La With reference to the following table for each parameter, we can get n = 6 by using the fsolve function of MATLAB.

<!-- b000256 | furniture | pages [18] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000257 | furniture | pages [18] -->
Team # 86103

<!-- b000258 | furniture | pages [18] -->
Page 15 of 25

<!-- b000259 | heading | pages [18] -->
5 Comparison between sea surface model and ground surface

<!-- b000260 | prose | pages [18] -->
model

<!-- b000261 | prose | pages [18] -->
Because the ground environment is more complicated than the sea surface and is com- posed of various materials, we take the relative permittivity of 3 to 8 as the basic value and the geodetic equivalent conductivity as the electrical conductivity in the calculation.

<!-- b000262 | prose | pages [18] -->
By using the proposed model and the algorithm proposed above, we take the undu- lation of the mountain as the motion of the wave and calculate it approximately. Because there are many obstacles on the ground, the electromagnetic wave will be diffracted when it meets the obstacle. However, because the short wave wavelength is not enough to avoid obstacles, most of them will be blocked by various obstacles, so the propagation ability of short wave on the ground is very weak. According to the analysis,we substi- tute the electromagnetic parameters of ground into the formula and get the solutionas [13]: follows

<!-- b000263 | caption | pages [18] -->
Figure 11 Reflection coefficient relationship curves under different ground conditions

<!-- b000264 | prose | pages [18] -->
The related parameters are shown in the table.

<!-- b000265 | caption | pages [18] -->
Table 3 ε,σ in different environments

<!-- b000266 | prose | pages [18] -->
Variation Average Ground form ε(F/m) σ(S/m) ε(F/m) σ(S/m) Seawater 80 1∼4.3 80 4 10−3 Freshwater 80 10−3 ∼2.4×10−2 80 10−2 Wet soil 10∼30 3×10−3 ∼2.4 × 10−2 10 10−3 Dry soil 3∼4 1.1×10−5 ∼2 × 10−2 4

<!-- b000267 | prose | pages [18] -->
The first reflection intensity in hilly areas is as shown in the diagram, especially when the terrain is smooth, the relief degree is 0.

<!-- b000268 | furniture | pages [19] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000269 | furniture | pages [19] -->
Team # 86103

<!-- b000270 | furniture | pages [19] -->
Page 16 of 25

<!-- b000271 | caption | pages [19] -->
Figure 12 Strength of the first reflection

<!-- b000272 | prose | pages [19] -->
Wetake Lg as 6.53dB when the ground is flat and we get that n = 4. Compared with the sea surface, the propagation distance of the HF radio through the ground is much shorter than that of the sea surface.

<!-- b000273 | heading | pages [19] -->
6 Motion analysis of ships using HF radio propagation on tur-

<!-- b000274 | prose | pages [19] -->
bulent ocean

<!-- b000275 | prose | pages [19] -->
Maximum time(tmax) using the same multi-hop path 6.1

<!-- b000276 | prose | pages [19] -->
In the above model, we only consider the condition that the reception point is fixed. This model is applicable to the communication between two fixed points , or the case where the position change of the receiving point is negligible. The ship in the turbulent ocean has a long moving distance, so we can not only calculate the effective propaga- [14]. At this point, the propagation distance r is related tion distance r as a fixed value to the emission angle ∆, and La, Lg is related to n(the number of hops of sky-wave), meanwhile, Lg is also related to the emission angle ∆. To ensure that the received signal is clear enough, we conclude that the SNR should be greater than or equal to 10, that is:

<!-- b000277 | prose | pages [19] -->
SNR = 201.56+10 lg P 0 −20 lg f −20 lg r−10 lg B −nLa−(n−1)Lg −Yp−Fa ≥10 (24)

<!-- b000278 | prose | pages [19] -->
Through analysis, we know that since Lg is related to ∆, the longer the route distance is, the higher the power transmitter and the increase antenna are needed to assist the ship in the sea course. Or the radio frequency can be adjusted to avoid overattenuating to make the SNR too low and difficult to distinguish.

<!-- b000279 | furniture | pages [20] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000280 | furniture | pages [20] -->
Team # 86103

<!-- b000281 | furniture | pages [20] -->
Page 17 of 25

<!-- b000282 | caption | pages [20] -->
Figure 13 Relationships among distance, frequency and SNR

<!-- b000283 | prose | pages [20] -->
As shown in the figure, SNR of 100w signal is obtained at the receiving pointswith different frequencies and distances, with the number of hops n = 1 ∼6, the wind scale is 5, and the receiving points at different frequencies and distances.

<!-- b000284 | caption | pages [20] -->
Table 4 Maximum propagation distance r when f=15Hz, P =100w

<!-- b000285 | prose | pages [20] -->
Number of hops n Maximum propagation distance r(km) SNR(dB) 1 3225 54.0977 2 6449 23.2859 3 9674 16.9728 4 10125 10 5 <10125 10 6 <10125 10

<!-- b000286 | prose | pages [20] -->
We can know from the figure that when n is fixed, the propagation distance is insuf- ficient or the signal-to-noise ratio is too low with increasingdistance.

<!-- b000287 | prose | pages [20] -->
By analyzing the data above, we draw a conclusion that when the number of hops is too high, for the ship traveling on the turbulent sea surface, the signal reflects too many times between the sea surface and the ionosphere, and the loss of the propagation path is too large, which results in the decrease of the maximum propagation distance. It is not enough to spread the signal far enough. Therefore, in this case, we need to increase the transmission power or signal frequency to increase the signal-to-noise ratio and the maximum propagation distance.

<!-- b000288 | prose | pages [20] -->
In summary, the maximum time for ships to maintain multi-hop paths in turbulent ocean is :

<!-- b000289 | prose | pages [20, 21] -->
r tmax = (27) v Where v is the speed of the ship moving at sea. In the case of the table above, the multi-hop path must be changed for every 3000km movement. In the case of 100W and 15MHz, the signal power and frequency must be increased when the transmission distance is over 10000 km.

<!-- b000290 | furniture | pages [21] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000291 | furniture | pages [21] -->
Team # 86103

<!-- b000292 | furniture | pages [21] -->
Page 18 of 25

<!-- b000294 | heading | pages [21] -->
6.2 Suggestions on frequency selection oftransmitter

<!-- b000295 | prose | pages [21] -->
Because not only the periodic variation of the ionosphere,but also the influence of the day and night, the season, the solar activity and so on can affect the value of the iono- spheric propagation loss La. In order for ships to have better communication at sea, the emitter must choose different frequency at different time to achieve better propagation. The following table shows the range of radio broadcasts commonly used to take into account ionospheric effects:

<!-- b000296 | caption | pages [21] -->
Table 5 Recommended emission frequency

<!-- b000297 | prose | pages [21] -->
2∼4 MHz Tropical frequency, small number of sunspots and transmission is good.

<!-- b000298 | prose | pages [21] -->
Some countries near the equator can use it as domestic broadcasting 6∼7 MHz More suitable using in autumn and winter or night for close-range broa- dcasting 9∼11 MHz Moderate and suitable for all-day broadcasting both inside and outside 13 MHz Effect would be better at daytime and is suitable for long distance broa- dcasting 15∼17MHz Better in spring and summer

<!-- b000299 | heading | pages [21] -->
7 Strengths and weaknesses

<!-- b000300 | heading | pages [21] -->
7.1 Strengths

<!-- b000301 | prose | pages [21] -->
• Weclassify and analyze the propagation path, which makes our calculation more accurate.

<!-- b000302 | prose | pages [21] -->
• Wehave established a three-dimensional wave model, which is more intuitive.

<!-- b000303 | prose | pages [21] -->
• Weadopt the correction method of reflection coefficient, which is different from the previous empirical formula, and can analyze the reflection coefficient under different sea conditions quantitatively.

<!-- b000304 | prose | pages [21] -->
• Wetake the effects of periodic ionospheric variations into account, which are sensitive and can be used in various situations.

<!-- b000305 | heading | pages [21] -->
7.2 Weaknesses

<!-- b000306 | prose | pages [21] -->
• Weonly consider the HF sky-wave transmission model, but the ground-wave transmission also has certain influence.

<!-- b000307 | prose | pages [21, 22] -->
• In real life, the ionospheric loss is complicated and varies greatly with latitude, longitude, seasons and so on. However, we only calculate the reasonable values according to the literature.

<!-- b000308 | furniture | pages [22] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000309 | furniture | pages [22] -->
Team # 86103

<!-- b000310 | furniture | pages [22] -->
Page 19 of 25

<!-- b000312 | prose | pages [22] -->
• We only focus on the characteristics of shortwave propagation at sea level and the effect of reflection without considering the effect of refractiondiffraction.

<!-- b000313 | prose | pages [22] -->
• The dielectric constant and conductivity of the reflected surface change with the frequency, but we only use the fixed value to calculate. When the salinity and temperature of seawater change sharply, the reliability of the data will decrease.

<!-- b000314 | furniture | pages [23] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000315 | furniture | pages [23] -->
Team # 86103

<!-- b000316 | furniture | pages [23] -->
Page 20 of 25

<!-- b000317 | heading | pages [23] -->
References

<!-- b000318 | references | pages [23] -->
[1] LI Wei. Influence of Ionospheric Characteristics on Shortwave Transmission[J]. In-

<!-- b000319 | references | pages [23] -->
ner Mongolia Radio & TV Broadcast Engineering,2016,33(06):68-71. Mathematical

<!-- b000320 | references | pages [23] -->
Society and Addison-Wesley Publishing Company , 1984-1986.

<!-- b000321 | references | pages [23] -->
[2] SHI Xiang-tong, WANG Lei, HU Bo. Frequency Selection of Shortwave Communi-

<!-- b000322 | references | pages [23] -->
cation Radio[J]. Ship Electronic Engineering, 2013, 33(10):39-41.

<!-- b000323 | references | pages [23] -->
[3] QI Ning, XIA Tian, LI Wen-yan, ZHAO Li-guang. Simulation of the Mathematical

<!-- b000324 | references | pages [23] -->
Model of 3-D Irregular Wave Based on MATLAB[J]. Computer Knowledge and

<!-- b000325 | references | pages [23] -->
Technology,2013,9(25):5737-5739.

<!-- b000326 | references | pages [23] -->
[4] PENG Feng-hua, ZHOU Xue-jun. Propagation of Maritime Short-wave Telecom-

<!-- b000327 | references | pages [23] -->
munication Link[J]. Ship Electronic Engineering,2011,31(12):125-127.

<!-- b000328 | references | pages [23] -->
[5] ZHAO Yu-cai. Research and Realization on Radio Propagation Prediction and

<!-- b000329 | references | pages [23] -->
Interference Analyzing Technology[D]. National University of Defense Technol-

<!-- b000330 | references | pages [23] -->
ogy,2009.

<!-- b000331 | references | pages [23] -->
[6] YUAN Xiao-bo. Shortwave Sky Wave Propagation Loss Prediction and Prediction

<!-- b000332 | references | pages [23] -->
of Field Strength[J]. Information & Communications,2013(05):11-12.

<!-- b000333 | references | pages [23] -->
[7] LI Xue-hongLI FazhongHAN LongCHEN Lijun. Method and Models of Field

<!-- b000334 | references | pages [23] -->
Strength Calculation in HF Sky Wave Communication[J]. Communications

<!-- b000335 | references | pages [23] -->
Technology,2016,49(04):418-422.

<!-- b000336 | references | pages [23] -->
[8] WANG Ying, GU Jian. Research and simulation analysis of radio reflection char-

<!-- b000337 | references | pages [23] -->
acteristic over the ocean[J]. International Electronic Elements, 2016, 24(05):113-

<!-- b000338 | references | pages [23] -->
115+119.

<!-- b000339 | references | pages [23] -->
[9] LUO Jia, ZHANG Wen-ming, WANG Xue-song. Modeling and Simulation of

<!-- b000340 | references | pages [23] -->
HF Skywave Transmission Loss in Communication Countermeasure[J]. Computer

<!-- b000341 | references | pages [23] -->
Simulation,2007(08):28-31+35.

<!-- b000342 | references | pages [23] -->
[10] DONG HangXU ChiYI TaoHAN Dong. HF Communication Aid DecisionMaking

<!-- b000343 | references | pages [23] -->
Model basedon SNR Evaluation[J]. CommunicationsTechnology,2014,47(11):1313-

<!-- b000344 | references | pages [23] -->
1317.

<!-- b000345 | references | pages [23] -->
[11] Qu Gui-cheng, Wang Rui. Research on the Feasibility of Shortwave Commu-

<!-- b000346 | references | pages [23] -->
nication at Sea under the Condition of Atmosphere Yawp.[J]. Ship Electronic

<!-- b000347 | references | pages [23] -->
Engineering,2009,29(01):92-95.

<!-- b000348 | references | pages [23] -->
[12] ZHANG Hai-yong. Evaluation of SNR and SIR Based on HF Field-Strength Predic-

<!-- b000349 | references | pages [23] -->
tion[A]. Thirteen Chinese Conference SSTA :2011:5.

<!-- b000350 | references | pages [23] -->
[13] ZHUANG Qian-boSUN Fang-gang. Influence of Different Ground Forms on Short-

<!-- b000351 | references | pages [23] -->
wave Communication[J]. China NewTelecommunications,2014,16(09):92+97.

<!-- b000352 | references | pages [23] -->
[14] HUANG Fang. Research on Characteristics of Maritime Wireless Radio Propaga-

<!-- b000353 | references | pages [23] -->
tion and Channel Modeling[D]. HainanUniversity,2016,49(04):418-422.

<!-- b000354 | furniture | pages [24] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000355 | furniture | pages [24] -->
Team # 86103

<!-- b000356 | furniture | pages [24] -->
Page 21 of 25

<!-- b000357 | heading | pages [24] -->
Appendices

<!-- b000358 | heading | pages [24] -->
Appendix A

<!-- b000359 | prose | pages [24] -->
First appendix

<!-- b000360 | prose | pages [24] -->
Here are simulation programmes we used in our model as follow.

<!-- b000361 | prose | pages [24] -->
%Wave situaion fengji=8; pinpushu=1000; jiaodushu=5;

<!-- b000362 | prose | pages [24] -->
wavewmin = [2.438306 1.462983 1.044989 0.812770 0.664988 0.562683 0.487659 0.430288]; wavewmax = [16.444115 9.866469 7.047480 5.481373 4.484760 3.794799 3.288826 2.90190]; wavewp=[4.053570 2.432142 1.737244 1.351190 1.105519 0.935439 0.810714 0.715336];

<!-- b000363 | prose | pages [24] -->
%----------------------------------------------------- u=[3,5,7,9,11,13,15,17]; %---------------------------------------------------

<!-- b000364 | prose | pages [24] -->
if fengji>8 fengji=8; end if fengji<1 fengji=1; end fi=fengji; wmin=wavewmin(fi); wmax=wavewmax(fi); wp=wavewp(fi); ui=u(fi); M=pinpushu; N=jiaodushu; wavewn=(wmax-wmin)/M; thetawn=pi/N; dx=1; dy=1; x=[0:dx:500]; y=[0:dy:300]; [x,y]=meshgrid(x,y); z=zeros(size(x)); for wi=1:M for ki=1:N theta=-pi/2+(ki-1)*thetawn; epsin=rand*2*pi; w=wmin+(wi-1)*wavewn+wavewn/2; swi=0.81*exp(-7400/(w*ui+eps).^4)*2*(cos(theta)).^2/(pi*(w.^5+eps)); an=sqrt(2*swi*wavewn*theta); z1=w*w*x*cos(theta)/9.8+w*w*y*sin(theta)/9.8+epsin; z=an*cos(z1)+z; end end surfl(x,y,abs(z)); shading flat; colormap ;

<!-- b000365 | furniture | pages [25] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000366 | furniture | pages [25] -->
Team # 86103

<!-- b000367 | furniture | pages [25] -->
Page 22 of 25

<!-- b000368 | prose | pages [25] -->
lightangle(-45,30); set(findobj(gca,’type’,’surface’),’FaceLighting’,’phong’,’AmbientStrength’,.3,’DiffuseStrength ’Sp ecularStrength’,.9,’SpecularExponent’,200) set(gca,’ztick’,[0,5]);

<!-- b000369 | prose | pages [25] -->
%Figure 5:calculate the relationship between Rh,Rv and incidence angle thetas=(0:1:90); theta=thetas./180.*pi; niu=10; lambda=1./niu; epsilon=80-1i.*60.*lambda.*50; RH1=sin(theta)-sqrt(epsilon-cos(theta).^2); RH2=sin(theta)+sqrt(epsilon-cos(theta).^2); RHh=abs(RH1./RH2); subplot(1,2,1); plot(thetas,RHh,’LineWidth’,1.5);axis([0 90 0.2 1]);hold; xlabel(’incident angle(a˛)’) ylabel(’reflection coefficient’) RH1=epsilon.*sin(theta)-sqrt(epsilon-cos(theta).^2); RH2=epsilon.*sin(theta)+sqrt(epsilon-cos(theta).^2); RHv=abs(RH1./RH2); subplot(1,2,2); plot(thetas,RHv,’LineWidth’,1.5);axis([0 90 0.2 1]);hold; xlabel(’incident angle(a˛)’) ylabel(’reflection coefficient’) niu=20; lambda=1./niu; epsilon=80-1i.*60.*lambda.*50; RH1=sin(theta)-sqrt(epsilon-cos(theta).^2); RH2=sin(theta)+sqrt(epsilon-cos(theta).^2); RHh=abs(RH1./RH2); subplot(1,2,1); plot(thetas,RHh,’r’,’LineWidth’,1.5);axis([0 90 0.2 1]);hold; set(get(gca,’YLabel’),’Fontsize’,12) set(get(gca,’XLabel’),’Fontsize’,12) RH1=epsilon.*sin(theta)-sqrt(epsilon-cos(theta).^2); RH2=epsilon.*sin(theta)+sqrt(epsilon-cos(theta).^2); RHv=abs(RH1./RH2); subplot(1,2,2); plot(thetas,RHv,’r’,’LineWidth’,1.5);axis([0 90 0.2 1]);hold; set(get(gca,’YLabel’),’Fontsize’,12) set(get(gca,’XLabel’),’Fontsize’,12)

<!-- b000370 | prose | pages [25, 26] -->
%Figure 8:Diagrams of correction coefficients clc;clear; niu1=30*10^6;c=3*10^8;niu2=20*10^6;niu3=10*10^6; theta=1/180*pi; omega=[0:20]; h=0.0051.*omega.^2; g1=0.5*(4.*pi.*h.*niu1.*sin(theta)./c); g2=0.5*(4.*pi.*h.*niu2.*sin(theta)./c); g3=0.5*(4.*pi.*h.*niu3.*sin(theta)./c); rou1=1./(sqrt(3.2.*g1-2+sqrt((3.2.*g1).^2-7.*g1+9))); rou2=1./(sqrt(3.2.*g2-2+sqrt((3.2.*g2).^2-7.*g2+9))); rou3=1./(sqrt(3.2.*g3-2+sqrt((3.2.*g3).^2-7.*g3+9))); subplot(1,2,1); plot(omega,rou1,’r’,omega,rou2,’b’,omega,rou3,’g’,’LineWidth’,1.5);axis([0 20 0.97 1]);hold on legend(’10MHz’,’20MHz’,’30MHz’) xlabel(’wind speed(m/s)’) ylabel(’ correction coefficient’) set(get(gca,’YLabel’),’Fontsize’,12) set(get(gca,’XLabel’),’Fontsize’,12) niu=20*10^6; theta1=1/180*pi;c=3*10^8;theta2=5/180*pi;theta3=15/180*2; omega=[0:20]; h=0.0051.*omega.^2; g1=0.5*(4.*pi.*h.*niu.*sin(theta1)./c); g2=0.5*(4.*pi.*h.*niu.*sin(theta2)./c); g3=0.5*(4.*pi.*h.*niu.*sin(theta3)./c); rou1=1./(sqrt(3.2.*g1-2+sqrt((3.2.*g1).^2-7.*g1+9))); rou2=1./(sqrt(3.2.*g2-2+sqrt((3.2.*g2).^2-7.*g2+9))); rou3=1./(sqrt(3.2.*g3-2+sqrt((3.2.*g3).^2-7.*g3+9))); subplot(1,2,2); plot(omega,rou1,’r’,omega,rou2,’b’,omega,rou3,’g’,’LineWidth’,1.5);axis([0 20 0.84 1]); legend(’1a˛’,’5a˛’,’15a˛’) xlabel(’wind speed(m/s)’) ylabel(’ correction coefficient’) set(get(gca,’YLabel’),’Fontsize’,12) set(get(gca,’XLabel’),’Fontsize’,12)

<!-- b000371 | furniture | pages [26] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000372 | furniture | pages [26] -->
Team # 86103

<!-- b000373 | furniture | pages [26] -->
Page 23 of 25

<!-- b000375 | prose | pages [26, 27] -->
%Figure9 Relation curve of reflection coefficient under different wind %speed clc;clear; theta=87/180.*pi; niu=(3:30); lambda=1./niu; epsilon=80-1i.*60.*lambda.*50; RH1=sin(theta)-sqrt(epsilon-cos(theta).^2); RH2=sin(theta)+sqrt(epsilon-cos(theta).^2); RHh=abs(RH1./RH2); RH1=epsilon.*sin(theta)-sqrt(epsilon-cos(theta).^2); RH2=epsilon.*sin(theta)+sqrt(epsilon-cos(theta).^2); RHv=abs(RH1./RH2); RH=(power(RHh,2)+power(RHv,2))/2; theta1=87/180*pi; c=3*10^8; nius=[3:30]; niu=nius.*10^6; h1=0;h2=1.5;h3=3,h4=4.5; g1=0.5*(4.*pi.*h1.*niu.*sin(theta1)./c); g2=0.5*(4.*pi.*h2.*niu.*sin(theta1)./c); g3=0.5*(4.*pi.*h3.*niu.*sin(theta1)./c); g4=0.5*(4.*pi.*h4.*niu.*sin(theta1)./c); rou1=1./(sqrt(3.2.*g1-2+sqrt((3.2.*g1).^2-7.*g1+9))); rou2=1./(sqrt(3.2.*g2-2+sqrt((3.2.*g2).^2-7.*g2+9))); rou3=1./(sqrt(3.2.*g3-2+sqrt((3.2.*g3).^2-7.*g3+9))); rou4=1./(sqrt(3.2.*g4-2+sqrt((3.2.*g4).^2-7.*g4+9))); RH_1=RH.*rou1;RH_2=RH.*rou2;RH_3=RH.*rou3;RH_4=RH.*rou4; plot(nius,RH_1,’r’,nius,RH_2,’b’,nius,RH_3,’g’,nius,RH_4,’y’,’LineWidth’,1.5); xlabel(’frequency(MHz)’) ylabel(’reflection coefficient’) set(get(gca,’YLabel’),’Fontsize’,12) set(get(gca,’XLabel’),’Fontsize’,12) legend(’calm’,’level 2’,’level 4’,’level 6’) %Figure11 Reflection coefficient relationship curves under different ground %conditions clc;clear; theta=87/180.*pi; niu=(3:30); lambda=1./niu; epsilon=80-1i.*60.*lambda.*50; epsilon=8; RH1=sin(theta)-sqrt(epsilon-cos(theta).^2); RH2=sin(theta)+sqrt(epsilon-cos(theta).^2); RHh=abs(RH1./RH2); RH1=epsilon.*sin(theta)-sqrt(epsilon-cos(theta).^2); RH2=epsilon.*sin(theta)+sqrt(epsilon-cos(theta).^2); RHv=abs(RH1./RH2); RH=(power(RHh,2)+power(RHv,2))/2; theta1=87/180*pi; c=3*10^8; nius=[3:30]; niu=nius.*10^6; h1=0;h2=1.5;h3=3,h4=4.5; g1=0.5*(4.*pi.*h1.*niu.*sin(theta1)./c); g2=0.5*(4.*pi.*h2.*niu.*sin(theta1)./c); g3=0.5*(4.*pi.*h3.*niu.*sin(theta1)./c); g4=0.5*(4.*pi.*h4.*niu.*sin(theta1)./c); rou1=1./(sqrt(3.2.*g1-2+sqrt((3.2.*g1).^2-7.*g1+9))); rou2=1./(sqrt(3.2.*g2-2+sqrt((3.2.*g2).^2-7.*g2+9))); rou3=1./(sqrt(3.2.*g3-2+sqrt((3.2.*g3).^2-7.*g3+9))); rou4=1./(sqrt(3.2.*g4-2+sqrt((3.2.*g4).^2-7.*g4+9))); RH_1=RH.*rou1;RH_2=RH.*rou2;RH_3=RH.*rou3;RH_4=RH.*rou4; subplot(1,2,1) plot(nius,RH_1,’r’,nius,RH_2,’b’,nius,RH_3,’g’,nius,RH_4,’y’,’LineWidth’,1.5); xlabel(’frequency(MHz)’) ylabel(’reflection coefficient’) set(get(gca,’YLabel’),’Fontsize’,12) set(get(gca,’XLabel’),’Fontsize’,12) RH_1=-10*log10(RH_1);RH_2=-10*log10(RH_2);RH_3=-10*log10(RH_3);RH_4=-10*log10(RH_4); subplot(1,2,2) plot(nius,RH_1,’r’,nius,RH_2,’b’,nius,RH_3,’g’,nius,RH_4,’y’,’LineWidth’,1.5); xlabel(’frequency(MHz)’) ylabel(’Sea surface reflection loss’);legend(’calm’,’hills’,’low mountains’,’middle mountains’ set(get(gca,’YLabel’),’Fontsize’,12) set(get(gca,’XLabel’),’Fontsize’,12)

<!-- b000376 | furniture | pages [27] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000377 | furniture | pages [27] -->
Team # 86103

<!-- b000378 | furniture | pages [27] -->
Page 24 of 25

<!-- b000380 | prose | pages [27, 28] -->
%figure 13 relationship among distances frequency and SNR clear;clc;format ; P=100;B=3000*10^-6;Yp=15;La=4;Fa=80;f=[3:30]; r=[4000:1000:20000];R=6371;h=300;c=3*10^8;flow=3; n=1;thetas=(3:3:90);theta=thetas.*pi./180; D=2*R*(acos(R/(R+h)*cos(theta))-theta); lambda=1./f; epsilon=80-1i.*60.*lambda.*50; RH1=zeros(length(theta),length(epsilon)); RH2=zeros(length(theta),length(epsilon)); RHh=zeros(length(theta),length(epsilon)); RHv=zeros(length(theta),length(epsilon)); RH=zeros(length(theta),length(epsilon)); for i=1:length(theta) for j=1:length(f) RH1(i,j)=sin(theta(i))-sqrt(epsilon(j)-cos(theta(i))^2); RH2(i,j)=sin(theta(i))+sqrt(epsilon(j)-cos(theta(i))^2); RHh(i,j)=abs(RH1(i,j)/RH2(i,j)); RH1(i,j)=epsilon(j)*sin(theta(i))-sqrt(epsilon(j)-cos(theta(i))^2); RH2(i,j)=epsilon(j)*sin(theta(i))+sqrt(epsilon(j)-cos(theta(i))^2); RHh(i,j)=abs(RH1(i,j)/RH2(i,j)); RH(i,j)=(power(RHh(i,j),2)+power(RHv(i,j),2));%¡ˇn end end rou=zeros(length(theta),length(epsilon)); g=zeros(length(theta),length(epsilon)); niu=f.*10^6; for i=1:length(theta) for j=1:length(f) g(i,j)=0.5*(4.*pi.*flow.*niu(j).*sin(theta(i))./c); rou(i,j)=1./(sqrt(3.2.*g(i,j)-2+sqrt((3.2.*g(i,j)).^2-7.*g(i,j)+9))); end end RH=RH.*rou; Lg=-10*log10(RH); for n=1:6 for j=1:30 thetax=3*j; L(1,j)=n*D(1,j); for i=1:28 fs=i+2; SNR(j,i)=201.56+10*log10(P)-20*log10(fs)-20*log10(L(1,j))-10*log10(B)-n*La-(n-1)* if i==13 dis(n)=L(1,1) end end end mesh(f,L,SNR);hold on; max(n)=min(SNR(:,13)) end

<!-- b000381 | furniture | pages [28] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000382 | furniture | pages [28] -->
Team # 86103

<!-- b000383 | furniture | pages [28] -->
Page 25 of 25
