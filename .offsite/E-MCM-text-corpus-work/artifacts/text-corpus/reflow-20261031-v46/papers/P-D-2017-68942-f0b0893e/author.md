The objective of our Internal Control Management (ICM) team was to investigate the flow of passengers through American airport checkpoints in light of various airport security controversies. The TSA asked our team to determine bottlenecks in the current security process that impacted passenger throughput and variance in wait times, and to develop modifications that might expedite throughput and decrease variance. We developed an agent-based model using NetLogo to study how passengers move through a typical security checkpoint. Our model divided the current screening process into individual components (processes like document-checking and lines for those processes) to precisely locate potential bottlenecks and included separate components for passengers enrolled in PreCheck, a program that expedites screening for trusted travellers. Travelers and their speeds through certain components of the process were generated probabilistically to most accurately represent real-world unpredictability.

We ran the model with different checkpoint configurations and varying traffic volumes. Our model found that for low traffic volumes, overall wait times and variance were low. More importantly, at higher volumes (approx. 3 or less seconds per passenger) there were three significant bottlenecks: the lines for PreCheck and regular document-checking at the start of the checkpoint, and for the body scanners that most regular passengers must pass through. These three components caused over 99% of the variance and length of total wait times, with standard deviation of wait times topping 30 minutes during peak hours.

Using the NetLogo model, we studied how certain modifications would impact passenger flow. At higher traffic volumes, throughput was increased by up to 16% by more metal detector use, better officer training for pat-downs, or the addition of a single metal detector or body scanner and the extra body scanner reduced variance by 33%. The model also investigated how throughput and wait times were influenced by passenger behaviors. We found that cutting, opting for pat-downs, and slower walking all impacted the checkpoint negatively, but with less severity than expected.

Our model allowed us to closely analyze the efficiency of airport security checkpoints and shed light on how to resolve one of travelling's biggest issues.

1 Introduction

On the morning of September 11, 2001, a series of four coordinated terrorists attacks in New York, Pennsyl- vania, and Virginia killed nearly 3000 people and injured over 6000 others. The insuﬃcient airport security methods at the time allowed terrorists to board and subsequently hijack four passenger airliners. In the aftermath of the attacks, Congress and former President George W. Bush passed the Aviation and Trans- portation Security Act which established the Transportation Security Agency (TSA) as method to prevent similar attacks in the future. The TSA’s mission is to “protect the nation’s transportation systems to ensure freedom of movement for people and commerce” and desires to “provide the most eﬀective transportation security in the most eﬃcient way as a high performing counter-terrorism organization” [11].

Since its inception, the TSA has evolved to combat the various threats that terrorists pose to ordinary travelers. The addition of baggage screening, liquids limitations, and millimeter wave body scanners are just some examples of the increased security measures the TSA has implemented over the past decade. However, in 2016, the TSA came under sharp criticism when extremely long lines, particularly at large airports, caused travelers to miss their ﬂights. Furthermore, there have been incidents where travelers experienced unexpected and unpredicted long wait times. This high variance has lead to travelers making the tough choice between arriving at the airport unnecessarily early or potentially missing their ﬂight. As a result, the TSA is facing a tension between maximizing security and minimizing inconvenience travelers. Although the TSA’s PreCheck program, which allows travelers expedite the screening process, has become more popular, the exact eﬀect on traveler throughput is not known.

Our team has been tasked by the TSA with optimizing the traveler throughput at an airport security checkpoint. Our solution identiﬁes the problems with the current airport security checkpoint, shown above in Figure 4, and proposes a model that improves the checkpoint throughput and reduces variance in wait time while maintaining current safety and security standards.

2 Screening Process

Airport security checkpoints can be divided into four major zones, as demonstrated in Figure 4.

In Zone A, passengers arrive to the checkpoint and wait in a queue until a security oﬃcer can inspect their documents. In Zone B, passengers walk to an available screening lane. There, they unload their belongings for x-ray screening and pass through a millimeter wave body scanner or a walk-through metal detector (WTMD). In Zone C, the passengers collect their belongings from the x-ray conveyor belt and leave the checkpoint. In Zone D, passengers who require additional screening undergo pat-downs and/or baggage searches.

We model the checkpoint as a sequence of processes (e.g., passing through a body scanner) and queues (e.g., the line before a body scanner). The amount of time each process takes is set in our model, which queue times depend on the length and nature of the queue. Airports and the TSA wish to minimize the amount of time that passengers spend in any queue. In our model, there are a total of four queues and ten processes in the screening process, not including Zone D. They are, in chronological order:

Zone Queue Process Document check line (q0) A Walk to document check Document check Walk to screening lane X-ray screening line (q1) Unload belongings for screening Walk to line Body scanner or B WTMD line (q2) Walk to scanner or WTMD Body scanning or WTMD Walk to collection line Collection line (q3) C Collect belongings Exit

If a passenger undergoes additional screening in Zone D, he or she walks to Zone D, waits in a queue for an available security oﬃcer, and then undergoes the screening. In the case of a baggage search, the passenger exits the checkpoint from Zone D. Otherwise, the passenger walks to Zone C to retrieve baggage and then exits.

3 Assumptions

Real-world It was necessary to make several assumptions in our model:

1. Each passenger travels alone. We assume that passengers do not travel in pairs, as families, or in groups; each makes decisions that are dependent on his or her own needs and not the needs of others.

2. The given data set is representative of how passengers proceed through the screening process. It is diﬃcult to accurately predict how long each traveler will spend in each zone of the screening process. We assume that the given data closely approximates the movements of most travelers through security checkpoints.

3. Arrivals are uniformly random. According to the given data, the arrival times of travelers do not follow any clear pattern within short time periods (Figure 3). Thus, the best way to model arrivals is to generate travelers with a constant probability. The probability itself may vary between regular and Pre-Check arrivals, as well as with total traﬃc volumes.

4. Travelers choose the screening lane with the least amount of people. When passing from the document check to the baggage and body screening, people will choose what they perceive to be the most eﬃcient route: the lane with the least number of people.

5. The general layout of any US security checkpoint is the same as presented in Figure 4. The TSA sets strict guidelines for the layout, equipment, and dimensions of any airport security checkpoint [12]. Because it is diﬃcult and costly to expand the total space of security checkpoints, we limit the total number of lanes to six, though lanes may be closed during periods of lower traﬃc.

Similarly, the number of document-checking security oﬃcers is limited by physical space availability.

A typical checkpoint, as depicted in [12], has one document-checking oﬃcer for each body scanner.

6. For every two screening lines, there is one metal detector and one millimeter wave body scanner. According to the TSA’s Security Checkpoint Layout Design/Reconﬁguration Guide, the optimal layout for Zone B is two screening lines per metal detector and one metal detector per body scanner whenever possible [12].

7. Queues have no limit. At a real-world security checkpoint, bottlenecks in Zones B and C would translate to longer queue times in Zone A because of physical limits to the lengths of lines. However, we allow all queues to extend indeﬁnitely in order to discover precisely where bottlenecks exist in the screening process. Long queue lengths and wait times indicate which parts of the process are causing delays.

8. At most one passenger arrives to the checkpoint every second. Most airport security queues

are designed so that only one person can join at a time. It is reasonable to assume that passengers allow for a one-second gap to the next person.

9. Walking from the checkpoint entrance to the document-checking queue requires no time.

When lines are short, security oﬃcers will frequently reroute the queue to shorten the distance from the checkpoint entrance. As a result, it usually takes little time to walk to the end of the document-checking queue in Zone A.

10. An average American passenger’s personal space is a 3’ by 3’ square. [12]

11. All passengers eventually complete the screening process.

We assume that all passengers successfully exit the security checkpoint; none are arrested, detained, or leave the airport.

12. All travelers enrolled in the PreCheck program pass through WTMDs. [10]

13. Every passenger brings at least one piece of luggage. The TSA screens more than 1.7 billion carry-on bags a year, more than double the number of passengers. It is reasonable to assume that every traveler carrys at least one bag, if only to store his or her documents, wallet, and other important possesions.

3.1 Normality

We used the Shapiro-Wilk normality test [4] and quantile-quantile (Q-Q) plots to determine the distributions of datasets from the given passenger data. We found two that could be approximated by normal distribu- tions: document check process times and millimeter wave body scanner times, as determined by subtracting successive timestamps in the given data. For both, normality was not rejected at the p = 0.01 signiﬁcance level and the Q-Q plots showed linear trends with fairly random deviations (Figure 2). This allowed us to design our program to generate probabilistic times based on a normal distribution.

3.2 Process Times

Many of the process times were determined from the given data. However, for some processes it was necessary to make certain assumptions regarding the TSA screening process and traveler speeds. We based many of these values on personal investigation and real-world footage of travelers in airport checkpoints.

Zone Process Time (s) Walk to document check 2 A Document check 11.2 Walk to screening lane 3 [1] Unload belongings for screening 15 [1] Walk to scanner or WMTD line 3 B Walk to scanner or WMTD 2 Body scan 10.5 WTMD 1 Walk to collection line 3 Collect belongings 15 [1] C Exit 5-7 Walk to Zone D 3 D Pat-down 150 [8] Baggage Search 200 Some passengers enroll in PreCheck, a TSA program that expedites the screening process. Passengers in PreCheck do not need to remove jackets, belts, shoes, or laptops, shortening the time for unloading and retrieving belongings at the scanner (in our model, to 10 seconds). In addition, PreCheck passengers pass through WTMDs instead of the body scanners, which speeds the process further. However, the other times are largely the same.

3.3 Rates and Probabilities

Certain processes, like pat-downs and baggage searches, do not occur for every passenger. Instead, we assigned each process a certain probability.

• Each person has a 3% chance of being given a pat-down, including the approximate 1% of passengers who opt for a pat-down instead of a body scan [3]. Other reasons for pat-downs include failing a body scan or metal detector.

• The probability of having a baggage search is equal to that of receiving a pat-down.

• Travelers not enrolled in the PreCheck program have a 20% probability of being sent through the WTMD instead of the millimeter wave body scanner. The majority of non-PreCheck passengers sent through the WTMD are under 12, over 65, or have severe disabilities.

4 Deﬁnitions and Testing Parameters

The TSA wishes to evaluate and improve its airport security checkpoints. In particular, it is concerned with two statistics:

Deﬁnition 1. The throughput of a checkpoint at any time is the rate of passengers exiting the checkpoint.

The unit of throughput used in this paper is passengers per minute (PAX/min).

Deﬁnition 2. The wait time of a passenger is the total amount of time that he or she spent in queues during the checkpoint.

Our goal was to investigate possible bottlenecks in the security screening process that might cause de- creases in throughput, increases in wait time, and increases in wait time variance. We measured variance of wait time by calculating the standard deviation of the wait times of all passengers.

4.1 Arrivals

To simulate the randomness of the real-world passenger arrivals, passengers in our model are generated probabilistically every second rather than at a constant rate. Each arrival is then categorized as PreCheck or regular and sent to the corresponding queue.

Deﬁnition 3. The generation probability is the probability at each second that a passenger enters the checkpoint.

From the given data, the generation probability is 0.19, the average “rate” of passengers per second from the given data (Figure 3). This was determined by counting the number of total passenger arrival timestamps, both PreCheck and regular, that occurred within nine minutes. After arriving, each new passenger has a 0.45 probability of joining the PreCheck queue, since approximately 45% of passengers are currently enrolled in PreCheck.

4.2 Lanes and Oﬃcers

The checkpoint tested in our model contains six screening lanes. PreCheck lanes usually make up a third of total lanes, so when the checkpoint is fully running there are two PreCheck lanes and four regular lanes. The number of available oﬃcers in Zone D is equal to the number of active lanes: six. However, during times of less traﬃc airports will decrease the number of active screening lanes and document-checking oﬃcers in order to save money.

Therefore, we tested two diﬀerent conﬁgurations of active lanes and oﬃcers: one with all six lanes open for higher traﬃc, and one with only three lanes open for lower traﬃc.

Each conﬁguration is denoted by a four-digit number. For example, the number 1234 denotes the conﬁg- uration with 1 PreCheck document-checking oﬃcer, 2 active PreCheck screening lanes, 3 regular document- checking oﬃcers, and 4 active regular screening lanes.

Deﬁnition 4. The conﬁguration number is the four-digit number that denotes the numbers of lanes and oﬃcers active in the conﬁguration.

4.3 Testing

In our model, we tested diﬀerent volumes of traﬃc by increasing or decreasing the generation probability. We tested ﬁve generation probabilities: 0.09 (low traﬃc), 0.18 (normal traﬃc), 0.36 (busy traﬃc), 0.54 (high traﬃc), and 0.72 (peak traﬃc).

We tested conﬁguration 1221 for lower traﬃc (generation probabilities of 0.09, 0.18, 0.36, 0.54) and conﬁguration 2243 for higher traﬃc (generation probabilities of 0.18, 0.36, 0.54, 0.72). Each conﬁguration was run at least three times in our model, collecting data after each run and averaging across all runs to obtain our results. Each run generated passengers for one hour (3600 seconds) and then ran until the all passengers exited. To measure throughput, we counted the number of exiting passengers every ten minutes and divided by ten to obtain throughput passengers per minute.

We also tested the eﬀect of increasing or decreasing the number of PreCheck document-checking oﬃcers on throughput and wait time, varying the number of oﬃcers from 1 to 3 for the 1221 conﬁguration and the standard 0.18 generation probability.

5 NetLogo Model

To evaluate our assumptions and generate data, we use an agent-based NetLogo model. By using NetLogo, we are able to visually and robustly simulate passengers, oﬃcers, scanners, and queues in a time-accurate model. We can also use NetLogo’s powerful experimentation functionality to generate data.

5.1 Passengers

The basis of our model are passengers as represented by “turtles”, icons in the grid with attributes and the ability to perform actions. Each of our passengers has several attributes, including attributes that describe the passenger like is-precheck and speed-factor. Other attributes, including queue-pos and stage describe the passenger’s position in the model. Passengers are represented by pink (PreCheck) people, or purple (non-PreCheck) people.

Each passenger’s attributes are probabilistically decided by global values. For example, is-precheck is determined by precheck-percentage and is-cutter is determined by cutting-percentage. Passengers also record key data, including time-waiting to track total waiting time, and a wait-queue value for each queue they wait in.

5.2 Other turtles

Our passengers are aﬀected by not only their own attributes, but by the oﬃcers, scanners, and “pack stations”. Oﬃcers occupy one of two areas: either an document check lane (Zone A), or the rescreen/pat- down lanes (Zone D). In Zone A, they are assigned to either precheck or non-precheck, calling for passengers at the beginning of their respective queues. They are represented by orange people with blue hats and a badge. In Zone D, they are represented by a single oﬃcer icon that can patdown/rescreen multiple passengers. Scanners come in two forms - millimeter wave scanners or walk-through metal detectors. Each scanner pair operates as part of two lanes, and has its own queue. Millimeter wave scanners are represented by red hexagons, and WTMDs are represented by yellow rectangles. “Pack stations” are used to represent the areas in which passengers take oﬀor put on coats, bags, and other items before or after screening. Each lane has one “unpack station” and one “repack station”. They are represented by the dark brown circles on the lighter brown x-ray machines.

5.3 Running the simulation

When setup is called, the world creates oﬃcers, scanners, packing stations, and colors patches to visually guide the progression of passengers through lanes. When the model is set to go, the model generates a passenger at each tick (equivalent to a second) at a certain probability gen-prob. Passengers progress through security in several stages according to our outlined process. Our simulation only generates passengers in the ﬁrst 3600 ticks in order to only simulate a single real-world hour. The simulation stops when there are no longer passengers in the security checkpoint. At the end of the run, we use mean and standard-deviation to calculate the values we use for our analysis.

For single, visible runs, we use the green sliders on the left to adjust parameters, the purple buttons to setup and go, viewing output in the boxes on the right when the simulation ﬁnishes. For batches of runs, we use NetLogo’s “BehaviorSpace” to run 3 trials of simulations with varying parameters.

6 Results

Total Average Wait Time Total Standard Deviation Generation Probability (sec) (sec) 0.09 20.51 41.68 0.18 232.39 286.88

Generation Average Standard Deviation Average Standard Deviation Queue Probability (PreCheck) (PreCheck) (Regular) (Regular) q0 0.69 2.25 9.58 17.46 q1 0.00 0.00 0.00 0.00 0.09 q2 0.28 0.85 0.14 0.92 q3 23.17 50.30 7.72 27.29 Total 24.14 53.40 17.45 45.67 q0 1.75 4.08 372.53 297.88 q1 0.00 0.00 0.00 0.00 0.18 q2 0.51 1.15 0.40 1.72 q3 36.68 64.89 15.00 42.05 Total 38.94 70.12 387.93 341.65

For conﬁguration 1221, the average throughput peaks at about 14 passengers/min for generation probabilities of 0.36 and 0.54, indicating that this was not the best conﬁguration for those higher traﬃc volumes (Figure 6). However, for 0.09 and 0.18 the conﬁguration had more than enough capacity for the arrivals. This seems to imply that the bottleneck for throughput is primarily the number of active lanes and oﬃcers; once arrival rates increase past a certain point, increases in arrival rate no longer signiﬁcantly impacts the throughput. From Table 4, it is clear that the main bottleneck of both the PreCheck and the regular processes is line q3 (retrieving belongings from the x-ray belt) for all except the regular passengers at 0.18 generation probability, where the bottleneck is q0 (document-checking line). The variance in wait times is more than double the average wait time for a generation probability of 0.09. This may also be due to the natural variance that occurs from such a low generation probability, since high variance in arrivals easily translates to variance in wait times and throughput.

The wait time standard deviation is not immediately concerning for all but the 0.18, regular passengers case. The highest total standard deviation in those three cases is 70 seconds, or just over a minute. This means that a traveler having to wait more than ﬁve minutes longer than expected is high improbable. However, the case of regular passengers in the 0.18 generation probability case is much greater, with a wait time standard deviation of nearly six minutes.

Total Average Wait Time Total Standard Deviation Generation Probability (sec) (sec) 0.18 3.95 6.89 0.36 221.27 351.47 0.54 1088.93 867.74 0.72 2012.31 1409.13

Generation Average Standard Deviation Queue Probability (PAX) (PAX) q0 1.97 4.67 q1 0.00 0.00 0.18 q2 0.39 0.96 q3 0.00 0.00 Total 2.36 5.63 q0 162.31 322.88 q1 0.00 0.00 0.36 q2 0.66 1.15 q3 0.00 0.00 Total 162.98 324.03 q0 914.88 545.95 q1 0.00 0.00 0.54 q2 0.80 1.31 q3 0.00 0.00 Total 915.69 547.26 q0 1817.71 1060.32 q1 0.00 0.00 0.72 q2 0.76 1.27 q3 0.00 0.00 Total 1818.47 1061.59 Generation Average Standard Deviation Queue Probability (PAX) (PAX) q0 0.49 1.80 q1 0.00 0.00 0.18 q2 4.83 7.43 q3 0.00 0.00 Total 5.31 9.24 q0 7.94 17.12 q1 0.00 0.00 0.36 q2 262.35 345.87 q3 0.00 0.00 Total 270.29 363.00 q0 484.27 275.54 q1 0.00 0.00 0.54 q2 744.30 871.23 q3 0.00 0.00 Total 1228.57 1146.77 q0 1219.21 714.21 q1 0.00 0.00 0.72 q2 945.64 1154.63 q3 0.00 0.00 Total 2164.86 1868.85

For conﬁguration 2243, the average throughput peaks at about 21 passengers/min for generation prob- abilities of 0.36, 0.54 and 0.72, indicating that this was not the best conﬁguration for those higher traﬃc volumes (Figure 7). However, for a generation probability of 0.09, the conﬁguration had more than enough capacity for the arrivals. From the regular passengers described in table 7, we see a bottleneck at both the document check queue (q0) and the scanner queue (q2). Our PreCheck passengers in table 6 do not have a bottleneck in the scanner queue, but still have a high waiting time in the document check queue. Our observed variance in q0 wait times is more than double the average for regular and PreCheck passengers with generation probabilities 0.18 and 0.36, likely due to a few extremely high wait times. Our standard deviation with a generation probability is low, less than 10 seconds in either case. With generation probability 0.36, the standard deviation increases to approximately 5.5 minutes for PreCheck and 6 minutes for non-PreCheck passengers. Standard deviations of generation probabilities of 0.54 and 0.72 become excessive, almost 10 and 20 minutes for PreCheck and 20 and 30 minutes for non-PreCheck passengers. We see an unacceptably high standard deviation of wait times with this conﬁguration at high density populations.

6.1 Varying PreCheck Document-checking Oﬃcers

Number of Average Wait Time Standard Deviation Avg. Throughput PreCheck Oﬃcers (sec) (sec) (PAX/min) 1 2216.70 1276.84 4.82 2 309.62 252.01 9.23 3 59.26 101.28 10.49

As the number of document-checking oﬃcers increases, both the average wait time and the wait time standard deviation decrease signiﬁcantly, with the largest decrease occurring from one to two oﬃcers. However, while there is a signiﬁcant increase of nearly 100% in average throughput from one to two oﬃcers, the increase from two to three is much smaller. Therefore, when taking cost into account two oﬃcers does seem to be the optimal number when there is one active PreCheck lane and low traﬃc.

7 Improvements to the Current Process

It was clear from the results in Section 6 that there was much room for improvement in the current security screening process. We proposed four modiﬁcations and, using the NetLogo model, investigated how these changes might aﬀect throughput and wait times. The modiﬁcations were:

1. Adding another metal detector

2. Increasing the probability of WTMD usage for non-PreCheck passengers

3. Adding another millimeter wave body scanner

4. Reducing Pat-Down Times

5. Increasing the percent of PreCheck passengers

6. Increasing the number of PreCheck document-checkers

For nearly all modiﬁcations to the original model, we used the 1221 conﬁguration for generation proba- bilities of 0.09 and 0.18 and the 2243 conﬁguration for generation probabilities of 0.36, 0.54, and 0.72.

7.1 Throughput Data

Generation Extra Metal More WTMD Use Extra Shorter Probability Detector 30 40 50 Scanner Pat-downs 9 – 0.97 1.77 1.59 0.93 1.02 18 – 0.60 0.71 1.01 1.03 1.01 36 1.00 1.01 1.14 1.16 1.08 0.99 54 1.22 1.04 1.05 1.08 1.11 0.99 72 1.43 1.05 1.08 1.13 1.13 1.00

7.2 Extra Metal Detector

By adding another metal detector to our PreCheck lanes, we can alleviate queue wait times and decrease variance in the queue before scanning (q2).

Wait Time Standard Deviation Wait Time Standard Deviation Generation w/o Extra w/o Extra w/ Extra w/ Extra Probability PreCheck Lane PreCheck Lane PreCheck Lane PreCheck Lane (sec) (sec) (sec) (sec) 0.36 221.27 351.47 337.27 329.46 0.54 1088.93 867.74 711.87 940.49 0.72 2012.31 1409.13 1344.34 1607.91

metal detector

From Table 10 we can see that adding an extra metal detector when the generation probability is 0.54 and 0.72 signiﬁcantly decreases the average wait time of the screening process. We do not see the same eﬀect with a generation possibility of 0.36. However, the metal detector does increase throughput at all three generation probabilities. Thus, we can conclude that adding an extra metal detector is strictly beneﬁcial.

The increases in standard deviation are likely to due the fact that PreCheck passengers already experience shorter wait times than regular passengers do. Decreasing PreCheck times further will increase overall standard deviation. Based on table 9, adding an extra metal detector increases throughput from 28% to 82% varying based on generation probabilty.

7.3 Increasing WTMD Usage

Travelers pass through the WTMD almost without stopping, while travelers that use the millimeter wave body scanner spend about 11 seconds being scanned. If we increase the probability that any traveler proceeds through the WTMD instead of the millimeter wave body scanner, we should be able to increase the rate at which travelers pass through Zone B. To modify our current model, which has 20% of travelers being selected for the WTMD, we increased that probability to 30%, 40%, and 50%. Figure 11 shows the results.

expressed as the mean + the standard deviation.

From Figure 11, we can see that increasing the probability of travelers proceeding through the WTMD instead of the millimeter wave body scanners does indeed decrease the average wait time of travelers during the screening process. Looking at the generation probabilities of 0.36, 0.54, and 0.72, there is a clear downward trend as the probability increases. The same is true for standard deviations of wait times; while the change that they show is less, there is a noticeable decrease in standard deviations from the original 20% WTMD usage for higher generational probabilities (0.36, 0.54, and 0.72). Based on table 9, increasing WTMD usage correlates to increasing throughput, anywhere from a decrease of 40% to an increase of 113% based on generation probability. The beneﬁts of increasing WTMD usage are most pronounced with a 50% usage rate, presenting a beneﬁt to all generation probabilites.

7.4 Extra Millimeter Wave Scanner

By adding an additional millimeter wave scanner, the security checkpoint should see an increase in throughput as more passengers are able to be scanned. We see a greatly decreased wait time and standard deviation for most passenger arrival densities, but an increased wait time and standard deviation when the generation probability is 0.18. The diﬀerences are signiﬁcant; for higher traﬃc volumes (generation probabilities of 0.36 or more), the standard deviation decreases by more than a third. This could justify the extra cost of adding another body scanner, which costs about $250,000 [12].

Wait Time Standard Deviation Wait Time Standard Deviation w/ Extra Scanner w/ Extra Scanner Generation Probability (sec) (sec) (sec) (sec) 0.09 20.51 41.68 16.91 36.35 0.18 232.39 286.88 314.69 376.13 0.36 221.27 351.47 111.61 104.23 0.54 1088.93 867.74 526.05 530.25 0.72 2012.31 1409.13 989.71 992.35

Scanner

Adding an extra scanner can have mixed results on throughput (based on Table 9). Though it causes a throughput increase of 3% to 99% for generation probabilities 18 to 72, the checkpoints’s throughput decreases by 7% with a low generation probability of 9%.

7.5 Decreasing Pat-down Times

We consider improved training for TSA oﬃcers responsible for conducting pat-downs and baggage rescreening in order to improve these processes. This would cause an increase in throughput, as faster pat-downs and rescreenings would allow these aﬀected passengers to pass through security more quickly. We see a slight decrease in wait time and standard deviation for lower generation probabilities, namely 9% and 18%. However, for higher traﬃc the changes are nearly negligible, with the standard deviation increasing for when generation probability is 0.72.

Wait Time Standard Deviation Wait Time Standard Deviation Generation w/ Regular Pat-downs w/ Regular Pat-downs w/ Faster Pat-downs w/ Faster Pat-downs Probability (sec) (sec) (sec) (sec) 0.09 20.51 41.68 13.13 27.23 0.18 232.39 286.88 190.30 249.36 0.36 221.27 351.47 199.50 314.69 0.54 1088.93 867.74 1089.12 838.24 0.72 2012.31 1409.13 2095.55 1489.29

Pat-downs

Based on table 9, shorter pat-downs have a very slight change to the average throughput (±5%), with the exception of a generation probability of 36, which had a 82% increase.

7.6 Increasing percentage of PreCheck passengers

TSA PreCheck allows passengers to pass through security without removing light jackets, shoes, laptops, and belts. It also allows passengers to more quickly pass through security with a WTMD rather than a millimeter body scanner. An increase in percentage of people with access to this expedited process could potentially increase the throughput of the security checkpoint and reduce variance from waiting in the scanner queue.

as the mean + standard deviation.

However, while the increase did lead to improvements when traﬃc was low, the increase in percentage of PreCheck passengers was detrimental at probabilities higher than 0.18. This is likely due to the limiting factor of only two lanes and two document-checking oﬃcers for PreCheck passengers.

7.7 Increasing the number of PreCheck percentage and document-checkers

Having observed a bottleneck in the document-checking queue with PreCheck passengers at high volumes of traﬃc, we add two document-checking oﬃcers, making the conﬁguration 2443 rather than 2243.

as the mean + standard deviation.

We see that as we increase percentage of PreCheck enrollment, we see an overall decrease in wait time and wait time variance, lowest at 55%. After this sharp dip, average wait time increases steadily. This is observed at all generation probabilites, though it is most pronounced after 0.36. Overall, a slight increase in PreCheck enrollment is greatly beneﬁcial.

8 Variation in Traveler Behavior

In our model, we assumed that passengers follow mostly the same behavior, with only small variations in times. However, in the real world passengers exhibit a wide range of diﬀerent behaviors. This is especially true at large international airports, where passengers diﬀer by culture in addition to age, mobility, and personal preferences. We tested our model with the addition of new traveler styles to investigate how diﬀerent social interactions would aﬀect throughput and wait time. In particular, we investigated the following behaviors:

1. Cutting in line

2. Aversion to body scanners (people can opt out of body scanning and receive a pat-down instead)

3. Slower movement

8.1 Throughput Data

Table ?? shows the change in average throughput from each new passenger behavior.

Generation More Pat-downs Slow Cutting Probability 1% 2% Travelers 0.09 1.04 0.98 0.98 0.94 0.18 1.05 1.00 1.00 0.99 0.36 1.00 0.99 0.98 1.00 0.54 0.99 0.99 0.99 0.99 0.72 1.00 1.01 1.02 0.98

8.2 Cutting

In the interest of personal eﬃciency, some passengers may value their own position in queues rather more than the queue’s overall order. We refer to these passengers as “cutters”, people who will try to skip to the front of their queue and succeed about half the time. In modifying our model, we had 20% of travelers be cutters.

Comparing the data at various arrival densities (Table 14), we ﬁnd that cutting led to an increase in average and standard deviations of wait time. This may be because cutters cause other passengers to have to wait longer, therefore increasing the average wait time and standard deviation; as expected, cutting beneﬁts only those who cut. However, the negative eﬀects of cutting could be mitigated by enforcing a strict no-cutting policy in all queues.

Wait Time Standard Deviation Wait Time Standard Deviation Generation w/o Cutting w/o Cutting w/ Cutting w/ Cutting Probability (sec) (sec) (sec) (sec) 0.09 20.51 41.68 18.49 39.65 0.18 232.39 286.88 329.34 385.85 0.36 221.27 351.47 266.60 634.58 0.54 1088.93 867.74 1143.61 1183.92 0.72 2012.31 1409.13 2075.03 1697.81

8.3 Higher Pat-down Probability

Since the addition of the new millimeter wave body scanners to the TSA’s screening process in 2010, many travelers have expressed their concerns about the privacy of these machines. Responding to those concerns, the TSA allow people to defer a scan by the millimeter wave body scanner and receive a pat-down instead. Thus, we tested diﬀerent probabilities of travelers declining a millimeter wave body scan and receiving a pat-down to see if it had any eﬀect on the wait time for the screening process. According to the TSA, only about 1% of travelers opt for a pat-down instead of a millimeter wave body scan so we tested both a 1% probability and a 2% probability [8].

standard deviation.

From Figure 12, a 1% or 2% amount of travelers deferring a millimeter wave scan does not aﬀect the wait time standard deviations signiﬁcantly. This may not remain true for higher probabilities, but with low probabilities, the eﬀect is not signiﬁcant.

8.4 Slower Travelers

Not all travelers move at the same rate. While young adults move relatively quickly, older travelers and children may move slower than them. Thus, to incorporate the idea of a variety of speeds, we included slow travelers into the model. These travelers move half as fast as regular travelers and appear 20% of the time.

Wait Time Standard Deviation Wait Time Standard Deviation Generation w/o Slow Travelers w/o Slow Travelers w/ Slow Travelers w/ Travelers Probability (sec) (sec) (sec) (sec) 0.09 20.51 41.68 13.27 31.75 0.18 232.39 286.88 268.67 312.06 0.36 221.27 351.47 314.23 386.51 0.54 1088.93 867.74 1126.22 812.25 0.72 2012.31 1409.13 2101.90 1399.51

Travelers

From Figure 15, we can see that the addition of slow travelers increases the wait time, but not the standard deviation of screening process. This seems logical, because slower travelers will not only slow down the process as a whole, but also slow down travelers around them, accounting for the smaller standard deviations.

9 Policy and Procedural Recommendations

Based on our observations, we recognize several problem areas for current TSA checkpoints. PreCheck passengers are limited by the number of document-checking TSA oﬃcers, especially at a high volume of traﬃc. Non-PreCheck passengers are limited by document checking queues and scanner queues. These high wait times also lead to unacceptably large wait times and variances in those wait times, up to 30 minutes in high traﬃc scenarios. To improve the eﬃciency of the security checkpoint, we encourage the TSA to make one or more of the following changes:

• Add a metal detector to alleviate long, varied queue lengths in PreCheck lanes.

• Add a millimeter wave scanner in non-PreCheck lanes in order to reduce variance and length of queues.

• Increase the number of document-checking TSA oﬃcers

In order to address future increases in the proportion of passengers enrolled in PreCheck, we also suggest the following:

• Add document-checking TSA oﬃcers for PreCheck queues

• Add more Pre-Check lanes

Devoting more resources to PreCheck is less eﬀective on its own. These changes are only made eﬀective by an increase in PreCheck enrollment.

Other observed behaviors, including slower passengers and passengers that cut in front of others can be addressed speciﬁcally:

• Enforce stricter queueing. Cutting increases wait time variance and can increase average wait time, especially at higher traﬃc volumes. Posted signs in queues can help reduce incentive to skip through queues.

• Slower travelers can be overwhelmed in high traﬃc scenarios, but should be reassured their progress through security is not aﬀecting variance.

10 Strengths and Weaknesses

In future work, we would like to address the weaknesses of our model and improve on the computational eﬃciency of our simulations. This model had a number of strengths and weaknesses:

• Strength: Our model is based on real data released by the TSA.

By generating values based on real-world data directly from the TSA and other reputable sources, our model more eﬀectively represents real-world scenarios.

• Strength: Our model uses probabilistic methods to generate data.

Because we use previous data but add random variance, we are able to simulate scenarios with realistic randomness. A deterministic model would not be able to factor the signiﬁcant unpredictability that is present in the real world.

• Strength: Our model is ﬂexible and readily adaptable.

By using NetLogo, we can very quickly and easily change settings to investigate eﬀects of each param- eter. The experimentation capabilities of NetLogo allow us to automatically compile large quantities of data in spreadsheets. Our many inputs allow a wide variety of conﬁgurations to be ﬁne-tuned.

• Strength: Our model tests a large variety of modiﬁcations and diﬀerent behaviors.

We were able to simulate changes in both the checkpoint itself and in human behavior, and ﬁnd some modiﬁcations that improved overall eﬃciency of the checkpoint.

• Weakness: Our model cannot assess all potential combinations of parameters and conﬁgurations.

The ideal solution would test each of the thousands of possible security conﬁgurations, varying the numbers of lanes, document-checking oﬃcers, and equipment to ﬁnd the optimal conﬁguration. How- ever, this is a vastly unreasonable task. Instead, our model compares a large set of conﬁgurations to determine the best one.

• Weakness: Our model does not include a quantiﬁcation of security.

Each simulation, though representative of throughput and queue times, does not quantify security. It is diﬃcult to analyze how “secure” a checkpoint without extensive data and studies on each component of the screening process.

• Weakness: Our model cannot portray the complete complexity of human behaviors.

Though we consider a number of the most common behaviors, including diﬀering perceptions of personal space and propensity for cutting in line, there are many more to be found among real-world passengers.

Analyzing and implementing more behaviors into our model is a strong avenue for future work.

• Weakness: Our model has a limited number of trials for each combination of factors.

Though we are able to analyze data with 3 trials each, due to the probabilistic nature of the model, these trials may not accurately reﬂect the real-world system. More trials would allow us to more accurately analyze our model.
