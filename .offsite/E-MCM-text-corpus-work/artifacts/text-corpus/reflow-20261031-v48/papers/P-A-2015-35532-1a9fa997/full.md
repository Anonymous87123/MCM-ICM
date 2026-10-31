# P-A-2015-35532-1a9fa997

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Team Control Number

<!-- b000002 | front_matter | pages [1] -->
35532

<!-- b000003 | prose | pages [1] -->
For office use only For office use only T1 ________________ F1 ________________ T2 ________________ F2 ________________ T3 ________________ F3 ________________ Problem Chosen T4 ________________ F4 ________________

<!-- b000004 | front_matter | pages [1] -->
A

<!-- b000005 | front_matter | pages [1] -->
2015 Mathematical Contest in Modeling (MCM) Summary Sheet

<!-- b000006 | heading | pages [1] -->
Summary

<!-- b000007 | prose | pages [1] -->
The complex epidemic of Zaire ebolavirus has been affecting West Africa. A series of realistic, sensible, and useful mathematical model about Ebola of spreading and medication delivery are developed to eradicating Ebola.

<!-- b000008 | prose | pages [1] -->
First, we divide the spreading of disease into three periods: naturally spreading period, spreading period with isolation but without effective medications and spreading period with effective medications. We develop a SEIR (susceptible-exposed-infectious-recovered) model to simulate the spread of the disease in the primary period. Then the model are improved to a SEIQR (susceptible-exposed-infectious-quarantined-recovered) model to adapt to the second and third period and to predict the future trends in Guinea, Sierra Leone and Liberia.

<!-- b000009 | prose | pages [1] -->
According to our plan, drugs are delivered to countries in need separately by air, then to medical centers by highway and be used for therapy of patients there. To solve the problem of location decision of medical centers, which belongs to a set covering problem, we developed a multi-objective optimization model. The model’s goal is minimizing the numbers of medical centers and total patients’ time cost on the road on the condition that all of patients can be sent a medical center in time. We solved the model with genetic algorithm, and get an approximate optimal solution with 7 medical centers. Then we built a logistic block growth model to describe the changing speed of drugs manufacturing. Comparing it with the SEIIR model, we considered the two situations: one is in severe shortage of drugs, the other is relatively sufficient in drugs. We built two optimization models for the two situations. The optimization goal is minimizing the number of the infectious and minimizing of death cases and the number of infectious individuals, respectively. The decision variables is the drug allocation for every country, and the constraint conditions is drug production.

<!-- b000010 | prose | pages [1] -->
Finally, by a comprehensive analysis, we made a six-month drug delivery plan for Guinea, Liberia and Sierra Leone, and predict the spreading trends of Ebola in the next six month with the efficient medication’s blockage.

<!-- b000011 | prose | pages [1] -->
The sensitivity analysis of our models has pointed out that the transmission rate and the initial value setting will affect the result greatly. We find that the speed of drug manufacturing’s growth rate r may control of the epidemic. The minimum daily output of drugs G must m greater than 4000. Otherwise ,the epidemic will be out of control.

<!-- b000012 | furniture | pages [2] -->
Team # 35532                                                                          1 / 34

<!-- b000013 | heading | pages [2] -->
Introduction

<!-- b000014 | prose | pages [2] -->
Problem background

<!-- b000015 | prose | pages [2] -->
A complex epidemic of Zaire Ebola virus (EBOV) has been affecting West Africa since approximately December 2013, with first cases likely occurring in southern Guinea [1] and facilitating several transmission chains to progress essentially unchecked in the region and to cross porous borders with neighboring Sierra Leone and Liberia and seed a limited outbreak in Nigeria via commercial airplane on 20 July 2014 [2]. Then the number of new cases appear an exponential growth. While public health interventions have been introduced in all affected countries, the numbers of infected cases and deaths from EBOV continue to increase due to the loss of effective medication. A total of 22,495 cases, with 8,981 deaths, have been reported to the World Health Organization as of 4 February 2015[3].

<!-- b000016 | prose | pages [2] -->
Our work

<!-- b000017 | prose | pages [2] -->
Since new anti-Ebola drug has been developed, a realistic, sensible, and useful mathematical model about drug allocation and delivery is necessary. Depending on the goal, we divide the spread of disease into three periods: naturally spreading period, spreading period with intervention and spreading period with effective medications. And then we develop a SEIR (susceptible-exposed-infectious-recovered) model to simulate the spread of the disease in the primary period, based on the changing trend of the numbers of infected cases and deaths. Finally, the model are improved to a SEIIR (susceptible-exposed-infectious-isolated-recovered) model to adapt to the second and third period and to predict the future trends in Guinea, Sierra Leone and Liberia.

<!-- b000018 | prose | pages [2] -->
A delivery system include two main parts: numbers and locations of medical central delivering drugs decision and drug allocation of every medical center. For this reason, an evaluation system of every country’s long-term epidemic situation, two multi-objective optimization are built separately. We developed a detailed plan via our models.

<!-- b000019 | prose | pages [2] -->
Symbols and definitions

<!-- b000020 | heading | pages [2] -->
(1) Symbol for SEIIR model with effective medication

<!-- b000021 | heading | pages [2] -->
Symbol

<!-- b000022 | prose | pages [2] -->
definitions S susceptible individuals exposed individuals E I infectious individuals

<!-- b000023 | prose | pages [2] -->
I isolated infectious individuals isolated

<!-- b000024 | prose | pages [2] -->
I non- isolated infectious individuals free

<!-- b000025 | prose | pages [2, 3] -->
R recover and survive individuals D death case N total population of the area

<!-- b000026 | furniture | pages [3] -->
Team # 35532                                                                          2 / 34

<!-- b000028 | prose | pages [3] -->
 The transmission rate of EBOV

<!-- b000029 | prose | pages [3] -->
1  the average durations of incubation.

<!-- b000030 | prose | pages [3] -->
1  the average durations of infectiousness

<!-- b000031 | prose | pages [3] -->
f the case fatality rate

<!-- b000032 | prose | pages [3] -->
the ratio of new non-isolated infective  patients

<!-- b000033 | prose | pages [3] -->
1f the non- isolated individuals fatality rate

<!-- b000034 | prose | pages [3] -->
2f the isolated individuals fatality rate

<!-- b000035 | prose | pages [3] -->
G t ( ) number of drug supply

<!-- b000036 | heading | pages [3] -->
(2)Symbol for model II

<!-- b000037 | heading | pages [3] -->
Symbol

<!-- b000038 | prose | pages [3] -->
definitions the number of capitals of first-level p administrative divisions in a country the number of medical centers for EVD set q in a country;    V v v , , , v , , v the set of capitals 1 2 i p

<!-- b000039 | prose | pages [3] -->
   X x x , , x , x the set of medical centers 1 2 j q

<!-- b000040 | prose | pages [3] -->
he shortest distance from x to y d x y ( , )

<!-- b000041 | prose | pages [3] -->
the metric of quantity of drug needed of the ih i th administrative in the coming period the population of the nth administrative R n division

<!-- b000042 | prose | pages [3] -->
the area of the nth administrative division M n

<!-- b000043 | prose | pages [3] -->
the population of the main city of the nth nr : administrative division.

<!-- b000044 | prose | pages [3, 4] -->
the area of the main city of the nth m : n administrative division. the temperature of the nth administrative B n division the Infected people number of the nth nI administrative division is represented F open degree of Ebola treatment centers n

<!-- b000045 | furniture | pages [4] -->
Team # 35532                                                                          3 / 34

<!-- b000047 | prose | pages [4] -->
the temperature of the nth administrative C n division open degree of Ebola treatment centers F n

<!-- b000048 | prose | pages [4] -->
the number of open ETCs in the country c open

<!-- b000049 | prose | pages [4] -->
the number of cities in the country c all

<!-- b000050 | prose | pages [4] -->
The economy of the n th country E n

<!-- b000051 | prose | pages [4] -->
The education level of the n th country i J n

<!-- b000052 | prose | pages [4] -->
K age coefficient

<!-- b000053 | heading | pages [4] -->
(3)Symbol for model III

<!-- b000054 | heading | pages [4] -->
Symbol

<!-- b000055 | prose | pages [4] -->
definitions G The average daily production of drugs.

<!-- b000056 | prose | pages [4] -->
G the maximum production rate of the drugs. m

<!-- b000057 | prose | pages [4] -->
rt growth trends in drug production speed

<!-- b000058 | prose | pages [4] -->
ntP the aggregate of drug

<!-- b000059 | prose | pages [4] -->
the first day of the time period of drug nt delivery.

<!-- b000060 | prose | pages [4] -->
T the time period of drug delivery p

<!-- b000061 | prose | pages [4] -->
the number of non-isolated infectious I ,i free individuals

<!-- b000062 | prose | pages [4] -->
G t ( ) i th country’s number of the drug i

<!-- b000063 | prose | pages [4] -->
N i th country’s the total population i

<!-- b000064 | prose | pages [4] -->
D i th country’s death cases i

<!-- b000065 | heading | pages [4] -->
Assumptions

<!-- b000066 | prose | pages [4] -->
1. In early transmission period, EBOV spread in absence of control interventions. 2. The average duration of the incubation and infectious period were fixed to previous estimates

<!-- b000067 | prose | pages [4] -->
from an outbreak of the same EBOV subtype in Congo in 1995 (1  = 5 .3 days and1  =

<!-- b000068 | prose | pages [4] -->
5 .61 days) [3]. 3. Infection only occurs between the patients who are not isolated and susceptible.

<!-- b000069 | furniture | pages [5] -->
Team # 35532                                                                          4 / 34

<!-- b000070 | prose | pages [5] -->
4. Even if without effective medication, the mortality rate of isolated patients is lower than that of free patients. 5. People who have recovered from Ebola will obtain the long-term immunity against Ebola. 6. Only being sent to medical center and isolated, affected people have the chance to receive therapy. 7. Ignoring patient’s different condition, the quantity of the medicine needed by all affected people whose disease is not advanced during the whole therapy is equal to one portion of drugs. 8. The population of the region we study is a constant N 9. The transmission only occurs btween only the susceptible and the infective. 10. Patients isolated will not affect the suspective. In other word,their effective contact rate equals to zero. 11 .The medication only refers to drugs used therapy of Ebola, not include vaccine. 12. If affected people want to accept therapy, they must get to a medical center set as delivering medication. 13. If a patient in whom symptoms of Ebola has appeared don’t get a medical central (usually the nearest medical center) in 24 hours, the new medication won’t affect his disease. 14. We set all the medical centers at the capitals of first-level administrative divisions. 15. We use the capital of an administrative division as a representation of the administrative

<!-- b000071 | heading | pages [5] -->
Model I

<!-- b000072 | heading | pages [5] -->
SEIR model

<!-- b000073 | prose | pages [5] -->
After transmission of the virus, susceptible individuals S enter the exposed class E before they become infectious individuals I that either recover and survive R or die D .

<!-- b000074 | caption | pages [5] -->
Fig.1 shows the process.

<!-- b000075 | caption | pages [5] -->
Fig.1 the process of the model

<!-- b000076 | prose | pages [5] -->
According to the it，people can be divided into four class:

<!-- b000077 | prose | pages [5] -->
the susceptible ( S ), who are susceptible to infection.  the exposed( E ), who are affected but in the incubation.  the infectious ( I ), who are infected and have the symptom.  the recovered( R ), who recover or survive.  The total population of the area is N , and    N S E

<!-- b000078 | heading | pages [5] -->
I R

<!-- b000079 | prose | pages [5] -->
, according to the assumption 8. Numbers of all kinds of people in the initial time are shown as follows:

<!-- b000080 | prose | pages [5] -->
       S (0) S 0 E (0) E 0

<!-- b000081 | heading | pages [5] -->
I I

<!-- b000082 | prose | pages [5] -->
(0) 0 R (0) R =0 , , , 0 0 0 0

<!-- b000083 | prose | pages [5] -->
Let  be the contact rate in absence of control interventions. S N is the proportion of the

<!-- b000084 | prose | pages [5, 6] -->
 S N susceptible in total population. Hence, the effective contact rate is , and in a unit of time,  SI N the number of new patients is .In other words, the rate of change in the number of the

<!-- b000085 | furniture | pages [6] -->
Team # 35532                                                                          5 / 34

<!-- b000087 | prose | pages [6] -->
susceptible is

<!-- b000088 | prose | pages [6] -->
 d S S I  .   (1) d t N

<!-- b000089 | prose | pages [6] -->
 E We assumed that is the number of people newly entering the infectious. Therefore,

<!-- b000090 | prose | pages [6] -->
1 is the average durations of incubation. As for the number of people newly entering the

<!-- b000091 | prose | pages [6] -->
exposed every day, it can be calculated as follows:

<!-- b000092 | prose | pages [6] -->
 dE SI    E (2) dt N

<!-- b000093 | prose | pages [6] -->
In the same manner, we calculate the increment of the infective people:

<!-- b000094 | prose | pages [6] -->
dI     E I , dt

<!-- b000095 | prose | pages [6] -->
Where  is sum of natural cure rate and mortality of the infectious. 1 can be seen the

<!-- b000096 | prose | pages [6] -->
average durations of infectiousness. Suppose the case fatality rate is given by f , then

<!-- b000097 | prose | pages [6] -->
  (1 f ) I is the number of death per day. Thus, the changing rate of recovery case and death

<!-- b000098 | prose | pages [6] -->
case with time can be represented as follows respectively:

<!-- b000099 | prose | pages [6] -->
dR    (1 f ) I , (3) dt

<!-- b000100 | prose | pages [6] -->
dD   f I . dt

<!-- b000101 | prose | pages [6] -->
From the above analysis results, We described the early transmission of EBOV as a SEIR (susceptible-exposed-infectious-recovered) dynamics model.

<!-- b000102 | heading | pages [6] -->
Result

<!-- b000103 | prose | pages [6] -->
The average duration of the incubation and infectious period were fixed to previous estimates

<!-- b000104 | prose | pages [6] -->
from an outbreak of the same EBOV subtype in Congo in 1995 (1 = 5 .3 days and1  = 5 .61

<!-- b000105 | prose | pages [6] -->
days).The other parameter has been given by Chowell et al [4]. All important parameters’ value are listed in Table 1.

<!-- b000106 | caption | pages [6] -->
Table 1. Parameter estimates for the 2014 EBOV outbreak

<!-- b000107 | prose | pages [6] -->
Parameter Guinea Sierra Leone Liberia

<!-- b000108 | prose | pages [6, 7] -->
The average durations of incubation, 1  5.3 5.3 5.3 the average durations of infectiousness, 1  5.61 5.61 5.61

<!-- b000109 | furniture | pages [7] -->
Team # 35532                                                                          6 / 34

<!-- b000111 | prose | pages [7] -->
Transmission rate,  0.27 0.43 0.29

<!-- b000112 | prose | pages [7] -->
Case fatality rate, f 0.75 0.49 0.69

<!-- b000113 | prose | pages [7] -->
2 December Date of appearance of first infectious case, T 19 Apr 2014 16 Apr 2014 2013 Based on facts, we set the initial numbers of all kinds of as follows:

<!-- b000114 | prose | pages [7] -->
     S (0) N E I E (0) 10 , (0) I 1 R (0)=0 , , 0 0

<!-- b000115 | prose | pages [7] -->
Due to the complexity of the system of differential equations, we can’t gain its analytical solution. Therefore, we solve it numerically ode toolbox in MATLAB 2014B for three country (Guinea, Sierra Leone and Liberia) and compare the results with data in the early EBOV transmission period (shown in Fig.2), since EBOV spread in absence of control interventions in that stage.

<!-- b000116 | furniture | pages [8] -->
Team # 35532                                                                          7 / 34

<!-- b000117 | caption | pages [8] -->
Fig.2.1the early EBOV transmission period of Guinea

<!-- b000118 | caption | pages [8] -->
Fig.2.2the early EBOV transmission period of Liberia

<!-- b000119 | caption | pages [8] -->
Fig.2.3the early EBOV transmission period of Sierra Leone

<!-- b000120 | prose | pages [8] -->
Fig 2. Dynamics of 2014 EBOV outbreaks in Guinea, Sierra Leone and Liberia. Outbreak data for Guinea, Sierra Leone and Liberia were based on the cumulative numbers of reported total cases (confirmed, probable and suspected) and deaths from the World Health Organization (WHO) [5]. As we can see, The model fits the reported data of cases and deaths in Guinea, Sierra Leone and Liberia well.

<!-- b000121 | heading | pages [8] -->
SEIIR model

<!-- b000122 | furniture | pages [9] -->
Team # 35532                                                                          8 / 34

<!-- b000123 | prose | pages [9] -->
Generally, when the affected people is much enough, it will draw the attention of the government, and the epidemic will be declared as a public health emergency. So does EVBO. According to WHO’s suggestion [6], the first measurement that government should take is isolate the patients, which will impede the spreading of epidemic apparently. The SEIR (susceptible-exposed-infectious-recovered) model fit the early spreading of the disease, but it don’t consider this point. Therefore, there needs to be a improvement for the it. To achieve this goal, we develop a new SEIIR(susceptible-exposed-infectious-quarantined -recovered) model based on the SEIR model, considering the isolated people and without efficient medication. In this model, as transmission of the virus, susceptible individuals S enter the exposed class E

<!-- b000124 | prose | pages [9] -->
I before they become insolated infectious individuals or uncontrolled infectious isolated

<!-- b000125 | prose | pages [9] -->
that either recover and survive R or die D . Fig.3 shows the process. I individuals free

<!-- b000126 | caption | pages [9] -->
Fig.3 the process of the SEIIR model

<!-- b000127 | prose | pages [9] -->
The total population:

<!-- b000128 | prose | pages [9] -->
     N S E

<!-- b000129 | heading | pages [9] -->
I I

<!-- b000130 | prose | pages [9] -->
R free isolated

<!-- b000131 | prose | pages [9] -->
Considering the assumption 10, formulas (1) changes as follows:

<!-- b000132 | prose | pages [9] -->
 SI dS f r e  ， dt N

<!-- b000133 | prose | pages [9] -->
Similarly, formula (2) and (3)

<!-- b000134 | prose | pages [9] -->
 SI dE f r e e    E ， dt N

<!-- b000135 | prose | pages [9] -->
dI free     E I , (7). free dt

<!-- b000136 | prose | pages [9] -->
And the numbers of isolated patients’ changing rate is:

<!-- b000137 | prose | pages [9] -->
dI       isolated (1 ) E I , (8) isolated dt The coefficient  in Formula (7) and (8) represents the ratio of new non-isolated infective patients in new infective patients, since not all of patients are willing to be isolated out of different reason. The value of  mainly depends on the development level of medical system. Suppose that:

<!-- b000138 | furniture | pages [10] -->
Team # 35532                                                                          9 / 34

<!-- b000139 | prose | pages [10] -->
    (1 ) ;

<!-- b000140 | prose | pages [10] -->
If all the patients in isolation can be cured, all the infective patients will be willing to be

<!-- b000141 | prose | pages [10] -->
 0 isolated, and ;

<!-- b000142 | prose | pages [10] -->
The lower the mortality of isolated patients is, the smaller the value of  is.

<!-- b000143 | prose | pages [10] -->
According to it, we can describe the relationship between  and 2f with a function:

<!-- b000144 | prose | pages [10] -->
   2f e

<!-- b000145 | prose | pages [10] -->
1f is much lower that of non-isolated patient 2f . Obviously, the mortality of isolated patients

<!-- b000146 | prose | pages [10] -->
So, the recovered people can be divided into two parts according to being isolated or not. Thus, the changing rate of recovery case and death case with time can be represented as follows respectively:

<!-- b000147 | prose | pages [10] -->
dR       (1 f ) I (1 f ) I 1 free 2 isolated dt

<!-- b000148 | prose | pages [10] -->
dD     f I f I 1 free 2 isolated dt

<!-- b000149 | prose | pages [10] -->
      E (0) E 0 I (0) 0 For the initial value, (0) S 0 R (0) 0 I (0) 0 , , , 0 isolated free

<!-- b000150 | prose | pages [10] -->
Simulation Result:

<!-- b000151 | prose | pages [10] -->
f  0.8 According to the report of WHO, the fatality rate of Ebola range from 0.6 to 0.8. Let 1

<!-- b000152 | prose | pages [10] -->
f  0.6 and while other coefficient unchanged. 2

<!-- b000153 | prose | pages [10] -->
Due to the naturally spreading stage before isolation measures being taken, we set the initial value with the data in the 100th day as follows:

<!-- b000154 | prose | pages [10] -->
S  E  R  D    12219576 2209 971 2912 I 822 I 822 , , , , , 0 0 0 0 0, free 0, quarantined

<!-- b000155 | prose | pages [10] -->
In the same manner, we get a numerical solution by using the ode toolbox in Matlab201.The results shows in Fig.4.

<!-- b000156 | furniture | pages [11] -->
Team # 35532                                                                          10 / 34

<!-- b000157 | caption | pages [11] -->
Fig.4 the result of SEIIR model

<!-- b000158 | prose | pages [11] -->
The SEIIR model indeed shows the blockage of isolation to the Ebola’s spreading.

<!-- b000159 | heading | pages [11] -->
SEIIR model with effective medication

<!-- b000160 | prose | pages [11] -->
Now since the World Medical Association has developed a new medication which could stop Ebola and cures patients whose disease is not advanced. Outside of isolation , we can eradicate Ebola with the mediation, which has more effect on Ebola’s spreading. Base on this former work, we improve our model once again and get the SEIIR model with effective medication. The model can be described by a system of differential equations as follows

<!-- b000161 | prose | pages [11] -->
 SI dS free  , dt N

<!-- b000162 | prose | pages [11] -->
 SI dE f r e e    E , dt N

<!-- b000163 | prose | pages [11] -->
dI free     E I , free dt

<!-- b000164 | prose | pages [11] -->
dI        isolated (1 ) E

<!-- b000165 | heading | pages [11] -->
I M t

<!-- b000166 | prose | pages [11] -->
( ) , isolated dt

<!-- b000167 | prose | pages [11] -->
dR        (1 f ) I (1 f )

<!-- b000168 | heading | pages [11] -->
I M t

<!-- b000169 | prose | pages [11] -->
( ) , 1 free 2 isolated dt

<!-- b000170 | prose | pages [11] -->
dD      f I f

<!-- b000171 | heading | pages [11] -->
I M t

<!-- b000172 | prose | pages [11] -->
( ) , 1 free 2 isolated dt

<!-- b000173 | prose | pages [11] -->
      E (0) E 0 I (0) 0 S (0) 0 R (0) 0 I (0) 0 , , , , 0 isolated free

<!-- b000174 | prose | pages [11] -->
M t is the number of people who can receive the medication in a unit of time. ( ) Where

<!-- b000175 | prose | pages [11] -->
I According assumption 12, the M(t) have no effect on the changing rate of . And other free

<!-- b000176 | prose | pages [11] -->
parameters and coefficients’ definition are the same as before.

<!-- b000177 | prose | pages [11, 12] -->
M t increase, more and more patients will be being isolated, in other word, ( ) In addition, as  becomes smaller. The results shows in Fig.5.

<!-- b000178 | furniture | pages [12] -->
Team # 35532                                                                          11 / 34

<!-- b000180 | caption | pages [12] -->
Fig.5 the result of SEIIR model with effective medication

<!-- b000181 | prose | pages [12] -->
The SEIIR model with effective medication indeed shows the blockage of isolation to the Ebola’s spreading.

<!-- b000182 | heading | pages [12] -->
Model II

<!-- b000183 | prose | pages [12] -->
Since the new medication still cannot be manufactured on a large scale, which indicates a shortage of the drug, a feasible delivery system is necessary based on epidemic situation of countries and districts.

<!-- b000184 | prose | pages [12] -->
The setting of the delivery system can be divided into two main parts:  the medical center number and location decision  and the medication allocation for every affected countries and districts.

<!-- b000185 | prose | pages [12] -->
Number and location decision

<!-- b000186 | heading | pages [12] -->
Assumption:

<!-- b000187 | prose | pages [12] -->
Affected people must get to a medical center within a specified time because the new medication can only cure patients whose disease is not advanced. According to Wikipedia, we assume that if a patient in whom symptoms of Ebola has appeared don’t get a medical central (usually the nearest medical center) in 24 hours, the new medication won’t affect his disease. Accounting for the poor transport facilities in West Africa and convenience of drug managing, we set all the medical centers at the capitals of first-level administrative divisions.

<!-- b000188 | prose | pages [12] -->
We simplify the distance from everywhere in an administrative division to a medical center as the distance from the capital of the administrative division to the medical center. In other words, we use the capital of an administrative division as a representation of the administrative. It’s feasible because most of people in the West Africa tend to gather in several big cities.

<!-- b000189 | heading | pages [12] -->
Model:

<!-- b000190 | prose | pages [12] -->
Generally, the aid work in the charged of some international organizations, like WHO, They, rather than every country separately, assign the medical workers and allocate the medication and other medical source.

<!-- b000191 | prose | pages [12] -->
Therefore, the new medication is delivered to countries in need separately by air, then to medical centers by highway and be used for therapy of patients there.

<!-- b000192 | furniture | pages [13] -->
Team # 35532                                                                          12 / 34

<!-- b000193 | prose | pages [13] -->
Our first goal is decide the number and locations of medical centers.

<!-- b000194 | prose | pages [13] -->
Due to the assumption, there must be at least one medical center within a specified distance from every administrative division to ensure patients can get to a medical center. This suggests the number and location decision is a set covering problem. In set covering problems, the objective is to minimize the number or cost of facility location such that a specified level of coverage is obtained.

<!-- b000195 | prose | pages [13] -->
To describe the issue more clearly, we define some parameters as follows: p , the number of capitals of first-level administrative divisions in a country; q , the number of medical centers for EVD set in a country;

<!-- b000196 | prose | pages [13] -->
   V v v , , , v , , v , the set of capitals; 1 2 i p

<!-- b000197 | prose | pages [13] -->
   X x x , , x , x , the set of medical centers; 1 2 j q

<!-- b000198 | prose | pages [13] -->
d x y , the shortest distance from x to y ; ( , )

<!-- b000199 | prose | pages [13] -->
Due to the assumption, 

<!-- b000200 | heading | pages [13] -->
X V

<!-- b000201 | prose | pages [13] -->
. Therefore,

<!-- b000202 | prose | pages [13] -->
  jx V j , 1,2, , q .

<!-- b000203 | prose | pages [13] -->
be the distance from the i th administrative division to the nearest d v X ( , ) Then we let i q

<!-- b000204 | prose | pages [13] -->
medical central:

<!-- b000205 | prose | pages [13] -->
   d v X ( , ) min d v x ( , ) . i q i j  1 j q

<!-- b000206 | prose | pages [13] -->
If there is a medical central in it,

<!-- b000207 | prose | pages [13] -->
d v X ( , )=0 i q

<!-- b000208 | prose | pages [13] -->
Suppose that the distance patients can moved within 24h is, because the assumption,       1max i p d v X , . i q 

<!-- b000209 | prose | pages [13] -->
Considering that healthcare works, financial resources and devices are limited, we should minimize the number of medical centers for EVD, q ,on the premise of meeting the coverage requirement.

<!-- b000210 | prose | pages [13] -->
In addition, administrative division’s need in medication vary from each other. Obviously, the larger an administrative division’s quantity of the medicine needed, the closer the nearest medical center should be. So, we also should

<!-- b000211 | prose | pages [13] -->
p  Min h d v X ( , ) , i i q 1

<!-- b000212 | prose | pages [13] -->
ih is the metric of quantity of drug needed of the i th administrative in the coming Where

<!-- b000213 | prose | pages [13] -->
period.

<!-- b000214 | prose | pages [13, 14] -->
ih . In next part, we will clarify how to calculate To sum up, We model the problem about medical centers number and location decision with multi-objective optimization. The formulas of this model is p  Min h d v X ( , ) i i q  i 1 Min q       s t . . max d v X , i q  1 i p    X x x , , , x q 1 2 q   x V , for i 1,2, , q j

<!-- b000215 | furniture | pages [14] -->
Team # 35532                                                                          13 / 34

<!-- b000217 | heading | pages [14] -->
Solution:

<!-- b000218 | prose | pages [14] -->
Without loss of generality, we take the most seriously effected Sierra Leone for example and locate medical centers for it.

<!-- b000219 | prose | pages [14] -->
The Republic of Sierra Leone is composed of four regions: the Northern Province, Southern Province, the Eastern Province, and the Western Area. The first three provinces are further divided into 12 districts. Fig.6 shows it.

<!-- b000220 | caption | pages [14] -->
Fig.6 The 12 districts and 2 areas of Sierra

<!-- b000221 | prose | pages [14] -->
Leone.

<!-- b000222 | prose | pages [14] -->
S

<!-- b000223 | prose | pages [14] -->
According to our model, we replace every district with its capital (the western area be seen as a district and Freetown is its capital). So , the value of p equals 13.

<!-- b000224 | prose | pages [14] -->
We search and calculate the shortest path and distance between any two capitals via google map, and the results be shown in Table 2.

<!-- b000225 | caption | pages [14] -->
Table 2 :the shortest path and distance between any two capitals

<!-- b000226 | prose | pages [14, 15] -->
Kail Ken Koi Ma Ka Po Ka Magb Bo Bon Moy Puje Free ahu ema du ken mbi rt bal uraka the amb hun town n i a Lo a a ko Kailah 0 112 46 204 353 30 32 179 169 261 284 222 417 un .4 0 1 Kene 112 0 11 192 330 22 30 167 68. 149 173 110 305 ma 3 7 9 5 Koidu 46.4 113 0 159 308 25 27 133 162 256 253 213 340 3 6 Make 204 192 15 0 152 97 11 26.8 133 217 124 206 185 ni 9 .7 8 Kamb 353 330 30 152 0 51 26 176 263 298 181 337 126 ia 8 .1 9 Port 300 227 25 97. 51. 0 21 122 210 244 128 284 119 Loko 3 7 1 6 Kabal 321 309 27 118 269 21 0 105.9 144 334 242 323 302 a 6 6 Magb 179 167 13 26. 176 12 10 0 108 191 100 216 208 uraka 3 8 2 5.9 Bo 169 68.5 16 133 263 21 14 108 0 82. 106 75.3 174.

<!-- b000227 | furniture | pages [15] -->
Team # 35532                                                                          14 / 34

<!-- b000229 | prose | pages [15] -->
2 0 4 4 66 Mattr 261 149 25 217 298 24 33 191 82. 0 130 98.5 237 u jong 6 4 4 4 Moya 284 173 25 124 181 12 24 100 106 130 0 179 114 mba 3 8 2 Pujeh 222 110 21 206 337 28 32 216 75. 98. 179 0 312 un 3 4 3 3 5 Freet 417 305 34 185 126 11 30 208 174 237 114 312 0 own 0 9 2 .66 (unit: kilometer) (source: google earth) As for the value of, accounting for the time of preliminary judgment and poor transport facilities, a reasonable value is 92.1km.

<!-- b000230 | prose | pages [15] -->
ih Measuring the need of every district

<!-- b000231 | prose | pages [15] -->
Table.3 the revolution of city h h h Kailahun 0.512665 Koinadugu 0.379487 Kambia 0.341398 Kenema 0.553363 Tonkolili 0.294881 Port Loko 0.53602 Kono 0.22831 Bo 0.504783 Pujehun 0.334563 Bombali 0.441547 Bonthe 0.271492 Western Area 0.436276 Moyamba 0.505654

<!-- b000232 | prose | pages [15] -->
This optimal problem belongs to the NP-hard problems that can’t be solved in polynomial time. So, we can only get the approximate solution with a heuristic, such as genetic algorithm, simulated annealing and so on. Here, we select the genetic algorithm and write a program with Matlab2014.

<!-- b000233 | furniture | pages [16] -->
Team # 35532                                                                          15 / 34

<!-- b000234 | prose | pages [16] -->
Running the program repeatedly, we obtain a relatively good results and make our plan: There are seven mental centers located in Kailahun, Makeni, Kambia, Kabala, Bo, Moyamba and Freetown respectively. The Fig. 7 shows the scope that every mental center manages.

<!-- b000235 | caption | pages [16] -->
Fig.7 locations of medical centers in Sierra Leone

<!-- b000236 | prose | pages [16] -->
Part III

<!-- b000237 | heading | pages [16] -->
1. Specify evaluation norms

<!-- b000238 | prose | pages [16] -->
As for the evaluation the Susceptible standard for Each region, there are mainly aspects that count: Population density, Temperature, Humidity, the situation of current disease infection, Open or under construction，economy，National Education and age. What follows in the section will hammer at accounting for the eight aspects.  Population density: Population density undoubtedly accounts for key proportion in the demand level of the drug evaluation. Because Ebola is a spirited contagion disease, not only patients but also corpses can be the source of infection. Therefore, if the population density is high, the rate of spread disease will be fast in general situation. However, in some area, the pollution density of the area is low, but almost people live in a central city (in fact, the pollution density of the city is high), we deal with data preprocessing, making the aspect more reasonable evaluation model. The pollution density of the area could be calculated as follows:

<!-- b000239 | prose | pages [16] -->
R  a n 1 n M n

<!-- b000240 | prose | pages [16] -->
the pollution of the number n area. R : n

<!-- b000241 | prose | pages [16] -->
the acreage of the number n area. M : n

<!-- b000242 | prose | pages [16] -->
The pollution density of the main city in the area could be calculated as follows:

<!-- b000243 | furniture | pages [17] -->
Team # 35532                                                                          16 / 34

<!-- b000244 | prose | pages [17] -->
r  a n 2 n m n

<!-- b000245 | prose | pages [17] -->
the pollution of the main city number n area . nr :

<!-- b000246 | prose | pages [17] -->
the acreage of the main city number n area. m : n

<!-- b000247 | prose | pages [17] -->
We define a new population density which could be calculated as follows:

<!-- b000248 | prose | pages [17] -->
 ( a a )       2 n 1 n A a b a b b n 1 n 1 2 n 2 3 a 2 n    b b b 1 1 2 3

<!-- b000249 | prose | pages [17] -->
 . The numerical value depend on the ( a a ) 2 n 1 n

<!-- b000250 | prose | pages [17] -->
By the above calculation, the population density in the evaluation of the model is more reasonable and accurate.  Temperature Form the past Information and data, the Ebola usually outbreak in the summer ,but in the winter, the entire epidemic have been more effective control, and the status of major outbreaks in Africa is the lower latitudes area, which shows that the temperature is an important aspects in the demand level of the drug evaluation. The temperature of the area is:

<!-- b000251 | prose | pages [17] -->
B n

<!-- b000252 | prose | pages [17] -->
 Humidity Ebola outbreak in the areas which the annual precipitation is high and harmonious, especially in the tropical rain forest areas with high coverage. The World Health Organization's report shows that humid climate is conducive to the spread of the virus, therefore, we choose the humidity as an aspects in the evaluation model.

<!-- b000253 | prose | pages [17] -->
The temperature of the area is

<!-- b000254 | prose | pages [17] -->
C n

<!-- b000255 | prose | pages [17] -->
 current disease infection Current infection situation has a great impact on the future of the epidemic. The country who has large number of infected persons face the challenges in future, and need support from World Health Organization. Every patient will require substantial and large investment Because Ebola is highly infectious diseases. Therefore, we believe that using the number of patients to measure a country's entire national epidemic of severe is reasonable. The Infected people number of the area is

<!-- b000256 | prose | pages [17] -->
nI

<!-- b000257 | prose | pages [17, 18] -->
 Open or under construction As we all know, controlling the flow of people is an effective measure to prevent further deterioration of infectious diseases, On the one hand, under construction can control the spread of infection to uninfected areas, on the other hand, it have the ability to reduce the risk of infection of healthy people in infected area.

<!-- b000258 | furniture | pages [18] -->
Team # 35532                                                                          17 / 34

<!-- b000260 | prose | pages [18] -->
In a country, some cities under opening while some cities under closing (we only consider the large cities of the country).

<!-- b000261 | prose | pages [18] -->
We define Open coefficient which could be calculated as follows:

<!-- b000262 | prose | pages [18] -->
c open  F n c all

<!-- b000263 | prose | pages [18] -->
： the number of open cities in the country c open

<!-- b000264 | prose | pages [18] -->
： the number of all cities in the country. c all

<!-- b000265 | prose | pages [18] -->
 Economy In general situation, the more backward economy countries is the more difficult to control the disease is. Therefore, the economic situation of a country is an important indicator to determine the national level in the medical facilities. The lower the country's GDP means the more difficult to control Ebola infection because of under-developed Medical infrastructure. We use the GDP per capita as the aspects to show the economy of the area.

<!-- b000266 | prose | pages [18] -->
The economy of the area is：

<!-- b000267 | prose | pages [18] -->
E n

<!-- b000268 | prose | pages [18] -->
National Education [7]  Cremation in Africa do not comply with the local traditions, which is an important reason for the large-scale outbreak of Ebola. Ebola can spread through the corpses which lead a large number of people infected at the funeral. According to the survey, the higher the education level is, the greater the proportion of accept cremation. Therefore, we choose each country received higher education as a measure of the proportion of the country's level of education. The national education of the area is：

<!-- b000269 | prose | pages [18] -->
J n

<!-- b000270 | prose | pages [18] -->
Age[8]  According to the report of the World Health Organization, the probability of illness in young adults over the age of 14 is three times the age of 14, the probability of illness aged 65 or older is four times the age of 14. Thus, we can see that the higher proportion of the population over the age of 14 is, the greater the overall probability of illness is. We define age coefficient which could be calculated as follows:

<!-- b000271 | prose | pages [18] -->
 K K  14~65 65 K K all

<!-- b000272 | heading | pages [18] -->
Model

<!-- b000273 | furniture | pages [19] -->
Team # 35532                                                                          18 / 34

<!-- b000274 | heading | pages [19] -->
Introduction:

<!-- b000275 | prose | pages [19] -->
TOPSIS (technique for order performance by similarity to ideal solution) is a useful technique in dealing with multiattribute or multi-criteria decision making (MADM/MCDM) problems in the real world[9]. It helps decision maker organize the problems to be solved, and carry out analysis, comparisons and rankings of the alternatives. Accordingly, the selection of a suitable alternative(s) will be made. However, many decision making problems within organizations will be a collaborative effort. Hence, this model will extend TOPSIS to evaluate the demand of the drug. A complete and efficient procedure for decision making will then be provided.  Step one Since the different factors have greatly different in magnitude, we should normalized the

<!-- b000276 | prose | pages [19] -->
value of this factors. the normalized value X of the decision matrix X can be any linear- k ij

<!-- b000277 | prose | pages [19] -->
scale transformation to keep0   k . X 1 ij

<!-- b000278 | prose | pages [19] -->
We consider that the normalized value of X is the value of the corresponding element X k k ij ij

<!-- b000279 | prose | pages [19] -->
divided by the operation of its column elements, i.e., vector normalization, then (take the factor as example).

<!-- b000280 | prose | pages [19] -->
A  k X n m 1    2 2 2 A A A 1 2 n

<!-- b000281 | prose | pages [19] -->
 Step two: Construct decision matrix X The structure of the matrix can be expressed as follows:

<!-- b000282 | heading | pages [19] -->
X X

<!-- b000283 | heading | pages [19] -->
X X

<!-- b000284 | prose | pages [19] -->
1 2 n   k k k k x

<!-- b000285 | heading | pages [19] -->
X X

<!-- b000286 | heading | pages [19] -->
X X

<!-- b000287 | prose | pages [19] -->
1 11 12 1 j 1 n   k k k k x

<!-- b000288 | heading | pages [19] -->
X X

<!-- b000289 | heading | pages [19] -->
X X

<!-- b000290 | prose | pages [19] -->
  2 21 22 2 j 2 n    X   k k k k

<!-- b000291 | heading | pages [19] -->
X X

<!-- b000292 | heading | pages [19] -->
X X

<!-- b000293 | prose | pages [19] -->
x   i 1 i 2 ij in i     k k k k

<!-- b000294 | heading | pages [19] -->
X X

<!-- b000295 | heading | pages [19] -->
X X

<!-- b000296 | prose | pages [19] -->
  x   m 1 m 2 mj mn m

<!-- b000297 | prose | pages [19] -->
X represents the attribute or criterion j , ix denotes the alternativei , =1,2 Where ; i , m ， i

<!-- b000298 | prose | pages [19] -->
; j =1,2 , n ，

<!-- b000299 | prose | pages [19] -->
In the model, ix means different country, and X means different factors in the evaluation. i

<!-- b000300 | prose | pages [19] -->
Observe that we can also set the outcomes of qualitative attributes from each alternative as discrete values, e.g., 1 to 10 or linguistics values, so that the quantitative values will be placed in the above decision matrix. For example, current disease infection is a factor which we can’t evaluate it directly, we can use some Index to show it[10].  Step three

<!-- b000301 | prose | pages [19, 20] -->
Determine the ideal and negative ideal solutions V and V . - k k           k k k

<!-- b000302 | furniture | pages [20] -->
Team # 35532                                                                          19 / 34

<!-- b000304 | heading | pages [20] -->
V X

<!-- b000305 | prose | pages [20] -->
= , , X max X | j 1,2, , m k 1 n ij i         - k - k - k

<!-- b000306 | heading | pages [20] -->
V X

<!-- b000307 | prose | pages [20] -->
= , , X min X | j 1,2, , m k 1 n ij i  Step four

<!-- b000308 | prose | pages [20] -->
Calculate the separation measure from the ideal and the negative ideal solutions, iS  and iS , -

<!-- b000309 | prose | pages [20] -->
respectively, for the group.

<!-- b000310 | prose | pages [20] -->
n  v    + k k 2 S = ( v ) for alternati vei i , 1, , m ， i ij j  j 1

<!-- b000311 | prose | pages [20] -->
n  v    - k k 2 S = ( v ) for alternati vei i , 1, , m ， i ij j  j 1

<!-- b000312 | prose | pages [20] -->
 Step five Calculate the relative closeness C to the ideal solution for the group. Calculate the relative closeness to the ideal solution and rank the alternatives in descending

<!-- b000313 | prose | pages [20] -->
order. The relative closeness of the i th alternative iA with respect to positive idea solution

<!-- b000314 | prose | pages [20] -->
can be expressed as

<!-- b000315 | prose | pages [20] -->
 S   i C , i 1, , m    S S i i    The larger the index value, the better the performance of the alternative. Where 0 C 1

<!-- b000316 | heading | pages [20] -->
2. Collect data

<!-- b000317 | prose | pages [20] -->
To evaluate h of every districts, Many data is needed, we can find every district’s data needed for our specific evaluation norms by searching from the website，like Wikipedia and WHO. We finally conclude the relative statistics of those areas and list them in a form.

<!-- b000318 | caption | pages [20] -->
Table4:the data of the different district

<!-- b000319 | prose | pages [20] -->
Population Open Temperature Humidity Current density coefficient (ºC) (%) disease situation

<!-- b000320 | prose | pages [20, 21] -->
458.1595 100 24 94 4 Kailahun 4697.336 100 23 94 4 Kenema 2618.687 0 21 87 3 Kono 267.3536 100 26 81 2 Bombali 281.6377 50 24 94 3 Kambia 860.1828 100 22 89 5 Port Loko 299.7132 50 22 69 4 Koinadugu 1740.713 0 23 83 4 Tonkolili 266.1477 100 23 94 4 Bo 1248.725 50 24 91 1 Bonthe 392.2557 100 23 93 4 Moyamba 1176.208 50 25 89 3 Pujehun 25996.65 50 26 81 5 Western Area Note :1.the unit of the population denisty is People /per km Then we use the data to calculate the h with TOPSIS, and the results has been shown Table 3.

<!-- b000321 | furniture | pages [21] -->
Team # 35532                                                                          20 / 34

<!-- b000323 | prose | pages [21] -->
The effect on  of external factors

<!-- b000324 | prose | pages [21] -->
By analysis, we find that  not only is associated with the nature of the epidemic but also

<!-- b000325 | prose | pages [21] -->
affected by some external factors. These factors include population density, temperature, humidity, current epidemic situation ,open degree of ETC, economy, national education and

<!-- b000326 | prose | pages [21] -->
age. Hence,  vary from country to country. Some of these factors are change with time,

<!-- b000327 | prose | pages [21] -->
which result  changing with time. If we want to develop different reasonable long-term

<!-- b000328 | prose | pages [21] -->
delivery system for different countries, evaluating the external factor’s impact on  is needed.

<!-- b000329 | prose | pages [21] -->
For the same reason, we can estimate the effect of external facts on  with TOPSIS. We

<!-- b000330 | prose | pages [21] -->
define a influence coefficient C .usually, C is non-negative, and as it increase,  also

<!-- b000331 | prose | pages [21] -->
appear a growth.

<!-- b000332 | prose | pages [21] -->
The first four factors: population density, temperature, humidity, the current epidemic situation are defined as before. Obviously, their addition will result in increment of C. the other factors are redefined or defined as follows:  Open degree of ETC(Ebola treatment centers)

<!-- b000333 | prose | pages [21] -->
Considering there are many ETCs in a country, we redefine the open degree of ETC: ih

<!-- b000334 | prose | pages [21] -->
which could be calculated as follows:

<!-- b000335 | prose | pages [21] -->
c  F all n c open

<!-- b000336 | prose | pages [21] -->
c Where is the number of open ETCs in the country, open

<!-- b000337 | prose | pages [21] -->
is the number of cities in the country. c all

<!-- b000338 | prose | pages [21] -->
 Economy In general situation, the more undeveloped a country is, the more difficult to control the epidemic is. Therefore, the economic situation of a country, measured by GDP per capital is an important indicator to determine the medical treatment level.

<!-- b000339 | prose | pages [21] -->
The economy of the n th country is represented by：

<!-- b000340 | prose | pages [21] -->
E n

<!-- b000341 | prose | pages [21, 22] -->
 National Education Cremation do not comply with the local traditions in Africa, which is an important reason for the large-scale outbreak of Ebola. Ebola can spread through the corpses which lead a large number of people infected at the funeral. According to the survey, the higher the education level is, the greater the proportion of accept cremation is. Therefore, we choose the proportion of people received higher education in each country as a measure of the country's education level,

<!-- b000342 | furniture | pages [22] -->
Team # 35532                                                                          21 / 34

<!-- b000344 | prose | pages [22] -->
whose increment results increment of 

<!-- b000345 | prose | pages [22] -->
The education level of the n th country is represented by：

<!-- b000346 | prose | pages [22] -->
J n

<!-- b000347 | prose | pages [22] -->
 Age According to the report of the World Health Organization, the probability of being infected Ebola of young adults over the age of 14 is three times child below the age of 14, and the probability of poeple aged 65 or older is four times. Thus, we can see that the higher

<!-- b000348 | prose | pages [22] -->
proportion of the population over the age of 14 is, the greater the  will be. We define age

<!-- b000349 | prose | pages [22] -->
coefficient which could be calculated as follows:

<!-- b000350 | prose | pages [22] -->
 K K  14~65 65 K K all

<!-- b000351 | prose | pages [22] -->
Then we can use TOPSIS to estimate the variation of .

<!-- b000352 | prose | pages [22] -->
Considering the epidemic mainly spread in Sierra Leone, Guinea and Liberia, we select their data to solve our models and decide their drug allocation. By searching online carefully, we final get data needed from the website of World Bank.

<!-- b000353 | caption | pages [22] -->
Table 5: the data of the three country

<!-- b000354 | prose | pages [22] -->
current Temperature Humidity Open Economy education Population disease age (%) coefficient (dollar) (% of all) density (ºC) situation

<!-- b000355 | prose | pages [22] -->
2917 27 75 25 492 38.13 57.69 45.5 Guinea

<!-- b000356 | prose | pages [22] -->
8622 25 91 50 297 45.16 57.11 35.5 Liberia

<!-- b000357 | prose | pages [22] -->
Sierra 10518 27 85 85 366 26.44 58.44 79.4 Leone Note: the unit of the population is People /per km After calculating ,the results are shown in Table

<!-- b000358 | caption | pages [22] -->
Table 6 the initial influence coefficient of three country

<!-- b000359 | prose | pages [22] -->
C

<!-- b000360 | prose | pages [22, 23] -->
0.28615361 Guinea 0.467444301 Liberia 0.728861892 Sierra Leone C will be used later.

<!-- b000361 | furniture | pages [23] -->
Team # 35532                                                                          22 / 34

<!-- b000363 | prose | pages [23] -->
Part IV

<!-- b000364 | heading | pages [23] -->
Assumptions

<!-- b000365 | prose | pages [23] -->
 7 5 10 doses every year[14], we can calculate (1).Ebola drug production in the world can reach

<!-- b000366 | prose | pages [23] -->
the increment rate of production speed with this data.

<!-- b000367 | prose | pages [23] -->
 5 2 10 (2).The maximal amount of drugs produced per day can finally reach doses every year.

<!-- b000368 | prose | pages [23] -->
(3). Each patient needs 1 portion to rehabilitation, and each portion contain 10 doses drug. (4) Assumed that the drug distributed in every period of drug delivery are be used evenly every day.

<!-- b000369 | heading | pages [23] -->
Model:

<!-- b000370 | prose | pages [23] -->
Drug production model based logisitic. Because  This model meets these characteristic that the production in initial time is small, then sharp increase in the mid-production .and production in the finally time is large and stable.  the derivative of drug production rate increases at first and then decreases to zero. Therefore, we assume that the relationship between the drug production and time meets the logistic growth model, and the following equation can be listed:

<!-- b000371 | prose | pages [23] -->
dG G   rt (1 ) dg G m  G t ( ) 100 0

<!-- b000372 | prose | pages [23] -->
G :the daily production of drugs, namely the production speed.

<!-- b000373 | prose | pages [23] -->
G : the maximal production speed of drugs. m

<!-- b000374 | prose | pages [23] -->
rt : growth rate of drug production speed. amount of the drug delivered every time Our drug delivery plan think that there is only a drug delivery in a period of drug delivery

<!-- b000375 | prose | pages [23] -->
 T 14 days T . Let , Which is reasonable because it can save cost and don’t cause delay to p

<!-- b000376 | prose | pages [23] -->
the Ebola’s controlling.

<!-- b000377 | prose | pages [23] -->
Because drugs’ transporting need a certain period of time, and the drug output everyday, so we need to calculate the aggregate of drug which is the based of delivery.

<!-- b000378 | prose | pages [23] -->
 t T  n p P Gdt t t n n

<!-- b000379 | prose | pages [23] -->
nt ：the first day of the time period of drug delivery.

<!-- b000380 | prose | pages [23] -->
T : the period of drug delivery p

<!-- b000381 | heading | pages [23] -->
Delivery model

<!-- b000382 | prose | pages [23] -->
According to former analysis, drug production and drug demand change over time.

<!-- b000383 | furniture | pages [24] -->
Team # 35532                                                                          23 / 34

<!-- b000384 | prose | pages [24] -->
Comparing the drug production model and drug demand models, we can divide the whole duration into two stage: stage severely short in drugs and stage relative sufficient in drugs. now, we choose the 150th days as a time node.150th days ago, we faced with a severe drug shortage, and our purposes is to control the increment rate of the infectious .After 150th days, the production of the drugs achieve the certain number and the purpose become to reduce the number of death every day.

<!-- b000385 | heading | pages [24] -->
Delivery model at the stage severely short in drugs

<!-- b000386 | heading | pages [24] -->
Nonlinear programming model

<!-- b000387 | prose | pages [24] -->
In the first stage of drug manufacturing, Because of the great shortage in drug, many patients can’t get effective medical treatment, and the increment of the infectious and deaths are both high.

<!-- b000388 | prose | pages [24] -->
In this moment, we should give priority to the decrement of the increment of the infectious to make the epidemic becoming under the control as soon as possible which will benefit later epidemic controlling.

<!-- b000389 | prose | pages [24] -->
Hence, For the first stage of drug manufacturing, we build a nonlinear programming model:  the optimization goal which is minimizing the number of the infection sources of all countries:

<!-- b000390 | prose | pages [24] -->
k   Min I , i 1,2, , k i free ,  i 1

<!-- b000391 | prose | pages [24] -->
Where k is the number of countries needing drug assistance, and I is the average ,i free

<!-- b000392 | prose | pages [24] -->
number of infectious individuals non-isolated of the i th country in a period of drug delivery.

<!-- b000393 | prose | pages [24] -->
G t , ( )  the decision variables is the drug allocation distributed for each country noted by i

<!-- b000394 | prose | pages [24] -->
it refers the doses of drugs needed by the i th country.  the resistant condition is actual number of drugs.

<!-- b000395 | prose | pages [24] -->
k    G t ( ) P , i 1,2, , k i t n  i 1

<!-- b000396 | prose | pages [24] -->
Therefore, a Nonlinear programming optimization model of drug distribution is modeled as follows:

<!-- b000397 | prose | pages [24] -->
k  Min I , i free , i 1

<!-- b000398 | prose | pages [24] -->
k    G t ( ) P , i 1,2, , k i t n  i 1

<!-- b000399 | prose | pages [24] -->
 i 1,2 , k .

<!-- b000400 | prose | pages [24, 25] -->
delivery model at the stage relatively sufficient in drugs As time goes on, the speed of drug manufacturing grows rapidly. After a period of time, the speed of drugs become high enough to meet the need of every countries to control disease. In the moment, our goal become to minimize death cases every day with the number of the infectious stable. So, a multi-objective optimization model will be developed next based on the former model for the second stage.

<!-- b000401 | furniture | pages [25] -->
Team # 35532                                                                          24 / 34

<!-- b000403 | prose | pages [25] -->
Our goal can be described as follows:

<!-- b000404 | prose | pages [25] -->
k dD  i Min , dt i 1

<!-- b000405 | prose | pages [25] -->
dD i Where is the average death cases per day in a period of drug delivery. dt And

<!-- b000406 | prose | pages [25] -->
k  Min I , i free , i 1

<!-- b000407 | prose | pages [25] -->
At least making it stable. And there are two constraint condition, one is the drug amount restriction:

<!-- b000408 | prose | pages [25] -->
k    G t ( ) P , i 1,2, , k . i t n  i 1

<!-- b000409 | prose | pages [25] -->
The other is to consider the fairness to some extent:

<!-- b000410 | heading | pages [25] -->
I I

<!-- b000411 | prose | pages [25] -->
I k k 1 1     i free , i free , i free , ( ) 0.2 （11）. N k N k N   i 1 i 1 i i i

<!-- b000412 | prose | pages [25] -->
Where

<!-- b000413 | prose | pages [25] -->
N is i th country’s the total population. i

<!-- b000414 | prose | pages [25] -->
I I k 1  ,i free i free , is i th country’s percent of infectious individuals. is average percent N k N i 1 i i

<!-- b000415 | prose | pages [25] -->
of uncontrolled infectious individuals.

<!-- b000416 | prose | pages [25] -->
This shows the ration of difference between the proportion of patients non-isolated in all the population and the mean value of all the countries to the mean value of all the countries is less 20%. This will make the drug distribution is more evenly. The multi-objective optimization model can be described by following formulas:

<!-- b000417 | prose | pages [25] -->
k  min D , i  i 1 k  min I i free ,  i 1 k   s t . . G t ( ) P i t n  i 1

<!-- b000418 | furniture | pages [26] -->
Team # 35532                                                                          25 / 34

<!-- b000419 | heading | pages [26] -->
I I

<!-- b000420 | prose | pages [26] -->
I k k 1 1     i free , i free , i free , ( ) 0.2 N k N k N   i 1 i 1 i i i

<!-- b000421 | heading | pages [26] -->
D D

<!-- b000422 | prose | pages [26] -->
D k k 1 1     i free , i free , i free , ( ) 0.2 N k N k N   i 1 i 1 i i i

<!-- b000423 | prose | pages [26] -->
  G t ( ) 0 i

<!-- b000424 | heading | pages [26] -->
Results & analysis

<!-- b000425 | prose | pages [26] -->
 In the Drug production model, the formula (1 G G ) represent the resistance from the m

<!-- b000426 | prose | pages [26] -->
finite ability to manufacture drug. Obviously, as t goes on, rt becomes larger ，and

<!-- b000427 | prose | pages [26] -->
 (1 G G ) becomes smaller ，the increment of manufacturing speed of drugs depend both m

<!-- b000428 | prose | pages [26] -->
on them. According to the assumption (1) and (2), and supposed that at the 100th day, the manufacturing speed of drugs reaches the maximum, we can know that the maximal manufacturing speed of drugs

<!-- b000429 | prose | pages [26] -->
 5 G = 2 10 . m

<!-- b000430 | prose | pages [26] -->
And we solved the model with ode toolbox in Matlab2014 numerically. The result is shown in Fig.8.

<!-- b000431 | caption | pages [26] -->
Fig.8 the model based on logisitic

<!-- b000432 | prose | pages [26] -->
Since the epidemic mainly spread in Guinea, Liberia, Sierra Leone, we consider the situation where all the drugs are provided to these three country, and make a half-of-year drug delivery plan and predict the spreading trend in the half of year with the SEIIR model with efficient medication.

<!-- b000433 | prose | pages [26, 27] -->
Suppose we start to distribute the drug from the 100th day since the epidemic spread. Table.7 shows the value of parameters that moment.

<!-- b000434 | furniture | pages [27] -->
Team # 35532                                                                          26 / 34

<!-- b000436 | caption | pages [27] -->
Table 7 the value of parameters that moment

<!-- b000437 | prose | pages [27] -->
I I S E R D 0, free 0,isolated 0 0 0 0

<!-- b000438 | prose | pages [27] -->
12181398 4775 639 1209 243 1910 Guinea 4129792 9215 1228 2333 453 3686 Liberia Sierra 6223952 7799 1042 1079 475 3199 Leone In our plan, the period of drug delivery is 14 days, therefore, we will make the new delivery plan every 14 days. As we know from the former analysis, within the half of year, the value of

<!-- b000439 | prose | pages [27] -->
 vary from country to country and will change with time. Due to this, to recalculate the value

<!-- b000440 | prose | pages [27] -->
of  after a certain period time is also needed. We recalculate  with the TOSIS mentioned

<!-- b000441 | prose | pages [27] -->
above every month.

<!-- b000442 | prose | pages [27] -->
Solving the optimization model with optimization toolbox in Matlab2014. We get our delivery plan for six month shown as following table and figure.

<!-- b000443 | prose | pages [27, 28] -->
Infected Death portion Infected Death portion case case Case case 8380 2865 108 Guinea Guinea 8730 2984 456 Liberia 19334 5529 235 Liberia 23986 5769 679 15586 4798 345 Sierra Sierra 16142 5032 589 Leone Leone Infected Death portion Infected Death portion case case case case Guinea 16661 3284 685 Guinea 6905 3367 986 Liberia Liberia 21805 6169 891 18954 6398 1278 Sierra Sierra 16142 5648 981 13834 5781 1189 Leone Leone

<!-- b000444 | furniture | pages [28] -->
Team # 35532                                                                          27 / 34

<!-- b000446 | prose | pages [28] -->
Infect Death portion Infected Death portion ed case case case case Guinea 4101 3475 1230 Guinea 1771 3586 1580 Liberia Liberia 8747 6430 1806 2767 6529 2209 Sierra Sierra 8639 5863 1698 3910 5965 2497 Leone Leone The figures show the spreading trends of the Ebola in the three country in the next half of year. The tables show the total death cases and total infected cases at the moments delivering drugs .and the portions delivered to three country every time. According to the assumption (3), a portion of drugs equals to ten doses of drugs which can be used to cure one patient totally.

<!-- b000447 | heading | pages [28] -->
Conclusion

<!-- b000448 | prose | pages [28] -->
The isolation method and drug intervention can effectively control the EBOV spreading. And Drug manufacturing can also influence epidemic control. The difference between each country will cause the epidemic situation is different. So making epidemic control Strategy need consider a great deal.

<!-- b000449 | furniture | pages [29] -->
Team # 35532                                                                          28 / 34

<!-- b000450 | prose | pages [29] -->
Considering many factors including isolated method, drug intervention, geographical conditions, the differences between different countries, the characteristics of the spread of the virus, we build those models.

<!-- b000451 | prose | pages [29] -->
Model I can forecast the Infectious disease situation. Model II can determine the location of drug station. Model III can make the optimal choice of each country's number of drug. All of these help eradicating Ebola.

<!-- b000452 | heading | pages [29] -->
Model extending

<!-- b000453 | prose | pages [29] -->
In SEIIR with effective drug intervention model, we assume that medication only refers to drugs used therapy of Ebola, not include vaccine; Medications only work on patients but the vaccine can be used for individuals who live in the Susceptible area . Now we consider drugs and vaccines can simultaneously supply. The vaccines production is F dose per day. The drug production isG dose per day. Vaccine is able to let the individual to produce antibodies against the virus. So this formula (1) can be rewritten as  SI dS free   F t ( ). dt N At the same time putting the immune into the survivor population, then this formula (3) can be rewritten as

<!-- b000454 | prose | pages [29] -->
dR         (1 f ) I (1 f )

<!-- b000455 | heading | pages [29] -->
I M t

<!-- b000456 | prose | pages [29] -->
( ) F t ( ). . 1 free 2 isolated dt

<!-- b000457 | prose | pages [29] -->
SEIIR with effective drug intervention model was extended to SEIIR with effective drug and Vaccine intervention model. At the same time F Consistent with the Logistic block growth model，then

<!-- b000458 | prose | pages [29] -->
dF F   rt 1 (1 ) ， dg F m

<!-- b000459 | prose | pages [29] -->
 F t ( ) 100. 0

<!-- b000460 | prose | pages [29] -->
F is maximum of the vaccines production rate，1r is vaccines production growth rate. m

<!-- b000461 | heading | pages [29] -->
Sensitivity Analysis

<!-- b000462 | heading | pages [29] -->
SEIIR with effective drug intervention model

<!-- b000463 | prose | pages [29] -->
 There are some coefficients related to properties of the virus in SEIIR with effective drug intervention model:

<!-- b000464 | prose | pages [29] -->
1 : The average durations of incubation, 1 : the average durations of infectiousness, : the transmission rate.

<!-- b000465 | prose | pages [29] -->
We analysis the effect of the three factors on the death case by changing them.

<!-- b000466 | caption | pages [29] -->
Table 8:the three factors on the death case

<!-- b000467 | prose | pages [29, 30] -->
Initial value Changed value Changed percent 1  5.3 6 13.21% the death case 119556 124870 4.44%

<!-- b000468 | furniture | pages [30] -->
Team # 35532                                                                          29 / 34

<!-- b000470 | prose | pages [30] -->
1  5.61 6.3 12.31%

<!-- b000471 | prose | pages [30] -->
the death case 119556 131690 10.15%

<!-- b000472 | prose | pages [30] -->
 0.27 0.5 46%

<!-- b000473 | prose | pages [30] -->
the death case 119556 9343221 681.4%

<!-- b000474 | caption | pages [30] -->
Fig. 9: The

<!-- b000475 | prose | pages [30] -->
changes, and death cases

<!-- b000476 | prose | pages [30] -->
The table 8 shows that  is the factor which has the greatest effect on the death case

<!-- b000477 | prose | pages [30] -->
among the properties, and fig.9 shows the result graphicall

<!-- b000478 | prose | pages [30] -->
In conclusion, is a key factors to control Ebola, we can take some measures, such as control

<!-- b000479 | prose | pages [30] -->
the population density, isolation and so on, to reduce it.

<!-- b000480 | prose | pages [30] -->
E (2) Change the 0

<!-- b000481 | prose | pages [30] -->
S ,exposed When solving the models, we have set initial values of the initial susceptive 0

<!-- b000482 | prose | pages [30] -->
E ,infectious 0I ,etc. As for S , 0I , we can get relatively data from the data statistics of WHO. 0 0

<!-- b000483 | prose | pages [30, 31] -->
creases, and death cases increases E by estimation. So it is necessary to evaluate the effectiveness But we only can inaccurate 0

<!-- b000484 | caption | pages [30] -->
Fig.10:

<!-- b000485 | furniture | pages [31] -->
Team # 35532                                                                          30 / 34

<!-- b000487 | prose | pages [31] -->
E and observing the change of result. We change E from 10 to 1000 by step by changing 0 0

<!-- b000488 | prose | pages [31] -->
of 10.

<!-- b000489 | prose | pages [31] -->
E increases. In conclusion, As we can see from fig. 10, the death case increases related to 0

<!-- b000490 | prose | pages [31] -->
E can affect the result greatly. When we set model for predicting the future trend, we the 0

<!-- b000491 | prose | pages [31] -->
should determine the value of , E based on the reality situation , which will make the finally 0

<!-- b000492 | prose | pages [31] -->
forecasting more accurate.

<!-- b000493 | heading | pages [31] -->
(2) delivery systems model

<!-- b000494 | prose | pages [31] -->
When we build the drug delivery systems model, we use the Logistic block growth model describe the change of drug production speed with time. It’s a reasonable assumption. However, in the real world ,the relationship between the output of drug and time may vary from it. Not

<!-- b000495 | prose | pages [31] -->
only that, the coefficients r and G can also influent the results (r is the increase speed of m

<!-- b000496 | prose | pages [31] -->
G is the maximum daily output).Similarly, we study their influence by output growth rate; m

<!-- b000497 | prose | pages [31] -->
changing the value of them separately, The sensitivity tor .  The results of sensitivity analysis to r is shown on Table.9.

<!-- b000498 | prose | pages [31] -->
Table 9 The days use r The death case to control 50 250 629128 100(100%) 162(35.3%) 124870(80.1%) 200(400%) 102(59.2%) 272934(56.6%) From the Table 2, we find an obvious phenomenon that the bigger the value is ,the earlier the situation become under control.

<!-- b000499 | prose | pages [31] -->
G

<!-- b000500 | heading | pages [31] -->
The sensitivity to

<!-- b000501 | prose | pages [31] -->
 m

<!-- b000502 | prose | pages [31] -->
G have been changed from 100 to 10000 by step of 100. The m

<!-- b000503 | prose | pages [31] -->
We see the needed time to make the epidemic under the control is changed with the change of

<!-- b000504 | prose | pages [31, 32] -->
G in the Fig.11 m Fig.11 Epidemic controlling is very sensitive to the maximal daily output. The more the maximum daily output is, the less the death case is less. When the maximal daily output is under 4000 dose per day, the drug production can’t meet the need of epidemic controlling. When the maximum daily output is smaller, it is more difficult to control the epidemic and the death cases become high. Therefore, a way to control the epidemic and reduce the death cases is maximize the output every day and improve the increase speed of output growth rate.

<!-- b000505 | furniture | pages [32] -->
Team # 35532                                                                          31 / 34

<!-- b000507 | heading | pages [32] -->
Weakness and strengths

<!-- b000508 | heading | pages [32] -->
Weakness:

<!-- b000509 | prose | pages [32] -->
In model 1, according to the sensitivity analysis, the simulation results depend on largely the initial values of parameters and coefficients. But some values of the parameters can be only estimated, which can be inaccurate. In addition, the virus has a large probability of mutation, and some parameters will changed which we ignored, which will decrease the validity of the model. In model 2, to simplify the problem, we set all the medical centers at the capitals of districts.

<!-- b000510 | prose | pages [32] -->
And when calculating the shortest distance, we represent a district with its capital . In model 3, we build the optimization model without considering the vaccine.

<!-- b000511 | heading | pages [32] -->
Strengths

<!-- b000512 | prose | pages [32] -->
In model 1, we considered the influence of isolated people and improved our basic model through adding isolated people and drug intervention, which make the simulation more real and effective. The reasonable setting of the parameter ( ) , will bring the model the ability of self- regulation.

<!-- b000513 | prose | pages [32] -->
In model 2, when choosing locations of medical centers, considering the drug distribution point will not change once selected, we get our result from a long-term perspective. Which will make the results more reasonable.

<!-- b000514 | prose | pages [32, 33] -->
In model 3, we building a logistic block growth model about drug production. This model is reasonable. We consider two situations. The one is the condition of severe lacking drug, other one is the condition of relatively sufficient drug. At last we assume the disease is under control when the growth rate of infectious individuals develop into zero.

<!-- b000515 | furniture | pages [33] -->
Team # 35532                                                                          32 / 34

<!-- b000517 | heading | pages [33] -->
Letter for the world medical association

<!-- b000518 | prose | pages [33] -->
To the world medical association,

<!-- b000519 | prose | pages [33] -->
Ebola has received wide attention of people all over the world since 2014, and until now, the situation of the Ebola in Africa is still not optimistic. Recently, the number of the infected people appeared an increment again. With the coming warm rainy season, we must pay attention to the development trend of Ebola disease.

<!-- b000520 | prose | pages [33] -->
To prevent the spread of epidemic, we propose the following suggestion Based on our study:

<!-- b000521 | prose | pages [33] -->
National measures to control the epidemic infection Build strong and effective isolation to prevent deterioration of the condition, and focus on the patient in the incubation to avoid them a new source of infection before being isolated. Provide the public with the right to preventive methods by publicity, and reduce large gatherings in the public. The government should popularize cremation, even take lethal force cremation for death for Ebola patients with known. The government should control the regional migration.

<!-- b000522 | prose | pages [33] -->
For description of drug distribution Because the drug is in shortage, the need of each country medicines cannot be met. Therefore: Before drug production reach a certain amount, according to the different circumstances of each country and a reasonable prediction, we set a drug delivery system whose purpose is the overall controlled objectives, and the overall distribution of the situation is adjusted every two weeks. After drug production speed reach the necessary requirement .we use minimazing the number of deaths as the target for distribution. If you want to know more detailed analysis and the data, welcome to read our paper. We wish that Ebola will be controlled soon.

<!-- b000523 | prose | pages [33] -->
Yours sincerely

<!-- b000524 | heading | pages [33] -->
References

<!-- b000525 | references | pages [33] -->
[1] Baize S, Pannetier D, Oestereich L, et al. Emergence of Zaire Ebola virus disease in

<!-- b000526 | references | pages [33] -->
Guinea[J]. New England Journal of Medicine, 2014, 371(15): 1418-1425.

<!-- b000527 | references | pages [33] -->
World Health Organization: Ebola Virus Disease, West Africa –Update on 27.July 2014.

<!-- b000528 | references | pages [33] -->
2014.

<!-- b000529 | references | pages [33] -->
[2] Gire S K, Goba A, Andersen K G, et al. Genomic surveillance elucidates Ebola virus origin

<!-- b000530 | references | pages [33] -->
and transmission during the 2014 outbreak[J]. Science, 2014, 345(6202): 1369-1372.

<!-- b000531 | furniture | pages [34] -->
Team # 35532                                                                          33 / 34

<!-- b000532 | references | pages [34] -->
[3] Ebola Situation Report - 4 February 2015

<!-- b000533 | references | pages [34] -->
http://apps.who.int/ebola/en/ebola-situation-report/situation-reports/ebola-situation-report-4-

<!-- b000534 | references | pages [34] -->
february-2015

<!-- b000535 | references | pages [34] -->
Chowell G, Hengartner N W, Castillo-Chavez C, et al. The basic reproductive number of

<!-- b000536 | references | pages [34] -->
Ebola and the effects of public health measures: the cases of Congo and Uganda[J]. Journal of

<!-- b000537 | references | pages [34] -->
Theoretical Biology, 2004, 229(1): 119-126.

<!-- b000538 | references | pages [34] -->
[4] Althaus C L. Estimating the reproduction number of Zaire ebolavirus (EBOV) during the

<!-- b000539 | references | pages [34] -->
2014 outbreak in West Africa[J]. arXiv preprint arXiv:1408.3505, 2014.

<!-- b000540 | references | pages [34] -->
[5] Lekone, P. E. & Finkenstadt, B. F. 2006 Statistical inference in a stochastic epidemic SEIR

<!-- b000541 | references | pages [34] -->
model with control intervention: Ebola as a case study. Biometrics 62, 1170–

<!-- b000542 | references | pages [34] -->
7.doi:10.1111/j.1541-0420.2006.00609.x.

<!-- b000543 | references | pages [34] -->
[6] Hand hygiene for health workers caring for Ebola patients

<!-- b000544 | references | pages [34] -->
http://www.who.int/entity/csr/disease/ebola/hand-hygiene/en/index.html

<!-- b000545 | references | pages [34] -->
[7] Owen S H, Daskin M S. Strategic facility location: A review[J]. European Journal of

<!-- b000546 | references | pages [34] -->
Operational Research, 1998, 111(3): 423-447.

<!-- b000547 | references | pages [34] -->
[8] Ebola Situation Report - 4 February 2015

<!-- b000548 | references | pages [34] -->
http://apps.who.int/ebola/en/ebola-situation-report/situation-reports/ebola-situation-report-4-

<!-- b000549 | references | pages [34] -->
february-2015

<!-- b000550 | references | pages [34] -->
[9] S.M. Belenson, K.C. Kapur, An algorithm for solving multicriterion linear programming

<!-- b000551 | references | pages [34] -->
problems with examples, Operational Research Quarterly 24 (1) (1973) 65–77.

<!-- b000552 | references | pages [34] -->
[10] C.L. Hwang, K. Yoon, Multiple Attribute Decision Making, Springer-Verlag, Berlin,

<!-- b000553 | references | pages [34] -->
1981.

<!-- b000554 | references | pages [34] -->
[11] introduction about ebola

<!-- b000555 | references | pages [34] -->
http://www.who.int/csr/disease/ebola/en/

<!-- b000556 | references | pages [34] -->
[12] National Education

<!-- b000557 | references | pages [34] -->
Data.worldbank.com

<!-- b000558 | references | pages [34] -->
[13] Ebola Situation Report - 4 February 2015

<!-- b000559 | references | pages [34] -->
http://apps.who.int/ebola/en/ebola-situation-report/situation-reports/ebola-situation-

<!-- b000560 | references | pages [34] -->
report-4-february-2015

<!-- b000561 | references | pages [34] -->
[14] WHO approves Ebola trial drug

<!-- b000562 | references | pages [34] -->
http://english.cntv.cn/2014/08/13/VIDE1407889322218675.shtml
