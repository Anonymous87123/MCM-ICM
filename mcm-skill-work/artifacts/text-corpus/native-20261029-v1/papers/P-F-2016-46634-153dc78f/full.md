# P-F-2016-46634-153dc78f

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->


<!-- b000002 | furniture | pages [1] -->


<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | title | pages [1] -->
46634

<!-- b000005 | prose | pages [1] -->
For office use only

<!-- b000006 | prose | pages [1] -->
T1 ________________

<!-- b000007 | prose | pages [1] -->
T2 ________________

<!-- b000008 | furniture | pages [1] -->


<!-- b000009 | prose | pages [1] -->
T3 ________________

<!-- b000010 | prose | pages [1] -->
For office use only

<!-- b000011 | prose | pages [1] -->
F1 ________________

<!-- b000012 | prose | pages [1] -->
F2 ________________

<!-- b000013 | prose | pages [1] -->
F3 ________________

<!-- b000014 | prose | pages [1] -->
Problem Chosen

<!-- b000015 | prose | pages [1] -->
T4 ________________

<!-- b000016 | furniture | pages [1] -->


<!-- b000017 | prose | pages [1] -->
F4 ________________

<!-- b000018 | title | pages [1] -->
F

<!-- b000019 | furniture | pages [1] -->


<!-- b000020 | prose | pages [1] -->
2016 MCM/ICM

<!-- b000021 | heading | pages [1] -->
Summary Sheet

<!-- b000022 | prose | pages [1] -->
(Your team's summary should be included as the first page of your electronic submission.)

<!-- b000023 | prose | pages [1] -->
Type a summary of your results on this page. Do not include the name of your school, advisor, or team members on this page.

<!-- b000024 | furniture | pages [1] -->


<!-- b000025 | title | pages [1] -->
Modeling to Refugees Policies

<!-- b000026 | heading | pages [1] -->
Summary

<!-- b000027 | prose | pages [1] -->
With thousands of refugees moving across Europe and more arriving each day, considerable attention has been given to refugee integration policies and practices in many countries and regions.  We build a series of models to explore the factors involved with facilitating the movement of refugees from their countries of origin into safe haven countries.

<!-- b000028 | prose | pages [1] -->
Firstly, we optimize the Control Variable algorithm to build a model to analyze the measures and parameters of the crisis. We set factors such as the psychological quality and faith of refugees, the resources and refugee policy of the refugee-receiving country, the refugees’ saturation of the refugee-receiving country and the natural disaster or terrorist. Finding out that every factor is of crucial importance, and the more favorable the conditions are, the more likely the refugees move to the safe countries.

<!-- b000029 | prose | pages [1] -->
Secondly, we use the index set above to analyze the flow of refugees. From the optimized Small World Network algorithm, we find that there are 637000 refugees arriving EU a year, among them, 311000 refugees will transfer via Eastern Mediterranean, 221000 refugees via West Mediterranean, 45000 refugees via West Balkans, 32000 refugees via Eastern Borders, 18000 refugees from Albania to Greece, and 10000 refugees via Central Mediterranean. And the transfer rate should be controlled below 50187 per month.

<!-- b000030 | prose | pages [1] -->
Thirdly, we consider the parameters set in task 1 are dynamic, finding out that our model is also applicative while we should adjust the details in our model.

<!-- b000031 | prose | pages [1] -->
Finally, we make a report to discuss our model in detail and raise the needed policy support. We analyze the impact of exogenous events as well. Meanwhile, we state the scalability of our model. Then we believe that our model can solve most of the problems.

<!-- b000032 | prose | pages [1] -->
In the end, we analyze the stability and sensitivity of model. We also conclude the strengths and weaknesses of our model. Further, the accuracy of our model needs improving.

<!-- b000033 | furniture | pages [2] -->
Team#46634

<!-- b000034 | furniture | pages [2] -->
page 1 of 22

<!-- b000035 | furniture | pages [2] -->


<!-- b000036 | heading | pages [2] -->
Introduction

<!-- b000037 | prose | pages [2] -->
 Background

<!-- b000038 | prose | pages [2] -->
With hundreds of thousands of refugees moving across Europe and more arriving each day, considerable attention has been given to refugee integration policies and practices in many countries and regions. History has shown us that mass fleeing of populations occur as a result of major political and social unrest and warfare. These crises bring a set of unique challenges that must be managed carefully through effective policies. Events in the Middle East have caused a massive surge of refugees emigrating from the Middle East into safe haven countries in Europe and parts of Asia, often moving through the Mediterranean and into countries such as Turkey, Hungary, Germany, France, and UK. By the end of October 2015, European countries had received over 715,000 asylum applications from refugees. Hungary topped the charts with nearly 1,450 applications per 100,000 inhabitants, but with only a small percentage of those requests granted (32% in 2014), leaving close to a thousand refugees homeless per every 100K residents of the country. Europe has established a quota system that each country has agreed to take in a particular number of refugees, with the majority of the resettlement burden lying with France and Germany.

<!-- b000039 | prose | pages [2] -->
 Our Work

<!-- b000040 | prose | pages [2] -->
Firstly, we optimize the Control Variable algorithm to build a model to analyze the measures and parameters of the crisis. We set the psychological quality of refugees, the faith of the refugees, the material and financial resources of the refugee-receiving country, the refugee policy of the refugee-receiving country, the refugees saturation of the refugee- receiving country and the natural disaster, terrorist as factors, finding out that every factor is important to the crisis, and the more favorable the conditions are, the more likely the refugees move to the safe countries.

<!-- b000041 | prose | pages [2] -->
Secondly, we use the index set above to analyze the flow of refugees. From the optimized Small World Network algorithm, we find that there are 637000 refugees arriving EU a year, among them, 311000 refugees will transfer via Eastern Mediterranean, 221000 refugees via West Mediterranean, 45000 refugees via West Balkans, 32000 refugees via Eastern Borders, 18000 refugees from Albania to Greece, and 10000 refugees via Central Mediterranean. And the transfer rate should be controlled below 50187 per month.

<!-- b000042 | prose | pages [2] -->
Thirdly, we consider the parameters set in task 1 are dynamic, finding out that our model is also applicable while we should adjust the details in our model.

<!-- b000043 | prose | pages [2] -->
Finally, we make a report to discuss our model in detail and raise the needed policy support. We analyze the impact of exogenous events as well. Meanwhile, we state the scalability of our model. Then we believe that our model can solve most of the problems.

<!-- b000044 | heading | pages [2] -->
Assumptions

<!-- b000045 | prose | pages [2] -->
Ignore the slim refugees country. The countries that have few refugees or receive few refugees do not have much influence on our model.

<!-- b000046 | prose | pages [2] -->
Ignore the time of preparation for transfer. The time of preparation for transfer cannot determine its significance completely, and we take the time of preparation for transfer into consideration when we discuss the mutual reference of all work.

<!-- b000047 | furniture | pages [3] -->
Team#46634

<!-- b000048 | furniture | pages [3] -->
page 2 of 22

<!-- b000049 | furniture | pages [3] -->


<!-- b000050 | furniture | pages [3] -->


<!-- b000051 | caption | pages [3] -->
Table 1 shows the definitions of the symbols.

<!-- b000052 | caption | pages [3] -->
Table 1 Symbol definition instruction

<!-- b000053 | prose | pages [3] -->
Symbol Meaning

<!-- b000054 | prose | pages [3] -->
1F the success rate of refugees arriving in safe-haven countries

<!-- b000055 | prose | pages [3] -->
(1)

<!-- b000056 | furniture | pages [3] -->


<!-- b000057 | prose | pages [3] -->
refugees’ psychological diathesis of their own diathesis F 1

<!-- b000058 | prose | pages [3] -->
(2)

<!-- b000059 | prose | pages [3] -->
refugees’ physical diathesis of their own diathesis F

<!-- b000060 | furniture | pages [3] -->


<!-- b000061 | prose | pages [3] -->
1

<!-- b000062 | prose | pages [3] -->
(3)

<!-- b000063 | prose | pages [3] -->
F

<!-- b000064 | furniture | pages [3] -->


<!-- b000065 | prose | pages [3] -->
refugees’ cultural accomplishment of their own diathesis 1

<!-- b000066 | prose | pages [3] -->
(4)

<!-- b000067 | furniture | pages [3] -->


<!-- b000068 | prose | pages [3] -->
refugees’ choice of route of their own diathesis F 1

<!-- b000069 | prose | pages [3] -->
F the influence that countries’ policy brings to refugees 2

<!-- b000070 | prose | pages [3] -->
(1)

<!-- b000071 | furniture | pages [3] -->


<!-- b000072 | prose | pages [3] -->
the religious policy of the country F 2

<!-- b000073 | prose | pages [3] -->
(2)

<!-- b000074 | prose | pages [3] -->
F

<!-- b000075 | furniture | pages [3] -->


<!-- b000076 | prose | pages [3] -->
the number of refugees the country can feed 2

<!-- b000077 | prose | pages [3] -->
(3)

<!-- b000078 | prose | pages [3] -->
F

<!-- b000079 | furniture | pages [3] -->


<!-- b000080 | prose | pages [3] -->
financial and material resources of the country 2

<!-- b000081 | prose | pages [3] -->
(4)

<!-- b000082 | prose | pages [3] -->
the policy of the country refugees passed F

<!-- b000083 | furniture | pages [3] -->


<!-- b000084 | prose | pages [3] -->
2

<!-- b000085 | prose | pages [3] -->
F the impact of some emergency events 3

<!-- b000086 | prose | pages [3] -->
(1)

<!-- b000087 | prose | pages [3] -->
F

<!-- b000088 | furniture | pages [3] -->


<!-- b000089 | prose | pages [3] -->
the threat of the terrorist in the route 3

<!-- b000090 | prose | pages [3] -->
(2)

<!-- b000091 | prose | pages [3] -->
F

<!-- b000092 | furniture | pages [3] -->


<!-- b000093 | prose | pages [3] -->
the threat of nature disaster in the route 3

<!-- b000094 | prose | pages [3] -->
GS

<!-- b000095 | furniture | pages [3] -->


<!-- b000096 | prose | pages [3] -->
Flag whether country i and country j have the same religion ,i j

<!-- b000097 | prose | pages [3] -->
Sr the saturation rate of the refugees in country i i

<!-- b000098 | prose | pages [3] -->
Sp the contribution rate for refugees i

<!-- b000099 | prose | pages [3] -->
Ds the refugee mortality ij

<!-- b000100 | prose | pages [3] -->
Pk the number of refugees from country i to country j ij

<!-- b000101 | prose | pages [3] -->
G the cost of refugees from country i to country j ij

<!-- b000102 | prose | pages [3] -->
( )t

<!-- b000103 | prose | pages [3] -->
Po the instant resources of safe-haven country

<!-- b000104 | furniture | pages [3] -->


<!-- b000105 | prose | pages [3] -->
j

<!-- b000106 | prose | pages [3] -->
( )t

<!-- b000107 | prose | pages [3] -->
PN the number of refugees that the safe-haven country can hold

<!-- b000108 | furniture | pages [3] -->


<!-- b000109 | prose | pages [3] -->
j

<!-- b000110 | prose | pages [3] -->
( )t

<!-- b000111 | prose | pages [3] -->
PK the instant number of the safe-haven country j received

<!-- b000112 | furniture | pages [3] -->


<!-- b000113 | prose | pages [3] -->
j

<!-- b000114 | prose | pages [3] -->
The degree of discrepancy on environment and Climate between refugee- Ha

<!-- b000115 | prose | pages [3] -->
exporting i and the  safe-haven country j

<!-- b000116 | prose | pages [3] -->
ij

<!-- b000117 | prose | pages [3] -->
The degree of discrepancy on religion and law between exporting country Hb ij

<!-- b000118 | prose | pages [3] -->
economici and the  safe-haven country j

<!-- b000119 | prose | pages [3] -->
The degree of discrepancy on economic and culture between refugee- NG ij

<!-- b000120 | prose | pages [3] -->
exporting i and the  safe-haven country j

<!-- b000121 | prose | pages [3] -->
the transfer matrix of refugees from their country i to safe-haven country  ij Hp

<!-- b000122 | furniture | pages [3] -->


<!-- b000123 | prose | pages [3] -->
j

<!-- b000124 | prose | pages [3] -->
the  conflict between refugee-exporting country i and the safe-haven Wa ij country j

<!-- b000125 | prose | pages [3] -->
Pd The relationship between two safe-haven country(i and j ) ij

<!-- b000126 | furniture | pages [4] -->
Team#46634                                                                                                                                  page 3 of 22

<!-- b000127 | furniture | pages [4] -->


<!-- b000128 | prose | pages [4] -->
Task 1: Metrics of refugee crises

<!-- b000129 | prose | pages [4] -->
We consider the influence factors of the movement of refugees from three aspects. Firstly, in order to arrive at the asylum safely, the diathesis, which includes psychological diathesis, physical diathesis, the cultural accomplishment of refugees and the refugees’ choice of routes, is significant. Being refugees is a cruel thing, which is a heavy blow. If refugees do not have great psychological diathesis, they might be breakdown during the movement. Therefore, they cannot arrive at the asylum safely. It will be hard for them to complete the migration as well if the refugees are not healthy enough since the movement always be hard and taking a long time. Moreover, In the process of movement, refugees will go through many different countries and regions, thus a better understanding of the countries’ language, customs and cultural characteristics will surely help to increase the probability of fleeing successfully. As for refugees, there is often more than one route. Therefore, the choice of route, which is made by refugees, influences the success rate of movement. Choosing a safe and suitable route will increase the success rate of movement. On the other hand, once the refugees chose an unsuitable dangerous route for themselves, it would reduce the success rate of movement. [1]

<!-- b000130 | prose | pages [4] -->
    (1) (2) (3) F f F F F

<!-- b000131 | furniture | pages [4] -->


<!-- b000132 | prose | pages [4] -->
1 1 1

<!-- b000133 | prose | pages [4] -->
(1)

<!-- b000134 | prose | pages [4] -->
   (4) (5) F F (1) 1 1 1 1

<!-- b000135 | prose | pages [4] -->
means psychological diathesis of refugees’ diathesis F 1

<!-- b000136 | prose | pages [4] -->
(2)

<!-- b000137 | prose | pages [4] -->
means physical diathesis of refugees’ diathesis F 1

<!-- b000138 | prose | pages [4] -->
(3)

<!-- b000139 | prose | pages [4] -->
means the cultural accomplishment of refugees’ diathesis F 1

<!-- b000140 | prose | pages [4] -->
(4)

<!-- b000141 | prose | pages [4] -->
means the refugees’ choice of route of refugees’ abilities F 1

<!-- b000142 | prose | pages [4] -->
(5)

<!-- b000143 | prose | pages [4] -->
means the wealth of refugee F 1

<!-- b000144 | prose | pages [4] -->
We rank the five factors of the refugees with 1 to 10 representing capacity from low to

<!-- b000145 | furniture | pages [4] -->


<!-- b000146 | prose | pages [4] -->
high, then we have

<!-- b000147 | prose | pages [4] -->
      (1) (2) F F F

<!-- b000148 | furniture | pages [4] -->


<!-- b000149 | prose | pages [4] -->
1 11 1 12 1     (3) (4) (5) F F F (2) 13 13 1 14 1 15 1

<!-- b000150 | prose | pages [4] -->
For the contribution of these five factors，we are in accordance with the actual situation， then we have

<!-- b000151 | prose | pages [4] -->
   (1) (2) F 0.6 F 0.8 F

<!-- b000152 | furniture | pages [4] -->


<!-- b000153 | prose | pages [4] -->
1 1 1   (3) (4) (5) 0.4 F 0.3 F 0.2 F (3) 1 1 1

<!-- b000154 | prose | pages [4] -->
Secondly, as for the influence of the countries and regions where they stopped over, we

<!-- b000155 | furniture | pages [4] -->


<!-- b000156 | prose | pages [4] -->
believe factors of refugees, including the religious policy of countries, the number of refugees the countries can accommodate, the country's financial and material resources, the national policies on refugee. Meanwhile, the religious policy of the country has a great influence, because a large part of refugees’ movement is for religious persecution. And the number of refugees the country can accommodate influences the movement of refugees as well[2]. For

<!-- b000157 | furniture | pages [5] -->
Team#46634                                                                                                                                  page 4 of 22

<!-- b000158 | furniture | pages [5] -->


<!-- b000159 | prose | pages [5] -->
the current situation of highly developed information technology, most of the refugees will choose the best escape route, which is the most popular route. In this case, the

<!-- b000160 | prose | pages [5] -->
countries which are on the most popular route will undertake more pressure. If those countries can accommodate a large number of refugees, they will be bound to increase the success rate of refugees’ movement, which is on the contrary will have a negative impact on the refugees’ escape. For the country's financial and material resources, it can directly affect the process of refugees’ movement. As for refugees, they need to get funding from the country on the route, and this support is bound to affect the movement. Moreover, it is equally important for policies towards refugees in those countries. If the country is kind for refugees, then it will be beneficial to the refugees fleeing. On the contrary, if the country is against helping refugees, it will bring adverse effect to refugees fleeing[3].

<!-- b000161 | prose | pages [5] -->
   (1) F g F F

<!-- b000162 | furniture | pages [5] -->


<!-- b000163 | prose | pages [5] -->
2 2

<!-- b000164 | prose | pages [5] -->
(1)

<!-- b000165 | prose | pages [5] -->
means the religious policy of the country F 2

<!-- b000166 | prose | pages [5] -->
(2)

<!-- b000167 | prose | pages [5] -->
   (2) (3) (4) F F (4) 2 2 2

<!-- b000168 | prose | pages [5] -->
the number of refugees that the country can accommodate F 2

<!-- b000169 | prose | pages [5] -->
(3)

<!-- b000170 | prose | pages [5] -->
means the country's financial and material resources F 2

<!-- b000171 | prose | pages [5] -->
(4)

<!-- b000172 | prose | pages [5] -->
means the national policy on refugee F 2

<!-- b000173 | prose | pages [5] -->
We rank the four factors of the via countries，with 1 to 10 representative capacity from low to high，then we have

<!-- b000174 | prose | pages [5] -->
    (1) F F 2 21 2 22

<!-- b000175 | furniture | pages [5] -->


<!-- b000176 | prose | pages [5] -->
    (2) (3) (4) F F F 2 23 2 24 2 (5)

<!-- b000177 | prose | pages [5] -->
For the contribution of these four factors, we are in accordance with the actual situation， then we have

<!-- b000178 | prose | pages [5] -->
  (1) (2) F 0.9 F 0.8 F

<!-- b000179 | furniture | pages [5] -->


<!-- b000180 | prose | pages [5] -->
2 2   (3) (4) 0.5 F 0.4 F (6) 2 2 2 2

<!-- b000181 | prose | pages [5] -->
Thirdly, several external factors also have a certain impact on refugees’ movement.

<!-- b000182 | furniture | pages [5] -->


<!-- b000183 | prose | pages [5] -->
Meanwhile, the illness, nature disaster and the threat of terrorist on the route are important as well. From the point of the refugees’ safety, the impact of these factors on the refugees is more obvious.

<!-- b000184 | prose | pages [5] -->
  F h F 3

<!-- b000185 | furniture | pages [5] -->


<!-- b000186 | prose | pages [5] -->
(1)

<!-- b000187 | prose | pages [5] -->
F

<!-- b000188 | prose | pages [5] -->
  (1) (2) F 3 3 (7)

<!-- b000189 | prose | pages [5] -->
means the threat of the terrorist in the route 3

<!-- b000190 | prose | pages [5] -->
(2)

<!-- b000191 | prose | pages [5] -->
F means the illness, nature disaster in the route

<!-- b000192 | furniture | pages [5] -->


<!-- b000193 | prose | pages [5] -->
3

<!-- b000194 | prose | pages [5] -->
We rank the two factors of the refugees with 10 to 1 representing capacity from low to

<!-- b000195 | furniture | pages [5] -->


<!-- b000196 | prose | pages [5] -->
high，then we have

<!-- b000197 | furniture | pages [6] -->
Team#46634

<!-- b000198 | prose | pages [6] -->
  F F

<!-- b000199 | furniture | pages [6] -->


<!-- b000200 | prose | pages [6] -->
3 31

<!-- b000201 | furniture | pages [6] -->
page 5 of 22

<!-- b000202 | furniture | pages [6] -->


<!-- b000203 | furniture | pages [6] -->


<!-- b000204 | prose | pages [6] -->
  (1) (1) (2) F (8) 3 32 3

<!-- b000205 | prose | pages [6] -->
For the contribution of these two factors，we are in accordance with the actual situation， then we have

<!-- b000206 | prose | pages [6] -->
 (1) F 0.8 F

<!-- b000207 | furniture | pages [6] -->


<!-- b000208 | prose | pages [6] -->
3  (2) 0.8 F (9) 3 3 3

<!-- b000209 | prose | pages [6] -->
Among the factors that we have discussed above, the refugees’ diathesis is the most direct, the policy countries refugees transfer through is the most important, the refugees’ movement in the route is the most intense. Then we have

<!-- b000210 | prose | pages [6] -->
  F v F 1

<!-- b000211 | furniture | pages [6] -->


<!-- b000212 | prose | pages [6] -->
    F F

<!-- b000213 | furniture | pages [6] -->


<!-- b000214 | prose | pages [6] -->
1 1

<!-- b000215 | prose | pages [6] -->
  F 0.7 F

<!-- b000216 | furniture | pages [6] -->


<!-- b000217 | prose | pages [6] -->
1

<!-- b000218 | prose | pages [6] -->
10

<!-- b000219 | prose | pages [6] -->
9

<!-- b000220 | prose | pages [6] -->
8

<!-- b000221 | prose | pages [6] -->
7

<!-- b000222 | prose | pages [6] -->
6

<!-- b000223 | prose | pages [6] -->
Degree/De

<!-- b000224 | prose | pages [6] -->
5

<!-- b000225 | prose | pages [6] -->
4

<!-- b000226 | prose | pages [6] -->
3

<!-- b000227 | prose | pages [6] -->
2

<!-- b000228 | prose | pages [6] -->
1

<!-- b000229 | furniture | pages [6] -->


<!-- b000230 | prose | pages [6] -->
0 1 2 3 4

<!-- b000231 | prose | pages [6] -->
    F F 2 3 (10)

<!-- b000232 | prose | pages [6] -->
  F F (11) 2 2 2 3 3

<!-- b000233 | prose | pages [6] -->
 0.8 F 0.9 F (12) 2 3

<!-- b000234 | furniture | pages [6] -->


<!-- b000235 | prose | pages [6] -->
Mentality Physical Culture Choice Ability Resource

<!-- b000236 | prose | pages [6] -->
5 6 7 8 9 10

<!-- b000237 | prose | pages [6] -->
Capacity/Ca

<!-- b000238 | furniture | pages [6] -->


<!-- b000239 | caption | pages [6] -->
Figure 1 Different factor influence

<!-- b000240 | prose | pages [6] -->
As indicated in Figure 1, the optimization of all parameters will improve the transfer rate of the refugees. But,the degree of ascension is not exactly the same. And as we can see, the physical quality is the first ,mentally quality is the second, the literacy is the third,the choise ability is the fourth,and the resource is the last.

<!-- b000241 | prose | pages [6] -->
20

<!-- b000242 | prose | pages [6] -->
15

<!-- b000243 | prose | pages [6] -->
Influence

<!-- b000244 | prose | pages [6] -->
10

<!-- b000245 | prose | pages [6] -->
5

<!-- b000246 | prose | pages [6] -->
0 10

<!-- b000247 | prose | pages [6] -->
8

<!-- b000248 | prose | pages [6] -->
5

<!-- b000249 | prose | pages [6] -->
6 4 2

<!-- b000250 | prose | pages [6] -->
0

<!-- b000251 | prose | pages [6] -->
0

<!-- b000252 | prose | pages [6] -->
Country Resource Region

<!-- b000253 | prose | pages [6] -->
20

<!-- b000254 | prose | pages [6] -->
15

<!-- b000255 | prose | pages [6] -->
Influence

<!-- b000256 | prose | pages [6] -->
10

<!-- b000257 | prose | pages [6] -->
5

<!-- b000258 | prose | pages [6] -->
0 10

<!-- b000259 | prose | pages [6] -->
10

<!-- b000260 | prose | pages [6] -->
10 10

<!-- b000261 | prose | pages [6] -->
8

<!-- b000262 | prose | pages [6] -->
5

<!-- b000263 | prose | pages [6] -->
6 4 2

<!-- b000264 | prose | pages [6] -->
0

<!-- b000265 | prose | pages [6] -->
0

<!-- b000266 | prose | pages [6] -->
Space Region

<!-- b000267 | furniture | pages [6] -->


<!-- b000268 | furniture | pages [7] -->
Team#46634

<!-- b000269 | furniture | pages [7] -->
page 6 of  22

<!-- b000270 | furniture | pages [7] -->


<!-- b000271 | furniture | pages [7] -->


<!-- b000272 | caption | pages [7] -->
Figure 2 Different paremeter 1                        Figure 3 Different paremeter 2

<!-- b000273 | furniture | pages [7] -->


<!-- b000274 | prose | pages [7] -->
15

<!-- b000275 | prose | pages [7] -->
10

<!-- b000276 | prose | pages [7] -->
Influence

<!-- b000277 | prose | pages [7] -->
5

<!-- b000278 | prose | pages [7] -->
0 10

<!-- b000279 | prose | pages [7] -->
10 8

<!-- b000280 | prose | pages [7] -->
5

<!-- b000281 | prose | pages [7] -->
6 4 2

<!-- b000282 | prose | pages [7] -->
0

<!-- b000283 | prose | pages [7] -->
0

<!-- b000284 | prose | pages [7] -->
Policy Region

<!-- b000285 | prose | pages [7] -->
15

<!-- b000286 | prose | pages [7] -->
10

<!-- b000287 | prose | pages [7] -->
Influence

<!-- b000288 | prose | pages [7] -->
5

<!-- b000289 | prose | pages [7] -->
0 10

<!-- b000290 | prose | pages [7] -->
10 8

<!-- b000291 | prose | pages [7] -->
5

<!-- b000292 | prose | pages [7] -->
6 4 2

<!-- b000293 | prose | pages [7] -->
0

<!-- b000294 | prose | pages [7] -->
0

<!-- b000295 | prose | pages [7] -->
Country Resource

<!-- b000296 | furniture | pages [7] -->


<!-- b000297 | prose | pages [7] -->
Space

<!-- b000298 | caption | pages [7] -->
Figure 4 Different paremeter 3                        Figure 5 Different paremeter 4

<!-- b000299 | prose | pages [7] -->
To make a further study, we made Figure 2-Figure7 to observe the influence of different parameters. And from the results, we can find the slight difference.

<!-- b000300 | prose | pages [7] -->
Task 2: Flow of refugees

<!-- b000301 | prose | pages [7] -->
According to the information given in the task, we find that the refugees are mainly from Syria, Afghanistan, Eritrea, Kosovo and other areas. Their destinations are mainly countries such as Greece, Bulgaria, Italy, Spain, Malta and Cyprus. In this task, we mainly aim at the evaluation factors and parameters given in task 1, given the total number of refugees can be assumed, as well as the entry rate for each country at the entrance. To begin with, we identify the geographical relations between the 4 main refugee-exporting countries and the six refugee-receiving countries, the relations between the religious belief of these countries and taking the process from the entrance of the country transferring to other countries as a second shift into account [4].

<!-- b000302 | prose | pages [7] -->
Firstly, we consider the religious belief relations among the main refugee-exporting countries, the main refugee-receiving countries and second shifting countries. According to our assumption, religion is the decisive factor of the refugees’ movement, which means if their religions are different, there will not be transfer among the countries.

<!-- b000303 | caption | pages [7] -->
Table 2  The religious belief of the countries.

<!-- b000304 | prose | pages [7] -->
Country Region Greece The Orthodox Eastern Church Italy The Catholicism (90%)

<!-- b000305 | prose | pages [7] -->
The Orthodox Eastern Church

<!-- b000306 | prose | pages [7] -->
Bulgaria

<!-- b000307 | prose | pages [7] -->
(90%) The Mohammedanism (10%)

<!-- b000308 | furniture | pages [7] -->


<!-- b000309 | prose | pages [7] -->
Country Region Spain The Catholicism (90%) Malta The Catholicism

<!-- b000310 | prose | pages [7] -->
The Orthodox Church (50%) Cyprus The Mohammedanism (50%)

<!-- b000311 | prose | pages [7] -->
Then we consider the main reason why the refugee countries have refugees. The main refugee countries are Syria, Afghanistan, Kosovo, Iraq, Albania, Pakistan, Eritrea, Nigeria, Serbia and Ukraine. Most of the countries which have experienced or are now enduring the war and conflict, and like the Eritrea become refugees exporter mainly because their citizen

<!-- b000312 | furniture | pages [8] -->
Team#46634

<!-- b000313 | furniture | pages [8] -->
page 7 of 22

<!-- b000314 | furniture | pages [8] -->


<!-- b000315 | furniture | pages [8] -->


<!-- b000316 | prose | pages [8] -->
suffering long-term abuse. For Kosovo, it is the war that led to the long-term poverty, in this case , the refugees’ mental are likely to exist some problems, and other qualities of refugees may not that important of the refugees’ movement[5].

<!-- b000317 | prose | pages [8] -->
Afterwards, the financial and material resources of the refugee-receiving countries should take into account.  As for the six refugee-receiving countries, Greece and Italy can accommodate more refugees, but the financial and material resources of the Bulgaria, Malta and Cyprus are slightly weaker. For the second shifting countries, Germany, Sweden, Switzerland and other countries are great power. And we give the essential information in

<!-- b000318 | caption | pages [8] -->
Table3 to Table 6.

<!-- b000319 | caption | pages [8] -->
Table 3  The religious belief of the refugee-export countries.

<!-- b000320 | prose | pages [8] -->
Country Region

<!-- b000321 | prose | pages [8] -->
Syria The Mohammedanism(most) Afghanista

<!-- b000322 | prose | pages [8] -->
The Mohammedanism n

<!-- b000323 | prose | pages [8] -->
The Mohammedanism (50%) Eritrea

<!-- b000324 | prose | pages [8] -->
The Christianity (50%)

<!-- b000325 | prose | pages [8] -->
The Mohammedanism(most) Iraq

<!-- b000326 | prose | pages [8] -->
The Christianity

<!-- b000327 | prose | pages [8] -->
The Orthodox Eastern

<!-- b000328 | prose | pages [8] -->
Church(70%)

<!-- b000329 | prose | pages [8] -->
Ukraine

<!-- b000330 | prose | pages [8] -->
The Mohammedanism (20%)

<!-- b000331 | prose | pages [8] -->
The Buddhism

<!-- b000332 | furniture | pages [8] -->


<!-- b000333 | prose | pages [8] -->
Countr

<!-- b000334 | prose | pages [8] -->
Region y

<!-- b000335 | prose | pages [8] -->
Pakistan The Mohammedanism

<!-- b000336 | prose | pages [8] -->
Kosovo The Mohammedanism

<!-- b000337 | prose | pages [8] -->
The Mohammedanism

<!-- b000338 | prose | pages [8] -->
Nigeria

<!-- b000339 | prose | pages [8] -->
(50%) The Christianity (50%)

<!-- b000340 | prose | pages [8] -->
The Orthodox Eastern

<!-- b000341 | prose | pages [8] -->
Serbia

<!-- b000342 | prose | pages [8] -->
Church The Christianity

<!-- b000343 | furniture | pages [8] -->


<!-- b000344 | prose | pages [8] -->
The Mohammedanism

<!-- b000345 | caption | pages [8] -->
Table 4  The religious belief of the refugee-receiving countries

<!-- b000346 | prose | pages [8] -->
Country Region Austria The Catholicism Belgium The Christianity Luxembourg The Catholicism（90%） Germany The Christianity Spain The Catholicism（90%）

<!-- b000347 | prose | pages [8] -->
the Orthodox Eastern Church Bulgaria

<!-- b000348 | prose | pages [8] -->
The Mohammedanism (10%)

<!-- b000349 | prose | pages [8] -->
The Catholicism Netherlands

<!-- b000350 | prose | pages [8] -->
The Protestant

<!-- b000351 | prose | pages [8] -->
The Christianity

<!-- b000352 | prose | pages [8] -->
Latvia

<!-- b000353 | prose | pages [8] -->
the Orthodox Eastern Church

<!-- b000354 | prose | pages [8] -->
The Luther Protestant

<!-- b000355 | furniture | pages [8] -->


<!-- b000356 | prose | pages [8] -->
Country Region Finland The Christianity Malta The Catholicism Poland The Catholicism Portugal The Christianity Sweden The Christianity

<!-- b000357 | prose | pages [8] -->
The Orthodox Church (50%) Cyprus The Mohammedanism (50%)

<!-- b000358 | prose | pages [8] -->
The Catholicism (90%) Slovakia

<!-- b000359 | prose | pages [8] -->
The Christianity

<!-- b000360 | prose | pages [8] -->
Romania the Orthodox Eastern Church

<!-- b000361 | caption | pages [8] -->
Table 5  the GDP and Population of nations

<!-- b000362 | prose | pages [8] -->
Country ADGP Population Italy 33115 59685227 Spain 29289 47265321 Cyprus 26389 1117000

<!-- b000363 | furniture | pages [8] -->


<!-- b000364 | prose | pages [8] -->
Country ADGP Population Greece 22055 10815197 Malta 20852 452515 Bulgaria 7033 7364570

<!-- b000365 | furniture | pages [9] -->
Team#46634

<!-- b000366 | furniture | pages [9] -->
page 8 of 22

<!-- b000367 | furniture | pages [9] -->


<!-- b000368 | furniture | pages [9] -->


<!-- b000369 | caption | pages [9] -->
Table 6  the GDP and Population of nations

<!-- b000370 | prose | pages [9] -->
Country ADGP Population Sweden 56956 9555893 Austria 47083 8032926 Netherlands 46142 16788973 Finland 46098 5421827 Belgium 43686 11035948 Germany 41513 80399300 Spain 29289 47265321 Cyprus 26389 1117000

<!-- b000371 | furniture | pages [9] -->


<!-- b000372 | prose | pages [9] -->
Country ADGP Population Malta 20852 452515 Portugal 20178 10487289 Slovakia 16726 5410836 Latvia 13899 2217000 Poland 13540 38186860 Rumania 7934 20121641 Bulgaria 7033 7364570 Luxembourg 107206 537853

<!-- b000373 | prose | pages [9] -->
When it comes to the refugee policy of the refugee-receiving countries, for most of these countries are the members of EU, so most of their policies for refugees are loose. However, because some countries do not have a large population, receiving more refugees will inevitably lead to its population imbalance and brings some social problems, so there will be a certain number of restrictions on the number of refugees[6].

<!-- b000374 | furniture | pages [9] -->


<!-- b000375 | prose | pages [9] -->
Syria

<!-- b000376 | prose | pages [9] -->
Greece

<!-- b000377 | prose | pages [9] -->
Afghanistan

<!-- b000378 | prose | pages [9] -->
Kosovo

<!-- b000379 | prose | pages [9] -->
Bulgaria

<!-- b000380 | prose | pages [9] -->
Iraq

<!-- b000381 | prose | pages [9] -->
Italy

<!-- b000382 | prose | pages [9] -->
Pakistan

<!-- b000383 | prose | pages [9] -->
Spain

<!-- b000384 | prose | pages [9] -->
Eritrea

<!-- b000385 | prose | pages [9] -->
Nigeria

<!-- b000386 | prose | pages [9] -->
Malta

<!-- b000387 | prose | pages [9] -->
Serbia

<!-- b000388 | prose | pages [9] -->
Cyprus

<!-- b000389 | prose | pages [9] -->
Ukraine

<!-- b000390 | prose | pages [9] -->
Austria Luxembourg

<!-- b000391 | prose | pages [9] -->
Malta Poland

<!-- b000392 | prose | pages [9] -->
Spain

<!-- b000393 | prose | pages [9] -->
Belgium

<!-- b000394 | prose | pages [9] -->
Finland Germany

<!-- b000395 | prose | pages [9] -->
Portugal

<!-- b000396 | prose | pages [9] -->
Sweden

<!-- b000397 | prose | pages [9] -->
Bulgaria

<!-- b000398 | prose | pages [9] -->
Cyprus

<!-- b000399 | prose | pages [9] -->
Slovakia

<!-- b000400 | prose | pages [9] -->
Latvi

<!-- b000401 | prose | pages [9] -->
Netherlands

<!-- b000402 | prose | pages [9] -->
Romania

<!-- b000403 | furniture | pages [9] -->


<!-- b000404 | caption | pages [9] -->
Figure 6 Transfer Permission Situation

<!-- b000405 | prose | pages [9] -->
When considering external factors, we mainly think about refugees finish the transfer whether by land or by water. Because of the pirate and the stormy waves in the sea, the mortality of transferring by water is higher than by land.

<!-- b000406 | furniture | pages [9] -->


<!-- b000407 | prose | pages [9] -->
  

<!-- b000408 | prose | pages [9] -->
GS

<!-- b000409 | prose | pages [9] -->
(

<!-- b000410 | prose | pages [9] -->
i j

<!-- b000411 | prose | pages [9] -->
,

<!-- b000412 | prose | pages [9] -->
  

<!-- b000413 | prose | pages [9] -->
i

<!-- b000414 | prose | pages [9] -->
1,2, ,10;

<!-- b000415 | furniture | pages [9] -->


<!-- b000416 | prose | pages [9] -->


<!-- b000417 | prose | pages [9] -->
re re

<!-- b000418 | prose | pages [9] -->
, )

<!-- b000419 | prose | pages [9] -->
i i j

<!-- b000420 | prose | pages [9] -->
 

<!-- b000421 | prose | pages [9] -->
(13)

<!-- b000422 | prose | pages [9] -->
j

<!-- b000423 | prose | pages [9] -->
1,2, 25.

<!-- b000424 | prose | pages [9] -->
，means nation i and nation j have the same religion, GS 1 i j ,

<!-- b000425 | furniture | pages [10] -->
Team#46634

<!-- b000426 | prose | pages [10] -->


<!-- b000427 | furniture | pages [10] -->
page 9 of 22

<!-- b000428 | furniture | pages [10] -->


<!-- b000429 | furniture | pages [10] -->


<!-- b000430 | prose | pages [10] -->
，means nation i and nation j have different religion GS 0 i j ,

<!-- b000431 | prose | pages [10] -->
Define the saturation rate of the refugees:

<!-- b000432 | prose | pages [10] -->
 

<!-- b000433 | prose | pages [10] -->
Sr

<!-- b000434 | prose | pages [10] -->


<!-- b000435 | prose | pages [10] -->
i

<!-- b000436 | furniture | pages [10] -->


<!-- b000437 | prose | pages [10] -->


<!-- b000438 | prose | pages [10] -->
i

<!-- b000439 | prose | pages [10] -->
 

<!-- b000440 | prose | pages [10] -->
Max

<!-- b000441 | prose | pages [10] -->
_

<!-- b000442 | prose | pages [10] -->
r

<!-- b000443 | prose | pages [10] -->
i

<!-- b000444 | prose | pages [10] -->
Num

<!-- b000445 | prose | pages [10] -->
i

<!-- b000446 | prose | pages [10] -->
(14)

<!-- b000447 | prose | pages [10] -->


<!-- b000448 | prose | pages [10] -->
1,2, ,10

<!-- b000449 | prose | pages [10] -->
r means the maximum number of refugees accepted by the refugee-receiving country Max _ i

<!-- b000450 | prose | pages [10] -->
Num means the population of the refugee-receiving country i

<!-- b000451 | prose | pages [10] -->
Define the contribution rate of refugees,

<!-- b000452 | prose | pages [10] -->
 

<!-- b000453 | prose | pages [10] -->
Sp i

<!-- b000454 | prose | pages [10] -->


<!-- b000455 | furniture | pages [10] -->


<!-- b000456 | prose | pages [10] -->


<!-- b000457 | prose | pages [10] -->
i

<!-- b000458 | prose | pages [10] -->
1,2,

<!-- b000459 | prose | pages [10] -->
 

<!-- b000460 | prose | pages [10] -->
GDP p i i

<!-- b000461 | prose | pages [10] -->
(15)

<!-- b000462 | prose | pages [10] -->


<!-- b000463 | prose | pages [10] -->
25.

<!-- b000464 | prose | pages [10] -->
GDP means annual GDP of the refugee-receiving country i i

<!-- b000465 | prose | pages [10] -->
ip means the contribution rate of refugees of the refugee-receiving country i

<!-- b000466 | prose | pages [10] -->
ip is not only include economic strength of the refugee-receiving country i, but the refugee

<!-- b000467 | prose | pages [10] -->
policy as well.

<!-- b000468 | prose | pages [10] -->
Define the refugee mortality，

<!-- b000469 | prose | pages [10] -->


<!-- b000470 | prose | pages [10] -->
Ds ij

<!-- b000471 | prose | pages [10] -->


<!-- b000472 | furniture | pages [10] -->


<!-- b000473 | prose | pages [10] -->


<!-- b000474 | prose | pages [10] -->
i

<!-- b000475 | prose | pages [10] -->
1,2, ,10,

<!-- b000476 | prose | pages [10] -->
  

<!-- b000477 | prose | pages [10] -->
Dr ij

<!-- b000478 | prose | pages [10] -->
(16)

<!-- b000479 | prose | pages [10] -->
 

<!-- b000480 | prose | pages [10] -->
j j

<!-- b000481 | prose | pages [10] -->
1,2, ,25.

<!-- b000482 | prose | pages [10] -->
Dr only has two values，if the two countries i and j are connected by water , ij

<!-- b000483 | prose | pages [10] -->
Dr =0.005. Or they are connected by land, ij

<!-- b000484 | prose | pages [10] -->
Dr =0.08 ij

<!-- b000485 | prose | pages [10] -->
Therefore the total number of refugees can be accommodated is

<!-- b000486 | prose | pages [10] -->
10 25

<!-- b000487 | prose | pages [10] -->
 

<!-- b000488 | furniture | pages [10] -->


<!-- b000489 | prose | pages [10] -->
A GS s   i 1 j 1

<!-- b000490 | prose | pages [10] -->
6

<!-- b000491 | prose | pages [10] -->


<!-- b000492 | prose | pages [10] -->


<!-- b000493 | prose | pages [10] -->
max

<!-- b000494 | prose | pages [10] -->
A GS

<!-- b000495 | prose | pages [10] -->
s

<!-- b000496 | prose | pages [10] -->
 

<!-- b000497 | prose | pages [10] -->
i

<!-- b000498 | prose | pages [10] -->
1

<!-- b000499 | prose | pages [10] -->
j

<!-- b000500 | prose | pages [10] -->
1

<!-- b000501 | prose | pages [10] -->


<!-- b000502 | prose | pages [10] -->
25 25

<!-- b000503 | prose | pages [10] -->
 

<!-- b000504 | prose | pages [10] -->


<!-- b000505 | prose | pages [10] -->
Pk Max

<!-- b000506 | prose | pages [10] -->


<!-- b000507 | prose | pages [10] -->
ij

<!-- b000508 | prose | pages [10] -->
 

<!-- b000509 | prose | pages [10] -->
j

<!-- b000510 | prose | pages [10] -->
1

<!-- b000511 | prose | pages [10] -->
j

<!-- b000512 | prose | pages [10] -->
1

<!-- b000513 | prose | pages [10] -->


<!-- b000514 | furniture | pages [10] -->


<!-- b000515 | prose | pages [10] -->


<!-- b000516 | prose | pages [10] -->
25

<!-- b000517 | prose | pages [10] -->


<!-- b000518 | prose | pages [10] -->
 

<!-- b000519 | prose | pages [10] -->
Pk G Sp

<!-- b000520 | prose | pages [10] -->


<!-- b000521 | prose | pages [10] -->
ij ij

<!-- b000522 | prose | pages [10] -->


<!-- b000523 | prose | pages [10] -->


<!-- b000524 | prose | pages [10] -->
j

<!-- b000525 | prose | pages [10] -->
1

<!-- b000526 | prose | pages [10] -->
  

<!-- b000527 | prose | pages [10] -->
i

<!-- b000528 | prose | pages [10] -->
1,2, ,10.

<!-- b000529 | prose | pages [10] -->


<!-- b000530 | prose | pages [10] -->
 (17) Pk ij ij

<!-- b000531 | prose | pages [10] -->


<!-- b000532 | prose | pages [10] -->
Pk

<!-- b000533 | prose | pages [10] -->
ij ij ij

<!-- b000534 | prose | pages [10] -->
25

<!-- b000535 | prose | pages [10] -->


<!-- b000536 | prose | pages [10] -->
 

<!-- b000537 | prose | pages [10] -->
_ _

<!-- b000538 | prose | pages [10] -->
r Num Sr

<!-- b000539 | prose | pages [10] -->
i i i

<!-- b000540 | prose | pages [10] -->


<!-- b000541 | prose | pages [10] -->
j

<!-- b000542 | prose | pages [10] -->
1

<!-- b000543 | prose | pages [10] -->
(18)

<!-- b000544 | prose | pages [10] -->
i i

<!-- b000545 | furniture | pages [11] -->
Team#46634

<!-- b000546 | furniture | pages [11] -->
page 10 of 22

<!-- b000547 | furniture | pages [11] -->


<!-- b000548 | furniture | pages [11] -->


<!-- b000549 | prose | pages [11] -->
Pk means the number of refugees from the refugee-exporting country I to the refugee- ij receiving country j

<!-- b000550 | prose | pages [11] -->
G means the cost of the refugee-receiving country i receive one refugee from the

<!-- b000551 | furniture | pages [11] -->


<!-- b000552 | prose | pages [11] -->
ij

<!-- b000553 | prose | pages [11] -->
refugee country j

<!-- b000554 | prose | pages [11] -->
We calculate the number of refugees that transfer from refugee- exporting country(i) to Rn with formula the refugee-receiving country(j) ij

<!-- b000555 | prose | pages [11] -->
   

<!-- b000556 | prose | pages [11] -->
Rn

<!-- b000557 | prose | pages [11] -->
max

<!-- b000558 | prose | pages [11] -->
A Ds Sp

<!-- b000559 | prose | pages [11] -->


<!-- b000560 | prose | pages [11] -->
ij s ij

<!-- b000561 | furniture | pages [11] -->


<!-- b000562 | prose | pages [11] -->
  

<!-- b000563 | prose | pages [11] -->
i

<!-- b000564 | prose | pages [11] -->
1,2, ,10;

<!-- b000565 | prose | pages [11] -->
j

<!-- b000566 | prose | pages [11] -->
1,2,

<!-- b000567 | prose | pages [11] -->
 

<!-- b000568 | prose | pages [11] -->
Max

<!-- b000569 | prose | pages [11] -->
_

<!-- b000570 | prose | pages [11] -->
r

<!-- b000571 | prose | pages [11] -->


<!-- b000572 | prose | pages [11] -->
i

<!-- b000573 | prose | pages [11] -->
(

<!-- b000574 | prose | pages [11] -->
GS

<!-- b000575 | prose | pages [11] -->
,

<!-- b000576 | prose | pages [11] -->
p

<!-- b000577 | prose | pages [11] -->
)

<!-- b000578 | prose | pages [11] -->
i i i j

<!-- b000579 | prose | pages [11] -->
,

<!-- b000580 | prose | pages [11] -->
i

<!-- b000581 | prose | pages [11] -->
Num

<!-- b000582 | prose | pages [11] -->
i

<!-- b000583 | prose | pages [11] -->
(19)

<!-- b000584 | prose | pages [11] -->
25.

<!-- b000585 | prose | pages [11] -->
And then we can get the results with the help of MATLAB

<!-- b000586 | caption | pages [11] -->
Table 7  Number of Transfer

<!-- b000587 | furniture | pages [11] -->


<!-- b000588 | prose | pages [11] -->
Greece Bulgaria Syria 16788 34534 Afghanistan 12456 0 Kosovo 567 345 Iraq 1235 2456 Albania 2346 0 Pakistan 0 45 Eritrea 0 642 Nigeria 123 234 Serbia 665 0 Ukraine 0 0 Italy Spain Malta Cyorys 25 24546 45245 45234 642 43643 42364 23462 234 45643 45624 22346 0 12344 456 454 0 245 45 0 0 4524 44 0 45 546 0 435 0 464 4325 0 425 667 1245 345 0 45 452 0 As reached from the 2004’s and 2005’s data, we can predict the transfer rate with the number of refugees and the refugees transferred from refugee-exporting country (i) to the refugee-receiving country(j).and the average result is 50187 per month.

<!-- b000589 | prose | pages [11] -->
To show the results in detail, we show the transfer graph with the help of pajek.

<!-- b000590 | furniture | pages [12] -->
Team#46634

<!-- b000591 | furniture | pages [12] -->
page 11 of 22

<!-- b000592 | furniture | pages [12] -->


<!-- b000593 | furniture | pages [12] -->


<!-- b000594 | caption | pages [12] -->
Figure 7 Results of transfer

<!-- b000595 | prose | pages [12] -->
As we can see from the transfer graph, the transfer of refugees is a little sparse. And this can be explained plainly. Most of the transfer of refugees is influenced by the religion of the refugees, so it will be impossible for some refugees to transfer from a refugee-exporting country to a refugee-receiving country.

<!-- b000596 | furniture | pages [12] -->


<!-- b000597 | prose | pages [12] -->
Task 3: Dynamics of the Crisis

<!-- b000598 | prose | pages [12] -->
As time goes by, refugees themselves, the policy of the refugee-receiving countries or the external factors of the movement are not set in the stone. The refugees’ psychological diathesis, religious belief and wealth as well as the refugee-receiving countries’ financial and material resources and capability of refugees and the nature disaster will change over time. However, the refugees’ physical diathesis, the population and policy of the refugee-receiving country can be seen as fixed in a short time[7].

<!-- b000599 | prose | pages [12] -->
If the movement goes well, the refugees’ psychological diathesis will be better, but if it is not, their psychological diathesis will be worse. However, refugees’ wealth must be less during the movement. Also, their religious belief will be reformed gradually for necessity of themselves. Next, the refugee-receiving country’s financial and material resources and the capability of the refugee will change during the transfer time. If the refugees have gone to the so-called ideal destination, the ideal refugee-receiving country's financial and material resources, as well as the capacity to accommodate refugees will reduce. Besides, the impact of natural disasters, such as disease, weather and other natural disasters, in the process of refugee transfer, is a stochastic process.

<!-- b000600 | prose | pages [12] -->
However, if the transportation, religion, policy and the financial and material resources of the refugee-receiving country suit the refugee country, it will increase the refugees’ saturation capacity of the refugee-receiving country. Nevertheless, if the refugee-receiving country's financial and material resources are relatively adequate and the amount of refugees

<!-- b000601 | furniture | pages [13] -->
Team#46634

<!-- b000602 | furniture | pages [13] -->
page 12 of 22

<!-- b000603 | furniture | pages [13] -->


<!-- b000604 | furniture | pages [13] -->


<!-- b000605 | prose | pages [13] -->
received is little, it can increase the resource consumption of the refugees in the country,  on the contrary, it can reduce the resource consumption. Among them  the saturation capacity of the refugee-receiving country needs to be priority considered.

<!-- b000606 | prose | pages [13] -->
between refugee-exporting country i and the refugee-receiving country j will The GS ,i j

<!-- b000607 | prose | pages [13] -->
change

<!-- b000608 | prose | pages [13] -->
    

<!-- b000609 | prose | pages [13] -->
re re GS

<!-- b000610 | prose | pages [13] -->
(

<!-- b000611 | prose | pages [13] -->
i j

<!-- b000612 | prose | pages [13] -->
,

<!-- b000613 | prose | pages [13] -->
  

<!-- b000614 | prose | pages [13] -->
i

<!-- b000615 | prose | pages [13] -->
1,2, ,10,

<!-- b000616 | furniture | pages [13] -->


<!-- b000617 | prose | pages [13] -->


<!-- b000618 | prose | pages [13] -->


<!-- b000619 | prose | pages [13] -->
, , ) (

<!-- b000620 | prose | pages [13] -->
rp rp

<!-- b000621 | prose | pages [13] -->
, )

<!-- b000622 | prose | pages [13] -->
i i j i j

<!-- b000623 | prose | pages [13] -->
 

<!-- b000624 | prose | pages [13] -->
(20)

<!-- b000625 | prose | pages [13] -->
j

<!-- b000626 | prose | pages [13] -->
1,2, ,25.

<!-- b000627 | prose | pages [13] -->
has same definition in task 2. where ( re re , ) i j

<!-- b000628 | prose | pages [13] -->
 means if the refugee-exporting country i is reformed by the refugee- ( rp rp , ) i j

<!-- b000629 | prose | pages [13] -->
 ，or  receiving country j, so ( rp rp , ) 1 i j  . ( ( rp rp , ) 0 i j

<!-- b000630 | prose | pages [13] -->
Denote the refugee-receiving country's financial and material resources by j   j   PN , 1,2, 25. the capability of the refugee-receiving country by Po , 1,2, 25. j and j

<!-- b000631 | prose | pages [13] -->
j   PK , 1,2, 25. the amount of received refuges of the refugee-receiving country by

<!-- b000632 | prose | pages [13] -->
we have，

<!-- b000633 | prose | pages [13] -->


<!-- b000634 | prose | pages [13] -->


<!-- b000635 | prose | pages [13] -->
( )

<!-- b000636 | prose | pages [13] -->
t

<!-- b000637 | prose | pages [13] -->
Po Po

<!-- b000638 | prose | pages [13] -->


<!-- b000639 | prose | pages [13] -->
j

<!-- b000640 | prose | pages [13] -->


<!-- b000641 | prose | pages [13] -->
j

<!-- b000642 | prose | pages [13] -->
1,2,

<!-- b000643 | prose | pages [13] -->
 

<!-- b000644 | prose | pages [13] -->
( )t

<!-- b000645 | prose | pages [13] -->
then j

<!-- b000646 | prose | pages [13] -->
( )

<!-- b000647 | prose | pages [13] -->
t

<!-- b000648 | prose | pages [13] -->
PK

<!-- b000649 | prose | pages [13] -->
j

<!-- b000650 | prose | pages [13] -->


<!-- b000651 | prose | pages [13] -->
(0)

<!-- b000652 | prose | pages [13] -->
j

<!-- b000653 | prose | pages [13] -->
Max

<!-- b000654 | prose | pages [13] -->
_

<!-- b000655 | prose | pages [13] -->
r

<!-- b000656 | prose | pages [13] -->
j

<!-- b000657 | furniture | pages [13] -->


<!-- b000658 | prose | pages [13] -->
,25.

<!-- b000659 | prose | pages [13] -->
means the instant financial and material resources of the refugee-exporting country Po j

<!-- b000660 | prose | pages [13] -->
( )t

<!-- b000661 | prose | pages [13] -->
means the instant financial and material resources of the refugee-exporting country Po j

<!-- b000662 | prose | pages [13] -->
(0)

<!-- b000663 | prose | pages [13] -->
Po means the financial and material resources of the refugee-exporting country j

<!-- b000664 | prose | pages [13] -->
( )t

<!-- b000665 | prose | pages [13] -->
Po means the instant financial and material resources of the refugee-exporting country j

<!-- b000666 | prose | pages [13] -->
(0)

<!-- b000667 | prose | pages [13] -->
Po means the financial and material resources of the refugee-exporting country j

<!-- b000668 | prose | pages [13] -->
( )t

<!-- b000669 | prose | pages [13] -->
PK means the instant amount of refugees that the refugee-exporting country recieived j

<!-- b000670 | prose | pages [13] -->
r means the refugees’ saturation capacity of the refugee-exporting country Max _ j

<!-- b000671 | prose | pages [13] -->
( ) ,     ( ) t (0) t PN PN PK j 1,2, ,25

<!-- b000672 | furniture | pages [13] -->


<!-- b000673 | prose | pages [13] -->
j j j

<!-- b000674 | prose | pages [13] -->
( )t

<!-- b000675 | prose | pages [13] -->
PN means the instant refugees’ capability of refugee-exporting country j

<!-- b000676 | prose | pages [13] -->
(0)

<!-- b000677 | prose | pages [13] -->
Po means the refugees’ capability of the refugee-exporting country at the beginning

<!-- b000678 | furniture | pages [13] -->


<!-- b000679 | prose | pages [13] -->
j

<!-- b000680 | furniture | pages [14] -->
Team#46634                                                                                                                                page 13 of 22

<!-- b000681 | prose | pages [14] -->
( )t

<!-- b000682 | furniture | pages [14] -->


<!-- b000683 | prose | pages [14] -->
means the instant amount of refugees received by the refugee-exporting country PK j

<!-- b000684 | furniture | pages [14] -->


<!-- b000685 | prose | pages [14] -->
If we add the refugees from Canada, China and U.S, our model is applicable to a certain extent, since the factors that should be considered are the same. However, people in these three countries are relatively concentrated in their religious beliefs, and the traffic to the refugee-receiving countries in Europe is complex as well as they are all great nations of politics, economics and culture. As a result, their refugees’ movement is complicated[8].

<!-- b000686 | prose | pages [14] -->
With the help of pajek, we show the result modified in the Figure 8.

<!-- b000687 | furniture | pages [14] -->


<!-- b000688 | furniture | pages [14] -->


<!-- b000689 | caption | pages [14] -->
Figure 8 Results of transfer in detail

<!-- b000690 | prose | pages [14] -->
The graph shows the results that adding more conditions , and the results can explain the phenomenon that is difficult to explain in task2.

<!-- b000691 | furniture | pages [15] -->
Team#46634                                                                                                                                page 13 of 22

<!-- b000692 | furniture | pages [15] -->


<!-- b000693 | furniture | pages [15] -->


<!-- b000694 | heading | pages [15] -->
Task 4: Policy to Support Refugee Model

<!-- b000695 | prose | pages [15] -->
Since the United Nations Commission requires us to give priority to the health and safety of the refugees and the local people, to the optimal conditions for the optimal migration model in this case, we adopt the method of loop analysis.

<!-- b000696 | prose | pages [15] -->
First of all, our ultimate goal is to ensure the health and safety of the refugees and the local people, as a result, we should choose the safe route and suitable refugee-receiving country. In order to ensure the health and safety of local people, we should try to control the transfer of the refugees in a suitable range. Meanwhile, the received refugees should be on the same level of religious belief and cultural attainments with the local people. In this case, we use the Space-time analysis of algorithm analysis, to find a balance between the amount of the transfer of refugees and refugee-receiving countries. Also, the consulates between the refugee-exporting country and the refugee-receiving country plays an important role, if the refugee-receiving country has a perfect  consulate which will lead the balance to the higher level. On the contrary, if its consulate is not that good, the balance will be low. Besides, some non-governmental organizations also play an important part. On one hand, these organizations can ensure the refugees’ safe and basic needs. On the other hand, they can protect the local people of the refugee-receiving country. In addition, we need to consider whether it is suitable for refugees to live in the receiving country, the conflict of weather, eating habit and life style between two countries should be taken into account[9].

<!-- b000697 | prose | pages [15] -->
Another factor that should be considered is the policy of the refugee-receiving country. Firstly, whether the refugees’ religious belief and habits are illegal in receiving country and whether there are conflicts of laws between two countries. Under the circumstances, for ensuring the safety of the refugees and local people is the most significant thing, the amount of refugees that can transfer to the receiving country will be smaller and the speed of the movement can be slower.

<!-- b000698 | prose | pages [15] -->
We define

<!-- b000699 | prose | pages [15] -->


<!-- b000700 | prose | pages [15] -->
  

<!-- b000701 | prose | pages [15] -->
(1)

<!-- b000702 | prose | pages [15] -->
Ha h ij

<!-- b000703 | prose | pages [15] -->
  

<!-- b000704 | furniture | pages [15] -->


<!-- b000705 | prose | pages [15] -->
i

<!-- b000706 | prose | pages [15] -->
1,2, ,10,

<!-- b000707 | prose | pages [15] -->
 

<!-- b000708 | prose | pages [15] -->


<!-- b000709 | prose | pages [15] -->


<!-- b000710 | prose | pages [15] -->
(2) (3) , ,

<!-- b000711 | prose | pages [15] -->
h

<!-- b000712 | prose | pages [15] -->
,

<!-- b000713 | prose | pages [15] -->
h

<!-- b000714 | prose | pages [15] -->
,

<!-- b000715 | prose | pages [15] -->
ij ij ij ij

<!-- b000716 | prose | pages [15] -->
(22)

<!-- b000717 | prose | pages [15] -->
 

<!-- b000718 | prose | pages [15] -->
j j

<!-- b000719 | prose | pages [15] -->
1,2, ,25.

<!-- b000720 | prose | pages [15] -->
means eating habit, life style and weather of the refugee-exporting country i and the

<!-- b000721 | prose | pages [15] -->
 0 Ha

<!-- b000722 | prose | pages [15] -->
( ) v

<!-- b000723 | prose | pages [15] -->
h

<!-- b000724 | prose | pages [15] -->
preset value is 1, for refugee-receiving country j ij

<!-- b000725 | prose | pages [15] -->
，if there is great conflict ij

<!-- b000726 | prose | pages [15] -->


<!-- b000727 | prose | pages [15] -->
( ) v

<!-- b000728 | prose | pages [15] -->
h

<!-- b000729 | prose | pages [15] -->
0.1

<!-- b000730 | prose | pages [15] -->
between refugee-exporting country i and the receiving country j，then

<!-- b000731 | prose | pages [15] -->


<!-- b000732 | prose | pages [15] -->
( ) v

<!-- b000733 | prose | pages [15] -->
h

<!-- b000734 | prose | pages [15] -->
0

<!-- b000735 | prose | pages [15] -->
ij

<!-- b000736 | furniture | pages [15] -->


<!-- b000737 | prose | pages [15] -->
，or ij

<!-- b000738 | prose | pages [15] -->
，finally

<!-- b000739 | furniture | pages [16] -->
Team#46634

<!-- b000740 | prose | pages [16] -->


<!-- b000741 | prose | pages [16] -->


<!-- b000742 | prose | pages [16] -->


<!-- b000743 | prose | pages [16] -->


<!-- b000744 | prose | pages [16] -->
(1) (2) (3)

<!-- b000745 | prose | pages [16] -->
Ha h

<!-- b000746 | prose | pages [16] -->
,

<!-- b000747 | prose | pages [16] -->
h

<!-- b000748 | prose | pages [16] -->
,

<!-- b000749 | prose | pages [16] -->
h

<!-- b000750 | prose | pages [16] -->


<!-- b000751 | prose | pages [16] -->
ij ij ij

<!-- b000752 | furniture | pages [16] -->


<!-- b000753 | prose | pages [16] -->
  

<!-- b000754 | furniture | pages [16] -->
page 15 of 22

<!-- b000755 | furniture | pages [16] -->


<!-- b000756 | furniture | pages [16] -->


<!-- b000757 | prose | pages [16] -->


<!-- b000758 | prose | pages [16] -->


<!-- b000759 | prose | pages [16] -->


<!-- b000760 | prose | pages [16] -->
0

<!-- b000761 | prose | pages [16] -->
 

<!-- b000762 | prose | pages [16] -->
( )

<!-- b000763 | prose | pages [16] -->
v

<!-- b000764 | prose | pages [16] -->
, ,

<!-- b000765 | prose | pages [16] -->
Ha h ij ij ij ij

<!-- b000766 | prose | pages [16] -->


<!-- b000767 | prose | pages [16] -->
v

<!-- b000768 | prose | pages [16] -->
1

<!-- b000769 | furniture | pages [16] -->


<!-- b000770 | prose | pages [16] -->
(23) ,25.

<!-- b000771 | prose | pages [16] -->
i

<!-- b000772 | prose | pages [16] -->
1,2, ,10,

<!-- b000773 | prose | pages [16] -->
j

<!-- b000774 | prose | pages [16] -->
1,2,

<!-- b000775 | prose | pages [16] -->
 

<!-- b000776 | prose | pages [16] -->
Ha  Ha  0 0 if ，then . ij ij

<!-- b000777 | prose | pages [16] -->
  ，means the comparison of religion, laws and   (1) (2) (3) Hb hb , hb , hb , Define ij ij ij ij

<!-- b000778 | prose | pages [16] -->
other points between refugee-exporting country i and the refugee-receiving country j. For ( ) v

<!-- b000779 | prose | pages [16] -->
，if there exist great conflict between refugee-exporting country i and refugee-

<!-- b000780 | prose | pages [16] -->
random

<!-- b000781 | prose | pages [16] -->
h ij

<!-- b000782 | prose | pages [16] -->
     (1) (2) (3) Hb hb , hb , hb , 0 factor, then receiving country j on this

<!-- b000783 | prose | pages [16] -->
    . (1) (2) (3) Hb hb , hb , hb , 1 ij ij ij ij

<!-- b000784 | prose | pages [16] -->
，or ij ij ij ij

<!-- b000785 | prose | pages [16] -->
We have the final transition probability matrix between i and j

<!-- b000786 | prose | pages [16] -->


<!-- b000787 | prose | pages [16] -->
Hp

<!-- b000788 | prose | pages [16] -->


<!-- b000789 | prose | pages [16] -->
Hp

<!-- b000790 | prose | pages [16] -->


<!-- b000791 | prose | pages [16] -->
   

<!-- b000792 | prose | pages [16] -->
  

<!-- b000793 | prose | pages [16] -->
Hp Ha Hb

<!-- b000794 | prose | pages [16] -->
ij ij

<!-- b000795 | prose | pages [16] -->


<!-- b000796 | prose | pages [16] -->
Hp

<!-- b000797 | prose | pages [16] -->
  

<!-- b000798 | prose | pages [16] -->
Hp Hp

<!-- b000799 | prose | pages [16] -->
11 11 12 1

<!-- b000800 | prose | pages [16] -->
v

<!-- b000801 | prose | pages [16] -->
 

<!-- b000802 | prose | pages [16] -->
Hp Hp

<!-- b000803 | prose | pages [16] -->


<!-- b000804 | prose | pages [16] -->
21 21 22 2

<!-- b000805 | prose | pages [16] -->
v

<!-- b000806 | prose | pages [16] -->
(24)

<!-- b000807 | prose | pages [16] -->
       

<!-- b000808 | prose | pages [16] -->
Hp Hp

<!-- b000809 | prose | pages [16] -->


<!-- b000810 | prose | pages [16] -->
v v

<!-- b000811 | prose | pages [16] -->
1 1

<!-- b000812 | prose | pages [16] -->
v

<!-- b000813 | prose | pages [16] -->
2

<!-- b000814 | prose | pages [16] -->
vv

<!-- b000815 | prose | pages [16] -->
Then we consider the impact of non-governmental organizations

<!-- b000816 | prose | pages [16] -->


<!-- b000817 | prose | pages [16] -->
  

<!-- b000818 | prose | pages [16] -->
(1)

<!-- b000819 | prose | pages [16] -->
NG ng

<!-- b000820 | prose | pages [16] -->
,

<!-- b000821 | prose | pages [16] -->
ng ij ij

<!-- b000822 | prose | pages [16] -->


<!-- b000823 | prose | pages [16] -->
Define

<!-- b000824 | prose | pages [16] -->
  

<!-- b000825 | prose | pages [16] -->


<!-- b000826 | prose | pages [16] -->


<!-- b000827 | prose | pages [16] -->
(2) (3) ,

<!-- b000828 | prose | pages [16] -->
ng

<!-- b000829 | prose | pages [16] -->
,

<!-- b000830 | prose | pages [16] -->
ij ij

<!-- b000831 | prose | pages [16] -->
(25)

<!-- b000832 | prose | pages [16] -->


<!-- b000833 | prose | pages [16] -->
1,2,

<!-- b000834 | prose | pages [16] -->
i

<!-- b000835 | prose | pages [16] -->
1,2, ,10,

<!-- b000836 | prose | pages [16] -->
j

<!-- b000837 | prose | pages [16] -->
 

<!-- b000838 | prose | pages [16] -->
,25.

<!-- b000839 | prose | pages [16] -->
means non-governmental organizations which include economy, culture, sports and so on.

<!-- b000840 | prose | pages [16] -->
 0 ng ( ) v

<!-- b000841 | prose | pages [16] -->


<!-- b000842 | prose | pages [16] -->
( ) v ，if it has interest between i and j, then

<!-- b000843 | furniture | pages [16] -->


<!-- b000844 | prose | pages [16] -->
preset value is 0，for

<!-- b000845 | prose | pages [16] -->
ng

<!-- b000846 | prose | pages [16] -->
ij

<!-- b000847 | prose | pages [16] -->
ij

<!-- b000848 | prose | pages [16] -->


<!-- b000849 | prose | pages [16] -->
( ) v or

<!-- b000850 | prose | pages [16] -->
，final ng

<!-- b000851 | prose | pages [16] -->
0

<!-- b000852 | prose | pages [16] -->
ij

<!-- b000853 | prose | pages [16] -->


<!-- b000854 | prose | pages [16] -->


<!-- b000855 | prose | pages [16] -->


<!-- b000856 | prose | pages [16] -->


<!-- b000857 | prose | pages [16] -->
(1) (2)

<!-- b000858 | prose | pages [16] -->
NG ng

<!-- b000859 | prose | pages [16] -->
,

<!-- b000860 | prose | pages [16] -->
ng

<!-- b000861 | prose | pages [16] -->
,

<!-- b000862 | prose | pages [16] -->
ng

<!-- b000863 | prose | pages [16] -->


<!-- b000864 | prose | pages [16] -->
ij ij ij

<!-- b000865 | furniture | pages [16] -->


<!-- b000866 | prose | pages [16] -->
  

<!-- b000867 | prose | pages [16] -->
i

<!-- b000868 | prose | pages [16] -->
1,2, ,10,

<!-- b000869 | prose | pages [16] -->
j

<!-- b000870 | prose | pages [16] -->
1,2, ,25.

<!-- b000871 | prose | pages [16] -->
 

<!-- b000872 | prose | pages [16] -->
Take this factor into account

<!-- b000873 | prose | pages [16] -->
  

<!-- b000874 | prose | pages [16] -->
Hp NG Hp

<!-- b000875 | prose | pages [16] -->
11 11 12

<!-- b000876 | prose | pages [16] -->
  

<!-- b000877 | prose | pages [16] -->
Hp NG Hp

<!-- b000878 | prose | pages [16] -->


<!-- b000879 | prose | pages [16] -->
   

<!-- b000880 | prose | pages [16] -->
'

<!-- b000881 | prose | pages [16] -->
  

<!-- b000882 | prose | pages [16] -->
21 21 22

<!-- b000883 | prose | pages [16] -->
Hp Hp NG

<!-- b000884 | prose | pages [16] -->
 

<!-- b000885 | prose | pages [16] -->
ij ij

<!-- b000886 | prose | pages [16] -->
  

<!-- b000887 | prose | pages [16] -->
Hp NG Hp

<!-- b000888 | prose | pages [16] -->


<!-- b000889 | prose | pages [16] -->
v

<!-- b000890 | prose | pages [16] -->
1

<!-- b000891 | prose | pages [16] -->
v

<!-- b000892 | prose | pages [16] -->
1

<!-- b000893 | prose | pages [16] -->
v

<!-- b000894 | prose | pages [16] -->
2

<!-- b000895 | furniture | pages [16] -->


<!-- b000896 | prose | pages [16] -->
ng

<!-- b000897 | prose | pages [16] -->
0.01

<!-- b000898 | prose | pages [16] -->
， ij

<!-- b000899 | prose | pages [16] -->


<!-- b000900 | prose | pages [16] -->


<!-- b000901 | prose | pages [16] -->


<!-- b000902 | prose | pages [16] -->
0

<!-- b000903 | prose | pages [16] -->
 

<!-- b000904 | prose | pages [16] -->
(3) ( )

<!-- b000905 | prose | pages [16] -->
v

<!-- b000906 | prose | pages [16] -->
,

<!-- b000907 | prose | pages [16] -->
NG ng ij ij ij

<!-- b000908 | prose | pages [16] -->


<!-- b000909 | prose | pages [16] -->
v

<!-- b000910 | prose | pages [16] -->
1

<!-- b000911 | prose | pages [16] -->
(26)

<!-- b000912 | prose | pages [16] -->
in the transition probability matrix

<!-- b000913 | prose | pages [16] -->
     

<!-- b000914 | prose | pages [16] -->
' ' '

<!-- b000915 | prose | pages [16] -->
NG Hp NG Hp Hp Hp

<!-- b000916 | prose | pages [16] -->
11 1

<!-- b000917 | prose | pages [16] -->
v

<!-- b000918 | prose | pages [16] -->
1

<!-- b000919 | prose | pages [16] -->
v

<!-- b000920 | prose | pages [16] -->
11 12 1

<!-- b000921 | prose | pages [16] -->
v

<!-- b000922 | prose | pages [16] -->
     

<!-- b000923 | prose | pages [16] -->
' ' '

<!-- b000924 | prose | pages [16] -->
NG Hp NG Hp Hp Hp

<!-- b000925 | prose | pages [16] -->
   

<!-- b000926 | prose | pages [16] -->
22 2

<!-- b000927 | prose | pages [16] -->
v

<!-- b000928 | prose | pages [16] -->
2

<!-- b000929 | prose | pages [16] -->
v

<!-- b000930 | prose | pages [16] -->
21 22 2

<!-- b000931 | prose | pages [16] -->
v

<!-- b000932 | prose | pages [16] -->
               

<!-- b000933 | prose | pages [16] -->
' ' '

<!-- b000934 | prose | pages [16] -->
NG Hp NG

<!-- b000935 | prose | pages [16] -->
 

<!-- b000936 | prose | pages [16] -->
Hp Hp Hp

<!-- b000937 | prose | pages [16] -->
  

<!-- b000938 | prose | pages [16] -->
v

<!-- b000939 | prose | pages [16] -->
2

<!-- b000940 | prose | pages [16] -->
vv vv v

<!-- b000941 | prose | pages [16] -->
1

<!-- b000942 | prose | pages [16] -->
v

<!-- b000943 | prose | pages [16] -->
2

<!-- b000944 | prose | pages [16] -->
vv

<!-- b000945 | prose | pages [16] -->
With the help of MATLAB, we can calculate the matrix, and the results are as follows,

<!-- b000946 | furniture | pages [17] -->
Team#46634

<!-- b000947 | furniture | pages [17] -->


<!-- b000948 | furniture | pages [17] -->


<!-- b000949 | prose | pages [17] -->


<!-- b000950 | prose | pages [17] -->
0.78 0.11

<!-- b000951 | prose | pages [17] -->


<!-- b000952 | prose | pages [17] -->
0.44 0.12

<!-- b000953 | prose | pages [17] -->
 

<!-- b000954 | prose | pages [17] -->


<!-- b000955 | prose | pages [17] -->
'

<!-- b000956 | prose | pages [17] -->
Hp

<!-- b000957 | prose | pages [17] -->
=

<!-- b000958 | prose | pages [17] -->
  

<!-- b000959 | prose | pages [17] -->
ij

<!-- b000960 | prose | pages [17] -->


<!-- b000961 | prose | pages [17] -->
0.66 0.61

<!-- b000962 | prose | pages [17] -->


<!-- b000963 | furniture | pages [17] -->
page 16 of 22

<!-- b000964 | furniture | pages [17] -->


<!-- b000965 | furniture | pages [17] -->


<!-- b000966 | prose | pages [17] -->
 

<!-- b000967 | prose | pages [17] -->
0.23

<!-- b000968 | prose | pages [17] -->
 

<!-- b000969 | prose | pages [17] -->
0

<!-- b000970 | prose | pages [17] -->


<!-- b000971 | prose | pages [17] -->
(27)

<!-- b000972 | prose | pages [17] -->
    

<!-- b000973 | prose | pages [17] -->
0.25

<!-- b000974 | prose | pages [17] -->


<!-- b000975 | prose | pages [17] -->
From the results, we can find out that cultural restraint and religion have important influence to our movement of refugees, so we suggest that give priority to the cultural restraint and religion.

<!-- b000976 | prose | pages [17] -->
Task 5: Exogenous Events

<!-- b000977 | prose | pages [17] -->
Taking exogenous events into consideration, some of the parameters like index of policies and regulations in our model may be significantly changed for these events happen suddenly. For example, once conflict break out between the refugees-exporting countries and the refugees-receiving countries, even the refugee-exporting countries make war on their neighbours and partners. In this case, the transfer from the refugee-exporting countries to these countries would be completely closed, and at the same time the refugees which belongs to refugee-exporting in these countries must be resettled in other countries. So it is mainly affected the saturated of the refugees receiving countries to other refugees receiving countries, which can instantly drop to zero. Surely, the policies of the refugees-treatment would also change. Compared with other factors, the most direct one is the external factors we have set, which can cause the increase of the death rate on some routes[10].

<!-- b000978 | prose | pages [17] -->
For the neighbour of refugees receiving countries, if the war break out between the refugee-exporting country and the receiving country, it will be a new receiving country. That’s because the refugees coming from exporting countries won’t come back to their hometown, and most of them will go to the neighbours of their living country. But the contradiction appears in that condition, the living country may put pressure on their neighbours to refuse the refugees.

<!-- b000979 | prose | pages [17] -->
Based on the above, we take more consideration of external factors in our model.

<!-- b000980 | prose | pages [17] -->


<!-- b000981 | prose | pages [17] -->
  

<!-- b000982 | prose | pages [17] -->
(1)

<!-- b000983 | prose | pages [17] -->
Wa Wa ij

<!-- b000984 | prose | pages [17] -->


<!-- b000985 | furniture | pages [17] -->


<!-- b000986 | prose | pages [17] -->
We define that

<!-- b000987 | prose | pages [17] -->
 

<!-- b000988 | prose | pages [17] -->
i

<!-- b000989 | prose | pages [17] -->
1,2, ,10,

<!-- b000990 | prose | pages [17] -->
 

<!-- b000991 | prose | pages [17] -->


<!-- b000992 | prose | pages [17] -->


<!-- b000993 | prose | pages [17] -->
(2) (3) ,

<!-- b000994 | prose | pages [17] -->
Wa

<!-- b000995 | prose | pages [17] -->
,

<!-- b000996 | prose | pages [17] -->
Wa

<!-- b000997 | prose | pages [17] -->
,

<!-- b000998 | prose | pages [17] -->
ij ij ij ij

<!-- b000999 | prose | pages [17] -->
(28)

<!-- b001000 | prose | pages [17] -->
 

<!-- b001001 | prose | pages [17] -->
j j

<!-- b001002 | prose | pages [17] -->
1,2, ,25.

<!-- b001003 | prose | pages [17] -->
means the war, conflict and cold violence among the refugee-exporting countries i and

<!-- b001004 | prose | pages [17] -->
 0 Wa

<!-- b001005 | prose | pages [17] -->
( ) v

<!-- b001006 | prose | pages [17] -->
Wa

<!-- b001007 | prose | pages [17] -->
the refugees receiving countries j, the preset value of is 0. And for

<!-- b001008 | prose | pages [17] -->
, if a lot

<!-- b001009 | prose | pages [17] -->
ij

<!-- b001010 | prose | pages [17] -->
ij

<!-- b001011 | prose | pages [17] -->
, otherwise

<!-- b001012 | prose | pages [17] -->


<!-- b001013 | prose | pages [17] -->
( ) v

<!-- b001014 | prose | pages [17] -->
( ) v

<!-- b001015 | prose | pages [17] -->
Wa

<!-- b001016 | prose | pages [17] -->
1

<!-- b001017 | prose | pages [17] -->
Wa

<!-- b001018 | prose | pages [17] -->
0

<!-- b001019 | prose | pages [17] -->
impact exists in this factor between i and j, then

<!-- b001020 | prose | pages [17] -->
    (1) (2)

<!-- b001021 | prose | pages [17] -->
( ) v

<!-- b001022 | prose | pages [17] -->
Wa Wa , Wa Wa

<!-- b001023 | prose | pages [17] -->
1

<!-- b001024 | prose | pages [17] -->
some

<!-- b001025 | prose | pages [17] -->
, then, ij ij ij

<!-- b001026 | prose | pages [17] -->
     (1) (2) (3) Wa Wa , Wa , Wa , 0 ij ij ij ij

<!-- b001027 | furniture | pages [17] -->


<!-- b001028 | prose | pages [17] -->
. If there is

<!-- b001029 | prose | pages [17] -->
ij

<!-- b001030 | prose | pages [17] -->
ij

<!-- b001031 | prose | pages [17] -->
 

<!-- b001032 | prose | pages [17] -->


<!-- b001033 | prose | pages [17] -->
(3)

<!-- b001034 | prose | pages [17] -->
( ) v

<!-- b001035 | prose | pages [17] -->
, , Wa , 1

<!-- b001036 | prose | pages [17] -->
Wa

<!-- b001037 | prose | pages [17] -->
0

<!-- b001038 | prose | pages [17] -->
, and if all

<!-- b001039 | prose | pages [17] -->
, then, ij

<!-- b001040 | prose | pages [17] -->
ij ij ij

<!-- b001041 | prose | pages [17] -->
.

<!-- b001042 | furniture | pages [18] -->
Team#46634

<!-- b001043 | furniture | pages [18] -->
page 17 of 22

<!-- b001044 | furniture | pages [18] -->


<!-- b001045 | furniture | pages [18] -->


<!-- b001046 | prose | pages [18] -->
We using the transfer matrix in task 4, like the foll

<!-- b001047 | prose | pages [18] -->
 

<!-- b001048 | prose | pages [18] -->


<!-- b001049 | prose | pages [18] -->
'

<!-- b001050 | prose | pages [18] -->
f Hp

<!-- b001051 | prose | pages [18] -->
,

<!-- b001052 | prose | pages [18] -->
Wa

<!-- b001053 | prose | pages [18] -->
11 11

<!-- b001054 | prose | pages [18] -->


<!-- b001055 | prose | pages [18] -->
 

<!-- b001056 | prose | pages [18] -->


<!-- b001057 | prose | pages [18] -->
'

<!-- b001058 | prose | pages [18] -->
f Hp

<!-- b001059 | prose | pages [18] -->
,

<!-- b001060 | prose | pages [18] -->
Wa

<!-- b001061 | prose | pages [18] -->
   

<!-- b001062 | prose | pages [18] -->
''

<!-- b001063 | prose | pages [18] -->
 

<!-- b001064 | prose | pages [18] -->
''

<!-- b001065 | prose | pages [18] -->
 

<!-- b001066 | prose | pages [18] -->
21 21 '

<!-- b001067 | prose | pages [18] -->
Hp f Hp Wa

<!-- b001068 | prose | pages [18] -->
,

<!-- b001069 | prose | pages [18] -->
ij ij

<!-- b001070 | prose | pages [18] -->
 

<!-- b001071 | prose | pages [18] -->
ij

<!-- b001072 | prose | pages [18] -->


<!-- b001073 | prose | pages [18] -->
 

<!-- b001074 | prose | pages [18] -->
'

<!-- b001075 | prose | pages [18] -->
f Hp

<!-- b001076 | prose | pages [18] -->
,

<!-- b001077 | prose | pages [18] -->
Wa

<!-- b001078 | prose | pages [18] -->
 

<!-- b001079 | prose | pages [18] -->
v

<!-- b001080 | prose | pages [18] -->
1

<!-- b001081 | prose | pages [18] -->
v

<!-- b001082 | prose | pages [18] -->
1

<!-- b001083 | prose | pages [18] -->
,   Wa  ' 0 f Hp , Wa Among them, if ij ij ij

<!-- b001084 | furniture | pages [18] -->


<!-- b001085 | prose | pages [18] -->
   

<!-- b001086 | prose | pages [18] -->
 

<!-- b001087 | prose | pages [18] -->
' '

<!-- b001088 | prose | pages [18] -->
f Hp

<!-- b001089 | prose | pages [18] -->
,

<!-- b001090 | prose | pages [18] -->
Wa f Hp

<!-- b001091 | prose | pages [18] -->
,

<!-- b001092 | prose | pages [18] -->
Wa

<!-- b001093 | prose | pages [18] -->
12 12 13 13

<!-- b001094 | prose | pages [18] -->


<!-- b001095 | prose | pages [18] -->
   

<!-- b001096 | prose | pages [18] -->
 

<!-- b001097 | prose | pages [18] -->
' '

<!-- b001098 | prose | pages [18] -->
f Hp

<!-- b001099 | prose | pages [18] -->
,

<!-- b001100 | prose | pages [18] -->
Wa f Hp

<!-- b001101 | prose | pages [18] -->
,

<!-- b001102 | prose | pages [18] -->
Wa

<!-- b001103 | prose | pages [18] -->
22 22 2

<!-- b001104 | prose | pages [18] -->
v

<!-- b001105 | prose | pages [18] -->
2

<!-- b001106 | prose | pages [18] -->
v

<!-- b001107 | prose | pages [18] -->


<!-- b001108 | prose | pages [18] -->
(29)

<!-- b001109 | prose | pages [18] -->
    

<!-- b001110 | prose | pages [18] -->
   

<!-- b001111 | prose | pages [18] -->


<!-- b001112 | prose | pages [18] -->
' '

<!-- b001113 | prose | pages [18] -->
f Hp

<!-- b001114 | prose | pages [18] -->
,

<!-- b001115 | prose | pages [18] -->
Wa f Hp

<!-- b001116 | prose | pages [18] -->
,

<!-- b001117 | prose | pages [18] -->
Wa

<!-- b001118 | prose | pages [18] -->
 

<!-- b001119 | prose | pages [18] -->
v

<!-- b001120 | prose | pages [18] -->
2

<!-- b001121 | prose | pages [18] -->
v

<!-- b001122 | prose | pages [18] -->
3

<!-- b001123 | prose | pages [18] -->
vv vv

<!-- b001124 | prose | pages [18] -->
Wa ,   ' ,    ' 1 Hp f Hp Wa 0 , if . ij ij ij ij

<!-- b001125 | prose | pages [18] -->
We define that the number of refugees in receiving country j who come from exporting     PK i , 1,2, ,10;

<!-- b001126 | prose | pages [18] -->
j 1,2, 25. country i is . ij

<!-- b001127 | prose | pages [18] -->
So, the amount of refugees which would be resettlement is

<!-- b001128 | prose | pages [18] -->
10 25

<!-- b001129 | prose | pages [18] -->


<!-- b001130 | furniture | pages [18] -->


<!-- b001131 | prose | pages [18] -->
Wa  

<!-- b001132 | prose | pages [18] -->
i 1 j 1

<!-- b001133 | prose | pages [18] -->
 .                                                      (30)

<!-- b001134 | prose | pages [18] -->
PK

<!-- b001135 | prose | pages [18] -->
ij ij

<!-- b001136 | prose | pages [18] -->
   Pd 1,2, 10;

<!-- b001137 | prose | pages [18] -->
j 1,2, 25. The pressure between the two exporting countries is:

<!-- b001138 | prose | pages [18] -->
Then we can lead to conclusion:

<!-- b001139 | prose | pages [18] -->


<!-- b001140 | prose | pages [18] -->
  

<!-- b001141 | prose | pages [18] -->
Pd Wa

<!-- b001142 | prose | pages [18] -->


<!-- b001143 | prose | pages [18] -->
ij ij

<!-- b001144 | furniture | pages [18] -->


<!-- b001145 | prose | pages [18] -->
  

<!-- b001146 | prose | pages [18] -->
i

<!-- b001147 | prose | pages [18] -->
1,2, ,10;

<!-- b001148 | furniture | pages [18] -->


<!-- b001149 | prose | pages [18] -->
 v

<!-- b001150 | prose | pages [18] -->
pd

<!-- b001151 | furniture | pages [18] -->


<!-- b001152 | prose | pages [18] -->
ij

<!-- b001153 | prose | pages [18] -->
   1 2

<!-- b001154 | prose | pages [18] -->


<!-- b001155 | prose | pages [18] -->
pd pd

<!-- b001156 | prose | pages [18] -->
,

<!-- b001157 | prose | pages [18] -->
pd

<!-- b001158 | prose | pages [18] -->
,

<!-- b001159 | prose | pages [18] -->
ij ij

<!-- b001160 | prose | pages [18] -->
(31)

<!-- b001161 | prose | pages [18] -->
 

<!-- b001162 | prose | pages [18] -->
j j

<!-- b001163 | prose | pages [18] -->
1,2, ,25.

<!-- b001164 | prose | pages [18] -->
means the connections of economic and diplomacy.

<!-- b001165 | prose | pages [18] -->
among this

<!-- b001166 | prose | pages [18] -->
ij

<!-- b001167 | prose | pages [18] -->
With the help of MATLAB, we get the two figures below.

<!-- b001168 | prose | pages [18] -->
15

<!-- b001169 | prose | pages [18] -->
12

<!-- b001170 | prose | pages [18] -->
10

<!-- b001171 | prose | pages [18] -->
10

<!-- b001172 | prose | pages [18] -->
8

<!-- b001173 | prose | pages [18] -->
Influence

<!-- b001174 | prose | pages [18] -->
Influence

<!-- b001175 | prose | pages [18] -->
6

<!-- b001176 | prose | pages [18] -->
5

<!-- b001177 | prose | pages [18] -->
4

<!-- b001178 | prose | pages [18] -->
2

<!-- b001179 | prose | pages [18] -->
0

<!-- b001180 | prose | pages [18] -->
0

<!-- b001181 | prose | pages [18] -->
10

<!-- b001182 | prose | pages [18] -->
10

<!-- b001183 | prose | pages [18] -->
10 8

<!-- b001184 | prose | pages [18] -->
5

<!-- b001185 | prose | pages [18] -->
6 4 2

<!-- b001186 | prose | pages [18] -->
0

<!-- b001187 | prose | pages [18] -->
0

<!-- b001188 | prose | pages [18] -->
Policy Space

<!-- b001189 | prose | pages [18] -->
10 8

<!-- b001190 | prose | pages [18] -->
5

<!-- b001191 | prose | pages [18] -->
6 4 2

<!-- b001192 | prose | pages [18] -->
0

<!-- b001193 | prose | pages [18] -->
0

<!-- b001194 | prose | pages [18] -->
Policy

<!-- b001195 | furniture | pages [18] -->


<!-- b001196 | prose | pages [18] -->
Country Resource

<!-- b001197 | caption | pages [18] -->
Figure 9 Different paremeter 5                       Figure 10 Different paremeter 6

<!-- b001198 | prose | pages [18] -->
The comparison of the two figures indicates that our model fit the occurrence of exogenous events by the large, and if we adjust some parameters in our model, it will solve the problem more perfectly.

<!-- b001199 | prose | pages [18] -->
Task 6: Scalability

<!-- b001200 | furniture | pages [19] -->
Team#46634

<!-- b001201 | furniture | pages [19] -->
page 18 of 22

<!-- b001202 | furniture | pages [19] -->


<!-- b001203 | furniture | pages [19] -->


<!-- b001204 | prose | pages [19] -->
In our initial model, we have considered the factor of the size of refugee, so if the size of refugees is enlarged, our model can be satisfied overall. But if this happens, the size of refugees will become the major subject of consideration. Therefore, each refugee-receiving country’s saturability of receiving refugee will be correspondingly increase to an extreme value. And for refugees-exporting country, its economic strength will not change much in a short time, so the corresponding inputs for each refugee will inevitably reduce .

<!-- b001205 | prose | pages [19] -->
In order to improve our model’s ability to deal with this situation of large-scale refugee, we need to increase the corresponding control element on the basis of the original. And most important of which is the model of transportation for the refugee to transfer, and the basic

<!-- b001206 | prose | pages [19] -->
living security for refugee in the destination of transfer, besides the relationships with local residents. Because on the basis of existing public infrastructure, in order to meet the requirements of the transfer of refugees on a larger scale, we must consider transportation infrastructure.

<!-- b001207 | prose | pages [19] -->
   We define that Tr i , 1,2, ,10, j 1,2, ij   ,which denote the amount of traffic form 25.

<!-- b001208 | prose | pages [19] -->
the refugee-exporting country(i) to the refugee-receiving country(j),that is how many refugees that it can meet transferring from the refugee-exporting country(i) to the refugee-  receiving country(j).Also defining Ls i , 1,2, ij    which denote the basic ,10, j 1,2, 25.

<!-- b001209 | prose | pages [19] -->
livelihood of refugees than refugee-receiving country(j) can provide to the refugee-exporting country(i),that is how many refugees that the refugee-receiving country(j) can meet the basic livelihood for the refugee-export country. Define the conflict factor of the refugees with the     Cf i , 1,2, ,10, j 1,2, 25. local residents ij   among them 0 Cf 1 .The greater the ij

<!-- b001210 | prose | pages [19] -->
conflict factor the refugees with the local residents, the greater probability of conflict between the refugees and the local residents. And then the greater probability of conflict between the refugees and the local residents, the difficult that the refugee-receiving country(j) receive the refugees from the refugee-exploring country(i). So here planning the transfer route of the refugee rationally and making full use of the existing transport resources are becoming particularly important. In this case the competition for transfer of refugee is bound to produce, even conflict will be happened[11].

<!-- b001211 | prose | pages [19] -->
Finally, we define the existing number of refugees of refugee-exporting country(i) as Pn i   i i   ,the existing transportation resources available as Re , , 1,2, ,10 i 1,2, ,10 ,the

<!-- b001212 | prose | pages [19] -->
Cp i  probability of conflict between refugees as

<!-- b001213 | prose | pages [19] -->
 

<!-- b001214 | prose | pages [19] -->
Cp i

<!-- b001215 | prose | pages [19] -->
 

<!-- b001216 | prose | pages [19] -->
i

<!-- b001217 | prose | pages [19] -->
1,2,

<!-- b001218 | furniture | pages [19] -->


<!-- b001219 | prose | pages [19] -->


<!-- b001220 | prose | pages [19] -->
 , , 1,2, ,10 .In this case: i i

<!-- b001221 | prose | pages [19] -->
  

<!-- b001222 | prose | pages [19] -->
  

<!-- b001223 | prose | pages [19] -->
Pn

<!-- b001224 | prose | pages [19] -->
Re

<!-- b001225 | prose | pages [19] -->
i i i

<!-- b001226 | prose | pages [19] -->


<!-- b001227 | prose | pages [19] -->
(32)

<!-- b001228 | prose | pages [19] -->
,10.

<!-- b001229 | prose | pages [19] -->
i denote the the original quality of the citizens and nationals relations of Among them, refugee-exportING country(i).

<!-- b001230 | prose | pages [19] -->
Considering the threshold of time, we believe that to ensure the refugees to transfer before the collapse of the body or psychological breakdown is a threshold of time in this case. Of course, in order to control this threshold of time, we need to keep refugees psychological counseling and education, and arrange adequate medical resources to protect the basic

<!-- b001231 | furniture | pages [20] -->
Team#46634

<!-- b001232 | furniture | pages [20] -->
page 19 of 22

<!-- b001233 | furniture | pages [20] -->


<!-- b001234 | furniture | pages [20] -->


<!-- b001235 | prose | pages [20] -->
medical needs of the refugees, and to strengthen their pease with the local population and refugees in distress with local ideas.

<!-- b001236 | prose | pages [20] -->
After analyzing the scalability of our model, we get the results that the stabilization change with the expansion of  the scale.

<!-- b001237 | prose | pages [20] -->
80

<!-- b001238 | prose | pages [20] -->
70

<!-- b001239 | prose | pages [20] -->
frequency distribution of degree value

<!-- b001240 | prose | pages [20] -->
60

<!-- b001241 | prose | pages [20] -->
50

<!-- b001242 | prose | pages [20] -->
40

<!-- b001243 | prose | pages [20] -->
30

<!-- b001244 | prose | pages [20] -->
20

<!-- b001245 | prose | pages [20] -->
10

<!-- b001246 | prose | pages [20] -->
0 0 5 10 15 20 25 30 35 40 45 50

<!-- b001247 | prose | pages [20] -->
degree value of node

<!-- b001248 | furniture | pages [20] -->


<!-- b001249 | caption | pages [20] -->
Figure 11 change of stabilization

<!-- b001250 | furniture | pages [20] -->


<!-- b001251 | prose | pages [20] -->
It’s clear that our model is in point when the scale is less than then times, but when the scale is to 15 times, the stabilization is reduced to some extent.

<!-- b001252 | furniture | pages [20] -->


<!-- b001253 | furniture | pages [20] -->


<!-- b001254 | furniture | pages [21] -->
Team#46634

<!-- b001255 | furniture | pages [21] -->
page 20 of 22

<!-- b001256 | furniture | pages [21] -->


<!-- b001257 | heading | pages [21] -->
Stability and Sensitivity

<!-- b001258 | prose | pages [21] -->
Judging from the overall effect of our model, it is not only fit for the environment and area mentioned in the paper but also suited to most fields related to refugees, that is, our model has relatively wide range of applicability. After building refugees transfer model and the relationship of refugee-receiving country and refugee-exporting country referring the data of the two fields, we use them to study the quantities of the relationships and the influence of the evaluation objects, and the results turn out to be reasonable. So our model is practical and reliable.

<!-- b001259 | prose | pages [21] -->
Moreover, our model doesn’t depend on some certain data. As what is shown in Task 4, when the original data changes, the result of our model changes to a new one corresponding to reality. Regardless of we add some data into the model or remove some out, the results of the model will not have large fluctuations, which indicates the good stability and weak sensitivity of our model.

<!-- b001260 | prose | pages [21] -->
According to the assumption, we do not take time of preparation for the transfer into account. However, the time of preparation for the transfer has effect on both of the refugee- receiving countries and the refugee-exporting countries. In order to test the sensitivity of our model, we decided to take time of preparation for the transfer as a criterion and add it into our model. Let it to be the time of preparation for the transfer of refugee-exporting country.

<!-- b001261 | prose | pages [21] -->
it as a new criterion, we change other criterion’s weight and calculate the weighted Taking

<!-- b001262 | prose | pages [21] -->
incidence degree of each author again. From our point of view on the new result, although every refugee-exporting country weighted incidence degree changes a little after adding the time of preparation for the transfer, the change of their relative influence is rather small, indicating that our model has good sensitivity.

<!-- b001263 | heading | pages [21] -->
Strengths

<!-- b001264 | prose | pages [21] -->
After building the refugees transfer model, we calculate the influence of each of the evaluation object. Further, in order to ensure the stability of the model, we circulate the calculation process and weigh every evaluation object according to the weighted incidence degree determined. Then we use our model to evaluate all the evaluation objects again, thus giving the effective strategy of transfer.

<!-- b001265 | prose | pages [21] -->
When analyzing of the transfer of the refugees, we promote the model to different fields rather than keep it in one area so that the model is endowed with higher reliability and wider range of applications. Besides, after establishing the refugees transfer model, we solve the problems from different perspectives, thus giving a full description of our model from other points of view.

<!-- b001266 | heading | pages [21] -->
Weaknesses

<!-- b001267 | prose | pages [21] -->
In terms of statistics of data, sometimes it is not accurate enough in our model due to the limitations of resources and lack of statistical techniques, so there may be errors in the result.

<!-- b001268 | prose | pages [21] -->
Since there are many evaluation objects in our refugees transfer model, the transfer diagram would be rather disordered and difficult to study if all the evaluation objects are

<!-- b001269 | furniture | pages [22] -->
Team#46634

<!-- b001270 | furniture | pages [22] -->
page 21 of 22

<!-- b001271 | furniture | pages [22] -->


<!-- b001272 | prose | pages [22] -->
included in the refugees transfer model diagram. So we give schematic diagrams and uncompleted diagrams when analyzing as auxiliary description.

<!-- b001273 | prose | pages [22] -->
When discussing the scalability of the refugees transfer model, we find the number of the refugees is big while the cooperation between them is relatively little. As a consequence, the results of many evaluation objects are close under the evaluation index set in our model, lowering the persuasion of the results of our model.

<!-- b001274 | heading | pages [22] -->
References

<!-- b001275 | references | pages [22] -->
[1] Lubomyr,Y. Luciuk, Unintended Consequences in Refugee Resettlement: Post-War

<!-- b001276 | references | pages [22] -->
Ukrainian Refugee Immigration to Canada, The International Migration Review,1986,20(2):

<!-- b001277 | references | pages [22] -->
467–482.

<!-- b001278 | references | pages [22] -->
[2] Geddes, A., Immigration and European integration: towards fortress Europe? , Refugee

<!-- b001279 | references | pages [22] -->
Survey Quarterly, 2001, 20(1): 229–229.

<!-- b001280 | references | pages [22] -->
[3] Gallya Lahav, Immigration and Politics in the New Europe, Reinventing Borders, 2004.

<!-- b001281 | references | pages [22] -->
[4] James Hollifield，Philip Martin，Pia Orrenius, Controlling Immigration: A Global

<!-- b001282 | references | pages [22] -->
Perspective (Third Edition),2014.

<!-- b001283 | references | pages [22] -->
[5] Liisa H. Malkki, Refugees and Exile: From "Refugee Studies" to the National Order of

<!-- b001284 | references | pages [22] -->
Things, Annual Review of Anthropology, 1995, 24: 495-523.

<!-- b001285 | references | pages [22] -->
[6] Eric Neumayer, Bogus Refugees? The Determinants of Asylum Migration to Western

<!-- b001286 | references | pages [22] -->
Europe , International Studies Quarterly, 2005, 49(3):389-410.

<!-- b001287 | references | pages [22] -->
[7] Roger Zetter, More Labels, Fewer Refugees: Remaking the Refugee Label in an Era of

<!-- b001288 | references | pages [22] -->
Globalization, Journal of Refugee Studies, 2007, 20(2):172-192.

<!-- b001289 | references | pages [22] -->
[8] Eleonore Kofman, Gender and International Migration in Europe: Employment, Welfare,

<!-- b001290 | references | pages [22] -->
and Politics, 2000

<!-- b001291 | references | pages [22] -->
[9] Alessandra Buonfinoa , Between unity and plurality: the politicization and securitization

<!-- b001292 | references | pages [22] -->
of the discourse of immigration in Europe, New Political Science, 2004, 26(1):23-49.

<!-- b001293 | references | pages [22] -->
[10] Anthony H. Richmond, Reactive Migration: Sociological Perspectives On Refugee

<!-- b001294 | references | pages [22] -->
Movements, Journal of Refugee Studies,1993,6(1):7-24.

<!-- b001295 | references | pages [22] -->
[11] Elizabeth Fussell, James R. Elliott, Introduction: Social Organization of Demographic

<!-- b001296 | references | pages [22] -->
Responses to Disaster: Studying Population—Environment Interactions in the Case of

<!-- b001297 | references | pages [22] -->
Hurricane Katrina, Organization & Environment,2014,22(4):379-394.

<!-- b001298 | furniture | pages [22] -->


<!-- b001299 | furniture | pages [22] -->


<!-- b001300 | furniture | pages [22] -->


<!-- b001301 | furniture | pages [22] -->


<!-- b001302 | furniture | pages [22] -->


<!-- b001303 | furniture | pages [22] -->


<!-- b001304 | furniture | pages [23] -->
Team#46634

<!-- b001305 | furniture | pages [23] -->
page 22 of 22

<!-- b001306 | furniture | pages [23] -->


<!-- b001307 | references | pages [23] -->
Dear Sir or Madam,

<!-- b001308 | references | pages [23] -->
It is my pleasure to give policy recommendation to UN. As the factors that we have

<!-- b001309 | references | pages [23] -->
discussed, we find the refugees’ diathesis, country’s policy and external factors influence the

<!-- b001310 | references | pages [23] -->
movement of the refugees. Since the UN requires us to give priority to the health and safety

<!-- b001311 | references | pages [23] -->
of the refugees and the local people, we synthesize our result above and give our advice on

<!-- b001312 | references | pages [23] -->
policy about refugees.

<!-- b001313 | references | pages [23] -->
Firstly, we suggest that give priority to the cultural restraint and religion, so we could

<!-- b001314 | references | pages [23] -->
have a policy that the receiving country should accept prior the refugees who have similar

<!-- b001315 | references | pages [23] -->
cultures and religious beliefs.

<!-- b001316 | references | pages [23] -->
Secondly, we advise UN to establish a ‘safe zone’ as a buffer if there is a war between the

<!-- b001317 | references | pages [23] -->
refugee-exporting country and the refugee-receiving country. The ‘safe zone’ should be built

<!-- b001318 | references | pages [23] -->
at the boundary between the receiving country and its neighboring country (except the

<!-- b001319 | references | pages [23] -->
refugee country). During that time, UN should provide necessaries to the refugees.

<!-- b001320 | references | pages [23] -->
Finally, doctors and psychologists should be dispatched by UN. For the refugees suffer

<!-- b001321 | references | pages [23] -->
much pressure both on their mental and physical and this kind of pressure can not be stay

<!-- b001322 | references | pages [23] -->
long time.

<!-- b001323 | references | pages [23] -->
The policy recommendations above combine our results, we hope it sincerely that the

<!-- b001324 | references | pages [23] -->
advice can help refugees to come through the tough days!

<!-- b001325 | furniture | pages [23] -->


<!-- b001326 | furniture | pages [23] -->


<!-- b001327 | references | pages [23] -->
Yours sincerely

<!-- b001328 | furniture | pages [23] -->

