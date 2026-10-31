T1 F1 T2 F2 Problem Chosen T3 F3

F4 T4

.

The discovery of High Frequency skywaves in the 1920’s allowed amateur radio enthusiasts, even those with low powered transmitters, to connect over long distances. Now in common use, skywaves allow communication across the turbulent ocean to ships at sea or distant continents by bouncing waves between the ionosphere and the surface of the Earth. We create a model to tackle the challenge of reliable communication, simulating the unpredictability of skywave communication, including uneven ionosphere density and wild reflection off of non-uniform surfaces.

In our model, a transmitter at an initial latitude and longitude on a spherical Earth beams a HF signal with a bearing and elevation angle. We use NASA’s International Reference Ionosphere data set to determine the curved  trajectory resulting from refraction of the signal in the ionosphere. We generate small patches of terrain using either a wave simulator or geological elevation  data, which give the signal a new heading as it bounces. This multi-step process allows our model to create the complete path of a skywave signal.

Next, we can calculate how the atmosphere and terrain interfere with skywaves, or prevent them from reflecting at all. We model signal strength using the dominant sources of signal gain and loss, and stop propagation when the signal falls below the 10 dB minimum. The transmitter power, receiver sensitivity, and antenna gain provide 170 dB of margin.  The signal weakens along its trajectory because of the free space path loss.  The signal attenuates due to ionospheric absorption and diffuse surface reflection. 

We run high-throughput simulations of skywave paths that bounce on calm and turbulent water, as well as smooth and mountainous land. We randomly vary transmitter locations, and test paths from coastal cities to determine the maximum effective transmission distance. To explore our model’s sensitivity, we alter the wave conditions from calm to super-turbulent, increase the transmission power, and change ionospheric density. Lastly, we co-vary the frequency and elevation angle, which we determine to be the most sensitive parameters.

We inspect the average number of hops, distance travelled over the Earth, and power lost after bounces to compare our results. For our default frequency and angle of 3 MHz and 30 degrees, respectively, we find a maximum of two hops. The power after a first bounce is 0.72 dB less for turbulent seas compared to calm, and 0.26 dB less for mountainous land compared to smooth. The signals over turbulent ocean reach 1622 km from the shore. We find that depending on location, angle, and frequency, many signals pass through the ionosphere completely or are absorbed before they can bounce. Mapping bounce locations over ionospheric density, we find thatskywave propagation is most effective on the “greyline” between night and day, when absorption is lessened but the ionosphere can still reflect signals.

I. Introduction

Innovators since the dawn of humankind havesought a more interconnected society by enhancing our ability to communicate over long distances. The history of telecommunica- tion began in 1800 BC, where Chinese soldiers used smoke signals to warn their comrades 1 In 1876, Alexander Graham Bell achieved the first up to 500 miles away of an attack. 1 While the telephone was a vast improvement over other technologies at telephone call. the time, it required an enormous infrastructure investment and could only be usedwith static stations. A few decades later, the invention of the radio allowed mobile vehicles to communicate over vast distances. In 1914, the International Convention for the Safety of 2 Long-distance Life at Sea required shipboard radio stations to be manned 24 hours a day. communicationviaHFradiowavesremainsthemoststablemeansofcommunicationonthe 3 If a vessel is not within line-of-sight of a coastal radio station, the open ocean to this day. coastal radio station uses skywave propagation to reflect radio waves off of the ionosphere 4 As the radio wave skips between the surface and the ionosphere, it al- and back to Earth. lows the station to communicate beyond the horizon. Despite the unpredictability of radio over long distances, rugged terrain, and volatile seas, it remains an integral component of communication technologies that allow mankind to stay connected.

A. Problem Summary

• HighFrequency(HF) radio waves,from 3-30MHz, can“hop”between the ionosphere and the surface of the Earth, travelling a greater distance than they could along the ground. When sufficient signal strength is maintained (>10 dB), this enables long distance communication.

• If the signal reflects off the ocean surface, it may be affected by changing electrical and magnetic properties of the waves,as well as size, shape, frequency, and direction.

• If the signal reflects off the land, it may be affected by terrain variations.

• Followingthelossofamulti-hopsignalnecessitatesthemodelingofthetransmitter, propagation between bounces, interaction with the ionosphere, interaction with the Earth’s surface, and ftnally the receiver.

B. Our Starting Point: Existing Models

Studies of skywave communication have been performed both empirically and theoret- ically by radio operators and electrical engineers in the decades since its creation. These existing models have been refined over time by our increasing understanding of complex physical phenomenon, improved measuring tools, and the capabilities of modern comput- ers.

Before developing our own model, we explored the literature to gain a thorough under- standing of existing models, and which complexities they consider. A few arehighlighted here:

• Analyticaland geometricmodelsareeasytoimplementbutmakesimplificationsthat degrade accuracy. Examplesinclude:

– Assuming that the Earth and ionosphere are flat – Treating radio waves as single or double rays – Formula-based surfaces for terrain

• Numerical models can achieve high accuracy and take into account dynamiccondi- tions, but they require large data sets and computational power. Examples include:

– Using real ionospheric conditions as a function of time – Statistical fading of signals during propagation – Real terrain from geological or oceanic data sources

C. Our Model

Our modeling approach is rooted in our conclusion that while this prompt focuses on surface hops, a full model of the signal propagation is necessary. The losses in the ionosphere, for instance, directly determine the remaining signal strength for hops. Thus, our model will focus on implementing complexity where detail is most necessary, and simplicity where detail is not necessary, as determined by our research. Wehope to obtain anaccuratetrajectorythroughtheionosphere,aswellasaccurateinteractions with terrain, but simplify free space propagation.

The complexity of the propagation of radio waves requires us to evaluate the trade-offs betweenrealismandcomputationtime. Thisimpactsourterrainandionospheremodeling, the types of loss weconsider during propagation, and radio hardware. In the following sec- tions, we will determine which terrain and ionosphere models to use by considering those 5 Wewill determine a propagation model that with availabledata and sufficient resolution. includes losses with a significant magnitude compared to the complexity of the necessary calculations. Finally, we will choose general details about our transmitter, receiver and the system antennae in order to determine our signal strength. By programming different sce- narios into the model to link bounces together, we can track the results for the complete path of each signal.

II. Background

A. Transmitter and Receiver

The ending of each signal’s path can be determined by the point that the remaining signal power falls below the 10 decibel threshold. This threshold is called the “link margin,” and is the minimum power required to have a reliable connection. 6

The 100 W transmit power can be converted to decibels with the equation:

dBm = 10log10(P ∗1000/1) = 50 (1) The decibel is a relative calculation, which in this case is taken as a ratio of power to one milliwatt. In decibel form, the power P , positive antenna gain tt, and negative loss L can be added. The combination of these factors is known as the link budget, and willtell 6 us the received power.

PRx = PT x + ttT x + L + ttRx (2) Comparing this result to the receiver sensitivity yields the link margin. Because the characteristics of the receiver and the receiving antenna are part of the equation, we will treat the end of the signal path as the theoretical location where the receiver can no longer detect the signal, meaning the budget does not meet the required link margin.

Wedeterminethe antenna gainand receiver sensitivityfrom sources about radioequip-

6 We will use the

ment. A common range of receiver sensitivity is -90 to -120 dBm. highest sensitivity of -120 dBm, because we do not have any requirements for thebit error rate of the system, or how successfully it sends data.

A simple type of antenna is a 1.25 wavelength dipole, which has a gain of 5.03 dBi. 7 This is relative to an isotropic radiator, which radiates equally in all directions. The gain is due to the antenna signal being focused in certain directions, instead of equal. While the physical length might make it impractical to use, mathematically it represents a basic antennacase. Wewillusethesamefigureforboththetransmittingandreceivingantennas.

Lastly, the loss will be determined from the propagation of the radio waves. Once all these parameters are calculated, we can determine how far the signal can travel.

B. Radio Propagation and Loss

Even without any bounces, the received signal power will be less than the transmitted power. This is due to the spreading of the signal as it propagates through space. Instead of travellinginatightbeam,thewavefrontexpandsoutward,losingpower. Thisphenomenon is called free space loss, and increases with distance. 8

The free space loss only includes the effects of distance, and not any obstacles or interference the signal might encounter. During propagation, the signal also experiences 9 Molecules in loss from absorption in the atmosphere, multipath fading, and shadowing. the atmosphere, like water vapor or gaseous oxygen, can attenuate the signal as it passes through. When the signal interacts with objects, it can split into different paths that arrive atdifferenttimeswithdifferentphases,causinginterference. Thisiscalledshadowingwhen it occurs with large objects, and fading when it occurs with small ones.

C. Skywave Channel Interaction

Skywave radio follows a “channel” as it bounces between the ionosphere and the Earth. Both types of interactions can introduce losses.

1. Ionosphere interaction

In the ionosphere, radiation from the sun breaks down molecules into ions and elec- trons. These charged particles form layers. The varying electron density causes the index of refraction to decrease with altitude, bending the signals as they travel. The different layers absorb and refract the signal, until it is attenuated, reflected, or passes 10 The charged particles in the ionosphere vary with the sunlight, through into space.

changing between day and nighttime, different seasons, and periods of high and low so- 11 The ionosphere also interacts magnetically with radio waves, due to their lar activity.

5 electromagnetic nature, but this influence is often neglected in models.

In relation to skywaves, the changing layers of the ionosphere cause signals to behave 10 During the day, the D-layer from 60 to 90 differently over time, even hour to hour. km is generated by Lyman radiation and x-rays. This region contributes the most to absorption loss of the signals, especially those with lower frequency, and can prevent them from penetrating further. At night, however, the D region dissipates, leaving the reflective E and F regions from 100 to 400 km. At higher altitudes, the lower density gas takes longer for ions and electrons to recombine, allowing these regions to persist when the sun is not illuminating them. The signals can travel higher without being attenuated, and become refracted more and more, until they reach the point where they arereflected back. The balance between absorption and reflection means that the day/night terminator is an excellent location for skywaves to propagate. The height of the layer that the signals reach determines how far they can hop, with a 2500 km maximum for the E-layer and a 5000km maximumforthe F-layer. Duetothesignificant roleofthe ionosphereinskywave communication, we plan to incorporate its variations with height and location, although 10 to do so in time would be too computationally expensive.

2. Surface interaction

On the surface of the Earth, the signal can be reflected, diffracted, or scattered de- 9 The ground or water can impact the polarity of the signal, and pending on the terrain. multipath interference is common as signals interact with the ground and with each other. For modeling purposes, the terrain can be mathematically constructed surfaces, or actual 12 geographical data, which is only available for land models.

Diffraction mostly occurs on “knife edge” surfaces or around the edges of objects like 5 The buildings, so reflection and scattering are the most dominant for terrain reflection. surface of the Earth has a complex reflectivity coefficient, which depends on the conduc- tivity and permittivity of the medium, and effects the amplitude of the resulting signal due to phase interference. Depending on the roughness of the surface, the reflection will be specular, having a coherent main signal, or diffuse, and spread out in all directions. The comparison of the specular component versus scattering determines the signal loss due to reflection.

D. Performance Evaluation

At the completion of the signal’s path, we need to determine how it behaved. We first need to find the number of hops, which can simply be calculated bycounting the number of surface interactions before the signal is lost. We will also calculate the arc length across the Earth’s surface, which tells us the overall distance the signal travelled.

While it is beneficial to know how many hops were accomplished, we would also like to predict where the signal ends up on the globe. Using the distances and the directions that the signals are reflected, we can determine the latitude and longitude of the final bounces. The density of the signals on the Earth allows us to determine which locations are likely to receive a strong skywave signal.

III. Assumptions

A.

Model Assumptions

• The signal is not attenuated by rain, fog, and interactions with molecules in the lower 8 atmosphere. These losses are only significant for frequencies above 1 GHz.

• Ground interference is not a significant because the signal is high above theEarth’s surface for most of its path and the interference from the ground is viewed as a 5 minimal impairment until reflection.

• The signal is not polarized and the frequency remains the same during travel. These 5 factors are not as useful for long-distance radio models compared to free space loss.

• The ionosphere reaches from 80 km to 2000 km as a spherical shell above a spherical 13 The signal only begins to Earth for increased accuracy compared to flat models.

be refracted from bottom of the ionosphere.

• The ionosphere follows the Reference Standard Ionosphere data from NASA at a 13 given epoch, so the global data provides information about both night and day.

• When modeling the behavior of a radio wave bouncing off of water or land, every bounce will occur on that specified terrain. The coordinates that we use are only to determine the ionosphere data location and the distance travelled on the Earth.

• The ocean surface is stationary compared to the speed of light. The signal reflects off of fixed wave shapes.

• A calm ocean has wave heights of less than 1 m, while a rough ocean can have swells from 1 to 10 m. A super-turbulent ocean can have a peak swell of 15 m, based on 14 National Weather Service wave forecasts for a fully-developed sea.

• The land consists of topographical features without anysurface coverings, to simplify computations.

• A flat land surface is entirely smooth, while a mountainous region may have sharp altitude deviations in the tens of meters.

1 wavelength antennae with

• The transmitting and receiving antennae are dipole 1 4 6 The receiver has a sensitivity of -120 dBm. 6 gains of 5.03 dBi each.

• The velocities of the transmitting and receiving antennas, if in motion, are negligible compared to the speed of light.

• All the signal loss occurs between the two antennae, with no loss due to cabling, filters, or other noise at the transmitter and receiver. These values are usuallysmall 6 compared to path loss, and require defining precise equipment to determine.

• The communications link only needs to be complete in one direction, meaning that the transmitting station only transmits, and the receiving station only receives. We do not need to determine how successfully information is transmitted, only if the 4 connection is made.

Nomenclature

∆A Amplitude change factor ∆h Standard deviation of surface height [m] Initial angle of signal projection [rad] ∆ A Path length from starting point to bottom of the ionosphere[km] Permittivity of free space [8.8541 ∗10−12F ∗m s0 1] i Local incidence unit vector nˆ Local normal unit vector rˆ Local reflection unit vector λ Signal wavelength[m] µ(z) The refractive index at a given altitude ω Angular wave frequency [rad/s] φ0 The angle of incidence at pointPin[rad] ψ Phase [rad] ρ Complex reflectivitycoefficient Θj The angle swept out from the waveentering the ionosphere to its peak altitude [rad] θi Incidence angle between ray and surface [rad] ˙r Total reflection unit vector B Total path length [m] brg Initial bearing of a signal[rad] c Velocity of light [2.99792x10 8m/s] Charge on the electron [−1.602 ∗10−19C] e f Frequency of the signal wave [hertz] tt Antenna gain [dBi] h0 Distance from surface of the Earth to the lowestpoint of the ionosphere [80km] hr Distance from surfa√ce of the Earth to the highest point the ray reaches [km] Complex variable [ −1] j k Non-deviative absorption loss [dB] L Loss [dB] m Mass of the electron [9.109 10 31kg] ∗ N Electron density [ electrons] m3 P Power [W ] Pin/Pout The points of entry/exit into/leaving the ionosphere R Radius of the Earth [km] S Path length the ionosphere[km] v Electron-neutral collision frequency [Hz] z Distance between the ray and the surface of the Earth at any given point in its trajectory [km]

IV. Model Development

A.

Model Construction

The model is constructed in order to accurately create the path of the bouncing signal. This path provides the loss due to free space and ionospheric absorption, which are determined per distance. The ground model determines the loss from the terrain interaction as well as the new incidence angle for propagation of the next bounce.

1. Propagation and Ionosphere Interaction

The first portion of the model consists of the signal travelling from the ground to the ionosphere, refracting, and travelling from the ionosphere back to the ground. Over this entire section, we determine the path above and below the ionosphere separately. The 515 below equations are derived from several sources.

The equations in this section are based on a curved radio wave trajectory, as shown in our diagram, Figure 1.

Thedistancefrom thetransmittertothe ionosphereis determined fromthe law of sines using the equation

5 therefore By Snell’s law, the angle of incidence is equal to the angle of reflection, the length of the transmitter-ionosphere path is the same as the length of the ionosphere- receiver path.

Once the wave enters the ionosphere, it begins on a trajectory towards point Pproj. Due to the variability of the refractive index between the first 80 km of Earth’s atmosphere and the ionosphere, the ray begins to bend along path S until it reaches the reflection point, at which it bends back towards the Earth’s surface. We calculate the length of path S with the equation

The above equations convert from polar coordinates to a Cartesian grid with the origin on the earth’s surface directly below the radio wave’s virtual maximum. The value of Θj 5 is found with

We modeled the electron density of the ionosphere using values provided by a NASA 13 Our model has a sample for every 10° latitude by 20° longitude by 10km database. section of the ionosphere. These values are taken from January 1, 2001 at 1:30 AM GMT to provide a consistent dataset with both day and night regions, but it does not include variation in the ionosphere from season, solar cycle, and other factors. For computational speed, intermediate electron density is found with linear interpolation. See Figure 5 in the Appendix for an example of a trajectory calculated by our model. This trajectorymatches 2. Ground Interaction

When the radio wave comes in contact with the earth, we employ a different model to predict its new direction and loss. This model is generalized to allow for different types of land and water terrains.

For fixed terrain such as land masses, geological survey data exists that we can use to createrealisticshapes. TheUnitedStatesGeologicalSurveywebsitecontainsdownloadable data sets for elevation, such as the Space Shuttle Radar Topography Mission data that 12 We arbitrarily select one such data set, covers the globe with one arcsecond resolution. containing hills and gullies from the border of Guinea and Mali in western Africa.

For unfixed terrain such as water, no permanent data sets exist. Because we only need to capture the motion of the water at a fixed moment in time, we decide to generate instantaneous wave shapes. Such simulations are plentiful in MATLAB, and we adapt 17 This simulation models random waves of one provided by StackExchange user “Hoki”. set height based on wind patterns, using the Phillips spectrum of wave amplitude for a fully-developed sea. Figure 2 (and Figure 7 in the Appendix) are examples of turbulent and calm random waves, respectively.

We create the terrain for each type of surface as follows:

• Smooth land: We generate a perfectly flat 10 by 10 meter surface in MATLAB, representing a plains environment.

• Mountainous land: Our model randomly selects a 50 by 50 point subsection of the Guinea/Mali data set to provide the terrain shape. The size is scaled down to a 10 by 10 meter square, with smoothed elevation changes of 10 meters or less. This terrain can very from gentle slopes to steep mountainsides, but does not include cliffs.

• Calm seas: Wegenerate a 10 by 10 meter square of gentle waves, with amplitude less than one meter.

• Rough seas: We provide a crosswind to generate large swells, with amplitude from 1 to 10 meters for rough ocean and up to 15 meters for super-turbulent.

The size of each patch is determined by our need for a small mesh in order to reduce computation time, which means the area must also be small in order to preserve detail.

The next step is to determine the signal loss experienced on each type of terrain, using 5 We quantify the roughness of equations for reflection and scattering on rough surfaces. a surface using the standard deviation of the height ∆h over the entire mesh surface. We can then apply the Rayleigh roughness criterion to approximate how much the signal will reflect or scatter. The change in phase caused by the height difference, as different rays take different length paths, can be calculated using incidence angle θi and wavelength λ:

∆ψ = 4π∆hsin(θi)/λ (16) Thedifferent phases causemultipathinterferenceinthewave,which reduces the am- plitude of the coherent specularly reflected component. This amplitudereduction 5 can be calculated:

∆A = exp (−∆ψ 2) (17) The reflection capability of the terrain depends on its reflection coefficient ρ, deter- mined by the relative permittivity sr and conductivity σ. We use the equation for perpendicular polarization, although we have not assigned a polarization to our signal:

where χ = 18e9 σ/f , σwater = 5 S/m, σland = 0.002 S/m, srwater = 81, and srland = 13 18 for mountainous terrain.

5 The resulting loss, based on the power of the specular component, is:

Lreflection = 10log10(ρ(∆A) 2) (19) Lastly, we use ray tracing methods to determine the direction that the specular com- ponent will reflect, providing the new incidence angle for the next ionosphere bounce. 19 Using the terrain surface mesh, we find the local normal vector nˆ at each mesh-point using the MATLAB function surfnorm. Weuse the incidence angle between the incoming signal and the horizontal to find a local incidence vector ˆi, which is constant for each mesh-point. Using these two vectors with the Law of Reflection, we can determine the local reflected vectors rˆ. 19

rˆ = ˆi + 2cos(θlocal)nˆ (20) where θlocal is the local angle of incidence between the local normal and local incidence vector, determined by:

cos(θlocal) = −ˆi · nˆ (21) Once we find the local reflection vectors, we can take the mean of each component in ordertofindthe totalreflectionvector. Weremovethelocalvectorswhere thez-component isnegativefromthecalculation,becausethisrepresentscaseswheretheterrainisshadowed from the incident signal. With the total reflection direction, we extract the azimuth and elevation using MATLAB’s cart2sph converter to provide for the next bounce.

The example terrain plots, including Figure 2 and Figure 7 and 6 in the Appendix, display the surfaces with local vectors shown, as well as the mean incidence and reflected vectors.

3. Loss

To tie our model together, we return to the overall link budget, updated with new losses:

PRx = PT x + GTx + Lfree + Labsorption + Lreflection + GRx (22) Aftereachionosphereandsurfacebounce,ourmodelreevaluatesthisequationtodeter- mine if the link margin is met. If it is met, the signal continues for another bounce. If not, we determine that signal to be lost, and record its last known surface location. Overall, we have 180 dB in the budget, of which we can lose up to 170 dB to remain over 10 dB.

B.

Model Validation

We will first validate our model qualitatively by following individual rays along their path until they are absorbed, fly into space, or fall below the minimum signal strength. Given accounts of skywave radio operators, we expect that this will depend on the time of 10 We expect the signal to follow a straight day and electron density at the bounce location. path from the origin to the bottom of the ionosphere, followed bya curved point that peaks at the calculated point of refraction, followed by a straight path from the bottom of the ionosphere back to the surface. While we don’t have a quantitative expectation of the signal’s behavior after bouncing off of the surface; however, we do expect that the more surface variation, the more variation we will see in subsequent bounces. We expect that theloss willincreasewithdistancetravelled, and increasewitheach surfaceand ionosphere interaction.

Quantitatively, wefind that a range for the maximum distance of a hop is between 2500 20 We will likely see our maximum distance on our and 5000 km, depending on the height. first bounce because of our ability to control the input frequency and angle.

V. Model Application

In order to recreate the desired scenarios, we set the model conditions for each test, including input variables, output variables, and number of trials.

A. Part I

The first application of our model focuses on reflection of the signal off of the ocean. 13 we will uniformly Using the January 1, 2000 ionosphere data obtained from NASA, randomly select a latitude, longitude, and bearing as the origin of the signal. This location determines only the local ionospheric conditions, because we assume that the signal will bounce off of water for this problem, no matter where it goes.

Wesend this signal initially at an elevation angle of 30°, a frequency of 3 MHz, a power of 100 W, an antenna gain of 5.03 dBi, and a receiver antenna sensitivity of -120 dBm. We will determine a mean, median, and standard deviation of signal strength after a single bounce and the max number of bounces (where bounce 2 and onward are over calm water) given the above initial conditions. Wewill simulate 10000 signals for a first bounce on calm seas with <1 m waves (because this is our base case) and 1000 for a first bounce on rough seas with < 10 m waves.

B. Part II

We will reuse the initial conditions from above, but instead assume that everybounce will take place off land with smooth (perfectly flat) or mountainous (up to 10m deviations). Our results will be in the same format as Part I, and will show the effects of different terrains on the number of reflections of the signal, as well as the power lost for 1000 trials.

C. Part III

Using the same elevation angle and frequency, weremovethe random starting location, ftxing a transmitter location and bearing near the edge of the water. By running 1000 trials with different elevation angles, and outputting the location of each bounce, we can find the region where a ship would be able to receive the signal.

VI. Results

A.

Validation

As we discussed in the Background, we expect that the peak of radio wave reflection to occur in the region of the day/night terminator. This occurs because of a balance of the weak reflection of the night and the strong absorption of the day. Our model matches these results, as shown in Figures 8 and 9 in the Appendix. The former plots the latitude andlongitudeofmodeled oceanic bounces, superimposedoveracolormap ofthemaximum ionosphere electron density that day. The bounces occur between the bright and dark regions, showing a clear preference for the day/night terminator. The latter plot shows the probability of radio waves bursting through the ionosphere as a function of peakelectron density. This probability is near unity the highest and lowest densities, but decreases for intermediate densities, as would be expected near the day/night terminator. Thus, our model matches well with qualitative predictions.

B. Part I

Werunourmodeltocomparetheperformanceofthesignaloncalmoceanandturbulent ocean measured by the power of the signal after the first bounce. For Part I and Part II, we will use a 2 sample t-test because the observed data are from random samples of a skewed normal distributions. For our analysis, we say that our null hypothesis is that thetwo sets of data are the same.

Mean (dB) Std Power (dB) Calm 25.54 4.13 Turbulent 24.82 4.28 The distribution of signal strength after the first bounce is shown in Figure 10 in the Appendix and the numerical values are shown in 1. Running our t-test, we get a p-value of 0.0291, which means the difference in power from calm to turbulent is significant at a 5% level.

Av Distance (km) Std Distance (km) Av Bounces Std Bounces Calm 1444.67 474.26 1.53 0.50 Turbulent 1006.71 231.72 1.10 0.33

As we extend our analysis to include multiple bounces, we find that the maximum number of bounces with an initial angle of 30° and a frequency of 3 MHz is 2 bounces, for both initial calm and initial turbulent cases. Usingthesamet-teston the average signal distance, we get a p-value of 3.87∗10−32, and a p-value of 7.84∗10−28 for the number of bounces. This means that although both have the same maximum number of bounces, we can conclude that overall the turbulent ocean causes a reduction in both distance and bounce number.

C. Part II

We run our model to compare the performance of the signal on smooth terrain and rugged terrain measured by the power of the signal after the first bounce.

Mean (dB) Std Power (dB) Smooth 24.84 4.07 Rugged 24.58 3.97

The distribution of signal strength after the first bounce is shown in Figure 11 in the Appendix and the numerical values are shown in 1. Running our t-test on the two data sets, we get a p-value of 0.39 and cannot prove that the power data from the smooth and rugged terrain simulations are different.

Av Distance (km) Std Distance (km) Av Bounces Std Bounces Smooth 1360.45 453.67 1.47 0.50 Rugged 997.47 316.37 1.25 0.44

As weextend our analysis to include all signals that do not fall below the SNR threshold of 10 dB, we find that the maximum number of bounces that we observe with an initial angle of 30° and a frequency of 3 MHz over smooth and mountainous terrain is 2 bounces. Using the same t-test on the average signal distance over the Earth, we get a p-value of 2.74 ∗10−44 and reject the null hypothesis because the p-value is well below any reasonable statistical measure. Therefore, we can say that the distance data from the smooth and rugged terrain simulations are different. The p-value for bounces is 3.74 ∗10−10, which is similarly significant.

D. Sensitivity Results

Beforeproceeding to Part III, wemust first determine the best initialangle and the best initial frequency for our transmitting station and our boat receiver. Instead of the number of hops, wewill use the highest average Earth distance of an angle-frequency combination.

With an ideal angle 30° and frequency 3 MHz, we will sample three potential locations and ship travel directions in order to determine the maximum distance that the ship can travel away from the station while still receiving communication.

E. Part III

To ensure that our sample size has enough successful bounces to compare the three locations, we choose to sample from locations and directions that showed a highpercent- age of reflection from Parts I and II. Our two realistic locations are Monjaras, Honduras (13°09’07.6”N 87°23’07.2”W) and Los Angeles, California (32°41’19.9”N 117°13’14.7”W), 21 After running these and we will aim our transmitter West and Southwest, respectively. three simulations, we will determine the average performance of our radio system.

In this simulation, we vary the initial angle ∆from 0° to 60° in increments of 0.1° in order to get a representation of a transmitter dispersing a signal.

B1 Min Dist

B1 Max Dist

B2 Min Dist

B2 Max Dist

Honduras (W) 651.77 1085.87 187.67 1622.24 L.A. (SW) 676.42 810.67 - -

Our model tracks the minimum and maximum distance (km) for each bounce that we observe of individual rays. From Honduras, we see that a boat on turbulent oceans could maintain a signal with the transmitting station from 187.67km to 1622.24km in a straight line from the shore. As show in Figure 18 in the Appendix, the location of the first points are concentrated between 651.77km and 1085.87km from the shore. The second bounces are scattered by the turbulent waves and would not provide a consistent signal for a boat outside of the first bounce concentration.

FromL.A., our signal only bounces a single time and coversthe distance stretchof ocean from 676.42km to 810.42km in a straight line from the shore. Similar to the Honduras simulation, the first bounce points are concentrated along the initial trajectory.

VII. Sensitivity Analysis

A. Explore Parameter Space

Inordertoensurethatourmodelisrobust,weneed tounderstand howourassumptions and inputs effect the results. To do this, we select several key inputs and data sets, and vary them with 1000 trials to see how the model responds.

1. Frequency and Elevation Angle

The HF band contains frequencies from 3-30MHz, but wechoose 3 MHz as our default, launched at an angle of 30 degrees. This selection is arbitrary, so we decide to perform a study on the model’s sensitivity to combinations of elevation angle and signal frequency. Our metrics are the distance, bounces, and loss due to ionospheric absorption. We select elevation angles of 0, 2, 5, 10, 15, 20, 30, 40, and 50 degrees for this sweep, accompanying the changes in signal from 3 to 21 MHz by multiples of 3 MHz. We expect that some types of loss penalize high frequencies, while some penalize low, so there is a trade-off. Additionally, the elevation angle effects the overall path length, which effects loss.

The results of this analysis show that functional angle/frequency pairs exist on a line traversing through the parameter space. Deviation from this line causes the signal to either travel unabated through the ionosphere or be totally deteriorated by loss. Pairs with low frequencies and high angles tend to bounce more, but travel a shorter overall distance, as is seen in Figures 12 and 13 in the Appendix. High frequency/low angle pairs are much more likely to be consumed by loss than low frequency, high angle pairs. This can be observed in Figure 14 in the Appendix.

2. Wave Turbulence

For the wave turbulence, we wish to determine the limits of the extent to which tur- bulent water can effect the overall distance. We do this by adding an additional metric for super-turbulent swells with a max height of <15 m, representative of extreme storm conditions, as well as running trials that bounce off of the same type of wa- ter for all bounces instead of calm water for bounces after the first. We expect that super-turbulent water will have the most effect on decreasing distance, but changing the subsequent bounces will also decrease the distance.

performat-testtodeterminewherethesedifferencesaresignificant. Wetestthehypotheses that each pair of observations have the same mean and find p-values of essentially 0 for the Calm/Turbulent and Calm/Super Turbulent pairings. The final pairing,Turbulent/Super Turbulent,has an insignificant p-value of 0.64. Thus, we conclude that turbulent and super turbulent oceans tend decrease the mean distance traveled by the radio signal. A box-plot of these data are found in Figure 15 in the Appendix.

Distance Traveled Calm Turbulent Super Turbulent Mean (km) 1445 1007 995 Standard Derivation 474 232 253 (km)

3. Transmit Power

The power of the transmitter determines the initial signal strength, so we want to examine if increasing this parameter allows the signal to bounce a greater distance across theEarth. Thetransmitter power is increased inorder of magnitudesteps of 100 W, 1000 W, and 100,000 W, which correspond to 50, 60, and 80 dBm. Including the antenna and receiver sensitivity, the values are 180, 190, and 210 dBm total signal compared to the 10 dB cutoff.

Plugging these values into the simulation, we find statistics presented in Table 7. We compare these simulations with a 2-sample t-test, finding the differences between all three pairs to be statistically significant. The lowest p-value, 4E-5, corresponds to the null hypothesis that the 190 and 210 dBm signals have the same average distance travelled. This is much lower than any common significance level. The other p-values are essentially

0. Weconclude that the more powerful the transmitter, the greater the overall

distance travelled. A box plot of this data can be found in Figure 16 in the Appendix.

Distance Traveled 180 dBm 190 dBm 210 dBm Mean (km) 1445 1737 2105 Standard Derivation 474 672 1168 (km)

4. Ionosphere Density

Our sample used NASA’s ionosphere data for January 1, 2000. This year recorded 11 a relatively high amount of solar activity compared to neighboring nearly 140 sun spots, years. To test the effect of the number of sun spots on our model, we use NASA data for the years 2003 and 2009, with 70 sun spots and 10 sun spots 11, respectively.

These represent a moderate and low case of solar activity. The solar activity influences the electron density of the ionosphere, which should increase the refractive index, making it more difficult for signals to reflect instead of refract.

As in the previous cases, weplugged these parameters into the simulation and recorded the resultant total distances, with overall statistics displayed in Table 8. We perform a two-sample t-test on each of these pairs, and find an insignificant p-value of 0.6 for the 2009/2003 pair. Thus, wecannot conclude that these twodata sets are different. However, the 2009/2000 and 2003/2000 pairs have p-values of 0.03 and 0.003 respectively, which are both significant at the common 5% standard. Thus, we can conclude that high solar activity has a statistically signiftcant negative effect on distance travelled. See

Distance Traveled 2009 Data 2003 Data 2000 Data (Low) (Medium) (High) Mean (km) 1587 1551 1445 Standard Derivation 520 430 474 (km)

VIII. Conclusion

A. Our Conclusion

Using high-throughput simulation of radio wavetravel, we explore the parameters that most strongly affect radio communications. Wefind that the interaction between the radio wavesandtheionosphereisthestrongestdeterminantofpropagationbehavior. Thetypical loss a signal experiences in the ionosphere is around 15-20 dB, whereas typical loss from ground interaction is less than one dB.

The sensitivity to the ionosphere manifests itself when considering the frequencyand angle of elevation of skywave. Too much interaction with the ionosphere will sap the signal’s strength, while too little interaction will not alter its upward trajectory, allowing it to escape to space. The seasonal and daily changes in the ionosphere also have marked effectsonsignalpropagation,increasingand decreasingtheelectrondensityasmoreorless solar radiation is incident on the atmosphere.

Also important to radio wave propagation is interaction with the Earth. We consider multiple terrains in this model, and find that rough oceans or mountainous land slightly reduce signal strength while scattering its trajectory.

Through our consideration of all relevant signal attributes, we qualitatively match known radio wave behavior. Thus, we hold this model to be a useful tool for radio enthu- siasts and professionals alike.

B.

Strengths

• The model considers the complexity of the layers of the ionosphere, using real global data for day and night that varies with altitude. This allows more accurate cal- culations of ionospheric trajectory and absorption loss, as well as when signals are reflected or transmitted, matching real world expectations for the day/night termi- nator.

• The model considers a curved ionosphere and curved Earth, finding more accurate distances as arc lengths over the surface than a flat approximation.

• The model uses realistic terrain shapes for land and water, to aid in determining correct reflection loss and bounce direction.

• The model is computationally efficient, allowing 1000 trials to run in just a few minutes on a personal laptop.

C. Weaknesses and Limiting Assumptions

• The model ignores many potential sources of loss, including multipath loss due to polarization in areas other than the ground bounce, as well as Doppler shift and magnetic effects in the ionosphere.

• The model only considers a small patch of ground, when in reality the signal would bounce off a much larger area. It also neglects surface coverings.

• The model does not consider the ways that the ionosphere changes with time on scales larger than one day-night cycle, unless a completely new data set is provided.

• The model does not take into account the use of real radio equipment with cables, noise, and the need to transmit information with a low bit error rate.

D. Future Work

Our simulation could be extended and improved by increasing the complexity of the data used, and reducing assumptions. If we gained access to or created a model of iono- spheric conditions with time, we could make the time an input to our model. With a full global land data set, we could tie the latitude and longitude to terrain as well as the iono- sphere, and make theterraindeterministicfor a given location. Inaddition, with moretime wecould include bigger land and water patches, so larger features would dominate instead of very local ones. Loss accuracy could be increased by accounting for the signal phase and interference throughout the propagation, as well as considering real radio equipment.

Furthermore, we could gain greater understanding of the accuracy of our modelcom- pared to real skywave signals by finding an empirical data. For instance, if we found recorded information about the equipment used, transmit and receive locations, and exact date and time, we could use an ionosphere dataset for that day to simulate the real contact. We could see where the signals bounced on the Earth, and what power we expect themto arrive with, to see if our model is accurately recreating trajectory and loss.

IX. Letter

Skywave communication remains the only non-line-of-sight method of radiocommu- nication over vast, turbulent oceans and disruptive terrain. While bouncing the signal between the ionosphere and the surface of the Earth allows signal transmission over long distances, it introduces the unpredictability of the ionospheric density, the non-uniformity of reflection surfaces, and signal deterioration over the path of the signal.

Our model simulates a transmitter at an initial latitude and longitude on a spherical Earth beaming a HF (between 3 MHz and 30 MHz) signal with an initial bearing and eleva- tion angle. For our simulation, we assume a 100-Watt transmitter with a 100-meter dipole antenna. The model of the ionosphere was adapted from a gradient set of data collected by NASA (see NASA’s International Reference Ionosphere data set). Using the variable density, we can determine the refraction of the signal at each layer of the ionosphere.

Oncethe signalexits thebottom ofthe ionosphere, itcontinues onits trajectorytowards asimulatedpatchofterrainusingeitherawavesimulatororgeologicalelevationdata. From this bounce we determine the impact loss and the new trajectory of the signal. Weiterate this process until the signal falls below the sensitivity of the radio receiver.

With the path determined, we calculate the loss along the path of the signal considering freespacepathlossduetospreadingalongdistance,ionosphericabsorptionloss,andreflec- tion loss from scattering. While other sources of loss exist in real systems, we determined that these three losses constitute most of the loss incurred during transmission.

Due to the unpredictability of the ocean and of terrain, we test skywave paths that bounce on calm and turbulent water, as well as smooth and mountainous land. Wedo this by randomly varying transmitter locations, and test paths from coastal cities to determine the maximum effective transmission distance.

We observe the largest difference in our results when varying frequency and elevation angle. To determine their relation to one-another, we co-vary the frequency and elevation angle. From this analysis, we find an effective angle and transmission frequency around 10° and 20 MHz. Lower frequency and higher angle pairs, such as 30° and 3 MHz tends to bouncemore,buttravelalowerdistance. Theeffectivenessoftheradiowavesrangingabove 50° and 15 MHz quickly dissipates, as these waves are either absorbed in the ionosphere or launched into space.

We also explore our models sensitivity by altering the wave conditions from calm to super-turbulent, increasing the transmission power, and changing ionospheric density. Of these factors, the ruggedness of the terrain has the largest influence of the dispersion of the signal, while the ionospheric density (heavily influenced by sun spot number) causes our waves to be absorbed or lost in space.

Inour most realisticsimulation, wesend a signalfrom Honduras directly southwest at 3 MHz and a varying elevation angle. Wefind that the signal distance ranges from 187.67km to 1622.24km in a straight line from the shore. The signal as it first bounces is fairly concentrated, while the secondary bounces shows a near-chaotic dispersion of the signal fromtheroughnessofthewaves. This600raysimulationdemonstratestheunpredictability of the spread of HF radio waves on rough terrain. These results demonstrate the cause for dead-zones of skywave signals, especially on the open ocean.

In summary, our model considers the most significant factors in modeling the behavior of HF radio waves. Through these considerations and our sensitivity analysis, wequalita- tively match known radio wave behavior as well as approximate ranges expected from the transmission systems described above. Thus, we hold this model to be a useful tool for radio enthusiasts and professionals alike.

X. Appendix

Diagram of Calculated Ionosphere Trajectory

This plot provides an example of our ionosphere model, illustrating the bending of the signal before it is reflected.

Example Terrain with Vectors

These plots demonstrate the terrain generation and vector reflection calculations. The axes describe the x and y locations, as well as height, in meters. The local vectors are positioned at every mesh-point to illustrate the local calculations. The mean vectors are shown to the side in red and yellow. Land is shown in grey and water in blue. The water plot is formatted identically to land, except the local normal vectors are omitted for clarity.

Model Validation: Comparing Absorbed and Escaped Signals to Modeled Electron Density Signal Remaining After First Bounce for Water (Part I) and Land (Part I) Results of Frequency and Elevation Angle Sweep Sensitivity Analysis

Results of Ocean Turbulence Sensitivity Analysis

tistically different than both turbulent oceans.

Results of Transmit Power Sensitivity Analysis Results of Ionosphere Electron Density Sensitivity Analysis

Results from Geographic Locations in Part III
