# P-D-2017-68942-f0b0893e

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
1/20/2017 MCM 2017 Summary Sheet for Team 68942 Print This Page Close This Window x Team Control Number For office use only 68942 For office use only T1 F1 T2 F2 T3 F3 T4 Problem Chosen F4 D 2017 MCM/ICM Summary Sheet (Your team's summary should be included as the first page of your electronic submission.) Type a summary of your results on this page. Do not include the name of your school, advisor, or team members on this page.

<!-- b000002 | prose | pages [1] -->
The objective of our Internal Control Management (ICM) team was to investigate the flow of passengers through American airport checkpoints in light of various airport security controversies. The TSA asked our team to determine bottlenecks in the current security process that impacted passenger throughput and variance in wait times, and to develop modifications that might expedite throughput and decrease variance. We developed an agent-based model using NetLogo to study how passengers move through a typical security checkpoint. Our model divided the current screening process into individual components (processes like document-checking and lines for those processes) to precisely locate potential bottlenecks and included separate components for passengers enrolled in PreCheck, a program that expedites screening for trusted travellers. Travelers and their speeds through certain components of the process were generated probabilistically to most accurately represent real-world unpredictability.

<!-- b000003 | prose | pages [1] -->
We ran the model with different checkpoint configurations and varying traffic volumes. Our model found that for low traffic volumes, overall wait times and variance were low. More importantly, at higher volumes (approx. 3 or less seconds per passenger) there were three significant bottlenecks: the lines for PreCheck and regular document-checking at the start of the checkpoint, and for the body scanners that most regular passengers must pass through. These three components caused over 99% of the variance and length of total wait times, with standard deviation of wait times topping 30 minutes during peak hours.

<!-- b000004 | prose | pages [1] -->
Using the NetLogo model, we studied how certain modifications would impact passenger flow. At higher traffic volumes, throughput was increased by up to 16% by more metal detector use, better officer training for pat-downs, or the addition of a single metal detector or body scanner and the extra body scanner reduced variance by 33%. The model also investigated how throughput and wait times were influenced by passenger behaviors. We found that cutting, opting for pat-downs, and slower walking all impacted the checkpoint negatively, but with less severity than expected.

<!-- b000005 | prose | pages [1] -->
Our model allowed us to closely analyze the efficiency of airport security checkpoints and shed light on how to resolve one of travelling's biggest issues.

<!-- b000006 | furniture | pages [1] -->
https://www.comap.com/undergraduate/contests/mcm/team-summary-sheet.php 1/1

<!-- b000007 | furniture | pages [2] -->
Team 68942

<!-- b000008 | furniture | pages [2] -->
Page 1 of 36

<!-- b000009 | title | pages [2] -->
Optimizing Passenger Throughput at an Airport Security Checkpoint

<!-- b000010 | heading | pages [2] -->
1 Introduction

<!-- b000011 | prose | pages [2] -->
On the morning of September 11, 2001, a series of four coordinated terrorists attacks in New York, Pennsyl- vania, and Virginia killed nearly 3000 people and injured over 6000 others. The insuﬃcient airport security methods at the time allowed terrorists to board and subsequently hijack four passenger airliners. In the aftermath of the attacks, Congress and former President George W. Bush passed the Aviation and Trans- portation Security Act which established the Transportation Security Agency (TSA) as method to prevent similar attacks in the future. The TSA’s mission is to “protect the nation’s transportation systems to ensure freedom of movement for people and commerce” and desires to “provide the most eﬀective transportation security in the most eﬃcient way as a high performing counter-terrorism organization” [11].

<!-- b000012 | prose | pages [2] -->
Since its inception, the TSA has evolved to combat the various threats that terrorists pose to ordinary travelers. The addition of baggage screening, liquids limitations, and millimeter wave body scanners are just some examples of the increased security measures the TSA has implemented over the past decade. However, in 2016, the TSA came under sharp criticism when extremely long lines, particularly at large airports, caused travelers to miss their ﬂights. Furthermore, there have been incidents where travelers experienced unexpected and unpredicted long wait times. This high variance has lead to travelers making the tough choice between arriving at the airport unnecessarily early or potentially missing their ﬂight. As a result, the TSA is facing a tension between maximizing security and minimizing inconvenience travelers. Although the TSA’s PreCheck program, which allows travelers expedite the screening process, has become more popular, the exact eﬀect on traveler throughput is not known.

<!-- b000013 | caption | pages [2] -->
Figure 1: Illustration of the TSA Screening Process

<!-- b000014 | furniture | pages [3] -->
Team 68942

<!-- b000015 | furniture | pages [3] -->
Page 2 of 36

<!-- b000016 | prose | pages [3] -->
Our team has been tasked by the TSA with optimizing the traveler throughput at an airport security checkpoint. Our solution identiﬁes the problems with the current airport security checkpoint, shown above in Figure 4, and proposes a model that improves the checkpoint throughput and reduces variance in wait time while maintaining current safety and security standards.

<!-- b000017 | heading | pages [3] -->
2 Screening Process

<!-- b000018 | prose | pages [3] -->
Airport security checkpoints can be divided into four major zones, as demonstrated in Figure 4.

<!-- b000019 | prose | pages [3] -->
In Zone A, passengers arrive to the checkpoint and wait in a queue until a security oﬃcer can inspect their documents. In Zone B, passengers walk to an available screening lane. There, they unload their belongings for x-ray screening and pass through a millimeter wave body scanner or a walk-through metal detector (WTMD). In Zone C, the passengers collect their belongings from the x-ray conveyor belt and leave the checkpoint. In Zone D, passengers who require additional screening undergo pat-downs and/or baggage searches.

<!-- b000020 | prose | pages [3] -->
We model the checkpoint as a sequence of processes (e.g., passing through a body scanner) and queues (e.g., the line before a body scanner). The amount of time each process takes is set in our model, which queue times depend on the length and nature of the queue. Airports and the TSA wish to minimize the amount of time that passengers spend in any queue. In our model, there are a total of four queues and ten processes in the screening process, not including Zone D. They are, in chronological order:

<!-- b000021 | prose | pages [3] -->
Zone Queue Process Document check line (q0) A Walk to document check Document check Walk to screening lane X-ray screening line (q1) Unload belongings for screening Walk to line Body scanner or B WTMD line (q2) Walk to scanner or WTMD Body scanning or WTMD Walk to collection line Collection line (q3) C Collect belongings Exit

<!-- b000022 | caption | pages [3] -->
Table 1: Breakdown of the screening process

<!-- b000023 | prose | pages [3] -->
If a passenger undergoes additional screening in Zone D, he or she walks to Zone D, waits in a queue for an available security oﬃcer, and then undergoes the screening. In the case of a baggage search, the passenger exits the checkpoint from Zone D. Otherwise, the passenger walks to Zone C to retrieve baggage and then exits.

<!-- b000024 | heading | pages [3] -->
3 Assumptions

<!-- b000025 | prose | pages [3] -->
Real-world It was necessary to make several assumptions in our model:

<!-- b000026 | furniture | pages [4] -->
Team 68942

<!-- b000027 | furniture | pages [4] -->
Page 3 of 36

<!-- b000028 | prose | pages [4] -->
1. Each passenger travels alone. We assume that passengers do not travel in pairs, as families, or in groups; each makes decisions that are dependent on his or her own needs and not the needs of others.

<!-- b000029 | prose | pages [4] -->
2. The given data set is representative of how passengers proceed through the screening process. It is diﬃcult to accurately predict how long each traveler will spend in each zone of the screening process. We assume that the given data closely approximates the movements of most travelers through security checkpoints.

<!-- b000030 | prose | pages [4] -->
3. Arrivals are uniformly random. According to the given data, the arrival times of travelers do not follow any clear pattern within short time periods (Figure 3). Thus, the best way to model arrivals is to generate travelers with a constant probability. The probability itself may vary between regular and Pre-Check arrivals, as well as with total traﬃc volumes.

<!-- b000031 | prose | pages [4] -->
4. Travelers choose the screening lane with the least amount of people. When passing from the document check to the baggage and body screening, people will choose what they perceive to be the most eﬃcient route: the lane with the least number of people.

<!-- b000032 | prose | pages [4] -->
5. The general layout of any US security checkpoint is the same as presented in Figure 4. The TSA sets strict guidelines for the layout, equipment, and dimensions of any airport security checkpoint [12]. Because it is diﬃcult and costly to expand the total space of security checkpoints, we limit the total number of lanes to six, though lanes may be closed during periods of lower traﬃc.

<!-- b000033 | prose | pages [4] -->
Similarly, the number of document-checking security oﬃcers is limited by physical space availability.

<!-- b000034 | prose | pages [4] -->
A typical checkpoint, as depicted in [12], has one document-checking oﬃcer for each body scanner.

<!-- b000035 | prose | pages [4] -->
6. For every two screening lines, there is one metal detector and one millimeter wave body scanner. According to the TSA’s Security Checkpoint Layout Design/Reconﬁguration Guide, the optimal layout for Zone B is two screening lines per metal detector and one metal detector per body scanner whenever possible [12].

<!-- b000036 | prose | pages [4] -->
7. Queues have no limit. At a real-world security checkpoint, bottlenecks in Zones B and C would translate to longer queue times in Zone A because of physical limits to the lengths of lines. However, we allow all queues to extend indeﬁnitely in order to discover precisely where bottlenecks exist in the screening process. Long queue lengths and wait times indicate which parts of the process are causing delays.

<!-- b000037 | heading | pages [4] -->
8. At most one passenger arrives to the checkpoint every second. Most airport security queues

<!-- b000038 | prose | pages [4] -->
are designed so that only one person can join at a time. It is reasonable to assume that passengers allow for a one-second gap to the next person.

<!-- b000039 | heading | pages [4] -->
9. Walking from the checkpoint entrance to the document-checking queue requires no time.

<!-- b000040 | prose | pages [4] -->
When lines are short, security oﬃcers will frequently reroute the queue to shorten the distance from the checkpoint entrance. As a result, it usually takes little time to walk to the end of the document-checking queue in Zone A.

<!-- b000041 | prose | pages [4] -->
10. An average American passenger’s personal space is a 3’ by 3’ square. [12]

<!-- b000042 | heading | pages [4] -->
11. All passengers eventually complete the screening process.

<!-- b000043 | prose | pages [4] -->
We assume that all passengers successfully exit the security checkpoint; none are arrested, detained, or leave the airport.

<!-- b000044 | heading | pages [4] -->
12. All travelers enrolled in the PreCheck program pass through WTMDs. [10]

<!-- b000045 | prose | pages [4] -->
13. Every passenger brings at least one piece of luggage. The TSA screens more than 1.7 billion carry-on bags a year, more than double the number of passengers. It is reasonable to assume that every traveler carrys at least one bag, if only to store his or her documents, wallet, and other important possesions.

<!-- b000046 | furniture | pages [5] -->
Team 68942

<!-- b000047 | furniture | pages [5] -->
Page 4 of 36

<!-- b000048 | heading | pages [5] -->
3.1 Normality

<!-- b000049 | caption | pages [5] -->
Figure 2: Normal Q-Q Plots for document check (left) and body scan (right) times

<!-- b000050 | prose | pages [5] -->
We used the Shapiro-Wilk normality test [4] and quantile-quantile (Q-Q) plots to determine the distributions of datasets from the given passenger data. We found two that could be approximated by normal distribu- tions: document check process times and millimeter wave body scanner times, as determined by subtracting successive timestamps in the given data. For both, normality was not rejected at the p = 0.01 signiﬁcance level and the Q-Q plots showed linear trends with fairly random deviations (Figure 2). This allowed us to design our program to generate probabilistic times based on a normal distribution.

<!-- b000051 | heading | pages [5] -->
3.2 Process Times

<!-- b000052 | prose | pages [5] -->
Many of the process times were determined from the given data. However, for some processes it was necessary to make certain assumptions regarding the TSA screening process and traveler speeds. We based many of these values on personal investigation and real-world footage of travelers in airport checkpoints.

<!-- b000053 | prose | pages [5, 6] -->
Zone Process Time (s) Walk to document check 2 A Document check 11.2 Walk to screening lane 3 [1] Unload belongings for screening 15 [1] Walk to scanner or WMTD line 3 B Walk to scanner or WMTD 2 Body scan 10.5 WTMD 1 Walk to collection line 3 Collect belongings 15 [1] C Exit 5-7 Walk to Zone D 3 D Pat-down 150 [8] Baggage Search 200 Some passengers enroll in PreCheck, a TSA program that expedites the screening process. Passengers in PreCheck do not need to remove jackets, belts, shoes, or laptops, shortening the time for unloading and retrieving belongings at the scanner (in our model, to 10 seconds). In addition, PreCheck passengers pass through WTMDs instead of the body scanners, which speeds the process further. However, the other times are largely the same.

<!-- b000054 | caption | pages [5] -->
Table 2: Process times for regular passengers

<!-- b000055 | furniture | pages [6] -->
Team 68942

<!-- b000056 | furniture | pages [6] -->
Page 5 of 36

<!-- b000058 | heading | pages [6] -->
3.3 Rates and Probabilities

<!-- b000059 | prose | pages [6] -->
Certain processes, like pat-downs and baggage searches, do not occur for every passenger. Instead, we assigned each process a certain probability.

<!-- b000060 | prose | pages [6] -->
• Each person has a 3% chance of being given a pat-down, including the approximate 1% of passengers who opt for a pat-down instead of a body scan [3]. Other reasons for pat-downs include failing a body scan or metal detector.

<!-- b000061 | prose | pages [6] -->
• The probability of having a baggage search is equal to that of receiving a pat-down.

<!-- b000062 | prose | pages [6] -->
• Travelers not enrolled in the PreCheck program have a 20% probability of being sent through the WTMD instead of the millimeter wave body scanner. The majority of non-PreCheck passengers sent through the WTMD are under 12, over 65, or have severe disabilities.

<!-- b000063 | heading | pages [6] -->
4 Deﬁnitions and Testing Parameters

<!-- b000064 | prose | pages [6] -->
The TSA wishes to evaluate and improve its airport security checkpoints. In particular, it is concerned with two statistics:

<!-- b000065 | prose | pages [6] -->
Deﬁnition 1. The throughput of a checkpoint at any time is the rate of passengers exiting the checkpoint.

<!-- b000066 | prose | pages [6] -->
The unit of throughput used in this paper is passengers per minute (PAX/min).

<!-- b000067 | prose | pages [6] -->
Deﬁnition 2. The wait time of a passenger is the total amount of time that he or she spent in queues during the checkpoint.

<!-- b000068 | prose | pages [6] -->
Our goal was to investigate possible bottlenecks in the security screening process that might cause de- creases in throughput, increases in wait time, and increases in wait time variance. We measured variance of wait time by calculating the standard deviation of the wait times of all passengers.

<!-- b000069 | heading | pages [6] -->
4.1 Arrivals

<!-- b000070 | prose | pages [6] -->
To simulate the randomness of the real-world passenger arrivals, passengers in our model are generated probabilistically every second rather than at a constant rate. Each arrival is then categorized as PreCheck or regular and sent to the corresponding queue.

<!-- b000071 | prose | pages [6] -->
Deﬁnition 3. The generation probability is the probability at each second that a passenger enters the checkpoint.

<!-- b000072 | prose | pages [6, 7] -->
From the given data, the generation probability is 0.19, the average “rate” of passengers per second from the given data (Figure 3). This was determined by counting the number of total passenger arrival timestamps, both PreCheck and regular, that occurred within nine minutes. After arriving, each new passenger has a 0.45 probability of joining the PreCheck queue, since approximately 45% of passengers are currently enrolled in PreCheck.

<!-- b000073 | furniture | pages [7] -->
Team 68942

<!-- b000074 | furniture | pages [7] -->
Page 6 of 36

<!-- b000076 | caption | pages [7] -->
Figure 3: Arrivals (PreCheck and regular) over time

<!-- b000077 | heading | pages [7] -->
4.2 Lanes and Oﬃcers

<!-- b000078 | prose | pages [7] -->
The checkpoint tested in our model contains six screening lanes. PreCheck lanes usually make up a third of total lanes, so when the checkpoint is fully running there are two PreCheck lanes and four regular lanes. The number of available oﬃcers in Zone D is equal to the number of active lanes: six. However, during times of less traﬃc airports will decrease the number of active screening lanes and document-checking oﬃcers in order to save money.

<!-- b000079 | prose | pages [7] -->
Therefore, we tested two diﬀerent conﬁgurations of active lanes and oﬃcers: one with all six lanes open for higher traﬃc, and one with only three lanes open for lower traﬃc.

<!-- b000080 | prose | pages [7] -->
Each conﬁguration is denoted by a four-digit number. For example, the number 1234 denotes the conﬁg- uration with 1 PreCheck document-checking oﬃcer, 2 active PreCheck screening lanes, 3 regular document- checking oﬃcers, and 4 active regular screening lanes.

<!-- b000081 | prose | pages [7] -->
Deﬁnition 4. The conﬁguration number is the four-digit number that denotes the numbers of lanes and oﬃcers active in the conﬁguration.

<!-- b000082 | heading | pages [7] -->
4.3 Testing

<!-- b000083 | prose | pages [7] -->
In our model, we tested diﬀerent volumes of traﬃc by increasing or decreasing the generation probability. We tested ﬁve generation probabilities: 0.09 (low traﬃc), 0.18 (normal traﬃc), 0.36 (busy traﬃc), 0.54 (high traﬃc), and 0.72 (peak traﬃc).

<!-- b000084 | prose | pages [7] -->
We tested conﬁguration 1221 for lower traﬃc (generation probabilities of 0.09, 0.18, 0.36, 0.54) and conﬁguration 2243 for higher traﬃc (generation probabilities of 0.18, 0.36, 0.54, 0.72). Each conﬁguration was run at least three times in our model, collecting data after each run and averaging across all runs to obtain our results. Each run generated passengers for one hour (3600 seconds) and then ran until the all passengers exited. To measure throughput, we counted the number of exiting passengers every ten minutes and divided by ten to obtain throughput passengers per minute.

<!-- b000085 | prose | pages [7, 8] -->
We also tested the eﬀect of increasing or decreasing the number of PreCheck document-checking oﬃcers on throughput and wait time, varying the number of oﬃcers from 1 to 3 for the 1221 conﬁguration and the standard 0.18 generation probability.

<!-- b000086 | furniture | pages [8] -->
Team 68942

<!-- b000087 | furniture | pages [8] -->
Page 7 of 36

<!-- b000089 | heading | pages [8] -->
5 NetLogo Model

<!-- b000090 | prose | pages [8] -->
To evaluate our assumptions and generate data, we use an agent-based NetLogo model. By using NetLogo, we are able to visually and robustly simulate passengers, oﬃcers, scanners, and queues in a time-accurate model. We can also use NetLogo’s powerful experimentation functionality to generate data.

<!-- b000091 | heading | pages [8] -->
5.1 Passengers

<!-- b000092 | prose | pages [8] -->
The basis of our model are passengers as represented by “turtles”, icons in the grid with attributes and the ability to perform actions. Each of our passengers has several attributes, including attributes that describe the passenger like is-precheck and speed-factor. Other attributes, including queue-pos and stage describe the passenger’s position in the model. Passengers are represented by pink (PreCheck) people, or purple (non-PreCheck) people.

<!-- b000093 | prose | pages [8] -->
Each passenger’s attributes are probabilistically decided by global values. For example, is-precheck is determined by precheck-percentage and is-cutter is determined by cutting-percentage. Passengers also record key data, including time-waiting to track total waiting time, and a wait-queue value for each queue they wait in.

<!-- b000094 | heading | pages [8] -->
5.2 Other turtles

<!-- b000095 | caption | pages [8] -->
Figure 4: This screenshot shows the simulation before passengers are generated.

<!-- b000096 | prose | pages [8, 9] -->
Our passengers are aﬀected by not only their own attributes, but by the oﬃcers, scanners, and “pack stations”. Oﬃcers occupy one of two areas: either an document check lane (Zone A), or the rescreen/pat- down lanes (Zone D). In Zone A, they are assigned to either precheck or non-precheck, calling for passengers at the beginning of their respective queues. They are represented by orange people with blue hats and a badge. In Zone D, they are represented by a single oﬃcer icon that can patdown/rescreen multiple passengers. Scanners come in two forms - millimeter wave scanners or walk-through metal detectors. Each scanner pair operates as part of two lanes, and has its own queue. Millimeter wave scanners are represented by red hexagons, and WTMDs are represented by yellow rectangles. “Pack stations” are used to represent the areas in which passengers take oﬀor put on coats, bags, and other items before or after screening. Each lane has one “unpack station” and one “repack station”. They are represented by the dark brown circles on the lighter brown x-ray machines.

<!-- b000097 | furniture | pages [9] -->
Team 68942

<!-- b000098 | furniture | pages [9] -->
Page 8 of 36

<!-- b000100 | heading | pages [9] -->
5.3 Running the simulation

<!-- b000101 | prose | pages [9] -->
When setup is called, the world creates oﬃcers, scanners, packing stations, and colors patches to visually guide the progression of passengers through lanes. When the model is set to go, the model generates a passenger at each tick (equivalent to a second) at a certain probability gen-prob. Passengers progress through security in several stages according to our outlined process. Our simulation only generates passengers in the ﬁrst 3600 ticks in order to only simulate a single real-world hour. The simulation stops when there are no longer passengers in the security checkpoint. At the end of the run, we use mean and standard-deviation to calculate the values we use for our analysis.

<!-- b000102 | caption | pages [9] -->
Figure 5: This screenshot shows a simulation in progress.

<!-- b000103 | prose | pages [9] -->
For single, visible runs, we use the green sliders on the left to adjust parameters, the purple buttons to setup and go, viewing output in the boxes on the right when the simulation ﬁnishes. For batches of runs, we use NetLogo’s “BehaviorSpace” to run 3 trials of simulations with varying parameters.

<!-- b000104 | furniture | pages [10] -->
Team 68942

<!-- b000105 | furniture | pages [10] -->
Page 9 of 36

<!-- b000106 | heading | pages [10] -->
6 Results

<!-- b000107 | caption | pages [10] -->
Figure 6: Average throughputs (passengers/minute) over time for the 1221 conﬁguration

<!-- b000108 | prose | pages [10] -->
Total Average Wait Time Total Standard Deviation Generation Probability (sec) (sec) 0.09 20.51 41.68 0.18 232.39 286.88

<!-- b000109 | caption | pages [10] -->
Table 3: Wait time data for the 1221 conﬁguration

<!-- b000110 | prose | pages [10] -->
Generation Average Standard Deviation Average Standard Deviation Queue Probability (PreCheck) (PreCheck) (Regular) (Regular) q0 0.69 2.25 9.58 17.46 q1 0.00 0.00 0.00 0.00 0.09 q2 0.28 0.85 0.14 0.92 q3 23.17 50.30 7.72 27.29 Total 24.14 53.40 17.45 45.67 q0 1.75 4.08 372.53 297.88 q1 0.00 0.00 0.00 0.00 0.18 q2 0.51 1.15 0.40 1.72 q3 36.68 64.89 15.00 42.05 Total 38.94 70.12 387.93 341.65

<!-- b000111 | caption | pages [10] -->
Table 4: Wait times (sec) by queue for the 1221 conﬁguration

<!-- b000112 | prose | pages [10, 11] -->
For conﬁguration 1221, the average throughput peaks at about 14 passengers/min for generation probabilities of 0.36 and 0.54, indicating that this was not the best conﬁguration for those higher traﬃc volumes (Figure 6). However, for 0.09 and 0.18 the conﬁguration had more than enough capacity for the arrivals. This seems to imply that the bottleneck for throughput is primarily the number of active lanes and oﬃcers; once arrival rates increase past a certain point, increases in arrival rate no longer signiﬁcantly impacts the throughput. From Table 4, it is clear that the main bottleneck of both the PreCheck and the regular processes is line q3 (retrieving belongings from the x-ray belt) for all except the regular passengers at 0.18 generation probability, where the bottleneck is q0 (document-checking line). The variance in wait times is more than double the average wait time for a generation probability of 0.09. This may also be due to the natural variance that occurs from such a low generation probability, since high variance in arrivals easily translates to variance in wait times and throughput.

<!-- b000113 | furniture | pages [11] -->
Team 68942

<!-- b000114 | furniture | pages [11] -->
Page 10 of 36

<!-- b000116 | prose | pages [11] -->
The wait time standard deviation is not immediately concerning for all but the 0.18, regular passengers case. The highest total standard deviation in those three cases is 70 seconds, or just over a minute. This means that a traveler having to wait more than ﬁve minutes longer than expected is high improbable. However, the case of regular passengers in the 0.18 generation probability case is much greater, with a wait time standard deviation of nearly six minutes.

<!-- b000117 | prose | pages [11] -->
Total Average Wait Time Total Standard Deviation Generation Probability (sec) (sec) 0.18 3.95 6.89 0.36 221.27 351.47 0.54 1088.93 867.74 0.72 2012.31 1409.13

<!-- b000118 | caption | pages [11] -->
Table 5: Wait time data for the 2243 conﬁguration

<!-- b000119 | prose | pages [11, 12] -->
Generation Average Standard Deviation Queue Probability (PAX) (PAX) q0 1.97 4.67 q1 0.00 0.00 0.18 q2 0.39 0.96 q3 0.00 0.00 Total 2.36 5.63 q0 162.31 322.88 q1 0.00 0.00 0.36 q2 0.66 1.15 q3 0.00 0.00 Total 162.98 324.03 q0 914.88 545.95 q1 0.00 0.00 0.54 q2 0.80 1.31 q3 0.00 0.00 Total 915.69 547.26 q0 1817.71 1060.32 q1 0.00 0.00 0.72 q2 0.76 1.27 q3 0.00 0.00 Total 1818.47 1061.59 Generation Average Standard Deviation Queue Probability (PAX) (PAX) q0 0.49 1.80 q1 0.00 0.00 0.18 q2 4.83 7.43 q3 0.00 0.00 Total 5.31 9.24 q0 7.94 17.12 q1 0.00 0.00 0.36 q2 262.35 345.87 q3 0.00 0.00 Total 270.29 363.00 q0 484.27 275.54 q1 0.00 0.00 0.54 q2 744.30 871.23 q3 0.00 0.00 Total 1228.57 1146.77 q0 1219.21 714.21 q1 0.00 0.00 0.72 q2 945.64 1154.63 q3 0.00 0.00 Total 2164.86 1868.85

<!-- b000120 | caption | pages [11] -->
Table 6: PreCheck wait times (sec) by queue for the 2243 conﬁguration

<!-- b000121 | furniture | pages [12] -->
Team 68942

<!-- b000122 | furniture | pages [12] -->
Page 11 of 36

<!-- b000124 | caption | pages [12] -->
Table 7: Regular wait times (sec) by queue for the 2243 conﬁguration

<!-- b000125 | caption | pages [12] -->
Figure 7: Average throughputs (passengers/minute) over time for the 2243 conﬁguration

<!-- b000126 | prose | pages [12, 13] -->
For conﬁguration 2243, the average throughput peaks at about 21 passengers/min for generation prob- abilities of 0.36, 0.54 and 0.72, indicating that this was not the best conﬁguration for those higher traﬃc volumes (Figure 7). However, for a generation probability of 0.09, the conﬁguration had more than enough capacity for the arrivals. From the regular passengers described in table 7, we see a bottleneck at both the document check queue (q0) and the scanner queue (q2). Our PreCheck passengers in table 6 do not have a bottleneck in the scanner queue, but still have a high waiting time in the document check queue. Our observed variance in q0 wait times is more than double the average for regular and PreCheck passengers with generation probabilities 0.18 and 0.36, likely due to a few extremely high wait times. Our standard deviation with a generation probability is low, less than 10 seconds in either case. With generation probability 0.36, the standard deviation increases to approximately 5.5 minutes for PreCheck and 6 minutes for non-PreCheck passengers. Standard deviations of generation probabilities of 0.54 and 0.72 become excessive, almost 10 and 20 minutes for PreCheck and 20 and 30 minutes for non-PreCheck passengers. We see an unacceptably high standard deviation of wait times with this conﬁguration at high density populations.

<!-- b000127 | furniture | pages [13] -->
Team 68942

<!-- b000128 | furniture | pages [13] -->
Page 12 of 36

<!-- b000130 | heading | pages [13] -->
6.1 Varying PreCheck Document-checking Oﬃcers

<!-- b000131 | prose | pages [13] -->
Number of Average Wait Time Standard Deviation Avg. Throughput PreCheck Oﬃcers (sec) (sec) (PAX/min) 1 2216.70 1276.84 4.82 2 309.62 252.01 9.23 3 59.26 101.28 10.49

<!-- b000132 | caption | pages [13] -->
Table 8: Throughput and wait times for varying numbers of PreCheck oﬃcers

<!-- b000133 | prose | pages [13] -->
As the number of document-checking oﬃcers increases, both the average wait time and the wait time standard deviation decrease signiﬁcantly, with the largest decrease occurring from one to two oﬃcers. However, while there is a signiﬁcant increase of nearly 100% in average throughput from one to two oﬃcers, the increase from two to three is much smaller. Therefore, when taking cost into account two oﬃcers does seem to be the optimal number when there is one active PreCheck lane and low traﬃc.

<!-- b000134 | caption | pages [13] -->
Figure 8: Average throughputs (passengers/minute) over time for varing numbers of PreCheck oﬃcers

<!-- b000135 | heading | pages [13] -->
7 Improvements to the Current Process

<!-- b000136 | prose | pages [13] -->
It was clear from the results in Section 6 that there was much room for improvement in the current security screening process. We proposed four modiﬁcations and, using the NetLogo model, investigated how these changes might aﬀect throughput and wait times. The modiﬁcations were:

<!-- b000137 | furniture | pages [14] -->
Team 68942

<!-- b000138 | furniture | pages [14] -->
Page 13 of 36

<!-- b000139 | prose | pages [14] -->
1. Adding another metal detector

<!-- b000140 | prose | pages [14] -->
2. Increasing the probability of WTMD usage for non-PreCheck passengers

<!-- b000141 | prose | pages [14] -->
3. Adding another millimeter wave body scanner

<!-- b000142 | prose | pages [14] -->
4. Reducing Pat-Down Times

<!-- b000143 | prose | pages [14] -->
5. Increasing the percent of PreCheck passengers

<!-- b000144 | prose | pages [14] -->
6. Increasing the number of PreCheck document-checkers

<!-- b000145 | prose | pages [14] -->
For nearly all modiﬁcations to the original model, we used the 1221 conﬁguration for generation proba- bilities of 0.09 and 0.18 and the 2243 conﬁguration for generation probabilities of 0.36, 0.54, and 0.72.

<!-- b000146 | heading | pages [14] -->
7.1 Throughput Data

<!-- b000147 | caption | pages [14] -->
Table 9 shows the change in average throughput from each of the modiﬁcations.

<!-- b000148 | prose | pages [14] -->
Generation Extra Metal More WTMD Use Extra Shorter Probability Detector 30 40 50 Scanner Pat-downs 9 – 0.97 1.77 1.59 0.93 1.02 18 – 0.60 0.71 1.01 1.03 1.01 36 1.00 1.01 1.14 1.16 1.08 0.99 54 1.22 1.04 1.05 1.08 1.11 0.99 72 1.43 1.05 1.08 1.13 1.13 1.00

<!-- b000149 | caption | pages [14] -->
Table 9: Ratio of new to original throughputs

<!-- b000150 | heading | pages [14] -->
7.2 Extra Metal Detector

<!-- b000151 | prose | pages [14] -->
By adding another metal detector to our PreCheck lanes, we can alleviate queue wait times and decrease variance in the queue before scanning (q2).

<!-- b000152 | prose | pages [14] -->
Wait Time Standard Deviation Wait Time Standard Deviation Generation w/o Extra w/o Extra w/ Extra w/ Extra Probability PreCheck Lane PreCheck Lane PreCheck Lane PreCheck Lane (sec) (sec) (sec) (sec) 0.36 221.27 351.47 337.27 329.46 0.54 1088.93 867.74 711.87 940.49 0.72 2012.31 1409.13 1344.34 1607.91

<!-- b000153 | caption | pages [14] -->
Table 10: Average Wait Times and Standard Deviations of the Screening Process with and without an extra

<!-- b000154 | prose | pages [14] -->
metal detector

<!-- b000155 | prose | pages [14] -->
From Table 10 we can see that adding an extra metal detector when the generation probability is 0.54 and 0.72 signiﬁcantly decreases the average wait time of the screening process. We do not see the same eﬀect with a generation possibility of 0.36. However, the metal detector does increase throughput at all three generation probabilities. Thus, we can conclude that adding an extra metal detector is strictly beneﬁcial.

<!-- b000156 | prose | pages [14, 15] -->
The increases in standard deviation are likely to due the fact that PreCheck passengers already experience shorter wait times than regular passengers do. Decreasing PreCheck times further will increase overall standard deviation. Based on table 9, adding an extra metal detector increases throughput from 28% to 82% varying based on generation probabilty.

<!-- b000157 | furniture | pages [15] -->
Team 68942

<!-- b000158 | furniture | pages [15] -->
Page 14 of 36

<!-- b000160 | heading | pages [15] -->
7.3 Increasing WTMD Usage

<!-- b000161 | prose | pages [15] -->
Travelers pass through the WTMD almost without stopping, while travelers that use the millimeter wave body scanner spend about 11 seconds being scanned. If we increase the probability that any traveler proceeds through the WTMD instead of the millimeter wave body scanner, we should be able to increase the rate at which travelers pass through Zone B. To modify our current model, which has 20% of travelers being selected for the WTMD, we increased that probability to 30%, 40%, and 50%. Figure 11 shows the results.

<!-- b000162 | caption | pages [15] -->
Figure 9: Average Wait Times for Diﬀerent Probabilities of People Passing Through WTMDs. All data is

<!-- b000163 | prose | pages [15] -->
expressed as the mean + the standard deviation.

<!-- b000164 | prose | pages [15] -->
From Figure 11, we can see that increasing the probability of travelers proceeding through the WTMD instead of the millimeter wave body scanners does indeed decrease the average wait time of travelers during the screening process. Looking at the generation probabilities of 0.36, 0.54, and 0.72, there is a clear downward trend as the probability increases. The same is true for standard deviations of wait times; while the change that they show is less, there is a noticeable decrease in standard deviations from the original 20% WTMD usage for higher generational probabilities (0.36, 0.54, and 0.72). Based on table 9, increasing WTMD usage correlates to increasing throughput, anywhere from a decrease of 40% to an increase of 113% based on generation probability. The beneﬁts of increasing WTMD usage are most pronounced with a 50% usage rate, presenting a beneﬁt to all generation probabilites.

<!-- b000165 | heading | pages [15] -->
7.4 Extra Millimeter Wave Scanner

<!-- b000166 | prose | pages [15, 16] -->
By adding an additional millimeter wave scanner, the security checkpoint should see an increase in throughput as more passengers are able to be scanned. We see a greatly decreased wait time and standard deviation for most passenger arrival densities, but an increased wait time and standard deviation when the generation probability is 0.18. The diﬀerences are signiﬁcant; for higher traﬃc volumes (generation probabilities of 0.36 or more), the standard deviation decreases by more than a third. This could justify the extra cost of adding another body scanner, which costs about $250,000 [12].

<!-- b000167 | furniture | pages [16] -->
Team 68942

<!-- b000168 | furniture | pages [16] -->
Page 15 of 36

<!-- b000170 | prose | pages [16] -->
Wait Time Standard Deviation Wait Time Standard Deviation w/ Extra Scanner w/ Extra Scanner Generation Probability (sec) (sec) (sec) (sec) 0.09 20.51 41.68 16.91 36.35 0.18 232.39 286.88 314.69 376.13 0.36 221.27 351.47 111.61 104.23 0.54 1088.93 867.74 526.05 530.25 0.72 2012.31 1409.13 989.71 992.35

<!-- b000171 | caption | pages [16] -->
Table 11: Average Wait Times and Standard Deviations of the Screening Process with and without an Extra

<!-- b000172 | prose | pages [16] -->
Scanner

<!-- b000173 | prose | pages [16] -->
Adding an extra scanner can have mixed results on throughput (based on Table 9). Though it causes a throughput increase of 3% to 99% for generation probabilities 18 to 72, the checkpoints’s throughput decreases by 7% with a low generation probability of 9%.

<!-- b000174 | heading | pages [16] -->
7.5 Decreasing Pat-down Times

<!-- b000175 | prose | pages [16] -->
We consider improved training for TSA oﬃcers responsible for conducting pat-downs and baggage rescreening in order to improve these processes. This would cause an increase in throughput, as faster pat-downs and rescreenings would allow these aﬀected passengers to pass through security more quickly. We see a slight decrease in wait time and standard deviation for lower generation probabilities, namely 9% and 18%. However, for higher traﬃc the changes are nearly negligible, with the standard deviation increasing for when generation probability is 0.72.

<!-- b000176 | prose | pages [16] -->
Wait Time Standard Deviation Wait Time Standard Deviation Generation w/ Regular Pat-downs w/ Regular Pat-downs w/ Faster Pat-downs w/ Faster Pat-downs Probability (sec) (sec) (sec) (sec) 0.09 20.51 41.68 13.13 27.23 0.18 232.39 286.88 190.30 249.36 0.36 221.27 351.47 199.50 314.69 0.54 1088.93 867.74 1089.12 838.24 0.72 2012.31 1409.13 2095.55 1489.29

<!-- b000177 | caption | pages [16] -->
Table 12: Average Wait Times and Standard Deviations of the Screening Process with Regular and Faster

<!-- b000178 | prose | pages [16] -->
Pat-downs

<!-- b000179 | prose | pages [16] -->
Based on table 9, shorter pat-downs have a very slight change to the average throughput (±5%), with the exception of a generation probability of 36, which had a 82% increase.

<!-- b000180 | heading | pages [16] -->
7.6 Increasing percentage of PreCheck passengers

<!-- b000181 | prose | pages [16] -->
TSA PreCheck allows passengers to pass through security without removing light jackets, shoes, laptops, and belts. It also allows passengers to more quickly pass through security with a WTMD rather than a millimeter body scanner. An increase in percentage of people with access to this expedited process could potentially increase the throughput of the security checkpoint and reduce variance from waiting in the scanner queue.

<!-- b000182 | furniture | pages [17] -->
Team 68942

<!-- b000183 | furniture | pages [17] -->
Page 16 of 36

<!-- b000184 | caption | pages [17] -->
Figure 10: Average Wait Times for varying percentages of passengers with PreCheck. All data is expressed

<!-- b000185 | prose | pages [17] -->
as the mean + standard deviation.

<!-- b000186 | prose | pages [17] -->
However, while the increase did lead to improvements when traﬃc was low, the increase in percentage of PreCheck passengers was detrimental at probabilities higher than 0.18. This is likely due to the limiting factor of only two lanes and two document-checking oﬃcers for PreCheck passengers.

<!-- b000187 | heading | pages [17] -->
7.7 Increasing the number of PreCheck percentage and document-checkers

<!-- b000188 | prose | pages [17] -->
Having observed a bottleneck in the document-checking queue with PreCheck passengers at high volumes of traﬃc, we add two document-checking oﬃcers, making the conﬁguration 2443 rather than 2243.

<!-- b000189 | caption | pages [17] -->
Figure 11: Average Wait Times for varying percentages of passengers with PreCheck. All data is expressed

<!-- b000190 | prose | pages [17] -->
as the mean + standard deviation.

<!-- b000191 | furniture | pages [18] -->
Team 68942

<!-- b000192 | furniture | pages [18] -->
Page 17 of 36

<!-- b000193 | prose | pages [18] -->
We see that as we increase percentage of PreCheck enrollment, we see an overall decrease in wait time and wait time variance, lowest at 55%. After this sharp dip, average wait time increases steadily. This is observed at all generation probabilites, though it is most pronounced after 0.36. Overall, a slight increase in PreCheck enrollment is greatly beneﬁcial.

<!-- b000194 | heading | pages [18] -->
8 Variation in Traveler Behavior

<!-- b000195 | prose | pages [18] -->
In our model, we assumed that passengers follow mostly the same behavior, with only small variations in times. However, in the real world passengers exhibit a wide range of diﬀerent behaviors. This is especially true at large international airports, where passengers diﬀer by culture in addition to age, mobility, and personal preferences. We tested our model with the addition of new traveler styles to investigate how diﬀerent social interactions would aﬀect throughput and wait time. In particular, we investigated the following behaviors:

<!-- b000196 | prose | pages [18] -->
1. Cutting in line

<!-- b000197 | prose | pages [18] -->
2. Aversion to body scanners (people can opt out of body scanning and receive a pat-down instead)

<!-- b000198 | prose | pages [18] -->
3. Slower movement

<!-- b000199 | heading | pages [18] -->
8.1 Throughput Data

<!-- b000200 | prose | pages [18] -->
Table ?? shows the change in average throughput from each new passenger behavior.

<!-- b000201 | prose | pages [18] -->
Generation More Pat-downs Slow Cutting Probability 1% 2% Travelers 0.09 1.04 0.98 0.98 0.94 0.18 1.05 1.00 1.00 0.99 0.36 1.00 0.99 0.98 1.00 0.54 0.99 0.99 0.99 0.99 0.72 1.00 1.01 1.02 0.98

<!-- b000202 | caption | pages [18] -->
Table 13: Ratio of New to Old Throughputs

<!-- b000203 | heading | pages [18] -->
8.2 Cutting

<!-- b000204 | prose | pages [18] -->
In the interest of personal eﬃciency, some passengers may value their own position in queues rather more than the queue’s overall order. We refer to these passengers as “cutters”, people who will try to skip to the front of their queue and succeed about half the time. In modifying our model, we had 20% of travelers be cutters.

<!-- b000205 | prose | pages [18] -->
Comparing the data at various arrival densities (Table 14), we ﬁnd that cutting led to an increase in average and standard deviations of wait time. This may be because cutters cause other passengers to have to wait longer, therefore increasing the average wait time and standard deviation; as expected, cutting beneﬁts only those who cut. However, the negative eﬀects of cutting could be mitigated by enforcing a strict no-cutting policy in all queues.

<!-- b000206 | furniture | pages [19] -->
Team 68942

<!-- b000207 | furniture | pages [19] -->
Page 18 of 36

<!-- b000208 | prose | pages [19] -->
Wait Time Standard Deviation Wait Time Standard Deviation Generation w/o Cutting w/o Cutting w/ Cutting w/ Cutting Probability (sec) (sec) (sec) (sec) 0.09 20.51 41.68 18.49 39.65 0.18 232.39 286.88 329.34 385.85 0.36 221.27 351.47 266.60 634.58 0.54 1088.93 867.74 1143.61 1183.92 0.72 2012.31 1409.13 2075.03 1697.81

<!-- b000209 | caption | pages [19] -->
Table 14: Average Wait Times and Standard Deviations of the Screening Process with Individuals Who Cut

<!-- b000210 | heading | pages [19] -->
8.3 Higher Pat-down Probability

<!-- b000211 | prose | pages [19] -->
Since the addition of the new millimeter wave body scanners to the TSA’s screening process in 2010, many travelers have expressed their concerns about the privacy of these machines. Responding to those concerns, the TSA allow people to defer a scan by the millimeter wave body scanner and receive a pat-down instead. Thus, we tested diﬀerent probabilities of travelers declining a millimeter wave body scan and receiving a pat-down to see if it had any eﬀect on the wait time for the screening process. According to the TSA, only about 1% of travelers opt for a pat-down instead of a millimeter wave body scan so we tested both a 1% probability and a 2% probability [8].

<!-- b000212 | caption | pages [19] -->
Figure 12: Average wait times for various patdown probabilities. All data is expressed as the mean + the

<!-- b000213 | prose | pages [19] -->
standard deviation.

<!-- b000214 | prose | pages [19] -->
From Figure 12, a 1% or 2% amount of travelers deferring a millimeter wave scan does not aﬀect the wait time standard deviations signiﬁcantly. This may not remain true for higher probabilities, but with low probabilities, the eﬀect is not signiﬁcant.

<!-- b000215 | furniture | pages [20] -->
Team 68942

<!-- b000216 | furniture | pages [20] -->
Page 19 of 36

<!-- b000217 | heading | pages [20] -->
8.4 Slower Travelers

<!-- b000218 | prose | pages [20] -->
Not all travelers move at the same rate. While young adults move relatively quickly, older travelers and children may move slower than them. Thus, to incorporate the idea of a variety of speeds, we included slow travelers into the model. These travelers move half as fast as regular travelers and appear 20% of the time.

<!-- b000219 | prose | pages [20] -->
Wait Time Standard Deviation Wait Time Standard Deviation Generation w/o Slow Travelers w/o Slow Travelers w/ Slow Travelers w/ Travelers Probability (sec) (sec) (sec) (sec) 0.09 20.51 41.68 13.27 31.75 0.18 232.39 286.88 268.67 312.06 0.36 221.27 351.47 314.23 386.51 0.54 1088.93 867.74 1126.22 812.25 0.72 2012.31 1409.13 2101.90 1399.51

<!-- b000220 | caption | pages [20] -->
Table 15: Average Wait Times and Standard Deviations of the Screening Process with and Without Slow

<!-- b000221 | prose | pages [20] -->
Travelers

<!-- b000222 | prose | pages [20] -->
From Figure 15, we can see that the addition of slow travelers increases the wait time, but not the standard deviation of screening process. This seems logical, because slower travelers will not only slow down the process as a whole, but also slow down travelers around them, accounting for the smaller standard deviations.

<!-- b000223 | heading | pages [20] -->
9 Policy and Procedural Recommendations

<!-- b000224 | prose | pages [20] -->
Based on our observations, we recognize several problem areas for current TSA checkpoints. PreCheck passengers are limited by the number of document-checking TSA oﬃcers, especially at a high volume of traﬃc. Non-PreCheck passengers are limited by document checking queues and scanner queues. These high wait times also lead to unacceptably large wait times and variances in those wait times, up to 30 minutes in high traﬃc scenarios. To improve the eﬃciency of the security checkpoint, we encourage the TSA to make one or more of the following changes:

<!-- b000225 | prose | pages [20] -->
• Add a metal detector to alleviate long, varied queue lengths in PreCheck lanes.

<!-- b000226 | prose | pages [20] -->
• Add a millimeter wave scanner in non-PreCheck lanes in order to reduce variance and length of queues.

<!-- b000227 | prose | pages [20] -->
• Increase the number of document-checking TSA oﬃcers

<!-- b000228 | prose | pages [20] -->
In order to address future increases in the proportion of passengers enrolled in PreCheck, we also suggest the following:

<!-- b000229 | prose | pages [20] -->
• Add document-checking TSA oﬃcers for PreCheck queues

<!-- b000230 | prose | pages [20] -->
• Add more Pre-Check lanes

<!-- b000231 | prose | pages [20] -->
Devoting more resources to PreCheck is less eﬀective on its own. These changes are only made eﬀective by an increase in PreCheck enrollment.

<!-- b000232 | prose | pages [20] -->
Other observed behaviors, including slower passengers and passengers that cut in front of others can be addressed speciﬁcally:

<!-- b000233 | furniture | pages [21] -->
Team 68942

<!-- b000234 | furniture | pages [21] -->
Page 20 of 36

<!-- b000235 | prose | pages [21] -->
• Enforce stricter queueing. Cutting increases wait time variance and can increase average wait time, especially at higher traﬃc volumes. Posted signs in queues can help reduce incentive to skip through queues.

<!-- b000236 | prose | pages [21] -->
• Slower travelers can be overwhelmed in high traﬃc scenarios, but should be reassured their progress through security is not aﬀecting variance.

<!-- b000237 | heading | pages [21] -->
10 Strengths and Weaknesses

<!-- b000238 | prose | pages [21] -->
In future work, we would like to address the weaknesses of our model and improve on the computational eﬃciency of our simulations. This model had a number of strengths and weaknesses:

<!-- b000239 | prose | pages [21] -->
• Strength: Our model is based on real data released by the TSA.

<!-- b000240 | prose | pages [21] -->
By generating values based on real-world data directly from the TSA and other reputable sources, our model more eﬀectively represents real-world scenarios.

<!-- b000241 | prose | pages [21] -->
• Strength: Our model uses probabilistic methods to generate data.

<!-- b000242 | prose | pages [21] -->
Because we use previous data but add random variance, we are able to simulate scenarios with realistic randomness. A deterministic model would not be able to factor the signiﬁcant unpredictability that is present in the real world.

<!-- b000243 | prose | pages [21] -->
• Strength: Our model is ﬂexible and readily adaptable.

<!-- b000244 | prose | pages [21] -->
By using NetLogo, we can very quickly and easily change settings to investigate eﬀects of each param- eter. The experimentation capabilities of NetLogo allow us to automatically compile large quantities of data in spreadsheets. Our many inputs allow a wide variety of conﬁgurations to be ﬁne-tuned.

<!-- b000245 | prose | pages [21] -->
• Strength: Our model tests a large variety of modiﬁcations and diﬀerent behaviors.

<!-- b000246 | prose | pages [21] -->
We were able to simulate changes in both the checkpoint itself and in human behavior, and ﬁnd some modiﬁcations that improved overall eﬃciency of the checkpoint.

<!-- b000247 | prose | pages [21] -->
• Weakness: Our model cannot assess all potential combinations of parameters and conﬁgurations.

<!-- b000248 | prose | pages [21] -->
The ideal solution would test each of the thousands of possible security conﬁgurations, varying the numbers of lanes, document-checking oﬃcers, and equipment to ﬁnd the optimal conﬁguration. How- ever, this is a vastly unreasonable task. Instead, our model compares a large set of conﬁgurations to determine the best one.

<!-- b000249 | prose | pages [21] -->
• Weakness: Our model does not include a quantiﬁcation of security.

<!-- b000250 | prose | pages [21] -->
Each simulation, though representative of throughput and queue times, does not quantify security. It is diﬃcult to analyze how “secure” a checkpoint without extensive data and studies on each component of the screening process.

<!-- b000251 | prose | pages [21] -->
• Weakness: Our model cannot portray the complete complexity of human behaviors.

<!-- b000252 | prose | pages [21] -->
Though we consider a number of the most common behaviors, including diﬀering perceptions of personal space and propensity for cutting in line, there are many more to be found among real-world passengers.

<!-- b000253 | prose | pages [21] -->
Analyzing and implementing more behaviors into our model is a strong avenue for future work.

<!-- b000254 | prose | pages [21] -->
• Weakness: Our model has a limited number of trials for each combination of factors.

<!-- b000255 | prose | pages [21] -->
Though we are able to analyze data with 3 trials each, due to the probabilistic nature of the model, these trials may not accurately reﬂect the real-world system. More trials would allow us to more accurately analyze our model.

<!-- b000256 | furniture | pages [22] -->
Team 68942

<!-- b000257 | furniture | pages [22] -->
Page 21 of 36

<!-- b000258 | heading | pages [22] -->
References

<!-- b000259 | references | pages [22] -->
[1] “Airport Security Footage - September 2006. Minneapolis International Airport.” YouTube. YouTube,

<!-- b000260 | references | pages [22] -->
14 Oct. 2010. Web. 20 Jan. 2017.

<!-- b000261 | references | pages [22] -->
[2] Burns, Bob. “TSA 2015 Year in Review.” The TSA Blog. Transportation Security Administration, 21

<!-- b000262 | references | pages [22] -->
Jan. 2016. Web. 20 Jan. 2017.

<!-- b000263 | references | pages [22] -->
[3] Burns, Bob. “TSA Myth or Fact: Leaked Images, Handcuﬀed Hosts, Religious Garb, and More!” The

<!-- b000264 | references | pages [22] -->
TSA Blog. Transportation Security Administration, 18 Nov. 2010. Web. 21 Jan. 2017.

<!-- b000265 | references | pages [22] -->
[4] Dittami, Simon. “Shapiro-Wilk Normality Test.” Shapiro Wilk Test (Web Version). N.p., 2009. Web.

<!-- b000266 | references | pages [22] -->
20 Jan. 2017.

<!-- b000267 | references | pages [22] -->
[5] Duarte, Lourdes. “Long Lines Reported at Chicago Midway Airport’s TSA Checkpoint.” WGN-TV.

<!-- b000268 | references | pages [22] -->
WGN-TV, 13 July 2016. Web. 20 Jan. 2017.

<!-- b000269 | references | pages [22] -->
[6] Gildor, Omri A. “Security of Airports: Full Body Scanners and Walk Through Metal Detectors – CSCI

<!-- b000270 | references | pages [22] -->
1951E S01: Computer Systems Security: Principles and Practice.” CSCI 1951E S01 Computer Systems

<!-- b000271 | references | pages [22] -->
Security Principles and Practice. Brown University, 3 Feb. 2015. Web. 20 Jan. 2017.

<!-- b000272 | references | pages [22] -->
[7] Hetter, Katia. “How Long Will I Wait in the TSA Line?” CNN. Cable News Network, 9 June 2016.

<!-- b000273 | references | pages [22] -->
Web. 20 Jan. 2017.

<!-- b000274 | references | pages [22] -->
[8] Jansen, Bart. “TSA Defends Full-body Scanners at Airport Checkpoints.” USA Today. Gannett Satellite

<!-- b000275 | references | pages [22] -->
Information Network, 02 Mar. 2016. Web. 20 Jan. 2017.

<!-- b000276 | references | pages [22] -->
[9] McCoy, William. ”How Many Carry-on Items Can a Person Bring on an Airplane?” USA Today. Gannett

<!-- b000277 | references | pages [22] -->
Satellite Information Network, n.d. Web. 21 Jan. 2017.

<!-- b000278 | references | pages [22] -->
[10] Michaels, Allison. “The Pros and Cons of TSA PreCheck.” U.S. News World Report. U.S. News World

<!-- b000279 | references | pages [22] -->
Report, 22 Apr. 2014. Web. 20 Jan. 2017.

<!-- b000280 | references | pages [22] -->
[11] “Mission.” Transportation Security Administration. The Department of Homeland Security, 09 Dec.

<!-- b000281 | references | pages [22] -->
2016. Web. 20 Jan. 2017.

<!-- b000282 | references | pages [22] -->
[12] ”Security Checkpoint Layout Design/Reconﬁguration Guide.” Transportation Security Administration.

<!-- b000283 | references | pages [22] -->
The Department of Homeland Security, 7 Nov. 2006. Web. 20 Jan. 2017.

<!-- b000284 | references | pages [22] -->
[13] Schuppe, John. “Airline Slams TSA over Long Delays, Missed Flights.” CNBC. CNBC, 14 Apr. 2016.

<!-- b000285 | references | pages [22] -->
Web. 20 Jan. 2017.

<!-- b000286 | references | pages [22] -->
[14] “Transportation Security Timeline.” Transportation Security Administration. The Department of Home-

<!-- b000287 | references | pages [22] -->
land Security, n.d. Web. 20 Jan. 2017.

<!-- b000288 | references | pages [22] -->
[15] “Travel Tips: Advanced Imaging Technology.” Transportation Security Administration. The Depart-

<!-- b000289 | references | pages [22] -->
ment of Homeland Security, 12 May 2016. Web. 20 Jan. 2017.

<!-- b000290 | references | pages [22] -->
[16] “TSA Releases 2015 Statistics.” Transportation Security Administration. The Department of Homeland

<!-- b000291 | references | pages [22] -->
Security, 21 Jan. 2016. Web. 20 Jan. 2017.

<!-- b000292 | references | pages [22] -->
[17] Wilensky, U. (1999). NetLogo. http://ccl.northwestern.edu/netlogo/. Center for Connected Learning

<!-- b000293 | references | pages [22] -->
and Computer-Based Modeling, Northwestern University, Evanston, IL.

<!-- b000294 | references | pages [22] -->
[18] Wisniewski, Mary. “At Chicago Airports, Wait times in TSA Lines Are 10 Minutes or Less.” Chicagotri-

<!-- b000295 | references | pages [22] -->
bune.com. Chicago Tribune, 23 Aug. 2016. Web. 20 Jan. 2017.

<!-- b000296 | furniture | pages [23] -->
Team 68942

<!-- b000297 | furniture | pages [23] -->
Page 22 of 36

<!-- b000298 | references | pages [23] -->
Generation

<!-- b000299 | references | pages [23] -->
Average

<!-- b000300 | references | pages [23] -->
Standard Deviation

<!-- b000301 | references | pages [23] -->
Queue

<!-- b000302 | references | pages [23] -->
Probability

<!-- b000303 | references | pages [23] -->
(PAX)

<!-- b000304 | references | pages [23] -->
(PAX)

<!-- b000305 | references | pages [23] -->
q0

<!-- b000306 | references | pages [23] -->
0.26

<!-- b000307 | references | pages [23] -->
1.30

<!-- b000308 | references | pages [23] -->
q1

<!-- b000309 | references | pages [23] -->
0.00

<!-- b000310 | references | pages [23] -->
0.00

<!-- b000311 | references | pages [23] -->
0.09

<!-- b000312 | references | pages [23] -->
q2

<!-- b000313 | references | pages [23] -->
0.28

<!-- b000314 | references | pages [23] -->
0.87

<!-- b000315 | references | pages [23] -->
q3

<!-- b000316 | references | pages [23] -->
13.14

<!-- b000317 | references | pages [23] -->
32.70

<!-- b000318 | references | pages [23] -->
Total

<!-- b000319 | references | pages [23] -->
13.68

<!-- b000320 | references | pages [23] -->
34.87

<!-- b000321 | references | pages [23] -->
q0

<!-- b000322 | references | pages [23] -->
1.94

<!-- b000323 | references | pages [23] -->
4.38

<!-- b000324 | references | pages [23] -->
q1

<!-- b000325 | references | pages [23] -->
0.00

<!-- b000326 | references | pages [23] -->
0.00

<!-- b000327 | references | pages [23] -->
0.18

<!-- b000328 | references | pages [23] -->
q2

<!-- b000329 | references | pages [23] -->
0.58

<!-- b000330 | references | pages [23] -->
1.20

<!-- b000331 | references | pages [23] -->
q3

<!-- b000332 | references | pages [23] -->
46.84

<!-- b000333 | references | pages [23] -->
69.45

<!-- b000334 | references | pages [23] -->
Total

<!-- b000335 | references | pages [23] -->
49.36

<!-- b000336 | references | pages [23] -->
75.03

<!-- b000337 | references | pages [23] -->
q0

<!-- b000338 | references | pages [23] -->
136.01

<!-- b000339 | references | pages [23] -->
238.85

<!-- b000340 | references | pages [23] -->
q1

<!-- b000341 | references | pages [23] -->
0.00

<!-- b000342 | references | pages [23] -->
0.00

<!-- b000343 | references | pages [23] -->
0.36

<!-- b000344 | references | pages [23] -->
q2

<!-- b000345 | references | pages [23] -->
0.73

<!-- b000346 | references | pages [23] -->
1.23

<!-- b000347 | references | pages [23] -->
q3

<!-- b000348 | references | pages [23] -->
35.53

<!-- b000349 | references | pages [23] -->
70.90

<!-- b000350 | references | pages [23] -->
Total

<!-- b000351 | references | pages [23] -->
172.27

<!-- b000352 | references | pages [23] -->
310.98

<!-- b000353 | references | pages [23] -->
q0

<!-- b000354 | references | pages [23] -->
892.67

<!-- b000355 | references | pages [23] -->
491.70

<!-- b000356 | references | pages [23] -->
q1

<!-- b000357 | references | pages [23] -->
0.00

<!-- b000358 | references | pages [23] -->
0.00

<!-- b000359 | references | pages [23] -->
0.54

<!-- b000360 | references | pages [23] -->
q2

<!-- b000361 | references | pages [23] -->
0.71

<!-- b000362 | references | pages [23] -->
1.20

<!-- b000363 | references | pages [23] -->
q3

<!-- b000364 | references | pages [23] -->
67.50

<!-- b000365 | references | pages [23] -->
121.87

<!-- b000366 | references | pages [23] -->
Total

<!-- b000367 | references | pages [23] -->
960.85

<!-- b000368 | references | pages [23] -->
614.77

<!-- b000369 | references | pages [23] -->
q0

<!-- b000370 | references | pages [23] -->
2024.50

<!-- b000371 | references | pages [23] -->
1192.34

<!-- b000372 | references | pages [23] -->
q1

<!-- b000373 | references | pages [23] -->
0.69

<!-- b000374 | references | pages [23] -->
0.00

<!-- b000375 | references | pages [23] -->
0.72

<!-- b000376 | references | pages [23] -->
q2

<!-- b000377 | references | pages [23] -->
34.07

<!-- b000378 | references | pages [23] -->
1.19

<!-- b000379 | references | pages [23] -->
q3

<!-- b000380 | references | pages [23] -->
67.10

<!-- b000381 | references | pages [23] -->
67.10

<!-- b000382 | references | pages [23] -->
Total

<!-- b000383 | references | pages [23] -->
2126.36

<!-- b000384 | references | pages [23] -->
1260.63

<!-- b000385 | caption | pages [23] -->
Table 16: WTMD 30%

<!-- b000386 | furniture | pages [24] -->
Team 68942

<!-- b000387 | furniture | pages [24] -->
Page 23 of 36

<!-- b000388 | references | pages [24] -->
Generation

<!-- b000389 | references | pages [24] -->
Average

<!-- b000390 | references | pages [24] -->
Standard Deviation

<!-- b000391 | references | pages [24] -->
Queue

<!-- b000392 | references | pages [24] -->
Probability

<!-- b000393 | references | pages [24] -->
(PAX)

<!-- b000394 | references | pages [24] -->
(PAX)

<!-- b000395 | references | pages [24] -->
q0

<!-- b000396 | references | pages [24] -->
0.55

<!-- b000397 | references | pages [24] -->
2.03

<!-- b000398 | references | pages [24] -->
q1

<!-- b000399 | references | pages [24] -->
0.00

<!-- b000400 | references | pages [24] -->
0.00

<!-- b000401 | references | pages [24] -->
0.09

<!-- b000402 | references | pages [24] -->
q2

<!-- b000403 | references | pages [24] -->
0.44

<!-- b000404 | references | pages [24] -->
1.07

<!-- b000405 | references | pages [24] -->
q3

<!-- b000406 | references | pages [24] -->
12.36

<!-- b000407 | references | pages [24] -->
32.56

<!-- b000408 | references | pages [24] -->
Total

<!-- b000409 | references | pages [24] -->
13.35

<!-- b000410 | references | pages [24] -->
35.66

<!-- b000411 | references | pages [24] -->
q0

<!-- b000412 | references | pages [24] -->
3.17

<!-- b000413 | references | pages [24] -->
7.74

<!-- b000414 | references | pages [24] -->
q1

<!-- b000415 | references | pages [24] -->
0.00

<!-- b000416 | references | pages [24] -->
0.00

<!-- b000417 | references | pages [24] -->
0.18

<!-- b000418 | references | pages [24] -->
q2

<!-- b000419 | references | pages [24] -->
0.67

<!-- b000420 | references | pages [24] -->
1.28

<!-- b000421 | references | pages [24] -->
q3

<!-- b000422 | references | pages [24] -->
42.51

<!-- b000423 | references | pages [24] -->
70.06

<!-- b000424 | references | pages [24] -->
Total

<!-- b000425 | references | pages [24] -->
46.35

<!-- b000426 | references | pages [24] -->
79.08

<!-- b000427 | references | pages [24] -->
q0

<!-- b000428 | references | pages [24] -->
83.75

<!-- b000429 | references | pages [24] -->
154.49

<!-- b000430 | references | pages [24] -->
q1

<!-- b000431 | references | pages [24] -->
0.00

<!-- b000432 | references | pages [24] -->
0.00

<!-- b000433 | references | pages [24] -->
0.36

<!-- b000434 | references | pages [24] -->
q2

<!-- b000435 | references | pages [24] -->
0.70

<!-- b000436 | references | pages [24] -->
1.22

<!-- b000437 | references | pages [24] -->
q3

<!-- b000438 | references | pages [24] -->
48.75

<!-- b000439 | references | pages [24] -->
76.08

<!-- b000440 | references | pages [24] -->
Total

<!-- b000441 | references | pages [24] -->
133.20

<!-- b000442 | references | pages [24] -->
231.79

<!-- b000443 | references | pages [24] -->
q0

<!-- b000444 | references | pages [24] -->
972.72

<!-- b000445 | references | pages [24] -->
565.84

<!-- b000446 | references | pages [24] -->
q1

<!-- b000447 | references | pages [24] -->
0.00

<!-- b000448 | references | pages [24] -->
0.00

<!-- b000449 | references | pages [24] -->
0.54

<!-- b000450 | references | pages [24] -->
q2

<!-- b000451 | references | pages [24] -->
0.70

<!-- b000452 | references | pages [24] -->
1.22

<!-- b000453 | references | pages [24] -->
q3

<!-- b000454 | references | pages [24] -->
29.51

<!-- b000455 | references | pages [24] -->
57.71

<!-- b000456 | references | pages [24] -->
Total

<!-- b000457 | references | pages [24] -->
1002.93

<!-- b000458 | references | pages [24] -->
624.77

<!-- b000459 | references | pages [24] -->
q0

<!-- b000460 | references | pages [24] -->
1998.51

<!-- b000461 | references | pages [24] -->
1158.93

<!-- b000462 | references | pages [24] -->
q1

<!-- b000463 | references | pages [24] -->
0.00

<!-- b000464 | references | pages [24] -->
0.00

<!-- b000465 | references | pages [24] -->
0.72

<!-- b000466 | references | pages [24] -->
q2

<!-- b000467 | references | pages [24] -->
0.72

<!-- b000468 | references | pages [24] -->
1.24

<!-- b000469 | references | pages [24] -->
q3

<!-- b000470 | references | pages [24] -->
38.87

<!-- b000471 | references | pages [24] -->
82.61

<!-- b000472 | references | pages [24] -->
Total

<!-- b000473 | references | pages [24] -->
2038.1

<!-- b000474 | references | pages [24] -->
1242.78

<!-- b000475 | caption | pages [24] -->
Table 17: WTM 40%

<!-- b000476 | references | pages [24] -->
A

<!-- b000477 | references | pages [24] -->
Code

<!-- b000478 | references | pages [24] -->
The following is the code for the NetLogo model used in this paper:

<!-- b000479 | references | pages [24] -->
breed[passengers passenger]

<!-- b000480 | references | pages [24] -->
breed[officers officer]

<!-- b000481 | references | pages [24] -->
breed[xrays xray]

<!-- b000482 | references | pages [24] -->
breed[unpackers unpacker]

<!-- b000483 | references | pages [24] -->
breed[mmscanners mmscanner]

<!-- b000484 | references | pages [24] -->
breed[packers packer]

<!-- b000485 | references | pages [24] -->
undirected-link-breed[id-checks id-check]

<!-- b000486 | references | pages [24] -->
undirected-link-breed[queue-links queue-link]

<!-- b000487 | references | pages [24] -->
undirected-link-breed[unpack-links unpack-link]

<!-- b000488 | references | pages [24] -->
undirected-link-breed[pack-links pack-link]

<!-- b000489 | references | pages [24] -->
undirected-link-breed[scan-links scan-link]

<!-- b000490 | references | pages [24] -->
undirected-link-breed[patdown-links patdown-link]

<!-- b000491 | references | pages [24] -->
globals[

<!-- b000492 | references | pages [24] -->
p0-length ;;precheck document queue length

<!-- b000493 | references | pages [24] -->
n0-length ;;nonprecheck document queue length

<!-- b000494 | references | pages [24] -->
p1-length

<!-- b000495 | furniture | pages [25] -->
Team 68942

<!-- b000496 | furniture | pages [25] -->
Page 24 of 36

<!-- b000497 | references | pages [25] -->
n1-length

<!-- b000498 | references | pages [25] -->
a2-length

<!-- b000499 | references | pages [25] -->
pd-length

<!-- b000500 | references | pages [25] -->
total-passengers

<!-- b000501 | references | pages [25] -->
death-per-10m

<!-- b000502 | references | pages [25] -->
birth-per-10m

<!-- b000503 | references | pages [25] -->
total-wait-queue-p0;before id

<!-- b000504 | references | pages [25] -->
total-wait-queue-n0

<!-- b000505 | references | pages [25] -->
total-wait-queue-p1 ;before unpack

<!-- b000506 | references | pages [25] -->
total-wait-queue-n1

<!-- b000507 | references | pages [25] -->
total-wait-queue-p2 ;before scan

<!-- b000508 | references | pages [25] -->
total-wait-queue-n2

<!-- b000509 | references | pages [25] -->
total-wait-queue-p3 ;before repack

<!-- b000510 | references | pages [25] -->
total-wait-queue-n3

<!-- b000511 | references | pages [25] -->
total-wait-queue-pd ;before patdowns

<!-- b000512 | references | pages [25] -->
total-alive-time

<!-- b000513 | references | pages [25] -->
total-waiting-time

<!-- b000514 | references | pages [25] -->
avg-alive-time

<!-- b000515 | references | pages [25] -->
avg-waiting-time

<!-- b000516 | references | pages [25] -->
stddev-alive-time

<!-- b000517 | references | pages [25] -->
stddev-waiting-time

<!-- b000518 | references | pages [25] -->
avg-queue-p0

<!-- b000519 | references | pages [25] -->
avg-queue-p1

<!-- b000520 | references | pages [25] -->
avg-queue-p2

<!-- b000521 | references | pages [25] -->
avg-queue-p3

<!-- b000522 | references | pages [25] -->
avg-queue-n0

<!-- b000523 | references | pages [25] -->
avg-queue-n1

<!-- b000524 | references | pages [25] -->
avg-queue-n2

<!-- b000525 | references | pages [25] -->
avg-queue-n3

<!-- b000526 | references | pages [25] -->
avg-queue-pd

<!-- b000527 | references | pages [25] -->
stddev-queue-p0

<!-- b000528 | references | pages [25] -->
stddev-queue-p1

<!-- b000529 | references | pages [25] -->
stddev-queue-p2

<!-- b000530 | references | pages [25] -->
stddev-queue-p3

<!-- b000531 | references | pages [25] -->
stddev-queue-n0

<!-- b000532 | references | pages [25] -->
stddev-queue-n1

<!-- b000533 | references | pages [25] -->
stddev-queue-n2

<!-- b000534 | references | pages [25] -->
stddev-queue-n3

<!-- b000535 | references | pages [25] -->
stddev-queue-pd

<!-- b000536 | references | pages [25] -->
all-passengers

<!-- b000537 | references | pages [25] -->
]

<!-- b000538 | references | pages [25] -->
officers-own[

<!-- b000539 | references | pages [25] -->
which-queue

<!-- b000540 | references | pages [25] -->
id

<!-- b000541 | references | pages [25] -->
patters

<!-- b000542 | references | pages [25] -->
]

<!-- b000543 | references | pages [25] -->
unpackers-own[

<!-- b000544 | references | pages [25] -->
which-queue

<!-- b000545 | references | pages [25] -->
active

<!-- b000546 | references | pages [25] -->
]

<!-- b000547 | references | pages [25] -->
packers-own[

<!-- b000548 | furniture | pages [26] -->
Team 68942

<!-- b000549 | furniture | pages [26] -->
Page 25 of 36

<!-- b000550 | references | pages [26] -->
which-queue

<!-- b000551 | references | pages [26] -->
active

<!-- b000552 | references | pages [26] -->
]

<!-- b000553 | references | pages [26] -->
xrays-own[

<!-- b000554 | references | pages [26] -->
which-queue

<!-- b000555 | references | pages [26] -->
active

<!-- b000556 | references | pages [26] -->
]

<!-- b000557 | references | pages [26] -->
mmscanners-own[

<!-- b000558 | references | pages [26] -->
which-queue

<!-- b000559 | references | pages [26] -->
active

<!-- b000560 | references | pages [26] -->
capacity

<!-- b000561 | references | pages [26] -->
]

<!-- b000562 | references | pages [26] -->
passengers-own[

<!-- b000563 | references | pages [26] -->
is-precheck

<!-- b000564 | references | pages [26] -->
baggage

<!-- b000565 | references | pages [26] -->
personal-space

<!-- b000566 | references | pages [26] -->
is-cutter

<!-- b000567 | references | pages [26] -->
waiting-time

<!-- b000568 | references | pages [26] -->
scan-time

<!-- b000569 | references | pages [26] -->
which-queue

<!-- b000570 | references | pages [26] -->
queue-pos

<!-- b000571 | references | pages [26] -->
walking

<!-- b000572 | references | pages [26] -->
is-waiting

<!-- b000573 | references | pages [26] -->
fd-speed

<!-- b000574 | references | pages [26] -->
next-passenger

<!-- b000575 | references | pages [26] -->
p-length

<!-- b000576 | references | pages [26] -->
id-check-length

<!-- b000577 | references | pages [26] -->
unpack-length

<!-- b000578 | references | pages [26] -->
scan-length

<!-- b000579 | references | pages [26] -->
pack-length

<!-- b000580 | references | pages [26] -->
walking-time

<!-- b000581 | references | pages [26] -->
id-check-time

<!-- b000582 | references | pages [26] -->
unpack-time

<!-- b000583 | references | pages [26] -->
pack-time

<!-- b000584 | references | pages [26] -->
patdown-time

<!-- b000585 | references | pages [26] -->
stage

<!-- b000586 | references | pages [26] -->
md-prob

<!-- b000587 | references | pages [26] -->
total-wait-time

<!-- b000588 | references | pages [26] -->
wait-queue-0

<!-- b000589 | references | pages [26] -->
wait-queue-1

<!-- b000590 | references | pages [26] -->
wait-queue-2

<!-- b000591 | references | pages [26] -->
wait-queue-3

<!-- b000592 | references | pages [26] -->
wait-queue-pd

<!-- b000593 | references | pages [26] -->
alive-time

<!-- b000594 | references | pages [26] -->
delayer

<!-- b000595 | references | pages [26] -->
speed-factor

<!-- b000596 | references | pages [26] -->
]

<!-- b000597 | references | pages [26] -->
to setup

<!-- b000598 | references | pages [26] -->
clear-all

<!-- b000599 | references | pages [26] -->
reset-ticks

<!-- b000600 | furniture | pages [27] -->
Team 68942

<!-- b000601 | furniture | pages [27] -->
Page 26 of 36

<!-- b000602 | references | pages [27] -->
setup-globals

<!-- b000603 | references | pages [27] -->
setup-zones

<!-- b000604 | references | pages [27] -->
setup-decor

<!-- b000605 | references | pages [27] -->
let i 0

<!-- b000606 | references | pages [27] -->
let t num-precheck-id + num-normal-id

<!-- b000607 | references | pages [27] -->
create-officers t[

<!-- b000608 | references | pages [27] -->
set shape "Officer"

<!-- b000609 | references | pages [27] -->
set patters false

<!-- b000610 | references | pages [27] -->
set id i

<!-- b000611 | references | pages [27] -->
set i i + 1

<!-- b000612 | references | pages [27] -->
set color 27

<!-- b000613 | references | pages [27] -->
set size 2.5

<!-- b000614 | references | pages [27] -->
setxy (id * (60 / t)) mod 60 + ((60 / t) / 2) 45

<!-- b000615 | references | pages [27] -->
ifelse id < num-precheck-id[

<!-- b000616 | references | pages [27] -->
set which-queue 0

<!-- b000617 | references | pages [27] -->
][

<!-- b000618 | references | pages [27] -->
set which-queue 1

<!-- b000619 | references | pages [27] -->
]

<!-- b000620 | references | pages [27] -->
]

<!-- b000621 | references | pages [27] -->
set i 0

<!-- b000622 | references | pages [27] -->
create-officers 1[

<!-- b000623 | references | pages [27] -->
set shape "Officer"

<!-- b000624 | references | pages [27] -->
set patters true

<!-- b000625 | references | pages [27] -->
set color 27

<!-- b000626 | references | pages [27] -->
set size 2.5

<!-- b000627 | references | pages [27] -->
setxy (i * 3) + 41 3

<!-- b000628 | references | pages [27] -->
set which-queue i

<!-- b000629 | references | pages [27] -->
set i i + 1

<!-- b000630 | references | pages [27] -->
]

<!-- b000631 | references | pages [27] -->
set birth-per-10m []

<!-- b000632 | references | pages [27] -->
set death-per-10m []

<!-- b000633 | references | pages [27] -->
end

<!-- b000634 | references | pages [27] -->
to go

<!-- b000635 | references | pages [27] -->
if ticks mod 600 = 0[

<!-- b000636 | references | pages [27] -->
set birth-per-10m lput 0 birth-per-10m

<!-- b000637 | references | pages [27] -->
set death-per-10m lput 0 death-per-10m

<!-- b000638 | references | pages [27] -->
]

<!-- b000639 | references | pages [27] -->
if ticks = 0[make-passenger]

<!-- b000640 | references | pages [27] -->
if random 100 < gen-prob and ticks < 3600[make-passenger]

<!-- b000641 | references | pages [27] -->
increment-queues ;; each officer calls the front of the queue

<!-- b000642 | references | pages [27] -->
if count passengers = 0[

<!-- b000643 | references | pages [27] -->
process-data

<!-- b000644 | references | pages [27] -->
stop

<!-- b000645 | references | pages [27] -->
]

<!-- b000646 | references | pages [27] -->
ask passengers[

<!-- b000647 | references | pages [27] -->
set is-waiting true

<!-- b000648 | references | pages [27] -->
if stage = 0 and walking-time = int(2 * speed-factor)[

<!-- b000649 | references | pages [27] -->
set walking false

<!-- b000650 | references | pages [27] -->
set is-waiting false

<!-- b000651 | references | pages [27] -->
]

<!-- b000652 | references | pages [27] -->
if stage = 1 and walking-time = int(3 * speed-factor)[

<!-- b000653 | references | pages [27] -->
set walking false

<!-- b000654 | references | pages [27] -->
set stage 2

<!-- b000655 | furniture | pages [28] -->
Team 68942

<!-- b000656 | furniture | pages [28] -->
Page 27 of 36

<!-- b000657 | references | pages [28] -->
set is-waiting false

<!-- b000658 | references | pages [28] -->
]

<!-- b000659 | references | pages [28] -->
if stage = 3 and walking-time = int(3 * speed-factor)[

<!-- b000660 | references | pages [28] -->
set walking false

<!-- b000661 | references | pages [28] -->
set stage 4

<!-- b000662 | references | pages [28] -->
set is-waiting false

<!-- b000663 | references | pages [28] -->
]

<!-- b000664 | references | pages [28] -->
if stage = 4 and walking-time = int(2 * speed-factor)[

<!-- b000665 | references | pages [28] -->
set walking false

<!-- b000666 | references | pages [28] -->
set is-waiting false

<!-- b000667 | references | pages [28] -->
]

<!-- b000668 | references | pages [28] -->
if stage = 7 and walking-time = int(3 * speed-factor)[

<!-- b000669 | references | pages [28] -->
set walking false

<!-- b000670 | references | pages [28] -->
set stage 8

<!-- b000671 | references | pages [28] -->
set is-waiting false

<!-- b000672 | references | pages [28] -->
]

<!-- b000673 | references | pages [28] -->
if stage = 9[

<!-- b000674 | references | pages [28] -->
set is-waiting false

<!-- b000675 | references | pages [28] -->
facexy xcor ycor - 1

<!-- b000676 | references | pages [28] -->
fd 1

<!-- b000677 | references | pages [28] -->
if [pycor] of patch-here = 0[record-data]

<!-- b000678 | references | pages [28] -->
]

<!-- b000679 | references | pages [28] -->
if stage = 201 and walking-time = int(3 * speed-factor)[

<!-- b000680 | references | pages [28] -->
set walking false

<!-- b000681 | references | pages [28] -->
set is-waiting false

<!-- b000682 | references | pages [28] -->
]

<!-- b000683 | references | pages [28] -->
if walking[

<!-- b000684 | references | pages [28] -->
fd fd-speed

<!-- b000685 | references | pages [28] -->
set walking-time walking-time + 1

<!-- b000686 | references | pages [28] -->
set is-waiting false

<!-- b000687 | references | pages [28] -->
]

<!-- b000688 | references | pages [28] -->
if stage = 0 and id-check-time >= id-check-length[

<!-- b000689 | references | pages [28] -->
find-lane

<!-- b000690 | references | pages [28] -->
set id-check-time id-check-time + 1

<!-- b000691 | references | pages [28] -->
set is-waiting false

<!-- b000692 | references | pages [28] -->
]

<!-- b000693 | references | pages [28] -->
if count my-id-checks = 1[

<!-- b000694 | references | pages [28] -->
set id-check-time id-check-time + 1

<!-- b000695 | references | pages [28] -->
set is-waiting false

<!-- b000696 | references | pages [28] -->
]

<!-- b000697 | references | pages [28] -->
if (unpack-time = int(15 * speed-factor) and not(is-precheck) or (unpack-time = int(7 * speed-factor

<!-- b000698 | references | pages [28] -->
ask my-links[die]

<!-- b000699 | references | pages [28] -->
through-security

<!-- b000700 | references | pages [28] -->
set unpack-time unpack-time + 1

<!-- b000701 | references | pages [28] -->
set is-waiting false

<!-- b000702 | references | pages [28] -->
]

<!-- b000703 | references | pages [28] -->
if stage = 8 and (pack-time >= int(10 * speed-factor) and not(is-precheck) or (pack-time >= int(5 *

<!-- b000704 | references | pages [28] -->
ask my-links[die]

<!-- b000705 | references | pages [28] -->
set pack-time pack-time + 1

<!-- b000706 | references | pages [28] -->
ifelse random 100 < rescreen-prob[

<!-- b000707 | references | pages [28] -->
set stage 100

<!-- b000708 | references | pages [28] -->
set patdown-time 0

<!-- b000709 | references | pages [28] -->
set p-length rescreen-length

<!-- b000710 | references | pages [28] -->
set is-waiting false

<!-- b000711 | furniture | pages [29] -->
Team 68942

<!-- b000712 | furniture | pages [29] -->
Page 28 of 36

<!-- b000713 | references | pages [29] -->
if delay-on [set delayer random 5 + 5]

<!-- b000714 | references | pages [29] -->
patdown

<!-- b000715 | references | pages [29] -->
][

<!-- b000716 | references | pages [29] -->
set is-waiting false

<!-- b000717 | references | pages [29] -->
set stage 9

<!-- b000718 | references | pages [29] -->
]

<!-- b000719 | references | pages [29] -->
]

<!-- b000720 | references | pages [29] -->
if patdown-time = int(p-length * speed-factor) and stage = 201[

<!-- b000721 | references | pages [29] -->
;show "This happens!"

<!-- b000722 | references | pages [29] -->
set is-waiting false

<!-- b000723 | references | pages [29] -->
ask my-links[die]

<!-- b000724 | references | pages [29] -->
set stage 5

<!-- b000725 | references | pages [29] -->
set patdown-time patdown-time + 1

<!-- b000726 | references | pages [29] -->
ifelse p-length = patdown-length[

<!-- b000727 | references | pages [29] -->
repack

<!-- b000728 | references | pages [29] -->
][

<!-- b000729 | references | pages [29] -->
set is-waiting false

<!-- b000730 | references | pages [29] -->
set stage 9

<!-- b000731 | references | pages [29] -->
]

<!-- b000732 | references | pages [29] -->
]

<!-- b000733 | references | pages [29] -->
if stage = 4 and ((md-prob and scan-time = 1) or (not(md-prob) and scan-time >= scan-length))[

<!-- b000734 | references | pages [29] -->
set is-waiting false

<!-- b000735 | references | pages [29] -->
;show "This other thing happens!"

<!-- b000736 | references | pages [29] -->
ifelse random 100 < patdown-prob[

<!-- b000737 | references | pages [29] -->
set stage 200

<!-- b000738 | references | pages [29] -->
set p-length patdown-length

<!-- b000739 | references | pages [29] -->
set patdown-time 0

<!-- b000740 | references | pages [29] -->
patdown

<!-- b000741 | references | pages [29] -->
][

<!-- b000742 | references | pages [29] -->
set stage 5

<!-- b000743 | references | pages [29] -->
repack

<!-- b000744 | references | pages [29] -->
]

<!-- b000745 | references | pages [29] -->
set scan-time scan-time + 1

<!-- b000746 | references | pages [29] -->
]

<!-- b000747 | references | pages [29] -->
if count my-unpack-links = 1[

<!-- b000748 | references | pages [29] -->
set is-waiting false

<!-- b000749 | references | pages [29] -->
set unpack-time unpack-time + 1

<!-- b000750 | references | pages [29] -->
]

<!-- b000751 | references | pages [29] -->
if count my-scan-links = 1 and walking = false[

<!-- b000752 | references | pages [29] -->
set is-waiting false

<!-- b000753 | references | pages [29] -->
set scan-time scan-time + 1

<!-- b000754 | references | pages [29] -->
]

<!-- b000755 | references | pages [29] -->
if count my-pack-links = 1[

<!-- b000756 | references | pages [29] -->
set is-waiting false

<!-- b000757 | references | pages [29] -->
set pack-time pack-time + 1

<!-- b000758 | references | pages [29] -->
]

<!-- b000759 | references | pages [29] -->
if count my-patdown-links = 1[

<!-- b000760 | references | pages [29] -->
set is-waiting false

<!-- b000761 | references | pages [29] -->
set patdown-time patdown-time + 1

<!-- b000762 | references | pages [29] -->
]

<!-- b000763 | references | pages [29] -->
if is-waiting[

<!-- b000764 | references | pages [29] -->
ifelse stage = 0[set wait-queue-0 wait-queue-0 + 1][

<!-- b000765 | references | pages [29] -->
ifelse stage = 2[set wait-queue-1 wait-queue-1 + 1][

<!-- b000766 | references | pages [29] -->
ifelse stage = 4[set wait-queue-2 wait-queue-2 + 1][

<!-- b000767 | furniture | pages [30] -->
Team 68942

<!-- b000768 | furniture | pages [30] -->
Page 29 of 36

<!-- b000769 | references | pages [30] -->
ifelse stage = 8[set wait-queue-3 wait-queue-3 + 1][

<!-- b000770 | references | pages [30] -->
show stage]]]]

<!-- b000771 | references | pages [30] -->
if stage = 201[

<!-- b000772 | references | pages [30] -->
set wait-queue-pd wait-queue-pd + 1

<!-- b000773 | references | pages [30] -->
set delayer delayer - 1

<!-- b000774 | references | pages [30] -->
]

<!-- b000775 | references | pages [30] -->
;show stage

<!-- b000776 | references | pages [30] -->
set waiting-time waiting-time + 1

<!-- b000777 | references | pages [30] -->
]

<!-- b000778 | references | pages [30] -->
set alive-time alive-time + 1

<!-- b000779 | references | pages [30] -->
]

<!-- b000780 | references | pages [30] -->
tick

<!-- b000781 | references | pages [30] -->
end

<!-- b000782 | references | pages [30] -->
to setup-zones

<!-- b000783 | references | pages [30] -->
let t num-precheck-id + num-normal-id

<!-- b000784 | references | pages [30] -->
ask patches[

<!-- b000785 | references | pages [30] -->
ifelse pycor > 45[

<!-- b000786 | references | pages [30] -->
ifelse pxcor < 60 * (num-precheck-id / t)[

<!-- b000787 | references | pages [30] -->
set pcolor blue + 1

<!-- b000788 | references | pages [30] -->
][

<!-- b000789 | references | pages [30] -->
set pcolor blue - 2

<!-- b000790 | references | pages [30] -->
]

<!-- b000791 | references | pages [30] -->
][

<!-- b000792 | references | pages [30] -->
ifelse pycor > 10[

<!-- b000793 | references | pages [30] -->
ifelse pxcor < 20[

<!-- b000794 | references | pages [30] -->
set pcolor white - 2

<!-- b000795 | references | pages [30] -->
][

<!-- b000796 | references | pages [30] -->
set pcolor white

<!-- b000797 | references | pages [30] -->
]

<!-- b000798 | references | pages [30] -->
][

<!-- b000799 | references | pages [30] -->
ifelse pxcor > 40 and pycor < 6[

<!-- b000800 | references | pages [30] -->
set pcolor red

<!-- b000801 | references | pages [30] -->
][

<!-- b000802 | references | pages [30] -->
set pcolor green

<!-- b000803 | references | pages [30] -->
]

<!-- b000804 | references | pages [30] -->
]

<!-- b000805 | references | pages [30] -->
]

<!-- b000806 | references | pages [30] -->
]

<!-- b000807 | references | pages [30] -->
end

<!-- b000808 | references | pages [30] -->
to setup-decor

<!-- b000809 | references | pages [30] -->
ask patches[

<!-- b000810 | references | pages [30] -->
if pycor < 40 and pycor > 8 and (

<!-- b000811 | references | pages [30] -->
(pxcor > 0 and pxcor < 4) or

<!-- b000812 | references | pages [30] -->
(pxcor > 15 and pxcor < 19) or

<!-- b000813 | references | pages [30] -->
(pxcor > 20 and pxcor < 24) or

<!-- b000814 | references | pages [30] -->
(pxcor > 35 and pxcor < 39) or

<!-- b000815 | references | pages [30] -->
(pxcor > 40 and pxcor < 44) or

<!-- b000816 | references | pages [30] -->
(pxcor > 55 and pxcor < 59)

<!-- b000817 | references | pages [30] -->
)[

<!-- b000818 | references | pages [30] -->
set pcolor 36

<!-- b000819 | references | pages [30] -->
]

<!-- b000820 | references | pages [30] -->
]

<!-- b000821 | furniture | pages [31] -->
Team 68942

<!-- b000822 | furniture | pages [31] -->
Page 30 of 36

<!-- b000823 | references | pages [31] -->
let i 0

<!-- b000824 | references | pages [31] -->
create-xrays 3[

<!-- b000825 | references | pages [31] -->
set shape "rectangle"

<!-- b000826 | references | pages [31] -->
setxy i * 20 + 12 30

<!-- b000827 | references | pages [31] -->
facexy xcor ycor + 1

<!-- b000828 | references | pages [31] -->
set size 5

<!-- b000829 | references | pages [31] -->
set color yellow

<!-- b000830 | references | pages [31] -->
set which-queue i

<!-- b000831 | references | pages [31] -->
set active true

<!-- b000832 | references | pages [31] -->
set i i + 1

<!-- b000833 | references | pages [31] -->
]

<!-- b000834 | references | pages [31] -->
set i 0

<!-- b000835 | references | pages [31] -->
create-mmscanners 3[

<!-- b000836 | references | pages [31] -->
set shape "hex"

<!-- b000837 | references | pages [31] -->
ifelse i = 1 and mmscanner-extra-capacity[

<!-- b000838 | references | pages [31] -->
set capacity 2

<!-- b000839 | references | pages [31] -->
][

<!-- b000840 | references | pages [31] -->
set capacity 1

<!-- b000841 | references | pages [31] -->
]

<!-- b000842 | references | pages [31] -->
setxy i * 20 + 6.5 28

<!-- b000843 | references | pages [31] -->
facexy xcor ycor + 1

<!-- b000844 | references | pages [31] -->
set size 5

<!-- b000845 | references | pages [31] -->
set color red - 1

<!-- b000846 | references | pages [31] -->
set which-queue i

<!-- b000847 | references | pages [31] -->
set i i + 1

<!-- b000848 | references | pages [31] -->
set active true

<!-- b000849 | references | pages [31] -->
]

<!-- b000850 | references | pages [31] -->
set i 0

<!-- b000851 | references | pages [31] -->
let p [2 17 22 37 42 57]

<!-- b000852 | references | pages [31] -->
create-unpackers 6[

<!-- b000853 | references | pages [31] -->
set shape "circle"

<!-- b000854 | references | pages [31] -->
setxy item i p 35

<!-- b000855 | references | pages [31] -->
set size 2

<!-- b000856 | references | pages [31] -->
set color 34

<!-- b000857 | references | pages [31] -->
set which-queue i

<!-- b000858 | references | pages [31] -->
set i i + 1

<!-- b000859 | references | pages [31] -->
set active true

<!-- b000860 | references | pages [31] -->
]

<!-- b000861 | references | pages [31] -->
set i 0

<!-- b000862 | references | pages [31] -->
create-packers 6[

<!-- b000863 | references | pages [31] -->
set shape "circle"

<!-- b000864 | references | pages [31] -->
setxy item i p 15

<!-- b000865 | references | pages [31] -->
set size 2

<!-- b000866 | references | pages [31] -->
set color 34

<!-- b000867 | references | pages [31] -->
set which-queue i

<!-- b000868 | references | pages [31] -->
set i i + 1

<!-- b000869 | references | pages [31] -->
set active true

<!-- b000870 | references | pages [31] -->
]

<!-- b000871 | references | pages [31] -->
end

<!-- b000872 | references | pages [31] -->
to setup-globals

<!-- b000873 | references | pages [31] -->
set p0-length 0

<!-- b000874 | references | pages [31] -->
set n0-length 0

<!-- b000875 | furniture | pages [32] -->
Team 68942

<!-- b000876 | furniture | pages [32] -->
Page 31 of 36

<!-- b000877 | references | pages [32] -->
set p1-length n-values num-precheck-lanes [0]

<!-- b000878 | references | pages [32] -->
set n1-length n-values num-normal-lanes [0]

<!-- b000879 | references | pages [32] -->
set a2-length n-values ((num-precheck-lanes + num-normal-lanes + 2) / 2) [0]

<!-- b000880 | references | pages [32] -->
set pd-length n-values (num-precheck-lanes + num-normal-lanes + 2) [0]

<!-- b000881 | references | pages [32] -->
set total-wait-queue-p0 [];before id

<!-- b000882 | references | pages [32] -->
set total-wait-queue-n0 []

<!-- b000883 | references | pages [32] -->
set total-wait-queue-p1 [];before unpack

<!-- b000884 | references | pages [32] -->
set total-wait-queue-n1 []

<!-- b000885 | references | pages [32] -->
set total-wait-queue-p2 [];before scan

<!-- b000886 | references | pages [32] -->
set total-wait-queue-n2 []

<!-- b000887 | references | pages [32] -->
set total-wait-queue-p3 [];before repack

<!-- b000888 | references | pages [32] -->
set total-wait-queue-n3 []

<!-- b000889 | references | pages [32] -->
set total-wait-queue-pd [] ;before patdowns

<!-- b000890 | references | pages [32] -->
set total-alive-time []

<!-- b000891 | references | pages [32] -->
set total-waiting-time []

<!-- b000892 | references | pages [32] -->
end

<!-- b000893 | references | pages [32] -->
to increment-queues

<!-- b000894 | references | pages [32] -->
ask officers with [not(patters)][

<!-- b000895 | references | pages [32] -->
let p-in-queue (passengers with [walking = false and id-check-time = 0 and which-queue = [which-queu

<!-- b000896 | references | pages [32] -->
if count p-in-queue >= 1 and count my-links = 0[

<!-- b000897 | references | pages [32] -->
ask min-one-of p-in-queue [queue-pos][

<!-- b000898 | references | pages [32] -->
face myself

<!-- b000899 | references | pages [32] -->
set fd-speed (distancexy [xcor] of myself [ycor] of myself - 1) / 2

<!-- b000900 | references | pages [32] -->
create-id-check-with myself

<!-- b000901 | references | pages [32] -->
set walking true

<!-- b000902 | references | pages [32] -->
]

<!-- b000903 | references | pages [32] -->
]

<!-- b000904 | references | pages [32] -->
]

<!-- b000905 | references | pages [32] -->
ask unpackers with [active][

<!-- b000906 | references | pages [32] -->
let p-in-queue (passengers with [stage = 2 and walking = false and which-queue = [which-queue] of my

<!-- b000907 | references | pages [32] -->
;show p-in-queue

<!-- b000908 | references | pages [32] -->
if count p-in-queue >= 1[

<!-- b000909 | references | pages [32] -->
ask p-in-queue[

<!-- b000910 | references | pages [32] -->
if (count p-in-queue < unpack-capacity + personal-space) or (member? self (min-n-of (unpack-capa

<!-- b000911 | references | pages [32] -->
create-unpack-link-with myself

<!-- b000912 | references | pages [32] -->
]

<!-- b000913 | references | pages [32] -->
]

<!-- b000914 | references | pages [32] -->
]

<!-- b000915 | references | pages [32] -->
]

<!-- b000916 | references | pages [32] -->
ask mmscanners with [active][

<!-- b000917 | references | pages [32] -->
let p-in-queue (passengers with [stage = 4 and walking = false and int(which-queue / 2) = [which-que

<!-- b000918 | references | pages [32] -->
if count p-in-queue >= 1 and count my-links <= capacity - 1[

<!-- b000919 | references | pages [32] -->
ask min-one-of p-in-queue [queue-pos][

<!-- b000920 | references | pages [32] -->
face myself

<!-- b000921 | references | pages [32] -->
set fd-speed (distancexy [xcor] of myself [ycor] of myself) / 2

<!-- b000922 | references | pages [32] -->
create-scan-link-with myself

<!-- b000923 | references | pages [32] -->
set walking-time 0

<!-- b000924 | references | pages [32] -->
set walking true

<!-- b000925 | references | pages [32] -->
]

<!-- b000926 | references | pages [32] -->
]

<!-- b000927 | references | pages [32] -->
]

<!-- b000928 | references | pages [32] -->
ask xrays with [active][

<!-- b000929 | references | pages [32] -->
let p-in-queue (passengers with [stage = 4 and walking = false and int(which-queue / 2) = [which-que

<!-- b000930 | furniture | pages [33] -->
Team 68942

<!-- b000931 | furniture | pages [33] -->
Page 32 of 36

<!-- b000932 | references | pages [33] -->
if count p-in-queue >= 1 and (count my-links = 0 or (extra-md and count my-links = 1 and which-queue

<!-- b000933 | references | pages [33] -->
ask min-one-of p-in-queue [queue-pos][

<!-- b000934 | references | pages [33] -->
face myself

<!-- b000935 | references | pages [33] -->
set fd-speed (distancexy [xcor] of myself [ycor] of myself) / 2

<!-- b000936 | references | pages [33] -->
create-scan-link-with myself

<!-- b000937 | references | pages [33] -->
set walking-time 0

<!-- b000938 | references | pages [33] -->
set walking true

<!-- b000939 | references | pages [33] -->
]

<!-- b000940 | references | pages [33] -->
]

<!-- b000941 | references | pages [33] -->
]

<!-- b000942 | references | pages [33] -->
ask packers with [active and count passengers with [stage = 201 and delayer <= 0 and which-queue = [wh

<!-- b000943 | references | pages [33] -->
let p-in-queue (passengers with [stage = 8 and walking = false and which-queue = [which-queue] of my

<!-- b000944 | references | pages [33] -->
;show p-in-queue

<!-- b000945 | references | pages [33] -->
if count p-in-queue >= 1[

<!-- b000946 | references | pages [33] -->
ask p-in-queue[

<!-- b000947 | references | pages [33] -->
if (count p-in-queue < repack-capacity + personal-space) or (member? self (min-n-of (repack-capa

<!-- b000948 | references | pages [33] -->
create-pack-link-with myself

<!-- b000949 | references | pages [33] -->
]

<!-- b000950 | references | pages [33] -->
]

<!-- b000951 | references | pages [33] -->
]

<!-- b000952 | references | pages [33] -->
]

<!-- b000953 | references | pages [33] -->
ask officers with [patters][

<!-- b000954 | references | pages [33] -->
let p-in-queue (passengers with [stage = 201 and walking = false])

<!-- b000955 | references | pages [33] -->
if count p-in-queue >= 1 and count my-links < 6[

<!-- b000956 | references | pages [33] -->
ask p-in-queue[

<!-- b000957 | references | pages [33] -->
if (count p-in-queue < 6) or (member? self (min-n-of 6 p-in-queue [queue-pos]))[

<!-- b000958 | references | pages [33] -->
create-patdown-link-with myself

<!-- b000959 | references | pages [33] -->
]

<!-- b000960 | references | pages [33] -->
]

<!-- b000961 | references | pages [33] -->
]

<!-- b000962 | references | pages [33] -->
]

<!-- b000963 | references | pages [33] -->
end

<!-- b000964 | references | pages [33] -->
to make-passenger

<!-- b000965 | references | pages [33] -->
set birth-per-10m replace-item (length birth-per-10m - 1) birth-per-10m ((last birth-per-10m) + 1)

<!-- b000966 | references | pages [33] -->
create-passengers 1[

<!-- b000967 | references | pages [33] -->
set shape "person"

<!-- b000968 | references | pages [33] -->
set color 115

<!-- b000969 | references | pages [33] -->
set size 2.5

<!-- b000970 | references | pages [33] -->
set is-precheck random 100 < precheck-percentage

<!-- b000971 | references | pages [33] -->
set walking false

<!-- b000972 | references | pages [33] -->
set p-length 10000000

<!-- b000973 | references | pages [33] -->
set queue-pos -1

<!-- b000974 | references | pages [33] -->
ifelse random 100 < 20[

<!-- b000975 | references | pages [33] -->
set personal-space 0

<!-- b000976 | references | pages [33] -->
][

<!-- b000977 | references | pages [33] -->
ifelse random 100 < 50[

<!-- b000978 | references | pages [33] -->
set personal-space 1

<!-- b000979 | references | pages [33] -->
][

<!-- b000980 | references | pages [33] -->
set personal-space 2

<!-- b000981 | references | pages [33] -->
]

<!-- b000982 | references | pages [33] -->
]

<!-- b000983 | references | pages [33] -->
set id-check-length random-normal 11.21 3.79

<!-- b000984 | references | pages [33] -->
set scan-length random-normal 10.47 3.06

<!-- b000985 | furniture | pages [34] -->
Team 68942

<!-- b000986 | furniture | pages [34] -->
Page 33 of 36

<!-- b000987 | references | pages [34] -->
set delayer 0

<!-- b000988 | references | pages [34] -->
set is-cutter random 100 < cutter-percentage

<!-- b000989 | references | pages [34] -->
set speed-factor 1

<!-- b000990 | references | pages [34] -->
if random 100 < slow-percent[set speed-factor slow-factor]

<!-- b000991 | references | pages [34] -->
ifelse is-precheck[

<!-- b000992 | references | pages [34] -->
set color 135

<!-- b000993 | references | pages [34] -->
set which-queue 0

<!-- b000994 | references | pages [34] -->
set md-prob true

<!-- b000995 | references | pages [34] -->
setxy (random 30) + size / 2 max-pycor - size / 2

<!-- b000996 | references | pages [34] -->
;if p0-length != 0[

<!-- b000997 | references | pages [34] -->
;

<!-- b000998 | references | pages [34] -->
set next-passenger one-of passengers with [queue-pos = p0-length and which-queue = [which-queue

<!-- b000999 | references | pages [34] -->
;

<!-- b001000 | references | pages [34] -->
create-queue-link-with next-passenger[set color black]

<!-- b001001 | references | pages [34] -->
;]

<!-- b001002 | references | pages [34] -->
set p0-length p0-length + 1

<!-- b001003 | references | pages [34] -->
;show p0-length

<!-- b001004 | references | pages [34] -->
set queue-pos p0-length

<!-- b001005 | references | pages [34] -->
][

<!-- b001006 | references | pages [34] -->
set which-queue 1

<!-- b001007 | references | pages [34] -->
set md-prob random 100 < metal-detector-prob

<!-- b001008 | references | pages [34] -->
setxy (random 30) + 30 max-pycor - size / 2

<!-- b001009 | references | pages [34] -->
;if n0-length != 0[

<!-- b001010 | references | pages [34] -->
;

<!-- b001011 | references | pages [34] -->
set next-passenger one-of passengers with [queue-pos = n0-length and which-queue = [which-queue

<!-- b001012 | references | pages [34] -->
;

<!-- b001013 | references | pages [34] -->
create-queue-link-with next-passenger[set color black]

<!-- b001014 | references | pages [34] -->
;]

<!-- b001015 | references | pages [34] -->
set n0-length n0-length + 1

<!-- b001016 | references | pages [34] -->
;show n0-length

<!-- b001017 | references | pages [34] -->
set queue-pos n0-length

<!-- b001018 | references | pages [34] -->
]

<!-- b001019 | references | pages [34] -->
;show next-passenger

<!-- b001020 | references | pages [34] -->
]

<!-- b001021 | references | pages [34] -->
set total-passengers total-passengers + 1

<!-- b001022 | references | pages [34] -->
end

<!-- b001023 | references | pages [34] -->
to find-lane

<!-- b001024 | references | pages [34] -->
ask my-links[die]

<!-- b001025 | references | pages [34] -->
; join queue - represented by stage 1

<!-- b001026 | references | pages [34] -->
ifelse is-precheck[

<!-- b001027 | references | pages [34] -->
set which-queue (position min p1-length p1-length)

<!-- b001028 | references | pages [34] -->
ifelse is-cutter and random 100 < cutting-prob[

<!-- b001029 | references | pages [34] -->
set queue-pos 0

<!-- b001030 | references | pages [34] -->
][

<!-- b001031 | references | pages [34] -->
set queue-pos item which-queue p1-length

<!-- b001032 | references | pages [34] -->
]

<!-- b001033 | references | pages [34] -->
set p0-length p0-length - 1

<!-- b001034 | references | pages [34] -->
set p1-length replace-item (which-queue) p1-length (min p1-length + 1)

<!-- b001035 | references | pages [34] -->
;show p1-length

<!-- b001036 | references | pages [34] -->
][

<!-- b001037 | references | pages [34] -->
set n0-length n0-length - 1

<!-- b001038 | references | pages [34] -->
set which-queue (position min n1-length n1-length)

<!-- b001039 | references | pages [34] -->
ifelse is-cutter and random 100 < cutting-prob[

<!-- b001040 | references | pages [34] -->
set queue-pos 0

<!-- b001041 | references | pages [34] -->
][

<!-- b001042 | references | pages [34] -->
set queue-pos item which-queue n1-length

<!-- b001043 | references | pages [34] -->
]

<!-- b001044 | furniture | pages [35] -->
Team 68942

<!-- b001045 | furniture | pages [35] -->
Page 34 of 36

<!-- b001046 | references | pages [35] -->
set n1-length replace-item (which-queue) n1-length (min n1-length + 1)

<!-- b001047 | references | pages [35] -->
;show n1-length

<!-- b001048 | references | pages [35] -->
]

<!-- b001049 | references | pages [35] -->
let p [5 15 25 35 45 55]

<!-- b001050 | references | pages [35] -->
if not(is-precheck)[set which-queue which-queue + num-precheck-lanes]

<!-- b001051 | references | pages [35] -->
facexy (item which-queue p) (37 + queue-pos * .3)

<!-- b001052 | references | pages [35] -->
set fd-speed (distancexy (item which-queue p) (37 + queue-pos * .3)) / (3 * speed-factor)

<!-- b001053 | references | pages [35] -->
;show fd-speed

<!-- b001054 | references | pages [35] -->
set stage stage + 1

<!-- b001055 | references | pages [35] -->
set walking-time 0

<!-- b001056 | references | pages [35] -->
set walking true

<!-- b001057 | references | pages [35] -->
end

<!-- b001058 | references | pages [35] -->
to through-security

<!-- b001059 | references | pages [35] -->
ask my-links[die]

<!-- b001060 | references | pages [35] -->
; join queue - represented by stage 3

<!-- b001061 | references | pages [35] -->
set stage 3

<!-- b001062 | references | pages [35] -->
if random 100 < cant-scan[

<!-- b001063 | references | pages [35] -->
set patdown-time 0

<!-- b001064 | references | pages [35] -->
set p-length rescreen-length

<!-- b001065 | references | pages [35] -->
set is-waiting false

<!-- b001066 | references | pages [35] -->
if delay-on [set delayer random 5 + 5]

<!-- b001067 | references | pages [35] -->
patdown

<!-- b001068 | references | pages [35] -->
]

<!-- b001069 | references | pages [35] -->
ifelse is-precheck[

<!-- b001070 | references | pages [35] -->
set p1-length replace-item (which-queue) p1-length (item which-queue p1-length - 1)

<!-- b001071 | references | pages [35] -->
ifelse is-cutter and random 100 < cutting-prob[

<!-- b001072 | references | pages [35] -->
set queue-pos 0

<!-- b001073 | references | pages [35] -->
][

<!-- b001074 | references | pages [35] -->
set queue-pos item int(which-queue / 2) a2-length

<!-- b001075 | references | pages [35] -->
]

<!-- b001076 | references | pages [35] -->
set a2-length replace-item (int(which-queue / 2)) a2-length (queue-pos + 1)

<!-- b001077 | references | pages [35] -->
;show a2-length

<!-- b001078 | references | pages [35] -->
][

<!-- b001079 | references | pages [35] -->
set n1-length replace-item (which-queue - num-precheck-lanes) n1-length ((item (which-queue - num-pr

<!-- b001080 | references | pages [35] -->
ifelse is-cutter and random 100 < cutting-prob[

<!-- b001081 | references | pages [35] -->
set queue-pos 0

<!-- b001082 | references | pages [35] -->
][

<!-- b001083 | references | pages [35] -->
set queue-pos item int(which-queue / 2) a2-length

<!-- b001084 | references | pages [35] -->
]

<!-- b001085 | references | pages [35] -->
set a2-length replace-item (int(which-queue / 2)) a2-length (queue-pos + 1)

<!-- b001086 | references | pages [35] -->
;show a2-length

<!-- b001087 | references | pages [35] -->
]

<!-- b001088 | references | pages [35] -->
let p [8 28 48]

<!-- b001089 | references | pages [35] -->
facexy (item int(which-queue / 2) p) (33 + queue-pos * .3)

<!-- b001090 | references | pages [35] -->
set fd-speed (distancexy (item int(which-queue / 2) p) (33 + queue-pos * .3)) / int(3 * speed-factor)

<!-- b001091 | references | pages [35] -->
set walking-time 0

<!-- b001092 | references | pages [35] -->
set walking true

<!-- b001093 | references | pages [35] -->
end

<!-- b001094 | references | pages [35] -->
to repack

<!-- b001095 | references | pages [35] -->
; join queue - represented by stage 7

<!-- b001096 | references | pages [35] -->
ask my-links[die]

<!-- b001097 | furniture | pages [36] -->
Team 68942

<!-- b001098 | furniture | pages [36] -->
Page 35 of 36

<!-- b001099 | references | pages [36] -->
set stage 6

<!-- b001100 | references | pages [36] -->
let p [5 15 25 35 45 55]

<!-- b001101 | references | pages [36] -->
facexy (item which-queue p) (15) ; once was (15 + queue-pos * .3)

<!-- b001102 | references | pages [36] -->
set fd-speed (distancexy (item which-queue p) (15)) / int(3 * slow-factor)

<!-- b001103 | references | pages [36] -->
;show fd-speed

<!-- b001104 | references | pages [36] -->
set stage stage + 1

<!-- b001105 | references | pages [36] -->
set walking-time 0

<!-- b001106 | references | pages [36] -->
set walking true

<!-- b001107 | references | pages [36] -->
end

<!-- b001108 | references | pages [36] -->
to patdown

<!-- b001109 | references | pages [36] -->
; join queue - represented by stage 201

<!-- b001110 | references | pages [36] -->
ask my-links[die]

<!-- b001111 | references | pages [36] -->
let p [41 44 47 50 53 56]

<!-- b001112 | references | pages [36] -->
ifelse is-cutter and random 100 < cutting-prob[

<!-- b001113 | references | pages [36] -->
set queue-pos 0

<!-- b001114 | references | pages [36] -->
][

<!-- b001115 | references | pages [36] -->
set queue-pos item which-queue pd-length

<!-- b001116 | references | pages [36] -->
]

<!-- b001117 | references | pages [36] -->
set pd-length replace-item (which-queue) pd-length (queue-pos + 1)

<!-- b001118 | references | pages [36] -->
facexy (item which-queue p)(5 + queue-pos * .3)

<!-- b001119 | references | pages [36] -->
set fd-speed (distancexy (item which-queue p)(5 + queue-pos * .3)) / int(3 * speed-factor)

<!-- b001120 | references | pages [36] -->
set stage 201

<!-- b001121 | references | pages [36] -->
set walking-time 0

<!-- b001122 | references | pages [36] -->
set walking true

<!-- b001123 | references | pages [36] -->
end

<!-- b001124 | references | pages [36] -->
to record-data

<!-- b001125 | references | pages [36] -->
set death-per-10m replace-item (length death-per-10m - 1) death-per-10m ((last death-per-10m) + 1)

<!-- b001126 | references | pages [36] -->
set all-passengers all-passengers + 1

<!-- b001127 | references | pages [36] -->
ifelse is-precheck[

<!-- b001128 | references | pages [36] -->
set total-wait-queue-p0 lput wait-queue-0 total-wait-queue-p0

<!-- b001129 | references | pages [36] -->
set total-wait-queue-p1 lput wait-queue-1 total-wait-queue-p1

<!-- b001130 | references | pages [36] -->
set total-wait-queue-p2 lput wait-queue-2 total-wait-queue-p2

<!-- b001131 | references | pages [36] -->
set total-wait-queue-p3 lput wait-queue-3 total-wait-queue-p3

<!-- b001132 | references | pages [36] -->
set total-wait-queue-pd lput wait-queue-pd total-wait-queue-pd

<!-- b001133 | references | pages [36] -->
][

<!-- b001134 | references | pages [36] -->
set total-wait-queue-n0 lput wait-queue-0 total-wait-queue-n0

<!-- b001135 | references | pages [36] -->
set total-wait-queue-n1 lput wait-queue-1 total-wait-queue-n1

<!-- b001136 | references | pages [36] -->
set total-wait-queue-n2 lput wait-queue-2 total-wait-queue-n2

<!-- b001137 | references | pages [36] -->
set total-wait-queue-n3 lput wait-queue-3 total-wait-queue-n3

<!-- b001138 | references | pages [36] -->
set total-wait-queue-pd lput wait-queue-pd total-wait-queue-pd

<!-- b001139 | references | pages [36] -->
]

<!-- b001140 | references | pages [36] -->
set total-alive-time lput alive-time total-alive-time

<!-- b001141 | references | pages [36] -->
set total-waiting-time lput waiting-time total-waiting-time

<!-- b001142 | references | pages [36] -->
;show waiting-time

<!-- b001143 | references | pages [36] -->
die

<!-- b001144 | references | pages [36] -->
end

<!-- b001145 | references | pages [36] -->
to process-data

<!-- b001146 | references | pages [36] -->
set avg-alive-time mean total-alive-time

<!-- b001147 | references | pages [36] -->
set stddev-alive-time standard-deviation total-alive-time

<!-- b001148 | references | pages [36] -->
set avg-waiting-time mean total-waiting-time

<!-- b001149 | references | pages [36] -->
set stddev-waiting-time standard-deviation total-waiting-time

<!-- b001150 | furniture | pages [37] -->
Team 68942

<!-- b001151 | furniture | pages [37] -->
Page 36 of 36

<!-- b001152 | references | pages [37] -->
set avg-queue-p0 mean total-wait-queue-p0

<!-- b001153 | references | pages [37] -->
set avg-queue-p1 mean total-wait-queue-p1

<!-- b001154 | references | pages [37] -->
set avg-queue-p2 mean total-wait-queue-p2

<!-- b001155 | references | pages [37] -->
set avg-queue-p3 mean total-wait-queue-p3

<!-- b001156 | references | pages [37] -->
set avg-queue-n0 mean total-wait-queue-n0

<!-- b001157 | references | pages [37] -->
set avg-queue-n1 mean total-wait-queue-n1

<!-- b001158 | references | pages [37] -->
set avg-queue-n2 mean total-wait-queue-n2

<!-- b001159 | references | pages [37] -->
set avg-queue-n3 mean total-wait-queue-n3

<!-- b001160 | references | pages [37] -->
set avg-queue-pd mean total-wait-queue-pd

<!-- b001161 | references | pages [37] -->
set stddev-queue-p0 standard-deviation total-wait-queue-p0

<!-- b001162 | references | pages [37] -->
set stddev-queue-p1 standard-deviation total-wait-queue-p1

<!-- b001163 | references | pages [37] -->
set stddev-queue-p2 standard-deviation total-wait-queue-p2

<!-- b001164 | references | pages [37] -->
set stddev-queue-p3 standard-deviation total-wait-queue-p3

<!-- b001165 | references | pages [37] -->
set stddev-queue-n0 standard-deviation total-wait-queue-n0

<!-- b001166 | references | pages [37] -->
set stddev-queue-n1 standard-deviation total-wait-queue-n1

<!-- b001167 | references | pages [37] -->
set stddev-queue-n2 standard-deviation total-wait-queue-n2

<!-- b001168 | references | pages [37] -->
set stddev-queue-n3 standard-deviation total-wait-queue-n3

<!-- b001169 | references | pages [37] -->
set stddev-queue-pd standard-deviation total-wait-queue-pd

<!-- b001170 | references | pages [37] -->
end
