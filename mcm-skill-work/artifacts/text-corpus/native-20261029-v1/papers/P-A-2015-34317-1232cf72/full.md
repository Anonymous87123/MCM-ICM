# P-A-2015-34317-1232cf72

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | title | pages [1] -->
34317

<!-- b000003 | prose | pages [1] -->
For office use only

<!-- b000004 | prose | pages [1] -->
T1 ________________

<!-- b000005 | prose | pages [1] -->
T2 ________________

<!-- b000006 | furniture | pages [1] -->


<!-- b000007 | prose | pages [1] -->
T3 ________________

<!-- b000008 | prose | pages [1] -->
For office use only

<!-- b000009 | prose | pages [1] -->
F1 ________________

<!-- b000010 | prose | pages [1] -->
F2 ________________

<!-- b000011 | prose | pages [1] -->
F3 ________________

<!-- b000012 | prose | pages [1] -->
Problem Chosen

<!-- b000013 | prose | pages [1] -->
T4 ________________

<!-- b000014 | furniture | pages [1] -->


<!-- b000015 | prose | pages [1] -->
F4 ________________

<!-- b000016 | title | pages [1] -->
A

<!-- b000017 | furniture | pages [1] -->


<!-- b000018 | furniture | pages [1] -->


<!-- b000019 | heading | pages [1] -->
Summary

<!-- b000020 | prose | pages [1] -->
“Ebola is a major global crisis that demands a massive and immediate global response. No country or

<!-- b000021 | prose | pages [1] -->
organization can defeat Ebola alone.”

<!-- b000022 | prose | pages [1] -->
—— H.E. Ban Ki-moon, the UN Secretary-General.

<!-- b000023 | prose | pages [1] -->
As a number of Global Village, we do our best to help eradicate Ebola.

<!-- b000024 | prose | pages [1] -->
First, we develop a stage-structured model of Ebola Propagation. In the model, we consider the susceptible,

<!-- b000025 | prose | pages [1] -->
the exposed, the infected whose disease is not advanced, the infected whose disease is serious, the removed and

<!-- b000026 | prose | pages [1] -->
the dead. The model is good at predicting near future cases’ number but fails in predicting far future cases’

<!-- b000027 | prose | pages [1] -->
number. Then we take hospital into consideration and add 7 more parameters, then we do simulation once again.

<!-- b000028 | prose | pages [1] -->
Finally, we get a better result that the model well predicts the future cases. For example, the model predicts there

<!-- b000029 | prose | pages [1] -->
are 4000 total cases and 2500 death cases in Guinea, 9509 total cases and 4166 death cases in Liberia, 12556

<!-- b000030 | prose | pages [1] -->
total cases and 3933 death cases in Sierra Leone up to April,1st, 2015.

<!-- b000031 | prose | pages [1] -->
Second, we determine the locations of delivery. We invoke clustering method to divide the most serious

<!-- b000032 | prose | pages [1] -->
region, namely, West Africa into three parts, Guinea, Liberia and Sierra Leone. According to locations of

<!-- b000033 | prose | pages [1] -->
provincial capital, we use clustering method once again to divide a country into several clusters. Then we adopt

<!-- b000034 | prose | pages [1] -->
P-Center Method to determine a location of delivery in each cluster. We find there are two kinds of ways to

<!-- b000035 | prose | pages [1] -->
choose. One is one-way route and the other is circular route. As for one-way route, we think it is

<!-- b000036 | prose | pages [1] -->
time-consuming and energy-consuming. So we decide to use circular route. The circular route, in some ways, is

<!-- b000037 | prose | pages [1] -->
a little bit similar to TSP problem, we use mix integer programming to find an optimal circular route by Lingo

<!-- b000038 | prose | pages [1] -->
Software and each location of delivery has two optimal circular routes. The result is that there are 3 locations of

<!-- b000039 | prose | pages [1] -->
delivery in Guinea, 1 location of delivery in Liberia and 1 location of delivery in Sierra Leone.

<!-- b000040 | prose | pages [1] -->
Third, we know from the stage-structured model that Ebola cannot stop spreading by itself. Since we are

<!-- b000041 | prose | pages [1] -->
going to eradicate Ebola, we must use medicine and vaccine to stop Ebola. Medicine mainly influences the

<!-- b000042 | prose | pages [1] -->
number of the susceptible while vaccine mainly influences the number of the infected whose disease is not

<!-- b000043 | prose | pages [1] -->
advanced, in this way, we can eradicate Ebola. As for speed of manufacturing, we consider there is a linear

<!-- b000044 | prose | pages [1] -->
equation between the speed and time because the amount of medicine is too rare to meet the requirement of

<!-- b000045 | prose | pages [1] -->
patients. And this situation continues until the requirement is met. We can calculate the speed by the parameter

<!-- b000046 | prose | pages [1] -->
in the linear equation. And we allocate medicine to different places by ratio of the infected number in that place

<!-- b000047 | prose | pages [1] -->
to the number in three West African countries. Thus, we successfully stop Ebola from spreading.

<!-- b000048 | keywords | pages [1] -->
Keywords:  SEIIRF Model   TSP Model   Clustering Method    Ebola Evaluating

<!-- b000049 | furniture | pages [2] -->


<!-- b000050 | prose | pages [2] -->
A BATTLE WITHOUT GUN AND SMOKE

<!-- b000051 | prose | pages [2] -->
———— THE CONFRONTATION WITH EBOLA

<!-- b000052 | prose | pages [2] -->
Content

<!-- b000053 | prose | pages [2] -->
Ⅰ Introduction ............................................................................................................. 1

<!-- b000054 | prose | pages [2] -->
1.1 Aims are Changing now .................................................................................. 1

<!-- b000055 | prose | pages [2] -->
1.2 Our Understanding of the Words .................................................................... 1

<!-- b000056 | prose | pages [2] -->
1.3 Decompose the Problem and Our Tasks ......................................................... 2

<!-- b000057 | prose | pages [2] -->
Ⅱ Background – Behavior Change is Key to the Eradication of Ebola ...................... 3

<!-- b000058 | prose | pages [2] -->
Ⅲ Assumptions And Justifications .............................................................................. 4

<!-- b000059 | prose | pages [2] -->
Ⅳ SEIIRF Model for Ebola propagation ..................................................................... 4

<!-- b000060 | prose | pages [2] -->
4.1 Introduction ..................................................................................................... 4

<!-- b000061 | prose | pages [2] -->
4.2 Symbols and Definitions ................................................................................. 5

<!-- b000062 | prose | pages [2] -->
4.3 Construction of the Model .............................................................................. 6

<!-- b000063 | prose | pages [2] -->
4.4 Results are Not So Reasonable ....................................................................... 8

<!-- b000064 | prose | pages [2] -->
4.5 Refresh the Values of Parameters.................................................................... 8

<!-- b000065 | prose | pages [2] -->
4.6 Advanced Model ........................................................................................... 10

<!-- b000066 | prose | pages [2] -->
4.7 Results are Reasonable ................................................................................. 13

<!-- b000067 | prose | pages [2] -->
4.8 Prediction of the Future ................................................................................ 14

<!-- b000068 | prose | pages [2] -->
Ⅴ Model of Locations of Delivery ............................................................................ 18

<!-- b000069 | prose | pages [2] -->
5.1 What is Emergency Supplies ........................................................................ 18

<!-- b000070 | prose | pages [2] -->
5.2 Assumptions and Justifications ..................................................................... 19

<!-- b000071 | prose | pages [2] -->
5.3 Clustering Method, A Way to Determine Regions for Medicine Delivery ... 20

<!-- b000072 | prose | pages [2] -->
5.4 Results of Clustering Method ....................................................................... 21

<!-- b000073 | prose | pages [2] -->
5.5 Principle of Fairness ..................................................................................... 22

<!-- b000074 | prose | pages [2] -->
5.6 Principle of Efficiency .................................................................................. 22

<!-- b000075 | prose | pages [2] -->
5.7 Determine Delivery Locations in the Three West African Countries ........... 23

<!-- b000076 | prose | pages [2] -->
Ⅵ Model of Delivery System .................................................................................... 23

<!-- b000077 | furniture | pages [3] -->


<!-- b000078 | prose | pages [3] -->
6.1 Introduction ................................................................................................... 23

<!-- b000079 | prose | pages [3] -->
6.2 Symbols and Definitions ............................................................................... 24

<!-- b000080 | prose | pages [3] -->
6.3 TSP Model – Well-Planned Routes ............................................................... 24

<!-- b000081 | prose | pages [3] -->
6.4 Daily Demand for Medicine ......................................................................... 25

<!-- b000082 | prose | pages [3] -->
Ⅶ Model Implementation of three Countries ............................................................ 26

<!-- b000083 | prose | pages [3] -->
7.1General algorithm .......................................................................................... 26

<!-- b000084 | prose | pages [3] -->
7.2 Application of Algorithm .............................................................................. 27

<!-- b000085 | prose | pages [3] -->
7.2.1 Application in Guinea ........................................................................ 27

<!-- b000086 | prose | pages [3] -->
7.2.2 Application in Liberia ........................................................................ 29

<!-- b000087 | prose | pages [3] -->
7.2.3 Sierra Leone ....................................................................................... 30

<!-- b000088 | prose | pages [3] -->
Ⅷ Model of the Quantity of the Medicine Needed and Manufacturing Speed ......... 31

<!-- b000089 | prose | pages [3] -->
8.1 Introduction ................................................................................................... 31

<!-- b000090 | prose | pages [3] -->
8.2 Assumptions and Justifications ..................................................................... 32

<!-- b000091 | prose | pages [3] -->
8.3 symbols and definitions ................................................................................ 32

<!-- b000092 | prose | pages [3] -->
8.4 How Fast Need We Produce Medicine and Vaccine ..................................... 32

<!-- b000093 | prose | pages [3] -->
8.5 The Quantity of the Medicine Needed .......................................................... 35

<!-- b000094 | prose | pages [3] -->
Ⅸ Other Factors We Think Are Important ................................................................ 35

<!-- b000095 | prose | pages [3] -->
Ⅹ Extension of Models ............................................................................................. 36

<!-- b000096 | prose | pages [3] -->
10.1 Optimization of Coverage to Determine Delivery Locations ..................... 36

<!-- b000097 | prose | pages [3] -->
10.2 A No-boundary Scheme .............................................................................. 37

<!-- b000098 | prose | pages [3] -->
Ⅺ Sensitivity analysis................................................................................................ 38

<!-- b000099 | prose | pages [3] -->
11.1 Sensitivity Analysis of SEIIRF Model ........................................................ 38

<!-- b000100 | prose | pages [3] -->
11.2 Sensitivity Analysis of Model of the Speed to Produce Medicine .............. 39

<!-- b000101 | prose | pages [3] -->
Ⅻ Conclusion ............................................................................................................ 40

<!-- b000102 | prose | pages [3] -->
11.1 Strengths and Weaknesses ........................................................................... 40

<!-- b000103 | prose | pages [3] -->
11.2 Overall Results ............................................................................................ 41

<!-- b000104 | furniture | pages [3] -->


<!-- b000105 | furniture | pages [3] -->


<!-- b000106 | furniture | pages [4] -->
Team # 34317                                                                Page 1 of 44

<!-- b000107 | heading | pages [4] -->
Ⅰ Introduction

<!-- b000108 | prose | pages [4] -->
Ebola, a familiar but strange word to us. When the Ebola virus out broke in West Africa and caused plenty of deaths, no one would imagine the disastrous scene without mercy. And, of course, no one believes the word ‘Ebola’ just originated from a peaceful and beautiful river – Ebola River in Congo. Contrary to its attracting meaning, it is true that the Ebola virus do take lots of victims’ lives away. Countries all over the world, thus, have taken strategies, more specifically, distribute health works to disease-torn countries, speed up the development of medicine and establish feasible delivery systems to contain Ebola propagation.

<!-- b000109 | heading | pages [4] -->
1.1 Aims are changing now

<!-- b000110 | prose | pages [4] -->
The battle against Ebola will cost us heavily for sure, but human beings are not easily defeated. Although Ebola virus is fatal, we have methods. The WMA (World Medical Association) has announced that they have developed medicine to cure Ebola. At one level, the medicine is a milestone for us human beings in fighting Ebola, but at another it is the result of human nature. We know calling the command center to take away the sick is equally hard. It is our duty, in the interests of our own and the public good, to pick up the phone, but the reality is that, if we do, we may never hug our sister again. We can visit her in the treatment center and talk across two fences. The fortunate will be reunited. For the rest, the future is the body bag.[1] Ebola will not end without the medicine. Thanks to appearance of the medicine, we are gradually going out of confusion and turning to fight back in this smokeless battle. Many previous articles that mainly focus on how Ebola propagation or how difficult to contain Ebola are now may less important than those on how to effectively delivery medicine to most-need regions like West Africa. Accurate location with effective medicine – Ebola’s doomsday and we do our job to make it come true – considering propagation process, medicine needed, delivery systems, locations of delivery and manufacturing speed of vaccine or drug and so on.

<!-- b000111 | heading | pages [4] -->
1.2 Our understanding of the words

<!-- b000112 | prose | pages [4] -->
The problem requires us to de several jobs to evaluate Ebola. We think it is necessary for us to come to an understanding of some words in the problem.

<!-- b000113 | prose | pages [4] -->
Spread of the Disease: We consider this sub-problem as a requirement to analyze Ebola propagation process and predict future cases, including total cases and death cases in the three West African countries and what influence that new medicine will bring to us. As for Ebola cases in other countries, such as in the United States or in The United Kingdom, good health condition and developed facilities can contain the cases well, so in this paper, we mainly discuss Ebola cases in West Africa.

<!-- b000114 | furniture | pages [5] -->
Team # 34317                                                                Page 2 of 44

<!-- b000115 | prose | pages [5] -->
Locations of Delivery: How to understand the word ‘locations’ is the key to this sub-problem. We also have some criteria to choose ‘locations’ – easy to deliver medicine, cover most people or environment-friendly to build? Here, we regard ‘locations’ as places that have features of easy and time-saving in medicine delivering, being equal to all people in a region.

<!-- b000116 | prose | pages [5] -->
Possible Feasible Delivery Systems: We think this sub-problem needs us to design a route that can not only cover all places which are in need of medicine but also provide vehicles a fastest way to send medicine. Besides, delivery systems can allocate medicine to different places properly.

<!-- b000117 | prose | pages [5] -->
The Quantity of the Medicine Needed: There are several understandings of the word ‘quantity’, like amount of medicine to cure all Ebola patients or amount of medicine needed every day to keep serious patients from dying. Our understanding of this word is the total amount of medicine needed to cure patients whose disease is not advanced until there is no more patients appear. So it is a dynamic and time-varying number until cases stops increasing.

<!-- b000118 | prose | pages [5] -->
Speed of manufacturing of the vaccine or medicine: In our opinion, this sub-problem needs us to decide how fast a factory have to produce medicine when amount of medicine is too rare to cure patients and what changes a factory should obey when there is enough medicine for patients. As for vaccine, we consider it is similar to medicine.

<!-- b000119 | prose | pages [5] -->
Other factors: Something we forget to consider in our model but also important for Ebola evaluating. We will find them during the process of establishing models

<!-- b000120 | heading | pages [5] -->
1.3 Decompose the Problem and Our Tasks

<!-- b000121 | prose | pages [5] -->
To totally understand the problem better and know what we should to deal with Ebola, decompose it is needed to us. According to the steps needed in process of achieving our goal that accurate location with effective medicine, we deem the problem ‘Eradicating Ebola’ can be divided into five parts:

<!-- b000122 | prose | pages [5] -->
Propagation mechanism of Ebola virus.

<!-- b000123 | prose | pages [5] -->
Accurate locations for medicine to be delivered like disease-torn countries in

<!-- b000124 | prose | pages [5] -->
West Africa.

<!-- b000125 | prose | pages [5] -->
Effective transportation including amount of medicine needed in a place.

<!-- b000126 | prose | pages [5] -->
Total amount of medicine needed to cure Ebola patients until cases stops

<!-- b000127 | prose | pages [5] -->
increasing.

<!-- b000128 | furniture | pages [6] -->
Team # 34317                                                                Page 3 of 44

<!-- b000129 | prose | pages [6] -->
Vaccine or drug manufacturing speed

<!-- b000130 | prose | pages [6] -->
When the problem is unequivocal, we start to make it clear that what we need to do and how to do it. Since we have separated the problem into parts, we can deal with these parts one by one. Here the problem requires us do and our tasks are:

<!-- b000131 | prose | pages [6] -->
 Build a model to reflect the condition we face now and make prediction of the

<!-- b000132 | prose | pages [6] -->
future if medicine or hospital or other factors play roles in Ebola propagation process.

<!-- b000133 | prose | pages [6] -->
 Find some best delivery places according to our own understanding of word

<!-- b000134 | prose | pages [6] -->
‘locations’

<!-- b000135 | prose | pages [6] -->
 Design a delivery system both good in medicine transportation and medicine

<!-- b000136 | prose | pages [6] -->
allocation.

<!-- b000137 | prose | pages [6] -->
 Speed to produce medicine and total quantity needed to eradicate Ebola

<!-- b000138 | prose | pages [6] -->
 Other critical factors we consider important to optimize the eradication of Ebola

<!-- b000139 | prose | pages [6] -->
Ⅱ Background – Behavior Change is Key to the

<!-- b000140 | prose | pages [6] -->
Eradication of Ebola

<!-- b000141 | prose | pages [6] -->
As the number of Ebola cases and deaths grows in West Africa, many remain unaware of its deadly impact, causes and treatment options, or lack thereof. Let people know the harm of the diseases is of great importance both in the developing world and, more specifically, on the African continent.

<!-- b000142 | prose | pages [6] -->
Unfortunately, in remote districts of these three African countries – Guinea, Liberia and Sierra Leone few of the local have heard Google or ABC News or other TV media and say nothing of getting access of the newest Ebola news. Once the people who are seeing their family members get sick and die tend to believe an invisible killer who are from hell. Getting correct information about Ebola prevention and treatment to local communities throughout West Africa must become a higher priority, and we must begin to address it in culturally appropriate and innovative ways.[2]

<!-- b000143 | prose | pages [6] -->
Besides, human nature is another factor of Ebola spreading unimpededly, though great efforts have been made to find and quarantine Ebola patients. Like we introduced in Instruction, although talk of changing behavior is easy, when we think about the sort of behavior that needs to change, we realize it’s very hard. How many

<!-- b000144 | furniture | pages [7] -->
Team # 34317                                                                Page 4 of 44

<!-- b000145 | prose | pages [7] -->
of us could bear to watch our mother die without holding her hand, and then allow her body to be sprayed with chlorine, removed in a double body bag from the house, be loaded on to the back of a pick-up truck with several others, and taken to the cemetery for rapid interment with little more than a cursory prayer?[1]

<!-- b000146 | prose | pages [7] -->
We must have to realize that change awareness and human nature is quite hard. The most effective way is to find medicine if we want to win the battle against Ebola. Here is the time for medicine cure – the WMA have announced that they could.

<!-- b000147 | heading | pages [7] -->
Ⅲ Assumptions And Justifications

<!-- b000148 | prose | pages [7] -->
①Overlook the changing of population caused by natural birth rate and death

<!-- b000149 | prose | pages [7] -->
rate.

<!-- b000150 | prose | pages [7] -->
Compared to the influence of Ebola to the population, natural birth rate and death rate

<!-- b000151 | prose | pages [7] -->
have little impact. Also, the total natural growth of number of population is not large

<!-- b000152 | prose | pages [7] -->
in the period of the spread.

<!-- b000153 | prose | pages [7] -->
②There is no population flow among areas.

<!-- b000154 | prose | pages [7] -->
Since the outbreak of Ebola, the immigration among different districts and countries

<!-- b000155 | prose | pages [7] -->
play a role can be ignored in terms of the change of the population. In addition, the

<!-- b000156 | prose | pages [7] -->
flow rate of people may decrease in case of the infection of disease.

<!-- b000157 | prose | pages [7] -->
We list more and detailed assumptions in the following section when using them.

<!-- b000158 | heading | pages [7] -->
Ⅳ SEIIRF model for Ebola propagation

<!-- b000159 | heading | pages [7] -->
4.1 Introduction

<!-- b000160 | prose | pages [7] -->
The ongoing Ebola outbreak surprises us both in size and complexity. At the very beginning of 2015, many scientists and other people, like us students, are still fighting against Ebola in different ways, such as developing medicine, propagating health care and predicting the spread of Ebola. In this section, we apply SEIIRF Model to evaluate the spread of Ebola. Thanks to a previous article [5], we can use this model appropriately, however, as time goes by, values of parameters stated in that article

<!-- b000161 | furniture | pages [8] -->
Team # 34317                                                                Page 5 of 44

<!-- b000162 | prose | pages [8] -->
may not convinced enough anymore for that article just used data from October,2014 to November, 2014 to calculate values of parameters and then tested the model with data in December, 2014. If we still use the values of parameters in that article, we find it is far from accuracy of data in January, 2015. So we find a method – Genetic Algorithm to refresh the value of parameters by using data from October, 2014 to December, 2014 and the renewed SEIIRF Model well fits the data of January 1st, 2015 to February 3rd, 2015.

<!-- b000163 | heading | pages [8] -->
4.2 Symbols and Definitions

<!-- b000164 | prose | pages [8] -->
There are some symbols appear in the model. We show them below:

<!-- b000165 | caption | pages [8] -->
table4.1: symbols in the model

<!-- b000166 | heading | pages [8] -->
SYMBOL

<!-- b000167 | prose | pages [8] -->
DEFINITION UNITS

<!-- b000168 | prose | pages [8] -->
Transmission Parameter For First Stage Of Illness (Not  1

<!-- b000169 | prose | pages [8] -->
In Hospital)

<!-- b000170 | prose | pages [8] -->


<!-- b000171 | prose | pages [8] -->
-1 -1 people days

<!-- b000172 | prose | pages [8] -->
Ratio Of Infectiveness In First Vs. Second Of Stage Of

<!-- b000173 | prose | pages [8] -->
2

<!-- b000174 | furniture | pages [8] -->


<!-- b000175 | prose | pages [8] -->


<!-- b000176 | prose | pages [8] -->
Unitless

<!-- b000177 | prose | pages [8] -->
Illness (Not In Hospital)

<!-- b000178 | prose | pages [8] -->
1

<!-- b000179 | prose | pages [8] -->


<!-- b000180 | prose | pages [8] -->
Ratio Of Infectiveness In First

<!-- b000181 | prose | pages [8] -->
F

<!-- b000182 | furniture | pages [8] -->


<!-- b000183 | prose | pages [8] -->


<!-- b000184 | prose | pages [8] -->
Unitless

<!-- b000185 | prose | pages [8] -->
Stage Vs. Funeral Transmission (Not In Hospital)

<!-- b000186 | prose | pages [8] -->
1

<!-- b000187 | prose | pages [8] -->
 1 Average Incubation Period

<!-- b000188 | prose | pages [8] -->
1 1

<!-- b000189 | prose | pages [8] -->
Days

<!-- b000190 | prose | pages [8] -->
Length Of First Stage Of Illness (Not In Hospital)

<!-- b000191 | prose | pages [8] -->
 1

<!-- b000192 | prose | pages [8] -->
Days

<!-- b000193 | prose | pages [8] -->
Length Of Second Stage Of Illness (Not In Hospital) 2

<!-- b000194 | prose | pages [8] -->
  1

<!-- b000195 | prose | pages [8] -->
Days

<!-- b000196 | prose | pages [8] -->
Time From Death Until Burial F

<!-- b000197 | prose | pages [8] -->


<!-- b000198 | prose | pages [8] -->
Days

<!-- b000199 | prose | pages [8] -->
Overall Mortality Rate (Fraction) (Not In Hospital) 1 2 Unitless

<!-- b000200 | prose | pages [8] -->
Mortality Rate (Fraction) Among Those In Second  2

<!-- b000201 | prose | pages [8] -->
Unitless

<!-- b000202 | prose | pages [8] -->
Stage Of Illness (Not In Hospital)

<!-- b000203 | furniture | pages [9] -->
Team # 34317                                                                Page 6 of 44

<!-- b000204 | heading | pages [9] -->
4.3 Construction of the Model

<!-- b000205 | prose | pages [9] -->
To adequately reflect the propagation of Ebola and transmission of Ebola, we should take real conditions in life into consideration.

<!-- b000206 | prose | pages [9] -->
To begin with, we show our model as a form of figure.

<!-- b000207 | prose | pages [9] -->
S E I1 I2 F

<!-- b000208 | prose | pages [9] -->
R

<!-- b000209 | furniture | pages [9] -->


<!-- b000210 | caption | pages [9] -->
figure 4.1: Stage-Structured Model of Ebola propagation

<!-- b000211 | prose | pages [9] -->
We can get information from the figure 4.1. There are six stages in the whole propagation of Ebola. We also call this model as Stage-Structured Model,

<!-- b000212 | furniture | pages [9] -->


<!-- b000213 | prose | pages [9] -->
S represents the fraction of the population which is susceptible.

<!-- b000214 | furniture | pages [9] -->


<!-- b000215 | prose | pages [9] -->
E represents the fraction of the population which is exposed.

<!-- b000216 | furniture | pages [9] -->


<!-- b000217 | prose | pages [9] -->
1I represents the fraction of the population which is infected and remain in first

<!-- b000218 | prose | pages [9] -->
stage (such as fever, headache, sore throat, muscle aches and other milder symptoms which often progress to diarrhea and vomiting).

<!-- b000219 | furniture | pages [9] -->


<!-- b000220 | prose | pages [9] -->
2I represents the fraction of the population which is infected and deteriorate to

<!-- b000221 | prose | pages [9] -->
second stage (such as hemorrhaging and multi-organ failure).

<!-- b000222 | furniture | pages [9] -->


<!-- b000223 | prose | pages [9] -->
R represents the fraction of the population which is recovered. And

<!-- b000224 | furniture | pages [9] -->


<!-- b000225 | prose | pages [9] -->
F represents the fraction of the population who have died and are in the process of being buried.

<!-- b000226 | furniture | pages [9] -->


<!-- b000227 | furniture | pages [9] -->


<!-- b000228 | furniture | pages [9] -->


<!-- b000229 | furniture | pages [9] -->


<!-- b000230 | furniture | pages [10] -->
Team # 34317                                                                Page 7 of 44

<!-- b000231 | prose | pages [10] -->
The corresponding equations of Figure 4.1 are

<!-- b000232 | prose | pages [10] -->


<!-- b000233 | prose | pages [10] -->
dS

<!-- b000234 | prose | pages [10] -->


<!-- b000235 | prose | pages [10] -->


<!-- b000236 | prose | pages [10] -->


<!-- b000237 | prose | pages [10] -->
(

<!-- b000238 | prose | pages [10] -->
I

<!-- b000239 | prose | pages [10] -->


<!-- b000240 | prose | pages [10] -->
I

<!-- b000241 | prose | pages [10] -->
1

<!-- b000242 | prose | pages [10] -->
dt

<!-- b000243 | prose | pages [10] -->


<!-- b000244 | prose | pages [10] -->
dE

<!-- b000245 | prose | pages [10] -->
 

<!-- b000246 | prose | pages [10] -->


<!-- b000247 | prose | pages [10] -->


<!-- b000248 | prose | pages [10] -->


<!-- b000249 | prose | pages [10] -->
(

<!-- b000250 | prose | pages [10] -->
I

<!-- b000251 | prose | pages [10] -->


<!-- b000252 | prose | pages [10] -->
I

<!-- b000253 | prose | pages [10] -->
1

<!-- b000254 | prose | pages [10] -->
dt

<!-- b000255 | prose | pages [10] -->


<!-- b000256 | prose | pages [10] -->
dI

<!-- b000257 | prose | pages [10] -->
 

<!-- b000258 | prose | pages [10] -->


<!-- b000259 | prose | pages [10] -->


<!-- b000260 | prose | pages [10] -->


<!-- b000261 | prose | pages [10] -->
E I

<!-- b000262 | prose | pages [10] -->
1

<!-- b000263 | prose | pages [10] -->


<!-- b000264 | prose | pages [10] -->
1 1

<!-- b000265 | prose | pages [10] -->
dt dI

<!-- b000266 | prose | pages [10] -->
 

<!-- b000267 | prose | pages [10] -->


<!-- b000268 | prose | pages [10] -->


<!-- b000269 | prose | pages [10] -->


<!-- b000270 | prose | pages [10] -->
I

<!-- b000271 | prose | pages [10] -->
2

<!-- b000272 | prose | pages [10] -->


<!-- b000273 | prose | pages [10] -->
1 1 1

<!-- b000274 | prose | pages [10] -->
dt

<!-- b000275 | prose | pages [10] -->


<!-- b000276 | prose | pages [10] -->
dF

<!-- b000277 | prose | pages [10] -->
 

<!-- b000278 | prose | pages [10] -->


<!-- b000279 | prose | pages [10] -->


<!-- b000280 | prose | pages [10] -->
I

<!-- b000281 | prose | pages [10] -->
2 2 2

<!-- b000282 | prose | pages [10] -->


<!-- b000283 | prose | pages [10] -->
dt

<!-- b000284 | prose | pages [10] -->


<!-- b000285 | prose | pages [10] -->
dR

<!-- b000286 | prose | pages [10] -->
 

<!-- b000287 | prose | pages [10] -->


<!-- b000288 | prose | pages [10] -->


<!-- b000289 | prose | pages [10] -->
(1 )

<!-- b000290 | prose | pages [10] -->
1 1 1

<!-- b000291 | prose | pages [10] -->
dt

<!-- b000292 | prose | pages [10] -->
 

<!-- b000293 | prose | pages [10] -->


<!-- b000294 | prose | pages [10] -->


<!-- b000295 | prose | pages [10] -->
I F S

<!-- b000296 | prose | pages [10] -->
)

<!-- b000297 | prose | pages [10] -->
2 2 2

<!-- b000298 | prose | pages [10] -->
F

<!-- b000299 | prose | pages [10] -->


<!-- b000300 | prose | pages [10] -->


<!-- b000301 | prose | pages [10] -->


<!-- b000302 | prose | pages [10] -->


<!-- b000303 | prose | pages [10] -->
I I F S

<!-- b000304 | prose | pages [10] -->
)

<!-- b000305 | prose | pages [10] -->
E

<!-- b000306 | prose | pages [10] -->
2 2 2

<!-- b000307 | prose | pages [10] -->
F

<!-- b000308 | furniture | pages [10] -->


<!-- b000309 | prose | pages [10] -->
I I

<!-- b000310 | prose | pages [10] -->
2 2 2

<!-- b000311 | prose | pages [10] -->
 

<!-- b000312 | prose | pages [10] -->
F

<!-- b000313 | prose | pages [10] -->
F F

<!-- b000314 | prose | pages [10] -->
 

<!-- b000315 | prose | pages [10] -->


<!-- b000316 | prose | pages [10] -->
I I

<!-- b000317 | prose | pages [10] -->
(1 )

<!-- b000318 | prose | pages [10] -->
I

<!-- b000319 | prose | pages [10] -->
2 2 2

<!-- b000320 | prose | pages [10] -->
In the equations we consider the infected ( 1I and 2I ) and the dead ( F ) all have

<!-- b000321 | prose | pages [10] -->
ability to infect the susceptible. In fact, when our relatives get sick, we still contact with the in daily life, and it is not surprise for us to think that human nature play an important role in Ebola propagation – just as we have talked in introduction. How many of us could bear to watch our mother die without holding her hand, and then allow her body to be sprayed with chlorine, removed in a double body bag from the house, be loaded on to the back of a pick-up truck with several others, and taken to the cemetery for rapid interment with little more than a cursory prayer? Moreover, the

<!-- b000322 | prose | pages [10] -->
     ( I I F S ) exposed E are mainly form the susceptible and then have I 1 2 2 F

<!-- b000323 | prose | pages [10] -->
 chances to turn to first stage if they show symptoms ( ). And number of people in E

<!-- b000324 | prose | pages [10] -->
  1I are mainly from the exposed ( first stage

<!-- b000325 | prose | pages [10] -->
to second stage and the rest of them

<!-- b000326 | prose | pages [10] -->
) and then part of them ( ) turn 1 1 1I E

<!-- b000327 | prose | pages [10] -->
  (1 (1 ) I get recovered. Thus number of 1 1 1

<!-- b000328 | prose | pages [10] -->
 1 1 1I people in second stage are mainly from first stage (

<!-- b000329 | prose | pages [10] -->


<!-- b000330 | prose | pages [10] -->
) and some of them die. So

<!-- b000331 | prose | pages [10] -->
 ) in second stage and their bodies ( the dead is the result of people ( 2 2I 2

<!-- b000332 | prose | pages [10] -->
until being buried.

<!-- b000333 | prose | pages [10] -->
) exist FF

<!-- b000334 | prose | pages [10] -->
Then, to measure the total cases and death cases of Ebola, We invoke

<!-- b000335 | prose | pages [10] -->
t

<!-- b000336 | prose | pages [10] -->


<!-- b000337 | prose | pages [10] -->


<!-- b000338 | prose | pages [10] -->


<!-- b000339 | prose | pages [10] -->
y

<!-- b000340 | prose | pages [10] -->
C

<!-- b000341 | prose | pages [10] -->
0

<!-- b000342 | prose | pages [10] -->
t

<!-- b000343 | prose | pages [10] -->


<!-- b000344 | prose | pages [10] -->
E E

<!-- b000345 | prose | pages [10] -->
(t)

<!-- b000346 | prose | pages [10] -->
dt

<!-- b000347 | furniture | pages [10] -->


<!-- b000348 | prose | pages [10] -->


<!-- b000349 | prose | pages [10] -->


<!-- b000350 | prose | pages [10] -->
y

<!-- b000351 | prose | pages [10] -->
D

<!-- b000352 | prose | pages [10] -->
0

<!-- b000353 | prose | pages [10] -->
I

<!-- b000354 | prose | pages [10] -->
(t)

<!-- b000355 | prose | pages [10] -->
dt

<!-- b000356 | prose | pages [10] -->
2 2 2 2

<!-- b000357 | furniture | pages [11] -->
Team # 34317                                                                Page 8 of 44

<!-- b000358 | prose | pages [11] -->
y means total cases (or cumulate cases) and In these equations, C

<!-- b000359 | prose | pages [11] -->


<!-- b000360 | prose | pages [11] -->
y means D

<!-- b000361 | prose | pages [11] -->
means number of people begin to get sick and have death cases. And E (t)

<!-- b000362 | prose | pages [11] -->
symptoms so y is the time integral of C

<!-- b000363 | prose | pages [11] -->
who no longer in second stage anymore,

<!-- b000364 | prose | pages [11] -->
 y is the time integral of . 2 2(t) I D 2

<!-- b000365 | heading | pages [11] -->
4.4 Results are Not So Reasonable

<!-- b000366 | prose | pages [11] -->
  . While is number of people 2 2(t) I E (t)

<!-- b000367 | prose | pages [11] -->
 means number of dead people. So 2 2(t) I 2 2

<!-- b000368 | prose | pages [11] -->
The article[5] adopts Least Square Method to figure out values of parameters. Unfortunately, under the values of parameters, although the calculated curve fits quite well to real data in Guinea from October 1st, 2014 to December 31st, 2014, we fail to fit the calculated curve well to real data in Guinea when time reaches on January 1st, 2015, namely, the values of parameters in that article may ‘outdated’. So we do not show them here because they are not worthy enough.

<!-- b000369 | prose | pages [11] -->
So, we adopt genetic algorithm combined with least square method to calculate our new values of parameters.

<!-- b000370 | heading | pages [11] -->
4.5 Refresh the Values of Parameters

<!-- b000371 | prose | pages [11] -->
Genetic algorithm combined with least square method is used by us to find out new parameters values. Here flow diagram of Genetic algorithm is

<!-- b000372 | furniture | pages [11] -->


<!-- b000373 | furniture | pages [11] -->


<!-- b000374 | furniture | pages [11] -->


<!-- b000375 | furniture | pages [11] -->


<!-- b000376 | furniture | pages [11] -->


<!-- b000377 | furniture | pages [11] -->


<!-- b000378 | furniture | pages [11] -->


<!-- b000379 | furniture | pages [11] -->


<!-- b000380 | furniture | pages [11] -->


<!-- b000381 | furniture | pages [11] -->


<!-- b000382 | furniture | pages [11] -->


<!-- b000383 | furniture | pages [11] -->


<!-- b000384 | furniture | pages [11] -->


<!-- b000385 | furniture | pages [12] -->
Team # 34317                                                                Page 9 of 44

<!-- b000386 | furniture | pages [12] -->


<!-- b000387 | furniture | pages [12] -->


<!-- b000388 | prose | pages [12] -->
START

<!-- b000389 | furniture | pages [12] -->


<!-- b000390 | furniture | pages [12] -->


<!-- b000391 | furniture | pages [12] -->


<!-- b000392 | furniture | pages [12] -->


<!-- b000393 | prose | pages [12] -->
 PARAMETER INITIALIZATION

<!-- b000394 | furniture | pages [12] -->


<!-- b000395 | prose | pages [12] -->
X X

<!-- b000396 | furniture | pages [12] -->


<!-- b000397 | furniture | pages [12] -->


<!-- b000398 | prose | pages [12] -->
0

<!-- b000399 | furniture | pages [12] -->


<!-- b000400 | furniture | pages [12] -->


<!-- b000401 | furniture | pages [12] -->


<!-- b000402 | furniture | pages [12] -->


<!-- b000403 | prose | pages [12] -->
 CALCULATE FITNESS

<!-- b000404 | furniture | pages [12] -->


<!-- b000405 | prose | pages [12] -->
f F (X)

<!-- b000406 | furniture | pages [12] -->


<!-- b000407 | furniture | pages [12] -->


<!-- b000408 | furniture | pages [12] -->


<!-- b000409 | furniture | pages [12] -->


<!-- b000410 | prose | pages [12] -->
GENETIC

<!-- b000411 | furniture | pages [12] -->


<!-- b000412 | furniture | pages [12] -->


<!-- b000413 | furniture | pages [12] -->


<!-- b000414 | furniture | pages [12] -->


<!-- b000415 | furniture | pages [12] -->


<!-- b000416 | furniture | pages [12] -->


<!-- b000417 | prose | pages [12] -->
N>Nf

<!-- b000418 | furniture | pages [12] -->


<!-- b000419 | furniture | pages [12] -->


<!-- b000420 | furniture | pages [12] -->


<!-- b000421 | furniture | pages [12] -->


<!-- b000422 | furniture | pages [12] -->


<!-- b000423 | furniture | pages [12] -->


<!-- b000424 | prose | pages [12] -->
OUTPUT OPTIMAL

<!-- b000425 | furniture | pages [12] -->


<!-- b000426 | furniture | pages [12] -->


<!-- b000427 | furniture | pages [12] -->


<!-- b000428 | furniture | pages [12] -->


<!-- b000429 | prose | pages [12] -->
END

<!-- b000430 | furniture | pages [12] -->


<!-- b000431 | furniture | pages [12] -->


<!-- b000432 | caption | pages [12] -->
figure4.2: flow chart of Genetic Algorithm combined with least square method

<!-- b000433 | prose | pages [12] -->
 X In the flow diagram, de define

<!-- b000434 | prose | pages [12] -->
     

<!-- b000435 | prose | pages [12] -->
fitness

<!-- b000436 | prose | pages [12] -->
f F

<!-- b000437 | prose | pages [12] -->
(X) [

<!-- b000438 | prose | pages [12] -->
y

<!-- b000439 | prose | pages [12] -->
( )

<!-- b000440 | prose | pages [12] -->
t C t

<!-- b000441 | prose | pages [12] -->
( )]

<!-- b000442 | prose | pages [12] -->
C

<!-- b000443 | prose | pages [12] -->
0

<!-- b000444 | prose | pages [12] -->
 

<!-- b000445 | prose | pages [12] -->
t t t t c

<!-- b000446 | prose | pages [12] -->
        , / , / , , , , , , and 1 2 1 F 1 1 2 F 1 2 2

<!-- b000447 | prose | pages [12] -->
 ct is length of . Where

<!-- b000448 | prose | pages [12] -->
[ [

<!-- b000449 | prose | pages [12] -->
y

<!-- b000450 | prose | pages [12] -->
( )

<!-- b000451 | prose | pages [12] -->
t D t

<!-- b000452 | prose | pages [12] -->
( )]

<!-- b000453 | prose | pages [12] -->
D

<!-- b000454 | prose | pages [12] -->
0

<!-- b000455 | prose | pages [12] -->
c c

<!-- b000456 | prose | pages [12] -->
time from October 1st, 2014 to December 31st, 2014. And C t denotes real total 0( )

<!-- b000457 | prose | pages [12] -->
D t denotes real 0( ) ct while cases in a country updated every day within time length

<!-- b000458 | prose | pages [12] -->
ct . death cases in a country updated every day within time length

<!-- b000459 | prose | pages [12] -->
By now, we have method to find each parameter’s value by using data from

<!-- b000460 | furniture | pages [13] -->
Team # 34317                                                                Page 10 of 44

<!-- b000461 | prose | pages [13] -->
October, 2014 to December, 2014. Then we use these new values to calculate a curve to fit real data in Guinea.

<!-- b000462 | prose | pages [13] -->
Here the results are:

<!-- b000463 | furniture | pages [13] -->


<!-- b000464 | caption | pages [13] -->
figure4.3: test of the calculated curves

<!-- b000465 | furniture | pages [13] -->


<!-- b000466 | prose | pages [13] -->
We can see from the figures 4.3 that in about first 90 days, namely, date from Oct.1st, 2014 to Dec.31st, 2014, the model fits well to the real data of Guinea from

<!-- b000467 | prose | pages [13] -->
WHO website. Both y and y reflect accurate number of cases, respectively. C D

<!-- b000468 | prose | pages [13] -->
However, as New Year begins, real data has tendency of becoming less rapidly increasing while our prediction is out of accuracy although our curve is much better than that calculated in the article we refer to. We do not use this curve to predict cases in Liberia and Sierra Leone.

<!-- b000469 | heading | pages [13] -->
4.6 Advanced Model

<!-- b000470 | prose | pages [13] -->
After refreshing the values of parameters, we are still not satisfied with the curve we calculate. Data talks, we should try our best to make our model considerable. To improve the model we discussed in former section, we not only use more data from WHO website to calculate our parameters, but also consider other factors impact on Ebola spreading, like additional parameters and changing of parameters’ values if people receive treatment or get infected in hospital. There is a pie chart showing the proportion of getting infected in different ways (data of Sierra Leone).

<!-- b000471 | furniture | pages [14] -->
Team # 34317                                                                Page 11 of 44

<!-- b000472 | furniture | pages [14] -->


<!-- b000473 | caption | pages [14] -->
figure4.4: pie chart proportion of getting infected in different ways

<!-- b000474 | prose | pages [14] -->
There are 17.6% of healthy people in Sierra Leone get Ebola because of hospital. it is a factor important enough for us to take it into consideration when we evaluate Ebola propagation.

<!-- b000475 | prose | pages [14] -->
First, let us get an accessible way to additional parameters and their meanings in this advanced model.

<!-- b000476 | caption | pages [14] -->
table4.2: additional parameters and meanings in this advanced model

<!-- b000477 | prose | pages [14] -->
DEFINITION

<!-- b000478 | heading | pages [14] -->
SYMBOL

<!-- b000479 | prose | pages [14] -->
UNITS

<!-- b000480 | prose | pages [14] -->
Transmission Parameter For First Stage Of Illness (In 

<!-- b000481 | furniture | pages [14] -->


<!-- b000482 | prose | pages [14] -->
1 H

<!-- b000483 | prose | pages [14] -->
Hospital)

<!-- b000484 | prose | pages [14] -->
-1 -1 people days

<!-- b000485 | prose | pages [14] -->
Transmission Parameter For Second Stage Of Illness (In 

<!-- b000486 | furniture | pages [14] -->


<!-- b000487 | prose | pages [14] -->
2 H

<!-- b000488 | prose | pages [14] -->
Hospital)

<!-- b000489 | prose | pages [14] -->
-1 -1 people days

<!-- b000490 | prose | pages [14] -->
Length Of First Stage Of Illness (From Moment Of 1h  1

<!-- b000491 | prose | pages [14] -->
Days Symptoms Appearing To Go To Hospital)

<!-- b000492 | prose | pages [14] -->
Length Of Second Stage Of Illness (From Moment Of 2h  1

<!-- b000493 | prose | pages [14] -->
Days Symptoms Appearing To Go To Hospital)

<!-- b000494 | prose | pages [14] -->
3y  1 Length Of First Stage Of Illness (In Hospital)

<!-- b000495 | prose | pages [14] -->
4y  1

<!-- b000496 | prose | pages [14] -->
Days

<!-- b000497 | prose | pages [14] -->
Length Of Second Stage Of Illness (In Hospital)

<!-- b000498 | prose | pages [14] -->


<!-- b000499 | furniture | pages [14] -->


<!-- b000500 | prose | pages [14] -->
Days

<!-- b000501 | prose | pages [14] -->
Overall Mortality Rate (Fraction) (In Hospital) 1 H 2 H Unitless

<!-- b000502 | prose | pages [14] -->
Mortality Rate (Fraction) Among Those In Second Stage Of 

<!-- b000503 | furniture | pages [14] -->


<!-- b000504 | prose | pages [14] -->
2H

<!-- b000505 | prose | pages [14] -->
Unitless Illness (In Hospital)

<!-- b000506 | furniture | pages [15] -->
Team # 34317                                                                Page 12 of 44

<!-- b000507 | prose | pages [15] -->
The reason why we add these parameters is that if hospital plays a role in people’s daily life, people will have another access to cure Ebola. When people feel

<!-- b000508 | prose | pages [15] -->
1h , 2h , 1 1 uncomfortable, they may choose to go to hospital for doctors’ help. Thus,

<!-- b000509 | prose | pages [15] -->
4y  are generated to denote different length of time in or not in hospital. 3y  and 1 1

<!-- b000510 | prose | pages [15] -->
, ,  By the way, and 2 H 1 H 2 H 1 H

<!-- b000511 | prose | pages [15] -->
more considerably.

<!-- b000512 | prose | pages [15] -->
 are introduced to explain the model 2H

<!-- b000513 | prose | pages [15] -->
We show our advanced model as a form of figure

<!-- b000514 | prose | pages [15] -->
S E

<!-- b000515 | prose | pages [15] -->
H1

<!-- b000516 | prose | pages [15] -->
I1 I1 I2

<!-- b000517 | prose | pages [15] -->
R F

<!-- b000518 | prose | pages [15] -->
H2

<!-- b000519 | furniture | pages [15] -->


<!-- b000520 | caption | pages [15] -->
figure4.5: advanced stage-structured model of ebola propagation

<!-- b000521 | prose | pages [15] -->
The advanced equations of this model are

<!-- b000522 | prose | pages [15] -->


<!-- b000523 | prose | pages [15] -->
dS

<!-- b000524 | prose | pages [15] -->


<!-- b000525 | prose | pages [15] -->


<!-- b000526 | prose | pages [15] -->


<!-- b000527 | prose | pages [15] -->


<!-- b000528 | prose | pages [15] -->


<!-- b000529 | prose | pages [15] -->


<!-- b000530 | prose | pages [15] -->
[ (

<!-- b000531 | prose | pages [15] -->
I H

<!-- b000532 | prose | pages [15] -->
) (

<!-- b000533 | prose | pages [15] -->
I

<!-- b000534 | prose | pages [15] -->


<!-- b000535 | prose | pages [15] -->
I

<!-- b000536 | prose | pages [15] -->
1

<!-- b000537 | prose | pages [15] -->
H

<!-- b000538 | prose | pages [15] -->
1 2

<!-- b000539 | prose | pages [15] -->
dt

<!-- b000540 | prose | pages [15] -->


<!-- b000541 | prose | pages [15] -->
dE

<!-- b000542 | prose | pages [15] -->


<!-- b000543 | prose | pages [15] -->


<!-- b000544 | prose | pages [15] -->


<!-- b000545 | prose | pages [15] -->


<!-- b000546 | prose | pages [15] -->


<!-- b000547 | prose | pages [15] -->


<!-- b000548 | prose | pages [15] -->


<!-- b000549 | prose | pages [15] -->
[ (

<!-- b000550 | prose | pages [15] -->
I H

<!-- b000551 | prose | pages [15] -->
) (

<!-- b000552 | prose | pages [15] -->
I

<!-- b000553 | prose | pages [15] -->


<!-- b000554 | prose | pages [15] -->
I

<!-- b000555 | prose | pages [15] -->
1

<!-- b000556 | prose | pages [15] -->
H

<!-- b000557 | prose | pages [15] -->
1 2 2

<!-- b000558 | prose | pages [15] -->
dt

<!-- b000559 | prose | pages [15] -->


<!-- b000560 | prose | pages [15] -->
dI

<!-- b000561 | prose | pages [15] -->


<!-- b000562 | prose | pages [15] -->


<!-- b000563 | prose | pages [15] -->


<!-- b000564 | prose | pages [15] -->


<!-- b000565 | prose | pages [15] -->


<!-- b000566 | prose | pages [15] -->


<!-- b000567 | prose | pages [15] -->
E I h I

<!-- b000568 | prose | pages [15] -->
1 1 1 1 1

<!-- b000569 | prose | pages [15] -->


<!-- b000570 | prose | pages [15] -->
dt

<!-- b000571 | prose | pages [15] -->


<!-- b000572 | prose | pages [15] -->
dI

<!-- b000573 | prose | pages [15] -->


<!-- b000574 | prose | pages [15] -->


<!-- b000575 | prose | pages [15] -->


<!-- b000576 | prose | pages [15] -->


<!-- b000577 | prose | pages [15] -->


<!-- b000578 | prose | pages [15] -->


<!-- b000579 | prose | pages [15] -->
I I h I

<!-- b000580 | prose | pages [15] -->
2 1 1 1 2 2 2 2

<!-- b000581 | prose | pages [15] -->
dt dH

<!-- b000582 | prose | pages [15] -->


<!-- b000583 | prose | pages [15] -->
 

<!-- b000584 | prose | pages [15] -->


<!-- b000585 | prose | pages [15] -->
h I H

<!-- b000586 | prose | pages [15] -->
1

<!-- b000587 | prose | pages [15] -->


<!-- b000588 | prose | pages [15] -->
1 1 3 1

<!-- b000589 | prose | pages [15] -->
dt

<!-- b000590 | prose | pages [15] -->


<!-- b000591 | prose | pages [15] -->
dH

<!-- b000592 | prose | pages [15] -->


<!-- b000593 | prose | pages [15] -->
 

<!-- b000594 | prose | pages [15] -->
 

<!-- b000595 | prose | pages [15] -->


<!-- b000596 | prose | pages [15] -->


<!-- b000597 | prose | pages [15] -->
h I H H

<!-- b000598 | prose | pages [15] -->
2 2 2 1

<!-- b000599 | prose | pages [15] -->
H

<!-- b000600 | prose | pages [15] -->
3 1 4 2

<!-- b000601 | prose | pages [15] -->


<!-- b000602 | prose | pages [15] -->
dt

<!-- b000603 | prose | pages [15] -->


<!-- b000604 | prose | pages [15] -->
dF

<!-- b000605 | prose | pages [15] -->


<!-- b000606 | prose | pages [15] -->


<!-- b000607 | prose | pages [15] -->


<!-- b000608 | prose | pages [15] -->
 

<!-- b000609 | prose | pages [15] -->


<!-- b000610 | prose | pages [15] -->


<!-- b000611 | prose | pages [15] -->


<!-- b000612 | prose | pages [15] -->
I H F

<!-- b000613 | prose | pages [15] -->
2 2 2 2

<!-- b000614 | prose | pages [15] -->
H

<!-- b000615 | prose | pages [15] -->
4 2

<!-- b000616 | prose | pages [15] -->
F

<!-- b000617 | prose | pages [15] -->
dt

<!-- b000618 | prose | pages [15] -->
 

<!-- b000619 | prose | pages [15] -->
dR

<!-- b000620 | prose | pages [15] -->
 

<!-- b000621 | prose | pages [15] -->


<!-- b000622 | prose | pages [15] -->
 

<!-- b000623 | prose | pages [15] -->


<!-- b000624 | prose | pages [15] -->
(1 )

<!-- b000625 | prose | pages [15] -->
I

<!-- b000626 | prose | pages [15] -->
(1 )

<!-- b000627 | prose | pages [15] -->
I

<!-- b000628 | prose | pages [15] -->


<!-- b000629 | prose | pages [15] -->
1 1 1 2 2

<!-- b000630 | prose | pages [15] -->
dt

<!-- b000631 | furniture | pages [15] -->


<!-- b000632 | furniture | pages [15] -->


<!-- b000633 | prose | pages [15] -->


<!-- b000634 | prose | pages [15] -->


<!-- b000635 | prose | pages [15] -->


<!-- b000636 | prose | pages [15] -->


<!-- b000637 | prose | pages [15] -->
H

<!-- b000638 | prose | pages [15] -->
)

<!-- b000639 | prose | pages [15] -->
F S

<!-- b000640 | prose | pages [15] -->
]

<!-- b000641 | prose | pages [15] -->
2 2

<!-- b000642 | prose | pages [15] -->
H

<!-- b000643 | prose | pages [15] -->
2

<!-- b000644 | prose | pages [15] -->
F

<!-- b000645 | prose | pages [15] -->
 

<!-- b000646 | prose | pages [15] -->


<!-- b000647 | prose | pages [15] -->


<!-- b000648 | prose | pages [15] -->


<!-- b000649 | prose | pages [15] -->


<!-- b000650 | prose | pages [15] -->


<!-- b000651 | prose | pages [15] -->
H

<!-- b000652 | prose | pages [15] -->
)

<!-- b000653 | prose | pages [15] -->
F S

<!-- b000654 | prose | pages [15] -->
]

<!-- b000655 | prose | pages [15] -->
E

<!-- b000656 | prose | pages [15] -->
H

<!-- b000657 | prose | pages [15] -->
2

<!-- b000658 | prose | pages [15] -->
F

<!-- b000659 | furniture | pages [15] -->


<!-- b000660 | prose | pages [15] -->
 

<!-- b000661 | prose | pages [15] -->
 

<!-- b000662 | prose | pages [15] -->
 

<!-- b000663 | prose | pages [15] -->
  (1 ) H (1 ) H 2 2 1 H 3 1 2 H 4 2

<!-- b000664 | prose | pages [15] -->
H mean number of people in hospital who are in first stage and H and Where 1 2

<!-- b000665 | furniture | pages [16] -->
Team # 34317                                                                Page 13 of 44

<!-- b000666 | prose | pages [16] -->
in second stage, respectively. While 1I , 2I mean the number of people not in

<!-- b000667 | prose | pages [16] -->
hospital who are in first stage and in second stage, respectively. And S , E , F and

<!-- b000668 | prose | pages [16] -->
R have the same meanings as we talked before.

<!-- b000669 | prose | pages [16] -->
In this group of equations, the susceptible are not only vulnerable to the sick

<!-- b000670 | prose | pages [16] -->
   ), but also to the patients in hospital ( outside ( or I I S 2I S 1 2

<!-- b000671 | prose | pages [16] -->


<!-- b000672 | prose | pages [16] -->
or H H S 1 1

<!-- b000673 | prose | pages [16] -->
). Different from what we explained in 3.4, the infected who are in first H H S 2 2

<!-- b000674 | prose | pages [16] -->
stage have another way to go – hospital ( h I ). And the infected who are in second 1 1

<!-- b000675 | prose | pages [16] -->
h I ), too. For the infected in hospital, they may die or recover. stage do ( 2 2

<!-- b000676 | heading | pages [16] -->
4.7 Results are Reasonable

<!-- b000677 | prose | pages [16] -->
First, we should better to find additional parameters’ values. Similarly, we use genetic algorithm combined with least square method that we have introduced above to calculate values. But there is a little difference at this moment is that

<!-- b000678 | prose | pages [16] -->
       X , / , / , , , , , , 1 2 1 F 1 1 2 F 1 2     , , , h h , , , , , . 2 2 H 1 2 3 4 1 H 2 H

<!-- b000679 | prose | pages [16] -->
We calculate all parameters in Guinea are:

<!-- b000680 | caption | pages [16] -->
table4.3: all parameters in Guinea

<!-- b000681 | prose | pages [16] -->
PARAMETER VALUE

<!-- b000682 | prose | pages [16] -->
 0.04 1

<!-- b000683 | prose | pages [16] -->
  / 2.37 2 1

<!-- b000684 | prose | pages [16] -->
  / 1.27 F 1

<!-- b000685 | prose | pages [16] -->
 0.42

<!-- b000686 | prose | pages [16] -->
 0.19 1 2

<!-- b000687 | prose | pages [16] -->
 0.58 2

<!-- b000688 | prose | pages [16] -->


<!-- b000689 | furniture | pages [16] -->


<!-- b000690 | prose | pages [16] -->
0.46 F

<!-- b000691 | prose | pages [16] -->
 0.70 2

<!-- b000692 | prose | pages [16] -->
PARAMETER VALUE

<!-- b000693 | prose | pages [16] -->
1 0.26

<!-- b000694 | prose | pages [16] -->


<!-- b000695 | furniture | pages [16] -->


<!-- b000696 | prose | pages [16] -->
0.48 H

<!-- b000697 | prose | pages [16] -->
1h 0.43

<!-- b000698 | prose | pages [16] -->
2h 0.55

<!-- b000699 | prose | pages [16] -->
 0.20 3

<!-- b000700 | prose | pages [16] -->
 0.11 4

<!-- b000701 | prose | pages [16] -->


<!-- b000702 | furniture | pages [16] -->


<!-- b000703 | prose | pages [16] -->
0.49 1H

<!-- b000704 | prose | pages [16] -->


<!-- b000705 | furniture | pages [16] -->


<!-- b000706 | prose | pages [16] -->
0.81 2H

<!-- b000707 | furniture | pages [17] -->
Team # 34317                                                                Page 14 of 44

<!-- b000708 | prose | pages [17] -->
And curves in Guinea are :

<!-- b000709 | furniture | pages [17] -->


<!-- b000710 | caption | pages [17] -->
figure 4.6: Test of Calculated Curves (Guinea)

<!-- b000711 | prose | pages [17] -->
We can see from the figure 4.6, our curves fit much better if we take hospital into consideration and add more parameters than the article we refer to. The curves can fit real data from January 1st, 2015 to February 3rd, 2015 in Guinea both in total cases and death cases. So we trust these two curves.

<!-- b000712 | heading | pages [17] -->
4.8 Prediction of the Future

<!-- b000713 | prose | pages [17] -->
Since we have found curves to fit real data well, our next job is to use the curves to predict number of total cases and death cases in Guinea in the near future. We draw a figure based on the figures that we have showed above. We lengthen the time axis to predict future cases until end of April, 2015.

<!-- b000714 | furniture | pages [18] -->
Team # 34317                                                                Page 15 of 44

<!-- b000715 | furniture | pages [18] -->


<!-- b000716 | caption | pages [18] -->
figure 4.7: prediction of future cases in Guinea

<!-- b000717 | prose | pages [18] -->
From the figure 4.7, the curves deliver us information about Guinea that number of total cases and death cases is still growing, and total cases grow a little bit faster than death cases grow. Number of total cases will reach to nearly 4000 after 180 days and death cases will reach to about 2500 after 180 days. However, number of cases is much less than a condition without hospital and medicine (see figure 4.7). After all, we just have medicine to cure Ebola patients whose disease is not advanced. As for serious patients, the only endeavor we can do is supportive treatment and pray.

<!-- b000718 | prose | pages [18] -->
Besides, we calculate parameters and curves of Liberia and Sierra Leone, we see curves also fit well to real data.

<!-- b000719 | furniture | pages [18] -->


<!-- b000720 | furniture | pages [18] -->


<!-- b000721 | furniture | pages [18] -->


<!-- b000722 | furniture | pages [18] -->


<!-- b000723 | furniture | pages [18] -->


<!-- b000724 | furniture | pages [19] -->
Team # 34317                                                                Page 16 of 44

<!-- b000725 | prose | pages [19] -->
The parameters of Liberia:

<!-- b000726 | caption | pages [19] -->
table4.4: parameters of Liberia

<!-- b000727 | prose | pages [19] -->
PARAMETER VALUE

<!-- b000728 | prose | pages [19] -->
 0.19 1

<!-- b000729 | prose | pages [19] -->
  / 2.06 2 1

<!-- b000730 | prose | pages [19] -->
  / 1.97 F 1

<!-- b000731 | prose | pages [19] -->
 0.45

<!-- b000732 | prose | pages [19] -->
 0.18 1 2

<!-- b000733 | prose | pages [19] -->
 0.63 2

<!-- b000734 | prose | pages [19] -->


<!-- b000735 | furniture | pages [19] -->


<!-- b000736 | prose | pages [19] -->
0.46 F

<!-- b000737 | prose | pages [19] -->
 0.92 2

<!-- b000738 | prose | pages [19] -->
The curves of Liberia:

<!-- b000739 | prose | pages [19] -->
PARAMETER VALUE

<!-- b000740 | prose | pages [19] -->
1 0.28

<!-- b000741 | prose | pages [19] -->


<!-- b000742 | furniture | pages [19] -->


<!-- b000743 | prose | pages [19] -->
0.23 H

<!-- b000744 | prose | pages [19] -->
1h 0.44

<!-- b000745 | prose | pages [19] -->
2h 0.73

<!-- b000746 | prose | pages [19] -->
 0.12 3

<!-- b000747 | prose | pages [19] -->
 0.84 4

<!-- b000748 | prose | pages [19] -->


<!-- b000749 | furniture | pages [19] -->


<!-- b000750 | prose | pages [19] -->
0.31 1H

<!-- b000751 | prose | pages [19] -->


<!-- b000752 | furniture | pages [19] -->


<!-- b000753 | prose | pages [19] -->
0.79 2H

<!-- b000754 | furniture | pages [19] -->


<!-- b000755 | caption | pages [19] -->
figure4.8: Test of Calculated Curves (Liberia)

<!-- b000756 | furniture | pages [19] -->


<!-- b000757 | furniture | pages [19] -->


<!-- b000758 | prose | pages [19] -->
We can see from the figure 4.8 that curves also fit well to real data of Liberia.

<!-- b000759 | furniture | pages [19] -->


<!-- b000760 | furniture | pages [19] -->


<!-- b000761 | furniture | pages [19] -->


<!-- b000762 | furniture | pages [19] -->


<!-- b000763 | furniture | pages [20] -->
Team # 34317                                                                Page 17 of 44

<!-- b000764 | prose | pages [20] -->
The parameters Sierra Leone:

<!-- b000765 | caption | pages [20] -->
table4.5: parameters Sierra Leone:

<!-- b000766 | prose | pages [20] -->
PARAMETER VALUE

<!-- b000767 | prose | pages [20] -->
 0.29 1

<!-- b000768 | prose | pages [20] -->
  / 2.43 2 1

<!-- b000769 | prose | pages [20] -->
  / 2.25 F 1

<!-- b000770 | prose | pages [20] -->
 0.46

<!-- b000771 | prose | pages [20] -->
 0.14 1 2

<!-- b000772 | prose | pages [20] -->
 0.54 2

<!-- b000773 | prose | pages [20] -->


<!-- b000774 | furniture | pages [20] -->


<!-- b000775 | prose | pages [20] -->
0.49 F

<!-- b000776 | prose | pages [20] -->
 0.81 2

<!-- b000777 | prose | pages [20] -->
The curves of Sierra Leone:

<!-- b000778 | prose | pages [20] -->
PARAMETER VALUE

<!-- b000779 | prose | pages [20] -->
1 0.26

<!-- b000780 | prose | pages [20] -->


<!-- b000781 | furniture | pages [20] -->


<!-- b000782 | prose | pages [20] -->
0.11 H

<!-- b000783 | prose | pages [20] -->
1h 0.48

<!-- b000784 | prose | pages [20] -->
2h 0.79

<!-- b000785 | prose | pages [20] -->
 0.71 3

<!-- b000786 | prose | pages [20] -->
 0.84 4

<!-- b000787 | prose | pages [20] -->


<!-- b000788 | furniture | pages [20] -->


<!-- b000789 | prose | pages [20] -->
0.49 1H

<!-- b000790 | prose | pages [20] -->


<!-- b000791 | furniture | pages [20] -->


<!-- b000792 | prose | pages [20] -->
0.76 2H

<!-- b000793 | furniture | pages [20] -->


<!-- b000794 | caption | pages [20] -->
figure4.9: test of calculated curves (Sierra Leone)

<!-- b000795 | prose | pages [20] -->
We can see from the figure that curves also fit well to real data of Sierra Leone.Because of limited time, we cannot do prediction job for Liberia and Sierra Leone. But we strongly believe if we have enough time, we can predict future data precisely by using these 16 parameters with consideration of hospital. Here we must say sorry to people who live in Liberia and Sierra Leone.

<!-- b000796 | furniture | pages [21] -->
Team # 34317                                                                Page 18 of 44

<!-- b000797 | heading | pages [21] -->
Ⅴ Model of Locations of Delivery

<!-- b000798 | prose | pages [21] -->
Locations of delivery, by definition, it is the place to give out medicine to somewhere is in emergency. Ebola outbreak in West Africa covers a terrified curtain to people live there. People who enveloped in the curtain, in some ways, really need effective medicine delivered to accurate region, otherwise, sadly, there are only body bags waiting for them. So determine delivery locations are quite necessary. Considering total cases and current condition at the moment when medicine is successfully manufactured in these three diseases-torn countries, we use several methods and criteria to judge where are the relatively good places both have minimal cost and best treatment.

<!-- b000799 | heading | pages [21] -->
5.1 What is Emergency Supplies

<!-- b000800 | prose | pages [21] -->
At first, it is needed for us to have a clear understand of what are emergency supplies, like the medicine to cure Ebola. Different from normal supplies, emergency supplies are used to control bombshells when an emergency happens or used for evacuation, rescue and repair after an emergency happened while normal supplies are just used in daily life. More specifically, differences between them are shown as the table below:

<!-- b000801 | caption | pages [21] -->
table5.1: differences between two supplies[3]

<!-- b000802 | prose | pages [21] -->
NORMAL SUPPLIES ASPECTS EMERGENCY SUPPLIES

<!-- b000803 | prose | pages [21] -->
Maximize Profile And Aims

<!-- b000804 | prose | pages [21] -->
Consider Both Fair And

<!-- b000805 | prose | pages [21] -->
Minimize Cost

<!-- b000806 | prose | pages [21] -->
Efficiency

<!-- b000807 | prose | pages [21] -->
Supplies Collection Point,

<!-- b000808 | prose | pages [21] -->
Factory, Distribution Center Formation

<!-- b000809 | prose | pages [21] -->
Delivery Place And Supplies

<!-- b000810 | prose | pages [21] -->
And Customer

<!-- b000811 | prose | pages [21] -->
Demand Point

<!-- b000812 | prose | pages [21] -->
Permanent Property Temporary

<!-- b000813 | prose | pages [21] -->
Divide Into Long-Term,

<!-- b000814 | prose | pages [21] -->
Urgency, Make Tread-Off

<!-- b000815 | prose | pages [21] -->
Medium-Term And

<!-- b000816 | prose | pages [21] -->
Scheme

<!-- b000817 | prose | pages [21] -->
Decision At Once

<!-- b000818 | prose | pages [21] -->
Short-Term

<!-- b000819 | prose | pages [21] -->
Balance Between Efficiency

<!-- b000820 | prose | pages [21] -->
Think A Lot Of Optimization And Optimization Think A Lot Of Efficiency

<!-- b000821 | prose | pages [21] -->
Return And Tour Delivery Mode Return

<!-- b000822 | prose | pages [21] -->
Besides, there are some other characteristics of emergency supplies. Take the medicine developed by the WMA for example:

<!-- b000823 | prose | pages [21] -->
i.

<!-- b000824 | prose | pages [21] -->
Uncertainty: because we cannot predict when next Ebola outbreak happens and how terrible death it may bring to victims, so emergency supplies have

<!-- b000825 | furniture | pages [22] -->
Team # 34317                                                                Page 19 of 44

<!-- b000826 | prose | pages [22] -->
uncertainties of amount of need and region of giving out.

<!-- b000827 | prose | pages [22] -->
ii.

<!-- b000828 | prose | pages [22] -->
Irreplaceability: emergency supplies are special in special conditions and are irreplaceable. Like the medicine to cure Ebola, if we do not have the medicine, nothing can effectively cure Ebola patient.

<!-- b000829 | prose | pages [22] -->
iii.

<!-- b000830 | prose | pages [22] -->
Timeliness: emergency supplies play their role at a certain period and if we miss the very moment, emergency supplies will lose their value. Like the medicine cannot revive already-dead Ebola patients

<!-- b000831 | prose | pages [22] -->
iv.

<!-- b000832 | prose | pages [22] -->
Hysteresis: emergency supplies (or medicine) always delivered later than a disaster happened.

<!-- b000833 | prose | pages [22] -->
Thus, our goal is to filtrate several most-needed delivery locations in a country. In detail, we filtrate the delivery locations accord to clustering method and some principles.

<!-- b000834 | heading | pages [22] -->
5.2 Assumptions and Justifications

<!-- b000835 | prose | pages [22] -->
i.

<!-- b000836 | prose | pages [22] -->
All delivery location lies in the provincial capitals of the prefectures.

<!-- b000837 | furniture | pages [22] -->


<!-- b000838 | prose | pages [22] -->
It is evident that the capitals is easy to receive medicine that from developed countries. Namely, the delivery locations are supposed to have quick access to harbors or airports. Meanwhile, they have good public facilities status, road conditions and communication and they are plenty of power, water, heat and gas supply.

<!-- b000839 | prose | pages [22] -->
ii.

<!-- b000840 | prose | pages [22] -->
Drug-need areas are concentrated on capitals of the prefectures, namely, we send the drug to capitals and do not consider the lower level of administrative areas.

<!-- b000841 | furniture | pages [22] -->


<!-- b000842 | prose | pages [22] -->
From the size of prefectures, we know they are not large and it is easy for capitals to deliver drug to its lower level of administrative areas. Also, capitals are representative places to an Ebola-hit region. Because of its advanced development and high population density, the more infected people lived in the capitals.

<!-- b000843 | prose | pages [22] -->
iii.

<!-- b000844 | prose | pages [22] -->
We overlook the cost when constructing delivery locations and the spending in storage of drugs.

<!-- b000845 | furniture | pages [22] -->


<!-- b000846 | prose | pages [22] -->
Ebola outbreak in these countries and we should pay more attention to people’s health and lives and we should construct delivery locations as soon as it is needed. Actually, the speed of producing drugs is hard to satisfy the intense situation and we need to deliver the drug to the need as soon as possible.

<!-- b000847 | furniture | pages [23] -->
Team # 34317                                                                Page 20 of 44

<!-- b000848 | heading | pages [23] -->
5.3 Clustering Method, A Way to Determine Regions for Medicine

<!-- b000849 | prose | pages [23] -->
Delivery

<!-- b000850 | prose | pages [23] -->
We have a relatively clear understanding why the delivery locations have to be places in the prefecture where the provincial capital is located. However, we still have too many delivery locations to build just because of limited foundation in African countries. Thus, to maximal effect of delivery locations with consideration of limited money and other factors that we talked above, we have to make choice among different delivery locations and filtrate some of the delivery locations as ‘last winners’.

<!-- b000851 | prose | pages [23] -->
We deem two or more major cities in a same country as a ‘city group’ if they are close in distance. It is of little meaning to build delivery locations in each of these cities because we can transmit emergency supplies to each cities conveniently in a short time. It is too dense to build delivery locations in a ‘city group’. So we adopt clustering method to find out ‘city groups’ to divide a country into several regions.

<!-- b000852 | prose | pages [23] -->
According to the reticular distance (The reticular distance is the distance following the road network using main roads (primary, secondary, tertiary and few track/Trail)), we classify cities as different groups. Here our steps are:

<!-- b000853 | prose | pages [23] -->
 First we consider all cities in a certain country are independent to each other,

<!-- b000854 | prose | pages [23] -->
namely, no groups contain two or more cities. Find reticular distance between

<!-- b000855 | prose | pages [23] -->
D D every two cities and construct a distance matrix

<!-- b000856 | prose | pages [23] -->
matrix.

<!-- b000857 | prose | pages [23] -->
 Second, find the minimum element in

<!-- b000858 | prose | pages [23] -->
, is a symmetric (0) (0)

<!-- b000859 | prose | pages [23] -->
D D G and we call it , then gather (0) KL k

<!-- b000860 | prose | pages [23] -->
   G G G , G , that is, G into a new group, and M L D . ( is the distance M k L KL

<!-- b000861 | prose | pages [23] -->
G are two groups.) between G and G , G and k L k L

<!-- b000862 | prose | pages [23] -->
 Third, calculate the distance between new group G that generated in second M

<!-- b000863 | prose | pages [23] -->
G . Here recurrence formula is step and other group j

<!-- b000864 | prose | pages [23] -->


<!-- b000865 | prose | pages [23] -->
  D

<!-- b000866 | prose | pages [23] -->
min

<!-- b000867 | prose | pages [23] -->
d

<!-- b000868 | prose | pages [23] -->
min min

<!-- b000869 | prose | pages [23] -->
MJ ij    x G

<!-- b000870 | prose | pages [23] -->
,

<!-- b000871 | prose | pages [23] -->
x G x G i M j J i K

<!-- b000872 | prose | pages [23] -->
  

<!-- b000873 | prose | pages [23] -->
 d

<!-- b000874 | prose | pages [23] -->
, min

<!-- b000875 | prose | pages [23] -->
d

<!-- b000876 | prose | pages [23] -->
min

<!-- b000877 | prose | pages [23] -->
D

<!-- b000878 | prose | pages [23] -->
,

<!-- b000879 | prose | pages [23] -->
D

<!-- b000880 | furniture | pages [23] -->


<!-- b000881 | prose | pages [23] -->
ij ij KJ LJ    

<!-- b000882 | prose | pages [23] -->
, ,

<!-- b000883 | prose | pages [23] -->
x x G x G

<!-- b000884 | prose | pages [23] -->
,

<!-- b000885 | prose | pages [23] -->
x G j j J i L j J

<!-- b000886 | furniture | pages [24] -->
Team # 34317                                                                Page 21 of 44

<!-- b000887 | prose | pages [24] -->
Refresh distance matrix D by gathering the row where G lies in and the (0) k

<!-- b000888 | prose | pages [24] -->
column where G lies in into a new row and new column, so we get a new L

<!-- b000889 | prose | pages [24] -->
distance matrix . D (1)

<!-- b000890 | prose | pages [24] -->
 Last, repeat the second step until all cities are gathered into a group.

<!-- b000891 | prose | pages [24] -->
When all steps are done, we will successfully find how many ‘city groups’ in a country.

<!-- b000892 | heading | pages [24] -->
5.4 Results of Clustering Method

<!-- b000893 | prose | pages [24] -->
When finish all the steps we described above, we get three clustering pictures of Guinea, Liberia and Sierra Leone and we can use them to accomplish the following task. Here we give Liberia’ clustering results one picture. The other two countries’ district-dividing situation present in the Appendix.

<!-- b000894 | furniture | pages [24] -->


<!-- b000895 | caption | pages [24] -->
figure5.1: Clustering Picture of Liberia

<!-- b000896 | prose | pages [24] -->
Once we have found ‘city groups’, we have another job to determine how many ‘city groups’ we need and which city in a ‘city group’ should be a delivery location. There are two principles we may need to comply with, one is principle of fairness, and the other is principle of efficiency.

<!-- b000897 | furniture | pages [24] -->


<!-- b000898 | furniture | pages [25] -->
Team # 34317                                                                Page 22 of 44

<!-- b000899 | heading | pages [25] -->
5.5 Principle of Fairness

<!-- b000900 | prose | pages [25] -->
When a disaster occurs, it not only causes significant property damage but causes a lot of casualties with time going by. We hold an opinion that every life is equal. We cannot ignore the trapped or the patient of Ebola just because they are small in number or the cost of rescue. Providing our hands to everyone who needs help is a symbol of respect life and humanitarianism. Moreover, it enhances the country's sense of trust and identity.

<!-- b000901 | prose | pages [25] -->
For this kind of principle, we invoke P-Center model to illustrate our delivery locations choosing. Often cities are made up by many communities and other compositions, and there always have people live there. Thus, when we determine a delivery place in a region, life equality is our priority. We use equations to demonstrate the principal.

<!-- b000902 | prose | pages [25] -->


<!-- b000903 | prose | pages [25] -->
P

<!-- b000904 | prose | pages [25] -->
min 

<!-- b000905 | prose | pages [25] -->
Z

<!-- b000906 | furniture | pages [25] -->


<!-- b000907 | prose | pages [25] -->


<!-- b000908 | prose | pages [25] -->
Z

<!-- b000909 | prose | pages [25] -->


<!-- b000910 | prose | pages [25] -->
i I

<!-- b000911 | prose | pages [25] -->
D y

<!-- b000912 | prose | pages [25] -->
ij ij

<!-- b000913 | prose | pages [25] -->
 

<!-- b000914 | prose | pages [25] -->
j J

<!-- b000915 | prose | pages [25] -->
Where i denotes a destination of medicine transportation, j denotes a delivery

<!-- b000916 | prose | pages [25] -->
D means distance between destination i and a delivery place in a region. And ij

<!-- b000917 | prose | pages [25] -->
ijy  denotes we have to send medicine to destination i while place j . And 1

<!-- b000918 | prose | pages [25] -->
ijy 

<!-- b000919 | prose | pages [25] -->


<!-- b000920 | prose | pages [25] -->
denotes there is no need to do this. So 0

<!-- b000921 | prose | pages [25] -->
means total distance

<!-- b000922 | prose | pages [25] -->
Z D y ij ij

<!-- b000923 | prose | pages [25] -->
 

<!-- b000924 | prose | pages [25] -->
i I j J

<!-- b000925 | prose | pages [25] -->
we have to cover if there are places need medicine. If a region has even need of medicine, the delivery place often in geographical center of the region.

<!-- b000926 | heading | pages [25] -->
5.6 Principle of Efficiency

<!-- b000927 | prose | pages [25] -->
According to population, risks and importance of different regions, we deem these regions of different ‘value’. Then different amount of emergency supplies are allocated to different delivery locations. Only in this way can we utilize the emergency supplies well and response as soon as possible if happens an emergency.

<!-- b000928 | prose | pages [25] -->
For this kind of principle, we invoke P-median model to illustrate our delivery locations choosing. When we determine a delivery place in a region, efficiency of delivering is our priority. We use equations to demonstrate the principal.

<!-- b000929 | prose | pages [25] -->


<!-- b000930 | prose | pages [25] -->
Q

<!-- b000931 | prose | pages [25] -->
min

<!-- b000932 | prose | pages [25] -->


<!-- b000933 | prose | pages [25] -->
Y

<!-- b000934 | prose | pages [25] -->


<!-- b000935 | prose | pages [25] -->
i I

<!-- b000936 | prose | pages [25] -->


<!-- b000937 | prose | pages [25] -->
Y

<!-- b000938 | furniture | pages [25] -->


<!-- b000939 | prose | pages [25] -->
w D y

<!-- b000940 | prose | pages [25] -->
i ij ij

<!-- b000941 | prose | pages [25] -->
 

<!-- b000942 | prose | pages [25] -->
j J j J

<!-- b000943 | furniture | pages [26] -->
Team # 34317                                                                Page 23 of 44

<!-- b000944 | prose | pages [26] -->
Where i , j , D and ijy have same meanings as those in principle of fairness. ij

<!-- b000945 | prose | pages [26] -->
And iw denotes the number of Ebola patients in a place, that is, the more people get

<!-- b000946 | prose | pages [26] -->


<!-- b000947 | prose | pages [26] -->
infected by Ebola, the larger iw is. Thus,

<!-- b000948 | prose | pages [26] -->
means total ‘distance’

<!-- b000949 | prose | pages [26] -->
Y w D y i ij ij

<!-- b000950 | prose | pages [26] -->
 

<!-- b000951 | prose | pages [26] -->
i I j J

<!-- b000952 | prose | pages [26] -->
we have to cover if there are places needing medicine. The reason why we use

<!-- b000953 | prose | pages [26] -->
‘distance’ is that we take iw into consideration, so ‘distance’ is not the proper

<!-- b000954 | prose | pages [26] -->
distance that we comprehend in daily life. Usually the delivery place is nearer to a more serious place in a region.

<!-- b000955 | heading | pages [26] -->
5.7 Determine Delivery Locations in the Three West African

<!-- b000956 | prose | pages [26] -->
Countries

<!-- b000957 | prose | pages [26] -->
Considering emergency of Ebola outbreak in a region, we find ‘city groups’ in Guinea, Liberia and Sierra Leone with criteria of delivering medicine within one day by trucks following the certain route (we will talk it in later part). If delivering time is more than one day, we use clustering method to find other ‘city groups’ to meet the criteria. Then we add the principals we showed above and finally determine delivery place(s) in Guinea, Liberia and Sierra Leone. During estimating process, we give different weight to the principle of fairness and the principle of efficiency. We endow more weight to the principle of fairness than the principle of efficiency because considering we can send medicine within one day, so advantages in time in different places may not play a main role in delivery locations choosing. Primarily, we consider fairness.

<!-- b000958 | heading | pages [26] -->
Ⅵ Model of Delivery System

<!-- b000959 | heading | pages [26] -->
6.1 Introduction

<!-- b000960 | prose | pages [26] -->
In the model of locations of delivery, we have determined some best delivery locations in a country to fit all the need that we put forward. However, only having delivery locations is far from a perfect project to distribute medicine to people who need it most, an effective and considerable delivery strategy is required, or a well-organized delivery system is required.

<!-- b000961 | prose | pages [26] -->
We define delivery system is made up by well-planned routes to allocate medicine and scientific amount of medicine to distribute to every needed places in every day.

<!-- b000962 | furniture | pages [27] -->
Team # 34317                                                                Page 24 of 44

<!-- b000963 | heading | pages [27] -->
6.2 Symbols and Definitions

<!-- b000964 | heading | pages [27] -->
SYMBOL

<!-- b000965 | prose | pages [27] -->
ijc

<!-- b000966 | prose | pages [27] -->
j

<!-- b000967 | prose | pages [27] -->
i

<!-- b000968 | prose | pages [27] -->
ijx

<!-- b000969 | prose | pages [27] -->
H 1

<!-- b000970 | furniture | pages [27] -->


<!-- b000971 | prose | pages [27] -->
DEFINITION

<!-- b000972 | prose | pages [27] -->
The Distance Between Two Points

<!-- b000973 | prose | pages [27] -->
End Point

<!-- b000974 | prose | pages [27] -->
Start Point

<!-- b000975 | prose | pages [27] -->
A Route From A Delivery Place To A

<!-- b000976 | prose | pages [27] -->
Destination

<!-- b000977 | prose | pages [27] -->
Number Of Patients In Hospital Who Are In

<!-- b000978 | prose | pages [27] -->
First Stage

<!-- b000979 | heading | pages [27] -->
6.3 TSP Model – Well-Planned Routes

<!-- b000980 | prose | pages [27] -->
Once happens certain scales of Ebola outbreaks, medicine have to be sent to cities or villages as soon as possible. Thanks to TSP (traveling salesman problem) Model, we structure an optimized route for trucks to transport medicine quickly.

<!-- b000981 | prose | pages [27] -->
We introduce a 0-1 integer variable

<!-- b000982 | prose | pages [27] -->
ijx  0

<!-- b000983 | prose | pages [27] -->
 ijx  denotes there is a route : ijx ijx ( i j ) 1

<!-- b000984 | prose | pages [27] -->
denotes there is no route from point i to from point i to point j while

<!-- b000985 | prose | pages [27] -->
point j . The TSP Model can be expressed a group of equations.

<!-- b000986 | prose | pages [27] -->
n n n

<!-- b000987 | prose | pages [27] -->


<!-- b000988 | prose | pages [27] -->
min

<!-- b000989 | prose | pages [27] -->


<!-- b000990 | prose | pages [27] -->
i

<!-- b000991 | prose | pages [27] -->


<!-- b000992 | prose | pages [27] -->
n

<!-- b000993 | prose | pages [27] -->


<!-- b000994 | prose | pages [27] -->


<!-- b000995 | prose | pages [27] -->
x

<!-- b000996 | prose | pages [27] -->
1,

<!-- b000997 | prose | pages [27] -->


<!-- b000998 | prose | pages [27] -->
ij

<!-- b000999 | prose | pages [27] -->


<!-- b001000 | prose | pages [27] -->


<!-- b001001 | prose | pages [27] -->
j

<!-- b001002 | prose | pages [27] -->
1

<!-- b001003 | prose | pages [27] -->


<!-- b001004 | prose | pages [27] -->
n

<!-- b001005 | prose | pages [27] -->


<!-- b001006 | prose | pages [27] -->


<!-- b001007 | prose | pages [27] -->
x

<!-- b001008 | prose | pages [27] -->
1,

<!-- b001009 | prose | pages [27] -->
s t

<!-- b001010 | prose | pages [27] -->
. .

<!-- b001011 | prose | pages [27] -->


<!-- b001012 | prose | pages [27] -->
ij

<!-- b001013 | prose | pages [27] -->


<!-- b001014 | prose | pages [27] -->


<!-- b001015 | prose | pages [27] -->
i

<!-- b001016 | prose | pages [27] -->
1

<!-- b001017 | prose | pages [27] -->
 

<!-- b001018 | prose | pages [27] -->
x

<!-- b001019 | prose | pages [27] -->
0,1,

<!-- b001020 | prose | pages [27] -->
ij

<!-- b001021 | prose | pages [27] -->
 

<!-- b001022 | prose | pages [27] -->
no subcycle

<!-- b001023 | prose | pages [27] -->
n

<!-- b001024 | prose | pages [27] -->
 

<!-- b001025 | prose | pages [27] -->
x

<!-- b001026 | prose | pages [27] -->
1

<!-- b001027 | prose | pages [27] -->
c x

<!-- b001028 | furniture | pages [27] -->


<!-- b001029 | prose | pages [27] -->
ij ij

<!-- b001030 | prose | pages [27] -->


<!-- b001031 | prose | pages [27] -->
1 1

<!-- b001032 | prose | pages [27] -->
j j

<!-- b001033 | prose | pages [27] -->
1

<!-- b001034 | prose | pages [27] -->
  

<!-- b001035 | prose | pages [27] -->
i i

<!-- b001036 | prose | pages [27] -->
1,2, , ,

<!-- b001037 | prose | pages [27] -->
n j i

<!-- b001038 | prose | pages [27] -->
,

<!-- b001039 | prose | pages [27] -->
 

<!-- b001040 | prose | pages [27] -->
j j

<!-- b001041 | prose | pages [27] -->
1,2, , ,

<!-- b001042 | prose | pages [27] -->
n i j

<!-- b001043 | prose | pages [27] -->
,

<!-- b001044 | furniture | pages [27] -->


<!-- b001045 | prose | pages [27] -->


<!-- b001046 | prose | pages [27] -->
i j i j

<!-- b001047 | prose | pages [27] -->
, , 1,2, , ,

<!-- b001048 | prose | pages [27] -->
n

<!-- b001049 | prose | pages [27] -->
means there must have a start point i if we want to consider i

<!-- b001050 | prose | pages [27] -->
Where

<!-- b001051 | prose | pages [27] -->
ij

<!-- b001052 | prose | pages [27] -->


<!-- b001053 | prose | pages [27] -->
j

<!-- b001054 | prose | pages [27] -->
1

<!-- b001055 | prose | pages [27] -->
n

<!-- b001056 | prose | pages [27] -->
  means there must have an end point j if we

<!-- b001057 | prose | pages [27] -->
as a point in route while

<!-- b001058 | prose | pages [27] -->
x

<!-- b001059 | prose | pages [27] -->
1

<!-- b001060 | prose | pages [27] -->
ij

<!-- b001061 | prose | pages [27] -->


<!-- b001062 | prose | pages [27] -->
i

<!-- b001063 | prose | pages [27] -->
1

<!-- b001064 | furniture | pages [28] -->
Team # 34317                                                                Page 25 of 44

<!-- b001065 | prose | pages [28] -->
want to consider j as a point in route. And ‘no subcycle’ means we must cover all points in a certain region, namely, all trucks will cover a route that contains all cities which are in emergency of Ebola outbreak. Moreover, to well describe ‘no subcycle’,

<!-- b001066 | prose | pages [28] -->
 and additional constraint condition: we add another variable iu i ( 1,2, , ) n

<!-- b001067 | prose | pages [28] -->
     u u nx n 1, for u u , i j ij i j   

<!-- b001068 | furniture | pages [28] -->


<!-- b001069 | prose | pages [28] -->
0, 0, i 1,2, , , n j 2,3, , , n i j

<!-- b001070 | prose | pages [28] -->
By now, we have established a model for us to construct a best route for trucks.

<!-- b001071 | heading | pages [28] -->
6.4 Daily Demand for Medicine

<!-- b001072 | prose | pages [28] -->
A good delivery system requires precise amount of medicine needed by places every day. We should develop a method to evaluate quantity of medicine we need a day by exploring number of patient in different places. We introduce an assessment standard called urgency index to depict how prob (i) much medicine a place need in one day. The expression of is prob (i)

<!-- b001073 | prose | pages [28] -->
H in a certain place in one day  prob (i)

<!-- b001074 | prose | pages [28] -->
1

<!-- b001075 | furniture | pages [28] -->


<!-- b001076 | prose | pages [28] -->
H in three countries in one day 1

<!-- b001077 | prose | pages [28] -->
H has same meaning as that we have talked in Ebola propagation model, Where 1

<!-- b001078 | prose | pages [28] -->
H means number of patients in hospital who are in first stage (such as fever, namely, 1

<!-- b001079 | prose | pages [28] -->
headache, sore throat, muscle aches and other milder symptoms which often progress

<!-- b001080 | prose | pages [28] -->
H to describe the urgency to diarrhea and vomiting). There two reasons why we use 1

<!-- b001081 | prose | pages [28] -->
index, one is the WMA has announced their medicine can cure patients whose disease is not advanced, the other is that patients in first stage have great possibility to become more serious and step into second stage (such as hemorrhaging and multi-organ failure), we need to stop them from worsening.

<!-- b001082 | prose | pages [28] -->
If we have a certain amount of medicine (we will discuss the amount needed later), we can distribute different amount of medicine to different places to meet patients’ requirement.

<!-- b001083 | furniture | pages [29] -->
Team # 34317                                                                Page 26 of 44

<!-- b001084 | heading | pages [29] -->
Ⅶ Model Implementation of three Countries

<!-- b001085 | heading | pages [29] -->
7.1General algorithm

<!-- b001086 | prose | pages [29] -->
In the last part, we have discussed the models and, in fact, we are supposed to combine these models to use in specific situations. Here we give the general algorithm to determine the delivery locations and the transport route.

<!-- b001087 | furniture | pages [29] -->


<!-- b001088 | prose | pages [29] -->
START

<!-- b001089 | furniture | pages [29] -->


<!-- b001090 | furniture | pages [29] -->


<!-- b001091 | prose | pages [29] -->
USING CLATER METHOD

<!-- b001092 | furniture | pages [29] -->


<!-- b001093 | furniture | pages [29] -->


<!-- b001094 | prose | pages [29] -->
DETERMING THE DELIVER

<!-- b001095 | furniture | pages [29] -->


<!-- b001096 | heading | pages [29] -->
TSP MODEL TO GET THE

<!-- b001097 | furniture | pages [29] -->


<!-- b001098 | furniture | pages [29] -->


<!-- b001099 | prose | pages [29] -->
INCREASE THE

<!-- b001100 | prose | pages [29] -->
NUMBER OF

<!-- b001101 | furniture | pages [29] -->


<!-- b001102 | prose | pages [29] -->
CARS FINISH EVERY ROUTE

<!-- b001103 | furniture | pages [29] -->


<!-- b001104 | prose | pages [29] -->
IN ONE DAY?

<!-- b001105 | furniture | pages [29] -->


<!-- b001106 | furniture | pages [29] -->


<!-- b001107 | prose | pages [29] -->
GET LOCATIONS AND TRANSPORT

<!-- b001108 | furniture | pages [29] -->


<!-- b001109 | furniture | pages [29] -->


<!-- b001110 | prose | pages [29] -->
END

<!-- b001111 | furniture | pages [29] -->


<!-- b001112 | caption | pages [29] -->
figure7.1: general algorithm to determine the delivery locations and route

<!-- b001113 | furniture | pages [30] -->
Team # 34317                                                                Page 27 of 44

<!-- b001114 | heading | pages [30] -->
7.2 Application of Algorithm

<!-- b001115 | prose | pages [30] -->
By exploring maps from WHO website of different Ebola cases in different places, then adopting TSP Model, we find some routes not only can cover all places that we have to send medicine to, but also consider places with more Ebola cases as more dangerous places and send medicine to the places within less time.

<!-- b001116 | heading | pages [30] -->
7.2.1 Application in Guinea

<!-- b001117 | prose | pages [30] -->
Since the area is approximately 245857 square kilometers and we must assure the route solved by the TSP model is not too long, in specific, we considered that one car can cover the distance in one day.

<!-- b001118 | furniture | pages [30] -->


<!-- b001119 | prose | pages [30] -->
Step 1: only one delivery location

<!-- b001120 | prose | pages [30] -->
Use the principles which are needed to determine the location, we calculate the delivery location lies in DABOLA. The maximum distance among DABOLA and other prefectures is 585km.

<!-- b001121 | prose | pages [30] -->
Then use the results of the cluster method, we divided other prefectures into two parts and DABOLA is in respond for the distribution of drugs to them. Thus, we need to solve tow TSP problems.

<!-- b001122 | furniture | pages [30] -->


<!-- b001123 | prose | pages [30] -->
Step 2: solve the distance route

<!-- b001124 | prose | pages [30] -->
Use the TSP model, we solve the route and use the picture shows the results:

<!-- b001125 | prose | pages [30] -->
location

<!-- b001126 | prose | pages [30] -->
A B

<!-- b001127 | prose | pages [30] -->
Confirmed Cases

<!-- b001128 | furniture | pages [30] -->


<!-- b001129 | caption | pages [30] -->
figure7.2: one delivery location in guinea

<!-- b001130 | furniture | pages [31] -->
Team # 34317                                                                Page 28 of 44

<!-- b001131 | prose | pages [31] -->
In the map, A and B represent the two route and the distances of them are 1213.8km and 1548.2km. Considering the velocity of vehicles is 80km/h, and it will cost more than 12 hours to finish one route and it is not reasonable for the relief of the disease. Therefore, only one location is not appropriate.

<!-- b001132 | furniture | pages [31] -->


<!-- b001133 | prose | pages [31] -->
Step3: adjust the number of delivery locations

<!-- b001134 | prose | pages [31] -->
According to the result of cluster results, it is better to divide the prefectures into 3 clusters. Then calculate the 3 different locations, cut every cluster into 2 smaller parts and repeat step2. We get the map:

<!-- b001135 | prose | pages [31] -->
B

<!-- b001136 | prose | pages [31] -->
A

<!-- b001137 | prose | pages [31] -->
location

<!-- b001138 | prose | pages [31] -->
Confirmed Cases

<!-- b001139 | prose | pages [31] -->
location

<!-- b001140 | prose | pages [31] -->
D C

<!-- b001141 | prose | pages [31] -->
1

<!-- b001142 | prose | pages [31] -->
E

<!-- b001143 | prose | pages [31] -->
location

<!-- b001144 | prose | pages [31] -->
F

<!-- b001145 | furniture | pages [31] -->


<!-- b001146 | caption | pages [31] -->
figure7.3: three delivery locations in guinea

<!-- b001147 | prose | pages [31] -->
In the map, A, B, C, D, E and represent the two route and the distances of them show in the table:

<!-- b001148 | prose | pages [31] -->
A B C

<!-- b001149 | prose | pages [31] -->
752.2 686.6 578.0

<!-- b001150 | prose | pages [31] -->
D E F

<!-- b001151 | prose | pages [31] -->
546.5 640.4 701.2

<!-- b001152 | prose | pages [31] -->
Vehicles can pass through the distance in one day. We conclude that 3 cluster is enough for Guinea.

<!-- b001153 | prose | pages [31] -->
And the delivery locations are: DUBREKA, KOUROUSSA, and MACENTA.

<!-- b001154 | furniture | pages [31] -->


<!-- b001155 | furniture | pages [31] -->


<!-- b001156 | furniture | pages [32] -->
Team # 34317                                                                Page 29 of 44

<!-- b001157 | prose | pages [32] -->
The route is listed:

<!-- b001158 | caption | pages [32] -->
table7.1: the six routes

<!-- b001159 | prose | pages [32] -->
DUBREKAFRIABOKEBOFFACONAKRYFORECARIAH

<!-- b001160 | prose | pages [32] -->
A

<!-- b001161 | prose | pages [32] -->
COYAHDUBREKA

<!-- b001162 | prose | pages [32] -->
B DUBREKATELIMELEPITADALABAKINDIADUBREKA

<!-- b001163 | prose | pages [32] -->
C KOUROUSSAFARANAHDABOLAKOUROUSSA

<!-- b001164 | prose | pages [32] -->
D KOUROUSSASIGUIRIKANKANKOUROUSSA

<!-- b001165 | prose | pages [32] -->
MACENTAGUECKEDOUKISSIDOUGOU

<!-- b001166 | prose | pages [32] -->
E

<!-- b001167 | prose | pages [32] -->
KEROUANEMACENTA

<!-- b001168 | prose | pages [32] -->
F MACENTABEYLALOLANZEREKOREYOMOUMACENTA

<!-- b001169 | furniture | pages [32] -->


<!-- b001170 | heading | pages [32] -->
7.2.2 Application in Liberia

<!-- b001171 | prose | pages [32] -->
In terms of area, Liberia is smaller than Guinea and its area is 111370 square kilometers. Following the algorithm, like the steps in the analysis of Guinea, and we find only one deliver center is proper for the area.

<!-- b001172 | furniture | pages [32] -->


<!-- b001173 | furniture | pages [32] -->


<!-- b001174 | furniture | pages [32] -->


<!-- b001175 | furniture | pages [32] -->


<!-- b001176 | furniture | pages [32] -->


<!-- b001177 | furniture | pages [32] -->


<!-- b001178 | furniture | pages [32] -->


<!-- b001179 | furniture | pages [32] -->


<!-- b001180 | furniture | pages [32] -->


<!-- b001181 | furniture | pages [32] -->


<!-- b001182 | furniture | pages [32] -->


<!-- b001183 | furniture | pages [32] -->


<!-- b001184 | furniture | pages [32] -->


<!-- b001185 | furniture | pages [32] -->


<!-- b001186 | furniture | pages [33] -->
Team # 34317                                                                Page 30 of 44

<!-- b001187 | prose | pages [33] -->
Here the results are:

<!-- b001188 | prose | pages [33] -->
A

<!-- b001189 | prose | pages [33] -->
Confirmed Cases

<!-- b001190 | prose | pages [33] -->
location

<!-- b001191 | prose | pages [33] -->
B

<!-- b001192 | furniture | pages [33] -->


<!-- b001193 | caption | pages [33] -->
figure7.4: one location in Liberia

<!-- b001194 | prose | pages [33] -->
In the map, A, and B represent the two route and the distances of them show in the table:

<!-- b001195 | prose | pages [33] -->
A

<!-- b001196 | prose | pages [33] -->
869.0

<!-- b001197 | prose | pages [33] -->
B

<!-- b001198 | prose | pages [33] -->
715.6

<!-- b001199 | prose | pages [33] -->
Therefore, the deliver location is Grand Bassa.

<!-- b001200 | heading | pages [33] -->
7.2.3 Sierra Leone

<!-- b001201 | prose | pages [33] -->
In terms of area, Sierra Leone is the smallest among the three countries and its area is 71740 square kilometers.

<!-- b001202 | prose | pages [33] -->
Just like what we have done before, we apply the algorithm.

<!-- b001203 | furniture | pages [33] -->


<!-- b001204 | furniture | pages [33] -->


<!-- b001205 | furniture | pages [33] -->


<!-- b001206 | furniture | pages [33] -->


<!-- b001207 | furniture | pages [33] -->


<!-- b001208 | furniture | pages [33] -->


<!-- b001209 | furniture | pages [33] -->


<!-- b001210 | furniture | pages [33] -->


<!-- b001211 | furniture | pages [33] -->


<!-- b001212 | furniture | pages [33] -->


<!-- b001213 | furniture | pages [34] -->
Team # 34317                                                                Page 31 of 44

<!-- b001214 | prose | pages [34] -->
Here present the result:

<!-- b001215 | prose | pages [34] -->
A

<!-- b001216 | prose | pages [34] -->
Confirmed Cases

<!-- b001217 | prose | pages [34] -->
location

<!-- b001218 | prose | pages [34] -->
B

<!-- b001219 | furniture | pages [34] -->


<!-- b001220 | caption | pages [34] -->
figure7.5: Sierra Leone

<!-- b001221 | prose | pages [34] -->
In the map, A, and B represent the two route and the distances of them show in the table:

<!-- b001222 | prose | pages [34] -->
A

<!-- b001223 | prose | pages [34] -->
411.4

<!-- b001224 | prose | pages [34] -->
B

<!-- b001225 | prose | pages [34] -->
616.9

<!-- b001226 | prose | pages [34] -->
Therefore, the deliver location is Tonkolili.

<!-- b001227 | heading | pages [34] -->
Ⅷ Model of the Quantity of the Medicine Needed and

<!-- b001228 | prose | pages [34] -->
Manufacturing Speed

<!-- b001229 | heading | pages [34] -->
8.1 Introduction

<!-- b001230 | prose | pages [34] -->
In this section, we consider the quantity of the medicine needed and speed of manufacturing of the vaccine or drug together because the manufacturing speed will impact the number of the susceptible, the infected who are in first stage and the recovered. The reason is that if the susceptible are vaccinated, they will hardly get infected by Ebola, and the infected once receive drug they can recover day by day. So the recovered is more than before as we regard the vaccinated people and cured people as the recovered.

<!-- b001231 | furniture | pages [35] -->
Team # 34317                                                                Page 32 of 44

<!-- b001232 | heading | pages [35] -->
8.2 Assumptions and Justifications

<!-- b001233 | prose | pages [35] -->
 Amount of medicine and vaccine that are produced everyday increase

<!-- b001234 | prose | pages [35] -->
linearly with time when the medicine or vaccine is rare. Because the medicine or vaccine is newly developed by scientists and still in testing stage, so manufactures will not produce a large-scale of this kind of medicine or vaccine at first. So we consider amount of medicine and vaccine that are produced everyday increase linearly with time rather than exponentially with time.

<!-- b001235 | prose | pages [35] -->
 The infected do not have ability of allopathic medicines. The Ebola virus are

<!-- b001236 | prose | pages [35] -->
relatively stable, namely, variation is not common in Ebola virus. So we consider Ebola virus do not have ability of allopathic medicines.

<!-- b001237 | heading | pages [35] -->
8.3 symbols and definitions

<!-- b001238 | prose | pages [35] -->
SYMBOL

<!-- b001239 | prose | pages [35] -->
V 1

<!-- b001240 | prose | pages [35] -->
V 2

<!-- b001241 | prose | pages [35] -->
1b

<!-- b001242 | prose | pages [35] -->
2b

<!-- b001243 | prose | pages [35] -->
DEFINITION

<!-- b001244 | prose | pages [35] -->
Speed Of Producing Medicine

<!-- b001245 | prose | pages [35] -->
Speed Of Producing Vaccine

<!-- b001246 | prose | pages [35] -->
Initial Inventory Of Medicine

<!-- b001247 | prose | pages [35] -->
Initial Inventory Of Vaccine

<!-- b001248 | prose | pages [35] -->
‘Manufacturing Acceleration’ Of 1k

<!-- b001249 | prose | pages [35] -->
Medicine Per Day

<!-- b001250 | prose | pages [35] -->
‘Manufacturing Acceleration’ Of Vaccine 2k

<!-- b001251 | prose | pages [35] -->
i

<!-- b001252 | prose | pages [35] -->
 1

<!-- b001253 | prose | pages [35] -->
Per Day

<!-- b001254 | prose | pages [35] -->
Urgency Index

<!-- b001255 | prose | pages [35] -->
Course Of Treatment Of The Medicine h

<!-- b001256 | furniture | pages [35] -->


<!-- b001257 | heading | pages [35] -->
8.4 How Fast Need We Produce Medicine and Vaccine

<!-- b001258 | prose | pages [35] -->
We have talked that Amount of medicine and vaccine produced everyday increase linearly with time in assumption, so we have equations to express the amount that produced per day.

<!-- b001259 | furniture | pages [36] -->
Team # 34317                                                                Page 33 of 44

<!-- b001260 | prose | pages [36] -->
Medicine V

<!-- b001261 | prose | pages [36] -->
Vaccine

<!-- b001262 | prose | pages [36] -->
 

<!-- b001263 | prose | pages [36] -->
k t b

<!-- b001264 | prose | pages [36] -->
1 1 1 1

<!-- b001265 | furniture | pages [36] -->


<!-- b001266 | prose | pages [36] -->
 

<!-- b001267 | prose | pages [36] -->
V V k t b

<!-- b001268 | prose | pages [36] -->
2 2 2 2

<!-- b001269 | prose | pages [36] -->
2b denote initial inventory of medicine and vaccine, respectively. Where 1b and

<!-- b001270 | prose | pages [36] -->
2k mean ‘manufacturing acceleration’ of medicine and vaccine per day. And 1k ,

<!-- b001271 | prose | pages [36] -->
V and time t . We show the relationship between 1

<!-- b001272 | furniture | pages [36] -->


<!-- b001273 | caption | pages [36] -->
figure8.1: speed of producing medicine

<!-- b001274 | prose | pages [36] -->
From the figure 8.1, we get information that when medicine is rare, the amount of medicine produced everyday increases linearly with time until all the patients who are in first stage can get the medicine, and this condition happens nearly 25 days after the medicine is used in the public. Then the amount of medicine that is produced everyday will drop with the number of patients who are in first stage. Namely, we

<!-- b001275 | prose | pages [36] -->
have more specific equations to explain V .

<!-- b001276 | prose | pages [36] -->
 

<!-- b001277 | prose | pages [36] -->
medicine V

<!-- b001278 | prose | pages [36] -->
1

<!-- b001279 | prose | pages [36] -->


<!-- b001280 | prose | pages [36] -->
1 1

<!-- b001281 | prose | pages [36] -->
 

<!-- b001282 | prose | pages [36] -->
k t b

<!-- b001283 | prose | pages [36] -->
,

<!-- b001284 | prose | pages [36] -->
V H

<!-- b001285 | prose | pages [36] -->
1 1 1 1 1

<!-- b001286 | furniture | pages [36] -->


<!-- b001287 | prose | pages [36] -->


<!-- b001288 | prose | pages [36] -->
H H

<!-- b001289 | prose | pages [36] -->
,

<!-- b001290 | prose | pages [36] -->
V H

<!-- b001291 | prose | pages [36] -->
1 1 1

<!-- b001292 | prose | pages [36] -->
When medicine and vaccine are used in the public, equations of the susceptible, the infected in first stage and the recover we have shown in the advanced model in sectionⅣ may change (marked in red).

<!-- b001293 | prose | pages [36] -->


<!-- b001294 | prose | pages [36] -->
dS

<!-- b001295 | prose | pages [36] -->


<!-- b001296 | prose | pages [36] -->


<!-- b001297 | prose | pages [36] -->


<!-- b001298 | prose | pages [36] -->


<!-- b001299 | prose | pages [36] -->


<!-- b001300 | prose | pages [36] -->


<!-- b001301 | prose | pages [36] -->


<!-- b001302 | prose | pages [36] -->
[ (

<!-- b001303 | prose | pages [36] -->
I H

<!-- b001304 | prose | pages [36] -->
) (

<!-- b001305 | prose | pages [36] -->
I

<!-- b001306 | prose | pages [36] -->


<!-- b001307 | prose | pages [36] -->
I

<!-- b001308 | prose | pages [36] -->
1

<!-- b001309 | prose | pages [36] -->
H

<!-- b001310 | prose | pages [36] -->
1 2 2

<!-- b001311 | prose | pages [36] -->
dt

<!-- b001312 | prose | pages [36] -->


<!-- b001313 | prose | pages [36] -->
dH

<!-- b001314 | prose | pages [36] -->
 

<!-- b001315 | prose | pages [36] -->


<!-- b001316 | prose | pages [36] -->


<!-- b001317 | prose | pages [36] -->


<!-- b001318 | prose | pages [36] -->


<!-- b001319 | prose | pages [36] -->
1

<!-- b001320 | prose | pages [36] -->
h I H

<!-- b001321 | prose | pages [36] -->
V

<!-- b001322 | prose | pages [36] -->


<!-- b001323 | prose | pages [36] -->
1 1 3 1

<!-- b001324 | prose | pages [36] -->
i

<!-- b001325 | prose | pages [36] -->
1

<!-- b001326 | prose | pages [36] -->
h

<!-- b001327 | prose | pages [36] -->
dt

<!-- b001328 | prose | pages [36] -->
 

<!-- b001329 | prose | pages [36] -->
dR

<!-- b001330 | prose | pages [36] -->
 

<!-- b001331 | prose | pages [36] -->


<!-- b001332 | prose | pages [36] -->
 

<!-- b001333 | prose | pages [36] -->
 

<!-- b001334 | prose | pages [36] -->


<!-- b001335 | prose | pages [36] -->
(1 )

<!-- b001336 | prose | pages [36] -->
I

<!-- b001337 | prose | pages [36] -->
(1 )

<!-- b001338 | prose | pages [36] -->
I

<!-- b001339 | prose | pages [36] -->


<!-- b001340 | prose | pages [36] -->
1 1 1 2 2 2

<!-- b001341 | prose | pages [36] -->
d t

<!-- b001342 | prose | pages [36] -->


<!-- b001343 | prose | pages [36] -->
 

<!-- b001344 | prose | pages [36] -->


<!-- b001345 | prose | pages [36] -->


<!-- b001346 | prose | pages [36] -->


<!-- b001347 | prose | pages [36] -->


<!-- b001348 | prose | pages [36] -->
H

<!-- b001349 | prose | pages [36] -->
)

<!-- b001350 | prose | pages [36] -->
F S

<!-- b001351 | prose | pages [36] -->
]

<!-- b001352 | prose | pages [36] -->
V

<!-- b001353 | prose | pages [36] -->
H H

<!-- b001354 | prose | pages [36] -->
2

<!-- b001355 | prose | pages [36] -->
F

<!-- b001356 | prose | pages [36] -->
i

<!-- b001357 | prose | pages [36] -->
2

<!-- b001358 | furniture | pages [36] -->


<!-- b001359 | prose | pages [36] -->


<!-- b001360 | prose | pages [36] -->
 

<!-- b001361 | prose | pages [36] -->
 

<!-- b001362 | prose | pages [36] -->


<!-- b001363 | prose | pages [36] -->


<!-- b001364 | prose | pages [36] -->


<!-- b001365 | prose | pages [36] -->


<!-- b001366 | prose | pages [36] -->
(1 (1 )

<!-- b001367 | prose | pages [36] -->
H

<!-- b001368 | prose | pages [36] -->
(1 )

<!-- b001369 | prose | pages [36] -->
H V

<!-- b001370 | prose | pages [36] -->
1

<!-- b001371 | prose | pages [36] -->
H

<!-- b001372 | prose | pages [36] -->
3 1 2

<!-- b001373 | prose | pages [36] -->
H

<!-- b001374 | prose | pages [36] -->
4

<!-- b001375 | prose | pages [36] -->
2

<!-- b001376 | prose | pages [36] -->
i

<!-- b001377 | prose | pages [36] -->
2

<!-- b001378 | furniture | pages [37] -->
Team # 34317                                                                Page 34 of 44

<!-- b001379 | prose | pages [37] -->
i is the urgency index that we have described in section 6.4, namely, Where

<!-- b001380 | prose | pages [37] -->
H in a certain place in one day  

<!-- b001381 | prose | pages [37] -->
1

<!-- b001382 | prose | pages [37] -->
prob

<!-- b001383 | prose | pages [37] -->
(i) i

<!-- b001384 | prose | pages [37] -->
. We distribute medicine with criteria H in three countries in one day

<!-- b001385 | prose | pages [37] -->
1

<!-- b001386 | prose | pages [37] -->
that we have described in section 6.4, so  means number of the susceptible who iV 2

<!-- b001387 | prose | pages [37] -->
are vaccinated and have antibody to against Ebola, thus, can hardly get infected. And

<!-- b001388 | prose | pages [37] -->
 means number of the infected who are in first stage get recovered because of  V i 1 h

<!-- b001389 | prose | pages [37] -->
 means course of treatment of the medicine. And 1 the medicine, h  means the iV 2

<!-- b001390 | prose | pages [37] -->
number of the susceptible who will hardly get infected because of the vaccine. Then we draw a figure to express changing of total cases growing with time in the condition of using medicine.

<!-- b001391 | furniture | pages [37] -->


<!-- b001392 | caption | pages [37] -->
figure 8.2: Changing of Total Cases Growing with Time When Using Medicine

<!-- b001393 | prose | pages [37] -->
As for vaccine, it generates its effect mainly among the susceptible. Since number of the susceptible is much much larger than amount of vaccine, we ignore the effect generated by the vaccine. From the figure, we can see the medicine is used after 90 days form initial time, that is, we can figure out that the medicine is used from Feb.1st, 2015. And 50 days after using the medicine, number of total cases will not increase, which means the medicine has its positive impact on Ebola containing.

<!-- b001394 | prose | pages [37] -->
b  5 The parameters in our calculating process are (we produce 5 units of 1

<!-- b001395 | prose | pages [37] -->
k  5 medicine per day at the beginning of producing) and (we produce 5 more 1

<!-- b001396 | furniture | pages [38] -->
Team # 34317                                                                Page 35 of 44

<!-- b001397 | prose | pages [38] -->
units of medicine per day).

<!-- b001398 | prose | pages [38] -->
As for vaccine, we ignore it in our calculating process for it is much much less in number compared to number of the susceptible.

<!-- b001399 | heading | pages [38] -->
8.5 The Quantity of the Medicine Needed

<!-- b001400 | prose | pages [38] -->
We use integral computation to find the quantity of the medicine we need. So total needed amount is

<!-- b001401 | prose | pages [38] -->
 w t t

<!-- b001402 | furniture | pages [38] -->


<!-- b001403 | prose | pages [38] -->
V t dt ( ) 1 0 0

<!-- b001404 | prose | pages [38] -->
Use parameters we have calculated in last section, we draw a figure to show the quantity of the medicine.

<!-- b001405 | furniture | pages [38] -->


<!-- b001406 | caption | pages [38] -->
figure8.3: Changing of Quantity of The Medicine

<!-- b001407 | prose | pages [38] -->
So we need about 3400 units of medicine to cure the patient who are in first stage in the three west African countries.

<!-- b001408 | prose | pages [38] -->
If we develop better medicine that can cure patients in second stage in the future, we believe the quantity of medicine can decrease.

<!-- b001409 | prose | pages [38] -->
Ⅸ Other Factors We Think Are Important

<!-- b001410 | prose | pages [38] -->
In our first model –SEIIRF model and its advanced model, we didn’t consider other two factors that we think are necessary to discuss. One is control of Ebola spreading in hospitals, and the other is control of Ebola spreading in funerals.

<!-- b001411 | prose | pages [38] -->
If we control of Ebola spreading in hospital, there will be less healthy people get infected. We regard a hospital as a ‘huge’ patient with strong ability of infection. We must take measures to reduce the ability of infection. The figure shown below delivers us information that hoe the total cases in Guinea will be like if we reduce 50% and 90% of the ability down.

<!-- b001412 | furniture | pages [39] -->
Team # 34317                                                                Page 36 of 44

<!-- b001413 | furniture | pages [39] -->


<!-- b001414 | caption | pages [39] -->
figure9.1: changing of total cases in guinea if we control Ebola spreading in hospitals

<!-- b001415 | prose | pages [39] -->
We can see from the figure, if we take strategies to control Ebola spreading in hospitals, total cases will reduce greatly and significantly.

<!-- b001416 | prose | pages [39] -->
Then if we control Ebola spreading in funerals, what will happen? There is a figure will tell us.

<!-- b001417 | furniture | pages [39] -->


<!-- b001418 | caption | pages [39] -->
figure9.2: changing of total cases in guinea if we control Ebola spreading in funerals

<!-- b001419 | prose | pages [39] -->
Controlling Ebola spreading in funerals maybe are not as good as in hospitals. But at least, it does its positive effect on reducing total cases in the future.

<!-- b001420 | prose | pages [39] -->
Ⅹ Future Improvement

<!-- b001421 | heading | pages [39] -->
10.1 Optimization of Coverage to Determine Delivery Locations

<!-- b001422 | prose | pages [39] -->
Since we are introduced one method and two principles in delivery places choosing,

<!-- b001423 | furniture | pages [40] -->
Team # 34317                                                                Page 37 of 44

<!-- b001424 | prose | pages [40] -->
now we can easily make a decision on where to build a delivery place in a certain region. However, as a designer, we must be more considerable if we have more time to do our design. Unfortunately, time is limited, here we just introduce you another principle that is worthwhile to consider – principle of optimization of coverage. When a disaster occurs, we will generally distribute emergency supplies which are relatively near to the place that happens the disaster as fast as possible. Considering the disaster, like Ebola, is usually of great impact on the local and of tremendous harm, we sometimes need to allocate and transport more emergency supplies to this area. Thus, when we choose to delivery places we must take it into consideration that the delivery places can cover as many emergency-supplies-need regions as possible simultaneously. So when an emergency happens in an area that covered by a delivery place, emergency supplies, like the medicine, can be sent in time. Here the equations of the principle are

<!-- b001425 | prose | pages [40] -->


<!-- b001426 | prose | pages [40] -->
X

<!-- b001427 | prose | pages [40] -->
max 

<!-- b001428 | prose | pages [40] -->
A

<!-- b001429 | furniture | pages [40] -->


<!-- b001430 | prose | pages [40] -->


<!-- b001431 | prose | pages [40] -->
A

<!-- b001432 | prose | pages [40] -->


<!-- b001433 | prose | pages [40] -->
i I

<!-- b001434 | prose | pages [40] -->
wc y

<!-- b001435 | prose | pages [40] -->
i ij ij

<!-- b001436 | prose | pages [40] -->
 

<!-- b001437 | prose | pages [40] -->
j J j J

<!-- b001438 | prose | pages [40] -->
ijy have same meanings as those in principle of fairness. Where i , j , iw and

<!-- b001439 | prose | pages [40] -->
And we call ijc degree of coverage.

<!-- b001440 | prose | pages [40] -->


<!-- b001441 | prose | pages [40] -->
1

<!-- b001442 | prose | pages [40] -->
  

<!-- b001443 | prose | pages [40] -->
t t

<!-- b001444 | prose | pages [40] -->


<!-- b001445 | prose | pages [40] -->
c

<!-- b001446 | prose | pages [40] -->


<!-- b001447 | prose | pages [40] -->
ij

<!-- b001448 | prose | pages [40] -->


<!-- b001449 | prose | pages [40] -->
t

<!-- b001450 | prose | pages [40] -->


<!-- b001451 | prose | pages [40] -->
m

<!-- b001452 | prose | pages [40] -->


<!-- b001453 | prose | pages [40] -->
0

<!-- b001454 | prose | pages [40] -->
 

<!-- b001455 | prose | pages [40] -->
, ,

<!-- b001456 | prose | pages [40] -->
t t

<!-- b001457 | prose | pages [40] -->
m

<!-- b001458 | prose | pages [40] -->


<!-- b001459 | prose | pages [40] -->
, ,

<!-- b001460 | prose | pages [40] -->
t t t

<!-- b001461 | prose | pages [40] -->
1 1

<!-- b001462 | furniture | pages [40] -->


<!-- b001463 | prose | pages [40] -->
1

<!-- b001464 | prose | pages [40] -->
m

<!-- b001465 | prose | pages [40] -->
t t

<!-- b001466 | prose | pages [40] -->
1 1

<!-- b001467 | prose | pages [40] -->


<!-- b001468 | prose | pages [40] -->
, ,

<!-- b001469 | prose | pages [40] -->
t t

<!-- b001470 | prose | pages [40] -->
m

<!-- b001471 | prose | pages [40] -->
1t is minimum time of a truck to arrive at a destination while Where mt is

<!-- b001472 | prose | pages [40] -->
maximum time of a truck to arrive at a destination. In our model of delivery places

<!-- b001473 | prose | pages [40] -->
ijc , we can see the mt is no longer than one day. From expression of choosing,

<!-- b001474 | prose | pages [40] -->
degree of coverage increases with time going by, which is consistent with reality.

<!-- b001475 | heading | pages [40] -->
10.2 A No-boundary Scheme

<!-- b001476 | prose | pages [40] -->
In our paper, the models of locations and TSP apply in three countries (Sierra Leone, Liberia and Guinea) respectively. We consider there is no contact among these Ebola-hit countries and the delivery locations distributed in three countries and every countries delivery locations only send needed drug to itself. However, we human beings should unit to eradicate the Ebola in the face of such serious situation. Therefore, we are better to combine the three countries tightly and arrange the delivery locations and transportation system without considering the boundary and political problems.

<!-- b001477 | prose | pages [40] -->
So a no-boundary scheme can be developed to quickly get rid of the trouble of

<!-- b001478 | furniture | pages [41] -->
Team # 34317                                                                Page 38 of 44

<!-- b001479 | prose | pages [41] -->
Ebola.

<!-- b001480 | heading | pages [41] -->
Ⅺ Sensitivity analysis

<!-- b001481 | heading | pages [41] -->
11.1 Sensitivity Analysis of SEIIRF Model

<!-- b001482 | prose | pages [41] -->
We get some parameters through the method of least squares fitting in the model to predict the spread of Ebola,. To test the effect of changing parameters, we will produce a sensitivity analysis that shows whether our model is properly sensitive to these variations.

<!-- b001483 | prose | pages [41] -->
In the following section, we will analyze the sensitivity of total cases of patients, , Length Of First Stage Of Illness (Not In according to Average Incubation Period 1 1

<!-- b001484 | prose | pages [41] -->
1, Transmission Parameter For First Stage Of Illness (Not In Hospital) 1 Hospital)

<!-- b001485 | prose | pages [41] -->
, ,  respectively. In specific, we modified parameter ( 1 1) by 

<!-- b001486 | furniture | pages [41] -->


<!-- b001487 | prose | pages [41] -->
10% 1

<!-- b001488 | prose | pages [41] -->
respectively and observe the change of total cases.

<!-- b001489 | furniture | pages [41] -->


<!-- b001490 | prose | pages [41] -->
 to the total cases

<!-- b001491 | caption | pages [41] -->
figure11.1: the impact of

<!-- b001492 | prose | pages [41] -->
1

<!-- b001493 | prose | pages [41] -->
From the picture above we can get the result that the total cases of patients change

<!-- b001494 | prose | pages [41] -->
. So this proves the slight fluctuations of little with the change of 1  can be 1

<!-- b001495 | prose | pages [41] -->
ignored and the results we conclude in the above models are reliable.

<!-- b001496 | furniture | pages [41] -->


<!-- b001497 | furniture | pages [42] -->
Team # 34317                                                                Page 39 of 44

<!-- b001498 | furniture | pages [42] -->


<!-- b001499 | prose | pages [42] -->
1 to the total cases

<!-- b001500 | caption | pages [42] -->
figure11.2: the impact of

<!-- b001501 | prose | pages [42] -->
As the figure shows, the total cases stay relatively stable in different result

<!-- b001502 | prose | pages [42] -->
1. Therefore, the total cases we use is exact enough. generated from different

<!-- b001503 | heading | pages [42] -->
11.2 Sensitivity Analysis of Model of the Speed to Produce Medicine

<!-- b001504 | prose | pages [42] -->
We change initial speed of the production of medicine 1b and total cases of

<!-- b001505 | prose | pages [42] -->
patients are shown in the following the figure:

<!-- b001506 | furniture | pages [42] -->


<!-- b001507 | prose | pages [42] -->
1b to the total cases

<!-- b001508 | caption | pages [42] -->
figure11.3: the impact of

<!-- b001509 | furniture | pages [43] -->
Team # 34317                                                                Page 40 of 44

<!-- b001510 | prose | pages [43] -->
From the picture above, we find that if the speed 1b is relatively small, the

<!-- b001511 | prose | pages [43] -->
influence of the change of 1b is larger compared to bigger 1b . In addition, we find

<!-- b001512 | prose | pages [43] -->
that cases increase with the increase of initial speed and the trend is expected. In all, the results are stable.

<!-- b001513 | heading | pages [43] -->
Ⅻ Conclusion

<!-- b001514 | heading | pages [43] -->
11.1 Strengths and Weaknesses

<!-- b001515 | prose | pages [43] -->
Now we will analyze the strengths and weaknesses of models in our paper:

<!-- b001516 | furniture | pages [43] -->


<!-- b001517 | heading | pages [43] -->
SEIIRF Model

<!-- b001518 | prose | pages [43] -->
Strengths 1. The results of model conform to the reality well, such as the prediction of the number of patient cases. 2. We considered three ways of the spread of Ebola which are relatively comprehensive and more groups of people which are representative to the disease search.

<!-- b001519 | furniture | pages [43] -->


<!-- b001520 | prose | pages [43] -->
Weaknesses 1. There are more parameters in the model and it may bring negative influence to the sensitivity. 2. Due to lack of data, we do not study spatial distribution of Ebola.

<!-- b001521 | furniture | pages [43] -->


<!-- b001522 | heading | pages [43] -->
Model of Locations of Delivery and Delivery System

<!-- b001523 | prose | pages [43] -->
Strengths 1. We use TSP model which is relatively simple but effective to solve the delivery system. 2. We develop a general algorithm to determine the transportation locations and system. Weaknesses 1. Because the limit of time, we do not solve the the no-boundary scheme which is presented in the part of future improvement.

<!-- b001524 | furniture | pages [43] -->


<!-- b001525 | heading | pages [43] -->
Model of the Speed to Produce Medicine

<!-- b001526 | prose | pages [43] -->
Strengths 1. We calculated the model on quantitative analysis.

<!-- b001527 | furniture | pages [43] -->


<!-- b001528 | prose | pages [43] -->
Weaknesses 1. The speed to producing drug grow linearly and this process maybe too ideally

<!-- b001529 | furniture | pages [44] -->
Team # 34317                                                                Page 41 of 44

<!-- b001530 | heading | pages [44] -->
11.2 Overall Results

<!-- b001531 | prose | pages [44] -->
Up to now, we have accomplished all our tasks. And here we give the overall results of all our models.

<!-- b001532 | prose | pages [44] -->
Above all, we develop basic SEIIRF model and then improve this model to predict the spread of Ebola, and finally the model confirms to the reality which we test it using collected data. Then, we establish a general algorithm to solve the delivery locations and design delivery system. In specific, we get the locations of delivery and the certain route of transportation system through cluster analysis and TSP model. Also, the length of all routes is suitable for the delivery of drug. With the route, we can distribute drug according to urgency index which is relevant to the proportionality of the patients. Considering the specific speed of producing the drug, we simulate the situation and get the conclusion that in 50 days, we can eradicate Ebola. After that, we consider other factors, such as control of Ebola spreading in hospitals and in funerals, and the situation can be relieved greatly. At last, we test the sensitivity of our model and it shows that they are stable.

<!-- b001533 | furniture | pages [44] -->


<!-- b001534 | furniture | pages [44] -->


<!-- b001535 | furniture | pages [44] -->


<!-- b001536 | furniture | pages [44] -->


<!-- b001537 | furniture | pages [44] -->


<!-- b001538 | furniture | pages [44] -->


<!-- b001539 | furniture | pages [44] -->


<!-- b001540 | furniture | pages [44] -->


<!-- b001541 | furniture | pages [44] -->


<!-- b001542 | furniture | pages [44] -->


<!-- b001543 | furniture | pages [44] -->


<!-- b001544 | furniture | pages [44] -->


<!-- b001545 | furniture | pages [44] -->


<!-- b001546 | furniture | pages [44] -->


<!-- b001547 | furniture | pages [44] -->


<!-- b001548 | furniture | pages [44] -->


<!-- b001549 | furniture | pages [44] -->


<!-- b001550 | furniture | pages [45] -->
Team # 34317                                                                Page 42 of 44

<!-- b001551 | heading | pages [45] -->
LETTER

<!-- b001552 | prose | pages [45] -->
To: Professors of the World Medical Association

<!-- b001553 | prose | pages [45] -->
From: Team # 34317

<!-- b001554 | prose | pages [45] -->
Date: February 9, 2015

<!-- b001555 | prose | pages [45] -->
Subject: A Battle against Ebola

<!-- b001556 | furniture | pages [45] -->


<!-- b001557 | prose | pages [45] -->
Ebola, a familiar but strange word to us. No one can

<!-- b001558 | prose | pages [45] -->
imagine the name ‘Ebola’ just originates from a little

<!-- b001559 | prose | pages [45] -->
river - Ebola River in Congo. Contrary to its attracting

<!-- b001560 | prose | pages [45] -->
meaning, it is true that the Ebola virus do take lots of

<!-- b001561 | prose | pages [45] -->
victims’ lives away. Fighting against Ebola is now a

<!-- b001562 | prose | pages [45] -->
worldwide battle. We human beings need to unit together

<!-- b001563 | prose | pages [45] -->
and offer helps to each other. Besides, we are really

<!-- b001564 | prose | pages [45] -->
appreciate those doctors in the MSF who fight against

<!-- b001565 | prose | pages [45] -->
Ebola day and night in West Africa.

<!-- b001566 | prose | pages [45] -->
We also do our best to evaluate Ebola spreading in West

<!-- b001567 | heading | pages [45] -->
Africa. We use models to predict future cases in Guinea,

<!-- b001568 | prose | pages [45] -->
Liberia and Sierra Leone. First, we use real data to

<!-- b001569 | prose | pages [45] -->
calculate a curve for usage of prediction. Then we use

<!-- b001570 | prose | pages [45] -->
newest data in the WHO website to test the curve. We

<!-- b001571 | prose | pages [45] -->
find the curve can predict well and be trusted. Then, we

<!-- b001572 | furniture | pages [46] -->
Team # 34317                                                                Page 43 of 44

<!-- b001573 | prose | pages [46] -->
use this curve to predict future cases including total cases

<!-- b001574 | prose | pages [46] -->
and death cases. And we find that if we use medicine,

<!-- b001575 | prose | pages [46] -->
total cases and death cases will decrease a lot.

<!-- b001576 | prose | pages [46] -->
Then we design a method to find some best delivery

<!-- b001577 | prose | pages [46] -->
places in Guinea, Liberia and Sierra Leone that can

<!-- b001578 | prose | pages [46] -->
allocate medicine quickly to places where Ebola

<!-- b001579 | prose | pages [46] -->
outbreaks. Moreover, we offer you schemed routes both

<!-- b001580 | prose | pages [46] -->
are time-saving and able to caver most places for

<!-- b001581 | prose | pages [46] -->
vehicles to transport emergency supplies.

<!-- b001582 | prose | pages [46] -->
At last, we calculate out the quantity of the medicine

<!-- b001583 | prose | pages [46] -->
needed and the speed of manufacturing medicine and

<!-- b001584 | prose | pages [46] -->
vaccine. We take two conditions into consideration. One

<!-- b001585 | prose | pages [46] -->
is the condition that if medicine is too rare to help most

<!-- b001586 | prose | pages [46] -->
people, the medicine factories should gradually increase

<!-- b001587 | prose | pages [46] -->
their output, and the other condition is that if medicine is

<!-- b001588 | prose | pages [46] -->
enough for the infected, the amount of medicine should

<!-- b001589 | prose | pages [46] -->
decrease with time. The total amount of medicine is 3400

<!-- b001590 | prose | pages [46] -->
units.

<!-- b001591 | prose | pages [46] -->
Besides, we have done other jobs to evaluate Ebola, you

<!-- b001592 | prose | pages [46] -->
can see our paper for details.

<!-- b001593 | prose | pages [46] -->
Yours sincerely

<!-- b001594 | furniture | pages [46] -->
Team # 34317

<!-- b001595 | furniture | pages [47] -->
Team # 34317                                                                Page 44 of 44

<!-- b001596 | prose | pages [47] -->
ⅩⅢ Reference

<!-- b001597 | prose | pages [47] -->
[1]http://www.theguardian.com/commentisfree/2014/dec/29/2015-ebola-eradicated-ep

<!-- b001598 | prose | pages [47] -->
idemic-west-africa

<!-- b001599 | prose | pages [47] -->
[2]http://www.huffingtonpost.com/darius-mans/behavior-change-is-key-to_b_575270

<!-- b001600 | prose | pages [47] -->
4.html

<!-- b001601 | prose | pages [47] -->
[3] Tzeng, G H.,Cheng, H. J., and Huang, T. D. Multi-objective optimal planning for

<!-- b001602 | prose | pages [47] -->
designing relief delivery systems. Transportation Research Part E: Logistics and

<!-- b001603 | prose | pages [47] -->
Transportation Review, 2007,43(6),673-686.

<!-- b001604 | prose | pages [47] -->
[4] http://www.diva-gis.org/datadown

<!-- b001605 | prose | pages [47] -->
[5] Marisa C. Eisenberg, Joseph N.S. Eisenberg, Jeremy P. D'Silva, Eden V. Wells.”

<!-- b001606 | prose | pages [47] -->
Modeling surveillance and interventions in the 2014 Ebola epidemic” The Lancet

<!-- b001607 | prose | pages [47] -->
Infectious Diseases(2015).

<!-- b001608 | prose | pages [47] -->
[6] Chen zhi-zong, “Major events multi-objective decision model of facility location

<!-- b001609 | prose | pages [47] -->
of emergency rescue”, MANAGEMENT SCIENCES IN CHINA(2006).

<!-- b001610 | prose | pages [47] -->
[7] PANG Hai-yun, LIU Nan, WU Qiao, “Decision-making model for transportation

<!-- b001611 | prose | pages [47] -->
and distribution of emergency materials and its modified particle swarm optimization

<!-- b001612 | prose | pages [47] -->
algorithm” Control and Decision(2012).

<!-- b001613 | prose | pages [47] -->
[8] ZHU Jian-ming, HUANG Jun,” Randomized Algorithm for Vehicle Routing

<!-- b001614 | prose | pages [47] -->
Model for Medical Supplies  in Large-Scale Emergencies”, OPERATIONS

<!-- b001615 | prose | pages [47] -->
RESEARCH AND MANAGEMENT SCIENCE(2010).

<!-- b001616 | prose | pages [47] -->
[9] Liu Fang, “A brief introduction to the U.S. Strategic National Stockpile”, Mil Med

<!-- b001617 | prose | pages [47] -->
Sci. Vol 38, No.11, 2014.

<!-- b001618 | prose | pages [47] -->
[10] http://maps.who.int/MapJournal/?appid=5b29178821dd4584b78dcb18d280326a

<!-- b001619 | prose | pages [47] -->
[11] Gu Yong, ”Based on the mechanism of the prevention and control infectious

<!-- b001620 | prose | pages [47] -->
disease emergency supplies demand analysis”, Journal of Wuhan University of

<!-- b001621 | prose | pages [47] -->
Technology, 2010.

<!-- b001622 | furniture | pages [47] -->

