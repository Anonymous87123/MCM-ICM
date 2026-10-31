Summary

“Ebola is a major global crisis that demands a massive and immediate global response. No country or organization can defeat Ebola alone.”

—— H.E. Ban Ki-moon, the UN Secretary-General.

As a number of Global Village, we do our best to help eradicate Ebola.

First, we develop a stage-structured model of Ebola Propagation. In the model, we consider the susceptible, the exposed, the infected whose disease is not advanced, the infected whose disease is serious, the removed and the dead. The model is good at predicting near future cases’ number but fails in predicting far future cases’ number. Then we take hospital into consideration and add 7 more parameters, then we do simulation once again. Finally, we get a better result that the model well predicts the future cases. For example, the model predicts there are 4000 total cases and 2500 death cases in Guinea, 9509 total cases and 4166 death cases in Liberia, 12556 total cases and 3933 death cases in Sierra Leone up to April,1st, 2015.

Second, we determine the locations of delivery. We invoke clustering method to divide the most serious region, namely, West Africa into three parts, Guinea, Liberia and Sierra Leone. According to locations of provincial capital, we use clustering method once again to divide a country into several clusters. Then we adopt P-Center Method to determine a location of delivery in each cluster. We find there are two kinds of ways to choose. One is one-way route and the other is circular route. As for one-way route, we think it is time-consuming and energy-consuming. So we decide to use circular route. The circular route, in some ways, is a little bit similar to TSP problem, we use mix integer programming to find an optimal circular route by Lingo Software and each location of delivery has two optimal circular routes. The result is that there are 3 locations of delivery in Guinea, 1 location of delivery in Liberia and 1 location of delivery in Sierra Leone.

Third, we know from the stage-structured model that Ebola cannot stop spreading by itself. Since we are going to eradicate Ebola, we must use medicine and vaccine to stop Ebola. Medicine mainly influences the number of the susceptible while vaccine mainly influences the number of the infected whose disease is not advanced, in this way, we can eradicate Ebola. As for speed of manufacturing, we consider there is a linear equation between the speed and time because the amount of medicine is too rare to meet the requirement of patients. And this situation continues until the requirement is met. We can calculate the speed by the parameter in the linear equation. And we allocate medicine to different places by ratio of the infected number in that place to the number in three West African countries. Thus, we successfully stop Ebola from spreading.

Ⅰ Introduction

Ebola, a familiar but strange word to us. When the Ebola virus out broke in West Africa and caused plenty of deaths, no one would imagine the disastrous scene without mercy. And, of course, no one believes the word ‘Ebola’ just originated from a peaceful and beautiful river – Ebola River in Congo. Contrary to its attracting meaning, it is true that the Ebola virus do take lots of victims’ lives away. Countries all over the world, thus, have taken strategies, more specifically, distribute health works to disease-torn countries, speed up the development of medicine and establish feasible delivery systems to contain Ebola propagation.

1.1 Aims are changing now

The battle against Ebola will cost us heavily for sure, but human beings are not easily defeated. Although Ebola virus is fatal, we have methods. The WMA (World Medical Association) has announced that they have developed medicine to cure Ebola. At one level, the medicine is a milestone for us human beings in fighting Ebola, but at another it is the result of human nature. We know calling the command center to take away the sick is equally hard. It is our duty, in the interests of our own and the public good, to pick up the phone, but the reality is that, if we do, we may never hug our sister again. We can visit her in the treatment center and talk across two fences. The fortunate will be reunited. For the rest, the future is the body bag.[1] Ebola will not end without the medicine. Thanks to appearance of the medicine, we are gradually going out of confusion and turning to fight back in this smokeless battle. Many previous articles that mainly focus on how Ebola propagation or how difficult to contain Ebola are now may less important than those on how to effectively delivery medicine to most-need regions like West Africa. Accurate location with effective medicine – Ebola’s doomsday and we do our job to make it come true – considering propagation process, medicine needed, delivery systems, locations of delivery and manufacturing speed of vaccine or drug and so on.

1.2 Our understanding of the words

The problem requires us to de several jobs to evaluate Ebola. We think it is necessary for us to come to an understanding of some words in the problem.

Spread of the Disease: We consider this sub-problem as a requirement to analyze Ebola propagation process and predict future cases, including total cases and death cases in the three West African countries and what influence that new medicine will bring to us. As for Ebola cases in other countries, such as in the United States or in The United Kingdom, good health condition and developed facilities can contain the cases well, so in this paper, we mainly discuss Ebola cases in West Africa.

Locations of Delivery: How to understand the word ‘locations’ is the key to this sub-problem. We also have some criteria to choose ‘locations’ – easy to deliver medicine, cover most people or environment-friendly to build? Here, we regard ‘locations’ as places that have features of easy and time-saving in medicine delivering, being equal to all people in a region.

Possible Feasible Delivery Systems: We think this sub-problem needs us to design a route that can not only cover all places which are in need of medicine but also provide vehicles a fastest way to send medicine. Besides, delivery systems can allocate medicine to different places properly.

The Quantity of the Medicine Needed: There are several understandings of the word ‘quantity’, like amount of medicine to cure all Ebola patients or amount of medicine needed every day to keep serious patients from dying. Our understanding of this word is the total amount of medicine needed to cure patients whose disease is not advanced until there is no more patients appear. So it is a dynamic and time-varying number until cases stops increasing.

Speed of manufacturing of the vaccine or medicine: In our opinion, this sub-problem needs us to decide how fast a factory have to produce medicine when amount of medicine is too rare to cure patients and what changes a factory should obey when there is enough medicine for patients. As for vaccine, we consider it is similar to medicine.

Other factors: Something we forget to consider in our model but also important for Ebola evaluating. We will find them during the process of establishing models

1.3 Decompose the Problem and Our Tasks

To totally understand the problem better and know what we should to deal with Ebola, decompose it is needed to us. According to the steps needed in process of achieving our goal that accurate location with effective medicine, we deem the problem ‘Eradicating Ebola’ can be divided into five parts:

Propagation mechanism of Ebola virus.

Accurate locations for medicine to be delivered like disease-torn countries in West Africa.

Effective transportation including amount of medicine needed in a place.

Total amount of medicine needed to cure Ebola patients until cases stops increasing.

Vaccine or drug manufacturing speed

When the problem is unequivocal, we start to make it clear that what we need to do and how to do it. Since we have separated the problem into parts, we can deal with these parts one by one. Here the problem requires us do and our tasks are:

 Build a model to reflect the condition we face now and make prediction of the future if medicine or hospital or other factors play roles in Ebola propagation process.

 Find some best delivery places according to our own understanding of word ‘locations’

 Design a delivery system both good in medicine transportation and medicine allocation.

 Speed to produce medicine and total quantity needed to eradicate Ebola

 Other critical factors we consider important to optimize the eradication of Ebola

Ⅱ Background – Behavior Change is Key to the

Eradication of Ebola

As the number of Ebola cases and deaths grows in West Africa, many remain unaware of its deadly impact, causes and treatment options, or lack thereof. Let people know the harm of the diseases is of great importance both in the developing world and, more specifically, on the African continent.

Unfortunately, in remote districts of these three African countries – Guinea, Liberia and Sierra Leone few of the local have heard Google or ABC News or other TV media and say nothing of getting access of the newest Ebola news. Once the people who are seeing their family members get sick and die tend to believe an invisible killer who are from hell. Getting correct information about Ebola prevention and treatment to local communities throughout West Africa must become a higher priority, and we must begin to address it in culturally appropriate and innovative ways.[2]

Besides, human nature is another factor of Ebola spreading unimpededly, though great efforts have been made to find and quarantine Ebola patients. Like we introduced in Instruction, although talk of changing behavior is easy, when we think about the sort of behavior that needs to change, we realize it’s very hard. How many of us could bear to watch our mother die without holding her hand, and then allow her body to be sprayed with chlorine, removed in a double body bag from the house, be loaded on to the back of a pick-up truck with several others, and taken to the cemetery for rapid interment with little more than a cursory prayer?[1]

We must have to realize that change awareness and human nature is quite hard. The most effective way is to find medicine if we want to win the battle against Ebola. Here is the time for medicine cure – the WMA have announced that they could.

Ⅲ Assumptions And Justifications

①Overlook the changing of population caused by natural birth rate and death

rate.

Compared to the influence of Ebola to the population, natural birth rate and death rate

have little impact. Also, the total natural growth of number of population is not large

in the period of the spread.

②There is no population flow among areas.

Since the outbreak of Ebola, the immigration among different districts and countries

play a role can be ignored in terms of the change of the population. In addition, the

flow rate of people may decrease in case of the infection of disease.

We list more and detailed assumptions in the following section when using them.

Ⅳ SEIIRF model for Ebola propagation

4.1 Introduction

The ongoing Ebola outbreak surprises us both in size and complexity. At the very beginning of 2015, many scientists and other people, like us students, are still fighting against Ebola in different ways, such as developing medicine, propagating health care and predicting the spread of Ebola. In this section, we apply SEIIRF Model to evaluate the spread of Ebola. Thanks to a previous article [5], we can use this model appropriately, however, as time goes by, values of parameters stated in that article may not convinced enough anymore for that article just used data from October,2014 to November, 2014 to calculate values of parameters and then tested the model with data in December, 2014. If we still use the values of parameters in that article, we find it is far from accuracy of data in January, 2015. So we find a method – Genetic Algorithm to refresh the value of parameters by using data from October, 2014 to December, 2014 and the renewed SEIIRF Model well fits the data of January 1st, 2015 to February 3rd, 2015.

4.2 Symbols and Definitions

There are some symbols appear in the model. We show them below:

SYMBOL

DEFINITION UNITS

Transmission Parameter For First Stage Of Illness (Not  -1 -1 people days 1 In Hospital)

 Ratio Of Infectiveness In First Vs. Second Of Stage Of 2 Unitless  Illness (Not In Hospital) 1

 Ratio Of Infectiveness In First F Unitless  Stage Vs. Funeral Transmission (Not In Hospital) 1

 1 Average Incubation Period Days

1 1 Length Of First Stage Of Illness (Not In Hospital) Days

 1 Length Of Second Stage Of Illness (Not In Hospital) Days 2

  1 Time From Death Until Burial Days F

 Overall Mortality Rate (Fraction) (Not In Hospital) Unitless 1 2

Mortality Rate (Fraction) Among Those In Second  Unitless 2 Stage Of Illness (Not In Hospital)

4.3 Construction of the Model

To adequately reflect the propagation of Ebola and transmission of Ebola, we should take real conditions in life into consideration.

To begin with, we show our model as a form of figure.

S E I1 I2 F

R

We can get information from the figure 4.1. There are six stages in the whole propagation of Ebola. We also call this model as Stage-Structured Model,

S represents the fraction of the population which is susceptible.

E represents the fraction of the population which is exposed.

1I represents the fraction of the population which is infected and remain in first

stage (such as fever, headache, sore throat, muscle aches and other milder symptoms which often progress to diarrhea and vomiting).

2I represents the fraction of the population which is infected and deteriorate to

second stage (such as hemorrhaging and multi-organ failure).

R represents the fraction of the population which is recovered. And

F represents the fraction of the population who have died and are in the process of being buried.

The corresponding equations of Figure 4.1 are

 dS       ( I I F S )  I 1 2 2 F dt  dE          ( I I F S ) E  I 1 2 2 F dt  dI      1 E I  1 1 dt dI      2 I I  1 1 1 2 2 dt  dF      I F 2 2 2 F  dt  dR        (1 ) I (1 ) I 1 1 1 2 2 2 dt

In the equations we consider the infected ( 1I and 2I ) and the dead ( F ) all have

ability to infect the susceptible. In fact, when our relatives get sick, we still contact with the in daily life, and it is not surprise for us to think that human nature play an important role in Ebola propagation – just as we have talked in introduction. How many of us could bear to watch our mother die without holding her hand, and then allow her body to be sprayed with chlorine, removed in a double body bag from the house, be loaded on to the back of a pick-up truck with several others, and taken to the cemetery for rapid interment with little more than a cursory prayer? Moreover, the

     exposed E are mainly form the susceptible ( I I F S ) and then have I 1 2 2 F

 chances to turn to first stage if they show symptoms ( E ). And number of people in

  first stage 1I are mainly from the exposed ( E ) and then part of them ( 1 1 1I ) turn

  to second stage and the rest of them (1 ) I get recovered. Thus number of 1 1 1

 people in second stage are mainly from first stage ( 1 1 1I ) and some of them die. So

  the dead is the result of people ( 2 2I ) in second stage and their bodies ( FF ) exist 2

until being buried.

Then, to measure the total cases and death cases of Ebola, We invoke

t    y E (t) dt C 0 t    y I (t) dt D 2 2 2 0 In these equations, y means total cases (or cumulate cases) and y means C D

 death cases. And means number of people begin to get sick and have E (t)

  symptoms so y is the time integral of . While 2 2(t) I is number of people E (t) C

 who no longer in second stage anymore, means number of dead people. So 2 2(t) I 2

 y is the time integral of 2 2(t) I . D 2

4.4 Results are Not So Reasonable

The article[5] adopts Least Square Method to figure out values of parameters. Unfortunately, under the values of parameters, although the calculated curve fits quite well to real data in Guinea from October 1st, 2014 to December 31st, 2014, we fail to fit the calculated curve well to real data in Guinea when time reaches on January 1st, 2015, namely, the values of parameters in that article may ‘outdated’. So we do not show them here because they are not worthy enough.

So, we adopt genetic algorithm combined with least square method to calculate our new values of parameters.

4.5 Refresh the Values of Parameters

Genetic algorithm combined with least square method is used by us to find out new parameters values. Here flow diagram of Genetic algorithm is START

 PARAMETER INITIALIZATION X X 0

 CALCULATE FITNESS f F (X)

GENETIC

N>Nf

OUTPUT OPTIMAL

END

        In the flow diagram, de define X , / , / , , , , , , and 1 2 1 F 1 1 2 F 1 2 2

       fitness . Where ct is length of f F (X) [ y ( ) t C t ( )] [ y ( ) t D t ( )] C 0 D 0   t t t t c c

time from October 1st, 2014 to December 31st, 2014. And C t denotes real total 0( )

ct while D t denotes real 0( ) cases in a country updated every day within time length

death cases in a country updated every day within time length ct .

By now, we have method to find each parameter’s value by using data from October, 2014 to December, 2014. Then we use these new values to calculate a curve to fit real data in Guinea.

Here the results are:

We can see from the figures 4.3 that in about first 90 days, namely, date from Oct.1st, 2014 to Dec.31st, 2014, the model fits well to the real data of Guinea from

WHO website. Both y and y reflect accurate number of cases, respectively. C D

However, as New Year begins, real data has tendency of becoming less rapidly increasing while our prediction is out of accuracy although our curve is much better than that calculated in the article we refer to. We do not use this curve to predict cases in Liberia and Sierra Leone.

4.6 Advanced Model

After refreshing the values of parameters, we are still not satisfied with the curve we calculate. Data talks, we should try our best to make our model considerable. To improve the model we discussed in former section, we not only use more data from WHO website to calculate our parameters, but also consider other factors impact on Ebola spreading, like additional parameters and changing of parameters’ values if people receive treatment or get infected in hospital. There is a pie chart showing the proportion of getting infected in different ways (data of Sierra Leone).

There are 17.6% of healthy people in Sierra Leone get Ebola because of hospital. it is a factor important enough for us to take it into consideration when we evaluate Ebola propagation.

First, let us get an accessible way to additional parameters and their meanings in this advanced model.

SYMBOL

DEFINITION UNITS

Transmission Parameter For First Stage Of Illness (In  -1 -1 people days 1 H Hospital)

Transmission Parameter For Second Stage Of Illness (In  -1 -1 people days 2 H Hospital)

Length Of First Stage Of Illness (From Moment Of 1h  1 Days Symptoms Appearing To Go To Hospital)

Length Of Second Stage Of Illness (From Moment Of 2h  1 Days Symptoms Appearing To Go To Hospital)

3y  1 Length Of First Stage Of Illness (In Hospital) Days

4y  1 Length Of Second Stage Of Illness (In Hospital) Days

 Overall Mortality Rate (Fraction) (In Hospital) Unitless 1 H 2 H

Mortality Rate (Fraction) Among Those In Second Stage Of  Unitless 2H Illness (In Hospital) The reason why we add these parameters is that if hospital plays a role in people’s daily life, people will have another access to cure Ebola. When people feel

1h , 2h , 1 1 uncomfortable, they may choose to go to hospital for doctors’ help. Thus,

3y  and 4y  are generated to denote different length of time in or not in hospital. 1 1

, ,   By the way, and are introduced to explain the model 1 H 2 H 1 H 2 H 2H

more considerably.

We show our advanced model as a form of figure

S E I1 I2

R F

H1 H2

The advanced equations of this model are  dS           [ ( I H ) ( I H ) F S ]  I 1 H 1 2 2 H 2 F dt  dE              [ ( I H ) ( I H ) F S ] E  I 1 H 1 2 2 H 2 F dt  dI       E I h I 1 1 1 1 1  dt  dI       2 I I h I 1 1 1 2 2 2 2 dt dH     1 h I H  1 1 3 1 dt  dH        2 h I H H 2 2 1 H 3 1 4 2  dt  dF         I H F 2 2 2 2 H 4 2 F dt   dR               (1 ) I (1 ) I (1 ) H (1 ) H  1 1 1 2 2 2 1 H 3 1 2 H 4 2 dt

Where H and H mean number of people in hospital who are in first stage and 1 2 in second stage, respectively. While 1I , 2I mean the number of people not in

hospital who are in first stage and in second stage, respectively. And S , E , F and R have the same meanings as we talked before.

In this group of equations, the susceptible are not only vulnerable to the sick

   outside ( or ), but also to the patients in hospital ( or I I S 2I S H H S 1 2 1 1

 H H S ). Different from what we explained in 3.4, the infected who are in first 2 2

stage have another way to go – hospital ( h I ). And the infected who are in second 1 1

stage do ( h I ), too. For the infected in hospital, they may die or recover. 2 2

4.7 Results are Reasonable

First, we should better to find additional parameters’ values. Similarly, we use genetic algorithm combined with least square method that we have introduced above to calculate values. But there is a little difference at this moment is that            X , / , / , , , , , , , , h h , , , , , . 1 2 1 F 1 1 2 F 1 2 2 H 1 2 3 4 1 H 2 H

We calculate all parameters in Guinea are:

PARAMETER VALUE PARAMETER VALUE

 1 0.04 0.26 1

   / 2.37 0.48 2 1 H

  / 1h 1.27 0.43 F 1

 2h 0.42 0.55

  0.19 0.20 1 2 3

  0.58 0.11 2 4

  0.46 0.49 F 1H

  0.70 0.81 2 2H And curves in Guinea are :

We can see from the figure 4.6, our curves fit much better if we take hospital into consideration and add more parameters than the article we refer to. The curves can fit real data from January 1st, 2015 to February 3rd, 2015 in Guinea both in total cases and death cases. So we trust these two curves.

4.8 Prediction of the Future

Since we have found curves to fit real data well, our next job is to use the curves to predict number of total cases and death cases in Guinea in the near future. We draw a figure based on the figures that we have showed above. We lengthen the time axis to predict future cases until end of April, 2015.

From the figure 4.7, the curves deliver us information about Guinea that number of total cases and death cases is still growing, and total cases grow a little bit faster than death cases grow. Number of total cases will reach to nearly 4000 after 180 days and death cases will reach to about 2500 after 180 days. However, number of cases is much less than a condition without hospital and medicine (see figure 4.7). After all, we just have medicine to cure Ebola patients whose disease is not advanced. As for serious patients, the only endeavor we can do is supportive treatment and pray.

Besides, we calculate parameters and curves of Liberia and Sierra Leone, we see curves also fit well to real data.

The parameters of Liberia:

PARAMETER VALUE PARAMETER VALUE

 1 0.19 0.28 1

   / 2.06 0.23 2 1 H

  / 1h 1.97 0.44 F 1

 2h 0.45 0.73

  0.18 0.12 1 2 3

  0.63 0.84 2 4

  0.46 0.31 F 1H

  0.92 0.79 2 2H

The curves of Liberia:

We can see from the figure 4.8 that curves also fit well to real data of Liberia.

The parameters Sierra Leone:

PARAMETER VALUE PARAMETER VALUE

 1 0.29 0.26 1

   / 2.43 0.11 2 1 H

  / 1h 2.25 0.48 F 1

 2h 0.46 0.79

  0.14 0.71 1 2 3

  0.54 0.84 2 4

  0.49 0.49 F 1H

  0.81 0.76 2 2H

The curves of Sierra Leone:

We can see from the figure that curves also fit well to real data of Sierra Leone.Because of limited time, we cannot do prediction job for Liberia and Sierra Leone. But we strongly believe if we have enough time, we can predict future data precisely by using these 16 parameters with consideration of hospital. Here we must say sorry to people who live in Liberia and Sierra Leone.

Ⅴ Model of Locations of Delivery

Locations of delivery, by definition, it is the place to give out medicine to somewhere is in emergency. Ebola outbreak in West Africa covers a terrified curtain to people live there. People who enveloped in the curtain, in some ways, really need effective medicine delivered to accurate region, otherwise, sadly, there are only body bags waiting for them. So determine delivery locations are quite necessary. Considering total cases and current condition at the moment when medicine is successfully manufactured in these three diseases-torn countries, we use several methods and criteria to judge where are the relatively good places both have minimal cost and best treatment.

5.1 What is Emergency Supplies

At first, it is needed for us to have a clear understand of what are emergency supplies, like the medicine to cure Ebola. Different from normal supplies, emergency supplies are used to control bombshells when an emergency happens or used for evacuation, rescue and repair after an emergency happened while normal supplies are just used in daily life. More specifically, differences between them are shown as the table below:

ASPECTS NORMAL SUPPLIES EMERGENCY SUPPLIES Maximize Profile And Consider Both Fair And Aims Minimize Cost Efficiency Supplies Collection Point, Factory, Distribution Center Formation Delivery Place And Supplies And Customer Demand Point

Property Permanent Temporary

Divide Into Long-Term, Urgency, Make Tread-Off Scheme Medium-Term And Decision At Once Short-Term Balance Between Efficiency Think A Lot Of Optimization Think A Lot Of Efficiency And Optimization

Delivery Mode Return And Tour Return

Besides, there are some other characteristics of emergency supplies. Take the medicine developed by the WMA for example:

i. Uncertainty: because we cannot predict when next Ebola outbreak happens and how terrible death it may bring to victims, so emergency supplies have uncertainties of amount of need and region of giving out.

ii. Irreplaceability: emergency supplies are special in special conditions and are irreplaceable. Like the medicine to cure Ebola, if we do not have the medicine, nothing can effectively cure Ebola patient.

iii. Timeliness: emergency supplies play their role at a certain period and if we miss the very moment, emergency supplies will lose their value. Like the medicine cannot revive already-dead Ebola patients

iv. Hysteresis: emergency supplies (or medicine) always delivered later than a disaster happened.

Thus, our goal is to filtrate several most-needed delivery locations in a country. In detail, we filtrate the delivery locations accord to clustering method and some principles.

5.2 Assumptions and Justifications

i. All delivery location lies in the provincial capitals of the prefectures.

It is evident that the capitals is easy to receive medicine that from developed countries. Namely, the delivery locations are supposed to have quick access to harbors or airports. Meanwhile, they have good public facilities status, road conditions and communication and they are plenty of power, water, heat and gas supply.

ii. Drug-need areas are concentrated on capitals of the prefectures, namely, we send the drug to capitals and do not consider the lower level of administrative areas.

From the size of prefectures, we know they are not large and it is easy for capitals to deliver drug to its lower level of administrative areas. Also, capitals are representative places to an Ebola-hit region. Because of its advanced development and high population density, the more infected people lived in the capitals.

iii. We overlook the cost when constructing delivery locations and the spending in storage of drugs.

Ebola outbreak in these countries and we should pay more attention to people’s health and lives and we should construct delivery locations as soon as it is needed. Actually, the speed of producing drugs is hard to satisfy the intense situation and we need to deliver the drug to the need as soon as possible.

5.3 Clustering Method, A Way to Determine Regions for Medicine

Delivery

We have a relatively clear understanding why the delivery locations have to be places in the prefecture where the provincial capital is located. However, we still have too many delivery locations to build just because of limited foundation in African countries. Thus, to maximal effect of delivery locations with consideration of limited money and other factors that we talked above, we have to make choice among different delivery locations and filtrate some of the delivery locations as ‘last winners’.

We deem two or more major cities in a same country as a ‘city group’ if they are close in distance. It is of little meaning to build delivery locations in each of these cities because we can transmit emergency supplies to each cities conveniently in a short time. It is too dense to build delivery locations in a ‘city group’. So we adopt clustering method to find out ‘city groups’ to divide a country into several regions.

According to the reticular distance (The reticular distance is the distance following the road network using main roads (primary, secondary, tertiary and few track/Trail)), we classify cities as different groups. Here our steps are:

 First we consider all cities in a certain country are independent to each other, namely, no groups contain two or more cities. Find reticular distance between

every two cities and construct a distance matrix D , D is a symmetric (0) (0)

matrix.

 Second, find the minimum element in D and we call it D , then gather G (0) KL k

   G G G , and G into a new group, G , that is, . ( D is the distance M k L L M KL

between G and G , G and G are two groups.) k L k L

 Third, calculate the distance between new group G that generated in second M

step and other group G . Here recurrence formula is j

       D min d min min d , min d min D , D MJ ij ij ij KJ LJ       x G , x G x G , x G x G , x G i M j J i K j J i L j J Refresh distance matrix D by gathering the row where G lies in and the (0) k

column where G lies in into a new row and new column, so we get a new L

distance matrix . D (1)

 Last, repeat the second step until all cities are gathered into a group.

When all steps are done, we will successfully find how many ‘city groups’ in a country.

5.4 Results of Clustering Method

When finish all the steps we described above, we get three clustering pictures of Guinea, Liberia and Sierra Leone and we can use them to accomplish the following task. Here we give Liberia’ clustering results one picture. The other two countries’ district-dividing situation present in the Appendix.

Once we have found ‘city groups’, we have another job to determine how many ‘city groups’ we need and which city in a ‘city group’ should be a delivery location. There are two principles we may need to comply with, one is principle of fairness, and the other is principle of efficiency.

5.5 Principle of Fairness

When a disaster occurs, it not only causes significant property damage but causes a lot of casualties with time going by. We hold an opinion that every life is equal. We cannot ignore the trapped or the patient of Ebola just because they are small in number or the cost of rescue. Providing our hands to everyone who needs help is a symbol of respect life and humanitarianism. Moreover, it enhances the country's sense of trust and identity.

For this kind of principle, we invoke P-Center model to illustrate our delivery locations choosing. Often cities are made up by many communities and other compositions, and there always have people live there. Thus, when we determine a delivery place in a region, life equality is our priority. We use equations to demonstrate the principal.

  P min Z  Z D y ij ij   i I j J

Where i denotes a destination of medicine transportation, j denotes a delivery

place in a region. And D means distance between destination i and a delivery ij

ijy  denotes we have to send medicine to destination i while place j . And 1

 ijy  0 denotes there is no need to do this. So means total distance Z D y ij ij   i I j J we have to cover if there are places need medicine. If a region has even need of medicine, the delivery place often in geographical center of the region.

5.6 Principle of Efficiency

According to population, risks and importance of different regions, we deem these regions of different ‘value’. Then different amount of emergency supplies are allocated to different delivery locations. Only in this way can we utilize the emergency supplies well and response as soon as possible if happens an emergency.

For this kind of principle, we invoke P-median model to illustrate our delivery locations choosing. When we determine a delivery place in a region, efficiency of delivering is our priority. We use equations to demonstrate the principal.

  Q min Y  Y w D y i ij ij   i I j J Where i , j , D and ijy have same meanings as those in principle of fairness. ij

And iw denotes the number of Ebola patients in a place, that is, the more people get

 infected by Ebola, the larger iw is. Thus, means total ‘distance’ Y w D y i ij ij   i I j J we have to cover if there are places needing medicine. The reason why we use

‘distance’ is that we take iw into consideration, so ‘distance’ is not the proper

distance that we comprehend in daily life. Usually the delivery place is nearer to a more serious place in a region.

5.7 Determine Delivery Locations in the Three West African

Countries

Considering emergency of Ebola outbreak in a region, we find ‘city groups’ in Guinea, Liberia and Sierra Leone with criteria of delivering medicine within one day by trucks following the certain route (we will talk it in later part). If delivering time is more than one day, we use clustering method to find other ‘city groups’ to meet the criteria. Then we add the principals we showed above and finally determine delivery place(s) in Guinea, Liberia and Sierra Leone. During estimating process, we give different weight to the principle of fairness and the principle of efficiency. We endow more weight to the principle of fairness than the principle of efficiency because considering we can send medicine within one day, so advantages in time in different places may not play a main role in delivery locations choosing. Primarily, we consider fairness.

Ⅵ Model of Delivery System

6.1 Introduction

In the model of locations of delivery, we have determined some best delivery locations in a country to fit all the need that we put forward. However, only having delivery locations is far from a perfect project to distribute medicine to people who need it most, an effective and considerable delivery strategy is required, or a well-organized delivery system is required.

We define delivery system is made up by well-planned routes to allocate medicine and scientific amount of medicine to distribute to every needed places in every day.

6.2 Symbols and Definitions

SYMBOL

DEFINITION

ijc The Distance Between Two Points

j End Point i Start Point A Route From A Delivery Place To A ijx Destination Number Of Patients In Hospital Who Are In H 1 First Stage

6.3 TSP Model – Well-Planned Routes

Once happens certain scales of Ebola outbreaks, medicine have to be sent to cities or villages as soon as possible. Thanks to TSP (traveling salesman problem) Model, we structure an optimized route for trucks to transport medicine quickly.

 ijx  denotes there is a route We introduce a 0-1 integer variable : ijx ( i j ) 1

ijx  from point i to point j while 0 denotes there is no route from point i to

point j . The TSP Model can be expressed a group of equations.

n n  min c x ij ij   i 1 j 1

 n     x 1, i 1,2, , , n j i ,  ij   j 1  n     x 1, j 1,2, , , n i j , s t . .  ij   i 1    x 0,1, i j , 1,2, , , n ij   no subcycle

n   Where x 1 means there must have a start point i if we want to consider i ij  j 1

n   as a point in route while means there must have an end point j if we x 1 ij  i 1 want to consider j as a point in route. And ‘no subcycle’ means we must cover all points in a certain region, namely, all trucks will cover a route that contains all cities which are in emergency of Ebola outbreak. Moreover, to well describe ‘no subcycle’,

 we add another variable iu i ( 1,2, , ) n and additional constraint condition:

        u u nx n 1, for u u , 0, i 1,2, , , n j 2,3, , , n i j i j ij i j

By now, we have established a model for us to construct a best route for trucks.

6.4 Daily Demand for Medicine

A good delivery system requires precise amount of medicine needed by places every day. We should develop a method to evaluate quantity of medicine we need a day by exploring number of patient in different places. We introduce an assessment standard called urgency index to depict how prob (i) much medicine a place need in one day. The expression of is prob (i)

H in a certain place in one day  prob (i) 1 H in three countries in one day 1

Where H has same meaning as that we have talked in Ebola propagation model, 1

namely, H means number of patients in hospital who are in first stage (such as fever, 1

headache, sore throat, muscle aches and other milder symptoms which often progress

to diarrhea and vomiting). There two reasons why we use H to describe the urgency 1

index, one is the WMA has announced their medicine can cure patients whose disease is not advanced, the other is that patients in first stage have great possibility to become more serious and step into second stage (such as hemorrhaging and multi-organ failure), we need to stop them from worsening.

If we have a certain amount of medicine (we will discuss the amount needed later), we can distribute different amount of medicine to different places to meet patients’ requirement.

Ⅶ Model Implementation of three Countries

7.1General algorithm

In the last part, we have discussed the models and, in fact, we are supposed to combine these models to use in specific situations. Here we give the general algorithm to determine the delivery locations and the transport route.

START

USING CLATER METHOD

DETERMING THE DELIVER

TSP MODEL TO GET THE

INCREASE THE NUMBER OF

CARS FINISH EVERY ROUTE IN ONE DAY?

GET LOCATIONS AND TRANSPORT

END

7.2 Application of Algorithm

By exploring maps from WHO website of different Ebola cases in different places, then adopting TSP Model, we find some routes not only can cover all places that we have to send medicine to, but also consider places with more Ebola cases as more dangerous places and send medicine to the places within less time.

7.2.1 Application in Guinea

Since the area is approximately 245857 square kilometers and we must assure the route solved by the TSP model is not too long, in specific, we considered that one car can cover the distance in one day.

Step 1: only one delivery location

Use the principles which are needed to determine the location, we calculate the delivery location lies in DABOLA. The maximum distance among DABOLA and other prefectures is 585km.

Then use the results of the cluster method, we divided other prefectures into two parts and DABOLA is in respond for the distribution of drugs to them. Thus, we need to solve tow TSP problems.

Step 2: solve the distance route Use the TSP model, we solve the route and use the picture shows the results:

location A B

Confirmed Cases In the map, A and B represent the two route and the distances of them are 1213.8km and 1548.2km. Considering the velocity of vehicles is 80km/h, and it will cost more than 12 hours to finish one route and it is not reasonable for the relief of the disease. Therefore, only one location is not appropriate.

Step3: adjust the number of delivery locations According to the result of cluster results, it is better to divide the prefectures into 3 clusters. Then calculate the 3 different locations, cut every cluster into 2 smaller parts and repeat step2. We get the map:

location D B C 1

A location

E location F

Confirmed Cases

In the map, A, B, C, D, E and represent the two route and the distances of them show in the table:

A B

C D

E F

752.2 686.6 578.0 546.5 640.4 701.2

Vehicles can pass through the distance in one day. We conclude that 3 cluster is enough for Guinea.

And the delivery locations are: DUBREKA, KOUROUSSA, and MACENTA.

The route is listed:

DUBREKAFRIABOKEBOFFACONAKRYFORECARIAH A COYAHDUBREKA

B DUBREKATELIMELEPITADALABAKINDIADUBREKA

C KOUROUSSAFARANAHDABOLAKOUROUSSA

D KOUROUSSASIGUIRIKANKANKOUROUSSA

MACENTAGUECKEDOUKISSIDOUGOU E KEROUANEMACENTA

F MACENTABEYLALOLANZEREKOREYOMOUMACENTA

7.2.2 Application in Liberia

In terms of area, Liberia is smaller than Guinea and its area is 111370 square kilometers. Following the algorithm, like the steps in the analysis of Guinea, and we find only one deliver center is proper for the area.

Here the results are:

Confirmed Cases A

location

B

In the map, A, and B represent the two route and the distances of them show in the table:

A B

869.0 715.6

Therefore, the deliver location is Grand Bassa.

7.2.3 Sierra Leone

In terms of area, Sierra Leone is the smallest among the three countries and its area is 71740 square kilometers.

Just like what we have done before, we apply the algorithm.

Here present the result:

A location

B

Confirmed Cases

In the map, A, and B represent the two route and the distances of them show in the table:

A B

616.9 411.4

Therefore, the deliver location is Tonkolili.

Ⅷ Model of the Quantity of the Medicine Needed and

Manufacturing Speed

8.1 Introduction

In this section, we consider the quantity of the medicine needed and speed of manufacturing of the vaccine or drug together because the manufacturing speed will impact the number of the susceptible, the infected who are in first stage and the recovered. The reason is that if the susceptible are vaccinated, they will hardly get infected by Ebola, and the infected once receive drug they can recover day by day. So the recovered is more than before as we regard the vaccinated people and cured people as the recovered.

8.2 Assumptions and Justifications

 Amount of medicine and vaccine that are produced everyday increase linearly with time when the medicine or vaccine is rare. Because the medicine or vaccine is newly developed by scientists and still in testing stage, so manufactures will not produce a large-scale of this kind of medicine or vaccine at first. So we consider amount of medicine and vaccine that are produced everyday increase linearly with time rather than exponentially with time.

 The infected do not have ability of allopathic medicines. The Ebola virus are relatively stable, namely, variation is not common in Ebola virus. So we consider Ebola virus do not have ability of allopathic medicines.

8.3 symbols and definitions

SYMBOL DEFINITION

V Speed Of Producing Medicine 1

V Speed Of Producing Vaccine 2

1b Initial Inventory Of Medicine

2b Initial Inventory Of Vaccine

‘Manufacturing Acceleration’ Of 1k Medicine Per Day ‘Manufacturing Acceleration’ Of Vaccine 2k Per Day

i Urgency Index

 1 Course Of Treatment Of The Medicine h

8.4 How Fast Need We Produce Medicine and Vaccine

We have talked that Amount of medicine and vaccine produced everyday increase linearly with time in assumption, so we have equations to express the amount that produced per day.

  Medicine V k t b 1 1 1   Vaccine V k t b 2 2 2

Where 1b and 2b denote initial inventory of medicine and vaccine, respectively.

And 1k , 2k mean ‘manufacturing acceleration’ of medicine and vaccine per day.

We show the relationship between V and time t . 1

From the figure 8.1, we get information that when medicine is rare, the amount of medicine produced everyday increases linearly with time until all the patients who are in first stage can get the medicine, and this condition happens nearly 25 days after the medicine is used in the public. Then the amount of medicine that is produced everyday will drop with the number of patients who are in first stage. Namely, we

have more specific equations to explain V . 1

   k t b , V H 1 1 1 1  medicine V 1  H , V H  1 1 1

When medicine and vaccine are used in the public, equations of the susceptible, the infected in first stage and the recover we have shown in the advanced model in sectionⅣ may change (marked in red).

 dS             [ ( I H ) ( I H ) F S ] V  I 1 H 1 2 2 H 2 F i 2 dt  dH       1 h I H V  1 1 3 1 i 1 h dt   dR                  (1 ) I (1 ) I (1 ) H (1 ) H V  1 1 1 2 2 2 1 H 3 1 2 H 4 2 i 2 d t  i is the urgency index that we have described in section 6.4, namely, Where

H in a certain place in one day   1 prob (i) . We distribute medicine with criteria i H in three countries in one day 1

 that we have described in section 6.4, so means number of the susceptible who iV 2

are vaccinated and have antibody to against Ebola, thus, can hardly get infected. And

  means number of the infected who are in first stage get recovered because of V i 1 h

 means course of treatment of the medicine. And  1 the medicine, iV means the 2 h

number of the susceptible who will hardly get infected because of the vaccine. Then we draw a figure to express changing of total cases growing with time in the condition of using medicine.

As for vaccine, it generates its effect mainly among the susceptible. Since number of the susceptible is much much larger than amount of vaccine, we ignore the effect generated by the vaccine. From the figure, we can see the medicine is used after 90 days form initial time, that is, we can figure out that the medicine is used from Feb.1st, 2015. And 50 days after using the medicine, number of total cases will not increase, which means the medicine has its positive impact on Ebola containing.

b  5 The parameters in our calculating process are (we produce 5 units of 1

k  medicine per day at the beginning of producing) and 5 (we produce 5 more 1 units of medicine per day).

As for vaccine, we ignore it in our calculating process for it is much much less in number compared to number of the susceptible.

8.5 The Quantity of the Medicine Needed

We use integral computation to find the quantity of the medicine we need. So total needed amount is t  w V t dt ( ) 1 0 Use parameters we have calculated in last section, we draw a figure to show the quantity of the medicine.

So we need about 3400 units of medicine to cure the patient who are in first stage in the three west African countries.

If we develop better medicine that can cure patients in second stage in the future, we believe the quantity of medicine can decrease.

Ⅸ Other Factors We Think Are Important

In our first model –SEIIRF model and its advanced model, we didn’t consider other two factors that we think are necessary to discuss. One is control of Ebola spreading in hospitals, and the other is control of Ebola spreading in funerals.

If we control of Ebola spreading in hospital, there will be less healthy people get infected. We regard a hospital as a ‘huge’ patient with strong ability of infection. We must take measures to reduce the ability of infection. The figure shown below delivers us information that hoe the total cases in Guinea will be like if we reduce 50% and 90% of the ability down.

We can see from the figure, if we take strategies to control Ebola spreading in hospitals, total cases will reduce greatly and significantly.

Then if we control Ebola spreading in funerals, what will happen? There is a figure will tell us.

Controlling Ebola spreading in funerals maybe are not as good as in hospitals. But at least, it does its positive effect on reducing total cases in the future.

Ⅹ Future Improvement

10.1 Optimization of Coverage to Determine Delivery Locations

Since we are introduced one method and two principles in delivery places choosing, now we can easily make a decision on where to build a delivery place in a certain region. However, as a designer, we must be more considerable if we have more time to do our design. Unfortunately, time is limited, here we just introduce you another principle that is worthwhile to consider – principle of optimization of coverage. When a disaster occurs, we will generally distribute emergency supplies which are relatively near to the place that happens the disaster as fast as possible. Considering the disaster, like Ebola, is usually of great impact on the local and of tremendous harm, we sometimes need to allocate and transport more emergency supplies to this area. Thus, when we choose to delivery places we must take it into consideration that the delivery places can cover as many emergency-supplies-need regions as possible simultaneously. So when an emergency happens in an area that covered by a delivery place, emergency supplies, like the medicine, can be sent in time. Here the equations of the principle are   X max A  A wc y i ij ij   i I j J

Where i , j , iw and ijy have same meanings as those in principle of fairness.

And we call ijc degree of coverage.

  1 , t t m    t t   c , t t t 1  ij 1 m  t t  m 1   0 , t t  m

Where 1t is minimum time of a truck to arrive at a destination while mt is

maximum time of a truck to arrive at a destination. In our model of delivery places

choosing, mt is no longer than one day. From expression of ijc , we can see the

degree of coverage increases with time going by, which is consistent with reality.

10.2 A No-boundary Scheme

In our paper, the models of locations and TSP apply in three countries (Sierra Leone, Liberia and Guinea) respectively. We consider there is no contact among these Ebola-hit countries and the delivery locations distributed in three countries and every countries delivery locations only send needed drug to itself. However, we human beings should unit to eradicate the Ebola in the face of such serious situation. Therefore, we are better to combine the three countries tightly and arrange the delivery locations and transportation system without considering the boundary and political problems.

So a no-boundary scheme can be developed to quickly get rid of the trouble of Ebola.

Ⅺ Sensitivity analysis

11.1 Sensitivity Analysis of SEIIRF Model

We get some parameters through the method of least squares fitting in the model to predict the spread of Ebola,. To test the effect of changing parameters, we will produce a sensitivity analysis that shows whether our model is properly sensitive to these variations.

In the following section, we will analyze the sensitivity of total cases of patients, , Length Of First Stage Of Illness (Not In 1 according to Average Incubation Period

1, Transmission Parameter For First Stage Of Illness (Not In Hospital) 1 Hospital)

, ,  respectively. In specific, we modified parameter ( 1) by  10% 1 1

respectively and observe the change of total cases.

 to the total cases

1

From the picture above we can get the result that the total cases of patients change

. So this proves the slight fluctuations of  can be little with the change of 1 1

ignored and the results we conclude in the above models are reliable.

1 to the total cases

As the figure shows, the total cases stay relatively stable in different result

1. Therefore, the total cases we use is exact enough. generated from different

11.2 Sensitivity Analysis of Model of the Speed to Produce Medicine

We change initial speed of the production of medicine 1b and total cases of

patients are shown in the following the figure:

1b to the total cases From the picture above, we find that if the speed 1b is relatively small, the

influence of the change of 1b is larger compared to bigger 1b . In addition, we find

that cases increase with the increase of initial speed and the trend is expected. In all, the results are stable.

Ⅻ Conclusion

11.1 Strengths and Weaknesses

Now we will analyze the strengths and weaknesses of models in our paper:

SEIIRF Model

Strengths 1. The results of model conform to the reality well, such as the prediction of the number of patient cases. 2. We considered three ways of the spread of Ebola which are relatively comprehensive and more groups of people which are representative to the disease search.

Weaknesses 1. There are more parameters in the model and it may bring negative influence to the sensitivity. 2. Due to lack of data, we do not study spatial distribution of Ebola.

Model of Locations of Delivery and Delivery System

Strengths 1. We use TSP model which is relatively simple but effective to solve the delivery system. 2. We develop a general algorithm to determine the transportation locations and system. Weaknesses 1. Because the limit of time, we do not solve the the no-boundary scheme which is presented in the part of future improvement.

Model of the Speed to Produce Medicine

Strengths 1. We calculated the model on quantitative analysis.

Weaknesses 1. The speed to producing drug grow linearly and this process maybe too ideally

11.2 Overall Results

Up to now, we have accomplished all our tasks. And here we give the overall results of all our models.

Above all, we develop basic SEIIRF model and then improve this model to predict the spread of Ebola, and finally the model confirms to the reality which we test it using collected data. Then, we establish a general algorithm to solve the delivery locations and design delivery system. In specific, we get the locations of delivery and the certain route of transportation system through cluster analysis and TSP model. Also, the length of all routes is suitable for the delivery of drug. With the route, we can distribute drug according to urgency index which is relevant to the proportionality of the patients. Considering the specific speed of producing the drug, we simulate the situation and get the conclusion that in 50 days, we can eradicate Ebola. After that, we consider other factors, such as control of Ebola spreading in hospitals and in funerals, and the situation can be relieved greatly. At last, we test the sensitivity of our model and it shows that they are stable.

LETTER

To: Professors of the World Medical Association

From: Team # 34317

Date: February 9, 2015

Subject: A Battle against Ebola

Ebola, a familiar but strange word to us. No one can

imagine the name ‘Ebola’ just originates from a little

river - Ebola River in Congo. Contrary to its attracting

meaning, it is true that the Ebola virus do take lots of

victims’ lives away. Fighting against Ebola is now a

worldwide battle. We human beings need to unit together

and offer helps to each other. Besides, we are really

appreciate those doctors in the MSF who fight against

Ebola day and night in West Africa.

We also do our best to evaluate Ebola spreading in West

Africa. We use models to predict future cases in Guinea,

Liberia and Sierra Leone. First, we use real data to

calculate a curve for usage of prediction. Then we use

newest data in the WHO website to test the curve. We

find the curve can predict well and be trusted. Then, we use this curve to predict future cases including total cases

and death cases. And we find that if we use medicine,

total cases and death cases will decrease a lot.

Then we design a method to find some best delivery

places in Guinea, Liberia and Sierra Leone that can

allocate medicine quickly to places where Ebola

outbreaks. Moreover, we offer you schemed routes both

are time-saving and able to caver most places for

vehicles to transport emergency supplies.

At last, we calculate out the quantity of the medicine

needed and the speed of manufacturing medicine and

vaccine. We take two conditions into consideration. One

is the condition that if medicine is too rare to help most

people, the medicine factories should gradually increase

their output, and the other condition is that if medicine is

enough for the infected, the amount of medicine should

decrease with time. The total amount of medicine is 3400

units.

Besides, we have done other jobs to evaluate Ebola, you

can see our paper for details.

Yours sincerely ⅩⅢ Reference

[1]http://www.theguardian.com/commentisfree/2014/dec/29/2015-ebola-eradicated-ep idemic-west-africa [2]http://www.huffingtonpost.com/darius-mans/behavior-change-is-key-to_b_575270 4.html [3] Tzeng, G H.,Cheng, H. J., and Huang, T. D. Multi-objective optimal planning for designing relief delivery systems. Transportation Research Part E: Logistics and Transportation Review, 2007,43(6),673-686. [4] http://www.diva-gis.org/datadown [5] Marisa C. Eisenberg, Joseph N.S. Eisenberg, Jeremy P. D'Silva, Eden V. Wells.” Modeling surveillance and interventions in the 2014 Ebola epidemic” The Lancet Infectious Diseases(2015). [6] Chen zhi-zong, “Major events multi-objective decision model of facility location of emergency rescue”, MANAGEMENT SCIENCES IN CHINA(2006). [7] PANG Hai-yun, LIU Nan, WU Qiao, “Decision-making model for transportation and distribution of emergency materials and its modified particle swarm optimization algorithm” Control and Decision(2012). [8] ZHU Jian-ming, HUANG Jun,” Randomized Algorithm for Vehicle Routing Model for Medical Supplies  in Large-Scale Emergencies”, OPERATIONS RESEARCH AND MANAGEMENT SCIENCE(2010). [9] Liu Fang, “A brief introduction to the U.S. Strategic National Stockpile”, Mil Med Sci. Vol 38, No.11, 2014. [10] http://maps.who.int/MapJournal/?appid=5b29178821dd4584b78dcb18d280326a [11] Gu Yong, ”Based on the mechanism of the prevention and control infectious disease emergency supplies demand analysis”, Journal of Wuhan University of Technology, 2010.
