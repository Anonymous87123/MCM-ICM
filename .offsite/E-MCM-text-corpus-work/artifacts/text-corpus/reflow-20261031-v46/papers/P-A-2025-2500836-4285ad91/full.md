# P-A-2025-2500836-4285ad91

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
2025

<!-- b000002 | front_matter | pages [1] -->
Problem Chosen

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | prose | pages [1] -->
MCM/ICM

<!-- b000005 | furniture | pages [1] -->
2500836

<!-- b000006 | heading | pages [1] -->
Summary Sheet

<!-- b000007 | title | pages [1] -->
Stairs: The Glory of the Ordinary

<!-- b000008 | heading | pages [1] -->
Summary

<!-- b000009 | prose | pages [1] -->
Stairs have long been a fundamental architectural element widely utilized in building design to facilitate transportation connections. They embody the characteristics of both a "platform" and a "stair," serving as pathways for individuals to ascend and descend, enhancing the architectural aesthetic, and enriching the spatial hierarchy of structures. This article examines the construction duration, usage, and human behavior patterns associated with steps by analyzing their degree of wear.

<!-- b000010 | prose | pages [1] -->
In the Model Preparation phase, the research subjects were identified as the stairs inside the Leaning Tower of Pisa, which also determined the material and environmental conditions of the stairs. Then, Computer Vision techniques were used to obtain the required wear depth data of the stairs, and the focus was further narrowed to the bottom step of the Leaning Tower of Pisa. Finally, based on practical experience and literature, we concluded that the wear depth distribution on the stair surface follows a two-dimensional normal distribution. The parameters were then fitted using a Particle Swarm Optimization algorithm(PSO).

<!-- b000011 | prose | pages [1] -->
To address the first three issues, we developed a Step Wear Analysis Model. Firstly, we used pedestrian traffic, defined as the number of people using the stairs daily, to represent and calculate the stair usage frequency. Given the known distribution of wear depth, and based on Archard's Law, we integrated to find that the daily pedestrian traffic is 1,175. Next, by considering people's typical force application habits when ascending and descending stairs, we defined a direction preference index and, based on the wear depth distribution, determined that people prefer to descend the stairs. Finally, a continuity equation for simulating pedestrian flow was established based on Navier-Stokes Equations. Then we used the finite difference method to calculate the pedestrian density during stair usage and got ρ = 0.6535 < 1.5, which indicated that people prefer to travel single file.

<!-- b000012 | prose | pages [1] -->
To analyze the usage condition and characteristics of the steps, we built a Step Characteristic Analysis Model. We first established the relationship between the number of users and the age of the stairs as an exponential function. Based on the relationship between wear depth and pedestrian traffic, we calculated the theoretical wear depth to be 4.871 cm and compared it with the actual data of 4.5 cm. After analyzing the mean square error, we found that the results were in line with expectations. Next, using the known relationship between wear depth, pedestrian traffic, and stair age, we employed the Monte Carlo method to estimate the stair age, yielding a range of approximately (282.1984, and 342.8016). To determine whether the stairs have been repaired or renovated, we used chemical methods and compared the theoretical and actual stair ages, confirming that the Leaning Tower of Pisa stairs have been renovated, and we found supporting evidence to corroborate this. To study the material properties of the stairs, we first selected several representative parameters for stone and wood materials. By scanning images and obtaining data, we compared these parameters with those of the stairs and then used the Person correlation coefficient to analyze their relationship. Finally, to analyze the number of stair users on a specific day, we established a partial differential equation to instantaneously analyze the changes in pedestrian traffic, revealing that there was a small number of people using the stairs over a longer time.

<!-- b000013 | prose | pages [1] -->
Furthermore, we conduct a sensitivity analysis on the two-dimensional normal distribution model of wear depth and the continuity equation for simulating pedestrian flow, which further demonstrates the robustness and accuracy of the model presented in this paper.

<!-- b000014 | keywords | pages [1] -->
Key words: Wear depth; Archard; PSO; Navier-Stokes; Mont Carlo method;

<!-- b000015 | furniture | pages [2] -->
Page 1 of 25

<!-- b000016 | furniture | pages [2] -->
Team # 2500836

<!-- b000017 | heading | pages [2] -->
Contents

<!-- b000018 | contents | pages [2] -->
1 Introduction....

<!-- b000019 | contents | pages [2] -->
2

<!-- b000020 | contents | pages [2] -->
1.1 Problem Background

<!-- b000021 | contents | pages [2] -->
2

<!-- b000022 | contents | pages [2] -->
1.2 Restatement of the Problem.

<!-- b000023 | contents | pages [2] -->
2

<!-- b000024 | contents | pages [2] -->
1.3 Our Work ..

<!-- b000025 | contents | pages [2] -->
3

<!-- b000026 | contents | pages [2] -->
2 Assumptions and Justifications

<!-- b000027 | contents | pages [2] -->
4

<!-- b000028 | contents | pages [2] -->
3Notations .....

<!-- b000029 | contents | pages [2] -->
5

<!-- b000030 | contents | pages [2] -->
4Model Preparation.

<!-- b000031 | contents | pages [2] -->
5

<!-- b000032 | contents | pages [2] -->
4.1 Data Processing...

<!-- b000033 | contents | pages [2] -->
.5

<!-- b000034 | contents | pages [2] -->
4.2 Solution of the Wear Depth Distribution.

<!-- b000035 | contents | pages [2] -->
5 Model I: Step Wear Analysis Model..

<!-- b000036 | contents | pages [2] -->
.8

<!-- b000037 | contents | pages [2] -->
5.1 Pedestrian Flow Calculation based on Archard's Law..

<!-- b000038 | contents | pages [2] -->
..8

<!-- b000039 | contents | pages [2] -->
5.2 Preference Direction Model Based on Wear Depth Distribution

<!-- b000040 | contents | pages [2] -->
..10

<!-- b000041 | contents | pages [2] -->
5.3 Walking Patterns Model based on Navier-Stokes Equations

<!-- b000042 | contents | pages [2] -->
.11

<!-- b000043 | contents | pages [2] -->
Model II: Step Characteristic Analysis Model ....

<!-- b000044 | contents | pages [2] -->
..12

<!-- b000045 | contents | pages [2] -->
6

<!-- b000046 | contents | pages [2] -->
.13

<!-- b000047 | contents | pages [2] -->
6.1 Comparison of Actual and Theoretical Stair Usage Time.

<!-- b000048 | contents | pages [2] -->
.14

<!-- b000049 | contents | pages [2] -->
6.2 Calculation of Stair Service Life..

<!-- b000050 | contents | pages [2] -->
..16

<!-- b000051 | contents | pages [2] -->
6.3 Determination of Stair Renovation.

<!-- b000052 | contents | pages [2] -->
..17

<!-- b000053 | contents | pages [2] -->
6.4 Determination of Material Source

<!-- b000054 | contents | pages [2] -->
..19

<!-- b000055 | contents | pages [2] -->
6.5 Research on temporal distribution of the Pedestrian Flow

<!-- b000056 | contents | pages [2] -->
.20

<!-- b000057 | contents | pages [2] -->
7 Sensitivity Analysis....

<!-- b000058 | contents | pages [2] -->
.20

<!-- b000059 | contents | pages [2] -->
7.1 Sensitivity Analysis of 2-D Normal Distribution Model of Wear Depth ..

<!-- b000060 | contents | pages [2] -->
7.2 Sensitivity Analysis of Continuity Equation for Simulating Walking Patterns.

<!-- b000061 | contents | pages [2] -->
.21

<!-- b000062 | contents | pages [2] -->
.21

<!-- b000063 | contents | pages [2] -->
8 Strength and Weakness

<!-- b000064 | contents | pages [2] -->
8.1 Strength ...

<!-- b000065 | contents | pages [2] -->
.21

<!-- b000066 | contents | pages [2] -->
8.2 Weakness

<!-- b000067 | contents | pages [2] -->
22

<!-- b000068 | contents | pages [2] -->
9 Conclusion ...

<!-- b000069 | contents | pages [2] -->
22

<!-- b000070 | contents | pages [2] -->
References ....

<!-- b000071 | contents | pages [2] -->
23

<!-- b000072 | contents | pages [2] -->
.24

<!-- b000073 | contents | pages [2] -->
Appendix...

<!-- b000074 | furniture | pages [3] -->
Team # 2500836                                                                   Page 2 of 25

<!-- b000075 | heading | pages [3] -->
1 Introduction

<!-- b000076 | heading | pages [3] -->
1.1 Problem Background

<!-- b000077 | prose | pages [3] -->
Steps are structures typically found at the entrances of houses or along slopes, consisting of successive levels that allow people to ascend and descend. They are usually constructed from bricks, stones, concrete, or wood [1]. In feudal societies that emphasized hierarchy, the design and materials 微信公众号：数学模型 of staircases often symbolized power and status. Commoners' stairways featured fewer steps and were primarily made of simple wood and earth; those of individuals with slightly higher status included more steps and were crafted from bricks and stones, while the most opulent staircases showcased marble [2]. Consequently, the study of steps holds significant importance in understanding ancient civilizations. In contemporary architecture, the design and number of stairs are not limited by any particular framework, with a focus on comfort and safety as primary concerns.

<!-- b000078 | prose | pages [3] -->
When an ancient building is set to be renovated or expanded after its completion, determining the completion time often requires additional methods of reference beyond the relevant documents. The wear on the steps serves as a direct indicator of their frequency and duration of use. Over time, regular use causes the step surface to wear down, resulting in smooth, sunken, or flat areas. By analyzing the degree of wear on the surfaces of the steps, archaeologists can deduce their service life 微信号：MATHmodels and gain insights into usage patterns and the daily habits of ancient people. Furthermore, the architectural design of the steps, the materials utilized, and their chronological characteristics can also offer valuable information in establishing the timeline of completion.

<!-- b000079 | prose | pages [3] -->
a. Stone steps, Leaning Tower of Pisa b. Stone steps, Great Wall

<!-- b000080 | prose | pages [3] -->
c. Wooden steps d. Stone steps, Stirling Castle

<!-- b000081 | caption | pages [3] -->
Figure 1: Typical ancient architectural steps that have uneven wear after long-term use

<!-- b000082 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000083 | prose | pages [3, 4] -->
Considering the background information and restricted conditions identified in the problem statement, we need to solve the following problems: ⚫ Develop a model to describe the frequency of stair usage. ⚫ Create a model to determine whether a certain direction of travel was favored. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m ⚫ Develop a model to determine whether people traveled single file or side by side. ⚫ Build a model to evaluate whether the wear observed on the stairs is consistent with the historical and environmental factors influencing the stairwell’s age and usage. ⚫ Create a model to estimate the age of the stairwell and determine the reliability of the age estimate. ⚫ Design a model to identify signs of repairs or renovations. ⚫ Build a model to determine whether the wear on the stairwell is consistent with materials believed to originate from specific sources, such as quarries or forests. ⚫ Develop a model to estimate the typical number of people using the stairs and identify whether heavy short-term usage or prolonged lighter usage is more consistent with the observed wear patterns.

<!-- b000084 | furniture | pages [3] -->
m

<!-- b000085 | furniture | pages [3] -->
m

<!-- b000086 | furniture | pages [3] -->
m

<!-- b000087 | furniture | pages [3] -->
m

<!-- b000088 | furniture | pages [3] -->
m

<!-- b000089 | furniture | pages [3] -->
m

<!-- b000090 | furniture | pages [3] -->
m

<!-- b000091 | furniture | pages [3] -->
m

<!-- b000092 | furniture | pages [3] -->
m

<!-- b000093 | furniture | pages [3] -->
m

<!-- b000094 | furniture | pages [3] -->
m

<!-- b000095 | furniture | pages [3] -->
m

<!-- b000096 | furniture | pages [3] -->
m

<!-- b000097 | furniture | pages [3] -->
m

<!-- b000098 | furniture | pages [3] -->
m

<!-- b000099 | furniture | pages [3] -->
m

<!-- b000100 | furniture | pages [3] -->
m

<!-- b000101 | furniture | pages [3] -->
m

<!-- b000102 | furniture | pages [3] -->
m

<!-- b000103 | furniture | pages [3] -->
m

<!-- b000104 | furniture | pages [3] -->
m

<!-- b000105 | furniture | pages [3] -->
m

<!-- b000106 | furniture | pages [3] -->
m

<!-- b000107 | furniture | pages [3] -->
m

<!-- b000108 | furniture | pages [3] -->
m

<!-- b000109 | furniture | pages [3] -->
m

<!-- b000110 | furniture | pages [3] -->
m

<!-- b000111 | furniture | pages [3] -->
m

<!-- b000112 | furniture | pages [3] -->
m

<!-- b000113 | furniture | pages [3] -->
m

<!-- b000114 | furniture | pages [3] -->
m

<!-- b000115 | furniture | pages [3] -->
m

<!-- b000116 | furniture | pages [3] -->
m

<!-- b000117 | furniture | pages [3] -->
m

<!-- b000118 | furniture | pages [3] -->
m

<!-- b000119 | furniture | pages [3] -->
m

<!-- b000120 | furniture | pages [3] -->
m

<!-- b000121 | furniture | pages [3] -->
m

<!-- b000122 | furniture | pages [3] -->
m

<!-- b000123 | furniture | pages [3] -->
m

<!-- b000124 | furniture | pages [3] -->
m

<!-- b000125 | furniture | pages [3] -->
m

<!-- b000126 | furniture | pages [3] -->
m

<!-- b000127 | furniture | pages [3] -->
m

<!-- b000128 | furniture | pages [3] -->
m

<!-- b000129 | furniture | pages [3] -->
m

<!-- b000130 | furniture | pages [3] -->
m

<!-- b000131 | furniture | pages [3] -->
m

<!-- b000132 | furniture | pages [3] -->
m

<!-- b000133 | furniture | pages [3] -->
m

<!-- b000134 | furniture | pages [3] -->
m

<!-- b000135 | furniture | pages [3] -->
m

<!-- b000136 | furniture | pages [3] -->
m

<!-- b000137 | furniture | pages [3] -->
m

<!-- b000138 | furniture | pages [3] -->
m

<!-- b000139 | furniture | pages [3] -->
m

<!-- b000140 | furniture | pages [3] -->
m

<!-- b000141 | furniture | pages [3] -->
m

<!-- b000142 | furniture | pages [3] -->
m

<!-- b000143 | furniture | pages [3] -->
m

<!-- b000144 | furniture | pages [3] -->
m

<!-- b000145 | furniture | pages [3] -->
m

<!-- b000146 | furniture | pages [3] -->
m

<!-- b000147 | furniture | pages [3] -->
m

<!-- b000148 | furniture | pages [3] -->
m

<!-- b000149 | furniture | pages [3] -->
m

<!-- b000150 | furniture | pages [3] -->
m

<!-- b000151 | furniture | pages [3] -->
m

<!-- b000152 | furniture | pages [3] -->
m

<!-- b000153 | furniture | pages [3] -->
m

<!-- b000154 | furniture | pages [3] -->
m

<!-- b000155 | furniture | pages [3] -->
m

<!-- b000156 | furniture | pages [3] -->
m

<!-- b000157 | furniture | pages [3] -->
m

<!-- b000158 | furniture | pages [3] -->
m

<!-- b000159 | furniture | pages [3] -->
m

<!-- b000160 | furniture | pages [3] -->
m

<!-- b000161 | furniture | pages [3] -->
m

<!-- b000162 | furniture | pages [3] -->
m

<!-- b000163 | furniture | pages [3] -->
m

<!-- b000164 | furniture | pages [3] -->
m

<!-- b000165 | furniture | pages [3] -->
m

<!-- b000166 | furniture | pages [3] -->
m

<!-- b000167 | furniture | pages [3] -->
m

<!-- b000168 | furniture | pages [3] -->
m

<!-- b000169 | furniture | pages [3] -->
m

<!-- b000170 | furniture | pages [3] -->
m

<!-- b000171 | furniture | pages [3] -->
m

<!-- b000172 | furniture | pages [3] -->
m

<!-- b000173 | furniture | pages [3] -->
m

<!-- b000174 | furniture | pages [3] -->
m

<!-- b000175 | furniture | pages [3] -->
m

<!-- b000176 | furniture | pages [3] -->
m

<!-- b000177 | furniture | pages [3] -->
m

<!-- b000178 | furniture | pages [3] -->
m

<!-- b000179 | furniture | pages [3] -->
m

<!-- b000180 | furniture | pages [3] -->
m

<!-- b000181 | furniture | pages [3] -->
m

<!-- b000182 | furniture | pages [3] -->
m

<!-- b000183 | furniture | pages [3] -->
m

<!-- b000184 | furniture | pages [3] -->
m

<!-- b000185 | furniture | pages [3] -->
m

<!-- b000186 | furniture | pages [3] -->
m

<!-- b000187 | furniture | pages [3] -->
m

<!-- b000188 | furniture | pages [3] -->
m

<!-- b000189 | furniture | pages [3] -->
m

<!-- b000190 | furniture | pages [3] -->
m

<!-- b000191 | furniture | pages [3] -->
m

<!-- b000192 | furniture | pages [3] -->
m

<!-- b000193 | furniture | pages [3] -->
m

<!-- b000194 | furniture | pages [3] -->
m

<!-- b000195 | furniture | pages [3] -->
m

<!-- b000196 | furniture | pages [3] -->
m

<!-- b000197 | furniture | pages [3] -->
m

<!-- b000198 | furniture | pages [3] -->
m

<!-- b000199 | furniture | pages [3] -->
m

<!-- b000200 | furniture | pages [3] -->
m

<!-- b000201 | furniture | pages [3] -->
m

<!-- b000202 | furniture | pages [3] -->
m

<!-- b000203 | furniture | pages [3] -->
m

<!-- b000204 | furniture | pages [3] -->
m

<!-- b000205 | furniture | pages [3] -->
m

<!-- b000206 | furniture | pages [3] -->
m

<!-- b000207 | furniture | pages [3] -->
m

<!-- b000208 | furniture | pages [3] -->
m

<!-- b000209 | furniture | pages [3] -->
m

<!-- b000210 | furniture | pages [3] -->
m

<!-- b000211 | furniture | pages [3] -->
m

<!-- b000212 | furniture | pages [3] -->
m

<!-- b000213 | furniture | pages [3] -->
m

<!-- b000214 | furniture | pages [3] -->
m

<!-- b000215 | furniture | pages [3] -->
m

<!-- b000216 | furniture | pages [3] -->
m

<!-- b000217 | furniture | pages [3] -->
m

<!-- b000218 | furniture | pages [3] -->
m

<!-- b000219 | furniture | pages [3] -->
m

<!-- b000220 | furniture | pages [3] -->
m

<!-- b000221 | furniture | pages [3] -->
m

<!-- b000222 | furniture | pages [3] -->
m

<!-- b000223 | furniture | pages [3] -->
m

<!-- b000224 | furniture | pages [3] -->
m

<!-- b000225 | furniture | pages [3] -->
m

<!-- b000226 | furniture | pages [3] -->
m

<!-- b000227 | furniture | pages [3] -->
m

<!-- b000228 | furniture | pages [3] -->
m

<!-- b000229 | furniture | pages [3] -->
m

<!-- b000230 | furniture | pages [3] -->
m

<!-- b000231 | furniture | pages [3] -->
m

<!-- b000232 | furniture | pages [3] -->
m

<!-- b000233 | furniture | pages [3] -->
m

<!-- b000234 | furniture | pages [3] -->
m

<!-- b000235 | furniture | pages [3] -->
m

<!-- b000236 | furniture | pages [3] -->
m

<!-- b000237 | furniture | pages [3] -->
m

<!-- b000238 | furniture | pages [3] -->
m

<!-- b000239 | furniture | pages [3] -->
m

<!-- b000240 | furniture | pages [3] -->
m

<!-- b000241 | furniture | pages [3] -->
m

<!-- b000242 | furniture | pages [3] -->
m

<!-- b000243 | furniture | pages [3] -->
m

<!-- b000244 | furniture | pages [3] -->
m

<!-- b000245 | furniture | pages [3] -->
m

<!-- b000246 | furniture | pages [3] -->
m

<!-- b000247 | furniture | pages [3] -->
m

<!-- b000248 | furniture | pages [3] -->
m

<!-- b000249 | furniture | pages [3] -->
m

<!-- b000250 | furniture | pages [3] -->
m

<!-- b000251 | furniture | pages [3] -->
m

<!-- b000252 | furniture | pages [3] -->
m

<!-- b000253 | furniture | pages [3] -->
m

<!-- b000254 | furniture | pages [3] -->
m

<!-- b000255 | furniture | pages [3] -->
m

<!-- b000256 | furniture | pages [3] -->
m

<!-- b000257 | furniture | pages [3] -->
m

<!-- b000258 | furniture | pages [3] -->
m

<!-- b000259 | furniture | pages [3] -->
m

<!-- b000260 | furniture | pages [3] -->
m

<!-- b000261 | furniture | pages [3] -->
m

<!-- b000262 | furniture | pages [3] -->
m

<!-- b000263 | furniture | pages [3] -->
m

<!-- b000264 | furniture | pages [3] -->
m

<!-- b000265 | furniture | pages [3] -->
m

<!-- b000266 | furniture | pages [3] -->
m

<!-- b000267 | furniture | pages [3] -->
m

<!-- b000268 | furniture | pages [3] -->
m

<!-- b000269 | furniture | pages [3] -->
m

<!-- b000270 | furniture | pages [3] -->
m

<!-- b000271 | furniture | pages [3] -->
m

<!-- b000272 | furniture | pages [3] -->
m

<!-- b000273 | furniture | pages [3] -->
m

<!-- b000274 | furniture | pages [3] -->
m

<!-- b000275 | furniture | pages [3] -->
m

<!-- b000276 | furniture | pages [3] -->
m

<!-- b000277 | furniture | pages [3] -->
m

<!-- b000278 | furniture | pages [3] -->
m

<!-- b000279 | furniture | pages [3] -->
m

<!-- b000280 | furniture | pages [3] -->
m

<!-- b000281 | furniture | pages [3] -->
m

<!-- b000282 | furniture | pages [3] -->
m

<!-- b000283 | furniture | pages [3] -->
m

<!-- b000284 | furniture | pages [3] -->
m

<!-- b000285 | furniture | pages [3] -->
m

<!-- b000286 | furniture | pages [3] -->
m

<!-- b000287 | furniture | pages [3] -->
m

<!-- b000288 | furniture | pages [3] -->
m

<!-- b000289 | furniture | pages [3] -->
m

<!-- b000290 | furniture | pages [3] -->
m

<!-- b000291 | furniture | pages [3] -->
m

<!-- b000292 | furniture | pages [3] -->
m

<!-- b000293 | furniture | pages [3] -->
m

<!-- b000294 | furniture | pages [3] -->
m

<!-- b000295 | furniture | pages [3] -->
m

<!-- b000296 | furniture | pages [3] -->
m

<!-- b000297 | furniture | pages [3] -->
m

<!-- b000298 | furniture | pages [3] -->
m

<!-- b000299 | furniture | pages [3] -->
m

<!-- b000300 | furniture | pages [3] -->
m

<!-- b000301 | furniture | pages [3] -->
m

<!-- b000302 | furniture | pages [3] -->
m

<!-- b000303 | furniture | pages [3] -->
m

<!-- b000304 | furniture | pages [3] -->
m

<!-- b000305 | furniture | pages [3] -->
m

<!-- b000306 | furniture | pages [3] -->
m

<!-- b000307 | furniture | pages [3] -->
m

<!-- b000308 | furniture | pages [3] -->
m

<!-- b000309 | furniture | pages [3] -->
m

<!-- b000310 | furniture | pages [3] -->
m

<!-- b000311 | furniture | pages [3] -->
m

<!-- b000312 | furniture | pages [3] -->
m

<!-- b000313 | furniture | pages [3] -->
m

<!-- b000314 | furniture | pages [3] -->
m

<!-- b000315 | furniture | pages [3] -->
m

<!-- b000316 | furniture | pages [3] -->
m

<!-- b000317 | furniture | pages [3] -->
m

<!-- b000318 | furniture | pages [3] -->
m

<!-- b000319 | furniture | pages [3] -->
m

<!-- b000320 | furniture | pages [3] -->
m

<!-- b000321 | furniture | pages [3] -->
m

<!-- b000322 | furniture | pages [3] -->
m

<!-- b000323 | furniture | pages [3] -->
m

<!-- b000324 | furniture | pages [3] -->
m

<!-- b000325 | furniture | pages [3] -->
m

<!-- b000326 | furniture | pages [3] -->
m

<!-- b000327 | furniture | pages [3] -->
m

<!-- b000328 | furniture | pages [3] -->
m

<!-- b000329 | furniture | pages [3] -->
m

<!-- b000330 | furniture | pages [3] -->
m

<!-- b000331 | furniture | pages [3] -->
m

<!-- b000332 | furniture | pages [3] -->
m

<!-- b000333 | furniture | pages [3] -->
m

<!-- b000334 | furniture | pages [3] -->
m

<!-- b000335 | furniture | pages [3] -->
m

<!-- b000336 | furniture | pages [3] -->
m

<!-- b000337 | furniture | pages [3] -->
m

<!-- b000338 | furniture | pages [3] -->
m

<!-- b000339 | furniture | pages [3] -->
m

<!-- b000340 | furniture | pages [3] -->
m

<!-- b000341 | furniture | pages [3] -->
m

<!-- b000342 | furniture | pages [3] -->
m

<!-- b000343 | furniture | pages [3] -->
m

<!-- b000344 | furniture | pages [3] -->
m

<!-- b000345 | furniture | pages [3] -->
m

<!-- b000346 | furniture | pages [3] -->
m

<!-- b000347 | furniture | pages [3] -->
m

<!-- b000348 | furniture | pages [3] -->
m

<!-- b000349 | furniture | pages [3] -->
m

<!-- b000350 | furniture | pages [3] -->
m

<!-- b000351 | furniture | pages [3] -->
m

<!-- b000352 | furniture | pages [3] -->
m

<!-- b000353 | furniture | pages [3] -->
m

<!-- b000354 | furniture | pages [3] -->
m

<!-- b000355 | furniture | pages [3] -->
m

<!-- b000356 | furniture | pages [3] -->
m

<!-- b000357 | furniture | pages [3] -->
m

<!-- b000358 | furniture | pages [3] -->
m

<!-- b000359 | furniture | pages [3] -->
m

<!-- b000360 | furniture | pages [3] -->
m

<!-- b000361 | furniture | pages [3] -->
m

<!-- b000362 | furniture | pages [3] -->
m

<!-- b000363 | furniture | pages [3] -->
m

<!-- b000364 | furniture | pages [3] -->
m

<!-- b000365 | furniture | pages [3] -->
m

<!-- b000366 | furniture | pages [3] -->
m

<!-- b000367 | furniture | pages [3] -->
m

<!-- b000368 | furniture | pages [3] -->
m

<!-- b000369 | furniture | pages [3] -->
m

<!-- b000370 | furniture | pages [3] -->
m

<!-- b000371 | furniture | pages [3] -->
m

<!-- b000372 | furniture | pages [3] -->
m

<!-- b000373 | furniture | pages [3] -->
m

<!-- b000374 | furniture | pages [3] -->
m

<!-- b000375 | furniture | pages [3] -->
m

<!-- b000376 | furniture | pages [3] -->
m

<!-- b000377 | furniture | pages [3] -->
m

<!-- b000378 | furniture | pages [3] -->
m

<!-- b000379 | furniture | pages [3] -->
m

<!-- b000380 | furniture | pages [3] -->
m

<!-- b000381 | furniture | pages [3] -->
m

<!-- b000382 | furniture | pages [3] -->
m

<!-- b000383 | furniture | pages [3] -->
m

<!-- b000384 | furniture | pages [3] -->
m

<!-- b000385 | furniture | pages [3] -->
m

<!-- b000386 | furniture | pages [3] -->
m

<!-- b000387 | furniture | pages [3] -->
m

<!-- b000388 | furniture | pages [3] -->
m

<!-- b000389 | furniture | pages [3] -->
m

<!-- b000390 | furniture | pages [3] -->
m

<!-- b000391 | furniture | pages [3] -->
m

<!-- b000392 | furniture | pages [3] -->
m

<!-- b000393 | furniture | pages [3] -->
m

<!-- b000394 | furniture | pages [3] -->
m

<!-- b000395 | furniture | pages [3] -->
m

<!-- b000396 | furniture | pages [3] -->
m

<!-- b000397 | furniture | pages [3] -->
m

<!-- b000398 | furniture | pages [3] -->
m

<!-- b000399 | furniture | pages [3] -->
m

<!-- b000400 | furniture | pages [3] -->
m

<!-- b000401 | furniture | pages [3] -->
m

<!-- b000402 | furniture | pages [3] -->
m

<!-- b000403 | furniture | pages [3] -->
m

<!-- b000404 | furniture | pages [3] -->
m

<!-- b000405 | furniture | pages [3] -->
m

<!-- b000406 | furniture | pages [3] -->
m

<!-- b000407 | furniture | pages [3] -->
m

<!-- b000408 | furniture | pages [4] -->
Team # 2500836                                                                   Page 3 of 25

<!-- b000410 | heading | pages [4] -->
1.3  Our Work

<!-- b000411 | prose | pages [4] -->
In this paper, we carried out the following work to study stair usage frequency, service life, current condition, and pedestrian behavior patterns when using the stairs. ➢ Task 1: Model Preparation Firstly, we determined the material and environmental conditions of the stairs to be studied. Then, computer vision techniques were employed to obtain and process the data, followed by fitting the wear depth distribution on the stair surface. ➢ Task 2: Stair Wear Analysis Model We chose pedestrian traffic, represented by the number of people using the stairs daily, to characterize the stair usage frequency. Since the distribution of wear depth is known, the daily pedestrian traffic could be calculated based on the relationship between wear depth and pedestrian flow. Then, by considering people's typical force application habits when ascending and descending stairs, the changes in wear depth distribution on the stair surface could be used to infer their preferred walking direction. Finally, the pedestrian density during stair usage was calculated from the traffic flow, allowing us to determine whether people walk individually or side by side. ➢ Task 3:

<!-- b000412 | prose | pages [4] -->
⚫ To analyze the usage condition and material characteristics of the stairs, we established the relationship between stair age and pedestrian traffic based on the study of wear depth distribution.

<!-- b000413 | prose | pages [4] -->
⚫ Based on the relationship between wear depth and pedestrian traffic from Task 1, we calculated the theoretical wear depth and compared it with the actual data. An error analysis was then conducted to assess the accuracy.

<!-- b000414 | prose | pages [4] -->
⚫ Using the known relationship between wear depth, pedestrian traffic, and stair age, we input the actual wear depth and pedestrian traffic data to calculate the stair age, and then determine the error between theoretical and actual values to assess the accuracy.

<!-- b000415 | prose | pages [4] -->
⚫ To determine whether the stairs have been repaired or renovated, we can compare the theoretical stair age with the actual difference, observe changes in the wear coefficient, and use chemical methods for verification.

<!-- b000416 | prose | pages [4] -->
⚫ To address the final issue, we first selected several representative feature parameters of stair materials, compared them with the features of the stairs, and analyzed their correlation. When analyzing the pedestrian traffic on a specific day, we established a partial differential equation to analyze the instantaneous changes in traffic, thereby determining whether pedestrians use the stairs in a short-term peak or with a uniform distribution over a longer period.

<!-- b000417 | prose | pages [4] -->
Our work aims to gain a deeper understanding of the dynamics of stair usage and the impacts of varying pedestrian flow patterns. In summary, the entire modeling process can be outlined as follows:

<!-- b000418 | prose | pages [4] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 关注数学模型 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000419 | furniture | pages [4] -->
2

<!-- b000420 | furniture | pages [4] -->
m

<!-- b000421 | furniture | pages [4] -->
m

<!-- b000422 | furniture | pages [4] -->
m

<!-- b000423 | furniture | pages [4] -->
m

<!-- b000424 | furniture | pages [4] -->
m

<!-- b000425 | furniture | pages [4] -->
m

<!-- b000426 | furniture | pages [4] -->
m

<!-- b000427 | furniture | pages [4] -->
m

<!-- b000428 | furniture | pages [4] -->
m

<!-- b000429 | furniture | pages [4] -->
m

<!-- b000430 | furniture | pages [4] -->
m

<!-- b000431 | furniture | pages [4] -->
m

<!-- b000432 | furniture | pages [4] -->
m

<!-- b000433 | furniture | pages [4] -->
m

<!-- b000434 | furniture | pages [4] -->
m

<!-- b000435 | furniture | pages [4] -->
m

<!-- b000436 | furniture | pages [4] -->
m

<!-- b000437 | furniture | pages [4] -->
m

<!-- b000438 | furniture | pages [4] -->
m

<!-- b000439 | furniture | pages [4] -->
m

<!-- b000440 | furniture | pages [4] -->
m

<!-- b000441 | furniture | pages [4] -->
m

<!-- b000442 | furniture | pages [4] -->
m

<!-- b000443 | furniture | pages [4] -->
m

<!-- b000444 | furniture | pages [4] -->
m

<!-- b000445 | furniture | pages [4] -->
m

<!-- b000446 | furniture | pages [4] -->
m

<!-- b000447 | furniture | pages [4] -->
m

<!-- b000448 | furniture | pages [4] -->
m

<!-- b000449 | furniture | pages [4] -->
m

<!-- b000450 | furniture | pages [4] -->
m

<!-- b000451 | furniture | pages [4] -->
m

<!-- b000452 | furniture | pages [4] -->
m

<!-- b000453 | furniture | pages [4] -->
m

<!-- b000454 | furniture | pages [4] -->
m

<!-- b000455 | furniture | pages [4] -->
m

<!-- b000456 | furniture | pages [4] -->
m

<!-- b000457 | furniture | pages [4] -->
m

<!-- b000458 | furniture | pages [4] -->
m

<!-- b000459 | furniture | pages [4] -->
m

<!-- b000460 | furniture | pages [4] -->
m

<!-- b000461 | furniture | pages [4] -->
m

<!-- b000462 | furniture | pages [4] -->
m

<!-- b000463 | furniture | pages [4] -->
m

<!-- b000464 | furniture | pages [4] -->
m

<!-- b000465 | furniture | pages [4] -->
m

<!-- b000466 | furniture | pages [4] -->
m

<!-- b000467 | furniture | pages [4] -->
m

<!-- b000468 | furniture | pages [4] -->
m

<!-- b000469 | furniture | pages [4] -->
m

<!-- b000470 | furniture | pages [4] -->
m

<!-- b000471 | furniture | pages [4] -->
m

<!-- b000472 | furniture | pages [4] -->
m

<!-- b000473 | furniture | pages [4] -->
m

<!-- b000474 | furniture | pages [4] -->
m

<!-- b000475 | furniture | pages [4] -->
m

<!-- b000476 | furniture | pages [4] -->
m

<!-- b000477 | furniture | pages [4] -->
m

<!-- b000478 | furniture | pages [4] -->
m

<!-- b000479 | furniture | pages [4] -->
m

<!-- b000480 | furniture | pages [4] -->
m

<!-- b000481 | furniture | pages [4] -->
m

<!-- b000482 | furniture | pages [4] -->
m

<!-- b000483 | furniture | pages [4] -->
m

<!-- b000484 | furniture | pages [4] -->
m

<!-- b000485 | furniture | pages [4] -->
m

<!-- b000486 | furniture | pages [4] -->
m

<!-- b000487 | furniture | pages [4] -->
m

<!-- b000488 | furniture | pages [4] -->
m

<!-- b000489 | furniture | pages [4] -->
m

<!-- b000490 | furniture | pages [4] -->
m

<!-- b000491 | furniture | pages [4] -->
m

<!-- b000492 | furniture | pages [4] -->
m

<!-- b000493 | furniture | pages [4] -->
m

<!-- b000494 | furniture | pages [4] -->
m

<!-- b000495 | furniture | pages [4] -->
m

<!-- b000496 | furniture | pages [4] -->
m

<!-- b000497 | furniture | pages [4] -->
m

<!-- b000498 | furniture | pages [4] -->
m

<!-- b000499 | furniture | pages [4] -->
m

<!-- b000500 | furniture | pages [4] -->
m

<!-- b000501 | furniture | pages [4] -->
m

<!-- b000502 | furniture | pages [4] -->
m

<!-- b000503 | furniture | pages [4] -->
m

<!-- b000504 | furniture | pages [4] -->
m

<!-- b000505 | furniture | pages [4] -->
m

<!-- b000506 | furniture | pages [4] -->
m

<!-- b000507 | furniture | pages [4] -->
m

<!-- b000508 | furniture | pages [4] -->
m

<!-- b000509 | furniture | pages [4] -->
m

<!-- b000510 | furniture | pages [4] -->
m

<!-- b000511 | furniture | pages [4] -->
m

<!-- b000512 | furniture | pages [4] -->
m

<!-- b000513 | furniture | pages [4] -->
m

<!-- b000514 | furniture | pages [4] -->
m

<!-- b000515 | furniture | pages [4] -->
m

<!-- b000516 | furniture | pages [4] -->
m

<!-- b000517 | furniture | pages [4] -->
m

<!-- b000518 | furniture | pages [4] -->
m

<!-- b000519 | furniture | pages [4] -->
m

<!-- b000520 | furniture | pages [4] -->
m

<!-- b000521 | furniture | pages [4] -->
m

<!-- b000522 | furniture | pages [4] -->
m

<!-- b000523 | furniture | pages [4] -->
m

<!-- b000524 | furniture | pages [4] -->
m

<!-- b000525 | furniture | pages [4] -->
m

<!-- b000526 | furniture | pages [4] -->
m

<!-- b000527 | furniture | pages [4] -->
m

<!-- b000528 | furniture | pages [4] -->
m

<!-- b000529 | furniture | pages [4] -->
m

<!-- b000530 | furniture | pages [4] -->
m

<!-- b000531 | furniture | pages [4] -->
MATHmodels

<!-- b000532 | furniture | pages [4] -->
获取更多资讯

<!-- b000533 | furniture | pages [4] -->
m

<!-- b000534 | furniture | pages [4] -->
m

<!-- b000535 | furniture | pages [4] -->
m

<!-- b000536 | furniture | pages [4] -->
m

<!-- b000537 | furniture | pages [4] -->
m

<!-- b000538 | furniture | pages [4] -->
m

<!-- b000539 | furniture | pages [4] -->
m

<!-- b000540 | furniture | pages [4] -->
m

<!-- b000541 | furniture | pages [4] -->
m

<!-- b000542 | furniture | pages [4] -->
m

<!-- b000543 | furniture | pages [4] -->
m

<!-- b000544 | furniture | pages [4] -->
m

<!-- b000545 | furniture | pages [4] -->
m

<!-- b000546 | furniture | pages [4] -->
m

<!-- b000547 | furniture | pages [4] -->
m

<!-- b000548 | furniture | pages [4] -->
m

<!-- b000549 | furniture | pages [4] -->
m

<!-- b000550 | furniture | pages [4] -->
m

<!-- b000551 | furniture | pages [4] -->
m

<!-- b000552 | furniture | pages [4] -->
m

<!-- b000553 | furniture | pages [4] -->
m

<!-- b000554 | furniture | pages [4] -->
m

<!-- b000555 | furniture | pages [4] -->
m

<!-- b000556 | furniture | pages [4] -->
m

<!-- b000557 | furniture | pages [4] -->
m

<!-- b000558 | furniture | pages [4] -->
m

<!-- b000559 | furniture | pages [4] -->
m

<!-- b000560 | furniture | pages [4] -->
m

<!-- b000561 | furniture | pages [4] -->
m

<!-- b000562 | furniture | pages [4] -->
m

<!-- b000563 | furniture | pages [4] -->
m

<!-- b000564 | furniture | pages [4] -->
m

<!-- b000565 | furniture | pages [4] -->
m

<!-- b000566 | furniture | pages [4] -->
m

<!-- b000567 | furniture | pages [4] -->
m

<!-- b000568 | furniture | pages [4] -->
m

<!-- b000569 | furniture | pages [4] -->
m

<!-- b000570 | furniture | pages [4] -->
m

<!-- b000571 | furniture | pages [4] -->
m

<!-- b000572 | furniture | pages [4] -->
m

<!-- b000573 | furniture | pages [4] -->
m

<!-- b000574 | furniture | pages [4] -->
m

<!-- b000575 | furniture | pages [4] -->
m

<!-- b000576 | furniture | pages [4] -->
m

<!-- b000577 | furniture | pages [4] -->
m

<!-- b000578 | furniture | pages [4] -->
m

<!-- b000579 | furniture | pages [4] -->
m

<!-- b000580 | furniture | pages [4] -->
m

<!-- b000581 | furniture | pages [4] -->
m

<!-- b000582 | furniture | pages [4] -->
m

<!-- b000583 | furniture | pages [4] -->
m

<!-- b000584 | furniture | pages [4] -->
m

<!-- b000585 | furniture | pages [4] -->
m

<!-- b000586 | furniture | pages [4] -->
m

<!-- b000587 | furniture | pages [4] -->
m

<!-- b000588 | furniture | pages [4] -->
m

<!-- b000589 | furniture | pages [4] -->
m

<!-- b000590 | furniture | pages [4] -->
m

<!-- b000591 | furniture | pages [4] -->
m

<!-- b000592 | furniture | pages [4] -->
m

<!-- b000593 | furniture | pages [4] -->
m

<!-- b000594 | furniture | pages [4] -->
m

<!-- b000595 | furniture | pages [4] -->
m

<!-- b000596 | furniture | pages [4] -->
m

<!-- b000597 | furniture | pages [4] -->
m

<!-- b000598 | furniture | pages [4] -->
m

<!-- b000599 | furniture | pages [4] -->
m

<!-- b000600 | furniture | pages [4] -->
m

<!-- b000601 | furniture | pages [4] -->
m

<!-- b000602 | furniture | pages [4] -->
m

<!-- b000603 | furniture | pages [4] -->
m

<!-- b000604 | furniture | pages [4] -->
m

<!-- b000605 | furniture | pages [4] -->
m

<!-- b000606 | furniture | pages [4] -->
m

<!-- b000607 | furniture | pages [4] -->
m

<!-- b000608 | furniture | pages [4] -->
m

<!-- b000609 | furniture | pages [4] -->
m

<!-- b000610 | furniture | pages [4] -->
m

<!-- b000611 | furniture | pages [4] -->
m

<!-- b000612 | furniture | pages [4] -->
m

<!-- b000613 | furniture | pages [4] -->
m

<!-- b000614 | furniture | pages [4] -->
m

<!-- b000615 | furniture | pages [4] -->
m

<!-- b000616 | furniture | pages [4] -->
m

<!-- b000617 | furniture | pages [4] -->
m

<!-- b000618 | furniture | pages [4] -->
m

<!-- b000619 | furniture | pages [4] -->
m

<!-- b000620 | furniture | pages [4] -->
m

<!-- b000621 | furniture | pages [4] -->
m

<!-- b000622 | furniture | pages [4] -->
m

<!-- b000623 | furniture | pages [4] -->
m

<!-- b000624 | furniture | pages [4] -->
m

<!-- b000625 | furniture | pages [4] -->
m

<!-- b000626 | furniture | pages [4] -->
m

<!-- b000627 | furniture | pages [4] -->
m

<!-- b000628 | furniture | pages [4] -->
m

<!-- b000629 | furniture | pages [4] -->
m

<!-- b000630 | furniture | pages [4] -->
m

<!-- b000631 | furniture | pages [4] -->
m

<!-- b000632 | furniture | pages [4] -->
m

<!-- b000633 | furniture | pages [4] -->
m

<!-- b000634 | furniture | pages [4] -->
m

<!-- b000635 | furniture | pages [4] -->
m

<!-- b000636 | furniture | pages [4] -->
m

<!-- b000637 | furniture | pages [4] -->
m

<!-- b000638 | furniture | pages [4] -->
m

<!-- b000639 | furniture | pages [4] -->
m

<!-- b000640 | furniture | pages [4] -->
m

<!-- b000641 | furniture | pages [4] -->
m

<!-- b000642 | furniture | pages [4] -->
m

<!-- b000643 | furniture | pages [4] -->
m

<!-- b000644 | furniture | pages [4] -->
m

<!-- b000645 | furniture | pages [4] -->
m

<!-- b000646 | furniture | pages [4] -->
m

<!-- b000647 | furniture | pages [4] -->
m

<!-- b000648 | furniture | pages [4] -->
m

<!-- b000649 | furniture | pages [4] -->
m

<!-- b000650 | furniture | pages [4] -->
m

<!-- b000651 | furniture | pages [4] -->
m

<!-- b000652 | furniture | pages [4] -->
m

<!-- b000653 | furniture | pages [4] -->
m

<!-- b000654 | furniture | pages [4] -->
m

<!-- b000655 | furniture | pages [4] -->
m

<!-- b000656 | furniture | pages [4] -->
m

<!-- b000657 | furniture | pages [4] -->
m

<!-- b000658 | furniture | pages [4] -->
m

<!-- b000659 | furniture | pages [4] -->
m

<!-- b000660 | furniture | pages [4] -->
m

<!-- b000661 | furniture | pages [4] -->
m

<!-- b000662 | furniture | pages [4] -->
m

<!-- b000663 | furniture | pages [4] -->
m

<!-- b000664 | furniture | pages [4] -->
m

<!-- b000665 | furniture | pages [4] -->
m

<!-- b000666 | furniture | pages [4] -->
m

<!-- b000667 | furniture | pages [4] -->
m

<!-- b000668 | furniture | pages [4] -->
m

<!-- b000669 | furniture | pages [4] -->
m

<!-- b000670 | furniture | pages [4] -->
m

<!-- b000671 | furniture | pages [4] -->
m

<!-- b000672 | furniture | pages [4] -->
m

<!-- b000673 | furniture | pages [4] -->
m

<!-- b000674 | furniture | pages [4] -->
m

<!-- b000675 | furniture | pages [4] -->
m

<!-- b000676 | furniture | pages [4] -->
m

<!-- b000677 | furniture | pages [4] -->
m

<!-- b000678 | furniture | pages [4] -->
m

<!-- b000679 | furniture | pages [4] -->
m

<!-- b000680 | furniture | pages [4] -->
m

<!-- b000681 | furniture | pages [4] -->
m

<!-- b000682 | furniture | pages [4] -->
m

<!-- b000683 | furniture | pages [4] -->
m

<!-- b000684 | furniture | pages [4] -->
m

<!-- b000685 | furniture | pages [4] -->
m

<!-- b000686 | furniture | pages [4] -->
m

<!-- b000687 | furniture | pages [4] -->
m

<!-- b000688 | furniture | pages [4] -->
m

<!-- b000689 | furniture | pages [4] -->
m

<!-- b000690 | furniture | pages [4] -->
m

<!-- b000691 | furniture | pages [4] -->
m

<!-- b000692 | furniture | pages [4] -->
m

<!-- b000693 | furniture | pages [4] -->
m

<!-- b000694 | furniture | pages [4] -->
m

<!-- b000695 | furniture | pages [4] -->
m

<!-- b000696 | furniture | pages [4] -->
m

<!-- b000697 | furniture | pages [4] -->
m

<!-- b000698 | furniture | pages [4] -->
m

<!-- b000699 | furniture | pages [4] -->
m

<!-- b000700 | furniture | pages [4] -->
m

<!-- b000701 | furniture | pages [4] -->
m

<!-- b000702 | furniture | pages [4] -->
m

<!-- b000703 | furniture | pages [4] -->
m

<!-- b000704 | furniture | pages [4] -->
m

<!-- b000705 | furniture | pages [4] -->
m

<!-- b000706 | furniture | pages [4] -->
m

<!-- b000707 | furniture | pages [4] -->
m

<!-- b000708 | furniture | pages [4] -->
m

<!-- b000709 | furniture | pages [4] -->
m

<!-- b000710 | furniture | pages [4] -->
m

<!-- b000711 | furniture | pages [4] -->
m

<!-- b000712 | furniture | pages [4] -->
m

<!-- b000713 | furniture | pages [4] -->
m

<!-- b000714 | furniture | pages [4] -->
m

<!-- b000715 | furniture | pages [4] -->
m

<!-- b000716 | furniture | pages [4] -->
m

<!-- b000717 | furniture | pages [4] -->
m

<!-- b000718 | furniture | pages [4] -->
m

<!-- b000719 | furniture | pages [4] -->
m

<!-- b000720 | furniture | pages [4] -->
m

<!-- b000721 | furniture | pages [4] -->
m

<!-- b000722 | furniture | pages [4] -->
m

<!-- b000723 | furniture | pages [4] -->
m

<!-- b000724 | furniture | pages [4] -->
m

<!-- b000725 | furniture | pages [4] -->
m

<!-- b000726 | furniture | pages [4] -->
m

<!-- b000727 | furniture | pages [4] -->
m

<!-- b000728 | furniture | pages [4] -->
m

<!-- b000729 | furniture | pages [4] -->
m

<!-- b000730 | furniture | pages [4] -->
m

<!-- b000731 | furniture | pages [4] -->
m

<!-- b000732 | furniture | pages [4] -->
m

<!-- b000733 | furniture | pages [4] -->
m

<!-- b000734 | furniture | pages [4] -->
m

<!-- b000735 | furniture | pages [4] -->
m

<!-- b000736 | furniture | pages [4] -->
m

<!-- b000737 | furniture | pages [4] -->
m

<!-- b000738 | furniture | pages [5] -->
Page 4 of 25

<!-- b000739 | furniture | pages [5] -->
Team # 2500836

<!-- b000740 | heading | pages [5] -->
Sensitivity

<!-- b000741 | prose | pages [5] -->
Preparation Model Establishment Analtsis

<!-- b000742 | prose | pages [5] -->
Detailed Workflow

<!-- b000743 | heading | pages [5] -->
Sensitivity

<!-- b000744 | prose | pages [5] -->
Preparation Model I: Step Wear Analysis Model Analysis 1. Pedestrian Flow Calculation based on Archard's Law Identify the research 2. Preference Direction Model Based on Wear Depth Distribution subject: internal 3. Walking Patterns Model based on Navier-Stokes Equations 勺 stairs of the Leaning 2-D normal distribution model Tower of Pisa finite difference of wear depth

<!-- b000745 | prose | pages [5] -->
Data extraction: changing parameters CV method A 1. Comparison of Actual and Theoretical robust? Model II: Stair Usage Time Monte Carlo simulation Step 4 2. Calculation of Stair Service Life Characteristic Determine the wear Analysis 3. Determination of Stair Renovation depth distribution: Continuity equation 4. Determination of Material Source Model 2-D normal for simulating 5. Research on temporal distribution of distribution pedestrian flow the Pedestrian Flow Person correlation analysis PSO algorithm

<!-- b000746 | caption | pages [5] -->
Figure 2: Flowchart of our work

<!-- b000747 | heading | pages [5] -->
Assumptions and Justifications

<!-- b000748 | prose | pages [5] -->
2

<!-- b000749 | prose | pages [5] -->
To simplify the problem, we make the following basic assumptions, each of which is properly justified.

<!-- b000750 | prose | pages [5] -->
Assumption 1: Assuming that an archaeologist has access to the structure in question and can obtain whatever measurement your team believes is important.

<!-- b000751 | prose | pages [5] -->
Assumption 2: Assuming that the friction coefficient between the soles of the shoes and the steps is equal.

<!-- b000752 | prose | pages [5] -->
Justification: This assumption presumes that everyone is wearing shoes of the same type, material, and similar wear and tear, thus maintaining a consistent friction coefficient between the soles and the steps. In reality, the friction coefficient may be affected by factors such as the material of the shoe sole (e.g., rubber, leather, plastic, etc.), the surface texture (e.g., patterns on the sole), and the degree of wear. However, to simplify the derivation process of the model, it is assumed that the friction coefficient is the same, which can avoid excessive variable interference in calculations.

<!-- b000753 | prose | pages [5] -->
Assumption 3: Assuming that all people have equal pressure on the step.

<!-- b000754 | prose | pages [5] -->
Justification: This assumption is based on the premise that individuals have similar body weights and consistent walking patterns, resulting in small differences in gait, footfall, and other aspects, leading to roughly equal pressure on the steps by each person. In reality, the magnitude of pressure is not only related to individual body weight but is also influenced by factors such as walking posture, stride length, foot position, and changes in the center of gravity during stair climbing and descending. However, to simplify the model analysis and make it easy to solve, we make this assumption.

<!-- b000755 | prose | pages [5] -->
Assumption 4: Assuming that the relative friction distance between the soles and the steps is equal for everyone.

<!-- b000756 | prose | pages [5, 6] -->
Justification: Assuming that stride length, walking speed, and step frequency remain consistent across individuals, the relative friction distance between the soles and the steps is uniform. However, in reality, these factors can vary significantly due to individual differences. For instance, a person with a longer stride may experience shorter contact time with the steps, potentially leading to a reduced friction distance. Additionally, the size of the relative friction distance is influenced by the rhythm of the steps and the center of gravity. This assumption ignores the minor variations caused by individual differences, making the model calculation more concise and easier to analyze.

<!-- b000757 | furniture | pages [6] -->
Team # 2500836                                                                   Page 5 of 25

<!-- b000759 | heading | pages [6] -->
3 Notations

<!-- b000760 | prose | pages [6] -->
The key mathematical notations used in this paper are listed in Table 1.

<!-- b000761 | caption | pages [6] -->
Table 1: Notations used in this paper

<!-- b000762 | heading | pages [6] -->
Symbols

<!-- b000763 | prose | pages [6] -->
Definition Units The wear depth at each location (x, y)

<!-- b000764 | prose | pages [6] -->
Pedestrian flow Wear coefficients (also called Archard’s constant) / The time since the steps were completed The width of the steps The length of the steps The area of the i-th step The total number of steps / The pedestrian density The velocity vector of pedestrians The flux divergence, / ∇⋅(ρv) Experience factor / *There are some variables that are not listed here and will be discussed in detail below.

<!-- b000765 | heading | pages [6] -->
4 Model Preparation

<!-- b000766 | heading | pages [6] -->
4.1 Data Processing

<!-- b000767 | prose | pages [6] -->
We selected one of the typical ancient architectural steps, the steps inside the Leaning Tower of Pisa in Italy.

<!-- b000768 | prose | pages [6] -->
To extract more accurate images, we used computer vision technology to process the images. ⚫ Step 1: Image processing The original images were first transformed into grayscale images, then the images were denoised using Gaussian filtering.

<!-- b000769 | prose | pages [6] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m a. Original image b. grayscale image c. Gaussian denoising m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000770 | caption | pages [6] -->
Figure 3: Image processing

<!-- b000771 | prose | pages [6] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000772 | prose | pages [6, 7] -->
关注数学模型 ⚫ Step 2: Feature extraction Then, the edge detection was performed to extract the image feature information. ⚫

<!-- b000773 | furniture | pages [6] -->
2

<!-- b000774 | furniture | pages [6] -->
MATHmodels

<!-- b000775 | furniture | pages [6] -->
获取更多资讯

<!-- b000776 | furniture | pages [7] -->
Team # 2500836                                                                   Page 6 of 25

<!-- b000778 | heading | pages [7] -->
Step 3: Data processing

<!-- b000779 | prose | pages [7] -->
Next, the data was processed, and the step with the best processing effect was selected. We found that the bottom step in the example figure was the best, and studied it further.

<!-- b000780 | prose | pages [7] -->
微信公众号：数学模型

<!-- b000781 | caption | pages [7] -->
Figure 4: Step with the best processing effect

<!-- b000782 | prose | pages [7] -->
⚫ Step 4: Data visualization Finally, we visualized the processed data by drawing a three-dimensional image.

<!-- b000783 | prose | pages [7] -->
微信号：MATHmodels a. Aerial view                          b. Side view

<!-- b000784 | caption | pages [7] -->
Figure 5: A processed three-dimensional image

<!-- b000785 | prose | pages [7] -->
It is obvious from the figure that the edge of the step is seriously worn, with obvious depression, while the inside of the step is smaller.

<!-- b000786 | heading | pages [7] -->
4.2 Solution of the Wear Depth Distribution

<!-- b000787 | prose | pages [7] -->
Observation reveals that the steps are not uniformly worn but exhibit a concave state, with the central area being more severely indented than the sides. Considering that people tend to step within a certain range when walking on the steps, and taking into account the habits and force distribution of people's footsteps while going up and down the stairs, theoretically, the steps that have been used for a long time would develop two indentations, as each foot lands in a different position, forming one indentation on each side. In practice, these two indentations are almost identical. Therefore, we simplify the model and only study one indentation. To simplify the analysis, we only consider the case of a single person walking, then there is only one center of wear, resulting in the wear distribution of the steps taking the form of a two-dimensional normal distribution.

<!-- b000788 | prose | pages [7] -->
(1)

<!-- b000789 | prose | pages [7] -->
We took the midpoint of the outer edge line of the bottom surface of the steps as the origin and established a three-dimensional Cartesian coordinate system as shown in the figure below.

<!-- b000790 | furniture | pages [8] -->
Page 7 of 25

<!-- b000791 | furniture | pages [8] -->
Team # 2500836

<!-- b000792 | prose | pages [8] -->
z

<!-- b000793 | prose | pages [8] -->
y

<!-- b000794 | prose | pages [8] -->
x 0

<!-- b000795 | caption | pages [8] -->
Figure 6: 3-D Cartesian coordinate system

<!-- b000796 | prose | pages [8] -->
Then, we used the Particle Swarm Optimization (PSO) algorithm to fit the parameters. The PSO algorithm is used to minimize the objective function defined above. PSO is a global optimization algorithm suitable for finding the optimal solution to complex, multi-dimensional optimization problems. In this context, the role of PSO is to search the parameter space to find the combination of parameters that minimizes the objective function value defined by the least squares method.

<!-- b000797 | prose | pages [8] -->
Step 1: Initialization – Randomly generate a group of particles, specifying the number of particles, inertia weight (typically 0.8), learning factor 1 (usually 2), learning factor 2 (usually 2), the search range forρ, µ1, µ2, σ1, σ2, the number of iterations, and the number of variables.

<!-- b000798 | prose | pages [8] -->
Step 2: Evaluation – Calculate the fitness of each particle, which corresponds to the objective function value. The optimization goal is: min ∑(di− di)² i Step 3: Update Best Position – Compare each particle's current position with its historical best position and update both the individual best position and the global best position.

<!-- b000799 | prose | pages [8] -->
Step 4: Update Velocity and Position – Based on the individual best position, global best position, and certain weights and random factors, update the particle's velocity and position.

<!-- b000800 | prose | pages [8] -->
Step 5: Termination Condition Check – Check if the stopping criteria are met, such as reaching the maximum number of iterations or the objective function value meeting the requirements. If the stopping criteria are not met, repeat Steps 3 to 5 until the termination condition is satisfied.

<!-- b000801 | prose | pages [8] -->
Based on the data obtained from the scanned pictures, we fitted the parameters, and the calculation results were as follows:

<!-- b000802 | caption | pages [8] -->
Table 2: Results of fitting parameters

<!-- b000803 | prose | pages [8] -->
Parameter μ1 μ2 σ1 σ2 ρ

<!-- b000804 | prose | pages [8] -->
18.25 9.77 -10.21 Fitted value 0 0

<!-- b000805 | prose | pages [8] -->
The calculated error is 35.562, which is small, indicating a good fitting effect.

<!-- b000806 | furniture | pages [9] -->
Team # 2500836                                                                   Page 8 of 25

<!-- b000807 | prose | pages [9] -->
微信公众号：数学模型 a. 3-D                             b. 2-D Figure 7：Image of the data fitted We substituted the optimally fitted parameters into d(x, y), and plotted the three-dimensional 微信号：MATHmodels oblique view and two-dimensional top-down view of the two-dimensional normal distribution model. Through these images, we can visually see the wear condition at different positions of the stairs, which is very close to the actual wear condition, indicating the rationality and accuracy of the model.

<!-- b000808 | heading | pages [9] -->
5 Model Ⅰ: Step Wear Analysis Model

<!-- b000809 | prose | pages [9] -->
"The rocks are firm and thick, capable of enduring for a thousand years." This line, which originates from the ancient "Book of Songs," conveys that solid and dense stones can last for millennia without decay. In antiquity, people often viewed rock as a symbol of indestructibility, able to withstand the erosion and wear of nature, maintaining its original form over time. However, even the most durable materials cannot completely resist the passage of time and external forces; their gradual deterioration reflects factors such as foot traffic, duration of use, and the inherent characteristics of the material. Therefore, examining the degree of wear on stone steps can provide insights into their construction date, usage patterns, and pedestrian behavior. As observed in Figure 1, the worn steps display a slight concavity, attributed to the tendency of pedestrians to walk in the center when ascending and descending. This has resulted in greater wear in the middle section of the step compared to the edges.

<!-- b000810 | heading | pages [9] -->
5.1 Pedestrian Flow Calculation based on Archard's Law

<!-- b000811 | prose | pages [9] -->
Archard's Law is an important empirical formula for describing material wear [3]. It’s commonly used to describe the wear that occurs when the surfaces of two materials are in contact and slide relative to each other.

<!-- b000812 | heading | pages [9] -->
5.1.1 Assumptions

<!-- b000813 | prose | pages [9] -->
(1) Assuming a linear dependence of the product of wear and forward force and sliding distance, the study is suitable for flat, simple contact surfaces.

<!-- b000814 | prose | pages [9] -->
(2) The factors of the step surface shape change, the temperature effect, and the elasticity of the material are ignored.

<!-- b000815 | prose | pages [9] -->
(3) Assuming that each step is indented equally.

<!-- b000816 | heading | pages [9] -->
5.1.2 Model Establishment

<!-- b000817 | heading | pages [9] -->
1. The Relationship between Wear Depth and Pedestrian Flow

<!-- b000818 | prose | pages [9] -->
According to Archard's Law, the wear depth of stairs is directly proportional to the number of people passing over them, and the relationship is given by:

<!-- b000819 | furniture | pages [10] -->
Team # 2500836                                                                   Page 9 of 25

<!-- b000820 | prose | pages [10] -->
(2)

<!-- b000821 | prose | pages [10] -->
In the equation, d is the wear depth, used to describe the degree of wear on stairs caused by pedestrian traffic. k is an empirical constant that typically depends on the material properties and environmental conditions. b is an empirical exponent, usually ranging from 0.3 to 0.5.

<!-- b000822 | prose | pages [10] -->
By setting different wear coefficients k and empirical constants b, this model can simulate the stair wear process under varying environmental and material conditions, and infer the level of stair usage.

<!-- b000823 | heading | pages [10] -->
2. Calculation of Daily Pedestrian Traffic

<!-- b000824 | prose | pages [10] -->
The formula connects pedestrian flow to the wear depth on the stairs. By integrating the wear depth over various regions of the stair surface, the number of people passing through the stairs each day can be estimated:

<!-- b000825 | prose | pages [10] -->
(3)

<!-- b000826 | prose | pages [10] -->
where n is the total number of steps, is the area of the i-th step, T is the time since the steps were completed, and d(x, y) is the wear depth at each location (x, y), obtained through scanning images.

<!-- b000827 | heading | pages [10] -->
3. Determination of the parameters

<!-- b000828 | prose | pages [10] -->
a) According to the data, the Leaning Tower of Pisa was completed in 1370 [4], then

<!-- b000829 | prose | pages [10] -->
.

<!-- b000830 | prose | pages [10] -->
b) Empirical coefficient b ranges from 0.3 to 0.5, here we took 0.3. c) The area of a single step A is . d) According to the information, the steps of the Leaning Tower of Pisa are made of marble and have a coefficient of friction of 0.06.

<!-- b000831 | caption | pages [10] -->
Table 3: Values of the parameters

<!-- b000832 | prose | pages [10] -->
Parameter T b A k Value 238710 0.3 0.8 0.06

<!-- b000833 | prose | pages [10] -->
By substituting the above parameters into Equation (3), we calculated that the number of people passing through the stairs each day was 1175. From the research data, it is known that 500,000 tourists climb the tower each year, while 6 million tourists visit the square. 500,000/365≈1370, which is close to the actual number of people using the steps daily, indicating the reliability and accuracy of the model.

<!-- b000834 | prose | pages [10] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000835 | caption | pages [10] -->
Figure 8: Calculation result

<!-- b000836 | prose | pages [10, 11] -->
关注数学模型 (1) For the same step, by only changing the friction coefficient and keeping other conditions constant, as the friction coefficient increases, the usage frequency of the step, that is, the number of times it is stepped on per day, gradually decreases. In other words, the smaller the friction coefficient of the step material, the more wear-resistant the step is and the longer its service life will be.

<!-- b000837 | furniture | pages [10] -->
2

<!-- b000838 | furniture | pages [10] -->
MATHmodels

<!-- b000839 | furniture | pages [10] -->
获取更多资讯

<!-- b000840 | furniture | pages [11] -->
Team # 2500836                                                                   Page 10 of 25

<!-- b000841 | caption | pages [11] -->
Figure 8 shows that：

<!-- b000843 | prose | pages [11] -->
(2) When the step wear factor is between 0.02~0.04, the image is very steep, and as the wear factor increases, the daily usage frequency decreases rapidly; when the wear factor is between 0.04 ~ 0.1, the image is relatively flat, indicating that the increase in wear factor has a smaller impact on the daily usage frequency.

<!-- b000844 | prose | pages [11] -->
微信公众号：数学模型

<!-- b000845 | heading | pages [11] -->
5.2 Preference Direction Model Based on Wear Depth Distribution

<!-- b000846 | prose | pages [11] -->
As individuals descend or ascend stairs, the front edges of the steps are subject to greater wear due to how people naturally place their feet. This results in more significant wear at the front and edges of the steps. Consequently, people exhibit varying directional preferences when navigating stairs. The travel direction preference index is defined as follows:

<!-- b000847 | prose | pages [11] -->
(4)

<!-- b000848 | caption | pages [11] -->
Table 4: The meaning of different D values

<!-- b000849 | prose | pages [11] -->
微信号：MATHmodels D value Meaning more people go up the steps than down D＞0 more people go down the steps than up D＜0 the flow of people up and down the steps is close |D|≈0

<!-- b000850 | caption | pages [11] -->
Figure 9: Determination of travel direction preference index

<!-- b000851 | prose | pages [11] -->
The calculation yields

<!-- b000852 | prose | pages [11] -->
indicating that more people are taking the downward steps, meaning that stairs users prefer the downward direction.

<!-- b000853 | furniture | pages [12] -->
Team # 2500836                                                                   Page 11 of 25

<!-- b000854 | caption | pages [12] -->
Figure 10: Variation in wear depth of steps of different lengths

<!-- b000855 | prose | pages [12] -->
By observing the cross-sectional views for different values of x, we could see that the cases where x equals 5, 10, and 20, as well as when x equals 0, all show that is greater than , resulting in a calculated D that is less than 0. This further illustrates that the stairs are primarily used for going downstairs. After consulting the materials, we found that the stairs of the Leaning Tower of Pisa consist of two spiral staircases, one for ascending and the other for descending. This design not only saves space but also helps to disperse the pressure of pedestrian traffic. According to the calculation results, it is determined that the staircase we studied is mainly used for descending.

<!-- b000856 | heading | pages [12] -->
5.3 Walking Patterns Model based on Navier-Stokes Equations

<!-- b000857 | prose | pages [12] -->
Navier-Stokes Equations are fundamental equations that describe the motion of viscous fluids and can be applied to simulate the dynamics of pedestrian flow or crowd movement.

<!-- b000858 | heading | pages [12] -->
5.3.1 Assumptions

<!-- b000859 | prose | pages [12] -->
(1) Assumption of treating the crowd as a continuous medium: This is a simplification since individuals are discrete. By making this assumption, it becomes possible to describe the crowd using continuous functions such as velocity fields, density distributions, and pressure terms.

<!-- b000860 | prose | pages [12] -->
(2) Assumption of no-slip interaction between people and walls or obstacles: The interaction between people and walls or obstacles is assumed to be analogous to the relationship between a fluid and a solid boundary. That is, at the boundary, the fluid velocity is zero, meaning the velocity of the crowd at the point of contact with an obstacle is also zero.

<!-- b000861 | heading | pages [12] -->
5.3.2 Continuity Equation for Simulating Walking Patterns

<!-- b000862 | prose | pages [12] -->
Based on the Navier-Stokes Equations, a continuity equation (also known as the mass conservation equation) for simulating the movement of pedestrians in space is established [5]:

<!-- b000863 | prose | pages [12] -->
(5)

<!-- b000864 | prose | pages [12] -->
In this equation:

<!-- b000865 | prose | pages [12] -->
ρ represents the pedestrian density, indicating the number of people per unit area and describing • the level of crowding in a given area.

<!-- b000866 | prose | pages [12] -->
v represents the velocity vector of pedestrians, indicating their speed and direction of movement. • N(x, y, t) represents the traffic flow, which indicates how many people pass through a specific • location (x, y) at time t.

<!-- b000867 | prose | pages [12] -->
represents the rate of change of pedestrian density over time, describing how the pedestrian •

<!-- b000868 | prose | pages [12] -->
density at a specific location changes with time.

<!-- b000869 | prose | pages [12, 13] -->
关注数学模型 ∇⋅(ρv) is the flux divergence, describing pedestrians' inflow and outflow within a certain area. • ρv is the pedestrian flux, combining density and velocity to describe the flow of pedestrians.

<!-- b000870 | furniture | pages [12] -->
2

<!-- b000871 | furniture | pages [12] -->
MATHmodels

<!-- b000872 | furniture | pages [12] -->
获取更多资讯

<!-- b000873 | furniture | pages [13] -->
Team # 2500836                                                                   Page 12 of 25

<!-- b000875 | prose | pages [13] -->
We used the finite-difference (FDM) method to solve this equation.

<!-- b000876 | prose | pages [13] -->
For the time derivatives, Forward Euler was used.

<!-- b000877 | prose | pages [13] -->
(6)

<!-- b000878 | prose | pages [13] -->
微信公众号：数学模型 For the spatial derivatives, the central difference is used.

<!-- b000879 | prose | pages [13] -->
(7)

<!-- b000880 | prose | pages [13] -->
No-slip boundary conditions:

<!-- b000881 | prose | pages [13] -->
(8)

<!-- b000882 | prose | pages [13] -->
We can estimate the pedestrian flow speed at different densities based on the relationship between pedestrian density and flow rate [6]. The following rules apply: ⚫ If 0＜ρ＜1.5, the flow rate N = 1, meaning 1 person passes through per second. ⚫ If 1.5≤ρ≤2.5, the flow rate increases to N = 2. 微信号：MATHmodels This can be understood intuitively: When pedestrian density is low, there is more space between individuals, leading to minimal interference and fewer restrictions on movement. As density increases, the distance between individuals decreases, and mutual interference increases, causing the movement speed to become more restricted. In this density range, although pedestrians can still pass through the stairs, the available space becomes more constrained, and the flow rate increases to 2 people per second. At this point, the number of people passing through the stairs per second increases, but individual movement speed is limited due to the higher density.

<!-- b000883 | caption | pages [13] -->
Figure 11: Pedestrian Density Heatmap

<!-- b000884 | prose | pages [13] -->
Calculations show that , indicating that people typically choose to travel single file when using the stairs."

<!-- b000885 | heading | pages [13] -->
6 Model II: Step Characteristic Analysis Model

<!-- b000886 | prose | pages [13, 14] -->
Based on life experience, in situations of urban prosperity and people's stability, new buildings are constructed, and these buildings are used frequently when they are first built. Over time, changes in the rise and fall of cities, population migration, and the emergence of new buildings can lead to a decrease in the usage frequency of old buildings, and consequently, the usage frequency of staircases also declines continuously. Assuming that the number of people passing through the staircases decays m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m exponentially, we thus obtained the change in foot traffic over time as follows:

<!-- b000887 | furniture | pages [13] -->
m

<!-- b000888 | furniture | pages [13] -->
m

<!-- b000889 | furniture | pages [13] -->
m

<!-- b000890 | furniture | pages [13] -->
m

<!-- b000891 | furniture | pages [13] -->
m

<!-- b000892 | furniture | pages [13] -->
m

<!-- b000893 | furniture | pages [13] -->
m

<!-- b000894 | furniture | pages [13] -->
m

<!-- b000895 | furniture | pages [13] -->
m

<!-- b000896 | furniture | pages [13] -->
m

<!-- b000897 | furniture | pages [13] -->
m

<!-- b000898 | furniture | pages [13] -->
m

<!-- b000899 | furniture | pages [13] -->
m

<!-- b000900 | furniture | pages [13] -->
m

<!-- b000901 | furniture | pages [13] -->
m

<!-- b000902 | furniture | pages [13] -->
m

<!-- b000903 | furniture | pages [13] -->
m

<!-- b000904 | furniture | pages [13] -->
m

<!-- b000905 | furniture | pages [13] -->
m

<!-- b000906 | furniture | pages [13] -->
m

<!-- b000907 | furniture | pages [13] -->
m

<!-- b000908 | furniture | pages [13] -->
m

<!-- b000909 | furniture | pages [13] -->
m

<!-- b000910 | furniture | pages [13] -->
m

<!-- b000911 | furniture | pages [13] -->
m

<!-- b000912 | furniture | pages [13] -->
m

<!-- b000913 | furniture | pages [13] -->
m

<!-- b000914 | furniture | pages [13] -->
m

<!-- b000915 | furniture | pages [13] -->
m

<!-- b000916 | furniture | pages [13] -->
m

<!-- b000917 | furniture | pages [13] -->
m

<!-- b000918 | furniture | pages [13] -->
m

<!-- b000919 | furniture | pages [13] -->
m

<!-- b000920 | furniture | pages [13] -->
m

<!-- b000921 | furniture | pages [13] -->
m

<!-- b000922 | furniture | pages [13] -->
m

<!-- b000923 | furniture | pages [13] -->
m

<!-- b000924 | furniture | pages [13] -->
m

<!-- b000925 | furniture | pages [13] -->
m

<!-- b000926 | furniture | pages [13] -->
m

<!-- b000927 | furniture | pages [13] -->
m

<!-- b000928 | furniture | pages [13] -->
m

<!-- b000929 | furniture | pages [13] -->
m

<!-- b000930 | furniture | pages [13] -->
m

<!-- b000931 | furniture | pages [13] -->
m

<!-- b000932 | furniture | pages [13] -->
m

<!-- b000933 | furniture | pages [13] -->
m

<!-- b000934 | furniture | pages [13] -->
m

<!-- b000935 | furniture | pages [13] -->
m

<!-- b000936 | furniture | pages [13] -->
m

<!-- b000937 | furniture | pages [13] -->
m

<!-- b000938 | furniture | pages [13] -->
m

<!-- b000939 | furniture | pages [13] -->
m

<!-- b000940 | furniture | pages [13] -->
m

<!-- b000941 | furniture | pages [13] -->
m

<!-- b000942 | furniture | pages [13] -->
m

<!-- b000943 | furniture | pages [13] -->
m

<!-- b000944 | furniture | pages [13] -->
m

<!-- b000945 | furniture | pages [13] -->
m

<!-- b000946 | furniture | pages [13] -->
m

<!-- b000947 | furniture | pages [13] -->
m

<!-- b000948 | furniture | pages [13] -->
m

<!-- b000949 | furniture | pages [13] -->
m

<!-- b000950 | furniture | pages [13] -->
m

<!-- b000951 | furniture | pages [13] -->
m

<!-- b000952 | furniture | pages [13] -->
m

<!-- b000953 | furniture | pages [13] -->
m

<!-- b000954 | furniture | pages [13] -->
m

<!-- b000955 | furniture | pages [13] -->
m

<!-- b000956 | furniture | pages [13] -->
m

<!-- b000957 | furniture | pages [13] -->
m

<!-- b000958 | furniture | pages [13] -->
m

<!-- b000959 | furniture | pages [13] -->
m

<!-- b000960 | furniture | pages [13] -->
m

<!-- b000961 | furniture | pages [13] -->
m

<!-- b000962 | furniture | pages [13] -->
m

<!-- b000963 | furniture | pages [13] -->
m

<!-- b000964 | furniture | pages [13] -->
m

<!-- b000965 | furniture | pages [13] -->
m

<!-- b000966 | furniture | pages [13] -->
m

<!-- b000967 | furniture | pages [13] -->
m

<!-- b000968 | furniture | pages [13] -->
m

<!-- b000969 | furniture | pages [13] -->
m

<!-- b000970 | furniture | pages [13] -->
m

<!-- b000971 | furniture | pages [13] -->
m

<!-- b000972 | furniture | pages [13] -->
m

<!-- b000973 | furniture | pages [13] -->
m

<!-- b000974 | furniture | pages [13] -->
m

<!-- b000975 | furniture | pages [13] -->
m

<!-- b000976 | furniture | pages [13] -->
m

<!-- b000977 | furniture | pages [13] -->
m

<!-- b000978 | furniture | pages [13] -->
m

<!-- b000979 | furniture | pages [13] -->
m

<!-- b000980 | furniture | pages [13] -->
m

<!-- b000981 | furniture | pages [13] -->
m

<!-- b000982 | furniture | pages [13] -->
m

<!-- b000983 | furniture | pages [13] -->
m

<!-- b000984 | furniture | pages [13] -->
m

<!-- b000985 | furniture | pages [13] -->
m

<!-- b000986 | furniture | pages [13] -->
m

<!-- b000987 | furniture | pages [13] -->
m

<!-- b000988 | furniture | pages [13] -->
m

<!-- b000989 | furniture | pages [13] -->
m

<!-- b000990 | furniture | pages [13] -->
m

<!-- b000991 | furniture | pages [13] -->
m

<!-- b000992 | furniture | pages [13] -->
m

<!-- b000993 | furniture | pages [13] -->
m

<!-- b000994 | furniture | pages [13] -->
m

<!-- b000995 | furniture | pages [13] -->
m

<!-- b000996 | furniture | pages [13] -->
m

<!-- b000997 | furniture | pages [13] -->
m

<!-- b000998 | furniture | pages [13] -->
m

<!-- b000999 | furniture | pages [13] -->
m

<!-- b001000 | furniture | pages [13] -->
m

<!-- b001001 | furniture | pages [13] -->
m

<!-- b001002 | furniture | pages [13] -->
m

<!-- b001003 | furniture | pages [13] -->
m

<!-- b001004 | furniture | pages [13] -->
m

<!-- b001005 | furniture | pages [13] -->
m

<!-- b001006 | furniture | pages [13] -->
m

<!-- b001007 | furniture | pages [13] -->
m

<!-- b001008 | furniture | pages [13] -->
m

<!-- b001009 | furniture | pages [13] -->
m

<!-- b001010 | furniture | pages [13] -->
m

<!-- b001011 | furniture | pages [13] -->
m

<!-- b001012 | furniture | pages [13] -->
m

<!-- b001013 | furniture | pages [13] -->
m

<!-- b001014 | furniture | pages [13] -->
m

<!-- b001015 | furniture | pages [13] -->
m

<!-- b001016 | furniture | pages [13] -->
m

<!-- b001017 | furniture | pages [13] -->
m

<!-- b001018 | furniture | pages [13] -->
m

<!-- b001019 | furniture | pages [13] -->
m

<!-- b001020 | furniture | pages [13] -->
m

<!-- b001021 | furniture | pages [13] -->
m

<!-- b001022 | furniture | pages [13] -->
m

<!-- b001023 | furniture | pages [13] -->
m

<!-- b001024 | furniture | pages [13] -->
m

<!-- b001025 | furniture | pages [13] -->
m

<!-- b001026 | furniture | pages [13] -->
m

<!-- b001027 | furniture | pages [13] -->
m

<!-- b001028 | furniture | pages [13] -->
m

<!-- b001029 | furniture | pages [13] -->
m

<!-- b001030 | furniture | pages [13] -->
m

<!-- b001031 | furniture | pages [13] -->
m

<!-- b001032 | furniture | pages [13] -->
m

<!-- b001033 | furniture | pages [13] -->
m

<!-- b001034 | furniture | pages [13] -->
m

<!-- b001035 | furniture | pages [13] -->
m

<!-- b001036 | furniture | pages [13] -->
m

<!-- b001037 | furniture | pages [13] -->
m

<!-- b001038 | furniture | pages [13] -->
m

<!-- b001039 | furniture | pages [13] -->
m

<!-- b001040 | furniture | pages [13] -->
m

<!-- b001041 | furniture | pages [13] -->
m

<!-- b001042 | furniture | pages [13] -->
m

<!-- b001043 | furniture | pages [13] -->
m

<!-- b001044 | furniture | pages [13] -->
m

<!-- b001045 | furniture | pages [13] -->
m

<!-- b001046 | furniture | pages [13] -->
m

<!-- b001047 | furniture | pages [13] -->
m

<!-- b001048 | furniture | pages [13] -->
m

<!-- b001049 | furniture | pages [13] -->
m

<!-- b001050 | furniture | pages [13] -->
m

<!-- b001051 | furniture | pages [13] -->
m

<!-- b001052 | furniture | pages [13] -->
m

<!-- b001053 | furniture | pages [13] -->
m

<!-- b001054 | furniture | pages [13] -->
m

<!-- b001055 | furniture | pages [13] -->
m

<!-- b001056 | furniture | pages [13] -->
m

<!-- b001057 | furniture | pages [13] -->
m

<!-- b001058 | furniture | pages [13] -->
m

<!-- b001059 | furniture | pages [13] -->
m

<!-- b001060 | furniture | pages [13] -->
m

<!-- b001061 | furniture | pages [13] -->
m

<!-- b001062 | furniture | pages [13] -->
m

<!-- b001063 | furniture | pages [13] -->
m

<!-- b001064 | furniture | pages [13] -->
m

<!-- b001065 | furniture | pages [13] -->
m

<!-- b001066 | furniture | pages [13] -->
m

<!-- b001067 | furniture | pages [13] -->
m

<!-- b001068 | furniture | pages [13] -->
m

<!-- b001069 | furniture | pages [13] -->
m

<!-- b001070 | furniture | pages [13] -->
m

<!-- b001071 | furniture | pages [13] -->
m

<!-- b001072 | furniture | pages [13] -->
m

<!-- b001073 | furniture | pages [13] -->
m

<!-- b001074 | furniture | pages [13] -->
m

<!-- b001075 | furniture | pages [13] -->
m

<!-- b001076 | furniture | pages [13] -->
m

<!-- b001077 | furniture | pages [13] -->
m

<!-- b001078 | furniture | pages [13] -->
m

<!-- b001079 | furniture | pages [13] -->
m

<!-- b001080 | furniture | pages [13] -->
m

<!-- b001081 | furniture | pages [13] -->
m

<!-- b001082 | furniture | pages [13] -->
m

<!-- b001083 | furniture | pages [13] -->
m

<!-- b001084 | furniture | pages [13] -->
m

<!-- b001085 | furniture | pages [13] -->
m

<!-- b001086 | furniture | pages [13] -->
m

<!-- b001087 | furniture | pages [13] -->
m

<!-- b001088 | furniture | pages [13] -->
m

<!-- b001089 | furniture | pages [13] -->
m

<!-- b001090 | furniture | pages [13] -->
m

<!-- b001091 | furniture | pages [13] -->
m

<!-- b001092 | furniture | pages [13] -->
m

<!-- b001093 | furniture | pages [13] -->
m

<!-- b001094 | furniture | pages [13] -->
m

<!-- b001095 | furniture | pages [13] -->
m

<!-- b001096 | furniture | pages [13] -->
m

<!-- b001097 | furniture | pages [13] -->
m

<!-- b001098 | furniture | pages [13] -->
m

<!-- b001099 | furniture | pages [13] -->
m

<!-- b001100 | furniture | pages [13] -->
m

<!-- b001101 | furniture | pages [13] -->
m

<!-- b001102 | furniture | pages [13] -->
m

<!-- b001103 | furniture | pages [13] -->
m

<!-- b001104 | furniture | pages [13] -->
m

<!-- b001105 | furniture | pages [13] -->
m

<!-- b001106 | furniture | pages [13] -->
m

<!-- b001107 | furniture | pages [13] -->
m

<!-- b001108 | furniture | pages [13] -->
m

<!-- b001109 | furniture | pages [13] -->
m

<!-- b001110 | furniture | pages [13] -->
m

<!-- b001111 | furniture | pages [13] -->
m

<!-- b001112 | furniture | pages [13] -->
m

<!-- b001113 | furniture | pages [13] -->
m

<!-- b001114 | furniture | pages [13] -->
m

<!-- b001115 | furniture | pages [13] -->
m

<!-- b001116 | furniture | pages [13] -->
m

<!-- b001117 | furniture | pages [13] -->
m

<!-- b001118 | furniture | pages [13] -->
m

<!-- b001119 | furniture | pages [13] -->
m

<!-- b001120 | furniture | pages [13] -->
m

<!-- b001121 | furniture | pages [13] -->
m

<!-- b001122 | furniture | pages [13] -->
m

<!-- b001123 | furniture | pages [13] -->
m

<!-- b001124 | furniture | pages [13] -->
m

<!-- b001125 | furniture | pages [13] -->
m

<!-- b001126 | furniture | pages [13] -->
m

<!-- b001127 | furniture | pages [13] -->
m

<!-- b001128 | furniture | pages [13] -->
m

<!-- b001129 | furniture | pages [13] -->
m

<!-- b001130 | furniture | pages [13] -->
m

<!-- b001131 | furniture | pages [13] -->
m

<!-- b001132 | furniture | pages [13] -->
m

<!-- b001133 | furniture | pages [13] -->
m

<!-- b001134 | furniture | pages [13] -->
m

<!-- b001135 | furniture | pages [13] -->
m

<!-- b001136 | furniture | pages [13] -->
m

<!-- b001137 | furniture | pages [13] -->
m

<!-- b001138 | furniture | pages [13] -->
m

<!-- b001139 | furniture | pages [13] -->
m

<!-- b001140 | furniture | pages [13] -->
m

<!-- b001141 | furniture | pages [13] -->
m

<!-- b001142 | furniture | pages [13] -->
m

<!-- b001143 | furniture | pages [13] -->
m

<!-- b001144 | furniture | pages [13] -->
m

<!-- b001145 | furniture | pages [13] -->
m

<!-- b001146 | furniture | pages [13] -->
m

<!-- b001147 | furniture | pages [13] -->
m

<!-- b001148 | furniture | pages [13] -->
m

<!-- b001149 | furniture | pages [13] -->
m

<!-- b001150 | furniture | pages [13] -->
m

<!-- b001151 | furniture | pages [13] -->
m

<!-- b001152 | furniture | pages [13] -->
m

<!-- b001153 | furniture | pages [13] -->
m

<!-- b001154 | furniture | pages [13] -->
m

<!-- b001155 | furniture | pages [13] -->
m

<!-- b001156 | furniture | pages [13] -->
m

<!-- b001157 | furniture | pages [13] -->
m

<!-- b001158 | furniture | pages [13] -->
m

<!-- b001159 | furniture | pages [13] -->
m

<!-- b001160 | furniture | pages [13] -->
m

<!-- b001161 | furniture | pages [13] -->
m

<!-- b001162 | furniture | pages [13] -->
m

<!-- b001163 | furniture | pages [13] -->
m

<!-- b001164 | furniture | pages [13] -->
m

<!-- b001165 | furniture | pages [13] -->
m

<!-- b001166 | furniture | pages [13] -->
m

<!-- b001167 | furniture | pages [13] -->
m

<!-- b001168 | furniture | pages [13] -->
m

<!-- b001169 | furniture | pages [13] -->
m

<!-- b001170 | furniture | pages [13] -->
m

<!-- b001171 | furniture | pages [13] -->
m

<!-- b001172 | furniture | pages [13] -->
m

<!-- b001173 | furniture | pages [13] -->
m

<!-- b001174 | furniture | pages [13] -->
m

<!-- b001175 | furniture | pages [13] -->
m

<!-- b001176 | furniture | pages [13] -->
m

<!-- b001177 | furniture | pages [13] -->
m

<!-- b001178 | furniture | pages [13] -->
m

<!-- b001179 | furniture | pages [13] -->
m

<!-- b001180 | furniture | pages [13] -->
m

<!-- b001181 | furniture | pages [13] -->
m

<!-- b001182 | furniture | pages [13] -->
m

<!-- b001183 | furniture | pages [13] -->
m

<!-- b001184 | furniture | pages [13] -->
m

<!-- b001185 | furniture | pages [13] -->
m

<!-- b001186 | furniture | pages [13] -->
m

<!-- b001187 | furniture | pages [13] -->
m

<!-- b001188 | furniture | pages [13] -->
m

<!-- b001189 | furniture | pages [13] -->
m

<!-- b001190 | furniture | pages [13] -->
m

<!-- b001191 | furniture | pages [13] -->
m

<!-- b001192 | furniture | pages [13] -->
m

<!-- b001193 | furniture | pages [13] -->
m

<!-- b001194 | furniture | pages [13] -->
m

<!-- b001195 | furniture | pages [13] -->
m

<!-- b001196 | furniture | pages [13] -->
m

<!-- b001197 | furniture | pages [13] -->
m

<!-- b001198 | furniture | pages [13] -->
m

<!-- b001199 | furniture | pages [13] -->
m

<!-- b001200 | furniture | pages [13] -->
m

<!-- b001201 | furniture | pages [13] -->
m

<!-- b001202 | furniture | pages [13] -->
m

<!-- b001203 | furniture | pages [13] -->
m

<!-- b001204 | furniture | pages [13] -->
m

<!-- b001205 | furniture | pages [13] -->
m

<!-- b001206 | furniture | pages [13] -->
m

<!-- b001207 | furniture | pages [13] -->
m

<!-- b001208 | furniture | pages [13] -->
m

<!-- b001209 | furniture | pages [13] -->
m

<!-- b001210 | furniture | pages [13] -->
m

<!-- b001211 | furniture | pages [14] -->
Team # 2500836                                                                   Page 13 of 25

<!-- b001213 | prose | pages [14] -->
(9)

<!-- b001214 | prose | pages [14] -->
where is the number of people who passed through the steps on the first day, and is the rate of pedestrian decay.

<!-- b001215 | caption | pages [14] -->
Figure 12: Change in foot traffic over time

<!-- b001216 | prose | pages [14] -->
Observing Figure 12, initially there are many people trampling, but gradually the number of visitors or users decreases and then levels off, fitting an exponential decay trend.

<!-- b001217 | prose | pages [14] -->
Integrating Equation (6), we got

<!-- b001218 | prose | pages [14] -->
(10)

<!-- b001219 | heading | pages [14] -->
6.1 Comparison of Actual and Theoretical Stair Usage Time

<!-- b001220 | heading | pages [14] -->
6.1.1 Model Establishment

<!-- b001221 | prose | pages [14] -->
To judge whether the actual use time of the steps was consistent with the theoretical results, we substituted Equation (10) into Equation (1) to obtain the theoretical wear depth.

<!-- b001222 | prose | pages [14] -->
(11)

<!-- b001223 | caption | pages [14] -->
Table 5: Values of each parameter in Equation (11)

<!-- b001224 | prose | pages [14] -->
Parameter

<!-- b001225 | prose | pages [14] -->
Value 0.06 10000 0.004 0.3

<!-- b001226 | prose | pages [14] -->
关注数学模型

<!-- b001227 | furniture | pages [14] -->
2

<!-- b001228 | furniture | pages [14] -->
MATHmodels

<!-- b001229 | furniture | pages [14] -->
获取更多资讯

<!-- b001230 | furniture | pages [15] -->
Team # 2500836                                                                   Page 14 of 25

<!-- b001231 | heading | pages [15] -->
6.1.2 Results

<!-- b001232 | prose | pages [15] -->
微信公众号：数学模型

<!-- b001233 | caption | pages [15] -->
Figure 13: Accumulative wear depth variation

<!-- b001234 | prose | pages [15] -->
According to Figure 13, we could find that:

<!-- b001235 | prose | pages [15] -->
(1) The Leaning Tower of Pisa was completed 654 years ago, calculated as 2024 - 1370 = 654 years. Theoretically, by 2024, the accumulated wear depth should be 4.871 cm. In contrast, the actual depth measured from the images is approximately 4.5 cm, with a small error of 0.371 cm, within the expected range.

<!-- b001236 | prose | pages [15] -->
(2) In addition, we observed that the wear rate of the stairs in the red area (0~250 years) is relatively fast, while in the green area (251~700 years), the wear rate slows down. This is because, after the building's completion, the number of visitors was high for some time, leading to more frequent 微信号：MATHmodels use of the stairs and, consequently, more severe wear. This result is consistent with the t~N(t) function, confirming that our model is reasonable.

<!-- b001237 | heading | pages [15] -->
6.1.3 Error Analysis

<!-- b001238 | prose | pages [15] -->
Considering that the wear condition of a single step may be random and lack strong persuasiveness and accuracy, we collected the wear depth of 100 steps at the same location for study.

<!-- b001239 | prose | pages [15] -->
Finally, the mean squared error between the theoretical wear depth and the actual wear depth was calculated.

<!-- b001240 | prose | pages [15] -->
(12)

<!-- b001241 | prose | pages [15] -->
If (taken as 0.2), the theoretical wear depth and the actual wear depth can be considered the same. Otherwise, the difference means that the staircase has been repaired and renovated.

<!-- b001242 | prose | pages [15] -->
In the end, we calculated that MSE = 0.1542＜0.2, indicating that the theoretical wear depth is consistent with the actual situation.

<!-- b001243 | heading | pages [15] -->
6.2 Calculation of Stair Service Life

<!-- b001244 | prose | pages [15] -->
Since we have obtained the relationship between the step wear depth and the service life, we could estimate the service life of the step based on the measurement data:

<!-- b001245 | prose | pages [15] -->
(13)

<!-- b001246 | prose | pages [15, 16] -->
We calculated T through the actual measured wear depth and plotted the graph of T as a function of d, from which it could be seen that the deeper the wear depth, the older the staircase. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Then we substituted the measured value d = 4.5 into Equation (13), and the age of the step was calculated to be 312.5 years.

<!-- b001247 | furniture | pages [15] -->
m

<!-- b001248 | furniture | pages [15] -->
m

<!-- b001249 | furniture | pages [15] -->
m

<!-- b001250 | furniture | pages [15] -->
m

<!-- b001251 | furniture | pages [15] -->
m

<!-- b001252 | furniture | pages [15] -->
m

<!-- b001253 | furniture | pages [15] -->
m

<!-- b001254 | furniture | pages [15] -->
m

<!-- b001255 | furniture | pages [15] -->
m

<!-- b001256 | furniture | pages [15] -->
m

<!-- b001257 | furniture | pages [15] -->
m

<!-- b001258 | furniture | pages [15] -->
m

<!-- b001259 | furniture | pages [15] -->
m

<!-- b001260 | furniture | pages [15] -->
m

<!-- b001261 | furniture | pages [15] -->
m

<!-- b001262 | furniture | pages [15] -->
m

<!-- b001263 | furniture | pages [15] -->
m

<!-- b001264 | furniture | pages [15] -->
m

<!-- b001265 | furniture | pages [15] -->
m

<!-- b001266 | furniture | pages [15] -->
m

<!-- b001267 | furniture | pages [15] -->
m

<!-- b001268 | furniture | pages [15] -->
m

<!-- b001269 | furniture | pages [15] -->
m

<!-- b001270 | furniture | pages [15] -->
m

<!-- b001271 | furniture | pages [15] -->
m

<!-- b001272 | furniture | pages [15] -->
m

<!-- b001273 | furniture | pages [15] -->
m

<!-- b001274 | furniture | pages [15] -->
m

<!-- b001275 | furniture | pages [15] -->
m

<!-- b001276 | furniture | pages [15] -->
m

<!-- b001277 | furniture | pages [15] -->
m

<!-- b001278 | furniture | pages [15] -->
m

<!-- b001279 | furniture | pages [15] -->
m

<!-- b001280 | furniture | pages [15] -->
m

<!-- b001281 | furniture | pages [15] -->
m

<!-- b001282 | furniture | pages [15] -->
m

<!-- b001283 | furniture | pages [15] -->
m

<!-- b001284 | furniture | pages [15] -->
m

<!-- b001285 | furniture | pages [15] -->
m

<!-- b001286 | furniture | pages [15] -->
m

<!-- b001287 | furniture | pages [15] -->
m

<!-- b001288 | furniture | pages [15] -->
m

<!-- b001289 | furniture | pages [15] -->
m

<!-- b001290 | furniture | pages [15] -->
m

<!-- b001291 | furniture | pages [15] -->
m

<!-- b001292 | furniture | pages [15] -->
m

<!-- b001293 | furniture | pages [15] -->
m

<!-- b001294 | furniture | pages [15] -->
m

<!-- b001295 | furniture | pages [15] -->
m

<!-- b001296 | furniture | pages [15] -->
m

<!-- b001297 | furniture | pages [15] -->
m

<!-- b001298 | furniture | pages [15] -->
m

<!-- b001299 | furniture | pages [15] -->
m

<!-- b001300 | furniture | pages [15] -->
m

<!-- b001301 | furniture | pages [15] -->
m

<!-- b001302 | furniture | pages [15] -->
m

<!-- b001303 | furniture | pages [15] -->
m

<!-- b001304 | furniture | pages [15] -->
m

<!-- b001305 | furniture | pages [15] -->
m

<!-- b001306 | furniture | pages [15] -->
m

<!-- b001307 | furniture | pages [15] -->
m

<!-- b001308 | furniture | pages [15] -->
m

<!-- b001309 | furniture | pages [15] -->
m

<!-- b001310 | furniture | pages [15] -->
m

<!-- b001311 | furniture | pages [15] -->
m

<!-- b001312 | furniture | pages [15] -->
m

<!-- b001313 | furniture | pages [15] -->
m

<!-- b001314 | furniture | pages [15] -->
m

<!-- b001315 | furniture | pages [15] -->
m

<!-- b001316 | furniture | pages [15] -->
m

<!-- b001317 | furniture | pages [15] -->
m

<!-- b001318 | furniture | pages [15] -->
m

<!-- b001319 | furniture | pages [15] -->
m

<!-- b001320 | furniture | pages [15] -->
m

<!-- b001321 | furniture | pages [15] -->
m

<!-- b001322 | furniture | pages [15] -->
m

<!-- b001323 | furniture | pages [15] -->
m

<!-- b001324 | furniture | pages [15] -->
m

<!-- b001325 | furniture | pages [15] -->
m

<!-- b001326 | furniture | pages [15] -->
m

<!-- b001327 | furniture | pages [15] -->
m

<!-- b001328 | furniture | pages [15] -->
m

<!-- b001329 | furniture | pages [15] -->
m

<!-- b001330 | furniture | pages [15] -->
m

<!-- b001331 | furniture | pages [15] -->
m

<!-- b001332 | furniture | pages [15] -->
m

<!-- b001333 | furniture | pages [15] -->
m

<!-- b001334 | furniture | pages [15] -->
m

<!-- b001335 | furniture | pages [15] -->
m

<!-- b001336 | furniture | pages [15] -->
m

<!-- b001337 | furniture | pages [15] -->
m

<!-- b001338 | furniture | pages [15] -->
m

<!-- b001339 | furniture | pages [15] -->
m

<!-- b001340 | furniture | pages [15] -->
m

<!-- b001341 | furniture | pages [15] -->
m

<!-- b001342 | furniture | pages [15] -->
m

<!-- b001343 | furniture | pages [15] -->
m

<!-- b001344 | furniture | pages [15] -->
m

<!-- b001345 | furniture | pages [15] -->
m

<!-- b001346 | furniture | pages [15] -->
m

<!-- b001347 | furniture | pages [15] -->
m

<!-- b001348 | furniture | pages [15] -->
m

<!-- b001349 | furniture | pages [15] -->
m

<!-- b001350 | furniture | pages [15] -->
m

<!-- b001351 | furniture | pages [15] -->
m

<!-- b001352 | furniture | pages [15] -->
m

<!-- b001353 | furniture | pages [15] -->
m

<!-- b001354 | furniture | pages [15] -->
m

<!-- b001355 | furniture | pages [15] -->
m

<!-- b001356 | furniture | pages [15] -->
m

<!-- b001357 | furniture | pages [15] -->
m

<!-- b001358 | furniture | pages [15] -->
m

<!-- b001359 | furniture | pages [15] -->
m

<!-- b001360 | furniture | pages [15] -->
m

<!-- b001361 | furniture | pages [15] -->
m

<!-- b001362 | furniture | pages [15] -->
m

<!-- b001363 | furniture | pages [15] -->
m

<!-- b001364 | furniture | pages [15] -->
m

<!-- b001365 | furniture | pages [15] -->
m

<!-- b001366 | furniture | pages [15] -->
m

<!-- b001367 | furniture | pages [15] -->
m

<!-- b001368 | furniture | pages [15] -->
m

<!-- b001369 | furniture | pages [15] -->
m

<!-- b001370 | furniture | pages [15] -->
m

<!-- b001371 | furniture | pages [15] -->
m

<!-- b001372 | furniture | pages [15] -->
m

<!-- b001373 | furniture | pages [15] -->
m

<!-- b001374 | furniture | pages [15] -->
m

<!-- b001375 | furniture | pages [15] -->
m

<!-- b001376 | furniture | pages [15] -->
m

<!-- b001377 | furniture | pages [15] -->
m

<!-- b001378 | furniture | pages [15] -->
m

<!-- b001379 | furniture | pages [15] -->
m

<!-- b001380 | furniture | pages [15] -->
m

<!-- b001381 | furniture | pages [15] -->
m

<!-- b001382 | furniture | pages [15] -->
m

<!-- b001383 | furniture | pages [15] -->
m

<!-- b001384 | furniture | pages [15] -->
m

<!-- b001385 | furniture | pages [15] -->
m

<!-- b001386 | furniture | pages [15] -->
m

<!-- b001387 | furniture | pages [15] -->
m

<!-- b001388 | furniture | pages [15] -->
m

<!-- b001389 | furniture | pages [15] -->
m

<!-- b001390 | furniture | pages [15] -->
m

<!-- b001391 | furniture | pages [15] -->
m

<!-- b001392 | furniture | pages [15] -->
m

<!-- b001393 | furniture | pages [15] -->
m

<!-- b001394 | furniture | pages [15] -->
m

<!-- b001395 | furniture | pages [15] -->
m

<!-- b001396 | furniture | pages [15] -->
m

<!-- b001397 | furniture | pages [15] -->
m

<!-- b001398 | furniture | pages [15] -->
m

<!-- b001399 | furniture | pages [15] -->
m

<!-- b001400 | furniture | pages [15] -->
m

<!-- b001401 | furniture | pages [15] -->
m

<!-- b001402 | furniture | pages [15] -->
m

<!-- b001403 | furniture | pages [15] -->
m

<!-- b001404 | furniture | pages [15] -->
m

<!-- b001405 | furniture | pages [15] -->
m

<!-- b001406 | furniture | pages [15] -->
m

<!-- b001407 | furniture | pages [15] -->
m

<!-- b001408 | furniture | pages [15] -->
m

<!-- b001409 | furniture | pages [15] -->
m

<!-- b001410 | furniture | pages [15] -->
m

<!-- b001411 | furniture | pages [15] -->
m

<!-- b001412 | furniture | pages [15] -->
m

<!-- b001413 | furniture | pages [15] -->
m

<!-- b001414 | furniture | pages [15] -->
m

<!-- b001415 | furniture | pages [15] -->
m

<!-- b001416 | furniture | pages [15] -->
m

<!-- b001417 | furniture | pages [15] -->
m

<!-- b001418 | furniture | pages [15] -->
m

<!-- b001419 | furniture | pages [15] -->
m

<!-- b001420 | furniture | pages [15] -->
m

<!-- b001421 | furniture | pages [15] -->
m

<!-- b001422 | furniture | pages [15] -->
m

<!-- b001423 | furniture | pages [15] -->
m

<!-- b001424 | furniture | pages [15] -->
m

<!-- b001425 | furniture | pages [15] -->
m

<!-- b001426 | furniture | pages [15] -->
m

<!-- b001427 | furniture | pages [15] -->
m

<!-- b001428 | furniture | pages [15] -->
m

<!-- b001429 | furniture | pages [15] -->
m

<!-- b001430 | furniture | pages [15] -->
m

<!-- b001431 | furniture | pages [15] -->
m

<!-- b001432 | furniture | pages [15] -->
m

<!-- b001433 | furniture | pages [15] -->
m

<!-- b001434 | furniture | pages [15] -->
m

<!-- b001435 | furniture | pages [15] -->
m

<!-- b001436 | furniture | pages [15] -->
m

<!-- b001437 | furniture | pages [15] -->
m

<!-- b001438 | furniture | pages [15] -->
m

<!-- b001439 | furniture | pages [15] -->
m

<!-- b001440 | furniture | pages [15] -->
m

<!-- b001441 | furniture | pages [15] -->
m

<!-- b001442 | furniture | pages [15] -->
m

<!-- b001443 | furniture | pages [15] -->
m

<!-- b001444 | furniture | pages [15] -->
m

<!-- b001445 | furniture | pages [15] -->
m

<!-- b001446 | furniture | pages [15] -->
m

<!-- b001447 | furniture | pages [15] -->
m

<!-- b001448 | furniture | pages [15] -->
m

<!-- b001449 | furniture | pages [15] -->
m

<!-- b001450 | furniture | pages [15] -->
m

<!-- b001451 | furniture | pages [15] -->
m

<!-- b001452 | furniture | pages [15] -->
m

<!-- b001453 | furniture | pages [15] -->
m

<!-- b001454 | furniture | pages [15] -->
m

<!-- b001455 | furniture | pages [15] -->
m

<!-- b001456 | furniture | pages [15] -->
m

<!-- b001457 | furniture | pages [15] -->
m

<!-- b001458 | furniture | pages [15] -->
m

<!-- b001459 | furniture | pages [15] -->
m

<!-- b001460 | furniture | pages [15] -->
m

<!-- b001461 | furniture | pages [15] -->
m

<!-- b001462 | furniture | pages [15] -->
m

<!-- b001463 | furniture | pages [15] -->
m

<!-- b001464 | furniture | pages [15] -->
m

<!-- b001465 | furniture | pages [15] -->
m

<!-- b001466 | furniture | pages [15] -->
m

<!-- b001467 | furniture | pages [15] -->
m

<!-- b001468 | furniture | pages [15] -->
m

<!-- b001469 | furniture | pages [15] -->
m

<!-- b001470 | furniture | pages [15] -->
m

<!-- b001471 | furniture | pages [15] -->
m

<!-- b001472 | furniture | pages [15] -->
m

<!-- b001473 | furniture | pages [15] -->
m

<!-- b001474 | furniture | pages [15] -->
m

<!-- b001475 | furniture | pages [15] -->
m

<!-- b001476 | furniture | pages [15] -->
m

<!-- b001477 | furniture | pages [15] -->
m

<!-- b001478 | furniture | pages [15] -->
m

<!-- b001479 | furniture | pages [15] -->
m

<!-- b001480 | furniture | pages [15] -->
m

<!-- b001481 | furniture | pages [15] -->
m

<!-- b001482 | furniture | pages [15] -->
m

<!-- b001483 | furniture | pages [15] -->
m

<!-- b001484 | furniture | pages [15] -->
m

<!-- b001485 | furniture | pages [15] -->
m

<!-- b001486 | furniture | pages [15] -->
m

<!-- b001487 | furniture | pages [15] -->
m

<!-- b001488 | furniture | pages [15] -->
m

<!-- b001489 | furniture | pages [15] -->
m

<!-- b001490 | furniture | pages [15] -->
m

<!-- b001491 | furniture | pages [15] -->
m

<!-- b001492 | furniture | pages [15] -->
m

<!-- b001493 | furniture | pages [15] -->
m

<!-- b001494 | furniture | pages [15] -->
m

<!-- b001495 | furniture | pages [15] -->
m

<!-- b001496 | furniture | pages [15] -->
m

<!-- b001497 | furniture | pages [15] -->
m

<!-- b001498 | furniture | pages [15] -->
m

<!-- b001499 | furniture | pages [15] -->
m

<!-- b001500 | furniture | pages [15] -->
m

<!-- b001501 | furniture | pages [15] -->
m

<!-- b001502 | furniture | pages [15] -->
m

<!-- b001503 | furniture | pages [15] -->
m

<!-- b001504 | furniture | pages [15] -->
m

<!-- b001505 | furniture | pages [15] -->
m

<!-- b001506 | furniture | pages [15] -->
m

<!-- b001507 | furniture | pages [15] -->
m

<!-- b001508 | furniture | pages [15] -->
m

<!-- b001509 | furniture | pages [15] -->
m

<!-- b001510 | furniture | pages [15] -->
m

<!-- b001511 | furniture | pages [15] -->
m

<!-- b001512 | furniture | pages [15] -->
m

<!-- b001513 | furniture | pages [15] -->
m

<!-- b001514 | furniture | pages [15] -->
m

<!-- b001515 | furniture | pages [15] -->
m

<!-- b001516 | furniture | pages [15] -->
m

<!-- b001517 | furniture | pages [15] -->
m

<!-- b001518 | furniture | pages [15] -->
m

<!-- b001519 | furniture | pages [15] -->
m

<!-- b001520 | furniture | pages [15] -->
m

<!-- b001521 | furniture | pages [15] -->
m

<!-- b001522 | furniture | pages [15] -->
m

<!-- b001523 | furniture | pages [15] -->
m

<!-- b001524 | furniture | pages [15] -->
m

<!-- b001525 | furniture | pages [15] -->
m

<!-- b001526 | furniture | pages [15] -->
m

<!-- b001527 | furniture | pages [15] -->
m

<!-- b001528 | furniture | pages [15] -->
m

<!-- b001529 | furniture | pages [15] -->
m

<!-- b001530 | furniture | pages [15] -->
m

<!-- b001531 | furniture | pages [15] -->
m

<!-- b001532 | furniture | pages [15] -->
m

<!-- b001533 | furniture | pages [15] -->
m

<!-- b001534 | furniture | pages [15] -->
m

<!-- b001535 | furniture | pages [15] -->
m

<!-- b001536 | furniture | pages [15] -->
m

<!-- b001537 | furniture | pages [15] -->
m

<!-- b001538 | furniture | pages [15] -->
m

<!-- b001539 | furniture | pages [15] -->
m

<!-- b001540 | furniture | pages [15] -->
m

<!-- b001541 | furniture | pages [15] -->
m

<!-- b001542 | furniture | pages [15] -->
m

<!-- b001543 | furniture | pages [15] -->
m

<!-- b001544 | furniture | pages [15] -->
m

<!-- b001545 | furniture | pages [15] -->
m

<!-- b001546 | furniture | pages [15] -->
m

<!-- b001547 | furniture | pages [15] -->
m

<!-- b001548 | furniture | pages [15] -->
m

<!-- b001549 | furniture | pages [15] -->
m

<!-- b001550 | furniture | pages [15] -->
m

<!-- b001551 | furniture | pages [15] -->
m

<!-- b001552 | furniture | pages [15] -->
m

<!-- b001553 | furniture | pages [15] -->
m

<!-- b001554 | furniture | pages [15] -->
m

<!-- b001555 | furniture | pages [15] -->
m

<!-- b001556 | furniture | pages [15] -->
m

<!-- b001557 | furniture | pages [15] -->
m

<!-- b001558 | furniture | pages [15] -->
m

<!-- b001559 | furniture | pages [15] -->
m

<!-- b001560 | furniture | pages [15] -->
m

<!-- b001561 | furniture | pages [15] -->
m

<!-- b001562 | furniture | pages [15] -->
m

<!-- b001563 | furniture | pages [15] -->
m

<!-- b001564 | furniture | pages [15] -->
m

<!-- b001565 | furniture | pages [15] -->
m

<!-- b001566 | furniture | pages [15] -->
m

<!-- b001567 | furniture | pages [15] -->
m

<!-- b001568 | furniture | pages [15] -->
m

<!-- b001569 | furniture | pages [15] -->
m

<!-- b001570 | furniture | pages [15] -->
m

<!-- b001571 | furniture | pages [16] -->
Team # 2500836                                                                   Page 15 of 25

<!-- b001572 | caption | pages [16] -->
Figure 14: Variation in the service life of step

<!-- b001574 | prose | pages [16] -->
Considering that there were errors in the actual wear depth, pedestrian flow, and material property parameters when estimating the usage time of steps, we used the error propagation calculation formula:

<!-- b001575 | prose | pages [16] -->
(14)

<!-- b001576 | prose | pages [16] -->
where represents the wear depth error, which can be calculated based on scanning accuracy; refers to the pedestrian traffic estimation error, which can be easily obtained from historical data; and denotes the material wear coefficient error, which can be determined through experiments.

<!-- b001577 | prose | pages [16] -->
(15)

<!-- b001578 | prose | pages [16] -->
(16)

<!-- b001579 | prose | pages [16] -->
Combining two equations above based on Equation (11), the final calculated error is 15.46. Finally, a Monte Carlo simulation was used for reliability assessment, with hypothesis testing: is considered the optimal estimate, and a 95% confidence interval was applied.

<!-- b001580 | prose | pages [16] -->
(17)

<!-- b001581 | prose | pages [16] -->
The Monte Carlo method is a numerical technique based on random sampling and statistical principles, commonly used to solve complex problems. The basic steps are as follows: ⚫ Step 1: Define Parameter Uncertainty - Assume that the parameters in the model (such as , , , ) have some degree of uncertainty, which can be simulated by random sampling to represent the distribution of these parameters.

<!-- b001582 | prose | pages [16] -->
- For instance, assume that these parameters follow a normal distribution or a uniform distribution. ⚫ Step 2: Random Sampling - Perform multiple random samplings for each parameter to generate a set of parameter combinations.

<!-- b001583 | prose | pages [16] -->
关注数学模型

<!-- b001584 | furniture | pages [16] -->
2

<!-- b001585 | furniture | pages [16] -->
MATHmodels

<!-- b001586 | furniture | pages [16] -->
获取更多资讯

<!-- b001587 | furniture | pages [17] -->
Team # 2500836                                                                   Page 16 of 25

<!-- b001588 | heading | pages [17] -->
⚫ Step 3: Run the Model

<!-- b001589 | prose | pages [17] -->
- For each parameter combination, run the model to calculate the corresponding T value. ⚫ Step 4: Statistical Analysis - Conduct statistical analysis on all simulation results, calculating the mean, standard deviation, confidence interval, etc., to evaluate the stability and reliability of the model. 微信公众号：数学模型 微信号：MATHmodels

<!-- b001590 | caption | pages [17] -->
Figure 15: Monte Carlo simulation images

<!-- b001591 | prose | pages [17] -->
As can be seen from Figure 15, T is always in the upper and lower limits of the 95% confidence interval, indicating the high reliability of the model.According to Equation (17), the range of the staircase's age is (282.1984, 342.8016).

<!-- b001592 | heading | pages [17] -->
6.3 Determination of Stair Renovation

<!-- b001593 | prose | pages [17] -->
The renovation and maintenance of the stairs at the Leaning Tower of Pisa require careful handling in order to preserve its historical value. Common maintenance and renovation techniques involve image recognition and processing of cracks, magnifying details to observe traces of crack filling. By using a portable surface roughness tester, we can compare roughness differences across various areas of the stairs. Due to the repair methods, cracks are often filled with epoxy resin or lime-based materials. In areas with severe damage, the surface tends to become smoother, indicating that the stone has been replaced. If the roughness in certain areas is noticeably lower than others, it suggests that the stair material has been replaced with the same type to maintain consistency. To ensure stability, stainless steel or carbon fiber reinforcement may also have been applied. Renovations or repairs might also include the application of a waterproofing agent to prevent moisture penetration.

<!-- b001594 | prose | pages [17] -->
A portable laser scanner can be used to create a 3D model of the stairs, which is then compared with historical design drawings to observe any signs of stone replacement.

<!-- b001595 | prose | pages [17] -->
Since materials in the repaired areas may have different thermal conductivity and humidity conditions, these factors can result in distinct temperature distributions. By using infrared thermography, we can obtain the temperature distribution of the stairs and observe any abrupt changes. To test for waterproofing, a few drops of water can be applied to the stairs. If the water droplets roll off quickly, it indicates that waterproofing has been applied Besides, based on previous analysis, we calculated the age of the steps to be 312.5 years, which is less than the actual age of the Leaning Tower of Pisa at 654 years. This suggests that the stairs have undergone renovation or maintenance.

<!-- b001596 | prose | pages [17] -->
Through investigation and research into the restoration history of the Leaning Tower of Pisa, it has been discovered that the tower has been renovated and repaired multiple times, which can prove that our hypothesis is correct.

<!-- b001597 | prose | pages [17, 18] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 6.4 Determination of Material Source

<!-- b001598 | furniture | pages [17] -->
m

<!-- b001599 | furniture | pages [17] -->
m

<!-- b001600 | furniture | pages [17] -->
m

<!-- b001601 | furniture | pages [17] -->
m

<!-- b001602 | furniture | pages [17] -->
m

<!-- b001603 | furniture | pages [17] -->
m

<!-- b001604 | furniture | pages [17] -->
m

<!-- b001605 | furniture | pages [17] -->
m

<!-- b001606 | furniture | pages [17] -->
m

<!-- b001607 | furniture | pages [17] -->
m

<!-- b001608 | furniture | pages [17] -->
m

<!-- b001609 | furniture | pages [17] -->
m

<!-- b001610 | furniture | pages [17] -->
m

<!-- b001611 | furniture | pages [17] -->
m

<!-- b001612 | furniture | pages [17] -->
m

<!-- b001613 | furniture | pages [17] -->
m

<!-- b001614 | furniture | pages [17] -->
m

<!-- b001615 | furniture | pages [17] -->
m

<!-- b001616 | furniture | pages [17] -->
m

<!-- b001617 | furniture | pages [17] -->
m

<!-- b001618 | furniture | pages [17] -->
m

<!-- b001619 | furniture | pages [17] -->
m

<!-- b001620 | furniture | pages [17] -->
m

<!-- b001621 | furniture | pages [17] -->
m

<!-- b001622 | furniture | pages [17] -->
m

<!-- b001623 | furniture | pages [17] -->
m

<!-- b001624 | furniture | pages [17] -->
m

<!-- b001625 | furniture | pages [17] -->
m

<!-- b001626 | furniture | pages [17] -->
m

<!-- b001627 | furniture | pages [17] -->
m

<!-- b001628 | furniture | pages [17] -->
m

<!-- b001629 | furniture | pages [17] -->
m

<!-- b001630 | furniture | pages [17] -->
m

<!-- b001631 | furniture | pages [17] -->
m

<!-- b001632 | furniture | pages [17] -->
m

<!-- b001633 | furniture | pages [17] -->
m

<!-- b001634 | furniture | pages [17] -->
m

<!-- b001635 | furniture | pages [17] -->
m

<!-- b001636 | furniture | pages [17] -->
m

<!-- b001637 | furniture | pages [17] -->
m

<!-- b001638 | furniture | pages [17] -->
m

<!-- b001639 | furniture | pages [17] -->
m

<!-- b001640 | furniture | pages [17] -->
m

<!-- b001641 | furniture | pages [17] -->
m

<!-- b001642 | furniture | pages [17] -->
m

<!-- b001643 | furniture | pages [17] -->
m

<!-- b001644 | furniture | pages [17] -->
m

<!-- b001645 | furniture | pages [17] -->
m

<!-- b001646 | furniture | pages [17] -->
m

<!-- b001647 | furniture | pages [17] -->
m

<!-- b001648 | furniture | pages [17] -->
m

<!-- b001649 | furniture | pages [17] -->
m

<!-- b001650 | furniture | pages [17] -->
m

<!-- b001651 | furniture | pages [17] -->
m

<!-- b001652 | furniture | pages [17] -->
m

<!-- b001653 | furniture | pages [17] -->
m

<!-- b001654 | furniture | pages [17] -->
m

<!-- b001655 | furniture | pages [17] -->
m

<!-- b001656 | furniture | pages [17] -->
m

<!-- b001657 | furniture | pages [17] -->
m

<!-- b001658 | furniture | pages [17] -->
m

<!-- b001659 | furniture | pages [17] -->
m

<!-- b001660 | furniture | pages [17] -->
m

<!-- b001661 | furniture | pages [17] -->
m

<!-- b001662 | furniture | pages [17] -->
m

<!-- b001663 | furniture | pages [17] -->
m

<!-- b001664 | furniture | pages [17] -->
m

<!-- b001665 | furniture | pages [17] -->
m

<!-- b001666 | furniture | pages [17] -->
m

<!-- b001667 | furniture | pages [17] -->
m

<!-- b001668 | furniture | pages [17] -->
m

<!-- b001669 | furniture | pages [17] -->
m

<!-- b001670 | furniture | pages [17] -->
m

<!-- b001671 | furniture | pages [17] -->
m

<!-- b001672 | furniture | pages [17] -->
m

<!-- b001673 | furniture | pages [17] -->
m

<!-- b001674 | furniture | pages [17] -->
m

<!-- b001675 | furniture | pages [17] -->
m

<!-- b001676 | furniture | pages [17] -->
m

<!-- b001677 | furniture | pages [17] -->
m

<!-- b001678 | furniture | pages [17] -->
m

<!-- b001679 | furniture | pages [17] -->
m

<!-- b001680 | furniture | pages [17] -->
m

<!-- b001681 | furniture | pages [17] -->
m

<!-- b001682 | furniture | pages [17] -->
m

<!-- b001683 | furniture | pages [17] -->
m

<!-- b001684 | furniture | pages [17] -->
m

<!-- b001685 | furniture | pages [17] -->
m

<!-- b001686 | furniture | pages [17] -->
m

<!-- b001687 | furniture | pages [17] -->
m

<!-- b001688 | furniture | pages [17] -->
m

<!-- b001689 | furniture | pages [17] -->
m

<!-- b001690 | furniture | pages [17] -->
m

<!-- b001691 | furniture | pages [17] -->
m

<!-- b001692 | furniture | pages [17] -->
m

<!-- b001693 | furniture | pages [17] -->
m

<!-- b001694 | furniture | pages [17] -->
m

<!-- b001695 | furniture | pages [17] -->
m

<!-- b001696 | furniture | pages [17] -->
m

<!-- b001697 | furniture | pages [17] -->
m

<!-- b001698 | furniture | pages [17] -->
m

<!-- b001699 | furniture | pages [17] -->
m

<!-- b001700 | furniture | pages [17] -->
m

<!-- b001701 | furniture | pages [17] -->
m

<!-- b001702 | furniture | pages [17] -->
m

<!-- b001703 | furniture | pages [17] -->
m

<!-- b001704 | furniture | pages [17] -->
m

<!-- b001705 | furniture | pages [17] -->
m

<!-- b001706 | furniture | pages [17] -->
m

<!-- b001707 | furniture | pages [17] -->
m

<!-- b001708 | furniture | pages [17] -->
m

<!-- b001709 | furniture | pages [17] -->
m

<!-- b001710 | furniture | pages [17] -->
m

<!-- b001711 | furniture | pages [17] -->
m

<!-- b001712 | furniture | pages [17] -->
m

<!-- b001713 | furniture | pages [17] -->
m

<!-- b001714 | furniture | pages [17] -->
m

<!-- b001715 | furniture | pages [17] -->
m

<!-- b001716 | furniture | pages [17] -->
m

<!-- b001717 | furniture | pages [17] -->
m

<!-- b001718 | furniture | pages [17] -->
m

<!-- b001719 | furniture | pages [17] -->
m

<!-- b001720 | furniture | pages [17] -->
m

<!-- b001721 | furniture | pages [17] -->
m

<!-- b001722 | furniture | pages [17] -->
m

<!-- b001723 | furniture | pages [17] -->
m

<!-- b001724 | furniture | pages [17] -->
m

<!-- b001725 | furniture | pages [17] -->
m

<!-- b001726 | furniture | pages [17] -->
m

<!-- b001727 | furniture | pages [17] -->
m

<!-- b001728 | furniture | pages [17] -->
m

<!-- b001729 | furniture | pages [17] -->
m

<!-- b001730 | furniture | pages [17] -->
m

<!-- b001731 | furniture | pages [17] -->
m

<!-- b001732 | furniture | pages [17] -->
m

<!-- b001733 | furniture | pages [17] -->
m

<!-- b001734 | furniture | pages [17] -->
m

<!-- b001735 | furniture | pages [17] -->
m

<!-- b001736 | furniture | pages [17] -->
m

<!-- b001737 | furniture | pages [17] -->
m

<!-- b001738 | furniture | pages [17] -->
m

<!-- b001739 | furniture | pages [17] -->
m

<!-- b001740 | furniture | pages [17] -->
m

<!-- b001741 | furniture | pages [17] -->
m

<!-- b001742 | furniture | pages [17] -->
m

<!-- b001743 | furniture | pages [17] -->
m

<!-- b001744 | furniture | pages [17] -->
m

<!-- b001745 | furniture | pages [17] -->
m

<!-- b001746 | furniture | pages [17] -->
m

<!-- b001747 | furniture | pages [17] -->
m

<!-- b001748 | furniture | pages [17] -->
m

<!-- b001749 | furniture | pages [17] -->
m

<!-- b001750 | furniture | pages [17] -->
m

<!-- b001751 | furniture | pages [17] -->
m

<!-- b001752 | furniture | pages [17] -->
m

<!-- b001753 | furniture | pages [17] -->
m

<!-- b001754 | furniture | pages [17] -->
m

<!-- b001755 | furniture | pages [17] -->
m

<!-- b001756 | furniture | pages [17] -->
m

<!-- b001757 | furniture | pages [17] -->
m

<!-- b001758 | furniture | pages [17] -->
m

<!-- b001759 | furniture | pages [17] -->
m

<!-- b001760 | furniture | pages [17] -->
m

<!-- b001761 | furniture | pages [17] -->
m

<!-- b001762 | furniture | pages [17] -->
m

<!-- b001763 | furniture | pages [17] -->
m

<!-- b001764 | furniture | pages [17] -->
m

<!-- b001765 | furniture | pages [17] -->
m

<!-- b001766 | furniture | pages [17] -->
m

<!-- b001767 | furniture | pages [17] -->
m

<!-- b001768 | furniture | pages [17] -->
m

<!-- b001769 | furniture | pages [17] -->
m

<!-- b001770 | furniture | pages [17] -->
m

<!-- b001771 | furniture | pages [17] -->
m

<!-- b001772 | furniture | pages [17] -->
m

<!-- b001773 | furniture | pages [17] -->
m

<!-- b001774 | furniture | pages [17] -->
m

<!-- b001775 | furniture | pages [17] -->
m

<!-- b001776 | furniture | pages [17] -->
m

<!-- b001777 | furniture | pages [17] -->
m

<!-- b001778 | furniture | pages [17] -->
m

<!-- b001779 | furniture | pages [17] -->
m

<!-- b001780 | furniture | pages [17] -->
m

<!-- b001781 | furniture | pages [17] -->
m

<!-- b001782 | furniture | pages [17] -->
m

<!-- b001783 | furniture | pages [17] -->
m

<!-- b001784 | furniture | pages [17] -->
m

<!-- b001785 | furniture | pages [17] -->
m

<!-- b001786 | furniture | pages [17] -->
m

<!-- b001787 | furniture | pages [17] -->
m

<!-- b001788 | furniture | pages [17] -->
m

<!-- b001789 | furniture | pages [17] -->
m

<!-- b001790 | furniture | pages [17] -->
m

<!-- b001791 | furniture | pages [17] -->
m

<!-- b001792 | furniture | pages [17] -->
m

<!-- b001793 | furniture | pages [17] -->
m

<!-- b001794 | furniture | pages [17] -->
m

<!-- b001795 | furniture | pages [17] -->
m

<!-- b001796 | furniture | pages [17] -->
m

<!-- b001797 | furniture | pages [17] -->
m

<!-- b001798 | furniture | pages [17] -->
m

<!-- b001799 | furniture | pages [17] -->
m

<!-- b001800 | furniture | pages [17] -->
m

<!-- b001801 | furniture | pages [17] -->
m

<!-- b001802 | furniture | pages [17] -->
m

<!-- b001803 | furniture | pages [17] -->
m

<!-- b001804 | furniture | pages [17] -->
m

<!-- b001805 | furniture | pages [17] -->
m

<!-- b001806 | furniture | pages [17] -->
m

<!-- b001807 | furniture | pages [17] -->
m

<!-- b001808 | furniture | pages [17] -->
m

<!-- b001809 | furniture | pages [17] -->
m

<!-- b001810 | furniture | pages [17] -->
m

<!-- b001811 | furniture | pages [17] -->
m

<!-- b001812 | furniture | pages [17] -->
m

<!-- b001813 | furniture | pages [17] -->
m

<!-- b001814 | furniture | pages [17] -->
m

<!-- b001815 | furniture | pages [17] -->
m

<!-- b001816 | furniture | pages [17] -->
m

<!-- b001817 | furniture | pages [17] -->
m

<!-- b001818 | furniture | pages [17] -->
m

<!-- b001819 | furniture | pages [17] -->
m

<!-- b001820 | furniture | pages [17] -->
m

<!-- b001821 | furniture | pages [17] -->
m

<!-- b001822 | furniture | pages [17] -->
m

<!-- b001823 | furniture | pages [17] -->
m

<!-- b001824 | furniture | pages [17] -->
m

<!-- b001825 | furniture | pages [17] -->
m

<!-- b001826 | furniture | pages [17] -->
m

<!-- b001827 | furniture | pages [17] -->
m

<!-- b001828 | furniture | pages [17] -->
m

<!-- b001829 | furniture | pages [17] -->
m

<!-- b001830 | furniture | pages [17] -->
m

<!-- b001831 | furniture | pages [17] -->
m

<!-- b001832 | furniture | pages [17] -->
m

<!-- b001833 | furniture | pages [17] -->
m

<!-- b001834 | furniture | pages [17] -->
m

<!-- b001835 | furniture | pages [17] -->
m

<!-- b001836 | furniture | pages [17] -->
m

<!-- b001837 | furniture | pages [17] -->
m

<!-- b001838 | furniture | pages [17] -->
m

<!-- b001839 | furniture | pages [17] -->
m

<!-- b001840 | furniture | pages [17] -->
m

<!-- b001841 | furniture | pages [17] -->
m

<!-- b001842 | furniture | pages [17] -->
m

<!-- b001843 | furniture | pages [17] -->
m

<!-- b001844 | furniture | pages [17] -->
m

<!-- b001845 | furniture | pages [17] -->
m

<!-- b001846 | furniture | pages [17] -->
m

<!-- b001847 | furniture | pages [17] -->
m

<!-- b001848 | furniture | pages [17] -->
m

<!-- b001849 | furniture | pages [17] -->
m

<!-- b001850 | furniture | pages [17] -->
m

<!-- b001851 | furniture | pages [17] -->
m

<!-- b001852 | furniture | pages [17] -->
m

<!-- b001853 | furniture | pages [17] -->
m

<!-- b001854 | furniture | pages [17] -->
m

<!-- b001855 | furniture | pages [17] -->
m

<!-- b001856 | furniture | pages [17] -->
m

<!-- b001857 | furniture | pages [17] -->
m

<!-- b001858 | furniture | pages [17] -->
m

<!-- b001859 | furniture | pages [17] -->
m

<!-- b001860 | furniture | pages [17] -->
m

<!-- b001861 | furniture | pages [17] -->
m

<!-- b001862 | furniture | pages [17] -->
m

<!-- b001863 | furniture | pages [17] -->
m

<!-- b001864 | furniture | pages [17] -->
m

<!-- b001865 | furniture | pages [17] -->
m

<!-- b001866 | furniture | pages [17] -->
m

<!-- b001867 | furniture | pages [17] -->
m

<!-- b001868 | furniture | pages [17] -->
m

<!-- b001869 | furniture | pages [17] -->
m

<!-- b001870 | furniture | pages [17] -->
m

<!-- b001871 | furniture | pages [17] -->
m

<!-- b001872 | furniture | pages [17] -->
m

<!-- b001873 | furniture | pages [17] -->
m

<!-- b001874 | furniture | pages [17] -->
m

<!-- b001875 | furniture | pages [17] -->
m

<!-- b001876 | furniture | pages [17] -->
m

<!-- b001877 | furniture | pages [17] -->
m

<!-- b001878 | furniture | pages [17] -->
m

<!-- b001879 | furniture | pages [17] -->
m

<!-- b001880 | furniture | pages [17] -->
m

<!-- b001881 | furniture | pages [17] -->
m

<!-- b001882 | furniture | pages [17] -->
m

<!-- b001883 | furniture | pages [17] -->
m

<!-- b001884 | furniture | pages [17] -->
m

<!-- b001885 | furniture | pages [17] -->
m

<!-- b001886 | furniture | pages [17] -->
m

<!-- b001887 | furniture | pages [17] -->
m

<!-- b001888 | furniture | pages [17] -->
m

<!-- b001889 | furniture | pages [17] -->
m

<!-- b001890 | furniture | pages [17] -->
m

<!-- b001891 | furniture | pages [17] -->
m

<!-- b001892 | furniture | pages [17] -->
m

<!-- b001893 | furniture | pages [17] -->
m

<!-- b001894 | furniture | pages [17] -->
m

<!-- b001895 | furniture | pages [17] -->
m

<!-- b001896 | furniture | pages [17] -->
m

<!-- b001897 | furniture | pages [17] -->
m

<!-- b001898 | furniture | pages [17] -->
m

<!-- b001899 | furniture | pages [17] -->
m

<!-- b001900 | furniture | pages [17] -->
m

<!-- b001901 | furniture | pages [17] -->
m

<!-- b001902 | furniture | pages [17] -->
m

<!-- b001903 | furniture | pages [17] -->
m

<!-- b001904 | furniture | pages [17] -->
m

<!-- b001905 | furniture | pages [17] -->
m

<!-- b001906 | furniture | pages [17] -->
m

<!-- b001907 | furniture | pages [17] -->
m

<!-- b001908 | furniture | pages [17] -->
m

<!-- b001909 | furniture | pages [17] -->
m

<!-- b001910 | furniture | pages [17] -->
m

<!-- b001911 | furniture | pages [17] -->
m

<!-- b001912 | furniture | pages [17] -->
m

<!-- b001913 | furniture | pages [17] -->
m

<!-- b001914 | furniture | pages [17] -->
m

<!-- b001915 | furniture | pages [17] -->
m

<!-- b001916 | furniture | pages [17] -->
m

<!-- b001917 | furniture | pages [17] -->
m

<!-- b001918 | furniture | pages [17] -->
m

<!-- b001919 | furniture | pages [17] -->
m

<!-- b001920 | furniture | pages [17] -->
m

<!-- b001921 | furniture | pages [17] -->
m

<!-- b001922 | furniture | pages [18] -->
Team # 2500836

<!-- b001923 | furniture | pages [18] -->
Page 17 of 25

<!-- b001925 | prose | pages [18] -->
6.4.1 Selection of Characteristic Parameters of Raw Materials

<!-- b001926 | prose | pages [18] -->
By scanning the wear morphology, we can magnify the various wear characteristics of the stairs.

<!-- b001927 | heading | pages [18] -->
1. Stone

<!-- b001928 | prose | pages [18] -->
If the material is stone, we can obtain parameters such as crack size, which allows us to determine the stone's hardness, density, and wear coefficient. We collected relevant data from nearby quarries and performed a Pearson correlation analysis on this data to assess the correlation between the stair material and the stone from the nearby quarry, ultimately determining the material's source. If the material is wood, we obtained data on the tree ring width and crack size through image scanning, which provides information on the wood's species, fiber density, and age. We then applied the same method used for stone analysis to calculate the correlation coefficient and determine whether the material type matches.

<!-- b001929 | prose | pages [18] -->
1 mm 1 mm 1 mm

<!-- b001930 | caption | pages [18] -->
Figure 16: Wear morphology diagram L71

<!-- b001931 | prose | pages [18] -->
Background Noise

<!-- b001932 | prose | pages [18] -->
Fissure

<!-- b001933 | caption | pages [18] -->
Figure 17: Scan results [8]

<!-- b001934 | caption | pages [18] -->
Table 6: Parameter comparison table

<!-- b001935 | prose | pages [18] -->
Definition Stair Quarry Parameter 2.58 Density(g/cm³) 2.37~3.20 ρ k Wear rate(cm³/50cm²)(500N) 45.70 45.68(±0.28)

<!-- b001936 | prose | pages [18] -->
h 4.1 2~4.3 Mohs hardness

<!-- b001937 | prose | pages [18] -->
0.8 Porosity(%) 0.5~2.0 r

<!-- b001938 | prose | pages [18] -->
0.0001 Penetration 1.0e-6~0.0010 p

<!-- b001939 | heading | pages [18] -->
2. Wood

<!-- b001940 | prose | pages [18, 19] -->
For wood, we considered studying characteristics such as tree ring width, crack width, fiber density, and water absorption, as well as conducting carbon-14 dating. Then, following the same process as the stone analysis, we defined feature vectors for the wooden stairs and the original wood material and calculated the Pearson correlation coefficient to analyze the similarity.

<!-- b001941 | furniture | pages [19] -->
Team # 2500836                                                                   Page 18 of 25

<!-- b001943 | prose | pages [19] -->
Carbon-14 Dating：

<!-- b001944 | prose | pages [19] -->
(18)

<!-- b001945 | prose | pages [19] -->
If , it indicates that the age of the wooden stairs is consistent with the assumed age of the wood material used. 微信公众号：数学模型 a. poplar                     b. Metasequoia

<!-- b001946 | caption | pages [19] -->
Figure 18: Annual ring

<!-- b001947 | prose | pages [19] -->
微信号：MATHmodels

<!-- b001948 | heading | pages [19] -->
6.4.2  Person similarity test

<!-- b001949 | prose | pages [19] -->
In our research on the stone steps of the Leaning Tower of Pisa, we discovered that the stones for both sets of steps were sourced from nearby quarries. The stones for the internal steps of the Leaning Tower of Pisa were extracted from the renowned Carrara quarries [9]. We analyzed to compare the similarity between the steps and the original stones to identify the source of the materials. We assumed that the feature vectors for the steps and the rocks from the respective quarries are as follows:

<!-- b001950 | prose | pages [19] -->
where k is the wear coefficient, ρ is the density, h is the Mohs hardness, r is the porosity, and p is the penetration.

<!-- b001951 | prose | pages [19] -->
By calculation, and hypothesis testing was carried out, it turns out that the source of the staircase for the Leaning Tower of Pisa came from the nearby Carrara quarry.

<!-- b001952 | prose | pages [19] -->
Then, we used the Pearson correlation coefficient to calculate the similarity between the stairs and the raw stone.

<!-- b001953 | prose | pages [19] -->
(19)

<!-- b001954 | prose | pages [19] -->
Finally, the significance of the correlation coefficient was assessed based on the significance level (p-value). ⚫ p < 0.05 (or p < 0.01): Indicates a significant correlation, and the null hypothesis (that the two variables are uncorrelated) can be rejected. ⚫ p > 0.05: Indicates no significant correlation, and the null hypothesis cannot be rejected.

<!-- b001955 | prose | pages [19, 20] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Figure 19： Radar chart As shown in the figure above, the relevant parameters of this stone are similar to those of the Carrara quarry.

<!-- b001956 | furniture | pages [19] -->
m

<!-- b001957 | furniture | pages [19] -->
m

<!-- b001958 | furniture | pages [19] -->
m

<!-- b001959 | furniture | pages [19] -->
m

<!-- b001960 | furniture | pages [19] -->
m

<!-- b001961 | furniture | pages [19] -->
m

<!-- b001962 | furniture | pages [19] -->
m

<!-- b001963 | furniture | pages [19] -->
m

<!-- b001964 | furniture | pages [19] -->
m

<!-- b001965 | furniture | pages [19] -->
m

<!-- b001966 | furniture | pages [19] -->
m

<!-- b001967 | furniture | pages [19] -->
m

<!-- b001968 | furniture | pages [19] -->
m

<!-- b001969 | furniture | pages [19] -->
m

<!-- b001970 | furniture | pages [19] -->
m

<!-- b001971 | furniture | pages [19] -->
m

<!-- b001972 | furniture | pages [19] -->
m

<!-- b001973 | furniture | pages [19] -->
m

<!-- b001974 | furniture | pages [19] -->
m

<!-- b001975 | furniture | pages [19] -->
m

<!-- b001976 | furniture | pages [19] -->
m

<!-- b001977 | furniture | pages [19] -->
m

<!-- b001978 | furniture | pages [19] -->
m

<!-- b001979 | furniture | pages [19] -->
m

<!-- b001980 | furniture | pages [19] -->
m

<!-- b001981 | furniture | pages [19] -->
m

<!-- b001982 | furniture | pages [19] -->
m

<!-- b001983 | furniture | pages [19] -->
m

<!-- b001984 | furniture | pages [19] -->
m

<!-- b001985 | furniture | pages [19] -->
m

<!-- b001986 | furniture | pages [19] -->
m

<!-- b001987 | furniture | pages [19] -->
m

<!-- b001988 | furniture | pages [19] -->
m

<!-- b001989 | furniture | pages [19] -->
m

<!-- b001990 | furniture | pages [19] -->
m

<!-- b001991 | furniture | pages [19] -->
m

<!-- b001992 | furniture | pages [19] -->
m

<!-- b001993 | furniture | pages [19] -->
m

<!-- b001994 | furniture | pages [19] -->
m

<!-- b001995 | furniture | pages [19] -->
m

<!-- b001996 | furniture | pages [19] -->
m

<!-- b001997 | furniture | pages [19] -->
m

<!-- b001998 | furniture | pages [19] -->
m

<!-- b001999 | furniture | pages [19] -->
m

<!-- b002000 | furniture | pages [19] -->
m

<!-- b002001 | furniture | pages [19] -->
m

<!-- b002002 | furniture | pages [19] -->
m

<!-- b002003 | furniture | pages [19] -->
m

<!-- b002004 | furniture | pages [19] -->
m

<!-- b002005 | furniture | pages [19] -->
m

<!-- b002006 | furniture | pages [19] -->
m

<!-- b002007 | furniture | pages [19] -->
m

<!-- b002008 | furniture | pages [19] -->
m

<!-- b002009 | furniture | pages [19] -->
m

<!-- b002010 | furniture | pages [19] -->
m

<!-- b002011 | furniture | pages [19] -->
m

<!-- b002012 | furniture | pages [19] -->
m

<!-- b002013 | furniture | pages [19] -->
m

<!-- b002014 | furniture | pages [19] -->
m

<!-- b002015 | furniture | pages [19] -->
m

<!-- b002016 | furniture | pages [19] -->
m

<!-- b002017 | furniture | pages [19] -->
m

<!-- b002018 | furniture | pages [19] -->
m

<!-- b002019 | furniture | pages [19] -->
m

<!-- b002020 | furniture | pages [19] -->
m

<!-- b002021 | furniture | pages [19] -->
m

<!-- b002022 | furniture | pages [19] -->
m

<!-- b002023 | furniture | pages [19] -->
m

<!-- b002024 | furniture | pages [19] -->
m

<!-- b002025 | furniture | pages [19] -->
m

<!-- b002026 | furniture | pages [19] -->
m

<!-- b002027 | furniture | pages [19] -->
m

<!-- b002028 | furniture | pages [19] -->
m

<!-- b002029 | furniture | pages [19] -->
m

<!-- b002030 | furniture | pages [19] -->
m

<!-- b002031 | furniture | pages [19] -->
m

<!-- b002032 | furniture | pages [19] -->
m

<!-- b002033 | furniture | pages [19] -->
m

<!-- b002034 | furniture | pages [19] -->
m

<!-- b002035 | furniture | pages [19] -->
m

<!-- b002036 | furniture | pages [19] -->
m

<!-- b002037 | furniture | pages [19] -->
m

<!-- b002038 | furniture | pages [19] -->
m

<!-- b002039 | furniture | pages [19] -->
m

<!-- b002040 | furniture | pages [19] -->
m

<!-- b002041 | furniture | pages [19] -->
m

<!-- b002042 | furniture | pages [19] -->
m

<!-- b002043 | furniture | pages [19] -->
m

<!-- b002044 | furniture | pages [19] -->
m

<!-- b002045 | furniture | pages [19] -->
m

<!-- b002046 | furniture | pages [19] -->
m

<!-- b002047 | furniture | pages [19] -->
m

<!-- b002048 | furniture | pages [19] -->
m

<!-- b002049 | furniture | pages [19] -->
m

<!-- b002050 | furniture | pages [19] -->
m

<!-- b002051 | furniture | pages [19] -->
m

<!-- b002052 | furniture | pages [19] -->
m

<!-- b002053 | furniture | pages [19] -->
m

<!-- b002054 | furniture | pages [19] -->
m

<!-- b002055 | furniture | pages [19] -->
m

<!-- b002056 | furniture | pages [19] -->
m

<!-- b002057 | furniture | pages [19] -->
m

<!-- b002058 | furniture | pages [19] -->
m

<!-- b002059 | furniture | pages [19] -->
m

<!-- b002060 | furniture | pages [19] -->
m

<!-- b002061 | furniture | pages [19] -->
m

<!-- b002062 | furniture | pages [19] -->
m

<!-- b002063 | furniture | pages [19] -->
m

<!-- b002064 | furniture | pages [19] -->
m

<!-- b002065 | furniture | pages [19] -->
m

<!-- b002066 | furniture | pages [19] -->
m

<!-- b002067 | furniture | pages [19] -->
m

<!-- b002068 | furniture | pages [19] -->
m

<!-- b002069 | furniture | pages [19] -->
m

<!-- b002070 | furniture | pages [19] -->
m

<!-- b002071 | furniture | pages [19] -->
m

<!-- b002072 | furniture | pages [19] -->
m

<!-- b002073 | furniture | pages [19] -->
m

<!-- b002074 | furniture | pages [19] -->
m

<!-- b002075 | furniture | pages [19] -->
m

<!-- b002076 | furniture | pages [19] -->
m

<!-- b002077 | furniture | pages [19] -->
m

<!-- b002078 | furniture | pages [19] -->
m

<!-- b002079 | furniture | pages [19] -->
m

<!-- b002080 | furniture | pages [19] -->
m

<!-- b002081 | furniture | pages [19] -->
m

<!-- b002082 | furniture | pages [19] -->
m

<!-- b002083 | furniture | pages [19] -->
m

<!-- b002084 | furniture | pages [19] -->
m

<!-- b002085 | furniture | pages [19] -->
m

<!-- b002086 | furniture | pages [19] -->
m

<!-- b002087 | furniture | pages [19] -->
m

<!-- b002088 | furniture | pages [19] -->
m

<!-- b002089 | furniture | pages [19] -->
m

<!-- b002090 | furniture | pages [19] -->
m

<!-- b002091 | furniture | pages [19] -->
m

<!-- b002092 | furniture | pages [19] -->
m

<!-- b002093 | furniture | pages [19] -->
m

<!-- b002094 | furniture | pages [19] -->
m

<!-- b002095 | furniture | pages [19] -->
m

<!-- b002096 | furniture | pages [19] -->
m

<!-- b002097 | furniture | pages [19] -->
m

<!-- b002098 | furniture | pages [19] -->
m

<!-- b002099 | furniture | pages [19] -->
m

<!-- b002100 | furniture | pages [19] -->
m

<!-- b002101 | furniture | pages [19] -->
m

<!-- b002102 | furniture | pages [19] -->
m

<!-- b002103 | furniture | pages [19] -->
m

<!-- b002104 | furniture | pages [19] -->
m

<!-- b002105 | furniture | pages [19] -->
m

<!-- b002106 | furniture | pages [19] -->
m

<!-- b002107 | furniture | pages [19] -->
m

<!-- b002108 | furniture | pages [19] -->
m

<!-- b002109 | furniture | pages [19] -->
m

<!-- b002110 | furniture | pages [19] -->
m

<!-- b002111 | furniture | pages [19] -->
m

<!-- b002112 | furniture | pages [19] -->
m

<!-- b002113 | furniture | pages [19] -->
m

<!-- b002114 | furniture | pages [19] -->
m

<!-- b002115 | furniture | pages [19] -->
m

<!-- b002116 | furniture | pages [19] -->
m

<!-- b002117 | furniture | pages [19] -->
m

<!-- b002118 | furniture | pages [19] -->
m

<!-- b002119 | furniture | pages [19] -->
m

<!-- b002120 | furniture | pages [19] -->
m

<!-- b002121 | furniture | pages [19] -->
m

<!-- b002122 | furniture | pages [19] -->
m

<!-- b002123 | furniture | pages [19] -->
m

<!-- b002124 | furniture | pages [19] -->
m

<!-- b002125 | furniture | pages [19] -->
m

<!-- b002126 | furniture | pages [19] -->
m

<!-- b002127 | furniture | pages [19] -->
m

<!-- b002128 | furniture | pages [19] -->
m

<!-- b002129 | furniture | pages [19] -->
m

<!-- b002130 | furniture | pages [19] -->
m

<!-- b002131 | furniture | pages [19] -->
m

<!-- b002132 | furniture | pages [19] -->
m

<!-- b002133 | furniture | pages [19] -->
m

<!-- b002134 | furniture | pages [19] -->
m

<!-- b002135 | furniture | pages [19] -->
m

<!-- b002136 | furniture | pages [19] -->
m

<!-- b002137 | furniture | pages [19] -->
m

<!-- b002138 | furniture | pages [19] -->
m

<!-- b002139 | furniture | pages [19] -->
m

<!-- b002140 | furniture | pages [19] -->
m

<!-- b002141 | furniture | pages [19] -->
m

<!-- b002142 | furniture | pages [19] -->
m

<!-- b002143 | furniture | pages [19] -->
m

<!-- b002144 | furniture | pages [19] -->
m

<!-- b002145 | furniture | pages [19] -->
m

<!-- b002146 | furniture | pages [19] -->
m

<!-- b002147 | furniture | pages [19] -->
m

<!-- b002148 | furniture | pages [19] -->
m

<!-- b002149 | furniture | pages [19] -->
m

<!-- b002150 | furniture | pages [19] -->
m

<!-- b002151 | furniture | pages [19] -->
m

<!-- b002152 | furniture | pages [19] -->
m

<!-- b002153 | furniture | pages [19] -->
m

<!-- b002154 | furniture | pages [19] -->
m

<!-- b002155 | furniture | pages [19] -->
m

<!-- b002156 | furniture | pages [19] -->
m

<!-- b002157 | furniture | pages [19] -->
m

<!-- b002158 | furniture | pages [19] -->
m

<!-- b002159 | furniture | pages [19] -->
m

<!-- b002160 | furniture | pages [19] -->
m

<!-- b002161 | furniture | pages [19] -->
m

<!-- b002162 | furniture | pages [19] -->
m

<!-- b002163 | furniture | pages [19] -->
m

<!-- b002164 | furniture | pages [19] -->
m

<!-- b002165 | furniture | pages [19] -->
m

<!-- b002166 | furniture | pages [19] -->
m

<!-- b002167 | furniture | pages [19] -->
m

<!-- b002168 | furniture | pages [19] -->
m

<!-- b002169 | furniture | pages [19] -->
m

<!-- b002170 | furniture | pages [19] -->
m

<!-- b002171 | furniture | pages [19] -->
m

<!-- b002172 | furniture | pages [19] -->
m

<!-- b002173 | furniture | pages [19] -->
m

<!-- b002174 | furniture | pages [19] -->
m

<!-- b002175 | furniture | pages [19] -->
m

<!-- b002176 | furniture | pages [19] -->
m

<!-- b002177 | furniture | pages [19] -->
m

<!-- b002178 | furniture | pages [19] -->
m

<!-- b002179 | furniture | pages [19] -->
m

<!-- b002180 | furniture | pages [19] -->
m

<!-- b002181 | furniture | pages [19] -->
m

<!-- b002182 | furniture | pages [19] -->
m

<!-- b002183 | furniture | pages [19] -->
m

<!-- b002184 | furniture | pages [19] -->
m

<!-- b002185 | furniture | pages [19] -->
m

<!-- b002186 | furniture | pages [19] -->
m

<!-- b002187 | furniture | pages [19] -->
m

<!-- b002188 | furniture | pages [19] -->
m

<!-- b002189 | furniture | pages [19] -->
m

<!-- b002190 | furniture | pages [19] -->
m

<!-- b002191 | furniture | pages [19] -->
m

<!-- b002192 | furniture | pages [19] -->
m

<!-- b002193 | furniture | pages [19] -->
m

<!-- b002194 | furniture | pages [19] -->
m

<!-- b002195 | furniture | pages [19] -->
m

<!-- b002196 | furniture | pages [19] -->
m

<!-- b002197 | furniture | pages [19] -->
m

<!-- b002198 | furniture | pages [19] -->
m

<!-- b002199 | furniture | pages [19] -->
m

<!-- b002200 | furniture | pages [19] -->
m

<!-- b002201 | furniture | pages [19] -->
m

<!-- b002202 | furniture | pages [19] -->
m

<!-- b002203 | furniture | pages [19] -->
m

<!-- b002204 | furniture | pages [19] -->
m

<!-- b002205 | furniture | pages [19] -->
m

<!-- b002206 | furniture | pages [19] -->
m

<!-- b002207 | furniture | pages [19] -->
m

<!-- b002208 | furniture | pages [19] -->
m

<!-- b002209 | furniture | pages [19] -->
m

<!-- b002210 | furniture | pages [19] -->
m

<!-- b002211 | furniture | pages [19] -->
m

<!-- b002212 | furniture | pages [19] -->
m

<!-- b002213 | furniture | pages [19] -->
m

<!-- b002214 | furniture | pages [19] -->
m

<!-- b002215 | furniture | pages [19] -->
m

<!-- b002216 | furniture | pages [19] -->
m

<!-- b002217 | furniture | pages [19] -->
m

<!-- b002218 | furniture | pages [19] -->
m

<!-- b002219 | furniture | pages [19] -->
m

<!-- b002220 | furniture | pages [19] -->
m

<!-- b002221 | furniture | pages [19] -->
m

<!-- b002222 | furniture | pages [19] -->
m

<!-- b002223 | furniture | pages [19] -->
m

<!-- b002224 | furniture | pages [19] -->
m

<!-- b002225 | furniture | pages [19] -->
m

<!-- b002226 | furniture | pages [19] -->
m

<!-- b002227 | furniture | pages [19] -->
m

<!-- b002228 | furniture | pages [19] -->
m

<!-- b002229 | furniture | pages [19] -->
m

<!-- b002230 | furniture | pages [19] -->
m

<!-- b002231 | furniture | pages [19] -->
m

<!-- b002232 | furniture | pages [19] -->
m

<!-- b002233 | furniture | pages [19] -->
m

<!-- b002234 | furniture | pages [19] -->
m

<!-- b002235 | furniture | pages [19] -->
m

<!-- b002236 | furniture | pages [19] -->
m

<!-- b002237 | furniture | pages [19] -->
m

<!-- b002238 | furniture | pages [19] -->
m

<!-- b002239 | furniture | pages [19] -->
m

<!-- b002240 | furniture | pages [19] -->
m

<!-- b002241 | furniture | pages [19] -->
m

<!-- b002242 | furniture | pages [19] -->
m

<!-- b002243 | furniture | pages [19] -->
m

<!-- b002244 | furniture | pages [19] -->
m

<!-- b002245 | furniture | pages [19] -->
m

<!-- b002246 | furniture | pages [19] -->
m

<!-- b002247 | furniture | pages [19] -->
m

<!-- b002248 | furniture | pages [19] -->
m

<!-- b002249 | furniture | pages [19] -->
m

<!-- b002250 | furniture | pages [19] -->
m

<!-- b002251 | furniture | pages [19] -->
m

<!-- b002252 | furniture | pages [19] -->
m

<!-- b002253 | furniture | pages [19] -->
m

<!-- b002254 | furniture | pages [19] -->
m

<!-- b002255 | furniture | pages [19] -->
m

<!-- b002256 | furniture | pages [19] -->
m

<!-- b002257 | furniture | pages [19] -->
m

<!-- b002258 | furniture | pages [19] -->
m

<!-- b002259 | furniture | pages [19] -->
m

<!-- b002260 | furniture | pages [19] -->
m

<!-- b002261 | furniture | pages [19] -->
m

<!-- b002262 | furniture | pages [19] -->
m

<!-- b002263 | furniture | pages [19] -->
m

<!-- b002264 | furniture | pages [19] -->
m

<!-- b002265 | furniture | pages [19] -->
m

<!-- b002266 | furniture | pages [19] -->
m

<!-- b002267 | furniture | pages [19] -->
m

<!-- b002268 | furniture | pages [19] -->
m

<!-- b002269 | furniture | pages [19] -->
m

<!-- b002270 | furniture | pages [19] -->
m

<!-- b002271 | furniture | pages [19] -->
m

<!-- b002272 | furniture | pages [19] -->
m

<!-- b002273 | furniture | pages [19] -->
m

<!-- b002274 | furniture | pages [19] -->
m

<!-- b002275 | furniture | pages [19] -->
m

<!-- b002276 | furniture | pages [19] -->
m

<!-- b002277 | furniture | pages [19] -->
m

<!-- b002278 | furniture | pages [19] -->
m

<!-- b002279 | furniture | pages [19] -->
m

<!-- b002280 | furniture | pages [20] -->
Team # 2500836                                                                   Page 19 of 25

<!-- b002282 | heading | pages [20] -->
6.5  Research on temporal distribution of the Pedestrian Flow

<!-- b002283 | prose | pages [20] -->
The focus of this question is to study the temporal distribution of pedestrian traffic, employing instantaneous wear analysis. Assuming that the wear on steps caused by the majority of people in a short period and the minority over a long time is the same, but if the pedestrian flow is too high in a short time, it will exacerbate the wear, thus we obtained

<!-- b002284 | prose | pages [20] -->
(20)

<!-- b002285 | prose | pages [20] -->
where is the instantaneous pedestrian flow of the steps, and is the instantaneous wear depth. Let the uniform distribution of a flow of people with the quantity over a long period be

<!-- b002286 | prose | pages [20] -->
(21)

<!-- b002287 | prose | pages [20] -->
If the same number of pedestrians experience a peak in traffic within a short period, and since this peak period is very brief relative to a full day (24 hours), we assumed that this peak period can be approximated as an impulse function. Thus, we obtained

<!-- b002288 | prose | pages [20] -->
(22)

<!-- b002289 | prose | pages [20] -->
Therefore, the wear difference between a short-term peak in pedestrian traffic and a long-term uniform pedestrian flow is

<!-- b002290 | prose | pages [20] -->
(23)

<!-- b002291 | prose | pages [20] -->
where is the time of one day. This shows that the excessive flow of people in a short period can indeed increase wear and tear.

<!-- b002292 | prose | pages [20, 21] -->
关注数学模型 By scanning images of the stairs at the Leaning Tower of Pisa taken on two consecutive days, we can assess the wear on the stairs after one day's usage. Then, by investigating the number of visitors to the Leaning Tower of Pisa on that day, we can use the following equation to determine whether the pedestrian traffic for that day experienced a short-term peak or was uniformly distributed over a longer period. 微信公众号：数学模型 ⚫ explained that the pedestrian flow for that day experienced a short-term

<!-- b002293 | furniture | pages [20] -->
2

<!-- b002294 | furniture | pages [20] -->
MATHmodels

<!-- b002295 | furniture | pages [20] -->
获取更多资讯

<!-- b002296 | furniture | pages [21] -->
Team # 2500836                                                                   Page 20 of 25

<!-- b002298 | prose | pages [21] -->
peak;

<!-- b002299 | prose | pages [21] -->
⚫ explained that the pedestrian flow for that day was uniformly distributed

<!-- b002300 | prose | pages [21] -->
over a longer period.

<!-- b002301 | prose | pages [21] -->
Moreover, when a large number of pedestrians use the stairs in a short period, congestion occurs, and pedestrians tend to walk in a staggered manner, which results in the widening of the depressions. Therefore, by comparing the width changes of the depressions from scanning images of two consecutive days, we can also determine whether the pedestrian traffic on that day experienced a short- 微信号：MATHmodels term peak or was uniformly distributed over a longer period.

<!-- b002302 | prose | pages [21] -->
According to Equation (), we calculated that

<!-- b002303 | prose | pages [21] -->
Since 0.205＜0.241, we determined that there were a small number of people using the stairs over a longer time.

<!-- b002304 | prose | pages [21] -->
By consulting the official website of the Leaning Tower of Pisa, we found that the management of the tower is very strict, typically allowing only 20-30 visitors to enter at a time, with each visit lasting 20-30 minutes. This indicates that, in reality, the stairs are used uniformly over a long period, which aligns with the results of our model, thereby confirming the feasibility and reasonableness of the model.

<!-- b002305 | heading | pages [21] -->
7 Sensitivity Analysis

<!-- b002306 | heading | pages [21] -->
7.1  Sensitivity Analysis of 2-D Normal Distribution Model of Wear Depth

<!-- b002307 | prose | pages [21] -->
For the model

<!-- b002308 | prose | pages [21] -->
， we tested the effect of the parameter on the wear depth and the shape of the wear depression, The following is a longitudinal section of the steps at x = 0 when takes 5, 10, 15, and 20, respectively.

<!-- b002309 | prose | pages [21, 22] -->
Figure 20：Sensitivity Analysis of Wear Depth Distribution m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m From the image, we found that as gradually increases, the wear depth gradually decreases, the m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m wear depression changes from concentration to scattered, and the overall shape becomes flat. Therefore, m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m it is a reasonable and accurate choice to describe the wear degree, and the model has a high sensitivity. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b002310 | furniture | pages [22] -->
m

<!-- b002311 | furniture | pages [22] -->
m

<!-- b002312 | furniture | pages [22] -->
m

<!-- b002313 | furniture | pages [22] -->
m

<!-- b002314 | furniture | pages [22] -->
m

<!-- b002315 | furniture | pages [22] -->
m

<!-- b002316 | furniture | pages [22] -->
m

<!-- b002317 | furniture | pages [22] -->
m

<!-- b002318 | furniture | pages [22] -->
m

<!-- b002319 | furniture | pages [22] -->
m

<!-- b002320 | furniture | pages [22] -->
m

<!-- b002321 | furniture | pages [22] -->
m

<!-- b002322 | furniture | pages [22] -->
m

<!-- b002323 | furniture | pages [22] -->
m

<!-- b002324 | furniture | pages [22] -->
m

<!-- b002325 | furniture | pages [22] -->
m

<!-- b002326 | furniture | pages [22] -->
m

<!-- b002327 | furniture | pages [22] -->
m

<!-- b002328 | furniture | pages [22] -->
m

<!-- b002329 | furniture | pages [22] -->
m

<!-- b002330 | furniture | pages [22] -->
m

<!-- b002331 | furniture | pages [22] -->
m

<!-- b002332 | furniture | pages [22] -->
m

<!-- b002333 | furniture | pages [22] -->
m

<!-- b002334 | furniture | pages [22] -->
m

<!-- b002335 | furniture | pages [22] -->
m

<!-- b002336 | furniture | pages [22] -->
m

<!-- b002337 | furniture | pages [22] -->
m

<!-- b002338 | furniture | pages [22] -->
m

<!-- b002339 | furniture | pages [22] -->
m

<!-- b002340 | furniture | pages [22] -->
m

<!-- b002341 | furniture | pages [22] -->
m

<!-- b002342 | furniture | pages [22] -->
m

<!-- b002343 | furniture | pages [22] -->
m

<!-- b002344 | furniture | pages [22] -->
m

<!-- b002345 | furniture | pages [22] -->
m

<!-- b002346 | furniture | pages [22] -->
m

<!-- b002347 | furniture | pages [22] -->
m

<!-- b002348 | furniture | pages [22] -->
Team # 2500836                                                                   Page 21 of 25

<!-- b002349 | furniture | pages [22] -->
m

<!-- b002350 | furniture | pages [22] -->
m

<!-- b002351 | furniture | pages [22] -->
m

<!-- b002352 | furniture | pages [22] -->
m

<!-- b002353 | furniture | pages [22] -->
m

<!-- b002354 | furniture | pages [22] -->
m

<!-- b002355 | furniture | pages [22] -->
m

<!-- b002356 | furniture | pages [22] -->
m

<!-- b002357 | furniture | pages [22] -->
m

<!-- b002358 | furniture | pages [22] -->
m

<!-- b002359 | furniture | pages [22] -->
m

<!-- b002360 | furniture | pages [22] -->
m

<!-- b002361 | furniture | pages [22] -->
m

<!-- b002362 | furniture | pages [22] -->
m

<!-- b002363 | furniture | pages [22] -->
m

<!-- b002364 | furniture | pages [22] -->
m

<!-- b002365 | furniture | pages [22] -->
m

<!-- b002366 | furniture | pages [22] -->
m

<!-- b002367 | furniture | pages [22] -->
m

<!-- b002368 | furniture | pages [22] -->
m

<!-- b002369 | furniture | pages [22] -->
m

<!-- b002370 | furniture | pages [22] -->
m

<!-- b002371 | furniture | pages [22] -->
m

<!-- b002372 | furniture | pages [22] -->
m

<!-- b002373 | furniture | pages [22] -->
m

<!-- b002374 | furniture | pages [22] -->
m

<!-- b002375 | furniture | pages [22] -->
m

<!-- b002376 | furniture | pages [22] -->
m

<!-- b002377 | furniture | pages [22] -->
m

<!-- b002378 | furniture | pages [22] -->
m

<!-- b002379 | furniture | pages [22] -->
m

<!-- b002380 | furniture | pages [22] -->
m

<!-- b002381 | furniture | pages [22] -->
m

<!-- b002382 | furniture | pages [22] -->
m

<!-- b002383 | furniture | pages [22] -->
m

<!-- b002384 | furniture | pages [22] -->
m

<!-- b002385 | furniture | pages [22] -->
m

<!-- b002386 | furniture | pages [22] -->
m

<!-- b002387 | furniture | pages [22] -->
m

<!-- b002388 | furniture | pages [22] -->
m

<!-- b002389 | furniture | pages [22] -->
m

<!-- b002390 | furniture | pages [22] -->
m

<!-- b002391 | furniture | pages [22] -->
m

<!-- b002392 | furniture | pages [22] -->
m

<!-- b002393 | furniture | pages [22] -->
m

<!-- b002394 | furniture | pages [22] -->
m

<!-- b002395 | furniture | pages [22] -->
m

<!-- b002396 | furniture | pages [22] -->
m

<!-- b002397 | furniture | pages [22] -->
m

<!-- b002398 | furniture | pages [22] -->
m

<!-- b002399 | furniture | pages [22] -->
m

<!-- b002400 | furniture | pages [22] -->
m

<!-- b002401 | furniture | pages [22] -->
m

<!-- b002402 | furniture | pages [22] -->
m

<!-- b002403 | furniture | pages [22] -->
m

<!-- b002404 | furniture | pages [22] -->
m

<!-- b002405 | furniture | pages [22] -->
m

<!-- b002406 | furniture | pages [22] -->
m

<!-- b002407 | furniture | pages [22] -->
m

<!-- b002408 | furniture | pages [22] -->
m

<!-- b002409 | furniture | pages [22] -->
m

<!-- b002410 | furniture | pages [22] -->
m

<!-- b002411 | furniture | pages [22] -->
m

<!-- b002412 | furniture | pages [22] -->
m

<!-- b002413 | furniture | pages [22] -->
m

<!-- b002414 | furniture | pages [22] -->
m

<!-- b002415 | furniture | pages [22] -->
m

<!-- b002416 | furniture | pages [22] -->
m

<!-- b002417 | furniture | pages [22] -->
m

<!-- b002418 | furniture | pages [22] -->
m

<!-- b002419 | furniture | pages [22] -->
m

<!-- b002420 | furniture | pages [22] -->
m

<!-- b002421 | furniture | pages [22] -->
m

<!-- b002422 | furniture | pages [22] -->
m

<!-- b002423 | furniture | pages [22] -->
m

<!-- b002424 | furniture | pages [22] -->
m

<!-- b002425 | furniture | pages [22] -->
m

<!-- b002426 | furniture | pages [22] -->
m

<!-- b002427 | furniture | pages [22] -->
m

<!-- b002428 | furniture | pages [22] -->
m

<!-- b002429 | furniture | pages [22] -->
m

<!-- b002430 | furniture | pages [22] -->
m

<!-- b002431 | furniture | pages [22] -->
m

<!-- b002432 | furniture | pages [22] -->
m

<!-- b002433 | furniture | pages [22] -->
m

<!-- b002434 | furniture | pages [22] -->
m

<!-- b002435 | furniture | pages [22] -->
m

<!-- b002436 | furniture | pages [22] -->
m

<!-- b002437 | furniture | pages [22] -->
m

<!-- b002438 | furniture | pages [22] -->
m

<!-- b002439 | furniture | pages [22] -->
m

<!-- b002440 | furniture | pages [22] -->
m

<!-- b002441 | furniture | pages [22] -->
m

<!-- b002442 | furniture | pages [22] -->
m

<!-- b002443 | furniture | pages [22] -->
m

<!-- b002444 | furniture | pages [22] -->
m

<!-- b002445 | furniture | pages [22] -->
m

<!-- b002446 | furniture | pages [22] -->
m

<!-- b002447 | furniture | pages [22] -->
m

<!-- b002448 | furniture | pages [22] -->
m

<!-- b002449 | furniture | pages [22] -->
m

<!-- b002450 | furniture | pages [22] -->
m

<!-- b002451 | furniture | pages [22] -->
m

<!-- b002452 | furniture | pages [22] -->
m

<!-- b002453 | furniture | pages [22] -->
m

<!-- b002454 | furniture | pages [22] -->
m

<!-- b002455 | furniture | pages [22] -->
m

<!-- b002456 | furniture | pages [22] -->
m

<!-- b002457 | furniture | pages [22] -->
m

<!-- b002458 | furniture | pages [22] -->
m

<!-- b002459 | furniture | pages [22] -->
m

<!-- b002460 | furniture | pages [22] -->
m

<!-- b002461 | furniture | pages [22] -->
m

<!-- b002462 | furniture | pages [22] -->
m

<!-- b002463 | furniture | pages [22] -->
m

<!-- b002464 | furniture | pages [22] -->
m

<!-- b002465 | furniture | pages [22] -->
m

<!-- b002466 | furniture | pages [22] -->
m

<!-- b002467 | furniture | pages [22] -->
m

<!-- b002468 | furniture | pages [22] -->
m

<!-- b002469 | furniture | pages [22] -->
m

<!-- b002470 | furniture | pages [22] -->
m

<!-- b002471 | furniture | pages [22] -->
m

<!-- b002472 | furniture | pages [22] -->
m

<!-- b002473 | furniture | pages [22] -->
m

<!-- b002474 | furniture | pages [22] -->
m

<!-- b002475 | furniture | pages [22] -->
m

<!-- b002476 | furniture | pages [22] -->
m

<!-- b002477 | furniture | pages [22] -->
m

<!-- b002478 | furniture | pages [22] -->
m

<!-- b002479 | furniture | pages [22] -->
m

<!-- b002480 | furniture | pages [22] -->
m

<!-- b002481 | furniture | pages [22] -->
m

<!-- b002482 | furniture | pages [22] -->
m

<!-- b002483 | furniture | pages [22] -->
m

<!-- b002484 | furniture | pages [22] -->
m

<!-- b002485 | furniture | pages [22] -->
m

<!-- b002486 | furniture | pages [22] -->
m

<!-- b002487 | furniture | pages [22] -->
m

<!-- b002488 | furniture | pages [22] -->
m

<!-- b002489 | furniture | pages [22] -->
m

<!-- b002490 | furniture | pages [22] -->
m

<!-- b002491 | furniture | pages [22] -->
m

<!-- b002492 | furniture | pages [22] -->
m

<!-- b002493 | furniture | pages [22] -->
m

<!-- b002494 | furniture | pages [22] -->
m

<!-- b002495 | furniture | pages [22] -->
m

<!-- b002496 | furniture | pages [22] -->
m

<!-- b002497 | furniture | pages [22] -->
m

<!-- b002498 | furniture | pages [22] -->
m

<!-- b002499 | furniture | pages [22] -->
m

<!-- b002500 | furniture | pages [22] -->
m

<!-- b002501 | furniture | pages [22] -->
m

<!-- b002502 | furniture | pages [22] -->
m

<!-- b002503 | furniture | pages [22] -->
m

<!-- b002504 | furniture | pages [22] -->
m

<!-- b002505 | furniture | pages [22] -->
m

<!-- b002506 | furniture | pages [22] -->
m

<!-- b002507 | furniture | pages [22] -->
m

<!-- b002508 | furniture | pages [22] -->
m

<!-- b002509 | furniture | pages [22] -->
m

<!-- b002510 | furniture | pages [22] -->
m

<!-- b002511 | furniture | pages [22] -->
m

<!-- b002512 | furniture | pages [22] -->
m

<!-- b002513 | furniture | pages [22] -->
m

<!-- b002514 | furniture | pages [22] -->
m

<!-- b002515 | furniture | pages [22] -->
m

<!-- b002516 | furniture | pages [22] -->
m

<!-- b002517 | furniture | pages [22] -->
m

<!-- b002518 | furniture | pages [22] -->
m

<!-- b002519 | furniture | pages [22] -->
m

<!-- b002520 | furniture | pages [22] -->
m

<!-- b002521 | furniture | pages [22] -->
m

<!-- b002522 | furniture | pages [22] -->
m

<!-- b002523 | furniture | pages [22] -->
m

<!-- b002524 | furniture | pages [22] -->
m

<!-- b002525 | furniture | pages [22] -->
m

<!-- b002526 | furniture | pages [22] -->
m

<!-- b002527 | furniture | pages [22] -->
m

<!-- b002528 | furniture | pages [22] -->
m

<!-- b002529 | furniture | pages [22] -->
m

<!-- b002530 | furniture | pages [22] -->
m

<!-- b002531 | furniture | pages [22] -->
m

<!-- b002532 | furniture | pages [22] -->
m

<!-- b002533 | furniture | pages [22] -->
m

<!-- b002534 | furniture | pages [22] -->
m

<!-- b002535 | furniture | pages [22] -->
m

<!-- b002536 | furniture | pages [22] -->
m

<!-- b002537 | furniture | pages [22] -->
m

<!-- b002538 | furniture | pages [22] -->
m

<!-- b002539 | furniture | pages [22] -->
m

<!-- b002540 | furniture | pages [22] -->
m

<!-- b002541 | furniture | pages [22] -->
m

<!-- b002542 | furniture | pages [22] -->
m

<!-- b002543 | furniture | pages [22] -->
m

<!-- b002544 | furniture | pages [22] -->
m

<!-- b002545 | furniture | pages [22] -->
m

<!-- b002546 | furniture | pages [22] -->
m

<!-- b002547 | furniture | pages [22] -->
m

<!-- b002548 | furniture | pages [22] -->
m

<!-- b002549 | furniture | pages [22] -->
m

<!-- b002550 | furniture | pages [22] -->
m

<!-- b002551 | furniture | pages [22] -->
m

<!-- b002552 | furniture | pages [22] -->
m

<!-- b002553 | furniture | pages [22] -->
m

<!-- b002554 | furniture | pages [22] -->
m

<!-- b002555 | furniture | pages [22] -->
m

<!-- b002556 | furniture | pages [22] -->
m

<!-- b002557 | furniture | pages [22] -->
m

<!-- b002558 | furniture | pages [22] -->
m

<!-- b002559 | furniture | pages [22] -->
m

<!-- b002560 | furniture | pages [22] -->
m

<!-- b002561 | furniture | pages [22] -->
m

<!-- b002562 | furniture | pages [22] -->
m

<!-- b002563 | furniture | pages [22] -->
m

<!-- b002564 | furniture | pages [22] -->
m

<!-- b002565 | furniture | pages [22] -->
m

<!-- b002566 | furniture | pages [22] -->
m

<!-- b002567 | furniture | pages [22] -->
m

<!-- b002568 | furniture | pages [22] -->
m

<!-- b002569 | furniture | pages [22] -->
m

<!-- b002570 | furniture | pages [22] -->
m

<!-- b002571 | furniture | pages [22] -->
m

<!-- b002572 | furniture | pages [22] -->
m

<!-- b002574 | heading | pages [22] -->
7.2 Sensitivity Analysis of Continuity Equation for Simulating Walking Patterns

<!-- b002575 | prose | pages [22] -->
For the model

<!-- b002576 | prose | pages [22] -->
, we tested the effect of N (x, y, t) by increasing the number of people N (x, y, t) from 0 to 0.06.

<!-- b002577 | prose | pages [22] -->
Figure 21：Sensitivity Analysis of Continuity Equation for Simulating Walking Patterns As can be seen from Figure 21, the red area is single passage, and the green area is parallel passage. The density of traffic increases with the number of people passing per second. Thus, the model has a high sensitivity for determining whether people use stairs alone or individually.

<!-- b002578 | heading | pages [22] -->
8 Strengths and Weaknesses

<!-- b002579 | heading | pages [22] -->
8.1 Strengths

<!-- b002580 | prose | pages [22] -->
◆ The two-dimensional normal distribution model not only matches the description of the wear depth distribution, but also describes the wear difference of the value of the parameters in different positions by the force habit of people going up and down in different locations. ◆ In order to improve the fitting effect of the two-dimensional normal distribution model, we use the advanced machine learning algorithm, particle swarm optimization algorithm (PSO), which not only improves the efficiency of the fitting, but also enhances the accuracy of the fitting. ◆ It is a very innovative idea to abstract the crowd flow into liquid flow, and then use Navier- Stokes Equations to model the population flow. Finite difference method (FDM) is a very mature solution method to solve the numerical solution of the model, and the solution effect has high accuracy. ◆ We also innovatively introduced the impulse function to simulate the situation of a large number of people use stairs in a short time, solving the problem of judging whether the staircase is used by a large number of people in a short time or by a few people for a long time.

<!-- b002581 | prose | pages [22] -->
关注数学模型

<!-- b002582 | furniture | pages [22] -->
2

<!-- b002583 | furniture | pages [22] -->
MATHmodels

<!-- b002584 | furniture | pages [22] -->
获取更多资讯

<!-- b002585 | furniture | pages [23] -->
Team # 2500836                                                                   Page 22 of 25

<!-- b002586 | heading | pages [23] -->
8.2  Weaknesses

<!-- b002587 | prose | pages [23] -->
◆ We did not use more advanced instruments to the field to make more precise measurements of the wear on the stairs. ◆ Due to space limitation, we have only studied the worn stairs inside the Leaning Tower of Pisa, not the richer variety of stairs. 微信公众号：数学模型

<!-- b002588 | heading | pages [23] -->
9 Conclusion

<!-- b002589 | prose | pages [23] -->
In this study, based on the Archard wear model, we incorporated wear depth, wear coefficient, and pedestrian traffic into our calculations and developed an extended model. Given the wear depth, we derived the pedestrian traffic, representing the usage frequency. Additionally, through the analysis of human biomechanics and kinematics, we established a preference index model to distinguish between ascending and descending movements. Furthermore, by drawing an analogy between pedestrian flow and fluid motion, we applied the Navier-Stokes equations to determine pedestrian traffic by solving for density. Moreover, we utilized the Pearson correlation coefficient to assess the material's origin. This paper provides significant theoretical support for the preservation of historical buildings, 微信号：MATHmodels the evaluation of architectural lifespan, and related studies.

<!-- b002590 | prose | pages [23] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b002591 | furniture | pages [23] -->
m

<!-- b002592 | furniture | pages [23] -->
m

<!-- b002593 | furniture | pages [23] -->
m

<!-- b002594 | furniture | pages [23] -->
m

<!-- b002595 | furniture | pages [23] -->
m

<!-- b002596 | furniture | pages [23] -->
m

<!-- b002597 | furniture | pages [23] -->
m

<!-- b002598 | furniture | pages [23] -->
m

<!-- b002599 | furniture | pages [23] -->
m

<!-- b002600 | furniture | pages [23] -->
m

<!-- b002601 | furniture | pages [23] -->
m

<!-- b002602 | furniture | pages [23] -->
m

<!-- b002603 | furniture | pages [23] -->
m

<!-- b002604 | furniture | pages [23] -->
m

<!-- b002605 | furniture | pages [23] -->
m

<!-- b002606 | furniture | pages [23] -->
m

<!-- b002607 | furniture | pages [23] -->
m

<!-- b002608 | furniture | pages [23] -->
m

<!-- b002609 | furniture | pages [23] -->
m

<!-- b002610 | furniture | pages [23] -->
m

<!-- b002611 | furniture | pages [23] -->
m

<!-- b002612 | furniture | pages [23] -->
m

<!-- b002613 | furniture | pages [23] -->
m

<!-- b002614 | furniture | pages [23] -->
m

<!-- b002615 | furniture | pages [23] -->
m

<!-- b002616 | furniture | pages [23] -->
m

<!-- b002617 | furniture | pages [23] -->
m

<!-- b002618 | furniture | pages [23] -->
m

<!-- b002619 | furniture | pages [23] -->
m

<!-- b002620 | furniture | pages [23] -->
m

<!-- b002621 | furniture | pages [23] -->
m

<!-- b002622 | furniture | pages [23] -->
m

<!-- b002623 | furniture | pages [23] -->
m

<!-- b002624 | furniture | pages [23] -->
m

<!-- b002625 | furniture | pages [23] -->
m

<!-- b002626 | furniture | pages [23] -->
m

<!-- b002627 | furniture | pages [23] -->
m

<!-- b002628 | furniture | pages [23] -->
m

<!-- b002629 | furniture | pages [23] -->
m

<!-- b002630 | furniture | pages [23] -->
m

<!-- b002631 | furniture | pages [23] -->
m

<!-- b002632 | furniture | pages [23] -->
m

<!-- b002633 | furniture | pages [23] -->
m

<!-- b002634 | furniture | pages [23] -->
m

<!-- b002635 | furniture | pages [23] -->
m

<!-- b002636 | furniture | pages [23] -->
m

<!-- b002637 | furniture | pages [23] -->
m

<!-- b002638 | furniture | pages [23] -->
m

<!-- b002639 | furniture | pages [23] -->
m

<!-- b002640 | furniture | pages [23] -->
m

<!-- b002641 | furniture | pages [23] -->
m

<!-- b002642 | furniture | pages [23] -->
m

<!-- b002643 | furniture | pages [23] -->
m

<!-- b002644 | furniture | pages [23] -->
m

<!-- b002645 | furniture | pages [23] -->
m

<!-- b002646 | furniture | pages [23] -->
m

<!-- b002647 | furniture | pages [23] -->
m

<!-- b002648 | furniture | pages [23] -->
m

<!-- b002649 | furniture | pages [23] -->
m

<!-- b002650 | furniture | pages [23] -->
m

<!-- b002651 | furniture | pages [23] -->
m

<!-- b002652 | furniture | pages [23] -->
m

<!-- b002653 | furniture | pages [23] -->
m

<!-- b002654 | furniture | pages [23] -->
m

<!-- b002655 | furniture | pages [23] -->
m

<!-- b002656 | furniture | pages [23] -->
m

<!-- b002657 | furniture | pages [23] -->
m

<!-- b002658 | furniture | pages [23] -->
m

<!-- b002659 | furniture | pages [23] -->
m

<!-- b002660 | furniture | pages [23] -->
m

<!-- b002661 | furniture | pages [23] -->
m

<!-- b002662 | furniture | pages [23] -->
m

<!-- b002663 | furniture | pages [23] -->
m

<!-- b002664 | furniture | pages [23] -->
m

<!-- b002665 | furniture | pages [23] -->
m

<!-- b002666 | furniture | pages [23] -->
m

<!-- b002667 | furniture | pages [23] -->
m

<!-- b002668 | furniture | pages [23] -->
m

<!-- b002669 | furniture | pages [23] -->
m

<!-- b002670 | furniture | pages [23] -->
m

<!-- b002671 | furniture | pages [23] -->
m

<!-- b002672 | furniture | pages [23] -->
m

<!-- b002673 | furniture | pages [23] -->
m

<!-- b002674 | furniture | pages [23] -->
m

<!-- b002675 | furniture | pages [23] -->
m

<!-- b002676 | furniture | pages [23] -->
m

<!-- b002677 | furniture | pages [23] -->
m

<!-- b002678 | furniture | pages [23] -->
m

<!-- b002679 | furniture | pages [23] -->
m

<!-- b002680 | furniture | pages [23] -->
m

<!-- b002681 | furniture | pages [23] -->
m

<!-- b002682 | furniture | pages [23] -->
m

<!-- b002683 | furniture | pages [23] -->
m

<!-- b002684 | furniture | pages [23] -->
m

<!-- b002685 | furniture | pages [23] -->
m

<!-- b002686 | furniture | pages [23] -->
m

<!-- b002687 | furniture | pages [23] -->
m

<!-- b002688 | furniture | pages [23] -->
m

<!-- b002689 | furniture | pages [23] -->
m

<!-- b002690 | furniture | pages [23] -->
m

<!-- b002691 | furniture | pages [23] -->
m

<!-- b002692 | furniture | pages [23] -->
m

<!-- b002693 | furniture | pages [23] -->
m

<!-- b002694 | furniture | pages [23] -->
m

<!-- b002695 | furniture | pages [23] -->
m

<!-- b002696 | furniture | pages [23] -->
m

<!-- b002697 | furniture | pages [23] -->
m

<!-- b002698 | furniture | pages [23] -->
m

<!-- b002699 | furniture | pages [23] -->
m

<!-- b002700 | furniture | pages [23] -->
m

<!-- b002701 | furniture | pages [23] -->
m

<!-- b002702 | furniture | pages [23] -->
m

<!-- b002703 | furniture | pages [23] -->
m

<!-- b002704 | furniture | pages [23] -->
m

<!-- b002705 | furniture | pages [23] -->
m

<!-- b002706 | furniture | pages [23] -->
m

<!-- b002707 | furniture | pages [23] -->
m

<!-- b002708 | furniture | pages [23] -->
m

<!-- b002709 | furniture | pages [23] -->
m

<!-- b002710 | furniture | pages [23] -->
m

<!-- b002711 | furniture | pages [23] -->
m

<!-- b002712 | furniture | pages [23] -->
m

<!-- b002713 | furniture | pages [23] -->
m

<!-- b002714 | furniture | pages [23] -->
m

<!-- b002715 | furniture | pages [23] -->
m

<!-- b002716 | furniture | pages [23] -->
m

<!-- b002717 | furniture | pages [23] -->
m

<!-- b002718 | furniture | pages [23] -->
m

<!-- b002719 | furniture | pages [23] -->
m

<!-- b002720 | furniture | pages [23] -->
m

<!-- b002721 | furniture | pages [23] -->
m

<!-- b002722 | furniture | pages [23] -->
m

<!-- b002723 | furniture | pages [23] -->
m

<!-- b002724 | furniture | pages [23] -->
m

<!-- b002725 | furniture | pages [23] -->
m

<!-- b002726 | furniture | pages [23] -->
m

<!-- b002727 | furniture | pages [23] -->
m

<!-- b002728 | furniture | pages [23] -->
m

<!-- b002729 | furniture | pages [23] -->
m

<!-- b002730 | furniture | pages [23] -->
m

<!-- b002731 | furniture | pages [23] -->
m

<!-- b002732 | furniture | pages [23] -->
m

<!-- b002733 | furniture | pages [23] -->
m

<!-- b002734 | furniture | pages [23] -->
m

<!-- b002735 | furniture | pages [23] -->
m

<!-- b002736 | furniture | pages [23] -->
m

<!-- b002737 | furniture | pages [23] -->
m

<!-- b002738 | furniture | pages [23] -->
m

<!-- b002739 | furniture | pages [23] -->
m

<!-- b002740 | furniture | pages [23] -->
m

<!-- b002741 | furniture | pages [23] -->
m

<!-- b002742 | furniture | pages [23] -->
m

<!-- b002743 | furniture | pages [23] -->
m

<!-- b002744 | furniture | pages [23] -->
m

<!-- b002745 | furniture | pages [23] -->
m

<!-- b002746 | furniture | pages [23] -->
m

<!-- b002747 | furniture | pages [23] -->
m

<!-- b002748 | furniture | pages [23] -->
m

<!-- b002749 | furniture | pages [23] -->
m

<!-- b002750 | furniture | pages [23] -->
m

<!-- b002751 | furniture | pages [23] -->
m

<!-- b002752 | furniture | pages [23] -->
m

<!-- b002753 | furniture | pages [23] -->
m

<!-- b002754 | furniture | pages [23] -->
m

<!-- b002755 | furniture | pages [23] -->
m

<!-- b002756 | furniture | pages [23] -->
m

<!-- b002757 | furniture | pages [23] -->
m

<!-- b002758 | furniture | pages [23] -->
m

<!-- b002759 | furniture | pages [23] -->
m

<!-- b002760 | furniture | pages [23] -->
m

<!-- b002761 | furniture | pages [23] -->
m

<!-- b002762 | furniture | pages [23] -->
m

<!-- b002763 | furniture | pages [23] -->
m

<!-- b002764 | furniture | pages [23] -->
m

<!-- b002765 | furniture | pages [23] -->
m

<!-- b002766 | furniture | pages [23] -->
m

<!-- b002767 | furniture | pages [23] -->
m

<!-- b002768 | furniture | pages [23] -->
m

<!-- b002769 | furniture | pages [23] -->
m

<!-- b002770 | furniture | pages [23] -->
m

<!-- b002771 | furniture | pages [23] -->
m

<!-- b002772 | furniture | pages [23] -->
m

<!-- b002773 | furniture | pages [23] -->
m

<!-- b002774 | furniture | pages [23] -->
m

<!-- b002775 | furniture | pages [23] -->
m

<!-- b002776 | furniture | pages [23] -->
m

<!-- b002777 | furniture | pages [23] -->
m

<!-- b002778 | furniture | pages [23] -->
m

<!-- b002779 | furniture | pages [23] -->
m

<!-- b002780 | furniture | pages [23] -->
m

<!-- b002781 | furniture | pages [23] -->
m

<!-- b002782 | furniture | pages [23] -->
m

<!-- b002783 | furniture | pages [23] -->
m

<!-- b002784 | furniture | pages [23] -->
m

<!-- b002785 | furniture | pages [23] -->
m

<!-- b002786 | furniture | pages [23] -->
m

<!-- b002787 | furniture | pages [23] -->
m

<!-- b002788 | furniture | pages [23] -->
m

<!-- b002789 | furniture | pages [23] -->
m

<!-- b002790 | furniture | pages [23] -->
m

<!-- b002791 | furniture | pages [23] -->
m

<!-- b002792 | furniture | pages [23] -->
m

<!-- b002793 | furniture | pages [23] -->
m

<!-- b002794 | furniture | pages [23] -->
m

<!-- b002795 | furniture | pages [23] -->
m

<!-- b002796 | furniture | pages [23] -->
m

<!-- b002797 | furniture | pages [23] -->
m

<!-- b002798 | furniture | pages [23] -->
m

<!-- b002799 | furniture | pages [23] -->
m

<!-- b002800 | furniture | pages [23] -->
m

<!-- b002801 | furniture | pages [23] -->
m

<!-- b002802 | furniture | pages [23] -->
m

<!-- b002803 | furniture | pages [23] -->
m

<!-- b002804 | furniture | pages [23] -->
m

<!-- b002805 | furniture | pages [23] -->
m

<!-- b002806 | furniture | pages [23] -->
m

<!-- b002807 | furniture | pages [23] -->
m

<!-- b002808 | furniture | pages [23] -->
m

<!-- b002809 | furniture | pages [23] -->
m

<!-- b002810 | furniture | pages [23] -->
m

<!-- b002811 | furniture | pages [23] -->
m

<!-- b002812 | furniture | pages [23] -->
m

<!-- b002813 | furniture | pages [23] -->
m

<!-- b002814 | furniture | pages [23] -->
m

<!-- b002815 | furniture | pages [23] -->
m

<!-- b002816 | furniture | pages [23] -->
m

<!-- b002817 | furniture | pages [23] -->
m

<!-- b002818 | furniture | pages [23] -->
m

<!-- b002819 | furniture | pages [23] -->
m

<!-- b002820 | furniture | pages [23] -->
m

<!-- b002821 | furniture | pages [23] -->
m

<!-- b002822 | furniture | pages [23] -->
m

<!-- b002823 | furniture | pages [23] -->
m

<!-- b002824 | furniture | pages [23] -->
m

<!-- b002825 | furniture | pages [23] -->
m

<!-- b002826 | furniture | pages [23] -->
m

<!-- b002827 | furniture | pages [23] -->
m

<!-- b002828 | furniture | pages [23] -->
m

<!-- b002829 | furniture | pages [23] -->
m

<!-- b002830 | furniture | pages [23] -->
m

<!-- b002831 | furniture | pages [23] -->
m

<!-- b002832 | furniture | pages [23] -->
m

<!-- b002833 | furniture | pages [23] -->
m

<!-- b002834 | furniture | pages [23] -->
m

<!-- b002835 | furniture | pages [23] -->
m

<!-- b002836 | furniture | pages [23] -->
m

<!-- b002837 | furniture | pages [23] -->
m

<!-- b002838 | furniture | pages [23] -->
m

<!-- b002839 | furniture | pages [23] -->
m

<!-- b002840 | furniture | pages [23] -->
m

<!-- b002841 | furniture | pages [23] -->
m

<!-- b002842 | furniture | pages [23] -->
m

<!-- b002843 | furniture | pages [23] -->
m

<!-- b002844 | furniture | pages [23] -->
m

<!-- b002845 | furniture | pages [23] -->
m

<!-- b002846 | furniture | pages [23] -->
m

<!-- b002847 | furniture | pages [23] -->
m

<!-- b002848 | furniture | pages [23] -->
m

<!-- b002849 | furniture | pages [23] -->
m

<!-- b002850 | furniture | pages [23] -->
m

<!-- b002851 | furniture | pages [23] -->
m

<!-- b002852 | furniture | pages [23] -->
m

<!-- b002853 | furniture | pages [23] -->
m

<!-- b002854 | furniture | pages [23] -->
m

<!-- b002855 | furniture | pages [23] -->
m

<!-- b002856 | furniture | pages [23] -->
m

<!-- b002857 | furniture | pages [23] -->
m

<!-- b002858 | furniture | pages [23] -->
m

<!-- b002859 | furniture | pages [23] -->
m

<!-- b002860 | furniture | pages [23] -->
m

<!-- b002861 | furniture | pages [23] -->
m

<!-- b002862 | furniture | pages [23] -->
m

<!-- b002863 | furniture | pages [23] -->
m

<!-- b002864 | furniture | pages [23] -->
m

<!-- b002865 | furniture | pages [23] -->
m

<!-- b002866 | furniture | pages [23] -->
m

<!-- b002867 | furniture | pages [23] -->
m

<!-- b002868 | furniture | pages [23] -->
m

<!-- b002869 | furniture | pages [23] -->
m

<!-- b002870 | furniture | pages [23] -->
m

<!-- b002871 | furniture | pages [23] -->
m

<!-- b002872 | furniture | pages [23] -->
m

<!-- b002873 | furniture | pages [23] -->
m

<!-- b002874 | furniture | pages [23] -->
m

<!-- b002875 | furniture | pages [23] -->
m

<!-- b002876 | furniture | pages [23] -->
m

<!-- b002877 | furniture | pages [23] -->
m

<!-- b002878 | furniture | pages [23] -->
m

<!-- b002879 | furniture | pages [23] -->
m

<!-- b002880 | furniture | pages [23] -->
m

<!-- b002881 | furniture | pages [23] -->
m

<!-- b002882 | furniture | pages [23] -->
m

<!-- b002883 | furniture | pages [23] -->
m

<!-- b002884 | furniture | pages [23] -->
m

<!-- b002885 | furniture | pages [23] -->
m

<!-- b002886 | furniture | pages [23] -->
m

<!-- b002887 | furniture | pages [23] -->
m

<!-- b002888 | furniture | pages [23] -->
m

<!-- b002889 | furniture | pages [23] -->
m

<!-- b002890 | furniture | pages [23] -->
m

<!-- b002891 | furniture | pages [23] -->
m

<!-- b002892 | furniture | pages [23] -->
m

<!-- b002893 | furniture | pages [23] -->
m

<!-- b002894 | furniture | pages [23] -->
m

<!-- b002895 | furniture | pages [23] -->
m

<!-- b002896 | furniture | pages [23] -->
m

<!-- b002897 | furniture | pages [23] -->
m

<!-- b002898 | furniture | pages [23] -->
m

<!-- b002899 | furniture | pages [23] -->
m

<!-- b002900 | furniture | pages [23] -->
m

<!-- b002901 | furniture | pages [23] -->
m

<!-- b002902 | furniture | pages [23] -->
m

<!-- b002903 | furniture | pages [23] -->
m

<!-- b002904 | furniture | pages [23] -->
m

<!-- b002905 | furniture | pages [23] -->
m

<!-- b002906 | furniture | pages [23] -->
m

<!-- b002907 | furniture | pages [23] -->
m

<!-- b002908 | furniture | pages [23] -->
m

<!-- b002909 | furniture | pages [23] -->
m

<!-- b002910 | furniture | pages [23] -->
m

<!-- b002911 | furniture | pages [23] -->
m

<!-- b002912 | furniture | pages [23] -->
m

<!-- b002913 | furniture | pages [23] -->
m

<!-- b002914 | furniture | pages [23] -->
m

<!-- b002915 | furniture | pages [24] -->
Team # 2500836                                                                   Page 23 of 25

<!-- b002916 | heading | pages [24] -->
References

<!-- b002917 | references | pages [24] -->
[1]  Zhang, Qingyuan. Modern Chinese Common Words Dictionary. Chengdu: Sichuan People's

<!-- b002918 | references | pages [24] -->
Publishing House, 1992. 368.

<!-- b002919 | references | pages [24] -->
[2]  What Are the Particular Considerations for Steps in Ancient Chinese Architecture? 163.com,

<!-- b002920 | references | pages [24] -->
https://m.163.com/dy/article/G0SC3KCH0518I16I.html?spss=adap_pc.

<!-- b002921 | references | pages [24] -->
[3]  Archard, J. F. Contact and Rubbing of Flat Surfaces. Journal of Applied Physics, vol. 24, no. 9,

<!-- b002922 | references | pages [24] -->
1953, pp. 981-988. https://doi.org/10.1063/1.1721448.

<!-- b002923 | references | pages [24] -->
[4]  https://leaningtowerpisa.com/history

<!-- b002924 | references | pages [24] -->
[5]  Karaca, Z., Günes Yılmaz, N., and Goktan, R. M. Abrasion Wear Characterization of Some

<!-- b002925 | references | pages [24] -->
Selected Stone Flooring Materials with Respect to Contact Load. Construction and Building

<!-- b002926 | references | pages [24] -->
Materials, vol. 36, 2012, pp. 520-526. https://doi.org/10.1016/j.conbuildmat.2012.06.004.

<!-- b002927 | references | pages [24] -->
[6]  Helbing, D. Gas-Kinetic Derivation of Navier-Stokes-Like Traffic Equations. Physical Review E,

<!-- b002928 | references | pages [24] -->
vol. 53, no. 3, 1996, pp. 2366. https://arxiv.org/pdf/cond-mat/9806026.

<!-- b002929 | references | pages [24] -->
[7]  Schadschneider, A., and Seyfried, A. Pedestrian and Evacuation Dynamics. Encyclopedia of

<!-- b002930 | references | pages [24] -->
Complexity and Systems Science, 2012, pp. 6889-6902. Springer.

<!-- b002931 | references | pages [24] -->
[8]  Yue Xueqing, Wang Hua, Liu Lecun, et al. Friction and Wear Properties of Graphite-Coated Iron

<!-- b002932 | references | pages [24] -->
Nanoparticles Prepared by Ball Milling and Annealing. Mechanical Engineering Materials,

<!-- b002933 | references | pages [24] -->
2015, 39(05): 73-76+80.

<!-- b002934 | references | pages [24] -->
[9]  Yang Na, Zhang Chong, Li Tianhao. Design of a Crack Monitoring System for Ancient Chinese

<!-- b002935 | references | pages [24] -->
Wooden Architecture Based on Drones and Computer Vision. Engineering Mechanics, 2021,

<!-- b002936 | references | pages [24] -->
38(03): 27-39.

<!-- b002937 | references | pages [24] -->
[10]  Parameters of Carara Quarry: https://www.stonecontact.com/bianco-carrara-marble/s188.

<!-- b002938 | references | pages [24] -->
[11]  https://jingyan.baidu.com/article/3f16e00303e3576491c1039d.html

<!-- b002939 | references | pages [24] -->
关注数学模型

<!-- b002940 | furniture | pages [24] -->
2

<!-- b002941 | furniture | pages [24] -->
MATHmodels

<!-- b002942 | furniture | pages [24] -->
获取更多资讯

<!-- b002943 | furniture | pages [25] -->
Team # 2500836

<!-- b002944 | furniture | pages [25] -->
Page 24 of 25

<!-- b002945 | heading | pages [25] -->
Appendix

<!-- b002946 | prose | pages [25] -->
微信公众号：数学模型 微信号：MATHmodels

<!-- b002947 | caption | pages [25] -->
Figure 22: Location of the Leaning Tower of Pisa and the Carrara quarry

<!-- b002948 | prose | pages [25] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b002949 | furniture | pages [25] -->
m

<!-- b002950 | furniture | pages [25] -->
m

<!-- b002951 | furniture | pages [25] -->
m

<!-- b002952 | furniture | pages [25] -->
m

<!-- b002953 | furniture | pages [25] -->
m

<!-- b002954 | furniture | pages [25] -->
m

<!-- b002955 | furniture | pages [25] -->
m

<!-- b002956 | furniture | pages [25] -->
m

<!-- b002957 | furniture | pages [25] -->
m

<!-- b002958 | furniture | pages [25] -->
m

<!-- b002959 | furniture | pages [25] -->
m

<!-- b002960 | furniture | pages [25] -->
m

<!-- b002961 | furniture | pages [25] -->
m

<!-- b002962 | furniture | pages [25] -->
m

<!-- b002963 | furniture | pages [25] -->
m

<!-- b002964 | furniture | pages [25] -->
m

<!-- b002965 | furniture | pages [25] -->
m

<!-- b002966 | furniture | pages [25] -->
m

<!-- b002967 | furniture | pages [25] -->
m

<!-- b002968 | furniture | pages [25] -->
m

<!-- b002969 | furniture | pages [25] -->
m

<!-- b002970 | furniture | pages [25] -->
m

<!-- b002971 | furniture | pages [25] -->
m

<!-- b002972 | furniture | pages [25] -->
m

<!-- b002973 | furniture | pages [25] -->
m

<!-- b002974 | furniture | pages [25] -->
m

<!-- b002975 | furniture | pages [25] -->
m

<!-- b002976 | furniture | pages [25] -->
m

<!-- b002977 | furniture | pages [25] -->
m

<!-- b002978 | furniture | pages [25] -->
m

<!-- b002979 | furniture | pages [25] -->
m

<!-- b002980 | furniture | pages [25] -->
m

<!-- b002981 | furniture | pages [25] -->
m

<!-- b002982 | furniture | pages [25] -->
m

<!-- b002983 | furniture | pages [25] -->
m

<!-- b002984 | furniture | pages [25] -->
m

<!-- b002985 | furniture | pages [25] -->
m

<!-- b002986 | furniture | pages [25] -->
m

<!-- b002987 | furniture | pages [25] -->
m

<!-- b002988 | furniture | pages [25] -->
m

<!-- b002989 | furniture | pages [25] -->
m

<!-- b002990 | furniture | pages [25] -->
m

<!-- b002991 | furniture | pages [25] -->
m

<!-- b002992 | furniture | pages [25] -->
m

<!-- b002993 | furniture | pages [25] -->
m

<!-- b002994 | furniture | pages [25] -->
m

<!-- b002995 | furniture | pages [25] -->
m

<!-- b002996 | furniture | pages [25] -->
m

<!-- b002997 | furniture | pages [25] -->
m

<!-- b002998 | furniture | pages [25] -->
m

<!-- b002999 | furniture | pages [25] -->
m

<!-- b003000 | furniture | pages [25] -->
m

<!-- b003001 | furniture | pages [25] -->
m

<!-- b003002 | furniture | pages [25] -->
m

<!-- b003003 | furniture | pages [25] -->
m

<!-- b003004 | furniture | pages [25] -->
m

<!-- b003005 | furniture | pages [25] -->
m

<!-- b003006 | furniture | pages [25] -->
m

<!-- b003007 | furniture | pages [25] -->
m

<!-- b003008 | furniture | pages [25] -->
m

<!-- b003009 | furniture | pages [25] -->
m

<!-- b003010 | furniture | pages [25] -->
m

<!-- b003011 | furniture | pages [25] -->
m

<!-- b003012 | furniture | pages [25] -->
m

<!-- b003013 | furniture | pages [25] -->
m

<!-- b003014 | furniture | pages [25] -->
m

<!-- b003015 | furniture | pages [25] -->
m

<!-- b003016 | furniture | pages [25] -->
m

<!-- b003017 | furniture | pages [25] -->
m

<!-- b003018 | furniture | pages [25] -->
m

<!-- b003019 | furniture | pages [25] -->
m

<!-- b003020 | furniture | pages [25] -->
m

<!-- b003021 | furniture | pages [25] -->
m

<!-- b003022 | furniture | pages [25] -->
m

<!-- b003023 | furniture | pages [25] -->
m

<!-- b003024 | furniture | pages [25] -->
m

<!-- b003025 | furniture | pages [25] -->
m

<!-- b003026 | furniture | pages [25] -->
m

<!-- b003027 | furniture | pages [25] -->
m

<!-- b003028 | furniture | pages [25] -->
m

<!-- b003029 | furniture | pages [25] -->
m

<!-- b003030 | furniture | pages [25] -->
m

<!-- b003031 | furniture | pages [25] -->
m

<!-- b003032 | furniture | pages [25] -->
m

<!-- b003033 | furniture | pages [25] -->
m

<!-- b003034 | furniture | pages [25] -->
m

<!-- b003035 | furniture | pages [25] -->
m

<!-- b003036 | furniture | pages [25] -->
m

<!-- b003037 | furniture | pages [25] -->
m

<!-- b003038 | furniture | pages [25] -->
m

<!-- b003039 | furniture | pages [25] -->
m

<!-- b003040 | furniture | pages [25] -->
m

<!-- b003041 | furniture | pages [25] -->
m

<!-- b003042 | furniture | pages [25] -->
m

<!-- b003043 | furniture | pages [25] -->
m

<!-- b003044 | furniture | pages [25] -->
m

<!-- b003045 | furniture | pages [25] -->
m

<!-- b003046 | furniture | pages [25] -->
m

<!-- b003047 | furniture | pages [25] -->
m

<!-- b003048 | furniture | pages [25] -->
m

<!-- b003049 | furniture | pages [25] -->
m

<!-- b003050 | furniture | pages [25] -->
m

<!-- b003051 | furniture | pages [25] -->
m

<!-- b003052 | furniture | pages [25] -->
m

<!-- b003053 | furniture | pages [25] -->
m

<!-- b003054 | furniture | pages [25] -->
m

<!-- b003055 | furniture | pages [25] -->
m

<!-- b003056 | furniture | pages [25] -->
m

<!-- b003057 | furniture | pages [25] -->
m

<!-- b003058 | furniture | pages [25] -->
m

<!-- b003059 | furniture | pages [25] -->
m

<!-- b003060 | furniture | pages [25] -->
m

<!-- b003061 | furniture | pages [25] -->
m

<!-- b003062 | furniture | pages [25] -->
m

<!-- b003063 | furniture | pages [25] -->
m

<!-- b003064 | furniture | pages [25] -->
m

<!-- b003065 | furniture | pages [25] -->
m

<!-- b003066 | furniture | pages [25] -->
m

<!-- b003067 | furniture | pages [25] -->
m

<!-- b003068 | furniture | pages [25] -->
m

<!-- b003069 | furniture | pages [25] -->
m

<!-- b003070 | furniture | pages [25] -->
m

<!-- b003071 | furniture | pages [25] -->
m

<!-- b003072 | furniture | pages [25] -->
m

<!-- b003073 | furniture | pages [25] -->
m

<!-- b003074 | furniture | pages [25] -->
m

<!-- b003075 | furniture | pages [25] -->
m

<!-- b003076 | furniture | pages [25] -->
m

<!-- b003077 | furniture | pages [25] -->
m

<!-- b003078 | furniture | pages [25] -->
m

<!-- b003079 | furniture | pages [25] -->
m

<!-- b003080 | furniture | pages [25] -->
m

<!-- b003081 | furniture | pages [25] -->
m

<!-- b003082 | furniture | pages [25] -->
m

<!-- b003083 | furniture | pages [25] -->
m

<!-- b003084 | furniture | pages [25] -->
m

<!-- b003085 | furniture | pages [25] -->
m

<!-- b003086 | furniture | pages [25] -->
m

<!-- b003087 | furniture | pages [25] -->
m

<!-- b003088 | furniture | pages [25] -->
m

<!-- b003089 | furniture | pages [25] -->
m

<!-- b003090 | furniture | pages [25] -->
m

<!-- b003091 | furniture | pages [25] -->
m

<!-- b003092 | furniture | pages [25] -->
m

<!-- b003093 | furniture | pages [25] -->
m

<!-- b003094 | furniture | pages [25] -->
m

<!-- b003095 | furniture | pages [25] -->
m

<!-- b003096 | furniture | pages [25] -->
m

<!-- b003097 | furniture | pages [25] -->
m

<!-- b003098 | furniture | pages [25] -->
m

<!-- b003099 | furniture | pages [25] -->
m

<!-- b003100 | furniture | pages [25] -->
m

<!-- b003101 | furniture | pages [25] -->
m

<!-- b003102 | furniture | pages [25] -->
m

<!-- b003103 | furniture | pages [25] -->
m

<!-- b003104 | furniture | pages [25] -->
m

<!-- b003105 | furniture | pages [25] -->
m

<!-- b003106 | furniture | pages [25] -->
m

<!-- b003107 | furniture | pages [25] -->
m

<!-- b003108 | furniture | pages [25] -->
m

<!-- b003109 | furniture | pages [25] -->
m

<!-- b003110 | furniture | pages [25] -->
m

<!-- b003111 | furniture | pages [25] -->
m

<!-- b003112 | furniture | pages [25] -->
m

<!-- b003113 | furniture | pages [25] -->
m

<!-- b003114 | furniture | pages [25] -->
m

<!-- b003115 | furniture | pages [25] -->
m

<!-- b003116 | furniture | pages [25] -->
m

<!-- b003117 | furniture | pages [25] -->
m

<!-- b003118 | furniture | pages [25] -->
m

<!-- b003119 | furniture | pages [25] -->
m

<!-- b003120 | furniture | pages [25] -->
m

<!-- b003121 | furniture | pages [25] -->
m

<!-- b003122 | furniture | pages [25] -->
m

<!-- b003123 | furniture | pages [25] -->
m

<!-- b003124 | furniture | pages [25] -->
m

<!-- b003125 | furniture | pages [25] -->
m

<!-- b003126 | furniture | pages [25] -->
m

<!-- b003127 | furniture | pages [25] -->
m

<!-- b003128 | furniture | pages [25] -->
m

<!-- b003129 | furniture | pages [25] -->
m

<!-- b003130 | furniture | pages [25] -->
m

<!-- b003131 | furniture | pages [25] -->
m

<!-- b003132 | furniture | pages [25] -->
m

<!-- b003133 | furniture | pages [25] -->
m

<!-- b003134 | furniture | pages [25] -->
m

<!-- b003135 | furniture | pages [25] -->
m

<!-- b003136 | furniture | pages [25] -->
m

<!-- b003137 | furniture | pages [25] -->
m

<!-- b003138 | furniture | pages [25] -->
m

<!-- b003139 | furniture | pages [25] -->
m

<!-- b003140 | furniture | pages [25] -->
m

<!-- b003141 | furniture | pages [25] -->
m

<!-- b003142 | furniture | pages [25] -->
m

<!-- b003143 | furniture | pages [25] -->
m

<!-- b003144 | furniture | pages [25] -->
m

<!-- b003145 | furniture | pages [25] -->
m

<!-- b003146 | furniture | pages [25] -->
m

<!-- b003147 | furniture | pages [25] -->
m

<!-- b003148 | furniture | pages [25] -->
m

<!-- b003149 | furniture | pages [25] -->
m

<!-- b003150 | furniture | pages [25] -->
m

<!-- b003151 | furniture | pages [25] -->
m

<!-- b003152 | furniture | pages [25] -->
m

<!-- b003153 | furniture | pages [25] -->
m

<!-- b003154 | furniture | pages [25] -->
m

<!-- b003155 | furniture | pages [25] -->
m

<!-- b003156 | furniture | pages [25] -->
m

<!-- b003157 | furniture | pages [25] -->
m

<!-- b003158 | furniture | pages [25] -->
m

<!-- b003159 | furniture | pages [25] -->
m

<!-- b003160 | furniture | pages [25] -->
m

<!-- b003161 | furniture | pages [25] -->
m

<!-- b003162 | furniture | pages [25] -->
m

<!-- b003163 | furniture | pages [25] -->
m

<!-- b003164 | furniture | pages [25] -->
m

<!-- b003165 | furniture | pages [25] -->
m

<!-- b003166 | furniture | pages [25] -->
m

<!-- b003167 | furniture | pages [25] -->
m

<!-- b003168 | furniture | pages [25] -->
m

<!-- b003169 | furniture | pages [25] -->
m

<!-- b003170 | furniture | pages [25] -->
m

<!-- b003171 | furniture | pages [25] -->
m

<!-- b003172 | furniture | pages [25] -->
m

<!-- b003173 | furniture | pages [25] -->
m

<!-- b003174 | furniture | pages [25] -->
m

<!-- b003175 | furniture | pages [25] -->
m

<!-- b003176 | furniture | pages [25] -->
m

<!-- b003177 | furniture | pages [25] -->
m

<!-- b003178 | furniture | pages [25] -->
m

<!-- b003179 | furniture | pages [25] -->
m

<!-- b003180 | furniture | pages [25] -->
m

<!-- b003181 | furniture | pages [25] -->
m

<!-- b003182 | furniture | pages [25] -->
m

<!-- b003183 | furniture | pages [25] -->
m

<!-- b003184 | furniture | pages [25] -->
m

<!-- b003185 | furniture | pages [25] -->
m

<!-- b003186 | furniture | pages [25] -->
m

<!-- b003187 | furniture | pages [25] -->
m

<!-- b003188 | furniture | pages [25] -->
m

<!-- b003189 | furniture | pages [25] -->
m

<!-- b003190 | furniture | pages [25] -->
m

<!-- b003191 | furniture | pages [25] -->
m

<!-- b003192 | furniture | pages [25] -->
m

<!-- b003193 | furniture | pages [25] -->
m

<!-- b003194 | furniture | pages [25] -->
m

<!-- b003195 | furniture | pages [25] -->
m

<!-- b003196 | furniture | pages [25] -->
m

<!-- b003197 | furniture | pages [25] -->
m

<!-- b003198 | furniture | pages [25] -->
m

<!-- b003199 | furniture | pages [25] -->
m

<!-- b003200 | furniture | pages [25] -->
m

<!-- b003201 | furniture | pages [25] -->
m

<!-- b003202 | furniture | pages [25] -->
m

<!-- b003203 | furniture | pages [25] -->
m

<!-- b003204 | furniture | pages [25] -->
m

<!-- b003205 | furniture | pages [25] -->
m

<!-- b003206 | furniture | pages [25] -->
m

<!-- b003207 | furniture | pages [25] -->
m

<!-- b003208 | furniture | pages [25] -->
m

<!-- b003209 | furniture | pages [25] -->
m

<!-- b003210 | furniture | pages [25] -->
m

<!-- b003211 | furniture | pages [25] -->
m

<!-- b003212 | furniture | pages [25] -->
m

<!-- b003213 | furniture | pages [25] -->
m

<!-- b003214 | furniture | pages [25] -->
m

<!-- b003215 | furniture | pages [25] -->
m

<!-- b003216 | furniture | pages [25] -->
m

<!-- b003217 | furniture | pages [25] -->
m

<!-- b003218 | furniture | pages [25] -->
m

<!-- b003219 | furniture | pages [25] -->
m

<!-- b003220 | furniture | pages [25] -->
m

<!-- b003221 | furniture | pages [25] -->
m

<!-- b003222 | furniture | pages [25] -->
m

<!-- b003223 | furniture | pages [25] -->
m

<!-- b003224 | furniture | pages [25] -->
m

<!-- b003225 | furniture | pages [25] -->
m

<!-- b003226 | furniture | pages [25] -->
m

<!-- b003227 | furniture | pages [25] -->
m

<!-- b003228 | furniture | pages [25] -->
m

<!-- b003229 | furniture | pages [25] -->
m

<!-- b003230 | furniture | pages [25] -->
m

<!-- b003231 | furniture | pages [25] -->
m

<!-- b003232 | furniture | pages [25] -->
m

<!-- b003233 | furniture | pages [25] -->
m

<!-- b003234 | furniture | pages [25] -->
m

<!-- b003235 | furniture | pages [25] -->
m

<!-- b003236 | furniture | pages [25] -->
m

<!-- b003237 | furniture | pages [25] -->
m

<!-- b003238 | furniture | pages [25] -->
m

<!-- b003239 | furniture | pages [25] -->
m

<!-- b003240 | furniture | pages [25] -->
m

<!-- b003241 | furniture | pages [25] -->
m

<!-- b003242 | furniture | pages [25] -->
m

<!-- b003243 | furniture | pages [25] -->
m

<!-- b003244 | furniture | pages [25] -->
m

<!-- b003245 | furniture | pages [25] -->
m

<!-- b003246 | furniture | pages [25] -->
m

<!-- b003247 | furniture | pages [25] -->
m

<!-- b003248 | furniture | pages [25] -->
m

<!-- b003249 | furniture | pages [25] -->
m

<!-- b003250 | furniture | pages [25] -->
m

<!-- b003251 | furniture | pages [25] -->
m

<!-- b003252 | furniture | pages [25] -->
m

<!-- b003253 | furniture | pages [25] -->
m

<!-- b003254 | furniture | pages [25] -->
m

<!-- b003255 | furniture | pages [25] -->
m

<!-- b003256 | furniture | pages [25] -->
m

<!-- b003257 | furniture | pages [25] -->
m

<!-- b003258 | furniture | pages [25] -->
m

<!-- b003259 | furniture | pages [25] -->
m

<!-- b003260 | furniture | pages [25] -->
m

<!-- b003261 | furniture | pages [25] -->
m

<!-- b003262 | furniture | pages [25] -->
m

<!-- b003263 | furniture | pages [25] -->
m

<!-- b003264 | furniture | pages [25] -->
m

<!-- b003265 | furniture | pages [25] -->
m

<!-- b003266 | furniture | pages [25] -->
m

<!-- b003267 | furniture | pages [25] -->
m

<!-- b003268 | furniture | pages [25] -->
m

<!-- b003269 | furniture | pages [25] -->
m

<!-- b003270 | furniture | pages [25] -->
m

<!-- b003271 | furniture | pages [25] -->
m

<!-- b003272 | furniture | pages [25] -->
m
