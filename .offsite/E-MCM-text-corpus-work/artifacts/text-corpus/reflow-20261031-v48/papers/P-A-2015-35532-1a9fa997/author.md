For office use only For office use only T1 ________________ F1 ________________ T2 ________________ F2 ________________ T3 ________________ F3 ________________ Problem Chosen T4 ________________ F4 ________________

Summary

The complex epidemic of Zaire ebolavirus has been affecting West Africa. A series of realistic, sensible, and useful mathematical model about Ebola of spreading and medication delivery are developed to eradicating Ebola.

First, we divide the spreading of disease into three periods: naturally spreading period, spreading period with isolation but without effective medications and spreading period with effective medications. We develop a SEIR (susceptible-exposed-infectious-recovered) model to simulate the spread of the disease in the primary period. Then the model are improved to a SEIQR (susceptible-exposed-infectious-quarantined-recovered) model to adapt to the second and third period and to predict the future trends in Guinea, Sierra Leone and Liberia.

According to our plan, drugs are delivered to countries in need separately by air, then to medical centers by highway and be used for therapy of patients there. To solve the problem of location decision of medical centers, which belongs to a set covering problem, we developed a multi-objective optimization model. The model’s goal is minimizing the numbers of medical centers and total patients’ time cost on the road on the condition that all of patients can be sent a medical center in time. We solved the model with genetic algorithm, and get an approximate optimal solution with 7 medical centers. Then we built a logistic block growth model to describe the changing speed of drugs manufacturing. Comparing it with the SEIIR model, we considered the two situations: one is in severe shortage of drugs, the other is relatively sufficient in drugs. We built two optimization models for the two situations. The optimization goal is minimizing the number of the infectious and minimizing of death cases and the number of infectious individuals, respectively. The decision variables is the drug allocation for every country, and the constraint conditions is drug production.

Finally, by a comprehensive analysis, we made a six-month drug delivery plan for Guinea, Liberia and Sierra Leone, and predict the spreading trends of Ebola in the next six month with the efficient medication’s blockage.

The sensitivity analysis of our models has pointed out that the transmission rate and the initial value setting will affect the result greatly. We find that the speed of drug manufacturing’s growth rate r may control of the epidemic. The minimum daily output of drugs G must m greater than 4000. Otherwise ,the epidemic will be out of control.

Introduction

Problem background

A complex epidemic of Zaire Ebola virus (EBOV) has been affecting West Africa since approximately December 2013, with first cases likely occurring in southern Guinea [1] and facilitating several transmission chains to progress essentially unchecked in the region and to cross porous borders with neighboring Sierra Leone and Liberia and seed a limited outbreak in Nigeria via commercial airplane on 20 July 2014 [2]. Then the number of new cases appear an exponential growth. While public health interventions have been introduced in all affected countries, the numbers of infected cases and deaths from EBOV continue to increase due to the loss of effective medication. A total of 22,495 cases, with 8,981 deaths, have been reported to the World Health Organization as of 4 February 2015[3].

Our work

Since new anti-Ebola drug has been developed, a realistic, sensible, and useful mathematical model about drug allocation and delivery is necessary. Depending on the goal, we divide the spread of disease into three periods: naturally spreading period, spreading period with intervention and spreading period with effective medications. And then we develop a SEIR (susceptible-exposed-infectious-recovered) model to simulate the spread of the disease in the primary period, based on the changing trend of the numbers of infected cases and deaths. Finally, the model are improved to a SEIIR (susceptible-exposed-infectious-isolated-recovered) model to adapt to the second and third period and to predict the future trends in Guinea, Sierra Leone and Liberia.

A delivery system include two main parts: numbers and locations of medical central delivering drugs decision and drug allocation of every medical center. For this reason, an evaluation system of every country’s long-term epidemic situation, two multi-objective optimization are built separately. We developed a detailed plan via our models.

Symbols and definitions

(1) Symbol for SEIIR model with effective medication

Symbol

definitions S susceptible individuals exposed individuals E I infectious individuals

I isolated infectious individuals isolated

I non- isolated infectious individuals free

R recover and survive individuals D death case N total population of the area

 The transmission rate of EBOV

1  the average durations of incubation.

1  the average durations of infectiousness

f the case fatality rate

the ratio of new non-isolated infective  patients

1f the non- isolated individuals fatality rate

2f the isolated individuals fatality rate

G t ( ) number of drug supply

(2)Symbol for model II

Symbol

definitions the number of capitals of first-level p administrative divisions in a country the number of medical centers for EVD set q in a country;    V v v , , , v , , v the set of capitals 1 2 i p

   X x x , , x , x the set of medical centers 1 2 j q

he shortest distance from x to y d x y ( , )

the metric of quantity of drug needed of the ih i th administrative in the coming period the population of the nth administrative R n division

the area of the nth administrative division M n

the population of the main city of the nth nr : administrative division.

the area of the main city of the nth m : n administrative division. the temperature of the nth administrative B n division the Infected people number of the nth nI administrative division is represented F open degree of Ebola treatment centers n

the temperature of the nth administrative C n division open degree of Ebola treatment centers F n

the number of open ETCs in the country c open

the number of cities in the country c all

The economy of the n th country E n

The education level of the n th country i J n

K age coefficient

(3)Symbol for model III

Symbol

definitions G The average daily production of drugs.

G the maximum production rate of the drugs. m

rt growth trends in drug production speed

ntP the aggregate of drug

the first day of the time period of drug nt delivery.

T the time period of drug delivery p

the number of non-isolated infectious I ,i free individuals

G t ( ) i th country’s number of the drug i

N i th country’s the total population i

D i th country’s death cases i

Assumptions

1. In early transmission period, EBOV spread in absence of control interventions. 2. The average duration of the incubation and infectious period were fixed to previous estimates

from an outbreak of the same EBOV subtype in Congo in 1995 (1  = 5 .3 days and1  =

5 .61 days) [3]. 3. Infection only occurs between the patients who are not isolated and susceptible.

4. Even if without effective medication, the mortality rate of isolated patients is lower than that of free patients. 5. People who have recovered from Ebola will obtain the long-term immunity against Ebola. 6. Only being sent to medical center and isolated, affected people have the chance to receive therapy. 7. Ignoring patient’s different condition, the quantity of the medicine needed by all affected people whose disease is not advanced during the whole therapy is equal to one portion of drugs. 8. The population of the region we study is a constant N 9. The transmission only occurs btween only the susceptible and the infective. 10. Patients isolated will not affect the suspective. In other word,their effective contact rate equals to zero. 11 .The medication only refers to drugs used therapy of Ebola, not include vaccine. 12. If affected people want to accept therapy, they must get to a medical center set as delivering medication. 13. If a patient in whom symptoms of Ebola has appeared don’t get a medical central (usually the nearest medical center) in 24 hours, the new medication won’t affect his disease. 14. We set all the medical centers at the capitals of first-level administrative divisions. 15. We use the capital of an administrative division as a representation of the administrative

Model I

SEIR model

After transmission of the virus, susceptible individuals S enter the exposed class E before they become infectious individuals I that either recover and survive R or die D .

According to the it，people can be divided into four class:

the susceptible ( S ), who are susceptible to infection.  the exposed( E ), who are affected but in the incubation.  the infectious ( I ), who are infected and have the symptom.  the recovered( R ), who recover or survive.  The total population of the area is N , and    N S E

I R

, according to the assumption 8. Numbers of all kinds of people in the initial time are shown as follows:

       S (0) S 0 E (0) E 0

I I

(0) 0 R (0) R =0 , , , 0 0 0 0

Let  be the contact rate in absence of control interventions. S N is the proportion of the

 S N susceptible in total population. Hence, the effective contact rate is , and in a unit of time,  SI N the number of new patients is .In other words, the rate of change in the number of the

susceptible is

 d S S I  .   (1) d t N

 E We assumed that is the number of people newly entering the infectious. Therefore,

1 is the average durations of incubation. As for the number of people newly entering the

exposed every day, it can be calculated as follows:

 dE SI    E (2) dt N

In the same manner, we calculate the increment of the infective people:

dI     E I , dt

Where  is sum of natural cure rate and mortality of the infectious. 1 can be seen the

average durations of infectiousness. Suppose the case fatality rate is given by f , then

  (1 f ) I is the number of death per day. Thus, the changing rate of recovery case and death

case with time can be represented as follows respectively:

dR    (1 f ) I , (3) dt

dD   f I . dt

From the above analysis results, We described the early transmission of EBOV as a SEIR (susceptible-exposed-infectious-recovered) dynamics model.

Result

The average duration of the incubation and infectious period were fixed to previous estimates

from an outbreak of the same EBOV subtype in Congo in 1995 (1 = 5 .3 days and1  = 5 .61

days).The other parameter has been given by Chowell et al [4]. All important parameters’ value are listed in Table 1.

Parameter Guinea Sierra Leone Liberia

The average durations of incubation, 1  5.3 5.3 5.3 the average durations of infectiousness, 1  5.61 5.61 5.61

Transmission rate,  0.27 0.43 0.29

Case fatality rate, f 0.75 0.49 0.69

2 December Date of appearance of first infectious case, T 19 Apr 2014 16 Apr 2014 2013 Based on facts, we set the initial numbers of all kinds of as follows:

     S (0) N E I E (0) 10 , (0) I 1 R (0)=0 , , 0 0

Due to the complexity of the system of differential equations, we can’t gain its analytical solution. Therefore, we solve it numerically ode toolbox in MATLAB 2014B for three country (Guinea, Sierra Leone and Liberia) and compare the results with data in the early EBOV transmission period (shown in Fig.2), since EBOV spread in absence of control interventions in that stage.

Fig 2. Dynamics of 2014 EBOV outbreaks in Guinea, Sierra Leone and Liberia. Outbreak data for Guinea, Sierra Leone and Liberia were based on the cumulative numbers of reported total cases (confirmed, probable and suspected) and deaths from the World Health Organization (WHO) [5]. As we can see, The model fits the reported data of cases and deaths in Guinea, Sierra Leone and Liberia well.

SEIIR model

Generally, when the affected people is much enough, it will draw the attention of the government, and the epidemic will be declared as a public health emergency. So does EVBO. According to WHO’s suggestion [6], the first measurement that government should take is isolate the patients, which will impede the spreading of epidemic apparently. The SEIR (susceptible-exposed-infectious-recovered) model fit the early spreading of the disease, but it don’t consider this point. Therefore, there needs to be a improvement for the it. To achieve this goal, we develop a new SEIIR(susceptible-exposed-infectious-quarantined -recovered) model based on the SEIR model, considering the isolated people and without efficient medication. In this model, as transmission of the virus, susceptible individuals S enter the exposed class E

I before they become insolated infectious individuals or uncontrolled infectious isolated

that either recover and survive R or die D . Fig.3 shows the process. I individuals free

The total population:

     N S E

I I

R free isolated

Considering the assumption 10, formulas (1) changes as follows:

 SI dS f r e  ， dt N

Similarly, formula (2) and (3)

 SI dE f r e e    E ， dt N

dI free     E I , (7). free dt

And the numbers of isolated patients’ changing rate is:

dI       isolated (1 ) E I , (8) isolated dt The coefficient  in Formula (7) and (8) represents the ratio of new non-isolated infective patients in new infective patients, since not all of patients are willing to be isolated out of different reason. The value of  mainly depends on the development level of medical system. Suppose that:

    (1 ) ;

If all the patients in isolation can be cured, all the infective patients will be willing to be

 0 isolated, and ;

The lower the mortality of isolated patients is, the smaller the value of  is.

According to it, we can describe the relationship between  and 2f with a function:

   2f e

1f is much lower that of non-isolated patient 2f . Obviously, the mortality of isolated patients

So, the recovered people can be divided into two parts according to being isolated or not. Thus, the changing rate of recovery case and death case with time can be represented as follows respectively:

dR       (1 f ) I (1 f ) I 1 free 2 isolated dt

dD     f I f I 1 free 2 isolated dt

      E (0) E 0 I (0) 0 For the initial value, (0) S 0 R (0) 0 I (0) 0 , , , 0 isolated free

Simulation Result:

f  0.8 According to the report of WHO, the fatality rate of Ebola range from 0.6 to 0.8. Let 1

f  0.6 and while other coefficient unchanged. 2

Due to the naturally spreading stage before isolation measures being taken, we set the initial value with the data in the 100th day as follows:

S  E  R  D    12219576 2209 971 2912 I 822 I 822 , , , , , 0 0 0 0 0, free 0, quarantined

In the same manner, we get a numerical solution by using the ode toolbox in Matlab201.The results shows in Fig.4.

The SEIIR model indeed shows the blockage of isolation to the Ebola’s spreading.

SEIIR model with effective medication

Now since the World Medical Association has developed a new medication which could stop Ebola and cures patients whose disease is not advanced. Outside of isolation , we can eradicate Ebola with the mediation, which has more effect on Ebola’s spreading. Base on this former work, we improve our model once again and get the SEIIR model with effective medication. The model can be described by a system of differential equations as follows

 SI dS free  , dt N

 SI dE f r e e    E , dt N

dI free     E I , free dt

dI        isolated (1 ) E

I M t

( ) , isolated dt

dR        (1 f ) I (1 f )

I M t

( ) , 1 free 2 isolated dt

dD      f I f

I M t

( ) , 1 free 2 isolated dt

      E (0) E 0 I (0) 0 S (0) 0 R (0) 0 I (0) 0 , , , , 0 isolated free

M t is the number of people who can receive the medication in a unit of time. ( ) Where

I According assumption 12, the M(t) have no effect on the changing rate of . And other free

parameters and coefficients’ definition are the same as before.

M t increase, more and more patients will be being isolated, in other word, ( ) In addition, as  becomes smaller. The results shows in Fig.5.

The SEIIR model with effective medication indeed shows the blockage of isolation to the Ebola’s spreading.

Model II

Since the new medication still cannot be manufactured on a large scale, which indicates a shortage of the drug, a feasible delivery system is necessary based on epidemic situation of countries and districts.

The setting of the delivery system can be divided into two main parts:  the medical center number and location decision  and the medication allocation for every affected countries and districts.

Number and location decision

Assumption:

Affected people must get to a medical center within a specified time because the new medication can only cure patients whose disease is not advanced. According to Wikipedia, we assume that if a patient in whom symptoms of Ebola has appeared don’t get a medical central (usually the nearest medical center) in 24 hours, the new medication won’t affect his disease. Accounting for the poor transport facilities in West Africa and convenience of drug managing, we set all the medical centers at the capitals of first-level administrative divisions.

We simplify the distance from everywhere in an administrative division to a medical center as the distance from the capital of the administrative division to the medical center. In other words, we use the capital of an administrative division as a representation of the administrative. It’s feasible because most of people in the West Africa tend to gather in several big cities.

Model:

Generally, the aid work in the charged of some international organizations, like WHO, They, rather than every country separately, assign the medical workers and allocate the medication and other medical source.

Therefore, the new medication is delivered to countries in need separately by air, then to medical centers by highway and be used for therapy of patients there.

Our first goal is decide the number and locations of medical centers.

Due to the assumption, there must be at least one medical center within a specified distance from every administrative division to ensure patients can get to a medical center. This suggests the number and location decision is a set covering problem. In set covering problems, the objective is to minimize the number or cost of facility location such that a specified level of coverage is obtained.

To describe the issue more clearly, we define some parameters as follows: p , the number of capitals of first-level administrative divisions in a country; q , the number of medical centers for EVD set in a country;

   V v v , , , v , , v , the set of capitals; 1 2 i p

   X x x , , x , x , the set of medical centers; 1 2 j q

d x y , the shortest distance from x to y ; ( , )

Due to the assumption, 

X V

. Therefore,

  jx V j , 1,2, , q .

be the distance from the i th administrative division to the nearest d v X ( , ) Then we let i q

medical central:

   d v X ( , ) min d v x ( , ) . i q i j  1 j q

If there is a medical central in it,

d v X ( , )=0 i q

Suppose that the distance patients can moved within 24h is, because the assumption,       1max i p d v X , . i q 

Considering that healthcare works, financial resources and devices are limited, we should minimize the number of medical centers for EVD, q ,on the premise of meeting the coverage requirement.

In addition, administrative division’s need in medication vary from each other. Obviously, the larger an administrative division’s quantity of the medicine needed, the closer the nearest medical center should be. So, we also should

p  Min h d v X ( , ) , i i q 1

ih is the metric of quantity of drug needed of the i th administrative in the coming Where

period.

ih . In next part, we will clarify how to calculate To sum up, We model the problem about medical centers number and location decision with multi-objective optimization. The formulas of this model is p  Min h d v X ( , ) i i q  i 1 Min q       s t . . max d v X , i q  1 i p    X x x , , , x q 1 2 q   x V , for i 1,2, , q j

Solution:

Without loss of generality, we take the most seriously effected Sierra Leone for example and locate medical centers for it.

The Republic of Sierra Leone is composed of four regions: the Northern Province, Southern Province, the Eastern Province, and the Western Area. The first three provinces are further divided into 12 districts. Fig.6 shows it.

Leone.

S

According to our model, we replace every district with its capital (the western area be seen as a district and Freetown is its capital). So , the value of p equals 13.

We search and calculate the shortest path and distance between any two capitals via google map, and the results be shown in Table 2.

Kail Ken Koi Ma Ka Po Ka Magb Bo Bon Moy Puje Free ahu ema du ken mbi rt bal uraka the amb hun town n i a Lo a a ko Kailah 0 112 46 204 353 30 32 179 169 261 284 222 417 un .4 0 1 Kene 112 0 11 192 330 22 30 167 68. 149 173 110 305 ma 3 7 9 5 Koidu 46.4 113 0 159 308 25 27 133 162 256 253 213 340 3 6 Make 204 192 15 0 152 97 11 26.8 133 217 124 206 185 ni 9 .7 8 Kamb 353 330 30 152 0 51 26 176 263 298 181 337 126 ia 8 .1 9 Port 300 227 25 97. 51. 0 21 122 210 244 128 284 119 Loko 3 7 1 6 Kabal 321 309 27 118 269 21 0 105.9 144 334 242 323 302 a 6 6 Magb 179 167 13 26. 176 12 10 0 108 191 100 216 208 uraka 3 8 2 5.9 Bo 169 68.5 16 133 263 21 14 108 0 82. 106 75.3 174.

2 0 4 4 66 Mattr 261 149 25 217 298 24 33 191 82. 0 130 98.5 237 u jong 6 4 4 4 Moya 284 173 25 124 181 12 24 100 106 130 0 179 114 mba 3 8 2 Pujeh 222 110 21 206 337 28 32 216 75. 98. 179 0 312 un 3 4 3 3 5 Freet 417 305 34 185 126 11 30 208 174 237 114 312 0 own 0 9 2 .66 (unit: kilometer) (source: google earth) As for the value of, accounting for the time of preliminary judgment and poor transport facilities, a reasonable value is 92.1km.

ih Measuring the need of every district

Table.3 the revolution of city h h h Kailahun 0.512665 Koinadugu 0.379487 Kambia 0.341398 Kenema 0.553363 Tonkolili 0.294881 Port Loko 0.53602 Kono 0.22831 Bo 0.504783 Pujehun 0.334563 Bombali 0.441547 Bonthe 0.271492 Western Area 0.436276 Moyamba 0.505654

This optimal problem belongs to the NP-hard problems that can’t be solved in polynomial time. So, we can only get the approximate solution with a heuristic, such as genetic algorithm, simulated annealing and so on. Here, we select the genetic algorithm and write a program with Matlab2014.

Running the program repeatedly, we obtain a relatively good results and make our plan: There are seven mental centers located in Kailahun, Makeni, Kambia, Kabala, Bo, Moyamba and Freetown respectively. The Fig. 7 shows the scope that every mental center manages.

Part III

1. Specify evaluation norms

As for the evaluation the Susceptible standard for Each region, there are mainly aspects that count: Population density, Temperature, Humidity, the situation of current disease infection, Open or under construction，economy，National Education and age. What follows in the section will hammer at accounting for the eight aspects.  Population density: Population density undoubtedly accounts for key proportion in the demand level of the drug evaluation. Because Ebola is a spirited contagion disease, not only patients but also corpses can be the source of infection. Therefore, if the population density is high, the rate of spread disease will be fast in general situation. However, in some area, the pollution density of the area is low, but almost people live in a central city (in fact, the pollution density of the city is high), we deal with data preprocessing, making the aspect more reasonable evaluation model. The pollution density of the area could be calculated as follows:

R  a n 1 n M n

the pollution of the number n area. R : n

the acreage of the number n area. M : n

The pollution density of the main city in the area could be calculated as follows:

r  a n 2 n m n

the pollution of the main city number n area . nr :

the acreage of the main city number n area. m : n

We define a new population density which could be calculated as follows:

 ( a a )       2 n 1 n A a b a b b n 1 n 1 2 n 2 3 a 2 n    b b b 1 1 2 3

 . The numerical value depend on the ( a a ) 2 n 1 n

By the above calculation, the population density in the evaluation of the model is more reasonable and accurate.  Temperature Form the past Information and data, the Ebola usually outbreak in the summer ,but in the winter, the entire epidemic have been more effective control, and the status of major outbreaks in Africa is the lower latitudes area, which shows that the temperature is an important aspects in the demand level of the drug evaluation. The temperature of the area is:

B n

 Humidity Ebola outbreak in the areas which the annual precipitation is high and harmonious, especially in the tropical rain forest areas with high coverage. The World Health Organization's report shows that humid climate is conducive to the spread of the virus, therefore, we choose the humidity as an aspects in the evaluation model.

The temperature of the area is

C n

 current disease infection Current infection situation has a great impact on the future of the epidemic. The country who has large number of infected persons face the challenges in future, and need support from World Health Organization. Every patient will require substantial and large investment Because Ebola is highly infectious diseases. Therefore, we believe that using the number of patients to measure a country's entire national epidemic of severe is reasonable. The Infected people number of the area is

nI

 Open or under construction As we all know, controlling the flow of people is an effective measure to prevent further deterioration of infectious diseases, On the one hand, under construction can control the spread of infection to uninfected areas, on the other hand, it have the ability to reduce the risk of infection of healthy people in infected area.

In a country, some cities under opening while some cities under closing (we only consider the large cities of the country).

We define Open coefficient which could be calculated as follows:

c open  F n c all

： the number of open cities in the country c open

： the number of all cities in the country. c all

 Economy In general situation, the more backward economy countries is the more difficult to control the disease is. Therefore, the economic situation of a country is an important indicator to determine the national level in the medical facilities. The lower the country's GDP means the more difficult to control Ebola infection because of under-developed Medical infrastructure. We use the GDP per capita as the aspects to show the economy of the area.

The economy of the area is：

E n

National Education [7]  Cremation in Africa do not comply with the local traditions, which is an important reason for the large-scale outbreak of Ebola. Ebola can spread through the corpses which lead a large number of people infected at the funeral. According to the survey, the higher the education level is, the greater the proportion of accept cremation. Therefore, we choose each country received higher education as a measure of the proportion of the country's level of education. The national education of the area is：

J n

Age[8]  According to the report of the World Health Organization, the probability of illness in young adults over the age of 14 is three times the age of 14, the probability of illness aged 65 or older is four times the age of 14. Thus, we can see that the higher proportion of the population over the age of 14 is, the greater the overall probability of illness is. We define age coefficient which could be calculated as follows:

 K K  14~65 65 K K all

Model

Introduction:

TOPSIS (technique for order performance by similarity to ideal solution) is a useful technique in dealing with multiattribute or multi-criteria decision making (MADM/MCDM) problems in the real world[9]. It helps decision maker organize the problems to be solved, and carry out analysis, comparisons and rankings of the alternatives. Accordingly, the selection of a suitable alternative(s) will be made. However, many decision making problems within organizations will be a collaborative effort. Hence, this model will extend TOPSIS to evaluate the demand of the drug. A complete and efficient procedure for decision making will then be provided.  Step one Since the different factors have greatly different in magnitude, we should normalized the

value of this factors. the normalized value X of the decision matrix X can be any linear- k ij

scale transformation to keep0   k . X 1 ij

We consider that the normalized value of X is the value of the corresponding element X k k ij ij

divided by the operation of its column elements, i.e., vector normalization, then (take the factor as example).

A  k X n m 1    2 2 2 A A A 1 2 n

 Step two: Construct decision matrix X The structure of the matrix can be expressed as follows:

X X

X X

1 2 n   k k k k x

X X

X X

1 11 12 1 j 1 n   k k k k x

X X

X X

  2 21 22 2 j 2 n    X   k k k k

X X

X X

x   i 1 i 2 ij in i     k k k k

X X

X X

  x   m 1 m 2 mj mn m

X represents the attribute or criterion j , ix denotes the alternativei , =1,2 Where ; i , m ， i

; j =1,2 , n ，

In the model, ix means different country, and X means different factors in the evaluation. i

Observe that we can also set the outcomes of qualitative attributes from each alternative as discrete values, e.g., 1 to 10 or linguistics values, so that the quantitative values will be placed in the above decision matrix. For example, current disease infection is a factor which we can’t evaluate it directly, we can use some Index to show it[10].  Step three

Determine the ideal and negative ideal solutions V and V . - k k           k k k

V X

= , , X max X | j 1,2, , m k 1 n ij i         - k - k - k

V X

= , , X min X | j 1,2, , m k 1 n ij i  Step four

Calculate the separation measure from the ideal and the negative ideal solutions, iS  and iS , -

respectively, for the group.

n  v    + k k 2 S = ( v ) for alternati vei i , 1, , m ， i ij j  j 1

n  v    - k k 2 S = ( v ) for alternati vei i , 1, , m ， i ij j  j 1

 Step five Calculate the relative closeness C to the ideal solution for the group. Calculate the relative closeness to the ideal solution and rank the alternatives in descending

order. The relative closeness of the i th alternative iA with respect to positive idea solution

can be expressed as

 S   i C , i 1, , m    S S i i    The larger the index value, the better the performance of the alternative. Where 0 C 1

2. Collect data

To evaluate h of every districts, Many data is needed, we can find every district’s data needed for our specific evaluation norms by searching from the website，like Wikipedia and WHO. We finally conclude the relative statistics of those areas and list them in a form.

Population Open Temperature Humidity Current density coefficient (ºC) (%) disease situation

458.1595 100 24 94 4 Kailahun 4697.336 100 23 94 4 Kenema 2618.687 0 21 87 3 Kono 267.3536 100 26 81 2 Bombali 281.6377 50 24 94 3 Kambia 860.1828 100 22 89 5 Port Loko 299.7132 50 22 69 4 Koinadugu 1740.713 0 23 83 4 Tonkolili 266.1477 100 23 94 4 Bo 1248.725 50 24 91 1 Bonthe 392.2557 100 23 93 4 Moyamba 1176.208 50 25 89 3 Pujehun 25996.65 50 26 81 5 Western Area Note :1.the unit of the population denisty is People /per km Then we use the data to calculate the h with TOPSIS, and the results has been shown Table 3.

The effect on  of external factors

By analysis, we find that  not only is associated with the nature of the epidemic but also

affected by some external factors. These factors include population density, temperature, humidity, current epidemic situation ,open degree of ETC, economy, national education and

age. Hence,  vary from country to country. Some of these factors are change with time,

which result  changing with time. If we want to develop different reasonable long-term

delivery system for different countries, evaluating the external factor’s impact on  is needed.

For the same reason, we can estimate the effect of external facts on  with TOPSIS. We

define a influence coefficient C .usually, C is non-negative, and as it increase,  also

appear a growth.

The first four factors: population density, temperature, humidity, the current epidemic situation are defined as before. Obviously, their addition will result in increment of C. the other factors are redefined or defined as follows:  Open degree of ETC(Ebola treatment centers)

Considering there are many ETCs in a country, we redefine the open degree of ETC: ih

which could be calculated as follows:

c  F all n c open

c Where is the number of open ETCs in the country, open

is the number of cities in the country. c all

 Economy In general situation, the more undeveloped a country is, the more difficult to control the epidemic is. Therefore, the economic situation of a country, measured by GDP per capital is an important indicator to determine the medical treatment level.

The economy of the n th country is represented by：

E n

 National Education Cremation do not comply with the local traditions in Africa, which is an important reason for the large-scale outbreak of Ebola. Ebola can spread through the corpses which lead a large number of people infected at the funeral. According to the survey, the higher the education level is, the greater the proportion of accept cremation is. Therefore, we choose the proportion of people received higher education in each country as a measure of the country's education level,

whose increment results increment of 

The education level of the n th country is represented by：

J n

 Age According to the report of the World Health Organization, the probability of being infected Ebola of young adults over the age of 14 is three times child below the age of 14, and the probability of poeple aged 65 or older is four times. Thus, we can see that the higher

proportion of the population over the age of 14 is, the greater the  will be. We define age

coefficient which could be calculated as follows:

 K K  14~65 65 K K all

Then we can use TOPSIS to estimate the variation of .

Considering the epidemic mainly spread in Sierra Leone, Guinea and Liberia, we select their data to solve our models and decide their drug allocation. By searching online carefully, we final get data needed from the website of World Bank.

current Temperature Humidity Open Economy education Population disease age (%) coefficient (dollar) (% of all) density (ºC) situation

2917 27 75 25 492 38.13 57.69 45.5 Guinea

8622 25 91 50 297 45.16 57.11 35.5 Liberia

Sierra 10518 27 85 85 366 26.44 58.44 79.4 Leone Note: the unit of the population is People /per km After calculating ,the results are shown in Table

C

0.28615361 Guinea 0.467444301 Liberia 0.728861892 Sierra Leone C will be used later.

Part IV

Assumptions

 7 5 10 doses every year[14], we can calculate (1).Ebola drug production in the world can reach

the increment rate of production speed with this data.

 5 2 10 (2).The maximal amount of drugs produced per day can finally reach doses every year.

(3). Each patient needs 1 portion to rehabilitation, and each portion contain 10 doses drug. (4) Assumed that the drug distributed in every period of drug delivery are be used evenly every day.

Model:

Drug production model based logisitic. Because  This model meets these characteristic that the production in initial time is small, then sharp increase in the mid-production .and production in the finally time is large and stable.  the derivative of drug production rate increases at first and then decreases to zero. Therefore, we assume that the relationship between the drug production and time meets the logistic growth model, and the following equation can be listed:

dG G   rt (1 ) dg G m  G t ( ) 100 0

G :the daily production of drugs, namely the production speed.

G : the maximal production speed of drugs. m

rt : growth rate of drug production speed. amount of the drug delivered every time Our drug delivery plan think that there is only a drug delivery in a period of drug delivery

 T 14 days T . Let , Which is reasonable because it can save cost and don’t cause delay to p

the Ebola’s controlling.

Because drugs’ transporting need a certain period of time, and the drug output everyday, so we need to calculate the aggregate of drug which is the based of delivery.

 t T  n p P Gdt t t n n

nt ：the first day of the time period of drug delivery.

T : the period of drug delivery p

Delivery model

According to former analysis, drug production and drug demand change over time.

Comparing the drug production model and drug demand models, we can divide the whole duration into two stage: stage severely short in drugs and stage relative sufficient in drugs. now, we choose the 150th days as a time node.150th days ago, we faced with a severe drug shortage, and our purposes is to control the increment rate of the infectious .After 150th days, the production of the drugs achieve the certain number and the purpose become to reduce the number of death every day.

Delivery model at the stage severely short in drugs

Nonlinear programming model

In the first stage of drug manufacturing, Because of the great shortage in drug, many patients can’t get effective medical treatment, and the increment of the infectious and deaths are both high.

In this moment, we should give priority to the decrement of the increment of the infectious to make the epidemic becoming under the control as soon as possible which will benefit later epidemic controlling.

Hence, For the first stage of drug manufacturing, we build a nonlinear programming model:  the optimization goal which is minimizing the number of the infection sources of all countries:

k   Min I , i 1,2, , k i free ,  i 1

Where k is the number of countries needing drug assistance, and I is the average ,i free

number of infectious individuals non-isolated of the i th country in a period of drug delivery.

G t , ( )  the decision variables is the drug allocation distributed for each country noted by i

it refers the doses of drugs needed by the i th country.  the resistant condition is actual number of drugs.

k    G t ( ) P , i 1,2, , k i t n  i 1

Therefore, a Nonlinear programming optimization model of drug distribution is modeled as follows:

k  Min I , i free , i 1

k    G t ( ) P , i 1,2, , k i t n  i 1

 i 1,2 , k .

delivery model at the stage relatively sufficient in drugs As time goes on, the speed of drug manufacturing grows rapidly. After a period of time, the speed of drugs become high enough to meet the need of every countries to control disease. In the moment, our goal become to minimize death cases every day with the number of the infectious stable. So, a multi-objective optimization model will be developed next based on the former model for the second stage.

Our goal can be described as follows:

k dD  i Min , dt i 1

dD i Where is the average death cases per day in a period of drug delivery. dt And

k  Min I , i free , i 1

At least making it stable. And there are two constraint condition, one is the drug amount restriction:

k    G t ( ) P , i 1,2, , k . i t n  i 1

The other is to consider the fairness to some extent:

I I

I k k 1 1     i free , i free , i free , ( ) 0.2 （11）. N k N k N   i 1 i 1 i i i

Where

N is i th country’s the total population. i

I I k 1  ,i free i free , is i th country’s percent of infectious individuals. is average percent N k N i 1 i i

of uncontrolled infectious individuals.

This shows the ration of difference between the proportion of patients non-isolated in all the population and the mean value of all the countries to the mean value of all the countries is less 20%. This will make the drug distribution is more evenly. The multi-objective optimization model can be described by following formulas:

k  min D , i  i 1 k  min I i free ,  i 1 k   s t . . G t ( ) P i t n  i 1

I I

I k k 1 1     i free , i free , i free , ( ) 0.2 N k N k N   i 1 i 1 i i i

D D

D k k 1 1     i free , i free , i free , ( ) 0.2 N k N k N   i 1 i 1 i i i

  G t ( ) 0 i

Results & analysis

 In the Drug production model, the formula (1 G G ) represent the resistance from the m

finite ability to manufacture drug. Obviously, as t goes on, rt becomes larger ，and

 (1 G G ) becomes smaller ，the increment of manufacturing speed of drugs depend both m

on them. According to the assumption (1) and (2), and supposed that at the 100th day, the manufacturing speed of drugs reaches the maximum, we can know that the maximal manufacturing speed of drugs

 5 G = 2 10 . m

And we solved the model with ode toolbox in Matlab2014 numerically. The result is shown in Fig.8.

Since the epidemic mainly spread in Guinea, Liberia, Sierra Leone, we consider the situation where all the drugs are provided to these three country, and make a half-of-year drug delivery plan and predict the spreading trend in the half of year with the SEIIR model with efficient medication.

Suppose we start to distribute the drug from the 100th day since the epidemic spread. Table.7 shows the value of parameters that moment.

I I S E R D 0, free 0,isolated 0 0 0 0

12181398 4775 639 1209 243 1910 Guinea 4129792 9215 1228 2333 453 3686 Liberia Sierra 6223952 7799 1042 1079 475 3199 Leone In our plan, the period of drug delivery is 14 days, therefore, we will make the new delivery plan every 14 days. As we know from the former analysis, within the half of year, the value of

 vary from country to country and will change with time. Due to this, to recalculate the value

of  after a certain period time is also needed. We recalculate  with the TOSIS mentioned

above every month.

Solving the optimization model with optimization toolbox in Matlab2014. We get our delivery plan for six month shown as following table and figure.

Infected Death portion Infected Death portion case case Case case 8380 2865 108 Guinea Guinea 8730 2984 456 Liberia 19334 5529 235 Liberia 23986 5769 679 15586 4798 345 Sierra Sierra 16142 5032 589 Leone Leone Infected Death portion Infected Death portion case case case case Guinea 16661 3284 685 Guinea 6905 3367 986 Liberia Liberia 21805 6169 891 18954 6398 1278 Sierra Sierra 16142 5648 981 13834 5781 1189 Leone Leone

Infect Death portion Infected Death portion ed case case case case Guinea 4101 3475 1230 Guinea 1771 3586 1580 Liberia Liberia 8747 6430 1806 2767 6529 2209 Sierra Sierra 8639 5863 1698 3910 5965 2497 Leone Leone The figures show the spreading trends of the Ebola in the three country in the next half of year. The tables show the total death cases and total infected cases at the moments delivering drugs .and the portions delivered to three country every time. According to the assumption (3), a portion of drugs equals to ten doses of drugs which can be used to cure one patient totally.

Conclusion

The isolation method and drug intervention can effectively control the EBOV spreading. And Drug manufacturing can also influence epidemic control. The difference between each country will cause the epidemic situation is different. So making epidemic control Strategy need consider a great deal.

Considering many factors including isolated method, drug intervention, geographical conditions, the differences between different countries, the characteristics of the spread of the virus, we build those models.

Model I can forecast the Infectious disease situation. Model II can determine the location of drug station. Model III can make the optimal choice of each country's number of drug. All of these help eradicating Ebola.

Model extending

In SEIIR with effective drug intervention model, we assume that medication only refers to drugs used therapy of Ebola, not include vaccine; Medications only work on patients but the vaccine can be used for individuals who live in the Susceptible area . Now we consider drugs and vaccines can simultaneously supply. The vaccines production is F dose per day. The drug production isG dose per day. Vaccine is able to let the individual to produce antibodies against the virus. So this formula (1) can be rewritten as  SI dS free   F t ( ). dt N At the same time putting the immune into the survivor population, then this formula (3) can be rewritten as

dR         (1 f ) I (1 f )

I M t

( ) F t ( ). . 1 free 2 isolated dt

SEIIR with effective drug intervention model was extended to SEIIR with effective drug and Vaccine intervention model. At the same time F Consistent with the Logistic block growth model，then

dF F   rt 1 (1 ) ， dg F m

 F t ( ) 100. 0

F is maximum of the vaccines production rate，1r is vaccines production growth rate. m

Sensitivity Analysis

SEIIR with effective drug intervention model

 There are some coefficients related to properties of the virus in SEIIR with effective drug intervention model:

1 : The average durations of incubation, 1 : the average durations of infectiousness, : the transmission rate.

We analysis the effect of the three factors on the death case by changing them.

Initial value Changed value Changed percent 1  5.3 6 13.21% the death case 119556 124870 4.44%

1  5.61 6.3 12.31%

the death case 119556 131690 10.15%

 0.27 0.5 46%

the death case 119556 9343221 681.4%

changes, and death cases

The table 8 shows that  is the factor which has the greatest effect on the death case

among the properties, and fig.9 shows the result graphicall

In conclusion, is a key factors to control Ebola, we can take some measures, such as control

the population density, isolation and so on, to reduce it.

E (2) Change the 0

S ,exposed When solving the models, we have set initial values of the initial susceptive 0

E ,infectious 0I ,etc. As for S , 0I , we can get relatively data from the data statistics of WHO. 0 0

creases, and death cases increases E by estimation. So it is necessary to evaluate the effectiveness But we only can inaccurate 0

E and observing the change of result. We change E from 10 to 1000 by step by changing 0 0

of 10.

E increases. In conclusion, As we can see from fig. 10, the death case increases related to 0

E can affect the result greatly. When we set model for predicting the future trend, we the 0

should determine the value of , E based on the reality situation , which will make the finally 0

forecasting more accurate.

(2) delivery systems model

When we build the drug delivery systems model, we use the Logistic block growth model describe the change of drug production speed with time. It’s a reasonable assumption. However, in the real world ,the relationship between the output of drug and time may vary from it. Not

only that, the coefficients r and G can also influent the results (r is the increase speed of m

G is the maximum daily output).Similarly, we study their influence by output growth rate; m

changing the value of them separately, The sensitivity tor .  The results of sensitivity analysis to r is shown on Table.9.

Table 9 The days use r The death case to control 50 250 629128 100(100%) 162(35.3%) 124870(80.1%) 200(400%) 102(59.2%) 272934(56.6%) From the Table 2, we find an obvious phenomenon that the bigger the value is ,the earlier the situation become under control.

G

The sensitivity to

 m

G have been changed from 100 to 10000 by step of 100. The m

We see the needed time to make the epidemic under the control is changed with the change of

G in the Fig.11 m Fig.11 Epidemic controlling is very sensitive to the maximal daily output. The more the maximum daily output is, the less the death case is less. When the maximal daily output is under 4000 dose per day, the drug production can’t meet the need of epidemic controlling. When the maximum daily output is smaller, it is more difficult to control the epidemic and the death cases become high. Therefore, a way to control the epidemic and reduce the death cases is maximize the output every day and improve the increase speed of output growth rate.

Weakness and strengths

Weakness:

In model 1, according to the sensitivity analysis, the simulation results depend on largely the initial values of parameters and coefficients. But some values of the parameters can be only estimated, which can be inaccurate. In addition, the virus has a large probability of mutation, and some parameters will changed which we ignored, which will decrease the validity of the model. In model 2, to simplify the problem, we set all the medical centers at the capitals of districts.

And when calculating the shortest distance, we represent a district with its capital . In model 3, we build the optimization model without considering the vaccine.

Strengths

In model 1, we considered the influence of isolated people and improved our basic model through adding isolated people and drug intervention, which make the simulation more real and effective. The reasonable setting of the parameter ( ) , will bring the model the ability of self- regulation.

In model 2, when choosing locations of medical centers, considering the drug distribution point will not change once selected, we get our result from a long-term perspective. Which will make the results more reasonable.

In model 3, we building a logistic block growth model about drug production. This model is reasonable. We consider two situations. The one is the condition of severe lacking drug, other one is the condition of relatively sufficient drug. At last we assume the disease is under control when the growth rate of infectious individuals develop into zero.

Letter for the world medical association

To the world medical association,

Ebola has received wide attention of people all over the world since 2014, and until now, the situation of the Ebola in Africa is still not optimistic. Recently, the number of the infected people appeared an increment again. With the coming warm rainy season, we must pay attention to the development trend of Ebola disease.

To prevent the spread of epidemic, we propose the following suggestion Based on our study:

National measures to control the epidemic infection Build strong and effective isolation to prevent deterioration of the condition, and focus on the patient in the incubation to avoid them a new source of infection before being isolated. Provide the public with the right to preventive methods by publicity, and reduce large gatherings in the public. The government should popularize cremation, even take lethal force cremation for death for Ebola patients with known. The government should control the regional migration.

For description of drug distribution Because the drug is in shortage, the need of each country medicines cannot be met. Therefore: Before drug production reach a certain amount, according to the different circumstances of each country and a reasonable prediction, we set a drug delivery system whose purpose is the overall controlled objectives, and the overall distribution of the situation is adjusted every two weeks. After drug production speed reach the necessary requirement .we use minimazing the number of deaths as the target for distribution. If you want to know more detailed analysis and the data, welcome to read our paper. We wish that Ebola will be controlled soon.

Yours sincerely
