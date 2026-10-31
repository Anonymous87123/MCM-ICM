# P-C-2010-7812-c2fa13fd

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
TEAM # 7812                                                                                                                                                                  1 / 10

<!-- b000002 | title | pages [1] -->
Size-Classified Plastic Concentration in the Ocean

<!-- b000003 | heading | pages [1] -->
Problem and Introduction

<!-- b000004 | prose | pages [1] -->
Ocean (the Pacific Ocean, in particular) debris has proved to be new to the scientific community. Yet, it is quite similar to common marine litter problems in that it is an environmental, economic and health problem (UNEP, 2009). Moreover, ocean debris often causes dangers to marine organisms ranging from sea birds to sea mammals and filter eaters through ingestion and entanglement (Day, 1980) and thus breaks the balance of ocean ecosystem.

<!-- b000005 | prose | pages [1] -->
Previous studies have addressed the impacts of debris on birds, fish and filter-feeding organisms. However, few studies have recognized that while affecting the ocean ecosystem, ocean debris itself is also changing dynamically in the sense of mass concentration due to both human inputs and nature forces (mainly, physical abrasion and chemical photolysis).

<!-- b000006 | prose | pages [1] -->
Furthermore, although many studies have acknowledged the fact that marine organisms usually fail to distinguish between debris and their food (C. J. Moore, 2001), no studies have specifically considered the effects of different sizes of debris on different marine organism. The fact that marine organisms eat various sizes of food makes it important to classify the sizes of debris because marine organisms’ abilities to distinguish between debris and food depend on the size of the debris.

<!-- b000007 | prose | pages [1] -->
Therefore, this model studies the dynamic and classified system of ocean plastics to better understand how exactly human behaviors over time affect ocean ecosystem.

<!-- b000008 | prose | pages [1] -->
For the purpose of this model, ocean debris is simply referred as “Plastic” since plastics are the major components of debris (UNEP, 2009). Also, this model uses the North Pacific Central Gyre area as a sample for further discussion.

<!-- b000009 | prose | pages [1] -->
Classified Plastic Concentration Model

<!-- b000010 | prose | pages [1] -->
Plastic Input Ocean plastics are mainly results of human behaviors (UNEP 2009). There are two categories often used to classify sources of ocean plastics depending on their origins: land-based sources (LB) and sea-based sources (SB). Land-based sources primarily compose of consumer and industry plastic products wastes/dumps which are carried through the inland water system to the ocean.

<!-- b000011 | prose | pages [1] -->
Also, the types of plastic also vary over different sources. Based on the Leontief model, the source- coefficient matrix for this model is as the followings: Sources Plastic Wastes Inputs Type1  Type2  Type3 … TypeN C a11           a12        a13     …    a1n I a21           a22        a23   …    a2n S a31       a32        a33   …    a3n F a41       a42        a43   …    a4n

<!-- b000012 | caption | pages [1] -->
Table 1. Source-coefficient matrix. C: plastic source from

<!-- b000013 | prose | pages [1] -->
consumers; I: plastic source from industries; S: plastic source from shipping; F: plastic source from fishing.

<!-- b000014 | prose | pages [1] -->
Then, the following linear model is made on the mass of land-based plastic wastes at time t: PLBt=α1+α2Pct+α3Pit+µ1 … (1), where, for a given time t, PLBt stands for the mass of land-based plastic wastes; Pct and Pit stand for the mass of consumer plastic products and industry plastic products respectively; α1 is the intercept and α2, α3 the coefficients; µ1 is an error item that represents the total influence of all other related factors.

<!-- b000015 | prose | pages [1] -->
Shipping and fishing are the major sea-based sources of plastic wastes. Based on this, the sea-based plastic wastes model is expressed as: PSBt=β1+β2Pst+β3Pft+ µ2 … (2), where, similar to the land-based plastic wastes model, PSBt stands for the mass of sea-based plastic wastes; Pct and Pit stand for the mass of plastic products consumed by shipping and fishing respectively; β1 is the intercept and β2, β3 the coefficients; µ2 is the same as µ1.

<!-- b000016 | prose | pages [1] -->
Next, this model names the ocean area to study as the Area of Interest (AOI). The inputs of plastic wastes could simply be the combination of land-based and sea- based sources. However, the problem of ocean plastics involves another issue related with ocean geography (ocean current, in particular) that causes dispersion and deposition of plastics. Here is our approach to this problem.

<!-- b000017 | prose | pages [1, 2] -->
Any ocean area rather than our interested area AOI is defined as “Outside Area (OA)”. Due to the effect of ocean current, there must be already-existed debris exchange (both in and out) between AOI and OA. For the purpose of our model, however, this model assumes that such exchange is balanced. In another words, the input from OA to AOI and the output from AOI to OA are the same in total mass.

<!-- b000018 | furniture | pages [2] -->
TEAM # 7812                                                                                                                                                                  2 / 10

<!-- b000020 | prose | pages [2] -->
Also, regarding the dispersion and deposition of plastics happened when land-based and sea-based sources input to AOI, this model incorporates a new factor λ and name it “Ocean Geography Factor (OGF)”. λ represents the affected accumulative proportional mass of plastics wastes sources that is not transported into AOI due to various ocean geographical factors including ocean currents, tidal cycles, regional-scale topography, including sea-bed topography and wind (UNEP 2009).

<!-- b000021 | prose | pages [2] -->
Therefore, this model only considers the effect of fresh land-based plus sea-based sources of plastics wastes as inputs to our AOI. See Figure 1 below.

<!-- b000022 | prose | pages [2] -->
Plastic Inputs

<!-- b000023 | prose | pages [2] -->
Human

<!-- b000024 | prose | pages [2] -->
Sea-Based Land-Based

<!-- b000025 | prose | pages [2] -->
Unaffected Proportion Affected Proportion (1-λ) λ

<!-- b000026 | prose | pages [2] -->
AOI OA Balance

<!-- b000027 | caption | pages [2] -->
Figure 1. Plastic inputs.

<!-- b000028 | prose | pages [2] -->
The plastic input model is then, I= PLBt (1-λ1) + PSBt (1-λ2) … (3), where I means inputs of ocean plastic debris to AOI; PLBt stands for the mass of land-based plastic wastes; PSBt stands for the mass of sea-based plastic wastes; 1-λ1 stands for the proportion of PLBt unaffected by ocean geography, and 1-λ2 the proportion of PSBt unaffected by ocean geography.

<!-- b000029 | prose | pages [2] -->
Individual Plastic Object The physical abrasion and chemical photolysis of plastic objects are important factors in the discussion of the concentration of plastic in the ocean. The transformation of an individual plastic object in the ocean is discussed in this part.

<!-- b000030 | prose | pages [2] -->
Assume the size of an arbitrary plastic object in the ocean at time t is S(t), whose initial size at time t=0 is S0. The size of the object decreases by a proportion r1 of its initial size because of the physical abrasion and a proportion r2 because of the chemical photolysis per unit time (say 1 year).

<!-- b000031 | prose | pages [2] -->
According the assumptions stated above, the dS ( t ) following relation can be made: …     S ( t ) ( r r ) 1 2 dt (4). With the initial condition: S(0) = S0. Equation (4) is solved to get the expression:

<!-- b000032 | prose | pages [2] -->
   ( r r ) t S ( t ) S e …  (5). 1 2 0 To interpret the chemical decay rate r2, the physical abrasion rate r1 is set to 0. Equation (5), then,   r t S ( t ) S e becomes: . Calculate the half life of the 2 0 plastic object studied by taking S(t) = ½S0, t=t1/2, then t1/2 ln 2  is expressed as . This happens to be the t 1 / 2 r 2 expression for the half time of photolysis and r2 happens to be in the place of the rate constant Kp of photolysis reactions. Therefore, r2 can be interpreted as the reaction rate of photolysis on plastics. On the other hand, there is no direct relationship between r1 and a physical quantity.

<!-- b000033 | prose | pages [2] -->
The Classification of the Sizes of Plastic Objects One of the main purposes of studying the concentration of plastic objects in the ocean is to estimate their influence to marine organisms. Therefore, the sizes of the plastic objects are of essential interest. The objects have the most significant influence to a particular kind of animal when their sizes are in the range of that kind of animal’s food size.

<!-- b000034 | prose | pages [2] -->
The sizes of plastic objects are divided into four ranges or categories as listed below:

<!-- b000035 | prose | pages [2] -->
n3s - n4s Level 1 bottles, bags, fishing nets, etc. n2s - n3s Level 2 cigarette filters, fragments, etc. ns - n2s Level 3 visible dust Level 4 s – ns polymer molecules

<!-- b000036 | caption | pages [2] -->
Table 2. Category of the Sizes of Plastics.

<!-- b000037 | prose | pages [2] -->
Because the decay of the objects is exponential according to Equation (5), the ranges are made exponentially equivalent.   In Table 1, s is the smallest size of a particle that can be called plastic; n is a common constant factor. The magnitudes of s and n are to be determined later.

<!-- b000038 | prose | pages [2, 3] -->
With the categorization of plastic objects in Table 1, the time for an object to decay from the maximum of level i to the maximum of level i+1 and the time for an object to decay from the minimum of level i to the minimum of level i+1 would be the same. This implies that, if at time t0 there are x particles in Level i, there is a time m after which all the x particles are in level i+1.The time interval m is calculated by Equation (6):

<!-- b000039 | furniture | pages [3] -->
TEAM # 7812                                                                                                                                                                  3 / 10

<!-- b000041 | prose | pages [3] -->
ln n  1   ( r r ) m 2 ns n s e … (6), which gives: … 2  m  r r 1 2 (7). Assume the size (and thus the mass and concentration) of a given amount of plastic objects decays to lower size levels at a constant rate. Then, for any infinitesimal time interval dt, the amount of particles transfer from Level i to Level i+1 can be expressed as:

<!-- b000042 | prose | pages [3] -->
Ci , where Ci is the concentration (mass/ area) of all  dt m objects in size Level i.

<!-- b000043 | prose | pages [3] -->
Derivation of the Concentration vs. Time Relation Four differential equations are derived for the concentration of objects in the four size levels as follows: dC C       … (8); 1 1 I ( r r ) C , C ( 0 ) C 1 1 2 1 1 10 dt m dC C C … (9);        2 1 2 I ( r r ) C , C ( 0 ) C 2 1 2 2 2 20 dt m m dC C C … (10);          I r ( C C ) r C , C ( 0 ) C 3 2 3 3 1 1 2 2 3 3 30 dt m m dC C C … (11).       r ( C C C ) ,' C ( 0 ) C 4 3 4 2 1 2 3 4 40 dt m m In Equations (8), (9), (10) and (11), Ci represents the mass concentration of plastic objects of size level i in the Area of Interest (AOI). Ci(0) gives the initial conditions of the differential equations. r1 and r2 are the decay rates of the objects and m is the time for all objects in one size level to decay to the lower size level. I is a new variable that represents the concentration of the plastic input into the area of interest by means of human activities. The expressions for I have been derived in the plastic inputs part above.

<!-- b000044 | prose | pages [3] -->
The physical meaning of Equation (8) is: The rate of change of the Level 1 concentration is the sum of the rate of input, the rate of decaying to Level 2 and the rate of loss by physical and chemical reactions. To be more clear, the assumption is made so that the main part of an initial object will decay to objects of the next level, the particle loss by physical reaction will contribute to the increase of the mass concentration of level 3 and the particle loss by the chemical reaction will contribute to the increase of the mass concentration of level 4.

<!-- b000045 | prose | pages [3] -->
Similarly, the rate of change of the Level 2 concentration is the sum of rate of input, the rate of reception from Level 1, the rate of decay to Level 3 and the rate of physical and chemical particle loss.

<!-- b000046 | prose | pages [3] -->
The rate of change of the concentration of Level 3 is the sum of the rate of input, the rate of reception from Level 2, the rate of contribution from the physics abrasion of Level 1 and 2, the rate of decay to Level 4 and the rate of chemical lost. In this level, the physical abrasion may or may not function in the decay of objects. For the simplicity of the equation, the decay time from Level 3 to Level 4 is approximated to still be m.

<!-- b000047 | prose | pages [3] -->
The rate of change of the Level 4 concentration is the sum of the rate of reception from Level 3, the rate of contribution from the chemical loss of Level 1, 2 and 3 and the rate of decay to non-polymer or harmless molecules. Here, another coefficient m’ is involved to represent the average time for a particle of size in Level 4 to decay to non-polymer or harmless molecules. Also, assume there are no incoming particles at the molecule size level directly from human activities.

<!-- b000048 | prose | pages [3] -->
Equation (8), (9), (10), (11) gives the equation dC dC dC dC C … (12).        3 1 2 4 4 I I I 1 2 3 dt dt dt dt m ' Regarding the four size levels as a system, the rate of change of the whole system concentration is just the rate of total input minus the rate the plastic polymer decay to harmless particles.

<!-- b000049 | prose | pages [3] -->
Mass Concentration as a Function of Time The solutions for Equation (8), (9), (10) and (11) are listed below in order. They are expressions of the mass concentration of objects of certain size levels in the area of interest as a function of time.

<!-- b000050 | prose | pages [3] -->
  1    ( r r ) t   1 2    … (13); m C I t C e 1 1 10   1   C    ( r r ) t   1 2     m   … (14); 1 C I t C e 2 2 20 m   1   C     r t 2       … (15);   m 2 C I r ( C C ) t C e   3 3 1 1 2 30 m   1   C   t … (16).       m ' 3 C r ( C C C ) t C e   4 2 1 2 3 40 m In the expressions, the only variable is time t. However, the constants I1, I2, I3, m, m’, r1, r2 depend on the environmental and industrial situation and make the equations flexible enough to deal with particular situations on a case by case basis. Each of the four expressions is a combination of a linearly increasing term and an exponentially decay part.

<!-- b000051 | furniture | pages [4] -->
TEAM # 7812                                                                                                                                                                  4 / 10

<!-- b000052 | prose | pages [4] -->
The behavior of the concentrations along time will depend on which of the two terms overweigh the other. Roughly speaking, the larger the plastic input I is, the more weighed the first term; the larger the decay rates r1 and r2 (which result in a larger 1/m), the more weighed the second term. In a relatively short term fashion, the behavior will be linear increase dominated, exponential decay dominated or a combination of both. This behavior will be of important interest for the prediction of the situation of the ecosystem. In a long term fashion, the concentrations will show a linearly increasing pattern whatever constants are chosen, which limits the model’s abilities to describe the long term run of the system of interest. This limitation will be discussed in the “Limitation” section.

<!-- b000053 | heading | pages [4] -->
Discussion and Results

<!-- b000054 | prose | pages [4] -->
Ranges and Initial Values of Variables

<!-- b000055 | prose | pages [4] -->
Size Levels of Plastic Object The sizes of plastic objects are classified for studying their influence for certain groups of organisms. Therefore, the numerical ranges four size levels, i.e., constant n and s, are determined by the diet of organisms feeding on marine sources.

<!-- b000056 | prose | pages [4] -->
Filter feeders feed on planktons, the length range of which is 2*10-7m to 1*10-3m. Assign to this level the size range 5*10-6m-5*10-4m, which represents the size of majority planktons. Thus gives ns=5*10-6m and n2s=5*10- 4m. The food of small birds and fishes fits in the next level of n2s-n3s or 5*10-4m-5*10-2m (5cm). The food of large marine mammals, large birds and fishes fits in Level 1, which is 5*10-2m-5m. Level 4 (5*10-8m-5*10-6m) is considered the size molecules and small polymers. This size level is hardly related to the size of food of any marine organisms of interest.  Because plastic in Level 4 has no particular influence to any organisms and its concentration in the marine system is very low (e.g.

<!-- b000057 | prose | pages [4] -->
10 kgPlastics 1 ), its poisoning effect  3 1   3 11 1000 kgm km water 10 is ignored in this model. Level Diameter Corresponding Feeder Range 5*10-2-5 1 big large mammal & bird 5*10-4-5*10-2 2 middle small bird, fish, turtle 5*10-6-5*10-4 3 small filter feeder 5*10-8-5*10-6 4 tiny N/A

<!-- b000058 | caption | pages [4] -->
Table 3. Size Level in Length (m).

<!-- b000059 | prose | pages [4] -->
Level Volume Range Corresponding Feeder 1.25*10-4-1.25*102 1 large mammal & bird 1.25*10-10-1.25*10-4 2 small bird, fish, turtle 1.25*10-16-1.25*10-10 3 filter feeder 1.25*10-22-1.25*10-16 4 N/A

<!-- b000060 | caption | pages [4] -->
Table 4. Size Level in Volume (m3).

<!-- b000061 | prose | pages [4] -->
Thus constant n=106, s=1.25*10-22m3.

<!-- b000062 | prose | pages [4] -->
The Initial Mass Concentration of Plastics According to Moore, C.J. et al, 2001, the mass concentration of plastic 4.8*10-3m-3.5*10-4m in North Pacific Central Gyre is 5.1kg/km2. The size range is roughly half of that of size Level 2 in our model. Assume, then, C20=10kg/km2. To study and compare the concentration of objects in all four size levels, assume also that C10=C20=C30=C40=10kg/km2. Because the main focus is the change of the concentration instead of the original content, the values of C10, C20, C30, and C40 are not going to be varied in later discussion.

<!-- b000063 | prose | pages [4] -->
The Physical Abrasion and Photolysis Rate Studies have shown that complete decay of plastic in the ocean varies from 10-20 years to 450 years. Material Degradation Rate (year) plastic bag 10-20 commercial netting 30-40 foamed plastic buoy 80 plastic beverage bottle 450

<!-- b000064 | caption | pages [4] -->
Table 5. Degradation rates of different plastic products in

<!-- b000065 | prose | pages [4] -->
the marine environment.

<!-- b000066 | prose | pages [4] -->
Because most plastics are non-biodegradable, this model assumes the entire disappearance of plastic is due to photolysis process. Take 100 years as a standard, then the average life time τ is 100 yrs. ln 2 … (17). By … (18), get    t  t ln 2 69 3. yrs 1 1 r 2 2 2 r2=1%. Then let time interval of decay between two size levels m=100 yrs. This estimation is justified because an 1 object would decay to of its original size, which is 6 10 viewed as disappearance in this case. Assume r1=r2 (justified in “The Effect of Photolysis Rate” section), then, r2=6.9%. A rough range of decay rate is 1% ≤ r1=r2 ≤ 6.9%.

<!-- b000067 | prose | pages [4, 5] -->
The Effect of Input on Plastic Concentration Plastic input into the ocean can come in different size levels. With respect to the influence of the input on the concentration of plastic, two topics are explored. The first topic is the relationship between the absolute rate of input and the plastic concentration; the second topic is the influence of the distribution of the input over sizes on the concentration. Make the following assumptions: C10=C20=C30=C40=10kg/km2, r1=r2=5%/yr (within in the range of 1%-6.9%). Then, the time interval of decay 6 ln 10 between two size levels is .   m 138 yrs  r r 1 2

<!-- b000068 | furniture | pages [5] -->
TEAM # 7812                                                                                                                                                                  5 / 10

<!-- b000070 | prose | pages [5] -->
Effect of the Absolute Input Rate During a 100-year period, assume plastic input only comes in size Level 1 (input consist of different sizes will be discussed later), I2=I3=0. Then, the concentration trend of plastics of the 1st, 2nd, and 3rd levels with different input rates are compared in the curves C1 (t), C2 (t), and C3 (t).

<!-- b000071 | caption | pages [5] -->
Figure 2. Predicted concentration change of Level 1

<!-- b000072 | prose | pages [5] -->
plastic under various Size 1 input (I1=1, 0.1, 0.001kg/km2yr).

<!-- b000073 | caption | pages [5] -->
Figure 3. Predicted concentration change of Level 2

<!-- b000074 | prose | pages [5] -->
plastic under various Size 1 input (I1=1, 0.1, 0.001kg/km2yr).

<!-- b000075 | caption | pages [5] -->
Figure 4. Predicted concentration change of Level 3

<!-- b000076 | prose | pages [5] -->
plastic under various Size 1 input (I1=1, 0.1, 0.001kg/km2yr).

<!-- b000077 | prose | pages [5] -->
When the input is small enough (0.001), the concentration curves of all the three levels show a pattern of exponential decay, this kind of pattern is ideal when the high value of concentration is undesirable. A maximum input can be obtained, then, which keeps the concentration decaying during a long enough time. On the other hand, when the input is extremely big (1), the concentration experience a very short decay time, if it decays at all, and then increase with a high speed. This is extremely undesirable. With an input rate (0.1) between them, the concentration value will not flow up significantly in the time interval of interest. It is important to note that long term increase of concentration may or may not follow a short term of decrease.

<!-- b000078 | prose | pages [5] -->
Compare among the behavior of C1, C2 and C3 with the same input rate, C3 always flows up most rapidly. This indicates that the organisms whose food is in Level 3 will probably be the most vulnerable.

<!-- b000079 | prose | pages [5] -->
In conclusion, the input amount exerts a determining effect on plastic concentration of all sizes. Only input under certain amount will lead to continuous decrease of plastic concentration.

<!-- b000080 | prose | pages [5, 6] -->
Effect of the Distribution of Input Pre-dump physical treatment of plastic, e.g., grinding can result in different plastic input component. Let D1, D2, D3 denote three distributions of plastic input: totally size Level 1 (no physical treatment), totally size Level 2 (grind plastic to size Level 2), and equally mixture of size Level 1 & 2 (grind half plastic input) respectively. The yield of Level 3 plastic waste is physically uncontrollable, so is not discussed here.

<!-- b000081 | furniture | pages [6] -->
TEAM # 7812                                                                                                                                                                  6 / 10

<!-- b000083 | prose | pages [6] -->
The effect of the three distribution of input is displayed on Figure 5, 6 and 7.

<!-- b000084 | caption | pages [6] -->
Figure 5. Predicted concentration change of Level 1

<!-- b000085 | prose | pages [6] -->
plastic under different distribution of input (D1, D2, D3).

<!-- b000086 | caption | pages [6] -->
Figure 6. Predicted concentration change of Level 2

<!-- b000087 | prose | pages [6] -->
plastic under different distribution of input (D1, D2, D3).

<!-- b000088 | caption | pages [6] -->
Figure 7. Predicted concentration change of Level 3

<!-- b000089 | prose | pages [6] -->
plastic under different distribution of input (D1, D2, D3).

<!-- b000090 | caption | pages [6] -->
Figure 8. Predicted change of the total plastic

<!-- b000091 | prose | pages [6] -->
concentration under different distribution of input (D1, D2, D3).

<!-- b000092 | prose | pages [6] -->
The plastic concentration of different size is affected by size distribution of input. For size Level 1 & 3 plastic, treated input (D2) leads to least concentration increasing. However for Size Level 2 plastic, untreated input (D1) leads to least concentration increasing. The total plastic concentration also favors input of size Level 2 (treated input) only. However, for the sake of the total plastic concentration to be minimized, D2 is not the optimized point. The optimized input solution should be one with most input in size Level 2 and a little in size Level 1.

<!-- b000093 | prose | pages [6] -->
The Effect of Photolysis Rate r2 on Plastic Concentration

<!-- b000094 | prose | pages [6, 7] -->
Factors Affect Photolysis Rate r2 Plastic polymers that are vastly used in daily life and industry are mostly non-biodegradable. After been disposed into the marine system, plastics are mainly subject to physical abrasion and photolysis process whose rates are r1 and r2 respectively. Physical abrasion result from friction and impassive abrasion. Impassive abrasion is non-predictable and can be ignored if plastics are carried by current in open sea. Both fluvial friction abrasion and photolysis rate are very small. Therefore we suppose physical abrasion rate is constant and same as photolysis rate. Photolysis rate is determined by the  d [ P ]    k [ P ] I equation … (19) where [P] is p r a dt plastic concentration, Kp is photolysis rate constant, i.e., r2, Φr is the quantum yield for reaction Ia is the sunlight absorption rate.

<!-- b000095 | furniture | pages [7] -->
TEAM # 7812                                                                                                                                                                  7 / 10

<!-- b000097 | prose | pages [7] -->
Quantum yield Φr is the number of molecules transformed by absorbing light divided by total number of molecules that absorb light. This parameter is dependent on the chemical property of polymer thus varies by plastic type.

<!-- b000098 | prose | pages [7] -->
Sunlight absorption rate Ia is calculated by    I L …(20) where εw is the molar extinction a w w coefficient of the plastic at wavelength w and is determined by plastic type, Lw is determined by day- average sunlight intensity and calculated for solar radiation from 280-800nm at various latitude. The lower sunlight intensity of area of interest is, the slower the decay rate of plastic, the bigger size of remaining plastic.

<!-- b000099 | prose | pages [7] -->
Comparative Effect of r2 and I on Plastic Concentration The effect on plastic concentrations of input I and photolysis rate r2 have been discussed in previous sections separately. In this section, their influences are compared to determine which one is overarching.

<!-- b000100 | prose | pages [7] -->
According to estimation, the average photolysis rate should be 1%/yr-6.9%/yr. However, r2 not only depends on uncontrollable factor such as sunlight intensity, but also controllable factor such as plastic type. Some plastic product can decay completely within 20 years while others take up to 450 years. Thus decay rate can be more flexible than input amount and distribution. Assume the physical abrasion rate is held constant at 5%/yr. Take 0.1kg/km2yr as the central point and choose the range of input concentration to be 0.08kg/km2yr- 0.12kg/km2yr. Taking technology advancement and temporal decrease in concentration at 20-25 years (Figure 2), 30 years since now would be a reasonable time point to compare impact of photolysis rate and input and a photolysis rate r2 up to 15%/yr. can be assumed. Suppose all input are of Size Level 1 plastic only (I1). At 30th year time point, concentrations of plastics of various photolysis (1%-15%) rate under a range input can be predicted by plotting C1 (I1, r2), C2 (I1, r2), and C3 (I1, r2).

<!-- b000101 | caption | pages [7] -->
Figure 9. Predicted concentration change of Level 1

<!-- b000102 | prose | pages [7] -->
plastic with photolysis rate of 1%/yr-15%/yr under input 0.08kg/km2yr-0.12kg/km2yr.

<!-- b000103 | caption | pages [7] -->
Figure 10. Predicted concentration change of Level 2

<!-- b000104 | prose | pages [7] -->
plastic with photolysis rate of 1%/yr-15%/yr under input 0.08kg/km2yr-0.12kg/km2yr.

<!-- b000105 | furniture | pages [8] -->
TEAM # 7812                                                                                                                                                                  8 / 10

<!-- b000106 | caption | pages [8] -->
Figure 11. Predicted concentration change of Level 3

<!-- b000107 | prose | pages [8] -->
plastic with photolysis rate of 1%/yr-15%/yr under input 0.08kg/km2yr-0.12kg/km2yr.

<!-- b000108 | prose | pages [8] -->
Of all size level plastics, the influence on plastic concentration by photolysis rate decrease exponentially as photolysis rate increases while that of input undergoes a steady linear increase as input increases.

<!-- b000109 | prose | pages [8] -->
Compared among Figure 9, 10, and 11, the photolysis rate has a relative large influence on concentration of Size Level 2 plastics than on Size Level    C C C   2 3 1 1 & 3 plastics. In other words, …    r r r 2 2 2 (21). The change in the influence of r2 decreases as r2 gets   C C  ( a ) ( b ) i i bigger, which is … (22) when a<b.   r r 2 2 For all three levels, there is one or several equilibrium   Ci Ci  points which gives … (23). These points are   r I 2 1 important in policy determinations. Specifically, within the range of approximately 1%/yr-7%/yr, concentration of Size Level 2 plastic decrease dramatically as photolysis rate increases while decrease slightly as input decreases.

<!-- b000110 | prose | pages [8] -->
Limitations

<!-- b000111 | prose | pages [8] -->
The major limitation of this model is its inability to describe the long term behavior of the system. Take   1    ( r r ) t   1 2    Equation (13) as an example. m C I t C e 1 1 10 As t increases, the term I1t will keep on increasing linearly independent of the rate of decay and other terms. This makes the problem of pollutions seems to be unsolvable in a long term run. A restrictive term is needed to limit the increase the term I1t and other input terms. For example, manipulate I1t to I1f (t), in which f (t)’s slope decreases as t increases. However, the long term behavior is relatively not interesting in this problem because all the situations, like the production of plastic, the recycle technology or even the marine environment, will be quite different after a relatively long time. The model still works fairly well in a short time, say 30-50 years, with the reasonable choices of coefficients.

<!-- b000112 | prose | pages [8] -->
There are a series of other limitations. First, the physical abrasion rate of plastic objects is not modeled satisfactorily due to a lack of relevant information. Second, the sizes of plastic objects are classified so that the exponential range of each level is the same. That is, the maximum of each level is a certain multiple of the minimum of that level. The size levels cannot match perfectly with the food levels of marine animals. However, the distinctions are not significant. Third, the toxicity of plastic molecules in sea water is ignored in the model because there mass concentration is very small. It is possible that the toxicity may have unknown influence to marine organisms in spite of its low concentration.

<!-- b000113 | prose | pages [8] -->
The model can be improved by: (i) study the behavior of the system at infinities; (ii) dig more into the mechanism of the physical and chemical reactions of plastic; (iii) explore a more reasonable way to classify the sizes of plastic objects; (iv) explore the toxicity of plastic molecules and the release of such toxicity.

<!-- b000114 | prose | pages [8] -->
Implications and Advices

<!-- b000115 | prose | pages [8] -->
Referring to Table 3, for the purpose of further discussion, this model defines the marine organisms corresponding to plastic object size level 1 as “O1”. Similarly, the marine organisms related with size level 2, 3 and 4 are referred as O2, O3 and O4.

<!-- b000116 | prose | pages [8] -->
Geographical Influence From the results of sunlight intensity and decay rate study, sunlight intensity and decay rate have positive relationship. More specifically, at places with lower sunlight intensities, the quantity of large plastic objects (C1) is likely to be more than the smaller ones (C2, C3 and C4), vice versa because the decay rate is slower.

<!-- b000117 | prose | pages [8] -->
Although sunlight intensity is determined by many geographical factors such as rainfall and latitude, it is useful to discuss the effects of one factor and hold all others constant. In this model, latitude is chosen based on the fact that sunlight intensity is higher in low latitude areas and lower in high latitude areas given all other variables constant.

<!-- b000118 | prose | pages [8] -->
Therefore, the implication here is that in high latitude areas there are mainly large size plastic objects because of a lower decay rate.

<!-- b000119 | prose | pages [8] -->
As a result, organisms O1 will be largely impacted. The advice is to set up effective ocean cleaning plans especially in high latitude areas.

<!-- b000120 | prose | pages [8] -->
Plastic Inputs

<!-- b000121 | prose | pages [8, 9] -->
Inputs and Concentration (General) Based on Figure 2, 3, and 4, it is verified that any increase in the plastic inputs would cause increase of mass concentration in all size levels of plastic objects in the ocean, or in another words, the relationship between plastic inputs and mass concentration is always positive. Thus, in general, no increase of either land-based or sea- based plastic sources is recommended.

<!-- b000122 | furniture | pages [9] -->
TEAM # 7812                                                                                                                                                                  9 / 10

<!-- b000124 | prose | pages [9] -->
Because the plastic inputs affect the ocean plastics in all levels in all times, it is advisable for governments to use regulations or plastic waste tax tools for both land-based and sea-based sources.

<!-- b000125 | prose | pages [9] -->
Indicator The results also show that the mass concentration of Level 3is a good indicator of the classified plastic system in the ocean because holding the inputs constant, the mass concentration of Level 3 is the most responsive to change.

<!-- b000126 | prose | pages [9] -->
Monitoring the mass concentration of Level 3 thus provides good indicates the balance of the whole ecosystem because the loss of vulnerable O3 easily breaks the system.

<!-- b000127 | prose | pages [9] -->
“Illusion” Another important implication from the results is that once inputs reduced, the mass concentration of plastic objects decreases in short-term but has the potential to rise again in long-term (refer to Figure 2, 3, and 4).

<!-- b000128 | prose | pages [9] -->
Therefore, it is vital for governments to undertake monitoring plans constantly and continuously in order to understand the real situation. Simply speaking, do not get “happy” too early by the “illusion”.

<!-- b000129 | prose | pages [9] -->
Input Control This model could be used to find the maximum of plastic inputs for a certain purpose of protecting any group of organisms once data are given.

<!-- b000130 | prose | pages [9] -->
With a limit on inputs, it is easy for governments to use the already established plastic inputs parts to control the 4 main sources, consumer (land-based), industry (land-based), shipping (sea-based) and fishing (sea-based).

<!-- b000131 | prose | pages [9] -->
Plastic Wastes Pre-Dump Treatment According to the results of this model, the best treatment types (D1, D2 and D3) for minimizing the mass concentration of plastic objects at each size level is as the following: Level 1 Total-Treatment (D2) Level 2 No-Treatment (D1) Level 3 Total-Treatment (D2) Total Total-Treatment (D2)

<!-- b000132 | caption | pages [9] -->
Table 6. Pre-dump Treatment and Concentration

<!-- b000133 | prose | pages [9] -->
This table implies 3 things: (i) for the purpose of protecting both organism O1 and O3, total-treatment before plastic waste dump is the best choice; (ii) for the purpose of protecting organisms O2 no-treatment of plastic wastes input would be a better choice, which is counter-intuitive; (iii) for the purpose of protecting the ocean ecosystem as a whole, the preferable plan is to give more than 50% of the plastic wastes total-treatment.

<!-- b000134 | prose | pages [9] -->
The suggestion for government based on this implication is that controlling the plastic wastes pre-dump treatment is efficient for different ocean organism protection purposes. If, with no specific target organism group to protect, it is suggested for governments to carry out mandatory order on the plastic wastes pre-dump treatment to protect the ocean ecosystem as a whole.

<!-- b000135 | prose | pages [9] -->
Photolysis vs. Input This model shows that for level 2 (30-year time period), the influence of photolysis overwhelms the influence of input. Thus, it implies that for the purpose of protecting organisms O2, it is better to focus on how to increase the effect of photo rate of plastics.

<!-- b000136 | prose | pages [9] -->
At the same time, the approach to protecting organisms O1 and O3 depends on the current level of plastic quality (we define plastics with higher qualities have higher photolysis rate). If the average quality is high enough so that the influence of photolysis is rather little compared to the influence of inputs, then it is better to focus on how to limit inputs and vice versa.

<!-- b000137 | prose | pages [9] -->
Thus, this implication proposes to the government that when the average quality of plastic is low, encouraging easily-degradable materials for plastic products is more effective than restricting plastic wastes inputs; and when average quality of plastic is high, it is better to focus on restricting plastic wastes inputs.

<!-- b000138 | heading | pages [9] -->
References:

<!-- b000139 | references | pages [9] -->
A Comparison of Plastic and Plankton in the North

<!-- b000140 | references | pages [9] -->
Pacific Central Gyre. Marine Pollution Bulletin. 42

<!-- b000141 | references | pages [9] -->
(2001): 464-488. The Interdisciplinary Contest in

<!-- b000142 | references | pages [9] -->
Modeling. Lawrence University., Appleton, Seeley G.

<!-- b000143 | references | pages [9] -->
Mudd Library. 21 Feb. 2010.

<!-- b000144 | furniture | pages [10] -->
TEAM # 7812                                                                                                                                                                  10 / 10

<!-- b000145 | references | pages [10] -->
<http://www.comap.com/undergraduate/contests

<!-- b000146 | references | pages [10] -->
/mcm/contests/2010/problems/ICM_2010.pdf>

<!-- b000147 | references | pages [10] -->
Azzarello, Marie Y. and Edward S. Van Vleet. “Marine

<!-- b000148 | references | pages [10] -->
Birds and Plastic Pollution.” Marine Ecology. 37

<!-- b000149 | references | pages [10] -->
(1987): 295-303.

<!-- b000150 | references | pages [10] -->
Cadée, Gerhard C. “Seabirds and floating plastic debris.”

<!-- b000151 | references | pages [10] -->
Marine Pollution Bulletin. 44 (2002): 1294-1295.

<!-- b000152 | references | pages [10] -->
Science Direct. Lawrence University., Appleton,

<!-- b000153 | references | pages [10] -->
Seeley G. Mudd Library. 21 Feb. 2010.

<!-- b000154 | references | pages [10] -->
<http://www.sciencedirect.com/science?_

<!-- b000155 | references | pages [10] -->
b=ArticleURL&_pvudi=B6V6N-45X2MG4-

<!-- b000156 | references | pages [10] -->
J&_rdoc=11&_alid=1214142569&_user=9000194&

<!-- b000157 | references | pages [10] -->
_fmt=high&_orig=search&view=c&_ct=1677&_sort

<!-- b000158 | references | pages [10] -->
=r&_acct=C000050381&_version=1&_urlVersion=0

<!-- b000159 | references | pages [10] -->
&_userid=9000194&md5=eba56d418830debdcb5da

<!-- b000160 | references | pages [10] -->
6c5c711a487>.

<!-- b000161 | references | pages [10] -->
Day, R. H. The Occurrence and Characteristics of Plastic

<!-- b000162 | references | pages [10] -->
Pollution in Alaska’s Marine Birds. M.S. Thesis,

<!-- b000163 | references | pages [10] -->
University of Alaska. Fairbanks, AK, 111pp. 1980.

<!-- b000164 | references | pages [10] -->
Macalady, Donald, ed. Perspectives in Environmental

<!-- b000165 | references | pages [10] -->
Chemistry. New York Oxford: Oxford University

<!-- b000166 | references | pages [10] -->
Press, 1998.

<!-- b000167 | references | pages [10] -->
O'Hara et al., A Citizen Guide to Plastics in the Ocean:

<!-- b000168 | references | pages [10] -->
More Than A Litter Problem. Washtington, D.C.:

<!-- b000169 | references | pages [10] -->
Centre for Environmental Education, 1988.

<!-- b000170 | references | pages [10] -->
“Plankton Definitions.” Soil & Water Conservation

<!-- b000171 | references | pages [10] -->
Society of Metro Halifax. 21 Feb. 2010.

<!-- b000172 | references | pages [10] -->
<http://www.chebucto.ns.ca/ccn/info/Science/SWCS/

<!-- b000173 | references | pages [10] -->
plankton.html>.

<!-- b000174 | references | pages [10] -->
US Congress, Office of Technology Assessment, Wastes

<!-- b000175 | references | pages [10] -->
in Marine Environments. OTAO-334 Washington,

<!-- b000176 | references | pages [10] -->
DC: U.S. Government Printing Office, April 1987.

<!-- b000177 | references | pages [10] -->
United Nations Environment Programme, Regional   Seas

<!-- b000178 | references | pages [10] -->
Programme. “Guidelines on the Use of Market-based

<!-- b000179 | references | pages [10] -->
Instruments to Address the Problem of Marine Litter.”

<!-- b000180 | references | pages [10] -->
2009.

<!-- b000181 | references | pages [10] -->
United Nations Environment Programme, Regional Seas

<!-- b000182 | references | pages [10] -->
Programme. “Marin Litter: A Global Challenge.”

<!-- b000183 | references | pages [10] -->
April 2009.
