MCM/ICM

Summary Sheet

Summary

The illegal wildlife trade (IWT) causes great harm not only to animals, but also to the environment and human health. In this paper, our 5-year program relies heavily on networked collaborations built from data-driven efforts to achieve IWT reductions.

For task1, we build a population competition model. By combining the five elements of PUR, SR, PER, IN, CI, we calculate the scores of GA, INO and PAP, which are 0.42, 0.51 and 0.37 respectively. The higher the score, the more suitable it is for our project. Therefore, the client of our project is INO.

For task2, by fitting the data and solving the model, we verified that our project can make the number of poaching gangs to have a large decrease in the degree of hierarchy. We use BP neural network to drive the data, and the R-value of the model training result is about 0.966. The obtained prediction graph shows that the number of IWT will still be high in the next 5 years, so we need to move forward with the project to reduce the number of IWT.

For task3, we conduct our 5-year program around a 3-point strategy of cross-regional awareness, transaction hotspot crackdown, and regional sentinel surveillance.

For task4, we obtain the optimal path for cross-regional advocacy, and the results show a positive proportional increase in support for INO with the level of sensitization. We build a network of trading hotspots to combat trading hotspots and a network of monitoring systems in 5 countries, the results all indicate that the use of these strategies will lead to a sig- nificant decrease in the number of IWT globally over the next 5 years.

For task5, we consider the implementation of the three strategies reaching 95% as reach- ing the expected goal, and the probability of reaching the goal is 65.1% by calculation. Con- sidering three unexpected factors, we use binomial distribution and Poisson distribution to compare and conclude that the resistance of poaching organizations has the most serious impact on the project. In the case of its strengthening by 10%, the strategy attainment rate decreases by 19.73%, and the total project attainment rate will be reduced to 60.8%.

Finally, we evaluate the model and provide a memo. We hope that our model based on data-driven and networked collaboration will provide a new solution for reducing IWT.

关注数学模型

1 Introduction

1.1 Problem Background

微信公众号：数学模型 Due to the high global consumer demand for wildlife for medicinal purposes and other aspects [1], IWT is already worth up to $26.5 billion annually. IWT reduces biodiversity, has irreversible negative impacts on the environment [2], and can even lead to outbreaks of zoonotic diseases. Nowadays, the number of wildlife in many countries is declining rapidly and facing extinction. Therefore, we need to produce a program to reduce IWT in order to achieve peaceful coexistence between man and nature.

1.2 Restatement of the Problem

The model we are to build should solve the following problems:

1. Identify the customers for which our project is targeted.

2. We develop projects for client reasons and use existing research to support our projects.

微信号：MATHmodels 3. Rights and resources required by the client to implement the project.

4. Measures of illegal wildlife trade.

5. The likelihood of the project achieving its intended objectives, as well as conditions or events that may affect the project's ability to achieve its objectives.

1.3 Literature Review

Since the COVID-19 outbreak, many scientists have found that zoonoses are closely linked to the IWT [3]. According to Mozer Annika, a recent study by Prost Stefan found that more than 60% of emerging infectious diseases in humans are caused by zoonoses, which kill 2.7 million people every year [4]. More than that, IWT has cascading consequences on environ- ments, human lives and communities, national stability, and the economy. Moreover, IWT is linked to many different crimes, such as corruption, money laundering, drugs and so on [5].

Now, researchers are trying to find ways to strike a balance between economic and con- servation interests to reduce IWT. Dominic Meeks, Oscar Morton, and David P. Edwards have experimented with captive breeding of wild animals [6]. Justin Kurland, Stephen F. Pires et al have proposed the establishment of protected areas and fenced barriers to reduce animal-human conflict [7].

1.4 Our Work

In order to solve the problems, we build and optimize the entire model:

·First, collect and process data, build a competitive population model, and select the right client for our project from multiple potential clients.

·Second, give merits of our project, conduct data-driven analysis, and convince the client.

·Third, establish a global wildlife network, propose the main strategies for implementing the project and implement the path of cooperative combat.

·Fourth, the process of implementing the policy and comparing the results without the policy with the predicted results with the policy.

·Last, prediction of project compliance, sensitivity analysis and further discussion.

Our workflow is shown in Figure 1.

关注数学模型 微信公众号：数学模型

微信号：MATHmodels

2 Assumptions

To simplify the given problems, we make the following basic assumptions: ·The smallest participants in the global illegal wildlife trade are measured by country. ·The social environment is relatively stable. ·The data we collect is precise and representative.

3 Notations

The key mathematical notations used in this paper are listed in Table 1.

Symbol

Description β Prey Growth Rate δ Predation Rate γ Predator Mortality Rate IWT Illegal Wildlife Trade PUR Pursuit Rate SR Support Rate PER Persistence Rate IN Interestingness CI Cooperation Index SC Self Condition SD Species Diversity GA Government Agency INO International Non-profit Organization Focused On Biodiversity Conservation PAP Private Sector For Animal Protection SE Strike Effect OSR Overall Strike Rating TTV Total trade volume CAI Comprehensive adaptation index

关注数学模型

4 Data preprocessing

4.1 Data collection

微信公众号：数学模型 In order to identify our clients and develop programs to reduce IWT, we collect data on IWT from many official websites for almost every country in the world.

The IWT data is used to examine how effective our programs are in reducing IWT.

In order to obtain enough data and to speculate on historical trends, we find data from 193 countries for 36 years (1986-2021) according to data provided by cites [8].

4.2 Data normalization

First, the dataset is processed with normalization, where the maximum gap value in the data is   = − M max x x (1) i best

微信号：MATHmodels Honorific title

− x x = − i best x 1 (2) i M

The maximum distance from the iso-maximum to the boundary is     = − − (3) M max a min x ,max x b i i

Re-determining the elements yields

− − a x i 1   x a M i  =   x 1 a x b (4)  i i  −  x b x b − i 1 i  M

Considering the variability of data indicators, our data is standardized before being ap- plied. For n evaluation objects and m evaluation indicator variables, the matrix is constructed

  X X X 11 12 1 n   X X X   =  21 22 2 n (5) X  i   X X X   n 1 n 2 nn

Let the normalized matrix be Z. Then for every element in Z

X ij = Z (6) ij n  X ij = i 1

The weight of each sample under each indicator is then calculated, and after the previous normalization and standardization of the data, a matrix can be obtained

关注数学模型 Z Z Z 11 12 1 n Z Z Z = 21 22 2 n Z (7)

微信公众号：数学模型 Z Z Z n 1 n 2 nn

Next, calculate the specific gravity matrix P, where each element of P p is given by ij

Z ij = p (8) ij n  Z ij = i 1

According to the formula, it is easy to get

n  = (9) p 1 ij = i 1 微信号：MATHmodels We think of ratio (8) as a probability.

5 Lotka-Volterra integrated evaluation model for task1

5.1 Modeling population competition

Based on the data of globalized illegal wildlife trade behaviors, we find that the vitality of international wildlife conservation organizations presents a population competition relation- ship with the stealers. Therefore, we decide to describe the relationship between them through the Lotka-Volterra model. In this case, the International Wildlife Conservation Organization is the predator and the stealers are the prey.

Define:

·Prey growth rate α: the natural growth rate of poachers, estimated by the natural growth trend of illegal trade activities.

·Predation rate β: the efficiency of international organizations in "preying" (i.e., combat- ing) on the activities of poachers, expressed as the product of the chances of encounters be- tween the two (magnitude) and the success of the international organization in stopping the illegal activities (enforcement efficiency).

·Predator mortality rate γ: the natural rate of reduction of the international organization's power in the absence of predator activity, due to the loss of funds and attention (1/funding level).

·Energy conversion rate δ: the efficiency of an international organization's ability to strengthen itself by combating illegal activities (people's support × political support), as re- flected in the growth of its "population".

·Assume that X(t) is the population size of thieves and Y(t) is the "population" viability of the international organization.

The relationship we expect to obtain between the dynamics of international organizations and changes in the number of thieves' populations satisfies the differential equation.

关注数学模型  dX =  −  X XY  dt (10) dY  =  −  XY Y 微信公众号：数学模型  dt

Mapping the Lotka-Volterra model to a realistic organization has: PUR = predation rate = β, SR = energy conversion rate = δ, PER = 1/predator mortality rate = 1/γ.

After that, PUR, SR, and PER are optimized to improve the fight against thieves.

So, what we need is the customer to provide us with personnel support to facilitate the real-time combat and disruption of the theft network. At the same time, we need to take into account the economy of supply, so that our cooperation can be solid. We would also like to have good international support to facilitate our trans-regional behavior and the possibility of implementation.

5.2 Model solution

微信号：MATHmodels Under the guidance of the Convention on International Trade in Endangered Species of Wild Fauna and Flora, we evaluate and score three specific factors: PUR, SR, and PER.

Hierarchical analysis [9] is used to construct pairwise comparison matrices for PUR, SR, PER [10]:

  1 2 1.25   0.5 1 0.625 (11)     0.8 1.6 1   Calculating the weight [11]. As shown in the Figure 2, a below. It can be seen that in this model, PUR accounted for 0.43, PER accounted for 0.35 and SR accounted for 0.22.

The benefits to clients of reducing illegal wildlife trade are most notable in terms of inter- national reputation, biodiversity and tangible benefits.

Constructing a pairwise comparison matrix of international reputation, biodiversity and tangible benefits.

  1.00 0.75 1.50   1.33 1.00 2.00 (12)     0.67 0.50 1.00  

Calculating the weight. As shown in the Figure 2, b below. Biodiversity is the greatest benefit gained by clients from reducing illegal wildlife trade, accounting for 0.44 of the total benefits, followed by international reputation at 0.33 and practical benefits to a slightly lesser extent at 0.23.

关注数学模型 微信公众号：数学模型

5.3 Analysis and comparison

Based on the strike factor and interest factor, we search for clients globally, and we iden- tify GA, INO and PAP as our potential clients.

·GA: Have very high levels of funding and political support, as well as excellent local 微信号：MATHmodels and neighboring partnerships for building localized conservation networks. Interested in en- hancing their international reputation.

·INO: Have basic strengths that are comprehensive, but have strong global cooperation and can build a global conservation network. Interested in conserving species diversity.

·PAP: Highly effective in implementation, but cooperative only in small regions and can only build small conservation networks. Interested in enhancing tangible benefits.

We score GA, INO, PAP on PUR, SR, PER, IN, and CI respectively, and normalize the resultant data to obtain the results shown in Figure 3.

From Figure 3, it can be seen that PER is the most attractive to GA, with a degree of 0.81. CI and IN are the most attractive to INO, with degrees of 0.70 and 0.443, respectively. SR and

关注数学模型 PUR are the most attractive to PAP, with degrees of 0.86 and 0.71, respectively. In comparison, both CI and IN are the most attractive to INO, both are relatively weak to GA, and both are the least attractive to PAP. Both PUR and SR are most attractive to PAP, both are relatively weak to INO, and both are least attractive to GA. Both PUR and SR are most attractive to PAP, both 微信公众号：数学模型 are relatively weak to INO, and both are least attractive to GA.

Then, the CAI is created. The weights of PUR, SR, and PER are 0.43, 0.22, 0.35.

= +  = +  + + CAI (1 IN )(CI SC) (1 IN CI )( (0.43 PUR 0.22 SR 0.35 PER )) (13)

The results obtained are shown in Table 2.

GA INO PAP PUR 0.42 0.57 0.71 SR 0.23 0.46 0.86 PER 0.81 0.49 0.32 IN 0.34 0.43 0.23 微信号：MATHmodels CI 0.60 0.70 0.50 Score 0.42 0.51 0.37 From Table 2, we can see that the scores of GA, INO, and PAP for the composite adapta- tion index are 0.42, 0.51, and 0.37 respectively. Among them, INO has the highest score, which indicates that INO is the most suitable for our project. In other words, the customer facing our project is INO.

6 BP neural network prediction model for task2

6.1 Reduce the number of poaching organization

To verify that the program we developed is suitable for INO, we collect data on the number of poaching organization from 2000-2020. We normalize the collected data and then linearly fit the normalized data for each year to obtain a straight line as shown in Figure 5 below.

Substituting the data of all the years into the Lotka-Volterra model, i.e., Equation (10), yields

 dX = − 0.038 X 0.37452 XY (14)  dt  dY  = −  0.30277 XY 0.322203 0.1 Y  dt  = = X (0) 0.19 (0) Y 0.2 

The calculation results are shown in Figure 6 below.

关注数学模型 微信公众号：数学模型

From Figure 4, it can be seen that the number of poaching organizations roughly shows an upward trend as the number of years increases.

From Figure 5, if our model is used, the vitality of international organizations is roughly increasing over time, while the number of poaching organization has been decreasing over time, and by a large margin.

As can be seen from both Figure 4 and Figure 5, our project can lead to a substantial 微信号：MATHmodels decrease in the degree of hierarchy in the number of poaching organizations.

6.2 Improve biodiversity

A recent study by Sangram K. Pathare explores the feasibility of cooperative biodiversity conservation modeling. According to SYNERGISTIC CONSERVATION PARADIGMS: A STUDY OF COLLABORATIVE BIODIVERSITY CONSERVATION MODELS [12], Antipoach- ing measures are very important to improve conservation efficiency. In "Project Tiger", the inclusion of local people as investigators and frontline defenders and the promotion of their sense of ownership as a means of countering poaching have been instrumental in protecting local tigers. The study points out that anti-poaching initiatives not only increase the effective- ness of conservation actions, but also promote community participation and support for pro- tected areas.

This study emphasizes the importance of strengthening anti-poaching measures through collaborative models and community participation, pointing out that combating poaching ac- tivities increases the effectiveness of species diversity conservation.

Therefore, it can be argued that SD shows a positive correlation with the reduction of poaching activities, i.e.

=  SD

C Decline in poaching groups

(15)

According to Figure 6, our program is very effective in reducing poaching activities, i.e., our program has a strong positive effect on increasing species diversity and is productive in the short term.

If our program is implemented, it is predicted that the level of conservation of species diversity will increase by about 21% in five years.

6.3 Big data-driven forecasting

6.3.1 BP Neural Network

The computational representation of the output yj for each neuron j is:

关注数学模型 n  =   + (16) y ( x b ) j ij i j = i 1

where xi is the input value, ωij is the connection weight, bj is the deviation of the neuron, and σ 微信公众号：数学模型 is the activation function.

Calculating the loss function, for the regression problem, with mean square error:

P 1   = − 2 E ( , ) b ( d y ) (17) p p 2 = p 1

where dp is the target value, yp is the predicted value, P is the sample value, and M is the cate- gory value.

Update the weights:

 E  =  −  (18) i j new ( ) ij old ( )  ij 微信号：MATHmodels  E = − b b (19) j new ( ) j old ( )  b j

The chain rule is applied to compute the partial derivatives:

 y   E E j =  (20)      y ij j ij

Finally, the weights are repeatedly updated using the weight update formula described above until the stopping condition is satisfied.

The flowchart of the algorithm for the BP neural network is shown in Figure 6 below.

关注数学模型

6.3.2 Training of BP Neural Network

We train 248 data and loop 736 times to get this result with a training time of about 29 seconds. The training results are shown in Figure 7 below.

微信公众号：数学模型 微信号：MATHmodels

From Figure 7, we can see that the R of training is 0.997, the R of verification is 0.939, the R of test is 0.929, and the R of training is 0.923. These four R values are very close to 1, which can show that our BP neural network is well trained.

6.3.3 Forecasting future volumes

The trained BP neural network is used to process our collected data and predict the number of global IWT in the next 5 years to get the results shown in Figure 8.

关注数学模型 微信公众号：数学模型 微信号：MATHmodels

As can be seen from Figure 8, the height of our predicted data for the next 5 years is about the same as that of the historical data with similar fluctuations, which is consistent with the historical trend in terms of the pattern, and it can be shown that our predicted data are reason- able.

If the IWTs are not interfered with, the global number of IWTs will still be at a relatively high stage in the next 5 years.

Therefore, it is very necessary to implement our project.

7 Project assumptions and network prototyping for task3

Based on a huge amount of data, we built a global IWT network.

关注数学模型 We consider each country in the world as a node and gather all the countries together to 𝑛. If there is IWT between country i and country j, then there will be a form the set 𝑉= {𝑣𝑖}𝑖=1 vector edge generated from node i to node j. The darker is node color of a country, the more illegal wildlife trade relationship it has with the country. Where the darker the color of the node 微信公众号：数学模型 means that a country has illegal wildlife trade relationship with more countries.

The core of our 5-year plan will be around the cross-regional publicity strategy, trading hot spot attack strategy, and regional fixed-point monitoring strategy.

7.1 Cross-regional propaganda strategy

In order to make more people around the world understand and pay attention to IWT, we must be based on the international, cross-regional publicity to obtain more people's support and improve SR. We hope to carry out universal publicity according to the nodes of the global transaction network, and achieve the ideal publicity effect in the shortest possible time.

INO has a strong international reputation and high support rate, so it is the perfect person to conduct a global campaign about IWT. Therefore, assume that it needs to have the following 微信号：MATHmodels powers and conditions:

·Free to promote activities between countries around the world.

·The duration of the propagandist's stay in a country is 7 days.

·Propagandists spend no more than 8 hours on the road at a time.

·It is believed that the movement speed of propagandists is the same among countries, which is 120km/h.

7.2 Trading hot spot attack strategy

Opposition to IWT is essential to the destruction of trading points, especially trading hot spots. Cracking down on hot spots not only cracks down on thieves, but also gives information about hidden chains of transactions, to improve PUR. Relevant persons are arranged as neces- sary to bust important trading hotspots, which can reduce the number of crucial nodes in the transaction network.

By acting in cooperation with countries, we can gain access to important transaction net- work nodes. Assume that INO has the following powers and conditions:

·The intensity of the attack is related to the level of nodes.

·It takes one year to destroy a node, and the destroyed node will not be built again for five years.

7.3 Regional fixed-point monitoring strategy

To combat more thieves, area surveillance is needed. This will improve our PER against the thieves. Especially around the transaction node, monitoring institutions can be set up to monitor the transaction network and dig the transaction chain.

Because the monitoring of the surrounding network nodes can continuously act on the transaction network. Assume that INO has the following powers and conditions:

·The organization can provide a large number of human resources, the number of mon- itoring points will not be limited, but it will take a year to establish one.

·The monitoring area of each monitoring point is the same size.

关注数学模型

8 Analysis of Big Data Transaction Networks for task4

8.1 Realization of a global communication strategy

微信公众号：数学模型 According to task3, INO will be tasked with a global publicity campaign. It may be useful to make it start on any network transaction node and traverse all the nodes to publicize it.

8.1.1 Mathematical modeling of TSP

Define the set 𝐶= {1,2, ⋯, 𝑛} to denote the cities with indexes 1 to n. The distance ma- trix is

= (21) D [ d ] ij

where dij denotes the distance from city i to city j.

Let the decision variable be xij, then = →  x 1, i j i j (22)  = x 0, otherwise 微信号：MATHmodels  ij

The total travel distance minimized, i.e., the objective function is.

n n  Minimize d x (23) ij ij = =  i 1 j 1, j i

Assuming that each city can only have one entry and one exit, for 𝑖= 1,2, ⋯, 𝑛, there are

n  = x 1 (24) ij =  j 1, j i

8.1.2 Simulated Annealing Algorithm

The objective function to be optimized:

n n n n n n n n     = M i in mize d x min( d x , d x , , d x ) (25) − − ij ij 12 12 13 13 n n ( 1) n n ( 1)   x X x X = =  = =  = =  = =  i 1 j 1, j i i 1 j 1, j i i 1 j 1,, j i i 1 j 1, j i

Define how the temperature decreases and when the annealing process stops:

=  T T (26) new current

T T where is the current temperature, is the new temperature, and α is the cooling factor, current new

which usually takes a value less than one.

Metropolis acceptance criterion:

E = − (27) P accept ( ) exp( ) k T B

where E is the energy change, i.e. the difference between the new objective function value

k is the Boltzmann and the current objective function value, T is the current temperature, and B

constant. If E < 0, the new solution is accepted unconditionally.

关注数学模型 Neighborhood search: an optimization problem in continuous space that can be formulated as adding a temperature-controlled random perturbation to the current solution:

= +  x x ( , ) x T (28) new current 微信公众号：数学模型 Finally, the obtained data is normalized to get the result.

8.1.3 Optimal solutions

We find data from 166 countries and solve the optimal propaganda routes using the math- ematical model of the TSP and the simulated annealing algorithm. As shown in Figure 10 below.

微信号：MATHmodels

Therefore, the shortest time that INO can complete the global cycle of advocacy is about 1,696 days.

The change in people's support during the campaign is what we need to measure. Since awareness campaigns show a positive correlation with people's support, it can be assumed that awareness campaigns can directly contribute to the increase of support to indirectly inhibit the occurrence of poaching. According to a survey published in Biodiversity Science by Center for Nature and Society, School of Life Sciences, Peking University, Beijing [13], it can be learned that people's attitude against illegal animal trade in publicity campaigns expresses a very good response.

Strongly agree Agree Neutral Disagree Strongly disagree

Proportion 87.0% 8.1% 2.5% 1.3% 1.1% Based on the statistical results of Table 3, the relationship between our advocacy process and people's support is satisfied

=  Growth rate of people s support ' 0.9568 Promotional activities progress (29)

From equation (29), the deeper the sensitization process, the higher the level of people's support and the higher the level of support INO receives.

关注数学模型

8.2 Implementation of the Global Trading Node Strike Strategy

Based on the data of the trade between the found countries, we built a network of trading hotspots as shown in Figure 11.

微信公众号：数学模型 微信号：MATHmodels

The important nodes of the transaction can be clearly seen in Figure 11, which in turn can be struck against. The smaller the node is, the better the strike is, and conversely, the larger the node is, the worse the strike is. In other words, we can assume that the strike effect is inversely proportional to the size of that node.

Therefore, we can reflect SE through OSR, which in turn indirectly affects TTV.

 1 = SE (30) Node size  =  OSR SE TTV 

After implementing our program, according to Equation (30), the transaction volume of IWT in the next 5 years can be predicted. If a node is struck in each future year, the transaction volume of IWT will decline in the next five years. Among them, the transaction volume of IWT in 2024-2028 declines rapidly, while the transaction volume of IWT in 2028-2029 declines relatively more gently.

8.3 Implementation of trade network monitoring strategies

Considering the different trading nodes around the globe, we can build a network of mon- itoring systems to achieve the control of illegal wildlife trade.

关注数学模型 We have identified five countries to build the monitoring region through the optimization of greedy strategy [14], which are South Africa (25.7479ºS, 28.2293ºE), China (39.9042ºN, 116.4074ºE), United States of America (38.9072ºN, 77.0369ºW), Swiss Confederation (46.9480ºN, 7.4474ºE) and Brunei Darussalam (4.9031ºN, 114.9398ºE). 微信公众号：数学模型 We prioritize the countries in which we establish surveillance systems based on the size of the data we collect on national IWT over the years, with countries with large IWT establish- ing surveillance systems first, and countries with small IWT establishing surveillance systems later. The order for the establishment of surveillance systems year by year are as follows: Swiss Confederation, China, United States of America, Brunei Darussalam, South Africa.

The locations of the established surveillance systems are shown in Figure 12.

微信号：MATHmodels

In the figure, the monitoring radius of each monitoring point is 1000km. The IWT is max- imized for the area covered by each monitoring point.

After establishing the monitoring system in the above countries, our calculations suggest that the number of IWT globally will decline significantly over the next five years

8.4 Effectiveness of the project after implementation

From the above analysis, we can see that our three strategies are significantly effective in reducing IWT. Combining the effects of these three strategies, the overall reduction of IWT is more obvious, and the results are shown in Figure 16.

关注数学模型 微信公众号：数学模型

微信号：MATHmodels According to the heat map, we analyze the change in trade within the ellipse area of the graph and can see that our model will have a decrease of about 23.5% in the global illegal wildlife trade after five years of implementation.

9 Probabilistic model of project implementation for task5

9.1 Forecasting the likelihood of meeting expectations

Based on our expectations, we would like to see more than 95% implementation of all three of our strategies within five years, which would be considered to meet the desired goal.

Considering our project together, it is specifically the three main strategies that play a role. Now we further generalize based on the results calculated in task4. Since our strategies are all based on the assumptions of task3, we extend the model in a reasonable way. We consider the existence of some impediments:

·Hindering to the publicity strategy: flight delays ·Hindering to the policy of combating trading hotspots: resistance of poaching organiza- tions ·Hinder to the monitoring policy: the influence of weather factors We get the probability of flight delays is about 15.36% and the probability of resistance of poaching organizations is about 10% based on the data of the past years, and both probabil- ities obey the binomial distribution:

 n − = = − k n k X P X ( k ) p (1 p ) (31)  k 

The effect of the weather factor obeys a Poisson distribution with λ = 30:

−   k e = = X P X ( k ) (32) bad weather bad weather k !

关注数学模型 Thus, we can consider that the number of days of propaganda consumption= 1696 +

0.2𝐾2+1×(5−𝐾2) 8𝐾1(0 ≤𝐾1 ≤166), the effectiveness of trading hotspot strikes= , and the ef- 5

微信公众号：数学模型 𝐾3 fectiveness of monitoring the area= 1 −0.4( 365).

Let all the above three equations be greater than or equal to 95%, i.e.

  5 365  95%  + 1696 8 K  1 +  −  0.2 K 1 (5 K )  2 2 95% (33)  5   K −   3 1 0.4 95%  365

Solve for

  微信号：MATHmodels K 28 1   (34) K 1.25  2   K 45.625  3

Under the conditions of big data, the statistics show. The delay of flights and the resistance of poaching organizations can approximately satisfy the binomial distribution, so we can cal- culate the impact of flight delays and resistance events on the probability of project attainment through the n-weight Bernoulli test.

Therefore, the likelihood of the project meeting expectations is 𝑃= 𝑃(𝑘1 ≤28) ∙𝑃(𝑘2 ≤1.25) ∙𝑃(𝑘3 ≤45.625) = 0.8286 ∙0.9185 ∙0.9960 ∙100% = 65.1%

9.2 Contextual sensitivity analysis

·When the impact of flight delays increases, all other conditions remain unchanged. At

关注数学模型 10% enhancement of delay impact, the maximum value of K will become 25, which is calcu- lated based on the binomial distribution as a 166-weight Bernoulli test. At this point the prob- ability of meeting the standard to complete strategy one will become 0.8075, a decrease of about 2.5%. 微信公众号：数学模型 ·When the resistance of the poaching organization increases, all else being equal. At the time when its resistance grows by 10%, the maximum K value is any 1, while there is a signif- icant change in the probability, calculated according to the binomial distribution, as a 5-fold Bernoulli distribution. At this point the attainment of strategy two changes from 0.9185 to 0.7373, a decrease of about 19.73%.

·When the number of days of severe weather changes, all other conditions remain the same. Consider that its number of days of severe weather increases by 10%, the value of K changes and there is a change in the value of λ. According to the Poisson distribution, at this time, the attainment degree of strategy III will again be 0.996 to 0.9275, a decrease of about 6.8%.

Comprehensive analysis of the above discussion, the existence of events that have a seri- 微信号：MATHmodels ous impact on the project - poaching organizations resistance behavior strengthened.

It can be clearly seen that under the condition of a single variable, the strengthening of the resistance of the poaching organization will have a very negative impact on the project to meet the expectations, in the case of its strengthening of 10%, the strategy compliance rate will drop by 19.73%, and the total project to meet the expectations rate will be reduced to 60.8%.

10 Model Evaluation

10.1 Strengths

·Our project is based on the big data under the drive to carry out, the use of probability theory, neural network training and other algorithms, in-depth mining of the information behind the big data, to provide a strong prediction of the results, to provide an effective solution strat- egy.

·Established a global illegal wildlife trade network, visualized the trade process, and combined the nodes of the network to choose the appropriate strategy.

·Our strategy combines advocacy, crackdown, and monitoring methods. Three different optimization models are used to give specific solutions and calculate the implementation pos- sibilities.

·Our model takes into account the effects of unexpected factors, such as bad weather, flight delays, poachers' resistance, etc., to be more realistic.

10.2 Weaknesses

·We assume that the social environment is relatively stable and does not undergo sudden major changes. However, in our model, the suddenness of the social environment can be re- ferred to by the attainment rate of the strategy.

·We have not yet computed the data for all countries in the world, but we believe that our model has the power to do so.

关注数学模型

Memo

Data: February 5, 2024 微信公众号：数学模型 To: International Non-profit Organization Focused On Biodiversity Conservation From: Team # 2417340 Subject: Cooperation On Reducing The Illegal Wildlife Trade We are writing the MEMO to explore an opportunity to work with you to reduce the illegal wildlife trade globally. And the details are listed as follows.

To better illustrate our team's plan to reduce the illegal wildlife trade, we have included a table below describing the details.

The first year: Starting with LBN, the mission began its global mission along the theo- retically most suitable path to 33 countries in the first year. Strategy Ⅰ The second year: Assessing the impact of the previous year's campaigns, global support Global for the fight against illegal wildlife trade is expected to increase by 19.02%. Wildlife 微信号：MATHmodels Conserva- The third year: Ongoing advocacy and advocacy effectiveness evaluation. tion Advo- The fourth year: Combined with the publicity effect and the initial planning, fine-tune cacy Pro- the publicity, and then start the publicity from SE.

gram The fifth year: Conclude the presentation process. Global support for the fight against illegal wildlife trade is estimated to have risen to 95.68%. The The first year: The nodes are rated according to their degree, and the trading volume of five- countries with higher grades is reduced firstly. year The second year: The results of the first year of the assessment are expected to reduce Strategy Ⅱ plan the global illegal wildlife trade by 4.8%. Global to re- transaction The third year: On the basis of the second year, we will target more countries with low duce node strike scores and invest 20% more manpower. the il- strategy The fourth year: Scatter our manpower and focus on low-ranking countries. legal The fifth year: Focus on countries with high demand for wildlife to ensure that the bal- wild- ance of wildlife supply and demand in each country is met. life The first year: The first monitoring station will be established in the capital of SC, and trade 50 technicians are expected to be invested.

The second year: Construction of monitoring stations in East Asia, focusing on local Strategy Ⅲ import and export illegal wildlife trade. Illegal trade The third year: Establish a monitoring station centered in the United States to provide network technical support to combat illegal wildlife trafficking operations in North America. monitoring The fourth year: Establish a monitoring station to monitor a 1000km area around strategy Southeast Asia.

The fifth year: Establish monitoring stations centered in South Africa to monitor the il- legal activities of poachers at source.

We hope you will adopt our team's plan to reduce the illegal wildlife trade. If so, we be- lieve that with the joint cooperation of both sides, this illegal practice will gradually reduce from the earth.

If you have any questions, please do not hesitate to contact me for more information.

关注数学模型

Appendix

微信公众号：数学模型

LI BG

TD

ML CI

BB

VC KN

PA HN NI KI VU CN CZ NL DK DE GQ US JM CV AG GY SR BO LS ZW MW MG MR UZ KZ AZ LB IL CY UA PL HU LV AS WS NA SZ IQ DJ KE UG RW MV NP IN VN MY MM TO TV MX PF PE LC LR GM SN EC SV GT BZ KY CU AW BF NE GH SL GN MT BE PT FR CH AT BS HT CA IS LU SM PW PH TL AU PG MP SB KH KG BD LA ID BW MZ KM SO AF QA SA SY BY AL FI SI BA TZ ZM NG CF IT SE EE NO PR DO CO AR UY CL GL DZ ET BI SD RO LT FO IE ES TN CM TG BJ BH OM ER AO ST GA PY BR GR PK BT AM KW JO TR GE GB CR FJ NC NZ TH TJ TM HR

微信号：MATHmodels

关注数学模型
