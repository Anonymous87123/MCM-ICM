2016 MCM/ICM

Summary Sheet

(Your team's summary should be included as the first page of your electronic submission.)

Summary

With thousands of refugees moving across Europe and more arriving each day, considerable attention has been given to refugee integration policies and practices in many countries and regions.  We build a series of models to explore the factors involved with facilitating the movement of refugees from their countries of origin into safe haven countries.

Firstly, we optimize the Control Variable algorithm to build a model to analyze the measures and parameters of the crisis. We set factors such as the psychological quality and faith of refugees, the resources and refugee policy of the refugee-receiving country, the refugees’ saturation of the refugee-receiving country and the natural disaster or terrorist. Finding out that every factor is of crucial importance, and the more favorable the conditions are, the more likely the refugees move to the safe countries.

Secondly, we use the index set above to analyze the flow of refugees. From the optimized Small World Network algorithm, we find that there are 637000 refugees arriving EU a year, among them, 311000 refugees will transfer via Eastern Mediterranean, 221000 refugees via West Mediterranean, 45000 refugees via West Balkans, 32000 refugees via Eastern Borders, 18000 refugees from Albania to Greece, and 10000 refugees via Central Mediterranean. And the transfer rate should be controlled below 50187 per month.

Thirdly, we consider the parameters set in task 1 are dynamic, finding out that our model is also applicative while we should adjust the details in our model.

Finally, we make a report to discuss our model in detail and raise the needed policy support. We analyze the impact of exogenous events as well. Meanwhile, we state the scalability of our model. Then we believe that our model can solve most of the problems.

In the end, we analyze the stability and sensitivity of model. We also conclude the strengths and weaknesses of our model. Further, the accuracy of our model needs improving.

Introduction

 Background

With hundreds of thousands of refugees moving across Europe and more arriving each day, considerable attention has been given to refugee integration policies and practices in many countries and regions. History has shown us that mass fleeing of populations occur as a result of major political and social unrest and warfare. These crises bring a set of unique challenges that must be managed carefully through effective policies. Events in the Middle East have caused a massive surge of refugees emigrating from the Middle East into safe haven countries in Europe and parts of Asia, often moving through the Mediterranean and into countries such as Turkey, Hungary, Germany, France, and UK. By the end of October 2015, European countries had received over 715,000 asylum applications from refugees. Hungary topped the charts with nearly 1,450 applications per 100,000 inhabitants, but with only a small percentage of those requests granted (32% in 2014), leaving close to a thousand refugees homeless per every 100K residents of the country. Europe has established a quota system that each country has agreed to take in a particular number of refugees, with the majority of the resettlement burden lying with France and Germany.

 Our Work

Firstly, we optimize the Control Variable algorithm to build a model to analyze the measures and parameters of the crisis. We set the psychological quality of refugees, the faith of the refugees, the material and financial resources of the refugee-receiving country, the refugee policy of the refugee-receiving country, the refugees saturation of the refugee- receiving country and the natural disaster, terrorist as factors, finding out that every factor is important to the crisis, and the more favorable the conditions are, the more likely the refugees move to the safe countries.

Secondly, we use the index set above to analyze the flow of refugees. From the optimized Small World Network algorithm, we find that there are 637000 refugees arriving EU a year, among them, 311000 refugees will transfer via Eastern Mediterranean, 221000 refugees via West Mediterranean, 45000 refugees via West Balkans, 32000 refugees via Eastern Borders, 18000 refugees from Albania to Greece, and 10000 refugees via Central Mediterranean. And the transfer rate should be controlled below 50187 per month.

Thirdly, we consider the parameters set in task 1 are dynamic, finding out that our model is also applicable while we should adjust the details in our model.

Finally, we make a report to discuss our model in detail and raise the needed policy support. We analyze the impact of exogenous events as well. Meanwhile, we state the scalability of our model. Then we believe that our model can solve most of the problems.

Assumptions

Ignore the slim refugees country. The countries that have few refugees or receive few refugees do not have much influence on our model.

Ignore the time of preparation for transfer. The time of preparation for transfer cannot determine its significance completely, and we take the time of preparation for transfer into consideration when we discuss the mutual reference of all work.

Symbol Meaning 1F the success rate of refugees arriving in safe-haven countries (1) refugees’ psychological diathesis of their own diathesis F 1 (2) refugees’ physical diathesis of their own diathesis F 1 (3) F refugees’ cultural accomplishment of their own diathesis 1 (4) refugees’ choice of route of their own diathesis F 1 F the influence that countries’ policy brings to refugees 2 (1) the religious policy of the country F 2 (2) F the number of refugees the country can feed 2 (3) F financial and material resources of the country 2 (4) the policy of the country refugees passed F 2 F the impact of some emergency events 3 (1) F the threat of the terrorist in the route 3 (2) F the threat of nature disaster in the route 3 GS Flag whether country i and country j have the same religion ,i j Sr the saturation rate of the refugees in country i i Sp the contribution rate for refugees i Ds the refugee mortality ij Pk the number of refugees from country i to country j ij G the cost of refugees from country i to country j ij ( )t Po the instant resources of safe-haven country j ( )t PN the number of refugees that the safe-haven country can hold j ( )t PK the instant number of the safe-haven country j received j The degree of discrepancy on environment and Climate between refugee- Ha exporting i and the  safe-haven country j ij

The degree of discrepancy on religion and law between exporting country Hb ij economici and the  safe-haven country j The degree of discrepancy on economic and culture between refugee- NG ij exporting i and the  safe-haven country j the transfer matrix of refugees from their country i to safe-haven country  ij Hp j the  conflict between refugee-exporting country i and the safe-haven Wa ij country j Pd The relationship between two safe-haven country(i and j ) ij Task 1: Metrics of refugee crises

We consider the influence factors of the movement of refugees from three aspects. Firstly, in order to arrive at the asylum safely, the diathesis, which includes psychological diathesis, physical diathesis, the cultural accomplishment of refugees and the refugees’ choice of routes, is significant. Being refugees is a cruel thing, which is a heavy blow. If refugees do not have great psychological diathesis, they might be breakdown during the movement. Therefore, they cannot arrive at the asylum safely. It will be hard for them to complete the migration as well if the refugees are not healthy enough since the movement always be hard and taking a long time. Moreover, In the process of movement, refugees will go through many different countries and regions, thus a better understanding of the countries’ language, customs and cultural characteristics will surely help to increase the probability of fleeing successfully. As for refugees, there is often more than one route. Therefore, the choice of route, which is made by refugees, influences the success rate of movement. Choosing a safe and suitable route will increase the success rate of movement. On the other hand, once the refugees chose an unsuitable dangerous route for themselves, it would reduce the success rate of movement. [1]        (1) (2) (3) (4) (5) F f F F F F F (1) 1 1 1 1 1 1

(1) means psychological diathesis of refugees’ diathesis F 1

(2) means physical diathesis of refugees’ diathesis F 1

(3) means the cultural accomplishment of refugees’ diathesis F 1

(4) means the refugees’ choice of route of refugees’ abilities F 1

(5) means the wealth of refugee F 1

We rank the five factors of the refugees with 1 to 10 representing capacity from low to high, then we have

          (1) (2) (3) (4) (5) F F F F F F (2) 1 11 1 12 1 13 1 14 1 15 1

For the contribution of these five factors，we are in accordance with the actual situation， then we have

     (1) (2) (3) (4) (5) F 0.6 F 0.8 F 0.4 F 0.3 F 0.2 F (3) 1 1 1 1 1 1

Secondly, as for the influence of the countries and regions where they stopped over, we believe factors of refugees, including the religious policy of countries, the number of refugees the countries can accommodate, the country's financial and material resources, the national policies on refugee. Meanwhile, the religious policy of the country has a great influence, because a large part of refugees’ movement is for religious persecution. And the number of refugees the country can accommodate influences the movement of refugees as well[2]. For the current situation of highly developed information technology, most of the refugees will choose the best escape route, which is the most popular route. In this case, the

countries which are on the most popular route will undertake more pressure. If those countries can accommodate a large number of refugees, they will be bound to increase the success rate of refugees’ movement, which is on the contrary will have a negative impact on the refugees’ escape. For the country's financial and material resources, it can directly affect the process of refugees’ movement. As for refugees, they need to get funding from the country on the route, and this support is bound to affect the movement. Moreover, it is equally important for policies towards refugees in those countries. If the country is kind for refugees, then it will be beneficial to the refugees fleeing. On the contrary, if the country is against helping refugees, it will bring adverse effect to refugees fleeing[3].

      (1) (2) (3) (4) F g F F F F (4) 2 2 2 2 2

(1) means the religious policy of the country F 2

(2) the number of refugees that the country can accommodate F 2

(3) means the country's financial and material resources F 2

(4) means the national policy on refugee F 2

We rank the four factors of the via countries，with 1 to 10 representative capacity from low to high，then we have

        (1) (2) (3) (4) F F F F F 2 21 2 22 2 23 2 24 2 (5)

For the contribution of these four factors, we are in accordance with the actual situation， then we have

    (1) (2) (3) (4) F 0.9 F 0.8 F 0.5 F 0.4 F (6) 2 2 2 2 2

Thirdly, several external factors also have a certain impact on refugees’ movement. Meanwhile, the illness, nature disaster and the threat of terrorist on the route are important as well. From the point of the refugees’ safety, the impact of these factors on the refugees is more obvious.

    (1) (2) F h F F 3 3 3 (7)

(1) F means the threat of the terrorist in the route 3

(2) F means the illness, nature disaster in the route 3

We rank the two factors of the refugees with 10 to 1 representing capacity from low to high，then we have     (1) (2) F F F (8) 3 31 3 32 3

For the contribution of these two factors，we are in accordance with the actual situation， then we have

  (1) (2) F 0.8 F 0.8 F (9) 3 3 3

Among the factors that we have discussed above, the refugees’ diathesis is the most direct, the policy countries refugees transfer through is the most important, the refugees’ movement in the route is the most intense. Then we have      F v F F F 1 2 3 (10)

      F F F F (11) 1 1 2 2 3 3

   F 0.7 F 0.8 F 0.9 F (12) 1 2 3

10 Mentality Physical Culture 9 Choice Ability Resource 8

7

6 Degree/De 5

4

3

2

1 0 1 2 3 4 5 6 7 8 9 10 Capacity/Ca

As indicated in Figure 1, the optimization of all parameters will improve the transfer rate of the refugees. But,the degree of ascension is not exactly the same. And as we can see, the physical quality is the first ,mentally quality is the second, the literacy is the third,the choise ability is the fourth,and the resource is the last.

20 20

15 15 Influence Influence 10 10

5 5

0 0 10 10 10 10 8 8 5 5 6 6 4 4 2 2 0 0 0 0 Space Country Resource Region Region 15 15

10 10 Influence Influence 5 5

0 0 10 10 10 10 8 8 5 5 6 6 4 4 2 2 0 0 0 0 Country Resource Policy Space Region

To make a further study, we made Figure 2-Figure7 to observe the influence of different parameters. And from the results, we can find the slight difference.

Task 2: Flow of refugees

According to the information given in the task, we find that the refugees are mainly from Syria, Afghanistan, Eritrea, Kosovo and other areas. Their destinations are mainly countries such as Greece, Bulgaria, Italy, Spain, Malta and Cyprus. In this task, we mainly aim at the evaluation factors and parameters given in task 1, given the total number of refugees can be assumed, as well as the entry rate for each country at the entrance. To begin with, we identify the geographical relations between the 4 main refugee-exporting countries and the six refugee-receiving countries, the relations between the religious belief of these countries and taking the process from the entrance of the country transferring to other countries as a second shift into account [4].

Firstly, we consider the religious belief relations among the main refugee-exporting countries, the main refugee-receiving countries and second shifting countries. According to our assumption, religion is the decisive factor of the refugees’ movement, which means if their religions are different, there will not be transfer among the countries.

Country Region Country Region Greece The Orthodox Eastern Church Spain The Catholicism (90%) Italy The Catholicism (90%) Malta The Catholicism The Orthodox Eastern Church The Orthodox Church (50%) Bulgaria (90%) Cyprus The Mohammedanism (50%) The Mohammedanism (10%)

Then we consider the main reason why the refugee countries have refugees. The main refugee countries are Syria, Afghanistan, Kosovo, Iraq, Albania, Pakistan, Eritrea, Nigeria, Serbia and Ukraine. Most of the countries which have experienced or are now enduring the war and conflict, and like the Eritrea become refugees exporter mainly because their citizen suffering long-term abuse. For Kosovo, it is the war that led to the long-term poverty, in this case , the refugees’ mental are likely to exist some problems, and other qualities of refugees may not that important of the refugees’ movement[5].

Afterwards, the financial and material resources of the refugee-receiving countries should take into account.  As for the six refugee-receiving countries, Greece and Italy can accommodate more refugees, but the financial and material resources of the Bulgaria, Malta and Cyprus are slightly weaker. For the second shifting countries, Germany, Sweden, Switzerland and other countries are great power. And we give the essential information in

Countr Country Region Region y Syria The Mohammedanism(most) Pakistan The Mohammedanism Afghanista The Mohammedanism Kosovo The Mohammedanism n The Mohammedanism The Mohammedanism (50%) Eritrea Nigeria (50%) The Christianity (50%) The Christianity (50%) The Orthodox Eastern The Mohammedanism(most) Iraq Serbia Church The Christianity The Christianity The Orthodox Eastern Church(70%) Ukraine The Mohammedanism The Mohammedanism (20%) The Buddhism

Country Region Country Region Austria The Catholicism Finland The Christianity Belgium The Christianity Malta The Catholicism Luxembourg Poland The Catholicism The Catholicism（90%） Germany The Christianity Portugal The Christianity Spain Sweden The Christianity The Catholicism（90%） the Orthodox Eastern Church The Orthodox Church (50%) Bulgaria Cyprus The Mohammedanism (10%) The Mohammedanism (50%) The Catholicism The Catholicism (90%) Netherlands Slovakia The Protestant The Christianity The Christianity Latvia the Orthodox Eastern Church Romania the Orthodox Eastern Church The Luther Protestant

Country ADGP Population Country ADGP Population Italy 33115 59685227 Greece 22055 10815197 Spain 29289 47265321 Malta 20852 452515 Cyprus 26389 1117000 Bulgaria 7033 7364570 Country ADGP Population Country ADGP Population Sweden 56956 9555893 Malta 20852 452515 Austria 47083 8032926 Portugal 20178 10487289 Netherlands 46142 16788973 Slovakia 16726 5410836 Finland 46098 5421827 Latvia 13899 2217000 Belgium 43686 11035948 Poland 13540 38186860 Germany 41513 80399300 Rumania 7934 20121641 Spain 29289 47265321 Bulgaria 7033 7364570 Cyprus 26389 1117000 Luxembourg 107206 537853

When it comes to the refugee policy of the refugee-receiving countries, for most of these countries are the members of EU, so most of their policies for refugees are loose. However, because some countries do not have a large population, receiving more refugees will inevitably lead to its population imbalance and brings some social problems, so there will be a certain number of restrictions on the number of refugees[6].

Austria Luxembourg Malta Syria Poland Greece Spain Afghanistan Belgium Finland Kosovo Bulgaria Germany Portugal Sweden Iraq Italy Bulgaria Pakistan Cyprus

Spain Eritrea Slovakia

Nigeria Malta Latvi Serbia

Cyprus Netherlands Ukraine

Romania

When considering external factors, we mainly think about refugees finish the transfer whether by land or by water. Because of the pirate and the stormy waves in the sea, the mortality of transferring by water is higher than by land.

   GS ( re re , ) i j , i j     (13)  i 1,2, ,10; j 1,2, 25.



，means nation i and nation j have the same religion, GS 1 i j ,  ，means nation i and nation j have different religion GS 0 i j ,

Define the saturation rate of the refugees:

 Max _ r  Sr i  i Num i (14)   i 1,2, ,10  

Max _ i r means the maximum number of refugees accepted by the refugee-receiving country

Num means the population of the refugee-receiving country i

Define the contribution rate of refugees,

   Sp GDP p i i i  (15)   i 1,2, 25. 

GDP means annual GDP of the refugee-receiving country i i

ip means the contribution rate of refugees of the refugee-receiving country i

ip is not only include economic strength of the refugee-receiving country i, but the refugee policy as well.

Define the refugee mortality，

  Ds Dr ij ij  (16)    i 1,2, ,10, j 1,2, ,25. 

Dr only has two values，if the two countries i and j are connected by water , Dr =0.08 ij ij

Dr =0.005. Or they are connected by land, ij

Therefore the total number of refugees can be accommodated is

10 25    (17) A GS Pk s ij ij   i 1 j 1

6    max A GS Pk s ij ij   i 1 j 1  25 25 25       Pk Max _ r Num Sr  ij i i i    j 1 j 1 j 1  (18)  25    Pk G Sp  ij ij i   j 1    i 1,2, ,10.  Pk means the number of refugees from the refugee-exporting country I to the refugee- ij receiving country j

G means the cost of the refugee-receiving country i receive one refugee from the ij refugee country j

We calculate the number of refugees that transfer from refugee- exporting country(i) to the refugee-receiving country(j) Rn with formula ij

 Max _ r     Rn max A Ds Sp i ( GS , p )  ij s ij i i j , i Num i (19)    i 1,2, ,10; j 1,2, 25.  

And then we can get the results with the help of MATLAB

Greece Bulgaria Italy Spain Malta Cyorys Syria 16788 34534 25 24546 45245 45234 Afghanistan 12456 0 642 43643 42364 23462 Kosovo 567 345 234 45643 45624 22346 Iraq 1235 2456 0 12344 456 454 Albania 2346 0 0 245 45 0 Pakistan 0 45 0 4524 44 0 Eritrea 0 642 45 546 0 435 Nigeria 123 234 0 464 4325 0 Serbia 665 0 425 667 1245 345 Ukraine 0 0 0 45 452 0 As reached from the 2004’s and 2005’s data, we can predict the transfer rate with the number of refugees and the refugees transferred from refugee-exporting country (i) to the refugee-receiving country(j).and the average result is 50187 per month.

To show the results in detail, we show the transfer graph with the help of pajek.

As we can see from the transfer graph, the transfer of refugees is a little sparse. And this can be explained plainly. Most of the transfer of refugees is influenced by the religion of the refugees, so it will be impossible for some refugees to transfer from a refugee-exporting country to a refugee-receiving country.

Task 3: Dynamics of the Crisis

As time goes by, refugees themselves, the policy of the refugee-receiving countries or the external factors of the movement are not set in the stone. The refugees’ psychological diathesis, religious belief and wealth as well as the refugee-receiving countries’ financial and material resources and capability of refugees and the nature disaster will change over time. However, the refugees’ physical diathesis, the population and policy of the refugee-receiving country can be seen as fixed in a short time[7].

If the movement goes well, the refugees’ psychological diathesis will be better, but if it is not, their psychological diathesis will be worse. However, refugees’ wealth must be less during the movement. Also, their religious belief will be reformed gradually for necessity of themselves. Next, the refugee-receiving country’s financial and material resources and the capability of the refugee will change during the transfer time. If the refugees have gone to the so-called ideal destination, the ideal refugee-receiving country's financial and material resources, as well as the capacity to accommodate refugees will reduce. Besides, the impact of natural disasters, such as disease, weather and other natural disasters, in the process of refugee transfer, is a stochastic process.

However, if the transportation, religion, policy and the financial and material resources of the refugee-receiving country suit the refugee country, it will increase the refugees’ saturation capacity of the refugee-receiving country. Nevertheless, if the refugee-receiving country's financial and material resources are relatively adequate and the amount of refugees received is little, it can increase the resource consumption of the refugees in the country,  on the contrary, it can reduce the resource consumption. Among them  the saturation capacity of the refugee-receiving country needs to be priority considered.

The between refugee-exporting country i and the refugee-receiving country j will GS ,i j change

     GS ( re re , ) ( rp rp , ) i j , i j i j     (20)  i 1,2, ,10, j 1,2, ,25.



 where has same definition in task 2. ( re re , ) i j

 means if the refugee-exporting country i is reformed by the refugee- ( rp rp , ) i j  ，or   receiving country j, so ( rp rp , ) 1 ( rp rp , ) 0 . i j i j

Denote the refugee-receiving country's financial and material resources by j   j   Po , 1,2, 25. the capability of the refugee-receiving country by PN , 1,2, 25. and j j j   the amount of received refuges of the refugee-receiving country by PK , 1,2, 25. then j we have，

 ( ) t PK j   ( ) t (0) Po Po  j j Max _ r j  j 1,2, ,25.  

( )t means the instant financial and material resources of the refugee-exporting country Po j

( )t Po means the instant financial and material resources of the refugee-exporting country j

(0) Po means the financial and material resources of the refugee-exporting country j

( )t Po means the instant financial and material resources of the refugee-exporting country j

(0) Po means the financial and material resources of the refugee-exporting country j

( )t PK means the instant amount of refugees that the refugee-exporting country recieived j

Max _ r means the refugees’ saturation capacity of the refugee-exporting country j

( ) ,     ( ) t (0) t PN PN PK j 1,2, ,25 j j j

( )t PN means the instant refugees’ capability of refugee-exporting country j

(0) Po means the refugees’ capability of the refugee-exporting country at the beginning j ( )t means the instant amount of refugees received by the refugee-exporting country PK j

If we add the refugees from Canada, China and U.S, our model is applicable to a certain extent, since the factors that should be considered are the same. However, people in these three countries are relatively concentrated in their religious beliefs, and the traffic to the refugee-receiving countries in Europe is complex as well as they are all great nations of politics, economics and culture. As a result, their refugees’ movement is complicated[8].

With the help of pajek, we show the result modified in the Figure 8.

The graph shows the results that adding more conditions , and the results can explain the phenomenon that is difficult to explain in task2.

Task 4: Policy to Support Refugee Model

Since the United Nations Commission requires us to give priority to the health and safety of the refugees and the local people, to the optimal conditions for the optimal migration model in this case, we adopt the method of loop analysis.

First of all, our ultimate goal is to ensure the health and safety of the refugees and the local people, as a result, we should choose the safe route and suitable refugee-receiving country. In order to ensure the health and safety of local people, we should try to control the transfer of the refugees in a suitable range. Meanwhile, the received refugees should be on the same level of religious belief and cultural attainments with the local people. In this case, we use the Space-time analysis of algorithm analysis, to find a balance between the amount of the transfer of refugees and refugee-receiving countries. Also, the consulates between the refugee-exporting country and the refugee-receiving country plays an important role, if the refugee-receiving country has a perfect  consulate which will lead the balance to the higher level. On the contrary, if its consulate is not that good, the balance will be low. Besides, some non-governmental organizations also play an important part. On one hand, these organizations can ensure the refugees’ safe and basic needs. On the other hand, they can protect the local people of the refugee-receiving country. In addition, we need to consider whether it is suitable for refugees to live in the receiving country, the conflict of weather, eating habit and life style between two countries should be taken into account[9].

Another factor that should be considered is the policy of the refugee-receiving country. Firstly, whether the refugees’ religious belief and habits are illegal in receiving country and whether there are conflicts of laws between two countries. Under the circumstances, for ensuring the safety of the refugees and local people is the most significant thing, the amount of refugees that can transfer to the receiving country will be smaller and the speed of the movement can be slower.

We define       (1) (2) (3) Ha h , h , h , ij ij ij ij  (22)     i 1,2, ,10, j 1,2, ,25.  

means eating habit, life style and weather of the refugee-exporting country i and the  ( ) v h 0 Ha refugee-receiving country j preset value is 1, for ，if there is great conflict ij ij  ( ) v h 0.1 between refugee-exporting country i and the receiving country j，then ，or ij  ( ) v h 0 ，finally ij      0     (1) (2) (3) ( ) v Ha h , h , h , Ha h  ij ij ij ij ij ij  v 1 (23)    i 1,2, ,10, j 1,2, ,25.  

Ha  Ha  0 0 if ，then . ij ij

    ，means the comparison of religion, laws and (1) (2) (3) Hb hb , hb , hb , Define ij ij ij ij other points between refugee-exporting country i and the refugee-receiving country j. For ( ) v random ，if there exist great conflict between refugee-exporting country i and refugee- h ij      (1) (2) (3) Hb hb , hb , hb , 0 receiving country j on this factor, then ，or ij ij ij ij     . (1) (2) (3) Hb hb , hb , hb , 1 ij ij ij ij

We have the final transition probability matrix between i and j

   Hp Hp Hp 11 12 1 v    Hp Hp Hp          21 22 2 v Hp Ha Hb (24)      ij ij    Hp Hp Hp   v 1 v 2 vv Then we consider the impact of non-governmental organizations

      (1) (2) (3) NG ng , ng , ng , ij ij ij ij  Define (25)     i 1,2, ,10, j 1,2, ,25.  

means non-governmental organizations which include economy, culture, sports and so on.

 0  ng ( ) v ( ) v preset value is 0，for ng ，if it has interest between i and j, then ng 0.01 ， ij ij ij  ( ) v or ng 0 ，final ij

        0  (1) (2) (3) ( ) v NG ng , ng , ng , NG ng  ij ij ij ij ij ij  v 1 (26)    i 1,2, ,10, j 1,2, ,25.  

Take this factor into account in the transition probability matrix          ' ' ' Hp NG Hp NG Hp NG Hp Hp Hp 11 11 12 11 1 v 1 v 11 12 1 v          ' ' ' Hp NG Hp NG Hp NG Hp Hp Hp         '     21 21 22 22 2 v 2 v 21 22 2 v Hp Hp NG            ij ij          ' ' ' Hp NG Hp NG Hp NG   Hp Hp Hp     v 1 v 1 v 2 v 2 vv vv v 1 v 2 vv

With the help of MATLAB, we can calculate the matrix, and the results are as follows,    0.78 0.11 0.23    0.44 0.12 0     ' Hp = (27)       ij    0.66 0.61 0.25  

From the results, we can find out that cultural restraint and religion have important influence to our movement of refugees, so we suggest that give priority to the cultural restraint and religion.

Task 5: Exogenous Events

Taking exogenous events into consideration, some of the parameters like index of policies and regulations in our model may be significantly changed for these events happen suddenly. For example, once conflict break out between the refugees-exporting countries and the refugees-receiving countries, even the refugee-exporting countries make war on their neighbours and partners. In this case, the transfer from the refugee-exporting countries to these countries would be completely closed, and at the same time the refugees which belongs to refugee-exporting in these countries must be resettled in other countries. So it is mainly affected the saturated of the refugees receiving countries to other refugees receiving countries, which can instantly drop to zero. Surely, the policies of the refugees-treatment would also change. Compared with other factors, the most direct one is the external factors we have set, which can cause the increase of the death rate on some routes[10].

For the neighbour of refugees receiving countries, if the war break out between the refugee-exporting country and the receiving country, it will be a new receiving country. That’s because the refugees coming from exporting countries won’t come back to their hometown, and most of them will go to the neighbours of their living country. But the contradiction appears in that condition, the living country may put pressure on their neighbours to refuse the refugees.

Based on the above, we take more consideration of external factors in our model.

      (1) (2) (3) Wa Wa , Wa , Wa , ij ij ij ij  We define that (28)     i 1,2, ,10, j 1,2, ,25.  

means the war, conflict and cold violence among the refugee-exporting countries i and  0 Wa ( ) v Wa the refugees receiving countries j, the preset value of is 0. And for , if a lot ij ij , otherwise  ( ) v ( ) v Wa 1 Wa 0 impact exists in this factor between i and j, then . If there is ij ij        (1) (2) (3) ( ) v ( ) v Wa Wa , Wa , Wa , 1 Wa 1 Wa 0 some , then, , and if all , then, ij ij ij ij ij ij      (1) (2) (3) Wa Wa , Wa , Wa , 0 . ij ij ij ij We using the transfer matrix in task 4, like the foll          ' ' ' f Hp , Wa f Hp , Wa f Hp , Wa 11 11 12 12 13 13            ' ' ' f Hp , Wa f Hp , Wa f Hp , Wa     ''   ''   21 21 22 22 2 v 2 v '  (29) Hp f Hp Wa , ij ij       ij          ' ' ' f Hp , Wa f Hp , Wa f Hp , Wa     v 1 v 1 v 2 v 3 vv vv ,  Wa ,    ' , Wa    ' ' 0 1 Among them, if f Hp , Wa Hp , if f Hp Wa 0 . ij ij ij ij ij ij ij

We define that the number of refugees in receiving country j who come from exporting     PK i , 1,2, ,10; j 1,2, 25. country i is . ij

So, the amount of refugees which would be resettlement is

10 25   .                                                      (30) Wa PK ij ij   i 1 j 1

   Pd 1,2, 10; j 1,2, 25. The pressure between the two exporting countries is: ij

Then we can lead to conclusion:

     1 2    Pd Wa pd , pd ,  ij ij ij ij (31)      i 1,2, ,10; j 1,2, ,25.

 v pd among this means the connections of economic and diplomacy. ij

With the help of MATLAB, we get the two figures below.

15 12 10 10 8 Influence Influence 6 5 4 2 0 0 10 10 10 10 8 8 5 5 6 6 4 4 2 2 0 0 0 0 Policy Policy Space Country Resource

The comparison of the two figures indicates that our model fit the occurrence of exogenous events by the large, and if we adjust some parameters in our model, it will solve the problem more perfectly.

Task 6: Scalability In our initial model, we have considered the factor of the size of refugee, so if the size of refugees is enlarged, our model can be satisfied overall. But if this happens, the size of refugees will become the major subject of consideration. Therefore, each refugee-receiving country’s saturability of receiving refugee will be correspondingly increase to an extreme value. And for refugees-exporting country, its economic strength will not change much in a short time, so the corresponding inputs for each refugee will inevitably reduce .

In order to improve our model’s ability to deal with this situation of large-scale refugee, we need to increase the corresponding control element on the basis of the original. And most important of which is the model of transportation for the refugee to transfer, and the basic

living security for refugee in the destination of transfer, besides the relationships with local residents. Because on the basis of existing public infrastructure, in order to meet the requirements of the transfer of refugees on a larger scale, we must consider transportation infrastructure.

    We define that Tr i , 1,2, ,10, j 1,2, 25. ,which denote the amount of traffic form ij the refugee-exporting country(i) to the refugee-receiving country(j),that is how many refugees that it can meet transferring from the refugee-exporting country(i) to the refugee-     receiving country(j).Also defining Ls i , 1,2, ,10, j 1,2, 25. which denote the basic ij livelihood of refugees than refugee-receiving country(j) can provide to the refugee-exporting country(i),that is how many refugees that the refugee-receiving country(j) can meet the basic livelihood for the refugee-export country. Define the conflict factor of the refugees with the       Cf i , 1,2, ,10, j 1,2, 25. among them 0 Cf 1 local residents .The greater the ij ij conflict factor the refugees with the local residents, the greater probability of conflict between the refugees and the local residents. And then the greater probability of conflict between the refugees and the local residents, the difficult that the refugee-receiving country(j) receive the refugees from the refugee-exploring country(i). So here planning the transfer route of the refugee rationally and making full use of the existing transport resources are becoming particularly important. In this case the competition for transfer of refugee is bound to produce, even conflict will be happened[11].

Finally, we define the existing number of refugees of refugee-exporting country(i) as Pn i   i i   , 1,2, ,10 ,the existing transportation resources available as Re , 1,2, ,10 ,the i Cp i   , 1,2, ,10 probability of conflict between refugees as .In this case: i

       Cp Pn Re i i i i   (32)  i 1,2, ,10. 

i denote the the original quality of the citizens and nationals relations of Among them, refugee-exportING country(i).

Considering the threshold of time, we believe that to ensure the refugees to transfer before the collapse of the body or psychological breakdown is a threshold of time in this case. Of course, in order to control this threshold of time, we need to keep refugees psychological counseling and education, and arrange adequate medical resources to protect the basic medical needs of the refugees, and to strengthen their pease with the local population and refugees in distress with local ideas.

After analyzing the scalability of our model, we get the results that the stabilization change with the expansion of  the scale.

80

70

frequency distribution of degree value 60

50

40

30

20

10

0 0 5 10 15 20 25 30 35 40 45 50 degree value of node

It’s clear that our model is in point when the scale is less than then times, but when the scale is to 15 times, the stabilization is reduced to some extent.

Stability and Sensitivity

Judging from the overall effect of our model, it is not only fit for the environment and area mentioned in the paper but also suited to most fields related to refugees, that is, our model has relatively wide range of applicability. After building refugees transfer model and the relationship of refugee-receiving country and refugee-exporting country referring the data of the two fields, we use them to study the quantities of the relationships and the influence of the evaluation objects, and the results turn out to be reasonable. So our model is practical and reliable.

Moreover, our model doesn’t depend on some certain data. As what is shown in Task 4, when the original data changes, the result of our model changes to a new one corresponding to reality. Regardless of we add some data into the model or remove some out, the results of the model will not have large fluctuations, which indicates the good stability and weak sensitivity of our model.

According to the assumption, we do not take time of preparation for the transfer into account. However, the time of preparation for the transfer has effect on both of the refugee- receiving countries and the refugee-exporting countries. In order to test the sensitivity of our model, we decided to take time of preparation for the transfer as a criterion and add it into our model. Let it to be the time of preparation for the transfer of refugee-exporting country.

it as a new criterion, we change other criterion’s weight and calculate the weighted Taking incidence degree of each author again. From our point of view on the new result, although every refugee-exporting country weighted incidence degree changes a little after adding the time of preparation for the transfer, the change of their relative influence is rather small, indicating that our model has good sensitivity.

Strengths

After building the refugees transfer model, we calculate the influence of each of the evaluation object. Further, in order to ensure the stability of the model, we circulate the calculation process and weigh every evaluation object according to the weighted incidence degree determined. Then we use our model to evaluate all the evaluation objects again, thus giving the effective strategy of transfer.

When analyzing of the transfer of the refugees, we promote the model to different fields rather than keep it in one area so that the model is endowed with higher reliability and wider range of applications. Besides, after establishing the refugees transfer model, we solve the problems from different perspectives, thus giving a full description of our model from other points of view.

Weaknesses

In terms of statistics of data, sometimes it is not accurate enough in our model due to the limitations of resources and lack of statistical techniques, so there may be errors in the result.

Since there are many evaluation objects in our refugees transfer model, the transfer diagram would be rather disordered and difficult to study if all the evaluation objects are included in the refugees transfer model diagram. So we give schematic diagrams and uncompleted diagrams when analyzing as auxiliary description.

When discussing the scalability of the refugees transfer model, we find the number of the refugees is big while the cooperation between them is relatively little. As a consequence, the results of many evaluation objects are close under the evaluation index set in our model, lowering the persuasion of the results of our model.
