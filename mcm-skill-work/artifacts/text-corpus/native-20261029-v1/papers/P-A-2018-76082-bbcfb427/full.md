# P-A-2018-76082-bbcfb427

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000002 | furniture | pages [1] -->
Team Control Number

<!-- b000003 | title | pages [1] -->
76082

<!-- b000004 | prose | pages [1] -->
For office use only

<!-- b000005 | prose | pages [1] -->
For office use only

<!-- b000006 | prose | pages [1] -->
T1

<!-- b000007 | prose | pages [1] -->
F1

<!-- b000008 | prose | pages [1] -->
T2

<!-- b000009 | prose | pages [1] -->
F2

<!-- b000010 | prose | pages [1] -->
T3

<!-- b000011 | prose | pages [1] -->
F3

<!-- b000012 | prose | pages [1] -->
Problem Chosen

<!-- b000013 | title | pages [1] -->
A

<!-- b000014 | prose | pages [1] -->
F4

<!-- b000015 | prose | pages [1] -->
T4

<!-- b000016 | prose | pages [1] -->
2018 MCM/ICM Summary Sheet.

<!-- b000017 | title | pages [1] -->
HF Radio Propagation under Different Terrains

<!-- b000018 | heading | pages [1] -->
Summary

<!-- b000019 | prose | pages [1] -->
Even in the satellite era, high-frequency (HF) signal communication still plays an important role in everyday communications. In order to clearly understand the communication process of HF waves and its influencing factors, we first design a mathematical model of signal reflection off the ocean. Based on this model, we build the ground signal reflection model and compare the two. Besides, we study the communication process of vessel receivers on a turbulent sea.

<!-- b000020 | prose | pages [1] -->
We begin with the establishment of a mathematical model of signal reflection at sea from two aspects. On the one hand, we study the basic loss of the HF sky wave transmission process. On the other hand, we investigate the surface properties of the sea. We classify the ocean surface as a smooth and a rough sea. Based on the Fresnel reflection coefficient equation, we obtain the reflection intensity of rough and smooth sea surface. And their ratio equals to the square of the roughness correction factor. We select specific parameters for getting the specific value. Then we get the first reflection power of rough sea surface is 0.4378mW, and the first reflection power of smooth sea surface is 0.2832mW. The first reflection power of rough sea surface is 0.6469 times smooth sea surface. As a result, using this model, we can easily simulate the multi- hop path of the signal. Taking the selected specific value as the parameter, we calculate the maximum number of hops to 8 times if the signal-noise ratio threshold is not exceeded.

<!-- b000021 | prose | pages [1] -->
Next, based on the above models, we set up the mathematical model of ground signal reflection. Similarly, we classify the terrain as a smooth terrain and a mountainous terrain. The propagation loss of mountainous terrain is classified as diffraction loss of the mountain and absorption loss of the vegetation. We use Epstein-Peterson method to study the typical double- edged peak diffraction problem. Through comparison of the two models, we conclude that the ocean surface is more suitable for the transmission of shortwave skywaves than land surfaces.

<!-- b000022 | prose | pages [1] -->
What’s more, we introduce the ship sway model to further establish the communication model of the ship receiver at sea. The ship can maintain communication while traveling in the signal coverage. We get the longest communication time by calculating the maximum travel time of the ship in the signal coverage area.

<!-- b000023 | prose | pages [1] -->
Finally, we prepare a synopsis of the results that are suitable as a short note in IEEE Communications Magazine.

<!-- b000024 | prose | pages [1] -->
We focus on the transmission process of shortwave skywaves off the ocean. The conclusion can help in the communications of maritime transport and fishing industries.

<!-- b000025 | keywords | pages [1] -->
Keywords: Fresnel reflection coefficient equation, Sea signal reflection model, Transmission

<!-- b000026 | prose | pages [1] -->
loss

<!-- b000027 | furniture | pages [2] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000028 | furniture | pages [2] -->
Page 1 of 24

<!-- b000029 | furniture | pages [2] -->
Team#76082

<!-- b000030 | prose | pages [2] -->
Content

<!-- b000031 | prose | pages [2] -->
1.Introduction...................................................................................................................2 1.1 Restatement of the problem..................................................................................2 1.2 Notations.............................................................................................................. 3 2. Assumptions..................................................................................................................3 3. Skywave basic transmission loss................................................................................4 3.1 Loss model........................................................................................................... 4 3.2 Calculation Results Analysis...............................................................................5 4.The Mathematical Model of Ocean signal’s Reflection.............................................6 4.1Basic model...........................................................................................................6 4.1.1 Sea surface’s plural dielectric constant.............................................................6 4.1.2 Fresnel reflection coefficient of Sea......................................................................7 4.2Comparison of Reflection Intensity between Rough Sea and Smooth Sea.........11 4.3Calculation of the maximum number of hops.....................................................12

<!-- b000032 | prose | pages [2] -->
4.3.1 Signal to noise ratio calculation of shortwave sky wave communication............12 4.3.2 Calculation results............................................................................................... 12

<!-- b000033 | prose | pages [2] -->
5.The comparison of Ground Signal Transmission and Sea Signal Transmission... 13 5.1 The mathematical model of ground signal reflection.........................................13 5.1.1 Shortwave sky wave propagation loss in the smooth terrain...............................13 5.1.2 Shortwave sky wave in mountainous terrain transmission loss.......................... 13 5.2 Comparing results.............................................................................................. 14 6. The communication model of marine ship receiver................................................15 6.1 The model of ship rocks.....................................................................................15 6.2 Sea signal transmission model of combining ship swaying...............................16 6.3The same multi-hop path to maintain communication time................................18 7. Sensitivity Analysis-Time factor............................................................................... 19 8 Conclusions..................................................................................................................20 8.1 Strengths.............................................................................................................20 8.2 Weaknesses.........................................................................................................20 References.......................................................................................................................24

<!-- b000034 | furniture | pages [3] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000035 | furniture | pages [3] -->
Page 2 of 24

<!-- b000036 | furniture | pages [3] -->
Team#76082

<!-- b000037 | heading | pages [3] -->
1.Introduction

<!-- b000038 | heading | pages [3] -->
1.1 Restatement of the problem

<!-- b000039 | prose | pages [3] -->
The high frequency（HF, defined to be 3-30MHz）is the portion of the radio frequency spectrum . The HF band is a major part of the shortwave frequency band, so communication at these frequency is often called shortwave radio. Shortwave propagation modes include groundwave and skywaves. For frequencies below the maximum usable frequency (MUF), HF radio waves can travel further through the multiple reflections of the ionosphere and the earth's surface (even to the world). This method of communication is called "skip" or "skywave".

<!-- b000040 | prose | pages [3] -->
Many factors affect the propagation of HF skywaves, of which the properties of the reflecting surface are important. The properties of the reflecting surface determine the strength of the reflected wave and how far the wave will propagate with the useful signal integrity. The most important issue is the reflections on the sea.

<!-- b000041 | prose | pages [3] -->
We define the raging sea as a rough sea, and relatively speaking, we define a calm sea as a smooth sea.

<!-- b000042 | prose | pages [3] -->
The problems that we need to solve in this paper are: Establish a mathematical model of ocean signal reflection. Determine a first reflection intensity of a 100-watt HF constant carrier signal

<!-- b000043 | prose | pages [3] -->
transmitted from a land-based source at the turbulent ocean level. In this paper, we use the size of power on behalf of the strength of the size. Compare the above result with the first reflected intensity of the same signal on a

<!-- b000044 | prose | pages [3] -->
calm ocean surface Based on the first issue, the remaining reflections of the radio signals occur on a

<!-- b000045 | prose | pages [3] -->
calm sea surface. Determining the maximum number of hops the signal can reach before its strength falls below a usable signal-to- noise ratio (SNR) threshold of 10 dB Using the results obtained above compared with the results of high-frequency radio-

<!-- b000046 | prose | pages [3] -->
wave reflections on rugged versus smooth terrain. There is a marine vessel that uses high frequencies to communicate and receive

<!-- b000047 | prose | pages [3] -->
weather and traffic reports. Transforming the model to accommodate radio transmissions from the ship's receiver on a raging surface. Calculate the time that the boat keeps the signal commutating in the same multi-hop path.

<!-- b000048 | furniture | pages [4] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000049 | furniture | pages [4] -->
Team#76082

<!-- b000050 | heading | pages [4] -->
1.2 Notations

<!-- b000051 | furniture | pages [4] -->
Page 3 of 24

<!-- b000052 | prose | pages [4] -->
Let's first define the list of notations used in this article: Symbols Definition

<!-- b000053 | prose | pages [4] -->
Sea water relative dielectric constant r

<!-- b000054 | prose | pages [4] -->
 Sea water conductivity

<!-- b000055 | prose | pages [4] -->
Wavelength 

<!-- b000056 | prose | pages [4] -->
f The best available radio frequency

<!-- b000057 | prose | pages [4] -->
Smooth sea reflection coefficient R

<!-- b000058 | prose | pages [4] -->
Rough sea reflection coefficient R

<!-- b000059 | prose | pages [4] -->
 Rough correction factor

<!-- b000060 | prose | pages [4] -->
 Sea surface dielectric constant 

<!-- b000061 | prose | pages [4] -->
RH polarized Horizontal coefficient Rv wave Fresnel reflection

<!-- b000062 | prose | pages [4] -->
Vertical polarization Fresnel reflection coefficient

<!-- b000063 | prose | pages [4] -->
Signal to noise ratio

<!-- b000064 | prose | pages [4] -->
SNR Lb

<!-- b000065 | prose | pages [4] -->
Skywave basic transmission loss

<!-- b000066 | prose | pages [4] -->
Lbf

<!-- b000067 | prose | pages [4] -->
Transmission loss of free space

<!-- b000068 | prose | pages [4] -->
Li

<!-- b000069 | prose | pages [4] -->
Ionospheric absorption loss

<!-- b000070 | prose | pages [4] -->
Yp

<!-- b000071 | prose | pages [4] -->
Extra system loss

<!-- b000072 | heading | pages [4] -->
2. Assumptions

<!-- b000073 | prose | pages [4] -->
Calm sea is equivalent to a smooth sea, so calm sea is the reflection of radio waves is

<!-- b000074 | prose | pages [4] -->
specular reflection. The object of our study is the high frequency band of 3-30 MHz. If the wave

<!-- b000075 | prose | pages [4] -->
frequency exceeds MUF, the electric wave will enter the space through the ionosphere and the ionosphere will change frequently. Therefore, the best available frequency is usually 0.8 -0.9 times, we conservatively assume that the best available f 20MHz . frequency is

<!-- b000076 | prose | pages [4] -->
When the wavelength and the wave height are comparable or even far less than the

<!-- b000077 | prose | pages [4] -->
wave height, the influence of the shadow effect on the radio wave propagation needs to be considered. However, this dissertation is not applicable. Therefore, the influence of the shadow effect on the radio wave propagation is ignored. Assume that the directional factor of the emission and reception antennas is 1. Suppose the emitted electromagnetic wave is a circularly polarized wave. Assume that multipath interference is ignored

<!-- b000078 | furniture | pages [5] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000079 | furniture | pages [5] -->
Page 4 of 24

<!-- b000080 | furniture | pages [5] -->
Team#76082

<!-- b000081 | heading | pages [5] -->
3. Skywave basic transmission loss

<!-- b000082 | heading | pages [5] -->
3.1 Loss model

<!-- b000083 | prose | pages [5] -->
In order to clearly describe the spread of the electric wave, we give the figure 1 about a simple representation of its jumping process:

<!-- b000084 | caption | pages [5] -->
Figure1 Signal transmission diagram

<!-- b000085 | prose | pages [5] -->
A radio wave emitted by the terrestrial source first reaches the ionosphere and reaches the sea level through the reflection of the ionosphere. It is its first hopping process. After being reflected by the sea, it returns to the ionosphere and returns to the sea for the second jump and so on.

<!-- b000086 | prose | pages [5] -->
We know that, in practice, radio waves produce loss of energy when transmitting. According to the reason of transmission loss, the basic transmission loss of skywave is expressed as[1]

<!-- b000087 | prose | pages [5] -->
Lb LbfLiLg Yp (1)

<!-- b000088 | prose | pages [5] -->
Where: Lbfis the transmission loss in free space; Li is the ionospheric absorption loss; Lg is reflection loss on the ground; Yp is the additional system loss. We mainly discuss the ionospheric absorption loss and space transmission loss.

<!-- b000089 | prose | pages [5] -->
Basic transmission loss in free space Lbf The basic transmission loss in free space is the energy loss. the geometric diffusion causes energy loss after the radio wave leaves the transmitting antenna. The formula is [2]:

<!-- b000090 | prose | pages [5] -->
Lbf 32.4420lg f 20lgr (2)

<!-- b000091 | prose | pages [5] -->
Where: The unit of Lbf is dB; f is the working frequency, the unit is MHz; r is effective

<!-- b000092 | furniture | pages [6] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000093 | furniture | pages [6] -->
Team#76082

<!-- b000094 | furniture | pages [6] -->
Page 5 of 24

<!-- b000095 | prose | pages [6] -->
path for the propagation of radio waves, the unit is km. Ionospheric absorption loss Li In the ionosphere, there is a region of significant ionization in the atmosphere. In accordance with the electronic density changes with height, the ionosphere can be divided into D layer, E layer, F1 layer and F2 layer. The F layer is the reflective layer, because it is highest and allows the radio waves to travel the furthest distance[3]. Therefore, we consider the high-frequency signals mainly reflect on the F1 layer (150km-200km) in this paper.

<!-- b000096 | prose | pages [6] -->
Since the degree of ionospheric absorption relates to many factors, it is difficult to make theoretical calculations. So we choose semi-empirical formula[3-4]:

<!-- b000097 | prose | pages [6] -->
L  bf 677.2I seci100 (3) ( f f )1.98 10.2

<!-- b000098 | prose | pages [6] -->
H

<!-- b000099 | prose | pages [6] -->
I (10.0037R)(cos(0.881))1.3

<!-- b000100 | prose | pages [6] -->
(4)

<!-- b000101 | prose | pages [6] -->
i100 arcsin(0.985 cos )

<!-- b000102 | prose | pages [6] -->
Where: fH

<!-- b000103 | prose | pages [6] -->
(5)

<!-- b000104 | prose | pages [6] -->
is the frequency of the magnetic swing at a height of 100 km; I is the absorption coefficient, and represents the relationship of the ionospheric absorption and solar zenith angle and sunspots R ; i100 is the 100km-height of the incident angle, is the ray elevation.

<!-- b000105 | prose | pages [6] -->
Under certain circumstances, these parameters can access data to get a specific value. Extra system loss Yp The extra system loss is the sum of the losses calculated for other reasons, and accurate calculation is difficult. Since the additional system loss is basically a function of the local

<!-- b000106 | prose | pages [6] -->
time[1], we can estimate the additional system loss by looking at the data sheet. Reflection loss on the ground Lg Ground loss occurs from the radio wave through the ground reflection. In this model, the electric wave is reflected on the sea surface, so we do not consider the ground reflection loss.

<!-- b000107 | heading | pages [6] -->
3.2 Calculation Results Analysis

<!-- b000108 | prose | pages [6] -->
In order to make the calculation easily, we choose the typical numerical value to simulate.

<!-- b000109 | prose | pages [6] -->
The parameters we choose are as follows: Ray elevation =, Ionospheric height h 200 km ,so it is easy to obtain the ffective path of radio wave propagation r 200 2 km .Reflection point (123E, 26N ) is located in the East China Sea；fH = 1.24MHz; time point is 12:00 on July 1, check the number of sunspots R 110.

<!-- b000110 | prose | pages [6] -->
The sun zenith angle can be calculated by the following formula[4]:

<!-- b000111 | furniture | pages [7] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000112 | furniture | pages [7] -->
Team#76082

<!-- b000113 | furniture | pages [7] -->
Page 6 of 22

<!-- b000114 | prose | pages [7] -->
cos sin asin Sx cosacos Sx cos

<!-- b000115 | prose | pages [7] -->
Sx 23.44 sin[0.9856(Yn 80.7)]

<!-- b000116 | prose | pages [7] -->
(6) 18015(24 t 8) Sy  0 t 8

<!-- b000117 | prose | pages [7] -->
180 15(t8)  8 t 24

<!-- b000118 | prose | pages [7] -->
Where: Sx is the sun’s point of latitude, Sy is the sun’s point of longitude, Yn is the number of days from January 1 each year; t is Beijing time, a is the study point’s latitude; 

<!-- b000119 | prose | pages [7] -->
is the difference between study point’s longitude and Sy .

<!-- b000120 | prose | pages [7] -->
After simulation we get the transmission loss Lf We learn from the formula

<!-- b000121 | prose | pages [7] -->
is 97.4597dB.

<!-- b000122 | prose | pages [7] -->
L 10lg Pr

<!-- b000123 | prose | pages [7] -->
b

<!-- b000124 | prose | pages [7] -->
Calculate the power Pt

<!-- b000125 | prose | pages [7] -->
(7)

<!-- b000126 | prose | pages [7] -->
Pt

<!-- b000127 | prose | pages [7] -->
of a high-frequency constant carrier signal transmitted by a terrestrial source is 100W, incident power Pr is 0.43248mW.

<!-- b000128 | prose | pages [7] -->
reaching the sea surface after transmission loss

<!-- b000129 | heading | pages [7] -->
4.The Mathematical Model of Ocean signal’s Reflection

<!-- b000130 | heading | pages [7] -->
4.1Basic model

<!-- b000131 | prose | pages [7] -->
The reflection coefficient of sea waves mainly represents the reflection characteristics of sea waves on the surface of the sea. The reflection coefficient is related to the incident angle of the sea waves, the size of the waves, the electromagnetic parameters of the sea surface and other factors.

<!-- b000132 | prose | pages [7] -->
Before studying the reflection characteristics, we first study the electromagnetic properties of the sea surface. The electromagnetic characteristics of sea surface affect the sea surface reflection intensity of radio waves, and it is related to the seawater temperature, salinity, electromagnetic wave frequency and other factors. The complex permittivity of the sea is a parameter describing the electromagnetic properties of the sea surface.

<!-- b000133 | heading | pages [7] -->
4.1.1 Sea surface’s plural dielectric constant

<!-- b000134 | prose | pages [7] -->
The plural dielectric constant of sea surface is determined by the relative dielectric constant of seawater r, sea water conductivity and the wave length , the expression is [1]:

<!-- b000135 | prose | pages [7] -->
 (8) =r i60

<!-- b000136 | prose | pages [7] -->
We can calculate constants r and ratiobased on the polynomial fit function given by Consultants Committee of the International Radio (CCIR).

<!-- b000137 | prose | pages [7] -->
Relative dielectric constant of the sea water

<!-- b000138 | furniture | pages [8] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000139 | furniture | pages [8] -->
Team#76082

<!-- b000140 | prose | pages [8] -->


<!-- b000141 | furniture | pages [8] -->
Page 7 of 24

<!-- b000142 | prose | pages [8] -->
The expression of sea water’s relative dielectric constant is[5]

<!-- b000143 | prose | pages [8] -->
70

<!-- b000144 | prose | pages [8] -->
 

<!-- b000145 | prose | pages [8] -->
1

<!-- b000146 | prose | pages [8] -->


<!-- b000147 | prose | pages [8] -->


<!-- b000148 | prose | pages [8] -->
r

<!-- b000149 | prose | pages [8] -->


<!-- b000150 | prose | pages [8] -->
2 3

<!-- b000151 | prose | pages [8] -->
a bf

<!-- b000152 | furniture | pages [8] -->


<!-- b000153 | furniture | pages [8] -->


<!-- b000154 | prose | pages [8] -->
cf

<!-- b000155 | furniture | pages [8] -->


<!-- b000156 | furniture | pages [8] -->


<!-- b000157 | prose | pages [8] -->
df

<!-- b000158 | furniture | pages [8] -->


<!-- b000159 | prose | pages [8] -->
   

<!-- b000160 | prose | pages [8] -->
Where:

<!-- b000161 | prose | pages [8] -->
f 2253.5895

<!-- b000162 | prose | pages [8] -->


<!-- b000163 | prose | pages [8] -->
f 2253.5895

<!-- b000164 | prose | pages [8] -->


<!-- b000165 | prose | pages [8] -->
4

<!-- b000166 | furniture | pages [8] -->


<!-- b000167 | furniture | pages [8] -->


<!-- b000168 | prose | pages [8] -->
ef

<!-- b000169 | prose | pages [8] -->
f is the radio frequency, and its units is MHz; a 1.4114535102 ；b 5.2122497 108 ；c 5.8547829 1011

<!-- b000170 | prose | pages [8] -->
d 7.67174231016 ；e 2.98563181021

<!-- b000171 | prose | pages [8] -->
Conductivity of the Sea water The expression of sea water’s conductivity is[5]

<!-- b000172 | prose | pages [8] -->
0.5

<!-- b000173 | prose | pages [8] -->
 

<!-- b000174 | prose | pages [8] -->
r sf

<!-- b000175 | prose | pages [8] -->
tf

<!-- b000176 | prose | pages [8] -->
 

<!-- b000177 | prose | pages [8] -->


<!-- b000178 | prose | pages [8] -->


<!-- b000179 | prose | pages [8] -->


<!-- b000180 | prose | pages [8] -->
2

<!-- b000181 | prose | pages [8] -->
1 uf

<!-- b000182 | furniture | pages [8] -->


<!-- b000183 | furniture | pages [8] -->


<!-- b000184 | prose | pages [8] -->
uf

<!-- b000185 | furniture | pages [8] -->


<!-- b000186 | prose | pages [8] -->
 

<!-- b000187 | prose | pages [8] -->
Where:

<!-- b000188 | prose | pages [8] -->
f

<!-- b000189 | furniture | pages [8] -->


<!-- b000190 | prose | pages [8] -->
1106.207

<!-- b000191 | prose | pages [8] -->
 (10)

<!-- b000192 | prose | pages [8] -->
2 2

<!-- b000193 | prose | pages [8] -->
f

<!-- b000194 | furniture | pages [8] -->


<!-- b000195 | prose | pages [8] -->
1106.207

<!-- b000196 | prose | pages [8] -->


<!-- b000197 | prose | pages [8] -->
3

<!-- b000198 | prose | pages [8] -->
wf

<!-- b000199 | prose | pages [8] -->
 

<!-- b000200 | prose | pages [8] -->
f is the radio frequency, its units is MHz;

<!-- b000201 | prose | pages [8] -->
r 3.8586749 ；s 9.1253873104 ；t 1.5309921108

<!-- b000202 | prose | pages [8] -->
u 2.1179295105 ；v 6.5727504 1010 ；w 1.9647664 1015

<!-- b000203 | prose | pages [8] -->
is 20MHz, we can get seawater relative permittivity r= 70; f Because we assume sea water conductivity 5.0; Sea surface dielectric constant

<!-- b000204 | prose | pages [8] -->


<!-- b000205 | prose | pages [8] -->
70 4500i 。

<!-- b000206 | heading | pages [8] -->
4.1.2 Fresnel reflection coefficient of Sea

<!-- b000207 | prose | pages [8] -->
Fresnel reflection coefficient of smooth sea According to snell's law, the Fresnel reflection coefficient of horizontal and vertical polarized waves on a smooth sea surface is[5]

<!-- b000208 | prose | pages [8] -->
RH

<!-- b000209 | prose | pages [8] -->
RV

<!-- b000210 | prose | pages [8] -->
Where:is grazing angle of incidence.

<!-- b000211 | prose | pages [8] -->
 cos2 sin

<!-- b000212 | prose | pages [8] -->
(11)

<!-- b000213 | prose | pages [8] -->
 cos2 sin

<!-- b000214 | prose | pages [8] -->
 

<!-- b000215 | prose | pages [8] -->


<!-- b000216 | prose | pages [8] -->
cos2

<!-- b000217 | prose | pages [8] -->
sin

<!-- b000218 | prose | pages [8] -->
(12)

<!-- b000219 | prose | pages [8] -->
 

<!-- b000220 | prose | pages [8] -->


<!-- b000221 | prose | pages [8] -->
cos2

<!-- b000222 | prose | pages [8] -->
sin

<!-- b000223 | prose | pages [8] -->
The curve in Figure 2 reflects the relationship between the power reflection coefficient and the grazing incidence angle

<!-- b000224 | furniture | pages [9] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000225 | furniture | pages [9] -->
Page 8 of 24

<!-- b000226 | furniture | pages [9] -->
Team#76082

<!-- b000227 | prose | pages [9] -->
.

<!-- b000228 | caption | pages [9] -->
Figure 2 power reflection coefficient and the grazing incidence angle.

<!-- b000229 | prose | pages [9] -->
The grazing incidence angle is 4590 by observing, the change of the power reflection coefficient is not obvious.

<!-- b000230 | prose | pages [9] -->
For convenience of calculation, we set the grazing incidence angle as 45.

<!-- b000231 | prose | pages [9] -->
Fresnel reflection coefficient of rough sea We can easily get a smooth sea reflection coefficient, in fact, the sea is choppy, so we continue to study the reflection coefficient of the rough sea. Wave phenomenon is random and non-linear, so it is difficult to establish an accurate model of waves. According to the wave spectrum and the theory of stochastic ocean waves, we can regard the actual ocean waves as the result of the superposition of sine waves of different frequencies, different initial phases, different directions of propagation, and different wave heights..

<!-- b000232 | caption | pages [9] -->
Figure 3 is our simulation of the waves.

<!-- b000233 | caption | pages [9] -->
Figure 3 ocean wave diagram

<!-- b000234 | prose | pages [9] -->
In the raging sea, wave height, shape, and frequency change rapidly and wave

<!-- b000235 | furniture | pages [10] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000236 | furniture | pages [10] -->
Team#76082

<!-- b000237 | furniture | pages [10] -->
Page 9 of 24

<!-- b000238 | prose | pages [10] -->
propagation direction may change. To simplify the model, we only consider the effect of frequency and wave height on the roughness of the sea surface.

<!-- b000239 | prose | pages [10] -->
At present, Pierson-Moscowitz spectrum (Neutron spectrum), NTC spectrum (ITTC) and two-parameter ITTC spectrum are the most widely used marine spectra. Among them, PM spectrum is the most widely used, so we use PM spectrum to describe the frequency of ocean waves. The expression of PM spectrum is

<!-- b000240 | prose | pages [10] -->
8.1103 g 2 S(i)   g 4

<!-- b000241 | prose | pages [10] -->
exp[0.74( ) ]

<!-- b000242 | prose | pages [10] -->
(13)

<!-- b000243 | prose | pages [10] -->
5 5 v

<!-- b000244 | prose | pages [10] -->
Where: v is the average wind speed near the height of the sea surface.

<!-- b000245 | caption | pages [10] -->
Figure 4 describes the spectrum with the wind speed changes:

<!-- b000246 | prose | pages [10] -->
Figure 4 Wave spectrum From figure 4 we conclude that wind speed is a major factor affecting the frequency of waves.

<!-- b000247 | prose | pages [10] -->
Next we study the influence of wave height on the reflection coefficient. Phillips (1996) wave model as follows[6-7]:

<!-- b000248 | prose | pages [10] -->
According to

<!-- b000249 | prose | pages [10] -->
(14) h 0.0051v2

<!-- b000250 | prose | pages [10] -->
Where: h is the root mean square height of the sea surface, v is the wind speed near the height of the sea surface.

<!-- b000251 | prose | pages [10] -->
It is obvious that the high wind speed near the sea surface directly affects the root mean square of the sea surface. Therefore, we believe wind speed is a common major factor affecting frequency and wave height.

<!-- b000252 | prose | pages [10] -->
It is obvious that the high wind speed near the sea surface directly affects the root mean square of the sea surface. Therefore, we believe wind speed is a common major factor affecting frequency and wave height.

<!-- b000253 | prose | pages [10] -->
Then we can get rough correction factor expression based on Miller-Brown rough surface approximation model[8-9]

<!-- b000254 | prose | pages [10] -->
exp[2(2g)2 ]I [2(2g)2 ] (15)

<!-- b000255 | prose | pages [10] -->
0

<!-- b000256 | furniture | pages [11] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000257 | furniture | pages [11] -->
Team#76082

<!-- b000258 | furniture | pages [11] -->
Page 10 of 24

<!-- b000259 | prose | pages [11] -->
Where: I0 is the first kind of modified Bessel function of order 0;

<!-- b000260 | prose | pages [11] -->
g is the sea surface roughness which is used to describe the magnitude of sea surface The formula is g h sin/ 。 fluctuations.

<!-- b000261 | caption | pages [11] -->
Figure 5 shows the effect of wind speed on the roughness correction factor.

<!-- b000262 | caption | pages [11] -->
Figure 5 Relationship between wind speed and power reflection coefficient

<!-- b000263 | caption | pages [11] -->
Figure 5 shows that when the wind speed exceeds a certain level, the roughness

<!-- b000264 | prose | pages [11] -->
correction factor decreases rapidly with increasing wind speed.

<!-- b000265 | prose | pages [11] -->
Because communication at sea is a communication distance, the influence of earth curvature on the correction factor can not be ignored. D represents the Earth's curvature factor, which is calculation formula 16 [10]

<!-- b000266 | prose | pages [11] -->


<!-- b000267 | prose | pages [11] -->
2

<!-- b000268 | prose | pages [11] -->
G

<!-- b000269 | prose | pages [11] -->


<!-- b000270 | prose | pages [11] -->
1

<!-- b000271 | prose | pages [11] -->
D

<!-- b000272 | prose | pages [11] -->
 

<!-- b000273 | prose | pages [11] -->
1

<!-- b000274 | prose | pages [11] -->


<!-- b000275 | prose | pages [11] -->
R G G 

<!-- b000276 | prose | pages [11] -->


<!-- b000277 | prose | pages [11] -->
1

<!-- b000278 | prose | pages [11] -->
e

<!-- b000279 | prose | pages [11] -->
1

<!-- b000280 | prose | pages [11] -->


<!-- b000281 | prose | pages [11] -->


<!-- b000282 | prose | pages [11] -->
G G

<!-- b000283 | prose | pages [11] -->
2

<!-- b000284 | prose | pages [11] -->


<!-- b000285 | prose | pages [11] -->
2 2

<!-- b000286 | prose | pages [11] -->
(16)

<!-- b000287 | prose | pages [11] -->


<!-- b000288 | prose | pages [11] -->
sin

<!-- b000289 | prose | pages [11] -->


<!-- b000290 | prose | pages [11] -->


<!-- b000291 | prose | pages [11] -->
2 2

<!-- b000292 | prose | pages [11] -->
Where, G1 is the distance from the RF transmitting end to the specular reflection point,

<!-- b000293 | prose | pages [11] -->
and is the distance from the specular reflection point to the RF receiving end, which is the radius of the earth (the effective earth radius is 6400km).

<!-- b000294 | prose | pages [11] -->
Therefore, the rough correction factor for earth curvature is taken into account D .

<!-- b000295 | prose | pages [11] -->
We use the roughness correction factor to approximate the Fresnel reflection coefficient of the horizontal and vertical polarized waves of a rough sea surface

<!-- b000296 | prose | pages [11] -->
R

<!-- b000297 | prose | pages [11] -->
R

<!-- b000298 | prose | pages [11] -->
' '

<!-- b000299 | prose | pages [11] -->
R

<!-- b000300 | prose | pages [11] -->


<!-- b000301 | prose | pages [11] -->


<!-- b000302 | prose | pages [11] -->
H H H

<!-- b000303 | prose | pages [11] -->
(17)

<!-- b000304 | prose | pages [11] -->
' '

<!-- b000305 | prose | pages [11] -->
R

<!-- b000306 | prose | pages [11] -->


<!-- b000307 | prose | pages [11] -->


<!-- b000308 | prose | pages [11] -->
V V V

<!-- b000309 | prose | pages [11] -->
Depending on the relationship of the wavelength and frequency c v . When we can 20MHz , wave length get the frequency f 15m .

<!-- b000310 | prose | pages [11] -->
In this case, the wavelength is comparable to the height of the waves, as a result, shadowing may occur, in this article, to simplify the model, we assume no impact.

<!-- b000311 | prose | pages [11] -->
In order to meet the computing needs, we take six wind speed v 15m / s ,then h 1.1475 .Because45, We can get according to formula (15) The value of is

<!-- b000312 | furniture | pages [12] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000313 | furniture | pages [12] -->
Page 11 of 24

<!-- b000314 | furniture | pages [12] -->
Team#76082

<!-- b000315 | prose | pages [12] -->
0.8043.

<!-- b000316 | prose | pages [12] -->
4.2Comparison of Reflection Intensity between Rough Sea and

<!-- b000317 | prose | pages [12] -->
Smooth Sea

<!-- b000318 | prose | pages [12] -->
In order to facilitate the study, we replace the intensity with the power, so the power ratio is equal to the ratio of the intensity.

<!-- b000319 | prose | pages [12] -->
We set P1 as outgoing radio wave power for smooth sea surface.

<!-- b000320 | prose | pages [12] -->
Based on the concept of circularly polarized waves can be the formula

<!-- b000321 | prose | pages [12] -->
Where: RH

<!-- b000322 | prose | pages [12] -->
is Fresnel reflection coefficient of horizontal polarized wave on a smooth

<!-- b000323 | prose | pages [12] -->
sea surface; RV

<!-- b000324 | prose | pages [12] -->
is the Fresnel reflection coefficient of a vertically polarized wave on a smooth sea surface.

<!-- b000325 | prose | pages [12] -->
Again, we set P2

<!-- b000326 | prose | pages [12] -->
as Rough surface of the outgoing radio power.

<!-- b000327 | prose | pages [12] -->
We can get

<!-- b000328 | prose | pages [12] -->
When the electric waves emitted by the terrestrial sources are reflected for the first time, the incident electric wave power is the same both in the rough sea and in the smooth sea, so the sea surface reflection coefficient determines the difference between the rough sea surface

<!-- b000329 | prose | pages [12] -->
reflected power and the smooth sea surface reflected power. Using equations (17) and (18) we can easily derive equation 19

<!-- b000330 | prose | pages [12] -->
We can conclude that the ratio of the rough sea surface reflected power to the smooth sea surface reflected power is equal to the square of the roughness correction factor value.

<!-- b000331 | prose | pages [12] -->
We have calculated that the value of the incident wave power Pr is 0.43248mW, according to the formula (18) , we can get the smooth surface of the first reflected wave

<!-- b000332 | furniture | pages [13] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000333 | furniture | pages [13] -->
Team#76082

<!-- b000334 | furniture | pages [13] -->
Page 12 of 24

<!-- b000335 | prose | pages [13] -->
power P1= 0.4378mW. According to equation (19), we can calculate the first reflected wave power of rough sea surface P2 = 0.2832mW.

<!-- b000336 | prose | pages [13] -->
We conclude that the radio waves of the frequency 20MHz and the grazing angle 45 propagating under six winds, the first reflection intensity through the rough sea is 0.64689849 times the first reflection intensity of the smooth sea.

<!-- b000337 | prose | pages [13] -->
4.3Calculation of the maximum number of hops

<!-- b000338 | heading | pages [13] -->
4.3.1 Signal to noise ratio calculation of shortwave sky wave communication

<!-- b000339 | heading | pages [13] -->
The electric field strength of shortwave sky wave propagation

<!-- b000340 | prose | pages [13] -->
The field strength of the HF radio reception can be calculated using Equation 21[11]

<!-- b000341 | prose | pages [13] -->
Et137.2+20 lg f 10 lg P GtLb (21)

<!-- b000342 | prose | pages [13] -->
Where: Etis the signal strength of the receiving point in the skywave propagation, its unit is dB ( v / m ); P is the transmitter transmit power , its unit is kW; Gt is the transmitter antenna radiation gain, its unit is dB; Lbis the day-wave transmission loss.

<!-- b000343 | heading | pages [13] -->
Atmospheric noise field strength

<!-- b000344 | prose | pages [13] -->
The maritime shortwave communication under natural conditions is mainly disturbed by atmospheric noise. The industrial and cosmic interferences are relatively small and will not be considered here.

<!-- b000345 | prose | pages [13] -->
Atmospheric radio noise field strength RMS calculation formula[11]

<!-- b000346 | prose | pages [13] -->
EnFa +10 lg B 20 lg f 96.8

<!-- b000347 | prose | pages [13] -->
(22)

<!-- b000348 | prose | pages [13] -->
Enis the atmospheric radio noise field strength in dB;

<!-- b000349 | prose | pages [13] -->
Where:

<!-- b000350 | prose | pages [13] -->
Fa is the effective noise figure of the atmospheric radio in dB; B is the effective noise bandwidth of the receiver, we check the data to set its value to 6dB.

<!-- b000351 | prose | pages [13] -->
Shortwave sky wave signal to noise ratio  According to the formula 21 of signal-to-noise ratio of sky wave communication and formula 22 of rms value of atmospheric noise field, we can get the formula of SNR

<!-- b000352 | prose | pages [13] -->
SNRt 201.56 10 lg Pt20lg f 20lg r 10lg B LiYp Fa

<!-- b000353 | heading | pages [13] -->
4.3.2 Calculation results

<!-- b000354 | prose | pages [13] -->
(23)

<!-- b000355 | prose | pages [13] -->
The 100-watt high-frequency constant-carrier signal transmitted by the land-based source experienced a power of 0.2832mW after the first reflection at the turbulent ocean surface.

<!-- b000356 | prose | pages [13] -->
Because the threshold of signal available noise ratio (SNR) is 10 dB, SNRt10 dB . Using the previously set parameters and the resulting data, we calculate the maximum number of hops we get by 8 and the horizontal distance for each jump is 400 km.

<!-- b000357 | furniture | pages [14] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000358 | furniture | pages [14] -->
Team#76082

<!-- b000359 | furniture | pages [14] -->
Page 12 of 22

<!-- b000360 | prose | pages [14] -->
5.The comparison of Ground Signal Transmission and Sea

<!-- b000361 | prose | pages [14] -->
Signal Transmission

<!-- b000362 | heading | pages [14] -->
5.1 The mathematical model of ground signal reflection

<!-- b000363 | prose | pages [14] -->
We have learned from the above analysis that the loss of signal on different reflective surfaces is different. Next, we continue to discuss the comparison of the signals from different ground reflections. For ease of analysis, we classify the ground into smooth terrain and rough terrain.

<!-- b000364 | heading | pages [14] -->
5.1.1 Shortwave sky wave propagation loss in the smooth terrain

<!-- b000365 | prose | pages [14] -->
We assume that dry terrain is a smooth terrain that has the least surface obstructions compared to other terrain. We think that mainly on the smooth terrains produce ground

<!-- b000366 | prose | pages [14] -->
of dry

<!-- b000367 | prose | pages [14] -->
reflection loss. According to the data [12], we get the relative complex permittivity

<!-- b000368 | prose | pages [14] -->


<!-- b000369 | prose | pages [14] -->
earth equal to 4. According to the first question of Fresnel reflection coefficient formula and transmission loss formula, we can find a smooth terrain reflection loss of 9.1133dB.

<!-- b000370 | heading | pages [14] -->
5.1.2 Shortwave sky wave in mountainous terrain transmission loss

<!-- b000371 | prose | pages [14] -->
In addition to the reflection loss, shortwave sky wave in the mountainous terrain has the jungle mountain diffraction loss and sky wave through the jungle leaf loss in the transmission process [13]

<!-- b000372 | prose | pages [14] -->
The diffraction loss of shortwave sky wave through the jungle mountain In fact, the terrain of the jungle mountains is complex with many obstacles and it is difficult to accurately predict the diffraction loss of radio waves. In order to simplify the model, we study double-edged peak diffraction in this paper. According to literature[14], the Epstein-Peterson method using the equivalent method is an effective way to solve this problem. Figure 6 is a schematic of the Epstein-Peterson method.

<!-- b000373 | furniture | pages [15] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000374 | furniture | pages [15] -->
Team#76082

<!-- b000375 | furniture | pages [15] -->
Page 14 of 24

<!-- b000376 | caption | pages [15] -->
Figure6 Double-edged peak diffration

<!-- b000377 | prose | pages [15] -->
constitute a single-edged peak. We can use single-edged peak

<!-- b000378 | prose | pages [15] -->
a、b、hand b、c、h

<!-- b000379 | prose | pages [15] -->
1

<!-- b000380 | prose | pages [15] -->
2

<!-- b000381 | prose | pages [15] -->
diffraction loss formula respectively calculate the diffraction loss between L2

<!-- b000382 | prose | pages [15] -->
L 20lg(h 1

<!-- b000383 | prose | pages [15] -->
L 20lg(h 2

<!-- b000384 | prose | pages [15] -->
a、b、hdiffraction loss L1, and then find

<!-- b000385 | prose | pages [15] -->
1

<!-- b000386 | prose | pages [15] -->
2 ( 1 1

<!-- b000387 | prose | pages [15] -->
)) (24) 1 1

<!-- b000388 | prose | pages [15] -->
d1 d2

<!-- b000389 | prose | pages [15] -->
2 ( 1 1

<!-- b000390 | prose | pages [15] -->
)) (25) 2 2

<!-- b000391 | prose | pages [15] -->
d3 d4

<!-- b000392 | prose | pages [15] -->
The meaning of the parameters in the formula refer to Figure VI. After finding L1 and L2, a correction factor Lc needs to be added

<!-- b000393 | prose | pages [15] -->
L 10 lg[(a b)(b c)] c (26) b(a b c)

<!-- b000394 | prose | pages [15] -->
Then the total diffraction loss is calculated as Equation 27

<!-- b000395 | prose | pages [15] -->
La L1 L2 Lc

<!-- b000396 | prose | pages [15] -->
(27)

<!-- b000397 | prose | pages [15] -->
the loss of shortwave sky wave through the forest leaves

<!-- b000398 | prose | pages [15] -->
According to the literature[13], Ls is the loss of radio waves passing through the jungle leaves, which is expressed as

<!-- b000399 | prose | pages [15] -->
LS aLs (28)

<!-- b000400 | prose | pages [15] -->
Where: aLis the jungle attenuation coefficient (dB/m) and s is the thickness (m) of the electric wave passing through the bushes. The usual sky wave mode band (3 <f <30MHz), aLis 0.01-0.1dB/m.

<!-- b000401 | heading | pages [15] -->
5.2 Comparing results

<!-- b000402 | prose | pages [15] -->
hh60 m , a c 100 m , In order to compare the models, we take the parameters

<!-- b000403 | prose | pages [15] -->
1 2

<!-- b000404 | prose | pages [15] -->
aL0.8 . Substituting into the above formula, the maximum number of b=200m, s=10m, hops of a high-frequency radio wave transmitted on a smooth terrain is 3 and the maximum

<!-- b000405 | furniture | pages [16] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000406 | furniture | pages [16] -->
Team#76082

<!-- b000407 | furniture | pages [16] -->
Page 16 of 24

<!-- b000408 | prose | pages [16] -->
number of hops propagating in a mountainous area is two. At the same time, we can get smooth or rough sea and smooth or mountainous terrain wave reflection loss comparison chart, as shown in Figure 7

<!-- b000409 | caption | pages [16] -->
Figure 7 Loss comparison chart

<!-- b000410 | prose | pages [16] -->
Analyze the data, we get the following result: 1. The same radio transmission distance in the smooth ground is greater than the transmission distance in the mountainous terrain.

<!-- b000411 | prose | pages [16] -->
2. The same radio wave transmission loss in the smooth terrain is less than the transmission loss in the mountainous terrain.

<!-- b000412 | prose | pages [16] -->
3. The maximum number of hops transmitted by the same radio waves at sea is much larger than the maximum number of hops transmitted on land.

<!-- b000413 | prose | pages [16] -->
4. The same radio wave transmission loss in the sea is much smaller than the transmission loss of land.

<!-- b000414 | prose | pages [16] -->
As a result of the analysis, it is easy to obtain that the ocean surface is more suitable for the transmission of shortwave skywaves than land surfaces. This conclusion is consistent with experience.

<!-- b000415 | heading | pages [16] -->
6. The communication model of marine ship receiver

<!-- b000416 | prose | pages [16] -->
Due to the fluctuation of the sea, the ship swaying and causing the antenna to change to radio wave angle will affect the radio loss of the receiving end. We apply the method of adding the sloshing loss of the ship to the ocean signal reflection model to improve the signal propagation model at sea.

<!-- b000417 | prose | pages [16] -->
Under normal conditions, the shipborne antenna and the ship are relatively stationary. We assume that the movement of the ship is the movement of the shipborne antenna.

<!-- b000418 | heading | pages [16] -->
6.1 The model of ship rocks

<!-- b000419 | prose | pages [16] -->
There are many factors that affect sea surface fluctuation. In this paper, only the

<!-- b000420 | furniture | pages [17] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000421 | furniture | pages [17] -->
Team#76082

<!-- b000422 | furniture | pages [17] -->
Page 16 of 24

<!-- b000423 | prose | pages [17] -->
influence of wind-induced sea waves is considered.

<!-- b000424 | prose | pages [17] -->
There are three types of ship shaking, including floating up and down, left and right roll, pitch before and after. This abstracts the ship's six-degree-of-freedom motion model[15]. As shown in Figure 8, we create a spherical reference frame that is the center of the Earth.

<!-- b000425 | caption | pages [17] -->
Figure 8 Boat and antenna schematic

<!-- b000426 | prose | pages [17] -->
So the boat's movement can be expressed as: a. Altitude changes up and down the Z axis; b. Swaying around the X axis as the center of rotation; c. tilt around the Y axis as the center of rotation; Because there is no measured data of the movement of the vessel, we get the maximum value of the sway angle of the vessel max according to literature[15].

<!-- b000427 | prose | pages [17] -->
  Hmax arcsin  (29)

<!-- b000428 | prose | pages [17] -->


<!-- b000429 | prose | pages [17] -->
max  

<!-- b000430 | prose | pages [17] -->
2 2 2

<!-- b000431 | prose | pages [17] -->


<!-- b000432 | prose | pages [17] -->
sea H

<!-- b000433 | prose | pages [17] -->
 

<!-- b000434 | prose | pages [17] -->
max

<!-- b000435 | prose | pages [17] -->
Where: Hmax is the maximum height of the waves, sea is Wavelength of the waves.

<!-- b000436 | heading | pages [17] -->
6.2 Sea signal transmission model of combining ship swaying

<!-- b000437 | prose | pages [17] -->
Radio waves at sea environment propagation model shown in Figure 8[15].

<!-- b000438 | furniture | pages [18] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000439 | furniture | pages [18] -->
Page 17 of 24

<!-- b000440 | furniture | pages [18] -->
Team#76082

<!-- b000441 | caption | pages [18] -->
Figure 9 Radio waves environment propagation model

<!-- b000442 | prose | pages [18] -->
Radio waves at sea environment propagation model shown in Figure 8[15]. According to the receiving and dispatching end distance, the propagation distance is divided into three areas [15]:

<!-- b000443 | prose | pages [18] -->
Segment A: means from the transmitting antenna base station T to the base station visible point RA, the distance is d1 ;

<!-- b000444 | prose | pages [18] -->
Segment B: refers to the visual point from the base station RA

<!-- b000445 | prose | pages [18] -->
to the line of sight from

<!-- b000446 | prose | pages [18] -->
the visual point RB, the distance is d2 ;

<!-- b000447 | prose | pages [18] -->
Segment C: Refers to the shadow area of the earth beyond the visible range of line-of- sight RB, the distance is d3 .

<!-- b000448 | prose | pages [18] -->
In the segment A, a dual-path model considering ship sway is described, and in the segment B, a single-path model considering ship sway is described, ie a direct path is considered. The formula is

<!-- b000449 | prose | pages [18] -->
La 147.558220lg f 20lg CDP CRP

<!-- b000450 | prose | pages [18] -->
(30)

<!-- b000451 | prose | pages [18] -->
Lb147.5582 20 lg f 20 lg CDP

<!-- b000452 | prose | pages [18] -->
(31)

<!-- b000453 | prose | pages [18] -->
The data[13] shows that in section A, the up-and-down fluctuation has the greatest effect on sea surface propagation loss compared to the other two types of rocking. In section B, the influence of ship swaying on received power loss is negligible.

<!-- b000454 | prose | pages [18] -->
With the increase of transmitting and receiving distance, the impact of ship swaying on radio wave propagation loss is getting smaller and smaller. We assume that the signal will only float up and down when the signal is transmitted in section Aonly.

<!-- b000455 | prose | pages [18] -->
Through calculation, we get 1.5dB of ship sway loss in one sending and receiving process.

<!-- b000456 | furniture | pages [19] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000457 | furniture | pages [19] -->
Team#76082

<!-- b000458 | furniture | pages [19] -->
Page 18 of 24

<!-- b000459 | prose | pages [19] -->
6.3The same multi-hop path to maintain communication time

<!-- b000460 | prose | pages [19] -->
It is assumed that the ionosphere consists of many parallel thin sheets of very thin thickness with uniform electron density in each sheet. Assuming that the refractive index in air is 1, the corresponding refractive index of each parallel sheet is

<!-- b000461 | prose | pages [19] -->
n0 n1n2 n3 nn.

<!-- b000462 | prose | pages [19] -->
The frequency of the waves, with a certain angle of incidence by the air into the ionosphere, will occur continuous refraction. According to the refraction theorem, we get

<!-- b000463 | prose | pages [19] -->
n0sin0 n1 sin1 n2 sin2 n sinn (32)

<!-- b000464 | prose | pages [19] -->
The ability of the ionosphere to reflect radio waves is related to the frequency of the waves. At a certain angle of incidence, the lower the frequency of the radio wave, the easier it is to reflect. When a bunch of high frequency electromagnetic wave with the frequency of 3- 30MHz is injected into the ionosphere from the air at a certain angle of incidence, the waves of different frequencies will be reflected at different heights of the ionosphere. Its schematic diagram is shown in Figure 10.

<!-- b000465 | caption | pages [19] -->
Figure 10 Ionospheric reflection wave schematic

<!-- b000466 | prose | pages [19] -->
Due to the refraction, the higher frequency electric waves return to the sea after the ionosphere has been subjected to a horizontal gliding pass. Although the radio waves of different frequencies spread at different distances, the grazing angles incident on the sea surface are the same.

<!-- b000467 | prose | pages [19] -->
The locus of the wave propagation is Equation 33.

<!-- b000468 | prose | pages [19] -->
rdr

<!-- b000469 | prose | pages [19] -->
D=2

<!-- b000470 | prose | pages [19] -->
r

<!-- b000471 | prose | pages [19] -->
b

<!-- b000472 | prose | pages [19] -->
r2 cosdr

<!-- b000473 | prose | pages [19] -->
2

<!-- b000474 | prose | pages [19] -->
r

<!-- b000475 | prose | pages [19] -->
t (33)

<!-- b000476 | prose | pages [19] -->
0

<!-- b000477 | prose | pages [19] -->
rbr

<!-- b000478 | prose | pages [19] -->
r r cos  2 2

<!-- b000479 | prose | pages [19] -->
r0

<!-- b000480 | prose | pages [19] -->
0

<!-- b000481 | prose | pages [19] -->
Where: is initial incident elevation;

<!-- b000482 | prose | pages [19] -->
r n r cos  2 2 2 2 2 0

<!-- b000483 | prose | pages [19] -->
r0is earth radius (6370km); the subscript of r

<!-- b000484 | furniture | pages [20] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000485 | furniture | pages [20] -->
Page 19 of 24

<!-- b000486 | furniture | pages [20] -->
Team#76082

<!-- b000487 | prose | pages [20] -->
is ray fixed position. When HF waves return to the sea, a relatively uniform electromagnetic radiation field is formed between A and B. We call this area the signal coverage area. In this area, the ship's antenna can always be in communication. We get the longest communication time by calculating the maximum travel time of the ship in the signal coverage area.

<!-- b000488 | prose | pages [20] -->
The difference between the propagation distance of the highest-frequency electric wave and the propagation distance of the lowest-frequency electric wave is calculated by the formula 33. This difference is the maximum of the signal coverage area. We take the speed of the ship is 30kont, calculate the longest communication time is 15.12 hour. The total transmission distance is 840km.

<!-- b000489 | heading | pages [20] -->
7. Sensitivity Analysis-Time factor

<!-- b000490 | prose | pages [20] -->
Change the time, observe the influence of the changes of each changes on ionospheric loss. The sensitivity of time by calculation is obtained, as shown in the following figures.

<!-- b000491 | caption | pages [20] -->
Figure 11 Sensitivity of time (for signal-noise)

<!-- b000492 | furniture | pages [21] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000493 | furniture | pages [21] -->
Page 20 of 24

<!-- b000494 | furniture | pages [21] -->
Team#76082

<!-- b000495 | caption | pages [21] -->
Figure 12 Sensitivity of time (for ionospheric loss)

<!-- b000496 | prose | pages [21] -->
We can see that the grazing incidence is very sensitive to the parameters of time. It proves that the model we established is suitable for anytime.

<!-- b000497 | prose | pages [21] -->
On the other hand, the ionospheric loss is not very sensitive to the parameters of time. That is to say, the ionospheric loss cannot change too much.

<!-- b000498 | heading | pages [21] -->
8 Conclusions

<!-- b000499 | heading | pages [21] -->
8.1 Strengths

<!-- b000500 | prose | pages [21] -->
1. This model includes a large number of parameters. These parameters include the loss of radio transmission, the complex permittivity of the sea surface, and the rough correction factor and so on. they have great practical value and a wide range of application

<!-- b000501 | prose | pages [21] -->
2. The model is fit for the complex problem of HF waves on different surfaces of the loss and reflection. These fitting and approximation greatly reduce the difficulty of solving the model, and can get the results agree well with the real situation.

<!-- b000502 | prose | pages [21] -->
3. For the error analysis and sensitivity of the model, we discuss each parameter. Sensitivity analysis results show that our model parameters have a wide range of application.

<!-- b000503 | heading | pages [21] -->
8.2 Weaknesses

<!-- b000504 | prose | pages [21] -->
1. This model takes into account too much factors, causing the solving process is tedious.

<!-- b000505 | prose | pages [21] -->
2. The solution of the model is limited to the capacity of the computer, and it can't achieve higher accuracy。

<!-- b000506 | furniture | pages [22] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000507 | furniture | pages [22] -->
Page 21 of 24

<!-- b000508 | furniture | pages [22] -->
Team#76082

<!-- b000509 | prose | pages [22] -->
3. A large number of assumptions reduce the accuracy of the model’s calculation results.

<!-- b000510 | furniture | pages [23] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000511 | furniture | pages [23] -->
Team#76082

<!-- b000512 | furniture | pages [23] -->
Page 22 of 24

<!-- b000513 | prose | pages [23] -->
HF Radio Propagation under Different Terrains Summary We set up different models of HF radio propagation under different terrains.

<!-- b000514 | heading | pages [23] -->
Keywords Fresnel reflection coefficient equation, Sea signal reflection model,

<!-- b000515 | prose | pages [23] -->
Transmission loss

<!-- b000516 | heading | pages [23] -->
1 Introduction

<!-- b000517 | prose | pages [23] -->
Even in the satellite era, high-frequency （HF）signal communication still plays an important role in everyday communications. In order to clearly understand the communication process of HF waves and its influencing factors, we first design a mathematical model of signal reflection off the ocean. Based on this model, we build the ground signal reflection model and compare the two. Besides, we study the communication process of vessel receivers on a turbulent sea.

<!-- b000518 | heading | pages [23] -->
2 Model

<!-- b000519 | prose | pages [23] -->
We begin with the establishment of a mathematical model of signal reflection at sea from two aspects. On the one hand, due to the energy loss in the transmission of electric waves in the atmosphere, we study the basic loss of the HF sky wave transmission process. On the other hand, we investigate the surface properties of the sea. We classify the ocean surface as a smooth and a rough sea. Then, based on the Fresnel reflection coefficient for both sea types and the Phillips (1996) wave model, we obtain the reflection intensity of rough and smooth sea surface. And their ratio equals to the square of the roughness correction factor. Taking the high-frequency carrier signal with the power of 100 watts as an example, we select specific parameters and calculate the specific values.

<!-- b000520 | prose | pages [23] -->
The roughness correction factor is 0.8043, the first reflection power of rough sea surface is 0.4378mW, and the first reflection power of smooth sea surface is 0.2832mW. The ratio of the two is exactly equal to the square of the value of the roughness correction factor, which is consistent with the conclusion.

<!-- b000521 | prose | pages [23] -->
Using this model, we can easily simulate the multi-hop path of the signal. Taking the selected specific value as the parameter, we calculate the maximum number of hops to 8 times if the signal-noise ratio threshold is not exceeded.

<!-- b000522 | prose | pages [23] -->
Next, based on the above models, we set up the mathematical model of ground signal reflection. Depending on the surface characteristics of the ground, we simply divide the terrain into a smooth terrain and a mountainous terrain. The propagation loss of mountainous terrain is classified as diffraction loss of the mountain and absorption loss of the vegetation. We use Epstein-Peterson method to study the typical double-edged peak diffraction problem. In order to compare the two models, we still use the above-mentioned specific parameters to calculate the maximum number of hops and transmission loss of the same radio wave propagating on different ground. The results of the comparison are shown in Figure 7. We conclude that the ocean surface is more suitable for the transmission of shortwave skywaves than land surfaces, which is consistent with experience.

<!-- b000523 | prose | pages [23] -->
What’s more, we introduce the ship sway model to further establish the communication model of the ship receiver at sea. The ship can maintain communication while traveling in the signal coverage are. We get the longest communication time by calculating the maximum travel time of the ship in the signal coverage area.

<!-- b000524 | heading | pages [23] -->
3 Conclusion

<!-- b000525 | prose | pages [23] -->
We focus on the transmission process of shortwave skywaves off the ocean. The conclusion can help in the communications

<!-- b000526 | furniture | pages [24] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000527 | furniture | pages [24] -->
Page 23 of 24

<!-- b000528 | furniture | pages [24] -->
Team#76082

<!-- b000529 | prose | pages [24] -->
of maritime transport and fishing industries.

<!-- b000530 | furniture | pages [25] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000531 | furniture | pages [25] -->
Team#76082

<!-- b000532 | heading | pages [25] -->
References

<!-- b000533 | furniture | pages [25] -->
Page 24 of 24

<!-- b000534 | references | pages [25] -->
[1] Ren Z, Xu C, et al. Modeling and Simulation of SNR and SIR in HF Communication

<!-- b000535 | references | pages [25] -->
System [J]. Communication Countermeasures, 2010, 111(3): 29-33.

<!-- b000536 | references | pages [25] -->
[2] Zhao X.L, Huang J.Y, et al. Analysis of rader detection ability in evaporation duct

<!-- b000537 | references | pages [25] -->
environment [J]. Chinese Journal of Radio science, 2006, 21(6): 891-920.

<!-- b000538 | references | pages [25] -->
[3]Luo N, Wu W, et al. Simulation of Link Budget and Ionophere Characteristic [J]. Ship

<!-- b000539 | references | pages [25] -->
Electronic Engineering, 2007, 27(1): 132-134.

<!-- b000540 | references | pages [25] -->
[4]Jia J, Sheng W, Chen H. Simulation and Analysis of Path Propagation Loss for Sky

<!-- b000541 | references | pages [25] -->
Wave Over the Horizon Radar [J]. Morden Defence Technology, 2013, 41(3): 138-143.

<!-- b000542 | references | pages [25] -->
[5]Wang Y, Gu J. Research and Simulation Analysis of Radio Reflection Characteristic

<!-- b000543 | references | pages [25] -->
over the Ocean [J]. Electronic Design Engineering, 2016, 24(5): 113-119.

<!-- b000544 | references | pages [25] -->
[6] Jiang Z.H, Huang L.P, et al. One-cycle controller for parallel-connected interleaving

<!-- b000545 | references | pages [25] -->
critical continous conductionmode PFC converter[J]. Journal of TsingHua University,2007,

<!-- b000546 | references | pages [25] -->
47(7):1197-1200.

<!-- b000547 | references | pages [25] -->
[7] Lu B，Dong W，Zhao Q．Performance evaluation of Cool MOST Mand Si Cdiod e

<!-- b000548 | references | pages [25] -->
for single--phase power factor correction applieations[C].APEC’03，2003,2：65 1-657．

<!-- b000549 | references | pages [25] -->
[8] Miller A.R, Brown R.M, Vegh E. New derivation for the rough surface reflection

<!-- b000550 | references | pages [25] -->
coefficient and for the distribution of sea-wave elevations [C].IEEE Proc..1984:131,114-116.

<!-- b000551 | references | pages [25] -->
[9] Rui G.S, Guo Y, Tian W.B. Roughness Attenuation Factor in the Use of

<!-- b000552 | references | pages [25] -->
Electromagnetic Wave Propagation in Evaporation Duct Environment [J]. Journal of Naval

<!-- b000553 | references | pages [25] -->
Aeronautical and Astronautical University, 2012, 27(5): 545-548.

<!-- b000554 | references | pages [25] -->
[10] Huang F. Research on Characteristics of Maritime Wireless Radio Propagation and

<!-- b000555 | references | pages [25] -->
Channel Modeling [D]. Hai Nan, Hai Nan University, 2015: 24.

<!-- b000556 | references | pages [25] -->
propagation.

<!-- b000557 | references | pages [25] -->
[11]

<!-- b000558 | references | pages [25] -->
Xiong

<!-- b000559 | references | pages [25] -->
H.

<!-- b000560 | references | pages [25] -->
Radio

<!-- b000561 | references | pages [25] -->
wave

<!-- b000562 | references | pages [25] -->
Press,2000.2002:652-663

<!-- b000563 | references | pages [25] -->
Bei

<!-- b000564 | references | pages [25] -->
jing:

<!-- b000565 | references | pages [25] -->
Electronic

<!-- b000566 | references | pages [25] -->
Industry

<!-- b000567 | references | pages [25] -->
[12] Zhuang Q.P, Sui F.G. Influence on Different Forms of Ground on Shortwave

<!-- b000568 | references | pages [25] -->
Communication [J]. China New Telecommunications, 2014, 9: 92.

<!-- b000569 | references | pages [25] -->
[13] Jiang C.Y, Jiao P.N. Experimental Research of the Propagation Loss in the Forest

<!-- b000570 | references | pages [25] -->
Environment [J]. Journal of China Institute of Communications, 1992, 13(2): 73-78.

<!-- b000571 | references | pages [25] -->
[14] Cheng R.T. The Radio propagation model of ITU-R P.526 and diffraction of multi-

<!-- b000572 | references | pages [25] -->
edged peak [J]. The Window of Industry: 51-53.

<!-- b000573 | references | pages [25] -->
[15] Huang F. Research on Characteristics of Maritime Wireless Radio Propagation and

<!-- b000574 | references | pages [25] -->
Channel Modeling [D]. Hai Nan, Hai Nan University, 2015: 24.
