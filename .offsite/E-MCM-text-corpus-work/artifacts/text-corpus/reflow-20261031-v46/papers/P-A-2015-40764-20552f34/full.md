# P-A-2015-40764-20552f34

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team #40764

<!-- b000002 | furniture | pages [1] -->
Page 1 of 25

<!-- b000003 | title | pages [1] -->
Stochastic and Deterministic Models of the Eradication of Ebola in

<!-- b000004 | title | pages [1] -->
West Africa

<!-- b000005 | heading | pages [1] -->
Summary

<!-- b000006 | prose | pages [1] -->
Herein we present stochastic and deterministic models for the current Ebola outbreak in West Africa. The general approach used for both models is to divide the population into three states, infected people, healthy vulnerable people, and healthy immune people. We then assign parameters representing the rates at which possible transitions between these states occur. This enables us to predict the spread of the Ebola virus for any initial conditions.

<!-- b000007 | prose | pages [1] -->
To verify the general approach, stochastic and deterministic predictions are compared with World Health Orgnisation (WHO) data for the most recent eighty-ﬁve days of the outbreak. To ensure the general method is robust, we investigate four regions: Guinea, Liberia, Sierra Leone, and West Africa as a whole. We estimate the state transition rate parameters using available statistics, and show that realistic parameter estimates result in predictions that have good agreement with known data. We then use both models to predict the future of the outbreak, assuming present conditions remain. This provides a basis with which to compare the eﬀects of diﬀerent treatment methods.

<!-- b000008 | prose | pages [1] -->
In our sensitivity analysis, we independently consider the eﬀect of three treatment methods on the number of deaths caused by Ebola. The three treatment methods tested are: improvements in medical services, improvements in the quality and quantity of medicine, and distributing a vaccine. Stochastic simulations for several treatment regimes are performed over the short-term (six months), and medium- term (two years). This enables us to determine the relative eﬀectiveness of diﬀerent treatment methods, and which nations should be targeted in the application. We then generalise the investigation using the deterministic model. By analysing the stability of ﬁxed points in the model, we determine the relationship between parameters required to eradicate infections in the long-term. Qualitatively, key ﬁndings of the sensitivity analysis are:

<!-- b000009 | prose | pages [1] -->
• The most eﬀective short-term strategy in all countries is producing a large quantity of improved medicine

<!-- b000010 | prose | pages [1] -->
• The most eﬃcient strategy for reducing medium-term deaths is to improve medical services to isolate infected patients

<!-- b000011 | prose | pages [1] -->
• Short-term strategies will be most eﬀective in Sierra Leone and Liberia

<!-- b000012 | prose | pages [1] -->
• Medium-term strategies should target all three countries in the outbreak: Guinea, Sierra Leone, and Liberia

<!-- b000013 | prose | pages [1] -->
• Although vaccination is less eﬀective in the short and medium-term than other treatment methods in all countries, developing a vaccine is the only way to ensure that the virus can be eliminated in the long-term

<!-- b000014 | prose | pages [1] -->
These ﬁndings are used to produce recommendations of Ebola treatment strategy for the World Medical Association.

<!-- b000015 | furniture | pages [2] -->
Team #40764

<!-- b000016 | furniture | pages [2] -->
Page 2 of 25

<!-- b000017 | heading | pages [2] -->
1 Introduction

<!-- b000018 | prose | pages [2] -->
We present two models to predict the current Ebola outbreak in West Africa. The general approach in both models is to divide the population into three states, infected people, vulnerable healthy people, and immune healthy people, and consider the transitions between these states. Based on this approach, we develop stochastic and deterministic mathematical models to predict the spread of the virus. These models are also used to assess the impact of potential treatment methods.

<!-- b000019 | prose | pages [2] -->
The models are validated using data on the number of Ebola cases and deaths provided by the World Health Organisation. Both models show good agreement for the outbreak in four regions, to prove the robustness of the approach. The models are then extended to predict the future evolution of the data, if current treatment practices are preserved into the future. This provides a basis against which the eﬀects of diﬀerent treatment options are assessed independently.

<!-- b000020 | prose | pages [2] -->
The stochastic model is used to predict the short-term and medium-term eﬀects of three diﬀerent Ebola treatment options. These options are an improvement in medical services, improvement in available medicines, and developing a vaccine. We compare the eﬃciency of each method in three countries by comparing the reduction of total deaths predicted in the model with the percentage change required from current treatment levels. We ﬁnd that a large quantity of improved medicine is the most eﬀective short-term solution, but medical services become more eﬃcient in the medium term. In addition, we ﬁnd that treatment in the short-term should be targeted to Sierra Leone and Liberia, but in the medium-term, it is equally important to treat Guinea. Following this analysis, we generalise to ﬁnd the long-term impacts of diﬀerent treatment using the deterministic model. We ﬁnd that, although vaccines are less eﬃcient in the short and medium-term, the only way to ensure complete eradication of Ebola in the long term is to develop a vaccine. These ﬁndings inform recommendations to the World Medical Association to optimise the treatment of Ebola.

<!-- b000021 | heading | pages [2] -->
1.1 Problem Approach

<!-- b000022 | prose | pages [2] -->
To address the problem of eradicating Ebola, we initially present a general model that provides accurate predictions of the evolution of the outbreak in West Africa based on current treatment practices. To do this, we produce a general method, and ﬁnd parameters that match data provided by the World Health Organisation (2015a). Given an accurate model of the disease, we use it to isolate and predict the future impact of three diﬀerent types of additional treatment:

<!-- b000023 | prose | pages [2] -->
• Improving medical services, for example improved quarantine, and increased numbers of doctors and hospitals

<!-- b000024 | prose | pages [2] -->
• Improving medicine, for example that developed by the World Medical Association

<!-- b000025 | prose | pages [2] -->
• Developing and distributing a vaccine

<!-- b000026 | prose | pages [2] -->
We perform this analysis in each of the three countries in the primary Ebola outbreak: Guinea, Liberia, and Sierra Leone. Although the general model permits greater subdivision, the lack of data for smaller regions conﬁnes the investigation to three regions. The analysis provides insight into which treatment methods are most eﬀective, and which country would most beneﬁt from them. Based on our results, we provide recommendations to the World Medical Association in letter form.

<!-- b000027 | prose | pages [2] -->
A general model for the spread of Ebola is created by classifying each member of the population into one of three states. These states are

<!-- b000028 | prose | pages [2] -->
• People who are infected with Ebola

<!-- b000029 | prose | pages [2] -->
• Healthy people who are vulnerable to infection

<!-- b000030 | prose | pages [2, 3] -->
• Healthy people who are immune to infection As the disease spreads, people in the aﬀected areas undergo transitions between these three states. The generalised model is an open system, whereby total population can increase via births, and decrease via deaths. All possible state transitions are illustrated in Figure 1.

<!-- b000031 | furniture | pages [3] -->
Team #40764

<!-- b000032 | furniture | pages [3] -->
Page 3 of 25

<!-- b000034 | prose | pages [3] -->
Birth 1 2 ε ε Healthy 7 (Vulnerable) α 3 8 υ Infected 6 Healthy β 5 φ (Immune) γ 4 φ

<!-- b000035 | prose | pages [3] -->
Death

<!-- b000036 | caption | pages [3] -->
Figure 1: Possible transitions between population states in an Ebola outbreak

<!-- b000037 | prose | pages [3] -->
As Figure 1 shows, each of the eight state transition is assigned a number and a rate parameter. The rate parameters are deﬁned as the rate at which one person of the relevant state undergoes the state transition on a given day. They form the basis of the model, and are altered to model diﬀerent conditions. A list of these parameters is provided in Table 1.

<!-- b000038 | caption | pages [3] -->
Table 1: State transition rate parameters used in the general Ebola model

<!-- b000039 | prose | pages [3] -->
Parameter Description α The daily rate at which a healthy person is infected with Ebola β The daily recovery rate for a person with Ebola ν The daily vaccination rate per person γ The daily death rate per person for people infected with Ebola φ The daily death rate per person, for the healthy population ϵ The daily birth rate per person, assumed equal for both infected and healthy people

<!-- b000040 | prose | pages [3] -->
We deﬁne these parameters to represent the full set of possible transitions. The formulation is therefore suﬃcient to simulate the changes occurring in an Ebola outbreak. However, this interpretation relies on several assumptions, which are listed in Section 1.1.1.

<!-- b000041 | heading | pages [3] -->
1.1.1 Assumptions

<!-- b000042 | prose | pages [3, 4] -->
• The Ebola outbreak is conﬁned to Guinea, Liberia, and Sierra Leone. When developing the model, simulations of the spread of Ebola are performed for individual countries, and the spread of the virus as a whole. As the total number of cases and deaths from Ebola in other countries is small (eight deaths in Nigeria, as opposed to 1957 in Guinea (BBC 2015)), we assume that the entire outbreak occurs in Guinea, Liberia, and Sierra Leone • Population change depends on births and deaths only. We assume that net migration in each of the three countries is zero, as it is likely to be small relative to the overall population

<!-- b000043 | furniture | pages [4] -->
Team #40764

<!-- b000044 | furniture | pages [4] -->
Page 4 of 25

<!-- b000046 | prose | pages [4] -->
• The birth and death rates are constant. As the state transition parameters are constant, we must assume that the birth and death rate is constant. As the model’s calculations occur over a relatively short time, this is reasonable

<!-- b000047 | prose | pages [4] -->
• States are binary, and transition between states is instantaneous. We assume that each member of the population belongs to exactly one state at all times. This is reasonable for viral diseases such as Ebola. In addition, the severity of all cases is considered the same, which is reasonable when average data is used

<!-- b000048 | prose | pages [4] -->
• All people within a population are homogeneous. We assume that the spatial, gender, or age distributions do not aﬀect the rate parameters. This enables the rate parameters to be held constant in the model

<!-- b000049 | prose | pages [4] -->
• The virus does not mutate. There is no transition from immunity to vulnerability, as the model considers the spread of the current strain of the Ebola virus

<!-- b000050 | prose | pages [4] -->
• Recovery from Ebola is complete and independent. We assume that people who have recovered from Ebola have the same likelihood of death as other healthy people, and that a person’s recovery from Ebola does not depend on anyone else. Although healthy doctors provide vital assistance, the overall eﬀect of all healthy people on a patient’s recovery is negligible. In addition, we assume that antibodies generated in the recovery provide immunity from future infection. This is supported by Centers for Disease Control and Prevention (2014), which states that antibodies provide immunity from the same Ebola strain for at least ten years

<!-- b000051 | prose | pages [4] -->
• Infection with Ebola does not aﬀect birth rate. As the cycle of a person’s infection with Ebola is likely to last for much less than nine months, we assume that the birth rate for people with Ebola is the same as the rest of the population

<!-- b000052 | prose | pages [4] -->
• The possibility of death or recovery is independent of the Ebola infection cycle. In order to model state transitions by constant rates, we assume that the likelihood of death or recovery is the same regardless of how long a patient has been infected. The infected state is an average stage that represents all stages of the disease, for example incubation, infectious, recovering, etc.

<!-- b000053 | prose | pages [4] -->
• The virus is transferred between living people. Although Ebola is commonly contracted via contact with deceased (World Health Organisation 2014a), our model assumes that these people transfer the disease while living. This does not aﬀect overall rate of transmission. In addition, transmission between non-human species is neglected

<!-- b000054 | prose | pages [4] -->
• Treatment practices in place between 12 November 2014 and 5 February 2015 are constant. The models are developed based on data available from the World Health Organisation (WHO) between 12 November 2014 and 5 February 2015. The rate parameters therefore reﬂect the treatment practices available between these dates. Holding the rate parameters constant allows us to isolate variables when modelling new medicines and vaccines.

<!-- b000055 | prose | pages [4] -->
• Immunity is not passed on to the next generation. We assume that a survivor of Ebola cannot give birth to immune oﬀspring. We also assume that healthy parents give birth to healthy oﬀspring, and infected parents give birth to infected oﬀspring

<!-- b000056 | heading | pages [4] -->
2 Mathematical Models

<!-- b000057 | prose | pages [4, 5] -->
The problem interpretation described in Section 1.1 is solved using two mathematical models, a stochastic model and a deterministic model. The stochastic model provides a random simulation of the evolution of the disease, and simulates continuously in time. The deterministic model provides an analytical steady state solution, allowing analysis of ﬁxed points and stability. Both models provide a means to model the evolution of the disease based on existing data, and predict future trends.

<!-- b000058 | furniture | pages [5] -->
Team #40764

<!-- b000059 | furniture | pages [5] -->
Page 5 of 25

<!-- b000061 | heading | pages [5] -->
2.1 Stochastic Model

<!-- b000062 | prose | pages [5] -->
In the stochastic model, the probability of each transition occurring in a given timestep is calculated using the rate parameters, and then the evolution of the disease is simulated randomly. Deﬁnitions of parameters required for the stochastic model are given in Table 2.

<!-- b000063 | caption | pages [5] -->
Table 2: Parameters used in the stochastic model

<!-- b000064 | prose | pages [5] -->
Parameter Description n The timestep number dt The timestep size, given as a fraction of one day Pn The number of healthy, vulnerable people after n timesteps In The number of infected people after n timesteps Hn The number of healthy, immune people after n timesteps

<!-- b000065 | prose | pages [5] -->
The rate parameters in Table 1 provide a means of determining the probability that one event will occur in a given timestep. The timestep size, dt, is prescribed to ensure that a maximum of one transition of any type can occur in each timestep. In accordance with the eight transitions shown in Figure 1, the following shows the potential results of the subsequent timestep n + 1, and the probability that each event occurs.

<!-- b000066 | prose | pages [5] -->
 (In, Hn, Pn + 1) w.p. p1 = ϵ(Pn + Hn)dt    (In + 1, Hn, Pn) w.p. p2 = ϵIndt      (In, Hn, Pn −1) w.p. p3 = φPndt      (In, Hn −1, Pn) w.p. p4 = φHndt     (In+1, Hn+1, Pn+1) = (1) (In −1, Hn, Pn) w.p. p5 = γIndt  (In −1, Hn + 1, Pn) w.p. p6 = βIndt      (In + 1, Hn, Pn −1) w.p. p7 = αInPndt      (In, Hn + 1, Pn −1) w.p. p8 = νPndt     1 −P8  (In, Hn, Pn) w.p. i=1 pi 

<!-- b000067 | prose | pages [5] -->
For example, transition one is the birth of one healthy, but not immune person. The rate parameter ϵ provides the birth rate per person per day. In addition, we assume that all healthy people give birth to vulnerable healthy oﬀspring. Therefore, the probability of a healthy birth occurring in a given timestep is given by multiplying ϵ by the total number of healthy people, (Hn + Pn), and the fraction of one day for each timestep, dt. The result of this event is that the next timestep, n + 1, has one additional healthy person, i.e. Pn+1 = Pn + 1. The probabilities and outcomes of all other events are similarly determined (we note that the probability of transmission p7 depends on both the number of infected people and the number of vulnerable people). For the stochastic model to be valid, the timestep must be small enough such that 8 X pi ≤1, (2) i=1 which ensures that a maximum of one event can occur each timestep.

<!-- b000068 | prose | pages [5, 6] -->
Code to simulate this system is produced in Matlab. To generate the event for each timestep, a pseudo-random number r ∈[0, 1] is generated. An event is selected if r lies within the cumulative probability range up to that event. To keep track of the total number of cases and deaths due to Ebola, a counter that increments whenever a relevant event occurs is used. The simulation process is repeated for the desired number of timesteps to completely simulate an Ebola outbreak for a given initial state (I0, H0, P0).

<!-- b000069 | furniture | pages [6] -->
Team #40764

<!-- b000070 | furniture | pages [6] -->
Page 6 of 25

<!-- b000072 | heading | pages [6] -->
2.2 Deterministic Model

<!-- b000073 | prose | pages [6] -->
To implement the deterministic mode, we deﬁne Pn, In , and Hn in the same way as for the stochastic model, where the timestep number n represents a number of days. We then deﬁne functions f, g, and h containing diﬀerence equations for subsequent states. They are constructed using the same state transition rate parameters as the stochastic model. The diﬀerence equations are

<!-- b000074 | prose | pages [6] -->
 f(Pn, In, Hn) := Pn+1 = Pn(1 + ϵ −φ −ν −αIn) + ϵHn   (3) g(Pn, In, Hn) := In+1 = In(1 + ϵ −γ −β) + αInPn  h(Pn, In, Hn) := Hn+1 = Hn(1 −φ) + βIn + νPn. 

<!-- b000075 | prose | pages [6] -->
Unlike the stochastic model, the deterministic model only keeps track of the day-to-day number of people in each state. However, the system is easy to implement in Matlab, as randomness is not considered. Implementing the diﬀerence equations (3) in Matlab and iterating over n timesteps enables complete deterministic simulation of the Ebola outbreak for given initial conditions (I0, H0, P0).

<!-- b000076 | heading | pages [6] -->
2.3 Comparison of Models

<!-- b000077 | caption | pages [6] -->
Table 3 compares the relative strengths of the stochastic and deterministic models.

<!-- b000078 | caption | pages [6] -->
Table 3: Unique advantages of the stochastic and deterministic models

<!-- b000079 | prose | pages [6] -->
Stochastic Deterministic Randomness Repeated simulation not required State populations take integer values Analytical steady state solutions Timestep is eﬀectively continuous Less computational time Separate accounting of all state transitions

<!-- b000080 | prose | pages [6] -->
In our analysis, we take advantage of the unique features of the stochastic and deterministic models. The stochastic model provides a means to generate plots diﬀerent state transitions against time. This is used to compare with WHO data on the total number of Ebola cases and deaths. In addition, simulations using the stochastic model are used to perform sensitivity analysis on the parameters. This allows us to isolate the eﬀect of diﬀerent treatment practices. The deterministic model provides an analytical method to accurately analyse diﬀerent types of steady state solution, and determines the relationship between rate parameters required to drive Ebola infections to zero.

<!-- b000081 | heading | pages [6] -->
3 Results - Predicting the Spread of Ebola

<!-- b000082 | prose | pages [6] -->
We present stochastic and deterministic solutions for the spread of Ebola. The models are veriﬁed using data for the number of deaths and total cases in the 85 days from 12 November 2014 to 5 February 2015, which is available from the World Health Organisation (2015a). The development of an accurate model then enables us to make modiﬁcations based on diﬀerent treatment options.

<!-- b000083 | furniture | pages [7] -->
Team #40764

<!-- b000084 | furniture | pages [7] -->
Page 7 of 25

<!-- b000085 | heading | pages [7] -->
3.1 Model Parameters

<!-- b000086 | prose | pages [7] -->
To simulate the outbreak, we require numerical values for

<!-- b000087 | prose | pages [7] -->
• State transition rate parameters: α, β, ν, γ, φ, ϵ

<!-- b000088 | prose | pages [7] -->
• Initial conditions: I0, H0, P0

<!-- b000089 | prose | pages [7] -->
Where possible, we use realistic data to provide suitable estimates for these parameters. We predict the value of the parameters in all three countries independently, then combine them to produce a population-weighted average to model the outbreak as a whole. This method of prescribing the parameters provides a real-world basis for all state transitions in the model.

<!-- b000090 | prose | pages [7] -->
3.1.1 ν

<!-- b000091 | prose | pages [7] -->
As there is no current vaccine for Ebola (World Health Organisation 2015b) as of January 21 2015, we assume ν = 0 in the predictive model.

<!-- b000092 | prose | pages [7] -->
3.1.2 ϵ, φ

<!-- b000093 | prose | pages [7] -->
CountryMeters (2015) provides live population estimates, as well as data on the birth and death rates of each country. Table 4 gives this data for the three relevant countries on 5 February 2015.

<!-- b000094 | caption | pages [7] -->
Table 4: Live population statistics for February 5 2015 (CountryMeters 2015)

<!-- b000095 | prose | pages [7] -->
Birth Rate [ppl d−1] Death Rate [ppl d−1] Country Population Guinea 12,414,680 1,150 326 Liberia 4,615,917 425 121 Sierra Leone 6,404,599 626 191 Overall 23,436,196 2,201 638

<!-- b000096 | prose | pages [7] -->
The birth and death rate parameters, ϵ and φ respectively, are determined by

<!-- b000097 | prose | pages [7] -->
ϵ = Birth Rate Population, (4)

<!-- b000098 | prose | pages [7] -->
and φ = Death Rate Population . (5)

<!-- b000099 | prose | pages [7] -->
These give the rate at which one healthy person will give birth or die respectively. The initial population at 12 November 2014 is estimated by subtracting the net births over the 85 preceding days from the population given in Table 4,

<!-- b000100 | prose | pages [7] -->
Initial Population = Final Population −85(Birth Rate −Death Rate). (6)

<!-- b000101 | prose | pages [7] -->
Performing these operations gives the results in Table 5.

<!-- b000102 | caption | pages [7] -->
Table 5: Population parameters for use in the model

<!-- b000103 | prose | pages [7, 8] -->
Country ϵ φ Initial Population Guinea 9.3175e-5 2.6386e-5 12,343,779 Liberia 9.2567e-5 2.6392e-5 4,589,796 Sierra Leone 9.8295e-5 2.9981e-5 6,367,191 Overall 9.4455e-5 2.7369e-5 23,300,766 3.1.3 I0, H0, P0

<!-- b000104 | furniture | pages [8] -->
Team #40764

<!-- b000105 | furniture | pages [8] -->
Page 8 of 25

<!-- b000107 | prose | pages [8] -->
The initial population found in Section 3.1.2 entirely consists of the three states of the general model, I0, H0, and P0. To determine the initial population of each of the states, we consider WHO data for the number of Ebola cases from November 12 2014. This data is given in Table 6.

<!-- b000108 | caption | pages [8] -->
Table 6: WHO Ebola data for November 12 2014 (World Health Organisation 2015a)

<!-- b000109 | prose | pages [8] -->
Country Total Cases Total Deaths Guinea 1,878 1,142 Liberia 6,822 2,836 Sierra Leone 5,368 1,169 Overall 14,068 5,147

<!-- b000110 | prose | pages [8] -->
To estimate I0, we assume that all reported cases that have not resulted in death are still infected, and therefore I0 = Total Cases −Total Deaths. (7) Although this neglects the possibility that a reported case has recovered from the virus, which would lead to overestimating I0, we accept the assumption. This is because the total number of infections is low relative to the total population, the WHO acknowledge that their statistics underestimate the Ebola epidemic (World Health Organisation 2014b), and that it is diﬃcult to otherwise predict current infections from the data. Based on this assumption, we also have

<!-- b000111 | prose | pages [8] -->
H0 = 0, (8)

<!-- b000112 | prose | pages [8] -->
and P0 = Initial Population −I0. (9) This gives the following values for the initial states.

<!-- b000113 | caption | pages [8] -->
Table 7: Initial states for the Ebola model

<!-- b000114 | prose | pages [8] -->
Country I0 P0 Guinea 736 12,343,043 Liberia 3,986 4,585,810 Sierra Leone 4,199 6,362,992 Overall 8,921 23,291,845

<!-- b000115 | prose | pages [8] -->
3.1.4 α, β, γ

<!-- b000116 | prose | pages [8] -->
The parameters α, β, and γ are more diﬃcult to determine from available data. As an infected person will eventually transition to health or death, an important factor is the mortality rate of Ebola. An estimate of mortality rate, i.e. the likelihood of eventual death once infected, is given by Mortality Rate = Total Deaths Total Cases . (10)

<!-- b000117 | prose | pages [8] -->
For this calculation, we use the latest data, to reduce the proportion of ongoing cases. This data is given in Table 8.

<!-- b000118 | caption | pages [8] -->
Table 8: WHO Ebola data for February 5 2015 (World Health Organisation 2015a)

<!-- b000119 | prose | pages [8, 9] -->
Country Total Cases Total Deaths Mortality Rate Guinea 2,986 1,947 0.65204 Liberia 8,745 3,746 0.42836 Sierra Leone 10,756 3,286 0.30550 Overall 22,487 8,979 0.39930 However, to determine the daily rate of death and recovery, we introduce another parameter, T, the disease residence time. This is the average number of days required for an infection to result in either death or recovery. Using this parameter, we can determine the daily rates of death (γ) and recovery (β) among infected people, using γ = Mortality Rate , (11) T and β = 1 −Mortality Rate . (12) T To determine α, the rate of disease transmission, we introduce the parameter K, the average number of healthy people to whom each infected person transmits the disease during the period they are infected. The parameter α is therefore given by K α = . (13) TP0 As there is no reliable data available to determine T and K, their values are prescribed to ﬁt the WHO data. Doing this ensures that our model is accurate, and allowing K to come as part of the solution provides a prediction of the transmission rate in current conditions. The parameters shown in Table 9 result in suitable estimates of the ﬁnal death and case counts post-simulation.

<!-- b000120 | furniture | pages [9] -->
Team #40764

<!-- b000121 | furniture | pages [9] -->
Page 9 of 25

<!-- b000123 | caption | pages [9] -->
Table 9: Appropriate values of parameters

<!-- b000124 | prose | pages [9] -->
Country K T α β γ Guinea 0.90 45 1.6203e-9 7.7324e-3 1.4490e-2 Liberia 0.89 155 1.2521e-9 3.6880e-3 2.7636e-3 Sierra Leone 0.79 42 2.9561e-9 1.6536e-3 7.2739e-3 Overall 0.86 73 5.0992e-10 8.2775e-3 5.5022e-3

<!-- b000125 | prose | pages [9] -->
To determine if the calculated values of K are appropriate, we cite a study by Meltzer et al. (2015), which gives estimates for K in various situations:

<!-- b000126 | prose | pages [9] -->
• For hospitalised patients, K = 0.12

<!-- b000127 | prose | pages [9] -->
• For home patients with eﬀective isolation, K = 0.18

<!-- b000128 | prose | pages [9] -->
• For home patients without eﬀective isolation, K = 1.8 (Meltzer et al. 2015)

<!-- b000129 | prose | pages [9] -->
All average values of K predicted in Table 9 are therefore feasible based on combinations of current treatment techniques. To validate residence time T, we cite a survivor’s anecdote in which the patient ﬁrst noticed symptoms after a ten day incubation, and reached their worst condition after sixteen days (Grant 2014). Assuming it takes a further sixteen days to recover fully gives T that corresponds closely to Table 9. However, considering the result of Liberia, we infer that an appropriate T comes as an artefact of other aspects of the model, rather than from a physical basis.

<!-- b000130 | heading | pages [9] -->
3.2 Validation

<!-- b000131 | prose | pages [9] -->
The constant values of the parameters deﬁned in Section 3.1 completely specify the constants required to implement both the stochastic and deterministic models. These are used in both models to produce simulations for the spread of Ebola over the WHO reporting period. These simulations are compared with the WHO data to validate the models.

<!-- b000132 | heading | pages [9] -->
3.2.1 Stochastic Model

<!-- b000133 | prose | pages [9, 10] -->
To produce stochastic results, the Matlab simulation is run ten times for each of the four regions modelled. The simulation is run over 85 days to simulate the period from 12 November 2014 to 5 February 2015. The average number of cases and deaths at the end of the simulation are compared with WHO data to determine whether the model is accurate. Results are presented in Table 10. In the table, C and D represent the number of cases and deaths reported on February 5 2015 respectively, and subscripts M and W refer to the stochastic model and WHO data respectively. The parameter σ is the standard deviation of the ten simulation results.

<!-- b000134 | furniture | pages [10] -->
Team #40764

<!-- b000135 | furniture | pages [10] -->
Page 10 of 25

<!-- b000137 | caption | pages [10] -->
Table 10: Results for February 5 2015 of stochastic simulations used to validate the model

<!-- b000138 | prose | pages [10] -->
|CM−CW |DM−DW | | Country CM σC DM σD CW DW σC σD Guinea 3,053 110 1,957 50 2,986 1,947 0.61 0.20 Liberia 8,748 51 3,749 20 8,745 3,746 0.059 0.15 Sierra Leone 10,813 159 3,284 57 10,756 3,286 0.36 0.035 Overall 22,557 150 9,041 54 22,487 8,979 0.47 1.1

<!-- b000139 | prose | pages [10] -->
Note: ‘Overall’ in Table 10 represents the results of a separate simulation using parameters for the overall outbreak, not an arithmetic sum of results for each nation

<!-- b000140 | caption | pages [10] -->
Table 10 shows that the model predictions for total deaths and cases is very similar to the statistics

<!-- b000141 | prose | pages [10] -->
reported by the WHO. The fact that the real value falls within half a standard deviation of the model prediction in ﬁve of the eight statistics, and that no result is more than 1.1 standard deviations away from the actual value. We therefore conclude that the parameters in Section 3.1 accurately model the Ebola outbreak in all cases.

<!-- b000142 | prose | pages [10] -->
Further validation is provided by plotting simulation results against day-to-day WHO data for deaths and cases. Examples are provided in Figure 2.

<!-- b000143 | prose | pages [10] -->
2100 3800 WHO WHO Simulations 2000 3700 Simulations 1900 3600 1800 3500 Total Deaths Total Deaths 1700 3400 1600 3300 1500 3200 1400 3100 1300 3000 1200 2900 1100 2800 0 10 20 30 40 50 60 70 80 90 0 10 20 30 40 50 60 70 80 90 Time [d] Time [d]

<!-- b000144 | prose | pages [10] -->
(a) Guinea (b) Liberia

<!-- b000145 | prose | pages [10] -->
3500 9500 WHO WHO 9000 Simulations Simulations 3000 8500

<!-- b000146 | prose | pages [10] -->
8000 Total Deaths Total Deaths 2500 7500

<!-- b000147 | prose | pages [10] -->
7000 2000 6500

<!-- b000148 | prose | pages [10] -->
6000 1500 5500

<!-- b000149 | prose | pages [10] -->
1000 5000 0 10 20 30 40 50 60 70 80 90 0 10 20 30 40 50 60 70 80 90 Time [d] Time [d]

<!-- b000150 | prose | pages [10, 11] -->
(c) Sierra Leone (d) Overall As Figure 2 shows, the simulations track the WHO reported daily death count reasonably well. The model predictions produce a more linear trend than the WHO data as we assume the treatment practices (state transition rate parameters) are constant throughout the period. In addition, the WHO data is taken at irregular intervals, and each country updates their data on diﬀerent dates. This suggests the WHO data points may not accurately display the underlying trend in disease spread. We therefore accept the predictions of the model are valid based on WHO data.

<!-- b000151 | caption | pages [10] -->
Figure 2: Comparison of simulation results and WHO data for day-to-day death count in each region

<!-- b000152 | furniture | pages [11] -->
Team #40764

<!-- b000153 | furniture | pages [11] -->
Page 11 of 25

<!-- b000155 | heading | pages [11] -->
3.2.2 Deterministic Model

<!-- b000156 | prose | pages [11] -->
As the deterministic model only considers the population of the three states In, Hn, and Pn, and does not account for state transitions, we cannot compare with WHO data. However, given the success of the stochastic model, we assume that the deterministic model matches WHO data if its results match the stochastic model. Table 11 shows the results for February 5 2015 of simulating the deterministic model with the parameters in Section 3.1. In the table, subscripts D and S denote the deterministic and stochastic models respectively.

<!-- b000157 | caption | pages [11] -->
Table 11: Comparison of stochastic and deterministic results for February 5 2015

<!-- b000158 | prose | pages [11] -->
Country IS ID HS HD PS PD Guinea 640 618 457 438 12,412,178 12,411,344 Liberia 3,769 3,789 1,228 1,203 4,609,770 4,609,491 Sierra Leone 2,718 2,789 4,805 4,789 6,394,555 6,394,146 Overall 7,690 7,684 5,820 5,757 23,419,606 23,417,858

<!-- b000159 | prose | pages [11] -->
As expected, the deterministic model shows good agreement with the stochastic simulations if the same parameters are used in the model. A reason for the small discrepancy in the results is that the timestep used in each simulation is diﬀerent. The stochastic model applies a near-continuous timestep, whilst the deterministic model is updated using a timestep of one day. The stochastic model also incorporates randomness, which creates deviations from deterministic results. An example of this is illustrated in Figure 3.

<!-- b000160 | prose | pages [11] -->
9000 9000 Stochastic

<!-- b000161 | prose | pages [11] -->
8500 8500

<!-- b000162 | prose | pages [11] -->
In In

<!-- b000163 | prose | pages [11] -->
8000 8000

<!-- b000164 | prose | pages [11] -->
Deterministic 7500 7500 0 0 10 10 20 20 30 30 40 40 50 50 60 60 70 70 80 80 90 90 Time [d] Time [d]

<!-- b000165 | caption | pages [11] -->
Figure 3: Comparison of number of infected patients over time for the overall virus, for both

<!-- b000166 | prose | pages [11, 12] -->
deterministic and stochastic models deterministic solution. We conclude that both the deterministic and stochastic models provide a means of accurately tracking the spread of Ebola. In our analysis of the predicted eﬀects of possible treatment regimes, we use the predictions of both models.

<!-- b000167 | furniture | pages [12] -->
Team #40764

<!-- b000168 | furniture | pages [12] -->
Page 12 of 25

<!-- b000169 | caption | pages [12] -->
Figure 3 shows that the stochastic models introduce random ﬂuctuations about the underlying

<!-- b000171 | heading | pages [12] -->
4 Results - Predicting the Eﬀect of Improved Treatment

<!-- b000172 | prose | pages [12] -->
To determine the eﬀect of new treatment regimes, the February 5 2015 parameters given in Table 11 are used as initial states (I0, H0, P0) to the model. We initially consider the projected spread of Ebola if the treatment regime in practice from 12 November 2014 to 5 February 2015 is maintained – that is, if the values of state transition rate parameters determined based on WHO data are held constant. The simulations are run in both the short-term (using the stochastic model), and the long term (using the deterministic model). We then independently change parameters based on our interpretations of diﬀerent options to improve treatment. To provide targeted treatment, we perform the simulations in each of the three nations. The possible treatment options are described in Section 4.1.

<!-- b000173 | heading | pages [12] -->
4.1 Treatment Options

<!-- b000174 | prose | pages [12] -->
In our analysis, we consider three diﬀerent treatment options. Each has a unique eﬀect on the state transition rate parameters. The treatment options are

<!-- b000175 | prose | pages [12] -->
• Improving medical services

<!-- b000176 | prose | pages [12] -->
• Improving medicine

<!-- b000177 | prose | pages [12] -->
• Developing a vaccine

<!-- b000178 | heading | pages [12] -->
4.1.1 Improve Medical Services - Decrease α

<!-- b000179 | prose | pages [12] -->
Improved medical services entail improved quarantine procedures, for example by increasing medical staﬀ, hospital space, or public education. Doing this will improve patient isolation, decreasingα the rate of Ebola transmission from infected to healthy people. If we assume that it is impossible to isolate a patient in the incubation stage, which lasts a quarter of infection residence time, data from Meltzer et al. (2015) provides a means of estimating the minimum K.

<!-- b000180 | prose | pages [12] -->
Kmin = 0.75(0.12) + 0.25(1.8) = 0.54. (14)

<!-- b000181 | prose | pages [12] -->
As this is less than the model predictions in Table 9, there is scope to reduce the spread of the virus by improving medical services.

<!-- b000182 | heading | pages [12] -->
4.1.2 Improve Medicine - Decrease γ, Increase β

<!-- b000183 | prose | pages [12] -->
We deﬁne ‘medicine’ to incorporate all techniques available to reduce the mortality rate, including existing techniques such as providing intravenous nutrients, and newly developed drugs, for example by the World Medical Association. As the WMA medicine aﬀects patients even in the early stages of infection, we assume that improving either the quality or quantity of medicine will decrease the average mortality of an infected patient. This increases the rate of recovery, β, and decreases the rate of death from infection, γ. We consider the eﬀects of a range of medicine eﬀectiveness in our predictions. Changing the relevant parameters encompasses changes in the quantity of medicine, as well as the eﬀectiveness of distribution systems.

<!-- b000184 | furniture | pages [13] -->
Team #40764

<!-- b000185 | furniture | pages [13] -->
Page 13 of 25

<!-- b000186 | heading | pages [13] -->
4.1.3 Develop Vaccine - Increase ν

<!-- b000187 | prose | pages [13] -->
Developing a vaccine opens the possibility of transition from the vulnerable healthy state to the immune healthy state. This will decrease the rate of Ebola spread. To model a vaccine, we consider non-zero ν. As there is no vaccine available, we consider a range of diﬀerent distribution speeds in our simulations. In our simulation ν is related to the number of successful vaccinations.

<!-- b000188 | heading | pages [13] -->
4.2 Sensitivity Analysis

<!-- b000189 | prose | pages [13] -->
Sensitivity analysis is performed using both the stochastic and deterministic models. Short and medium-term simulations of six months, one year, and two years are performed using the stochastic model. These are important to guide immediate prevention strategy, and some assumptions (e.g. immunity is retained) are more likely to hold in the short-term. Long-term steady state conditions are predicted using the deterministic model. Speciﬁcally, we seek combinations of rate parameters that drive the steady-state number of infections to zero.

<!-- b000190 | heading | pages [13] -->
4.2.1 Stochastic Model

<!-- b000191 | prose | pages [13] -->
Stochastic simulations are Short-Term Projections Based on Current Treatment Levels performed using the same rate parameters and February 5 2015 initial values to predict the total number of cases and deaths in each country over six months, one year, and two years at the current level of treatment. As with the initial modelling the average of ten simulations is taken. These results are presented in Table 12. In the table, C and D represent the number of new cases since February 5 2015. We change this convention as we no longer need to match WHO data, the initial states are better deﬁned, and new cases provides a better indication of disease spread.

<!-- b000192 | caption | pages [13] -->
Table 12: Projection of Ebola spread at current level of treatment (new cases and new deaths)

<!-- b000193 | heading | pages [13] -->
6 Months

<!-- b000194 | heading | pages [13] -->
1 Year

<!-- b000195 | heading | pages [13] -->
2 Years

<!-- b000196 | prose | pages [13] -->
Country

<!-- b000197 | heading | pages [13] -->
C D

<!-- b000198 | heading | pages [13] -->
C D

<!-- b000199 | heading | pages [13] -->
C D

<!-- b000200 | prose | pages [13] -->
Guinea 2,049 1,441 3,625 2,549 6,093 4,201 Liberia 3,873 1,828 7,303 3,428 13,857 6,391 Sierra Leone 6,262 2,380 9,180 3,479 11,199 4,224

<!-- b000201 | prose | pages [13] -->
In our analysis, we consider ten percent changes in the relevant parameters, and other reasonable targets based on improved treatment methods. This is suitable for short term modelling, where large-scale changes are unlikely to be possible. We apply the stochastic model for each of the three nations, to determine which strategy is most useful in the short-term, and where they are optimally applied. In each case, data is the average of ten stochastic simulations.

<!-- b000202 | prose | pages [13] -->
Eﬀect of Improving Medical Services To assess the impact of increasing medical services in an individual country over six months, one year, and two years, we consider two cases:

<!-- b000203 | prose | pages [13] -->
• A 10% decrease in transmissions per infected person, i.e. decreasing α by 10%

<!-- b000204 | prose | pages [13] -->
• Decrease transmissions per infected person to the minimum, Kmin = 0.54

<!-- b000205 | prose | pages [13] -->
All other parameters are held constant in the stochastic simulations, and once again an average of ten simulations is taken. The results are given in terms of the overall reduction in deaths or cases measured after the given period. Intermediate data processing is omitted for simplicity. The results are given in Table 13 and Table 14 respectively.

<!-- b000206 | furniture | pages [14] -->
Team #40764

<!-- b000207 | furniture | pages [14] -->
Page 14 of 25

<!-- b000208 | caption | pages [14] -->
Table 13: Net change in cases and deaths if transmissions per infected person is decreased by 10%

<!-- b000209 | heading | pages [14] -->
6 Months

<!-- b000210 | heading | pages [14] -->
1 Year

<!-- b000211 | heading | pages [14] -->
2 Years

<!-- b000212 | prose | pages [14] -->
Country

<!-- b000213 | heading | pages [14] -->
C D

<!-- b000214 | heading | pages [14] -->
C D

<!-- b000215 | heading | pages [14] -->
C D

<!-- b000216 | prose | pages [14] -->
Guinea -589 -280 -1,386 -771 -2,956 -1,780 Liberia -576 -119 -1,359 -332 -3,491 -1,081 Sierra Leone -1,323 -310 -2,672 -731 -4,395 -1,347

<!-- b000217 | caption | pages [14] -->
Table 14: Net change in cases and deaths if transmissions per infected person is decreased to the

<!-- b000218 | prose | pages [14] -->
minimum, K = 0.54

<!-- b000219 | heading | pages [14] -->
6 Months

<!-- b000220 | heading | pages [14] -->
1 Year

<!-- b000221 | heading | pages [14] -->
2 Years

<!-- b000222 | prose | pages [14] -->
Country

<!-- b000223 | heading | pages [14] -->
C D

<!-- b000224 | heading | pages [14] -->
C D

<!-- b000225 | heading | pages [14] -->
C D

<!-- b000226 | prose | pages [14] -->
Guinea -1,378 -654 -2,889 -1,667 -5,325 -3,288 Liberia -1,898 -335 -4,196 -1,057 -9,562 -3,156 Sierra Leone -3,440 -808 -5,901 -1,673 -7,912 -2,421

<!-- b000227 | prose | pages [14] -->
Eﬀect of Improving Medicine To assess the impact of improving medicines, we consider:

<!-- b000228 | prose | pages [14] -->
• A 10% decrease in average mortality rate

<!-- b000229 | prose | pages [14] -->
• Distribution of a new WMA medicine such that average mortality rate is decreased to 30% in all regions

<!-- b000230 | prose | pages [14] -->
• Distribution of a new WMA medicine such that average mortality rate is decreased to 15% in all regions

<!-- b000231 | prose | pages [14] -->
The eﬀects of mortality rate on the parameters β and γ are determined by Equations (11) and (12). Average simulation results are given in Table 15, Table 16 and Table 17 respectively. In these tables, any increases in cases occurring in some simulations are likely to be caused by randomness.

<!-- b000232 | caption | pages [14] -->
Table 15: Net change in cases and deaths if mortality rate is decreased by 10%

<!-- b000233 | heading | pages [14] -->
6 Months

<!-- b000234 | heading | pages [14] -->
1 Year

<!-- b000235 | heading | pages [14] -->
2 Years

<!-- b000236 | prose | pages [14] -->
Country

<!-- b000237 | heading | pages [14] -->
C D

<!-- b000238 | heading | pages [14] -->
C D

<!-- b000239 | heading | pages [14] -->
C D

<!-- b000240 | prose | pages [14] -->
Guinea -116 -205 -311 -393 -199 -532 Liberia +18 -193 +146 -304 -25 -676 Sierra Leone +121 -175 -105 -380 -423 -575

<!-- b000241 | caption | pages [14] -->
Table 16: Net change in cases and deaths if the medicine decreases mortality rate to 30% in all regions

<!-- b000242 | heading | pages [14] -->
6 Months

<!-- b000243 | heading | pages [14] -->
1 Year

<!-- b000244 | heading | pages [14] -->
2 Years

<!-- b000245 | prose | pages [14] -->
Country

<!-- b000246 | heading | pages [14] -->
C D

<!-- b000247 | heading | pages [14] -->
C D

<!-- b000248 | heading | pages [14] -->
C D

<!-- b000249 | prose | pages [14] -->
Guinea -23 -775 -124 -1,215 -586 -2,401 Liberia -31 -571 -24 -1,022 +7 -1,896 Sierra Leone +75 -3 -231 -147 -239 -178

<!-- b000250 | caption | pages [14] -->
Table 17: Net change in cases and deaths if the medicine decreases mortality rate to 15% in all regions

<!-- b000251 | heading | pages [14] -->
6 Months

<!-- b000252 | heading | pages [14] -->
1 Year

<!-- b000253 | heading | pages [14] -->
2 Years

<!-- b000254 | prose | pages [14] -->
Country

<!-- b000255 | heading | pages [14] -->
C D

<!-- b000256 | heading | pages [14] -->
C D

<!-- b000257 | heading | pages [14] -->
C D

<!-- b000258 | prose | pages [14, 15] -->
Guinea -15 -1,109 -151 -1,974 -748 -3,333 Liberia -43 -1,196 +111 -2,221 +2 -4,159 Sierra Leone +67 -1,188 +14 -1,743 +62 -2,168 Eﬀect of Vaccination To assess the impact of distributing an eﬀective vaccine, we consider:

<!-- b000259 | furniture | pages [15] -->
Team #40764

<!-- b000260 | furniture | pages [15] -->
Page 15 of 25

<!-- b000262 | prose | pages [15] -->
• A vaccination distribution rate in which approximately 10% of the population will be successfully vaccinated in two years

<!-- b000263 | prose | pages [15] -->
• A vaccination distribution rate in which approximately 30% of the population will be successfully vaccinated in two years

<!-- b000264 | prose | pages [15] -->
• A vaccination distribution rate in which approximately 50% of the population will be successfully vaccinated in two years

<!-- b000265 | prose | pages [15] -->
The parameter ν is given by ν = V 730, (15)

<!-- b000266 | prose | pages [15] -->
where V is the proportion of the population that is vaccinated in two years. This gives ν = 1.3699e-4, ν = 4.1096e-4, and ν = 6.8493e-4 for the three respective cases. Simulating the stochastic model with these parameters gives results shown in Table 18, Table 19, and Table 20.

<!-- b000267 | caption | pages [15] -->
Table 18: Net change in cases and deaths if a vaccine is introduced to approximately 10% of the

<!-- b000268 | prose | pages [15] -->
population in two years

<!-- b000269 | heading | pages [15] -->
6 Months

<!-- b000270 | heading | pages [15] -->
1 Year

<!-- b000271 | heading | pages [15] -->
2 Years

<!-- b000272 | prose | pages [15] -->
Country

<!-- b000273 | heading | pages [15] -->
C D

<!-- b000274 | heading | pages [15] -->
C D

<!-- b000275 | heading | pages [15] -->
C D

<!-- b000276 | prose | pages [15] -->
Guinea -149 -68 -451 -250 -1,578 -911 Liberia -39 -32 -219 -36 -1,313 -347 Sierra Leone -10 +25 -488 -130 -1,045 -315

<!-- b000277 | caption | pages [15] -->
Table 19: Net change in cases and deaths if a vaccine is introduced to approximately 30% of the

<!-- b000278 | prose | pages [15] -->
population in two years

<!-- b000279 | heading | pages [15] -->
6 Months

<!-- b000280 | heading | pages [15] -->
1 Year

<!-- b000281 | heading | pages [15] -->
2 Years

<!-- b000282 | prose | pages [15] -->
Country

<!-- b000283 | heading | pages [15] -->
C D

<!-- b000284 | heading | pages [15] -->
C D

<!-- b000285 | heading | pages [15] -->
C D

<!-- b000286 | prose | pages [15] -->
Guinea -246 -108 -965 -515 -2,688 -1,586 Liberia -159 -52 -614 -138 -3,367 -943 Sierra Leone -370 -60 -1,230 -302 -2,844 -849

<!-- b000287 | caption | pages [15] -->
Table 20: Net change in cases and deaths if a vaccine is introduced to approximately 50% of the

<!-- b000288 | prose | pages [15] -->
population in two years

<!-- b000289 | heading | pages [15] -->
6 Months

<!-- b000290 | heading | pages [15] -->
1 Year

<!-- b000291 | heading | pages [15] -->
2 Years

<!-- b000292 | prose | pages [15] -->
Country

<!-- b000293 | heading | pages [15] -->
C D

<!-- b000294 | heading | pages [15] -->
C D

<!-- b000295 | heading | pages [15] -->
C D

<!-- b000296 | prose | pages [15] -->
Guinea -310 -127 -1,054 -564 -3,363 -1,999 Liberia -318 -55 -1,118 -215 -4,963 -1,463 Sierra Leone -513 -76 -1,798 -477 -3,539 -1,033

<!-- b000297 | prose | pages [15] -->
Analysis We assume that the primary measure of an eﬀective treatment is to prevent the highest number of total deaths. Therefore, to illustrate the most eﬃcient treatment method, we plot the reduction in total deaths against the medium-term percentage change in current treatment conditions, for each nation and type of treatment. In lieu of cost data, we assume that treatment eﬃciency is proportional to the reduction in deaths per percentage change in treatment. When parameters are set to uniform values across all regions, percentage change is calculated based on the initial value for the particular region. For example, change in mortality due to medicine is determined with respect to values in Table 8. The resulting short-term (six months) and medium-term (two years) plots are shown in Figure 4 and Figure 5 respectively.

<!-- b000298 | furniture | pages [16] -->
Team #40764

<!-- b000299 | furniture | pages [16] -->
Page 16 of 25

<!-- b000300 | prose | pages [16] -->
1500

<!-- b000301 | prose | pages [16] -->
Net Six−Month Reduction in Deaths 1000

<!-- b000302 | prose | pages [16] -->
Guinea 500 Liberia Sierra Leone Medical Services Medicine Vaccine 0 0 20 40 60 80 100 Percentage Increase in Treatment [%]

<!-- b000303 | caption | pages [16] -->
Figure 4: Net short-term (six month) reduction in deaths vs. percentage increase in treatment for

<!-- b000304 | prose | pages [16] -->
diﬀerent nations and treatment methods

<!-- b000305 | prose | pages [16] -->
5000

<!-- b000306 | prose | pages [16] -->
Net Two−Year Reduction in Deaths 4500

<!-- b000307 | prose | pages [16] -->
4000

<!-- b000308 | prose | pages [16] -->
3500

<!-- b000309 | prose | pages [16] -->
3000

<!-- b000310 | prose | pages [16] -->
2500

<!-- b000311 | prose | pages [16] -->
2000 Guinea Liberia 1500 Sierra Leone 1000 Medical Services Medicine 500 Vaccine

<!-- b000312 | prose | pages [16] -->
0 0 10 20 30 40 50 60 70 80 90 100 Percentage Increase in Treatment [%]

<!-- b000313 | caption | pages [16] -->
Figure 5: Net medium term (two year) reduction in deaths vs. percentage increase in treatment for

<!-- b000314 | prose | pages [16, 17] -->
diﬀerent nations and treatment methods In these ﬁgures, treatments that appear above the dotted trendline are relatively eﬃcient, and are therefore recommended for implementation. This is because they require a reduced percentage increase in treatment to achieve relatively greater reductions in death.

<!-- b000315 | furniture | pages [17] -->
Team #40764

<!-- b000316 | furniture | pages [17] -->
Page 17 of 25

<!-- b000318 | prose | pages [17] -->
In the short-term results show that improving medicine and medical services are more eﬃcient method of reducing deaths than vaccination. The most eﬀective methods of reducing death in the short-term are medicines that substantially decrease the average mortality rate. For example, in Sierra Leone, an eﬀective medicine can save 47% more lives in the short-term than the maximum possible improvement in medical services. These results are sensible considering the evolution of disease. The vaccine will not prevent many cases in the short-term, and more immediate treatment methods such as medicine are more eﬀective in reducing short-term deaths. Also, the results show that greater eﬃciencies are attained when the short-term strategies are deployed in Sierra Leone. This is because it has a higher number of initial cases.

<!-- b000319 | prose | pages [17] -->
However, as the medicine does not cause signiﬁcant reductions in the number of cases over two years, its eﬀectiveness in reducing deaths is decreased in the medium-term relative to other treatment methods. As Figure 5 shows, vaccination becomes a more competitive treatment option in the medium-term, whilst improving medical services is still important. In addition, the eﬃciency of introducing the three treatment methods is similar in each nation. Health services and vaccinations have a strong eﬀect in Guinea in gross and relative terms. This ﬁnding is important, as Guinea has by far the lowest proportion of cases of the three nations, and will be neglected if treatment is allocated according to this proportionality alone.

<!-- b000320 | prose | pages [17] -->
Based on this analysis, we recommend short-term provision of improved medical services and medicine, especially targeting aﬀected areas in Sierra Leone. However, if research shows that the current Ebola strain is likely to last up to two years, vaccination becomes a viable strategy, and all nations should be targeted for improved medical services and medicine. It must be emphasised that this analysis does not determine the relative cost of each treatment method. Cost-beneﬁt analysis is left to policy-makers with knowledge of the cost of each treatment method. The result is likely to be quite diﬀerent from the conclusions expressed here.

<!-- b000321 | heading | pages [17] -->
4.2.2 Deterministic Model

<!-- b000322 | prose | pages [17] -->
Long-term projections of the Long-Term Projections Based on Current Treatment Levels evolution of the Ebola outbreak are performed using the deterministic model. Once again, the rate parameters used are the constant values found to accurately predict the disease in the WHO’s reporting period. Results are shown in Figure 6.

<!-- b000323 | prose | pages [17] -->
5 7 7 x 10 x 10 x 10 14 18 3.4 16 12 3.2 14 10 12 3 8 10 Hn Pn In 2.8 8 6 6 2.6 4 4 2.4 2 2 0 0 2.2 0 1 2 3 4 5 6 0 1 2 3 4 5 6 0 1 2 3 4 5 6 Time [d] Time [d] Time [d] 4 4 4 x 10 x 10 x 10

<!-- b000324 | prose | pages [17, 18] -->
(a) Infected (b) Immune (c) Vulnerable Using the numbers for the overall outbreak, we ﬁnd that the number of infected and immune people diverge to inﬁnity, whilst the number of vulnerable people is stable. The model therefore emphasises the urgent necessity of improving treatment. In particular, the ﬁrst peak in the infected plot occurs after about 3000 days, so at minimum, medium-term strategies such as those suggested by the stochastic model are required. In addition to this, analysing the ﬁxed points of the deterministic model provides insight into parameter relationships that drive long-term steady state number of infections to zero.

<!-- b000325 | caption | pages [17] -->
Figure 6: Long-term deterministic simulation of the overall virus

<!-- b000326 | furniture | pages [18] -->
Team #40764

<!-- b000327 | furniture | pages [18] -->
Page 18 of 25

<!-- b000329 | heading | pages [18] -->
Fixed Point and Stability of Deterministic Model

<!-- b000330 | prose | pages [18] -->
To analyse the long-term eﬀects of changing the state transition rate parameters in a general outbreak, we consider the ﬁxed points of the deterministic system. We then determine relationships between the parameters that lead to stable solutions that eradicate the virus. The structure of treatment can then be altered based on the results to produce a strategy that eradicates Ebola long-term.

<!-- b000331 | prose | pages [18] -->
To determine the ﬁxed points of the system, we recall the deterministic diﬀerence equations (3),

<!-- b000332 | prose | pages [18] -->
 f(Pn, In, Hn) := Pn+1 = Pn(1 + ϵ −φ −ν −αIn) + ϵHn   g(Pn, In, Hn) := In+1 = In(1 + ϵ −γ −β) + αInPn  h(Pn, In, Hn) := Hn+1 = Hn(1 −φ) + βIn + νPn. 

<!-- b000333 | prose | pages [18] -->
To determine the ﬁxed points of this model, we solve the system

<!-- b000334 | prose | pages [18] -->
 Pn+1 = Pn   (16) In+1 = In  Hn+1 = Hn, 

<!-- b000335 | prose | pages [18] -->
which gives  Pn(ϵ −φ −ν) −αInPn + ϵHn = 0   (17) In(ϵ −γ −β) + αInPn = 0  Hn(−φ) + βIn + νPn = 0. 

<!-- b000336 | prose | pages [18] -->
The system (17) has eight possible steady state solutions. These are summarised in Table 21. The table lists all possible steady state values for each of the states, and lists any conditions on the parameters that arise in each case.

<!-- b000337 | furniture | pages [19] -->
Team #40764

<!-- b000338 | furniture | pages [19] -->
Page 19 of 25

<!-- b000339 | caption | pages [19] -->
Table 21: Fixed points of the deterministic model

<!-- b000340 | prose | pages [19] -->
Case Steady state Conditions Description Hn = 0 Ebola causes extinction In = 0 1 None in the region examined. Pn = 0 Hn = H Everyone will be immune.

<!-- b000341 | prose | pages [19] -->
2 In = 0 ϵ = 0 This is only the case Pn = 0 if there is no birth.

<!-- b000342 | prose | pages [19] -->
Everyone will be infected.

<!-- b000343 | prose | pages [19] -->
Hn = 0 This is only the case if γ = ϵ 3 In = I there is no recovery and the β = 0 Pn = 0 rates of birth and death of infected people are equal.

<!-- b000344 | prose | pages [19] -->
Hn = 0 Everyone will be vulnerable. ν = 0 4 In = 0 This is the case only if there ϵ = φ Pn = P is no vaccination.

<!-- b000345 | prose | pages [19] -->
No vulnerable person will remain.

<!-- b000346 | prose | pages [19] -->
Pn = 0 ϵ = 0 But since parameters are 5 γ = −β φHn = βIn non-negative we have β = γ = 0. Hence Hn = 0, just like Case 3.

<!-- b000347 | prose | pages [19] -->
No infected person In = 0 will remain, and a constant 6 ϵ = φ φHn = νPn proportion of people will be immune.

<!-- b000348 | prose | pages [19] -->
No immune person β(φ + ν −ϵ) = ν(γ + β −ϵ) Hn = 0 will remain, and a constant In = (ϵ −φ −ν)/α γ + β ≥ϵ 7 proportion of people Pn = (γ + β −ϵ)/α φ + ν ≥ϵ will be infected.

<!-- b000349 | prose | pages [19] -->
φ[−β(γ+β−ϵ)(ϵν+φ(ϵ−γ−ν) Hn = 1 + Each of the states will α(ϵβ−φ(γ+β−ϵ))) ν α(γ + β −ϵ)] share a constant 0 < Hn, In, Pn < ∞ 8 proportion of the In = (γ+β−ϵ)(ϵν+φ(ϵ−φ−ν)) α(ϵβ−φ(γ+β−ϵ)) total population. Pn = (γ + β −ϵ)/α

<!-- b000350 | prose | pages [19] -->
To eradicate the virus, we seek a ﬁxed point solution such that In = 0. In addition, we aim to control the outbreak by varying the parameters α, β, γ, and ν, as with the stochastic model. We do not consider Case 1, as it represents extinction, and does not depend on the parameters. Case 2 is also unrealistic, as it relies there being no births. Case 4 is also not considered, as it does not account for the possibility of vaccination. We therefore seek parameter values that lead to Case 6.

<!-- b000351 | prose | pages [19] -->
To determine these parameters, we consider the stability of the ﬁxed point, and determine parameters that lead to a stable steady-state solution. By the Jury conditions (De Leenheer 2009), a ﬁxed point is stable if |tr(J)| < 1 + det(J) < 2, (18)

<!-- b000352 | prose | pages [19] -->
where J is the Jacobian matrix associated with the diﬀerence equations. The Jacobian matrix for the system (3) is

<!-- b000353 | prose | pages [19, 20] -->
    1 + ϵ −φ −ν −αIn −αPn ∂f/∂Pn ∂f/∂In ∂f/∂Hn ϵ 1 + ϵ −γ −β + αPn J = ∂g/∂Pn ∂g/∂In ∂g/∂Hn = αIn 0 . (19)   1 −φ ∂h/∂Pn ∂h/∂In ∂h/∂Hn ν β The determinant and trace of J are

<!-- b000354 | furniture | pages [20] -->
Team #40764

<!-- b000355 | furniture | pages [20] -->
Page 20 of 25

<!-- b000357 | prose | pages [20] -->
tr(J) = −β −γ −ν + αPn −αIn + 2ϵ −2φ + 3, (20)

<!-- b000358 | prose | pages [20] -->
and

<!-- b000359 | prose | pages [20] -->
det(J) = (1−φ)[(−β−γ+αPn+ϵ+1)(−ν−αIn+ϵ−φ+1)+α2PnIn]+ϵ(βν+γν−ν−ανPn+αβIn−νϵ) (21) respectively. To analyse Case 6, we set In = 0 and ϵ = φ . Simplifying (20) and (21) based on this gives tr(J) = −β −γ −ν + αPn + 3, (22)

<!-- b000360 | prose | pages [20] -->
and det(J) = (β + γ −1 −αPn −φ)(1 −φ −ν). (23)

<!-- b000361 | prose | pages [20] -->
Substituting these into the jury condition (18) gives a condition on the parameters that give a stable solution at the ﬁxed point,

<!-- b000362 | prose | pages [20] -->
−β −γ −ν + αPn + 3 < (β + γ −1 −αPn −φ)(1 −φ −ν) + 1 < 2. (24)

<!-- b000363 | prose | pages [20] -->
As β, γ, ν ≤1, we have tr(J) ≥0. Hence, we can neglect the absolute value signs in (24). As shown in Table 21, there are two equations that specify the three states, In = 0, and φHn = νPn. This gives us one degree of freedom to specify one other parameter to close the system. Crucially, a closed system is only possible if the third equation in the system relates φ and ν. As the death rate of healthy people φ is constant, we must select ν as the independent variable. Rearranging Equation (24) to derive a constraint on ν gives ν > M(1 −φ) −1 = 1 −φ −1 M , (25) M where M = β + γ −1 −αPn −φ. (26)

<!-- b000364 | prose | pages [20] -->
Although the initial analysis of the model requires ϵ = φ, we can replicate the eﬀect of non-constant birth and death rates with a separate assumption on the steady state population,

<!-- b000365 | prose | pages [20] -->
n→∞Pn →∞. lim (27)

<!-- b000366 | prose | pages [20] -->
Equation (27) assumes that the population will eventually approach inﬁnity, as will occur if birth rate is greater than death rate. As the steady state number of infections is zero in this case, there are no deaths due to Ebola, so the assumption is valid if the birth and death rates are assumed constant. We therefore have 1 1 lim M = lim M = 0. (28) n→∞ Pn→∞ We therefore conclude that the condition that must be satisﬁed to produce a stable solution at the ﬁxed point of Case 6 is ν > 1 −φ. (29)

<!-- b000367 | prose | pages [20] -->
As this condition does not contain α, β, or γ, we reach the important conclusion that vaccination is the only way to ensure that Ebola is eradicated in the long-term. This assertion suggests that a vaccine must be developed for us to be sure that the Ebola outbreak in West Africa can be controlled.

<!-- b000368 | furniture | pages [21] -->
Team #40764

<!-- b000369 | furniture | pages [21] -->
Page 21 of 25

<!-- b000370 | heading | pages [21] -->
5 Summary of Mathematical Modelling

<!-- b000371 | heading | pages [21] -->
5.1 Strengths and Weaknesses

<!-- b000372 | prose | pages [21] -->
Strengths and weaknesses of our approach that become apparent during the solution process are summarised below:

<!-- b000373 | heading | pages [21] -->
Strengths

<!-- b000374 | prose | pages [21] -->
Our model...

<!-- b000375 | prose | pages [21] -->
• is based on realistic mechanism of disease transfer

<!-- b000376 | prose | pages [21] -->
• uses parameters that are based on empirical evidence

<!-- b000377 | prose | pages [21] -->
• enables predictions of the evolution of the disease over any length of time

<!-- b000378 | prose | pages [21] -->
• enables full accounting for the number of each transition and number of people in each state at any time

<!-- b000379 | prose | pages [21] -->
• accurately predicts known trends in the outbreak in diﬀerent regions, and accurate predictions are achieved with physically realistic values for the parameters

<!-- b000380 | prose | pages [21] -->
• allows independent analysis of three diﬀerent treatment options

<!-- b000381 | prose | pages [21] -->
• enables an analytical solution for the relationships between parameters required to drive Ebola infections to zero

<!-- b000382 | prose | pages [21] -->
• accounts for population growth which is important in long-term forecasts

<!-- b000383 | prose | pages [21] -->
• simulates randomness in the disease spread (which can lead to divergent outcomes)

<!-- b000384 | heading | pages [21] -->
Weaknesses

<!-- b000385 | prose | pages [21] -->
Our model...

<!-- b000386 | prose | pages [21] -->
• relies on parameter estimates that are justiﬁed using anecdotal evidence (in particular K)

<!-- b000387 | prose | pages [21] -->
• is validated against a short period relative to the entire Ebola outbreak

<!-- b000388 | prose | pages [21] -->
• requires good estimates for initial conditions that are not necessarily available from the data

<!-- b000389 | prose | pages [21] -->
• relies heavily on the accuracy of WHO data, which may be underestimated

<!-- b000390 | heading | pages [21] -->
5.2 Future Work

<!-- b000391 | prose | pages [21] -->
The modelling framework used in this analysis provides scope for future enhancement. The following tasks would reduce the assumptions made in this paper, to produce a better model of actual disease transmission:

<!-- b000392 | prose | pages [21] -->
• Obtaining necessary data to model smaller regions than entire nations

<!-- b000393 | prose | pages [21] -->
• Allowing the state transition rate parameters to be expressed as functions of time, instead of constant values. This will allow better modelling of how disease treatment changes with time

<!-- b000394 | prose | pages [21] -->
• Applying a cost function to diﬀerent treatment options, then use the sensitivity analysis to determine the most eﬃcient allocation of resources to reduce deaths

<!-- b000395 | prose | pages [21] -->
• Increasing the scope of sensitivity analysis to cover all possible parameter changes

<!-- b000396 | prose | pages [21, 22] -->
• Adding additional states to model the disease life cycle, for example incubation, infectious, recovering, and allowing transmission from deceased people. A disadvantage of adding states is that ﬁxed point analysis becomes more diﬃcult. Adding one extra state doubles the number of ﬁxed points • Increasing the complexity of the model by adding state transitions. For example, a transition from immune to vulnerable can be added to simulate virus mutation, and relaxing the assumption that infection guarantees future immunity. The state transition diagram would look like Figure 7.

<!-- b000397 | furniture | pages [22] -->
Team #40764

<!-- b000398 | furniture | pages [22] -->
Page 22 of 25

<!-- b000400 | prose | pages [22] -->
A disadvantage of this is that the rate parameters for the new transitions are diﬃcult to determine

<!-- b000401 | prose | pages [22] -->
Birth 1 2 ε ε 7 Healthy α (Vulnerable) 3 λ 10 8 υ μ Infected 9 6 Healthy β 5 φ (Immune) γ 4 φ

<!-- b000402 | prose | pages [22] -->
Death

<!-- b000403 | caption | pages [22] -->
Figure 7: A possible extension to the general model

<!-- b000404 | heading | pages [22] -->
5.3 Conclusion

<!-- b000405 | prose | pages [22] -->
Stochastic and deterministic models of the West African Ebola outbreak are presented. Both models are based on dividing the population into infected people, immune healthy people, and vulnerable healthy people, and assigning parameters to the rate of transition between these states. The numerical value of parameters are validated against WHO data for four regions from 12 November 2014 to 5 February 2015. We then extend the investigation to produce predictions of future spread of the virus under diﬀerent treatment conditions. Short and medium-term numerical predictions are performed using the stochastic model, and an analytical general solution for long-term steady state conditions is performed using the deterministic model. The ﬁndings of these investigations inform recommendations of future treatment strategies. Qualitatively, the key ﬁndings are

<!-- b000406 | prose | pages [22] -->
• The most eﬀective short-term strategy in all countries is producing a large quantity of improved medicine

<!-- b000407 | prose | pages [22] -->
• The most eﬃcient strategy for reducing medium-term deaths is to improve medical services to isolate infected patients

<!-- b000408 | prose | pages [22] -->
• Short-term strategies will be most eﬀective in Sierra Leone and Liberia

<!-- b000409 | prose | pages [22] -->
• Medium-term strategies should target all three countries in the outbreak: Guinea, Sierra Leone, and Liberia

<!-- b000410 | prose | pages [22] -->
• Although vaccination is less eﬀective in the short and medium-term than other treatment methods in all countries, developing a vaccine is the only way to ensure that the virus can be eliminated in the long-term

<!-- b000411 | furniture | pages [23] -->
Team #40764

<!-- b000412 | furniture | pages [23] -->
Page 23 of 25

<!-- b000413 | heading | pages [23] -->
References

<!-- b000414 | references | pages [23] -->
BBC 2015, Ebola: Mapping the outbreak, http://www.bbc.com/news/world-africa-28755033.

<!-- b000415 | references | pages [23] -->
Centers for Disease Control and Prevention 2014, Q&As on Transmission of Ebola Virus Disease,

<!-- b000416 | references | pages [23] -->
http://www.cdc.gov/vhf/ebola/transmission/qas.html.

<!-- b000417 | references | pages [23] -->
CountryMeters 2015, Current world population by country. Population data for every contry as of 2015,

<!-- b000418 | references | pages [23] -->
http://countrymeters.info/.

<!-- b000419 | references | pages [23] -->
De Leenheer, P 2009, Notes on the Jury conditions, http://math.oregonstate.edu/~deleenhp/

<!-- b000420 | references | pages [23] -->
teaching/spring09/MAP4484/notes-jury.pdf.

<!-- b000421 | references | pages [23] -->
Grant, K 2014, Survivors of Ebola outbreak in Nigeria share their stories, http://www.theglobeandmail.

<!-- b000422 | references | pages [23] -->
com/news/national/survivors- of- ebola- outbreak- in- nigeria- share- their- stories/

<!-- b000423 | references | pages [23] -->
article21985268/.

<!-- b000424 | references | pages [23] -->
Meltzer, MI, Atkins, CY, Santibanez, S, Knust, B, Petersen, BW, Ervin, ED, Nichol, ST, Damon, IK,

<!-- b000425 | references | pages [23] -->
and Washington, ML 2015, “Estimating the Future Number of Cases in the Ebola Epidemic – Liberia

<!-- b000426 | references | pages [23] -->
and Sierra Leone, 2014-2015”, MMWR Supplements, vol. 63, pp. 1–13.

<!-- b000427 | references | pages [23] -->
World Health Organisation 2014a, Ebola virus disease, http : / / www . who . int / mediacentre /

<!-- b000428 | references | pages [23] -->
factsheets/fs103/en/.

<!-- b000429 | references | pages [23] -->
World Health Organisation 2014b, Why the Ebola outbreak has been underestimated, http://www.who.

<!-- b000430 | references | pages [23] -->
int/mediacentre/news/ebola/22-august-2014/en/.

<!-- b000431 | references | pages [23] -->
World Health Organisation 2015a, Ebola data and statistics, http://apps.who.int/gho/data/view.

<!-- b000432 | references | pages [23] -->
ebola-sitrep.ebola-summary-latest?lang=en.

<!-- b000433 | references | pages [23] -->
World Health Organisation 2015b, Ebola vaccines, therapies, and diagnostics, http://www.who.int/

<!-- b000434 | references | pages [23] -->
medicines/emp_ebola_q_as/en/.

<!-- b000435 | references | pages [23] -->
Note: All sources accessed between February 5 and February 9 2015

<!-- b000436 | furniture | pages [24] -->
Team #40764

<!-- b000437 | furniture | pages [24] -->
Page 24 of 25

<!-- b000438 | references | pages [24] -->
World Medical Association Letter

<!-- b000439 | references | pages [24] -->
Dear World Medical Association,

<!-- b000440 | references | pages [24] -->
We were interested to hear your recent announcement about the development of new medication to stop

<!-- b000441 | references | pages [24] -->
Ebola and cure infected patients. This is a welcome and important development in the humanitarian

<!-- b000442 | references | pages [24] -->
ﬁght against the outbreak in West Africa. To assist the distribution of the new medicine, and planning

<!-- b000443 | references | pages [24] -->
future prevention measures, we performed investigations using mathematical modelling. We use two

<!-- b000444 | references | pages [24] -->
methods to simulate the spread of Ebola in Guinea, Liberia, and Sierra Leone. We use these models to

<!-- b000445 | references | pages [24] -->
determine the most suitable country to target in short-term and long-term distribution of the medicine.

<!-- b000446 | references | pages [24] -->
In addition, we analyse diﬀerent treatment options in both short-term and long-term, to determine the

<!-- b000447 | references | pages [24] -->
optimal way for the WMA to direct its future endeavours. We present our ﬁndings in this letter.

<!-- b000448 | references | pages [24] -->
The mathematical model that we have developed is based on data from the World Health Organisation

<!-- b000449 | references | pages [24] -->
(WHO). In our analysis, we simulate the spread of the outbreak from 12 November 2014 to 5 February

<!-- b000450 | references | pages [24] -->
2015 using two methods. We ﬁnd that both methods accurately predict the outbreak when considering

<!-- b000451 | references | pages [24] -->
four regions: Guinea, Liberia, Sierra Leone, and the West African region as a whole. This gives us

<!-- b000452 | references | pages [24] -->
conﬁdence that our model accurate.

<!-- b000453 | references | pages [24] -->
We then run the model forward to produce predictions of the disease spread from February 5 2015

<!-- b000454 | references | pages [24] -->
onwards. A key ﬁnding of the simulation is that the overall current level of treatment is insuﬃcient to

<!-- b000455 | references | pages [24] -->
control the virus in the long-term. If new measures are not implemented, the number of infections will

<!-- b000456 | references | pages [24] -->
increase out of control in approximately eight years time. This ﬁnding is why we are excited to learn

<!-- b000457 | references | pages [24] -->
of a newly developed medicine. We then amend the model to take into account the development of

<!-- b000458 | references | pages [24] -->
new medicine, as well as two alternative methods to mitigate the virus: improving health services, and

<!-- b000459 | references | pages [24] -->
developing and distributing a vaccine.

<!-- b000460 | references | pages [24] -->
Based on the amendments to the original model, we develop short-term (six months), medium-

<!-- b000461 | references | pages [24] -->
term (two years), and long-term recommendations for mitigating the virus. To develop short-term

<!-- b000462 | references | pages [24] -->
recommendations, we simulate the eﬀect of diﬀerent treatment options in each country, and compare

<!-- b000463 | references | pages [24] -->
the results with what would occur if treatment is not improved. After performing the short-term

<!-- b000464 | references | pages [24] -->
simulations, we produce the following recommendations for the quantity and distribution of the new

<!-- b000465 | references | pages [24] -->
medicine:

<!-- b000466 | references | pages [24] -->
• The largest single strategy short-term reduction in deaths is achieved by distributing a large

<!-- b000467 | references | pages [24] -->
quantity of medicine in Liberia, although all nations would substantially beneﬁt from the medicine

<!-- b000468 | references | pages [24] -->
• For a short-term strategy, medicine should be introduced in the highest quantity possible. The

<!-- b000469 | references | pages [24] -->
eﬃciency (deaths per increase in quantity of medicine) of using medicine is greatest when high

<!-- b000470 | references | pages [24] -->
quantities are distributed. This ﬁnding is consistent across all nations, but is especially important

<!-- b000471 | references | pages [24] -->
in Sierra Leone and Liberia

<!-- b000472 | references | pages [24] -->
• For a medium-term strategy, medicine’s eﬃciency does not change signiﬁcantly with the quantity

<!-- b000473 | references | pages [24] -->
distributed. High quantities still result in larger reductions in deaths, but should be subject to

<!-- b000474 | references | pages [24] -->
cost-beneﬁt analysis

<!-- b000475 | references | pages [24] -->
• To maximise death reduction in the medium-term, Liberia is the most important nation to target.

<!-- b000476 | references | pages [24] -->
However, it is also important to distribute high quantities of medicine in Guinea, despite its low

<!-- b000477 | references | pages [24] -->
relative incidence of Ebola

<!-- b000478 | references | pages [24] -->
We also provide the following recommendations regarding treatment methods other than medicine:

<!-- b000479 | references | pages [24] -->
• In the short-term, both improving medical services and vaccinations are less eﬀective in reduce

<!-- b000480 | references | pages [24] -->
deaths from Ebola

<!-- b000481 | references | pages [24] -->
• However, in the medium-term, improving medical services is more eﬃcient than distributing

<!-- b000482 | references | pages [24] -->
medicine, and vaccinations are more competitive

<!-- b000483 | references | pages [24] -->
• In the short to medium-term, Guinea will beneﬁt most from vaccinations.

<!-- b000484 | furniture | pages [25] -->
Team #40764

<!-- b000485 | furniture | pages [25] -->
Page 25 of 25

<!-- b000486 | references | pages [25] -->
• In the short-term, Sierra Leone will beneﬁt most from an improvement in medical services

<!-- b000487 | references | pages [25] -->
• In the long term, the only way to ensure that the Ebola virus is completely eradi-

<!-- b000488 | references | pages [25] -->
cated is by developing and distributing vaccines

<!-- b000489 | references | pages [25] -->
Despite these speciﬁc recommendations, all regions will beneﬁt from any of the treatment methods

<!-- b000490 | references | pages [25] -->
described. Our analysis also neglects the monetary cost of each treatment option. Should further

<!-- b000491 | references | pages [25] -->
information about these recommendations be desired, we can consult with relevant authorities to deter-

<!-- b000492 | references | pages [25] -->
mine the most cost-eﬀective treatment options. Nevertheless, we believe that these recommendations

<!-- b000493 | references | pages [25] -->
represent the most eﬃcient way to implement medicine and other strategies to reduce the overall

<!-- b000494 | references | pages [25] -->
number of deaths from Ebola. We hope that they will prove useful in the ongoing quest to reduce the

<!-- b000495 | references | pages [25] -->
eﬀects of Ebola.

<!-- b000496 | references | pages [25] -->
Yours sincerely,

<!-- b000497 | furniture | pages [25] -->
Team #40764
