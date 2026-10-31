2015 Mathematical Contest in Modeling (MCM/ICM) Summary Sheet How to Eradicate Ebola?

The breakout of Ebola in 2014 triggered global panic. How to control and eradicate Ebola has become a universal concern ever since.

Firstly, we build up an epidemic model SEIHCR (CT) which takes the special features of Ebola into consideration. These are treatment from hospital, infectious corpses and intensified contact tracing. This model is developed from the traditional SEIR model. The model’s results (Fig.4,5,6), whose parameters are decided using computer simulation, match perfectly with the data reported by WHO, suggesting the validity of our improved model.

Secondly, pharmaceutical intervention is studied thoroughly. The total quantity of the medicine needed is based on the cumulative number of individuals CUM (Fig.7). Results calculated from the WHO statistics and from the SEIHCR (CT) model show only minor discrepancy, further indicating the feasibility of our model. In designing the -c Means Clustering Algorithm and delivery system, we apply the weighted Fuzzy select 6 locations (Fig.10, Table.2) that should serve as the delivery centers for other cities. We optimize the delivery locations by each city’s location and needed medicine. The percentage each location shares is also figured out to facilitate future allocation (Table.3,4). The average speed of manufacturing should be no less than 106.2 unit dose per day and an increase in the manufacturing speed and the efficacy of medicine will reinforce the intervention effect.

Thirdly, other critical factors besides those discussed early in the model, safer treatment of corpses, and earlier identification/isolation also prove to be relevant. By varying the value of parameters, we can project the future CUM . Results (Fig.12,13) show that these interventions will help reduce CUM to a lower plateau at a faster speed.

We then analyze the factors for controlling and the time of eradication of Ebola. For example, when the rate of the infectious being isolated is 33% - 40%, the disease can be successfully controlled (Table.5). When the introduction time for treatment decreases from 210 to 145 days, the eradication of Ebola arrives over 200 days earlier.

Finally, we select three parameters: the transmission rate, the incubation period and the fatality rate for sensitivity analysis.

1. Introduction

1.1. Problem Background

Ebola virus disease (EVD), formerly known as Ebola haemorrhagic fever, is a severe, often fatal illness in humans. The current outbreak in West Africa, (first cases notified in March 2014), is the largest and most complex Ebola outbreak since the Ebola virus was first discovered in 1976. There have been more cases and deaths in this outbreak than all others combined. It started in Guinea and later spread across land borders to Sierra Leone and Liberia[1]. The current situation in the most affected countries can be seen clearly by the latest outbreak situation graph released by the World Health Organization (WHO).

http://www.cdc.gov/vhf/ebola/outbreaks/2014-west-africa/distribution-map.html

Ebola was first transmitted from fruit bats to the human population. It can now spread from human to human via direct contact with the blood, secretions, organs or other bodily fluids of infected people, and with surfaces and materials contaminated with these fluids. Burial ceremonies can also play a role in the transmission of Ebola because the virus can also be transmitted through the body of the deceased person[1].

Control of outbreaks requires coordinated medical services, alongside a certain level of community engagement. The medical services include rapid detection of cases of disease, contact tracing of those who have come into contact with infected individuals, quick access to laboratory services, proper healthcare for those who are infected, and proper disposal of the dead through cremation or burial[1],[2]. There are lots of different experimental vaccines and drug treatments for Ebola under development, tested both in the lab and in animal populations, but they have not yet been fully tested for safety or effectiveness[3], [4]. In the summer of 2014, the World Health Organization claimed fast-tracking testing was ethical in light of the epidemic[4]. In fact, the first batch of an experimental vaccine against Ebola have already been sent to Liberia in January 2015. According to the Dr Moncef Slaoui of British production company GlaxoSmithKline, the initial phase is encouraging and encourages them to progress to the next phases of clinical testing[5].

1.2. Previous Research

The analysis of the spread of epidemic has been a universal concern. Moreover, there have been a lot of research into the studies of the 2014 Ebola epidemic in West Africa[6]. For the spread of the disease, which is considered as an important factor in eradicating Ebola, there are a lot of previous research that can facilitate our understanding of the disease.

For example, Fisman et al. used a two-parameter mathematical model to describe the epidemic growth and control[7]. Gomes et al. researched into the risk of Ebola’s international spread along with its mobility data. His research reached a conclusion that the risk of Ebola’s international spread to outside Africa is relatively small compared to its expansion among the West African countries[8]. The Centers for Disease Control and Prevention used the traditional SIR model to extrapolate the Ebola epidemic and projected that Liberia and Sierra Leone will have had 1.4 million Ebola cases by Jan. 20, 2015[9]. Chowell et al. used the SEIR model and studied the effect of Ebola outbreaks in 1995 in Congo and in 2000 in Uganda[10]. The SEIR model takes the state of exposure into consideration, which is a special feature of Ebola because exposure to the virus will make individuals a lot more easily to be infected. Based on the SEIR model of Chowell et al[10], Althaus developed a model where the reproduction number is dependent on the time[11]. Valdez et al. developed a model and found that reducing population mobility had little effect on geographical containment of the disease and a rapid and early intervention that increases the hospitalization and reduces the disease transmission in hospitals and at funerals is the most important response to any possible re-emerging Ebola epidemic[12].

1.3. Our Work

We are asked to build a realistic, sensible, and useful model to optimize the eradication of Ebola or at least its current strain. Our model should not only consider the spread of the disease, the quantity of the medicine needed, possible feasible delivery systems, locations of delivery, speed of manufacturing of the vaccine or drug, but also other critical factors that we consider to be necessary.

To begin with, we searched a large number of papers that discuss the spread of Ebola to help us deepen the understanding of the problem. Chowell et al. provided a large amount of background information and their work[6] served as an important introduction. We found that a few of the papers used the traditional epidemic model to predict the transmission of the disease such as the SEIR model used by Althaus[11] to estimate the reproduction number of the virus during the 2014 outbreak. Therefore, we also applied the SEIR model in the early stage to predict the spread of Ebola. Later, we found out that the Ebola virus has some specific feathers that also needed to be considered and that are, the potential transmission threat posed by the highly infectious corpses, the improved infection control and reduced transmission rate if patients can be treated in hospitals, and the powerful intervention method: contact tracing. After taking all these critical factors into consideration, we improved our original epidemic model.

Next, we deeply analyzed the pharmaceutical intervention. We first used the statistics provided by WHO[24] to help figure out the quantity of the needed medicine. We also used our improved model to predict the number of the patients and needed medicine in Guinea, Sierra Leone and Liberia. Two parameters: 1) the current CUM and 2) the increasing rate of the disease  to cumulative number of patients p decide the quantity of the medicine are set up as criteria. After the quantity of the medicine had been calculated, we sorted the affected cities of the three countries into -c Means several groups to determine the location of delivery. We applied the Fuzzy Clustering Algorithm and eventually selected 6 delivery points. These delivery points will be in charge of storing the medicine and transporting them to the set of cities surrounding them. Later, we took the speed of manufacturing and the efficacy of medicine into consideration and tested how these parameters could affect intervention.

We then considered other important factors that would help the eradication of Ebola: 1) safer treatment of corpses and 2) intensified contact tracing and earlier isolation.

After finishing analyzing all the relevant factors, we reached our final conclusion and predicted a time for Ebola’s eradication. In the last stage, we provide a non- technical letter for the world medical association to use in their announcement of inventing a new drug to stop Ebola and treat patients whose disease is not advanced.

2. General Assumptions

 The population of the new-born are not counted in the total population.

 An individual who is exposed enters the incubation period and is not yet infectious.

 Recovered patients will not be infected again.

 Medicine are only provided in hospitals.

 Every location inside Guinea, Sierra Leone and Liberia can be selected as the delivery center and delivery routes between cities are straight lines.

 Medicine and vaccines can be delivered across borders.

3. Notations and Symbol Description

3.1. Notations

Susceptible individual[12]: A person with a clinical illness compatible with EVD and within 21 days before onset of illness, either:

 a history of travel to the affected areas OR  direct contact with a probable or confirmed case OR  exposure to EVD-infected blood or other body fluids or tissues OR  direct handling of bats, rodents or primates, from Ebola-affected countries OR  preparation or consumption of bush meat from Ebola-affected countries.

Exposed individual[14]: A person who has been infected by Ebola virus but are not yet infectious or symptomatic.

Basic reproduction number[6]: The average number of secondary cases caused by a typical infected individual through its entire course of infection in a completely susceptible population and in the absence of control interventions.

Contact tracing[15]: Find everyone who comes in direct contact with a sick Ebola patient. Contacts are watched for illness for 21 days from the last day they came in contact with the Ebola patient. If the contact develops a fever or other Ebola symptoms, they are immediately isolated, tested, provided care, and the cycle starts again-all of the new patient’s contacts are found and watched for 21 days.

3.2. Symbol Description

Symbol

Description R Basic reproduction number 0 N Size of total population S t ( ) Number of suspected individuals at time t E t Number of exposed individuals at time t ( ) I t Number of infectious individuals outside hospital at time t ( ) H t Number of hospitalized individuals at time t ( ) C t ( ) Number of contaminated deceased at time t R t Number of removed individuals at time t ( ) CUM t ( ) Cumulative number of individuals at time t Transmission rate     , , I H C (outside hospital, inside hospital, by corpses) 1/ Average duration of incubation  Rate of infectious individuals to be identified/isolated Average time from symptoms onset to recovery     , I H (outside hospital, inside hospital) Average time from symptoms onset to death    , I H (outside hospital, inside hospital) Fatality rate    , I H (outside hospital, inside hospital) 1/ Average time until the deceased is properly handled Average number of contacts traced per identified/isolated  infectious individual Probability a contact traced individual (exposed, infectious)     , E I is isolated without causing a new case Ratio of probability that contact traced individual is (exposed, infectious) at time of originating case identification to the    , E I probability a random individual in the population is (exposed, infectious)

4. Spread of Ebola

4.1. Traditional Epidemic Model

4.1.1. The SEIR Model

The transmission of EBOV follows SEIR (susceptible-exposed-infectious- recovered) dynamics and can be described by the following set of ordinary differential equations[10]:

   S t ( ) S t I t ( ) ( ) / N ,      E t ( ) S t I t ( ) ( ) / N E t ( ),       (4.1) I t ( ) E t ( ) I t ( ),     R t ( ) I t ( ),     CUM t ( ) E t ( ),  where:

S t is the number of susceptible individuals at time t, ( ) E t is the number of exposed individuals at time t, ( ) I t is the number of infectious individuals at time t, ( ) R t is the number of removed individuals at time t, ( ) CUM t is the cumulative number of Ebola cases from symptoms onset, ( ) N is the size of total population, 1/ is the average duration of incubation, 1/  is the average duration of infectiousness.

 is the transmission rate per person per day.  is constant in absence of   control interventions. However, after control measures are introduced at time t ,  is assumed to decay exponentially at rate k[16]. That is,     t , 0   (4.2) ( ) t       k (1 )  e t , 0

4.1.2. Outbreak Data

The most seriously affected countries of the 2014 EBOV outbreak were Guinea, Sierra Leone and Liberia. Therefore, we mainly use the SEIR model to estimate the cumulative cases of these three countries. The data needed for the estimation can be obtained from the Centers for Disease Control and Prevention[17] which organizes the information provided in all the WHO situation reports[18] that are from March 1, 2014 to the most recent one on February 4, 2015. The data includes the numbers of reported total cases (confirmed, probable and suspected) and deaths.

To test the validity of the SEIR model on the spread of the 2014 EBOV, we have to compare the actual data of cases and deaths in Guinea, Sierra Leone and Liberia with the calculated data from the model. And we need to first set the value for some of the parameters to carry on the calculation.

Parameter Guinea Sierra Leone Liberia Basic reproduction 1.51 2.53 1.59 number, R 0 Transmission rate without 0.27 0.45 0.28  control intervention 0

Reduce transmission, k 0.048 0.048 0.048

Total population size, N 12,000,000 6,100,000 4,092,310    The basic reproduction number R is given by where 1/ R / 5.61 0 0 day is the infectious duration from the study by Chowell et al[10]. Besides 1/  , 5.61  1/ 5.3 is the average duration of the incubation period from a previous outbreak of the same EBOV in Congo in 1995[10]. Values of other parameters estimates[11] are listed in table 1.

First, by applying the parameters into Equation (4.1), we are able to calculate the estimated number of cases and deaths for these three countries, that is, we will be able to predict the spread of the disease. Then, by comparing the calculated number with the reported data, we will be able to verify the validity of the SEIR model.

4.1.3. Results of the SEIR Model

Actual data of the cumulative numbers of infected cases and deaths are shown in the dotted curve, which are fitted against the data found in the WHO situation reports[18]. March 1, 2014 is defined as Day 1st and one cross in the figure represents one statistics of the cumulative numbers. Calculated data are obtained by solving Equation (4.1).

Guinea

Sierra Leone Liberia

From the figure above, we can see that the model fits the reported data of cases and deaths in these three countries very well. Therefore, SEIR can serve as a good tool for analyzing the spread of the 2014 EBOV outbreak.

4.2. Improved Model

4.2.1. The SEIHCR (CT) Model

SEIR is a basic model for predicting the spread of a disease. However, for the specific case of Ebola, we have to take other important factors into consideration. We mainly considered 1) The potential threat posed by infectious corpses and the provision of hospital care;

2) The involvement of contact tracing (CT).

and indicates the compartmental states and the transition rates among the states.

The traditional model SEIR should be modified[20], [23] and the improved SEIHCR (CT) model can be written as        S t ( ) S t I t ( ) ( ) / N S t H t ( ) ( ) / N S t C t ( ) ( ) / N , I H C          E t ( ) S t I t ( ) ( ) / N S t H t ( ) ( ) / N S t C t ( ) ( ) / N E t ( )  I H C              I t C t E t / N ,  E E           I t ( ) E t ( ) I t ( ) (1 ) I t ( ) I t ( ) I I I I (4.3)             I t C t I t / N ,  I I           H t ( ) I t ( ) (1 ) H t ( ) H t ( ),  H H H H        C t ( ) I t ( ) H t ( ) C t ( ),  I I H H           R t ( ) (1 ) I t ( ) (1 ) H t ( ) C t ( ),  I I H H where:

S t is the number of susceptible individuals at time t, ( ) E t is the number of exposed individuals at time t, ( ) I t is the number of infectious individuals outside hospital at time t, ( ) H t is the number of hospitalized individuals at time t, ( ) C t is the number of contaminated deceased at time t, ( ) R t is the number of removed individuals at time t, ( ) CUM t is the cumulative number of Ebola cases from symptoms onset. ( ) I is the transmission rate outside hospital,  is the transmission rate inside hospital, H  is the transmission rate due to improper handling of deceased, C    I t H t C t        and , I H C N N N  is the total transmission rate, 1/ is the average duration of incubation,  is the rate of infectious individuals to be identified/isolated,  1/ is the average time from symptoms onset to recovery inside hospital, H  is the average time from symptoms onset to death inside hospital, 1/ H  is the fatality rate inside hospital, H I is the average time from symptoms onset to recovery outside hospital, 1/  is the average time from symptoms onset to death outside hospital, 1/ I I is the fatality rate outside hospital, 1/ is the average time until deceased is properly handled.

 is the average number of contacts traced per identified/isolated infectious individual,  is the probability a contact traced exposed individual is isolated without E causing a new case,  is the ratio of probability that contact traced individual is exposed at time of E originating case identification to the probability a random individual in the population is exposed,  is the probability of a contact traced infectious individual is isolated without I causing a new case,  is the ratio probability that contact traced individual is infectious at time of I originating case identification to the probability a random individual in the population is infectious.

When we are to test the validity of the ultimate model, we should compare the calculated data with the actual data, just like what we have done in Section 4.1. The cumulative number of individuals can be obtained by  t t     CUM t ( t ) CUM t ( ) E s ds ( ) . (4.4) t

Reasons for considering corpses, hospitals and contact tracing

Firstly, the provision of hospital care[19] to affected populations could be used as a basis for treating patients and prevent the disease from spreading to a larger scale. Besides, funerals and burials[19] if regulated, will reduce the risk of being infected from improperly handled corpses of infected (contaminated deceased).

Secondly, contact tracing is sometimes regarded as the key factor to stanch the Ebola outbreak in West Africa because if patients can be found earlier in their course of illness, their chances of exposure to family members and community health workers will reduce significantly[21].

Equation (4.3) is improved from the original model SEIR and it is our ultimate model. We name it the SEIHCR (CT) model to illustrate its improvement and differences from the traditional SEIR model. The transition SEIR to SEIHCR (CT) shows how basic model can be greatly improved based on other factors and our own understanding toward this problem.

4.2.2. Choosing Parameters

1. Estimation of

R 0 In order to obtain the reproduction number R , we use a method, following van 0 den Driessche et al[22].

     1 (4.5) R FV , 0

where:

  A denotes the spectral radius of a matrix A, F is the rate of appearance of new infections, V is the rate of transfer of individuals by all other means.

F and V that are corresponded with the SEIHCR (CT) model are            0 SI / N SH / N SC N / I H C            E SI / N SH / N SC N /     I H C            E I I I 0 I I     F , V .      I H H 0     H H          I H C 0     I H          I H C 0     I H

2. Determination of other parameters

,  and  are estimated for the , , The values of the parameters I H C three countries using a least square curve fitting algorithm. The parameters , I,  ,  I and  are borrowed from existing references[11]. , , H I H H The basic reproduction number of the SEIHCR (CT) model is given by the following formula, computed by the next-generation method:

      (4.6) C R I H . 0             (1 ) (1 ) I I I I H H H H

 is constant in absence of control interventions, Among all these parameters, I just as  from the SEIR model. After control measures are introduced at time t   ,  is assumed to decay exponentially at rate k[16]. That is, I     t , I 0   (4.7) ( ) t I       k (1 )  e t , I 0

 Since k and are both related to the efficacy of medicine, we assume their H relationship to be

   k , (4.8) H

where  is assumed to be 3.2 based on experience.

2.1.1. Results of the SEIHCR (CT) Model

Again, we use the dotted line to represent the actual data of the cumulative numbers found in the WHO situation reports[18] and the solid line to represent our calculated number from Equation (4.3) of the SEIHCR (CT) model. The start day of the simulation is defined as Day 1st.

I    N  0.205 0.0001 12,000,000 2015. The parameter values are , , , 0 H   I      0.2 0.224 1/ 32 1/10 1/8 1/ 40 , , , , , , C H I H  k    0 0.03 200 0.18 , , , .

I    N  0.31 0.0001 6,000,000 4th, 2015. The parameter values are , , , 0 H   I   I   0.2 0.125 1/ 30 1/ 21 1/8 1/ 31 , , , , , , C H H  k    0 0.015 160 1/ 5.5 , , , .

I    N  0.30 0.0001 4,100,000 2015. The parameter values are , , , 0 H   I      0.2 0.23 1/ 32 1/10 1/8 1/ 40 , , , , , , C H I H  k    0 0.03 190 0.16 , , , .

These simulations are accomplished by varying combinations of parameters. Comparing these simulations with the ones based on the SEIR model, we can see that we obtain a better fit using the SEIHCR (CT) model, for the calculated data become more smoothly and closely approximate to the actual reported data with the simulation for Sierra Leone being the perfect approximation.

5. Pharmaceutical Intervention

If medicine and vaccines can be available to patients and healthy people, the survival rate of the patients will increase and the situation of affected countries will improve to a great extent. Therefore, the manufacturing and delivery of medicine should remain an important factor in combating Ebola. Our tasks are to calculate the total amount of medicine, design a favorable delivery system and compare the intervention extent of different manufacturing speed and different level of medicine efficacy.

5.1. Total Quantity of the Medicine

5.1.1. Results from WHO Statistics

When medicine are about to be delivered to affected areas of Ebola, apparently, people should first analyze how serious the current situation is to decide the amount of medicine. However, just knowing the present situation is not enough. We should also take the speed of the spread of the virus into consideration because a large speed poses great potential threat. Therefore, when deciding the quantity of the medicine needed, we considered two important factors:

1) The current cumulative number of patients CUM ; p 2) The increasing rate of the disease .

WHO has been releasing a weekly report of newly confirmed cases by district, which represent the sum of new patients[24] . Divide by the duration SUM SUM new new T  7 period T ( in this case since the report is released every week) and we will get the increasing rate of the disease v . Meanwhile, by adding the newly infected cases, we can know the current cumulative patients CUM as well. p By far, we have gathered all the information that we need to calculate the quantity of the medicine. By adding the current cumulative number of patients and the increasing rate of the disease (we place equal weights on these two factors), we can obtain the unit dose of the medicine needed every day D for each city and

   (5.1) D CUM T . p Due to the extremely large amount of statistics for both the number of cities (56 cities) and the duration of the reported data (57 weeks till Feb 1st, 2015), the concrete data and calculated value will not be presented. Instead, we drew a graph that illustrates the units of medicine needed by these three countries from Dec 30th, 2013 to Jan 31st, 2015.

Total Quantity Guinea Liberia Sierra Leone 2500 Unit dose of the medicine needed 2000

1500

1000

500

0

In the figure above, the blue, orange and green curve represents the unit dose of medicine needed per day by patients in Guinea, Liberia and Sierra Leone respectively. The grey area represents the combined doses needed by the three countries altogether.

Since no effective medicine has been developed and distributed in a large scale, the specific dose of medicine one patient needs is nowhere to be found. Therefore, we use the unit dose instead. It also perfectly reflects the quantity of needed medicine.

5.1.2. Results from the SEIHCR (CT) Model

As is mentioned before, there are so many cities that if we calculate every city’s need from the improved model, there will be too much work. Therefore, we only take one city as an example to test the feasibility of our model and we choose the capital of Sierra Leone, Freetown because this city has the largest number of cumulative patients.

The number of patients of Freetown can be calculated from the improved model CUM is obtained, we can also know the increasing rate . Applying these and after p to Equation (5.1) and we will get the quantity of needed medicine per day D .

The left graph in Figure 8 presents the changes of the cumulative numbers with time in Freetown. The grey curve in the right graph represents the every day’s unit dose of needed medicine and the shaded area represents the total quantity of needed medicine. Beside these, we also compared the result from the SEIHCR (HC) model and the result fitted by WHO statistics (the solid curve). We can see that these two results match and the discrepancies are within the acceptable range.

To conclude, SEIHCR (HC) can serve as a feasible model for both predicting the cumulative patients and figuring the quantity of needed medicine.

5.2. Delivery System

The medicine and vaccines of Ebola are manufactured in developed countries like USA and UK. Therefore, it is not difficult to determine the locations that are in charge of loading drugs and vaccines. It is in fact the amount of medicine and the places that the airplanes are headed to are the most difficult part to decide for the delivery system.

Hence, to design the delivery system of medicine and vaccines, we divided our task into two parts:

1) Deciding the locations for receiving drugs;

2) Calculating the amount of drugs these locations need respectively.

5.2.1. Locations of Delivery

To transport the drugs and vaccines to the three most affected West African countries: Guinea, Sierra Leone and Liberia, we should first find several places to store the drugs. These places will also be responsible for delivering medicine to a few places next to them. In other words, we will first find some ‘headquarters’ for storage. Then we will determine from which one of these headquarters other cities will receive the drugs.

We now need to divide these three countries into several parts and we use the -c Means Clustering Algorithm to accomplish this goal. Fuzzy

-c Means Clustering Algorithm: The Weighted Fuzzy

-c Means Clustering Algorithm differs from the traditional The Weighted Fuzzy -c Means Clustering Algorithm in that it considers Fuzzy D , the quantity of medicine k needed by each city.

-c Means Clustering Algorithm is to represent the similarity a The key of Fuzzy point shares with each cluster with a function whose values (memberships) are between zero and one[25]. Each sample will have a membership in every cluster, memberships close to unity signify a high degree of similarity between the sample and the cluster while memberships close to zero imply little similarity between the sample and that cluster[25].

    n n - Y y k , 1,2, N be a sample of N observations in Let R ( k    n dimensional vector, - y y , y , , y dimensional Euclidean space), being a k k 1 k 2 kn     and U be a real c N U u matrix, . U is the matrix representation of the ik partition  iY and the elements satisfy

n   (5.2) u 1  for all , k ik  i 1       we denote the sets of all fuzzy c-partitions of Y by M U | u 0,1 .  fc c N ik

The most popular and well-studied clustering criteria for identifying optimal fuzzy -c partitions in Y is associated with the generalized least-squared errors functional. After weights, the quantity of medicine needed by each city, have been applied, the generalized least-squared errors functional can be written as N c    2 m   min J ( , ) U v D u y v , m k ik k i   k 1 i 1 (5.3)   c c , max s.t.    y y y ,  ki min ki ki max

where      n Y y y , , y R the data, 1 2 N    c number of clusters in , 2 Y c n ,    m weighting exponent, 1 m ,   U fuzzy -partition of , c Y U M , fc D quantity of medicine needed by city k, k     v v v , , v vectors of centers, 1 2 c     v v v , , v center of cluster . i i i 1 i 2 in Optimal fuzzy clustering of Y are defined as pairs   ˆ ˆ U v that locally minimize , m  are well known. For m , if  1 1 ˆ J . The necessary conditions for , for y v m k j all j and k,   ˆ ˆ U v may be locally optimal for , J only if m N    m ˆ D u y k ik k    ˆ k 1 v ,  1 i c , (5.4) i N    m ˆ D u k ik  k 1

 1      2/ m 1   c d        ˆ   ik (5.5) u 1 k N , 1 i c ,     ik d    j 1   jk

where ˆ   ˆ d y v . ik k i Equation (5.2) and (5.3) provide means for optimizing J via iteration by m looping back and forth from these two equations until the iterate sequence shows but small changes in successive entries of ˆU or ˆv . We formalize the general procedure -c Means Clustering Algorithm as follows: for the Fuzzy  0  1) Fix c, m. Choose an initial matrix U M . Then at step k, k, = 0, 1, ..., N. fc  ˆ k 2) Compute means v , i = 1, 2, ..., c with Equation (5.3).

  ˆ     k 1  (k 1) ˆ 3) Compute an updated membership matrix  with Equation (5.4). U u ik  1     ˆ k ˆ k ˆ ˆ  to  k 1 k   4) Compare U U in any convenient matrix norm. If U U , stop.

  1 ˆ ˆ  k k  U U Otherwise, set and return to step 2).

In this case, we set m to be 2. For the value of c , we first decide that the number of headquarters should nether be too large nor too small, which should not only be enough to facilitate the delivery but will also be able to prevent the delivery to be a too demanding job. To set the specific value for c , we found out that J is surely m *c , decreasing with more clusters. When c is increased from 1 to J will decrease m dramatically. However the decreasing pace will slow down when c continues to J with c , the inflection increase. If we draw a curve that reflects the variance of m point should be the ultimate cluster number. The curve is drawn below:

J with c

m

From Figure 9, we can see that choosing 6 clusters and consequently 6 headquarters for all the cities in Guinea, Sierra Leone and Liberia is the ultimate choice, which also corresponds with our initial criterion.

WHO provides explicit data on the number of cases in the three countries’ cities  ˆ k that have patients[24]. Using these data, we are able to calculate means v and  1 ˆ k  to carry on the algorithm. Through iteration, we can obtain U membership matrix our results of delivery locations which are presented below.

In the above figure, the 6 yellow stars represent the 6 ‘headquarters’ that we select to store the medicine and they are labelled from 1 to 6 to facilitate later discussion. The geographical locations for these 6 headquarters are presented in Table 2.

Location 1 2 3 4 5 6 8.4897 N  10.3315 N 10.9935 N 6.9627 N 8.5729 N 10.5202 E Latitude 9.1702W  13.4050W 10.8677W 10.5202W 12.4282W 8.3181W Longitude

There are also 6 sets of dots that are distinguished from each other using 6 different colors. Each set of dots will later receive medicine and vaccines from the headquarter inside them. That is to say, medicine and vaccines will be delivered from the 6 yellow stars to the specific set of colored dots surrounding them.

5.2.2. Amount of Delivery

-c Means Clustering Algorithm and we get the unit dose of Apply the Fuzzy needed medicine for the 6 headquarters. We use 4 weeks as a cycle to reduce the amount of statistics needed to be enclosed. We also add up the unit of dose to see the total amount of medicine needed for a certain period of time. Besides, percentage of the medicine that will be allocated for these 6 headquarters is also calculated to facilitate further delivery.

Every 4 weeks 1 2 3 4 5 6 Sum 2013/12/30 0 0 0 0 0 0 0 2014/1/27 0 0 0 0 0 0 0 2014/2/24 63 3 0 0 0 0 66 2014/3/24 158 99 9 3 0 0 269 2014/4/21 82 15 0 3 6 6 112 2014/5/19 193 145 3 290 12 0 643 2014/6/16 272 35 0 945 37 13 1302 2014/7/14 336 66 21 1719 248 41 2431 2014/8/11 1063 202 0 3038 1208 185 5696 2014/9/8 961 253 20 3208 3546 162 8150 2014/10/6 957 284 24 1345 4669 69 7348 2014/11/3 942 333 173 629 5219 43 7339 2014/12/1 625 672 49 58 4153 0 5557 2014/12/29 116 412 21 3 2059 0 2611 2015/1/26 31 66 9 0 5 0 111 Percentage 13.93% 6.21% 0.79% 27.00% 50.83% 1.25% 100% Apart from the respective amount of medicine needed by the six quarters, we also categorize the needed medicine by country. That is, the specific amount of medicine needed by each country is calculated and their percentage is also figured out to facilitate further allocation.

Every 4 weeks Guinea Liberia Sierra Leone Sum 2013/12/30 0 0 0 0 2014/1/27 0 0 0 0 2014/2/24 64 2 0 66 2014/3/24 259 10 0 269 2014/4/21 91 15 6 112 2014/5/19 313 46 284 643 2014/6/16 165 282 855 1302 2014/7/14 197 907 1327 2431 2014/8/11 851 2856 1989 5696 2014/9/8 1138 3163 3849 8150 2014/10/6 1238 1170 4940 7348 2014/11/3 1445 622 5272 7339 2014/12/1 1346 23 4188 5557 2014/12/29 549 0 2062 2611 2015/1/26 106 0 5 111 Percentage 18.64% 21.85% 59.51% 100.00%

5.3. Speed of Manufacturing

 Since the fatality rate inside hospital depends greatly on the amount of H available medicine, if the speed of manufacturing u is larger than the quantity of the daily needed medicine D , we assume the fatality rate will reach the lowest value  . However, if the speed of manufacturing u is smaller than the quantity of the H 0 daily needed medicine D , demands will not be wholly met and will result in a decrease  satisfy the following equation in the fatality rate. Therefore, u and H   D u      , u D ,    u H 0 (5.6) D H    , u D ,  H 0

 is a coefficient that has a value of 0.7, the lowest fatality rate   where 20% . u H 0 From the calculated doses of medicine before, the average quantity of daily needed u  106.2 medicine is 106.2 unit dose per day. Therefore, if the manufacturing speed     unit dose per day, the fatality rate 20% . However, if the manufacturing H H 0 u  u   is calculated 106.2 50 speed unit dose per day, assume , the fatality rate H to be 57.0%, which is a huge increase..

To conclude, the speed of manufacturing can greatly impact the efficiency of pharmaceutical intervention.

5.4. Medicine Efficacy

 Since 1/ represents the average time from symptoms onset to recovery inside H hospital, this is a parameter that is influenced greatly by the efficacy of medicine. If a medicine has a greater efficacy, the cure time will probably reduce. The relationship  and the efficacy of medicine  is, between H        ln 1 , (5.7)  H  is a coefficient that has a value of 0.206. Therefore, by varying the value of where    (different values of  at the same time), we can test how different values of H H affect the cumulative number of individuals CUM .

  10,15,20,25,30 with H

  In Figure 11, five values have been set to . We can see that a larger , which H H in turn leads to a better medicine efficacy , will lead to a moderate drop in the cumulative number of individuals CUM .

6. Other Important Interventions

6.1. Safer Treatment of Corpses

As can be seen from the comparison of the fitted statistics between the original SEIR model and the improved model that considers infectious corpses, better treatment of corpses remain a positive factor that will potentially help control the spread of Ebola. Since 1/ is the average time until the deceased is properly handled, we can vary the value of  to see if better treatment of corpses can serve as a potential intervention for Ebola.

We set the value of  to be 2, 4, 6, 8, 10 and the value of 1/varies at the same time. The predicted cumulative cases will also vary correspondingly.

 2,4,6,8,10 with

In fact, the curve for predicted cumulative cases descend with the increase in . That is, the highest predicted cumulative number is predicted to occur when   and the lowest curve is corresponding to the condition of 1/ . 1/ 1/10 1/ 2 From the analysis above, we can see that a decrease in the average time before the deceased can be properly handled (1/) is of great importance in trying to control or further eradicate Ebola. The shorter the average time before the deceased can be properly handled is, the slower the virus will spread, leading to a smaller population of cumulative number of individuals.

6.2. Intensified Contact Tracing and Earlier Isolation

As has been defined and given description before,  is the average number of contacts traced per identified/isolated infectious individual, which describes the intensity of contact tracing.  is the rate of infectious individuals to be identified/isolated, which is also a contact tracing parameter.

Varying these two contact tracing parameters  and  while keeping other parameters constant can help us see the effect of intensified contact tracing and identification/isolation.

 0.05  0.1

  0.3 0.2

. The value of  for these four figures are 0.05, 0.1, 0.2,  0,10,20,30,40 with and 0.3 respectively.

Firstly, for each of the four figures, with an increase in , the number of the future cumulative cases is predicted to increase in a decreasing speed. That is, the highest  curve corresponds to the condition of and the lowest curve represents the 0  . Therefore, a larger value of (meaning more contacts being condition of 40 traced) is beneficial to control the spread of the Ebola.

Secondly, comparing all these four figures, we can see that with a small , there are chances that the disease will spread beyond control. For example, the cumulative  0.05 cases under the condition of will increase dramatically and beyond control  . Therefore, the number of contacts traced per identified case  is when 0 important if  is small.

To conclude,  and  are both important figures in trying to control and eradicate Ebola. Intensified contact tracing and earlier identification/isolation can serve as effective tools for the eradication of Ebola.

6.3. Conclusion

From the above discussion regarding safer treatment of corpses, intensified contact tracing and earlier identification and isolation, we can see that these important interventions will help reduce the increasing rate of cumulative number of cases to a lowered plateau to help control and eventually eradicate the spread of the disease. .

Furthermore, we can make a reasonable assumption that if intervention strategies had been applied earlier and in a more effective way, the control and eradication of the Ebola epidemic could have appeared at a much earlier time.

7. Control and Eradication of Ebola

When we are to predict the control and eradication of Ebola, we use the statistics of all the three countries instead of just using Sierra Leone as an example. The reason is, control and eradicate Ebola is of significant meaning to all the affected West African countries. Therefore, it makes sense to take all of them into consideration. The value of I  parameters under this condition vary and new values for the parameters are 0.30 , 0    I     0.009 , 0.125 , 1/ 30 , 1/8 , 1/ 30 , and 1/ 5.5 C H H I k  0.021 .

7.1. How Ebola Can Be Controlled

We first define the control of Ebola to be: 1) the second derivative of the cumulative case number CUM is less than or equal to 0; 2) the derivative of CUM is not 0. That is,   CUM 0, (7.1)   CUM 0.  CUM 0 The critical condition occurs when , which means Ebola is just about to be controlled.

Many factors influence CUM and its growing trend and we mainly consider four of them:

1) , which is the rate of infectious individuals to be identified/isolated, 2) , which reflects the intensity of contact tracing,  3) 1/ , which reflects the cure cycle, H , which is the fatality rate inside hospital. 4) H We vary the value of these four parameters and predict the trend of CUM .

1.  2. 

  3. 1/ 4. H H

  , on controlling spread of Ebola H H

CUM 0 The black line in the blue area means the critical condition when and the blue area represents the critical region where Ebola can be regarded as being controlled. The red area above the blue area means the situation that Ebola will spread out of control. The green area below the blue area is the region where Ebola can be effectively controlled. The remaining grey area is where CUM can be located theoretically but not practically.

The specific values for , , 1/   in different colored regions are and H H listed in Table 5.

  and in different colored region H H Red Blue Green Critical value Graph 1  0.25-0.31 0.31-0.33 0.33-0.4 0.32 Graph 2  5-17 17-26 26-50 20  Graph 3 1/ 1/25-1/7 1/7-1/2.9 1/2.9-1/1.7 1/3.2 H  Graph 4 0.6-0.01 0.01-0.04 0.04-0 0.07 H

From Graph 1, we can see that an increase in  can lead to better control of the disease. This is the same with an increase in (see Graph 2), which suggests an increasing rate of identifying and isolating infectious individuals and an intensified contact tracing practice will both help control the spread of Ebola. From Graph 3 and Graph 4, we can see that though the decreasing of curing cycle and fatality rate can lead to the control of Ebola, it is not that an effective approach.

7.2. When Ebola Will Be Eradicated

If the cumulative case number CUM remains unchanged with time, apparently there are no new infectious individuals, meaning the eradication of Ebola. Therefore, if Ebola is to be eradicated, CUM should satisfy CUM 0. (7.2) Three parameters are especially essential in trying to eradicate Ebola and they are 1) the introduction time of control measures ; 2) the efficacy of the medicine ; 3)  the introduction time of contact tracing . CT By varying their values, we can see how these three parameters ,  and  CT affect the final day for the eradication of Ebola.

The black line in Figure 14 represents the trend of CUM without changing  and the colored lines each correspond to a particular value of . We can see that a small value of , which represents a really fast responding time for introducing control measures, will have a great impact on the eradicating date of Ebola. By comparing the , we can see most significantly, a smaller  will   145 240 two curves of and lead to a tremendous drop in the cumulative number of individuals. Besides, the eradicating date also shortens with a smaller . A decrease from   210 145 to will approximately witness an earlier coming of the final eradicating day by 200 days.

the introduction time of contact tracing c

The black lines in Figure 16 also represent no changing of the medicine efficacy   and the introduction time of contact tracing respectively. The dotted line in CT  these two graphs represent the eradicating points of Ebola. By increasing  and , CT the eradicating points will arrive more quickly. Another thing that is worth noting is  is relatively large, it still won’t cause CUM to expand without that, even if CT control. However, an early introduction of contract tracing will lead to both a drop in CUM and an earlier eradicating day.

8. Sensitivity Analysis

There are some parameters that have a fixed value throughout our work. By varying the value of these parameters, we can see their impact on the model.



8.1. Impact of Transmission Rate

I The black dotted curve in Figure 17 represents the actual statistics. The red area surrounding this curve represents the normal range for the cumulative number of individuals where results in this range are assumed to be reasonable. However, a little  will probably let the results fall into the grey region, which variance in the value of I we regard as being irrational.

 for the red area is from 0.30 to 0.32, which is relatively small The value of I  is from 0.2 to 0.30 and 0.32 to 0.45. compared to the grey area whose value of I  is a rather sensitive parameter and any error, either from calculation or Therefore, I from misunderstanding will lead to a comparatively large discrepancy for the prediction of the cumulative number of individuals. Values within the acceptable range are  and . regarded as reasonable. This is the same with other transmission rates H C

8.2. Impact of the Incubation Period 1/

 is set to be 9 when fitting the reported data and is not changed ever since. However, by varying the value of  from 5 to 15, which is a quite large variance that is almost beyond the normal range, we can see from Figure 18 that the trends of cumulative number of individuals are quite similar. Therefore, we come to the conclusion that the results are not sensitive to different values of .



8.3. Fluctuation of

H

 to test its sensibility. The Noises are added to the fatality rate inside hospital H left graph and right graph add a 50% and 100% Gaussian noise respectively.



H

 mainly We can see that minor differences occur when noises are added. Since H reflects the manufacturing speed of medicine and the efficacy of medicine as wel, we can come to the conclusion that the speed of manufacturing and the efficacy of medicine will not impact the cumulative number of individuals too much.

9. Strengths and Weaknesses

9.1. Strengths

 We improved the traditional epidemic model SEIR and transformed it into the SEIHCR (CT) model which considers more factors and is thus better suited to the special features of West Africa.  We divided the factors that would impact the situation of Ebola into three parts:

1) Factors that should be taken into consideration when improving the spread model;

2) Factors regarding the pharmaceutical intervention, such as medication efficacy;

3) Other important interventions such as treatment of corpses, contact tracing.

Different methods have been applied for different factors to improve accuracy.  The Weighted Fuzzy -c Means Clustering Algorithm is applied in deciding the delivery locations. Daily needed medicine quantities for different cities calculated from the SEIHCR (CT) model are used as weights to make this algorithm a part of the whole epidemic model, which increases integrity.  Later, we analyzed the influence of the critical factors on the control and eradication of Ebola and predicted the day of the final eradication, providing valuable reference information to the public.

9.2. Weaknesses

 Due to the large number of parameters in the model, the integrity of them in solving the problem may sometimes be lacking.  Due to the large quantity of statistics for the cities in Guinea, Sierra Leone and Liberia, we only selected Freetown as an example for analysis, which might cause some discrepancy.

9.3. Future Work

Since there are many weaknesses in our work, such as a relatively weak integrity between parameters and not enough analysis of each city’ statistics, plenty of efforts can be spent in the future to improve our work.

Firstly, relationship between parameters will be our top consideration in the future.

 In this article, we only considered a few of them, such as the relationship between H and k . Considering the large amount of parameters, it is impossible that they are totally I, isolated from each other. For example, the value of the three transmission rates: ,  are correlative in practice, so the variation of these three parameters should H C be related. Marisa C. Eisenberg et al showed deep insight into this problem[26].

Secondly, more analysis of each city’s data can be obtained using the SEIHCR (CT) model. In this sense, we’ll know how Ebola spreads among cities by the results of our own model, not only according to the statistics of WHO.

Furthermore, we can also test the possibility of applying our model to other epidemics that share similar features with Ebola. By doing so, we may even discover differences between diseases and will probably improve our model even further. More importantly, we can apply our model to the former outbreaks of Ebola and test its feasibility.

Finally, because all outbreaks of Ebola in history didn’t last long, we could try to find out the inner reason why diseases like these have this kind of unusual characteristic.

Letter to the World Medical Association

To whom it may concern,

Upon hearing that your association has developed a new medication that is able to stop Ebola and cure patients whose disease is not advanced, I believe not only me, but also every other person in the affected areas is thrilled ！Not a single effective pharmaceutical drug had been able to be produced in large quantity before your announcement though numerous efforts have been paid to slow the spread of Ebola and invent new drugs to cure patients!

I and my fellow colleagues have been researching deeply into the spread of Ebola and how medication can serve as an important intervention in controlling and eradicating this deathly disease. We hope some of the outcome of our research can help you decide on the manufacturing and delivering this new medication. This is the reason we write this letter.

Specifically, we improved the traditional epidemic model and transformed it into one that suited the specific feathers of Ebola. Our model is of good feasibility because we successfully simulated the growing trend of the number of cumulative individuals in Freetown, capital of Sierra Leone, the city with the most patients. Our calculated data correspond with the reported data by WHO greatly. Since the quantity of needed medicine is related to the number of cumulative patients, our model will serve as a perfect tool for later decide the quantity of medicine each city needs.

Based on our studies, the location of delivery in the terrain of Guinea, Sierra Leone and Liberia will include 6 ‘headquarters’. These headquarters will be in charge of storing and allocating medicine. Their locations are presented in the following picture.

One specific set of colored cities will later receive medication from the headquarter inside them. The geographical coordinates for these headquarters are:

Location 1 2 3 4 5 6 8.4897 N  10.3315 N 10.9935 N 6.9627 N 8.5729 N 10.5202 E Latitude 9.1702W  13.4050W 10.8677W 10.5202W 12.4282W 8.3181W Longitude

If medicine are to be delivered every 4 weeks, the respective percentage allocated to these 6 headquarters are 13.93%, 6.21%, 0.79%, 27.00%, 50.83% and 1.25%.

We suggest that a few important factors be taken into careful consideration if you want to control and eradicate Ebola. Firstly, it’s the speed of manufacturing. The results of our studies suggest that the average speed of manufacturing should be 106.2 unit dose per day to assure needs from patients per day can be satisfied. Secondly, it’s the introduction time before allocation takes place. The earlier medicine can be sent to those in need, the better the control effect will be. Thirdly, it’s the efficacy of the medicine. With an increase in the efficacy of medicine, the day of finally eradicating Ebola is predicted to arrive faster. And lastly, it’s the time before contact tracing takes place. An intensified contact taking practice will lead to a much faster controlling of the disease.

To conclude, we hope that the studies of us will be helpful for you to make the strategy of manufacturing and delivering the new medication. We sincerely hope that with everyone’s efforts, including our research and your invention of the new medication, the day of the eradication of Ebola to come as soon as possible!

Best regards,

M. The basic reproductive number of Ebola and the effects of public health

measures: the cases of Congo and Uganda, Journal of Theoretical Biology, 229:

119–126, 2004. [11] Althaus, C. L., Estimating the reproduction number of Ebola virus (EBOV) during the 2014 outbreak in West Africa, PLOS Currents Outbreaks, Sep 2nd, 2014. [12] Valdez, L. D., Rêgo, H. H. A., Stanley, H. E., Braunstein, L. A., Predicting the extinction of Ebola spreading in Liberia due to mitigation strategies, arXiv:1502.01326v2, 2015. [13] New Zealand Ministry of Care, Case definitions for Ebola virus disease, http://www.health.govt.nz/our-work/diseases-and-conditions/ebola-updates/case- definitions-ebola-virus-disease.

[14] Legrand, J., Grais, R.F., Boelle, P.Y., Valleron, A.J., Flahault, A., Understanding the dynamics of Ebola epidemics, Epidemiology and Infection, 135(4): 610-621, 2007. [15] Centers for Disease Control and Prevention, Contact tracing can stop Ebola in its tracks, http://www.cdc.gov/vhf/ebola/outbreaks/what-is-contact-tracing.html. [16] Lekone, P. E., Finkenstädt, B. F., Statistical inference in a stochastic epidemic

SEIR model with control intervention: Ebola as a case study, Biometrics, 62(4):

1170–1177, 2006. [17] Centers for Disease Control and Prevention, 2014 Ebola Outbreak in West Africa - Reported Cases Graphs, http://www.cdc.gov/vhf/ebola/outbreaks/2014-west-africa/cumulative-cases- graphs.html [18] World Health Organization, Ebola situation report, http://www.who.int/csr/disease/ebola/situation-reports/en/. [19] Briand, S., Bertherat, E., Cox, P., et al, The international Ebola emergency, The New England Journal of Medicine, 371: 1180-1183,2014. [20] Rivers, C. M., Lofgren, E.T., Marathe, M., Eubank, S., Lewis, B.L., Modeling the Impact of Interventions on an Epidemic of Ebola in Sierra Leone and Liberia.

PLOS Currents Outbreaks. Oct 17th, 2014. [21] Partners in Health, Need to Know: How Contact Tracing Can Stop Ebola, http://www.pih.org/media/need-to-know-contact-tracing. [22] Driessche, P. V. D., Watmough, J., Reproduction numbers and sub-threshold endemic equilibrium for compartmental models of disease transmission, Math.

Biosci., 180:29-48, 2002. [23] Browne, C., Huo, X., Magal, P., Seydi, M., Seydi, O., Webb, G., A Model of the 2014 Ebola Epidemic in West Africa with Contact Tracing, arXiv:1410.3817v2[q-bio.PE], Oct 21st, 2014 [24] World Health Organization, Ebola data and statistics http://apps.who.int/gho/data/node.ebola-sitrep.ebola-country?lang=en [25] Bezdek, J.C., Ehrlich, R., Full, W., FCM: The fuzzy c-means clustering algorithm, Computers and Geosciences, 10 (2-3): 191-203,1984. [26] Eisenberg, M. C., Eisenberg, J. N. S., Jeremy, D’Silva, P., Wells, E. V., Cherng, S., Kao, Y. H., Meza, R., Modeling surveillance and interventions in the 2014 Ebola epidemic, arXiv:1501.05555v1 [q-bio.PE], Jan 22nd, 2015.
