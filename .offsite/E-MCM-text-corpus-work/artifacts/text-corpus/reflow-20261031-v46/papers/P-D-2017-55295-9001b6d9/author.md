For ofﬁce use only For ofﬁce use only

T1 F1

T2 F2 Problem Chosen T3 F3

T4 F4

Mathematical Contest in Modeling (MCM/ICM) Summary Sheet

Summary

In order to improve the performance of airport security check while preserving the same security standards, we model and reﬁne this process. We run extensive simulations to analyze performance of our model. Speciﬁcally,

For task (a), we model the airport security process with a queueing network. We get the parameters of the queueing network model by ﬁtting the data in the provided data sheet to different distributions. We validate our model by simulating it with the real world parameter combination and comparing its output against data collected from airport passengers. We identify three bottlenecks in our model: lack of sufﬁcient ID check points; exclusive assignment of screening check points to passengers; the presence of suspicious passengers.

For task (b), we propose three routing algorithms to optimize the throughput and variance of the airport: greedy algorithm, backpressure algorithm, and drift-plus-penalty algorithm. The best one of these algorithms achieves high throughput that is close to optimal and relatively low variance in waiting time. Besides, our proposed routing al- gorithm manages to retain passenger satisfaction while scheduling. We also explore the optimal ratio of different kinds of check points and test the robustness of modiﬁed mod- els.

For task (c), we analyze the impact of different cultures and traveler types and run simulation to see the reaction of our model. The cultures we analyze are collectivist cul- tures, individualist cultures. The types of travelers we analyze are family-based travelers and tech-based travelers. We also propose accommodations to these special situations.

For task (d), we propose both globally applicable and locally applicable policies to airport security managers. Our policies are based on our analysis of different cultures and types of travelers as well as our analysis of our routing algorithms.

Summary

In order to improve the performance of airport security check while preserving the same security standards, we model and reﬁne this process. We run extensive simulations to analyze performance of our model. Speciﬁcally,

For task (a), we model the airport security process with a queueing network. We get the parameters of the queueing network model by ﬁtting the data in the provided data sheet to different distributions. We validate our model by simulating it with the real world parameter combination and comparing its output against data collected from airport passengers. We identify three bottlenecks in our model: lack of sufﬁcient ID check points; exclusive assignment of screening check points to passengers; the presence of suspicious passengers.

For task (b), we propose three routing algorithms to optimize the throughput and variance of the airport: greedy algorithm, backpressure algorithm, and drift-plus-penalty algorithm. The best one of these algorithms achieves high throughput that is close to optimal and relatively low variance in waiting time. Besides, our proposed routing al- gorithm manages to retain passenger satisfaction while scheduling. We also explore the optimal ratio of different kinds of check points and test the robustness of modiﬁed mod- els.

For task (c), we analyze the impact of different cultures and traveler types and run simulation to see the reaction of our model. The cultures we analyze are collectivist cul- tures, individualist cultures. The types of travelers we analyze are family-based travelers and tech-based travelers. We also propose accommodations to these special situations.

For task (d), we propose both globally applicable and locally applicable policies to airport security managers. Our policies are based on our analysis of different cultures and types of travelers as well as our analysis of our routing algorithms.

7 Conclusion

19

7.1 Conclusion of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19

7.2 Policy Proposal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19

7.3 Strength and Weakness of Our Model . . . . . . . . . . . . . . . . . . . . . 19

7.4 Future Application of Models . . . . . . . . . . . . . . . . . . . . . . . . . . 20

1 Introduction

Security has been of ﬁrst priority in transportation activities that involve people since the beginning of the century. A series of time-consuming security check processes are necessary to ensure the security of all passengers aboard. But passengers are complain- ing about waiting for security check in extremely long queues. It is quite challenging to improve the performance of airport security check systems while preserving the current security standards.

In this paper, we try to model this security check process and reﬁne the model. Our main contributions are as follows:

1. We model the security check process with a queueing network. We validate our model by simulating it with real-world parameter combinations and comparing its result with real world data. We identify lack of sufﬁcient ID check points, exclusive assignment of screening check points, presence of suspicious passengers as three bottlenecks in the model.

2. We propose and implement three routing algorithms to optimize our basic mod- el. We simulate our model with these algorithms and analyze their performance.

We ﬁnd that the proposed backpressure algorithm achieves throughput close to optimal and a relatively low variance in waiting time.

3. We analyze the sensitivity of our model by considering the impacts of cultural norms and passenger types. We analyze how the output of our model changes with respect to different norms and passengers, and propose accommodations to these situations.

2 Basic Analysis of the problem

2.1 Single Queueing Nodes

M/G/1 Queue: We adopt M/G/1 queue[1](shown in Figure 1(a)) in our model.

• M: the arrival times of the passengers follow a Poisson distribution

• G: the service times follow an arbitrary probability distribution

• 1: there is only one check point available

The arrivals are determined by a Poisson process with rate parameter µ. Job service time has a normal distribution with parameter µ and σ.

M/G/c Queue: We also adopt M/G/c queue(shown in Figure 1(b)) in our model, which is a generalization of the M/G/1 queue. c represents the number of check points. The arrival time of passengers follows a Poisson distribution with rate parameter λ. Job service time follows a normal distribution with parameter µ and σ.

FIFO: The queue obeys a ﬁrst-come, ﬁrst-served discipline. A single check point serves customers one at a time from the front of the queue. When the service is complete, 1

2 λ λ 3 Poisson μ Poisson arrivals arrivals Exponentially distributed service time c Exponentially distributed μ service time (a) M/G/1

(b) M/G/c

the customer leaves the queue and the number of customers in the system reduces by one.

2.2 Parameter Settings

Before the simulation, we set basic parameters of the probability distribution in queue- ing node based on the data in the data sheet. We use the EstimatedDistribution function of Mathematica to determine probability distributions and estimate parame- ters. The average interval for the arrival time of regular and pre-check passengers fol- 1 1 lows exponential distribution with parameter λ1 and λ2 respectively. And the average rate of ID check service in zone A and baggage and body screening follow normal dis- tribution with parameters (µ1, σ1) and (µ2, σ2). Besides, we assume the time for regular passengers to remove shoes, belts, light jackets and computers from their bags follows a normal distribution with the parameters (µ4, σ4). Thus the average rate of baggage and body screening for regular customer follows normal distribution with parameters p σ2 2 + σ2 (µ3, σ3), where µ3 = µ2 + µ4 and σ3 = 4. The normal distribution (µ3, σ3) and the normal distribution (µ4, σ4) are independent to each other. The speciﬁc numbers are in Table 1.

Symbol Deﬁnition value λ1 4.63476 Rate of regular passenger arrivals λ2 6.52921 Rate of pre-check passenger arrivals (µ1, σ1) (0.186875, 0.0612029) Mean and variance of ID check service time Mean and variance of screening service time (µ2, σ2) (0.507639, 0.158551) for pre-check passengers Mean and variance of screening service time (µ3, σ3) (2.507639, 0.524536) for regular passengers

Times Times Times Times 2.5 3.0 6 6 2.0 2.5 5 5 2.0 4 4 1.5 1.5 3 3 1.0 1.0 2 2 0.5 0.5 1 1 1.4 Arrving time interval(min) 0.6 Arrving time interval(min) 0.0 0 1.0 Service time(min) 0.4 Service time(min) 0.0 0 0.2 0.4 0.6 0.8 1.0 1.2 0.1 0.2 0.3 0.4 0.5 0.4 0.6 0.8 0.1 0.2 0.3

The distribution of service time in different check points s not identical in real life. In order to simulate the differences among check points, we keep the variance of normal distribution σk unchanged(k = 1, 2, 3), and uniformly generate µki of normal distribu- tion between µk −σk and µk + σk.

2.3 Rate Stability

Due to the cost of hiring employees and maintaining the machine, it is impossible for airport to set up inﬁnite check points. But the airport makes sure that the number of check points satisﬁes the need of passengers and the number of passengers waiting in queue will not grow larger over time.

Let Q (t) represent the contents of a single queueing node deﬁned at time slots t ∈ {0, 1, 2, ...}. Q (t) is a stochastic process according to probability law. A queueing node E{|Q(t)|} is rate stable[2] if limt→∞ = 0. Rate stability ensures the queue will not keep t growing over time. a (t) represents the number of new passengers that arrive on slot t and b (t) represents the number of passengers the check point of the queue can serve on slot t . Q (t) is rate stable if

t−1 1 X [a (τ) −b (τ)] ≤0. lim supt→∞ t τ=0

We stipulate that the number of check points satisﬁes rate stability while the ratio of check points between the regular and pre-check passengers is 3 : 1. Therefore we set the number of check points as shown in Table 2.

zone regular pre-check 3 1 ID check(zone A) 12 4 Screening(zone B)

2.4 Measures of Performance

Throughput and variance of average waiting time are two main measures in the se- curity check system. They are deﬁned as follows.

Throughput: The average number of passengers that pass the security check system in per unit time. The per unit time here is set as minute.

Variance: Suppose the waiting time for regular passenger is X1 and the waiting time for pre-check passenger is X2. The percentage of regular passengers is p. The variance of system is deﬁned as

h (X1 −E (X1))2i h (X2 −E (X2))2i pE + (1 −p) E

Throughput measures the security check system’s capacity on a collective level while variance of waiting time measures the fairness on an individual level.

3 Models

In this section, we ﬁrst present our models in details. The ﬁrst model is an optimal but unpractical model, which serves as a comparison and aims to provide modiﬁcation insights. The second one models the queueing networks of real security checking system in an airport.

Symbol Deﬁnition λ The rate parameter for the exponential distribution µ The mean value parameter for the normal distribution σ The rate parameter(squared scale) for the normal distribution N The number of check points Q(c) The backlogs at queueing node a for passenger c at time t a (t) The transmitting rate from queueing node a and queueing node b for µ(c) ab (t) passenger c at time t L(t) The Lyanpnov function at time t ∆(t) The Lyanpnov drift at time t V The control parameter in drift-plus-penalty algorithm

3.1 Tandem M/G/c Queueing Model

We ﬁrst present an ideal model, the tandem M/G/c model. This model realizes the maximum throughput but is not feasible in the real life. We will later compare the per- formance of this ideal model with that of practical model to evaluate the latter and make modiﬁcation.

As Figure 3 demonstrates, two M/G/c queues are in a tandem array. The ﬁrst M/G/c queueing node denotes the queues of ID check(Zone A) and there are NA check points. Similarly, the second M/G/c queue denotes the queues of baggage and body screen- ing(Zone B) and there are NB check points. All check points are accessible to both reg- ular passengers and pre-check passengers and the only difference is that the pre-check passengers are likely to spend less time at Zone B.

Screening Check ID Check

λ1+λ2 Poisson arrivals

μ 2，σ 2    Regular Pax μ 1，σ 1 μ 3，σ 3  Pre-check Pax Normal distributed service time Tandem M/G/c queueing model achieves the optimal performance. All check points in the same zone are busy as long as there are passengers waiting in queue. As for other models, a check point in one queueing node is idle when passengers are waiting before the line in another queueing node when a zone have more than one queueing node. In this way, tandem M/G/c model avoids unnecessary waiting time and attain the maximum throughput.

However, tandem M/G/c model is unpractical. For one thing, the single queue at ev- ery zone can be extremely long, which is hard to keep order. For another, access to every check points for both regular passengers and pre-check customers is feasible. Particular- ly, screening check points at zone B have different check process for these two kinds of passengers and it’s impossible to mix two process together.

Therefore, tandem M/G/c model has achieved maximum throughput but is unprac- tical in real life. This model is used for comparison with real-life model and provide insights for modiﬁcations later.

3.2 Queueing Network Model

Now we introduce queueing network model which models the security check in real- life airports. Queueing networks are systems in which a number of queues are connected by customer routing. Similar to BCMP networks[3], our queueing network models are open networks with very general service time which follows the normal distribution.

The queueing network in real-life airport is illustrated in Figure 4. Every queueing node is an M/G/1 queueing, for there is one queue for every check point. Regular pas- sengers and pre-check passengers are separate from each other in the entire process of security check. Every queueing node at zone A directs to its corresponding queueing nodes at zone B. We use NA1 and NA2 to denotes the number of queueing node in Zone A for regular passengers and pre-check passengers respectively and use NB1 and NB2 to denotes the number of queueing node in Zone B for regular passengers and pre-check passengers respectively.

ID Check Screening Check

Regular Pax

NB1 NA1 NA2 NB2 Pre-check Pax

We will later modify the topology of queueing networks and apply different routing algorithms in queueing networks to achieve larger throughput and smaller variance in the queueing system.

4 Simulations and Bottleneck Detection

4.1 Simulation Setup

We run massive simulations on the queueing network model using the data from the real airports to validate the queueing network model.

We simulate both the tandem M/G/c network and queueing networks model. The simulation data is generated based on the probability distribution that we obtain from the data sheet. We set 1000 people to pass the system in every simulation and collect statistics of length of the queue, throughput, average, and variance of waiting time.

We also consider the presence of suspicious passengers in the security check system 1 in simulation. Every suspicious passenger appears with a probability of 1000 and the queue will be stuck for 10 min. We test the robustness of queueing system by adding the presence of suspicious passengers.

4.2 Validating Our Model

To validate our model, we simulate the model using real-world parameter combina- tions and compare the result with real-world data provided by airport passengers.

Speciﬁcally, we get the number of daily passengers of 5 biggest airports in the US from their ofﬁcial website [4][5][6][7][8]. We then assume that the arrival time of pas- sengers follow the Poisson distribution, and therefore we can calculate the mean arrival rate of passengers by dividing the total number of passengers with the time length of a day. Besides, we get the mean waiting time of passengers from [9]. Other parameters are set after the Bangkok International Airport, which is shown in Figure 5. After that, we simulate our model using the corresponding arrival time distribution. The result of our simulation is shown in Table 4.

average waiting daily average waiting time calculated Airport arrival time from by passengers websites(minute) model(minute) Chicago O’Hare 40 −60 2, 000, 000 79.0155 International(ORD) Hartsﬁeld-Jackson Atlanta 10 −20 260, 000 42.9196 International(ATL) Los Angeles 20 −30 32.5824 205,000 International(LAX) John F. Kennedy 10 −20 156, 000 16.8958 International(JFK) San Francisco 1 −10 9.4987 137,000 International(SFO)

We can see from Table 4 that the resulting average waiting time of our model is gen- erally close to the real average waiting time and thus our model is valid in real life. The discrepancy between the model output and the ground truth can be explained as fol- lows. The number of check points of our model is far less than that of the real case. Since the real number of check points is unavailable online, so we have to estimate the num- ber from the fact that the waiting queue of clients is at least rate stable(as is discussed in section 2.3). That is, λ ≤c · µ, where λ is the arrival time, µ is the service rate(estimated from Excel data), and c is the number of check points. c obtained in this way is very like- ly to be far smaller than the real number of check points since real airports deploy more check points to deal with large number of passengers. In all, the inaccurate estimation of number of check points contributes to the discrepancy.

4.3 Simulation Evaluation

We now evaluate the simulation results given the parameters in our problem and analyze the bottleneck in current security check system.

The lack of sufﬁcient ID check points for pre-check passengers is a bottleneck in the queueing network model. From section 3.2, we see that the length of ID check queue for pre-check passengers grows quickly. However, the high speed of screening check point for pre-check passengers keeps the average waiting time for pre-check passengers much smaller than that of regular passengers. The imbalanced allocation of resource incurs congestion in the security system for pre-check users. Deploying one more ID check point for pre-check passengers, which is an effective but luxurious solution to the limit of ID check point, may not meet the approval due to the heavy cost.

The exclusive assignment of screening check points to some speciﬁc group of pas- sengers is another bottleneck. In this model, every ID check point only connects to 4 screening check points for the convenience of managing passengers and these 4 check points are exclusively used by passengers from the previous ID check point. In section 3.2, 4 screening queues from the same ID check points for regular passengers suffer from long queue while screening queues from other ID check points have much shorter queue.

Since the service time is not identical for every check point, a passenger from fast ID check points is possible to be directed to slow screening check points. In consequence, there might be certain screening check points suffering from long waiting queues and the separation of screening check points for regular customers results in the waste of resource.

PreIDQ0 RegScreenQ02 80 RegIDQ0 RegScreenQ03 Number of PAXin queue RegIDQ1 RegScreenQ10 60 RegIDQ2 RegScreenQ11 PreScreenQ00 RegScreenQ12 40 PreScreenQ01 RegScreenQ13 PreScreenQ02 RegScreenQ20 20

PreScreenQ03 RegScreenQ21 0 RegScreenQ00 RegScreenQ22 0 50 100 150 RegScreenQ01 RegScreenQ23 Time/min

Maxnumber of PAXin a queue 80 20 Number of PAXin queue 60 15 40

ID Check Queue

10 Screening Check Queue 20 5

0 0 0 50 100 150 200 0 20 40 60 80 100 120 Time/min Time/min

M/G/c Queueing Model Suspicious Passenger

The presence of suspicious passengers is the third bottleneck of this model. After analyzing Figure 6 and 7, the outline of 6 is the maximum number of passengers in a queue without the presence of suspicious people. Contrasting the Figure 7 with the outline of Figure 6, there is a suspicious passenger showing up at 88 minutes, which results in the rising slope increases for 15 minutes, and the maximum value is larger. At 152 minutes, another suspicious passenger arrives, which results in the maximum number of a queue keeping for 10 minutes instead of decreasing as in Figure 6. By comparing the ﬁgures, we ﬁnd that the presence of suspicious passengers will inﬂuence the stability of the system. In the airport, the suspicious passengers are more likely to be detected when the security check is strict especially in festivals or after certain events. So the inﬂuence of suspicious passengers should be considered as one of the bottlenecks of queueing network model.

These bottleneck of queueing networks model all result from the plain structure of security check system and oversimple queueing rules. In Figure 8, passengers wait in front of every queue node during the whole process and thus all the check points are working all the time. The results of tandem M/G/1 network model in Figure 8 show that the balance of all the queueing system enables the system to make full use of resource.

We will modify the security checking system to achieve a more efﬁcient use of resources in the next section.

5 Modiﬁcations to the Process

In this section we will introduce modiﬁcations for the bottleneck detected in the pre- vious section. We implement different routing algorithms and optimize the ratio of two kinds of passengers in order to achieve larger throughput and smaller variance.

5.1 Greedy Routing Based on Backlogs

We allow the queueing nodes to direct to more queueing nodes in this section. Pre- vious model have bottleneck where the queueing nodes corresponding to one node are busy and queueing nodes corresponding to another node are idle. Enabling passengers to make choice among more check points will make better use of the resource of check points by avoiding wastes. As Figure 9 demonstrated, both kinds of passengers are still prohibited to enter the check points of each for the privilege of the pre-check passenger- s, but all check points in zone B are accessible to passengers from the check point for passengers of the same kind in zone A.

Screening Check ID Check

Regular Pax

NB1 NA1 NA2 NB2

Pre-check Pax

We apply greedy routing based on the backlogs of the queueing node. The amount of total passengers waiting in queue nodes n are denoted as the backlog Qn (t). Every passenger makes the locally optimal choice of choosing the queueing node with the least queue backlog.

The results are illustrated in the Figure 10. The greedy algorithm achieves a much smaller queue size of less then 16 compared to the original model in section 3.2. Also, the total time required for all passengers to pass the line is much less. The throughput RegScreen7 RegID0 15 RegScreen8 RegID1 Number of PAXin queue RegScreen9 RegID2 10 RegScreen10 RegScreen0 RegScreen11 RegScreen1 PreID0 RegScreen2 5 PreScreen0 RegScreen3 PreScreen1 RegScreen4 PreScreen2 0 RegScreen5 0 20 40 60 80 100 120 PreScreen3 RegScreen6 Time/min

is 7.148PAX/min and the variance of waiting time is 103.427min2 The queueing system in greedy algorithm has better performance than the original model.

5.2 Lyapunov Drift and Backpressure-Based Routing

5.2.1 Lyapunov Optimization for Queueing Networks

Consider a queueing network with N queueing nodes in discrete time slots t in {0, 1, 2, ...}. On each slot, routing and transmission scheduling decisions are made in an effort to deliver passenger to destination. Let Q(c) n (t), where c can be both regular and pre-check passengers, be the current amount of passenger in node n, also called the queue backlog. The queue backlogs from one slot to the next satisﬁes the following for all n ∈{1, ..., N}, c ∈{regular, pre −check}:

N N " # µ(c) X X Q(c) Q(c) µ(c) an (t) + A(c) n (t + 1) ≤max n (t) − nb (t) , 0 + n (t) a=1 b=1

where A(c) n (t) is the random amount of passengers that exogenously arrives to node n on slot t, and µ(c) ab (t) is the transmission rate allocated to passenger c on link (a, b) on slot t. Note that µ(c) ab (t) may be more than the amount of passengers c that is actually transmitted on link (a, b) on slot t. This is because there may not be enough backlog in node a.

The backpressure algorithm[10] is designed by choosing transmission and routing variables to greedily minimize a bound on the drift of a Lyapunov function. Speciﬁcally, deﬁne Q (t) = Q(c) n (t) as the matrix of current queue backlogs. Deﬁne the Lyapunov function N L (t) = 1 (t)2 . Q(c) X X i 2 c i=1

This fuction is a scalar measure of the total queue backlog in the network. Note that this is a sum of the squares of queue backlogs. Thus the backlogs in every Queues are small if the Lyanpnov function is small. Then the Lyapunov drift is deﬁned as the change in this function from one slot to the next:

∆(t) = E {L (t + 1) −L (t) |Q (t)} .

We intend to minimize the Lyapunov drift so as to minimize the total queue backlog in the network as time goes by.

We transform the equation using the inequality of backlog from one slot to another slot

N N N ( ) Q(c) µ(c) X X X X (t) E λ(c) µ(c) ∆(t) ≤B + an (t) − nb (t) |Q (t) n (t) + , i c n=1 a=1 b=1

  λ(c) where B is a ﬁnite constant and n (t) is passenger arrival rate matrix. Since B and   λ(c) n (t) is constant, we maximize the following terms to minimizing the Lyanpnov drift N N h i µ(c) a (t) −Q(c) X X X Q(c) ab (t) (t) . b c a=1 b=1 The weight Q(c) a (t) −Q(c) (t) is called the current differential backlog of c between nodes b   µ(c) a and b. Thus, we want to choose decision variables ab (t) so as to maximize the above weighted sum, where weights are differential backlogs.

Clearly we should not send data in a direction of negative differential backlog, and so we should choose µ(c) ab (t) = 0 whenever the differential backlog is negative. Further, giv- en µ(c) ab (t) for a particular link (a, b), the optimal µ(c) ab (t) are chosen as follows: ﬁrst ﬁnd copt ab (t) that maximize the differential backlog for link (a, b). If this maximizing differen- tial backlog is negative, assign µ(c) ab (t) = 0 for both kinds of passengers. Else, allocate the full link rate µab (t) to the passengers copt ab (t), and zero rate to the other passengers on this link. With this choice, our aim is to maximize

N N   copt(t) copt(t) X X (t) −Q µabWab (t) (t) , where Wab (t) = max Q (t) ab ab a b a=1 b=1

choosing µ (ab) is called the max-weight algorithm. It maximizes a linear sum of trans- mission rates, where the weights Wab (t) correspond to differential backlogs. The back- pressure algorithm uses the max-weight decisions for µab (t), and then chooses routing   µ(c) ab (t) variables via the maximum differential backlog as described above.

5.2.2 The Performance of Backpressure Routing

Now we apply the backpressure routing to the queueing network model. The trans- mitting rate µ(c) ab (t) has an inverse relationship with the current serving time of queueing node a. Except the rules in 5.2.1, pre-check passengers are able to queue before the check points for regular passengers. However, they receive the same check process and spend the same time as the regular passengers. This assumption is reasonable, for pre-check passengers have rights to go to regular check points when their own check points are too busy. The diagram of the queueing network is illustrated in Figure 11.

ID Check Screening Check

Regular Pax

Pre-check Pax

10 in greedy routing, the longest queue is the same. Although more queues are likely to have the long queues, this result from shorter service time of these check point. The graph also shows that it takes less time for all passengers to pass the security check The throughput is 7.328PAX/min, which is closer to systems than greedy routing. 7.673PAX/min of the optimal models than greedy routing. The variance of waiting time is 84.971min2, smaller than that of greedy routing.

14 IDCheck0 ScreenCheck6 IDCheck1 ScreenCheck7 12 Number of PAXin queue IDCheck2 ScreenCheck8 10 IDCheck3 ScreenCheck9 8 ScreenCheck0 ScreenCheck10 6 ScreenCheck1 ScreenCheck11 4 ScreenCheck2 ScreenCheck12 2 ScreenCheck3 ScreenCheck13 0 ScreenCheck4 ScreenCheck14 0 20 40 60 80 100 120 ScreenCheck5 ScreenCheck15 Time/min

The robustness of the queueing networks improves when suspicious passengers pass the system. As illustrated in Figure 13a, where the dash line denotes the arrival of the suspicious passengers, the longest line is almost the same as the outline of Figure 12 and the queueing networks are rather stable. The queueing network is almost immune to the suspicious passengers.

We also explore the optimal ratio between regular and pre-check passengers(Figure 14). We adjust the ratio of check points in zone B, where exists most of the long queues and we have 16 check points in the zone B. The throughput increases sharply at ﬁrst and then ﬂuctuates around 7.3 while the variance of average waiting time goes directly down with the increase of check points for regular passengers. 13 check points for regular passengers is a proper choice for the queueing system in backpressure algorithm, for it maintains a relatively small variance as well as the largest throughput.

20 20 Maxnumber of PAXin a queue Maxnumber of PAXin a queue 15 15

10 10

5 5

0 0 0 20 40 60 80 100 120 140 0 50 100 150 Time/min Time/min

(a) Backpressure Routing (b) Drift-Plus-Penalty Algorithm

Suspicious Passengers)

7.6 250 7.4 Throughput PAX/min 200 7.2 Variance/min 2 7.0 150 6.8 100 6.6 50 6.4 0 6.2 0 2 4 6 8 10 12 14 0 2 4 6 8 10 12 14 Number of TSA regular check points Number of TSA regular check points

Check Points(16 Check Points in total)

5.3 Drift-Plus-Penalty Algorithm

5.3.1 Drift-Plus-Penalty

We intend to reduce the number of pre-check passengers to enter the check points compared to the previous routing algorithm under the same rule. Previous routing algo- rithm requires the pre-check passengers to enter the check points for regular customers to achieve larger throughput and smaller variance. Since the pre-check passengers pay extra money for better-service, they may be reluctant to receive the security check like the regular customers. Therefore, we improve the previous routing algorithm.

V penalty (t) term is introduced to the Lyapunov drift in the previous backpressure routing. Instead of taking a control action to minimize a bound on ∆(t), we minimize a bound the following drift-plus-penalty expression:

∆(t) + V E {penalty (t)}

where V ≥0 is a parameter that represents an “importance weight” on how much we emphasize to reduce the number of the pre-check passengers to enter the check point for regular passengers.

In the same way that minimizing a bound on ∆(t) leads to an expression ∆(t) ≤B, minimizing a bound on the drift-plus-penalty leads to an expression of the form:

∆(t) + V E {penalty (t)} ≤B + V p∗,

where p∗is the optimal time average penalty.

5.3.2 The Performance of Drift-Plus-Penalty Algorithm

We apply the drift-plus-penalty algorithm in the problem. Let V = 0.5 and penalty (t) =   −Q(c) 1 t(c)   Qa (t) when we transmit pre-check passengers from queueing node a to b 2 queueing node b.

The results of drift-plus-penalty algorithm are demonstrate in Figure 15. The back- logs are larger than the backpressure routing as some queue reach over 14 and the largest backlog attain 20. Also, it takes more time for all passengers to pass the security check. The throughput of the system is 7.224PAX/min and the variance of waiting time is 149.880min2, both of the result are worse off compared to the backpressure routing. This algorithm sacriﬁce the throughput and variance of waiting time to maintain the right of pre-check users.

20 IDCheck0 ScreenCheck6 IDCheck1 ScreenCheck7 Number of PAXin queue 15 IDCheck2 ScreenCheck8 IDCheck3 ScreenCheck9 10 ScreenCheck0 ScreenCheck10 ScreenCheck1 ScreenCheck11 5 ScreenCheck2 ScreenCheck12 ScreenCheck3 ScreenCheck13 0 ScreenCheck4 ScreenCheck14 0 20 40 60 80 100 120 140 ScreenCheck5 ScreenCheck15 Time/min

We also look into the robustness of the queueing networks when suspicious passen- gers enter security check system. Figure 13b illustrates the longest queue in the security check system and the dash line means the time when the suspicious passengers pass. Only a small increase in slope shows up in Figure 13b compared to the outline of Figure 15 and the increase diminishes quickly in less than 5 minutes. This means the queue length of are less susceptible to this kind of emergency case.

We explore the optimal ratio between regular and pre-check passengers(Figure 16). As most long queues exist in zone B, we intend to adjust the ratio of check points in zone B. Suppose we have 16 check points in the zone B. The throughput increases sharply at ﬁrst and then ﬂuctuates around 7.2 while the variance of average waiting time goes directly down with the increase of check points for regular passengers. We choose 11 check points for regular passengers, which lead to a relatively small variance as well as a large throughput.

6 Sensitivity Analysis

We perform sensitivity analysis on our model by considering the cultural impacts on the parameters. More speciﬁcally, we examine several different cultural norms and model them as changes to input parameters of our model. Then we are able to tell the exact impacts of different cultural norms by comparing the performance metrics of our 7.5 300 Throughput (PAX/min) 250 Variance/min 2 7.0 200

150 6.5 100

50 6.0 0 0 2 4 6 8 10 12 14 0 2 4 6 8 10 12 14 Number of TSA regular check points Number of TSA regular check points

Check Points(16 Check Points in total)

model under different parameter combinations.

6.1 Modeling Different Situations

We will present the modeling of four different situations(including those in different cultural norms and different types of traveler) in this section. The evaluation of the impacts of these situations will be provided in section 6.2. The accommodation to these situations will be provided in section 6.3.

6.1.1 Collectivist Cultural Norms

Switzerland is a country whose Power Distance Index(PDI), an indicator that ex- presses the public’s general acceptance towards inequalities, is lower than that of most countries [11]. Believing that inequalities among people should be minimized, Swiss people tend to prioritize collective efﬁciency, which motivates us to model their willing- ness to sacriﬁce personal gains for the good of the public.

We change the control parameter V of the drift-plus-penalty model to describe such willingness. As is discussed in section 5.3.1, V stands for the penalty of scheduling a pre-check passenger to regular check points, a decision that will improve the global throughput and variance but cost the pre-check passenger more time. A passenger from collectivist cultures(as those in Switzerland) may readily follow the schedule and thus has a small control parameter.

6.1.2 Individualist Cultural Norms

In contrast to what was believed by Chinese a thousand years ago, individual efﬁ- ciency is the dominating factor in the code of conduct of Chinese today. The act of cutting in line, carried out by those who desperately seek individual efﬁciency, can be observed in some airports in China. This leads us to model the act of skipping by adding new queueing rules to our model.

As is shown in section 2.1 ,our model naturally supports the ﬁrst-in-ﬁrst-out queue- ing rule. To model the skipping acts, a new passenger can now go to the head of the queue. The probability of a passenger going to the head of a queue is 30%, a value estimated from daily life experience.

6.1.3 Family-based Travelers

Familial relationships are cherished in almost all cultures. Flying with family mem- bers to some fascinating destinations is a good choice of spending vacations as well as enhancing family ties. This traveling situation motivates us to model the family-based travelers with different passenger arrival distribution.

In the previous discussion, we have mentioned that our model assumes the arriving passengers are a Poisson ﬂow(section 2.1). The family-based travelers do not follow the Poisson distribution since they arrive at the same time, which is a safe assumption. Also, we assume that family-based travelers from the same family will process through the same check point and that they are always consecutive in a queue.

6.1.4 Tech-based Travelers

Our last proposed situation consists of travelers who turn to modern communication technology for an accurate estimation of waiting time. A growing number of airports collect the queueing information in the airport and push estimated waiting time to pas- sengers through mobile apps. In this way, the passengers are aware of the queueing situations and are able to better arrange their trips to the airport. We model this type of travelers using different arrival distribution.

Similar to the situation in section 6.1.3, with a-prior knowledge, the arriving passen- gers do not follow poisson distribution. We therefore model the arrival time of these travelers as a random variable following a normal distribution whose parameters are estimated through life experiences: the mean value of this distribution is 30 minutes be- fore the departure time, and the variance depends on the accuracy of the information provided by the airport.

6.2 Impact of Various Situations

6.2.1 Collectivist Cultural Norms

We change the control parameter from 0.1 to 1.0 and measure the performance met- rics of our model. The result of this experiment is shown in Figure 17.

7.50 1200 Throughput (PAX/min) 7.00 1000 Variance(min 2) 6.50 800 6.00 Variance 600 Throughput 5.50 400 5.00 200 4.50 0 0.0 0.2 0.4 0.6 0.8 1.0 Penalty factor

We can see that the throughput of the system shrinks and that the variance increases as the control parameter grows, which means both the performance and the stability of the system deteriorates if passengers favor individual efﬁciency too much.

6.2.2 Individualist Cultural Norms

We run our model with skipping queueing rule for 10 times and calculate the aver- aged performance metrics. Table 5 shows the variance and the throughput of the cutting- in-line system and the normal system.

Variance(min2) Throughput(PAX/min) Non-cutting 96.024 7.575 Cutting 43.622 7.690

We can see that the system which allows cutting in line has better variance and s- lightly better throughput than the system that does not. This is because cutting in line increases the waiting time of passengers after the person who skips, but does not nec- essarily increase the waiting time of the person who leaves last, and therefore does not necessarily deteriorate throughput.

6.2.3 Family-based Travelers

We add family-based travelers to our model and simulate the model for different percentages of family-based travelers in all passengers. Figure 18 shows the variance and throughput of the system with respect to different ratios.

1200 5 Throughput (PAX/min) 1000 Variance(min 2) 4 800 3 600 Control group 2 400 With family checkpoint 200 1 W/o family checkpoint 0 0 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 Percentage of family PAX Percentage of family PAX

We see from Figure 18 that the family-based travelers hurt the performance metrics of the airport. The more family-based travelers, the more the metrics will deteriorate. To accommodate large number of family-based travelers, a check point that specially designed for them can be deployed. This kind of check points can help improve vari- ance and throughput when the number of family-based travelers is large. We will give detailed explanation for this kind of special check points at section 6.3.

6.2.4 Tech-based Travelers

We simulate our model on different arrival distributions described earlier in sec- tion 6.1.4. Figure 19 illustrates how variance and throughput of our model change with respect to the standard variance of the arrival distribution.

6.40 550 6.20 Throughput (PAX/min) 500 Variance(min 2) 6.00 5.80 450 Variance 5.60 Throughput 400 5.40 5.20 350 5.00 10 12 14 16 18 σ of arrival normal distribution

bution

Basically, Figure 19 tells us that if passengers arrive more intensely in a given time period, then the security check process will have better performance. So if the airport provides more accurate information such that the passengers can correctly estimate their arriving time, the airport will have better throughput and lower variance.

6.3 Accommodation for Situations

In this section, we will provide some accommodations that correspond to the previ- ous situations we have discussed.

1. Collectivist cultural norms: people from collectivist cultures favor collective ef- ﬁciency more. The airport can deploy a scheduling algorithm like that in sec- tion 5.3.1 to optimize global throughput and variance.

2. Individualist cultural norms: for the sake of passenger’s satisfaction, the airport should strictly forbid cutting in line despite its potential help in lower the variance of waiting time.

3. Family-based travelers: deploying a special check point for family members can help. The special check point only serves family-based travelers and mainly focus on the parents when doing identiﬁcation check, which implies shorter service time for the whole family. Figure 18 shows that this special check point helps improve throughput and variance.

4. Tech-based travelers: the airport should encourage the passengers to use the mo- bile app that provides information about queueing in the airport. The airport should also try to collect as accurate data as possible to help passengers better estimate their arriving time.

7 Conclusion

7.1 Conclusion of the Problem

We model the problem as a queueing network and identify lack of sufﬁcient ID check points, exclusive assignment of screening check points, presence of suspicious passen- gers as three bottlenecks of the system. We reﬁne the model by applying greedy routing algorithm, backpressure algorithm, drift-plus-penalty algorithm to optimize passenger scheduling process. We implement and simulate our model and ﬁnd that the backpres- sure algorithm is close to optimal scheduling and is practical in real airports. We also explore the optimal ratio of different kinds of check points and test the robustness of modiﬁed models. We perform sensitivity analysis of our model by considering the im- pacts of different cultural norms and different types of travelers. We also propose several policies that may help airports deal with the inﬂow of passengers in various situations.

7.2 Policy Proposal

We propose the following policies:

1. Globally applicable:

(a) Deploy backpressure algorithm discussed in section 5.3.1 to optimize passen- ger scheduling.

(b) Push accurate airport queueing information to passengers through mobile apps.

(c) Strictly forbid cutting in line for the sake of passengers’ satisfaction.

(d) The ratio of pre-check check points and regular check points should be care- fully chosen(based on arriving rate of passengers, the percentage of pre-check passengers, etc).

2. Locally applicable:

(a) Airports in countries inﬂuenced by collectivist cultures can deploy drift-plus- penalty algorithm with small control factor to improve throughput and vari- ance of passengers.

(b) When operate in traveling season, airports can deploy a temporary check point for family-based travelers to enhance throughput and decrease vari- ance.

7.3 Strength and Weakness of Our Model

Strength:

1. Requiring little change to current security check process

2. Achieving throughput of passengers close to optimal

3. Retaining passenger satisfaction while scheduling passengers 4. Consistent good performance regardless of the distribution of arriving times

Weakness:

1. Requiring external intervention to achieve good performance

2. Not taking the distances among check points into consideration

3. Limited performance metrics

4. Using imprecise estimated parameter from a small data set

7.4 Future Application of Models

Our proposed model can also be generalized into ﬁelds like:

1. communication systems: our scheduling algorithm can be used to schedule the transportation of data packets in order to improve throughput and reduce vari- ance.

2. logistics networks: our models correctly reﬂect the queueing process and trans- portation process of logistics networks. The optimization approaches mentioned in our model can also be applied in this ﬁeld.

3. queueing hardware: in hardware systems, several queueing devices may need to compete to use the bus to send their data to destinations. The scheduling algorithm in our model can be used to optimize the throughput and variance of such systems.
