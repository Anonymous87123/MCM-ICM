# P-B-2011-9440-95f0fa40

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [2] -->
Team #9440              Page  1 / 40

<!-- b000002 | prose | pages [2] -->
Least Number of Repeaters Covering a

<!-- b000003 | prose | pages [2] -->
Circular Area: Iterative Extremal

<!-- b000004 | prose | pages [2] -->
Optimization Based on Voronoi Diagram

<!-- b000005 | furniture | pages [2] -->


<!-- b000006 | heading | pages [2] -->
Abstract

<!-- b000007 | prose | pages [2] -->
In this paper, we propose a two-tiered network model, where lower-power users can

<!-- b000008 | prose | pages [2] -->
communicate with one another through repeaters, which amplify weak signals and

<!-- b000009 | prose | pages [2] -->
retransmit them. A repeater is of limited capacity and may interfere with a nearby

<!-- b000010 | prose | pages [2] -->
repeater if their transmitter frequencies are close and they share the same private line

<!-- b000011 | prose | pages [2] -->
tone. Our objective is to place the least number of repeaters that can satisfy the users’

<!-- b000012 | prose | pages [2] -->
communication requirement: the weak requirement is that every user must be covered

<!-- b000013 | prose | pages [2] -->
by at least one repeater while the strong requirement is that every user can

<!-- b000014 | prose | pages [2] -->
communicate with another user in any position of the considered area. Motivated by

<!-- b000015 | prose | pages [2] -->
the structure of cellular networks, we give a naïve solution where the number of

<!-- b000016 | prose | pages [2] -->
repeaters and their positions can be obtained analytically. In a circular area with radius

<!-- b000017 | heading | pages [2] -->
40 miles, 12 repeaters are enough to accommodate 1000 simultaneous users. We

<!-- b000018 | heading | pages [2] -->
further propose an iterative refinement algorithm consisting of three fundamental

<!-- b000019 | prose | pages [2] -->
modules: to draw the Voronoi diagram, to determine the circumscribed circles of

<!-- b000020 | prose | pages [2] -->
Voronoi areas and move the repeaters to the centers of these circumscribed circles,

<!-- b000021 | prose | pages [2] -->
and to escape the local optimum by using the idea of extremal optimization. The

<!-- b000022 | prose | pages [2] -->
proposed algorithm outperforms the naïve solution. For the case of 1000 users, it

<!-- b000023 | prose | pages [2] -->
obtains a solution with 11 repeaters, which can be proved to be the real optimum. For

<!-- b000024 | prose | pages [2] -->
the case of 10000 users, it obtains a solution with 104 repeaters, better than the naïve

<!-- b000025 | prose | pages [2] -->
solution with 108 repeaters. We further discuss how to assign frequencies and private

<!-- b000026 | prose | pages [2] -->
line tones based on maximum and minimum spanning tree technique, the effects of

<!-- b000027 | prose | pages [2] -->
simultaneous users need to be accommodated, the fluctuation of user density in reality,

<!-- b000028 | prose | pages [2] -->
how the landscape can affect the design of repeaters’ locations, and the strengths and

<!-- b000029 | prose | pages [2] -->
weaknesses of the model and algorithms.

<!-- b000030 | furniture | pages [2] -->


<!-- b000031 | furniture | pages [2] -->


<!-- b000032 | furniture | pages [3] -->
Team #9440              Page  2 / 40

<!-- b000033 | heading | pages [3] -->
1  Introduction

<!-- b000034 | prose | pages [3] -->
The design of amplify-and-forward relay networks has attracted increasing attention recently [1-3]. The relay networks are very helpful for long-distance communication since the relay nodes can amplify the weak signals and forward them to other relay nodes or send them directly to the destinations. Through several relay nodes, low-power users can communicate with one another in situation where direct user-to-user communication would not be possible. The relay networks have already found wide applications in cooperative communication [4]. For example, in amateur radio activities hams can communicate with distant hams through one or more relay nodes (also called radio repeaters) [5], and in wireless sensor networks relay nodes are used to help information dissemination between distant sensors [6].

<!-- b000035 | prose | pages [3] -->
In many amplify-and-forward cooperative communication networks, the nodes are homogeneous, namely a node can simultaneously play the roles as source node, sink node and relay node. A typical example is the mobile communication, where a cell phone can also be an amplify-and-forward relay node [4]. In another scenario, the relay nodes usually do not initiate communications but only help communications between other nodes. For example, in amateur radio activities, radio repeaters can be considered as relay nodes, and hams usually carry their own radios (transceivers). Repeaters can pick up weak signals from radios, amplify and retransmit them. Different from the homogeneous scenario, the functionalities of repeaters and radios are different, and the specifications of repeaters and radios are also different. For example, in Utah, the power of a radio is usually a few watts, while most repeaters are of power no less than a hundred watts.

<!-- b000036 | prose | pages [3] -->
Pan et al. [7] proposed a two-tiered relay network model, where the base stations are considered as low power users and some inter-application nodes are playing the role of relay nodes. However, they did not address the issue of covering users by relay nodes. Gupta and Younis considered the fault-tolerant [8] and traffic load balance [9] problems in a two-tiered relay network model, yet they did not address the placement problem of relay nodes. Tang et al. [10] proposed two algorithms for the relay nodes placement problem, aiming at placing the fewest number of relay nodes in the considered area such that each user can communicate with at least one relay node and the network of relay nodes is connected.

<!-- b000037 | prose | pages [3] -->
The above-mentioned works are different from ours because in a more general scenario that includes the amateur radio communication, the capacity of a repeater and the interference among nearby repeaters should be taken into account. In this paper, we propose a more general two-tiered network model, where each repeater can simultaneously manage at most C users and two nearby repeaters will interfere with each other if their transmitter frequencies are close and they share the same private line tone. Our objective is to place the least number of repeaters that can satisfy the users’ communication requirement. We respectively consider two different requirements: the weak requirement is that every user must be covered by at least one repeater and the strong requirement is that every user can communicate with another user in any position of the considered area. Our analysis indicates that the former requirement is equivalent to a circle covering problem while the solution on the latter requirement is based on the answer to the former requirement.

<!-- b000038 | prose | pages [3] -->
The geometric covering problem is known to be NP hard [11], and the algorithm is usually very time-consuming even for a small number of circles. For example, Nurmela and Ostergard [12] proposed a simulated annealing algorithm to obtain near-optimal solutions for the unit square

<!-- b000039 | furniture | pages [3] -->


<!-- b000040 | furniture | pages [4] -->
Team #9440              Page  3 / 40

<!-- b000041 | prose | pages [4] -->
covering problem with up to 30 equal circles. Their result are known to be one of the most accurate results yet the algorithm has to run more than 2 weeks to obtain the solution for 27 circles. In contrast, considering the limited capacity of a repeater, when the number of users being accommodated increases, we have to place remarkably more repeaters than being considered in the previous works.

<!-- b000042 | prose | pages [4] -->
Motivated by the structure of cellular networks (i.e., networks with beehive-like structure), we give a naïve solution where the number of repeaters as well as their positions can be obtained analytically. In numerical simulation, this naïve solution performs unexpectedly well. In a circular area with radius 40 miles, 12 repeaters are enough to accommodate 1000 simultaneous users and for 10000 users, 108 repeaters are sufficient. In comparison, in the former case, 11 repeaters are the optimum and in the later case. We further propose an iterative refinement algorithm consisting of three fundamental modules: to draw the Voronoi diagram [13], to determine the circumscribed circles [14] of Voronoi areas and move the repeaters to the centers of these circumscribed circles, and to escape the local optimum by using the idea of extremal optimization [15,16]. This method outperforms the naïve solution. For the case of 1000 users, it obtains a solution with 11 repeaters, which can be proved to be the real optimum. For the case of 10000 users, it obtains a solution with 104 repeaters, better than the naïve solution.

<!-- b000043 | prose | pages [4] -->
Taking into account the capacity limitation and interferences, we proposed a more general model than most of previous models. Two methods are designed to place the repeaters in a typical area. They both perform very well. This work provides a general model and a novel algorithm to an extensively studied problem: how to place relay nodes in a cooperative communication system. This work can find applications in not only the amateur radio activities, but also the design of sensor wireless networks and mobile wireless networks.

<!-- b000044 | prose | pages [4] -->
This paper is organized as follows. In Section 2, we clarify the considered problem, and in Section 3, we descript the proposed two-tiered amplify-and-forward network model, as well as the definitions of solution and strong solution. Section 4 presents the calculation of the communication range of repeaters and users, the capacity of a repeater. In this section, we apply the continuous approximation and show how to map this problem to a “circles covering circle” problem. The naïve solution is also given in Section 4. We present the algorithms respectively to determine the requirement number of repeaters as well as their positions and to assign frequencies and private line tones to repeaters in Section 5. In Section 6, we give the solutions obtained by our algorithm, compare them with the naïve solution, and prove that the solution for the small population case is the optimal one. In Section 7, we discuss the effects of simultaneous users need to be accommodated, the fluctuation of user density in reality, and how the landscape can affect the design of repeaters’ locations, and finally, in Section 8, we summarize the paper and discuss the strengths and weaknesses of the model and algorithms.

<!-- b000045 | prose | pages [4] -->
Parameters, mathematical symbols and assumptions appear everywhere in this paper. Therefore, for convenience, in Appendix A, we list all the parameters, in Appendix B, we list the mathematical symbols, and in Appendix C, we summarize the important assumptions made in this paper.

<!-- b000046 | furniture | pages [4] -->


<!-- b000047 | furniture | pages [4] -->


<!-- b000048 | furniture | pages [4] -->


<!-- b000049 | furniture | pages [4] -->


<!-- b000050 | furniture | pages [4] -->


<!-- b000051 | furniture | pages [5] -->
Team #9440              Page  4 / 40

<!-- b000052 | heading | pages [5] -->
2 Problem Description

<!-- b000053 | prose | pages [5] -->
Given a circular flat area of radius  (this circular area is denoted by ), we are asked to determine the least number of radio repeaters necessary to accommodate a given number of users N. A repeater is a combination of a radio receiver and a radio transmitter that picks up weak signals, amplify them, and retransmit them on a different frequency. In this problem, the three most fundamental parameters characterizing a repeater are the receiver frequency fr, the transmitter frequency ft and the private line (PL) tone nPL. A repeater responds only to signals on its receiver frequency and containing the same PL tone. If so, the signals will be amplified and transmitted on the repeater’s transmitter frequency and the PL tone will not be changed. In this problem, both fr, and ft belong to the range [145MHz, 148MHz], |fr - ft |=0.6MHz, and there are in total NPL=54 different PL tones available.

<!-- b000054 | prose | pages [5] -->
For example, a repeater located in Mong Kok, Hong Kong has the receiver frequency 145.025MHz, the transmitter frequency 145.625MHz, and the PL tone 110.9Hz. That is to say, only the signals on 145.025MHz and with PL tone 110.9Hz can be amplified by this repeater, and after amplification, the signals will be transmitted with frequency 145.625MHz and PL tone 110.9Hz.

<!-- b000055 | prose | pages [5] -->
Notice that, two repeaters will interfere with each other if they satisfy all the following three conditions: (i) they carry exactly the same PL tone; (ii) their distance is smaller than the twofold of the communication radius R of the repeater (for simplicity, we assume every repeater has the same communication radius R); (iii) the difference between their transmitter frequencies is smaller than a threshold fc. It is necessary to guarantee that no interference will happen between any pair of repeaters.

<!-- b000056 | prose | pages [5] -->
Each user can directly contact other nearby users and reach distant users through one or several repeaters. The maximal communication distance from a user to a repeater, r, is supposed to be identical for every user, which is remarkably smaller than the communication radius of a repeater (i.e., r<R). Every user should be covered by at least one repeater, namely at least one repeater locates inside the circle with radius r and centered at the user’s location. Under a stronger requirement, each user is able to send information to users at any positions in the considered area through one or several repeaters.

<!-- b000057 | prose | pages [5] -->
Since the communication ranges, R and r, are finite, and the capacity of a repeater, C, is very limited (i.e., a repeater can manage at most C different users simultaneously), usually a number of repeaters are required to accommodate users in a given area. The primary problem is to determine the minimum number of repeaters that can satisfy the communication requirement of a given number of users. Of course, a complete solution should also contain the positions, receiver and transmitter frequencies, as well as the PL tones of repeaters. The effects of the number of users and the landscape are emphasized in this problem. More detailed description of the meanings and effects of the parameters, and the in-depth analysis on the problem constrains are presented in the following sections.

<!-- b000058 | furniture | pages [5] -->


<!-- b000059 | furniture | pages [5] -->


<!-- b000060 | furniture | pages [5] -->


<!-- b000061 | furniture | pages [5] -->


<!-- b000062 | furniture | pages [5] -->


<!-- b000063 | furniture | pages [5] -->


<!-- b000064 | furniture | pages [6] -->
Team #9440              Page  5 / 40

<!-- b000065 | heading | pages [6] -->
3 Model

<!-- b000066 | prose | pages [6] -->
To present the system, we use a two-tiered directed network D(Vu, Vr, Eur, Err), where

<!-- b000067 | prose | pages [6] -->
  V { , u u ,..., u } V { , r r ,..., r } denote the sets of users and repeaters, and Eur and and u 1 2 N r 1 2 M

<!-- b000068 | prose | pages [6] -->
Err are the sets of directed links from users to repeaters and between repeaters. Each user ui is

<!-- b000069 | prose | pages [6] -->
identified by her/his location ( ( ), ( )) x u y u in a 2-dimensional plane, and each repeater rj is i i

<!-- b000070 | prose | pages [6] -->
identified by its location, receiver frequency, transmitter frequency and PL tone as

<!-- b000071 | prose | pages [6] -->
( ( ), ( ), x r y r f r ( ), f r ( ), n ( )) r . As mentioned above, the frequencies of an arbitrary j j r j t j PL j

<!-- b000072 | prose | pages [6] -->
repeater rj should obey the constrains f r  f r ( ), ( ) [145MHz,148MHz] and r j t j

<!-- b000073 | prose | pages [6] -->
. Since the considered area is a circular area of radius , the   f r ( ) f r ( ) 0.6MHz r j t j

<!-- b000074 | prose | pages [6] -->
location for arbitrary user or repeater should satisfy the inequality

<!-- b000075 | prose | pages [6] -->
 2 x

<!-- b000076 | furniture | pages [6] -->


<!-- b000077 | prose | pages [6] -->


<!-- b000078 | prose | pages [6] -->
                           (1) 2 2 2 y y

<!-- b000079 | prose | pages [6] -->
 is given a priori. A directed link from ui to rj exists (i.e., ( , 40 where u r ) E ) if the i j ur

<!-- b000080 | prose | pages [6] -->
distance between ui and rj is no more than a user’s communication range r. A directed link from rj

<!-- b000081 | prose | pages [6] -->
 to rk exists (i.e., ( , r r ) E ) if the distance between rj and rk is no more than a repeater’s j k rr

<!-- b000082 | prose | pages [6] -->
communication range R, the transmitter frequency of rj equals the receiver frequency of rk (i.e.,

<!-- b000083 | prose | pages [6] -->
 f r ( ) f r ( )  n ( ) r n ( ) r ) and they share the same PL tone (i.e., t j r k ). Clearly, the sets of PL j PL k

<!-- b000084 | prose | pages [6] -->
directed links are determined when the information about users and repeaters is known.

<!-- b000085 | prose | pages [6] -->
A network D is called a solution (in section 4, we will discuss a more practical definition of solution that does not depend on a specific distribution of users’ locations) if the following three

<!-- b000086 | prose | pages [6] -->
) are all satisfied.

<!-- b000087 | prose | pages [6] -->
, , conditions ( 1 2 3

<!-- b000088 | prose | pages [6] -->
-Capacity constrain. For simplicity, we assume users are uniformly distributed in the 1

<!-- b000089 | prose | pages [6] -->
considered area  and each of them prefers to communicate with the nearest repeater. Each repeater can manage at most C users at the same time (the capacities of different repeaters are supposed to be the same, and the estimation of C will be given in the next section). For a repeater rj, there exists a connected area SV(rj) inside  such that for every point inside this area, rj is the nearest repeater and for every point outside this area, rj is definitely not the nearest repeater. This area is called the Voronoi area [13] of rj. For every repeater, the number of users inside its Voronoi area must be no more than its capacity C.

<!-- b000090 | prose | pages [6] -->
-Interference avoidance. If two repeaters share the same PL tone and are with distance 2

<!-- b000091 | prose | pages [6] -->
less than 2R, the difference between their transmitter frequencies must be no less than a given threshold fc. In the spectrum 145-148MHz, the standard threshold is fc=0.6MHz.

<!-- b000092 | furniture | pages [6] -->


<!-- b000093 | furniture | pages [7] -->
Team #9440              Page  6 / 40

<!-- b000094 | prose | pages [7] -->
 -Connectivity. Every user is covered by at least one repeater. That is to say, 3

<!-- b000095 | prose | pages [7] -->
 such that ( , u r ) E . i j ur

<!-- b000096 | furniture | pages [7] -->


<!-- b000097 | prose | pages [7] -->
 iu jr , ,

<!-- b000098 | furniture | pages [7] -->


<!-- b000099 | caption | pages [7] -->
Figure 1. An illustration about the reachable repeaters of u1. The circle centered at u1 is the

<!-- b000100 | prose | pages [7] -->
communication of u1 with radius r.

<!-- b000101 | furniture | pages [7] -->


<!-- b000102 | prose | pages [7] -->
Our goal is to find out the solution with the minimum number of repeaters M. In a solution, although every user is covered by at least one repeater, her/his signals may not reach the desired position in  since the coverage of a repeater is also limited and the solution does not guarantee the existence of a multi-hop path through several repeaters to reach the desired position. Ignoring the small area that can be directly reached by a user without the help of any repeater, the reachable area of a user ui, denoted by Sr(ui), is defined as the area in  that can be covered by at least one reachable repeater of ui (each repeater covers a circle with radius R). The set of reachable repeaters for ui, denoted by Rr(ui), consists of two parts: One is the repeaters that can be directly reached by ui (i.e., the repeaters located within the circle with radius r and centered at ui) and another is the repeaters that can be further reached through directed paths consisted of directed links in Err and started from the directly reachable repeaters. Figure 1 illustrates a simple example where r2 can be directly reached by u1, and r4 and r5 can be further reached starting from r2. Two nearby repeaters, like r2 and r3, may not have a link in between since they may not match with each other in frequency or PL tone. The reachable repeaters of u1 are r2, r4 and r5, and thus the reachable area of u1 is the union of the coverage areas of r2, r4 and r5. The following condition must be satisfied to guarantee every user can in principle reach any position of the considered area through multi-hop repeaters.

<!-- b000103 | prose | pages [7] -->
-Global Reachability. The reachable area of every user is equal to the considered area 4

<!-- b000104 | prose | pages [7] -->
.

<!-- b000105 | prose | pages [7] -->
) are all , , A network D is called a strong solution if the following three conditions ( 1 2 4

<!-- b000106 | prose | pages [7] -->
satisfied. Under these definitions, two propositions obviously hold, that is

<!-- b000107 | furniture | pages [7] -->


<!-- b000108 | furniture | pages [8] -->
Team #9440              Page  7 / 40

<!-- b000109 | prose | pages [8] -->
Proposition 1: A strong solution is a solution.

<!-- b000110 | prose | pages [8] -->
R , any solution is a strong solution.

<!-- b000111 | prose | pages [8] -->
2 Proposition 2: When To find a strong solution is much more difficult than to find a solution, and these two tasks

<!-- b000112 | prose | pages [8] -->
R . We will respectively study the cases of R  2 2 are equivalent to each other only if R , emphasizing on the strong solutions.

<!-- b000113 | prose | pages [8] -->
2 and

<!-- b000114 | furniture | pages [8] -->


<!-- b000115 | furniture | pages [8] -->


<!-- b000116 | furniture | pages [8] -->


<!-- b000117 | furniture | pages [8] -->


<!-- b000118 | furniture | pages [8] -->


<!-- b000119 | furniture | pages [8] -->


<!-- b000120 | furniture | pages [8] -->


<!-- b000121 | furniture | pages [8] -->


<!-- b000122 | furniture | pages [8] -->


<!-- b000123 | furniture | pages [8] -->


<!-- b000124 | furniture | pages [8] -->


<!-- b000125 | furniture | pages [8] -->


<!-- b000126 | furniture | pages [8] -->


<!-- b000127 | furniture | pages [8] -->


<!-- b000128 | furniture | pages [8] -->


<!-- b000129 | furniture | pages [8] -->


<!-- b000130 | furniture | pages [8] -->


<!-- b000131 | furniture | pages [8] -->


<!-- b000132 | furniture | pages [8] -->


<!-- b000133 | furniture | pages [8] -->


<!-- b000134 | furniture | pages [8] -->


<!-- b000135 | furniture | pages [8] -->


<!-- b000136 | furniture | pages [8] -->


<!-- b000137 | furniture | pages [8] -->


<!-- b000138 | furniture | pages [8] -->


<!-- b000139 | furniture | pages [8] -->


<!-- b000140 | furniture | pages [8] -->


<!-- b000141 | furniture | pages [8] -->


<!-- b000142 | furniture | pages [8] -->


<!-- b000143 | furniture | pages [8] -->


<!-- b000144 | furniture | pages [8] -->


<!-- b000145 | furniture | pages [8] -->


<!-- b000146 | furniture | pages [8] -->


<!-- b000147 | furniture | pages [8] -->


<!-- b000148 | furniture | pages [8] -->


<!-- b000149 | furniture | pages [8] -->


<!-- b000150 | furniture | pages [8] -->


<!-- b000151 | furniture | pages [8] -->


<!-- b000152 | furniture | pages [8] -->


<!-- b000153 | furniture | pages [8] -->


<!-- b000154 | furniture | pages [9] -->
Team #9440              Page  8 / 40

<!-- b000155 | heading | pages [9] -->
4 Analysis

<!-- b000156 | prose | pages [9] -->
In this section, we will give some elementary analysis about the model. Firstly, in subsection 4.1 and 4.2, we will calculate the communication ranges for repeaters and users, as well as the repeater’s capacity according to the Shannon’s theory. Taking into consideration of the mobility of users, in subsection 4.3, we will show that the continuous approximation of the distribution of users’ locations is necessary to address the problem. In subsection 4.4, we will present a naïve solution where repeaters are arranged in a cellular network (i.e., a beehive-like structure). In spite of the simplicity, the naïve solution performs unexpectedly well, which will play a role of benchmark solution in evaluating the algorithmic output.

<!-- b000157 | furniture | pages [9] -->


<!-- b000158 | heading | pages [9] -->
4.1 Communication Radius

<!-- b000159 | prose | pages [9] -->
We apply a simple model to determine the effective radiated distance (i.e., communication range) of repeaters and users. According to the problem description, we assume that this circular area is a place where wireless signals can fade freely. That is to say, there are not any other sorts of interference such as fogs, rivers, hills, buildings, activities of sun and so forth. Therefore the fading of signals under such situation is only due to the distance across which the signal is transmitted.

<!-- b000160 | prose | pages [9] -->
P be the power of the signal transmitted by a repeater. Since the signal can fade

<!-- b000161 | furniture | pages [9] -->


<!-- b000162 | prose | pages [9] -->
Let ,r out

<!-- b000163 | prose | pages [9] -->
freely, its average power P within one unit area at a distance d from the repeater is

<!-- b000164 | prose | pages [9] -->
 P

<!-- b000165 | furniture | pages [9] -->


<!-- b000166 | prose | pages [9] -->
P P r out

<!-- b000167 | prose | pages [9] -->
,

<!-- b000168 | prose | pages [9] -->
(2) 

<!-- b000169 | prose | pages [9] -->
2 4 4

<!-- b000170 | prose | pages [9] -->
d

<!-- b000171 | prose | pages [9] -->
2 4  , where According to the antenna theory [17], the effective receiving area of an antenna is

<!-- b000172 | prose | pages [9] -->
 is the wave length of the signal. So the receiving power of the signal is

<!-- b000173 | prose | pages [9] -->
P

<!-- b000174 | prose | pages [9] -->


<!-- b000175 | prose | pages [9] -->
'

<!-- b000176 | prose | pages [9] -->
P

<!-- b000177 | furniture | pages [9] -->


<!-- b000178 | prose | pages [9] -->
4

<!-- b000179 | prose | pages [9] -->


<!-- b000180 | prose | pages [9] -->
2

<!-- b000181 | prose | pages [9] -->


<!-- b000182 | prose | pages [9] -->
r out

<!-- b000183 | prose | pages [9] -->
, ,

<!-- b000184 | prose | pages [9] -->
(3)   

<!-- b000185 | prose | pages [9] -->
2

<!-- b000186 | prose | pages [9] -->
d d

<!-- b000187 | prose | pages [9] -->
4

<!-- b000188 | prose | pages [9] -->
Substituting  with c f , where c is the velocity of light and f is the frequency of the

<!-- b000189 | prose | pages [9] -->
signal, one obtains

<!-- b000190 | prose | pages [9] -->


<!-- b000191 | prose | pages [9] -->
'

<!-- b000192 | prose | pages [9] -->
P P

<!-- b000193 | furniture | pages [9] -->


<!-- b000194 | prose | pages [9] -->
c

<!-- b000195 | prose | pages [9] -->
2 ( )

<!-- b000196 | prose | pages [9] -->
(4)

<!-- b000197 | prose | pages [9] -->
r out , ,

<!-- b000198 | prose | pages [9] -->


<!-- b000199 | prose | pages [9] -->
4

<!-- b000200 | prose | pages [9] -->
df

<!-- b000201 | prose | pages [9] -->
sL is In terms of the communication theory (Shannon’s thoery), the loss

<!-- b000202 | prose | pages [9] -->
P  

<!-- b000203 | prose | pages [9] -->
r out

<!-- b000204 | prose | pages [9] -->
,

<!-- b000205 | prose | pages [9] -->
L

<!-- b000206 | prose | pages [9] -->
10lg( )

<!-- b000207 | furniture | pages [9] -->


<!-- b000208 | prose | pages [9] -->
s '

<!-- b000209 | prose | pages [9] -->
P  

<!-- b000210 | prose | pages [9] -->
92.4 20lg

<!-- b000211 | prose | pages [9] -->
d

<!-- b000212 | prose | pages [9] -->
20lg

<!-- b000213 | prose | pages [9] -->
f (5)

<!-- b000214 | prose | pages [9] -->
sL is measured by dB, d is measured by km, f is in GHz. The actual power of where

<!-- b000215 | prose | pages [9] -->
P received signal is ,r in

<!-- b000216 | furniture | pages [9] -->


<!-- b000217 | furniture | pages [10] -->
Team #9440              Page  9 / 40

<!-- b000218 | prose | pages [10] -->
    P P ( G G ) (

<!-- b000219 | furniture | pages [10] -->


<!-- b000220 | prose | pages [10] -->
r in , r out , out in     L L L ) ( L L ) L (6) f out , f in , b out , b in , s

<!-- b000221 | prose | pages [10] -->
 L L From one repeater (transmitter) to another repeater (receiver), the equations hold as

<!-- b000222 | prose | pages [10] -->
 L L

<!-- b000223 | furniture | pages [10] -->


<!-- b000224 | prose | pages [10] -->
f out , f in ,

<!-- b000225 | prose | pages [10] -->
 G G (other loss of the system), (the loss of feed system), b out , b in ,

<!-- b000226 | prose | pages [10] -->
  L L 2 dB L antenna). Normally, , f out , f in , b out

<!-- b000227 | prose | pages [10] -->
(the gain of out in

<!-- b000228 | prose | pages [10] -->
    G G 39 dB L 1 dB , . For this out in , , b in ,

<!-- b000229 | prose | pages [10] -->
problem, the frequency of signals is about 0.1465GHz (i.e., the middle point of the available spectrum 145MHz~148MHz), and thus

<!-- b000230 | prose | pages [10] -->
10lg

<!-- b000231 | prose | pages [10] -->


<!-- b000232 | prose | pages [10] -->
d

<!-- b000233 | prose | pages [10] -->
10

<!-- b000234 | furniture | pages [10] -->


<!-- b000235 | prose | pages [10] -->
P P

<!-- b000236 | prose | pages [10] -->
r out

<!-- b000237 | prose | pages [10] -->
,

<!-- b000238 | prose | pages [10] -->


<!-- b000239 | prose | pages [10] -->
37.2328

<!-- b000240 | prose | pages [10] -->
P

<!-- b000241 | prose | pages [10] -->
r in

<!-- b000242 | prose | pages [10] -->
,

<!-- b000243 | prose | pages [10] -->
20

<!-- b000244 | prose | pages [10] -->
(7)

<!-- b000245 | furniture | pages [10] -->


<!-- b000246 | furniture | pages [10] -->


<!-- b000247 | caption | pages [10] -->
Table 1: Effective radiated powers of repeaters in Utah (http://www.ussc.com/~uvhfs/rptr.html)

<!-- b000248 | prose | pages [10] -->
Call No. Call No.

<!-- b000249 | prose | pages [10] -->
ERP Call No.

<!-- b000250 | prose | pages [10] -->
ERP ERP Call No.

<!-- b000251 | prose | pages [10] -->
ERP Call No.

<!-- b000252 | prose | pages [10] -->
ERP

<!-- b000253 | prose | pages [10] -->
KD7NX K7UCS 120 W WA7UAH 30 W

<!-- b000254 | prose | pages [10] -->
KF6RAL 100 W KD7HUS 25 W K7JH

<!-- b000255 | prose | pages [10] -->
58 W K7JL 100 W K7JL 500 W

<!-- b000256 | prose | pages [10] -->
100 W K7MLA 100 W K7SDC 100 W

<!-- b000257 | prose | pages [10] -->
K7QEQ W7IHC 100 W WV7H 40 W

<!-- b000258 | prose | pages [10] -->
AA7JR 100 W N7BSA 80 W W7SP

<!-- b000259 | prose | pages [10] -->
100 W W7WAC 50 W K7MLA 100 W

<!-- b000260 | prose | pages [10] -->
100 W N7KM 40 W N7NKK 50 W

<!-- b000261 | prose | pages [10] -->
WV7H NZ6Z 100 W W7BAR 100 W 100 W W7EO 40 W K7MLA 100 W

<!-- b000262 | prose | pages [10] -->
AE7TA KE7FO 20 W K7HEN 100 W 120 W KC7SNN 100 W K7JL 100 W

<!-- b000263 | prose | pages [10] -->
N6EZO KR7D 100 W W7DRC 48 W 100 W K7OGM 100 W AC7O 10 W

<!-- b000264 | prose | pages [10] -->
W7SU K7JL 50 W K7SDC 100 W

<!-- b000265 | prose | pages [10] -->
N7WFM 100 W W7SP 100 W NR7K

<!-- b000266 | prose | pages [10] -->
100 W K7MLA 75 W N7ZOI 100 W

<!-- b000267 | prose | pages [10] -->
100 W K7DAV 50 W W7EO 100 W

<!-- b000268 | prose | pages [10] -->
N7PCE WB7REL 160 W WA7MXZ 100 W

<!-- b000269 | prose | pages [10] -->
K7SDC 100 W W7JVN 100 W K7JL

<!-- b000270 | prose | pages [10] -->
100 W W7BAR 183 W AB7TS 100 W

<!-- b000271 | prose | pages [10] -->
100 W K7SDC 100 W KJ7VO 100 W

<!-- b000272 | prose | pages [10] -->
KD7YE WA7KMF 100 W W7DRC 60 W 97 W N7DZP 40 W WA7YZR 100 W

<!-- b000273 | prose | pages [10] -->
W7NRC N7BYU 100 W W7DHH 100 W

<!-- b000274 | prose | pages [10] -->
K7ACA 100 W N7JSQ 100 W KD0J

<!-- b000275 | prose | pages [10] -->
100 W KB7ZCL 200 W K7HEN 100 W

<!-- b000276 | prose | pages [10] -->
100 W K7CEM 40 W N7PQD 147 W

<!-- b000277 | prose | pages [10] -->
K7QEQ W7EO 160 W KD0J 100 W 100 W K7SDC 100 W N7WPF 125 W

<!-- b000278 | prose | pages [10] -->
W7SU KA7LEG 200 W KA7STK 25 W

<!-- b000279 | prose | pages [10] -->
AC7O 100 W W7NRC 100 W NR7K

<!-- b000280 | prose | pages [10] -->
100 W WX7Y 100 W AC7O 200 W

<!-- b000281 | prose | pages [10] -->
20 W K7SDC 60 W K7SG 25 W

<!-- b000282 | prose | pages [10] -->
N7TOP WB7TSQ 100 W AC7O 100 W 175 W N7GGN 20 W K7UCS 120 W

<!-- b000283 | prose | pages [10] -->
W7BYU W7DES 25 W WB7CBS 100 W 50 W W7BAR 100 W W7CWK 100 W

<!-- b000284 | prose | pages [10] -->
WA7GIE W7EO 100 W K7UCS 120 W

<!-- b000285 | prose | pages [10] -->
K7SDC 100 W KK7EX 50 W WI7M

<!-- b000286 | prose | pages [10] -->
100 W KB7WQD 48 W WB7TSQ 100 W

<!-- b000287 | prose | pages [10] -->
67 W WA7GIE 100 W WA7GIE 100 W

<!-- b000288 | prose | pages [10] -->
WR7AAA 100 W KK7DO 800 W NR7K 100 W

<!-- b000289 | furniture | pages [10] -->


<!-- b000290 | prose | pages [10] -->
AG7BL 100 W W7NRC 100 W

<!-- b000291 | furniture | pages [10] -->


<!-- b000292 | furniture | pages [10] -->


<!-- b000293 | prose | pages [10] -->
In the light of the statistics about the 2-meter repeaters in Utah, USA (see Table 1), the

<!-- b000294 | prose | pages [10] -->
 P 100 W effective radiated power of most of the repeaters is

<!-- b000295 | furniture | pages [10] -->


<!-- b000296 | prose | pages [10] -->
, and normally a repeater can r out ,

<!-- b000297 | furniture | pages [11] -->
Team #9440              Page  10 / 40

<!-- b000298 | prose | pages [11] -->
 receive the signal with power no less than 1 W

<!-- b000299 | prose | pages [11] -->
R  communication radius of a repeater is

<!-- b000300 | prose | pages [11] -->
  P 1 W (i.e., ). According to Eq. (7), the r in ,

<!-- b000301 | prose | pages [11] -->
85.45 miles (the original result is measured by kilometers, and we have already changed it to miles). Analogously, the average working power for

<!-- b000302 | prose | pages [11] -->
a user (according to several wireless devices) is

<!-- b000303 | prose | pages [11] -->
r  15.28

<!-- b000304 | prose | pages [11] -->
   P 3.2 W and P 1 W , resulting in the u out , u in ,

<!-- b000305 | prose | pages [11] -->
R  2 miles. Although our calculation indicates that user’s communication radius

<!-- b000306 | prose | pages [11] -->
) is equivalent to the connectivity ( and the global reachability ( 4

<!-- b000307 | prose | pages [11] -->
R .

<!-- b000308 | prose | pages [11] -->
2 paper the more complicated case when

<!-- b000309 | furniture | pages [11] -->


<!-- b000310 | heading | pages [11] -->
4.2 Repeater’s Capacity

<!-- b000311 | prose | pages [11] -->
), we will discuss in this 3

<!-- b000312 | prose | pages [11] -->
In this subsection, we will calculate the maximal number of users that can be simultaneously accommodated in a repeater, namely the capacity C.

<!-- b000313 | prose | pages [11] -->
Ignoring the background noise and the interference, namely we assume that signals from one repeater will not affect others. Considering the transmitter frequency in a repeater is an exact value rather than in a broad band, we come up with a method to calculate the capacity through the gain. A mainstream method to estimate the capacity of information over a noisy channel is the famous Shannon theory, as:

<!-- b000314 | prose | pages [11] -->
  log (1 B

<!-- b000315 | furniture | pages [11] -->


<!-- b000316 | prose | pages [11] -->
SNR ) (8) 2 2

<!-- b000317 | prose | pages [11] -->
where  is the information bit rate, measured by watt (dB), SNR is the signal-to-noise ratio,

<!-- b000318 | prose | pages [11] -->
which is dimensionless, and B is the total bandwidth, measured by Hz.

<!-- b000319 | prose | pages [11] -->
Inspired by Shannon Theory, Gilhousen et al. [18] put forward a method to estimate the capacity of a cellular CDMA System. Of greater importance for reliable system operation is the bit energy-to-noise density ratio, whose numerator is obtained by dividing the desired signal power by the information bit rate , and dividing the noise by the total bandwidth W, which results in

<!-- b000320 | prose | pages [11] -->
the equation

<!-- b000321 | prose | pages [11] -->
E P 

<!-- b000322 | prose | pages [11] -->
b

<!-- b000323 | furniture | pages [11] -->


<!-- b000324 | prose | pages [11] -->
 N

<!-- b000325 | prose | pages [11] -->
(

<!-- b000326 | prose | pages [11] -->
C

<!-- b000327 | prose | pages [11] -->
0

<!-- b000328 | prose | pages [11] -->
 B P 

<!-- b000329 | prose | pages [11] -->
ur ur ur

<!-- b000330 | prose | pages [11] -->
(9)

<!-- b000331 | prose | pages [11] -->


<!-- b000332 | prose | pages [11] -->
1) 1)

<!-- b000333 | prose | pages [11] -->
P

<!-- b000334 | prose | pages [11] -->
/

<!-- b000335 | prose | pages [11] -->
B C

<!-- b000336 | prose | pages [11] -->
1

<!-- b000337 | prose | pages [11] -->
ur

<!-- b000338 | prose | pages [11] -->
where Pur is the power of signal come from a single user and received by a repeater, measured by bps; C is the maximum number of users that can be simultaneously managed by a repeater,

<!-- b000339 | prose | pages [11] -->
N level is assumed which ensures operation at the level of bit error performance required E b 0

<!-- b000340 | prose | pages [11] -->
E N is a for digital voice transmission, which is always set ranging from 5 to 30 dB.

<!-- b000341 | prose | pages [11] -->
b 0

<!-- b000342 | prose | pages [11] -->
standard for digital voice transmission, and can take different values according to different circumstances.

<!-- b000343 | prose | pages [11] -->
Different from the CDMA System, the transmitter frequency in a repeater is an exact value rather than in a broad band. We prefer to take the following equation

<!-- b000344 | prose | pages [11] -->
E 

<!-- b000345 | prose | pages [11] -->
b

<!-- b000346 | furniture | pages [11] -->


<!-- b000347 | prose | pages [11] -->
N V C

<!-- b000348 | prose | pages [11] -->
( 0

<!-- b000349 | furniture | pages [11] -->


<!-- b000350 | prose | pages [11] -->
G

<!-- b000351 | prose | pages [11] -->
out

<!-- b000352 | prose | pages [11] -->
(10)

<!-- b000353 | prose | pages [11] -->
  

<!-- b000354 | prose | pages [11] -->
1)(1

<!-- b000355 | prose | pages [11] -->
I I

<!-- b000356 | prose | pages [11] -->
)

<!-- b000357 | prose | pages [11] -->
other self

<!-- b000358 | furniture | pages [12] -->
Team #9440              Page  11 / 40

<!-- b000359 | prose | pages [12] -->
I where G is the gain of antenna, V is the gain of voice,

<!-- b000360 | prose | pages [12] -->
I repeaters, and is the interference of itself. self

<!-- b000361 | prose | pages [12] -->
is the interference come from other other

<!-- b000362 | prose | pages [12] -->
In the situation that a repeater can accommodate C users simultaneously, SNR can be regarded as the ratio of the effective information in the total received signal, say

<!-- b000363 | prose | pages [12] -->
 SNR

<!-- b000364 | furniture | pages [12] -->


<!-- b000365 | prose | pages [12] -->
(

<!-- b000366 | prose | pages [12] -->
C

<!-- b000367 | prose | pages [12] -->
  G 39 dB 7966.40 W Normally, and out

<!-- b000368 | prose | pages [12] -->
P P

<!-- b000369 | prose | pages [12] -->
1

<!-- b000370 | prose | pages [12] -->


<!-- b000371 | prose | pages [12] -->
ur

<!-- b000372 | prose | pages [12] -->
(11)

<!-- b000373 | prose | pages [12] -->
  

<!-- b000374 | prose | pages [12] -->
1)

<!-- b000375 | prose | pages [12] -->
P C

<!-- b000376 | prose | pages [12] -->
1

<!-- b000377 | prose | pages [12] -->
ur

<!-- b000378 | prose | pages [12] -->
  V 0.4 dB 1.07 W (in the calculation, the

<!-- b000379 | prose | pages [12] -->
 I I 0 unit must be watt). We ignore the interference come from other repeaters, namely

<!-- b000380 | prose | pages [12] -->
  E N 18 dB 63.01 W

<!-- b000381 | prose | pages [12] -->
. other self

<!-- b000382 | prose | pages [12] -->
(the bit energy-to-noise density ratio is always ranging from Setting b 0

<!-- b000383 | prose | pages [12] -->
5 to 30dB, and for transceiver we set it as the middle point 18dB), we can get the capacity of a single repeater through:

<!-- b000384 | prose | pages [12] -->
G  C

<!-- b000385 | prose | pages [12] -->
1

<!-- b000386 | furniture | pages [12] -->


<!-- b000387 | prose | pages [12] -->
 V

<!-- b000388 | prose | pages [12] -->
(1

<!-- b000389 | prose | pages [12] -->
I

<!-- b000390 | prose | pages [12] -->
other

<!-- b000391 | furniture | pages [12] -->


<!-- b000392 | heading | pages [12] -->
4.3 Continuous Approximation

<!-- b000393 | prose | pages [12] -->


<!-- b000394 | prose | pages [12] -->
out out

<!-- b000395 | prose | pages [12] -->
119

<!-- b000396 | prose | pages [12] -->
(12)

<!-- b000397 | prose | pages [12] -->
I I

<!-- b000398 | prose | pages [12] -->
)

<!-- b000399 | prose | pages [12] -->
E N

<!-- b000400 | prose | pages [12] -->
self b

<!-- b000401 | prose | pages [12] -->
0

<!-- b000402 | prose | pages [12] -->
Taking into account the mobility of users, the repeaters have to cover all the considered area

<!-- b000403 | heading | pages [12] -->
. Given distributed users Vu, a solution

<!-- b000404 | prose | pages [12] -->
distribution of users. That is to say, the network

<!-- b000405 | prose | pages [12] -->
' V and

<!-- b000406 | prose | pages [12] -->
D V V ( , ) may be not a solution for another u r

<!-- b000407 | prose | pages [12] -->
' D V V ( , ) may not be a solution although the u r

<!-- b000408 | prose | pages [12] -->
V are sampled from an identical uniform distribution. Therefore, user locations of both u u

<!-- b000409 | prose | pages [12] -->
a practical solution should not depend on a specific distribution.

<!-- b000410 | prose | pages [12] -->
To make it possible, we use a continuous approximation instead of the uniform distribution of users. Under this approximation, the number of users is considered as a real variable (do not be surprised if we talk about 94.40 users) and the N users are distributed completely uniformly in the considered area. At any point inside the considered area, the user density, denoted by , is a

<!-- b000411 | prose | pages [12] -->
constant as

<!-- b000412 | prose | pages [12] -->


<!-- b000413 | furniture | pages [12] -->


<!-- b000414 | prose | pages [12] -->
N 

<!-- b000415 | prose | pages [12] -->
(13)

<!-- b000416 | prose | pages [12] -->
 2

<!-- b000417 | prose | pages [12] -->
, the other three constrains are  is the area of . Except the irrelevant constrain 2 where

<!-- b000418 | prose | pages [12] -->
changed correspondingly as

<!-- b000419 | prose | pages [12] -->
2

<!-- b000420 | prose | pages [12] -->
-Capacity constrain. For every repeater rj, if the area of its Voronoi area is SV(rj), it * 1

<!-- b000421 | prose | pages [12] -->
must satisfy the inequality

<!-- b000422 | prose | pages [12] -->
 S

<!-- b000423 | furniture | pages [12] -->


<!-- b000424 | prose | pages [12] -->
V

<!-- b000425 | furniture | pages [12] -->


<!-- b000426 | prose | pages [12] -->
 ( ) r r C (14) j j

<!-- b000427 | furniture | pages [13] -->
Team #9440              Page  12 / 40

<!-- b000428 | prose | pages [13] -->
-Connectivity. Every point in the considered area is covered by at least one repeater. * 3

<!-- b000429 | prose | pages [13] -->
-Global Reachability. The reachable area of every point (considering that at every point, * 4

<!-- b000430 | prose | pages [13] -->
there can be user) is equal to the considered area .

<!-- b000431 | prose | pages [13] -->
Hereinafter, the terms solution and strong solution are all corresponding to the continuous case. Although we assume the users are uniformly distributed, in the real discrete case, the distribution can never be as uniform as the continuous case. The effects of fluctuation in the real distribution of users’ locations (where the number of users is always an integer) will be discussed in the Section 7.

<!-- b000432 | prose | pages [13] -->
As mentioned in Proposition 1 and 2, if we only consider the solution or in the case with R , under continuous approximation, our problem is equivalent to the “circles covering 2 circle” problem if we can easily make sure any two repeaters will not interfere with each other. In a word, we should determine the least number of circles with radius r’ to cover a circle with radius

<!-- b000433 | prose | pages [13] -->
. Notice that, r’ may be smaller than r due to the capacity limitation.

<!-- b000434 | prose | pages [13] -->
R  2 In the frequency range [145MHz, 148MHz] with fc=0.6MHz, in a PL tone, if (when R , any pair of repeaters in the considered area may interfere with each other), there are at most six different repeaters without interference, whose transmitter frequencies are 145.0MHz, 145.6MHz, 146.2MHz, 146.8MHz, 147.4MHz and 148.0MHz. However, according to the pigeonhole principle, there must be a pair of repeaters with inverse frequency pair as f1-f2 and f2-f1 (Here, a repeater represented by f1-f2 has a receiver frequency f1 and a transmitter frequency f2). It is very possible that the former repeater amplifies signals and sends to the latter repeater, and the latter repeater amplifies the received signals and sends back to the former repeater, again the former repeater will amplify the signals and send to the latter repeater, and so on. To avoid such a problem, we consider a set of non-interacting repeaters in a PL tone. Obviously, the maximum number of such a group of repeaters is five. An example set is 145.6-145.0, 146.3-145.7,

<!-- b000435 | prose | pages [13] -->
147.0-146.4, 147.7-147.1 and 147.4-148.0. Therefore, we can conclude that when R , with

<!-- b000436 | prose | pages [13] -->
 N 54 different PL tones, the maximum number of repeaters without any the help of PL

<!-- b000437 | prose | pages [13] -->
  interference is 54 6 324 , and the maximum number of repeaters without any interactions is  54 5 270 . Therefore, if the required number of small circles is no more than 324, we do not need to consider the interference avoidance constrain but just set these repeaters to make sure they do not interfere with each other, while if the required number is no more than 270, we can make sure there will not be any needless interactions between repeaters. Of course, if we consider the

<!-- b000438 | prose | pages [13] -->
R , the situation is much more complicated, and interactions between 2 strong solution with repeaters are generally necessary.

<!-- b000439 | prose | pages [13] -->
According to the connectivity constrain, in any solution, the number of repeaters M should satisfy the inequality

<!-- b000440 | prose | pages [13] -->


<!-- b000441 | prose | pages [13] -->


<!-- b000442 | prose | pages [13] -->
2

<!-- b000443 | prose | pages [13] -->
 

<!-- b000444 | prose | pages [13] -->
M

<!-- b000445 | furniture | pages [13] -->


<!-- b000446 | prose | pages [13] -->


<!-- b000447 | prose | pages [13] -->
2 r

<!-- b000448 | prose | pages [13] -->
M  7

<!-- b000449 | prose | pages [13] -->
 

<!-- b000450 | prose | pages [13] -->
2 2

<!-- b000451 | prose | pages [13] -->
40

<!-- b000452 | prose | pages [13] -->
 

<!-- b000453 | prose | pages [13] -->
6.85

<!-- b000454 | prose | pages [13] -->
(15)

<!-- b000455 | prose | pages [13] -->
2 2 2 r r 15.28

<!-- b000456 | prose | pages [13] -->
. According to the capacity constrain, in any solution, the Since M is an integer, we have number of repeaters M should satisfy the inequality

<!-- b000457 | furniture | pages [13] -->


<!-- b000458 | furniture | pages [14] -->
Team #9440              Page  13 / 40

<!-- b000459 | prose | pages [14] -->
 M

<!-- b000460 | furniture | pages [14] -->


<!-- b000461 | prose | pages [14] -->
N N  (16) C 118

<!-- b000462 | prose | pages [14] -->
M  9 In this problem, for N=1000, the lower boundary of M is 9 (i.e., M  85 85 (i.e., ).

<!-- b000463 | furniture | pages [14] -->


<!-- b000464 | heading | pages [14] -->
4.4 Naïve Solution

<!-- b000465 | prose | pages [14] -->
), while for N=10000, it is

<!-- b000466 | prose | pages [14] -->
Cellular networks are widely used in placing the relay nodes, especially in the design of the locations of base stations in mobile wireless networks. In this paper, as a naïve solution, we directly apply the cellular network structure to cover the considered area. Table 2 illustrates some small-size cellular networks, each of them can be considered as the Voronoi diagram [13] where the center of each regular hexagon lays a repeater. Clearly, the number of regular hexagons is equal to the number of repeaters M.

<!-- b000467 | prose | pages [14] -->
We firstly consider an inverse problem, that is, given a number of equal regular hexagons (we assume the edge length is a unit), to determine the largest circle that can be fully covered by these regular hexagons (these hexagons must be arranged in a beehive-like pattern). Table 2 gives the results up to 13 regular hexagons, which are calculated by hand.

<!-- b000468 | furniture | pages [14] -->


<!-- b000469 | caption | pages [14] -->
Table 2: The cellular networks that can cover the largest circle. The third column lists the radiuses

<!-- b000470 | prose | pages [14] -->
of the corresponding circles. Given the number of cells M, sometimes, the cellular networks are not unique, and then we only draw one of them as a representative.

<!-- b000471 | prose | pages [14] -->
The schematic diagram

<!-- b000472 | prose | pages [14] -->
The number of

<!-- b000473 | prose | pages [14] -->
cells, M

<!-- b000474 | prose | pages [14] -->
1

<!-- b000475 | prose | pages [14] -->
2

<!-- b000476 | prose | pages [14] -->
3

<!-- b000477 | prose | pages [14] -->
4

<!-- b000478 | prose | pages [14] -->
5

<!-- b000479 | furniture | pages [14] -->


<!-- b000480 | prose | pages [14] -->
The radius of the largest

<!-- b000481 | prose | pages [14] -->
circle can be covered

<!-- b000482 | furniture | pages [14] -->


<!-- b000483 | furniture | pages [14] -->


<!-- b000484 | furniture | pages [14] -->


<!-- b000485 | prose | pages [14] -->
3 2

<!-- b000486 | furniture | pages [14] -->


<!-- b000487 | furniture | pages [14] -->


<!-- b000488 | prose | pages [14] -->
3 2

<!-- b000489 | prose | pages [14] -->
1

<!-- b000490 | furniture | pages [14] -->


<!-- b000491 | furniture | pages [14] -->


<!-- b000492 | furniture | pages [14] -->


<!-- b000493 | furniture | pages [14] -->


<!-- b000494 | furniture | pages [14] -->


<!-- b000495 | prose | pages [14] -->
7 2

<!-- b000496 | furniture | pages [14] -->


<!-- b000497 | furniture | pages [14] -->


<!-- b000498 | furniture | pages [14] -->


<!-- b000499 | prose | pages [14] -->
7 5

<!-- b000500 | furniture | pages [15] -->
Team #9440              Page  14 / 40

<!-- b000501 | prose | pages [15] -->
6

<!-- b000502 | prose | pages [15] -->
7

<!-- b000503 | prose | pages [15] -->
8

<!-- b000504 | prose | pages [15] -->
9

<!-- b000505 | prose | pages [15] -->
10

<!-- b000506 | prose | pages [15] -->
11

<!-- b000507 | prose | pages [15] -->
12

<!-- b000508 | prose | pages [15] -->
13

<!-- b000509 | furniture | pages [15] -->


<!-- b000510 | furniture | pages [15] -->


<!-- b000511 | furniture | pages [15] -->


<!-- b000512 | prose | pages [15] -->
3

<!-- b000513 | furniture | pages [15] -->


<!-- b000514 | furniture | pages [15] -->


<!-- b000515 | prose | pages [15] -->
2

<!-- b000516 | prose | pages [15] -->
2

<!-- b000517 | furniture | pages [15] -->


<!-- b000518 | furniture | pages [15] -->


<!-- b000519 | prose | pages [15] -->
2

<!-- b000520 | furniture | pages [15] -->


<!-- b000521 | furniture | pages [15] -->


<!-- b000522 | furniture | pages [15] -->


<!-- b000523 | furniture | pages [15] -->


<!-- b000524 | furniture | pages [15] -->


<!-- b000525 | prose | pages [15] -->
19 2

<!-- b000526 | furniture | pages [15] -->


<!-- b000527 | furniture | pages [15] -->


<!-- b000528 | furniture | pages [15] -->


<!-- b000529 | prose | pages [15] -->
19 2

<!-- b000530 | furniture | pages [15] -->


<!-- b000531 | furniture | pages [15] -->


<!-- b000532 | prose | pages [15] -->
7

<!-- b000533 | furniture | pages [15] -->


<!-- b000534 | furniture | pages [15] -->


<!-- b000535 | prose | pages [15] -->
7

<!-- b000536 | prose | pages [15] -->
R  for 2 Here we show how to directly obtain the solution or the strong solution with

<!-- b000537 | prose | pages [15] -->
N    0.1989 the case N=1000 by using Table 2. In this case, the user density is

<!-- b000538 | prose | pages [15] -->
. The

<!-- b000539 | prose | pages [15] -->
  2

<!-- b000540 | prose | pages [15] -->
maximal area of the Voronoi area of any repeater in a cellular network is equal to the area of the regular hexagon (in the edge of the considered area, a repeater’s Voronoi area may be smaller than the area of the regular hexagon). The edge length of the regular hexagon rh should not exceed the communication range r to make sure each point is covered by at least one repeater. In addition, according to the capacity limitation, the edge length rh should satisfy the inequality

<!-- b000541 | furniture | pages [15] -->


<!-- b000542 | furniture | pages [16] -->
Team #9440              Page  15 / 40

<!-- b000543 | prose | pages [16] -->
3 3

<!-- b000544 | furniture | pages [16] -->


<!-- b000545 | prose | pages [16] -->
2  2 2 hr hr C (17)

<!-- b000546 | prose | pages [16] -->
These two conditions determine the possibly longest edge length, and of course, to cover as large circle as possible, we always use the longest rh. In this case, r=15.28 miles, and according to Eq.

<!-- b000547 | prose | pages [16] -->
hr should be no longer than 15.18 miles. Therefore, the edge length of the regular hexagon (17),

<!-- b000548 | prose | pages [16] -->
 19    7 40 is rh=15.18miles. The circle to be covered is of radius miles. Since , 2 hr

<!-- b000549 | prose | pages [16] -->
according to Table 2, 12 repeaters are sufficient to cover the considered area under the constrains of capacity and connectivity, yet 11 repeaters are not possible using the cellular network structure. This solution is shown in Figure 2, and the coordinates of repeaters are presented in Table 3.

<!-- b000550 | prose | pages [16] -->
R , the 2 Notice that, here we only consider the solution or the strong solution with frequencies and PL tones of repeaters are easily to be arranged. As an example, we use three PL tones to make sure there is no interaction or interference.

<!-- b000551 | furniture | pages [16] -->


<!-- b000552 | furniture | pages [16] -->


<!-- b000553 | caption | pages [16] -->
Figure 2: The solution consisted of 12 repeaters arranged in a cellular network. The blue circle

<!-- b000554 | prose | pages [16] -->
denotes the considered area with radius 40miles, the read regular hexagons represent the cellular network, and the blue points in the centers of the regular hexagons denote the positions of repeaters.

<!-- b000555 | furniture | pages [16] -->


<!-- b000556 | prose | pages [16] -->
As shown above, the basic procedure to get the naïve solution contains two steps: (i) find the longest rh, (ii) search the best solution according to Table 2. However, the calculation of the radius of the largest coverable circle is not an easy problem (at least not easy by hand) for many regular hexagons. We only get the analytical results for two particular cases up to 121 circles, where the covered circle’s center is either at the center of the central hexagon or at the intersection of the three more central hexagons.

<!-- b000557 | furniture | pages [16] -->


<!-- b000558 | furniture | pages [17] -->
Team #9440              Page  16 / 40

<!-- b000559 | caption | pages [17] -->
Table 3: The coordinates, frequencies and PL tones of the solution shown in Fig. 2.

<!-- b000560 | prose | pages [17] -->
Repeater

<!-- b000561 | prose | pages [17] -->
x-Coordinate y-Coordinate

<!-- b000562 | prose | pages [17] -->
No.

<!-- b000563 | prose | pages [17] -->
1 -15.1800 0.0000

<!-- b000564 | prose | pages [17] -->
2 7.5900 13.1463

<!-- b000565 | prose | pages [17] -->
3 7.5900 -13.1463

<!-- b000566 | prose | pages [17] -->
4 -15.1800 26.2925

<!-- b000567 | prose | pages [17] -->
5 -37.9500 -12.6411

<!-- b000568 | prose | pages [17] -->
6 -37.9500 12.6411

<!-- b000569 | prose | pages [17] -->
7 -15.1800 -26.2925

<!-- b000570 | prose | pages [17] -->
8 7.5900 39.2733

<!-- b000571 | prose | pages [17] -->
9 7.5900 -39.2733

<!-- b000572 | prose | pages [17] -->
10 30.3600 0.0000

<!-- b000573 | prose | pages [17] -->
11 30.3600 26.0436

<!-- b000574 | prose | pages [17] -->
12 30.3600 -26.0436

<!-- b000575 | furniture | pages [17] -->


<!-- b000576 | prose | pages [17] -->
Receiver

<!-- b000577 | prose | pages [17] -->
Transmitter

<!-- b000578 | prose | pages [17] -->
PL Tone

<!-- b000579 | prose | pages [17] -->
Frequency

<!-- b000580 | prose | pages [17] -->
Frequency

<!-- b000581 | prose | pages [17] -->
145.6 145.0 1

<!-- b000582 | prose | pages [17] -->
146.3 145.7 1

<!-- b000583 | prose | pages [17] -->
147.0 146.4 1

<!-- b000584 | prose | pages [17] -->
147.7 147.1 1

<!-- b000585 | prose | pages [17] -->
147.4 148.0 1

<!-- b000586 | prose | pages [17] -->
145.6 145.0 2

<!-- b000587 | prose | pages [17] -->
146.3 145.7 2

<!-- b000588 | prose | pages [17] -->
147.0 146.4 2

<!-- b000589 | prose | pages [17] -->
147.7 147.1 2

<!-- b000590 | prose | pages [17] -->
147.4 148.0 2

<!-- b000591 | prose | pages [17] -->
145.0 145.6 3

<!-- b000592 | prose | pages [17] -->
147.4 148.0 3

<!-- b000593 | caption | pages [17] -->
Table 4: Analytical results for two particular cases. In the left side the largest covered circle is

<!-- b000594 | prose | pages [17] -->
centered at the center of the central hexagon, while in the right side the largest covered circle is centered at the intersection of the three more central hexagons.

<!-- b000595 | prose | pages [17] -->
Center of a circle                 Intersection of three circle

<!-- b000596 | prose | pages [17] -->
The number

<!-- b000597 | prose | pages [17] -->
The radius of the largest

<!-- b000598 | furniture | pages [17] -->


<!-- b000599 | prose | pages [17] -->
of cells, M

<!-- b000600 | prose | pages [17] -->
coverable circle

<!-- b000601 | furniture | pages [17] -->


<!-- b000602 | prose | pages [17] -->
1 3 2

<!-- b000603 | prose | pages [17] -->
2 7

<!-- b000604 | furniture | pages [17] -->


<!-- b000605 | prose | pages [17] -->
13 3 3 2

<!-- b000606 | prose | pages [17] -->
19 13

<!-- b000607 | furniture | pages [17] -->


<!-- b000608 | prose | pages [17] -->
31 5 3 2

<!-- b000609 | prose | pages [17] -->
37 5

<!-- b000610 | furniture | pages [17] -->


<!-- b000611 | prose | pages [17] -->
55 7 3 2

<!-- b000612 | prose | pages [17] -->
61 43

<!-- b000613 | furniture | pages [17] -->


<!-- b000614 | prose | pages [17] -->
The number

<!-- b000615 | prose | pages [17] -->
The radius of the largest

<!-- b000616 | prose | pages [17] -->
of cells, M

<!-- b000617 | prose | pages [17] -->
coverable circle

<!-- b000618 | prose | pages [17] -->
1 3

<!-- b000619 | prose | pages [17] -->
6 3

<!-- b000620 | prose | pages [17] -->
12 7

<!-- b000621 | prose | pages [17] -->
18 3

<!-- b000622 | prose | pages [17] -->
27 4

<!-- b000623 | prose | pages [17] -->
36 21

<!-- b000624 | prose | pages [17] -->
48 31

<!-- b000625 | prose | pages [17] -->
60 6

<!-- b000626 | furniture | pages [18] -->
Team #9440              Page  17 / 40

<!-- b000627 | furniture | pages [18] -->


<!-- b000628 | prose | pages [18] -->
85 9 3 2

<!-- b000629 | furniture | pages [18] -->


<!-- b000630 | prose | pages [18] -->
91 8

<!-- b000631 | furniture | pages [18] -->


<!-- b000632 | prose | pages [18] -->
121 91

<!-- b000633 | furniture | pages [18] -->


<!-- b000634 | prose | pages [18] -->
N    1.989 In the case N=10000,   2

<!-- b000635 | prose | pages [18] -->


<!-- b000636 | prose | pages [18] -->
hr 

<!-- b000637 | prose | pages [18] -->
 

<!-- b000638 | prose | pages [18] -->
4.80 miles. Since 8 9

<!-- b000639 | prose | pages [18] -->
75 7

<!-- b000640 | prose | pages [18] -->
90 57

<!-- b000641 | prose | pages [18] -->
108 9

<!-- b000642 | prose | pages [18] -->
, according to the capacity constrain Eq. (17), we

<!-- b000643 | prose | pages [18] -->
, according to Table 4, 108 repeaters are sufficient to

<!-- b000644 | prose | pages [18] -->
have

<!-- b000645 | prose | pages [18] -->
hr

<!-- b000646 | prose | pages [18] -->
cover the considered area under the constrains of capacity and connectivity. Since the number of repeaters is smaller than 324, it is easy to arrange them when considering only a solution or a

<!-- b000647 | prose | pages [18] -->
R . Figure 3 shows this solution, and the table containing all the 2 strong solution with coordinates is ignored.

<!-- b000648 | furniture | pages [18] -->


<!-- b000649 | furniture | pages [18] -->


<!-- b000650 | caption | pages [18] -->
Figure 3: The solution consisted of 108 repeaters arranged in a cellular network. The blue circle

<!-- b000651 | prose | pages [18] -->
denotes the considered area with radius 40miles, the red regular hexagons represent the cellular network. The repeaters are also lay in the centers of the regular hexagons (not shown).

<!-- b000652 | furniture | pages [18] -->


<!-- b000653 | furniture | pages [18] -->


<!-- b000654 | furniture | pages [18] -->


<!-- b000655 | furniture | pages [18] -->


<!-- b000656 | furniture | pages [19] -->
Team #9440              Page  18 / 40

<!-- b000657 | heading | pages [19] -->
5 Algorithm

<!-- b000658 | prose | pages [19] -->
This section will present two algorithms. The main algorithm tries to solve the circles covering circle problem with the least number of circles, and the secondary algorithm assigns each repeater the receiver frequency, the transmitter frequency and the PL tone.

<!-- b000659 | prose | pages [19] -->
40

<!-- b000660 | prose | pages [19] -->
30

<!-- b000661 | prose | pages [19] -->
R20

<!-- b000662 | prose | pages [19] -->
20

<!-- b000663 | prose | pages [19] -->
R8

<!-- b000664 | prose | pages [19] -->
R5

<!-- b000665 | prose | pages [19] -->
10

<!-- b000666 | prose | pages [19] -->
R2

<!-- b000667 | prose | pages [19] -->
R13

<!-- b000668 | prose | pages [19] -->
R1

<!-- b000669 | prose | pages [19] -->
0

<!-- b000670 | prose | pages [19] -->
R27

<!-- b000671 | prose | pages [19] -->
-10

<!-- b000672 | prose | pages [19] -->
R7

<!-- b000673 | prose | pages [19] -->
-20

<!-- b000674 | prose | pages [19] -->
R29

<!-- b000675 | prose | pages [19] -->
R3

<!-- b000676 | prose | pages [19] -->
R17

<!-- b000677 | prose | pages [19] -->
-30

<!-- b000678 | prose | pages [19] -->
R18

<!-- b000679 | prose | pages [19] -->
-40

<!-- b000680 | prose | pages [19] -->
-40 -30 -20 -10

<!-- b000681 | prose | pages [19] -->
R19

<!-- b000682 | prose | pages [19] -->
R28

<!-- b000683 | prose | pages [19] -->
R11

<!-- b000684 | prose | pages [19] -->
R15

<!-- b000685 | prose | pages [19] -->
R25

<!-- b000686 | prose | pages [19] -->
R26

<!-- b000687 | prose | pages [19] -->
R23

<!-- b000688 | prose | pages [19] -->
R16

<!-- b000689 | prose | pages [19] -->
R6

<!-- b000690 | prose | pages [19] -->
R4

<!-- b000691 | prose | pages [19] -->
R12

<!-- b000692 | prose | pages [19] -->
R30

<!-- b000693 | prose | pages [19] -->
R9

<!-- b000694 | prose | pages [19] -->
R24

<!-- b000695 | prose | pages [19] -->
R14

<!-- b000696 | prose | pages [19] -->
R10

<!-- b000697 | prose | pages [19] -->
R22

<!-- b000698 | prose | pages [19] -->
R21

<!-- b000699 | prose | pages [19] -->
0 0 10 20 30 40

<!-- b000700 | furniture | pages [19] -->


<!-- b000701 | caption | pages [19] -->
Figure 4: Illustration of an initial configuration with 30 repeaters. The coordinates of each

<!-- b000702 | prose | pages [19] -->
repeater are generated randomly inside the considered area.

<!-- b000703 | furniture | pages [19] -->


<!-- b000704 | prose | pages [19] -->
40

<!-- b000705 | prose | pages [19] -->
30

<!-- b000706 | prose | pages [19] -->
R20

<!-- b000707 | prose | pages [19] -->
20

<!-- b000708 | prose | pages [19] -->
R8

<!-- b000709 | prose | pages [19] -->
R5

<!-- b000710 | prose | pages [19] -->
10

<!-- b000711 | prose | pages [19] -->
R2

<!-- b000712 | prose | pages [19] -->
R13

<!-- b000713 | prose | pages [19] -->
R1

<!-- b000714 | prose | pages [19] -->
0

<!-- b000715 | prose | pages [19] -->
R27

<!-- b000716 | prose | pages [19] -->
-10

<!-- b000717 | prose | pages [19] -->
R7

<!-- b000718 | prose | pages [19] -->
-20

<!-- b000719 | prose | pages [19] -->
R29

<!-- b000720 | prose | pages [19] -->
R3

<!-- b000721 | prose | pages [19] -->
R17

<!-- b000722 | prose | pages [19] -->
-30

<!-- b000723 | prose | pages [19] -->
R18

<!-- b000724 | prose | pages [19] -->
-40

<!-- b000725 | prose | pages [19] -->
-40 -30 -20 -10

<!-- b000726 | prose | pages [19] -->
R19

<!-- b000727 | prose | pages [19] -->
R28

<!-- b000728 | prose | pages [19] -->
R11

<!-- b000729 | prose | pages [19] -->
R15

<!-- b000730 | prose | pages [19] -->
R25

<!-- b000731 | prose | pages [19] -->
R26

<!-- b000732 | prose | pages [19] -->
R23

<!-- b000733 | prose | pages [19] -->
R16

<!-- b000734 | prose | pages [19] -->
R6

<!-- b000735 | prose | pages [19] -->
R4

<!-- b000736 | prose | pages [19] -->
R12

<!-- b000737 | prose | pages [19] -->
R30

<!-- b000738 | prose | pages [19] -->
R9

<!-- b000739 | prose | pages [19] -->
R24

<!-- b000740 | prose | pages [19] -->
R14

<!-- b000741 | prose | pages [19] -->
R10

<!-- b000742 | prose | pages [19] -->
R22

<!-- b000743 | prose | pages [19] -->
R21

<!-- b000744 | prose | pages [19] -->
0 0 10 20 30 40

<!-- b000745 | furniture | pages [19] -->


<!-- b000746 | caption | pages [19] -->
Figure 5: The resulted Voronoi diagram corresponding to the configuration shown in Fig. 4.

<!-- b000747 | furniture | pages [19] -->


<!-- b000748 | furniture | pages [19] -->


<!-- b000749 | furniture | pages [20] -->
Team #9440              Page  19 / 40

<!-- b000750 | prose | pages [20] -->
Before running the algorithm, we first determine the lower boundary of M according to Eqs. (15) and (16). The boundary is denoted by M0. The procedure of the algorithm is as follows.

<!-- b000751 | prose | pages [20] -->
(1) Randomly place M0 repeaters in the considered area (See Fig. 4). (2) Divide the area into different parts in terms of Voronoi diagram, that is to say, determine

<!-- b000752 | prose | pages [20] -->
the Voronoi area of each repeater. The algorithm can be found in Ref. [13], and one can see Fig. 5 for the resulted Voronoi diagram of the above configuration. Notice that, for some repeaters close to the edge of the considered area, their Voronoi areas may contain a part of the edge of the considered area. (3) Determine the circumscribed circle of each Voronoi area (i.e., a circle which can cover

<!-- b000753 | prose | pages [20] -->
the area and meanwhile has the minimal radius). A standard algorithm can be found in Ref. [14], an advanced method can be found in Ref. [19]. We apply the standard method. The corresponding result after Fig. 5 is shown in Fig. 6.

<!-- b000754 | furniture | pages [20] -->


<!-- b000755 | prose | pages [20] -->
40

<!-- b000756 | prose | pages [20] -->
30

<!-- b000757 | prose | pages [20] -->
R20

<!-- b000758 | prose | pages [20] -->
20

<!-- b000759 | prose | pages [20] -->
R8

<!-- b000760 | prose | pages [20] -->
R5

<!-- b000761 | prose | pages [20] -->
10

<!-- b000762 | prose | pages [20] -->
R2

<!-- b000763 | prose | pages [20] -->
R13

<!-- b000764 | prose | pages [20] -->
R1

<!-- b000765 | prose | pages [20] -->
0

<!-- b000766 | prose | pages [20] -->
R27

<!-- b000767 | prose | pages [20] -->
-10

<!-- b000768 | prose | pages [20] -->
R7

<!-- b000769 | prose | pages [20] -->
-20

<!-- b000770 | prose | pages [20] -->
R29

<!-- b000771 | prose | pages [20] -->
R3

<!-- b000772 | prose | pages [20] -->
R17

<!-- b000773 | prose | pages [20] -->
-30

<!-- b000774 | prose | pages [20] -->
R18

<!-- b000775 | prose | pages [20] -->
-40

<!-- b000776 | prose | pages [20] -->
-40 -30 -20 -10

<!-- b000777 | prose | pages [20] -->
R19

<!-- b000778 | prose | pages [20] -->
R28

<!-- b000779 | prose | pages [20] -->
R11

<!-- b000780 | prose | pages [20] -->
R15

<!-- b000781 | prose | pages [20] -->
R25

<!-- b000782 | prose | pages [20] -->
R26

<!-- b000783 | prose | pages [20] -->
R23

<!-- b000784 | prose | pages [20] -->
R16

<!-- b000785 | prose | pages [20] -->
R6

<!-- b000786 | prose | pages [20] -->
R4

<!-- b000787 | prose | pages [20] -->
R12

<!-- b000788 | prose | pages [20] -->
R30

<!-- b000789 | prose | pages [20] -->
R9

<!-- b000790 | prose | pages [20] -->
R24

<!-- b000791 | prose | pages [20] -->
R14

<!-- b000792 | prose | pages [20] -->
R10

<!-- b000793 | prose | pages [20] -->
R22

<!-- b000794 | prose | pages [20] -->
R21

<!-- b000795 | prose | pages [20] -->
0 10 20 30 40

<!-- b000796 | furniture | pages [20] -->


<!-- b000797 | caption | pages [20] -->
Figure 6: The circumscribed circles of the Voronoi areas, corresponding to the ones shown in Fig.

<!-- b000798 | prose | pages [20] -->
5. The circumscribed circles are colored in green while the Voronoi areas are colored in red. Notice that, for the some repeaters close to the edge of the considered area, their Voronoi areas may contain a part of the edge of the considered area.

<!-- b000799 | furniture | pages [20] -->


<!-- b000800 | prose | pages [20] -->
(4) Calculate the coordinates of the center of each circumscribed circle. (5) Calculate the distance from each repeater’s current location to the centers of the

<!-- b000801 | prose | pages [20] -->
corresponding circumscribed circle. Sum up all the distances and compare the sum to a

<!-- b000802 | prose | pages [20] -->
threshold . If the sum is less than , the current set of repeaters’ locations is

<!-- b000803 | prose | pages [20] -->
considered to be converged. If it is converged, go to step (6), otherwise, move each repeater to the center of the corresponding circumscribed circle (see figure 7) and go

<!-- b000804 | furniture | pages [20] -->


<!-- b000805 | furniture | pages [21] -->
Team #9440              Page  20 / 40

<!-- b000806 | prose | pages [21] -->
back to step (2). (6) Calculate the number of users in each Voronoi region and see if the number is less than

<!-- b000807 | prose | pages [21] -->
the repeater’s capacity, and the radius of the circumscribed circle should be less than the communication radius of users. If so, stop the algorithm and output the current solution. Otherwise, go to step (7) (7) With the current number of repeaters, if the number of extremal optimization operations

<!-- b000808 | prose | pages [21] -->
is less than a threshold Tc, pick up the repeater with the smallest Voronoi area, move it to a random position in the considered area and go back to step (2) and count an extremal optimization operation. Otherwise, add one more repeater, randomized the positions of all repeaters, and go back to step (2).

<!-- b000809 | furniture | pages [21] -->


<!-- b000810 | prose | pages [21] -->
40

<!-- b000811 | prose | pages [21] -->
30

<!-- b000812 | prose | pages [21] -->
R20

<!-- b000813 | prose | pages [21] -->
20

<!-- b000814 | prose | pages [21] -->
R8

<!-- b000815 | prose | pages [21] -->
R5

<!-- b000816 | prose | pages [21] -->
10

<!-- b000817 | prose | pages [21] -->
R2

<!-- b000818 | prose | pages [21] -->
R13

<!-- b000819 | prose | pages [21] -->
R1

<!-- b000820 | prose | pages [21] -->
0

<!-- b000821 | prose | pages [21] -->
R27

<!-- b000822 | prose | pages [21] -->
-10

<!-- b000823 | prose | pages [21] -->
R7

<!-- b000824 | prose | pages [21] -->
-20

<!-- b000825 | prose | pages [21] -->
R29

<!-- b000826 | prose | pages [21] -->
R3

<!-- b000827 | prose | pages [21] -->
R17

<!-- b000828 | prose | pages [21] -->
-30

<!-- b000829 | prose | pages [21] -->
R18

<!-- b000830 | prose | pages [21] -->
-40

<!-- b000831 | prose | pages [21] -->
-40 -30 -20 -10

<!-- b000832 | prose | pages [21] -->
R19

<!-- b000833 | prose | pages [21] -->
R28

<!-- b000834 | prose | pages [21] -->
R11

<!-- b000835 | prose | pages [21] -->
R15

<!-- b000836 | prose | pages [21] -->
R25

<!-- b000837 | prose | pages [21] -->
R26

<!-- b000838 | prose | pages [21] -->
R23

<!-- b000839 | prose | pages [21] -->
R16

<!-- b000840 | prose | pages [21] -->
R6

<!-- b000841 | prose | pages [21] -->
R4

<!-- b000842 | prose | pages [21] -->
R12

<!-- b000843 | prose | pages [21] -->
R30

<!-- b000844 | prose | pages [21] -->
R9

<!-- b000845 | prose | pages [21] -->
R24

<!-- b000846 | prose | pages [21] -->
R14

<!-- b000847 | prose | pages [21] -->
R10

<!-- b000848 | prose | pages [21] -->
R22

<!-- b000849 | prose | pages [21] -->
R21

<!-- b000850 | prose | pages [21] -->
0 10 20 30 40

<!-- b000851 | furniture | pages [21] -->


<!-- b000852 | caption | pages [21] -->
Figure 7: The black asterisks stand for the locations of repeaters, the red ones represent the

<!-- b000853 | prose | pages [21] -->
centers of the circumscribed circles, and the black arrows show the directions towards which the repeaters will move. This illustration corresponds to the result shown in Fig. 6.

<!-- b000854 | furniture | pages [21] -->


<!-- b000855 | prose | pages [21] -->
Here, the Voronoi area can be considered as the contribution of the corresponding repeater, and thus a repeater with smaller Voronoi area is less effective. The so-called extremal optimization is a method to escape the local optimum by every time change the individual with the least fitness. This idea originally comes from the Bak-Sneppen model [20] that describes the punctuated equilibrium in evolution caused by the annihilation of the least fit species. In the simulation, we

<!-- b000856 | prose | pages [21] -->
cT   100 0.01 set and .

<!-- b000857 | prose | pages [21] -->
Next we present the secondary algorithm, whose task is to assign each repeater a receiving

<!-- b000858 | furniture | pages [21] -->


<!-- b000859 | furniture | pages [22] -->
Team #9440              Page  21 / 40

<!-- b000860 | prose | pages [22] -->
frequency, a transmitting frequency and a PL tone. This algorithm will not change the locations of the repeaters obtained from the first algorithm, and will not add new repeaters. That is to say, this algorithm tries to maximize the reachable area of users just by rearranging the frequencies and PL tones of repeaters. The procedure of the algorithm is presented as follows.

<!-- b000861 | prose | pages [22] -->
40

<!-- b000862 | prose | pages [22] -->
30

<!-- b000863 | prose | pages [22] -->
Rp21

<!-- b000864 | prose | pages [22] -->
20

<!-- b000865 | prose | pages [22] -->
Rp11

<!-- b000866 | prose | pages [22] -->
10

<!-- b000867 | prose | pages [22] -->
Rp9 Rp10

<!-- b000868 | prose | pages [22] -->
0

<!-- b000869 | prose | pages [22] -->
Rp15

<!-- b000870 | prose | pages [22] -->
-10

<!-- b000871 | prose | pages [22] -->
Rp12

<!-- b000872 | prose | pages [22] -->
Rp19

<!-- b000873 | prose | pages [22] -->
-20

<!-- b000874 | prose | pages [22] -->
-30

<!-- b000875 | prose | pages [22] -->
Rp5

<!-- b000876 | prose | pages [22] -->
-40 -40 -30 -20 -10

<!-- b000877 | prose | pages [22] -->
Rp7

<!-- b000878 | prose | pages [22] -->
Rp4

<!-- b000879 | prose | pages [22] -->
Rp3

<!-- b000880 | prose | pages [22] -->
Rp13

<!-- b000881 | prose | pages [22] -->
Rp20

<!-- b000882 | prose | pages [22] -->
Rp16

<!-- b000883 | prose | pages [22] -->
Rp14

<!-- b000884 | prose | pages [22] -->
Rp8

<!-- b000885 | prose | pages [22] -->
Rp2

<!-- b000886 | prose | pages [22] -->
Rp6

<!-- b000887 | prose | pages [22] -->
Rp18

<!-- b000888 | prose | pages [22] -->
Rp1

<!-- b000889 | prose | pages [22] -->
Rp17

<!-- b000890 | prose | pages [22] -->
0 0 10 20 30 40

<!-- b000891 | furniture | pages [22] -->


<!-- b000892 | caption | pages [22] -->
Figure 8: The red asterisks represent the repeaters while a green line connecting two repeaters if

<!-- b000893 | prose | pages [22] -->
they have the chance to transmit signals (i.e., within a distance R).

<!-- b000894 | furniture | pages [22] -->


<!-- b000895 | prose | pages [22] -->
40

<!-- b000896 | prose | pages [22] -->
Rp20

<!-- b000897 | prose | pages [22] -->
Rp13

<!-- b000898 | prose | pages [22] -->
30

<!-- b000899 | prose | pages [22] -->
Rp8

<!-- b000900 | prose | pages [22] -->
Rp3

<!-- b000901 | prose | pages [22] -->
Rp10

<!-- b000902 | prose | pages [22] -->
20

<!-- b000903 | prose | pages [22] -->
Rp9

<!-- b000904 | prose | pages [22] -->
Rp12

<!-- b000905 | prose | pages [22] -->
10

<!-- b000906 | prose | pages [22] -->
Rp5

<!-- b000907 | prose | pages [22] -->
Rp17 Rp16

<!-- b000908 | prose | pages [22] -->
Rp2

<!-- b000909 | prose | pages [22] -->
0

<!-- b000910 | prose | pages [22] -->
Rp4

<!-- b000911 | prose | pages [22] -->
Rp7

<!-- b000912 | prose | pages [22] -->
-10

<!-- b000913 | prose | pages [22] -->
Rp18

<!-- b000914 | prose | pages [22] -->
Rp21

<!-- b000915 | prose | pages [22] -->
Rp1

<!-- b000916 | prose | pages [22] -->
-20

<!-- b000917 | prose | pages [22] -->
Rp6

<!-- b000918 | prose | pages [22] -->
Rp11

<!-- b000919 | prose | pages [22] -->
Rp19

<!-- b000920 | prose | pages [22] -->
-30

<!-- b000921 | prose | pages [22] -->
Rp15

<!-- b000922 | prose | pages [22] -->
Rp14

<!-- b000923 | prose | pages [22] -->
-40 -40 -30 -20 -10 0 10 20 30 40

<!-- b000924 | prose | pages [22] -->
40

<!-- b000925 | prose | pages [22] -->
Rp20

<!-- b000926 | prose | pages [22] -->
Rp13

<!-- b000927 | prose | pages [22] -->
30

<!-- b000928 | prose | pages [22] -->
Rp8

<!-- b000929 | prose | pages [22] -->
Rp3

<!-- b000930 | prose | pages [22] -->
Rp10

<!-- b000931 | prose | pages [22] -->
20

<!-- b000932 | prose | pages [22] -->
Rp9

<!-- b000933 | prose | pages [22] -->
Rp12

<!-- b000934 | prose | pages [22] -->
10

<!-- b000935 | prose | pages [22] -->
Rp5

<!-- b000936 | prose | pages [22] -->
Rp17 Rp16

<!-- b000937 | prose | pages [22] -->
Rp2

<!-- b000938 | prose | pages [22] -->
0

<!-- b000939 | prose | pages [22] -->
Rp4

<!-- b000940 | prose | pages [22] -->
Rp7

<!-- b000941 | prose | pages [22] -->
-10

<!-- b000942 | prose | pages [22] -->
Rp18

<!-- b000943 | prose | pages [22] -->
Rp21

<!-- b000944 | prose | pages [22] -->
Rp1

<!-- b000945 | prose | pages [22] -->
-20

<!-- b000946 | prose | pages [22] -->
Rp6

<!-- b000947 | prose | pages [22] -->
Rp11

<!-- b000948 | prose | pages [22] -->
Rp19

<!-- b000949 | prose | pages [22] -->
-30

<!-- b000950 | prose | pages [22] -->
Rp15

<!-- b000951 | prose | pages [22] -->
Rp14

<!-- b000952 | prose | pages [22] -->
-40 -40 -30 -20 -10 0 10 20 30 40

<!-- b000953 | furniture | pages [22] -->


<!-- b000954 | prose | pages [22] -->
(a)A maximum spanning tree             (b) A minimum spanning tree

<!-- b000955 | caption | pages [22] -->
Figure 9: Illustration of the maximum spanning tree (a) and the minimum spanning tree (b) of G

<!-- b000956 | prose | pages [22] -->
The red lines are the edges in the spanning trees and green lines are the other edges in the graph

<!-- b000957 | prose | pages [22] -->
G .

<!-- b000958 | furniture | pages [22] -->


<!-- b000959 | prose | pages [22] -->
(1) Construct a graph G to represent the relation that two repeaters have the ability to

<!-- b000960 | prose | pages [22] -->
transmit signal to each other. That is to say, if the distance between two repeaters is less than R, we add one edge between them (see Fig. 8)

<!-- b000961 | prose | pages [22] -->
(2) Find the minimum spanning tree T or the maximum spanning tree

<!-- b000962 | furniture | pages [22] -->


<!-- b000963 | prose | pages [22] -->
T of G . From '

<!-- b000964 | furniture | pages [23] -->
Team #9440              Page  22 / 40

<!-- b000965 | prose | pages [23] -->
the illustration shown in Fig. 9, one can see that edges in the minimum spanning tree will not intersect. If we build the signal transmission paths along the minimum spanning tree, the signals received by repeaters are fewer than the case of maximum spanning tree. However, since the distance between two adjacent repeaters along the tree is the shortest, the received signals will be much stronger than other type of assignment. So the assignment based on the minimum spanning tree is suitable for communication in local area. In contrast, most edges in maximum spanning tree intersect with each other, the number of signals in many areas is very large and signals can cover larger areas. However, this increases the possibility of frequency interference. For different purposes, one can choose different spanning tree to continue our algorithm. (3) Remove edges from the spanning tree. For any node i whose degree k is larger than 3, we

<!-- b000966 | prose | pages [23] -->
delete k-2 edges. Then the node i will be divided apart from k-2 connected components.

<!-- b000967 | prose | pages [23] -->
SC , then the method of removing edges can be Let the size of component j be j j

<!-- b000968 | prose | pages [23] -->
 

<!-- b000969 | prose | pages [23] -->
|

<!-- b000970 | prose | pages [23] -->
SC SC

<!-- b000971 | prose | pages [23] -->
|

<!-- b000972 | prose | pages [23] -->
presented as follows: find k-2 edges to remove in order to minimize

<!-- b000973 | prose | pages [23] -->
The results can be found in Fig. 10.

<!-- b000974 | prose | pages [23] -->
.

<!-- b000975 | prose | pages [23] -->
a b a b

<!-- b000976 | prose | pages [23] -->
,

<!-- b000977 | prose | pages [23] -->
(4) After the step 3, we can obtain several distinct signal routes that do not connect. Assign a

<!-- b000978 | prose | pages [23] -->
different PL tone to each distinct route. Then for the repeaters in each different route, assign its transmitting frequency and receiving frequency. Make sure the transmitting frequency of a repeater is the receiving frequency of the repeater’s neighbors in the same signal route.

<!-- b000979 | furniture | pages [23] -->


<!-- b000980 | prose | pages [23] -->
40

<!-- b000981 | prose | pages [23] -->
Rp20

<!-- b000982 | prose | pages [23] -->
Rp13

<!-- b000983 | prose | pages [23] -->
30

<!-- b000984 | prose | pages [23] -->
Rp8

<!-- b000985 | prose | pages [23] -->
Rp3

<!-- b000986 | prose | pages [23] -->
Rp10

<!-- b000987 | prose | pages [23] -->
20

<!-- b000988 | prose | pages [23] -->
Rp9

<!-- b000989 | prose | pages [23] -->
Rp12

<!-- b000990 | prose | pages [23] -->
10

<!-- b000991 | prose | pages [23] -->
Rp5

<!-- b000992 | prose | pages [23] -->
Rp17 Rp16

<!-- b000993 | prose | pages [23] -->
Rp2

<!-- b000994 | prose | pages [23] -->
0

<!-- b000995 | prose | pages [23] -->
Rp4

<!-- b000996 | prose | pages [23] -->
Rp7

<!-- b000997 | prose | pages [23] -->
-10

<!-- b000998 | prose | pages [23] -->
Rp18

<!-- b000999 | prose | pages [23] -->
Rp21

<!-- b001000 | prose | pages [23] -->
Rp1

<!-- b001001 | prose | pages [23] -->
-20

<!-- b001002 | prose | pages [23] -->
Rp6

<!-- b001003 | prose | pages [23] -->
Rp11

<!-- b001004 | prose | pages [23] -->
Rp19

<!-- b001005 | prose | pages [23] -->
-30

<!-- b001006 | prose | pages [23] -->
Rp15

<!-- b001007 | prose | pages [23] -->
Rp14

<!-- b001008 | prose | pages [23] -->
-40 -40 -30 -20 -10 0 10 20 30 40

<!-- b001009 | prose | pages [23] -->
40

<!-- b001010 | prose | pages [23] -->
Rp20

<!-- b001011 | prose | pages [23] -->
Rp13

<!-- b001012 | prose | pages [23] -->
30

<!-- b001013 | prose | pages [23] -->
Rp8

<!-- b001014 | prose | pages [23] -->
Rp3

<!-- b001015 | prose | pages [23] -->
Rp10

<!-- b001016 | prose | pages [23] -->
20

<!-- b001017 | prose | pages [23] -->
Rp9

<!-- b001018 | prose | pages [23] -->
Rp12

<!-- b001019 | prose | pages [23] -->
10

<!-- b001020 | prose | pages [23] -->
Rp5

<!-- b001021 | prose | pages [23] -->
Rp17 Rp16

<!-- b001022 | prose | pages [23] -->
Rp2

<!-- b001023 | prose | pages [23] -->
0

<!-- b001024 | prose | pages [23] -->
Rp4

<!-- b001025 | prose | pages [23] -->
Rp7

<!-- b001026 | prose | pages [23] -->
-10

<!-- b001027 | prose | pages [23] -->
Rp18

<!-- b001028 | prose | pages [23] -->
Rp21

<!-- b001029 | prose | pages [23] -->
Rp1

<!-- b001030 | prose | pages [23] -->
-20

<!-- b001031 | prose | pages [23] -->
Rp6

<!-- b001032 | prose | pages [23] -->
Rp11

<!-- b001033 | prose | pages [23] -->
Rp19

<!-- b001034 | prose | pages [23] -->
-30

<!-- b001035 | prose | pages [23] -->
Rp15

<!-- b001036 | prose | pages [23] -->
Rp14

<!-- b001037 | prose | pages [23] -->
-40 -40 -30 -20 -10 0 10 20 30 40

<!-- b001038 | furniture | pages [23] -->


<!-- b001039 | prose | pages [23] -->
(a)Signal routes in maximum spanning tree    (b) Signal routes in minimum spanning tree

<!-- b001040 | caption | pages [23] -->
Figure 10: The resulted routes after the removal of edges, corresponding to the spanning tree in

<!-- b001041 | prose | pages [23] -->
Fig 9. The red dashed lines represent the removed edges, while the blue solid lines are the reserved ones. The repeaters on the same blue line share the same tone.

<!-- b001042 | furniture | pages [23] -->


<!-- b001043 | furniture | pages [23] -->


<!-- b001044 | furniture | pages [23] -->


<!-- b001045 | furniture | pages [23] -->


<!-- b001046 | furniture | pages [23] -->


<!-- b001047 | furniture | pages [23] -->


<!-- b001048 | furniture | pages [23] -->


<!-- b001049 | furniture | pages [23] -->


<!-- b001050 | furniture | pages [24] -->
Team #9440              Page  23 / 40

<!-- b001051 | heading | pages [24] -->
6 Simulation Results

<!-- b001052 | prose | pages [24] -->
In this section, we present the strong solutions obtained by the proposed algorithm. The analysis in subsection 4.1 indicates that R is larger than the diameter of the considered area, and thus a solution is also a strong solution. In subsection 6.1 and 6.2, we will show the algorithmic results for N=1000 and N=10000, with R=85.45miles. The number if required repeaters are 11 and 104 respectively, better than the ones obtained by the naïve solution, 12 and 108. In subsection 6.1, we will prove that 11 is the optimal solution. Notice that, the calculation made in subsection 4.1 is based on an ideal circumstance, while the fog or rain can largely affect the transmitting of signal and reduce the effective communication range of a repeater. Therefore, in subsection 6.3 and 6.4, we will discuss the cases with shorter R. Since the communication range R will be affected by the weather, when discussing the interference, we should consider the case with large R to avoid possible interference in good weather while when discussing the global reachability, we should consider short R to make sure any point-to-point communication is possible even under bad

<!-- b001053 | prose | pages [24] -->
weather. Therefore, as in the ideal case the communication range is larger than the diameter ( 2) of the considered area (when R , any two repeaters may interfere with each other) we always guarantee that the transmitter frequency difference between any two repeaters sharing the same PL tone is no less than 0.6MHz. In subsections 6.3 and 6.4, we assume that R=40miles.

<!-- b001054 | furniture | pages [24] -->


<!-- b001055 | heading | pages [24] -->
6.1 N=1000, R=85.45

<!-- b001056 | caption | pages [24] -->
Figure 11 reports a solution with 11 repeaters obtained by our algorithm. The maximal

<!-- b001057 | prose | pages [24] -->
Voronoi area is 560.56, the user density is 0.1989, and thus the largest capacity demand is 112, smaller than the repeater’s capacity C=119. The advantage of this result compared with the naïve solution is twofold: (i) the number of required repeaters is smaller; (ii) the sizes of Voronoi areas of repeaters are more homogeneous. Detailed information of the repeaters is presented in Table 5.

<!-- b001058 | furniture | pages [24] -->


<!-- b001059 | caption | pages [24] -->
Figure 11: The solution consisted of 11 repeaters obtained by our algorithm. The blue circle

<!-- b001060 | prose | pages [24] -->
denotes the considered area with radius 40miles, the red small circles represent the ability of receiving signals from users, and the blue points in the centers of the small red circles denote the positions of repeaters.

<!-- b001061 | furniture | pages [24] -->


<!-- b001062 | furniture | pages [25] -->
Team #9440              Page  24 / 40

<!-- b001063 | caption | pages [25] -->
Table 5: The coordinates, frequencies and PL tones of the solution shown in Fig. 11.

<!-- b001064 | prose | pages [25] -->
Repeater

<!-- b001065 | prose | pages [25] -->
x-Coordinate y-Coordinate

<!-- b001066 | prose | pages [25] -->
No.

<!-- b001067 | prose | pages [25] -->
1 -38.3765 0.0000

<!-- b001068 | prose | pages [25] -->
2 -24.3880 -23.0549

<!-- b001069 | prose | pages [25] -->
3 -24.3880 23.0549

<!-- b001070 | prose | pages [25] -->
4 -12.4503 0.0000

<!-- b001071 | prose | pages [25] -->
5 -3.6744 -27.7292

<!-- b001072 | prose | pages [25] -->
6 -3.9222 27.5753

<!-- b001073 | prose | pages [25] -->
7 4.6059 0.0000

<!-- b001074 | prose | pages [25] -->
8 14.5012 26.5499

<!-- b001075 | prose | pages [25] -->
9 15.0139 -26.5499

<!-- b001076 | prose | pages [25] -->
10 29.2673 -11.0660

<!-- b001077 | prose | pages [25] -->
11 29.2673 11.0660

<!-- b001078 | prose | pages [25] -->
Receiver

<!-- b001079 | prose | pages [25] -->
Transmitter

<!-- b001080 | prose | pages [25] -->
PL Tone

<!-- b001081 | prose | pages [25] -->
Frequency

<!-- b001082 | prose | pages [25] -->
Frequency

<!-- b001083 | prose | pages [25] -->
145.6 145.0 1

<!-- b001084 | prose | pages [25] -->
146.3 145.7 1

<!-- b001085 | prose | pages [25] -->
147.0 146.4 1

<!-- b001086 | prose | pages [25] -->
147.7 147.1 1

<!-- b001087 | prose | pages [25] -->
147.4 148.0 1

<!-- b001088 | prose | pages [25] -->
145.6 145.0 2

<!-- b001089 | prose | pages [25] -->
146.3 145.7 2

<!-- b001090 | prose | pages [25] -->
147.0 146.4 2

<!-- b001091 | prose | pages [25] -->
147.7 147.1 2

<!-- b001092 | prose | pages [25] -->
147.4 148.0 2

<!-- b001093 | prose | pages [25] -->
145.0 145.6 3

<!-- b001094 | furniture | pages [25] -->


<!-- b001095 | furniture | pages [25] -->


<!-- b001096 | prose | pages [25] -->
We next prove that the solution shown in Table 5 with 11 repeaters is the optimal solution, namely 10 repeaters with radius no more than 15.28miles cannot cover a circle with radius 40miles.

<!-- b001097 | prose | pages [25] -->
Lemma 1 [21]: Let r(n) be the maximum radius of a circular disc that can be covered by n closed unit circles, then r(n)=1+2cos(2π/(n−1)) for n=8, n=9, and n=10.

<!-- b001098 | prose | pages [25] -->
Proposition 3: To cover a circular area with radius 40, the least number of circles with radius 15.28 is 11.

<!-- b001099 | prose | pages [25] -->
Proof. Table 5 has already shown a possible solution, and thus we only need to prove that to cover with 10 circles is not possible. According to Lemma 1, r(10)=1+2cos(2/9π)=2.532, which is smaller than the ratio 40/15.28=2.618, and thus the coverage with 10 circles is not possible.

<!-- b001100 | prose | pages [25] -->
■

<!-- b001101 | heading | pages [25] -->
6.2 N=10000, R=85.45

<!-- b001102 | caption | pages [25] -->
Figure 12 reports a solution with 104 repeaters obtained by our algorithm, with the detailed

<!-- b001103 | prose | pages [25] -->
information of repeaters shown in Table 6. 21 PL tones are used to guarantee that every pair of repeaters will not interact each other.

<!-- b001104 | furniture | pages [25] -->


<!-- b001105 | furniture | pages [25] -->


<!-- b001106 | furniture | pages [26] -->
Team #9440              Page  25 / 40

<!-- b001107 | prose | pages [26] -->
40

<!-- b001108 | prose | pages [26] -->
30

<!-- b001109 | prose | pages [26] -->
20

<!-- b001110 | prose | pages [26] -->
10

<!-- b001111 | prose | pages [26] -->
0

<!-- b001112 | prose | pages [26] -->
-10

<!-- b001113 | prose | pages [26] -->
-20

<!-- b001114 | prose | pages [26] -->
-30

<!-- b001115 | prose | pages [26] -->
-40

<!-- b001116 | prose | pages [26] -->
-40 -30 -20 -10 0 10 20 30 40

<!-- b001117 | furniture | pages [26] -->


<!-- b001118 | caption | pages [26] -->
Figure 12: The solution consisted of 104 repeaters obtained by our algorithm. The blue circle

<!-- b001119 | prose | pages [26] -->
denotes the considered area with radius 40miles, the red areas are the corresponding Voronoi areas and the blue points denote the positions of repeaters.

<!-- b001120 | furniture | pages [26] -->


<!-- b001121 | caption | pages [26] -->
Table 6: The coordinates, frequencies and PL tones of the solution shown in Fig. 12.

<!-- b001122 | prose | pages [26] -->
Repeater

<!-- b001123 | prose | pages [26] -->
x-Coordinate y-Coordinate

<!-- b001124 | prose | pages [26] -->
No.

<!-- b001125 | prose | pages [26] -->
1 -21.4846 10.7841

<!-- b001126 | prose | pages [26] -->
2 20.0881 9.8614

<!-- b001127 | prose | pages [26] -->
3 -24.3006 -16.2601

<!-- b001128 | prose | pages [26] -->
4 13.8192 -27.0256

<!-- b001129 | prose | pages [26] -->
5 -38.7037 -1.9022

<!-- b001130 | prose | pages [26] -->
6 1.0018 12.7802

<!-- b001131 | prose | pages [26] -->
7 -13.2011 13.9291

<!-- b001132 | prose | pages [26] -->
8 26.0811 8.6698

<!-- b001133 | prose | pages [26] -->
9 26.8280 -5.1802

<!-- b001134 | prose | pages [26] -->
10 -18.9492 -33.9863

<!-- b001135 | prose | pages [26] -->
11 -19.2527 17.5280

<!-- b001136 | prose | pages [26] -->
12 -36.7795 -10.8329

<!-- b001137 | prose | pages [26] -->
13 27.8500 -10.6307

<!-- b001138 | prose | pages [26] -->
14 19.6493 24.5973

<!-- b001139 | prose | pages [26] -->
15 -6.8453 -37.6773

<!-- b001140 | furniture | pages [26] -->


<!-- b001141 | prose | pages [26] -->
Receiver

<!-- b001142 | prose | pages [26] -->
Transmitter

<!-- b001143 | prose | pages [26] -->
PL

<!-- b001144 | prose | pages [26] -->
Frequency

<!-- b001145 | prose | pages [26] -->
Frequency

<!-- b001146 | prose | pages [26] -->
Tone

<!-- b001147 | prose | pages [26] -->
145.6 145.0 1

<!-- b001148 | prose | pages [26] -->
146.3 145.7 1

<!-- b001149 | prose | pages [26] -->
147.0 146.4 1

<!-- b001150 | prose | pages [26] -->
147.7 147.1 1

<!-- b001151 | prose | pages [26] -->
147.4 148.0 1

<!-- b001152 | prose | pages [26] -->
145.6 145.0 2

<!-- b001153 | prose | pages [26] -->
146.3 145.7 2

<!-- b001154 | prose | pages [26] -->
147.0 146.4 2

<!-- b001155 | prose | pages [26] -->
147.7 147.1 2

<!-- b001156 | prose | pages [26] -->
147.4 148.0 2

<!-- b001157 | prose | pages [26] -->
145.6 145.0 3

<!-- b001158 | prose | pages [26] -->
146.3 145.7 3

<!-- b001159 | prose | pages [26] -->
147.0 146.4 3

<!-- b001160 | prose | pages [26] -->
147.7 147.1 3

<!-- b001161 | prose | pages [26] -->
147.4 148.0 3

<!-- b001162 | furniture | pages [27] -->
Team #9440              Page  26 / 40

<!-- b001163 | prose | pages [27] -->
16 -12.0455 -33.8082

<!-- b001164 | prose | pages [27] -->
17 18.2067 -4.1299

<!-- b001165 | prose | pages [27] -->
18 -31.0283 22.1830

<!-- b001166 | prose | pages [27] -->
19 14.0491 22.4823

<!-- b001167 | prose | pages [27] -->
20 -25.2712 28.5517

<!-- b001168 | prose | pages [27] -->
21 6.0148 9.6461

<!-- b001169 | prose | pages [27] -->
22 -5.2833 -22.9543

<!-- b001170 | prose | pages [27] -->
23 -24.2711 4.0665

<!-- b001171 | prose | pages [27] -->
24 -7.2155 -29.6266

<!-- b001172 | prose | pages [27] -->
25 23.5724 -18.8907

<!-- b001173 | prose | pages [27] -->
26 0.7092 -8.6258

<!-- b001174 | prose | pages [27] -->
27 -22.0810 22.4277

<!-- b001175 | prose | pages [27] -->
28 -4.6952 -3.5107

<!-- b001176 | prose | pages [27] -->
29 -28.4376 -23.5828

<!-- b001177 | prose | pages [27] -->
30 15.0935 36.0433

<!-- b001178 | prose | pages [27] -->
31 -10.0930 1.3872

<!-- b001179 | prose | pages [27] -->
32 8.9930 -33.6010

<!-- b001180 | prose | pages [27] -->
33 -10.8101 34.2136

<!-- b001181 | prose | pages [27] -->
34 -16.5338 28.0647

<!-- b001182 | prose | pages [27] -->
35 2.7253 -1.7304

<!-- b001183 | prose | pages [27] -->
36 -28.9439 -10.5425

<!-- b001184 | prose | pages [27] -->
37 28.9259 13.9310

<!-- b001185 | prose | pages [27] -->
38 17.4628 -20.3533

<!-- b001186 | prose | pages [27] -->
39 -18.4778 34.4848

<!-- b001187 | prose | pages [27] -->
40 -15.3172 -13.9991

<!-- b001188 | prose | pages [27] -->
41 -13.8680 -4.9981

<!-- b001189 | prose | pages [27] -->
42 -7.1204 9.4823

<!-- b001190 | prose | pages [27] -->
43 35.9930 -5.8130

<!-- b001191 | prose | pages [27] -->
44 -12.9073 -22.4915

<!-- b001192 | prose | pages [27] -->
45 6.5647 36.2554

<!-- b001193 | prose | pages [27] -->
46 23.7103 31.8433

<!-- b001194 | prose | pages [27] -->
47 -12.7061 22.2901

<!-- b001195 | prose | pages [27] -->
48 3.9099 -13.5329

<!-- b001196 | prose | pages [27] -->
49 -20.2166 -9.6509

<!-- b001197 | prose | pages [27] -->
50 -19.1212 -0.5781

<!-- b001198 | prose | pages [27] -->
51 1.7840 -38.9554

<!-- b001199 | prose | pages [27] -->
52 6.1130 -27.4748

<!-- b001200 | prose | pages [27] -->
53 13.3601 15.2740

<!-- b001201 | prose | pages [27] -->
54 -15.5091 -26.6073

<!-- b001202 | prose | pages [27] -->
55 35.3109 -13.2947

<!-- b001203 | prose | pages [27] -->
56 -25.5448 -4.7593

<!-- b001204 | furniture | pages [27] -->


<!-- b001205 | prose | pages [27] -->
145.6 145.0 4

<!-- b001206 | prose | pages [27] -->
146.3 145.7 4

<!-- b001207 | prose | pages [27] -->
147.0 146.4 4

<!-- b001208 | prose | pages [27] -->
147.7 147.1 4

<!-- b001209 | prose | pages [27] -->
147.4 148.0 4

<!-- b001210 | prose | pages [27] -->
145.6 145.0 5

<!-- b001211 | prose | pages [27] -->
146.3 145.7 5

<!-- b001212 | prose | pages [27] -->
147.0 146.4 5

<!-- b001213 | prose | pages [27] -->
147.7 147.1 5

<!-- b001214 | prose | pages [27] -->
147.4 148.0 5

<!-- b001215 | prose | pages [27] -->
145.6 145.0 6

<!-- b001216 | prose | pages [27] -->
146.3 145.7 6

<!-- b001217 | prose | pages [27] -->
147.0 146.4 6

<!-- b001218 | prose | pages [27] -->
147.7 147.1 6

<!-- b001219 | prose | pages [27] -->
147.4 148.0 6

<!-- b001220 | prose | pages [27] -->
145.6 145.0 7

<!-- b001221 | prose | pages [27] -->
146.3 145.7 7

<!-- b001222 | prose | pages [27] -->
147.0 146.4 7

<!-- b001223 | prose | pages [27] -->
147.7 147.1 7

<!-- b001224 | prose | pages [27] -->
147.4 148.0 7

<!-- b001225 | prose | pages [27] -->
145.6 145.0 8

<!-- b001226 | prose | pages [27] -->
146.3 145.7 8

<!-- b001227 | prose | pages [27] -->
147.0 146.4 8

<!-- b001228 | prose | pages [27] -->
147.7 147.1 8

<!-- b001229 | prose | pages [27] -->
147.4 148.0 8

<!-- b001230 | prose | pages [27] -->
145.6 145.0 9

<!-- b001231 | prose | pages [27] -->
146.3 145.7 9

<!-- b001232 | prose | pages [27] -->
147.0 146.4 9

<!-- b001233 | prose | pages [27] -->
147.7 147.1 9

<!-- b001234 | prose | pages [27] -->
147.4 148.0 9

<!-- b001235 | prose | pages [27] -->
145.6 145.0 10

<!-- b001236 | prose | pages [27] -->
146.3 145.7 10

<!-- b001237 | prose | pages [27] -->
147.0 146.4 10

<!-- b001238 | prose | pages [27] -->
147.7 147.1 10

<!-- b001239 | prose | pages [27] -->
147.4 148.0 10

<!-- b001240 | prose | pages [27] -->
145.6 145.0 11

<!-- b001241 | prose | pages [27] -->
146.3 145.7 11

<!-- b001242 | prose | pages [27] -->
147.0 146.4 11

<!-- b001243 | prose | pages [27] -->
147.7 147.1 11

<!-- b001244 | prose | pages [27] -->
147.4 148.0 11

<!-- b001245 | prose | pages [27] -->
145.6 145.0 12

<!-- b001246 | furniture | pages [28] -->
Team #9440              Page  27 / 40

<!-- b001247 | prose | pages [28] -->
57 30.9858 19.5100

<!-- b001248 | prose | pages [28] -->
58 8.6603 -20.2950

<!-- b001249 | prose | pages [28] -->
59 -15.3072 6.1877

<!-- b001250 | prose | pages [28] -->
60 -8.2420 26.4597

<!-- b001251 | prose | pages [28] -->
61 -1.3574 21.7607

<!-- b001252 | prose | pages [28] -->
62 -19.9827 -20.4432

<!-- b001253 | prose | pages [28] -->
63 -30.1025 8.9472

<!-- b001254 | prose | pages [28] -->
64 5.9444 17.4680

<!-- b001255 | prose | pages [28] -->
65 -0.5221 29.9967

<!-- b001256 | prose | pages [28] -->
66 0.6271 -29.8848

<!-- b001257 | prose | pages [28] -->
67 -3.6197 -13.9964

<!-- b001258 | prose | pages [28] -->
68 5.9811 23.8501

<!-- b001259 | prose | pages [28] -->
69 -32.7771 -17.8837

<!-- b001260 | prose | pages [28] -->
70 9.2566 -6.0159

<!-- b001261 | prose | pages [28] -->
71 20.3993 -11.3469

<!-- b001262 | prose | pages [28] -->
72 28.6670 -25.6027

<!-- b001263 | prose | pages [28] -->
73 38.1683 1.7115

<!-- b001264 | prose | pages [28] -->
74 -36.8485 6.2865

<!-- b001265 | prose | pages [28] -->
75 12.1489 -10.6071

<!-- b001266 | prose | pages [28] -->
76 -36.2190 14.8745

<!-- b001267 | prose | pages [28] -->
77 15.3432 29.9396

<!-- b001268 | prose | pages [28] -->
78 37.3272 13.5208

<!-- b001269 | prose | pages [28] -->
79 12.7538 1.2800

<!-- b001270 | prose | pages [28] -->
80 -8.7399 -8.9681

<!-- b001271 | prose | pages [28] -->
81 -23.6555 -27.8664

<!-- b001272 | prose | pages [28] -->
82 22.1340 -28.0080

<!-- b001273 | prose | pages [28] -->
83 30.7725 -18.5245

<!-- b001274 | prose | pages [28] -->
84 -9.5450 -17.3707

<!-- b001275 | prose | pages [28] -->
85 13.0948 -15.5244

<!-- b001276 | prose | pages [28] -->
86 34.6099 6.7702

<!-- b001277 | prose | pages [28] -->
87 18.0988 -32.7824

<!-- b001278 | prose | pages [28] -->
88 13.6878 7.6081

<!-- b001279 | prose | pages [28] -->
89 5.6810 2.5887

<!-- b001280 | prose | pages [28] -->
90 -31.1704 0.1887

<!-- b001281 | prose | pages [28] -->
91 10.9276 -37.9560

<!-- b001282 | prose | pages [28] -->
92 21.3901 2.2075

<!-- b001283 | prose | pages [28] -->
93 -0.1086 -34.3627

<!-- b001284 | prose | pages [28] -->
94 7.9409 29.8451

<!-- b001285 | prose | pages [28] -->
95 0.6967 -21.3952

<!-- b001286 | prose | pages [28] -->
96 -27.7998 16.0646

<!-- b001287 | prose | pages [28] -->
97 -1.9265 4.5995

<!-- b001288 | furniture | pages [28] -->


<!-- b001289 | prose | pages [28] -->
146.3 145.7 12

<!-- b001290 | prose | pages [28] -->
147.0 146.4 12

<!-- b001291 | prose | pages [28] -->
147.7 147.1 12

<!-- b001292 | prose | pages [28] -->
147.4 148.0 12

<!-- b001293 | prose | pages [28] -->
145.6 145.0 13

<!-- b001294 | prose | pages [28] -->
146.3 145.7 13

<!-- b001295 | prose | pages [28] -->
147.0 146.4 13

<!-- b001296 | prose | pages [28] -->
147.7 147.1 13

<!-- b001297 | prose | pages [28] -->
147.4 148.0 13

<!-- b001298 | prose | pages [28] -->
145.6 145.0 14

<!-- b001299 | prose | pages [28] -->
146.3 145.7 14

<!-- b001300 | prose | pages [28] -->
147.0 146.4 14

<!-- b001301 | prose | pages [28] -->
147.7 147.1 14

<!-- b001302 | prose | pages [28] -->
147.4 148.0 14

<!-- b001303 | prose | pages [28] -->
145.6 145.0 15

<!-- b001304 | prose | pages [28] -->
146.3 145.7 15

<!-- b001305 | prose | pages [28] -->
147.0 146.4 15

<!-- b001306 | prose | pages [28] -->
147.7 147.1 15

<!-- b001307 | prose | pages [28] -->
147.4 148.0 15

<!-- b001308 | prose | pages [28] -->
145.6 145.0 16

<!-- b001309 | prose | pages [28] -->
146.3 145.7 16

<!-- b001310 | prose | pages [28] -->
147.0 146.4 16

<!-- b001311 | prose | pages [28] -->
147.7 147.1 16

<!-- b001312 | prose | pages [28] -->
147.4 148.0 16

<!-- b001313 | prose | pages [28] -->
145.6 145.0 17

<!-- b001314 | prose | pages [28] -->
146.3 145.7 17

<!-- b001315 | prose | pages [28] -->
147.0 146.4 17

<!-- b001316 | prose | pages [28] -->
147.7 147.1 17

<!-- b001317 | prose | pages [28] -->
147.4 148.0 17

<!-- b001318 | prose | pages [28] -->
145.6 145.0 18

<!-- b001319 | prose | pages [28] -->
146.3 145.7 18

<!-- b001320 | prose | pages [28] -->
147.0 146.4 18

<!-- b001321 | prose | pages [28] -->
147.7 147.1 18

<!-- b001322 | prose | pages [28] -->
147.4 148.0 18

<!-- b001323 | prose | pages [28] -->
145.6 145.0 19

<!-- b001324 | prose | pages [28] -->
146.3 145.7 19

<!-- b001325 | prose | pages [28] -->
147.0 146.4 19

<!-- b001326 | prose | pages [28] -->
147.7 147.1 19

<!-- b001327 | prose | pages [28] -->
147.4 148.0 19

<!-- b001328 | prose | pages [28] -->
145.6 145.0 20

<!-- b001329 | prose | pages [28] -->
146.3 145.7 20

<!-- b001330 | furniture | pages [29] -->
Team #9440              Page  28 / 40

<!-- b001331 | prose | pages [29] -->
98 -5.8836 17.3017

<!-- b001332 | prose | pages [29] -->
99 21.6476 17.3278

<!-- b001333 | prose | pages [29] -->
100 29.7908 0.7205

<!-- b001334 | prose | pages [29] -->
101 -6.6019 34.9874

<!-- b001335 | prose | pages [29] -->
102 26.8732 24.1059

<!-- b001336 | prose | pages [29] -->
103 -0.9480 37.5368

<!-- b001337 | prose | pages [29] -->
104 -34.8281 -5.6874

<!-- b001338 | furniture | pages [29] -->


<!-- b001339 | heading | pages [29] -->
6.3 N=1000, R=40

<!-- b001340 | prose | pages [29] -->
147.0 146.4 20

<!-- b001341 | prose | pages [29] -->
147.7 147.1 20

<!-- b001342 | prose | pages [29] -->
147.4 148.0 20

<!-- b001343 | prose | pages [29] -->
145.6 145.0 21

<!-- b001344 | prose | pages [29] -->
146.3 145.7 21

<!-- b001345 | prose | pages [29] -->
147.0 146.4 21

<!-- b001346 | prose | pages [29] -->
147.7 147.1 21

<!-- b001347 | prose | pages [29] -->
As mentioned in Section 5, we will not add more repeaters to make sure every user can communicate with other users at any positions in the considered area. Instead, our secondary algorithm tries to maximize the reachable areas of users. Therefore, the repeaters’ locations of the solutions in subsections 6.3 and 6.4 are the same to those in subsections 6.1 and 6.2. However, the frequencies and PL tones are different.

<!-- b001348 | furniture | pages [29] -->


<!-- b001349 | caption | pages [29] -->
Table 7: The coordinates, frequencies and PL tones of the solution shown in Fig. 11.

<!-- b001350 | prose | pages [29] -->
Repeater

<!-- b001351 | prose | pages [29] -->
x-Coordinate y-Coordinate

<!-- b001352 | prose | pages [29] -->
No.

<!-- b001353 | prose | pages [29] -->
1 -38.3765 0.0000

<!-- b001354 | prose | pages [29] -->
2 -24.3880 -23.0549

<!-- b001355 | prose | pages [29] -->
3 -24.3880 23.0549

<!-- b001356 | prose | pages [29] -->
4 -12.4503 0.0000

<!-- b001357 | prose | pages [29] -->
5 -3.6744 -27.7292

<!-- b001358 | prose | pages [29] -->
6 -3.9222 27.5753

<!-- b001359 | prose | pages [29] -->
7 4.6059 0.0000

<!-- b001360 | prose | pages [29] -->
8 14.5012 26.5499

<!-- b001361 | prose | pages [29] -->
9 15.0139 -26.5499

<!-- b001362 | prose | pages [29] -->
10 29.2673 -11.0660

<!-- b001363 | prose | pages [29] -->
11 29.2673 11.0660

<!-- b001364 | furniture | pages [29] -->


<!-- b001365 | prose | pages [29] -->
Receiver

<!-- b001366 | prose | pages [29] -->
Transmitter

<!-- b001367 | prose | pages [29] -->
PL Tone

<!-- b001368 | prose | pages [29] -->
Frequency

<!-- b001369 | prose | pages [29] -->
Frequency

<!-- b001370 | prose | pages [29] -->
145.0 145.6 1

<!-- b001371 | prose | pages [29] -->
145.0 145.6 2

<!-- b001372 | prose | pages [29] -->
145.0 145.6 3

<!-- b001373 | prose | pages [29] -->
145.6 146.2 1

<!-- b001374 | prose | pages [29] -->
145.6 146.2 2

<!-- b001375 | prose | pages [29] -->
145.6 146.2 3

<!-- b001376 | prose | pages [29] -->
146.2 146.8 1

<!-- b001377 | prose | pages [29] -->
146.2 146.8 3

<!-- b001378 | prose | pages [29] -->
146.2 146.8 2

<!-- b001379 | prose | pages [29] -->
146.8 147.4 2

<!-- b001380 | prose | pages [29] -->
146.8 147.4 3

<!-- b001381 | caption | pages [29] -->
Table 7 presents the result for N=1000. To test the effectiveness of the secondary algorithm,

<!-- b001382 | prose | pages [29] -->
we randomly pick up 100000 ordered pairs of points (u,v) inside the considered area to see in how many pairs, u can send to v signals. The answer is 90708, namely given a user, the probability that the system can satisfy this user’s requirement to communicate with a random user is about 90.71%.

<!-- b001383 | furniture | pages [29] -->


<!-- b001384 | heading | pages [29] -->
6.4 N=10000, R=40

<!-- b001385 | caption | pages [29] -->
Table 8 reports the result for N=10000. Similar to the solution in subsection 6.4, this solution

<!-- b001386 | prose | pages [29] -->
could not guarantee that a user can communicate with other users in any positions in the considered area. However, it seems that when the required number of repeaters increases, the reachable area of a user increases. For example, in this case, for the solution shown in Table 8, the corresponding probability is 97.12%。

<!-- b001387 | furniture | pages [29] -->


<!-- b001388 | furniture | pages [29] -->


<!-- b001389 | furniture | pages [30] -->
Team #9440              Page  29 / 40

<!-- b001390 | caption | pages [30] -->
Table 8: The coordinates, frequencies and PL tones of the solution shown in Fig. 12.

<!-- b001391 | prose | pages [30] -->
Repeater

<!-- b001392 | prose | pages [30] -->
x-Coordinate y-Coordinate

<!-- b001393 | prose | pages [30] -->
No.

<!-- b001394 | prose | pages [30] -->
1 -21.4846 10.7841

<!-- b001395 | prose | pages [30] -->
2 20.0881 9.8614

<!-- b001396 | prose | pages [30] -->
3 -24.3006 -16.2601

<!-- b001397 | prose | pages [30] -->
4 13.8192 -27.0256

<!-- b001398 | prose | pages [30] -->
5 -38.7037 -1.9022

<!-- b001399 | prose | pages [30] -->
6 1.0018 12.7802

<!-- b001400 | prose | pages [30] -->
7 -13.2011 13.9291

<!-- b001401 | prose | pages [30] -->
8 26.0811 8.6698

<!-- b001402 | prose | pages [30] -->
9 26.8280 -5.1802

<!-- b001403 | prose | pages [30] -->
10 -18.9492 -33.9863

<!-- b001404 | prose | pages [30] -->
11 -19.2527 17.5280

<!-- b001405 | prose | pages [30] -->
12 -36.7795 -10.8329

<!-- b001406 | prose | pages [30] -->
13 27.8500 -10.6307

<!-- b001407 | prose | pages [30] -->
14 19.6493 24.5973

<!-- b001408 | prose | pages [30] -->
15 -6.8453 -37.6773

<!-- b001409 | prose | pages [30] -->
16 -12.0455 -33.8082

<!-- b001410 | prose | pages [30] -->
17 18.2067 -4.1299

<!-- b001411 | prose | pages [30] -->
18 -31.0283 22.1830

<!-- b001412 | prose | pages [30] -->
19 14.0491 22.4823

<!-- b001413 | prose | pages [30] -->
20 -25.2712 28.5517

<!-- b001414 | prose | pages [30] -->
21 6.0148 9.6461

<!-- b001415 | prose | pages [30] -->
22 -5.2833 -22.9543

<!-- b001416 | prose | pages [30] -->
23 -24.2711 4.0665

<!-- b001417 | prose | pages [30] -->
24 -7.2155 -29.6266

<!-- b001418 | prose | pages [30] -->
25 23.5724 -18.8907

<!-- b001419 | prose | pages [30] -->
26 0.7092 -8.6258

<!-- b001420 | prose | pages [30] -->
27 -22.0810 22.4277

<!-- b001421 | prose | pages [30] -->
28 -4.6952 -3.5107

<!-- b001422 | prose | pages [30] -->
29 -28.4376 -23.5828

<!-- b001423 | prose | pages [30] -->
30 15.0935 36.0433

<!-- b001424 | prose | pages [30] -->
31 -10.0930 1.3872

<!-- b001425 | prose | pages [30] -->
32 8.9930 -33.6010

<!-- b001426 | prose | pages [30] -->
33 -10.8101 34.2136

<!-- b001427 | prose | pages [30] -->
34 -16.5338 28.0647

<!-- b001428 | prose | pages [30] -->
35 2.7253 -1.7304

<!-- b001429 | prose | pages [30] -->
36 -28.9439 -10.5425

<!-- b001430 | prose | pages [30] -->
37 28.9259 13.9310

<!-- b001431 | prose | pages [30] -->
38 17.4628 -20.3533

<!-- b001432 | prose | pages [30] -->
39 -18.4778 34.4848

<!-- b001433 | furniture | pages [30] -->


<!-- b001434 | prose | pages [30] -->
Receiver

<!-- b001435 | prose | pages [30] -->
Transmitter

<!-- b001436 | prose | pages [30] -->
PL

<!-- b001437 | prose | pages [30] -->
Frequency

<!-- b001438 | prose | pages [30] -->
Frequency

<!-- b001439 | prose | pages [30] -->
Tone

<!-- b001440 | prose | pages [30] -->
145.0 145.6 1

<!-- b001441 | prose | pages [30] -->
145.6 146.2 2

<!-- b001442 | prose | pages [30] -->
145.6 146.2 3

<!-- b001443 | prose | pages [30] -->
145.0 145.6 4

<!-- b001444 | prose | pages [30] -->
145.0 145.6 5

<!-- b001445 | prose | pages [30] -->
145.6 146.2 6

<!-- b001446 | prose | pages [30] -->
145.0 145.6 7

<!-- b001447 | prose | pages [30] -->
146.2 146.8 2

<!-- b001448 | prose | pages [30] -->
145.6 146.2 8

<!-- b001449 | prose | pages [30] -->
145.0 145.6 9

<!-- b001450 | prose | pages [30] -->
145.6 146.2 1

<!-- b001451 | prose | pages [30] -->
146.2 146.8 5

<!-- b001452 | prose | pages [30] -->
145.0 145.6 8

<!-- b001453 | prose | pages [30] -->
146.2 146.8 10

<!-- b001454 | prose | pages [30] -->
146.2 146.8 9

<!-- b001455 | prose | pages [30] -->
145.6 146.2 9

<!-- b001456 | prose | pages [30] -->
145.6 146.2 11

<!-- b001457 | prose | pages [30] -->
145.0 145.6 12

<!-- b001458 | prose | pages [30] -->
145.0 145.6 13

<!-- b001459 | prose | pages [30] -->
146.8 147.4 1

<!-- b001460 | prose | pages [30] -->
146.2 146.8 6

<!-- b001461 | prose | pages [30] -->
145.6 146.2 14

<!-- b001462 | prose | pages [30] -->
146.2 146.8 15

<!-- b001463 | prose | pages [30] -->
146.2 146.8 14

<!-- b001464 | prose | pages [30] -->
145.6 146.2 16

<!-- b001465 | prose | pages [30] -->
145.6 146.2 17

<!-- b001466 | prose | pages [30] -->
146.2 146.8 1

<!-- b001467 | prose | pages [30] -->
146.2 146.8 18

<!-- b001468 | prose | pages [30] -->
145.6 146.2 19

<!-- b001469 | prose | pages [30] -->
145.0 145.6 10

<!-- b001470 | prose | pages [30] -->
145.6 146.2 18

<!-- b001471 | prose | pages [30] -->
145.6 146.2 20

<!-- b001472 | prose | pages [30] -->
145.6 146.2 21

<!-- b001473 | prose | pages [30] -->
146.2 146.8 22

<!-- b001474 | prose | pages [30] -->
146.2 146.8 17

<!-- b001475 | prose | pages [30] -->
146.2 146.8 3

<!-- b001476 | prose | pages [30] -->
146.8 147.4 2

<!-- b001477 | prose | pages [30] -->
145.0 145.6 16

<!-- b001478 | prose | pages [30] -->
145.0 145.6 21

<!-- b001479 | furniture | pages [31] -->
Team #9440              Page  30 / 40

<!-- b001480 | prose | pages [31] -->
40 -15.3172 -13.9991

<!-- b001481 | prose | pages [31] -->
41 -13.8680 -4.9981

<!-- b001482 | prose | pages [31] -->
42 -7.1204 9.4823

<!-- b001483 | prose | pages [31] -->
43 35.9930 -5.8130

<!-- b001484 | prose | pages [31] -->
44 -12.9073 -22.4915

<!-- b001485 | prose | pages [31] -->
45 6.5647 36.2554

<!-- b001486 | prose | pages [31] -->
46 23.7103 31.8433

<!-- b001487 | prose | pages [31] -->
47 -12.7061 22.2901

<!-- b001488 | prose | pages [31] -->
48 3.9099 -13.5329

<!-- b001489 | prose | pages [31] -->
49 -20.2166 -9.6509

<!-- b001490 | prose | pages [31] -->
50 -19.1212 -0.5781

<!-- b001491 | prose | pages [31] -->
51 1.7840 -38.9554

<!-- b001492 | prose | pages [31] -->
52 6.1130 -27.4748

<!-- b001493 | prose | pages [31] -->
53 13.3601 15.2740

<!-- b001494 | prose | pages [31] -->
54 -15.5091 -26.6073

<!-- b001495 | prose | pages [31] -->
55 35.3109 -13.2947

<!-- b001496 | prose | pages [31] -->
56 -25.5448 -4.7593

<!-- b001497 | prose | pages [31] -->
57 30.9858 19.5100

<!-- b001498 | prose | pages [31] -->
58 8.6603 -20.2950

<!-- b001499 | prose | pages [31] -->
59 -15.3072 6.1877

<!-- b001500 | prose | pages [31] -->
60 -8.2420 26.4597

<!-- b001501 | prose | pages [31] -->
61 -1.3574 21.7607

<!-- b001502 | prose | pages [31] -->
62 -19.9827 -20.4432

<!-- b001503 | prose | pages [31] -->
63 -30.1025 8.9472

<!-- b001504 | prose | pages [31] -->
64 5.9444 17.4680

<!-- b001505 | prose | pages [31] -->
65 -0.5221 29.9967

<!-- b001506 | prose | pages [31] -->
66 0.6271 -29.8848

<!-- b001507 | prose | pages [31] -->
67 -3.6197 -13.9964

<!-- b001508 | prose | pages [31] -->
68 5.9811 23.8501

<!-- b001509 | prose | pages [31] -->
69 -32.7771 -17.8837

<!-- b001510 | prose | pages [31] -->
70 9.2566 -6.0159

<!-- b001511 | prose | pages [31] -->
71 20.3993 -11.3469

<!-- b001512 | prose | pages [31] -->
72 28.6670 -25.6027

<!-- b001513 | prose | pages [31] -->
73 38.1683 1.7115

<!-- b001514 | prose | pages [31] -->
74 -36.8485 6.2865

<!-- b001515 | prose | pages [31] -->
75 12.1489 -10.6071

<!-- b001516 | prose | pages [31] -->
76 -36.2190 14.8745

<!-- b001517 | prose | pages [31] -->
77 15.3432 29.9396

<!-- b001518 | prose | pages [31] -->
78 37.3272 13.5208

<!-- b001519 | prose | pages [31] -->
79 12.7538 1.2800

<!-- b001520 | prose | pages [31] -->
80 -8.7399 -8.9681

<!-- b001521 | furniture | pages [31] -->


<!-- b001522 | prose | pages [31] -->
146.2 146.8 24

<!-- b001523 | prose | pages [31] -->
145.6 146.2 22

<!-- b001524 | prose | pages [31] -->
145.6 146.2 7

<!-- b001525 | prose | pages [31] -->
145.0 145.6 1

<!-- b001526 | prose | pages [31] -->
145.6 146.2 25

<!-- b001527 | prose | pages [31] -->
145.0 145.6 26

<!-- b001528 | prose | pages [31] -->
146.8 147.4 10

<!-- b001529 | prose | pages [31] -->
145.6 146.2 22

<!-- b001530 | prose | pages [31] -->
145.0 145.6 17

<!-- b001531 | prose | pages [31] -->
145.6 146.2 24

<!-- b001532 | prose | pages [31] -->
145.0 145.6 22

<!-- b001533 | prose | pages [31] -->
145.0 145.6 27

<!-- b001534 | prose | pages [31] -->
145.0 145.6 20

<!-- b001535 | prose | pages [31] -->
145.6 146.2 13

<!-- b001536 | prose | pages [31] -->
145.0 145.6 25

<!-- b001537 | prose | pages [31] -->
145.6 146.2 1

<!-- b001538 | prose | pages [31] -->
145.0 145.6 24

<!-- b001539 | prose | pages [31] -->
145.0 145.6 28

<!-- b001540 | prose | pages [31] -->
145.0 145.6 29

<!-- b001541 | prose | pages [31] -->
145.0 145.6 18

<!-- b001542 | prose | pages [31] -->
145.0 145.6 22

<!-- b001543 | prose | pages [31] -->
145.6 146.2 30

<!-- b001544 | prose | pages [31] -->
145.0 145.6 3

<!-- b001545 | prose | pages [31] -->
145.6 146.2 15

<!-- b001546 | prose | pages [31] -->
145.0 145.6 6

<!-- b001547 | prose | pages [31] -->
145.0 145.6 31

<!-- b001548 | prose | pages [31] -->
146.2 146.8 27

<!-- b001549 | prose | pages [31] -->
145.0 145.6 5

<!-- b001550 | prose | pages [31] -->
146.2 146.8 26

<!-- b001551 | prose | pages [31] -->
145.0 145.6 19

<!-- b001552 | prose | pages [31] -->
146.8 147.4 29

<!-- b001553 | prose | pages [31] -->
146.2 146.8 11

<!-- b001554 | prose | pages [31] -->
146.8 147.4 4

<!-- b001555 | prose | pages [31] -->
145.0 145.6 32

<!-- b001556 | prose | pages [31] -->
145.0 145.6 15

<!-- b001557 | prose | pages [31] -->
146.2 146.8 29

<!-- b001558 | prose | pages [31] -->
146.2 146.8 12

<!-- b001559 | prose | pages [31] -->
145.6 146.2 10

<!-- b001560 | prose | pages [31] -->
145.6 146.2 32

<!-- b001561 | prose | pages [31] -->
145.6 146.2 10

<!-- b001562 | prose | pages [31] -->
146.2 146.8 23

<!-- b001563 | furniture | pages [32] -->
Team #9440              Page  31 / 40

<!-- b001564 | prose | pages [32] -->
81 -23.6555 -27.8664

<!-- b001565 | prose | pages [32] -->
82 22.1340 -28.0080

<!-- b001566 | prose | pages [32] -->
83 30.7725 -18.5245

<!-- b001567 | prose | pages [32] -->
84 -9.5450 -17.3707

<!-- b001568 | prose | pages [32] -->
85 13.0948 -15.5244

<!-- b001569 | prose | pages [32] -->
86 34.6099 6.7702

<!-- b001570 | prose | pages [32] -->
87 18.0988 -32.7824

<!-- b001571 | prose | pages [32] -->
88 13.6878 7.6081

<!-- b001572 | prose | pages [32] -->
89 5.6810 2.5887

<!-- b001573 | prose | pages [32] -->
90 -31.1704 0.1887

<!-- b001574 | prose | pages [32] -->
91 10.9276 -37.9560

<!-- b001575 | prose | pages [32] -->
92 21.3901 2.2075

<!-- b001576 | prose | pages [32] -->
93 -0.1086 -34.3627

<!-- b001577 | prose | pages [32] -->
94 7.9409 29.8451

<!-- b001578 | prose | pages [32] -->
95 0.6967 -21.3952

<!-- b001579 | prose | pages [32] -->
96 -27.7998 16.0646

<!-- b001580 | prose | pages [32] -->
97 -1.9265 4.5995

<!-- b001581 | prose | pages [32] -->
98 -5.8836 17.3017

<!-- b001582 | prose | pages [32] -->
99 21.6476 17.3278

<!-- b001583 | prose | pages [32] -->
100 29.7908 0.7205

<!-- b001584 | prose | pages [32] -->
101 -6.6019 34.9874

<!-- b001585 | prose | pages [32] -->
102 26.8732 24.1059

<!-- b001586 | prose | pages [32] -->
103 -0.9480 37.5368

<!-- b001587 | prose | pages [32] -->
104 -34.8281 -5.6874

<!-- b001588 | furniture | pages [32] -->


<!-- b001589 | furniture | pages [32] -->


<!-- b001590 | furniture | pages [32] -->


<!-- b001591 | furniture | pages [32] -->


<!-- b001592 | furniture | pages [32] -->


<!-- b001593 | furniture | pages [32] -->


<!-- b001594 | furniture | pages [32] -->


<!-- b001595 | furniture | pages [32] -->


<!-- b001596 | furniture | pages [32] -->


<!-- b001597 | furniture | pages [32] -->


<!-- b001598 | furniture | pages [32] -->


<!-- b001599 | furniture | pages [32] -->


<!-- b001600 | furniture | pages [32] -->


<!-- b001601 | furniture | pages [32] -->


<!-- b001602 | furniture | pages [32] -->


<!-- b001603 | furniture | pages [32] -->


<!-- b001604 | furniture | pages [32] -->


<!-- b001605 | furniture | pages [32] -->


<!-- b001606 | furniture | pages [32] -->


<!-- b001607 | prose | pages [32] -->
146.2 146.8 19

<!-- b001608 | prose | pages [32] -->
146.2 146.8 4

<!-- b001609 | prose | pages [32] -->
146.2 146.8 16

<!-- b001610 | prose | pages [32] -->
146.2 146.8 25

<!-- b001611 | prose | pages [32] -->
145.6 146.2 29

<!-- b001612 | prose | pages [32] -->
145.6 146.2 32

<!-- b001613 | prose | pages [32] -->
145.6 146.2 4

<!-- b001614 | prose | pages [32] -->
145.0 145.6 2

<!-- b001615 | prose | pages [32] -->
145.0 145.6 14

<!-- b001616 | prose | pages [32] -->
145.6 146.2 10

<!-- b001617 | prose | pages [32] -->
146.2 146.8 20

<!-- b001618 | prose | pages [32] -->
145.0 145.6 11

<!-- b001619 | prose | pages [32] -->
145.6 146.2 27

<!-- b001620 | prose | pages [32] -->
145.6 146.2 26

<!-- b001621 | prose | pages [32] -->
145.0 145.6 14

<!-- b001622 | prose | pages [32] -->
145.6 146.2 12

<!-- b001623 | prose | pages [32] -->
146.2 146.8 7

<!-- b001624 | prose | pages [32] -->
145.0 145.6 30

<!-- b001625 | prose | pages [32] -->
145.0 145.6 14

<!-- b001626 | prose | pages [32] -->
146.2 146.8 8

<!-- b001627 | prose | pages [32] -->
146.2 146.8 21

<!-- b001628 | prose | pages [32] -->
145.6 146.2 28

<!-- b001629 | prose | pages [32] -->
145.6 146.2 31

<!-- b001630 | prose | pages [32] -->
145.6 146.2 5

<!-- b001631 | furniture | pages [33] -->
Team #9440              Page  32 / 40

<!-- b001632 | heading | pages [33] -->
7 Sensitivity Analysis

<!-- b001633 | prose | pages [33] -->
In subsection 7.1, we will investigate the sensitive of the algorithmic output versus the change of model parameters. In subsection 7.2, we will analysis the error caused by the continuous approximation of user density. In subsection 7.3, we will discuss the possible defects in line-of-sight propagation caused by mountainous areas, as well as some promising ways in solving the repeater placement problem in such circumstance.

<!-- b001634 | furniture | pages [33] -->


<!-- b001635 | heading | pages [33] -->
7.1 Sensitivity of Parameters

<!-- b001636 | prose | pages [33] -->
Most parameters hereinbefore are regarded as constants. However, parameters can be regulated in a certain range, which may have a huge impact on the algorithmic results. Here we discuss to what extent the results depend on the parameters.

<!-- b001637 | furniture | pages [33] -->


<!-- b001638 | caption | pages [33] -->
Figure 13: The Comparison between the least numbers of required repeaters obtained by the

<!-- b001639 | prose | pages [33] -->
proposed algorithm and the Naïve solution. The largest coverable circle in naïve solution 1 is centered at the center of the central hexagon, while the largest coverable circle in naïve solution 2 is centered at the intersection of the three more central hexagons.

<!-- b001640 | furniture | pages [33] -->


<!-- b001641 | caption | pages [33] -->
Figure 13 shows the least number of repeaters versus the number of users. The number of

<!-- b001642 | prose | pages [33] -->
users varies from 100 to 10000. It is clear that the proposed algorithm is better than the Naïve solution. Notice that there is a transition point at about N=1000, which approximately satisfies the equation

<!-- b001643 | prose | pages [33] -->
N

<!-- b001644 | furniture | pages [33] -->


<!-- b001645 | prose | pages [33] -->
 

<!-- b001646 | prose | pages [33] -->
2 C

<!-- b001647 | prose | pages [33] -->
 

<!-- b001648 | prose | pages [33] -->
(18)

<!-- b001649 | prose | pages [33] -->


<!-- b001650 | prose | pages [33] -->
2

<!-- b001651 | prose | pages [33] -->
r

<!-- b001652 | prose | pages [33] -->
Before this transition point, the number of repeaters mainly depends on the communication range r, while after this transition point, capacity becomes the bottleneck determining the least number of require repeaters. Actually, given the considered area, the least number of repeaters keeps as a constant before the transition point. Since the capacity limitation will play the major role when many users are presented, it is not a surprise that the growing tendency of the number of repeaters is linear versus the number of users.

<!-- b001653 | furniture | pages [33] -->


<!-- b001654 | furniture | pages [34] -->
Team #9440              Page  33 / 40

<!-- b001655 | caption | pages [34] -->
Figure 14 reports the relation between the least number of required repeaters and the user’s

<!-- b001656 | prose | pages [34] -->
communication range r. The curves have been normalized through dividing by their respective largest value. In the case N=10000, the number of repeaters never changes with r, again indicating that the capacity limitation determines the result, while when N=1000, the number of repeaters decreases with the increase of user’s communication range.

<!-- b001657 | furniture | pages [34] -->


<!-- b001658 | caption | pages [34] -->
Figure 14: The Comparison between the least numbers of required repeaters obtained by the

<!-- b001659 | prose | pages [34] -->
proposed algorithm and the Naïve solution. The red and black points correspond to the case of N=10000 and N=1000, respectively. Two curves have been normalized.

<!-- b001660 | furniture | pages [34] -->


<!-- b001661 | heading | pages [34] -->
7.2 User Density Fluctuation

<!-- b001662 | prose | pages [34] -->
In the analysis of our model, the user density is a constant in the considered area, behaving like a real variable. However, in reality, the number of users can only be an integer. If we consider the discrete case where users are distributed uniformly, then in a Voronoi area Sv centered by a

<!-- b001663 | prose | pages [34] -->
, and thus the number of 2 vS repeater. Each user belongs to this area with the probability

<!-- b001664 | prose | pages [34] -->
users in this area, X, obeys a Bernoulli distribution

<!-- b001665 | prose | pages [34] -->
 

<!-- b001666 | prose | pages [34] -->
N

<!-- b001667 | prose | pages [34] -->


<!-- b001668 | prose | pages [34] -->
P X

<!-- b001669 | prose | pages [34] -->
( )

<!-- b001670 | furniture | pages [34] -->


<!-- b001671 | prose | pages [34] -->
 

<!-- b001672 | prose | pages [34] -->
 X

<!-- b001673 | prose | pages [34] -->
   

<!-- b001674 | prose | pages [34] -->
X N X

<!-- b001675 | prose | pages [34] -->
 

<!-- b001676 | prose | pages [34] -->
S S S

<!-- b001677 | prose | pages [34] -->


<!-- b001678 | prose | pages [34] -->
v v v

<!-- b001679 | prose | pages [34] -->
1

<!-- b001680 | prose | pages [34] -->
(19)

<!-- b001681 | prose | pages [34] -->
   

<!-- b001682 | prose | pages [34] -->


<!-- b001683 | prose | pages [34] -->


<!-- b001684 | prose | pages [34] -->
2 2 2

<!-- b001685 | prose | pages [34] -->
 

<!-- b001686 | prose | pages [34] -->
whose mathematical expectation and standard deviation are

<!-- b001687 | prose | pages [34] -->
 E X ( ) NS

<!-- b001688 | furniture | pages [34] -->


<!-- b001689 | prose | pages [34] -->
and

<!-- b001690 | prose | pages [34] -->
 NS    v ( X ) 1

<!-- b001691 | furniture | pages [34] -->


<!-- b001692 | prose | pages [34] -->
    2 

<!-- b001693 | prose | pages [34] -->
   2 S (20) v v v

<!-- b001694 | prose | pages [34] -->
 S S S    v v v S 1

<!-- b001695 | prose | pages [34] -->
(21)

<!-- b001696 | prose | pages [34] -->
 v    2 2 

<!-- b001697 | prose | pages [34] -->
When the total number of users N is small, the capacity is not a big problem, and when N is big (corresponding to high user density), the area Sv should be small due to the capacity limitation.

<!-- b001698 | furniture | pages [34] -->


<!-- b001699 | furniture | pages [35] -->
Team #9440              Page  34 / 40

<!-- b001700 | prose | pages [35] -->
Therefore, the standard deviation is about the square root of the expected number of users in the Voronoi area. Of course, we are interested in the case when the number of users in Sv is approaching to the capacity limitation. For example, in this problem, C=119, and thus the standard deviation is about 11. If we would like to set up a tolerance for two times of the standard deviation, the tolerant capacity C’ should satisfy the approximate equation

<!-- b001701 | prose | pages [35] -->
 C ' 2

<!-- b001702 | furniture | pages [35] -->


<!-- b001703 | prose | pages [35] -->
 C ' C (22)

<!-- b001704 | prose | pages [35] -->
leading to an answer C’=99. The qualitative relation is trivial, namely higher tolerance leads to lower capacity and generally corresponds to more repeaters.

<!-- b001705 | furniture | pages [35] -->


<!-- b001706 | heading | pages [35] -->
7.3 Effects of Landscape: Discussing the Mountainous Areas

<!-- b001707 | prose | pages [35] -->
Completely flat area is just a kind of ideal assumption, but the complex landscape is common which should be taken into consideration. Actually, there might be defects in line-of-sight propagation caused by mountainous areas. Here we analyze the impact of landscape on signal transmission, and based on the analysis, we put forward a proposal on how to arrange the position and tone of repeaters.

<!-- b001708 | prose | pages [35] -->
Because the VHF radio spectrum involves line-of-sight transmission and reception, the mountain will obstruct the signal’s diffusion along the straight line. On the other hand, it makes a contribution to avoiding the interference between the two repeaters, even if they are geographically nearby and use close transmitter frequencies. The available spectrum is in the range from 145 to 148MHz and the wavelength is about 2 meters, so the signal wave have a strong ability to bypass the a dwarf, small or single mountain according to diffraction properties of wave. In a word, the situation that the area is full of rolling mountains is the point we should focus on.

<!-- b001709 | furniture | pages [35] -->


<!-- b001710 | furniture | pages [35] -->


<!-- b001711 | furniture | pages [35] -->


<!-- b001712 | furniture | pages [36] -->
Team #9440              Page  35 / 40

<!-- b001713 | caption | pages [36] -->
Figure 15: An illustration about how a signal can be transmitted from a hollow area to a distant

<!-- b001714 | prose | pages [36] -->
place with the help of a hierarchically organized relay network.

<!-- b001715 | furniture | pages [36] -->


<!-- b001716 | prose | pages [36] -->
The proposal put forward here is based on hierarchical organization. We divide all the repeaters into two levels. The repeaters of the first (lower) level, are always located at hollows to make sure all the users can be covered by at least one repeater. The repeaters of the second (higher) level are always located at the top of maintain, who play a central role in the information transmission. The higher altitude the repeater locates at, the wider its communication range is. Comparatively, the signal from hollow is difficult to be received by repeaters. According to the

<!-- b001717 | prose | pages [36] -->
, we must design a suitable arrangement of repeaters covering all the connectivity constrain 3

<!-- b001718 | prose | pages [36] -->
users, so we first put some repeaters in the hollow, and erect them highly enough to make sure the signal they received can be transmitted to a second-lever repeater. The second-level repeaters are always put on the top of maintains to expand the range of radiation, who can communicate with other second-level repeaters. Through such a hierarchically organized relay network, a signal can be transmitted from a hollow area to a distant place, just like what is shown in Fig. 15. The mountains narrow the range of radiation, so we must use more repeaters in mountainous area than flat area and this make arrangement of PL tones difficult. Considering the mountain between first-level repeaters can avoid the interference, they can share the same tone and the same transmitter frequency. If a first-level repeater can be covered by two second-level repeaters, it chooses the nearest repeater to send signals. So that a second-level repeater may receive signals from several first-level repeaters simultaneously, and the signals transmitted to several first-level repeaters can pass through a second-level repeater. We set all the first-level repeaters covered by one second-level repeater share the same transmitter frequency, and share the PL same tone with the second-level repeater. In this way, we reduce the number of PL tones. We only need to distribute PL tones to secondary repeaters using the same way in the flat area. Then we set the receiver frequency of a first-level repeater being equal to the transmitter frequency of the corresponding second-level repeater, and set the transmitter frequency of a first-level repeater being equal to the receiver frequency of the corresponding second-level repeater.

<!-- b001719 | furniture | pages [36] -->


<!-- b001720 | furniture | pages [36] -->


<!-- b001721 | furniture | pages [36] -->


<!-- b001722 | furniture | pages [36] -->


<!-- b001723 | furniture | pages [36] -->


<!-- b001724 | furniture | pages [36] -->


<!-- b001725 | furniture | pages [36] -->


<!-- b001726 | furniture | pages [36] -->


<!-- b001727 | furniture | pages [36] -->


<!-- b001728 | furniture | pages [36] -->


<!-- b001729 | furniture | pages [36] -->


<!-- b001730 | furniture | pages [36] -->


<!-- b001731 | furniture | pages [36] -->


<!-- b001732 | furniture | pages [36] -->


<!-- b001733 | furniture | pages [36] -->


<!-- b001734 | furniture | pages [36] -->


<!-- b001735 | furniture | pages [37] -->
Team #9440              Page  36 / 40

<!-- b001736 | heading | pages [37] -->
8 Conclusion and Discussion

<!-- b001737 | prose | pages [37] -->
In this paper, we propose a two-tiered network model, where lower-power users can communicate with one another through repeaters. The capacity limitation and interference have been taken into consideration in our model. Motivated by the structure of cellular networks, we give a naïve solution where the number of repeaters and their positions can be obtained analytically. We further propose an iterative extremal optimization algorithm based on the Voronoi diagram. The proposed algorithm outperforms the naïve solution. For the case of 1000 users, it obtains a solution with 11 repeaters, which has been proved to be the real optimum. For the case of 10000 users, it obtains a solution with 104 repeaters, better than the naïve solution with 108 repeaters. Moreover, we proposed an algorithm based on maximum and minimum spanning tree to assign frequencies and private line tones. This algorithm does not introduce any new repeaters yet can largely broaden the reachable areas of users. For example, in the case of 10000 users, given a user, the probability this user can successfully send signal to a random position in the considered area is about 97.12%.

<!-- b001738 | prose | pages [37] -->
Compared with the related model for sensor wireless networks and mobile communication networks, our model is more general. The proposed algorithm is very effective and efficient: it runs much faster than the simulated annealing approach [12] and is of higher ability to escape the local optimum than another iterative refinement algorithm [22]. Concepts and methods from disparate scientific domains are well integrated in this algorithm, such as the extremal optimization from statistical physics community, the Voronoi diagram from geographic information science, and iterative refinement framework from computer science. Another advantage of the algorithm is that it can be widely applied since it does not require any specific geographical features of the considered area, while many efficient circle-covering algorithms only work well for squares.

<!-- b001739 | prose | pages [37] -->
There are also two considerable weaknesses in this work. Firstly, we have not developed an effective algorithm to satisfy the constrain of global reachability without adding too many repeaters. Secondly, our model is largely simplified, which have not taken into account the heterogeneity of users and repeaters, or the wave reflection and refraction by atmosphere.

<!-- b001740 | furniture | pages [37] -->


<!-- b001741 | furniture | pages [37] -->


<!-- b001742 | furniture | pages [37] -->


<!-- b001743 | furniture | pages [37] -->


<!-- b001744 | furniture | pages [37] -->


<!-- b001745 | furniture | pages [37] -->


<!-- b001746 | furniture | pages [37] -->


<!-- b001747 | furniture | pages [37] -->


<!-- b001748 | furniture | pages [37] -->


<!-- b001749 | furniture | pages [37] -->


<!-- b001750 | furniture | pages [37] -->


<!-- b001751 | furniture | pages [37] -->


<!-- b001752 | furniture | pages [37] -->


<!-- b001753 | furniture | pages [37] -->


<!-- b001754 | furniture | pages [37] -->


<!-- b001755 | furniture | pages [37] -->


<!-- b001756 | furniture | pages [38] -->
Team #9440              Page  37 / 40

<!-- b001757 | heading | pages [38] -->
Appendix A  Table of Parameters

<!-- b001758 | prose | pages [38] -->
For convenience, here we list parameters used in this paper. The detailed definitions can be found in the main content. The values of the parameters, expect for those free parameters, are also presented in this Table. Some values are given in the contest problem itself or directly obtained from literatures, while others are calculated according to our model. Details can be found in the main content.

<!-- b001759 | furniture | pages [38] -->


<!-- b001760 | caption | pages [38] -->
Table 9: Parameters appeared in this paper.

<!-- b001761 | prose | pages [38] -->
Parameter Brief Description  Value/Range Radius of the considered circular area 40 miles

<!-- b001762 | prose | pages [38] -->
Number of users need to be accommodated N Tunable parameter. Two cases,

<!-- b001763 | prose | pages [38] -->
N=1000 and N=10000, are

<!-- b001764 | prose | pages [38] -->
emphasized in this paper

<!-- b001765 | prose | pages [38] -->
Receiver frequency of a repeater fr  [145MHz,148MHz]

<!-- b001766 | furniture | pages [38] -->


<!-- b001767 | prose | pages [38] -->
Transmitter frequency of a repeater ft  [145MHz,148MHz]

<!-- b001768 | furniture | pages [38] -->


<!-- b001769 | prose | pages [38] -->
Specific PL tone of a repeater nPL  {1,2,...,54}

<!-- b001770 | furniture | pages [38] -->


<!-- b001771 | prose | pages [38] -->
Total number of available PL tones NPL 54

<!-- b001772 | prose | pages [38] -->
Communication radius of a repeater R 85.45 miles

<!-- b001773 | prose | pages [38] -->
Threshold of the frequency difference, below fc

<!-- b001774 | prose | pages [38] -->
0.6MHz

<!-- b001775 | prose | pages [38] -->
which interference may happen

<!-- b001776 | prose | pages [38] -->
Maximal distance for a user to send signals to a r

<!-- b001777 | prose | pages [38] -->
repeater

<!-- b001778 | prose | pages [38] -->
C Capacity of a repeater

<!-- b001779 | prose | pages [38] -->
15.28 miles

<!-- b001780 | prose | pages [38] -->
119 users

<!-- b001781 | prose | pages [38] -->
Tolerant capacity of a repeater C’ 99 users

<!-- b001782 | prose | pages [38] -->
Loss of feed system for transmitter L

<!-- b001783 | furniture | pages [38] -->


<!-- b001784 | prose | pages [38] -->
f out , 2dB

<!-- b001785 | prose | pages [38] -->
Loss of feed system for receiver L

<!-- b001786 | furniture | pages [38] -->


<!-- b001787 | prose | pages [38] -->
f in , 2dB

<!-- b001788 | prose | pages [38] -->
Other loss of the transmitter L

<!-- b001789 | furniture | pages [38] -->


<!-- b001790 | prose | pages [38] -->
b out , 1dB

<!-- b001791 | prose | pages [38] -->
Other loss of the receiver L

<!-- b001792 | furniture | pages [38] -->


<!-- b001793 | prose | pages [38] -->
b in , 1dB

<!-- b001794 | prose | pages [38] -->
Antenna gain of the transmitter G

<!-- b001795 | furniture | pages [38] -->


<!-- b001796 | prose | pages [38] -->
out 39dB

<!-- b001797 | prose | pages [38] -->
Antenna gain of the receiver G in 39dB

<!-- b001798 | prose | pages [38] -->
Effective radiated power of a repeater P

<!-- b001799 | furniture | pages [38] -->


<!-- b001800 | prose | pages [38] -->
,r out 100W

<!-- b001801 | prose | pages [38] -->
Actual power of received signal for a repeater P

<!-- b001802 | furniture | pages [38] -->


<!-- b001803 | prose | pages [38] -->
,r in

<!-- b001804 | furniture | pages [38] -->


<!-- b001805 | prose | pages [38] -->
 

<!-- b001806 | heading | pages [38] -->
1 W

<!-- b001807 | furniture | pages [38] -->


<!-- b001808 | furniture | pages [39] -->
Team #9440              Page  38 / 40

<!-- b001809 | prose | pages [39] -->
Effective radiated power of a user P

<!-- b001810 | furniture | pages [39] -->


<!-- b001811 | prose | pages [39] -->
u out , 3.2W

<!-- b001812 | prose | pages [39] -->
Actual power of received signal for a user P

<!-- b001813 | furniture | pages [39] -->


<!-- b001814 | prose | pages [39] -->
u in ,  

<!-- b001815 | heading | pages [39] -->
1 W

<!-- b001816 | furniture | pages [39] -->


<!-- b001817 | prose | pages [39] -->
Bit energy-to-noise density ratio E N b 0

<!-- b001818 | prose | pages [39] -->
V Voice gain 

<!-- b001819 | prose | pages [39] -->
18dB for transceiver, and always in the range 5-30dB

<!-- b001820 | prose | pages [39] -->
0.4dB The information bit rate bps

<!-- b001821 | prose | pages [39] -->
Threshold to judge whether the iterative 

<!-- b001822 | prose | pages [39] -->
0.01miles

<!-- b001823 | prose | pages [39] -->
refinement is converged

<!-- b001824 | prose | pages [39] -->
Threshold to judge whether we should stop the Tc

<!-- b001825 | prose | pages [39] -->
100

<!-- b001826 | prose | pages [39] -->
extremal optimization operation

<!-- b001827 | furniture | pages [39] -->


<!-- b001828 | heading | pages [39] -->
Appendix B  Table of Symbols

<!-- b001829 | prose | pages [39] -->
For convenience, here we list mathematical used in this paper. The detailed definitions can be found in the main content.

<!-- b001830 | furniture | pages [39] -->


<!-- b001831 | caption | pages [39] -->
Table 10: Mathematical symbols appeared in this paper.

<!-- b001832 | heading | pages [39] -->
Symbol

<!-- b001833 | prose | pages [39] -->
 Description The circular area described in the problem D A two-tiered directed network

<!-- b001834 | prose | pages [39] -->
Interference from other repeaters I

<!-- b001835 | furniture | pages [39] -->


<!-- b001836 | prose | pages [39] -->
other

<!-- b001837 | prose | pages [39] -->
Interference from itself I

<!-- b001838 | furniture | pages [39] -->


<!-- b001839 | prose | pages [39] -->
self

<!-- b001840 | prose | pages [39] -->
The set of users V u

<!-- b001841 | prose | pages [39] -->
The set of users V '

<!-- b001842 | furniture | pages [39] -->


<!-- b001843 | prose | pages [39] -->
u

<!-- b001844 | prose | pages [39] -->
The set of repeaters V r

<!-- b001845 | prose | pages [39] -->
Signal-to-noise ratio SNR

<!-- b001846 | prose | pages [39] -->
The set of directed links from users to repeaters E

<!-- b001847 | furniture | pages [39] -->


<!-- b001848 | prose | pages [39] -->
ur

<!-- b001849 | prose | pages [39] -->
The set of directed links from repeaters to repeaters E rr

<!-- b001850 | prose | pages [39] -->
iu

<!-- b001851 | prose | pages [39] -->
ir

<!-- b001852 | prose | pages [39] -->
S ( ) r

<!-- b001853 | prose | pages [39] -->
A user

<!-- b001854 | prose | pages [39] -->
A repeater

<!-- b001855 | prose | pages [39] -->
jr The Voronoi area of a repeater

<!-- b001856 | furniture | pages [39] -->


<!-- b001857 | prose | pages [39] -->
V j

<!-- b001858 | furniture | pages [39] -->


<!-- b001859 | furniture | pages [40] -->
Team #9440              Page  39 / 40

<!-- b001860 | prose | pages [40] -->
S u ( ) iu

<!-- b001861 | furniture | pages [40] -->


<!-- b001862 | prose | pages [40] -->
The reachable area of a user r i

<!-- b001863 | prose | pages [40] -->
R u ( ) iu

<!-- b001864 | furniture | pages [40] -->


<!-- b001865 | prose | pages [40] -->
The reachable repeaters of a user r i

<!-- b001866 | prose | pages [40] -->
 Density of users

<!-- b001867 | prose | pages [40] -->
M Number of repeaters

<!-- b001868 | prose | pages [40] -->
B Bandwidth

<!-- b001869 | prose | pages [40] -->
Pur Power of signal from a user to a repeater

<!-- b001870 | prose | pages [40] -->
T The minimal spanning tree

<!-- b001871 | prose | pages [40] -->
T’ The maximum spanning tree

<!-- b001872 | furniture | pages [40] -->


<!-- b001873 | heading | pages [40] -->
Appendix C  Summary of Assumptions

<!-- b001874 | prose | pages [40] -->
For convenience, here we summary all the important assumptions made for our model. Notice that, these assumptions also appeared in the model description of the main content.

<!-- b001875 | prose | pages [40] -->
[A1]. Users are uniformly distributed in the considered area, and in a more strong assumption, we consider the number of users as a real variable and the user density in the considered area is a constant.

<!-- b001876 | prose | pages [40] -->
[A2]. Users prefer to communicate with the nearest repeaters. [A3]. Considering two repeaters sharing the same PL tone and the difference between their transmitter frequencies is less than a threshold fc=0.6MHz. If the distance between them is less than 2R, they will interfere with each other.

<!-- b001877 | prose | pages [40] -->
[A4]. The considered circular area is a place where wireless signals can fade freely, which means there are not any other sorts of interference such as fogs, rivers, hills, buildings, activities of sun and so forth, so the fading of signals under such situation is only due to the distance across.

<!-- b001878 | prose | pages [40] -->
[A5]. There is no background noise in this system. [A6]. Repeaters don’t have noisy impact on others. [A7]. Functionalities and specifications of users’ radios are the same (i.e., homogeneous users’ radios). Functionalities and specifications of radio repeaters are the same (i.e., homogeneous repeaters).

<!-- b001879 | heading | pages [40] -->
References

<!-- b001880 | references | pages [40] -->
[1] K. T. Phan et al., Power Allocation in Wireless Multi-User Relay Networks, IEEE Trans.

<!-- b001881 | references | pages [40] -->
Wireless Commun. 8 (2009) 2535.

<!-- b001882 | references | pages [40] -->
[2] W. Shi, S. Roy, Achieving Full Diversity by Selection in Arbitrary Multi-hop

<!-- b001883 | references | pages [40] -->
Amplify-and-Forward Relay Networks, GLOBECOM 2009, IEEE Press.

<!-- b001884 | references | pages [40] -->
[3] T. C.-K. Liu et al., Adaptive Power Allocation for Bidirectional Amplify-and-Forward

<!-- b001885 | references | pages [40] -->
Multiple-Relay Multiple-User Networks, GLOBECOM 2010, IEEE Press.

<!-- b001886 | references | pages [40] -->
[4] A. Nosratinia, T. E. Hunter, A. Hedayat, Cooperative Communication in Wireless Networks,

<!-- b001887 | references | pages [40] -->
IEEE Commun. Magazine 3 (2004) 74.

<!-- b001888 | references | pages [40] -->
[5] http://en.wikipedia.org/wiki/Amateur_radio

<!-- b001889 | references | pages [40] -->
[6] I. F. Akyildiz, W. Su, Y. Sankarasubramaniam, E. Cayirci, Wireless sensor networks: a survey,

<!-- b001890 | references | pages [40] -->
Comput. Netw. J. 38 (2002) 393.

<!-- b001891 | references | pages [40] -->
[7] J. Pan, Y. T. Hou, L. Cai, Y. Shi, S. X. Shen, Topology control for wireless sensor networks,

<!-- b001892 | furniture | pages [40] -->


<!-- b001893 | furniture | pages [41] -->
Team #9440              Page  40 / 40

<!-- b001894 | references | pages [41] -->
MOBICOM 2003, ACM Press.

<!-- b001895 | references | pages [41] -->
[8] G. Gupta, M. Younis, Fault-tolerant clustering of wireless sensor networks, WCNC 2003, IEEE

<!-- b001896 | references | pages [41] -->
Press.

<!-- b001897 | references | pages [41] -->
[9] G. Gupta, M. Younis, Load-balanced clustering of wireless sensor networks, WCNC 2003,

<!-- b001898 | references | pages [41] -->
IEEE Press.

<!-- b001899 | references | pages [41] -->
[10] J. Tang, B. Hao, A. Sen, Relay node placement in large scale wireless sensor networks,

<!-- b001900 | references | pages [41] -->
Comput. Commun. 29 (2006) 490.

<!-- b001901 | references | pages [41] -->
[11] R. J. Fowler, M. S. Paterson, S. L. Tanimoto, Optimal packing and covering in the plane are

<!-- b001902 | references | pages [41] -->
NP-complete, Information Processing Letter 12 (1981) 133.

<!-- b001903 | references | pages [41] -->
[12] K. J. Nurmela, P. R. J. Ostergard, Covering a square with up to 30 Equal Circles, Research

<!-- b001904 | references | pages [41] -->
Report HUT-TCS-A62, Laboratory for Theoretical Computer Science, Helsinky University of

<!-- b001905 | references | pages [41] -->
Technology, 2000.

<!-- b001906 | references | pages [41] -->
[13] F. Aurenhammer, Voronoi Diagrams - A Survey of a Fundamental Geometric Data Structure,

<!-- b001907 | references | pages [41] -->
ACM Computing Surveys 23 (1991) 345.

<!-- b001908 | references | pages [41] -->
[14] http://en.wikipedia.org/wiki/Circumcircle

<!-- b001909 | references | pages [41] -->
[15] S. Boettcher, A. G. Percus, Optimization with Extremal Dynamics, Phys. Rev. Lett. 86 (2001)

<!-- b001910 | references | pages [41] -->
5211.

<!-- b001911 | references | pages [41] -->
[16] T. Zhou, W.-J. Bai, L.-J. Cheng, B.-H. Wang, Continuous extremal optimization for

<!-- b001912 | references | pages [41] -->
Lennard-Jones Clusters, Phys. Rev. E 72 (2005) 016702.

<!-- b001913 | references | pages [41] -->
[17] C. A. Balanis, Antenna Theory: Analysis and Design (3rd Edition), John Wiley &. Sons, 2005.

<!-- b001914 | references | pages [41] -->
[18] K. S. Gilhousen et al., On the Capacity of a Cellular CDMA System, IEEE Trans. Vehicular

<!-- b001915 | references | pages [41] -->
Technology 40 (1991) 303.

<!-- b001916 | references | pages [41] -->
[19] N. Megiddo, Linear-time algorithms for linear programming in R3 and related problems,

<!-- b001917 | references | pages [41] -->
SIAM J. Comput. 12 (1983) 759.

<!-- b001918 | references | pages [41] -->
[20] P. Bak, K. Sneppen, Punctuated equilibrium and criticality in a simple model of evolution,

<!-- b001919 | references | pages [41] -->
Phys. Rev. Lett. 71 (1993) 4083.

<!-- b001920 | references | pages [41] -->
[21] G. F. Toth, Thinnest Covering of a Circle by Eight, Nine, or Ten Congruent Circles,

<!-- b001921 | references | pages [41] -->
Combinatorial &. Computational Geometry 52 (2005) 361.

<!-- b001922 | references | pages [41] -->
[22] G. K. Das, S. Das, S. C. Nandy, B. P. Sinha, Efficient algorithm for placing a given number of

<!-- b001923 | references | pages [41] -->
base stations to cover a convex region, J. Parallel &. Distributed Comput. 66 (2006) 1353.

<!-- b001924 | furniture | pages [41] -->

