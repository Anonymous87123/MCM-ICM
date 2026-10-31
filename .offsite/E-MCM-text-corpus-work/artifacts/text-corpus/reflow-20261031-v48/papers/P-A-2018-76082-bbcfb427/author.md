For office use only For office use only T1 F1 T2 F2 T3 F3 Problem Chosen

F4 T4

2018 MCM/ICM Summary Sheet.

Summary

Even in the satellite era, high-frequency (HF) signal communication still plays an important role in everyday communications. In order to clearly understand the communication process of HF waves and its influencing factors, we first design a mathematical model of signal reflection off the ocean. Based on this model, we build the ground signal reflection model and compare the two. Besides, we study the communication process of vessel receivers on a turbulent sea.

We begin with the establishment of a mathematical model of signal reflection at sea from two aspects. On the one hand, we study the basic loss of the HF sky wave transmission process. On the other hand, we investigate the surface properties of the sea. We classify the ocean surface as a smooth and a rough sea. Based on the Fresnel reflection coefficient equation, we obtain the reflection intensity of rough and smooth sea surface. And their ratio equals to the square of the roughness correction factor. We select specific parameters for getting the specific value. Then we get the first reflection power of rough sea surface is 0.4378mW, and the first reflection power of smooth sea surface is 0.2832mW. The first reflection power of rough sea surface is 0.6469 times smooth sea surface. As a result, using this model, we can easily simulate the multi- hop path of the signal. Taking the selected specific value as the parameter, we calculate the maximum number of hops to 8 times if the signal-noise ratio threshold is not exceeded.

Next, based on the above models, we set up the mathematical model of ground signal reflection. Similarly, we classify the terrain as a smooth terrain and a mountainous terrain. The propagation loss of mountainous terrain is classified as diffraction loss of the mountain and absorption loss of the vegetation. We use Epstein-Peterson method to study the typical double- edged peak diffraction problem. Through comparison of the two models, we conclude that the ocean surface is more suitable for the transmission of shortwave skywaves than land surfaces.

What’s more, we introduce the ship sway model to further establish the communication model of the ship receiver at sea. The ship can maintain communication while traveling in the signal coverage. We get the longest communication time by calculating the maximum travel time of the ship in the signal coverage area.

Finally, we prepare a synopsis of the results that are suitable as a short note in IEEE Communications Magazine.

We focus on the transmission process of shortwave skywaves off the ocean. The conclusion can help in the communications of maritime transport and fishing industries.

loss

2. Assumptions

Calm sea is equivalent to a smooth sea, so calm sea is the reflection of radio waves is specular reflection. The object of our study is the high frequency band of 3-30 MHz. If the wave frequency exceeds MUF, the electric wave will enter the space through the ionosphere and the ionosphere will change frequently. Therefore, the best available frequency is usually 0.8 -0.9 times, we conservatively assume that the best available f 20MHz . frequency is When the wavelength and the wave height are comparable or even far less than the wave height, the influence of the shadow effect on the radio wave propagation needs to be considered. However, this dissertation is not applicable. Therefore, the influence of the shadow effect on the radio wave propagation is ignored. Assume that the directional factor of the emission and reception antennas is 1. Suppose the emitted electromagnetic wave is a circularly polarized wave. Assume that multipath interference is ignored

3. Skywave basic transmission loss

3.1 Loss model

In order to clearly describe the spread of the electric wave, we give the figure 1 about a simple representation of its jumping process:

A radio wave emitted by the terrestrial source first reaches the ionosphere and reaches the sea level through the reflection of the ionosphere. It is its first hopping process. After being reflected by the sea, it returns to the ionosphere and returns to the sea for the second jump and so on.

We know that, in practice, radio waves produce loss of energy when transmitting. According to the reason of transmission loss, the basic transmission loss of skywave is expressed as[1] Lb LbfLiLg Yp (1) Where: Lbfis the transmission loss in free space; Li is the ionospheric absorption loss; Lg is reflection loss on the ground; Yp is the additional system loss. We mainly discuss the ionospheric absorption loss and space transmission loss. Basic transmission loss in free space Lbf The basic transmission loss in free space is the energy loss. the geometric diffusion causes energy loss after the radio wave leaves the transmitting antenna. The formula is [2]:

Lbf 32.4420lg f 20lgr (2) Where: The unit of Lbf is dB; f is the working frequency, the unit is MHz; r is effective path for the propagation of radio waves, the unit is km.

Ionospheric absorption loss Li In the ionosphere, there is a region of significant ionization in the atmosphere. In accordance with the electronic density changes with height, the ionosphere can be divided into D layer, E layer, F1 layer and F2 layer. The F layer is the reflective layer, because it is highest and allows the radio waves to travel the furthest distance[3]. Therefore, we consider the high-frequency signals mainly reflect on the F1 layer (150km-200km) in this paper.

Since the degree of ionospheric absorption relates to many factors, it is difficult to make theoretical calculations. So we choose semi-empirical formula[3-4]:

677.2I seci100 L (3)  ( f f )1.98 10.2 bf H

I (10.0037R)(cos(0.881))1.3 (4)

i100 arcsin(0.985 cos ) (5) Where: fH is the frequency of the magnetic swing at a height of 100 km; I is the absorption coefficient, and represents the relationship of the ionospheric absorption and solar zenith angle and sunspots R ; i100 is the 100km-height of the incident angle, is the ray elevation.

Under certain circumstances, these parameters can access data to get a specific value.

Extra system loss Yp The extra system loss is the sum of the losses calculated for other reasons, and accurate calculation is difficult. Since the additional system loss is basically a function of the local time[1], we can estimate the additional system loss by looking at the data sheet.

Reflection loss on the ground Lg Ground loss occurs from the radio wave through the ground reflection. In this model, the electric wave is reflected on the sea surface, so we do not consider the ground reflection loss.

3.2 Calculation Results Analysis

In order to make the calculation easily, we choose the typical numerical value to simulate.

The parameters we choose are as follows:

Ray elevation =, Ionospheric height h 200 km ,so it is easy to obtain the ffective path of radio wave propagation r 200 2 km .Reflection point (123E, 26N ) is located in the East China Sea；fH = 1.24MHz; time point is 12:00 on July 1, check the number of sunspots R 110.

The sun zenith angle can be calculated by the following formula[4]:

cos sin asin Sx cosacos Sx cos Sx 23.44 sin[0.9856(Yn 80.7)] (6) 18015(24 t 8) 0 t 8 Sy  180 15(t8) 8 t 24  Where: Sx is the sun’s point of latitude, Sy is the sun’s point of longitude, Yn is the number of days from January 1 each year; t is Beijing time, a is the study point’s latitude;  is the difference between study point’s longitude and Sy . After simulation we get the transmission loss Lf is 97.4597dB.

We learn from the formula L 10lg Pr (7) b Pt Calculate the power Pt of a high-frequency constant carrier signal transmitted by a terrestrial source is 100W, incident power Pr reaching the sea surface after transmission loss is 0.43248mW.

4.The Mathematical Model of Ocean signal’s Reflection

4.1Basic model

The reflection coefficient of sea waves mainly represents the reflection characteristics of sea waves on the surface of the sea. The reflection coefficient is related to the incident angle of the sea waves, the size of the waves, the electromagnetic parameters of the sea surface and other factors.

Before studying the reflection characteristics, we first study the electromagnetic properties of the sea surface. The electromagnetic characteristics of sea surface affect the sea surface reflection intensity of radio waves, and it is related to the seawater temperature, salinity, electromagnetic wave frequency and other factors. The complex permittivity of the sea is a parameter describing the electromagnetic properties of the sea surface.

4.1.1 Sea surface’s plural dielectric constant

The plural dielectric constant of sea surface is determined by the relative dielectric constant of seawater r, sea water conductivity and the wave length , the expression is [1]:

 (8) =r i60 We can calculate constants r and ratiobased on the polynomial fit function given by Consultants Committee of the International Radio (CCIR).

Relative dielectric constant of the sea water  The expression of sea water’s relative dielectric constant is[5] 70  f 2253.5895   1   r f 2253.5895   2 3 4 a bf cf df ef    

Where:

f is the radio frequency, and its units is MHz; a 1.4114535102 ；b 5.2122497 108 ；c 5.8547829 1011 d 7.67174231016 ；e 2.98563181021 Conductivity of the Sea water The expression of sea water’s conductivity is[5]

0.5  f 1106.207   (10) 2 r sf tf     f 1106.207   2 3 1 uf uf wf   

Where:

f is the radio frequency, its units is MHz;

r 3.8586749 ；s 9.1253873104 ；t 1.5309921108 u 2.1179295105 ；v 6.5727504 1010 ；w 1.9647664 1015 is 20MHz, we can get seawater relative permittivity r= 70; f Because we assume sea water conductivity 5.0; Sea surface dielectric constant  70 4500i 。

4.1.2 Fresnel reflection coefficient of Sea

Fresnel reflection coefficient of smooth sea According to snell's law, the Fresnel reflection coefficient of horizontal and vertical polarized waves on a smooth sea surface is[5]

 cos2 sin (11) RH  cos2 sin

  cos2 sin (12) RV   sin cos2 Where:is grazing angle of incidence.

The curve in Figure 2 reflects the relationship between the power reflection coefficient and the grazing incidence angle .

The grazing incidence angle is 4590 by observing, the change of the power reflection coefficient is not obvious. For convenience of calculation, we set the grazing incidence angle as 45.

Fresnel reflection coefficient of rough sea We can easily get a smooth sea reflection coefficient, in fact, the sea is choppy, so we continue to study the reflection coefficient of the rough sea. Wave phenomenon is random and non-linear, so it is difficult to establish an accurate model of waves. According to the wave spectrum and the theory of stochastic ocean waves, we can regard the actual ocean waves as the result of the superposition of sine waves of different frequencies, different initial phases, different directions of propagation, and different wave heights..

In the raging sea, wave height, shape, and frequency change rapidly and wave propagation direction may change. To simplify the model, we only consider the effect of frequency and wave height on the roughness of the sea surface.

At present, Pierson-Moscowitz spectrum (Neutron spectrum), NTC spectrum (ITTC) and two-parameter ITTC spectrum are the most widely used marine spectra. Among them, PM spectrum is the most widely used, so we use PM spectrum to describe the frequency of ocean waves. The expression of PM spectrum is 8.1103 g 2 g 4 exp[0.74( ) ] (13) S(i)  5  v Where: v is the average wind speed near the height of the sea surface.

Figure 4 Wave spectrum From figure 4 we conclude that wind speed is a major factor affecting the frequency of waves.

Next we study the influence of wave height on the reflection coefficient. According to Phillips (1996) wave model as follows[6-7]:

(14) h 0.0051v2 Where: h is the root mean square height of the sea surface, v is the wind speed near the height of the sea surface.

It is obvious that the high wind speed near the sea surface directly affects the root mean square of the sea surface. Therefore, we believe wind speed is a common major factor affecting frequency and wave height.

It is obvious that the high wind speed near the sea surface directly affects the root mean square of the sea surface. Therefore, we believe wind speed is a common major factor affecting frequency and wave height.

Then we can get rough correction factor expression based on Miller-Brown rough surface approximation model[8-9]

exp[2(2g)2 ]I [2(2g)2 ] (15) 0 Where: I0 is the first kind of modified Bessel function of order 0; g is the sea surface roughness which is used to describe the magnitude of sea surface The formula is g h sin/ 。 fluctuations.

correction factor decreases rapidly with increasing wind speed.

Because communication at sea is a communication distance, the influence of earth curvature on the correction factor can not be ignored. D represents the Earth's curvature factor, which is calculation formula 16 [10]

1    2 G G 2   1 D   1 2 (16)   sin R G G     1 2 e

Where, G1 is the distance from the RF transmitting end to the specular reflection point,

and is the distance from the specular reflection point to the RF receiving end, which is the radius of the earth (the effective earth radius is 6400km).

Therefore, the rough correction factor for earth curvature is taken into account D .

We use the roughness correction factor to approximate the Fresnel reflection coefficient of the horizontal and vertical polarized waves of a rough sea surface

' R R   H H (17) ' R R   V V

Depending on the relationship of the wavelength and frequency c v . When we can 20MHz , wave length get the frequency f 15m . In this case, the wavelength is comparable to the height of the waves, as a result, shadowing may occur, in this article, to simplify the model, we assume no impact.

In order to meet the computing needs, we take six wind speed v 15m / s ,then h 1.1475 .Because45, We can get according to formula (15) The value of is 0.8043.

4.2Comparison of Reflection Intensity between Rough Sea and

Smooth Sea

In order to facilitate the study, we replace the intensity with the power, so the power ratio is equal to the ratio of the intensity.

We set P1 as outgoing radio wave power for smooth sea surface. Based on the concept of circularly polarized waves can be the formula

Where: RH is Fresnel reflection coefficient of horizontal polarized wave on a smooth sea surface; RV is the Fresnel reflection coefficient of a vertically polarized wave on a smooth sea surface.

Again, we set P2 as Rough surface of the outgoing radio power.

We can get

When the electric waves emitted by the terrestrial sources are reflected for the first time, the incident electric wave power is the same both in the rough sea and in the smooth sea, so the sea surface reflection coefficient determines the difference between the rough sea surface reflected power and the smooth sea surface reflected power.

Using equations (17) and (18) we can easily derive equation 19

We can conclude that the ratio of the rough sea surface reflected power to the smooth sea surface reflected power is equal to the square of the roughness correction factor value.

We have calculated that the value of the incident wave power Pr is 0.43248mW, according to the formula (18) , we can get the smooth surface of the first reflected wave power P1= 0.4378mW. According to equation (19), we can calculate the first reflected wave power of rough sea surface P2 = 0.2832mW.

We conclude that the radio waves of the frequency 20MHz and the grazing angle 45 propagating under six winds, the first reflection intensity through the rough sea is 0.64689849 times the first reflection intensity of the smooth sea.

4.3Calculation of the maximum number of hops

4.3.1 Signal to noise ratio calculation of shortwave sky wave communication

The electric field strength of shortwave sky wave propagation

The field strength of the HF radio reception can be calculated using Equation 21[11] Et137.2+20 lg f 10 lg P GtLb (21) Where: Etis the signal strength of the receiving point in the skywave propagation, its unit is dB ( v / m ); P is the transmitter transmit power , its unit is kW; Gt is the transmitter antenna radiation gain, its unit is dB; Lbis the day-wave transmission loss.

Atmospheric noise field strength

The maritime shortwave communication under natural conditions is mainly disturbed by atmospheric noise. The industrial and cosmic interferences are relatively small and will not be considered here.

Atmospheric radio noise field strength RMS calculation formula[11] EnFa +10 lg B 20 lg f 96.8 (22) Enis the atmospheric radio noise field strength in dB; Fa is the effective Where: noise figure of the atmospheric radio in dB; B is the effective noise bandwidth of the receiver, we check the data to set its value to 6dB.

Shortwave sky wave signal to noise ratio  According to the formula 21 of signal-to-noise ratio of sky wave communication and formula 22 of rms value of atmospheric noise field, we can get the formula of SNR SNRt 201.56 10 lg Pt20lg f 20lg r 10lg B LiYp Fa (23)

4.3.2 Calculation results

The 100-watt high-frequency constant-carrier signal transmitted by the land-based source experienced a power of 0.2832mW after the first reflection at the turbulent ocean surface.

Because the threshold of signal available noise ratio (SNR) is 10 dB, SNRt10 dB .

Using the previously set parameters and the resulting data, we calculate the maximum number of hops we get by 8 and the horizontal distance for each jump is 400 km.

5.The comparison of Ground Signal Transmission and Sea

Signal Transmission

5.1 The mathematical model of ground signal reflection

We have learned from the above analysis that the loss of signal on different reflective surfaces is different. Next, we continue to discuss the comparison of the signals from different ground reflections. For ease of analysis, we classify the ground into smooth terrain and rough terrain.

5.1.1 Shortwave sky wave propagation loss in the smooth terrain

We assume that dry terrain is a smooth terrain that has the least surface obstructions compared to other terrain. We think that mainly on the smooth terrains produce ground of dry reflection loss. According to the data [12], we get the relative complex permittivity  earth equal to 4. According to the first question of Fresnel reflection coefficient formula and transmission loss formula, we can find a smooth terrain reflection loss of 9.1133dB.

5.1.2 Shortwave sky wave in mountainous terrain transmission loss

In addition to the reflection loss, shortwave sky wave in the mountainous terrain has the jungle mountain diffraction loss and sky wave through the jungle leaf loss in the transmission process [13] The diffraction loss of shortwave sky wave through the jungle mountain In fact, the terrain of the jungle mountains is complex with many obstacles and it is difficult to accurately predict the diffraction loss of radio waves. In order to simplify the model, we study double-edged peak diffraction in this paper. According to literature[14], the Epstein-Peterson method using the equivalent method is an effective way to solve this problem. Figure 6 is a schematic of the Epstein-Peterson method.

a、b、hand b、c、h constitute a single-edged peak. We can use single-edged peak 1 2 a、b、hdiffraction loss L1, and then find diffraction loss formula respectively calculate 1 the diffraction loss between L2 2 ( 1 1 L 20lg(h )) (24) 1 1 d1 d2

2 ( 1 1 L 20lg(h )) (25) 2 2 d3 d4 The meaning of the parameters in the formula refer to Figure VI.

After finding L1 and L2, a correction factor Lc needs to be added L 10 lg[(a b)(b c)] (26) c b(a b c)

Then the total diffraction loss is calculated as Equation 27 La L1 L2 Lc (27) the loss of shortwave sky wave through the forest leaves According to the literature[13], Ls is the loss of radio waves passing through the jungle leaves, which is expressed as LS aLs (28) Where: aLis the jungle attenuation coefficient (dB/m) and s is the thickness (m) of the electric wave passing through the bushes. The usual sky wave mode band (3 <f <30MHz), aLis 0.01-0.1dB/m.

5.2 Comparing results

hh60 m , a c 100 m , In order to compare the models, we take the parameters 1 2 aL0.8 . Substituting into the above formula, the maximum number of b=200m, s=10m, hops of a high-frequency radio wave transmitted on a smooth terrain is 3 and the maximum number of hops propagating in a mountainous area is two.

At the same time, we can get smooth or rough sea and smooth or mountainous terrain wave reflection loss comparison chart, as shown in Figure 7

Analyze the data, we get the following result:

1. The same radio transmission distance in the smooth ground is greater than the transmission distance in the mountainous terrain.

2. The same radio wave transmission loss in the smooth terrain is less than the transmission loss in the mountainous terrain.

3. The maximum number of hops transmitted by the same radio waves at sea is much larger than the maximum number of hops transmitted on land.

4. The same radio wave transmission loss in the sea is much smaller than the transmission loss of land.

As a result of the analysis, it is easy to obtain that the ocean surface is more suitable for the transmission of shortwave skywaves than land surfaces. This conclusion is consistent with experience.

6. The communication model of marine ship receiver

Due to the fluctuation of the sea, the ship swaying and causing the antenna to change to radio wave angle will affect the radio loss of the receiving end. We apply the method of adding the sloshing loss of the ship to the ocean signal reflection model to improve the signal propagation model at sea.

Under normal conditions, the shipborne antenna and the ship are relatively stationary. We assume that the movement of the ship is the movement of the shipborne antenna.

6.1 The model of ship rocks

There are many factors that affect sea surface fluctuation. In this paper, only the influence of wind-induced sea waves is considered.

There are three types of ship shaking, including floating up and down, left and right roll, pitch before and after. This abstracts the ship's six-degree-of-freedom motion model[15]. As shown in Figure 8, we create a spherical reference frame that is the center of the Earth.

So the boat's movement can be expressed as:

a. Altitude changes up and down the Z axis;

b. Swaying around the X axis as the center of rotation;

c. tilt around the Y axis as the center of rotation;

Because there is no measured data of the movement of the vessel, we get the maximum value of the sway angle of the vessel max according to literature[15].

  Hmax arcsin  (29)  max   2 2 2  sea H   max Where: Hmax is the maximum height of the waves, sea is Wavelength of the waves.

6.2 Sea signal transmission model of combining ship swaying

Radio waves at sea environment propagation model shown in Figure 8[15].

Radio waves at sea environment propagation model shown in Figure 8[15].

According to the receiving and dispatching end distance, the propagation distance is divided into three areas [15]:

Segment A: means from the transmitting antenna base station T to the base station visible point RA, the distance is d1 ; Segment B: refers to the visual point from the base station RA to the line of sight from the visual point RB, the distance is d2 ;

Segment C: Refers to the shadow area of the earth beyond the visible range of line-of- sight RB, the distance is d3 .

In the segment A, a dual-path model considering ship sway is described, and in the segment B, a single-path model considering ship sway is described, ie a direct path is considered. The formula is La 147.558220lg f 20lg CDP CRP (30)

Lb147.5582 20 lg f 20 lg CDP (31) The data[13] shows that in section A, the up-and-down fluctuation has the greatest effect on sea surface propagation loss compared to the other two types of rocking. In section B, the influence of ship swaying on received power loss is negligible.

With the increase of transmitting and receiving distance, the impact of ship swaying on radio wave propagation loss is getting smaller and smaller. We assume that the signal will only float up and down when the signal is transmitted in section Aonly.

Through calculation, we get 1.5dB of ship sway loss in one sending and receiving process.

6.3The same multi-hop path to maintain communication time

It is assumed that the ionosphere consists of many parallel thin sheets of very thin thickness with uniform electron density in each sheet. Assuming that the refractive index in air is 1, the corresponding refractive index of each parallel sheet is n0 n1n2 n3 nn.

The frequency of the waves, with a certain angle of incidence by the air into the ionosphere, will occur continuous refraction. According to the refraction theorem, we get n0sin0 n1 sin1 n2 sin2 n sinn (32)

The ability of the ionosphere to reflect radio waves is related to the frequency of the waves. At a certain angle of incidence, the lower the frequency of the radio wave, the easier it is to reflect. When a bunch of high frequency electromagnetic wave with the frequency of 3- 30MHz is injected into the ionosphere from the air at a certain angle of incidence, the waves of different frequencies will be reflected at different heights of the ionosphere. Its schematic diagram is shown in Figure 10.

Due to the refraction, the higher frequency electric waves return to the sea after the ionosphere has been subjected to a horizontal gliding pass. Although the radio waves of different frequencies spread at different distances, the grazing angles incident on the sea surface are the same.

The locus of the wave propagation is Equation 33.

r2 cosdr rdr D=2 2 r r b t (33) 0 rbr r r cos  r n r cos  2 2 2 2 2 2 2 r0 0 0 Where: is initial incident elevation; r0is earth radius (6370km); the subscript of r is ray fixed position.

When HF waves return to the sea, a relatively uniform electromagnetic radiation field is formed between A and B. We call this area the signal coverage area. In this area, the ship's antenna can always be in communication. We get the longest communication time by calculating the maximum travel time of the ship in the signal coverage area.

The difference between the propagation distance of the highest-frequency electric wave and the propagation distance of the lowest-frequency electric wave is calculated by the formula 33. This difference is the maximum of the signal coverage area. We take the speed of the ship is 30kont, calculate the longest communication time is 15.12 hour. The total transmission distance is 840km.

7. Sensitivity Analysis-Time factor

Change the time, observe the influence of the changes of each changes on ionospheric loss. The sensitivity of time by calculation is obtained, as shown in the following figures.

We can see that the grazing incidence is very sensitive to the parameters of time. It proves that the model we established is suitable for anytime.

On the other hand, the ionospheric loss is not very sensitive to the parameters of time. That is to say, the ionospheric loss cannot change too much.

8 Conclusions

8.1 Strengths

1. This model includes a large number of parameters. These parameters include the loss of radio transmission, the complex permittivity of the sea surface, and the rough correction factor and so on. they have great practical value and a wide range of application 2. The model is fit for the complex problem of HF waves on different surfaces of the loss and reflection. These fitting and approximation greatly reduce the difficulty of solving the model, and can get the results agree well with the real situation.

3. For the error analysis and sensitivity of the model, we discuss each parameter. Sensitivity analysis results show that our model parameters have a wide range of application.

8.2 Weaknesses

1. This model takes into account too much factors, causing the solving process is tedious.

2. The solution of the model is limited to the capacity of the computer, and it can't achieve higher accuracy。 3. A large number of assumptions reduce the accuracy of the model’s calculation results.

HF Radio Propagation under Different Terrains Summary We set up different models of HF radio propagation under different terrains.

Keywords Fresnel reflection coefficient equation, Sea signal reflection model,

Transmission loss

1 Introduction

Even in the satellite era, high-frequency （HF）signal communication still plays an important role in everyday communications. In order to clearly understand the communication process of HF waves and its influencing factors, we first design a mathematical model of signal reflection off the ocean. Based on this model, we build the ground signal reflection model and compare the two. Besides, we study the communication process of vessel receivers on a turbulent sea.

2 Model

We begin with the establishment of a mathematical model of signal reflection at sea from two aspects. On the one hand, due to the energy loss in the transmission of electric waves in the atmosphere, we study the basic loss of the HF sky wave transmission process. On the other hand, we investigate the surface properties of the sea. We classify the ocean surface as a smooth and a rough sea. Then, based on the Fresnel reflection coefficient for both sea types and the Phillips (1996) wave model, we obtain the reflection intensity of rough and smooth sea surface. And their ratio equals to the square of the roughness correction factor. Taking the high-frequency carrier signal with the power of 100 watts as an example, we select specific parameters and calculate the specific values. The roughness correction factor is 0.8043, the first reflection power of rough sea surface is 0.4378mW, and the first reflection power of smooth sea surface is 0.2832mW. The ratio of the two is exactly equal to the square of the value of the roughness correction factor, which is consistent with the conclusion. Using this model, we can easily simulate the multi-hop path of the signal. Taking the selected specific value as the parameter, we calculate the maximum number of hops to 8 times if the signal-noise ratio threshold is not exceeded.

Next, based on the above models, we set up the mathematical model of ground signal reflection. Depending on the surface characteristics of the ground, we simply divide the terrain into a smooth terrain and a mountainous terrain. The propagation loss of mountainous terrain is classified as diffraction loss of the mountain and absorption loss of the vegetation. We use Epstein-Peterson method to study the typical double-edged peak diffraction problem. In order to compare the two models, we still use the above-mentioned specific parameters to calculate the maximum number of hops and transmission loss of the same radio wave propagating on different ground. The results of the comparison are shown in Figure 7. We conclude that the ocean surface is more suitable for the transmission of shortwave skywaves than land surfaces, which is consistent with experience.

What’s more, we introduce the ship sway model to further establish the communication model of the ship receiver at sea. The ship can maintain communication while traveling in the signal coverage are. We get the longest communication time by calculating the maximum travel time of the ship in the signal coverage area.

3 Conclusion

We focus on the transmission process of shortwave skywaves off the ocean. The conclusion can help in the communications of maritime transport and fishing industries.
