# P-B-2011-9440-95f0fa40

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Print This Page Close This Window

<!-- b000002 | front_matter | pages [1] -->
Team Control Number

<!-- b000003 | front_matter | pages [1] -->
For office use only

<!-- b000004 | front_matter | pages [1] -->
9440

<!-- b000005 | front_matter | pages [1] -->
For office use only

<!-- b000006 | title | pages [1] -->
T1

<!-- b000007 | title | pages [1] -->
F1

<!-- b000008 | title | pages [1] -->
T2

<!-- b000009 | title | pages [1] -->
F2

<!-- b000010 | title | pages [1] -->
T3

<!-- b000011 | title | pages [1] -->
F3

<!-- b000012 | front_matter | pages [1] -->
Problem Chosen

<!-- b000013 | title | pages [1] -->
T4

<!-- b000014 | title | pages [1] -->
F4

<!-- b000015 | front_matter | pages [1] -->
B

<!-- b000016 | front_matter | pages [1] -->
2011 Mathematical Contest in Modeling (MCM) Summary Sheet

<!-- b000017 | front_matter | pages [1] -->
(Attach a copy of this page to each copy of your solution paper.)

<!-- b000018 | front_matter | pages [1] -->
Type a summary of your results on this page. Do not include

<!-- b000019 | front_matter | pages [1] -->
the name of your school, advisor, or team members on this page.

<!-- b000020 | prose | pages [1] -->
KEY PARAMETERS N-Number of users Voronoi R-Communication range Diagram of a repeater Beats r-Communication range of Cellular a user Network C-Capacity of a repeater KEY CONCEPT Relay Networks 104 Repeaters from out algorithm 108 Repeaters from the naïve solution Problem Clarification. In a wireless communication system, amplify-and-forward Two-Tiered Model repeaters are of great significance in supporting long-distance communication between Covering Problem low-power users. Repeaters are of limited capacities and may interfere with one another if they locate nearby and use close transmitter frequencies. Given a circular flat Voronoi Diagram area, we are asked to determine the least number of repeaters, as well as their working KEY TECHNIQUES frequencies and private line tones, to accommodate a number of simultaneous users Assumptions. The crucial assumptions in modeling the system are threefold: (i) users

<!-- b000021 | heading | pages [1] -->
Iterative Refinement

<!-- b000022 | prose | pages [1] -->
are uniformly distributed in the considered area and prefer to communicate with the nearest repeaters; (ii) two repeaters will interfere with each other if the difference Extremal Optimization between their transmitter frequencies is less than 0.6MHz, they share the same PL tone and their distance is less than twice of the repeater's communication range; (iii) in the Ploting Voronoi Diagram considered area, the wireless signals can fade freely. Determining Circumcircle Model. We propose a two-tiered network model consisted of two kinds of nodes: normal users and repeaters. User's and repeater's communication ranges are Minimum Spanning Tree respectively r and R. Users can send signals to repeaters within a distance r and repeaters can transmit signals to other repeaters and users up to a distance R. A repeater's capacity is C. Besides the capacity constrain and the interference avoidance, every user should be covered by at leasț one repeater and in a stronger requirement, every user can communicate with another user in any position of the considered area. Methods. (i) Inspired by the cellular network structure, we give a naïve solution where the number of repeaters and their positions can be obtained analytically. (ii) We propose an iterative refinement algorithm consisting of three fundamental modules: to draw the Voronoi diagram, to determine the circumscribed circles of Voronoi areas, and to escape the local optimum by using the idea of extremal optimization. (iii) We propose a greedy algorithm based on the minimal spanning tree to rearrange the frequencies and PL tones of repeaters. Results. The naïve solution: 12 repeaters for 1000 users and 108 repeaters for 10000 users. The proposed algorithm: 11 repeaters for 1000 users and 104 repeaters for 10000 users. We have proved that the 11 repeaters is the optimal solution. Without adding any more repeaters, after the rearrangement of the 104 repeaters' frequencies and PL tones by the greedy algorithm, with probability 97.12%, a randomly selected user can successfully send signals to a random position in the considered area. Strengths. The model is very general and can be naturally mapped to a well-defined opi te ti  i  s i o  p otuuns much faster than the simulated annealing-approach and is of higher ability to escape the local optimum than other iterative refinement and machine learning algorithms. Weaknesses. We have not developed an effective method to make sure every user can communicate with users in any positions.of the considered area.

<!-- b000023 | title | pages [1] -->
http://www.comap.com/undergraduate/contests/mcm/team-summary-sheet.php

<!-- b000024 | prose | pages [1, 2] -->
2011-2-14 Least Number of Repeaters Covering a Circular Area: Iterative Extremal Optimization Based on Voronoi Diagram

<!-- b000025 | furniture | pages [2] -->
Team #9440              Page  1 / 40

<!-- b000027 | heading | pages [2] -->
Abstract

<!-- b000028 | prose | pages [2] -->
In this paper, we propose a two-tiered network model, where lower-power users can communicate with one another through repeaters, which amplify weak signals and retransmit them. A repeater is of limited capacity and may interfere with a nearby repeater if their transmitter frequencies are close and they share the same private line tone. Our objective is to place the least number of repeaters that can satisfy the users’ communication requirement: the weak requirement is that every user must be covered by at least one repeater while the strong requirement is that every user can communicate with another user in any position of the considered area. Motivated by the structure of cellular networks, we give a naïve solution where the number of repeaters and their positions can be obtained analytically. In a circular area with radius 40 miles, 12 repeaters are enough to accommodate 1000 simultaneous users. We further propose an iterative refinement algorithm consisting of three fundamental modules: to draw the Voronoi diagram, to determine the circumscribed circles of Voronoi areas and move the repeaters to the centers of these circumscribed circles, and to escape the local optimum by using the idea of extremal optimization. The proposed algorithm outperforms the naïve solution. For the case of 1000 users, it obtains a solution with 11 repeaters, which can be proved to be the real optimum. For the case of 10000 users, it obtains a solution with 104 repeaters, better than the naïve solution with 108 repeaters. We further discuss how to assign frequencies and private line tones based on maximum and minimum spanning tree technique, the effects of simultaneous users need to be accommodated, the fluctuation of user density in reality, how the landscape can affect the design of repeaters’ locations, and the strengths and weaknesses of the model and algorithms.

<!-- b000029 | furniture | pages [3] -->
Team #9440              Page  2 / 40

<!-- b000030 | heading | pages [3] -->
1  Introduction

<!-- b000031 | prose | pages [3] -->
The design of amplify-and-forward relay networks has attracted increasing attention recently [1-3]. The relay networks are very helpful for long-distance communication since the relay nodes can amplify the weak signals and forward them to other relay nodes or send them directly to the destinations. Through several relay nodes, low-power users can communicate with one another in situation where direct user-to-user communication would not be possible. The relay networks have already found wide applications in cooperative communication [4]. For example, in amateur radio activities hams can communicate with distant hams through one or more relay nodes (also called radio repeaters) [5], and in wireless sensor networks relay nodes are used to help information dissemination between distant sensors [6].

<!-- b000032 | prose | pages [3] -->
In many amplify-and-forward cooperative communication networks, the nodes are homogeneous, namely a node can simultaneously play the roles as source node, sink node and relay node. A typical example is the mobile communication, where a cell phone can also be an amplify-and-forward relay node [4]. In another scenario, the relay nodes usually do not initiate communications but only help communications between other nodes. For example, in amateur radio activities, radio repeaters can be considered as relay nodes, and hams usually carry their own radios (transceivers). Repeaters can pick up weak signals from radios, amplify and retransmit them. Different from the homogeneous scenario, the functionalities of repeaters and radios are different, and the specifications of repeaters and radios are also different. For example, in Utah, the power of a radio is usually a few watts, while most repeaters are of power no less than a hundred watts.

<!-- b000033 | prose | pages [3] -->
Pan et al. [7] proposed a two-tiered relay network model, where the base stations are considered as low power users and some inter-application nodes are playing the role of relay nodes. However, they did not address the issue of covering users by relay nodes. Gupta and Younis considered the fault-tolerant [8] and traffic load balance [9] problems in a two-tiered relay network model, yet they did not address the placement problem of relay nodes. Tang et al. [10] proposed two algorithms for the relay nodes placement problem, aiming at placing the fewest number of relay nodes in the considered area such that each user can communicate with at least one relay node and the network of relay nodes is connected.

<!-- b000034 | prose | pages [3] -->
The above-mentioned works are different from ours because in a more general scenario that includes the amateur radio communication, the capacity of a repeater and the interference among nearby repeaters should be taken into account. In this paper, we propose a more general two-tiered network model, where each repeater can simultaneously manage at most C users and two nearby repeaters will interfere with each other if their transmitter frequencies are close and they share the same private line tone. Our objective is to place the least number of repeaters that can satisfy the users’ communication requirement. We respectively consider two different requirements: the weak requirement is that every user must be covered by at least one repeater and the strong requirement is that every user can communicate with another user in any position of the considered area. Our analysis indicates that the former requirement is equivalent to a circle covering problem while the solution on the latter requirement is based on the answer to the former requirement.

<!-- b000035 | prose | pages [3, 4] -->
The geometric covering problem is known to be NP hard [11], and the algorithm is usually very time-consuming even for a small number of circles. For example, Nurmela and Ostergard [12] proposed a simulated annealing algorithm to obtain near-optimal solutions for the unit square covering problem with up to 30 equal circles. Their result are known to be one of the most accurate results yet the algorithm has to run more than 2 weeks to obtain the solution for 27 circles. In contrast, considering the limited capacity of a repeater, when the number of users being accommodated increases, we have to place remarkably more repeaters than being considered in the previous works.

<!-- b000036 | furniture | pages [4] -->
Team #9440              Page  3 / 40

<!-- b000038 | prose | pages [4] -->
Motivated by the structure of cellular networks (i.e., networks with beehive-like structure), we give a naïve solution where the number of repeaters as well as their positions can be obtained analytically. In numerical simulation, this naïve solution performs unexpectedly well. In a circular area with radius 40 miles, 12 repeaters are enough to accommodate 1000 simultaneous users and for 10000 users, 108 repeaters are sufficient. In comparison, in the former case, 11 repeaters are the optimum and in the later case. We further propose an iterative refinement algorithm consisting of three fundamental modules: to draw the Voronoi diagram [13], to determine the circumscribed circles [14] of Voronoi areas and move the repeaters to the centers of these circumscribed circles, and to escape the local optimum by using the idea of extremal optimization [15,16]. This method outperforms the naïve solution. For the case of 1000 users, it obtains a solution with 11 repeaters, which can be proved to be the real optimum. For the case of 10000 users, it obtains a solution with 104 repeaters, better than the naïve solution.

<!-- b000039 | prose | pages [4] -->
Taking into account the capacity limitation and interferences, we proposed a more general model than most of previous models. Two methods are designed to place the repeaters in a typical area. They both perform very well. This work provides a general model and a novel algorithm to an extensively studied problem: how to place relay nodes in a cooperative communication system. This work can find applications in not only the amateur radio activities, but also the design of sensor wireless networks and mobile wireless networks.

<!-- b000040 | prose | pages [4] -->
This paper is organized as follows. In Section 2, we clarify the considered problem, and in Section 3, we descript the proposed two-tiered amplify-and-forward network model, as well as the definitions of solution and strong solution. Section 4 presents the calculation of the communication range of repeaters and users, the capacity of a repeater. In this section, we apply the continuous approximation and show how to map this problem to a “circles covering circle” problem. The naïve solution is also given in Section 4. We present the algorithms respectively to determine the requirement number of repeaters as well as their positions and to assign frequencies and private line tones to repeaters in Section 5. In Section 6, we give the solutions obtained by our algorithm, compare them with the naïve solution, and prove that the solution for the small population case is the optimal one. In Section 7, we discuss the effects of simultaneous users need to be accommodated, the fluctuation of user density in reality, and how the landscape can affect the design of repeaters’ locations, and finally, in Section 8, we summarize the paper and discuss the strengths and weaknesses of the model and algorithms.

<!-- b000041 | prose | pages [4] -->
Parameters, mathematical symbols and assumptions appear everywhere in this paper. Therefore, for convenience, in Appendix A, we list all the parameters, in Appendix B, we list the mathematical symbols, and in Appendix C, we summarize the important assumptions made in this paper.

<!-- b000042 | furniture | pages [5] -->
Team #9440              Page  4 / 40

<!-- b000043 | heading | pages [5] -->
2 Problem Description

<!-- b000044 | prose | pages [5] -->
Given a circular flat area of radius  (this circular area is denoted by ), we are asked to determine the least number of radio repeaters necessary to accommodate a given number of users N. A repeater is a combination of a radio receiver and a radio transmitter that picks up weak signals, amplify them, and retransmit them on a different frequency. In this problem, the three most fundamental parameters characterizing a repeater are the receiver frequency fr, the transmitter frequency ft and the private line (PL) tone nPL. A repeater responds only to signals on its receiver frequency and containing the same PL tone. If so, the signals will be amplified and transmitted on the repeater’s transmitter frequency and the PL tone will not be changed. In this problem, both fr, and ft belong to the range [145MHz, 148MHz], |fr - ft |=0.6MHz, and there are in total NPL=54 different PL tones available.

<!-- b000045 | prose | pages [5] -->
For example, a repeater located in Mong Kok, Hong Kong has the receiver frequency 145.025MHz, the transmitter frequency 145.625MHz, and the PL tone 110.9Hz. That is to say, only the signals on 145.025MHz and with PL tone 110.9Hz can be amplified by this repeater, and after amplification, the signals will be transmitted with frequency 145.625MHz and PL tone 110.9Hz.

<!-- b000046 | prose | pages [5] -->
Notice that, two repeaters will interfere with each other if they satisfy all the following three conditions: (i) they carry exactly the same PL tone; (ii) their distance is smaller than the twofold of the communication radius R of the repeater (for simplicity, we assume every repeater has the same communication radius R); (iii) the difference between their transmitter frequencies is smaller than a threshold fc. It is necessary to guarantee that no interference will happen between any pair of repeaters.

<!-- b000047 | prose | pages [5] -->
Each user can directly contact other nearby users and reach distant users through one or several repeaters. The maximal communication distance from a user to a repeater, r, is supposed to be identical for every user, which is remarkably smaller than the communication radius of a repeater (i.e., r<R). Every user should be covered by at least one repeater, namely at least one repeater locates inside the circle with radius r and centered at the user’s location. Under a stronger requirement, each user is able to send information to users at any positions in the considered area through one or several repeaters.

<!-- b000048 | prose | pages [5] -->
Since the communication ranges, R and r, are finite, and the capacity of a repeater, C, is very limited (i.e., a repeater can manage at most C different users simultaneously), usually a number of repeaters are required to accommodate users in a given area. The primary problem is to determine the minimum number of repeaters that can satisfy the communication requirement of a given number of users. Of course, a complete solution should also contain the positions, receiver and transmitter frequencies, as well as the PL tones of repeaters. The effects of the number of users and the landscape are emphasized in this problem. More detailed description of the meanings and effects of the parameters, and the in-depth analysis on the problem constrains are presented in the following sections.

<!-- b000049 | furniture | pages [6] -->
Team #9440              Page  5 / 40

<!-- b000050 | heading | pages [6] -->
3 Model

<!-- b000051 | prose | pages [6] -->
To present the system, we use a two-tiered directed network D(Vu, Vr, Eur, Err), where

<!-- b000052 | prose | pages [6] -->
  V { , u u ,..., u } V { , r r ,..., r } and denote the sets of users and repeaters, and Eur and u 1 2 N r 1 2 M

<!-- b000053 | prose | pages [6] -->
Err are the sets of directed links from users to repeaters and between repeaters. Each user ui is

<!-- b000054 | prose | pages [6] -->
identified by her/his location ( ( ), ( )) x u y u in a 2-dimensional plane, and each repeater rj is i i

<!-- b000055 | prose | pages [6] -->
identified by its location, receiver frequency, transmitter frequency and PL tone as

<!-- b000056 | prose | pages [6] -->
( ( ), ( ), x r y r f r ( ), f r ( ), n ( )) r . As mentioned above, the frequencies of an arbitrary j j r j t j PL j

<!-- b000057 | prose | pages [6] -->
f r  f r ( ), ( ) [145MHz,148MHz] repeater rj should obey the constrains and r j t j

<!-- b000058 | prose | pages [6] -->
. Since the considered area is a circular area of radius , the   f r ( ) f r ( )

<!-- b000059 | heading | pages [6] -->
0.6MHz

<!-- b000060 | prose | pages [6] -->
r j t j

<!-- b000061 | prose | pages [6] -->
location for arbitrary user or repeater should satisfy the inequality

<!-- b000062 | prose | pages [6] -->
                            (1) 2 2 2 x y

<!-- b000063 | prose | pages [6] -->
  is given a priori. A directed link from ui to rj exists (i.e., ( , u r ) E 40 where ) if the i j ur

<!-- b000064 | prose | pages [6] -->
distance between ui and rj is no more than a user’s communication range r. A directed link from rj

<!-- b000065 | prose | pages [6] -->
 to rk exists (i.e., ( , r r ) E ) if the distance between rj and rk is no more than a repeater’s j k rr

<!-- b000066 | prose | pages [6] -->
communication range R, the transmitter frequency of rj equals the receiver frequency of rk (i.e.,

<!-- b000067 | prose | pages [6] -->
  f r ( ) f r ( ) n ( ) r n ( ) r ) and they share the same PL tone (i.e., ). Clearly, the sets of t j r k PL j PL k

<!-- b000068 | prose | pages [6] -->
directed links are determined when the information about users and repeaters is known.

<!-- b000069 | prose | pages [6] -->
A network D is called a solution (in section 4, we will discuss a more practical definition of solution that does not depend on a specific distribution of users’ locations) if the following three

<!-- b000070 | prose | pages [6] -->
) are all satisfied. , , conditions ( 1 2 3

<!-- b000071 | prose | pages [6] -->
-Capacity constrain. For simplicity, we assume users are uniformly distributed in the 1

<!-- b000072 | prose | pages [6] -->
considered area  and each of them prefers to communicate with the nearest repeater. Each repeater can manage at most C users at the same time (the capacities of different repeaters are supposed to be the same, and the estimation of C will be given in the next section). For a repeater rj, there exists a connected area SV(rj) inside  such that for every point inside this area, rj is the nearest repeater and for every point outside this area, rj is definitely not the nearest repeater. This area is called the Voronoi area [13] of rj. For every repeater, the number of users inside its Voronoi area must be no more than its capacity C.

<!-- b000073 | prose | pages [6] -->
-Interference avoidance. If two repeaters share the same PL tone and are with distance 2

<!-- b000074 | prose | pages [6] -->
less than 2R, the difference between their transmitter frequencies must be no less than a given threshold fc. In the spectrum 145-148MHz, the standard threshold is fc=0.6MHz.

<!-- b000075 | furniture | pages [7] -->
Team #9440              Page  6 / 40

<!-- b000076 | prose | pages [7] -->
-Connectivity. Every user is covered by at least one repeater. That is to say,   iu jr , , 3

<!-- b000077 | prose | pages [7] -->
 such that ( , u r ) E . i j ur

<!-- b000078 | caption | pages [7] -->
Figure 1. An illustration about the reachable repeaters of u1. The circle centered at u1 is the

<!-- b000079 | prose | pages [7] -->
communication of u1 with radius r.

<!-- b000080 | prose | pages [7] -->
Our goal is to find out the solution with the minimum number of repeaters M. In a solution, although every user is covered by at least one repeater, her/his signals may not reach the desired position in  since the coverage of a repeater is also limited and the solution does not guarantee the existence of a multi-hop path through several repeaters to reach the desired position. Ignoring the small area that can be directly reached by a user without the help of any repeater, the reachable area of a user ui, denoted by Sr(ui), is defined as the area in  that can be covered by at least one reachable repeater of ui (each repeater covers a circle with radius R). The set of reachable repeaters for ui, denoted by Rr(ui), consists of two parts: One is the repeaters that can be directly reached by ui (i.e., the repeaters located within the circle with radius r and centered at ui) and another is the repeaters that can be further reached through directed paths consisted of directed links in Err and started from the directly reachable repeaters. Figure 1 illustrates a simple example where r2 can be directly reached by u1, and r4 and r5 can be further reached starting from r2. Two nearby repeaters, like r2 and r3, may not have a link in between since they may not match with each other in frequency or PL tone. The reachable repeaters of u1 are r2, r4 and r5, and thus the reachable area of u1 is the union of the coverage areas of r2, r4 and r5. The following condition must be satisfied to guarantee every user can in principle reach any position of the considered area through multi-hop repeaters.

<!-- b000081 | prose | pages [7] -->
-Global Reachability. The reachable area of every user is equal to the considered area 4

<!-- b000082 | prose | pages [7] -->
.

<!-- b000083 | prose | pages [7] -->
) are all , , A network D is called a strong solution if the following three conditions ( 1 2 4

<!-- b000084 | prose | pages [7, 8] -->
satisfied. Under these definitions, two propositions obviously hold, that is Proposition 1: A strong solution is a solution.

<!-- b000085 | furniture | pages [8] -->
Team #9440              Page  7 / 40

<!-- b000087 | prose | pages [8] -->
R , any solution is a strong solution. 2 Proposition 2: When To find a strong solution is much more difficult than to find a solution, and these two tasks R . We will respectively study the cases of R  2 2 are equivalent to each other only if R , emphasizing on the strong solutions. 2 and

<!-- b000088 | furniture | pages [9] -->
Team #9440              Page  8 / 40

<!-- b000089 | heading | pages [9] -->
4 Analysis

<!-- b000090 | prose | pages [9] -->
In this section, we will give some elementary analysis about the model. Firstly, in subsection 4.1 and 4.2, we will calculate the communication ranges for repeaters and users, as well as the repeater’s capacity according to the Shannon’s theory. Taking into consideration of the mobility of users, in subsection 4.3, we will show that the continuous approximation of the distribution of users’ locations is necessary to address the problem. In subsection 4.4, we will present a naïve solution where repeaters are arranged in a cellular network (i.e., a beehive-like structure). In spite of the simplicity, the naïve solution performs unexpectedly well, which will play a role of benchmark solution in evaluating the algorithmic output.

<!-- b000091 | heading | pages [9] -->
4.1 Communication Radius

<!-- b000092 | prose | pages [9] -->
We apply a simple model to determine the effective radiated distance (i.e., communication range) of repeaters and users. According to the problem description, we assume that this circular area is a place where wireless signals can fade freely. That is to say, there are not any other sorts of interference such as fogs, rivers, hills, buildings, activities of sun and so forth. Therefore the fading of signals under such situation is only due to the distance across which the signal is transmitted.

<!-- b000093 | prose | pages [9] -->
P Let be the power of the signal transmitted by a repeater. Since the signal can fade ,r out

<!-- b000094 | prose | pages [9] -->
freely, its average power P within one unit area at a distance d from the repeater is

<!-- b000095 | prose | pages [9] -->
P  r out , P (2)  2 4 d

<!-- b000096 | prose | pages [9] -->
2 4  , where According to the antenna theory [17], the effective receiving area of an antenna is

<!-- b000097 | prose | pages [9] -->
 is the wave length of the signal. So the receiving power of the signal is

<!-- b000098 | prose | pages [9] -->
 P 2   r out , ' P (3)   2 4 d 4

<!-- b000099 | prose | pages [9] -->
Substituting  with c f , where c is the velocity of light and f is the frequency of the

<!-- b000100 | prose | pages [9] -->
signal, one obtains

<!-- b000101 | prose | pages [9] -->
c  ' 2 P P ( ) (4) r out ,  4 df

<!-- b000102 | prose | pages [9] -->
sL is In terms of the communication theory (Shannon’s thoery), the loss

<!-- b000103 | prose | pages [9] -->
P     r out , L 10lg( ) 92.4 20lg d 20lg f (5) s ' P

<!-- b000104 | prose | pages [9] -->
sL is measured by dB, d is measured by km, f is in GHz. The actual power of where

<!-- b000105 | prose | pages [9, 10] -->
P received signal is ,r in         P P ( G G ) (

<!-- b000106 | furniture | pages [10] -->
Team #9440              Page  9 / 40

<!-- b000108 | heading | pages [10] -->
L L

<!-- b000109 | prose | pages [10] -->
) (

<!-- b000110 | heading | pages [10] -->
L L

<!-- b000111 | prose | pages [10] -->
) L (6) r in , r out , out in f out , f in , b out , b in , s

<!-- b000112 | prose | pages [10] -->


<!-- b000113 | heading | pages [10] -->
L L

<!-- b000114 | prose | pages [10] -->
From one repeater (transmitter) to another repeater (receiver), the equations hold as f out , f in ,

<!-- b000115 | prose | pages [10] -->
 

<!-- b000116 | heading | pages [10] -->
L L

<!-- b000117 | prose | pages [10] -->
G G (the loss of feed system), (other loss of the system), (the gain of b out , b in , out in

<!-- b000118 | prose | pages [10] -->
     

<!-- b000119 | heading | pages [10] -->
L L

<!-- b000120 | prose | pages [10] -->
2 dB

<!-- b000121 | heading | pages [10] -->
L L

<!-- b000122 | prose | pages [10] -->
1 dB G G 39 dB antenna). Normally, , , . For this f out , f in , b out , b in , out in

<!-- b000123 | prose | pages [10] -->
problem, the frequency of signals is about 0.1465GHz (i.e., the middle point of the available spectrum 145MHz~148MHz), and thus

<!-- b000124 | prose | pages [10] -->
P r out ,  10lg 37.2328 P r in ,  d 10 20 (7)

<!-- b000125 | caption | pages [10] -->
Table 1: Effective radiated powers of repeaters in Utah (http://www.ussc.com/~uvhfs/rptr.html)

<!-- b000126 | prose | pages [10] -->
Call No. ERP Call No. ERP Call No. ERP Call No. ERP Call No. ERP

<!-- b000127 | prose | pages [10] -->
K7UCS 120 W WA7UAH 30 W KD7NX 58 W K7JL 100 W K7JL 500 W

<!-- b000128 | prose | pages [10] -->
KF6RAL 100 W KD7HUS 25 W K7JH 100 W K7MLA 100 W K7SDC 100 W

<!-- b000129 | prose | pages [10] -->
W7IHC 100 W WV7H 40 W K7QEQ 100 W W7WAC 50 W K7MLA 100 W

<!-- b000130 | prose | pages [10] -->
AA7JR 100 W N7BSA 80 W W7SP 100 W N7KM 40 W N7NKK 50 W

<!-- b000131 | prose | pages [10] -->
NZ6Z 100 W W7BAR 100 W WV7H 100 W W7EO 40 W K7MLA 100 W

<!-- b000132 | prose | pages [10] -->
KE7FO 20 W K7HEN 100 W AE7TA 120 W KC7SNN 100 W K7JL 100 W

<!-- b000133 | prose | pages [10] -->
KR7D 100 W W7DRC 48 W N6EZO 100 W K7OGM 100 W AC7O 10 W

<!-- b000134 | prose | pages [10] -->
K7JL 50 W K7SDC 100 W W7SU 100 W K7MLA 75 W N7ZOI 100 W

<!-- b000135 | prose | pages [10] -->
N7WFM 100 W W7SP 100 W NR7K 100 W K7DAV 50 W W7EO 100 W

<!-- b000136 | prose | pages [10] -->
WB7REL 160 W WA7MXZ 100 W N7PCE 100 W W7BAR 183 W AB7TS 100 W

<!-- b000137 | prose | pages [10] -->
K7SDC 100 W W7JVN 100 W K7JL 100 W K7SDC 100 W KJ7VO 100 W

<!-- b000138 | prose | pages [10] -->
WA7KMF 100 W W7DRC 60 W KD7YE 97 W N7DZP 40 W WA7YZR 100 W

<!-- b000139 | prose | pages [10] -->
N7BYU 100 W W7DHH 100 W W7NRC 100 W KB7ZCL 200 W K7HEN 100 W

<!-- b000140 | prose | pages [10] -->
K7ACA 100 W N7JSQ 100 W KD0J 100 W K7CEM 40 W N7PQD 147 W

<!-- b000141 | prose | pages [10] -->
W7EO 160 W KD0J 100 W K7QEQ 100 W K7SDC 100 W N7WPF 125 W

<!-- b000142 | prose | pages [10] -->
KA7LEG 200 W KA7STK 25 W W7SU 100 W WX7Y 100 W AC7O 200 W

<!-- b000143 | prose | pages [10] -->
AC7O 100 W W7NRC 100 W NR7K 20 W K7SDC 60 W K7SG 25 W

<!-- b000144 | prose | pages [10] -->
WB7TSQ 100 W AC7O 100 W N7TOP 175 W N7GGN 20 W K7UCS 120 W

<!-- b000145 | prose | pages [10] -->
W7DES 25 W WB7CBS 100 W W7BYU 50 W W7BAR 100 W W7CWK 100 W

<!-- b000146 | prose | pages [10] -->
W7EO 100 W K7UCS 120 W WA7GIE 100 W KB7WQD 48 W WB7TSQ 100 W

<!-- b000147 | prose | pages [10] -->
K7SDC 100 W KK7EX 50 W WI7M 67 W WA7GIE 100 W WA7GIE 100 W

<!-- b000148 | prose | pages [10] -->
KK7DO 800 W NR7K 100 W WR7AAA 100 W AG7BL 100 W W7NRC 100 W

<!-- b000149 | prose | pages [10] -->
In the light of the statistics about the 2-meter repeaters in Utah, USA (see Table 1), the

<!-- b000150 | prose | pages [10, 11] -->
 P 100 W effective radiated power of most of the repeaters is , and normally a repeater can r out ,    P 1 W receive the signal with power no less than 1 W (i.e., ). According to Eq. (7), the r in ,

<!-- b000151 | furniture | pages [11] -->
Team #9440              Page  10 / 40

<!-- b000153 | prose | pages [11] -->
R  85.45 communication radius of a repeater is miles (the original result is measured by kilometers, and we have already changed it to miles). Analogously, the average working power for

<!-- b000154 | prose | pages [11] -->
   P 3.2 W and P 1 W a user (according to several wireless devices) is , resulting in the u out , u in ,

<!-- b000155 | prose | pages [11] -->
r  R  15.28 2 user’s communication radius miles. Although our calculation indicates that

<!-- b000156 | prose | pages [11] -->
) is equivalent to the connectivity ( ), we will discuss in this and the global reachability ( 4 3

<!-- b000157 | prose | pages [11] -->
R . 2 paper the more complicated case when

<!-- b000158 | heading | pages [11] -->
4.2 Repeater’s Capacity

<!-- b000159 | prose | pages [11] -->
In this subsection, we will calculate the maximal number of users that can be simultaneously accommodated in a repeater, namely the capacity C.

<!-- b000160 | prose | pages [11] -->
Ignoring the background noise and the interference, namely we assume that signals from one repeater will not affect others. Considering the transmitter frequency in a repeater is an exact value rather than in a broad band, we come up with a method to calculate the capacity through the gain. A mainstream method to estimate the capacity of information over a noisy channel is the famous Shannon theory, as:

<!-- b000161 | prose | pages [11] -->
  B log (1 SNR ) (8) 2

<!-- b000162 | prose | pages [11] -->
where  is the information bit rate, measured by watt (dB), SNR is the signal-to-noise ratio, which is dimensionless, and B is the total bandwidth, measured by Hz.

<!-- b000163 | prose | pages [11] -->
Inspired by Shannon Theory, Gilhousen et al. [18] put forward a method to estimate the capacity of a cellular CDMA System. Of greater importance for reliable system operation is the bit energy-to-noise density ratio, whose numerator is obtained by dividing the desired signal power by the information bit rate , and dividing the noise by the total bandwidth W, which results in the equation

<!-- b000164 | prose | pages [11] -->
 E P B P   b ur ur (9)   N (

<!-- b000165 | heading | pages [11] -->
C P

<!-- b000166 | prose | pages [11] -->
1) / B C 1 0 ur

<!-- b000167 | prose | pages [11] -->
where Pur is the power of signal come from a single user and received by a repeater, measured by bps; C is the maximum number of users that can be simultaneously managed by a repeater,

<!-- b000168 | prose | pages [11] -->
E N level is assumed which ensures operation at the level of bit error performance required b 0

<!-- b000169 | prose | pages [11] -->
E N is a for digital voice transmission, which is always set ranging from 5 to 30 dB. b 0

<!-- b000170 | prose | pages [11] -->
standard for digital voice transmission, and can take different values according to different circumstances.

<!-- b000171 | prose | pages [11] -->
Different from the CDMA System, the transmitter frequency in a repeater is an exact value rather than in a broad band. We prefer to take the following equation

<!-- b000172 | prose | pages [11] -->
E G  b out (10)   N

<!-- b000173 | heading | pages [11] -->
V C

<!-- b000174 | prose | pages [11] -->
( 1)(1

<!-- b000175 | heading | pages [11] -->
I I

<!-- b000176 | prose | pages [11, 12] -->
) 0 other self I where G is the gain of antenna, V is the gain of voice,

<!-- b000177 | furniture | pages [12] -->
Team #9440              Page  11 / 40

<!-- b000179 | prose | pages [12] -->
I repeaters, and is the interference of itself. self is the interference come from other other

<!-- b000180 | prose | pages [12] -->
In the situation that a repeater can accommodate C users simultaneously, SNR can be regarded as the ratio of the effective information in the total received signal, say

<!-- b000181 | prose | pages [12] -->
 SNR P 1  ur (11)  

<!-- b000182 | heading | pages [12] -->
C P

<!-- b000183 | prose | pages [12] -->
(

<!-- b000184 | prose | pages [12] -->
  G 39 dB 7966.40 W Normally, and out 1) C 1 ur

<!-- b000185 | prose | pages [12] -->
  V 0.4 dB 1.07 W (in the calculation, the

<!-- b000186 | prose | pages [12] -->


<!-- b000187 | heading | pages [12] -->
I I

<!-- b000188 | prose | pages [12] -->
0 unit must be watt). We ignore the interference come from other repeaters, namely

<!-- b000189 | prose | pages [12] -->
  E N 18 dB 63.01 W . other self

<!-- b000190 | prose | pages [12] -->
(the bit energy-to-noise density ratio is always ranging from Setting b 0

<!-- b000191 | prose | pages [12] -->
5 to 30dB, and for transceiver we set it as the middle point 18dB), we can get the capacity of a single repeater through:

<!-- b000192 | prose | pages [12] -->
G  C 1 

<!-- b000193 | heading | pages [12] -->
V I

<!-- b000194 | prose | pages [12] -->
(1 other

<!-- b000195 | heading | pages [12] -->
4.3 Continuous Approximation

<!-- b000196 | prose | pages [12] -->
 out 119 (12)

<!-- b000197 | heading | pages [12] -->
I E

<!-- b000198 | prose | pages [12] -->
) N self b 0

<!-- b000199 | prose | pages [12] -->
Taking into account the mobility of users, the repeaters have to cover all the considered area

<!-- b000200 | prose | pages [12] -->
. Given distributed users Vu, a solution

<!-- b000201 | prose | pages [12] -->
distribution of users. That is to say, the network

<!-- b000202 | prose | pages [12] -->
' V and

<!-- b000203 | heading | pages [12] -->
D V V

<!-- b000204 | prose | pages [12] -->
( , ) may be not a solution for another u r

<!-- b000205 | prose | pages [12] -->
'

<!-- b000206 | heading | pages [12] -->
D V V

<!-- b000207 | prose | pages [12] -->
( , ) may not be a solution although the u r

<!-- b000208 | prose | pages [12] -->
V are sampled from an identical uniform distribution. Therefore, user locations of both u u

<!-- b000209 | prose | pages [12] -->
a practical solution should not depend on a specific distribution.

<!-- b000210 | prose | pages [12] -->
To make it possible, we use a continuous approximation instead of the uniform distribution of users. Under this approximation, the number of users is considered as a real variable (do not be surprised if we talk about 94.40 users) and the N users are distributed completely uniformly in the considered area. At any point inside the considered area, the user density, denoted by , is a constant as

<!-- b000211 | prose | pages [12] -->
 N  (13)  2

<!-- b000212 | prose | pages [12] -->
, the other three constrains are  is the area of . Except the irrelevant constrain 2 where

<!-- b000213 | prose | pages [12] -->
changed correspondingly as 2

<!-- b000214 | prose | pages [12] -->
-Capacity constrain. For every repeater rj, if the area of its Voronoi area is SV(rj), it * 1

<!-- b000215 | prose | pages [12] -->
must satisfy the inequality

<!-- b000216 | prose | pages [12, 13] -->
 S V  ( ) r C (14) j -Connectivity. Every point in the considered area is covered by at least one repeater. * 3

<!-- b000217 | furniture | pages [13] -->
Team #9440              Page  12 / 40

<!-- b000219 | prose | pages [13] -->
-Global Reachability. The reachable area of every point (considering that at every point, * 4

<!-- b000220 | prose | pages [13] -->
there can be user) is equal to the considered area .

<!-- b000221 | prose | pages [13] -->
Hereinafter, the terms solution and strong solution are all corresponding to the continuous case. Although we assume the users are uniformly distributed, in the real discrete case, the distribution can never be as uniform as the continuous case. The effects of fluctuation in the real distribution of users’ locations (where the number of users is always an integer) will be discussed in the Section 7.

<!-- b000222 | prose | pages [13] -->
As mentioned in Proposition 1 and 2, if we only consider the solution or in the case with R , under continuous approximation, our problem is equivalent to the “circles covering 2 circle” problem if we can easily make sure any two repeaters will not interfere with each other. In a word, we should determine the least number of circles with radius r’ to cover a circle with radius . Notice that, r’ may be smaller than r due to the capacity limitation.

<!-- b000223 | prose | pages [13] -->
R  2 In the frequency range [145MHz, 148MHz] with fc=0.6MHz, in a PL tone, if (when R , any pair of repeaters in the considered area may interfere with each other), there are at most six different repeaters without interference, whose transmitter frequencies are 145.0MHz, 145.6MHz, 146.2MHz, 146.8MHz, 147.4MHz and 148.0MHz. However, according to the pigeonhole principle, there must be a pair of repeaters with inverse frequency pair as f1-f2 and f2-f1 (Here, a repeater represented by f1-f2 has a receiver frequency f1 and a transmitter frequency f2). It is very possible that the former repeater amplifies signals and sends to the latter repeater, and the latter repeater amplifies the received signals and sends back to the former repeater, again the former repeater will amplify the signals and send to the latter repeater, and so on. To avoid such a problem, we consider a set of non-interacting repeaters in a PL tone. Obviously, the maximum number of such a group of repeaters is five. An example set is 145.6-145.0, 146.3-145.7, 147.0-146.4, 147.7-147.1 and 147.4-148.0. Therefore, we can conclude that when R , with

<!-- b000224 | prose | pages [13] -->
 N 54 the help of different PL tones, the maximum number of repeaters without any PL

<!-- b000225 | prose | pages [13] -->
  interference is 54 6 324 , and the maximum number of repeaters without any interactions is  54 5 270 . Therefore, if the required number of small circles is no more than 324, we do not need to consider the interference avoidance constrain but just set these repeaters to make sure they do not interfere with each other, while if the required number is no more than 270, we can make sure there will not be any needless interactions between repeaters. Of course, if we consider the R , the situation is much more complicated, and interactions between 2 strong solution with repeaters are generally necessary.

<!-- b000226 | prose | pages [13] -->
According to the connectivity constrain, in any solution, the number of repeaters M should satisfy the inequality

<!-- b000227 | prose | pages [13] -->
   2 2 2 40     M 6.85 (15)  2 2 2 r r 15.28

<!-- b000228 | prose | pages [13, 14] -->
M  7 Since M is an integer, we have . According to the capacity constrain, in any solution, the number of repeaters M should satisfy the inequality N N   M (16) C 118 M  9 In this problem, for N=1000, the lower boundary of M is 9 (i.e., ), while for N=10000, it is M  85 85 (i.e., ).

<!-- b000229 | furniture | pages [14] -->
Team #9440              Page  13 / 40

<!-- b000231 | heading | pages [14] -->
4.4 Naïve Solution

<!-- b000232 | prose | pages [14] -->
Cellular networks are widely used in placing the relay nodes, especially in the design of the locations of base stations in mobile wireless networks. In this paper, as a naïve solution, we directly apply the cellular network structure to cover the considered area. Table 2 illustrates some small-size cellular networks, each of them can be considered as the Voronoi diagram [13] where the center of each regular hexagon lays a repeater. Clearly, the number of regular hexagons is equal to the number of repeaters M.

<!-- b000233 | prose | pages [14] -->
We firstly consider an inverse problem, that is, given a number of equal regular hexagons (we assume the edge length is a unit), to determine the largest circle that can be fully covered by these regular hexagons (these hexagons must be arranged in a beehive-like pattern). Table 2 gives the results up to 13 regular hexagons, which are calculated by hand.

<!-- b000234 | caption | pages [14] -->
Table 2: The cellular networks that can cover the largest circle. The third column lists the radiuses

<!-- b000235 | prose | pages [14] -->
of the corresponding circles. Given the number of cells M, sometimes, the cellular networks are not unique, and then we only draw one of them as a representative.

<!-- b000236 | prose | pages [14] -->
The number of The schematic diagram The radius of the largest cells, M circle can be covered 1 3 2 2 3 2

<!-- b000237 | prose | pages [14] -->
1 3

<!-- b000238 | prose | pages [14] -->
4 7 2

<!-- b000239 | prose | pages [14, 15] -->
5 7 5 6 3

<!-- b000240 | furniture | pages [15] -->
Team #9440              Page  14 / 40

<!-- b000242 | prose | pages [15] -->
2 7

<!-- b000243 | prose | pages [15] -->
2 8

<!-- b000244 | prose | pages [15] -->
2 9

<!-- b000245 | prose | pages [15] -->
10 19 2

<!-- b000246 | prose | pages [15] -->
11 19 2

<!-- b000247 | prose | pages [15] -->
12 7

<!-- b000248 | prose | pages [15] -->
13 7

<!-- b000249 | prose | pages [15] -->
R  for 2 Here we show how to directly obtain the solution or the strong solution with N    0.1989 the case N=1000 by using Table 2. In this case, the user density is . The   2

<!-- b000250 | prose | pages [15, 16] -->
maximal area of the Voronoi area of any repeater in a cellular network is equal to the area of the regular hexagon (in the edge of the considered area, a repeater’s Voronoi area may be smaller than the area of the regular hexagon). The edge length of the regular hexagon rh should not exceed the communication range r to make sure each point is covered by at least one repeater. In addition, according to the capacity limitation, the edge length rh should satisfy the inequality 3 3  2 hr C (17) 2

<!-- b000251 | furniture | pages [16] -->
Team #9440              Page  15 / 40

<!-- b000253 | prose | pages [16] -->
These two conditions determine the possibly longest edge length, and of course, to cover as large circle as possible, we always use the longest rh. In this case, r=15.28 miles, and according to Eq.

<!-- b000254 | prose | pages [16] -->
hr should be no longer than 15.18 miles. Therefore, the edge length of the regular hexagon (17),

<!-- b000255 | prose | pages [16] -->
 19    7 40 is rh=15.18miles. The circle to be covered is of radius miles. Since , 2 hr

<!-- b000256 | prose | pages [16] -->
according to Table 2, 12 repeaters are sufficient to cover the considered area under the constrains of capacity and connectivity, yet 11 repeaters are not possible using the cellular network structure. This solution is shown in Figure 2, and the coordinates of repeaters are presented in Table 3.

<!-- b000257 | prose | pages [16] -->
R , the 2 Notice that, here we only consider the solution or the strong solution with frequencies and PL tones of repeaters are easily to be arranged. As an example, we use three PL tones to make sure there is no interaction or interference.

<!-- b000258 | caption | pages [16] -->
Figure 2: The solution consisted of 12 repeaters arranged in a cellular network. The blue circle

<!-- b000259 | prose | pages [16] -->
denotes the considered area with radius 40miles, the read regular hexagons represent the cellular network, and the blue points in the centers of the regular hexagons denote the positions of repeaters.

<!-- b000260 | prose | pages [16] -->
As shown above, the basic procedure to get the naïve solution contains two steps: (i) find the longest rh, (ii) search the best solution according to Table 2. However, the calculation of the radius of the largest coverable circle is not an easy problem (at least not easy by hand) for many regular hexagons. We only get the analytical results for two particular cases up to 121 circles, where the covered circle’s center is either at the center of the central hexagon or at the intersection of the three more central hexagons.

<!-- b000261 | furniture | pages [17] -->
Team #9440              Page  16 / 40

<!-- b000262 | caption | pages [17] -->
Table 3: The coordinates, frequencies and PL tones of the solution shown in Fig. 2.

<!-- b000263 | prose | pages [17] -->
Repeater x-Coordinate y-Coordinate Receiver Transmitter PL Tone No. Frequency Frequency 1 -15.1800 0.0000 145.6 145.0 1 2 7.5900 13.1463 146.3 145.7 1 3 7.5900 -13.1463 147.0 146.4 1 4 -15.1800 26.2925 147.7 147.1 1 5 -37.9500 -12.6411 147.4 148.0 1 6 -37.9500 12.6411 145.6 145.0 2 7 -15.1800 -26.2925 146.3 145.7 2 8 7.5900 39.2733 147.0 146.4 2 9 7.5900 -39.2733 147.7 147.1 2 10 30.3600 0.0000 147.4 148.0 2 11 30.3600 26.0436 145.0 145.6 3 12 30.3600 -26.0436 147.4 148.0 3

<!-- b000264 | caption | pages [17] -->
Table 4: Analytical results for two particular cases. In the left side the largest covered circle is

<!-- b000265 | prose | pages [17] -->
centered at the center of the central hexagon, while in the right side the largest covered circle is centered at the intersection of the three more central hexagons.

<!-- b000266 | prose | pages [17] -->
Center of a circle                 Intersection of three circle The number The radius of the largest The number The radius of the largest of cells, M of cells, M coverable circle coverable circle 1 3 1 3 2 2 6 7 3

<!-- b000267 | prose | pages [17] -->
12 13 7 3 3 2 18 19 13 3

<!-- b000268 | prose | pages [17] -->
27 31 4 5 3 2 36 37 21 5

<!-- b000269 | prose | pages [17, 18] -->
48 55 31 7 3 2 60 61 43 6 75 85 7 9 3 2 90 91 57 8

<!-- b000270 | furniture | pages [18] -->
Team #9440              Page  17 / 40

<!-- b000272 | prose | pages [18] -->
108 121 91 9

<!-- b000273 | prose | pages [18] -->
N    1.989 In the case N=10000, , according to the capacity constrain Eq. (17), we   2

<!-- b000274 | prose | pages [18] -->
 hr    4.80 miles. Since 8 9 have , according to Table 4, 108 repeaters are sufficient to hr

<!-- b000275 | prose | pages [18] -->
cover the considered area under the constrains of capacity and connectivity. Since the number of repeaters is smaller than 324, it is easy to arrange them when considering only a solution or a R . Figure 3 shows this solution, and the table containing all the 2 strong solution with coordinates is ignored.

<!-- b000276 | caption | pages [18] -->
Figure 3: The solution consisted of 108 repeaters arranged in a cellular network. The blue circle

<!-- b000277 | prose | pages [18] -->
denotes the considered area with radius 40miles, the red regular hexagons represent the cellular network. The repeaters are also lay in the centers of the regular hexagons (not shown).

<!-- b000278 | furniture | pages [19] -->
Team #9440              Page  18 / 40

<!-- b000279 | heading | pages [19] -->
5 Algorithm

<!-- b000280 | prose | pages [19] -->
This section will present two algorithms. The main algorithm tries to solve the circles covering circle problem with the least number of circles, and the secondary algorithm assigns each repeater the receiver frequency, the transmitter frequency and the PL tone.

<!-- b000281 | prose | pages [19] -->
40

<!-- b000282 | prose | pages [19] -->
30 R19 R20 R28 R11 20 R8 R15 R5 R25 10 R2 R26 R23 R13 R16 R1 R6 0 R4 R27 R12 R30 -10 R9 R24 R7 R14 -20 R29 R10 R22 R3 R17 -30 R18 R21

<!-- b000283 | prose | pages [19] -->
-40

<!-- b000284 | prose | pages [19] -->
-40 -30 -20 -10 0 10 20 30 40

<!-- b000285 | caption | pages [19] -->
Figure 4: Illustration of an initial configuration with 30 repeaters. The coordinates of each

<!-- b000286 | prose | pages [19] -->
repeater are generated randomly inside the considered area.

<!-- b000287 | prose | pages [19] -->
40

<!-- b000288 | prose | pages [19] -->
30 R19 R20 R28 R11 20 R8 R15 R5 R25 10 R2 R26 R23 R13 R16 R1 R6 0 R4 R27 R12 R30 -10 R9 R24 R7 R14 -20 R29 R10 R22 R3 R17 -30 R18 R21

<!-- b000289 | prose | pages [19] -->
-40

<!-- b000290 | prose | pages [19, 20] -->
-40 -30 -20 -10 0 10 20 30 40 Before running the algorithm, we first determine the lower boundary of M according to Eqs. (15) and (16). The boundary is denoted by M0. The procedure of the algorithm is as follows.

<!-- b000291 | caption | pages [19] -->
Figure 5: The resulted Voronoi diagram corresponding to the configuration shown in Fig. 4.

<!-- b000292 | furniture | pages [20] -->
Team #9440              Page  19 / 40

<!-- b000294 | prose | pages [20] -->
(1) Randomly place M0 repeaters in the considered area (See Fig. 4).

<!-- b000295 | prose | pages [20] -->
(2) Divide the area into different parts in terms of Voronoi diagram, that is to say, determine the Voronoi area of each repeater. The algorithm can be found in Ref. [13], and one can see Fig. 5 for the resulted Voronoi diagram of the above configuration. Notice that, for some repeaters close to the edge of the considered area, their Voronoi areas may contain a part of the edge of the considered area.

<!-- b000296 | prose | pages [20] -->
(3) Determine the circumscribed circle of each Voronoi area (i.e., a circle which can cover the area and meanwhile has the minimal radius). A standard algorithm can be found in Ref. [14], an advanced method can be found in Ref. [19]. We apply the standard method.

<!-- b000297 | prose | pages [20] -->
The corresponding result after Fig. 5 is shown in Fig. 6.

<!-- b000298 | prose | pages [20] -->
40

<!-- b000299 | prose | pages [20] -->
30 R19 R20 R28 R11 20 R8 R15

<!-- b000300 | prose | pages [20] -->
R5 R25 10 R2 R26 R23 R13 R16 R1 R6 0 R4 R27 R12 R30 -10 R9 R24 R7 R14 -20 R29 R10 R22 R3 R17 -30 R18 R21

<!-- b000301 | prose | pages [20] -->
-40

<!-- b000302 | prose | pages [20] -->
-40 -30 -20 -10 0 10 20 30 40

<!-- b000303 | caption | pages [20] -->
Figure 6: The circumscribed circles of the Voronoi areas, corresponding to the ones shown in Fig.

<!-- b000304 | prose | pages [20] -->
5. The circumscribed circles are colored in green while the Voronoi areas are colored in red. Notice that, for the some repeaters close to the edge of the considered area, their Voronoi areas may contain a part of the edge of the considered area.

<!-- b000305 | prose | pages [20] -->
(4) Calculate the coordinates of the center of each circumscribed circle.

<!-- b000306 | prose | pages [20] -->
(5) Calculate the distance from each repeater’s current location to the centers of the corresponding circumscribed circle. Sum up all the distances and compare the sum to a

<!-- b000307 | prose | pages [20] -->
threshold . If the sum is less than , the current set of repeaters’ locations is

<!-- b000308 | prose | pages [20, 21] -->
considered to be converged. If it is converged, go to step (6), otherwise, move each repeater to the center of the corresponding circumscribed circle (see figure 7) and go back to step (2).

<!-- b000309 | furniture | pages [21] -->
Team #9440              Page  20 / 40

<!-- b000311 | prose | pages [21] -->
(6) Calculate the number of users in each Voronoi region and see if the number is less than the repeater’s capacity, and the radius of the circumscribed circle should be less than the communication radius of users. If so, stop the algorithm and output the current solution.

<!-- b000312 | prose | pages [21] -->
Otherwise, go to step (7) (7) With the current number of repeaters, if the number of extremal optimization operations is less than a threshold Tc, pick up the repeater with the smallest Voronoi area, move it to a random position in the considered area and go back to step (2) and count an extremal optimization operation. Otherwise, add one more repeater, randomized the positions of all repeaters, and go back to step (2).

<!-- b000313 | prose | pages [21] -->
40

<!-- b000314 | prose | pages [21] -->
30 R19 R20 R28 R11 20 R8 R15

<!-- b000315 | prose | pages [21] -->
R5 R25 10 R26 R2 R23 R13 R16 R6 R1 0 R4 R27 R12 R30 -10 R9 R24

<!-- b000316 | prose | pages [21] -->
R7 R14 -20 R29 R10 R22 R3 R17 -30 R18 R21

<!-- b000317 | prose | pages [21] -->
-40

<!-- b000318 | prose | pages [21] -->
-40 -30 -20 -10 0 10 20 30 40

<!-- b000319 | caption | pages [21] -->
Figure 7: The black asterisks stand for the locations of repeaters, the red ones represent the

<!-- b000320 | prose | pages [21] -->
centers of the circumscribed circles, and the black arrows show the directions towards which the repeaters will move. This illustration corresponds to the result shown in Fig. 6.

<!-- b000321 | prose | pages [21] -->
Here, the Voronoi area can be considered as the contribution of the corresponding repeater, and thus a repeater with smaller Voronoi area is less effective. The so-called extremal optimization is a method to escape the local optimum by every time change the individual with the least fitness. This idea originally comes from the Bak-Sneppen model [20] that describes the punctuated equilibrium in evolution caused by the annihilation of the least fit species. In the simulation, we

<!-- b000322 | prose | pages [21] -->
cT   100 0.01 set and .

<!-- b000323 | prose | pages [21, 22] -->
Next we present the secondary algorithm, whose task is to assign each repeater a receiving frequency, a transmitting frequency and a PL tone. This algorithm will not change the locations of the repeaters obtained from the first algorithm, and will not add new repeaters. That is to say, this algorithm tries to maximize the reachable area of users just by rearranging the frequencies and PL tones of repeaters. The procedure of the algorithm is presented as follows.

<!-- b000324 | furniture | pages [22] -->
Team #9440              Page  21 / 40

<!-- b000326 | prose | pages [22] -->
40 Rp7

<!-- b000327 | prose | pages [22] -->
Rp4 30 Rp21 Rp3 20 Rp11 Rp13

<!-- b000328 | prose | pages [22] -->
10 Rp20 Rp16 Rp9 Rp10 0 Rp14 Rp8 Rp15 -10 Rp12 Rp2 Rp6 Rp19 Rp18 -20

<!-- b000329 | prose | pages [22] -->
Rp1 -30 Rp5 Rp17 -40 -40 -30 -20 -10 0 10 20 30 40

<!-- b000330 | caption | pages [22] -->
Figure 8: The red asterisks represent the repeaters while a green line connecting two repeaters if

<!-- b000331 | prose | pages [22] -->
they have the chance to transmit signals (i.e., within a distance R).

<!-- b000332 | prose | pages [22] -->
40 40 Rp20 Rp20 Rp13 Rp13 30 30 Rp8 Rp8 Rp3 Rp3 Rp10 Rp10 20 20 Rp9 Rp9 Rp12 Rp12 10 10 Rp5 Rp5 Rp17 Rp17 Rp16 Rp16 Rp2 Rp2 0 0

<!-- b000333 | prose | pages [22] -->
Rp4 Rp4 Rp7 Rp7 -10 -10 Rp18 Rp18 Rp21 Rp21 Rp1 Rp1 -20 -20 Rp6 Rp6 Rp11 Rp11 Rp19 Rp19 -30 -30 Rp15 Rp15

<!-- b000334 | prose | pages [22] -->
Rp14 Rp14 -40 -40 -40 -30 -20 -10 0 10 20 30 40 -40 -30 -20 -10 0 10 20 30 40

<!-- b000335 | prose | pages [22] -->
(a)A maximum spanning tree             (b) A minimum spanning tree

<!-- b000336 | caption | pages [22] -->
Figure 9: Illustration of the maximum spanning tree (a) and the minimum spanning tree (b) of G

<!-- b000337 | prose | pages [22] -->
The red lines are the edges in the spanning trees and green lines are the other edges in the graph G .

<!-- b000338 | prose | pages [22, 23] -->
(1) Construct a graph G to represent the relation that two repeaters have the ability to transmit signal to each other. That is to say, if the distance between two repeaters is less than R, we add one edge between them (see Fig. 8) (2) Find the minimum spanning tree T or the maximum spanning tree T of G . From ' the illustration shown in Fig. 9, one can see that edges in the minimum spanning tree will not intersect. If we build the signal transmission paths along the minimum spanning tree, the signals received by repeaters are fewer than the case of maximum spanning tree.

<!-- b000339 | furniture | pages [23] -->
Team #9440              Page  22 / 40

<!-- b000341 | prose | pages [23] -->
However, since the distance between two adjacent repeaters along the tree is the shortest, the received signals will be much stronger than other type of assignment. So the assignment based on the minimum spanning tree is suitable for communication in local area. In contrast, most edges in maximum spanning tree intersect with each other, the number of signals in many areas is very large and signals can cover larger areas.

<!-- b000342 | prose | pages [23] -->
However, this increases the possibility of frequency interference. For different purposes, one can choose different spanning tree to continue our algorithm.

<!-- b000343 | prose | pages [23] -->
(3) Remove edges from the spanning tree. For any node i whose degree k is larger than 3, we delete k-2 edges. Then the node i will be divided apart from k-2 connected components.

<!-- b000344 | prose | pages [23] -->
SC , then the method of removing edges can be Let the size of component j be j

<!-- b000345 | prose | pages [23] -->
  | SC SC | presented as follows: find k-2 edges to remove in order to minimize . a b a b , The results can be found in Fig. 10.

<!-- b000346 | prose | pages [23] -->
(4) After the step 3, we can obtain several distinct signal routes that do not connect. Assign a different PL tone to each distinct route. Then for the repeaters in each different route, assign its transmitting frequency and receiving frequency. Make sure the transmitting frequency of a repeater is the receiving frequency of the repeater’s neighbors in the same signal route.

<!-- b000347 | prose | pages [23] -->
40 40 Rp20 Rp20 Rp13 Rp13 30 30 Rp8 Rp8 Rp3 Rp3 Rp10 Rp10 20 20 Rp9 Rp9 Rp12 Rp12 10 10 Rp5 Rp5 Rp17 Rp17 Rp16 Rp16 Rp2 Rp2 0 0 Rp4 Rp4 Rp7 Rp7 -10 -10 Rp18 Rp18 Rp21 Rp21 Rp1 Rp1 -20 -20 Rp6 Rp6 Rp11 Rp11 Rp19 Rp19 -30 -30 Rp15 Rp15 Rp14 Rp14 -40 -40 -40 -30 -20 -10 0 10 20 30 40 -40 -30 -20 -10 0 10 20 30 40

<!-- b000348 | prose | pages [23] -->
(a)Signal routes in maximum spanning tree    (b) Signal routes in minimum spanning tree

<!-- b000349 | caption | pages [23] -->
Figure 10: The resulted routes after the removal of edges, corresponding to the spanning tree in

<!-- b000350 | prose | pages [23] -->
Fig 9. The red dashed lines represent the removed edges, while the blue solid lines are the reserved ones. The repeaters on the same blue line share the same tone.

<!-- b000351 | furniture | pages [24] -->
Team #9440              Page  23 / 40

<!-- b000352 | heading | pages [24] -->
6 Simulation Results

<!-- b000353 | prose | pages [24] -->
In this section, we present the strong solutions obtained by the proposed algorithm. The analysis in subsection 4.1 indicates that R is larger than the diameter of the considered area, and thus a solution is also a strong solution. In subsection 6.1 and 6.2, we will show the algorithmic results for N=1000 and N=10000, with R=85.45miles. The number if required repeaters are 11 and 104 respectively, better than the ones obtained by the naïve solution, 12 and 108. In subsection 6.1, we will prove that 11 is the optimal solution. Notice that, the calculation made in subsection 4.1 is based on an ideal circumstance, while the fog or rain can largely affect the transmitting of signal and reduce the effective communication range of a repeater. Therefore, in subsection 6.3 and 6.4, we will discuss the cases with shorter R. Since the communication range R will be affected by the weather, when discussing the interference, we should consider the case with large R to avoid possible interference in good weather while when discussing the global reachability, we should consider short R to make sure any point-to-point communication is possible even under bad weather. Therefore, as in the ideal case the communication range is larger than the diameter ( 2) of the considered area (when R , any two repeaters may interfere with each other) we always guarantee that the transmitter frequency difference between any two repeaters sharing the same PL tone is no less than 0.6MHz. In subsections 6.3 and 6.4, we assume that R=40miles.

<!-- b000354 | heading | pages [24] -->
6.1 N=1000, R=85.45

<!-- b000355 | caption | pages [24] -->
Figure 11 reports a solution with 11 repeaters obtained by our algorithm. The maximal

<!-- b000356 | prose | pages [24] -->
Voronoi area is 560.56, the user density is 0.1989, and thus the largest capacity demand is 112, smaller than the repeater’s capacity C=119. The advantage of this result compared with the naïve solution is twofold: (i) the number of required repeaters is smaller; (ii) the sizes of Voronoi areas of repeaters are more homogeneous. Detailed information of the repeaters is presented in Table 5.

<!-- b000357 | caption | pages [24] -->
Figure 11: The solution consisted of 11 repeaters obtained by our algorithm. The blue circle

<!-- b000358 | prose | pages [24] -->
denotes the considered area with radius 40miles, the red small circles represent the ability of receiving signals from users, and the blue points in the centers of the small red circles denote the positions of repeaters.

<!-- b000359 | furniture | pages [25] -->
Team #9440              Page  24 / 40

<!-- b000360 | caption | pages [25] -->
Table 5: The coordinates, frequencies and PL tones of the solution shown in Fig. 11.

<!-- b000361 | prose | pages [25] -->
Repeater x-Coordinate y-Coordinate Receiver Transmitter PL Tone No. Frequency Frequency 1 -38.3765 0.0000 145.6 145.0 1 2 -24.3880 -23.0549 146.3 145.7 1 3 -24.3880 23.0549 147.0 146.4 1 4 -12.4503 0.0000 147.7 147.1 1 5 -3.6744 -27.7292 147.4 148.0 1 6 -3.9222 27.5753 145.6 145.0 2 7 4.6059 0.0000 146.3 145.7 2 8 14.5012 26.5499 147.0 146.4 2 9 15.0139 -26.5499 147.7 147.1 2 10 29.2673 -11.0660 147.4 148.0 2 11 29.2673 11.0660 145.0 145.6 3

<!-- b000362 | prose | pages [25] -->
We next prove that the solution shown in Table 5 with 11 repeaters is the optimal solution, namely 10 repeaters with radius no more than 15.28miles cannot cover a circle with radius 40miles.

<!-- b000363 | prose | pages [25] -->
Lemma 1 [21]: Let r(n) be the maximum radius of a circular disc that can be covered by n closed unit circles, then r(n)=1+2cos(2π/(n−1)) for n=8, n=9, and n=10.

<!-- b000364 | prose | pages [25] -->
Proposition 3: To cover a circular area with radius 40, the least number of circles with radius 15.28 is 11.

<!-- b000365 | prose | pages [25] -->
Proof. Table 5 has already shown a possible solution, and thus we only need to prove that to cover with 10 circles is not possible. According to Lemma 1, r(10)=1+2cos(2/9π)=2.532, which is smaller than the ratio 40/15.28=2.618, and thus the coverage with 10 circles is not possible.

<!-- b000366 | prose | pages [25] -->
■

<!-- b000367 | heading | pages [25] -->
6.2 N=10000, R=85.45

<!-- b000368 | caption | pages [25] -->
Figure 12 reports a solution with 104 repeaters obtained by our algorithm, with the detailed

<!-- b000369 | prose | pages [25] -->
information of repeaters shown in Table 6. 21 PL tones are used to guarantee that every pair of repeaters will not interact each other.

<!-- b000370 | furniture | pages [26] -->
Team #9440              Page  25 / 40

<!-- b000371 | prose | pages [26] -->
40

<!-- b000372 | prose | pages [26] -->
30

<!-- b000373 | prose | pages [26] -->
20

<!-- b000374 | prose | pages [26] -->
10

<!-- b000375 | prose | pages [26] -->
0

<!-- b000376 | prose | pages [26] -->
-10

<!-- b000377 | prose | pages [26] -->
-20

<!-- b000378 | prose | pages [26] -->
-30

<!-- b000379 | prose | pages [26] -->
-40

<!-- b000380 | prose | pages [26] -->
-40 -30 -20 -10 0 10 20 30 40

<!-- b000381 | caption | pages [26] -->
Figure 12: The solution consisted of 104 repeaters obtained by our algorithm. The blue circle

<!-- b000382 | prose | pages [26] -->
denotes the considered area with radius 40miles, the red areas are the corresponding Voronoi areas and the blue points denote the positions of repeaters.

<!-- b000383 | caption | pages [26] -->
Table 6: The coordinates, frequencies and PL tones of the solution shown in Fig. 12.

<!-- b000384 | prose | pages [26, 27, 28, 29] -->
Repeater x-Coordinate y-Coordinate Receiver Transmitter PL No. Frequency Frequency Tone 1 -21.4846 10.7841 145.6 145.0 1 2 20.0881 9.8614 146.3 145.7 1 3 -24.3006 -16.2601 147.0 146.4 1 4 13.8192 -27.0256 147.7 147.1 1 5 -38.7037 -1.9022 147.4 148.0 1 6 1.0018 12.7802 145.6 145.0 2 7 -13.2011 13.9291 146.3 145.7 2 8 26.0811 8.6698 147.0 146.4 2 9 26.8280 -5.1802 147.7 147.1 2 10 -18.9492 -33.9863 147.4 148.0 2 11 -19.2527 17.5280 145.6 145.0 3 12 -36.7795 -10.8329 146.3 145.7 3 13 27.8500 -10.6307 147.0 146.4 3 14 19.6493 24.5973 147.7 147.1 3 15 -6.8453 -37.6773 147.4 148.0 3 16 -12.0455 -33.8082 145.6 145.0 4 17 18.2067 -4.1299 146.3 145.7 4 18 -31.0283 22.1830 147.0 146.4 4 19 14.0491 22.4823 147.7 147.1 4 20 -25.2712 28.5517 147.4 148.0 4 21 6.0148 9.6461 145.6 145.0 5 22 -5.2833 -22.9543 146.3 145.7 5 23 -24.2711 4.0665 147.0 146.4 5 24 -7.2155 -29.6266 147.7 147.1 5 25 23.5724 -18.8907 147.4 148.0 5 26 0.7092 -8.6258 145.6 145.0 6 27 -22.0810 22.4277 146.3 145.7 6 28 -4.6952 -3.5107 147.0 146.4 6 29 -28.4376 -23.5828 147.7 147.1 6 30 15.0935 36.0433 147.4 148.0 6 31 -10.0930 1.3872 145.6 145.0 7 32 8.9930 -33.6010 146.3 145.7 7 33 -10.8101 34.2136 147.0 146.4 7 34 -16.5338 28.0647 147.7 147.1 7 35 2.7253 -1.7304 147.4 148.0 7 36 -28.9439 -10.5425 145.6 145.0 8 37 28.9259 13.9310 146.3 145.7 8 38 17.4628 -20.3533 147.0 146.4 8 39 -18.4778 34.4848 147.7 147.1 8 40 -15.3172 -13.9991 147.4 148.0 8 41 -13.8680 -4.9981 145.6 145.0 9 42 -7.1204 9.4823 146.3 145.7 9 43 35.9930 -5.8130 147.0 146.4 9 44 -12.9073 -22.4915 147.7 147.1 9 45 6.5647 36.2554 147.4 148.0 9 46 23.7103 31.8433 145.6 145.0 10 47 -12.7061 22.2901 146.3 145.7 10 48 3.9099 -13.5329 147.0 146.4 10 49 -20.2166 -9.6509 147.7 147.1 10 50 -19.1212 -0.5781 147.4 148.0 10 51 1.7840 -38.9554 145.6 145.0 11 52 6.1130 -27.4748 146.3 145.7 11 53 13.3601 15.2740 147.0 146.4 11 54 -15.5091 -26.6073 147.7 147.1 11 55 35.3109 -13.2947 147.4 148.0 11 56 -25.5448 -4.7593 145.6 145.0 12 57 30.9858 19.5100 146.3 145.7 12 58 8.6603 -20.2950 147.0 146.4 12 59 -15.3072 6.1877 147.7 147.1 12 60 -8.2420 26.4597 147.4 148.0 12 61 -1.3574 21.7607 145.6 145.0 13 62 -19.9827 -20.4432 146.3 145.7 13 63 -30.1025 8.9472 147.0 146.4 13 64 5.9444 17.4680 147.7 147.1 13 65 -0.5221 29.9967 147.4 148.0 13 66 0.6271 -29.8848 145.6 145.0 14 67 -3.6197 -13.9964 146.3 145.7 14 68 5.9811 23.8501 147.0 146.4 14 69 -32.7771 -17.8837 147.7 147.1 14 70 9.2566 -6.0159 147.4 148.0 14 71 20.3993 -11.3469 145.6 145.0 15 72 28.6670 -25.6027 146.3 145.7 15 73 38.1683 1.7115 147.0 146.4 15 74 -36.8485 6.2865 147.7 147.1 15 75 12.1489 -10.6071 147.4 148.0 15 76 -36.2190 14.8745 145.6 145.0 16 77 15.3432 29.9396 146.3 145.7 16 78 37.3272 13.5208 147.0 146.4 16 79 12.7538 1.2800 147.7 147.1 16 80 -8.7399 -8.9681 147.4 148.0 16 81 -23.6555 -27.8664 145.6 145.0 17 82 22.1340 -28.0080 146.3 145.7 17 83 30.7725 -18.5245 147.0 146.4 17 84 -9.5450 -17.3707 147.7 147.1 17 85 13.0948 -15.5244 147.4 148.0 17 86 34.6099 6.7702 145.6 145.0 18 87 18.0988 -32.7824 146.3 145.7 18 88 13.6878 7.6081 147.0 146.4 18 89 5.6810 2.5887 147.7 147.1 18 90 -31.1704 0.1887 147.4 148.0 18 91 10.9276 -37.9560 145.6 145.0 19 92 21.3901 2.2075 146.3 145.7 19 93 -0.1086 -34.3627 147.0 146.4 19 94 7.9409 29.8451 147.7 147.1 19 95 0.6967 -21.3952 147.4 148.0 19 96 -27.7998 16.0646 145.6 145.0 20 97 -1.9265 4.5995 146.3 145.7 20 98 -5.8836 17.3017 147.0 146.4 20 99 21.6476 17.3278 147.7 147.1 20 100 29.7908 0.7205 147.4 148.0 20 101 -6.6019 34.9874 145.6 145.0 21 102 26.8732 24.1059 146.3 145.7 21 103 -0.9480 37.5368 147.0 146.4 21 104 -34.8281 -5.6874 147.7 147.1 21

<!-- b000385 | furniture | pages [27] -->
Team #9440              Page  26 / 40

<!-- b000387 | furniture | pages [28] -->
Team #9440              Page  27 / 40

<!-- b000389 | furniture | pages [29] -->
Team #9440              Page  28 / 40

<!-- b000391 | heading | pages [29] -->
6.3 N=1000, R=40

<!-- b000392 | prose | pages [29] -->
As mentioned in Section 5, we will not add more repeaters to make sure every user can communicate with other users at any positions in the considered area. Instead, our secondary algorithm tries to maximize the reachable areas of users. Therefore, the repeaters’ locations of the solutions in subsections 6.3 and 6.4 are the same to those in subsections 6.1 and 6.2. However, the frequencies and PL tones are different.

<!-- b000393 | caption | pages [29] -->
Table 7: The coordinates, frequencies and PL tones of the solution shown in Fig. 11.

<!-- b000394 | prose | pages [29] -->
Repeater x-Coordinate y-Coordinate Receiver Transmitter PL Tone No. Frequency Frequency 1 -38.3765 0.0000 145.0 145.6 1 2 -24.3880 -23.0549 145.0 145.6 2 3 -24.3880 23.0549 145.0 145.6 3 4 -12.4503 0.0000 145.6 146.2 1 5 -3.6744 -27.7292 145.6 146.2 2 6 -3.9222 27.5753 145.6 146.2 3 7 4.6059 0.0000 146.2 146.8 1 8 14.5012 26.5499 146.2 146.8 3 9 15.0139 -26.5499 146.2 146.8 2 10 29.2673 -11.0660 146.8 147.4 2 11 29.2673 11.0660 146.8 147.4 3

<!-- b000395 | caption | pages [29] -->
Table 7 presents the result for N=1000. To test the effectiveness of the secondary algorithm,

<!-- b000396 | prose | pages [29] -->
we randomly pick up 100000 ordered pairs of points (u,v) inside the considered area to see in how many pairs, u can send to v signals. The answer is 90708, namely given a user, the probability that the system can satisfy this user’s requirement to communicate with a random user is about 90.71%.

<!-- b000397 | heading | pages [29] -->
6.4 N=10000, R=40

<!-- b000398 | caption | pages [29] -->
Table 8 reports the result for N=10000. Similar to the solution in subsection 6.4, this solution

<!-- b000399 | prose | pages [29, 30, 31, 32] -->
could not guarantee that a user can communicate with other users in any positions in the considered area. However, it seems that when the required number of repeaters increases, the reachable area of a user increases. For example, in this case, for the solution shown in Table 8, the corresponding probability is 97.12%。 Repeater x-Coordinate y-Coordinate Receiver Transmitter PL No. Frequency Frequency Tone 1 -21.4846 10.7841 145.0 145.6 1 2 20.0881 9.8614 145.6 146.2 2 3 -24.3006 -16.2601 145.6 146.2 3 4 13.8192 -27.0256 145.0 145.6 4 5 -38.7037 -1.9022 145.0 145.6 5 6 1.0018 12.7802 145.6 146.2 6 7 -13.2011 13.9291 145.0 145.6 7 8 26.0811 8.6698 146.2 146.8 2 9 26.8280 -5.1802 145.6 146.2 8 10 -18.9492 -33.9863 145.0 145.6 9 11 -19.2527 17.5280 145.6 146.2 1 12 -36.7795 -10.8329 146.2 146.8 5 13 27.8500 -10.6307 145.0 145.6 8 14 19.6493 24.5973 146.2 146.8 10 15 -6.8453 -37.6773 146.2 146.8 9 16 -12.0455 -33.8082 145.6 146.2 9 17 18.2067 -4.1299 145.6 146.2 11 18 -31.0283 22.1830 145.0 145.6 12 19 14.0491 22.4823 145.0 145.6 13 20 -25.2712 28.5517 146.8 147.4 1 21 6.0148 9.6461 146.2 146.8 6 22 -5.2833 -22.9543 145.6 146.2 14 23 -24.2711 4.0665 146.2 146.8 15 24 -7.2155 -29.6266 146.2 146.8 14 25 23.5724 -18.8907 145.6 146.2 16 26 0.7092 -8.6258 145.6 146.2 17 27 -22.0810 22.4277 146.2 146.8 1 28 -4.6952 -3.5107 146.2 146.8 18 29 -28.4376 -23.5828 145.6 146.2 19 30 15.0935 36.0433 145.0 145.6 10 31 -10.0930 1.3872 145.6 146.2 18 32 8.9930 -33.6010 145.6 146.2 20 33 -10.8101 34.2136 145.6 146.2 21 34 -16.5338 28.0647 146.2 146.8 22 35 2.7253 -1.7304 146.2 146.8 17 36 -28.9439 -10.5425 146.2 146.8 3 37 28.9259 13.9310 146.8 147.4 2 38 17.4628 -20.3533 145.0 145.6 16 39 -18.4778 34.4848 145.0 145.6 21 40 -15.3172 -13.9991 146.2 146.8 24 41 -13.8680 -4.9981 145.6 146.2 22 42 -7.1204 9.4823 145.6 146.2 7 43 35.9930 -5.8130 145.0 145.6 1 44 -12.9073 -22.4915 145.6 146.2 25 45 6.5647 36.2554 145.0 145.6 26 46 23.7103 31.8433 146.8 147.4 10 47 -12.7061 22.2901 145.6 146.2 22 48 3.9099 -13.5329 145.0 145.6 17 49 -20.2166 -9.6509 145.6 146.2 24 50 -19.1212 -0.5781 145.0 145.6 22 51 1.7840 -38.9554 145.0 145.6 27 52 6.1130 -27.4748 145.0 145.6 20 53 13.3601 15.2740 145.6 146.2 13 54 -15.5091 -26.6073 145.0 145.6 25 55 35.3109 -13.2947 145.6 146.2 1 56 -25.5448 -4.7593 145.0 145.6 24 57 30.9858 19.5100 145.0 145.6 28 58 8.6603 -20.2950 145.0 145.6 29 59 -15.3072 6.1877 145.0 145.6 18 60 -8.2420 26.4597 145.0 145.6 22 61 -1.3574 21.7607 145.6 146.2 30 62 -19.9827 -20.4432 145.0 145.6 3 63 -30.1025 8.9472 145.6 146.2 15 64 5.9444 17.4680 145.0 145.6 6 65 -0.5221 29.9967 145.0 145.6 31 66 0.6271 -29.8848 146.2 146.8 27 67 -3.6197 -13.9964 145.0 145.6 5 68 5.9811 23.8501 146.2 146.8 26 69 -32.7771 -17.8837 145.0 145.6 19 70 9.2566 -6.0159 146.8 147.4 29 71 20.3993 -11.3469 146.2 146.8 11 72 28.6670 -25.6027 146.8 147.4 4 73 38.1683 1.7115 145.0 145.6 32 74 -36.8485 6.2865 145.0 145.6 15 75 12.1489 -10.6071 146.2 146.8 29 76 -36.2190 14.8745 146.2 146.8 12 77 15.3432 29.9396 145.6 146.2 10 78 37.3272 13.5208 145.6 146.2 32 79 12.7538 1.2800 145.6 146.2 10 80 -8.7399 -8.9681 146.2 146.8 23 81 -23.6555 -27.8664 146.2 146.8 19 82 22.1340 -28.0080 146.2 146.8 4 83 30.7725 -18.5245 146.2 146.8 16 84 -9.5450 -17.3707 146.2 146.8 25 85 13.0948 -15.5244 145.6 146.2 29 86 34.6099 6.7702 145.6 146.2 32 87 18.0988 -32.7824 145.6 146.2 4 88 13.6878 7.6081 145.0 145.6 2 89 5.6810 2.5887 145.0 145.6 14 90 -31.1704 0.1887 145.6 146.2 10 91 10.9276 -37.9560 146.2 146.8 20 92 21.3901 2.2075 145.0 145.6 11 93 -0.1086 -34.3627 145.6 146.2 27 94 7.9409 29.8451 145.6 146.2 26 95 0.6967 -21.3952 145.0 145.6 14 96 -27.7998 16.0646 145.6 146.2 12 97 -1.9265 4.5995 146.2 146.8 7 98 -5.8836 17.3017 145.0 145.6 30 99 21.6476 17.3278 145.0 145.6 14 100 29.7908 0.7205 146.2 146.8 8 101 -6.6019 34.9874 146.2 146.8 21 102 26.8732 24.1059 145.6 146.2 28 103 -0.9480 37.5368 145.6 146.2 31 104 -34.8281 -5.6874 145.6 146.2 5

<!-- b000400 | furniture | pages [30] -->
Team #9440              Page  29 / 40

<!-- b000401 | caption | pages [30] -->
Table 8: The coordinates, frequencies and PL tones of the solution shown in Fig. 12.

<!-- b000403 | furniture | pages [31] -->
Team #9440              Page  30 / 40

<!-- b000405 | furniture | pages [32] -->
Team #9440              Page  31 / 40

<!-- b000407 | furniture | pages [33] -->
Team #9440              Page  32 / 40

<!-- b000408 | heading | pages [33] -->
7 Sensitivity Analysis

<!-- b000409 | prose | pages [33] -->
In subsection 7.1, we will investigate the sensitive of the algorithmic output versus the change of model parameters. In subsection 7.2, we will analysis the error caused by the continuous approximation of user density. In subsection 7.3, we will discuss the possible defects in line-of-sight propagation caused by mountainous areas, as well as some promising ways in solving the repeater placement problem in such circumstance.

<!-- b000410 | heading | pages [33] -->
7.1 Sensitivity of Parameters

<!-- b000411 | prose | pages [33] -->
Most parameters hereinbefore are regarded as constants. However, parameters can be regulated in a certain range, which may have a huge impact on the algorithmic results. Here we discuss to what extent the results depend on the parameters.

<!-- b000412 | caption | pages [33] -->
Figure 13: The Comparison between the least numbers of required repeaters obtained by the

<!-- b000413 | prose | pages [33] -->
proposed algorithm and the Naïve solution. The largest coverable circle in naïve solution 1 is centered at the center of the central hexagon, while the largest coverable circle in naïve solution 2 is centered at the intersection of the three more central hexagons.

<!-- b000414 | caption | pages [33] -->
Figure 13 shows the least number of repeaters versus the number of users. The number of

<!-- b000415 | prose | pages [33] -->
users varies from 100 to 10000. It is clear that the proposed algorithm is better than the Naïve solution. Notice that there is a transition point at about N=1000, which approximately satisfies the equation N C  (18)    2 2 r Before this transition point, the number of repeaters mainly depends on the communication range r, while after this transition point, capacity becomes the bottleneck determining the least number of require repeaters. Actually, given the considered area, the least number of repeaters keeps as a constant before the transition point. Since the capacity limitation will play the major role when many users are presented, it is not a surprise that the growing tendency of the number of repeaters is linear versus the number of users.

<!-- b000416 | furniture | pages [34] -->
Team #9440              Page  33 / 40

<!-- b000417 | caption | pages [34] -->
Figure 14 reports the relation between the least number of required repeaters and the user’s

<!-- b000418 | prose | pages [34] -->
communication range r. The curves have been normalized through dividing by their respective largest value. In the case N=10000, the number of repeaters never changes with r, again indicating that the capacity limitation determines the result, while when N=1000, the number of repeaters decreases with the increase of user’s communication range.

<!-- b000419 | caption | pages [34] -->
Figure 14: The Comparison between the least numbers of required repeaters obtained by the

<!-- b000420 | prose | pages [34] -->
proposed algorithm and the Naïve solution. The red and black points correspond to the case of N=10000 and N=1000, respectively. Two curves have been normalized.

<!-- b000421 | heading | pages [34] -->
7.2 User Density Fluctuation

<!-- b000422 | prose | pages [34] -->
In the analysis of our model, the user density is a constant in the considered area, behaving like a real variable. However, in reality, the number of users can only be an integer. If we consider the discrete case where users are distributed uniformly, then in a Voronoi area Sv centered by a

<!-- b000423 | prose | pages [34] -->
, and thus the number of 2 vS repeater. Each user belongs to this area with the probability

<!-- b000424 | prose | pages [34] -->
users in this area, X, obeys a Bernoulli distribution

<!-- b000425 | prose | pages [34] -->
 X N X   N   S S   v v P X ( ) 1 (19)         2 2 X     

<!-- b000426 | prose | pages [34] -->
whose mathematical expectation and standard deviation are

<!-- b000427 | prose | pages [34] -->
    2 E X ( ) NS S (20) v v

<!-- b000428 | prose | pages [34] -->
and

<!-- b000429 | prose | pages [34] -->
  NS S S       v v v ( X ) 1 S 1 (21)   v       2 2 2  

<!-- b000430 | prose | pages [34] -->
When the total number of users N is small, the capacity is not a big problem, and when N is big (corresponding to high user density), the area Sv should be small due to the capacity limitation.

<!-- b000431 | furniture | pages [35] -->
Team #9440              Page  34 / 40

<!-- b000432 | prose | pages [35] -->
Therefore, the standard deviation is about the square root of the expected number of users in the Voronoi area. Of course, we are interested in the case when the number of users in Sv is approaching to the capacity limitation. For example, in this problem, C=119, and thus the standard deviation is about 11. If we would like to set up a tolerance for two times of the standard deviation, the tolerant capacity C’ should satisfy the approximate equation

<!-- b000433 | prose | pages [35] -->
 

<!-- b000434 | heading | pages [35] -->
C C

<!-- b000435 | prose | pages [35] -->
' 2 ' C (22)

<!-- b000436 | prose | pages [35] -->
leading to an answer C’=99. The qualitative relation is trivial, namely higher tolerance leads to lower capacity and generally corresponds to more repeaters.

<!-- b000437 | heading | pages [35] -->
7.3 Effects of Landscape: Discussing the Mountainous Areas

<!-- b000438 | prose | pages [35] -->
Completely flat area is just a kind of ideal assumption, but the complex landscape is common which should be taken into consideration. Actually, there might be defects in line-of-sight propagation caused by mountainous areas. Here we analyze the impact of landscape on signal transmission, and based on the analysis, we put forward a proposal on how to arrange the position and tone of repeaters.

<!-- b000439 | prose | pages [35] -->
Because the VHF radio spectrum involves line-of-sight transmission and reception, the mountain will obstruct the signal’s diffusion along the straight line. On the other hand, it makes a contribution to avoiding the interference between the two repeaters, even if they are geographically nearby and use close transmitter frequencies. The available spectrum is in the range from 145 to 148MHz and the wavelength is about 2 meters, so the signal wave have a strong ability to bypass the a dwarf, small or single mountain according to diffraction properties of wave. In a word, the situation that the area is full of rolling mountains is the point we should focus on.

<!-- b000440 | furniture | pages [36] -->
Team #9440              Page  35 / 40

<!-- b000441 | caption | pages [36] -->
Figure 15: An illustration about how a signal can be transmitted from a hollow area to a distant

<!-- b000442 | prose | pages [36] -->
place with the help of a hierarchically organized relay network.

<!-- b000443 | prose | pages [36] -->
The proposal put forward here is based on hierarchical organization. We divide all the repeaters into two levels. The repeaters of the first (lower) level, are always located at hollows to make sure all the users can be covered by at least one repeater. The repeaters of the second (higher) level are always located at the top of maintain, who play a central role in the information transmission. The higher altitude the repeater locates at, the wider its communication range is. Comparatively, the signal from hollow is difficult to be received by repeaters. According to the

<!-- b000444 | prose | pages [36] -->
, we must design a suitable arrangement of repeaters covering all the connectivity constrain 3

<!-- b000445 | prose | pages [36] -->
users, so we first put some repeaters in the hollow, and erect them highly enough to make sure the signal they received can be transmitted to a second-lever repeater. The second-level repeaters are always put on the top of maintains to expand the range of radiation, who can communicate with other second-level repeaters. Through such a hierarchically organized relay network, a signal can be transmitted from a hollow area to a distant place, just like what is shown in Fig. 15. The mountains narrow the range of radiation, so we must use more repeaters in mountainous area than flat area and this make arrangement of PL tones difficult. Considering the mountain between first-level repeaters can avoid the interference, they can share the same tone and the same transmitter frequency. If a first-level repeater can be covered by two second-level repeaters, it chooses the nearest repeater to send signals. So that a second-level repeater may receive signals from several first-level repeaters simultaneously, and the signals transmitted to several first-level repeaters can pass through a second-level repeater. We set all the first-level repeaters covered by one second-level repeater share the same transmitter frequency, and share the PL same tone with the second-level repeater. In this way, we reduce the number of PL tones. We only need to distribute PL tones to secondary repeaters using the same way in the flat area. Then we set the receiver frequency of a first-level repeater being equal to the transmitter frequency of the corresponding second-level repeater, and set the transmitter frequency of a first-level repeater being equal to the receiver frequency of the corresponding second-level repeater.

<!-- b000446 | furniture | pages [37] -->
Team #9440              Page  36 / 40

<!-- b000447 | heading | pages [37] -->
8 Conclusion and Discussion

<!-- b000448 | prose | pages [37] -->
In this paper, we propose a two-tiered network model, where lower-power users can communicate with one another through repeaters. The capacity limitation and interference have been taken into consideration in our model. Motivated by the structure of cellular networks, we give a naïve solution where the number of repeaters and their positions can be obtained analytically. We further propose an iterative extremal optimization algorithm based on the Voronoi diagram. The proposed algorithm outperforms the naïve solution. For the case of 1000 users, it obtains a solution with 11 repeaters, which has been proved to be the real optimum. For the case of 10000 users, it obtains a solution with 104 repeaters, better than the naïve solution with 108 repeaters. Moreover, we proposed an algorithm based on maximum and minimum spanning tree to assign frequencies and private line tones. This algorithm does not introduce any new repeaters yet can largely broaden the reachable areas of users. For example, in the case of 10000 users, given a user, the probability this user can successfully send signal to a random position in the considered area is about 97.12%.

<!-- b000449 | prose | pages [37] -->
Compared with the related model for sensor wireless networks and mobile communication networks, our model is more general. The proposed algorithm is very effective and efficient: it runs much faster than the simulated annealing approach [12] and is of higher ability to escape the local optimum than another iterative refinement algorithm [22]. Concepts and methods from disparate scientific domains are well integrated in this algorithm, such as the extremal optimization from statistical physics community, the Voronoi diagram from geographic information science, and iterative refinement framework from computer science. Another advantage of the algorithm is that it can be widely applied since it does not require any specific geographical features of the considered area, while many efficient circle-covering algorithms only work well for squares.

<!-- b000450 | prose | pages [37] -->
There are also two considerable weaknesses in this work. Firstly, we have not developed an effective algorithm to satisfy the constrain of global reachability without adding too many repeaters. Secondly, our model is largely simplified, which have not taken into account the heterogeneity of users and repeaters, or the wave reflection and refraction by atmosphere.

<!-- b000451 | furniture | pages [38] -->
Team #9440              Page  37 / 40

<!-- b000452 | heading | pages [38] -->
Appendix A  Table of Parameters

<!-- b000453 | prose | pages [38] -->
For convenience, here we list parameters used in this paper. The detailed definitions can be found in the main content. The values of the parameters, expect for those free parameters, are also presented in this Table. Some values are given in the contest problem itself or directly obtained from literatures, while others are calculated according to our model. Details can be found in the main content.

<!-- b000454 | caption | pages [38] -->
Table 9: Parameters appeared in this paper.

<!-- b000455 | prose | pages [38] -->
Parameter Brief Description Value/Range  Radius of the considered circular area 40 miles N Number of users need to be accommodated Tunable parameter. Two cases, N=1000 and N=10000, are emphasized in this paper fr Receiver frequency of a repeater  [145MHz,148MHz]

<!-- b000456 | prose | pages [38] -->
ft Transmitter frequency of a repeater  [145MHz,148MHz]

<!-- b000457 | prose | pages [38] -->
nPL Specific PL tone of a repeater  {1,2,...,54}

<!-- b000458 | prose | pages [38] -->
NPL Total number of available PL tones 54 R Communication radius of a repeater 85.45 miles fc Threshold of the frequency difference, below 0.6MHz which interference may happen r Maximal distance for a user to send signals to a 15.28 miles repeater C Capacity of a repeater 119 users C’ Tolerant capacity of a repeater 99 users Loss of feed system for transmitter 2dB L f out ,

<!-- b000459 | prose | pages [38] -->
Loss of feed system for receiver 2dB L f in ,

<!-- b000460 | prose | pages [38] -->
Other loss of the transmitter 1dB L b out ,

<!-- b000461 | prose | pages [38] -->
Other loss of the receiver 1dB L b in ,

<!-- b000462 | prose | pages [38] -->
Antenna gain of the transmitter 39dB G out

<!-- b000463 | prose | pages [38] -->
Antenna gain of the receiver 39dB G in

<!-- b000464 | prose | pages [38] -->
Effective radiated power of a repeater 100W P ,r out

<!-- b000465 | prose | pages [38] -->
Actual power of received signal for a repeater   P

<!-- b000466 | heading | pages [38] -->
1 W

<!-- b000467 | prose | pages [38, 39] -->
,r in Effective radiated power of a user 3.2W P u out ,

<!-- b000468 | furniture | pages [39] -->
Team #9440              Page  38 / 40

<!-- b000470 | prose | pages [39] -->
Actual power of received signal for a user   P

<!-- b000471 | heading | pages [39] -->
1 W

<!-- b000472 | prose | pages [39] -->
u in ,

<!-- b000473 | prose | pages [39] -->
Bit energy-to-noise density ratio 18dB for transceiver, and E N b 0 always in the range 5-30dB V Voice gain 0.4dB  The information bit rate bps Threshold to judge whether the iterative 0.01miles  refinement is converged Tc Threshold to judge whether we should stop the 100 extremal optimization operation

<!-- b000474 | heading | pages [39] -->
Appendix B  Table of Symbols

<!-- b000475 | prose | pages [39] -->
For convenience, here we list mathematical used in this paper. The detailed definitions can be found in the main content.

<!-- b000476 | caption | pages [39] -->
Table 10: Mathematical symbols appeared in this paper.

<!-- b000477 | heading | pages [39] -->
Symbol

<!-- b000478 | prose | pages [39] -->
Description  The circular area described in the problem D A two-tiered directed network Interference from other repeaters I other

<!-- b000479 | prose | pages [39] -->
Interference from itself I self

<!-- b000480 | prose | pages [39] -->
The set of users V u

<!-- b000481 | prose | pages [39] -->
The set of users V ' u

<!-- b000482 | prose | pages [39] -->
The set of repeaters V r

<!-- b000483 | prose | pages [39] -->
SNR Signal-to-noise ratio The set of directed links from users to repeaters E ur

<!-- b000484 | prose | pages [39] -->
The set of directed links from repeaters to repeaters E rr

<!-- b000485 | prose | pages [39] -->
A user iu

<!-- b000486 | prose | pages [39] -->
A repeater ir

<!-- b000487 | prose | pages [39, 40] -->
S ( ) r jr The Voronoi area of a repeater V j S u ( ) iu The reachable area of a user r i

<!-- b000488 | furniture | pages [40] -->
Team #9440              Page  39 / 40

<!-- b000490 | prose | pages [40] -->
R u ( ) iu The reachable repeaters of a user r i  Density of users M Number of repeaters B Bandwidth Pur Power of signal from a user to a repeater T The minimal spanning tree T’ The maximum spanning tree

<!-- b000491 | heading | pages [40] -->
Appendix C  Summary of Assumptions

<!-- b000492 | prose | pages [40] -->
For convenience, here we summary all the important assumptions made for our model. Notice that, these assumptions also appeared in the model description of the main content.

<!-- b000493 | prose | pages [40] -->
[A1]. Users are uniformly distributed in the considered area, and in a more strong assumption, we consider the number of users as a real variable and the user density in the considered area is a constant.

<!-- b000494 | prose | pages [40] -->
[A2]. Users prefer to communicate with the nearest repeaters.

<!-- b000495 | prose | pages [40] -->
[A3]. Considering two repeaters sharing the same PL tone and the difference between their transmitter frequencies is less than a threshold fc=0.6MHz. If the distance between them is less than 2R, they will interfere with each other.

<!-- b000496 | prose | pages [40] -->
[A4]. The considered circular area is a place where wireless signals can fade freely, which means there are not any other sorts of interference such as fogs, rivers, hills, buildings, activities of sun and so forth, so the fading of signals under such situation is only due to the distance across.

<!-- b000497 | prose | pages [40] -->
[A5]. There is no background noise in this system.

<!-- b000498 | prose | pages [40] -->
[A6]. Repeaters don’t have noisy impact on others.

<!-- b000499 | prose | pages [40] -->
[A7]. Functionalities and specifications of users’ radios are the same (i.e., homogeneous users’ radios). Functionalities and specifications of radio repeaters are the same (i.e., homogeneous repeaters).

<!-- b000500 | heading | pages [40] -->
References

<!-- b000501 | references | pages [40] -->
[1] K. T. Phan et al., Power Allocation in Wireless Multi-User Relay Networks, IEEE Trans.

<!-- b000502 | references | pages [40] -->
Wireless Commun. 8 (2009) 2535.

<!-- b000503 | references | pages [40] -->
[2] W. Shi, S. Roy, Achieving Full Diversity by Selection in Arbitrary Multi-hop

<!-- b000504 | references | pages [40] -->
Amplify-and-Forward Relay Networks, GLOBECOM 2009, IEEE Press.

<!-- b000505 | references | pages [40] -->
[3] T. C.-K. Liu et al., Adaptive Power Allocation for Bidirectional Amplify-and-Forward

<!-- b000506 | references | pages [40] -->
Multiple-Relay Multiple-User Networks, GLOBECOM 2010, IEEE Press.

<!-- b000507 | references | pages [40] -->
[4] A. Nosratinia, T. E. Hunter, A. Hedayat, Cooperative Communication in Wireless Networks,

<!-- b000508 | references | pages [40] -->
IEEE Commun. Magazine 3 (2004) 74.

<!-- b000509 | references | pages [40] -->
[5] http://en.wikipedia.org/wiki/Amateur_radio

<!-- b000510 | references | pages [40] -->
[6] I. F. Akyildiz, W. Su, Y. Sankarasubramaniam, E. Cayirci, Wireless sensor networks: a survey,

<!-- b000511 | references | pages [40] -->
Comput. Netw. J. 38 (2002) 393.

<!-- b000512 | references | pages [40] -->
[7] J. Pan, Y. T. Hou, L. Cai, Y. Shi, S. X. Shen, Topology control for wireless sensor networks,

<!-- b000513 | furniture | pages [41] -->
Team #9440              Page  40 / 40

<!-- b000514 | references | pages [41] -->
MOBICOM 2003, ACM Press.

<!-- b000515 | references | pages [41] -->
[8] G. Gupta, M. Younis, Fault-tolerant clustering of wireless sensor networks, WCNC 2003, IEEE

<!-- b000516 | references | pages [41] -->
Press.

<!-- b000517 | references | pages [41] -->
[9] G. Gupta, M. Younis, Load-balanced clustering of wireless sensor networks, WCNC 2003,

<!-- b000518 | references | pages [41] -->
IEEE Press.

<!-- b000519 | references | pages [41] -->
[10] J. Tang, B. Hao, A. Sen, Relay node placement in large scale wireless sensor networks,

<!-- b000520 | references | pages [41] -->
Comput. Commun. 29 (2006) 490.

<!-- b000521 | references | pages [41] -->
[11] R. J. Fowler, M. S. Paterson, S. L. Tanimoto, Optimal packing and covering in the plane are

<!-- b000522 | references | pages [41] -->
NP-complete, Information Processing Letter 12 (1981) 133.

<!-- b000523 | references | pages [41] -->
[12] K. J. Nurmela, P. R. J. Ostergard, Covering a square with up to 30 Equal Circles, Research

<!-- b000524 | references | pages [41] -->
Report HUT-TCS-A62, Laboratory for Theoretical Computer Science, Helsinky University of

<!-- b000525 | references | pages [41] -->
Technology, 2000.

<!-- b000526 | references | pages [41] -->
[13] F. Aurenhammer, Voronoi Diagrams - A Survey of a Fundamental Geometric Data Structure,

<!-- b000527 | references | pages [41] -->
ACM Computing Surveys 23 (1991) 345.

<!-- b000528 | references | pages [41] -->
[14] http://en.wikipedia.org/wiki/Circumcircle

<!-- b000529 | references | pages [41] -->
[15] S. Boettcher, A. G. Percus, Optimization with Extremal Dynamics, Phys. Rev. Lett. 86 (2001)

<!-- b000530 | references | pages [41] -->
5211.

<!-- b000531 | references | pages [41] -->
[16] T. Zhou, W.-J. Bai, L.-J. Cheng, B.-H. Wang, Continuous extremal optimization for

<!-- b000532 | references | pages [41] -->
Lennard-Jones Clusters, Phys. Rev. E 72 (2005) 016702.

<!-- b000533 | references | pages [41] -->
[17] C. A. Balanis, Antenna Theory: Analysis and Design (3rd Edition), John Wiley &. Sons, 2005.

<!-- b000534 | references | pages [41] -->
[18] K. S. Gilhousen et al., On the Capacity of a Cellular CDMA System, IEEE Trans. Vehicular

<!-- b000535 | references | pages [41] -->
Technology 40 (1991) 303.

<!-- b000536 | references | pages [41] -->
[19] N. Megiddo, Linear-time algorithms for linear programming in R3 and related problems,

<!-- b000537 | references | pages [41] -->
SIAM J. Comput. 12 (1983) 759.

<!-- b000538 | references | pages [41] -->
[20] P. Bak, K. Sneppen, Punctuated equilibrium and criticality in a simple model of evolution,

<!-- b000539 | references | pages [41] -->
Phys. Rev. Lett. 71 (1993) 4083.

<!-- b000540 | references | pages [41] -->
[21] G. F. Toth, Thinnest Covering of a Circle by Eight, Nine, or Ten Congruent Circles,

<!-- b000541 | references | pages [41] -->
Combinatorial &. Computational Geometry 52 (2005) 361.

<!-- b000542 | references | pages [41] -->
[22] G. K. Das, S. Das, S. C. Nandy, B. P. Sinha, Efficient algorithm for placing a given number of

<!-- b000543 | references | pages [41] -->
base stations to cover a convex region, J. Parallel &. Distributed Comput. 66 (2006) 1353.
