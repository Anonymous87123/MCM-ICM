summary

We aim to devise a model evaluating the performance of an ODR (Orbital Debris Removal) system and propose the best alternative. Conclusion is drawn about whether there exist proﬁtable business chances illustrated in a time-dependent mode. Further analysis is conducted by AHP to assess the overall performance of ODR. We are also required to come up with a new method implementing collision avoidance activities.

The ﬁrst model simulating the debris removal process is built on ordinary diﬀerential equations. This model serves as a basis for the proﬁts model which generates the net gains as the diﬀerence of the ODR cost and total revenue. We conclude that it takes a private ﬁrm more than 50 years to beneﬁt economically from this industry. Currently there is no proﬁts to be made.

We extend the proﬁts model to include the recycling activities of debris. Results show that it has smaller beneﬁts than the non-recycled mode due to high recycling cost. Further extensions take varying sizes of debris and diﬀerent types of cleaners into account. We conclude that using one type of cleaner makes more proﬁts than using diﬀerent types.

The third model utilizes AHP to choose the best alternatives in terms of overall performance based on ﬁve factors. The SpaDE ODR system is evaluated to be the most favorable one.Our sensitivity analysis demonstrates that our ﬁrst debris removal model is robust to parameters changes. The AHP model is sensitive to the relative weights value of the ﬁve factors.

We additionally contrive a new method of collision avoidance. The advantages of traditional ”box” method and the ”collisional probability” method are incorporated in our new method.

1 Introduction

1.1 Background

Ever since the ﬁrst spacecraft Sputnik 1 was sent into space by human in 1957, there have been about 7100 spacecraft launched into space until now [1]. The problem arising with this augmenting number is the leftover debris in s- pace resulting from explosions of defunct artiﬁcial satellites, collisions between spacecraft and so on. Currently the earth is surrounded by approximately 21,000 bits of debris larger than 10 cm and much more of it in smaller sizes [2]. Figure 1 shows the debris distribution in view of LEO (low earth orbit).

Large amount of debris poses an unneglectable threat on operating space- craft since collisions with even a small piece of such debris will involve consid- erable energy and destroy the satellites [3]. Figure 2 illustrates the number of different types of debris from year 1956 to 2012. With the space debris issue be- coming more and more alarming as people keep sending multipurpose satellites into space, a potential proﬁtable opportunity exists for private ﬁrms to commer- cialize the space debris removal. Different ODR (Orbital Debris Removal) sys- tems under developing which can be adopted by companies along with other factors such as risks, cost etc. should all be considered in this business mode [9].

1.2 Restatement of the Problem

We are required to build a mathematical model to judge whether a private ﬁrm can beneﬁt from removing space debris via a certain method or combina- tions of different alternatives. The problem is analyzed into three parts:

• Build a model to simulate the debris elimination process and predict the effect of the orbital debris removal system.

• Propose the best method using a mathematical criterion.

• Provide innovative schemes for collision avoidance if no viable commer- cial opportunity exists.

Notions to notice:

• The debris in this paper only includes the ones larger than 10 cm that can be traced and processed by the ”cleaner”. By ”debris” we refer to the man- made objects in orbit around the earth which no longer serve a useful pur- pose [3]. The meteorite pieces are not contained in the problem domain.

• In the commercial mode, the private ﬁrms only involve in business of debris removal but not in other ﬁled-related industries such as satellites launching. In our problem domain, companies can only beneﬁt from ODR systems.

1.3 Literature Review

Donald Kessler advanced a mathematical model in 1978 to predict the rate at which the debris belt might form. It was concluded that the debris ﬂux would in- crease exponentially with time even though zero net input rate were maintained [4], which is referred to as the ”Kessler Syndrome” [5].This could be traced back as the ﬁrst notion to address the space debris problem.

Ever since the concept has been put forward, numerous solutions have been proposed to deal with this issue. These technologies are mainly categorized as follows: the ground-based approaches to active debris removal and the passive de-orbit systems which are deployed at the end of life. For the ground based ap- proaches, high powered laser systems can remove debris in the low earth orbit. In the passive de-orbit systems, inﬂatable balloons, inﬂatable tube membranes, suspendable tethers etc. are all simple and easily deployable drag systems that can hasten the speed of debris de-orbiting process [6].

1.4 Results

We use a system of ordinary differential equations to simulate the environ- ment of the space from qualitative and quantitative perspectives, with ODR present or not. The results of modeling generate approximate amounts of debris and remaining spacecraft based on their initial numbers. We concluded that O- DR can help eliminate the debris while protecting the spacecraft effectively. The proﬁts of different methods are calculated by subtracting the ODR systems’ cost from the total value of protected satellites. Next we use AHP (Analytic Hierar- chy Process) to evaluate the performance of different ODR systems in regards to our pre-set essential factors. The result indicates the SpaDE ODR system to be the most favorable one. Our results show that given the best model, the de- bris removal industry will not make money in the current situation, but will be proﬁtable in more than 50 years from now on.

2 Models

2.1 Overview

The space debris removal problem encompasses a multitude of factors. To simplify the description, we concentrate on the numerical perspective and study dynamics of the number of satellites and space debris orbiting the earth.

Assumptions and Justiﬁcations

• There are only two types of satellites: in high orbit or low orbit.

• All the destructive space debris is the same and evenly distributed around the earth.

• The collision between a satellite and a debris is assumed to be a catastroph- ic one in which the satellite is destroyed into pieces. The number of debris generated in one collision is constant, regardless of the sizes of different spacecraft. The debris is of the same size.

2.2 Symbols

• t: time (measured in years)

• Sh: satellite population in high orbit

• Sl: satellite population in low orbit

• D: debris population

• β: collision coefﬁcient between satellite and debris

• α: number of satellites launched per year

• γ : number of satellites expired per year

• ρ: proportion of retired satellites that turn into space debris

• N: number of fragments when a satellite crashes

• λ: natural growth rate of space debris

2.3 Establishment

Assumptions and Justiﬁcaitons

• The earth is a close system. There is no space junk from outer space that enters into this system.

• The debris will not decompose nor spontaneously fall into the earth’s at- mosphere. It will always orbit the earth unless external impact exists.

• Among all types of space debris, we only concentrate on the relatively large objects, since there are hundreds of millions of debris in the space and not all of them are deadly to the satellites.

(1) The satellite part

The change of satellite population can occur in three ways: new satellites that launched into space, retired satellites and satellites destroyed in the colli- sion. The statistics show that in the past several decades since the launching technology became mature, the numbers of satellites launched each year are not remarkably different. So we treat the number launched α as constant and so is the number of retired satellites γ. Therefore, by introducing a collision co- efﬁcient β, the dynamics of satellite population in high and low orbit can be depicted as

dSh dt = −βhDSh + αh −γh (2.1)

dSl dt = −βlDSl + αl −γl (2.2)

(2) The debris part

Similar to the analysis above, we assume that space debris is created in three ways: the collision between satellite and debris, defunct satellites and natural growth rate of debris (caused by the collision among debris itself or boosters and dead spacecrafts). For simplicity, we also assume the number of fragment produced in collision to be the same, denoted by N, and a ﬁxed percentage of satellites transformed into space junk in the process of dying, denoted by γ. We also hold the annual growth rate of space debris λ to be constant. So the dynamics of the debris population can be described as

dD dt = (βhSh + βlSl)DN + (γh + γl)ρN + λD (2.3)

By now we have constructed a system of ordinary differential equations with initial values dSh  dt = −βhDSh + αh −γh         dSl   dt = −βlDSl + αl −γl        dD dt = (βhSh + βlSl)DN1 + (γh + γl)ρN2 + λD         Sh(0) = Sh0, Sl(0) = Sl0         D(0) = D0 

(3) Test the Model

We use the data found on websites to test the validity of our model. Based on the initial values and the value of parameters, we can predict the number of satellites and debris in the future and see the consequence of increasing space debris.

• Sh: 0.482 (measured in thousand, according to Satellite Database[1])

• Sl: 0.589

• D: 21 (the relatively large objects, from Wikipedia)

• βh: 0.0000247 (calculated from the collisions occurred in recent years)

• βl: 0.0001213

• αh: 0.034 (according to Satellite Database[1])

• αl: 0.112

• γh: 0.027 (according to Satellite Database[1])

• γl: 0.086

• ρ: 0.1 (calculated from Spacecraft Encyclopedia[10])

• N1: 1 (in consideration of small and big collision)

• N1: 0.5

• λ: 0.05 (from Wikipedia)

(4) Analysis and Conclusions

From the graph we can see the satellite population reaches its peak around 50th years in the future. Satellite population in low orbit grows faster in the next 40 years and gradually decreases with few satellites left in the orbit. Similarly, the satellite population in high orbit gradually drops to zero at a relatively small rate while the debris grows exponentially.

The result of our model is consistent with the Kessler syndrome [Kessler 1978], which means that the density of the objects around the earth will become so high in the future that the resulting debris cascade could make prospects for long-term viability of satellites in low earth orbit extremely low[Wikipedia]. The result also suggests that mitigating measures should be taken to restrict the in- crease of debris.

2.4 Model II

The model in the last section shows that when there is no removal measures, ”wandering” debris will continue to propagate through collisions, launches, ex- plosions and the expiration of active satellites. With each passing day the risk of damage to active satellites increases. Therefore, to make sure satellites can survive in the next few decades, mitigating measures are indispensable.

First we aim at analyzing the effects the cleaning system has on the earth’s orbit. We assume that the system is composed of several cleaning machines operating in the space to de-orbit or recycle the objects surrounding the earth. Additionally, we’re not going to focus on different types of ”cleaners” in this section. All the cleaners launched into space are treated as identical. In this way, we can introduce the variable W and θ to denote the cleaner population and its cleaning efﬁciency. Similarly to satellite, the cleaner also face the risk of collision with space debris, or undergo machinery damage in the process of working. Let δ denote the machinery damage rate.

(1)Additional assumptions

Without loss of generality, we have to make additional assumptions as fol- lows:

• The machines are not fully occupied so that the number of debris removed per unit time is positively correlated with the debris population in the s- pace.

• The more debris the machine has removed, the larger the possibility of machinery damage, which means that the damage frequency is relevant to the debris population.

• We neglect the debris produced by the cleaners themselves since the num- ber of cleaners is very small compared to the satellite population, and the collision with debris can be ascribed to machinery damage.

(2)Establishment & Test

By introducing ODR, the dynamics of satellite and debris population are un- doubtedly different from that in the last section. Based on Model I, the effect of launching cleaners can also be represented in differential equations. We need to notice that ODR has no direct impact on the satellite population. It affects the satellite population by removing the debris in the space, thus the differen- tial equations on the satellite part remain unchanged. The debris removed per unit time can be calculated as θWD, so on the debris part, equation (2.3) can be modiﬁed as

dD dt = (βhSh + βlSl)DN + (γh + γl)ρN + λD −θWD (2.4)

Considering the machinery damage of the cleaners, the cleaner population can be depicted as dW dt = −δWD (2.5)

So the system of ordinary differential equations of introducing ODR is

 dSh dt = −βhDSh + αh −γh         dSl    dt = −βlDSl + αl −γl         dD    dt = (βhSh + βlSl)DN1 + (γh + γl)ρN2 + λD −θWD 

  dW    dt = −δWD          Sh(0) = Sh0, Sl(0) = Sl0         D(0) = D0 

A diagram can be drawn to illustrate the structure of the system.

Based on the value of parameters, we can also simulate the satellite and de- bris population in the future and see the effect of ODR. The parameters related to cleaners are:

• θ : 4 (calculated from the research on laser base[11])

• W :0.02 (set according to research on laser base[11])

• δ : 0.0011905 (calculated from the research on laser base[11]) Running the model by MATLAB, the development of this system is shown in the following ﬁgure.

(3)Analysis and Conclusions

With the existence of ODR, we can see that the satellite population and debris population remain at the high level for more than 100 years. Compared to the ”do nothing” system, ODR has controlled the amount of debris to some extent and assured that more satellite can survive in the next few decades. From the ﬁgure we can also see that in the long run, the debris population still grows exponentially,. This may due to the fact that the cleaner will all eventually be damaged and the growth of debris is thereafter unrestricted.

The result of this model also shows that it is wise for us to launch cleaners continuously in order to keep the debris at a low level. Here we don’t take the speciﬁc number of cleaners into account; nevertheless, there exists the problem of how many cleaners should be launched, and we’ll show it in the later part.

3 Model Extension

3.1 What if launching different cleaners?

(1)Analysis of the Problem In the last section we assume that all the debris is the same and there is only one type of cleaner that has the same cleaning efﬁciency. While in fact, ”no two snowﬂakes are the same”. The sizes of space debris are unlikely to be identical. We assume that there are two kinds of debris: large and small, denoted by D1 and D2, and each has the same probability to hit the satellite. However, because of the difference in size, the efforts needed to de-orbit them are not the same.

Let p1 and p2 denote the removal coefﬁcient ( i.e.efforts needed) for each type. Based on the second model, the number of debris removed per unit time is −pθWD. Note that in the last section we do not take this parameter into ac- count since we normalize average value p = 1. Thus we have 0 < p1 < 1 and p2 > 1.

Now we consider the specialization in cleaners. The heavy cleaners have the higher power and light cleaners have lower power. Our goal is to see whether this strategy is more effective in the removing system since both types are de- signed to have different functions. So the cleaning efﬁciency θ of these two types are different, θ1 > θ2 ( 1 for heavy and 2 for light). Again we assume the each size of debris has the same distribution in the space. Then with the same damage rate, the system of ordinary differential equations with specialization in cleaners is

dSh  dt = −βh(D1 + D2)Sh + αh −γh         dSl   dt = −βl(D1 + D2)Sl + αl −γl          dD1   = (βhSh + βlSl)(D1 + D2)N1 + (γh + γl)ρ1N2 + λD1 −(θ1W1 + θ2W2)p1D1   dt   dD2   = (βhSh + βlSl)(D1 + D2)N1 + (γh + γl)ρ2N2 + λD2 −(θ1W1 + θ2W2)p2D2   dt       dW1    = −δW1(Dl + D2)   dt       dW2   = −δW2(Dl + D2)   dt

Also, we can use a diagram to illustrate the structure.

(2)Test and Conclusions

• W1: 0.005 • W2: 0.015

• D1: 5000 ( consistent with the current distribution )

• D2: 15000

• p1: 0.7 ( larger debris are difﬁcult to remove )

• p2: 1.2

• θ1: 10 ( heavy cleaner has higher cleaning efﬁciency )

• θ2: 3

• ρ1: 0.25 ( consistent with the current distribution )

• ρ2: 0.75

The result is shown in the following ﬁgure.

We can see from the ﬁgure that the specialization in cleaner indeed has some- what positive effect on restricting the debris. The peak of the satellite population occurs in more than 100 years in the future, which is later than that in Model II, and the maximum is also larger. However, this result is not surprising since the specialization in cleaner may indeed increase the efﬁciency so that the overall debris population grows slower than that with identical cleaners.

Practically speaking, it is better for us to design machines for special use or aimed at different types of debris. A combination of different removing methods may also be the best choice in cleaning space debris.

3.2 Is there a commercial opportunity?

3.2.1 The Proﬁt Motive

When it comes to whether a commercial opportunity exists in the world, proﬁt is undoubtedly the most important factor that a ﬁrm will care about. No agency of a space-faring nation will want to commit huge amounts of funding for the removal of space objects. Here for private companies, there is a question: How can anyone make money with space debris? Space trash has little value compared to the tens or hundreds of millions of dollars needed to retrieve it. However, practical proposals state that an insurance premium can be imposed to ﬁnance the debris removal measures. To ﬁnd the proﬁt of the company, we need to make several assumptions in this industry:

• All the countries invest in the removal system and they share the same protection, since the governments of space-faring nations would beneﬁt by allowing a private-sector company to remove debris.

• We believe that in the long run, the income from cleaning the debris must equal to the value the ﬁrm has produced, and the value is measured in the number of satellite the ﬁrm has protected.

• All the ﬁrms in this industry are identical. We can determine whether a commercial opportunity exists according to whether this industry is at- tractive enough.

Based on these assumptions, we can measure the proﬁt by subtracting the cost from its income. Note that the cost is composed of three parts: research and development, production, maintenance cost. So we can compare the cost and revenue of the total industry to see if this industry is proﬁtable now or in the future.

3.2.2 The Results

The proﬁt of ODR can be calculated as

π = (N2(t) −N1(t)) ∗V

where N2/N1 is the satellite population with/without ODR and V denotes the average value of a satellite. C(t) is the cost function related to time.

Here we set number the cleaners W at the same level with that in Model II. Additionally, about $100 - 200 million per year is required for maintenance [9]. We assume an additional cost of $20 billion is required during the research and $2 billion is required to produce and launch the cleaner. The replacement cost for the approximately 1071 active satellites in orbit today is estimated to be around $109 million [ESA/ESOC, 2013]. We thus set V = 0.101.

It’s not hard to ﬁnd that in the near future the research cost is so high that it’s impossible for the ﬁrms to make proﬁts. When t = 50, from the result of Model 1 and Model 2 , N1 = 1935, N2 = 2679, π(50) is calculated to be $75.14 billion. C(50) = $80 billion. C(50) > π(50). So in the 50th year, the company will only suffer a little deﬁcit.

When t = 60, the calculation shows that N1 = 1771, N2 = 2877. In the 60th years, π(60) is calculated to be $111.7 billion, C(60) = 84 billion. So C(60) < π(60) , the ﬁrms can make a proﬁt after 50 - 60 years.

Therefore, our calculation shows that the debris-cleaning industry will be proﬁtable in future. So there indeed exist opportunities for private ﬁrms several decades after. But in the near future, it may be very risky for ﬁrm to enter the industry because the costs are too high.

3.3 What if recycling the debris?

We now consider the fact that not all the debris is useless. We use machine to recycle the debris and extract proportional value from the debris. Again we assume that debris is identical. Because of the effort to recycle the debris, the efﬁciency of the cleaner is obviously lower in terms of the number removed. Assume that in order to directly collect debris, the efﬁciency becomes half of its original value. Then the satellite and debris population are shown in the ﬁgure.

Similarly, in the 60th year, the numbers of satellites No and Nr are 2,877 with ODR and 2,046 with recycle system. The debris population is 28.95 thousand without recycle and 168 thousand with recycle system. If we can ﬁnd one object useful among a thousand, the relative value of recycle in the next 60 years is calculated as (No −Nr) ∗V −0.001V (Do −Dr) < 0.

This means that the proﬁt made from recycle is less than just removing them from space. More speciﬁcally, the debris are so useless that it’s not wise for us to recycle them in the near future.

4 Sensitivity Analysis

(1) Collision rate: β

The collision rate between the debris and spacecraft is calculated according to the data available from the space agency. In the current situation, collision takes place nearly once per year, which is a comparatively small probability event. To make reasonable changes, we vary this data by a multiplication of 2 and 0.5 to test the inﬂuence of collision rate on the result.The ﬁrst ﬁgure shows the result when β is decreased to 0.5 times. The second shows the result when β doubles.

We can see from the ﬁgures that when β is smaller, satellites reach a higher peak at a postponed time and a lower peak appears at an advanced time with bigger β. These observations are in accordance with our hypothesis. Further- more, the values of peaks do not change much with different β.

(2)Numbers of Fragments Produced : N

The amount of debris produced in a collision is estimated according to the current data reported by detectors in space. This data is inevitably inaccurate since many pieces are lost because of the inability of tracing technique. We vary the amount of generated debris in one collision from the original 1000 to 1500, even 500,000 pieces. Results show that this factor exerts little inﬂuence on the ﬁnal predicted number of spacecrafts.

In Model 2, the change of collision rate and the amount of debris produced in one collision has no speciﬁc effect on the cleaner factor. Results show that these two elements exert the same inﬂuence on the predicted number of spacecraft as they do in model 1.

5 Evaluation Model

5.1 Metrics

Generally, a space debris cleaner can be evaluated from 5 aspects, including cost, cleaning efﬁciency, production cycle, disturbance and life expectancy.

(1)Cost

Undoubtedly, the total cost of a cleaner accounts for the majority percentage in the cleaner assessment. The cost consists of researching expense, produc- ing cost and launching price. The researching expense is directly related to the number of qualiﬁed published paper pi in a speciﬁc time period, since the more papers published, the larger amounts of money have been invested into the re- searching process. And in the aspect of producing, the total cost cpi approxi- mately equal to the cost of the main components. As to the launching expense, it is positively correlated to the weight z of the object.

Ci = pi + cpi + ε ∗zi

(2)Cleaning Efﬁciency

Cleaning efﬁciency refers to the number of debris it can deal with in a speciﬁc time period. Ei = n t

(3)Production Cycle

We divide the production cycle into two parts. One is the time it takes to building the main part of the cleaner, another part is the time to build the left part. According to the critical path theory, the producing time of the main part contribute the majority proportion of the whole production cycle.

Ti = tmaini

(4)Disturbance

Different cleaners may cause various environment disturbance. There is a degree for different cleaners that disturb the normal functional spacecraft while coping with the space debris.

(5)Life Expectancy

Life expectancy deﬁnes the life span of the cleaner under normal condition.

5.2 Target Cleaner Selection

Here we collect data and determine the rank of four cleaners, they are space- based laser radiation, SpaDE (Space Debris Elimination) program from NASA, space-based water jets, tethered space tug. These four approaches are frequently discussed in papers or websites.

Laser radiation is aimed at ablating the objects and provides an impulse to the debris causing it to de-orbit. SpaDE is a method that will push satellites into a lower orbit by using air bursts within the atmosphere. Space-based water jets uses water to make the debris deviate from its orbit. The tethered system is also a promising technology to de-orbit the space debris. From these alternatives, we can build a model to choose the most preferable approach.

5.3 Analytic Hierarchy Process ( AHP )

While evaluating different aspects of those cleaners, all the criteria need to be considered and we must avoid subjective judgment. So we prefer to use AHP to make the decision.

(1)Obtain the Criteria Weight Vector

Determine the pairwise-comparison criteria judging matrix. In AHP, 1-9 method are used to represent the relatively importance between criteria. Con- structing the judging matrix A = (aij)n∗n, each element must satisfy following constraints:

aij > 0 Goal Criteria Alternatives

Rank of the Cleaners Cost Laser Efﬁciency SpaDE Production Cycle Water Jet Disturbance Tethered Tug Life Expectancy

aii = 1 aij = 1 aji

Calculate the eigenvalues and the corresponding eigenvectors. and Select the eigenvector u = (u1, u2, , un)T with the maximum eigenvalue λmax as the criteria weight vector and normalizing it as ui u′ i = Pn j=1 uj

(2)Applying consistency checking

• CI = λmax −n n −1

• Coincidence indicator table:

n 1 2 3 4 5 6 7 8 9

RI 0 0 0.58 0.90 1.12 1.24 1.32 1.41 1.45

We calculate the consistency ratio by CR = CI RI , if the calculating ratio is less than 0.1. Then we think the judging matrix is qualiﬁed and the eigenvector with the largest eigenvalue can be used as the weight vector; If not, the judging matrix need to be modiﬁed until the less-than condition is satisﬁed.

Determine the pairwise-comparison judging matrix between four cleaners in the respect of the ﬁve criteria. Repeating the above procedure and get ﬁve weight vectors which can be treated as relative grade vectors.

(3)Analysis and result

Criteria Judging matrix   1 1 5 7 2 1 1 7 5 1   1/5 1/7 1 1/5 1/9 A = 1/7 1/5 5 1 1/3 1/2 1 9 3 1

The corresponding criteria weight vector is u = (0.3522, 0.2895, 0.0356, 0.0841, 0.2386). The grade vectors of four alternatives in the respect of ﬁve criteria is shown in the following ﬁgure.

The ﬁnal score of four alternatives are

Rank Method Score

1 SpaDE 0.3812 2 Water Jet 0.2778 3 Laser 0.2279 4 Tethered Tug 0.1131

The result of AHP shows that cost plays a signiﬁcant role in evaluating the candidate space debris cleaner followed by cleaning efﬁciency and SpaDE get the highest score in the evaluation process and have less variation with all crite- ria.

(4)Sensitivity Analysis

We analyze how the pairwise-comparison matrix will inﬂuence the ranking of candidate space debris cleaners. According to our model currentlyit is very hard for the de-debris service company to make a money. So when developing a space debris cleaner, the most signiﬁcant factor must be taken into consideration is the cost. Suppose in the future when de-debris business is far more proﬁtable, the cost of the cleaner plays a less signiﬁcant role in assessing one cleaner. So we modify the pairwise-comparison criteria matrix as:

  1 1/3 3 1/5 1/2 3 1 5 1/3 1   1/3 1/5 1 1/9 1/5 A = 5 3 9 1 3 2 1 5 1/3 1

And the corresponding weight vector is U = (0.0920, 0.2012, 0.0396, 0.4841, 0.1831)

The result becomes:

Rank Method Score

1 SpaDE 0.4834 2 Laser 0.2639 3 Tethered Tug 0.1280 4 Water Jet 0.1248

The result is quite different from the original one, so the selection of the cri- teria matrix has considerable inﬂuence on the ﬁnal result.

5.4 A proper approach to avoid collision

(1)Assumptions

• The collision avoidance strategy can only be applied on trackable debris and for the minor debris we make the assumption that they will not cause catastrophic damage and we can adopt special protecting-shield to limit the damage.

• Suppose the method we proposed can be achieved regardless of the tech- nical difﬁculties.

(2)Model Due to the complicated environmental situation of the space, signiﬁcant un- certainties exist in the rotating orbit of trackable debris. Before we can build a collision avoidance system, position measurement of the space objects is needed. We need to obtain the rotating orbit information of both debris and functional spacecraft so that we can make the conjunction analysis. Here is our method, combining the Box method and the collision probability method:

Deﬁne a box area Vo of each functional spacecraft. The length, width and height for this box area are lo, wo, ho respectively. This box is deﬁned as ”outer box”. Based on the space object position measurement, predictions can be made about whether any debris will pass through this box. If debris exists, the control center will activate the level-one plan, keeping on surveilling the debris and offering detailed information.

Then calculate the position of both target spacecraft and debris based on the tracking data. Here r is the orbit vector of this spacecraft or debris while e is the error vector of the position of spacecraft or debris caused by environmental disturbance.

• The position vector of spacecraft: Rs = rs + es.

• The position vector of debris: Rd = rd + ed.

• Calculating the predicted minimum distance between spacecraft and de- bris.

md = |Rs −Rd|

If the minimum distance md is within the threshold , level-two plan will be activated. So it then adjusts the velocity of the spacecraft to change its orbit to avoid collision.

• Deﬁne another box area called inner box whose size is li, wi, hi respectively.

• If the predicted data indicates that the debris will across the inner box, then the level-three plan, which is speciﬁed for the serious situation, will be activated. Much more emergent measurements will be adopted.

• Based on the value of the spacecraft, we can classify the spacecraft into three categories: low value, commercial, high value. For different type of spacecraft, different box size and threshold is deﬁned.

6 Strengths and Weaknesses

6.1 Strengths

• We apply scientiﬁc methods in approximating our model parameters. Such as the impact into spacecraft structure formula

• Our model of the space debris removal process takes various factors into account.

• Our debris removal models are insensitive to parameter changes.

• We made extensions to our proﬁt model that takes the additional debris recycling beneﬁts into account.

• We evaluate the ODR system in basically two scales: the pure proﬁts aspect and the overall performance aspect

• We come up with a new method to perform collision avoidance which takes advantage of existing alternatives, reducing costs and enhancing per- formance.

6.2 Weaknesses

• The exponential model simulating debris growth may be unrealistic.

• The categorization of the earth orbits is rough, with only LEO and GEO separated.

• The value setting in pairwise-comparison criteria matrix of AHP is a little sensitive to parameters value.

7 Conclusions

According to our model, if no action is taken, the turning point of the debris increasing and number of collision will come in few decades. On the contrary, if human being start to send space debris cleaner from now, the appearance of the turning point will be postponed signiﬁcantly. Although the situation is emer- gent, the collision rate of spacecraft and debris is still at a low level currently. So, it is hard for one private company to make a money through ODR business in the short term. Moreover, our model predict it will not be proﬁtable until at least 50 years later.

Our cleaner assessment model is based on Analytic Hierarchy Process, the pairwise-comparison criteria matrix deﬁned including 5 criteria: cost, cleaning efﬁciency, production cycle, disturbance and life expectancy. In the paper we discuss four speciﬁc type including: space-based laser, SpaDE, water jet, teth- ered space tug. And it turns out SpaDE,conducted by NASA, is the best alterna- tive.

As mentioned above that ODR business will not make proﬁts in recent years, so collision avoidance method is preferred currently.We combine the strength of two separate collision method and build a new collision avoidance system. This method calculating the probability of collision in two ways based on the data of the trackable space object.

Executive Summary

Space debris is becoming increasingly alarming as nations worldwide are sending more satellites into space. Issues concerning this problem deserve more attention and proper measures need to be taken. Currently there are two kinds of approaches that can be adopted: ”doing nothing” or concentrate on the problem now. The ﬁrst approach will not cause obvious harm at present but future generations are at a risk of losing the space resources. The second approach is more advisable but a considerable cost is needed.

In order to know what we should do in this complex situation, we ﬁrst construct several models to study the effect of space junk on several basic assumptions. From the analysis of the results, we ﬁnd that the space will only contain space junk in the next few decade. We also ﬁnd that with the ODR(Orbital Debris Removal) system,it will take about 50- 60 years for the numbers of satellites to decrease. Additionally, launching specialized cleaners may be a better idea.

Our calculations also show that it is hard for a private company to make proﬁt in the near future, but there truly exist opportunities to make money several decades after. According to our model, the debris threat now is at a low level and the increasing rate of debris is at a low level. But the turning point will occur after about 50 years when debris start to grow exponentially and collision between spacecraft and debris become increasingly frequent. At that time, ODR may begins to make money through ﬁnance from government or companies that own satellites.

We construct another model to evaluate different types space debris cleaner. This model takes ﬁve properties of the cleaner into consideration including: cost, cleaning efﬁciency, production cycle, disturbance and life expectancy. Each of these criteria is assigned with different weights. We treat Cost as the most important factor, followed by cleaning efﬁciency, life expectancy, disturbance, production cycle. And the result is shown is the following table:

We think SpaDe is the best approach considering the overall performance. The is determined based on the fact that cost is the main obstacle in removing space debris now. Removing space debris can make proﬁts in future and contribute positively to the outer space environment. Therefore we strongly recommend the government ﬁnance the researches in this ﬁeld to achieve more beneﬁts both environmentally and economically.
