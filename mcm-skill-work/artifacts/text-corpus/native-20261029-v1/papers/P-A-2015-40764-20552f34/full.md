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

<!-- b000017 | prose | pages [2] -->
1

<!-- b000018 | heading | pages [2] -->
Introduction

<!-- b000019 | prose | pages [2] -->
We present two models to predict the current Ebola outbreak in West Africa. The general approach in

<!-- b000020 | prose | pages [2] -->
both models is to divide the population into three states, infected people, vulnerable healthy people, and immune healthy people, and consider the transitions between these states. Based on this approach, we develop stochastic and deterministic mathematical models to predict the spread of the virus. These models are also used to assess the impact of potential treatment methods.

<!-- b000021 | prose | pages [2] -->
The models are validated using data on the number of Ebola cases and deaths provided by the World Health Organisation. Both models show good agreement for the outbreak in four regions, to prove the robustness of the approach. The models are then extended to predict the future evolution of the data, if current treatment practices are preserved into the future. This provides a basis against which the eﬀects of diﬀerent treatment options are assessed independently.

<!-- b000022 | prose | pages [2] -->
The stochastic model is used to predict the short-term and medium-term eﬀects of three diﬀerent Ebola treatment options. These options are an improvement in medical services, improvement in available medicines, and developing a vaccine. We compare the eﬃciency of each method in three countries by comparing the reduction of total deaths predicted in the model with the percentage change required from current treatment levels. We ﬁnd that a large quantity of improved medicine is the most eﬀective short-term solution, but medical services become more eﬃcient in the medium term. In addition, we ﬁnd that treatment in the short-term should be targeted to Sierra Leone and Liberia, but in the medium-term, it is equally important to treat Guinea. Following this analysis, we generalise to ﬁnd the long-term impacts of diﬀerent treatment using the deterministic model. We ﬁnd that, although vaccines are less eﬃcient in the short and medium-term, the only way to ensure complete eradication of Ebola in the long term is to develop a vaccine. These ﬁndings inform recommendations to the World Medical Association to optimise the treatment of Ebola.

<!-- b000023 | prose | pages [2] -->
1.1 Problem Approach

<!-- b000024 | prose | pages [2] -->
To address the problem of eradicating Ebola, we initially present a general model that provides accurate predictions of the evolution of the outbreak in West Africa based on current treatment practices. To do this, we produce a general method, and ﬁnd parameters that match data provided by the World Health Organisation (2015a). Given an accurate model of the disease, we use it to isolate and predict the future impact of three diﬀerent types of additional treatment:

<!-- b000025 | prose | pages [2] -->
• Improving medical services, for example improved quarantine, and increased numbers of doctors and hospitals

<!-- b000026 | prose | pages [2] -->
• Improving medicine, for example that developed by the World Medical Association

<!-- b000027 | prose | pages [2] -->
• Developing and distributing a vaccine

<!-- b000028 | prose | pages [2] -->
We perform this analysis in each of the three countries in the primary Ebola outbreak: Guinea, Liberia,

<!-- b000029 | prose | pages [2] -->
and Sierra Leone. Although the general model permits greater subdivision, the lack of data for smaller regions conﬁnes the investigation to three regions. The analysis provides insight into which treatment methods are most eﬀective, and which country would most beneﬁt from them. Based on our results, we provide recommendations to the World Medical Association in letter form.

<!-- b000030 | prose | pages [2] -->
A general model for the spread of Ebola is created by classifying each member of the population into one of three states. These states are

<!-- b000031 | prose | pages [2] -->
• People who are infected with Ebola

<!-- b000032 | prose | pages [2] -->
• Healthy people who are vulnerable to infection

<!-- b000033 | prose | pages [2] -->
• Healthy people who are immune to infection

<!-- b000034 | furniture | pages [3] -->
Team #40764

<!-- b000035 | furniture | pages [3] -->
Page 3 of 25

<!-- b000036 | prose | pages [3] -->
As the disease spreads, people in the aﬀected areas undergo transitions between these three states. The generalised model is an open system, whereby total population can increase via births, and decrease via deaths. All possible state transitions are illustrated in Figure 1.

<!-- b000037 | prose | pages [3] -->
Birth

<!-- b000038 | prose | pages [3] -->
2

<!-- b000039 | prose | pages [3] -->
ε

<!-- b000040 | prose | pages [3] -->
α

<!-- b000041 | prose | pages [3] -->
Infected

<!-- b000042 | prose | pages [3] -->
6

<!-- b000043 | prose | pages [3] -->
β

<!-- b000044 | prose | pages [3] -->
5

<!-- b000045 | prose | pages [3] -->
γ

<!-- b000046 | prose | pages [3] -->
1

<!-- b000047 | prose | pages [3] -->
ε

<!-- b000048 | prose | pages [3] -->
Healthy

<!-- b000049 | prose | pages [3] -->
7

<!-- b000050 | prose | pages [3] -->
(Vulnerable)

<!-- b000051 | prose | pages [3] -->
3 8

<!-- b000052 | prose | pages [3] -->
υ

<!-- b000053 | prose | pages [3] -->
Healthy

<!-- b000054 | prose | pages [3] -->
φ

<!-- b000055 | prose | pages [3] -->
(Immune)

<!-- b000056 | prose | pages [3] -->
4

<!-- b000057 | prose | pages [3] -->
φ

<!-- b000058 | prose | pages [3] -->
Death

<!-- b000059 | caption | pages [3] -->
Figure 1: Possible transitions between population states in an Ebola outbreak

<!-- b000060 | prose | pages [3] -->
As Figure 1 shows, each of the eight state transition is assigned a number and a rate parameter. The rate parameters are deﬁned as the rate at which one person of the relevant state undergoes the state transition on a given day. They form the basis of the model, and are altered to model diﬀerent conditions. A list of these parameters is provided in Table 1.

<!-- b000061 | caption | pages [3] -->
Table 1: State transition rate parameters used in the general Ebola model

<!-- b000062 | prose | pages [3] -->
Parameter Description The daily rate at which a healthy person is infected with Ebola α The daily recovery rate for a person with Ebola β The daily vaccination rate per person ν The daily death rate per person for people infected with Ebola γ The daily death rate per person, for the healthy population φ The daily birth rate per person, assumed equal for both infected and healthy people ϵ

<!-- b000063 | prose | pages [3] -->
We deﬁne these parameters to represent the full set of possible transitions. The formulation is therefore

<!-- b000064 | prose | pages [3] -->
suﬃcient to simulate the changes occurring in an Ebola outbreak. However, this interpretation relies on several assumptions, which are listed in Section 1.1.1.

<!-- b000065 | prose | pages [3] -->
1.1.1

<!-- b000066 | heading | pages [3] -->
Assumptions

<!-- b000067 | prose | pages [3] -->
• The Ebola outbreak is conﬁned to Guinea, Liberia, and Sierra Leone. When developing the model, simulations of the spread of Ebola are performed for individual countries, and the spread of the virus as a whole. As the total number of cases and deaths from Ebola in other countries is small (eight deaths in Nigeria, as opposed to 1957 in Guinea (BBC 2015)), we assume that the entire outbreak occurs in Guinea, Liberia, and Sierra Leone

<!-- b000068 | furniture | pages [4] -->
Team #40764

<!-- b000069 | furniture | pages [4] -->
Page 4 of 25

<!-- b000070 | prose | pages [4] -->
• Population change depends on births and deaths only. We assume that net migration in each of the three countries is zero, as it is likely to be small relative to the overall population

<!-- b000071 | prose | pages [4] -->
• The birth and death rates are constant. As the state transition parameters are constant, we must assume that the birth and death rate is constant. As the model’s calculations occur over a relatively short time, this is reasonable

<!-- b000072 | prose | pages [4] -->
• States are binary, and transition between states is instantaneous. We assume that each member of the population belongs to exactly one state at all times. This is reasonable for viral diseases such as Ebola. In addition, the severity of all cases is considered the same, which is reasonable when average data is used

<!-- b000073 | prose | pages [4] -->
• All people within a population are homogeneous. We assume that the spatial, gender, or age distributions do not aﬀect the rate parameters. This enables the rate parameters to be held constant in the model

<!-- b000074 | prose | pages [4] -->
• The virus does not mutate. There is no transition from immunity to vulnerability, as the model considers the spread of the current strain of the Ebola virus

<!-- b000075 | prose | pages [4] -->
• Recovery from Ebola is complete and independent. We assume that people who have recovered from Ebola have the same likelihood of death as other healthy people, and that a person’s recovery from Ebola does not depend on anyone else. Although healthy doctors provide vital assistance, the overall eﬀect of all healthy people on a patient’s recovery is negligible. In addition, we assume that antibodies generated in the recovery provide immunity from future infection. This is supported by Centers for Disease Control and Prevention (2014), which states that antibodies provide immunity from the same Ebola strain for at least ten years

<!-- b000076 | prose | pages [4] -->
• Infection with Ebola does not aﬀect birth rate. As the cycle of a person’s infection with Ebola is likely to last for much less than nine months, we assume that the birth rate for people with Ebola is the same as the rest of the population

<!-- b000077 | prose | pages [4] -->
• The possibility of death or recovery is independent of the Ebola infection cycle. In order to model state transitions by constant rates, we assume that the likelihood of death or recovery is the same regardless of how long a patient has been infected. The infected state is an average stage that represents all stages of the disease, for example incubation, infectious, recovering, etc.

<!-- b000078 | prose | pages [4] -->
• The virus is transferred between living people. Although Ebola is commonly contracted via contact with deceased (World Health Organisation 2014a), our model assumes that these people transfer the disease while living. This does not aﬀect overall rate of transmission. In addition, transmission between non-human species is neglected

<!-- b000079 | prose | pages [4] -->
• Treatment practices in place between 12 November 2014 and 5 February 2015 are constant. The models are developed based on data available from the World Health Organisation (WHO) between 12 November 2014 and 5 February 2015. The rate parameters therefore reﬂect

<!-- b000080 | prose | pages [4] -->
the treatment practices available between these dates. Holding the rate parameters constant allows us to isolate variables when modelling new medicines and vaccines.

<!-- b000081 | prose | pages [4] -->
• Immunity is not passed on to the next generation. We assume that a survivor of Ebola cannot give birth to immune oﬀspring. We also assume that healthy parents give birth to healthy oﬀspring, and infected parents give birth to infected oﬀspring

<!-- b000082 | prose | pages [4] -->
2

<!-- b000083 | heading | pages [4] -->
Mathematical Models

<!-- b000084 | prose | pages [4] -->
The problem interpretation described in Section 1.1 is solved using two mathematical models, a stochastic model and a deterministic model. The stochastic model provides a random simulation of the evolution of the disease, and simulates continuously in time. The deterministic model provides an

<!-- b000085 | furniture | pages [5] -->
Team #40764

<!-- b000086 | furniture | pages [5] -->
Page 5 of 25

<!-- b000087 | prose | pages [5] -->
analytical steady state solution, allowing analysis of ﬁxed points and stability. Both models provide a means to model the evolution of the disease based on existing data, and predict future trends.

<!-- b000088 | prose | pages [5] -->
2.1

<!-- b000089 | heading | pages [5] -->
Stochastic Model

<!-- b000090 | prose | pages [5] -->
In the stochastic model, the probability of each transition occurring in a given timestep is calculated using the rate parameters, and then the evolution of the disease is simulated randomly. Deﬁnitions of parameters required for the stochastic model are given in Table 2.

<!-- b000091 | caption | pages [5] -->
Table 2: Parameters used in the stochastic model

<!-- b000092 | prose | pages [5] -->
Parameter Description n The timestep number The timestep size, given as a fraction of one day dt The number of healthy, vulnerable people after n timesteps Pn The number of infected people after n timesteps In The number of healthy, immune people after n timesteps Hn

<!-- b000093 | prose | pages [5] -->
The rate parameters in Table 1 provide a means of determining the probability that one event will occur in a given timestep. The timestep size, dt, is prescribed to ensure that a maximum of one transition of any type can occur in each timestep. In accordance with the eight transitions shown in Figure 1, the following shows the potential results of the subsequent timestep n + 1, and the probability that each event occurs.

<!-- b000094 | prose | pages [5] -->


<!-- b000095 | prose | pages [5] -->
(In, Hn, Pn + 1)

<!-- b000096 | prose | pages [5] -->
  

<!-- b000097 | prose | pages [5] -->
w.p.

<!-- b000098 | prose | pages [5] -->
p1 = ϵ(Pn + Hn)dt (In + 1, Hn, Pn)

<!-- b000099 | prose | pages [5] -->
    

<!-- b000100 | prose | pages [5] -->
w.p.

<!-- b000101 | prose | pages [5] -->
p2 = ϵIndt (In, Hn, Pn −1)

<!-- b000102 | prose | pages [5] -->
    

<!-- b000103 | prose | pages [5] -->
w.p.

<!-- b000104 | prose | pages [5] -->
p3 = φPndt (In, Hn −1, Pn)

<!-- b000105 | prose | pages [5] -->
   

<!-- b000106 | prose | pages [5] -->
(In+1, Hn+1, Pn+1) =

<!-- b000107 | prose | pages [5] -->
w.p.

<!-- b000108 | prose | pages [5] -->
p4 = φHndt

<!-- b000109 | prose | pages [5] -->
(1)

<!-- b000110 | prose | pages [5] -->
(In −1, Hn, Pn)

<!-- b000111 | prose | pages [5] -->


<!-- b000112 | prose | pages [5] -->
w.p.

<!-- b000113 | prose | pages [5] -->
p5 = γIndt (In −1, Hn + 1, Pn)

<!-- b000114 | prose | pages [5] -->
    

<!-- b000115 | prose | pages [5] -->
w.p.

<!-- b000116 | prose | pages [5] -->
p6 = βIndt (In + 1, Hn, Pn −1)

<!-- b000117 | prose | pages [5] -->
    

<!-- b000118 | prose | pages [5] -->
w.p.

<!-- b000119 | prose | pages [5] -->
p7 = αInPndt (In, Hn + 1, Pn −1)

<!-- b000120 | prose | pages [5] -->
    

<!-- b000121 | prose | pages [5] -->
(In, Hn, Pn)

<!-- b000122 | prose | pages [5] -->


<!-- b000123 | prose | pages [5] -->
w.p.

<!-- b000124 | prose | pages [5] -->
p8 = νPndt 1 −P8 w.p.

<!-- b000125 | prose | pages [5] -->
i=1 pi

<!-- b000126 | prose | pages [5] -->
For example, transition one is the birth of one healthy, but not immune person. The rate parameter ϵ provides the birth rate per person per day. In addition, we assume that all healthy people give birth to vulnerable healthy oﬀspring. Therefore, the probability of a healthy birth occurring in a given timestep is given by multiplying ϵ by the total number of healthy people, (Hn + Pn), and the fraction of one day for each timestep, dt. The result of this event is that the next timestep, n + 1, has one additional healthy person, i.e. Pn+1 = Pn + 1. The probabilities and outcomes of all other events are similarly determined (we note that the probability of transmission p7 depends on both the number of infected people and the number of vulnerable people). For the stochastic model to be valid, the timestep must be small enough such that

<!-- b000127 | prose | pages [5] -->
8 X

<!-- b000128 | prose | pages [5] -->
i=1

<!-- b000129 | prose | pages [5] -->
pi ≤1, (2)

<!-- b000130 | prose | pages [5] -->
which ensures that a maximum of one event can occur each timestep.

<!-- b000131 | prose | pages [5] -->
Code to simulate this system is produced in Matlab. To generate the event for each timestep, a pseudo-random number r ∈[0, 1] is generated. An event is selected if r lies within the cumulative probability range up to that event. To keep track of the total number of cases and deaths due to Ebola, a counter that increments whenever a relevant event occurs is used. The simulation process is repeated

<!-- b000132 | furniture | pages [6] -->
Team #40764

<!-- b000133 | furniture | pages [6] -->
Page 6 of 25

<!-- b000134 | prose | pages [6] -->
for the desired number of timesteps to completely simulate an Ebola outbreak for a given initial state (I0, H0, P0).

<!-- b000135 | prose | pages [6] -->
2.2

<!-- b000136 | heading | pages [6] -->
Deterministic Model

<!-- b000137 | prose | pages [6] -->
To implement the deterministic mode, we deﬁne Pn, In , and Hn in the same way as for the stochastic model, where the timestep number n represents a number of days. We then deﬁne functions f, g, and h containing diﬀerence equations for subsequent states. They are constructed using the same state transition rate parameters as the stochastic model. The diﬀerence equations are

<!-- b000138 | prose | pages [6] -->


<!-- b000139 | prose | pages [6] -->
f(Pn, In, Hn) := Pn+1 = Pn(1 + ϵ −φ −ν −αIn) + ϵHn

<!-- b000140 | prose | pages [6] -->
 

<!-- b000141 | prose | pages [6] -->
(3)

<!-- b000142 | prose | pages [6] -->
g(Pn, In, Hn) := In+1 = In(1 + ϵ −γ −β) + αInPn

<!-- b000143 | prose | pages [6] -->


<!-- b000144 | prose | pages [6] -->
h(Pn, In, Hn) := Hn+1 = Hn(1 −φ) + βIn + νPn.

<!-- b000145 | prose | pages [6] -->


<!-- b000146 | prose | pages [6] -->
Unlike the stochastic model, the deterministic model only keeps track of the day-to-day number of people in each state. However, the system is easy to implement in Matlab, as randomness is not considered. Implementing the diﬀerence equations (3) in Matlab and iterating over n timesteps enables complete deterministic simulation of the Ebola outbreak for given initial conditions (I0, H0, P0).

<!-- b000147 | prose | pages [6] -->
2.3

<!-- b000148 | heading | pages [6] -->
Comparison of Models

<!-- b000149 | caption | pages [6] -->
Table 3 compares the relative strengths of the stochastic and deterministic models.

<!-- b000150 | caption | pages [6] -->
Table 3: Unique advantages of the stochastic and deterministic models

<!-- b000151 | prose | pages [6] -->
Stochastic Randomness State populations take integer values Timestep is eﬀectively continuous Deterministic Repeated simulation not required Analytical steady state solutions Less computational time Separate accounting of all state transitions

<!-- b000152 | prose | pages [6] -->
In our analysis, we take advantage of the unique features of the stochastic and deterministic models. The stochastic model provides a means to generate plots diﬀerent state transitions against time. This is used to compare with WHO data on the total number of Ebola cases and deaths. In addition, simulations using the stochastic model are used to perform sensitivity analysis on the parameters. This allows us to isolate the eﬀect of diﬀerent treatment practices. The deterministic model provides an analytical method to accurately analyse diﬀerent types of steady state solution, and determines the relationship between rate parameters required to drive Ebola infections to zero.

<!-- b000153 | heading | pages [6] -->
Results - Predicting the Spread of Ebola

<!-- b000154 | prose | pages [6] -->
3

<!-- b000155 | prose | pages [6] -->
We present stochastic and deterministic solutions for the spread of Ebola. The models are veriﬁed using

<!-- b000156 | prose | pages [6] -->
data for the number of deaths and total cases in the 85 days from 12 November 2014 to 5 February 2015, which is available from the World Health Organisation (2015a). The development of an accurate model then enables us to make modiﬁcations based on diﬀerent treatment options.

<!-- b000157 | furniture | pages [7] -->
Team #40764

<!-- b000158 | prose | pages [7] -->
3.1

<!-- b000159 | heading | pages [7] -->
Model Parameters

<!-- b000160 | furniture | pages [7] -->
Page 7 of 25

<!-- b000161 | prose | pages [7] -->
To simulate the outbreak, we require numerical values for

<!-- b000162 | prose | pages [7] -->
• State transition rate parameters: α, β, ν, γ, φ, ϵ

<!-- b000163 | prose | pages [7] -->
• Initial conditions: I0, H0, P0

<!-- b000164 | prose | pages [7] -->
Where possible, we use realistic data to provide suitable estimates for these parameters. We predict

<!-- b000165 | prose | pages [7] -->
the value of the parameters in all three countries independently, then combine them to produce a population-weighted average to model the outbreak as a whole. This method of prescribing the parameters provides a real-world basis for all state transitions in the model.

<!-- b000166 | prose | pages [7] -->
3.1.1 ν

<!-- b000167 | prose | pages [7] -->
As there is no current vaccine for Ebola (World Health Organisation 2015b) as of January 21 2015, we assume ν = 0 in the predictive model.

<!-- b000168 | prose | pages [7] -->
3.1.2 ϵ, φ

<!-- b000169 | prose | pages [7] -->
CountryMeters (2015) provides live population estimates, as well as data on the birth and death rates of each country. Table 4 gives this data for the three relevant countries on 5 February 2015.

<!-- b000170 | caption | pages [7] -->
Table 4: Live population statistics for February 5 2015 (CountryMeters 2015)

<!-- b000171 | prose | pages [7] -->
Birth Rate [ppl d−1] Country Population Guinea 12,414,680 Liberia 4,615,917 Sierra Leone 6,404,599 Overall 23,436,196 Death Rate [ppl d−1] 1,150 326 425 121 626 191 2,201 638

<!-- b000172 | prose | pages [7] -->
The birth and death rate parameters, ϵ and φ respectively, are determined by

<!-- b000173 | prose | pages [7] -->
ϵ = Birth Rate

<!-- b000174 | prose | pages [7] -->
Population,

<!-- b000175 | prose | pages [7] -->
and

<!-- b000176 | prose | pages [7] -->
(4)

<!-- b000177 | prose | pages [7] -->
φ = Death Rate

<!-- b000178 | prose | pages [7] -->
Population .

<!-- b000179 | prose | pages [7] -->
(5)

<!-- b000180 | prose | pages [7] -->
These give the rate at which one healthy person will give birth or die respectively. The initial population at 12 November 2014 is estimated by subtracting the net births over the 85 preceding days from the population given in Table 4,

<!-- b000181 | prose | pages [7] -->
Initial Population = Final Population −85(Birth Rate −Death Rate).

<!-- b000182 | prose | pages [7] -->
(6)

<!-- b000183 | prose | pages [7] -->
Performing these operations gives the results in Table 5.

<!-- b000184 | caption | pages [7] -->
Table 5: Population parameters for use in the model

<!-- b000185 | prose | pages [7] -->
Country ϵ Guinea 9.3175e-5 Liberia 9.2567e-5 Sierra Leone 9.8295e-5 Overall 9.4455e-5 φ Initial Population 2.6386e-5 12,343,779 2.6392e-5 4,589,796 2.9981e-5 6,367,191 2.7369e-5 23,300,766

<!-- b000186 | furniture | pages [8] -->
Team #40764

<!-- b000187 | prose | pages [8] -->
3.1.3 I0, H0, P0

<!-- b000188 | furniture | pages [8] -->
Page 8 of 25

<!-- b000189 | prose | pages [8] -->
The initial population found in Section 3.1.2 entirely consists of the three states of the general model, I0, H0, and P0. To determine the initial population of each of the states, we consider WHO data for the number of Ebola cases from November 12 2014. This data is given in Table 6.

<!-- b000190 | caption | pages [8] -->
Table 6: WHO Ebola data for November 12 2014 (World Health Organisation 2015a)

<!-- b000191 | prose | pages [8] -->
Total Cases Country Total Deaths 1,878 Guinea 1,142 6,822 Liberia 2,836 5,368 Sierra Leone 1,169 14,068 Overall 5,147

<!-- b000192 | prose | pages [8] -->
To estimate I0, we assume that all reported cases that have not resulted in death are still infected, and therefore

<!-- b000193 | prose | pages [8] -->
I0 = Total Cases −Total Deaths.

<!-- b000194 | prose | pages [8] -->
(7)

<!-- b000195 | prose | pages [8] -->
Although this neglects the possibility that a reported case has recovered from the virus, which would lead to overestimating I0, we accept the assumption. This is because the total number of infections is low relative to the total population, the WHO acknowledge that their statistics underestimate the Ebola epidemic (World Health Organisation 2014b), and that it is diﬃcult to otherwise predict current infections from the data. Based on this assumption, we also have

<!-- b000196 | prose | pages [8] -->
H0 = 0,

<!-- b000197 | prose | pages [8] -->
and

<!-- b000198 | prose | pages [8] -->
(8)

<!-- b000199 | prose | pages [8] -->
P0 = Initial Population −I0.

<!-- b000200 | prose | pages [8] -->
This gives the following values for the initial states.

<!-- b000201 | prose | pages [8] -->
(9)

<!-- b000202 | caption | pages [8] -->
Table 7: Initial states for the Ebola model

<!-- b000203 | prose | pages [8] -->
Country Guinea Liberia Sierra Leone Overall

<!-- b000204 | prose | pages [8] -->
3.1.4 α, β, γ

<!-- b000205 | prose | pages [8] -->
I0 P0 736 12,343,043 3,986 4,585,810 4,199 6,362,992 8,921 23,291,845

<!-- b000206 | prose | pages [8] -->
The parameters α, β, and γ are more diﬃcult to determine from available data. As an infected person will eventually transition to health or death, an important factor is the mortality rate of Ebola. An estimate of mortality rate, i.e. the likelihood of eventual death once infected, is given by

<!-- b000207 | prose | pages [8] -->
Mortality Rate = Total Deaths

<!-- b000208 | prose | pages [8] -->
Total Cases .

<!-- b000209 | prose | pages [8] -->
(10)

<!-- b000210 | prose | pages [8] -->
For this calculation, we use the latest data, to reduce the proportion of ongoing cases. This data is given in Table 8.

<!-- b000211 | caption | pages [8] -->
Table 8: WHO Ebola data for February 5 2015 (World Health Organisation 2015a)

<!-- b000212 | prose | pages [8] -->
Country Total Cases Guinea 2,986 Liberia 8,745 Sierra Leone 10,756 Overall 22,487 Total Deaths Mortality Rate 1,947 0.65204 3,746 0.42836 3,286 0.30550 8,979 0.39930

<!-- b000213 | furniture | pages [9] -->
Team #40764

<!-- b000214 | furniture | pages [9] -->
Page 9 of 25

<!-- b000215 | prose | pages [9] -->
However, to determine the daily rate of death and recovery, we introduce another parameter, T, the disease residence time. This is the average number of days required for an infection to result in either death or recovery. Using this parameter, we can determine the daily rates of death (γ) and recovery (β) among infected people, using

<!-- b000216 | prose | pages [9] -->
γ = Mortality Rate

<!-- b000217 | prose | pages [9] -->
and

<!-- b000218 | prose | pages [9] -->
, (11) T

<!-- b000219 | prose | pages [9] -->
β = 1 −Mortality Rate

<!-- b000220 | prose | pages [9] -->
.

<!-- b000221 | prose | pages [9] -->
(12) T

<!-- b000222 | prose | pages [9] -->
To determine α, the rate of disease transmission, we introduce the parameter K, the average number of healthy people to whom each infected person transmits the disease during the period they are infected. The parameter α is therefore given by

<!-- b000223 | prose | pages [9] -->
α = K

<!-- b000224 | prose | pages [9] -->
.

<!-- b000225 | prose | pages [9] -->
(13)

<!-- b000226 | prose | pages [9] -->
TP0

<!-- b000227 | prose | pages [9] -->
As there is no reliable data available to determine T and K, their values are prescribed to ﬁt the WHO data. Doing this ensures that our model is accurate, and allowing K to come as part of the solution provides a prediction of the transmission rate in current conditions. The parameters shown in Table 9 result in suitable estimates of the ﬁnal death and case counts post-simulation.

<!-- b000228 | caption | pages [9] -->
Table 9: Appropriate values of parameters

<!-- b000229 | prose | pages [9] -->
Country K T Guinea 0.90 45 Liberia 0.89 155 Sierra Leone 0.79 42 α β γ 1.6203e-9 7.7324e-3 1.4490e-2 1.2521e-9 3.6880e-3 2.7636e-3 2.9561e-9 1.6536e-3 7.2739e-3 5.0992e-10 Overall 0.86 73 8.2775e-3 5.5022e-3

<!-- b000230 | prose | pages [9] -->
To determine if the calculated values of K are appropriate, we cite a study by Meltzer et al. (2015), which gives estimates for K in various situations:

<!-- b000231 | prose | pages [9] -->
• For hospitalised patients, K = 0.12

<!-- b000232 | prose | pages [9] -->
• For home patients with eﬀective isolation, K = 0.18

<!-- b000233 | prose | pages [9] -->
• For home patients without eﬀective isolation, K = 1.8 (Meltzer et al. 2015)

<!-- b000234 | prose | pages [9] -->
All average values of K predicted in Table 9 are therefore feasible based on combinations of current treatment techniques. To validate residence time T, we cite a survivor’s anecdote in which the patient ﬁrst noticed symptoms after a ten day incubation, and reached their worst condition after sixteen days (Grant 2014). Assuming it takes a further sixteen days to recover fully gives T that corresponds closely

<!-- b000235 | prose | pages [9] -->
to Table 9. However, considering the result of Liberia, we infer that an appropriate T comes as an artefact of other aspects of the model, rather than from a physical basis.

<!-- b000236 | prose | pages [9] -->
3.2

<!-- b000237 | heading | pages [9] -->
Validation

<!-- b000238 | prose | pages [9] -->
The constant values of the parameters deﬁned in Section 3.1 completely specify the constants required to implement both the stochastic and deterministic models. These are used in both models to produce simulations for the spread of Ebola over the WHO reporting period. These simulations are compared with the WHO data to validate the models.

<!-- b000239 | prose | pages [9] -->
3.2.1

<!-- b000240 | heading | pages [9] -->
Stochastic Model

<!-- b000241 | prose | pages [9] -->
To produce stochastic results, the Matlab simulation is run ten times for each of the four regions modelled. The simulation is run over 85 days to simulate the period from 12 November 2014 to 5

<!-- b000242 | furniture | pages [10] -->
Team #40764

<!-- b000243 | furniture | pages [10] -->
Page 10 of 25

<!-- b000244 | prose | pages [10] -->
February 2015. The average number of cases and deaths at the end of the simulation are compared with WHO data to determine whether the model is accurate. Results are presented in Table 10. In the table, C and D represent the number of cases and deaths reported on February 5 2015 respectively, and subscripts M and W refer to the stochastic model and WHO data respectively. The parameter σ is the standard deviation of the ten simulation results.

<!-- b000245 | caption | pages [10] -->
Table 10: Results for February 5 2015 of stochastic simulations used to validate the model

<!-- b000246 | prose | pages [10] -->
Country CM σC DM σD

<!-- b000247 | prose | pages [10] -->
Guinea 3,053 110 1,957 Liberia 8,748 51 3,749 Sierra Leone 10,813 159 3,284 Overall 22,557 150 9,041

<!-- b000248 | prose | pages [10] -->
|CM−CW

<!-- b000249 | prose | pages [10] -->
|DM−DW |

<!-- b000250 | prose | pages [10] -->
|

<!-- b000251 | prose | pages [10] -->
CW DW

<!-- b000252 | prose | pages [10] -->
σC

<!-- b000253 | prose | pages [10] -->
σD 50 50 2,986 1,947 0.61 0.20 20 20 8,745 3,746 0.059 0.15 57 57 10,756 3,286 0.36 0.035 54 54 22,487 8,979 0.47 1.1

<!-- b000254 | prose | pages [10] -->
Note: ‘Overall’ in Table 10 represents the results of a separate simulation using parameters for the overall outbreak, not an arithmetic sum of results for each nation

<!-- b000255 | caption | pages [10] -->
Table 10 shows that the model predictions for total deaths and cases is very similar to the statistics

<!-- b000256 | prose | pages [10] -->
reported by the WHO. The fact that the real value falls within half a standard deviation of the model prediction in ﬁve of the eight statistics, and that no result is more than 1.1 standard deviations away from the actual value. We therefore conclude that the parameters in Section 3.1 accurately model the Ebola outbreak in all cases.

<!-- b000257 | prose | pages [10] -->
Further validation is provided by plotting simulation results against day-to-day WHO data for deaths and cases. Examples are provided in Figure 2.

<!-- b000258 | furniture | pages [10] -->


<!-- b000259 | prose | pages [10] -->
2100

<!-- b000260 | prose | pages [10] -->
WHO

<!-- b000261 | prose | pages [10] -->
2000

<!-- b000262 | prose | pages [10] -->
Simulations

<!-- b000263 | prose | pages [10] -->
1900

<!-- b000264 | prose | pages [10] -->
1800

<!-- b000265 | prose | pages [10] -->
Total Deaths

<!-- b000266 | prose | pages [10] -->
1700

<!-- b000267 | prose | pages [10] -->
1600

<!-- b000268 | prose | pages [10] -->
1500

<!-- b000269 | prose | pages [10] -->
1400

<!-- b000270 | prose | pages [10] -->
1300

<!-- b000271 | prose | pages [10] -->
1200

<!-- b000272 | furniture | pages [10] -->


<!-- b000273 | prose | pages [10] -->
1100 0 10 20 30 40 50 60 70 80 90

<!-- b000274 | prose | pages [10] -->
Time [d]

<!-- b000275 | prose | pages [10] -->
(a) Guinea

<!-- b000276 | furniture | pages [10] -->


<!-- b000277 | prose | pages [10] -->
3500

<!-- b000278 | prose | pages [10] -->
WHO Simulations

<!-- b000279 | prose | pages [10] -->
3000

<!-- b000280 | prose | pages [10] -->
Total Deaths

<!-- b000281 | prose | pages [10] -->
2500

<!-- b000282 | prose | pages [10] -->
2000

<!-- b000283 | prose | pages [10] -->
1500

<!-- b000284 | furniture | pages [10] -->


<!-- b000285 | prose | pages [10] -->
1000 0 10 20 30 40 50 60 70 80 90

<!-- b000286 | prose | pages [10] -->
Time [d]

<!-- b000287 | prose | pages [10] -->
(c) Sierra Leone

<!-- b000288 | furniture | pages [10] -->


<!-- b000289 | prose | pages [10] -->
3800

<!-- b000290 | prose | pages [10] -->
WHO Simulations

<!-- b000291 | prose | pages [10] -->
3700

<!-- b000292 | prose | pages [10] -->
3600

<!-- b000293 | prose | pages [10] -->
3500

<!-- b000294 | prose | pages [10] -->
Total Deaths

<!-- b000295 | prose | pages [10] -->
3400

<!-- b000296 | prose | pages [10] -->
3300

<!-- b000297 | prose | pages [10] -->
3200

<!-- b000298 | prose | pages [10] -->
3100

<!-- b000299 | prose | pages [10] -->
3000

<!-- b000300 | prose | pages [10] -->
2900

<!-- b000301 | furniture | pages [10] -->


<!-- b000302 | prose | pages [10] -->
2800 0 10 20 30 40 50 60 70 80 90

<!-- b000303 | prose | pages [10] -->
Time [d]

<!-- b000304 | prose | pages [10] -->
(b) Liberia

<!-- b000305 | furniture | pages [10] -->


<!-- b000306 | prose | pages [10] -->
9500

<!-- b000307 | prose | pages [10] -->
WHO

<!-- b000308 | prose | pages [10] -->
9000

<!-- b000309 | prose | pages [10] -->
Simulations

<!-- b000310 | prose | pages [10] -->
8500

<!-- b000311 | prose | pages [10] -->
8000

<!-- b000312 | prose | pages [10] -->
Total Deaths

<!-- b000313 | prose | pages [10] -->
7500

<!-- b000314 | prose | pages [10] -->
7000

<!-- b000315 | prose | pages [10] -->
6500

<!-- b000316 | prose | pages [10] -->
6000

<!-- b000317 | prose | pages [10] -->
5500

<!-- b000318 | furniture | pages [10] -->


<!-- b000319 | prose | pages [10] -->
5000 0 10 20 30 40 50 60 70 80 90

<!-- b000320 | prose | pages [10] -->
Time [d]

<!-- b000321 | prose | pages [10] -->
(d) Overall

<!-- b000322 | caption | pages [10] -->
Figure 2: Comparison of simulation results and WHO data for day-to-day death count in each region

<!-- b000323 | furniture | pages [11] -->
Team #40764

<!-- b000324 | furniture | pages [11] -->
Page 11 of 25

<!-- b000325 | prose | pages [11] -->
As Figure 2 shows, the simulations track the WHO reported daily death count reasonably well. The model predictions produce a more linear trend than the WHO data as we assume the treatment practices (state transition rate parameters) are constant throughout the period. In addition, the WHO data is taken at irregular intervals, and each country updates their data on diﬀerent dates. This suggests the WHO data points may not accurately display the underlying trend in disease spread. We therefore accept the predictions of the model are valid based on WHO data.

<!-- b000326 | prose | pages [11] -->
3.2.2

<!-- b000327 | heading | pages [11] -->
Deterministic Model

<!-- b000328 | prose | pages [11] -->
As the deterministic model only considers the population of the three states In, Hn, and Pn, and does not account for state transitions, we cannot compare with WHO data. However, given the success of the stochastic model, we assume that the deterministic model matches WHO data if its results match the stochastic model. Table 11 shows the results for February 5 2015 of simulating the deterministic model with the parameters in Section 3.1. In the table, subscripts D and S denote the deterministic and stochastic models respectively.

<!-- b000329 | caption | pages [11] -->
Table 11: Comparison of stochastic and deterministic results for February 5 2015

<!-- b000330 | prose | pages [11] -->
Country IS ID HS Guinea 640 618 457 Liberia HD PS PD 438 12,412,178 12,411,344 1,228 3,769 3,789 1,203 4,609,770 4,609,491 4,805 2,718 2,789 Sierra Leone 4,789 6,394,555 6,394,146 5,820 Overall 7,690 7,684 5,757 23,419,606 23,417,858

<!-- b000331 | prose | pages [11] -->
As expected, the deterministic model shows good agreement with the stochastic simulations if the same parameters are used in the model. A reason for the small discrepancy in the results is that the timestep used in each simulation is diﬀerent. The stochastic model applies a near-continuous timestep, whilst the deterministic model is updated using a timestep of one day. The stochastic model also incorporates randomness, which creates deviations from deterministic results. An example of this is illustrated in Figure 3.

<!-- b000332 | prose | pages [11] -->
9000

<!-- b000333 | prose | pages [11] -->
9000

<!-- b000334 | prose | pages [11] -->
8500

<!-- b000335 | prose | pages [11] -->
8500

<!-- b000336 | prose | pages [11] -->
In

<!-- b000337 | prose | pages [11] -->
In

<!-- b000338 | prose | pages [11] -->
8000

<!-- b000339 | prose | pages [11] -->
8000

<!-- b000340 | prose | pages [11] -->
Deterministic

<!-- b000341 | prose | pages [11] -->
7500

<!-- b000342 | prose | pages [11] -->
7500

<!-- b000343 | furniture | pages [11] -->


<!-- b000344 | furniture | pages [11] -->


<!-- b000345 | prose | pages [11] -->
0

<!-- b000346 | prose | pages [11] -->
0

<!-- b000347 | prose | pages [11] -->
10

<!-- b000348 | prose | pages [11] -->
10

<!-- b000349 | prose | pages [11] -->
20

<!-- b000350 | prose | pages [11] -->
20

<!-- b000351 | prose | pages [11] -->
30

<!-- b000352 | prose | pages [11] -->
30

<!-- b000353 | prose | pages [11] -->
Stochastic

<!-- b000354 | prose | pages [11] -->
40

<!-- b000355 | prose | pages [11] -->
40

<!-- b000356 | prose | pages [11] -->
40

<!-- b000357 | prose | pages [11] -->
40

<!-- b000358 | prose | pages [11] -->
50

<!-- b000359 | prose | pages [11] -->
50

<!-- b000360 | prose | pages [11] -->
60

<!-- b000361 | prose | pages [11] -->
60

<!-- b000362 | prose | pages [11] -->
70

<!-- b000363 | prose | pages [11] -->
70

<!-- b000364 | prose | pages [11] -->
80

<!-- b000365 | prose | pages [11] -->
80

<!-- b000366 | prose | pages [11] -->
90

<!-- b000367 | prose | pages [11] -->
90

<!-- b000368 | prose | pages [11] -->
Time [d]

<!-- b000369 | prose | pages [11] -->
Time [d]

<!-- b000370 | caption | pages [11] -->
Figure 3: Comparison of number of infected patients over time for the overall virus, for both

<!-- b000371 | prose | pages [11] -->
deterministic and stochastic models

<!-- b000372 | furniture | pages [12] -->
Team #40764

<!-- b000373 | furniture | pages [12] -->
Page 12 of 25

<!-- b000374 | caption | pages [12] -->
Figure 3 shows that the stochastic models introduce random ﬂuctuations about the underlying

<!-- b000375 | prose | pages [12] -->
deterministic solution. We conclude that both the deterministic and stochastic models provide a means of accurately tracking the spread of Ebola. In our analysis of the predicted eﬀects of possible treatment regimes, we use the predictions of both models.

<!-- b000376 | prose | pages [12] -->
4

<!-- b000377 | heading | pages [12] -->
Results - Predicting the Eﬀect of Improved Treatment

<!-- b000378 | prose | pages [12] -->
To determine the eﬀect of new treatment regimes, the February 5 2015 parameters given in Table 11 are used as initial states (I0, H0, P0) to the model. We initially consider the projected spread of Ebola if the treatment regime in practice from 12 November 2014 to 5 February 2015 is maintained – that is, if the values of state transition rate parameters determined based on WHO data are held constant. The simulations are run in both the short-term (using the stochastic model), and the long term (using the deterministic model). We then independently change parameters based on our interpretations of diﬀerent options to improve treatment. To provide targeted treatment, we perform the simulations in each of the three nations. The possible treatment options are described in Section 4.1.

<!-- b000379 | prose | pages [12] -->
4.1 Treatment Options

<!-- b000380 | prose | pages [12] -->
In our analysis, we consider three diﬀerent treatment options. Each has a unique eﬀect on the state transition rate parameters. The treatment options are

<!-- b000381 | prose | pages [12] -->
• Improving medical services

<!-- b000382 | prose | pages [12] -->
• Improving medicine

<!-- b000383 | prose | pages [12] -->
• Developing a vaccine

<!-- b000384 | prose | pages [12] -->
4.1.1 Improve Medical Services - Decrease α

<!-- b000385 | prose | pages [12] -->
Improved medical services entail improved quarantine procedures, for example by increasing medical staﬀ, hospital space, or public education. Doing this will improve patient isolation, decreasingα the rate of Ebola transmission from infected to healthy people. If we assume that it is impossible to isolate a patient in the incubation stage, which lasts a quarter of infection residence time, data from Meltzer et al. (2015) provides a means of estimating the minimum K.

<!-- b000386 | prose | pages [12] -->
Kmin = 0.75(0.12) + 0.25(1.8) = 0.54.

<!-- b000387 | prose | pages [12] -->
(14)

<!-- b000388 | prose | pages [12] -->
As this is less than the model predictions in Table 9, there is scope to reduce the spread of the virus by improving medical services.

<!-- b000389 | prose | pages [12] -->
4.1.2 Improve Medicine - Decrease γ, Increase β

<!-- b000390 | prose | pages [12] -->
We deﬁne ‘medicine’ to incorporate all techniques available to reduce the mortality rate, including

<!-- b000391 | prose | pages [12] -->
existing techniques such as providing intravenous nutrients, and newly developed drugs, for example by the World Medical Association. As the WMA medicine aﬀects patients even in the early stages of infection, we assume that improving either the quality or quantity of medicine will decrease the average mortality of an infected patient. This increases the rate of recovery, β, and decreases the rate of death from infection, γ. We consider the eﬀects of a range of medicine eﬀectiveness in our predictions. Changing the relevant parameters encompasses changes in the quantity of medicine, as well as the eﬀectiveness of distribution systems.

<!-- b000392 | furniture | pages [13] -->
Team #40764

<!-- b000393 | prose | pages [13] -->
4.1.3 Develop Vaccine - Increase ν

<!-- b000394 | furniture | pages [13] -->
Page 13 of 25

<!-- b000395 | prose | pages [13] -->
Developing a vaccine opens the possibility of transition from the vulnerable healthy state to the immune healthy state. This will decrease the rate of Ebola spread. To model a vaccine, we consider non-zero ν. As there is no vaccine available, we consider a range of diﬀerent distribution speeds in our simulations. In our simulation ν is related to the number of successful vaccinations.

<!-- b000396 | prose | pages [13] -->
4.2

<!-- b000397 | heading | pages [13] -->
Sensitivity Analysis

<!-- b000398 | prose | pages [13] -->
Sensitivity analysis is performed using both the stochastic and deterministic models. Short and medium-term simulations of six months, one year, and two years are performed using the stochastic model. These are important to guide immediate prevention strategy, and some assumptions (e.g. immunity is retained) are more likely to hold in the short-term. Long-term steady state conditions are predicted using the deterministic model. Speciﬁcally, we seek combinations of rate parameters that drive the steady-state number of infections to zero.

<!-- b000399 | prose | pages [13] -->
4.2.1

<!-- b000400 | heading | pages [13] -->
Stochastic Model

<!-- b000401 | prose | pages [13] -->
Stochastic simulations are Short-Term Projections Based on Current Treatment Levels performed using the same rate parameters and February 5 2015 initial values to predict the total number of cases and deaths in each country over six months, one year, and two years at the current level of treatment. As with the initial modelling the average of ten simulations is taken. These results are presented in Table 12. In the table, C and D represent the number of new cases since February 5 2015. We change this convention as we no longer need to match WHO data, the initial states are better deﬁned, and new cases provides a better indication of disease spread.

<!-- b000402 | caption | pages [13] -->
Table 12: Projection of Ebola spread at current level of treatment (new cases and new deaths)

<!-- b000403 | heading | pages [13] -->
6 Months

<!-- b000404 | prose | pages [13] -->
Country C D Guinea 2,049 1,441 Liberia 3,873 1,828 Sierra Leone 6,262 2,380

<!-- b000405 | heading | pages [13] -->
1 Year

<!-- b000406 | heading | pages [13] -->
2 Years

<!-- b000407 | prose | pages [13] -->
C D C D 3,625 2,549 6,093 4,201 7,303 3,428 13,857 6,391 9,180 3,479 11,199 4,224

<!-- b000408 | prose | pages [13] -->
In our analysis, we consider ten percent changes in the relevant parameters, and other reasonable targets based on improved treatment methods. This is suitable for short term modelling, where large-scale changes are unlikely to be possible. We apply the stochastic model for each of the three nations, to determine which strategy is most useful in the short-term, and where they are optimally applied. In each case, data is the average of ten stochastic simulations.

<!-- b000409 | prose | pages [13] -->
Eﬀect of Improving Medical Services To assess the impact of increasing medical services in an individual country over six months, one year, and two years, we consider two cases:

<!-- b000410 | prose | pages [13] -->
• A 10% decrease in transmissions per infected person, i.e. decreasing α by 10%

<!-- b000411 | prose | pages [13] -->
• Decrease transmissions per infected person to the minimum, Kmin = 0.54

<!-- b000412 | prose | pages [13] -->
All other parameters are held constant in the stochastic simulations, and once again an average of ten simulations is taken. The results are given in terms of the overall reduction in deaths or cases measured after the given period. Intermediate data processing is omitted for simplicity. The results are given in Table 13 and Table 14 respectively.

<!-- b000413 | furniture | pages [14] -->
Team #40764

<!-- b000414 | furniture | pages [14] -->
Page 14 of 25

<!-- b000415 | caption | pages [14] -->
Table 13: Net change in cases and deaths if transmissions per infected person is decreased by 10%

<!-- b000416 | heading | pages [14] -->
6 Months

<!-- b000417 | prose | pages [14] -->
Country C D Guinea -589 -280 Liberia -576 -119 Sierra Leone -1,323 -310

<!-- b000418 | heading | pages [14] -->
1 Year

<!-- b000419 | heading | pages [14] -->
2 Years

<!-- b000420 | prose | pages [14] -->
C D C D -1,386 -771 -2,956 -1,780 -1,359 -332 -3,491 -1,081 -2,672 -731 -4,395 -1,347

<!-- b000421 | caption | pages [14] -->
Table 14: Net change in cases and deaths if transmissions per infected person is decreased to the

<!-- b000422 | prose | pages [14] -->
minimum, K = 0.54

<!-- b000423 | heading | pages [14] -->
6 Months

<!-- b000424 | prose | pages [14] -->
Country C D Guinea -1,378 -654 Liberia -1,898 -335 Sierra Leone -3,440 -808

<!-- b000425 | heading | pages [14] -->
1 Year

<!-- b000426 | heading | pages [14] -->
2 Years

<!-- b000427 | prose | pages [14] -->
C D C D -2,889 -1,667 -5,325 -3,288 -4,196 -1,057 -9,562 -3,156 -5,901 -1,673 -7,912 -2,421

<!-- b000428 | prose | pages [14] -->
To assess the impact of improving medicines, we consider: Eﬀect of Improving Medicine

<!-- b000429 | prose | pages [14] -->
• A 10% decrease in average mortality rate

<!-- b000430 | prose | pages [14] -->
• Distribution of a new WMA medicine such that average mortality rate is decreased to 30% in all regions

<!-- b000431 | prose | pages [14] -->
• Distribution of a new WMA medicine such that average mortality rate is decreased to 15% in all regions

<!-- b000432 | prose | pages [14] -->
The eﬀects of mortality rate on the parameters β and γ are determined by Equations (11) and (12). Average simulation results are given in Table 15, Table 16 and Table 17 respectively. In these tables, any increases in cases occurring in some simulations are likely to be caused by randomness.

<!-- b000433 | caption | pages [14] -->
Table 15: Net change in cases and deaths if mortality rate is decreased by 10%

<!-- b000434 | heading | pages [14] -->
6 Months

<!-- b000435 | prose | pages [14] -->
Country C D Guinea -116 -205 Liberia +18 -193 Sierra Leone +121 -175

<!-- b000436 | heading | pages [14] -->
1 Year

<!-- b000437 | heading | pages [14] -->
2 Years

<!-- b000438 | prose | pages [14] -->
C D C D -311 -393 -199 -532 +146 -304 -25 -676 -105 -380 -423 -575

<!-- b000439 | caption | pages [14] -->
Table 16: Net change in cases and deaths if the medicine decreases mortality rate to 30% in all regions

<!-- b000440 | heading | pages [14] -->
6 Months

<!-- b000441 | prose | pages [14] -->
Country C D Guinea -23 -775 Liberia -31 -571 Sierra Leone +75 -3

<!-- b000442 | heading | pages [14] -->
1 Year

<!-- b000443 | heading | pages [14] -->
2 Years

<!-- b000444 | prose | pages [14] -->
C D C D -124 -1,215 -586 -2,401 -24 -1,022 +7 -1,896 -231 -147 -239 -178

<!-- b000445 | caption | pages [14] -->
Table 17: Net change in cases and deaths if the medicine decreases mortality rate to 15% in all regions

<!-- b000446 | heading | pages [14] -->
6 Months

<!-- b000447 | prose | pages [14] -->
Country C D Guinea -15 -1,109 Liberia -43 -1,196 Sierra Leone +67 -1,188

<!-- b000448 | heading | pages [14] -->
1 Year

<!-- b000449 | heading | pages [14] -->
2 Years

<!-- b000450 | prose | pages [14] -->
C D C D -151 -1,974 -748 -3,333 +111 -2,221 +2 -4,159 +14 -1,743 +62 -2,168

<!-- b000451 | furniture | pages [15] -->
Team #40764

<!-- b000452 | prose | pages [15] -->
Eﬀect of Vaccination

<!-- b000453 | furniture | pages [15] -->
Page 15 of 25

<!-- b000454 | prose | pages [15] -->
To assess the impact of distributing an eﬀective vaccine, we consider:

<!-- b000455 | prose | pages [15] -->
• A vaccination distribution rate in which approximately 10% of the population will be successfully vaccinated in two years

<!-- b000456 | prose | pages [15] -->
• A vaccination distribution rate in which approximately 30% of the population will be successfully vaccinated in two years

<!-- b000457 | prose | pages [15] -->
• A vaccination distribution rate in which approximately 50% of the population will be successfully vaccinated in two years

<!-- b000458 | prose | pages [15] -->
The parameter ν is given by

<!-- b000459 | prose | pages [15] -->
ν = V

<!-- b000460 | prose | pages [15] -->
730, (15)

<!-- b000461 | prose | pages [15] -->
where V is the proportion of the population that is vaccinated in two years. This gives ν = 1.3699e-4, ν = 4.1096e-4, and ν = 6.8493e-4 for the three respective cases. Simulating the stochastic model with these parameters gives results shown in Table 18, Table 19, and Table 20.

<!-- b000462 | caption | pages [15] -->
Table 18: Net change in cases and deaths if a vaccine is introduced to approximately 10% of the

<!-- b000463 | prose | pages [15] -->
population in two years

<!-- b000464 | heading | pages [15] -->
6 Months

<!-- b000465 | prose | pages [15] -->
Country C D Guinea -149 -68 Liberia -39 -32 Sierra Leone -10 +25

<!-- b000466 | heading | pages [15] -->
1 Year

<!-- b000467 | heading | pages [15] -->
2 Years

<!-- b000468 | prose | pages [15] -->
C D C D -451 -250 -1,578 -911 -219 -36 -1,313 -347 -488 -130 -1,045 -315

<!-- b000469 | caption | pages [15] -->
Table 19: Net change in cases and deaths if a vaccine is introduced to approximately 30% of the

<!-- b000470 | prose | pages [15] -->
population in two years

<!-- b000471 | heading | pages [15] -->
6 Months

<!-- b000472 | prose | pages [15] -->
Country C D Guinea -246 -108 Liberia -159 -52 Sierra Leone -370 -60

<!-- b000473 | heading | pages [15] -->
1 Year

<!-- b000474 | heading | pages [15] -->
2 Years

<!-- b000475 | prose | pages [15] -->
C D C D -965 -515 -2,688 -1,586 -614 -138 -3,367 -943 -1,230 -302 -2,844 -849

<!-- b000476 | caption | pages [15] -->
Table 20: Net change in cases and deaths if a vaccine is introduced to approximately 50% of the

<!-- b000477 | prose | pages [15] -->
population in two years

<!-- b000478 | heading | pages [15] -->
6 Months

<!-- b000479 | prose | pages [15] -->
Country C D Guinea -310 -127 Liberia -318 -55 Sierra Leone -513 -76

<!-- b000480 | heading | pages [15] -->
1 Year

<!-- b000481 | heading | pages [15] -->
2 Years

<!-- b000482 | prose | pages [15] -->
C D C D -1,054 -564 -3,363 -1,999 -1,118 -215 -4,963 -1,463 -1,798 -477 -3,539 -1,033

<!-- b000483 | prose | pages [15] -->
We assume that the primary measure of an eﬀective treatment is to prevent the highest Analysis number of total deaths. Therefore, to illustrate the most eﬃcient treatment method, we plot the reduction in total deaths against the medium-term percentage change in current treatment conditions, for each nation and type of treatment. In lieu of cost data, we assume that treatment eﬃciency is proportional to the reduction in deaths per percentage change in treatment. When parameters are set to uniform values across all regions, percentage change is calculated based on the initial value for the particular region. For example, change in mortality due to medicine is determined with respect to values in Table 8. The resulting short-term (six months) and medium-term (two years) plots are shown in Figure 4 and Figure 5 respectively.

<!-- b000484 | furniture | pages [16] -->
Team #40764

<!-- b000485 | prose | pages [16] -->
1500

<!-- b000486 | prose | pages [16] -->
Net Six−Month Reduction in Deaths

<!-- b000487 | prose | pages [16] -->
1000

<!-- b000488 | prose | pages [16] -->
500

<!-- b000489 | prose | pages [16] -->
0

<!-- b000490 | furniture | pages [16] -->


<!-- b000491 | prose | pages [16] -->
0 20 40

<!-- b000492 | furniture | pages [16] -->
Page 16 of 25

<!-- b000493 | furniture | pages [16] -->


<!-- b000494 | prose | pages [16] -->
Guinea Liberia Sierra Leone Medical Services Medicine Vaccine

<!-- b000495 | prose | pages [16] -->
60 80 100

<!-- b000496 | prose | pages [16] -->
Percentage Increase in Treatment [%]

<!-- b000497 | caption | pages [16] -->
Figure 4: Net short-term (six month) reduction in deaths vs. percentage increase in treatment for

<!-- b000498 | prose | pages [16] -->
diﬀerent nations and treatment methods

<!-- b000499 | prose | pages [16] -->
5000

<!-- b000500 | prose | pages [16] -->
Net Two−Year Reduction in Deaths

<!-- b000501 | prose | pages [16] -->
4500

<!-- b000502 | prose | pages [16] -->
4000

<!-- b000503 | prose | pages [16] -->
3500

<!-- b000504 | prose | pages [16] -->
3000

<!-- b000505 | prose | pages [16] -->
2500

<!-- b000506 | prose | pages [16] -->
2000

<!-- b000507 | prose | pages [16] -->
1500

<!-- b000508 | prose | pages [16] -->
1000

<!-- b000509 | prose | pages [16] -->
500

<!-- b000510 | prose | pages [16] -->
0

<!-- b000511 | furniture | pages [16] -->


<!-- b000512 | prose | pages [16] -->
0 10 20 30 40

<!-- b000513 | furniture | pages [16] -->


<!-- b000514 | prose | pages [16] -->
Guinea Liberia Sierra Leone Medical Services Medicine Vaccine

<!-- b000515 | prose | pages [16] -->
50 60 70 80 90 100

<!-- b000516 | prose | pages [16] -->
Percentage Increase in Treatment [%]

<!-- b000517 | caption | pages [16] -->
Figure 5: Net medium term (two year) reduction in deaths vs. percentage increase in treatment for

<!-- b000518 | prose | pages [16] -->
diﬀerent nations and treatment methods

<!-- b000519 | furniture | pages [17] -->
Team #40764

<!-- b000520 | furniture | pages [17] -->
Page 17 of 25

<!-- b000521 | prose | pages [17] -->
In these ﬁgures, treatments that appear above the dotted trendline are relatively eﬃcient, and are therefore recommended for implementation. This is because they require a reduced percentage increase in treatment to achieve relatively greater reductions in death.

<!-- b000522 | prose | pages [17] -->
In the short-term results show that improving medicine and medical services are more eﬃcient method of reducing deaths than vaccination. The most eﬀective methods of reducing death in the short-term are medicines that substantially decrease the average mortality rate. For example, in Sierra Leone, an eﬀective medicine can save 47% more lives in the short-term than the maximum possible improvement in medical services. These results are sensible considering the evolution of disease. The vaccine will not prevent many cases in the short-term, and more immediate treatment methods such as medicine are more eﬀective in reducing short-term deaths. Also, the results show that greater eﬃciencies are attained when the short-term strategies are deployed in Sierra Leone. This is because it has a higher number of initial cases.

<!-- b000523 | prose | pages [17] -->
However, as the medicine does not cause signiﬁcant reductions in the number of cases over two years, its eﬀectiveness in reducing deaths is decreased in the medium-term relative to other treatment methods. As Figure 5 shows, vaccination becomes a more competitive treatment option in the medium-term, whilst improving medical services is still important. In addition, the eﬃciency of introducing the three treatment methods is similar in each nation. Health services and vaccinations have a strong eﬀect in Guinea in gross and relative terms. This ﬁnding is important, as Guinea has by far the lowest proportion of cases of the three nations, and will be neglected if treatment is allocated according to this proportionality alone.

<!-- b000524 | prose | pages [17] -->
Based on this analysis, we recommend short-term provision of improved medical services and medicine, especially targeting aﬀected areas in Sierra Leone. However, if research shows that the current Ebola strain is likely to last up to two years, vaccination becomes a viable strategy, and all nations should be targeted for improved medical services and medicine. It must be emphasised that this analysis does not determine the relative cost of each treatment method. Cost-beneﬁt analysis is left to policy-makers with knowledge of the cost of each treatment method. The result is likely to be quite diﬀerent from the conclusions expressed here.

<!-- b000525 | prose | pages [17] -->
4.2.2

<!-- b000526 | heading | pages [17] -->
Deterministic Model

<!-- b000527 | prose | pages [17] -->
Long-term projections of the Long-Term Projections Based on Current Treatment Levels evolution of the Ebola outbreak are performed using the deterministic model. Once again, the rate parameters used are the constant values found to accurately predict the disease in the WHO’s reporting period. Results are shown in Figure 6.

<!-- b000528 | prose | pages [17] -->
5

<!-- b000529 | prose | pages [17] -->
7

<!-- b000530 | prose | pages [17] -->
x 10

<!-- b000531 | prose | pages [17] -->
x 10

<!-- b000532 | prose | pages [17] -->
14

<!-- b000533 | prose | pages [17] -->
18

<!-- b000534 | prose | pages [17] -->
16

<!-- b000535 | prose | pages [17] -->
12

<!-- b000536 | prose | pages [17] -->
14

<!-- b000537 | prose | pages [17] -->
10

<!-- b000538 | prose | pages [17] -->
12

<!-- b000539 | prose | pages [17] -->
8

<!-- b000540 | prose | pages [17] -->
10

<!-- b000541 | prose | pages [17] -->
Hn

<!-- b000542 | prose | pages [17] -->
In

<!-- b000543 | prose | pages [17] -->
8

<!-- b000544 | prose | pages [17] -->
6

<!-- b000545 | prose | pages [17] -->
6

<!-- b000546 | prose | pages [17] -->
4

<!-- b000547 | prose | pages [17] -->
4

<!-- b000548 | prose | pages [17] -->
2

<!-- b000549 | prose | pages [17] -->
2

<!-- b000550 | prose | pages [17] -->
0

<!-- b000551 | prose | pages [17] -->
0

<!-- b000552 | prose | pages [17] -->
0 1 2 3 4 5 6

<!-- b000553 | prose | pages [17] -->
0 1 2

<!-- b000554 | prose | pages [17] -->
7

<!-- b000555 | prose | pages [17] -->
x 10 3.4

<!-- b000556 | prose | pages [17] -->
3.2

<!-- b000557 | prose | pages [17] -->
3

<!-- b000558 | prose | pages [17] -->
Pn

<!-- b000559 | prose | pages [17] -->
2.8

<!-- b000560 | prose | pages [17] -->
2.6

<!-- b000561 | prose | pages [17] -->
2.4

<!-- b000562 | prose | pages [17] -->
2.2

<!-- b000563 | prose | pages [17] -->
3 4 5 6

<!-- b000564 | prose | pages [17] -->
0 1 2 3 4 5 6

<!-- b000565 | prose | pages [17] -->
Time [d]

<!-- b000566 | prose | pages [17] -->
Time [d]

<!-- b000567 | prose | pages [17] -->
4

<!-- b000568 | prose | pages [17] -->
x 10

<!-- b000569 | prose | pages [17] -->
Time [d]

<!-- b000570 | prose | pages [17] -->
4

<!-- b000571 | prose | pages [17] -->
4

<!-- b000572 | prose | pages [17] -->
x 10

<!-- b000573 | prose | pages [17] -->
x 10

<!-- b000574 | prose | pages [17] -->
(b) Immune

<!-- b000575 | prose | pages [17] -->
(a) Infected

<!-- b000576 | prose | pages [17] -->
(c) Vulnerable

<!-- b000577 | caption | pages [17] -->
Figure 6: Long-term deterministic simulation of the overall virus

<!-- b000578 | furniture | pages [18] -->
Team #40764

<!-- b000579 | furniture | pages [18] -->
Page 18 of 25

<!-- b000580 | prose | pages [18] -->
Using the numbers for the overall outbreak, we ﬁnd that the number of infected and immune people diverge to inﬁnity, whilst the number of vulnerable people is stable. The model therefore emphasises the urgent necessity of improving treatment. In particular, the ﬁrst peak in the infected plot occurs after about 3000 days, so at minimum, medium-term strategies such as those suggested by the stochastic model are required. In addition to this, analysing the ﬁxed points of the deterministic model provides insight into parameter relationships that drive long-term steady state number of infections to zero.

<!-- b000581 | heading | pages [18] -->
Fixed Point and Stability of Deterministic Model

<!-- b000582 | prose | pages [18] -->
To analyse the long-term eﬀects of changing the state transition rate parameters in a general outbreak, we consider the ﬁxed points of the deterministic system. We then determine relationships between the parameters that lead to stable solutions that eradicate the virus. The structure of treatment can then be altered based on the results to produce a strategy that eradicates Ebola long-term.

<!-- b000583 | prose | pages [18] -->
To determine the ﬁxed points of the system, we recall the deterministic diﬀerence equations (3),

<!-- b000584 | prose | pages [18] -->


<!-- b000585 | prose | pages [18] -->
f(Pn, In, Hn) := Pn+1 = Pn(1 + ϵ −φ −ν −αIn) + ϵHn

<!-- b000586 | prose | pages [18] -->
 

<!-- b000587 | prose | pages [18] -->
g(Pn, In, Hn) := In+1 = In(1 + ϵ −γ −β) + αInPn

<!-- b000588 | prose | pages [18] -->


<!-- b000589 | prose | pages [18] -->
h(Pn, In, Hn) := Hn+1 = Hn(1 −φ) + βIn + νPn.

<!-- b000590 | prose | pages [18] -->


<!-- b000591 | prose | pages [18] -->
To determine the ﬁxed points of this model, we solve the system

<!-- b000592 | prose | pages [18] -->


<!-- b000593 | prose | pages [18] -->
Pn+1 = Pn

<!-- b000594 | prose | pages [18] -->
 

<!-- b000595 | prose | pages [18] -->
(16)

<!-- b000596 | prose | pages [18] -->
In+1 = In

<!-- b000597 | prose | pages [18] -->


<!-- b000598 | prose | pages [18] -->
Hn+1 = Hn,

<!-- b000599 | prose | pages [18] -->


<!-- b000600 | prose | pages [18] -->
which gives 

<!-- b000601 | prose | pages [18] -->
Pn(ϵ −φ −ν) −αInPn + ϵHn = 0

<!-- b000602 | prose | pages [18] -->
 

<!-- b000603 | prose | pages [18] -->
(17)

<!-- b000604 | prose | pages [18] -->
In(ϵ −γ −β) + αInPn = 0

<!-- b000605 | prose | pages [18] -->


<!-- b000606 | prose | pages [18] -->
Hn(−φ) + βIn + νPn = 0.

<!-- b000607 | prose | pages [18] -->


<!-- b000608 | prose | pages [18] -->
The system (17) has eight possible steady state solutions. These are summarised in Table 21. The table lists all possible steady state values for each of the states, and lists any conditions on the parameters that arise in each case.

<!-- b000609 | furniture | pages [19] -->
Team #40764

<!-- b000610 | furniture | pages [19] -->
Page 19 of 25

<!-- b000611 | caption | pages [19] -->
Table 21: Fixed points of the deterministic model

<!-- b000612 | prose | pages [19] -->
Case Steady state

<!-- b000613 | prose | pages [19] -->
Hn = 0

<!-- b000614 | prose | pages [19] -->
In = 0

<!-- b000615 | prose | pages [19] -->
1

<!-- b000616 | prose | pages [19] -->
Pn = 0

<!-- b000617 | prose | pages [19] -->
Hn = H

<!-- b000618 | prose | pages [19] -->
In = 0

<!-- b000619 | prose | pages [19] -->
2

<!-- b000620 | prose | pages [19] -->
Pn = 0

<!-- b000621 | prose | pages [19] -->
Hn = 0

<!-- b000622 | prose | pages [19] -->
In = I

<!-- b000623 | prose | pages [19] -->
3

<!-- b000624 | prose | pages [19] -->
Pn = 0

<!-- b000625 | prose | pages [19] -->
Hn = 0

<!-- b000626 | prose | pages [19] -->
In = 0

<!-- b000627 | prose | pages [19] -->
4

<!-- b000628 | prose | pages [19] -->
Pn = P

<!-- b000629 | prose | pages [19] -->
Pn = 0 5 φHn = βIn

<!-- b000630 | prose | pages [19] -->
In = 0 6 φHn = νPn

<!-- b000631 | prose | pages [19] -->
Conditions Description

<!-- b000632 | prose | pages [19] -->
Ebola causes extinction None in the region examined.

<!-- b000633 | prose | pages [19] -->
Everyone will be immune. This is only the case

<!-- b000634 | prose | pages [19] -->
ϵ = 0

<!-- b000635 | prose | pages [19] -->
if there is no birth.

<!-- b000636 | prose | pages [19] -->
Everyone will be infected. This is only the case if

<!-- b000637 | prose | pages [19] -->
γ = ϵ

<!-- b000638 | prose | pages [19] -->
there is no recovery and the

<!-- b000639 | prose | pages [19] -->
β = 0

<!-- b000640 | prose | pages [19] -->
rates of birth and death of infected people are equal.

<!-- b000641 | prose | pages [19] -->
Everyone will be vulnerable.

<!-- b000642 | prose | pages [19] -->
ν = 0

<!-- b000643 | prose | pages [19] -->
This is the case only if there

<!-- b000644 | prose | pages [19] -->
ϵ = φ

<!-- b000645 | prose | pages [19] -->
is no vaccination.

<!-- b000646 | prose | pages [19] -->
No vulnerable person will remain.

<!-- b000647 | prose | pages [19] -->
ϵ = 0

<!-- b000648 | prose | pages [19] -->
But since parameters are

<!-- b000649 | prose | pages [19] -->
γ = −β

<!-- b000650 | prose | pages [19] -->
non-negative we have β = γ = 0. Hence Hn = 0, just like Case 3.

<!-- b000651 | prose | pages [19] -->
No infected person will remain, and a constant

<!-- b000652 | prose | pages [19] -->
ϵ = φ

<!-- b000653 | prose | pages [19] -->
proportion of people will be immune.

<!-- b000654 | prose | pages [19] -->
No immune person

<!-- b000655 | prose | pages [19] -->
β(φ + ν −ϵ) = ν(γ + β −ϵ)

<!-- b000656 | prose | pages [19] -->
Hn = 0 In = (ϵ −φ −ν)/α 7 Pn = (γ + β −ϵ)/α

<!-- b000657 | prose | pages [19] -->
φ[−β(γ+β−ϵ)(ϵν+φ(ϵ−γ−ν)

<!-- b000658 | prose | pages [19] -->
Hn = 1

<!-- b000659 | prose | pages [19] -->
+ α(ϵβ−φ(γ+β−ϵ))) ν α(γ + β −ϵ)]

<!-- b000660 | prose | pages [19] -->
will remain, and a constant

<!-- b000661 | prose | pages [19] -->
γ + β ≥ϵ

<!-- b000662 | prose | pages [19] -->
proportion of people

<!-- b000663 | prose | pages [19] -->
φ + ν ≥ϵ

<!-- b000664 | prose | pages [19] -->
will be infected.

<!-- b000665 | prose | pages [19] -->
Each of the states will share a constant

<!-- b000666 | prose | pages [19] -->
0 < Hn, In, Pn < ∞

<!-- b000667 | prose | pages [19] -->
8

<!-- b000668 | prose | pages [19] -->
In = (γ+β−ϵ)(ϵν+φ(ϵ−φ−ν))

<!-- b000669 | prose | pages [19] -->
α(ϵβ−φ(γ+β−ϵ)) Pn = (γ + β −ϵ)/α

<!-- b000670 | prose | pages [19] -->
proportion of the total population.

<!-- b000671 | prose | pages [19] -->
To eradicate the virus, we seek a ﬁxed point solution such that In = 0. In addition, we aim to control the outbreak by varying the parameters α, β, γ, and ν, as with the stochastic model. We do not consider Case 1, as it represents extinction, and does not depend on the parameters. Case 2 is also unrealistic, as it relies there being no births. Case 4 is also not considered, as it does not account for the possibility of vaccination. We therefore seek parameter values that lead to Case 6.

<!-- b000672 | prose | pages [19] -->
To determine these parameters, we consider the stability of the ﬁxed point, and determine parameters that lead to a stable steady-state solution. By the Jury conditions (De Leenheer 2009), a ﬁxed point is stable if

<!-- b000673 | prose | pages [19] -->
|tr(J)| < 1 + det(J) < 2, (18)

<!-- b000674 | prose | pages [19] -->
where J is the Jacobian matrix associated with the diﬀerence equations. The Jacobian matrix for the system (3) is

<!-- b000675 | prose | pages [19] -->


<!-- b000676 | prose | pages [19] -->


<!-- b000677 | prose | pages [19] -->


<!-- b000678 | prose | pages [19] -->


<!-- b000679 | prose | pages [19] -->
1 + ϵ −φ −ν −αIn

<!-- b000680 | prose | pages [19] -->
∂f/∂Pn ∂f/∂In ∂f/∂Hn ∂g/∂Pn ∂g/∂In ∂g/∂Hn

<!-- b000681 | prose | pages [19] -->
J =

<!-- b000682 | prose | pages [19] -->
=

<!-- b000683 | prose | pages [19] -->


<!-- b000684 | prose | pages [19] -->


<!-- b000685 | prose | pages [19] -->
∂h/∂Pn ∂h/∂In ∂h/∂Hn

<!-- b000686 | prose | pages [19] -->
−αPn ϵ 1 + ϵ −γ −β + αPn αIn 0

<!-- b000687 | prose | pages [19] -->
. (19)

<!-- b000688 | prose | pages [19] -->
1 −φ ν β

<!-- b000689 | furniture | pages [20] -->
Team #40764

<!-- b000690 | prose | pages [20] -->
The determinant and trace of J are

<!-- b000691 | furniture | pages [20] -->
Page 20 of 25

<!-- b000692 | prose | pages [20] -->
tr(J) = −β −γ −ν + αPn −αIn + 2ϵ −2φ + 3,

<!-- b000693 | prose | pages [20] -->
and

<!-- b000694 | prose | pages [20] -->
(20)

<!-- b000695 | prose | pages [20] -->
det(J) = (1−φ)[(−β−γ+αPn+ϵ+1)(−ν−αIn+ϵ−φ+1)+α2PnIn]+ϵ(βν+γν−ν−ανPn+αβIn−νϵ)

<!-- b000696 | prose | pages [20] -->
(21) respectively. To analyse Case 6, we set In = 0 and ϵ = φ . Simplifying (20) and (21) based on this gives

<!-- b000697 | prose | pages [20] -->
tr(J) = −β −γ −ν + αPn + 3,

<!-- b000698 | prose | pages [20] -->
and

<!-- b000699 | prose | pages [20] -->
(22)

<!-- b000700 | prose | pages [20] -->
det(J) = (β + γ −1 −αPn −φ)(1 −φ −ν).

<!-- b000701 | prose | pages [20] -->
(23)

<!-- b000702 | prose | pages [20] -->
Substituting these into the jury condition (18) gives a condition on the parameters that give a stable solution at the ﬁxed point,

<!-- b000703 | prose | pages [20] -->
−β −γ −ν + αPn + 3 < (β + γ −1 −αPn −φ)(1 −φ −ν) + 1 < 2.

<!-- b000704 | prose | pages [20] -->
(24)

<!-- b000705 | prose | pages [20] -->
As β, γ, ν ≤1, we have tr(J) ≥0. Hence, we can neglect the absolute value signs in (24). As shown in Table 21, there are two equations that specify the three states, In = 0, and φHn = νPn. This gives us one degree of freedom to specify one other parameter to close the system. Crucially, a closed system is only possible if the third equation in the system relates φ and ν. As the death rate of healthy people φ is constant, we must select ν as the independent variable. Rearranging Equation (24) to derive a constraint on ν gives

<!-- b000706 | prose | pages [20] -->
ν > M(1 −φ) −1

<!-- b000707 | prose | pages [20] -->
M

<!-- b000708 | prose | pages [20] -->
where

<!-- b000709 | prose | pages [20] -->
= 1 −φ −1

<!-- b000710 | prose | pages [20] -->
M , (25)

<!-- b000711 | prose | pages [20] -->
M = β + γ −1 −αPn −φ.

<!-- b000712 | prose | pages [20] -->
(26)

<!-- b000713 | prose | pages [20] -->
Although the initial analysis of the model requires ϵ = φ, we can replicate the eﬀect of non-constant birth and death rates with a separate assumption on the steady state population,

<!-- b000714 | prose | pages [20] -->
n→∞Pn →∞. lim (27)

<!-- b000715 | prose | pages [20] -->
Equation (27) assumes that the population will eventually approach inﬁnity, as will occur if birth rate is greater than death rate. As the steady state number of infections is zero in this case, there are no deaths due to Ebola, so the assumption is valid if the birth and death rates are assumed constant. We therefore have

<!-- b000716 | prose | pages [20] -->
1

<!-- b000717 | prose | pages [20] -->
lim

<!-- b000718 | prose | pages [20] -->
M =

<!-- b000719 | prose | pages [20] -->
n→∞

<!-- b000720 | prose | pages [20] -->
1

<!-- b000721 | prose | pages [20] -->
lim

<!-- b000722 | prose | pages [20] -->
M = 0.

<!-- b000723 | prose | pages [20] -->
(28)

<!-- b000724 | prose | pages [20] -->
Pn→∞

<!-- b000725 | prose | pages [20] -->
We therefore conclude that the condition that must be satisﬁed to produce a stable solution at the

<!-- b000726 | prose | pages [20] -->
ﬁxed point of Case 6 is

<!-- b000727 | prose | pages [20] -->
ν > 1 −φ.

<!-- b000728 | prose | pages [20] -->
(29)

<!-- b000729 | prose | pages [20] -->
As this condition does not contain α, β, or γ, we reach the important conclusion that vaccination is the only way to ensure that Ebola is eradicated in the long-term. This assertion suggests that a vaccine must be developed for us to be sure that the Ebola outbreak in West Africa can be controlled.

<!-- b000730 | furniture | pages [21] -->
Team #40764

<!-- b000731 | furniture | pages [21] -->
Page 21 of 25

<!-- b000732 | prose | pages [21] -->
5

<!-- b000733 | heading | pages [21] -->
Summary of Mathematical Modelling

<!-- b000734 | prose | pages [21] -->
5.1

<!-- b000735 | heading | pages [21] -->
Strengths and Weaknesses

<!-- b000736 | prose | pages [21] -->
Strengths and weaknesses of our approach that become apparent during the solution process are summarised below:

<!-- b000737 | heading | pages [21] -->
Strengths

<!-- b000738 | prose | pages [21] -->
Our model...

<!-- b000739 | prose | pages [21] -->
• is based on realistic mechanism of disease transfer

<!-- b000740 | prose | pages [21] -->
• uses parameters that are based on empirical evidence

<!-- b000741 | prose | pages [21] -->
• enables predictions of the evolution of the disease over any length of time

<!-- b000742 | prose | pages [21] -->
• enables full accounting for the number of each transition and number of people in each state at any time

<!-- b000743 | prose | pages [21] -->
• accurately predicts known trends in the outbreak in diﬀerent regions, and accurate predictions are achieved with physically realistic values for the parameters

<!-- b000744 | prose | pages [21] -->
• allows independent analysis of three diﬀerent treatment options

<!-- b000745 | prose | pages [21] -->
• enables an analytical solution for the relationships between parameters required to drive Ebola infections to zero

<!-- b000746 | prose | pages [21] -->
• accounts for population growth which is important in long-term forecasts

<!-- b000747 | prose | pages [21] -->
• simulates randomness in the disease spread (which can lead to divergent outcomes)

<!-- b000748 | heading | pages [21] -->
Weaknesses

<!-- b000749 | prose | pages [21] -->
Our model...

<!-- b000750 | prose | pages [21] -->
• relies on parameter estimates that are justiﬁed using anecdotal evidence (in particular K)

<!-- b000751 | prose | pages [21] -->
• is validated against a short period relative to the entire Ebola outbreak

<!-- b000752 | prose | pages [21] -->
• requires good estimates for initial conditions that are not necessarily available from the data

<!-- b000753 | prose | pages [21] -->
• relies heavily on the accuracy of WHO data, which may be underestimated

<!-- b000754 | prose | pages [21] -->
5.2

<!-- b000755 | heading | pages [21] -->
Future Work

<!-- b000756 | prose | pages [21] -->
The modelling framework used in this analysis provides scope for future enhancement. The following tasks would reduce the assumptions made in this paper, to produce a better model of actual disease transmission:

<!-- b000757 | prose | pages [21] -->
• Obtaining necessary data to model smaller regions than entire nations

<!-- b000758 | prose | pages [21] -->
• Allowing the state transition rate parameters to be expressed as functions of time, instead of constant values. This will allow better modelling of how disease treatment changes with time

<!-- b000759 | prose | pages [21] -->
• Applying a cost function to diﬀerent treatment options, then use the sensitivity analysis to determine the most eﬃcient allocation of resources to reduce deaths

<!-- b000760 | prose | pages [21] -->
• Increasing the scope of sensitivity analysis to cover all possible parameter changes

<!-- b000761 | prose | pages [21] -->
• Adding additional states to model the disease life cycle, for example incubation, infectious, recovering, and allowing transmission from deceased people. A disadvantage of adding states is that ﬁxed point analysis becomes more diﬃcult. Adding one extra state doubles the number of ﬁxed points

<!-- b000762 | furniture | pages [22] -->
Team #40764

<!-- b000763 | furniture | pages [22] -->
Page 22 of 25

<!-- b000764 | prose | pages [22] -->
• Increasing the complexity of the model by adding state transitions. For example, a transition from immune to vulnerable can be added to simulate virus mutation, and relaxing the assumption that infection guarantees future immunity. The state transition diagram would look like Figure 7. A disadvantage of this is that the rate parameters for the new transitions are diﬃcult to determine

<!-- b000765 | prose | pages [22] -->
Birth

<!-- b000766 | prose | pages [22] -->
2

<!-- b000767 | prose | pages [22] -->
ε

<!-- b000768 | prose | pages [22] -->
α

<!-- b000769 | prose | pages [22] -->
λ 10

<!-- b000770 | prose | pages [22] -->
Infected

<!-- b000771 | prose | pages [22] -->
6

<!-- b000772 | prose | pages [22] -->
β

<!-- b000773 | prose | pages [22] -->
5

<!-- b000774 | prose | pages [22] -->
γ

<!-- b000775 | prose | pages [22] -->
1

<!-- b000776 | prose | pages [22] -->
ε

<!-- b000777 | prose | pages [22] -->
7

<!-- b000778 | prose | pages [22] -->
Healthy (Vulnerable)

<!-- b000779 | prose | pages [22] -->
3

<!-- b000780 | prose | pages [22] -->
8

<!-- b000781 | prose | pages [22] -->
υ

<!-- b000782 | prose | pages [22] -->
μ

<!-- b000783 | prose | pages [22] -->
9

<!-- b000784 | prose | pages [22] -->
Healthy

<!-- b000785 | prose | pages [22] -->
φ

<!-- b000786 | prose | pages [22] -->
(Immune)

<!-- b000787 | prose | pages [22] -->
4

<!-- b000788 | prose | pages [22] -->
φ

<!-- b000789 | prose | pages [22] -->
Death

<!-- b000790 | caption | pages [22] -->
Figure 7: A possible extension to the general model

<!-- b000791 | prose | pages [22] -->
5.3

<!-- b000792 | heading | pages [22] -->
Conclusion

<!-- b000793 | prose | pages [22] -->
Stochastic and deterministic models of the West African Ebola outbreak are presented. Both models are based on dividing the population into infected people, immune healthy people, and vulnerable healthy people, and assigning parameters to the rate of transition between these states. The numerical value of parameters are validated against WHO data for four regions from 12 November 2014 to 5 February 2015. We then extend the investigation to produce predictions of future spread of the virus under diﬀerent treatment conditions. Short and medium-term numerical predictions are performed using the stochastic model, and an analytical general solution for long-term steady state conditions is performed using the deterministic model. The ﬁndings of these investigations inform recommendations of future treatment strategies. Qualitatively, the key ﬁndings are

<!-- b000794 | prose | pages [22] -->
• The most eﬀective short-term strategy in all countries is producing a large quantity of improved medicine

<!-- b000795 | prose | pages [22] -->
• The most eﬃcient strategy for reducing medium-term deaths is to improve medical services to isolate infected patients

<!-- b000796 | prose | pages [22] -->
• Short-term strategies will be most eﬀective in Sierra Leone and Liberia

<!-- b000797 | prose | pages [22] -->
• Medium-term strategies should target all three countries in the outbreak: Guinea, Sierra Leone, and Liberia

<!-- b000798 | prose | pages [22] -->
• Although vaccination is less eﬀective in the short and medium-term than other treatment methods in all countries, developing a vaccine is the only way to ensure that the virus can be eliminated in the long-term

<!-- b000799 | furniture | pages [23] -->
Team #40764

<!-- b000800 | furniture | pages [23] -->
Page 23 of 25

<!-- b000801 | heading | pages [23] -->
References

<!-- b000802 | references | pages [23] -->
BBC 2015, Ebola: Mapping the outbreak, http://www.bbc.com/news/world-africa-28755033.

<!-- b000803 | references | pages [23] -->
Centers for Disease Control and Prevention 2014, Q&As on Transmission of Ebola Virus Disease,

<!-- b000804 | references | pages [23] -->
http://www.cdc.gov/vhf/ebola/transmission/qas.html.

<!-- b000805 | references | pages [23] -->
CountryMeters 2015, Current world population by country. Population data for every contry as of 2015,

<!-- b000806 | references | pages [23] -->
http://countrymeters.info/.

<!-- b000807 | references | pages [23] -->
De Leenheer, P 2009, Notes on the Jury conditions, http://math.oregonstate.edu/~deleenhp/

<!-- b000808 | references | pages [23] -->
teaching/spring09/MAP4484/notes-jury.pdf.

<!-- b000809 | references | pages [23] -->
Grant, K 2014, Survivors of Ebola outbreak in Nigeria share their stories, http://www.theglobeandmail.

<!-- b000810 | references | pages [23] -->
com/news/national/survivors- of- ebola- outbreak- in- nigeria- share- their- stories/

<!-- b000811 | references | pages [23] -->
article21985268/.

<!-- b000812 | references | pages [23] -->
Meltzer, MI, Atkins, CY, Santibanez, S, Knust, B, Petersen, BW, Ervin, ED, Nichol, ST, Damon, IK,

<!-- b000813 | references | pages [23] -->
and Washington, ML 2015, “Estimating the Future Number of Cases in the Ebola Epidemic – Liberia

<!-- b000814 | references | pages [23] -->
and Sierra Leone, 2014-2015”, MMWR Supplements, vol. 63, pp. 1–13.

<!-- b000815 | references | pages [23] -->
World Health Organisation 2014a, Ebola virus disease, http : / / www . who . int / mediacentre /

<!-- b000816 | references | pages [23] -->
factsheets/fs103/en/.

<!-- b000817 | references | pages [23] -->
World Health Organisation 2014b, Why the Ebola outbreak has been underestimated, http://www.who.

<!-- b000818 | references | pages [23] -->
int/mediacentre/news/ebola/22-august-2014/en/.

<!-- b000819 | references | pages [23] -->
World Health Organisation 2015a, Ebola data and statistics, http://apps.who.int/gho/data/view.

<!-- b000820 | references | pages [23] -->
ebola-sitrep.ebola-summary-latest?lang=en.

<!-- b000821 | references | pages [23] -->
World Health Organisation 2015b, Ebola vaccines, therapies, and diagnostics, http://www.who.int/

<!-- b000822 | references | pages [23] -->
medicines/emp_ebola_q_as/en/.

<!-- b000823 | references | pages [23] -->
Note: All sources accessed between February 5 and February 9 2015

<!-- b000824 | furniture | pages [24] -->
Team #40764

<!-- b000825 | furniture | pages [24] -->
Page 24 of 25

<!-- b000826 | references | pages [24] -->
World Medical Association Letter

<!-- b000827 | references | pages [24] -->
Dear World Medical Association,

<!-- b000828 | references | pages [24] -->
We were interested to hear your recent announcement about the development of new medication to stop

<!-- b000829 | references | pages [24] -->
Ebola and cure infected patients. This is a welcome and important development in the humanitarian

<!-- b000830 | references | pages [24] -->
ﬁght against the outbreak in West Africa. To assist the distribution of the new medicine, and planning

<!-- b000831 | references | pages [24] -->
future prevention measures, we performed investigations using mathematical modelling. We use two

<!-- b000832 | references | pages [24] -->
methods to simulate the spread of Ebola in Guinea, Liberia, and Sierra Leone. We use these models to

<!-- b000833 | references | pages [24] -->
determine the most suitable country to target in short-term and long-term distribution of the medicine.

<!-- b000834 | references | pages [24] -->
In addition, we analyse diﬀerent treatment options in both short-term and long-term, to determine the

<!-- b000835 | references | pages [24] -->
optimal way for the WMA to direct its future endeavours. We present our ﬁndings in this letter.

<!-- b000836 | references | pages [24] -->
The mathematical model that we have developed is based on data from the World Health Organisation

<!-- b000837 | references | pages [24] -->
(WHO). In our analysis, we simulate the spread of the outbreak from 12 November 2014 to 5 February

<!-- b000838 | references | pages [24] -->
2015 using two methods. We ﬁnd that both methods accurately predict the outbreak when considering

<!-- b000839 | references | pages [24] -->
four regions: Guinea, Liberia, Sierra Leone, and the West African region as a whole. This gives us

<!-- b000840 | references | pages [24] -->
conﬁdence that our model accurate.

<!-- b000841 | references | pages [24] -->
We then run the model forward to produce predictions of the disease spread from February 5 2015

<!-- b000842 | references | pages [24] -->
onwards. A key ﬁnding of the simulation is that the overall current level of treatment is insuﬃcient to

<!-- b000843 | references | pages [24] -->
control the virus in the long-term. If new measures are not implemented, the number of infections will

<!-- b000844 | references | pages [24] -->
increase out of control in approximately eight years time. This ﬁnding is why we are excited to learn

<!-- b000845 | references | pages [24] -->
of a newly developed medicine. We then amend the model to take into account the development of

<!-- b000846 | references | pages [24] -->
new medicine, as well as two alternative methods to mitigate the virus: improving health services, and

<!-- b000847 | references | pages [24] -->
developing and distributing a vaccine.

<!-- b000848 | references | pages [24] -->
Based on the amendments to the original model, we develop short-term (six months), medium-

<!-- b000849 | references | pages [24] -->
term (two years), and long-term recommendations for mitigating the virus. To develop short-term

<!-- b000850 | references | pages [24] -->
recommendations, we simulate the eﬀect of diﬀerent treatment options in each country, and compare

<!-- b000851 | references | pages [24] -->
the results with what would occur if treatment is not improved. After performing the short-term

<!-- b000852 | references | pages [24] -->
simulations, we produce the following recommendations for the quantity and distribution of the new

<!-- b000853 | references | pages [24] -->
medicine:

<!-- b000854 | references | pages [24] -->
• The largest single strategy short-term reduction in deaths is achieved by distributing a large

<!-- b000855 | references | pages [24] -->
quantity of medicine in Liberia, although all nations would substantially beneﬁt from the medicine

<!-- b000856 | references | pages [24] -->
• For a short-term strategy, medicine should be introduced in the highest quantity possible. The

<!-- b000857 | references | pages [24] -->
eﬃciency (deaths per increase in quantity of medicine) of using medicine is greatest when high

<!-- b000858 | references | pages [24] -->
quantities are distributed. This ﬁnding is consistent across all nations, but is especially important

<!-- b000859 | references | pages [24] -->
in Sierra Leone and Liberia

<!-- b000860 | references | pages [24] -->
• For a medium-term strategy, medicine’s eﬃciency does not change signiﬁcantly with the quantity

<!-- b000861 | references | pages [24] -->
distributed. High quantities still result in larger reductions in deaths, but should be subject to

<!-- b000862 | references | pages [24] -->
cost-beneﬁt analysis

<!-- b000863 | references | pages [24] -->
• To maximise death reduction in the medium-term, Liberia is the most important nation to target.

<!-- b000864 | references | pages [24] -->
However, it is also important to distribute high quantities of medicine in Guinea, despite its low

<!-- b000865 | references | pages [24] -->
relative incidence of Ebola

<!-- b000866 | references | pages [24] -->
We also provide the following recommendations regarding treatment methods other than medicine:

<!-- b000867 | references | pages [24] -->
• In the short-term, both improving medical services and vaccinations are less eﬀective in reduce

<!-- b000868 | references | pages [24] -->
deaths from Ebola

<!-- b000869 | references | pages [24] -->
• However, in the medium-term, improving medical services is more eﬃcient than distributing

<!-- b000870 | references | pages [24] -->
medicine, and vaccinations are more competitive

<!-- b000871 | references | pages [24] -->
• In the short to medium-term, Guinea will beneﬁt most from vaccinations.

<!-- b000872 | furniture | pages [25] -->
Team #40764

<!-- b000873 | furniture | pages [25] -->
Page 25 of 25

<!-- b000874 | references | pages [25] -->
• In the short-term, Sierra Leone will beneﬁt most from an improvement in medical services

<!-- b000875 | references | pages [25] -->
• In the long term, the only way to ensure that the Ebola virus is completely eradi-

<!-- b000876 | references | pages [25] -->
cated is by developing and distributing vaccines

<!-- b000877 | references | pages [25] -->
Despite these speciﬁc recommendations, all regions will beneﬁt from any of the treatment methods

<!-- b000878 | references | pages [25] -->
described. Our analysis also neglects the monetary cost of each treatment option. Should further

<!-- b000879 | references | pages [25] -->
information about these recommendations be desired, we can consult with relevant authorities to deter-

<!-- b000880 | references | pages [25] -->
mine the most cost-eﬀective treatment options. Nevertheless, we believe that these recommendations

<!-- b000881 | references | pages [25] -->
represent the most eﬃcient way to implement medicine and other strategies to reduce the overall

<!-- b000882 | references | pages [25] -->
number of deaths from Ebola. We hope that they will prove useful in the ongoing quest to reduce the

<!-- b000883 | references | pages [25] -->
eﬀects of Ebola.

<!-- b000884 | references | pages [25] -->
Yours sincerely,

<!-- b000885 | furniture | pages [25] -->
Team #40764
