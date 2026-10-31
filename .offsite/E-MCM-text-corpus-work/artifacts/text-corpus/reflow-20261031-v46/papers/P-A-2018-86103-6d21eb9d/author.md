T1 F1 T2 F2 Problem Chosen T3 F3

T4 F4

MCM/ICM

Summary Sheet

Summary

HF radio propagation plays an extremely important role in communication at sea and mountains. It may be influenced by various factors, resulting in great loss of signal transmission. In this paper we focus on transmission and reflection loss of HF radio propagation in reflecting surface changes.

First, according to the PM wave spectrum and random wave theory, we establish a three-dimensional random wave model to simulate the motion of waves. On this ba- sis, we analyze the reflection of electromagnetic waves on the sea surface. We consider the influence of wave height caused by different wind levels on the reflection coefficient and obtain the reflection loss of electromagnetic wave under different conditions suc- cessfully. Then we get the sum of the lossin the transmission and the The first reflection intensity of the turbulent ocean and the calm one. At last we analyze the signal electric- field and atmospheric noise electric field of the receiving point, get the relation between SNR, transmission distance and hops, and the maximum number of hops should be 6 when SNR attenuates to 10dB.

Second, we analyze the transmission on the ground on the basis of the wave model. We simulate the topography with the wave fluctuation. Because the electromagnetic characteristics of the earth are different from the sea surface, we correct the relative di- electric constant and conductivity. Since there are more obstacles on the ground than on the sea, so we also analyze the diffraction phenomenon of electromagnetic wave prop- agation on the ground. We calculate and compare the first reflection intensity between mountainous or rugged terrain and smooth terrain. Surprisingly, the effectivedistance of sky-wave transmission is shorter than that of sea surface reflection. Under the same conditions, the maximum number of hops of HF radio propagation is4.

Finally, we consider the wind and waves that the ship may encounter on the sea sur- face, and calculate the longest distance that the received signal can propagate at a given wind level (i.e., SNR not less than 10 dB). Because ships usually travel longer, we also analyze the periodic variation of the ionosphere with time, and obtain the influence of the periodic variation of the ionosphere on the propagation of sky wave. On the basis of this, we get the optimal radio frequency under different conditions. After taking the ship speed into account, we amend the original model and obtain the maximum time for the ship to maintain the same multi-hop path.

Abstract

HF radio is widely used in long-distance propagation in a lot of countries because of its advantages of long propagation distance, low transmission loss and no external influence on the quality of propagation, especially maritime propagation. Because it is capable of reflections off the ionosphere and the earth, "jumping" to its destination. Besides, the characteristics of the reflected surface determine the intensity of the reflected waves and the extent to which the signal eventually travels. In this paper, we simulate different environments of the ocean and ground, and obtain the degree of signal loss and the propagation distance finally.

Ocean wave model

According to the wave spectrum and random wave theory, we take the actual wave as the superposition result of sinusoidal wave with different frequency, different propagation direction, different wave height and different initial phase. Then we establish the Longuet- Higgins long peak wave model. On this basis, we analyze the possible superposition of waves, and get the three-dimensional simulation diagram of the waves, and simulate it.

when the wind scale is 6 Transmission loss analysis In the process of transmission, SNR of the signal may be reduced due to various factors. For a fixed reception point, the loss of the signal is related to the angle of the signal emission, the transmission distance, the ionospheric absorption intensity, sea situation and so on. We have a simple classification of the loss of the signal: free space transmission loss, ionospheric absorption loss, additional loss and sea surface reflection loss.

Then, we lay special stress on the relationship between sea surface reflection loss and various factors. By simulating the reflection path, we study the relationship between reflection path and reflection coefficient, and draw the conclusion that when the hop count is 1, the relationship between the first reflection intensity and the wind scale is as follows:

and the first reflection intensity

In long-distance propagation, the number of multi-hop is often greater than 1 so that the wave can travel enough distance. But the integrity of the signal also attenuates gradually with the propagation. By calculation, we know that the maximum number of hops at calm sea is 6 when the power is 100 w and the frequency is 15 MHz.

Compare with the model on the ground

Based on the three-dimensional wave model, we simulate the relief of the terrain with the wave fluctuation. Considering diffraction may occur during the ground propagation, and the variation of the conductivity and relative dielectric constant caused by the complex ground. We modify the existing models, calculate the first reflection intensity and the maximum number of hops on different ground forms. Modification based on navigation

In the actual navigation, the receiving point is motional. Thus, it cannot be regarded as a fixed point and to be calculated. So we modify the model to calculate the emission angle, frequency, power and so on as variables. Based on these, we obtain the maximum distance and the time to maintain the same multi-hop path before the SNR attenuates to 10 dB. We also conclude that the absorption loss will increase due to the periodic variation of the ionosphere. So the launch frequency needs to be adjusted at different times.

7 Strengths and weaknesses

18 Strengths.................................................................................................................... 18 7.1 Weaknesses................................................................................................................18 7.2

Appendices

21

Appendix A First appendix

21

1 Introduction

1.1 Background

It is universally acknowledged that a ship sailing in the boundless sea will encounter a variety of danger at any time. With the increasing number of ships in the world and the trend toward large-scale and high-speed ocean shipping, the world’s waterways are becoming more and more crowded and crisis may occur at any time. In this case, HF radio propagation has played a significant role. HF radio propagation can attract us to transmitting messages, thats mainly because that HF communication can be achieved only by appropriate transmitting power and moderate equipment cost even far apart.

1.2 Restatement of the problem

As required by the question, we are supposed to determine the strength of the first re- flection off a turbulent ocean and compare it with the strength off a calm ocean. Mean- while, we will also determine the maximum number of hops the signal can take before its strength falls below a usable SNR. After that, we will compare the findings with hf reflections off different topography. Moreover, we are going to change our model to accommodate a shipboard receiver moving on a turbulent ocean.

There are two forms of shortwave propagation. One is ground wave, which consists of surface wave, direct wave and reflected wave; and another is sky wave that reaches the ground reception point being reflected by the ionospheric. In this article, we only model the reflection of sky waves.

2 Assumptions

• We consider the transmission of sky waves as the main way.

Reason: Energy is lost with the propagation of ground wave, and the higher the frequency(that is, the shorter the wave length), the greater the loss. However, sky-wave communication has the advantages of long propagation distance, low transmission loss and not being affected by the geological types of both sides. So we consider the transmission of sky waves as the main way.

• The reflection of sky-waves in the ionosphere is mainly considered in the F2 layer.

Reason: (1) It’s exist all day. (2) It’s height can accommodate the longest path. (3) MUF(maximum usable frequency) is the biggest.

• The main factor affecting wave height is wind speed.

• We regard the relative permittivity and conductivity of seawater as fixed values.

Reason: The changes of relative dielectric constant and conductivity are mainly caused by the change of salt content and temperature, and the wave and sea wa- ter motion have little effect on them, so we think that they are almost unchanged, and regard them as fixed values.

• We consider ships movement on the sea as a uniform motion.

3 Notation

Notation

Definition Lb Transmission loss Lbf Free space transmission loss La Ionospheric absorption loss Lg Ground reflection loss ε Electric medium constant σ Conductivity YP Additional loss r Propagation distance D Maximum propagation distance Elevation angle of transmission ∆ n Number of hops f Working frequency P0 Power of the transmitter P1 First reflection intensity R Reflection coefficient θ Incidence angle of electromagnetic wave

P.s. Other symbols instruction will be given in the text.

4 Radio propagation on sea surface model

4.1 Introduction to HF propagation

4.1.1 Way of HF propagation

HF propagation is the radio propagation of radio waves in the range of 3 to 30MHz(corre- sponding wave length 100 to 10m). HF communication has the advantages of long communication distance, strong persistence and simple equipment,meanwhile, it has the disadvantages of channel congestion, time-varying, dispersion characteristics, and so on. Moreover, it is easy to be influenced by other external factors and is unstable. HF propagation can propagate along the ground as the ground-wave, and it can also prop- agate through reflections off the ionospheric as the sky-wave. The propagation diagram is as follows:

4.1.2 Structure of ionosphere

Ionosphere is a ionization region of the earths atmosphere. It is ionized by highenergy radiation from the sun and cosmic rays. For the existence of a huge number of free electrons and ions, radio waves can change the speed of propagation ,and refraction, reflection and scattering occurred. The ionosphere can be divided into layer D, E, F [1]. The height of each layer and so on, and the layer F can be divided into F1 and F 2 changes over time, and some layers even disappear at night.

4.1.3 Best usable frequency

According to the theory of ionospheric propagation, shortwave with a higher frequency can only return to the ground from the reflection off ionosphere with a higher electron density distribution. There is a maximum frequency of radio waves that can be reflected back to the ground, which we call MUF(maximum usable frequency). the frequency of propagation should be as high as possible to reduce absorption, but generally only at the frequency of 0.85 MUF. Because if we use MUF, as long as the ionosphere changes slightly, the radio waves would go through the ionosphere without going back. So we [2]the best usablefrequency. call the frequency of 0.85 MUF

4.2 Wave model

4.2.1 Longuet - Higgins wave model

The wave phenomenon is very complex, and its speculative and nonlinear. Therefore, it is very difficult to establish an accurate wave model. According to the wave spectrum and random wave theory, we can regard the actual wave as the result of sinusoidal wave superposition with different frequency, different propagation directions, different wave [3] describes the waves heights and different initial phases. The Longuet-Higgins model of long-peak waves by the superposition of countless random cosine waves, and the amplitude is expressed as follows:

Where ξai refers to the amplitude of the i cosine wave, ωi refers to the frequency of the i cosine wave, and εi refers to the phase of the i cosine wave.

In practical applications, the Longuet-Higgins model is often expressed by the wave spectrum:

In the formula, Sζ ∆ωis the wave spectrum. At present, there are several widely used ocean spectrum,such as Pierson-Moscowitz spectrum(PM spectrum), Neumann spectrum(N spectrum), ITTC spectrum and so on, among which PM spectrum is the most widely used. It can well represent the fully developed random waves. Therefore, we use the PM spectrum. And the expression of PM spectrum is as follows:

Where v is the wind speed with a height of 19.5m above the sea level.

4.2.2 Three dimensional wave model

In the above model, we consider only one direction. But in the actual wave, the wave not only changes in height and frequency, but also spread in more than one direction. So we define the waves which are superimposed on each other and diffused randomly to ±π/2inthemainwaveasthreedimensionalirregularshortpeakrandomwavemodel.

We overlay the above model in many directions, and finally we get the following expression:

Where ζaij , ωi , ki , µj and εij are the amplitude, the angular frequency, the wave number, the direction angle and the random initial phase of the component harmonics, εij is random number between 0 and π/2, (ξ, η)is the coordinates of a certain point on a wave surface.

4.2.3 Model simulation

We simulated the model in MATLAB, and the results are as follows:

Transmission loss of HF radio waves Lb 4.3

During the transmission of radio waves, there are many factors that can affect the trans- mission loss. We divide the basic transmission loss(Lb) during the whole propagation process into four parts: free space transmission loss Lbf , ionospheric absorption loss La , ground reflection loss Lg, and additional loss YP . If all losses are expressed in deci- bel(dB), the basic transmission loss of sky-wave propagation is as follows:

(5) Lb = Lbf + Li + Lg + YP

4.3.1 Free space transmission loss Lbf

The free space transmission loss is the loss of energy caused by geometric factors after [4]: radio wave detaching antenna. The equality of Lbf is as follows

(6) Lbf = 32.44 + 20lgf + 20lgr

Where f is the working frequency in MHz and r is the effective path of HF radio propagation in km.

The curvature of the earth and the height of the ionosphere limit the one-time maxi- [5]: mum jump distance of the reflection off the ionosphericDmax

In the equation, ∆min is the minimum elevation angle of the antenna, and we know that the general elevation angle of the antenna is greater than 3◦. The Re is the radius of the earth, and we value it as 6371km. The h is the reflection virtual height of the ionosphere. The height of each layer is shown in the diagram. For F2 reflection, the maximum propagation distance Dmax is 4000km.

4.3.2 Ionospheric absorption lossLa

In HF radio propagation, the loss caused by ionospheric absorption mainly occurs in layer D, because there are more neutral molecules in layer D and the collision loss is [6]. The concentration of electrons in layer D decreases at night, and the absorption larger loss decreases. The loss is mainly non-offset absorption. The emission absorption in [7] . We ignore it in calculation for its layer 4 E or F mainly refers to offset absorption very small (≤1 dB).

Whereϕistheincidentangleataheightof100km,f(MHz)istheworkingfrequency and fH(MHz) is the gyromagnetic frequency,I is the absorption index and n is number of hops in the path.

The absorption index I is:

(9) I = (1 +0.037R)(cos 0.881χ)1.3

Where R is the number of sunspots and χ is the zenith angle of two 100 km high absorbs.

For the ionospheric absorption loss is related to transmitter, issue time and teh pa- rameters of receiving spots, and that the calculation is too complex, we take it as 4dB to make the calculation easy.

4.3.3 Sea surface reflection loss Lg

(1) Calm sea reflection For multi-hop sea surface reﬂection loss suppose incident wave is messy polariza-tionThe energy of the radio waves is evenly distributed on the horizontal and vertical polarizations, so that the formula for calculating the energy is

(10)

WhereRHandRVarethereﬂectioncoefﬁcientsofhorizontalandverticalpolarizedwaves, respectively, as follows:

Where θ is the incident angle, is the complex permittivity of the sea surface, ε is the permittivity of seawater, λ is the wavelength of the incident wave and σ is the con-ductivity. Accordingtothisformula,therelationshipbetweenRH，Rvandtheangleofincidence.

Accordingtothe ﬁgure,it isnotdifﬁcultto ﬁnd thatforthehorizontal polarized wave,the reﬂection coefﬁcientdecreases graduallyfrom 1, while the amplitude is verysmall.For the vertical polarized wave, with the reﬂection coefﬁcient increases with the increase of the incident angle,thereﬂectioncoefﬁcientincreasesto1gradually afterde-creasingrapidlyatﬁrst.The comparison shows that the change of reﬂection coefﬁcient of the horizontal polarization wave is much more sensitive to the incident angle.

(2) Ocean Wave Model algorithm for turbulentocean

Forthe three dimensionalirregular short-peak randomwave model mentioned above, we randomly select a wave cross section to analyze. When the electromagnetic wave shines on the wave, most of the available electromagnetic waves are emitted in the form of reflection and scattering, and reflection is the main one.

For the wave function ξ(x) of this cross section at a certain time, we take the deriva- tive of it and obtain the tangent equation of the section irradiated by electromagnetic wave.

(14) y = ξ′(x)(x −x0) + y0 Where (x0, y0) is the coordinate of surface element α. According to Sneel’s law, we assume that the grazing angle of electromagnetic wave incident to plane α is θ, and then we obtain the propagation path equation of reflected wave as shown below:

(15) y = tan(∆+ arctan ξ′(x))(x −x0) + y0

Because the water surface has a certain dip angle, the full incident wave cant be reflected in the positive direction. Therefore, we differentiate the wave surface, analyze each micro-element plane, and find out the total number of reflected waves reflected in the forward direction, and get the correction coefficient finally:

m (16) ρ = M

Where m is the total number of positive and negative reflection electromagnetic waves and M is the total number of incident electromagnetic waves.

As shown in the figure, the actual waves will have ups and downs. Especially when the wind and waves are high, some of the sea surface will be covered by the waves. At this point, we have corrected the occluded part, ignoring the reflected light in that part. The correction method is as follows:

We obtain the second derivative for wave function ξ(x) and obtain the tangent equa- tion of extreme value point corresponding to its extreme point. Then the second inter- section point of electromagnetic wave and wave is the intersection point of the equation and wave function, and the shading is the shaded area.

S −s ρ′ = ρ (17) ∗ S Where S is the surface area of a wave and s is the shaded area.

In the figure above, the left image shows the correction coefficients at different wind speeds when the grazing angle is 1◦/5◦/15◦, and the right image shows the correction coefficients at different wind speeds when the frequency is 10 MHz / 20 MHz / 30 MHz.

Wecan get the following curve, which is the final reflection coefficient bymultiply- ing it with the reflection coefficient when it is stationary:

Then we can get the loss of turbulent ocean:

(18) L′g = Lg −10 lg(ρ′)

4.3.4 Additional loss YP

Additional loss is the loss caused by other factors in addition to the main reasonsmen- tioned above. The detailed calculation is too complicated, but we conclude that it is [9]. mainly related to local time, which is assumed to be about 15 dB here

4.4 First reflection intensity

Combined with the loss analysis above, for a single jump signal source, we can get the following formula:

(19) 10lg(P1) = 10lg(P0) −Lbf −La −Lg −YP

Among them, P1(w) is the electromagnetic wave power of the transmitting point and P0(w) is the first reflection intensity. For the electromagnetic wave propagation route which has been determined in both time and space, only Lg is alterable because of the different sea conditions, we get the following chart bycalculation:

Parameter Reference value Unit dB 4 La 15 dB YP MHz 100 f w 100 P0 ◦ θ 3

As is shown in the figure, its the first reflection intensity of a signal with different frequencies under different wind speeds. We can get the curve of reflection intensity changing with sea condition by fitting. From the diagram, we can know that the first reflection intensity decreases with the increase of frequency and the increase of wind speed. Thus, we must consider the influence of weather in the process of maritime communication.

4.5 Calculation of SNR

[10]

4.5.1 HF sky-wave field intensity

The field strength of the receiving point can be calculated by the following formula:

(20) Et= 137.2 + 20 lg f + 10 lg P 0+ Gt−Lb

In the formula, Et(dB) is the signal intensity of the receiving point during the prop- agation of sky wave, f(MHz) is the working frequency, P(kw) is the power of the trans- mitter, tt(dB) is the normal gain of the transmitter antenna radiation, and Lb(dB) is the transmission loss of sky-wave.

4.5.2 Field intensity of atmospheric noise

[11] . It is the main noise source of ma- Atmospheric noise is mainly caused by lightning rine HF radio propagation at present. The formula for calculating the effective value of atmospheric noise field intensity is as follows:

(21) En = Fa + 10 lg B + 20 lg f−96.8

In the formula, En(dB) is the field intensity of atmospheric noise, Fa(dB) is the ef- fective noise coefficient of atmospheric radio, B(dB) is the effective noise bandwidth of receiver, F(MHz) is working frequency.

Atmospheric noise is usually estimated by the noise data provided in the CCIR322nd report. A complete set of atmospheric noise data contains 72 charts. The calculation pro- cess is very complicated and the accuracy is not high enough. Thus we use themethod of establishing a database to make a simple estimate. The following figure shows the [12]. atmospheric noise table at different times in a certain area in summer

4.5.3 Maximum number of hops

According to the formula for calculating the electric field intensity of HF sky-wave and the formula for calculating the effective value of atmospheric noise field intensity, we obtain the formula for calculating signal-to-noise ratio of shortwave sky-wave commu- nication under natural conditions.

(22) SNR = 201.56 + 10lgP0 −20lgf −20lgr −10lgB −La −Lg −YP −Fa

In the formula, after n jumps, we found that

(23) r = nDmax

(24) L′g = (n −1)× Lg (25) L′a = n × La With reference to the following table for each parameter, we can get n = 6 by using the fsolve function of MATLAB.

5 Comparison between sea surface model and ground surface

model

Because the ground environment is more complicated than the sea surface and is com- posed of various materials, we take the relative permittivity of 3 to 8 as the basic value and the geodetic equivalent conductivity as the electrical conductivity in the calculation.

By using the proposed model and the algorithm proposed above, we take the undu- lation of the mountain as the motion of the wave and calculate it approximately. Because there are many obstacles on the ground, the electromagnetic wave will be diffracted when it meets the obstacle. However, because the short wave wavelength is not enough to avoid obstacles, most of them will be blocked by various obstacles, so the propagation ability of short wave on the ground is very weak. According to the analysis,we substi- tute the electromagnetic parameters of ground into the formula and get the solutionas [13]: follows

The related parameters are shown in the table.

Variation Average Ground form ε(F/m) σ(S/m) ε(F/m) σ(S/m) Seawater 80 1∼4.3 80 4 10−3 Freshwater 80 10−3 ∼2.4×10−2 80 10−2 Wet soil 10∼30 3×10−3 ∼2.4 × 10−2 10 10−3 Dry soil 3∼4 1.1×10−5 ∼2 × 10−2 4

The first reflection intensity in hilly areas is as shown in the diagram, especially when the terrain is smooth, the relief degree is 0.

Wetake Lg as 6.53dB when the ground is flat and we get that n = 4. Compared with the sea surface, the propagation distance of the HF radio through the ground is much shorter than that of the sea surface.

6 Motion analysis of ships using HF radio propagation on tur-

bulent ocean

Maximum time(tmax) using the same multi-hop path 6.1

In the above model, we only consider the condition that the reception point is fixed. This model is applicable to the communication between two fixed points , or the case where the position change of the receiving point is negligible. The ship in the turbulent ocean has a long moving distance, so we can not only calculate the effective propaga- [14]. At this point, the propagation distance r is related tion distance r as a fixed value to the emission angle ∆, and La, Lg is related to n(the number of hops of sky-wave), meanwhile, Lg is also related to the emission angle ∆. To ensure that the received signal is clear enough, we conclude that the SNR should be greater than or equal to 10, that is:

SNR = 201.56+10 lg P 0 −20 lg f −20 lg r−10 lg B −nLa−(n−1)Lg −Yp−Fa ≥10 (24)

Through analysis, we know that since Lg is related to ∆, the longer the route distance is, the higher the power transmitter and the increase antenna are needed to assist the ship in the sea course. Or the radio frequency can be adjusted to avoid overattenuating to make the SNR too low and difficult to distinguish.

As shown in the figure, SNR of 100w signal is obtained at the receiving pointswith different frequencies and distances, with the number of hops n = 1 ∼6, the wind scale is 5, and the receiving points at different frequencies and distances.

Number of hops n Maximum propagation distance r(km) SNR(dB) 1 3225 54.0977 2 6449 23.2859 3 9674 16.9728 4 10125 10 5 <10125 10 6 <10125 10

We can know from the figure that when n is fixed, the propagation distance is insuf- ficient or the signal-to-noise ratio is too low with increasingdistance.

By analyzing the data above, we draw a conclusion that when the number of hops is too high, for the ship traveling on the turbulent sea surface, the signal reflects too many times between the sea surface and the ionosphere, and the loss of the propagation path is too large, which results in the decrease of the maximum propagation distance. It is not enough to spread the signal far enough. Therefore, in this case, we need to increase the transmission power or signal frequency to increase the signal-to-noise ratio and the maximum propagation distance.

In summary, the maximum time for ships to maintain multi-hop paths in turbulent ocean is :

r tmax = (27) v Where v is the speed of the ship moving at sea. In the case of the table above, the multi-hop path must be changed for every 3000km movement. In the case of 100W and 15MHz, the signal power and frequency must be increased when the transmission distance is over 10000 km.

6.2 Suggestions on frequency selection oftransmitter

Because not only the periodic variation of the ionosphere,but also the influence of the day and night, the season, the solar activity and so on can affect the value of the iono- spheric propagation loss La. In order for ships to have better communication at sea, the emitter must choose different frequency at different time to achieve better propagation. The following table shows the range of radio broadcasts commonly used to take into account ionospheric effects:

2∼4 MHz Tropical frequency, small number of sunspots and transmission is good.

Some countries near the equator can use it as domestic broadcasting 6∼7 MHz More suitable using in autumn and winter or night for close-range broa- dcasting 9∼11 MHz Moderate and suitable for all-day broadcasting both inside and outside 13 MHz Effect would be better at daytime and is suitable for long distance broa- dcasting 15∼17MHz Better in spring and summer

7 Strengths and weaknesses

7.1 Strengths

• Weclassify and analyze the propagation path, which makes our calculation more accurate.

• Wehave established a three-dimensional wave model, which is more intuitive.

• Weadopt the correction method of reflection coefficient, which is different from the previous empirical formula, and can analyze the reflection coefficient under different sea conditions quantitatively.

• Wetake the effects of periodic ionospheric variations into account, which are sensitive and can be used in various situations.

7.2 Weaknesses

• Weonly consider the HF sky-wave transmission model, but the ground-wave transmission also has certain influence.

• In real life, the ionospheric loss is complicated and varies greatly with latitude, longitude, seasons and so on. However, we only calculate the reasonable values according to the literature.

• We only focus on the characteristics of shortwave propagation at sea level and the effect of reflection without considering the effect of refractiondiffraction.

• The dielectric constant and conductivity of the reflected surface change with the frequency, but we only use the fixed value to calculate. When the salinity and temperature of seawater change sharply, the reliability of the data will decrease.

Appendices

Appendix A

First appendix

Here are simulation programmes we used in our model as follow.

%Wave situaion fengji=8; pinpushu=1000; jiaodushu=5;

wavewmin = [2.438306 1.462983 1.044989 0.812770 0.664988 0.562683 0.487659 0.430288]; wavewmax = [16.444115 9.866469 7.047480 5.481373 4.484760 3.794799 3.288826 2.90190]; wavewp=[4.053570 2.432142 1.737244 1.351190 1.105519 0.935439 0.810714 0.715336];

%----------------------------------------------------- u=[3,5,7,9,11,13,15,17]; %---------------------------------------------------

if fengji>8 fengji=8; end if fengji<1 fengji=1; end fi=fengji; wmin=wavewmin(fi); wmax=wavewmax(fi); wp=wavewp(fi); ui=u(fi); M=pinpushu; N=jiaodushu; wavewn=(wmax-wmin)/M; thetawn=pi/N; dx=1; dy=1; x=[0:dx:500]; y=[0:dy:300]; [x,y]=meshgrid(x,y); z=zeros(size(x)); for wi=1:M for ki=1:N theta=-pi/2+(ki-1)*thetawn; epsin=rand*2*pi; w=wmin+(wi-1)*wavewn+wavewn/2; swi=0.81*exp(-7400/(w*ui+eps).^4)*2*(cos(theta)).^2/(pi*(w.^5+eps)); an=sqrt(2*swi*wavewn*theta); z1=w*w*x*cos(theta)/9.8+w*w*y*sin(theta)/9.8+epsin; z=an*cos(z1)+z; end end surfl(x,y,abs(z)); shading flat; colormap ;

lightangle(-45,30); set(findobj(gca,’type’,’surface’),’FaceLighting’,’phong’,’AmbientStrength’,.3,’DiffuseStrength ’Sp ecularStrength’,.9,’SpecularExponent’,200) set(gca,’ztick’,[0,5]);

%Figure 5:calculate the relationship between Rh,Rv and incidence angle thetas=(0:1:90); theta=thetas./180.*pi; niu=10; lambda=1./niu; epsilon=80-1i.*60.*lambda.*50; RH1=sin(theta)-sqrt(epsilon-cos(theta).^2); RH2=sin(theta)+sqrt(epsilon-cos(theta).^2); RHh=abs(RH1./RH2); subplot(1,2,1); plot(thetas,RHh,’LineWidth’,1.5);axis([0 90 0.2 1]);hold; xlabel(’incident angle(a˛)’) ylabel(’reflection coefficient’) RH1=epsilon.*sin(theta)-sqrt(epsilon-cos(theta).^2); RH2=epsilon.*sin(theta)+sqrt(epsilon-cos(theta).^2); RHv=abs(RH1./RH2); subplot(1,2,2); plot(thetas,RHv,’LineWidth’,1.5);axis([0 90 0.2 1]);hold; xlabel(’incident angle(a˛)’) ylabel(’reflection coefficient’) niu=20; lambda=1./niu; epsilon=80-1i.*60.*lambda.*50; RH1=sin(theta)-sqrt(epsilon-cos(theta).^2); RH2=sin(theta)+sqrt(epsilon-cos(theta).^2); RHh=abs(RH1./RH2); subplot(1,2,1); plot(thetas,RHh,’r’,’LineWidth’,1.5);axis([0 90 0.2 1]);hold; set(get(gca,’YLabel’),’Fontsize’,12) set(get(gca,’XLabel’),’Fontsize’,12) RH1=epsilon.*sin(theta)-sqrt(epsilon-cos(theta).^2); RH2=epsilon.*sin(theta)+sqrt(epsilon-cos(theta).^2); RHv=abs(RH1./RH2); subplot(1,2,2); plot(thetas,RHv,’r’,’LineWidth’,1.5);axis([0 90 0.2 1]);hold; set(get(gca,’YLabel’),’Fontsize’,12) set(get(gca,’XLabel’),’Fontsize’,12)

%Figure 8:Diagrams of correction coefficients clc;clear; niu1=30*10^6;c=3*10^8;niu2=20*10^6;niu3=10*10^6; theta=1/180*pi; omega=[0:20]; h=0.0051.*omega.^2; g1=0.5*(4.*pi.*h.*niu1.*sin(theta)./c); g2=0.5*(4.*pi.*h.*niu2.*sin(theta)./c); g3=0.5*(4.*pi.*h.*niu3.*sin(theta)./c); rou1=1./(sqrt(3.2.*g1-2+sqrt((3.2.*g1).^2-7.*g1+9))); rou2=1./(sqrt(3.2.*g2-2+sqrt((3.2.*g2).^2-7.*g2+9))); rou3=1./(sqrt(3.2.*g3-2+sqrt((3.2.*g3).^2-7.*g3+9))); subplot(1,2,1); plot(omega,rou1,’r’,omega,rou2,’b’,omega,rou3,’g’,’LineWidth’,1.5);axis([0 20 0.97 1]);hold on legend(’10MHz’,’20MHz’,’30MHz’) xlabel(’wind speed(m/s)’) ylabel(’ correction coefficient’) set(get(gca,’YLabel’),’Fontsize’,12) set(get(gca,’XLabel’),’Fontsize’,12) niu=20*10^6; theta1=1/180*pi;c=3*10^8;theta2=5/180*pi;theta3=15/180*2; omega=[0:20]; h=0.0051.*omega.^2; g1=0.5*(4.*pi.*h.*niu.*sin(theta1)./c); g2=0.5*(4.*pi.*h.*niu.*sin(theta2)./c); g3=0.5*(4.*pi.*h.*niu.*sin(theta3)./c); rou1=1./(sqrt(3.2.*g1-2+sqrt((3.2.*g1).^2-7.*g1+9))); rou2=1./(sqrt(3.2.*g2-2+sqrt((3.2.*g2).^2-7.*g2+9))); rou3=1./(sqrt(3.2.*g3-2+sqrt((3.2.*g3).^2-7.*g3+9))); subplot(1,2,2); plot(omega,rou1,’r’,omega,rou2,’b’,omega,rou3,’g’,’LineWidth’,1.5);axis([0 20 0.84 1]); legend(’1a˛’,’5a˛’,’15a˛’) xlabel(’wind speed(m/s)’) ylabel(’ correction coefficient’) set(get(gca,’YLabel’),’Fontsize’,12) set(get(gca,’XLabel’),’Fontsize’,12)

%Figure9 Relation curve of reflection coefficient under different wind %speed clc;clear; theta=87/180.*pi; niu=(3:30); lambda=1./niu; epsilon=80-1i.*60.*lambda.*50; RH1=sin(theta)-sqrt(epsilon-cos(theta).^2); RH2=sin(theta)+sqrt(epsilon-cos(theta).^2); RHh=abs(RH1./RH2); RH1=epsilon.*sin(theta)-sqrt(epsilon-cos(theta).^2); RH2=epsilon.*sin(theta)+sqrt(epsilon-cos(theta).^2); RHv=abs(RH1./RH2); RH=(power(RHh,2)+power(RHv,2))/2; theta1=87/180*pi; c=3*10^8; nius=[3:30]; niu=nius.*10^6; h1=0;h2=1.5;h3=3,h4=4.5; g1=0.5*(4.*pi.*h1.*niu.*sin(theta1)./c); g2=0.5*(4.*pi.*h2.*niu.*sin(theta1)./c); g3=0.5*(4.*pi.*h3.*niu.*sin(theta1)./c); g4=0.5*(4.*pi.*h4.*niu.*sin(theta1)./c); rou1=1./(sqrt(3.2.*g1-2+sqrt((3.2.*g1).^2-7.*g1+9))); rou2=1./(sqrt(3.2.*g2-2+sqrt((3.2.*g2).^2-7.*g2+9))); rou3=1./(sqrt(3.2.*g3-2+sqrt((3.2.*g3).^2-7.*g3+9))); rou4=1./(sqrt(3.2.*g4-2+sqrt((3.2.*g4).^2-7.*g4+9))); RH_1=RH.*rou1;RH_2=RH.*rou2;RH_3=RH.*rou3;RH_4=RH.*rou4; plot(nius,RH_1,’r’,nius,RH_2,’b’,nius,RH_3,’g’,nius,RH_4,’y’,’LineWidth’,1.5); xlabel(’frequency(MHz)’) ylabel(’reflection coefficient’) set(get(gca,’YLabel’),’Fontsize’,12) set(get(gca,’XLabel’),’Fontsize’,12) legend(’calm’,’level 2’,’level 4’,’level 6’) %Figure11 Reflection coefficient relationship curves under different ground %conditions clc;clear; theta=87/180.*pi; niu=(3:30); lambda=1./niu; epsilon=80-1i.*60.*lambda.*50; epsilon=8; RH1=sin(theta)-sqrt(epsilon-cos(theta).^2); RH2=sin(theta)+sqrt(epsilon-cos(theta).^2); RHh=abs(RH1./RH2); RH1=epsilon.*sin(theta)-sqrt(epsilon-cos(theta).^2); RH2=epsilon.*sin(theta)+sqrt(epsilon-cos(theta).^2); RHv=abs(RH1./RH2); RH=(power(RHh,2)+power(RHv,2))/2; theta1=87/180*pi; c=3*10^8; nius=[3:30]; niu=nius.*10^6; h1=0;h2=1.5;h3=3,h4=4.5; g1=0.5*(4.*pi.*h1.*niu.*sin(theta1)./c); g2=0.5*(4.*pi.*h2.*niu.*sin(theta1)./c); g3=0.5*(4.*pi.*h3.*niu.*sin(theta1)./c); g4=0.5*(4.*pi.*h4.*niu.*sin(theta1)./c); rou1=1./(sqrt(3.2.*g1-2+sqrt((3.2.*g1).^2-7.*g1+9))); rou2=1./(sqrt(3.2.*g2-2+sqrt((3.2.*g2).^2-7.*g2+9))); rou3=1./(sqrt(3.2.*g3-2+sqrt((3.2.*g3).^2-7.*g3+9))); rou4=1./(sqrt(3.2.*g4-2+sqrt((3.2.*g4).^2-7.*g4+9))); RH_1=RH.*rou1;RH_2=RH.*rou2;RH_3=RH.*rou3;RH_4=RH.*rou4; subplot(1,2,1) plot(nius,RH_1,’r’,nius,RH_2,’b’,nius,RH_3,’g’,nius,RH_4,’y’,’LineWidth’,1.5); xlabel(’frequency(MHz)’) ylabel(’reflection coefficient’) set(get(gca,’YLabel’),’Fontsize’,12) set(get(gca,’XLabel’),’Fontsize’,12) RH_1=-10*log10(RH_1);RH_2=-10*log10(RH_2);RH_3=-10*log10(RH_3);RH_4=-10*log10(RH_4); subplot(1,2,2) plot(nius,RH_1,’r’,nius,RH_2,’b’,nius,RH_3,’g’,nius,RH_4,’y’,’LineWidth’,1.5); xlabel(’frequency(MHz)’) ylabel(’Sea surface reflection loss’);legend(’calm’,’hills’,’low mountains’,’middle mountains’ set(get(gca,’YLabel’),’Fontsize’,12) set(get(gca,’XLabel’),’Fontsize’,12)

%figure 13 relationship among distances frequency and SNR clear;clc;format ; P=100;B=3000*10^-6;Yp=15;La=4;Fa=80;f=[3:30]; r=[4000:1000:20000];R=6371;h=300;c=3*10^8;flow=3; n=1;thetas=(3:3:90);theta=thetas.*pi./180; D=2*R*(acos(R/(R+h)*cos(theta))-theta); lambda=1./f; epsilon=80-1i.*60.*lambda.*50; RH1=zeros(length(theta),length(epsilon)); RH2=zeros(length(theta),length(epsilon)); RHh=zeros(length(theta),length(epsilon)); RHv=zeros(length(theta),length(epsilon)); RH=zeros(length(theta),length(epsilon)); for i=1:length(theta) for j=1:length(f) RH1(i,j)=sin(theta(i))-sqrt(epsilon(j)-cos(theta(i))^2); RH2(i,j)=sin(theta(i))+sqrt(epsilon(j)-cos(theta(i))^2); RHh(i,j)=abs(RH1(i,j)/RH2(i,j)); RH1(i,j)=epsilon(j)*sin(theta(i))-sqrt(epsilon(j)-cos(theta(i))^2); RH2(i,j)=epsilon(j)*sin(theta(i))+sqrt(epsilon(j)-cos(theta(i))^2); RHh(i,j)=abs(RH1(i,j)/RH2(i,j)); RH(i,j)=(power(RHh(i,j),2)+power(RHv(i,j),2));%¡ˇn end end rou=zeros(length(theta),length(epsilon)); g=zeros(length(theta),length(epsilon)); niu=f.*10^6; for i=1:length(theta) for j=1:length(f) g(i,j)=0.5*(4.*pi.*flow.*niu(j).*sin(theta(i))./c); rou(i,j)=1./(sqrt(3.2.*g(i,j)-2+sqrt((3.2.*g(i,j)).^2-7.*g(i,j)+9))); end end RH=RH.*rou; Lg=-10*log10(RH); for n=1:6 for j=1:30 thetax=3*j; L(1,j)=n*D(1,j); for i=1:28 fs=i+2; SNR(j,i)=201.56+10*log10(P)-20*log10(fs)-20*log10(L(1,j))-10*log10(B)-n*La-(n-1)* if i==13 dis(n)=L(1,1) end end end mesh(f,L,SNR);hold on; max(n)=min(SNR(:,13)) end
