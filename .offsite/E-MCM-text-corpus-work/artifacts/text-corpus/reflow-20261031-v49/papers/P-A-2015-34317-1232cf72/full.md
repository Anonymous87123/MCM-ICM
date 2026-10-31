# P-A-2015-34317-1232cf72

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Team Control Number

<!-- b000002 | front_matter | pages [1] -->
34317

<!-- b000003 | front_matter | pages [1] -->
For office use only For office use only

<!-- b000004 | front_matter | pages [1] -->
T1 ________________ F1 ________________

<!-- b000005 | front_matter | pages [1] -->
T2 ________________ F2 ________________

<!-- b000006 | front_matter | pages [1] -->
T3 ________________ F3 ________________ Problem Chosen T4 ________________ F4 ________________

<!-- b000007 | front_matter | pages [1] -->
A

<!-- b000008 | heading | pages [1] -->
Summary

<!-- b000009 | prose | pages [1] -->
“Ebola is a major global crisis that demands a massive and immediate global response. No country or organization can defeat Ebola alone.”

<!-- b000010 | prose | pages [1] -->
—— H.E. Ban Ki-moon, the UN Secretary-General.

<!-- b000011 | prose | pages [1] -->
As a number of Global Village, we do our best to help eradicate Ebola.

<!-- b000012 | prose | pages [1] -->
First, we develop a stage-structured model of Ebola Propagation. In the model, we consider the susceptible, the exposed, the infected whose disease is not advanced, the infected whose disease is serious, the removed and the dead. The model is good at predicting near future cases’ number but fails in predicting far future cases’ number. Then we take hospital into consideration and add 7 more parameters, then we do simulation once again. Finally, we get a better result that the model well predicts the future cases. For example, the model predicts there are 4000 total cases and 2500 death cases in Guinea, 9509 total cases and 4166 death cases in Liberia, 12556 total cases and 3933 death cases in Sierra Leone up to April,1st, 2015.

<!-- b000013 | prose | pages [1] -->
Second, we determine the locations of delivery. We invoke clustering method to divide the most serious region, namely, West Africa into three parts, Guinea, Liberia and Sierra Leone. According to locations of provincial capital, we use clustering method once again to divide a country into several clusters. Then we adopt P-Center Method to determine a location of delivery in each cluster. We find there are two kinds of ways to choose. One is one-way route and the other is circular route. As for one-way route, we think it is time-consuming and energy-consuming. So we decide to use circular route. The circular route, in some ways, is a little bit similar to TSP problem, we use mix integer programming to find an optimal circular route by Lingo Software and each location of delivery has two optimal circular routes. The result is that there are 3 locations of delivery in Guinea, 1 location of delivery in Liberia and 1 location of delivery in Sierra Leone.

<!-- b000014 | prose | pages [1] -->
Third, we know from the stage-structured model that Ebola cannot stop spreading by itself. Since we are going to eradicate Ebola, we must use medicine and vaccine to stop Ebola. Medicine mainly influences the number of the susceptible while vaccine mainly influences the number of the infected whose disease is not advanced, in this way, we can eradicate Ebola. As for speed of manufacturing, we consider there is a linear equation between the speed and time because the amount of medicine is too rare to meet the requirement of patients. And this situation continues until the requirement is met. We can calculate the speed by the parameter in the linear equation. And we allocate medicine to different places by ratio of the infected number in that place to the number in three West African countries. Thus, we successfully stop Ebola from spreading.

<!-- b000015 | keywords | pages [1] -->
Keywords:  SEIIRF Model   TSP Model   Clustering Method    Ebola Evaluating

<!-- b000016 | contents | pages [2] -->
A BATTLE WITHOUT GUN AND SMOKE

<!-- b000017 | contents | pages [2] -->
———— THE CONFRONTATION WITH EBOLA

<!-- b000018 | heading | pages [2] -->
Content

<!-- b000019 | contents | pages [2] -->
Ⅰ Introduction ............................................................................................................. 1

<!-- b000020 | contents | pages [2] -->
1.1 Aims are Changing now .................................................................................. 1

<!-- b000021 | contents | pages [2] -->
1.2 Our Understanding of the Words .................................................................... 1

<!-- b000022 | contents | pages [2] -->
1.3 Decompose the Problem and Our Tasks ......................................................... 2

<!-- b000023 | contents | pages [2] -->
Ⅱ Background – Behavior Change is Key to the Eradication of Ebola ...................... 3

<!-- b000024 | contents | pages [2] -->
Ⅲ Assumptions And Justifications .............................................................................. 4

<!-- b000025 | contents | pages [2] -->
Ⅳ SEIIRF Model for Ebola propagation ..................................................................... 4

<!-- b000026 | contents | pages [2] -->
4.1 Introduction ..................................................................................................... 4

<!-- b000027 | contents | pages [2] -->
4.2 Symbols and Definitions ................................................................................. 5

<!-- b000028 | contents | pages [2] -->
4.3 Construction of the Model .............................................................................. 6

<!-- b000029 | contents | pages [2] -->
4.4 Results are Not So Reasonable ....................................................................... 8

<!-- b000030 | contents | pages [2] -->
4.5 Refresh the Values of Parameters.................................................................... 8

<!-- b000031 | contents | pages [2] -->
4.6 Advanced Model ........................................................................................... 10

<!-- b000032 | contents | pages [2] -->
4.7 Results are Reasonable ................................................................................. 13

<!-- b000033 | contents | pages [2] -->
4.8 Prediction of the Future ................................................................................ 14

<!-- b000034 | contents | pages [2] -->
Ⅴ Model of Locations of Delivery ............................................................................ 18

<!-- b000035 | contents | pages [2] -->
5.1 What is Emergency Supplies ........................................................................ 18

<!-- b000036 | contents | pages [2] -->
5.2 Assumptions and Justifications ..................................................................... 19

<!-- b000037 | contents | pages [2] -->
5.3 Clustering Method, A Way to Determine Regions for Medicine Delivery ... 20

<!-- b000038 | contents | pages [2] -->
5.4 Results of Clustering Method ....................................................................... 21

<!-- b000039 | contents | pages [2] -->
5.5 Principle of Fairness ..................................................................................... 22

<!-- b000040 | contents | pages [2] -->
5.6 Principle of Efficiency .................................................................................. 22

<!-- b000041 | contents | pages [2] -->
5.7 Determine Delivery Locations in the Three West African Countries ........... 23

<!-- b000042 | contents | pages [2] -->
Ⅵ Model of Delivery System .................................................................................... 23

<!-- b000043 | contents | pages [3] -->
6.1 Introduction ................................................................................................... 23

<!-- b000044 | contents | pages [3] -->
6.2 Symbols and Definitions ............................................................................... 24

<!-- b000045 | contents | pages [3] -->
6.3 TSP Model – Well-Planned Routes ............................................................... 24

<!-- b000046 | contents | pages [3] -->
6.4 Daily Demand for Medicine ......................................................................... 25

<!-- b000047 | contents | pages [3] -->
Ⅶ Model Implementation of three Countries ............................................................ 26

<!-- b000048 | contents | pages [3] -->
7.1General algorithm .......................................................................................... 26

<!-- b000049 | contents | pages [3] -->
7.2 Application of Algorithm .............................................................................. 27

<!-- b000050 | contents | pages [3] -->
7.2.1 Application in Guinea ........................................................................ 27

<!-- b000051 | contents | pages [3] -->
7.2.2 Application in Liberia ........................................................................ 29

<!-- b000052 | contents | pages [3] -->
7.2.3 Sierra Leone ....................................................................................... 30

<!-- b000053 | contents | pages [3] -->
Ⅷ Model of the Quantity of the Medicine Needed and Manufacturing Speed ......... 31

<!-- b000054 | contents | pages [3] -->
8.1 Introduction ................................................................................................... 31

<!-- b000055 | contents | pages [3] -->
8.2 Assumptions and Justifications ..................................................................... 32

<!-- b000056 | contents | pages [3] -->
8.3 symbols and definitions ................................................................................ 32

<!-- b000057 | contents | pages [3] -->
8.4 How Fast Need We Produce Medicine and Vaccine ..................................... 32

<!-- b000058 | contents | pages [3] -->
8.5 The Quantity of the Medicine Needed .......................................................... 35

<!-- b000059 | contents | pages [3] -->
Ⅸ Other Factors We Think Are Important ................................................................ 35

<!-- b000060 | contents | pages [3] -->
Ⅹ Extension of Models ............................................................................................. 36

<!-- b000061 | contents | pages [3] -->
10.1 Optimization of Coverage to Determine Delivery Locations ..................... 36

<!-- b000062 | contents | pages [3] -->
10.2 A No-boundary Scheme .............................................................................. 37

<!-- b000063 | contents | pages [3] -->
Ⅺ Sensitivity analysis................................................................................................ 38

<!-- b000064 | contents | pages [3] -->
11.1 Sensitivity Analysis of SEIIRF Model ........................................................ 38

<!-- b000065 | contents | pages [3] -->
11.2 Sensitivity Analysis of Model of the Speed to Produce Medicine .............. 39

<!-- b000066 | contents | pages [3] -->
Ⅻ Conclusion ............................................................................................................ 40

<!-- b000067 | contents | pages [3] -->
11.1 Strengths and Weaknesses ........................................................................... 40

<!-- b000068 | contents | pages [3] -->
11.2 Overall Results ............................................................................................ 41

<!-- b000069 | furniture | pages [4] -->
Team # 34317                                                                Page 1 of 44

<!-- b000070 | heading | pages [4] -->
Ⅰ Introduction

<!-- b000071 | prose | pages [4] -->
Ebola, a familiar but strange word to us. When the Ebola virus out broke in West Africa and caused plenty of deaths, no one would imagine the disastrous scene without mercy. And, of course, no one believes the word ‘Ebola’ just originated from a peaceful and beautiful river – Ebola River in Congo. Contrary to its attracting meaning, it is true that the Ebola virus do take lots of victims’ lives away. Countries all over the world, thus, have taken strategies, more specifically, distribute health works to disease-torn countries, speed up the development of medicine and establish feasible delivery systems to contain Ebola propagation.

<!-- b000072 | prose | pages [4] -->
1.1 Aims are changing now

<!-- b000073 | prose | pages [4] -->
The battle against Ebola will cost us heavily for sure, but human beings are not easily defeated. Although Ebola virus is fatal, we have methods. The WMA (World Medical Association) has announced that they have developed medicine to cure Ebola. At one level, the medicine is a milestone for us human beings in fighting Ebola, but at another it is the result of human nature. We know calling the command center to take away the sick is equally hard. It is our duty, in the interests of our own and the public good, to pick up the phone, but the reality is that, if we do, we may never hug our sister again. We can visit her in the treatment center and talk across two fences. The fortunate will be reunited. For the rest, the future is the body bag.[1] Ebola will not end without the medicine. Thanks to appearance of the medicine, we are gradually going out of confusion and turning to fight back in this smokeless battle. Many previous articles that mainly focus on how Ebola propagation or how difficult to contain Ebola are now may less important than those on how to effectively delivery medicine to most-need regions like West Africa. Accurate location with effective medicine – Ebola’s doomsday and we do our job to make it come true – considering propagation process, medicine needed, delivery systems, locations of delivery and manufacturing speed of vaccine or drug and so on.

<!-- b000074 | heading | pages [4] -->
1.2 Our understanding of the words

<!-- b000075 | prose | pages [4] -->
The problem requires us to de several jobs to evaluate Ebola. We think it is necessary for us to come to an understanding of some words in the problem.

<!-- b000076 | prose | pages [4] -->
Spread of the Disease: We consider this sub-problem as a requirement to analyze Ebola propagation process and predict future cases, including total cases and death cases in the three West African countries and what influence that new medicine will bring to us. As for Ebola cases in other countries, such as in the United States or in The United Kingdom, good health condition and developed facilities can contain the cases well, so in this paper, we mainly discuss Ebola cases in West Africa.

<!-- b000077 | furniture | pages [5] -->
Team # 34317                                                                Page 2 of 44

<!-- b000078 | prose | pages [5] -->
Locations of Delivery: How to understand the word ‘locations’ is the key to this sub-problem. We also have some criteria to choose ‘locations’ – easy to deliver medicine, cover most people or environment-friendly to build? Here, we regard ‘locations’ as places that have features of easy and time-saving in medicine delivering, being equal to all people in a region.

<!-- b000079 | prose | pages [5] -->
Possible Feasible Delivery Systems: We think this sub-problem needs us to design a route that can not only cover all places which are in need of medicine but also provide vehicles a fastest way to send medicine. Besides, delivery systems can allocate medicine to different places properly.

<!-- b000080 | prose | pages [5] -->
The Quantity of the Medicine Needed: There are several understandings of the word ‘quantity’, like amount of medicine to cure all Ebola patients or amount of medicine needed every day to keep serious patients from dying. Our understanding of this word is the total amount of medicine needed to cure patients whose disease is not advanced until there is no more patients appear. So it is a dynamic and time-varying number until cases stops increasing.

<!-- b000081 | prose | pages [5] -->
Speed of manufacturing of the vaccine or medicine: In our opinion, this sub-problem needs us to decide how fast a factory have to produce medicine when amount of medicine is too rare to cure patients and what changes a factory should obey when there is enough medicine for patients. As for vaccine, we consider it is similar to medicine.

<!-- b000082 | prose | pages [5] -->
Other factors: Something we forget to consider in our model but also important for Ebola evaluating. We will find them during the process of establishing models

<!-- b000083 | heading | pages [5] -->
1.3 Decompose the Problem and Our Tasks

<!-- b000084 | prose | pages [5] -->
To totally understand the problem better and know what we should to deal with Ebola, decompose it is needed to us. According to the steps needed in process of achieving our goal that accurate location with effective medicine, we deem the problem ‘Eradicating Ebola’ can be divided into five parts:

<!-- b000085 | prose | pages [5] -->
Propagation mechanism of Ebola virus.

<!-- b000086 | prose | pages [5] -->
Accurate locations for medicine to be delivered like disease-torn countries in West Africa.

<!-- b000087 | prose | pages [5] -->
Effective transportation including amount of medicine needed in a place.

<!-- b000088 | prose | pages [5] -->
Total amount of medicine needed to cure Ebola patients until cases stops increasing.

<!-- b000089 | furniture | pages [6] -->
Team # 34317                                                                Page 3 of 44

<!-- b000090 | prose | pages [6] -->
Vaccine or drug manufacturing speed

<!-- b000091 | prose | pages [6] -->
When the problem is unequivocal, we start to make it clear that what we need to do and how to do it. Since we have separated the problem into parts, we can deal with these parts one by one. Here the problem requires us do and our tasks are:

<!-- b000092 | prose | pages [6] -->
 Build a model to reflect the condition we face now and make prediction of the future if medicine or hospital or other factors play roles in Ebola propagation process.

<!-- b000093 | prose | pages [6] -->
 Find some best delivery places according to our own understanding of word ‘locations’

<!-- b000094 | prose | pages [6] -->
 Design a delivery system both good in medicine transportation and medicine allocation.

<!-- b000095 | prose | pages [6] -->
 Speed to produce medicine and total quantity needed to eradicate Ebola

<!-- b000096 | prose | pages [6] -->
 Other critical factors we consider important to optimize the eradication of Ebola

<!-- b000097 | prose | pages [6] -->
Ⅱ Background – Behavior Change is Key to the

<!-- b000098 | prose | pages [6] -->
Eradication of Ebola

<!-- b000099 | prose | pages [6] -->
As the number of Ebola cases and deaths grows in West Africa, many remain unaware of its deadly impact, causes and treatment options, or lack thereof. Let people know the harm of the diseases is of great importance both in the developing world and, more specifically, on the African continent.

<!-- b000100 | prose | pages [6] -->
Unfortunately, in remote districts of these three African countries – Guinea, Liberia and Sierra Leone few of the local have heard Google or ABC News or other TV media and say nothing of getting access of the newest Ebola news. Once the people who are seeing their family members get sick and die tend to believe an invisible killer who are from hell. Getting correct information about Ebola prevention and treatment to local communities throughout West Africa must become a higher priority, and we must begin to address it in culturally appropriate and innovative ways.[2]

<!-- b000101 | prose | pages [6, 7] -->
Besides, human nature is another factor of Ebola spreading unimpededly, though great efforts have been made to find and quarantine Ebola patients. Like we introduced in Instruction, although talk of changing behavior is easy, when we think about the sort of behavior that needs to change, we realize it’s very hard. How many of us could bear to watch our mother die without holding her hand, and then allow her body to be sprayed with chlorine, removed in a double body bag from the house, be loaded on to the back of a pick-up truck with several others, and taken to the cemetery for rapid interment with little more than a cursory prayer?[1]

<!-- b000102 | furniture | pages [7] -->
Team # 34317                                                                Page 4 of 44

<!-- b000104 | prose | pages [7] -->
We must have to realize that change awareness and human nature is quite hard. The most effective way is to find medicine if we want to win the battle against Ebola. Here is the time for medicine cure – the WMA have announced that they could.

<!-- b000105 | heading | pages [7] -->
Ⅲ Assumptions And Justifications

<!-- b000106 | prose | pages [7] -->
①Overlook the changing of population caused by natural birth rate and death

<!-- b000107 | prose | pages [7] -->
rate.

<!-- b000108 | prose | pages [7] -->
Compared to the influence of Ebola to the population, natural birth rate and death rate

<!-- b000109 | prose | pages [7] -->
have little impact. Also, the total natural growth of number of population is not large

<!-- b000110 | prose | pages [7] -->
in the period of the spread.

<!-- b000111 | prose | pages [7] -->
②There is no population flow among areas.

<!-- b000112 | prose | pages [7] -->
Since the outbreak of Ebola, the immigration among different districts and countries

<!-- b000113 | prose | pages [7] -->
play a role can be ignored in terms of the change of the population. In addition, the

<!-- b000114 | prose | pages [7] -->
flow rate of people may decrease in case of the infection of disease.

<!-- b000115 | prose | pages [7] -->
We list more and detailed assumptions in the following section when using them.

<!-- b000116 | heading | pages [7] -->
Ⅳ SEIIRF model for Ebola propagation

<!-- b000117 | heading | pages [7] -->
4.1 Introduction

<!-- b000118 | prose | pages [7, 8] -->
The ongoing Ebola outbreak surprises us both in size and complexity. At the very beginning of 2015, many scientists and other people, like us students, are still fighting against Ebola in different ways, such as developing medicine, propagating health care and predicting the spread of Ebola. In this section, we apply SEIIRF Model to evaluate the spread of Ebola. Thanks to a previous article [5], we can use this model appropriately, however, as time goes by, values of parameters stated in that article may not convinced enough anymore for that article just used data from October,2014 to November, 2014 to calculate values of parameters and then tested the model with data in December, 2014. If we still use the values of parameters in that article, we find it is far from accuracy of data in January, 2015. So we find a method – Genetic Algorithm to refresh the value of parameters by using data from October, 2014 to December, 2014 and the renewed SEIIRF Model well fits the data of January 1st, 2015 to February 3rd, 2015.

<!-- b000119 | furniture | pages [8] -->
Team # 34317                                                                Page 5 of 44

<!-- b000121 | heading | pages [8] -->
4.2 Symbols and Definitions

<!-- b000122 | prose | pages [8] -->
There are some symbols appear in the model. We show them below:

<!-- b000123 | caption | pages [8] -->
table4.1: symbols in the model

<!-- b000124 | heading | pages [8] -->
SYMBOL

<!-- b000125 | prose | pages [8] -->
DEFINITION UNITS

<!-- b000126 | prose | pages [8] -->
Transmission Parameter For First Stage Of Illness (Not  -1 -1 people days 1 In Hospital)

<!-- b000127 | prose | pages [8] -->
 Ratio Of Infectiveness In First Vs. Second Of Stage Of 2 Unitless  Illness (Not In Hospital) 1

<!-- b000128 | prose | pages [8] -->
 Ratio Of Infectiveness In First F Unitless  Stage Vs. Funeral Transmission (Not In Hospital) 1

<!-- b000129 | prose | pages [8] -->
 1 Average Incubation Period Days

<!-- b000130 | prose | pages [8] -->
1 1 Length Of First Stage Of Illness (Not In Hospital) Days

<!-- b000131 | prose | pages [8] -->
 1 Length Of Second Stage Of Illness (Not In Hospital) Days 2

<!-- b000132 | prose | pages [8] -->
  1 Time From Death Until Burial Days F

<!-- b000133 | prose | pages [8] -->
 Overall Mortality Rate (Fraction) (Not In Hospital) Unitless 1 2

<!-- b000134 | prose | pages [8] -->
Mortality Rate (Fraction) Among Those In Second  Unitless 2 Stage Of Illness (Not In Hospital)

<!-- b000135 | furniture | pages [9] -->
Team # 34317                                                                Page 6 of 44

<!-- b000136 | heading | pages [9] -->
4.3 Construction of the Model

<!-- b000137 | prose | pages [9] -->
To adequately reflect the propagation of Ebola and transmission of Ebola, we should take real conditions in life into consideration.

<!-- b000138 | prose | pages [9] -->
To begin with, we show our model as a form of figure.

<!-- b000139 | prose | pages [9] -->
S E I1 I2 F

<!-- b000140 | prose | pages [9] -->
R

<!-- b000141 | caption | pages [9] -->
figure 4.1: Stage-Structured Model of Ebola propagation

<!-- b000142 | prose | pages [9] -->
We can get information from the figure 4.1. There are six stages in the whole propagation of Ebola. We also call this model as Stage-Structured Model,

<!-- b000143 | prose | pages [9] -->
S represents the fraction of the population which is susceptible.

<!-- b000144 | prose | pages [9] -->
E represents the fraction of the population which is exposed.

<!-- b000145 | prose | pages [9] -->
1I represents the fraction of the population which is infected and remain in first

<!-- b000146 | prose | pages [9] -->
stage (such as fever, headache, sore throat, muscle aches and other milder symptoms which often progress to diarrhea and vomiting).

<!-- b000147 | prose | pages [9] -->
2I represents the fraction of the population which is infected and deteriorate to

<!-- b000148 | prose | pages [9] -->
second stage (such as hemorrhaging and multi-organ failure).

<!-- b000149 | prose | pages [9] -->
R represents the fraction of the population which is recovered. And

<!-- b000150 | prose | pages [9] -->
F represents the fraction of the population who have died and are in the process of being buried.

<!-- b000151 | furniture | pages [10] -->
Team # 34317                                                                Page 7 of 44

<!-- b000152 | prose | pages [10] -->
The corresponding equations of Figure 4.1 are

<!-- b000153 | prose | pages [10] -->
 dS       ( I I F S )  I 1 2 2 F dt  dE          ( I I F S ) E  I 1 2 2 F dt  dI      1 E I  1 1 dt dI      2 I I  1 1 1 2 2 dt  dF      I F 2 2 2 F  dt  dR        (1 ) I (1 ) I 1 1 1 2 2 2 dt

<!-- b000154 | prose | pages [10] -->
In the equations we consider the infected ( 1I and 2I ) and the dead ( F ) all have

<!-- b000155 | prose | pages [10] -->
ability to infect the susceptible. In fact, when our relatives get sick, we still contact with the in daily life, and it is not surprise for us to think that human nature play an important role in Ebola propagation – just as we have talked in introduction. How many of us could bear to watch our mother die without holding her hand, and then allow her body to be sprayed with chlorine, removed in a double body bag from the house, be loaded on to the back of a pick-up truck with several others, and taken to the cemetery for rapid interment with little more than a cursory prayer? Moreover, the

<!-- b000156 | prose | pages [10] -->
     exposed E are mainly form the susceptible ( I I F S ) and then have I 1 2 2 F

<!-- b000157 | prose | pages [10] -->
 chances to turn to first stage if they show symptoms ( E ). And number of people in

<!-- b000158 | prose | pages [10] -->
  first stage 1I are mainly from the exposed ( E ) and then part of them ( 1 1 1I ) turn

<!-- b000159 | prose | pages [10] -->
  to second stage and the rest of them (1 ) I get recovered. Thus number of 1 1 1

<!-- b000160 | prose | pages [10] -->
 people in second stage are mainly from first stage ( 1 1 1I ) and some of them die. So

<!-- b000161 | prose | pages [10] -->
  the dead is the result of people ( 2 2I ) in second stage and their bodies ( FF ) exist 2

<!-- b000162 | prose | pages [10] -->
until being buried.

<!-- b000163 | prose | pages [10] -->
Then, to measure the total cases and death cases of Ebola, We invoke

<!-- b000164 | prose | pages [10, 11] -->
t    y E (t) dt C 0 t    y I (t) dt D 2 2 2 0 In these equations, y means total cases (or cumulate cases) and y means C D

<!-- b000165 | furniture | pages [11] -->
Team # 34317                                                                Page 8 of 44

<!-- b000167 | prose | pages [11] -->
 death cases. And means number of people begin to get sick and have E (t)

<!-- b000168 | prose | pages [11] -->
  symptoms so y is the time integral of . While 2 2(t) I is number of people E (t) C

<!-- b000169 | prose | pages [11] -->
 who no longer in second stage anymore, means number of dead people. So 2 2(t) I 2

<!-- b000170 | prose | pages [11] -->
 y is the time integral of 2 2(t) I . D 2

<!-- b000171 | prose | pages [11] -->
4.4 Results are Not So Reasonable

<!-- b000172 | prose | pages [11] -->
The article[5] adopts Least Square Method to figure out values of parameters. Unfortunately, under the values of parameters, although the calculated curve fits quite well to real data in Guinea from October 1st, 2014 to December 31st, 2014, we fail to fit the calculated curve well to real data in Guinea when time reaches on January 1st, 2015, namely, the values of parameters in that article may ‘outdated’. So we do not show them here because they are not worthy enough.

<!-- b000173 | prose | pages [11] -->
So, we adopt genetic algorithm combined with least square method to calculate our new values of parameters.

<!-- b000174 | heading | pages [11] -->
4.5 Refresh the Values of Parameters

<!-- b000175 | prose | pages [11, 12] -->
Genetic algorithm combined with least square method is used by us to find out new parameters values. Here flow diagram of Genetic algorithm is START

<!-- b000176 | furniture | pages [12] -->
Team # 34317                                                                Page 9 of 44

<!-- b000178 | prose | pages [12] -->
 PARAMETER INITIALIZATION X X 0

<!-- b000179 | prose | pages [12] -->
 CALCULATE FITNESS f F (X)

<!-- b000180 | prose | pages [12] -->
GENETIC

<!-- b000181 | prose | pages [12] -->
N>Nf

<!-- b000182 | prose | pages [12] -->
OUTPUT OPTIMAL

<!-- b000183 | prose | pages [12] -->
END

<!-- b000184 | caption | pages [12] -->
figure4.2: flow chart of Genetic Algorithm combined with least square method

<!-- b000185 | prose | pages [12] -->
        In the flow diagram, de define X , / , / , , , , , , and 1 2 1 F 1 1 2 F 1 2 2

<!-- b000186 | prose | pages [12] -->
       fitness . Where ct is length of f F (X) [ y ( ) t C t ( )] [ y ( ) t D t ( )] C 0 D 0   t t t t c c

<!-- b000187 | prose | pages [12] -->
time from October 1st, 2014 to December 31st, 2014. And C t denotes real total 0( )

<!-- b000188 | prose | pages [12] -->
ct while D t denotes real 0( ) cases in a country updated every day within time length

<!-- b000189 | prose | pages [12] -->
death cases in a country updated every day within time length ct .

<!-- b000190 | prose | pages [12, 13] -->
By now, we have method to find each parameter’s value by using data from October, 2014 to December, 2014. Then we use these new values to calculate a curve to fit real data in Guinea.

<!-- b000191 | furniture | pages [13] -->
Team # 34317                                                                Page 10 of 44

<!-- b000193 | prose | pages [13] -->
Here the results are:

<!-- b000194 | caption | pages [13] -->
figure4.3: test of the calculated curves

<!-- b000195 | prose | pages [13] -->
We can see from the figures 4.3 that in about first 90 days, namely, date from Oct.1st, 2014 to Dec.31st, 2014, the model fits well to the real data of Guinea from

<!-- b000196 | prose | pages [13] -->
WHO website. Both y and y reflect accurate number of cases, respectively. C D

<!-- b000197 | prose | pages [13] -->
However, as New Year begins, real data has tendency of becoming less rapidly increasing while our prediction is out of accuracy although our curve is much better than that calculated in the article we refer to. We do not use this curve to predict cases in Liberia and Sierra Leone.

<!-- b000198 | heading | pages [13] -->
4.6 Advanced Model

<!-- b000199 | prose | pages [13] -->
After refreshing the values of parameters, we are still not satisfied with the curve we calculate. Data talks, we should try our best to make our model considerable. To improve the model we discussed in former section, we not only use more data from WHO website to calculate our parameters, but also consider other factors impact on Ebola spreading, like additional parameters and changing of parameters’ values if people receive treatment or get infected in hospital. There is a pie chart showing the proportion of getting infected in different ways (data of Sierra Leone).

<!-- b000200 | furniture | pages [14] -->
Team # 34317                                                                Page 11 of 44

<!-- b000201 | caption | pages [14] -->
figure4.4: pie chart proportion of getting infected in different ways

<!-- b000202 | prose | pages [14] -->
There are 17.6% of healthy people in Sierra Leone get Ebola because of hospital. it is a factor important enough for us to take it into consideration when we evaluate Ebola propagation.

<!-- b000203 | prose | pages [14] -->
First, let us get an accessible way to additional parameters and their meanings in this advanced model.

<!-- b000204 | caption | pages [14] -->
table4.2: additional parameters and meanings in this advanced model

<!-- b000205 | heading | pages [14] -->
SYMBOL

<!-- b000206 | prose | pages [14] -->
DEFINITION UNITS

<!-- b000207 | prose | pages [14] -->
Transmission Parameter For First Stage Of Illness (In  -1 -1 people days 1 H Hospital)

<!-- b000208 | prose | pages [14] -->
Transmission Parameter For Second Stage Of Illness (In  -1 -1 people days 2 H Hospital)

<!-- b000209 | prose | pages [14] -->
Length Of First Stage Of Illness (From Moment Of 1h  1 Days Symptoms Appearing To Go To Hospital)

<!-- b000210 | prose | pages [14] -->
Length Of Second Stage Of Illness (From Moment Of 2h  1 Days Symptoms Appearing To Go To Hospital)

<!-- b000211 | prose | pages [14] -->
3y  1 Length Of First Stage Of Illness (In Hospital) Days

<!-- b000212 | prose | pages [14] -->
4y  1 Length Of Second Stage Of Illness (In Hospital) Days

<!-- b000213 | prose | pages [14] -->
 Overall Mortality Rate (Fraction) (In Hospital) Unitless 1 H 2 H

<!-- b000214 | prose | pages [14, 15] -->
Mortality Rate (Fraction) Among Those In Second Stage Of  Unitless 2H Illness (In Hospital) The reason why we add these parameters is that if hospital plays a role in people’s daily life, people will have another access to cure Ebola. When people feel

<!-- b000215 | furniture | pages [15] -->
Team # 34317                                                                Page 12 of 44

<!-- b000217 | prose | pages [15] -->
1h , 2h , 1 1 uncomfortable, they may choose to go to hospital for doctors’ help. Thus,

<!-- b000218 | prose | pages [15] -->
3y  and 4y  are generated to denote different length of time in or not in hospital. 1 1

<!-- b000219 | prose | pages [15] -->
, ,   By the way, and are introduced to explain the model 1 H 2 H 1 H 2 H 2H

<!-- b000220 | prose | pages [15] -->
more considerably.

<!-- b000221 | prose | pages [15] -->
We show our advanced model as a form of figure

<!-- b000222 | prose | pages [15] -->
S E I1 I2

<!-- b000223 | prose | pages [15] -->
R F

<!-- b000224 | prose | pages [15] -->
H1 H2

<!-- b000225 | caption | pages [15] -->
figure4.5: advanced stage-structured model of ebola propagation

<!-- b000226 | prose | pages [15] -->
The advanced equations of this model are  dS           [ ( I H ) ( I H ) F S ]  I 1 H 1 2 2 H 2 F dt  dE              [ ( I H ) ( I H ) F S ] E  I 1 H 1 2 2 H 2 F dt  dI       E I h I 1 1 1 1 1  dt  dI       2 I I h I 1 1 1 2 2 2 2 dt dH     1 h I H  1 1 3 1 dt  dH        2 h I H H 2 2 1 H 3 1 4 2  dt  dF         I H F 2 2 2 2 H 4 2 F dt   dR               (1 ) I (1 ) I (1 ) H (1 ) H  1 1 1 2 2 2 1 H 3 1 2 H 4 2 dt

<!-- b000227 | prose | pages [15, 16] -->
Where H and H mean number of people in hospital who are in first stage and 1 2 in second stage, respectively. While 1I , 2I mean the number of people not in

<!-- b000228 | furniture | pages [16] -->
Team # 34317                                                                Page 13 of 44

<!-- b000230 | prose | pages [16] -->
hospital who are in first stage and in second stage, respectively. And S , E , F and R have the same meanings as we talked before.

<!-- b000231 | prose | pages [16] -->
In this group of equations, the susceptible are not only vulnerable to the sick

<!-- b000232 | prose | pages [16] -->
   outside ( or ), but also to the patients in hospital ( or I I S 2I S H H S 1 2 1 1

<!-- b000233 | prose | pages [16] -->
 H H S ). Different from what we explained in 3.4, the infected who are in first 2 2

<!-- b000234 | prose | pages [16] -->
stage have another way to go – hospital ( h I ). And the infected who are in second 1 1

<!-- b000235 | prose | pages [16] -->
stage do ( h I ), too. For the infected in hospital, they may die or recover. 2 2

<!-- b000236 | prose | pages [16] -->
4.7 Results are Reasonable

<!-- b000237 | prose | pages [16] -->
First, we should better to find additional parameters’ values. Similarly, we use genetic algorithm combined with least square method that we have introduced above to calculate values. But there is a little difference at this moment is that            X , / , / , , , , , , , , h h , , , , , . 1 2 1 F 1 1 2 F 1 2 2 H 1 2 3 4 1 H 2 H

<!-- b000238 | prose | pages [16] -->
We calculate all parameters in Guinea are:

<!-- b000239 | caption | pages [16] -->
table4.3: all parameters in Guinea

<!-- b000240 | prose | pages [16] -->
PARAMETER VALUE PARAMETER VALUE

<!-- b000241 | prose | pages [16] -->
 1 0.04 0.26 1

<!-- b000242 | prose | pages [16] -->
   / 2.37 0.48 2 1 H

<!-- b000243 | prose | pages [16] -->
  / 1h 1.27 0.43 F 1

<!-- b000244 | prose | pages [16] -->
 2h 0.42 0.55

<!-- b000245 | prose | pages [16] -->
  0.19 0.20 1 2 3

<!-- b000246 | prose | pages [16] -->
  0.58 0.11 2 4

<!-- b000247 | prose | pages [16] -->
  0.46 0.49 F 1H

<!-- b000248 | prose | pages [16, 17] -->
  0.70 0.81 2 2H And curves in Guinea are :

<!-- b000249 | furniture | pages [17] -->
Team # 34317                                                                Page 14 of 44

<!-- b000251 | caption | pages [17] -->
figure 4.6: Test of Calculated Curves (Guinea)

<!-- b000252 | prose | pages [17] -->
We can see from the figure 4.6, our curves fit much better if we take hospital into consideration and add more parameters than the article we refer to. The curves can fit real data from January 1st, 2015 to February 3rd, 2015 in Guinea both in total cases and death cases. So we trust these two curves.

<!-- b000253 | heading | pages [17] -->
4.8 Prediction of the Future

<!-- b000254 | prose | pages [17] -->
Since we have found curves to fit real data well, our next job is to use the curves to predict number of total cases and death cases in Guinea in the near future. We draw a figure based on the figures that we have showed above. We lengthen the time axis to predict future cases until end of April, 2015.

<!-- b000255 | furniture | pages [18] -->
Team # 34317                                                                Page 15 of 44

<!-- b000256 | caption | pages [18] -->
figure 4.7: prediction of future cases in Guinea

<!-- b000257 | prose | pages [18] -->
From the figure 4.7, the curves deliver us information about Guinea that number of total cases and death cases is still growing, and total cases grow a little bit faster than death cases grow. Number of total cases will reach to nearly 4000 after 180 days and death cases will reach to about 2500 after 180 days. However, number of cases is much less than a condition without hospital and medicine (see figure 4.7). After all, we just have medicine to cure Ebola patients whose disease is not advanced. As for serious patients, the only endeavor we can do is supportive treatment and pray.

<!-- b000258 | prose | pages [18] -->
Besides, we calculate parameters and curves of Liberia and Sierra Leone, we see curves also fit well to real data.

<!-- b000259 | furniture | pages [19] -->
Team # 34317                                                                Page 16 of 44

<!-- b000260 | prose | pages [19] -->
The parameters of Liberia:

<!-- b000261 | caption | pages [19] -->
table4.4: parameters of Liberia

<!-- b000262 | prose | pages [19] -->
PARAMETER VALUE PARAMETER VALUE

<!-- b000263 | prose | pages [19] -->
 1 0.19 0.28 1

<!-- b000264 | prose | pages [19] -->
   / 2.06 0.23 2 1 H

<!-- b000265 | prose | pages [19] -->
  / 1h 1.97 0.44 F 1

<!-- b000266 | prose | pages [19] -->
 2h 0.45 0.73

<!-- b000267 | prose | pages [19] -->
  0.18 0.12 1 2 3

<!-- b000268 | prose | pages [19] -->
  0.63 0.84 2 4

<!-- b000269 | prose | pages [19] -->
  0.46 0.31 F 1H

<!-- b000270 | prose | pages [19] -->
  0.92 0.79 2 2H

<!-- b000271 | prose | pages [19] -->
The curves of Liberia:

<!-- b000272 | caption | pages [19] -->
figure4.8: Test of Calculated Curves (Liberia)

<!-- b000273 | prose | pages [19] -->
We can see from the figure 4.8 that curves also fit well to real data of Liberia.

<!-- b000274 | furniture | pages [20] -->
Team # 34317                                                                Page 17 of 44

<!-- b000275 | prose | pages [20] -->
The parameters Sierra Leone:

<!-- b000276 | caption | pages [20] -->
table4.5: parameters Sierra Leone:

<!-- b000277 | prose | pages [20] -->
PARAMETER VALUE PARAMETER VALUE

<!-- b000278 | prose | pages [20] -->
 1 0.29 0.26 1

<!-- b000279 | prose | pages [20] -->
   / 2.43 0.11 2 1 H

<!-- b000280 | prose | pages [20] -->
  / 1h 2.25 0.48 F 1

<!-- b000281 | prose | pages [20] -->
 2h 0.46 0.79

<!-- b000282 | prose | pages [20] -->
  0.14 0.71 1 2 3

<!-- b000283 | prose | pages [20] -->
  0.54 0.84 2 4

<!-- b000284 | prose | pages [20] -->
  0.49 0.49 F 1H

<!-- b000285 | prose | pages [20] -->
  0.81 0.76 2 2H

<!-- b000286 | prose | pages [20] -->
The curves of Sierra Leone:

<!-- b000287 | caption | pages [20] -->
figure4.9: test of calculated curves (Sierra Leone)

<!-- b000288 | prose | pages [20] -->
We can see from the figure that curves also fit well to real data of Sierra Leone.Because of limited time, we cannot do prediction job for Liberia and Sierra Leone. But we strongly believe if we have enough time, we can predict future data precisely by using these 16 parameters with consideration of hospital. Here we must say sorry to people who live in Liberia and Sierra Leone.

<!-- b000289 | furniture | pages [21] -->
Team # 34317                                                                Page 18 of 44

<!-- b000290 | heading | pages [21] -->
Ⅴ Model of Locations of Delivery

<!-- b000291 | prose | pages [21] -->
Locations of delivery, by definition, it is the place to give out medicine to somewhere is in emergency. Ebola outbreak in West Africa covers a terrified curtain to people live there. People who enveloped in the curtain, in some ways, really need effective medicine delivered to accurate region, otherwise, sadly, there are only body bags waiting for them. So determine delivery locations are quite necessary. Considering total cases and current condition at the moment when medicine is successfully manufactured in these three diseases-torn countries, we use several methods and criteria to judge where are the relatively good places both have minimal cost and best treatment.

<!-- b000292 | heading | pages [21] -->
5.1 What is Emergency Supplies

<!-- b000293 | prose | pages [21] -->
At first, it is needed for us to have a clear understand of what are emergency supplies, like the medicine to cure Ebola. Different from normal supplies, emergency supplies are used to control bombshells when an emergency happens or used for evacuation, rescue and repair after an emergency happened while normal supplies are just used in daily life. More specifically, differences between them are shown as the table below:

<!-- b000294 | caption | pages [21] -->
table5.1: differences between two supplies[3]

<!-- b000295 | prose | pages [21] -->
ASPECTS NORMAL SUPPLIES EMERGENCY SUPPLIES Maximize Profile And Consider Both Fair And Aims Minimize Cost Efficiency Supplies Collection Point, Factory, Distribution Center Formation Delivery Place And Supplies And Customer Demand Point

<!-- b000296 | prose | pages [21] -->
Property Permanent Temporary

<!-- b000297 | prose | pages [21] -->
Divide Into Long-Term, Urgency, Make Tread-Off Scheme Medium-Term And Decision At Once Short-Term Balance Between Efficiency Think A Lot Of Optimization Think A Lot Of Efficiency And Optimization

<!-- b000298 | prose | pages [21] -->
Delivery Mode Return And Tour Return

<!-- b000299 | prose | pages [21] -->
Besides, there are some other characteristics of emergency supplies. Take the medicine developed by the WMA for example:

<!-- b000300 | prose | pages [21, 22] -->
i. Uncertainty: because we cannot predict when next Ebola outbreak happens and how terrible death it may bring to victims, so emergency supplies have uncertainties of amount of need and region of giving out.

<!-- b000301 | furniture | pages [22] -->
Team # 34317                                                                Page 19 of 44

<!-- b000303 | prose | pages [22] -->
ii. Irreplaceability: emergency supplies are special in special conditions and are irreplaceable. Like the medicine to cure Ebola, if we do not have the medicine, nothing can effectively cure Ebola patient.

<!-- b000304 | prose | pages [22] -->
iii. Timeliness: emergency supplies play their role at a certain period and if we miss the very moment, emergency supplies will lose their value. Like the medicine cannot revive already-dead Ebola patients

<!-- b000305 | prose | pages [22] -->
iv. Hysteresis: emergency supplies (or medicine) always delivered later than a disaster happened.

<!-- b000306 | prose | pages [22] -->
Thus, our goal is to filtrate several most-needed delivery locations in a country. In detail, we filtrate the delivery locations accord to clustering method and some principles.

<!-- b000307 | heading | pages [22] -->
5.2 Assumptions and Justifications

<!-- b000308 | prose | pages [22] -->
i. All delivery location lies in the provincial capitals of the prefectures.

<!-- b000309 | prose | pages [22] -->
It is evident that the capitals is easy to receive medicine that from developed countries. Namely, the delivery locations are supposed to have quick access to harbors or airports. Meanwhile, they have good public facilities status, road conditions and communication and they are plenty of power, water, heat and gas supply.

<!-- b000310 | prose | pages [22] -->
ii. Drug-need areas are concentrated on capitals of the prefectures, namely, we send the drug to capitals and do not consider the lower level of administrative areas.

<!-- b000311 | prose | pages [22] -->
From the size of prefectures, we know they are not large and it is easy for capitals to deliver drug to its lower level of administrative areas. Also, capitals are representative places to an Ebola-hit region. Because of its advanced development and high population density, the more infected people lived in the capitals.

<!-- b000312 | prose | pages [22] -->
iii. We overlook the cost when constructing delivery locations and the spending in storage of drugs.

<!-- b000313 | prose | pages [22] -->
Ebola outbreak in these countries and we should pay more attention to people’s health and lives and we should construct delivery locations as soon as it is needed. Actually, the speed of producing drugs is hard to satisfy the intense situation and we need to deliver the drug to the need as soon as possible.

<!-- b000314 | furniture | pages [23] -->
Team # 34317                                                                Page 20 of 44

<!-- b000315 | heading | pages [23] -->
5.3 Clustering Method, A Way to Determine Regions for Medicine

<!-- b000316 | prose | pages [23] -->
Delivery

<!-- b000317 | prose | pages [23] -->
We have a relatively clear understanding why the delivery locations have to be places in the prefecture where the provincial capital is located. However, we still have too many delivery locations to build just because of limited foundation in African countries. Thus, to maximal effect of delivery locations with consideration of limited money and other factors that we talked above, we have to make choice among different delivery locations and filtrate some of the delivery locations as ‘last winners’.

<!-- b000318 | prose | pages [23] -->
We deem two or more major cities in a same country as a ‘city group’ if they are close in distance. It is of little meaning to build delivery locations in each of these cities because we can transmit emergency supplies to each cities conveniently in a short time. It is too dense to build delivery locations in a ‘city group’. So we adopt clustering method to find out ‘city groups’ to divide a country into several regions.

<!-- b000319 | prose | pages [23] -->
According to the reticular distance (The reticular distance is the distance following the road network using main roads (primary, secondary, tertiary and few track/Trail)), we classify cities as different groups. Here our steps are:

<!-- b000320 | prose | pages [23] -->
 First we consider all cities in a certain country are independent to each other, namely, no groups contain two or more cities. Find reticular distance between

<!-- b000321 | prose | pages [23] -->
every two cities and construct a distance matrix D , D is a symmetric (0) (0)

<!-- b000322 | prose | pages [23] -->
matrix.

<!-- b000323 | prose | pages [23] -->
 Second, find the minimum element in D and we call it D , then gather G (0) KL k

<!-- b000324 | prose | pages [23] -->
   G G G , and G into a new group, G , that is, . ( D is the distance M k L L M KL

<!-- b000325 | prose | pages [23] -->
between G and G , G and G are two groups.) k L k L

<!-- b000326 | prose | pages [23] -->
 Third, calculate the distance between new group G that generated in second M

<!-- b000327 | prose | pages [23] -->
step and other group G . Here recurrence formula is j

<!-- b000328 | prose | pages [23, 24] -->
       D min d min min d , min d min D , D MJ ij ij ij KJ LJ       x G , x G x G , x G x G , x G i M j J i K j J i L j J Refresh distance matrix D by gathering the row where G lies in and the (0) k

<!-- b000329 | furniture | pages [24] -->
Team # 34317                                                                Page 21 of 44

<!-- b000331 | prose | pages [24] -->
column where G lies in into a new row and new column, so we get a new L

<!-- b000332 | prose | pages [24] -->
distance matrix . D (1)

<!-- b000333 | prose | pages [24] -->
 Last, repeat the second step until all cities are gathered into a group.

<!-- b000334 | prose | pages [24] -->
When all steps are done, we will successfully find how many ‘city groups’ in a country.

<!-- b000335 | heading | pages [24] -->
5.4 Results of Clustering Method

<!-- b000336 | prose | pages [24] -->
When finish all the steps we described above, we get three clustering pictures of Guinea, Liberia and Sierra Leone and we can use them to accomplish the following task. Here we give Liberia’ clustering results one picture. The other two countries’ district-dividing situation present in the Appendix.

<!-- b000337 | caption | pages [24] -->
figure5.1: Clustering Picture of Liberia

<!-- b000338 | prose | pages [24] -->
Once we have found ‘city groups’, we have another job to determine how many ‘city groups’ we need and which city in a ‘city group’ should be a delivery location. There are two principles we may need to comply with, one is principle of fairness, and the other is principle of efficiency.

<!-- b000339 | furniture | pages [25] -->
Team # 34317                                                                Page 22 of 44

<!-- b000340 | heading | pages [25] -->
5.5 Principle of Fairness

<!-- b000341 | prose | pages [25] -->
When a disaster occurs, it not only causes significant property damage but causes a lot of casualties with time going by. We hold an opinion that every life is equal. We cannot ignore the trapped or the patient of Ebola just because they are small in number or the cost of rescue. Providing our hands to everyone who needs help is a symbol of respect life and humanitarianism. Moreover, it enhances the country's sense of trust and identity.

<!-- b000342 | prose | pages [25] -->
For this kind of principle, we invoke P-Center model to illustrate our delivery locations choosing. Often cities are made up by many communities and other compositions, and there always have people live there. Thus, when we determine a delivery place in a region, life equality is our priority. We use equations to demonstrate the principal.

<!-- b000343 | prose | pages [25] -->
  P min Z  Z D y ij ij   i I j J

<!-- b000344 | prose | pages [25] -->
Where i denotes a destination of medicine transportation, j denotes a delivery

<!-- b000345 | prose | pages [25] -->
place in a region. And D means distance between destination i and a delivery ij

<!-- b000346 | prose | pages [25] -->
ijy  denotes we have to send medicine to destination i while place j . And 1

<!-- b000347 | prose | pages [25] -->
 ijy  0 denotes there is no need to do this. So means total distance Z D y ij ij   i I j J we have to cover if there are places need medicine. If a region has even need of medicine, the delivery place often in geographical center of the region.

<!-- b000348 | heading | pages [25] -->
5.6 Principle of Efficiency

<!-- b000349 | prose | pages [25] -->
According to population, risks and importance of different regions, we deem these regions of different ‘value’. Then different amount of emergency supplies are allocated to different delivery locations. Only in this way can we utilize the emergency supplies well and response as soon as possible if happens an emergency.

<!-- b000350 | prose | pages [25] -->
For this kind of principle, we invoke P-median model to illustrate our delivery locations choosing. When we determine a delivery place in a region, efficiency of delivering is our priority. We use equations to demonstrate the principal.

<!-- b000351 | prose | pages [25, 26] -->
  Q min Y  Y w D y i ij ij   i I j J Where i , j , D and ijy have same meanings as those in principle of fairness. ij

<!-- b000352 | furniture | pages [26] -->
Team # 34317                                                                Page 23 of 44

<!-- b000354 | prose | pages [26] -->
And iw denotes the number of Ebola patients in a place, that is, the more people get

<!-- b000355 | prose | pages [26] -->
 infected by Ebola, the larger iw is. Thus, means total ‘distance’ Y w D y i ij ij   i I j J we have to cover if there are places needing medicine. The reason why we use

<!-- b000356 | prose | pages [26] -->
‘distance’ is that we take iw into consideration, so ‘distance’ is not the proper

<!-- b000357 | prose | pages [26] -->
distance that we comprehend in daily life. Usually the delivery place is nearer to a more serious place in a region.

<!-- b000358 | heading | pages [26] -->
5.7 Determine Delivery Locations in the Three West African

<!-- b000359 | prose | pages [26] -->
Countries

<!-- b000360 | prose | pages [26] -->
Considering emergency of Ebola outbreak in a region, we find ‘city groups’ in Guinea, Liberia and Sierra Leone with criteria of delivering medicine within one day by trucks following the certain route (we will talk it in later part). If delivering time is more than one day, we use clustering method to find other ‘city groups’ to meet the criteria. Then we add the principals we showed above and finally determine delivery place(s) in Guinea, Liberia and Sierra Leone. During estimating process, we give different weight to the principle of fairness and the principle of efficiency. We endow more weight to the principle of fairness than the principle of efficiency because considering we can send medicine within one day, so advantages in time in different places may not play a main role in delivery locations choosing. Primarily, we consider fairness.

<!-- b000361 | heading | pages [26] -->
Ⅵ Model of Delivery System

<!-- b000362 | heading | pages [26] -->
6.1 Introduction

<!-- b000363 | prose | pages [26] -->
In the model of locations of delivery, we have determined some best delivery locations in a country to fit all the need that we put forward. However, only having delivery locations is far from a perfect project to distribute medicine to people who need it most, an effective and considerable delivery strategy is required, or a well-organized delivery system is required.

<!-- b000364 | prose | pages [26] -->
We define delivery system is made up by well-planned routes to allocate medicine and scientific amount of medicine to distribute to every needed places in every day.

<!-- b000365 | furniture | pages [27] -->
Team # 34317                                                                Page 24 of 44

<!-- b000366 | heading | pages [27] -->
6.2 Symbols and Definitions

<!-- b000367 | heading | pages [27] -->
SYMBOL

<!-- b000368 | prose | pages [27] -->
DEFINITION

<!-- b000369 | prose | pages [27] -->
ijc The Distance Between Two Points

<!-- b000370 | prose | pages [27] -->
j End Point i Start Point A Route From A Delivery Place To A ijx Destination Number Of Patients In Hospital Who Are In H 1 First Stage

<!-- b000371 | heading | pages [27] -->
6.3 TSP Model – Well-Planned Routes

<!-- b000372 | prose | pages [27] -->
Once happens certain scales of Ebola outbreaks, medicine have to be sent to cities or villages as soon as possible. Thanks to TSP (traveling salesman problem) Model, we structure an optimized route for trucks to transport medicine quickly.

<!-- b000373 | prose | pages [27] -->
 ijx  denotes there is a route We introduce a 0-1 integer variable : ijx ( i j ) 1

<!-- b000374 | prose | pages [27] -->
ijx  from point i to point j while 0 denotes there is no route from point i to

<!-- b000375 | prose | pages [27] -->
point j . The TSP Model can be expressed a group of equations.

<!-- b000376 | prose | pages [27] -->
n n  min c x ij ij   i 1 j 1

<!-- b000377 | prose | pages [27] -->
 n     x 1, i 1,2, , , n j i ,  ij   j 1  n     x 1, j 1,2, , , n i j , s t . .  ij   i 1    x 0,1, i j , 1,2, , , n ij   no subcycle

<!-- b000378 | prose | pages [27] -->
n   Where x 1 means there must have a start point i if we want to consider i ij  j 1

<!-- b000379 | prose | pages [27, 28] -->
n   as a point in route while means there must have an end point j if we x 1 ij  i 1 want to consider j as a point in route. And ‘no subcycle’ means we must cover all points in a certain region, namely, all trucks will cover a route that contains all cities which are in emergency of Ebola outbreak. Moreover, to well describe ‘no subcycle’,

<!-- b000380 | furniture | pages [28] -->
Team # 34317                                                                Page 25 of 44

<!-- b000382 | prose | pages [28] -->
 we add another variable iu i ( 1,2, , ) n and additional constraint condition:

<!-- b000383 | prose | pages [28] -->
        u u nx n 1, for u u , 0, i 1,2, , , n j 2,3, , , n i j i j ij i j

<!-- b000384 | prose | pages [28] -->
By now, we have established a model for us to construct a best route for trucks.

<!-- b000385 | heading | pages [28] -->
6.4 Daily Demand for Medicine

<!-- b000386 | prose | pages [28] -->
A good delivery system requires precise amount of medicine needed by places every day. We should develop a method to evaluate quantity of medicine we need a day by exploring number of patient in different places. We introduce an assessment standard called urgency index to depict how prob (i) much medicine a place need in one day. The expression of is prob (i)

<!-- b000387 | prose | pages [28] -->
H in a certain place in one day  prob (i) 1 H in three countries in one day 1

<!-- b000388 | prose | pages [28] -->
Where H has same meaning as that we have talked in Ebola propagation model, 1

<!-- b000389 | prose | pages [28] -->
namely, H means number of patients in hospital who are in first stage (such as fever, 1

<!-- b000390 | prose | pages [28] -->
headache, sore throat, muscle aches and other milder symptoms which often progress

<!-- b000391 | prose | pages [28] -->
to diarrhea and vomiting). There two reasons why we use H to describe the urgency 1

<!-- b000392 | prose | pages [28] -->
index, one is the WMA has announced their medicine can cure patients whose disease is not advanced, the other is that patients in first stage have great possibility to become more serious and step into second stage (such as hemorrhaging and multi-organ failure), we need to stop them from worsening.

<!-- b000393 | prose | pages [28] -->
If we have a certain amount of medicine (we will discuss the amount needed later), we can distribute different amount of medicine to different places to meet patients’ requirement.

<!-- b000394 | furniture | pages [29] -->
Team # 34317                                                                Page 26 of 44

<!-- b000395 | heading | pages [29] -->
Ⅶ Model Implementation of three Countries

<!-- b000396 | heading | pages [29] -->
7.1General algorithm

<!-- b000397 | prose | pages [29] -->
In the last part, we have discussed the models and, in fact, we are supposed to combine these models to use in specific situations. Here we give the general algorithm to determine the delivery locations and the transport route.

<!-- b000398 | prose | pages [29] -->
START

<!-- b000399 | prose | pages [29] -->
USING CLATER METHOD

<!-- b000400 | prose | pages [29] -->
DETERMING THE DELIVER

<!-- b000401 | heading | pages [29] -->
TSP MODEL TO GET THE

<!-- b000402 | prose | pages [29] -->
INCREASE THE NUMBER OF

<!-- b000403 | prose | pages [29] -->
CARS FINISH EVERY ROUTE IN ONE DAY?

<!-- b000404 | prose | pages [29] -->
GET LOCATIONS AND TRANSPORT

<!-- b000405 | prose | pages [29] -->
END

<!-- b000406 | caption | pages [29] -->
figure7.1: general algorithm to determine the delivery locations and route

<!-- b000407 | furniture | pages [30] -->
Team # 34317                                                                Page 27 of 44

<!-- b000408 | heading | pages [30] -->
7.2 Application of Algorithm

<!-- b000409 | prose | pages [30] -->
By exploring maps from WHO website of different Ebola cases in different places, then adopting TSP Model, we find some routes not only can cover all places that we have to send medicine to, but also consider places with more Ebola cases as more dangerous places and send medicine to the places within less time.

<!-- b000410 | heading | pages [30] -->
7.2.1 Application in Guinea

<!-- b000411 | prose | pages [30] -->
Since the area is approximately 245857 square kilometers and we must assure the route solved by the TSP model is not too long, in specific, we considered that one car can cover the distance in one day.

<!-- b000412 | prose | pages [30] -->
Step 1: only one delivery location

<!-- b000413 | prose | pages [30] -->
Use the principles which are needed to determine the location, we calculate the delivery location lies in DABOLA. The maximum distance among DABOLA and other prefectures is 585km.

<!-- b000414 | prose | pages [30] -->
Then use the results of the cluster method, we divided other prefectures into two parts and DABOLA is in respond for the distribution of drugs to them. Thus, we need to solve tow TSP problems.

<!-- b000415 | prose | pages [30] -->
Step 2: solve the distance route Use the TSP model, we solve the route and use the picture shows the results:

<!-- b000416 | prose | pages [30] -->
location A B

<!-- b000417 | prose | pages [30, 31] -->
Confirmed Cases In the map, A and B represent the two route and the distances of them are 1213.8km and 1548.2km. Considering the velocity of vehicles is 80km/h, and it will cost more than 12 hours to finish one route and it is not reasonable for the relief of the disease. Therefore, only one location is not appropriate.

<!-- b000418 | caption | pages [30] -->
figure7.2: one delivery location in guinea

<!-- b000419 | furniture | pages [31] -->
Team # 34317                                                                Page 28 of 44

<!-- b000421 | prose | pages [31] -->
Step3: adjust the number of delivery locations According to the result of cluster results, it is better to divide the prefectures into 3 clusters. Then calculate the 3 different locations, cut every cluster into 2 smaller parts and repeat step2. We get the map:

<!-- b000422 | prose | pages [31] -->
location D B C 1

<!-- b000423 | prose | pages [31] -->
A location

<!-- b000424 | prose | pages [31] -->
E location F

<!-- b000425 | prose | pages [31] -->
Confirmed Cases

<!-- b000426 | caption | pages [31] -->
figure7.3: three delivery locations in guinea

<!-- b000427 | prose | pages [31] -->
In the map, A, B, C, D, E and represent the two route and the distances of them show in the table:

<!-- b000428 | prose | pages [31] -->
A B

<!-- b000429 | heading | pages [31] -->
C D

<!-- b000430 | prose | pages [31] -->
E F

<!-- b000431 | prose | pages [31] -->
752.2 686.6 578.0 546.5 640.4 701.2

<!-- b000432 | prose | pages [31] -->
Vehicles can pass through the distance in one day. We conclude that 3 cluster is enough for Guinea.

<!-- b000433 | prose | pages [31] -->
And the delivery locations are: DUBREKA, KOUROUSSA, and MACENTA.

<!-- b000434 | furniture | pages [32] -->
Team # 34317                                                                Page 29 of 44

<!-- b000435 | prose | pages [32] -->
The route is listed:

<!-- b000436 | caption | pages [32] -->
table7.1: the six routes

<!-- b000437 | prose | pages [32] -->
DUBREKAFRIABOKEBOFFACONAKRYFORECARIAH A COYAHDUBREKA

<!-- b000438 | prose | pages [32] -->
B DUBREKATELIMELEPITADALABAKINDIADUBREKA

<!-- b000439 | prose | pages [32] -->
C KOUROUSSAFARANAHDABOLAKOUROUSSA

<!-- b000440 | prose | pages [32] -->
D KOUROUSSASIGUIRIKANKANKOUROUSSA

<!-- b000441 | prose | pages [32] -->
MACENTAGUECKEDOUKISSIDOUGOU E KEROUANEMACENTA

<!-- b000442 | prose | pages [32] -->
F MACENTABEYLALOLANZEREKOREYOMOUMACENTA

<!-- b000443 | heading | pages [32] -->
7.2.2 Application in Liberia

<!-- b000444 | prose | pages [32] -->
In terms of area, Liberia is smaller than Guinea and its area is 111370 square kilometers. Following the algorithm, like the steps in the analysis of Guinea, and we find only one deliver center is proper for the area.

<!-- b000445 | furniture | pages [33] -->
Team # 34317                                                                Page 30 of 44

<!-- b000446 | prose | pages [33] -->
Here the results are:

<!-- b000447 | prose | pages [33] -->
Confirmed Cases A

<!-- b000448 | prose | pages [33] -->
location

<!-- b000449 | prose | pages [33] -->
B

<!-- b000450 | caption | pages [33] -->
figure7.4: one location in Liberia

<!-- b000451 | prose | pages [33] -->
In the map, A, and B represent the two route and the distances of them show in the table:

<!-- b000452 | prose | pages [33] -->
A B

<!-- b000453 | prose | pages [33] -->
869.0 715.6

<!-- b000454 | prose | pages [33] -->
Therefore, the deliver location is Grand Bassa.

<!-- b000455 | heading | pages [33] -->
7.2.3 Sierra Leone

<!-- b000456 | prose | pages [33] -->
In terms of area, Sierra Leone is the smallest among the three countries and its area is 71740 square kilometers.

<!-- b000457 | prose | pages [33] -->
Just like what we have done before, we apply the algorithm.

<!-- b000458 | furniture | pages [34] -->
Team # 34317                                                                Page 31 of 44

<!-- b000459 | prose | pages [34] -->
Here present the result:

<!-- b000460 | prose | pages [34] -->
A location

<!-- b000461 | prose | pages [34] -->
B

<!-- b000462 | prose | pages [34] -->
Confirmed Cases

<!-- b000463 | caption | pages [34] -->
figure7.5: Sierra Leone

<!-- b000464 | prose | pages [34] -->
In the map, A, and B represent the two route and the distances of them show in the table:

<!-- b000465 | prose | pages [34] -->
A B

<!-- b000466 | prose | pages [34] -->
616.9 411.4

<!-- b000467 | prose | pages [34] -->
Therefore, the deliver location is Tonkolili.

<!-- b000468 | heading | pages [34] -->
Ⅷ Model of the Quantity of the Medicine Needed and

<!-- b000469 | prose | pages [34] -->
Manufacturing Speed

<!-- b000470 | heading | pages [34] -->
8.1 Introduction

<!-- b000471 | prose | pages [34] -->
In this section, we consider the quantity of the medicine needed and speed of manufacturing of the vaccine or drug together because the manufacturing speed will impact the number of the susceptible, the infected who are in first stage and the recovered. The reason is that if the susceptible are vaccinated, they will hardly get infected by Ebola, and the infected once receive drug they can recover day by day. So the recovered is more than before as we regard the vaccinated people and cured people as the recovered.

<!-- b000472 | furniture | pages [35] -->
Team # 34317                                                                Page 32 of 44

<!-- b000473 | heading | pages [35] -->
8.2 Assumptions and Justifications

<!-- b000474 | prose | pages [35] -->
 Amount of medicine and vaccine that are produced everyday increase linearly with time when the medicine or vaccine is rare. Because the medicine or vaccine is newly developed by scientists and still in testing stage, so manufactures will not produce a large-scale of this kind of medicine or vaccine at first. So we consider amount of medicine and vaccine that are produced everyday increase linearly with time rather than exponentially with time.

<!-- b000475 | prose | pages [35] -->
 The infected do not have ability of allopathic medicines. The Ebola virus are relatively stable, namely, variation is not common in Ebola virus. So we consider Ebola virus do not have ability of allopathic medicines.

<!-- b000476 | prose | pages [35] -->
8.3 symbols and definitions

<!-- b000477 | prose | pages [35] -->
SYMBOL DEFINITION

<!-- b000478 | prose | pages [35] -->
V Speed Of Producing Medicine 1

<!-- b000479 | prose | pages [35] -->
V Speed Of Producing Vaccine 2

<!-- b000480 | prose | pages [35] -->
1b Initial Inventory Of Medicine

<!-- b000481 | prose | pages [35] -->
2b Initial Inventory Of Vaccine

<!-- b000482 | prose | pages [35] -->
‘Manufacturing Acceleration’ Of 1k Medicine Per Day ‘Manufacturing Acceleration’ Of Vaccine 2k Per Day

<!-- b000483 | prose | pages [35] -->
i Urgency Index

<!-- b000484 | prose | pages [35] -->
 1 Course Of Treatment Of The Medicine h

<!-- b000485 | heading | pages [35] -->
8.4 How Fast Need We Produce Medicine and Vaccine

<!-- b000486 | prose | pages [35] -->
We have talked that Amount of medicine and vaccine produced everyday increase linearly with time in assumption, so we have equations to express the amount that produced per day.

<!-- b000487 | furniture | pages [36] -->
Team # 34317                                                                Page 33 of 44

<!-- b000488 | prose | pages [36] -->
  Medicine V k t b 1 1 1   Vaccine V k t b 2 2 2

<!-- b000489 | prose | pages [36] -->
Where 1b and 2b denote initial inventory of medicine and vaccine, respectively.

<!-- b000490 | prose | pages [36] -->
And 1k , 2k mean ‘manufacturing acceleration’ of medicine and vaccine per day.

<!-- b000491 | prose | pages [36] -->
We show the relationship between V and time t . 1

<!-- b000492 | caption | pages [36] -->
figure8.1: speed of producing medicine

<!-- b000493 | prose | pages [36] -->
From the figure 8.1, we get information that when medicine is rare, the amount of medicine produced everyday increases linearly with time until all the patients who are in first stage can get the medicine, and this condition happens nearly 25 days after the medicine is used in the public. Then the amount of medicine that is produced everyday will drop with the number of patients who are in first stage. Namely, we

<!-- b000494 | prose | pages [36] -->
have more specific equations to explain V . 1

<!-- b000495 | prose | pages [36] -->
   k t b , V H 1 1 1 1  medicine V 1  H , V H  1 1 1

<!-- b000496 | prose | pages [36] -->
When medicine and vaccine are used in the public, equations of the susceptible, the infected in first stage and the recover we have shown in the advanced model in sectionⅣ may change (marked in red).

<!-- b000497 | prose | pages [36, 37] -->
 dS             [ ( I H ) ( I H ) F S ] V  I 1 H 1 2 2 H 2 F i 2 dt  dH       1 h I H V  1 1 3 1 i 1 h dt   dR                  (1 ) I (1 ) I (1 ) H (1 ) H V  1 1 1 2 2 2 1 H 3 1 2 H 4 2 i 2 d t  i is the urgency index that we have described in section 6.4, namely, Where

<!-- b000498 | furniture | pages [37] -->
Team # 34317                                                                Page 34 of 44

<!-- b000500 | prose | pages [37] -->
H in a certain place in one day   1 prob (i) . We distribute medicine with criteria i H in three countries in one day 1

<!-- b000501 | prose | pages [37] -->
 that we have described in section 6.4, so means number of the susceptible who iV 2

<!-- b000502 | prose | pages [37] -->
are vaccinated and have antibody to against Ebola, thus, can hardly get infected. And

<!-- b000503 | prose | pages [37] -->
  means number of the infected who are in first stage get recovered because of V i 1 h

<!-- b000504 | prose | pages [37] -->
 means course of treatment of the medicine. And  1 the medicine, iV means the 2 h

<!-- b000505 | prose | pages [37] -->
number of the susceptible who will hardly get infected because of the vaccine. Then we draw a figure to express changing of total cases growing with time in the condition of using medicine.

<!-- b000506 | caption | pages [37] -->
figure 8.2: Changing of Total Cases Growing with Time When Using Medicine

<!-- b000507 | prose | pages [37] -->
As for vaccine, it generates its effect mainly among the susceptible. Since number of the susceptible is much much larger than amount of vaccine, we ignore the effect generated by the vaccine. From the figure, we can see the medicine is used after 90 days form initial time, that is, we can figure out that the medicine is used from Feb.1st, 2015. And 50 days after using the medicine, number of total cases will not increase, which means the medicine has its positive impact on Ebola containing.

<!-- b000508 | prose | pages [37] -->
b  5 The parameters in our calculating process are (we produce 5 units of 1

<!-- b000509 | prose | pages [37, 38] -->
k  medicine per day at the beginning of producing) and 5 (we produce 5 more 1 units of medicine per day).

<!-- b000510 | furniture | pages [38] -->
Team # 34317                                                                Page 35 of 44

<!-- b000512 | prose | pages [38] -->
As for vaccine, we ignore it in our calculating process for it is much much less in number compared to number of the susceptible.

<!-- b000513 | heading | pages [38] -->
8.5 The Quantity of the Medicine Needed

<!-- b000514 | prose | pages [38] -->
We use integral computation to find the quantity of the medicine we need. So total needed amount is t  w V t dt ( ) 1 0 Use parameters we have calculated in last section, we draw a figure to show the quantity of the medicine.

<!-- b000515 | caption | pages [38] -->
figure8.3: Changing of Quantity of The Medicine

<!-- b000516 | prose | pages [38] -->
So we need about 3400 units of medicine to cure the patient who are in first stage in the three west African countries.

<!-- b000517 | prose | pages [38] -->
If we develop better medicine that can cure patients in second stage in the future, we believe the quantity of medicine can decrease.

<!-- b000518 | prose | pages [38] -->
Ⅸ Other Factors We Think Are Important

<!-- b000519 | prose | pages [38] -->
In our first model –SEIIRF model and its advanced model, we didn’t consider other two factors that we think are necessary to discuss. One is control of Ebola spreading in hospitals, and the other is control of Ebola spreading in funerals.

<!-- b000520 | prose | pages [38] -->
If we control of Ebola spreading in hospital, there will be less healthy people get infected. We regard a hospital as a ‘huge’ patient with strong ability of infection. We must take measures to reduce the ability of infection. The figure shown below delivers us information that hoe the total cases in Guinea will be like if we reduce 50% and 90% of the ability down.

<!-- b000521 | furniture | pages [39] -->
Team # 34317                                                                Page 36 of 44

<!-- b000522 | caption | pages [39] -->
figure9.1: changing of total cases in guinea if we control Ebola spreading in hospitals

<!-- b000523 | prose | pages [39] -->
We can see from the figure, if we take strategies to control Ebola spreading in hospitals, total cases will reduce greatly and significantly.

<!-- b000524 | prose | pages [39] -->
Then if we control Ebola spreading in funerals, what will happen? There is a figure will tell us.

<!-- b000525 | caption | pages [39] -->
figure9.2: changing of total cases in guinea if we control Ebola spreading in funerals

<!-- b000526 | prose | pages [39] -->
Controlling Ebola spreading in funerals maybe are not as good as in hospitals. But at least, it does its positive effect on reducing total cases in the future.

<!-- b000527 | heading | pages [39] -->
Ⅹ Future Improvement

<!-- b000528 | heading | pages [39] -->
10.1 Optimization of Coverage to Determine Delivery Locations

<!-- b000529 | prose | pages [39, 40] -->
Since we are introduced one method and two principles in delivery places choosing, now we can easily make a decision on where to build a delivery place in a certain region. However, as a designer, we must be more considerable if we have more time to do our design. Unfortunately, time is limited, here we just introduce you another principle that is worthwhile to consider – principle of optimization of coverage. When a disaster occurs, we will generally distribute emergency supplies which are relatively near to the place that happens the disaster as fast as possible. Considering the disaster, like Ebola, is usually of great impact on the local and of tremendous harm, we sometimes need to allocate and transport more emergency supplies to this area. Thus, when we choose to delivery places we must take it into consideration that the delivery places can cover as many emergency-supplies-need regions as possible simultaneously. So when an emergency happens in an area that covered by a delivery place, emergency supplies, like the medicine, can be sent in time. Here the equations of the principle are   X max A  A wc y i ij ij   i I j J

<!-- b000530 | furniture | pages [40] -->
Team # 34317                                                                Page 37 of 44

<!-- b000532 | prose | pages [40] -->
Where i , j , iw and ijy have same meanings as those in principle of fairness.

<!-- b000533 | prose | pages [40] -->
And we call ijc degree of coverage.

<!-- b000534 | prose | pages [40] -->
  1 , t t m    t t   c , t t t 1  ij 1 m  t t  m 1   0 , t t  m

<!-- b000535 | prose | pages [40] -->
Where 1t is minimum time of a truck to arrive at a destination while mt is

<!-- b000536 | prose | pages [40] -->
maximum time of a truck to arrive at a destination. In our model of delivery places

<!-- b000537 | prose | pages [40] -->
choosing, mt is no longer than one day. From expression of ijc , we can see the

<!-- b000538 | prose | pages [40] -->
degree of coverage increases with time going by, which is consistent with reality.

<!-- b000539 | heading | pages [40] -->
10.2 A No-boundary Scheme

<!-- b000540 | prose | pages [40] -->
In our paper, the models of locations and TSP apply in three countries (Sierra Leone, Liberia and Guinea) respectively. We consider there is no contact among these Ebola-hit countries and the delivery locations distributed in three countries and every countries delivery locations only send needed drug to itself. However, we human beings should unit to eradicate the Ebola in the face of such serious situation. Therefore, we are better to combine the three countries tightly and arrange the delivery locations and transportation system without considering the boundary and political problems.

<!-- b000541 | prose | pages [40, 41] -->
So a no-boundary scheme can be developed to quickly get rid of the trouble of Ebola.

<!-- b000542 | furniture | pages [41] -->
Team # 34317                                                                Page 38 of 44

<!-- b000544 | heading | pages [41] -->
Ⅺ Sensitivity analysis

<!-- b000545 | heading | pages [41] -->
11.1 Sensitivity Analysis of SEIIRF Model

<!-- b000546 | prose | pages [41] -->
We get some parameters through the method of least squares fitting in the model to predict the spread of Ebola,. To test the effect of changing parameters, we will produce a sensitivity analysis that shows whether our model is properly sensitive to these variations.

<!-- b000547 | prose | pages [41] -->
In the following section, we will analyze the sensitivity of total cases of patients, , Length Of First Stage Of Illness (Not In 1 according to Average Incubation Period

<!-- b000548 | prose | pages [41] -->
1, Transmission Parameter For First Stage Of Illness (Not In Hospital) 1 Hospital)

<!-- b000549 | prose | pages [41] -->
, ,  respectively. In specific, we modified parameter ( 1) by  10% 1 1

<!-- b000550 | prose | pages [41] -->
respectively and observe the change of total cases.

<!-- b000551 | prose | pages [41] -->
 to the total cases

<!-- b000552 | caption | pages [41] -->
figure11.1: the impact of

<!-- b000553 | prose | pages [41] -->
1

<!-- b000554 | prose | pages [41] -->
From the picture above we can get the result that the total cases of patients change

<!-- b000555 | prose | pages [41] -->
. So this proves the slight fluctuations of  can be little with the change of 1 1

<!-- b000556 | prose | pages [41] -->
ignored and the results we conclude in the above models are reliable.

<!-- b000557 | furniture | pages [42] -->
Team # 34317                                                                Page 39 of 44

<!-- b000558 | prose | pages [42] -->
1 to the total cases

<!-- b000559 | caption | pages [42] -->
figure11.2: the impact of

<!-- b000560 | prose | pages [42] -->
As the figure shows, the total cases stay relatively stable in different result

<!-- b000561 | prose | pages [42] -->
1. Therefore, the total cases we use is exact enough. generated from different

<!-- b000562 | heading | pages [42] -->
11.2 Sensitivity Analysis of Model of the Speed to Produce Medicine

<!-- b000563 | prose | pages [42] -->
We change initial speed of the production of medicine 1b and total cases of

<!-- b000564 | prose | pages [42] -->
patients are shown in the following the figure:

<!-- b000565 | prose | pages [42, 43] -->
1b to the total cases From the picture above, we find that if the speed 1b is relatively small, the

<!-- b000566 | caption | pages [42] -->
figure11.3: the impact of

<!-- b000567 | furniture | pages [43] -->
Team # 34317                                                                Page 40 of 44

<!-- b000569 | prose | pages [43] -->
influence of the change of 1b is larger compared to bigger 1b . In addition, we find

<!-- b000570 | prose | pages [43] -->
that cases increase with the increase of initial speed and the trend is expected. In all, the results are stable.

<!-- b000571 | heading | pages [43] -->
Ⅻ Conclusion

<!-- b000572 | heading | pages [43] -->
11.1 Strengths and Weaknesses

<!-- b000573 | prose | pages [43] -->
Now we will analyze the strengths and weaknesses of models in our paper:

<!-- b000574 | heading | pages [43] -->
SEIIRF Model

<!-- b000575 | prose | pages [43] -->
Strengths 1. The results of model conform to the reality well, such as the prediction of the number of patient cases. 2. We considered three ways of the spread of Ebola which are relatively comprehensive and more groups of people which are representative to the disease search.

<!-- b000576 | prose | pages [43] -->
Weaknesses 1. There are more parameters in the model and it may bring negative influence to the sensitivity. 2. Due to lack of data, we do not study spatial distribution of Ebola.

<!-- b000577 | heading | pages [43] -->
Model of Locations of Delivery and Delivery System

<!-- b000578 | prose | pages [43] -->
Strengths 1. We use TSP model which is relatively simple but effective to solve the delivery system. 2. We develop a general algorithm to determine the transportation locations and system. Weaknesses 1. Because the limit of time, we do not solve the the no-boundary scheme which is presented in the part of future improvement.

<!-- b000579 | heading | pages [43] -->
Model of the Speed to Produce Medicine

<!-- b000580 | prose | pages [43] -->
Strengths 1. We calculated the model on quantitative analysis.

<!-- b000581 | prose | pages [43] -->
Weaknesses 1. The speed to producing drug grow linearly and this process maybe too ideally

<!-- b000582 | furniture | pages [44] -->
Team # 34317                                                                Page 41 of 44

<!-- b000583 | heading | pages [44] -->
11.2 Overall Results

<!-- b000584 | prose | pages [44] -->
Up to now, we have accomplished all our tasks. And here we give the overall results of all our models.

<!-- b000585 | prose | pages [44] -->
Above all, we develop basic SEIIRF model and then improve this model to predict the spread of Ebola, and finally the model confirms to the reality which we test it using collected data. Then, we establish a general algorithm to solve the delivery locations and design delivery system. In specific, we get the locations of delivery and the certain route of transportation system through cluster analysis and TSP model. Also, the length of all routes is suitable for the delivery of drug. With the route, we can distribute drug according to urgency index which is relevant to the proportionality of the patients. Considering the specific speed of producing the drug, we simulate the situation and get the conclusion that in 50 days, we can eradicate Ebola. After that, we consider other factors, such as control of Ebola spreading in hospitals and in funerals, and the situation can be relieved greatly. At last, we test the sensitivity of our model and it shows that they are stable.

<!-- b000586 | furniture | pages [45] -->
Team # 34317                                                                Page 42 of 44

<!-- b000587 | heading | pages [45] -->
LETTER

<!-- b000588 | prose | pages [45] -->
To: Professors of the World Medical Association

<!-- b000589 | prose | pages [45] -->
From: Team # 34317

<!-- b000590 | prose | pages [45] -->
Date: February 9, 2015

<!-- b000591 | prose | pages [45] -->
Subject: A Battle against Ebola

<!-- b000592 | prose | pages [45] -->
Ebola, a familiar but strange word to us. No one can

<!-- b000593 | prose | pages [45] -->
imagine the name ‘Ebola’ just originates from a little

<!-- b000594 | prose | pages [45] -->
river - Ebola River in Congo. Contrary to its attracting

<!-- b000595 | prose | pages [45] -->
meaning, it is true that the Ebola virus do take lots of

<!-- b000596 | prose | pages [45] -->
victims’ lives away. Fighting against Ebola is now a

<!-- b000597 | prose | pages [45] -->
worldwide battle. We human beings need to unit together

<!-- b000598 | prose | pages [45] -->
and offer helps to each other. Besides, we are really

<!-- b000599 | prose | pages [45] -->
appreciate those doctors in the MSF who fight against

<!-- b000600 | prose | pages [45] -->
Ebola day and night in West Africa.

<!-- b000601 | prose | pages [45] -->
We also do our best to evaluate Ebola spreading in West

<!-- b000602 | prose | pages [45] -->
Africa. We use models to predict future cases in Guinea,

<!-- b000603 | prose | pages [45] -->
Liberia and Sierra Leone. First, we use real data to

<!-- b000604 | prose | pages [45] -->
calculate a curve for usage of prediction. Then we use

<!-- b000605 | prose | pages [45] -->
newest data in the WHO website to test the curve. We

<!-- b000606 | prose | pages [45, 46] -->
find the curve can predict well and be trusted. Then, we use this curve to predict future cases including total cases

<!-- b000607 | furniture | pages [46] -->
Team # 34317                                                                Page 43 of 44

<!-- b000609 | prose | pages [46] -->
and death cases. And we find that if we use medicine,

<!-- b000610 | prose | pages [46] -->
total cases and death cases will decrease a lot.

<!-- b000611 | prose | pages [46] -->
Then we design a method to find some best delivery

<!-- b000612 | prose | pages [46] -->
places in Guinea, Liberia and Sierra Leone that can

<!-- b000613 | prose | pages [46] -->
allocate medicine quickly to places where Ebola

<!-- b000614 | prose | pages [46] -->
outbreaks. Moreover, we offer you schemed routes both

<!-- b000615 | prose | pages [46] -->
are time-saving and able to caver most places for

<!-- b000616 | prose | pages [46] -->
vehicles to transport emergency supplies.

<!-- b000617 | prose | pages [46] -->
At last, we calculate out the quantity of the medicine

<!-- b000618 | prose | pages [46] -->
needed and the speed of manufacturing medicine and

<!-- b000619 | prose | pages [46] -->
vaccine. We take two conditions into consideration. One

<!-- b000620 | prose | pages [46] -->
is the condition that if medicine is too rare to help most

<!-- b000621 | prose | pages [46] -->
people, the medicine factories should gradually increase

<!-- b000622 | prose | pages [46] -->
their output, and the other condition is that if medicine is

<!-- b000623 | prose | pages [46] -->
enough for the infected, the amount of medicine should

<!-- b000624 | prose | pages [46] -->
decrease with time. The total amount of medicine is 3400

<!-- b000625 | prose | pages [46] -->
units.

<!-- b000626 | prose | pages [46] -->
Besides, we have done other jobs to evaluate Ebola, you

<!-- b000627 | prose | pages [46] -->
can see our paper for details.

<!-- b000628 | prose | pages [46, 47] -->
Yours sincerely ⅩⅢ Reference

<!-- b000629 | furniture | pages [46] -->
Team # 34317

<!-- b000630 | furniture | pages [47] -->
Team # 34317                                                                Page 44 of 44

<!-- b000632 | prose | pages [47] -->
[1]http://www.theguardian.com/commentisfree/2014/dec/29/2015-ebola-eradicated-ep idemic-west-africa [2]http://www.huffingtonpost.com/darius-mans/behavior-change-is-key-to_b_575270 4.html [3] Tzeng, G H.,Cheng, H. J., and Huang, T. D. Multi-objective optimal planning for designing relief delivery systems. Transportation Research Part E: Logistics and Transportation Review, 2007,43(6),673-686. [4] http://www.diva-gis.org/datadown [5] Marisa C. Eisenberg, Joseph N.S. Eisenberg, Jeremy P. D'Silva, Eden V. Wells.” Modeling surveillance and interventions in the 2014 Ebola epidemic” The Lancet Infectious Diseases(2015). [6] Chen zhi-zong, “Major events multi-objective decision model of facility location of emergency rescue”, MANAGEMENT SCIENCES IN CHINA(2006). [7] PANG Hai-yun, LIU Nan, WU Qiao, “Decision-making model for transportation and distribution of emergency materials and its modified particle swarm optimization algorithm” Control and Decision(2012). [8] ZHU Jian-ming, HUANG Jun,” Randomized Algorithm for Vehicle Routing Model for Medical Supplies  in Large-Scale Emergencies”, OPERATIONS RESEARCH AND MANAGEMENT SCIENCE(2010). [9] Liu Fang, “A brief introduction to the U.S. Strategic National Stockpile”, Mil Med Sci. Vol 38, No.11, 2014. [10] http://maps.who.int/MapJournal/?appid=5b29178821dd4584b78dcb18d280326a [11] Gu Yong, ”Based on the mechanism of the prevention and control infectious disease emergency supplies demand analysis”, Journal of Wuhan University of Technology, 2010.
