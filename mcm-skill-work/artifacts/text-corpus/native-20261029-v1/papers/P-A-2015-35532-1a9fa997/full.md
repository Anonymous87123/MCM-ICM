# P-A-2015-35532-1a9fa997

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | title | pages [1] -->
35532

<!-- b000003 | prose | pages [1] -->
For office use only T1 ________________ T2 ________________

<!-- b000004 | furniture | pages [1] -->


<!-- b000005 | prose | pages [1] -->
T3 ________________

<!-- b000006 | prose | pages [1] -->
For office use only F1 ________________ F2 ________________ F3 ________________

<!-- b000007 | prose | pages [1] -->
Problem Chosen

<!-- b000008 | prose | pages [1] -->
T4 ________________

<!-- b000009 | furniture | pages [1] -->


<!-- b000010 | prose | pages [1] -->
F4 ________________

<!-- b000011 | title | pages [1] -->
A

<!-- b000012 | furniture | pages [1] -->


<!-- b000013 | furniture | pages [1] -->


<!-- b000014 | heading | pages [1] -->
2015 Mathematical Contest in Modeling (MCM) Summary Sheet

<!-- b000015 | heading | pages [1] -->
Summary

<!-- b000016 | prose | pages [1] -->
The complex epidemic of Zaire ebolavirus has been affecting West Africa. A series of realistic, sensible, and useful mathematical model about Ebola of spreading and medication delivery are developed to eradicating Ebola.

<!-- b000017 | prose | pages [1] -->
First, we divide the spreading of disease into three periods: naturally spreading period, spreading period with isolation but without effective medications and spreading period with effective medications. We develop a SEIR (susceptible-exposed-infectious-recovered) model to simulate the spread of the disease in the primary period. Then the model are improved to a SEIQR (susceptible-exposed-infectious-quarantined-recovered) model to adapt to the second and third period and to predict the future trends in Guinea, Sierra Leone and Liberia.

<!-- b000018 | prose | pages [1] -->
According to our plan, drugs are delivered to countries in need separately by air, then to medical centers by highway and be used for therapy of patients there. To solve the problem of location decision of medical centers, which belongs to a set covering problem, we developed a multi-objective optimization model. The model’s goal is minimizing the numbers of medical centers and total patients’ time cost on the road on the condition that all of patients can be sent a medical center in time. We solved the model with genetic algorithm, and get an approximate optimal solution with 7 medical centers. Then we built a logistic block growth model to describe the changing speed of drugs manufacturing. Comparing it with the SEIIR model, we considered the two situations: one is in severe shortage of drugs, the other is relatively sufficient in drugs. We built two optimization models for the two situations. The optimization goal is minimizing the number of the infectious and minimizing of death cases and the number of infectious individuals, respectively. The decision variables is the drug allocation for every country, and the constraint conditions is drug production.

<!-- b000019 | prose | pages [1] -->
Finally, by a comprehensive analysis, we made a six-month drug delivery plan for Guinea, Liberia and Sierra Leone, and predict the spreading trends of Ebola in the next six month with the efficient medication’s blockage.

<!-- b000020 | prose | pages [1] -->
The sensitivity analysis of our models has pointed out that the transmission rate and the initial value setting will affect the result greatly. We find that the speed of drug manufacturing’s growth rate r may control of the epidemic. The minimum daily output of drugs G must m greater than 4000. Otherwise ,the epidemic will be out of control.

<!-- b000021 | furniture | pages [1] -->


<!-- b000022 | furniture | pages [1] -->


<!-- b000023 | furniture | pages [1] -->


<!-- b000024 | furniture | pages [2] -->
Team # 35532                                                                          1 / 34

<!-- b000025 | furniture | pages [2] -->


<!-- b000026 | heading | pages [2] -->
Introduction

<!-- b000027 | prose | pages [2] -->
Problem background

<!-- b000028 | prose | pages [2] -->
A complex epidemic of Zaire Ebola virus (EBOV) has been affecting West Africa since

<!-- b000029 | furniture | pages [2] -->


<!-- b000030 | prose | pages [2] -->
approximately December 2013, with first cases likely occurring in southern Guinea [1] and facilitating several transmission chains to progress essentially unchecked in the region and to cross porous borders with neighboring Sierra Leone and Liberia and seed a limited outbreak in Nigeria via commercial airplane on 20 July 2014 [2]. Then the number of new cases appear an exponential growth. While public health interventions have been introduced in all affected countries, the numbers of infected cases and deaths from EBOV continue to increase due to the loss of effective medication. A total of 22,495 cases, with 8,981 deaths, have been reported to the World Health Organization as of 4 February 2015[3].

<!-- b000031 | prose | pages [2] -->
Our work

<!-- b000032 | prose | pages [2] -->
Since new anti-Ebola drug has been developed, a realistic, sensible, and useful mathematical model about drug allocation and delivery is necessary. Depending on the goal, we divide the spread of disease into three periods: naturally spreading period, spreading period with intervention and spreading period with effective medications. And then we develop a SEIR (susceptible-exposed-infectious-recovered) model to simulate the spread of the disease in the primary period, based on the changing trend of the numbers of infected cases and deaths. Finally, the model are improved to a SEIIR (susceptible-exposed-infectious-isolated-recovered) model to adapt to the second and third period and to predict the future trends in Guinea, Sierra Leone and Liberia.

<!-- b000033 | prose | pages [2] -->
A delivery system include two main parts: numbers and locations of medical central delivering drugs decision and drug allocation of every medical center. For this reason, an evaluation system of every country’s long-term epidemic situation, two multi-objective optimization are built separately. We developed a detailed plan via our models.

<!-- b000034 | prose | pages [2] -->
Symbols and definitions

<!-- b000035 | heading | pages [2] -->
(1) Symbol for SEIIR model with effective medication

<!-- b000036 | heading | pages [2] -->
Symbol

<!-- b000037 | prose | pages [2] -->
S

<!-- b000038 | prose | pages [2] -->
E I

<!-- b000039 | prose | pages [2] -->
I

<!-- b000040 | furniture | pages [2] -->


<!-- b000041 | prose | pages [2] -->
isolated

<!-- b000042 | prose | pages [2] -->
I

<!-- b000043 | furniture | pages [2] -->


<!-- b000044 | prose | pages [2] -->
free

<!-- b000045 | prose | pages [2] -->
R

<!-- b000046 | prose | pages [2] -->
D

<!-- b000047 | prose | pages [2] -->
definitions susceptible individuals

<!-- b000048 | prose | pages [2] -->
exposed individuals infectious individuals

<!-- b000049 | prose | pages [2] -->
isolated infectious individuals

<!-- b000050 | prose | pages [2] -->
non- isolated infectious individuals

<!-- b000051 | prose | pages [2] -->
recover and survive individuals

<!-- b000052 | prose | pages [2] -->
death case

<!-- b000053 | furniture | pages [3] -->
Team # 35532                                                                          2 / 34

<!-- b000054 | furniture | pages [3] -->


<!-- b000055 | prose | pages [3] -->
N

<!-- b000056 | prose | pages [3] -->


<!-- b000057 | prose | pages [3] -->
1 

<!-- b000058 | prose | pages [3] -->
1 

<!-- b000059 | prose | pages [3] -->
total population of the area

<!-- b000060 | prose | pages [3] -->
The transmission rate of EBOV

<!-- b000061 | prose | pages [3] -->
the average durations of incubation.

<!-- b000062 | prose | pages [3] -->
the average durations of infectiousness

<!-- b000063 | prose | pages [3] -->
f

<!-- b000064 | prose | pages [3] -->


<!-- b000065 | prose | pages [3] -->
1f

<!-- b000066 | prose | pages [3] -->
the case fatality rate

<!-- b000067 | prose | pages [3] -->
the ratio of new non-isolated infective

<!-- b000068 | prose | pages [3] -->
patients

<!-- b000069 | prose | pages [3] -->
the non- isolated individuals fatality rate

<!-- b000070 | prose | pages [3] -->
2f

<!-- b000071 | prose | pages [3] -->
G t ( )

<!-- b000072 | furniture | pages [3] -->


<!-- b000073 | heading | pages [3] -->
(2)Symbol for model II

<!-- b000074 | heading | pages [3] -->
Symbol

<!-- b000075 | prose | pages [3] -->
p

<!-- b000076 | prose | pages [3] -->
the isolated individuals fatality rate

<!-- b000077 | prose | pages [3] -->
number of drug supply

<!-- b000078 | prose | pages [3] -->
definitions

<!-- b000079 | prose | pages [3] -->
the number of capitals of first-level administrative divisions in a country

<!-- b000080 | prose | pages [3] -->
the number of medical centers for EVD set q

<!-- b000081 | prose | pages [3] -->
   V v v , , , v , , v

<!-- b000082 | furniture | pages [3] -->


<!-- b000083 | prose | pages [3] -->
1 2 i p

<!-- b000084 | prose | pages [3] -->
   X x x , , x , x

<!-- b000085 | furniture | pages [3] -->


<!-- b000086 | prose | pages [3] -->
1 2 j q

<!-- b000087 | prose | pages [3] -->
d x y ( , )

<!-- b000088 | prose | pages [3] -->
in a country;

<!-- b000089 | prose | pages [3] -->
the set of capitals

<!-- b000090 | prose | pages [3] -->
the set of medical centers

<!-- b000091 | prose | pages [3] -->
he shortest distance from x to y

<!-- b000092 | prose | pages [3] -->
the metric of quantity of drug needed of the ih

<!-- b000093 | prose | pages [3] -->
i th administrative in the coming period

<!-- b000094 | prose | pages [3] -->
the population of the nth administrative R n

<!-- b000095 | prose | pages [3] -->
division

<!-- b000096 | prose | pages [3] -->
the area of the nth administrative division M n

<!-- b000097 | prose | pages [3] -->
the population of the main city of the nth nr :

<!-- b000098 | furniture | pages [3] -->


<!-- b000099 | prose | pages [3] -->
m :

<!-- b000100 | furniture | pages [3] -->


<!-- b000101 | prose | pages [3] -->
n

<!-- b000102 | prose | pages [3] -->
administrative division.

<!-- b000103 | prose | pages [3] -->
the area of the main city of the nth

<!-- b000104 | prose | pages [3] -->
administrative division.

<!-- b000105 | prose | pages [3] -->
the temperature of the nth administrative B n

<!-- b000106 | prose | pages [3] -->
nI

<!-- b000107 | prose | pages [3] -->
division

<!-- b000108 | prose | pages [3] -->
the Infected people number of the nth administrative division is represented

<!-- b000109 | furniture | pages [4] -->
Team # 35532                                                                          3 / 34

<!-- b000110 | furniture | pages [4] -->


<!-- b000111 | prose | pages [4] -->
F open degree of Ebola treatment centers n

<!-- b000112 | prose | pages [4] -->
the temperature of the nth administrative

<!-- b000113 | prose | pages [4] -->
C n

<!-- b000114 | prose | pages [4] -->
division

<!-- b000115 | prose | pages [4] -->
open degree of Ebola treatment centers F n

<!-- b000116 | prose | pages [4] -->
the number of open ETCs in the country

<!-- b000117 | prose | pages [4] -->
c open

<!-- b000118 | furniture | pages [4] -->


<!-- b000119 | prose | pages [4] -->
the number of cities in the country

<!-- b000120 | prose | pages [4] -->
c all

<!-- b000121 | furniture | pages [4] -->


<!-- b000122 | prose | pages [4] -->
The economy of the n th country

<!-- b000123 | prose | pages [4] -->
E n

<!-- b000124 | prose | pages [4] -->
The education level of the n th country i

<!-- b000125 | prose | pages [4] -->
J n

<!-- b000126 | prose | pages [4] -->
K age coefficient

<!-- b000127 | furniture | pages [4] -->


<!-- b000128 | heading | pages [4] -->
(3)Symbol for model III

<!-- b000129 | heading | pages [4] -->
Symbol

<!-- b000130 | prose | pages [4] -->
G

<!-- b000131 | prose | pages [4] -->
G

<!-- b000132 | prose | pages [4] -->
definitions The average daily production of drugs.

<!-- b000133 | prose | pages [4] -->
the maximum production rate of the drugs. m

<!-- b000134 | prose | pages [4] -->
rt

<!-- b000135 | prose | pages [4] -->
ntP

<!-- b000136 | prose | pages [4] -->
nt

<!-- b000137 | prose | pages [4] -->
T p

<!-- b000138 | prose | pages [4] -->
I

<!-- b000139 | furniture | pages [4] -->


<!-- b000140 | prose | pages [4] -->
,i free

<!-- b000141 | prose | pages [4] -->
G t ( ) i

<!-- b000142 | prose | pages [4] -->
N i

<!-- b000143 | prose | pages [4] -->
D i

<!-- b000144 | heading | pages [4] -->
Assumptions

<!-- b000145 | prose | pages [4] -->
growth trends in drug production speed

<!-- b000146 | prose | pages [4] -->
the aggregate of drug

<!-- b000147 | prose | pages [4] -->
the first day of the time period of drug

<!-- b000148 | prose | pages [4] -->
delivery.

<!-- b000149 | prose | pages [4] -->
the time period of drug delivery

<!-- b000150 | prose | pages [4] -->
the number of non-isolated infectious

<!-- b000151 | prose | pages [4] -->
individuals

<!-- b000152 | prose | pages [4] -->
i th country’s number of the drug

<!-- b000153 | prose | pages [4] -->
i th country’s the total population

<!-- b000154 | prose | pages [4] -->
i th country’s death cases

<!-- b000155 | prose | pages [4] -->
1. In early transmission period, EBOV spread in absence of control interventions. 2. The average duration of the incubation and infectious period were fixed to previous estimates

<!-- b000156 | prose | pages [4] -->
from an outbreak of the same EBOV subtype in Congo in 1995 (1  = 5 .3 days and1  =

<!-- b000157 | prose | pages [4] -->
5 .61 days) [3]. 3. Infection only occurs between the patients who are not isolated and susceptible.

<!-- b000158 | furniture | pages [5] -->
Team # 35532                                                                          4 / 34

<!-- b000159 | furniture | pages [5] -->


<!-- b000160 | prose | pages [5] -->
4. Even if without effective medication, the mortality rate of isolated patients is lower than that of free patients. 5. People who have recovered from Ebola will obtain the long-term immunity against Ebola. 6. Only being sent to medical center and isolated, affected people have the chance to receive therapy. 7. Ignoring patient’s different condition, the quantity of the medicine needed by all affected people whose disease is not advanced during the whole therapy is equal to one portion of drugs.

<!-- b000161 | heading | pages [5] -->
8. The population of the region we study is a constant N

<!-- b000162 | prose | pages [5] -->
9. The transmission only occurs btween only the susceptible and the infective. 10. Patients isolated will not affect the suspective. In other word,their effective contact rate equals to zero. 11 .The medication only refers to drugs used therapy of Ebola, not include vaccine. 12. If affected people want to accept therapy, they must get to a medical center set as delivering medication. 13. If a patient in whom symptoms of Ebola has appeared don’t get a medical central (usually the nearest medical center) in 24 hours, the new medication won’t affect his disease. 14. We set all the medical centers at the capitals of first-level administrative divisions. 15. We use the capital of an administrative division as a representation of the administrative

<!-- b000163 | heading | pages [5] -->
Model I

<!-- b000164 | heading | pages [5] -->
SEIR model

<!-- b000165 | prose | pages [5] -->
After transmission of the virus, susceptible individuals S enter the exposed class E before they become infectious individuals I that either recover and survive R or die D .

<!-- b000166 | caption | pages [5] -->
Fig.1 shows the process.

<!-- b000167 | caption | pages [5] -->
Fig.1 the process of the model

<!-- b000168 | furniture | pages [5] -->


<!-- b000169 | furniture | pages [5] -->


<!-- b000170 | prose | pages [5] -->
According to the it，people can be divided into four class: the susceptible ( S ), who are susceptible to infection.  the exposed( E ), who are affected but in the incubation.  the infectious ( I ), who are infected and have the symptom.  the recovered( R ), who recover or survive.  The total population of the area is N , and

<!-- b000171 | prose | pages [5] -->
  N S  E E I R , according to the assumption 8. Numbers of all kinds of people in the initial time are shown as follows:

<!-- b000172 | prose | pages [5] -->
    S (0) S 0 E (0) E , 0 0    0 0 I (0) I 0 R (0) R =0 , , ,

<!-- b000173 | furniture | pages [5] -->


<!-- b000174 | prose | pages [5] -->
0 0

<!-- b000175 | prose | pages [5] -->
Let  be the contact rate in absence of control interventions. S N is the proportion of the

<!-- b000176 | prose | pages [5] -->
 S N susceptible in total population. Hence, the effective contact rate is , and in a unit of time,

<!-- b000177 | furniture | pages [6] -->
Team # 35532                                                                          5 / 34

<!-- b000178 | furniture | pages [6] -->


<!-- b000179 | prose | pages [6] -->
 SI N .In other words, the rate of change in the number of the the number of new patients is

<!-- b000180 | prose | pages [6] -->
susceptible is

<!-- b000181 | prose | pages [6] -->
d S  d t

<!-- b000182 | prose | pages [6] -->
 E

<!-- b000183 | prose | pages [6] -->
 S I .   (1) N

<!-- b000184 | prose | pages [6] -->
is the number of people newly entering the infectious. Therefore, We assumed that

<!-- b000185 | prose | pages [6] -->
1 is the average durations of incubation. As for the number of people newly entering the

<!-- b000186 | prose | pages [6] -->
exposed every day, it can be calculated as follows:

<!-- b000187 | prose | pages [6] -->
 dE SI  dt N   E (2)

<!-- b000188 | prose | pages [6] -->
In the same manner, we calculate the increment of the infective people:

<!-- b000189 | prose | pages [6] -->
dI  dt     E I ,

<!-- b000190 | prose | pages [6] -->
Where  is sum of natural cure rate and mortality of the infectious. 1 can be seen the

<!-- b000191 | prose | pages [6] -->
average durations of infectiousness. Suppose the case fatality rate is given by f , then

<!-- b000192 | prose | pages [6] -->
  (1 f ) I is the number of death per day. Thus, the changing rate of recovery case and death

<!-- b000193 | prose | pages [6] -->
case with time can be represented as follows respectively:

<!-- b000194 | prose | pages [6] -->
dR  (1 dt

<!-- b000195 | prose | pages [6] -->
dD dt

<!-- b000196 | prose | pages [6] -->
   f f ) I , (3)

<!-- b000197 | prose | pages [6] -->
   f I .

<!-- b000198 | prose | pages [6] -->
From the above analysis results, We described the early transmission of EBOV as a SEIR (susceptible-exposed-infectious-recovered) dynamics model.

<!-- b000199 | heading | pages [6] -->
Result

<!-- b000200 | prose | pages [6] -->
The average duration of the incubation and infectious period were fixed to previous estimates

<!-- b000201 | prose | pages [6] -->
from an outbreak of the same EBOV subtype in Congo in 1995 (1 = 5 .3 days and1  = 5 .61

<!-- b000202 | prose | pages [6] -->
days).The other parameter has been given by Chowell et al [4]. All important parameters’ value are listed in Table 1.

<!-- b000203 | caption | pages [6] -->
Table 1. Parameter estimates for the 2014 EBOV outbreak

<!-- b000204 | prose | pages [6] -->
Parameter

<!-- b000205 | prose | pages [6] -->
The average durations of incubation, 1 

<!-- b000206 | prose | pages [6] -->
Guinea Sierra Leone Liberia

<!-- b000207 | prose | pages [6] -->
5.3 5.3 5.3

<!-- b000208 | furniture | pages [7] -->
Team # 35532                                                                          6 / 34

<!-- b000209 | furniture | pages [7] -->


<!-- b000210 | prose | pages [7] -->
the average durations of infectiousness, 1 

<!-- b000211 | prose | pages [7] -->
Transmission rate, 

<!-- b000212 | prose | pages [7] -->
Case fatality rate, f

<!-- b000213 | prose | pages [7] -->
Date of appearance of first infectious case, T

<!-- b000214 | prose | pages [7] -->
5.61 5.61 5.61

<!-- b000215 | prose | pages [7] -->
0.27 0.43 0.29

<!-- b000216 | prose | pages [7] -->
0.75 0.49 0.69

<!-- b000217 | prose | pages [7] -->
2 December

<!-- b000218 | prose | pages [7] -->
19 Apr 2014 16 Apr 2014 2013

<!-- b000219 | prose | pages [7] -->
Based on facts, we set the initial numbers of all kinds of as follows:

<!-- b000220 | prose | pages [7] -->
   S (0) N E I E (0) , 0 0   , (0) I 10 1 R (0)=0 ,

<!-- b000221 | furniture | pages [7] -->


<!-- b000222 | prose | pages [7] -->
Due to the complexity of the system of differential equations, we can’t gain its analytical solution. Therefore, we solve it numerically ode toolbox in MATLAB 2014B for three country (Guinea, Sierra Leone and Liberia) and compare the results with data in the early EBOV transmission period (shown in Fig.2), since EBOV spread in absence of control interventions in that stage.

<!-- b000223 | furniture | pages [7] -->


<!-- b000224 | furniture | pages [8] -->
Team # 35532                                                                          7 / 34

<!-- b000225 | furniture | pages [8] -->


<!-- b000226 | caption | pages [8] -->
Fig.2.1the early EBOV transmission period of Guinea

<!-- b000227 | caption | pages [8] -->
Fig.2.2the early EBOV transmission period of Liberia

<!-- b000228 | caption | pages [8] -->
Fig.2.3the early EBOV transmission period of Sierra Leone

<!-- b000229 | furniture | pages [8] -->


<!-- b000230 | prose | pages [8] -->
Fig 2. Dynamics of 2014 EBOV outbreaks in Guinea, Sierra Leone and Liberia.

<!-- b000231 | prose | pages [8] -->
Outbreak data for Guinea, Sierra Leone and Liberia were based on the cumulative numbers of reported total

<!-- b000232 | prose | pages [8] -->
cases (confirmed, probable and suspected) and deaths from the World Health Organization (WHO) [5].

<!-- b000233 | prose | pages [8] -->
As we can see, The model fits the reported data of cases and deaths in Guinea, Sierra Leone and Liberia well.

<!-- b000234 | heading | pages [8] -->
SEIIR model

<!-- b000235 | furniture | pages [9] -->
Team # 35532                                                                          8 / 34

<!-- b000236 | furniture | pages [9] -->


<!-- b000237 | prose | pages [9] -->
Generally, when the affected people is much enough, it will draw the attention of the government, and the epidemic will be declared as a public health emergency. So does EVBO. According to WHO’s suggestion [6], the first measurement that government should take is isolate the patients, which will impede the spreading of epidemic apparently. The SEIR (susceptible-exposed-infectious-recovered) model fit the early spreading of the disease, but it don’t consider this point. Therefore, there needs to be a improvement for the it. To achieve this goal, we develop a new SEIIR(susceptible-exposed-infectious-quarantined -recovered) model based on the SEIR model, considering the isolated people and without efficient medication. In this model, as transmission of the virus, susceptible individuals S enter the exposed class E

<!-- b000238 | prose | pages [9] -->
I before they become insolated infectious individuals or uncontrolled infectious isolated

<!-- b000239 | prose | pages [9] -->
that either recover and survive R or die D . Fig.3 shows the process. I individuals free

<!-- b000240 | caption | pages [9] -->
Fig.3 the process of the SEIIR model

<!-- b000241 | prose | pages [9] -->
The total population:

<!-- b000242 | prose | pages [9] -->
   N S E I   I R

<!-- b000243 | furniture | pages [9] -->


<!-- b000244 | prose | pages [9] -->
free isolated

<!-- b000245 | prose | pages [9] -->
Considering the assumption 10, formulas (1) changes as follows:

<!-- b000246 | prose | pages [9] -->
dS

<!-- b000247 | prose | pages [9] -->


<!-- b000248 | furniture | pages [9] -->


<!-- b000249 | prose | pages [9] -->
dt

<!-- b000250 | prose | pages [9] -->
Similarly, formula (2) and (3)

<!-- b000251 | prose | pages [9] -->


<!-- b000252 | prose | pages [9] -->
dE

<!-- b000253 | prose | pages [9] -->


<!-- b000254 | furniture | pages [9] -->


<!-- b000255 | prose | pages [9] -->
dt

<!-- b000256 | prose | pages [9] -->
dI

<!-- b000257 | prose | pages [9] -->
free

<!-- b000258 | prose | pages [9] -->
 

<!-- b000259 | furniture | pages [9] -->


<!-- b000260 | prose | pages [9] -->
dt

<!-- b000261 | furniture | pages [9] -->


<!-- b000262 | prose | pages [9] -->


<!-- b000263 | prose | pages [9] -->
SI f r e

<!-- b000264 | prose | pages [9] -->
，

<!-- b000265 | prose | pages [9] -->
N

<!-- b000266 | prose | pages [9] -->
SI f r e e

<!-- b000267 | prose | pages [9] -->
 

<!-- b000268 | prose | pages [9] -->
E

<!-- b000269 | prose | pages [9] -->
，

<!-- b000270 | prose | pages [9] -->
N

<!-- b000271 | prose | pages [9] -->
  E E I , (7). free

<!-- b000272 | prose | pages [9] -->
And the numbers of isolated patients’ changing rate is:

<!-- b000273 | prose | pages [9] -->
dI   

<!-- b000274 | prose | pages [9] -->
isolated (1

<!-- b000275 | prose | pages [9] -->
dt   

<!-- b000276 | prose | pages [9] -->
)

<!-- b000277 | prose | pages [9] -->
E I , (8) isolated

<!-- b000278 | prose | pages [9] -->
The coefficient  in Formula (7) and (8) represents the ratio of new non-isolated infective

<!-- b000279 | prose | pages [9] -->
patients in new infective patients, since not all of patients are willing to be isolated out of different reason. The value of  mainly depends on the development level of medical system.

<!-- b000280 | prose | pages [9] -->
Suppose that:

<!-- b000281 | furniture | pages [10] -->
Team # 35532                                                                          9 / 34

<!-- b000282 | furniture | pages [10] -->


<!-- b000283 | prose | pages [10] -->
  (1   ) ) ;

<!-- b000284 | prose | pages [10] -->
If all the patients in isolation can be cured, all the infective patients will be willing to be

<!-- b000285 | prose | pages [10] -->
 0 isolated, and ;

<!-- b000286 | prose | pages [10] -->
The lower the mortality of isolated patients is, the smaller the value of  is.

<!-- b000287 | prose | pages [10] -->
According to it, we can describe the relationship between  and

<!-- b000288 | prose | pages [10] -->
 

<!-- b000289 | prose | pages [10] -->
2f with a function:

<!-- b000290 | prose | pages [10] -->
 2f e e

<!-- b000291 | furniture | pages [10] -->


<!-- b000292 | prose | pages [10] -->
2f . 1f is much lower that of non-isolated patient Obviously, the mortality of isolated patients

<!-- b000293 | prose | pages [10] -->
So, the recovered people can be divided into two parts according to being isolated or not. Thus, the changing rate of recovery case and death case with time can be represented as follows respectively:

<!-- b000294 | prose | pages [10] -->
dR    (1 f ) I

<!-- b000295 | furniture | pages [10] -->


<!-- b000296 | prose | pages [10] -->
1 dt

<!-- b000297 | prose | pages [10] -->
dD   f I 1 free dt

<!-- b000298 | prose | pages [10] -->
   E (0) E 0 For the initial value, (0) S 0 , 0

<!-- b000299 | prose | pages [10] -->
Simulation Result:

<!-- b000300 | prose | pages [10] -->
   (1 f ) I

<!-- b000301 | furniture | pages [10] -->


<!-- b000302 | prose | pages [10] -->
free free 2 isolated

<!-- b000303 | prose | pages [10] -->
  f I

<!-- b000304 | furniture | pages [10] -->


<!-- b000305 | prose | pages [10] -->
2 isolated

<!-- b000306 | prose | pages [10] -->
   I (0) 0 R (0) 0 I (0) 0 , ,

<!-- b000307 | furniture | pages [10] -->


<!-- b000308 | prose | pages [10] -->
,

<!-- b000309 | furniture | pages [10] -->


<!-- b000310 | prose | pages [10] -->
isolated free

<!-- b000311 | prose | pages [10] -->
f  0.8 According to the report of WHO, the fatality rate of Ebola range from 0.6 to 0.8. Let

<!-- b000312 | prose | pages [10] -->
f  0.6 and while other coefficient unchanged. 2

<!-- b000313 | prose | pages [10] -->
1

<!-- b000314 | prose | pages [10] -->
Due to the naturally spreading stage before isolation measures being taken, we set the initial value with the data in the 100th day as follows:

<!-- b000315 | prose | pages [10] -->
S  E   12219576 2209 I 822 , , , 0 0 0, free D  R   971 2912 I I 822 , ,

<!-- b000316 | furniture | pages [10] -->


<!-- b000317 | prose | pages [10] -->
0 0 0, quarantined

<!-- b000318 | prose | pages [10] -->
In the same manner, we get a numerical solution by using the ode toolbox in Matlab201.The results shows in Fig.4.

<!-- b000319 | furniture | pages [10] -->


<!-- b000320 | furniture | pages [11] -->
Team # 35532                                                                          10 / 34

<!-- b000321 | furniture | pages [11] -->


<!-- b000322 | furniture | pages [11] -->


<!-- b000323 | furniture | pages [11] -->


<!-- b000324 | caption | pages [11] -->
Fig.4 the result of SEIIR model

<!-- b000325 | prose | pages [11] -->
The SEIIR model indeed shows the blockage of isolation to the Ebola’s spreading.

<!-- b000326 | heading | pages [11] -->
SEIIR model with effective medication

<!-- b000327 | prose | pages [11] -->
Now since the World Medical Association has developed a new medication which could stop Ebola and cures patients whose disease is not advanced. Outside of isolation , we can eradicate Ebola with the mediation, which has more effect on Ebola’s spreading. Base on this former work, we improve our model once again and get the SEIIR model with effective medication. The model can be described by a system of differential equations as follows

<!-- b000328 | prose | pages [11] -->
dS

<!-- b000329 | prose | pages [11] -->


<!-- b000330 | prose | pages [11] -->
dt

<!-- b000331 | prose | pages [11] -->


<!-- b000332 | prose | pages [11] -->
dE

<!-- b000333 | prose | pages [11] -->


<!-- b000334 | furniture | pages [11] -->


<!-- b000335 | prose | pages [11] -->
dt

<!-- b000336 | prose | pages [11] -->
dI

<!-- b000337 | prose | pages [11] -->
free

<!-- b000338 | prose | pages [11] -->


<!-- b000339 | prose | pages [11] -->
SI free

<!-- b000340 | prose | pages [11] -->
,

<!-- b000341 | prose | pages [11] -->
N

<!-- b000342 | prose | pages [11] -->
SI f r e e

<!-- b000343 | prose | pages [11] -->
 

<!-- b000344 | prose | pages [11] -->
E

<!-- b000345 | prose | pages [11] -->
,

<!-- b000346 | prose | pages [11] -->
N

<!-- b000347 | prose | pages [11] -->
 

<!-- b000348 | furniture | pages [11] -->


<!-- b000349 | prose | pages [11] -->
dt

<!-- b000350 | prose | pages [11] -->
dI    

<!-- b000351 | prose | pages [11] -->
isolated (1

<!-- b000352 | prose | pages [11] -->
dt

<!-- b000353 | prose | pages [11] -->
dR     (1 f ) I 1 free dt

<!-- b000354 | prose | pages [11] -->
dD    f I 1 free dt

<!-- b000355 | prose | pages [11] -->
   E (0) E 0 I S (0) 0 , , 0 isolated

<!-- b000356 | prose | pages [11] -->
  E I , free

<!-- b000357 | prose | pages [11] -->
  

<!-- b000358 | prose | pages [11] -->
) )

<!-- b000359 | prose | pages [11] -->
E E I M t

<!-- b000360 | prose | pages [11] -->
( )

<!-- b000361 | prose | pages [11] -->
, isolated

<!-- b000362 | prose | pages [11] -->
   (1 (1 f ) I M t ( ) , 2 isolated

<!-- b000363 | prose | pages [11] -->
  f f I M t ( ) , 2 2 isolated

<!-- b000364 | prose | pages [11] -->
   (0) 0 R (0) 0 I (0) 0 , ,

<!-- b000365 | furniture | pages [11] -->


<!-- b000366 | prose | pages [11] -->
free

<!-- b000367 | prose | pages [11] -->
M t is the number of people who can receive the medication in a unit of time.

<!-- b000368 | prose | pages [11] -->
( ) Where

<!-- b000369 | prose | pages [11] -->
I According assumption 12, the M(t) have no effect on the changing rate of . And other free

<!-- b000370 | prose | pages [11] -->
parameters and coefficients’ definition are the same as before.

<!-- b000371 | prose | pages [11] -->
M t increase, more and more patients will be being isolated, in other word, ( ) In addition, as

<!-- b000372 | furniture | pages [12] -->
Team # 35532                                                                          11 / 34

<!-- b000373 | furniture | pages [12] -->


<!-- b000374 | prose | pages [12] -->
 becomes smaller. The results shows in Fig.5.

<!-- b000375 | furniture | pages [12] -->


<!-- b000376 | furniture | pages [12] -->


<!-- b000377 | caption | pages [12] -->
Fig.5 the result of SEIIR model with effective medication

<!-- b000378 | prose | pages [12] -->
The SEIIR model with effective medication indeed shows the blockage of isolation to the Ebola’s spreading.

<!-- b000379 | heading | pages [12] -->
Model II

<!-- b000380 | prose | pages [12] -->
Since the new medication still cannot be manufactured on a large scale, which indicates a shortage of the drug, a feasible delivery system is necessary based on epidemic situation of countries and districts.

<!-- b000381 | prose | pages [12] -->
The setting of the delivery system can be divided into two main parts:  the medical center number and location decision  and the medication allocation for every affected countries and districts.

<!-- b000382 | prose | pages [12] -->
Number and location decision

<!-- b000383 | heading | pages [12] -->
Assumption:

<!-- b000384 | prose | pages [12] -->
Affected people must get to a medical center within a specified time because the new medication can only cure patients whose disease is not advanced. According to Wikipedia, we assume that if a patient in whom symptoms of Ebola has appeared don’t get a medical central (usually the nearest medical center) in 24 hours, the new medication won’t affect his disease. Accounting for the poor transport facilities in West Africa and convenience of drug managing, we set all the medical centers at the capitals of first-level administrative divisions.

<!-- b000385 | prose | pages [12] -->
We simplify the distance from everywhere in an administrative division to a medical center as the distance from the capital of the administrative division to the medical center. In other words, we use the capital of an administrative division as a representation of the administrative. It’s feasible because most of people in the West Africa tend to gather in several big cities.

<!-- b000386 | heading | pages [12] -->
Model:

<!-- b000387 | prose | pages [12] -->
Generally, the aid work in the charged of some international organizations, like WHO, They, rather than every country separately, assign the medical workers and allocate the medication and other medical source.

<!-- b000388 | prose | pages [12] -->
Therefore, the new medication is delivered to countries in need separately by air, then to medical centers by highway and be used for therapy of patients there.

<!-- b000389 | furniture | pages [13] -->
Team # 35532                                                                          12 / 34

<!-- b000390 | furniture | pages [13] -->


<!-- b000391 | prose | pages [13] -->
Our first goal is decide the number and locations of medical centers. Due to the assumption, there must be at least one medical center within a specified distance from every administrative division to ensure patients can get to a medical center. This suggests the number and location decision is a set covering problem. In set covering problems, the objective is to minimize the number or cost of facility location such that a specified level of coverage is obtained.

<!-- b000392 | prose | pages [13] -->
To describe the issue more clearly, we define some parameters as follows: p , the number of capitals of first-level administrative divisions in a country; q , the number of medical centers for EVD set in a country;

<!-- b000393 | prose | pages [13] -->
   V v v , , , v , , v , the set of capitals; 1 2 i p

<!-- b000394 | prose | pages [13] -->
   X x x , , x , x , the set of medical centers; 1 2 j q

<!-- b000395 | prose | pages [13] -->
d x y , the shortest distance from x to y ; ( , )

<!-- b000396 | prose | pages [13] -->
Due to the assumption,

<!-- b000397 | prose | pages [13] -->
X Therefore,

<!-- b000398 | prose | pages [13] -->
 jx V j ,

<!-- b000399 | prose | pages [13] -->
  V .

<!-- b000400 | prose | pages [13] -->
  1,2, , q .

<!-- b000401 | prose | pages [13] -->
be the distance from the i th administrative division to the nearest d v X ( , ) Then we let i q

<!-- b000402 | prose | pages [13] -->
medical central:

<!-- b000403 | prose | pages [13] -->
   min d v X ( , ) i q 1

<!-- b000404 | prose | pages [13] -->
If there is a medical central in it,

<!-- b000405 | prose | pages [13] -->
d v X ( , i

<!-- b000406 | prose | pages [13] -->
d v x ( , ) . i j   j q

<!-- b000407 | prose | pages [13] -->
)=0

<!-- b000408 | furniture | pages [13] -->


<!-- b000409 | prose | pages [13] -->
q

<!-- b000410 | prose | pages [13] -->
Suppose that the distance patients can moved within 24h is, because the assumption,

<!-- b000411 | prose | pages [13] -->
      i p d v X 1max

<!-- b000412 | furniture | pages [13] -->


<!-- b000413 | prose | pages [13] -->
 , , . i i q

<!-- b000414 | prose | pages [13] -->
Considering that healthcare works, financial resources and devices are limited, we should minimize the number of medical centers for EVD, q ,on the premise of meeting the coverage

<!-- b000415 | prose | pages [13] -->
requirement.

<!-- b000416 | prose | pages [13] -->
In addition, administrative division’s need in medication vary from each other. Obviously, the larger an administrative division’s quantity of the medicine needed, the closer the nearest medical center should be. So, we also should

<!-- b000417 | prose | pages [13] -->
p

<!-- b000418 | prose | pages [13] -->


<!-- b000419 | prose | pages [13] -->
Min 1

<!-- b000420 | prose | pages [13] -->
h d v X

<!-- b000421 | prose | pages [13] -->
( , )

<!-- b000422 | prose | pages [13] -->
, i i i q

<!-- b000423 | prose | pages [13] -->
ih is the metric of quantity of drug needed of the i th administrative in the coming Where

<!-- b000424 | prose | pages [13] -->
period.

<!-- b000425 | prose | pages [13] -->
In next part, we will clarify how to calculate ih .

<!-- b000426 | furniture | pages [14] -->
Team # 35532                                                                          13 / 34

<!-- b000427 | furniture | pages [14] -->


<!-- b000428 | prose | pages [14] -->
To sum up, We model the problem about medical centers number and location decision with multi-objective optimization. The formulas of this model is

<!-- b000429 | prose | pages [14] -->
p

<!-- b000430 | prose | pages [14] -->


<!-- b000431 | prose | pages [14] -->
h d v X

<!-- b000432 | prose | pages [14] -->
Min

<!-- b000433 | prose | pages [14] -->


<!-- b000434 | prose | pages [14] -->
i

<!-- b000435 | prose | pages [14] -->
1

<!-- b000436 | prose | pages [14] -->
Min

<!-- b000437 | prose | pages [14] -->
q

<!-- b000438 | prose | pages [14] -->
 

<!-- b000439 | prose | pages [14] -->
( , )

<!-- b000440 | prose | pages [14] -->
i i i q

<!-- b000441 | prose | pages [14] -->
 

<!-- b000442 | prose | pages [14] -->


<!-- b000443 | prose | pages [14] -->


<!-- b000444 | prose | pages [14] -->
d v X s t

<!-- b000445 | prose | pages [14] -->
. . max

<!-- b000446 | prose | pages [14] -->


<!-- b000447 | prose | pages [14] -->
1

<!-- b000448 | prose | pages [14] -->
i p

<!-- b000449 | prose | pages [14] -->


<!-- b000450 | prose | pages [14] -->


<!-- b000451 | prose | pages [14] -->
X x x

<!-- b000452 | prose | pages [14] -->
,

<!-- b000453 | prose | pages [14] -->
q

<!-- b000454 | prose | pages [14] -->
1

<!-- b000455 | prose | pages [14] -->


<!-- b000456 | prose | pages [14] -->
, ,

<!-- b000457 | furniture | pages [14] -->


<!-- b000458 | prose | pages [14] -->
i i q

<!-- b000459 | prose | pages [14] -->


<!-- b000460 | prose | pages [14] -->
, ,

<!-- b000461 | prose | pages [14] -->
x

<!-- b000462 | prose | pages [14] -->
2 2

<!-- b000463 | prose | pages [14] -->
q

<!-- b000464 | prose | pages [14] -->


<!-- b000465 | prose | pages [14] -->
for i x V

<!-- b000466 | prose | pages [14] -->
,

<!-- b000467 | prose | pages [14] -->
j

<!-- b000468 | heading | pages [14] -->
Solution:

<!-- b000469 | prose | pages [14] -->
1,2, ,

<!-- b000470 | prose | pages [14] -->
q

<!-- b000471 | prose | pages [14] -->
Without loss of generality, we take the most seriously effected Sierra Leone for example and locate medical centers for it.

<!-- b000472 | prose | pages [14] -->
The Republic of Sierra Leone is composed of four regions: the Northern Province, Southern Province, the Eastern Province, and the Western Area. The first three provinces are further divided into 12 districts. Fig.6 shows it.

<!-- b000473 | caption | pages [14] -->
Fig.6 The 12 districts and 2 areas of Sierra

<!-- b000474 | prose | pages [14] -->
Leone. S

<!-- b000475 | furniture | pages [14] -->


<!-- b000476 | furniture | pages [14] -->


<!-- b000477 | furniture | pages [14] -->


<!-- b000478 | prose | pages [14] -->
According to our model, we replace every district with its capital (the western area be seen as a district and Freetown is its capital). So , the value of p equals 13.

<!-- b000479 | prose | pages [14] -->
We search and calculate the shortest path and distance between any two capitals via google map, and the results be shown in Table 2.

<!-- b000480 | caption | pages [14] -->
Table 2 :the shortest path and distance between any two capitals

<!-- b000481 | furniture | pages [14] -->


<!-- b000482 | prose | pages [14] -->
Kail

<!-- b000483 | prose | pages [14] -->
Ken

<!-- b000484 | prose | pages [14] -->
Koi

<!-- b000485 | prose | pages [14] -->
Ma

<!-- b000486 | prose | pages [14] -->
Ka

<!-- b000487 | prose | pages [14] -->
Po

<!-- b000488 | prose | pages [14] -->
ahu

<!-- b000489 | prose | pages [14] -->
ema

<!-- b000490 | prose | pages [14] -->
du

<!-- b000491 | prose | pages [14] -->
ken

<!-- b000492 | prose | pages [14] -->
mbi

<!-- b000493 | prose | pages [14] -->
rt

<!-- b000494 | prose | pages [14] -->
n

<!-- b000495 | prose | pages [14] -->
i

<!-- b000496 | prose | pages [14] -->
a

<!-- b000497 | prose | pages [14] -->
Lo ko

<!-- b000498 | prose | pages [14] -->
Kailah 0 112 46 204 353 30

<!-- b000499 | furniture | pages [14] -->


<!-- b000500 | prose | pages [14] -->
Ka

<!-- b000501 | prose | pages [14] -->
Magb

<!-- b000502 | prose | pages [14] -->
Bo Bon

<!-- b000503 | prose | pages [14] -->
Moy

<!-- b000504 | prose | pages [14] -->
Puje

<!-- b000505 | prose | pages [14] -->
Free

<!-- b000506 | prose | pages [14] -->
bal

<!-- b000507 | prose | pages [14] -->
uraka

<!-- b000508 | prose | pages [14] -->
the

<!-- b000509 | prose | pages [14] -->
amb

<!-- b000510 | prose | pages [14] -->
hun

<!-- b000511 | prose | pages [14] -->
town

<!-- b000512 | prose | pages [14] -->
a a

<!-- b000513 | prose | pages [14] -->
a

<!-- b000514 | prose | pages [14] -->
32 179 169 261 284 222 417

<!-- b000515 | furniture | pages [15] -->
Team # 35532                                                                          14 / 34

<!-- b000516 | furniture | pages [15] -->


<!-- b000517 | prose | pages [15] -->
un .4 0

<!-- b000518 | prose | pages [15] -->
Kene

<!-- b000519 | prose | pages [15] -->
112 0 11 192 330 22

<!-- b000520 | prose | pages [15] -->
ma

<!-- b000521 | prose | pages [15] -->
3 7

<!-- b000522 | prose | pages [15] -->
Koidu 46.4 113 0 159 308 25 3

<!-- b000523 | prose | pages [15] -->
Make

<!-- b000524 | prose | pages [15] -->
204 192 15 0 152 97

<!-- b000525 | prose | pages [15] -->
ni

<!-- b000526 | prose | pages [15] -->
9 .7

<!-- b000527 | prose | pages [15] -->
Kamb

<!-- b000528 | prose | pages [15] -->
353 330 30 152 0 51

<!-- b000529 | prose | pages [15] -->
ia

<!-- b000530 | prose | pages [15] -->
8 .1

<!-- b000531 | prose | pages [15] -->
Port

<!-- b000532 | prose | pages [15] -->
300 227 25 97.

<!-- b000533 | prose | pages [15] -->
51.

<!-- b000534 | prose | pages [15] -->
0

<!-- b000535 | prose | pages [15] -->
Loko

<!-- b000536 | prose | pages [15] -->
3 7 1

<!-- b000537 | prose | pages [15] -->
Kabal

<!-- b000538 | prose | pages [15] -->
321 309 27 118 269 21

<!-- b000539 | prose | pages [15] -->
a

<!-- b000540 | prose | pages [15] -->
6 6

<!-- b000541 | prose | pages [15] -->
Magb

<!-- b000542 | prose | pages [15] -->
179 167 13 26.

<!-- b000543 | prose | pages [15] -->
176 12

<!-- b000544 | prose | pages [15] -->
uraka

<!-- b000545 | prose | pages [15] -->
3 8 2

<!-- b000546 | prose | pages [15] -->
Bo 169 68.5 16 133 263 21 2 0

<!-- b000547 | prose | pages [15] -->
Mattr

<!-- b000548 | prose | pages [15] -->
261 149 25 217 298 24

<!-- b000549 | prose | pages [15] -->
u jong

<!-- b000550 | prose | pages [15] -->
6 4

<!-- b000551 | prose | pages [15] -->
Moya

<!-- b000552 | prose | pages [15] -->
284 173 25 124 181 12

<!-- b000553 | prose | pages [15] -->
mba

<!-- b000554 | prose | pages [15] -->
3 8

<!-- b000555 | prose | pages [15] -->
Pujeh

<!-- b000556 | prose | pages [15] -->
222 110 21 206 337 28

<!-- b000557 | prose | pages [15] -->
un

<!-- b000558 | prose | pages [15] -->
3 4

<!-- b000559 | prose | pages [15] -->
Freet

<!-- b000560 | prose | pages [15] -->
417 305 34 185 126 11

<!-- b000561 | prose | pages [15] -->
own

<!-- b000562 | prose | pages [15] -->
0 9

<!-- b000563 | prose | pages [15] -->
1 1

<!-- b000564 | prose | pages [15] -->
30 167 68.

<!-- b000565 | prose | pages [15] -->
149 173 110 305 9 9 5

<!-- b000566 | prose | pages [15] -->
27 133 162 256 253 213 340 6 6

<!-- b000567 | prose | pages [15] -->
11 26.8 133 217 124 206 185 8 8

<!-- b000568 | prose | pages [15] -->
26 176 263 298 181 337 126 9 9

<!-- b000569 | prose | pages [15] -->
21 122 210 244 128 284 119 6 6

<!-- b000570 | prose | pages [15] -->
0 0 105.9 144 334 242 323 302

<!-- b000571 | prose | pages [15] -->
10 0 108 191 100 216 208 5.9

<!-- b000572 | prose | pages [15] -->
14 108 0 82.

<!-- b000573 | prose | pages [15] -->
106 75.3 174. 4 4 4 66

<!-- b000574 | prose | pages [15] -->
33 191 82.

<!-- b000575 | prose | pages [15] -->
0 130 98.5 237 4 4 4

<!-- b000576 | prose | pages [15] -->
24 100 106 130 0 179 114 2 2

<!-- b000577 | prose | pages [15] -->
32 216 75.

<!-- b000578 | prose | pages [15] -->
98.

<!-- b000579 | prose | pages [15] -->
179 0 312 3 3 3 5

<!-- b000580 | prose | pages [15] -->
30 208 174

<!-- b000581 | prose | pages [15] -->
237 114 312 0

<!-- b000582 | prose | pages [15] -->
2 2 .66

<!-- b000583 | prose | pages [15] -->
(unit: kilometer) (source: google earth) As for the value of, accounting for the time of preliminary judgment and poor transport facilities, a reasonable value is 92.1km.

<!-- b000584 | prose | pages [15] -->
ih Measuring the need of every district

<!-- b000585 | furniture | pages [15] -->


<!-- b000586 | furniture | pages [15] -->


<!-- b000587 | prose | pages [15] -->
Table.3 the revolution of city

<!-- b000588 | furniture | pages [15] -->


<!-- b000589 | prose | pages [15] -->
h

<!-- b000590 | furniture | pages [15] -->


<!-- b000591 | prose | pages [15] -->
Kailahun 0.512665 Koinadugu Kenema 0.553363 Tonkolili Kono 0.22831 Bo Bombali 0.441547 Bonthe Moyamba 0.505654

<!-- b000592 | furniture | pages [15] -->


<!-- b000593 | furniture | pages [15] -->


<!-- b000594 | furniture | pages [15] -->


<!-- b000595 | furniture | pages [15] -->


<!-- b000596 | prose | pages [15] -->
h

<!-- b000597 | furniture | pages [15] -->


<!-- b000598 | prose | pages [15] -->
h 0.379487 Kambia 0.341398 0.294881 Port Loko 0.53602 0.504783 Pujehun 0.334563 0.271492 Western Area 0.436276

<!-- b000599 | furniture | pages [15] -->


<!-- b000600 | furniture | pages [15] -->


<!-- b000601 | furniture | pages [15] -->


<!-- b000602 | furniture | pages [15] -->


<!-- b000603 | furniture | pages [15] -->


<!-- b000604 | furniture | pages [15] -->


<!-- b000605 | furniture | pages [15] -->


<!-- b000606 | prose | pages [15] -->
This optimal problem belongs to the NP-hard problems that can’t be solved in polynomial time. So, we can only get the approximate solution with a heuristic, such as genetic algorithm, simulated annealing and so on. Here, we select the genetic algorithm and write a program with Matlab2014.

<!-- b000607 | furniture | pages [16] -->
Team # 35532                                                                          15 / 34

<!-- b000608 | furniture | pages [16] -->


<!-- b000609 | prose | pages [16] -->
Running the program repeatedly, we obtain a relatively good results and make our plan: There are seven mental centers located in Kailahun, Makeni, Kambia, Kabala, Bo, Moyamba and Freetown respectively. The Fig. 7 shows the scope that every mental center manages.

<!-- b000610 | caption | pages [16] -->
Fig.7 locations of medical centers in Sierra Leone

<!-- b000611 | prose | pages [16] -->
Part III

<!-- b000612 | heading | pages [16] -->
1. Specify evaluation norms

<!-- b000613 | prose | pages [16] -->
As for the evaluation the Susceptible standard for Each region, there are mainly aspects that count: Population density, Temperature, Humidity, the situation of current disease infection, Open or under construction，economy，National Education and age. What follows in the section will hammer at accounting for the eight aspects.  Population density: Population density undoubtedly accounts for key proportion in the demand level of the drug evaluation. Because Ebola is a spirited contagion disease, not only patients but also corpses can be the source of infection. Therefore, if the population density is high, the rate of spread disease will be fast in general situation. However, in some area, the pollution density of the area is low, but almost people live in a central city (in fact, the pollution density of the city is high), we deal with data preprocessing, making the aspect more reasonable evaluation model. The pollution density of the area could be calculated as follows:

<!-- b000614 | furniture | pages [16] -->


<!-- b000615 | prose | pages [16] -->
R 

<!-- b000616 | prose | pages [16] -->
n

<!-- b000617 | prose | pages [16] -->
a

<!-- b000618 | prose | pages [16] -->
1 n

<!-- b000619 | prose | pages [16] -->
M

<!-- b000620 | prose | pages [16] -->
n

<!-- b000621 | prose | pages [16] -->
the pollution of the number n area. R : n

<!-- b000622 | prose | pages [16] -->
the acreage of the number n area. M : n

<!-- b000623 | prose | pages [16] -->
The pollution density of the main city in the area could be calculated as follows:

<!-- b000624 | furniture | pages [17] -->
Team # 35532                                                                          16 / 34

<!-- b000625 | furniture | pages [17] -->


<!-- b000626 | prose | pages [17] -->
a

<!-- b000627 | prose | pages [17] -->
2 n

<!-- b000628 | furniture | pages [17] -->


<!-- b000629 | prose | pages [17] -->
r  

<!-- b000630 | prose | pages [17] -->
n

<!-- b000631 | prose | pages [17] -->
m

<!-- b000632 | prose | pages [17] -->
n

<!-- b000633 | prose | pages [17] -->
the pollution of the main city number n area . nr :

<!-- b000634 | prose | pages [17] -->
the acreage of the main city number n area. m : n

<!-- b000635 | prose | pages [17] -->
We define a new population density which could be calculated as follows:

<!-- b000636 | prose | pages [17] -->
  

<!-- b000637 | prose | pages [17] -->
A a b a

<!-- b000638 | prose | pages [17] -->
n

<!-- b000639 | prose | pages [17] -->
1

<!-- b000640 | prose | pages [17] -->
n

<!-- b000641 | prose | pages [17] -->
1 2

<!-- b000642 | prose | pages [17] -->
n

<!-- b000643 | prose | pages [17] -->
  

<!-- b000644 | prose | pages [17] -->
b b b

<!-- b000645 | prose | pages [17] -->
1

<!-- b000646 | prose | pages [17] -->
1 2 3

<!-- b000647 | furniture | pages [17] -->


<!-- b000648 | prose | pages [17] -->
 The numerical value depend on the ( a a 2 n 1

<!-- b000649 | prose | pages [17] -->


<!-- b000650 | furniture | pages [17] -->


<!-- b000651 | prose | pages [17] -->
(

<!-- b000652 | prose | pages [17] -->
a a

<!-- b000653 | prose | pages [17] -->
)

<!-- b000654 | prose | pages [17] -->
   

<!-- b000655 | prose | pages [17] -->
2

<!-- b000656 | prose | pages [17] -->
n

<!-- b000657 | prose | pages [17] -->
1

<!-- b000658 | prose | pages [17] -->
n

<!-- b000659 | prose | pages [17] -->
b b b

<!-- b000660 | prose | pages [17] -->
2 3

<!-- b000661 | prose | pages [17] -->
a

<!-- b000662 | prose | pages [17] -->
2

<!-- b000663 | prose | pages [17] -->
n

<!-- b000664 | prose | pages [17] -->
. ) ) n n

<!-- b000665 | prose | pages [17] -->
By the above calculation, the population density in the evaluation of the model is more reasonable and accurate.  Temperature

<!-- b000666 | prose | pages [17] -->
Form the past Information and data, the Ebola usually outbreak in the summer ,but in the winter, the entire epidemic have been more effective control, and the status of major outbreaks in Africa is the lower latitudes area, which shows that the temperature is an important aspects in the demand level of the drug evaluation. The temperature of the area is:

<!-- b000667 | prose | pages [17] -->
 Humidity

<!-- b000668 | prose | pages [17] -->
B n

<!-- b000669 | prose | pages [17] -->
Ebola outbreak in the areas which the annual precipitation is high and harmonious, especially in the tropical rain forest areas with high coverage. The World Health Organization's report shows that humid climate is conducive to the spread of the virus, therefore, we choose the humidity as an aspects in the evaluation model.

<!-- b000670 | prose | pages [17] -->
The temperature of the area is

<!-- b000671 | prose | pages [17] -->
 current disease infection

<!-- b000672 | prose | pages [17] -->
C n

<!-- b000673 | prose | pages [17] -->
Current infection situation has a great impact on the future of the epidemic. The country who has large number of infected persons face the challenges in future, and need support from World Health Organization. Every patient will require substantial and large investment Because Ebola is highly infectious diseases. Therefore, we believe that using the number of patients to measure a country's entire national epidemic of severe is reasonable. The Infected people number of the area is

<!-- b000674 | prose | pages [17] -->
 Open or under construction

<!-- b000675 | prose | pages [17] -->
nI

<!-- b000676 | furniture | pages [18] -->
Team # 35532                                                                          17 / 34

<!-- b000677 | furniture | pages [18] -->


<!-- b000678 | prose | pages [18] -->
As we all know, controlling the flow of people is an effective measure to prevent further deterioration of infectious diseases, On the one hand, under construction can control the spread of infection to uninfected areas, on the other hand, it have the ability to reduce the risk of infection of healthy people in infected area.

<!-- b000679 | prose | pages [18] -->
In a country, some cities under opening while some cities under closing (we only consider the large cities of the country).

<!-- b000680 | prose | pages [18] -->
We define Open coefficient which could be calculated as follows:

<!-- b000681 | prose | pages [18] -->
F

<!-- b000682 | prose | pages [18] -->
n

<!-- b000683 | furniture | pages [18] -->


<!-- b000684 | prose | pages [18] -->
c

<!-- b000685 | prose | pages [18] -->
open

<!-- b000686 | prose | pages [18] -->
  c

<!-- b000687 | prose | pages [18] -->
all

<!-- b000688 | prose | pages [18] -->
： the number of open cities in the country c open

<!-- b000689 | prose | pages [18] -->
： the number of all cities in the country. c all

<!-- b000690 | prose | pages [18] -->
 Economy

<!-- b000691 | prose | pages [18] -->
In general situation, the more backward economy countries is the more difficult to control the disease is. Therefore, the economic situation of a country is an important indicator to determine the national level in the medical facilities. The lower the country's GDP means the more difficult to control Ebola infection because of under-developed Medical infrastructure. We use the GDP per capita as the aspects to show the economy of the area.

<!-- b000692 | prose | pages [18] -->
The economy of the area is：

<!-- b000693 | prose | pages [18] -->
National Education [7] 

<!-- b000694 | prose | pages [18] -->
E n

<!-- b000695 | prose | pages [18] -->
Cremation in Africa do not comply with the local traditions, which is an important reason for the large-scale outbreak of Ebola. Ebola can spread through the corpses which lead a large number of people infected at the funeral. According to the survey, the higher the education level is, the greater the proportion of accept cremation. Therefore, we choose each country received higher education as a measure of the proportion of the country's level of education. The national education of the area is：

<!-- b000696 | prose | pages [18] -->
Age[8] 

<!-- b000697 | prose | pages [18] -->
J n n

<!-- b000698 | prose | pages [18] -->
According to the report of the World Health Organization, the probability of illness in young adults over the age of 14 is three times the age of 14, the probability of illness aged 65 or older is four times the age of 14. Thus, we can see that the higher proportion of the population over the age of 14 is, the greater the overall probability of illness is. We define age coefficient which could be calculated as follows:

<!-- b000699 | furniture | pages [18] -->


<!-- b000700 | prose | pages [18] -->
K

<!-- b000701 | prose | pages [18] -->


<!-- b000702 | furniture | pages [18] -->


<!-- b000703 | prose | pages [18] -->


<!-- b000704 | prose | pages [18] -->
K

<!-- b000705 | prose | pages [18] -->
14~65

<!-- b000706 | prose | pages [18] -->
K

<!-- b000707 | furniture | pages [18] -->


<!-- b000708 | heading | pages [18] -->
Model

<!-- b000709 | prose | pages [18] -->
65

<!-- b000710 | prose | pages [18] -->
K

<!-- b000711 | prose | pages [18] -->
all

<!-- b000712 | furniture | pages [19] -->
Team # 35532                                                                          18 / 34

<!-- b000713 | furniture | pages [19] -->


<!-- b000714 | heading | pages [19] -->
Introduction:

<!-- b000715 | prose | pages [19] -->
TOPSIS (technique for order performance by similarity to ideal solution) is a useful technique in dealing with multiattribute or multi-criteria decision making (MADM/MCDM) problems in the real world[9]. It helps decision maker organize the problems to be solved, and carry out analysis, comparisons and rankings of the alternatives. Accordingly, the selection of a suitable alternative(s) will be made. However, many decision making problems within organizations will be a collaborative effort. Hence, this model will extend TOPSIS to evaluate the demand of the drug. A complete and efficient procedure for decision making will then be provided.  Step one Since the different factors have greatly different in magnitude, we should normalized the

<!-- b000716 | prose | pages [19] -->
X of the decision matrix X can be any linear- value of this factors. the normalized value

<!-- b000717 | prose | pages [19] -->
scale transformation to keep0   k . X 1 ij

<!-- b000718 | prose | pages [19] -->
k k ij ij

<!-- b000719 | prose | pages [19] -->
X is the value of the corresponding element We consider that the normalized value of k ij X k ij

<!-- b000720 | prose | pages [19] -->
divided by the operation of its column elements, i.e., vector normalization, then (take the factor as example).

<!-- b000721 | prose | pages [19] -->


<!-- b000722 | prose | pages [19] -->
k

<!-- b000723 | prose | pages [19] -->
X

<!-- b000724 | prose | pages [19] -->
m

<!-- b000725 | prose | pages [19] -->
1 2

<!-- b000726 | prose | pages [19] -->
A

<!-- b000727 | prose | pages [19] -->
1

<!-- b000728 | prose | pages [19] -->
 Step two: Construct decision matrix X

<!-- b000729 | furniture | pages [19] -->


<!-- b000730 | prose | pages [19] -->
A

<!-- b000731 | prose | pages [19] -->
n

<!-- b000732 | prose | pages [19] -->
   

<!-- b000733 | prose | pages [19] -->
2 2

<!-- b000734 | prose | pages [19] -->
A A

<!-- b000735 | prose | pages [19] -->
2

<!-- b000736 | prose | pages [19] -->
n

<!-- b000737 | prose | pages [19] -->
The structure of the matrix can be expressed as follows:

<!-- b000738 | furniture | pages [19] -->


<!-- b000739 | prose | pages [19] -->
X X

<!-- b000740 | prose | pages [19] -->
1

<!-- b000741 | prose | pages [19] -->


<!-- b000742 | prose | pages [19] -->
k k

<!-- b000743 | prose | pages [19] -->
x X X

<!-- b000744 | prose | pages [19] -->
1 11 12

<!-- b000745 | prose | pages [19] -->


<!-- b000746 | prose | pages [19] -->
k k

<!-- b000747 | prose | pages [19] -->
x X X

<!-- b000748 | prose | pages [19] -->


<!-- b000749 | prose | pages [19] -->
2 21 22

<!-- b000750 | prose | pages [19] -->
 

<!-- b000751 | prose | pages [19] -->
X

<!-- b000752 | prose | pages [19] -->


<!-- b000753 | prose | pages [19] -->
k k

<!-- b000754 | prose | pages [19] -->
X X x

<!-- b000755 | prose | pages [19] -->


<!-- b000756 | prose | pages [19] -->
i

<!-- b000757 | prose | pages [19] -->
1

<!-- b000758 | prose | pages [19] -->
i i

<!-- b000759 | prose | pages [19] -->
 

<!-- b000760 | prose | pages [19] -->
k k

<!-- b000761 | prose | pages [19] -->
X X

<!-- b000762 | prose | pages [19] -->


<!-- b000763 | prose | pages [19] -->
x

<!-- b000764 | prose | pages [19] -->


<!-- b000765 | prose | pages [19] -->
m

<!-- b000766 | prose | pages [19] -->
1

<!-- b000767 | prose | pages [19] -->
m m

<!-- b000768 | prose | pages [19] -->
ix denotes the alternativei , =1,2 Where i ，

<!-- b000769 | prose | pages [19] -->
; j =1,2 , n ，

<!-- b000770 | prose | pages [19] -->
In the model, ix means different country, and

<!-- b000771 | furniture | pages [19] -->


<!-- b000772 | prose | pages [19] -->
X X

<!-- b000773 | prose | pages [19] -->
2 2

<!-- b000774 | prose | pages [19] -->
n

<!-- b000775 | prose | pages [19] -->


<!-- b000776 | prose | pages [19] -->
k k

<!-- b000777 | prose | pages [19] -->
X X

<!-- b000778 | prose | pages [19] -->
1

<!-- b000779 | prose | pages [19] -->
j

<!-- b000780 | prose | pages [19] -->
1

<!-- b000781 | prose | pages [19] -->
n

<!-- b000782 | prose | pages [19] -->


<!-- b000783 | prose | pages [19] -->
k k

<!-- b000784 | prose | pages [19] -->
X X

<!-- b000785 | prose | pages [19] -->


<!-- b000786 | prose | pages [19] -->
2

<!-- b000787 | prose | pages [19] -->
j

<!-- b000788 | prose | pages [19] -->
2

<!-- b000789 | prose | pages [19] -->
n

<!-- b000790 | prose | pages [19] -->
 

<!-- b000791 | prose | pages [19] -->
k k

<!-- b000792 | prose | pages [19] -->
X X

<!-- b000793 | prose | pages [19] -->


<!-- b000794 | prose | pages [19] -->
2 2

<!-- b000795 | prose | pages [19] -->
ij in

<!-- b000796 | prose | pages [19] -->
 

<!-- b000797 | prose | pages [19] -->
k k

<!-- b000798 | prose | pages [19] -->
X X

<!-- b000799 | prose | pages [19] -->
 

<!-- b000800 | prose | pages [19] -->
2 2

<!-- b000801 | prose | pages [19] -->
mj mn

<!-- b000802 | prose | pages [19] -->
X represents the attribute or criterion j , ; , , m m i

<!-- b000803 | prose | pages [19] -->
X means different factors in the evaluation. i

<!-- b000804 | prose | pages [19] -->
Observe that we can also set the outcomes of qualitative attributes from each alternative as discrete values, e.g., 1 to 10 or linguistics values, so that the quantitative values will be placed in the above decision matrix. For example, current disease infection is a factor which we can’t evaluate it directly, we can use some Index to show it[10].  Step three

<!-- b000805 | prose | pages [19] -->
Determine the ideal and negative ideal solutions

<!-- b000806 | prose | pages [19] -->
V and V . - k k

<!-- b000807 | furniture | pages [20] -->
Team # 35532                                                                          19 / 34

<!-- b000808 | furniture | pages [20] -->


<!-- b000809 | prose | pages [20] -->
      k k V = X , , X k 1 n

<!-- b000810 | prose | pages [20] -->
    - k - k - V = X , , X k 1 n

<!-- b000811 | prose | pages [20] -->
 Step four

<!-- b000812 | prose | pages [20] -->
     k max X | j 1,2, , m ij i

<!-- b000813 | prose | pages [20] -->
   

<!-- b000814 | furniture | pages [20] -->


<!-- b000815 | prose | pages [20] -->
 k min X | j 1,2, , m ij i i

<!-- b000816 | prose | pages [20] -->
Calculate the separation measure from the ideal and the negative ideal solutions,

<!-- b000817 | prose | pages [20] -->
respectively, for the group.

<!-- b000818 | prose | pages [20] -->
n

<!-- b000819 | prose | pages [20] -->


<!-- b000820 | prose | pages [20] -->
v 

<!-- b000821 | prose | pages [20] -->


<!-- b000822 | prose | pages [20] -->
+

<!-- b000823 | prose | pages [20] -->
k k

<!-- b000824 | prose | pages [20] -->
2

<!-- b000825 | prose | pages [20] -->
S

<!-- b000826 | prose | pages [20] -->
= (

<!-- b000827 | prose | pages [20] -->
v

<!-- b000828 | prose | pages [20] -->
)

<!-- b000829 | prose | pages [20] -->
iS  and iS , -

<!-- b000830 | furniture | pages [20] -->


<!-- b000831 | prose | pages [20] -->


<!-- b000832 | prose | pages [20] -->
for alternati

<!-- b000833 | prose | pages [20] -->
，

<!-- b000834 | prose | pages [20] -->
i ij j

<!-- b000835 | prose | pages [20] -->


<!-- b000836 | prose | pages [20] -->
j

<!-- b000837 | prose | pages [20] -->
1

<!-- b000838 | prose | pages [20] -->
n

<!-- b000839 | prose | pages [20] -->


<!-- b000840 | prose | pages [20] -->
v 

<!-- b000841 | prose | pages [20] -->


<!-- b000842 | prose | pages [20] -->
-

<!-- b000843 | prose | pages [20] -->
k k

<!-- b000844 | prose | pages [20] -->
2

<!-- b000845 | prose | pages [20] -->
S

<!-- b000846 | prose | pages [20] -->
= (

<!-- b000847 | prose | pages [20] -->
v

<!-- b000848 | furniture | pages [20] -->


<!-- b000849 | furniture | pages [20] -->


<!-- b000850 | prose | pages [20] -->
vei i

<!-- b000851 | prose | pages [20] -->
, 1, ,

<!-- b000852 | prose | pages [20] -->
m

<!-- b000853 | furniture | pages [20] -->


<!-- b000854 | prose | pages [20] -->


<!-- b000855 | prose | pages [20] -->
for alternati

<!-- b000856 | prose | pages [20] -->
)

<!-- b000857 | prose | pages [20] -->
，

<!-- b000858 | prose | pages [20] -->
i ij j

<!-- b000859 | prose | pages [20] -->


<!-- b000860 | prose | pages [20] -->
j

<!-- b000861 | prose | pages [20] -->
1

<!-- b000862 | prose | pages [20] -->
 Step five

<!-- b000863 | furniture | pages [20] -->


<!-- b000864 | furniture | pages [20] -->


<!-- b000865 | prose | pages [20] -->
vei i

<!-- b000866 | prose | pages [20] -->
, 1, ,

<!-- b000867 | prose | pages [20] -->
m

<!-- b000868 | prose | pages [20] -->
Calculate the relative closeness C to the ideal solution for the group. Calculate the relative closeness to the ideal solution and rank the alternatives in descending

<!-- b000869 | prose | pages [20] -->
order. The relative closeness of the i th alternative

<!-- b000870 | prose | pages [20] -->
can be expressed as

<!-- b000871 | prose | pages [20] -->


<!-- b000872 | prose | pages [20] -->
S

<!-- b000873 | prose | pages [20] -->


<!-- b000874 | prose | pages [20] -->
i

<!-- b000875 | prose | pages [20] -->
C

<!-- b000876 | prose | pages [20] -->
 

<!-- b000877 | prose | pages [20] -->
S S

<!-- b000878 | prose | pages [20] -->
i

<!-- b000879 | prose | pages [20] -->


<!-- b000880 | heading | pages [20] -->
iA with respect to positive idea solution

<!-- b000881 | furniture | pages [20] -->


<!-- b000882 | prose | pages [20] -->


<!-- b000883 | prose | pages [20] -->
, ,

<!-- b000884 | prose | pages [20] -->
i

<!-- b000885 | prose | pages [20] -->
1, ,

<!-- b000886 | prose | pages [20] -->
m

<!-- b000887 | prose | pages [20] -->
 

<!-- b000888 | prose | pages [20] -->
i i

<!-- b000889 | prose | pages [20] -->
  The larger the index value, the better the performance of the alternative. Where 0 C 1

<!-- b000890 | heading | pages [20] -->
2. Collect data

<!-- b000891 | prose | pages [20] -->
To evaluate h of every districts, Many data is needed, we can find every district’s data

<!-- b000892 | prose | pages [20] -->
needed for our specific evaluation norms by searching from the website，like Wikipedia and WHO. We finally conclude the relative statistics of those areas and list them in a form.

<!-- b000893 | caption | pages [20] -->
Table4:the data of the different district

<!-- b000894 | furniture | pages [20] -->


<!-- b000895 | prose | pages [20] -->
Population

<!-- b000896 | prose | pages [20] -->
Open

<!-- b000897 | prose | pages [20] -->
density

<!-- b000898 | prose | pages [20] -->
coefficient

<!-- b000899 | prose | pages [20] -->
458.1595 100 Kailahun

<!-- b000900 | prose | pages [20] -->
4697.336 100 Kenema

<!-- b000901 | prose | pages [20] -->
2618.687 0 Kono

<!-- b000902 | prose | pages [20] -->
267.3536 100 Bombali

<!-- b000903 | prose | pages [20] -->
281.6377 50 Kambia

<!-- b000904 | prose | pages [20] -->
860.1828 100 Port Loko

<!-- b000905 | prose | pages [20] -->
299.7132 50 Koinadugu

<!-- b000906 | prose | pages [20] -->
1740.713 0 Tonkolili

<!-- b000907 | prose | pages [20] -->
266.1477 100 Bo

<!-- b000908 | prose | pages [20] -->
1248.725 50 Bonthe

<!-- b000909 | prose | pages [20] -->
392.2557 100 Moyamba

<!-- b000910 | prose | pages [20] -->
1176.208 50 Pujehun

<!-- b000911 | prose | pages [20] -->
Temperature

<!-- b000912 | prose | pages [20] -->
Humidity

<!-- b000913 | prose | pages [20] -->
Current

<!-- b000914 | prose | pages [20] -->
(ºC)

<!-- b000915 | prose | pages [20] -->
(%)

<!-- b000916 | prose | pages [20] -->
disease situation

<!-- b000917 | prose | pages [20] -->
24 94 4

<!-- b000918 | prose | pages [20] -->
23 94 4

<!-- b000919 | prose | pages [20] -->
21 87 3

<!-- b000920 | prose | pages [20] -->
26 81 2

<!-- b000921 | prose | pages [20] -->
24 94 3

<!-- b000922 | prose | pages [20] -->
22 89 5

<!-- b000923 | prose | pages [20] -->
22 69 4

<!-- b000924 | prose | pages [20] -->
23 83 4

<!-- b000925 | prose | pages [20] -->
23 94 4

<!-- b000926 | prose | pages [20] -->
24 91 1

<!-- b000927 | prose | pages [20] -->
23 93 4

<!-- b000928 | prose | pages [20] -->
25 89 3

<!-- b000929 | furniture | pages [21] -->
Team # 35532                                                                          20 / 34

<!-- b000930 | furniture | pages [21] -->


<!-- b000931 | prose | pages [21] -->
25996.65 50 Western Area

<!-- b000932 | prose | pages [21] -->
Note :1.the unit of the population denisty is People /per km

<!-- b000933 | prose | pages [21] -->
26 81 5

<!-- b000934 | prose | pages [21] -->
Then we use the data to calculate the h with TOPSIS, and the results has been shown Table 3.

<!-- b000935 | prose | pages [21] -->
The effect on  of external factors

<!-- b000936 | prose | pages [21] -->
By analysis, we find that  not only is associated with the nature of the epidemic but also

<!-- b000937 | prose | pages [21] -->
affected by some external factors. These factors include population density, temperature, humidity, current epidemic situation ,open degree of ETC, economy, national education and

<!-- b000938 | prose | pages [21] -->
age. Hence,  vary from country to country. Some of these factors are change with time,

<!-- b000939 | prose | pages [21] -->
which result  changing with time. If we want to develop different reasonable long-term

<!-- b000940 | prose | pages [21] -->
delivery system for different countries, evaluating the external factor’s impact on  is needed.

<!-- b000941 | prose | pages [21] -->
For the same reason, we can estimate the effect of external facts on  with TOPSIS. We

<!-- b000942 | prose | pages [21] -->
define a influence coefficient C .usually, C is non-negative, and as it increase,  also

<!-- b000943 | prose | pages [21] -->
appear a growth.

<!-- b000944 | prose | pages [21] -->
The first four factors: population density, temperature, humidity, the current epidemic situation are defined as before. Obviously, their addition will result in increment of C. the other factors are redefined or defined as follows:  Open degree of ETC(Ebola treatment centers)

<!-- b000945 | prose | pages [21] -->
Considering there are many ETCs in a country, we redefine the open degree of ETC:

<!-- b000946 | prose | pages [21] -->
which could be calculated as follows:

<!-- b000947 | prose | pages [21] -->
 F

<!-- b000948 | prose | pages [21] -->
n

<!-- b000949 | prose | pages [21] -->
c

<!-- b000950 | prose | pages [21] -->
ih

<!-- b000951 | furniture | pages [21] -->


<!-- b000952 | prose | pages [21] -->
c

<!-- b000953 | prose | pages [21] -->
all

<!-- b000954 | prose | pages [21] -->
c c

<!-- b000955 | prose | pages [21] -->
open

<!-- b000956 | prose | pages [21] -->
is the number of open ETCs in the country, Where open

<!-- b000957 | prose | pages [21] -->
is the number of cities in the country. c all

<!-- b000958 | furniture | pages [21] -->


<!-- b000959 | prose | pages [21] -->
 Economy

<!-- b000960 | prose | pages [21] -->
In general situation, the more undeveloped a country is, the more difficult to control the epidemic is. Therefore, the economic situation of a country, measured by GDP per capital is an important indicator to determine the medical treatment level.

<!-- b000961 | prose | pages [21] -->
The economy of the n th country is represented by：

<!-- b000962 | prose | pages [21] -->
 National Education

<!-- b000963 | prose | pages [21] -->
E n

<!-- b000964 | furniture | pages [22] -->
Team # 35532                                                                          21 / 34

<!-- b000965 | furniture | pages [22] -->


<!-- b000966 | prose | pages [22] -->
Cremation do not comply with the local traditions in Africa, which is an important reason for the large-scale outbreak of Ebola. Ebola can spread through the corpses which lead a large number of people infected at the funeral. According to the survey, the higher the education level is, the greater the proportion of accept cremation is. Therefore, we choose the proportion of people received higher education in each country as a measure of the country's education level,

<!-- b000967 | heading | pages [22] -->
whose increment results increment of 

<!-- b000968 | prose | pages [22] -->
The education level of the n th country is represented by：

<!-- b000969 | prose | pages [22] -->
 Age

<!-- b000970 | prose | pages [22] -->
J n n

<!-- b000971 | prose | pages [22] -->
According to the report of the World Health Organization, the probability of being infected Ebola of young adults over the age of 14 is three times child below the age of 14, and the probability of poeple aged 65 or older is four times. Thus, we can see that the higher

<!-- b000972 | prose | pages [22] -->
proportion of the population over the age of 14 is, the greater the  will be. We define age

<!-- b000973 | prose | pages [22] -->
coefficient which could be calculated as follows:

<!-- b000974 | furniture | pages [22] -->


<!-- b000975 | prose | pages [22] -->
K

<!-- b000976 | prose | pages [22] -->


<!-- b000977 | furniture | pages [22] -->


<!-- b000978 | prose | pages [22] -->


<!-- b000979 | prose | pages [22] -->
K

<!-- b000980 | prose | pages [22] -->
14~65

<!-- b000981 | prose | pages [22] -->
K

<!-- b000982 | prose | pages [22] -->
65

<!-- b000983 | prose | pages [22] -->
K

<!-- b000984 | prose | pages [22] -->
all

<!-- b000985 | prose | pages [22] -->
Then we can use TOPSIS to estimate the variation of .

<!-- b000986 | prose | pages [22] -->
Considering the epidemic mainly spread in Sierra Leone, Guinea and Liberia, we select their data to solve our models and decide their drug allocation. By searching online carefully, we final get data needed from the website of World Bank.

<!-- b000987 | caption | pages [22] -->
Table 5: the data of the three country

<!-- b000988 | prose | pages [22] -->
current

<!-- b000989 | prose | pages [22] -->
Temperature

<!-- b000990 | prose | pages [22] -->
Humidity

<!-- b000991 | prose | pages [22] -->
disease

<!-- b000992 | furniture | pages [22] -->


<!-- b000993 | prose | pages [22] -->
Open

<!-- b000994 | prose | pages [22] -->
Economy

<!-- b000995 | prose | pages [22] -->
education

<!-- b000996 | prose | pages [22] -->
Population

<!-- b000997 | prose | pages [22] -->
age

<!-- b000998 | prose | pages [22] -->
coefficient

<!-- b000999 | prose | pages [22] -->
(%)

<!-- b001000 | prose | pages [22] -->
(ºC)

<!-- b001001 | prose | pages [22] -->
situation

<!-- b001002 | prose | pages [22] -->
2917 27 75 Guinea

<!-- b001003 | prose | pages [22] -->
8622 25 91 Liberia

<!-- b001004 | prose | pages [22] -->
Sierra

<!-- b001005 | prose | pages [22] -->
10518 27 85

<!-- b001006 | prose | pages [22] -->
Leone

<!-- b001007 | prose | pages [22] -->
Note: the unit of the population is People /per km After calculating ,the results are shown in Table

<!-- b001008 | prose | pages [22] -->
(dollar)

<!-- b001009 | prose | pages [22] -->
(% of all)

<!-- b001010 | prose | pages [22] -->
density

<!-- b001011 | prose | pages [22] -->
25 492 38.13 57.69 45.5

<!-- b001012 | prose | pages [22] -->
50 297 45.16 57.11 35.5

<!-- b001013 | prose | pages [22] -->
85 366 26.44 58.44 79.4

<!-- b001014 | caption | pages [22] -->
Table 6 the initial influence coefficient of three country

<!-- b001015 | furniture | pages [22] -->


<!-- b001016 | prose | pages [22] -->
Guinea

<!-- b001017 | prose | pages [22] -->
Liberia Sierra Leone

<!-- b001018 | prose | pages [22] -->
C

<!-- b001019 | prose | pages [22] -->
0.28615361

<!-- b001020 | prose | pages [22] -->
0.467444301 0.728861892

<!-- b001021 | furniture | pages [23] -->
Team # 35532                                                                          22 / 34

<!-- b001022 | furniture | pages [23] -->


<!-- b001023 | prose | pages [23] -->
C will be used later.

<!-- b001024 | prose | pages [23] -->
Part IV

<!-- b001025 | heading | pages [23] -->
Assumptions

<!-- b001026 | prose | pages [23] -->
 7 5 10 doses every year[14], we can calculate (1).Ebola drug production in the world can reach

<!-- b001027 | prose | pages [23] -->
the increment rate of production speed with this data.

<!-- b001028 | prose | pages [23] -->
 5 2 10 (2).The maximal amount of drugs produced per day can finally reach doses every year.

<!-- b001029 | prose | pages [23] -->
(3). Each patient needs 1 portion to rehabilitation, and each portion contain 10 doses drug. (4) Assumed that the drug distributed in every period of drug delivery are be used evenly every day.

<!-- b001030 | heading | pages [23] -->
Model:

<!-- b001031 | prose | pages [23] -->
Drug production model based logisitic. Because  This model meets these characteristic that the production in initial time is small, then sharp increase in the mid-production .and production in the finally time is large and stable.  the derivative of drug production rate increases at first and then decreases to zero. Therefore, we assume that the relationship between the drug production and time meets the logistic growth model, and the following equation can be listed:

<!-- b001032 | prose | pages [23] -->
dG

<!-- b001033 | prose | pages [23] -->


<!-- b001034 | prose | pages [23] -->
rt dg

<!-- b001035 | prose | pages [23] -->


<!-- b001036 | prose | pages [23] -->
G t

<!-- b001037 | prose | pages [23] -->
( )

<!-- b001038 | prose | pages [23] -->
0

<!-- b001039 | prose | pages [23] -->
G

<!-- b001040 | prose | pages [23] -->


<!-- b001041 | prose | pages [23] -->
(1 )

<!-- b001042 | prose | pages [23] -->
G

<!-- b001043 | furniture | pages [23] -->


<!-- b001044 | prose | pages [23] -->
m

<!-- b001045 | prose | pages [23] -->
100

<!-- b001046 | prose | pages [23] -->
G :the daily production of drugs, namely the production speed.

<!-- b001047 | prose | pages [23] -->
G : the maximal production speed of drugs. m

<!-- b001048 | prose | pages [23] -->
rt : growth rate of drug production speed. amount of the drug delivered every time

<!-- b001049 | prose | pages [23] -->
Our drug delivery plan think that there is only a drug delivery in a period of drug delivery

<!-- b001050 | prose | pages [23] -->
 T 14 days T . Let , Which is reasonable because it can save cost and don’t cause delay to p

<!-- b001051 | prose | pages [23] -->
the Ebola’s controlling.

<!-- b001052 | prose | pages [23] -->
Because drugs’ transporting need a certain period of time, and the drug output everyday, so we need to calculate the aggregate of drug which is the based of delivery.

<!-- b001053 | prose | pages [23] -->
 P t

<!-- b001054 | prose | pages [23] -->
n

<!-- b001055 | prose | pages [23] -->
 

<!-- b001056 | prose | pages [23] -->
t t T

<!-- b001057 | prose | pages [23] -->
n n p

<!-- b001058 | prose | pages [23] -->
Gdt

<!-- b001059 | furniture | pages [23] -->


<!-- b001060 | prose | pages [23] -->
t t

<!-- b001061 | prose | pages [23] -->
n n

<!-- b001062 | prose | pages [23] -->
nt ：the first day of the time period of drug delivery.

<!-- b001063 | prose | pages [23] -->
T : the period of drug delivery p

<!-- b001064 | heading | pages [23] -->
Delivery model

<!-- b001065 | prose | pages [23] -->
According to former analysis, drug production and drug demand change over time.

<!-- b001066 | furniture | pages [24] -->
Team # 35532                                                                          23 / 34

<!-- b001067 | furniture | pages [24] -->


<!-- b001068 | prose | pages [24] -->
Comparing the drug production model and drug demand models, we can divide the whole duration into two stage: stage severely short in drugs and stage relative sufficient in drugs. now, we choose the 150th days as a time node.150th days ago, we faced with a severe drug shortage, and our purposes is to control the increment rate of the infectious .After 150th days, the production of the drugs achieve the certain number and the purpose become to reduce the number of death every day.

<!-- b001069 | heading | pages [24] -->
Delivery model at the stage severely short in drugs

<!-- b001070 | heading | pages [24] -->
Nonlinear programming model

<!-- b001071 | prose | pages [24] -->
In the first stage of drug manufacturing, Because of the great shortage in drug, many patients can’t get effective medical treatment, and the increment of the infectious and deaths are both high.

<!-- b001072 | prose | pages [24] -->
In this moment, we should give priority to the decrement of the increment of the infectious to make the epidemic becoming under the control as soon as possible which will benefit later epidemic controlling.

<!-- b001073 | prose | pages [24] -->
Hence, For the first stage of drug manufacturing, we build a nonlinear programming model:  the optimization goal which is minimizing the number of the infection sources of all countries:

<!-- b001074 | prose | pages [24] -->
k

<!-- b001075 | prose | pages [24] -->


<!-- b001076 | prose | pages [24] -->
Min

<!-- b001077 | prose | pages [24] -->
I

<!-- b001078 | prose | pages [24] -->


<!-- b001079 | prose | pages [24] -->
i

<!-- b001080 | prose | pages [24] -->
1

<!-- b001081 | prose | pages [24] -->


<!-- b001082 | prose | pages [24] -->
,

<!-- b001083 | prose | pages [24] -->
i

<!-- b001084 | prose | pages [24] -->
1,2, ,

<!-- b001085 | prose | pages [24] -->
k

<!-- b001086 | furniture | pages [24] -->


<!-- b001087 | prose | pages [24] -->
i free

<!-- b001088 | prose | pages [24] -->
, ,

<!-- b001089 | prose | pages [24] -->
Where k is the number of countries needing drug assistance, and I is the average ,i free

<!-- b001090 | prose | pages [24] -->
number of infectious individuals non-isolated of the i th country in a period of drug delivery.

<!-- b001091 | prose | pages [24] -->
 G t , ( ) the decision variables is the drug allocation distributed for each country noted by i

<!-- b001092 | prose | pages [24] -->
it refers the doses of drugs needed by the i th country.  the resistant condition is actual number of drugs.

<!-- b001093 | prose | pages [24] -->
k

<!-- b001094 | prose | pages [24] -->
 

<!-- b001095 | prose | pages [24] -->
G t

<!-- b001096 | prose | pages [24] -->
( )

<!-- b001097 | prose | pages [24] -->
P

<!-- b001098 | prose | pages [24] -->
i

<!-- b001099 | prose | pages [24] -->


<!-- b001100 | prose | pages [24] -->
i

<!-- b001101 | prose | pages [24] -->
1

<!-- b001102 | prose | pages [24] -->


<!-- b001103 | prose | pages [24] -->
, ,

<!-- b001104 | prose | pages [24] -->
i

<!-- b001105 | prose | pages [24] -->
1,2, ,

<!-- b001106 | prose | pages [24] -->
k

<!-- b001107 | furniture | pages [24] -->


<!-- b001108 | prose | pages [24] -->
t t

<!-- b001109 | prose | pages [24] -->
n n

<!-- b001110 | prose | pages [24] -->
Therefore, a Nonlinear programming optimization model of drug distribution is modeled as follows:

<!-- b001111 | prose | pages [24] -->
Min

<!-- b001112 | prose | pages [24] -->
k

<!-- b001113 | prose | pages [24] -->
 

<!-- b001114 | prose | pages [24] -->
G t

<!-- b001115 | prose | pages [24] -->
( )

<!-- b001116 | prose | pages [24] -->
i

<!-- b001117 | prose | pages [24] -->


<!-- b001118 | prose | pages [24] -->
i

<!-- b001119 | prose | pages [24] -->
1

<!-- b001120 | prose | pages [24] -->
 i

<!-- b001121 | furniture | pages [24] -->


<!-- b001122 | furniture | pages [24] -->


<!-- b001123 | prose | pages [24] -->
k

<!-- b001124 | prose | pages [24] -->


<!-- b001125 | prose | pages [24] -->
I

<!-- b001126 | prose | pages [24] -->
,

<!-- b001127 | prose | pages [24] -->
i free

<!-- b001128 | prose | pages [24] -->
,

<!-- b001129 | prose | pages [24] -->
i

<!-- b001130 | prose | pages [24] -->
1

<!-- b001131 | prose | pages [24] -->


<!-- b001132 | prose | pages [24] -->
P P

<!-- b001133 | prose | pages [24] -->
,

<!-- b001134 | prose | pages [24] -->
i

<!-- b001135 | prose | pages [24] -->
1,2, ,

<!-- b001136 | prose | pages [24] -->
k

<!-- b001137 | furniture | pages [24] -->


<!-- b001138 | prose | pages [24] -->
t t

<!-- b001139 | prose | pages [24] -->
n

<!-- b001140 | prose | pages [24] -->
1,2 , k .

<!-- b001141 | heading | pages [24] -->
delivery model at the stage relatively sufficient in drugs

<!-- b001142 | prose | pages [24] -->
As time goes on, the speed of drug manufacturing grows rapidly. After a period of time, the

<!-- b001143 | furniture | pages [25] -->
Team # 35532                                                                          24 / 34

<!-- b001144 | furniture | pages [25] -->


<!-- b001145 | prose | pages [25] -->
speed of drugs become high enough to meet the need of every countries to control disease. In the moment, our goal become to minimize death cases every day with the number of the infectious stable. So, a multi-objective optimization model will be developed next based on the former model for the second stage.

<!-- b001146 | prose | pages [25] -->
Our goal can be described as follows:

<!-- b001147 | prose | pages [25] -->
Min

<!-- b001148 | prose | pages [25] -->
dD i

<!-- b001149 | prose | pages [25] -->
dD

<!-- b001150 | prose | pages [25] -->
k k

<!-- b001151 | prose | pages [25] -->
 

<!-- b001152 | prose | pages [25] -->
i

<!-- b001153 | prose | pages [25] -->
, dt

<!-- b001154 | prose | pages [25] -->
i i

<!-- b001155 | prose | pages [25] -->
1 1

<!-- b001156 | prose | pages [25] -->
is the average death cases per day in a period of drug delivery.

<!-- b001157 | prose | pages [25] -->
Where

<!-- b001158 | prose | pages [25] -->
dt

<!-- b001159 | prose | pages [25] -->
And

<!-- b001160 | prose | pages [25] -->
Min

<!-- b001161 | prose | pages [25] -->
At least making it stable. And there are two constraint condition, one is the drug amount restriction:

<!-- b001162 | prose | pages [25] -->
k

<!-- b001163 | prose | pages [25] -->
 

<!-- b001164 | prose | pages [25] -->
G t

<!-- b001165 | prose | pages [25] -->
( )

<!-- b001166 | prose | pages [25] -->
P

<!-- b001167 | prose | pages [25] -->
i

<!-- b001168 | prose | pages [25] -->


<!-- b001169 | prose | pages [25] -->
i

<!-- b001170 | prose | pages [25] -->
1

<!-- b001171 | prose | pages [25] -->
k k

<!-- b001172 | prose | pages [25] -->
 

<!-- b001173 | prose | pages [25] -->
I

<!-- b001174 | prose | pages [25] -->
,

<!-- b001175 | prose | pages [25] -->
i free

<!-- b001176 | prose | pages [25] -->
,

<!-- b001177 | prose | pages [25] -->
i i

<!-- b001178 | prose | pages [25] -->
1 1

<!-- b001179 | prose | pages [25] -->


<!-- b001180 | prose | pages [25] -->
, ,

<!-- b001181 | prose | pages [25] -->
i

<!-- b001182 | prose | pages [25] -->
1,2, ,

<!-- b001183 | prose | pages [25] -->
k

<!-- b001184 | prose | pages [25] -->
.

<!-- b001185 | prose | pages [25] -->
t t

<!-- b001186 | prose | pages [25] -->
n n

<!-- b001187 | prose | pages [25] -->
The other is to consider the fairness to some extent:

<!-- b001188 | furniture | pages [25] -->


<!-- b001189 | prose | pages [25] -->
I I

<!-- b001190 | prose | pages [25] -->
k

<!-- b001191 | prose | pages [25] -->
1

<!-- b001192 | prose | pages [25] -->
 

<!-- b001193 | prose | pages [25] -->
i free

<!-- b001194 | prose | pages [25] -->
,

<!-- b001195 | prose | pages [25] -->
i free

<!-- b001196 | prose | pages [25] -->
,

<!-- b001197 | prose | pages [25] -->
( )

<!-- b001198 | prose | pages [25] -->
N k N 

<!-- b001199 | prose | pages [25] -->
i

<!-- b001200 | prose | pages [25] -->
1

<!-- b001201 | prose | pages [25] -->
i i

<!-- b001202 | prose | pages [25] -->
Where

<!-- b001203 | prose | pages [25] -->
N is i th country’s the total population. i

<!-- b001204 | prose | pages [25] -->
I

<!-- b001205 | prose | pages [25] -->
,i free

<!-- b001206 | furniture | pages [25] -->


<!-- b001207 | furniture | pages [25] -->


<!-- b001208 | furniture | pages [25] -->


<!-- b001209 | prose | pages [25] -->
I

<!-- b001210 | prose | pages [25] -->
k

<!-- b001211 | prose | pages [25] -->
1 1

<!-- b001212 | prose | pages [25] -->
 

<!-- b001213 | prose | pages [25] -->
i free

<!-- b001214 | prose | pages [25] -->
,

<!-- b001215 | prose | pages [25] -->
0.2

<!-- b001216 | prose | pages [25] -->
（11）. k k N 

<!-- b001217 | prose | pages [25] -->
i i

<!-- b001218 | prose | pages [25] -->
1

<!-- b001219 | prose | pages [25] -->
i

<!-- b001220 | prose | pages [25] -->
I

<!-- b001221 | prose | pages [25] -->
k 1

<!-- b001222 | prose | pages [25] -->


<!-- b001223 | prose | pages [25] -->
i free

<!-- b001224 | prose | pages [25] -->
,

<!-- b001225 | prose | pages [25] -->
is i th country’s percent of infectious individuals.

<!-- b001226 | prose | pages [25] -->
N

<!-- b001227 | prose | pages [25] -->
i

<!-- b001228 | prose | pages [25] -->
of uncontrolled infectious individuals.

<!-- b001229 | prose | pages [25] -->
is average percent k N

<!-- b001230 | prose | pages [25] -->
i

<!-- b001231 | prose | pages [25] -->
1

<!-- b001232 | prose | pages [25] -->
i

<!-- b001233 | prose | pages [25] -->
This shows the ration of difference between the proportion of patients non-isolated in all the population and the mean value of all the countries to the mean value of all the countries is less 20%. This will make the drug distribution is more evenly. The multi-objective optimization model can be described by following formulas:

<!-- b001234 | prose | pages [25] -->
min

<!-- b001235 | prose | pages [25] -->
min

<!-- b001236 | furniture | pages [25] -->


<!-- b001237 | prose | pages [25] -->
s t

<!-- b001238 | prose | pages [25] -->
. .

<!-- b001239 | prose | pages [25] -->
k k

<!-- b001240 | prose | pages [25] -->


<!-- b001241 | prose | pages [25] -->
D

<!-- b001242 | prose | pages [25] -->
,

<!-- b001243 | prose | pages [25] -->
i

<!-- b001244 | prose | pages [25] -->


<!-- b001245 | prose | pages [25] -->
i i

<!-- b001246 | prose | pages [25] -->
1

<!-- b001247 | prose | pages [25] -->
k k

<!-- b001248 | prose | pages [25] -->


<!-- b001249 | prose | pages [25] -->
I

<!-- b001250 | furniture | pages [25] -->


<!-- b001251 | prose | pages [25] -->
i free

<!-- b001252 | prose | pages [25] -->
,

<!-- b001253 | prose | pages [25] -->


<!-- b001254 | prose | pages [25] -->
i i

<!-- b001255 | prose | pages [25] -->
1

<!-- b001256 | prose | pages [25] -->
k k

<!-- b001257 | prose | pages [25] -->


<!-- b001258 | prose | pages [25] -->


<!-- b001259 | prose | pages [25] -->
G t

<!-- b001260 | prose | pages [25] -->
( )

<!-- b001261 | prose | pages [25] -->
P

<!-- b001262 | prose | pages [25] -->
i t

<!-- b001263 | prose | pages [25] -->
n

<!-- b001264 | prose | pages [25] -->
 

<!-- b001265 | prose | pages [25] -->
i i

<!-- b001266 | prose | pages [25] -->
1

<!-- b001267 | furniture | pages [26] -->
Team # 35532                                                                          25 / 34

<!-- b001268 | furniture | pages [26] -->


<!-- b001269 | prose | pages [26] -->
I I

<!-- b001270 | prose | pages [26] -->
k

<!-- b001271 | prose | pages [26] -->
1

<!-- b001272 | prose | pages [26] -->
 

<!-- b001273 | prose | pages [26] -->
i free

<!-- b001274 | prose | pages [26] -->
,

<!-- b001275 | prose | pages [26] -->
i free

<!-- b001276 | prose | pages [26] -->
,

<!-- b001277 | prose | pages [26] -->
(

<!-- b001278 | prose | pages [26] -->
N k N 

<!-- b001279 | prose | pages [26] -->
i

<!-- b001280 | prose | pages [26] -->
1

<!-- b001281 | prose | pages [26] -->
i i

<!-- b001282 | prose | pages [26] -->
D D

<!-- b001283 | prose | pages [26] -->
k

<!-- b001284 | prose | pages [26] -->
1

<!-- b001285 | prose | pages [26] -->
 

<!-- b001286 | prose | pages [26] -->
i free

<!-- b001287 | prose | pages [26] -->
,

<!-- b001288 | prose | pages [26] -->
i free

<!-- b001289 | prose | pages [26] -->
,

<!-- b001290 | prose | pages [26] -->
(

<!-- b001291 | prose | pages [26] -->
N k N 

<!-- b001292 | prose | pages [26] -->
i

<!-- b001293 | prose | pages [26] -->
1

<!-- b001294 | prose | pages [26] -->
i i

<!-- b001295 | prose | pages [26] -->


<!-- b001296 | furniture | pages [26] -->


<!-- b001297 | prose | pages [26] -->
G t

<!-- b001298 | heading | pages [26] -->
Results & analysis

<!-- b001299 | prose | pages [26] -->
I

<!-- b001300 | prose | pages [26] -->
k

<!-- b001301 | prose | pages [26] -->
1

<!-- b001302 | prose | pages [26] -->
 

<!-- b001303 | prose | pages [26] -->
i free

<!-- b001304 | prose | pages [26] -->
,

<!-- b001305 | prose | pages [26] -->
) ) 0.2

<!-- b001306 | furniture | pages [26] -->


<!-- b001307 | prose | pages [26] -->
k N 

<!-- b001308 | prose | pages [26] -->
i

<!-- b001309 | prose | pages [26] -->
1

<!-- b001310 | prose | pages [26] -->
i

<!-- b001311 | prose | pages [26] -->
D

<!-- b001312 | prose | pages [26] -->
k

<!-- b001313 | prose | pages [26] -->
1

<!-- b001314 | prose | pages [26] -->
 

<!-- b001315 | prose | pages [26] -->
i free

<!-- b001316 | prose | pages [26] -->
,

<!-- b001317 | prose | pages [26] -->
) ) 0.2

<!-- b001318 | furniture | pages [26] -->


<!-- b001319 | prose | pages [26] -->
k N 

<!-- b001320 | prose | pages [26] -->
i

<!-- b001321 | prose | pages [26] -->
1

<!-- b001322 | prose | pages [26] -->
i

<!-- b001323 | prose | pages [26] -->
 ( ) 0

<!-- b001324 | furniture | pages [26] -->


<!-- b001325 | prose | pages [26] -->
i i

<!-- b001326 | furniture | pages [26] -->


<!-- b001327 | furniture | pages [26] -->


<!-- b001328 | prose | pages [26] -->


<!-- b001329 | heading | pages [26] -->
In the Drug production model, the formula (1

<!-- b001330 | prose | pages [26] -->
G G ) represent the resistance from the m

<!-- b001331 | prose | pages [26] -->
finite ability to manufacture drug. Obviously, as t goes on, rt becomes larger ，and

<!-- b001332 | prose | pages [26] -->
 (1 G G ) becomes smaller ，the increment of manufacturing speed of drugs depend both m

<!-- b001333 | prose | pages [26] -->
on them. According to the assumption (1) and (2), and supposed that at the 100th day, the manufacturing speed of drugs reaches the maximum, we can know that the maximal manufacturing speed of drugs

<!-- b001334 | prose | pages [26] -->
G = m  5 2 10 .

<!-- b001335 | prose | pages [26] -->
And we solved the model with ode toolbox in Matlab2014 numerically. The result is shown in Fig.8.

<!-- b001336 | caption | pages [26] -->
Fig.8 the model based on logisitic

<!-- b001337 | furniture | pages [26] -->


<!-- b001338 | furniture | pages [26] -->


<!-- b001339 | prose | pages [26] -->
Since the epidemic mainly spread in Guinea, Liberia, Sierra Leone, we consider the situation where all the drugs are provided to these three country, and make a half-of-year drug delivery plan and predict the spreading trend in the half of year with the SEIIR model with efficient medication.

<!-- b001340 | prose | pages [26] -->
Suppose we start to distribute the drug from the 100th day since the epidemic spread. Table.7

<!-- b001341 | furniture | pages [27] -->
Team # 35532                                                                          26 / 34

<!-- b001342 | furniture | pages [27] -->


<!-- b001343 | prose | pages [27] -->
shows the value of parameters that moment.

<!-- b001344 | furniture | pages [27] -->


<!-- b001345 | caption | pages [27] -->
Table 7 the value of parameters that moment

<!-- b001346 | furniture | pages [27] -->


<!-- b001347 | prose | pages [27] -->
I E S 0 0 I R D

<!-- b001348 | furniture | pages [27] -->


<!-- b001349 | furniture | pages [27] -->


<!-- b001350 | prose | pages [27] -->
0, free 0,isolated 0 0

<!-- b001351 | prose | pages [27] -->
639 12181398 4775 Guinea 1209 243 1910

<!-- b001352 | prose | pages [27] -->
1228 4129792 9215 Liberia

<!-- b001353 | prose | pages [27] -->
Sierra

<!-- b001354 | prose | pages [27] -->
2333 453 3686

<!-- b001355 | prose | pages [27] -->
1042 6223952 7799

<!-- b001356 | prose | pages [27] -->
Leone

<!-- b001357 | prose | pages [27] -->
1079 475 3199

<!-- b001358 | prose | pages [27] -->
In our plan, the period of drug delivery is 14 days, therefore, we will make the new delivery plan every 14 days. As we know from the former analysis, within the half of year, the value of

<!-- b001359 | prose | pages [27] -->
 vary from country to country and will change with time. Due to this, to recalculate the value

<!-- b001360 | prose | pages [27] -->
of  after a certain period time is also needed. We recalculate  with the TOSIS mentioned

<!-- b001361 | prose | pages [27] -->
above every month.

<!-- b001362 | heading | pages [27] -->
Solving the optimization model with optimization toolbox in Matlab2014. We get our

<!-- b001363 | prose | pages [27] -->
delivery plan for six month shown as following table and figure.

<!-- b001364 | furniture | pages [27] -->


<!-- b001365 | furniture | pages [27] -->


<!-- b001366 | prose | pages [27] -->
Infected

<!-- b001367 | prose | pages [27] -->
Death

<!-- b001368 | prose | pages [27] -->
portion

<!-- b001369 | furniture | pages [27] -->


<!-- b001370 | prose | pages [27] -->
case

<!-- b001371 | prose | pages [27] -->
case

<!-- b001372 | prose | pages [27] -->
8380 2865 108

<!-- b001373 | furniture | pages [27] -->


<!-- b001374 | prose | pages [27] -->
Infected

<!-- b001375 | prose | pages [27] -->
Death

<!-- b001376 | prose | pages [27] -->
portion

<!-- b001377 | prose | pages [27] -->
Case

<!-- b001378 | prose | pages [27] -->
case

<!-- b001379 | prose | pages [27] -->
Guinea Guinea 8730 2984 456 Liberia Liberia 19334 5529 235

<!-- b001380 | prose | pages [27] -->
15586 4798 345

<!-- b001381 | prose | pages [27] -->
23986 5769 679

<!-- b001382 | prose | pages [27] -->
Sierra

<!-- b001383 | prose | pages [27] -->
Sierra

<!-- b001384 | prose | pages [27] -->
16142 5032 589

<!-- b001385 | prose | pages [27] -->
Leone

<!-- b001386 | prose | pages [27] -->
Leone

<!-- b001387 | furniture | pages [28] -->
Team # 35532                                                                          27 / 34

<!-- b001388 | furniture | pages [28] -->


<!-- b001389 | furniture | pages [28] -->


<!-- b001390 | prose | pages [28] -->
Infected

<!-- b001391 | prose | pages [28] -->
Death

<!-- b001392 | prose | pages [28] -->
portion

<!-- b001393 | furniture | pages [28] -->


<!-- b001394 | prose | pages [28] -->
case

<!-- b001395 | prose | pages [28] -->
case

<!-- b001396 | prose | pages [28] -->
Guinea 16661 3284 685 Liberia 21805 6169 891 Sierra 16142 5648 981 Leone

<!-- b001397 | furniture | pages [28] -->


<!-- b001398 | prose | pages [28] -->
Infect

<!-- b001399 | prose | pages [28] -->
Death

<!-- b001400 | prose | pages [28] -->
portion

<!-- b001401 | furniture | pages [28] -->


<!-- b001402 | prose | pages [28] -->
ed

<!-- b001403 | prose | pages [28] -->
case

<!-- b001404 | prose | pages [28] -->
case

<!-- b001405 | furniture | pages [28] -->


<!-- b001406 | prose | pages [28] -->
Infected

<!-- b001407 | prose | pages [28] -->
Death

<!-- b001408 | prose | pages [28] -->
portion

<!-- b001409 | prose | pages [28] -->
case

<!-- b001410 | prose | pages [28] -->
case

<!-- b001411 | prose | pages [28] -->
Guinea 6905 3367 986 Liberia 18954 6398 1278 Sierra 13834 5781 1189 Leone

<!-- b001412 | furniture | pages [28] -->


<!-- b001413 | prose | pages [28] -->
Infected

<!-- b001414 | prose | pages [28] -->
Death

<!-- b001415 | prose | pages [28] -->
portion

<!-- b001416 | prose | pages [28] -->
case

<!-- b001417 | prose | pages [28] -->
case

<!-- b001418 | prose | pages [28] -->
Guinea Guinea 4101 3475 1230 1771 3586 1580 Liberia Liberia 8747 6430 1806 2767 6529 2209

<!-- b001419 | prose | pages [28] -->
Sierra

<!-- b001420 | prose | pages [28] -->
Sierra

<!-- b001421 | prose | pages [28] -->
8639 5863 1698

<!-- b001422 | prose | pages [28] -->
3910 5965 2497

<!-- b001423 | prose | pages [28] -->
Leone

<!-- b001424 | prose | pages [28] -->
Leone

<!-- b001425 | prose | pages [28] -->
The figures show the spreading trends of the Ebola in the three country in the next half of year. The tables show the total death cases and total infected cases at the moments delivering drugs .and the portions delivered to three country every time. According to the assumption (3), a portion of drugs equals to ten doses of drugs which can be used to cure one patient totally.

<!-- b001426 | heading | pages [28] -->
Conclusion

<!-- b001427 | prose | pages [28] -->
The isolation method and drug intervention can effectively control the EBOV spreading. And Drug manufacturing can also influence epidemic control. The difference between each country will cause the epidemic situation is different. So making epidemic control Strategy need consider a great deal.

<!-- b001428 | furniture | pages [29] -->
Team # 35532                                                                          28 / 34

<!-- b001429 | furniture | pages [29] -->


<!-- b001430 | prose | pages [29] -->
Considering many factors including isolated method, drug intervention, geographical conditions, the differences between different countries, the characteristics of the spread of the virus, we build those models.

<!-- b001431 | prose | pages [29] -->
Model I can forecast the Infectious disease situation. Model II can determine the location of drug station. Model III can make the optimal choice of each country's number of drug. All of these help eradicating Ebola.

<!-- b001432 | heading | pages [29] -->
Model extending

<!-- b001433 | prose | pages [29] -->
In SEIIR with effective drug intervention model, we assume that medication only refers to drugs used therapy of Ebola, not include vaccine; Medications only work on patients but the vaccine can be used for individuals who live in the Susceptible area . Now we consider drugs and vaccines can simultaneously supply. The vaccines production is F dose per day. The drug production isG dose per day. Vaccine is able to let the individual to produce antibodies against the virus. So this formula (1) can be rewritten as

<!-- b001434 | prose | pages [29] -->


<!-- b001435 | prose | pages [29] -->
dS

<!-- b001436 | furniture | pages [29] -->


<!-- b001437 | prose | pages [29] -->


<!-- b001438 | prose | pages [29] -->
dt SI SI free

<!-- b001439 | prose | pages [29] -->


<!-- b001440 | prose | pages [29] -->
F t ( ). N N

<!-- b001441 | prose | pages [29] -->
At the same time putting the immune into the survivor population, then this formula (3) can be rewritten as

<!-- b001442 | prose | pages [29] -->
dR      (1 f ) I (1 1 free dt    f f ) I M t ( ) F t ( ).

<!-- b001443 | prose | pages [29] -->
. 2 2 isolated

<!-- b001444 | prose | pages [29] -->
SEIIR with effective drug intervention model was extended to SEIIR with effective drug and

<!-- b001445 | prose | pages [29] -->
Vaccine intervention model. At the same time F Consistent with the Logistic block growth model，then

<!-- b001446 | prose | pages [29] -->
dF  rt

<!-- b001447 | prose | pages [29] -->
1 (1

<!-- b001448 | prose | pages [29] -->
dg

<!-- b001449 | prose | pages [29] -->
F t ( ) 0

<!-- b001450 | prose | pages [29] -->
F 

<!-- b001451 | prose | pages [29] -->
)

<!-- b001452 | prose | pages [29] -->
， F

<!-- b001453 | prose | pages [29] -->
m

<!-- b001454 | prose | pages [29] -->
  100.

<!-- b001455 | furniture | pages [29] -->


<!-- b001456 | prose | pages [29] -->
F is maximum of the vaccines production rate，1r is vaccines production growth rate. m

<!-- b001457 | heading | pages [29] -->
Sensitivity Analysis

<!-- b001458 | heading | pages [29] -->
SEIIR with effective drug intervention model

<!-- b001459 | prose | pages [29] -->
 There are some coefficients related to properties of the virus in SEIIR with effective drug intervention model:

<!-- b001460 | prose | pages [29] -->
1 : The average durations of incubation, 1 : the average durations of infectiousness, : the transmission rate. We analysis the effect of the three factors on the death case by changing them.

<!-- b001461 | caption | pages [29] -->
Table 8:the three factors on the death case

<!-- b001462 | furniture | pages [29] -->


<!-- b001463 | prose | pages [29] -->
Initial value

<!-- b001464 | prose | pages [29] -->
1  5.3

<!-- b001465 | prose | pages [29] -->
Changed value Changed percent

<!-- b001466 | prose | pages [29] -->
6 13.21%

<!-- b001467 | furniture | pages [30] -->
Team # 35532                                                                          29 / 34

<!-- b001468 | furniture | pages [30] -->


<!-- b001469 | prose | pages [30] -->
the death case 119556

<!-- b001470 | prose | pages [30] -->
1  5.61

<!-- b001471 | prose | pages [30] -->
the death case 119556

<!-- b001472 | prose | pages [30] -->
 0.27

<!-- b001473 | prose | pages [30] -->
the death case 119556

<!-- b001474 | prose | pages [30] -->
124870 4.44%

<!-- b001475 | prose | pages [30] -->
6.3 12.31%

<!-- b001476 | prose | pages [30] -->
131690 10.15%

<!-- b001477 | prose | pages [30] -->
0.5 46%

<!-- b001478 | prose | pages [30] -->
9343221 681.4%

<!-- b001479 | prose | pages [30] -->
changes, and death cases

<!-- b001480 | caption | pages [30] -->
Fig. 9: The

<!-- b001481 | prose | pages [30] -->
The table 8 shows that  is the factor which has the greatest effect on the death case

<!-- b001482 | heading | pages [30] -->
among the properties, and fig.9 shows the result graphicall

<!-- b001483 | furniture | pages [30] -->


<!-- b001484 | prose | pages [30] -->
In conclusion, is a key factors to control Ebola, we can take some measures, such as control

<!-- b001485 | prose | pages [30] -->
the population density, isolation and so on, to reduce it.

<!-- b001486 | prose | pages [30] -->
E (2) Change the 0

<!-- b001487 | prose | pages [30] -->
S ,exposed When solving the models, we have set initial values of the initial susceptive

<!-- b001488 | prose | pages [30] -->
E ,infectious S ,

<!-- b001489 | prose | pages [30] -->
0

<!-- b001490 | prose | pages [30] -->
0I , we can get relatively data from the data statistics of WHO. 0I ,etc. As for 0 0

<!-- b001491 | prose | pages [30] -->
creases, and death cases increases

<!-- b001492 | caption | pages [30] -->
Fig.10:

<!-- b001493 | furniture | pages [31] -->
Team # 35532                                                                          30 / 34

<!-- b001494 | furniture | pages [31] -->


<!-- b001495 | prose | pages [31] -->
E by estimation. So it is necessary to evaluate the effectiveness But we only can inaccurate 0

<!-- b001496 | heading | pages [31] -->
E and observing the change of result. We change

<!-- b001497 | prose | pages [31] -->
by changing 0

<!-- b001498 | prose | pages [31] -->
of 10.

<!-- b001499 | prose | pages [31] -->
E from 10 to 1000 by step 0

<!-- b001500 | heading | pages [31] -->
E increases. In conclusion,

<!-- b001501 | prose | pages [31] -->
As we can see from fig. 10, the death case increases related to 0

<!-- b001502 | prose | pages [31] -->
E can affect the result greatly. When we set model for predicting the future trend, we the 0

<!-- b001503 | prose | pages [31] -->
should determine the value of , E based on the reality situation , which will make the finally 0

<!-- b001504 | prose | pages [31] -->
forecasting more accurate.

<!-- b001505 | heading | pages [31] -->
(2) delivery systems model

<!-- b001506 | prose | pages [31] -->
When we build the drug delivery systems model, we use the Logistic block growth model describe the change of drug production speed with time. It’s a reasonable assumption. However, in the real world ,the relationship between the output of drug and time may vary from it. Not

<!-- b001507 | heading | pages [31] -->
G can also influent the results (r is the increase speed of

<!-- b001508 | prose | pages [31] -->
only that, the coefficients r and m

<!-- b001509 | prose | pages [31] -->
G is the maximum daily output).Similarly, we study their influence by output growth rate;

<!-- b001510 | prose | pages [31] -->
m

<!-- b001511 | prose | pages [31] -->
changing the value of them separately, The sensitivity tor .  The results of sensitivity analysis to r is shown on Table.9.

<!-- b001512 | prose | pages [31] -->
Table 9

<!-- b001513 | prose | pages [31] -->
The days use r

<!-- b001514 | prose | pages [31] -->
to control

<!-- b001515 | prose | pages [31] -->
50 250

<!-- b001516 | prose | pages [31] -->
100(100%) 162(35.3%)

<!-- b001517 | prose | pages [31] -->
200(400%) 102(59.2%)

<!-- b001518 | prose | pages [31] -->
The death case

<!-- b001519 | prose | pages [31] -->
629128

<!-- b001520 | prose | pages [31] -->
124870(80.1%)

<!-- b001521 | prose | pages [31] -->
272934(56.6%) From the Table 2, we find an obvious phenomenon that the bigger the value is ,the earlier the situation become under control.

<!-- b001522 | prose | pages [31] -->
G

<!-- b001523 | heading | pages [31] -->
The sensitivity to

<!-- b001524 | prose | pages [31] -->
 m

<!-- b001525 | prose | pages [31] -->
G have been changed from 100 to 10000 by step of 100. The m

<!-- b001526 | prose | pages [31] -->
We see the needed time to make the epidemic under the control is changed with the change of

<!-- b001527 | prose | pages [31] -->
G in the Fig.11 m

<!-- b001528 | furniture | pages [32] -->
Team # 35532                                                                          31 / 34

<!-- b001529 | furniture | pages [32] -->


<!-- b001530 | furniture | pages [32] -->


<!-- b001531 | prose | pages [32] -->
Fig.11 Epidemic controlling is very sensitive to the maximal daily output. The more the maximum daily output is, the less the death case is less. When the maximal daily output is under 4000 dose per day, the drug production can’t meet the need of epidemic controlling. When the maximum daily output is smaller, it is more difficult to control the epidemic and the death cases become high. Therefore, a way to control the epidemic and reduce the death cases is maximize the output every day and improve the increase speed of output growth rate.

<!-- b001532 | heading | pages [32] -->
Weakness and strengths

<!-- b001533 | heading | pages [32] -->
Weakness:

<!-- b001534 | prose | pages [32] -->
In model 1, according to the sensitivity analysis, the simulation results depend on largely the initial values of parameters and coefficients. But some values of the parameters can be only estimated, which can be inaccurate. In addition, the virus has a large probability of mutation, and some parameters will changed which we ignored, which will decrease the validity of the model. In model 2, to simplify the problem, we set all the medical centers at the capitals of districts.

<!-- b001535 | prose | pages [32] -->
And when calculating the shortest distance, we represent a district with its capital . In model 3, we build the optimization model without considering the vaccine.

<!-- b001536 | heading | pages [32] -->
Strengths

<!-- b001537 | prose | pages [32] -->
In model 1, we considered the influence of isolated people and improved our basic model through adding isolated people and drug intervention, which make the simulation more real and effective. The reasonable setting of the parameter ( ) , will bring the model the ability of self-

<!-- b001538 | prose | pages [32] -->
regulation.

<!-- b001539 | prose | pages [32] -->
In model 2, when choosing locations of medical centers, considering the drug distribution point will not change once selected, we get our result from a long-term perspective. Which will make the results more reasonable.

<!-- b001540 | prose | pages [32] -->
In model 3, we building a logistic block growth model about drug production. This model is

<!-- b001541 | furniture | pages [33] -->
Team # 35532                                                                          32 / 34

<!-- b001542 | furniture | pages [33] -->


<!-- b001543 | prose | pages [33] -->
reasonable. We consider two situations. The one is the condition of severe lacking drug, other one is the condition of relatively sufficient drug. At last we assume the disease is under control when the growth rate of infectious individuals develop into zero.

<!-- b001544 | heading | pages [33] -->
Letter for the world medical association

<!-- b001545 | prose | pages [33] -->
To the world medical association,

<!-- b001546 | furniture | pages [33] -->


<!-- b001547 | prose | pages [33] -->
Ebola has received wide attention of people all over the world since 2014, and until now, the situation of the Ebola in Africa is still not optimistic. Recently, the number of the infected people appeared an increment again. With the coming warm rainy season, we must pay attention to the development trend of Ebola disease.

<!-- b001548 | furniture | pages [33] -->


<!-- b001549 | prose | pages [33] -->
To prevent the spread of epidemic, we propose the following suggestion Based on our study:

<!-- b001550 | furniture | pages [33] -->


<!-- b001551 | prose | pages [33] -->
National measures to control the epidemic infection Build strong and effective isolation to prevent deterioration of the condition, and focus on the patient in the incubation to avoid them a new source of infection before being isolated. Provide the public with the right to preventive methods by publicity, and reduce large gatherings in the public. The government should popularize cremation, even take lethal force cremation for death for Ebola patients with known. The government should control the regional migration.

<!-- b001552 | furniture | pages [33] -->


<!-- b001553 | prose | pages [33] -->
For description of drug distribution Because the drug is in shortage, the need of each country medicines cannot be met. Therefore: Before drug production reach a certain amount, according to the different circumstances of each country and a reasonable prediction, we set a drug delivery system whose purpose is the overall controlled objectives, and the overall distribution of the situation is adjusted every two weeks. After drug production speed reach the necessary requirement .we use minimazing the number of deaths as the target for distribution. If you want to know more detailed analysis and the data, welcome to read our paper. We wish that Ebola will be controlled soon.

<!-- b001554 | furniture | pages [33] -->


<!-- b001555 | prose | pages [33] -->
Yours sincerely

<!-- b001556 | furniture | pages [33] -->


<!-- b001557 | heading | pages [33] -->
References

<!-- b001558 | references | pages [33] -->
[1] Baize S, Pannetier D, Oestereich L, et al. Emergence of Zaire Ebola virus disease in

<!-- b001559 | references | pages [33] -->
Guinea[J]. New England Journal of Medicine, 2014, 371(15): 1418-1425.

<!-- b001560 | references | pages [33] -->
World Health Organization: Ebola Virus Disease, West Africa –Update on 27.July 2014.

<!-- b001561 | references | pages [33] -->
2014.

<!-- b001562 | references | pages [33] -->
[2] Gire S K, Goba A, Andersen K G, et al. Genomic surveillance elucidates Ebola virus origin

<!-- b001563 | references | pages [33] -->
and transmission during the 2014 outbreak[J]. Science, 2014, 345(6202): 1369-1372.

<!-- b001564 | furniture | pages [34] -->
Team # 35532                                                                          33 / 34

<!-- b001565 | furniture | pages [34] -->


<!-- b001566 | references | pages [34] -->
[3] Ebola Situation Report - 4 February 2015

<!-- b001567 | references | pages [34] -->
http://apps.who.int/ebola/en/ebola-situation-report/situation-reports/ebola-situation-report-4-

<!-- b001568 | references | pages [34] -->
february-2015

<!-- b001569 | references | pages [34] -->
Chowell G, Hengartner N W, Castillo-Chavez C, et al. The basic reproductive number of

<!-- b001570 | references | pages [34] -->
Ebola and the effects of public health measures: the cases of Congo and Uganda[J]. Journal of

<!-- b001571 | references | pages [34] -->
Theoretical Biology, 2004, 229(1): 119-126.

<!-- b001572 | references | pages [34] -->
[4] Althaus C L. Estimating the reproduction number of Zaire ebolavirus (EBOV) during the

<!-- b001573 | references | pages [34] -->
2014 outbreak in West Africa[J]. arXiv preprint arXiv:1408.3505, 2014.

<!-- b001574 | references | pages [34] -->
[5] Lekone, P. E. & Finkenstadt, B. F. 2006 Statistical inference in a stochastic epidemic SEIR

<!-- b001575 | references | pages [34] -->
model with control intervention: Ebola as a case study. Biometrics 62, 1170–

<!-- b001576 | references | pages [34] -->
7.doi:10.1111/j.1541-0420.2006.00609.x.

<!-- b001577 | references | pages [34] -->
[6] Hand hygiene for health workers caring for Ebola patients

<!-- b001578 | references | pages [34] -->
http://www.who.int/entity/csr/disease/ebola/hand-hygiene/en/index.html

<!-- b001579 | references | pages [34] -->
[7] Owen S H, Daskin M S. Strategic facility location: A review[J]. European Journal of

<!-- b001580 | references | pages [34] -->
Operational Research, 1998, 111(3): 423-447.

<!-- b001581 | references | pages [34] -->
[8] Ebola Situation Report - 4 February 2015

<!-- b001582 | references | pages [34] -->
http://apps.who.int/ebola/en/ebola-situation-report/situation-reports/ebola-situation-report-4-

<!-- b001583 | references | pages [34] -->
february-2015

<!-- b001584 | references | pages [34] -->
[9] S.M. Belenson, K.C. Kapur, An algorithm for solving multicriterion linear programming

<!-- b001585 | references | pages [34] -->
problems with examples, Operational Research Quarterly 24 (1) (1973) 65–77.

<!-- b001586 | references | pages [34] -->
[10] C.L. Hwang, K. Yoon, Multiple Attribute Decision Making, Springer-Verlag, Berlin,

<!-- b001587 | references | pages [34] -->
1981.

<!-- b001588 | references | pages [34] -->
[11] introduction about ebola

<!-- b001589 | references | pages [34] -->
http://www.who.int/csr/disease/ebola/en/

<!-- b001590 | references | pages [34] -->
[12] National Education

<!-- b001591 | furniture | pages [34] -->


<!-- b001592 | references | pages [34] -->
Data.worldbank.com

<!-- b001593 | references | pages [34] -->
[13] Ebola Situation Report - 4 February 2015

<!-- b001594 | references | pages [34] -->
http://apps.who.int/ebola/en/ebola-situation-report/situation-reports/ebola-situation-

<!-- b001595 | references | pages [34] -->
report-4-february-2015

<!-- b001596 | references | pages [34] -->
[14] WHO approves Ebola trial drug

<!-- b001597 | references | pages [34] -->
http://english.cntv.cn/2014/08/13/VIDE1407889322218675.shtml

<!-- b001598 | furniture | pages [34] -->


<!-- b001599 | furniture | pages [34] -->

