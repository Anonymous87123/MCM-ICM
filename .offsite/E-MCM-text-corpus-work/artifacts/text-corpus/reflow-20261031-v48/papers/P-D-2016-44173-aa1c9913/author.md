For ofﬁce use only For ofﬁce use only

T1 F1 T2 F2 T3 F3 Problem Chosen T4 F4

2016 Mathematical Contest in Modeling (MCM) Summary Sheet

How to Understand the Information The ﬂow of information has never been as easy or wide-ranging as it is today. This paper proposes some models to explore the relationship between speed/ﬂow of information with inherent value of information.

First,to explore information ﬂow, we build up a SIIR model which takes the me- dia inﬂuence into consideration. This model is developed from the classical SIR model.We introduce the concept of hot transmission nodes to highlight the impact of media. We demonstrate our design with American media data. The results show that our model has a signiﬁcant performance in validating predicted values of the characteristics of information network in 2050.

Second,the information ﬁltering can be regarded as a classiﬁcation problem. We design a radial basis function network to implement the information ﬁltering. In order to solve sample noises and improve the computing performance,we decide to use K-means algorithm and RLS algorithm to implement our RBF network. We demonstrate our network in online news dataset ,with an training accuracy of 75.1%,and testing accuracy of 74.3%.we are satisﬁed that the accuracy rate with information ﬁltering as news.

Third, We have only considered the social network in the Internet and build a social network SIR(SN-SIR) model to explore the problem-how public interest and opin- ion can be changed through network.It simulates in the standard dataset: Facebook social network dataset .By analyzing the factors which can implement our result- s,we can make a plan to determinate information propagation. Then,we take infor- mation values ,people ˛a´rs initial opinion and bias, form of the message or its source, and topology or other reasons into account and propose a detailed scheme.

Finally, effects of external factors are considered in our models.And we analyze the stability and sensitively of our models. Although there are some weakness in our models,the results still demonstrate that our model can undergo disturbance in certain extent.

1 Introduction

1.1 Background

Broadly speaking, information is one of the important ways for us to perceive the outside world. Today it spreads quickly in tech-connected communication network. Sometimes it is due to the information ﬁnding its way to inﬂuential or central network nodes that accelerate its spread through social media. Our prevailing premise is that this cultural characteristic to share information (both serious and trivial) has always been three. At present, information propa- gation is exposed explosive growth.Beacause our social networks and medium are more and more complex.Without effective ways to solve these problems ,it will ﬁnally cause information propagation is more and more difﬁcult to umderstand.Hence,our work has its unprecedented signiﬁcance in world nowadays.

1.2 Our Work

This paper propose some models to explore the relationship between speed/ﬂow of informa- tion with inherent value of information. The Dilemma:

• An adaptive ﬂow model is established with the consideration of the complex network changes.

• Make use of the existing parameters to ﬁlter the information reasonably.

• Reasonable analysis of inﬂuencing factors in the process of information transmission.

The Approach:

• FirstˇcˇnTo explore information ﬂow, we build up a SIIR model which takes the special fea- tures if media inﬂuence into consideration. This model is developed from classical SIR model.

• The Results show that our model has a signiﬁcant performance in validate the value of prediction with real value. And then ,we predict the rate of daily contact in 2050.

• Information ﬁltering is regarded as classiﬁcation problem. we design a radial basis func- tion network to implement information ﬁltering. In order to solve sample noise and com- puting performance, we decide to use K-means algorithm and RLS algorithm to imple- ment our RBF network.

• We have only considered the social network in the Internet and build a social network SIR(SN-SIR) to explore the problem ˛a´s how public interest an opinion can be changed through network ˛a´s.

• We can make a plan to determinate information propagation. Then ,we take information value ,people ˛a´rs initial opinion and bias, form of the message or its source, and topology or other reasons into account and build a detailed scheme.

2 Assumptions

The accuracy of our models rely on certain key, simplifying assumptions. These assumptions are listed below:

• Do not consider factors such as natural birth,death,and population mobility.The total population keeps as a constant K.

• Infected individuals once contact with susceptible individuals,Infected individuals change to susceptible individuals at a certain probability.

• At a certain time,The number of individuals per unit time removing from the infected individuals is proportional to the number of patients.

• The number of media is relatively ﬁxed in the same period.

Under the above and basic assumptions, we can set out to construct our model.

3 A SIIR Model of Information Flow

Information is created by the social network users and transmits in the entire network.The result of transmission is that the receiver of the information translates into the transmitter and disseminate the information to others,or translates to the recovered one and does not transmit to others.Obviously, this transmission way is similar with the way Infectious diseases spread in the crowd. Based on the analysis of social network structure,we introduce the hot transmission node into network,and proposes an information transmission model based on the improved SIR model [1],which is simulated with the data-based Facebook social network.

3.1 Social Network Information Dissemination

3.1.1 Social Network Information Dissemination Characteristics

In this section,we propose a to explore a general model of information ﬂow problems, which is not subjected to the limitations of the times and mediums of communication.

The total number of user nodes in social networks is denoted as N.The network is assumed to be an undirected graph and each node in the network may be in one of three states: susceptible(s), infected(i), or recovered(r).Nodes in state i have received the message and have the ability to transmit it.Nodes in state s have not received the message and have the possibility to receive it.Nodes in state r have received the message and will not transmit it any more.

There are a variety of mediums of communication,such as newspapers,televisions,the Inter- net and so on.Different mediums have different ability of transmission,but all of these medi- ums owe stronger ability than human beings.We consider media as the hot transmission n- odes.Their contact rate is denoted as λ1. Ordinary users in networks are considered as ordinary nodes.Their contact rate is denoted as λ2.

The laws of Information dissemination of social networks with hot transmission nodes are as below:[2] • Hot transmission nodes contact with other nodes with the contact rate x1,while ordinary nodes with the contact rate λ2.

• After nodes in state s received the information from nodes in state i,they change into recovered nodes in a probability of µ,and into ordinary infected nodes in a probability of 1 −µ.

• With the propagation of information,the proportion of three types of nodes will tend to be stable.

The schematic diagram of information dissemination of social networks with hot transmis- sion nodes as shown in Figure 1, the solid line shows the information transmission between two points.

3.1.2 Model Building

According to the characteristics of the transmission above,we can get the information transmis- sion of atrioventricular model structure diagrams, as shown in Figure 1.

i0 is the proportion of hot transmission nodes in networks,which is usually ﬁxed.i(t) is the proportion of ordinary infected nodes in the time of t,which consists of i1(t),the ordinary in- fected nodes generated by hot transmission nodes,and i2(t),the ordinary nodes infected nodes generated by ordinary infected nodes.λ1 is the contact rate of hot transmission nodes,while λ2 is the contact rate of ordinary infected nodes.r(t) is the proportion of nodes in state r,µ is the rate of Immune probability.[3] We can get the model as follows:

ds(t)  = −λ1i0s(t) −λ2s(t)i(t) dt        di(t)  = µ[λ1i0s(t) + λ2s(t)i(t)]   dt        dr(t) = (1 −µ)[λ1i0s(t) + λ2s(t)i(t)] (1) dt       s(t) + i(t) + i0 + r(t) = 1           i0 = i10, i(0) = i20, s(0) = s0, r(0) = r0 

3.2 Calculating and Simplifying the Model

3.2.1 The Model Results

Take the United States as an example,we obtain the statistical data of the circulation of news- papers, and numbers of users of radio, television, mobile phone and the Internet in different years.After analysis,we calculate the daily contact ratio of the ﬁve media,λi.We calculated the proportion of people contact with the different media group in all the population in the US. at that time.

N X λ1 = λiPi (2) i=1

We choose ﬁve years:1850,1930,1960,1996,2012,to calculate the model,and get the pictures of the change trend of the proportion of three kinds of nodes.

100 100 90 90 Susceptible individuals Susceptible individuals Recovered individuals Recovered individuals 80 80 Infected individuals Infected individuals 70 70 the rate of three node the rate of three node 60 60 X: 66.04 X: 83.88 Y: 50.07 Y: 50.02 50 50 40 40 30 30 20 20 X: 72.35 X: 54.55 Y: 10.06 Y: 10.08 10 10 0 0 0 10 20 30 40 50 60 70 80 90 100 0 10 20 30 40 50 60 70 80 90 100 time/days time/days

100 100 Susceptible individuals 90 90 Susceptible individuals Recovered individuals Recovered individuals 80 80 Infected individuals Infected individuals 70 70 the rate of three node the rate of three node 60 60 X: 62.19 X: 59.29 Y: 50.3 Y: 50.06 50 50 40 40 30 30 20 20 X: 47.75 X: 50.62 Y: 10.05 Y: 9.897 10 10 0 0 0 10 20 30 40 50 60 70 80 90 100 0 10 20 30 40 50 60 70 80 90 100 time/days time/days

The simulation results show that,the number of individuals who have known the informa- tion is increasing,and the proportion of susceptible nodes is decreasing over time.If the time is long enough, information can spread throughout the entire network.By contrast,we can know that the average contact rate of infected nodes increases gradually,which shortens the period of information dissemination and expands the scope of information dissemination.

In conclusion,the improved information transmission model can reveal the inherent law of information transmission in social network more accurately.

100 90 Susceptible individuals Recovered individuals 80 Infected individuals 70 the rate of three node 60 X: 62.08 Y: 50.3 50 40 30 20 X: 50.74 Y: 10.3 10 0 0 10 20 30 40 50 60 70 80 90 100 time/days

3.2.2 Rationality validation And Sensitivity analysis

In order to illustrate the model better , we investigate Facebook data and get the latest Facebook data on DMR website.Total number of Facebook daily active users is 1038 billionˇcˇn26.7 per- cent of the Internet users in the US. that clicked a Facebook share button on blog posts they enjoyed.General users has 245 friends in average.Model parameters can be determined by the conditions and the initial value is as follows: λ1 = 1000, λ2 = 245, µ = 73.3%, i0 = 5 × 10 −7, i(0) = 0, s0 = 1, r(0) = 0, we use Matlab to solve the Differential equations and get the ﬁgures of the change trend of the proportion of three kinds of nodes in Facebook.It can be seen that:

More than half of the users has received the message In less than 7 days.After ten days, about 70% of the users in the network have get the message.Eventually the ratios of the number of three kinds of nodes achieve stable.

The Inﬂuence of Parameters on the Information Dissemination 1.Contact rates of hot transmission nodes By changing the daily contact rate of hot transmission nodes in social network,we can ﬁnd the result in Figure5,After contrast,we know that with the increase of average daily contact rate of transmission nodes,the period of information dissemination has been shortened and the scope of information dissemination has been expanded.

100 Susceptible individuals Recovered individuals Infected individuals 80

60 X: 7.155 the rate of three node Y: 49.99

40

20 X: 6.131 Y: 10.09

0

−20 0 5 10 15 20 time/days 100 100 100 Susceptible individuals Susceptible individuals Susceptible individuals Recovered individuals Recovered individuals Recovered individuals Infected individuals Infected individuals Infected individuals 80 80 80

60 60 60 X: 7.825 X: 7.542 X: 6.928 the rate of three node the rate of three node the rate of three node Y: 50.19 Y: 50.07 Y: 50.05

40 40 40

20 20 20 X: 6.516 X: 5.902 Y: 10.04 Y: 10.03

0 0 0

−20 −20 −20 0 5 10 15 20 0 5 10 15 20 0 5 10 15 20 time/days time/days time/days

100 100 Susceptible individuals Susceptible individuals Recovered individuals Recovered individuals Infected individuals Infected individuals 80 80

60 60 X: 16.29 X: 4.555 the rate of three node the rate of three node Y: 50.4 Y: 50.01

40 40

20 20

0 0

−20 −20 0 10 20 30 40 50 0 5 10 15 20 time/days time/days

2.The Probability of the Immune By changing the probability of the immune,we can ﬁnd the result in pictures as bellow. The probability of the immune can impact the period of information dissemination,too.Reducing the probability of the immune can speed up the information transmission and shorten the pe- riod of information dissemination.

3.3 Prediction

We carry out the multiple regression analysis on data and make predictions,and get general changes of daily contact rate for each media.Figure14

With the changes of The times and the emergence of kinds of media,the proportion of each medium also changes over time.as is shown in Figure15

Considering the tendency of different media and changes of the way people get their news,combining with relevant information and data.We can ﬁnd that:

100 100 Susceptible individuals Susceptible individuals Recovered individuals Recovered individuals Infected individuals Infected individuals 80 80

60 60 the rate of three node the rate of three node X: 11.36 Y: 34.84 40 40

X: 8.459 20 20 Y: 14.84

0 0 X: 5.328 X: 4.541 Y: 0.5121 Y: 0.4047 −20 −20 0 5 10 15 20 0 5 10 15 20 time/days time/days

1.Before the 19th century, the newspaper is the main access to gain news, and around 1950, the radio has a majority of users,.The data changes again in 1980, TV at this time holds the leading position.After that,the number of users of mobile phones, and the Internet is constantly rising.Besides,after 2000, the number rises quickly and clearly, and the Internet and the mobile phone gradually become the main tools to get news and messages in people’s daily lives.

2.Users of newspapers, radio and television have decreased constantly.But in recent years the pace of decline has gradually slowed down.But after 2020, with the popularity of the Internet, the users number will tend to be saturated, although there is still a rising trend, but the rise has slowed.

In the case of 2050, we take the predict data into information ˛a´rs ﬂow model, the situation of the information ﬂow is shown as follows.

When only consider the changes of average daily contact rate of average daily contact rate,we can see that:

100 90 Susceptible individuals 80 Recovered individuals 70 Infected individuals the rate of three node 60 50 40 30 20 10 0 0 20 40 60 80 100 120 time/days

1.Compared with 2012,the speed of news propagation will keep going up in 2050.In less than 40 days,almost half of the people can acquire the news when it happens.While in 2012,nearly half of the people learn a message in 50 days.The speed of information transmission increased by about 25%.

2.The transmission of the message gets into its stride at the 20th day in 2012.While in 2050,the transmission of the message starts at the 10th day.In 2050, by contrast, the begining of the trans- mission will be in advance,which is another sign of increasing of the information transmission speed.

3.In 2012,the spread of information cycle lasts about 60 days,while in 2050,The spread of infor- mation cycle lasts about only 50 days,which means that in the same length of time, the amount of messages people contact will increase.And this portends that information capacity will be constantly increasing,with the development of communication tools .

From 2000,the number of people using social networks has increased,and the contact rate of ordinary nodes has changed,too.Ordinary nodes have more opportunity to change into hot transmission nodes,resulting to the proportion of hot transmission nodes in the whole heat has increased.So we boost the number of hot transmission nodes and the contact rate of ordinary nodes.The model adjusted is as follow:

100 Susceptible individuals Recovered individuals Infected individuals 80

60 the rate of three node 40

20

0

−20 0 10 20 30 40 50 60 70 80 90 100 time/days

Compare two results, the information transmission will accelerate again,and the transmis- sion cycle will shorten again.Owing to this,information will exist in a shorter time, and a lot of information will become a fast-good-type messages,which is a kind of portrayal of real life.

4 A Model of Information Filtering

4.1 Model Description

The purpose of information ﬁltering is to extract the information as news.Essentially, infor- mation ﬁltering is a classiﬁcation problem. We propose a radial basis function network(RBF) model[4]. In order to solve the samples noise and computing performance, we decide to use K-means algorithm and RLS algorithm implement network. We demonstrate our model using online news dataset.

4.2 Hybrid Learning Procedure For Networks

we develop a hybrid learning procedure for RBF networks. First,we use K-means algorithm to train hidden layer. And then, RLS algorithm is checked to train output layer. We call The hybrid learning procedure as “”K-means RLS “”algorithm. The algorithm is divided to three steps:

• Input layer.

The size of input layer is determined by the dimensionality of input vector x, which is denoted by m0.

• Hidden layer.

1. The size of the hidden layer ,m1 is determined by the proposed number of clusters, K. Indeed, the parameter K may by viewed as a degree of freedom under the design- er ˛a´rs control. As such, the parameter K holds the key to the model-selection problem and thereby controls not only the performance, but also computational complexity of network.

2. The cluster mean ˆµj,computed by the K-means algorithm working on the unlabeled

sample xiN i=1 of input vectors, determines the center xj in the Gaussian function φ(·, xj) assigned to the hidden unit j = 1, 2, · · · , k. 3. To simplify the design ,the same width, denoted by σ,is assigned to all the Gaussian functions in accordance with the spread of the centers discovered by the K-means algo- rithm ,as shown by σ = dmax √ 2K ,where K is the number of centers and dmax is the maximum distance between them. This formula ensures that the individual Gaussian units are not too peaked or too ﬂat;both extreme conditions should be avoided in practice.

• Output layer.

Once the training of the hidden layer is completed, the training of the output layer can begin. Let the K × 1 vector.

  ϕ(xi, x1) ϕ(xi, x2)   φ(x) = (3)   ...     ϕ(xi, xK)

denote the outputs of the K units in the hidden layer. This vector is produced in response to the stimulus xi, i = 1, 2, , N. Thus, insofar as the supervised training of the output layer is concerned,the training sample is deﬁned by

Φ(i), d(i)N i=1

,where di is desired response at the overall output of the RBF network for input xi,This training is carried out using the RLS algorithm. Once the network training is completed, testing of the whole network with data not seen before can begin.

4.3 Experiment

We demonstrate out model in online news dataset[5].we pre-process dataset in term of ﬁlter Unnecessary factors. Our dataset is divided to two class , the number of shares more than 1400 is considered signiﬁcant ˛a ˛a information. The number of information is 39240,we train our net- work using 27908 information, and then test with 11332 information.The considering factors as follows, 1) Days between the article publication and the dataset acquisition(non-predictive). 2) Number of words in the title. 3) Number of words in the content. 4) Number of images. 5) Number of videos. 6) Number of keywords in the metadata. 7) Data channel: lifestyle, entertainment , business, social media,tech,world. 8) Was the article published on the weekend? 9) Number of shares

The results of our network is given in table: Accuracy in train procedure is 75.1%.

4.4 Sensitively Analysis

We draw a ROC curve graph to verify the sensitively of our network. The curve can cover most area. It indicate our network is sensitive. In order to validate the stability of our network ˇcˇnwe test our network in our dataset. The re- sults is given in table as above. Accuracy in test procedure is 74.3%.The results show that out model can adapt to data-change, and ﬁlter information as news.

4.5 Conclusion

The RBF network adopt “”K-means RLS“” algorithm, which can improve the performance of computing. This algorithm has two characteristics: computational simplicity and acceleration convergence. The only suspect is the lack of the training of hidden layer and the training of output layer combined with the most criteria, which in the statistical sense to ensure the entire system of optimality. The only thing to doubt is not to p=optimize the training of hidden layer and output layer, so as to ensure the optimality of whole system in statistics. Using RBF network ,we can implement our information ﬁltering efﬁciently.

5 A SN-SIR Model

To solve the problem of how public interest and opinion can be changed through information networks in the Internet,we model of social network mainly about public opinion based on SIR and complex network theory,and then we text the model performance by FaceBook’s social network datasets.

5.1 The Way of Information Dissemination in Network

In the social network ,the relationship between the user can be established only by both sides of the identity authentication .[7] So social network can be thought of as net which does not has directions and weight and use the users and the relation ship between users replaces nodes and edges,and topics or news spread along the edges.[8]

5.2 A Model of Public Opinion Dissemination in Social Network

we classify nodes into three types as same as we deﬁne above,and assume that all nodes are susceptible in the beginning,but adding or changing some deﬁnition of factors are as follows.

• 1)Psi is the rate of probability of node in state s turn to Node in state i when s contacts with i.

• 2)α is the rate of probability of node s turned to node i when s gets some public opinions but does not contact with i.

• 3)Pir is the rate of probability of node i turn to node r in state r when node i lose s interest about a public opinion and stops spreading the public opinion.

• 4)Psr is the rate of probability of node s trun to node r when s gets a public opinion it is not interested in and dose not want to spread the public opinion.

• 5)k is the degree value of each node.

5.2.1 Model Building

It is a kind of dynamic procedure when we refer to the spread of social networking topic. Propaga of topic is inﬂuenced by one or more factors . The spread when a node in social net- work want to spread some opinions will be inﬂuenced by the ability of neighboring nodes. The greater the degree of spread of nodes,the better to public opinion spread in the network. Make a conclusion about the above knowable,and we get the model of node state transition in social network.[6] On the basis of model of node state transition and theory about SIR,we build the public opin-

ion transmission model in the social network is as followsˇcž

ds(k,t)  = −psiks(k, t)θt −αs(k, t) −psrs(k, t) dt        di(k,t)  = psiksk, tθt + αs(k, t) −pirs(k, t)   dt   (4) dr(k,t)  = psrsk, t + pirik, t   dt         s(k, t) + i(k, t) + r(k, t) = 1  In the above equation,θ(t) signiﬁes the probability of any edges can contact with nodes in state i at time of t,and its equation is as follows:

P k kP(k)i(k, t) θ(t) = (5) < k > In the above equation,P(k) is the degree distribution function of social networksˇc˙z< k > is the average node degree of social networks.

5.3 Sensitivity Analysis and Model Validation

5.3.1 Model Validation

In order to validate the efﬁciency of public opinion topic transmission model which we pro- posed,we choose the standard data sets -“” Facebook social network dataset“”which includes 4039 nodes and 88234 sides to carry on our simulation experiment.[9] 1. The relation between the density of different nodes over time Assuming that there is only one communication node in the network and the rest areall nodes in state s .Set the total pa- rameters of ( 1 ) as follows : the external infection probability Psi = 0.4; the internal infection probability α = 0.3; the immune probability Pir = 0.2; the direct immune probability Psr = 0.1. The change relation between the density of each node and the spread of public opinion topic is shown in ﬁgure 3.From pictures below:

we can see: The density of the susceptible nodes have a tendency to attenuate until it is close to zero.The density of transmission node have a rapid growth in the initial stage,and it will decline rapidly after its peak until its tendency to zero.While the density of the immune node shows a quick growth at the beginning of the diffusion of a topic.It will become stable gradually after its peak and tend to be 1 in the end. We can draw the conclusions as follows after our parameter veriﬁcation of the social network.

• 1.Generally speaking ,the higher the value of an information is,the lower immunisation rates of the information will be ,the higher the internal infection rate will be. There will be more transmission nodes and less immune nodes in a short transmission-cycle time.Which means the more quickly the information spread,the more widely the range of users will cover.

• 2.User ˛a´rs interests and prejudices can react on the immune probability and the infection rate,the higher the user’s interests in the message is,the lower the corresponding immune probability and direct immune immunisation rates will be ,and the infection rate will rise accordingly, when the message comes to the user, the speed of the spread will be faster, and as for a message, the more uses are interested in, the lower the corresponding im- munity will be,the more people infected will be,the more transmission nodes will be, the faster the news propagation speed will be ,that is to say,the transmission will be faster if it owns more users interested in.

5.3.2 Sensitivity, parameter validation analysis

1.The inﬂuence of Psi When Psi is changed ,the variation trend of density ﬂuctuation about nodes in state s and r is as followsˇcž

(1)Before the Internet reach steady state, with the increase of Psi ,the density about nodes in state s is growth,but the density about nodes in state r is go down.The reason about this is the greater of Psi ,the more number of nodes in state i transform into nodes in state sˇc˙z

(2)With the increase of Psi ,the time of The spread of social network public opinion reaches a steady state is more longer.

(3)When Psi=0, social network information can still be propagated,this is different with pre- vious research results.The reason about this is the connectivity of social networks is higher when it compare with traditional network and social network user can get public opinion from each other and other mode.

2,The inﬂuence of Pir When Pir is changed ,the variation trend of density ﬂuctuation about nodes in state s and r is as followsˇcž (1) When Pir >0, before the Internet reach steady state, Pir and the density about nodes in state s against each other and found a negative correlation,but Pir and the density about nodes in state r found a positive correlation.So,the value of Pir is greater,the rate of probability of nodes in state i turn to state r is higher.

(2) When Pir =0, Pir increase rapidly in the early,gradually stabilized after get to the peak .The reason about this is when Pir =0, nodes in state I Will always keep their state and do not switch to the state r.However,the density about nodes in stater !=0 because of the inﬂuence of Psr and some nodes in state s turn to stater.

3,The inﬂuence of α When α is changed ,the variation trend of density ﬂuctuation about nodes in state s and r is as follows.The ﬁgure shows that before the Internet reach steady state,as long as the value of˛eÁ- further increase, the density about nodes in state i increases correspondingly,but the density about nodes in state r decrease all the time.This is mainly because the value of α is greater,the rate of probability of nodes in state s turn to state i is higher.

4,The inﬂuence of Psr When Psr is changed ,the variation trend of density ﬂuctuation about nodes in state s and r is as follows.The ﬁgure shows that with the increase of Psr,the density about nodes in state r is growth,but the density about nodes in state i is go down. This is mainly because the value of Psr is greater,the rate of probability of nodes in state s turn to state r directly without turn to state i is higher.

5,The inﬂuence of initial nodes degree k0 When k0 is changed ,the variation trend of den- sity ﬂuctuation about nodes in state s is as follows.And we can know that the value of k0 is greater,the speed of public opinion propagation is faster in social network.

6,The inﬂuence of different node density changes over time When the density about nodes in state s,i and r is changed, public opinion evolution trend over time is as follows.From the picture,we can kown that, no matter how the density about nodes in state s,i and r change with time, public opinion evolution trend are basically identical. This shows that the different value of nodes has similar behavior characteristics.

5.4 Result Analysis

Using social network dataset to validate the patameters , we can draw the conclusions as fol- lows. (1)Generally speaking ,the higher the value of an information is , the lower immune probability of the information will be ,the higher the internal infection probability will be. There will be more nodes in state s and less nodes in state r in a short transmission-cycle time , which means the more quickly the information spread, the more widely the range of users will cover.

(2)User ˛a´rs interests and prejudices can react on the immune probability and the infection rate .The higher the user’s interests in the message is , the lower the corresponding immune prob- ability and direct immune rates will be ,and the infection rate will rise accordingly, when the message comes to the user, the speed of the spread will be faster, and as for a message, the more uses are interested in, the lower the corresponding immunity will be , and the more people in- fected will be , the more transmission nodes will be, the faster the news propagation speed will be ,that is to say , the transmission will be faster if it owns more users interested in.

(3)In social network ,the source of the message can be divided into hot transmission nodes and normal transmission nodes as we discussed in the information ﬂow model. Hot trans- mission nodes have larger infection rate and degree of value ,but normal transmission nodes that infection rate is lesser, degree of value is smaller than hot transmission nodes. Consider- ing the inﬂuence of parameters, we parsed on the information dissemination model, when the news that come from hot transmission nodes have faster transmission speed and wider scope of news than ordinary nodes.

(4) Using degree value of the nodes describes the different network topology and strength . Through transformation analysis of parameters, the degree of initial node in social networks have an obvious impact on public opinion propagation velocity , and different nodes ˛a˝o distri- bution has a small impact.

6 Analysis

6.1 Strengths

• Our model invokes and expand the classical SIR model.

We take times ,Medium inﬂuence into consideration and develop a SIIR model to solve information ﬂow problem. the external infection rate is taken into account.In order to adapt internet information ﬂow,we propose a SIR model that base on social network in internet.

• The solving processing and solution is stable.

• The result of out model is visible and easy to understand.

We demonstrate our model using data, and the result can be understand from the exper- iments. Consequently , anyone can comprehend the evaluation without any background knowledge.

• Our model has a strong sense of professional background.

Our model based on both subjective and objective methods solve the information ﬂow , information ﬁltering ,and ﬁnd the factors of inﬂuence information ﬂow.

• Our model can be extended into higher dimension.

As an information ﬁltering system can extend to take more dimension factors ,and then using our model to ﬁlter the information. Our model can explain the sustainability in a more explicit way.

• The dynamic prediction can be easily tracked.

The mechanism of our system dynamic offers handy to predict information ﬂow and capacity.

6.2 Weaknesses

• The model does not take platformsˇcˇnnetwork complexityˇcˇnRegion inﬂuenceˇcˇngovern- ment control and other factors into consider.

The model cannot accurately forecast information ﬂow between different region or plat- form, thus the sustainability is not necessarily exact in terms of some uncontrollable fac- tors.

• The statistical date used in implementing of model not complete achievable.

We cannot ﬁnd all data we required for sustainability. Fortunately, ICM‘’s extensive Medium resources and inﬂuence would deﬁnitely help ICM to attain the data.

• The dynamic system can only explain the local part of information ﬂow.

We invoke SIR to solve the model which is not fully simulate the formation dissemination of the real world.
