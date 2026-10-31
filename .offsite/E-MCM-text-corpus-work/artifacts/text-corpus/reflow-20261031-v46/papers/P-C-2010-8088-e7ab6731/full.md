# P-C-2010-8088-e7ab6731

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
1 of 10

<!-- b000002 | furniture | pages [1] -->
Team # 8088

<!-- b000003 | heading | pages [1] -->
Abstract

<!-- b000004 | prose | pages [1] -->
Massive amounts of plastic waste have been accumulating in the Great Pacific Garbage Gyre and are posing a threat to the marine environment. Since little is known about the degradation of plastics in this marine setting, we adopted the goal of modeling the photodegradation of a common plastic, polyethylene, in seawater. The plastic in the ocean is exposed to UV light form the sun which causes photodegradation, which is a natural source of plastic decomposition.  We developed two models to describe the rate of photodegradation of polyethylene floating in seawater; the Low Transmittance of Light Model (LTM) and the High Transmittance of Light Model (HTM).   Using the constant rate of UV irradiance and the average bond dissociation energy of carbon-carbon single bonds (C-C) we calculate the mass lost per unit of time by triple integrating the rate of mass lost per unit of time over area and time. The outputs of our models were realistic and resulted in the change of mass over time. The HTM predicated that a 1x1x2cm rectangular prism of polyethylene weighing 1.86g will lose 1.26g of mass in one year. The LTM predicts a hollow sphere with thickness 0.0315cm and a radius of 5cm weighing 9.145g, and is partially submerged in low transmittance water to lose 0.1897g of mass in the first year. The design of our models allows us to change the limits of integrations to model other shapes, adjust the intensity of UV light, and can realistically predict the photodegradation of polyethylene.

<!-- b000005 | furniture | pages [2] -->
2 of 10

<!-- b000006 | furniture | pages [2] -->
Team # 8088

<!-- b000007 | prose | pages [2] -->
Shedding Light on Marine Pollution

<!-- b000008 | furniture | pages [2] -->
Team #8088

<!-- b000009 | prose | pages [2] -->
ICM 2010

<!-- b000010 | heading | pages [2] -->
Table of Contents

<!-- b000011 | heading | pages [2] -->
I. Introduction

<!-- b000012 | prose | pages [2] -->
3

<!-- b000013 | heading | pages [2] -->
II. Description of the Problem

<!-- b000014 | prose | pages [2] -->
3

<!-- b000015 | heading | pages [2] -->
III. Photodegradation of Polyethylene

<!-- b000016 | prose | pages [2] -->
3

<!-- b000017 | heading | pages [2] -->
IV. General Assumptions

<!-- b000018 | prose | pages [2] -->
5

<!-- b000019 | heading | pages [2] -->
V. High Transmittance Model

<!-- b000020 | prose | pages [2] -->
5

<!-- b000021 | heading | pages [2] -->
VI. Low Transmittance Model

<!-- b000022 | prose | pages [2] -->
6

<!-- b000023 | heading | pages [2] -->
VII. Comparisons and Limitations

<!-- b000024 | prose | pages [2] -->
8

<!-- b000025 | heading | pages [2] -->
VIII. Discussion of Impacts

<!-- b000026 | prose | pages [2] -->
9

<!-- b000027 | heading | pages [2] -->
IX. Conclusion

<!-- b000028 | prose | pages [2] -->
9

<!-- b000029 | heading | pages [2] -->
X. References

<!-- b000030 | references | pages [2] -->
10

<!-- b000031 | heading | pages [2] -->
XI. Appendix A

<!-- b000032 | prose | pages [2] -->
11

<!-- b000033 | furniture | pages [3] -->
3 of 10

<!-- b000034 | furniture | pages [3] -->
Team # 8088

<!-- b000035 | heading | pages [3] -->
I Introduction

<!-- b000036 | prose | pages [3] -->
The accumulation of plastic debris in our oceans is quickly coming to light as one of the most prevalent and devastating threats to the marine environment.  The “Great Pacific Ocean Garbage Patch” is one of many areas of wind current convergence where massive amounts of debris collect and stew.  The “garbage” is not primarily found in the form of bottles and bags, but rather as tiny particles referred to as neustonic plastics.  These neustonic plastics are the products of degradation of post-consumer and industrial wastes and may pose great risk for marine life.  The nature of the degradation of plastics has thus become an important element in the study of this environmental catastrophe. In this study, we focus specifically on the photolytic degradation of plastic accumulating in the gyre. This involves the consideration of ultraviolet radiation reaching the surface of the ocean, the energy required to break the bonds that form the common plastic polyethylene, and physical considerations concerning buoyancy, mass, and surface area of the plastic particles. Specifically, this study models the loss of mass of polyethylene plastics by photolytic degradation per year.

<!-- b000037 | heading | pages [3] -->
II Description of the Problem

<!-- b000038 | prose | pages [3] -->
In this problem we consider the degradation of floating polyethylene fragments by photolytic degradation.  The fragments are considered to be hollow spheres partially filled with seawater, to represent common post-consumer waste containers. The fragments are partially submerged in water with either low or high percent transmittance of light. High transmittance water can use the entire effective surface area of the fragment to model degradation while fragments in low transmittance water only the portion of the fragment above water will be susceptible to photolytic degradation16.  Ultraviolet light is assumed to hit the fragment orthogonally to the plane of the ocean, thereby exposing a 2-dimensional effective surface area, from now on referred to as , to the rays.  Thus,  represents the portion of the fragment susceptible to photolytic degradation. We relate  to the radius of the fragment, , since surface area of a sphere varies with radius.  The mass of the fragment, then depends on and .  The goal then, is to effectively model these relationships with respect to each other and to time in a way that will input some time, , and output a mass, which will describe the loss of mass experienced by a polyethylene fragment.

<!-- b000039 | heading | pages [3] -->
III Photolytic Degradation of Polyethylene

<!-- b000040 | prose | pages [3] -->
Polyethylene is a polymer consisting of long chains of the monomer ethylene1. There are two types of bonds present in polyethylene; carbon-carbon single bonds (C-C) and carbon-hydrogen single bonds (C-H)4.  See Figure 1 for polyethylene structure.

<!-- b000041 | caption | pages [3] -->
Figure 1: Structure of polyethylene where n= number of monomers in the chain

<!-- b000042 | prose | pages [3] -->
- (CH2-CH2) n-

<!-- b000043 | prose | pages [3, 4] -->
Photodegradation is a process by which chemical bonds are broken when struck by light1,8. In order to break an intermolecular bond the light must carry enough energy to cleave the bond. The energy needed to cleave a bond can be estimated using the average bond dissociation energy (B.D.E) 4. Once the energy needed to cleave a bond is known, the equation can be used to find the minimum wavelength, , of light that carries enough energy to break the bond10.  See Figure 2 for calculation of .

<!-- b000044 | furniture | pages [4] -->
4 of 10

<!-- b000045 | furniture | pages [4] -->
Team # 8088

<!-- b000047 | caption | pages [4] -->
Figure 2: Calculation of

<!-- b000048 | prose | pages [4] -->
When polyethylene is exposed to ultraviolet light (UV) with a  of 344 nm, C-C single bonds are cleaved and free radicals are formed to react quickly with O2 to form peroxy radicals. The peroxy radicals then either continue a chain reaction of radical formation or two free radicals can react to terminate the chain reaction1,7,12 . The pathway of free radical chain reactions and termination reactions can be seen in Figure 3.

<!-- b000049 | caption | pages [4] -->
Figure 3: Photo oxidative reaction mechanism1.

<!-- b000050 | prose | pages [4] -->
R-H + UV         R∙

<!-- b000051 | prose | pages [4] -->
R∙ + O2                R-O-O∙

<!-- b000052 | prose | pages [4] -->
R-O-O∙ + R-H        R-O-O-H + R∙

<!-- b000053 | prose | pages [4] -->
Photo oxidation termination reactions.

<!-- b000054 | prose | pages [4] -->
R∙ + R∙           R-R

<!-- b000055 | prose | pages [4] -->
R-O-O∙ + R∙        R-O-O-R

<!-- b000056 | prose | pages [4] -->
An integral part of the model is the cleavage of C-C single bonds to break polyethylene into fragments. This accounts for the loss of mass as the polyethylene is degraded over time. The rate of degradation can be estimated by assuming that every time a C-C bond is cleaved by UV light, a monomer is removed from the original mass of polyethylene. The rate at which the C-C bonds can be cleaved is dependent on the amount of UV light emitted by the sun in watts/m2 which is a unit of irradiance. See Figure 5 for unit conversion1,7,12.

<!-- b000057 | caption | pages [4] -->
Figure 5: Unit conversion used to find the rate of photodegradation in (sec*cm2/g)

<!-- b000058 | furniture | pages [5] -->
5 of 10

<!-- b000059 | furniture | pages [5] -->
Team # 8088

<!-- b000060 | heading | pages [5] -->
IV General Assumptions

<!-- b000061 | prose | pages [5] -->
For the sake of simplicity we make the following assumptions:

<!-- b000062 | prose | pages [5] -->
Mechanical degradation due to torque on plastic is minimal due to small size of plastic  particles11, and colliding plastic particles are rare due to low particle density5, therefore our model neglects mechanical degradation Polyethylene particles will float in seawater since polyethylene’s density is .93g/ml and  average density of 35ppt saline seawater at 15ºC is about 1.0255g/ml9. This neglects water currents.

<!-- b000063 | prose | pages [5] -->
Source of UV light is a constant average at sea level pacific northwest3.  Polyethylene in model does not contain UV stabilizers and is medium density.  Polyethylene is composed of ethylene monomers and the average bond dissociation energy  for C-C single bonds is used to predict energy needed to cleave the C-C bonds4.

<!-- b000064 | prose | pages [5] -->
Only the portions of the plastic fragments that are perpendicular to the UV light are subject  to photolytic degradation.

<!-- b000065 | prose | pages [5] -->
We are assuming transmittance of light through the water is high in the Simple Model and  very low in the Final only the effective surface area above water can receive UV light.

<!-- b000066 | prose | pages [5] -->
The photolytic cleavage of C-C bond in the model is assumed to be a fast forward reaction  Krxn>>1 and the reverse reaction very slow. Immediately after the bond is cleaved the free radical forms and is quenched by any of the termination reactions that also have a Krxnb>>1.

<!-- b000067 | heading | pages [5] -->
V High transmittance Model

<!-- b000068 | prose | pages [5] -->
This model considers the degradation of a square prism of polyethylene on a flat surface on land or in water with a very high percent transmittance of light. One of the faces of the prism facing directly perpendicular to the UV light source. For this Low Transmittance model, we will define the rate of degradation from Figure 5 as the constant K1.  This expression can be modeled over time and area as a triple integral:

<!-- b000069 | prose | pages [5] -->
The result is a simple, linear model of degradation based on time and area:

<!-- b000070 | prose | pages [5] -->
Consider a square prism with the dimensions of 1x1x3 cm with an initial mass of 1.86g. After 365 days of UV exposure, 1.26 grams of polyethylene are lost as a result of photolytic degradation9.

<!-- b000071 | furniture | pages [6] -->
6 of 10

<!-- b000072 | furniture | pages [6] -->
Team # 8088

<!-- b000073 | heading | pages [6] -->
VI Low transmittance Model

<!-- b000074 | prose | pages [6] -->
A primary factor in describing the amount of UV light that a fragment of plastic absorbs is the effective surface area perpendicular to direct sunlight.  Since the North Pacific Gyre is a collection of floating debris, we used Archimedes’ principle to relate the buoyancy of a piece of plastic to its effective surface area.  We have chosen to neglect the effect of air in the container on buoyancy for simplicity.  Archimedes’ principle states that “the buoyant force on a submerged object is equal to the weight of the fluid that is displaced by that object. “ 15   In addition, since the plastic is in kinetic equilibrium in the vertical direction, its buoyant force must be equal in magnitude to its weight:

<!-- b000075 | prose | pages [6] -->
By selecting that we want to define volume submerged in terms of mass we choose;

<!-- b000076 | prose | pages [6] -->
Where M is mass, W is weight, V is volume, d is density, and g is the force due to gravity.

<!-- b000077 | prose | pages [6] -->
We can define the right side of this equation with the triple integral

<!-- b000078 | prose | pages [6] -->
With limits of integration where h is the thickness of the plastic and x is the angle in radians from the zenith to the point on the sphere’s surface where it contacts the water level.  Setting this integral equal to the total mass of the plastic, you can solve for x. Trigonometry relates the radius of the sphere, r, and the angle, x, to the effective surface area of the sphere exposed perpendicularly to UVB rays (c). This is depicted in Diagram 1 below.

<!-- b000079 | prose | pages [6] -->
Ocean Surface

<!-- b000080 | prose | pages [6] -->
r x

<!-- b000081 | prose | pages [6, 7] -->
Diagram 1: Finding the Effective Solar Radius As you can see from Diagram 1, the effective solar radius is

<!-- b000082 | furniture | pages [7] -->
7 of 10

<!-- b000083 | furniture | pages [7] -->
Team # 8088

<!-- b000085 | prose | pages [7] -->
To consolidate the necessary input arguments, we have defined r in terms of m by subtracting the volumes of two concentric spheres with ∆r=h, then multiplying by the density of the plastic, l.

<!-- b000086 | prose | pages [7] -->
The equation above can easily be rearranged to solve for r:

<!-- b000087 | prose | pages [7] -->
We created a constant K based on our fundamental relationship between the mass of plastic in grams, and the total bond energies within that mass in Joules.  K has of the units  .  K is easily calculated using the molar mass and average bond energy of polyethylene as shown in this dimensional analysis:

<!-- b000088 | prose | pages [7] -->
Ultraviolet light is the source of energy in this model.  We have defined it as a variable, U, only substituting in a value when necessary to show example outputs from the model.  A true experiential value for U would need to be calculated on site and calibrated to represent the average Joules of UV light that reaches the Pacific Gyre per year.  U is the amount of energy available to impact the system in J/cm2*yr.  UK uses the constant K to define that energy as amount of mass in grams, cleaved off by the breaking of a total number of Joules of C-C single bonds.  The term UK therefore, has units of g/cm2*year.  To solve for a total change in grams over a specific time and area, we integrate the term with respect to time from zero to t, and then with respect to area, a double integral in polar coordinates.

<!-- b000089 | prose | pages [7] -->
Furthermore, if you take this change in mass and subtract it from the initial mass, the result is a final mass of plastic for given initial mass subject to ultraviolet light of intensity U over a time t.

<!-- b000090 | prose | pages [7] -->
Where the units are:

<!-- b000091 | furniture | pages [8] -->
8 of 10

<!-- b000092 | furniture | pages [8] -->
Team # 8088

<!-- b000093 | prose | pages [8] -->
Using the LTM consider a hollow sphere with thickness .0315cm, a radius 5cm, initial mass of 9.145g after one year of UV exposure the loss in mass is .1897g of polyethylene. Rate of degradation can be visualized in Diagram 2.

<!-- b000094 | prose | pages [8] -->
Diagram 2: The Relationship between Mass of Sphere and Time

<!-- b000095 | prose | pages [8] -->
Mfinal(t)

<!-- b000096 | prose | pages [8] -->
10 9 8 7 Mass (g) 6 5 4 3 2 1 0 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49

<!-- b000097 | prose | pages [8] -->
Time (years)

<!-- b000098 | heading | pages [8] -->
VII Comparisons and Limitations

<!-- b000099 | prose | pages [8] -->
Two models were developed to determine the mass lost due to photodegradation from a piece of polyethylene plastic after a certain length of time exposed to UV light. The first model is the High Transmittance Model (HTM), where the fragment is a rectangular prism, and is treated as if it is on land or in 100% transmittance water. This model uses a triple integral over time and area, giving an output of grams of original polyethylene lost. The Low Transmittance Model (LTM) describes a fragment submersed in low transmittance water where only the exposed effective surface area of the fragment can undergo photodegradation. Like the HTM, this model uses a triple integral to find grams of original polyethylene lost.  The difference is that the LTM models the exposed effective surface area of a hollow sphere of a particular thickness, partially submerged in water due to buoyancy. Depending on the conditions of the water (density and transmittance) and the shape of the object, the models can be altered to describe photodegradation of polyethylene in many other shapes in high or low transmittance water.

<!-- b000100 | prose | pages [8] -->
Although both models give reasonable outputs, each is particularly applicable in specific situations. Many assumptions about the reaction conditions had to be made to simplify the mathematics. The assumptions were not perfect and decrease the accuracy of the model. In order to increase the accuracy of our model a few main points need additional research and refinement:

<!-- b000101 | prose | pages [8] -->
Value (U) used for Irradiance of UV light in the North Pacific Ocean needs to be verified  primary research in order to find a solid value for UV irradiance.

<!-- b000102 | furniture | pages [9] -->
9 of 10

<!-- b000103 | furniture | pages [9] -->
Team # 8088

<!-- b000104 | prose | pages [9] -->
Mechanical degradation will also have an effect on the degradation and should be included  along with the photo degradation function to increase the accuracy of mass lost.

<!-- b000105 | prose | pages [9] -->
Models do not describe the fact that particles tend to converge on a similar size around 3-  5mm14.

<!-- b000106 | prose | pages [9] -->
Many polyethylene products have UV stabilizers that increase the longevity of the plastic by  inhibiting the free radical chain reaction1.

<!-- b000107 | prose | pages [9] -->
Polyethylene can be one of many types varying in density. Our model used medium density  polyethylene (MDPE).

<!-- b000108 | prose | pages [9] -->
Plastics are not just on the ocean surface but also at depths up to 100ft.  Polyethylene, although very common, is not the only plastic in the North Pacific Gyre. 

<!-- b000109 | heading | pages [9] -->
VIII  Discussion of Impacts

<!-- b000110 | prose | pages [9] -->
Our models effectively describe the rate at which UV light breaks down polyethylene. The process is slow and there is inconclusive evidence as to whether plastics ever degrade entirely in the gyre. Plastics are thus a prevalent long-term environmental antagonist.  Possible ecologic effects of the accumulation of massive amounts of plastic in the Pacific Ocean Gyre include ingestion of plastic particles by marine life, the disturbance of the transmittance of light below the surface of the water, which may affect many organisms’ ability to synthesis energy from photosynthesis, and the distribution of hydrophobic pollutants.  Our model relates to the ingestion of plastic particles by marine life since it predicts the mass of fragments at a given time and marine organisms may confuse plastic fragments that are similar in size to their normal food source.

<!-- b000111 | prose | pages [9] -->
Contributing to the growing problem of plastic pollution in the ocean is the lack of governmental regulation on pollution by cruise ships.  During a one-week trip, a typical cruise ship produces 50 tons of garbage17.  Regulations are tricky though, because international waters do not have well- defined environmental authority structures, and monitoring is minimal17. Stronger regulations and monitoring systems are required to decrease the impact of pollution by cruise ships.

<!-- b000112 | prose | pages [9] -->
Land-based sources contribute to 80% of marine debris, 65% of which is from post-consumer plastics that were improperly disposed of18.  This means that the plastics are littered, not just that they are not recycled.  Many states have laws against littering, but monitoring efforts need to be improved.  Education about the devastating impacts of littering is a must.  Education and monitoring programs may be expensive, but the cost would likely be small when compared to the potential for environmental protection.

<!-- b000113 | heading | pages [9] -->
IX Conclusion

<!-- b000114 | prose | pages [9] -->
In this study we proposed two realistic models for the photodegradation of polyethylene.  The first model is used for a solid chunk of polyethylene either on land, or in water with 100% transmittance of light.  The second model is more complex and considers a partially submerged hollow sphere of polyethylene that is only degraded over the effective surface area. Each model has an output in terms of mass in grams.  Practical application of these models includes the investigation of the

<!-- b000115 | furniture | pages [10] -->
10 of 10 Team # 8088

<!-- b000116 | prose | pages [10] -->
photodegradation of plastic currently in the gyre as well as future accumulations.  This means that our models can accurately describe degradation of partially degraded or intact plastic products since the initial physical properties (size, mass, etc.) of polyethylene can be manipulated in both models. The ease of manipulation and thorough consideration of realist variables make our models appropriate for the study of photodegradation of polyethylene.

<!-- b000117 | heading | pages [10] -->
X References

<!-- b000118 | source_object | pages [10] -->
1. Carey, Francis A., and Richard J. Sundberg. Advanced Organic Chemistry: Part A: Structure and Mechanisms (Advanced Organic Chemistry / Part A: Structure and Mechanisms). 5th ed. Vol. A. New York: Springer, 2007. Print. 2. "The Chemical Composition of Seawater." Seafriends home page. 2006. Web. 21 Feb. 2010. <http://www.seafriends.org.nz>. 3. Karam, Andrew. "What Percentage of Sunlight is UV Light." MadSciNet: The 24-hour exploding laboratory. 27 July 2005. Web. 20 Feb. 2010. <http://www.madsci.org/>. 4. Leeming, William. Thermal and Photolytic Degradation of Polypropylene. Thesis. Univeristy of Glasgow, 1973. Glasgow: Glasgow Thesis Service, 1973. Print. 5. Moore, C. J., G. L. Lattin, and A. F. Zellers. "Density of Plastic Particles found in zooplankton trawls from." Algalita Marine Research Foundation. Print. 6. Moore, C. J., S. L. Moore, M. K. Leecaster, and S. B. Weisberg. "A Comparison of PLastic and Plankton in the North Pacific Central Gyre." Marine Pollution Bulliton 42.12 (2001):1297-1300. Print 7. McNaught, A. D., and A. Wilkinson. IUPAC. Compendium of Chemical Terminology. 2nd ed. Oxford: Blackwell Scientific Publications, 1997. Print. 8. Okabe, Hideo. Photochemistry of Small Molecules. New York: Wiley-Interscience Publication, 1978. Print. 9. "Polyethylene EMEA." Chevron Phillips Chemical Company. 2009. Web. 20 Feb. 2010. <http://www.cpchem.com/>. 10. Skoog, Holler, and Crouch. Principles of Insturmental Analysis. 6th ed. Vol. 1. Thompson Brooks/Cole, 2007. Print. 11. Tipler, Paul Allen. Physics for scientists and engineers. New York: W.H. Freeman, 2004. Print. 12. Trozzolo, A., and F. Winslow. "A Mechanism for the Oxidative Photodegradation of Polyethylene." Macromolecules (1967): 98-100. Print.v 13. Wade, L. G. Organic chemistry. 7th ed. Upper Saddle River, N.J: Pearson Prentice Hall, 2010. 14. Yamashita, Rei, and Atusushi Tanimura. "Floating plastic in the Kuroshio Current area, western North Pacific Ocean." Marine Pollution Bulletin 54.4 (2007): 485-88. Print 15. Hodanbosi, Carol. "Buoyancy: Archimedes Principle." NASA. Aug. 1996. Web. 22 Feb. 2010. <http://www.grc.nasa.gov/WWW/K-12/WindTunnel/Activities/buoy_Archimedes.html>. 16. Ivanhoff, Alexander, Nils Jerlov, and Talbot Waterman. "A Comparitive Study of Beam Transmittance and Scattering In the Sea Near Bermuda." Luminology and Oceanography 2.2 (1961): 129-48. Print. 17. Cruise Ship Pollution State Activity Page." State Environmental Resource Center - Welcome. Web. 22 Feb. 2010. <http://www.serconline.org/cruiseShipPollution.html> 18. Algalita Marine Research Foundation - Marine Research, Education and Restoration. Web. 22 Feb. 2010. <http://algalita.org/AlgalitaFAQs.htm>.

<!-- b000119 | furniture | pages [11] -->
11 of 10 Team # 8088

<!-- b000120 | source_object | pages [11] -->
Variable m h x t r c k u d l re dm mf Units grams(g) (cm) (radians) (years) (cm) (cm)2 (g/J) J/(cm2*years) (g/cm2) (g/cm2) (g) (g) Description Total Initial Mass of Plastic Thickness of Plastic Angle from vertical to contact  with water Time Outer Radius of Sphere Effective Above Water Surface Area Unit Conversion, Proportional Constant UV light energy Density of the Water the Plastic is Buoyed in Density of the Plastic Effective Radius of The Water- Line of the Sphere Change in Mass after time (t) Mass after time (t) Value for Model 9.145 0.0315 x=acos(3*m/(2*pi*d*(3*r^2- 3*r*h+h^2) *h)-1) 1 r=4*pi*h^2+SQRT((4*pi*h^2)^2- 4*4*pi*h*(4/3*pi*h^3-m/0.93)) /(2*4*pi*h) c=pi*(r*cos(- 1*(acos(3*m/ (2*d*pi*h*(3*r^2- 3*r*h+h^2)) -1)+pi/2)))^2 8.046*10-5 1400 1.0255 0.93 re=r*cos (pi/2-x) mf=m-(u* k*re^2*pi*t) mf=m-(u* k*re^2*pi*t) mi h t r(t-1) c k u d l RE(t-1) Change in M Mfinal(t) Input 9.145 0.0315 x(t-1) 0 0.00008046 1400 1.0255 0.93 9.145 0.0315 0.616098 1 4.996599986 2.6489E-30 0.00008046 90 1.0255 0.93 2.887309 0.189653 8.955347 0.0315 0.616054 2 4.944647618 5.79493981 0.00008046 90 1.0255 0.93 2.857112 0.185706 8.769641 0.0315 0.61601 3 4.893240429 5.6747479 0.00008046 90 1.0255 0.93 2.827231 0.181842 8.587799 0.0315 0.615965 4 4.842372699 5.55705691 0.00008046 90 1.0255 0.93 2.797665 0.178059 8.40974 0.0315 0.61592 5 4.792038768 5.44181471 0.00008046 90 1.0255 0.93 2.768409 0.174354 8.235385 0.0315 0.615875 6 4.742233035 5.32897026 0.00008046 90 1.0255 0.93 2.739459 0.170727 8.064658 0.0315 0.615829 7 4.692949958 5.2184736 0.00008046 90 1.0255 0.93 2.710814 0.167175 7.897483 0.0315 0.615782 8 4.644184053 5.11027579 0.00008046 90 1.0255 0.93 2.682469 0.163697 7.733786 0.0315 0.615735 9 4.595929896 5.00432893 0.00008046 90 1.0255 0.93 2.654421 0.160292 7.573494 0.0315 0.615688 10 4.548182115 4.90058611 0.00008046 90 1.0255 0.93 2.626668 0.156958 7.416536 0.0315 0.61564 11 4.500935398 4.79900139 0.00008046 90 1.0255 0.93 2.599206 0.153693 7.262843 0.0315 0.615592 12 4.454184488 4.69952981 0.00008046 90 1.0255 0.93 2.572032 0.150496 7.112347 0.0315 0.615543 13 4.407924184 4.60212733 0.00008046 90 1.0255 0.93 2.545143 0.147366 6.964981 0.0315 0.615493 14 4.362149337 4.50675084 0.00008046 90 1.0255 0.93 2.518536 0.144301 6.82068 0.0315 0.615443 15 4.316854854 4.41335811 0.00008046 90 1.0255 0.93 2.492209 0.1413 6.679381

<!-- b000121 | caption | pages [11] -->
Appendix A: Excel Spreadsheet of Variables and LTM
