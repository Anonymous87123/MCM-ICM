MCM/ICM

Summary Sheet

(Your team's summary should be included as the first page of your electronic submission.)

Analysis of Society’s Information Networks

With the development of technology, the situation of information flow becomes more complicated which has aroused widely concerns. In this paper, we establish a double-layer complex network model to measure the evolution and influence in society’s information networks.

In our double-layered complex network model, the inner layer is to analyze the situation of the information flow among a region. We specially take several factors such as inherent value of information, the media effect and personal subjective emotions into account to quantify the attributes of node and side. Optimizing the AsIC Model, we establish point to point model to simulate the flow of information in the network. In the outer layer, Based on the Reaction-Diffusion Model, we establish a global network model to correct the formulas of propagation probability and propagation delay by taking the distance factor into consideration.

Based on our constructed model, with the combination of the inherent value of the information and the efficiency of information flow, we first give out the method of qualifying news. According to the different condition of media usage, we obtain the proportion of different media in different areas based on regression analysis. Compared the simulation of propagation ratio in our network with the actual market share of a certain media, we find that the relative error is less than 10%. Based on our collecting data, we predict that the propagation probability will increase rapidly while the propagation delay will decrease around the year 2050. Meanwhile, the significance of inherent value of information will depress.

Later, based on Bounded Confidence Model, we establish an interaction model to analyze factors which influence the public interest and opinion through information networks. As a result, we get distribution function of public opinion to observe the change of public opinion. Through a piece of specific information, we find the public opinion changes rapidly in the beginning and finally into the stable state. Next, we analyze the influence of several factors in spreading information and public opinion. We get diagram after calculation to show the trend. For example, the propagation probability and change rate of opinion are proportional to information value while propagation delay is opposite.

Meanwhile, we adopt sensitivity analysis on different elements. We conclude that the model is more sensitive to Authority, later comes Influence, Activity and Willing.

1. Introduction

1.1 Background

Nowadays, information is spread quickly in our daily life. Due to the development of technology, no matter the big events or the trivia, people have access to information quickly and conveniently. As a result, the information garbage is everywhere which influences our life. In order to manage and track the flow of information, people raise awareness of the importance of establishing a society information network.

Interested in information communication situation of social network, several methods have been adopted to describe it. Most models supposed that information is spread according to time sequence. For example, Independent Cascade Model[1] regards that propagation probability is same among nodes all the time which has no memory. Meanwhile, Linear threshold model[2] concentrates on cumulative probability which reflects the accepted ability of receiver. However, these models ignore such factors:

 Attributes of nodes such as personal interests.  Influence of inherent value of information in propagation.  Propagation process is not synchronous.

Therefore, there is an urgent need for a complete scientific model. Based on it, we establish a double-layer complex network.

1.2 Our work

To further present our solutions, we arrange our paper as follow.

 In section 2, we give out the reliable assumptions to simplify the model.  In section 3, the double-layer network is constructed to analyze and forecast the information flow. The inner layer analyzes the information flow among a region. While the outer layer analyze the flow from region to region. Meanwhile, the sensitivity analysis is given out to validate our model.  In section 4, we apply our model to solve a series of problem, such as qualification of news, prediction of information flow today and around the year 2050. Next, we establish a model to analyze the factors to influence the public interest and opinion. Later, we analyze the influence of different indexes in Spreading Information and Public Opinion.  At last, we discuss the strengths and weaknesses of our model in detail.

2. Assumptions

 The data we found is authentic and reliable.  No invention of media in the time for prediction. That is to say, people use the same media as today, just the proportion of media changes.  Ignore the firewall among countries which restrains the spread of information. The information in the our network is not secret.  Due to the difference of development level is relatively little in a small area, we ignore the difference in media usage from a statistical point of view.  To simplify the model, we only consider six media to spread information which are newspaper, telegraph, radio, television, the Internet and mobile phone.  The node spread the same message only once. That is to say，the in-degree of a node is no more than 1.

3. Task 1: Establish a Double-layer Complex Network

3.1 Frame

A large amount of factors ought to take into account to quantify the flow of information. For example, due to the difference in development level among countries, the way and speed of flow must be different. Also, with the Internet technology become more sophisticated, each person plays a more and more important role in spreading information instead of original media such as newspaper and television, which the objective factors such as personal interests should be taken into consideration.

Based on above analysis, we can see that a simple network cannot reflect the whole situation of the flow of information well. As a result, a complex network with multi-layers, whose layers have a certain interactions and independence, seems to be more reasonable.

Therefore, we come up with a double-layered network, global information network and point to point information network, which belongs to a complex network, to reflect the information flow more specifically.

The structure of our double-layer complex network is shown in Figure 1.

The blue dots represent each person and small circle represents a region. The directed line represents the direction of information flow. The figure vividly indicates that the information originates from a node(source), then spread quickly over a region and at last spread the whole world. The internal and external factors which influence the information flow is analyzed in detail in next two sections.

3.2 Inner Layer: Information Flow over a Region

The process of information propagation can be divided into massive point to point cases. Each case has three entities: sender(S), receiver(R) and content(C). Figure 2 shows the relationship.

The information spread from sender to receiver, each spread case carries a piece of information.

3.2.1 Index Extraction

In order to describe the flow of information specifically, we choose Twitter as an example. Based on the AsIC Model, to improve the accuracy of our model, we take the inherent value of information, the media effect and personal subjective emotions into consideration and give five indexes to analyze the information flow: Communication Media Effect, Sender Characteristic, Receiver Characteristic, Content Characteristic, Relation between Sender and Receiver. Suppose that node u as a sender, node v as a receiver.

)  Communication Media Characteristic ( m

From a historical perspective, the communication media change a lot. From newspaper, and radio in the early time to television, Internet, mobile phone and many other media nowadays. Information tends to spread more quickly and wide. Due to the difference in social developments, mainstream media of different regions varies a lot. Based on six media (newspaper, telegraph, radio, television, Internet and mobile phone), communication medium

is calculated as follows: effect m

    ( i N , TEL , R , TV , I , M ) (1) m i i i

When N,TEL,R,TV,I is short for six media, newspaper, telegraph, radio, television the idenotes the market share of ith medium Internet and mobile phone respectively; where idenotes corresponding effect on spreading communication such as propagation speed and and scope.

Base on the Analytic Hierarchy Process[3], we train the collected data and obtain the final weights as follows. The result has been approximated in order to simplify calculation.

iand  is constant which represent the Meanwhile, in a specific area we assume that m

average level. The weight of different media is listed in Table 1.

Medium Weight Medium Weight Newspaper 1 Television 2.5 Telegraphy 0.5 Internet 3 Radio 2 Mobile phone 3.5

s)  Sender Characteristic (

 Influence(F): Influence shows the importance degree of a node. It should be:

  InF ( u ) lg( RT )1 (2)

Where RT denotes the total number of forwarding times of a node.  Authority(A): It is defined as the ratio of in-degree divides out-degree which is calculated as follows:

FO   A (u) lg( )1 (3) FR Where FO denotes the number of fans while FR denotes the number of idol.  Activity(Ac):

PO   Ac ( u ) lg( )1 (4) D Where PO denotes total number of messages the user has been published. D denotes the number of the user’s active days.

We take normalized form membership functions for each index so that values of all the factors can be constrained between 0 and 1.The normalization is shown as follows:

 x min { x } i j   1 j n  ' x (5) i  max { x } min { x } j j     1 j n 1 j n

' ix and ix respectively denotes the original value and the value after standar- Where

dization.

)  Receiver Characteristic( R

 Willing(W): The value of willing indicates the possible trend for receivers to spr- ead the information(v) is calculated as follows:

R   W ( v ) lg( )1 (6) P Where R denotes the number of retweet times. P denotes the number of original messages.

, iy . In the same way, normalize the index as c)  Content Characteristic (

Inherent value of content plays an important role in the information flow. For example, the funnier or more important message tends to spread more quickly. To evaluate such abstract idea, we quantify it for two aspects: the value of information content and the quality of presentation.

Luckily, the article in Journal of Information Engineering University[4] determines 5 indicators for the value of information content and 5 indicators for the quality of presentation. Specific indexes and their weights are shown in Table 2.

General  indicator Specific indicator Weight Authenticity 0.318 Importance 0.174 Inherent value(0.7) Timeliness 0.247 Target 0.102 Confidentiality 0.159 Clear scheme 0.203 Careful thinking 0.063 Quality of presentation(0.3) Accurate description 0.299 Concise expression 0.232 Comprehensive factors 0.203

We give out general formulas to calculate the above two aspects below:

 5     (7) value i i i 1  10     (8) qua i i i 6

       7.0 3.0 (9) c value qua denotes the weight of above 10 indicators respectively. i denotes the value Where i  of the corresponding index, which arranges from 0 to 9. denotes the value of value  information content and denotes the quality of presentation. pre   Relation between Sender and Receiver ( ) S, R

 Interest similarity(Si): The message the user published indicates his or her interests which plays an important role in spreading information. TF-IDF model[5] is adopted to information retrieval and data mining. Sim-i(u,v) is:

 P Q  Si ( u , v ) (10)  P Q

where P and Q respectively file vector of uses u and v.  Structural similarity(Ss):It illustrates the similarity of circle of friends among users. The Jaccard Distance[6] is applied to the calculation:

 N ( u ) N ( v )  Ss ( u , v ) (11)  N ( u ) N ( v )

iv . N ( iv ) Where denotes the neighboring nodes of node CL ( u , v )  Closeness( ):When the message contains information of receiver, it will be

CL ( u , v ) spread more easily. Define as follows:

 ,1 when the message of u mentions v  CL ( u , v )  (12) ,0 on the contrary 

3.2.2 Information flow between two nodes

) and side vector Based on above analysis, we establish eigenvector of node vector ( n e) .These two vectors are shown as follows: (   T     (13) n S R C   (14) e S , R To obtain the propagation probability, fundamentally function is calculated as follows:

        T T f ( u , v , c ) k (15) 1 m 1 n 2 e

denotes weight of nodes’ characteristic, denotes weight is a constant, Where 1 2 m of sides’ characteristic. The weight represents how corresponding characteristic influence in 1k is the weight. propagation probability.

Based on Bayesian logistic function[7],the propagation probability is calculated:

1  p ( u , v , c ) (16)   1 In ( f ( u , v , c ))

In the same way, propagation delay is calculated as follows:

         T T ( u , v , c ) k (17) 2 m 1 n 2 e

and respectively denotes weight of nodes and sides  Where is constant, 1 2 m 2k is the weight. characteristics.

3.2.3 Coefficient calculation

 and i(i=1,2), maximum likelihood estimate ik , In order to calculate the coefficient i theory[8] is adopted as follows.

Taking time decay factor into account, the propagation probability decreases as time goes by. Accumulated propagation probability from node u to node v is defined as follows:

t   v F (( v , t (|) u , t )) f ( u , v , c ) dt (18) v u t u  ti ( i u , v ) Where denotes the time when node i spread the information.

S (( v , t (|) u , t )) Define as the probability of which node u will not spread the v u vt . information to v before time  S (( v , t (|) u , t )) 1 - F (( v , t (|) u , t )) (19) v u v u D  k {( v , t ),..., ( v , t )} Determine a set to represents all the node and its spreading i i n n    k k Q {( v , t ) D , t t } time. And the set denotes the nodes which spread information i i i par (v ) before time t. is defined as the information source of node v, that is to say, the par (v ) information spread from to v.

kc is calculated as follows: The propagation of a piece of information     k f ( c ) F (( v , t (|) u , t )) S (( v , t (|) u , t )) (20) v u v u k   ( v , t ) Q ( v \) par ( v ) v C  1 2 nc { c , c ,..., } So the propagation probability of all pieces of information in set can be obtained in the following formula:

  kc f ( C ) f ( ) (21)   1 k n f (C ) To get the larger value of , we set the object function:

 min lg f ( C ) (22)

 and ik , Train data through computer, we can finally obtain the value of coefficient i i(i=1,2).

3.3 Outer Layer: Information Flow from Region to Region

As analyzed above, the development level is unbalanced on the Earth which influences the flow of information, so the nodes we choose must be representative. To simplify the model, we choose GDP per capita as the criteria, with data from the CJDBY.net[9], which is shown in Figure 3.

We can see that each of which has obvious difference GDP per capita is signed by a certain color. Apparently, the GDP per capita of America, Canada, Northern Europe and Australia(area with color of purple)is four times as big as the world’s average level. On the contrary, the one of area with dark blue color is relative low. According to development level and geography, we choose seven typical countries in Figure 4:America, Brazil, France, Congo, Russia, China and Austria.

In order to investigate the flow of information among nodes, we detail this phenomenon by applying the mechanism of two-dimensional reaction-diffusion model(R-D equation).

  f ( , ) A scalar field and its gradient, whose magnitude is the maximum rate of change

of f per unit length of the coordinate space at the given point, could be described below in

polar coordinate system:

  f 1 f       V [ f ( , )] e e （23）       

  f ( , ) Therefore, this scalar field will transfer into a vector field V after derogating

gradient. For a source flow, all the streamlines are straight lines emanating from a central point, as shown in Figure 5. Obviously, we see that the components in the radial and

/   /       f f f / 0 tangential directions are and , respectively, where .

According to the mechanism of reaction-diffusion model, the divergence of every

point in this vector field V can be obtained easily :

 f    div div ( f ) div ( e )    (24)     2 1 f 1 f f      ( )           2

(  ( div ) ) Where : denotes divergence while denotes gradient.

f /   2 2 The second part in above equation, that is, , has little impacts on the final value. Here, for the convenience of calculations, we overlook this part.

1 f  d i v ( ) (25) 

And final conclusion could be draw that divergence of gradient of a scalar field is inversely proportional to the radial distance.

Considering the fact that the further distance leads to weaker propagation of information, so we only take the link between a node and its neighboring node into account. Figure 4 shows the nodes chosen and its direct connect. The yellow line represents international information flow.

)is a constant From above analysis, we assume that Communication Media Effect ( m among a country which ignores the difference of development level among the range of countries. Meanwhile, the factor of distance is neglected in point to point information network as well.

To full present the reality, based on above model, we taken into distance between two  into account. It is a common sense that propagation of countries and difference of m information between points is inversely proportional to their distance while the propagation delay is on the contrary. And the information flow is limited to relatively backward country.

between two countries and choose the lower value of into calculation. Compare the m m According to above assumption, together with the mechanism of reaction- diffsion model[10], we suppose that the propagation of information happens from node u to n  ode v .The propagation probability between u and v can p and propagation delay ex ex be described as:

 p ( u , v , c )  p k  ex 1 d (26) uv       k ( u , v , c ) d ex 2 uv

denotes the distance from node u to node v , and d k 1,k Where : denotes the uv 2 weight respectively.

3.4 Information Flow Situation

We have obtained the propagation probability and propagation delay from above analysis. Set up two sets: set K includes the nodes which have spread the information(including the information source) and set N includes all nodes except nodes in set K.

To express the information flow clearly ,there are mainly four steps as follows:

as the information source and the number of all nodes is  Step 1:Suppose the node 1     1  idenotes the spread time from source to node i).  K 0 n 1 m. . ( (n denotes 1 the number of nodes in set K).

     f ( , ) ( , )  Step 2:Calculate the propagation probability and propagation delay i j i j in set K and all their neighboring node in set N. between the node j i     into set K. (is a threshold, usually from 0.5 to 0.6), take node f ( , )  Step 3:If j i j        n  n 1 ( , ) , .Return to Step 2. j i i j   f ( u , v )  Step 4:If there not exists a node v which and the last included node is is the total propagation time, .The conclusion is that n/ m is the total propagation p p ratio.

The blue spots represents the nodes which have spread the information. As shown in the Figure 5,there is only one node in the beginning which is information source. Through the spread of information, as shown in Figure 6, the number of blue spots increases and new blue spots work as new ‘information source’ to spread information.

3.5 Sensitivity Analysis

3.5.1 Change the Value of Index

Based on our constructed model, we extract many indexes as the attributes of node and side. For the purpose of concise writing, we choose two representative indexes for detailed description which represents the attributes of node and side respectively.

(attributes of node) and the interest similarity between the sender and receiver (attributes of side).The blue solid line represents the original trend of willing degree, the dashed lines represent adjusted trends of index; red one matches expanding value of index, while green one matches reducing influence of index.

It is obvious that the total trend of three lines in Figure 13 is all rising, which represents that the propagation ratio is in proportion to willing degree. Increasing the value of willing degree seems to help improve the flow of information.

The results of sensitivity analysis of Si is similar to the one of W. But the trend for Si is smoother which shows that our model is not sensitive to the interest similarity compared to willing degree of receiver.

3.5.2 Remove a Index

To show the different influence degree of different indexes to the flow of information, we choose four indexes: Influence(F), Authority(A), Activity(Ac), Willing(W) as example.

of the case when we remove one of above four indexes.

We can conclude that the lack of Influence index and Willing index leads to increasing the propagation delay time. The difference between the case of lack F and the normal is larger than the case of lack W and the normal, which represents that F is more sensitive to our model than W. In the same way, the lack of Authority leads to decreasing the propagation delay time. Among all these four indexes, model is most sensitive to authority, later comes influence, Activity and Willing.

Meanwhile, the difference is relatively small which indicates the stability of our model.

4. Application and Analysis

After all equations are determined above, our model is final completed. So next, we concentrate on solving relative problems and giving out analysis as well.

4.1 Task 1: Qualification of News

Both the inherent value of the information itself and speed of information are vital to information propagation. News, a form of information which satisfies the law of information propagation, ought to be qualified from above two aspects. The inherent value of news are divided into the value of content and the quality of presentation which we have analyzed above. We will discuss the information flow efficiency in detail as below.

As we have analyzed above, the total propagation delay timeand the total propagation ratio ,which reflects the flow efficiency, can be obtained through computer calculation.

 Quantify the efficiency below: eff    1     (27) eff 2

 (  is negative while is positive. i 2,1 ) Where denotes the weight. i 1 2 In conclusion, the quality of news can be calculated as follows:

       (28) quality 1 eff 2 c

i (   denotes the weight of ith indicator. i 2,1 ) Where denotes information flow eff cdenotes the inherent value which has been analyzed above. efficiency and    For the different situation, we can set different threshold .When ,the quality information can qualified as news.

4.2 Task 2: Predict the Information Communication Situation for Today

The market share of different media is an indicator to quantify the information into 1 in equation(1) and let i  0 communication. Change the weight (i=TEL,R,TV,I,M) N ,which is analyzed in section 4.2. Compared with the to calculate the propagation ratio N N actual market share of newspaper, we come to analyze the error between our model and the reality. The market share forecast of other media is in the same way.

First, we give out the total trend in market share of six media plots as follows based on regression analysis. We choose two representative countries: America and China as study objects.

The specific value of market share of different media is listed in Table 3 and Table 4.

Medium Newspaper Telegraph Radio Television Internet Phone Weigh 0.09 0.01 0.04 0.32 0.27 0.27

Medium Newspaper Telegraph Radio Television Internet Phone Weigh 0.12 0.02 0.07 0.29 0.25 0.25 We can see that the market share of traditional media such as newspaper and radio is descending all the time. On the contrary, the new media such as the Internet and mobile phone occupy more media share.

There are six media and seven regions, for concise writing, we choose the newspaper and the Internet of America for example. We collect data from a discussion paper from communic@tions Management Inc[11]and BBC news[12].

Internet. The blue full line represents the reality and the green dashed line represents the forecast based on the past data. Obviously, the green line is close to the blue one ,with the relative error is under 10%, shows that our model is reliable. The specific error is shown in

Medium True value Forecast Absolute Error Relative Error Newspaper 0.3 0.28 0.02 6.67% Internet 0.773 0.785 0.12 1.55%

 Example

To specify the information communication situation for today, we choose a important world event about the death of Bin Laden, which happens in May 1st, 2011. Based on our model, we calculate information value as the number of 8.3.

In order to reduce the amount of calculation, we choose to calculate the number of propagation nodes in one minute to verify our model. Following are our results.

We obtained that the number of nodes is 89.According to the data from peixun.net[13],we know that there are 80 people re-post the information in Twitter, which is similar to our evaluation. From above example, we validate our model’s reliability.

4.3 Task 3: Predict the situation around the year 2050

There are seven regions, thus, for concise writing, we choose two representative regions, where United States and Congo respectively as our study objects.

4.3.1 Communication networks’ relationships

As time goes on, our society tends to information-overloaded, with more and more useless information around us. With the development of technology and minds changing, it is obviously that the inherent value of information itself decreases while the efficiency of information flow increases. To show the relationship between flow of speed of  c), which have been quantified above, information( ) vs inherent value of information( eff we define the ratio s as follows:

 eff  s (29)  c

time and reaches a plateau around the year 2030, which indicates the popularity rate of the Internet will be high and stable at that moment. The ratio will reach approximately the number of 14 around the year 2050. In the same way, Figure 16 shows trend of ratio changes in Congo, which is different from the one of America. The line declines slowly at first and falls faster in about the year 2020, and finally will reach the number of 30 around the year 2050, which is lower than the one of America. These figures indicate the difference of social development level.

4.3.2 Communication networks’ capacities

According to our constructed model, the total propagation time and the total propagation radioare the two indicators to evaluate networks’ capacities. The data are employed to train the network. Figure 11 and 12 show indicators and  of two countries from the year 1860 to the year 2050 below. We assume that the quantitative value of propagation delay is the number of 1.

delay decreases while propagation probability increases on the contrary. There are two time point in the graph, the first one is around the year 1870 when the newspaper come to the world, which improve the spread of information extremely. The second one is the year around 2000 because of the rapid development of Internet technology. These two graphs indicate the history of media and its importance in spreading information. Figure 18 indicates the capacities in Congo changes in the same way.

To sum up, the global network capacity increases rapidly before the year 2050 and the developed countries reach a plateau while developing countries are still in their developing period.

4.4 Task 4: Influence in Public Interest and Opinion

4.4.1 Foundation of Model

) ,which represents the interest for In above analysis, we assume that Receiver Effect ( R an individual, is a constant of a node. However, the opinion of an individual is not static all the time. It will be influenced by the spread information or the opinion of its acquaintance and other factors. With the evolution of opinion of each individual, public interest and opinion can be obtained. To simplify the model, we only assume the opinion of an individual is influenced by the spread information.

Based on the Bounded Confidence Model[14] ,we establish the public interest and opinion (  si (t ) si t ) [ ]1,0 change model as follows. Define the opinion of node i in time t is , .When:

  si ( t ) 5.0 si ( t ) 5.0 represents neutral point of view, represents positive opinion, with the value more close to the number of 1,the opinion is more positive. The same way, represents negative opinion. Threshold  is the maximum value for two nodes’  si ( t ) 5.0    s ( t ) s ( t ) opinion differences to spread information. That is to say, when ,information i j can be spread.

The changes in opinion are shown in the following formula:

      s ( t )1 s ( t ) [( s ( t ) s ( t )]  i i j i (30)       s ( t )1 s ( t ) [( s ( t ) s ( t )] j j i j

Where is the weight. Usually,   [ ]1,0 .

Based on our double-layer network, with regard task 4,we only take the Internet as si (t ) media. When the information spread in our network, of each node i can be recorded. By as means of statistical methods, we can finally get the average public interest and opinion o follows:

 s ( t ) i    i M ( t ) (31) o m Where m denotes the total number of nodes in our network. Set M includes all the nodes

 can reflect the public opinion comprehensively. in our network so that the value of o

  ( t ) 0 The change rate of public opinion is defined as .  t

 Example

To simplify how public interest and opinion changed through information networks, we choose a important event which is about the China helped people in Africa combat Ebola

 change is virus.to spread in the network. The trend for he public interest and opinion o

shown as follows:

is From above picture, we come to a conclusion that before the information spread, o

close to 0.5 which represents that the public opinion is neutral. Later in the early time of

 tends information spread, the changes of public opinion are extreme. As the time goes by, o

to a constant(the number of 0.65)which represents the average public opinion.

4.4.2 Suggestions

Based on our constructed model above, we can give some suggestions to the government or relevant departments to manage the public interest and opinion on the Internet effectively.  Filter bad or false information when necessary. That is to say, reduce the value of threshold to restrain the spread.  The content of news information ought to be carefully selected. Based on our model to qualify news in section 4.3, we can increases the value of threshold  to guarantee the quality of news.  Strengthen the construction of mainstream news website. Use mainstream voice to influence public opinion, which these websites are more credible and attracts more people.  Besides, the Internet ought to actively interact with the traditional news media to manage public opinion.

4.5 Task 5: Factors Influence in Spreading Information and Public Opinion

With regard to task 5, we have analyzed information value, people’s initial opinion and bias, form of the message or its source, and the topology or strength of the information network in a region, country, or worldwide from our constructed model. For concise writing, we only analyze how information value spread information and influence public opinion.

4.5.1 Influence in Spreading Information

We have concluded that propagation probability and propagation delay are two indicators to show the information flow. In order to better illustrate the difference among countries, we choose America and China for example. Figure 20 and 21 show these two indicators’ change trend with time.

Horizontal axis is the information value, with its value ranges from 0 to 9 which have analyzed above. Propagation probability increases results from the increasing value of information. On the contrary, propagation delay decreases. These two graphs illustrates that the information with higher value can be spread more quickly and wide. Meanwhile, the propagation probability of China is lower than the one of America while the situation of propagation delay is on the contrary.

4.5.2 Influence in Public Opinion

  ( t ) 0 The value of represents the influence in public opinion. The higher value  t indicates that the public opinion can be influenced more easily. Figure 22 shows the change of its value over time.

As is shown in the picture, we can conclude that the information with higher value can change the public opinion more easily, which has a greater influence in public opinion. Compare China with America, we can find that the change rate of America is relative higher than the one of China, mainly due to the different proportion of media and development level.

5. Strengths and Weaknesses

5.1 Strengths

 The model combines several attributes of side and code such as the inherent value of information, personal interests, changes of media, which reflects the reality well.

Considering seven regions divided from the whole world into our double-layer network,  our model is already comprehensive to some extent.

5.2 Weaknesses

 The model is applied to well-constructed network such as Facebook or Twitter. It cannot reflect the random event very well.  Due to our complex model and amounts of indicators to calculate, it is inevitable to increase calculated amount which decreases the efficiency of network.  Because of several factors are not considered and the lack of data, our model are not enough to indicate the accurate situation which has a risk of error.
