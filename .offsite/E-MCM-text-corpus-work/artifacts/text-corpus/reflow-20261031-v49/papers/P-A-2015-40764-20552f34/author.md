Summary

Herein we present stochastic and deterministic models for the current Ebola outbreak in West Africa. The general approach used for both models is to divide the population into three states, infected people, healthy vulnerable people, and healthy immune people. We then assign parameters representing the rates at which possible transitions between these states occur. This enables us to predict the spread of the Ebola virus for any initial conditions.

To verify the general approach, stochastic and deterministic predictions are compared with World Health Orgnisation (WHO) data for the most recent eighty-ﬁve days of the outbreak. To ensure the general method is robust, we investigate four regions: Guinea, Liberia, Sierra Leone, and West Africa as a whole. We estimate the state transition rate parameters using available statistics, and show that realistic parameter estimates result in predictions that have good agreement with known data. We then use both models to predict the future of the outbreak, assuming present conditions remain. This provides a basis with which to compare the eﬀects of diﬀerent treatment methods.

In our sensitivity analysis, we independently consider the eﬀect of three treatment methods on the number of deaths caused by Ebola. The three treatment methods tested are: improvements in medical services, improvements in the quality and quantity of medicine, and distributing a vaccine. Stochastic simulations for several treatment regimes are performed over the short-term (six months), and medium- term (two years). This enables us to determine the relative eﬀectiveness of diﬀerent treatment methods, and which nations should be targeted in the application. We then generalise the investigation using the deterministic model. By analysing the stability of ﬁxed points in the model, we determine the relationship between parameters required to eradicate infections in the long-term. Qualitatively, key ﬁndings of the sensitivity analysis are:

• The most eﬀective short-term strategy in all countries is producing a large quantity of improved medicine

• The most eﬃcient strategy for reducing medium-term deaths is to improve medical services to isolate infected patients

• Short-term strategies will be most eﬀective in Sierra Leone and Liberia

• Medium-term strategies should target all three countries in the outbreak: Guinea, Sierra Leone, and Liberia

• Although vaccination is less eﬀective in the short and medium-term than other treatment methods in all countries, developing a vaccine is the only way to ensure that the virus can be eliminated in the long-term

These ﬁndings are used to produce recommendations of Ebola treatment strategy for the World Medical Association.

1 Introduction

We present two models to predict the current Ebola outbreak in West Africa. The general approach in both models is to divide the population into three states, infected people, vulnerable healthy people, and immune healthy people, and consider the transitions between these states. Based on this approach, we develop stochastic and deterministic mathematical models to predict the spread of the virus. These models are also used to assess the impact of potential treatment methods.

The models are validated using data on the number of Ebola cases and deaths provided by the World Health Organisation. Both models show good agreement for the outbreak in four regions, to prove the robustness of the approach. The models are then extended to predict the future evolution of the data, if current treatment practices are preserved into the future. This provides a basis against which the eﬀects of diﬀerent treatment options are assessed independently.

The stochastic model is used to predict the short-term and medium-term eﬀects of three diﬀerent Ebola treatment options. These options are an improvement in medical services, improvement in available medicines, and developing a vaccine. We compare the eﬃciency of each method in three countries by comparing the reduction of total deaths predicted in the model with the percentage change required from current treatment levels. We ﬁnd that a large quantity of improved medicine is the most eﬀective short-term solution, but medical services become more eﬃcient in the medium term. In addition, we ﬁnd that treatment in the short-term should be targeted to Sierra Leone and Liberia, but in the medium-term, it is equally important to treat Guinea. Following this analysis, we generalise to ﬁnd the long-term impacts of diﬀerent treatment using the deterministic model. We ﬁnd that, although vaccines are less eﬃcient in the short and medium-term, the only way to ensure complete eradication of Ebola in the long term is to develop a vaccine. These ﬁndings inform recommendations to the World Medical Association to optimise the treatment of Ebola.

1.1 Problem Approach

To address the problem of eradicating Ebola, we initially present a general model that provides accurate predictions of the evolution of the outbreak in West Africa based on current treatment practices. To do this, we produce a general method, and ﬁnd parameters that match data provided by the World Health Organisation (2015a). Given an accurate model of the disease, we use it to isolate and predict the future impact of three diﬀerent types of additional treatment:

• Improving medical services, for example improved quarantine, and increased numbers of doctors and hospitals

• Improving medicine, for example that developed by the World Medical Association

• Developing and distributing a vaccine

We perform this analysis in each of the three countries in the primary Ebola outbreak: Guinea, Liberia, and Sierra Leone. Although the general model permits greater subdivision, the lack of data for smaller regions conﬁnes the investigation to three regions. The analysis provides insight into which treatment methods are most eﬀective, and which country would most beneﬁt from them. Based on our results, we provide recommendations to the World Medical Association in letter form.

A general model for the spread of Ebola is created by classifying each member of the population into one of three states. These states are

• People who are infected with Ebola

• Healthy people who are vulnerable to infection

• Healthy people who are immune to infection As the disease spreads, people in the aﬀected areas undergo transitions between these three states. The generalised model is an open system, whereby total population can increase via births, and decrease via deaths. All possible state transitions are illustrated in Figure 1.

Birth 1 2 ε ε Healthy 7 (Vulnerable) α 3 8 υ Infected 6 Healthy β 5 φ (Immune) γ 4 φ

Death

As Figure 1 shows, each of the eight state transition is assigned a number and a rate parameter. The rate parameters are deﬁned as the rate at which one person of the relevant state undergoes the state transition on a given day. They form the basis of the model, and are altered to model diﬀerent conditions. A list of these parameters is provided in Table 1.

Parameter Description α The daily rate at which a healthy person is infected with Ebola β The daily recovery rate for a person with Ebola ν The daily vaccination rate per person γ The daily death rate per person for people infected with Ebola φ The daily death rate per person, for the healthy population ϵ The daily birth rate per person, assumed equal for both infected and healthy people

We deﬁne these parameters to represent the full set of possible transitions. The formulation is therefore suﬃcient to simulate the changes occurring in an Ebola outbreak. However, this interpretation relies on several assumptions, which are listed in Section 1.1.1.

1.1.1 Assumptions

• The Ebola outbreak is conﬁned to Guinea, Liberia, and Sierra Leone. When developing the model, simulations of the spread of Ebola are performed for individual countries, and the spread of the virus as a whole. As the total number of cases and deaths from Ebola in other countries is small (eight deaths in Nigeria, as opposed to 1957 in Guinea (BBC 2015)), we assume that the entire outbreak occurs in Guinea, Liberia, and Sierra Leone • Population change depends on births and deaths only. We assume that net migration in each of the three countries is zero, as it is likely to be small relative to the overall population

• The birth and death rates are constant. As the state transition parameters are constant, we must assume that the birth and death rate is constant. As the model’s calculations occur over a relatively short time, this is reasonable

• States are binary, and transition between states is instantaneous. We assume that each member of the population belongs to exactly one state at all times. This is reasonable for viral diseases such as Ebola. In addition, the severity of all cases is considered the same, which is reasonable when average data is used

• All people within a population are homogeneous. We assume that the spatial, gender, or age distributions do not aﬀect the rate parameters. This enables the rate parameters to be held constant in the model

• The virus does not mutate. There is no transition from immunity to vulnerability, as the model considers the spread of the current strain of the Ebola virus

• Recovery from Ebola is complete and independent. We assume that people who have recovered from Ebola have the same likelihood of death as other healthy people, and that a person’s recovery from Ebola does not depend on anyone else. Although healthy doctors provide vital assistance, the overall eﬀect of all healthy people on a patient’s recovery is negligible. In addition, we assume that antibodies generated in the recovery provide immunity from future infection. This is supported by Centers for Disease Control and Prevention (2014), which states that antibodies provide immunity from the same Ebola strain for at least ten years

• Infection with Ebola does not aﬀect birth rate. As the cycle of a person’s infection with Ebola is likely to last for much less than nine months, we assume that the birth rate for people with Ebola is the same as the rest of the population

• The possibility of death or recovery is independent of the Ebola infection cycle. In order to model state transitions by constant rates, we assume that the likelihood of death or recovery is the same regardless of how long a patient has been infected. The infected state is an average stage that represents all stages of the disease, for example incubation, infectious, recovering, etc.

• The virus is transferred between living people. Although Ebola is commonly contracted via contact with deceased (World Health Organisation 2014a), our model assumes that these people transfer the disease while living. This does not aﬀect overall rate of transmission. In addition, transmission between non-human species is neglected

• Treatment practices in place between 12 November 2014 and 5 February 2015 are constant. The models are developed based on data available from the World Health Organisation (WHO) between 12 November 2014 and 5 February 2015. The rate parameters therefore reﬂect the treatment practices available between these dates. Holding the rate parameters constant allows us to isolate variables when modelling new medicines and vaccines.

• Immunity is not passed on to the next generation. We assume that a survivor of Ebola cannot give birth to immune oﬀspring. We also assume that healthy parents give birth to healthy oﬀspring, and infected parents give birth to infected oﬀspring

2 Mathematical Models

The problem interpretation described in Section 1.1 is solved using two mathematical models, a stochastic model and a deterministic model. The stochastic model provides a random simulation of the evolution of the disease, and simulates continuously in time. The deterministic model provides an analytical steady state solution, allowing analysis of ﬁxed points and stability. Both models provide a means to model the evolution of the disease based on existing data, and predict future trends.

2.1 Stochastic Model

In the stochastic model, the probability of each transition occurring in a given timestep is calculated using the rate parameters, and then the evolution of the disease is simulated randomly. Deﬁnitions of parameters required for the stochastic model are given in Table 2.

Parameter Description n The timestep number dt The timestep size, given as a fraction of one day Pn The number of healthy, vulnerable people after n timesteps In The number of infected people after n timesteps Hn The number of healthy, immune people after n timesteps

The rate parameters in Table 1 provide a means of determining the probability that one event will occur in a given timestep. The timestep size, dt, is prescribed to ensure that a maximum of one transition of any type can occur in each timestep. In accordance with the eight transitions shown in Figure 1, the following shows the potential results of the subsequent timestep n + 1, and the probability that each event occurs.

 (In, Hn, Pn + 1) w.p. p1 = ϵ(Pn + Hn)dt    (In + 1, Hn, Pn) w.p. p2 = ϵIndt      (In, Hn, Pn −1) w.p. p3 = φPndt      (In, Hn −1, Pn) w.p. p4 = φHndt     (In+1, Hn+1, Pn+1) = (1) (In −1, Hn, Pn) w.p. p5 = γIndt  (In −1, Hn + 1, Pn) w.p. p6 = βIndt      (In + 1, Hn, Pn −1) w.p. p7 = αInPndt      (In, Hn + 1, Pn −1) w.p. p8 = νPndt     1 −P8  (In, Hn, Pn) w.p. i=1 pi 

For example, transition one is the birth of one healthy, but not immune person. The rate parameter ϵ provides the birth rate per person per day. In addition, we assume that all healthy people give birth to vulnerable healthy oﬀspring. Therefore, the probability of a healthy birth occurring in a given timestep is given by multiplying ϵ by the total number of healthy people, (Hn + Pn), and the fraction of one day for each timestep, dt. The result of this event is that the next timestep, n + 1, has one additional healthy person, i.e. Pn+1 = Pn + 1. The probabilities and outcomes of all other events are similarly determined (we note that the probability of transmission p7 depends on both the number of infected people and the number of vulnerable people). For the stochastic model to be valid, the timestep must be small enough such that 8 X pi ≤1, (2) i=1 which ensures that a maximum of one event can occur each timestep.

Code to simulate this system is produced in Matlab. To generate the event for each timestep, a pseudo-random number r ∈[0, 1] is generated. An event is selected if r lies within the cumulative probability range up to that event. To keep track of the total number of cases and deaths due to Ebola, a counter that increments whenever a relevant event occurs is used. The simulation process is repeated for the desired number of timesteps to completely simulate an Ebola outbreak for a given initial state (I0, H0, P0).

2.2 Deterministic Model

To implement the deterministic mode, we deﬁne Pn, In , and Hn in the same way as for the stochastic model, where the timestep number n represents a number of days. We then deﬁne functions f, g, and h containing diﬀerence equations for subsequent states. They are constructed using the same state transition rate parameters as the stochastic model. The diﬀerence equations are

 f(Pn, In, Hn) := Pn+1 = Pn(1 + ϵ −φ −ν −αIn) + ϵHn   (3) g(Pn, In, Hn) := In+1 = In(1 + ϵ −γ −β) + αInPn  h(Pn, In, Hn) := Hn+1 = Hn(1 −φ) + βIn + νPn. 

Unlike the stochastic model, the deterministic model only keeps track of the day-to-day number of people in each state. However, the system is easy to implement in Matlab, as randomness is not considered. Implementing the diﬀerence equations (3) in Matlab and iterating over n timesteps enables complete deterministic simulation of the Ebola outbreak for given initial conditions (I0, H0, P0).

2.3 Comparison of Models

Stochastic Deterministic Randomness Repeated simulation not required State populations take integer values Analytical steady state solutions Timestep is eﬀectively continuous Less computational time Separate accounting of all state transitions

In our analysis, we take advantage of the unique features of the stochastic and deterministic models. The stochastic model provides a means to generate plots diﬀerent state transitions against time. This is used to compare with WHO data on the total number of Ebola cases and deaths. In addition, simulations using the stochastic model are used to perform sensitivity analysis on the parameters. This allows us to isolate the eﬀect of diﬀerent treatment practices. The deterministic model provides an analytical method to accurately analyse diﬀerent types of steady state solution, and determines the relationship between rate parameters required to drive Ebola infections to zero.

3 Results - Predicting the Spread of Ebola

We present stochastic and deterministic solutions for the spread of Ebola. The models are veriﬁed using data for the number of deaths and total cases in the 85 days from 12 November 2014 to 5 February 2015, which is available from the World Health Organisation (2015a). The development of an accurate model then enables us to make modiﬁcations based on diﬀerent treatment options.

3.1 Model Parameters

To simulate the outbreak, we require numerical values for

• State transition rate parameters: α, β, ν, γ, φ, ϵ

• Initial conditions: I0, H0, P0

Where possible, we use realistic data to provide suitable estimates for these parameters. We predict the value of the parameters in all three countries independently, then combine them to produce a population-weighted average to model the outbreak as a whole. This method of prescribing the parameters provides a real-world basis for all state transitions in the model.

3.1.1 ν

As there is no current vaccine for Ebola (World Health Organisation 2015b) as of January 21 2015, we assume ν = 0 in the predictive model.

3.1.2 ϵ, φ

CountryMeters (2015) provides live population estimates, as well as data on the birth and death rates of each country. Table 4 gives this data for the three relevant countries on 5 February 2015.

Birth Rate [ppl d−1] Death Rate [ppl d−1] Country Population Guinea 12,414,680 1,150 326 Liberia 4,615,917 425 121 Sierra Leone 6,404,599 626 191 Overall 23,436,196 2,201 638

The birth and death rate parameters, ϵ and φ respectively, are determined by

ϵ = Birth Rate Population, (4)

and φ = Death Rate Population . (5)

These give the rate at which one healthy person will give birth or die respectively. The initial population at 12 November 2014 is estimated by subtracting the net births over the 85 preceding days from the population given in Table 4,

Initial Population = Final Population −85(Birth Rate −Death Rate). (6)

Performing these operations gives the results in Table 5.

Country ϵ φ Initial Population Guinea 9.3175e-5 2.6386e-5 12,343,779 Liberia 9.2567e-5 2.6392e-5 4,589,796 Sierra Leone 9.8295e-5 2.9981e-5 6,367,191 Overall 9.4455e-5 2.7369e-5 23,300,766 3.1.3 I0, H0, P0

The initial population found in Section 3.1.2 entirely consists of the three states of the general model, I0, H0, and P0. To determine the initial population of each of the states, we consider WHO data for the number of Ebola cases from November 12 2014. This data is given in Table 6.

Country Total Cases Total Deaths Guinea 1,878 1,142 Liberia 6,822 2,836 Sierra Leone 5,368 1,169 Overall 14,068 5,147

To estimate I0, we assume that all reported cases that have not resulted in death are still infected, and therefore I0 = Total Cases −Total Deaths. (7) Although this neglects the possibility that a reported case has recovered from the virus, which would lead to overestimating I0, we accept the assumption. This is because the total number of infections is low relative to the total population, the WHO acknowledge that their statistics underestimate the Ebola epidemic (World Health Organisation 2014b), and that it is diﬃcult to otherwise predict current infections from the data. Based on this assumption, we also have

H0 = 0, (8)

and P0 = Initial Population −I0. (9) This gives the following values for the initial states.

Country I0 P0 Guinea 736 12,343,043 Liberia 3,986 4,585,810 Sierra Leone 4,199 6,362,992 Overall 8,921 23,291,845

3.1.4 α, β, γ

The parameters α, β, and γ are more diﬃcult to determine from available data. As an infected person will eventually transition to health or death, an important factor is the mortality rate of Ebola. An estimate of mortality rate, i.e. the likelihood of eventual death once infected, is given by Mortality Rate = Total Deaths Total Cases . (10)

For this calculation, we use the latest data, to reduce the proportion of ongoing cases. This data is given in Table 8.

Country Total Cases Total Deaths Mortality Rate Guinea 2,986 1,947 0.65204 Liberia 8,745 3,746 0.42836 Sierra Leone 10,756 3,286 0.30550 Overall 22,487 8,979 0.39930 However, to determine the daily rate of death and recovery, we introduce another parameter, T, the disease residence time. This is the average number of days required for an infection to result in either death or recovery. Using this parameter, we can determine the daily rates of death (γ) and recovery (β) among infected people, using γ = Mortality Rate , (11) T and β = 1 −Mortality Rate . (12) T To determine α, the rate of disease transmission, we introduce the parameter K, the average number of healthy people to whom each infected person transmits the disease during the period they are infected. The parameter α is therefore given by K α = . (13) TP0 As there is no reliable data available to determine T and K, their values are prescribed to ﬁt the WHO data. Doing this ensures that our model is accurate, and allowing K to come as part of the solution provides a prediction of the transmission rate in current conditions. The parameters shown in Table 9 result in suitable estimates of the ﬁnal death and case counts post-simulation.

Country K T α β γ Guinea 0.90 45 1.6203e-9 7.7324e-3 1.4490e-2 Liberia 0.89 155 1.2521e-9 3.6880e-3 2.7636e-3 Sierra Leone 0.79 42 2.9561e-9 1.6536e-3 7.2739e-3 Overall 0.86 73 5.0992e-10 8.2775e-3 5.5022e-3

To determine if the calculated values of K are appropriate, we cite a study by Meltzer et al. (2015), which gives estimates for K in various situations:

• For hospitalised patients, K = 0.12

• For home patients with eﬀective isolation, K = 0.18

• For home patients without eﬀective isolation, K = 1.8 (Meltzer et al. 2015)

All average values of K predicted in Table 9 are therefore feasible based on combinations of current treatment techniques. To validate residence time T, we cite a survivor’s anecdote in which the patient ﬁrst noticed symptoms after a ten day incubation, and reached their worst condition after sixteen days (Grant 2014). Assuming it takes a further sixteen days to recover fully gives T that corresponds closely to Table 9. However, considering the result of Liberia, we infer that an appropriate T comes as an artefact of other aspects of the model, rather than from a physical basis.

3.2 Validation

The constant values of the parameters deﬁned in Section 3.1 completely specify the constants required to implement both the stochastic and deterministic models. These are used in both models to produce simulations for the spread of Ebola over the WHO reporting period. These simulations are compared with the WHO data to validate the models.

3.2.1 Stochastic Model

To produce stochastic results, the Matlab simulation is run ten times for each of the four regions modelled. The simulation is run over 85 days to simulate the period from 12 November 2014 to 5 February 2015. The average number of cases and deaths at the end of the simulation are compared with WHO data to determine whether the model is accurate. Results are presented in Table 10. In the table, C and D represent the number of cases and deaths reported on February 5 2015 respectively, and subscripts M and W refer to the stochastic model and WHO data respectively. The parameter σ is the standard deviation of the ten simulation results.

|CM−CW |DM−DW | | Country CM σC DM σD CW DW σC σD Guinea 3,053 110 1,957 50 2,986 1,947 0.61 0.20 Liberia 8,748 51 3,749 20 8,745 3,746 0.059 0.15 Sierra Leone 10,813 159 3,284 57 10,756 3,286 0.36 0.035 Overall 22,557 150 9,041 54 22,487 8,979 0.47 1.1

Note: ‘Overall’ in Table 10 represents the results of a separate simulation using parameters for the overall outbreak, not an arithmetic sum of results for each nation

reported by the WHO. The fact that the real value falls within half a standard deviation of the model prediction in ﬁve of the eight statistics, and that no result is more than 1.1 standard deviations away from the actual value. We therefore conclude that the parameters in Section 3.1 accurately model the Ebola outbreak in all cases.

Further validation is provided by plotting simulation results against day-to-day WHO data for deaths and cases. Examples are provided in Figure 2.

2100 3800 WHO WHO Simulations 2000 3700 Simulations 1900 3600 1800 3500 Total Deaths Total Deaths 1700 3400 1600 3300 1500 3200 1400 3100 1300 3000 1200 2900 1100 2800 0 10 20 30 40 50 60 70 80 90 0 10 20 30 40 50 60 70 80 90 Time [d] Time [d]

(a) Guinea (b) Liberia

3500 9500 WHO WHO 9000 Simulations Simulations 3000 8500

8000 Total Deaths Total Deaths 2500 7500

7000 2000 6500

6000 1500 5500

1000 5000 0 10 20 30 40 50 60 70 80 90 0 10 20 30 40 50 60 70 80 90 Time [d] Time [d]

(c) Sierra Leone (d) Overall As Figure 2 shows, the simulations track the WHO reported daily death count reasonably well. The model predictions produce a more linear trend than the WHO data as we assume the treatment practices (state transition rate parameters) are constant throughout the period. In addition, the WHO data is taken at irregular intervals, and each country updates their data on diﬀerent dates. This suggests the WHO data points may not accurately display the underlying trend in disease spread. We therefore accept the predictions of the model are valid based on WHO data.

3.2.2 Deterministic Model

As the deterministic model only considers the population of the three states In, Hn, and Pn, and does not account for state transitions, we cannot compare with WHO data. However, given the success of the stochastic model, we assume that the deterministic model matches WHO data if its results match the stochastic model. Table 11 shows the results for February 5 2015 of simulating the deterministic model with the parameters in Section 3.1. In the table, subscripts D and S denote the deterministic and stochastic models respectively.

Country IS ID HS HD PS PD Guinea 640 618 457 438 12,412,178 12,411,344 Liberia 3,769 3,789 1,228 1,203 4,609,770 4,609,491 Sierra Leone 2,718 2,789 4,805 4,789 6,394,555 6,394,146 Overall 7,690 7,684 5,820 5,757 23,419,606 23,417,858

As expected, the deterministic model shows good agreement with the stochastic simulations if the same parameters are used in the model. A reason for the small discrepancy in the results is that the timestep used in each simulation is diﬀerent. The stochastic model applies a near-continuous timestep, whilst the deterministic model is updated using a timestep of one day. The stochastic model also incorporates randomness, which creates deviations from deterministic results. An example of this is illustrated in Figure 3.

9000 9000 Stochastic

8500 8500

In In

8000 8000

Deterministic 7500 7500 0 0 10 10 20 20 30 30 40 40 50 50 60 60 70 70 80 80 90 90 Time [d] Time [d]

deterministic and stochastic models deterministic solution. We conclude that both the deterministic and stochastic models provide a means of accurately tracking the spread of Ebola. In our analysis of the predicted eﬀects of possible treatment regimes, we use the predictions of both models.

4 Results - Predicting the Eﬀect of Improved Treatment

To determine the eﬀect of new treatment regimes, the February 5 2015 parameters given in Table 11 are used as initial states (I0, H0, P0) to the model. We initially consider the projected spread of Ebola if the treatment regime in practice from 12 November 2014 to 5 February 2015 is maintained – that is, if the values of state transition rate parameters determined based on WHO data are held constant. The simulations are run in both the short-term (using the stochastic model), and the long term (using the deterministic model). We then independently change parameters based on our interpretations of diﬀerent options to improve treatment. To provide targeted treatment, we perform the simulations in each of the three nations. The possible treatment options are described in Section 4.1.

4.1 Treatment Options

In our analysis, we consider three diﬀerent treatment options. Each has a unique eﬀect on the state transition rate parameters. The treatment options are

• Improving medical services

• Improving medicine

• Developing a vaccine

4.1.1 Improve Medical Services - Decrease α

Improved medical services entail improved quarantine procedures, for example by increasing medical staﬀ, hospital space, or public education. Doing this will improve patient isolation, decreasingα the rate of Ebola transmission from infected to healthy people. If we assume that it is impossible to isolate a patient in the incubation stage, which lasts a quarter of infection residence time, data from Meltzer et al. (2015) provides a means of estimating the minimum K.

Kmin = 0.75(0.12) + 0.25(1.8) = 0.54. (14)

As this is less than the model predictions in Table 9, there is scope to reduce the spread of the virus by improving medical services.

4.1.2 Improve Medicine - Decrease γ, Increase β

We deﬁne ‘medicine’ to incorporate all techniques available to reduce the mortality rate, including existing techniques such as providing intravenous nutrients, and newly developed drugs, for example by the World Medical Association. As the WMA medicine aﬀects patients even in the early stages of infection, we assume that improving either the quality or quantity of medicine will decrease the average mortality of an infected patient. This increases the rate of recovery, β, and decreases the rate of death from infection, γ. We consider the eﬀects of a range of medicine eﬀectiveness in our predictions. Changing the relevant parameters encompasses changes in the quantity of medicine, as well as the eﬀectiveness of distribution systems.

4.1.3 Develop Vaccine - Increase ν

Developing a vaccine opens the possibility of transition from the vulnerable healthy state to the immune healthy state. This will decrease the rate of Ebola spread. To model a vaccine, we consider non-zero ν. As there is no vaccine available, we consider a range of diﬀerent distribution speeds in our simulations. In our simulation ν is related to the number of successful vaccinations.

4.2 Sensitivity Analysis

Sensitivity analysis is performed using both the stochastic and deterministic models. Short and medium-term simulations of six months, one year, and two years are performed using the stochastic model. These are important to guide immediate prevention strategy, and some assumptions (e.g. immunity is retained) are more likely to hold in the short-term. Long-term steady state conditions are predicted using the deterministic model. Speciﬁcally, we seek combinations of rate parameters that drive the steady-state number of infections to zero.

4.2.1 Stochastic Model

Stochastic simulations are Short-Term Projections Based on Current Treatment Levels performed using the same rate parameters and February 5 2015 initial values to predict the total number of cases and deaths in each country over six months, one year, and two years at the current level of treatment. As with the initial modelling the average of ten simulations is taken. These results are presented in Table 12. In the table, C and D represent the number of new cases since February 5 2015. We change this convention as we no longer need to match WHO data, the initial states are better deﬁned, and new cases provides a better indication of disease spread.

6 Months

1 Year

2 Years

Country

C D

C D

C D

Guinea 2,049 1,441 3,625 2,549 6,093 4,201 Liberia 3,873 1,828 7,303 3,428 13,857 6,391 Sierra Leone 6,262 2,380 9,180 3,479 11,199 4,224

In our analysis, we consider ten percent changes in the relevant parameters, and other reasonable targets based on improved treatment methods. This is suitable for short term modelling, where large-scale changes are unlikely to be possible. We apply the stochastic model for each of the three nations, to determine which strategy is most useful in the short-term, and where they are optimally applied. In each case, data is the average of ten stochastic simulations.

Eﬀect of Improving Medical Services To assess the impact of increasing medical services in an individual country over six months, one year, and two years, we consider two cases:

• A 10% decrease in transmissions per infected person, i.e. decreasing α by 10%

• Decrease transmissions per infected person to the minimum, Kmin = 0.54

All other parameters are held constant in the stochastic simulations, and once again an average of ten simulations is taken. The results are given in terms of the overall reduction in deaths or cases measured after the given period. Intermediate data processing is omitted for simplicity. The results are given in Table 13 and Table 14 respectively.

6 Months

1 Year

2 Years

Country

C D

C D

C D

Guinea -589 -280 -1,386 -771 -2,956 -1,780 Liberia -576 -119 -1,359 -332 -3,491 -1,081 Sierra Leone -1,323 -310 -2,672 -731 -4,395 -1,347

minimum, K = 0.54

6 Months

1 Year

2 Years

Country

C D

C D

C D

Guinea -1,378 -654 -2,889 -1,667 -5,325 -3,288 Liberia -1,898 -335 -4,196 -1,057 -9,562 -3,156 Sierra Leone -3,440 -808 -5,901 -1,673 -7,912 -2,421

Eﬀect of Improving Medicine To assess the impact of improving medicines, we consider:

• A 10% decrease in average mortality rate

• Distribution of a new WMA medicine such that average mortality rate is decreased to 30% in all regions

• Distribution of a new WMA medicine such that average mortality rate is decreased to 15% in all regions

The eﬀects of mortality rate on the parameters β and γ are determined by Equations (11) and (12). Average simulation results are given in Table 15, Table 16 and Table 17 respectively. In these tables, any increases in cases occurring in some simulations are likely to be caused by randomness.

6 Months

1 Year

2 Years

Country

C D

C D

C D

Guinea -116 -205 -311 -393 -199 -532 Liberia +18 -193 +146 -304 -25 -676 Sierra Leone +121 -175 -105 -380 -423 -575

6 Months

1 Year

2 Years

Country

C D

C D

C D

Guinea -23 -775 -124 -1,215 -586 -2,401 Liberia -31 -571 -24 -1,022 +7 -1,896 Sierra Leone +75 -3 -231 -147 -239 -178

6 Months

1 Year

2 Years

Country

C D

C D

C D

Guinea -15 -1,109 -151 -1,974 -748 -3,333 Liberia -43 -1,196 +111 -2,221 +2 -4,159 Sierra Leone +67 -1,188 +14 -1,743 +62 -2,168 Eﬀect of Vaccination To assess the impact of distributing an eﬀective vaccine, we consider:

• A vaccination distribution rate in which approximately 10% of the population will be successfully vaccinated in two years

• A vaccination distribution rate in which approximately 30% of the population will be successfully vaccinated in two years

• A vaccination distribution rate in which approximately 50% of the population will be successfully vaccinated in two years

The parameter ν is given by ν = V 730, (15)

where V is the proportion of the population that is vaccinated in two years. This gives ν = 1.3699e-4, ν = 4.1096e-4, and ν = 6.8493e-4 for the three respective cases. Simulating the stochastic model with these parameters gives results shown in Table 18, Table 19, and Table 20.

population in two years

6 Months

1 Year

2 Years

Country

C D

C D

C D

Guinea -149 -68 -451 -250 -1,578 -911 Liberia -39 -32 -219 -36 -1,313 -347 Sierra Leone -10 +25 -488 -130 -1,045 -315

population in two years

6 Months

1 Year

2 Years

Country

C D

C D

C D

Guinea -246 -108 -965 -515 -2,688 -1,586 Liberia -159 -52 -614 -138 -3,367 -943 Sierra Leone -370 -60 -1,230 -302 -2,844 -849

population in two years

6 Months

1 Year

2 Years

Country

C D

C D

C D

Guinea -310 -127 -1,054 -564 -3,363 -1,999 Liberia -318 -55 -1,118 -215 -4,963 -1,463 Sierra Leone -513 -76 -1,798 -477 -3,539 -1,033

Analysis We assume that the primary measure of an eﬀective treatment is to prevent the highest number of total deaths. Therefore, to illustrate the most eﬃcient treatment method, we plot the reduction in total deaths against the medium-term percentage change in current treatment conditions, for each nation and type of treatment. In lieu of cost data, we assume that treatment eﬃciency is proportional to the reduction in deaths per percentage change in treatment. When parameters are set to uniform values across all regions, percentage change is calculated based on the initial value for the particular region. For example, change in mortality due to medicine is determined with respect to values in Table 8. The resulting short-term (six months) and medium-term (two years) plots are shown in Figure 4 and Figure 5 respectively.

1500

Net Six−Month Reduction in Deaths 1000

Guinea 500 Liberia Sierra Leone Medical Services Medicine Vaccine 0 0 20 40 60 80 100 Percentage Increase in Treatment [%]

diﬀerent nations and treatment methods

5000

Net Two−Year Reduction in Deaths 4500

4000

3500

3000

2500

2000 Guinea Liberia 1500 Sierra Leone 1000 Medical Services Medicine 500 Vaccine

0 0 10 20 30 40 50 60 70 80 90 100 Percentage Increase in Treatment [%]

diﬀerent nations and treatment methods In these ﬁgures, treatments that appear above the dotted trendline are relatively eﬃcient, and are therefore recommended for implementation. This is because they require a reduced percentage increase in treatment to achieve relatively greater reductions in death.

In the short-term results show that improving medicine and medical services are more eﬃcient method of reducing deaths than vaccination. The most eﬀective methods of reducing death in the short-term are medicines that substantially decrease the average mortality rate. For example, in Sierra Leone, an eﬀective medicine can save 47% more lives in the short-term than the maximum possible improvement in medical services. These results are sensible considering the evolution of disease. The vaccine will not prevent many cases in the short-term, and more immediate treatment methods such as medicine are more eﬀective in reducing short-term deaths. Also, the results show that greater eﬃciencies are attained when the short-term strategies are deployed in Sierra Leone. This is because it has a higher number of initial cases.

However, as the medicine does not cause signiﬁcant reductions in the number of cases over two years, its eﬀectiveness in reducing deaths is decreased in the medium-term relative to other treatment methods. As Figure 5 shows, vaccination becomes a more competitive treatment option in the medium-term, whilst improving medical services is still important. In addition, the eﬃciency of introducing the three treatment methods is similar in each nation. Health services and vaccinations have a strong eﬀect in Guinea in gross and relative terms. This ﬁnding is important, as Guinea has by far the lowest proportion of cases of the three nations, and will be neglected if treatment is allocated according to this proportionality alone.

Based on this analysis, we recommend short-term provision of improved medical services and medicine, especially targeting aﬀected areas in Sierra Leone. However, if research shows that the current Ebola strain is likely to last up to two years, vaccination becomes a viable strategy, and all nations should be targeted for improved medical services and medicine. It must be emphasised that this analysis does not determine the relative cost of each treatment method. Cost-beneﬁt analysis is left to policy-makers with knowledge of the cost of each treatment method. The result is likely to be quite diﬀerent from the conclusions expressed here.

4.2.2 Deterministic Model

Long-term projections of the Long-Term Projections Based on Current Treatment Levels evolution of the Ebola outbreak are performed using the deterministic model. Once again, the rate parameters used are the constant values found to accurately predict the disease in the WHO’s reporting period. Results are shown in Figure 6.

5 7 7 x 10 x 10 x 10 14 18 3.4 16 12 3.2 14 10 12 3 8 10 Hn Pn In 2.8 8 6 6 2.6 4 4 2.4 2 2 0 0 2.2 0 1 2 3 4 5 6 0 1 2 3 4 5 6 0 1 2 3 4 5 6 Time [d] Time [d] Time [d] 4 4 4 x 10 x 10 x 10

(a) Infected (b) Immune (c) Vulnerable Using the numbers for the overall outbreak, we ﬁnd that the number of infected and immune people diverge to inﬁnity, whilst the number of vulnerable people is stable. The model therefore emphasises the urgent necessity of improving treatment. In particular, the ﬁrst peak in the infected plot occurs after about 3000 days, so at minimum, medium-term strategies such as those suggested by the stochastic model are required. In addition to this, analysing the ﬁxed points of the deterministic model provides insight into parameter relationships that drive long-term steady state number of infections to zero.

Fixed Point and Stability of Deterministic Model

To analyse the long-term eﬀects of changing the state transition rate parameters in a general outbreak, we consider the ﬁxed points of the deterministic system. We then determine relationships between the parameters that lead to stable solutions that eradicate the virus. The structure of treatment can then be altered based on the results to produce a strategy that eradicates Ebola long-term.

To determine the ﬁxed points of the system, we recall the deterministic diﬀerence equations (3),

 f(Pn, In, Hn) := Pn+1 = Pn(1 + ϵ −φ −ν −αIn) + ϵHn   g(Pn, In, Hn) := In+1 = In(1 + ϵ −γ −β) + αInPn  h(Pn, In, Hn) := Hn+1 = Hn(1 −φ) + βIn + νPn. 

To determine the ﬁxed points of this model, we solve the system

 Pn+1 = Pn   (16) In+1 = In  Hn+1 = Hn, 

which gives  Pn(ϵ −φ −ν) −αInPn + ϵHn = 0   (17) In(ϵ −γ −β) + αInPn = 0  Hn(−φ) + βIn + νPn = 0. 

The system (17) has eight possible steady state solutions. These are summarised in Table 21. The table lists all possible steady state values for each of the states, and lists any conditions on the parameters that arise in each case.

Case Steady state Conditions Description Hn = 0 Ebola causes extinction In = 0 1 None in the region examined. Pn = 0 Hn = H Everyone will be immune.

2 In = 0 ϵ = 0 This is only the case Pn = 0 if there is no birth.

Everyone will be infected.

Hn = 0 This is only the case if γ = ϵ 3 In = I there is no recovery and the β = 0 Pn = 0 rates of birth and death of infected people are equal.

Hn = 0 Everyone will be vulnerable. ν = 0 4 In = 0 This is the case only if there ϵ = φ Pn = P is no vaccination.

No vulnerable person will remain.

Pn = 0 ϵ = 0 But since parameters are 5 γ = −β φHn = βIn non-negative we have β = γ = 0. Hence Hn = 0, just like Case 3.

No infected person In = 0 will remain, and a constant 6 ϵ = φ φHn = νPn proportion of people will be immune.

No immune person β(φ + ν −ϵ) = ν(γ + β −ϵ) Hn = 0 will remain, and a constant In = (ϵ −φ −ν)/α γ + β ≥ϵ 7 proportion of people Pn = (γ + β −ϵ)/α φ + ν ≥ϵ will be infected.

φ[−β(γ+β−ϵ)(ϵν+φ(ϵ−γ−ν) Hn = 1 + Each of the states will α(ϵβ−φ(γ+β−ϵ))) ν α(γ + β −ϵ)] share a constant 0 < Hn, In, Pn < ∞ 8 proportion of the In = (γ+β−ϵ)(ϵν+φ(ϵ−φ−ν)) α(ϵβ−φ(γ+β−ϵ)) total population. Pn = (γ + β −ϵ)/α

To eradicate the virus, we seek a ﬁxed point solution such that In = 0. In addition, we aim to control the outbreak by varying the parameters α, β, γ, and ν, as with the stochastic model. We do not consider Case 1, as it represents extinction, and does not depend on the parameters. Case 2 is also unrealistic, as it relies there being no births. Case 4 is also not considered, as it does not account for the possibility of vaccination. We therefore seek parameter values that lead to Case 6.

To determine these parameters, we consider the stability of the ﬁxed point, and determine parameters that lead to a stable steady-state solution. By the Jury conditions (De Leenheer 2009), a ﬁxed point is stable if |tr(J)| < 1 + det(J) < 2, (18)

where J is the Jacobian matrix associated with the diﬀerence equations. The Jacobian matrix for the system (3) is

    1 + ϵ −φ −ν −αIn −αPn ∂f/∂Pn ∂f/∂In ∂f/∂Hn ϵ 1 + ϵ −γ −β + αPn J = ∂g/∂Pn ∂g/∂In ∂g/∂Hn = αIn 0 . (19)   1 −φ ∂h/∂Pn ∂h/∂In ∂h/∂Hn ν β The determinant and trace of J are

tr(J) = −β −γ −ν + αPn −αIn + 2ϵ −2φ + 3, (20)

and

det(J) = (1−φ)[(−β−γ+αPn+ϵ+1)(−ν−αIn+ϵ−φ+1)+α2PnIn]+ϵ(βν+γν−ν−ανPn+αβIn−νϵ) (21) respectively. To analyse Case 6, we set In = 0 and ϵ = φ . Simplifying (20) and (21) based on this gives tr(J) = −β −γ −ν + αPn + 3, (22)

and det(J) = (β + γ −1 −αPn −φ)(1 −φ −ν). (23)

Substituting these into the jury condition (18) gives a condition on the parameters that give a stable solution at the ﬁxed point,

−β −γ −ν + αPn + 3 < (β + γ −1 −αPn −φ)(1 −φ −ν) + 1 < 2. (24)

As β, γ, ν ≤1, we have tr(J) ≥0. Hence, we can neglect the absolute value signs in (24). As shown in Table 21, there are two equations that specify the three states, In = 0, and φHn = νPn. This gives us one degree of freedom to specify one other parameter to close the system. Crucially, a closed system is only possible if the third equation in the system relates φ and ν. As the death rate of healthy people φ is constant, we must select ν as the independent variable. Rearranging Equation (24) to derive a constraint on ν gives ν > M(1 −φ) −1 = 1 −φ −1 M , (25) M where M = β + γ −1 −αPn −φ. (26)

Although the initial analysis of the model requires ϵ = φ, we can replicate the eﬀect of non-constant birth and death rates with a separate assumption on the steady state population,

n→∞Pn →∞. lim (27)

Equation (27) assumes that the population will eventually approach inﬁnity, as will occur if birth rate is greater than death rate. As the steady state number of infections is zero in this case, there are no deaths due to Ebola, so the assumption is valid if the birth and death rates are assumed constant. We therefore have 1 1 lim M = lim M = 0. (28) n→∞ Pn→∞ We therefore conclude that the condition that must be satisﬁed to produce a stable solution at the ﬁxed point of Case 6 is ν > 1 −φ. (29)

As this condition does not contain α, β, or γ, we reach the important conclusion that vaccination is the only way to ensure that Ebola is eradicated in the long-term. This assertion suggests that a vaccine must be developed for us to be sure that the Ebola outbreak in West Africa can be controlled.

5 Summary of Mathematical Modelling

5.1 Strengths and Weaknesses

Strengths and weaknesses of our approach that become apparent during the solution process are summarised below:

Strengths

Our model...

• is based on realistic mechanism of disease transfer

• uses parameters that are based on empirical evidence

• enables predictions of the evolution of the disease over any length of time

• enables full accounting for the number of each transition and number of people in each state at any time

• accurately predicts known trends in the outbreak in diﬀerent regions, and accurate predictions are achieved with physically realistic values for the parameters

• allows independent analysis of three diﬀerent treatment options

• enables an analytical solution for the relationships between parameters required to drive Ebola infections to zero

• accounts for population growth which is important in long-term forecasts

• simulates randomness in the disease spread (which can lead to divergent outcomes)

Weaknesses

Our model...

• relies on parameter estimates that are justiﬁed using anecdotal evidence (in particular K)

• is validated against a short period relative to the entire Ebola outbreak

• requires good estimates for initial conditions that are not necessarily available from the data

• relies heavily on the accuracy of WHO data, which may be underestimated

5.2 Future Work

The modelling framework used in this analysis provides scope for future enhancement. The following tasks would reduce the assumptions made in this paper, to produce a better model of actual disease transmission:

• Obtaining necessary data to model smaller regions than entire nations

• Allowing the state transition rate parameters to be expressed as functions of time, instead of constant values. This will allow better modelling of how disease treatment changes with time

• Applying a cost function to diﬀerent treatment options, then use the sensitivity analysis to determine the most eﬃcient allocation of resources to reduce deaths

• Increasing the scope of sensitivity analysis to cover all possible parameter changes

• Adding additional states to model the disease life cycle, for example incubation, infectious, recovering, and allowing transmission from deceased people. A disadvantage of adding states is that ﬁxed point analysis becomes more diﬃcult. Adding one extra state doubles the number of ﬁxed points • Increasing the complexity of the model by adding state transitions. For example, a transition from immune to vulnerable can be added to simulate virus mutation, and relaxing the assumption that infection guarantees future immunity. The state transition diagram would look like Figure 7.

A disadvantage of this is that the rate parameters for the new transitions are diﬃcult to determine

Birth 1 2 ε ε 7 Healthy α (Vulnerable) 3 λ 10 8 υ μ Infected 9 6 Healthy β 5 φ (Immune) γ 4 φ

Death

5.3 Conclusion

Stochastic and deterministic models of the West African Ebola outbreak are presented. Both models are based on dividing the population into infected people, immune healthy people, and vulnerable healthy people, and assigning parameters to the rate of transition between these states. The numerical value of parameters are validated against WHO data for four regions from 12 November 2014 to 5 February 2015. We then extend the investigation to produce predictions of future spread of the virus under diﬀerent treatment conditions. Short and medium-term numerical predictions are performed using the stochastic model, and an analytical general solution for long-term steady state conditions is performed using the deterministic model. The ﬁndings of these investigations inform recommendations of future treatment strategies. Qualitatively, the key ﬁndings are

• The most eﬀective short-term strategy in all countries is producing a large quantity of improved medicine

• The most eﬃcient strategy for reducing medium-term deaths is to improve medical services to isolate infected patients

• Short-term strategies will be most eﬀective in Sierra Leone and Liberia

• Medium-term strategies should target all three countries in the outbreak: Guinea, Sierra Leone, and Liberia

• Although vaccination is less eﬀective in the short and medium-term than other treatment methods in all countries, developing a vaccine is the only way to ensure that the virus can be eliminated in the long-term
