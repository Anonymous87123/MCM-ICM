# P-B-2017-56731-a60a9459

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For office use only

<!-- b000003 | prose | pages [1] -->
For office use only

<!-- b000004 | prose | pages [1] -->
56731

<!-- b000005 | prose | pages [1] -->
T1 ________________

<!-- b000006 | prose | pages [1] -->
F1 ________________

<!-- b000007 | furniture | pages [1] -->


<!-- b000008 | prose | pages [1] -->
T2 ________________

<!-- b000009 | prose | pages [1] -->
F2 ________________

<!-- b000010 | prose | pages [1] -->
Problem Chosen

<!-- b000011 | prose | pages [1] -->
T3 ________________

<!-- b000012 | prose | pages [1] -->
F3 ________________

<!-- b000013 | title | pages [1] -->
B

<!-- b000014 | prose | pages [1] -->
T4 ________________

<!-- b000015 | prose | pages [1] -->
F4 ________________

<!-- b000016 | furniture | pages [1] -->


<!-- b000017 | furniture | pages [1] -->


<!-- b000018 | prose | pages [1] -->
2017 MCM/ICM

<!-- b000019 | heading | pages [1] -->
Summary Sheet

<!-- b000020 | prose | pages [1] -->
(Your team's summary should be included as the first page of your electronic submission.) Type a summary of your results on this page. Do not include the name of your school, advisor, or team members on this

<!-- b000021 | prose | pages [1] -->
page.

<!-- b000022 | prose | pages [1] -->
A New Type of Toll Plaza Based on Bionics-Honeycomb

<!-- b000023 | heading | pages [1] -->
Summary

<!-- b000024 | prose | pages [1] -->
In this paper, we analyze the performance of commonly used toll plaza based on our proposed mathematical model. A new improved toll plaza is proposed to reduce the cost, decrease the probability of collision at the merging point and increase the throughput.

<!-- b000025 | prose | pages [1] -->
The distribution of our proposed tollbooths resembles the honeycomb. At the center of each regular hexagonal honeycomb, there are two tollbooths, which serve two separated vehicle streams. The vehicles in these two separated streams are merged in advance before they continue their journey on the highway. Due to the specific pattern of the new toll plaza, the total area can be reduced significantly. Meanwhile, the average wasted time caused by queuing can be diminished, which means that the throughput will be raised.  Additionally, by splitting the merging procedure into two stages, the possibility of accidents can also be decreased.

<!-- b000026 | prose | pages [1] -->
The main contributions of this paper are as follows: (1) The new designed cellular architecture can greatly reduce the construction area compared with traditional linear distributed toll gates.

<!-- b000027 | title | pages [1] -->
(2) We analyze the throughput of toll plazas by means of the queuing theory. To verify our theory,

<!-- b000028 | prose | pages [1] -->
we simulate the behavior of the large number of vehicles passing the toll plaza with the help of PTV- VISSIM. Simulation results show that the ideal cellular distributed toll booths have better results compared with traditional toll stations, especially when the traffic flow is heavy, the average travel time reduced by about 55% and the average delay time of each lane is reduced by about 70%.

<!-- b000029 | prose | pages [1] -->
(3) We analyze the influence of the proportions of different types of tollbooths to our design. According to relevant documents, the impact of exact-change tollbooths is similar to manual tollbooths, so we only consider two kinds of tollbooths: human-staffed tollbooths and E-ZPass tollbooths. PTV-VISSIM simulation results show that full ETC tollbooth is 8 times faster than full MTC tollbooth.

<!-- b000030 | prose | pages [1] -->
(4) We simulate the performance of the cellular toll plaza under different traffic throughput. Simulation results show that the average transit time remains at about 11 seconds under different throughputs from 0 to 2000 (Unit: veh / h). We can infer that this model is not sensitive to traffic flow variations and has strong robustness which is suitable for practical construction.

<!-- b000031 | prose | pages [1] -->
(5) To further reduce the possibility of accident, we improve the cellular tollbooth concept model: make the transition zone more smooth and arrange different kinds of tollbooths more equitable.

<!-- b000032 | prose | pages [1] -->
(6) For self-driving vehicles, in the center of the toll plaza, we reserve special E-ZPass tollbooths, which match the characteristics of autonomous vehicles: safer and faster.

<!-- b000033 | prose | pages [1] -->
Electronic toll collection and autonomous vehicles are the trends of modern transportation, our new designed model can improve the performance of toll plaza in the aspects of cost, throughput and accident prevention.

<!-- b000034 | furniture | pages [2] -->
Team # 56731                                                                                                                                                 Page 2 of 22

<!-- b000035 | heading | pages [2] -->
I. Introduction

<!-- b000036 | heading | pages [2] -->
1.1 Problem Background

<!-- b000037 | prose | pages [2] -->
With the number of vehicles increasing, expressway is confronted with great traffic pressure, especially at the toll plaza. The congestion problem at the toll station becomes more and more serious due to the outdated design. Related research found that 36% of the total travel time in China is delay time caused by tolling [1]. In addition, as a vehicle-intensive place, toll plaza has become an accident-prone section because of the drivers' improper operation [2].

<!-- b000038 | prose | pages [2] -->
With the widespread use of Electronic Toll Collection (ETC) and E-ZPass, the efficiency of toll collection has been improved significantly and further the congestion at the toll plaza is released. However, due to the high speed of the vehicles passing through the toll plaza, the probability of collision in the merging zone is increased. Moreover, the construction of future toll plaza is very expensive. Considering above factors, it is necessary to design new toll plaza to improve its throughput, reduce the cost of construction and decrease the possibility of collision in the merging zone.

<!-- b000039 | prose | pages [2] -->
In this paper, we design a toll station model based on bionics-honeycomb as shown in

<!-- b000040 | caption | pages [2] -->
Figure 1.1. The hexagonal tiling creates a partition with equal-sized cells, while minimizing

<!-- b000041 | prose | pages [2] -->
the total perimeter of the cells. Known in geometry as the honeycomb conjecture, this was given by Jan Brożek and proved much later by Thomas Hales [3]. Cellular Structure is widely used in many aspects of life. For example, the base stations of mobile communications are distributed like the honeycomb. In our new designed toll plaza model, the tollbooths are located in the center of each regular hexagonal.

<!-- b000042 | furniture | pages [2] -->


<!-- b000043 | caption | pages [2] -->
Figure 1.1 Honeycomb

<!-- b000044 | heading | pages [2] -->
1.2 Notations Description

<!-- b000045 | furniture | pages [2] -->


<!-- b000046 | prose | pages [2] -->
Total time cost: The average time interval for a vehicle from the beginning point of the detection area to the ending point of the detection area is the total time cost.

<!-- b000047 | prose | pages [2] -->
Theoretical time cost:  If there is only one vehicle in the system and that vehicle is not limited by the control signal, the time interval for that vehicle from the beginning point of the detection area to the ending point of the detection area is the theoretical time cost.

<!-- b000048 | prose | pages [2] -->
Time delayed: The difference between the total time cost and the theoretical time cost is the Time delayed.

<!-- b000049 | prose | pages [2] -->
L: the number of lanes in each direction of the highway. B: the total number of tollbooths in each direction.

<!-- b000050 | furniture | pages [2] -->


<!-- b000051 | heading | pages [2] -->
1.3 Our Work

<!-- b000052 | prose | pages [2] -->
With the popularization of ETC equipment and autonomous vehicles, the MTC lanes will be totally replaced by the ETC lanes in the next 20 years, which will increase the road capacity and decrease the time cost by each car passing through the toll station.

<!-- b000053 | prose | pages [2] -->
At present the traditional design of toll stations covers a large area, and the cost of construction is high. With the raise of the vehicles' speed, there will be congestions at the merging point, which may increase the possibility of accident.

<!-- b000054 | prose | pages [2] -->
① We designed a cellular toll booth model, designed its shape, size and merge. In order

<!-- b000055 | furniture | pages [3] -->
Team # 56731                                                                                                                                                 Page 3 of 22

<!-- b000056 | prose | pages [3] -->
to make the cellular toll booth more adaptable to practical application, we escalated from the aspects of the area, the throughput, the accident prevention, the hybrid lane and the only ETC lane, self-driving vehicle and so on. ② Through the analysis of the toll station area model, we quantified how much we could

<!-- b000057 | prose | pages [3] -->
reduce the toll station area. ③  We use the VISSIM to simulate whether the cellular toll station can gather and

<!-- b000058 | prose | pages [3] -->
distribute traffic in batches, and reduce the average travel time and average delay time of vehicle merging. ④ We use the VISSIM to analyze the traffic capacity of the cellular toll station in the

<!-- b000059 | prose | pages [3] -->
mixed (artificial charge, ETC, change) lane, pure ETC-type toll lane, both for heavy traffic flow and light flow. ⑤ We improved our design from 3 different aspects. ⑥ We analyzed the influence of the traffic flow to the capacity of the toll station. ⑦ We analyzed whether the toll station can meet the need of the autonomous vehicles.

<!-- b000060 | furniture | pages [3] -->


<!-- b000061 | caption | pages [3] -->
Figure 1.2 Design evolution diagram

<!-- b000062 | furniture | pages [3] -->


<!-- b000063 | heading | pages [3] -->
II. General Assumption

<!-- b000064 | prose | pages [3] -->
 The arrival of vehicles obeys the Poisson distribution;  In general, the traffic of ETC toll stations should be much heavier than the traffic of other

<!-- b000065 | prose | pages [3] -->
types of toll station.  All toll stations are ETC or E-ZPass unless otherwise specified.  There is no ramp or other exits near the tollbooth. We do not consider the possibility of

<!-- b000066 | prose | pages [3] -->
additional vehicle access, only consider the vehicles already on the main road.  The service procedure of the toll stations and the merging procedure of the vehicles after

<!-- b000067 | prose | pages [3] -->
the tollbooths are both queuing system. They follow the principle of first come first served.

<!-- b000068 | heading | pages [3] -->
III. Design Scheme of Honeycomb-like Toll plaza

<!-- b000069 | prose | pages [3] -->
In traditional toll plazas, there are always more tollbooths than the incoming lanes of traffic. A toll plaza consists of the fan-out area before the barrier toll, the toll barrier itself, and the fan-

<!-- b000070 | furniture | pages [4] -->
Team # 56731                                                                                                                                                 Page 4 of 22

<!-- b000071 | prose | pages [4] -->
in area after the toll barrier. The toll barriers are often constructed in a straight line placed across the highway, perpendicular to the direction of traffic flow. So the area of toll plaza is pretty large. To reduce the area of the toll plaza and further save the construction cost, we design a new toll plaza based on the structure of the honeycomb. In addition, by splitting the merging procedure into two stages, our new designed toll plaza can reduce the probability of collision, in contrast with the traditional emerging procedure, where large number of vehicles concentrate into the highway simultaneously. The evolution of our design is shown in Figure 3.1, where we smooth the transition zone to avoid sharp turn and add some reserved tollbooths in the middle for autonomous vehicles.

<!-- b000072 | furniture | pages [4] -->


<!-- b000073 | furniture | pages [4] -->


<!-- b000074 | caption | pages [4] -->
Figure 3.1 Evolutionary process

<!-- b000075 | heading | pages [4] -->
IV. Model Design

<!-- b000076 | heading | pages [4] -->
4.1 Estimated Cost of the Toll Plaza

<!-- b000077 | prose | pages [4] -->
The cost of building a toll station mainly includes the construction cost of the road surface and the construction cost of the toll booth. We assess its area and try to minimize it. Toll booths total area S can be divided into the area of the transition zone and the area of toll gates.

<!-- b000078 | prose | pages [4] -->
We assume that the number of the toll gates is nt,the number of the lanes of the highway is nl, the width of the lane is wl, the tangential offset width is wo, the design speed is v, the length of the transition zone is lt, the width of the toll gates is wt, the area of the traditional toll station are ST1  and SC1 ,respectively, the area of the transition zone are ST2  and SC2 , respectively.

<!-- b000079 | furniture | pages [4] -->


<!-- b000080 | furniture | pages [5] -->
Team # 56731                                                                                                                                                 Page 5 of 22

<!-- b000081 | furniture | pages [5] -->


<!-- b000082 | caption | pages [5] -->
Figure 4.1 Symbol explanation

<!-- b000083 | furniture | pages [5] -->


<!-- b000084 | heading | pages [5] -->
4.1.1 Comparison of the Area of the Charging Zone

<!-- b000085 | prose | pages [5] -->
The area of the traditional toll station:

<!-- b000086 | prose | pages [5] -->
𝑆𝑇1 = 2𝑙𝑡𝑛𝑙(𝑤𝑡+ 𝑤𝑙) The area of the cellular toll station:

<!-- b000087 | prose | pages [5] -->
𝑆𝐶1 = 𝑛𝑙

<!-- b000088 | prose | pages [5] -->
2 (𝑙𝑡(𝑤𝑡+ 2𝑤𝑙) + 𝑤𝑙𝑙𝑡)

<!-- b000089 | prose | pages [5] -->
The difference in the area of the charging zone:

<!-- b000090 | prose | pages [5] -->
2 𝑤𝑡𝑙𝑡𝑛𝑙+ 3

<!-- b000091 | prose | pages [5] -->
𝛥𝑆1 = 𝑆𝑇1 −𝑆𝐶1 = 1

<!-- b000092 | prose | pages [5] -->
2 𝑤𝑙𝑙𝑡𝑛𝑙> 0

<!-- b000093 | heading | pages [5] -->
4.1.2 Comparison of the Area of the Transition Zone

<!-- b000094 | prose | pages [5] -->
The area of the traditional toll station:

<!-- b000095 | prose | pages [5] -->
𝑤𝑜= 𝑛𝑡(𝑤𝑙+ 𝑤𝑡) −𝑛𝑙𝑤𝑙

<!-- b000096 | prose | pages [5] -->
𝑤𝑜𝑣2

<!-- b000097 | prose | pages [5] -->
= 𝑣2

<!-- b000098 | prose | pages [5] -->
60 (𝑛𝑡𝑤𝑙+ 𝑛𝑡𝑤𝑡−𝑛𝑙𝑤𝑙)

<!-- b000099 | prose | pages [5] -->
𝑙𝑡=

<!-- b000100 | prose | pages [5] -->
60

<!-- b000101 | prose | pages [5] -->
𝑣2

<!-- b000102 | prose | pages [5] -->
1

<!-- b000103 | prose | pages [5] -->
2 + 𝑛𝑡 2 + 2𝑛𝑡 2𝑤𝑙 2𝑤𝑡 2𝑤𝑙𝑤𝑡−𝑛𝑙 2𝑤𝑙 2) 120 (𝑛𝑡

<!-- b000104 | prose | pages [5] -->
2 (𝑛𝑡(𝑤𝑙+ 𝑤𝑡) + 𝑛𝑙𝑤𝑙)𝑙𝑡=

<!-- b000105 | prose | pages [5] -->
𝑆𝑇2 =

<!-- b000106 | prose | pages [5] -->
The area of the cellular toll station:

<!-- b000107 | prose | pages [5] -->
2 −𝑛𝑙) ⋅𝑤𝑙

<!-- b000108 | prose | pages [5] -->
𝑤𝑜= (𝑛𝑡

<!-- b000109 | prose | pages [5] -->
𝑤𝑜𝑣2

<!-- b000110 | prose | pages [5] -->
1

<!-- b000111 | prose | pages [5] -->
2

<!-- b000112 | prose | pages [5] -->
𝑛𝑡 60 𝑤𝑙𝑣2 (

<!-- b000113 | prose | pages [5] -->
𝑙𝑡=

<!-- b000114 | prose | pages [5] -->
= 60

<!-- b000115 | prose | pages [5] -->
1

<!-- b000116 | prose | pages [5] -->
𝑛𝑡

<!-- b000117 | prose | pages [5] -->
𝑆𝐶2 =

<!-- b000118 | prose | pages [5] -->
2 (

<!-- b000119 | prose | pages [5] -->
2 + 𝑛𝑙) 𝑤𝑙𝑙𝑡=

<!-- b000120 | prose | pages [5] -->
The difference in the transition zone:

<!-- b000121 | prose | pages [5] -->
𝛥𝑆2 = 𝑆𝑇2 −𝑆𝐶2 = 𝑣2

<!-- b000122 | prose | pages [5] -->
120 (3

<!-- b000123 | prose | pages [5] -->
2 −𝑛𝑙)

<!-- b000124 | prose | pages [5] -->
2

<!-- b000125 | prose | pages [5] -->
1

<!-- b000126 | prose | pages [5] -->
𝑛𝑡

<!-- b000127 | prose | pages [5] -->
2) 𝑤𝑙 2𝑣2

<!-- b000128 | prose | pages [5] -->
120 (

<!-- b000129 | prose | pages [5] -->
4 −𝑛𝑙

<!-- b000130 | prose | pages [5] -->
4 𝑛𝑡2𝑤𝑙2 + 𝑛𝑡2𝑤𝑡2 + 2𝑛𝑡2𝑤𝑙𝑤𝑡) > 0

<!-- b000131 | heading | pages [5] -->
4.1.3 Comparison of the Total Area

<!-- b000132 | prose | pages [5] -->
From the equations above, we can learn that the cellular toll station can significantly save space compared with traditional toll station. The effect can be seen in Figure 4.2 intuitively.

<!-- b000133 | furniture | pages [6] -->
Team # 56731                                                                                                                                                 Page 6 of 22

<!-- b000134 | furniture | pages [6] -->


<!-- b000135 | caption | pages [6] -->
Figure 4.2 Area comparison

<!-- b000136 | heading | pages [6] -->
4.2 Analyzation of the Throughput of Toll Plazas

<!-- b000137 | prose | pages [6] -->
In our model, we consider the entire process of tolling as the operation of two serially connected queuing systems. First, the process of vehicles passing through the toll booths and queuing in front of the toll booths is treated as a queuing system, and the process of vehicles passing through the merging points at the exit of the toll station as the second queuing system. Next, we will start from a briefly introduction to the queuing theory.

<!-- b000138 | heading | pages [6] -->
4.2.1 A Brief Introduction of the Queueing Model

<!-- b000139 | prose | pages [6] -->
Queueing theory is the mathematical study of waiting lines, or queues. In queueing theory, a model is constructed so that queue lengths and waiting time can be predicted. Queueing theory is generally considered a branch of operations research because the results are often used when making business decisions about the resources needed to provide a service [4].

<!-- b000140 | furniture | pages [6] -->


<!-- b000141 | furniture | pages [6] -->


<!-- b000142 | caption | pages [6] -->
Figure 4.3 Elements of a queueing model

<!-- b000143 | heading | pages [6] -->
4.2.2 Queueing System at Toll Collectors

<!-- b000144 | prose | pages [6] -->
In reality, when vehicles enter the toll station, the drivers will head to a toll gate according to certain principles, such as the distance to each toll gate, the number of vehicles waiting in the queue. But in our model, the arrival interval of vehicles at each toll gate follows exponential distribution. Meanwhile, the time cost by each vehicle in the toll gate also follows exponential distribution. In addition, it is clear that each toll gate can handle only one lane at each time, so that although toll booths have multiple toll booths, there is still only one set of toll collection facilities for each toll gate. Although in our model there are two toll gates at each toll island, this is not contrary to the aforementioned principles.

<!-- b000145 | prose | pages [6] -->
In summary, we believe that each toll gate can be considered as an M/M/1 queuing system.

<!-- b000146 | heading | pages [6] -->
4.2.3 Queueing System at Merging Points

<!-- b000147 | prose | pages [6] -->
Based on the Burke's theorem，If the arrival time and service time of a M/M/1 queuing model is a Poisson process with parameters λ, the departure process of the queuing model is also a Poisson process [5]. The output of the toll booth is a Poisson process; therefore, the arrival intervals of the merging points are also Poisson processes.

<!-- b000148 | prose | pages [6] -->
The existing road design guidelines stipulate that lane merging can only be started from

<!-- b000149 | furniture | pages [7] -->
Team # 56731                                                                                                                                                 Page 7 of 22

<!-- b000150 | prose | pages [7] -->
the right side of the vehicle's driving direction and only one lane can be merged at a time [6]. According to this provision, and also to simplify the model, we will divide the lanes into two types. Type I doesn’t pass through any merging point, but type II does. The number of type I equals to L-1, because there exists one lane, even it directly connects to the highway, but it needs to merge with all lanes at its right side, such as lane 4 in the figure 4.4.

<!-- b000151 | prose | pages [7] -->
For the type I lanes, the vehicles can directly drive pass through them, we consider the time cost equals to number of merging points multiplies the time cost passing each of them, that is, (𝐵−𝐿) × (1 𝜇0 ) = (𝐵−𝐿)/𝜇0 and (𝐵/2 −𝐿) × (1 𝜇0 ) = (𝐵−2𝐿)/2𝜇0, where B ⁄ ⁄ is the number of the toll gates, L is the number of the lanes of highway, μ0 is the service rate at a merging point when the merging conflict doesn’t occur. The total possibility of these lanes, for the traditional toll station is (L-1)/B, for our cellular toll station is (L-1)/(B/2).

<!-- b000152 | prose | pages [7] -->
For the type II lanes, the possibility of vehicles driving on these roads are (B-L+1)/B and (B-2L+2)/B, respectively. Besides, for the k-th merging point, the arrival possibility is the sum of the possibility of one lane plus the possibility of the (k-1)-th merging point, that is, (k+1)/B and 2(k+1)/B, respectively. Take the merging pattern shown in the figure 4.4 as the example, the possibility of the merging point 1 equals to lane 1 plus lane 2, that is, 1/B+1/B=2/B, and the merging point 2 equals to lane 3 plus merging point 1, that is, 1/B+2/B=3/B. As for the traffic flow, we can similarly obtain the value of merging point k, equals to (k+1)𝛷/B, where Φ is the total traffic flow.

<!-- b000153 | furniture | pages [7] -->


<!-- b000154 | furniture | pages [7] -->


<!-- b000155 | caption | pages [7] -->
Figure 4.4 Merging points at the transition zone

<!-- b000156 | furniture | pages [7] -->


<!-- b000157 | prose | pages [7] -->
To simplify the model, we don’t distinguish between two lanes which merges at the same merging point, that is, the time a vehicle passes through a single merging point is independent of the lane in which it is located, only in relation to the state of the other lane. If there is no vehicle on the other lane, or a vehicle on the other lane but it stops to avoid the merging conflict, this vehicle can complete the merging process without deceleration, we define the time cost at this process as 1/𝜇0. Otherwise, this vehicle needs to stop and wait, the time cost is defined as 1/𝜇1.

<!-- b000158 | prose | pages [7] -->
In summary, the arrival rate of the queueing system at merging points follows the exponential distribution (i.e. a Poisson process), but the service rate is a general function, therefore, that is a M/G/1 queueing model.

<!-- b000159 | heading | pages [7] -->
4.3 Calculation

<!-- b000160 | prose | pages [7] -->
From the previous section, we have obtained the queueing model corresponding to our design. Then, we will substitute the specific parameter to those formulas to calculate the average time cost passing through the traditional or the cellular toll station, and make comparison of their throughput.

<!-- b000161 | heading | pages [7] -->
4.3.1 Parameter Assignment

<!-- b000162 | prose | pages [7] -->
B: Number of tollbooths  In reality, the number of toll gates depends on the traffic flow, type of vehicles, etc. However, to simplify our model, we make it equals to 8. We need to notice that even there is

<!-- b000163 | furniture | pages [8] -->
Team # 56731                                                                                                                                                 Page 8 of 22

<!-- b000164 | prose | pages [8] -->
two toll gates at one toll island and we take the strategy of pre-merging to half the lanes after the entry of the toll station, but these won't affect the number of the toll gates, which is the maximum number of vehicle the toll station can serve at the same time.

<!-- b000165 | prose | pages [8] -->
L: Number of lanes of highway  Toll merging zone at the exit of the toll plaza is directly connected to the highway，to ensure the number of lanes of the highway is greater than that of the exit of the charging zone, we take 3 as the value of L.

<!-- b000166 | prose | pages [8] -->
μT: Service rate of a tollbooth  At present, the electronic toll system widely installed, to enable our system to adapt to future trends, we take its service rate as 1200 𝑣𝑒ℎ/ℎ[7].

<!-- b000167 | prose | pages [8] -->
μ0: The service rate at a merging point when the merging conflict doesn’t occur.  μ0 is the service rate when the merging conflict doesn’t occur, or occurs but the other vehicle stop and wait. Meanwhile, we also take it as the service rate when a vehicle directly heads for a lane of the highway without passing any merging point. The average speed of vehicles on the highway is 60mph [7], therefore the length of the merging point should be the length of a normal vehicle plus a safe distance, which is six times the length of a normal vehicle [7], thus the length of the merging point is 15ft + 6 × 15ft = 105ft. Then the average time for a vehicle passing a merging point equals to the length of it divided by the speed of the vehicle, which is 105ft ÷ 60mph = 1.1932s，take value of its reciprocal as the value of μ0 , and convert it to the one hour, we can derive 3600(s h ⁄ ) ÷ 1.1932s = 3017.1veh/h.

<!-- b000168 | prose | pages [8] -->
μ1: The service rate at a merging point when the merging conflict occurs.  Applied for the vehicle which parks to avoid the other vehicle when two vehicles reach the merging point at the same time. the avoiding car will park temporarily, and wait for the front car, then accelerate the vehicle and continue driving. When starting again, the vehicle will start at 0 m / s, and the vehicle safe distance is only one times the length of the vehicle [7]. According to the displacement formula s = 0.5𝑎𝑡2，we can derive the formula t = √2s a ⁄ ， and the average acceleration of the vehicle is 6.5ft/s2[1]，Substitute the parameters into the

<!-- b000169 | prose | pages [8] -->
formula, we can obtain the value √2(15𝑓𝑡+ 15𝑓𝑡) ÷ 6.5(𝑓𝑡/𝑠2) = 3.0382𝑠，similarly, we take the reciprocal and convert to one hour, the result is the value of μ1 , which is 3600(𝑠/ℎ)/3.0382𝑠= 1184.9𝑣𝑒ℎ/ℎ .

<!-- b000170 | heading | pages [8] -->
4.3.2 Time Cost at Toll Gates

<!-- b000171 | prose | pages [8] -->
Based on the formula for calculating the arrival rate of each lane given above, we can calculate the average time spent by each vehicle in the toll booth according to the formula [8]. For the traditional toll station, the following equation is obvious; For the cellular toll station, since the divergence before entering the toll gate, so each toll gate is facing the same traffic flow as one lane of the traditional toll station. The formula is shown below:

<!-- b000172 | prose | pages [8] -->
𝑊𝑇=

<!-- b000173 | prose | pages [8] -->
Where:

<!-- b000174 | prose | pages [8] -->
1

<!-- b000175 | furniture | pages [8] -->


<!-- b000176 | prose | pages [8] -->
𝜇𝑇−𝛷

<!-- b000177 | prose | pages [8] -->
𝐵

<!-- b000178 | prose | pages [8] -->
WT is the time cost passing through the toll gate. μT is the service rate of toll gates. Φ is the traffic flow. B is the number of toll gates.

<!-- b000179 | furniture | pages [9] -->
Team # 56731                                                                                                                                                 Page 9 of 22

<!-- b000180 | heading | pages [9] -->
4.3.3 Time Cost at Merging Points

<!-- b000181 | furniture | pages [9] -->


<!-- b000182 | caption | pages [9] -->
Figure 4.5 State transition of a birth-death process

<!-- b000183 | furniture | pages [9] -->


<!-- b000184 | furniture | pages [9] -->


<!-- b000185 | prose | pages [9] -->
The merge process at each merge point is essentially a Birth-Death Process，figure 4.5 describes the state transition of this process in the form of a Markov chain. In this process, each state follows the rule that the sum of the transit-in probability equals to the sum of the transit- out probability [5], and the probability sum of all events is 1. Therefore，we have the equations below:

<!-- b000186 | prose | pages [9] -->
λP0 = 𝜇0𝑃1

<!-- b000187 | prose | pages [9] -->
𝜆𝑃1 + 𝜇0𝑃1 = 𝜆𝑃0 + 𝜇1𝑃2

<!-- b000188 | furniture | pages [9] -->


<!-- b000189 | furniture | pages [9] -->


<!-- b000190 | prose | pages [9] -->
𝜆𝑃𝑛+ 𝜇1𝑃𝑛= 𝜆𝑃𝑛−1 + 𝜇1𝑃𝑛+1, 𝑛≥2

<!-- b000191 | furniture | pages [9] -->


<!-- b000192 | prose | pages [9] -->
∞

<!-- b000193 | furniture | pages [9] -->


<!-- b000194 | prose | pages [9] -->
∑𝑃𝑖

<!-- b000195 | prose | pages [9] -->
= 1

<!-- b000196 | prose | pages [9] -->
{

<!-- b000197 | prose | pages [9] -->
𝑖=0

<!-- b000198 | prose | pages [9] -->
Where: Pn, 𝑛∈𝑁 is the possibility of n vehicles in the system. λ is the arrival rate of a merging point. μ0 is the service rate at a merging point when the merging conflict doesn’t occur. μ1 is the service rate at a merging point when the merging conflict occurs. Solve the equations above, we can obtain the following set of equations:

<!-- b000199 | prose | pages [9] -->
𝑃0 = (1 + 𝜆

<!-- b000200 | prose | pages [9] -->
+

<!-- b000201 | prose | pages [9] -->
−1

<!-- b000202 | prose | pages [9] -->
2𝜆𝜇1

<!-- b000203 | prose | pages [9] -->
) 2 + 𝜆𝜇0𝜇1 −𝜆2𝜇0 2𝜇1 −𝜆𝜇0

<!-- b000204 | prose | pages [9] -->
𝜇0

<!-- b000205 | prose | pages [9] -->
𝜇0

<!-- b000206 | furniture | pages [9] -->


<!-- b000207 | prose | pages [9] -->
𝑃1 = 𝜆

<!-- b000208 | prose | pages [9] -->
𝑃0

<!-- b000209 | prose | pages [9] -->
𝜇0

<!-- b000210 | furniture | pages [9] -->


<!-- b000211 | prose | pages [9] -->
𝑛−2

<!-- b000212 | furniture | pages [9] -->


<!-- b000213 | prose | pages [9] -->
2𝜆2

<!-- b000214 | prose | pages [9] -->
( 𝜆

<!-- b000215 | prose | pages [9] -->
𝑃𝑛=

<!-- b000216 | prose | pages [9] -->
)

<!-- b000217 | prose | pages [9] -->
2 + 𝜆𝜇0

<!-- b000218 | prose | pages [9] -->
𝜇1

<!-- b000219 | prose | pages [9] -->
𝜇0

<!-- b000220 | prose | pages [9] -->
{

<!-- b000221 | furniture | pages [9] -->


<!-- b000222 | prose | pages [9] -->
𝑃0, 𝑛≥2

<!-- b000223 | prose | pages [9] -->
According to the probability obtained above, we can calculate the expected number of vehicles in the whole queuing system:

<!-- b000224 | prose | pages [9] -->
∞

<!-- b000225 | prose | pages [9] -->
𝜆

<!-- b000226 | prose | pages [9] -->
𝐿𝑠(𝜆) = ∑𝑖𝑃𝑖

<!-- b000227 | prose | pages [9] -->
𝜆𝜇1 −𝜆𝜇0

<!-- b000228 | furniture | pages [9] -->


<!-- b000229 | prose | pages [9] -->
𝜇1 −𝜆+ =

<!-- b000230 | prose | pages [9] -->
𝑖=1

<!-- b000231 | prose | pages [9] -->
Where:

<!-- b000232 | prose | pages [9] -->
𝜆𝜇1 −𝜆𝜇0 + 𝜇0𝜇1

<!-- b000233 | prose | pages [9] -->
Ls(λ) is the expected value of the vehicle in the system, also called the average queue length. According to the Little's Law[5], we obtain the formula below:

<!-- b000234 | prose | pages [9] -->
𝐿𝑠= 𝜆𝑊𝑠 We can get the average time of each vehicle staying in the queuing system:

<!-- b000235 | prose | pages [9] -->
𝑊𝑠(𝜆) = 𝐿𝑠

<!-- b000236 | prose | pages [9] -->
1 𝜇1 −𝜇0

<!-- b000237 | furniture | pages [9] -->


<!-- b000238 | prose | pages [9] -->
𝜇1 −𝜆+ 𝜆=

<!-- b000239 | prose | pages [9] -->
Where:

<!-- b000240 | prose | pages [9] -->
𝜆𝜇1 −𝜆𝜇0 + 𝜇0𝜇1

<!-- b000241 | prose | pages [9] -->
Ws(λ) is the average waiting time for vehicles in the system at a merge point

<!-- b000242 | heading | pages [9] -->
4.3.4 Total Time Cost

<!-- b000243 | prose | pages [9] -->
According to the assumption shown above, the traffic flow at the k-th merging point in a traditional toll station is:

<!-- b000244 | furniture | pages [10] -->
Team # 56731                                                                                                                                                 Page 10 of 22

<!-- b000245 | prose | pages [10] -->
(𝑘+ 1)𝛷

<!-- b000246 | prose | pages [10] -->
, 𝑘= 1,2, … , 𝐵−𝐿+ 1 𝐵

<!-- b000247 | prose | pages [10] -->
The possibility of arrival of corresponding k-th merging point is:

<!-- b000248 | prose | pages [10] -->
𝑘+ 1

<!-- b000249 | prose | pages [10] -->
, 𝑘= 1,2, … , 𝐵−𝐿+ 1 𝐵

<!-- b000250 | prose | pages [10] -->
According to the formula shown above, the total time cost at the merging point is:

<!-- b000251 | prose | pages [10] -->
𝐵−𝐿

<!-- b000252 | prose | pages [10] -->
+ 𝐵−𝐿+ 1

<!-- b000253 | prose | pages [10] -->
𝑊𝑀𝑇= 𝐿−1

<!-- b000254 | prose | pages [10] -->
⋅𝐵−𝐿 𝐵

<!-- b000255 | prose | pages [10] -->
𝜇0

<!-- b000256 | prose | pages [10] -->
Where:

<!-- b000257 | prose | pages [10] -->
∑𝑘+ 1

<!-- b000258 | prose | pages [10] -->
𝑊𝑠(𝑘+ 1

<!-- b000259 | furniture | pages [10] -->


<!-- b000260 | prose | pages [10] -->
𝛷)

<!-- b000261 | prose | pages [10] -->
𝐵 𝐵

<!-- b000262 | prose | pages [10] -->
𝐵

<!-- b000263 | prose | pages [10] -->
𝐵

<!-- b000264 | prose | pages [10] -->
𝑘=1

<!-- b000265 | prose | pages [10] -->
WMT is the average of the time spent by each vehicle at the merging point in a traditional toll station: L is the number of the lanes of the highway. Adding the time cost WT passing through each toll gate obtained above, we can calculate the average time cost WAT passing through the whole toll station:

<!-- b000266 | prose | pages [10] -->
𝐵−𝐿

<!-- b000267 | prose | pages [10] -->
⋅𝐵−𝐿

<!-- b000268 | prose | pages [10] -->
1

<!-- b000269 | prose | pages [10] -->
+ 𝐿−1

<!-- b000270 | prose | pages [10] -->
WAT = 𝑊𝑇+ 𝑊𝑀𝑇=

<!-- b000271 | prose | pages [10] -->
𝜇𝑇−Φ

<!-- b000272 | prose | pages [10] -->
𝐵

<!-- b000273 | prose | pages [10] -->
𝐵

<!-- b000274 | prose | pages [10] -->
Where:

<!-- b000275 | prose | pages [10] -->
+ 𝐵−𝐿+ 1

<!-- b000276 | prose | pages [10] -->
∑𝑘+ 1

<!-- b000277 | prose | pages [10] -->
𝑊𝑠(𝑘+ 1

<!-- b000278 | furniture | pages [10] -->


<!-- b000279 | prose | pages [10] -->
Φ)

<!-- b000280 | prose | pages [10] -->
𝜇0

<!-- b000281 | prose | pages [10] -->
𝐵

<!-- b000282 | prose | pages [10] -->
𝐵

<!-- b000283 | prose | pages [10] -->
𝐵

<!-- b000284 | prose | pages [10] -->
𝑘=1

<!-- b000285 | prose | pages [10] -->
WAT is the average time cost of each vehicle passing through the toll booth. But in our design, since the traffic flow merges in advance, the traffic flow of each lane becomes twice the previous lane, and the number of lanes reduce by half To simplify the calculation, we may assume that B is always even, so that the traffic flow at the k-th merging point is:

<!-- b000286 | prose | pages [10] -->
2(𝑘+ 1)𝛷 , 𝑘= 1,2, … , 𝐵 𝐵

<!-- b000287 | prose | pages [10] -->
2 −𝐿+ 1

<!-- b000288 | prose | pages [10] -->
The probability of the arrival of the corresponding k-th merging point is:

<!-- b000289 | prose | pages [10] -->
2(𝑘+ 1) , 𝑘= 1,2, … , 𝐵 𝐵

<!-- b000290 | prose | pages [10] -->
The total time is：

<!-- b000291 | prose | pages [10] -->
2 −𝐿+ 1

<!-- b000292 | prose | pages [10] -->
𝐵 2−𝐿

<!-- b000293 | prose | pages [10] -->
∑2(𝑘+ 1)

<!-- b000294 | prose | pages [10] -->
𝑊𝑠(2(𝑘+ 1)

<!-- b000295 | prose | pages [10] -->
+ 𝐵−2𝐿+ 2

<!-- b000296 | prose | pages [10] -->
𝑊𝑀𝐼= 2𝐿−2

<!-- b000297 | prose | pages [10] -->
⋅𝐵−2𝐿 𝐵

<!-- b000298 | prose | pages [10] -->
2𝜇0

<!-- b000299 | prose | pages [10] -->
𝐵

<!-- b000300 | prose | pages [10] -->
Where:

<!-- b000301 | furniture | pages [10] -->


<!-- b000302 | prose | pages [10] -->
𝛷)

<!-- b000303 | prose | pages [10] -->
𝐵

<!-- b000304 | prose | pages [10] -->
𝐵

<!-- b000305 | prose | pages [10] -->
𝑘=1

<!-- b000306 | prose | pages [10] -->
WMI is the average of the time spent by each vehicle in the cellular toll booths at the merging point. For cellular toll booths, all lanes will be merged in advance, we need to calculate additional time WEx cost at the pre-merging process,:

<!-- b000307 | prose | pages [10] -->
𝑊𝐸𝑥= 𝑊(2𝛷

<!-- b000308 | prose | pages [10] -->
𝐵)

<!-- b000309 | prose | pages [10] -->
Similarly, together with the time cost shown above, we obtain the average time cost WAI for each vehicle passing through the toll station:

<!-- b000310 | prose | pages [10] -->
WAI = 𝑊𝑇+ 𝑊𝑀𝐼+ 𝑊𝐸𝑥 Which is

<!-- b000311 | prose | pages [10] -->
𝐵 2−𝐿

<!-- b000312 | prose | pages [10] -->
∑2(𝑘+ 1)

<!-- b000313 | prose | pages [10] -->
𝑊𝑠(2(𝑘+ 1)

<!-- b000314 | prose | pages [10] -->
+ B −2L + 2

<!-- b000315 | prose | pages [10] -->
1

<!-- b000316 | prose | pages [10] -->
+ 2L −2

<!-- b000317 | prose | pages [10] -->
⋅𝐵−2𝐿

<!-- b000318 | prose | pages [10] -->
𝑊AI =

<!-- b000319 | prose | pages [10] -->
𝜇𝑇−Φ

<!-- b000320 | prose | pages [10] -->
B

<!-- b000321 | prose | pages [10] -->
2𝜇0

<!-- b000322 | prose | pages [10] -->
B

<!-- b000323 | prose | pages [10] -->
𝐵

<!-- b000324 | prose | pages [10] -->
+ 𝑊𝑠(2Φ

<!-- b000325 | prose | pages [10] -->
𝐵)

<!-- b000326 | prose | pages [10] -->
Φ)

<!-- b000327 | prose | pages [10] -->
𝐵

<!-- b000328 | prose | pages [10] -->
𝐵

<!-- b000329 | prose | pages [10] -->
𝑘=1

<!-- b000330 | prose | pages [10] -->
Substitute the specific parameters into WMI and WAI to calculate and plot, the comparison results shown in Figure 4.5：

<!-- b000331 | furniture | pages [11] -->
Team # 56731                                                                                                                                                 Page 11 of 22

<!-- b000332 | furniture | pages [11] -->


<!-- b000333 | caption | pages [11] -->
Figure 4.6 Comparison under different traffic flow

<!-- b000334 | furniture | pages [11] -->


<!-- b000335 | heading | pages [11] -->
4.4 Improve the Accident Prevention Ability

<!-- b000336 | heading | pages [11] -->
4.4.1 Hierarchical Merge Pattern

<!-- b000337 | prose | pages [11] -->
Traditional tollbooth has only one merging point at the end of the transition zone, increasing the possibility of being overcrowded. But for in our cellular tollbooth, there are bends in the cellular, keeping the speed of vehicles within a safe range. Therefore, we can decrease the possibility of these two kinds of accident:

<!-- b000338 | prose | pages [11] -->
(1) Traffic accidents caused by excessive speed; (2) Traffic congestion caused by overcrowding. The figures shown below describe our Pre-merging pattern and the traditional only-one merging pattern.

<!-- b000339 | furniture | pages [11] -->


<!-- b000340 | furniture | pages [11] -->


<!-- b000341 | caption | pages [11] -->
Figure 4.7 This merging patern has high security

<!-- b000342 | furniture | pages [11] -->


<!-- b000343 | furniture | pages [12] -->
Team # 56731                                                                                                                                                 Page 12 of 22

<!-- b000344 | furniture | pages [12] -->


<!-- b000345 | caption | pages [12] -->
Figure 4.8 high possibility merging conflict

<!-- b000346 | heading | pages [12] -->
4.4.2 A Gentle Design of the Transition Zone

<!-- b000347 | prose | pages [12] -->
The gradient rate of the transition zone is set according to the design speed and the tangential offset width, and different countries have different standards, the maximum ratio of US standard is 1:20, and the minimum is 1:8 [9].

<!-- b000348 | prose | pages [12] -->
Therefore, we further improve the model, by changing the rate of cross-section of the toll station to improve safety, the improved model is as follows:

<!-- b000349 | furniture | pages [12] -->


<!-- b000350 | caption | pages [12] -->
Figure 4.9 Improved design I

<!-- b000351 | heading | pages [12] -->
4.4.3 More Suitable for ETC Technology

<!-- b000352 | prose | pages [12] -->
Toll stations typically include a different set of charging models: conventional (human- staffed) tollbooths, exact-change (automated) tollbooths, and electronic toll collection booths. Vehicles near the entrance to the toll plaza often encounter traffic accidents due to the choice of different access routes, the location of different types of toll booths is also critical to safety.

<!-- b000353 | furniture | pages [12] -->


<!-- b000354 | prose | pages [12] -->
Due to large-scale promotion of ETC technology, the ways vehicles enter and exit the toll station, the ways vehicles drive through the toll station are different from the traditional charging pattern, which increase the possibility of accidents. A computational experiments show that gates associated to higher risk traffic flows, e.g. traffic directed to ETC, gates which approaches the toll station at speeds significantly above the average, should be locate in a central position with respect to other gate types. [10]. So, we add two ETC lanes in the middle of the new toll station。

<!-- b000355 | furniture | pages [13] -->
Team # 56731                                                                                                                                                 Page 13 of 22

<!-- b000356 | furniture | pages [13] -->


<!-- b000357 | caption | pages [13] -->
Figure 4.10 Improved design II

<!-- b000358 | heading | pages [13] -->
4.5 The influence of autonomous vehicles

<!-- b000359 | prose | pages [13] -->
As smart cars are non-cash payment, when compared to the traditional toll station, the cellular toll stations can better meet the needs of smart car. In this section, we first analyze the principle and characteristics of autonomous vehicles, then, according to the principle and characteristics of them, we optimized the cellular toll station model.

<!-- b000360 | heading | pages [13] -->
4.5.1 The Characteristics of Autonomous Vehicles

<!-- b000361 | prose | pages [13] -->
（1）Since the autonomous car are uncontrolled, they need to be equipped with automatic payment system, that is, ETC equipment. Therefore, they can pass through the toll station quickly. （2）Self-driving vehicles can improve road safety in one way or another. autonomous vehicles are equipped with sensing systems, which helps sensing the environment, based on the information about the road, vehicle location, and obstacles, the vehicle can steer and control the speed automatically. Therefore, they have a better control of the vehicle distance, brake, etc. which can reduce possibility of the occurrence of traffic accidents at the toll station. Besides, the driver's own factors (such as bad mood, disputes with the toll station service staff, etc.) will not affect the vehicle's safety [11]. （3）Vehicles at the junction of the toll station convergence can be more orderly，which avoids the occurrence of congestion and maximize the efficiency of cellular toll stations.

<!-- b000362 | heading | pages [13] -->
4.5.2 Our Solution

<!-- b000363 | prose | pages [13] -->
(1) In the future, there are more autonomous vehicles, since these vehicles are all equipped with ETC equipment, the cellular toll booths must increase the number of automatic toll lanes, reducing the number of manual toll lanes to maximize the efficiency. Our design can provide perfect service for those cars. As shown in the figure 4.10, the MTC lanes will be located at the sides of the toll station, and the straight lanes for Large vehicles are in the middle，reducing the inconvenient for the large vehicles. Meanwhile, as the autonomous vehicles are easy to steer, the rest lanes are all ETC lanes. When the autonomous vehicles enter the global market, the proportion of vehicles equipped with ETC will increase greatly.

<!-- b000364 | furniture | pages [13] -->


<!-- b000365 | furniture | pages [14] -->
Team # 56731                                                                                                                                                 Page 14 of 22

<!-- b000366 | furniture | pages [14] -->


<!-- b000367 | caption | pages [14] -->
Figure 4.11 Next generation tollbooth for autonomous vehicle

<!-- b000368 | furniture | pages [14] -->


<!-- b000369 | furniture | pages [14] -->


<!-- b000370 | prose | pages [14] -->
(2) According to the queueing model and the simulation result from VISSIM, the throughput of the toll station increases accompanies with the increase of the number of the ETC lanes. As the autonomous vehicles are all non-cash payment, when compared with the traditional toll station, the cellular design is more suitable.

<!-- b000371 | heading | pages [14] -->
V. Analysis of our Design

<!-- b000372 | heading | pages [14] -->
5.1 Using VISSIM Simulation to Find the Difference of These Two

<!-- b000373 | prose | pages [14] -->
Tollbooths.

<!-- b000374 | heading | pages [14] -->
5.1.1 Basic Data for Simulation

<!-- b000375 | prose | pages [14] -->
We use PTV-VISSIM 4.3 to do this simulation. Because there is no special configuration for other traffic simulation design(such as road connections, car route selection , deceleration belt and the design of tollbooths), so there are no more other detailed explanation about the parameter, and you can find more information at [12]. We set the speed of the vehicle through the ETC deceleration belt is 24km/h and deceleration speed is 2m/s2 .We refer to “The vehicles’ speed reduces to 24km/h when passing ETC lane” at literature[13]. （1）Establish VISSIM backplane

<!-- b000376 | furniture | pages [14] -->


<!-- b000377 | caption | pages [14] -->
Figure 5.1 Conceptual design model and simulation

<!-- b000378 | furniture | pages [14] -->


<!-- b000379 | furniture | pages [14] -->


<!-- b000380 | furniture | pages [14] -->


<!-- b000381 | caption | pages [14] -->
Figure 5.2 Traditional design model and simulation

<!-- b000382 | furniture | pages [14] -->


<!-- b000383 | furniture | pages [14] -->


<!-- b000384 | furniture | pages [15] -->
Team # 56731                                                                                                                                                 Page 15 of 22

<!-- b000385 | prose | pages [15] -->
（2）Design traffic composition and proportion

<!-- b000386 | furniture | pages [15] -->


<!-- b000387 | caption | pages [15] -->
Figure 5.3 Traffic composition and vehicle velocity distribution

<!-- b000388 | prose | pages [15] -->
（3）Other important description

<!-- b000389 | furniture | pages [15] -->


<!-- b000390 | furniture | pages [15] -->


<!-- b000391 | prose | pages [15] -->
We totally did two simulations, and you can find details in the table below:

<!-- b000392 | caption | pages [15] -->
Table 5.1 Simulation content

<!-- b000393 | prose | pages [15] -->
The first simulation Simulation times

<!-- b000394 | prose | pages [15] -->
Traditional

<!-- b000395 | prose | pages [15] -->
Tollbooth

<!-- b000396 | prose | pages [15] -->
Tollbooth

<!-- b000397 | prose | pages [15] -->
pattern

<!-- b000398 | prose | pages [15] -->
3 Main street 8 Toll lane 2 ETC

<!-- b000399 | prose | pages [15] -->
Bottom Road

<!-- b000400 | prose | pages [15] -->
ETC lane

<!-- b000401 | prose | pages [15] -->
position

<!-- b000402 | furniture | pages [15] -->


<!-- b000403 | prose | pages [15] -->
The second Simulation

<!-- b000404 | prose | pages [15] -->
Honeycomb

<!-- b000405 | prose | pages [15] -->
Traditional

<!-- b000406 | prose | pages [15] -->
Honeycomb

<!-- b000407 | prose | pages [15] -->
Tollbooths

<!-- b000408 | prose | pages [15] -->
Tollbooth

<!-- b000409 | prose | pages [15] -->
Tollbooths 3 3 3 8 8 8 2 0 0

<!-- b000410 | prose | pages [15] -->
The center

<!-- b000411 | prose | pages [15] -->
0 0

<!-- b000412 | prose | pages [15] -->
two lanes

<!-- b000413 | prose | pages [15] -->
Q: Why only consider ETC and artificial charges in the simulation, but do not consider the exact-change toll pattern？

<!-- b000414 | prose | pages [15] -->
A: According to the literature [17], the capacity of tollbooths in the United States, MTC (Only pre-sale tickets) 500veh/h, exact-change toll(Collect some coins) 500veh/h. This time only to simulate the above situation, if we consider all the charge pattern, our model will be too complicated. You can find section 5.2 for details.

<!-- b000415 | prose | pages [15] -->
Q: Why not consider autonomous vehicles? A: Because autonomous vehicles don’t need driver. The main solution is to install an ETC device on an automatic car. Ignoring the difference in this simulation, the specific impact of autonomous vehicles on the tollbooth is described in section 4.5.

<!-- b000416 | prose | pages [15] -->
Q: How to explain the great difference between the result of the queueing model and the result of the VISSIM simulation?

<!-- b000417 | prose | pages [15] -->
A: VISSIM software has taken a lot of factors into consideration. Therefore, compared with the pure theoretical derivation, VISSIM is more practical.

<!-- b000418 | prose | pages [15] -->
Q: How to explain the great change at the traffic flow 2000veh/h. A: Both two kinds of toll station have their maximum capacity. Therefore, there will be a great change for the total time cost and the time delayed. We can't eliminate the error between VISSUM and the reality, however, this won't affect our analysis.

<!-- b000419 | heading | pages [15] -->
5.1.2 Simulation Conclusion

<!-- b000420 | heading | pages [15] -->
(1) Sensitivity Analysis of Traffic Flow in Honeycomb Tollbooths

<!-- b000421 | prose | pages [15] -->
According to Fig. 1, Compared with the traditional tollbooth, honeycomb tollbooth is not sensitive to the traffic flow and has strong robustness. It is suitable for practical construction.

<!-- b000422 | prose | pages [15] -->
Simulation results show that the average transit time remains at about 11 seconds under different throughputs from 0 to 2000 (Unit: veh / h). We can infer that this model is not sensitive to traffic flow variations and has strong robustness which is suitable for practical construction.

<!-- b000423 | furniture | pages [15] -->


<!-- b000424 | furniture | pages [16] -->
Team # 56731                                                                                                                                                 Page 16 of 22

<!-- b000425 | furniture | pages [16] -->


<!-- b000426 | caption | pages [16] -->
Figure 5.4 Traffic capacity changed with traffic flow

<!-- b000427 | furniture | pages [16] -->


<!-- b000428 | furniture | pages [16] -->


<!-- b000429 | caption | pages [16] -->
Table 5.2 Honeycomb Tollbooths(All ETC)

<!-- b000430 | prose | pages [16] -->
Traffic flow (veh/h) Average time(s) Car number (veh)

<!-- b000431 | prose | pages [16] -->
10.778 42.778 500 10.900 88.222 1000 11.500 180.111 2000 11.567 189.556 2100 20.133 173.778 2200 22.878 184.556 2500 23.444 177.000 3000

<!-- b000432 | furniture | pages [16] -->


<!-- b000433 | prose | pages [16] -->
Delay time(s) Stop time(s) Stop number

<!-- b000434 | prose | pages [16] -->
0.056 0.000 0.000 0.144 0.000 0.000 0.633 0.000 0.006 0.667 0.000 0.001 9.256 2.700 0.541 12.033 3.933 0.621 12.578 4.522 0.723

<!-- b000435 | caption | pages [16] -->
Table 5.3 Traditional tollbooth(All ETC)

<!-- b000436 | prose | pages [16] -->
Traffic flow

<!-- b000437 | prose | pages [16] -->
Average time(s) Car number

<!-- b000438 | prose | pages [16] -->
(veh/h)

<!-- b000439 | prose | pages [16] -->
(veh)

<!-- b000440 | prose | pages [16] -->
10.078 43.000 500 10.200 88.444 1000 12.078 174.556 2000 13.267 179.667 2100 47.178 146.889 2200 51.222 145.000 2500 57.100 151.333 3000

<!-- b000441 | furniture | pages [16] -->


<!-- b000442 | prose | pages [16] -->
Delay time(s) Stop time(s) Stop number

<!-- b000443 | prose | pages [16] -->
0.056 0.000 0.000 0.100 0.000 0.000 1.911 0.767 0.173 3.078 1.378 0.283 36.422 22.567 1.944 40.444 24.367 2.331 46.933 30.878 2.201

<!-- b000444 | prose | pages [16] -->
（2）When the toll station is all configured ETC, we can get:

<!-- b000445 | prose | pages [16] -->
①The throughput of the two toll stations is almost the same in light traffic. ②Honeycomb tollbooth is better than traditional tollbooth in heavy traffic, when traffic flow is 2500veh/h. The VISSIM simulation results show that the honeycomb tollbooth is 55% larger than the traditional tollbooth on total time cost, and about 70% on time delay. ③The simulation results are in good agreement with the results of queuing theory.

<!-- b000446 | prose | pages [16] -->
It is shown that the queuing theory model is very reasonable to measure the throughput of the honeycomb tollbooth. （2）Two ETC and six MTC, we can get:

<!-- b000447 | prose | pages [16] -->
①The throughput of the two toll stations is almost the same in light traffic(<400veh/h) ②The traffic capacity of honeycomb tollbooths will decrease in heavy traffic(>900veh/h). ③The traffic flow between 400 veh/h and 900 veh/h honeycomb tollbooths is stronger than the traditional tollbooth.

<!-- b000448 | furniture | pages [17] -->
Team # 56731                                                                                                                                                 Page 17 of 22

<!-- b000449 | furniture | pages [17] -->


<!-- b000450 | caption | pages [17] -->
Figure 5.5 Average travel time and average time delay (Two ETC and six MTC)

<!-- b000451 | furniture | pages [17] -->


<!-- b000452 | furniture | pages [17] -->


<!-- b000453 | caption | pages [17] -->
Table 5.4 Honeycomb Tollbooths (Two ETC and six MTC)

<!-- b000454 | prose | pages [17] -->
Traffic flow (veh/h) Average time(s) Car number

<!-- b000455 | prose | pages [17] -->
(veh)

<!-- b000456 | prose | pages [17] -->
48.622 16.444 200.000 51.600 32.000 400.000 54.211 48.667 600.000 59.144 65.222 800.000 64.111 78.778 1000.000 71.567 84.889 1200.000

<!-- b000457 | prose | pages [17] -->
Delay time(s) Stop time(s) Stop number

<!-- b000458 | prose | pages [17] -->
0.889 0.100 0.031 1.267 0.178 0.058 2.511 0.411 0.108 5.156 1.144 0.259 10.900 2.922 0.573 18.556 5.644 0.986

<!-- b000459 | furniture | pages [17] -->


<!-- b000460 | furniture | pages [17] -->


<!-- b000461 | caption | pages [17] -->
Table 5.5 Traditional tollbooth (Two ETC and six MTC)

<!-- b000462 | prose | pages [17] -->
Traffic flow (veh/h) Average time(s) Car number

<!-- b000463 | prose | pages [17] -->
(veh)

<!-- b000464 | prose | pages [17] -->
40.922 16.111 200.000

<!-- b000465 | prose | pages [17] -->
50.822 32.111 400.000

<!-- b000466 | prose | pages [17] -->
58.389 44.000 600.000

<!-- b000467 | prose | pages [17] -->
60.967 43.889 800.000

<!-- b000468 | prose | pages [17] -->
60.989 43.778 1000.000

<!-- b000469 | prose | pages [17] -->
61.867 43.889 1200.000

<!-- b000470 | furniture | pages [17] -->


<!-- b000471 | heading | pages [17] -->
5.1.3 Simulation example

<!-- b000472 | prose | pages [17] -->
Delay time(s) Stop time(s) Stop number

<!-- b000473 | prose | pages [17] -->
0.000 0.056 0.042

<!-- b000474 | prose | pages [17] -->
1.522 0.322 0.159

<!-- b000475 | prose | pages [17] -->
5.433 0.600 0.220

<!-- b000476 | prose | pages [17] -->
6.922 0.422 0.176

<!-- b000477 | prose | pages [17] -->
7.056 0.367 0.148

<!-- b000478 | prose | pages [17] -->
7.689 0.456 0.169

<!-- b000479 | furniture | pages [17] -->


<!-- b000480 | caption | pages [17] -->
Figure 5.6 Circulation of traffic

<!-- b000481 | furniture | pages [17] -->


<!-- b000482 | caption | pages [17] -->
Figure 5.7 Congestion occurs in merging

<!-- b000483 | furniture | pages [18] -->
Team # 56731                                                                                                                                                 Page 18 of 22

<!-- b000484 | furniture | pages [18] -->


<!-- b000485 | heading | pages [18] -->
5.2 The influence of different proportions tollbooth

<!-- b000486 | heading | pages [18] -->
5.2.1 Model Simplify

<!-- b000487 | prose | pages [18] -->
According to the data in [14], there is no great difference between the influence of MTC tollbooths and the influence of exact-change tollbooths, thus we can omit that difference and only take MTC into consideration. In the rest part of the paper, we combine the MTC method and the exact-change method into cash method.

<!-- b000488 | furniture | pages [18] -->


<!-- b000489 | caption | pages [18] -->
Table 5.6 Throughput of each lane in the US[14]

<!-- b000490 | prose | pages [18] -->
Charging type MTC system Exact-change Low speed ETC system High speed ETC system

<!-- b000491 | furniture | pages [18] -->


<!-- b000492 | heading | pages [18] -->
5.2.2 Result Analysis

<!-- b000493 | furniture | pages [18] -->


<!-- b000494 | prose | pages [18] -->
Throughput per lane（veh/h） 425 500 1200 1800

<!-- b000495 | furniture | pages [18] -->


<!-- b000496 | furniture | pages [18] -->


<!-- b000497 | heading | pages [18] -->
（1）Sensitivity Analysis of Impact of Cellular Toll Station on Capacity

<!-- b000498 | prose | pages [18] -->
The capacity of cellular toll stations is more sensitive to the proportion of ETC lanes. There is a possible scenario that when decreasing the number of ETC lanes, the total time cost increases rapidly.

<!-- b000499 | furniture | pages [18] -->


<!-- b000500 | caption | pages [18] -->
Figure 5.8 The influence of the number of ETC lanes

<!-- b000501 | furniture | pages [18] -->


<!-- b000502 | furniture | pages [18] -->


<!-- b000503 | caption | pages [18] -->
Table 5.7 Comparison under different number of ETC lanes

<!-- b000504 | prose | pages [18] -->
Total time cost

<!-- b000505 | prose | pages [18] -->
Number of vehicle

<!-- b000506 | prose | pages [18] -->
ETC/MTC (sec)

<!-- b000507 | prose | pages [18] -->
per lane (veh)

<!-- b000508 | prose | pages [18] -->
80.689 276.111 0\8 76.111 283.556 1\7 66.378 286.667 2\6 57.167 288.889 3\5 49.633 289.333 4\4 42.611 290.111 5\3 34.722 290.667 6\2 18.778 292.111 7\1 8\0 10.822 292.667

<!-- b000509 | prose | pages [18] -->
Time cost on

<!-- b000510 | prose | pages [18] -->
Number of

<!-- b000511 | prose | pages [18] -->
Time delayed (sec) parking (sec)

<!-- b000512 | prose | pages [18] -->
parking (sec) 19.078 4.089 0.712 16.500 4.622 0.744 11.922 3.344 0.586 8.311 2.011 0.386 6.478 1.544 0.308 5.578 1.278 0.259 4.844 0.633 0.111 1.456 0.467 0.071 0.111 0.000 0.000

<!-- b000513 | furniture | pages [18] -->


<!-- b000514 | furniture | pages [18] -->


<!-- b000515 | prose | pages [18] -->
（2）The lower the proportion of cash charges, the smaller average transit time and average delay. （3）With the increase in the number of ETC lanes, the average number of vehicles per lane increased at the same time, improve the road utilization.

<!-- b000516 | furniture | pages [19] -->
Team # 56731                                                                                                                                                 Page 19 of 22

<!-- b000517 | prose | pages [19] -->
（4）When 8 ETC non-cash lanes are opened, the cellular toll station allows all cars on the lane to pass through without parking or waiting in queue.. （5）8 ETC lanes are 8 times faster than 8 cash lanes.

<!-- b000518 | heading | pages [19] -->
5.3 Strengths and Weaknesses

<!-- b000519 | heading | pages [19] -->
5.3.1 Strengths

<!-- b000520 | prose | pages [19] -->
(1) Cellular toll stations greatly save land area and reduce construction costs. (2) Cellular toll stations adopt the pre-merging strategy, preventing the overcrowding. (3) Cellular toll stations can force deceleration, preventing the accident caused by the speed difference between the ETC lanes and MTC lanes.

<!-- b000521 | prose | pages [19] -->
(4) Through a large number of VISSIM traffic simulation data, we successfully obtained the simulation result, and the result is identical to the result of the queueing model. Simulation results show that the ideal cellular distributed toll booths have better results compared with traditional toll stations, especially when the traffic flow is heavy, the average travel time reduced by about 55% and the average delay time of each lane is reduced by about 70%.

<!-- b000522 | prose | pages [19] -->
(5) Through the VISSIM simulation, we obtained the results can't directly obtain from the queueing model, which is toll station with both ETC and MTC lanes, making up for the shortcomings of the model can't be applied to reality.

<!-- b000523 | heading | pages [19] -->
5.3.2 Weakness

<!-- b000524 | prose | pages [19] -->
(1) The length of the vehicles must be taken into the consideration for the reason that some long vehicle can't pass through the cellular.

<!-- b000525 | prose | pages [19] -->
(2) Because there is no toll station model in VISSIM4.3, we refer to a large number of references to determine the average speed of the vehicle through the toll station, and simulate the process through the deceleration zone model.

<!-- b000526 | prose | pages [19] -->
(3) Because the actual traffic composition ratio of the actual data and speed acceleration is not easy to obtain, resulting in traffic simulation is not close to reality.

<!-- b000527 | prose | pages [19] -->
(4) In the simulation, the difference between the exact-change lane and the manual lane is neglected.

<!-- b000528 | heading | pages [19] -->
VI. Conclusion

<!-- b000529 | prose | pages [19] -->
With the popularization of ETC equipment and autonomous vehicles, the MTC lanes will be totally replaced by the ETC lanes in the next 20 years, which will increase the road capacity and decrease the time cost by each car passing through the toll station.

<!-- b000530 | prose | pages [19] -->
At present the traditional design of toll stations covers a large area, and the cost of construction is high. With the raise of the vehicles' speed, there will be congestions at the merging point, which may increase the possibility of accident.

<!-- b000531 | prose | pages [19] -->
In order to solve these problems, we put forward a new design of cellular toll stations. This design is inspired by the honeycomb. The tollbooths are located at the center of each regular hexagon. Thanks to this special structure, the cost of construction can be significantly reduced. Meanwhile, by pre-merging the traffic flow inside the toll station, the expected time cost by vehicles in the merging procedure can be diminished extraordinarily. In addition, by appropriate design, the probability of collision at the emerging points can be decreased.

<!-- b000532 | furniture | pages [19] -->


<!-- b000533 | furniture | pages [19] -->


<!-- b000534 | furniture | pages [19] -->


<!-- b000535 | furniture | pages [19] -->


<!-- b000536 | furniture | pages [19] -->


<!-- b000537 | furniture | pages [19] -->


<!-- b000538 | furniture | pages [20] -->
Team # 56731                                                                                                                                                 Page 20 of 22

<!-- b000539 | furniture | pages [20] -->


<!-- b000540 | heading | pages [20] -->
Letter

<!-- b000541 | prose | pages [20] -->
Dear New Jersey Turnpike Administration:

<!-- b000542 | furniture | pages [20] -->


<!-- b000543 | prose | pages [20] -->
It is my pleasure to give policy recommendation to New Jersey Turnpike Authority. We have developed a new design of toll station system，This kind of design can solve many problems caused by the increase of ETC service and autonomous car,

<!-- b000544 | furniture | pages [20] -->


<!-- b000545 | prose | pages [20] -->
According to our information, New Jersey's freeway mileage is more than 321 kilometers, ranked fifth among the US. Meanwhile, the ETC utilization rate of toll stations of New Jersey has exceeded 80%. In the future, with the popularity of ETC equipment, the use of ETC in the toll station may further increase. While the commercial layout of autonomous vehicles is accelerating, in the next 20 years there may be a large number of autonomous vehicles on the road, which increases the speed passing through the toll station. Therefore, your problem might be: “How to guarantee the road capacity of toll station?”,” How to lead the traffic flow to converge at the exit?”,” How to ensure the safety of vehicles?”.

<!-- b000546 | furniture | pages [20] -->


<!-- b000547 | furniture | pages [20] -->


<!-- b000548 | furniture | pages [20] -->


<!-- b000549 | furniture | pages [20] -->


<!-- b000550 | furniture | pages [20] -->


<!-- b000551 | prose | pages [20] -->
We come up with a cellular toll booth design, whose conceptual model is shown above. This design has four main advantages：

<!-- b000552 | prose | pages [20] -->
(1) Through the analyzation of the toll station area, we can know that cellular architecture can reduce the construction area about 50% compared with... with the same number of tollbooths (8 as an example).

<!-- b000553 | prose | pages [20] -->
(2) We simulate a large number of actual situation with the use of PTV-VISSIM. Simulation results show that the ideal cellular distributed tollbooths have better performances compared with traditional toll stations, especially when the traffic flow is heavy. That is the average travel time reduced by about 55% and the average delay time of each lane was reduced by about 70%.

<!-- b000554 | prose | pages [20] -->
(3) According to PTV-VISSIM simulation: full ETC tollbooth is 8 times faster than full MTC tollbooth.

<!-- b000555 | prose | pages [20] -->
(4) We simulate the performance of the cellular toll plaza under different traffic throughput. Simulation results show that the average transit time remains at about 11 seconds under different throughputs from 0 to 2000 (Unit: Veh / h). We can infer that this model is not sensitive to traffic flow variations and has strong robustness which is suitable for practical construction.

<!-- b000556 | furniture | pages [20] -->


<!-- b000557 | prose | pages [20] -->
In order to give you a more intuitive view of the advantages of our cellular toll station, we

<!-- b000558 | furniture | pages [21] -->
Team # 56731                                                                                                                                                 Page 21 of 22

<!-- b000559 | prose | pages [21] -->
make a comparison diagram for you，The black part shown below is our design with 8 toll gates, while the blue par is the traditional design.

<!-- b000560 | furniture | pages [21] -->


<!-- b000561 | prose | pages [21] -->
Furthermore, in order to make you understand the advantages of the cellular toll station with more ETC lanes. We make the diagram shown below, where the blue solid line stands for the performance of the traditional design and the red dashed line is our design. From the diagram, we can learn that the time cost passing through the cellular toll station is lower than the traditional one under the heavy traffic flow.

<!-- b000562 | furniture | pages [21] -->


<!-- b000563 | prose | pages [21] -->
Thank you again for taking the time to read our suggestions. We sincerely hope that the cellular toll station can solve the problem of congestion!

<!-- b000564 | furniture | pages [21] -->


<!-- b000565 | prose | pages [21] -->
Best Regards, Sincerely

<!-- b000566 | furniture | pages [21] -->


<!-- b000567 | furniture | pages [21] -->


<!-- b000568 | furniture | pages [21] -->


<!-- b000569 | furniture | pages [21] -->


<!-- b000570 | furniture | pages [21] -->


<!-- b000571 | furniture | pages [21] -->


<!-- b000572 | furniture | pages [21] -->


<!-- b000573 | furniture | pages [21] -->


<!-- b000574 | furniture | pages [21] -->


<!-- b000575 | furniture | pages [21] -->


<!-- b000576 | furniture | pages [21] -->


<!-- b000577 | furniture | pages [21] -->


<!-- b000578 | furniture | pages [21] -->


<!-- b000579 | furniture | pages [21] -->


<!-- b000580 | furniture | pages [21] -->


<!-- b000581 | furniture | pages [21] -->


<!-- b000582 | furniture | pages [21] -->


<!-- b000583 | furniture | pages [22] -->
Team # 56731                                                                                                                                                 Page 22 of 22

<!-- b000584 | heading | pages [22] -->
VII. References

<!-- b000585 | references | pages [22] -->
[1]Wang Dianhai. Traffic flow theory [M].Beijing: China Communications Press.2002.

<!-- b000586 | references | pages [22] -->
[2]Wu Xiaowu. Study on Traffic Safety of Toll Station of Expressway [D].Chang’an Universi

<!-- b000587 | references | pages [22] -->
ty,2004.

<!-- b000588 | references | pages [22] -->
[3]Honeycomb.https://en.wikipedia.org/wiki/Honeycomb.

<!-- b000589 | references | pages [22] -->
[4]Queueing theory, https://en.wikipedia.org/wiki/Queueing_theory.

<!-- b000590 | references | pages [22] -->
[5]Gross D. Fundamentals of queueing theory[M]. John Wiley & Sons, 2008.

<!-- b000591 | references | pages [22] -->
[6]The Washington State Department of Transportation design manual, chapter 1210,

<!-- b000592 | references | pages [22] -->
Geometric Plan Elements.

<!-- b000593 | references | pages [22] -->
[7]Manual H C. Highway capacity manual[J]. Washington, DC, 2000.

<!-- b000594 | references | pages [22] -->
[8]Hock, Ng Chee, Queueing Modeling Fundamentals, Wiley, New York, 1996.

<!-- b000595 | references | pages [22] -->
[9]Cheng J, Jiang P. Design of Toll Collection Station for Quanzhou to Xiamen Freeway[J].

<!-- b000596 | references | pages [22] -->
Journal of Highway & Transportation Reseach Andk Development, 1995.

<!-- b000597 | references | pages [22] -->
[10] Pratelli A, Schoen F. Multi-Toll-Type Motorway Stations Optimal Layout[C]// Urban

<!-- b000598 | references | pages [22] -->
Transport XII. Urban Transport and the Environment in the 21st Century. 2006.

<!-- b000599 | references | pages [22] -->
[11] Sivak M, Schoettle B. Road safety with self-driving vehicles: General limitations and road

<!-- b000600 | references | pages [22] -->
sharing with conventional vehicles[J]. 2015.

<!-- b000601 | references | pages [22] -->
[12]PTV Vissim. http://vision-traffic.ptvgroup.com/en-us/products/ptv-vissim/.

<!-- b000602 | references | pages [22] -->
[13] Liu L, Weng J, Rong J. Simulation Based Mixed ETC/MTC Freeway Toll Station

<!-- b000603 | references | pages [22] -->
Capacity[C]// 19th ITS World Congress. 2012.

<!-- b000604 | references | pages [22] -->
[14]Ding Chuangxin. Study on Capacity of High - grade Highway Toll Station [D]. Kunming

<!-- b000605 | references | pages [22] -->
University of Science and Technology,2005.

<!-- b000606 | furniture | pages [22] -->


<!-- b000607 | furniture | pages [23] -->
Team # 56731                                                                                                                                                 Page 23 of 22

<!-- b000608 | heading | pages [23] -->
VIII. Appendix

<!-- b000609 | heading | pages [23] -->
8.1 Figure

<!-- b000610 | prose | pages [23] -->
We have design 3D model of our honeycomb tollbooths.

<!-- b000611 | furniture | pages [23] -->


<!-- b000612 | caption | pages [23] -->
Figure 8.1 3D model I

<!-- b000613 | furniture | pages [23] -->


<!-- b000614 | caption | pages [23] -->
Figure 8.2 3D model II

<!-- b000615 | furniture | pages [23] -->


<!-- b000616 | furniture | pages [23] -->


<!-- b000617 | furniture | pages [23] -->


<!-- b000618 | furniture | pages [23] -->

